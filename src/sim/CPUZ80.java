package sim;

import java.util.List;

public class CPUZ80 extends CPU {
	
	int [] memory = new int[64*1024];
	
	int pc;

	public CPUZ80(List<String> lines) {
		super(lines);
		
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
					flow(op,par)
				) 
			{
				debug(addr,instruction);
			} else {			
				throw new RuntimeException("Unknown instruction "+addr+":"+op+":"+par);
			}
		}
	}
	
	public boolean flow(String op, String par) {
		if(op.equals("JP")) {
			if(par.startsWith("$")) {
				int dest = Integer.parseInt(par.substring(1),16);
				pc = findCodeTarget(dest);
				return true;
			}
		}
		return false;
	}

}
