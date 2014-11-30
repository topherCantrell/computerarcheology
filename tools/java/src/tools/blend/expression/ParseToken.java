package tools.blend.expression;

import java.util.List;

import tools.code.CodeLine;

/**
 * This class represents a single scanned token from an algebraic expression. It can also be a 
 * sublist of tokens like between an open and close parenthesis.
 */
public class ParseToken 
{
	
	/** The type of the token */
	public ParseTokenType tokenType;
	
	/** The text of the token itself */
	public String token;
	
	/** If this is a SUBLIST then the list of sub tokens */
	public List<ParseToken> subList;
	
	/** The line of code where this token came from */
	public CodeLine codeLine;
	
	/** The token's position within the line of code */
	public int position;
	
}
