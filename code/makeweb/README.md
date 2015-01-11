Creating the Web Site
==================

The "makeweb" code generates the HTML files ...

How to run ...

## Text ##

Blank lines are treated as paragraph separators. They become &lt;p&gt; in the resulting HTML.

You can insert HTML line breaks in the text with "[[br]]".

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
{{{
This is
preformatted
text
}}}
    

    
    
    


## Code ##
