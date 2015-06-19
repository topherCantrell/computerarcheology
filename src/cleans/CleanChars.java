package cleans;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.List;

public class CleanChars {
	
	public static void main(String [] args) throws Exception {
		
		String fname = "content/Arcade/SpaceInvaders/SpaceInvaders.mark";
		
		InputStream is = new FileInputStream(fname);
		int [] data = new int[is.available()];
		for(int x=0;x<data.length;++x) {
			data[x] = is.read();
		}
		is.close();
		
		List<Integer> newData = new ArrayList<Integer>();
		for(int x=0;x<data.length;++x) {
			//System.out.println(data[x]);
			if(data[x]>127) {
				if(data[x]==0xE2 && data[x+1]==0x80) {
					switch(data[x+2]) {
					case 0x9C:
						newData.add((int) '"');
						break;
					case 0x9D:
						newData.add((int) '"');
						break;
					case 0x93:
						newData.add((int) '"');
						break;
					case 0xA6:
						newData.add((int) '"');
						break;
					case 0x98:
						newData.add((int) '"');
						break;
					case 0x99:
						newData.add((int) '"');
						break;
					default:
						throw new Exception("Unknown "+data[x+2]);
					}
					x = x + 2;
				} else {
					throw new Exception("Unknown "+data[x]);
				}				
			} else {
				newData.add(data[x]);
			}
		}		
		
		OutputStream os = new FileOutputStream("New.mark");
		for(int i : newData) {
			os.write(i);
		}
		os.flush();
		os.close();
		
	}

}
