# Computer Archeology

The markdown files in this repo are parsed by a toolchain to generate the HTML files
for [Computer Archeology](http://computerarcheology.com).

Even pure disassembly code benefits from markdown discussion sections. Everything the
toolchain processes is thus markdown.

The markdown is also standard github flavor allowing files to be viewed there without the
fancy HTML linking.

```
py -m computerarcheology.carender.app
py -m computerarcheology.carender.development_server
```

# The names_in_code Tool

## Operands

Most assembly instruction have operands in the code that reference memory locations. Take 
the following three Z80 instructions for instance.

```
11 F0 02        LD      DE,$02F0            ; Put the value 02F1 in DE
3A 46 40        LD      A,($4046)           ; Load A with the value in memory $4046
28 01           JR      C,$CE               ; Jump if Z to code address $CE
```

In the first case, what is the value $02F1? Is it a pointer to a memory location? Or
is it just a constant for counting? Maybe it is a fast way to load D with 2 and E
with F0.

If the value $02F0 is a constant, then the line of disassembly is fine as is.

But if it is a pointer to memory, the memory might have a name. It would be useful for 
the architect to see that name. In our example here, let's say that $02F0 is the address
of a two-byte value called "syncDelay". The disassembly line is more useful like this:

```
11 F0 02        LD      DE,$02F0            ; {syncDelay} Pointer to the 2-byte counter
```

Now the architect can see what the memory is used for. And the web-deployment tool will
replace the numeric constant with an HTML link to the memory definition file. The link
uses the "syncDelay" name instead of constant. The tool also removes the {...} from the 
deployed comment.

For many instructions, the disassembler knows how the operand is used. In the second
instruction in our example, the value in parenthesis is a memory access -- no other
choice.

The same thing is true for the third instruction. The $CE is a memory address in the
code. If that code address has a label, the architect can look in the comments to
see the label instead of having to look it up. For instance:

```
11 F0 02        LD      DE,$02F0            ; Put the value 02F1 in DE
3A 46 40        LD      A,($4046)           ; {numAliens} Number of aliens left on this level
28 01           JR      Z,$CE               ; {startNext} If there are none, start the next level
```

## Multiple memory definition files

A system might have different memory definition files for different areas. All the code is usually
together in the disassembly file. But the RAM-usage might be defined in another file. The 
hardware memory locations might be defined in yet another file. The disassembly file lists all of
the memory files near the top. For instance:

```
>>> memoryTable hard 
[Hardware Info](SoundHardware.md)

>>> memoryTable ram 
[RAM Usage](SoundRAMUse.md)
```

This defines two memory definition files in addition to the current file. The "SoundHardware.md" is given 
a table name of "hard" (it contains hardware memory addresses). The "SoundRAMUse.md" is given a table
name of "ram" (it contains the RAM usage addresses). The current file is given the table name of
"code", since it is the disassembly opcodes.

The table names are prepended to the names in the comments making it easy for the architect to know where
a name comes from. For instance:

```
11 F0 02        LD      DE,$02F0            ; Put the value 02F1 in DE
3A 46 40        LD      A,($4046)           ; {ram.numAliens} Number of aliens left on this level
28 01           JR      Z,$CE               ; {code.startNext} If there are none, start the next level
```

## The tool

The "names_in_code" tool takes the name of the disassembly text file as a command-line
argument. The tool loads the disassembly and adds/corrects the "{...}" comments as needed. The
tool looks through the memory definition files for every operand in the code. If a name has
changed, the comment is updated to the latest name.

By default, all immediate-data instructions, like our example "LD DE,$02F0" are considered to be
constants. The are not given a "{...}" comment.

By default, all jumps and calls are considered to be memory addresses. They are given a "{...}"
comment by default. Our example "JR Z,$CE" for instance.

By default, all memory access is given a "{...}" comment.

If there is no name associated with the memory address, the tool inserts an empty comment "{}".
Later, as the architect adds code labels and memory definitions, the tool updates the comments
in the disassembly. You figured out that "00CE" is the "startNext" code. You add that label and
run the tool. Now all 50 places that call "00CE" are commented with the "startNext" name.

There are times when the architect needs to control the "{...}" comment tags.

Tags of the form "{!...}" will never be edited by the tool. The tool will use these tags, but it will never
update them.

Tags of the form "{+...}" tell the tool to treat the operand as a memory address. This is how we fix the
first opcode in our example. The tool will update the name in the tag if it changes.

Remember, a tag of the form "{...}" is in complete control of the names_in_code tool. The tool will
automatically edit or remove the tag as needed.

Here is the updated example with the $02F0 treated as a memory address:

```
11 F0 02        LD      DE,$02F0            ; {+ram.syncDelay} Pointer to the 2-byte counter
3A 46 40        LD      A,($4046)           ; {ram.numAliens} Number of aliens left on this level
28 01           JR      Z,$CE               ; {code.startNext} If there are none, start the next level
```