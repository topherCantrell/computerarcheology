{
	
	"content_root" : "content/",
	"deploy_root"  : "deploy/",
	
	"entries": [
		 {"mark": "index.mark",   "out": "index.html"},	     
	     {"copy": "Arch.jpg"},	   
	     {"copy": "favicon.ico"},
	     
	     {"copyDir": "js"},
	     {"copyDir": "css"},
	     {"copyDir": "img"},	
	     
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
	             {"mark": "Code.mark", "out": "Code.html", "nav": "Code"},
	             {"mark": "VectorROM.mark", "out": "VectorROM.html", "nav": "Vector ROM"},
	             {"separator": ""},
	             {"mark": "DVG.mark", "out": "DVG.html", "nav": "DVG"},	             
	             {"copy": "DVG.jpg"},
	             {"copy": "Asteroids.jpg"},
	             {"copy": "VectorROM.js"}
	             ]
	         },
	         {"dir": "Defender", "nav": "Defender", "entries": [	         
	             {"mark": "Defender.mark", "out": "index.html"},	             
	             {"mark": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
	             {"mark": "Hardware.mark", "out": "Hardware.html", "nav": "Hardware"},	             
	             {"mark": "Bank1.mark", "out": "Bank1.html", "nav":"Bank 1"},
	             {"mark": "Bank2.mark", "out": "Bank2.html", "nav":"Bank 2"},
	             {"mark": "Bank3.mark", "out": "Bank3.html", "nav":"Bank 3"},
	             {"mark": "Bank7.mark", "out": "Bank7.html", "nav":"Bank 7"},
	             {"mark": "BankFixed.mark", "out": "BankFixed.html", "nav":"Fixed Bank"},	             
	             {"separator": ""},	             
	             {"mark": "SoundRAMUse.mark", "out": "SoundRAMUse.html", "nav": "Sound RAM Use"},
	             {"mark": "SoundHardware.mark", "out": "SoundHardware.html", "nav": "Sound Hardware"},
	             {"mark": "SoundCode.mark", "out": "SoundCode.html", "nav":"Sound Code"},
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
	             {"mark": "SoundRAMUse.mark", "out": "SoundRAMUse.html", "nav": "Sound RAM Use"},
	             {"mark": "SoundHardware.mark", "out": "SoundHardware.html", "nav": "Sound Hardware"},	             
	             {"mark": "SoundCode.mark", "out": "SoundCode.html", "nav": "Sound Code"},
	             {"copy": "Frogger.jpg"},	             
	             {"copy": "FroggerFix.mp3"},
	             {"copy": "Frogger.js"},
	             {"mark": "Code.mark", "out":"Main.html","nav":"Main Board"},
	             {"mark": "GFX.mark", "out":"GFX.html","nav":"GFX"},
	             {"mark": "Hardware.mark", "out":"Hardware.html","nav":"Hardware"},
	             {"mark": "RAMUse.mark", "out":"RAMUse.html","nav":"RAM Use"}
	             ]
	         },
	         {"dir": "Galaga", "nav": "Galaga", "entries": [
                 {"mark": "Galaga.mark", "out": "index.html"},
                 {"mark": "CPU1.mark", "out":"CPU1.html","nav":"CPU1"},
                 {"mark": "CPU2.mark", "out":"CPU2.html","nav":"CPU2"},
                 {"mark": "CPU3.mark", "out":"CPU3.html","nav":"CPU3"},
                 {"copy": "Galaga.jpg"},
                 {"copy": "galaga1.jpg"},
                 {"copy": "galaga2.jpg"}
	             ]
	         },
	         {"dir": "MoonPatrol", "nav": "Moon Patrol", "entries": [
                 {"copy": "MoonPatrol.jpg"},
                 {"copy": "MoonPatrol.js"},
	             {"mark": "MoonPatrol.mark", "out": "index.html"},
	             {"mark": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
	             {"mark": "Hardware.mark", "out": "Hardware.html", "nav": "Hardware"},
	             {"mark": "Code.mark", "out": "Code.html", "nav": "Code"},
	             {"separator": ""},
	             {"mark": "MoonPatrolSound.mark", "out": "MoonPatrolSound.html", "nav":"Moon Patrol Sound"},
	             {"mark": "SoundRAMUse.mark", "out": "SoundRAMUse.html", "nav": "Sound RAM Use"},
	             {"mark": "SoundHardware.mark", "out": "SoundHardware.html", "nav": "Sound Hardware"},
	             {"mark": "SoundCode.mark", "out": "SoundCode.html", "nav": "Sound Code"},
	             {"separator": ""},
	             {"mark": "GFX1.mark", "out": "GFX1.html", "nav": "GFX1"},
	             {"mark": "GFX2.mark", "out": "GFX2.html", "nav": "GFX2"},
	             {"mark": "GFX3.mark", "out": "GFX3.html", "nav": "GFX3"},
	             {"mark": "GFX4.mark", "out": "GFX4.html", "nav": "GFX4"},
	             {"mark": "GFX5.mark", "out": "GFX5.html", "nav": "GFX5"},	             
	             {"mark": "ImageBackgroundColors.mark", "out": "ImageBackgroundColors.html", "nav": "Background Colors"},
	             {"mark": "SpriteColors.mark", "out": "SpriteColors.html", "nav": "Sprite Colors"},
	             {"mark": "SpriteColorSets.mark", "out": "SpriteColorSets.html", "nav": "Sprite Color Sets"},
	             {"mark": "TextColors.mark", "out": "TextColors.html", "nav": "Text Colors"}
	             ]
	         },
	         {"dir": "OmegaRace", "nav": "Omega Race", "entries": [
	             {"mark": "OmegaRace.mark", "out":"index.html"},
                 {"mark": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
                 {"mark": "Hardware.mark", "out": "Hardware.html", "nav": "Hardware"},
                 {"mark": "MainBoard.mark", "out":"MainBoard.html", "nav": "Main Board"},     
                 {"separator": ""},
                 {"mark": "VectorROM.mark", "out":"VectorROM.html", "nav": "Vector ROM"},
                 {"mark": "DVGPROM.mark", "out": "DVGPROM.html", "nav": "DVG PROM"},
                 {"separator": ""},
                 {"mark": "SoundHardware.mark", "out": "SoundHardware.html", "nav": "Sound Hardware"},
                 {"mark": "SoundRAMUse.mark", "out": "SoundRAMUse.html", "nav": "Sound RAM Use"},
	             {"mark": "SoundBoard.mark", "out":"SoundBoard.html", "nav": "Sound Code"}, 	                         
	             {"copy": "ORace.jpg"},
	             {"copy": "VectorROM.js"}
	             ]
	         },	              
	         {"dir": "SpaceInvaders", "nav": "Space Invaders", "entries": [
	             {"mark": "SpaceInvaders.mark", "out": "index.html"},
	             {"mark": "RAMUse.mark",        "nav":"RAM Usage", "out": "RAMUse.html"},
	             {"mark": "Hardware.mark",      "nav":"Hardware", "out": "Hardware.html"},
	             {"mark": "Code.mark",          "nav":"Code", "out": "Code.html"},	             
	             {"copy": "SpaceInvaders.jpg"}	             	             
	             {"copy": "SpaceInvaders.js"}
	             
	             ]
	         },
	         {"dir": "TimePilot", "nav": "Time Pilot", "entries": [
	             {"copy": "TimePilot.jpg"},
	             {"mark": "TimePilot.mark", "out": "index.html"},
	             {"mark": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
	             {"mark": "Hardware.mark", "out": "Hardware.html", "nav": "Hardware Info"},
	             {"mark": "SoundCode.mark", "out": "SoundCode.html", "nav": "Sound Code"}
	             ]
	         }
	         	         
	         ]
	     },
	     
	     {"dir": "Atari2600", "nav": "Atari 2600", "entries": [
	         {"mark": "Atari2600.mark", "out": "index.html"},
	         {"copy": "Atari2600.jpg"},
	         {"copy": "Hardware.jpg"},
	         {"mark": "Stella.mark", "out": "Stella.html", "nav": "Stella"},
	         
	         {"dir": "Asteroids", "nav": "Asteroids", "entries": [
	             {"copy": "A2600Asteroids.jpg"},
	             {"mark": "Asteroids.mark", "out": "index.html"},
	             {"mark": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
	             {"mark": "Code.mark", "out": "Code.html", "nav": "Code"}
	             ]
	         },	         
	         {"dir": "BattleZone", "nav": "BattleZone", "entries": [
	             {"copy": "A2600Battlezone.jpg"},
	             {"mark": "BattleZone.mark", "out": "index.html"},
	             {"mark": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
	             {"mark": "Code.mark", "out": "Code.html", "nav": "Code"}
	             ]
	         },
	         {"dir": "Chess", "nav": "Chess", "entries": [
	             {"copy": "A2600Chess.jpg"},
	             {"mark": "Chess.mark", "out": "index.html"},
	             {"mark": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
	             {"mark": "Code.mark", "out": "Code.html", "nav": "Code"}
	             ]
	         },	         
	         {"dir": "Combat", "nav": "Combat", "entries": [
	             {"copy": "A2600Combat.jpg"},
	             {"mark": "Combat.mark", "out": "index.html"},
	             {"mark": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
	             {"mark": "Code.mark", "out": "Code.html", "nav": "Code"}
	             ]
	         },
	         {"dir": "ET", "nav": "ET", "entries": [
	             {"copy": "A2600ET.jpg"},
	             {"mark": "ET.mark", "out": "index.html"},
	             {"mark": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
	             {"mark": "Code.mark", "out": "Code.html", "nav": "Code"}
	             ]
	         },	         
	         {"dir": "MissileCommand", "nav": "Missile Command", "entries": [
	             {"copy": "A2600MissileCommand.jpg"},
	             {"mark": "MissileCommand.mark", "out": "index.html"},
	             {"mark": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
	             {"mark": "Code.mark", "out": "Code.html", "nav": "Code"}
	             ]
	         },
	         {"dir": "DoubleGap", "nav": "Double Gap", "entries": [
	             {"copy": "DoubleGap.jpg"},
	             {"mark": "DoubleGap.mark", "out": "index.html"},
	             {"mark": "Code.mark", "out": "Code.html", "nav": "Code"}
	             ]
	         },
	         	         
	         ]
	     },
	     
	     {"dir": "CoCo", "nav": "CoCo", "entries": [
             {"mark": "CoCo.mark", "out": "index.html"},
             {"mark": "Hardware.mark", "out": "Hardware.html", "nav":"Hardware"},
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
                 {"mark": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
                 {"mark": "Code.mark", "out": "Code.html", "nav": "Code"},
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
                 {"mark": "RAMUse.mark", "out": "RAMUse.html", "nav":"RAM Use"},
                 {"mark": "Code.mark", "out": "Code.html", "nav": "Code"},
                 {"copy": "Pyramid.jpg"},
                 {"copy": "pyramid.js"},
                 {"copy": "DEFAULT.js"},
                 {"copy": "GAME.js"},
                 {"copy": "MAIN.js"},
                 {"copy": "OBJS.js"},
                 {"copy": "PARSE.js"},
                 {"copy": "ROOMS.js"},
                 {"copy": "SCRIPTER.js"},
                 {"copy": "BinaryDataPyramid.js"}
                 ]
             }, 
             {"dir": "RaakaTu", "nav": "Raaka Tu", "entries" : [
			     {"mark": "RaakaTu.mark", "out": "index.html"},
				 {"mark": "RAMUse.mark", "out": "RAMUse.html", "nav":"RAM Use"},
				 {"mark": "Code.mark", "out": "Code.html", "nav": "Code"},
				 {"copy": "RaakaTu.jpg"},
				 {"copy": "raakatu.js"},
				 {"copy": "BinaryDataRaakaTu.js"}
                 ]
             },
             {"dir": "Bedlam", "nav": "Bedlam", "entries" : [
                 {"mark": "Bedlam.mark", "out": "index.html"},
                 {"mark": "RAMUse.mark", "out": "RAMUse.html", "nav":"RAM Use"},
                 {"mark": "Code.mark", "out": "Code.html", "nav": "Code"},
                 {"copy": "Bedlam.jpg"},
                 {"copy": "bedlam.js"},
                 {"copy": "BinaryDataBedlam.js"}
                 ]
             },
             {"dir": "Daggorath", "nav": "Daggorath", "entries" : [
				 {"mark": "Daggorath.mark", "out": "index.html"},
				 {"mark": "Levels.mark", "out": "levels.html", "nav":"Level Maps"},
				 {"mark": "RAMUse.mark", "out": "RAMUse.html", "nav":"RAM Use"},
				 {"mark": "Code.mark", "out": "Code.html", "nav": "Code"},
				 {"copy": "Daggorath.jpg"},
                 {"copy": "daggorath.js"}
                 ]
             }
             
	    	 ]	    	 
	     },
	     
	     {"dir": "Gameboy", "nav": "Gameboy", "entries": [
  	         {"mark": "Gameboy.mark", "out": "index.html"},
  	         {"copy": "Gameboy.jpg"},
  	                                              	         
  	         {"dir": "Zelda", "nav": "Zelda", "entries": [
  	             {"copy": "GBZelda.jpg"},
  	             {"copy": "zeldaGB.js"},
  	             {"mark": "GBZelda.mark", "out": "index.html"},
  	             {"mark": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
  	             {"mark": "Hardware.mark", "out": "Hardware.html", "nav": "Hardware Info"},
  	             {"mark": "Bank00.mark", "out": "Bank00.html", "nav": "Bank00"},
  	             {"mark": "Bank01.mark", "out": "Bank01.html", "nav": "Bank01"},
  	             {"mark": "Bank02.mark", "out": "Bank02.html", "nav": "Bank02"},
  	             {"mark": "Bank03.mark", "out": "Bank03.html", "nav": "Bank03"},
  	             {"mark": "Bank04.mark", "out": "Bank04.html", "nav": "Bank04"},
  	             {"mark": "Bank05.mark", "out": "Bank05.html", "nav": "Bank05"},
  	             {"mark": "Bank06.mark", "out": "Bank06.html", "nav": "Bank06"},
  	             {"mark": "Bank07.mark", "out": "Bank07.html", "nav": "Bank07"},
  	             {"mark": "Bank08.mark", "out": "Bank08.html", "nav": "Bank08"},
  	             {"mark": "Bank09.mark", "out": "Bank09.html", "nav": "Bank09"},
  	             {"mark": "Bank0A.mark", "out": "Bank0A.html", "nav": "Bank0A"},
  	             {"mark": "Bank0B.mark", "out": "Bank0B.html", "nav": "Bank0B"},
  	             {"mark": "Bank0C.mark", "out": "Bank0C.html", "nav": "Bank0C"},
  	             {"mark": "Bank0D.mark", "out": "Bank0D.html", "nav": "Bank0D"},
  	             {"mark": "Bank0E.mark", "out": "Bank0E.html", "nav": "Bank0E"},
  	             {"mark": "Bank0F.mark", "out": "Bank0F.html", "nav": "Bank0F"}, 	 
  	             {"mark": "Bank10.mark", "out": "Bank10.html", "nav": "Bank10"},
  	             {"mark": "Bank11.mark", "out": "Bank11.html", "nav": "Bank11"},
  	             {"mark": "Bank12.mark", "out": "Bank12.html", "nav": "Bank12"},
  	             {"mark": "Bank13.mark", "out": "Bank13.html", "nav": "Bank13"},
  	             {"mark": "Bank14.mark", "out": "Bank14.html", "nav": "Bank14"},
	             {"mark": "Bank15.mark", "out": "Bank15.html", "nav": "Bank15"},
	             {"mark": "Bank16.mark", "out": "Bank16.html", "nav": "Bank16"},
	             {"mark": "Bank17.mark", "out": "Bank17.html", "nav": "Bank17"},
	             {"mark": "Bank18.mark", "out": "Bank18.html", "nav": "Bank18"},
	             {"mark": "Bank19.mark", "out": "Bank19.html", "nav": "Bank19"}, 	 
	             {"mark": "Bank1A.mark", "out": "Bank1A.html", "nav": "Bank1A"},
	             {"mark": "Bank1B.mark", "out": "Bank1B.html", "nav": "Bank1B"},
	             {"mark": "Bank1C.mark", "out": "Bank1C.html", "nav": "Bank1C"},
	             {"mark": "Bank1D.mark", "out": "Bank1D.html", "nav": "Bank1D"},
	             {"mark": "Bank1E.mark", "out": "Bank1E.html", "nav": "Bank1E"},
	             {"mark": "Bank1F.mark", "out": "Bank1F.html", "nav": "Bank1F"}  	             
  	             ]
  	         }
  	         ]
  	     },
  	     
  	     {"dir": "NES", "nav": "Nintendo NES", "entries": [
	         {"mark": "NES.mark", "out": "index.html"},
	         {"copy": "NES.jpg"},
	                                              	         
	         {"dir": "Zelda", "nav": "Zelda", "entries": [
	             {"copy": "Zelda.jpg"},
	             {"copy": "zelda.js"},
	             {"copy": "ZeldaBanks.jpg"},
	             {"mark": "Zelda.mark", "out": "index.html"},
	             {"mark": "RAMUse.mark", "out": "RAMUse.html", "nav": "RAM Use"},
	             {"mark": "Hardware.mark", "out": "Hardware.html", "nav": "Hardware Info"},
	             {"mark": "Bank0.mark", "out": "Bank0.html", "nav": "Bank0"},
	             {"mark": "Bank1.mark", "out": "Bank1.html", "nav": "Bank1"},
	             {"mark": "Bank2.mark", "out": "Bank2.html", "nav": "Bank2"},
	             {"mark": "Bank3.mark", "out": "Bank3.html", "nav": "Bank3"},
	             {"mark": "Bank4.mark", "out": "Bank4.html", "nav": "Bank4"},
	             {"mark": "Bank5.mark", "out": "Bank5.html", "nav": "Bank5"},
	             {"mark": "Bank6.mark", "out": "Bank6.html", "nav": "Bank6"},
	             {"mark": "Bank7.mark", "out": "Bank7.html", "nav": "Bank7"}
	             ]
	         }
	         ]
	     },
	     
	     {"dir": "TRS80", "nav": "TRS80", "entries": [
             {"mark": "TRS80.mark", "out": "index.html"},
             {"mark": "Hardware.mark", "out": "Hardware.html", "nav":"Hardware"},            
             {"copy": "TRS80.jpg"},
             {"copy": "TRS80Tech.jpg"},      
             {"copy": "TRS80Text.js"},
             {"dir": "HauntedHouse", "nav": "HauntedHouse", "entries": [
           	  {"mark": "HauntedHouse.mark", "out": "index.html"},
             	  {"mark": "Code1.mark", "out": "Code1.html", "nav": "Code1"},
                 {"mark": "RAMUse1.mark", "out": "RAMUse1.html", "nav":"RAM Use (1st)"},
                 {"mark": "Code2.mark", "out": "Code2.html", "nav": "Code2"},
                 {"mark": "RAMUse2.mark", "out": "RAMUse2.html", "nav":"RAM Use (2nd)"}, 
                 {"copy": "HauntedHouse.jpg"},
                 {"copy": "hauntedhouse.js"},
                 {"copy": "BinaryDataHauntedHouse.js"}
                 ]
             },
             {"dir": "Pyramid", "nav": "Pyramid", "entries": [
           	  {"mark": "TRS80Pyramid.mark", "out": "index.html"},
           	  {"mark": "RAMUse.mark", "out": "RAMUse.html", "nav":"RAM Use"},
                 {"mark": "Code.mark", "out": "Code.html", "nav": "Code"},
                 {"copy": "TRS80Pyramid.jpg"},
                 {"copy": "trs80pyramid.js"},
                 {"copy": "BinaryDataTRS80Pyramid.js"}
           	  ]
             },
             {"dir": "Xenos", "nav": "Xenos", "entries": [
           	  {"mark": "Xenos.mark", "out": "index.html"},
           	  {"mark": "RAMUse.mark", "out": "RAMUse.html", "nav":"RAM Use"},
                 {"mark": "Code.mark", "out": "Code.html", "nav": "Code"},
                 {"copy": "Xenos.png"}               
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
