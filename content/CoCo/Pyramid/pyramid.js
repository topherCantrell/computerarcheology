
function startPyramid(consoleElement,tapeElement) {
	
	// The CoCo emulator
	var CoCoText = makeCoCoText(consoleElement,tapeElement);
	// The game code
	var BinaryData = makeBinaryDataPyramid();
	
    function write(addr,value) {        
    	if(addr>=0x0600 && addr<0x3F21) {
    		// RAM where the game is loaded
        	BinaryData.write(addr,value);
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
    	    	    	
    	if(addr===0x0F1B) {
    		// This is the game's endless-loop after death and such
    		CoCoText.startEndlessLoop();    		
    	}
    	
        if(addr>=0x0600 && addr<0x3F21) {
        	// RAM where the game is loaded
            return BinaryData.read(addr); 
        }        
        
        return undefined;
        
    }
      
    BinaryData.loadDataCacheFromURL("/CoCo/Pyramid/Code.html",function() { 
    	CoCoText.init(read,write,function() {CoCoText.runUntilWaitKey();}, 0x0600);
    	CoCoText.runUntilWaitKey();    	  
    });    
    
};