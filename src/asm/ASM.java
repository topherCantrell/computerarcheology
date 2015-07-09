package asm;

import java.io.IOException;
import java.io.PrintStream;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

import code.CU;
import code.CodeFile;
import code.CodeLine;
import cpu.CPU;

import javax.script.ScriptEngineManager;
import javax.script.ScriptEngine;
import javax.script.ScriptException;

public class ASM {
	
	CodeFile codeFile;
	CPU cpu;
	Map<String,String> defines = new HashMap<String,String>();
	Map<String,String> subs = new HashMap<String,String>();
	
	ScriptEngineManager mgr = new ScriptEngineManager();
    ScriptEngine engine = mgr.getEngineByName("JavaScript");
	
	public ASM(String filename) throws IOException {		
		codeFile = new CodeFile(Paths.get(filename));
		expandIncludes();		
	}
	
	public void assemble() throws ASMException {		
		defines.clear();
		doPass(true);  // First pass  ... stub up the data		
		doPass(false); // Second pass ... fill out the data		
	}
	
	protected void doPass(boolean firstPass) throws ASMException {
		
		int address = 0; // The current instruction's address (default origin is 0)
		
		for(CodeLine c : codeFile.code) {
			
			if(c.address>=0) {
				address = c.address;				
			} else {
				c.address = address;
			}
			if(c.label!=null && c.label.length()>0) {
				doAssign(firstPass, c.label+"="+address,c);				
			}
			
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
				if(c.data!=null) {
					address = address + c.data.size();
				}
			} else {				
				address = address + doOpcode(firstPass,c);
			}
		}
	}
	
	protected void doAssign(boolean firstPass, String command, CodeLine c) throws ASMException {
		int i = command.indexOf("=");
		if(i>=0) {
			String key = command.substring(0,i).trim();
			String val = command.substring(i+1).trim();			
			if(firstPass && defines.containsKey(key)) {
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
		String[] ss = command.split("\\,");
		for(String s : ss) {
			int i = s.indexOf("=");
			if(i<0) {
				throw new ASMException("Invalid .subs '"+command+"'",c);
			}
			String key = s.substring(0,i).trim();
			String val = s.substring(i+1).trim();	
			if(defines.containsKey(key)) {
				throw new ASMException("Already subbed '"+key+"'",c);
			}
			subs.put(key, val);
		}
	}
		
	protected void doByte(boolean firstPass, String command, CodeLine c) throws ASMException {
		c.data = new ArrayList<Integer>();
		String[] dats = command.split(",");
		for(String dat : dats) {
			int v = parseData(firstPass, dat, c);
			c.data.add(v);
		}		
	}
	
	protected void doWord(boolean firstPass, String command, CodeLine c) throws ASMException {
		c.data = new ArrayList<Integer>();
		String[] dats = command.split(",");
		for(String dat : dats) {
			int v = parseData(firstPass, dat, c);
			if(cpu.bigEndian) {
				c.data.add((v>>8)&0xFF);
				c.data.add(v&0xFF);
			} else {
				c.data.add(v&0xFF);
				c.data.add((v>>8)&0xFF);				
			}			
		}
	}
	
	private boolean isTermChar(char ch) {
		if(ch=='_' || (ch>='a' && ch<='z') || (ch>='A' && ch<='Z') || (ch>='0' && ch<='9')) {
			return true;
		}
		return false;
	}
	
	private String processTerm(String curTerm, CodeLine c) throws ASMException {
		if(curTerm.charAt(0)>='0' && curTerm.charAt(0)<='9') {
			if(!CU.isNumeric(curTerm, 10)) {
				throw new ASMException("Invalid number '"+curTerm+"'",c);
			}
			return ""+ CU.parseInt(curTerm, 10);
		} else {
			String val = defines.get(curTerm);
			if(val==null) {
				throw new ASMException("Symbol not defined '"+curTerm+"'",c);
			}
			return val;						
		}
	}
	
	protected int parseData(boolean firstPass, String command, CodeLine c) throws ASMException {
		if(firstPass) {
			return 0;
		}
		command = command.trim();
		for(Entry<String, String> s : subs.entrySet()) {
			command = CU.replaceAll(command, s.getKey(), s.getValue());
		}
		
		// The expression is a string of terms and operators.
		// A term begins with a number or letter. Everything else is
		// an operator.
		
		// Run through the expression and replace numbers with plain decimal and symbols
		// with their numeric value.
				
		String s = "";
		String curTerm = null;
		for(int i=0;i<command.length();++i) {
			char ch = command.charAt(i);			
			
			if(isTermChar(ch)) {
				if(curTerm!=null) {
					curTerm = curTerm + ch;
				} else {
					curTerm = ""+ch;
				}
			} else {				
				if(curTerm!=null) {						
					s = s + processTerm(curTerm,c);
					curTerm = null;					
				}
				s = s + ch;
			}
		}
		if(curTerm!=null) {
			s = s + processTerm(curTerm,c);
		}
				
	    try {
			String val = engine.eval(s).toString();
			return Integer.parseInt(val);			
		} catch (ScriptException e) {
			throw new ASMException("Could not evaluate expression '"+s+"'",c);
		}
	}
	
	protected int doOpcode(boolean firstPass, CodeLine c) {
		
		/*
		 
		 An opcode spec looks like this:
		 "DEC t,X" : "DEtltm"
		 
		 Beginning part "DEC " (note the space)
		 Ending part ",X"
		 
		 The Z80 has one opcode with multiple fill-ins:
		 "LD (IY+i),b" : "FD36iibb"		 
		 This +i is also signed. It might appear as (IY-i).		 
		 
		 The Z80 assembler will have to convert "LD (IY-128),4" to "LD (IY+-128),4"
		 for proper matching.		 
		 
		 - Find the numbers in the input. Make an array of CONST+number+CONST+number+CONST+number
		   as many as there are
		 - Match the terms to the opcode. There should only be one match.
		 
		 */
		
		// TODO Finish this
		//System.out.println(c.opcode);
		c.data = new ArrayList<Integer>();
		c.data.add(0);
		c.data.add(1);
		c.data.add(2);
		return 3;
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
	
	public void makeListing(PrintStream ps) {
		
		int[] spacing = cpu.getSpacing();
		
		for(CodeLine c : codeFile.code) {
			if(c.data==null || c.data.size()==0) {
				ps.println(c.originalText);
				continue;
			}
			
			String s = CU.hex4(c.address)+": ";
			
			String dat = "";
			for(int i : c.data) {
				s = s + CU.hex2(i)+" ";
			}
			dat = CU.padTo(dat, spacing[0]);
			
			String ot = c.originalText;
			if(c.label!=null && c.label.length()>0) {
				s = c.label+":\n"+s;
			}
						
			ps.println(s+dat+ot);
		}
		
	}
	
	public static void main(String [] args) throws Exception {
		
		ASM asm = new ASM("content/atari2600/doublegap/doublegap.asm");	
		asm.assemble();		
		
		asm.makeListing(System.out);
				
	}

}
