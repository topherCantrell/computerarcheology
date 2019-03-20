package code;

public class AddressDef {
	
	BusDir busDir;
	BusType busType;
	
	int startAddress;
	int endAddress;
	
	public String name;
	
	public AddressDef(String addr, String n) {
		
		busType = BusType.MAIN;
		
		name = n;
		
		if(addr.endsWith("r")) {
			busDir = BusDir.READ;
			addr = addr.substring(0,addr.length()-1);
		} else if(addr.endsWith("w")) {
			busDir = BusDir.WRITE;
			addr = addr.substring(0,addr.length()-1);
		} else {
			busDir = BusDir.BOTH;			
		}
		
		if(addr.endsWith("p")) {
			busType = BusType.PORT;
			addr = addr.substring(0,addr.length()-1);
		}
		
		int i = addr.indexOf(":");
		if(i>0) {
			startAddress = CU.parseInt(addr.substring(0,i).trim(), 16);
			endAddress = CU.parseInt(addr.substring(i+1).trim(), 16);
		} else {
			startAddress = CU.parseInt(addr.trim(), 16);
			endAddress = -1;
		}
		
	}

	public boolean isMe(int address, BusDir b, BusType type) {
		
		if(type!=busType) {
			// Not even the right bus
			return false;
		}
		
		// Single address or within a range
		if(endAddress==-1) {
			if(address != startAddress) {
				return false;
			}
		} else {
			if(address<startAddress || address>endAddress) {
				return false;
			}
		}
		
		// Exact match
		if(b==busDir) {
			return true;
		}
		
		// If we are both directions then this is good
		if(busDir==BusDir.BOTH) {
			return true;
		}
		
		return false;
		
	}

	public String getTarget() {
		String ret = CU.hex4(startAddress);
		if(busType==BusType.PORT) {
			ret = ret + "p";
		}
		if(busDir==BusDir.READ){
			ret = ret + "r";
		}
		if(busDir==BusDir.WRITE){
			ret = ret + "w";
		}
		return ret;
	}
	

}
