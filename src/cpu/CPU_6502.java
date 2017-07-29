package cpu;

public class CPU_6502 extends CPU {
	
	public CPU_6502() {
		try {
			loadOpcodes("cpu/6502.js");
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}	
		
}
