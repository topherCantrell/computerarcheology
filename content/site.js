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
             {"copy": "CoCoText.js"},
                          
             {"dir": "Pyramid", "nav": "Pyramid", "entries": [
                 {"mark": "Pyramid.mark", "out": "index.html"},
                 {"address": "RAMUse.mark", "out": "RAMUse.html", "nav":"RAM Use"},
                 {"code": "Code.cmark", "out": "Code.html", "nav": "Code"},
                 {"copy": "Pyramid.jpg"},
                 {"copy": "pyramid.js"},
                 {"copy": "DEFAULT.js"},
                 {"copy": "GAME.js"},
                 {"copy": "MAIN.js"},
                 {"copy": "OBJS.js"},
                 {"copy": "PARSE.js"},
                 {"copy": "ROOMS.js"},
                 {"copy": "SCRIPTER.js"}
                 ]
             }, 
             {"dir": "RaakaTu", "nav": "Raaka Tu", "entries" : [
                 {"mark": "RaakaTu.mark", "out": "index.html"},
                 {"address": "RAMUse.mark", "out": "RAMUse.html", "nav":"RAM Use"},
                 {"code": "Code.cmark", "out": "Code.html", "nav": "Code"},
                 {"copy": "RaakaTu.jpg"},
                 {"copy": "raakatu.js"}
                 ]
             },
             {"dir": "Bedlam", "nav": "Bedlam", "entries" : [
                 {"mark": "Bedlam.mark", "out": "index.html"},
                 {"address": "RAMUse.mark", "out": "RAMUse.html", "nav":"RAM Use"},
                 {"code": "Code.cmark", "out": "Code.html", "nav": "Code"},
                 {"copy": "Bedlam.jpg"},
                 {"copy": "bedlam.js"}
                 ]
             }
             ]           
         },
	     
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
