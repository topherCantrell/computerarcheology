package cleans;

import java.io.PrintWriter;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import code.AddressAccess;
import code.AddressDef;
import code.AddressTable;
import code.CU;
import code.CodeFile;
import code.CodeLine;

public class LinkFix {
	
	List<Integer> notFounds;
	
	public void fix(CodeFile tabs) {
		
		notFounds = new ArrayList<Integer>();
		
		for(CodeLine c : tabs.code) {			
			if(c.comment!=null && c.comment.contains("{{")) {
				// Don't change any "fixed" references
				continue;
			}			
			if(c.opcode==null) {
				// Not an opcode ... nothing to reference
				continue;
			}
			int i = c.opcode.indexOf("$");
			if(i<0) {
				// No numeric constant ... nothing to reference
				continue;
			}
			
			// Get the complete number
			++i;
			int j = i;
			while(j<c.opcode.length()) {
				int ch = c.opcode.charAt(j);
				if( !((ch>='0' && ch<='9') || (ch>='A' && ch<='F')) ) {
					break;
				}
				++j;
			}
			
			// Check the opcode for read/write/port
			AddressAccess ac = tabs.cpu.getAccess(c.opcode, i-1, CU.parseInt(c.opcode.substring(i,j),16) );
			if(ac==null) {
				continue;
			}
			
			// Remove any existing {...} entry
			i = c.comment.indexOf("{");
			if(i>=0) {
				j = c.comment.indexOf("}",i);
				String exist = c.comment.substring(i,j+1);
				i = c.originalText.indexOf(exist);
				String a = c.originalText.substring(0,i)+c.originalText.substring(i+exist.length());
				c.originalText = a;
			}
			
			// TODO			
			// If there is no comment then make a blank one.					
			
			AddressTable table = tabs.getAddressTable(ac.address);
			String tnam = "";
			if(!ac.isCode && table!=null) {
				tnam = table.name;
			}
			
			i = c.originalText.indexOf(";");
			c.originalText = c.originalText.substring(0,i+1)+"{"+tnam+"}"+c.originalText.substring(i+1);
			
			if(table!=null) {
				AddressDef en = table.getEntry(ac.address, ac.bus);	
				if(en == null) {
					if(!notFounds.contains(ac.address)) {
						notFounds.add(ac.address);
					}
				}
			}						
			
		}
		
	}
	
	public static void main(String [] args) throws Exception {
		
		LinkFix fixer = new LinkFix();
		
		Path p = Paths.get("content/NES/Zelda/Bank0.cmark");
		
		CodeFile tabs = new CodeFile(p);
		
		fixer.fix(tabs);		
		
		if(fixer.notFounds.size()>0) {		
			System.out.println("The following definitions were not found in the address tables:");
			Collections.sort(fixer.notFounds);
			for(int ii : fixer.notFounds) {
				System.out.println("|| "+CU.hex4(ii)+" || "+CU.hex4(ii)+" ||");
			}
		}
		
		PrintWriter pw = new PrintWriter("New.cmark");
		for(CodeLine c : tabs.code){
			pw.println(c.originalText);
		}
		
		pw.flush();
		pw.close();
		
	}

}
