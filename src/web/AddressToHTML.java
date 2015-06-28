package web;


public class AddressToHTML  extends MarkupToHTML {	
	
    protected String markDownStartTable(String proc) {
		
		String[] hdrs = proc.split("\\|\\|");		
		
		if(hdrs[1].startsWith("=")) {
			hdrs[1] = hdrs[1].substring(1).trim();
			String s = "<table class=\"table table-condensed\"><thead><tr>";		
			for(int x=1;x<hdrs.length;++x) {
				s = s + "<th>" + hdrs[x].trim()+ "</th>";
			}
			return s + "</tr></thead>";
		} else {
			String s = "<table class=\"table table-condensed\"><tr>";
			s = s + makeTarget(hdrs[1]);
			for(int x=2;x<hdrs.length;++x) {
				s = s + "<td>" + hdrs[x].trim()+ "</td>";
			}
			return s + "</tr>";
		}
		 
	}
    
    private String makeTarget(String org) {
    	
    	String tar = org.trim();
    	int i = tar.indexOf(":");
		if(i>=0) {
			tar = tar.substring(0,i).trim();
		}
		
		return "<td><span class=\"siteTarget\" id=\""+tar+"\">"+org+"</span></td>";
    	
    }
	
	protected String markDownContinueTable(String proc) {
		
		// <td><span class="siteTarget" id="01B2">01B2</span></td>
		
		String[] cells = proc.split("\\|\\|");
		String s = "<tr>";
		
		s = s + makeTarget(cells[1].trim());		
		
		for(int x=2;x<cells.length;++x) {
			s = s + "<td>" + cells[x].trim() + "</td>";
		}
		return s + "</tr>";
	}	

}
