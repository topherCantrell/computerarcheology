package cpu;

public class CPU_6803 extends CPU {
	
	public CPU_6803() {
		try {
			loadOpcodes("cpu/6803.js");
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}
				
}
