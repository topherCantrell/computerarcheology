package util;

import java.io.FileInputStream;
import java.io.IOException;

public class Diff {

	public static void main(String[] args) throws IOException {
		
		byte [] a = new byte[16384];
		byte [] b = new byte[16384];
		
		FileInputStream fisa = new FileInputStream("content/arcade/galaga/CPU1.bin");
		fisa.read(a);
		
		FileInputStream fisb = new FileInputStream("content/arcade/galaga/CPU1Fix.bin");
		fisb.read(b);
		
		System.out.println("HERE");
		for(int x=0;x<16384;++x) {
			if(a[x] != b[x]) System.out.println("Different at "+CU.hex4(x));
		}
		
		
	}

}
