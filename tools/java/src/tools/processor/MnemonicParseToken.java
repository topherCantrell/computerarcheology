package tools.processor;

/**
 * Mnemonics parse into tokens of two types: text-match and numeric-values. This class
 * encapsulates a parsed mnemonic.
 */
public class MnemonicParseToken {
	
	public enum TYPE { 
		MATCH,  // The "text" is absolute text to match against 
		NUMBER  // The "text" is a numeric value (or single lower-case-character
		        // representing a numeric fill-in)
	};	
	
	public TYPE tokenType;
	public String text;
	
	public MnemonicParseToken(MnemonicParseToken.TYPE tokenType, String text)
	{
		this.tokenType = tokenType;
		this.text = text;
	}

}
