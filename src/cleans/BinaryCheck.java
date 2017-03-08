package cleans;

import java.io.FileInputStream;
import java.io.InputStream;
import java.nio.file.Path;
import java.nio.file.Paths;

import code.CU;
import code.CodeFile;
import code.CodeLine;
import files.BinaryFiles;

public class BinaryCheck {
	
	public static void main2(String [] args) throws Exception {
		
		// Compare two binary files
		InputStream fa = new FileInputStream("content/arcade/asteroids/035127.01");
		InputStream fb = new FileInputStream("content/arcade/asteroids/rev2/035127.02");
		
		int start = 0x0800;
		
		if(fa.available()!=fb.available()) {
			throw new RuntimeException("Different sizes");
		}
				
		
		while(fa.available()>0) {
			int a = fa.read();
			int b = fb.read();
			if(a!=b) {
				System.out.println("Different at "+CU.hex4(start));
			}
			++start;
		}
		
	}

    public static void main(String[] args) throws Exception {

        BinaryFiles data = new BinaryFiles("0800~content/arcade/asteroids/rev2/035127.02");        
        Path p = Paths.get("content/arcade/asteroids/VectorROM.cmark");
        CodeFile tabs = new CodeFile(p);
        int start = 0x0800;
        int end = 0xFFF;
        
        int chk = 0;
        
        for(CodeLine line : tabs.code) {
            if(line.data==null || line.data.size()==0) continue;
            if(line.address!=start) {
                throw new Exception("Binary position is "+CU.hex4(start)+" but text says "+CU.hex4(line.address));
            }
            for(int d : line.data) {
            	chk = chk + d;
                if(d != data.getByte(start)) {
                    throw new Exception("Bytes are different at "+CU.hex4(start));
                }
                ++start;
            }
        }
        
        if(start!=(end+1)) {
            throw new Exception("Text did not end at "+CU.hex4(end));
        }
        
        System.out.println(chk);
        

    }

}
