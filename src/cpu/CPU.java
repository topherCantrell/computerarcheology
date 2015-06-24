package cpu;

import code.AddressAccess;

public abstract class CPU {
	
	public abstract AddressAccess getAccess(String opcode, int numPos, int num);

}
