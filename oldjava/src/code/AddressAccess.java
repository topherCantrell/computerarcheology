package code;

public class AddressAccess implements Comparable<AddressAccess> {
	
	public BusType accessType;
	
	public BusDir bus;
	
	public boolean isCode;
	
	public int address;
		
	@Override
	public int compareTo(AddressAccess other) {
		return address - other.address;
	}
	
	@Override
	public boolean equals(Object o) {
		AddressAccess other = (AddressAccess)o;
		if(accessType==other.accessType && isCode==other.isCode && address==other.address) {
			return true;
		}
		return false;
	}	
	
	@Override
	public String toString() {
		String ret = "|| " + CU.hex4(address);
		if(accessType==BusType.PORT){
			ret = ret + "p";
		}
						
		ret = ret +" || || ||";
		return ret;
	}
		

}
