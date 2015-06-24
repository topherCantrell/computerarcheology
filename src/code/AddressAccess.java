package code;

public class AddressAccess {
	
	public BusType accessType;
	
	public BusDir bus;
	
	public boolean isCode;
	
	public int address;
	
	public String toString() {
		return bus.toString()+" "+isCode+" "+accessType+" "+address;
	}

}
