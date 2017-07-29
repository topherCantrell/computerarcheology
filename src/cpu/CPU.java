package cpu;

import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Reader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import bus.AddressAccess;
import bus.BusDir;
import bus.BusType;
import code.CodeLine;
import util.CU;

public class CPU {
	
	static Map<String,CPU> cache = new HashMap<String,CPU>();
	
	public List<Opcode> opcodes; // Opcodes for this CPU
	public boolean bigEndian;	 // True if this is a big-endian CPU
	
	private BusDir decodeBusDirection(String d) {		
		if(d.contains("r") && d.contains("w")) return BusDir.BOTH;
		if(d.contains("r")) return BusDir.READ;
		if(d.contains("w")) return BusDir.WRITE;
		return null;
	}
	
	/**
	 * A line of disassembly will have an opcode and the fill-in numerical values. The
	 * numerical value may or may not result in a fixed memory access. If it does then
	 * the HTML generator can provide links and symbolic names to the access.
	 * 
	 * This method checks the opcode to see if the numerical portion is actually a
	 * bus access. If it is, this method fills out the information about that access.
	 * @param opcode the opcode making the access
	 * @param num the fill-in number
	 * @param directPage the value of the direct page offset
	 * @param accessOverride true if the line has been commented with an override request 
	 * @return the AddressAccess information
	 */
	public final AddressAccess getAccess(Opcode opcode, int num, int directPage, boolean accessOverride) {
		
		AddressAccess ret = new AddressAccess();		
		ret.address = num;
		
		if(opcode==null) {
			// TODO until we flesh out the DVG opcodes this will allow the JMP and JSR to create links	
			ret.busType = BusType.MAIN;
			ret.busDir = BusDir.READ;
			return ret;
		}
		
		String code = opcode.code;
		
		ret.busDir =  decodeBusDirection(opcode.bus);
		ret.busType = BusType.MAIN; // The usual case
		
		// Ports are always PORT
		if(code.contains("o")) {
			ret.busType = BusType.PORT;			
			return ret;
		}
		
		// Direct pages are always MAIN
		if(code.contains("p")) {	
			if(accessOverride) {		
				return null;
			}
			ret.address = num + directPage;
			return ret;
		}
		
		// Relative flow destinations ... always leading to memory
		if(code.contains("r") || code.contains("s")) {			
			return ret;
		}
		
		// The opcode considers these constants to be likely memory targets
		if(code.contains("t")) {			
			if(accessOverride) {		
				// But sometimes the indexed forms are used for other reasons
				return null;
			}
			return ret;
		}
		
		// At this point we don't think this is a memory access. But if the comment
		// insists then we'll pretend it is.
		if(accessOverride) {			
			return ret;
		}
		
		// This constant is NOT a memory access
		return null;
		
	}
		
	/**
	 * Common code used by all CPUs to load the opcode description file.
	 * @param filename
	 * @throws IOException
	 * @throws ParseException
	 */
	protected void loadOpcodes(String filename) throws IOException, ParseException {
		
		opcodes = new ArrayList<Opcode>();
		
		Reader ir = new InputStreamReader(CPU.class.getClassLoader().getResourceAsStream(filename));		
		
		JSONParser parser = new JSONParser();
		
		JSONArray objs = (JSONArray) parser.parse(ir);
		
		for(Object obj : objs) {
			JSONObject o = (JSONObject)obj;	
			if(o.containsKey("mnem")) {	
				Opcode op = new Opcode(o.get("mnem").toString(), o.get("code").toString());		
				op.bus = o.get("bus").toString();				
				opcodes.add(op);
			}
		}
	}
	
	/**
	 * Get a CPU object by name
	 * @param name the name of the CPU
	 * @return the CPU object
	 */
	public static CPU getCPU(String name) {		
		if(name==null) return null;
		CPU ret = cache.get(name);
		if(ret==null) {		
			
			switch(name) {
			case "6502":
				ret = new CPU_6502();
				break;
			case "6803":
				ret = new CPU_6803();
				break;
			case "6809":
				ret = new CPU_6809();
				break;
			case "DVG":
				ret = new CPU_DVG();
				break;
			case "Z80":
				ret = new CPU_Z80();
				break;
			case "Z80GB":
				ret = new CPU_Z80GB();
				break;
				default:
					return null;
			}
			
			cache.put(name, ret);
		}
		return ret;
	}
			
	private boolean couldMatch(String pot, Opcode op) {
	    
	    for(int x=0;x<op.code.length();++x) {
	        char c = op.code.charAt(x);
	        if(c>='a' && c<='z') {
	            // Fill-in field. Matches anything.
	            continue;
	        }
	        // Numbers must match exactly
	        if(pot.charAt(x)!=c) return false;
	    }
	    // This fits
	    return true;
	}
	
	/**
	 * Find the first opcode that matches the given line of disassembly. Some opcodes
	 * have multiple mnemonic matches (BCC/BHS are the same thing).
	 * @param codeLine the code
	 * @return the matching opcode
	 */
	public Opcode matchDisassembly(CodeLine codeLine) {
		String dat = "";
		for(int i : codeLine.data) {
			dat += CU.hex2(i);
		}
		if(opcodes==null) return null;
		Opcode ret = null;
		for(Opcode op : opcodes) {
			if(op.getSize()==codeLine.data.size()) {
				if(couldMatch(dat,op)) {
					//if(ret!=null) {
					//	throw new RuntimeException("Multiple opcodes match the disassembly: "+codeLine.originalText);
					//}
					ret = op;
					break;
				}
			}
		}
		if(ret==null) {
			throw new RuntimeException("Unknown line of disassembly: "+codeLine.originalText);
		}
		return ret;
	}
	
	/*
	public static void main(String [] args) throws Exception {
		CPU cpu = getCPU("6502");
		System.out.println(cpu);
		cpu = getCPU("6803");
		System.out.println(cpu);
		cpu = getCPU("6809");
		System.out.println(cpu);
		cpu = getCPU("DVG");
		System.out.println(cpu);
		cpu = getCPU("Z80");
		System.out.println(cpu);
		cpu = getCPU("Z80GB");
		System.out.println(cpu);
	}
	*/
		
}
