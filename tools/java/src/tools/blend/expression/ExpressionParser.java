package tools.blend.expression;

import java.util.ArrayList;
import java.util.List;

import tools.code.CodeLine;
import tools.code.CodeLineInputStream;

/**
 * These functions scan and parse a textual representation of a logic equation expressed
 * in a C-like notation. The equation may consist of logic operation AND (&&), OR (||),
 * and NOT (!) along with comparison operations like ">" and "<=". Parenthesis may be
 * used to group the order of operation.
 * 
 * The functions here are a two-step process. In the first step an expression (example
 * shown below) is scanned into functional tokens. The scanning handles quotes and
 * escaped characters. The scanning recognizes operators and parenthesis.
 * 
 * In the second step the sub-expressions are grown into a tree of tokens ready for
 * processing at even higher levels.
 * 
 * Example expression:
 * A==3 && (B==0x4 || !(C!='\n' && D>6))
 * 
 * (1) Scanned into tokens (separated here by spaces)
 * A == 3 && ( B == 0x4 || ! ( C != '\n' && D > 6 ) )
 * 
 * (2) Parsed into a tree of tokens
 * A == 3 &&  *
 *            B == 0x4 || !*                        
 *                         C != '\n' && D>6
 */
public final class ExpressionParser 
{
	
	static final String LOGIC_TOKENS_SET = "&|"; // "&&", "||"
	
	// Since NOT (!) is a unary operator it is not included in the logical-grouping operators
	// above. It is a token type all to itself. It may only appear before an open parenthesis.
	
	static final String COMPARE_TOKENS_SET = "=!<>"; // "==", "!=", "<=", ">=", "<" ,">"
	
	/**
	 * This function grows the flat list of parse tokens into a tree of parse tokens.
	 * This allows for easier processing in a context where a parse-token and a 
	 * list-of-parse-tokens are interchangeable.
	 * @param parseTokens the list to grow (input and output to function)
	 * @throws ExpressionException if there is a syntax error
	 */
	public static void parseExpressionTree(List<ParseToken> parseTokens) throws ExpressionException
	{
		
		// The return list of tokens and sub-lists
		List<ParseToken> expression = new ArrayList<ParseToken>();
		
		int pos=0;
		while(pos<parseTokens.size()) {
			ParseToken pt = parseTokens.get(pos++);
			if(pt.tokenType==ParseTokenType.OPEN) {
				// Build the sub list from this OPEN to matching CLOSE
				pt.subList = new ArrayList<ParseToken>();
				pt.tokenType = ParseTokenType.SUBLIST;
				int parenLevel = 1;
				while(true) {
					ParseToken ps = parseTokens.get(pos++);
					if(ps.tokenType==ParseTokenType.CLOSE) {
						--parenLevel;
						if(parenLevel==0) break;
					}
					if(ps.tokenType==ParseTokenType.OPEN) {
						++parenLevel;
					}
					pt.subList.add(ps);					
				}				
				// Recursively process the sublist
				
				parseExpressionTree(pt.subList);								
				expression.add(pt); 
			} else {
				expression.add(pt);
			}
		}
		
		parseTokens.clear();
		parseTokens.addAll(expression);
	}
	
	/**
	 * This function scans an expression into a list of parse tokens. The scanner handles escaped
	 * characters and quotes/ticks and counts open/close parenthesis levels
	 * @param expression the expression all in a string
	 * @param filename the filename to use in ExpressionExceptions
	 * @param lineNumber the line number to use in ExpressionExceptions
	 * @return the flat list of parse tokens
	 * @throws ExpressionException if there is a syntax error
	 */
	public static List<ParseToken> scanExpression(String expression, 
			String filename, int lineNumber) throws ExpressionException
	{
		CodeLine tmp = new CodeLine(expression,filename,lineNumber);
		List<CodeLine> tmpList = new ArrayList<CodeLine>();
		tmpList.add(tmp);
		CodeLineInputStream clis = new CodeLineInputStream(tmpList,0,0);
		return scanExpression(clis);
	}
	
	/**
	 * This function scans an expression into a list of parse tokens. The scanner handles escaped
	 * characters and quotes/ticks and counts open/close parenthesis levels
	 * @param clis the input stream of CodeLines
	 * @return the flat list of parse tokens
	 * @throws ExpressionException if there is a syntax error
	 */
	public static List<ParseToken> scanExpression(CodeLineInputStream clis) throws ExpressionException
	{
		
		List<ParseToken> parseTokens = new ArrayList<ParseToken>();
		
		// TODO ick, this needs refactoring. The goal is to parse the stream into a list of tokens.
		// I have learned a little about context free grammars and such. This is just an ugly brute force.
		
		int parenLevel = 0;
		boolean escapeMode = false;
		char waitClose = 0;

		StringBuffer currentToken = null;
		ParseTokenType currentTokenType = ParseTokenType.SYMBOL;
		
		CodeLine lastOpenCodeLine=null;
		int lastOpenPosition=-1;
				
		while(true) {
			
			// Get next character (we aren't expecting an end of stream)
			int n = clis.read();
			if(n<0) {
				throw new ExpressionException("Missing close parenthesis",lastOpenCodeLine,lastOpenPosition);
			}
			
			// If a character was just escaped then add it to the current token
			if(escapeMode) {
				// We made sure we had a running token when we entered escape mode
				currentToken.append((char)n);
				escapeMode=false;
				continue;
			}
						
			// Check starting an escape sequence. Ignore the escape itself.
			if(n=='\\') {
				// Only a symbol can begin with an escaped character
				if(currentToken==null) {
					currentToken = new StringBuffer();
					currentTokenType = ParseTokenType.SYMBOL;					
				}
				escapeMode=true;
				continue;
			}			
			
			// If we are in a quote (or tick) then add blindly until we reach the end of the sequence
			if(waitClose!=0) {
				if(n==waitClose) {
					waitClose=0;
				}
				currentToken.append((char)n);
				continue;
			}
						
			// Check if we are starting a quoted sequence
			if(n=='\'' || n=='"') {
				
				// End any running token
				if(currentTokenType!=ParseTokenType.SYMBOL) {
					ParseToken pt = new ParseToken();
					pt.token = currentToken.toString();
					pt.tokenType = currentTokenType;
					pt.position = clis.getCurrentPosition();
					pt.codeLine = clis.getCurrentLine();
					parseTokens.add(pt);
					currentToken = null;
				}
				
				waitClose = (char)n;
				// Quotes (and ticks) are only in symbols
				if(currentToken==null) {
					currentToken = new StringBuffer();
					currentTokenType = ParseTokenType.SYMBOL;					
				} 
				currentToken.append((char)n);
				continue;				
			}	
			
			// New lines and spaces are ignored, but they do end a token
			if(n=='\n' || n==' ' || n=='\t') {
				if(currentToken!=null) {
					ParseToken pt = new ParseToken();
					pt.token = currentToken.toString();
					pt.tokenType = currentTokenType;
					pt.position = clis.getCurrentPosition();
					pt.codeLine = clis.getCurrentLine();
					parseTokens.add(pt);
					currentToken = null;
				}
				continue;
			}
			
			// Close paren ... this could be the end of the expression
			if(n==')') {
				// Any running token is done
				if(currentToken!=null) {
					ParseToken pt = new ParseToken();
					pt.token = currentToken.toString();
					pt.tokenType = currentTokenType;
					pt.position = clis.getCurrentPosition();
					pt.codeLine = clis.getCurrentLine();
					parseTokens.add(pt);
					currentToken = null;
				}
				// Add the close token
				ParseToken pt = new ParseToken();
				pt.token = ")";
				pt.tokenType = ParseTokenType.CLOSE;
				pt.position = clis.getCurrentPosition();
				pt.codeLine = clis.getCurrentLine();
				parseTokens.add(pt);
				
				--parenLevel;
				if(parenLevel<0) {
					// Special case of close but no open
					throw new ExpressionException("No open parenthesis",pt.codeLine,pt.position);					
				}
				if(parenLevel==0) {
					// We reached the end of the expression ... no error
					return parseTokens;					
				}
				continue;
			}
			
			// Open paren ... just count
			if(n=='(') {
				// Any running token is done
				if(currentToken!=null) {
					ParseToken pt = new ParseToken();
					pt.token = currentToken.toString();
					pt.tokenType = currentTokenType;
					pt.position = clis.getCurrentPosition();
					pt.codeLine = clis.getCurrentLine();
					parseTokens.add(pt);
					lastOpenCodeLine = pt.codeLine;
					lastOpenPosition = pt.position;
					currentToken = null;
				}
				// Start the new token
				ParseToken pt = new ParseToken();
				pt.token = "(";
				pt.tokenType = ParseTokenType.OPEN;
				pt.position = clis.getCurrentPosition();
				pt.codeLine = clis.getCurrentLine();
				parseTokens.add(pt);
				
				++parenLevel;
				continue;
			}
			
			
			// This is a character that continues or starts a new token
					
			// Figure out what the new character is
			ParseTokenType currentCharType = ParseTokenType.SYMBOL;
			if(LOGIC_TOKENS_SET.indexOf(n)>=0) currentCharType = ParseTokenType.LOGIC;
			else if(COMPARE_TOKENS_SET.indexOf(n)>=0) currentCharType = ParseTokenType.COMPARE;
			
			if(currentToken==null) {
				// No token running ... start one
				currentToken = new StringBuffer();
				currentToken.append((char)n);
				currentTokenType = currentCharType;				
			} else {
				if(currentTokenType==currentCharType) {
					// Same type of character as running token? Just append it
					currentToken.append((char)n);
				} else {
					// This is a new token. Store the old one and start a new one.
					ParseToken pt = new ParseToken();
					pt.token = currentToken.toString();
					pt.tokenType = currentTokenType;
					if(pt.token.equals("!")) pt.tokenType = ParseTokenType.NOT;
					pt.position = clis.getCurrentPosition();
					pt.codeLine = clis.getCurrentLine();
					parseTokens.add(pt);
					currentToken = new StringBuffer();
					currentToken.append((char)n);
					currentTokenType = currentCharType;	
				}
			}
			
		}		
		
	}	

}
