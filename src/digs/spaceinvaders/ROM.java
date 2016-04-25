package digs.spaceinvaders;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

public class ROM implements AddressBusDevice {
	
	int[] data;
	
	//int debcnt = 0;
	
	public ROM(int size) {
		this.data = new int[size];
	}
	
	public ROM(String filename) throws IOException {		
		try(InputStream is = new FileInputStream(filename)) {
			data = new int[is.available()];
			for(int x=0;x<data.length;++x) {
				data[x] = is.read();
			}
		}				
	}

	@Override
	public int getByte(int address) {
		//System.out.println("Reading from "+Integer.toString(address,16));
		//++debcnt;
		//if(debcnt==10) System.exit(0);
		return data[address];
	}

	@Override
	public void setByte(int address, int value) {
		throw new RuntimeException("Attempt to write to ROM "+address+","+value);
	}
	
}
