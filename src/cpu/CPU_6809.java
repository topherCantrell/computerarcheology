package cpu;

import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import code.AddressAccess;
import code.BusDir;
import code.BusType;

public class CPU_6809 extends CPU {
	
	public CPU_6809() {
		try {
			loadOpcodes("src/cpu/6809.js");
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}
	
protected void loadOpcodes(String filename) throws IOException, ParseException {
		
		opcodes = new ArrayList<Opcode>();
		
		JSONParser parser = new JSONParser();
		JSONArray objs = (JSONArray) parser.parse(new FileReader(filename));
		
		for(Object obj : objs) {
			JSONObject o = (JSONObject)obj;
			Opcode op = new Opcode();
			if(o.containsKey("mnem")) {
				op.mnemonic = o.get("mnem").toString();
				op.bus = o.get("bus").toString();
				op.clocks = o.get("clocks").toString();
				op.flags = o.get("flags").toString();
				op.code = o.get("code").toString();
				opcodes.add(op);
			}
		}
	}
	
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
		if(numPos>0 && opcode.charAt(numPos-1)=='<') {
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
