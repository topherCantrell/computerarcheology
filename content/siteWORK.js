{
	
	"content_root" : "content/",
	"deploy_root"  : "deploy/",
	
	"entries": [
		 {"mark": "index.mark",   "out": "index.html"},	     
	     {"copy": "Arch.jpg"},	     	
	     
	     {"copyDir": "js"},
	     {"copyDir": "css"},
	     {"copyDir": "img"},	     
	     
	     {"dir": "NES", "nav": "Nintendo NES", "entries": [
             {"mark": "NES.mark", "out": "index.html"},
             {"copy": "NES.jpg"},
                                                             
             {"dir": "Zelda", "nav": "Zelda", "entries": [
                 {"copy": "Zelda.jpg"},
                 {"copy": "zelda.js"},
                 {"copy": "ZeldaBanks.jpg"},
                 {"mark": "Zelda.mark", "out": "index.html"},
                 {"address": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
                 {"address": "Hardware.mark", "out": "Hardware.html", "nav": "Hardware Info"},
                 {"code": "Bank0.cmark", "out": "Bank0.html", "nav": "Bank0"},
                 {"code": "Bank1.cmark", "out": "Bank1.html", "nav": "Bank1"},
                 {"code": "Bank2.cmark", "out": "Bank2.html", "nav": "Bank2"},
                 {"code": "Bank3.cmark", "out": "Bank3.html", "nav": "Bank3"},
                 {"code": "Bank4.cmark", "out": "Bank4.html", "nav": "Bank4"},
                 {"code": "Bank5.cmark", "out": "Bank5.html", "nav": "Bank5"},
                 {"code": "Bank6.cmark", "out": "Bank6.html", "nav": "Bank6"},
                 {"code": "Bank7.cmark", "out": "Bank7.html", "nav": "Bank7"}
                 ]
             }
             ]
         }
	             
	 ]

}
