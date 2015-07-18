package cpu;

import java.util.ArrayList;

import asm.ASM;
import asm.ASMException;
import code.AddressAccess;
import code.BusDir;
import code.BusType;
import code.CU;
import code.CodeLine;

public class CPU_6502 extends CPU {
	
	public CPU_6502() {
		try {
			loadOpcodes("src/cpu/6502.js");
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}
	
	@Override
	public int[] getSpacing() {
		int[] ret = {9,6,16};
		return ret;
	}
	
	@Override
	public int assemble(boolean firstPass, CodeLine co, ASM asm) throws ASMException {
						
		// 'LDA ('   '>0x20'   '),Y'
		//    a         b       c
		
		String a = co.opcode.trim();
		String b = null;
		String c = null;
		
		// Addresses can have direct/extended override marks
		int addrOverrideType = 0; // 1="<" and 2=">"
		
		int num = 1; // Number of terms (1 to 3)
		int i = a.indexOf(" ");
		if(i>0) {
			num = 2;
			b = a.substring(i+1);
			a = a.substring(0,i+1);
			b = b.replaceAll(" ","");
			
			// IMMEDIATE or DIRECT or EXTENDED marks
			if(b.charAt(0)=='#') {
				a = a + "#";
				b = b.substring(1);
			} else if(b.charAt(0)=='<') {
				addrOverrideType = 1;
				b = b.substring(1);
			} else if(b.charAt(0)=='>') {
				addrOverrideType = 2;
				b = b.substring(1);
			} 			
			
			// Indexing results in a 3rd term
			i = b.indexOf(",");			
			if(i>=0) {
				num = 3;
				c = b.substring(i);
				b = b.substring(0,i);
				if(b.charAt(0)=='(' && b.charAt(b.length()-1)==')') {
					a = a+"(";
					c = ")"+c;
					b = b.substring(1,b.length()-1);
				}
			}
			
			// Some opcodes target the A register instead of a number
			if(b.equals("A")) {
				a = a + "A";
				b = null;
				c = null;
				num = 1;
			}
		}
		
		// On the second pass we evaluate the value		
		int value = 0;
		if(b!=null && !firstPass) {
			value = asm.parseData(firstPass,b,co);
		}
		
		Opcode fnd = null;
		for(Opcode op : opcodes) {
									
			// The opcode must match the number of pieces we have
			if(op.mnemonic.length != num) continue;
			
			// There is always a first piece
			if(!op.mnemonic[0].equals(a)) {
				continue;
			}
			
			// If there is a 3rd piece, make sure it matches
			if(c!=null) {
				if(op.mnemonic.length!=3) continue;
				if(!c.toUpperCase().equals(op.mnemonic[2])) continue;
			}
			
			// Make sure the opcode matches the override (if any)
			if(op.mnemonic.length>1) {
				if(addrOverrideType==1 && !op.mnemonic[1].equals("p")) continue;
				if(addrOverrideType==2 && !op.mnemonic[1].equals("t")) continue;
			}
						
			if(fnd!=null && num>1) {
				
				// There might be multiple matches. We need to distinguish between 'p' (direct)
				// and 't' (extended) opcodes based on override marks or value size.
					
				Opcode pForm = null;
				Opcode tForm = null;
				
				if(fnd.mnemonic[1].equals("p")) {
					pForm = fnd;
				} else if(fnd.mnemonic[1].equals("t")) {
					tForm = fnd;
				}
				if(op.mnemonic[1].equals("p")) {
					pForm = op;
				} else if(op.mnemonic[1].equals("t")) {
					tForm = op;
				}
				
				if( pForm!=null && tForm!=null) {
					
					// We are dealing with a p vs t situation. Pick the best one.
					
					// To pick we need to know the value. If this is a defined
					// symbol then we'll have it in the first pass. Otherwise
					// we have to assume the worst (2 byte value). If you don't
					// like what we pick then use the '<' or '>' to force it.
					if(firstPass) {
						try {
							value = asm.parseData(false,b,co);
						} catch (ASMException e) {
							// Might be a code symbol later we pick up later
							// in the first pass.
							value = 0xFFFF;
						}
					} 
					
					if(value>=0 && value<=0xFF) {
						fnd = pForm;
					} else {
						fnd = tForm;
					}
					
					continue;
				} 				
				
				throw new RuntimeException("Multiple opcode match "+co.originalText);
			}
						
			fnd = op;
			
		}
		
		if(fnd==null) {
			throw new ASMException("Unknown mnemonic "+co.originalText,co);
		}
		
		// First pass there is no need to calculate the real data ... just
		// a placeholder.
		if(firstPass) {
			co.data = new ArrayList<Integer>();
			for(int x=0;x<fnd.code.length()/2;++x) {
				co.data.add(0);				
			}
			return co.data.size();
		}
		
		if(fnd.code.endsWith("rr")) {
			int ofs = co.address+fnd.code.length()/2; // This is the address of the next opcode
			ofs = value-ofs; // Now relative
			if(ofs<-128 || ofs>127) {
				throw new ASMException("Destination is too far away",co);
			}
			if(ofs<0) ofs=ofs+256;
			value = ofs;
		}
		
		co.data.clear();
		co.data.add(Integer.parseInt(fnd.code.substring(0,2),16));
		if(fnd.code.length()==4) {
			if(value>255) {
				throw new ASMException("Value does not fit in a byte",co);
			}
			co.data.add(value);
		} else if(fnd.code.length()==6) {
			co.data.add(value&0xFF);
			co.data.add((value>>8)&0xFF);			
		} else if(fnd.code.length()!=2) {			
			System.out.println(fnd.code);
			throw new RuntimeException("OOPS");
		}
		
		System.out.println(CU.hex4(co.address)+":"+co.data.size());
		return co.data.size();
	}
		
	@Override
	public AddressAccess getAccess(String opcode, int numPos, int num, int directPage) {
		
		if(opcode.charAt(numPos-1)=='#') {
			// Immediate constant
			return null;
		}
		
		if(opcode.contains(",")) {
			// Index forms
			return null;
		}
		
		AddressAccess ret = new AddressAccess();
		ret.address = num;
		ret.bus = BusDir.BOTH;
		ret.accessType = BusType.MAIN;
				
		if(opcode.startsWith("B") || opcode.startsWith("J")) {
			// This is a code reference (a flow branch)		
			ret.isCode = true;			
			return ret;
		}				
				
		if(opcode.startsWith("LD")) {
			ret.bus = BusDir.READ;
		} else if(opcode.startsWith("ST")) {
			ret.bus = BusDir.WRITE;
		} else {
			ret.bus = BusDir.BOTH;
		}
				
		return ret;
	}
		
}
