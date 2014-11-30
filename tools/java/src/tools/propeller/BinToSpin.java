package tools.propeller;

import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.PrintWriter;

/**
 * This class makes a SPIN source file with the data from a given
 * binary file.
 */
public class BinToSpin 
{

	public static void main(String[] args) throws Exception 
	{
		FileInputStream fis = new FileInputStream(args[0]);
		int [] data = new int[fis.available()];
		for(int x=0;x<data.length;++x) {
			data[x] = fis.read();
		}
		fis.close();
				
		FileWriter fw = new FileWriter(args[1]);
		PrintWriter pw = new PrintWriter(fw);
		
		pw.println("PUB getData");
		pw.println("  return @_program_");
		pw.println("");
		pw.println("DAT");
		pw.println("");
		pw.println("_program_");
		pw.println("");
		
		for(int x=0;x<data.length;++x) {
			int cnt = x%64;
			if(cnt==0) {
				pw.print("  byte  ");
			}
			pw.print("$"+Integer.toString(data[x],16));
			if(cnt==63) {
				pw.println();
			} else {
				if(x!=(data.length-1)) pw.print(",");
			}
		}
		
		pw.flush();
		pw.close();
	}

}
