
var SCRIPTER = function () {

	var my = {};
	
	var scriptAbort; // used to abort a script from a subscript
	
	var inputNoun = null;
	
	var debugMes = function (mes) {
		//println("@@"+mes+"@@");
	};

	SCRIPTCOMMANDS = {
	
		MoveToRoomX : function(room) {	
		
			debugMes("MoveToRoomX("+room+")");
			
			// If there is light in the old room or new room then you have
        	// enough light to move without stepping.
        	var lightNearby = false;
        	if (GAME.lastRoom && ROOMS.isRoomLit(GAME.lastRoom)) {
            	lightNearby = true;
        	}
        	if (ROOMS.isRoomLit(room)) {
            	lightNearby = true;
        	}
                
        	// No light ... 60% chance you die
        	if (!lightNearby) {
            	var rand = getRandomByte();
            	if (rand >= 103) {
                	println("YOU FELL INTO A PIT AND BROKE EVERY BONE IN YOUR BODY.");
                	SCRIPTCOMMANDS.PrintScore();
                	GAME.gameOver = true;
                	return;
            	}            
        	}        
    
        	// Make the move
        	GAME.lastRoom = GAME.currentRoom;
        	GAME.currentRoom = room;
        	SCRIPTER.look();
        
        	// If you move with more than two treasures then the Mummy moves all treasures 
        	// to the chest in the maze (if it is in the maze). Their location becomes
        	// "chest", and the chest description shows them.        
        	var chest = OBJS.getExactObjectByName("#CHEST");
        	if (chest.location === "") {
            	// Find the treasures in the pack
            	var p = OBJS.getObjectsAtLocation("pack");
            	var pts = [];
            	for (var x = 0;x < p.length; ++x) {            	
                	if (p[x].treasure) {
                    	pts.push(p[x]);
                	}
            	}
            	// If there are more than two then move them
            	if (pts.length > 1) {
                	for (var y = 0; y < pts.length; ++y) {
                    	pts[y].location = "room_53";
                	}
                	println("SUDDENLY, A MUMMY CREEPS UP BEHIND YOU!! \"I'M THE KEEPER OF THE TOMB\", HE WAILS, \"I TAKE THESE TREASURES AND PUT THEM IN THE CHEST DEEP IN THE MAZE!\" HE GRABS YOUR TREASURE AND VANISHES INTO THE GLOOM.");
                	chest.location = "room_53";
            	}            	
        	}        
        
        	return true;   
		},
		
		AssertObjectXIsInPack : function(obj) {
			debugMes("AssertObjectXIsInPack("+obj+")");
			var o = OBJS.getTopObjectByName(obj);
			if(o.location === 'pack') {
				return true;
			}
			return false;
		},
		
		AssertObjectXIsInCurrentRoom : function(obj) {
			debugMes("AssertObjectXIsInCurrentRoom("+obj+")");
			var o = OBJS.getTopObjectByName(obj);
			if(o.location === GAME.currentRoom) {
				return true;
			}
			return false;
		},
		
		AssertObjectXIsInCurrentRoomOrPack : function(obj) {
			debugMes("AssertObjectXIsInRoomOrPack("+obj+")");
			var o = OBJS.getTopObjectByName(obj);
			if(o.location === 'pack' || o.location === GAME.currentRoom) {
				return true;
			}
			return false;
		},
		
		PrintMessageX : function(message) {
			debugMes("PrintMessageX()");
			println(message);
			return true;
		},
		
		PrintRoomDescription : function() {
			debugMes("PrintRoomDescription()");
			look();
			return true;
		},
		
		MoveObjectXToRoomY : function(x,y) {
			debugMes("MoveObjectXToRoomY("+x+","+y+")");
			var objX = OBJS.getExactObjectByName(x);
			objX.location = y;
			return true;
		},
		
		Quit : function () {
			debugMes("Quit()");
			SCRIPTCOMMANDS.PrintScore();
			GAME.gameOver = true;
            return;
		},
		
		PlayerDied : function () {
			debugMes("PlayerDied()");
			SCRIPTCOMMANDS.PrintScore();
			GAME.gameOver = true;
            return;
		},
		
		MoveObjectXToIntoContainerY : function (x,y) {
			debugMes("MoveObjectXToRoomY("+x+","+y+")");
			var objX = OBJS.getExactObjectByName(x);
			objX.location = y;
			return true;
		},
		
		MoveObjectXToCurrentRoom : function (x) {
			debugMes("MoveObjectXToCurrentRoom("+x+")");
			var objX = OBJS.getExactObjectByName(x);
			objX.location = GAME.currentRoom;
			println("OK");
			return true;
		},
		
		PrintScore : function () {
			debugMes("PrintScore()");
			var score = 0;
	        var obs = OBJS.getAllObjects();
	        for(var x=0;x<obs.length;++x) {
	        	var ob = obs[x];
	        	if (ob.treasure) {
	        		// Could be in chest. Where is the chest?
	        	    ob = OBJS.getTopObjectByName(ob.name);            	
	                if (ob.location === "room_2") {
	                    score = score + 20;
	                } else if (ob.location === "pack") {
	                    score = score + 5;
	                }
	            }    
	        }           
			println("YOU HAVE SCORED " + score + " OUT OF 220.");
	        println("USING " + GAME.turnCount + " TURNS.");
	        return true;
		},
		
		AssertObjectXMatchesUserInput : function(obj) {
			debugMes("AssertObjectXMatchesUserInput("+obj+") ["+inputNoun.name+"]");
			if(obj === inputNoun.name) {
				return true;
			}
			return false;
		},
		
		GetUserInputObject : function() {	
			debugMes("GetUserInputObject() ["+inputNoun.name+"]");
			if(!inputNoun.packable) {
				println("DON'T BE REDICULOUS!")
				return true;
			}
			if(OBJS.getTopObjectByName(inputNoun.name).location === "pack") {
				println("YOU ARE ALREADY CARRYING IT.");
				return true;
			}			
			var objs = OBJS.getObjectsAtLocation("pack");
			if (objs.length > 7) {
				println("YOU CAN'T CARRY ANYTHING MORE. YOU'LL HAVE TO DROP SOMETHING FIRST.");
				return true;
			}			
			OBJS.getTopObjectByName(inputNoun.name).location = "pack";
			println("OK");			
			return true;
		},
		
		GetObjectXFromRoom : function (x) {
			debugMes("GetObjectXFromRoom("+x+")");
			var objs = OBJS.getObjectsAtLocation("pack");
			if(!inputNoun.packable) {
				println("DON'T BE REDICULOUS!")
				return true;
			}
			if (objs.length > 7) {
				println("YOU CAN'T CARRY ANYTHING MORE. YOU'LL HAVE TO DROP SOMETHING FIRST.");
				return true;
			}	
			var objX = OBJS.getExactObjectByName(x);
			objX.location = "pack";
			println("OK");
			return true;
		},
		
		PrintInventory : function() {
			debugMes("PrintInventory()");
			var objs = OBJS.getObjectsAtLocation("pack");
			if (objs.length===0) {
				println("YOU'RE NOT CARRYING ANYTHING.");
			} else {
				for (var x=0;x<objs.length;++x) {
					println(objs[x].short);
				}
			}
			return true;
		},
		
		DropUserInputObject : function() {
			debugMes("DropUserInputObject() ["+inputNoun.name+"]");
			OBJS.getTopObjectByName(inputNoun.name).location = GAME.currentRoom;
			println("OK");
			return true;
		},
		
		DropObjectX : function (x) {
			debugMes("DropObjectX("+x+")");
			var objX = OBJS.getExactObjectByName(x);
			objX.location = GAME.currentRoom;
			println("OK");
			return true;
		},
				
		PrintOK : function() {
			debugMes("PrintOK()");
			println("OK");
			return true; 
		},
		
		JumpToTopOfGameLoop : function() {		
			debugMes("JumpToTopOfGameLoop()");
			return true; 
		},
				
		AssertRandomIsGreaterThanX : function (num) {
			debugMes("AssertRandomIsGreaterThanX("+num+")");
			var val = getRandomByte();
			if(num<=val) {
				println("YOU HAVE CRAWLED AROUND IN SOME LITTLE HOLES AND WOUND UP BACK IN THE MAIN PASSAGE.");
				SCRIPTCOMMANDS.look();				
				return true;
			} 			
			return false;
		},
		
		MoveToRoomXIfItWasLastRoom : function (room) {
			// Never used in game
			debugMes("MoveToRoomXIfItWasLastRoom("+room+")");
			if(room === GAME.lastRoom) {
				return SCRIPTCOMMANDS.MoveToRoomX(room);
			} else {
				return false;
			}						
		},
		
		MoveToLastRoom : function () {
			debugMes("MoveToLastRoom()");
			if(!GAME.lastRoom) {
				println("SORRY, BUT I NO LONGER SEEM TO REMEMBER HOW IT WAS YOU GOT HERE.");
				return true;
			}
			return SCRIPTCOMMANDS.MoveToRoomX(GAME.lastRoom);
		},
		
		AssertPackIsEmptyExceptForEmerald : function() {
			debugMes("AssertPackIsEmptyExceptForEmerald()");
			var objs = OBJS.getObjectsAtLocation("pack");			
			if(objs.length===0) return true;
			if(objs.length>1) return false;
			if(objs[0].name !== "#EMERALD") return false;
			return true;			
		},	
		
		SaveGame : function () {
			var state = "";
			var objs = OBJS.getAllObjects();
			for (var x=0;x<objs.length;++x) {
				var lo = objs[x].location;
				if(lo.indexOf("room_")==0) {
					lo = lo.substring(4);
				}
				state = state + lo+",";
			}
			
			state = "LOAD "+state + GAME.currentRoom+","+GAME.lastRoom+","+GAME.turnCount+","+GAME.gameOver+","+GAME.batteryLife;
						
			println("Please copy the following long line to a text file to save your game. Then paste in the line to reload.");
			println("");
			println(state);
			println("");
			
			return true;			
		},
		
		LoadGame : function () {
			var state = PARSE.loadState.split(",");
			var objs = OBJS.getAllObjects();
			var x = 0;
			for (;x<objs.length;++x) {
				var lo = state[x];
				if (lo[0]==='_') lo = "room"+lo;
				objs[x].location = lo;				
			}
			
			GAME.currentRoom = state[x++];
			if(state[x]==='null') {
				GAME.lastRoom = null;
				++x;
			} else {
				GAME.lastRoom = parseInt(state[x++]);
			}
			GAME.turnCount = parseInt(state[x++]);
			if(state[x++]==='true') {
				GAME.gameOver = true;
			} else {
				GAME.gameOver = false;
			}
			GAME.batteryLife = parseInt(state[x++]);
			
			return true;
		},
				
		SubScriptXAbortIfPass : function(script) {
			debugMes("SubScriptXAbortIfPass...");
			var ret = parseScriptRec(script);
			if(!ret) {
				return true;
			}
			abortScript = true;
			return true;
		}
		
	};	
			
    /**
     * This function prints the current room description and all objects in it ... if there is light.
     */
    var look = function () {  
    
    	getRandomByte(); // Some entropy into the random number
        
        var room = ROOMS.getRoom(GAME.currentRoom);
        
        if (ROOMS.isRoomLit(GAME.currentRoom)) {        
            println(room.desc);
            var objsInRoom = OBJS.getObjectsAtLocation(GAME.currentRoom);
            for (var x  = 0;x < objsInRoom.length;++x) {
            	if(objsInRoom[x].long) println(objsInRoom[x].long);          
            }
        } else {
            println("IT IS NOW PITCH DARK. IF YOU PROCEED, YOU WILL LIKELY FALL INTO A PIT.");
        }
        
    };
	
	/**
	 * This is the toplevel entry for running a script.
	 * @param script the script to run
	 * @param noun the input noun (if any)
	 * @return true if the script completed or false if it failed
	 */
	var parseScript = function(script,noun) {
		inputNoun = noun;
		abortScript = false;
		return parseScriptRec(script);
	}
		
	/**
	 * This is the recursive entry for processing subscripts.
	 * @param script the script to run
	 * @param return true if the script completed or false if it failed
	 */
	var parseScriptRec = function(script) {	
		var ptr = 0;
		while(ptr<script.length) {
			if(abortScript) {
				return true; // Scripts only abort on subscript "pass"
			}
			var com = script[ptr++];
			var x = null;
			var y = null;
			if(com.indexOf('X')>=0) {
				x = script[ptr++];
			}
			if(com.indexOf('Y')>=0) {
				y = script[ptr++];
			}
			//println("**"+com+"("+x+","+y+")");
			var fn = SCRIPTCOMMANDS[com];
			if(fn) {
				var rs = fn(x,y);
				if(!rs) return rs;
			} else {
				println("** UNIMPLEMENTED SCRIPT COMMAND '"+com+"'");
				abortScript = true;
				return true;
			}
		}	
		return true;
	};
	
	// Random number taken from Dungeons of Daggorath disassembly
    var randomSeed = 0x00FACEDE; // hard-coded seed value
    var getRandomByte = function () {
    	for (var x=0;x<8;++x) {    		
    		var a = (randomSeed>>16) & 255;
    		a = a & 0xE1;
    		var b = 0;
    		for (var y=0;y<8;++y) {
    			a = a << 1;
    			if (a>255) {
    				b = b + 1;
    				a = a & 255;
    			}
    		}
    		randomSeed = randomSeed << 1;
    		randomSeed = randomSeed & 0x00FFFFFF;
    		randomSeed = randomSeed | (b&1);
    	}
    	return randomSeed&255;
    };
	
	// public API	
	my.parseScript = parseScript;
	my.look = look;
	
	return my;

}();