package tools.web;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class DeployFile {
		
	// TODO document the include language
	
	/**
	 * This method loads an HTML file and processes any includes within.
	 * @param basePath the base for all file access
	 * @param filePathAndName the name of the file to load
	 * @return a list of lines for the loaded file
	 * @throws IOException if something goes wrong
	 */
	static List<String> loadFile(String basePath, String filePathAndName) throws IOException
	{
		List<String> ret = new ArrayList<String>();
		FileReader fr = new FileReader(filePathAndName);
		BufferedReader br = new BufferedReader(fr);
		while(true) {
			String g = br.readLine();
			if(g==null) break;
			ret.add(g);
		}		
		
		// Now process includes behind the scenes
		for(int x=ret.size()-1;x>=0;--x) {
			String g = ret.get(x);
			if(!g.trim().startsWith("<!--#include ")) {
				continue;
			}
			
			ret.remove(x);
			System.out.println("  Processing include: "+g);
			
			int i = g.indexOf("\"")+1;
			int j = g.indexOf("\"",i);
			String includeName = g.substring(i,j);
			StringTokenizer st = new StringTokenizer(includeName,"/");
			String includePath = basePath.substring(0,basePath.length()-1);
			while(st.hasMoreElements()) {
				String a = st.nextToken();
				if(a.equals("..")) {
					i = includePath.lastIndexOf("/");
					includePath = includePath.substring(0,i);
				} else {
					includePath = includePath+"/"+a;								
				}
			}
			
			List<String> includeLines = loadFile(basePath,includePath);
			
			String startIndicator = "";
			i=g.indexOf("start=\"");
			if(i>=0) {
				i=i+7;
				j = g.indexOf("\"",i);
				startIndicator = g.substring(i,j);
			}
			
			String stopIndicator="";
			i=g.indexOf("stop=\"");
			if(i>=0) {
				i=i+6;
				j=g.indexOf("\"",i);
				stopIndicator = g.substring(i,j);
			}
			
			String typeIndicator="raw";
			i=g.indexOf("type=\"");
			if(i>=0) {
				i=i+6;
				j=g.indexOf("\"",i);
				typeIndicator = g.substring(i,j);
			}
			
			// Find the requested subset of the include lines
			int [] ij = LineListSubset.findStartStop(includeLines, startIndicator, stopIndicator);			
			includeLines = includeLines.subList(ij[0], ij[1]+1);			
			
			if(typeIndicator.equals("html")) {
				for(int c=0;c<includeLines.size();++c) {
					includeLines.set(c, DOCXToWeb.makeHTMLFriendly(includeLines.get(c)));
				}
			}
			
			
			// TODO ... filter the lines in includeLines
			
			ret.addAll(x,includeLines);			
			
		}
		
		br.close();
		
		return ret;
	}
	
	public static void deployHTMLFile(String localPath, String name, String remotePath) throws Exception
	{		
		List<String> lines = loadFile(localPath,name);
		
		FileWriter fw = new FileWriter(name+".trx");
		PrintWriter pw = new PrintWriter(fw);
		
		for(String s : lines) {
			pw.println(s);
		}
		
		pw.flush();
		pw.close();			
	}
	

}
