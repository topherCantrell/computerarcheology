package tools.wiki;

import java.util.List;

public class DigCleaner {
	
	static String[] CODE_LINKS_6809 = {
		"BNE","JSR","BRA","BEQ","JMP","LBEQ","BMI","BCS","LBMI","BSR","BCC","BLS","LBNE"
	};
	
	public static void main(String [] args) throws Exception
	{
		
		List<String> lines = WU.loadLines("fromwiki.txt");
		
		WU.makeCodeLinks(lines, CODE_LINKS_6809);
				
		WU.writeLines("towiki.txt", lines);
		
	}

}
