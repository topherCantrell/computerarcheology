package cpu;

import code.AddressAccess;
import code.BusDir;
import code.BusType;

public class CPU_DVG extends CPU {

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
