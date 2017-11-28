var Combat = (function() {
	
	var my = {};
	
	my.getPlayfield = function(index, address) {
		
		var addrPF0, addrPF1, addrPF2;
		if(index==0) {
			addrPF0 = 0xF779;
			addrPF1 = 0xF785;
			addrPF2 = 0xF791;
		} else if(index==1) {
			addrPF0 = 0xF779; 
			addrPF1 = 0xF79D;
			addrPF2 = 0xF79D;
		} else if(index==2) {
			addrPF0 = 0xF779; 
			addrPF1 = 0xF7AE;
			addrPF2 = 0xF7BA;
		} else if(index==3) {
			addrPF0 = 0xF79E; 
			addrPF1 = 0xF7A1;
			addrPF2 = 0xF7A1;
		} else {
			addrPF0 = 0xF79E; 
			addrPF1 = 0xF7A2;
			addrPF2 = 0xF7A2;
		}
		
		// Return 20x16
		
		var ret = [];
		
		var data0 = BinaryData.getData(addrPF0,12);
		var data1 = BinaryData.getData(addrPF1,12);
		var data2 = BinaryData.getData(addrPF2,12);
		
		for (var x=0;x<12;++x) {
			var a = data0[x].toString(2);
    		while(a.length<8) a="0"+a;
    		var b = data1[x].toString(2);
    		while(b.length<8) b="0"+b;
    		var c = data2[x].toString(2);
    		while(c.length<8) c="0"+c;
    		
    		for(var y=3;y>=0;--y) {    			
    			// Only upper 4 bits in PF0
    			ret.push(parseInt(a.charAt(y)));    			
    		}    		
    		for(y=0;y<8;++y) {
    			ret.push(parseInt(b.charAt(y)));
    		}
    		for(y=7;y>=0;--y) {
    			ret.push(parseInt(c.charAt(y)));
    		}
			
		}
		
		// TODO mirroring
		
		return ret;
		
	}
	
	return my;
	
}());