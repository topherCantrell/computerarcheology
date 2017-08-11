package sim;

import java.util.ArrayList;
import java.util.List;

public class CPU6809 extends CPU {
	
	int [] memory = new int[64*1024];	
			
	boolean cf, zf;			
	
	int pc;
	
	public CPU6809(List<String> lines) {
		super(lines);
		
		registers.put("DP",new Register("DP",false));
		Register a = new Register("A",false);
		Register b = new Register("B",false);
		registers.put("A", a);
		registers.put("B", b);
		registers.put("D", new RegisterPair("D",a,b));
		registers.put("X", new Register("X",true));
		registers.put("Y", new Register("Y",true));
		registers.put("U", new Register("U",true));
		Register sp = new Register("SP",true);
		registers.put("SP",sp);
		registers.put("S",sp);
		
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
	
	public int readMemory(int addr, boolean isWordSize) {
		if(isWordSize) {
			return (memory[addr]<<8) | memory[addr+1];
		} else {
			return memory[addr];
		}
	}
	public void writeMemory(int addr, int value, boolean isWordSize) {
		Register.checkSize(value, isWordSize);
		if(isWordSize) {
			memory[addr] = value>>8;
			memory[addr+1] = value&0xFF;
		} else {			
			memory[addr] = value;
		}
	}	
		
	public void push(int value, boolean word) {		
		Register sp = getRegister("SP");
		int p = sp.readValue();
		//System.out.println("PUSH SP="+p);
		if(word) {
			p = p - 2;						
		} else {
			p = p - 1;			
		}	
		sp.writeValue(p);
		writeMemory(p,value,word);
	}
	
	public int pop(boolean word) {
		Register sp = getRegister("SP");
		int p = sp.readValue();
		//System.out.println("POP SP="+p);
		int ret = readMemory(p,word);
		if(word) {
			p = p + 2;						
		} else {
			p = p + 1;			
		}	
		sp.writeValue(p);
		return ret;
	}
			
	int setNZv(int value) {
		zf = (value==0);
		// TODO other flags as needed
		return value;
	}
	
	int setNZ(int value) {
		zf = (value==0);
		// TODO other flags as needed
		return value;
	}
	
	int setNZVC(int value,boolean isWordSize) {
		zf = (value==0);		
		int ret = value;
		if(ret<0) {
			// Make sure we "borrow" for 16 bits
			ret = 0x10_0000 + ret;
		}
		if(isWordSize) {
			cf = (value>0xFFFF);
			ret = ret & 0xFFFF;
		} else {
			cf = (value>0xFF);
			ret = ret & 0xFF;
		}		
		// TODO other flags as needed
		return ret;
	}
	
	void debug(String addr, String instruction) {
		/*
		String g = CU.padTo(addr+": "+instruction,20);
		g = g +" A:"+CU.hex2(getRegister("A").readValue());
		g = g +" B:"+CU.hex2(getRegister("B").readValue());
		g = g +" X:"+CU.hex4(getRegister("X").readValue());
		g = g +" Y:"+CU.hex4(getRegister("Y").readValue());
		g = g +" U:"+CU.hex4(getRegister("U").readValue());
		g = g +" SP:"+CU.hex4(getRegister("SP").readValue());
		g = g +"    CF:"+cf+" ZF:"+zf;
		System.out.println(g);
			*/
	}
	
	
	
	
	
	
	public Accessable decodeParameter(String param, boolean word) {
		
		if(param.startsWith("#$")) {
			return new AccessConstant(Integer.parseInt(param.substring(2),16),word);
		}
		
		if(param.startsWith("<$")) {
			Register dp = getRegister("DP");
			int p = (dp.readValue()<<8) + Integer.parseInt(param.substring(2),16);
			return new MemoryAccess(this,p,word);
		}
		
		// TODO "[" before this
		if(param.contains(",")) {
			int i = param.indexOf(",");
			String left = param.substring(0, i).trim();
			String right = param.substring(i+1).trim();
			int ofs = 0;
			if(!left.isEmpty()) {
				if(left.equals("B")) {
					ofs = getRegister("B").readValue();
				} else if(left.equals("A")) {
					ofs = getRegister("A").readValue();
				} else {
					ofs = Integer.parseInt(left);
				}
			}
			int adj = 0;
			if(right.startsWith("--")) {
				adj = -2;
				right = right.substring(2);
			} else if(right.startsWith("-")) {
				adj = -1;
				right = right.substring(1);
			} else if(right.endsWith("++")) {
				adj = 2;
				right = right.substring(0,right.length()-2);
			} else if(right.endsWith("+")) {
				adj = 1;
				right = right.substring(0,right.length()-1);
			}
			IndexAccess ia = new IndexAccess(this,getRegister(right),word);
			ia.setAdjust(adj);
			ia.setOffset(ofs);
			return ia;
		}
						
		throw new RuntimeException("Unknown param type '"+param+"'");
		
	}
	
	List<Register> parseRegisterList(String par) {
		List<Register> ret = new ArrayList<Register>();
		String [] regs = par.split(",");
		for(String r : regs) {
			ret.add(getRegister(r));
		}
		return ret;
	}
	
	public void run(int address) {
		
		// Good info on instruction set:
		// http://atjs.mbnet.fi/mc6809/Information/6809.htm	
		
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
			
			//System.out.println("::"+line+"::");
			
			if(
				loadStore(op,par) ||
				math(op,par) ||
				flow(op,par) ||
				stack(op,par) ||
				misc(op,par)) 
			{
				// OK
				debug(addr,instruction);
			} else {
				System.out.println(">> "+instruction);
				throw new RuntimeException("Unknown instruction :"+op+":"+par+":");
			}	
		
		}
						
	}
	
	boolean loadStore(String op, String par) {
		if(op.startsWith("LD")) {
			Register r = getRegister(op.substring(2));
			Accessable ac = decodeParameter(par,r.isWordSize());
			r.writeValue(setNZv(ac.readValue()));
			return true;
		}
		
		if(op.startsWith("ST")) {
			Register r = getRegister(op.substring(2));
			Accessable ac = decodeParameter(par,r.isWordSize());
			ac.writeValue(setNZv(r.readValue()));
			return true;
		}
		
		return false;
	}
	
	boolean math(String op, String par) {
		if(op.startsWith("CLR")) {
			Accessable ac;
			if(par!=null) {
				ac = decodeParameter(par,false);
			} else {
				ac = getRegister(op.substring(3));
			}
			ac.writeValue(0);
			cf = false;
			zf = true;
			return true;
		}
		
		if(op.startsWith("INC")) {
			Accessable ac;
			if(par!=null) {
				ac = decodeParameter(par,false);
			} else {
				ac = getRegister(op.substring(3));
			}
			int val = ac.readValue() + 1;
			if(ac.isWordSize()) {
				if(val>0xFFFF) val = 0;
			} else {
				if(val>0xFF) val = 0;
			}
			zf = (val == 0);
			ac.writeValue(val);			
			return true;
		}
		
		if(op.startsWith("DEC")) {
			Accessable ac;
			if(par!=null) {
				ac = decodeParameter(par,false);
			} else {
				ac = getRegister(op.substring(3));
			}
			int val = ac.readValue() - 1;
			if(val<0) {
				if(ac.isWordSize()) {
					val = 0xFFFF;
				} else {
					val = 0xFF;
				}
			}
			zf = (val == 0);
			ac.writeValue(val);			
			return true;
		}
		
		if(op.startsWith("AND")) {				
			Register r = getRegister(op.substring(3));
			Accessable ac = decodeParameter(par,r.isWordSize());
			int v = r.readValue() & ac.readValue();
			r.writeValue(setNZv(v));
			return true;
		}
		
		if(op.startsWith("BIT")) {				
			Register r = getRegister(op.substring(3));
			Accessable ac = decodeParameter(par,r.isWordSize());
			int v = r.readValue() & ac.readValue();
			setNZv(v);
			return true;
		}
		
		if(op.startsWith("OR")) {				
			Register r = getRegister(op.substring(2));
			Accessable ac = decodeParameter(par,r.isWordSize());
			int v = r.readValue() | ac.readValue();
			r.writeValue(setNZv(v));
			return true;
		}
		
		if(op.startsWith("ADD")) {
			Register r = getRegister(op.substring(3));
			Accessable ac = decodeParameter(par,r.isWordSize());
			int v = r.readValue() + ac.readValue();
			r.writeValue(setNZVC(v,r.isWordSize()));
			return true;
		}
		
		if(op.startsWith("CMP")) {
			Register r = getRegister(op.substring(3));
			Accessable ac = decodeParameter(par,r.isWordSize());
			int v = r.readValue() - ac.readValue();
			setNZVC(v,r.isWordSize());
			return true;
		}
		
		if(op.startsWith("TST")) {
			Accessable ac;
			if(par!=null) {
				ac = decodeParameter(par,false);
			} else {
				ac = getRegister(op.substring(3));
			}
			int v = ac.readValue();			
			setNZ(v);
			return true;
		}
		
		if(op.startsWith("ASL")) {				
			Register r = getRegister(op.substring(3));				
			int v = r.readValue()<<1;
			cf = (v>255);
			v = v & 0xFF;
			zf = (v==0);				
			r.writeValue(v);
			return true;
		}
		
		if(op.startsWith("LSR")) {				
			Register r = getRegister(op.substring(3));
			int v = r.readValue();
			cf = ((v & 1) == 1);
			v = v>>1;
			zf = (v==0);				
			r.writeValue(v);
			return true;
		}
		
		if(op.startsWith("ROL")) {			
			Accessable ac;
			if(par!=null) {
				ac = decodeParameter(par,false);
			} else {
				ac = getRegister(op.substring(3));
			}
			int v = ac.readValue();
			v = v << 1;
			if(cf) v = v | 1;
			cf = (v>255);
			v = v & 0xFF;
			zf = (v==0);
			ac.writeValue(v);
			return true;
		}
		
		if(op.equals("MUL")) {
			int a = getRegister("A").readValue();
			int b = getRegister("B").readValue();
			a = a * b;
			a = a &0xFFFF;
			cf = ((a>>7)&1)!=0;
			zf = (a==0);
			getRegister("D").writeValue(a);
			return true;
		}
		
		return false;
	}
	
	boolean flow(String op, String par) {
		
		int dest = -1;
		if(par != null && par.startsWith("$")) {
			dest = Integer.parseInt(par.substring(1),16);
		}
		
		if(op.equals("JSR") || op.equals("BSR")) {			
			push(pc,true);
			pc = findCodeTarget(dest);
			return true;			
		}
		
		if(op.equals("RTS")) {
			pc = pop(true);			
			return true;
		}
		
		if(op.equals("BCC")) {			
			if(!cf) {
				pc = findCodeTarget(dest);											
			}
			return true;
		}		
		
		if(op.equals("BRA") || op.equals("JMP")) {			
			pc = findCodeTarget(dest);			
			return true;
		}
		
		if(op.equals("BEQ")) {			
			if(zf) {
				pc = findCodeTarget(dest);											
			}
			return true;
		}
		if(op.equals("BNE")) {			
			if(!zf) {
				pc = findCodeTarget(dest);											
			}
			return true;
		}
		
		return false;
	}
	
	boolean stack(String op, String par) {
		
		if(op.equals("PSHS")) {
			String[] rs = par.split(",");
			for(String s : rs) {
				Register r = getRegister(s);
				push(r.readValue(),r.isWordSize());
			}
			// No flags
			return true;
		}		
		
		if(op.equals("PULS")) {
			String[] rs = par.split(",");
			for(String s : rs) {
				if(s.equals("PC")) {
					pc = pop(true);
					continue;
				}
				Register r = getRegister(s);
				r.writeValue(pop(r.isWordSize()));				
			}
			// No flags
			return true;
		}
		
		return false;
	}
	
	boolean misc(String op, String par) {
		
		if(op.equals("ABX")) {
			Register b = getRegister("B");
			Register x = getRegister("X");
			x.writeValue(x.readValue()+b.readValue());
			// No flags
			return true;
		}
		
		if(op.startsWith("LEA")) {
			String reg = op.substring(3);
			Register r = getRegister(reg);
			Accessable ac = decodeParameter(par,r.isWordSize());
			int ea = ac.getEffectiveAddress();
			r.writeValue(ea);
			if(reg.equals("X") || reg.equals("Y")) {
				zf = (ea==0);
			}
			return true;
		}
		
		if(op.equals("TFR")) {
			List<Register> regs = parseRegisterList(par);
			if(regs.size()!=2) {
				throw new RuntimeException("Expected two registers");
			}
			Register src = regs.get(0);
			Register dst = regs.get(1);
			dst.writeValue(src.readValue());
			return true;
		}
		
		if(op.equals("EXG")) {
			List<Register> regs = parseRegisterList(par);
			if(regs.size()!=2) {
				throw new RuntimeException("Expected two registers");
			}
			Register src = regs.get(0);
			int srcVal = src.readValue();
			Register dst = regs.get(1);
			int dstVal = dst.readValue();
			dst.writeValue(srcVal);
			src.writeValue(dstVal);
			return true;
		}
		
		return false;
	}

}
