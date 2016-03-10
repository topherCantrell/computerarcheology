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

function openTree() {	
	
	var crumbs = $("#crumbs").find("li a, li strong");
	var path = [];	
	for(var x=1;x<crumbs.length;++x) {
		path.push(crumbs[x].textContent);		
	}
		
	var treeNode = $("#siteTree");
	
	for(var x=0;x<path.length-1;++x) {
		var ch = treeNode.children();
		for(var y=0;y<ch.length;++y) {
			if(ch[y].firstChild.textContent==path[x]) {
				treeNode = $(ch[y]);
				$(treeNode).children().eq(1).removeAttr("hidden");
				$(treeNode).addClass("expanded");
				treeNode = treeNode.find("ul");
				break;				
			}
		}		
	}
	
	var last = path[path.length-1];
	if(!last) last="Home";
	var ch = treeNode.children();
	for(var y=0;y<ch.length;++y) {
		if(ch[y].firstChild.textContent==last) {
			$(ch[y]).children().first().replaceWith('<span class="sna"><strong>'+last+'</strong></span>');
			var ul = $(ch[y]).find("ul");
			if(ul.length>0) {
				$(ul[0]).removeAttr("hidden");
				$(ch[y]).addClass("expanded");
			}
			break;				
		}
	}	
	
}

function prepareList() {
	
	openTree();
	
    $('#siteTree').find('li:has(ul)')
      .click( function(event) {
              $(this).toggleClass('expanded');
              $(this).children('ul').toggle('medium');          
          return false;
      })    
      
      //Hack to add links inside the cv
      $('#siteTree a').unbind('click').click(function() {
          window.open($(this).attr('href'),"_self");
          return false;
      });
    };
   
$(document).ready( function() {
	$("#siteTree").load("/tree.html", function() {
        prepareList();
    }); 
});