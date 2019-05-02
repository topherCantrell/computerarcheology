![Madness and the Minotaur](Madness.jpg)

# Walkthrough of my Game 

This is the description of my game experience played using the saved-game info below. 
You can duplicate my steps with my file:

  * [first.cas](first.cas) (For mocha emulator) 
  * [first.txt](first.txt) (For emulator on this page)
  * [Save Game Viewer](SaveGameViewer.html?file=first.txt) (Open in save-game-viewer)

## TASK 1: LEARN VETAR 

```
SOUTH         ; This is room with music where SPRITE can't go

GET FOOD  
NORTH
GET LAMP
LAMP ON

EAST EAST SOUTH SOUTH SOUTH WEST
JUMP HOLE
SOUTH EAST EAST EAST EAST EAST DOWN DOWN 
NORTH         ; 50/50 chance of this failing and putting you in a random room in the maze.
NORTH         ; Magic spell might push you back. Took me several tries.
NORTH
GET MUSHROOM
JUMP PIT
WEST NORTH EAST UP
UP            ; Took me several tries. It helps to be light as possible.
WEST SOUTH WEST WEST SOUTH SOUTH 
EAST          ;  _u ... GOLD appears
GET GOLD
NORTH         ; Now know VETAR

SOUTH WEST NORTH NORTH WEST WEST SOUTH

; Drop our objects in room with music where SPRITE can't move them.

DROP FOOD
DROP MUSHROOM
DROP GOLD
```
[s_one.cas](s_one.cas) [s_one.txt](s_one.txt)

## TASK 2: LEARN MITRA 

```
NORTH EAST EAST SOUTH SOUTH SOUTH WEST
JUMP HOLE
SOUTH DOWN DOWN DOWN EAST NORTH EAST EAST NORTH EAST EAST NORTH NORTH NORTH WEST SOUTH WEST
GET PARCHMENT

NORTH WEST WEST WEST
JUMP DOWN

NORTH NORTH WEST SOUTH WEST WEST SOUTH WEST
JUMP HOLE

WEST WEST
NORTH         ; Took several tries
DOWN NORTH NORTH EAST

NORTH WEST UP SOUTH EAST EAST SOUTH
DROP PARCHMENT
```
[s_two.cas](s_two.cas) [s_two.txt](s_two.txt)

## TASK 3: LEARN OKKAN 

```
NORTH EAST EAST SOUTH SOUTH SOUTH WEST
JUMP HOLE
SOUTH DOWN DOWN DOWN
GET TALISMAN

EAST NORTH EAST EAST NORTH EAST EAST NORTH NORTH NORTH WEST SOUTH WEST NORTH WEST WEST WEST
JUMP DOWN

NORTH NORTH WEST SOUTH WEST WEST SOUTH WEST NORTH WEST WEST
DOWN          ; LEARN OKKAN 
UP EAST EAST SOUTH EAST NORTH NORTH NORTH WEST WEST SOUTH

DROP TALISMAN
```
[s_three.cas](s_three.cas) [s_three.txt](s_three.txt)

## TASK 4: Get the SWORD and SHIELD 

```
GET PARCHMENT
NORTH WEST WEST NORTH DOWN
JUMP PIT
SOUTH SOUTH

GET SWORD

JUMP
WEST WEST WEST UP UP SOUTH SOUTH
DROP PARCHMENT
NORTH NORTH EAST EAST EAST

GET SHIELD
```
[s_four.cas](s_four.cas) [s_four.txt](s_four.txt)

## TASK 5: Get the ROPE and learn AKHIROM

```
WEST WEST WEST SOUTH SOUTH
DROP SWORD
DROP SHIELD
NORTH EAST EAST SOUTH SOUTH SOUTH WEST
JUMP HOLE
SOUTH DOWN DOWN DOWN EAST NORTH EAST NORTH EAST EAST EAST NORTH 
NORTH NORTH WEST SOUTH WEST NORTH WEST
GET ROPE

WEST WEST
JUMP DOWN
NORTH NORTH WEST NORTH WEST WEST WEST WEST WEST WEST NORTH DOWN EAST
SOUTH WEST SOUTH SOUTH SOUTH EAST EAST EAST

NORTH         ; Now know AKHIROM

SOUTH WEST WEST WEST NORTH NORTH NORTH NORTH UP SOUTH EAST EAST SOUTH
DROP ROPE
```
[s_five.cas](s_five.cas) [s_five.txt](s_five.txt)

## TASK 6: Get the SCEPTER and learn NERGAL 

```
NORTH EAST EAST SOUTH SOUTH SOUTH WEST
JUMP HOLE
SOUTH DOWN DOWN DOWN EAST NORTH EAST NORTH

GET SCEPTER

EAST EAST EAST NORTH NORTH NORTH
WEST SOUTH WEST NORTH WEST WEST WEST

JUMP DOWN

NORTH NORTH WEST NORTH WEST WEST 
WEST WEST WEST WEST NORTH DOWN

JUMP PIT
SOUTH

; I had to wait here for several shakings to open the passage south

SOUTH
JUMP          ; Now know NERGAL

DROP SCEPTER

JUMP PIT
JUMP PIT      ; Jumping into the treasure room
DOWN
SOUTH
```
[s_six.cas](s_six.cas) [s_six.txt](s_six.txt)

## TASK 7: Get VIAL, BELROG, and CROM 

```
GET MUSHROOM
NORTH WEST WEST NORTH DOWN

JUMP PIT
SOUTH SOUTH
JUMP

GET VIAL 

JUMP PIT
JUMP PIT      ; Jumping into the treasure room
DOWN WEST WEST NORTH DOWN EAST SOUTH EAST EAST EAST
NORTH EAST EAST
JUMP DOWN

VETAR         ; Random chance ... I had to recover the lamp
LAMP ON

EAST SOUTH
SOUTH         ; Now know BELROG

; Had to wait on a couple of shakes here to unblock north

NORTH NORTH
GET PENDANT

SOUTH SOUTH EAST DOWN EAST NORTH NORTH NORTH WEST SOUTH
WEST NORTH WEST WEST WEST WEST WEST SOUTH SOUTH SOUTH
EAST SOUTH EAST NORTH NORTH EAST
EAST          ; Now know CROM

NORTH WEST
DROP PENDANT
JUMP PIT
DOWN SOUTH
```
[s_seven.cas](s_seven.cas) [s_seven.txt](s_seven.txt)

## TASK 8: Learn ISHTAR

TO BE DONE

# Save-Game Analysis 

Save-game analysis for 'first.cas' 

## Map 

```html
<pre>
<span style="font-size: 8px">                                                                                                                                                                                   
Floor 1                                                                                                                                                                                                            
                                                                                                                                                                                                                   
                                                                                                                                                                                                                   
                                                                                                                                                                                                                   
        +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+              
        |0                  |   |1                  |   |2                  |   |3                  |   |4                  |   |5                  |   |6                  |   |7                  |              
        |             D:64D |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |             D:71A |              
        |                   |   |       O           |   |                   |   |                   |   |                   |   |                   |   |       P           |   |                   |              
        |                   |   |                   +---+                   +---+                   +---+                   +---+                   |   |                   |---+                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   | *SPELLBOOK        |   | *SHIELD           |   |                   |   |                   |              
        +---------+---------+   +-------------------+   +---------+---------+   +-------------------+   +-------------------+   +---------+---------+   +---------+---------+   +-------------------+              
                  |                                               |                                                                       |                       |                                                
                  |                                               |                                                                       |                       |                                                
                  |                                               |                                                                       |                       |                                                
        +---------+---------+   +-------------------+   +---------+---------+   +-------------------+   +-------------------+   +---------+---------+   +---------+---------+   +-------------------+              
        |8                  |   |9                  |   |10                 |   |11                 |   |12                 |   |13                 |   |14                 |   |15              _c |              
        |                   |   |                   |   | U:202C            |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |       @           |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   +---+                   +---+                   +---+                   +---+                   +---+                   +---+                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   | LAMP              |   |                   |   |                   |   |                   |   |                   |   | DAGGER            |              
        +-------------------+   +-------------------+   +---------+---------+   +-------------------+   +---------+---------+   +-------------------+   +---------+---------+   +---------+---------+              
                                          |                       |                                               |                                               |                       |                        
                                          |                       |                                               |                                               |                       |                        
                                          |                       |                                               |                                               |                       |                        
        +-------------------+   +---------+---------+   +---------+---------+   +-------------------+   +---------+---------+   +-------------------+   +---------+---------+   +---------+---------+              
        |16                 |   |17              _o |   |18              _z |   |19                 |   |20                 |   |21   V             |   |22                 |   |23                 |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        | J:POOL:17:128F    |   | J:POOL:16:128F    |   |                   |   |                   +---+                   |   |                   |   |                   +---+                   |              
        | j:17              |   | j:16              |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        | BOTTLE            |   |                   |   | FOOD              |   |                   |   |                   |   |                   |   |                   |   |                   |              
        +---------+---------+   +-------------------+   +---------+---------+   +-------------------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+              
                  |                                               |                                               |                       |                       |                       |                        
                  |                                               F                                               |                       |                       |                       |                        
                  |                                               |                                               |                       |                       |                       |                        
        +---------+---------+   +-------------------+   +-------------------+   +-------------------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+              
        |24              _p |   |25                 |   |26                 |   |27                 |   |28                 |   |29              _u |   |30                 |   |31                 |              
        |              D:88 |   |             D:89A |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   +---+                   +---+                   |   |                   +---+                   +---+                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        +---------+---------+   +-------------------+   +-------------------+   +---------+---------+   +---------+---------+   +-------------------+   +-------------------+   +---------+---------+              
                  |                                                                       |                       |                                                                       |                        
                  |                                                                       |                       |                                                                       |                        
                  |                                                                       |                       |                                                                       |                        
        +---------+---------+   +-------------------+   +-------------------+   +---------+---------+   +---------+---------+   +-------------------+   +-------------------+   +---------+---------+              
        |32             _32 |   |33             _33 |   |34                 |   |35                 |   |36                 |   |37                 |   |38                 |   |39                 |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |             D:102 |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   +---+                   +---+ J:PIT:35:120S(20) |   | J:HOLE:34:150S(40)+---+                   +---+                   +---+                   |   |                   |              
        |                   |   |                   |   | j:35              |   | j:34              |   |                   |   |                   |   | j:102             |   | j:194             |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        +-------------------+   +-------------------+   +---------+---------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+              
                                                                  |                                                                                                                                                
                                                                  |                                                                                                                                                
                                                                  |                                                                                                                                                
        +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+              
        |40                 |   |41                 |   |42                 |   |43                 |   |44                 |   |45                 |   |46                 |   |47                 |              
        | U:232       D:104 |   | U:233       D:105 |   | U:234       D:106 |   | U:235       D:107 |   | U:236       D:108 |   | U:237       D:109 |   | U:238       D:110 |   | U:239       D:111 |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   +---+                   +---+                   +---+                   +---+ J:PIT:182:10S(10) +---+                   +---+                   +---+                   +--- 48        
        |                   |   |                   |   |                   |   |                   |   | j:182             |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   | *TRUTHRING        |   |                   |   |                   |   |                   |              
        +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+              
                  |                       |                       |                       |                       |                       |                       |                       |                        
                  |                       |                       |                       |                       |                       |                       |                       |                        
                  |                       |                       |                       |                       |                       |                       |                       |                        
        +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+              
        |48                 |   |49                 |   |50                 |   |51                 |   |52                 |   |53                 |   |54                 |   |55                 |              
        | U:240       D:112 |   | U:241       D:113 |   | U:242       D:114 |   | U:243F      D:115 |   | U:244       D:116 |   | U:245       D:117 |   | U:246       D:118 |   | U:247       D:119 |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
  47 ---+                   +---+                   +---+                   +---+                   +---+                   +---+                   +---+                   +---+                   +--- 56        
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+              
                  |                       |                       |                       |                       |                       |                       |                       |                        
                  |                       |                       |                       |                       |                       |                       |                       |                        
                  |                       |                       |                       |                       |                       |                       |                       |                        
        +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+              
        |56                 |   |57                 |   |58                 |   |59                 |   |60                 |   |61                 |   |62              _r |   |63                 |              
        | U:248       D:120 |   | U:249       D:121 |   | U:250       D:122 |   | U:251       D:123 |   | U:252       D:124 |   | U:253       D:125 |   | U:254       D:126 |   | U:255       D:127 |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
  55 ---+                   +---+                   +---+                   +---+                   +---+                   +---+                   +---+                   +---+                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+              
                                                                                                                                                                                                                   
                                                                                                                                                                                                                   

                                                                                                                                                                                                                   
Floor 2                                                                                                                                                                                  63                        
                                                                                                                                                                                          |                        
                                                                                                                                                                                          |                        
                                                                                                                                                                                          |                        
        +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +---------+---------+              
        |64                 |   |65                 |   |66                 |   |67                 |   |68                 |   |69                 |   |70              _f |   |71              _s |              
        | U:0D              |   |                   |   | U:2A              |   |                   |   | U:4D              |   |                   |   |                   |   | U:7A       D:135D |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |       N           |   |                   |              
        | J:PIT:128:30D     +---+                   |   |                   +---+                   |   |                   +---+                   +---+ J:DOWN:140:80S(20)|   |                   |              
        | j:128             |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   | *SKULL            |   | URN               |   |                   |   | FLUTE             |   |                   |   |                   |   |                   |              
        +-------------------+   +---------+---------+   +-------------------+   +---------+---------+   +---------+---------+   +-------------------+   +---------+---------+   +-------------------+              
                  |                       |                                               |                       |                       |                       |                                                
                  |                       |                                               |                       |                       C                       |                                                
                  |                       |                                               |                       |                       |                       |                                                
        +---------+---------+   +---------+---------+   +-------------------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +-------------------+              
        |72              _v |   |73   M             |   |74                 |   |75                 |   |76                 |   |77              _q |   |78              _q |   |79                 |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   +---+                   +---+                   +-A-+                   +---+                   |   |                   |   | J:CHASM:86:64F    |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   | j:86              |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        +---------+---------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +---------+---------+   +-------------------+   +---------+---------+              
                  |                                                                                                                       |                                               |                        
                  |                                                                                                                       |                                               |                        
                  |                                                                                                                       |                                               |                        
        +---------+---------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +---------+---------+   +-------------------+   +---------+---------+              
        |80              _h |   |81              _n |   |82                 |   |83                 |   |84                 |   |85                 |   |86                 |   |87                 |              
        |                   |   |                   |   |                   |   | U:19E             |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |       S           |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   +---+                   +---+                   +-A-+                   +---+                   |   | J:CHASM:78:64F    +---+                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   | j:78              |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        +---------+---------+   +-------------------+   +-------------------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+              
                  |                                                                       |                       |                       |                       |                       |                        
                  |                                                                       |                       |                       |                       |                       |                        
                  |                                                                       |                       |                       |                       |                       |                        
        +---------+---------+   +-------------------+   +-------------------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+              
        |88                 |   |89   O             |   |90                 |   |91   A             |   |92                 |   |93                 |   |94                 |   |95                 |              
        |                   |   | U:25A      D:153A |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   +---+                   |   | J:DOWN:156:150S(30)   |                   +---+ J:DOWN:158:90S(10)|   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        +---------+---------+   +-------------------+   +-------------------+   +---------+---------+   +-------------------+   +-------------------+   +-------------------+   +---------+---------+              
                  |                                                                       |                                                                                               |                        
                  |                                                                       |                                                                                               |                        
                  |                                                                       |                                                                                               |                        
        +---------+---------+   +-------------------+   +-------------------+   +---------+---------+   +-------------------+   +-------------------+   +-------------------+   +---------+---------+              
        |96                 |   |97                 |   |98                 |   |99                 |   |100             _x |   |101                |   |102                |   |103                |              
        |                   |   |             D:161 |   |                   |   |                   |   |                   |   |                   |   |             D:166 |   |             D:167 |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   +---+                   +---+                   +---+                   +---+                   +---+                   +---| J:UP:38:160F      |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   | j:166             |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+              
                                          |                                                                                                                                                                        
                                          H                                                                                                                                                                        
                                          |                                                                                                                                                                        
        +-------------------+   +---------+---------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+              
        |104                |   |105                |   |106                |   |107                |   |108                |   |109                |   |110                |   |111                |              
        | U:40        D:168 |   | U:41        D:169 |   | U:42        D:170 |   | U:43        D:171 |   | U:44        D:172 |   | U:45        D:173 |   | U:46        D:174 |   | U:47        D:175 |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   +-I-+                   +-I-+                   +---+                   +---+                   +---+                   +---+                   +---+                   +--- 112       
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+              
                  |                       |                       |                       |                       |                       |                       |                       |                        
                  |                       |                       |                       |                       |                       |                       |                       |                        
                  |                       |                       |                       |                       |                       |                       |                       |                        
        +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+              
        |112                |   |113                |   |114                |   |115                |   |116                |   |117                |   |118                |   |119                |              
        | U:48        D:176 |   | U:49        D:177 |   | U:50        D:178 |   | U:51        D:179 |   | U:52        D:180 |   | U:53        D:181 |   | U:54        D:182 |   | U:55        D:183 |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
 111 ---+                   +---+                   +---+                   +---+                   +---+                   +---+                   +---+                   +---+                   +--- 120       
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+              
                  |                       |                       |                       |                       |                       |                       |                       |                        
                  |                       |                       |                       |                       |                       |                       |                       |                        
                  |                       |                       |                       |                       |                       |                       |                       |                        
        +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+              
        |120                |   |121                |   |122             _b |   |123                |   |124             _a |   |125                |   |126                |   |127                |              
        | U:56        D:184 |   | U:57        D:185 |   | U:58        D:186 |   | U:59        D:187 |   | U:60        D:188 |   | U:61        D:189 |   | U:62        D:190 |   | U:63        D:191 |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
 119 ---+                   +---+                   +---+                   +---+                   +---+                   +---+                   +---+                   +---+                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+              



                                                                                                                                                                                                                   
Floor 3                                                                                                                                                                                                            
                                                                                                                                                                                                                   
                                                                                                                                                                                                                   
                                                                                                                                                                                                                   
        +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+              
        |128                |   |129                |   |130                |   |131                |   |132                |   |133  N             |   |134                |   |135                |              
        |                   |   |                   |   | U:66D             |   |                   |   |                   |   |                   |   |                   |   | U:71D             |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |       M           |   |                   |              
        | J:UP:64:100F      |   |                   +---+                   +---+                   +---+                   +---+ J:PIT:203:192F    |   |                   +---|                   |              
        | j:64              |   |                   |   |                   |   |                   |   |                   |   | j:144             |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   | BASKET            |   | *VIAL             |   |                   |   | *POWERRING,*LIGH~ |              
        +---------+---------+   +-------------------+   +---------+---------+   +-------------------+   +-------------------+   +-------------------+   +---------+---------+   +-------------------+              
                  |                                               |                                                                                               |                                                
                  |                                               |                                                                                               |                                                
                  |                                               |                                                                                               |                                                
        +---------+---------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +---------+---------+   +-------------------+              
        |136                |   |137                |   |138                |   |139                |   |140                |   |141             _t |   |142                |   |143                |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |       T           |   |       Y           |   |                   |   |                   |   |                   |              
        |                   |   |                   +---+                   +-G-+                   +---+                   +---+                   |---+                   |---+ J:PIT:151:128D    |              
        |                   |   |                   |   |                   |   |                   |   | j:70              |   |                   |   |                   |   | j:151             |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   | AX                |   |                   |   |                   |   |                   |   | PENDANT           |   | MACE              |   |                   |              
        +---------+---------+   +---------+---------+   +---------+---------+   +-------------------+   +-------------------+   +---------+---------+   +---------+---------+   +-------------------+              
                  |                       |                       |                                                                       |                       |                                                
                  |                       |                       |                                                                       |                       |                                                
                  |                       |                       |                                                                       |                       |                                                
        +---------+---------+   +---------+---------+   +---------+---------+   +-------------------+   +-------------------+   +---------+---------+   +---------+---------+   +-------------------+              
        |144                |   |145                |   |146                |   |147                |   |148                |   |149                |   |150                |   |151                |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   | U:86A             |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        | J::133:20S(20)    |   |                   |   |                   |   |                   +---+                   |   |                   |   |                   |   | J:PIT:143:128F    |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   | j:143             |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        | *SWORD            |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   | MUSHROOM          |              
        +-------------------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +-------------------+   +---------+---------+              
                                          |                       |                       |                       |                       |                                               |                        
                                          |                       |                       |                       |                       |                                               |                        
                                          |                       |                       |                       |                       |                                               |                        
        +-------------------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +-------------------+   +---------+---------+              
        |152                |   |153                |   |154                |   |155             _q |   |156             _l |   |157  B             |   |158                |   |159             _k |              
        |                   |   | U:89A             |   |                   |   |                   |   | U:92C             |   |                   |   |             D:222 |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   +---+                   +---+                   |   |                   +---+                   +---+                   +---|                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   | j:92              |   |                   |   | j:94              |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        +---------+---------+   +---------+---------+   +---------+---------+   +-------------------+   +---------+---------+   +-------------------+   +-------------------+   +---------+---------+              
                  |                       |                       |                                               |                                                                       |                        
                  |                       |                       |                                               |                                                                       |                        
                  |                       |                       |                                               |                                                                       |                        
        +---------+---------+   +---------+---------+   +---------+---------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +---------+---------+              
        |160                |   |161                |   |162                |   |163                |   |164                |   |165                |   |166             _f |   |167                |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   +---+                   +---+                   +---+                   +---+ J:PIT:202:160D    +---+                   |---+ J:UP:102:80F      |   |                   |              
        |                   |   |                   |   | j:202             |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        +-------------------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +-------------------+   +---------+---------+              
                                          |                       |                       |                       |                       |                                               |                        
                                          |                       |                       |                       |                       |                                               H                        
                                          |                       |                       |                       |                       |                                               |                        
        +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +---------+---------+              
        |168                |   |169                |   |170                |   |171                |   |172                |   |173                |   |174                |   |175                |              
        | U:104       D:232 |   | U:105       D:233 |   | U:106       D:234 |   | U:107       D:235 |   | U:108       D:236 |   | U:109       D:237 |   | U:110       D:238 |   | U:111       D:239 |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   +---+                   +---+                   +---+                   +---+                   +---+                   +---+                   +-I-+                   +-I- 176       
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+              
                  |                       |                       |                       |                       |                       |                       |                       |                        
                  |                       |                       |                       |                       |                       |                       |                       |                        
                  |                       |                       |                       |                       |                       |                       |                       |                        
        +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+              
        |176             _x |   |177                |   |178                |   |179                |   |180                |   |181                |   |182                |   |183                |              
        | U:112       D:240 |   | U:113       D:241 |   | U:114       D:242 |   | U:115      D:243F |   | U:116       D:244 |   | U:117       D:245 |   | U:118       D:246 |   | U:119       D:247 |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
 175 -I-+                   +---+                   +---+                   +---+                   +---+                   +---+                   +---+ J:PIT:44:20S(20)  +---+                   +--- 184       
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   | j:44              |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+              
                  |                       |                       |                       |                       |                       |                       |                       |                        
                  |                       |                       |                       |                       |                       |                       |                       |                        
                  |                       |                       |                       |                       |                       |                       |                       |                        
        +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+              
        |184                |   |185                |   |186                |   |187                |   |188                |   |189                |   |190                |   |191                |              
        | U:120       D:248 |   | U:121       D:249 |   | U:122       D:250 |   | U:123       D:251 |   | U:124       D:252 |   | U:125       D:253 |   | U:126       D:254 |   | U:127       D:255 |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
 183 ---+                   +---+                   +---+                   +---+                   +---+                   +---+                   +---+                   +---+                   +--- 192       
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+              
 
 
                                                                                                                                                                                                                 
                                                                                                                                                                                                                   
Floor 4                                                                                                                                                                                                            
                                                                                                                                                                                                                   
                                                                                                                                                                                                                   
                                                                                                                                                                                                                   
        +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+              
        |192             _i |   |193                |   |194           _203 |   |195                |   |196                |   |197                |   |198                |   |199            _32 |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   +---+                   +---+ J:DOWN:39:140F    +---+                   +---+                   +---+                   |   |                   +---+                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   | ROPE              |   |                   |   |                   |   |                   |              
        +---------+---------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +---------+---------+   +---------+---------+   +---------+---------+              
                  |                                                                                                                       |                       |                       |                        
                  |                                                                                                                       |                       |                       |                        
                  |                                                                                                                       |                       |                       |                        
        +---------+---------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +---------+---------+   +---------+---------+   +---------+---------+              
        |200             _j |   |201                |   |202                |   |203           _203 |   |204                |   |205                |   |206                |   |207             _q |              
        |                   |   |                   |   |             D:10B |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   +---+                   |   | J:DOWN:162:30S(20)|   | J:PIT:202:128S(30)+---+                   |   |                   +---+                   |   |                   |              
        |                   |   |                   |   | j:203             |   | j:133             |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   | PARCHMENT         |   |                   |   |                   |              
        +---------+---------+   +---------+---------+   +-------------------+   +-------------------+   +---------+---------+   +-------------------+   +-------------------+   +---------+---------+              
                  |                       |                                                                       |                                                                       |                        
                  |                       |                                                                       E                                                                       |                        
                  |                       |                                                                       |                                                                       |                        
        +---------+---------+   +---------+---------+   +-------------------+   +-------------------+   +---------+---------+   +-------------------+   +-------------------+   +---------+---------+              
        |208                |   |209                |   |210                |   |211             _d |   |212  C             |   |213           _213 |   |214                |   |215                |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   +---+                   |   |                   +---+                   +---+ J:MIST:213:70S(20)|   | J:MIST:212:70S(20)+---+                   +---+                   |              
        |                   |   |                   |   |                   |   |                   |   | j:213             |   | j:212             |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        +---------+---------+   +---------+---------+   +---------+---------+   +-------------------+   +-------------------+   +---------+---------+   +---------+---------+   +---------+---------+              
                  |                       |                       |                                                                       |                       |                       |                        
                  |                       |                       |                                                                       |                       |                       |                        
                  |                       |                       |                                                                       |                       |                       |                        
        +---------+---------+   +---------+---------+   +---------+---------+   +-------------------+   +-------------------+   +---------+---------+   +---------+---------+   +---------+---------+              
        |216                |   |217                |   |218                |   |219                |   |220             _e |   |221                |   |222                |   |223                |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   +---+                   |   |                   |   |                   +---+                   +---+                   +---+                   +---+                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   | SCEPTER           |   |                   |   |                   |   |                   |              
        +-------------------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+              
                                          |                       |                       |                       |                       |                       |                       |                        
                                          A                       |                       |                       |                       |                       |                       |                        
                                          |                       |                       |                       |                       |                       |                       |                        
        +-------------------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+              
        |224                |   |225                |   |226                |   |227                |   |228                |   |229                |   |230                |   |231                |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   +---+                   +---+                   |   |                   +---+                   +---+                   +---+                   +---+                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        +---------+---------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+              
                  |                                                                       |                                                                                                                        
                  G                                                                       |                                                                                                                        
                  |                                                                       |                                                                                                                        
        +-------------------+   +-------------------+   +-------------------+   +---------+---------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+              
        |232           _232 |   |233                |   |234                |   |235                |   |236                |   |237                |   |238                |   |239                |              
        | U:168        D:40 |   | U:169        D:41 |   | U:170        D:42 |   | U:171        D:43 |   | U:172        D:44 |   | U:173        D:45 |   | U:174        D:46 |   | U:175        D:47 |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   +---+                   +---+                   +---+                   +---+                   +---+                   +---+                   +---+                   +--- 240       
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   | TALISMAN          |   |                   |   |                   |   |                   |   |                   |   |                   |              
        +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+              
                  |                       |                       |                       |                       |                       |                       |                       |                        
                  |                       |                       |                       |                       |                       |                       |                       |                        
                  |                       |                       |                       |                       |                       |                       |                       |                        
        +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+              
        |240                |   |241                |   |242                |   |243                |   |244                |   |245                |   |246                |   |247                |              
        | U:176        D:48 |   | U:177        D:49 |   | U:178        D:50 |   | U:179F      D:51F |   | U:180        D:52 |   | U:181        D:53 |   | U:182        D:54 |   | U:183        D:55 |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
 239 ---+                   +---+                   +---+                   +---+                   +---+                   +---+                   +---+                   +---+                   +--- 248       
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+              
                  |                       |                       |                       |                       |                       |                       |                       |                        
                  |                       |                       |                       |                       |                       |                       |                       |                        
                  |                       |                       |                       |                       |                       |                       |                       |                        
        +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+   +---------+---------+              
        |248                |   |249                |   |250                |   |251                |   |252                |   |253  I             |   |254                |   |255                |              
        | U:184        D:56 |   | U:185        D:57 |   | U:186        D:58 |   | U:187        D:59 |   | U:188        D:60 |   | U:189        D:61 |   | U:190        D:62 |   | U:191        D:63 |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
 247 ---+                   +---+                   +---+                   +---+                   +---+                   +---+                   +---+                   +---+                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |   |                   |              
        |                   |   |                   |   |                   |   |                   |   |                   |   | GOBLET            |   |                   |   |                   |              
        +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+   +-------------------+              
    
</pre>                                                                                                                                                                                                               
</span>

<pre>
***** Object Data *****
FOOD in room 18
BOTTLE in room 16
DAGGER in room 15
MACE in room 142
AX in room 137
*SWORD in room 144
*SHIELD in room 5
FLUTE in room 68
MUSHROOM in room 151
PENDANT in room 141
SCEPTER in room 220
LAMP in room 10
BASKET in room 132
PARCHMENT in room 205
*VIAL in room 133
URN in room 66
TALISMAN in room 234
GOBLET in room 253
*SKULL in room 65
ROPE in room 196
*SPELLBOOK in room 4
*POWERRING in room 135
*LIGHTRING in room 135
*TRUTHRING in room 44

***** Spell Data *****
Spell VETRA: in room 21
Spell MITRA: in room 73
Spell OKKAN: in room 89
Spell AKHIROM: in room 91
Spell NERGAL: in room 133
Spell BELROG: in room 157
Spell CROM: in room 212
Spell ISHTAR: in room 253

***** Creature Data *****
SPRITE is in room 6
TROGLODYTE is in room 139
SCORPION is in room 81
NYMPH is in room 70
SATYR is in room 140
MINOTAUR is in room 134
ORACLE is in room 1

***** Room Enter-Action Location *****
Room 124 _a Cave in to next floor (32 damage) if pack heavier than 192. If so move a and b to random rooms.
Room 122 _b Cave in to next floor (32 damage) if pack heavier than 128. If so move a and b to random rooms.
Room 15 _c Cave in to next floor (32 damage) if pack heavier than 95. If so move a and b to random rooms.
Room 211 _d If we have VETAR make the pile-of-rocks appear in this room (it stays here).
Room 220 _e # Play sound effect (same as bb). If we play the flute and have the parchment then the LEDGE appears here.
Room 70 _f 1/2 the time a powerful gust blows lamp out of grasp.
Room 78 _g # Hydra is here. If it is free it pushes us back to last room.
Room 80 _h If we know VETAR or have the SCEPTER, nothing happens. Otherwise we do a RUN.
Room 192 _i Do nothing if we have VETAR. If random number > phys condition or 1/2 the time we RUN and take 5 damage.
Room 200 _j Do nothing if we have MITRA. If random number > phys condition or 1/2 the time we RUN and take 5 damage.
Room 159 _k Do nothing if we have OKKAN. If random number > phys condition or 1/2 the time we RUN and take 5 damage.
Room 156 _l Do nothing if we have AKHIROM. If random number > phys condition or 1/2 the time we RUN and take 5 damage.
Room 78 _m Do nothing if we have NERGAL. If random number > phys condition or 1/2 the time we RUN and take 5 damage.
Room 81 _n Do nothing if we have BELROG. If random number > phys condition or 1/2 the time we RUN and take 5 damage.
Room 17 _o Do nothing if we have CROM. If random number > phys condition or 1/2 the time we RUN and take 5 damage.
Room 24 _p Do nothing if we have ISHTAR. If random number > phys condition or 1/2 the time we RUN and take 5 damage.
Room 77 _q Start the poison clock (we can't stay here long). 1/3 of the time we give the clock an extra tick.
Room 62 _r # When we enter this room 3 times the treasure is released.
Room 78 _q Start the poison clock (we can't stay here long). 1/3 of the time we give the clock an extra tick.
Room 155 _q Start the poison clock (we can't stay here long). 1/3 of the time we give the clock an extra tick.
Room 71 _s # If we have the lamp and it is off then the room drops its treasure. (Strange color walls)
Room 141 _t # If we are holding the packrat's trigger treasure (randomized at start) then the packrat drops his treasure.
Room 207 _q Start the poison clock (we can't stay here long). 1/3 of the time we give the clock an extra tick.
Room 29 _u # If we can see you instantly get the treasure.
Room 72 _v Print POOL OF OIL if the pool has oil in it and we know ISHTAR.
Room 166 _f 1/2 the time a powerful gust blows lamp out of grasp.
Room 199 _32 If we can't see we take 30 damage.
Room 100 _x Add 40 to health and move us a short distance away. 10 minutes must pass before again.
Room 176 _x Add 40 to health and move us a short distance away. 10 minutes must pass before again.
Room 194 _203 # Print SMALL PIT IN CORNER OF ROOM.
Room 213 _213 Print LAYER OF MIST EAST WALL.
Room 32 _32 If we can't see we take 30 damage.
Room 33 _33 # If lamp is off we instantly get the treasure.
Room 203 _203 # Print SMALL PIT IN CORNER OF ROOM.
Room 18 _z Room with music (init to room 16 to 39). The sprite can't move objects here.
Room 232 _232 If we came south to this room and carrying pendant move us near start and random room for pendant.

***** Object Owners *****
OPAL _t(rat)
SAPPHIRE MINOTAUR
SCROLL hydra
SCARAB crypt
JEWLBOX crypt-king
TABLET _33
GOLD _u
SILVER NYMPH
DIAMOND pit
RUBY pile-of-rocks
FLEECE ledge
TIARA _s
POWDER SATYR
AMULET _r
POTION SPRITE
CROWN TROGLODYTE

***** Protected Object Requirements  *****
3FB8: 1A              ; TROGLODYTE
3FB9: 43 07 3B FF     ;   DAGGER (plus bits), SHIELD, NERGAL
3FBD: 1D              ; SATYR
3FBE: 23 77 FF        ;   SPELLBOOK, VETAR (plus bits)
3FC1: 1E              ; MINOTAUR
3FC2: 45 3B FF        ;   AX (plus bits), NERGAL
3FC5: 1B              ; SCORPION
3FC6: 48 3B FF        ;   FLUTE (plus bits), NERGAL
3FC9: 1C              ; NYMPH
3FCA: 48 39 FF        ;   FLUTE (plus bits), OKKAN
3FCD: 19              ; SPRITE
3FCE: 54 2A FF        ;   SKULL (plus bits), POWERRING
3FD1: 06              ; SWORD
3FD2: 0E FF           ;   PARCHMENT
3FD4: 0F              ; VIAL
3FD5: 09 77 FF        ;   MUSHROOM, VETAR (plus bits)
3FD8: 07              ; SHIELD
3FD9: 06 FF           ;   SWORD
3FDB: 14              ; SKULL
3FDC: 0B FF           ;   SCEPTER
3FDE: 2A              ; POWERRING
3FDF: 07 0B 0E 79 FF  ;   SHIELD, SCEPTER, PARCHMENT, OKKAN (plus bits)
3FE4: 2B              ; LIGHTRING
3FE5: 2A 7D 11 FF     ;   POWERRING, CROM (plus bits), TALISMAN
3FE9: 2C              ; TRUTHRING
3FEA: 2B 08 7A FF     ;   LIGHTRING, FLUTE, AKHIROM (plus bits)
3FEE: 23              ; SPELLBOOK
3FEF: 09 13 7C FF     ;   MUSHROOM, GOBLET, BELROG (plus bits)

***** Engine Memory *****
  0A  : 00	  ** current room
  0A  : 01	  ** last room
  00  : 02	direction command bit pattern
  05  : 03	length of user input
  00  : 04	  ** weight of pack
  FF  : 05	  ** physical condition
  00  : 06	  ** bulk of pack
  00  : 07	decoded object number from noun
  00  : 08	Accumulated odds of falling (0, 1/8, 2/8, 3/8 ... with each step in the dark)
  00  : 09	  ** Scorpion sting (0=not, not-zero=number of times)
  00  : 0A	  ** 0 if lamp is off, not 0 is on
  00  : 0B	Count of spaces at the end of the row in print routine
  00  : 0C	Set by BetweenRoomACDE if a climb-down failed ... abort the movement
  00  : 0D	pushed back flag (nobody reads this)
  00  : 0E	  ** HydraStatus: AA = tied up, 1 = dead, 0 = free
  00  : 0F 	  ** HydraPushedUsBack (must be set to TIE HYDRA)  0 = not, 1 = hydra blocked last move (cleared every direction command)
  00  : 10	  ** 1 if "pile of rocks" has been moved to us
  00  : 11	1 if "pile of rocks" has been exposed with OKKAN
  00  : 12	  ** 1 if south passage in room 9 is open. 0 if closed. (open with drapes)
  00  : 13	  ** Count down timer until we can walk through aura and heal again (10 seconds each time)
  00  : 14	1 if lamp has been blown from pack by entering room routine or failed jump
  00  : 15	1 if treasure "$0B" has been released
  00  : 16	NEVER USED
  07  : 17	Random number for passage-description printing
A6BE  : 18:19	Rolling pointer to BASIC rom for random numbers
  00  : 1A	Number of times advice has been given 0-13
  1A  : 1B 	Object 0 
  1D  : 1C	Object 1
  1E  : 1D	Object 2
  1B  : 1E	Object 3    Advice table. Object number is stored here. Upper
  1C  : 1F	Object 4    bit set if advice has already been given for this
  19  : 20	Object 5    protected object.
  06  : 21	Object 6
  0F  : 22	Object 7
  07  : 23	Object 8
  14  : 24	Object 9
  2A  : 25	Object 10
  2B  : 26	Object 11
  2C  : 27	Object 12
  00  : 28	Calculated score
  00  : 29	NEVER USED
  2B  : 2A	Verb command number
  FF  : 2B	Noun word number
  2F  : 2C	Trigger object to make packrat drop treasure
  00  : 2D	NEVER USED
  00  : 2E	Holder value for BetweenRoomACDE
  0C  : 2F	General use lots of places
  00  : 30	Used in InPack
  00  : 31	Used in InPack
  00  : 32	Set by EnteringRoomAction_q (MYSTERIOUS FOG)
  4E  : 33	  ** Current room of HYDRA
  02  : 34	  ** Number of times more ISHTAR can be used. Random init to 1-4.
  C2  : 35	Room for small pit in corner of room
  00  : 36	Room of LEDGE
  00  : 37	Room of "pile of rocks" (OKKAN spell)
0708  : 38:39	  **Oil level of lamp (0 is empty)
  06  : 3A	  ** Number of times lamp can be filled (init to $34 + 4)
0560  : 3B:3C	Pointer to start of input on screen
  17  : 3D	Used in Random-between-0-and-B
  00  : 3E	  ** Time until we can drink from bottle to heal again (16 seconds)
  15  : 3F	Interrupt divisor count (seconds)
  02  : 40	Interrupt sub divisor (minutes)
  00  : 41	Minotaur state timer
  00  : 42	Troglodyte state timer
  00  : 43	Satyr state timer
  00  : 44	Scorpion state timer
  00  : 45	Fog clock runs in room MYSTERIOUS FOG. At 6 seconds we get warned. At 10 we die.
  00  : 46	  ** Minutes of immunity left (AKHIROM gives 3 minutes)
  00  : 47	Count of times entering room with EnteringRoomAction_r. 3 times and treasure drops.
  00  : 48	NEVER USED
  00  : 49	NEVER USED
0002  : 4A:4B	Continual second counter (nobody uses it)
0002  : 4C:4D	Counts the time in a room. Once 15, no going BACK
  00  : 4E	NEVER USED
  00  : 4F	NEVER USED
  00  : 50	NEVER USED
  00  : 51	Used in Oracle advice
  00  : 52	Used in killing Hydra
  00  : 53	Used in sound effects
0000  : 54:55	Used in tape-write
3436  : 56:65	16 byte buffer for decode and auto-word wrap
  00  : 66	Not used
  00  : F3
  00  : F4
  00  : F5
  00  : F6
  00  : F7  Shifting buffer of rooms blocked by Shaking Ground.
  00  : F8  As new rooms are blocked at random, they go on the
  00  : F9  end of the list. Rooms are pulled off of the front
  00  : FA  of the list and unblocked completely. This keeps
  00  : FB  lots of shaking from blocking up the floors over
  00  : FC  time.
  00  : FD
  00  : FE
</pre>
```
