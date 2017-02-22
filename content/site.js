{
	
	"content_root" : "content/",
	"deploy_root"  : "deploy/",
	
	"entries": [
		 {"mark": "index.mark",   "out": "index.html"},	     
	     {"copy": "Arch.jpg"},	     	
	     
	     {"copyDir": "js"},
	     {"copyDir": "css"},
	     {"copyDir": "img"},	     
	     
	     {"dir": "TRS80", "nav": "TRS80", "entries": [
            {"mark": "TRS80.mark", "out": "index.html"},
            {"address": "Hardware.mark", "out": "Hardware.html", "nav":"Hardware"},            
            {"copy": "TRS80.jpg"},
            {"copy": "TRS80Tech.jpg"},            
            {"dir": "Pyramid", "nav": "Pyramid", "entries": [
          	  {"mark": "TRS80Pyramid.mark", "out": "index.html"},
          	  {"address": "RAMUse.mark", "out": "RAMUse.html", "nav":"RAM Use"},
                {"code": "Code.cmark", "out": "Code.html", "nav": "Code"},
                {"copy": "TRS80Pyramid.jpg"},
                {"copy": "trs80pyramid.js"}
          	  ]
            }  
            
    	 ]	    	 
     }
	             
	 ]

}
