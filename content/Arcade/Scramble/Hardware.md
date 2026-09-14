![Pooyan](pooyan.jpg)

# Hardware

**Pooyan** runs on Konami's 1982 Pooyan board (MAME driver `konami/pooyan.cpp`, machine
`pooyan`), which shares its audio design with Time Pilot. The main CPU is a **Zilog Z80**
clocked at **3.072 MHz** (18.432 MHz / 6), giving **50688 cycles per frame** at a **60.606 Hz**
refresh; the native raster is 256×224, displayed rotated a quarter-turn to portrait (MAME
`ROT90`).

A **second Z80** drives the sound hardware — **two AY-3-8910** PSGs — and receives command
bytes from the main CPU through the sound latch at `0xA100`, woken by an attention line the
main CPU pulses (below).

Three things matter when reading the map. (1) A **read and a write at one address can be
different devices**: `0xA000` **reads DSW1**, but a **write** there **kicks the watchdog**.
(2) The input and dip-switch ports around `0xA0x0` are decoded through mirror masks, so each
answers across a range of addresses, and the inputs are **active-low** — an idle port reads
`0xFF`. (3) A bank of single-bit control lines is an **LS259 addressable latch** at
`0xA180–0xA187`: **one address per line, the data on bit 0**, with the line index in the low
three address bits. It carries the NMI enable, the sound-CPU attention line, the audio mute,
the two coin counters, a payout line, and screen-flip.

The board raises a **vblank NMI** (vector `0x0066`) once per frame, but only while the LS259's
NMI-enable line (`0xA180`) is set; the main loop arms it each frame and clears it to mask.

## Memory & I/O map

>>> memory

| Address | Name | Description |
| --- | --- | --- |
| 0000:7fff | rom | Program ROM, 32768 bytes (`pooyan` main-CPU parts 1.4a + 2.5a + 3.6a + 4.7a) |
| 8000:83ff | colorRam | Colour RAM — per-tile attribute bytes; a write marks the tilemap dirty |
| 8400:87ff | videoRam | Video RAM — per-tile character codes |
| 8800:8fff | workRam | Work RAM, 2048 bytes (see [Work RAM](RAMUse.md)) |
| 9000:90ff | spriteRam0 | Sprite RAM, bank 0 (mirror mask 0x0B00) |
| 9400:94ff | spriteRam1 | Sprite RAM, bank 1 (mirror mask 0x0B00) |
| a000 | dsw1watchdog | R: DSW1 dip switches; W: kick the watchdog |
| a080 | in0 | R: IN0 — coins, start, service (active-low; mirror mask 0xA1E0) |
| a0a0 | in1 | R: IN1 — player-1 controls (active-low) |
| a0c0 | in2 | R: IN2 — player-2 controls / cocktail (active-low) |
| a0e0 | dsw0 | R: DSW0 — coinage (active-low) |
| a100 | soundLatch | W: sound-command byte handed to the sound CPU |
| a180 | irqEnable | W (D0): NMI enable — set to arm the vblank NMI, clear to mask |
| a181 | soundAttention | W (D0): attention line to the sound CPU — a rising edge raises its /INT |
| a182 | soundMute | W (D0): audio mute |
| a183 | coinCounter0 | W (D0): coin counter 0 |
| a184 | coinCounter1 | W (D0): coin counter 1 |
| a185 | payout | W (D0): payout / ticket line |
| a187 | flipScreen | W (D0): screen flip for a cocktail cabinet (the latched sense is inverted) |
