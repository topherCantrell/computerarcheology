package tools.web;
import java.io.IOException;
import java.io.PrintStream;
import java.util.StringTokenizer;

import org.jdom.Element;
import org.jdom.JDOMException;

import tools.docx.Book;
import tools.docx.Paragraph;
import tools.file.ZIP;

/**
 * This class reads a Microsoft WORD document (XML) and makes an HTML document
 * from it. The document must be strictly formated to be processed here.
 * 
 * A set of paragraphs with a style of "CASnippet" become a PRE formatted section.
 * 
 * A paragraph with a style of "CAHeading1" becomes an H1 text run. This is for the title
 * line above all other text.
 * 
 * A paragraph with a style of "CAHeading2" becomes an H2 text run.
 * A paragraph with a style of "CAHeading3" becomes an H3 text run.
 * A paragraph with a style of "CAHeading4" becomes an H4 text run.
 * 
 * Styles CAHeading2 through CAHeading4 become the Table of Contents at the top of the page.
 * CAHeading2 is the first level. CAHeading3 is beneath that and so on. The Table of contents
 * is automatically generated and placed immediately before the first CAHeading2 paragraph.
 * 
 * Paragraphs with a style CACodeList make a table of code-file links to the right of the
 * table of contents. The table of links is generated along with the table of contents.
 * Each paragraph is a row in the table. Each paragraph has five tokens separated with
 * the "|" character as follows: * 
 *      title | url | raw | cpu | size | percent
 *      title is the name shown in the table (underline line)
 *      url is the name of the file on the website (this is the processed disassembly)
 *      raw is the name of the raw file on the website (this is the unprocessed disassembly)
 *      cpu is the name of the cpu used in the disassembly (use "none" for data)
 *      size is the size of the binary the disassembly was taken from
 *      percent is the percent complete of the disassembly
 * 
 * The document body text must be labeled "CABodyText". The code translates "italics" and "bold"
 * to HTML tags. HTML special characters in the text are converted to entities UNLESS the text
 * is flagged as "subscript". Text with "subscript" style are passed through as-is to the
 * final document. This is used for embedded HTML within the WORD document.
 */
public class DOCXToWeb {
	
	/**
	 * This static method reads the given Microsoft WORD document and generates
	 * an HTML document to the given output file (null for stdout).
	 * @param fname name of the input file
	 * @param out name of the output file (or null for stdout)
	 * @throws JDOMException if anything goes wrong
	 * @throws IOException if anything goes wrong
	 */
	public static void main(String fname, String out) throws IOException, JDOMException
	{
		ZIP z = new ZIP(fname);
		Element e = z.readXML("word/document.xml");
		Book book = new Book(e);
		
		PrintStream ps = System.out;
		if(out!=null) ps = new PrintStream(out);
		generateHTML(book,ps);
		ps.flush();
		if(out!=null) ps.close();
	}

	/**
	 * OS Command-line entry point.
	 * @param args command line arguments
	 * @throws Exception if anything goes wrong
	 */
	public static void main(String [] args) throws Exception
	{		
		main(args[0],null);
	}	
	
	public static void generateHTML(Book book, PrintStream ps)
	{
		boolean inSnippet = false;
		boolean madeTOC = false;
		
		for(Paragraph paragraph : book.content) {
						
			if(paragraph.style.equals("CASnippet")) {
				// If we have opened a <pre> then just continue
				if(inSnippet) {
					ps.println(paragraph.combined);
					continue;
				} 
				// Start a snippet section
				ps.println("<pre"+addId(paragraph.toc)+" class=\"CASnippet\">");
				inSnippet = true;
				ps.println(paragraph.combined);
				continue;				
			}
			
			// Not a CASnippet style ... end the snippet section
			if(inSnippet) {
				ps.println("</pre>");
				inSnippet = false;
			}						
			
			// If this is a heading wrap it in a heading tag
			if(paragraph.style.equals("CAHeading1")) {
				ps.println("<h1"+addId(paragraph.toc)+">"+paragraph.combined+"</h1>");				
				continue;
			} else if(paragraph.style.equals("CAHeading2")) {
				if(!madeTOC) {
					madeTOC = true;
					String toc = generateTOC(book);
					String col = generateCodeList(book);
					ps.println("<table><tr>");
					ps.println("<td style=\"vertical-align: top;\">"+toc+"</td>");
					ps.println("<td style=\"vertical-align: top;\">"+col+"</td>");
					ps.println("</tr></table>");					
				}
				ps.println("<h2"+addId(paragraph.toc)+">"+paragraph.combined+"</h2>");				
				continue;
			} else if(paragraph.style.equals("CAHeading3")) {
				ps.println("<h3"+addId(paragraph.toc)+">"+paragraph.combined+"</h3>");				
				continue;
			} else if(paragraph.style.equals("CAHeading4")) {
				ps.println("<h4"+addId(paragraph.toc)+">"+paragraph.combined+"</h4>");				
				continue;
			}
						
			// Regular paragraph
			if(paragraph.style.equals("CABodyText")) {
				ps.println("<p"+addId(paragraph.toc)+">");
				ps.println(paragraph.combined);
				ps.println("</p>");
				continue;
			}
			
			// TO DO do something special here. Spit out a file?
			if(paragraph.style.equals("CAtodo")) {
				ps.println("<p"+addId(paragraph.toc)+">");
				ps.println(paragraph.combined);
				ps.println("</p>");
				continue;
			}
						
			// Ignored TOC entry
			if(paragraph.style.equals("CATOCEntry") || paragraph.style.equals("CACodeList")) {
				continue;
			}
			
			// Unknown
			throw new RuntimeException("Unknown style '"+paragraph.style+"'");
		}	
	}
		
	/**
	 * This static method generates the table of code-file links at the top of the page. Each
	 * paragraph of type "CACodeList" becomes a row in the table. Each row must have five
	 * columns with text separated with "|".
	 * @param book the parsed WORD document
	 * @return the HTML table
	 */
	static String generateCodeList(Book book)
	{
		
		boolean containsCode = false;
		for(int x=0;x<book.content.size();++x) {
			Paragraph paragraph = book.content.get(x);	
			if(paragraph.style.startsWith("CACodeList")) {
				containsCode = true;
				break;
			}
		}
		
		if(!containsCode) return "";
		
		StringBuffer ret = new StringBuffer();
		ret.append("<table class=\"codeList\">\r\n");	
		ret.append("<tr><td>Code List</td></tr><tr><td></td></tr>\r\n");
		for(int x=0;x<book.content.size();++x) {
			Paragraph paragraph = book.content.get(x);	
			if(paragraph.style.startsWith("CACodeList")) {
				StringTokenizer st = new StringTokenizer(paragraph.combined,"|");
				String a = st.nextToken();
				String b = st.nextToken();
				String c = st.nextToken();
				String d = st.nextToken();
				String e = st.nextToken();
				String f = st.nextToken();
				ret.append(
						"<tr><td><a target=\"_blank\" href=\""+b+"\">"+a+"</a>"+
						"</td><td><a target=\"_blank\" href=\""+c+"\">[raw]</a>"+
						"</td><td>"+d+
						"</td><td>"+e+
						"</td><td>"+f+
						"</td><td></tr>");				
			}
		}		
		ret.append("</table>\r\n");
		return ret.toString();
	}
	
	/**
	 * This static method generates the table-of-contents at the top of the page.
	 * WORD paragraphs must be styled with "CATOCEntry1" through "CATOCEntry4".
	 * @param book the parsed WORD document
	 * @return the HTML table
	 */
	static String generateTOC(Book book)
	{
		StringBuffer ret = new StringBuffer();
		ret.append("<table class=\"toc\"><tr><td>Contents<br>\r\n");
		int [] toc = {0,0,0,0,0,0,0,0,0,0};
		int lastTOCLevel = -1;
		for(int x=0;x<book.content.size();++x) {
			Paragraph paragraph = book.content.get(x);			
			int newLevel = 0;
			String label = null;
			Paragraph tocPara = null;
						
			if(paragraph.style.startsWith("CAHeading")) {
				tocPara = paragraph;
				label = paragraph.combined;
				newLevel = paragraph.style.charAt(9)-'0';		
				lastTOCLevel = newLevel;
				if(newLevel==1) continue; // Skip Heading 1
			} else if(paragraph.style.equals("CATOCEntry")) {
				newLevel = lastTOCLevel;
				label = paragraph.combined;
				if(label.startsWith("+")) {
					label = label.substring(1);
					++newLevel;
				}
				tocPara = book.content.get(x+1);				
			}
			
			if(tocPara!=null) {
				int ofs = newLevel-2; // Base 0
				for(int y=0;y<=ofs;++y) {
					if(toc[y]==0) {						
						ret.append("<ul>\r\n"); // Opening a level
					}					
				}
				// Close up levels if we are backing up
				for(int y=ofs+1;y<toc.length;++y) {
					if(toc[y]>0) {
						ret.append("</ul>\r\n");
						toc[y]=0;
					}
				}
				// Add this to the current level
				++toc[ofs];				
				tocPara.toc = makeTOCString(toc);
				ret.append("<li>"+"<a href=\"#TOC-"+tocPara.toc+"\">"+
						tocPara.toc+" "+label+"</a>"+
						"</li>\r\n");
				tocPara.toc = "TOC-"+tocPara.toc;
			}
			
		}
		// Close up any levels left open
		for(int y=0;y<toc.length;++y) {
			if(toc[y]>0) {						
				ret.append("</ul>\r\n"); 
			}					
		}
		ret.append("</td></tr></table>\r\n");
		
		return ret.toString();
	}	
	
	/**
	 * This method builds a string of the form '1.2.3.4' with the
	 * given heading numbers. A '0' heading number stops the
	 * string.
	 * @param toc array of index numbers
	 * @return the string of the form '1.2.3.4'
	 */
	static String makeTOCString(int [] toc) 
	{
		String ret = "";
		for(int x=0;x<toc.length;++x) {
			if(toc[x]==0) break;
			ret = ret + toc[x]+".";
		}
		if(ret.endsWith(".")) {
			ret = ret.substring(0,ret.length()-1);
		}
		return ret;
	}
	
	/**
	 * A table-of-contents click takes you to a target point in the HTML. This
	 * method generates the "id='blah'" string for the target point.
	 * @param toc table-of-contents target point
	 * @return the target id string for the destination
	 */
	static String addId(String toc) {
		if(toc==null || toc.length()==0) return "";
		return " id=\""+toc+"\"";
	}
	
	/**
	 * This static method makes a given string HTML friendly by replacing special
	 * characters with entities.	
	 * @param str the string to clean
	 * @return the entized string
	 */
	public static String makeHTMLFriendly(String str) {		
		int pos = 0;
		while(true) {
			int i = str.indexOf('<',pos);
			if(i<0) break;
			String a = str.substring(0,i)+"&lt;"+str.substring(i+1);
			str = a;			
			pos = i+1;
		}
		return str;
	}	
	
}
