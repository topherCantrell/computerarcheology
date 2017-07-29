package cpu;

import asm.ASM;
import asm.ASMException;
import code.AddressAccess;
import code.BusDir;
import code.BusType;
import code.CodeLine;

public class CPU_DVG extends CPU {
	
	@Override
	public int assemble(boolean firstPass, CodeLine c, ASM asm) throws ASMException {
		throw new RuntimeException("IMPLEMENT ME");
	}

	@Override
	public AddressAccess getAccess(String opcode, int numPos, int num, int directPage) {
		
		if(opcode.startsWith("JSR") || opcode.startsWith("JMP")) {
			AddressAccess ret = new AddressAccess();
			ret.address = num;
			ret.isCode = true;
			ret.bus = BusDir.BOTH;
			ret.accessType = BusType.MAIN;
			return ret;
		}
		
		return null;
		
	}

}
