![Donkey Kong](dkong.jpg)

# Donkey Kong — Hardware

**Donkey Kong** runs on Nintendo's TKG-04 two-board set (MAME driver `nintendo/dkong.cpp`,
machine `dkong`). The main CPU is a **Zilog Z80** clocked at **3.072 MHz**
(61.44 MHz / 5 / 4), giving **50688 cycles/frame** at a **60.606 Hz** refresh; the native
raster is 256×224, displayed rotated into portrait (MAME `ROT270`).

A **second CPU** — an **Intel 8035** at 6 MHz — drives the sound hardware, mixing a DAC
against a set of discrete analog circuits and replaying one compressed sample (the gorilla
roar) out of its own second ROM. The main CPU reaches it through the tune latch at `0x7C00`,
three of the eight signal lines at `0x7D00`–`0x7D07`, and the interrupt line at `0x7D80`;
the rest of those signal lines fire discrete circuits directly, with no CPU in between.

An **i8257 DMA controller** at `0x7800`–`0x780F` does the sprite blit: the CPU stages 96
four-byte sprite records in work RAM, programs channel 0 source / channel 1 destination /
count, and pulses `0x7D85` to raise DREQ, which copies the block into sprite RAM.

Execution enters the main CPU at two points — the **reset vector** (`0x0000`) and the
**vblank NMI** (`0x0066`). Everything time-critical hangs off the NMI; the main loop is a
task scheduler that spins on a frame counter the NMI decrements.

Four hardware invariants matter when reading the map below: (1) a read and a write at one
address can be different devices — `0x7C00` **reads** the joystick and **writes** the tune
latch, `0x7D00` **reads** the coin/start port and **writes** the sound-signal latch; (2) a
read is not always pure — reading `0x7D00` *kicks* the watchdog and clocks the coin counter;
(3) the LS259 control latch at `0x7D00`–`0x7D07` is bit-addressable — one address per bit,
the data on d0, and the same one-address-per-bit scheme carries the palette bank at
`0x7D86`–`0x7D87`; (4) work RAM stops at `0x6BFF` — `0x6C00`–`0x6FFF` is not populated on
this board.

## Memory & I/O map

>>> memory

| Address | Name | Description |
| --- | --- | --- |
| 0000:3fff | rom | Program ROM, 16384 bytes (`dkong` main-CPU parts c_5et_g.bin + c_5ct_g.bin + c_5bt_g.bin + c_5at_g.bin); the board decodes as far as 4fff, the rest is unpopulated |
| 6000:6bff | workRam | Work RAM (see [Work RAM](RAMUse.md)); 6c00-6fff is not populated |
| 7000:73ff | spriteRam | Sprite RAM, 4-byte records; the DMA fills it from the work-RAM shadow buffer at 6900 once a frame |
| 7400:77ff | videoRam | Video RAM / tilemap, 32x32 cells of 8x8 tiles, row-major |
| 7800:780f | dma8257 | i8257 DMA controller registers (channel source, destination and transfer count) |
| 7c00 | in0 | R: IN0 - player 1 joystick + jump, active high |
| 7c00 | tuneLatch | W: tune number to the sound CPU (low 4 bits; table below) |
| 7c80 | in1 | R: IN1 - player 2 joystick + jump (cocktail), active high |
| 7d00 | in2 | R: IN2 - coin + start, active high; the read also kicks the watchdog and clocks the coin counter |
| 7d00 | soundLatch | W (7d00-7d07): the LS259 sound-signal latch - one address per bit, the data on d0 (bit table below) |
| 7d80 | dsw1 | R: DIP switch bank (lives, bonus, coinage, cabinet) |
| 7d80 | soundIrq | W: sound-CPU interrupt line - the "dead" trigger |
| 7d81 | gridEnable | W: Radar Scope grid enable; decoded by the board, never written by this ROM |
| 7d82 | flipScreen | W: screen flip for a cocktail cabinet (bit 0) |
| 7d83 | spriteBank | W: sprite-RAM bank select (bit 0) |
| 7d84 | nmiEnable | W: vblank NMI mask/enable (bit 0); clearing it both acknowledges the NMI and blocks re-entry |
| 7d85 | dmaRequest | W: pulses the DMA request lines - the sprite blit trigger |
| 7d86 | paletteBank0 | W: palette bank bit 0 (data on d0) |
| 7d87 | paletteBank1 | W: palette bank bit 1 (data on d0) |

## IN0 — player 1 controls (read at 0x7C00, active high)

| Bit | Mask | Input |
| --- | --- | --- |
| 0 | 0x01 | Right (4-way) |
| 1 | 0x02 | Left (4-way) |
| 2 | 0x04 | Up (4-way) |
| 3 | 0x08 | Down (4-way) |
| 4 | 0x10 | Jump (BUTTON1) |

## IN1 — player 2 controls (read at 0x7C80, active high)

The same five bits in the same order, from the cocktail cabinet's second control panel. The
ROM only reads this port when the cabinet DIP says cocktail and player 2 is up.

## IN2 — coin / start (read at 0x7D00, active high)

| Bit | Mask | Input |
| --- | --- | --- |
| 0 | 0x01 | Service / diagnostic (unlabelled on the schematics) |
| 2 | 0x04 | Start 1P |
| 3 | 0x08 | Start 2P |
| 6 | 0x40 | Status line back from the sound CPU |
| 7 | 0x80 | Coin |

## DIP switches (read at 0x7D80)

| Bits | Mask | Setting |
| --- | --- | --- |
| 0-1 | 0x03 | Lives: 3 / 4 / 5 / 6 |
| 2-3 | 0x0c | Bonus life at: 7000 / 10000 / 15000 / 20000 |
| 4-6 | 0x70 | Coinage: 000 = 1C/1P, 001 = 2C/1P, 010 = 1C/2P, 011 = 3C/1P, 100 = 1C/3P, 101 = 4C/1P, 110 = 1C/4P, 111 = 5C/1P |
| 7 | 0x80 | Cabinet: 1 = upright, 0 = cocktail |

## Tune select (write 0x7C00, low 4 bits)

The latch holds the number of the tune the sound CPU should play; the game rewrites it every
frame, so a held value loops.

| Value | Tune |
| --- | --- |
| 00 | silence |
| 01 | intro |
| 02 | "How high can you get?" intermission |
| 03 | out of time |
| 04 | hammer |
| 05 | rivet board, second completion (end tune) |
| 06 | hammer hit |
| 07 | standard board completed |
| 08 | background - 25m, girders and barrels |
| 09 | background - 50m, conveyors ("pie factory") |
| 0a | background - 75m, elevators and springs |
| 0b | background - 100m, rivets |
| 0c | rivet board, first completion (end tune) |
| 0d | rivet removed |
| 0e | rivet board completed |
| 0f | gorilla roar |

## LS259 sound-signal latch (write 0x7D00–0x7D07, one address per bit, data on d0)

Bits 0–2 fire discrete analog circuits directly. Bits 3–5 are input pins the sound CPU polls
rather than sounds in their own right. Bits 6–7 are decoded by the latch but reach nothing on
this board.

| Address | Bit | Line |
| --- | --- | --- |
| 7d00 | 0 | Walk |
| 7d01 | 1 | Jump |
| 7d02 | 2 | Boom - the gorilla stomps his foot |
| 7d03 | 3 | Coin insert / spring (read by the sound CPU) |
| 7d04 | 4 | Gorilla falling (sound CPU T1 input) |
| 7d05 | 5 | Barrel jump / prize (sound CPU T0 input) |
| 7d06 | 6 | Decoded, not connected |
| 7d07 | 7 | Decoded, not connected |

The ROM does not write these addresses individually: it holds eight one-per-line countdown
counters in work RAM and walks them against `0x7D00`–`0x7D07` once per vblank, asserting a
line while its counter is non-zero. Storing 3 into a counter is therefore a three-frame
assert. The ninth trigger — "dead" — is the write at `0x7D80`.

## Sprite record format (4 bytes each, staged at 0x6900, DMA'd to 0x7000)

Sprite RAM holds 4-byte records in a 0x200-byte bank selected by `0x7D83`; the game stages 96
records in work RAM and blits all 384 bytes each frame. Each record decodes as: **byte0** →
screen position on one axis; **byte1** → tile `code & 0x7f` plus flip on 0x80; **byte2** →
`color = byte2 & 0x0f` plus the palette bank, with the other flip on 0x80; **byte3** → the
other screen axis. Under the display's portrait (ROT270) view, the game's own X is byte0 and
its Y is byte3, while the raster reads them the other way round — that swap is the rotation,
not an error in the record.

Two hardware behaviours are visible in play: sprites **wrap** from one screen edge to the
other instead of clipping, and only the **first 16 sprites on a scanline** are shown, because
the line buffer holds 64 bytes.

## Tilemap and colour

The background is a 32×32 grid of 8×8 tiles at `0x7400`, one byte per cell. Colour is not
stored per cell: a PROM supplies a colour code **per screen column**, which the palette bank
bits at `0x7D86`–`0x7D87` extend. Changing the palette bank therefore recolours the whole
screen at once, which is how the board flashes on completion.
