function switchTab(name) {    	
	if( $("#"+name+"Tab").hasClass("active") ) {
		return;
	}    	
	if(name=="page") {
		$("#siteTab").removeClass("active");
		$("#pageTab").addClass("active");    	
		$("#siteTree").addClass("hidden");
		$("#pageTree").removeClass("hidden");
	} else {
		$("#pageTab").removeClass("active");
		$("#siteTab").addClass("active");
		$("#pageTree").addClass("hidden");
		$("#siteTree").removeClass("hidden");
	}
}

function pageScrollTo(name) {
	$('html, body').animate({
        scrollTop: $("#"+name).offset().top-150
    }, 200);
}