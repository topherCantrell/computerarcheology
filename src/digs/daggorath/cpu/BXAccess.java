package digs.daggorath.cpu;

public class BXAccess implements Accessable {
		
	CPU6809 cpu;
		boolean word;
		boolean lea;
		int adjust = 0;
		
		BXAccess(CPU6809 cpu, boolean word, boolean lea) {
			this.cpu = cpu;
			this.word = word;
			this.lea = lea;
		}

		@Override
		public int readValue() {
			/*
			int offset = cpu.b;
			if(adjust<0) cpu.x = cpu.x + adjust;
			int ret;
			if(word) {
				ret = cpu.readWord(cpu.x+offset);				
			} else {
				ret = cpu.readByte(cpu.x+offset);	
			}				
			if(adjust>0) cpu.x = cpu.x + adjust;
			return ret;
			*/
			return 0;
		}

		@Override
		public void writeValue(int value) {
			/*
			int offset = cpu.b;
			if(adjust<0) cpu.x = cpu.x + adjust;
			if(word) {
				cpu.writeWord(cpu.x+offset, value);				
			} else {
				cpu.writeWord(cpu.x+offset, value);	
			}				
			if(adjust>0) cpu.x = cpu.x + adjust;
			return;		
			*/	
		}

		@Override
		public boolean isWordSize() {
			// TODO Auto-generated method stub
			return false;
		}

		@Override
		public int getEffectiveAddress() {
			// TODO Auto-generated method stub
			return 0;
		}
		
	}