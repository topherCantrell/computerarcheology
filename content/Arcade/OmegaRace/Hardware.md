![Omega Race Hardware Info](ORace.jpg)

# Hardware

>>> memory

| | | |
| --- | --- | --- |
|  09p     | WDOG             | Reset watchdog timer |
|  08p     | VGSTART          | Start/ (VG start) |
|  0Ap     | SEQRES           | SEQRES/ (VG stop/reset?) |
|  0Bp     | RDSTOP           | RDSTOP/ d7 = stop (VG running if 0) |
|  10p     | DIPSWC4          | DIP SW C4 (game ship settings) |
|  11p     | INPUTA           | Test, P1 Fire, P1 Thrust, Tilt, Coin1, Coin2 |
|  12p     | INPUTB           | Player/credit, P2 fire, P2 thrust (cocktail) |
|  13p     | OUTPUTA          | Screen flip, LEDs, coin meters |
|  14p     | SOUNDCMD         | Sound command (interrupts sound CPU) |
|  15p     | ENCODER1         | Encoder 1 |
|  16p     | ENCODER2         | Encoder 2 |
|  17p     | DIPSWC6          | DIP SW C6 (coin/cocktail settings) |


```
 /* main CPU */
 /* XTAL101 Crystal @ 12mhz */
 /* through 74LS161, Pin 13 = divide by 4 */
 MDRV_CPU_ADD("maincpu", Z80,12000000/4)
 MDRV_CPU_PROGRAM_MAP(main_map, 0)
 MDRV_CPU_IO_MAP(port_map, 0)
 MDRV_CPU_PERIODIC_INT(irq0_line_hold,250)

Memory Map:

    0000 - 3FFF ROM
    4000 - 4BFF RAM (3k)
    5C00 - 5CFF NVRAM (256 x 4bits)
    8000 - 8FFF VECTOR RAM (4k)
    9000 - 9FFF VECTOR ROM (4k)

    10 I    DIP SW C4 (game ship settings)

            6 5  4 3  2 1
                          1st bonus ship at
            | |  | |  0 0  40,000
            | |  | |  0 1  50,000
            | |  | |  1 0  70,000
            | |  | |  1 1 100,000
            | |  | |      2nd and  3rd bonus ships
            | |  0 0      150,000   250,000
            | |  0 1      250,000   500,000
            | |  1 0      500,000   750,000
            | |  1 1      750,000 1,500,000
            | |           ships per credit
            0 0           1 credit = 2 ships / 2 credits = 4 ships
            0 1           1 credit = 2 ships / 2 credits = 5 ships
            1 0           1 credit = 3 ships / 2 credits = 6 ships
            1 1           1 credit = 3 ships / 2 credits = 7 ships

    11 I
        7 = Test
        6 = P1 Fire
        5 = P1 Thrust
        4 = Tilt

        1 = Coin 2
        0 = Coin 1

    12 I
        7 = 1P2CR
        6 = 1P1CR

        3 = 2P2CR
        2 = 2P1CR
        1 = P2Fire -+
        0 = P2Thr  -+ cocktail only

    13 O
        7 =
        6 = screen reverse
        5 = 2 player 2 credit start LED
        4 = 2 player 1 credit start LED
        3 = 1 player 2 credit start LED
        2 = 1 player 1 credit start LED
        1 = coin meter 2
        0 = coin meter 1

    14 O    sound command (interrupts sound Z80)

    15 I    encoder 1 (d7-d2)

        The encoder is a 64 position Grey Code encoder, or a
        pot and A to D converter.

        Unlike the quadrature inputs on Atari and Sega games,
            Omega Race's controller is an absolute angle.

        0x00, 0x04, 0x14, 0x10, 0x18, 0x1c, 0x5c, 0x58,
        0x50, 0x54, 0x44, 0x40, 0x48, 0x4c, 0x6c, 0x68,
        0x60, 0x64, 0x74, 0x70, 0x78, 0x7c, 0xfc, 0xf8,
        0xf0, 0xf4, 0xe4, 0xe0, 0xe8, 0xec, 0xcc, 0xc8,
        0xc0, 0xc4, 0xd4, 0xd0, 0xd8, 0xdc, 0x9c, 0x98,
        0x90, 0x94, 0x84, 0x80, 0x88, 0x8c, 0xac, 0xa8,
        0xa0, 0xa4, 0xb4, 0xb0, 0xb8, 0xbc, 0x3c, 0x38,
        0x30, 0x34, 0x24, 0x20, 0x28, 0x2c, 0x0c, 0x08

    16 I    encoder 2 (d5-d0)

        The inputs aren't scrambled as they are on the 1 player
            encoder

    17 I    DIP SW C6 (coin/cocktail settings)

            8  7  6 5 4  3 2 1
                                 coin switch 1
            |  |  | | |  0 0 0   1 coin  2 credits
            |  |  | | |  0 0 1   1 coin  3 credits
            |  |  | | |  0 1 0   1 coin  5 credits
            |  |  | | |  0 1 1   4 coins 5 credits
            |  |  | | |  1 0 0   3 coins 4 credits
            |  |  | | |  1 0 1   2 coins 3 credits
            |  |  | | |  1 1 0   2 coins 1 credit
            |  |  | | |  1 1 1   1 coin  1 credit
            |  |  | | |
            |  |  | | |          coin switch 2
            |  |  0 0 0          1 coin  2 credits
            |  |  0 0 1          1 coin  3 credits
            |  |  0 1 0          1 coin  5 credits
            |  |  0 1 1          4 coins 5 credits
            |  |  1 0 0          3 coins 4 credits
            |  |  1 0 1          2 coins 3 credits
            |  |  1 1 0          2 coins 1 credit
            |  |  1 1 1          1 coin  1 credit
            |  |
            |  0                 coin play
            |  1                 free play
            |
            0                    normal
            1                    cocktail

```
