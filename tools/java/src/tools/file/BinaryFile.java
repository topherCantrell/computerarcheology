package tools.file;

public class BinaryFile {
	
	public String filename;         // The name of the file	
	public String bitSwapPattern;   // Bit-swap pattern with digits 01234567
	public int size;                // The size of the data
	public int origin;              // The origin in the final memory map
	public int [] data;             // The data of the file
	
}
