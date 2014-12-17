package tools.file;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.StringTokenizer;



public class BinaryFiles {
	
	public BinaryFile [] binaryFiles;
	String rootPath;
	
	public BinaryFiles(String fileList) throws IOException
	{
		this(fileList,"");
	}
	
	public BinaryFiles(String fileList,String rootPath) throws IOException
	{
		
		this.rootPath = rootPath;
		
		// 0~rom1.bin+rom2.bin+1000~rom3.bin(01234576)
		
		StringTokenizer st = new StringTokenizer(fileList,"+");
		binaryFiles = new BinaryFile[st.countTokens()];
		int currentOrigin = 0;
		for(int x=0;x<binaryFiles.length;++x) {
			String s = st.nextToken().trim();
			int i = s.indexOf("~");
			if(i>=0) {
				currentOrigin = Integer.parseInt(s.substring(0,i).trim(),16);
				s=s.substring(i+1).trim();				
			}
			
			BinaryFile b = new BinaryFile();
			if(s.endsWith(")")) {
				int k = s.lastIndexOf("(");
				b.bitSwapPattern = s.substring(k+1,s.length()-1);
				s = s.substring(0,k);
			}
			
			b.filename = s;
			b.origin = currentOrigin;
			FileInputStream fis = new FileInputStream(rootPath+s);
			b.size = fis.available();
			b.data = new int[b.size];
			for(int y=0;y<b.size;++y) {
				int d = fis.read();
				if(b.bitSwapPattern!=null) {
					d = BinaryBitSwap.doSwap(d, b.bitSwapPattern);
				}
				b.data[y] = d;
			}
			binaryFiles[x] = b;
			currentOrigin = currentOrigin+b.size;
			fis.close();
		}
		
	}
	
	public int getLowestAddress() {
		int ret = Integer.MAX_VALUE;
		for(BinaryFile b : binaryFiles) {
			if(b.origin<ret) {
				ret = b.origin;
			}
		}
		return ret;
	}

	public int getHighestAddress() {
		int ret = 0;
		for(BinaryFile b : binaryFiles) {
			int la = b.origin+b.size-1;
			if(la>ret) {
				ret=la;
			}
		}
		return ret;
	}
	
	public void setByte(int address, int value) {
		for(BinaryFile b : binaryFiles) {
			if(address>=b.origin && address<(b.origin+b.size)) {
				b.data[address-b.origin] = value;
			}
		}
	}
	
	public int getByte(int address) {
		for(BinaryFile b : binaryFiles) {
			if(address>=b.origin && address<(b.origin+b.size)) {
				return b.data[address-b.origin];
			}
		}
		return -1;		
	}

}
