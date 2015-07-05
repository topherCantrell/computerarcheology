package cleans;

import java.io.PrintWriter;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

import web.SiteInfo;
import web.SiteInfoEntry;
import code.CodeFile;
import code.CodeLine;

public class Direct {
	
	public static void main(String [] args) throws Exception {
		
		SiteInfo si = new SiteInfo();	
		processRecurse(si.root.entries, "content/");
		
	}
	
	static void processRecurse(List<SiteInfoEntry> entries, String contentPath) throws Exception {
		for(SiteInfoEntry entry : entries) {
			if(entry.command.equals("code")) {
				System.out.println(contentPath+entry.arg);
				fix(contentPath+entry.arg);
			}
			if(entry.command.equals("dir")) {
				processRecurse(entry.entries,contentPath+entry.arg+"/");
			}
		}		
		
	}
	
	public static void fix(String filename) throws Exception {
		
		Path p = Paths.get(filename);				
		
		// Load the code and tables
		CodeFile tabs = new CodeFile(p);
		
		for(CodeLine c : tabs.code) {
			if(c.opcode==null) {
				continue;
			}			
			
			int i = c.opcode.indexOf(">");
			if(i>=0) {
				i = i + c.opcodePos;
				String a = c.originalText.substring(0,i)+"<"+c.originalText.substring(i+1);
				c.originalText = a;				
			}
			
		}	
		
		// Replace the contents of the file
		PrintWriter pw = new PrintWriter(p.toString());
		for(CodeLine c : tabs.code){
			pw.println(c.originalText);			
		}		
		pw.flush();
		pw.close();
		
	}

}
