package tools.code;

import java.io.InputStream;
import java.util.List;

/**
 * This class implements an InputStream over a list of CodeLine lines. This is
 * useful for a parser that reads constructs that span several lines. This 
 * stream only traverses opcode data ... not labels or comments.
 */
public class CodeLineInputStream extends InputStream 
{
	
	private List<CodeLine> codeLines;	
	private CodeLine currentCodeLine;
	private String currentLine;
	private int currentLineNumber;
	private int position;
	
	/**
	 * This constructs a new CodeLineInputStream
	 * @param codeLines the list of CodeLine lines
	 * @param startLineNumber the starting line number
	 * @param startPosition the starting position within the starting line
	 */
	public CodeLineInputStream(List<CodeLine> codeLines, int startLineNumber, int startPosition)
	{
		this.codeLines = codeLines;
		this.currentLineNumber = startLineNumber;
		this.position = startPosition;
		this.currentCodeLine = codeLines.get(currentLineNumber);
		
		this.currentLine = currentCodeLine.getOpcodeString();		
	}
	
	/**
	 * This method returns the current line index in the array of code lines.
	 * @return current line index (not the same as the line number in the original file)
	 */
	public int getCurrentLineNumber() {
		return currentLineNumber;
	}
	
	/**
	 * This method returns the current line number within the list of CodeLine lines.
	 * @return the current line number
	 */
	public int getCurrentFileLineNumber() {
		return currentCodeLine.getLineNumber();
	}

	/**
	 * This method return the current character index of the current line.
	 * @return current character index of the current line
	 */
	public int getCurrentPosition() {
		return position;
	}
	
	/**
	 * This method returns the name of the file of the current line.
	 * @return filename of the current line
	 */
	public String getCurrentFilename() {
		return currentCodeLine.getFilename();
	}
	
	/**
	 * This method returns the current line
	 * @return the current CodeLine
	 */
	public CodeLine getCurrentLine() {
		return currentCodeLine;
	}
	
	@Override
	public int read()
	{
		// Advance the line/position 		
		if(currentLine==null || position==currentLine.length()) {
			if(currentLineNumber==(codeLines.size()-1)) {
				// End of the lines
				return -1;
			}
			position = 0;
			++currentLineNumber;
			currentCodeLine = codeLines.get(currentLineNumber);
			currentLine = currentCodeLine.getOpcodeString();
			return '\n';
		}
		return currentLine.charAt(position++);
	}
	
}
