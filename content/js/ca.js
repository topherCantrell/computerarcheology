
$(function() {
	
	$('#siteTab').on('click', function() {
		if($("#siteTab").hasClass("active")) {
			return;
		}
		$("#pageTab").removeClass("active");
		$("#siteTab").addClass("active");
		$("#pageTree").addClass("hidden");
		$("#siteTree").removeClass("hidden");
	});
	
	$('#pageTab').on('click', function() {
		if($("#pageTab").hasClass("active")) {
			return;
		}
		$("#siteTab").removeClass("active");
		$("#pageTab").addClass("active");
		$("#siteTree").addClass("hidden");
		$("#pageTree").removeClass("hidden");
	});
	
	$('.branch').on('click', function(evt) {
		if (evt.target.localName=='li') {
			var e = $(this);	
			if(e.hasClass('expanded')) {
				e.removeClass('expanded');
				e.addClass('collapsed');
			} else {
				e.removeClass('collapsed');
				e.addClass('expanded');
			}		
			e.find('ul').toggle('fast');  
			evt.stopPropagation();
		}
	});
	
});

/*
function openTree() {  

	var x,y,ch;	
	var crumbs = $("#crumbs li a, #crumbs li span");
	var path = [];  
	var treeNode = $("#siteTree");
	
	// Get the path from the bread crumbs
	for(x=1;x<crumbs.length;++x) {
	    path.push(crumbs[x].textContent);       
	}	
	
	// All the items with children are collapsible
	$('#siteTree').find('li:has(ul)').toggleClass('collapsed');
	// All children are collapsed
	$('#siteTree').find('ul').attr('hidden',true);	
	
	var lastNode = null;
		
	for(x=0;x<path.length;++x) {
		ch = treeNode.children(); // treeNode is a <ul>
		for(y=0;y<ch.length;++y) {
			treeNode = $(ch[y]);		
			if(ch[y].firstChild.textContent.trim()==path[x]) {
				// This <li> node matches the path				
				// All of its direct children are visible				
				lastNode = $(ch[y].firstChild);
				lastNode.addClass("selectedPagePath");
				if($(treeNode).hasClass('collapsed')) {
					$(treeNode).children().removeAttr("hidden");				
					$(treeNode).addClass("expanded");	
				}
				// Keep processing with the children <ul>
				treeNode = treeNode.find("ul");
				break;              
			}
		}       
	}
	
	if(lastNode!==null) {
		var c = lastNode.html();
		lastNode.replaceWith("<span class='selectedPage'>"+c+"</span>");		
	}
	
}
*/

/*
function prepareList() {
	
	// We use the same tree for all pages. This function opens the tree
	// branches to match the breadcrumbs.
	openTree();

	$('#siteTree').find('li:has(ul)')
	.click( function(event) {
		$(this).toggleClass('expanded');
		$(this).children('ul').toggle('medium');          
		return false;
	});    

	// Sometimes a collapsible container is a link. In that case
	// just the +/- icon opens and closes. We need to deregister
	// the click handler we just added and let it flow normally.
	$('#siteTree a').unbind('click').click(function() {
		window.open($(this).attr('href'),"_self");
		return false;
	});
}

$(document).ready( function() {
	prepareList();	     
});
*/
