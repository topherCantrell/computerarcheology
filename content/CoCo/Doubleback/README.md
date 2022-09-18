![Doubleback](doubleback.jpg)

# Doubleback

>>> deploy:<br>
>>>   +doubleback.jpg<br>
>>>   +doubleback.js<br>
>>>   RAMUse.md<br>
>>>   %Code.md<br>
>>>   ----<br>
>>>   Journal.md<br>

This game runs on the original 4K Color Computer. The 128x96 screen buffer takes 3K of that
RAM. There is only one screen -- no double buffering. 

The code is not interrupt driven. It runs as one long loop that synchronizes to the screen
refresh VBLANK at the end of every loop.

At 4K, it fits in half the memory space allocated to the cartridge.

This is one of the first ROMs I disassembled in my youth. Way back in highschool I poured
through the tractor-feed printout. I didn't comment the whole thing back then, but I did
find the algorithm for checking objects for being looped. The check seemed to be incomplete
allowing "U"s around an object to count as loops. Sure enough, the running code proved
my theory.

Only now, decades later, have I finished the disassembly. I am amazed that my younger self
was able to spot the looping-"U" glitch.

>>> tourGuide {

    # Tour Guide

    The splash screen includes a cursive "double back" written pixel by pixel. Have a look at the
    datastructure with an interactive slow-motion drawing: [Cursive Double Back](Code.html#the-cursive-doubleback-text)

    Here are the graphics for numbers (scores): [Digit Graphics](Code.html#digit-graphics)
    
    Have a look at all the game objects: [Game Object Graphics](Code.html#game-objects)

    There are several text areas for messages show during the game. These are not drawn as tiled areas instead of individual letter graphics: [Text Area Graphics](Code.html#text-areas)

    The game manual says: "Warning: After 10 skulls, beware of the unexpected!". It refers to a fast moving "X" object that appears
    after 10 skulls. Here is the code that create it: [The Unexpected](Code.html#the-unexpected)

    The code to check if an object is looped is not very sophisticated. The player can make a "U" shape around the objects instead of looping. Here is the loop-check code: [Loop Check](Code.html#looped-object-detection)

    A single audio routine generates the "dirty tone" effect used in all three songs (1 for each life), the end-of-life tone, and the object appearing pop: [Play Song](Code.html#play-song)

    The songs themselves are in lists of words beginning here: [Song Data](Code.html#songs)

>>> }
