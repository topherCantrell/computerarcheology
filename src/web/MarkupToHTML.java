package web;

import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import bus.AddressAccess;
import bus.BusType;
import code.CodeLine;
import cpu.CPU;
import cpu.Opcode;
import util.CU;

// TODO
// - Forms like "$300,X" are not refs by default but comment "; {}" makes them
// - Must use the opcode info to decide if DP applies -- and then add it to the number to get the label (we aren't doing that now)

public class MarkupToHTML {
		
	enum BlockType {
		NONE,    // No block at all
		PRE,     // This block is a <pre> wrapper
		PLAYME,  // This is a "PlayMe" styled block
		TOUR,    // This is a "TourGuide" styled block
		HTML,    // Pure HTML
		CODE,    // Lines of code
		MEMORY,  // A memory-map table
		//SNIPPET // Lines of code from another file (don't chase the fill-ins)
	}
	
	static class ExternalMemoryMap {
		String name;
		String markupFile;
		String htmlFile;
		AddressMap map;
	}
	
	// For code that references external memory map tables
	List<ExternalMemoryMap> memoryMaps = new ArrayList<ExternalMemoryMap>();
	Map<Integer,LineOfMarkup> labelValues = new HashMap<Integer,LineOfMarkup>();
	
	List<LineOfMarkup> lines;     // The list of markup lines. We'll add to these as we go.
	int pos;                      // Our current position within the lines as we process them.
	
	Map<String,String> variables; // Any %% variables in the markup
	PageNavInfo rootPageNav;      // The navigation tree for the page
	List<String> ids;             // Unique IDs on the page
	String contentRoot;           // Where the content begins
	PageNavInfo navCursor;        // For moving up and down the navigation tree as we build it	
	
	BlockType blockType = BlockType.NONE; // The kind of block we are currently in (if any)
	
	/**
	 * Expand all include directives
	 * @param lines the current list of lines
	 * @param inFile the name of the input file
	 * @throws IOException file errors
	 */
	void expandIncludes(List<LineOfMarkup> lines,String inFile) throws IOException {
		for(int x=lines.size()-1;x>=0;--x) {
			String s = lines.get(x).line.trim();
			if(s.startsWith("%%include ")) {
				int i = inFile.lastIndexOf("/");
				List<String> inc = Files.readAllLines(Paths.get(inFile.substring(0,i+1)+s.substring(10).trim()));
				lines.remove(x);
				lines.addAll(x,LineOfMarkup.convert(inc, "INCLUDED FROM '"+s.substring(10).trim()));				
			}
		}
	}
	
	/**
	 * A line that begins with ";" is a code line.
	 * A line of the form "1234:" is a code line.
	 * A blank line is code if the next line is code (a recursive check).
	 * A line that starts with "Label:" is a label (a code line) if the next line is code (a recursive check). 
	 * @param pos the current position within the list of lines
	 * @return true if this is code
	 */	 
	boolean isCodeLine(int pos) {
		if(pos>=lines.size()) return false;
		if(lines.get(pos).lineNumber<0) return false; // We never insert code;
		String lineTrim = lines.get(pos).line.trim();
		if(lineTrim.startsWith(";")) return true; // Code comment is code
		if(lineTrim.length()>4 && CU.isNumeric(lineTrim.substring(0, 4), 16)  && lineTrim.charAt(4)==':') {
			return true;
		}
		if(lineTrim.isEmpty()) {				
			// Blank line could be code if next line is
			// DANGEROUS RECURSION HERE			
			boolean is = isCodeLine(pos+1);
			return is;
		}
		// It could be a label
		int i = lineTrim.indexOf(":");
		if(i<0) return false; // Must have a colon
		int j = lineTrim.indexOf(" ");
		if(j>=0 && j<i) return false; // No spaces in labels		
		// It is only a label if the next line is code
		// DANGEROUS RECURSION HERE
		boolean is = isCodeLine(pos+1);
		return is;
	}
	
	/**
	 * We keep a list of unique IDs on the page. This method ensures the
	 * id is unique by modifying it until it is. 
	 * @param org the original (requested) id
	 * @return the actual (maybe modified) id
	 */
	String addID(String org) {
		if(!ids.contains(org)) {
			ids.add(org);
			return org;
		}		
		int un = 2;
		while(ids.contains(org+un)) {
			++un;
		}
		ids.add(org+un);
		return org+un;		
	}
	
	/**
	 * Parse the set-variable line from the markup.
	 * @param com the markup text
	 */
	void setVariable() {
		LineOfMarkup mark = lines.get(pos);
		String com = mark.lineTrim;		
		
		int i = com.indexOf("=");
		if(i<0) {
			throw new MarkupException("Expected '=' in '"+com+"'");
		}
		String key = com.substring(2,i).trim();
		String value = com.substring(i+1).trim();
		if(key.startsWith("-")) {			
			ExternalMemoryMap ne = new ExternalMemoryMap();
			ne.name = key;
			i = value.indexOf(" ");
			ne.markupFile = value.substring(0, i).trim();
			ne.htmlFile = value.substring(i+1).trim();		
			List<String> mapEntries;
			try {
				mapEntries = Files.readAllLines(Paths.get(contentRoot,ne.markupFile));
			} catch(IOException e) {
				throw new MarkupException("Could not load address table "+ne.markupFile);
			}
			ne.map = new AddressMap();
			ne.map.parseMaps(mapEntries);
			memoryMaps.add(ne);
		} else {
			variables.put(key,value );
		}		
		mark.newLine = null;
	}
	
	/**
	 * Parse all markdown links in the string and replace with HTML
	 * @param line the markdown line
	 * @return the modified line
	 */
	String fixLinks(String line) {
		while(true) {
			int i = line.indexOf('[');
			if(i<0) return line;
			int j = line.indexOf(']',i);
			if(j<0) return line;
			String text = line.substring(i+1, j);
			String link = text;
			String target = "";
			if(j+1<line.length() && line.charAt(j+1)=='(') {
				int k = line.indexOf(')',j+1);
				if(k<0) return line;
				link = line.substring(j+2,k);
				j = k;
				if(link.endsWith("`")) {
					link = link.substring(0, link.length()-1);
					int m = link.indexOf("`");
					target = " target='"+link.substring(m+1)+"' ";
					link = link.substring(0,m);
				}
			}
			String rep = "<a "+target+"href='"+link+"'>"+text+"</a>";
			//System.out.println(rep);
			line = line.substring(0,i)+rep+line.substring(j+1);
		}		
	}
	
	/**
	 * Parse the header and create a navigation link
	 * @param lineTrim the header line
	 */
	void parseHeader() {
		LineOfMarkup mark = lines.get(pos);
		String lineTrim = mark.lineTrim;
		String style = null;
		
		int i = lineTrim.indexOf('`');
		if(i>0) {
			int j = lineTrim.indexOf('`',i+1);
			style = lineTrim.substring(i+1, j);
			lineTrim = lineTrim.substring(0,i).trim();
		}
				
		int level = 0;		
		while(level<lineTrim.length() && lineTrim.charAt(level)=='#') {
			++level;
		}
		
		PageNavInfo ni = new PageNavInfo();
		ni.text = lineTrim.substring(level).trim();
		ni.link = addID(PageNavInfo.idFromText(ni.text));	
		ni.style = style;
		
		mark.newLine = "<h"+(level+1)+" id='"+ni.link+"'>"+ni.text+"</h"+(level+1)+">\n";
		
		if(navCursor.level == 0) {
			// This is the very first entry
			if(level!=1) {
				throw new MarkupException("First heading must be level 1");
			}
			ni.parent = navCursor;
			ni.level = 1;
			navCursor.subs.add(ni);
			navCursor = ni;
		} else if(navCursor.level == level) {
			// Same level as the cursor
			ni.parent = navCursor.parent;
			ni.level = level;
			navCursor.parent.subs.add(ni);
			navCursor = ni;
		} else if(level>navCursor.level) {
			// Adding a level
			ni.parent = navCursor;
			ni.level = navCursor.level+1;
			navCursor.subs.add(ni);
			navCursor = ni;
		} else {
			// Back up one or more levels
			while(level<navCursor.level) {				
				navCursor = navCursor.parent;
			}
			ni.parent = navCursor.parent;
			ni.level = level;
			navCursor.parent.subs.add(ni);
			navCursor = ni;
		}
				
	}
	
	void parseTable() {
		// For memory blocks add the id
		String style = "";
		if(blockType==BlockType.MEMORY) {
			style = " class='memoryMapTable table table-condensed'";
		}
		LineOfMarkup ne = new LineOfMarkup("<table"+style+">","GENERATED",-1);
		lines.add(pos,ne);
		++pos;
		
		if(lines.get(pos).lineTrim.substring(2).trim().startsWith("=")) {
			String n = "<tr>";
			String [] cells = lines.get(pos).lineTrim.split("\\|\\|");
			for(int x=1;x<cells.length;++x) {
				if(x==1) {
					n = n + "<th>"+cells[x].trim().substring(1).trim()+"</th>";
				} else {
					n = n + "<th>"+cells[x].trim()+"</th>";
				}
			}
			n = n + "</tr>";
			lines.get(pos).newLine = n;
			++pos;
		}
		
		while(true) {
			String lineTrim = lines.get(pos).lineTrim;
			if(!lineTrim.startsWith("||")) {
				ne = new LineOfMarkup("</table>","GENERATED",-1);
				lines.add(pos,ne);
				//++pos;
				return;
			}
			String [] cells = lineTrim.split("\\|\\|");
			String n = "<tr>";
			if(blockType == BlockType.MEMORY) {
				n = "<tr id='addr_"+cells[2].trim()+"'>";
			}			
			for(int x=1;x<cells.length;++x) {
				n = n + "<td>"+cells[x].trim()+"</td>";
			}
			n = n + "</tr>";
			lines.get(pos).newLine = n;
			++pos;
		}				
		
	}
	
	/**
	 * Parse a list of bullets at the current pos line cursor.
	 * Add lines and change line text in place to create a bullet list
	 */
	void parseBullet() {
		// Add multi-levels if ever needed
		LineOfMarkup ne = new LineOfMarkup("<ul>","GENERATED",-1);
		lines.add(pos,ne);
		++pos;	
		while(pos<lines.size()) {
			String lineTrim = lines.get(pos).line.trim();			
			if(!lineTrim.startsWith("*")) break;
			lineTrim = lineTrim.substring(1).trim();
			//System.out.println(">>"+lineTrim+"<<");
			lines.get(pos).newLine = "<li>"+fixHTMLText(lineTrim)+"</li>\n";
			++pos;
		}		
		ne = new LineOfMarkup("</ul>","GENERATED",-1);
		lines.add(pos,ne);
	}
	
	/**
	 * Processes links and entities.
	 * @param line the line to be HTML
	 * @return the modified line
	 */
	String fixHTMLText(String line) {	
		line = CU.replaceAll(line, "&", "&amp;"); // Do this first ... it adds more "&"
		line = CU.replaceAll(line, "<", "&lt;");
		line = CU.replaceAll(line, ">", "&gt;");
		line = CU.replaceAll(line, "[[br]]", "<br>");
		line = CU.replaceAll(line, "[[BR]]", "<br>");
		line = fixLinks(line);		
		return line;
	}
	
	/**
	 * We collected navigation information. Now to combine it all together into an HTML
	 * string.
	 * @param inFile the name of the input file (for error messages)
	 * @param pageNav
	 * @return
	 */
	protected String makePageNav(String inFile, List<PageNavInfo> pageNav) {
		if(pageNav.size()<1) {
			return "";
		}
		
		int tlev = (int) pageNav.get(0).level;
		if(tlev != 1) {
			throw new RuntimeException("File '"+inFile+"' Headers must start at level 1.");
		}
		
		List<PageNavInfo> pret = new ArrayList<PageNavInfo>();
		PageNavInfo p = new PageNavInfo();
		p.level = 0;
		pret.add(p);
		
		makePageNavRecurse(inFile, pret,1,0,pageNav);
		
		List<String> lines = new ArrayList<String>();
		makePageNavHTMLRecurse(pret.get(0).subs, lines);		
				
		return CU.listToString(lines);				
	}	
	private void makePageNavHTMLRecurse(List<PageNavInfo> cur, List<String> lines) {
		for(PageNavInfo c : cur) {			
			
			String style = "";
			if(c.style!=null) style=" class='pageNav_"+c.style+"'";
			
			String li = "<li><a "+style+"href=\"#"+c.link+"\">"+c.text+"</a>";
			lines.add(li);
			
			if(c.subs!=null) {
				lines.add("<ul>");
				makePageNavHTMLRecurse(c.subs,lines);
				lines.add("</ul>");
			}
			
			lines.add("</li>");
			
		}
	}	
	private int makePageNavRecurse(String fileName, List<PageNavInfo> parent, int level, int pos, List<PageNavInfo> pageNav) {		
		List<PageNavInfo> ret = new ArrayList<PageNavInfo>();
		while(true) {
			if(pos==pageNav.size() || pageNav.get(pos).level<level) {
				parent.get(parent.size()-1).subs = ret;
				return pos;
			}
			if(pageNav.get(pos).level == level) {
				ret.add(pageNav.get(pos));
				pos = pos + 1;
				continue;
			}
			if(pageNav.get(pos).level != (level+1)) {
				throw new RuntimeException("In '"+fileName+"' Missing header level");
			}
			pos = makePageNavRecurse(fileName, ret,level+1,pos,pageNav);		
		}				
	}
	
	private void parseBlockOpen() {
		
		LineOfMarkup mark = lines.get(pos);
		String lineTrim = mark.lineTrim;
		
		if(blockType!=BlockType.NONE) {
			System.out.println(lines.get(pos).lineNumber+":"+lines.get(pos).line+":"+blockType);
			throw new MarkupException("No nested blocks allowed:");
		}
		if(lineTrim.toUpperCase().equals("{{{MEMORY")) {
			// Just a flag to treat tables specially
			mark.newLine = null;
			blockType = BlockType.MEMORY;
			return;
		}
		if(lineTrim.toUpperCase().equals("{{{PLAYME")) {
			blockType = BlockType.PLAYME;
			mark.newLine = "<div class='playMe'><div>";				
			return;
		}
		if(lineTrim.toUpperCase().equals("{{{TOURGUIDE")) {
			blockType = BlockType.TOUR;
			mark.newLine = "<div class='tourGuide'><div>";				
			return;
		}
		if(lineTrim.toUpperCase().equals("{{{HTML")) {
			blockType = BlockType.HTML;
			mark.newLine = null;
			return;
		}		
		if(lineTrim.toUpperCase().equals("{{{CODE")) {
			blockType = BlockType.CODE;
			mark.newLine = "<pre class='codePreStyle'>";		
			return;
		}
		String style = "";
		if(lineTrim.length()!=3) {
			style = " class='block_"+lineTrim.substring(3).trim()+"'";
		}		
		blockType = BlockType.PRE;
		mark.newLine = "<pre"+style+">";			
		return;				
	}
			
	private void parseBlockClose() {		
		LineOfMarkup mark = lines.get(pos);
		switch(blockType) {
		case TOUR:			
		case PLAYME:
			mark.newLine = "</div></div>";				
			break;
		case HTML:
			mark.newLine = null;
			break;			
		case NONE:
			System.out.println(mark.lineNumber+":"+pos);
			throw new MarkupException("Found a close-block but wasn't in a block");		
		case PRE:
			mark.newLine = "</pre>";					
			break;			
		case CODE:
			mark.newLine = "</pre>	";				
			break;
		case MEMORY:
			// Just a flag
			mark.newLine = null;
			break; 
		}
		blockType = BlockType.NONE;		
	}
 
	/**
	 * Parse the given input markup file and write the HTML to the given
	 * output file.
	 * @param contentRoot the root path of the content (we may pull in other files)
	 * @param inFile the name of the input markup file 
	 * @param outFile the output file to generate
	 * @param breadCrumbs the breadcrumb string for this page
	 * @param siteNav the site navigation string (common to all pages)
	 * @param title default page title
	 * @throws IOException with file operation exceptions
	 */
	public void translate(String contentRoot, String inFile, String outFile, 
			String breadCrumbs, String siteNav,	String title) throws IOException {
		
		this.contentRoot = contentRoot;
		Path ip = Paths.get(inFile);
		List<String> ls = Files.readAllLines(ip);
		lines = LineOfMarkup.convert(ls, inFile);
		expandIncludes(lines,inFile);
		
		// Wrap the code in code blocks
		int x = 0;
		boolean isCodeBlock = false;
		
		lines.add(new LineOfMarkup("@@@","@@@",-1));
				
		while(x<lines.size()) {
			
			// Other types of blocks can't be code blocks			
			if(lines.get(x).lineTrim.startsWith("{{{")) {
				while(!lines.get(x).lineTrim.startsWith("}}}")) {
					++x;
				}
				continue; // Back around
			}
									
			boolean ic = isCodeLine(x);
			if(ic) {				
				lines.get(x).codeLine = new CodeLine(lines.get(x).line);
				if(!isCodeBlock) {
					lines.add(x,new LineOfMarkup("{{{CODE","",-1));					
					isCodeBlock = true;
					x=x+1; // Skip over the newly created					
				}				
			} else {
				if(isCodeBlock) {
					lines.add(x,new LineOfMarkup("}}}","",-1));
					isCodeBlock = false;
					x=x+1; // Skip over the newly created					
				}							
			}			
			++x;
		}
		
		// Work backwards to give all code labels an address		
		int address = Integer.MAX_VALUE;
		for(x=lines.size()-1;x>=0;--x) {
			LineOfMarkup mark = lines.get(x);
			CodeLine code = mark.codeLine;
			if(code!=null) {
				if(code.address>=0) {
					address = code.address;					
				}
				if(code.label!=null) {
					code.address = address;
					labelValues.put(address, mark);
				}
			}
		}
		
		// Getting ready to run the markup line by line
		ids = new ArrayList<String>();                // Unique IDs used on this page
		variables = new HashMap<String,String>();     // Variables defined on this page
		variables.put("template", "master.template"); // Default page template
		variables.put("title", title);                // The page title
		rootPageNav = new PageNavInfo();		      // Navigation tree
		rootPageNav.level = 0;		                  // Starting at the root level    
		navCursor = rootPageNav;		              // Current heading position within the page tree
						
        boolean startedPElement  = false;             // Are we in a <p> element (must be closed later)
		
		pos = -1;
		while((pos+1)<lines.size()) {
			++pos;
			LineOfMarkup mark = lines.get(pos);
			String lineTrim = mark.lineTrim;			
			
			// Set a variable's value
			if(lineTrim.startsWith("%%")) {
				setVariable();
				continue;
			}
			
			// Header
			if(lineTrim.startsWith("#")) {				
				parseHeader();							
				continue;
			}
			
			// Bullets
			if(lineTrim.startsWith("*")) {				
				parseBullet();
				continue;				
			}
			
			// Starting/stopping blocks of markup
			if(lineTrim.startsWith("{{{")) {
				parseBlockOpen();				
				continue;				
			}			
			if(lineTrim.startsWith("}}}")) {
				parseBlockClose();
				continue;
			}
			
			if(lineTrim.startsWith("||")) {
				parseTable();
				continue;
			}
												
			// Special actions if we are in a block
			if(blockType==BlockType.CODE) {				
				fixCode(mark);
			} else {						
				if(blockType!=BlockType.HTML) { // if we are in HTML then don't do any fixing
					if(blockType!=BlockType.PRE) { // PRE and CODE are wrapped in <pre> ... no need to <p>
						if(lineTrim.isEmpty()) {
							// We are prepared for adjacent blank lines
							if(startedPElement) {
								LineOfMarkup ne = new LineOfMarkup("</p>","GENERATED",-1);
								lines.add(pos,ne);
								++pos;								
								startedPElement = false;
							}
						} else {
							if(!startedPElement) {
								LineOfMarkup ne = new LineOfMarkup("<p>","GENERATED",-1);
								lines.add(pos,ne);
								++pos;		
								startedPElement=true;
							}
						}
					}
					mark.newLine = fixHTMLText(mark.newLine);					
				}
			}								
									
		}
		
		if(blockType!=BlockType.NONE) {
			System.out.println("THIS IS WHAT I AM FIXING");
		}
		
		// Pull the HTML lines together into one string
		StringBuffer body = new StringBuffer();
		for(LineOfMarkup m : lines) {
			if(m.newLine!=null) {
				
				if(m.fileName.equals("@@@")) continue;
				
				if(m.giveId!=null) {
					body.append("<span id='"+m.giveId+"'></span>");
				}
				
				body.append(m.newLine);
				body.append('\n');
			}
		}
							
		// Load the template
		String templateFile = variables.get("template");		
		String template = "<!-- %%BODY%% -->";
		Path p = Paths.get(contentRoot+"/"+templateFile);
		List<String> tlines = Files.readAllLines(p);
		template = CU.listToString(tlines);		
		
		// Get page_nav fillin		
		String pageTree = makePageNav(inFile,rootPageNav.subs);
						
		// Fill in the template substitutions
		template = CU.replaceAll(template, "<!-- %%title=%% -->", variables.get("title"));		
		template = CU.replaceAll(template, "<!-- %%CONTENT_TITLE%% -->", variables.get("title"));
		template = CU.replaceAll(template, "<!-- %%BREAD_CRUMBS%% -->", breadCrumbs);
		template = CU.replaceAll(template, "<!-- %%PAGE_TREE%% -->", pageTree);
		template = CU.replaceAll(template, "<!-- %%SITE_TREE%% -->", siteNav);
		template = CU.replaceAll(template, "<!-- %%CONTENT%% -->", body.toString());
		template = CU.replaceAll(template, "<!-- %%IMAGE%% -->", variables.get("image"));
				
		// Write the output file
		PrintWriter pw = new PrintWriter(outFile);
		pw.print(template);
		pw.flush();
		pw.close();	
		
	}	
	
	LineOfMarkup findCodeAtAddress(int address) {
		for(LineOfMarkup mark : lines) {			
			CodeLine code = mark.codeLine;
			if(code!=null) {				
				if(code.address == address) {
					return mark;
				}
			}						
		}		
		return null;
	}
	
	String stripOverride(String s) {
		s = CU.replaceAll(s, "@@ ", "");
		return CU.replaceAll(s, "@@", "");
	}
	
	String fixCodeHTMLText(String text) {
		List<String> keeps = new ArrayList<String>();
		while(true) {
			int i = text.indexOf('`');
			if(i<0) break;
			int j = text.indexOf('`',i+1);
			keeps.add(text.substring(i+1, j));
			text = text.substring(0,i)+"__FILLIN__"+(keeps.size()-1)+"__"+text.substring(j+1);
		}
		text = fixHTMLText(text);
		for(int x=0;x<keeps.size();++x) {
			text = CU.replaceAll(text, "__FILLIN__"+x+"__", keeps.get(x));
		}
		return text;
	}
	
	void fixCode(LineOfMarkup mark) {	
		
		CodeLine code = mark.codeLine;		
				
		if(code.opcode==null) {
			mark.newLine = fixCodeHTMLText(mark.line);		
			return; // No opcode ... just data
		}
		
		CPU cpu = CPU.getCPU(variables.get("cpu"));
		if(cpu==null) {
			mark.newLine = fixCodeHTMLText(mark.line);		
			return; // No CPU ... nothing to do
		}
		
		// Separate the code text into left (before comment) and right. We
		// don't do fill-ins in the comment.
		String leftPart = mark.newLine;
		String rightPart = "";
		int i = leftPart.indexOf(";");
		if(i>=0) {
			rightPart = leftPart.substring(i);
			leftPart = leftPart.substring(0, i);
		}
		
		boolean accessOverride = rightPart.contains("@@");
		
		
		i = leftPart.indexOf("$"); // Numerics are always hex
		if(i<0) {
			mark.newLine = fixCodeHTMLText(mark.line);		
			return; // Nothing to fill in
		}
		
		int j = i+1;
		while(true) {
			char c = leftPart.charAt(j);
			if (!((c>='0' && c<='9') || (c>='A' && c<='F') || c=='-')) break;
			++j;
			if(j==leftPart.length()) break;
		}
		
		int num = Integer.parseInt(leftPart.substring(i+1, j),16);
		int numlen = j-i;
		
		String dps = variables.get("directPage");
		int dp = 0;
		if(dps!=null) dp = Integer.parseInt(dps,16);	
						
		// The opcode itself has much better information about what this access is
		// But for now we'll ask based on text (the code.opcode is text)
		Opcode op = cpu.matchDisassembly(code);
				
		AddressAccess a = cpu.getAccess(op, num, dp, accessOverride); 
		if(a==null) {
			mark.newLine = stripOverride(fixCodeHTMLText(mark.line));		
			return; // This number isn't a memory reference
		}
		
		// i = start of numeric sub
		// numlen = length of numeric sub
		// a = access information		
						
		ExternalMemoryMap emm = null;
		AddressTableEntry e = null;
		for(ExternalMemoryMap map : memoryMaps) {			
			e = map.map.findEntryForAccess(num+dp, a.busDir, a.busType); 
			if(e != null) {
				emm = map;
				break;
			}			
		}
		
		String name = null;   // the symbolic name of the number
		String url = null;    // URL link for the anchor
		String style = null;  // the CSS styling for the link
		String target = "";   // target window for memory address links
		int mod = 0;
		
		String offset = "";
		
		if(e!=null) {
			// We found a memory map
			name = e.name;
			if(name.isEmpty()) {
				name = CU.hex4(e.start);
			}
			url = emm.htmlFile+"#addr_"+name;
			style = "addr_"+emm.name.substring(1);		
			target = " target='"+emm.name.substring(1)+"'";
			if((num+dp)!=e.start) {
				int k = (num+dp)-e.start;
				if(k<256) {
					offset="+"+CU.hex2(k);
					mod=3;
				} else {
					offset="+"+CU.hex4(k);
					mod=5;
				}				
			}
		} else {	
			// It might be in the code ... but only on the main bus
			if(a.busType==BusType.MAIN) {				
				LineOfMarkup lab = labelValues.get(num);
				if(lab!=null) {
					// We found a code label
					name = lab.codeLine.label;
					url = "#addr_"+name;
					style = "addr_code";
					lab.giveId = "addr_"+name;					
				} else {
					lab = findCodeAtAddress(num);
					if(lab!=null) {
						name = leftPart.substring(i, i+numlen);	
						url = "#addr_"+CU.hex4(num);
						style = "addr_code";
						lab.giveId = "addr_"+CU.hex4(num);	
					} 
				}
			} 
		}		
		
		if(name==null) {
			mark.newLine = stripOverride(fixCodeHTMLText(mark.line));		
			return;
		}			
		
		// Here is where the fillin goes (we'll be entizing the original)
		leftPart = leftPart.substring(0,i)+"_@FILLIN@_"+leftPart.substring(i+numlen);
									
		String html = "<a title='"+CU.hex4(num)+"' class='"+style+"' href='"+url+"'"+target+">"+name+offset+"</a>";
																
		// The symbolic name is usually longer or shorter than the numeric constant it
		// replaces. We need to add or remove spaces before the comment to preserve the
		// visible spacing.								
		
		numlen = mod + name.length() - numlen; // Number of spaces to remove (negative means add)
							
		while(numlen<0) {
			leftPart = leftPart + " ";
			++numlen;
		}
		while(numlen>0 && leftPart.charAt(leftPart.length()-1)==' ') {
			leftPart = leftPart.substring(0,leftPart.length()-1);
			--numlen;
		}
					
		// Strip {...} from comments. We only do this to comments that we
		// are making fill-ins to.		
		
		i = rightPart.indexOf("{");
		if(i>=0) {
			j = rightPart.lastIndexOf("}");
			if(j>0) {
				rightPart = rightPart.substring(0,i-1)+rightPart.substring(j+1);
			}
		}
		
		mark.newLine = stripOverride(fixCodeHTMLText(leftPart + rightPart));	
		mark.newLine = CU.replaceAll(mark.newLine, "_@FILLIN@_", html);
		
	}

}
