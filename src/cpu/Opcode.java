package cpu;

public class Opcode {
    
    public String[] mnemonic;
    public String clocks;
    public String code;
    public String bus;
    public String flags;
    
    public static Opcode UNKNOWN;
    
    static {
        String[] unk = {"???"};
        UNKNOWN = new Opcode(unk,"bb");
    }
	
	public Opcode(String[] mnemonic, String code) {
		this.mnemonic = mnemonic;
		this.code = code;		
	}
	
    public int getSize() {
        return code.length()/2;
    }

}
