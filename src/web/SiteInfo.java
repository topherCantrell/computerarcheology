package web;

import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class SiteInfo {
	
	public Path contentRoot;
	public Path deployRoot;
	
	public SiteInfoEntry root;
	
	/**
	 * This creates a SiteInfo object parsed from the input JSON file.
	 * @param siteInfoFile the name of the site info JSON file
	 * @throws IOException
	 * @throws ParseException
	 * @throws Exception
	 */
	public SiteInfo(String siteInfoFile) throws IOException, ParseException {
		
		// This never changes ... and there are no others
		Path filename = Paths.get(siteInfoFile);
		
		JSONParser parser = new JSONParser();
		JSONObject obj = (JSONObject) parser.parse(new FileReader(filename.toString()));
		
		contentRoot = Paths.get(obj.get("content_root").toString());
		deployRoot = Paths.get(obj.get("deploy_root").toString());
		
		root = new SiteInfoEntry();
		root.entries = parseEntries((JSONArray) obj.get("entries"));
		
	}
	
	private List<SiteInfoEntry> parseEntries(JSONArray obj) {
		
		List<SiteInfoEntry> ret = new ArrayList<SiteInfoEntry>();
		
		for(Object o : obj) {
			JSONObject j = (JSONObject)o;
			SiteInfoEntry ent = new SiteInfoEntry();
			
			String k = (String)j.get("mark");
			if(k!=null) {
				ent.command = "mark";
				ent.arg = k;
				ent.nav = (String)j.get("nav");
				ent.out = (String)j.get("out");
				ret.add(ent);
				continue;
			}
									
			k = (String)j.get("copy");
			if(k!=null) {
				ent.command = "copy";
				ent.arg = k;				
				ret.add(ent);
				continue;
			}
			
			k = (String)j.get("copyDir");
			if(k!=null) {
				ent.command = "copyDir";
				ent.arg = k;				
				ret.add(ent);
				continue;
			}
			
			k = (String)j.get("dir");
			if(k!=null) {
				
				Boolean le = (Boolean)j.get("leaf");
				if(le!=null) {
					ent.leaf = le;
				}
				
				ent.command = "dir";
				ent.arg = k;
				ent.nav = (String)j.get("nav");
				ent.entries = parseEntries((JSONArray) j.get("entries"));
				ret.add(ent);
				continue;
			}
			
			k= (String)j.get("separator");
			if(k!=null) {
				ent.command = "separator";
				ret.add(ent);
				continue;
			}
			
			throw new RuntimeException("Unknown entry '"+j.toString()+"'");			
			
		}
		
		return ret;
		
	}

}
