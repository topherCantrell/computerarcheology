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
              {"copy": "TRS80Text.js"},
              {"dir": "HauntedHouse", "nav": "HauntedHouse", "entries": [
                  {"mark": "HauntedHouse.mark", "out": "index.html"},
                  {"code": "Code1.cmark", "out": "Code1.html", "nav": "Code1"},
                  {"address": "RAMUse1.mark", "out": "RAMUse1.html", "nav":"RAM Use (1st)"},
                  {"code": "Code2.cmark", "out": "Code2.html", "nav": "Code2"},
                  {"address": "RAMUse2.mark", "out": "RAMUse2.html", "nav":"RAM Use (2nd)"}, 
                  {"copy": "HauntedHouse.jpg"},
                  {"copy": "hauntedhouse.js"}
                  ]
              },
              {"dir": "Pyramid", "nav": "Pyramid", "entries": [
                  {"mark": "TRS80Pyramid.mark", "out": "index.html"},
                  {"address": "RAMUse.mark", "out": "RAMUse.html", "nav":"RAM Use"},
                  {"code": "Code.cmark", "out": "Code.html", "nav": "Code"},
                  {"copy": "TRS80Pyramid.jpg"},
                  {"copy": "trs80pyramid.js"}
                  ]
              },
              {"dir": "Xenos", "nav": "Xenos", "entries": [
                  {"mark": "Xenos.mark", "out": "index.html"},
                  {"address": "RAMUse.mark", "out": "RAMUse.html", "nav":"RAM Use"},
                  {"code": "Code.cmark", "out": "Code.html", "nav": "Code"},
                  {"copy": "Xenos.png"}               
                  ]
              }      
         ]           
       }
	     ]

}
