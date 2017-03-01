$(function() {
	
	$("#floorOne").on("click",function() {
		BinaryData.loadDataCacheFromURL("/TRS80/HauntedHouse/Code1.html",function() {
			floor=1;
			TRS80Text.reset();
			TRS80Text.runUntilWaitKey();  
		});
	});
	
	$("#floorTwo").on("click",function() {		
		BinaryData.loadDataCacheFromURL("/TRS80/HauntedHouse/Code2.html",function() {
			floor=2;
			TRS80Text.reset();
			TRS80Text.runUntilWaitKey();  
		});
	});
	
	var floor=1;
	
	function write(addr,value) {
		// From the loaded game RAM
		if(addr>=0x42E9 &&addr<0x5000) {
			BinaryData.write(addr,value);
			return true;
		}
		
		return undefined;
	}
	
	function read(addr) { 
		
		// Endless loops in code
		if(floor===1 && addr===0x4A48) {
			TRS80Text.startEndlessLoop(); 
			return 0;					
		}
		if(floor===2 && addr===0x4A97) {
			TRS80Text.startEndlessLoop(); 
			return 0;					
		}
				
		if(addr===0x4774) {
		    // We hijacked the input spin-loop. We need
		    // to simulate the random number counter.
            return Math.floor(Math.random()*256);
        }
		
		// From the loaded game RAM
		if(addr>=0x42E9 &&addr<0x5000) {
			return BinaryData.read(addr);
		}
		
		return undefined;
	}
	
	BinaryData.loadDataCacheFromURL("/TRS80/Pyramid/Code.html",function() {		
		TRS80Text.init(read,write,function() {TRS80Text.runUntilWaitKey();}, 0x4300);
		TRS80Text.runUntilWaitKey();    
	});	
	
});




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
	
	$("#floorOne").on("click",function() {
		BinaryData.loadDataCacheFromURL("/TRS80/HauntedHouse/Code1.html",function() {
			floor=1;
			endlessloop = false;
			comp.reset();
			runTillInput();
		});
	});
	
	$("#floorTwo").on("click",function() {		
		BinaryData.loadDataCacheFromURL("/TRS80/HauntedHouse/Code2.html",function() {
			floor=2;
			endlessloop = false;
			comp.reset();
			runTillInput();
		});
	});
	
	var floor=1;
		
	BinaryData.loadDataCacheFromURL("/TRS80/HauntedHouse/Code1.html",function() {		
		
		var machine = {		
			mem_read : function(addr) {
				
				// Endless loops in code
				if(floor===1 && addr===0x4A48) {
					endlessloop = true;
					running = false;
					return 0;					
				}
				if(floor===2 && addr===0x4A97) {
					endlessloop = true;
					running = false;
					return 0;					
				}
				
				if(addr>=0x42E9 &&addr<0x5000) {
					return BinaryData.read(addr);
				}
									
				// Reset (starutp) comes here. Jump to the program.
				// JP $42E9
				if(addr===0) return 0xC3;
				if(addr===1) return 0x5E;
				if(addr===2) return 0x43;
	
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
				
				// Tape operation (loading 2nd floor)
				if(addr===0x0293) {
					BinaryData.loadDataCacheFromURL("/TRS80/HauntedHouse/Code2.html",function() {
						comp.reset();
						runTillInput();
					});
					running = false;
					return 0;
				}				
				throw "Unknown memory read "+addr;
			},
			mem_write : function(addr,value) {
				if(addr>=0x42E9 &&addr<0x5000) {
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
		
}

