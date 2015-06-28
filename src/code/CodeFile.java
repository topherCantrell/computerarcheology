package code;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

import cpu.CPU;

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
				cpu = CPU.getCPU(c);				
			}
			if(s.startsWith(";;%%-")) {
				
				int i = s.indexOf(" ");
				int j = s.indexOf(" ",i+1);
				
				String pa = s.substring(i+1,j);
				String re = s.substring(j+1).trim();				
				
				tables.add(new AddressTable(Paths.get("content/",pa), re, tables.size()));
				
			}
		}
		
		collectLabels();
	}
	
	private void collectLabels() {
		
		List<String> current = new ArrayList<String>();
		
		for(int x=0;x<code.size();++x) {
		
			CodeLine r = code.get(x);
			if(r.data==null || r.data.size()!=0) {
				// No data and no opcode. Collect any labels for the next real line.
				if(r.label!=null) {
					current.add(r.label);					
				}
			} else {
				// This is a real line of code ... attach any labels collected above.
				if(r.label!=null) {
					current.add(r.label);					
				}
				if(current.size()>0) {
					r.collectedLabels = new String[current.size()];
					for(int y=0;y<current.size();++y) {
						r.collectedLabels[y] = current.get(y);
					}
					current.clear();
				}
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

	public String getCodeLabel(int address) {
		// If the address is found then return either:
		// - the first label if there is one or
		// - flag the line and return the hex address
		for(CodeLine c : code) {
			if(c.address == address) {
				if(c.collectedLabels!=null) {
					return c.collectedLabels[0];
				}
				c.flag = true;
				return "$"+CU.hex4(address);
			}
		}		
		return null;		
	}

}
