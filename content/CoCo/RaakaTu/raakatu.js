
$(function() {
	
    function write(addr,value) {        
    	if(addr>=0x0600 && addr<0x3F18) {
    		// RAM where the game is loaded
        	BinaryData.write(addr,value);
        	return true;
        }    	
    }
    
    function read(addr) {   
        
        if(addr===0x09D6) {
            // This is the long delay loop for flashing an error hint.
            // We want that wait to happen by the browser ... not in a 
            // spin within the code.
            // TODO need to halt input to the text field here
            CoCoText.pause();
            setTimeout(function() {
                CoCoText.unpause();
                CoCoText.runUntilWaitKey();
            },100);
            return 0x12; // NOP
        }
        if(addr===0x09D7) {
            // We hijacked the long-delay loop starting at 09D6. We returned
            // a NOP. When the CPU resumes it comes here. We already delayed,
            // so cancel the spin routine.
            return 0x39; // RTS
        }
    	    	
    	if(addr===0x10B5) {
    		// This is the game's endless-loop after death and such
    		CoCoText.startEndlessLoop();    		
    	}
    	
        if(addr>=0x0600 && addr<0x3F18) {
        	// RAM where the game is loaded
            return BinaryData.read(addr); 
        }        
        
        return undefined;
        
    }
      
    BinaryData.loadDataCacheFromURL("/CoCo/RaakaTu/Code.html",function() { 
    	CoCoText.init(read,write,function() {CoCoText.runUntilWaitKey();}, 0x0600);
    	CoCoText.runUntilWaitKey();    	  
    });    
    
});