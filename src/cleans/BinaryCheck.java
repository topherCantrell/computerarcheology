package cleans;

import java.nio.file.Path;
import java.nio.file.Paths;

import code.CU;
import code.CodeFile;
import code.CodeLine;
import files.BinaryFiles;

public class BinaryCheck {

    public static void main(String[] args) throws Exception {

        BinaryFiles data = new BinaryFiles("0600~content/CoCo/Pyramid/pyramid.bin");        
        Path p = Paths.get("content/CoCo/Pyramid/Code.cmark");
        CodeFile tabs = new CodeFile(p);
        int start = 0x0600;
        int end = 0x0601;
        
        for(CodeLine line : tabs.code) {
            if(line.data==null || line.data.size()==0) continue;
            if(line.address!=start) {
                throw new Exception("Binary position is "+CU.hex4(start)+" but text says "+CU.hex4(line.address));
            }
            for(int d : line.data) {
                if(d != data.getByte(start)) {
                    throw new Exception("Bytes are different at "+CU.hex4(start));
                }
                ++start;
            }
        }
        
        if(start!=(end+1)) {
            throw new Exception("Text did not end at "+CU.hex4(end));
        }
        

    }

}
