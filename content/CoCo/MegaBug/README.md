![Megabug](megabug.jpg)

# Megabug

>>> deploy:<br>
>>>   +megabug.jpg<br>
>>>   +megabug.js<br>
>>>   +BinaryDataMegabug.js<br>
>>>   RAMUse.md<br>
>>>   Code.md<br>
>>>   ----<br>
>>>   Journal.md<br>

# Code Links

* [Disassembled Code](Code.md)
* [RAM Usage](RAMUse.md)

>>> tourGuide {

# Tour Guide
  * The maze generator
  * The game graphics
  * Using the top of the stack as a register  
  * The bug in the code around the "You need 16k" message
  * Code "personality" areas of questionable code
>>> }

# History
https://en.wikipedia.org/wiki/Dung_Beetles_(video_game)
1982 by Datasoft. Steve Bjork ported it to CoCo ... still licensed by Datasoft.
http://www.lcurtisboyle.com/nitros9/megabug.html

# Overview

Three screen buffers. Maze on first. 2nd and 3rd alternate drawing/display. Bugs and mouth
drawn on the magnifier (not magnification of smaller images).

Hold enter down at start to max bugs at 32. Maze gets tougher each level beaten. 9 different
difficulties. The last has no loops (see maze generator).

Reward screen between levels.

# We Gotcha
Audio samples

# Random values

# Inputs

Joystick or keyboard ... orthogonal/reverse direction handling.

# A Code Bug

The "not enough memory" bug.

# The pixel doubler table

# Maze Generator
Loopiness. Copy text from code for detail.


