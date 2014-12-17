package tools.code;

/**
 * Memory references carry lots of other information besides the 
 * key/value name/address. 
 */
public class AddressSpec 
{	
	
	public boolean manual;          // True if manually set. False if this comes from the code.
	public boolean isPort;          // True if this is an I/O space address
	
	public String readLabel;        // The label of the address when read
	public String writeLabel;       // The label of the address when written
	
	public int address;             // The address itself
	public int size;                // Number of bytes consumed
	public boolean eightBitAddress; // true if this is an 8-bit address (zero/base page)
	
	public String comment;          // For disassembly
	
	/**
	 * This method parses a special disassembly comment for an address-spec.
	 * @param s the comment content
	 * @return null if OK or error message
	 */
	public String parseDisassembly(String s)
	{
		
		// F000rw name comment
		
		manual = true;
		
		// Separate the name
		int i = s.indexOf(" ");
		if(i<0) return "Expected 'value name'";
		String ad = s.substring(0,i);
		s = s.substring(i+1).trim();
		
		// Separate the value
		i = s.indexOf(" ");
		if(i<0) return "Expected 'value name'";
		String lab = s.substring(0,i);
		s = s.substring(i+1).trim();	
		
		if(ad.endsWith("p")) {
			isPort=true;
			ad = ad.substring(0,ad.length()-1);
		}
				
		// Assign read/write labels and convert address to an int
		if(ad.endsWith("rw")) {
			writeLabel = lab;
			readLabel = lab;
			ad = ad.substring(0,ad.length()-2);			
		} else if(ad.endsWith("r")) {
			readLabel = lab;
			ad = ad.substring(0,ad.length()-1);
		} else if(ad.endsWith("w")) {
			writeLabel = lab;
			ad = ad.substring(0,ad.length()-1);
		} else {
			readLabel = lab;
			writeLabel =lab;			
		}
		
		// Size
		size = 1;
		i = ad.indexOf(".");
		if(i>=0) {
			try {
				size = Integer.parseInt(ad.substring(i+1));
			} catch (Exception e) {
				return "Invalid size '"+ad.substring(i+1);
			}
		}
		
		// Convert address
		try {
			address = Integer.parseInt(ad,16);
		} catch (Exception e) {
			return "Invalid address '"+ad+"'";
		}

		// If there is a comment
		if(s.length()>0) comment = s;		
		
		return null;
	}
	
	/**
	 * This method parses a special assembly directive for an address-spec.
	 * @param s the comment content
	 * @return null if OK or error message
	 */
	public String parseAssembly(String s)
	{
		
		// rw name = value size
		
		throw new RuntimeException("TODO");
		
		//return null;
	}
	
}
