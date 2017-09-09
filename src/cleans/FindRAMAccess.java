package cleans;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import code.CodeLine;
import util.CU;
import web.LineOfMarkup;
import web.MarkupToHTML;

public class FindRAMAccess {
		
	public static void main(String[] args) throws Exception {
		
		List<Integer> knowns = new ArrayList<Integer>();
		List<Integer> unknowns = new ArrayList<Integer>();
		
		
		List<String> lines = Files.readAllLines(Paths.get("content/coco/daggorath/code.mark"));
		
		List<LineOfMarkup> marks = LineOfMarkup.convert(lines, "");		
		for(int pos=0;pos<marks.size();++pos) {
			LineOfMarkup mark = marks.get(pos);
			if(MarkupToHTML.isCodeLine(marks, pos)) {
				mark.codeLine = new CodeLine(mark.line);				
			}			
		}
		
		for(LineOfMarkup mark : marks) {
			if(mark.codeLine!=null) {
				String s = mark.codeLine.opcode;	
				if(s==null) continue;
				int i = s.indexOf("<$");
				if(i>=0) {										
					int addr = Integer.parseInt(s.substring(i+2,i+4),16);
					boolean fnd = mark.codeLine.comment !=null && mark.codeLine.comment.contains("{-ram_");
					if(fnd) {
						if(!knowns.contains(addr)) knowns.add(addr);
					} else {
						if(!unknowns.contains(addr)) unknowns.add(addr);
					}					
				}				
			}
		}
		
		Collections.sort(unknowns);
		
		for(int a : unknowns) {
			System.out.println("|| "+CU.hex4(a+512)+"      || "+"m"+CU.hex4(a+512)+"                || ?? ||");
		}
		

	}		

}
