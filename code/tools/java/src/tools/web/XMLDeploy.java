package tools.web;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.InputStream;
import java.io.PrintWriter;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

import org.jdom2.Document;
import org.jdom2.Element;
import org.jdom2.input.SAXBuilder;

import tools.code.CU;

public class XMLDeploy {
	
	static String rootPath = "c:/projects/computerarcheology/";
	static String webRootPath = "/computerarcheology.com/";
	
	static List<String> generatedFiles = new ArrayList<String>();
	
	public static void main(String [] args) throws Exception 
	{
		
		InputStream is = new FileInputStream(rootPath+"deploy.xml");		
		SAXBuilder builder = new SAXBuilder();
		Document doc = builder.build(is);	
		
		Element root = doc.getRootElement();
		
		String pp = "";
		if(args.length!=0) pp = args[0];
		
		if(pp.length()==0 || pp.startsWith("/")) {
			pp = "all"+pp;
		}
		
		StringTokenizer st = new StringTokenizer(pp,"/");
		while(st.hasMoreElements()) {
			String path = st.nextToken();
			List<Element> modules = root.getChildren("module");
			Element mod = null;
			for(Element m : modules) {
				String n = m.getAttributeValue("name");
				if(n==null) continue; // Not a visible module
				if(n.equals(path)) {
					mod = m;					
					break;
				}
			}			
			root = mod;
		}
		
		processModule(root);		
					
	}
	
	static void processModule(Element module) throws Exception {
		
		System.out.println("*** "+module.getAttributeValue("name")+":"+module.getAttributeValue("directory")+" ***");
		
		List<String> ftpPut = new ArrayList<String>();
		List<String> toDelete = new ArrayList<String>();
		List<Element> commands = module.getChildren();
		for(Element c : commands) {
			switch(c.getName()) {
			case "docToWeb":
				handleDocToWeb(module.getAttributeValue("directory"),c);
				break;
			case "codeToWeb":
				handleCodeToWeb(module.getAttributeValue("directory"),c);
				break;
			case "file":
				handleFile(module.getAttributeValue("directory"),c,ftpPut,toDelete);
				break;
			case "journalHead":
				Journal.headJournal(Integer.parseInt(c.getAttributeValue("entries")));
				break;
			case "module":				
				processModule(c);
				break;
			case "digTool":
				String dirRep = rootPath+module.getAttributeValue("directory");
				String className = c.getAttributeValue("class");
				List<Element> argEs = c.getChildren("arg");
				String [] args = new String[argEs.size()];
				for(int x=0;x<args.length;++x) {
					args[x] = argEs.get(x).getText();
					args[x] = CU.replaceAll(args[x], "{directory}", dirRep);
				}
				Class<?> tc = XMLDeploy.class.getClassLoader().loadClass(className);
				Method main = tc.getMethod("main", String[].class);				
				main.invoke(null, (Object)args);				
				break;
			default:
				throw new Exception("Unknown XML Deploy command '"+c.getName()+"'");
			}
		}
		
		FileReader fr = new FileReader("c:/projects/web.info");
		BufferedReader br = new BufferedReader(fr);
		br.readLine();
		String username = br.readLine();
		String password = br.readLine();
		br.close();
		
		if(ftpPut.size()>0) {
		PrintWriter pw = new PrintWriter(rootPath+module.getAttributeValue("directory")+"/ftpscr.txt");
			pw.println(username);
			pw.println(password);
			pw.println("bin");
			for(String s : ftpPut) {
				pw.println(s);
				System.out.println(s);
			}
			pw.println("quit");
			pw.flush();
			pw.close();
			
			System.out.println("FTP files ...");
			Process p = Runtime.getRuntime().exec("ftp -s:ftpscr.txt computerarcheology.com",null,new File(rootPath+module.getAttributeValue("directory")));		
			p.waitFor();		
			System.out.println("... FTP done.");
			
			toDelete.add(rootPath+module.getAttributeValue("directory")+"ftpscr.txt");
		}				
		
		for(String s : toDelete) {
			System.out.println("DELETE "+s);
			File f = new File(s);
			f.delete();
		}
		
	}
	
	static void handleDocToWeb(String dir,Element com) throws Exception {
		
		DOCXToWeb.main(rootPath+dir+com.getAttributeValue("doc"),
				rootPath+dir+com.getAttributeValue("html"));
		
	}
	
	static void handleCodeToWeb(String dir,Element com) throws Exception {
		
		CodeToWeb.main(rootPath+dir,com.getAttributeValue("code"),com.getAttributeValue("title"),
				com.getAttributeValue("html"),com.getAttributeValue("set"));
		
	}
	
	static void handleFile(String dir,Element com, List<String> ftpPut, List<String> toDelete) throws Exception {
		
		// 	<file name="{workspace}/tools/src/tools/processor/Family_650X.xml"/>
		String name = com.getAttributeValue("name");
		String localPath = name;
		int i = name.lastIndexOf("/");
		if(i>=0) {
			localPath = name.substring(0,i+1);
			name = name.substring(i+1);
			localPath = CU.replaceAll(localPath, "{workspace}", "c:/projects/workspace");
		} else {
			localPath = rootPath+dir;			
		}
		
		String loc = localPath+name;
		String rem = webRootPath+dir+name;
		
		if(com.getAttributeValue("delete")!=null && com.getAttributeValue("delete").equals("true")) {
			toDelete.add(loc);
		}
		
		if(com.getAttributeValue("local")!=null && com.getAttributeValue("local").equals("true")) {
			// Local file only ... nothing to push
			return;
		}
		
		System.out.println("FILE "+loc);		
		
		if(com.getAttributeValue("inc")!=null && com.getAttributeValue("inc").equals("true")) {
			DeployFile.deployHTMLFile(rootPath+dir,loc,webRootPath+dir);
			ftpPut.add("put "+loc+".trx "+rem);		
			toDelete.add(loc+".trx");
		} else {
			ftpPut.add("put "+loc+" "+rem);			
		}
		
	}

}
