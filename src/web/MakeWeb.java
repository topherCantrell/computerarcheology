package web;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import files.FU;

public class MakeWeb {
	
	public static void main(String [] args) throws Exception {
		
		// Load the site layout
		SiteInfo si = new SiteInfo();
		
		// Recursively delete the deploy directory
		File dep = new File(si.deployRoot.toString());
		if(dep.exists()) {
			FU.deleteRecursive(dep);
		}
				
		// Create the empty deploy directory		
		dep.mkdir();
		
		// Process all the entries	
		List<SiteInfoEntry> nodes = new ArrayList<SiteInfoEntry>();
		nodes.add(si.root);
		processEntries(si.contentRoot.toString(),si.root,nodes,si.deployRoot.toString(),si.contentRoot.toString());
		
	}
	
	private static void translateMarkupToHTML(String contentRoot, String inFile, String outFile, 
			String breadCrumbs, String siteNav, String nav) {
		
	}
	
	private static void translateCodeToHTML(String contentRoot, String inFile, String outFile, 
			String breadCrumbs, String siteNav, String nav) {
		
	}
	
	public static Object[] getBreadCrumbs(List<SiteInfoEntry> nodes) {
		
		// Don't include the last node if it has no navigation
		int end = nodes.size()-1;
		if(nodes.get(end).nav == null) {
			end = end - 1;
		}
		
		SiteInfoEntry activeNode = null;
		String crumbs = "";
				
		for(int x=1;x<=end;++x) {
			String link = "/";			
			for(int y=1;y<x+1;++y) {
				if(nodes.get(y).command.equals("dir")) {
					link = link + nodes.get(y).arg+"/";
				}
			}
			SiteInfoEntry si = nodes.get(x);
			boolean active = false;
			if(x==end) {
				activeNode = si;
				active = true;
			}
			String nav = si.nav;
			if(nav==null) {
				nav = si.arg; // dir
			}
			
			crumbs = crumbs + MakeWeb.makeCrumb(link, nav, active);
		}		
				
		Object[] ret = {crumbs, activeNode};
		return ret;
	}
	
	private static String makeCrumb(String link, String nav, boolean active) {
		if(active) {
	        return "<li class=\"active\"><strong>" + nav + "</strong></li>";
		} else {
	        return "<li><a href=\"" + link + "\">" + nav + "</a></li>";
		}
	}
	
	private static String makeNav(String link, String nav, int level, boolean active, boolean leaf, boolean opened) {
		String cl = "snn";
		if(level==0) {
			cl = "sn1";			
		}		
		if(!leaf) {
			if(opened) {
				cl = cl + " collapsed expanded";
			} else {
				cl = cl + " collapsed";
			}
		}
		if(active) {
			return "<li class=\"" + cl + "\"><span class=\"sna\"><strong>" + nav + "</strong></span>";
		} else {
			return "<li class=\"" + cl + "\"><a class=\"sna\" href=\"" + link + "\">" + nav + "</a>";
		}		
		
	}

	public static String getSiteNav(SiteInfoEntry desc, List<SiteInfoEntry> nodes, SiteInfoEntry activeNode) {
		String a = null;
		if(nodes.size()<3) {
			a = MakeWeb.makeNav("/", "Home", 0, true, true, true) + "<p></li>";
		} else {
			a = MakeWeb.makeNav("/", "Home", 0, false, true, true) + "<p></li>";
		}
		return a + MakeWeb.getSiteNavRecurse(desc, nodes, "/", 0, activeNode);
	}
	
	private static String getSiteNavRecurse(SiteInfoEntry root, List<SiteInfoEntry> nodes, String link, int level, SiteInfoEntry activeNode) {
		
		String ret = "";
		
		for(SiteInfoEntry ent : root.entries) {
			boolean active = false;
			if(ent==activeNode) {
				active = true;
			}
			boolean opened = false;
			for(SiteInfoEntry n : nodes) {
				if(n==ent) {
					opened = true;
					break;
				}
			}
			if(ent.command.equals("dir")) {
				if(ent.nav!=null) {
					boolean leaf = false;
					if(ent.leaf){
						leaf = true;
					}
					ret = ret + MakeWeb.makeNav(link+ent.arg+"/", ent.nav, level, active, leaf, opened);
					if(opened) {
						ret = ret + "<ul>";
					} else {
						ret = ret + "<ul hidden>";
					}
					ret = ret + MakeWeb.getSiteNavRecurse(ent, nodes, link+ent.arg+"/", level+1, activeNode);
					ret = ret + "</ul></li>";
				}
			} else if(ent.nav!=null) {
				ret = ret + MakeWeb.makeNav(link+ent.out, ent.nav, level, active, true, opened);
				ret = ret + "</li>";
			}
			
		}
		
		return ret;		
		
	}

	public static void processEntries(String contentRoot, SiteInfoEntry root, List<SiteInfoEntry> nodes, String dep, String cont ) throws IOException {
		
		SiteInfoEntry e = nodes.get(nodes.size()-1);
		
		for (SiteInfoEntry ent : e.entries) {
			
			String nav = null;
			if(ent.nav!=null && ent.nav.length()>0) {
				nav = ent.nav;
			}
			
			if(ent.command.equals("mark") || ent.command.equals("address")) {				
				Object[] mr = MakeWeb.getBreadCrumbs(nodes);
				String breadCrumbs = (String)mr[0];
				SiteInfoEntry activeNode = (SiteInfoEntry)mr[1];
				String siteNav = MakeWeb.getSiteNav(root, nodes, activeNode);
				MakeWeb.translateMarkupToHTML(contentRoot, cont+"/"+ent.arg, ent.out, breadCrumbs, siteNav, nav);
			} else if(ent.command.equals("code")) {
				Object[] mr = MakeWeb.getBreadCrumbs(nodes);
				String breadCrumbs = (String)mr[0];
				SiteInfoEntry activeNode = (SiteInfoEntry)mr[1];
				String siteNav = MakeWeb.getSiteNav(root, nodes, activeNode);
				MakeWeb.translateCodeToHTML(contentRoot, cont+"/"+ent.arg, ent.out, breadCrumbs, siteNav, nav);
			} 
			
			else if(ent.command.equals("copy")) {
				FU.copyFile(new File(cont+"/"+ent.arg), new File(dep+"/"+ent.arg));
			} else if(ent.command.equals("copyDir")) {
				FU.copyDirectory(new File(cont+"/"+ent.arg), new File(dep+"/"+ent.arg));
			}			
			else if(ent.command.equals("dir")) {
				// Make directory
				File nd = new File(dep+"/"+ent.arg);
				nd.mkdir();
				nodes.add(ent);
				MakeWeb.processEntries(contentRoot,root,nodes, dep+"/"+ent.arg, cont+"/"+ent.arg);
				nodes.remove(nodes.size()-1);
			} else {
				throw new RuntimeException("Unknown site layout directive '"+ent.command+"'");
			}
			
		}
		
	}

}
