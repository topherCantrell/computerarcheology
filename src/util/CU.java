package util;

import java.util.List;

public final class CU {
	
	private CU() {}
	
	/** 
	 * Check if the given string is a valid number in the given base.
	 * @param s the string
	 * @param base the base
	 * @return true if the string is a valid number
	 */
	public static boolean isNumeric(String s, int base) {
		try {
			Integer.parseInt(s,base);			
			return true;
		} catch (Exception e) {
			return false;
		}
	}
	
	/**
	 * Convert a list of strings to a single string separated by LF.
	 * @param strs the list of strings
	 * @return the merged string
	 */
	public static String listToString(List<String> strs) {
		String ret = "";
		for(String s : strs) {
			ret = ret + s + "\n";
		}
		return ret;
	}
	
	/**
	 * Replace all of the given keys with the given values.
	 * @param target the target string
	 * @param key the key to replace
	 * @param value the new value
	 * @return the new string
	 */
	public static String replaceAll(String target, String key, String value) {
		
		String builder = "";
		
		while(true) {
			int i = target.indexOf(key);
			if(i<0) break;
			builder += target.substring(0,i)+value;			
			target = target.substring(i+key.length());
		}
		return builder+target;
	}
	
	/**
	 * This function parses an integer specification. The string may start with "0x" (hex)
	 * or "0b" (binary) or "0d" (decimal). All underscores are stripped out.
	 * @param s the string to parse
	 * @return the integer representation
	 */
	public static int parseInt(String s, int base) {
		if(s.startsWith("0x")) {
			s = s.substring(2);
			base = 16;
		} else if(s.startsWith("0b")) {
			s = s.substring(2);
			base = 2;
		}
		s = s.replace("_","");
		// Throws an exception if not valid
		return Integer.parseInt(s, base);		
	}
	
	/**
	 * Convert the value to a 4 digit hex string.
	 * @param value the value
	 * @return the hex string
	 */
	public static String hex4(int value) {
		String ret = Integer.toString(value,16).toUpperCase();
		while(ret.length()<4) {
			ret = "0"+ret;
		}
		return ret;
	}
		
	/**
	 * Convert the value to a 2 digit hex string.
	 * @param value the value
	 * @return the hex string
	 */
	public static String hex2(int value) {
		String ret = Integer.toString(value,16).toUpperCase();
		while(ret.length()<2) {
			ret = "0"+ret;
		}
		return ret;
	}
	
	/**
	 * Pad spaces onto the end of the given string until it is
	 * the given length.
	 * @param s the string to pad
	 * @param length the length to pad to
	 * @return the padded string
	 */
	public static String padTo(String s, int length) {
		while(s.length()<length) {
			s = s+" ";
		}
		return s;
	}

	/**
	 * Returns true if the target two characters in the string
	 * are a two-digit hex value (with a space or EOL after).
	 * @param s the full string
	 * @param pos the position within the string
	 * @return true if the position is a two-digit hex value
	 */
	public static boolean isTwoDigitHex(String s, int pos) {
		if(pos>=s.length()) return false;
		char a = s.charAt(pos++);
		if(pos>=s.length()) return false;
		char b = s.charAt(pos++);

		if(pos!=s.length() && s.charAt(pos)!=' ') return false;

		if( (a>='0' && a<='9' || a>='A' && a<='F') && (b>='0' && b<='9' || b>='A' && b<='F') ) {
			return true;
		}
		return false;
	}
	
}
