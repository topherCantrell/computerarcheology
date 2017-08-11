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
		
		System.out.println("\nDONE");
		
	}
			
	private static Object[] getBreadCrumbs(List<SiteInfoEntry> nodes) {
		
		// Don't include the last node if it has no navigation
		int end = nodes.size()-1;
		if(nodes.get(end).nav == null) {
			end = end - 1;
		}		
		
		SiteInfoEntry activeNode = null;
		String crumbs = "";
		
		if(end>0) {
			crumbs = MakeWeb.makeCrumb("/","Home",false);
		} else {
			crumbs = MakeWeb.makeCrumb("/","Home",true);
		}
				
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
	        return "<li><span>" + nav + "</span></li>";
		} else {
	        return "<li><a href=\"" + link + "\">" + nav + "</a></li>";
		}
	}
	
	private static String makeSeparator() {
		return "<li><hr class='navSeparator'></li>";
	}
	
	private static String makeNav(String link, String nav) {
		return "<li><a href='" + link + "'>" + nav + "</a>";		
	}

	private static String getSiteNav(SiteInfoEntry desc, List<SiteInfoEntry> nodes, SiteInfoEntry activeNode) {
		String a = MakeWeb.makeNav("/", "Home") + "</li>\n";
		return a + MakeWeb.getSiteNavRecurse(desc, nodes, "/");
	}
	
	private static String getSiteNavRecurse(SiteInfoEntry root, List<SiteInfoEntry> nodes, String link) {
		
		String ret = "";
		
		for(SiteInfoEntry ent : root.entries) {
			
			if(ent.command.equals("separator")) {
				ret = ret + MakeWeb.makeSeparator();
				continue;
			}			
			
			if(ent.command.equals("dir")) {
				if(ent.nav!=null) {					
					ret = ret + MakeWeb.makeNav(link+ent.arg+"/", ent.nav);
					ret = ret + "\n<ul>\n";					
					ret = ret + MakeWeb.getSiteNavRecurse(ent, nodes, link+ent.arg+"/");
					ret = ret + "</ul>\n</li>\n";
				}
			} else if(ent.nav!=null) {
				ret = ret + MakeWeb.makeNav(link+ent.out, ent.nav);
				ret = ret + "</li>\n";
			}
			
		}
		
		return ret;		
		
	}

	private static void processEntries(String contentRoot, SiteInfoEntry root, List<SiteInfoEntry> nodes, String dep, String cont ) throws IOException {
		
		SiteInfoEntry e = nodes.get(nodes.size()-1);
		
		String siteNav = MakeWeb.getSiteNav(root, nodes, null);
		
		for (SiteInfoEntry ent : e.entries) {
			
			String nav = null;
			if(ent.nav!=null && ent.nav.length()>0) {
				nav = ent.nav;
			}
									
			if(ent.command.equals("mark")) {
				System.out.println("MARK "+cont+"/"+ent.arg+" "+dep+"/"+ent.out+" "+nav);
				nodes.add(ent);
				Object[] mr = MakeWeb.getBreadCrumbs(nodes);
				String breadCrumbs = (String)mr[0];
				nodes.remove(nodes.size()-1);
				MarkupToHTML tr = new MarkupToHTML();
				tr.translate(contentRoot, cont+"/"+ent.arg, dep+"/"+ent.out, breadCrumbs, siteNav, nav);
			} else if(ent.command.equals("code")) {
				System.out.println("CODE "+cont+"/"+ent.arg+" "+dep+"/"+ent.out+" "+nav);
				nodes.add(ent);
				Object[] mr = MakeWeb.getBreadCrumbs(nodes);
				String breadCrumbs = (String)mr[0];
				nodes.remove(nodes.size()-1);
				CodeToHTML tr = new CodeToHTML();
				tr.translate(contentRoot, cont+"/"+ent.arg, dep+"/"+ent.out, breadCrumbs, siteNav, nav);
			} else if(ent.command.equals("address")) {
				System.out.println("ADDRESS "+cont+"/"+ent.arg+" "+dep+"/"+ent.out+" "+nav);
				nodes.add(ent);
				Object[] mr = MakeWeb.getBreadCrumbs(nodes);
				String breadCrumbs = (String)mr[0];
				nodes.remove(nodes.size()-1);
				AddressToHTML tr = new AddressToHTML();
				tr.translate(contentRoot, cont+"/"+ent.arg, dep+"/"+ent.out, breadCrumbs, siteNav, nav);
			}
			
			else if(ent.command.equals("copy")) {
				System.out.println("COPY "+cont+"/"+ent.arg);
				FU.copyFile(new File(cont+"/"+ent.arg), new File(dep+"/"+ent.arg));
			} else if(ent.command.equals("copyDir")) {
				System.out.println("COPY_DIR "+cont+"/"+ent.arg);
				FU.copyDirectory(new File(cont+"/"+ent.arg), new File(dep+"/"+ent.arg));
			} else if(ent.command.equals("separator")) {
				
			}
			else if(ent.command.equals("dir")) {
				System.out.println("DIR "+cont+"/"+ent.arg);
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
