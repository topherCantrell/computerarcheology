package cpu;

import asm.ASM;
import asm.ASMException;
import code.AddressAccess;
import code.BusDir;
import code.BusType;
import code.CodeLine;

public class CPU_Z80 extends CPU {
	
	public CPU_Z80() {
		try {
			loadOpcodes("src/cpu/Z80.js");
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}
	
	@Override
	public int assemble(boolean firstPass, CodeLine c, ASM asm) throws ASMException {
		throw new RuntimeException("IMPLEMENT ME");
	}

	@Override
	public AddressAccess getAccess(String opcode, int numPos, int num, int directPage) {
		
		if(opcode.startsWith("RST")) {
			// Software interrupts by number
			return null;
		}
		
		// Limited few flow change opcodes
		if(opcode.startsWith("JP ") || opcode.startsWith("CALL ") || 
				opcode.startsWith("JR ") || opcode.startsWith("DJNZ ") || opcode.startsWith("DJZ ")) 
		{
			AddressAccess ret = new AddressAccess();
			ret.address = num;
			ret.bus = BusDir.BOTH;
			ret.accessType = BusType.MAIN;
			ret.isCode = true;
			return ret;
		}
		
		if(opcode.startsWith("IN")) {
			AddressAccess ret = new AddressAccess();
			ret.address = num;
			ret.bus = BusDir.READ;
			ret.accessType = BusType.PORT;
			ret.isCode = false;
			return ret;
		}
		
		if(opcode.startsWith("OUT")) {
			AddressAccess ret = new AddressAccess();
			ret.address = num;
			ret.bus = BusDir.WRITE;
			ret.accessType = BusType.PORT;
			ret.isCode = false;
			return ret;
		}
		
		// Memory access is always in parenthesis
		if(numPos>1) {			
			if(opcode.charAt(numPos-1)=='(') {
				
				AddressAccess ret = new AddressAccess();
				ret.address = num;				
				ret.accessType = BusType.MAIN;
				ret.isCode = false;
				
				if(opcode.charAt(numPos-2)==' ') {
					ret.bus = BusDir.WRITE;
				} else {
					ret.bus = BusDir.READ;
				}		
				
				return ret;
			}
		}		
		
		//System.out.println(opcode);	
		return null;
	}

}
