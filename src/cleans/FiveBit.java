package cleans;

public class FiveBit {
	
	static String chars = "@ 012ABCDEFGHIJKLMNOPQRSTUVWXYZ";

	public static void main(String[] args) {
		String s = "20 4e 9b 64 b8 46 0d 20 2f 40";
		String bin = "";
		
		String[] dat = s.split(" ");
		for(String d : dat) {
			int dd = Integer.parseInt(d,16);
			String bi = Integer.toString(dd,2);
			while(bi.length()<8) bi="0"+bi;
			bin = bin + bi;
		}
		//System.out.println(bin);
		
		String dataString = "";
		String decodeString = "";
		
		int pos = 0;
		while(pos<bin.length()) {
			for(int x=0;x<3;++x) {
				String a = bin.substring(pos+x*5,pos+x*5+5);
				dataString = dataString+a+"_";
				int val = Integer.parseInt(bin.substring(pos+x*5,pos+x*5+5),2);
				decodeString = decodeString + chars.charAt(val)+"     ";				
			}			
			dataString = dataString+bin.charAt(pos+15)+" ";
			pos = pos + 16;
		}
		
		System.out.println(dataString);
		System.out.println(decodeString);

	}

}
