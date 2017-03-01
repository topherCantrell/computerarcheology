package cleans;

import java.io.PrintStream;
import java.nio.file.Path;
import java.nio.file.Paths;

import code.CU;
import code.CodeFile;
import code.CodeLine;

public class BinaryToJS {

	public static void main(String[] args) throws Exception {
		
		//Path p = Paths.get("content/TRS80/pyramid/Code.cmark");
	    //CodeFile tabs = new CodeFile(p);
	    //int start = 0x4300;
	    
	    //Path p = Paths.get("content/CoCo/bedlam/Code.cmark");
	    //CodeFile tabs = new CodeFile(p);
	    //int start = 0x0600;
	    
	    //Path p = Paths.get("content/CoCo/pyramid/Code.cmark");
	    //CodeFile tabs = new CodeFile(p);
	    //int start = 0x0600;
	    
	    Path p = Paths.get("content/CoCo/RaakaTu/Code.cmark");
	    CodeFile tabs = new CodeFile(p);
	    int start = 0x0600;
	    
	    PrintStream ps = new PrintStream("data.js");
	    ps.print("var data = [");
	    
	    int pos=0;
	    
	    for(CodeLine line : tabs.code) {
            if(line.data==null || line.data.size()==0) continue;
            if(line.address!=start) {
                throw new Exception("Binary position is "+CU.hex4(start)+" but text says "+CU.hex4(line.address));
            }
            for(int d : line.data) {
            	String v = Integer.toString(d,16).toUpperCase();
            	if(v.length()<2) v="0"+v;
            	ps.print("0x"+v+",");   
            	++start;
            	++pos;
            	if(pos==32) {
            		ps.println();
            		pos = 0;
            	}
            }            
        }
        
	    
	    ps.println("];");
	    ps.flush();
	    ps.close();

	}

}
