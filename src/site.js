{
	
	"content_root" : "../content/",
	"deploy_root"  : "../deploy/",
	
	"entries": [
		 {"mark": "index.mark",   "out": "index.html"},	     
	     {"copy": "Arch.jpg"},	     	
	     
	     {"copyDir": "js"},
	     {"copyDir": "css"},
	     {"copyDir": "img"},
	     
	     {"dir": "Help",
	    	 "entries": [
                 {"copy": "Help.jpg"},
                 {"copy": "HelpExample1.jpg"},
                 {"copy": "HelpExample2.jpg"},
                 {"copy": "HelpExample3.jpg"},
                 {"copy": "HelpExample4.jpg"},
                 {"mark": "Help.mark", "out": "Help.html"}
	    	 ]	    	 
	     },
	     
	     {"dir": "Contact",
	    	 "entries": [
	    	     {"copy": "Contact.jpg"},
	    	     {"mark": "Contact.mark", "out": "Contact.html"}
	    	 ]	    	 
	     },
	     
	     
	     	     
	     {"dir": "Amiga", "nav": "Amiga",
	    	 "entries": [
	    	     {"mark": "Amiga.mark", "out": "index.html"},
	    	     {"copy": "Amiga.jpg"},
	    	     {"dir": "Rainbow", "nav": "Rainbow Islands",
	    	    	 "entries": [
	    	    	     {"copy": "Rainbow.jpg"},
	    	    	     {"mark": "Rainbow.mark", "out": "index.html"},
	    	    	     {"mark": "1loader_dec.mark", "out": "1loader_dec.html", "nav": "1loader_dec"},
	    	    	     {"mark": "1loader.mark", "out": "1loader.html", "nav": "1loader"},
	    	    	     {"mark": "boot.mark", "out": "boot.html", "nav": "boot"},
	    	    	     {"mark": "orig_boot.mark", "out": "orig_boot.html", "nav": "orig_boot"}
	    	    	 ]
	    	     }
	    	 ]
	     }     
	             
	 ]

}
