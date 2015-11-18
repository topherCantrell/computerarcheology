package cleans;
import java.io.FileInputStream;
import java.io.InputStream;

public class GBHeader {
    
    public static String twoDigitHex(int value) {
        String ret = Integer.toString(value,16).toUpperCase();
        while(ret.length()<2) ret="0"+ret;
        return ret;
    }
            
    public static void main(String [] args) throws Exception
    {
        
        InputStream is = new FileInputStream("zelda.gb");
        int [] data = new int[is.available()];
        
        for(int x=0;x<data.length;++x) {
            data[x] = is.read();
        }
        
        is.close();
        
   
        int pos = 0x000;
        for(int y=0;y<17;++y) {
            System.out.print(Integer.toString(pos,16)+":");
            for(int x=0;x<16;++x) {
                System.out.print(" "+twoDigitHex(data[pos++]));                
            }
            System.out.println();
        }
        
    }

}
