package cpu;

import code.BusType;
import code.AddressAccess;
import code.BusDir;

public class CPU_6502 extends CPU {
		
	@Override
	public AddressAccess getAccess(String opcode, int numPos, int num, int directPage) {
		
		if(opcode.charAt(numPos-1)=='#') {
			// Immediate constant
			return null;
		}
		
		if(opcode.contains(",")) {
			// Index forms
			return null;
		}
		
		AddressAccess ret = new AddressAccess();
		ret.address = num;
		ret.bus = BusDir.BOTH;
		ret.accessType = BusType.MAIN;
				
		if(opcode.startsWith("B") || opcode.startsWith("J")) {
			// This is a code reference (a flow branch)		
			ret.isCode = true;			
			return ret;
		}				
				
		if(opcode.startsWith("LD")) {
			ret.bus = BusDir.READ;
		} else if(opcode.startsWith("ST")) {
			ret.bus = BusDir.WRITE;
		} else {
			ret.bus = BusDir.BOTH;
		}
				
		return ret;
	}

}
