// requires Binary.js

var SpaceInvaders = (function() { 
    
    var my = {};

	my.data = null

    my.get8x8Data = function(tile,address) {
    
    	var ret = [];
    	var dat = my.data.slice(address+tile*8,address+tile*8+8);    	
    	for(var x=0;x<8;++x) {
    		var a = dat[x].toString(2);
    		while(a.length<8) a="0"+a;
    		for(var y=7;y>=0;--y) {
    			var ming = a.charAt(y);
    			ret.push(parseInt(ming,2));
    		}		
    	}
    	
    	return rotateCCW(ret,8,8);
    	
    };
    
    my.get8x8CharData = function(tile) {
    	
    	var ret = [];
    	var x;
    	
    	var dat = my.data.slice(0x1E00+tile*8,0x1E00+tile*8+8);
    		
    	for(x=0;x<8;++x) {
    		var a = dat[x].toString(2);
    		while(a.length<8) a="0"+a;
    		for(var y=7;y>=0;--y) {
    			var ming = a.charAt(y);
    			ret.push(parseInt(ming,2));
    		}
    	}
    	
    	return rotateCCW(ret,8,8);
    	
    };
    
    my.get8x3Data = function(tile,address) {
    	var ret =[];
    	
    	var dat = my.data.slice(address+tile*3,address+tile*3+3);
    	    	
    	for(var x=0;x<3;++x) {
    		var a = dat[x].toString(2);
    		while(a.length<8) a="0"+a;
    		for(var y=7;y>=0;--y) {
    			var ming = a.charAt(y);
    			ret.push(parseInt(ming,2));
    		}
    	}
    	
    	return rotateCCW(ret,8,3);
    };
    
   my.get1x8Data = function(tile,address) {
    	
    	var ret = [];
    	
    	var dat = my.data.slice(address+tile,address+tile+1);
    	for(var x=0;x<1;++x) {
    		var a = dat[x].toString(2);
    		while(a.length<8) a="0"+a;
    		for(var y=7;y>=0;--y) {
    			var ming = a.charAt(y);
    			ret.push(parseInt(ming,2));
    		}
    	}
    	
    	return rotateCCW(ret,8,1);
    };
    
    my.get6x8Data = function(tile,address) {
    	
    	var ret = [];
    	
    	var dat = my.data.slice(address+tile,address+tile+6);
    	for(var x=0;x<6;++x) {
    		var a = dat[x].toString(2);
    		while(a.length<8) a="0"+a;
    		for(var y=7;y>=0;--y) {
    			var ming = a.charAt(y);
    			ret.push(parseInt(ming,2));
    		}
    	}
    	
    	return rotateCCW(ret,8,6);
    };
    
    my.get8x16Data = function(tile,address) {
        var ret = [];
    	
        var dat = my.data.slice(address+tile*16,address+tile*16+16);
    	for(var x=0;x<16;++x) {
    		var a = dat[x].toString(2);
    		while(a.length<8) a="0"+a;
    		for(var y=7;y>=0;--y) {
    			var ming = a.charAt(y);
    			ret.push(parseInt(ming,2));
    		}
    	}
    	
    	return rotateCCW(ret,8,16);
    };
    
    my.get8x24Data = function(tile,address) {
        var ret = [];
    	
        var dat = my.data.slice(address+tile*24,address+tile*24+24);
    	for(var x=0;x<24;++x) {
    		var a = dat[x].toString(2);
    		while(a.length<8) a="0"+a;
    		for(var y=7;y>=0;--y) {
    			var ming = a.charAt(y);
    			ret.push(parseInt(ming,2));
    		}
    	}
    	
    	return rotateCCW(ret,8,24);
    };
    
    my.get16x22Data = function(tile,address) {
    	
    	var ret = [];	
    	var dat = [];
    	var x,y;
    	var ming;
    	
    	dat = my.data.slice(address,address+44);    	
    	
    	for(x=0;x<22;++x) {
    		var a = dat[x*2].toString(2);
    		while(a.length<8) a="0"+a;		
    		for(y=7;y>=0;--y) {
    			ming = a.charAt(y);
    			ret.push(parseInt(ming,2));
    		}
    		var b = dat[x*2+1].toString(2);
    		while(b.length<8) b="0"+b;
    		for(y=7;y>=0;--y) {
    			ming = b.charAt(y);
    			ret.push(parseInt(ming,2));			
    		}
    	}
    	
    	return rotateCCW(ret,16,22);
    	
    };
    
    function rotateCCW(data,width,height) {
    	
    	var ret = [];
    	
    	for(var x=width-1;x>=0;--x) {
    		for(var y=0;y<height;++y) {
    			ret.push(data[x+y*width]);
    		}
    	}
    	
    	return ret;
    	
    }
    
    return my;

}());
