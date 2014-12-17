package tools.file;

import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

import org.jdom.Document;
import org.jdom.Element;
import org.jdom.JDOMException;
import org.jdom.input.SAXBuilder;

public class ZIP {
	
	private String filename;
	
	public ZIP(String filename) {
		this.filename = filename;
	}
	
	public InputStream openStream(String name) throws IOException 
	{		
		FileInputStream fis = new FileInputStream(filename);
		ZipInputStream zin = new ZipInputStream(new BufferedInputStream(fis));
		
		while(true) {
			ZipEntry ze = zin.getNextEntry();
			if(ze==null) break;
			if(ze.getName().equals(name)) {
				return zin;
			}
		}
		
		return null;	
	}
	
	public Element readXML(String name) throws IOException, JDOMException
	{		
		InputStream is = openStream(name);		
		SAXBuilder builder = new SAXBuilder();
		Document doc = builder.build(is);		
		return doc.getRootElement();		
	}	
	
}
