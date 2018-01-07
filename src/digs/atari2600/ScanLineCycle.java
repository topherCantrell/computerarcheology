package digs.atari2600;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

/**
 * This class holds all the data from one line of Z26 debug spew.
 *
 */
public class ScanLineCycle {
    int frame;
    int line;
    int cycle;
    int clock;
    int p0Pos;
    int p1Pos;
    int m0Pos;
    int m1Pos;
    int bPos;
    String flags;
    int aRegister;
    int xRegister;
    int yRegister;
    int spRegister;
    int flagsRegister;
    int pcRegister;
    String code;
    String disasm;
    int codeAddress;
    
    String hardwareAccess;     // Special register read/write
    boolean hardwareWrite;     // TRUE if write, FALSE if read
    int hardwareAccessValue;   // Value written (or -1 if read)    
    int hardwareAccessAddress; // Address of any read/write
    
    /**
     * Returns true if the string is non-numeric.
     * @param name the string
     * @return true if non-numeric, false if numeric
     */
    static boolean isToken(String name) {
    	
    	// Must be something
    	if(name.length()==0) return false;
    	
    	// Anything but upper-case and numbers fails
        for(int x=0;x<name.length();++x) {
            char a = name.charAt(x);
            if( !((a>='0' && a<='9') || (a>='A' && a<='Z'))) return false;
        }
        
        // A pure number will also fail
        for(int x=0;x<name.length();++x) {
            char a = name.charAt(x);
            if( a<'0' || a>'9') {
                return true;
            }
        }        
        return false;
    }
    
    /**
     * This method decodes a single line of Z26 debug spew.
     * @param s the debug spew
     * @param useInfo the usageinfo return
     */
    public void decode(String s,Map<Integer,Map<String,List<Integer>>> useInfo) {
    	// (1097  26  21  -5) ( 44  38  86  56 128) nvBdIzC 50 00 00 ff  d4ca: bd 8d de lda  de8d,x  = de8d  
    	//  FFFF  LL  CC  KK    PP  pp  MM  mm bbb  ggggggg AA XX YY ss  ppppoooooooooodddddddddddddddddddd
    	
        StringTokenizer st = new StringTokenizer(s,"() :");
        frame      = Integer.parseInt(st.nextToken()); // FFFF
        line       = Integer.parseInt(st.nextToken()); // LL
        cycle      = Integer.parseInt(st.nextToken()); // CC
        clock      = Integer.parseInt(st.nextToken()); // KK
        p0Pos      = Integer.parseInt(st.nextToken()); // PP
        p1Pos      = Integer.parseInt(st.nextToken()); // pp
        m0Pos      = Integer.parseInt(st.nextToken()); // MM
        m1Pos      = Integer.parseInt(st.nextToken()); // mm
        bPos       = Integer.parseInt(st.nextToken()); // bbb
        flags      = st.nextToken();                   // ggggggg        
        flagsRegister = 0;
        if(flags.indexOf("N")>0) flagsRegister=flagsRegister | 0x80;
        if(flags.indexOf("V")>0) flagsRegister=flagsRegister | 0x40;
        if(flags.indexOf("B")>0) flagsRegister=flagsRegister | 0x10;
        if(flags.indexOf("D")>0) flagsRegister=flagsRegister | 0x8;
        if(flags.indexOf("I")>0) flagsRegister=flagsRegister | 0x4;
        if(flags.indexOf("Z")>0) flagsRegister=flagsRegister | 0x2;
        if(flags.indexOf("C")>0) flagsRegister=flagsRegister | 0x1;
        aRegister  = Integer.parseInt(st.nextToken(),16); // AA
        xRegister  = Integer.parseInt(st.nextToken(),16); // XX
        yRegister  = Integer.parseInt(st.nextToken(),16); // YY
        spRegister = Integer.parseInt(st.nextToken(),16); // ss
        pcRegister = Integer.parseInt(st.nextToken(),16); // pppp
        int lp = s.lastIndexOf(':');
        codeAddress = Integer.parseInt(s.substring(lp-4,lp),16);
        code       = s.substring(lp+1,lp+11).trim();           // oooo...
        disasm     = s.substring(lp+11).trim();              // dddd...
        
        // The current debug spew has trouble with some forms of "stx". For instance,
        // (1097  20  34  34) ( 44  38  87  65 128) nvBdIZC 04 00 01 ff  f9c3: d0 fd    bne  f9c2
        // (1097  20  36  40) ( 44  38  87  65 128) nvBdIZC 04 00 01 ff  f9c5: stx  12,y    = RESM1
        // Notice how the opcode is missing and the "stx" is in the opcode field. We will
        // move the disasm over and set the opcode to all FFs here.
        if(code.indexOf("stx")>=0) {
        	code = "FF FF FF";
        	disasm = s.substring(lp+1).trim();            
        }
        if(code.indexOf("ldx")>=0) {
        	code = "FF FF FF";
        	disasm = s.substring(lp+1).trim();
        }
        
        // Combat moves the stack pointer and then pushes tia registers. The debug spew
        // doesn't catch that so we will here.
        if(disasm.startsWith("ph") || disasm.startsWith("pl")) {
        	if(spRegister<=0x2C) {
        		if(disasm.startsWith("ph")) {
        			disasm = disasm + " = "+Z26Frame.tiaRegisters[spRegister];
        		} else {
        			disasm = disasm + " = "+Z26Frame.tiaReadRegisters[spRegister];
        		}        		
        	}
        }
        
        // Just to make sure there are no more disasms in the opcode field
        try {
        	Integer.parseInt(code.substring(0,2),16);
        } catch (Exception e) {
        	System.out.println(s);
        	throw new RuntimeException(e.getMessage());
        }
        
        // The addressing mode may be complex. The emulator spews the calcualted address
        // in these cases. If the target address is one of the special addresses, the
        // numerical location is replaced with the special name. We are only interestead
        // in specials here, so only make note of specials.
        
        // disasm:
        // sta GRP1
        // lda #02
        // lda (8b),y = ff36
        
        disasm = disasm.trim();
        
        String ha = "";
        int i = disasm.indexOf("=");
        if(i>=0) {
        	ha = disasm.substring(i+1).trim();
        } else {
        	i = disasm.indexOf(" ");
        	if(i>=0) {
        		ha = disasm.substring(i+1).trim();
        	}
        }
        
        if(isToken(ha)) {
        	// Note that it is a special register
        	hardwareAccess = ha;
        } else if(ha.length()==2) {
        	// Note that it is a memory address
        	hardwareAccessAddress = Integer.parseInt(ha,16);
        }
        
        // If a special register is involved, we need to know if it was
        // a read or write, and if it was a write we need to know the 
        // written value. Too bad the emulator doesn't report this directly,
        // but we can figure it out from the assembly.
        if(hardwareAccess!=null) {
        	hardwareAccessValue = -1;
            if(disasm.startsWith("lda")) {
                hardwareWrite = false;                
            } else if(disasm.startsWith("sta")) {
                hardwareWrite =  true;
                hardwareAccessValue = aRegister;
            } else if(disasm.startsWith("sty")) {
                hardwareWrite =  true;
                hardwareAccessValue = yRegister;
            } else if(disasm.startsWith("stx")) {
                hardwareWrite =  true;
                hardwareAccessValue = xRegister;
            } else if(disasm.startsWith("bit")) {
                hardwareWrite = false;
            } else if(disasm.startsWith("and")) {
                hardwareWrite = false;
            } else if(disasm.startsWith("ldx")) {
                hardwareWrite = false;
            } else if(disasm.startsWith("ldy")) {
                hardwareWrite = false;
            } else if(disasm.startsWith("php")) {
            	hardwareWrite =  true;
                hardwareAccessValue = flagsRegister;
            } else if(disasm.startsWith("pha")) {
            	hardwareWrite =  true;
                hardwareAccessValue = aRegister;
            } else if(disasm.startsWith("plp")) {
            	hardwareWrite = false;
            } else if(disasm.startsWith("pla")) {
            	hardwareWrite = false;
            } else if(disasm.startsWith("ora")) {
            	hardwareWrite = false;
            } else if(disasm.startsWith("lsr")) {
            	hardwareWrite = false;
            } else if(disasm.startsWith("cpy")) {
            	hardwareWrite = false;
            }
            else {
            	// We should have covered all possible reads/writes above,
            	// but if we missed some we'll get here. Find out what it is
            	// and add it to the list.
            	System.out.println(s);
            	System.out.println(code+":"+disasm);
                throw new RuntimeException("Need to know about this:"+disasm);
            }
        }
                        
        if(useInfo==null) return;
        if(hardwareAccess==null) return;
        
        Map<String,List<Integer>> infoForAddress = useInfo.get(codeAddress);
        if(infoForAddress==null) {
        	infoForAddress = new HashMap<String,List<Integer>>();
        	useInfo.put(codeAddress, infoForAddress);
        }
        
        List<Integer> infoOnAccess = infoForAddress.get(hardwareAccess);
        if(infoOnAccess == null) {
        	infoOnAccess = new ArrayList<Integer>();
        	infoForAddress.put(hardwareAccess, infoOnAccess);
        }
        
        if(!infoOnAccess.contains(line)) {
        	infoOnAccess.add(line);
        }
        
    }
    
    public String toString() {
        String ret = "";
        ret = ret + "FRAME: "+frame +"\r\n";
        ret = ret + "LINE: "+line +"\r\n";
        ret = ret + "CYCLE: "+cycle +"\r\n";
        ret = ret + "CLOCK: "+clock +"\r\n";
        
        ret = ret + ":POPOS "+p0Pos +"\r\n";
        ret = ret + ":P1POS "+p1Pos +"\r\n";
        ret = ret + ":M0POS "+m0Pos +"\r\n";
        ret = ret + ":M1POS "+m1Pos +"\r\n";
        ret = ret + ":BPOS "+bPos +"\r\n";
        
        ret = ret + ":A "+ aRegister +"\r\n";
        ret = ret + ":X "+ xRegister +"\r\n";
        ret = ret + ":Y "+ yRegister +"\r\n";
        ret = ret + ":SP "+ spRegister +"\r\n";
        ret = ret + ":PC "+ pcRegister +"\r\n";
        
        ret = ret +":"+code+":";
        ret = ret +":"+disasm+":";
        
        if(hardwareAccess!=null) {
            ret=ret+":"+hardwareAccess+":\r\n";
            ret=ret+":"+hardwareWrite+"\r\n";
            ret=ret+":"+hardwareAccessValue+"\r\n";
        }
        
        return ret;
    }
    
}