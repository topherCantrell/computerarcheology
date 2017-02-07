package sim;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

import code.CU;

public class DissReader {
	
	private List<String> raw;
	private List<String> lines;
	
	public DissReader(String name) throws IOException {
		raw = Files.readAllLines(Paths.get(name));
		lines = new ArrayList<String>();
		
		for(String line : raw) {
			int i = line.indexOf(";");
			if(i>=0) {
				line = line.substring(0,i);
			}
			line = line.trim();
			if(line.isEmpty()) continue;
			if(!line.contains(" ") && line.endsWith(":")) {
				continue;
			}
			line = CU.replaceAll(line,"  "," ");

			for(int pos=6;pos<line.length();pos=pos+3) {
				if(!CU.isTwoDigitHex(line,pos)) {
					line = line.substring(0,pos)+":"+line.substring(pos);
					break;
				}
			}
			lines.add(line);	
		}		
		
	}
	
	public void getData(int [] memory) {
		for(String s : lines) {
			
			int i = s.indexOf(":",5);
			if(i>0) {
				s = s.substring(0,i);
			}			
			
			int addr = Integer.parseInt(s.substring(0,4),16);
			s = s.substring(6).trim();
			while(s.length()>0) {
				int val = Integer.parseInt(s.substring(0,2),16);
				s = s.substring(2).trim();
				memory[addr] = val;
				++addr;
			}
			
		}
	}

	public List<String> getCleaned() {
		return lines;
	}

	

}
