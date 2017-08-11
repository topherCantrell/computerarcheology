package files;

import java.io.FileInputStream;

public class Propeller {
	
	public static void main(String [] args) throws Exception {
		
		FileInputStream fis = new FileInputStream("content/Atari2600/Combat/Combat.bin");
		int [] data = new int[fis.available()];
		for(int x=0;x<data.length;++x) {
			data[x] = fis.read();
		}
		fis.close();
		
		for(int x=0;x<data.length/16;++x) {
			System.out.print("    byte ");
			for(int y=0;y<16;++y) {
				String s = Integer.toString(data[x*16+y],16).toUpperCase();
				while(s.length()<2) s="0"+s;
				if(y<15) {
					System.out.print("$"+s+", ");
				} else {
					System.out.print("$"+s);
				}
			}
			System.out.println();
		}
		
		
		
	}

}
