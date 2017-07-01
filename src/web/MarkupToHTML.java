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

import code.CU;

public class MarkupToHTML {
	
	Map<String,String> variables; // Any %% variables in the markup
	PageNavInfo rootPageNav;      // The navigation tree for the page
	List<String> ids;             // Unique IDs on the page
	StringBuffer body;	
	PageNavInfo navCursor;        // For moving up and down the navigation tree as we build it
	List<String> lines;
	int pos;
		
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
	void setVariable(String com) {
		int i = com.indexOf("=");
		if(i<0) {
			throw new MarkupException("Expected '=' in '"+com+"'");
		}
		String key = com.substring(2,i).trim();
		String value = com.substring(i+1).trim();
		variables.put(key,value );
		//System.out.println(":"+key+":"+value+":");
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
			if(j+1<line.length() && line.charAt(j+1)=='(') {
				int k = line.indexOf(')',j+1);
				if(k<0) return line;
				link = line.substring(j+2,k);
				j = k;
			}
			String rep = "<a href='"+link+"'>"+text+"</a>";
			//System.out.println(rep);
			line = line.substring(0,i)+rep+line.substring(j+1);
		}		
	}
	
	/**
	 * Parse the header and create a navigation link
	 * @param lineTrim the header line
	 */
	void parseHeader(String lineTrim) {
		int level = 0;
		while(level<lineTrim.length() && lineTrim.charAt(level)=='#') {
			++level;
		}
		
		PageNavInfo ni = new PageNavInfo();
		
		if(level>navCursor.level) {
			if(navCursor.level+1 != level) {
				throw new MarkupException("Header skipped a sublevel '"+lineTrim+"'");
			}								
			navCursor.subs.add(ni);
			navCursor = ni;					
		} else {
			for(int x=1;x<level;++x) {
				navCursor = navCursor.parent;
			}					
			navCursor.subs.add(ni);
		}
		
		ni.level = level;
		ni.parent = navCursor;
		ni.text = lineTrim.substring(level).trim();
		ni.link = addID(PageNavInfo.idFromText(ni.text));	
		
		body.append("<h"+(level+1)+" id='"+ni.link+"'>"+ni.text+"</h"+(level+1)+">\n");
	}
	
	/**
	 * Parse a list of bullets
	 * @param lineTrim the first bullet
	 */
	void parseBullet(String lineTrim) {
		// TODO multi-levels if ever needed
		--pos; // Back up to this one
		body.append("<ul>\n");
		while(pos<lines.size()) {
			lineTrim = lines.get(pos++).trim();			
			if(!lineTrim.startsWith("*")) break;
			lineTrim = lineTrim.substring(1).trim();
			//System.out.println(">>"+lineTrim+"<<");
			body.append("<li>"+fixHTMLText(lineTrim)+"</li>\n");
		}		
		body.append("</ul>\n");
	}
	
	/**
	 * Processes links and entities.
	 * @param line the line to be HTML
	 * @return the modified line
	 */
	String fixHTMLText(String line) {
		line = fixLinks(line);
		// TODO entize
		return line;
	}
	
	/**
	 * Expand all include directives
	 * @param lines the current list of lines
	 * @param inFile the name of the input file
	 * @throws IOException file errors
	 */
	void expandIncludes(List<String> lines,String inFile) throws IOException {
		for(int x=lines.size()-1;x>=0;--x) {
			String s = lines.get(x).trim();
			if(s.startsWith("##include ")) {
				int i = inFile.lastIndexOf("/");
				List<String> inc = Files.readAllLines(Paths.get(inFile.substring(0,i+1)+s.substring(10).trim()));
				lines.remove(x);
				lines.addAll(x,inc);				
			}
		}
	}
	
	/**
	 * Parse the given input markup file and write the HTML to the given
	 * output file.
	 * @param contentRoot the root path of the content (we may pull in other files)
	 * @param inFile the name of the input markup file 
	 * @param outFile the output file to generate
	 * @param breadCrumbs the breadcrumb string for this page
	 * @param siteNav the site navigation string (common to all pages)
	 * @param pageNav the page navigation string for this page
	 * @param lines the lines of markdown
	 * @throws IOException with file operation exceptions
	 */
	public void translate(String contentRoot, String inFile, String outFile, String breadCrumbs, String siteNav,
			String pageNav, List<String> lines) throws IOException {
		
		this.lines = lines;
		//lines = Files.readAllLines(Paths.get(contentRoot,inFile));
		
		ids = new ArrayList<String>();
		variables = new HashMap<String,String>();
		rootPageNav = new PageNavInfo();		
		rootPageNav.level = 1;		
		navCursor = rootPageNav;		
		
		body = new StringBuffer();
		
		boolean startedPElement  = false;
		
		pos = 0;
		while(pos<lines.size()) {
			String line = lines.get(pos++);			
			String lineTrim = line.trim();			
			
			// Set a variable's value
			if(lineTrim.startsWith("%%")) {
				setVariable(lineTrim);
				continue;
			}
			
			// Header
			if(lineTrim.startsWith("#")) {				
				parseHeader(lineTrim);							
				continue;
			}
			
			if(lineTrim.startsWith("*")) {				
				parseBullet(lineTrim);
				continue;				
			}
			
			if(lineTrim.startsWith("{{{")) {
				System.out.println("BLOCK:"+lineTrim);
				continue;
				// Block mode
				// Some are completely <pre> and some are complete markdown with div wraps
			}
			
			// TODO Tables
															
			if(lineTrim.isEmpty()) {
				// We are prepared for adjacent blank lines
				if(startedPElement) {
					body.append("</p>\n");
					startedPElement = false;
				}
			} else {
				// TODO this logic will change with <pre> and <html> elements
				if(!startedPElement) {
					body.append("<p>\n");
					startedPElement=true;
				}
			}
			
			// Depends on what kind of block we are in
			line = fixHTMLText(line);
			
			body.append(line);
			
			body.append("\n");
			continue;
			
		}
							
		// Load the template
		String templateFile = variables.get("template");
		if(templateFile==null) {
			templateFile = "master.template";
		}		
		String template = "<!-- %%BODY%% -->";
		Path p = Paths.get(contentRoot+"/"+templateFile);
		List<String> tlines = Files.readAllLines(p);
		template = CU.listToString(tlines);		
						
		// Fill in the template substitutions
		template = CU.replaceAll(template, "<!-- %%title=%% -->", variables.get("title"));		
		template = CU.replaceAll(template, "<!-- %%CONTENT_TITLE%% -->", variables.get("title"));
		template = CU.replaceAll(template, "<!-- %%BREAD_CRUMBS%% -->", breadCrumbs);
		template = CU.replaceAll(template, "<!-- %%PAGE_TREE%% -->", pageNav);
		template = CU.replaceAll(template, "<!-- %%SITE_TREE%% -->", siteNav);
		template = CU.replaceAll(template, "<!-- %%CONTENT%% -->", body.toString());
		template = CU.replaceAll(template, "<!-- %%IMAGE%% -->", variables.get("image"));
				
		// Write the output file
		PrintWriter pw = new PrintWriter(outFile);
		pw.print(template);
		pw.flush();
		pw.close();					
						
	}
	
	// Address and Code derived classes use this
	protected void translate(String contentRoot, String inFile, String outFile, 
			String breadCrumbs, String siteNav, String nav) throws IOException 
	{
		Path ip = Paths.get(inFile);
		List<String> lines = Files.readAllLines(ip);
		expandIncludes(lines,inFile);
		translate(contentRoot, inFile, outFile, breadCrumbs, siteNav, nav, lines);
	}
	
}
