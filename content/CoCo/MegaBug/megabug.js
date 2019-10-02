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


function drawMaze() {
	ctx = $('#mazeArea')[0].getContext('2d')
	
	var ox = 5
	var oy = 5	
	ctx.beginPath()	
	for(var y=0;y<16;++y) {
		for(var x=0;x<20;++x) {
			ctx.moveTo(ox+x*16, oy+y*16)
			ctx.lineTo(ox+x*16+16, oy+y*16)
			ctx.moveTo(ox+x*16, oy+y*16)
			ctx.lineTo(ox+x*16, oy+y*16+16)
		}
	}
	ctx.moveTo(ox, oy+16*16)
	ctx.lineTo(ox+20*16, oy+16*16)
	ctx.moveTo(ox+20*16, oy)
	ctx.lineTo(ox+20*16, oy+16*16)
	//ctx.moveTo(ox+x*16, oy+y*16)
	//ctx.lineTo(ox+x*16, oy+y*16+16)
	
	ctx.stroke()
}