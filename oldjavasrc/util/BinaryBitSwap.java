package util;

import java.io.FileInputStream;
import java.io.FileOutputStream;

/**
 * This class performs the bit-swapping for eprom chips that have data
 * lines swapped.
 */
public class BinaryBitSwap {
	
	public static void main(String [] args) throws Exception
	{
		// 76543210
		FileInputStream fis = new FileInputStream(args[0]);
		FileOutputStream fos = new FileOutputStream(args[1]);
		String swap = args[2];
		while(fis.available()>0) {
			int a = fis.read();
			a = doSwap(a,swap);
			fos.write(a);
		}
		fis.close();
		fos.flush();
		fos.close();
	}
	
	public static int doSwap(int value, String pattern) {
		String a = Integer.toString(value,2);
		while(a.length()<8) a="0"+a;
		byte [] d = new byte[8];
		for(int x=0;x<8;++x) {
			int bp = pattern.charAt(x)-'0';
			bp = 7-bp;
			d[x] = (byte)a.charAt(bp);
		}
		a = new String(d);
		return Integer.parseInt(a,2);
	}

}
