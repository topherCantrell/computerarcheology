package digs.daggorath.cpu;

public class AccessConstant implements Accessable {
		
		int value;
		boolean isWordSize;
		
		AccessConstant(int value, boolean isWordSize) {
			this.value = value;
			this.isWordSize = isWordSize;
		}

		@Override
		public int readValue() {
			return value;
		}

		@Override
		public void writeValue(int value) {
			throw new RuntimeException("Cannot write constant");			
		}

		@Override
		public boolean isWordSize() {
			return isWordSize;
		}

		@Override
		public int getEffectiveAddress() {
			throw new RuntimeException("Cannot get effective address of a constant");
		}
		
	}
