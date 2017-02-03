package sim;

public class RegisterPair extends Register {

	Register msb,lsb;
	
	public RegisterPair(String name, Register msb, Register lsb) {
		super(name, true);
		this.msb = msb;
		this.lsb = lsb;
	}
	
	@Override
	public int readValue() {
		return (msb.readValue()<<8) | lsb.readValue();
	}

	@Override
	public void writeValue(int value) {
		msb.writeValue(value>>8);
		lsb.writeValue(value & 0xFF);	
	}
		
}
