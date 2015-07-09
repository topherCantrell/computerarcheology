package code;

import java.util.List;

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
	
	public static String listToString(List<String> strs) {
		String ret = "";
		for(String s : strs) {
			ret = ret + s + "\n";
		}
		return ret;
	}
	
	public static String replaceAll(String target, String key, String value) {
		while(true) {
			int i = target.indexOf(key);
			if(i<0) break;
			String a = target.substring(0,i)+value+(target.substring(i+key.length()));
			target = a;
		}
		return target;
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

	public static String hex2(int value) {
		String ret = Integer.toString(value,16).toUpperCase();
		while(ret.length()<2) {
			ret = "0"+ret;
		}
		return ret;
	}
	
	public static String padTo(String s, int length) {
		while(s.length()<length) {
			s = s+" ";
		}
		return s;
	}

}
