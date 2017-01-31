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
		
		// 42E9
		
		InputStream is = new FileInputStream("haunt.cas");
		int [] data = new int[is.available()];
		for(int x=0;x<data.length;++x) {
			data[x] = is.read();
		}
		is.close();
		
		OutputStream os = new FileOutputStream("haunt1.bin");
		int pos = 0x0106;		
		
		for(int z=0;z<14;++z) {
			System.out.print(CU.hex4(pos)+": ");
			for(int x=0;x<5;++x) {
				System.out.print(CU.hex2(data[pos++])+" ");
			}
			System.out.println();
			
			for(int y=0;y<0x100;++y) {
				os.write(data[pos+y]);
			}
			
			pos = pos + 0x100;
		}
		
		while(pos<data.length) {
			os.write(data[pos++]);
		}
				
		os.flush();
		os.close();

	}
	
	public static void main2(String[] args) throws Exception {
		
		// Looks like hauntORG has a couple of file loads in it. Looks like the game loads
		// its second half over the first.
		
		// 435E
		
		InputStream is = new FileInputStream("haunt.cas");
		int [] data = new int[is.available()];
		for(int x=0;x<data.length;++x) {
			data[x] = is.read();
		}
		is.close();
		
		OutputStream os = new FileOutputStream("haunt2.bin");
		int pos = 0x0F81;		
		
		for(int z=0;z<11;++z) {
			System.out.print(CU.hex4(pos)+": ");
			for(int x=0;x<5;++x) {
				System.out.print(CU.hex2(data[pos++])+" ");
			}
			System.out.println();
			
			for(int y=0;y<0x100;++y) {
				os.write(data[pos+y]);
			}
			
			pos = pos + 0x100;			
		}
		
		while(pos<data.length) {
			os.write(data[pos++]);
		}
				
		os.flush();
		os.close();
		
	}

}
