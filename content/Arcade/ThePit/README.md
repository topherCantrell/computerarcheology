![The Pit](thepit.jpg)

# The Pit

>>> deploy:<br>
>>>   +thepit.jpg<br>
>>>   Hardware.md<br>
>>>   RAMUse.md<br>
>>>   Code.md<br>

**Disassembled by Karl Stiefvater**

# The Pit

**The Pit** (Zilec Electronics / Centuri / Taito, 1982) is a dig-and-escape game. You
play an **astronaut-explorer** stranded on a forbidden planet. You **dig down** through
a field of dirt and tunnels to a treasure chamber at the bottom, **grab jewels** — the
sparse crystals and diamonds scattered in the dirt — and then **climb back up to your ship** to escape. 
The final stretch of the climb is the **"Pit"** crossing.

A rival craft has also landed, so **three rival explorers** roam the tunnels. They are
hostile, and all three can be shot with your **horizontal laser**. Falling rocks and
arrows, and the Pit crossing itself, *block* your movement but never cost a life — a
life is lost only to enemy contact. The ubiquitous red field is diggable *dirt*, not
treasure; the only collectibles are the sparse crystals and diamonds.

A board **completes** when you reach the **top rung carrying at least one diamond**: the
ship descends to carry you off, and the board then rebuilds one level higher and faster.
Run out of lives and the game is over, with a chance to enter your initials on the
high-score table.

## Navigation

  * [Hardware](Hardware.md) — CPU, memory map, I/O ports, LS259 control latch, sprite format
  * [Work RAM](RAMUse.md) — the named work-RAM cells (0x8000–0x87FF)
  * [Main CPU code](Code.md) — the annotated Z80 disassembly

## About this disassembly

This disassembly, RAM map, and game description were **produced by AI** and are
**verified against the original ROM and against MAME**. The recovered code was checked
to reproduce the ROM's own execution frame-for-frame, and the game model was confirmed
by observing the real game running under MAME. It is offered here transparently, as AI
work, precisely because it is machine-checked rather than hand-asserted — so verify it
against that evidence. Project: [https://github.com/qarl/arcade-js](https://github.com/qarl/arcade-js).

The disassembly covers the code reached from the two entry points — the reset vector
(`0x0000`) and the vblank NMI (`0x0066`); ROM data tables (tilemaps, lookup tables, the
drop queue, text) are shown as `DEFB` dat