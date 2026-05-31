// This file is free software, distributed under the BSD license.

#include "advent.h"

// Print a generic message
void rspeak (unsigned msg)
{
//{{{ Message array ----------------------------------------------------

static const char* const c_messages [MAXMSG] = {
// 1
"Somewhere nearby is Colossal Cave, where others have found fortunes in\n"
"treasure and gold, though it is rumored that some who enter are never\n"
"seen again. Magic is said to work in the cave. I will be your eyes and\n"
"hands. Direct me with commands of one or two words. I should warn you\n"
"that I look at only the first five letters of each word, so you'll have\n"
"to enter \"northeast\" as \"ne\" to distinguish it from \"north\". Type\n"
"\"help\" and \"info\" if you need more help.\n",
// 2
BOLD_ON "A little dwarf with a big knife blocks your way." BOLD_OFF,
// 3
BOLD_ON "A little dwarf just walked around a corner, saw you,\n"
"threw a little axe at you which missed, cursed, and ran away." BOLD_OFF,
// 4
BOLD_ON "There is a threatening little dwarf in the room with you!" BOLD_OFF,
// 5
"One sharp, nasty knife is thrown at you!",
// 6
"None of them hit you!",
// 7
"One of them gets you!",
// 8
"A hollow voice says \"Plugh\".",
// 9
"There is no way to go that direction.",
// 10
"I am unsure how you are facing. Use compass points or nearby objects.",
// 11
"I don't know in from out here. Use compass points or name\n"
"something in the general direction you want to go.",
// 12
"I don't know how to apply that word here.",
// 13
"I don't understand that!",
// 14
"I'm game. Would you care to explain how?",
// 15
"",
// 16
"It is now pitch dark. If you proceed you will likely fall into a pit.",
// 17
"If you prefer, simply type W rather than West.",
// 18
"Are you trying to catch the bird?",
// 19
"The bird is frightened right now and you cannot catch\n"
"it no matter what you try. Perhaps you might try later.",
// 20
"Are you trying to somehow deal with the snake?",
// 21
"You can't kill the snake, or drive it away, or avoid it, or anything\n"
"like that. There is a way to get by, but you don't have the necessary\n"
"resources right now.",
// 22
"Do you really want to quit now?",
// 23
"You fell into a pit and broke every bone in your body!",
// 24
"You are already carrying it!",
// 25
"You can't be serious!",
// 26
"The bird was unafraid when you entered, but as you approach\n"
"it becomes disturbed and you cannot catch it.",
// 27
"You can catch the bird, but you cannot carry it.",
// 28
"There is nothing here with a lock!",
// 29
"You aren't carrying it!",
// 30
"The little bird attacks the green snake, and in an\n"
"astounding flurry drives the snake away.",
// 31
"You have no keys!",
// 32
"It has no lock.",
// 33
"I don't know how to lock or unlock such a thing.",
// 34
"It was already locked.",
// 35
"The grate is now locked.",
// 36
"The grate is now unlocked.",
// 37
"It was already unlocked.",
// 38
"You have no source of light.",
// 39
"Your lamp is now on.",
// 40
"Your lamp is now off.",
// 41
"There is no way to get past the bear to unlock the chain,_\n"
"which is probably just as well.",
// 42
"Nothing happens.",
// 43
"Where?",
// 44
"There is nothing here to attack.",
// 45
"The little bird is now dead. Its body disappears.",
// 46
"Attacking the snake both doesn't work and is very dangerous.",
// 47
"You killed a little dwarf.",
// 48
BOLD_ON "You attack a little dwarf, but he dodges out of the way." BOLD_OFF,
// 49
"With what? Your bare hands?",
// 50
"Good try, but that is an old worn-out magic word.",
// 51
"I know of places, actions, and things. Most of my vocabulary describes places\n"
"and is used to move you there. To move, try words like forest, building,\n"
"downstream, enter, east, west, north, south, up or down.\n"
"\n"
"I know about a few special objects, like a black rod hidden in the cave.\n"
"These objects can be manipulated using some of the action words I know.\n"
"Usually you will need to give both the object and action words (In either\n"
"order), but sometimes I can infer the object from the verb alone. Some\n"
"objects also imply verbs; in particular, \"inventory\" implies\n"
"\"take inventory\", which causes me to give you a list of what you're carrying.\n"
"\n"
"The objects have side effects; for instance, the rod scares the bird.\n"
"Usually people having trouble moving just need to try a few more words.\n"
"Usually people trying unsuccessfully to manipulate an object are attempting\n"
"something beyond their (or my!) capabilities and should try a completely\n"
"different tack.\n"
"\n"
"To speed the game up, you can sometimes move long distances with a single\n"
"word. For example, \"building\" usually gets you to the building from anywhere\n"
"above ground except when lost in the forest. Also, note that cave passages\n"
"turn a lot, and that leaving a room to the north does not guarantee entering\n"
"the next from the south. Good luck!",
// 52
"It misses!",
// 53
"It gets you!",
// 54
"Ok",
// 55
"You can't unlock the keys.",
// 56
"You have crawled around in some little holes\n"
"and wound up back in the main passage.",
// 57
"I don't know where the cave is, but hereabouts no stream can run\n"
"on the surface for very long. I would try the stream.",
// 58
"I need more detailed instructions to do that.",
// 59
"I can only tell you what you see as you move about and\n"
"manipulate things. I cannot tell you where remote things are.",
// 60
"I don't know that word.",
// 61
"What?",
// 62
"Are you trying to get into the cave?",
// 63
"The grate is very solid and has a hardened steel lock. You cannot enter\n"
"without a key, and there are no keys nearby. I would recommend looking\n"
"elsewhere for the keys.",
// 64
"The trees of the forest are large hardwood oak and maple, with an occasional\n"
"grove of pine or spruce. There is quite a bit of undergrowth, largely birch\n"
"and ash saplings plus nondescript bushes of various sorts. This time of year\n"
"visibility is quite restricted by all the leaves, but travel is quite easy\n"
"if you detour around the spruce and berry bushes.",
// 65
"\n" BOLD_ON
"			+==========================+\n"
"			|        Welcome to        |\n"
"			| Colossal Cave Adventure! |\n"
"			+==========================+\n"
BOLD_OFF "\n"
"		Original development by Willie Crowther.\n"
"		Major features added by Don Woods.\n"
"		Conversion to BDS C by J. R. Jaeger.\n"
"		Unix standardization by Jerry D. Pohl.\n"
"		Port to QNX 4 and bug fixes by James Lummel.\n",
// 66
"Digging without a shovel is quite impractical.\n"
"Even with a shovel progress is unlikely.",
// 67
"Blasting requires dynamite.",
// 68
"I'm as confused as you are.",
// 69
"Mist is a white vapor, usually water. Seen from time to time in caverns. It can\n"
"be found anywhere but is frequently a sign of a deep pit leading down to water.",
// 70
"Your feet are now wet.",
// 71
"I think I just lost my appetite.",
// 72
"Thank you. It was delicious!",
// 73
"You have taken a drink from the stream. The water tastes strongly of minerals,\n"
"but is not unpleasant. It is extremely cold.",
// 74
"The bottle of water is now empty.",
// 75
"Rubbing the electric lamp is not particularly rewarding.\n"
"Anyway, nothing exciting happens.",
// 76
"Peculiar. Nothing unexpected happens.",
// 77
"Your bottle is empty and the ground is wet.",
// 78
"You can't pour that.",
// 79
"Watch it!",
// 80
"Which way?",
// 81
"Oh dear, you seem to have gotten yourself killed.\n"
"I might be able to help you out, but I've never really done this before.\n"
"Do you want me to try to reincarnate you?",
// 82
"All right. But don't blame me if something goes wr......\n"
"		" BOLD_ON "--- POOF !! ---" BOLD_OFF "\n"
"You are engulfed in a cloud of orange smoke. Coughing and\n"
"gasping, you emerge from the smoke and find...",
// 83
"You clumsy oaf, you've done it again! I don't know how long I can\n"
"keep this up. Do you want me to try reincarnating you again?",
// 84
"Okay, now where did I put my orange smoke? ... " BOLD_ON "> POOF! <" BOLD_OFF "\n"
"Everything disappears in a dense cloud of orange smoke.",
// 85
"Now you've really done it! I'm out of orange smoke! You don't expect me\n"
"to do a decent reincarnation without any orange smoke, do you?",
// 86
"Okay, If you're so smart, do it yourself! I'm leaving!",
// 87
"Reserved",
// 88
"Reserved",
// 89
"Reserved",
// 90
"Reserved",
// 91
"Sorry, but I no longer seem to remember how it was you got here.",
// 92
"You can't carry anything more. You'll have to drop something first.",
// 93
"You can't go through a locked steel grate!",
// 94
"I believe what you want is right here with you.",
// 95
"You don't fit through a two-inch slit!",
// 96
"I respectfully suggest you go across the bridge instead of jumping.",
// 97
"There is no way across the fissure.",
// 98
"You're not carrying anything.",
// 99
"You are currently holding the following:",
// 100
"It's not hungry (It's merely pinin' for the Fjords).\n"
"Besides You have no bird seed.",
// 101
"The snake has now devoured your bird.",
// 102
"There's nothing here it wants to eat (Except perhaps you).",
// 103
"You fool, Dwarves eat only coal! Now you've made him REALLY mad !!",
// 104
"You have nothing in which to carry it.",
// 105
"Your bottle is already full.",
// 106
"There is nothing here with which to fill the bottle.",
// 107
"Your bottle is now full of water.",
// 108
"Your bottle is now full of oil.",
// 109
"You can't fill that.",
// 110
"Don't be ridiculous!",
// 111
"The door is extremely rusty and refuses to open.",
// 112
"The plant indignantly shakes the oil off its leaves and asks: \"Water?\".",
// 113
"The hinges are quite thoroughly rusted now and won't budge.",
// 114
"The oil has freed up the hinges so that the door will now move,\n"
"although it requires some effort.",
// 115
"The plant has exceptionally deep roots and cannot be pulled free.",
// 116
"The Dwarves' knives vanish as they strike the walls of the cave.",
// 117
"Something you're carrying won't fit through the tunnel with you.\n"
"You'd best take inventory and drop something.",
// 118
"You can't fit this five-foot clam through that little passage!",
// 119
"You can't fit this five foot oyster through that little passage!",
// 120
"I advise you to put down the clam before opening it. " BOLD_ON ">STRAIN!<" BOLD_OFF,
// 121
"I advise you to put down the oyster before opening it. " BOLD_ON ">WRENCH!<" BOLD_OFF,
// 122
"You don't have anything strong enough to open the clam.",
// 123
"You don't have anything strong enough to open the oyster.",
// 124
"A glistening pearl falls out of the clam and rolls away. Goodness,\n"
"this must really be an oyster. (I never was very good at identifying\n"
"bivalves.) Whatever it is, it has now snapped shut again.",
// 125
"The oyster creaks open, revealing nothing but oyster inside.\n"
"It promptly snaps shut again.",
// 126
"You have crawled around in some little holes and found your way blocked\n"
"by a recent cave-in. You are now back in the main passage.",
// 127
"There are faint rustling noises from the darkness behind you.",
// 128
"Out from the shadows behind you pounces a bearded pirate! \"Har, har\" he\n"
"chortles, \"I'll just take all this booty and hide it away with me chest\n"
"deep in the maze!\". He snatches your treasure and vanishes into the gloom.",
// 129
"A sepulchral voice reverberating through the cave says:\n"
"\"Cave closing soon. All adventurers exit immediately through main office.\"",
// 130
"A mysterious recorded voice groans into life and announces:\n"
"\"This exit is closed. Please leave via main office.\"",
// 131
"It looks as though you're dead. Well, seeing as how it's so\n"
"close to closing time anyway, I think we'll just call it a day.",
// 132
"The sepulchral voice entones, \"The cave is now closed.\" As the echoes\n"
"fade, there is a blinding flash of light (and a small puff of orange\n"
"smoke).... As your eyes refocus you look around and find...",
// 133
"There is a loud explosion, and a twenty-foot hole appears in the far wall,\n"
"burying the Dwarves in the rubble. You march through the hole and find\n"
"yourself in the main office, where a cheering band of friendly elves\n"
"carry the conquering adventurer off into the sunset.",
// 134
"There is a loud explosion, and a twenty-foot hole appears in the far\n"
"wall, burying the snakes in the rubble. A river of molten lava pours in\n"
"through the hole, destroying everything in its path, including you!!",
// 135
"There is a loud explosion, and you are suddenly\n"
"splashed across the walls of the room.",
// 136
"The resulting ruckus has awakened the Dwarves.\n"
BOLD_ON "There are now several threatening little Dwarves in the room with you!\n"
"Most of them throw knives at you! All of them get you!" BOLD_OFF,
// 137
"Oh, leave the poor unhappy bird alone.",
// 138
"I daresay whatever you want is around here somewhere.",
// 139
"I don't know the word \"stop\". Use \"quit\" if you want to give up.",
// 140
"You can't get there from here.",
// 141
"You are being followed by a very large, tame bear.",
// 142
"If you want to end your adventure early, say \"quit\". To suspend your\n"
"adventure such that you can continue later say \"save\" To see how\n"
"well you're doing, say \"score\". To get full credit for a treasure,\n"
"you must have left it safely in the wellhouse building, though you get\n"
"partial credit just for locating it. You lose points for getting killed,\n"
"or for quitting, though the former costs you more.  There are also points\n"
"based on how much (If any) of the cave you've managed to explore;  in\n"
"particular, there is a large bonus just for getting in (to distinguish\n"
"the beginners from the rest of the pack), and there are other ways to\n"
"determine whether you've been through some of the more harrowing sections.\n"
"\n"
"If you think you've found all the treasures, just keep exploring for a\n"
"while. If nothing interesting happens, you haven't found them all yet. If\n"
"something interesting DOES happen, it means you're getting a bonus and\n"
"have an opportunity to garner many more points in the master's section.\n"
"\n"
"I may occasionally offer hints in you seem to be having trouble. If I do,\n"
"I'll warn you in advance how accepting hints will affect your score.",
// 143
"Do you indeed wish to quit now?",
// 144
"There is nothing here with which to fill the vase.",
// 145
"The sudden change in temperature has delicately shattered the vase.",
// 146
"It is beyond your power to do that.",
// 147
"I don't know how.",
// 148
"It is too far up for you to reach.",
// 149
"You killed a little dwarf. The body vanished in a cloud of greasy black smoke.",
// 150
"The shell is very strong and impervious to attack.",
// 151
"What's the matter, can't you read? Now you'd best start over.",
// 152
"The axe bounces harmlessly off the dragon's thick scales.",
// 153
"The dragon looks rather nasty. You'd best not try to get by.",
// 154
"The little bird attacks the green dragon, and in an\n"
"astounding flurry gets burnt to a cinder. The ashes blow away.",
// 155
"On what?",
// 156
"Okay, from now on I'll only describe a place in full the first time you\n"
"come to it. To get the full description say \"look\".",
// 157
"Trolls are close relatives with the rocks and have skin as tough as that\n"
"of a rhinoceros. The troll fends off your blows effortlessly.",
// 158
"The troll deftly catches the axe, examines it carefully, and tosses it\n"
"back, declaring, \"Good workmanship, but it's not valuable enough.\".",
// 159
"The troll catches your treasure and scurries away out of sight.",
// 160
"The troll refuses to let you cross.",
// 161
"There is no longer any way across the chasm.",
// 162
"Just as you reach the other side, the bridge buckles beneath the weight of the\n"
"bear, which was still following you around. You scrabble desperately for\n"
"support, but as the bridge collapses you stumble back and fall into the chasm.",
// 163
"The bear lumbers toward the troll, who lets out a startled shriek and\n"
"scurries away. The bear soon gives up pursuit and wanders back.",
// 164
"The axe misses and lands near the bear where you can't get at it.",
// 165
"With what? Your bare hands? Agains HIS bear hands??",
// 166
"The bear is confused; he only wants to be your friend.",
// 167
"For crying out loud, the poor thing is already dead!",
// 168
"The bear eagerly wolfs down your food, after which he seems\n"
"to calm down considerably, and even becomes rather friendly.",
// 169
"The bear is still chained to the wall.",
// 170
"The chain is still locked.",
// 171
"The chain is now unlocked.",
// 172
"The chain is now locked.",
// 173
"There is nothing here to which the chain can be locked.",
// 174
"There is nothing here to eat.",
// 175
"Do you want the hint?",
// 176
"Do you need help getting out of the maze?",
// 177
"You can make the passages look less alike by dropping things.",
// 178
"Are you trying to explore beyond the plover room?",
// 179
"There is a way to explore that region without having to worry about\n"
"falling into a pit. None of the objects available is immediately useful\n"
"in descovering the secret.",
// 180
"Do you need help getting out of here?",
// 181
"Don't go west.",
// 182
"Gluttony is not one of the Troll's vices. Avarice, however, is.",
// 183
"Your lamp is getting dim... You'd best start wrapping this up, unless\n"
"you can find some fresh batteries. I seem to recall there's a vending\n"
"machine in the maze. Bring some coins with you.",
// 184
"Your lamp has run out of power.",
// 185
"There's not much point in wandering around out here, and you can't\n"
"explore the cave without a lamp. So let's just call it a day.",
// 186
"There are faint rustling noises from the darkness behind you. As you\n"
"turn toward them, the beam of your lamp falls across a bearded pirate.\n"
"He is carrying a large chest. \"Shiver me timbers!\" he cries, \"I've been\n"
"spotted! I'd best hide meself off to the maze and hide me chest!\"\n"
"With that, he vanished into the gloom.",
// 187
"Your lamp is getting dim. You'd best go back for those batteries.",
// 188
"Your lamp is getting dim.. I'm taking the liberty of replacing the batteries.",
// 189
"Your lamp is getting dim, and you're out of spare batteries.\n"
"You'd best start wrapping this up.",
// 190
"I'm afraid the magazine is written in Dwarvish.",
// 191
"\"This is not the maze where the pirate leaves his treasure chest.\"",
// 192
"Hmm, this looks like a clue, which means it'll cost you 10\n"
"points to read it. Should I go ahead and read it anyway?",
// 193
"It says, \"There is something strange about this place, such that one of\n"
"the words I've always known now has a new effect.\"",
// 194
"It says the same thing it did before.",
// 195
"I'm afraid I don't understand.",
// 196
"\"Congratulations on bringing light into the dark-room!\"",
// 197
"You strike the mirror a resounding blow, whereupon it\n"
"shatters into a myriad tiny fragments.",
// 198
"You have taken the vase and hurled it delicately to the ground.",
// 199
"You prod the nearest Dwarf, who wakes up grumpily, takes\n"
"one look at you, curses, and grabs for his axe.",
// 200
"Is this acceptable?",
// 201
"There's no point in suspending a demonstration game."
};

//}}}-------------------------------------------------------------------

    if (--msg < ArraySize(c_messages))
	puts (c_messages [msg]);
}

// Routine to speak default verb message
void actspk (unsigned v)
{
    // action messages
    static const uint8_t c_actmsg[] = {
	24,29,0,33,0,33,38,38,42,14,
	43,110,29,110,73,75,29,13,59,59,
	174,109,67,13,147,155,195,146,110,13,
	13
    };
    if (--v < ArraySize(c_actmsg))
	rspeak (c_actmsg[v]);
}

// Routine to request a yes or no answer to a question.
bool yes (unsigned qmsg, unsigned ymsg, unsigned nmsg)
{
    if (qmsg)
	rspeak(qmsg);
    printf (BOLD_ON "[yn]? " BOLD_OFF);
    char answer [16] = {};
    fgets (ArrayBlock(answer), stdin);
    if (tolower (answer[0]) == 'y') {
	if (ymsg)
	    rspeak (ymsg);
	return true;
    } else {
	if (nmsg)
	    rspeak (nmsg);
	return false;
    }
}
