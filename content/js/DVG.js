
var x=0;
var y=0;
var baseScale=0;
var origin=0;
var screenScale = 1.0;

var pixColors = ["#101010","#202020","#303030","#404040",
                 "#505050","#606060","#707070","#C0C0C0",
                 "#C8C8C8","#D0D0D0","#D8D8D8","#E0E0E0",
                 "#E8E8E8","#F0F0F0","#F8F8F8","#FFFFFF"];

function handleDVGCanvas(can) {
	
	
	var att = can.getAttribute("data-address");	
	if(att) {
		setDataCursor(att);
	}
	att = can.getAttribute("data-origin");
	if(att) {
		origin = parseInt(att,16);
	}
	att = can.getAttribute("data-colors");	
	if(att) {
		pixColors = JSON.parse(att);		
	}
	
	var command = can.getAttribute("data-command").split(",");
	screenScale = 1.0;  
	
	var context = can.getContext("2d");
	context.fillStyle="#000000";
	context.fillRect(0,0,can.width,can.height);
				
	for(var p=0;p<command.length;++p) {		
		command[p] = command[p].trim();
		if(command[p].indexOf("x=")===0) {
			x = parseInt(command[p].substring(2));
		} else if(command[p].indexOf("y=")===0) {
			y = parseInt(command[p].substring(2));
		} else if(command[p].indexOf("baseScale=")===0) {
			baseScale = parseInt(command[p].substring(10));
		} else if(command[p].indexOf("screenScale=")===0) {
			screenScale = parseFloat(command[p].substring(12));		
		} else {			
			if(command[p]!="*") {
				setDataCursor(parseInt(command[p],16));
			}
			
			context.beginPath();
			
			var callStack = [];
			context.moveTo(x*screenScale,y*screenScale);
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
					
					context.beginPath();
					context.moveTo(x*screenScale,y*screenScale);
					
					c = getNextByte();
					d = getNextByte();	
					s = 1 << (9-(op+baseScale)); // Scale (divisor)
					//s=s/baseScale;
					ny = ((b&3)<<8) + a;
					if((b&4)!==0) ny = -ny;
					i = d>>4; // Intensity
					nx = ((d&3)<<8) + c;
					if((d&4)!==0) nx = -nx;
					x = x + (nx / s);
					y = y - (ny / s);
					if(i!==0) {				
						if(nx===0 && ny===0) {
							context.fillStyle=pixColors[i];
							context.fillRect(x*screenScale,y*screenScale,2,2);
						} else {	
							context.strokeStyle=pixColors[i];
							context.lineTo(x*screenScale,y*screenScale);
							context.stroke();
						}
					} 
					
				} else if(op==10) { // LABS
					c = getNextByte();
					d = getNextByte();
					
					y = 1024 - (((b&15)<<8)+a);
					x = ((d&15)<<8)+c +3; 
					
					context.moveTo(x*screenScale,y*screenScale);
					
					baseScale = (d>>4) & 15;					

				} else if(op==11) { // HALT
					break; // Just stop the sequence
				} else if(op==12) { // JSRL
					callStack.push(cursor);
					b = ((b&15)<<8)+a;
					b = b - origin;
					setDataCursor(b*2+origin);
				} else if(op==13) { // RTSL
					if(callStack.length===0) { 
						break;
					}
					cursor = callStack.pop();
				} else if(op==14) { // JMPL
					b = ((b&15)<<8)+a;
					b = b - origin;
					setDataCursor(b*2+origin);				
				} else { // SVEC
					
					context.beginPath();
					context.moveTo(x*screenScale,y*screenScale);
					
					ny = (b&3)<<8;
					if((b&4)!==0) ny=-ny;
					nx = (a&3)<<8;
					if((a&4)!==0) nx=-nx;
					i = a>>4;
					s = ((a>>2)&2) + ((b>>3)&1);
					s = 1 << (7-(s+baseScale)); // Now a divisor		
					x = x + (nx / s);
					y = y - (ny / s);
					if(i!==0) {
						if(nx===0 && ny===0) {
							context.fillStyle=pixColors[i];
							context.fillRect(x*screenScale,y*screenScale,2,2);
						} else {	
							context.strokeStyle=pixColors[i];
							context.lineTo(x*screenScale,y*screenScale);
							context.stroke();
						}
					} 				
				}
			}		
						
		}				
		
	}

}