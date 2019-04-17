function startMadness(splashElement, consoleElement,tapeElement) {
				
	var cocoConsole = $('#'+consoleElement);
	
	$('#'+splashElement).on('click',function() {
		$('#'+splashElement).hide();
		cocoConsole.show();
		cocoConsole.focus();
		state='init';
		runUntilWaitKey();
	});
	
	
	cocoConsole.keypress(function(evt) {
		
		if(state=='init') {
			// Starting up ... ignore the key
			return;
		}
		
		if(state=='waitForStart') {
			// We are waiting to start. Eat the key and start the
			// CPU running again.
			state='playing';
			runUntilWaitKey();
			return;
		}
		
		if(state=='waitForKey') {
			var c = String.fromCharCode(evt.charCode);
			c = c.toUpperCase();
			c = c.charCodeAt(0);		
			console.log(c);
			CPU6809.set('a',c);
			state='playing';
			runUntilWaitKey();
			return;
		}
		
		throw "Unknown state "+state;
		
	});
	
	var CHARMAP = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
				  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
				  "@ABCDEFGHIJKLMNOPQRSTUVWXYZ[~]~~"+
				  " !\"#$%&'()*+,-./0123456789:;<=>?"+
				  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
				  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
				  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
				  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~";
	
	var binData = makeBinaryDataPyramid();
	var CPU6809 = make6809();
	var ram = Array(0x300);
	ram.fill(0);
	var ram2 = Array(0x5000-0x3EB8);
	ram2.fill(0);
	
	var running = true;
	var state = 'start';
		
	var my = {};
	
	my.resetVector = 0x300;
	
	CPU6809.init(write,read,function(){});
	// We start in the BASIC environment
	CPU6809.set('sp',0x1FFF);
	CPU6809.set('dp',0);
	
	function runUntilWaitKey() {
		// TODO interrupts
		running = true;
		while(running) {
			CPU6809.steps(1);
		}		
	}
	
	function updateScreen() {
		// TODO allow for flipping
        var t = "";
        var p = 0x400;
        for(var y=0;y<16;++y) {
            for(var x=0;x<32;++x) {
                var c = binData.read(p++);
                t = t + CHARMAP[c];
            }       
            if(y!=15) t=t+"\n";            
        }
        cocoConsole.text(t);
    }
			
	function write(addr,value) {
		
		if(addr<0x300) {
        	ram[addr] = value;
        } else if(addr>=0x300 && addr<=0x3EB7) {
        	binData.write(addr,value);
        	
        	if(addr>=0x400 && addr<0x600) {
        		updateScreen();
        	}
        	
        } else if(addr>=0x3EB8 && addr<=0x5000) {
        	ram2[addr-0x3EB8] = value;
        } else if(addr>=0xFF00) {
        	// Ignore writes to hardware
        }
        
        else {		
        	throw "Write to "+addr+" from "+CPU6809.status()['pc'];
        }
		
	}
	
	function read(addr) {
		
		// 6809 reset vector (point to game code at 0600)
        if(addr===0xFFFE) return my.resetVector>>8;
        if(addr===0xFFFF) return my.resetVector&0xFF;
                
        if(addr<0x300) {
        	return ram[addr];
        }        
        if(addr>=0x300 && addr<=0x3EB7) {
        	return binData.read(addr);
        }
        if(addr>=0x3EB8 && addr<=0x5000) {
        	return ram2[addr-0x3EB8];
        }
        
        // Random routine uses ROM bytes. If we are in that routine, return a random value.                
        if(addr>=0xA000 && addr<=0xC005 && (CPU6809.status()['pc']==0x0673||CPU6809.status()['pc']==0x0675)) {
        	return Math.floor(Math.random()*256); // returns a random integer from 0 to 255
        }
        
        if(addr==0xA1B1) {
        	// TODO blink cursor
        	running = false;
        	state = 'waitForKey';
        	// We return, but we aren't running. The key-event will set
        	// the A register before starting again.
        	return 0x39;
        }
        
        if(addr==0xA1C1) {        	
        	// This is the wait-for-key to start the game.
        	ram[0x400]=0x61;
        	updateScreen();
        	running = false;
        	state = 'waitForStart';
        	cc = CPU6809.status()['flags'];
        	cc = cc & 0xFB; // Clear the Z flag.
        	CPU6809.set('flags',cc);
        	return 0x39;
        }
        if(addr==0xA7EB) {
        	// Cas Motor off
        	return 0x39;
        }
        if(addr==0xA928) {
        	// Clear screen
        	var i;
        	for(i=0x400;i<0x600;++i) {
        		binData.write(i,0x60);
        	}
        	ram[0x88] = 0x04;
        	ram[0x89] = 0x00;
        	return 0x39;
        }
        if(addr==0xA92F) {
        	// Clear 2 page video
        	var i;
        	for(i=0x200;i<0x300;++i) {
        		ram[i] = 0x60
        	}
        	for(i=0x300;i<0x600;++i) {
        		binData.write(i,0x60);
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