package cpu;

import code.AddressAccess;

public abstract class CPU {
	
	public abstract AddressAccess getAccess(String opcode, int numPos, int num);
	
	public static CPU getCPU(String name) {
		if(name.equals("6502")) {
			return new CPU_6502();
		}
		if(name.equals("6803")) {
			return new CPU_6803();
		}
		if(name.equals("6809")) {
			return new CPU_6809();
		}
		if(name.equals("DVG")) {
			return new CPU_DVG();
		}
		if(name.equals("Z80")) {
			return new CPU_Z80();
		}
		return new CPU_None();
	}

}
