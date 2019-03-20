package tools.processor;

import java.io.InputStream;
import java.lang.reflect.Constructor;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.jdom.Document;
import org.jdom.Element;
import org.jdom.input.SAXBuilder;

/**
 * Processors often come in related families. For instance, the Z80 is the big-brother
 * of the 8080. The Z80 has all of the 8080's opcodes plus a few others. In fact, the
 * 8080 opcodes can use the Z80 mnemonics, which are clearer in my opinion. The XML
 * file groups processors by family, and this class maintains a grouping of related
 * Processor objects. 
 */
public class ProcessorFamily {
	
	private String familyName;
	
	private Map<String,PrintSpacing> printSpacing = new HashMap<String,PrintSpacing>();
	
	private Map<String,Processor> processors = new HashMap<String,Processor>();
	
	private List<ProcessorBlendEntry> blendEntries = new ArrayList<ProcessorBlendEntry>();
	private String blendJump;
	
	private boolean littleEndian=true;
	
	/**
	 * This function creates a new Processor object by parsing the corresponding XML.
	 * @param familyFileName name of the family's XML file 
	 */
	public ProcessorFamily(String familyFileName) 
	{
		try {
			
			SAXBuilder builder = new SAXBuilder(false);		
			InputStream is = getClass().getResourceAsStream("/tools/processor/"+familyFileName);
			Document d = builder.build(is);
			Element pi = d.getRootElement();

			familyName = pi.getAttributeValue("name");
			String s = pi.getAttributeValue("littleEndian");
			if(s!=null && s.equals("big")) littleEndian=false;
			
			@SuppressWarnings("unchecked")
			List<Element> fSpace = pi.getChild("printSpacing").getChildren();
			for(Element fs : fSpace) {
				PrintSpacing psp = new PrintSpacing();
				psp.dataFieldSize = Integer.parseInt(fs.getAttributeValue("dataFieldSize"));
				psp.mnemonicFieldSize = Integer.parseInt(fs.getAttributeValue("mnemonicFieldSize"));
				printSpacing.put(fs.getAttributeValue("name"), psp);
			}

			@SuppressWarnings("unchecked")
			List<Element> procInfos = pi.getChild("processors").getChildren();
			for(Element pri : procInfos) {
				String name = pri.getAttributeValue("name");
				try {
					String className = pri.getAttributeValue("class");
					if(className==null) className="tools.processor.Processor";
					else className = "tools.processor."+className;
					Class<?> c = this.getClass().getClassLoader().loadClass(className);					
					Constructor<?> con = c.getConstructor(ProcessorFamily.class,Element.class,Element.class);
					Processor pro = (Processor) con.newInstance(this,pri,pi);
					processors.put(name,pro);
				} catch (Exception e) {					
					throw new RuntimeException("Error loading Processor"+name+" class: ",e);
				}			
			}
			
			// Collect the blend-tool's information
			Element blendInfo = pi.getChild("blends");
			if(blendInfo!=null) {
				blendJump = blendInfo.getAttributeValue("jump");
				@SuppressWarnings("unchecked")
				List<Element> blendInfos = blendInfo.getChildren();
				for(Element e : blendInfos) {
					ProcessorBlendEntry be = new ProcessorBlendEntry();
					be.left = e.getAttributeValue("left");
					be.op = e.getAttributeValue("op");
					be.right = e.getAttributeValue("right");
					be.branchPass = e.getAttributeValue("branchPass");
					be.branchFail = e.getAttributeValue("branchFail");					
					blendEntries.add(be);
				}				
			}
			

		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}

	public String getFamilyName() {	return familyName; }
	public Map<String, PrintSpacing> getPrintSpacing() { return printSpacing; }
	public Map<String, Processor> getProcessors() {	return processors;	}
	public boolean isLittleEndian() { return littleEndian; }
	public List<ProcessorBlendEntry> getBlendEntries() {return blendEntries;}
	public String getBlendJump() {return blendJump;}
	
}
