package cleans;


import java.io.PrintStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class ColumnSpacing {

	public static void main(String[] args) throws Exception {
		
		List<String> lines = Files.readAllLines(Paths.get("content/arcade/defender/BankFIxed.mark"));
		
		PrintStream ps = new PrintStream("out.txt");
		
		
		for(String line : lines) {
			
			if(line.length()>5 && line.charAt(4)==':') {
				int i = line.indexOf(";");
				if(i<0) {
					ps.println(line);
				} else {
					String a = line.substring(0, i);
					String b = line.substring(i);
					while(a.length()<45) {
						a = a + " ";
					}
					ps.println(a+b);
				}
			} else {
				ps.println(line);
			}
			
		}
		
		ps.flush();
		ps.close();
		
	}

}
