package digs.trs80;

import code.CU;
import sim.DissReader;

public class Unpack {

	public static void main(String[] args) throws Exception {
		Unpack un = new Unpack();
		
		DissReader reader = new DissReader("content/trs80/hauntedhouse/Code2.cmark");
		int [] memory = new int[64*1024];
		reader.getData(memory);
				
		int pos = 0x4B51;
		//for(int x=0;x<59;++x) { For 1
		for(int x=0;x<30;++x) {
			int npos = un.parseMessage(memory,pos);
			printDump(memory,pos,npos,un.lastUnpack);
			//System.out.println(un.lastUnpack);
			pos = npos;
		}

	}
	
	private static void printDump(int[] memory, int pos, int npos, String lastUnpack) {
		System.out.println();
		System.out.println("; "+lastUnpack);
		int prpos = 0;
		while(pos<npos) {
			if((prpos%16)==0 ) {
				if(prpos!=0) System.out.println();
				System.out.print(CU.hex4(pos)+": ");
			}
			++prpos;
			System.out.print(CU.hex2(memory[pos++])+" ");			
		}
		System.out.println();
		
	}

	public int parseMessage(int [] message, int pos) {
		
		lastUnpack = "";
		
		if(message[pos]==0) throw new RuntimeException("Ouch "+CU.hex4(pos));
		int len = message[pos];
		unpack(len,message,pos+1);
		pos = pos + len*2 + 1;
		while(true) {
			if(message[pos]==0) {
				lastUnpack = lastUnpack+"[CR]";
				return pos+1;
			} else if(message[pos]==1) {				
				return pos+1;
			} else if(message[pos]==0x0A) {
				throw new RuntimeException("Yep");
			} 
			lastUnpack = lastUnpack+(char)message[pos++];
		}
					
	}
	
	
	public static final String CHARS = "?!2_\"'<>/03ABCDEFGHIJKLMNOPQRSTUVWXYZ-,.";
	
	int M01C3;
	int M01C4;
	int M01C5;
	
	int [] B0204 = new int[3];
	int posB0204;
	
	int M0202;
	int M0201;
	int M0200;
	int M01FF;	
	int M01FE;
	int M01FD;	
	
	boolean cf,zf;
	
	int ASL(int v) {
		v = v<<1;
		cf = (v>255);
		v = v & 0xFF;
		zf = (v==0);				
		return v;
	}
	
	int ROL(int v) {
		v = v << 1;
		if(cf) v = v | 1;
		cf = (v>255);
		v = v & 0xFF;
		zf = (v==0);
		return v;
	}
	
	int ADDA(int a, int v) {
		a = a + v;
		cf = (a>0xFF);
		zf = (a==0);
		return a & 0xFF;
	}
	int ADCA(int a, int v) {
		a = a + v;
		if(cf) a = a + 1;
		cf = (a>0xFF);
		zf = (a==0);
		return a & 0xFF;
	}
	
	int SUBA(int a, int v) {
		a = a - v;
		cf = (a<0);
		if(cf) a = a + 256;
		zf = (a==0);
		return a;
	}
	
	int SBCA(int a, int v) {
		a = a - v;
		if(cf) a = a - 1;
		cf = (a<0);
		if(cf) a = a + 256;
		zf = (a==0);
		return a;
	}
	
	String lastUnpack;
	
	public void unpack(int count, int [] buffer, int bufpos) {		
		
		M01C5 = 1;
		
		for(;count>0;--count) {
						
			M01FE = buffer[bufpos++];
			M01FD = buffer[bufpos++];
			posB0204 = 3;
			
			for(int cnt01C2=0;cnt01C2<3;++cnt01C2) {
				
				M01C3 = 0;
				M01C4 = 0x28;
				M01FF = 0;
				M0200 = 0;
				
				int passes = 17;
				
				cf = false;
				
				while(true) {
					M01FE = ROL(M01FE);
					M01FD = ROL(M01FD);
					passes = passes - 1;
					if(passes == 0) break;		
					
					int A = ADCA(0,0);					
					M0200 = ASL(M0200);
					M01FF = ROL(M01FF);
					A = ADDA(A,M0200);
					A = SUBA(A,M01C4);
					M0202 = A;
					
					A = M01FF;
					A = SBCA(A,M01C3);
					M0201 = A;
					
					if(cf) {
						int D = (M0201<<8) | M0202;
						int V = (M01C3<<8) | M01C4;
						D = D + V;
						M01FF = (D>>8)&0xFF;
						M0200 = (D)&0xFF;
						cf = D>0xFFFF;						
					} else {
						int D = (M0201<<8) | M0202;
						M01FF = (D>>8)&0xFF;
						M0200 = (D)&0xFF;                     
					}					
					
					cf = !cf;
				}
				
				char decoded = CHARS.charAt(M0200);
				--posB0204;
				B0204[posB0204] = decoded;					
				
			}
			
			for(int x=0;x<3;++x) {
				lastUnpack = lastUnpack + (char)B0204[x];				
			}
									
		}
		
	}

}
