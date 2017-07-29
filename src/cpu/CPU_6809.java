package cpu;

import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Reader;
import java.util.ArrayList;
import java.util.List;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import util.CU;

public class CPU_6809 extends CPU {
	
	public CPU_6809() {
		try {
			loadOpcodes("cpu/6809.js");
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}
			
	protected void loadOpcodes(String filename) throws IOException, ParseException {
		
		super.loadOpcodes(filename);
				
		List<Opcode> posts = new ArrayList<Opcode>();
		
		Reader ir = new InputStreamReader(CPU.class.getClassLoader().getResourceAsStream(filename));		
		JSONParser parser = new JSONParser();		
		JSONArray objs = (JSONArray) parser.parse(ir);
		
		for(Object obj : objs) {
			JSONObject o = (JSONObject)obj;			
			if(o.containsKey("post")) {				
				Opcode op = new Opcode(o.get("post").toString(), o.get("code").toString());				
				posts.add(op);
			}
		}
		
		// Now we expand all the opcodes with their many "post" forms
		for(int x=opcodes.size()-1;x>=0;--x) {
			Opcode op = opcodes.get(x);
			String co = op.code;
			if(co.contains("yy")) {
				opcodes.remove(x);
				
				for(Opcode p : posts) {
															
					// Replace the "yy" with the postfix tokens. This likely extends the
					// opcode with other bytes and fill-ins.
					String nc = CU.replaceAll(co, "yy", p.code);
					
					// Replace the "y" with the postfix contribution to the mnemonic
					String mn = op.mnemonic;
										
					Opcode no = new Opcode(mn,nc);	
					no.bus = ""; // By default we consider these non-memory							
					opcodes.add(no);					
					
				}
				
			}
		}
	}
		
}
