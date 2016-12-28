# Journal

## 12/28/2016

Daggorath for the holidays! I whipped up a 6809 disassembly runner and mapped out the levels. The output is
an SVG file. I am having trouble calculating the starting positions of the monsters. I patched the code
and played in mocha.jar. I prevented the monsters from moving and started with a seer scroll. Thus I could
walk through the levels and manually map creatures and what they hold. But I can't get the software to
produce what I see in the walkthrough. Frustrating.

## 4/24/2016

Mark McDougall asked about Space Invaders RAM initialization. It looks like 0x1FF is not initialized before
it is read in the demo screen. The code blows up if it is bad.

I added the SpaceInvaders simulator code to the project. Sure enough. Read before written. I am checking
with Gary to see if that the TMS4060 powers up to all zeros.

## 12/30/2015

I wrote a graphics-processor disassembler to make better comments in the picture data. Lots
of little cleans and comments all over the place. This is some wonderful code.

## 12/27/2015

I wish I had been keeping this journal over the years. I don't know why I didn't think of it until now.

I have been working on a development cartridge for the gameboy in another repository. As part of that
I disassembled the Zelda cartridge for Computer Archeology. I made a javascript module to display
Gameboy tiles.

The week between Christmas and New Years is always Dungeons of Daggorath time. I'm sure I'll make some
progress in that disassembly -- getting the hand-commented code off of paper and into electronic form
here.

