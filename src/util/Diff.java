package util;

import java.io.FileInputStream;
import java.io.IOException;

public class Diff {

	public static void main(String[] args) throws IOException {
		
		byte [] a = new byte[2048];
		byte [] b = new byte[2048];
		
		FileInputStream fisa = new FileInputStream("content/atari2600/combat/combat.bin");
		fisa.read(a);
		
		FileInputStream fisb = new FileInputStream("content/atari2600/combat/combatPAL.bin");
		fisb.read(b);
		
		for(int x=0;x<2048;++x) {
			if(a[x] == b[x]) System.out.println("Same at "+CU.hex4(x));
		}
		
		
	}

}
