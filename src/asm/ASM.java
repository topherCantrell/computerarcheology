package asm;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;

import code.CodeFile;
import code.CodeLine;
import cpu.CPU;

public class ASM {
	
	CodeFile codeFile;
	CPU cpu;
	Map<String,String> defines = new HashMap<String,String>();
	Map<String,String> subs = new HashMap<String,String>();
	
	public ASM(String filename) throws IOException {		
		codeFile = new CodeFile(Paths.get(filename));
		expandIncludes();		
	}
	
	public void assemble() throws ASMException {		
		defines.clear();
		doPass(true);  // First pass  ... stub up the data
		defines.clear();
		doPass(false); // Second pass ... fill out the data		
	}
	
	protected void doPass(boolean firstPass) throws ASMException {
		for(CodeLine c : codeFile.code) {
			String st = c.opcode;
			if(st==null) continue;
			if(st.length()>0 && st.charAt(0)=='.') {
				if(st.startsWith(".byte")) {
					doByte(firstPass, st.substring(5).trim(),c);
				} else if(st.startsWith(".word")) {
					doWord(firstPass, st.substring(5).trim(),c);
				} else if(st.startsWith(".subs")) {
					doSubs(firstPass, st.substring(5).trim(),c);
				} else if(st.startsWith(".cpu")) {
					cpu = CPU.getCPU(st.substring(5).trim());
				} else {
					doAssign(firstPass, st.substring(1).trim(),c);
				}
			} else {
				doOpcode(firstPass,c);
			}
		}
	}
	
	protected void doAssign(boolean firstPass, String command, CodeLine c) throws ASMException {
		int i = command.indexOf("=");
		if(i>=0) {
			String key = command.substring(0,i).trim();
			String val = command.substring(i+1).trim();			
			if(defines.containsKey(key)) {
				throw new ASMException("Already defined '"+command+"'",c);
			}
			defines.put(key, val);
		} else {
			String key = command.trim();
			defines.remove(key);
		}		
	}
	
	protected void doSubs(boolean firstPass, String command, CodeLine c) throws ASMException {
		
		subs.clear();
		String[] ss = command.split(",");
		for(String s : ss) {
			int i = s.indexOf("=");
			if(i<0) {
				throw new ASMException("Invalid .subs '"+command+"'",c);
			}
			String key = command.substring(0,i).trim();
			String val = command.substring(i+1).trim();	
			if(defines.containsKey(key)) {
				throw new ASMException("Already subbed '"+key+"'",c);
			}
			subs.put(key, val);
		}
	}
	
	protected void doByte(boolean firstPass, String command, CodeLine c) {
		System.out.println("BYTE :"+command+":");
		// TODO Must process math expressions
	}
	
	protected void doWord(boolean firstPass, String command, CodeLine c) {
		System.out.println("WORD :"+command+":");
		// TODO Must process math expressions
	}
	
	protected void doOpcode(boolean firstPass, CodeLine c) {
		//System.out.println(c.opcode);
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
				
	}

}
