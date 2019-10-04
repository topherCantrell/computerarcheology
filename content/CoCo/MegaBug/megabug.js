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

var COLORS = [
	'#FFFFFF',
	'#FF80FF',
	'#80FFFF'
]

var LOOPWALLCOLOR = '#00FFFF'

function drawMaze() {
	
	//  cccccccc_oooooooo_RBrb
	
	// b = bottom
	// r = right
	// B = bottomLoop
	// R = rightLoop
	// o = onList number (0 for not on list)
	// c = background color

	can = $('#mazeArea')[0]
	ctx = can.getContext('2d')	
	ctx.clearRect(0, 0, can.width, can.height);
	
	var org_style = ctx.strokeStyle
	
	var ox = 5
	var oy = 5	
		
	for(var y=0;y<16;++y) {
		for(var x=0;x<20;++x) {
			ctx.strokeStyle = org_style
			var d = lineDefs[y*20+x]			
			var bot = d&1
			var right = d&2
			var loopRight = d&4
			var loopBottom = d&8
			var onList = (d>>4) & 0xFF
			var col = (d>>12) & 0xFF
			ctx.fillStyle = COLORS[col]
			ctx.fillRect(ox+x*16,oy+y*16,16,16)
			if(onList>0) {
				ctx.fillStyle = 'black'
				ctx.font = "8px Arial"
				if(onList>9) {
					ctx.fillText(""+onList,ox+x*16+4,oy+y*16+10)
				} else {
					ctx.fillText(""+onList,ox+x*16+6,oy+y*16+10)
				}
			}
			if(loopBottom) {
				ctx.beginPath()
				ctx.strokeStyle = LOOPWALLCOLOR
				ctx.moveTo(ox+x*16, oy+y*16+16)
				ctx.lineTo(ox+x*16+16, oy+y*16+16)
				ctx.stroke()
			}
			if(bot) { // bottom
				ctx.beginPath()
				ctx.strokeStyle = org_style
				ctx.moveTo(ox+x*16, oy+y*16+16)
				ctx.lineTo(ox+x*16+16, oy+y*16+16)
				ctx.stroke()
			}
			if(loopRight) {
				ctx.beginPath()
				ctx.strokeStyle = LOOPWALLCOLOR			 
				ctx.moveTo(ox+x*16+16, oy+y*16)
				ctx.lineTo(ox+x*16+16, oy+y*16+16)
				ctx.stroke()
			}			
			if(right) { // right
				ctx.beginPath()
				ctx.strokeStyle = org_style
				ctx.moveTo(ox+x*16+16, oy+y*16)
				ctx.lineTo(ox+x*16+16, oy+y*16+16)
				ctx.stroke()
			}
		}
	}
	ctx.beginPath()
	ctx.strokeStyle = org_style
	ctx.moveTo(ox, oy)
	ctx.lineTo(ox+20*16, oy)
	ctx.moveTo(ox, oy)
	ctx.lineTo(ox, oy+16*16)	
	ctx.stroke()
}

var binData = makeBinaryDataMegabug();

var state = "uninitialized"
var CPU6809
	
function initMazeGen() {
	
	numRun = 0
	runColor = 1
	
	for(var x=0;x<20*16;++x) {
		lineDefs[x] = 3
	}
		
	var x
	var ram1 = Array(0x4000)
	for(x=0;x<0x4000;++x) {
		ram1[x] = 0
	}
	
	var looping = parseInt($('#loopiness').val())
	ram1[0xC0] = looping
		
	// Initialize the 6809 CPU.
	CPU6809 = make6809()
	CPU6809.init(write,read,function(){})	
	CPU6809.set('sp',0x1FFF)
	CPU6809.set('dp',0)
	
	state = "initialized"
							
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
			state = "done"
			return 0x12
		}
		
		if(addr>=0xA000 && addr<0xC000) {
			return Math.floor(Math.random()*256)
		}
		
		if(addr<0x4000) {
			return ram1[addr]
		}
		
		if(addr==0xDD4F) {
			console.log('Next Run '+numRun)
			++numRun
		}
		
		if(addr==0xDD93) {
			// A = Y, B = X
			var y = CPU6809.status()['a']
			var x = CPU6809.status()['b']
			console.log('Clearing cell bottom '+x+','+y)	
			lineDefs[y*20+x] = (lineDefs[y*20+x] & 0xFFFFE) | (runColor<<12)
			state = "graphics"
			return 0x39 // RTS
		}
		
		if(addr==0xDDAD) {
			// A = Y, B = X
			var y = CPU6809.status()['a']
			var x = CPU6809.status()['b']
			console.log('Clearing cell left '+x+','+y)
			lineDefs[y*20+x] = (lineDefs[y*20+x] & 0xFFFFD) | (runColor<<12)
			state = "graphics"
			return 0x39 // RTS
		}
						
		// Specific ROM addresses for graphics
		
		if(addr<0xE000 && addr>=0xC000) {
			return binData.read(addr)
		}
		
		throw "Read of "+addr+" from "+CPU6809.status()['pc'];
	}		
}

function stepMazeGen() {
	if(state=="done" || state=="uninitialized") {
		// If we need to start over
		initMazeGen()
	}
	state = "running"
	while(state=="running" || state=="graphics") {
		if(state=="graphics") {
			drawMaze()
			setTimeout(stepMazeGen,50)
			return
		}
		// Until SOMETHING happens
		CPU6809.steps(100)
	}
	drawMaze()
}

function runMazeGen() {
	
	initMazeGen()
	while(state!="done") {
		CPU6809.steps(100)
	}
	drawMaze()	
    
}
