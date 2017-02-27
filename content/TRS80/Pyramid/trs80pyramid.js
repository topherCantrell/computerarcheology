

// The Z80 computer
var comp;
var running;
var endlessloop;

function runTillInput() {	
	running = true;
	while(running) {
		comp.run_instruction();
	}	
}

window.onload = function() {
	
	var inputKey;
	
	var console = $("#trs80console");
		
	console.on("keydown",function(evt) {		
		inputKey = evt.keyCode;
		if(!endlessloop) {
			runTillInput();
		}
		return false;
	});

	BinaryData.loadDataCacheFromURL("/TRS80/Pyramid/Code.html",function() {		
		
		var machine = {		
			mem_read : function(addr) {
									
				// Reset (starutp) comes here. Jump to the program.
				// JP $42E9
				if(addr===0) return 0xC3;
				if(addr===1) return 0x00;
				if(addr===2) return 0x42;
	
				// Key input routine (the game reads the keyboard manually)
				// The first IN halts the CPU until a key is ready.
				// The second IN returns the actual key.
				// 44E9: DB 00  IN A,($00)   ; Trigger halt-till-key
                // 44EB: DB 01  IN A,($01)   ; Return last key
                // 44ED: C9     RET
				if(addr===0x44E9) return 0xDB;
				if(addr===0x44EA) return 0x00;
				if(addr===0x44EB) return 0xDB;
				if(addr===0x44EC) return 0x01;
				if(addr===0x44ED) return 0xC9;
	
				// Print routine.
				// 0010: D3 00  OUT ($00),A
				// 0012: C9     RET	
				if(addr===0x10) return 0xD3;
				if(addr===0x11) return 0x00;
				if(addr===0x12) return 0xC9;
				
				if(addr===0x558F) {
				    // This is the endless loop in the game
				    endlessloop = true;
				    running = false;
				    return 0x00; // NOP
				}
				
				if(addr===0x4711) {
				    // We hijacked the input spin-loop. We need
				    // to simulate the random number counter.
		            return Math.floor(Math.random()*256);
		        }
				
				if(addr>=0x4200 &&addr<0x8000) {
                    return BinaryData.read(addr);
                }
								
				throw "Unknown memory read "+addr;
			},
			mem_write : function(addr,value) {
				if(addr>=0x4200 &&addr<0x8000) {
					BinaryData.write(addr,value);				
					return;
				}
				throw "Unknown memory write "+addr;
			},
			io_read : function(addr) {
				addr = addr & 0xFF;
				if(addr===0) {
					running = false;
					return;
				}
				if(addr===1) {
				    return inputKey;
				}
				throw "Unknown io read "+addr;
			},
			io_write : function(addr,value) {
				addr = addr & 0xFF;
				if(addr===0) {					
					var oldtext = console.text();
					if(value===8) {
						oldtext = oldtext.substring(0,oldtext.length-1);
					} else if(value===14) {
						oldtext = "";
					} else {
						oldtext = oldtext+String.fromCharCode(value);
					}
					console.text(oldtext);
					console.scrollTop(console[0].scrollHeight);
					return;
				}
				throw "Unknown io write "+addr;
			}		
		};
				
		comp = new Z80(machine);
		
		runTillInput();
	
	});
		
};

