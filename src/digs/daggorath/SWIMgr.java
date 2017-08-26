package digs.daggorath;

import java.io.IOException;
import java.io.PrintStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class SWIMgr {
	
	List<String> lines;
	
	List<String> functionNames;
	
	public SWIMgr() throws IOException {
		functionNames = new ArrayList<String>();
		lines = Files.readAllLines(Paths.get("content/CoCo/Daggorath/Code.mark"));
		int pos = 0;
		while(!lines.get(pos++).startsWith("||= SWI ||"));
		for(int x=0;x<29;++x) {
			String [] ss = lines.get(pos++).split("\\|\\|");
			functionNames.add(ss[3].trim());
		}
								
	}

	public static void main(String[] args) throws Exception {
		
		SWIMgr mgr = new SWIMgr();
		
		PrintStream ps = new PrintStream("dag.out");
		for(int ind=0;ind<mgr.lines.size();++ind) {
			
			String s = mgr.lines.get(ind);
			
			if(s.startsWith("SWI_")) {
				int i = s.indexOf(":");
				int sn = Integer.parseInt(s.substring(4,i),16);
				mgr.lines.set(ind+1, "; "+mgr.functionNames.get(sn));				
			}
			
			int i = s.indexOf("SWI_");
			if(i>0) {
				if(s.charAt(i+5)==':' || s.charAt(i+6)==':') {
					int k = s.indexOf('_',i);
					i = s.indexOf(':',i);
					int j = s.indexOf(':',i+1);		
					int sn = Integer.parseInt(s.substring(k+1,i),16);
					String n = mgr.functionNames.get(sn);
					String d = "#addr_SWI_"+Integer.toString(sn,16).toUpperCase();
					ps.println(s.substring(0, i)+ ":["+n+"]("+d+"):"+s.substring(j+1));
					continue;
				}
			}
			ps.println(s);			
		}
		
		ps.flush();
		ps.close();
		
		// At the SWI_x: labels ... put the name
		
	}

}
