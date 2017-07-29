package cleans;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

import util.CU;

public class CPUJS {

	static void checkParams(String code) {
		for(int x=0;x<code.length();x=x+2) {
			char c = code.charAt(x);
			if( (c>='0' && c<='9') || (c>='A' && c<='F')) continue;
			
			switch(c) {
			case 'p': continue; // Zero or Direct Page
			case 'b': continue; // Immediate byte
			case 'w': continue; // Immediate word
			case 't': continue; // Two byte absolute address
			case 'r': continue; // One byte relative code destination
			case 's': continue; // Two byte relative code destination
			case 'i': continue; // One byte signed offset
			case 'k': continue; // Two byte signed offset
			case 'y': continue; // 6809 post bytes
			case 'z': continue; // 6809 register pair
			case 'x': continue; // 6809 system stack push registers
			case 'q': continue; // 6809 system stack pull registers
			case 'u': continue; // 6809 user stack push registers
			case 'v': continue; // 6809 user stack pull registers			
			case 'o': continue; // One byte port
			}
			
			throw new RuntimeException("Unknown Param "+c);
		}
	}
	
	public static void main(String [] args) throws Exception
	{
		List<String> lines = Files.readAllLines(Paths.get("src/cpu/Z80GB.js"));
		for(String line : lines) {
			if(line.startsWith("{\"mnem")) {
				int i = line.indexOf("[");
				int j = line.lastIndexOf("]");
				String m = line.substring(i+2, j);
				String mm = "";
				while(!m.isEmpty()) {
					i = m.indexOf('"');
					mm = mm + m.substring(0, i);
					m = m.substring(i+1);
					if(!m.isEmpty()) {
						m = m.substring(2);
					}
				}
				i = line.indexOf("code\":")+7;
				j = line.indexOf('"',i);
				String cc = line.substring(i, j);
				checkParams(cc);
				
				i = line.indexOf("bus\":")+6;
				j = line.indexOf('"',i);
				String bus = line.substring(i, j);				
				
				String comb = "{\"mnem\":"+CU.padTo("\""+mm+"\",", 16);
				comb = comb + "\"code\":"+CU.padTo("\""+cc+"\",", 14);
				comb = comb + "\"bus\":"+CU.padTo("\""+bus+"\"", 8);
				comb = comb + "},";
				
				System.out.println(comb);
			}
		}
	}
	

}
