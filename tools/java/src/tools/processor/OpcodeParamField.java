package tools.processor;

/**
 * This enum defines the parameter primitives that opcodes are built from.
 * Don't think about mnemonics. This is purely binary opcode.
 * 
 * For instance:
 * DD36bbii   the 'b' field is an immediate byte and the 'i' field is an index byte. 
 * 28tltm     the 't' field is an address word pointing to code (text). The "tl" is the
 *            lsb and the "tm" is the msb.
 *            
 * Parameter info:
 *   bytes      number of opcode bytes taken by the parameter
 *   sub        the lower-case letter representing the parameter
 *   signed     true if the numeric value is signed (branch offsets, for instance)
 *   address    true if the numeric value is an address and not a constant (a RAM address, for instance)
 *   pc-offset  true if the numeric value is offset from the PC (branch offsets, for instance)
 *   io         true if the numeric value is a port (IO) address 
 *
 */
public enum OpcodeParamField {
	                           //bytes  sub   signed address  pc-offset  io 
	INDEX_BYTE                 (   1,   'i',  false, false,   false,   false),  // Unsigned byte used as an address offset
	SIGNED_INDEX_BYTE          (   1,   'j',  true,  false,   false,   false),  // Signed byte used as an address offset
	SIGNED_INDEX_WORD          (   2,   'k',  true,  false,   false,   false),  // Signed word used an an address offset
	IMMEDIATE_BYTE             (   1,   'b',  false, false,   false,   false),  // Byte constant
	IMMEDIATE_WORD             (   2,   'w',  false, false,   false,   false),  // Word constant
	ADDRESS_WORD_DATA          (   2,   't',  false, true,    false,   false),  // Word address for data
	BASE_ADDRESS_BYTE_DATA     (   1,   'p',  false, true,    false,   false),  // Byte address for data
	PORT_ADDRESS_BYTE          (   1,   'o',  false, false,   false,   true),   // Byte port address for I/O
	ADDRESS_WORD_TEXT          (   2,   'm',  false, true,    false,   false),  // Word address for code
	REL_BYTE_ADDRESS_TEXT      (   1,   'r',  true,  true,    true,    false),  // PC relative address offset byte for code
	REL_WORD_ADDRESS_TEXT      (   2,   's',  true,  true,    true,    false),  // PC relative address offset word for code
	// 6809 Specific
	PUSH_6809_U                (   1,   'u',  false, false,   false,   false),  // 6809 register set for pushes to U stack
	PUSH_6809_S                (   1,   'x',  false, false,   false,   false),  // 6809 register set for pushes to S stack
	PULL_6809_U                (   1,   'v',  false, false,   false,   false),  // 6809 register set for pulls from S stack
	PULL_6809_S                (   1,   'q',  false, false,   false,   false),  // 6809 register set for pulls from S stack
	REG_6809_TFR               (   1,   'z',  false, false,   false,   false),  // Byte field used in 6809 for register-pairs
	POST_6809                  (   1,   'y',  false, false,   false,   false);  // Byte used in 6809 to identify indexed form
	
	private int numBytes;
	private char subChar;
	private boolean address;
	private boolean pcOffset;
	private boolean io;
	private boolean signed;
	
	/**
	 * This static method returns the OpcodeParamField based on single-letter name.
	 * @param tag the single letter name
	 * @return the OpcodeParamField that maps to the given letter
	 */
	public static OpcodeParamField getParamField(char tag) {
		OpcodeParamField [] values = OpcodeParamField.values();
		for(OpcodeParamField para : values) {
			if(para.getSubChar()==tag) return para;
		}
		throw new RuntimeException("Unknown opcode param field type '"+tag+"'");
	}	
	
	OpcodeParamField(int numBytes, char subChar, boolean signed, boolean address, boolean pcOffset, boolean io) {
		this.numBytes = numBytes;
		this.subChar = subChar;
		this.address = address;
		this.pcOffset = pcOffset;
		this.io = io;
		this.signed = signed;
	}

	public int getNumBytes() {
		return numBytes;
	}

	public char getSubChar() {
		return subChar;
	}

	public boolean isAddress() {
		return address;
	}
	
	public boolean isPCOffset() {
		return pcOffset;
	}
	
	public boolean isIO() {
		return io;
	}
	
	public boolean isSigned() {
		return signed;
	}
	
}
