package files;

import java.util.ArrayList;
import java.util.List;

/**
 * Tracks a line of text back to the file and line-number it came from.
 */
public class LineFromFile {
	
	/**
	 * Create a list of LineFromAFile from a plain list of strings.
	 * We might add or remove lines, but we want to keep the original information
	 * for error reporting.
	 * @param original the list of strings (likely just read from a file)
	 * @param file the name of the file to add to the LineFromAFile
	 * @return the list of LineFromAFile
	 */
	public static List<LineFromFile> convert(List<String> original, String file) {
		List<LineFromFile> ret = new ArrayList<LineFromFile>(original.size());
		int lineNumber = 1;
		for(String s : original) {
			LineFromFile f = new LineFromFile(s,file,lineNumber++);
			ret.add(f);
		}
		return ret;
	}
	
	/**
	 * Create a new LineFromAFile
	 * @param line the line of text
	 * @param file the name of the file
	 * @param lineNumber the line number of the text in the file
	 */
	public LineFromFile(String line, String file, int lineNumber) {
		this.line = line;
		this.file = file;
		this.lineNumber = lineNumber;
	}
	
	public String line;
	public String file;
	public int lineNumber;

}
