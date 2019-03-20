package tools.processor;

import java.util.HashMap;
import java.util.Map;

import tools.code.CU;

/**
 * An opcode represents a CPU instruction for a given target processor. Fundamentally, the opcode
 * is a sequence of bytes with possible numeric fill-ins. There are also various mnemonic (human
 * readable) representations of the opcode that also contain the numeric fill-ins.
 * 
 * Fill-ins are single-lower-case-letters. In the "code" representation these letters are followed
 * by a "m" or "l" for "most significant" and "least significant" where appropriate.
 * 
 * For example:
 * <op code="10B3tmtl" m6809="CMPD t" clocks="8" flags="-aaaa" mCish="D-t" />
 * 
 * The letters are all described in OpcodeParamField.
 * 
 * The assembler may create "dynamic" opcodes to represent data strings. In this case the created
 * opcode will have no mnemonics or other attributes ... just code with no fill-ins.
 */

public class Opcode {
	
	private Processor processor;
	private String code;
	private String clocks;
	private String flags;
	private String bus;	
	private Map<String,Mnemonic> mnemonics = new HashMap<String,Mnemonic>();	
	
	/**
	 * This constructs a new opcode.
	 * @param processor backwards link to the owning processor
	 * @param code the code bytes of the opcode as hex bytes and lower-case-letter fill-ins
	 * @param clocks information about the number of clocks the opcode takes
	 * @param flags information about the flags this opcode affects
	 * @param bus information about the address/data bus access of this opcode
	 * @param mnemonicTexts all the various mnemonic representations of this opcode
	 */
	public Opcode(Processor processor, String code, String clocks, String flags, String bus,
			Map<String,String> mnemonicTexts)
	{
		this.processor = processor;
		this.code = code;
		this.clocks = clocks;
		this.flags = flags;
		this.bus = bus;
		if(mnemonicTexts!=null) { // There are dynamic entries created for data
			for(String key : mnemonicTexts.keySet()) {
				mnemonics.put(key, new Mnemonic(mnemonicTexts.get(key)));
			}
		}
	}
	
	/**
	 * This method maps the given data bytes into parameter-field values. This is used by
	 * a disassembly process to map existing bytes back into their mnemonic fill-in
	 * locations.
	 * @param data the data to map into the opcode
	 * @return the map of opcode-field to data-value
	 */
	public Map<OpcodeParamField,String> decodeData(int [] data) {
		Map<OpcodeParamField,String> ret = new HashMap<OpcodeParamField,String>();
		for(int x=0;x<code.length();x=x+2) {
			char a = code.charAt(x);
			// Code substitutions are always lower-case letters (two of them)
			if(a>='a' && a<='z') {
				char b = code.charAt(x+1); // Second letter could be byte-ordering
				String cv = ret.get(OpcodeParamField.getParamField(a));
				String nv = CU.twoDigitHex(data[x/2]); 
				if(cv==null) {
					// There is no existing value ... this is a one-byte value
					ret.put(OpcodeParamField.getParamField(a), nv);
				} else {
					// There was a previous value. Stick the new value on the front or back
					if(b=='l') {
						// The new value is the back
						ret.put(OpcodeParamField.getParamField(a), cv+nv);
					} else {
						// 'm' The new value is the front
						ret.put(OpcodeParamField.getParamField(a), nv+cv);
					}
				}
			}					
		}		
		return ret;
	}
		
	/**
	 * This method returns the number of bytes occupied by the opcode.
	 * @return byte-size of the opcode
	 */
	public int getOpcodeSize() {
		return code.length()/2;
	}	
	
	public Processor getProcessor() { return processor; }
	public String getCode() { return code; }
	public String getClocks() { return clocks; }	
	public String getFlags() { return flags; }	
	public String getBus() { return bus; }
	public Map<String,Mnemonic> getMnemonics() { return mnemonics; }
	
}
