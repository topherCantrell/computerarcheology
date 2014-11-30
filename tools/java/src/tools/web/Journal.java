package tools.web;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.PrintWriter;

public class Journal 
{
	
	public static void headJournal(int numEntries) throws Exception
	{
		
		FileReader fr = new FileReader("c:/projects/computerarcheology/journal/journal.html");
		BufferedReader br = new BufferedReader(fr);
		FileWriter fw = new FileWriter("c:/projects/computerarcheology/journal/journal.inc.html");
		PrintWriter pw = new PrintWriter(fw);
		
		while(true) {
			String g = br.readLine();
			if(g.startsWith("<b>")) {
				pw.println(g);
				break;
			}
		}
		
		while(true) {
			String g = br.readLine();
			if(!g.startsWith("<b>")) {
				pw.println(g);
				continue;
			}
			--numEntries;
			if(numEntries<=0) break;
			pw.println(g);
		}
		
		pw.flush();
		pw.close();
		br.close();
		
	}
	public static void main(String [] args) throws Exception
	{
		int numEntries = 2;
		if(args.length>0) {
			numEntries = Integer.parseInt(args[0]);
		}
		
		headJournal(numEntries);		
	}

}
