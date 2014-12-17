package tools.disassembly;

import java.io.BufferedReader;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.util.StringTokenizer;

import tools.code.CU;

public class ToAssem {
	
	public static void main(String [] args) throws Exception
	{
		
		
		FileOutputStream fos = new FileOutputStream("c:\\projects\\computerarcheology\\spaceinvaders\\sitest.org.bin");
		
		// inFile
		
		FileReader fr = new FileReader("c:\\projects\\computerarcheology\\spaceinvaders\\sitest.org.txt");
		BufferedReader br = new BufferedReader(fr);
		
		while(true) {
			String g = br.readLine();
			if(g==null) break;
			
			g=g.trim();
			g = CU.replaceAll(g, "\t", " ");
			
			if(g.length()<5 || g.charAt(4)!=':') {
				System.out.println(g);
				continue;
			}			
			
			g = g.substring(6);
			
			g = CU.replaceAll(g, "$", "0x");
			
			String a = g;
			int i = a.indexOf(";");
			if(i>=0) a = a.substring(0,i).trim();
			
			int j = -1;
			for(int x=0;x<a.length();++x) {
				if(a.charAt(x)>='a' && a.charAt(x)<='z') {
					j = x;
					break;
				}
			}
			
			String dd = a;
			if(j>=0) {
				dd = dd.substring(0,j).trim();
			}
			StringTokenizer st = new StringTokenizer(dd," ");
			while(st.hasMoreTokens()) {
				String z = st.nextToken();
				fos.write(Integer.parseInt(z,16));
			}
			
			if(j>=0) {				
				
				String aa = "";
				String bb = "";				
				String cc = null;
				if(i>=0) {
					cc = g.substring(i+1).trim();
				}
				g = g.substring(j);
				a = a.substring(j);
				j = a.indexOf(" ");
				if(j>=0) {
					aa = a.substring(0,j).trim();
					bb = a.substring(j).trim();
				} else {
					aa = a;
				}
				
				System.out.print("        "+CU.padTo(aa, 8)+CU.padTo(bb,16));
				if(cc!=null) System.out.print("; "+cc);
				System.out.println();
				
			} else {
				a = CU.replaceAll(a," ",",0x");
				System.out.print("# 0x"+a);
				if(i>=0) System.out.print(" "+g.substring(i));
				System.out.println();
			}
			
			
			
		}
		
		br.close();		
		
		fos.flush();
		fos.close();
		
	}

}
