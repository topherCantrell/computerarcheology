package digs.spaceinvaders;

public class RAM implements AddressBusDevice {
	
	private int[] data;	
	
	private boolean[] initialized;
	
	public RAM(int size) {
		data = new int[size];		
		data[0x1FF] = 255;
		initialized = new boolean[size];		
	}		

	@Override
	public int getByte(int address) {
		if(address==0x1FF) {
			System.out.println("READING 0x1FF from "+Integer.toString(Invaders.cpu.PC,16));
		}
		if(!initialized[address]) {
			System.out.println("OOPS "+Integer.toString(address,16));
		}
		return data[address];
	}

	@Override
	public void setByte(int address, int value) {	
		if(address==0x1FF) {
			System.out.println("WRITING 0x1FF,"+value+" from "+Integer.toString(Invaders.cpu.PC,16));
		}
		initialized[address] = true;
		data[address] = value;
	}

}
