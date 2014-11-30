package tools.web;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.ArrayList;

import tools.code.CU;

public class SaveHTMLComments {
	
	public static void main(String [] args) throws Exception 
	{
		
		
		File dir = new File("c:\\projects\\computerarcheology");
		String [] dirFiles = dir.list();
		for(String s : dirFiles) {
			if(!s.startsWith("comments.")) continue;
			handleComments("c:\\projects\\computerarcheology\\"+s,s.substring(9));
			File f = new File("c:\\projects\\computerarcheology\\"+s);
			f.delete();
		}
		
	}
	
	static void handleComments(String commentFile, String filename) throws Exception
	{
		ArrayList<String> newLines = new ArrayList<String>();
		
		System.out.println(filename);
		FileReader fr = new FileReader(commentFile);
		BufferedReader br = new BufferedReader(fr);
		ArrayList<String> comments = new ArrayList<String>();
		ArrayList<String> addresses = new ArrayList<String>();
		while(true) {
			String s = br.readLine();
			if(s==null) break;
			int i = s.indexOf(":");
			int a = Integer.parseInt(s.substring(0,i));
			addresses.add(CU.fourDigitHex(a)+":");
			comments.add(s.substring(i+1));			
		}
		br.close();
		
		fr = new FileReader(filename);
		br = new BufferedReader(fr);
		while(true) {
			String g = br.readLine();
			if(g==null) break;
			if(g.length()<5 || g.charAt(4)!=':') {
				newLines.add(g);
				continue;
			}
			int i = addresses.indexOf(g.substring(0,5));
			if(i<0) {
				newLines.add(g);
				continue;
			}
			int j = g.indexOf(";");
			if(j<0) {
				newLines.add(g);
				continue;			
			}
			newLines.add(g.substring(0,j+1)+comments.get(i));		
		}
		br.close();
		
		FileWriter fw = new FileWriter(filename);
		PrintWriter pw = new PrintWriter(fw);
		for(String s : newLines) {
			pw.println(s);
		}
		pw.flush();
		pw.close();
		
		
	}

}
