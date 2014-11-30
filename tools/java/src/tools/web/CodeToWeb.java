package tools.web;

import java.io.PrintStream;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

import tools.code.AddressSpec;
import tools.code.CU;
import tools.code.CodeLine;
import tools.disassembly.Disassembler;
import tools.disassembly.DisassemblyFile;
import tools.disassembly.Menu;
import tools.processor.Opcode;
import tools.processor.OpcodeParamField;
import tools.processor.PrintSpacing;
import tools.processor.Processor;
import tools.processor.Processors;

// TODO Reports on labels and such 

/**
 * This tool converts commented disassembly to a web-friendly format. The list of mnemonic sets
 * can be overriden here.
 */
public class CodeToWeb 
{
	
	// HTML color and link templates for various fill ins.
	private static final String CODE_TEMPLATE =      "<a class='CodeLink' href='@1@'>@2@</a>";
	private static final String CODE_DEST_TEMPLATE = "<span class='CodeLinkDest' id='@1@'>; @2@</span>";
	private static final String RAM_TEMPLATE =       "<span class='RAMEntry'>@1@</span>";
	private static final String HDW_TEMPLATE =       "<span class='HDWEntry'>@1@</span>";
	private static final String PORT_TEMPLATE =      "<span class='PortEntry'>@1@</span>";
	
	static void main(String rootPath, String fileName, String htmlTitle, String out, String set) throws Exception 
	{
		
		PrintStream ps = System.out;
		if(out!=null) ps = new PrintStream(rootPath+out);
				
		// Load the disassembly file and process the special comments.
		DisassemblyFile df = new DisassemblyFile(rootPath,fileName);
						
		// We'll need the processor the code runs on
		String cpu = df.getMachineInfo().getCpuType();
				
		// We may be using alternate mnemonic sets
		String [] resultSet = df.getMachineInfo().getAsTypes();
		if(resultSet==null) {
			resultSet = new String[1];
			resultSet[0] = cpu;
		}
				
		int dataFieldSize = 0;
		int mnemonicFieldSize = 0;		
				
		Processor processor = null;
		if(!cpu.equals("none")) {
					
			processor = Processors.getInstance().getProcessor(cpu);
					
			if(set!=null) {
				StringTokenizer st = new StringTokenizer(set,",");
				for(int x=0;x<resultSet.length;++x) {
					resultSet[x] = st.nextToken();
				}
			}	
					
			// Get DATA and MNEMONIC spacing (either specified in file or default from mnemonic set)
			PrintSpacing psp = processor.getFamily().getPrintSpacing().get(resultSet[0]);
			dataFieldSize = psp.dataFieldSize;
			mnemonicFieldSize = psp.mnemonicFieldSize;
			int [] sizeOver = df.getMachineInfo().getPrintSpacing();
			if(sizeOver!=null) {
				dataFieldSize = sizeOver[0];
				mnemonicFieldSize = sizeOver[1];
			}	
		}	
				
		// Print the beginning of the HTML file
		ps.print("<HTML>\r\n");
		ps.print("<HEAD>\r\n");
		ps.print("<link rel=\"stylesheet\" href=\"/CodeView.css\" type=\"text/css\">\r\n");
		ps.print("<title>"+htmlTitle+"</title>\r\n");
		ps.print("</HEAD>\r\n");
				
		ps.println("<BODY background=\"/bg.jpg\">");
		ps.println("<!--#include file=\"../header.inc.html\"-->");		
				
		// Make the link table
		List<Menu> menus = df.getMenus();		
		for(Menu menu : menus) {
			ps.println("<table class=\"LinkTable"+menu.numColumns+"\">");
			ps.println("<tr><th colspan=\""+menu.numColumns+"\">"+menu.displayName+"</th></tr>");
			int colCnt = 0;
			for(int x=0;x<menu.displayNames.size();++x) {
				if(colCnt==0) {
					ps.print("<tr>");
					colCnt = 1;
				}
				String link = menu.links.get(x);
				String displayName = menu.displayNames.get(x);
				ps.print("<td><a href=\"#"+link+"\">"+displayName+"</a></td>\r\n");
				++colCnt;
				if(colCnt>menu.numColumns) {
					ps.print("</tr>");
					colCnt = 0;
				}				
			}
			if(colCnt!=0) {
				ps.print("</tr>");				
			}	
			ps.println("</table>");
		}
				
		// Now the code
				
		ps.print("<PRE id='code'>\r\n");
				
		List<CodeLine> lines = df.getLines();
		for(int x=0;x<lines.size();++x) {
			CodeLine c = lines.get(x);
				
			if(c.getAddress()==0xFF11) {
				System.out.println("HERE");
			}
					
			// Handle specials
			String comment = c.getSpecialCommentData();			
			if(comment!=null) {					
				if(comment.startsWith("$")) {
					df.getMachineInfo().parseInfo(comment.substring(1).trim());
				} else {
					printSpecialComment(c,ps);
				}
			} else if(c.getOpcode()==null || c.getData()==null) {
				printNonCode(c,ps,false);				
			} else {
				printCodeLine(c,ps,df,resultSet,dataFieldSize,mnemonicFieldSize,false);				
			}			
				
		}		
		ps.print("</PRE>\r\n");
				
		// Close the HTML	
		ps.println("</BODY>");
		ps.println("</HTML>");	
		
		if(out!=null) {
			ps.flush();
			ps.close();
		}
		
	}
	
	// 0           1            2             3         3
	// fileName    htmlTitle    [resultSets]  [-report] [-edit]
	public static void main(String [] args) throws Exception 
	{
		
		// For now this is a unix-like tool with everything going to STDOUT
		PrintStream ps = System.out;
		
		// Load the disassembly file and process the special comments.
		DisassemblyFile df = new DisassemblyFile("",args[0]);
				
		// We'll need the processor the code runs on
		String cpu = df.getMachineInfo().getCpuType();
		
		// We may be using alternate mnemonic sets
		String [] resultSet = df.getMachineInfo().getAsTypes();
		if(resultSet==null) {
			resultSet = new String[1];
			resultSet[0] = cpu;
		}
		
		int dataFieldSize = 0;
		int mnemonicFieldSize = 0;		
		
		boolean edit = false;
		
		if(args[args.length - 1].equals("-edit")) {
			edit = true;
		}
				
		Processor processor = null;
		if(!cpu.equals("none")) {
			
			processor = Processors.getInstance().getProcessor(cpu);
			
			if(args.length>2 && !args[2].startsWith("-")) {
				StringTokenizer st = new StringTokenizer(args[2],",");
				for(int x=0;x<resultSet.length;++x) {
					resultSet[x] = st.nextToken();
				}
			}
			
			// Get DATA and MNEMONIC spacing (either specified in file or default from mnemonic set)
			PrintSpacing psp = processor.getFamily().getPrintSpacing().get(resultSet[0]);
			dataFieldSize = psp.dataFieldSize;
			mnemonicFieldSize = psp.mnemonicFieldSize;
			int [] sizeOver = df.getMachineInfo().getPrintSpacing();
			if(sizeOver!=null) {
				dataFieldSize = sizeOver[0];
				mnemonicFieldSize = sizeOver[1];
			}	
		}	
		
		// Print the beginning of the HTML file
		ps.print("<HTML>\r\n");
		ps.print("<HEAD>\r\n");
		if(edit) {
			ps.print("<link rel=\"stylesheet\" href=\"CodeView.css\" type=\"text/css\">\r\n");
		} else {
			ps.print("<link rel=\"stylesheet\" href=\"/CodeView.css\" type=\"text/css\">\r\n");
		}
		ps.print("<title>"+args[1]+"</title>\r\n");
		
		if(edit) {
			ps.println("<script src='../editcode.js'></script>");
		}
		ps.print("</HEAD>\r\n");
		
		ps.println("<BODY background=\"/bg.jpg\">");
		ps.println("<!--#include file=\"../header.inc.html\"-->");		
		
		if(edit) {
			ps.println("<input type='text' id='saveFile' value='"+args[0]+"'/>");
			ps.println("<input type='button' id='btSave' value='Save Comments'/>");
		}
		
		// Make the link table
		List<Menu> menus = df.getMenus();		
		for(Menu menu : menus) {
			ps.println("<table class=\"LinkTable"+menu.numColumns+"\">");
			ps.println("<tr><th colspan=\""+menu.numColumns+"\">"+menu.displayName+"</th></tr>");
			int colCnt = 0;
			for(int x=0;x<menu.displayNames.size();++x) {
				if(colCnt==0) {
					ps.print("<tr>");
					colCnt = 1;
				}
				String link = menu.links.get(x);
				String displayName = menu.displayNames.get(x);
				ps.print("<td><a href=\"#"+link+"\">"+displayName+"</a></td>\r\n");
				++colCnt;
				if(colCnt>menu.numColumns) {
					ps.print("</tr>");
					colCnt = 0;
				}				
			}
			if(colCnt!=0) {
				ps.print("</tr>");				
			}	
			ps.println("</table>");
		}
		
		// Now the code
		
		ps.print("<PRE id='code'>\r\n");
		
		List<CodeLine> lines = df.getLines();
		for(int x=0;x<lines.size();++x) {
			CodeLine c = lines.get(x);
			
			if(c.getAddress()==0xFF11) {
				System.out.println("HERE");
			}
			
			// Handle specials
			String comment = c.getSpecialCommentData();			
			if(comment!=null) {					
				if(comment.startsWith("$")) {
					df.getMachineInfo().parseInfo(comment.substring(1).trim());
				} else {
					printSpecialComment(c,ps);
				}
			} else if(c.getOpcode()==null || c.getData()==null) {
				printNonCode(c,ps,edit);				
			} else {
				printCodeLine(c,ps,df,resultSet,dataFieldSize,mnemonicFieldSize,edit);				
			}			
			
		}		
		ps.print("</PRE>\r\n");
		
		// Close the HTML	
		ps.println("</BODY>");
		ps.println("</HTML>");	
		
	}
	
	static void printCodeLine(CodeLine codeLine, PrintStream ps, DisassemblyFile df, String [] resultSet, 
			int dataFieldSize, int mnemonicFieldSize, boolean edit) 
	{
		// For a code line we will ignore any existing opcode string and make our own. Thus the opcodes
		// are always up to date.
		
		Opcode opcode = codeLine.getOpcode();
		List<OpcodeParamFieldReplaceInfo> replacements = new ArrayList<OpcodeParamFieldReplaceInfo>();
		
		Map<OpcodeParamField,String> params = opcode.decodeData(codeLine.getData());
		for(OpcodeParamField field : params.keySet()) {
						
			// We are only interested in addresses (data or code)
			if(!field.isAddress() && !field.isIO()) continue;
			
			int val = Integer.parseInt(params.get(field),16);
			if(field.isPCOffset()) {
				val = val + codeLine.getData().length;
				if(field.getNumBytes()==2) {
					if(val>32767) val=val-65536;
				} else {
					if(val>127) val=val-256;
				}
				val = val + codeLine.getAddress();
			}
			
			// Allow for multiple code files (ROM banks)
			String bankName = "";
			DisassemblyFile bankFile = df;
			if(codeLine.getComment()!=null && codeLine.getComment().trim().startsWith("%%")) {
				String bn = codeLine.getComment().trim();
				int i = bn.indexOf(" ");
				if(i>0) {
					bn = bn.substring(0,i);
				}
				bn = bn.substring(2);
				if(bn.length()==0) { 
					bn="fixed";
				}
				bankFile = df.getBank(bn);
				if(bankFile!=null) {
					bankName = bankFile.getFilename()+".html";
				}
			}
			
			if(bankFile==null) {
				throw new RuntimeException(codeLine.getComment());
			}
			
			
			// First look for a code address
			AddressSpec spec = bankFile.findCodeAddress(opcode.getBus(),val,false,false);			
			if(spec!=null) {
				OpcodeParamFieldReplaceInfo or = new OpcodeParamFieldReplaceInfo();
				or.field = field;							
				or.replacementPrintedSize = spec.readLabel.length();
				List<String> rp = new ArrayList<String>();
				rp.add(bankName+"#"+spec.readLabel);
				rp.add(spec.readLabel);
				or.replacement = substituteIn(CODE_TEMPLATE,rp);
				replacements.add(or);
				continue;
			}						
			
			// Next look for manual port or memory address
			if(field.isIO()) {
				spec = bankFile.findCodeAddress(opcode.getBus(),val,true,true);
				if(spec!=null) {
					OpcodeParamFieldReplaceInfo or = new OpcodeParamFieldReplaceInfo();
					or.field = field;		
					String label = spec.readLabel;
					if(opcode.getBus()!=null && opcode.getBus().equals("w")) {
						label = spec.writeLabel;
					}
					or.replacementPrintedSize = label.length();
					List<String> rp = new ArrayList<String>();
					rp.add(label);
					or.replacement = substituteIn(PORT_TEMPLATE,rp);
					replacements.add(or);
					continue;
				} 
			} else {	
				// Base-page offset
				if(field==OpcodeParamField.BASE_ADDRESS_BYTE_DATA) {
					val = val + bankFile.getMachineInfo().getCurrentBasePageOffset();
				}
				spec = bankFile.findCodeAddress(opcode.getBus(),val,false,true);
				if(spec!=null) {
					OpcodeParamFieldReplaceInfo or = new OpcodeParamFieldReplaceInfo();
					or.field = field;		
					String label = spec.readLabel;
					if(opcode.getBus()!=null && opcode.getBus().equals("w")) {
						label = spec.writeLabel;
					}
					if(label!=null) {
						or.replacementPrintedSize = label.length();
						List<String> rp = new ArrayList<String>();
						rp.add(label);
						// TODO this should be meta information in the comment ... not dependent on starting with "_"
						if(label.startsWith("_")) {
							or.replacement = substituteIn(HDW_TEMPLATE,rp);
						} else {
							or.replacement = substituteIn(RAM_TEMPLATE,rp);
						}
						replacements.add(or);
						continue;
					}
				}
			}			
			
		}
				
		String a = CU.getDataString(codeLine.getData());
		a = CU.padTo(a,dataFieldSize);
		
		String b = Disassembler.getDisassembly(codeLine.getAddress(), codeLine.getData(), codeLine.getOpcode(), 
				replacements, resultSet,mnemonicFieldSize);
				
		String com = "";
		if(codeLine.getComment()!=null) {			
			com=";"+codeLine.getComment();			
		}								
		
		if(edit) {
			ps.print(editableComment(codeLine.getAddress(),CU.fourDigitHex(codeLine.getAddress())+": "+a+b+com+"\r\n"));
		} else {
			ps.print(CU.fourDigitHex(codeLine.getAddress())+": "+a+b+com+"\r\n");
		}
		
	}
	
	static String editableComment(int address, String s) {		
		if(address==-1) return s;
		int i = s.indexOf(";");
		if(i<0) {			
			return s;
		}
		
		String post = "";
		int j = s.indexOf("\r\n");
		if(j>=0) {
			post = s.substring(j);
			s = s.substring(0,j);
		}
		
		String a = s.substring(0,i+1);
		String b = s.substring(i+1);	
		
		b = CU.replaceAll(b, "'", "&apos;");
		
		return a + "<input class='CodeInput' type='text' size='100' id='"+address+"' value='"+b+"'/>"+post;
		
	}
	
	static void printNonCode(CodeLine codeLine, PrintStream ps, boolean edit) {
		// Not a "code" line
		if(edit) {
			ps.print(editableComment(codeLine.getAddress(),codeLine.getOriginalText()+"\r\n"));
		} else {
			ps.print(codeLine.getOriginalText()+"\r\n");
		}
	}
	
	static void printSpecialComment(CodeLine codeLine,PrintStream ps) {
		
		String comment = codeLine.getSpecialCommentData();
		
		// Could be a base-page setting that could change over the course of the file
				
		if(comment.startsWith("--")) {
			ps.println("<hr>");
			return;
		}
		
		if(comment.startsWith("!")) {
			ps.print(comment.substring(1).trim());			
			return;
		}
		
		if(comment.startsWith("Menu")) {
			return;
		}
		
		if(comment.equals("-") || comment.startsWith("- ")) {
			return;
		}
		
		if(comment.startsWith("+") || comment.startsWith("*")) {
			//TODO maybe something better descriptive? A table?
			ps.print("; "+codeLine.getOriginalText().substring(2)+"\r\n");
			return;
		}
		
		// It MUST be a link destination
		if(comment.startsWith("-")) {
			comment = comment.substring(1);
		}
						
		String ca=comment;
		int i = ca.indexOf(" ");
		if(i>0) {					
			ca = ca.substring(0,i);
		}
		
		List<String> rp = new ArrayList<String>();
		rp.add(ca);
		rp.add(comment);
		ps.print(substituteIn(CODE_DEST_TEMPLATE,rp)+"\n");
	}


	private static String substituteIn(String codeTemplate, List<String> rp) {		
		for(int x=0;x<rp.size();++x) {
			codeTemplate = CU.replaceAll(codeTemplate, "@"+(x+1)+"@", rp.get(x));			
		}		
		return codeTemplate;
	}

}
