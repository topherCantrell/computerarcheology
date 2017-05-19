package cleans;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class DVMerge {

	static String findUpdate(String org, List<String> update) {
		String a = org.substring(0,5);
		for(String b : update) {
			if(b.startsWith(a)) return b;
		}
		return null;
		
	}
	
	
	public static void main(String[] args) throws Exception {
		List<String> original = Files.readAllLines(Paths.get("content/arcade/asteroids/VectorROM.cmark"));
		List<String> update = Files.readAllLines(Paths.get("content/arcade/asteroids/rerun.txt"));
		
		for(String org : original) {
			if(org.contains("SVEC") && org.contains("y=")) {
				String u = findUpdate(org,update);
				int i = org.indexOf("y=");
				int j = u.indexOf("y=");	
				
				String n = org.substring(0,i)+u.substring(j,j+5)+org.substring(i+5);
								
				System.out.println(n);				
			} else {
				System.out.println(org);
			}
		}

	}

}
