{
	
	"content_root" : "content/",
	"deploy_root"  : "deploy/",
	
	"entries": [
		 {"mark": "index.mark",   "out": "index.html"},	     
	     {"copy": "Arch.jpg"},	     	
	     
	     {"copyDir": "js"},
	     {"copyDir": "css"},
	     {"copyDir": "img"},	     
	     
	     {"dir": "CoCo", "nav": "CoCo", "entries": [
             {"mark": "CoCo.mark", "out": "index.html"},
             {"address": "Hardware.mark", "out": "Hardware.html", "nav":"Hardware"},
             {"copy": "PIA0.jpg"},
             {"copy": "PIA1.jpg"},
             {"copy": "SAM.jpg"},
             {"copy": "color-basic-unravelled.pdf"},
             {"copy": "disk-basic-unravelled.pdf"},
             {"copy": "extended-basic-unravelled.pdf"},
             {"copy": "super-extended-basic-unravelled.pdf"},
             {"copy": "CoCo.jpg"},
             {"copy": "CoCoTech.jpg"},
             
             {"dir": "Daggorath", "nav": "Daggorath", "entries" : [
                 {"mark": "Daggorath.mark", "out": "index.html"},
                 {"mark": "Levels.mark", "out": "levels.html", "nav":"Level Maps"},
                 {"address": "RAMUse.mark", "out": "RAMUse.html", "nav":"RAM Use"},
                 {"code": "Code.cmark", "out": "Code.html", "nav": "Code"},
                 {"copy": "Daggorath.jpg"},
                 {"copy": "daggorath.js"}
                 ]
             }
             ]           
         }
	             
	 ]

}
