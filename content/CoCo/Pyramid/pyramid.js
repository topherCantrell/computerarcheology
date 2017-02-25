
var running;
var endlessloop = false;

function runTillInput() {	
	running = true;	
	while(running) {
		CPU6809.steps(1);
	}	
}

$(function() {
    
	var inputKey;
	
	var console = $("#cocoConsole");
	
	var pureRAM = [];
	for(var x=0;x<0600;++x) pureRAM.push(0);
		
	console.on("keydown",function(evt) {		
		inputKey = evt.keyCode;
		if(!endlessloop) {
			runTillInput();
		}
		return false;
	});
	
    function write(addr,value) {
    	// Pure RAM in the COCO system
        if(/*addr>=0x01B0 && */addr<0x600) {
        	pureRAM[addr] = value;
        	return;
        }
        if(addr>=0x600 && addr<0x3F21) {
            BinaryData.write(addr,value);
            return;
        }
        throw "Unhandled write "+addr+":"+value;
    }
    
    function read(addr) {
        
        // 6809 reset vector (point to game code at 0600)
        if(addr===0xFFFE) return 0x06;
        if(addr===0xFFFF) return 0x00;
        
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
            var oldtext = console.text();
			if(value===8) {
				oldtext = oldtext.substring(0,oldtext.length-1);
			} else {
				oldtext = oldtext+String.fromCharCode(value);
			}
			console.text(oldtext);
			console.scrollTop(console[0].scrollHeight);			
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
        
        // Pure RAM in the COCO system
        if(addr>=0x1B0 && addr<0x600) {
        	return pureRAM[addr];
        }
        
        // RAM where the game is loaded
        if(addr>=0x0600 && addr<0x3F21) {
            return BinaryData.read(addr);
        }
        
        // Oops! Not in our address space
        throw "Unhandled read "+addr;
    }
      
    BinaryData.loadDataCacheFromURL("/CoCo/Pyramid/Code.html",function() { 
    	CPU6809.init(write,read,function(){});    
    	runTillInput();    	  
    });    
    
});