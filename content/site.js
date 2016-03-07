{
	
	"content_root" : "content/",
	"deploy_root"  : "deploy/",
	
	"entries": [
		 {"mark": "index.mark",   "out": "index.html"},	     
	     {"copy": "Arch.jpg"},	     	
	     
	     {"copyDir": "js"},
	     {"copyDir": "css"},
	     {"copyDir": "img"},
	     
	     {"dir": "Help", "entries": [
             {"copy": "Help.jpg"},
             {"copy": "HelpExample1.jpg"},
             {"copy": "HelpExample2.jpg"},
             {"copy": "HelpExample3.jpg"},
             {"copy": "HelpExample4.jpg"},
             {"mark": "Help.mark", "out": "index.html"}
	    	 ]	    	 
	     },
	     
	     {"dir": "Contact",  "entries": [
	         {"copy": "Contact.jpg"},
	    	 {"mark": "Contact.mark", "out": "index.html"}
	    	 ]	    	 
	     },    	     	     
	     
	     
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
	             {"copy": "Asteroids.jpg"}
	             ]
	         },
	         
	         
	         {"dir": "OmegaRace", "nav": "Omega Race", "entries": [
	             {"mark": "OmegaRace.mark", "out":"index.html"},
                 {"address": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
                 {"address": "Hardware.mark", "out": "Hardware.html", "nav": "Hardware"},
                 {"code": "MainBoard.cmark", "out":"MainBoard.html", "nav": "Main Board"},     
                 {"separator": ""},
                 {"code": "VectorROM.cmark", "out":"VectorROM.html", "nav": "Vector ROM"},
                 {"address": "DVGPROM.mark", "out": "DVGPROM.html", "nav": "DVG PROM"},
                 {"separator": ""},
                 {"address": "SoundHardware.mark", "out": "SoundHardware.html", "nav": "Sound Hardware"},
                 {"address": "SoundRAMUse.mark", "out": "SoundRAMUse.html", "nav": "Sound RAM Use"},
	             {"code": "SoundBoard.cmark", "out":"SoundBoard.html", "nav": "Sound Code"}, 	                         
	             {"copy": "ORace.jpg"}
	             ]
	         }
	         	         
	         ]
	     },
	     
	     {"dir": "People",  "nav": "People", "entries": [	         
	         {"mark": "People.mark", "out": "index.html"},
	         {"mark": "ChrisCantrell.mark", "out": "ChrisCantrell.html", "nav": "Chris Cantrell"},
	         {"mark": "HarryHurst.mark", "out": "HarryHurst.html", "nav": "Harry Hurst"},
	         {"mark": "PatrikSevallius.mark", "out": "PatrikSevallius.html", "nav": "Patrik Sevallius"}
	         ]	    	 
	     },
	     
	     
	     
	     {"dir": "Tools", "nav": "Tools", "entries": [
	         {"mark": "Tools.mark", "out": "index.html"},
	         {"copy": "Tools.jpg"},
	                                       	                                          	                                              	         
	         {"dir": "Blend", "nav": "Blend", "leaf":true, "entries": [
	               {"copy": "Blend.jpg"},
	               {"copy": "blend.zip"},
	               {"copy": "Blend1.png"},
	               {"copy": "photo1.jpg"},
	               {"mark": "Blend.mark", "out": "index.html"}
	               ]
	         }
	         ]
	     }
	             
	 ]

}
