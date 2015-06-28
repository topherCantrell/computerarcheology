package web;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

import cleans.LinkFix;
import code.CodeFile;
import code.CodeLine;

public class CodeToHTML extends MarkupToHTML {
	
	public void translate(String contentRoot, String inFile, String outFile, 
			String breadCrumbs, String siteNav, String nav) throws IOException 
	{
		
		// Load the code file (and all its address tables)
		Path ip = Paths.get(inFile);
		CodeFile code = new CodeFile(ip);
		
		// Fix up the inter-HTML links
		LinkFix fixer = new LinkFix();
		fixer.fix(code, false);			
		
		// Convert to pure markdown		
		List<String> lines = new ArrayList<String>();
		boolean inMarkup = true;		
		for(CodeLine c : code.code) {			
			if(c.comment!=null && c.comment.startsWith(";")) {
				if(!inMarkup) {
					lines.add("}}}");
					inMarkup = true;
				}				
				lines.add(c.originalText.trim().substring(2).trim());
			} else {
				if(inMarkup) {
					lines.add("{{{code");
					inMarkup = false;
				}
				lines.add(codeToHTML(c));
			}			
		}
		
		// Do the markdown
		super.translate(contentRoot, inFile, outFile, breadCrumbs, siteNav, nav, lines);		
		
	}

	private String codeToHTML(CodeLine c) {
		// c.flag != null if we need to insert a raw-address span
		// c.label != null if we need to insert a label span		
		// c.comment.startsWith(";{") if we need to insert an anchor
		
		String ret = c.originalText;
		
		if(c.flag!=null || c.label!=null) {
			// This is a target. Give it an id for HREFfing.
			String targ = c.label;
			if(targ==null) {
				targ = ret.substring(0,4);
			}
			String a = "<span class=\"siteTarget\" id=\""+targ+"\">" +
			           ret.charAt(0)+"</span>"+
					   ret.substring(1);
			ret = a;			
		}		
				
		int i = ret.indexOf(";{");
		if(i>=0) {
			int j = ret.lastIndexOf("}");
			String spec = ret.substring(i+2,j);
			if(spec.length()>0 && spec.charAt(0)=='{') {
				spec = spec.substring(1,spec.length()-1);
			}
			ret = ret.substring(0,i+1)+ret.substring(j+1);
			
			if(spec.length()<5) {
				throw new RuntimeException("Bad Specification '"+c.originalText+"'");
			}
			
			String [] sp = spec.split(":");
			String href = sp[0];
			String text = sp[1];
			int index = Integer.parseInt(sp[2]);
			if(href.startsWith("#$")) {
				href = "#"+href.substring(2);
			}
			
			if(href.length()==0 || text.length()==0) {
				throw new RuntimeException("Bad Specification '"+c.originalText+"'");
			}
									
			// Replace the numeric constant with a link
			String targetWindow = "_self";
			if(index>0) {
				targetWindow = "TABLE_"+index;
			}
			String toReplace = c.opcode.substring(c.numericConstantStart-1,c.numericConstantEnd);
			String replaceWith = "<a class=\"addressLink"+index+"\" href=\""+href+"\" title=\""+toReplace+"\" target=\""+targetWindow+"\">"+text+"</a>";			
			i = ret.indexOf(toReplace);
			ret = ret.substring(0,i)+replaceWith+ret.substring(i+toReplace.length());
			
			// Fix any spacing issues (the label is likely longer than the original numeric constant)
			i = ret.indexOf(";") - 1;
			j = i;
			while(ret.charAt(j)==' ') {
				--j;
			}
			int k = text.length()-toReplace.length();
			if(k>0) {
				if(k<(i-j)) {
					String a = ret.substring(0,i-k)+ret.substring(i);
					ret = a;
				} else {
					//throw new RuntimeException(ret+" "+k+" "+(i-j));
				}
			}
												
		}
				
		return ret;
	}

}
