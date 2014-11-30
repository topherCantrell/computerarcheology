package tools.web;

import java.io.BufferedReader; 
import java.io.FileReader;

public class DocToWeb 
{
	
	static String [] html = {
		"<H1>","<H2>","<H3>","<PRE>","<I>","<B>","<FONT","<A","<IMG",
		"</A","</FONT","</H1>","</H2>","</H3>","</PRE>","</I>","</B>"
	};
	
	static boolean isLessThanAllowed(String g, int i)
	{
		g = g.toUpperCase();
		for(int x=0;x<html.length;++x) {
			int j = g.indexOf(html[x],i);
			if(j==i) return true;
		}
		return false;
	}
	
	static String removeLessThan(String g)
	{
		int pos = 0;
		while(true) {
			int i = g.indexOf('<',pos);
			if(i<0) break;
			if(!isLessThanAllowed(g,i)) {
				String a = g.substring(0,i)+"&lt;"+g.substring(i+1);
				g = a;
			}
			pos = i+1;
		}
		return g;
	}
	
	public static void main(String [] args) throws Exception
	{
		FileReader fr = new FileReader(args[0]);
		BufferedReader br = new BufferedReader(fr);
		boolean inPre = false; 
		while(true) {
			String g = br.readLine();
			if(g==null) break;
			if(inPre) {
				System.out.println(removeLessThan(g));
				if(g.toUpperCase().indexOf("</PRE>")>=0) {
					inPre = false;
				}
			} else {
				System.out.println(removeLessThan(g)+"<p>");
				if(g.toUpperCase().indexOf("<PRE>")>=0) {
					inPre = true;
				}
			}
		}
		br.close();
	}

}
