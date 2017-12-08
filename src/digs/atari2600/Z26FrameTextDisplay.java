package digs.atari2600;

import java.util.ArrayList;

public class Z26FrameTextDisplay {
    byte [][] data;
    byte [][] display;
    int frame;
    ArrayList<String> key;
    
    Z26FrameTextDisplay(int frame) {
        this.frame = frame;
        key = new ArrayList<String>();
        data = new byte[280][76];
        display = new byte[240][160];
        for(int y=0;y<280;++y) {
            for(int x=0;x<160;++x) {
                if(x<76) data[y][x] = '.';
                if(y<240) display[y][x] = '.';
            }
        }
    }
    
    public void setDisplay(int line, int clock, byte c) {
        if(c==(byte)'.') return;
        if(line<40) return; // Don't care about the overscan
        //System.out.println(line+":"+clock);
        if((line-40)<display.length && (clock-68)<display[0].length) {
            display[line-40][clock-68] = c;
        }
    }
    
    public void setData(int line, int cycle, byte c) {
        if(line<data.length && cycle<data[0].length) {
            data[line][cycle] = c;
        }
    }
    
    public String accessToString() {
        StringBuffer sb = new StringBuffer();
        sb.append("Frame "+frame+"\r\n");
        for(int y=0;y<280;++y) {
            //if(y==40 || y==259) {
            //  for(int x=0;x<82;++x) {
            //    sb.append("_");
            //  }
            //  sb.append("\r\n");
            //}
            String l = Integer.toString(y);
            while(l.length()!=3) {
                l=" "+l;
            }
            sb.append(l+"|");
            sb.append(new String(data[y],0,23));
            sb.append("|");
            sb.append(new String(data[y],23,(76-23)));
            sb.append("|");
            sb.append("\r\n");
        }
        
        return sb.toString();
    }
    
    public void setKey(char k, String desc) {
        String r = ""+k+" ="+desc;
        if(!key.contains(r)) key.add(r);
    }
    
    public String keyToString() {
        int ls = 0;
        StringBuffer sb = new StringBuffer();
        for(int x=0;x<key.size();++x) {
            String g = (String)key.get(x);
            int i = g.length();
            sb.append(g);
            ls=ls+i;
            while(i<12) {
                sb.append(" ");
                ++i;
                ++ls;
            }
            if(ls>80) {
                sb.append("\r\n");
                ls=0;
            }
        }
        if(ls!=0) sb.append("\r\n");
        return sb.toString();
    }
    
    public String toString() {
        StringBuffer sb = new StringBuffer();
        sb.append("Frame "+frame+"\r\n");
        for(int y=0;y<280;++y) {
            //if(y==40 || y==259) {
            //  for(int x=0;x<82;++x) {
            //    sb.append("_");
            //  }
            //  sb.append("\r\n");
            //}
            String l = Integer.toString(y);
            while(l.length()!=3) {
                l=" "+l;
            }
            sb.append(l+"|");
            sb.append(new String(data[y],0,23));
            sb.append("|");
            sb.append(new String(data[y],23,(76-23)));
            sb.append("|");
            sb.append("\r\n");
        }
        
        sb.append("\r\n\r\n");
        
        for(int x=0;x<display.length;++x) {
            String gg = Integer.toString(x+40);
            while(gg.length()<3) gg=" "+gg;
            sb.append(gg+" ");
            sb.append(new String(display[x]));
            sb.append("\r\n");
        }
        
        return sb.toString();
    }
    
}