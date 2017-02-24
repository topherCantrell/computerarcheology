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
             {"dir": "MoonPatrol", "nav": "Moon Patrol", "entries": [
                 {"copy": "MoonPatrol.jpg"},
                 {"copy": "MoonPatrol.js"},
                 {"mark": "MoonPatrol.mark", "out": "index.html"},
                 {"address": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
                 {"address": "Hardware.mark", "out": "Hardware.html", "nav": "Hardware"},
                 {"code": "Code.cmark", "out": "Code.html", "nav": "Code"},
                 {"separator": ""},
                 {"mark": "MoonPatrolSound.mark", "out": "MoonPatrolSound.html"},
                 {"address": "SoundRAMUse.mark", "out": "SoundRAMUse.html", "nav": "Sound RAM Use"},
                 {"address": "SoundHardware.mark", "out": "SoundHardware.html", "nav": "Sound Hardware"},
                 {"code": "SoundCode.cmark", "out": "SoundCode.html", "nav": "Sound Code"},
                 {"separator": ""},
                 {"code": "GFX1.cmark", "out": "GFX1.html", "nav": "GFX1"},
                 {"code": "GFX2.cmark", "out": "GFX2.html", "nav": "GFX2"},
                 {"code": "GFX3.cmark", "out": "GFX3.html", "nav": "GFX3"},
                 {"code": "GFX4.cmark", "out": "GFX4.html", "nav": "GFX4"},
                 {"code": "GFX5.cmark", "out": "GFX5.html", "nav": "GFX5"},              
                 {"code": "ImageBackgroundColors.cmark", "out": "ImageBackgroundColors.html", "nav": "Background Colors"},
                 {"code": "SpriteColors.cmark", "out": "SpriteColors.html", "nav": "Sprite Colors"},
                 {"code": "SpriteColorSets.cmark", "out": "SpriteColorSets.html", "nav": "Sprite Color Sets"},
                 {"code": "TextColors.cmark", "out": "TextColors.html", "nav": "Text Colors"}
                 ]
             },
             {"dir": "SpaceInvaders", "nav": "Space Invaders", "entries": [
                 {"mark": "SpaceInvaders.mark", "out": "index.html"},
                 {"copy": "SpaceInvaders.jpg"},
                 {"address": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
                 {"address": "Hardware.mark", "out": "Hardware.html", "nav": "Hardware Info"},
                 {"code": "Code.cmark", "out": "Code.html", "nav": "Code"},
                 {"separator": ""},
                 {"mark": "Chronology.mark", "out": "Chronology.html", "nav": "Chronology"},                 
                 {"copy": "Alive.jpg"},
                 {"copy": "Check23.jpg"},
                 {"copy": "Chronology.jpg"},
                 {"copy": "Diag.jpg"},
                 {"copy": "DiagRun.jpg"},
                 {"copy": "Flip.jpg"},
                 {"copy": "NoTAITO.jpg"},
                 {"copy": "SideCheck.jpg"},
                 {"copy": "SpaceInvaders.js"}
                 ]
             }
             
                         
             ]
         }
	             
	 ]

}
