package cleans;

import java.io.PrintStream;

import code.CU;
import files.BinaryFiles;

public class DaggorathPictures {
    
    // TODO I might change the output here. I need a routine that runs the existing code and looks
    // for the old output and replaces with the new.

    public static void main(String[] args) throws Exception {
        
        BinaryFiles data = new BinaryFiles("C000~content/CoCo/Daggorath/daggorath.bin");
        
        int pos = 0xDfca;
        boolean startSegment = true;
        int nx,ny,x,y;
        
        PrintStream ps = System.out;
        String d;
        String e;
        
        top:
        while(true) {
            
            d = CU.hex4(pos)+": ";
            int com = data.getByte(pos++);

            switch(com) {
            case 0xFA: // Return
                printCode(ps,d+"FA","Return");
                break;
            case 0xFB: // Jump to subroutine
                throw new Exception("Unimplemented");
            case 0xFC: // Multiple short segments
                printCode(ps,d+CU.hex2(com),"Draw short lines");
                while(true) {                    
                    com = data.getByte(pos++);
                    if(com==0) {
                        printCode(ps,CU.hex4(pos-1)+": 00","    End of short lines");
                        break;
                    }
                    ny = com >> 4;
                    if(ny>=8) ny=ny | 0xF0;
                    ny = ny << 1;
                    ny = ny & 0xFF;
                    nx = com & 0x0F;
                    if(nx>=8) nx=nx | 0xF0;
                    nx = nx << 1;
                    nx = nx & 0xFF;
                    if(nx>127) nx=nx-256;
                    if(ny>127) ny=ny-256;
                    e = "    Short line to relative ("+nx+","+ny+")";
                    printCode(ps,CU.hex4(pos-1)+": "+CU.hex2(com),e);
                }
                startSegment = true;
                break;
            case 0xFD: // Jump to XXXX
                nx = data.getByte(pos++);
                ny = data.getByte(pos++);
                d = d + "FD "+CU.hex2(nx)+" "+CU.hex2(ny);
                e = "Jump to "+CU.hex2(nx)+CU.hex2(ny);
                printCode(ps,d,e);
                break;                
            case 0xFE: // Exit
                printCode(ps,d+"FE","End of image");
                break top;
            case 0xFF: // Start a new segment
                printCode(ps,d+"FF","Start new line");
                startSegment = true;
                break;
            default:
                y = com;
                x = data.getByte(pos++);
                d = d +CU.hex2(y)+" "+CU.hex2(x);
                if(startSegment) {                
                    e = "Move to absolute ("+x+","+y+")";
                    startSegment = false;
                } else {
                    e = "Line to absolute ("+x+","+y+")";
                }
                printCode(ps,d,e);
                break;
            }
        }
        
        
        
        

    }
    
    static void printCode(PrintStream ps, String data, String exp) {
        ps.println(CU.padTo(data, 20)+"; "+exp);
    }

}
