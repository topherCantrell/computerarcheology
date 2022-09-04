
/**
 * When the page has loaded then look for every <canvas> on the page and run its
 * "data-canvasFunction" function. The function name is cached so that only the
 * first canvas on the page needs to specify a function used by all.
 */

 var Canvas = (function() {	
	
	var my = {}

	my.handleCanvasFunction = null

	my.redrawGraphics = function() {
		var cans = $("canvas")	
		for(var x=0;x<cans.length;++x) {
			var att = cans[x].getAttribute("data-canvasFunction")
			if(att) {
				my.handleCanvasFunction = eval(att)
			}
			my.handleCanvasFunction(cans[x])			
		}
	}

	return my;

}());
