package diss.cpu;

import cpu.CPU;

public class DissCPU_Z80 extends DissCPU {
	
	public DissCPU_Z80() {
		cpu = CPU.getCPU("Z80");
	}

}
