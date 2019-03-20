package cleans;

import util.FU;

public class GFX {
	
	static void print8x8(int[]data, int pos) {
		for(int x=0;x<8;++x) {
			String a = Integer.toString(data[pos+x],2);
			while(a.length()<8) a="0"+a;
			a.replace('0', '_');
			a.replace('1', '*');
			System.out.println(a);
		}
	}

	public static void main(String[] args) throws Exception {
		
		int [] data = FU.readBinary("content/arcade/frogger/roms/frogger.607","content/arcade/frogger/roms/frogger.606");
		
		for(int x=0;x<10;++x) {
			print8x8(data,x*8);
			System.out.println("");
		}
		

	}

}
