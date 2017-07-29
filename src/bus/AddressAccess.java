package bus;

/**
 * Information about a single bus access location.
 */
public class AddressAccess {
	
	public BusType busType;  // Main or Port
	public BusDir busDir;	 // Read, Write, or Both	
	public int address;      // The numeric address			

}
