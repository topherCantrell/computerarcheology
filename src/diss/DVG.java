package diss;
import java.io.*;

import code.CU;

public class DVG
{


	static String [] OPCODES = 
		{
		"????",
		"DVCTR",
		"DVCTR",
		"DVCTR",
		"DVCTR",
		"DVCTR",
		"DVCTR",
		"DVCTR",
		"DVCTR",
		"DVCTR",
		"DLABS",  //10
		"DHALT",  //11
		"DJSRL",  //12
		"DRTSL",  //13
		"DJMPL",  //14
		"DSVEC"   //15
		};

	static String fluff(int value)
	{
		String ret = Integer.toString(value,16);
		while(ret.length()<4) {
			ret = "0"+ret;
		}
		return ret+" ";
	}

	public static int twosComp(int val)
	{
		val = val & 0x0FFF; // 12 bits
		if(val>=0x0800) {
			val = val - 0x1000;
		}
		return val;
	}


	public static String decodeDLABS(int a, int b)
	{
		int x = twosComp(b);
		int y = twosComp(a);    
		int scale = b>>12;
		return "  DLABS("+x+","+y+",  "+scale+")"; 
	}

	public static String decodeDVCTR(int vn,int a, int b)
	{
		int y = a&0x03FF;
		if( (a&0x0400)!=0) y=-y;
		int x = b&0x03FF;
		if( (b&0x0400)!=0) x=-x;
		int z = b>>12;
		return "  DVCTR("+x+","+y+","+z+","+vn+")";
	}

	public static String decodeDHALT(int a)
	{
		if((a&0x0FFF) !=0 ) {
			return "HALT ?? 0x"+Integer.toString(a&0x0FFF,16);
		} else {
			return "HALT()";
		}
	}

	public static String decodeDJSRL(int a)
	{
		return "DJSRL(0x"+Integer.toString(a&0x0FFF,16)+")";
	}

	public static String decodeDRTSL(int a)
	{
		if((a&0x0FFF) !=0 ) {
			return "DRTSL ?? 0x"+Integer.toString(a&0x0FFF,16);
		} else {
			return "DRTSL()";
		}
	}

	public static String decodeDJMPL(int a)
	{
		return "DJMPL(0x"+Integer.toString(a&0x0FFF,16)+")";
	}

	public static String decodeDSVEC(int a)
	{
		int y = a & 0x0300;
		if( (a&0x0400)>0) y=-y;
		int x = (a & 0x03)<<8;
		if( (a&0x0004)>0) x=-x;
		int z = (a>>4)&0x0f;
		int vn = 2 + ((a >> 2) & 0x02) + ((a >> 11) & 0x01);
		return "  DSVEC("+x+","+y+","+z+","+vn+")";
	}
	
	static int [] SCALE_VALS = {512,256,128,64,32,16,8,4,2,1};
	
	static String getScale(int s) {
		switch(s) {
		case 0:
			return "scale=00(/512) ";
		case 1:
			return "scale=01(/256) ";
		case 2:
			return "scale=02(/128) ";
		case 3:
			return "scale=03(/64)  ";
		case 4:
			return "scale=04(/32)  ";
		case 5:
			return "scale=05(/16)  ";
		case 6:
			return "scale=06(/8)   ";
		case 7:
			return "scale=07(/4)   ";
		case 8:
			return "scale=08(/2)   ";
		case 9:
			return "scale=09(/1)   ";
		}
		return ""+s+"(/???) ";
	}

	public static void main(String [] args) throws Exception
	{
		
		//InputStream is = new FileInputStream(args[0]);
		
		InputStream is = new FileInputStream("content/arcade/Asteroids/rev2/035127.02");
		
		int [] data = new int[is.available()];
		for(int x=0;x<data.length;++x) {
			data[x] = is.read();
		}
		
		is.close();
		
		
		int org = 0x0800;
		int pos = 0;
		
		while(pos<data.length) {
			
			int addr = org + pos;
			
			int a = data[pos++];
			int b = data[pos++];
			
			int com = b>>4;
			
			if(com<10) { // VCTR							
				int c = data[pos++];
				int d = data[pos++];
				
				int bri = (d>>4)&15;
				String scale = getScale(com);
				int y = ((b&7)<<8) + a;
				if(y>1024) {
					y = 0-(y&1023);
				}
				String dy = String.format("%.04f", (double)(y)/SCALE_VALS[com]);
				int x = ((d&7)<<8) + c;
				if(x>1024) {
					x = 0-(x&1023);
				}
				String dx = String.format("%.04f", (double)(x)/SCALE_VALS[com]);
				
				System.out.print(CU.hex4(addr)+": "+CU.hex2(a)+" "+CU.hex2(b)+" "+CU.hex2(c)+" "+CU.hex2(d)+"    VEC  ");
				System.out.println(scale+CU.padTo("bri="+bri, 10)+CU.padTo("x="+x,10)+CU.padTo("y="+y, 10)+"("+dx+", "+dy+")");
			} else if(com==10) { // LABS
				int c = data[pos++];
				int d = data[pos++];
				
				int y = ((b&3)<<8) + a;
				int x = ((d&3)<<8) + c;								
				int baseScale = (d>>4) & 15;
				
				System.out.print(CU.hex4(addr)+": "+CU.hex2(a)+" "+CU.hex2(b)+" "+CU.hex2(c)+" "+CU.hex2(d)+"    CUR  ");
				System.out.println(getScale(baseScale)+"          "+CU.padTo("x="+x, 10)+CU.padTo("y="+y, 10));
			} else if(com==11) { // HALT
				System.out.println(CU.hex4(addr)+": "+CU.hex2(a)+" "+CU.hex2(b)+"          HALT ");				
			} else if(com==12) { // JSRL
				
				int dest = ((b&15)<<8) + a;
				dest = (dest-org)*2 + org;
				
				System.out.print(CU.hex4(addr)+": "+CU.hex2(a)+" "+CU.hex2(b)+"          JSR  ");
				System.out.println("$"+CU.hex4(dest));
			} else if(com==13) { // RTSL
				System.out.println(CU.hex4(addr)+": "+CU.hex2(a)+" "+CU.hex2(b)+"          RTS  ");				
			} else if(com==14) { // JMPL
				
				int dest = ((b&15)<<8) + a;
				dest = (dest-org)*2 + org;
				
				System.out.print(CU.hex4(addr)+": "+CU.hex2(a)+" "+CU.hex2(b)+"          JMP  ");
				System.out.println("$"+CU.hex4(dest));
			} else { // SVEC
				
				int bri = (a>>4)&15;
				int sc = ((a&8)>>2)|((b&8)>>3);
				String scale = getScale(sc);
				int y = b&7;
				if(y>3) {
					y = 0-(y&3);
				}
				String dy = String.format("%.04f", (double)(y)/SCALE_VALS[sc]);
				int x = a&7;
				if(x>3) {
					x = 0-(x&3);
				}
				String dx = String.format("%.04f", (double)(x)/SCALE_VALS[sc]);				
				
				System.out.print(CU.hex4(addr)+": "+CU.hex2(a)+" "+CU.hex2(b)+"          SVEC ");
				System.out.println(scale+CU.padTo("bri="+bri, 10)+CU.padTo("x="+x,10)+CU.padTo("y="+y, 10)+"("+dx+", "+dy+")");
			}
						
		}
		
	}


}
