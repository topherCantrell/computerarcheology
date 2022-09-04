var Daggorath = (function() { 
    
    var my = {};

	var data = null
	var origin = 0
    
    var x = 0;
    var y = 0;
    var scale = 1.0;
    var xoffs = 0;
    var yoffs = 0;
    var colors = ["#000000","#FFFFFF"];
    
    var startSegment = true;

    function padBinaryTo8Bits(value) {
    	var ret = value.toString(2);
    	while(ret.length<8) ret="0"+ret;
    	return ret;
    }
    
    my.get5x7Packed = function(tile,address) {
    	
    	var ret = [];
    	
    	var dat = my.data.slice(address+tile*5-my.origin,address+tile*5-my.origin+5);
    	
    	//getLineOfData(address+tile*5,dat);
    	
    	var comb = padBinaryTo8Bits(dat[0])+padBinaryTo8Bits(dat[1])+padBinaryTo8Bits(dat[2])+padBinaryTo8Bits(dat[3])+padBinaryTo8Bits(dat[4]);
    	comb = comb.substring(5);
    	
    	for(var x=0;x<7;++x) {
    		for(var y=0;y<5;++y) {
    			ret.push(parseInt(comb.substring(y,y+1),2));
    		}
    		comb = comb.substring(5);
    	}
    	return ret;
    };
    
    my.get8x7 = function(tile,address) {
    	var ret = [];
    	var dat = my.data.slice(address+tile*7-my.origin,address+tile*7-my.origin+7);
    	
    	for(var y=0;y<7;++y) {
    		var comb = padBinaryTo8Bits(dat[y]);
    		for(var x=0;x<8;++x) {
    			ret.push(parseInt(comb.substring(x,x+1),2));
    		}
    	}
    	return ret;
    };
    
    function processScript(context,pc) {
    	var cursor = pc;
    	startSegment = true;
    	
    	var com,nx,ny;
    	while(true) {
    		
    		com = my.data[cursor - my.origin];cursor=cursor+1
    		switch(com) {
    		case 0xFA: // Return from graphics subroutine			
    			return;
    		case 0xFB: // Jump to graphics subroutine
    			var tpa = cursor;
    			nx = my.data[cursor - my.origin];cursor=cursor+1
    			ny = my.data[cursor - my.origin];cursor=cursor+1
    			processScript(context,nx<<8 | ny);
    			cursor = tpa;
    			break;
    		case 0xFC: // Multiple short segments
    			while(true) {
    				com = my.data[cursor - my.origin];cursor=cursor+1
    				if(com===0) break;
    				ny = com >> 4;
    				if(ny>=8) ny=ny | 0xF0;
    				ny = ny << 1;
    				ny = ny & 0xFF;
    				nx = com & 0x0F;
    				if(nx>=8) nx=nx | 0xF0;
    				nx = nx << 1;
    				nx = nx & 0xFF;
    				if(nx>127) nx=nx-256;
    				if(ny>127) ny=ny-256;
    				nx = nx*scale + x;
    				ny = ny*scale + y;
    				context.lineTo(xoffs+nx,yoffs+ny);
    				x = nx;
    				y = ny;
    			}
    			startSegment = true;
    			break;
    		case 0xFD: // Jump to XXXX
    			startSegment = true;
    			nx = my.data[cursor - my.origin];cursor=cursor+1
    			ny = my.data[cursor - my.origin];cursor=cursor+1
    			cursor = nx<<8 | ny;
    			break;
    		case 0xFE: // Exit
    			return;
    		case 0xFF: // Start a new segment
    			startSegment = true;
    			break;
    		default: // Regular line
    			if(startSegment) {
    				y = com*scale;
    				x = my.data[cursor - my.origin]*scale;cursor=cursor+1
    				context.moveTo(xoffs+x,yoffs+y);
    				startSegment = false;				
    			} else {
    				nx = my.data[cursor - my.origin];cursor=cursor+1
    				context.lineTo(xoffs+nx*scale,yoffs+com*scale);
    				y = com*scale;
    				x = nx*scale;
    			}				
    		}
    				
    	}	
    			
    }
    
    my.handleDagCanvas = function(can) {
    			
    	var att = can.getAttribute("data-scale");	
    	if(att) {
    		scale = parseFloat(att);
    	}
    	att = can.getAttribute("data-colors");	
    	if(att) {
    		colors = JSON.parse(att);		
    	}
    	att = can.getAttribute("data-xoffs");	
    	if(att) {
    		xoffs = parseInt(att);
    	}
    	att = can.getAttribute("data-yoffs");	
    	if(att) {
    		yoffs = parseInt(att);
    	}
    	
    	// Prepare the canvas
    	var context = can.getContext("2d");
    	context.fillStyle=colors[0];	
    	context.fillRect(0,0,can.width,can.height);
    	context.strokeStyle=colors[1];
    	context.beginPath();
    	
    	att = can.getAttribute("data-border");
    	if(!att || att!="false") {
    		context.rect(0,0,can.width-1, can.height-1);
    	}
    	
    	var command = can.getAttribute("data-command").split(",");
    	
    	for(var p=0;p<command.length;++p) {		
    		command[p] = command[p].trim();
    		var pc = parseInt(command[p],16);
    	
    		// Execute the command	
    		processScript(context,pc);	
    	
    	}
    	
    	context.stroke();
    	
    };
    
    return my;

}());