// This file is free software, distributed under the BSD license.

#pragma once
#include "../config.h"

//{{{ Game constants ---------------------------------------------------

#define	ADVENTURE_SCOREFILE	_PATH_GAME_STATE "adventure.scores"
#define ADVENTURE_SAVE_NAME	"adventure"
#define SCOREFILE_MAGIC		"advent"

enum {
    MAXOBJ	= 100,	// max # of objects in cave
    MAXWORDLEN	= 20,	// max # of chars in commands
    MAXMSG	= 201,	// max # of long location descr
    MAXTRAV	= 16+1,	// max # of travel directions from loc, +1 for terminator travel[x].tdest=-1
    MAXDWARVES	= 7,	// max # of nasty dwarves
    MAXDIE	= 3,	// max # of deaths before close
    MAXTRS	= 79,	// max # of
    MAXSCORES	= 10
};

// Object definitions
enum Object {
    KEYS = 1, LAMP, GRATE, CAGE,
    ROD, ROD2, STEPS, BIRD, DOOR,
    PILLOW, SNAKE, FISSURE, TABLET, CLAM,
    OYSTER, MAGAZINE, DWARF, KNIFE, FOOD,
    BOTTLE, WATER, OIL, MIRROR, PLANT,
    PLANT2, AXE = 28,
    DRAGON = 31, CHASM, TROLL, TROLL2,
    BEAR, MESSAGE, VEND = 38, BATTERIES,
    NUGGET = 50, DIAMONDS, GOLD_BARS, JEWELS, COINS,
    CHEST, EGGS, TRIDENT, VASE, EMERALD,
    PYRAMID, PEARL, RUG, SPICES, CHAIN
};

enum Location {
    END_OF_ROAD	= 1,
    WELLHOUSE	= 3,
    IN_VALLEY	= 4,
    IN_FOREST	= 5,
    STREAM_SLIT	= 7,
    AT_GRATE	= 8,
    UNDER_GRATE	= 9,
    XYZZY_ROOM	= 11,
    MIST_HALL	= 15,
    FISSURE_E	= 17,
    KING_HALL	= 19,
    FISSURE_W	= 27,
    Y2_ROOM	= 33,
    CO_JUNCTION	= 64,
    GIANT_ROOM	= 92,
    ORIENT_ROOM	= 97,
    PLOVER_ROOM	= 100,
    WITTS_END	= 108,
    CHEST_ROOM1	= 114,
    REPOSITORY1	= 115,
    REPOSITORY2	= 116,
    CHASM_SW	= 117,
    DRAGON_LAIR	= 120,
    CHASM_NE	= 122,
    CHEST_ROOM2	= 140,
    MAXLOC	= CHEST_ROOM2,
    CARRIED
};

enum MotionWords {
    GO_HILL = 2, GO_ENTER, GO_DOWNSTREAM,
    GO_FOREST = 6, GO_FORWARD, GO_BACK, GO_VALLEY,
    GO_STAIRS, GO_OUTSIDE, GO_BUILDING, GO_GULLY, GO_STREAM,
    GO_ROCK, GO_BED, GO_CRAWL, GO_COBBLESTONE, GO_INSIDE,
    GO_SURFACE, GO_NOWHERE, GO_DARK, GO_PASSAGE, GO_LOW,
    GO_CANYON, GO_AWKWARD, GO_GIANT, GO_VIEW, GO_UP,
    GO_DOWN, GO_PIT, GO_OUTDOORS, GO_CRACK, GO_STEPS,
    GO_DOME, GO_LEFT, GO_RIGHT, GO_HALL, GO_JUMP,
    GO_BARREN, GO_OVER, GO_ACROSS, GO_EAST, GO_WEST,
    GO_NORTH, GO_SOUTH, GO_NE, GO_SE, GO_SW,
    GO_NW, GO_DEBRIS, GO_HOLE, GO_WALL, GO_BROKEN,
    GO_Y2, GO_CLIMB, GO_LOOK, GO_FLOOR, GO_ROOM,
    GO_SLIT, GO_SLAB, GO_XYZZY, GO_DEPRESSION, GO_ENTRANCE,
    GO_PLUGH, GO_SECRET, GO_CAVE, GO_CROSS = 69,
    GO_BEDQUILT, GO_PLOVER, GO_ORIENTAL, GO_CAVERN, GO_SHELL,
    GO_RESERVOIR, GO_OFFICE, GO_FORK,
};

enum ActionWords {
    TAKE = 1, DROP, SAY, OPEN,
    NOTHING, LOCK, ON, OFF, WAVE,
    CALM, WALK, KILL, POUR, EAT,
    DRINK, RUB, THROW, QUIT, FIND,
    INVENTORY, FEED, FILL, BLAST, SCORE,
    FOO, BRIEF, READ, BREAK, WAKE,
    SUSPEND, HOURS, LOG, LOAD
};

enum MagicWords { MAGIC_HELP = 51 };

// BIT mapping of "cond" array which indicates location status
enum ConditionBit {
    LIGHT	=1<<0,
    WATOIL	=1<<1,
    LIQUID	=1<<2,
    NOPIRAT	=1<<3,
    HINTC	=1<<4,
    HINTB	=1<<5,
    HINTS	=1<<6,
    HINTM	=1<<7,
    HINT	=HINTC |HINTB |HINTS |HINTM
};

//}}}-------------------------------------------------------------------
//{{{ Type definitions

struct trav {
    uint32_t	tverb:8;
    uint32_t	tdest:12;
    uint32_t	tcond:12;
};

typedef uint8_t loc_t;
typedef uint8_t obj_t;

struct Score {
    uint16_t	total;
    uint8_t	treasures;
    uint8_t	survival;
    uint8_t	wellin;
    uint8_t	masters;
    uint8_t	bonus;
    char	name [9];
};

//}}}-------------------------------------------------------------------
//{{{ Global variable declartions

// Database variables
extern struct trav travel [MAXTRAV];

// Command parser variables
extern int verb;
extern int object;
extern int motion;
extern char word1 [MAXWORDLEN];
extern char word2 [MAXWORDLEN];

// Play variables
extern unsigned	turns;
extern int16_t	clock1;		// timing variables
extern int16_t	clock2;
extern int16_t	limit;		// time limit
extern uint8_t	tally;		// item counts
extern uint8_t	tally2;
extern uint8_t	holding;	// count of held items
extern uint8_t	numdie;		// number of deaths
extern uint8_t	dkill;		// dwarves killed
extern uint8_t	dflag;		// dwarf flag
extern uint8_t	foobar;		// fie fie foe foo...
extern uint8_t	bonus;		// to pass to end
extern loc_t	loc;		// location variables
extern loc_t	newloc;
extern loc_t	oldloc;
extern loc_t	oldloc2;
extern loc_t	knfloc;		// knife location
extern loc_t	chloc;		// chest locations
extern loc_t	chloc2;
extern loc_t	daltloc;	// alternate appearance
extern obj_t	object1;	// to help intrans.
extern bool	lmwarn;		// lamp warning flag
extern bool	wzdark;		// game state flags
extern bool	closing;
extern bool	closed;
extern bool	panic;
extern bool	gaveup;		// 1 if he quit early

extern bool	saveflg;	// if game being saved

extern uint8_t	visited [(MAXLOC+1+7)/8]; // bit set if has been here
extern loc_t	dloc [MAXDWARVES];	// dwarf locations
extern bool	dseen [MAXDWARVES];	// dwarf seen flag
extern loc_t	odloc [MAXDWARVES];	// dwarf old locations

// Object runtime status arrays, in obj.c
extern loc_t	place [MAXOBJ];		// object location
extern loc_t	fixed [MAXOBJ];		// second object loc
extern int8_t	prop [MAXOBJ];		// status of object

// Location status, in loc.c
extern const uint8_t cond [MAXLOC+1];

extern struct Score game_score;

//}}}-------------------------------------------------------------------
//{{{ Function prototypes

// advent.c
bool restore (void);

// database.c
bool yes (unsigned qmsg, unsigned ymsg, unsigned nmsg);

// itverb.c
void itverb (void);

// loc.c
void desclg (loc_t l);
void descsh (loc_t l);
void gettrav (loc_t l);

// msg.c
void rspeak (unsigned msg);
void actspk (unsigned verb);

// obj.c
bool here (obj_t item);
bool toting (obj_t item);
bool at (obj_t item);
void destroy_object (obj_t obj);
void move_object (obj_t obj, loc_t where);
void carry (obj_t obj);
void drop (obj_t obj, loc_t where);
int put (obj_t obj, loc_t where, int pval);
int liq (void);
int liqloc (loc_t loc);
int liq2 (int pbottle);
void pspeak (obj_t item, int state);

// turn.c
void turn (void);
void describe (void);
void dwarfend (void);
_Noreturn void normend (void);
void score (void);
const char* probj (obj_t object);

// verb.c
void trverb (void);
void needobj (void);
void vtake (void);
void vopen (void);
void vkill (void);
void veat (void);
void vdrink (void);
void vblast (void);
void vfill (void);
unsigned dcheck (void);

// vocab.c
int parse_magic_word (const char* word);
bool english (void);
bool analyze (char* word, int* type, int* value);
void getwords (void);
void outwords (void);

//}}}-------------------------------------------------------------------
//{{{ Inline functions

// visited array interface
inline static bool visited_location (loc_t l)
    { return visited[l/8] & (1u<<(l%8)); }
inline static void set_location_visited (loc_t l)
    { visited[l/8] |= (1u<<(l%8)); }
inline static void set_location_not_visited (loc_t l)
    { visited[l/8] &= ~(1u<<(l%8)); }

// Routine true x% of the time.
inline static bool pct (unsigned x)
    { return rand()%100u < x; }

// Routine to test for darkness
inline static bool dark (void)
    { return !(cond[loc] & LIGHT) && (!prop[LAMP] || !here(LAMP)); }

// Routine to tell if a location causes a forced move.
inline static bool forced (loc_t atloc)
    { return cond[atloc] == 2; }

//}}}-------------------------------------------------------------------
