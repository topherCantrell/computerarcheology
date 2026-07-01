function startXenos(consoleElement, tapeElement) {	
	loadBinaryFromUrl("combined.bin", consoleElement, tapeElement);	
};

function getRandomIntInclusive(min, max) {
  const minCeiled = Math.ceil(min);
  const maxFloored = Math.floor(max);
  // The maximum is inclusive and the minimum is inclusive
  return Math.floor(Math.random() * (maxFloored - minCeiled + 1) + minCeiled);
};

async function loadBinaryFromUrl(url,consoleElement, tapeElement) {
  try {
    const response = await fetch(url);
    
    // Read the body data as an ArrayBuffer
    const buffer = await response.arrayBuffer();
    
    // View the raw bytes using a TypedArray (0 to 255)
    const bytes = new Uint8Array(buffer);    

	const combinedBuffer = new ArrayBuffer(bytes.length + 0x5D00);
	const view = new Uint8Array(combinedBuffer);
	view.set(bytes,0x5D00);
	startXenosAfterLoad(view, consoleElement, tapeElement);
  } catch (error) {
    console.error("Failed to load binary file:", error);
  }
}


// TODO quit/exit program

function makeXenosMachine(consoleElement,tapeElement) {
	
	// this/self
	var my = {};
	
	// The Z80 CPU
	var comp;
	var running;
	var endlessLoop;
	var noInput;
	var inputKey;
	
	var gameConsole;
	var tape;		

	var systemObjects;
	var loadPosition;

	function printChar(value) {
		var x = gameConsole.value = gameConsole.value + String.fromCharCode(value);
		if(x.length>1024) {
			x = x.substring(x.length-1024);
		}
		gameConsole.value = x;
		gameConsole.scrollTop = gameConsole.scrollHeight;
	}
	
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
    
    my.init = function(binData) {    			

		gameConsole = document.getElementById(consoleElement);
		tape = document.getElementById(tapeElement);
		tapeArea = document.getElementById(tapeElement+"Area");				
		
		gameConsole.addEventListener("keydown",function(evt) {   			
			if(!endlessLoop && !noInput) {
			    if(evt.keyCode===16) return; // Lone shift key
				inputKey = evt.keyCode;
				my.runUntilWaitKey();
			}
			// Consume the event
            evt.preventDefault();
		});
		
		var machine = {
			mem_read : function(addr) {				
				
				// Reset (starutp) comes here. Jump to the program.
				// JP $5D00
				if(addr===0) return 0xC3; // JP
				if(addr===1) return 0x00;
				if(addr===2) return 0x5D;
				
				// Key input routine.
                // The first IN halts the CPU until a key is ready.
                // The second IN returns the actual key.                
				// 002B: 00     NOP    ; Halt the machine until a key is pressed
				// 002C: C9     RET    ; Return the key that was pressed
                if(addr===0x2B) {
					running = false;
					return 0x00;
				}
                if(addr===0x2C) {
					var zstate = comp.getState();
					var c = inputKey;
					if(c>=97 && c<=122) { // Convert lowercase to uppercase
						c = c - 32;
					}
					zstate.a = c;
					comp.setState(zstate);
					return 0xC9;
				}                
	
                // Print routine.
                // 0033: C9     RET   ; Print the character in A
                if(addr===0x33) {
					var zstate = comp.getState();
					printChar(zstate.a);
					if(zstate.a==13) {
						for(var i=0;i<64;i++) {
							binData[0x3FC0+i] = 0x20; // Clear the bottom row
						}
						binData[0x4020] = 0xC0
        				binData[0x4021] = 0x3F
					}
					return 0xC9;
				}

				if(addr==0x4420) { // Open new or existing (we only get here for SAVE)
					var zstate = comp.getState();
					zstate.flags['Z'] = 1;
					comp.setState(zstate);
					tape.value = "";
					return 0xC9
				}

				if(addr==0x4424) { // Open existing (only get here for LOAD)
					loadPosition = 0;
					var zstate = comp.getState();
					zstate.flags['Z'] = 1;
					comp.setState(zstate);
					return 0xC9
				}

				if(addr==0x4428) { // Open new or existing (we only get here for SAVE)
					var zstate = comp.getState();
					zstate.flags['Z'] = 1;
					comp.setState(zstate);
					return 0xC9
				}

				if(addr==0x4436) { // Read 3 bytes into HL
					var zstate = comp.getState();
					var s = tape.value
					while(s.length < 960) {
						s = s + "0";
					}
					var hl = zstate.h*256 + zstate.l;
					for(var i=0;i<3;i++) {
						var dat = s.substring(loadPosition,loadPosition+2);
						loadPosition = loadPosition + 2;
						var v = parseInt(dat,16);
						binData[hl+i] = v;
					}						
					zstate.flags['Z'] = 1;
					comp.setState(zstate);
					return 0xC9;
				}

				if(addr==0x4439) { // Write 3 bytes pointed to by HL (return Z=1)
					var zstate = comp.getState();
					var hl = zstate.h*256 + zstate.l;
					for(var i=0;i<3;i++) {
						var v = binData[hl+i].toString(16).toUpperCase();
						if(v.length==1) v = "0"+v;
						tape.value = tape.value + v;
					}
					zstate.flags['Z'] = 1;
					comp.setState(zstate);
					return 0xC9;
				}

				if(addr==0x619F) {
					var zstate = comp.getState();
					zstate.pc = 0x5D3B - 1;
					comp.setState(zstate);
					printChar(13);
					for(var i=0;i<64;i++) {
						printChar(binData[0x3FC0+i]);
						//msg = msg + String.fromCharCode(binData[0x3FC0+i]);
						binData[0x3FC0+i] = 0x20; // Clear the bottom row
					}
					printChar(13);

					return 0x00; // NOP					
				}

				if(addr==0x61EB) {
					var zstate = comp.getState();
					// TODO handle backspace specially
					if(zstate.a==8) {
						gameConsole.value = gameConsole.value.substring(0,gameConsole.value.length-1);
						return binData[addr];
					}
					if (zstate.a!=13) {
						printChar(zstate.a);
					}
					return binData[addr];
				}

				if(addr==0x6A29) { // Load disk section
					console.log("Load disk section "+binData[0x6AEC]);
					// Each section is 2817 bytes (thats 0xB00 + 1)
					// The sections follow the main program that is 25344 bytes
					// The data is loaded into memory at 5D00
					// Section 0 starts at 0xC000
					var sp = (binData[0x6AEC]-0x30-1)*2817 + 0xC000;
					// Probably some fancy new way to do this in JS
					for(var i=0;i<2816;i++) {
						binData[0x5200+i] = binData[sp+i];
					}
					var zstate = comp.getState();
					zstate.pc = 0x6A6F-1;
					comp.setState(zstate);
					return 0x00; // NOP					
				}

				if(addr==0xBB5A) {
					tapeArea.style.display = "block";
				}

				if(addr==0x71E4) { // Code that generates random word in 71EC
					binData[0x71EC] = getRandomIntInclusive(0,255);
					binData[0x71ED] = getRandomIntInclusive(0,255);
					return 0x97; // SUB A instruction
				}

				if(addr>=0x9EFF && addr<0xA0F0) {
					console.log("Hit script at "+addr.toString(16));
					return binData[addr];
				}

				// if(addr==0x6E6A) { // save game
				// 	var zstate = comp.getState();
				// 	zstate.pc = 0x6E3F-1;
				// 	comp.setState(zstate);
				// 	return 0x00; // NOP
				// }

				// if(addr==0x6E82) { // load game					
				// 	var zstate = comp.getState();
				// 	zstate.pc = 0x6E3F-1;
				// 	comp.setState(zstate);
				// 	return 0x00; // NOP
				// }

				if(addr==0x6EBB) { // Save system objects
					systemObjects = [];
					for(var i=0x887A;i<0xB3AF;i++) {						
						systemObjects.push(binData[i]);
					}					
					var zstate = comp.getState();
					zstate.pc = 0x6F45-1;
					comp.setState(zstate);
					return 0x00; // NOP
				}

				if(addr==0x6EC5) { // Restore system objects
					for(var i=0x887A;i<0xB3AF;i++) {
						binData[i] = systemObjects[i-0x887A];
					}
					var zstate = comp.getState();
					zstate.pc = 0x6F45-1;
					comp.setState(zstate);
					return 0x00; // NOP
				}

				// -------------------

				// Screen memory
				if(addr>=0x3C00 && addr<0x4400) {
					return binData[addr];
				}
				
				// From the game code
				if(addr>=0x5200 && addr<0xC000) {
					return binData[addr];
				}

				z = comp.getState();                
                throw "Unknown memory read "+addr+" PC="+z.pc;
			},
			mem_write : function(addr,value) {
				if(addr>=0x3C00 && addr<0x4000) {
					binData[addr] = value;
					return true;
				}
				if(addr>=0x4000 && addr<0xC000) {
					// Anywhere else in RAM
					binData[addr] = value;
					return true;
				}
				throw "Unknown memory write "+addr;
			},
			io_read : function(addr) {				
				throw "Unknown io read "+addr;
			},
			io_write : function(addr,value) {
				addr = addr & 0xFF;								
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

function startXenosAfterLoad(bytes, consoleElement, tapeElement) {

	var xenosMachine = makeXenosMachine(consoleElement, tapeElement);	

	xenosMachine.init(bytes);

	// Run the machine until the code waits for a key from the user
	xenosMachine.runUntilWaitKey();    		

}

