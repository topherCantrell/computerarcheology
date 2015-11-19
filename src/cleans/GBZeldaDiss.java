package cleans;
import code.CU;
import diss.Disassembler;

public class GBZeldaDiss {

    public static void main(String[] args) throws Exception {
        
        /*
        InputStream is = new FileInputStream("content/gameboy/zelda/zelda.gb");
        for(int x=0;x<32;++x) {
            String bn = ""+x;
            if(bn.length()<2) bn="0"+bn;
            OutputStream os = new FileOutputStream("content/gameboy/zelda/bank"+bn+".bin");
            for(int y=0;y<16*1024;++y) {
                int a = is.read();
                os.write(a);
            }
            os.flush();
            os.close();
        }
        */        
        
        
        for(int x=0;x<32;++x) {
            String bn = ""+x;
            if(bn.length()<2) bn="0"+bn;
            if(x==0) {
                String[] a = {"0x0000~content/gameboy/zelda/bank"+bn+".bin","content/gameboy/zelda/Bank_"+bn+".txt","Z80GB"};
                Disassembler.main(a);
            } else {
                String[] a = {"0x4000~content/gameboy/zelda/bank"+bn+".bin","content/gameboy/zelda/Bank_"+bn+".txt","Z80GB"};
                Disassembler.main(a);
            }
        }
        
    }

}
