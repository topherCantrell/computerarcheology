// requires BinaryData.js

var Stella = (function() { 
    
    var my = {};

    my.get8x5Data = function(tile,address) {
    
    	var ret = [];
    	
    	var dat = BinaryData.getData(address+tile*5,5);  
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
    	
    	var dat = BinaryData.getData(address+tile*8,8);  
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
