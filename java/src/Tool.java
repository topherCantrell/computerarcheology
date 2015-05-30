
/**
 * The tools live in their separate packages. This single dispatcher eases
 * the command-line clutter.
 */
public class Tool {
	
	public static void main(String [] args) throws Exception
	{
		
		String tool = args[0];
		
		String [] nargs = new String[args.length-1];
		for(int x=0;x<nargs.length;++x) {
			nargs[x] = args[x+1];
		}
		
		if(tool.toUpperCase().startsWith("DIF")) {
			tools.Diff.main(nargs);
		} else if(tool.toUpperCase().startsWith("BUILD")) {
			tools.Build.main(nargs);
		} else if(tool.toUpperCase().startsWith("AS")) {
			tools.assembler.Assembler.main(nargs);
		} else if(tool.toUpperCase().startsWith("DIS")) {
			tools.disassembly.Disassembler.main(nargs);
		} else if(tool.toUpperCase().startsWith("REBIN")) {
			tools.disassembly.ReBin.main(nargs);
		} else if(tool.toUpperCase().startsWith("DEPLOY")) {
			tools.web.XMLDeploy.main(nargs);
		}
		
		else {
			throw new RuntimeException("Unknown tool '"+tool+"'");
		}
	}

}
