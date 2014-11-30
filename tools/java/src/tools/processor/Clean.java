package tools.processor;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

import org.jdom.Attribute;
import org.jdom.Document;
import org.jdom.Element;
import org.jdom.input.SAXBuilder;

import tools.code.CU;

/**
 * This utility class is for manipulating, cleaning, and general access of the family XML files.
 * Any code in this class is scaffolding left over from the last cleaning operation.
 */
@SuppressWarnings("unused")
public class Clean {
	
	private static final String FILENAME="/tools/processor/Family_6809.xml";
	
	static final String [] fields = {		
		"code",   "16",		
		"m6809",  "28",	
		"clocks", "14",
		"flags",  "16",				
	};
	
	public static void main999(String [] args) throws Exception
	{
		InputStream is = Clean.class.getResourceAsStream(FILENAME);
		BufferedReader br = new BufferedReader(new InputStreamReader(is));
		while(true) {
			String g = br.readLine();
			if(g==null) break;
			if(!g.startsWith("  <op")) {
				System.out.println(g);
				continue;
			}
			
			int i = g.indexOf("mZ80=\"")+6;
			int j = g.indexOf("\"",i);
			String h = g.substring(i,j);
			int k=h.indexOf(" ");
			if(k>0) {
				String m = h.substring(0,k);
				String n = CU.padTo(m, 6) + h.substring(k+1);				
				h = n;
			}
			
			String p = g.substring(0,i)+h+g.substring(j);
			
			System.out.println(p);
			
			
			// 115
			
		}
	}
	
	@SuppressWarnings("unchecked")
	public static void main(String [] args) throws Exception
	{
		
		SAXBuilder builder = new SAXBuilder(false);		
		InputStream is = Clean.class.getResourceAsStream(FILENAME);
		Document d = builder.build(is);
		Element root = d.getRootElement();
		
		Element pf = root.getChild("opcodes");		
		List<Element> nops = pf.getChildren();
		
		/*
		List<String> attNames = new ArrayList<String>();
		for(Element no : nops) {
			for(Attribute at : (List<Attribute>)(no.getAttributes())) {
				if(!attNames.contains(at.getName())) {
					attNames.add(at.getName());
				}
			}
		}
		for(String s : attNames) System.out.println(s);
		*/
		
		
		// Sort the ops by code
		List<Element> ops = new ArrayList<Element>();
		ops.addAll(nops);		
		boolean changed=true;
		while(changed) {
			changed = false;
			for(int x=0;x<ops.size()-1;++x) {
				Element a = ops.get(x);
				Element b = ops.get(x+1);
				if(a.getAttributeValue("code").compareTo(b.getAttributeValue("code"))>0) {
					ops.set(x,b);
					ops.set(x+1, a);
					changed = true;
				}
			}
		}
		
		
		
		/*	
		
		List<String> ovs = new ArrayList<String>();	
		
		for(Element op : ops) {
			String ov = op.getAttributeValue("mZ80");
			int i = ov.indexOf(" ");
			if(i>0) ov=ov.substring(0,i);
			if(!ovs.contains(ov)) ovs.add(ov);
		}		
		for(String s : ovs) {
			System.out.println("        <KEYWORD1>"+s+"</KEYWORD1>");
		}
		*/
		
		
		for(Element op : ops) {
			String s = op.getAttributeValue("m6801");
			if(s!=null) {
				op.setAttribute("m6803",s);				
			}
		}
		
				
				
		
		for(Element op : ops) {
									
			System.out.print("  <op ");
			for(int x=0;x<fields.length;x=x+2) {
				String f = fields[x];
				int s = Integer.parseInt(fields[x+1]);			
				String ov = op.getAttributeValue(f);
				if(ov==null) ov="";
				else ov = f+"=\""+ov+"\"";
				if(ov.length()>s) {
					throw new RuntimeException("OOPS:"+ov+":");
				}
				if(ov.indexOf("/")>0 && f.charAt(0)=='m') {
					throw new RuntimeException(ov);
				}
				ov = CU.padTo(ov, s);
				System.out.print(ov+" ");
			}
			System.out.println("/>");
			//System.out.println("  </op>");
			
		}
				
		
	}

}
