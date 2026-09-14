![Donkey Kong](dkong.jpg)

# Donkey Kong

>>> deploy:<br>
>>>   +dkong.jpg<br>
>>>   Hardware.md<br>
>>>   RAMUse.md<br>
>>>   Code.md<br>

**Disassembled by Karl Stiefvater**

# Donkey Kong

**Donkey Kong** (Nintendo, 1981) is a climbing game. A giant ape has carried a woman —
Pauline — to the top of a half-built construction site, and you play **Mario**, the carpenter
climbing up after her. You run along girders, climb ladders and **jump** the things the ape throws down;
a hit or a fall from more than a short drop costs a life. A **bonus counter** runs down for
the whole board and is paid into your score when you finish it.

There are **four boards**. **25m** is the girders, where the ape rolls **barrels** down at
you. **50m** is the conveyors. **75m** is the elevators and springs. **100m** is the rivets.
Two **hammers** are placed on 25m, 50m and 100m — not on 75m: grab one and you smash whatever
you touch until its timer runs out, but while you hold it you can only walk. You cannot jump,
you cannot climb, and you cannot put it down.

A board **completes** by position on 25m and 75m — climbing to the row where she is waiting —
by climbing past a line on 50m, and on 100m by removing the last of the **eight rivets**,
which you do by walking over them. The board order is a table in ROM, and it is not the
four-stages-a-level the outside record describes: level 1 is **two** boards (25m then 100m),
level 2 three, level 3 four, level 4 five, and from level 5 on the same group of six repeats
forever, with the difficulty ramp rising by level.

## Navigation

  * [Hardware](Hardware.md) — CPU, memory map, I/O ports, sound latches, sprite format
  * [Work RAM](RAMUse.md) — the named work-RAM cells (0x6000–0x6BFF)
  * [Main CPU code](Code.md) — the annotated Z80 disassembly

## About this disassembly

This disassembly, RAM map, and game description were **produced by AI** and are **verified against the original ROM and against MAME**. 
The recovered code was checked to reproduce the
ROM's own execution frame-for-frame, and the game model was confirmed by observing the real
game running under MAME. It is offered here transparently, as AI work, precisely because it
is machine-checked rather than hand-asserted — so verify it against that evidence. Project:
[https://github.com/qarl/arcade-js](https://github.com/qarl/arcade-js).

The main CPU has two entry points — the reset vector (`0x0000`) and the vblank NMI
(`0x0066`) — and everything time-critical hangs off the NMI; the main loop is a task
scheduler that waits on a frame counter the NMI decrements.
