package asm;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import code.CodeFile;
import code.CodeLine;

public class ASM {
	
	CodeFile codeFile;
	
	public ASM(String filename) throws IOException {		
		codeFile = new CodeFile(Paths.get(filename));
		expandIncludes();		
	}
	
	public void assemble() {		
		doPass(true);  // First pass  ... stub up the data
		doPass(false); // Second pass ... fill out the data		
	}
	
	protected void doPass(boolean firstPass) {
		
	}
	
	private void expandIncludes() throws IOException {
		boolean changed = true;
		while(changed) {
			changed = false;
			for(int x=codeFile.code.size()-1;x>=0;--x) {
				CodeLine c = codeFile.code.get(x);
				if(c.originalText.startsWith(".include")) {
					changed = true;
					codeFile.code.remove(x);
					int i = c.originalText.indexOf(" ");
					String fname = c.originalText.substring(i+1).trim();
					if(fname.startsWith("\"")) {
						fname = fname.substring(1,fname.length()-1);
					}
					Path p = Paths.get(codeFile.filename);					
					CodeFile inc = new CodeFile(Paths.get(p.getParent()+"/"+fname));
					for(int y=0;y<inc.code.size();++y) {
						codeFile.code.add(x+y,inc.code.get(y));						
					}					
				}
			}
		}
	}
	
	public static void main(String [] args) throws Exception
	{
		
		ASM asm = new ASM("content/atari2600/doublegap/doublegap.asm");	
		asm.assemble();
		System.out.println(asm);
				
	}

}
