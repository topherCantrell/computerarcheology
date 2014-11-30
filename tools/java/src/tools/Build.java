package tools;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.Reader;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;

/**
 * This tool runs through an assembly file and executes all build commands embedded
 * in the comments line "; @build .....". 
 */
public class Build 
{
	
	public static void main(String [] args) throws Exception
	{		
		
		Reader fr = new FileReader(args[0]);
		BufferedReader br = new BufferedReader(fr);
		
		List<String> commands = new ArrayList<String>();
		
		while(true) {
			String g = br.readLine();
			if(g==null) break;
			if(g.startsWith(";")) {
				g = g.substring(1).trim();
				if(g.startsWith("@build")) {
					g = g.substring(7).trim();
					commands.add(g);
				}
			}			
		}
		
		br.close();
		
		for(String s : commands) {
			System.out.println("Running "+s);
			runCommand(s);
		}
		
	}
	
	public static void runCommand(String command) throws Exception
	{
		String [] args = command.split(" ");
		if(args[0].toUpperCase().equals("PAUSE")) {
			Thread.sleep(Integer.parseInt(args[1]));
			return;
		}
		Class<?> c = Build.class.getClassLoader().loadClass(args[0]);
		String [] r = new String[args.length-1];
		Method m = c.getMethod("main", r.getClass());
		for(int x=1;x<args.length;++x) {
			r[x-1] = args[x];
		}
		Object [] params = {r};
		m.invoke(null, params);				
		
	}

}
