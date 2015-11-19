import code.CU;
import diss.Disassembler;

public class Mass {

    public static void main(String[] args) throws Exception {
        
        for(int x=0;x<2;++x) {
            String[] a = {"0x0000~content/gameboy/zelda/zelda.gb","Bank"+x+".txt","Z80GB",CU.hex4(x*16*1024),CU.hex4((x+1)*16*1024-1)};
            Disassembler.main(a);
        }
    }

}
