// This file is free software, distributed under the BSD license.

#include "advent.h"

//{{{ place, fixed, prop - object runtime data arrays ------------------

// Object location
loc_t place [MAXOBJ] = {
    0,
	WELLHOUSE,
	WELLHOUSE,
	AT_GRATE,
	10,
	XYZZY_ROOM,
	0,
	14,
	13,
	94,
    96,
	KING_HALL,
	FISSURE_E,
	101,
	103,
	0,
	106,
	0,
	0,
	WELLHOUSE,
    WELLHOUSE,
	0,
	0,
	109,
	25,
	23,
	111,
	35,
	0,
	ORIENT_ROOM,
    0,
	119,
	CHASM_SW,
	CHASM_SW,
	0,
	130,
	0,
	126,
	CHEST_ROOM2,
	0,
    96,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
    18,
	FISSURE_W,
	28,
	29,
	30,
	0,
	GIANT_ROOM,
	95,
	ORIENT_ROOM,
	100,
    101,
	0,
	119,
	127,
	130,
	0,
	0,
	0,
	0,
	0,
    0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0
};

// Second object loc
loc_t fixed [MAXOBJ] = {
    0,0,0,UNDER_GRATE,0,0,0,MIST_HALL,0,CARRIED,
    0,CARRIED,FISSURE_W,CARRIED,0,0,0,CARRIED,0,0,
    0,0,0,CARRIED,CARRIED,67,CARRIED,110,0,CARRIED,
    CARRIED,121,CHASM_NE,CHASM_NE,0,CARRIED,CARRIED,CARRIED,CARRIED,0,
    CARRIED,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,
    0,0,121,CARRIED,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0
};

// Status of object
int8_t prop [MAXOBJ] = {
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,
    -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,
    -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,
    -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,
    -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,
    -1,-1,-1,-1,-1,-1,-1,-1,-1,-1
};

//}}}-------------------------------------------------------------------

// Routine to tell if an item is present.
bool here (obj_t item)
{
    return place[item] == loc || toting(item);
}

// Routine to tell if an item is being carried.
bool toting (obj_t item)
{
    return place[item] == CARRIED;
}

// Routine to tell if player is on either side of a two sided object.
bool at (obj_t item)
{
    return (place[item] == loc || fixed[item] == loc);
}

// Routine to destroy an object
void destroy_object (obj_t obj)
{
    move_object (obj, 0);
}

// Routine to move an object
void move_object (obj_t obj, loc_t where)
{
    loc_t from = (obj < MAXOBJ) ? place[obj] : fixed[obj-MAXOBJ];
    if (from != CARRIED)
	carry (obj);
    drop (obj, where);
}

// Routine to carry an object
void carry (obj_t obj)
{
    if (obj < MAXOBJ && place[obj] != CARRIED) {
	place[obj] = CARRIED;
	++holding;
    }
}

// Routine to drop an object
void drop (obj_t obj, loc_t where)
{
    if (obj < MAXOBJ) {
	if (place[obj] == CARRIED)
	    --holding;
	place[obj] = where;
    } else
	fixed[obj - MAXOBJ] = where;
}

// routine to move an object and return a
// value used to set the negated prop values
// for the repository.
int put (obj_t obj, loc_t where, int pval)
{
    move_object (obj, where);
    return -1-pval;
}

// Determine liquid in the bottle
int liq (void)
{
    int i = prop[BOTTLE];
    int j = -1 - i;
    return liq2 (i > j ? i : j);
}

// Determine liquid at a location
int liqloc (loc_t l)
{
    if (cond[l] & LIQUID)
	return liq2(cond[l] & WATOIL);
    else
	return liq2(1);
}

// Convert 0 to WATER
// 1 to nothing
// 2 to OIL
int liq2 (int pbottle)
{
    return (1 - pbottle) * WATER + (pbottle >> 1) * (WATER + OIL);
}

// Multiple object descriptions exist based on conditions; set skip to select sub-message
void pspeak (obj_t n, int s)
{
//{{{ Message array ----------------------------------------------------
    static const char* const c_odesc [64] = {
// 1
	"Set of keys.\0"
	"There are some keys on the ground here.\0",
// 2
	"Brass lantern\0"
	"There is a shiny brass lamp nearby.\0"
	"There is a lamp shining nearby.\0",
// 3
	"*Grate\0"
	"The grate is locked.\0"
	"The grate is open.\0",
// 4
	"Wicker cage\0"
	"There is a small wicker cage discarded nearby.\0",
// 5
	"Black rod\0"
	"A three foot black rod with a rusty star on an end lies nearby.\0",
// 6
	"Black rod\0"
	"A three foot black rod with a rusty mark on an end lies nearby.\0",
// 7
	"*Steps\0"
	"Rough stone steps lead down the pit.\0"
	"Rough stone steps lead up the dome.\0",
// 8
	"Little bird in cage\0"
	"A cheerful little bird is sitting here singing.\0"
	"There is a little bird in the cage.\0",
// 9
	"*Rusty door\0"
	"The way north is barred by a massive, rusty, iron door.\0"
	"The way north leads through a massive, rusty, iron door.\0",
// 10
	"Velvet pillow\0"
	"A small velvet pillow lies on the floor.\0",
// 11
	"*Snake\0"
	"A huge green fierce snake bars the way!\0",
// 12
	"*Fissure\0"
	"\0"
	"A crystal bridge now spans the fissure.\0"
	"The crystal bridge has vanished!\0",
// 13
	"*Stone tablet\0"
	"A massive stone tablet imbedded in the wall reads:\0"
	"\"Congratulations on bringing light into the dark-room!\"\0",
// 14
	"Giant clam >Grunt!<\0"
	"There is an enormous clam here with its shell tightly closed.\0",
// 15
	"Giant oyster >Groan!<\0"
	"There is an enormous oyster here with its shell tightly closed.\0"
	"Interesting. Something is written on the underside of the oyster.\0",
// 16
	"\"Spelunker Today\"\0"
	"There are a few recent issues of \"Spelunker Today\" magazine here.\0",
// 17
	"\0",
// 18
	"\0",
// 19
	"Tasty food\0"
	"There is tasty food here.\0",
// 20
	"Small bottle\0"
	"There is a bottle of water here.\0"
	"There is an empty bottle here.\0"
	"There is a bottle of oil here.\0",
// 21
	"Water in the bottle.\0",
// 22
	"Oil in the bottle\0",
// 23
	"*Mirror\0",
// 24
	"*Plant\0"
	"There is a tiny little plant in the pit, murmuring \"Water, Water, ...\"\0"
	"The plant spurts into furious growth for a few seconds.\0"
	"There is a 12-foot-tall beanstalk stretching up out of the pit,\n"
		"bellowing \"Water!! Water!!\"\0"
	"The plant grows explosively, almost filling the bottom of the pit.\0"
	"There is a gigantic beanstalk stretching all the way up to the hole.\0"
	"You've over-watered the plant! It's shriveling up! It's, It's...\0",
// 25
	"*Phony plant\0"
	"\0"
	"The top of a 12-foot-tall beanstalk is poking up out of the west pit.\0"
	"There is a huge beanstalk growing out of the west pit up to the hole.\0",
// 26
	"*Stalactite\0",
// 27
	"*Shadowy figure\0"
	"The shadowy figure seems to be trying to attract your attention.\0",
// 28
	"Dwarf's axe\0"
	"There is a little axe here.\0"
	"There is a little axe lying beside the bear.\0",
// 29
	"*Cave drawings\0",
// 30
	"*Pirate\0",
// 31
	"*Dragon\0"
	"A huge green fierce dragon bars the way!\0"
	"Congratulations! You have just vanquished a dragon with your bare hands!\n"
		"(Unbelievable, Isn't it?)\0"
	"The body of a huge green dead dragon is lying off to one side.\0",
// 32
	"*Chasm\0"
	"A rickety wooden bridge extends across the chasm, vanishing into the mist.\0"
	"A sign posted on the bridge reads:\n"
		  "\"Stop! Pay Troll!\"\0"
	"The wreckage of a bridge (and a dead bear)\n"
		"can be seen at the bottom of the chasm.\0",
// 33
	"*Troll\0"
	"A burly troll stands by the bridge and insists you throw\n"
		"him a treasure before you may cross.\0"
	"The troll steps out from beneath the bridge and blocks your way.\0",
// 34
	"*Phony troll\0"
	"The troll is nowhere to be seen.\0",
// 35
	"\0"
	"There is a ferocious cave bear eyeing you from the far end of the room!\0"
	"There is a gentle cave bear sitting placidly in one corner.\0"
	"There is a contented-looking bear wandering about nearby.\0",
// 36
	"*Message in second maze\0"
	"There is a message scrawled in the dust in a flowery script, reading:\n"
		"\"This is not the maze where the\"\n"
		"\"pirate leaves his treasure chest\"\0",
// 37
	"*Volcano or Geyser\0",
// 38
	"*Vending machine\0"
	"There is a massive vending machine here. The instructions on it read:\n"
		"\"Drop coins here to receive fresh batteries.\"\0",
// 39
	"Batteries\0"
	"There are fresh batteries here.\0"
	"Some worn-out batteries have been discarded nearby.\0",
// 40
	"*Carpet and,or moss\0",
// 41
	"\0",
// 42
	"\0",
// 43
	"\0",
// 44
	"\0",
// 45
	"\0",
// 46
	"\0",
// 47
	"\0",
// 48
	"\0",
// 49
	"\0",
// 50
	"Large gold nugget\0"
	"There is a large sparkling nugget of gold here!\0",
// 51
	"Several diamonds\0"
	"There are diamonds here!\0",
// 52
	"Bars of silver\0"
	"There are bars of silver here!\0",
// 53
	"Precious jewelry\0"
	"There is precious jewelry here!\0",
// 54
	"Rare coins\0"
	"There are many coins here!\0",
// 55
	"Treasure chest\0"
	"The pirate's treasure chest is here!\0",
// 56
	"Golden eggs\0"
	"There is a large nest here, full of golden eggs!\0"
	"The nest of golden eggs has vanished!\0"
	"Done!\0",
// 57
	"Jeweled trident\0"
	"There is a jewel-encrusted trident here!\0",
// 58
	"Ming vase\0"
	"There is a delicate, precious, ming vase here!\0"
	"The vase is now resting, delicately, on a velvet pillow.\0"
	"The floor is littered with worthless shards of pottery.\0"
	"The ming vase drops with a delicate crash.\0",
// 59
	"Egg-sized emerald\0"
	"There is an emerald here the size of a plover's egg!\0",
// 60
	"Platinum pyramid\0"
	"There is a platinum pyramid here, 8 inches on a side!\0",
// 61
	"Glistening pearl\0"
	"Off to one side lies a glistening pearl!\0",
// 62
	"Persian rug\0"
	"There is a persian rug spread out on the floor!\0"
	"The dragon is sprawled out on a persian rug!!\0",
// 63
	"Rare spices\0"
	"There are rare spices here!\0",
// 64
	"Golden chain\0"
	"There is a golden chain lying in a heap on the floor!\0"
	"The bear is locked to the wall with a golden chain!\0"
	"There is a golden chain locked to the wall!\0"
    };
//}}}-------------------------------------------------------------------
    if (--n >= ArraySize(c_odesc))
	return;
    const char* m = c_odesc[n];
    for (int i = 0; i <= s && *m; ++i)
	m += strlen(m)+1;
    printf (BOLD_ON "%s" BOLD_OFF "\n", m);
}
