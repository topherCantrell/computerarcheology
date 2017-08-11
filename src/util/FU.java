package util;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.channels.FileChannel;
import java.util.ArrayList;
import java.util.List;

public final class FU {
	
	private FU() {}
	
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
    
    /**
     * Copy all the files from one directory to another.
     * @param source the source directory
     * @param dest the destination directory
     * @throws IOException
     */
    public static void copyDirectory(File source, File dest) throws IOException {
    	
    	if(!dest.exists()) {
            dest.mkdir();
        }
    	
    	String dst = dest.getPath();
    	    	    	
    	for(File f : source.listFiles()) {
    		if(f.isDirectory()) {
    			throw new RuntimeException("IMPLEMENT ME");
    		} else {
    			FU.copyFile(f, new File(dst+"/"+f.getName()));
    		}
    	}
    	
    }
   
       
    /**
     * Copy a file from
     * @param sourceFile
     * @param destFile
     * @throws IOException
     */
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
    
    public static int[] readBinary(String ... names) throws IOException {
    	List<Integer> data = new ArrayList<Integer>();
    	
    	for(String name : names) {
    		try (InputStream is = new FileInputStream(name)) {
    			int s = is.available();
    			for(int x=0;x<s;++x) data.add(is.read());
    		}
    	}
    	
    	int [] ret = new int[data.size()];
    	for(int x=0;x<ret.length;++x) {
    		ret[x] = data.get(x);
    	}
    	
    	return ret;   	
    	
    }

}
