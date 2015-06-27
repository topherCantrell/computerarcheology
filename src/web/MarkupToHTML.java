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
	
	List<String> headers = new ArrayList<String>();
	String rawMode = "none";
	String mode = "none";
	
	private boolean markDownContinueRaw(String line, List<String> ret) {
		if(line.trim().startsWith("}}}")) {
			if(rawMode.equals("pre")) {
				ret.add("</pre>");
			}
			return true;
		}
		
		ret.add(line);
		return false;
	}
	
	private void markDownStartRaw(String line, List<String> ret) {
		
		// Code uses a special coloring class
		if(line.startsWith("{{{code")) {
			rawMode = "pre";
			ret.add("<pre class=\"codePreStyle\">");
			return;
		}
		
		// HTML .. no <pre>
		if(line.startsWith("{{{html")) {
			rawMode = "html";
			return;
		}
		
		// Simple raw block is just <pre>
		ret.add("<pre>");
		rawMode = "pre";
	}
	
	private String entizeString(String s) {
		String ret = "";
		for(int i=0;i<s.length();++i) {
			char c = s.charAt(i);
			if(c=='<') {
				ret = ret + "&lt;";
			} else if(c=='>') {
				ret = ret + "&gt;";
			} else if(c=='&') {
				ret = ret + "&amp;";
			} else {
				ret = ret + c;
			}
		}		
		return ret;
	}
	
	private String markDownHeaders(String proc, List<PageNavInfo> pageNav) {
		//     text        lid   id
        // == This is it == it #thisIt

        // Count the leading "=". This is the
        // header number.
		
		int i = 0;
		while(proc.charAt(i)=='=') {
			i = i + 1;
		}
		
		int j = proc.indexOf('=',i);
		
		String text = proc.substring(i,j).trim();
		String altText = proc.substring(j+i).trim();
		String lid = "";
		
		int x = altText.indexOf("#");
		if(x>=0) {
			lid = altText.substring(x+1).trim();
			altText = altText.substring(0,x).trim();
		} else {
			lid = makeHeaderLink(text);
		}
		
		if(altText.length()==0) {
			altText = text;
		}
		
		String ret = "<h"+i+" id=\""+lid+"\" class=\"siteTarget\">"+text+"</h"+i+">";
		
		PageNavInfo n = new PageNavInfo();
		n.level = i;
		n.link = lid;
		n.text = altText;
		pageNav.add(n);
		
		//System.out.println(n.level+" "+n.link+" "+n.text);
		
		return ret;
	}
	
	private String makeHeaderLink(String text) {
		String ret = "";
		for(int x=0;x<text.length();++x) {
			char c=text.charAt(x);
			if( (c>='a' && c<='z') || (c>='A' && c<='Z') || (c>='0' && c<='9') ) {
				ret = ret + c;
			}
		}		
		if(ret.length()==0) {
			ret = "header";
		}
		if(headers.contains(ret)) {
			ret = ret + "" + headers.size();
		}
		headers.add(ret);
		return ret;
	}
	
	private String markDownBraces(String proc) {
						
		while(true) {			
			int i = proc.indexOf("[");		
			int ii = i+1;
			if(i<0) return proc;
			
			String ltp = "<a href=\"###HREF###\">###TEXT###</a>";						
			int j = proc.indexOf("]",i);			
			if(proc.charAt(i+1)=='!') {
				ltp = "<img src=\"###HREF###\">###TEXT###</img>";
				ii = ii + 1;
			}
			
			String a = proc.substring(ii,j);	
			
			int x = a.indexOf(" ");
			if(x>=0) {
				ltp = CU.replaceAll(ltp, "###HREF###", a.substring(0,x));
				ltp = CU.replaceAll(ltp, "###TEXT###", a.substring(x+1).trim());
			} else {
				ltp = CU.replaceAll(ltp, "###HREF###", a);
				ltp = CU.replaceAll(ltp, "###TEXT###", a);				
			}
			proc = proc.substring(0,i)+ltp+proc.substring(j+1);			
		}
		
	}
	
	private String markDownStartBullets(String proc) {
		return "<ul><li>"+proc.substring(1).trim()+"</li>";
	}

	private void markDownEndBullets(List<String> ret) {
		ret.add("</ul>");
	}

	private String markDownContinueBullets(String proc) {
		return "<li>"+proc.substring(1).trim()+"</li>";
	}
	
	
	private String markDownStartTable(String proc) {
		
		String[] hdrs = proc.split("\\|\\|");		
		
		if(hdrs[1].startsWith("=")) {
			hdrs[1] = hdrs[1].substring(1).trim();
			String s = "<table class=\"table table-condensed\"><thead><tr>";		
			for(int x=1;x<hdrs.length;++x) {
				s = s + "<th>" + hdrs[x].trim()+ "</th>";
			}
			return s + "</tr></thead>";
		} else {
			String s = "<table class=\"table table-condensed\"><tr>";
			for(int x=1;x<hdrs.length;++x) {
				s = s + "<th>" + hdrs[x].trim()+ "</th>";
			}
			return s + "</tr>";
		}
		 
	}

	private void markDownEndTable(List<String> ret) {
		ret.add("</table>");
	}

	private String markDownContinueTable(String proc) {
		String[] cells = proc.split("\\|\\|");
		String s = "<tr>";
		for(int x=1;x<cells.length;++x) {
			s = s + "<td>" + cells[x].trim() + "</td>";
		}
		return s + "</tr>";
	}
			
	
	
	public String markDown(String fileName, List<String> lines, List<PageNavInfo> pageNav) {		
		
		List<String> ret = new ArrayList<String>();
		
		mode = "none";
		headers.clear();
		
		int pos = 0;
		
		try {
		
			for(String line : lines) {
				++pos;
				
				// In raw mode we don't do any processing at all
				if(mode.equals("raw")) {
					boolean nm = markDownContinueRaw(line, ret);
					if(nm) {
						mode = "none";
					}
					continue;
				}
				
				String proc = line.trim();
				
				// This is how you get into raw mode
				if(proc.startsWith("{{{")) {
					markDownStartRaw(proc,ret);
					mode = "raw";
					continue;
				}
				
				if(proc.startsWith("%%")) {
					// Ignore any defines
					continue;
				}
				
				// Make this string HTML friendly
				proc = entizeString(proc);
				
				// Handle line breaks
				proc = CU.replaceAll(proc, "[[br]]", "<br>");
				proc = CU.replaceAll(proc, "[[BR]]", "<br>");
				
				// Handle paragraph breaks
				if(proc.length()==0) {
					proc = "<p />";
				}
				
				// Handle headers
				if(proc.startsWith("=")) {
					proc = markDownHeaders(proc,pageNav);
				}
				
				// Links
				if(proc.contains("[")) {
					proc = markDownBraces(proc);
				}
				
				// Bullets
				if(mode.equals("bullets")) {
					if(proc.startsWith("*")) {
						proc = markDownContinueBullets(proc);
					} else {
						markDownEndBullets(ret);
						mode = "none";
					}				
				} else if(proc.startsWith("*")) {
					if(proc.startsWith("*")) {
						proc = markDownStartBullets(proc);
						mode = "bullets";
						ret.add(proc);
						continue;
					}				
				}			
				
				// Table
				if(mode.equals("table")) {
					if(proc.startsWith("||")) {
						proc = markDownContinueTable(proc);
					} else {
						markDownEndTable(ret);
						mode = "none";
					}
				} else {
					if(proc.startsWith("||")) {
						proc = markDownStartTable(proc);
						mode = "table";
						ret.add(proc);
						continue;
					}
					
				}
							
				ret.add(proc+" ");
							
			}		
			
			return CU.listToString(ret);
		
		} catch (RuntimeException e) {
			RuntimeException er = new RuntimeException("File '"+fileName+"' line "+pos,e);
			throw er;
		}
	}

	public void getFillIns(String preamble, Map<String, String> fills, List<String> lines) {
		for(String s : lines) {
			String t = s.trim();
			if(t.startsWith(preamble)) {
				t = t.substring(preamble.length()).trim();
				int i = t.indexOf(" ");
				String key = t.substring(0,i);
				String value = t.substring(i+1).trim();
				fills.put(key, value);
			}
		}		
	}
	
	private String makePageNav(String inFile, List<PageNavInfo> pageNav) {
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
			
			String cl = "n";
			if(c.level==1) {
				cl = "1";
			}
			
			String li = "<li class=\"sn"+cl+"\"><a class=\"sna\" href=\"#"+c.link+"\">"+c.text+"</a>";
			lines.add(li);
			
			if(c.subs!=null) {
				lines.add("<ul>");
				makePageNavHTMLRecurse(c.subs,lines);
				lines.add("</ul>");
			}
			
			lines.add("</i>");
			
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
		
	public void translate(String contentRoot, String inFile, String outFile, 
			String breadCrumbs, String siteNav, String nav) throws IOException 
	{
		Path ip = Paths.get(inFile);
		List<String> lines = Files.readAllLines(ip);
		translate(contentRoot, inFile, outFile, breadCrumbs, siteNav, nav, lines);
	}
	
	public void translate(String contentRoot, String inFile, String outFile, 
			String breadCrumbs, String siteNav, String nav, List<String> lines) throws IOException 
	{									
		
		List<PageNavInfo> pageNav = new ArrayList<PageNavInfo>(); // Page navigation targets
		
		Map<String,String> fills = new HashMap<String,String>(); // Fill-ins		
		fills.put("template", "master.template"); // Default page template
		fills.put("title", nav);
		
		getFillIns("%%",fills,lines);
		
		// Process the markdown (results in a string)		
		String body = markDown(inFile,lines, pageNav);
		
		// Read the template
		String tempName = fills.get("template");
		String template = "<!-- %%BODY%% -->";
		if(tempName!=null) {
			Path p = Paths.get(contentRoot+"/"+tempName);
			List<String> tlines = Files.readAllLines(p);
			template = CU.listToString(tlines);
		}
				
		// Get page_nav fillin		
		String pageTree = makePageNav(inFile,pageNav);
		
		String im = fills.get("image");
		if(im!=null) {
			im = "<img src=\"" + im + "\" height=\"90\" style=\"PADDING-LEFT: 40px\"/>";
		} else {
			im = "";
		}
		
		template = CU.replaceAll(template, "<!-- %%TITLE%% -->", fills.get("title"));		
		template = CU.replaceAll(template, "<!-- %%CONTENT_TITLE%% -->", fills.get("title"));
		template = CU.replaceAll(template, "<!-- %%BREAD_CRUMBS%% -->", breadCrumbs);
		template = CU.replaceAll(template, "<!-- %%PAGE_TREE%% -->", pageTree);
		template = CU.replaceAll(template, "<!-- %%SITE_TREE%% -->", siteNav);
		template = CU.replaceAll(template, "<!-- %%CONTENT%% -->", body);
		template = CU.replaceAll(template, "<!-- %%IMAGE%% -->", im);
				
		PrintWriter pw = new PrintWriter(outFile);
		pw.print(template);
		pw.flush();
		pw.close();	
						
	}

}
