// "splashElement", "madnessConsole",""
function startMadness() {
	
	// ASCII to CoCo screen printable
	var CHARMAP = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
				  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
				  "@ABCDEFGHIJKLMNOPQRSTUVWXYZ[~]~~"+
				  " !\"#$%&'()*+,-./0123456789:;<=>?"+
				  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
				  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
				  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
				  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~";
	
	// It is easier to have the RAM and program data in one array.
	// Pull the binary into RAM.
	var binData = makeBinaryDataPyramid();
	var ram = Array(0x5000);
	var x;
	var screen=1;
	for(x=0;x<300;++x) {
		ram[x] = 0;
	}
	for(x=0x300;x<0x3EB8;++x) {
		ram[x] = binData.read(x);
	}
	for(x=0x3EB8;x<0x5000;++x) {
		ram[x]=0;
	}
	
	// Initialize the 6809 CPU.
	var CPU6809 = make6809();	
	var resetVector = 0x300;	
	CPU6809.init(write,read,function(){});	
	CPU6809.set('sp',0x1FFF);
	CPU6809.set('dp',0);
	
	// State's in the running game:
	//   - null: waiting for the game to start
	//   - init: running the initialization code
	//   - waitForStart: the game is waiting for the user to press a key to start
	//   - waitForKey: the game running is waiting of the user to enter a key
	//   - playing: the game processing code is running
	//   - servicingInterrupt: the service interrupt code is running
	//   - interruptDone: the service interrupt code has finished
	var state = null;
	
	var cursorChar = '\u2588';
	var cursorChar2 = ' ';
	var cursorCur = cursorChar;
	
	var quietMode = false;
	
	var cocoConsole = $('#madnessConsole');
	
	$('#splashElement').on('click',function() {
		$('#splashElement').hide();
		cocoConsole.show();
		cocoConsole.focus();
		state='init';		
		runUntilStateChange(); // We assume this is pretty quick
		// Start the 1s game interrupt
		setInterval(interrupt,1000);
	});
		
	cocoConsole.keydown(function(evt) {
		
		var c = evt.keyCode
		if(c==16) {
			return;
		}
		
		// Consume the event
        evt.preventDefault();
		
		if(state=='init') {
			// Starting up ... ignore the key
			return;
		}
		
		if(state=='waitForStart') {
			// We are waiting to start. Eat the key and run to the
			// next input wait.
			state='playing';
			runUntilStateChange();
			return;
		}
		
		if(state=='waitForKey') {
			//console.log(c);			
			if(c==38) {
				screen = 0;				
				updateScreen();
				return;
			}
			if(c==40) {
				screen = 1;
				updateScreen();
				return;
			}
			if(c==49 && evt.shiftKey) {
				c = 33; // !
			} else if(c==48 && evt.shiftKey) {
				c = 41; // )
			}
			CPU6809.set('a',c);
			state='playing';
			removeCursor();
			runUntilStateChange();
			return;
		}
		
		throw "Unknown game state "+state;
		
	});
	
	
	function runUntilStateChange() {
		// We assume this is very fast ... fast enough to
		// run synchronously. The "read" handler will change
		// the states at key points in the code (like when
		// the code calls out to wait for a key).
		var curState = state;
		while(curState == state) {
			CPU6809.steps(1);
		}		
	}
	
	function updateScreen() {
		// Called anytime the screen memory is twiddled and the
		// GUI needs refreshing.		
        var t = "";
        var p = 0x400;
        if(screen==0) {
        	p = 0x200;
        }
        for(var y=0;y<16;++y) {
            for(var x=0;x<32;++x) {
                var c = ram[p++];
                if(c==0) {
                	t = t + cursorCur;                	
                } else {
                	t = t + CHARMAP[c];
                }
            }       
            if(y!=15) t=t+"\n";            
        }
        cocoConsole.text(t);
    }
			
	function interrupt() {
		
		// Called by the 1-second timer
		
		if(state=='waitForStart') {
			// We haven't started the code yet. Ignore this.
			return;
		}
		
		if(state!='waitForKey') {
			// This better be the state we are in when an interrupt
			// comes in.
			throw 'UNEXPECTED STATE FOR INTERRUPT: '+state;
		}
		
		if(quietMode) {
			// Quiet mode ... no interrupts
			return;
		}
		
		//console.log('Interrupt');
		state='servicingInterrupt';
		
		// Hold all the registers (INT would push them on the stack)
		var status = CPU6809.status();
				
		// Modified service routine address. We only need the 1s tick.
		CPU6809.set('pc',0x0751);
		removeCursor();
		runUntilStateChange();
		drawCursor();
		
		// Back to the waiting state.
		state = 'waitForKey';
		
		// Restore the registers (RTI would pop these)
		CPU6809.set('a',status['a']);
		CPU6809.set('b',status['b']);
		CPU6809.set('flags',status['flags']);
		CPU6809.set('pc',status['pc']);
		CPU6809.set('sp',status['sp']);
		CPU6809.set('u',status['u']);
		CPU6809.set('x',status['x']);
		CPU6809.set('y',status['y']);
						
	}
			
	function write(addr,value) {
		// All 6809 writes are handled here
		
		if(addr<0x5000) {
        	ram[addr] = value;
        	if(addr>=0x400 && addr<0x600) {
        		updateScreen();
        	}
        } else if(addr>=0xFF00) {
        	// Ignore writes to hardware
        }
        
        else {		
        	throw "Write to "+addr+" from "+CPU6809.status()['pc'];
        }
		
	}
	
	function drawCursor() {
		cp = ram[0x88]<<8 | ram[0x89];
		ram[cp]=0;
		updateScreen();
		if(cursorCur==cursorChar) {
			cursorCur = cursorChar2;
		} else {
			cursorCur = cursorChar;
		}
	}
	function removeCursor() {
		cp = ram[0x88]<<8 | ram[0x89];
		ram[cp]=0x60;
		updateScreen();		
	}
	
	var readingFirst = true;
	
	function read(addr) {
		
		// All 6809 reads are handled here
		
		// 6809 reset vector (point to game code at 0600)
        if(addr===0xFFFE) return resetVector>>8;
        if(addr===0xFFFF) return resetVector&0xFF;
        
        if(addr==0x080E) {
        	// This is the RTI at the end of the interrupt service
        	if(state!='servicingInterrupt') {
        		throw 'RTI but not in interrupt service';
        	}
        	state = 'interruptDone';
        	return 0x12; // NOP (We will be restoring everything)        	
        }
        
        if(addr==0x0B3E) {
        	var audio = new Audio('flute.wav');
        	audio.play();
        	return 0x39;
        }
        
        if(addr==0x173F) {
        	quietMode=true;
        	$('#cocoTapeArea').show();
        	return 0xBD;
        }
        if(addr==0x1767) {
        	quietMode=false;        	
        	return 0x7E;
        }
        
        if(addr==0x11D) {        	
        	var data = '';
        	var x;
        	// 0200-05FF (engine data and screen)
        	// 3BC1-3FFF (tables)
        	for(x=0x240;x<0x600;++x) {
        		data = data + String.fromCharCode(ram[x]);
        	}
        	for(x=0x3BC1;x<0x4000;++x) {
        		data = data + String.fromCharCode(ram[x]);
        	}
        	$('#cocoTape').val(btoa(data));
        	return 0x39;
        }
        if(addr==0xA500) {
        	// Two reads in a row. Ignore the first one. We do all the work
        	// in the second.
        	if(readingFirst) {
        		readingFirst = false;
        		return 0x39
        	}        	        	
        	data = atob($('#cocoTape').val());
        	var pos = 0;
        	for(x=0x240;x<0x600;++x) {
        		ram[x] = data.charCodeAt(pos++);        		
        	}
        	for(x=0x3BC1;x<0x4000;++x) {
        		ram[x] = data.charCodeAt(pos++); 
        	}   
        	updateScreen();
        	return 0x39;
        }
                
        if(addr<0x5000) {
        	return ram[addr];
        }        
        
        // Random routine uses ROM bytes. If we are in that routine, return a random value.                
        if(addr>=0xA000 && addr<=0xC005 && (CPU6809.status()['pc']==0x0673||CPU6809.status()['pc']==0x0675)) {
        	return Math.floor(Math.random()*256); // returns a random integer from 0 to 255
        }
        
        if(addr==0xA1B1) {
        	drawCursor();
        	state = 'waitForKey';
        	// We return, but we aren't running. The key-event will set
        	// the A register before starting again.
        	return 0x39;
        }
        
        if(addr==0xA1C1) {        	
        	// This is the wait-for-key to start the game.
        	updateScreen();
        	state = 'waitForStart';
        	cc = CPU6809.status()['flags'];
        	cc = cc & 0xFB; // Clear the Z flag.
        	CPU6809.set('flags',cc);
        	return 0x39;
        }
        if(addr==0xA34E) {
        	// Scroll 2-page screen
        	
        	var i;
        	for(i=0x240;i<0x05E0;++i) {
        		ram[i] = ram[i+32];
        	}
        	
        	for(i=0x05E0;i<0x600;++i) {
        		ram[i] = 0x60;
        	}        	
        	
        	ram[0x88] = 0x05;
        	ram[0x89] = 0xE0;
        	updateScreen();
        	return 0x35;
        }
        if(addr==0xA34F) {
        	return 0x96;
        }
        if(addr==0xA7EB) {
        	// Cas Motor off
        	return 0x39;
        }
        if(addr==0xA928) {
        	// Clear screen
        	var i;
        	for(i=0x400;i<0x600;++i) {
        		ram[i] = 0x60;
        	}
        	ram[0x88] = 0x04;
        	ram[0x89] = 0x00;
        	return 0x39;
        }
        if(addr==0xA92F) {
        	// Clear 2 page video
        	var i;
        	for(i=0x200;i<0x600;++i) {
        		ram[i] = 0x60
        	}        	
        	return 0x39;
        }
        if(addr==0xA976) {
        	// Sound is enabled
        	return 0x39;
        }
        if(addr==0xA9A2) {
        	// Sound is DAC
        	return 0x39;
        }
        if(addr>=0xFF00) {
        	// Ignore reads from hardware
        	return 0;
        }
                
		throw "Read of "+addr+" from "+CPU6809.status()['pc'];
	}		
    
};

function viewSaveFile(data) {
	data = atob(data);	
}