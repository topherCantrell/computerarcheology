![Frogger Main Board Hardware](Frogger.jpg)

# Main Board Hardware

**Frogger** runs on Konami's 1981 Frogger board, a member of the Galaxian video family
(MAME driver `galaxian/galaxian.cpp`, machine `frogger`). The main CPU is a **Zilog Z80**
clocked at **3.072 MHz** (18.432 MHz / 6), giving **50688 cycles/frame** at a **60.606 Hz**
refresh; the native raster is 256×224, displayed rotated (MAME `ROT90`).

A **second Z80** drives the sound hardware — an **AY-3-8910** PSG — receiving command
bytes from the main CPU through the second of the board's two i8255 PPIs (below).

Three hardware invariants matter when reading the map below: (1) a read and a write at
one address can be different devices — the program writes work RAM at `0x8800` region
addresses while a **read** of `0x8800` **kicks the watchdog** and returns `0xFF`; (2) all
memory-mapped I/O above `0xC000` runs through **two i8255 PPIs** in mode 0, so a port's
direction is set by control words the boot code writes — `PPI0` carries the three input
ports, `PPI1` the sound-command latch and audio interrupt; (3) a handful of single-bit
control lines are **standalone D0 latches** — one address per line, the data on bit 0 —
for the NMI enable, the two screen-flip bits, and the two coin counters.

## Memory & I/O map

>>> memory

| Address | Name | Description |
| --- | --- | --- |
| 0000:3fff | rom | Program ROM, 16384 bytes (`frogger` main-CPU parts frogger.26 + frogger.27 + frsm3.7) |
| 8000:87ff | workRam | Work RAM (see [Work RAM](RAMUse.md)) |
| 8800 | watchdog | R: watchdog reset — the read kicks the dog and returns 0xFF; mirror at 0x8800+0x07ff |
| a800:abff | videoRam | Video RAM / tilemap (galaxian_videoram_w), 0x20-wide rows; mirror mask 0x0400 |
| b000:b0ff | objRam | Object RAM (galaxian_objram_w): per-column scroll+colour 0x00-0x3F, 8 sprites × 4 bytes 0x40-0x5F, bullets 0x60-0x7F; mirror mask 0x0700 |
| b808 | irqEnable | W (D0): NMI enable — the main loop sets it to arm the vblank NMI, clears it to mask |
| b80c | flipY | W (D0): screen flip Y (cocktail) |
| b810 | flipX | W (D0): screen flip X (cocktail) |
| b818 | coinCounter0 | W (D0): coin counter 0 |
| b81c | coinCounter1 | W (D0): coin counter 1 |
| d000 | soundLatch | W: sound-command byte to the sound CPU (PPI1 port A) |
| d002 | soundControl | W: sound control (PPI1 port B) — a falling edge of bit 3 raises the audio /INT, bit 4 mutes |
| e000 | in0 | R: IN0 — joystick left/right, service, coins (PPI0 port A, active-low) |
| e002 | in1 | R: IN1 — start buttons, lives DIP (PPI0 port B, active-low) |
| e004 | in2 | R: IN2 — joystick up/down, coinage + cabinet DIPs (PPI0 port C, active-low) |

## IN0 — joystick L/R, service, coins (read at 0xE000, active-low, idle 0xFF)

| Bit | Mask | Input |
| --- | --- | --- |
| 2 | 0x04 | Service |
| 4 | 0x10 | Right |
| 5 | 0x20 | Left |
| 6 | 0x40 | Coin 2 |
| 7 | 0x80 | Coin 1 |

Bit 0 (0x01) carries Up in the flipped cocktail view; bits 1 and 3 are unused.

## IN1 — start buttons + lives DIP (read at 0xE002, active-low, idle 0xFC)

| Bit | Mask | Input |
| --- | --- | --- |
| 0–1 | 0x03 | DIP: lives (default 0x00 = 3) |
| 6 | 0x40 | Start 2P |
| 7 | 0x80 | Start 1P |

Bits 4–5 carry Right/Left in the cocktail view; bits 2 and 3 are unused. The lives DIP
sits in this port (default `0x00` = 3), which is why the idle read is `0xFC`, not `0xFF`.

## IN2 — joystick U/D, coinage + cabinet DIPs (read at 0xE004, active-low, idle 0xF1)

| Bit | Mask | Input |
| --- | --- | --- |
| 1–2 | 0x06 | DIP: coinage (default 0x00 = 1 coin / 1 credit) |
| 3 | 0x08 | DIP: cabinet (default 0x00 = upright; set = cocktail, screen flip) |
| 4 | 0x10 | Up |
| 6 | 0x40 | Down |

Bit 0 (0x01) carries Down in the cocktail view; bits 5 and 7 are unused. The two DIP bits
seated here make the idle read `0xF1`.

## Standalone D0 control latches (one address per line, data on bit 0)

Five single-bit lines are written as their own addresses, each taking the value on data
bit 0 (the decode masks the address, so mirrors resolve to the same latch).

| Address | Line |
| --- | --- |
| b808 | NMI enable (the main loop writes 1 to arm the vblank NMI) |
| b80c | Screen flip Y (cocktail) |
| b810 | Screen flip X (cocktail) |
| b818 | Coin counter 0 |
| b81c | Coin counter 1 |

## Video — tilemap + object RAM

The display is a Galaxian-family tilemap plus an object layer. **Video RAM** at
`0xA800`–`0xABFF` holds one tile code per cell over a 0x20-wide grid (drawn rotated).
**Object RAM** at `0xB000`–`0xB0FF` is three regions in one page: the first 0x40 bytes are
**per-column scroll and colour** (the river and road lanes scroll by writing these — column
N takes its scroll from objRam[N×2]), `0x40`–`0x5F` are the **eight hardware sprites** of
four bytes each (the frog, the fly, and the sprite-drawn objects), and `0x60`–`0x7F` is the
bullet region (unused by Frogger's play). Each sprite record decodes as: **byte0** →
position on one axis; **byte1** → tile `code & 0x3f` plus flip-X (0x40) / flip-Y (0x80);
**byte2** → colour; **byte3** → the other axis.