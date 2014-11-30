package tools.file;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

/**
 * This class encapsulates the data from a binary file and the dissassembly text that
 * goes with it.
 */
public class BinTextPair {
	
	public int [] data;
	public int origin;
	public List<String> lines = new ArrayList<String>();
	
	/**
	 * This constructs a new BinTextPair and loads the data from the two files.
	 * @param textName name of the text disassembly file
	 * @param origin the origin of the binary file
	 * @param binName the name of the binary file
	 * @throws IOException if something goes wrong reading the files
	 */
	public BinTextPair(String textName, int origin, String binName) throws IOException {
		
		this.origin = origin;
		
		FileReader fr = new FileReader(textName);
		BufferedReader br = new BufferedReader(fr);
		while(true) {
			String g = br.readLine();
			if(g==null) break;
			lines.add(g);
		}
		fr.close();
		
		InputStream is = new FileInputStream(binName);
		data = new int[is.available()];
		for(int x=0;x<data.length;++x) {
			data[x] = is.read();
		}
		is.close();
				
	}
	

}
