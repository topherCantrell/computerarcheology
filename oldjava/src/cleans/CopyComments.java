package cleans;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class CopyComments {

	public static void main(String[] args) throws Exception {
		List<String> src = Files.readAllLines(Paths.get("content/TRS80/HauntedHouse/Code1.cmark"));
		List<String> dst = Files.readAllLines(Paths.get("content/TRS80/HauntedHouse/Code2.cmark"));
		
		List<String> srcSub = new ArrayList<String>();
		List<String> dstSub = new ArrayList<String>();
		
		int x=0;
		while(!src.get(x).equals("##START")) ++x;
		++x;
		while(!src.get(x).equals("##END")) {
			srcSub.add(src.get(x));
			++x;
		}
		
		x=0;
		while(!dst.get(x).equals("##START")) ++x;
		++x;
		while(!dst.get(x).equals("##END")) {
			dstSub.add(dst.get(x));
			++x;
		}
		
		if(dstSub.size()!=srcSub.size()) throw new RuntimeException("WRONG SIZE");
		for(int y=0;y<srcSub.size();++y) {
			String a = srcSub.get(y);
			String b = dstSub.get(y);
			if(a.length()<5 || a.charAt(4)!=':') {
				System.out.println(a);
				continue;
			}
			int i = a.indexOf(";");
			if(i<0) {
				System.out.println(b);
				continue;
			}
			String com = a.substring(i);
			System.out.println(b+com);
		}

	}

}
