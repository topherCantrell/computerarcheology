
var CoCoText = (function() {
	
	var my = {};
	
	var inputKey;
	var running;
	var endlessLoop = false;
	
	var pureRAM = [];
	var screenRAM = "";
	var cursor = 0x400;
	
	function write(addr,value) { 
		if(addr<0x0100) {
			if(addr===0x88) {
				cursor = (value<<8) | (cursor & 0xFF);
				return;
			}
			if(addr===0x89) {
				cursor = (cursor & 0xFF00) | value;
				return;
			}
        	throw "Unimplemented BASIC RAM write "+addr;
        }
        
        if(addr>=0x0400 && addr<0x0600) {
        	addr = addr - 0x400;
        	if(value==0x60) value=0x20;
        	screenRAM = screenRAM.substring(0,addr)+String.fromCharCode(value)+screenRAM.substring(addr+1);
        	updateScreen();
        	return;
        }
        
        if(addr>=0x8000 && addr<0xF000) {
        	throw "Unimplemented ROM write "+addr;
        }
        
        if(addr>=0xF000) {
        	throw "Unimplemented high ROM write "+addr;
        }
        
        if(addr<0x600) {
        	pureRAM[addr] = value;
        	return;
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
        
        if(addr<0x0100) {
        	if(addr===0x88) {
        		return cursor>>8;
        	}
        	if(addr===0x89) {
        		return cursor & 0xFF;
        	}
        	throw "Unimplemented BASIC RAM read "+addr;
        }
        
        if(addr>=0x0400 && addr<0x0600) {
        	throw "Unimplemented screen read "+addr;
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
    	var b = "";
    	for(var x=0;x<16;++x) {
    		b = b + screenRAM.substring(x*32,(x+1)*32);
    		if(x!==15) b = b + "\n";
    	}
    	my.console.val(b);
    }
	
	my.init = function(readFN, writeFN, onKeyPress, resetVector, console) {
		my.readFN = readFN;
		my.writeFN = writeFN;
		my.resetVector = resetVector;	
		my.console = console;
		my.onKeyPress = onKeyPress;
		
		for(var x=0;x<0600;++x) pureRAM.push(0);
		for(x=0;x<32*16;++x) screenRAM = screenRAM + " ";
		
		updateScreen();
		
		console.on("keydown",function(evt) {	
			alert("KEY");
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
		if(value==0x60) value=0x20;
		if(value===0x0D) {
			// Store spaces at cursor and bump until cursor is at beginning of line
			do {
				printByte(0x60);				
			} while((cursor%32)!=0);
			return;
		}
		if(value===0x08) {
			throw "Implement me";
		}
		
		var p = cursor-0x400;
		
		// TODO eh, after doing this I see it would be easier just to update the screen from pureRAM
		screenRAM = screenRAM.substring(0,p)+String.fromCharCode(value)+screenRAM.substring(p+1);
		++cursor;
		if(cursor===0x600) {
			cursor = cursor - 32;
			screenRAM = screenRAM.substring(32)+"                                ";
		}
		updateScreen();
		
	}
	
	my.startEndlessLoop = function() {	
		running = false;
		endlessLoop = true;
	};
	
	return my;	
	
}());