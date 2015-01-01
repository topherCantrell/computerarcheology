Computer Archeology
==================

This project contains the content and tools to generate my [Computer Archeology](http://computerarcheology.com) website.

It also contains the archeology tools (disassemblers, assemblers, formatters, etc).

# Website Format

The old website format was a TRAC wiki. I created several TRAC plugins that formatted disassembly markups. The goal was to make a multi-user site where lots of people could contribute. But TRAC is much more than a wiki. It has links for bug tracking and code browsing, none of which make sense in the archeology context.

The archeology site is all static pages. I decided to revert it to a plain website and run formatting tools on the code and text as part of the deployment-to-web process. These tools will process some TRAC-like markup in the text, and they will add links to the disassembly code.

There are two types of pages on the site: "code" and "discussion". They both have the same format shown here:

![](https://github.com/topherCantrell/computerarcheology/blob/master/art/NewLayout.jpg)

The "Constant links" provide contact and help information and anything else I might think of.

The left area of the page is a navigation tree of links. There are two tabs. The "Site" tab shows the navigation tree for the entire web site. This allows you to quickly jump to any page. The "Page" tab shows the navigation tree for the current page. This allows you to quickly jump to any section on a page. The navigation tree area has its own scroll bar.

The archeology site is very hierarchical. The "Bread Crumbs" show your current level in the hierarchy and gives you a quick path back up the chain.

There is an area in the page header for optional images that might distinguish a particular page. Space Invaders, for instance, might have a graphic of one of the invaders.

The "Page Content" is the main area of the page. This area has its own scrollbar. The page header is always visible.

# Art, Content, and Code

The "Art" directory contains pictures used in the README files in this project.

The "Content" directory here contains the resource files that go into making the website pages. This includes
the disassembly and the discussion about the disassembly.

The "Code" directory here contains the tools for deploying the "Content" to the web. It also includes the 
dig-tools (disassemblers, assemblers, etc) along with individualized tools for specific dig sites.

# TODO #

 - Fix the 3-area layout
 - Collapsible trees in the nav area
 - Movable separator between code and nav
 - Add an example page showing all the markup syntax (markup, code, address-files, etc)
 - Fix content on MadnessAndMinotaur
 - Rewrite entry text
 