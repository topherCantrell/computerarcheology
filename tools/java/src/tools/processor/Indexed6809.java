package tools.processor;

/**
 * The 6809 processor has a versatile indexed mode that
 * can be applied to most instructions. This class encapsulates
 * the information in a single entry in the indexed-mode
 * opcode postfix table.
 */
public class Indexed6809 {
	
	/** Number of additional clocks the indexed operation takes */
	public String clocks;
	
	/** The binary code of the indexed operation */
	public String code;
	
	/** The mnemonic postfix */
	public String m6809;

}
