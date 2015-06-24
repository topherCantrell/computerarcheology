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

/**
 * This class (and tool) manages the "{...}" link specifications in the code comments.
 * The "{{...}}" specifications are fixed and are left alone.
 * The others specifications are blindly replaced in the comments.
 * The code also reports on addresses that are accessed but not found in an
 * address table file.
 */
public class LinkFix {
	
	List<Integer> notFounds;
	
	/**
	 * Fix up all the links in all comments in the code.
	 * @param tabs the code and address tables
	 */
	public void fix(CodeFile tabs) {
		
		notFounds = new ArrayList<Integer>();
		
		int commentPos = 0;
		
		for(CodeLine c : tabs.code) {	
			
			// Keep up with where these are in case we have to make one
			if(c.commentPos>=0) {
				commentPos = c.commentPos;
			}
			
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
			
			if(tabs.cpu==null) {
				throw new RuntimeException(";;%%cpu must be valid");
			}
			
			// Check the opcode for read/write/port
			AddressAccess ac = tabs.cpu.getAccess(c.opcode, i-1, CU.parseInt(c.opcode.substring(i,j),16) );
			if(ac==null) {
				continue;
			}			
					
			// If there is no comment then make a blank one.			
			if(c.comment==null) {
				while(c.originalText.length()<commentPos) {
					c.originalText = c.originalText + " ";
				}
				c.originalText = c.originalText+";";
				c.comment = "";
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
			
			// Find the table (if any) that goes with this address
			AddressTable table = tabs.getAddressTable(ac.address);
			
			// Get the name (like "-") to go in the specification. Code references are
			// left blank.
			String tnam = "";
			if(!ac.isCode && table!=null) {
				tnam = table.name;
			}
			
			// Add the specification to the code line
			i = c.originalText.indexOf(";");
			c.originalText = c.originalText.substring(0,i+1)+"{"+tnam+"}"+c.originalText.substring(i+1);
			
			// Lookup the actual entry in the table. Collect the address for reporting if it 
			// is not in the table.
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
	
	/**
	 * This tool fixes the links in the target file IN PLACE overwriting the
	 * existing file. Be sure to check-in to GIT before running this tool so
	 * you have a way to back out the changes.
	 * @param args
	 * @throws Exception
	 */
	public static void main(String [] args) throws Exception {
		
		Path p = Paths.get("content/NES/Zelda/Bank7.cmark");
		
		// The worker object
		LinkFix fixer = new LinkFix();		
		
		// Load the code and tables
		CodeFile tabs = new CodeFile(p);
		
		// Do the fix up
		fixer.fix(tabs);		
		
		// Report on missing entries in the tables
		if(fixer.notFounds.size()>0) {		
			System.out.println("The following definitions were not found in the address tables:");
			Collections.sort(fixer.notFounds);
			for(int ii : fixer.notFounds) {
				System.out.println("|| "+CU.hex4(ii)+" || "+CU.hex4(ii)+" || ||");
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
