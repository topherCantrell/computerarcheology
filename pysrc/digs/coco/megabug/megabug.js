
var CPU6809 = make6809()

function runMegaBug() {
    
    var resetVector = 0xC000
    
    rom = makeBinaryDataPyramid()
    ram = []
    for(var x=0;x<0x4000;++x) {
    	ram.push(0)
    }
	
	function write(addr,value) {
		
		if(addr>=0 && addr<ram.length) {
			ram[addr] = value
			return true
		}
		
		if(addr>=0xFF00 && addr<0xFF60) {
			return true
		}
		
		console.log('WRITE ADDRESS '+addr.toString(16)+' VALUE '+value.toString(16))        
		
		console.log(CPU6809.status())
        throw 'OOPS'
    }
    
    function read(addr) {       	
    	// 6809 reset vector (point to game code at 0600)
        if(addr===0xFFFE) return resetVector>>8
        if(addr===0xFFFF) return resetVector&0xFF
        
        if(addr>=0xC000 && addr<0xE000) return rom.read(addr)
        
        if(addr>=0 && addr<ram.length) return ram[addr]
        
        if(addr>=0xFF00 && addr<0xFF60) {
			return 0xFF
		}
        
    	console.log('UNKNOWN READ ADDRESS '+addr.toString(16))
    	console.log(CPU6809.status())
    	throw 'OOPS'
                
    }
    
    CPU6809.init(write,read,function(){})
    
    for(var steps=0;steps<100;++steps) {       
        CPU6809.steps(1)
    }
            
};