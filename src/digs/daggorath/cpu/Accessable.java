package digs.daggorath.cpu;

public interface Accessable {
	
	boolean isWordSize();
	int readValue();	
	void writeValue(int value);
	int getEffectiveAddress();	
	
}