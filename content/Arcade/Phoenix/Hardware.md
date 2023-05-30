![Phoenix Hardware Info](Phoenix.jpg)

# Hardware

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
