package files;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.channels.FileChannel;
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
	
	/**
     * By default File#delete fails for non-empty directories, it works like "rm". 
     * We need something a little more brutual - this does the equivalent of "rm -r"
     * @param path Root File Path
     * @return true iff the file and all sub files/directories have been removed
     * @throws FileNotFoundException
     */
    public static boolean deleteRecursive(File path) throws FileNotFoundException{
        if (!path.exists()) throw new FileNotFoundException(path.getAbsolutePath());
        boolean ret = true;
        if (path.isDirectory()){
            for (File f : path.listFiles()){
                ret = ret && FU.deleteRecursive(f);
            }
        }
        return ret && path.delete();
    }
    
    public static void copyDirectory(File source, File dest) throws IOException {
    	
    	if(!dest.exists()) {
            dest.mkdir();
        }
    	
    	String dst = dest.getPath();
    	    	    	
    	for(File f : source.listFiles()) {
    		if(f.isDirectory()) {
    			throw new IOException("IMPLEMENT ME");
    		} else {
    			FU.copyFile(f, new File(dst+"/"+f.getName()));
    		}
    	}
    	
    }
    
    // TODO fix this
    
    @SuppressWarnings("resource")
    public static void copyFile(File sourceFile, File destFile) throws IOException {
    	if(!destFile.exists()) {
            destFile.createNewFile();
        }

        FileChannel source = null;
        FileChannel destination = null;

        try {
            source = new FileInputStream(sourceFile).getChannel();
            destination = new FileOutputStream(destFile).getChannel();
            destination.transferFrom(source, 0, source.size());
        }
        finally {
            if(source != null) {
                source.close();
            }
            if(destination != null) {
                destination.close();
            }
        }
    }

}
