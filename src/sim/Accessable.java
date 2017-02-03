package sim;

public interface Accessable {
	
	public boolean isWordSize();
	public int readValue();	
	public void writeValue(int value);
	public int getEffectiveAddress();	
	
}