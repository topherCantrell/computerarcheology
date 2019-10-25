![Haunted House](HauntedHouse.jpg)

# Haunted House

>>> deploy:<br>
>>>   +BinaryDataHauntedHouse.js<br>
>>>   +HauntedHouse.jpg<br>
>>>   +hauntedhouse.js<br>
>>>   RAMUse1.md<br>
>>>   Code1.md<br>
>>>   RAMUse2.md<br>
>>>   Code2.md<br>
>>>   ----<br>
>>>   Journal.md<br>

```html
<script src="/TRS80/HauntedHouse/BinaryDataHauntedHouse.js"></script>
<script src="/js/Z80.js"></script>
<script src="/TRS80/TRS80Text.js"></script>
<script src="/TRS80/HauntedHouse/hauntedhouse.js"></script>
<script>window.onload = function() {startHauntedHouse("hauntedConsole");}</script>
```

>>> playMe {

# Play Me!
Play the game in a TRS80 emulator. Click on the black console and press any key.

```html
<button id="floorOne" class="btn btn-primary" >1st Floor</button><button id="floorTwo" class="btn btn-primary" style="margin-left:0.5em">2nd Floor</button><p>
<textarea id="hauntedConsole" rows="16" style="background-color: black;color: white;font-family: monospace;font-size:12px;width:65ch;" ></textarea>
```

>>> }


# Code Links 

* [Disassembled Code 1st Floor](Code1.md)
* [Disassembled Code 2nd Floor](Code2.md)
* [RAM Usage 1st Floor](RAMUse1.md)
* [RAM Usage 2nd Floor](RAMUse2.md)

# Get Out! 

Generations have passed since the McDaniel family mysteriously disappeared. It is said that a stranger came 
to visit on that cold, Autumn day many years ago, but no one knows for sure. Their house has been vacant 
for decades now. Its two story image is forlorn and looming, visible only from the narrow, winding road that 
has been distorted by vegetation from the surrounding forest. The stone wall that encompasses the house is 
discolored and broken from years of neglect, its iron gate rusty and worn by angry seasons. The windows are 
boarded ? the house is quiet and contented, not accustomed to visitors. The wind is restless today, blowing 
fallen leaves in all directions. As you walk towards the entrance of the house, the wind grows distant and weak. 
Suddenly, the calm and silence is broken by sounds from within the house!

# From the mind of Robert Arnstein 

This is one of the many Robert Arnstein text games disassmebled on my site. You can see the evolution of the
game engine by comparing Haunted House with [Pyramid](../../CoCo/Pyramid),
[Pyramid for TRS-80](/TRS80/Pyramid/index.html), [RaakaTu](../..CoCo/RaakaTu), and 
[Bedlam](../..CoCo/Bedlam).

>>> tourGuide {

# Tour Guide 

The code is code-within-code. The adventure language processor commands are [here](Code1.html#script-commands).

Have a look at all the unpacked messages in the game:
* [First Floor Messages](Code1.html#compressed-text)
* [Second Floor Messages](Code2.html#compressed-text)

Visit the room scripts to see what you can do in each room. Then visit the general script that runs after the 
current room has a chance to take the command. These "adventure language scripts" are interpreted by 
the [Script Processor](Code1.html#run-script).
* [Room scripts 1st floor](Code1.html#room-scripts)
* [General Script 1st floor](Code1.html#general-script)
* [Room scripts 2nd floor](Code2.html#room-scripts)
* [General Script 2nd floor](Code2.html#general-script)

Read through all words that the game understands:
* [Word 1st Floor](Code1.html#command-table)
* [Word 2nd Floor](Code2.html#command-table)

>>> }

# References

If you seek specific game information, solutions, and online emulators then check out [Sean Murphy's wonderful site](http://www.figmentfly.com).

Joe Peterson has recreated the original Haunted house in Java and Python. The Java version makes a nice Android app you can play
on your phone. Check it out on [The "Explore" Adventure Games website](http://www.wildlava.com/explore/).
