package code;

public class CodeLine {
	
	private String originalText;
	private String filename;
	private int line;
	
	private int address = -1;
	private byte[] data = null;
	private String opcode = null;
	private int opcodePos = -1;	
	private String comment = null;
	private int commentPos = -1;
	
	private String label = null;
	private String[] collectedLabels = null;
	
	// PrintChar:
	// 4000: 01 02 03  LDA  $500   ; This is a comment
	//
	// PureAssembly:
	// PrintChar:
	//    STA tmp1 ; This is a comment
	
	public CodeLine(String originalText, String filename, int line) {
		this.originalText = originalText;
		this.filename = filename;
		this.line = line;		
	}
	
	public static void main(String [] args) {
		
		System.out.println("Still here");
		
	}

}
