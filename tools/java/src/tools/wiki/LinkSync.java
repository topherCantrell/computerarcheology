package tools.wiki;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import tools.code.CU;
import tools.code.CodeLine;
import tools.file.LinesFromFile;

public class LinkSync {
	
	/**
	 * This function finds all target labels in the code. Target labels are in the comment
	 * and are of the form {*blah} or {*}. If no name "blah" is given then the code uses
	 * any label on the line of code instead. The code assigns an address to the label.
	 * If the line of code has no address (as in a pure label) then the code finds the
	 * next addressed line of code.
	 * @param code the lines of code
	 * @return a list of CodeTarget
	 */
	static List<CodeTarget> findTargets(List<CodeLine> code) {
		List<CodeTarget> ret = new ArrayList<CodeTarget>();
		
		for(int x=0;x<code.size();++x) {
			CodeLine c = code.get(x);
			String com = c.getComment();
			if(com==null) continue;
			
			int i = com.indexOf("{*");
			if(i>=0) {
				int j = com.indexOf("}");
				if(j<0) {
					System.out.println("Ignoring badly formed {} in:"+c.getOriginalText());
					continue;
				}
				CodeTarget ct = new CodeTarget();
				ct.codeLine = c;
				ct.name = com.substring(i+2, j).trim();
				if(ct.name.length()==0 && !c.getLabels().isEmpty()) {
					ct.name = c.getLabels().get(0);
				}
				i = x;
				while(code.get(i).getAddress()<0 && i<code.size()-1) {
					++i;
				}
				ct.address = code.get(i).getAddress();
				
				ret.add(ct);
				
			}
			
		}
		
		return ret;
	}
	
	/**
	 * This function finds all the menu references at the top of the code file. All menu items are
	 * assumed to come before the first line with "{{{" in it. Menu items are assumed to be of the
	 * form [#link display] or [#link] where "link" is the name of a target and "display" is the
	 * text to display.
	 * @param code
	 * @return
	 */
	static List<CodeRef> getMenuReferences(List<CodeLine> code) {
		List<CodeRef> ret = new ArrayList<CodeRef>();
		
		for(CodeLine c : code) {
			if(c.getOriginalText().contains("{{{")) {
				return ret;
			}
			
			String g = c.getOriginalText();
			
			while(true) {
				int i = g.indexOf("[#");
				if(i<0) break;
				int j = g.indexOf("]");
				if(j<0) {
					System.out.println("Ignoring malformed [# ] in: "+c.getOriginalText());
					break;
				}
				String a = g.substring(i+2, j);				
				g = g.substring(j+1);
				int k = a.indexOf(" ");
				CodeRef cr = new CodeRef();
				if(k>=0) {
					cr.name = a.substring(0, k);
					cr.display = a.substring(k).trim();
				} else {
					cr.name = a;
				}
				ret.add(cr);
			}
			
		}
		
		return ret;
	}
	
	/**
	 * This function parses a RAMUsage file for memory targets. The targets are defined in a single wiki table 
	 * of the form ||address||name||description||. The "address" can have "_" in it (they are ignored). The
	 * "address" can be of the form "address:size" where "size" is the number of bytes (assumed to be 1 if
	 * not given).
	 * @param filename name of the RAMUsage file
	 * @param tableName name of the wiki table within the file
	 * @param type the type of memory target for this table
	 * @param grow an optional list to add to (null to create one)
	 * @return the list of MemoryTarget the new list or the "grow"
	 * @throws IOException if something goes wrong
	 */
	static List<MemoryTarget> getMemoryTargets(String filename, String tableName, MemoryTargetType type, List<MemoryTarget> grow) throws IOException {
		
		// TODO allow a "type" to be assigned to all targets (like RAM, Port)
		// TODO allow a list to be passed in to grow
		
		if(grow == null) {
			grow = new ArrayList<MemoryTarget>();
		}
				
		BufferedReader br = new BufferedReader(new FileReader(filename));
		String g;
		while(true) {
			g = br.readLine();
			if(g==null) {
				System.out.println("No table named '"+tableName+"' found in '"+filename+"'");
				br.close();
				return grow;
			}
			if(g.equals("= "+tableName+" =")) break;
		}
		
		while(true) {
			g = br.readLine();
			if(g==null) {
				System.out.println("Table '"+tableName+"' is empty");
				br.close();
				return grow;
			}
			if(g.startsWith("||")) break;
		}
		
		while(true) {
			if(!g.startsWith("||=")) {
				// ||2_04||??204||Initialized to FF||
				MemoryTarget mr = new MemoryTarget();
				int i = -1;
				int j = -1;
				int k = -2;
				i = g.indexOf("||",2);
				if(i>=0) {
					j = g.indexOf("||",i+2);
					if(j>=0) {
						k = g.indexOf("||",j+2);
					}
				}
				if(i<0 || j<0 || k<0) {
					System.out.println("Malformed table entry: "+g);
					br.close();
					return grow;
				}
				String a = g.substring(2, i).trim();
				a = CU.replaceAll(a, "_", "");
				int x = a.indexOf(":");
				if(x>=0) {
					mr.size = Integer.parseInt(a.substring(x+1));
					a = a.substring(0,x);
				} else {
					mr.size = 1;
				}
				mr.address = Integer.parseInt(a,16);
				mr.name = g.substring(i+2,j).trim();
				mr.description = g.substring(j+2,k).trim();
				mr.type = type;
				grow.add(mr);
			}
			g = br.readLine();
			if(g==null) {
				br.close();
				return grow;
			}
			if(!g.startsWith("||")) {
				br.close();
				return grow;
			}
		}
				
	}
	
	
	public static void main(String [] args) throws Exception {
		
		LinesFromFile lines = new LinesFromFile("d:\\workspace\\daggorath\\daggorath.txt");
		List<CodeLine> code = lines.listToCode(lines.getLines());
		
		List<CodeTarget> targets = findTargets(code);
		List<CodeRef> refs = getMenuReferences(code);		
		List<MemoryTarget> memTargets = getMemoryTargets("d:\\workspace\\daggorath\\ram.txt","DP=2 Game Variables",MemoryTargetType.RAM,null);
		
		// TODO if we attempt to line up menu items with code targets then we'll miss wiki section references
		// An easy way is to just report on them with a comment saying "These might be wiki references"
		
		for(MemoryTarget t : memTargets) {
			System.out.println(":"+t.address+":"+t.name+":"+t.description+":");
		}
		
		/*
		for(CodeRef r : refs) {
			System.out.println(":"+r.name+":"+r.display+":"); 
		}
		*/
		
		/*
		for(CodeTarget target : targets) {
			System.out.println(target.name+" "+target.address);
		}
		*/
		
		// TODO Report all targets+nextLineDescription in wiki table format for menu table		
		// TODO find all RAM references in the code and add/edit a {-} entry to the line if there isn't one
		// TODO a {!} means "do nothing"
		// TODO find all code references and add/edit a {} entry to the line if there isn't one		
		// TODO add "$$$$" to modified lines. That allows easy search and one search/replace to remove
		
		// Two outputs: a modified input source file and a "report" file to stdio
		// Things like "changing 'CopyXY' references 'CopyYtoX'"
		
	}	

}
