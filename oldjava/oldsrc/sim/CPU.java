package sim;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public abstract class CPU {
	
	protected List<String> lines;	
	protected Map<String,Register> registers = new HashMap<String,Register>();
	
	public abstract int readMemory(int addr, boolean isWordSize);	
	public abstract void writeMemory(int addr, int value, boolean isWordSize);
	public abstract void push(int value, boolean word);	
	public abstract int pop(boolean word);	
	public abstract void run(int address);	
	
	public CPU(List<String> lines) {
		this.lines = lines;
	}
	
	public void call(int address) {
		push(0xFFFF,true);
		run(address);
	}
	
	public Register getRegister(String reg) {
		Register ret = registers.get(reg);
		if(ret==null) {
			throw new RuntimeException("Unknown register '"+reg+"'");
		}
		return ret;
	}	
	
	public int readByte(int addr) {
		return readMemory(addr,false);
	}
	
	public int readWord(int addr) {
		return readMemory(addr,true);
	}
	
	public void writeByte(int addr, int value) {
		writeMemory(addr,value,false);
	}
	
	public void writeWord(int addr, int value) {
		writeMemory(addr,value,true);
	}
	
	public int findCodeTarget(int address) {
		String adr = Integer.toString(address,16).toUpperCase();
		for(int x=0;x<lines.size();++x) {
			if(lines.get(x).startsWith(adr+":")) {
				return x;
			}
		}
		throw new RuntimeException("No code target "+address);
	}

}
