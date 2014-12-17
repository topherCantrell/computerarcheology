package tools.code;

import java.util.ArrayList;
import java.util.List;

public class TextRect {
	
	List<String> strings = new ArrayList<String>();
	
	public TextRect() {
		
	}
	
	public TextRect(String s, int i) {
		for(int x=0;x<i;++x) {
			strings.add(s);
		}
	}

	public TextRect addRow(String a) {
		strings.add(a);
		return this;
	}

	public void replaceAll(String target, String rep) {
		for(int x=0;x<strings.size();++x) {
			strings.set(x, CU.replaceAll(strings.get(x),target,rep));
		}		
	}
	
	@Override
	public String toString() {
		String ret = "";
		for(String s : strings) {
			ret = ret + s+"\n";
		}
		return ret;
	}
	
	private void appendToRow(int row, String s) {
		strings.set(row, strings.get(row)+s);
	}

	public void append(TextRect rect, int row) {
	    for(String r : rect.strings) {
	    	appendToRow(row,r);
	    	++row;
	    }
	}

}
