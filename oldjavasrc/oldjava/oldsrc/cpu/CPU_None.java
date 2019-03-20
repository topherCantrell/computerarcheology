package cpu;

import asm.ASM;
import asm.ASMException;
import code.AddressAccess;
import code.CodeLine;

public class CPU_None extends CPU {

	@Override
	public AddressAccess getAccess(String opcode, int numPos, int num, int directPage) {
		return null;
	}
	
	@Override
	public int assemble(boolean firstPass, CodeLine c, ASM asm) throws ASMException {
		throw new ASMException("No CPU",c);
	}

}
