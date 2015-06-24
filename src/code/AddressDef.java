package code;

public class AddressDef {
	
	BusDir bus;
	
	int startAddress;
	int endAddress;
	
	public String name;
	
	public AddressDef(String addr, String n) {
		
		name = n;
		
		if(addr.endsWith("r")) {
			bus = BusDir.READ;
			addr = addr.substring(0,addr.length()-1);
		} else if(addr.endsWith("w")) {
			bus = BusDir.WRITE;
			addr = addr.substring(0,addr.length()-1);
		} else {
			bus = BusDir.BOTH;
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

	public boolean isMe(int address, BusDir b) {
		
		if(endAddress==-1) {
			if(address != startAddress) {
				return false;
			}
		} else {
			if(address<startAddress || address>endAddress) {
				return false;
			}
		}
		
		if(b==bus) {
			return true;
		}
		
		if(bus==BusDir.BOTH) {
			return true;
		}
		
		return false;
		
	}

}
