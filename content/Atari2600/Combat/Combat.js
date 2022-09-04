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
			// In case we want to show the larger clouds
			addrPF0 = 0xF79E; 
			addrPF1 = 0xF7A2;
			addrPF2 = 0xF7A2;
		}
		
		// Return 20x12
		
		var ret = [];
		
		var data0 = Stella.data.slice(addrPF0-Stella.origin,addrPF0-Stella.origin+12);
		var data1 = Stella.data.slice(addrPF1-Stella.origin,addrPF1-Stella.origin+12);
		var data2 = Stella.data.slice(addrPF2-Stella.origin,addrPF2-Stella.origin+12);
		
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
		
		return ret;
		
	}
	
    my.getPlayfieldPAL = function(index, address) {
		
		var addrPF0, addrPF1, addrPF2;
		if(index==0) {
			addrPF0 = 0xF76F;
			addrPF1 = 0xF77E;
			addrPF2 = 0xF78D;
		} else if(index==1) {
			addrPF0 = 0xF76F; 
			addrPF1 = 0xF79C;
			addrPF2 = 0xF79C;
		} else if(index==2) {
			addrPF0 = 0xF76F; 
			addrPF1 = 0xF7B0;
			addrPF2 = 0xF7BF;
		} else if(index==3) {
			addrPF0 = 0xF79D; 
			addrPF1 = 0xF7A0;
			addrPF2 = 0xF7A0;
		} 
		
		// Return 20x15
		
		var ret = [];
		
		var data0 = Stella.data.slice(addrPF0-Stella.origin,addrPF0-Stella.origin+15);
		var data1 = Stella.data.slice(addrPF1-Stella.origin,addrPF1-Stella.origin+15);
		var data2 = Stella.data.slice(addrPF2-Stella.origin,addrPF2-Stella.origin+15);
		
		for (var x=0;x<15;++x) {
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
		
		return ret;
		
	}
	
	return my;
	
}());
