package cleans;

import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class OpcodeFrag {
	
	public static void main(String [] args) throws Exception {
		
		Path p = Paths.get("src/cpu/Z80.js");
		
		// {"mnem":"ORA (p),Y", "code":"11pp", "clocks":"5", "bus":"r", "flags":"-------"},
		// {"mnem":["ORA (","p","),Y"], "code":"11pp", "clocks":"5", "bus":"r", "flags":"-------"},
		
		List<String> lines = Files.readAllLines(p);
		for(String line : lines) {
			
			int i = line.indexOf("\"mnem\":");
			if(i<0) {
				i = line.indexOf("\"post\":");
			}
			if(i<0) {			
				System.out.println(line);
				continue;
			}
			i=i+7;
			int j = line.indexOf("\"",i+1)+1;
			
			String s = line.substring(i+1,j-1);			
			//System.out.println(line.substring(i,j));
			
			List<String> frags = new ArrayList<String>();
			String curFrag="";
			int pos = 0;
			while(pos<s.length()) {
				char ch = s.charAt(pos++);
				if(ch>='a' && ch<='z') {
					frags.add(curFrag);
					curFrag = "";
					frags.add(""+ch);
				} else {
					curFrag = curFrag + ch;
				}
			}
			if(curFrag.length()>0) {
				frags.add(curFrag);
			}
			String rep = "[";
			for(String frag : frags) {
				rep=rep+"\""+frag+"\",";
			}
			rep = rep.substring(0,rep.length()-1)+"]";
			System.out.println(line.substring(0,i)+rep+line.substring(j));
			
		}
		
	}

}
