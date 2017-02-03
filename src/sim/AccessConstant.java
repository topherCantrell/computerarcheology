package sim;

public class AccessConstant implements Accessable {
		
		private int value;
		private boolean isWordSize;
		
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
			throw new RuntimeException("Cannot write to constant value");			
		}

		@Override
		public boolean isWordSize() {
			return isWordSize;
		}

		@Override
		public int getEffectiveAddress() {
			throw new RuntimeException("Cannot get the effective address of a constant value");
		}
		
	}
