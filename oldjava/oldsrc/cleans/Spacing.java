package cleans;

import java.io.PrintWriter;
import java.nio.file.Path;
import java.nio.file.Paths;

import code.CodeFile;
import code.CodeLine;

public class Spacing {
	
	public static void main(String [] args) throws Exception {
		
		Path p = Paths.get("content/Arcade/Asteroids/Code.cmark");
				
		int [] spacing = {20,6,20};
		
		// Load the code and tables
		CodeFile tabs = new CodeFile(p);
		
		for(CodeLine c : tabs.code) {
			if(c.opcode==null) {
				continue;
			}
			String aa = c.originalText.substring(0,c.opcodePos).trim();
			String bb = c.opcode;
			String cc = "";
			int i = bb.indexOf(" ");
			if(i>=0) {
				cc = bb.substring(i).trim();
				bb = bb.substring(0,i).trim();
			}
			String dd = null;
			if(c.comment!=null) {
				dd = c.originalText.substring(c.commentPos);
			}
			
			
			while(aa.length()<spacing[0]) aa=aa+" ";
			while(bb.length()<spacing[1]) bb=bb+" ";
			while(cc.length()<spacing[2]) cc=cc+" ";
			
			aa = aa+bb+cc;
			if(dd!=null) {
				aa = aa + dd;
			}
						
			c.originalText = aa;
			
		}	
		
		/*
		for(CodeLine c : tabs.code){
			System.out.println(c.originalText);
		}
		*/		
				
		// Replace the contents of the file
		PrintWriter pw = new PrintWriter(p.toString());
		for(CodeLine c : tabs.code){
			pw.println(c.originalText);			
		}		
		pw.flush();
		pw.close();		
		
	}

}
