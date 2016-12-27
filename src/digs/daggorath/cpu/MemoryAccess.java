package digs.daggorath.cpu;

public class MemoryAccess implements Accessable {
		
		CPU6809 cpu;
		int addr;
		boolean isWordAccess;
		
		MemoryAccess(CPU6809 cpu, int addr, boolean isWordAccess) {
			this.cpu = cpu;
			this.addr = addr;
			this.isWordAccess = isWordAccess;
		}

		@Override
		public int readValue() {
			if(isWordAccess) {
				return cpu.readWord(addr);
			} else {
				return cpu.readByte(addr);				
			} 
		}

		@Override
		public void writeValue(int value) {			
			if(isWordAccess) {
				cpu.writeWord(addr,value);				
			} else {
				cpu.writeByte(addr,value);			
			}
		}

		@Override
		public boolean isWordSize() {
			return isWordAccess;
		}

		@Override
		public int getEffectiveAddress() {
			return addr;
		}
		
	}