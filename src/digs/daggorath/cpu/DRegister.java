package digs.daggorath.cpu;

public class DRegister extends Register {

	Register a,b;
	
	public DRegister(Register a, Register b) {
		super("D", true);
		this.a = a;
		this.b = b;
	}
	
	@Override
	public int readValue() {
		return (a.readValue()<<8) | b.readValue();
	}

	@Override
	public void writeValue(int value) {
		a.writeValue(value>>8);
		b.writeValue(value & 0xFF);	
	}
		
}
