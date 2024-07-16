![Phoenix Hardware Info](Phoenix.jpg)

# Hardware

https://github.com/mamedev/historic-mame/blob/master/src/mame/video/phoenix.c

```
Each memory bank:

0000 - 033F  - 32x26 foreground tiles
0340 - 07FF
0800 - 0B3F  - 32x26 background tiles
0B40 - 0FFF

The lower bit of video register 50xx selects the memory bank and the screen flipping for cocktail mode
(if cocktail mode is available via dipswitch). When the 2nd bank is selected (and switch) then the screen
is flipped.

The next-to-lowest bit control the color palette for both foreground and background.
```

From phoenix.cpp:

```
   map(0x0000, 0x3fff).rom();
	map(0x4000, 0x4fff).bankr("bank1").w(FUNC(phoenix_state::phoenix_videoram_w)); /* 2 pages selected by bit 0 of the video register */
	map(0x5000, 0x53ff).w(FUNC(phoenix_state::phoenix_videoreg_w));
	map(0x5800, 0x5bff).w(FUNC(phoenix_state::phoenix_scroll_w));
	map(0x6000, 0x63ff).w("cust", FUNC(phoenix_sound_device::control_a_w));
	map(0x6800, 0x6bff).w("cust", FUNC(phoenix_sound_device::control_b_w));
	map(0x7000, 0x73ff).portr("IN0");                            /* IN0 or IN1 */
	map(0x7800, 0x7bff).portr("DSW0");                           /* DSW */
```

Upper bit of DSW (0x78xx) is a screen-blanking flag. 0=in_VBLANK 1=not_in_VBLANK

```
0x7000
LSB goes from 1 to 0 when a coin is inserted
```

Music:

```
Tune1 -- Alarm sound
Tune2 -- Fuer Elise, Beethoven          0x6800:1000_1111
Tune3 -- ESTUDIO (Phoenix theme song)   0x6800:1100_1111
Tune4 --  single notes
```

# Switch Settings

```
LL_BB_C_xx_M

LL: Number of lives
  11 = three
  01 = four
  10 = five
  00 = six

BB: Bonus lives at
  11 = 3K/30K
  01 = 4K/40K
  10 = 5K/50K
  00 = 6K/60K

C: Coinage
  1 = 1 coin for 1 credit
  0 = 2 coins for 1 credit

M: Cabinet mode
  1 = cocktail
  0 = upright
```
>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 5000  | videoRegister  | Lower bit selects the RAM bank |
|	5800  | scrollRegister | Screen scrolling |
|	6000  | soundControlA  | Sound control A |
|	6800  | soundControlB  | Sound control B |
|	7000  | IN0            | Player inputs |
|	7800  | DSW0           | DIP switch settings|  
