package tools.code;

import java.util.List;

/**
 * This class contains lots of tool functions for dealing with assembly code.
 */
public final class CU {
	
	// Nobody make one
	private CU() {}
		
	/**
	 * This method removes unneeded whitespace in a line of code. Whitespace before
	 * and after symbols is not needed. 
	 * @param text the input text
	 * @param starts where each character in the return string started in the original string
	 * @return the compacted space
	 */
	public static String removeWhiteSpace(String text, List<Integer> starts)
	{
		
		// A symbol is made of 0123456789_ABCDEFGHIJKLMNOPQRSTUVWXYZ
		// Whitespace between two characters from this set is mandatory. 
		// All other whitespace can go.
				
		// For instance:		
		// LD A , 45 [ C+ D]
		// LD A,45[C+D]
		
		if(starts!=null) {
			starts.clear();			
		}
		
		boolean lastWasSpace=false;
		
		String ret = "";		
		for(int x=0;x<text.length();++x) {
			char c = text.charAt(x);
			if(c==' ' || c=='\t') { // Tabs and spaces are the same thing here
				c = ' '; // Convert tabs to spaces
				if(lastWasSpace) continue; // Ignore repeated white space
				lastWasSpace = true; // If there is another we'll ignore it
				char a = text.charAt(x-1);
				int y=x+1;
				while(text.charAt(y)==' ' || text.charAt(y)=='\t') ++y;
				char b = text.charAt(y);
				if(SYMBOL_CHAR.indexOf(a)<0 || SYMBOL_CHAR.indexOf(b)<0) {
					// If the character before and after the space could be a runnable sequence
					// then this whitespace is mandatory. If either character is NOT in the
					// runnable sequence then ignore this.
					continue;
				}				
			} else {
				lastWasSpace = false;
			}
			
			ret = ret + c;
			if(starts!=null) {
				starts.add(x);
			}
		}		
		
		// Trim any leading spaces
		if(ret.charAt(0)==' ') {
			ret = ret.substring(1);
			if(starts!=null) {
				starts.remove(0);
			}
		}
		
		// Trim any trailing spaces
		int x = ret.length()-1;
		if(ret.charAt(x)==' ') {
			ret = ret.substring(0,x);
			if(starts!=null) {
				starts.remove(x);
			}			
		}
				
		return ret;
		
	}
	
	/**
	 * This method locates the end of a token run. The returned value is one past
	 * the last character of the run (one past the end of the string if the 
	 * run is at the end of the string)
	 * @param text the text to search
	 * @param start the starting position of the token to find the end
	 * @return the position one past the end of the token
	 */
	public static int findEndOfExpression(String text, int start)
	{		
		
		while(true) {
			if(start==text.length()) return start;
			if(text.charAt(start)=='(') {
				int parenLevel = 1;				
				while(parenLevel!=0) {
					++start;
					if(start==text.length()) return start;
					if(text.charAt(start)=='(') ++parenLevel;
					if(text.charAt(start)==')') --parenLevel;
				}
				++start;
				continue;				
			}
			if(TERM_CHAR.indexOf(text.charAt(start))<0) {
				return start;
			}
			++start;
		}				
		
	}
	
	public static int findEndOfSymbol(String text, int start)
	{
		while(true) {
			if(start==text.length()) return start;
			if(SYMBOL_CHAR.indexOf(text.charAt(start))<0) {
				return start;
			}
			++start;
		}
	}
	
	private static String SYMBOL_CHAR = "0123456789_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
	private static String EXPRESSION_CHAR = "+-*/&|!^%";
	private static String TERM_CHAR = SYMBOL_CHAR+EXPRESSION_CHAR;
	
	/**
	 * This static method checks to see if there is a two-digit hex value at
	 * the given location in the target string. A space may follow or the
	 * end of the string.
	 * @param s target string
	 * @param start starting point in the string
	 * @return length of number or -1 if not valid
	 */
	public static boolean isTwoDigitHex(String s, int start) {
		if(start>=s.length()) return false;
		s = s.toUpperCase();
		for(int x=0;x<2;++x) {
			char c = s.charAt(start+x);
			if( !((c>='A' && c<='F') || (c>='0' && c<='9')) ) return false;
		}
		if((start+2)==s.length()) return true;
		if(s.charAt(start+2)!=' ') return false;
		return true;
	}
	
	/**
	 * This method checks that the string starts with a four digit hex
	 * number.
	 * @param s the target string
	 * @return true if the string starts with 4 digitis of hex
	 */
	public static boolean isFourDigitHex(String s)
	{
		if(s.length()<4) return false;
		for(int x=0;x<4;++x) {
			char c = s.charAt(x);
			if( !((c>='A' && c<='F') || (c>='0' && c<='9')) ) return false;
		}
		return true;
	}
	
	/**
	 * This static method returns the given value as a 4 digit hex number.
	 * @param value the value to convert
	 * @return 4 digit hex representation
	 */
	public static String fourDigitHex(int value)
	{
		String ret = Integer.toString(value,16).toUpperCase();
		while(ret.length()<4) ret="0"+ret;
		return ret;
	}
	
	public static String eightDigitBinary(int value)
	{
		String ret = Integer.toString(value,2).toUpperCase();
		while(ret.length()<8) ret="0"+ret;
		return ret;
	}
	
	public static String firstWord(String s) {
		if(s==null) return "";
		s = s.trim();
		int i = s.indexOf(" ");
		if(i<0) i = s.length();
		return s.substring(0,i);
	}
	
	/**
	 * This static method returns the given value as a 2 digit hex number.
	 * @param value the value to convert
	 * @return 2 digit hex representation
	 */
	public static String twoDigitHex(int value)
	{
		String ret = Integer.toString(value,16).toUpperCase();
		while(ret.length()<2) ret="0"+ret;
		return ret;
	}
	
	/**
	 * This static method returns the given value as a 2 digit or 4 digit
	 * hex number (4 if greater than 255).
	 * @param value the value to convert
	 * @return 2 or 4 digit hex representation
	 */
	public static String twoOrFourDigitHex(int value) {
		if(value>255) return fourDigitHex(value);
		return twoDigitHex(value);
	}
	
	/**
	 * This static method replaces all "key" in "source" with "value".
	 * @param source the string to substitute into
	 * @param key the target text to replace
	 * @param value the text to replace with
	 * @return the resulting string
	 */
	public static String replaceAll(String source, String key, String value) {
		int pos = 0;
		String ret = "";
		while(true) {
			int i = source.indexOf(key,pos);
			if(i<0) break;
			ret=ret+source.substring(pos,i)+value;
			pos=i+key.length();
		}
		ret = ret + source.substring(pos);
		return ret;
	}
	
	/**
	 * This static method pads the given string to the given length by
	 * appending white-space to the end.
	 * @param s the string to pad
	 * @param len the required length
	 * @return the padded string
	 */
	public static String padTo(String s, int len)
	{
		while(s.length()<len) s=s+" ";
		return s;
	}
	
	/**
	 * This static method pads a string with leading zeros.
	 * @param s the string to pad
	 * @param len the length of the string to pad to
	 * @return the padded string
	 */
	public static String leadingZero(String s, int len)
	{
		while(s.length()<len) s="0"+s;
		return s;
	}
	
	/**
	 * This static method collapses multiple white spaces into one white space.
	 * Tabs are also collapsed into white space.
	 * @param s the string to process
	 * @return the cleaned string
	 */
	public static String collapseWhiteSpace(String s) {
		while(true) {
			int i = s.indexOf('\t');
			if(i<0) break;
			String a = s.substring(0,i)+" "+s.substring(i+1);
			s = a;
		}
		while(true) {
			int i = s.indexOf("  ");
			if(i<0) break;
			String a = s.substring(0,i)+s.substring(i+1);
			s = a;
		}	
		
		return s;
	}
	
	/**
	 * This static method converts an N-bit signed value to a true java
	 * signed value.
	 * @param bits number of bits in the value
	 * @param value the signed value
	 * @return the true java signed value
	 */
	public static int signedNumber(int bits, int value) {
		int sub = (int)Math.pow(2, bits);
		int comp = (int)Math.pow(2,bits-1);
		if(value>=comp) {
			value = value - sub;
		}
		return value;		
	}

	/**
	 * This method produces a string of hex bytes for the given byte array.
	 * @param data the byte array
	 * @return the string representation
	 */
	public static String getDataString(int[] data) {
		String ret = "";
		for(int x=0;x<data.length;++x) {
			ret=ret+CU.twoDigitHex(data[x])+" ";
		}
		return ret.trim();
	}
	
	/**
	 * This method parses an integer value from the given string accounting for
	 * base specification.
	 * @param s the string to parse
	 * @return the int value
	 */
	public static int parseIntValue(String s) {
		s=s.toUpperCase();
		while(true) {
			int i = s.indexOf("_");
			if(i<0) break;
			String g = s.substring(0,i)+s.substring(i+1);
			s = g;
		}
		if(s.startsWith("0X")) {
			return Integer.parseInt(s.substring(2).toLowerCase(),16);
		} else if(s.startsWith("0B")) {
			return Integer.parseInt(s.substring(2).toLowerCase(),2);
		}
		return Integer.parseInt(s);
	}

}
