var MoonPatrol = (function() {
	
	var my = {};

	my.data = null
	my.origin = 0
	
	function getSpriteQuadrantData(tileAddress) {
		
		var ret = [];
		
		var plane1 = my.data.slice(tileAddress-my.origin,tileAddress-my.origin+8); 
		var plane2 = my.data.slice(tileAddress-my.origin+0x1000,tileAddress-my.origin+0x1000+8);
		
		for(var x=0;x<8;++x) {
			var a = plane1[x].toString(2);
			while(a.length<8) a="0"+a;
			var b = plane2[x].toString(2);
			while(b.length<8) b="0"+b;		
			for(var y=0;y<8;++y) {
				var ming = a.charAt(y)+""+b.charAt(y);
				ret.push(parseInt(ming,2));
			}		
		}
		
		return ret;
	}
	
	my.getSprite16x16Data = function(tileAddress) {	
		
		var ret = [];
		var x,y;
		
		var a = getSpriteQuadrantData(tileAddress*32);
		var b = getSpriteQuadrantData(tileAddress*32+8);
		var c = getSpriteQuadrantData(tileAddress*32+16);
		var d = getSpriteQuadrantData(tileAddress*32+24);
		
		var cnta=0;
		var cntb=0;
		for(y=0;y<8;++y) {
			for(x=0;x<8;++x) {
				ret.push(a[cnta++]);
			}
			for(x=0;x<8;++x) {
				ret.push(c[cntb++]);
			}		
		}
		
		cnta=0;
		cntb=0;
		for(y=0;y<8;++y) {
			for(x=0;x<8;++x) {
				ret.push(b[cnta++]);
			}
			for(x=0;x<8;++x) {
				ret.push(d[cntb++]);
			}		
		}
		
		return ret;
		
	};
	
	my.getBackground8x8Data = function(tileAddress) {
		
		var ret = [];
		
		var dataA = my.data.slice(tileAddress*8-my.origin,tileAddress*8-my.origin+8);
		var dataB = my.data.slice(tileAddress*8+4096-my.origin,tileAddress*8+4096-my.origin+8);	
		
		for(var x=0;x<8;++x) {
			var a = dataA[x].toString(2);
			while(a.length<8) a="0"+a;
			var b = dataB[x].toString(2);
			while(b.length<8) b="0"+b;
			ret.push(parseInt(""+a.charAt(0)+""+b.charAt(0),2));
			ret.push(parseInt(""+a.charAt(1)+""+b.charAt(1),2));
			ret.push(parseInt(""+a.charAt(2)+""+b.charAt(2),2));
			ret.push(parseInt(""+a.charAt(3)+""+b.charAt(3),2));
			ret.push(parseInt(""+a.charAt(4)+""+b.charAt(4),2)); 
			ret.push(parseInt(""+a.charAt(5)+""+b.charAt(5),2)); 
			ret.push(parseInt(""+a.charAt(6)+""+b.charAt(6),2)); 
			ret.push(parseInt(""+a.charAt(7)+""+b.charAt(7),2)); 
		}	
		
		return ret;
		
	};
	
	my.getBackgroundImage = function() {
		
		var data = my.data.slice(0-my.origin,0-my.origin+4096);
		var ret = [];
		for(var x=0;x<4096;++x) {
			var a = data[x].toString(2);
			while(a.length<8) a="0"+a;
			ret.push(parseInt(""+a.charAt(4)+""+a.charAt(0),2));
			ret.push(parseInt(""+a.charAt(5)+""+a.charAt(1),2));
			ret.push(parseInt(""+a.charAt(6)+""+a.charAt(2),2));
			ret.push(parseInt(""+a.charAt(7)+""+a.charAt(3),2));          	       
		}     
	
		return ret;
	
	};
	
	return my;

}());
