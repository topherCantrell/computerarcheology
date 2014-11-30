package tools.disassembly;

import tools.code.CU;
import tools.code.CodeLine;

/**
 * Occasionally the disassembler changes (hopefully for the better). Then it
 * may be necessary to "re-disassemble" a file by replacing the opcode
 * mnemonics in place but leave the comments and data alone. This tool does that.
 */
public class ReDis {

	// ReDis disFile
	
	public static void main(String [] args) throws Exception 
	{	
		// Load the disassembly file
		DisassemblyFile df = new DisassemblyFile("",args[0]);
				
		MachineInfo mi = df.getMachineInfo();
		
		String [] resultSets = mi.getAsTypes();
		if(resultSets == null) {
			resultSets = new String[1];
			resultSets[0] = mi.getCpuType();
		}
		
		int [] spacing = {14,25};
				
		for(CodeLine c : df.getLines()) {
			
			if(c.getOpcode()!=null) {
												
				String b = Disassembler.getDisassembly(c.getAddress(), c.getData(),
						c.getOpcode(), null,resultSets,spacing[1]);
												
				String a = CU.getDataString(c.getData());
				a = CU.padTo(a,spacing[0]);
				String comment = "";
				if(c.getComment()!=null) {
					comment=";"+c.getComment();
				}				
				System.out.println(CU.fourDigitHex(c.getAddress())+": "+a+" "+b+comment);
				
				
			} else {
				System.out.println(c.getOriginalText());
			}
			
		}
				
	}

}
