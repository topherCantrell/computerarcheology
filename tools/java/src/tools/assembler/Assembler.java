package tools.assembler;

import java.io.BufferedReader;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.StringTokenizer;

import tools.blend.Blender;
import tools.code.AddressSpec;
import tools.code.CU;
import tools.code.CodeLine;
import tools.code.OpcodeParameterInfo;
import tools.processor.Opcode;
import tools.processor.OpcodeParamField;
import tools.processor.Processor;
import tools.processor.ProcessorFamily;
import tools.processor.Processors;


/**
 * This application reads a text file (with includes) into a list of CodeLines
 * and assembles the code lines to give them data and addresses. Many of the
 * assembly steps are static methods that can be reused in other contexts.
 */
public class Assembler 
{	
	
	/**
	 * This tool assembles a text file into a binary file and produces an optional
	 * listing file.
	 * 
	 * Command line arguments: inputFileName outputFileName [-list]
	 * 
	 * Files may be included (recursively) in the input file with the following syntax:
	 * 
	 * include myFile.asm
	 * 
	 * The exact syntax of the individual mnemonics depends on the target CPU's
	 * mnemonic set. But there is some common structure for all assembly files:
	 * 
	 * The colon ':' is reserved to mark the end of a label. A line may have have only
	 * one label. Labels collapse down to the first line of generated data.
	 * 
	 * Origins are labels that happen to be numeric.
	 * 
	 * All numeric constants may have an optional base specification. The default base
	 * is decimal. Examples of numbers: "0xFF00" and "123" and "0b00_11_11_00". Note 
	 * that '_' are ignored in numeric constants but may be used to separate fields.
	 * 
	 * Values may be defined with a "define" directive:
	 *   define key = value
	 * 
	 * Memory address outside the code area may be defined with an "address" directive.
	 * Memory addresses can be assigned automatically in increasing order using a "*".
	 *   address mySpot = 0xF000 byte     ; mySpot points to a byte at F000
	 *   address myOtherSpot = * word     ; myOtherSpot points to F001 
	 *   address baseSpot = >0x80 byte    ; The ">" means an 8-bit address (base/zero page)
	 *   address bs2 = *                  ; bs2 points to 81 and is a byte
	 * 
	 * The program must define 'CPU' before the first opcode. Like:
	 * define CPU = 8080
	 * or
	 * define CPU = 8080 as Z80,Cish
	 * The "as" clause narrows the mnemonics to just the list given. If "as" is not given then
	 * the instruction set is the processor and the "Cish" set.
	 *
	 * 
	 * 
	 * A line beginning with '#' is parsed as data. For example:
	 * # 1,2,3,(WORD)4,5,(BYTE)6,20,PF0,"This is a test",0
	 * Once WORD or BYTE is given on a line the following data is the same size
	 * unless overridden. 
	 * 
	 * @param args the command line arguments
	 * @throws Exception if anything goes wrong
	 */
	public static void main(String [] args) throws Exception
	{
		
		// Command line arguments:
		// input output [-list]
		
		// Read the input text
		List<CodeLine> codeLines = readAssemblyText(args[0]);
		for(CodeLine e : codeLines) {
			if(e.getError()!=null) {
				System.err.println(e.getErrorDescription());
				System.exit(-1);
				return; // But never getting here
			}
		}
		
		// Find all the defines (constants) and addresses (outside the code)
		Map<String,AddressSpec> addresses = new HashMap<String,AddressSpec>();
		Map<String,String> defines = new HashMap<String,String>();		
		CodeLine err = Assembler.getDefinesAndAddresses(codeLines, defines, addresses);
		if(err!=null) {
			System.err.println(err.getErrorDescription());
			System.exit(-1);
			return; // But never getting here
		}
		
		// We just want the family. There may be specifics in the CPU define.
		String procName = defines.get("CPU");
		if(procName==null) {
			System.err.println("No CPU defined");
			System.exit(-1);
			return;
		}
		int j = procName.indexOf(" ");
		if(j>=0) {
			procName = procName.substring(0,j);
		}
		ProcessorFamily procFam = Processors.getInstance().getProcessor(procName).getFamily();
						
		// 3rd generation flow constructs (if/else/do/while)
		err = Blender.blend(codeLines,procFam);
		if(err!=null) {
			System.err.println(err.getErrorDescription());
			System.exit(-1);
			return; // But never getting here
		}
						
		// Assemble the lines		
		Set<String> usedBlendLabels = new HashSet<String>();
		err = assemble(codeLines,defines,addresses,usedBlendLabels);
		if(err!=null) {
			System.err.println(err.getErrorDescription());
			System.exit(-1);
			return;
		}
		
		int start=0xFFFF;
		int end=0;
		for(CodeLine c: codeLines) {
			if(c.getOpcodeString()==null) continue;
			if(c.getAddress()!=-1) {
				if(c.getAddress()<start) start=c.getAddress();
				if((c.getAddress()+c.getData().length-1)>end) {
					end=c.getAddress()+c.getData().length-1;				
				}
			}
		}
				
		int [] data = extractBinary(codeLines,start,end);
		if(data==null) {
			for(CodeLine c : codeLines) {
				if(c.getError()!=null) {
					System.err.println(c.getErrorDescription());
					System.exit(-1);
					return;
				}
			}
		}	
		
		int fillValue = 0;
		String fills = defines.get("_FILL");
		if(fills!=null) {
			fillValue = CU.parseIntValue(fills.trim());
		}
		
		FileOutputStream fos = new FileOutputStream(args[1]);
		for(int i : data) {
			if(i==-1) i=fillValue;
			fos.write(i);
		}
		fos.flush();
		fos.close();					
		
		if(args[args.length-1].equals("-list")) {
			fos = new FileOutputStream(args[1]+".list");
			PrintStream ps = new PrintStream(fos);
			printListing(ps,codeLines,defines,addresses,usedBlendLabels);
			ps.flush();
			ps.close();
		}
				
	}

	
	/**
	 * This method collects free labels and origins. Labels can (usually) be
	 * given on lines by themselves. Multiple labels can be given for a single line
	 * of code. This function pulls all the "free" labels (and origins) down to the
	 * next line of code that has an opcode. Any labels on the end of the code are
	 * collected together but left dangling.
	 * @param codeLines the list of lines
	 * @return the error line or null if OK
	 */
	static CodeLine collectFreeLabels(List<CodeLine> codeLines) {
		
		for(int x=0;x<codeLines.size()-1;++x) {
			CodeLine b = codeLines.get(x);
			// If this line has an opcode then leave its labels on it
			if(b.getOpcodeString()!=null && b.getOpcodeString().length()>0) {
				continue;
			}
						
			CodeLine c = codeLines.get(x+1);
			
			// Move the labels down to the next line
			c.getLabels().addAll(b.getLabels());
			b.getLabels().clear();
			
			// Move origin too
			if(b.getAddress()>=0) {
				if(c.getAddress()>=0 && c.getAddress()!=b.getAddress()) {
					b.setError("Trying to assign origin of '"+CU.fourDigitHex(b.getAddress())+
							"' but line already has origin of '"+CU.fourDigitHex(c.getAddress())+
							"'");
					return b;
				}
				c.setAddress(b.getAddress());
			}
			
		}
				
		return null;		
	}
	
	/**	
	 * Get all the "define" and "address" directives.
	 * @param codeLines list of code lines to process
	 * @param defines map of defines to fill out
	 * @return error line or null if OK
	 */
	static CodeLine getDefinesAndAddresses(List<CodeLine> codeLines, Map<String,String> defines, 
			Map<String,AddressSpec> addresses)
	{
		
		
		int nextAutoAddress = 0;
		boolean nextAutoAddressBase = false;
		int nextAutoAddressSize = 1;
		
		for(CodeLine c : codeLines) {			
			String s = c.getOpcodeString();
			if(s==null) continue;
			
			if(s.startsWith("define ")) {
				s = s.substring(7).trim();
				int i = s.indexOf("=");
				if(i<0) {
					c.setError("Expected an '='");
					return c;
				}
				String key = s.substring(0,i).trim();
				String value = s.substring(i+1).trim();
				if(key.length()==0 || value.length()==0) {
					c.setError("Invalid define (must be key=value)");
					return c;
				}
				String v2 = defines.get(key);
				if(v2!=null && !v2.equals(value)) {
					c.setError("Define '"+key+"' already has a value of '"+v2+"'");
					return c;
				}
				if(addresses.get(key)!=null) {
					c.setError("Symbol '"+key+"' already defined as an address");
					return c;
				}
				defines.put(key, value);
				c.setDirective(true);
			} else if(s.startsWith("address ")) {
				s = s.substring(8).trim();
				
				if(s.endsWith("byte")) {
					nextAutoAddressSize = 1;
					s=s.substring(0,s.length()-4).trim();
				}
				if(s.endsWith("word")) {
					nextAutoAddressSize = 2;
					s=s.substring(0,s.length()-4).trim();
				}
				int i = s.indexOf("#");
				if(i>=0) {
					nextAutoAddressSize = Integer.parseInt(s.substring(i+1));
					s=s.substring(0,i-1).trim();					
				}
				
				i = s.indexOf("=");
				if(i<0) {
					c.setError("Expected an '='");
					return c;
				}
				
				String key = s.substring(0,i).trim();
				s = s.substring(i+1).trim();
								
				if(!s.equals("*")) {
					if(s.startsWith(">")) {
						nextAutoAddressBase = true;
						s=s.substring(1).trim();
					}
					nextAutoAddress = CU.parseIntValue(s);					
				}
								
				AddressSpec spec = new AddressSpec();
				spec.address = nextAutoAddress;
				spec.eightBitAddress = nextAutoAddressBase;
				spec.readLabel = key;
				spec.writeLabel = key;
				spec.manual = true;
				spec.size = nextAutoAddressSize;
				
				if(defines.get(key)!=null) {
					c.setError("Address '"+key+"' already has a value as a 'define'");
					return c;
				}
				if(addresses.get(key)!=null) {
					c.setError("Address '"+key+"' is multiply defined");
					return c;
				}
				addresses.put(spec.readLabel, spec);
				
				nextAutoAddress = nextAutoAddress + nextAutoAddressSize;
				
				c.setDirective(true);
			}
		}			
		
		return null;
	}
		
	/**
	 * This function performs the assembly of the given code lines. Each
	 * line is filled out with an address and data.
	 * @param codeLines the list of lines
	 * @return any error or null if OK
	 */
	public static CodeLine assemble(List<CodeLine> codeLines, Map<String,String> defines, Map<String, AddressSpec> addresses, Set<String> usedBlendLabels)
	{
		
		// Find the processor		
		String cpu = defines.get("CPU");
		if(cpu==null) {
			CodeLine c = codeLines.get(0);
			c.setError("Missing 'CPU = ??' define");
			return c;
		}
		
		// There may be labels (and origins) on lines by themselves. There
		// may be many labels (on separate lines) for the same code. This
		// function pulls all the labels (and origin) for a line together.
		CodeLine err = collectFreeLabels(codeLines);
		if(err!=null) return err;	
		
		// May have specified a list of mnemonic sets to use (default is current+Cish)
		List<String> as = new ArrayList<String>();
		int i = cpu.toUpperCase().indexOf(" AS ");
		if(i>=0) {
			String t = cpu.substring(i+4).trim();
			cpu = cpu.substring(0,i);
			StringTokenizer st = new StringTokenizer(t,",");
			while(st.hasMoreTokens()) {
				as.add(st.nextToken().trim());
			}			
		}		
		
		// Get the target processor, which defines the list of available opcodes
		Processor processor = Processors.getInstance().getProcessor(cpu);
		if(processor==null) {
			CodeLine c = codeLines.get(0);
			c.setError("Unknown CPU '"+cpu+"'");
			return c;
		}
		
		// If there is no list of mnemonics use the target processor plus Cish
		if(as.size()==0) {
			as.add(processor.getName());
			as.add("Cish");
		}
				
		// Look for "#" tokens and scan data specifications
		for(CodeLine c : codeLines) {	
			if(c.getOpcodeString()==null) continue;
			if(c.getOpcodeString().startsWith("#")) {				
				parseData(c);
				if(c.getError()!=null) return c;
			}			
		}
				
		// First pass ... figure out the opcodes
		for(CodeLine c : codeLines) {		
			if(c.getOpcode()!=null) continue; // Could be data or other
			if(c.isDirective()) continue;
			if(c.getOpcodeString()==null) continue;
			
			// Here is the magic: convert the human-typed line of text to an opcode lining up
			// all the fill-in info.
			Opcode op = processor.findOpcode(c.getOpcodeString(),c.getOpcodeParamInfo(),as);
			if(op==null) {
				c.setError("Unknown mnemonic '"+c.getOpcodeString()+"'");
				return c;
			}		
			c.setOpcode(op);
			
		}
		
		// We know the opcodes ... now we can give each line an origin
		int lastAddress = -1;
		for(CodeLine c : codeLines) {
			if(c.getOpcodeString()==null) continue;
			if(c.isDirective()) continue;
			if(c.getAddress()>=0) {
				lastAddress = c.getAddress();
			} else {
				c.setAddress(lastAddress);
			}			
			if(lastAddress>=0) {
				lastAddress = lastAddress + c.getOpcode().getOpcodeSize();
			}			
		}
		
		// Build a map of all code labels and their addresses
		for(CodeLine c : codeLines) {
			for(String s : c.getLabels()) {		
				if(defines.get(s)!=null) {
					c.setError("Label '"+s+"' already has a value from a 'define'");
					return c;
				}
				if(addresses.get(s)!=null) {
					c.setError("Label '"+s+"' is multiply defined.");
					return c;
				}
				if(c.getAddress()==-1) {
					c.setError("Label '"+s+"' has no definition.");
					return c;
				}
				AddressSpec spec = new AddressSpec();
				spec.readLabel = s;
				spec.writeLabel = s;
				spec.address = c.getAddress();		
				// Size and 8-bit don't apply to code labels				
				addresses.put(spec.readLabel, spec);				
			}
		}
		
		// Second pass ... fill in the opcode data
		for(CodeLine c : codeLines) {
			if(c.getOpcodeString()==null) continue;
			if(c.isDirective()) continue;
			int address=c.getAddress();
			Map<String,OpcodeParameterInfo> dataMap = c.getOpcodeParamInfo();
			Opcode op = c.getOpcode();
			String t = op.getCode();
			int [] data = new int[op.getOpcodeSize()];
			c.setData(data);
			
			if(op instanceof DataOpcode) {
				
				// Data lines are converted to bytes here
				
				DataOpcode dop = (DataOpcode)op;
				int dcur = 0;
				
				for(int x=0;x<dop.values.size();++x) {
					
					int dsize = dop.sizes.get(x);
					String dvalue = dop.values.get(x);
					
					if(dsize==1) {
						data[dcur++] = decodeDataByte(c,address,'b','b',dvalue,addresses,defines,usedBlendLabels);
						if(c.getError()!=null) return c;
					} else if(dsize==2) {
						if(processor.getFamily().isLittleEndian()) {
							data[dcur++] = decodeDataByte(c,address,'w','l',dvalue,addresses,defines,usedBlendLabels);
							if(c.getError()!=null) return c;
							data[dcur++] = decodeDataByte(c,address,'w','m',dvalue,addresses,defines,usedBlendLabels);
							if(c.getError()!=null) return c;
						} else {
							data[dcur++] = decodeDataByte(c,address,'w','m',dvalue,addresses,defines,usedBlendLabels);
							if(c.getError()!=null) return c;
							data[dcur++] = decodeDataByte(c,address,'w','l',dvalue,addresses,defines,usedBlendLabels);
							if(c.getError()!=null) return c;
						}
					} else {
						throw new RuntimeException("Unimplemented data size '"+dsize+"'");
					}					
					
				}
				
				continue;
			}
			
			// Not a data-line ... process all fill-ins in the opcode
			for(int pos=0;pos<t.length();pos=pos+2) {
				char p = t.charAt(pos);
				
				if(p>='a' && p<='z') {
					// Opcode parameter field (get the value from labels or defines
					data[pos/2] = decodeDataByte(c,address,p,t.charAt(pos+1),dataMap.get(""+p).value,addresses,defines,usedBlendLabels);
					if(c.getError()!=null) return c;
				} else {
					// Straight byte value
					data[pos/2] = Integer.parseInt(t.substring(pos,pos+2),16);
				}			
				
			}
			
		}
		
		// No error
		return null;
		
	}
		
	/*
	 * Return a byte value for the given opcode parameter. This may involve looking up symbols
	 * and performing PC-relative math. 
	 * @param co the code line 
	 * @param address the address of this opcode (for PC relative)
	 * @param p the first letter (the opcode parameter)
	 * @param q the second letter (l for LSB or m for MSB)
	 * @param value the value to decode
	 * @param addresses all known address specifications
	 * @param defines all defines
	 * @param usedBlendLabels a growing list of used blend labels
	 * @return the int value
	 */
	static int decodeDataByte(CodeLine co, int address, char p, char q, String value, 
			Map<String, AddressSpec> addresses,	Map<String,String> defines, Set<String> usedBlendLabels) 
	{
		// At this point we don't care if the parameter is an address, define, or number. We fill
		// in whatever we are given.
		
		// The blend process creates a LOT of labels. Some are used ... most are not. We track
		// the labels that are actually used in the code so we can ignore the others when
		// generating the listing file.
		if(value.startsWith("__")) usedBlendLabels.add(value);
		
		// We need various information about this paramter (p)
		OpcodeParamField opf = OpcodeParamField.getParamField(p);		
		int size = opf.getNumBytes();
		boolean signed = opf.isSigned();
		boolean pcRel = opf.isPCOffset();
		
		// Must be a constant, address, or define, and it must resolve to a numeric value
		Integer i = Expression.decodeExpression(co,value,defines,addresses);
		if(i==null) return 0;
						
		if(pcRel) {
			
			// Signed offset to the target label
			
			int target = i-(address+co.getOpcode().getOpcodeSize());
			
			if(size==1) {
				if(target<-128 || target>127) {
					co.setError("Relative address out of byte-offset range.");
					return 0;
				}				
				if(target<0) target=target+256;
			} else {
				if(target<-32768 || target>32767) {
					co.setError("Relative address out of word-offset range.");
					return 0;
				}				
				if(target<0) target=target+65536;
			}			
			
			i = target;
			
		} else {
			
			// One or two byte constant
			
			// If this is not a signed value then negatives produce an error. Otherwise
			// normalize negatives.
			if(i<0) {
				if(signed) {
					if(size==1) {
						i = i + 256;
					} else {
						i = i + 65536;
					}
				} else {
					co.setError("Invalid (negative) value '"+i+"'");
					return 0;
				}
			}
		}
			
		// Return the LSB or MSB of the value
		if(size==1) {
			if(i>255) {
				co.setError("Value is larger than a byte '"+i+"'");
			}
			return i;
		} else {
			if(q=='l') { // Return the least significant byte of the 2-byte value
				return i&255;
			} else if(q=='m') { // Return the most significant byte of the 2-byte value
				return (i>>8)&255;
			} else {
				throw new RuntimeException("Unknown 2nd char op parameter '"+q+"'");
			}
		}						
		
	}
	
	// Parse a data line
	static void parseData(CodeLine c)
	{
		DataOpcode da = new DataOpcode();
		String text = c.getOpcodeString().substring(1).trim();
		
		int size = 1;
		String lastValue = "0";
		
		while(text.length()!=0) {
			
			// Repeat last value
			if(text.startsWith(",")) {
				text=text.substring(1).trim();
				da.values.add(lastValue);
				da.sizes.add(size);
				continue;
			}
			
			// Size specification
			if(text.startsWith("(")) {
				int i = text.indexOf(")");
				if(i<0) {
					c.setError("Expected a ')'");
					return;
				}
				String a = text.substring(1,i).trim().toUpperCase();
				text = text.substring(i+1).trim();
				if(a.equals("BYTE")) size=1;
				else if(a.equals("WORD")) size=2;
				else if(a.equals("LONG")) size=4;
				else {
					c.setError("Unknown size ("+a+")");
					return;
				}
				continue;				
			}
			
			// Strings
			if(text.startsWith("\"")) {
				// TODO ability to escape the " in a string
				int j = text.indexOf("\"",1);
				if(j<0) {
					c.setError("Missing close quote");
					return;
				}
				for(int i=1;i<j;++i) {
					lastValue = ""+(int)text.charAt(i);
					da.values.add(lastValue);
					da.sizes.add(1);					
				}				
				text = text.substring(j+1).trim();
				if(text.startsWith(",")) text=text.substring(1);
				
				size = 1;
				continue;
			}
			
			// Find the end of this numeric term
			int i = text.indexOf(",");
			if(i<0) {
				i = text.length();			
			}
			
			// Pop off the term
			String a = text.substring(0,i);
			if(i<text.length()) text=text.substring(i+1).trim();
			else text="";
			
			// Numeric expression here
			//System.out.println(a);
			// TODO expression processor here
			
			
			// Add all the repeats to the opcode
			lastValue = a;
			da.values.add(lastValue);
			da.sizes.add(size);			
			
		}
				
		c.setOpcode(da);
	}
	
	// Recursive read routine for handling includes within includes.
	private static void recurseRead(String name, List<CodeLine> codeLines) throws IOException
	{
		FileReader fr = new FileReader(name);
		BufferedReader br = new BufferedReader(fr);
		int lineNumber = 0;
		
		while(true) {
			
			String g = br.readLine();
			if(g==null) break;
			++lineNumber;		
			
			// Parse the line
			CodeLine c = new CodeLine(g,name,lineNumber);
			codeLines.add(c);
						
			// Handle includes
			String gg = g.trim();
			int i = gg.indexOf(";");
			if(i>=0) {
				gg = gg.substring(0,i);
			}			
			if(gg.toUpperCase().startsWith("INCLUDE ")) {
				c.setDirective(true);
				String fn = gg.substring(8).trim();
				recurseRead(fn,codeLines);		
			}											
			
		}
		br.close();				
		
	}
	
	/**
	 * This function reads an assembly file (and includes) and parses it into CodeLines.
	 * @param name the name of the file
	 * @return the list of code lines
	 * @throws IOException with file errors
	 */
	public static List<CodeLine> readAssemblyText(String name) throws IOException
	{
		List<CodeLine> codeLines = new ArrayList<CodeLine>();
		recurseRead(name,codeLines);
		return codeLines;
	}
	
	public static int [] extractBinary(List<CodeLine> codeLines, int start, int end)
	{
		int [] ret = new int[end-start+1];
		for(int x=0;x<ret.length;++x) ret[x] = -1;
		
		for(CodeLine c : codeLines) {
			int [] data = c.getData();
			if(data==null) continue;
			int address = c.getAddress();
			for(int x=0;x<data.length;++x) {
				int i = address+x;
				if(i>=start && i<=end) {
					if(ret[i-start]!=-1) {
						c.setError("Multiple lines assemble to this same address.");
						return null;
					}
					ret[i-start] = data[x];
				}
			}
		}
		
		return ret;
	}
	
	public static void printListing(PrintStream ps, List<CodeLine> codeLines, 
			Map<String,String> defines, Map<String, AddressSpec> addresses, Set<String> usedBlendLabels) 
	{
		
		ps.println("Defines:");
		List<String> keys = new ArrayList<String>();
		keys.addAll(defines.keySet());
		Collections.sort(keys);		
		int maxLength = 0;
		for(String key : keys) {
			if(key.length()>maxLength) maxLength=key.length();
		}		
		for(String key : keys) {
			ps.println(CU.padTo(key,maxLength)+" = "+defines.get(key));
		}
		
		ps.println();
		ps.println("Address defines:");
		keys.clear();
		keys.addAll(addresses.keySet());
		Collections.sort(keys);		
		for(String key : keys) {
			if(!addresses.get(key).manual) continue; 
			if(key.startsWith("__")) continue; // ignore blend-generated labels
			ps.println(CU.fourDigitHex(addresses.get(key).address)+" = "+key);
		}
		
		ps.println();
		ps.println("Code labels:");
		keys.clear();
		keys.addAll(addresses.keySet());
		Collections.sort(keys);		
		for(String key : keys) {
			if(addresses.get(key).manual) continue;
			if(key.startsWith("__")) continue; // ignore blend-generated labels
			ps.println(CU.fourDigitHex(addresses.get(key).address)+" = "+key);
		}
					
		ps.println();
		for(CodeLine c : codeLines) {
			if(c.isDirective()) {
				ps.println(c.getOriginalText());
				continue;
			}
			if(c.getOpcodeString()==null) {
				String ot = c.getOriginalText();
				if(ot.startsWith("__") && ot.endsWith(":")) {
					if(!usedBlendLabels.contains(ot.substring(0,ot.length()-1))) {
						continue;				
					}
				}
				ps.println(c.getOriginalText());
				continue;
			}
			int dataWidth = 0; // No padding unless specified by the mnemonics	
			if(c.getOpcode()!=null && c.getOpcode().getProcessor()!=null) {
				Processor proc = c.getOpcode().getProcessor();
				ProcessorFamily pf = proc.getFamily();
				dataWidth = pf.getPrintSpacing().get(proc.getName()).dataFieldSize;
			}			
			// Find the processor and use its data width
			String data = CU.padTo(CU.getDataString(c.getData()), dataWidth);
			ps.println(CU.fourDigitHex(c.getAddress())+": "+data+" "+c.getOriginalText().trim());
		}
		
	}

}
