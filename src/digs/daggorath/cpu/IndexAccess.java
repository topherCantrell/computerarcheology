package digs.daggorath.cpu;

public class IndexAccess implements Accessable {
	
	CPU6809 cpu;
	Register reg;
	int adjust;
	int offset;
	boolean isWordAccess;
						
	IndexAccess(CPU6809 cpu, Register reg, boolean isWordAccess) {
		this.cpu = cpu;
		this.reg = reg;		
		this.isWordAccess = isWordAccess;		
	}
	
	public void setAdjust(int adjust) {
		this.adjust = adjust;
	}
	
	public void setOffset(int offset) {
		this.offset = offset;
	}
		
	@Override
	public int readValue() {		
		int p = getEffectiveAddress();
		return cpu.readMemory(p, isWordAccess);		
	}
	
	@Override
	public void writeValue(int value) {		
		int p = getEffectiveAddress();
		cpu.writeMemory(p, value, isWordAccess);		
	}

	@Override
	public boolean isWordSize() {
		return isWordSize();
	}

	@Override
	public int getEffectiveAddress() {
		if(adjust<0) {
			reg.writeValue(reg.readValue()+adjust);
		}
		
		int p = reg.readValue()+offset;		
		
		if(adjust>0) {
			reg.writeValue(reg.readValue()+adjust);
		}
		
		return p;
	}
}