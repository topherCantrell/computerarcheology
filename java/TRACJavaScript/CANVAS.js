
// data-canvasFunction
var handleCanvasFunction = null;

// Cache of the page (for data extraction)
var htmlUpper = "";

/**
 * When the page has loaded then look for every <canvas> on the page and run its
 * "data-canvasFunction" function. The function name is cached to that only the
 * first canvas on the page needs to specify a function used by all.
 */
window.onload = function() {	
	
	htmlUpper = document.body.innerHTML.toUpperCase();

	var cans = document.getElementsByTagName("canvas");
	for(var x=0;x<cans.length;++x) {		
		var att = cans[x].getAttribute("data-canvasFunction");	
		if(att!=undefined) {
			handleCanvasFunction = att;
		}
		window[handleCanvasFunction](cans[x]);		
	}

};