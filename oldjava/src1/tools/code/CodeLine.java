package tools.code;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import tools.processor.Opcode;


/**
 * This class encapsulates a single line of assembly or disassembly. 
 * 
 * Example of Assembly:
 * 
 * 0xF000:
 * MySpot:
 *   LDA    MYVAL-2[SPOTA-SPOTB+10]  ; Comment
 * 
 * Example of Disassembly:
 * 
 * F000: 80 40 55 55      LDA  0x20[0x0400]
 *  
 */

public class CodeLine 
{
	
	// General info
	private String filename;     // Where the line came from
	private int lineNumber;      // Line number of the original source
	private String error;        // Any error associated with this line
	
	// Address and data
	private int address=-1;      // Address of code line in memory
	private int [] data;	     // The bytes of opcode data	
	
	private String originalText; // The original complete line of text (if loaded from a file)
	private String textNoComment; // The line without comment
	private String comment;      // Any comment on the end of the line
	
	// Opcode information (if any)
	private Opcode opcode;
	private Map<String,OpcodeParameterInfo> opcodeParamInfo = new HashMap<String,OpcodeParameterInfo>();
	
	// Data needed by the assembler
	private List<String> labels = new ArrayList<String>(); // List of labels attached to the line
	private boolean directive;   // True if this is an assembler directive
	private String opcodeString; // The text of the opcode field (before conversion to opcode)		
			
	/**
	 * This constructs a new CodeLine with the given original text. The line fragments
	 * are parsed here but not the opcode.
	 * @param code the original line of code
	 * @param filename the name of the file this line came from
	 * @param lineNumber the line-number in the file this came from
	 * @param hexAddress true if the address is just a 4-byte hex number (like with disassembly)
	 */
	public CodeLine(String code, String filename, int lineNumber) {
		this(code,filename,lineNumber,false);
	}
	public CodeLine(String code, String filename, int lineNumber, boolean hexAddress)
	{
		this.originalText = code;		
		this.filename = filename;
		this.lineNumber = lineNumber;
		
		code = code.trim();
		
		// Strip off and note any comment
		int i = code.indexOf(";");
		if(i>=0) {
			comment = code.substring(i+1);
			code = code.substring(0,i).trim();			
		} 
		textNoComment = code;
		
		// Labels could be origins (if numbers) or just tag strings
		i = code.indexOf(":");
		if(i>=0) {			
			String s = code.substring(0,i);
			code = code.substring(i+1).trim();			
			try {
				if(hexAddress) {
					address = CU.parseIntValue("0x"+s);
				} else {
					address = CU.parseIntValue(s);
				}
			} catch (Exception e) {
				labels.add(s);					
			}				
		}
				
		// Parse out any leading data specification like "98 AF 44 32".
		// Data values are always 2 digit hex. Mnemonics must NOT be
		// two digit hex numbers. "ADD", for instance, is hex but not
		// two digit.		
		List<Integer> dataList = new ArrayList<Integer>();
		while(CU.isTwoDigitHex(code, 0)) { 
			dataList.add(Integer.parseInt(code.substring(0,2),16));
			code = code.substring(2).trim();
		}
		if(dataList.size()!=0) {
			data = new int[dataList.size()];
			for(int x=0;x<dataList.size();++x) {
				data[x] = dataList.get(x);
			}						
		}	
		
		// Everything else is opcode		
		if(code.length()>0) {
			opcodeString = code;
		}
		
	}	

	/**
	 * This method returns the data of a system-targeted comment. These
	 * comments begin with ##. If the comment is not for the system this 
	 * method returns null.
	 * @return the system-targeted comment data or null if not a system-target
	 */
	public String getSpecialCommentData() {
		if(comment==null) return null;
		if(comment.trim().startsWith("##")) {
			return comment.trim().substring(2).trim();
		}
		return null;		
	}
	
	/**
	 * This method returns true if the line has been flagged as an
	 * assembler directive.
	 * @return true if this is an assembler directive
	 */
	public boolean isDirective() {
		return directive;
	}
	
	/**
	 * This method flags a line as an assembler directive.
	 * @param directive true if this is an assembler directive
	 */
	public void setDirective(boolean directive) {
		this.directive = directive;
	}

	/**
	 * This method returns all labels attached to this assembly line.
	 * @return the list of lines
	 */
	public List<String> getLabels() {
		return labels;
	}

	/**
	 * This method returns the code address or -1 if there is none.
	 * @return the code address or -1
	 */
	public int getAddress() {
		return address;
	}
	
	/**
	 * This sets the code address.
	 * @param address the new address
	 */
	public void setAddress(int address) {
		this.address = address;
	}

	/**
	 * This method returns the code data or null if there is none.
	 * @return data array or null
	 */
	public int[] getData() {
		return data;
	}
	
	/**
	 * This sets the code's data.
	 * @param data the code's data
	 */
	public void setData(int[] data) {
		this.data = data;
	}

	/**
	 * This method returns the code comment or null if there is none.
	 * @return comment or null
	 */
	public String getComment() {
		return comment;
	}
	
	public String noComment() {
		return textNoComment;
	}
	
	/**
	 * This sets the code's comment.
	 * @param comment the comment
	 */
	public void setComment(String comment) {
		this.comment = comment;
	}

	/**
	 * This method returns the original code text.
	 * @return the original text
	 */
	public String getOriginalText() {
		return originalText;
	}
	
	/**
	 * This sets the line's "original text".
	 * @param originalText the original text
	 */
	public void setOriginalText(String originalText) {
		this.originalText = originalText;
	}
			
	/**
	 * This method gets the line's opcode or null if none.
	 * @return the opcode
	 */
	public Opcode getOpcode() {
		return opcode;
	}
			
	/**
	 * This method sets the line's opcode.
	 * @param opcode the new opcode
	 */
	public void setOpcode(Opcode opcode) {
		this.opcode = opcode;
	}
	
	/**
	 * This method returns the mnemonic text.
	 * @return the opcode
	 */
	public String getOpcodeString() {
		return opcodeString;
	}
	
	/**
	 * This sets the opcode string.
	 * @param t the new opcode string
	 */
	public void setOpcodeString(String t) {
		opcodeString = t;
	}
	
	/**
	 * This method returns the name of the file the line
	 * was loaded from.
	 * @return the file name
	 */
	public String getFilename() {
		return filename;
	}
	
	/**
	 * This method returns the line number of the file this
	 * line was loaded from.
	 * @return the line number
	 */
	public int getLineNumber() {
		return lineNumber;
	}
	
	/**
	 * This method returns any errors attached to the line or
	 * null if none.
	 * @return error string or null if OK
	 */
	public String getError() {
		return error;
	}
	
	/**
	 * This method attaches an error to the code line.
	 * @param error the error string
	 */
	public void setError(String error) {
		this.error = error;
	}
	
	/**
	 * This method returns the complete description of an error for the line.
	 * @return the error description
	 */
	public String getErrorDescription() {
		String ret = "ERROR " + error + "\n"
			+ filename+"("+lineNumber+") "+originalText;
		return ret;
	}
	
	/**
	 * This method returns the map of opcode-parameter information.
	 * @return the opcode parameter information
	 */
	public Map<String,OpcodeParameterInfo> getOpcodeParamInfo() {
		return opcodeParamInfo;
	}
	
}
