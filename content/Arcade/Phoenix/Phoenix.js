
var Phoenix = (function() {
	
	var my = {};

	my.data = null
	my.origin = 0
			
    function rotateCCW(data,width,height) {
    	
    	var ret = [];
    	
    	for(var x=width-1;x>=0;--x) {
    		for(var y=0;y<height;++y) {
    			ret.push(data[x+y*width]);
    		}
    	}
    	
    	return ret;
    	
    }

    function flipHorizontal(data,width,height) {
        var ret = []
        for(var y=0;y<height;++y) {
            for(var x=width-1;x>=0;--x) {
                ret.push(data[x+y*width])
            }

        }
        return ret
    }

	my.getBackground8x8Data = function(tileAddress) {
		
		var ret = []
		
		var dataB = my.data.slice(tileAddress*8-my.origin,tileAddress*8-my.origin+8)
		var dataA = my.data.slice(tileAddress*8+2048-my.origin,tileAddress*8+2048-my.origin+8);
		
		for(var x=0;x<8;++x) {
			var a = dataA[x].toString(2)
			while(a.length<8) a="0"+a
			var b = dataB[x].toString(2)
			while(b.length<8) b="0"+b
			ret.push(parseInt(""+a.charAt(0)+""+b.charAt(0),2))
			ret.push(parseInt(""+a.charAt(1)+""+b.charAt(1),2))
			ret.push(parseInt(""+a.charAt(2)+""+b.charAt(2),2))
			ret.push(parseInt(""+a.charAt(3)+""+b.charAt(3),2))
			ret.push(parseInt(""+a.charAt(4)+""+b.charAt(4),2)) 
			ret.push(parseInt(""+a.charAt(5)+""+b.charAt(5),2)) 
			ret.push(parseInt(""+a.charAt(6)+""+b.charAt(6),2)) 
			ret.push(parseInt(""+a.charAt(7)+""+b.charAt(7),2));
		}	
		
		ret = rotateCCW(ret,8,8)
        ret = flipHorizontal(ret,8,8)

        return ret
		
	}
	
	return my

}())
