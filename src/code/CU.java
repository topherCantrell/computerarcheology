package code;

public class CU {
	
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
	
	public static String hex4(int value) {
		String ret = Integer.toString(value,16).toUpperCase();
		while(ret.length()<4) {
			ret = "0"+ret;
		}
		return ret;
	}
	
	public static boolean isNumeric(String s, int base) {
		try {
			parseInt(s,base);
			return true;
		} catch (Exception e) {
			return false;
		}
	}

}
