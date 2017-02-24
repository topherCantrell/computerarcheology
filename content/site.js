{
	
	"content_root" : "content/",
	"deploy_root"  : "deploy/",
	
	"entries": [
		 {"mark": "index.mark",   "out": "index.html"},	     
	     {"copy": "Arch.jpg"},	     	
	     
	     {"copyDir": "js"},
	     {"copyDir": "css"},
	     {"copyDir": "img"},	     
	     
	     {"dir": "Gameboy", "nav": "Gameboy", "entries": [
             {"mark": "Gameboy.mark", "out": "index.html"},
             {"copy": "Gameboy.jpg"},
                                                             
             {"dir": "Zelda", "nav": "Zelda", "entries": [
                 {"copy": "GBZelda.jpg"},
                 {"copy": "zeldaGB.js"},
                 {"mark": "GBZelda.mark", "out": "index.html"},
                 {"address": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
                 {"address": "Hardware.mark", "out": "Hardware.html", "nav": "Hardware Info"},
                 {"code": "Bank00.cmark", "out": "Bank00.html", "nav": "Bank00"},
                 {"code": "Bank01.cmark", "out": "Bank01.html", "nav": "Bank01"},
                 {"code": "Bank02.cmark", "out": "Bank02.html", "nav": "Bank02"},
                 {"code": "Bank03.cmark", "out": "Bank03.html", "nav": "Bank03"},
                 {"code": "Bank04.cmark", "out": "Bank04.html", "nav": "Bank04"},
                 {"code": "Bank05.cmark", "out": "Bank05.html", "nav": "Bank05"},
                 {"code": "Bank06.cmark", "out": "Bank06.html", "nav": "Bank06"},
                 {"code": "Bank07.cmark", "out": "Bank07.html", "nav": "Bank07"},
                 {"code": "Bank08.cmark", "out": "Bank08.html", "nav": "Bank08"},
                 {"code": "Bank09.cmark", "out": "Bank09.html", "nav": "Bank09"},
                 {"code": "Bank0A.cmark", "out": "Bank0A.html", "nav": "Bank0A"},
                 {"code": "Bank0B.cmark", "out": "Bank0B.html", "nav": "Bank0B"},
                 {"code": "Bank0C.cmark", "out": "Bank0C.html", "nav": "Bank0C"},
                 {"code": "Bank0D.cmark", "out": "Bank0D.html", "nav": "Bank0D"},
                 {"code": "Bank0E.cmark", "out": "Bank0E.html", "nav": "Bank0E"},
                 {"code": "Bank0F.cmark", "out": "Bank0F.html", "nav": "Bank0F"},    
                 {"code": "Bank10.cmark", "out": "Bank10.html", "nav": "Bank10"},
                 {"code": "Bank11.cmark", "out": "Bank11.html", "nav": "Bank11"},
                 {"code": "Bank12.cmark", "out": "Bank12.html", "nav": "Bank12"},
                 {"code": "Bank13.cmark", "out": "Bank13.html", "nav": "Bank13"},
                 {"code": "Bank14.cmark", "out": "Bank14.html", "nav": "Bank14"},
                 {"code": "Bank15.cmark", "out": "Bank15.html", "nav": "Bank15"},
                 {"code": "Bank16.cmark", "out": "Bank16.html", "nav": "Bank16"},
                 {"code": "Bank17.cmark", "out": "Bank17.html", "nav": "Bank17"},
                 {"code": "Bank18.cmark", "out": "Bank18.html", "nav": "Bank18"},
                 {"code": "Bank19.cmark", "out": "Bank19.html", "nav": "Bank19"},    
                 {"code": "Bank1A.cmark", "out": "Bank1A.html", "nav": "Bank1A"},
                 {"code": "Bank1B.cmark", "out": "Bank1B.html", "nav": "Bank1B"},
                 {"code": "Bank1C.cmark", "out": "Bank1C.html", "nav": "Bank1C"},
                 {"code": "Bank1D.cmark", "out": "Bank1D.html", "nav": "Bank1D"},
                 {"code": "Bank1E.cmark", "out": "Bank1E.html", "nav": "Bank1E"},
                 {"code": "Bank1F.cmark", "out": "Bank1F.html", "nav": "Bank1F"}                 
                 ]
             }
             ]
         }
	             
	 ]

}
