package tools.disassembly;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

import tools.code.CU;
import tools.code.CodeLine;
import tools.file.BinaryFiles;
import tools.processor.Mnemonic;
import tools.processor.Opcode;
import tools.processor.OpcodeParamField;
import tools.processor.PrintSpacing;
import tools.processor.Processor;
import tools.processor.ProcessorFamily;
import tools.processor.Processors;
import tools.web.OpcodeParamFieldReplaceInfo;

/**
 * This class manages the conversion of binary data into disassembly.
 */
public class Disassembler { 
	
	/**
	 * This tool disassembles a binary file into text opcodes for a target processor.
	 * 
	 * Command line arguments: binFile cpu [start] [end] [resultMnemonic]
	 * 
	 * The 'binFile' is a list of ROM files each with a given origin. For instance:
	 * 0x0000~invaders.h+invaders.g+invaders.f+invaders.e
	 * 
	 * This puts the four Space Invaders ROM files together in order. The first file
	 * is given the origin "0x0000" and the others follow right behind it.
	 * 
	 * The 'cpu' is the CPU that runs the code.
	 * 
	 * The 'start' and 'end' are optional starting and ending points in the disassembly
	 * ROM data. If 'start' is not given then the first address is used. If 'end' is
	 * not given the the last address is used. Leave both out to disassemble the entire
	 * binary collection.
	 * 
	 * The 'resultMnemonic' gives the output menonic set for the opcodes. The default is
	 * to use the same CPU as the 'cpu' value. Most of the time this is exactly what
	 * you want to do. But this is useful if you want to disassemble cpu=8080 code but
	 * output the mnemonics as resultCPU=Z80. If you used cpu=Z80 then you would get
	 * Z80 mnemonics in the output in data sections.
	 * 
	 * Once a file has been disassembled to text then it can be annotated and run through
	 * ReDiss to change the mnemonic set(s) and spacing.
	 * 
	 * @param args see above
	 * @throws Exception errors opening files
	 */
	public static void main(String [] args) throws Exception 
	{
		
		// TODO allow data/mnemonic spacing values to be passed in
		
		if(args.length==0) {
			System.out.println("Arguments: binFile cpu [start] [end] [resultMnemonics]");
			return;
		}
		
		// Load the data from multiple files. The origin is part of the
		// specification.
		BinaryFiles files = new BinaryFiles(args[0]);
		int start = files.getLowestAddress();
		int end = files.getHighestAddress();
		
		// Get the opcode set
		Processor processor = Processors.getInstance().getProcessor(args[1]);
		String [] resultMnemonics = {processor.getName()};
		
		// Start at the first address unless told otherwise
		if(args.length>2) {
			start = CU.parseIntValue(args[2]);
		}
		
		// End at the last address unless told otherwise
		if(args.length>3) {
			end = CU.parseIntValue(args[3]);
		}
		
		// Can output in another nmemonic set
		if(args.length>4) {
			resultMnemonics[0] = args[4];
		}
		
		// We need the binary data in an array for scanning						
		int [] binary = new int[end-start+1];
		for(int x=start;x<=end;++x) binary[x-start]=files.getByte(x);		
		
		// Disassemble the binary to opdoces (not mnemonics ... that comes next)
		List<CodeLine> lines = getDisassemblyOpcodes(processor,binary,start);
		
		// Print the disassembly
		printDisassembly(lines,args[1],resultMnemonics,true);
		
	}
	
	/**
	 * This function disassembles the binary data into a list of opcodes.
	 * @param processor the target processor
	 * @param binary the binary data
	 * @param origin the origin of the first location of the data
	 * @return the disassembled opcodes
	 */
	public static List<CodeLine> getDisassemblyOpcodes(Processor processor, int [] binary, int origin)
	{
		// Final disassembly
		List<CodeLine> lines = new ArrayList<CodeLine>();
		
		int pos = 0;		
		while(pos<binary.length) {			
			int len = 1;
			while(true) {
				List<Opcode> potentials = processor.findPossibleOpcodes(binary, pos, len);
				// Keep going till there are 1 or no potentials
				if(potentials.size()>1) {
					++len;
					continue;
				}
				
				Opcode nc = null;
				int ns = 1;
				
				if(potentials.size()==1) {
					nc = potentials.get(0);
					ns = nc.getOpcodeSize();
				}
										
				int [] cdata = new int[ns];
				for(int x=0;x<ns;++x) {
					if((pos+x)<binary.length) {
						cdata[x] = binary[pos+x];
					} else {
						cdata[x]= 0xFF;
					}
				}
				CodeLine c = new CodeLine("","",0);
				lines.add(c);
				c.setAddress(origin+pos);
				c.setOpcode(nc);
				c.setData(cdata);
				
				// Next address
				pos = pos + cdata.length;
				
				break; // Done here						
			}
		}
		
		return lines;
	}
		
	/**
	 * This method returns the disassembly mnemonic for the given run of data. The field is padded to the visible
	 * length (certain substituted fields may contribute invisible (HTML markup) text.
	 * @param address the memory address of this data (needed for relative destinations
	 * @param data the opcode data bytes
	 * @param opcode the opcode information
	 * @param replacements list of any substitution labels into the mnemonic text (or null for pure numeric values)
	 * @param resultMnemonics the mnemonics set names to generate in order (within the processor family)
	 * @param fieldPadding the mnemonic field spacing override. Use 0 for the default.
	 */
	public static String getDisassembly(int address, int [] data, Opcode opcode, 
			List<OpcodeParamFieldReplaceInfo> replacements,	String [] resultMnemonics,
			int fieldPadding)
	{		
				
		// If the opcode is given but has no entry for the requested mnemonic sets then bomb
		Mnemonic mn = null;
		for(String s : resultMnemonics) {
			mn = opcode.getMnemonics().get(s);			
			if(mn!=null) break;
		}
		if(mn==null) {
			String t = "";
			for(String s : resultMnemonics) t=t+" "+s; 
			throw new RuntimeException("Opcode '"+opcode.getCode()+
					"' has no mnemonic set "+t);
		}
				
		// Use the first representation
		String mnt = mn.getTextRepresentations()[0];
					
		// Decode the data into the opcode's param fields
		Map<OpcodeParamField,String> vals = opcode.decodeData(data);		
						
		String ret = "";		
		int mnemonicVisibleLength=0;
		
		for(int x=0;x<mnt.length();++x) {
			char a = mnt.charAt(x);
			
			if(a<'a' || a>'z') {
				// Plain old character ... just add it
				ret = ret + a;
				++mnemonicVisibleLength;
				continue;
			}
				
			// Get the info about the parameter
			OpcodeParamField param = OpcodeParamField.getParamField(a);			
			String pv = vals.get(param);
			
			
			if(pv==null) {
				System.out.println(mnt);
				System.out.println(vals);
				System.out.println(param);
				System.out.println(Arrays.toString(data));
			}
			
			// Get the numeric value for the parameter
			int v = Integer.parseInt(pv,16);
				
			// Correct if signed
			if(param.isSigned()) {
				v = CU.signedNumber(param.getNumBytes()*8, v);
			}
								
			// If parameter is a PC offset then add the address
			if(param.isPCOffset()) {
				v = v+address+data.length;
			}
				
			String cnv = null;				

			if(param==OpcodeParamField.PUSH_6809_U || param==OpcodeParamField.PUSH_6809_S) {
				cnv = "";
				if((v&128)!=0) cnv=cnv+",PC";
				if((v&64)!=0) {
					if(param==OpcodeParamField.PUSH_6809_U) {
						cnv=cnv+",S";
					} else {
						cnv=cnv+",U";							
					}						
				}
				if((v&32)!=0) cnv=cnv+",Y";
				if((v&16)!=0) cnv=cnv+",X";
				if((v&8)!=0) cnv=cnv+",DP";
				if((v&4)!=0) cnv=cnv+",B";
				if((v&2)!=0) cnv=cnv+",A";
				if((v&1)!=0) cnv=cnv+",CC";			
				if(cnv.startsWith(",")) cnv = cnv.substring(1);
			} else if(param==OpcodeParamField.PULL_6809_U || param==OpcodeParamField.PULL_6809_S) {
				cnv = "";					
				if((v&1)!=0) cnv=cnv+",CC";
				if((v&2)!=0) cnv=cnv+",A";
				if((v&4)!=0) cnv=cnv+",B";
				if((v&8)!=0) cnv=cnv+",DP";
				if((v&16)!=0) cnv=cnv+",X";
				if((v&32)!=0) cnv=cnv+",Y";
				if((v&64)!=0) {
					if(param==OpcodeParamField.PUSH_6809_U) {
						cnv=cnv+",S";
					} else {
						cnv=cnv+",U";							
					}						
				}					
				if((v&128)!=0) cnv=cnv+",PC";								
				if(cnv.startsWith(",")) cnv = cnv.substring(1);
			} else if(param==OpcodeParamField.REG_6809_TFR) {
				String [] regs = {"D","X","Y","U","S","PC","?","?","A","B","CCR","DP","?","?" ,"?","?"};
				cnv=regs[v>>4]+","+regs[v&15];
			} else {
				if(param.getNumBytes()==1) {
					cnv = "$"+CU.twoDigitHex(v);
				} else {
					cnv = "$"+CU.fourDigitHex(v);
				}
			}
			int cnvVisibleLength = cnv.length();
				
			if(replacements!=null) {
				for(OpcodeParamFieldReplaceInfo rep : replacements) {
					if(rep.field.getSubChar()==a) {
						cnv = rep.replacement;
						cnvVisibleLength = rep.replacementPrintedSize;
						break;
					}
				}
			}
				
			ret = ret + cnv;
			mnemonicVisibleLength+=cnvVisibleLength;
					
		}
		
		// Get the spacing for the fields of this opcode
		if(fieldPadding<=0) {
			ProcessorFamily pf = opcode.getProcessor().getFamily();
			PrintSpacing psp = pf.getPrintSpacing().get(resultMnemonics[0]);
			fieldPadding = psp.mnemonicFieldSize;
		}
		
		while(mnemonicVisibleLength<fieldPadding) {
			++mnemonicVisibleLength;
			ret = ret + " ";
		}
				
		return ret;

	}
	
	/**
	 * This function prints the disassembly of a list of code lines in the given
	 * mnemonic set.
	 * @param lines the list of lines
	 * @param mnemonicSets the name of the mnemonic sets to output (in order)
	 * @param commentOverride true will always add a comment, even if it is blank
	 */
	public static void printDisassembly(List<CodeLine> lines, String cpu, String [] mnemonicSets, boolean commentOverride) 
	{
		
		String t = "";
		for(String s : mnemonicSets) t=t+" "+s;
		System.out.println(";##$ CPU "+cpu+" as"+t);
						
		// Dump the disassembly
		for(CodeLine line : lines) {
			if(line.getOpcode()==null) {
				int [] dat = line.getData();
				if(dat.length>0) {
					System.out.print(CU.fourDigitHex(line.getAddress())+": ");
					for(int i : dat) System.out.print(CU.twoDigitHex(i)+" ");
					System.out.println();
				} else {
					System.out.println(line.getOriginalText());
				}
				continue;
			}
			String a = CU.getDataString(line.getData());
			// For now we use the first spacing. We can always RedDiss it later and set the spacing.
			PrintSpacing psp = line.getOpcode().getProcessor().getFamily().getPrintSpacing().get(mnemonicSets[0]);
			a = CU.padTo(a,psp.dataFieldSize);
			String b = getDisassembly(line.getAddress(),line.getData(),line.getOpcode(),null,mnemonicSets,0);			
			String comment = "";
			if(line.getComment()!=null) {
				comment=";"+line.getComment();
			} else {
				if(commentOverride) comment="; ";
			}
			System.out.println(CU.fourDigitHex(line.getAddress())+": "+a+" "+b+comment);
			
		}	
		
	}

}
