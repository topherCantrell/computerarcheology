package diss;

import code.CU;
import cpu.CPU;
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
        
        String [] targs = {"0x0000~content/gameboy/zelda/zelda.gb","Z80GB"};
        args = targs;
                
        if(args.length<2) {
            System.out.println("Arguments: binFile cpu [start] [end]");
            return;
        }
        
        // Load the data from multiple files. The origin is part of the
        // specification.
        BinaryFiles files = new BinaryFiles(args[0]);
        int start = files.getLowestAddress();
        int end = files.getHighestAddress();
        
        if(args.length>2) {
            start = CU.parseInt(args[2], 16);
        }
        
        if(args.length>3) {
            start = CU.parseInt(args[3], 16);
        }
        
        CPU cpu = CPU.getCPU(args[1]);
        
        
        System.out.println(""+start+" "+end+" "+cpu);
        
    }

}
