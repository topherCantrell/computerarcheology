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
        scrollTop: $("#"+name).offset().top
    }, 200);
}

function prepareList() {
    $('#siteTree').find('li:has(ul)')
      .click( function(event) {
          
          //if (this == event.target) {
              //alert("clicked");
              $(this).toggleClass('expanded');
              $(this).children('ul').toggle('medium');
          //}
          return false;
      })
    
      //.addClass('collapsed expanded')
      //.children('ul').hide();
      
      //Hack to add links inside the cv
      $('#siteTree a').unbind('click').click(function() {
          window.open($(this).attr('href'),"_self");
          return false;
      });
    };
   
$(document).ready( function() {
    prepareList();
});