package code;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class AddressTable {
	
	public String name;
	Path inputFile;
	Path htmlRef;
	
	List<Integer> rangeStarts = new ArrayList<Integer>();
	List<Integer> rangeStops = new ArrayList<Integer>();
	
	List<AddressDef> defs = new ArrayList<AddressDef>();
	
	public AddressTable(Path path) throws IOException {
		this(path,null,null);
	}
	
	public AddressTable(Path path, String name, Path htmlRef) throws IOException {	
		
		this.name = name;
		this.inputFile = path;
		this.htmlRef = htmlRef;	
		
		List<String> lines = Files.readAllLines(path);
				
		for(String line : lines) {
			
			if(line.startsWith("%%range")) {
				String [] rents = line.substring(8).trim().split(",");
				for(String r : rents) {
					String [] rs = r.split(":");
					rangeStarts.add(CU.parseInt(rs[0].trim(), 16));
					rangeStops.add(CU.parseInt(rs[1].trim(), 16));
				}				
				continue;
			}
			
			if(!line.startsWith("||")) {
				continue;
			}
			if(line.startsWith("||=")) {
				continue;
			}
			
			String [] parts = line.trim().split("\\|\\|");
			String address = parts[1].trim();
			if(address.length()==0) {
				continue;
			}
			String n = parts[2].trim();			
			defs.add(new AddressDef(address,n));
		}
		
	}
	
	public boolean hasAddress(int address) {
		for(int x=0;x<rangeStarts.size();++x) {
			if(address>=rangeStarts.get(x) && address<=rangeStops.get(x)) {
				return true;
			}
		}
		return false;
	}
	
	public AddressDef getEntry(int address, BusDir bus) {
		for(AddressDef ad : defs) {
			if(ad.isMe(address,bus)) {
				return ad;
			}
		}
		return null;
	}
	
}
