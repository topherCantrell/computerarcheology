
$(function() {
	
    function write(addr,value) {        
    	if(addr<0x0600 || addr>0x3F20) {
        	// Oops! Not in our address space
            throw "Unhandled write "+addr;
        }
    	// RAM where the game is loaded
    	BinaryData.write(addr,value);
    }
    
    function read(addr) {   
    	
        if(addr<0x0600 || addr>0x3F20) {
        	// Oops! Not in our address space
            throw "Unhandled read "+addr;
        }        
        
        if(addr===0x0F1B) {
    		// This is the game's endless-loop after death and such
    		CoCoText.startEndlessLoop();    		
    	}
        
        // RAM where the game is loaded
        return BinaryData.read(addr); 
    }
      
    BinaryData.loadDataCacheFromURL("/CoCo/Pyramid/Code.html",function() { 
    	var console = $("#cocoConsole");
    	CoCoText.init(read,write,function() {CoCoText.runUntilWaitKey();}, 0x0600,console);
    	CoCoText.runUntilWaitKey();    	  
    });    
    
});