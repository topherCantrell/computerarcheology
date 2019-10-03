// requires BinaryData

var Megabug = (function() {
	
	var my = {}
	
	function padBinaryTo8Bits(value) {
    	var ret = value.toString(2);
    	while(ret.length<8) ret="0"+ret;
    	return ret;
    }
	
	my.getPlayer = function(number, address) {
		var dat = BinaryData.getData(address+number*6,6)
		
		ret = []
		for(var y=0;y<6;++y) {
			var b = padBinaryTo8Bits(dat[y])
			for(var x=0;x<8;++x) {
				ret.push(parseInt(b.substring(x,x+1),2))
			}
		}
				
		return ret
		
	}
	
	my.getCharacter = function(number, address) {
		
		var dat = BinaryData.getData(address+number*9,9)
		
		ret = []
		for(var y=0;y<9;++y) {
			var b = padBinaryTo8Bits(dat[y])
			for(var x=0;x<8;++x) {
				ret.push(parseInt(b.substring(x,x+1),2))
			}
		}
				
		return ret
	}
	
	my.getSmallBug = function(number, address) {
		
		var dat = BinaryData.getData(address+number*18,18)
		
		ret = []
		
		for(var y=0;y<6;++y) {
			for(var x=0;x<3;++x) {			
				var b = padBinaryTo8Bits(dat[x*6+y])
				for(p=0;p<4;++p) {
					var s = b.substring(p*2,p*2+2)
					ret.push(parseInt(s,2))
				}
			}
		}
		
		return ret
		
	};
			
	my.getGraphicsLargeBug = function(bugAddress) {	
		
		var dat = BinaryData.getData(bugAddress,5*32)
		
		var ret = []
		
		for(var y=0;y<32;++y) {	
			for(var x=0;x<5;++x) {
				var v = dat[x*32+y]
				ret.push((v>>6)&3)
				ret.push((v>>4)&3)
				ret.push((v>>2)&3)
				ret.push(v & 3)
			}
		}
						
		return ret
		
	};
			
	return my

}());


var lineDefs = Array(20*16)
for(var x=0;x<20*16;++x) {
	lineDefs[x] = 3
}

function drawMaze() {
	
	// 1=bottom
	// 2=right
	ctx = $('#mazeArea')[0].getContext('2d')
	
	var ox = 5
	var oy = 5	
	ctx.beginPath()	
	for(var y=0;y<16;++y) {
		for(var x=0;x<20;++x) {
			var d = lineDefs[y*20+x]
			if(d&1) { // bottom
				ctx.moveTo(ox+x*16, oy+y*16+16)
				ctx.lineTo(ox+x*16+16, oy+y*16+16)
			}
			if(d&2) { // right
				ctx.moveTo(ox+x*16+16, oy+y*16)
				ctx.lineTo(ox+x*16+16, oy+y*16+16)
			}
		}
	}
	ctx.moveTo(ox, oy)
	ctx.lineTo(ox+20*16, oy)
	ctx.moveTo(ox, oy)
	ctx.lineTo(ox, oy+16*16)	
	
	ctx.stroke()
}

var binData = makeBinaryDataMegabug();

function runMazeGen() {
	
	console.log('Starting')
	var x
	var ram1 = Array(0x4000)
	for(x=0;x<0x4000;++x) {
		ram1[x] = 0
	}
	
	var looping = parseInt($('#loopiness').val())
	ram1[0xC0] = looping
		
	// Initialize the 6809 CPU.
	var CPU6809 = make6809()
	CPU6809.init(write,read,function(){})	
	CPU6809.set('sp',0x1FFF)
	CPU6809.set('dp',0)
	
	var running = true
	while(running) {
		CPU6809.steps(100)
	}
	
	console.log('Done')
	
	drawMaze()
					
	function write(addr,value) {
		if(addr<0x4000) {
			ram1[addr] = value
		}
        
        else {		
        	throw "Write to "+addr+" from "+CPU6809.status()['pc'];
        }		
	}
			
	function read(addr) {	
						
		if(addr==0xFFFE) {
			return 0xDC
		} else if(addr==0xFFFF) {
			return 0x94
		}
		
		if(addr==0xDDCB) {
			running=false
			return 0x12
		}
		
		if(addr>=0xA000 && addr<0xC000) {
			return Math.floor(Math.random()*256)
		}
		
		if(addr<0x4000) {
			return ram1[addr]
		}
		
		if(addr==0xDD93) {
			// A = Y, B = X
			var y = CPU6809.status()['a']
			var x = CPU6809.status()['b']
			console.log('Clearing cell bottom '+x+','+y)	
			lineDefs[y*20+x] = lineDefs[y*20+x] & 0xFE
			//drawMaze()
			return 0x39 // RTS
		}
		
		if(addr==0xDDAD) {
			// A = Y, B = X
			var y = CPU6809.status()['a']
			var x = CPU6809.status()['b']
			console.log('Clearing cell left '+x+','+y)
			lineDefs[y*20+x] = lineDefs[y*20+x] & 0xFD
			//drawMaze()
			return 0x39 // RTS
		}
						
		// TODO specific ROM addresses for graphics
		
		if(addr<0xE000 && addr>=0xC000) {
			return binData.read(addr)
		}
		
		throw "Read of "+addr+" from "+CPU6809.status()['pc'];
	}		
    
}
