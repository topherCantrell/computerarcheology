package cleans;

import java.io.FileOutputStream;
import java.io.OutputStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

import code.CodeLine;
import util.CU;
import web.LineOfMarkup;
import web.MarkupToHTML;

public class ExtractBinary {
	
	public static void main(String [] args) throws Exception {
		
		List<String> lines = Files.readAllLines(Paths.get("content/arcade/galaga/CPU1Fix.mark"));
		
		List<LineOfMarkup> marks = LineOfMarkup.convert(lines, "");		
		for(int pos=0;pos<marks.size();++pos) {
			LineOfMarkup mark = marks.get(pos);
			if(MarkupToHTML.isCodeLine(marks, pos)) {
				mark.codeLine = new CodeLine(mark.line);				
			}			
		}
		
		int pos = 0;
		int origin = 0;
		
		OutputStream os = new FileOutputStream("CPU1FIX.bin");
		
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
					os.write(i);
					++pos;
				}
			}
		}
		
		os.flush();
		os.close();
		
	}

}
