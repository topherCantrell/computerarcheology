package cpu;

import code.AddressAccess;
import code.BusDir;
import code.BusType;

public class CPU_6803 extends CPU {
	
	static final String[] CODE = {"JSR","BPL","BNE","BEQ","BMI","JMP","BCC","BRA","BCS"};
	static final String[] READ = {"LDA", "LDB", "LDX","LDD","ORA","ADDA","ANDA","ORB","CMPA"};
	static final String[] WRITE = {"STA", "STB", "STX","STD","CLR"};
	static final String[] BOTH = {"INC","DEC"};

	@Override
	public AddressAccess getAccess(String opcode, int numPos, int num, int directPage) {
		
		// Immediates always have a '#'
		if(numPos>0 && opcode.charAt(numPos-1)=='#') {
			return null;
		}
		
		// No indexing
		if(opcode.contains(",")) {
			return null;
		}
		
		for(String s : CODE) {
			if(opcode.startsWith(s+" ")) {
				AddressAccess ret = new AddressAccess();
				ret.address = num;
				ret.bus = BusDir.BOTH;
				ret.accessType = BusType.MAIN;
				ret.isCode = true;
				return ret;
			}
		}
		
		for(String s : READ) {
			if(opcode.startsWith(s+" ")) {
				AddressAccess ret = new AddressAccess();
				ret.address = num;
				ret.bus = BusDir.READ;
				ret.accessType = BusType.MAIN;
				return ret;
			}
		}
		
		for(String s : WRITE) {
			if(opcode.startsWith(s+" ")) {
				AddressAccess ret = new AddressAccess();
				ret.address = num;
				ret.bus = BusDir.WRITE;
				ret.accessType = BusType.MAIN;
				return ret;
			}
		}
		
		for(String s : BOTH) {
			if(opcode.startsWith(s+" ")) {
				AddressAccess ret = new AddressAccess();
				ret.address = num;
				ret.bus = BusDir.BOTH;
				ret.accessType = BusType.MAIN;
				return ret;
			}
		}
		
		//System.out.println(opcode);
		
		return null;
	}

}
