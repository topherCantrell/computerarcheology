package web;

import java.util.ArrayList;
import java.util.List;

import code.CodeLine;

/**
 * All the parsed information from a single line of markup.
 */
public class LineOfMarkup {
	
	public String line;
	public String lineTrim;
	String newLine;
	String fileName;
	public int lineNumber;	
	
	public CodeLine codeLine = null;
	
	String giveId = null;
	
	public LineOfMarkup(String line, String fileName, int lineNumber) {
		this.line = line;
		this.lineTrim = line.trim();
		this.newLine = line;
		this.fileName = fileName;
		this.lineNumber = lineNumber;
	}
	
	/**
	 * Convert the list of strings to a list of LineOfMarkup
	 * @param original the list of strings
	 * @param fileName where all these strings came from
	 * @return the list of markup
	 */
	public static List<LineOfMarkup> convert(List<String> original, String fileName) {
		List<LineOfMarkup> ret = new ArrayList<LineOfMarkup>(original.size());
		int n = 1;
		for(String s : original) {
			ret.add(new LineOfMarkup(s,fileName,n++));
		}
		return ret;		
	}

}
