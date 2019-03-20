package cleans;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

import code.CodeLine;
import util.CU;
import util.FU;
import web.LineOfMarkup;
import web.MarkupToHTML;

public class CheckBinary {

	public static void main(String[] args) throws Exception {
		
		int[] data = FU.readBinary("content/coco/daggorath/daggorath.bin");
		int origin = 0xC000;
		
		List<String> lines = Files.readAllLines(Paths.get("content/coco/daggorath/code.mark"));
		
		List<LineOfMarkup> marks = LineOfMarkup.convert(lines, "");		
		for(int pos=0;pos<marks.size();++pos) {
			LineOfMarkup mark = marks.get(pos);
			if(MarkupToHTML.isCodeLine(marks, pos)) {
				mark.codeLine = new CodeLine(mark.line);				
			}			
		}
		
		int pos = 0;
		
		for(LineOfMarkup mark : marks) {
			if(mark.codeLine==null) continue;
			if(mark.codeLine.address>=0) {
				if(mark.codeLine.address != pos+origin) {
					throw new Exception("Expected address "+CU.hex4(pos+origin)+" but got "+CU.hex4(mark.codeLine.address));
				}				
			}
			if(mark.codeLine.data!=null) {
				for(int x=0;x<mark.codeLine.data.size();++x) {
				    int i = mark.codeLine.data.get(x);
					if(data[pos]!=i) {
						throw new Exception("Values different at "+CU.hex4(pos+origin));
					}
					++pos;
				}
			}
		}
		
		System.out.println("Binary is OK. Checked through "+CU.hex4(pos+origin-1));
		
	}

}
