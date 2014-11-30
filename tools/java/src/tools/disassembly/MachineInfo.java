package tools.disassembly;

import java.util.StringTokenizer;

import tools.code.CU;

/**
 * This class encapsulates all the information about a machine
 * including the CPU type and memory map.
 */
public class MachineInfo 
{
	
	private String cpuType;
	private String [] asTypes;
	private int romStart;
	private int romEnd;
	private int ramStart;
	private int ramEnd;
	private String originalBinary;
	private int [] printSpacing;
	private String patchOutput;
	private int currentBasePageOffset;
	
	public String getPatchOutput() {
		return patchOutput;
	}
	
	public String getOriginalBinary() {
		return originalBinary;
	}
	
	public int getRomStart() {
		return romStart;
	}

	public int getRomEnd() {
		return romEnd;
	}

	public int getRamStart() {
		return ramStart;
	}

	public int getRamEnd() {
		return ramEnd;
	}

	public String getCpuType() {
		return cpuType;
	}
	
	public String [] getAsTypes() {
		return asTypes;
	}
	
	public int [] getPrintSpacing() {
		return printSpacing;
	}

	public void parseInfo(String comment) {		
		String cup = comment.toUpperCase();
		if(cup.startsWith("CPU")) {
			cpuType = comment.substring(3).trim();
			int i = cpuType.toUpperCase().indexOf(" AS ");
			if(i>=0) {
				StringTokenizer st = new StringTokenizer(cpuType.substring(i+4),",");
				asTypes = new String[st.countTokens()];
				for(int j=0;j<asTypes.length;++j) {
					asTypes[j] = st.nextToken();
				}
				cpuType = cpuType.substring(0,i);
			} 
		} else if(cup.startsWith("ROM")) {
			String s = comment.substring(3).trim();
			int i = s.indexOf("-");
			romStart = Integer.parseInt(s.substring(0,i).trim(),16);
			romEnd = Integer.parseInt(s.substring(i+1).trim(),16);
		} else if(cup.startsWith("RAM")) {
			String s = comment.substring(3).trim();
			int i = s.indexOf("-");
			ramStart = Integer.parseInt(s.substring(0,i).trim(),16);
			ramEnd = Integer.parseInt(s.substring(i+1).trim(),16);
		} else if(cup.startsWith("ORIGINALBINARY")) {
			originalBinary = comment.substring(14).trim();
		} else if(cup.startsWith("PRINTSPACING")) {
			String s = comment.substring(12).trim();
			int i = s.indexOf(" ");
			printSpacing = new int[2];
			printSpacing[0] = Integer.parseInt(s.substring(0,i));
			printSpacing[1] = Integer.parseInt(s.substring(i+1).trim());
		} else if(cup.startsWith("PATCHOUTPUT")) {
			patchOutput = comment.substring(11).trim();
		} else if(cup.startsWith("BASEPAGE")) {
			currentBasePageOffset = CU.parseIntValue(cup.substring(8).trim());
		}
		
		else {
			throw new RuntimeException("Unknown Machine info '"+comment+"'");
		}
	}

	public int getCurrentBasePageOffset() {
		return currentBasePageOffset;
	}

	public void setCurrentBasePageOffset(int currentBasePageOffset) {
		this.currentBasePageOffset = currentBasePageOffset;
	}

	

}
