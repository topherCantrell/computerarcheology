package diss;
import java.io.*;

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

	public static void main(String [] args) throws Exception
	{

		//InputStream is = new FileInputStream(args[0]);
		
		InputStream is = new FileInputStream("content/arcade/Asteroids/035127.01");
		int addr = 0x8000;
		while(is.available()>0) {


			String f = fluff(addr/2);

			int opcode = is.read() + is.read()*256;
			String oc = fluff(opcode);
			addr+=2;
			int type = opcode>>12;
			int a = opcode&0x0FFF;    

			String rr = "???? "+Integer.toString(a,16);
			if(type>0 && type<10) {
				int b  = is.read() + is.read()*256;
				oc=oc+fluff(b);
				rr = decodeDVCTR(type,a,b);
				addr+=2;
			} else if(type==10) {
				int b  = is.read() + is.read()*256;
				oc=oc+fluff(b);
				addr+=2;
				rr = decodeDLABS(a,b);
			} else if(type==11) {
				rr = decodeDHALT(a);
			} else if(type==12) {
				rr = decodeDJSRL(a);
			} else if(type==13) {
				rr = decodeDRTSL(a);
			} else if(type==14) {
				rr = decodeDJMPL(a);
			} else if(type==15) {
				rr = decodeDSVEC(a);
			}

			while(oc.length()<11) oc=oc+" ";

			System.out.println(f+oc+rr);    

		}
		
		is.close();

	}


}
