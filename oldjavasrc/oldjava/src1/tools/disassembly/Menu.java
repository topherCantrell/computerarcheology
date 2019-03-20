
package tools.disassembly;

import java.util.ArrayList;
import java.util.List;

/**
 * This class encapsulates the information about a menu of links within
 * a disassembly file. This is used in building an HTML page.
 */
public class Menu {
	
	public int numColumns;
	public String displayName;
	public List<String> links = new ArrayList<String>();
	public List<String> displayNames = new ArrayList<String>();
	
}