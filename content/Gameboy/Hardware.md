![Hardware](GBZelda.jpg)

# Hardware

 * 0000-3FFF : Fixed ROM bank (8K)
 * 4000-7FFF : Bank-switched ROM (8K)
 * 8000-9FFF : VRAM (tiles, palettes, maps)
 * A000-BFFF : Space for cartridge RAM, if any, which might be battery-backed
 * C000-FEFF : Main RAM
 * FF00-FFFF : I/O ports and high RAM

# Bank Switchers

There were several on-cartridge chips to manage cartridge memory bank switching
(RAM and ROM).

MB1: write anywhere from 2000-3FFF to select a ROM bank at 4000-7FFF. The value
written is the bank number. Write anywhere from 4000-5FFF selects a RAM bank from
A000-C000.

# VRAM

TODO describe formats, windows, etc

 * 8000-97FF : Character RAM 
 * 9800-9BFF : BG Map Data 1 
 * 9C00-9FFF : BG Map Data 2 
 * FE00-FE9F : Object Attribute Memory

# I/O Ports and High RAM

FF80-FFFE is an area of RAM called High RAM -- HRAM.

>>>memory

| | | |
| --- | --- | --- |
| FF00 | JOYPAD       | Joypad port  |  
| FF01 | SIODATA      | Serial I/O Data  |  
| FF02 | SIOCNT       | Serial I/O Control  |  
| FF04 | DIVIDER      | Meaning unknown  |   
| FF05 | TIMECNT      | Timer Counter  |   
| FF06 | TIMERMOD     | Timer Modulo  |   
| FF07 | TIMERCONT    | Timer Control  |   
| FF0F | IFLAGS       | Interrupt Flags  |   
| FF10 | SNDREG10     | Sweep  #1 |   
| FF11 | SNDREG11     | Sound length/pattern duty  #1 |   
| FF12 | SNDREG12     | Control  #1 |   
| FF13 | SNDREG13     | Frequency low #1 |   
| FF14 | SNDREG14     | Frequency high  #1 |   
| FF16 | SNDREG21     | Sound length/pattern duty  #2 |   
| FF17 | SNDREG22     | Control  #2 |   
| FF18 | SNDREG23     | Frequency low  #2 |   
| FF19 | SNDREG24     | Frequency high  #2 |   
| FF1A | SNDREG30     | Control  #3 |   
| FF1B | SNDREG31     | Sound length  #3 |   
| FF1C | SNDREG32     | Output level  #3 |  
| FF1D | SNDREG33     | Frequency low  #3 |   
| FF1E | SNDREG34     | Frequency high #3 |   
| FF20 | SNDREG41     | Sound length/pattern duty #4 |   
| FF21 | SNDREG42     | Control #4  |   
| FF22 | SNDREG43     | Polynomial counter #4 |   
| FF23 | SNDREG44     | Frequency high #4  |   
| FF24 | SNDREG50     | Channel and volume control |   
| FF25 | SNDREG51     | Sound output terminal selector |   
| FF26 | SNDREG52     | Sound on/off  |   
| FF40 | LCDCONT      | LCD control |   
| FF41 | LCDSTAT      | LCD status |   
| FF42 | SCROLLY      | Background vertical scrolling |   
| FF43 | SCROLLX      | Background horizontal scrolling |   
| FF44 | CURLINE      | Current scanline |   
| FF45 | CMPLINE      | Scanline comparison |   
| FF47 | BRGDPAL      | Background palette |   
| FF48 | OBJ0PAL      | Sprite palette #0 |   
| FF49 | OBJ1PAL      | Sprite palette #1 |   
| FF4A | WNDPOSY      | Window Y position |   
| FF4B | WNDPOSX      | Window X position |   
| FFFF | ISWITCH      | Interrupt Enable/Disable | 

