package files;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Path;

public class FU {
	
	/**
	 * This function does a simple checksum over the bytes in a file.
	 * @param file path to the data file
	 * @return the simple checksum
	 * @throws IOException
	 */
	public static long simpleBinaryFileChecksum(Path file) throws IOException {
		long ret = 0;		
		InputStream is = new FileInputStream(file.toString());
		while(is.available()>0) {
			ret = ret + is.read();
		}
		is.close();
		return ret;
	}

}
