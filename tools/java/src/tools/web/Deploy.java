package tools.web;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;



import com.enterprisedt.net.ftp.FTPTransferType;
import com.enterprisedt.net.ftp.FileTransferClient;

/**
 * This tool deploys the current directory (and its children) to the 
 * mirror directory on the web site. The deployment is simple. In
 * every directory the process looks for 'DirectoryList.txt'. If the
 * file exists, it contains a list of files and subdirectories (one
 * per line) to push. If the file is not found in the directory then
 * the entire directory and subdirectories are pushed. <p>
 * 
 * Usage examples:<br>
 * java ca.Deploy
 */
public class Deploy {
	
	private static String DEPLOY_LIST = "DeployList.txt";
			
	private static List<String> getListOfFilesToDeploy(String directory) throws Exception
	{
		List<String> ret = new ArrayList<String>();
		
		String fname = directory+File.separatorChar+DEPLOY_LIST;
		File f = new File(fname);
		if(f.exists()) {
			FileReader fr = new FileReader(fname);
			BufferedReader br = new BufferedReader(fr);
			while(true) {
				String g = br.readLine();
				if(g==null) break;
				g = g.trim();
				if(g.startsWith(";")) continue;
				if(g.startsWith("*")) g=g.substring(1);				
				if(g.length()==0) continue;
				ret.add(g);
			}
			br.close();
		} else {
			// No file ... take everything
			f = new File(directory);
			String [] s = f.list();
			for(String ss : s) {
				if(ss.toUpperCase().equals("DEPLOY.BAT")) continue;
				ret.add(ss);
			}
		}
		
		return ret;		
	}
	
	/*
	static int findIndicator(List<String> lines, String indicator)
	{
		
		//System.out.println("::"+indicator);
		
		int i = indicator.indexOf("+");
		if(i<0) i = indicator.indexOf("-");
		
		String first = indicator;
		String offset = null;
		
		if(i>=0) {
			first = indicator.substring(0,i);
			offset = indicator.substring(i+1);
			if(first.length()==0) first="0";
		}
		
		
		String function = null;
		String args = null;
		String multiplier = null;
		int k = first.indexOf("(");
		if(k>=0) {
			function = first.substring(0,k);
			int kk = first.lastIndexOf(")");
			args = first.substring(k+1,kk);
			multiplier = first.substring(kk+1).trim();
			if(multiplier.startsWith("*")) multiplier = multiplier.substring(1);
			if(multiplier.length()==0) multiplier = "1";
		}
		
		int index = 0;
		if(function==null) {
			index = Integer.parseInt(first);
		} else {			
			int mult = Integer.parseInt(multiplier);
			//System.out.println("FUN:"+function+":"+args+":"+mult+":");
			for(int x=0;x<mult;++x) {
				while(true) {
					String s = lines.get(index);
					++index;
					if(function.equals("startsWith")) {
						if(s.startsWith(args)) break;
					} else if(function.equals("endsWith")) {
						if(s.endsWith(args)) break;
					} else if(function.equals("contains")) {
						if(s.contains(args)) break;
					} else {
						throw new RuntimeException("Unknown function '"+function+"'");
					}					
				}
			}
			--index;
		}
		
		if(i>=0) {
			int ofs = Integer.parseInt(offset);
			if(indicator.charAt(i)=='-') {
				ofs = -ofs;
			}
			index = index + ofs;
		}
		
		//System.out.println("::INDEX "+index);
		
		return index;
		
	}
	*/
	
	static List<String> loadFile(String name, String localBase) throws IOException
	{
		List<String> ret = new ArrayList<String>();
		FileReader fr = new FileReader(name);
		BufferedReader br = new BufferedReader(fr);
		while(true) {
			String g = br.readLine();
			if(g==null) break;
			ret.add(g);
		}		
		
		// Now process includes behind the scenes
		for(int x=ret.size()-1;x>=0;--x) {
			String g = ret.get(x);
			if(!g.trim().startsWith("<!--#include ")) {
				continue;
			}
			
			ret.remove(x);
			System.out.println("  Processing include: "+g);
			
			int i = g.indexOf("\"")+1;
			int j = g.indexOf("\"",i);
			String includeName = g.substring(i,j);
			StringTokenizer st = new StringTokenizer(includeName,"/");
			String includePath = localBase;
			while(st.hasMoreElements()) {
				String a = st.nextToken();
				if(a.equals("..")) {
					i = includePath.lastIndexOf(File.separatorChar);
					includePath = includePath.substring(0,i);
				} else {
					includePath = includePath+File.separatorChar+a;								
				}
			}
			
			List<String> includeLines = loadFile(includePath,localBase);
			
			String startIndicator = "";
			i=g.indexOf("start=\"");
			if(i>=0) {
				i=i+7;
				j = g.indexOf("\"",i);
				startIndicator = g.substring(i,j);
			}
			
			String stopIndicator="";
			i=g.indexOf("stop=\"");
			if(i>=0) {
				i=i+6;
				j=g.indexOf("\"",i);
				stopIndicator = g.substring(i,j);
			}
			
			String typeIndicator="raw";
			i=g.indexOf("type=\"");
			if(i>=0) {
				i=i+6;
				j=g.indexOf("\"",i);
				typeIndicator = g.substring(i,j);
			}
			
			// Find the requested subset of the include lines
			int [] ij = LineListSubset.findStartStop(includeLines, startIndicator, stopIndicator);			
			includeLines = includeLines.subList(ij[0], ij[1]+1);			
			
			if(typeIndicator.equals("html")) {
				for(int c=0;c<includeLines.size();++c) {
					includeLines.set(c, DOCXToWeb.makeHTMLFriendly(includeLines.get(c)));
				}
			}
			
			
			// TODO ... filter the lines in includeLines
			
			ret.addAll(x,includeLines);			
			
		}
		
		br.close();
		
		return ret;
	}
	
	private static void deployHTMLFile(FileTransferClient ftp, String localPath, String localBase, String remotePath) throws Exception
	{		
		List<String> lines = loadFile(localPath,localBase);
		
		FileWriter fw = new FileWriter(localPath+".trx");
		PrintWriter pw = new PrintWriter(fw);
		
		for(String s : lines) {
			pw.println(s);
		}
		
		pw.flush();
		pw.close();		
		ftp.uploadFile(localPath+".trx", remotePath);
		File ff = new File(localPath+".trx");
		ff.delete();		
	}
	
	
	public static void deployFile(FileTransferClient ftp, String rootPath, String webRootPath, String name) throws Exception
	{
		
		// Make sure the directory exists on the web server (could be a new dig)
		ensureDirectory(ftp,webRootPath);
		
		if(name.toUpperCase().endsWith(".HTML")) {
			System.out.println(":PushingHTML:"+rootPath+name+":");
			//deployHTMLFile(ftp,localPath,localBase,name);
		} else {
			System.out.println(":Pushing:"+rootPath+name+":");
			//ftp.uploadFile(localPath,name);
		}
		
	}
	
	private static void recursiveDeploy(FileTransferClient ftp, String localBase) throws Exception
	{
		List<String> toDeploy = getListOfFilesToDeploy(localBase);
		for(String s : toDeploy) {
			String localPath = localBase+File.separatorChar+s;
			File f = new File(localPath);
			if(!f.exists()) {
				throw new RuntimeException("No such file/directory '"+localPath+"'");
			}
			if(f.isDirectory()) {
				System.out.println(":Directory:"+s);
				ensureDirectory(ftp,s);
				ftp.changeDirectory(s);
				recursiveDeploy(ftp,localPath);
				ftp.changeDirectory("..");			
			} else {
				if(localPath.toUpperCase().endsWith(".HTML")) {
					System.out.println(":PushingHTML:"+localPath+":");
					deployHTMLFile(ftp,localPath,localBase,s);
				} else {
					System.out.println(":Pushing:"+localPath+":");
					ftp.uploadFile(localPath, s);
				}
			}
		}
	}
	
	/* Used to make a backup of the site
	public static void recursivePull(FileTransferClient ftp, String localBase) throws Exception
	{		
		FTPFile[] files = ftp.directoryList(".");
        for(FTPFile file : files) {
        	String name = file.getName();    	    
        	String localPath = localBase+name;
        	String remotePath = file.getPath();
        	remotePath = remotePath.substring(0,remotePath.length()-1)+name;        	
        	if(file.isDir()) {        		
        		System.out.println(":DIR:"+remotePath+":"+localPath);
        		File f = new File(localPath);
        		if(!f.exists()) f.mkdir();
        		ftp.changeDirectory(name);
        		recursivePull(ftp,localPath+File.separatorChar);
        		ftp.changeDirectory("..");
        		continue;
        	}
        	System.out.println(":"+remotePath+":to:"+localPath+":");
        	ftp.downloadFile(localPath, remotePath);
        }		
	}
	*/
	
	private static void ensureDirectory(FileTransferClient ftp, String directory) throws Exception	
	{
		try {
			// TODO we can do better than ignoring the error.
			ftp.createDirectory(directory);
		} catch (Exception e) {}
	}
	
	public static void main(String [] args) throws Exception
	{
		FileTransferClient ftp = new FileTransferClient();
		
		if(args.length>0) {
			DEPLOY_LIST = args[0];
		}
		
		// Info is stored in an external file to avoid deploying the credentials.
		FileReader fr = new FileReader("\\projects\\web.info");
		BufferedReader br = new BufferedReader(fr);
		
        ftp.setRemoteHost(br.readLine());
        ftp.setUserName(br.readLine());
        ftp.setPassword(br.readLine());
        ftp.connect();
        ftp.changeDirectory(br.readLine());
        ftp.setContentType(FTPTransferType.BINARY);
        String CA_BASE = br.readLine();
        
        br.close();
        
        File f = new File(".");
        String currentDirectory = f.getAbsolutePath();       
        currentDirectory = currentDirectory.substring(0,currentDirectory.length()-1);        
        if(!currentDirectory.toUpperCase().startsWith(CA_BASE.toUpperCase())) {
        	throw new RuntimeException("Must be in project directory to deploy");
        }
        String s = currentDirectory.substring(CA_BASE.length());
        StringTokenizer st = new StringTokenizer(s,File.separator);        
        while(st.hasMoreTokens()) {
        	String n = st.nextToken();
        	ensureDirectory(ftp,n);
        	ftp.changeDirectory(n);        	
        }
        
        recursiveDeploy(ftp,currentDirectory.substring(0,currentDirectory.length()-1));
        
        ftp.disconnect();		
	}

}
