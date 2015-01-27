Creating the Web Site
==================

The "makeweb" code generates the HTML files ...

How to run using "Deploy.py"

## Deployment JSON ##

TODO: discuss the "deploment" tool and its JSON format. Disuss directory structure.

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
 - %%ramMap - used in code markdown. Defines the file containing ram-usage information.
 - %%hardwareMap - used in code markdown. Defines the file containing hardware-usage information.

## Code ##

Code files are processed with a tool designed for assembly/disassembly code.

Lines that begin with ";;" are unwrapped and handled as is by the markdown processor.
This allows markdown discussion sections to be included in the code yet still like
leading-semicolon comments to the assembler.

Code may be linked two markdown files that describe ram-address-usage and hardware-address-definitions.

These separate files contain one or more tables of the format:

```
||= Address || Name             || Description ||
|| 00       || curRoom          || current room ||
|| 01       || lastRoom         || last room ||
|| 02       || dirBits          || direction command bit pattern ||
|| 03       || inpLen           || length of user input ||
|| 04       || weight           || weight of pack ||
|| 05       || condition        || physical condition ||  
|| 06:22    || buffer           || user input buffer ||
```

The first column is the numeric address referenced in the code. The second column contains the symbolic name for the address.
This can be left blank and the number address will be shown instead. The third column describes how the location is used

The address actually be a stretch of addresses. You can give the start address and the end address (inclusive) separated by
a semicolon as shown in the last entry in the table above.

You link the code to the description files with a define. For instance:

```
;;%%ramMap Coco/MadnessMinotaur/RAMUse.mark /CoCo/MadnessMinotaur/RAMUse.html
;;%%hardwareMap Coco/Hardware.mark /CoCo/Hardware.html
```

The defines include the name of the markdown file (needed to parse the info) and the name of the
resulting file (needed in HTML links placed in the code).

### Labels in the nav-tree ###

Code label lines are of the form "SomeLabel:". These are processed as plain code lines.

Code labels can be added to the page-navigation tree by adding a comment on the end with
one or more "=" marks. Use the desired number of "=" to pick the heading level in the
navigation tree. For instance:

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
0330: 9E 88               LDX     >$88        ; {-} Cursor
0332: 81 08               CMPA    #$08        ; Printing a backspace?
0334: 26 0B               BNE     $341        ; {} No ... move on
0336: 8C 02 00            CMPX    #$0200      ; Already at top of screen (double screen)
0339: 27 38               BEQ     $373        ; {} Yes ... ignore it (done)
033B: 86 60               LDA     #$60        ; Space
033D: A7 82               STA     ,-X         ; Over last in buffer
033F: 20 25               BRA     $366        ; {} Store new cursor and out
```

In this case the number "$88" is replaced with an HTML link to the RAM file that defines the 
address. If the RAM file has a name for the address then the name is used as the text for
the link. Otherwise the link is named "$88". The single "-" tells the processor to link to the
the "RAM usage" file.

A double "--" tells the processor to link to the "Hardware usage" file.

In this case the number "$366" in the last line is replaced with a link back to the middle line
in the snippet that begins with "0336:". If this line had a preceding label then the text of that
label would be used in the link. Since it does not, the link text is just "$366".

There are several options with the "{...}" syntax. All are optional.

The link can be placed in one of three places on the code line:
 - {} No ">". Replace the number directly in the opcode.
 - {>} One ">". Place the link to the right of the opcode.
 - {>>} Two ">". Replace the "{}" in the comment. 

The second part indicates the address mapping:
 - {} No "-". The reference is to part of the code.
 - {-} One "-". The reference is to the RAM Usage.
 - {--} Two "-". The reference is to the Hardware Usage.

The rest of the "{}" indicates the target and text of the reference in the form {target:text}. 

If the "target" contains a "/" then it is treated as an HTML URL. 

If the "target" is just a word then it is treated as a reference to a code label in the current file. 

If the "target" is empty then the processor uses the number (starts with $) in the opcode and finds the 
reference in the code. The text is the label if the line has a label or the plain number if not.

If "text" is given then it is used as the text in the link instead of the target.

Complete Examples:
 - {} Lookup the label or address and insert the link in place of the "$" in the opcode.
 - {>:HERE} Lookup the reference and insert a link at the end of the opcode. Use "HERE" as the link text.
 - {http:/nowhere:HERE} Replace the "$" with the link to "http:/nowhere". Use "HERE" as the link text.
 - {PrintChar} Replace the "$" with a link to the "PrintChar" label in the current code
 - {>>-} Lookup the number (starts with "$") as a RAM address and insert the link in place of the "{...}" in the comment.
 - {--FF20:PIA1} Lookup "FF20" in the hardware reference and insert a link in place of the "$" in the opcode.
 