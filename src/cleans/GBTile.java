package cleans;

import java.io.FileInputStream;
import java.io.InputStream;
import java.io.PrintStream;

import code.CU;

public class GBTile {
    
    final static String BINBASE="content/Gameboy/Zelda/bins/bank";
    
    public static void main(String [] args) throws Exception {
        
        String bank = "0C";
        int start = 0x4000;
        int end = 0x8000;
        
        //PrintStream ps= System.out;
        
        PrintStream ps = new PrintStream("tile.txt");
        
        int org = 0;
        if(start>=0x4000) {
            org = 0x4000;
            start = start - 0x4000;
        }
        if(end>=0x4000) {
            end = end - 0x4000;
        }
        
        int [] data = new int[0x4000];
        InputStream is = new FileInputStream(BINBASE+bank+".bin");
        for(int x=0;x<data.length;++x) {
            data[x] = is.read();
        }
        is.close();
        
        while(start!=end) {            
        
            for(int x=0;x<16;x=x+2) {
                int a = data[start+x];
                int b = data[start+x+1];
                String ascii = "";
                for(int mask=0x80;mask>=1;mask=mask>>1) {
                    int v = 0;
                    if( (a&mask)!=0 ) v=v|2;
                    if( (b&mask)!=0 ) v=v|1;
                    if(v>0) {
                        ascii = ascii + v;
                    } else {
                        ascii = ascii + '.';
                    }
                }
                ps.println(CU.hex4(start+org+x)+": "+CU.hex2(a)+" "+CU.hex2(b)+"     ; "+ascii);               
            }
            
            start = start + 16;
            ps.println();
        
        }
        
        ps.flush();
        ps.close();
        
    }

}
