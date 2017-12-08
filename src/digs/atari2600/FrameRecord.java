package digs.atari2600;

import java.util.ArrayList;
import java.util.List;

/**
 * This class holds all the scanline cycles for a single display frame as
 * parsed from the Z26 debug spew.
 */
public class FrameRecord {
	public int frameNumber;
    public List<ScanLineCycle> scanLines = new ArrayList<ScanLineCycle>();
}
