package diss.cpu;

import java.util.Map;

import cpu.CPU;
import cpu.Opcode;
import util.BinaryFiles;

public class DissCPU_6809 extends DissCPU {
	
	public DissCPU_6809() {
		cpu = CPU.getCPU("6809");
	}
	
	@Override
	public void fillin(Opcode op, BinaryFiles files, int addr, Map<String, Object> fillins) {
		super.fillin(op, files, addr, fillins);
		
		// TFR
		
		// PSHU
		// PULU		
		
		//               7    6   5   4                0
		String [] PS = {"PC","U","Y","X","DP","B","A","CC"};
		// PUSH ORDER ->
		// PULL ORDER <-	
		
		//               7    6   5   4                0
		String [] PU = {"PC","S","Y","X","DP","B","A","CC"};
		// PUSH ORDER ->
		// PULL ORDER <-
		
		String [] TXFR = {"D","X","Y", "U", "SP","PC","?","?",
				          "A","B","CC","DP","?", "?", "?","?"};
		
		if(op.mnemonic.startsWith("PSHS ")) {			
			String v = (String) fillins.get("wordB");
			int pshs = Integer.parseInt(v.substring(1),16);			
			String rep = "";
			for(int i=128, p=0;i>0;i=i>>1,++p) {
				if((i&pshs)!=0) {
					rep = rep + PS[p]+",";
				}
			}		
			if(rep.endsWith(",")) {
				fillins.put("wordB", rep.substring(0, rep.length()-1));
			}
		}
		
		if(op.mnemonic.startsWith("PULS ")) {		
			String v = (String) fillins.get("wordB");
			int pshs = Integer.parseInt(v.substring(1),16);			
			String rep = "";
			for(int i=1, p=7;i<256;i=i<<1,--p) {
				if((i&pshs)!=0) {
					rep = rep + PS[p]+",";
				}
			}		
			if(rep.endsWith(",")) {
				fillins.put("wordB", rep.substring(0, rep.length()-1));
			}
		}
		
		if(op.mnemonic.startsWith("PSHU ")) {		
			String v = (String) fillins.get("wordB");
			int pshs = Integer.parseInt(v.substring(1),16);			
			String rep = "";
			for(int i=128, p=0;i>0;i=i>>1,++p) {
				if((i&pshs)!=0) {
					rep = rep + PU[p]+",";
				}
			}		
			if(rep.endsWith(",")) {
				fillins.put("wordB", rep.substring(0, rep.length()-1));
			}
		}
		
		if(op.mnemonic.startsWith("PULU ")) {		
			String v = (String) fillins.get("wordB");
			int pshs = Integer.parseInt(v.substring(1),16);			
			String rep = "";
			for(int i=1, p=7;i<256;i=i<<1,--p) {
				if((i&pshs)!=0) {
					rep = rep + PU[p]+",";
				}
			}		
			if(rep.endsWith(",")) {
				fillins.put("wordB", rep.substring(0, rep.length()-1));
			}
		}
		
		if(op.mnemonic.startsWith("TFR ")) {		
			String v = (String) fillins.get("wordB");
			int tf = Integer.parseInt(v.substring(1),16);
			int r1 = tf/16;
			int r2 = tf%16;
			String rep = TXFR[r1]+","+TXFR[r2];
			fillins.put("wordB", rep);
		}
		
	}

}
