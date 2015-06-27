package web;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import cleans.LinkFix;
import code.CodeFile;
import code.CodeLine;

public class CodeToHTML extends MarkupToHTML {
	
	public void translate(String contentRoot, String inFile, String outFile, 
			String breadCrumbs, String siteNav, String nav) throws IOException 
	{
		
		System.out.println("CHERE "+inFile);
		
		// Load the code file (and all its address tables)
		Path ip = Paths.get(inFile);
		CodeFile code = new CodeFile(ip);
		
		// Fix up the inter-HTML links
		LinkFix fixer = new LinkFix();
		fixer.fix(code, false);			
		
		// TODO
		
		// Markups and code linking
		
		// c.comment.flag != null if we need to insert a raw-address span
		// c.label != null if we need to insert a label span
		// c.comment.startsWith(";{") if we need to insert an anchor
		
		for(CodeLine c : code.code) {
			
			/*
			if(c.comment!=null && c.comment.startsWith(";{")) {
				System.out.println(c.originalText+":"+c.comment);
			}
			*/
			
			/*
			if(c.flag !=null) {
				System.out.println(c.originalText);				
			}
			*/
		}
		
		//System.exit(0);
		
	}

}
