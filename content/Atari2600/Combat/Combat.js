var Combat = (function() {
	
	var my = {};
	
	my.getPlayfield = function(index) {
		
		//var addrPF0, addrPF1, addrPF2;
		//if(index==0) {
			addrPF0 = 0xF775;
			addrPF1 = 0xF781;
			addrPF2 = 0xF78D;
		//}
		
		// Return 20x16
		
		var ret = [];
		
		var data0 = BinaryData.getData(addrPF0,16);
		var data1 = BinaryData.getData(addrPF1,16);
		var data2 = BinaryData.getData(addrPF2,16);
		
		for (var x=0;x<16;++x) {
			var a = data0[x].toString(2);
    		while(a.length<8) a="0"+a;
    		var b = data1[x].toString(2);
    		while(b.length<8) b="0"+b;
    		var c = data2[x].toString(2);
    		while(c.length<8) c="0"+c;
    		
    		for(var y=4;y<8;++y) {    			
    			// Only 4 bits in PF0
    			ret.push(parseInt(a.charAt(y)));    			
    		}    		
    		for(y=0;y<8;++y) {
    			ret.push(parseInt(b.charAt(y)));
    		}
    		for(y=0;y<8;++y) {
    			ret.push(parseInt(c.charAt(y)));
    		}
			
		}
		
		// TODO mirroring
		
		return ret;
		
	}
	
	return my;
	
}());