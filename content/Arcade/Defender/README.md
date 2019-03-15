![Defender](Defender.jpg)

>>> deploy:<br>
>>>  RAMUse.md<br>
>>>  Hardware.md<br>
>>>  Bank1.md<br>
>>>  Bank2.md<br>
>>>  Bank3.md<br>
>>>  Bank7.md<br>
>>>  BankFixed.md<br>
>>>  Mapping.txt<br>
>>>  SoundHardware.md<br>
>>>  SoundRAMUse.md<br>
>>>  SoundCode.md<br>
>>>  Defender-Theory-Early.pdf<br>
>>>  Defender-Theory-Later.pdf<br>
>>>  Defender.CPU.jpg<br>
>>>  +Defender.jpg<br>
>>>  Defender.ROM.B&W.jpg<br>
>>>  Defender.Vid.B&W.jpg<br>
>>>  SoundROM.txt<br>

# Defender

Harry Hurst is working on this dig.

# Code Links

* [Main Board RAM Use](RAMUse.md)
* [Main Board Hardware](Hardware.md)
* [Bank 1 Code](Bank1.md)
* [Bank 2 Code](Bank2.md)
* [Bank 3 Code](Bank3.md)
* [Bank 7 Code](Bank7.md)
* [Fixed ROM Code](BankFixed.md)
* [Sound Board Code](SoundCode.md)
* [Sound Board RAM Use](SoundRAMUse.md)
* [Sound Board Hardware Info](SoundHardware.md)

# Memory and ROM Banks

Memory $D000 - $FFFF is always ROM. The 6809 vectors are at the end of the map from $FFF0 - $FFFF. All the vectors point to 
the RESET address except for the IRQ vector.

Memory $0000 - $BFFF is always RAM. The screen memory consumes 0000 - $9FFF. The remainder $A000 - $BFFF is general purpose RAM. 
The stack pointer is initialized to BFFF.

Memory $C000 - $CFFF is bank switched by writing the bank number to ROM address $D000.

Bank 0 is the I/O space and CMOS RAM (high score table). Banks 1, 2, and 3 are full 4K banks of code and data. Banks 4, 5, 
and 6 have no chips to back them. Bank 7 is a small 2K bank.

The RESET vector points to $F61F (in fixed ROM). This is where Defender begins at power up.
