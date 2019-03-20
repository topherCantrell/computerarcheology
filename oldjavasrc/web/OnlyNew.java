package web;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

public class OnlyNew {
	
	public static void recurseFind(File root, List<String> listOfFinds, boolean dirs) {
		
		File [] cc = root.listFiles();
		for(File c : cc) {
			
			if(c.isFile() && !dirs) {
				listOfFinds.add(c.getAbsolutePath());
			}
			if(c.isDirectory() && dirs) {
				listOfFinds.add(c.getAbsolutePath());
			}
			
			if(c.isDirectory()) {
				recurseFind(c,listOfFinds,dirs);
			}
						
		}
		
	}
	
	public static int indexOf(List<String> files, String name) {
		int i = name.indexOf("ploy\\");
		String n = name.substring(i);
		for(int x=0;x<files.size();++x) {
			if(files.get(x).endsWith(n)) {
				return x;
			}
		}
		return -1;
	}
	
	public static boolean compareFiles(String f1, String f2) throws IOException {
		
		try (InputStream is1 = new FileInputStream(f1);
			 InputStream is2 = new FileInputStream(f2)) 
		{
			byte [] d1 = new byte[is1.available()];
			byte [] d2 = new byte[is2.available()];
			
			if(d1.length!=d2.length) {			
				return false;
			}
			
			is1.read(d1);
			is2.read(d2);
			for(int x=0;x<d1.length;++x) {
				if(d1[x] != d2[x]) {
					return false;
				}
			}
						
			return true;
		}
		
	}
	
	public static void sortByPathSize(List<String> paths) {
		
		boolean changed = true;
		while(changed) {
			changed = false;
			for(int i = 0;i<paths.size()-1;++i) {
				String a = paths.get(i);
				String b = paths.get(i+1);
				int psa = 0;
				int j = a.indexOf("ploy\\");
				for(int k=j;k<a.length();++k) {
					if(a.charAt(k)=='\\') ++psa;
				}
				int psb = 0;
				j = b.indexOf("ploy\\");
				for(int k=j;k<b.length();++k) {
					if(b.charAt(k)=='\\') ++psb;
				}
				if(psb<psa) {
					paths.set(i,b);
					paths.set(i+1, a);
					changed = true;
				}				
			}
		}
		
	}
	
	public static void main(String[] args) throws Exception {
		
		File last = new File("lastDeploy");
		File current = new File("deploy");
		
		List<String> currentFiles = new ArrayList<String>();
		List<String> currentDirs = new ArrayList<String>();
		List<String> lastFiles = new ArrayList<String>();
		List<String> lastDirs = new ArrayList<String>();		
						
		recurseFind(current,currentFiles,false);
		recurseFind(current,currentDirs,true);
		
		recurseFind(last,lastFiles,false);
		recurseFind(last,lastDirs,true);
		
		sortByPathSize(currentDirs);
		sortByPathSize(lastDirs);
		
		for(int x=0;x<currentFiles.size();++x) {
			String c = currentFiles.get(x);
			int i = indexOf(lastFiles,c);
			if(i<0) {
				System.out.println("NEW FILE: "+c);
			} else {
				if(compareFiles(c,lastFiles.get(i))) {
					System.out.println("FILE HAS NOT CHANGED: "+c);
					File f = new File(c);
					f.delete();										
				}
			}
		}
		
		// Backwards so we delete children before parents
		for(int x=currentDirs.size()-1;x>=0;--x) {
			String c = currentDirs.get(x);
			int i = indexOf(lastDirs,c);
			if(i<0) {
				System.out.println("NEW DIR: "+c);
			} else {
				File d = new File(c);
				if(d.listFiles().length==0) {
					System.out.println("DIR HAS NOT CHANGED: "+c);
					d.delete();
				}				
			}
		}
		
		// TODO point out things that are in lastDeploy that are not in deploy. These need to be
		// deleted from remote.
		
	}

}
