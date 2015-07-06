package cpu;

import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import code.AddressAccess;

public abstract class CPU {
	
	protected List<Opcode> opcodes;
	
	static Map<String,CPU> cache = new HashMap<String,CPU>();
	
	public abstract AddressAccess getAccess(String opcode, int numPos, int num, int directPage);
	
	protected void loadOpcodes(String filename) throws IOException, ParseException {
		
		opcodes = new ArrayList<Opcode>();
		
		JSONParser parser = new JSONParser();
		JSONArray objs = (JSONArray) parser.parse(new FileReader(filename));
		
		for(Object obj : objs) {
			JSONObject o = (JSONObject)obj;
			Opcode op = new Opcode();
			op.mnemonic = o.get("mnem").toString();
			op.bus = o.get("bus").toString();
			op.clocks = o.get("clocks").toString();
			op.flags = o.get("flags").toString();
			op.code = o.get("code").toString();
			opcodes.add(op);
		}
	}
	
	public static CPU getCPU(String name) {		
		CPU ret = cache.get(name);
		if(ret==null) {			
			if(name.equals("6502")) {
				ret = new CPU_6502();
			} else if(name.equals("6803")) {
				ret = new CPU_6803();
			} else if(name.equals("6809")) {
				ret = new CPU_6809();
			} else if(name.equals("DVG")) {
				ret = new CPU_DVG();
			} else if(name.equals("Z80")) {
				ret = new CPU_Z80();
			} else {
				ret = new CPU_None();
			}
			cache.put(name, ret);
		}
		return ret;
	}

}
