package cpu;

/**
 * The information about an opcode.
 */
public class Opcode {
    
    public String mnemonic;    // Like "LDA ,X+"
    public String code;        // Like "85tmtl"
    public String bus;         // Direction and type -- combinations of 'p', 'r', 'w'
    
    public static Opcode UNKNOWN; // When an opcode is unknown (common to all CPUs)    
    static {
        UNKNOWN = new Opcode("???","bb");
    }        
	
    /**
     * Create an opcode with minimal information
     * @param mnemonic the mnemonic
     * @param code the code pattern
     */
	public Opcode(String mnemonic, String code) {
		this.mnemonic = mnemonic;
		this.code = code;		
	}
	
	/**
	 * Get the number of bytes this opcode uses
	 * @return
	 */
    public int getSize() {
        return code.length()/2;
    }

}
