![Moon Patrol](MoonPatrol.jpg)

>>> deploy:<br>
>>>   +MoonPatrol.jpg<br>
>>>   +MoonPatrol.js<br>
>>>   Hardware.md<br>
>>>   RAMUse.md<br>
>>>   Code.md<br>
>>>   ----<br>
>>>   GFX1.md:GFX1 (Text)<br>
>>>   GFX2.md:GFX2 (Sprites)<br>
>>>   GFX3.md:GFX3 (Mountains)<br>
>>>   GFX4.md:GFX4 (Hills)<br>
>>>   GFX5.md:GFX5 (City)<br>
>>>   ImageBackgroundColors.md<br>
>>>   SpriteColors.md<br>
>>>   SpriteColorSets.md<br>
>>>   TextColors.md<br>
>>>   ----<br>
>>>   MoonPatrolSound.md<br>
>>>   SoundHardware.md<br>
>>>   SoundRAMUse.md<br>
>>>   SoundCode.md<br>
>>>   ----<br>
>>>   Journal.md<br>

# Moon Patrol

[See the discussion of the sound board](MoonPatrolSound.md)

# Code Links

* [Main Board Code](Code.md)
* [GFX1 Background Tiles](GFX1.md)
* [GFX2 Sprite Tiles](GFX2.md)
* [GFX3 Mountains Background](GFX3.md)
* [GFX4 Hills Background](GFX4.md)
* [GFX5 City Background](GFX5.md)
* [Text Color Sets](TextColors.md)
* [Image Background Colors](ImageBackgroundColors.md)
* [Sprite Colors](SpriteColors.md)
* [Sprite Color Sets](SpriteColorSets.md)
* [Hardware](Hardware.md)
* [RAM Usage](RAMTable.md)

# Luna City

You are a police officer patrolling Luna City's Sector Nine -- home of the "toughest thugs in the galaxy".

## The Service Mode

The last 3K (20%) of the main program is a service-mode routine that executes on startup if the service-mode DIP switch is enabled. The routine 
performs an extensive RAM test and verifies the checksum of all 4 ROM chips. Unfortunately, the routine itself is in the last ROM chip and the 
jump to it is in the first ROM chip. Ideally the routine would be in the first chip with its jump. Then it could function if only the first ROM 
chip was good. As it is the first and last chips must be good.

Once the RAM/ROM tests are complete, the service-mode routine falls into an interactive hardware test menu. This menu has several sub-menus that 
allow you to test sound effects, read the DIP switches, test inputs, and test character and sprite hardware. This is a great find for a computer 
archeologist because it gives you small code routines that focus on individual aspects of hardware. You can easily modify these small code routines 
to write different values to the hardware thus tinkering with the hardware to figure out how it behaves.

This 3K area also gives you a large area of ROM to write your own code to replace game routines when you are experimenting. Normally you would have to 
look for smaller sections of code scattered around the program.

## Coin Modes

Moon Patrol has a complex, configurable pricing scheme. The DIP switches allow the owner to configure how many coins it takes for one game (1 through 7) 
or how many games you get for one coin (1 through 8).

The owner can even configure two different currency slots. One slot could take quarters while another could take pesos. Each slot would have its own 
pricing scheme thus allowing the owner to configure his or her own conversion rate between quarters and pesos.

I can't imagine this dual slot mode was used very often. Arcades solved the currency problem on their own by selling tokens. Most of the games in the
 arcade lacked this fine-grain level of price configuration, and certainly there was no standard. The usual standard was one-coin-for-one-game with a 
 few popular/expensive games requiring two coins to play.

## State Machines

The entire code is driven by two state machines. The ISR state machine processes 32 fixed game objects with every vertical blank. These are the obvious 
game objects: the moon-buggy, the alien ships, and the shots.

The main-loop state machine processes a dynamic list of up to 63 "text" commands. These are always "text" commands that affect the background tile memory.

The game loop begins at 026E with a number of regular function calls made every pass. Then at 0283 all (if any) text-objects run. Meanwhile, the ISR tasks 
interrupt the main loop and run every vertical blank. The main loop, which is free running, uses the ISR counters for timing.

```plainCode
; Main loop
;
026E: CD DC 0D       CALL  $0DDC              ; ?? Change terrain
0271: CD 0D 21       CALL  $0D21              ; Draw "point letter" in upper center status window
0274: CD 3A 1B       CALL  $1B3A              ; ?? Start UFO shot
0277: CD C7 1B       CALL  $1BC7              ; ?? Init aliens
027A: CD A7 12       CALL  $12A7              ; ?? Alien sounds
027D: CD E7 12       CALL  $12E7              ; ??
0280: CD DC 0D       CALL  $0DDC              ; ?? Change terrain
;
;RunTxtCmds
; Run the list of text commands from start to finish
;
0283: 3A CF E1       LD    A,($E1CF)          ; LSB of head of text command list
;
0286: 21 D0 E1       LD    HL,$E1D0           ; Next available text command pointer * J02AB
0289: BE             CP    (HL)               ; Have we reached the end of the list?
028A: 28 E2          JR    Z,$26E             ; Yes ... back to the top
;
```

## Text Commands (Main loop objects)

The dynamic "main loop" objects are kept in memory from E300 to E3FF. Objects are added to the tail of a circular list and removed from the head 
as they finish. Each object structure is four bytes.

The first byte selects the code to run to handle this object. The byte is an index into a jump table of 11 possible routines. The first routine 
is numbered 1, and 0 means the object is finished and will be removed from the list.

The second byte of the object structure is a parameter value. Some of the handler routines need additional information. For instance, the first 
routine (Adjust Score) needs to know what value to add to the player's score.

The third and fourth bytes are a pointer to a text string to draw or erase by the handler routine. This "string" is much more than a simple 
copy-to-memory list of characters. There are special command bytes that set the color and add repeated characters (used for spacing). The text 
system is discussed below.

```plainCode
;TxtCmdTable
02D5: 22 06 ; 0622 01 TxtCmd_01 Adjust Score
02D7: FA 02 ; 02FA 02 TxtCmd_02 Run text script
02D9: ED 02 ; 02ED 03 TxtCmd_03 Set timer for next run and run script
02DB: 22 03 ; 0322 04 TxtCmd_04 Run the text-script if it is time
02DD: 2F 03 ; 032F 05 TxtCmd_05 Run the text-script but erase it from screen
02DF: 67 03 ; 0367 06 TxtCmd_06 Init flashing-text process (transition to 7)
02E1: 61 03 ; 0361 07 TxtCmd_07 Flashing-text draw state (transitions to 8)
02E3: 37 03 ; 0337 08 TxtCmd_08 Flashing-text erase state (transitions to 7 or dies after X loops)
02E5: A6 0D ; 0DA6 09 TxtCmd_09 Open crater in ground when alien shot hits
02E7: 01 12 ; 1201 0A TxtCmd_0A Init "MOON PATROL" splash sequence
02E9: 18 12 ; 1218 0B TxtCmd_0B Run "MOON PATROL" splash sequence
```

## Text Scripting 
To Do

## ISR Game Objects 

Moon Patrol supports 32 game objects in memory from E300 to E3FF. Each object is 16 bytes. Most of the objects map directly to hardware sprites. 
The player air shots, however, (ISR Objects 3, 4, 5, and 6) are drawn on the background text screen.

The first byte of each object is the index into the object handler functions (1 through 49). A value of 0 means the object is inactive. The second 
byte (index 01) is an index into the sprite memory for the object. A sprite slot is 4 bytes and the entire sprite memory is copied from RAM into the 
hardware at once.

Most objects are not one sprite but a collection of sprites drawn in a grid. The moon buggy, for instance, is a grid of 2x2 sprites all drawn next 
to each other. ISRObject 0 is the one object that controls the moon buggy. The second byte (index 01) in ISRObject 0 points to the first sprite of 
four sprites drawn together to make the buggy.

The ISRObjects do not encapsulate the sprite geometry. Instead, the byte at index 0D of each ISRObject indexes into a table 2E18 that describes the 
graphics. Each entry in this graphics-object table is 4 bytes.

The first byte of each graphics object is the base tile number for the graphics. The second byte is the flip-bits and color-set applied to each tile 
in the grid. The third byte is yet another pointer ... this one to a drawing function for the graphics object. Graphics objects with similar geometry 
share drawing functions. For instance, all of the objects that ride the ground (boulders, rocks, and exploding versions of each) all use the same 
drawing function.

Most sprites change over time. The player's forward shot, for instance, flips between two tile pictures giving it animation as it crosses the screen. 
The buggy wheel flips between two images making it look like it is spinning.

There is no common strategy for animating sprites. Sometimes the different animations have different graphics-objects and the ISRObject switches among 
them. This is how the player's forward shot works. ISRObject 20 switches between graphics objects 09 and 0A as it moves the shot forward.

The buggy wheel, however, is animated by the drawing routine instead of the ISRObject. Graphics object 16 (the wheel) picks the tile number to draw 
based on the timer value.
