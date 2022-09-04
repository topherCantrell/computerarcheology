function makeBinaryDataBedlam() {
    
    var dataOrigin = 0x0600;    
           
    var datab = Binary.readBinary('Code.md.bin')
    var data = []    
    for(var i=0;i<datab.length;i++) {
        data.push(datab[i])
    }
    // Drop the bootloader at the end of the disassembly
    data = data.slice(0,0x3F02-dataOrigin)    
    
    // Change the JSR at 0B6C to jump to the patch
    data[0x0B6D-dataOrigin] = 0x3F;
    data[0x0B6E-dataOrigin] = 0x02;
    
    // Here is the patch
    data = data.concat([0x34,0x04,0xC6,0x01,0xBD,0x13,0x19,0x5A,0x26,0xFA,0x35,0x04,0x39]);
    /* Call the random generator a number of times  
    ;
    ; Write random number to 3F05 each time 0B6C is hit
    0B6C: BD 3F 02
    ;      
    3F02: 34 04     PSHS  B
    3F04: C6 00     LDB   #??    ; Write a random number here first
    loop:
    3F06: BD 13 19  JSR   $1319
    3F09: 5A        DECB
    3F0A: 26 FA     BNE   loop
    3F0C: 35 04     PULS  B
    3F0E: 39        RTS     
    */
    
    var my = {};
    
    // Simple read/write
    my.read = function(addr) {
        return data[addr-dataOrigin];
    };
    my.write = function(addr,value) {
       data[addr-dataOrigin] = value;
    };
        
    return my;
    
};

function startBedlam(consoleElement) {
	
	// The CoCo emulator
	var CoCoText = makeCoCoText(consoleElement);
	// The game code
	var binData = makeBinaryDataBedlam();
	
    function write(addr,value) {        
    	if(addr>=0x0600 && addr<0x3F10) {
    		// RAM where the game is loaded
        	binData.write(addr,value);
        	return true;
        }    	
    }
    
    function read(addr) { 
    	
        if(addr===0x0B6C) {            
        	// The real code calls the random number generator in the input loop.
        	// We are hijacking the input loop to let the wait happen in the
        	// browser. We patched the code (see BinaryDataBedlam.js) to include
        	// an extra routine to spin the RNG a number of times. We randomize
        	// that spin count here.
            write(0x3F05,Math.floor(Math.random()*8)+1);
            // Fall through
        }        
        
        if(addr===0x0A17) {
            // This is the long delay loop for flashing an error hint.
            // We want that wait to happen by the browser ... not in a 
            // spin within the code.
            CoCoText.pause();
            setTimeout(function() {
                CoCoText.runUntilWaitKey();
            },100);
            return 0x12; // NOP
        }
        if(addr===0x0A18) {
            // We hijacked the long-delay loop starting at 09D6. We returned
            // a NOP. When the CPU resumes it comes here. We already delayed,
            // so cancel the spin routine.
            return 0x39; // RTS
        }
                
        if(addr===0x117B) {
            // This is the game's endless-loop after death and such
            CoCoText.startEndlessLoop();            
        }
        
        if(addr>=0x0600 && addr<0x3F10) {
            // RAM where the game is loaded
            return binData.read(addr); 
        }        
        
        return undefined;
        
    }

    CoCoText.init(read,write,function() {CoCoText.runUntilWaitKey();}, 0x0600);
    CoCoText.runUntilWaitKey();  
    
};