package tools.docx;

import java.util.ArrayList;
import java.util.List;

import org.jdom.Element;
import org.jdom.Namespace;

/**
 * This class encapsulates a DOCX file as a list of paragraphs.
 */
public class Book {
	
	Namespace na; // The "w" namespace used throughout the DOCX
	
	/** The list of paragraphs in the document */
	public List<Paragraph> content = new ArrayList<Paragraph>();
		
	/**
	 * This constructs a new DOCX book by parsing the list of paragraphs
	 * from the XML element.
	 * @param book the XML element
	 */
	public Book(Element book) {
		na = book.getNamespace("w");
		book = book.getChild("body",na);		
		List<?> children = book.getChildren("p",na);
		for(Object paragraphO : children) {
			Element paragraph = (Element)paragraphO;
			content.add(new Paragraph(paragraph,this));
		}	
	}
	
}
