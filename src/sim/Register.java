package sim;

public class Register implements Accessable {
	
	private String name;
	private boolean isWordSize;
	private int value;
	
	public static void checkSize(int value, boolean isWordSize) {
		if(value<0) throw new RuntimeException ("Invalid value "+value);
		if(isWordSize) {
			if(value>65535) {
				throw new RuntimeException("Invalid word value "+value);
			}
		} else {
			if(value>255) {
				throw new RuntimeException("Invalid byte value "+value);
			}
		}
	}
	
	public Register(String name, boolean isWordSize) {
		this.name = name;
		this.isWordSize = isWordSize;
	}
	
	public String getName() {
		return name;
	}

	@Override
	public boolean isWordSize() {
		return isWordSize;
	}

	@Override
	public int readValue() {
		return value;
	}

	@Override
	public void writeValue(int value) {
		checkSize(value,isWordSize);
		this.value = value;		
	}

	@Override
	public int getEffectiveAddress() {
		throw new RuntimeException("Cannot get the effective address of a register");
	}

}
