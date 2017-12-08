package digs.atari2600;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/* 
  TO DO: 
    - Vertical Delay
    - Import register initial states from a text file (there is no way for the
      tool to know what state they were in before the target frame).
    - Missle Command doesn't show the duplicate missiles on a line
    - Don't load every frame ... just the requested one to draw
 */

/*
 
 The Z26 emulator can spit out debug spew if turned on. 
 
 c:> z26 -t misscomm.bin
 
 Then quickly press F12 to turn off capture. Press F11 when you want to capture and then F12 to
 turn it off again. Be as quick as possible.
 
 c:> java Z26Frame z26.log             (show the list of frames in the data set)
 c:> java Z26Frame z26.log 1234        (render the info for frame 1234)
 
 Z26 has some other useful debugging tools:
 = takes a picture to z26.pcx

 Alt+key  Effect
 Z        Enable/disable player 0
 X        Enable/disable player 1
 C        Enable/disable missile 0
 V        Enable/disable missile 1
 B        Enable/disable ball
 N        Enable/disable playfield
 /        Enable all of the above (returns to default)

*/

public class Z26Frame {
    
    static int [] hardwareMemory = new int[0x400];
    
    public static String [] tiaRegisters = // 0x00
    {
        "VSYNC", "VBLANK","WSYNC", "RSYNC", "NUSIZ0","NUSIZ1","COLUP0","COLUP1",
        "COLUPF","COLUBK","CTRLPF","REFP0", "REFP1", "PF0",   "PF1",   "PF2",
        "RESP0", "RESP1", "RESM0", "RESM1", "RESBL", "AUDC0", "AUDC1", "AUDF0",
        "AUDF1", "AUDV0", "AUDV1", "GRP0",  "GRP1",  "ENAM0", "ENAM1", "ENABL",
        "HMP0",  "HMP1",  "HMM0",  "HMM1",  "HMBL",  "VDELP0","VDELP1","VDELBL",
        "RESMP0","RESMP1","HMOVE", "HMCLR", "CXCLR"
    };    
    public static String [] tiaRegistersTD = {
        "vV","bB","*", "#", "N", "n", "C", "c",
        "D", "d", "W", "P", "p", "0", "1", "2",
        "F", "t", "M", "m", "!", "5", "6", "E",
        "e", "7", "8", "xX","yY","tT","uU","zZ",
        "H", "h", "K", "k", "A", "G", "g", "I",
        "J", "j", "O", "R", "S"
    };
    
    public static String [] tiaReadRegisters = // 0x30
    {
        "CXM0P", "CXM1P", "CXP0FB","CXP1FB",
        "CXM0FB","CXM1FB","CXBLPF","CXPPMM",
        "INPT0", "INPT1", "INPT2", "INPT3",
        "INPT4", "INPT5"
    };    
    public static String [] tiaReadRegistersTD = {
        "+","+","+","+",
        "+","+","+","+",
        "?","?","?","?",
        "?","?"
    };
    
    public static String [] piaRegistersA = // 0x280
    {
        "SWCHA",
        "DDRA",
        "SWCHB", // Read only
        "DDRB",  // DO NOT USE
        "INTIM"
    };    
    public static String [] piaRegistersATD = {
        "@","`","!","`","%"
    };
    
    public static String [] piaRegistersB = // 0x294
    {        
        "TIM1T","TIM8T","TIM64T","T1024T"
    };    
    public static String [] piaRegistersBTD = {        
        "~","~","~","~"
    };
       
    public static int getAddress(String name) {
        for(int x=0;x<tiaRegisters.length;++x) {
            if(name.equals(tiaRegisters[x])) return x;
        }
        for(int x=0;x<tiaReadRegisters.length;++x) {
            if(name.equals(tiaReadRegisters[x])) return x+0x30;
        }
        for(int x=0;x<piaRegistersA.length;++x) {
            if(name.equals(piaRegistersA[x])) return x+0x280;
        }
        for(int x=0;x<piaRegistersB.length;++x) {
            if(name.equals(piaRegistersB[x])) return x+0x294;
        }
        throw new RuntimeException("Couldn't find hardware register named '"+name+"'");
    }
    
    // If a token is all uppercase letters/numbers and is not numeric it must be
    // a label.
    
    public static byte getCharacterForHardwareRegister(int address, boolean write, int value) {
        int cp=0;
        if(address<0x30) {
            if(!write) {
                return getCharacterForHardwareRegister(address+0x30,write,value);
            }
            if(address==0 && (value&02)!=0) cp=1;
            if(address==1 && (value&02)!=0) cp=1;
            if(address==0x1D && (value&02)!=0) cp=1;
            if(address==0x1E && (value&02)!=0) cp=1;
            if(address==0x1F && (value&02)!=0) cp=1;
            if(address==0x1B && value!=0) cp=1;
            if(address==0x1C && value!=0) cp=1;
            return (byte)tiaRegistersTD[address].charAt(cp);
        }
        if(address>=0x30 && address<=0x3d) {
            return (byte)tiaReadRegistersTD[address-0x30].charAt(0);
        }
        if(address>=0x280 && address<=0x284) {
            return (byte)piaRegistersATD[address-0x280].charAt(0);
        }
        if(address>=0x294 && address<=0x297) {
            return (byte)piaRegistersBTD[address-0x294].charAt(0);
        }
        throw new RuntimeException("Don't know about hardware address '"+Integer.toString(address,16)+"'");
    }
    
    public static void mapBits(boolean reverse, int clock, int line, Z26FrameTextDisplay disp,int numBits, int v, byte mark, int width) {
        if(!reverse) {
            int stopval = 0x100;
            int shift = 1;
            if(numBits == 4) shift=0x10;
            while(shift!=stopval) {
                byte val = (byte)'.';
                if((v&shift) != 0) val = mark;
                for(int z=0;z<width;++z) {
                    disp.setDisplay(line,clock++,val);
                }
                shift = shift*2;
            }
        } else {
            int stopval = 0;
            int shift = 0x80;
            if(numBits==4) stopval = 0x08;
            while(shift!=stopval) {
                byte val = (byte)'.';
                if((v&shift) != 0) val = mark;
                for(int z=0;z<width;++z) {
                    disp.setDisplay(line,clock++,val);
                }
                shift = shift/2;
            }
            
        }
    }
    
    public static void processTextDisplayScanLine(FrameRecord frame, int line, Z26FrameTextDisplay disp) {
    	
    	// Find the requested line in the frame record
        int cur = 0;
        ScanLineCycle s;
        while(true) {
            if(cur==frame.scanLines.size()) return;
            s = frame.scanLines.get(cur++);
            if(s.line>line) {
                return; // No such scanline in recorded data
            }
            if(s.line==line) break;
        }
        
        // Run all cycles on this line
        ScanLineCycle atZero = null;
        for(int curclock=0;curclock<228;++curclock) {
            if(s!=null) {
                if(s.clock<=0) atZero = s;
                if(s.clock>0 && atZero==null) atZero = s;
                if(s.clock+68 == curclock) {
                    // Process instruction                    
                    if(s.hardwareAccess!=null) {
                        boolean write = s.hardwareWrite;
                        int val = s.hardwareAccessValue;
                        if(write) {
                            int ad = getAddress(s.hardwareAccess);
                            hardwareMemory[ad] = val;
                        }
                    }
                    if(frame.scanLines.size()>cur) {
                        s = (ScanLineCycle)frame.scanLines.get(cur++);
                        if(s.line!=line) {
                            cur = frame.scanLines.size();
                            s=null;
                        }
                    }
                }
            }
            
            // First half of playfield is picked up at clock 0, 16, and 48
            if((curclock-68)==0) {    // PF0
                int v = hardwareMemory[getAddress("PF0")];
                mapBits(false,curclock,line,disp,4,v,(byte)'A',4);                
            }
            if((curclock-68)==16) {   // PF1
                int v = hardwareMemory[getAddress("PF1")];
                mapBits(true,curclock,line,disp,8,v,(byte)'B',4);                
            }
            if((curclock-68)==48) {   // PF2
                int v = hardwareMemory[getAddress("PF2")];
                mapBits(false,curclock,line,disp,8,v,(byte)'C',4);                
            }
            
            int flip = hardwareMemory[getAddress("CTRLPF")];
            flip = flip & 1;
            
            // Second half of playfield is picked up at clock 80, 112, 144
            if(flip==0) {
                if((curclock-68-80)==0) {	  // PF0
                    int v = hardwareMemory[getAddress("PF0")];
                    mapBits(false,curclock,line,disp,4,v,(byte)'a',4);                    
                }
                if((curclock-68-80)==16) {   // PF1
                    int v = hardwareMemory[getAddress("PF1")];
                    mapBits(true,curclock,line,disp,8,v,(byte)'b',4);                    
                }
                if((curclock-68-80)==48) {   // PF2
                    int v = hardwareMemory[getAddress("PF2")];
                    mapBits(false,curclock,line,disp,8,v,(byte)'c',4);                    
                }
            } else {
                if((curclock-68)==80) { 
                    int v = hardwareMemory[getAddress("PF2")];
                    mapBits(true,curclock,line,disp,8,v,(byte)'c',4);                    
                }
                if((curclock-68)==112) {
                    int v = hardwareMemory[getAddress("PF1")];
                    mapBits(false,curclock,line,disp,8,v,(byte)'b',4);                    
                }
                if((curclock-68)==144) {
                    int v = hardwareMemory[getAddress("PF0")];
                    mapBits(true,curclock,line,disp,4,v,(byte)'a',4);                    
                }
            }
            
            // Handle the ball ... position and size
            boolean be = (hardwareMemory[getAddress("ENABL")]&2)==2;
            int bs = (hardwareMemory[getAddress("CTRLPF")]>>4)&3;
            bs = (int)Math.pow(2,bs);
            int bvd = hardwareMemory[getAddress("VDELBL")]&1;
            if(be) {
                mapBits(false,atZero.bPos+68,atZero.line+bvd,disp,1,0x80,(byte)'O',bs);
            }
            
            // Missile 1
            boolean mis = (hardwareMemory[getAddress("ENAM1")]&2)==2;
            int ms = (hardwareMemory[getAddress("NUSIZ1")]>>4)&3;
            ms = (int)Math.pow(2,ms);
            if(mis) {
            	int shape = hardwareMemory[getAddress("NUSIZ1")]&7;                
                switch(shape) {
                case 0:
                    mapBits(false,atZero.m1Pos+68,atZero.line,disp,1,0x80,(byte)'m',ms);
                    break;
                case 1:
                	mapBits(false,atZero.m1Pos+68,atZero.line,disp,1,0x80,(byte)'m',ms);
                    mapBits(false,atZero.m1Pos+68+16,atZero.line,disp,1,0x80,(byte)'m',ms);
                    break;
                case 2:
                	mapBits(false,atZero.m1Pos+68,atZero.line,disp,1,0x80,(byte)'m',ms);
                	mapBits(false,atZero.m1Pos+68+32,atZero.line,disp,1,0x80,(byte)'m',ms);
                    break;
                case 3:
                	mapBits(false,atZero.m1Pos+68,atZero.line,disp,1,0x80,(byte)'m',ms);
                	mapBits(false,atZero.m1Pos+68+16,atZero.line,disp,1,0x80,(byte)'m',ms);
                	mapBits(false,atZero.m1Pos+68+32,atZero.line,disp,1,0x80,(byte)'m',ms);
                    break;
                case 4:
                	mapBits(false,atZero.m1Pos+68,atZero.line,disp,1,0x80,(byte)'m',ms);
                	mapBits(false,atZero.m1Pos+68+4,atZero.line,disp,1,0x80,(byte)'m',ms);
                    break;
                case 5:
                	mapBits(false,atZero.m1Pos+68,atZero.line,disp,1,0x80,(byte)'m',ms);
                    break;
                case 6:
                	mapBits(false,atZero.m1Pos+68,atZero.line,disp,1,0x80,(byte)'m',ms);
                	mapBits(false,atZero.m1Pos+68+32,atZero.line,disp,1,0x80,(byte)'m',ms);
                	mapBits(false,atZero.m1Pos+68+64,atZero.line,disp,1,0x80,(byte)'m',ms);
                    break;
                case 7:
                	mapBits(false,atZero.m1Pos+68,atZero.line,disp,1,0x80,(byte)'m',ms);
                    break;
                }
            }
            
            // Missile 0
            mis = (hardwareMemory[getAddress("ENAM0")]&2)==2;
            ms = (hardwareMemory[getAddress("NUSIZ0")]>>4)&3;
            ms = (int)Math.pow(2,ms);
            if(mis) {
            	int shape = hardwareMemory[getAddress("NUSIZ0")]&7;
            	switch(shape) {
                case 0:
                    mapBits(false,atZero.m0Pos+68,atZero.line,disp,1,0x80,(byte)'M',ms);
                    break;
                case 1:
                	mapBits(false,atZero.m0Pos+68,atZero.line,disp,1,0x80,(byte)'M',ms);
                    mapBits(false,atZero.m0Pos+68+16,atZero.line,disp,1,0x80,(byte)'M',ms);
                    break;
                case 2:
                	mapBits(false,atZero.m0Pos+68,atZero.line,disp,1,0x80,(byte)'M',ms);
                	mapBits(false,atZero.m0Pos+68+32,atZero.line,disp,1,0x80,(byte)'M',ms);
                    break;
                case 3:
                	mapBits(false,atZero.m0Pos+68,atZero.line,disp,1,0x80,(byte)'M',ms);
                	mapBits(false,atZero.m0Pos+68+16,atZero.line,disp,1,0x80,(byte)'M',ms);
                	mapBits(false,atZero.m0Pos+68+32,atZero.line,disp,1,0x80,(byte)'M',ms);
                    break;
                case 4:
                	mapBits(false,atZero.m0Pos+68,atZero.line,disp,1,0x80,(byte)'M',ms);
                	mapBits(false,atZero.m0Pos+68+4,atZero.line,disp,1,0x80,(byte)'M',ms);
                    break;
                case 5:
                	mapBits(false,atZero.m0Pos+68,atZero.line,disp,1,0x80,(byte)'M',ms);
                    break;
                case 6:
                	mapBits(false,atZero.m0Pos+68,atZero.line,disp,1,0x80,(byte)'M',ms);
                	mapBits(false,atZero.m0Pos+68+32,atZero.line,disp,1,0x80,(byte)'M',ms);
                	mapBits(false,atZero.m0Pos+68+64,atZero.line,disp,1,0x80,(byte)'M',ms);
                    break;
                case 7:
                	mapBits(false,atZero.m0Pos+68,atZero.line,disp,1,0x80,(byte)'M',ms);
                    break;
                }
            }
            
            // Player 1
            int spr = hardwareMemory[getAddress("GRP1")];
            int vdel = hardwareMemory[getAddress("VDELP1")] & 1;
            if(spr!=0) {
                int shape = hardwareMemory[getAddress("NUSIZ1")]&7;
                boolean ref = (hardwareMemory[getAddress("REFP1")]&8)==8;
                ref=!ref;
                switch(shape) {
                    case 0:
                        mapBits(ref,atZero.p1Pos+68,atZero.line+vdel,disp,8,spr,(byte)'p',1);
                        break;
                    case 1:
                        mapBits(ref,atZero.p1Pos+68,atZero.line+vdel,disp,8,spr,(byte)'p',1);
                        mapBits(ref,atZero.p1Pos+68+16,atZero.line+vdel,disp,8,spr,(byte)'p',1);
                        break;
                    case 2:
                        mapBits(ref,atZero.p1Pos+68,atZero.line+vdel,disp,8,spr,(byte)'p',1);
                        mapBits(ref,atZero.p1Pos+68+32,atZero.line+vdel,disp,8,spr,(byte)'p',1);
                        break;
                    case 3:
                        mapBits(ref,atZero.p1Pos+68,atZero.line+vdel,disp,8,spr,(byte)'p',1);
                        mapBits(ref,atZero.p1Pos+68+16,atZero.line+vdel,disp,8,spr,(byte)'p',1);
                        mapBits(ref,atZero.p1Pos+68+32,atZero.line+vdel,disp,8,spr,(byte)'p',1);
                        break;
                    case 4:
                        mapBits(ref,atZero.p1Pos+68,atZero.line+vdel,disp,8,spr,(byte)'p',1);
                        mapBits(ref,atZero.p1Pos+68+4,atZero.line+vdel,disp,8,spr,(byte)'p',1);
                        break;
                    case 5:
                        mapBits(ref,atZero.p1Pos+68,atZero.line+vdel,disp,8,spr,(byte)'p',2);
                        break;
                    case 6:
                        mapBits(ref,atZero.p1Pos+68,atZero.line+vdel,disp,8,spr,(byte)'p',1);
                        mapBits(ref,atZero.p1Pos+68+32,atZero.line+vdel,disp,8,spr,(byte)'p',1);
                        mapBits(ref,atZero.p1Pos+68+64,atZero.line+vdel,disp,8,spr,(byte)'p',1);
                        break;
                    case 7:
                        mapBits(ref,atZero.p1Pos+68,atZero.line+vdel,disp,8,spr,(byte)'p',4);
                        break;
                }
            }
            
            // Player 0
            spr = hardwareMemory[getAddress("GRP0")];
            vdel = hardwareMemory[getAddress("VDELP0")] & 1;
            if(spr!=0) {
                int shape = hardwareMemory[getAddress("NUSIZ0")]&7;
                boolean ref = (hardwareMemory[getAddress("REFP0")]&8)==8;
                ref=!ref;
                switch(shape) {
                    case 0:
                        mapBits(ref,atZero.p0Pos+68,atZero.line+vdel,disp,8,spr,(byte)'P',1);
                        break;
                    case 1:
                        mapBits(ref,atZero.p0Pos+68,atZero.line+vdel,disp,8,spr,(byte)'P',1);
                        mapBits(ref,atZero.p0Pos+68+16,atZero.line+vdel,disp,8,spr,(byte)'P',1);
                        break;
                    case 2:
                        mapBits(ref,atZero.p0Pos+68,atZero.line+vdel,disp,8,spr,(byte)'P',1);
                        mapBits(ref,atZero.p0Pos+68+32,atZero.line+vdel,disp,8,spr,(byte)'P',1);
                        break;
                    case 3:
                        mapBits(ref,atZero.p0Pos+68,atZero.line+vdel,disp,8,spr,(byte)'P',1);
                        mapBits(ref,atZero.p0Pos+68+16,atZero.line+vdel,disp,8,spr,(byte)'P',1);
                        mapBits(ref,atZero.p0Pos+68+32,atZero.line+vdel,disp,8,spr,(byte)'P',1);
                        break;
                    case 4:
                        mapBits(ref,atZero.p0Pos+68,atZero.line+vdel,disp,8,spr,(byte)'P',1);
                        mapBits(ref,atZero.p0Pos+68+4,atZero.line+vdel,disp,8,spr,(byte)'P',1);
                        break;
                    case 5:
                        mapBits(ref,atZero.p0Pos+68,atZero.line+vdel,disp,8,spr,(byte)'P',2);
                        break;
                    case 6:
                        mapBits(ref,atZero.p0Pos+68,atZero.line+vdel,disp,8,spr,(byte)'p',1);
                        mapBits(ref,atZero.p0Pos+68+32,atZero.line+vdel,disp,8,spr,(byte)'P',1);
                        mapBits(ref,atZero.p0Pos+68+64,atZero.line+vdel,disp,8,spr,(byte)'P',1);
                        break;
                    case 7:
                        mapBits(ref,atZero.p0Pos+68,atZero.line+vdel,disp,8,spr,(byte)'P',4);
                        break;
                }
            }
            
        }
        
    }
    
    
    
    public static String fixString(String s) {
        byte [] b = s.getBytes();
        byte [] bb = new byte[b.length];
        int y=0;
        for(int x=0;x<b.length;++x) {
            if(b[x]!=(byte)'\r') bb[y++] = b[x];
        }
        return new String(bb,0,y);
    }
    
    public static void textDisplay(FrameRecord c) {
        Z26FrameTextDisplay dis = new Z26FrameTextDisplay(c.frameNumber);
        
        for(int x=0;x<c.scanLines.size();++x) {
            ScanLineCycle s = (ScanLineCycle)c.scanLines.get(x);
            if(s.hardwareAccess!=null) {
                int a = getAddress(s.hardwareAccess);
                byte b = getCharacterForHardwareRegister(a,s.hardwareWrite,s.hardwareAccessValue);
                dis.setData(s.line,s.cycle,b);
                dis.setKey((char)b,s.hardwareAccess);
            }
        }
        
        for(int xx=0;xx<260;++xx) {
            processTextDisplayScanLine(c,xx,dis);
        }
        
        System.out.println(dis.keyToString());
        System.out.println(dis);
        
    }
    
    public static void command_text(List<FrameRecord> frames, String [] args) {
        FrameRecord ff = frames.get(0);
        int fn = ff.frameNumber;
        int of = 0;
        if(args[2].startsWith("+")) {
            of = Integer.parseInt(args[2].substring(1));
        } else {
            fn = Integer.parseInt(args[2]);
        }
        fn = fn + of;
        System.out.println("Z26Frame: Generating text display for frame "+fn+" ...");
        for(int x=0;x<frames.size();++x) {
            FrameRecord f = (FrameRecord)frames.get(x);
            if(f.frameNumber == fn) {
                textDisplay(f);
                return;
            }
        }
        throw new RuntimeException("Frame '"+fn+"' not found.");
    }
    
    public static void main(String [] args) throws Exception {
    	
    	if(args.length==0) {
    		String [] targs = {"content/Atari2600/Combat/combatZ26.log","30"};
    		args = targs;
    	}
        
    	int argsPos = 0;
    	
        System.out.println("Z26Frame: Loading Z26 log file '"+args[argsPos]+"' ...");
        FileReader fr = new FileReader(args[argsPos++]);
        BufferedReader br = new BufferedReader(fr);
        
        // Skip the Z26 log header
        for(int x=0;x<4;++x) {
            br.readLine();
        }
            
        // In case we want to keep up with and write the use-info to a file
        Map<Integer,Map<String,List<Integer>>> useInfo = null;
        //String useInfoFile = null;        
        if(argsPos<args.length && args[argsPos].equals("-useInfo")) {
        	useInfo = new HashMap<Integer,Map<String,List<Integer>>>();
        	++argsPos;
        	//useInfoFile = args[argsPos++];
        }        
        
        // The target frame is the one we seek out and show as text. If there is no
        // target frame given then we just print out all frame numbers.
        int targetFrame = -1;
        if(argsPos<args.length) {
        	targetFrame = Integer.parseInt(args[argsPos++]);
        }
        
        // This is a LOT of information ... too much to cache all of it
        //List<FrameRecord> frames = new ArrayList<FrameRecord>();
        FrameRecord currentFrame = new FrameRecord();        
        while(true) {
            String g = br.readLine();
            if(g==null) break;
            g=g.trim();
            if(g.length()<10) continue;
            ScanLineCycle s = new ScanLineCycle();
            s.decode(g,useInfo);            
            
            // If this is the very first frame, set its frame number
            if(currentFrame.frameNumber==0) {
                currentFrame.frameNumber = s.frame;                
            }
            
            // If this scanline belongs in the current frame, add it. Otherwise create a
            // new frame and add it there.
            if(currentFrame.frameNumber == s.frame) {
                currentFrame.scanLines.add(s);
            } else {
                if(currentFrame.scanLines.size()>0) {
                	// Dump info as we go in case we run into parse trouble
                    System.out.println("FRAME: "+currentFrame.frameNumber +" ("+currentFrame.scanLines.size()+" clock records)");
                    //frames.add(currentFrame);
                    if(targetFrame == currentFrame.frameNumber) {
                    	textDisplay(currentFrame);
                    }
                }
                currentFrame = new FrameRecord();
                currentFrame.frameNumber = s.frame;
                currentFrame.scanLines.add(s);
            }
        }
        // Dump info of the last frame
        if(currentFrame.scanLines.size()>0) {
            System.out.println("FRAME: "+currentFrame.frameNumber +" ("+currentFrame.scanLines.size()+" clock records)");
            //frames.add(currentFrame);
        }
        
        br.close();
        
               
       /* 
        
        FileWriter fw = new FileWriter(args[3]);
        PrintWriter pw = new PrintWriter(fw);
        
        if(useInfo!=null) {
        	fr = new FileReader(args[2]);
        	br = new BufferedReader(fr);
        	while(true) {
        		String g = br.readLine();
        		if(g==null) break;
        		if(g.length()<5 || g.charAt(4)!=':') {
        			pw.print(g+"\r\n");
        			continue;
        		}
        		int addr = Integer.parseInt(g.substring(0,4),16);
        		Map<String,List<Integer>> info = useInfo.get(addr);
        		if(info!=null) {
        			String inf = "";
        			for(String key : info.keySet()) {
        				inf = inf+key+":";
        				List<Integer> vals = info.get(key);
        				if(vals.size()>4) {
        					inf = inf+"lots";
        				} else {
        					for(Integer i : vals) {
        						inf = inf + i+",";
        					}
        					inf=inf.substring(0,inf.length()-1);
        				}
        				inf = inf +" ";
        			}
        			int j = g.indexOf(";");
        			if(j<0) {
        				g=g+";";
        				j = g.indexOf(";");
        			}
        			g = g + inf;
        			
        		}
        		pw.print(g+"\r\n");
        	}
        }
        pw.flush();
        pw.close();
        */
        
    }
    
}
