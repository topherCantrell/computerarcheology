![Journal](../../img/journal.jpg)

# Journal

# Questions to answer in the dig
  - Why the padding before certain routines to land them on nice addresses?
  - How does the call-stack work when RAM banks are changed

## 6/3/2023 



## 6/2/2023 

I did a little decoding of the first part of the ROM. It contains general purpose functions like 2-bit adds/subtracts
and 6-digit BCD math for the scores. There is a 6-digit BCD subtract, but it is never called. A score never
goes down.

I commented the "wait for VBLANK and handle coins" code. Too funny: the code only counts up to 9 coins. Any coins
that are put in after that are not counted. There are two digits on the screen for coins, but the code doesn't
handle two digits.

## 6/1/2023

I got the web site graphics working. You can switch between the two color pallettes with the click of a button.

I looked at the Mame video driver. The cocktail screen flip is tied to the RAM bank selected. If the coctail switch
is set, then switching to the second back automatically flips the screen. That's a sure tell that the banks are for
different players. But now I wonder how the stack works with bank flips.

Two byte values are referenced by pointers to the second (LSB). The code subtracts one to get to the MSB.

## 5/27/2023

I'm following the startup sequence. That should initialize the hardware and clear the screen.

There is a routine at 0x006B that clears a large chunk of memory from 0x4000 to 0x4BF8. It is called twice: once
for each bank of ram (switched by the lower bit in the video register). Let me change "clearing to 0" to
"clearing to 1" to verify at runtime.

I found the strings for the splash screen. The screen memory is just a map of bytes. I need to figure out how the color
palette works. The number chars are red while the letters are blue. There is nothing in the tile grids to suggest a
difference.

I have seen in videos that the palettes do change. The double-ring planet changes color in one of the videos.

## 5/26/2023

I'm going to keep a detailed journal of this one -- step by step!

Why Phoenix? I remember it as a minor arcade game (not a mainstream game like PacMan) found at the grocery store. I'd play while my mom shopped.

It's not a complex game with only one 8085 CPU. I disassembled it as Z80 opcodes.

The mame source shows how the individual ROM files map to program space:

```
    ROM_REGION( 0x10000, "maincpu", 0 )
	ROM_LOAD( "ic45",         0x0000, 0x0800, CRC(9f68086b) SHA1(fc3cef299bf03bf0586c4047c6b96ca666846220) )
	ROM_LOAD( "ic46",         0x0800, 0x0800, CRC(273a4a82) SHA1(6f3019a074e73ff50ceb92f655fcf15659f34919) )
	ROM_LOAD( "ic47",         0x1000, 0x0800, CRC(3d4284b9) SHA1(6e69f8f0d537fe89140cd95d2398531d7e93d102) )
	ROM_LOAD( "ic48",         0x1800, 0x0800, CRC(cb5d9915) SHA1(49bcf55a5721cfcc02c3b811a4b601e35ea576db) )
	ROM_LOAD( "h5-ic49.5a",   0x2000, 0x0800, CRC(a105e4e7) SHA1(b35142a91b6b7fdf7535202671793393c9f4685f) )
	ROM_LOAD( "h6-ic50.6a",   0x2800, 0x0800, CRC(ac5e9ec1) SHA1(0402e5241d99759d804291998efd43f37ce99917) )
	ROM_LOAD( "h7-ic51.7a",   0x3000, 0x0800, CRC(2eab35b4) SHA1(849bf8273317cc869bdd67e50c68399ee8ece81d) )
	ROM_LOAD( "h8-ic52.8a",   0x3800, 0x0800, CRC(aff8e9c5) SHA1(e4164f85ec12d4d9bcbffba27ab1f51b3599f6d0) )

	ROM_REGION( 0x1000, "bgtiles", 0 )
	ROM_LOAD( "ic23.3d",      0x0000, 0x0800, CRC(3c7e623f) SHA1(e7ff5fc371664af44785c079e92eeb2d8530187b) )
	ROM_LOAD( "ic24.4d",      0x0800, 0x0800, CRC(59916d3b) SHA1(71aec70a8e096ed1f0c2297b3ae7dca1b8ecc38d) )

	ROM_REGION( 0x1000, "fgtiles", 0 )
	ROM_LOAD( "b1-ic39.3b",   0x0000, 0x0800, CRC(53413e8f) SHA1(d772358505b973b10da840d204afb210c0c746ec) )
	ROM_LOAD( "b2-ic40.4b",   0x0800, 0x0800, CRC(0be2ba91) SHA1(af9243ee23377b632b9b7d0b84d341d06bf22480) )

	ROM_REGION( 0x0200, "proms", 0 )
	ROM_LOAD( "mmi6301.ic40",   0x0000, 0x0100, CRC(79350b25) SHA1(57411be4c1d89677f7919ae295446da90612c8a8) )  /* palette low bits */
	ROM_LOAD( "mmi6301.ic41",   0x0100, 0x0100, CRC(e176b768) SHA1(e2184dd495ed579f10b6da0b78379e02d7a6229f) )  /* palette high bits */
```

First up is to create the boilerplate directory in the content area so the web-render program will function. I'll
make binary files for the background tiles, foreground tiles, and proms.

The mame source "phoenix.cpp" has a lot of good info:

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

I looked through the code for "$50", "$58", "$60", etc and noted these hardware references in the comments.

Mame allows you to change the dip switch settings. I looked at the fields the code reads from the switches and found that Mame is
showing the switches left to right (backwards). Here are the switches from the code's point of view (MSb first):

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

There are two sets of sprites: background and foreground. The foreground is drawn over the scrolling background.

My intuition says the tiles are like the tiles in other systems (like Moon Patrol): split into two "bit planes" in the rom.
I ran a quick program to print text representations of the combined planes. I found the letters and numbers as expected,
though the images need to be rotated counter-clock-wise and then mirrored left to right. That's easy to do in code.

There are 256 tiles for foreground and 256 for background. Each tile is 8 bytes (8 bits by 8 bits). Each pixel can be one
of four colors (2 bits). One of the bits comes from the first plane in rom. The other comes from the second. 

I duplicated the javascript from other digs and got the tile sets displayed. Pretty cool looking. There is still a lot of
work to be done on the color palettes.

I made an intial pass through the code just looking around. There are a lot of padding FF bytes to start some functions
at nice addresses. For instance, the rountine at 0x200 has 8 padding bytes before it to land it on 0x200 exactly. I'm not
sure why the developers cared for the numeric address. Maybe I'll find that out!

I loked for "JP (HL)" and found a jump table at 0x400. Jump tables are easy to debug at runtime by changing the destinations.

I looked through the code for long sections of code that look "funny". These are data sections. Data seems to be sprinkled all
through the code and not neatly separated out to the end.