package web;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class CodeToHTML extends MarkupToHTML {
	
	public void translate(String contentRoot, String inFile, String outFile, 
			String breadCrumbs, String siteNav, String nav) throws IOException 
	{
		
		Path ip = Paths.get(inFile);
		List<String> lines = Files.readAllLines(ip);
		
		System.out.println("CHERE");
		
	}

}
