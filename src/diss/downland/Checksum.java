package diss.downland;

import java.io.FileInputStream;

public class Checksum {

	public static void main(String[] args) throws Exception {
		
		FileInputStream fis = new FileInputStream("content/CoCo/Downland/downland.bin");
		
		int sum = 0;
		for(int x=0;x<0x2000;++x) {
			sum = sum + fis.read();
		}
		
		System.out.println(sum);

	}

}
