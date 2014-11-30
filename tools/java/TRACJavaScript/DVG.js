
var x=0;
var y=0;
var globalScale=1;
var origin=0;

var colors = ["#000000","#000000","#000000","#000000",
              "#000000","#000000","#000000","#000000",
              "#000000","#000000","#000000","#000000",
              "#000000","#000000","#000000","#000000"];

function handleDVGCanvas(can) {
	
	var att = can.getAttribute("data-address");	
	if(att!=undefined) {
		setDataCursor(att);
	}
	att = can.getAttribute("data-origin");
	if(att!=undefined) {
		origin = parseInt(att,16);
	}
	att = can.getAttribute("data-colors");	
	if(att!=undefined) {
		colors = JSON.parse(att);		
	}
	
	var command = can.getAttribute("data-command").split(",");
	
	var context = can.getContext("2d");
	context.fillStyle="#000000";
	context.fillRect(0,0,can.width,can.height);
				
	for(var p=0;p<command.length;++p) {		
		command[p] = command[p].trim();
		if(command[p].indexOf("x=")==0) {
			x = parseInt(command[p].substring(2));
		} else if(command[p].indexOf("y=")==0) {
			y = parseInt(command[p].substring(2));
		} else if(command[p].indexOf("globalScale=")==0) {
			globalScale = parseInt(command[p].substring(12));
		} else {
			if(command[p]!="*") {
				setDataCursor(parseInt(command[p],16));
			}
			context.beginPath();
			var callStack = new Array();
			context.moveTo(x,y);
			var nx = 0;
			var ny = 0;
			var c = 0;
			var d = 0;
			var i = 0;
			var s = 0;
			while(true) {
				var a = getNextByte();
				var b = getNextByte();				
				var op = b>>4;
				if(op<10) { // VCTR
					c = getNextByte();
					d = getNextByte();	
					s = 1 << (9-op); // Scale (divisor)
					s=s/globalScale;
					ny = ((b&3)<<8) + a;
					if((b&4)!=0) ny = -ny;
					i = d>>4; // Intensity
					nx = ((d&3)<<8) + c;
					if((d&4)!=0) nx = -nx;
					x = x + (nx / s);
					y = y - (ny / s);
					if(i!=0) {
						context.strokeStyle=colors[i];
						context.lineTo(x,y);
						//alert("LINE TO "+nx+","+ny);
					} else {
						context.moveTo(x,y);
						//alert("MOVE TO "+nx+","+ny);
					}									
				} else if(op==10) { // LABS
					c = getNextByte();
					d = getNextByte();
					// TODO not implemented
				} else if(op==11) { // HALT
					break; // Just stop the sequence
				} else if(op==12) { // JSRL
					callStack.push(lineAddress);
					b = ((b&15)<<8)+a;
					setDataCursor(b*2+origin);
				} else if(op==13) { // RTSL
					if(callStack.length==0) { 
						break;
					}
					setDataCursor(callStack.pop());
				} else if(op==14) { // JMPL
					b = ((b&15)<<8)+a;
					setDataCursor(b*2+origin);				
				} else { // SVEC
					ny = (b&3)<<8;
					if((b&4)!=0) ny=-ny;
					nx = (a&3)<<8;
					if((a&4)!=0) nx=-nx;
					i = a>>4;
					s = ((a>>2)&2) + ((b>>3)&1);
					s = 1 << (7-s); // Now a divisor		
					s=s/globalScale;
					x = x + (nx / s);
					y = y - (ny / s);
					if(i!=0) {
						context.strokeStyle=colors[i];
						context.lineTo(x,y);
						//alert("LINE TO "+nx+","+ny);
					} else {
						context.moveTo(x,y);
						//alert("MOVE TO "+nx+","+ny);
					}					
				}
			}		
			context.closePath();
			context.stroke();
		}		
		
	}

}