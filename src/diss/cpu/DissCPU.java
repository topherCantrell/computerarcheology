package diss.cpu;

import java.util.HashMap;
import java.util.Map;

import cpu.CPU;
import cpu.Opcode;
import util.BinaryFiles;
import util.CU;

public class DissCPU {
	
	CPU cpu;
	
	static Map<String,DissCPU> cache = new HashMap<String,DissCPU>();
	
	/**
	 * Get a DissCPU object by name
	 * @param name the name of the CPU
	 * @return the CPU object
	 */
	public static DissCPU getDissCPU(String name) {		
		if(name==null) return null;
		DissCPU ret = cache.get(name);
		if(ret==null) {		
			
			switch(name) {
			case "6502":
				ret = new DissCPU_6502();
				break;
			case "6803":
				ret = new DissCPU_6803();
				break;
			case "6809":
				ret = new DissCPU_6809();
				break;
			case "DVG":
				ret = new DissCPU_DVG();
				break;
			case "Z80":
				ret = new DissCPU_Z80();
				break;
			case "Z80GB":
				ret = new DissCPU_Z80GB();
				break;
				default:
					return null;
			}
			
			cache.put(name, ret);
		}
		return ret;
	}

	public Opcode disassemble(BinaryFiles files, int addr, Map<String, Object> fillins) {
		int pos = addr; 
        
        String pot = "";
        
        Opcode ret = null;
        
        for(Opcode op : cpu.opcodes) {
        	if(op.code.equals("DDE5")) {
        		System.out.println("CLOSER");
        		throw new RuntimeException("What is this?");
        	}
        	
            while(pot.length()<(op.getSize()*2)) {
                pot = pot + CU.hex2(files.getByte(pos++));                
            }
            if(cpu.couldMatch(pot,op)) {
                if(ret!=null) {
                    //throw new RuntimeException("OOPS");
                	System.out.println("OOPS");
                }
                ret = op;
                fillin(op, files, addr, fillins);  
            }
        }
        
        return ret;    
	}

	public void fillin(Opcode op, BinaryFiles files, int addr, Map<String, Object> fillins) {
		// "bytes" : [1,2,3,4]
        // "wordA" : "LDA"
        // "wordB" : "24,X++"
        
	    fillins.clear();
	    
        int [] data = new int[op.getSize()];
        for(int x=0;x<data.length;++x) {
            data[x] = files.getByte(addr+x);             
        }
        
        String mnem = op.mnemonic;
        
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
                    rep = expandFillinField(addr,c, d, files.getByte(ofs+addr), files.getByte(ofs+1+addr));
                    pos = pos + 4;
                    ofs += 2;                    
                } else {                    
                    rep = expandFillinField(addr,c,d,files.getByte(ofs+addr),0);  
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
	
	protected String expandFillinField(int addr, char c, char d, int ba, int bb) {
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

	public int[] getSpacing() {
		int[] ret = {16,8,16};
		return ret;
	}

}
