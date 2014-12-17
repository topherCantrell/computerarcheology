package tools.processor;

import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

import tools.code.CU;

/** 
 * This class encapsulates an opcode mnemonic that may have multiple forms.
 * 
 * A mnemonic is a human readable form of an opcode. For instance, "09EEwmwl" might be represented
 * with "LDX #w".
 * 
 * There may be multiple forms of a single mnemonic. For instance, in the 6809 the "BCC" (branch if
 * carry clear) and "BHS" (branch if higher or the same) are exactly the same. The programmer can
 * pick either form. Thus the mnemonic representation here includes collections for multiple forms.
 *	
 * Mnemonics are lists of two types of tokens:
 *   Absolute text matches like "LDX #" in the above example
 *   Place holders for numbers like "w" in the above example
 *	
 * This class assumes that a text representation of the mnemonic assumes that numeric-fill-ins are
 * represented with single-lower-case-letters. The mnemonics are parsed into tokens here. 
 *	
 * For instance, a line like "A=A+PORT[b+i]" would result in the following tokens:
 * "A=A+PORT[b" ... b ... "+" ... i ... "]"
 *    MATCH      NUMBER  MATCH  NUMBER  MATCH 
 *
 */
public class Mnemonic 
{	
	
	/** The various text representations of a mnemonic **/
	private String [] textRepresentations;
	
	/** The parsed-token-list for each representation of a mnemonic **/
	private List<List<MnemonicParseToken>> parseTokens;
	
	/**
	 * This constructs a new mnemonic by parsing the text representations (separated
	 * with ";". Numeric fill-ins are single lower-case letters.
	 * @param text the combined mnemonic representation
	 */
	public Mnemonic(String text)
	{
		StringTokenizer st = new StringTokenizer(text,";");
		textRepresentations = new String[st.countTokens()];
		parseTokens = new ArrayList<List<MnemonicParseToken>>();
		for(int x=0;x<textRepresentations.length;++x) {			
			textRepresentations[x] = st.nextToken().trim();
			parseTokens.add(parseTokens(textRepresentations[x]));
		}
	}
	
	private List<MnemonicParseToken> parseTokens(String text)
	{
		List<Integer> ignore = new ArrayList<Integer>();
		text = CU.removeWhiteSpace(text,ignore);
		List<MnemonicParseToken> ret = new ArrayList<MnemonicParseToken>();
		String lastToken = "";
		for(int x=0;x<text.length();++x) {
			char c = text.charAt(x);
			if(c>='a' && c<='z') {
				if(lastToken.length()>0) {
					ret.add(new MnemonicParseToken(MnemonicParseToken.TYPE.MATCH,lastToken.toUpperCase()));
					lastToken="";					
				}
				ret.add(new MnemonicParseToken(MnemonicParseToken.TYPE.NUMBER,""+c));
			} else {
				lastToken = lastToken + c;
			}
		}
		if(lastToken.length()>0) {
			ret.add(new MnemonicParseToken(MnemonicParseToken.TYPE.MATCH,lastToken.toUpperCase()));
		}
		
		return ret;
	}
	
	/**
	 * This method returns all the text representations for a single mnemonic.
	 * @return the text representations for a single mnemonic.
	 */
	public String [] getTextRepresentations() { 
		return textRepresentations; 
	}
	
	/**
	 * This method returns the parse tokens for all the text representations for a
	 * single mnemonic.
	 * @return the list of parse tokens ... one list for each representation
	 */
	public List<List<MnemonicParseToken>> getParseTokens() { 
		return parseTokens; 
	}

}
