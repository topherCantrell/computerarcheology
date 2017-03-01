function makeCoCoText() {
	
	// ROM Calls:
	// [A004] Start cassette and read leader
	// [A006] Read block
	//        7E, 7F : Destination
	//        7C     : Block type
	//        7D     : Length
	//        Return ZF set if OK
	//
	// [A00C] Start cassette and write leader
	// [A008] Write block
	//        7E, 7F : Source
	//        7C     : Block type
	//        7D     : Length
	//
	// FF21 - write 34 to turn motor off
	
	var my = {};
	
	var inputKey;
	var running;
	var noInput;
	var endlessLoop = false;
	var tapepos;
	
	var pureRAM = [];
	
	var CHARMAP = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
                  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
	              "@ABCDEFGHIJKLMNOPQRSTUVWXYZ[~]~~"+
	              " !\"#$%&'()*+,-./0123456789:;<=>?"+
	              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
	              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
	              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
	              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~";
	
	var tape;
	var cocoConsole;
	
	function write(addr,value) {
		
		// Let the system have it first in case it overrides something.
		var ret = my.writeFN(addr,value);
		if(ret) return;
        
        if(addr<0x0600) {
        	pureRAM[addr] = value;
        	if(addr>=0x400 && addr<0x600) {
        		updateScreen();
        	}        	
        	return;
        }
        
        if(addr>=0x8000 && addr<0xF000) {
        	throw "Unimplemented ROM write "+addr;
        }
        
        if(addr>=0xF000) {
        	return;
        	//throw "Unimplemented high ROM write "+addr;
        }
                        
        throw "Unimplemented write "+addr;
    }
    
    function read(addr) {     
    	
    	var src;
    	var cnt;
    	var v;
    	
    	// Try the system first (in case it overrides something)
    	var ret = my.readFN(addr);
    	if(ret!==undefined) return ret;
    	
        // 6809 reset vector (point to game code at 0600)
        if(addr===0xFFFE) return my.resetVector>>8;
        if(addr===0xFFFF) return my.resetVector&0xFF;
        
        // BASIC ROM vector points to character-output
        // routine. We'll intercept C000 below.
        if(addr===0xA002) return 0xC1;
        if(addr===0xA003) return 0x00;
        
        // BASIC ROM vector points to character-input
        // routine. We'll intercept C100 below.
        if(addr===0xA000) return 0xC0;
        if(addr===0xA001) return 0x00;
        
        // Tape operations
        if(addr===0xA004) return 0xD0;
        if(addr===0xA005) return 0x04;
        if(addr===0xA006) return 0xD0;
        if(addr===0xA007) return 0x06;
        if(addr===0xA00C) return 0xD0;
        if(addr===0xA00D) return 0x0C;
        if(addr===0xA008) return 0xD0;
        if(addr===0xA009) return 0x08;
        
        if(addr===0xD004 || addr===0xD00C) { // Read/write leader  
        	if(addr===0xD00C) {
        	    tape.value = ""; // Writing? Clear the tape first.    		
        	}     	
        	tapepos = 0;
        	return 0x39; // RTS
        }
        if(addr===0xD006) { // Read block
        	src = (pureRAM[0x7E]<<8) | pureRAM[0x7F];
        	cnt = pureRAM[0x7D];       	
        	var dat = tape.value;
        	while(cnt>0) {
        		v = parseInt(dat.substring(tapepos,tapepos+2),16);
        		tapepos = tapepos + 2;
        		write(src++,v);
        		--cnt;
        	}
        	CPU6809.set("X",src);
        	CPU6809.set("FLAGS",CPU6809.status().flags | 4); // Set the Z flag (no error)
        	return 0x39;
        }        
        if(addr===0xD008) { // Write block
        	src = (pureRAM[0x7E]<<8) | pureRAM[0x7F];
        	cnt = pureRAM[0x7D];        	
        	while(cnt>0) {
        		v = read(src++).toString(16).toUpperCase();
        		if(v.length<2) v="0"+v;        		
        		tape.value = tape.value + v;
        		--cnt;
        	}
        	CPU6809.set("X",src);
        	return 0x39;
        }
        
        // Trying to read the code at the character-output routine.
        // Instead we'll print A on the screen and return a 0x39
        // (the opcode for RTS)
    	
        if(addr===0xC100) {
            var value = CPU6809.status().a;
            printByte(value);		
            return 0x39;
        }
        
        // Trying to read the code at the character-input routine.
        if(addr===0xC000 || addr===0xC001) {
        	if(inputKey) {
        		CPU6809.set("A",inputKey);
        		inputKey = null;
        		CPU6809.set("FLAGS",CPU6809.status().flags & (0xFF-4)); // clear Z flag
        		return 0x39;
        	}
        	running=false;
        	return 0x12; // NOP            
        }          
        
        if(addr>=0x8000 && addr<0xF000) {
        	throw "Unimplemented ROM read "+addr;
        }
        
        if(addr>=0xF000) {
        	throw "Unimplemented high ROM read "+addr;
        }
    
        if(addr<0x600) {
        	return pureRAM[addr];
        }
        
        throw "Unimplemented read "+addr;
    }
    
    function updateScreen() {
    	var t = "";
    	var p = 0x400;
    	for(var y=0;y<16;++y) {
    		for(var x=0;x<32;++x) {
    			var c = pureRAM[p++];
    			t = t + CHARMAP[c];
    		}    	
    		if(y!=15) t=t+"\n";
    	}
    	cocoConsole.value = t;
    }
    
    function printByte(value) {
		//console.log(""+value+":"+String.fromCharCode(value));		
		var cursor = (pureRAM[0x88]<<8) | (pureRAM[0x89]);
		if(value===0x08) {
			if(cursor===0x400) return; // Top of screen ... nothing to do
			cursor = cursor - 1;
			pureRAM[cursor] = 0x60;
		} else if(value===0x0D) {			
			do {
				pureRAM[cursor++] = 0x60;
			} while((cursor%32)!==0);
		} else {
			if(value<0x20) return; // No control characters
			if(value<128) {
				if(value<0x40) {
					value = value ^ 0x40;
				} else if(value>=0x60) {
					value = value & 0xDF;
					value = value ^ 0x40;
				}
			}
			pureRAM[cursor++] = value;			
		}
		if(cursor>=0x600) {
			for(var x=0x0420;x<0x600;++x) {
				pureRAM[x-32] = pureRAM[x];				
			}
			for(x=0x600-0x20;x<0x600;++x) {
				pureRAM[x] = 0x60;
			}
			cursor = 0x600-0x20;
		}
		pureRAM[0x88] = cursor>>8;
		pureRAM[0x89] = cursor & 0xFF;		
		updateScreen();
	}
    
    // ----- Public API -----
    
    my.pause = function() {
        running = false;
        noInput = true;
    };
        	
	my.init = function(readFN, writeFN, onKeyPress, resetVector) {
		my.readFN = readFN;
		my.writeFN = writeFN;
		my.resetVector = resetVector;			
		my.onKeyPress = onKeyPress;
		
		tape = document.getElementById("tape");
	    cocoConsole = document.getElementById("cocoConsole");
		
		for(var x=0;x<0600;++x) pureRAM.push(0);		
		
		updateScreen();
		
		cocoConsole.addEventListener("keydown",function(evt) {	
			if(!endlessLoop && !noInput) {
			    if(evt.keyCode===16) return; // Lone shift key
			    var c = evt.keyCode;			    
			    if(c===37)      c=0x15; // Left on PC becomes SHIFT-LEFT on coco
			    else if(c===39) c=0x5D; // Right on PC becomes SHIFT-RIGHT on coco
			    else if(c===46) c=0x09; // Del on PC becomes RIGHT on coco
			    else if(c===27) c=0x0C; // ESC on PC becomes CLEAR on coco
				inputKey = c;
				my.onKeyPress();
			}
			// Consume the event
			evt.preventDefault();
		});
		
		CPU6809.init(write,read,function(){});
	};
	
	my.runUntilWaitKey = function() {		
		if(endlessLoop) {
			return;
		}
		running = true;
		noInput = false;
		while(running) {			
			CPU6809.steps(1);
		}
	};
	
	my.set = function(register,value) {
		CPU6809.set(register,value);
	};
	
	my.startEndlessLoop = function() {	
		running = false;
		endlessLoop = true;
	};
	
	return my;	
	
};