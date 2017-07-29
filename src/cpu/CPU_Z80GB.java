package cpu;

public class CPU_Z80GB extends CPU {
	
	public CPU_Z80GB() {
		try {
			loadOpcodes("cpu/Z80GB.js");
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}
		
}
