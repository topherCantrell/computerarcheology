var Stella = (function() { 
    
    var my = {};

	my.data = null
	my.origin = 0

    my.get8x5Data = function(tile,address) {
    
    	var ret = [];
    	
    	var dat = my.data.slice(address+tile*5-my.origin,address+tile*5-my.origin+5);  
    	for(var x=0;x<5;++x) {
    		var a = dat[x].toString(2);
    		while(a.length<8) a="0"+a;
    		for(var y=0;y<8;++y) {
    			var ming = a.charAt(y);
    			ret.push(parseInt(ming,2));
    		}		
    	}
    	
    	return ret;
    	
    };
    
    my.get8x8Data = function(tile,address) {
        
    	var ret = [];
    	
    	var dat = my.data.slice(address+tile*8-my.origin,address+tile*8-my.origin+8);  
    	for(var x=0;x<8;++x) {
    		var a = dat[x].toString(2);
    		while(a.length<8) a="0"+a;
    		for(var y=0;y<8;++y) {
    			var ming = a.charAt(y);
    			ret.push(parseInt(ming,2));
    		}		
    	}
    	
    	return ret;
    	
    };
    
    return my;

}());
