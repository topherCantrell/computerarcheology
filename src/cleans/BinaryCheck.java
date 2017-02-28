package cleans;

import java.nio.file.Path;
import java.nio.file.Paths;

import code.CU;
import code.CodeFile;
import code.CodeLine;
import files.BinaryFiles;

public class BinaryCheck {

    public static void main(String[] args) throws Exception {

        BinaryFiles data = new BinaryFiles("4200~content/TRS80/pyramid/pyrmd2.cas");        
        Path p = Paths.get("content/TRS80/pyramid/Code.cmark");
        CodeFile tabs = new CodeFile(p);
        int start = 0x4200;
        int end = 0x7F83;
        
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
