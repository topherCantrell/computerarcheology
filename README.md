Computer Archeology
==================

This project contains the content and tools to generate my [Computer Archeology](http://computerarcheology.com) website.

It also contains the archeology tools (disassemblers, assemblers, formatters, etc).

First clone this project. The "art" directory contains images for the READMEs here. The "java" directory contains assemblers and disassemblers and various older tools that need translating to Python.

The "content" directory contains the raw files that make up the Computer Archeology website.

The "src" directory contains the Python source files. You should run command line tools with this as your current working directory.

Once you have cloned the project open a command line to the "src" directory. 

```
python make_web.py
```

This command creates a "deploy" directory. This is a local copy of the webserver root directory.

```
python local_web_server.py
```

This command starts a local web server. Point your browser to "localhost".

The "site.js" file in the "src" directory is the JSON file that describes the content directories and the process to create the website. If you add new digs or files then you'll edit this description.

# Website Format

The old website format was a TRAC wiki. I created several TRAC plugins that formatted disassembly markups. The goal was to make a multi-user site where lots of people could contribute. But TRAC is much more than a wiki. It has links for bug tracking and code browsing, none of which make sense in the archeology context.

The new archeology site is all static pages. I decided to revert it to a plain website and run formatting tools on the code and text as part of the deployment-to-web process. These tools will process some TRAC-like markup in the text, and they will add links to the disassembly code.

There are two types of pages on the site: "code" and "discussion". They both have the same format shown here:

![](https://github.com/topherCantrell/computerarcheology/blob/master/art/NewLayout.jpg)

The "Constant links" provide contact and help information and anything else I might think of.

The left area of the page is a navigation tree of links. There are two tabs. The "Site" tab shows the navigation tree for the entire web site. This allows you to quickly jump to any page. The "Page" tab shows the navigation tree for the current page. This allows you to quickly jump to any section on a page. The navigation tree area has its own scroll bar.

The archeology site is very hierarchical. The "Bread Crumbs" show your current level in the hierarchy and gives you a quick path back up the chain.

There is an area in the page header for optional images that might distinguish a particular page. Space Invaders, for instance, might have a graphic of one of the invaders.

The "Page Content" is the main area of the page. This area has its own scrollbar. The page header is always visible.

# Content and Code

The "Content" directory here contains the resource files that go into making the website pages. This includes
the disassembly and the discussion about the disassembly.

The "Code" directory here contains the tools for deploying the "Content" to the web. It also includes the 
dig-tools (disassemblers, assemblers, etc) along with individualized tools for specific dig sites.

# TODO #

 - Add an example page showing all the markup syntax (markup, code, address-files, etc)
 - Rest of CoCo pages (Pyramid, Rakatu, Bedlam)
 - Collapsible trees in the nav area
 - Movable separator between code and nav
 - Rewrite entry text
 
# Markup Syntax (.mark files)

## Text ##

Blank lines are treated as paragraph separators. They become &lt;p&gt; in the resulting HTML.

You can insert HTML line breaks in the text with "[[br]]".

For instance:

```
These three lines[[br]]
are close[[br]
together.
```

### Raw Format ###

You can tell the processor not to process a section of text. The "{{{" at the 
beginning of a line begins a non-processed section of lines. The "}}}" at the
beginning of a line ends the non-processed section of lines.

There are three kinds of "raw" sections:
 - {{{ - the section is wrapped in a "pre" element. The contents are still "entized" (see below).
 - {{{code - the section is wrapped in a "pre" element. The contents are still "entized" (see below).
 - {{{html - the section is placed as is with a "pre" and without "entizing".

The "code" and "(nothing)" are identical except for CSS styling. The "code" section has a different'
CSS class allowing for different fonts and background colors. The default (nothing), for example,
has a gray background while "code" is white.

Examples:
```
{{{
This is
preformatted
text
}}}

{{{html
<span class="flashing">Important Text</span>
}}}

{{{code
0308: CE 00 A5            LDU     #$00A5      ; Destination (over BASIC's GETCCH routine)
030B: A6 80               LDA     ,X+         ; Copy ...
030D: A7 C0               STA     ,U+         ; ... the ...
030F: 8C 03 75            CMPX    #$0375      ; ... print character ...
}}}
```
    
### Entizing ###

Some characters like "&lt;" and the " itself have meaning in the broswer rendering the HTML. These must be replaced
with entities like "&amp;lt;" and "&amp;quot;". This is done automatically for all lines EXCEPT lines in an "html"
raw section.
    
### Headers ###

Headers and subheaders are defined with leading and trailing "=". The more "="
the deeper the subheading. These headers and subheaders automatically form the
page's navigation tree on the left.

You might want the entry in the navigation tree to have a different (shorter)
text. Any text following the ending "=" is used in the nav tree. For instance:

```
== Finding all the Spell Containers == Spells
```

This creates a level-two subheading with the given text. In the navigation tree
the shorter "Spells" is used.    

### Tables ###

Tables are defined using the double pipe character at the beginning of the line.

For instance:

```
||= Address || Name             || Description ||
|| 00       || curRoom          || current room ||
|| 01       || lastRoom         || last room ||
|| 02       || dirBits          || direction command bit pattern ||
|| 03       || inpLen           || length of user input ||
|| 04       || weight           || weight of pack ||
|| 05       || condition        || physical condition ||    
```

The "||=" on the first line indicates that the line is a table header. Tables may be defined without a header row.

### Links ###

You can define HTML links to other pages or sites with the "[url text]" syntax. The "url" is the destination
of the link. The "text" is the text of the link. If you omit the "text" then the "url" is used as the text.

```
For more information see [http://https://www.wikipedia.org/].
For more information see [https://www.wikipedia.org/ The Wikipedia].
```

If the URL begins with a '!' then the URL is treated as an image dropped inline.

```
Here are the schematics:
[!http:/somePicture.jpg]
```

### Bullet Lists ###

Bullet lists are created with a series of lines that begin with a '*'. For instance:

```
This section of code is:
* Well written
* Fast
* Fun to look at
```

You may use links (see above) in bullet lists.

### Defines ###

Defines allow you to pass information to the processor itself. These usually appear at the beginning of the text.

Defines begin with "%%". For instance:

```
%%title Pyramid
%%template SpecialShort.template

Welcome to the Pyramid site!
```

The key is the first word after the "%%". The rest of the line is the value.

Defines and their use:
 - %%title - gives the text used in the browser tab. The default is the page title from the deployment description.
 - %%template - gives the page's master HTML template. The default is "master.template". This is ?never? used.
 - %%- - used in code markdown. Defines the file containing ram-usage information.
 - %%-2 - used in code markdown. Defines the file containing hardware-usage information.

## Code Markup ##

Code files are processed with a tool designed for assembly/disassembly code.

Lines that begin with ";;" are unwrapped and handled as-is by the markdown processor.
This allows markdown discussion sections to be included in the code yet still use
leading-semicolon comments to the assembler/disassembler tools.

Code may be linked to markdown files that describe ram-address-usage and hardware-address-definitions.

These separate files contain one or more tables of the format:

```
||= Address || Name             || Description ||
|| 00       || curRoom          || current room ||
|| 01       || lastRoom         || last room ||
|| 02w      || WSYNC            || start VSYNC ||
|| 02r      || COLP1PF          || check collision between player and field ||
|| 03       || inpLen           || length of user input ||
|| 04       || weight           || weight of pack ||
|| 05       || condition        || physical condition ||  
|| 06:22    || buffer           || user input buffer ||
```

The first column is the numeric address referenced in the code. The second column contains the symbolic name for the address.
This can be left blank and the number address will be shown instead. The third column describes how the location is used.

Note the "w" and "r" on address "02". Hardware addresses often have different functions for reading and writing. You may give
addresses a "w" or "r" to indiciate which label is for which direction.

The address can actually be a stretch of addresses. You can give the start address and the end address (inclusive) separated by
a semicolon as shown in the last entry in the table above.

You link the code to the description files with a define. For instance:

```
;;%%- Coco/MadnessMinotaur/RAMUse.mark /CoCo/MadnessMinotaur/RAMUse.html
;;%%-2 Coco/Hardware.mark /CoCo/Hardware.html
```

The defines include the name of the markdown file (needed to parse the info) and the name of the
resulting file (needed in HTML links placed in the code).

### Labels in the nav-tree ###

Code label lines are of the form "SomeLabel:". These are processed as plain code lines by the code tools and by the markdown
processor.

Code labels can be added to the page-navigation tree by adding a comment on the end with one or more "=" marks. Use the 
desired number of "=" to pick the heading level in the navigation tree. For instance:

```
PrintChar: ; ==
```

The "PrintChar" will appear in the page navigation at level two (two '=').

### Moving labels above comments ###

Labels are usually kept close to the code. But sometimes a long section of markdown
discussion appears before the label. You would like for links to the label to target
the discussion instead of the label itself.

You do this by adding an empty "#" to the end of a header in the code markdown:

```
;; == Print a Character == #
;; A6 -- Print character in A with scrolling. This screen is TWO screens long
;; so that the user can use UP and DOWN to switch between screens. This replaces
;; BASIC's one-screen print.
;;
PrintChar:
;
032E: 34 16               PSHS    X,B,A       ; Save parameters
0330: 9E 88               LDX     >$88        ; Cursor
0332: 81 08               CMPA    #$08        ; Printing a backspace?
0334: 26 0B               BNE     $341        ; No ... move on
0336: 8C 02 00            CMPX    #$0200      ; Already at top of screen (double screen)
0339: 27 38               BEQ     $373        ; Yes ... ignore it (done)
033B: 86 60               LDA     #$60        ; Space
033D: A7 82               STA     ,-X         ; Over last in buffer
033F: 20 25               BRA     $366        ; Store new cursor and out
```

Any code that links to 032E (PrintChar) will link to the header "Print a Character" instead. The
processor will automatically look down from the "#" line to find the very next label in the code.

### Address links ###

Numeric constants in the code (specifically disassembly) often refer to memory addresses. These
could be addresses in the code (as with "jumps" or "call" statements). They could be memory
addresses where variables are stored. Or they could be memory-mapped hardware addresses.

These addresses can be given symbolic names. In code you give a code label to the target address.
In memory-use or hardware-use you give a separate file with a table that defines the addresses.

Either way the code processor can replace the numeric constants in the code with HTML links to
the definition. This makes it particularly easy to jump around while reading code.

You must tell the code processor what numbers are addresses and what kind of address they are.
You do this with the "{...}" syntax in the code comment.

For example:

```
PrintChar:
032E: 34 16               PSHS    X,B,A       ; Save parameters
0330: 9E 88               LDX     >$88        ; {-88} Cursor
0332: 81 08               CMPA    #$08        ; Printing a backspace?
0334: 26 0B               BNE     $341        ; {341} No ... move on
0336: 8C 02 00            CMPX    #$0200      ; Already at top of screen (double screen)
0339: 27 38               BEQ     $373        ; {373:IgnoreIt} Yes ... ignore it (done)
033B: 86 60               LDA     #$60        ; Space
033D: A7 82               STA     ,-X         ; Over last in buffer
033F: 20 25               BRA     $366        ; {366} Store new cursor and out
```

In this case the number "$88" is replaced with an HTML link to the RAM file that defines the 
address. If the RAM file has a name for the address then the name is used as the text for
the link. Otherwise the link is named "$88". The single "-" tells the processor to link to the
the "RAM usage" file.

A double "--" tells the processor to link to the "Hardware usage" file.

In this case the number "$366" in the last line is replaced with a link back to the middle line
in the snippet that begins with "0336:". The number "$373" is replaced with "IgnoreIt".

The link can be placed in one of three places on the code line:
 - {...} No ">". Replace the number directly in the opcode.
 - {>...} One ">". Place the link to the right of the opcode.
 - {>>...} Two ">". Replace the "{}" in the comment. 

The second part indicates the address mapping:
 - {...} No "-". The reference is to part of the code.
 - {-}... One "-". The reference is to the RAM Usage.
 - {--...} Two "-". The reference is to the Hardware Usage.

The rest of the "{}" indicates the target and text of the reference in the form {target:text}. 

If the "target" contains a "/" then it is treated as an HTML URL. Otherwise (most often) it is treated as a numeric value
to be looked up in the code or address mapping file.

The "text" is the label at the numeric destination. It might be a label in the code or a name from a mapping file.

If the text is not given then the number itself is used as the text.

The "link" tool updates the "{...}" entries in the raw markup. You run this periodically to update the text labels (you
want to see these labels when you are working on the disassembly).

The link tool will add or update the "target:text" completely. Thus you can initially use "{}" or "{-}" as a placeholder
for the tool to process. If you do not want the link tool to update an entry then use the "{{...}}" syntax. It functions
the same but is ignored by the link tool.

The link tool uses the opcode to decide on "read" or "write" versions of the label from the hardware map file. For instance
"IN" and "OUT".

# New Format

## Variables

The page templates use information from variables that are usually set near the top of the page. The syntax is ```%%variable = value``.
* ```%%image    = Arch.jpg``` The image to use in the banner at the top of the page
* ```%%template = newlook.template``` The markdown template to use (defaults to ```master.template```)
* ```%%title    = Computer Archeology``` The title to use on the page

## Headers

Headers on the page are defined with the familiar markdown syntax.
```
# First level
## Second level
# Back to first level
```

## Links

Links are given as ```[text on page](url)```.

You can use the url as the text as ```[link]```.

## Bullets

Bullet lists are defined with the familiar markdown syntax.

```
* Item
* Item
* Item
```

Coming soon: nested bullets

## Blocks

```
{{{playMe
}}}

{{{html
}}}

{{{pre
}}}
```