
function mergePixels(data) {
	var ret = new Array();
	for(var x=0;x<16;x=x+2) {
		var a = data[x].toString(2);
		while(a.length<8) a="0"+a;
		var b = data[x+1].toString(2);
		while(b.length<8) b="0"+b;		
		for(var y=0;y<8;++y) {
			var ming = b.charAt(y)+""+a.charAt(y);
			ret.push(parseInt(ming,2));
		}
	}
	return ret;
}

function getGBTile(tile) {
	
	var dat = getData(address+tile*16,16);
	
	return mergePixels(dat);
	
}