package web;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

import bus.BusDir;
import bus.BusType;
import util.CU;

public class AddressMap {
	
	List<AddressTableEntry> entries = new ArrayList<AddressTableEntry>();
	
	public AddressTableEntry findEntryForAccess(int address, BusDir dir, BusType type) {
		AddressTableEntry ret = null;
		
		if(dir==BusDir.BOTH) {
			// We can only pick one name. Read usually happens first, so
			// let's pick READ.
			dir = BusDir.READ;
		}
		
		for(AddressTableEntry e : entries) {
									
			if(address>=e.start && address<=e.end) {
				
				boolean match = false;
				if(e.dir == dir) match = true;
				else if(e.dir==BusDir.BOTH) match = true;
				
				if(e.type!=type) match = false;
				
				if(match) {				
					if(ret!=null) {
						throw new RuntimeException("Multiple matches for address "+CU.hex4(address));
					}
					ret = e;				
				}				
				
			}
		}
		
		return ret;
	}
			
	public void parseMaps(List<String> lines) {
		boolean inBlock = false;
		int pos = 0;
		for(String s : lines) {
			++pos;
			s=s.trim();
			if(s.toUpperCase().startsWith("{{{MEMORY")) {
				if(inBlock) {
					throw new RuntimeException("Line "+pos+": Nested memory blocks are not allowed.");
				}
				inBlock = true;
			}
			if(s.toUpperCase().startsWith("}}}")) {
				// Might be other kinds of blocks, but since we don't nest ...
				inBlock = false;
			}
			if(inBlock && s.startsWith("||")) {
				String [] row = s.split("\\|\\|");
				if(row.length<4) {
					throw new RuntimeException("Line "+pos+": must have ||ADDRESS||NAME||DESC||");
				}
				String address = row[1].trim();
				String name = row[2].trim();
				String description = row[3].trim();
				if(address.isEmpty()) continue; // Allow spacer rows
				if(address.startsWith("=")) continue; // This is the header row
				
				BusDir dir = BusDir.BOTH;
				if(address.toUpperCase().endsWith("R")) {
					dir=BusDir.READ;
					address = address.substring(0, address.length()-1);
				} else if(address.toUpperCase().endsWith("W")) {
					dir=BusDir.WRITE;
					address = address.substring(0, address.length()-1);
				}
				
				BusType type = BusType.MAIN;
				if(address.toUpperCase().endsWith("P")) {
					type = BusType.PORT;
					address = address.substring(0, address.length()-1);
				}
				
				int start;
				int end;
				int i = address.indexOf(":");
				if(i<0) {
					start = Integer.parseInt(address,16);
					end = start;
				} else {
					start = Integer.parseInt(address.substring(0,i),16);
					end = Integer.parseInt(address.substring(i+1),16);
				}
				
				AddressTableEntry entry = new AddressTableEntry();				
				entry.start = start;
				entry.end = end;
				entry.dir = dir;
				entry.type = type;
				entry.name = name;
				entry.description = description;
				
				entries.add(entry);
				
			}
		}
	}

	public static void main(String[] args) throws Exception {
		
		List<String> lines = Files.readAllLines(Paths.get("content/Arcade/SpaceInvaders/Hardware.mark"));
		AddressMap am = new AddressMap();
		am.parseMaps(lines);
		
		AddressTableEntry e = am.findEntryForAccess(0x2, BusDir.READ, BusType.PORT);
		System.out.println(":"+CU.hex4(e.start)+":"+CU.hex4(e.end)+":"+e.name+":"+e.description+":");
		
	}

}
