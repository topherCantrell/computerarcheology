// requires BinaryData

var Megabug = (function() {
	
	var my = {}
			
	my.getGraphicsLargeBug = function(bugAddress) {	
		
		var dat = BinaryData.getData(bugAddress,5*32)
		
		var ret = []
		
		for(var y=0;y<32;++y) {	
			for(var x=0;x<5;++x) {
				var v = dat[x*32+y]
				ret.push((v>>6)&3)
				ret.push((v>>4)&3)
				ret.push((v>>2)&3)
				ret.push(v & 3)
			}
		}
						
		return ret
		
	};
			
	return my

}());
