package tools.docx;

import java.util.ArrayList;
import java.util.List;

import org.jdom.Element;

/**
 * This class encapsulates a list of content fragments. 
 */
public class TextRange {
	
	public String decoration;
	public List<String> content = new ArrayList<String>();
	
	/**
	 * This constructs a text range by parsing the DOCX xml.
	 * @param range the xml
	 * @param book the containing DOCX book
	 */
	public TextRange(Element range, Book book)
	{	
		decoration = "";
				
		List<?> chTs = range.getChildren();
		for(Object chTo : chTs) {
			Element t = (Element)chTo;
			if(t.getName().equals("t")) {
				String fr = t.getText();				
				content.add(fr);		
				//System.out.println("::"+t.getText());
			} else if(t.getName().equals("br")) {
				content.add(null);
			} else if(t.getName().equals("rPr")) {
				Element tt = (Element)t.getChildren().get(0);
				if(tt.getName().equals("i")) {
					decoration = decoration+"italic ";
				} else {				
					decoration = decoration+tt.getAttributeValue("val",book.na)+" ";
				}
			} else if(t.getName().equals("lastRenderedPageBreak")) {				
			}
			
			else {
				throw new RuntimeException("Unexpected "+t);
			}
		}	
			
	}

}
