// This file is free software, distributed under the BSD license.

#include "advent.h"

//{{{ Adventure vocabulary ---------------------------------------------

struct wac { char aword [14]; uint16_t acode; };

enum {
    MOTION_WORD,
    OBJECT_WORD,
    ACTION_WORD,
    MAGIC_WORD
};

#define WORD_BASE(t)	(t*1000)
#define MO(w) (WORD_BASE(MOTION_WORD)+w)
#define GO(w) (WORD_BASE(MOTION_WORD)+GO_##w)
#define OB(w) (WORD_BASE(OBJECT_WORD)+w)
#define AW(w) (WORD_BASE(ACTION_WORD)+w)
#define MA(w) (WORD_BASE( MAGIC_WORD)+w)

static const struct wac c_words[] = {
    { "",		MO (0)		},
    { "?",		MA (MAGIC_HELP)	},
    { "above",		GO (UP)	},
    { "abra",		MA (50)		},
    { "abracadabra",	MA (50)		},
    { "across",		GO (ACROSS)	},
    { "ascend",		GO (UP)	},
    { "attack",		AW (KILL)	},
    { "awkward",	GO (AWKWARD)	},
    { "axe",		OB (AXE)	},
    { "back",		GO (BACK)	},
    { "barren",		GO (BARREN)	},
    { "bars",		OB (GOLD_BARS)	},
    { "batteries",	OB (BATTERIES)	},
    { "battery",	OB (BATTERIES)	},
    { "beans",		OB (PLANT)	},
    { "bear",		OB (BEAR)	},
    { "bed",		GO (BED)	},
    { "bedquilt",	GO (BEDQUILT)	},
    { "bird",		OB (BIRD)	},
    { "blast",		AW (BLAST)	},
    { "blowup",		AW (BLAST)	},
    { "bottle",		OB (BOTTLE)	},
    { "box",		OB (CHEST)	},
    { "break",		AW (BREAK)	},
    { "brief",		AW (BRIEF)	},
    { "broken",		GO (BROKEN)	},
    { "building",	GO (BUILDING)	},
    { "cage",		OB (CAGE)	},
    { "calm",		AW (CALM)	},
    { "canyon",		GO (CANYON)	},
    { "capture",	AW (TAKE)	},
    { "carpet",		OB (40)		},
    { "carry",		AW (TAKE)	},
    { "catch",		AW (TAKE)	},
    { "cave",		GO (CAVE)	},
    { "cavern",		GO (CAVERN)	},
    { "chain",		OB (CHAIN)	},
    { "chant",		AW (SAY)	},
    { "chasm",		OB (CHASM)	},
    { "chest",		OB (CHEST)	},
    { "clam",		OB (CLAM)	},
    { "climb",		GO (CLIMB)	},
    { "close",		AW (LOCK)	},
    { "cobblestone",	GO (COBBLESTONE)},
    { "coins",		OB (COINS)	},
    { "continue",	AW (WALK)	},
    { "crack",		GO (CRACK)	},
    { "crap",		MA (79)		},
    { "crawl",		GO (CRAWL)	},
    { "cross",		GO (CROSS)	},
    { "d",		GO (DOWN)	},
    { "damn",		MA (79)		},
    { "damnit",		MA (79)		},
    { "dark",		GO (DARK)	},
    { "debris",		GO (DEBRIS)	},
    { "depression",	GO (DEPRESSION)	},
    { "descend",	GO (DOWN)	},
    { "describe",	GO (LOOK)	},
    { "detonate",	AW (BLAST)	},
    { "devour",		AW (EAT)	},
    { "diamonds",	OB (DIAMONDS)	},
    { "dig",		MA (66)		},
    { "discard",	AW (DROP)	},
    { "disturb",	AW (WAKE)	},
    { "dome",		GO (DOME)	},
    { "door",		OB (DOOR)	},
    { "down",		GO (DOWN)	},
    { "downstream",	GO (DOWNSTREAM)	},
    { "downward",	GO (DOWN)	},
    { "dragon",		OB (DRAGON)	},
    { "drawing",	OB (29)		},
    { "drink",		AW (DRINK)	},
    { "drop",		AW (DROP)	},
    { "dump",		AW (DROP)	},
    { "dwarf",		OB (DWARF)	},
    { "dwarves",	OB (DWARF)	},
    { "e",		GO (EAST)	},
    { "east",		GO (EAST)	},
    { "eat",		AW (EAT)	},
    { "egg",		OB (EGGS)	},
    { "eggs",		OB (EGGS)	},
    { "emerald",	OB (EMERALD)	},
    { "enter",		GO (ENTER)	},
    { "entrance",	GO (ENTRANCE)	},
    { "examine",	GO (LOOK)	},
    { "excavate",	MA (66)		},
    { "exit",		GO (OUTSIDE)	},
    { "explore",	AW (WALK)	},
    { "extinguish",	AW (OFF)	},
    { "fee",		AW (FOO)	},
    { "fee",		MA (1)		},
    { "feed",		AW (FEED)	},
    { "fie",		AW (FOO)	},
    { "fie",		MA (2)		},
    { "fight",		AW (KILL)	},
    { "figure",		OB (27)		},
    { "fill",		AW (FILL)	},
    { "find",		AW (FIND)	},
    { "fissure",	OB (FISSURE)	},
    { "floor",		GO (FLOOR)	},
    { "foe",		AW (FOO)	},
    { "foe",		MA (3)		},
    { "follow",		AW (WALK)	},
    { "foo",		AW (FOO)	},
    { "foo",		MA (4)		},
    { "food",		OB (FOOD)	},
    { "forest",		GO (FOREST)	},
    { "fork",		GO (FORK)	},
    { "forward",	GO (FORWARD)	},
    { "free",		AW (DROP)	},
    { "fuck",		MA (79)		},
    { "fum",		AW (FOO)	},
    { "fum",		MA (5)		},
    { "get",		AW (TAKE)	},
    { "geyser",		OB (37)		},
    { "giant",		GO (GIANT)	},
    { "go",		AW (WALK)	},
    { "gold",		OB (NUGGET)	},
    { "goto",		AW (WALK)	},
    { "grate",		OB (GRATE)	},
    { "gully",		GO (GULLY)	},
    { "h2o",		OB (WATER)	},
    { "hall",		GO (HALL)	},
    { "headlamp",	OB (LAMP)	},
    { "help",		MA (MAGIC_HELP)	},
    { "hill",		GO (HILL)	},
    { "hit",		AW (KILL)	},
    { "hocus",		MA (50)		},
    { "hole",		GO (HOLE)	},
    { "hours",		AW (HOURS)	},
    { "house",		GO (BUILDING)	},
    { "i",		AW (INVENTORY)	},
    { "ignite",		AW (BLAST)	},
    { "in",		GO (INSIDE)	},
    { "info",		MA (142)	},
    { "information",	MA (142)	},
    { "inside",		GO (INSIDE)	},
    { "inventory",	AW (INVENTORY)	},
    { "inward",		GO (INSIDE)	},
    { "issue",		OB (MAGAZINE)	},
    { "jar",		OB (BOTTLE)	},
    { "jewel",		OB (JEWELS)	},
    { "jewelry",	OB (JEWELS)	},
    { "jewels",		OB (JEWELS)	},
    { "jump",		GO (JUMP)	},
    { "keep",		AW (TAKE)	},
    { "key",		OB (KEYS)	},
    { "keys",		OB (KEYS)	},
    { "kill",		AW (KILL)	},
    { "knife",		OB (KNIFE)	},
    { "knives",		OB (KNIFE)	},
    { "l",		GO (LOOK)	},
    { "lamp",		OB (LAMP)	},
    { "lantern",	OB (LAMP)	},
    { "leave",		GO (OUTSIDE)	},
    { "left",		GO (LEFT)	},
    { "light",		AW (ON)		},
    { "lite",		AW (ON)		},
    { "load",		AW (LOAD)	},
    { "lock",		AW (LOCK)	},
    { "log",		AW (LOG)	},
    { "look",		GO (LOOK)	},
    { "lost",		MA (68)		},
    { "low",		GO (LOW)	},
    { "machine",	OB (VEND)	},
    { "magazine",	OB (MAGAZINE)	},
    { "main",		GO (OFFICE)	},
    { "message",	OB (MESSAGE)	},
    { "ming",		OB (VASE)	},
    { "mirror",		OB (MIRROR)	},
    { "mist",		MA (69)		},
    { "moss",		OB (40)		},
    { "mumble",		AW (SAY)	},
    { "n",		GO (NORTH)	},
    { "ne",		GO (NE)		},
    { "nest",		OB (EGGS)	},
    { "north",		GO (NORTH)	},
    { "nothing",	AW (NOTHING)	},
    { "nowhere",	GO (NOWHERE)	},
    { "nugget",		OB (NUGGET)	},
    { "null",		GO (NOWHERE)	},
    { "nw",		GO (NW)		},
    { "off",		AW (OFF)	},
    { "office",		GO (OFFICE)	},
    { "oil",		OB (OIL)	},
    { "on",		AW (ON)		},
    { "onward",		GO (FORWARD)	},
    { "open",		AW (OPEN)	},
    { "opensesame",	MA (50)		},
    { "oriental",	GO (ORIENTAL)	},
    { "out",		GO (OUTSIDE)	},
    { "outdoors",	GO (OUTDOORS)	},
    { "outside",	GO (OUTSIDE)	},
    { "over",		GO (OVER)	},
    { "oyster",		OB (OYSTER)	},
    { "passage",	GO (PASSAGE)	},
    { "pause",		AW (SUSPEND)	},
    { "pearl",		OB (PEARL)	},
    { "persian",	OB (RUG)	},
    { "peruse",		AW (READ)	},
    { "pillow",		OB (PILLOW)	},
    { "pirate",		OB (30)		},
    { "pit",		GO (PIT)	},
    { "placate",	AW (CALM)	},
    { "plant",		OB (PLANT)	},
    { "plant",		OB (PLANT2)	},
    { "platinum",	OB (PYRAMID)	},
    { "plover",		GO (PLOVER)	},
    { "plugh",		GO (PLUGH)	},
    { "pocus",		MA (50)		},
    { "pottery",	OB (VASE)	},
    { "pour",		AW (POUR)	},
    { "proceed",	AW (WALK)	},
    { "pyramid",	OB (PYRAMID)	},
    { "quit",		AW (QUIT)	},
    { "rations",	OB (FOOD)	},
    { "read",		AW (READ)	},
    { "release",	AW (DROP)	},
    { "reservoir",	GO (RESERVOIR)	},
    { "restore",	AW (LOAD)	},
    { "retreat",	GO (BACK)	},
    { "return",		GO (BACK)	},
    { "right",		GO (RIGHT)	},
    { "road",		GO (HILL)	},
    { "rock",		GO (ROCK)	},
    { "rod",		OB (ROD)	},
    { "rod",		OB (ROD2)	},
    { "room",		GO (ROOM)	},
    { "rub",		AW (RUB)	},
    { "rug",		OB (RUG)	},
    { "run",		AW (WALK)	},
    { "s",		GO (SOUTH)	},
    { "save",		AW (SUSPEND)	},
    { "say",		AW (SAY)	},
    { "score",		AW (SCORE)	},
    { "se",		GO (SE)		},
    { "secret",		GO (SECRET)	},
    { "sesame",		MA (50)		},
    { "shadow",		OB (27)		},
    { "shake",		AW (WAVE)	},
    { "shard",		OB (VASE)	},
    { "shatter",	AW (BREAK)	},
    { "shazam",		MA (50)		},
    { "shell",		GO (SHELL)	},
    { "shit",		MA (79)		},
    { "silver",		OB (GOLD_BARS)	},
    { "sing",		AW (SAY)	},
    { "slab",		GO (SLAB)	},
    { "slit",		GO (SLIT)	},
    { "smash",		AW (BREAK)	},
    { "snake",		OB (SNAKE)	},
    { "south",		GO (SOUTH)	},
    { "spelunker",	OB (MAGAZINE)	},
    { "spice",		OB (SPICES)	},
    { "spices",		OB (SPICES)	},
    { "stairs",		GO (STAIRS)	},
    { "stalactite",	OB (26)		},
    { "steal",		AW (TAKE)	},
    { "steps",		OB (STEPS)	},
    { "steps",		GO (STEPS)	},
    { "stop",		MA (139)	},
    { "stream",		GO (STREAM)	},
    { "strike",		AW (KILL)	},
    { "surface",	GO (SURFACE)	},
    { "suspend",	AW (SUSPEND)	},
    { "sw",		GO (SW)		},
    { "swim",		MA (147)	},
    { "swing",		AW (WAVE)	},
    { "tablet",		OB (TABLET)	},
    { "take",		AW (TAKE)	},
    { "tame",		AW (CALM)	},
    { "throw",		AW (THROW)	},
    { "toss",		AW (THROW)	},
    { "tote",		AW (TAKE)	},
    { "touch",		GO (LOOK)	},
    { "travel",		AW (WALK)	},
    { "treasure",	OB (CHEST)	},
    { "tree",		MA (64)		},
    { "trees",		MA (64)		},
    { "trident",	OB (TRIDENT)	},
    { "troll",		OB (TROLL)	},
    { "troll",		OB (TROLL2)	},
    { "tunnel",		GO (PASSAGE)	},
    { "turn",		AW (WALK)	},
    { "u",		GO (UP)	},
    { "unlock",		AW (OPEN)	},
    { "up",		GO (UP)	},
    { "upstream",	GO (DOWNSTREAM)	},
    { "upward",		GO (UP)	},
    { "utter",		AW (SAY)	},
    { "valley",		GO (VALLEY)	},
    { "vase",		OB (VASE)	},
    { "velvet",		OB (PILLOW)	},
    { "vending",	OB (VEND)	},
    { "view",		GO (VIEW)	},
    { "volcano",	OB (37)		},
    { "w",		GO (WEST)	},
    { "wake",		AW (WAKE)	},
    { "walk",		AW (WALK)	},
    { "wall",		GO (WALL)	},
    { "water",		OB (WATER)	},
    { "wave",		AW (WAVE)	},
    { "west",		GO (WEST)	},
    { "xyzzy",		GO (XYZZY)	},
    { "y2",		GO (Y2)		}
};

//}}}-------------------------------------------------------------------

static int binary (const char* w, const struct wac wctable[], int maxwc)
{
    int lo = 0;
    int hi = maxwc - 1;
    while (lo <= hi) {
	int mid = (lo + hi) / 2;
	int check = strcmp(w, wctable[mid].aword);
	if (check < 0)
	    hi = mid - 1;
	else if (check > 0)
	    lo = mid + 1;
	else
	    return mid;
    }
    return -1;
}

// look-up vocabulary word in lex-ordered table.  words may have
// two entries with different codes. if minimum acceptable value
// = 0, then return minimum of different codes.  last word CANNOT
// have two entries(due to binary sort).
// word is the word to look up.
// val  is the minimum acceptable value,
// if != 0 return %1000
static int vocab (const char* word, int val)
{
    int v1 = binary (word, ArrayBlock(c_words));
    if (v1 < 0)
	return -1;
    int v2 = binary (word, ArrayBlock(c_words)-1);
    if (v2 < 0)
	v2 = v1;
    if (!val)
	return c_words[v1].acode < c_words[v2].acode ? c_words[v1].acode : c_words[v2].acode;
    if (val <= c_words[v1].acode)
	return c_words[v1].acode % 1000;
    else if (val <= c_words[v2].acode)
	return c_words[v2].acode % 1000;
    else
	return -1;
}

int parse_magic_word (const char* word)
    { return vocab (word, WORD_BASE (MAGIC_WORD)); }

// Analyze a two word sentence
bool english (void)
{
    verb = object = motion = 0;
    int type2 = -1, val2 = -1;
    int type1 = -1, val1 = -1;
    const char* msg = "bad grammar...";

    getwords();

    if (!(*word1))
	return false;	       // ignore whitespace
    if (!analyze(word1, &type1, &val1))	// check word1
	return false;	       // didn't know it

    if (type1 == 2 && val1 == SAY) {
	verb = SAY;	       // repeat word & act upon if..
	object = 1;
	return true;
    }

    if (*word2)
	if (!analyze(word2, &type2, &val2))
	    return false;	       // didn't know it

    // check his grammar
    if (type1 == 3 && type2 == 3 && val1 == MAGIC_HELP && val2 == MAGIC_HELP) {
	outwords();
	return false;
    } else if (type1 == 3) {
	rspeak(val1);
	return false;
    } else if (type2 == 3) {
	rspeak(val2);
	return false;
    } else if (type1 == 0) {
	if (type2 == 0) {
	    printf ("%s\n", msg);
	    return false;
	} else
	    motion = val1;
    } else if (type2 == 0)
	motion = val2;
    else if (type1 == 1) {
	object = val1;
	if (type2 == 2)
	    verb = val2;
	if (type2 == 1) {
	    printf ("%s\n", msg);
	    return false;
	}
    } else if (type1 == 2) {
	verb = val1;
	if (type2 == 1)
	    object = val2;
	if (type2 == 2) {
	    printf ("%s\n", msg);
	    return false;
	}
    } else {
	puts ("Huh?");
	return false;
    }
    return true;
}

// Routine to analyze a word.
bool analyze (char *word, int *type, int *value)
{
    // make sure I understand
    int wordval = vocab(word, 0);
    if (wordval == -1) {
	static const int8_t c_rmsg[] = {60,61,13};
	rspeak (c_rmsg[rand()%3]);
	return false;
    }
    *type = wordval / 1000;
    *value = wordval % 1000;
    return true;
}

// retrieve input line (max 80 chars), convert to lower case
// & rescan for first two words (max. WORDSIZE-1 chars).
void getwords (void)
{
    printf (BOLD_ON "> " BOLD_OFF);
    word1[0] = word2[0] = '\0';
    char words [MAXWORDLEN*2];
    fgets (ArrayBlock(words), stdin);
    for (char* c = words; *c; ++c)
	*c = tolower(*c);
    sscanf (words, "%19s %19s", word1, word2);
}

// output adventure word list (motion and actions only)
void outwords (void)
{
    for (unsigned i = 0, j = 0; i < ArraySize(c_words); ++i) {
	if (c_words[i].acode < WORD_BASE (OBJECT_WORD)
		|| (c_words[i].acode >= WORD_BASE (ACTION_WORD)
		    && c_words[i].acode < WORD_BASE (MAGIC_WORD))) {
	    printf ("%-12s", c_words[i].aword);
	    if ((++j == 6) || (i == ArraySize(c_words)-1)) {
		j = 0;
		fputc ('\n', stdout);
	    }
	}
    }
}
