package digs.spaceinvaders;

public interface AddressBusDevice {
	
	public int getByte(int address);
	public void setByte(int address, int value);

}
