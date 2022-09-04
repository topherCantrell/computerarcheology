
function makeBinaryDataPyramid() {
    
    var dataOrigin = 0x0600;    
           
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

function startPyramid(consoleElement,tapeElement) {
	
	// The CoCo emulator
	var CoCoText = makeCoCoText(consoleElement,tapeElement);
	// The game code
	var binData = makeBinaryDataPyramid();
	
    function write(addr,value) {        
    	if(addr>=0x0600 && addr<0x3F21) {
    		// RAM where the game is loaded
        	binData.write(addr,value);
        	return true;
        }    	
    }
    
    function read(addr) {   
    	
    	// The game uses the input-loop to increment 1EB as a
    	// random number. Since we aren't allowing the
    	// input loop to spin, we'll return a random number here.
    	if(addr===0x01EB) {
    		return Math.floor(Math.random()*256);
    	}
    	
    	// Virtual tape area
    	if(addr===0x3C27) {
    	    $("#cocoTapeArea").show();
    	}
    	    	    	
    	if(addr===0x0F1B) {
    		// This is the game's endless-loop after death and such
    		CoCoText.startEndlessLoop();    		
    	}
    	
        if(addr>=0x0600 && addr<0x3F21) {
        	// RAM where the game is loaded
            return binData.read(addr); 
        }        
        
        return undefined;
        
    }
      
    CoCoText.init(read,write,function() {CoCoText.runUntilWaitKey();}, 0x0600);
    CoCoText.runUntilWaitKey();    	          
    
};