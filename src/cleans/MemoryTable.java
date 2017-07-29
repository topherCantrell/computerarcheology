package cleans;

import java.io.PrintStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

import util.CU;

public class MemoryTable {
	
	public static void main(String [] args) throws Exception {
		List<String> lines = Files.readAllLines(Paths.get("in.txt"));
		
		boolean changed = true;
		while(changed) {
			changed = false;
			for(int x=0;x<lines.size()-1;++x) {
				String a = lines.get(x);
				String b = lines.get(x+1);
				int aa = Integer.parseInt(a.substring(2,8).trim(),16);
				int bb = Integer.parseInt(b.substring(2,8).trim(),16);
				if(bb<aa) {
					lines.set(x, b);
					lines.set(x+1, a);
					changed = true;
				}
			}
		}
		
		PrintStream ps = new PrintStream("out.txt");
		for(String s : lines) {
			ps.println(s);
		}
		ps.flush();
		ps.close();
		
	}

	public static void main2(String[] args) throws Exception {
		
		List<String> lines = Files.readAllLines(Paths.get("content/CoCo/Daggorath/RAMUse.mark"));
		
		PrintStream ps = new PrintStream("out.txt");
		
		boolean inMemoryBlock = false;
		
		for(String s : lines) {
			if(s.startsWith("{{{memory")) inMemoryBlock = true;
			if(s.startsWith("}}}")) inMemoryBlock = false;
			
			if(inMemoryBlock && s.startsWith("||") && !s.startsWith("||=")) {
				int i = s.indexOf("||",2);
				int k = s.indexOf("||",i+2);
				
				String addr = s.substring(2,i).trim();
				String name = s.substring(i+2,k).trim();
				
				if(name.isEmpty()) {
					name = "m"+addr;
					i = name.indexOf(":");
					if(i>0) name = name.substring(0, i).trim();
				}
				
				addr = CU.padTo(addr, 9);
				name = CU.padTo(name, 20);
				
				ps.println("|| "+addr+" || "+name+" "+s.substring(k));
				
			} else {			
				ps.println(s);
			}
			
		}		
		
		
		ps.flush();
		ps.close();
		

	}

}
