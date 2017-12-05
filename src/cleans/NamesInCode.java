package cleans;

import java.io.IOException;
import java.io.PrintStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import bus.AddressAccess;
import bus.BusType;
import code.CodeLine;
import cpu.CPU;
import cpu.Opcode;
import util.CU;
import web.AddressMap;
import web.AddressTableEntry;
import web.LineOfMarkup;
import web.MarkupException;
import web.MarkupToHTML;

/**
 * This class (and tool) manages the "{...}" link specifications in the code comments.
 * 
 */
public class NamesInCode {
	
	static final int COMMENTCOL = 45+4;
	
	static List<LineOfMarkup> lines; 
	static List<ExternalMemoryMap> memoryMaps;
	static Map<Integer,LineOfMarkup> labelValues;
	
	static Map<String,String> variables = new HashMap<String,String>();
			
	static class ExternalMemoryMap {
		String name;
		String markupFile;
		String htmlFile;
		AddressMap map;
	}
	
	static LineOfMarkup findCodeAtAddress(int address) {
		for(LineOfMarkup mark : lines) {			
			CodeLine code = mark.codeLine;
			if(code!=null) {				
				if(code.address == address) {
					return mark;
				}
			}						
		}		
		return null;
	}
	
	static boolean isCodeLine(int pos) {
		if(pos>=lines.size()) return false;
		if(lines.get(pos).lineNumber<0) return false; // We never insert code;
		String lineTrim = lines.get(pos).line.trim();
		if(lineTrim.startsWith(";")) return true; // Code comment is code
		if(lineTrim.length()>4 && CU.isNumeric(lineTrim.substring(0, 4), 16)  && lineTrim.charAt(4)==':') {
			return true;
		}
		if(lineTrim.isEmpty()) {				
			// Blank line could be code if next line is
			// DANGEROUS RECURSION HERE			
			boolean is = isCodeLine(pos+1);
			return is;
		}
		// It could be a label
		int i = lineTrim.indexOf(":");
		if(i<0) return false; // Must have a colon
		int j = lineTrim.indexOf(" ");
		if(j>=0 && j<i) return false; // No spaces in labels		
		// It is only a label if the next line is code
		// DANGEROUS RECURSION HERE
		boolean is = isCodeLine(pos+1);
		return is;
	}
	
	/**
	 * This tool fixes the links in the target file IN PLACE overwriting the
	 * existing file. Be sure to check-in to GIT before running this tool so
	 * you have a way to back out the changes.
	 * @param args
	 * @throws Exception
	 */
	public static void main(String [] args) throws Exception {
		
		// For running within dev
		//String [] targs = {"content/arcade/frogger/Code.mark"};
		//String [] targs = {"content/coco/daggorath/Code.mark"};
		String [] targs = {"content/atari2600/combat/Code.mark"};
		args = targs;
		
		try (PrintStream ps = new PrintStream("NamesInCode.txt")) {
		
			// Load the lines of markup
			List<String> ls = Files.readAllLines(Paths.get(args[0]));
			lines = LineOfMarkup.convert(ls, args[0]);
			MarkupToHTML.expandIncludes(lines,args[0]);
			
			// For code that references external memory map tables
			memoryMaps = new ArrayList<ExternalMemoryMap>();
			labelValues = new HashMap<Integer,LineOfMarkup>();
			
			int x = 0;
			boolean isCodeBlock = false;
			
			while(x<lines.size()) {
				
				// Other types of blocks can't be code blocks			
				if(lines.get(x).lineTrim.startsWith("{{{")) {
					while(!lines.get(x).lineTrim.startsWith("}}}")) {
						++x;
					}
					continue; // Back around
				}
										
				boolean ic = isCodeLine(x);
				if(ic) {				
					lines.get(x).codeLine = new CodeLine(lines.get(x).line);
					if(!isCodeBlock) {						
						isCodeBlock = true;							
					}				
				} else {
					if(isCodeBlock) {
						isCodeBlock = false;				
					}							
				}			
				++x;
			}
			
			// Work backwards to give all code labels an address		
			int address = Integer.MAX_VALUE;
			for(x=lines.size()-1;x>=0;--x) {
				LineOfMarkup mark = lines.get(x);
				CodeLine code = mark.codeLine;
				if(code!=null) {
					if(code.address>=0) {
						address = code.address;					
					}
					if(code.label!=null) {
						code.address = address;
						labelValues.put(address, mark);
					}
				}
			}
			
			for(LineOfMarkup mark : lines) {
				
				String lineTrim = mark.lineTrim;			
				
				// Set a variable's value
				if(lineTrim.startsWith("%%")) {	
					ps.println(mark.line);
					int i = lineTrim.indexOf("=");
					if(i<0) {
						throw new MarkupException("Expected '=' in '"+lineTrim+"'");
					}
					String key = lineTrim.substring(2,i).trim();
					String value = lineTrim.substring(i+1).trim();
					if(key.startsWith("-")) {			
						ExternalMemoryMap ne = new ExternalMemoryMap();
						ne.name = key;
						i = value.indexOf(" ");
						ne.markupFile = value.substring(0, i).trim();
						ne.htmlFile = value.substring(i+1).trim();		
						List<String> mapEntries;
						try {
							mapEntries = Files.readAllLines(Paths.get("content",ne.markupFile));
						} catch(IOException e) {
							throw new MarkupException("Could not load address table "+ne.markupFile);
						}
						ne.map = new AddressMap();
						ne.map.parseMaps(mapEntries);
						memoryMaps.add(ne);					
					} else {
						variables.put(key,value );
					}	
					continue;
				}
				
				if(mark.codeLine!=null) {
					ps.println(fixCode(mark.codeLine));
					continue;
				}			
				
				ps.println(mark.line);
				
			}
			
			ps.flush();
		}
		
				
	}

	private static String fixCode(CodeLine code) {		
		
		// Strip off any {...}
		String o = code.originalText;
		int i = o.indexOf(";");
		if(i>=0) {
			int j = o.indexOf("{",i);
			if(j>0) {
				int k = o.indexOf("}",j);
				if(o.charAt(j-1)==' ') --j;
				code.originalText = o.substring(0, j)+o.substring(k+1);				
			}
		}
				
		if(code.opcode==null) {			
			return code.originalText; // No opcode ... just data
		}
		
		CPU cpu = CPU.getCPU(variables.get("cpu"));
		if(cpu==null) {
			return code.originalText; // No CPU ... nothing to do
		}
		
		// Separate the code text into left (before comment) and right. We
		// don't do fill-ins in the comment.
		String leftPart = code.originalText;
		String rightPart = "";
		i = leftPart.indexOf(";");
		if(i>=0) {
			rightPart = leftPart.substring(i);
			leftPart = leftPart.substring(0, i);
		}
		
		boolean accessOverride = rightPart.contains("@@");
		
		i = leftPart.indexOf("$"); // Numerics are always hex
		if(i<0) {
			return code.originalText; // Nothing to fill in
		}
		
		int j = i+1;
		while(true) {
			char c = leftPart.charAt(j);
			if (!((c>='0' && c<='9') || (c>='A' && c<='F') || c=='-')) break;
			++j;
			if(j==leftPart.length()) break;
		}
		
		int num = Integer.parseInt(leftPart.substring(i+1, j),16);
				
		String dps = variables.get("directPage");
		int dp = 0;
		if(dps!=null) dp = Integer.parseInt(dps,16);	
		
		// The opcode itself has much better information about what this access is
		// But for now we'll ask based on text (the code.opcode is text)
		Opcode op = cpu.matchDisassembly(code);
				
		AddressAccess a = cpu.getAccess(op, num, dp, accessOverride); 
		if(a==null) {
			return code.originalText; // This number isn't a memory reference
		}
		
		// i = start of numeric sub
		// numlen = length of numeric sub
		// a = access information		
						
		ExternalMemoryMap emm = null;
		AddressTableEntry e = null;
		for(ExternalMemoryMap map : memoryMaps) {			
			e = map.map.findEntryForAccess(num+dp, a.busDir, a.busType); 
			if(e != null) {
				emm = map;
				break;
			}			
		}
		
		String name = null;   // the symbolic name of the number
				
		if(e!=null) {
			// We found a memory map
			name = e.name;
			if(name.isEmpty()) {
				name = CU.hex4(e.start);
			}						
		} else {	
			// It might be in the code ... but only on the main bus
			if(a.busType==BusType.MAIN) {				
				LineOfMarkup lab = labelValues.get(num);
				if(lab!=null) {
					// We found a code label
					name = lab.codeLine.label;									
				}				
			} 
		}		
		
		if(name==null) {
			return code.originalText;
		}
		
		i = code.originalText.indexOf(";");
		if(i<0) {
			code.originalText = CU.padTo(code.originalText, COMMENTCOL) + ";";
			i = code.originalText.indexOf(";");
		}
		
		if(e!=null) {
			name = emm.name+"_"+name;
		}
		
		code.originalText = code.originalText.substring(0, i+1)+" {"+name+"}"+code.originalText.substring(i+1);
				
		return code.originalText;
	}

}
