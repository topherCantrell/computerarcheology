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

public class NewMarkupToHTML {
	
	Map<String,String> variables; // Any %% variables in the markup
	PageNavInfo rootPageNav;      // The navigation tree for the page
	List<String> ids;             // Unique IDs on the page
		
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
	 * Parse the given input markup file and write the HTML to the given
	 * output file.
	 * @param contentRoot the root path of the content (we may pull in other files)
	 * @param inFile the name of the input markup file 
	 * @param outFile the output file to generate
	 * @throws IOException with file operation exceptions
	 */
	public void makeHTML(String contentRoot, String inFile, String outFile) throws IOException {
		List<String> lines = Files.readAllLines(Paths.get(contentRoot,inFile));
		
		variables = new HashMap<String,String>();
		rootPageNav = new PageNavInfo();
		ids = new ArrayList<String>();
		rootPageNav.level = 1;
		
		PageNavInfo navCursor = rootPageNav;		
		
		StringBuffer body = new StringBuffer();
		
		boolean startedPElement  = false;
		
		int pos = 0;
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
							
				continue;
			}
			
			if(lineTrim.startsWith("*")) {
				System.out.println("BULLET:"+lineTrim);
				
				body.append("<p>BULLET ITEM HERE</p>\n");
				continue;
				// Remember, we stripped off space counts
				// We can use the PageNav tree class here too
				// And we can use that for site info
			}
			
			if(lineTrim.startsWith("{{{")) {
				System.out.println("BLOCK:"+lineTrim);
				continue;
				// Block mode
				// Some are completely <pre> and some are complete markdown with div wraps
			}
			
			// Tables
			
			// Entize strings
			
			// Expand links (after entize)	
			
			// Blank lines are end of paragraphs
			
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
			
			body.append(line);
			body.append("\n");
			continue;
			
		}
				
		// TODO build these
		String breadCrumbs = "BREAD";
		String pageTree = "PAGETREE";
		String siteNav = "SITENAV";
			
		// Load the template
		String templateFile = variables.get("template");
		if(templateFile==null) {
			templateFile = "master.template";
		}		
		String template = "<!-- %%BODY%% -->";
		Path p = Paths.get(contentRoot+"/"+templateFile);
		List<String> tlines = Files.readAllLines(p);
		template = CU.listToString(tlines);		
		
		// This is the image at the top of the page (beside the logo)
		String im = variables.get("image");
		if(im!=null) {
			im = "<img class='pageImage' src=\"" + im + "\"/>";
		} else {
			im = "";
		}
		
		// Fill in the template substitutions
		template = CU.replaceAll(template, "<!-- %%TITLE%% -->", variables.get("title"));		
		template = CU.replaceAll(template, "<!-- %%CONTENT_TITLE%% -->", variables.get("title"));
		template = CU.replaceAll(template, "<!-- %%BREAD_CRUMBS%% -->", breadCrumbs);
		template = CU.replaceAll(template, "<!-- %%PAGE_TREE%% -->", pageTree);
		template = CU.replaceAll(template, "<!-- %%SITE_TREE%% -->", siteNav);
		template = CU.replaceAll(template, "<!-- %%CONTENT%% -->", body.toString());
		template = CU.replaceAll(template, "<!-- %%IMAGE%% -->", im);
				
		// Write the output file
		PrintWriter pw = new PrintWriter(outFile);
		pw.print(template);
		pw.flush();
		pw.close();					
						
	}
	
	/*
	private void printPageNavInfo(PageNavInfo p) {
		for(int x=0;x<p.level;++x) {
			System.out.print(" ");
		}
		System.out.println(":"+p.text+":"+p.link+":");
		for(PageNavInfo pc : p.subs) {
			printPageNavInfo(pc);
		}
	}
	*/
	
	public static void main(String[] args) throws Exception {
		
		String contentRoot = "./content";
		
		NewMarkupToHTML trans = new NewMarkupToHTML();
		trans.makeHTML(contentRoot,"index.mark","test.html");

	}

}
