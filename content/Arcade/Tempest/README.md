![Tempest](tempest.jpg)

>>> deploy:<br>
>>>   +tempest.jpg<br>
>>>   Hardware.md<br>
>>>   RAMUse.md<br>
>>>   %Code.md<br>

# Tempest

**Disassembled by Karl Stiefvater**

**Tempest** (Atari, 1981) is a first-person tube shooter drawn on a **colour vector**
display. You look **down a three-dimensional well** rendered in perspective. Your ship —
a claw-shaped **Blaster** — rides the **near rim** of the tube, and a **spinner** (a rotary
knob) rotates it around the edge, one lane at a time. Enemies climb **up the lanes toward you** 
from the far end; you fire straight down the lane the Blaster sits on to destroy them
before they reach the rim.

Each level is one tube of a fixed shape — a closed circle, a flat open line, a cross, a
figure of several joined segments — divided into **lanes** around its perimeter. The
geometry and the colour scheme change as you advance, cycling through a set of distinct
shapes recoloured across many levels.

Several kinds of enemy work up the well. A **flipper** is the basic threat: it flips from
one lane to the next and is deadly if it reaches your rim. A **tanker** carries two enemies
and **splits** when shot or when it tops out. A **spiker** spirals up a lane leaving a
growing **spike** behind it — a spike will not kill you on the rim, but it **impales** you
during the end-of-level warp if you fly down a lane that still holds a tall one. A
**fuseball** rolls along the rim between lanes, hard to hit and deadly on contact, and a
**pulsar** sits in a lane and electrifies it, killing you if it pulses while you share the
lane.

Your panic weapon is the **Superzapper**: the first press on a level destroys every enemy
on screen, a second press kills just one, and it recharges each level. Clear the tube and
you **warp** down the well to the next level — the view zooms through the geometry, and any
tall spikes must be shot away first or they take a life on the way through. Points come from
shooting enemies (harder types and deeper hits score more) and from clearing levels; bonus
lives arrive at DIP-selected score thresholds. Lose all your lives and the game ends, with a
chance to enter your initials on a high-score table that survives power-off.

## Navigation

  * [Hardware](Hardware.md) — CPU, memory & I/O map, the spinner and buttons, the two POKEYs, the AVG vector generator, the math box, the EAROM
  * [Work RAM](RAMUse.md) — the named work-RAM cells (0x0000–0x07FF)
  * [Main CPU code](Code.md) — the annotated 6502 disassembly

## About this disassembly

This disassembly, RAM map, and game description were **produced by AI** and are
**verified against the original ROM and against MAME**. The recovered code was checked
to reproduce the ROM's own execution frame-for-frame, and the game model was confirmed
by observing the real game running under MAME. It is offered here transparently, as AI
work, precisely because it is machine-checked rather than hand-asserted — so verify it
against that evidence. Project: [https://github.com/qarl/arcade-js](https://github.com/qarl/arcade-js).

The disassembly covers the code reached from the machine's real entry points — the reset
vector and the IRQ vector; ROM data tables (the tube geometry and colour tables, lookup
tables, text) are shown as data. Sound comes from **two POKEY custom chips**, driven
directly by the main CPU; there is no second processor, so this is the whole program. The
**Analog Vector Generator** that draws the picture and the **math box** that projects the
tube are hardware the 6502 feeds — a display list and a stream of coordinates — not code of
their own.
