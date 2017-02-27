
$(function() {
	
    function write(addr,value) {        
    	if(addr>=0x0600 && addr<0x3F18) {
    		// RAM where the game is loaded
        	BinaryData.write(addr,value);
        	return true;
        }    	
    }
    
    function read(addr) {   
    	    	
    	if(addr===0x117B) {
    		// This is the game's endless-loop after death and such
    		CoCoText.startEndlessLoop();    		
    	}
    	
        if(addr>=0x0600 && addr<0x3F18) {
        	// RAM where the game is loaded
            return BinaryData.read(addr); 
        }        
        
        return undefined;
        
    }
      
    BinaryData.loadDataCacheFromURL("/CoCo/Bedlam/Code.html",function() { 
    	CoCoText.init(read,write,function() {CoCoText.runUntilWaitKey();}, 0x0600);
    	CoCoText.runUntilWaitKey();    	  
    });    
    
});