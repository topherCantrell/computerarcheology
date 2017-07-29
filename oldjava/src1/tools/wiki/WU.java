package tools.wiki;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

/**
 * This class contains static code processing functions.
 */
public final class WU {
	
	private WU() {}
	
	/**
	 * Load a text file into a list of lines.
	 * @param filename name of the file
	 * @return list of lines
	 * @throws IOException file I/O errors
	 */
	public static List<String> loadLines(String filename) throws IOException
	{
		List<String> ret = new ArrayList<String>();
		
		FileReader fr = new FileReader(filename);
		BufferedReader br = new BufferedReader(fr);
		while(true) {
			 String g = br.readLine();
			 if(g==null) break;
			 ret.add(g);
		}
		br.close();
		
		return ret;
	}
	
	/**
	 * Write a list of lines to a text file.
	 * @param filename name of the file
	 * @param lines list of lines
	 * @throws IOException file I/O errors
	 */
	public static void writeLines(String filename, List<String> lines) throws IOException
	{
		PrintWriter pw = new PrintWriter(filename);
		for(String s : lines) {
			pw.println(s);
		}
		pw.flush();
		pw.close();
	}
	
	public static String[] getWords(String s) {
		StringTokenizer st = new StringTokenizer(s," ");
		String [] ret = new String[st.countTokens()];
		int p = 0;
		while(st.hasMoreTokens()) {
			ret[p++] = st.nextToken();
		}
		return ret;
	}
	
	public static String stripComment(String s) {
		int i = s.indexOf(";");
		if(i>=0) {
			return s.substring(0,i);
		}
		return s;
	}
	
	public static String moveCodeCommentToColumn(String s, int column, int afterCol) {
		int i = s.indexOf(";");
		if(s.length()<5 || s.charAt(4)!=':' || i<afterCol) return s;
		String a = s.substring(0,i).trim();
		String b = s.substring(i);
		while(a.length()<column) {
			a = a + " ";
		}
		return a+b;
	}
	
	public static String setJumpRequest(String s, String label) {
		int i = s.indexOf(";");
		if(i<0) {
			return s +" ; {"+label+"}";
		}
		
		int j = s.indexOf("{",i);
		if(j>=0) {
			int k = s.indexOf("}",j);			
			return s.substring(0,j)+"{"+label+"}"+s.substring(k+1);
		}
		
		return s.substring(0,i+1)+"{"+label+"} "+s.substring(i+1);		
	}
	
	public static Map<String,String> findGivenLabels(List<String> lines) {
		Map<String,String> ret = new HashMap<String,String>();
		for(int x=0;x<lines.size();++x) {
			String g = lines.get(x);
			if(g.length()<5 || g.charAt(4)!=':') continue;
			int y = x;
			String h = g;
			while(true) {						
				int i = h.indexOf("{*");
				if(i>=0) {
					int j = h.indexOf("}",i);
					if(j>i+2) {
						ret.put(g.substring(0,4), h.substring(i+2,j));
						break;
					}
				}
				--y;				
				if(y<0) break;		
				h = lines.get(y);
				if(h.length()>4 && h.charAt(4)==':') break;
			}
		}
		return ret;
	}
	
	public static void makeCodeLinks(List<String> lines, String [] ops) {
		
		List<String> opList = new ArrayList<String>();
		for(String s : ops) opList.add(s);
		
		Map<String,String> labels = WU.findGivenLabels(lines);
		//for(Entry<String, String> i : labels.entrySet()) {
		//	System.out.println(i.getValue());
		//}
		
		List<String> mustMakeLink = new ArrayList<String>();
		
		for(int x=0;x<lines.size();++x) {
			String g = lines.get(x);	
			String nc = WU.stripComment(g);
			String [] words = WU.getWords(nc);
			
			if(words.length>1) {
				String addr = words[words.length-1];
				if(addr.startsWith("$")) {
					addr = addr.substring(1);
					String op = words[words.length-2];
					if(opList.contains(op)) {						
						String lab = labels.get(addr);
						if(lab!=null) {
							g = WU.setJumpRequest(g, lab);
						} else {	
							g = WU.setJumpRequest(g, "");
							if(!mustMakeLink.contains(addr)) {
								mustMakeLink.add(addr);
							}
						}	
						lines.set(x, g);
					}
				}
			}									
		}
		
		for(int x=0;x<lines.size();++x) {
			String g = lines.get(x);
			if(g.length()<5 || g.charAt(4)!=':') continue;
			if(mustMakeLink.contains(g.substring(0,4))) {
				g = g + "{*}";
				lines.set(x,g);
			}
		}
	}

}
