
// Cache of the page (for data extraction)
var htmlUpper = "";

window.onload = function() {
	
	htmlUpper = document.body.innerHTML.toUpperCase();
		
	var machine = {		
		mem_read : function(addr) {
			if(addr===0) return 0xC3;
			if(addr===1) return 0xE9;
			if(addr===2) return 0x42;
			
			if(addr===51) { // Print routine
				// Output value in A
				console.log("?");
				return 0xC9;
			}
			
			if(addr>=0x42E9 &&addr<0x5000) {
				return dataCache[addr-dataOrigin];
			}
			
			throw "Unknown memory read "+addr;
		},
		mem_write : function(addr,value) {
			if(addr>=0x42E9 &&addr<0x5000) {
				dataCache[addr-dataOrigin] = value;
				return;
			}
			throw "Unknown memory write "+addr;
		},
		io_read : function(addr) {
			alert("IO Reading "+addr);
		},
		io_write : function(addr,value) {
			alert("IO Writing "+addr+","+value);
		}		
	};
	
	loadDataCache();
	
	var comp = new Z80(machine);
	
	for(var x=0;x<200;++x) {
		comp.run_instruction();
	}
		
}

