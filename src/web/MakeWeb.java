package web;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import util.FU;

public class MakeWeb {
	
	public static void main(String [] args) throws Exception {
		
		SiteInfo info = new SiteInfo("content/site.js");
		
		// Recursively delete the deploy directory
		File dep = new File(info.deployRoot.toString());
		if(dep.exists()) {
			FU.deleteRecursive(dep);
		}
				
		// Create the empty deploy directory		
		dep.mkdir();		   
		
		// Process all the entries (recursively)
		List<SiteInfoEntry> nodes = new ArrayList<SiteInfoEntry>();
		nodes.add(info.root);		
		
		String siteNav = MakeWeb.getSiteNav(info.root, nodes, null);
		//System.out.println(siteNav);
		
		processEntries(siteNav,
				info.contentRoot.toString(),
				info.root,
				nodes,
				info.deployRoot.toString(),
				info.contentRoot.toString()); // The directory is the root directory

	}
	
	// A separator list item in the site tree
	private static String makeSeparator() {
		return "<li><hr class='navSeparator'></li>";
	}
	
	// A navigation list item in the site tree (leaves the tag open in case
	// there are children to add.
	private static String makeNav(String link, String nav) {
		return "<li><a href='" + link + "'>" + nav + "</a>";		
	}

	private static String getSiteNav(SiteInfoEntry desc, List<SiteInfoEntry> nodes, SiteInfoEntry activeNode) {
		// Add a quick link back to the site's landing page
		String a = MakeWeb.makeNav("/", "Home") + "</li>\n";
		// Run the tree of information and generate an HTML nested list of links
		return a + MakeWeb.getSiteNavRecurse(desc,  "/");
	}
	
	private static String getSiteNavRecurse(SiteInfoEntry root, String link) {
		
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
					ret = ret + MakeWeb.getSiteNavRecurse(ent, link+ent.arg+"/");
					ret = ret + "</ul>\n</li>\n";
				}
			} else if(ent.nav!=null) {
				ret = ret + MakeWeb.makeNav(link+ent.out, ent.nav);
				ret = ret + "</li>\n";
			}
			
		}
		
		return ret;		
		
	}
	
	/** 
	 * Get the list of breadcrumbs for the banner navigation. This shows the path
	 * to the currently open directory of the site.
	 * @param nodes the list of site info nodes (in order of traversal)
	 * @return the HTML list for the nav bar
	 */
    private static String getBreadCrumbs(List<SiteInfoEntry> nodes) {
		
		// Don't include the last node if it has no navigation
		int end = nodes.size()-1;
		if(nodes.get(end).nav == null) {
			end = end - 1;
		}		
		
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
				active = true;
			}
			String nav = si.nav;
			if(nav==null) {
				nav = si.arg; // dir
			}
			
			crumbs = crumbs + MakeWeb.makeCrumb(link, nav, active);
		}		
				
		return crumbs;
	}
	
    /**
     * Make a list item for the navigation -- either a link or a span
     * @param link the href of the anchor
     * @param nav the text of the item
     * @param active true if this is the last item in the list
     * @return the HTML list item
     */
	private static String makeCrumb(String link, String nav, boolean active) {
		if(active) {
	        return "<li><span>" + nav + "</span></li>";
		} else {
	        return "<li><a href=\"" + link + "\">" + nav + "</a></li>";
		}
	}
	
	/**
	 * Run a directory of the site information tree and generate the deployment directory 
	 * by executing each entry command. This is called recursively for subdirectories.
	 * @param siteNav the common site-navigation-tree
	 * @param contentRoot the root path of the content
	 * @param root the root node at this directory level
	 * @param nodes the nodes traversed to this point
	 * @param dep the root path of the deployment output
	 * @param cont the path to this directory
	 * @throws IOException
	 */
	private static void processEntries(String siteNav, String contentRoot, SiteInfoEntry root, List<SiteInfoEntry> nodes, String dep, String cont) throws IOException {
		
		SiteInfoEntry e = nodes.get(nodes.size()-1);
		
		for (SiteInfoEntry ent : e.entries) {
			
			String nav = null;
			if(ent.nav!=null && ent.nav.length()>0) {
				nav = ent.nav;
			}
									
			if(ent.command.equals("mark")) {				
				System.out.println("MARK "+cont+"/"+ent.arg+" "+dep+"/"+ent.out+" "+nav);				
				nodes.add(ent); // Add this node just for breadcrumbing
				String breadCrumbs = MakeWeb.getBreadCrumbs(nodes);
				nodes.remove(nodes.size()-1); // Now take it back off
				MarkupToHTML tr = new MarkupToHTML();
				tr.translate(contentRoot, cont+"/"+ent.arg, dep+"/"+ent.out, breadCrumbs, siteNav, nav);				
			} 
			
			else if(ent.command.equals("copy")) {
				System.out.println("COPY "+cont+"/"+ent.arg);
				FU.copyFile(new File(cont+"/"+ent.arg), new File(dep+"/"+ent.arg));
			} else if(ent.command.equals("copyDir")) {
				System.out.println("COPY_DIR "+cont+"/"+ent.arg);
				FU.copyDirectory(new File(cont+"/"+ent.arg), new File(dep+"/"+ent.arg));
			} else if(ent.command.equals("dir")) {
				System.out.println("DIR "+cont+"/"+ent.arg);
				// Make directory
				File nd = new File(dep+"/"+ent.arg);
				nd.mkdir();
				nodes.add(ent);
				MakeWeb.processEntries(siteNav,contentRoot,root,nodes, dep+"/"+ent.arg, cont+"/"+ent.arg);
				nodes.remove(nodes.size()-1);
			} else if(ent.command.equals("separator")) {
				// Separators create dividers in the navigation tree, but they have no
				// actions to process here
			} else {
				throw new RuntimeException("Unknown site layout directive '"+ent.command+"'");
			}
			
		}
		
	}

}
