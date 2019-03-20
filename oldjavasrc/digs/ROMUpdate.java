package digs;

import util.CU;
import util.FU;

public class ROMUpdate {
	
	static void bitswap(int [] data, String pattern) {	
		for(int x=0;x<data.length;++x) {
			int a = data[x];
			String aa = Integer.toString(a,2);
			while(aa.length()<8) aa="0"+aa;
			String bb = "";
			for(int y=0;y<8;++y) {
				int bn = pattern.charAt(y)-'0';
				bb = bb+aa.charAt(7-bn);
			}
			data[x] = Integer.parseInt(bb,2);
		}
	}
	
	static String[] getTile(int number, int[] f1, int[] f2) {
		String [] ret = new String[8];
		
		for(int y=0;y<8;++y) {
			ret[y] = "";
			int pos = 0x80;
			for(int x=0;x<8;++x) {
				int a = f1[number*8+y]&pos;
				int b = f2[number*8+y]&pos;
				pos = pos >> 1;
				int v = 0;
				if(a!=0) v = v + 1;
				if(b!=0) v = v + 2;
				ret[y] = ret[y] + v;
			}
		}		
		
		return ret;
	}
	
	
	public static String[] rotate(String[] tile) {
		String[] ret = new String[8];		
		return ret;
	}
	

	public static void main(String[] args) throws Exception {
		
		int [] f1 = FU.readBinary("content/arcade/frogger/roms/frogger.607");
		int [] f2 = FU.readBinary("content/arcade/frogger/roms/frogger.606");		
		bitswap(f2,"76543201");
		
		// Slots are divided into two banks. First 8 bytes is "0".
		// Two bits per pixel. One from each bank. Upper bit is the top row.
		
		// Monitor is rotated
		
		/*		
		String[] tile = getTile(1,f1,f2);
		for(String s : tile) {
			System.out.println(s);
		}
		*/
		
		int addr = 0;
		
		for(addr=0;addr<0x1000;++addr) {
			int v;
			if(addr<0x800) {
				v = f1[addr];
			} else {
				v = f2[addr-0x800];
			}
			if(addr%16 == 0) {
				System.out.println();
				System.out.print(CU.hex4(addr)+":");				
			}
			
			System.out.print(" "+CU.hex2(v));
			
		}
						
		/*
		bitswap(f2,"76543201");
		FU.writeBinary(f1,"d:/mame/roms/frogger/frogger.607");
		FU.writeBinary(f2,"d:/mame/roms/frogger/frogger.606");
		*/

	}

}
