computerarcheology
==================

This project contains the content and tools to generate my [Computer Archeology](http://computerarcheology.com) website.

It also contains the archeology tools (disassemblers, assemblers, formatters, etc).

# Website Format

The old website format was a TRAC wiki. I created several TRAC plugins that formatted disassembly markups. The goal was to make a multi-user site where lots of people could contribute. But TRAC is much more than a wiki. It has links for bug tracking and code browsing, none of which make sense in the archeology context.

The archeology site is all static pages. I decided to revert it to a plain website and run formatting tools on the code and text as part of the deployment-to-web process. These tools will process some TRAC-like markup in the text, and they will add links to the disassembly code.

There are two types of pages on the site: "code" and "discussion". They both have the same format shown here:

![](https://github.com/topherCantrell/computerarcheology/blob/master/art/NewLayout.jpg)

