package sim;

import java.io.IOException;
import java.util.List;

import code.CU;

public class CPUZ80 extends CPU {
	
	// http://www.z80.info/z80flag.htm
	
	private static final boolean DEBUG = false;
	private static final int STOPAFTER = -1;
	
	int inscnt;
	
	int [] memory = new int[64*1024];
	
	int pc;
	
	boolean zf, cf;
	
	public CPUZ80(List<String> lines) {
		super(lines);
		
		registers.put("SP", new Register("SP",true));
		registers.put("A", new Register("A",false));
		registers.put("B", new Register("B",false));
		registers.put("C", new Register("C",false));
		registers.put("D", new Register("D",false));
		registers.put("E", new Register("E",false));
		registers.put("H", new Register("H",false));
		registers.put("L", new Register("L",false));
		registers.put("BC", new RegisterPair("BC",getRegister("B"),getRegister("C")));
		registers.put("DE", new RegisterPair("DE",getRegister("D"),getRegister("E")));
		registers.put("HL", new RegisterPair("HL",getRegister("H"),getRegister("L")));
		
		for(String s : lines) {			
			int i = s.indexOf(":",5);
			if(i>0) {
				s = s.substring(0,i);
			}						
			int addr = Integer.parseInt(s.substring(0,4),16);
			s = s.substring(6).trim();
			while(s.length()>0) {
				int val = Integer.parseInt(s.substring(0,2),16);
				s = s.substring(2).trim();
				memory[addr] = val;
				++addr;
			}			
		
		}
	}

	@Override
	public int readMemory(int addr, boolean isWordSize) {
		if(isWordSize) {
			return (memory[addr+1]<<8) | memory[addr];
		} else {
			return memory[addr];
		}
	}

	@Override
	public void writeMemory(int addr, int value, boolean isWordSize) {
		Register.checkSize(value, isWordSize);
		if(isWordSize) {
			memory[addr+1] = value>>8;
			memory[addr] = value&0xFF;
		} else {			
			memory[addr] = value;
		}
	}

	@Override
	public void push(int value, boolean word) {		
		if(!word) throw new RuntimeException("Stack ops are word sized");
		Accessable sp = getRegister("SP");
		int spval = sp.readValue();
		spval = spval - 2;
		writeMemory(spval,value,true);		
		sp.writeValue(spval);		
	}

	@Override
	public int pop(boolean word) {
		if(!word) throw new RuntimeException("Stack ops are word sized");
		Accessable sp = getRegister("SP");
		int spval = sp.readValue();		
		int ret = readMemory(spval,true);	
		spval = spval + 2;
		sp.writeValue(spval);		
		return ret;
	}
	
	String addDebugRegister(String name) {
		Accessable a = getRegister(name);
		String ta = name+"=";
		if(a.isWordSize()) {
			ta = ta + CU.hex4(a.readValue());
			ta = CU.padTo(ta, 6);
		} else {
			ta = ta + CU.hex2(a.readValue());
			ta = CU.padTo(ta, 8);
		}
		return ta;		
	}
	
	public void debug(String addr, String instruction) {
		if(DEBUG) {
			String ic = CU.padTo(Integer.toString(inscnt).toUpperCase(),12);
			String ins = ic+CU.padTo(addr+": "+instruction,30);
			ins = ins + addDebugRegister("A");
			ins = ins + addDebugRegister("B");
			ins = ins + addDebugRegister("C");
			ins = ins + addDebugRegister("D");
			ins = ins + addDebugRegister("E");
			ins = ins + addDebugRegister("H");
			ins = ins + addDebugRegister("L");
			ins = ins + "CF="+cf+" ZF="+zf;
			System.out.println(ins);
			++inscnt;
			if(STOPAFTER>0 && inscnt==STOPAFTER) System.exit(0);
		}
	}

	@Override
	public void run(int address) {
		pc = findCodeTarget(address);
		
		while(pc!= 65535) {			
			String line = lines.get(pc);
			pc=pc+1;
			int i = line.indexOf(":",5);
			String instruction = line.substring(i+1);
			String addr = line.substring(0, 4);
			
			String op=null;
			String par=null;
			i = instruction.indexOf(" ");
			
			if(i>0) {
				op = instruction.substring(0, i);
				par = instruction.substring(i+1);
			} else {
				op = instruction;
			}
			
			try {
				if(
						flow(op,par) ||
						load(op,par) ||
						math(op,par) ||
						stack(op,par) ||
						misc(op,par)
					) 
				{
					debug(addr,instruction);
				} else {			
					throw new RuntimeException("Unknown instruction "+addr+":"+op+":"+par);
				}
			} catch (Exception e) {
				RuntimeException ne = new RuntimeException(":"+line+":",e);				
				throw ne;
			}
		}
	}
	
	Accessable decodeRegister(String par) {
		if(par.startsWith("$")) return null;
		if(par.startsWith("(")) return null;
		return getRegister(par);
	}
	
	Accessable decodeNonRegister(String par,boolean isWordAccess) {
		if(par.startsWith("$")) {
			return new AccessConstant(Integer.parseInt(par.substring(1),16),isWordAccess);
		}
		if(par.startsWith("($")) {
			return new MemoryAccess(this,Integer.parseInt(par.substring(2, par.length()-1),16),isWordAccess);
		}
		// This MUST be "(reg)"
		Register r = getRegister(par.substring(1,par.length()-1));
		return new IndexAccess(this,r,isWordAccess);		
	}
	
	Accessable [] decodeMathA(String par) {
		Accessable dst,val;
		dst = getRegister("A");
		if(par.equals("(HL)")) {
			val = new IndexAccess(this,getRegister("HL"),false);
		} else if(par.startsWith("$")) {
			val = new AccessConstant(Integer.parseInt(par.substring(1),16),false);
		} else { // Must be a register
			val = getRegister(par);
		}
		Accessable [] ret = {dst,val};
		return ret;
	}
	
	Accessable [] decodeMathPair(String par) {
		Accessable dst,val;
		// First must be "HL," or "A,"
		if(par.startsWith("HL,")) {
			dst = getRegister("HL");
			par = par.substring(3);
		} else {
			dst = getRegister("A");
			par = par.substring(2);
		}
		// Second can be "$val" or a register
		if(par.startsWith("$")) {
			val = new AccessConstant(Integer.parseInt(par.substring(1),16),dst.isWordSize());
		} else {
			val = getRegister(par);
		}
		// TODO might be "(HL)"
		Accessable [] ret = {dst,val};
		return ret;
	}
	
	void setZF(int value) {
		zf = (value==0);
	}
	
	int setCF(int value, boolean isWordSize) {
		cf = false;
		if(isWordSize) {
			if(value<0) {
				cf = true;
				return 65536+value;
			}
			if(value>65535) {
				cf = true;
				return value & 0xFFFF;				
			}
		} else {
			if(value<0) {
				cf = true;
				return 256+value;
			}
			if(value>255) {
				cf = true;
				return value & 0xFF;
			}
		}
		return value;
	}
	
	public boolean math(String op, String par) {
		if(op.equals("SBC")) {
			Accessable [] pair = decodeMathPair(par);
			Accessable dst=pair[0];Accessable val=pair[1];
			//
			int aval = dst.readValue() - val.readValue();
			if(cf) aval = aval - 1;
			//			
			aval = setCF(aval,dst.isWordSize());
			setZF(aval);			
			//
			dst.writeValue(aval);
			return true;
		}
		if(op.equals("SUB")) {
			Accessable [] pair = decodeMathPair(par);
			Accessable dst=pair[0];Accessable val=pair[1];
			//			
			int aval = dst.readValue() - val.readValue();
			//			
			aval = setCF(aval,dst.isWordSize());
			setZF(aval);			
			//
			dst.writeValue(aval);
			return true;
		}
		if(op.equals("ADC")) {
			Accessable [] pair = decodeMathPair(par);
			Accessable dst=pair[0];Accessable val=pair[1];
			//			
			int aval = dst.readValue() + val.readValue();
			if(cf) aval = aval + 1;
			//			
			aval = setCF(aval,dst.isWordSize());
			setZF(aval);			
			//
			dst.writeValue(aval);
			return true;
		}
		if(op.equals("ADD")) {
			Accessable [] pair = decodeMathPair(par);
			Accessable dst=pair[0];Accessable val=pair[1];
			//	
			int aval = dst.readValue() + val.readValue();
			//			
			aval = setCF(aval,dst.isWordSize());
			setZF(aval);			
			//
			dst.writeValue(aval);
			return true;
		}
		if(op.equals("INC")) {
			Accessable ac;
			if(par.equals("(HL)")) {
				ac = new IndexAccess(this,getRegister("HL"),false);
			} else {
				ac = getRegister(par);
			}
			int val = ac.readValue();
			val = val + 1;
			// INC does NOT affect the CF
			if(ac.isWordSize()) {
				val = val & 0xFFFF;
			} else {
				val = val & 0xFF;
			}
			setZF(val);
			//
			ac.writeValue(val);					
			return true;
		}
		if(op.equals("DEC")) {
			Accessable ac;
			if(par.equals("(HL)")) {
				ac = new IndexAccess(this,getRegister("HL"),false);
			} else {
				ac = getRegister(par);
			}
			int val = ac.readValue();
			val = val - 1;
			// DEC does NOT affect the CF
			if(val<0) {
				if(ac.isWordSize()) {
					val = val + 65536;
				} else {
					val = val + 256;
				}
			}
			setZF(val);
			//
			ac.writeValue(val);					
			return true;
		}
		if(op.equals("AND")) {
			Accessable [] pair = decodeMathA(par);
			Accessable dst=pair[0];Accessable val=pair[1];
			//	
			int aval = dst.readValue() & val.readValue();
			//
			cf = false;
			setZF(aval);
			//
			dst.writeValue(aval);
			return true;
		}
		if(op.equals("CP")) {
			Accessable [] pair = decodeMathA(par);
			Accessable dst=pair[0];Accessable val=pair[1];
			//			
			int aval = dst.readValue() - val.readValue();
			//			
			aval = setCF(aval,dst.isWordSize());
			setZF(aval);			
			//			
			return true;
		}
		if(op.equals("RLA")) {
			int aval = getRegister("A").readValue();
			aval = aval << 1;
			if(aval>0xFF) {
				aval = (aval & 0xFF) | 1;
				cf = true;
			} else {
				cf = false;
			}
			getRegister("A").writeValue(aval);
			return true;
		}
		return false;
	}
	
	public boolean misc(String op, String par) {
		if(op.equals("CCF")) {
			cf = false;
			return true;
		}
		if(op.equals("EX")) {
			Accessable left,right;
			if(par.equals("(SP),HL")) {
				left = new MemoryAccess(this,getRegister("SP").readValue(),true);
				right = getRegister("HL");
			} else {
				String [] parts = par.split(",");			
				left = getRegister(parts[0]);
				right = getRegister(parts[1]);
			}
			int lv = left.readValue();
			left.writeValue(right.readValue());
			right.writeValue(lv);
			return true;
		}
		return false;
	}
	
	public boolean stack(String op, String par) {
		if(op.equals("PUSH")) {
			Accessable reg = getRegister(par);
			push(reg.readValue(),reg.isWordSize());
			return true;
		}
		if(op.equals("POP")) {
			Accessable reg = getRegister(par);
			reg.writeValue(pop(reg.isWordSize()));
			return true;
		}
		return false;
	}
	
	public boolean load(String op, String par) {
		if(op.equals("LD")) {
			
			// NONE of the LD opcodes affect the flags
			
			Accessable left,right;
			
			if(par.startsWith("(HL),$")) {
				left = new IndexAccess(this,getRegister("HL"),false);
				right = new AccessConstant(Integer.parseInt(par.substring(6),16),false);
			} else {			
				// One of these must be a register
				String [] parts = par.split(",");	
				left = decodeRegister(parts[0]);		
				right = decodeRegister(parts[1]);
				
				// The other can be a register or something else
				if(left==null) {
					left = decodeNonRegister(parts[0],right.isWordSize());
				}
				if(right==null) {
					right = decodeNonRegister(parts[1],left.isWordSize());
				}		
			}
			
			left.writeValue(right.readValue());
			
			return true;
		}
		return false;
	}
	
	public boolean evaluateCondition(String cond) {
		if(cond.equals("NZ")) return !zf;
		if(cond.equals("Z")) return zf;
		if(cond.equals("NC")) return !cf;
		if(cond.equals("C")) return cf;
		throw new RuntimeException("Unknown condition "+cond);
	}
	
	public boolean flow(String op, String par) {
		if(op.equals("JP")) {
			boolean take = true;
			int i = par.indexOf(",");
			if(i>=0) {
				take = evaluateCondition(par.substring(0, i));
				par = par.substring(i+1);
			}
			if(par.startsWith("$")) {
				int dest = Integer.parseInt(par.substring(1),16);
				if(take) {
					pc = findCodeTarget(dest);
				}
				return true;
			}
		}
		
		if(op.equals("CALL")) {
			int dest = Integer.parseInt(par.substring(1),16);
			if(dest==0x33) {
				ROMCALL_DISPLAY();
				return true;
			}
			if(dest==0x2B) {
				ROMCALL_GETCHAR();
				return true;
			}
			push(pc,true);			
			pc = findCodeTarget(dest);
			return true;
		}
		
		if(op.equals("RET")) {
			boolean take = true;
			if(par!=null) take = evaluateCondition(par);
			if(take) {
				pc = pop(true);
			}
			return true;
		}		
		
		return false;
	}
	
	void ROMCALL_DISPLAY() {
		//System.out.println("DISPLAY:"+(char)getRegister("A").readValue());
		if(DEBUG) {
			System.out.println(":ROMCALL_DISPLAY:"+(char)getRegister("A").readValue());
		} else {
			System.out.print((char)getRegister("A").readValue());
		}
	}
	
	void ROMCALL_GETCHAR() {
		if(DEBUG) {
			System.out.println(":ROMCALL_GETCHAR:");
		}
		try {
			int c = System.in.read();
			getRegister("A").writeValue(c);
		} catch (IOException e) {
			throw new RuntimeException(e);
		}
	}

}
