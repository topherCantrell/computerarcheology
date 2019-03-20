package digs.atari2600;

import java.util.ArrayList;
import java.util.List;

public class RAMEntry {
	
	int address;
	
	List<Integer> writers = new ArrayList<Integer>();
	List<Integer> readers = new ArrayList<Integer>();

}
