package cpu;

public class CPU_Z80 extends CPU {
	
	public CPU_Z80() {
		try {
			loadOpcodes("cpu/Z80.js");
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}
		
}
