function startHauntedHouse() {
	
	var TRS80Text = makeTRS80Text();
	var BinaryData = makeBinaryDataHauntedHouse();
	
    document.getElementById("floorOne").onclick = function() {
		BinaryData.loadDataCacheFromURL("/TRS80/HauntedHouse/Code1.html",function() {
			floor=1;
			TRS80Text.changeResetVector(0x42E9);
			TRS80Text.reset();
			TRS80Text.runUntilWaitKey();  
		});
	};
	
	document.getElementById("floorTwo").onclick = function() {	
		BinaryData.loadDataCacheFromURL("/TRS80/HauntedHouse/Code2.html",function() {
			floor=2;
			TRS80Text.changeResetVector(0x435E);
			TRS80Text.reset();
			TRS80Text.runUntilWaitKey();  
		});
	};
	
	var floor=1;
	
	function write(addr,value) {
		// From the loaded game RAM
		if(addr>=0x42E9 &&addr<0x5000) {
			BinaryData.write(addr,value);
			return true;
		}
		
		return undefined;
	}
	
	function read(addr) { 
		
		// Endless loops in code
		if(floor===1 && addr===0x4A48) {
			TRS80Text.startEndlessLoop(); 
			return 0;					
		}
		if(floor===2 && addr===0x4A97) {
			TRS80Text.startEndlessLoop(); 
			return 0;					
		}
		
		// We hijacked the input spin-loop. We need
        // to simulate the random number counter.
		if(addr===0x467E && floor===1) {
		    return Math.floor(Math.random()*256);
		}
		if(addr===0x4683 && floor===2) {
		    return Math.floor(Math.random()*256);
        }
						
		// Tape operation (loading 2nd floor)
        if(addr===0x0293) {
            BinaryData.loadDataCacheFromURL("/TRS80/HauntedHouse/Code2.html",function() {
                floor = 2;
                TRS80Text.changeResetVector(0x435E);
                TRS80Text.reset();
                TRS80Text.runUntilWaitKey();  
            });
            TRS80Text.pause();
            return 0;
        }               
		
		// From the loaded game RAM
		if(addr>=0x42E9 &&addr<0x5000) {
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
	
	BinaryData.loadDataCacheFromURL("/TRS80/HauntedHouse/Code1.html",function() {		
		TRS80Text.init(
		        read,
		        write,
		        function() {return undefined;}, 
                function() {return undefined;},
		        function() {TRS80Text.runUntilWaitKey();}, 
		        0x42E9);
		TRS80Text.runUntilWaitKey();    
	});	
	
};
