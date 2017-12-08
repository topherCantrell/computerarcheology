package digs.atari2600;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Atari2600RamReport {
	
	public static void main(String [] args) throws Exception
	{
		
		Map<Integer,List<Integer>> access = new HashMap<Integer,List<Integer>>();
		
		FileReader fr = new FileReader("c:\\projects\\computerarcheology\\combat\\combat.txt");
		BufferedReader br = new BufferedReader(fr);
		
		while(true) {
			String g = br.readLine();
			if(g==null) break;
			
			int i = g.indexOf(";");
			if(i>=0) {
				g = g.substring(0,i);
			}
			g = g.trim();
			
			if(g.length()<27) continue;
			if(g.charAt(26)!='$') continue;
			if(g.length()>29) continue;
			
			int address = Integer.parseInt(g.substring(0,4),16);
			int value = Integer.parseInt(g.substring(27,29),16);
			
			List<Integer> ac = access.get(value);
			if(ac==null) {
				ac = new ArrayList<Integer>();
				access.put(value, ac);
			}
			
			if(!ac.contains(address)) ac.add(address);
									
		}
		
		br.close();
		
		
		fr = new FileReader("c:\\projects\\computerarcheology\\combat\\combatrun.log");
		br = new BufferedReader(fr);
		while(true) {
			String g = br.readLine();
			if(g==null) break;
			int i = g.indexOf("=");
			if(i<0) continue;
			
			String a = g.substring(i+1).trim();
			if(a.length()!=2) continue;			
						
			int value = Integer.parseInt(a,16);
			
			i = g.indexOf(":");
			int address = Integer.parseInt(g.substring(i-4,i),16);
			
			List<Integer> ac = access.get(value);
			if(ac==null) {
				ac = new ArrayList<Integer>();
				access.put(value, ac);
			}
			
			if(!ac.contains(address)) {
				ac.add(address);
				//System.out.println(Integer.toString(value,16)+":"+Integer.toString(address,16));
			}
			
		}
		
		br.close();
		
		
		List<Integer> keys = new ArrayList<Integer>();
		for(Integer i : access.keySet()) {
			keys.add(i);
		}
		Collections.sort(keys);
		
		for(int k : keys) {
			List<Integer> acs = access.get(k);
			Collections.sort(acs);
			String ra = Integer.toString(k,16).toUpperCase();
			String a = ";##+1280:0080:00FF:00"+ra+"  ??"+ra+"                ";			
			for(int x : acs) {
				a = a + Integer.toString(x,16).toUpperCase()+",";
			}
			a = a.substring(0,a.length()-1);
			System.out.println(a);
		}
		
	}

}
