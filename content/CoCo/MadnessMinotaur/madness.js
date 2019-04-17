function startMadness(consoleElement,tapeElement) {
	
	var binData = makeBinaryDataPyramid();
	var CPU6809 = make6809();
	var ram = Array(0x300);
	ram.fill(0);
	var ram2 = Array(0x4000-0x3EB8);
	ram2.fill(0);
		
	var my = {};
	
	my.resetVector = 0xCE3;
			
	function write(addr,value) {
		
		if(addr<0x300) {
        	ram[addr] = value;
        } else if(addr>=0x300 && addr<=0x3EB7) {
        	binData.write(addr,value);
        } else if(addr>=0x3EB8 && addr<=0x3FB8) {
        	ram2[addr-0x3EB8] = value;
        } 
        
        else {		
        	throw "Write to "+addr+" from "+CPU6809.status()['pc'];
        }
		
	}
	
	function read(addr) {
		
		// 6809 reset vector (point to game code at 0600)
        if(addr===0xFFFE) return my.resetVector>>8;
        if(addr===0xFFFF) return my.resetVector&0xFF;
        
        if(addr==0xA6) {
        	console.log('PRINTCHAR');
        	return 0x39;
        }
        
        if(addr<0x300) {
        	return ram[addr];
        }        
        if(addr>=0x300 && addr<=0x3EB7) {
        	return binData.read(addr);
        }
        if(addr>=0x3EB8 && addr<=0x4000) {
        	return ram2[addr-0x3EB8];
        }
        
        // TODO random routine uses ROM bytes. If we are in that routine, return a random value.
        // PC==0673
        
        if(addr>=0xA000 && addr<0xC000 && (CPU6809.status()['pc']==0x0673||CPU6809.status()['pc']==0x0675)) {
        	// TODO random value
        	return 20;
        }
        
        if(addr==0xA1C1) {
        	// TODO Clear the Z flag
        	// This is the wait-for-key to start the game.
        	return 0x39;
        }
        if(addr==0xA928) {
        	console.log('CLEARSCREEN');
        	var i;
        	for(i=0x400;i<0x600;++i) {
        		ram[i] = 0x60;
        	}
        	ram[0x88] = 0x04;
        	ram[0x89] = 0x00;
        	return 0x39;
        }
        if(addr==0xA976) {
        	console.log('Enable sound');
        	return 0x39;
        }
        if(addr==0xA9A2) {
        	console.log('Sound is DAC');
        	return 0x39;
        }
                
		throw "Read of "+addr+" from "+CPU6809.status()['pc'];
	}
	
	CPU6809.init(write,read,function(){});
	
	while(true) {
		CPU6809.steps(1);
	}
			
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