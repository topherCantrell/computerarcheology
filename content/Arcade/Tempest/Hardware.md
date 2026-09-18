![Tempest](tempest.jpg)

# Hardware

**Tempest** runs on Atari's 1981 Tempest hardware — an **Analog Vector-Generator PCB**
paired with a **Math Box PCB** (MAME driver `atari/tempest.cpp`, machine `tempest`). The CPU
is a **MOS 6502** clocked at **1.512 MHz** (the 12.096 MHz master crystal divided by 8); unlike
the raster boards there is no video bus contention, so a nominal frame is a flat **25200 cycles** 
at a **60 Hz** refresh.

Tempest is a **colour vector** game — Atari's "QuadraScan". There is **no tilemap and no frame buffer**. 
The 6502 builds a **display list** in **vector RAM** (`0x2000`–`0x2FFF`),
and the **Analog Vector Generator (AVG)** — a microcoded state machine sequenced by a
256-byte PROM — walks that list, together with shared shapes in **vector ROM**
(`0x3000`–`0x3FFF`), and drives the beam directly as line vectors. Colour is not baked into
a PROM: the program writes a live palette into **colour RAM** at `0x0800`–`0x080F` (sixteen
4-bit entries, write-only, the nibble active-low), which the AVG reads as it draws. The
monitor is mounted rotated for a portrait cabinet (MAME `ROT270`). The program kicks off a
draw by writing `0x4800` (AVG *go*) and can halt it by writing `0x5800` (AVG *reset*).

The **3D perspective of the tube is computed in hardware.** A **math box** — a multiply/
divide coprocessor built from PROM-driven bit-slice logic on its own PCB — takes an operation
and operand written to `0x6080`–`0x609F`, and the program reads back the two result bytes at
`0x6060` and `0x6070` and a status at `0x6040`. This is what projects the well and places
enemies at depth without the 6502 doing the arithmetic itself.

Two hardware conventions matter when reading the map. (1) **A read and a write at one address can be different devices** — most visibly at `0x6040`, where a **read** returns math-box
status and a **write** is EAROM control, and at `0x5000`, a write-only address that both kicks
the watchdog and acknowledges the interrupt. (2) **The player controls are read through the POKEY chips, not a memory-mapped input port.** The **spinner** is a 4-bit rotary encoder wired
to POKEY 1's pot (ADC) inputs; **fire** and **superzapper** are wired to POKEY 2's pots. The
program reads them by reading the POKEYs at `0x60C0`/`0x60D0`, the same chips that make the
sound.

The one interrupt is a **free-running periodic IRQ** (not an NMI, and **not** tied to vblank),
asserted about **246 times a second** (the 3 kHz clock divided by 12 — roughly four per
frame). The program **acknowledges it by writing `0x5000`** (which also resets the watchdog),
clearing the 6502 IRQ line. Because nothing signals vblank as an interrupt, the code syncs to
the display by polling the **AVG done** bit (IN0 bit 6) and a **~3 kHz clock** bit (IN0 bit 7).
A **watchdog** (the 3 kHz clock divided by 256, ~11.5 Hz) reboots the board if the game stops
kicking it. High scores survive power-off in an **EAROM** — a GI ER2055 64×8 electrically
alterable ROM — written at `0x6000`–`0x603F`, controlled at `0x6040`, and read at `0x6050`.

## Memory & I/O map

>>> memory

| Address | Name | Description |
| --- | --- | --- |
| 0000:07ff | workRam | R/W: work RAM (see [Work RAM](RAMUse.md)) |
| 0800:080f | colorRam | W (write-only): colour RAM — 16 × 4-bit entries (nibble active-low) the AVG reads while drawing |
| 0c00 | in0 | R: IN0 — coins (b0-2), tilt (b3), self-test (b4), diagnostic step (b5), AVG done/HALT (b6, active-high), ~3 kHz clock (b7) |
| 0d00 | dsw1 | R: DSW1 — coinage DIP bank (switch N13 on the AVG PCB) |
| 0e00 | dsw2 | R: DSW2 — minimum credits, language, bonus-life interval, lives (switch L12 on the AVG PCB) |
| 2000:2fff | vectorRam | R/W: vector RAM — the display list the 6502 builds each frame for the AVG |
| 3000:3fff | vectorRom | R: vector ROM — shared shapes/characters the display list references |
| 4000 | coin | W: coin counters (b0-2) + AVG screen flip X (0x08) / Y (0x10) |
| 4800 | avgGo | W: AVG *go* — start walking the display list |
| 5000 | wdclr / irqAck | W: reset the watchdog and acknowledge/clear the 6502 IRQ line |
| 5800 | avgReset | W: AVG *reset* (halt the vector generator) |
| 6000:603f | earomWrite | W: EAROM (high-score NVRAM) — address + data |
| 6040 | mathboxStatus / earomControl | R: math box status. W: EAROM control |
| 6050 | earomRead | R: EAROM data |
| 6060 | mathboxLo | R: math box result, low byte |
| 6070 | mathboxHi | R: math box result, high byte |
| 6080:609f | mathboxGo | W: math box — the offset selects the operation, the data is the operand |
| 60c0:60cf | pokey1 | R/W: POKEY 1 — sound; its pots read the spinner + cabinet DIP, and a read returns the hardware random number |
| 60d0:60df | pokey2 | R/W: POKEY 2 — sound; its pots read fire, superzapper, the start buttons + difficulty/rating DIPs |
| 60e0 | led | W: start LEDs (inverted) + player-select / cocktail bit (0x04) |
| 9000:dfff | rom | Program ROM, 20480 bytes (`tempest` parts 136002-133.d1 + -134.f1 + -235.j1 + -136.lm1 + -237.p1) |
| f000:ffff | rom | R: program ROM — a reload of the last 4K, holding the reset/IRQ vectors at 0xFFFA/C/E |

## Inputs — read through the POKEY pots

Tempest has no digital joystick. The controls arrive as one-bit "paddle" lines on the two
POKEY chips' pot (ADC) inputs, so the program reads them by reading the POKEYs:

| Control | Where | Notes |
| --- | --- | --- |
| Spinner | POKEY 1 pots, 4 bits | A rotary encoder; the code reads the 4-bit position and derives its own per-frame delta |
| Cabinet (upright/cocktail) | POKEY 1 pot bit 4 | A DIP, not a live switch (default upright) |
| Fire | POKEY 2 pot (BUTTON1) | Active-low |
| Superzapper | POKEY 2 pot (BUTTON2) | Active-low |
| Start 1 / Start 2 | POKEY 2 pots | Active-low |
| Difficulty / rating | POKEY 2 pots | DIP switches (D/E2 on the Math Box PCB) |

## IN0 — coins, service, AVG done, clock (read at 0x0C00, mixed polarity)

| Bit | Mask | Input |
| --- | --- | --- |
| 0 | 0x01 | Coin 3 (active-low) |
| 1 | 0x02 | Coin 2 (active-low) |
| 2 | 0x04 | Coin 1 (active-low) |
| 3 | 0x08 | Tilt (active-low) |
| 4 | 0x10 | Self-test (active-low) |
| 5 | 0x20 | Diagnostic step (active-low) |
| 6 | 0x40 | AVG done / HALT (active-high — the program polls it to know the draw finished) |
| 7 | 0x80 | ~3 kHz clock (active-high — a timing reference the program polls) |

## Sound

Sound is generated by **two POKEY custom chips** at `0x60C0` and `0x60D0`, each clocked at
**1.512 MHz** (master / 8), driven directly by the main 6502 — there is no separate sound
processor. Beyond the four tone/noise channels apiece, the POKEYs serve double duty as the
board's analogue-input readers (the spinner and buttons above) and as the source of the
**hardware random number** the game reads.
