function makeTRS80Text() {
	
	// ROM Calls:
	// 0212 : turn on cassette
	// 01F8 : turn off cassette
	//
	// 0296 : read leader
	// 0287 : write leader
	//
	// 0264 : write byte in A
	// 0235 : read one byte to A
	
	var my = {};
	
	// The Z80 CPU
	var comp;
	var running;
	var endlessLoop;
	var noInput;
	var inputKey;
	
	var console;
	var tape;
	
	my.reset = function() {
		endlessLoop = false;
		comp.reset();
	};
	
	my.pause = function() {
		running = false;
		noInput = true;
	};
	
	my.unpause = function() {
        running = true;
        noInput = false;
    };
    
    my.changeResetVector = function(resetVector) {
        my.resetVector = resetVector;   
    };
    
    my.init = function(readFN, writeFN, ioreadFN, iowriteFN, onKeyPress, resetVector) {
    	my.readFN = readFN;
		my.writeFN = writeFN;
		my.ioreadFN = ioreadFN;
        my.iowriteFN = iowriteFN;
		my.resetVector = resetVector;	
		my.onKeyPress = onKeyPress;
		console = document.getElementById("trs80console");
		tape = document.getElementById("tape");		
		
		console.addEventListener("keydown",function(evt) {   			
			if(!endlessLoop && !noInput) {
				inputKey = evt.keyCode;
				my.runUntilWaitKey();
			}
			// Consume the event
            evt.preventDefault();
		});
		
		var machine = {
			mem_read : function(addr) {
				var ret = my.readFN(addr);
				if(ret!==undefined) return ret;
				
				// Reset (starutp) comes here. Jump to the program.
				// JP $42E9
				if(addr===0) return 0xC3; // JP
				if(addr===1) return my.resetVector&0xFF;
				if(addr===2) return my.resetVector>>8;
				
				// Key input routine.
                // The first IN halts the CPU until a key is ready.
                // The second IN returns the actual key.
                // 002B: DB 00  IN A,($00)
                // 002D: DB 01  IN A,($01)
                // 002F: C9     RET
                if(addr===0x2B) return 0xDB;
                if(addr===0x2C) return 0x00;
                if(addr===0x2D) return 0xDB;
                if(addr===0x2E) return 0x01;
                if(addr===0x2F) return 0xC9;
	
                // Print routine.
                // 0033: D3 00  OUT ($00),A
                // 0035: C9     RET 
                if(addr===0x33) return 0xD3;
                if(addr===0x34) return 0x00;
                if(addr===0x35) return 0xC9;
                
                // Tape write.
                // 0264: D3 00  OUT ($01),A
                // 0266: C9     RET 
                if(addr===0x0264) return 0xD3;
                if(addr===0x0265) return 0x01;
                if(addr===0x0266) return 0xC9;
                
                // Tape read.
                // 0235: DB 02  IN ($02),A
                // 0237: C9     RET 
                if(addr===0x0235) return 0xDB;
                if(addr===0x0236) return 0x02;
                if(addr===0x0237) return 0xC9;
                
                // Misc tape commands (do nothing)
                if(addr===0x0212) return 0xC9; // Turn on tape
                if(addr===0x01F8) return 0xC9; // Turn off tape
                if(addr===0x0296) {
                    tapepos = 0;
                    return 0xC9; // Read tape leader
                }
                if(addr===0x0287) {
                    tape.value = "";                    
                    return 0xC9; // Write tape leader                
                }
                throw "Unknown memory read "+addr;
			},
			mem_write : function(addr,value) {
				// Let the system have it first in case it overrides something.
				var ret = my.writeFN(addr,value);
				if(ret) return;
				throw "Unknown memory write "+addr;
			},
			io_read : function(addr) {
			    var ret = my.ioreadFN(addr);
			    if(ret!==undefined) return ret;
				addr = addr & 0xFF;
				if(addr===0) {
					running = false;
					return;
				}
				if(addr===1) {
				    return inputKey;
				}
				if(addr===2) {
				    var dat = tape.value;
				    var v = parseInt(dat.substring(tapepos,tapepos+2),16);
	                tapepos = tapepos + 2;
	                return v;
				}
				throw "Unknown io read "+addr;
			},
			io_write : function(addr,value) {
				addr = addr & 0xFF;
				var ret = my.iowriteFN(addr,value);
                if(ret) return;
				if(addr===0) {					
					var oldtext = console.value;
					if(value===8) {
						oldtext = oldtext.substring(0,oldtext.length-1);
					} else if(value===14) {
						oldtext = "";
					} else {
						oldtext = oldtext+String.fromCharCode(value);
					}
					console.value = oldtext;
					console.scrollTop = console.scrollHeight;
					//console.scrollTop(console.scrollHeight);
					return;
				}
				if(addr===1) {				    
				    value = value.toString(16).toUpperCase();
				    if(value.length<2) value = "0"+value;				    
				    tape.value = tape.value + value;
				    return;
				}
				throw "Unknown io write "+addr;
			}					
		};
		comp = new Z80(machine);
    };
    
    my.runUntilWaitKey = function() {		
		if(endlessLoop) {
			return;
		}
		running = true;
		while(running) {			
			comp.run_instruction();
		}
	};
	
	my.startEndlessLoop = function() {	
		running = false;
		endlessLoop = true;
	};
	
	return my;
	
};