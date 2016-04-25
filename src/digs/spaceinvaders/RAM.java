package digs.spaceinvaders;

public class RAM implements AddressBusDevice {
	
	private int[] data;	
	
	private boolean[] initialized;

	public RAM(int size) {
		data = new int[size];		
		initialized = new boolean[size];
	}		

	@Override
	public int getByte(int address) {
		if(!initialized[address]) {
			System.out.println("OOPS "+Integer.toString(address,16));
		}
		return data[address];
	}

	@Override
	public void setByte(int address, int value) {
		initialized[address] = true;
		data[address] = value;
	}

}
