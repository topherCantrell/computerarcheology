var Galaga = (function() {
	
	var my = {};

	my.data = null
	my.origin = 0
	
	my.getSprite16x16Data = function(tileAddress) {
		
		var ret = [];
		
		t0 = my.getChar8x8Data(tileAddress*4+0);
		t1 = my.getChar8x8Data(tileAddress*4+1);
		t2 = my.getChar8x8Data(tileAddress*4+2);
		t3 = my.getChar8x8Data(tileAddress*4+3);

		if(tileAddress<0x20) {
			for(var y=4;y<8;++y) {
				for(var x=0;x<8;++x) {
					ret.push(t2[y*8+x]);				
				}		
				for(var x=0;x<8;++x) {
					ret.push(t0[y*8+x]);				
				}
			}
			for(var y=0;y<4;++y) {
				for(var x=0;x<8;++x) {
					ret.push(t2[y*8+x]);				
				}		
				for(var x=0;x<8;++x) {
					ret.push(t0[y*8+x]);				
				}
			}
			for(var y=4;y<8;++y) {
				for(var x=0;x<8;++x) {
					ret.push(t3[y*8+x]);				
				}		
				for(var x=0;x<8;++x) {
					ret.push(t1[y*8+x]);				
				}
			}
			for(var y=0;y<4;++y) {
				for(var x=0;x<8;++x) {
					ret.push(t3[y*8+x]);				
				}		
				for(var x=0;x<8;++x) {
					ret.push(t1[y*8+x]);				
				}
			}
		} else {
			for(var y=0;y<8;++y) {
				for(var x=0;x<8;++x) {
					ret.push(t2[y*8+x]);				
				}		
				for(var x=0;x<8;++x) {
					ret.push(t0[y*8+x]);				
				}
			}			
			for(var y=0;y<8;++y) {
				for(var x=0;x<8;++x) {
					ret.push(t3[y*8+x]);				
				}		
				for(var x=0;x<8;++x) {
					ret.push(t1[y*8+x]);				
				}
			}			
			
		}
		
		return ret;
		
	};
		
	my.getChar8x8Data = function(tileAddress) {
		
		var ret = [];
		
		var data = my.data.slice(tileAddress*16-my.origin,tileAddress*16-my.origin+16);
		
		
		for(var x=0;x<8;++x) {
			var a = data[x].toString(2);
			while(a.length<8) a="0"+a;
			var b = data[x+8].toString(2);
			while(b.length<8) b="0"+b;
			if(tileAddress>=0x80) {
				c = a
				a = b
				b = c
			}
			ret.push(parseInt(""+b.charAt(0)+""+b.charAt(4),2)); 
			ret.push(parseInt(""+b.charAt(1)+""+b.charAt(5),2)); 
			ret.push(parseInt(""+b.charAt(2)+""+b.charAt(6),2)); 
			ret.push(parseInt(""+b.charAt(3)+""+b.charAt(7),2)); 
			ret.push(parseInt(""+a.charAt(0)+""+a.charAt(4),2));
			ret.push(parseInt(""+a.charAt(1)+""+a.charAt(5),2));
			ret.push(parseInt(""+a.charAt(2)+""+a.charAt(6),2));
			ret.push(parseInt(""+a.charAt(3)+""+a.charAt(7),2));			
		}	
		
		return rotateCC(ret,8,8);		
		//return ret
		
	};
		
	function rotateCC(data,width,height) {
    	
    	var ret = [];

		for(var x=0;x<width;++x) {
			for(var y=height-1;y>=0;--y) {			
				ret.push(data[x+y*width]);
    		}
    	}
    	    	    	
    	return ret;
    	
    }
	
	return my;

}());
