package cpu;

import code.AddressAccess;

public class CPU_None extends CPU {

	@Override
	public AddressAccess getAccess(String opcode, int numPos, int num) {
		return null;
	}

}
