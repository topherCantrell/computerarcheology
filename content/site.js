{
	
	"content_root" : "content/",
	"deploy_root"  : "deploy/",
	
	"entries": [
		 {"mark": "index.mark",   "out": "index.html"},	     
	     {"copy": "Arch.jpg"},	     	
	     
	     {"copyDir": "js"},
	     {"copyDir": "css"},
	     {"copyDir": "img"},	
	     
	     {"dir": "Arcade", "nav": "Arcade", "entries": [
	         {"mark": "Arcade.mark", "out": "index.html"},
	         {"copy": "Arcade.jpg"},
	         {"dir": "Asteroids", "nav": "Asteroids", "entries": [
	             {"mark": "Asteroids.mark", "out": "index.html"},
	             {"address": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
	             {"address": "Hardware.mark", "out": "Hardware.html", "nav": "Hardware"},	             
	             {"code": "Code.cmark", "out": "Code.html", "nav": "Code"},
	             {"code": "VectorROM.cmark", "out": "VectorROM.html", "nav": "Vector ROM"},
	             {"separator": ""},
	             {"mark": "DVG.mark", "out": "DVG.html", "nav": "DVG"},	             
	             {"copy": "DVG.jpg"},
	             {"copy": "Asteroids.jpg"},
	             {"copy": "VectorROM.js"}
	             ]
	         },
	         
	         	         
	         ]
	     },
	     
	     ]

}
