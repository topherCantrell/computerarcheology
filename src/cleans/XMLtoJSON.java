package cleans;

import java.io.FileReader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

import org.json.simple.JSONArray;
import org.json.simple.parser.JSONParser;

public class XMLtoJSON {
	
	public static void main2(String [] args) throws Exception {
		Path p = Paths.get("src/cpu/6502.js");
		JSONParser parser = new JSONParser();
		JSONArray obj = (JSONArray) parser.parse(new FileReader(p.toString()));
	}
	
	public static String getValue(String target, String key) {
		int i = target.indexOf(key+"=");
		if(i<0) return null;
		i=i+key.length()+2;
		int j = target.indexOf("\"",i);
		return target.substring(i,j);
	}
	
	public static void main(String [] args) throws Exception {
		
		Path p = Paths.get("java/src/tools/processor/Family_6809.xml");
		List<String> lines = Files.readAllLines(p);
		
		for(String line : lines) {
			line = line.trim();
			//if(!line.startsWith("<op")) continue;
			if(!line.startsWith("<post")) continue;
			String opcode = getValue(line,"m6809");
			if(opcode==null) continue;
			
			String code = getValue(line,"code");
			String clocks = getValue(line,"clocks");
			//String bus = getValue(line,"bus");
			//if(bus==null) bus="";
			//String flags = getValue(line,"flags");
			//if(flags==null) flags = "";
			
			/*
			System.out.println("{\"mnem\":\""+opcode+
					"\", \"code\":\""+code+"\""+
					", \"clocks\":\""+clocks+"\""+
					", \"bus\":\""+bus+"\""+
					", \"flags\":\""+flags+"\"},");
					*/
			
			System.out.println("{\"post\":\""+opcode+
					"\", \"code\":\""+code+"\""+
					", \"clocks\":\""+clocks+"\"},");
		}
				
	}

}
