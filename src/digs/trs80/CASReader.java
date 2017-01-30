package digs.trs80;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;

import code.CU;

public class CASReader {

	public static void main(String[] args) throws Exception {
		
		// Looks like hauntORG has a couple of file loads in it. Looks like the game loads
		// its second half over the first.
		
		InputStream is = new FileInputStream("hauntORG.cas");
		int [] data = new int[is.available()];
		for(int x=0;x<data.length;++x) {
			data[x] = is.read();
		}
		is.close();
		
		OutputStream os = new FileOutputStream("haunt.bin");
		int pos = 0x0106;
		int datpos = 0x42E9;
		
		for(int z=0;z<14;++z) {
			System.out.print(CU.hex4(pos)+"("+CU.hex4(datpos)+"): ");
			for(int x=0;x<5;++x) {
				System.out.print(CU.hex2(data[pos++])+" ");
			}
			System.out.println();
			
			for(int y=0;y<0x100;++y) {
				os.write(data[pos+y]);
			}
			
			pos = pos + 0x100;
			datpos = datpos+0x100;
		}
		
		/*
		pos = 0x0F81;
		for(int z=0;z<12;++z) {
			System.out.print(CU.hex4(pos)+"("+CU.hex4(datpos)+"): ");
			for(int x=0;x<5;++x) {
				System.out.print(CU.hex2(data[pos++])+" ");
			}
			System.out.println();
			
			pos = pos + 0x100;
			datpos = datpos+0x100;
		}
		*/
		
		//pos = 0x1ABD;
		
		os.flush();
		os.close();

	}

}
