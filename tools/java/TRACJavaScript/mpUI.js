
function getSprite16x16Data(tileAddress) {	
	
	var ret = new Array();
	
	var a = getSpriteQuadrantData(tileAddress*32);
	var b = getSpriteQuadrantData(tileAddress*32+8);
	var c = getSpriteQuadrantData(tileAddress*32+16);
	var d = getSpriteQuadrantData(tileAddress*32+24);
	
	var cnta=0;
	var cntb=0;
	for(var y=0;y<8;++y) {
		for(var x=0;x<8;++x) {
			ret.push(a[cnta++])
		}
		for(var x=0;x<8;++x) {
			ret.push(c[cntb++])
		}		
	}
	
	cnta=0;
	cntb=0;
	for(var y=0;y<8;++y) {
		for(var x=0;x<8;++x) {
			ret.push(b[cnta++])
		}
		for(var x=0;x<8;++x) {
			ret.push(d[cntb++])
		}		
	}
	
	return ret;
	
}

function getSpriteQuadrantData(tileAddress) {
	
	var ret = new Array();
	
	var plane1 = new Array(); 
	getLineOfData(tileAddress,plane1);
	var plane2 = new Array();
	getLineOfData(tileAddress+0x1000,plane2);
	
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

function getBackground8x8Data(tileAddress) {
	
	var ret = new Array();
	
	var dataA = new Array();
	getLineOfData(tileAddress*8,dataA);
	var dataB = new Array();
	getLineOfData(tileAddress*8+4096,dataB);	
	
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
	
}

function getBackgroundImage(tileAddress) {
	
	// There is just one giant tile image. Ignore
	// the tileAddressed passed in.

	var data = new Array();
	var j = 0;
	
	while(j<htmlUpper.length) {
		
		var k=htmlUpper.indexOf("\n",j);
		if(k<0) k=htmlUpper.length;
		var text = htmlUpper.substring(j,k);
		j = k+1;

		if(text.length<5) continue;
		if(text.charAt(4)!=':') continue;

		for(var x=6;x<text.length;x=x+3) {
			data.push(parseInt(text.substring(x,x+2),16));
		}

	}	

	var ret = new Array();
	for(var x=0;x<4096;++x) {
		var a = data[x].toString(2);
		while(a.length<8) a="0"+a;
		ret.push(parseInt(""+a.charAt(4)+""+a.charAt(0),2));
		ret.push(parseInt(""+a.charAt(5)+""+a.charAt(1),2));
		ret.push(parseInt(""+a.charAt(6)+""+a.charAt(2),2));
		ret.push(parseInt(""+a.charAt(7)+""+a.charAt(3),2));          	       
	}     

	return ret;

}

