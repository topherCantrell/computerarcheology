package diss;

import java.io.PrintStream;
import java.util.HashMap;
import java.util.Map;

import code.CU;
import cpu.CPU;
import cpu.Opcode;
import files.BinaryFiles;

public class Disassembler {
    
    /**
     * This tool disassembles a binary file into text opcodes for a target processor.
     * 
     * Command line arguments: binFile cpu [start] [end]
     * 
     * The 'binFile' is a list of ROM files each with a given origin. For instance:
     * 0x0000~invaders.h+invaders.g+invaders.f+invaders.e
     * 
     * This puts the four Space Invaders ROM files together in order. The first file
     * is given the origin "0x0000" and the others follow right behind it.
     * 
     * The 'cpu' is the CPU that runs the code.
     * 
     * The 'start' and 'end' are optional starting and ending points in the disassembly
     * ROM data. If 'start' is not given then the first address is used. If 'end' is
     * not given the the last address is used. Leave both out to disassemble the entire
     * binary collection.
     * 
     * @param args see above
     * @throws Exception errors opening files
     */
    public static void main(String [] args) throws Exception {
                
        
        String [] targs = {"0x42E9~haunt.bin","c:\\tmp\\test.txt","Z80"};
        args = targs;
                
        if(args.length<3) {
            //                               0       1     2    3       4
            System.out.println("Arguments: binFile outfile cpu [start] [end]");
            return;
        }
        
        PrintStream ps = new PrintStream(args[1]);
        
        // Load the data from multiple files. The origin is part of the
        // specification.
        BinaryFiles files = new BinaryFiles(args[0]);
        int start = files.getLowestAddress();
        int end = files.getHighestAddress();        
        
        if(args.length>3) {
            start = CU.parseInt(args[3], 16);
        }
        
        if(args.length>4) {
            end = CU.parseInt(args[4], 16);
        } 
        
        CPU cpu = CPU.getCPU(args[2]);
        
        System.out.println(CU.hex4(start)+" - "+CU.hex4(end));
        
        // We need the binary data in an array for scanning                     
        int [] binary = new int[end-start+1];
        for(int x=start;x<=end;++x) binary[x-start]=files.getByte(x);   
        
        Map<String,Object> fillins = new HashMap<String,Object>();
        int addr = start;
        while(addr<=end) {
            Opcode op = cpu.disassemble(files,addr,fillins);
            if(op==null) {
                op = Opcode.UNKNOWN;
                cpu.fillin(op, files, addr, fillins);
            }
                                    
            printDisassembly(cpu, addr, op,fillins,ps);
            
            addr = addr + op.getSize();
            
        }                
        
        ps.flush();
        ps.close();
        
    }
    
    static void printDisassembly(CPU cpu, int addr, Opcode op, Map<String,Object> fillins, PrintStream ps) {
        
        int [] spacing = cpu.getSpacing();
        
        String data = "";
        for(int val : (int[])fillins.get("bytes")) {
            data = data +" "+CU.hex2(val);
        }
        data = CU.padTo(data, spacing[0]);
        
        String wordA = (String)fillins.get("wordA");
        wordA = CU.padTo(wordA, spacing[1]);
        String wordB = (String)fillins.get("wordB");
        wordB = CU.padTo(wordB, spacing[2]);
        
        ps.println(CU.hex4(addr)+":"+data+wordA+wordB);
        
    }

}
