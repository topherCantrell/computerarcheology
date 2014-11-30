package tools.file;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;

import tools.code.CodeLine;

public class LinesFromFile {
	
	String name;
	List<String> lines = new ArrayList<String>();
	int cursor = -1;
	
	public LinesFromFile(String name) throws Exception {
		
		this.name = name;
		
		FileReader fr = new FileReader(name);	
		BufferedReader br = new BufferedReader(fr);
		
		while(true) {
			String g = br.readLine();
			if(g==null) break;
			lines.add(g);
		}	
		
		br.close();
		
		cursor = 0;
		
	}
	
	public List<String> getLines() {
		return lines;
	}
	
	public List<String> getRange(String startsWith, String endsWith) {
		
		List<String> ret = new ArrayList<String>();
		
		int x=0;
		for(;x<lines.size();++x) {
			if(lines.get(x).startsWith(startsWith)) break;
		}
		
		while(!lines.get(x).startsWith(endsWith)) {
			ret.add(lines.get(x++));
		}
		ret.add(lines.get(x++));
		
		return ret;
	}
	
	public void skipToStartsWith(String text) {
		while(true) {
			if(lines.get(cursor).startsWith(text)) {
				return;
			}
			++cursor;
		}
	}
	
	public List<CodeLine> listToCode(List<String> lines) {
		ArrayList<CodeLine> ret = new ArrayList<CodeLine>();
		for(int x=0;x<lines.size();++x) {
			String line = lines.get(x);
			ret.add(new CodeLine(line,name,x,true));
		}
		return ret;
	}

}
