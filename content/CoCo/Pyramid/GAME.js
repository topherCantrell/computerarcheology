/*global OBJS, ROOMS, DEFAULT, PARSE, SCRIPTER, println, printChars, valueOrFunction */

var GAME = function () {

    var my =  {    
        currentRoom : "room_1",  // Player's current room
        lastRoom : null,         // Player's last room
        turnCount : 0,           // Number of turns taken
        gameOver: false,         // Is the game over? (no input or output if so)     
        batteryLife: 310         // Life of the batteries
    };
    
    /**
     * Software errors come here.
     * @er the error details
     */
    var facePalm = function (er) {
        println("*** " + er + " ***");
    }; 
    
    /**
     * This function attempts to change the batteries in the lamp. If the fresh batteries are in the
     * pack then the lamp time is reset and the fresh batteries are swapped for the dead ones.
     * Note the lamp doesn't have to be in the pack.
     * @return true if the batteries were changed
     */
    var tryChangeBatteries = function () {
    	var batt = OBJS.getExactObjectByName("#BATTERIES_fresh");
    	if(batt.location === "pack") {
    		println("YOUR LAMP IS GETTING DIM. I'M TAKING THE LIBERTY OF REPLACING THE BATTERIES.");
    		my.batteryLife = 310;
    		batt.location = null;
    		batt = OBJS.getExactObjectByName("#BATTERIES_worn");
    		batt.location = "pack";
    		return true;
    	}
    	return false;    
    };
    
    /**
     * This function is called after every player turn just before the next input wait.
     */
    var do_afterPlayerTurn = function () {   
    
    	++my.turnCount;
    
    	var lamp = OBJS.getExactObjectByName("#LAMP_on");
    	if(lamp.location) {
    		--GAME.batteryLife;
    		if(GAME.batteryLife === 0) {
    			// Batteries ran out ... try and change them or power off
            	if (!tryChangeBatteries()) {                	
                	var lampDead = OBJS.getExactObjectByName("#LAMP_dead");
                	lampDead.location = lamp.location;
                	lamp.location = null;
                	println("YOUR LAMP HAS RUN OUT OF POWER.");
                }
    		} else if (GAME.batteryLife === 20) {
            	// Twenty turns left ... warn the player
                println("YOUR LAMP IS GETTING DIM. YOU'D BEST START WRAPPING THIS UP, UNLESS YOU CAN FIND SOME FRESH BATTERIES. I SEEM TO RECALL THERE IS A VENDING MACHINE IN THE MAZE. BRING SOME COINS WITH YOU.");
            }            
    	}    
    	if (GAME.batteryLife <= 10) {
        	// Less than 10 turns of light left ... try to change batteries
            tryChangeBatteries();
        }
                   
    };   

    /**
     * This function processes the player's input.
     * @param chunk the input line
     */
    var input = function (ck) {
        if (ck) {
        
            var chs = ck.split(";");
            if(chs.length==0) chs.push("");
            
            for(var x=0;x<chs.length;++x) {
            	var chunk = chs[x];
            	if(chs.length>1) {
            		println(": "+chunk);
            	}
        
	            var dec = PARSE.parseInput(chunk);
	            if(!dec) {
	            	printChars(": ");
	            	return; // General input error ... just repeat input
	            }
	                        
	            var passed = false; // Nobody handled the command yet
	            
	            // Let the room handle it if it has a handler
	            var room = ROOMS.getRoom(my.currentRoom);
	            var script = room.commands[dec.verb];                       
	            if(script) {
	            	passed = SCRIPTER.parseScript(script,dec.noun);
	            }
	            
	            // If the room didn't handle it try the default script
	            if(!passed) {
	            	script = DEFAULT.getDefaultScript(dec.verb);
	            	if (script) {            	
	            		passed = SCRIPTER.parseScript(script,dec.noun);
	            	}
	            }
	            
	            // Nobody handled it. Just error out.
	            if(!passed) {
	            	println("I DON'T KNOW HOW TO APPLY THAT WORD HERE.");
	            }
	           
	            // After every turn
	        	do_afterPlayerTurn();  
        	} 
        	
        	printChars(": "); 
        }        
    };

    /**
     * This function initializes the game for play.
     */
    var init = function () {
        println("WELCOME TO PYRAMID!!");
        println("");
        SCRIPTER.look();
        printChars(": ");        
    };
            
    // Public API    
    my.facePalm = facePalm;
    my.input = input;
    my.init = init;      
    
    return my;
        
}();
