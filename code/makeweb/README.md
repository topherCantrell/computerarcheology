Creating the Web Site
==================

The "makeweb" code generates the HTML files ...

How to run ...

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
 - %%ramMap - used in code markup. Defines the file containing ram-usage information.
 - %%hardwareMap - used in code markup. Defines the file containing hardware-usage information.

## Code ##
