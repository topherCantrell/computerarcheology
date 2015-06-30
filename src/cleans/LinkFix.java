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
import cpu.CPU;

/**
 * This class (and tool) manages the "{...}" link specifications in the code comments.
 * The "{{...}}" specifications are fixed and are left alone.
 * The others specifications are blindly replaced in the comments.
 * The code also reports on addresses that are accessed but not found in an
 * address table file.
 * 
 * There are two versions of link specifications. The "long" version contains everything.
 * The "short" version is easier to see when looking at a raw disassembly. The "{{...}}"
 * must be the full "long" specification.
 * 
 * {link:label}
 * {/CoCo/Hardware.html#F00D:diskCntrl}
 * 
 * Short version: {-2diskCntrl}
 * 
 * Note that the short version is never used as an input. It is purely for the human to
 * read while disassembling. The web builder always erases the full "{...}" and rebuilds 
 * it to the current long specification.
 */
public class LinkFix {
	
	List<AddressAccess> notFounds;
	
	/**
	 * Fix up all the links in all comments in the code.
	 * @param tabs the code and address tables
	 */
	public void fix(CodeFile tabs, boolean shortVersion) {
				
		notFounds = new ArrayList<AddressAccess>();
		
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
						
			if(c.comment!=null) {
				int i = c.comment.indexOf("{");
				if(i>=0) {
					int j = c.comment.indexOf("}",i);
					if(j<0) {
						throw new RuntimeException("Bad Specification '"+c.originalText+"'");
					}
					String exist = c.comment.substring(i,j+1);
					i = c.originalText.indexOf(exist);
					String a = c.originalText.substring(0,i)+c.originalText.substring(i+exist.length());
					c.originalText = a;					
				}
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
				if( !((ch>='0' && ch<='9') || (ch>='A' && ch<='F') || ch=='-') ) {
					break;
				}
				++j;
			}
			
			c.numericConstantStart = i;
			c.numericConstantEnd = j;
			
			if(tabs.cpu==null) {
				//throw new RuntimeException(";;%%cpu must be valid");
				tabs.cpu = CPU.getCPU("None");
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
			
			// Find the table (if any) that goes with this address
			AddressTable table = tabs.getAddressTable(ac.address);			
			
			// Add the specification to the code line
			i = c.originalText.indexOf(";");
			String tnam = null;
			if(shortVersion) {
				tnam = getShortVersion(table,ac,c, tabs);
			} else {
				tnam = getLongVersion(table,ac,c, tabs);
			}
			if(tnam!=null) {
				c.originalText = c.originalText.substring(0,i+1)+tnam+c.originalText.substring(i+1);
			}								
			
		}
		
	}
	
	private String getShortVersion(AddressTable table, AddressAccess ac, CodeLine c, CodeFile code) {
		// {E277}      - Code (address not labeled)
		// {printVar}  - Code (address has label)
		// {-curPtr}   - Table (table has name)
		// {-60}       - Table (table has no name)
		
		if(ac.isCode){
			String target = code.getCodeLabel(ac.address);
			if(target!=null && target.charAt(0)!='$') {
				return "{"+target+"}";
			} 
			return null;			
		} else {
			if(table==null) {
				if(!notFounds.contains(ac)) {
					notFounds.add(ac);
				}
				return null;
			}
			AddressDef en = table.getEntry(ac.address, ac.bus, ac.accessType);	
			if(en == null) {
				if(!notFounds.contains(ac)) {
					notFounds.add(ac);
				}
				return null;
			}
			if(en.name==null || en.name.length()==0) {
				return null;
			}
			return "{"+table.shortName+en.name+"}";
		}
			
	}
	
	private String getLongVersion(AddressTable table, AddressAccess ac, CodeLine c, CodeFile code) {		
		// {#E277:E277:0}            - Code (address not labeled)
		// {#printVar:printVar:0}    - Code (address has label)
		// {RAMUse.html#60:curPtr:1} - Table (table has name)
		// {RAMUse.html#60:60:1}     - Table (table has no name)
		
		if(ac.isCode) {
			String target = code.getCodeLabel(ac.address);
			if(target!=null) {
				return "{#"+target+":"+target+":0}";
			} 
			return null;			
		} else {
			if(table==null) {
				if(!notFounds.contains(ac)) {
					notFounds.add(ac);
				}
				return null;
			}
			AddressDef en = table.getEntry(ac.address, ac.bus, ac.accessType);	
			if(en == null) {
				if(!notFounds.contains(ac)) {
					notFounds.add(ac);
				}
				return null;
			}
			if(en.name==null || en.name.length()==0) {
				return null;
			}
			return "{"+table.htmlRef+"#"+CU.hex4(ac.address)+":"+en.name+":"+table.index+"}";
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
		
		Path p = Paths.get("content/Arcade/TimePilot/SoundCode.cmark");
		
		// The worker object
		LinkFix fixer = new LinkFix();		
		
		// Load the code and tables
		CodeFile tabs = new CodeFile(p);
		
		// Do the fix up
		fixer.fix(tabs,true);		
		
		// Report on missing entries in the tables
		if(fixer.notFounds.size()>0) {		
			System.out.println("The following definitions were not found in the address tables:");
			Collections.sort(fixer.notFounds);
			for(AddressAccess ii : fixer.notFounds) {
				System.out.println(ii);
				//System.out.println("|| "+CU.hex4(ii)+" || "+CU.hex4(ii)+" || ||");
			}
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
