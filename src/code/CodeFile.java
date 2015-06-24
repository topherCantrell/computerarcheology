package code;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

import cpu.CPU;
import cpu.CPU_6502;

public class CodeFile {
	
	public List<AddressTable> tables = new ArrayList<AddressTable>();
	public List<CodeLine> code = new ArrayList<CodeLine>();
	
	public CPU cpu = null;
		
	public CodeFile(Path codeFile) throws IOException {
		
		List<String> lines = Files.readAllLines(codeFile);
		
		int lineno = 1;
		for(String s : lines) {
			
			code.add(new CodeLine(s,codeFile.toString(),lineno));
			++lineno;
			
			if(s.startsWith(";;%%cpu")) {
				String c = s.substring(8).trim();
				if(c.equals("6502")) {
					cpu = new CPU_6502();
				}
			}
			if(s.startsWith(";;%%-")) {
				
				int i = s.indexOf(" ");
				int j = s.indexOf(" ",i+1);
				
				String nm = s.substring(4,i);
				String pa = s.substring(i+1,j);
				String re = s.substring(j+1).trim();				
				
				tables.add(new AddressTable(Paths.get("content/",pa), nm, Paths.get(re)));
				
			}
		}
	}
	
	public AddressTable getAddressTable(int address) {
		
		for(AddressTable ret : tables) {
			if(ret.hasAddress(address)) {
				return ret;
			}
		}
		
		return null;
		
	}

}
