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
	         {"dir": "Defender", "nav": "Defender", "entries": [	         
	             {"mark": "Defender.mark", "out": "index.html"},	             
	             {"address": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
	             {"address": "Hardware.mark", "out": "Hardware.html", "nav": "Hardware"},	             
	             {"mark": "Bank1.cmark", "out": "Bank1.html", "nav":"Bank 1"},
	             {"mark": "Bank2.cmark", "out": "Bank2.html", "nav":"Bank 2"},
	             {"mark": "Bank3.cmark", "out": "Bank3.html", "nav":"Bank 3"},
	             {"mark": "Bank7.cmark", "out": "Bank7.html", "nav":"Bank 7"},
	             {"mark": "BankFixed.cmark", "out": "BankFixed.html", "nav":"Fixed Bank"},	             
	             {"separator": ""},	             
	             {"address": "SoundRAMUse.mark", "out": "SoundRAMUse.html", "nav": "Sound RAM Use"},
	             {"address": "SoundHardware.mark", "out": "SoundHardware.html", "nav": "Sound Hardware"},
	             {"mark": "SoundCode.cmark", "out": "SoundCode.html", "nav":"Sound Code"},
	             {"copy": "Defender-Theory-Early.pdf"},
	             {"copy": "Defender-Theory-Later.pdf"},
	             {"copy": "Defender.ROM.B&W.jpg"},
	             {"copy": "Defender.CPU.jpg"},
	             {"copy": "Defender.Vid.B&W.jpg"},
	             {"copy": "Defender.jpg"}
	             ]
	         },
	         {"dir": "Frogger", "nav": "Frogger", "entries": [
	             {"mark": "Frogger.mark", "out": "index.html"},
	             {"address": "SoundRAMUse.mark", "out": "SoundRAMUse.html", "nav": "Sound RAM Use"},
	             {"address": "SoundHardware.mark", "out": "SoundHardware.html", "nav": "Sound Hardware"},	             
	             {"code": "SoundCode.cmark", "out": "SoundCode.html", "nav": "Sound Code"},
	             {"copy": "Frogger.jpg"},	             
	             {"copy": "FroggerFix.mp3"}
	             ]
	         },
	         {"dir": "Galaga", "nav": "Galaga", "entries": [
                 {"mark": "Galaga.mark", "out": "index.html"},
                 {"code": "CPU1.cmark", "out":"CPU1.html","nav":"CPU1"},
                 {"code": "CPU2.cmark", "out":"CPU2.html","nav":"CPU2"},
                 {"code": "CPU3.cmark", "out":"CPU3.html","nav":"CPU3"},
                 {"copy": "Galaga.jpg"},
                 {"copy": "galaga1.jpg"},
                 {"copy": "galaga2.jpg"}
	             ]
	         },
	         
	         {"dir": "MoonPatrol", "nav": "Moon Patrol", "entries": [
                 {"copy": "MoonPatrol.jpg"},	             
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
	         
	         {"dir": "OmegaRace", "nav": "Omega Race", "entries": [
	             {"mark": "OmegaRace.mark", "out":"index.html"},
                 {"address": "MainRAMUse.mark", "out": "MainRAMUse.html", "nav": "RAM Use"},
                 {"code": "MainBoard.cmark", "out":"MainBoard.html", "nav": "Main Board"},      
                 {"code": "VectorROM.cmark", "out":"VectorROM.html", "nav": "Vector ROM"},
                 {"separator": ""},
                 {"address": "SoundRAMUse.mark", "out": "SoundRAMUse.html", "nav": "Sound RAM Use"},
	             {"code": "SoundBoard.cmark", "out":"SoundBoard.html", "nav": "Sound Code"}, 	                         
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
	             {"copy": "SideCheck.jpg"}
	             ]
	         },
	         
	         {"dir": "TimePilot", "nav": "Time Pilot", "entries": [
	             {"copy": "TimePilot.jpg"},
	             {"mark": "TimePilot.mark", "out": "index.html"},
	             {"address": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
	             {"address": "Hardware.mark", "out": "Hardware.html", "nav": "Hardware Info"},
	             {"code": "SoundCode.cmark", "out": "SoundCode.html", "nav": "Sound Code"}
	             ]
	         }
	         	         
	         ]
	     },
	     
	     {"dir": "Atari2600", "nav": "Atari 2600", "entries": [
	         {"mark": "Atari2600.mark", "out": "index.html"},
	         {"copy": "Atari2600.jpg"},
	         {"copy": "Hardware.jpg"},
	         {"address": "Stella.mark", "out": "Stella.html", "nav": "Stella"},
	         
	         {"dir": "Asteroids", "nav": "Asteroids", "entries": [
	             {"copy": "A2600Asteroids.jpg"},
	             {"mark": "Asteroids.mark", "out": "index.html"},
	             {"address": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
	             {"code": "Code.cmark", "out": "Code.html", "nav": "Code"}
	             ]
	         },
	         
	         {"dir": "BattleZone", "nav": "BattleZone", "entries": [
	             {"copy": "A2600Battlezone.jpg"},
	             {"mark": "BattleZone.mark", "out": "index.html"},
	             {"address": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
	             {"code": "Code.cmark", "out": "Code.html", "nav": "Code"}
	             ]
	         },
	         
	         {"dir": "Chess", "nav": "Chess", "entries": [
	             {"copy": "A2600Chess.jpg"},
	             {"mark": "Chess.mark", "out": "index.html"},
	             {"address": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
	             {"code": "Code.cmark", "out": "Code.html", "nav": "Code"}
	             ]
	         },
	         
	         {"dir": "Combat", "nav": "Combat", "entries": [
	             {"copy": "A2600Combat.jpg"},
	             {"mark": "Combat.mark", "out": "index.html"},
	             {"address": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
	             {"code": "Code.cmark", "out": "Code.html", "nav": "Code"}
	             ]
	         },
	         
	         {"dir": "DoubleGap", "nav": "Double Gap", "entries": [
	             {"copy": "DoubleGap.jpg"},
	             {"mark": "DoubleGap.mark", "out": "index.html"},
	             {"mark": "DoubleGap.asm", "out": "Code.html", "nav": "Code"}
	             ]
	         },
	         
	         {"dir": "ET", "nav": "ET", "entries": [
	             {"copy": "A2600ET.jpg"},
	             {"mark": "ET.mark", "out": "index.html"},
	             {"address": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
	             {"code": "Code.cmark", "out": "Code.html", "nav": "Code"}
	             ]
	         },
	         
	         {"dir": "MissileCommand", "nav": "Missile Command", "entries": [
	             {"copy": "A2600MissileCommand.jpg"},
	             {"mark": "MissileCommand.mark", "out": "index.html"},
	             {"address": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
	             {"code": "Code.cmark", "out": "Code.html", "nav": "Code"}
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
                 {"code": "Code.cmark", "out": "Code.html", "nav": "Code"},
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
                 {"code": "Code.cmark", "out": "Code.html", "nav": "Code"},
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
				 {"code": "Code.cmark", "out": "Code.html", "nav": "Code"},
				 {"copy": "RaakaTu.jpg"}
                 ]
             },
             {"dir": "Bedlam", "nav": "Bedlam", "entries" : [
                 {"mark": "Bedlam.mark", "out": "index.html"},
                 {"address": "RAMUse.mark", "out": "RAMUse.html", "nav":"RAM Use"},
                 {"code": "Code.cmark", "out": "Code.html", "nav": "Code"},
                 {"copy": "Bedlam.jpg"}
                 ]
             },
             {"dir": "Daggorath", "nav": "Daggorath", "entries" : [
				 {"mark": "Daggorath.mark", "out": "index.html"},
				 {"address": "RAMUse.mark", "out": "RAMUse.html", "nav":"RAM Use"},
				 {"code": "Code.cmark", "out": "Code.html", "nav": "Code"},
				 {"copy": "Daggorath.jpg"}
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
	     
	     {"dir": "Gameboy", "nav": "Gameboy", "entries": [
  	         {"mark": "Gameboy.mark", "out": "index.html"},
  	         {"copy": "Gameboy.jpg"},
  	                                              	         
  	         {"dir": "Zelda", "nav": "Zelda", "entries": [
  	             {"copy": "GBZelda.jpg"},
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
  	             {"code": "Bank20.cmark", "out": "Bank20.html", "nav": "Bank20"},
	             {"code": "Bank21.cmark", "out": "Bank21.html", "nav": "Bank21"},
	             {"code": "Bank22.cmark", "out": "Bank22.html", "nav": "Bank22"},
	             {"code": "Bank23.cmark", "out": "Bank23.html", "nav": "Bank23"},
	             {"code": "Bank24.cmark", "out": "Bank24.html", "nav": "Bank24"},
	             {"code": "Bank25.cmark", "out": "Bank25.html", "nav": "Bank25"}, 	 
	             {"code": "Bank26.cmark", "out": "Bank26.html", "nav": "Bank26"},
	             {"code": "Bank27.cmark", "out": "Bank27.html", "nav": "Bank27"},
	             {"code": "Bank28.cmark", "out": "Bank28.html", "nav": "Bank28"},
	             {"code": "Bank29.cmark", "out": "Bank29.html", "nav": "Bank29"},
	             {"code": "Bank30.cmark", "out": "Bank30.html", "nav": "Bank30"},
	             {"code": "Bank31.cmark", "out": "Bank31.html", "nav": "Bank31"}  	             
  	             ]
  	         }
  	         ]
  	     },
	     
	     {"dir": "NES", "nav": "Nintendo NES", "entries": [
	         {"mark": "NES.mark", "out": "index.html"},
	         {"copy": "NES.jpg"},
	                                              	         
	         {"dir": "Zelda", "nav": "Zelda", "entries": [
	             {"copy": "Zelda.jpg"},
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
	     },
	     
	     {"dir": "Virus", "nav": "Viruses", "leaf":true, "entries": [
	         {"mark": "Virus.mark", "out": "index.html"},
	         {"copy": "Virus.jpg"},
	                                          	                                              	         
	         {"dir": "MorrisWorm", "nav": "Morris Worm", "leaf":true, "entries": [
	              {"copy": "Worm.jpg"},
	              {"copy": "wormvax.gif"},
	              {"mark": "Worm.mark", "out": "index.html"}
	              ]
	         },
	         
	         {"dir": "Stoned", "nav": "Stoned", "leaf":true, "entries": [
	              {"copy": "Stoned.jpg"},
	              {"mark": "Stoned.mark", "out": "index.html"}
	              ]
	         }
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
