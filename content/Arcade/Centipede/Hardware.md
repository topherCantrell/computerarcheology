![Centipede](centiped.jpg)

# Hardware

**Centipede** runs on Atari's 1981 Centipede PCB (MAME driver `atari/centiped.cpp`,
machine `centiped`). The CPU is a **MOS 6502** clocked at **1.512 MHz** (12.096 MHz / 8).
The 6502 **halves to 0.756 MHz whenever it touches playfield RAM** (`0x0400`–`0x07BF`) —
the video hardware steals the bus there — so the real per-frame instruction count is lower
than the nominal 25200 cycles and depends on what the code is doing. The frame rate is a
flat **60 Hz**. The native raster is 256×256 with a 256×240 visible window; the monitor is
mounted rotated 90° counter-clockwise (MAME `ROT270`, a portrait cabinet).

The player controls a shooter along the bottom of the screen with a **trackball**, not a
joystick: the trackball's X and Y are **analogue deltas** read as up/down counters (a
4-bit magnitude plus a sign bit) at two input ports, not as direction bits.

Two hardware conventions matter when reading the map. (1) **A read and a write at one address can be different devices** — 
most visibly at `0x2000`, where a **read** returns
program ROM and a **write kicks the watchdog**. (2) A bank of single-bit outputs lives in an
**LS259 addressable latch** at `0x1C00`–`0x1C07`: one address per line, and the value written
is **data bit 7** (`write_d7`) — the coin counters, the two player LEDs (inverted), and the
screen-flip bit.

The one interrupt is an **IRQ** (not an NMI), asserted by the video counter chain a few times
per frame; the program **acknowledges it by writing `0x1800`** (`irq_ack_w`), which clears the
6502 IRQ line. High scores survive power-off in an **EAROM** (a small serial NVRAM) at
`0x1600`–`0x173F`. Sound is a **POKEY** custom chip at `0x1000`–`0x100F` (also the source of
the hardware random number the game reads).

## Memory & I/O map

>>> memory

| Address | Name | Description |
| --- | --- | --- |
| 0000:03ff | workRam | Work RAM (see [Work RAM](RAMUse.md)) |
| 0400:07bf | videoRam | Video RAM — a 32×30 grid of tile codes (the mushroom field and text) |
| 07c0:07ff | spriteRam | Sprite RAM — 16 objects × 4 fields (the shooter, centipede segments, spider, flea, scorpion, shots) |
| 0800 | dsw1 | R: DIP switch bank 1 (lives, bonus, difficulty, language) |
| 0801 | dsw2 | R: DIP switch bank 2 (coinage) |
| 0c00 | in0 / trackballX | R: IN0 — trackball X (bits 0-3 count, bit 7 sign), cabinet DIP (bit 4), service (bit 5, active-low), VBLANK (bit 6, active-high) |
| 0c01 | in1 | R: IN1 (active-low) — start 1P/2P, fire, tilt, coins, service |
| 0c02 | in2 / trackballY | R: IN2 — trackball Y (bits 0-3 count, bit 7 sign) |
| 0c03 | in3 | R: IN3 — cocktail P2 joystick (unused on the upright board) |
| 1000:100f | pokey | R/W: POKEY sound chip; a read returns the hardware random number / pot state |
| 1400:140f | paletteRam | W: colour RAM — the live palette the video hardware reads |
| 1600:163f | earomWrite | W: EAROM (high-score NVRAM) data |
| 1680 | earomControl | W: EAROM control |
| 1700:173f | earomRead | R: EAROM data |
| 1800 | irqAck | W: acknowledge/clear the 6502 IRQ line |
| 1c00:1c07 | outLatch | W (D7): LS259 output latch — one address per line (coin counters, LEDs, screen flip) |
| 2000 | rom / watchdog | R: program ROM. W: watchdog reset |
| 2000:3fff | rom | Program ROM, 8192 bytes (`centiped` parts 136001-307.d1 + -308.e1 + -309.fh1 + -310.j1) |

## IN0 — trackball X, cabinet, service, VBLANK (read at 0x0C00, MIXED polarity)

| Bit | Mask | Input |
| --- | --- | --- |
| 0–3 | 0x0f | Trackball X magnitude (this frame's horizontal delta) |
| 4 | 0x10 | DIP: cabinet (0 = upright) |
| 5 | 0x20 | Service (active-low) |
| 6 | 0x40 | VBLANK (active-high — the program polls it to sync to the frame) |
| 7 | 0x80 | Trackball X sign (direction) |

## IN1 — controls + coins (read at 0x0C01, active-low, idle 0xFF)

| Bit | Mask | Input |
| --- | --- | --- |
| 0 | 0x01 | Start 1P |
| 1 | 0x02 | Start 2P |
| 2 | 0x04 | Fire |
| 3 | 0x08 | Fire (cocktail) |
| 4 | 0x10 | Tilt |
| 5 | 0x20 | Coin 1 |
| 6 | 0x40 | Coin 2 |
| 7 | 0x80 | Service credit |

## IN2 — trackball Y (read at 0x0C02)

| Bit | Mask | Input |
| --- | --- | --- |
| 0–3 | 0x0f | Trackball Y magnitude (this frame's vertical delta) |
| 7 | 0x80 | Trackball Y sign (direction) |

## LS259 output latch (0x1C00–0x1C07, one address per line, value = data bit 7)

| Address | Line |
| --- | --- |
| 1c00 | Coin counter (left) |
| 1c01 | Coin counter (centre) |
| 1c02 | Coin counter (right) |
| 1c03 | Player-1 start LED (inverted) |
| 1c04 | Player-2 start LED (inverted) |
| 1c07 | Screen flip (cocktail) |

Addresses `0x1C05`–`0x1C06` are unused.

## Video — mushroom-field tilemap + sprites

The playfield is a **32×30 tilemap** at `0x0400`–`0x07BF`: one tile code per cell, holding
the mushroom field and the on-screen text. **Sprite RAM** at `0x07C0`–`0x07FF` holds **16 objects of four bytes each** — 
the shooter, the centipede's segments, the spider, the flea,
the scorpion, and the shots — each record giving a picture number, a colour, and a screen
position. The colours are not fixed in a PROM: the program writes a **live palette** into
colour RAM at `0x1400`–`0x140F`, which the video hardware reads as it draws (this is how the
game flashes and recolours the field between waves). The character and sprite pictures come
from two `0x800` bitplane ROMs (8×8 characters and 8×16 sprites decode from the same data).
