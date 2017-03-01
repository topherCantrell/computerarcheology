function startTRS80Pyramid(consoleElement,tapeElement) {
	
	var TRS80Text = makeTRS80Text(consoleElement,tapeElement);
	var BinaryData = makeBinaryDataTRS80Pyramid();
	
	function write(addr,value) {
		// From the loaded game RAM
		if(addr>=0x4300 && addr<0x8000) {
           BinaryData.write(addr,value);
           return true;
        }
		
		return undefined;
	}
	
	function read(addr) { 
		
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
            return BinaryData.read(addr);
        }
		
		return undefined;
	}
	
	function ioread(addr) {
        return undefined;
    }
    
    function iowrite(addr,value) {
        return undefined;
    }
	
	BinaryData.loadDataCacheFromURL("/TRS80/Pyramid/Code.html",function() {		
		TRS80Text.init(
		        read,
		        write,
		        ioread, 
		        iowrite,
		        function() {TRS80Text.runUntilWaitKey();}, 
		        0x4300);
		TRS80Text.runUntilWaitKey();    
	});	
	
};
