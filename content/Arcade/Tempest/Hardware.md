![Time Pilot](timeplt.jpg)

# Hardware

**Time Pilot** runs on Konami's Time Pilot board (MAME driver `konami/timeplt.cpp`,
machine `timeplt`). The main CPU is a **Zilog Z80** clocked at **3.072 MHz** (the
18.432 MHz master clock / 3 / 2 — the driver notes this divider is unconfirmed but
standard for Konami boards of the era), giving **51200 cycles/frame** at an **exactly
60 Hz** refresh. The native raster is 256×256, of which 256×224 is visible (H 0–255,
V 16–239), displayed turned a quarter-turn for the upright cabinet (MAME `ROT90`).

A **second Z80** drives the sound hardware — **two AY-3-8910 PSGs** — and takes its
commands from the main CPU through a sound latch. The main CPU writes the command byte to
`0xC000`; it then pulses **`0xC304`** (LS259 bit 2) low-then-high, and that rising edge
fires a maskable interrupt on the sound Z80, which reads the latched byte back through
AY-3-8910 #1's port A.

Three hardware quirks matter when reading the map below: (1) a read and a write at one
address can be different devices — `0xC000` **reads** the video scan-line counter and
**writes** the sound latch, and `0xC200` **reads** a DIP-switch bank and **writes** the
watchdog reset; (2) the LS259 control latch at `0xC300`–`0xC30F` is bit-addressable with
**two addresses per bit** — the bit index is `(addr − 0xC300) >> 1`, the data taken from
d0; (3) unmapped reads **float high** and return `0xFF` (MAME's map opens with
`unmap_value_high()`), and the boot code relies on it — the reset routine reads `0x6000`
and compares it against `0x55` to detect an expansion ROM that is not fitted.

## Memory & I/O map

>>> memory

| Address | Name | Description |
| --- | --- | --- |
| 0000:5fff | rom | Program ROM, 24576 bytes (`timeplt` main-CPU parts tm1 + tm2 + tm3) |
| a000:a3ff | colorRam | Colour RAM — per-tile colour attribute; this board has *writable* colour, and a write marks the tilemap tile dirty |
| a400:a7ff | videoRam | Video RAM / tilemap — a 32×32 grid of 8×8 tiles |
| a800:afff | workRam | Work RAM, 2048 bytes (see [Work RAM](RAMUse.md)) |
| b000:b0ff | spriteRam0 | Sprite RAM bank 0 (mirror mask 0x0B00); only 0xB010–0xB03F is used |
| b400:b4ff | spriteRam1 | Sprite RAM bank 1 (mirror mask 0x0B00); only 0xB410–0xB43F is used |
| c000 | scanline | R: video scan-line counter — the ROM multiplexes the cloud sprites by it, drawing them twice 128 lines apart |
| c000 | soundLatch | W: sound-command byte to the audio Z80 |
| c200 | dsw1 | R: DIP-switch bank SW2 — lives, cabinet, bonus-life, difficulty, demo sounds |
| c200 | watchdog | W: watchdog reset |
| c300 | in0 | R: IN0 — coin / service / start, active-low |
| c300 | mainLatch | W (c300–c30f): the LS259 control latch — bit index `(addr−0xC300)>>1`, data on d0 (bit table below) |
| c320 | in1 | R: IN1 — player-1 8-way stick + fire, active-low |
| c340 | in2 | R: IN2 — player-2 (cocktail) 8-way stick + fire, active-low |
| c360 | dsw0 | R: DIP-switch bank SW1 — coinage |

Every I/O block carries a MAME mirror mask (`0x0CFF` on `0xC000`/`0xC200`, `0x0C9F` on
the port group): the mask names *don't-care* address bits, not a range, so a block answers
at every address that differs from its base only in those bits. Sprite RAM's `0x0B00`
mask likewise leaves bit `0x0400` free to pick between the two banks across
`0xB000`–`0xBFFF`.

## IN0 — coin / service / start (read at 0xC300, active-low, idle 0xFF)

The inputs are active-low: idle reads `0xFF`, and a pressed control clears its bit to 0.

| Bit | Mask | Input |
| --- | --- | --- |
| 0 | 0x01 | Coin 1 |
| 1 | 0x02 | Coin 2 |
| 2 | 0x04 | Service credit |
| 3 | 0x08 | Start 1P |
| 4 | 0x10 | Start 2P |

(Bits 5–7 are unused.)

## IN1 — player-1 controls (read at 0xC320, active-low, idle 0xFF)

| Bit | Mask | Input |
| --- | --- | --- |
| 0 | 0x01 | Left (8-way) |
| 1 | 0x02 | Right (8-way) |
| 2 | 0x04 | Up (8-way) |
| 3 | 0x08 | Down (8-way) |
| 4 | 0x10 | Fire (BUTTON1) |

(Bits 5–7 are unused.)

## IN2 — player-2 / cocktail controls (read at 0xC340, active-low, idle 0xFF)

IN2 is the cocktail player-2 stick and fire, with the identical bit layout to IN1 (left
`0x01`, right `0x02`, up `0x04`, down `0x08`, fire `0x10`); it is meaningful only in
cocktail play.

## LS259 control latch (write 0xC300–0xC30F, two addresses per bit, data on d0)

The latch is an 8-bit LS259 addressable latch (marked **B3** on the board). A write to
`0xC300`–`0xC30F` sets one of its eight bits from data bit 0; the bit is
`(addr − 0xC300) >> 1`, so two consecutive addresses select the same bit.

| Address | Bit | Line |
| --- | --- | --- |
| c300 | 0 | NMI enable — the main loop sets it to arm the vblank NMI |
| c302 | 1 | Flip screen (inverted: a *clear* latch bit flips the screen) |
| c304 | 2 | Sound-CPU IRQ trigger — a low→high edge fires a maskable interrupt on the audio Z80 |
| c306 | 3 | Audio mute — DC-mutes the LA4460 amplifier |
| c308 | 4 | Video enable; the ROM also stuffs values computed from ROM content here as a protection / tamper check |
| c30a | 5 | Coin counter 1 |
| c30c | 6 | Coin counter 2 |
| c30e | 7 | Payout (wired, not used) |

## Sprite record format (work-RAM object model → two hardware banks)

Moving objects live as **two parallel arrays in work RAM**: a **record** array based at
`0xA800` (16 bytes per slot) and a **sprite-entry** array based at `0xAA10` (2 bytes per
slot), locked in step by `entry = 0xAA10 + (record − 0xA800) / 8`. The record carries
state, headings and the sub-pixel *fraction* of the position; the entry carries the
whole-pixel X, the tile code, the attribute (colour plus two flip bits) and Y. A per-frame
DMA — the largest routine in the game — copies two 48-byte shadow bands from the entry
array into the two hardware sprite banks at `0xB010` and `0xB410`, encoding Y as
`~(Y + 0x0E)` and reordering the entries so that nearer parallax layers land at the lowest
hardware offsets (which paint last and so win overlaps).

In the hardware banks themselves — the 256-byte regions at `0xB000` (bank 0) and `0xB400`
(bank 1), of which only `0xB010`–`0xB03F` and `0xB410`–`0xB43F` are used — each sprite is
**two bytes in each bank**, read back by MAME's sprite drawing for even offsets `0x10`
through `0x3E`:

| Byte | Meaning |
| --- | --- |
| bank 0, even | screen X |
| bank 0, odd | tile code |
| bank 1, even | attribute: `colour = byte & 0x3F`, flip-X = `~byte & 0x40`, flip-Y = `byte & 0x80` |
| bank 1, odd | Y — drawn at raster row `241 − byte` |

That is the raster MAME renders; the whole picture is then turned a quarter-turn (`ROT90`)
for the upright cabinet. **Player shots are not sprites at all** — they are painted as 2×2
blocks of character cells through a pair of deferred-cell lists, and they skip any cell
whose colour-RAM priority bit is set, so they never scribble over foreground or HUD tiles.
