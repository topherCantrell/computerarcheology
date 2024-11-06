![Frogger Main Board Hardware](Frogger.jpg)

# Main Board Hardware

Main CPU is a Z80 running at 3.072MHz.

Sound CPU is a Z80 running at 1.78975MHz.

| Position   | Mapping        |
| ---------  | ---------      |
| frogger.26 | main 0000:0FFF |
| frogger.27 | main 1000:1FFF |
| frsm3.7    | main 2000:2FFF |
|  |  |
| frogger.608 | sound 0000:07FF |
| frogger.609 | sound 0800:0FFF |
| frogger.610 | sound 1000:17FF |
|  |  |
| frogger.607 | gfx 0000:07FF |
| frogger.606 | gfx 0800:0FFF |
|  |  |
| pr-91.6l | PROM |

```
    ADDRESS_MAP_UNMAP_HIGH
	AM_RANGE(0x0000, 0x3fff) AM_ROM
	AM_RANGE(0x8000, 0x87ff) AM_RAM
	AM_RANGE(0x8800, 0x8800) AM_MIRROR(0x07ff) AM_DEVREAD("watchdog", watchdog_timer_device, reset_r)
	AM_RANGE(0xa800, 0xabff) AM_MIRROR(0x0400) AM_RAM_WRITE(galaxian_videoram_w) AM_SHARE("videoram")
	AM_RANGE(0xb000, 0xb0ff) AM_MIRROR(0x0700) AM_RAM_WRITE(galaxian_objram_w) AM_SHARE("spriteram")
	AM_RANGE(0xb808, 0xb808) AM_MIRROR(0x07e3) AM_WRITE(irq_enable_w)
	AM_RANGE(0xb80c, 0xb80c) AM_MIRROR(0x07e3) AM_WRITE(galaxian_flip_screen_y_w)
	AM_RANGE(0xb810, 0xb810) AM_MIRROR(0x07e3) AM_WRITE(galaxian_flip_screen_x_w)
	AM_RANGE(0xb818, 0xb818) AM_MIRROR(0x07e3) AM_WRITE(coin_count_0_w) /* IOPC7 */
	AM_RANGE(0xb81c, 0xb81c) AM_MIRROR(0x07e3) AM_WRITE(coin_count_1_w) /* POUT1 */
	AM_RANGE(0xc000, 0xffff) AM_READWRITE(frogger_ppi8255_r, frogger_ppi8255_w)
```

>>> memory

| | | |
| --- | --- | --- |
| 8800      | watchdog         | read to reset watchdog |
| A800:ABFF | VIDEORAM         | |
| B000:B0FF | SPRITERAM        | |
| B808      | IRQENABLE        | |
| B80C      | FLIPY            | |
| B810      | FLIPX            | |
| B818      | COINCNT0         | |
| B81C      | COINCNT1         | |
| D000      | SOUND_CMD        | Port A: Sound command byte |
| D002      | SOUND_CTRL       | Port B: Sound control (interrupt) |
| D004      | 8255_0_C         | Port C: not used |
| D006      | 8255_0_CTRL      | Control register |
| E000      | INPUTS_A         | Port A: Inputs |
| E002      | INPUTS_B         | Port B: Inputs |
| E004      | INPUTS_C         | Port C: Inputs|
| E006      | 8255_1_CTRL      | Control register |

```
Inputs A:
0 2P UP
1 1P Shoot-2
2 SERVICE
3 1P Shoot-1
4 1P Right
5 1P Left
6 Coin-1
7 Coin-2

Inputs B:
0 DSW-2
1 DSW-1
2 2P Shoot-2
3 2P Shoot-1
4 2P Right
5 2P Left
6 2P Start
7 1P Start

Inputs C:
0 2P Down
1 DSW-5
2 DSW-4
3 DSW-3
4 1P UP
5 nc
6 1P Down
7 nc
```

```
/* the 2nd gfx ROM has data lines D0 and D1 swapped */
	for (offs = 0x0800; offs < 0x1000; offs++)
		rombase[offs] = BITSWAP8(rombase[offs], 7,6,5,4,3,2,0,1);
```

Lots of good information in mame/src/mame/video/galaxian.cpp
```
            objram[40] = vertical position of sprite 0
            objram[41] = picture number and H/V flip of sprite 0
            objram[42] = color of sprite 0
            objram[43] = horizontal position of sprite 0
```
