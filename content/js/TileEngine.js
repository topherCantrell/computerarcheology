var TileEngine = (function() {	
	
	var my = {};

	var colors = ["#000000","#FF00FF","#FFFF00","#00FFFF"];
	var pixWidth = 8;
	var pixHeight = 8;
	var gridX = 8;
	var gridY = 8;
	var gap = 0.0;
	var address = 0;
	var gridPad = 0;
	var showBorder = false;
	var labColor = "#FFFFFF";
	var colorMap = {};
	var getTileDataFunction = null;
	
	/**
	 * This function processes the attributes and drawing for a single canvas. The
	 * attributes specify drawing parameters that are preserved until changed
	 * by a later canvas.
	 *   
	 *   data-colors                array of color values to map to pixel values -- or the name of a defined set
	 *   data-colorsName            if given, the name of this color set for later reference in data-colors
	 *   data-pixWidth              the width of a pixel square drawn on the canvas
	 *   data-pixHeight             the height of a pixel square drawn on the canvas
	 *   data-gridX                 number of pixels across a tile
	 *   data-gridY                 number of pixels down a tile
	 *   data-gap                   gap between pixels in a tile drawing
	 *   data-labelColor            color of the tile label ("" for no label)
	 *   data-address               disassembly address for the data for this canvas
	 *   data-gridPad               gap between tiles in a matrix of tiles
	 *   data-file                  name of disassembly file to load from the server
	 *   data-showBorder            true to show the border around the canvas (for sizing)
	 *   data-getTileDataFunction   name of the function used to get data for the tile commands
	 *   
	 *   data-command               list of tile commands separated with a ","
	 *     VH20               draw tile 20 with vertical and horizontal mirroring (V and H are optional)
	 *                        the next tile is drawn to the right of this one unless changed (see below)
	 *     :2x3:1,2,3,4,5,6   draw a 2x3 (2 across, 3 down) matrix of tiles given
	 *     :2x3:1,2           automatic increment to get 3,4,5, and 6
	 *     :2x3:1,2,,4,,6     empty tile values are left empty on the screen
	 *     #NewSet            change the color set to a predefined color set
	 *     +x                 skip a pixel to the right (for spacing)
	 *     +y                 skip a pixel down (for spacing)
	 *     *                  set X to 0 and Y to the next row (for spacing)
	 *
	 * @param can the canvas element in the HTML
	 */
	my.handleTileCanvas = function(can) {   
	
	    var att = can.getAttribute("data-address");
	    if(att) {
	        my.address = parseInt(att,16);
	    }
		att = can.getAttribute("data-pixWidth");	
		if(att) {
			pixWidth = parseInt(att);
		}
		att = can.getAttribute("data-getTileDataFunction");
		if(att) {
			getTileDataFunction = eval(att);
		}
		att = can.getAttribute("data-pixHeight");	
		if(att) {
			pixHeight = parseInt(att);
		}
		att = can.getAttribute("data-gridX");
		if(att) {
			gridX = parseInt(att);
		}
		att = can.getAttribute("data-gridY");
		if(att) {
			gridY = parseInt(att);
		}
		att = can.getAttribute("data-showBorder");
		if(att) {
			if(att=="true") showBorder=true;
			else showBorder=false;
		}
		att = can.getAttribute("data-colors");	
		if(att) {
			if(att.charAt(0)=='[') {
				colors = JSON.parse(att);
			} else {
				colors = colorMap[att];
			}
		}
		att = can.getAttribute("data-gap");
		if(att) {
			gap = parseFloat(att);
		}
		att = can.getAttribute("data-labelColor");
		if(att || att==="") {
			labColor = att;
		}
		att = can.getAttribute("data-address");
		if(att) {
			address = parseInt(att,16);
		}
		att = can.getAttribute("data-gridPad");
		if(att) {
			gridPad = parseFloat(att);
		}
		att = can.getAttribute("data-colorsName");
		if(att) {
			colorMap[att] = colors;
		}
		att = can.getAttribute("data-file");
		if(att) {
			if(att == "*") {
				htmlUpper = document.body.innerHTML.toUpperCase();
			} else {
				var client = new XMLHttpRequest();
				client.open("GET",att,false);
				client.send(null);
				var test = client.responseText;
				BinaryData.loadDataCache(test);
			}
		}
	
		att = can.getAttribute("data-command");
		if(!att) return;
		
		// Handle drawing commands
	
		var command = can.getAttribute("data-command").split(",");
	
		var context = can.getContext("2d");
		context.clearRect(0,0,can.width,can.height);
	
		var xo = 0;
		var yo = 0;
		var lastHeight = 8;
		var showCS = false
		var cs = ''
	
		for(var x=0;x<command.length;++x) {		
			command[x] = command[x].trim();
			console.log(command[x])
			if(command[x].charAt(0)=='#') {
				if(command[x].charAt(1)=='#') {
					cs = ''
				} else {				
					colors = colorMap[command[x].substring(1)];
					cs = command[x].substring(1)
				}
			} else if(command[x]=="*") {
				xo = 0;
				yo = yo + lastHeight*pixHeight;
			} else if(command[x]=="+x") {
				xo = xo + pixWidth;
			} else if(command[x]=="+y") {
				yo = yo + pixHeight;
			} else if(command[x].charAt(0)==':') {
				var i = command[x].indexOf("x");
				var width = parseInt(command[x].substring(1,i));
				var j = command[x].indexOf(":",i);
				var height = parseInt(command[x].substring(i+1,j));
				lastHeight = height*gridY;
				command[x] = command[x].substring(j+1);
				var lastCommand = "0";
				for(var yy=0;yy<height;++yy) {
					for(var xx=0;xx<width;++xx) {
						if(x<command.length) {
							if(command[x].charAt(0)=='#') {
								colors = colorMap[command[x].substring(1)];
								cs = command[x++].substring(1)
							}
							lastCommand = command[x++].trim();
						} else {
							var val = parseInt(lastCommand,16)+1;
							lastCommand = val.toString(16);						
						}
						singleTileCommand(context,xo+xx*pixWidth*gridX+xx*gridPad,yo+yy*pixHeight*gridY+yy*gridPad,gridX,gridY,lastCommand,cs);
					}
				}			
				--x;
				xo = xo + pixWidth*width*gridX;
			} else {			
				singleTileCommand(context,xo,yo,gridX,gridY,command[x],cs);
				xo = xo + pixWidth*gridX;
				lastHeight = gridY;
			}
	
		}
		
		if(showBorder) {		
			context.rect(0,0,can.width-1,can.height-1);
			context.strokeStyle = "#ff0000";
			context.stroke();
		}
	};
	
	my.setColorMap = function(colors) {
		colorMap = colors
	}
	
	/**
     * This function draws a single tile specification. A tile spec is a number with optional
     * prepended V (vertical mirroring) or H (horizontal mirroring) or both. This function
     * uses the registered "get data" function to get the tile data.
     * @param context  the canvas context
     * @param xo       x offset on canvas
     * @param yo       y offset on canvas
     * @param gridX    number of pixels across
     * @param gridY    number of pixels down
     * @param com      the tile command
     */
    function singleTileCommand(context,xo,yo,gridX,gridY,com,cs='') {
        
        var hmirror = false;
        var vmirror = false;
    
        com = com.toString();
        var ocom = com.trim();
        
        if(cs!='') {
        	ocom = ocom+' ('+cs+')'
        }
    
        if(com.charAt(0)=='V') {
            vmirror = true;
            com = com.substring(1);
        }
    
        if(com.charAt(0)=='H') {
            hmirror = true;
            com = com.substring(1);
        }
    
        if(com.length===0) return;
        
        var tileAddress = parseInt(com,16); 
        
        var pixelData = getTileDataFunction(tileAddress,address);
                
        drawPixelGrid(context,pixelData,0,gridX,gridY,ocom,hmirror,vmirror,xo,yo);
        
    }
    
    /**
     * This function draws a grid of pixels on the canvas and
     * optionally displays the given label over the top.
     * @param context    the canvas context
     * @param pixelData  the array of pixel data, 1 per pixel
     * @param dataStart  the starting offset in the pixelData
     * @param width      number of pixels across
     * @param height     number of pixels down
     * @param label      label to show over grid or null for none
     * @param hMirror    true if grid should be mirrored horizontally
     * @param vMirror    true if grid should be mirrored vertically
     * @param xo         x offset on canvas
     * @param yo         y offset on canvas
     */
    function drawPixelGrid(context,pixelData,dataStart,width,height,label,
            hMirror,vMirror,xo,yo) 
    {           
        for(var y=0;y<height;++y) {
            for(var x=0;x<width;++x) {
                context.fillStyle = colors[pixelData[dataStart++]];
                
                var xx;
                var yy;
                
                if(hMirror) {
                    xx = xo+(width-1-x)*pixWidth;
                } else {
                    xx = xo+x*pixWidth;
                }
                
                if(vMirror) {
                    yy = yo+(height-1-y)*pixHeight;
                } else {                                  
                    yy = yo+y*pixHeight;
                }
                           
                context.fillRect(xx,yy,pixWidth-gap,pixWidth-gap);
            }
        }       
        if(label!==null && labColor!==null && labColor!=="") {
            context.fillStyle = labColor;   
            context.fillText(label,xo+pixWidth, yo+pixHeight*2);
        }   
    }
	
	return my;

}());