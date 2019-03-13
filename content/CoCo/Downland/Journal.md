![Journal](../../img/journal.jpg)

# Journal

## 3/13/2019

I updated the content to the latest markdown format.

## April 21, 2018

Getting a clean binary from the actual cartridge I bought on ebay. I put a piece of tape over the cart interrupt.
The first byte is 0x12, as one of my images shows. Maybe that image is correct? Let me run a checksum and see.

On the CoCo I got 787090 from C000 to DFFF. I wonder if the cartridge goes into the E000s. Surely not. But the
cartridge does use A13 and A14. Hmmm. C000 to DFFF only needs A0-A12. I will have to take the cartridge apart.

The checksum of my binary matches 787090. I'm going to say they are the same.

Now for this above-E000 stuff.

I ran a loop. There is data up there. Without the cartridge, the loop prints 255s. With the cartridge there
is stuff.

The stuff appears to go right up FF00 (E000-FEFF).

Ah ha! The pins on the cartridge connector go nowhere. I checked the "stuff". It is just a ghost of C000-DFFF.
Good. The cartridge is standard 8K, and I have the binary.

## April 14, 2018

I can't find any info on what happens when you finish the game. I guess I'll look at the 
code to find the answer.
