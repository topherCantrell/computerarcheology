package tools.web;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;

import tools.code.CU;

/**
 * This static utility class finds a subset of lines within a list of lines. Start 
 * and stop indicators are used to define the subset.<p>
 * 
 * For instance: "contains(blah)*2-4" finds the second line (*2) that contains the 
 * text "blah". The target line is four above this (-4).<p>
 * 
 * If a start indicator is not given, the first line begins the subset. If the stop 
 * indicator is not given, the last line ends the subset.
 */
public class LineListSubset {
		
	public static void sort(List<String> lines, String sortSpec) {
		
		// null or "" just start at beginning
		// else find index of
		
		boolean changed = true;
		while(changed) {
			changed = false;
			for(int x=0;x<lines.size()-1;++x) {
				String a = lines.get(x);
				String b = lines.get(x+1);
				String sa = a;
				String sb = b;
				if(sortSpec!=null && sortSpec.length()>0) {
					int i = sa.indexOf(sortSpec);
					if(i>=0) {
						sa = sa.substring(i);
					}
					i = sb.indexOf(sortSpec);
					if(i>-0) {
						sb = sb.substring(i);
					}
				}
				if(sb.compareTo(sa)<0) {
					lines.set(x,b);
					lines.set(x+1,a);
					changed=true;
				}
			}			
		}		
		
	}
	
	/**
	 * Find the start and stop index defining a subset within a list of lines.
	 * @param lines the list of lines
	 * @param startIndicator the start indicator or "" for first-line
	 * @param stopIndicator the stop indicator or "" for last-line
	 * @return an array containing the start and stop indices
	 */
	public static int[] findStartStop(List<String> lines, String startIndicator, String stopIndicator)
	{
		startIndicator = CU.replaceAll(startIndicator, "&quot;", "\"");
		stopIndicator = CU.replaceAll(stopIndicator, "&quot;", "\"");
		int i = findIndicator(lines, startIndicator, 0, true);
		int j = findIndicator(lines, stopIndicator, i, false);
		int [] ret = {i,j};
		return ret;		
	}
	
	static int findIndicator(List<String> lines, String indicator, int startIndex, boolean start)
	{
		
		// A no-indicator is the start or end of the list
		if(indicator==null || indicator.length()==0) {
			if(start) return startIndex;
			else return lines.size()-1;
		}
		
		// Parse off any + or - term
		int i = indicator.indexOf("+");
		if(i<0) i = indicator.indexOf("-");
		
		String first = indicator;
		String offset = null;		
		if(i>=0) {
			first = indicator.substring(0,i);
			offset = indicator.substring(i+1);
			if(first.length()==0) first="0";
		}
		
		// Parse off any function
		String function = null;
		String args = null;
		String multiplier = null;
		int k = first.indexOf("(");
		if(k>=0) {
			function = first.substring(0,k);
			int kk = first.lastIndexOf(")");
			args = first.substring(k+1,kk);
			multiplier = first.substring(kk+1).trim();
			if(multiplier.startsWith("*")) multiplier = multiplier.substring(1);
			if(multiplier.length()==0) multiplier = "1";
		}
		
		int index = startIndex;
		if(function==null) {
			// Not a function. It must be an absolute number.
			index = index + Integer.parseInt(first);
		} else {			
			int mult = Integer.parseInt(multiplier);
			//System.out.println("FUN:"+function+":"+args+":"+mult+":");
			for(int x=0;x<mult;++x) {
				while(true) {
					String s = lines.get(index);
					++index;
					if(function.equals("startsWith")) {
						if(s.trim().startsWith(args)) break;
					} else if(function.equals("endsWith")) {
						if(s.trim().endsWith(args)) break;
					} else if(function.equals("contains")) {
						if(s.contains(args)) break;
					} else if(function.equals("notStartsWith")) {
						if(!s.trim().startsWith(args)) break;
					}
					else {
						throw new RuntimeException("Unknown function '"+function+"'");
					}					
				}
			}
			--index;
		}
		
		if(i>=0) {
			int ofs = Integer.parseInt(offset);
			if(indicator.charAt(i)=='-') {
				ofs = -ofs;
			}
			index = index + ofs;
		}
		
		//System.out.println("::INDEX "+index);
		
		return index;
		
	}
	
	public static void main(String [] args) throws Exception
	{
		
		String fn = args[0];
		String start = args[1];
		String stop = args[2];
		String sort = args[3];
		
		// Read the lines
		FileReader fr = new FileReader(fn);
		BufferedReader br = new BufferedReader(fr);
		List<String> lines = new ArrayList<String>();
		while(true) {
			String g = br.readLine();
			if(g==null) break;
			lines.add(g);
		}
		br.close();
		
		// Find the sublist		
		int [] jk = findStartStop(lines,start,stop);
		List<String> sublist = lines.subList(jk[0], jk[1]+1);
		
		// Sort the list
		sort(sublist,sort);
		
		// Print the list
		for(String s : sublist) {
			System.out.println(s);
		}
		
	}

}
