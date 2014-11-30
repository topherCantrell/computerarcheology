package tools.docx;

import java.util.ArrayList;
import java.util.List;

import org.jdom.Element;

import tools.web.DOCXToWeb;


/**
 * This class encapsulates a DOCX paragraph as a list of text ranges combined
 * into a single string. 
 */
public class Paragraph {
	
	public String style;	
	public String combined;
	
	public String toc;	// Used in making a Table Of Contents for the document
	
	/**
	 * This constructs a new Paragraph by parsing the DOCX xml element.
	 * @param paragraph the DOCX xml element
	 * @param book the containing book
	 */
	public Paragraph(Element paragraph, Book book) 
	{
		
		List<TextRange> content = new ArrayList<TextRange>();
		
		Element sty = paragraph.getChild("pPr",book.na);
		if(sty!=null) {
			sty = sty.getChild("pStyle",book.na);
			if(sty!=null) {
				style = sty.getAttributeValue("val",book.na);
			}
		}
						
		List<?> ch = paragraph.getChildren();
		for(Object o : ch) {
			Element paraCont = (Element)o;
			if(paraCont.getName().equals("pPr")) continue;
			if(paraCont.getName().equals("r")) {				
				content.add(new TextRange(paraCont,book));									
			} else if(paraCont.getName().equals("proofErr")) {				
			} else if(paraCont.getName().equals("bookmarkStart")) {				
			} else if(paraCont.getName().equals("bookmarkEnd")) {				
			}
			
			else {
				throw new RuntimeException("Unexpected element "+paraCont);
			}
		}
		
		collapseTextRanges(content);
		
	}
	
	private void collapseTextRanges(List<TextRange> content)
	{
		String com = "";
		for(TextRange t : content) {
			if(t==null) continue;
			String dpre = "";
			String dpost = "";
			boolean entize = true;
			if(t.decoration!=null && t.decoration.length()>0) {
				if(t.decoration.equals("apple-style-span ")) {					
				} else if(t.decoration.equals("apple-converted-space ")) {					
				} 
				else if(t.decoration.indexOf("superscript ")>=0) {
					dpre = "<sup>";
					dpost = "</sup>";
				}
				else if(t.decoration.indexOf("italic ")>=0) {
					dpre = "<i>";
					dpost = "</i>";
				}
				else if(t.decoration.indexOf("subscript ")>=0) {
					entize = false; 
				}
								
				else {
					throw new RuntimeException("Unknown decoration '"+t.decoration+"'"+t);
				}
			}
			com = com + dpre;
			for(String s : t.content) {
				if(s==null) {
					com = com+"<br/>";
				} else {
					if(entize) {
						com = com + DOCXToWeb.makeHTMLFriendly(s);
					} else {
						com = com + s;
					}
				}
			}
			com = com + dpost;
			if(com.indexOf("<sub>")>=0) {
				System.out.println("::"+com+"::");
				System.exit(0);
			}
		}
		content.clear();
		combined = com;
		
	}

}
