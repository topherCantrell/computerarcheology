var Downland = (function() { 
    
    var my = {};
        
    function padBinaryTo8Bits(value) {
    	var ret = value.toString(2);
    	while(ret.length<8) ret="0"+ret;
    	return ret;
    }
    
    my.get8x7 = function(tile,address) {
    	var ret = [];
    	var dat = BinaryData.getData(address+tile*7,7);
    	
    	for(var y=0;y<7;++y) {
    		var comb = padBinaryTo8Bits(dat[y]);
    		for(var x=0;x<8;++x) {
    			ret.push(parseInt(comb.substring(x,x+1),2));
    		}
    	}
    	return ret;
    };
            
    return my;

}());