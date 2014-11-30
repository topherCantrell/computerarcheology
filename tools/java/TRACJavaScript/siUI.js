
function get8x8Data(tile) {

	var ret = new Array();
	var dat = new Array();
	getLineOfData(address+tile*8,dat);
	for(var x=0;x<8;++x) {
		var a = dat[x].toString(2);
		while(a.length<8) a="0"+a;
		for(var y=7;y>=0;--y) {
			var ming = a.charAt(y);
			ret.push(parseInt(ming,2));
		}		
	}
	
	return rotateCCW(ret,8,8);
	
}


function get8x8CharData(tile) {
	
	var ret = new Array();
	
	setDataCursor(0x1E00);
	for(var x=0;x<tile*8;++x) {
		getNextByte();
	}
	
	var dat = new Array();
	for(var x=0;x<8;++x) {
		dat.push(getNextByte());
	}
		
	for(var x=0;x<8;++x) {
		var a = dat[x].toString(2);
		while(a.length<8) a="0"+a;
		for(var y=7;y>=0;--y) {
			var ming = a.charAt(y);
			ret.push(parseInt(ming,2));
		}
	}
	
	return rotateCCW(ret,8,8);
	
}

function get8x3Data(tile) {
	var ret = new Array();
	
	var dat = new Array();	
	getLineOfData(address+tile*3,dat);
	getLineOfData(address+tile*3+1,dat);
	getLineOfData(address+tile*3+2,dat);
	
	for(var x=0;x<3;++x) {
		var a = dat[x].toString(2);
		while(a.length<8) a="0"+a;
		for(var y=7;y>=0;--y) {
			var ming = a.charAt(y);
			ret.push(parseInt(ming,2));
		}
	}
	
	return rotateCCW(ret,8,3);
}

function get1x8Data(tile) {
	
	var ret = new Array();
	
	var dat = new Array();
	getLineOfData(address+tile,dat);
	for(var x=0;x<1;++x) {
		var a = dat[x].toString(2);
		while(a.length<8) a="0"+a;
		for(var y=7;y>=0;--y) {
			var ming = a.charAt(y);
			ret.push(parseInt(ming,2));
		}
	}
	
	return rotateCCW(ret,8,1);
}

function get6x8Data(tile) {
	
	var ret = new Array();
	
	var dat = new Array();
	getLineOfData(address+tile,dat);
	for(var x=0;x<6;++x) {
		var a = dat[x].toString(2);
		while(a.length<8) a="0"+a;
		for(var y=7;y>=0;--y) {
			var ming = a.charAt(y);
			ret.push(parseInt(ming,2));
		}
	}
	
	return rotateCCW(ret,8,6);
}

function get8x16Data(tile) {
    var ret = new Array();
	
    var dat = new Array();
	getLineOfData(address+tile*16,dat);
	for(var x=0;x<16;++x) {
		var a = dat[x].toString(2);
		while(a.length<8) a="0"+a;
		for(var y=7;y>=0;--y) {
			var ming = a.charAt(y);
			ret.push(parseInt(ming,2));
		}
	}
	
	return rotateCCW(ret,8,16);
}

function get8x24Data(tile) {
    var ret = new Array();
	
    var dat = new Array();
	getLineOfData(address+tile*24,dat);
	for(var x=0;x<24;++x) {
		var a = dat[x].toString(2);
		while(a.length<8) a="0"+a;
		for(var y=7;y>=0;--y) {
			var ming = a.charAt(y);
			ret.push(parseInt(ming,2));
		}
	}
	
	return rotateCCW(ret,8,24);
}

function get16x22Data(tile) {
	
	var ret = new Array();
	
	var dat = new Array();
	getLineOfData(address,dat);
	getLineOfData(address+22,dat);
	
	for(var x=0;x<22;++x) {
		var a = dat[x*2].toString(2);
		while(a.length<8) a="0"+a;		
		for(var y=7;y>=0;--y) {
			var ming = a.charAt(y);
			ret.push(parseInt(ming,2));
		}
		var b = dat[x*2+1].toString(2);
		while(b.length<8) b="0"+b;
		for(var y=7;y>=0;--y) {
			var ming = b.charAt(y);
			ret.push(parseInt(ming,2));			
		}
	}
	
	return rotateCCW(ret,16,22);
	
}

function rotateCCW(data,width,height) {
	
	var ret = new Array();
	
	for(var x=width-1;x>=0;--x) {
		for(var y=0;y<height;++y) {
			ret.push(data[x+y*width]);
		}
	}
	
	return ret;
	
}

