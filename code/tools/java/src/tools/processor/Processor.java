package tools.processor;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.jdom.Attribute;
import org.jdom.Element;

import tools.code.CU;
import tools.code.OpcodeParameterInfo;


/**
 * This class encapsulates all the information about a single processor. This
 * is the base information for specific CPUs defined in "ProcessorCPU.java"
 * files where CPU is the processor's name.
 */
public class Processor {

	protected String name;
			
	protected ProcessorFamily family;
	
	protected List<Opcode> opcodes = new ArrayList<Opcode>();
			
	/**
	 * This parses the generic processor info common to all processors.
	 * @param family the processor's family
	 * @param info the processor's info structure
	 * @param familyInfo the XML element for the family (might be some processor-specifics in there)
	 */
	public Processor(ProcessorFamily family, Element info, Element familyInfo) 
	{
		this.family = family;
		this.name = info.getAttributeValue("name");				
		
		// The opcode-parsing is separated out in case it needs to be overriden by the specific 
		// processor class.
		parseProcessorOpcodes(familyInfo);
						
	}
	
	/**
	 * This method parses the processor's opcode list from the family's master list of opcodes.
	 * If the family opcode belongs with this processor then the XML entry will have a "mCPU"
	 * attribute with the mnemonic text. This is just the "default" behavior, or course.
	 * Specific processors may use the family XML how ever they want.
	 * @param familyInfo
	 */
	@SuppressWarnings("unchecked")
	protected void parseProcessorOpcodes(Element familyInfo)
	{
		
		List<Element> ops = familyInfo.getChild("opcodes").getChildren("op");
		for(Element ope : ops) {	
			
			// Extract the map of all mnemonic sets.
			Map<String,String> mnemonicTexts = new HashMap<String,String>();
			List<Attribute> atts = ope.getAttributes();
			for(Attribute a : atts) {
				if(a.getName().startsWith("m")) {
					mnemonicTexts.put(a.getName().substring(1), a.getValue());					
				}
			}
			
			// Ignore all family opcodes that are not included in this processor.
			if(mnemonicTexts.get(name)==null) continue;
			
			// Add the opcode to the processor
			Opcode op = new Opcode(this,
					ope.getAttributeValue("code"),
					ope.getAttributeValue("clocks"),
					ope.getAttributeValue("flags"),
					ope.getAttributeValue("bus"),
					mnemonicTexts
					);			
			opcodes.add(op);
			
		}

	}
	
	/**
	 * This method looks at the processor's opcode list and returns all that potentially
	 * match the given binary stream. A disassembler would call this method with longer
	 * and longer binary streams until just one (or none) opcodes match. 
	 * 
	 * This really belongs in a processor-specific disassembler implementation, but for
	 * simplicity we will keep it here.
	 * 
	 * @param binary the array of binary data
	 * @param start the starting point of the binary stream to decode
	 * @param length the number of bytes in the stream
	 * @return the list of opcodes that match the stream
	 */
	public List<Opcode> findPossibleOpcodes(int [] binary, int start, int length) 
	{
		
		List<Opcode> ret = new ArrayList<Opcode>();
		
		// Brutal string searching here. We could convert the opcode "code" to
		// numbers for faster searches. But this works.
		
		// Convert the binary stream to a string of 2-digit hex bytes.
		String pos = "";
		for(int x=0;x<length;++x) {
			pos = pos + CU.twoDigitHex(binary[start+x]);
		}
				
		for(Opcode op : opcodes) {
			String p = op.getCode();			
			// We shouldn't get here, but if the binary stream is longer than the opcode
			// stream then it doesn't match ... even if the opcode is completely in the
			// binary stream.
			if(p.length()<pos.length()) continue;
			boolean match = true;
			for(int x=0;x<pos.length();++x) {
				// Numeric fill-ins in the opcode match anything
				if(p.charAt(x)>='a' && p.charAt(x)<='z') continue;
				if(p.charAt(x)!=pos.charAt(x)) {
					match = false;
					break;
				}
			}
			if(match) ret.add(op);			
		}
		
		return ret;
	}
	
	public ProcessorFamily getFamily() { return family; }

	public String getName() {		
		return name;
	}
	
	public String preprocessOpcode(String comp, List<Integer> starts)
	{
		return comp;
	}

	/**
	 * This method finds the opcode for the given mnemonic text string. This is the core work
	 * of assembly a program from an input file. The method is here so it can be overridden
	 * with processor-specifics if needed.
	 * @param comp the input line with defines substituted in and extraneous white-space collapsed
	 * @param params a return map containing fill-in data for the second pass
	 * @param as a list of mnemonic sets to use (or null to use all in the family)
	 * @return the opcode or null if no match (the dataMap is also a return)
	 */
	public Opcode findOpcode(String comp, Map<String, OpcodeParameterInfo> params, List<String> as) 
	{
		
		List<Integer> starts = new ArrayList<Integer>();
		comp = CU.removeWhiteSpace(comp,starts);

		// 6809 turns lists of registers like "A,B,CC,PC" into a single byte
		comp = preprocessOpcode(comp,starts);

		// The default implementation is to return the first opcode that matches. If you use this
		// default implementation then you must organize the processor XML to prioritize the opcodes.
		
		List<Opcode> opMatches = new ArrayList<Opcode>();
		List<Map<String,OpcodeParameterInfo>> opMatchInfo = new ArrayList<Map<String,OpcodeParameterInfo>>();
		List<Integer> opMatchTokens = new ArrayList<Integer>();
		
		// Run the opcodes in the processor
		for(Opcode op : opcodes) {

			// Run the list of mnemonics for this opcode
			Map<String,Mnemonic> mnems = op.getMnemonics();
			for(String mkey : mnems.keySet()) {

				// If the user has given a list of mnemonic-sets then ignore this set if
				// it is not in the list.
				if(as!=null && !as.contains(mkey)) continue;

				Mnemonic mnem = mnems.get(mkey);

				// Run all the possible representations for the mnemonic
				List<List<MnemonicParseToken>> tokenLists = mnem.getParseTokens();				
				for(int x=0;x<tokenLists.size();++x) {					
					List<MnemonicParseToken> parseTokens = tokenLists.get(x);
					Map<String,OpcodeParameterInfo> info = new HashMap<String,OpcodeParameterInfo>();
					if(matchTokens(comp,starts,parseTokens,info)) {
						opMatches.add(op);
						opMatchInfo.add(info);
						opMatchTokens.add(parseTokens.size());																
					}					 
				}

			}			
		}		
		
		if(opMatches.size()==0) {
			// Nothing matched
			return null;
		}
		
		/*
		if(opMatches.size()>1) {			
			//System.out.println("Multiple opcode matches");
			//return null;
		}
		*/		

		// Match
		params.clear();
		params.putAll(opMatchInfo.get(0));
		return opMatches.get(0);
	}	

	// This method runs a list of tokens against the input string and looks for a match. Along the way
	// we note any fill-in values for the next compile pass.
	private boolean matchTokens(String comp, List<Integer> starts, List<MnemonicParseToken> parseTokens, Map<String, OpcodeParameterInfo> params) 
	{
		
		// This is a return value. Make sure nothing is in it.
		params.clear();
		
		int compPos = 0;
								
		// Run the tokens
		for(MnemonicParseToken token : parseTokens) {
			
			// If there is a token but nothing left in the string then it doesn't match
			if(comp.length()==0) return false;
			
			if(token.tokenType==MnemonicParseToken.TYPE.MATCH) {
				if(!comp.toUpperCase().startsWith(token.text)) {
					return false;
				}
				// Straight match ... just chop it off the string
				compPos += token.text.length();
				comp = comp.substring(token.text.length());				
			} else { // Must be a numeric fill-in
				int i = CU.findEndOfExpression(comp, 0);
				String t = comp.substring(0,i);
				OpcodeParameterInfo info = new OpcodeParameterInfo();
				info.value = t;
				info.paramName = ""+token.text.charAt(0);				
				info.startInText = starts.get(compPos);
				info.endInText = starts.get(compPos+i-1);								
				params.put(info.paramName,info);
				compPos+=i;
				comp = comp.substring(i);				
			}
		}
		
		// If the string has no more tokens either then we found a match
		if(comp.length()==0) return true;		
		
		// String has more stuff in it ... can't be a match
		return false;
	}
	
}
