package tools.wiki;

import java.io.BufferedReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class PushPull {
	
	public static void getPage(String url, String localName) throws IOException {
		int i = url.indexOf("/");
		String host = url.substring(0,i);
		String page = url.substring(i);
		Socket s = new Socket(host,80);		
		InputStream is = s.getInputStream();
		BufferedReader br = new BufferedReader(new InputStreamReader(is));
		PrintWriter pw = new PrintWriter(s.getOutputStream());
		
		pw.print("GET "+page+" HTTP/1.0\r\n");
		pw.println("Host: www.computerarcheology.com");
		pw.print("\r\n");
		pw.flush();
		
		while(true) {
			String g = br.readLine();
			if(g.length()==0) break;
		}
		
		PrintWriter fw = new PrintWriter(new FileWriter(localName));
		
		while(true) {		
			String g = br.readLine();
			if(g==null) break;
			fw.println(g);
		}
		
		fw.flush();
		fw.close();
		s.close();		
		
	}
	
	public static void pushPage(String localName, String host) {
		// TODO implement this
	}
	
	public static void main(String [] args) throws Exception {
		getPage("www.computerarcheology.com/wiki/wiki/CoCo/Daggorath/Code?format=txt","dd.txt");
	}

}
