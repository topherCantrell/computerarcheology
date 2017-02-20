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
            {"dir": "HauntedHouse", "nav": "HauntedHouse", "entries": [
            	{"mark": "HauntedHouse.mark", "out": "index.html"},
                {"address": "RAMUse1.mark", "out": "RAMUse1.html", "nav":"RAM Use (1st)"},
                {"address": "RAMUse2.mark", "out": "RAMUse2.html", "nav":"RAM Use (2nd)"},
                {"code": "Code1.cmark", "out": "Code1.html", "nav": "Code1"},
                {"code": "Code2.cmark", "out": "Code2.html", "nav": "Code2"},
                {"copy": "HauntedHouse.jpg"}                
                ]
            }            
            
    	 ]	    	 
     }
	             
	 ]

}
