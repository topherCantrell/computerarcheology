![Time Pilot](timeplt.jpg)

>>> deploy:<br>
>>>   +timeplt.jpg<br>
>>>   Hardware.md<br>
>>>   RAMUse.md<br>
>>>   %Code.md<br>

# Time Pilot

**Disassembled by Karl Stiefvater**

**Time Pilot** (Konami, 1982) is a free-roaming multi-directional aerial shooter. Your
fighter stays fixed in the centre of the screen and turns to face the direction you steer
with the **8-way joystick**; the whole sky scrolls and banks around it, and you **fire in
the direction the ship is facing**. The parallax reads as forward flight, but mechanically
it is the world that moves past a centred plane.

The game runs through **five time eras** — **1910, 1940, 1970, 1982 and 2001** — in strict
order. In each era you shoot down enough enemy craft to make that era's **Mother-Ship**
appear, destroy it, and warp forward to the next era. Along the way, **parachuting pilots**
drift down across the field and are worth bonus points if you collect them.

There is no ending: clearing the final era wraps back to the first, harder and more
crowded than before. Run out of fighters and the game is over, with a chance to enter your
initials on the high-score table.

## Navigation

  * [Hardware](Hardware.md) — CPU, memory map, I/O ports, LS259 control latch, sprite format
  * [Work RAM](RAMUse.md) — the named work-RAM cells (0xA800–0xAFFF)
  * [Main CPU code](Code.md) — the annotated Z80 disassembly

## About this disassembly

This disassembly, RAM map, and game description were **produced by AI** and are
**verified against the original ROM and against MAME**. The recovered code was checked
to reproduce the ROM's own execution frame-for-frame, and the game model was confirmed
by observing the real game running under MAME. It is offered here transparently, as AI
work, precisely because it is machine-checked rather than hand-asserted — so verify it
against that evidence. Project: [https://github.com/qarl/arcade-js](https://github.com/qarl/arcade-js).

The disassembly covers the code reached from the two entry points — the reset vector
(`0x0000`, which jumps straight to `0x07B1`) and the vblank NMI (`0x0066`); ROM data
tables (tilemaps, lookup tables, text) and spans never reached from those entries are
shown as `DEFB` data blocks.
