package tools.processor;

import java.io.IOException;
import java.io.InputStream;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.jdom.Document;
import org.jdom.Element;
import org.jdom.JDOMException;
import org.jdom.input.SAXBuilder;

/**
 * This singleton class parses the Processors.xml file. It maintains a cache of loaded processor families.
 *  Usually an application will only load one processor family.
 */
public class Processors 
{
	// Singleton pattern
	protected static Processors singleton;
	
	// The information from the "Processors.xml" file. Maps processor names to family-files.
	private Map<String,String> knownProcessors = new HashMap<String,String>();
	
	// Loaded processor families
	private Map<String,ProcessorFamily> cachedFamilies = new HashMap<String,ProcessorFamily>();
	
	/**
	 * This static method returns the singleton Processors instance.
	 * @return the Processors singleton
	 */
	public static Processors getInstance()
	{
		if(singleton==null) {
			try {
				singleton = new Processors();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		return singleton;
	}
		
	protected Processors() throws JDOMException, IOException
	{
		SAXBuilder builder = new SAXBuilder(false);		
		InputStream is = getClass().getResourceAsStream("/tools/processor/Processors.xml");
		Document d = builder.build(is);
		Element root = d.getRootElement();
		
		@SuppressWarnings("unchecked")
		List<Element> pis = root.getChildren("processor");
		for(Element pi : pis) {
			knownProcessors.put(pi.getAttributeValue("name"),pi.getAttributeValue("family"));
		}				
	}
	
	/**
	 * This method returns the Processor info for a given CPU type.
	 * @param name the name of the CPU
	 * @return the Processor info or null if not found	
	 */	
	public Processor getProcessor(String name)
	{
		
		// Check the cache ... these are rather bulky so we'll cache them
		ProcessorFamily fam = cachedFamilies.get(name);
				
		if(fam==null) {
			// Not in the cache ... get the name of the file
			String familyName = knownProcessors.get(name);			
			if(familyName==null) {
				// No family by that name
				throw new RuntimeException("Unknown processor family for processor '"+name+"'");
			}
			// Load the family from the given file
			fam = new ProcessorFamily(familyName);
		}		
		
		// Get the specific processor
		Processor p = fam.getProcessors().get(name);
		if(p==null) throw new RuntimeException("Unknown processor family for processor '"+name+"'");
		
		return p;				
		
	}	
	
	// TEST STUB
	public static void main(String [] args) throws Exception
	{
		Processors p = Processors.getInstance();
		Processor pr = p.getProcessor("6502");
		System.out.println(pr);
	}
		
}
