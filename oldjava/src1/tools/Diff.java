package tools;

import java.io.FileInputStream;
import java.io.IOException;

import tools.code.CU;

/**
 * This tool is a simple binary file diff.
 */
public class Diff {
		
	/**
	 * This function performs the diff of two files.
	 * @param args the files
	 * @throws IOException error reading files
	 */
	public static void main(String [] args) throws IOException
	{
		
		int ofsA = 0;
		int ofsB = 0;
		
		String fnA = args[0];
		String fnB = args[1];
		
		if(fnA.startsWith("+")) {
			int i = fnA.indexOf(":");
			ofsA = Integer.parseInt(fnA.substring(1,i),16);
			fnA = fnA.substring(i+1);
		}
		
		if(fnB.startsWith("+")) {
			int i = fnB.indexOf(":");
			ofsB = Integer.parseInt(fnB.substring(1,i),16);
			fnB = fnB.substring(i+1);
		}
		
		FileInputStream fA = new FileInputStream(fnA);
		FileInputStream fB = new FileInputStream(fnB);
		
		for(int x=0;x<ofsA;++x) {
			fA.read();
		}
		for(int x=0;x<ofsB;++x) {
			fB.read();
		}
		
		if(fA.available()!=fB.available()) {
			System.out.println("Sizes are different.");
		}
		int pos = 0;
		while(fA.available()>0) {
			int a = fA.read();
			int b = fB.read();
			if(a!=b) {
				if(ofsA!=ofsB) {
					System.out.println("Files are different at "+CU.fourDigitHex(pos+ofsA)+":"+CU.fourDigitHex(pos+ofsB));
				} else {
					System.out.println("Files are different at "+CU.fourDigitHex(pos+ofsA));
				}
				//break;
			}
			++pos;
		}
		fA.close();
		fB.close();
	}

}
