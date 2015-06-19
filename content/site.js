{
	
	"content_root" : "../content/",
	"deploy_root"  : "../deploy/",
	
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
	     
	     	     	     	     
	     {"dir": "Amiga", "nav": "Amiga", "entries": [
	    	 {"mark": "Amiga.mark", "out": "index.html"},
	    	 {"copy": "Amiga.jpg"},
	    	 {"dir": "Rainbow", "nav": "Rainbow Islands", "entries": [
	    	     {"copy": "Rainbow.jpg"},
	    	     {"mark": "Rainbow.mark", "out": "index.html"},
	    	     {"mark": "1loader_dec.mark", "out": "1loader_dec.html", "nav": "1loader_dec"},
	    	     {"mark": "1loader.mark", "out": "1loader.html", "nav": "1loader"},
	    	     {"mark": "boot.mark", "out": "boot.html", "nav": "boot"},
	    	     {"mark": "orig_boot.mark", "out": "orig_boot.html", "nav": "orig_boot"}
	    	     ]
	    	 }
	    	 ]
	     },
	     
	     {"dir": "Arcade", "nav": "Arcade", "entries": [
	         {"mark": "Arcade.mark", "out": "index.html"},
	         {"copy": "Arcade.jpg"},
	         {"dir": "Asteroids", "nav": "Asteroids", "entries": [
	             {"mark": "Asteroids.mark", "out": "index.html"},
	             {"mark": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
	             {"mark": "Hardware.mark", "out": "Hardware.html", "nav": "Hardware"},
	             {"code": "Code.mark", "out": "Code.html", "nav": "Code"},
	             {"mark": "DVG.mark", "out": "DVG.html", "nav": "DVG"},
	             {"code": "VectorROM.mark", "out": "VectorROM.html", "nav": "Vector ROM"},
	             {"copy": "DVG.jpg"},
	             {"copy": "Asteroids.jpg"}
	             ]
	         },
	         {"dir": "Defender", "nav": "Defender", "entries": [	         
	             {"mark": "Defender.mark", "out": "index.html"},
	             {"mark": "Bank1.mark", "out": "Bank1.html", "nav":"Bank 1"},
	             {"mark": "Bank2.mark", "out": "Bank2.html", "nav":"Bank 2"},
	             {"mark": "Bank3.mark", "out": "Bank3.html", "nav":"Bank 3"},
	             {"mark": "Bank7.mark", "out": "Bank7.html", "nav":"Bank 7"},
	             {"mark": "MemoryMap.mark", "out": "MemoryMap.html", "nav":"MemoryMap"},
	             {"mark": "Sound.mark", "out": "Sound.html", "nav":"Sound"},
	             {"copy": "Defender-Theory-Early.pdf"},
	             {"copy": "Defender-Theory-Later.pdf"},
	             {"copy": "Defender.ROM.B&W.jpg"},
	             {"copy": "Defender.CPU.jpg"},
	             {"copy": "Defender.Vid.B&W.jpg"}
	             ]
	         },
	         {"dir": "Frogger", "nav": "Frogger", "entries": [
	             {"mark": "Frogger.mark", "out": "index.html"},
	             {"mark": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
	             {"code": "SoundCode.mark", "out": "SoundCode.html", "nav": "Sound Code"},
	             {"copy": "Frogger.jpg"},
	             {"copy": "FroggerFix.mp3"}
	             ]
	         },
	         {"dir": "Galaga", "nav": "Galaga", "entries": [
                 {"mark": "Galaga.mark", "out": "index.html"},
                 {"code": "CPU1.mark", "out":"CPU1.html","nav":"CPU1"},
                 {"code": "CPU2.mark", "out":"CPU2.html","nav":"CPU2"},
                 {"code": "CPU3.mark", "out":"CPU3.html","nav":"CPU3"},
                 {"copy": "Galaga.jpg"},
                 {"copy": "galaga1.jpg"},
                 {"copy": "galaga2.jpg"}
	             ]
	         },
	         
	         {"dir": "MoonPatrol", "nav": "Moon Patrol", "entries": [
                 {"copy": "MoonPatrol.jpg"},
	             
	             {"mark": "MoonPatrol.mark", "out": "index.html"},
	             {"mark": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
	             {"mark": "Hardware.mark", "out": "Hardware.html", "nav": "Hardware"},
	             {"code": "Code.cmark", "out": "Code.html", "nav": "Code"},
	             
	             {"mark": "MoonPatrolSound.mark", "out": "MoonPatrolSound.html"},
	             {"mark": "SoundRAMUse.mark", "out": "SoundRAMUse.html", "nav": "Sound RAM Use"},
	             {"mark": "SoundHardware.mark", "out": "SoundHardware.html", "nav": "Sound Hardware"},
	             {"code": "SoundCode.cmark", "out": "SoundCode.html", "nav": "Sound Code"},
	             
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
	         
	         {"dir": "OmegaRace", "nav": "Omega Race", "entries": [
                 {"mark": "MainRAMUse.mark", "out": "MainRAMUse.html", "nav": "RAM Use (Main)"},
                 {"mark": "SoundRAMUse.mark", "out": "SoundRAMUse.html", "nav": "RAM Use (Sound)"},
	             {"mark": "OmegaRace.mark", "out":"index.html"},
	             {"code": "VectorROM.mark", "out":"VectorROM.html", "nav": "Vector ROM"},
	             {"code": "MainBoard.mark", "out":"MainBoard.html", "nav": "Main Board"},
	             {"code": "SoundBoard.mark", "out":"SoundBoard.html", "nav": "Sound Board"},	             
	             {"copy": "ORace.jpg"}
	             ]
	         },
	         
	         {"dir": "Robotron", "nav": "Robotron", "entries": [
	             {"mark": "Robotron.mark", "out": "index.html"},
	             {"copy": "Robotron.jpg"},
	             {"code": "SoundCode.cmark", "out": "SoundCode.html", "nav": "Sound Code"}	                                                            
	             ]
	         },
	         
	         {"dir": "SpaceInvaders", "nav": "Space Invaders", "entries": [
	             {"mark": "SpaceInvaders.mark", "out": "index.html"},
	             {"copy": "SpaceInvaders.jpg"},
	             {"mark": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
	             {"mark": "Hardware.mark", "out": "Hardware.html", "nav": "Hardware Info"},
	             {"code": "Code.cmark", "out": "Code.html", "nav": "Code"}
	             ]
	         },
	         
	         {"dir": "TimePilot", "nav": "Time Pilot", "entries": [
	             {"copy": "TimePilot.jpg"},
	             {"mark": "TimePilot.mark", "out": "index.html"},
	             {"code": "SoundCode.cmark", "out": "SoundCode.html", "nav": "Sound Code"}
	             ]
	         }
	         	         
	         ]
	     },
	     
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
             {"dir": "EarlyWork", "nav": "My Early Work", "leaf":true, "entries": [
                 {"mark": "EarlyWork.mark", "out": "index.html"},
                 {"copy": "CoverTRS80News.jpg"},
                 {"copy": "BullsEye1.jpg"},
                 {"copy": "BullsEye2.jpg"},
                 {"copy": "Cover80Micro.jpg"},
                 {"copy": "Animal1.jpg"},
                 {"copy": "Animal2.jpg"},
                 {"copy": "Animal3.jpg"},
                 {"copy": "DOS1.jpg"},
                 {"copy": "DOS2.jpg"}
                 ]
             },
             {"dir": "MadnessMinotaur", "nav": "Madness & Minotaur", "entries": [
                 {"mark": "Madness.mark", "out": "index.html"},
                 {"address": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
                 {"code": "Code.mark", "out": "Code.html", "nav": "Code"},
                 {"copy": "Madness.jpg"},
                 {"copy": "madness.inf"},
                 {"copy": "MadGameLoop.inf"},
                 {"copy": "MadRooms.inf"},
                 {"copy": "MadRoomActions.inf"},
                 {"copy": "MadPassages.inf"},
                 {"copy": "MadItems.inf"},
                 {"copy": "MadSpells.inf"},
                 {"copy": "MadBlocks.inf"},
                 {"copy": "MadBanner.inf"},
                 {"copy": "MadDebug.inf"},
                 {"copy": "Madness.z5"},
                 {"copy": "inst.cas"},
                 {"copy": "s_one.cas"},
                 {"copy": "s_two.cas"},
                 {"copy": "s_three.cas"},
                 {"copy": "s_four.cas"},
                 {"copy": "s_five.cas"},
                 {"copy": "s_six.cas"},
                 {"copy": "s_seven.cas"}
                 ]
             },
             {"dir": "Pyramid", "nav": "Pyramid", "entries": [
             	 {"mark": "Pyramid.mark", "out": "index.html"},
                 {"address": "RAMUse.mark", "out": "RAMUse.html", "nav":"RAM Use"},
                 {"code": "Code.mark", "out": "Code.html", "nav": "Code"},
                 {"copy": "Pyramid.jpg"},
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
				 {"code": "Code.mark", "out": "Code.html", "nav": "Code"},
				 {"copy": "RaakaTu.jpg"}
                 ]
             },
             {"dir": "Bedlam", "nav": "Bedlam", "entries" : [
                 {"mark": "Bedlam.mark", "out": "index.html"},
                 {"address": "RAMUse.mark", "out": "RAMUse.html", "nav":"RAM Use"},
                 {"code": "Code.mark", "out": "Code.html", "nav": "Code"},
                 {"copy": "Bedlam.jpg"}
                 ]
             },
             {"dir": "Daggorath", "nav": "Daggorath", "entries" : [
				 {"mark": "Daggorath.mark", "out": "index.html"},
				 {"address": "RAMUse.mark", "out": "RAMUse.html", "nav":"RAM Use"},
				 {"code": "Code.mark", "out": "Code.html", "nav": "Code"},
				 {"copy": "Daggorath.jpg"}
                 ]
             }
	    	 ]	    	 
	     },
	     
	     {"dir": "People",  "nav": "People", "entries": [	         
	         {"mark": "People.mark", "out": "index.html"},
	         {"copy": "cc-187_t.JPG"}, 
	         {"mark": "ChrisCantrell.mark", "out": "ChrisCantrell.html", "nav": "Chris Cantrell"},
	         {"mark": "HarryHurst.mark", "out": "HarryHurst.html", "nav": "Harry Hurst"},
	         {"mark": "PatrikSevallius.mark", "out": "PatrikSevallius.html", "nav": "Patrik Sevallius"}
	         ]	    	 
	     }
	             
	 ]

}
