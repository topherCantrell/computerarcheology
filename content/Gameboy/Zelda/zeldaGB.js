var ZeldaGB = (function() { 
    
    var my = {};

	my.data = null
	my.origin = 0

    function mergePixels(data) {
    	var ret = [];
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
    
    my.getGBTile = function(tile,address) {
    	
    	var dat = my.data.slice(address+tile*16-my.origin,address+tile*16-my.origin+16);
    	
    	return mergePixels(dat);
    	
    };
    
    return my;

}());