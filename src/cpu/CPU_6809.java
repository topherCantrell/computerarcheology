package cpu;

import code.AddressAccess;
import code.BusDir;
import code.BusType;

public class CPU_6809 extends CPU {
	
	static final String[] CODE = {"JSR","BPL","BNE","BEQ","BMI","JMP","BCC","BRA","BCS", 
		"LBEQ", "LBNE","BLS","BSR","BHI","BRN","LBSR","LBCC","LBCS","BVS","BLE","BLT","BVC","BGE","BGT","LBLE","LBPL","LBMI"};
	static final String[] READ = {"LDA", "LDB", "LDX","LDD","ORA","ADDA","ANDA","ORB","CMPA","CMPB","TST",
		"LDY","LDU","CMPX","CMPY","SUBA","SBCA","ADDD","ADDB","SUBD","SUBB","CPX","ANDB","ADCA","EORB","EORA",
		"ADCB","BITB","ADCB","SBCB","BITA","CMPD"};
	static final String[] WRITE = {"STA", "STB", "STX","STD","CLR","STY","STU","STS"};
	static final String[] BOTH = {"INC","DEC","ROL","ASL","NEG","ROR","COM","LSR","LSL"};

	@Override
	public AddressAccess getAccess(String opcode, int numPos, int num, int directPage) {
		
		// Immediates always have a '#'
		if(numPos>0 && opcode.charAt(numPos-1)=='#') {
			return null;
		}
		
		// Direct page offsets
		if(numPos>0 && opcode.charAt(numPos-1)=='>') {
			num = num + directPage;			
		}
		
		// No indexing
		if(opcode.contains(",")) {
			return null;
		}
		
		if(opcode.startsWith("CWAI")) {
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
		
		System.out.println(opcode);
		
		return null;
	}

}
