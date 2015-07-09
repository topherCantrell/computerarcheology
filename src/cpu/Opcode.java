package cpu;

public class Opcode {
	
	public Opcode(String[] mnemonic, String code) {
		this.mnemonic = mnemonic;
		this.code = code;		
	}
	
	public String[] mnemonic;
	public String clocks;
	public String code;
	public String bus;
	public String flags;

}
