package cleans;

import java.io.FileInputStream;
import java.io.InputStream;
import java.util.List;

import code.CU;
import sim.DissReader;

public class CompareBinary {
	
	public static void main(String [] args) throws Exception {
		
		DissReader diss = new DissReader("content/TRS80/HauntedHouse/Code2.cmark");		
		List<Integer> data = diss.getData();
		
		InputStream is = new FileInputStream("content/TRS80/HauntedHouse/Code2.bin");
		if(is.available()!=data.size()) {
			throw new RuntimeException("SIZE");
		}
		
		int pos = 0;
		for(int i : data) {
			if(i!=is.read()) {				
				throw new RuntimeException("MISMATCH "+CU.hex4(pos));
			}
			++pos;
		}
		
		
		
		
		
		
		// Extract data from disassembly
		// Extract binary
		
		// compare
		
	}

}
