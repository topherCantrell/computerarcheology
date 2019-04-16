function startMadness(consoleElement,tapeElement) {
	
	var binData = makeBinaryDataPyramid();
	var CPU6809 = make6809();
	
	var my = {};
	
	my.resetVector = 0xCE3;
	
	function write(addr,value) {
		throw "Write to "+addr+" from "+CPU6809.status()['pc'];
	}
	
	function read(addr) {
		
		// 6809 reset vector (point to game code at 0600)
        if(addr===0xFFFE) return my.resetVector>>8;
        if(addr===0xFFFF) return my.resetVector&0xFF;
        
        if(addr>=0x300 && addr<=0x3EB7) {
        	return binData.read(addr);
        }
        
		throw "Read from "+addr;
	}
	
	CPU6809.init(write,read,function(){});
	
	CPU6809.steps(100);
			
	// The user input loop is at 0864. It calls A1B1 to blink the cursor
	// and wait for a key. This is where the JS should hook. The game
	// interrupts still happen once a second.
	
	// Execution begins at 0CE3
	
	// The CoCo emulator
	//var CoCoText = makeCoCoText(consoleElement,tapeElement);
	// The game code
	//var BinaryData = makeBinaryDataMadness();
	
	/*
    function write(addr,value) {        
    	if(addr>=0x0600 && addr<0x3F21) {
    		// RAM where the game is loaded
        	BinaryData.write(addr,value);
        	return true;
        }    	
    }
    
    function read(addr) {   
    	
    	// The game uses the input-loop to increment 1EB as a
    	// random number. Since we aren't allowing the
    	// input loop to spin, we'll return a random number here.
    	if(addr===0x01EB) {
    		return Math.floor(Math.random()*256);
    	}
    	
    	// Virtual tape area
    	if(addr===0x3C27) {
    	    $("#cocoTapeArea").show();
    	}
    	    	    	
    	if(addr===0x0F1B) {
    		// This is the game's endless-loop after death and such
    		CoCoText.startEndlessLoop();    		
    	}
    	
        if(addr>=0x0600 && addr<0x3F21) {
        	// RAM where the game is loaded
            return BinaryData.read(addr); 
        }        
        
        return undefined;
        
    }
    */
      
	/*
    BinaryData.loadDataCacheFromURL("Code.html",function() { 
    	CoCoText.init(read,write,function() {CoCoText.runUntilWaitKey();}, 0x0600);
    	CoCoText.runUntilWaitKey();    	  
    });
    */    
    
};