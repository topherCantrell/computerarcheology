
var CoCoText = (function() {
	
	var my = {};
	
	var inputKey;
	var running;
	var endlessLoop = false;
	
	var pureRAM = [];
	
	var CHARMAP = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
                  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
	              "@ABCDEFGHIJKLMNOPQRSTUVWXYZ[~]~~"+
	              " !\"#$%&'()*+,-./0123456789:;<=>?"+
	              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
	              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
	              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
	              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~";
	
	function write(addr,value) {
        
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
        	throw "Unimplemented high ROM write "+addr;
        }
                        
        my.writeFN(addr,value);
    }
    
    function read(addr) {        
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
        		CPU6809.set("CC",CPU6809.status().cc & (0xFF-4)); // clear Z flag
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
        
        return my.readFN(addr);
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
    	my.console.val(t);
    }
	
	my.init = function(readFN, writeFN, onKeyPress, resetVector, console) {
		my.readFN = readFN;
		my.writeFN = writeFN;
		my.resetVector = resetVector;	
		my.console = console;
		my.onKeyPress = onKeyPress;
		
		for(var x=0;x<0600;++x) pureRAM.push(0);		
		
		updateScreen();
		
		console.on("keydown",function(evt) {	
			if(!endlessLoop) {
				inputKey = evt.keyCode;
				my.onKeyPress();
			}
			// Consume the event
			return false;
		});
		
		CPU6809.init(write,read,function(){});
	};
	
	my.runUntilWaitKey = function() {		
		if(endlessLoop) {
			return;
		}
		running = true;
		while(running) {			
			CPU6809.steps(1);
		}
	};
	
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
			} while((cursor%32)!=0);
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
	
	my.startEndlessLoop = function() {	
		running = false;
		endlessLoop = true;
	};
	
	return my;	
	
}());