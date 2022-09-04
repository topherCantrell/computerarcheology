function makeBinaryDataPyramid() {
    
    var dataOrigin = 0x4300;    
           
    var datab = Binary.readBinary('Code.md.bin')
    var data = []    
    for(var i=0;i<datab.length;i++) {
        data.push(datab[i])
    }
        
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

function startTRS80Pyramid(consoleElement,tapeElement) {
	
	var TRS80Text = makeTRS80Text(consoleElement,tapeElement);
	// The game code
	var binData = makeBinaryDataPyramid();
	
	function write(addr,value) {
		// From the loaded game RAM
		if(addr>=0x4300 && addr<0x8000) {
			binData.write(addr,value);
           return true;
        }
		
		return undefined;
	}
	
	function read(addr) { 
	    
	    // Virtual tape area
        if(addr===0x7FA0) {
            $("#tapeArea").show();
        }
		
		if(addr===0x55F2) {
		    // This is the endless loop in the game
			TRS80Text.startEndlessLoop(); 
		    return 0x00; // NOP
		}
		
		if(addr===0x4774) {
		    // We hijacked the input spin-loop. We need
		    // to simulate the random number counter.
            return Math.floor(Math.random()*256);
        }
		
		// From the loaded game RAM
		if(addr>=0x4300 && addr<0x8000) {
            return binData.read(addr);
        }
		
		return undefined;
	}
	
	function ioread(addr) {
        return undefined;
    }
    
    function iowrite(addr,value) {
        return undefined;
    }
		
	TRS80Text.init(
			read,
			write,
			ioread, 
			iowrite,
			function() {TRS80Text.runUntilWaitKey();}, 
			0x4300);
	TRS80Text.runUntilWaitKey();    
		
};
