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
		throw new RuntimeException("Implement me");
	}

	@Override
	public int pop(boolean word) {
		throw new RuntimeException("Implement me");
	}
	
	public void debug(String addr, String instruction) {
		
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
					load(op,par)
				) 
			{
				debug(addr,instruction);
			} else {			
				throw new RuntimeException("Unknown instruction "+addr+":"+op+":"+par);
			}
		}
	}
	
	public boolean load(String op, String par) {
		if(op.equals("LD")) {
			// NONE of the LD opcodes affect the flags			
			String [] parts = par.split(",");			
			boolean isWordAccess = false;
			Accessable left=null,right=null;
			// One of these must be a register
			if(!parts[0].startsWith("$") && !parts[0].startsWith("(")) {
				// src is a register
				left = getRegister(parts[0]);
				isWordAccess = left.isWordSize();
			} else if(!parts[1].startsWith("$") && !parts[1].startsWith("(")) {
				// src is a register
				right = getRegister(parts[0]);
				isWordAccess = right.isWordSize();
			} else {
				throw new RuntimeException("One of these must be a register");
			}
			
			if(parts[0].startsWith("(")) {
				left = new MemoryAccess(this,Integer.parseInt(parts[0].substring(1,parts[0].length()-1),16),isWordAccess);
			} 
			if(parts[1].startsWith("(")) {
				right = new MemoryAccess(this,Integer.parseInt(parts[1].substring(1,parts[1].length()-1),16),isWordAccess);
			} 
			if(parts[0].startsWith("$")) {
				left = new AccessConstant(Integer.parseInt(parts[0].substring(1),16),isWordAccess);
			}
			if(parts[1].startsWith("$")) {
				right = new AccessConstant(Integer.parseInt(parts[1].substring(1),16),isWordAccess);
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
			push(pc,true);
			int dest = Integer.parseInt(par.substring(1),16);
			pc = findCodeTarget(dest);
			return true;
		}
		
		return false;
	}

}
