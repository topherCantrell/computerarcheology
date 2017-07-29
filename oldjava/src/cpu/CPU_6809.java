package cpu;

import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import asm.ASM;
import asm.ASMException;
import code.AddressAccess;
import code.BusDir;
import code.BusType;
import code.CodeLine;

public class CPU_6809 extends CPU {
	
	public CPU_6809() {
		try {
			loadOpcodes("src/cpu/6809.js");
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}
	
	@Override
	public int assemble(boolean firstPass, CodeLine c, ASM asm) throws ASMException {
		throw new RuntimeException("IMPLEMENT ME");
	}
	
	protected void loadOpcodes(String filename) throws IOException, ParseException {
		
		opcodes = new ArrayList<Opcode>();		
		List<Opcode> posts = new ArrayList<Opcode>();
		
		JSONParser parser = new JSONParser();
		JSONArray objs = (JSONArray) parser.parse(new FileReader(filename));
		
		for(Object obj : objs) {
			JSONObject o = (JSONObject)obj;			
			if(o.containsKey("mnem")) {
				JSONArray mns = (JSONArray) o.get("mnem");
				String [] mn = new String[mns.size()];
				for(int x=0;x<mn.length;++x) mn[x] = mns.get(x).toString();
				Opcode op = new Opcode(mn, o.get("code").toString());				
				op.bus = o.get("bus").toString();
				op.clocks = o.get("clocks").toString();
				op.flags = o.get("flags").toString();
				opcodes.add(op);
			} else {
				JSONArray psts = (JSONArray) o.get("post");
				String [] mn = new String[psts.size()];
				for(int x=0;x<mn.length;++x) mn[x] = psts.get(x).toString();
				Opcode op = new Opcode(mn, o.get("code").toString());				
				op.bus = o.get("bus").toString();
				op.clocks = o.get("clocks").toString();
				op.flags = o.get("flags").toString();
				posts.add(op);
			}
		}
		
		// Now we expand all the opcodes with their many "post" forms
		for(int x=0;x<opcodes.size();++x) {
			Opcode op = opcodes.get(x);
			String co = op.code;
			if(co.contains("yy")) {
				opcodes.remove(x);
				System.out.println("EXPANDING");
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
