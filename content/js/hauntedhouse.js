

// The Z80 computer
var comp;
var running;

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
		runTillInput();
		return false;
	});
	
	$("#floorOne").on("click",function() {
		BinaryData.loadDataCacheFromURL("/TRS80/HauntedHouse/Code1.html",function() {
			comp.reset();
			runTillInput();
		});
	});
	
	$("#floorTwo").on("click",function() {		
		BinaryData.loadDataCacheFromURL("/TRS80/HauntedHouse/Code2.html",function() {
			comp.reset();
			runTillInput();
		});
	});
		
	BinaryData.loadDataCacheFromURL("/TRS80/HauntedHouse/Code1.html",function() {
		
		var machine = {		
			mem_read : function(addr) {
				
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

