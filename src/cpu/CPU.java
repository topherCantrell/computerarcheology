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

import asm.ASM;
import asm.ASMException;
import code.AddressAccess;
import code.CU;
import code.CodeLine;

public abstract class CPU {
	
	public List<Opcode> opcodes;

	public boolean bigEndian;
	
	static Map<String,CPU> cache = new HashMap<String,CPU>();
	
	public abstract AddressAccess getAccess(String opcode, int numPos, int num, int directPage);
	
	public abstract int assemble(boolean firstPass, CodeLine c, ASM asm) throws ASMException;
	
	public int[] getSpacing() {
		int[] ret = {12,8,16};
		return ret;
	}
	
	protected void loadOpcodes(String filename) throws IOException, ParseException {
		
		opcodes = new ArrayList<Opcode>();
		
		JSONParser parser = new JSONParser();
		JSONArray objs = (JSONArray) parser.parse(new FileReader(filename));
		
		for(Object obj : objs) {
			JSONObject o = (JSONObject)obj;
			JSONArray mns = (JSONArray) o.get("mnem");
			String [] mn = new String[mns.size()];
			for(int x=0;x<mn.length;++x) mn[x] = mns.get(x).toString();
			Opcode op = new Opcode(mn, o.get("code").toString());			
			op.bus = o.get("bus").toString();
			op.clocks = o.get("clocks").toString();
			op.flags = o.get("flags").toString();			
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
			} else if(name.equals("Z80GB")) {
			    ret = new CPU_Z80GB();
			}
			
			else {
				ret = new CPU_None();
			}
			cache.put(name, ret);
		}
		return ret;
	}
	
	public boolean couldMatch(String pot, Opcode op) {
	    
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
	
	public String expandFillinField(int addr, char c, char d, int ba, int bb) {
	    if(c!=d) {
	        int val = 0;
	        if(d=='l') {
	            val = ba + (bb<<8);
	        } else {
	            val = (ba<<8) + bb;
	        }
	        // TODO signed and relative
	        return "$"+CU.hex4(val);
	    } else {
	        
	        if(c=='r') {
	            if(ba>127) {
	                ba = ba - 256;
	            }
	            ba = ba + addr + 2;
	            return "$"+CU.hex2(ba);
	        } else {	        
    	        return "$"+CU.hex2(ba);
	        }
	    }
	}
	
	public int dsafe(int[] binary, int addr) {
	    if(addr<binary.length) return binary[addr];
	    return 0;
	}
	
	
	public void fillin(Opcode op, int[] binary, int addr, Map<String, Object> fillins) {
	    
	    // "bytes" : [1,2,3,4]
        // "wordA" : "LDA"
        // "wordB" : "24,X++"
        
	    fillins.clear();
	    
        int [] data = new int[op.getSize()];
        for(int x=0;x<data.length;++x) {
            if(x<binary.length) {
                data[x] = dsafe(binary,x+addr);
            } 
        }
        
        String mnem = "";
        for(String a : op.mnemonic) {
            mnem = mnem + a;
        }
        
        int ofs = 0;
        int pos = 0;
        while(pos<op.code.length()) {            
            char c = op.code.charAt(pos);
            char d = op.code.charAt(pos+1);
            
            if(c>='a' && c<='z') {
                String rep = "";
                if(d!=c) {
                    char e = op.code.charAt(pos+2);
                    //char f = op.code.charAt(pos+3);
                    if(c!=e) {
                        throw new RuntimeException("OOPS");
                    }
                    rep = expandFillinField(addr,c, d, binary[ofs+addr], binary[ofs+1+addr]);
                    pos = pos + 4;
                    ofs += 2;                    
                } else {                    
                    rep = expandFillinField(addr,c,d,binary[ofs+addr],0);  
                    ofs = ofs + 1;
                    pos = pos + 2;
                }
                
                mnem = CU.replaceAll(mnem, ""+c, rep);
                
            } else {
                ofs = ofs + 1;
                pos = pos + 2;
            }
            
        }
                        
        int x = mnem.indexOf(" ");
        if(x>=0) {
            fillins.put("wordA",mnem.substring(0,x).trim());
            fillins.put("wordB",mnem.substring(x+1).trim());
        } else {
            fillins.put("wordA", mnem);
            fillins.put("wordB", "");
        }
        
        // Calculate relative addresses
        // Need 1-byte signed calculations type
        
        fillins.put("bytes", data);
        
	}

    public Opcode disassemble(int[] binary, int addr, Map<String, Object> fillins) {
        
        int pos = addr; 
                
        String pot = "";
        
        Opcode ret = null;
        
        for(Opcode op : opcodes) {
            while(pot.length()<(op.getSize()*2)) {
                if(pos<binary.length) {
                    pot = pot + CU.hex2(binary[pos]);
                    ++pos;
                } else {
                    pot = pot + "00";
                }
            }
            if(couldMatch(pot,op)) {
                if(ret!=null) {
                    throw new RuntimeException("OOPS");
                }
                ret = op;
                fillin(op, binary, addr, fillins);  
            }
        }
        
        return ret;    
    }

}
