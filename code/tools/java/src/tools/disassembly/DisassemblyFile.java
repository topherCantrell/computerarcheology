package tools.disassembly;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

import tools.code.AddressSpec;
import tools.code.CodeLine;
import tools.file.BinaryFiles;
import tools.processor.Opcode;
import tools.processor.Processor;
import tools.processor.Processors;

/**
 * This class parses a commented disassembly file into code lines. Special comments
 * can be added to define menus and RAM/Code addresses. This class encapsulates
 * all of these.
 */
public class DisassemblyFile 
{
	
	// Information about the machine (from comments)
	private MachineInfo machineInfo = new MachineInfo();
	
	// The CodeLines themselves
	private List<CodeLine> lines = new ArrayList<CodeLine>();
	
	// The parsed comments
	private List<Menu> menus = new ArrayList<Menu>();	
	
	// Address specifications (code and manual)	
	private Map<String,AddressSpec> addresses = new HashMap<String,AddressSpec>();
			
	// The loaded binary data
	private BinaryFiles binaryFiles;
	
	// Other related banks of code
	private Map<String,DisassemblyFile> banks = new HashMap<String,DisassemblyFile>();
	
	// The filename
	private String filename;	
	
	private String rootPath;
	
	public DisassemblyFile(String rootPath,String filename) throws IOException
	{
		this(rootPath,filename,null,true);
	}	
	public DisassemblyFile(String rootPath, String filename, String binName) throws IOException
	{
		this(rootPath,filename,binName,true);
	}	
	public DisassemblyFile(String rootPath, String filename, String binName, boolean followBanks) throws IOException
	{
		this.filename = filename;
		this.rootPath = rootPath;
		
		// Read all the lines into a random-access list
		Reader r = new FileReader(this.rootPath+filename);
		BufferedReader br = new BufferedReader(r);
		int lineNumber = 0;
		while(true) {
			String g = br.readLine();
			if(g==null) break;
			++lineNumber;
			lines.add(new CodeLine(g,filename,lineNumber,true));
		}
		br.close();
		
		// Handle includes
		for(int y=0;y<lines.size();++y) {
			CodeLine c = lines.get(y);
			String comment = c.getSpecialCommentData();
			if(comment==null) continue;
			if(comment.startsWith("include ")) {
				List<CodeLine> sub = new ArrayList<CodeLine>();
				String fn = comment.substring(8).trim();
				r = new FileReader(rootPath+fn);
				br = new BufferedReader(r);
				lineNumber = 0;
				while(true) {
					String g = br.readLine();
					if(g==null) break;
					++lineNumber;
					sub.add(new CodeLine(g,fn,lineNumber));
				}
				lines.remove(y);
				lines.addAll(y,sub);
				--y;
			}
		}
		
		// Build the menu system. 
		// Gather manual addresses.
		// Gather the code addresses.
		// Gather CPU info.
		Menu currentMenu = null;
		for(int y=0;y<lines.size();++y) {
			CodeLine c = lines.get(y);
			String comment = c.getSpecialCommentData();
			if(comment==null) continue;
			
			//;##Menu numCols displayName          Start of a new group of menu items
			//;##MenuLink codeSpot displayName     Define a menu item
			//;##- comment after space             Ignored in the rendered output
			//;##codeSpot    A code-spot for menu-item reference                        
			//;##-codeSpot   A code-spot for menu-item reference and filled into other code lines
			
			if(comment.equals("-") ||              // Ignore special comments 
					comment.startsWith("- ") ||    // Ignore special comments
					comment.startsWith("--") ||    // ?
					comment.startsWith("!"))       // ?
			{
				continue;
			}
			
			// Code banks
			if(comment.startsWith("Bank ")) {
				if(followBanks) {
					StringTokenizer st = new StringTokenizer(comment.substring(5)," ");
					String bankName = st.nextToken();
					String bankFile = st.nextToken();
					banks.put(bankName, new DisassemblyFile(rootPath,bankFile,null,false));
				}
				continue;
			}
			
			// Menu system
			if(comment.startsWith("Menu ")) {
				currentMenu = new Menu();
				menus.add(currentMenu);
				comment = comment.substring(5).trim();
				int i = comment.indexOf(" ");
				currentMenu.numColumns = Integer.parseInt(comment.substring(0,i));
				comment = comment.substring(i).trim();
				if(comment.startsWith("\"")) comment=comment.substring(1);
				if(comment.endsWith("\"")) comment=comment.substring(0,comment.length()-1);
				currentMenu.displayName = comment;
				continue;
			}
			if(comment.startsWith("MenuLink ")) {
				comment = comment.substring(9).trim();
				int i = comment.indexOf(" ");
				currentMenu.links.add(comment.substring(0,i));
				comment = comment.substring(i).trim();
				if(comment.startsWith("\"")) comment=comment.substring(1);
				if(comment.endsWith("\"")) comment=comment.substring(0,comment.length()-1);
				currentMenu.displayNames.add(comment);
				continue;
			}
			
			// CPU info
			if(comment.startsWith("$")) {
				comment = comment.substring(1).trim();
				machineInfo.parseInfo(comment);
				continue;
			}	
			
			// Manual addresses
			if(comment.startsWith("*") || comment.startsWith("+")) {				
				AddressSpec spec = new AddressSpec();
				spec.manual = true;
				if(comment.startsWith("*")) spec.isPort = true;
				spec.parseDisassembly(comment.substring(1));
				if(spec.readLabel!=null) addresses.put(spec.readLabel, spec);
				if(spec.writeLabel!=null) addresses.put(spec.writeLabel, spec);
				continue;
			}			
						
			// Must be "##Spot" or "##-Spot". 
			// The "##Spot" becomes a menu link destination.
			// The "##-Spot" becomes a menu link dest AND an address spec.
			
			// Ignore the link destinations that are NOT address specs.
			if(!comment.startsWith("-")) continue;
			
			// Ignore anything beyond the name
			int i = comment.indexOf(" ");
			if(i>0) {
				comment = comment.substring(1,i);
			}
			
			AddressSpec spec = new AddressSpec();
			spec.readLabel = comment.substring(1);
			spec.writeLabel = spec.readLabel;			
			for(int z=y+1;z<lines.size();++z) {
				CodeLine d = lines.get(z);
				if(d.getAddress()>-1) {				
					spec.address = d.getAddress();
					break;
				}					
			}		
			addresses.put(spec.readLabel,spec);
			
		}
		
		// Attach the binary file information, but we won't check for data matching. We might
		// be doing a "patch" in which case we expect differences.
		if(binName==null) {
			binName = machineInfo.getOriginalBinary();
		}		
		if(binName!=null) {
			binaryFiles = new BinaryFiles(binName,rootPath);			
		}

		// Find the correct opcode for lines that are code
		if(!machineInfo.getCpuType().equals("none")) {
			Processor processor = Processors.getInstance().getProcessor(machineInfo.getCpuType());
			for(CodeLine c : lines) {				
				
				if(c.getOpcodeString()==null) continue; // Just a comment or blank line. Ignore it.
				
				int [] dataList = c.getData();
				if(dataList==null) {
					throw new RuntimeException("No data bytes for line. File "+c.getFilename()+" "+c.getLineNumber());					
				}
				
				int address = c.getAddress();
				if(address<0) {
					throw new RuntimeException("No address on line. File "+c.getFilename()+" "+c.getLineNumber());
				}
								
				if(c.getOpcodeString()==null || c.getOpcodeString().length()==0) continue;
								
				List<Opcode> ops = processor.findPossibleOpcodes(dataList, 0, dataList.length);
				if(ops.size()!=1) {
					throw new RuntimeException("Could not find an opcode for the given data. File "+c.getFilename()+" "+c.getLineNumber());
				}			
				c.setOpcode(ops.get(0));
			}
		}
				
	}
	
	public String getFilename() {
		return filename;
	}
	
	public DisassemblyFile getBank(String name) {
		return banks.get(name);
	}
			
	public BinaryFiles getBinaryFiles() {
		return binaryFiles;
	}

	public MachineInfo getMachineInfo() {
		return machineInfo;
	}	
		
	public List<CodeLine> getLines() {
		return lines;
	}

	public List<Menu> getMenus() {
		return menus;
	}

	public Map<String,AddressSpec> getAddresses() {
		return addresses;
	}

	public AddressSpec findCodeAddress(String bus,int val, boolean port, boolean manual) 
	{		
		
		for(AddressSpec spec : addresses.values()) {
			if(spec.isPort!=port) continue;  
			if(spec.manual!=manual) continue; 
			if(spec.address != val) continue;
			
			// Unknown bus direction ... take first spec match
			if(bus==null) return spec;
			
			// Make sure read/write match
			if(bus.equals("r") && spec.readLabel!=null) return spec;
			if(bus.equals("w") && spec.writeLabel!=null) return spec;
			
		}
		
		// No matches
		return null;		
	}
			
}
