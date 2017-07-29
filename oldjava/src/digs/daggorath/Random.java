package digs.daggorath;

public class Random {
	
	private static int seedA;
	private static int seedB;
	private static int seedC;
	
	public static void setSeeds(int a, int b, int c) {
		seedA = a;
		seedB = b;
		seedC = c;
	}
	
	public static int getNextRandom() {
		
		for(int x=0;x<8;++x) {
			
			int a = seedC & 0xE1;	// 1110_0001		
			
			// Count the bits in a
			int b = 0;
			for(int y=0;y<8;++y) {	
				if((a & (1<<y))!=0) {
					b = b + 1;
				}				
			}
								
			// Rotate the seeds left 
			int cc = b&1;
			seedA = seedA * 2 + cc;
			cc = (seedA>>8)&1;
			seedA = seedA & 0xFF;
			
			seedB = seedB * 2 + cc;
			cc = (seedB>>8)&1;
			seedB = seedB & 0xFF;
			
			seedC = seedC * 2 + cc;
			seedC = seedC & 0xFF;
		
		}		
		
		return seedA;
	}

}
