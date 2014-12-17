package tools.assembler;

import java.util.ArrayList;
import java.util.List;

import tools.processor.Opcode;

/**
 * This Opcode implementation holds variable length data runs defined
 * in an assembly program.
 */
public class DataOpcode extends Opcode {
	
	public DataOpcode() 
	{
		super(null, null, null, null, null, null);		
	}

	public List<String> values = new ArrayList<String>();
	public List<Integer> sizes = new ArrayList<Integer>();
	
	public int getOpcodeSize() {
		int ret = 0;
		for(int i : sizes) ret=ret+i;
		return ret;
	}

}
