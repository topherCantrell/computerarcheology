package tools.processor;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

import org.jdom.Element;

import tools.code.CU;
import tools.processor.Indexed6809;

/**
 * The 6809 has an extensive indexed addressing mode. Indexed instructions have a post-fix byte
 * that describes additional opcode bytes and mnemonic representation. It is impractical to
 * spell all of these combinations out in the processor file. Instead we'll list the post-fix
 * byte in a separate table and then expand the slew of opcodes here ... with code.
 */
public class Processor_6809 extends Processor 
{
	
	// List of parsed 6809 indexed modes
	private List<Indexed6809> indexeds = new ArrayList<Indexed6809>();	
	
	@SuppressWarnings("unchecked")
	public Processor_6809(ProcessorFamily family, Element info, Element familyInfo) {
		
		
		// The base stuff
		super(family,info,familyInfo);
		
		// Parse the indexed mode info from the XML
		List<Element> inds = familyInfo.getChild("indexed").getChildren();
		for(Element ind : inds) {
			Indexed6809 i = new Indexed6809();
			indexeds.add(i);
			i.code = ind.getAttributeValue("code");
			i.m6809 = ind.getAttributeValue("m6809");
			i.clocks = ind.getAttributeValue("clocks");
		}
		
		// For now we'll expand the indexed opcodes into the master list
		for(int x=opcodes.size()-1;x>=0;--x) {
			Opcode op = opcodes.get(x);
			String co = op.getCode();
			if(co.contains("yy")) {
				opcodes.remove(x);
				for(Indexed6809 i : indexeds) {
					
					// Replace the "yy" with the postfix value. This likely extends the
					// opcode with other bytes and fill-ins.
					String nc = CU.replaceAll(co, "yy", i.code);
					
					// TODO the indexed mode affects these values.
					String nclocks = op.getClocks();
					String nflags = op.getFlags();
					String nbus = op.getBus();					
					
					// The existing mnemonic for 6809 has a "y" in it. Replace that with the new
					// mnemonic fill-in.
					Mnemonic nm = op.getMnemonics().get("6809");
					String rep = nm.getTextRepresentations()[0];
					rep = CU.replaceAll(rep, "y", i.m6809);										
					
					Map<String,String> nms = new HashMap<String,String>();
					nms.put("6809", rep);
					
					// Create the new opcode for 6809
					Opcode no = new Opcode(this,nc,
							nclocks,nflags,nbus,
							nms);
					
					opcodes.add(no);
												
				}
			}
		}
	}	
		
	static final String [] regs = {"D","X","Y","U","S","PC","?","?","A","B","CCR","DP","?","?" ,"?","?"};	
	static final String [] stackOrder = {"CC","A","B","DP","X","Y","*","PC"};	
	
	@Override
	public String preprocessOpcode(String comp, List<Integer> starts)
	{
		if(comp.startsWith("TFR ") || comp.startsWith("EXG ")) {
			if(comp.length()<7) return comp; // Invalid
			String left = comp.substring(4,5);
			String right = comp.substring(6,7);
			int ln = -1;
			for(int x=0;x<regs.length;++x) {
				if(regs[x].equals(left)) {
					ln = x;
					break;
				}
			}
			int rn = -1;
			for(int x=0;x<regs.length;++x) {
				if(regs[x].equals(right)) {
					rn = x;
					break;
				}
			}
			if(ln<0 || rn<0) return comp; // Invalid
			ln = (ln<<4) | rn;
			comp = comp.substring(0,4)+ln;
			
		} 
		
		else if(comp.startsWith("PULS ") || comp.startsWith("PULU") || comp.startsWith("PSHS ") || comp.startsWith("PSHU")) {			
			if(comp.length()<6) return comp; // Invalid
			String which = comp.substring(3,4);
			int val = 0;
			StringTokenizer st = new StringTokenizer(comp.substring(5),",");
			while(st.hasMoreElements()) {
				String reg = st.nextToken();
				if(reg.equals(which)) reg="*";
				int rn = -1;
				for(int x=0;x<stackOrder.length;++x) {
					if(stackOrder[x].equals(reg)) {
						rn = x;
						break;
					}
				}
				if(rn<0) return comp; // Invalid
				
				val = val | (int)Math.pow(2, rn);
			}
			comp = comp.substring(0,5)+val;			
		} 
		
		// TODO just for now
		while(starts.size()<comp.length()) starts.add(0);
		
		return comp;
	}

}
