package sim;

import java.util.List;

public class CPUZ80 extends CPU {
	
	// http://www.z80.info/z80flag.htm
	
	int [] memory = new int[64*1024];
	
	int pc;

	public CPUZ80(List<String> lines) {
		super(lines);
		
		registers.put("SP", new Register("SP",true));
		registers.put("A", new Register("A",false));
		registers.put("B", new Register("A",false));
		registers.put("H", new Register("H",false));
		registers.put("L", new Register("L",false));
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
		// SP = SP - 1
		// write LSB
		// SP = SP - 1
		// write MSB
		Accessable sp = getRegister("SP");
		int spval = sp.readValue();
		spval = spval - 1;
		memory[spval] = value&0xFF;
		if(word) {
			spval = spval - 1;
			memory[spval] = (value>>8)&0xFF;
		}
		sp.writeValue(spval);		
	}

	@Override
	public int pop(boolean word) {
		// read MSB
		// SP = SP - 1
		// read LSB
		// SP = SP - 1
		throw new RuntimeException("Implement me");
	}
	
	public void debug(String addr, String instruction) {
		System.out.println(addr+": "+instruction);
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
			
			if(
					flow(op,par) ||
					load(op,par) ||
					math(op,par)
				) 
			{
				debug(addr,instruction);
			} else {			
				throw new RuntimeException("Unknown instruction "+addr+":"+op+":"+par);
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
	
	public void setFlags(int value, int C, int Z, int P, int S, int N, int H) {
		// -1 means calculate from value		
	}
	
	public boolean math(String op, String par) {
		if(op.equals("AND")) {
			int val = getRegister(par).readValue();
			int aval = getRegister("A").readValue();
			aval = aval & val;
			getRegister("A").writeValue(aval);			
			//             C   Z   P   S  N  H
			setFlags(aval, 0, -1, -1, -1, 0, 1); // Set Z,S,P   C=0,N=0,H=1
		}
		return false;
	}
	
	public boolean load(String op, String par) {
		if(op.equals("LD")) {
			
			// NONE of the LD opcodes affect the flags
			
			String [] parts = par.split(",");			
			
			// One of these must be a register
			Accessable left,right;
			left = decodeRegister(parts[0]);		
			right = decodeRegister(parts[1]);
			
			// The other can be a register or something else
			if(left==null) {
				left = decodeNonRegister(parts[0],right.isWordSize());
			}
			if(right==null) {
				right = decodeNonRegister(parts[1],left.isWordSize());
			}			
			
			left.writeValue(right.readValue());
			
			return true;
		}
		return false;
	}
	
	public boolean flow(String op, String par) {
		if(op.equals("JP")) {
			if(par.startsWith("$")) {
				int dest = Integer.parseInt(par.substring(1),16);
				pc = findCodeTarget(dest);
				return true;
			}
		}
		
		if(op.equals("CALL")) {
			int dest = Integer.parseInt(par.substring(1),16);
			if(dest==0x33) {
				ROMCALL_DISPLAY();
				return true;
			}
			push(pc,true);			
			pc = findCodeTarget(dest);
			return true;
		}
		
		
		return false;
	}
	
	void ROMCALL_DISPLAY() {
		System.out.println("DISPLAY:"+getRegister("A").readValue());
	}

}
