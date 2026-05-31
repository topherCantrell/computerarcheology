// This file is free software, distributed under the BSD license.

#include "advent.h"

struct location {
    const char* sdesc;
    const char* ldesc;
    struct trav travs [MAXTRAV];
};

//{{{ Location list ----------------------------------------------------

#define LMSG(m)		500+m
#define SPCM(m)		300+m
#define LCO(t,o)	(t*100)+o

static const struct location c_locs [MAXLOC] = {
    { // 1, END_OF_ROAD
	"You're at end of road again.",
	"You are standing at the end of a road before a small brick building. Around\n"
	"you is a forest. A small stream flows out of the building and down a gully.",
	{	{ GO_HILL,	2,		0 },
		{ GO_WEST,	2,		0 },
		{ GO_UP,	2,		0 },
		{ GO_ENTER,	WELLHOUSE,	0 },
		{ GO_BUILDING,	WELLHOUSE,	0 },
		{ GO_INSIDE,	WELLHOUSE,	0 },
		{ GO_EAST,	WELLHOUSE,	0 },
		{ GO_GULLY,	IN_VALLEY,	0 },
		{ GO_STREAM,	IN_VALLEY,	0 },
		{ GO_SOUTH,	IN_VALLEY,	0 },
		{ GO_DOWN,	IN_VALLEY,	0 },
		{ GO_FOREST,	IN_FOREST,	0 },
		{ GO_NORTH,	IN_FOREST,	0 },
		{ GO_EAST,	IN_FOREST,	0 },
		{ GO_DEPRESSION, AT_GRATE,	0 },
		{ }}
    },{ // 2
	"You're at hill in road.",
	"You have walked up a hill, still in the forest.\n"
	"The road slopes back down the other side of the hill.\n"
	"There is a building in the distance.",
	{	{ GO_HILL,	END_OF_ROAD,	0 },
		{ GO_BUILDING,	END_OF_ROAD,	0 },
		{ GO_FORWARD,	END_OF_ROAD,	0 },
		{ GO_EAST,	END_OF_ROAD,	0 },
		{ GO_NORTH,	END_OF_ROAD,	0 },
		{ GO_DOWN,	END_OF_ROAD,	0 },
		{ GO_FOREST,	IN_FOREST,	0 },
		{ GO_NORTH,	IN_FOREST,	0 },
		{ GO_SOUTH,	IN_FOREST,	0 },
		{ }}
    },{ // 3, WELLHOUSE
	"You're inside building.",
	"You are inside a building, a well house for a large spring.",
	{	{ GO_ENTER,	END_OF_ROAD,	0 },
		{ GO_OUTSIDE,	END_OF_ROAD,	0 },
		{ GO_OUTDOORS,	END_OF_ROAD,	0 },
		{ GO_WEST,	END_OF_ROAD,	0 },
		{ GO_XYZZY,	XYZZY_ROOM,	0 },
		{ GO_PLUGH,	Y2_ROOM,	0 },
		{ GO_STREAM,	79,		0 },
		{ }}
    },{ // 4, IN_VALLEY
	"You're in valley.",
	"You are in a valley in the forest beside a stream tumbling along a rocky bed.",
	{	{ GO_DOWNSTREAM,	END_OF_ROAD,	0 },
		{ GO_BUILDING,	END_OF_ROAD,	0 },
		{ GO_NORTH,	END_OF_ROAD,	0 },
		{ GO_FOREST,	IN_FOREST,	0 },
		{ GO_EAST,	IN_FOREST,	0 },
		{ GO_WEST,	IN_FOREST,	0 },
		{ GO_UP,	IN_FOREST,	0 },
		{ GO_SOUTH,	STREAM_SLIT,	0 },
		{ GO_DOWN,	STREAM_SLIT,	0 },
		{ GO_DEPRESSION, AT_GRATE,	0 },
		{ }}
    },{ // 5, IN_FOREST
	"You're in forest.",
	"You are in open forest, with a deep valley to one side.",
	{	{ GO_VALLEY,	IN_VALLEY,	0 },
		{ GO_EAST,	IN_VALLEY,	0 },
		{ GO_DOWN,	IN_VALLEY,	0 },
		{ GO_FOREST,	IN_FOREST,	50 },
		{ GO_FORWARD,	IN_FOREST,	50 },
		{ GO_NORTH,	IN_FOREST,	50 },
		{ GO_FOREST,	6,		0 },
		{ GO_WEST,	IN_FOREST,	0 },
		{ GO_SOUTH,	IN_FOREST,	0 },
		{ }}
    },{ // 6
	"You're in forest.",
	"You are in open forest near both a valley and a road.",
	{	{ GO_HILL,	END_OF_ROAD,	0 },
		{ GO_NORTH,	END_OF_ROAD,	0 },
		{ GO_VALLEY,	IN_VALLEY,	0 },
		{ GO_EAST,	IN_VALLEY,	0 },
		{ GO_WEST,	IN_VALLEY,	0 },
		{ GO_DOWN,	IN_VALLEY,	0 },
		{ GO_FOREST,	IN_FOREST,	0 },
		{ GO_SOUTH,	IN_FOREST,	0 },
		{ }}
    },{ // 7, STREAM_SLIT
	"You're at slit in streambed.",
	"At your feet all the water of the stream splashes into a 2-inch slit in the rock.\n"
	"Downstream the streambed is bare rock.",
	{	{ GO_BUILDING,	END_OF_ROAD,	0 },
		{ GO_DOWNSTREAM,IN_VALLEY,	0 },
		{ GO_NORTH,	IN_VALLEY,	0 },
		{ GO_FOREST,	IN_FOREST,	0 },
		{ GO_EAST,	IN_FOREST,	0 },
		{ GO_WEST,	IN_FOREST,	0 },
		{ GO_ROCK,	AT_GRATE,	0 },
		{ GO_BED,	AT_GRATE,	0 },
		{ GO_SOUTH,	AT_GRATE,	0 },
		{ GO_SLIT,	LMSG (95),	0 },
		{ GO_STREAM,	LMSG (95),	0 },
		{ GO_DOWN,	LMSG (95),	0 },
		{ }}
    },{ // 8, AT_GRATE
	"You're outside grate.",
	"You are in a 20-foot depression floored with bare dirt.\n"
	"Set into the dirt is a strong steel grate mounted in concrete.\n"
	"A dry streambed leads into the depression.",
	{	{ GO_FOREST,	IN_FOREST,	0 },
		{ GO_EAST,	IN_FOREST,	0 },
		{ GO_SOUTH,	IN_FOREST,	0 },
		{ GO_WEST,	IN_FOREST,	0 },
		{ GO_BUILDING,	END_OF_ROAD,	0 },
		{ GO_DOWNSTREAM, STREAM_SLIT,	0 },
		{ GO_GULLY,	STREAM_SLIT,	0 },
		{ GO_NORTH,	STREAM_SLIT,	0 },
		{ GO_ENTER,	UNDER_GRATE,	LCO (3,GRATE) },
		{ GO_INSIDE,	UNDER_GRATE,	LCO (3,GRATE) },
		{ GO_DOWN,	UNDER_GRATE,	LCO (3,GRATE) },
		{ GO_ENTER,	LMSG (93),	0 },
		{ }}
    },{ // 9, UNDER_GRATE
	"You're below the grate.",
	"You are in a small chamber beneath a 3x3 steel grate to the surface.\n"
	"A low crawl over cobbles leads inward to the West.",
	{	{ GO_OUTSIDE,	AT_GRATE,	LCO (3,GRATE) },
		{ GO_UP,	AT_GRATE,	LCO (3,GRATE) },
		{ GO_OUTSIDE,	LMSG (93),	0 },
		{ GO_CRAWL,	10,		0 },
		{ GO_COBBLESTONE, 10,		0 },
		{ GO_INSIDE,	10,		0 },
		{ GO_WEST,	10,		0 },
		{ GO_PIT,	14,		0 },
		{ GO_DEBRIS,	XYZZY_ROOM,	0 },
		{ }}
    },{ // 10
	"You're in cobble crawl.",
	"You are crawling over cobbles in a low passage.\n"
	"There is a dim light at the east end of the passage.",
	{	{ GO_OUTSIDE,	UNDER_GRATE,	0 },
		{ GO_SURFACE,	UNDER_GRATE,	0 },
		{ GO_NOWHERE,	UNDER_GRATE,	0 },
		{ GO_EAST,	UNDER_GRATE,	0 },
		{ GO_INSIDE,	XYZZY_ROOM,	0 },
		{ GO_DARK,	XYZZY_ROOM,	0 },
		{ GO_WEST,	XYZZY_ROOM,	0 },
		{ GO_DEBRIS,	XYZZY_ROOM,	0 },
		{ GO_PIT,	14,		0 },
		{ }}
    },{ // 11, XYZZY_ROOM
	"You're in debris room.",
	"You are in a debris room filled with stuff washed in from the surface.\n"
	"A low wide passage with cobbles becomes plugged with mud and debris here,\n"
	"but an awkward canyon leads upward and west. A note on the wall says:\n"
	"	Magic Word \"XYZZY\"",
	{	{ GO_DEPRESSION, AT_GRATE,	LCO (3,GRATE) },
		{ GO_ENTRANCE,	UNDER_GRATE,	0 },
		{ GO_CRAWL,	10,		0 },
		{ GO_COBBLESTONE, 10,		0 },
		{ GO_PASSAGE,	10,		0 },
		{ GO_LOW,	10,		0 },
		{ GO_EAST,	10,		0 },
		{ GO_CANYON,	12,		0 },
		{ GO_INSIDE,	12,		0 },
		{ GO_UP,	12,		0 },
		{ GO_WEST,	12,		0 },
		{ GO_XYZZY,	WELLHOUSE,	0 },
		{ GO_PIT,	14,		0 },
		{ }}
    },{ // 12
	"You are in an awkward sloping east/west canyon.",
	"You are in an awkward sloping east/west canyon.",
	{	{ GO_DEPRESSION, AT_GRATE,	LCO (3,GRATE) },
		{ GO_ENTRANCE,	UNDER_GRATE,	0 },
		{ GO_DOWN,	XYZZY_ROOM,	0 },
		{ GO_EAST,	XYZZY_ROOM,	0 },
		{ GO_DEBRIS,	XYZZY_ROOM,	0 },
		{ GO_INSIDE,	13,		0 },
		{ GO_UP,	13,		0 },
		{ GO_WEST,	13,		0 },
		{ GO_PIT,	14,		0 },
		{ }}
    },{ // 13
	"You're in bird chamber.",
	"You are in a splendid chamber thirty feet high. The walls are frozen\n"
	"rivers of orange stone. An awkward canyon and a good passage exit from\n"
	"east and west sides of the chamber.",
	{	{ GO_DEPRESSION, AT_GRATE,	LCO (3,GRATE) },
		{ GO_ENTRANCE,	UNDER_GRATE,	0 },
		{ GO_DEBRIS,	XYZZY_ROOM,	0 },
		{ GO_CANYON,	12,		0 },
		{ GO_EAST,	12,		0 },
		{ GO_PASSAGE,	14,		0 },
		{ GO_PIT,	14,		0 },
		{ GO_WEST,	14,		0 },
		{ }}
    },{ // 14
	"You're at top of small pit.",
	"At your feet is a small pit breathing traces of white mist.\n"
	"An east passage ends here except for a small crack leading on.",
	{	{ GO_DEPRESSION, AT_GRATE,	LCO (3,GRATE) },
		{ GO_ENTRANCE,	UNDER_GRATE,	0 },
		{ GO_DEBRIS,	XYZZY_ROOM,	0 },
		{ GO_PASSAGE,	13,		0 },
		{ GO_EAST,	13,		0 },
		{ GO_DOWN,	20,		LCO (1,NUGGET) },
		{ GO_PIT,	20,		LCO (1,NUGGET) },
		{ GO_STEPS,	20,		LCO (1,NUGGET) },
		{ GO_DOWN,	MIST_HALL,	0 },
		{ GO_CRACK,	16,		0 },
		{ GO_WEST,	16,		0 },
		{ }}
    },{ // 15, MIST_HALL
	"You're in hall of mists.",
	"You are at one end of a vast hall stretching forward out of sight to the\n"
	"west. There are openings to either side. Nearby, a wide stone staircase\n"
	"leads downward. The hall is filled with wisps of white mist swaying to and\n"
	"fro almost as if alive. A cold wind blows up the staircase.\n"
	"There is a passage at the top of a dome behind you.",
	{	{ GO_LEFT,	18,		0 },
		{ GO_SOUTH,	18,		0 },
		{ GO_FORWARD,	FISSURE_E,	0 },
		{ GO_HALL,	FISSURE_E,	0 },
		{ GO_WEST,	FISSURE_E,	0 },
		{ GO_STAIRS,	KING_HALL,	0 },
		{ GO_DOWN,	KING_HALL,	0 },
		{ GO_NORTH,	KING_HALL,	0 },
		{ GO_UP,	22,		LCO (1,NUGGET) },
		{ GO_PIT,	22,		LCO (1,NUGGET) },
		{ GO_STEPS,	22,		LCO (1,NUGGET) },
		{ GO_DOME,	22,		LCO (1,NUGGET) },
		{ GO_PASSAGE,	22,		LCO (1,NUGGET) },
		{ GO_EAST,	22,		LCO (1,NUGGET) },
		{ GO_UP,	14,		0 },
		{ GO_Y2,	Y2_ROOM,	0 },
		{ }}
    },{ // 16
	"The crack is far too small for you to follow.",
	"The crack is far too small for you to follow.",
	{	{ GO_NORTH,	14,		0 },
		{ }}
    },{ // 17, FISSURE_E
	"You're on east bank of fissure.",
	"You are on the east bank of a fissure slicing clear across the hall.\n"
	"The mist is quite thick here, and the fissure is too wide to jump.",
	{	{ GO_HALL,	MIST_HALL,	0 },
		{ GO_EAST,	MIST_HALL,	0 },
		{ GO_JUMP,	LMSG (96),	LCO (3,FISSURE) },
		{ GO_FORWARD,	21,		LCO (4,FISSURE) },
		{ GO_OVER,	LMSG (97),	LCO (4,FISSURE) },
		{ GO_ACROSS,	LMSG (97),	LCO (4,FISSURE) },
		{ GO_WEST,	LMSG (97),	LCO (4,FISSURE) },
		{ GO_CROSS,	LMSG (97),	LCO (4,FISSURE) },
		{ GO_OVER,	FISSURE_W,	0 },
		{ }}
    },{ // 18
	"You're in nugget of gold room.",
	"This is a low room with a crude note on the wall. The note says:\n"
	"You won't get it up the steps.",
	{	{ GO_HALL,	MIST_HALL,	0 },
		{ GO_OUTSIDE,	MIST_HALL,	0 },
		{ GO_NORTH,	MIST_HALL,	0 },
		{ }}
    },{ // 19, KING_HALL
	"You're in hall of mt. king.",
	"You are in the hall of the mountain king,\n"
	"with passages off in all directions.",
	{	{ GO_STAIRS,	MIST_HALL,	0 },
		{ GO_UP,	MIST_HALL,	0 },
		{ GO_EAST,	MIST_HALL,	0 },
		{ GO_NORTH,	28,		LCO (3,SNAKE) },
		{ GO_LEFT,	28,		LCO (3,SNAKE) },
		{ GO_SOUTH,	29,		LCO (3,SNAKE) },
		{ GO_RIGHT,	29,		LCO (3,SNAKE) },
		{ GO_WEST,	30,		LCO (3,SNAKE) },
		{ GO_FORWARD,	30,		LCO (3,SNAKE) },
		{ GO_NORTH,	32,		0 },
		{ GO_SW,	74,		35 },
		{ GO_SW,	32,		LCO (2,SNAKE) },
		{ GO_SECRET,	74,		0 },
		{ }}
    },{ // 20
	"You are at the bottom of the pit with a broken neck.",
	"You are at the bottom of the pit with a broken neck.",
	{	{ }}
    },{ // 21
	"You didn't make it.",
	"You didn't make it.",
	{	{ }}
    },{ // 22
	"The dome is unclimbable.",
	"The dome is unclimbable.",
	{	{ GO_NORTH,	MIST_HALL,	0 },
		{ }}
    },{ // 23
	"You're at west end of twopit room.",
	"You are at the west end of the twopit room.\n"
	"There is a large hole in the wall above the pit at this end of the room.",
	{	{ GO_EAST,	67,		0 },
		{ GO_ACROSS,	67,		0 },
		{ GO_WEST,	68,		0 },
		{ GO_SLAB,	68,		0 },
		{ GO_DOWN,	25,		0 },
		{ GO_PIT,	25,		0 },
		{ GO_HOLE,	LMSG (148),	0 },
		{ }}
    },{ // 24
	"You're in east pit.",
	"You are that the bottom of the eastern pit in the twopit room.\n"
	"There is a small pool of oil in one corner of the pit.",
	{	{ GO_UP,	67,		0 },
		{ GO_OUTSIDE,	67,		0 },
		{ }}
    },{ // 25
	"You're in west pit.",
	"You are at the bottom of the western pit in the towpit room.\n"
	"There is a large hole in the wall about 25 feet above you.",
	{	{ GO_UP,	23,		0 },
		{ GO_OUTSIDE,	23,		0 },
		{ GO_CLIMB,	31,		LCO (7,PLANT) },
		{ GO_CLIMB,	26,		0 },
		{ }}
    },{ // 26
	"You clamber up the plant and scurry through the hole at the top.",
	"You clamber up the plant and scurry through the hole at the top.",
	{	{ 1,		88,		0 },
		{ }}
    },{ // 27, FISSURE_W
	"You are on the west side of the fissure in the hall of mists.",
	"You are on the west side of the fissure in the hall of mists.",
	{	{ GO_JUMP,	LMSG (96),	LCO (3,FISSURE) },
		{ GO_FORWARD,	21,		LCO (4,FISSURE) },
		{ GO_OVER,	LMSG (97),	LCO (4,FISSURE) },
		{ GO_ACROSS,	LMSG (97),	LCO (4,FISSURE) },
		{ GO_EAST,	LMSG (97),	LCO (4,FISSURE) },
		{ GO_CROSS,	LMSG (97),	LCO (4,FISSURE) },
		{ GO_OVER,	FISSURE_E,	0 },
		{ GO_NORTH,	40,		0 },
		{ GO_WEST,	41,		0 },
		{ }}
    },{ // 28
	"You are in a low N/S passage at a hole in the floor.\n"
	"The hole goes down to an E/W passage.",
	"You are in a low N/S passage at a hole in the floor.\n"
	"The hole goes down to an E/W passage.",
	{	{ GO_HALL,	KING_HALL,	0 },
		{ GO_OUTSIDE,	KING_HALL,	0 },
		{ GO_SOUTH,	KING_HALL,	0 },
		{ GO_NORTH,	Y2_ROOM,	0 },
		{ GO_Y2,	Y2_ROOM,	0 },
		{ GO_DOWN,	36,		0 },
		{ GO_HOLE,	36,		0 },
		{ }}
    },{ // 29
	"You are in the south side chamber.",
	"You are in the south side chamber.",
	{	{ GO_HALL,	KING_HALL,	0 },
		{ GO_OUTSIDE,	KING_HALL,	0 },
		{ GO_NORTH,	KING_HALL,	0 },
		{ }}
    },{ // 30
	"You are in the west side chamber of the hall of the mountain king.\n"
	"A passage continues west and up here.",
	"You are in the west side chamber of the hall of the mountain king.\n"
	"A passage continues west and up here.",
	{	{ GO_HALL,	KING_HALL,	0 },
		{ GO_OUTSIDE,	KING_HALL,	0 },
		{ GO_EAST,	KING_HALL,	0 },
		{ GO_WEST,	62,		0 },
		{ GO_UP,	62,		0 },
		{ }}
    },{ // 31
	">$<",
	">$<",
	{	{ 1,		89,		LCO (5,PLANT) },
		{ 1,		90,		0 },
		{ }}
    },{ // 32
	"You can't get by the snake.",
	"You can't get by the snake.",
	{	{ 1,		KING_HALL,	0 },
		{ }}
    },{ // 33, Y2_ROOM
	"You're at \"Y2\".",
	"You are in a large room, with a passage to the south, a passage\n"
	"to the west, and a wall of broken rock to the east.\n"
	"There is a large \"Y2\" on a rock in the room's center.",
	{	{ GO_PLUGH,	WELLHOUSE,	0 },
		{ GO_SOUTH,	28,		0 },
		{ GO_EAST,	34,		0 },
		{ GO_WALL,	34,		0 },
		{ GO_BROKEN,	34,		0 },
		{ GO_WEST,	35,		0 },
		{ GO_PLOVER,	SPCM (2),	LCO (1,EMERALD) },
		{ GO_PLOVER,	PLOVER_ROOM,	0 },
		{ }}
    },{ // 34
	"You are in a jumble of rock, with cracks everywhere.",
	"You are in a jumble of rock, with cracks everywhere.",
	{	{ GO_DOWN,	Y2_ROOM,	0 },
		{ GO_Y2,	Y2_ROOM,	0 },
		{ GO_UP,	MIST_HALL,	0 },
		{ }}
    },{ // 35
	"You're at window on pit.",
	"You're at a low window overlooking a huge pit, which extends up out of sight.\n"
	"A floor is indistinctly visible over 50 feet below. Traces of white mist\n"
	"cover the floor of the pit, becoming thicker to the right. Marks in the dust\n"
	"around the window would seem to indicate that someone has been here recently.\n"
	"Directly across the pit from you and 25 feet away there is a similar window\n"
	"looking into a lighted room.\n"
	"\n"
	"A shadowy figure can be seen there peering back at you.",
	{	{ GO_EAST,	Y2_ROOM,	0 },
		{ GO_Y2,	Y2_ROOM,	0 },
		{ GO_JUMP,	20,		0 },
		{ }}
    },{ // 36
	"You're in dirty passage.",
	"You are in a dirty broken passage.\n"
	"To the east is a crawl.\n"
	"To the west is a large passage.\n"
	"Above you is another passage.",
	{	{ GO_EAST,	37,		0 },
		{ GO_CRAWL,	37,		0 },
		{ GO_UP,	28,		0 },
		{ GO_HOLE,	28,		0 },
		{ GO_WEST,	39,		0 },
		{ GO_BEDQUILT,	65,		0 },
		{ }}
    },{ // 37
	"You are on the brink of a small clean climbable pit. A crawl leads west.",
	"You are on the brink of a small clean climbable pit.\n"
	"A crawl leads west.",
	{	{ GO_WEST,	36,		0 },
		{ GO_CRAWL,	36,		0 },
		{ GO_DOWN,	38,		0 },
		{ GO_PIT,	38,		0 },
		{ GO_CLIMB,	38,		0 },
		{ }}
    },{ // 38
	"You are in the bottom of a small pit with a little stream,\n"
	"which enters and exits through tiny slits.",
	"You are in the bottom of a small pit with a little stream,\n"
	"which enters and exits through tiny slits.",
	{	{ GO_CLIMB,	37,		0 },
		{ GO_UP,	37,		0 },
		{ GO_OUTSIDE,	37,		0 },
		{ GO_SLIT,	LMSG (95),	0 },
		{ GO_STREAM,	LMSG (95),	0 },
		{ GO_DOWN,	LMSG (95),	0 },
		{ GO_DOWNSTREAM, LMSG (95),	0 },
		{ 5,		LMSG (95),	0 },
		{ }}
    },{ // 39
	"You're in dusty rock room.",
	"You are in a large room full of dusty rocks.\n"
	"There is a big hole in the floor.\n"
	"There are cracks everywhere, and a passage leading east.",
	{	{ GO_EAST,	36,		0 },
		{ GO_PASSAGE,	36,		0 },
		{ GO_DOWN,	CO_JUNCTION,	0 },
		{ GO_HOLE,	CO_JUNCTION,	0 },
		{ GO_FLOOR,	CO_JUNCTION,	0 },
		{ GO_BEDQUILT,	65,		0 },
		{ }}
    },{ // 40
	"You have crawled through a very low wide passage\n"
	"parallel to and north of the hall of mists.",
	"You have crawled through a very low wide passage\n"
	"parallel to and north of the hall of mists.",
	{	{ GO_FORWARD,	41,		0 },
		{ }}
    },{ // 41
	"You're at west end of hall of mists.",
	"You are at the west end of hall of mists. A low wide crawl continues\n"
	"west and another goes north. To the south is a little passage 6 feet\n"
	"off the floor.",
	{	{ GO_SOUTH,	42,		0 },
		{ GO_UP,	42,		0 },
		{ GO_PASSAGE,	42,		0 },
		{ GO_CLIMB,	42,		0 },
		{ GO_EAST,	FISSURE_W,	0 },
		{ GO_NORTH,	59,		0 },
		{ GO_WEST,	60,		0 },
		{ GO_CRAWL,	60,		0 },
		{ }}
    },{ // 42
	"You are in a maze of twisty little passages, all alike.",
	"You are in a maze of twisty little passages, all alike.",
	{	{ GO_UP,	41,		0 },
		{ GO_NORTH,	42,		0 },
		{ GO_EAST,	43,		0 },
		{ GO_SOUTH,	45,		0 },
		{ GO_WEST,	80,		0 },
		{ }}
    },{ // 43
	"You are in a maze of twisty little passages, all alike.",
	"You are in a maze of twisty little passages, all alike.",
	{	{ GO_WEST,	42,		0 },
		{ GO_SOUTH,	44,		0 },
		{ GO_EAST,	45,		0 },
		{ }}
    },{ // 44
	"You are in a maze of twisty little passages, all alike.",
	"You are in a maze of twisty little passages, all alike.",
	{	{ GO_EAST,	43,		0 },
		{ GO_DOWN,	48,		0 },
		{ GO_SOUTH,	50,		0 },
		{ GO_NORTH,	82,		0 },
		{ }}
    },{ // 45
	"You are in a maze of twisty little passages, all alike.",
	"You are in a maze of twisty little passages, all alike.",
	{	{ GO_WEST,	42,		0 },
		{ GO_NORTH,	43,		0 },
		{ GO_EAST,	46,		0 },
		{ GO_SOUTH,	47,		0 },
		{ GO_UP,	87,		0 },
		{ GO_DOWN,	87,		0 },
		{ }}
    },{ // 46
	"Dead end.",
	"Dead end",
	{	{ GO_WEST,	45,		0 },
		{ GO_OUTSIDE,	45,		0 },
		{ }}
    },{ // 47
	"Dead end.",
	"Dead end",
	{	{ GO_EAST,	45,		0 },
		{ GO_OUTSIDE,	45,		0 },
		{ }}
    },{ // 48
	"Dead end.",
	"Dead end",
	{	{ GO_UP,	44,		0 },
		{ GO_OUTSIDE,	44,		0 },
		{ }}
    },{ // 49
	"You are in a maze of twisty little passages, all alike.",
	"You are in a maze of twisty little passages, all alike.",
	{	{ GO_EAST,	50,		0 },
		{ GO_WEST,	51,		0 },
		{ }}
    },{ // 50
	"You are in a maze of twisty little passages, all alike.",
	"You are in a maze of twisty little passages, all alike.",
	{	{ GO_EAST,	44,		0 },
		{ GO_WEST,	49,		0 },
		{ GO_DOWN,	51,		0 },
		{ GO_SOUTH,	52,		0 },
		{ }}
    },{ // 51
	"You are in a maze of twisty little passages, all alike.",
	"You are in a maze of twisty little passages, all alike.",
	{	{ GO_WEST,	49,		0 },
		{ GO_UP,	50,		0 },
		{ GO_EAST,	52,		0 },
		{ GO_SOUTH,	53,		0 },
		{ }}
    },{ // 52
	"You are in a maze of twisty little passages, all alike.",
	"You are in a maze of twisty little passages, all alike.",
	{	{ GO_WEST,	50,		0 },
		{ GO_EAST,	51,		0 },
		{ GO_SOUTH,	52,		0 },
		{ GO_UP,	53,		0 },
		{ GO_NORTH,	55,		0 },
		{ GO_DOWN,	86,		0 },
		{ }}
    },{ // 53
	"You are in a maze of twisty little passages, all alike.",
	"You are in a maze of twisty little passages, all alike.",
	{	{ GO_WEST,	51,		0 },
		{ GO_NORTH,	52,		0 },
		{ GO_SOUTH,	54,		0 },
		{ }}
    },{ // 54
	"Dead end.",
	"Dead end",
	{	{ GO_WEST,	53,		0 },
		{ GO_OUTSIDE,	53,		0 },
		{ }}
    },{ // 55
	"You are in a maze of twisty little passages, all alike.",
	"You are in a maze of twisty little passages, all alike.",
	{	{ GO_WEST,	52,		0 },
		{ GO_NORTH,	55,		0 },
		{ GO_DOWN,	56,		0 },
		{ GO_EAST,	57,		0 },
		{ }}
    },{ // 56
	"Dead end.",
	"Dead end",
	{	{ GO_UP,	55,		0 },
		{ GO_OUTSIDE,	55,		0 },
		{ }}
    },{ // 57
	"You're at brink of pit.",
	"You are on the brink of a thirty foot pit with a massive orange column\n"
	"down one wall. You could climb down here but you could not get back up.\n"
	"The maze continues at this level.",
	{	{ GO_DOWN,	13,		0 },
		{ GO_CLIMB,	13,		0 },
		{ GO_WEST,	55,		0 },
		{ GO_SOUTH,	58,		0 },
		{ GO_NORTH,	83,		0 },
		{ GO_EAST,	84,		0 },
		{ }}
    },{ // 58
	"Dead end.",
	"Dead end",
	{	{ GO_EAST,	57,		0 },
		{ GO_OUTSIDE,	57,		0 },
		{ }}
    },{ // 59
	"You have crawled through a very low wide passage paralled\n"
	"to and north of the hall of mists.",
	"You have crawled through a very low wide passage paralled\n"
	"to and north of the hall of mists.",
	{	{ GO_FORWARD,	FISSURE_W,	0 },
		{ }}
    },{ // 60
	"You're at east end of long hall.",
	"You are at the east end of a very long hall apparently without side chambers.\n"
	"To the east a low wide crawl slants up.\n"
	"To the north a round two foot hole slants down.",
	{	{ GO_EAST,	41,		0 },
		{ GO_UP,	41,		0 },
		{ GO_CRAWL,	41,		0 },
		{ GO_WEST,	61,		0 },
		{ GO_NORTH,	62,		0 },
		{ GO_DOWN,	62,		0 },
		{ GO_HOLE,	62,		0 },
		{ }}
    },{ // 61
	"You're at west end of long hall.",
	"You are at the west end of a very long featureless hall.\n"
	"The hall joins up with a narrow north/south passage.",
	{	{ GO_EAST,	60,		0 },
		{ GO_NORTH,	62,		0 },
		{ GO_SOUTH,	107,		100 },
		{ }}
    },{ // 62
	"You are at a crossover of a high N/S passage and a low E/W one.",
	"You are at a crossover of a high N/S passage and a low E/W one.",
	{	{ GO_WEST,	60,		0 },
		{ GO_NORTH,	63,		0 },
		{ GO_EAST,	30,		0 },
		{ GO_SOUTH,	61,		0 },
		{ }}
    },{ // 63
	"Dead end.",
	"Dead end",
	{	{ GO_SOUTH,	62,		0 },
		{ GO_OUTSIDE,	62,		0 },
		{ }}
    },{ // 64, CO_JUNCTION
	"You're at complex junction.",
	"You are at a complex junction. A low hands and knees passage from the\n"
	"north joins a higher crawl from the east to make a walking passage going\n"
	"west. There is also a large room above. The air is damp here.",
	{	{ GO_UP,	39,		0 },
		{ GO_CLIMB,	39,		0 },
		{ GO_ROOM,	39,		0 },
		{ GO_WEST,	65,		0 },
		{ GO_BEDQUILT,	65,		0 },
		{ GO_NORTH,	103,		0 },
		{ GO_SHELL,	103,		0 },
		{ GO_EAST,	106,		0 },
		{ }}
    },{ // 65
	"You are in bedquilt, a long east/west passage with holes everywhere.\n"
	"To explore at random select north, south, up or down.",
	"You are in bedquilt, a long east/west passage with holes everywhere.\n"
	"To explore at random select north, south, up or down.",
	{	{ GO_EAST,	CO_JUNCTION,	0 },
		{ GO_WEST,	66,		0 },
		{ GO_SOUTH,	LMSG (56),	80 },
		{ GO_SLAB,	68,		0 },
		{ GO_UP,	LMSG (56),	80 },
		{ GO_UP,	70,		50 },
		{ GO_UP,	39,		0 },
		{ GO_NORTH,	LMSG (56),	60 },
		{ GO_NORTH,	72,		75 },
		{ GO_NORTH,	71,		0 },
		{ GO_DOWN,	LMSG (56),	80 },
		{ GO_DOWN,	106,		0 },
		{ }}
    },{ // 66
	"You're in swiss cheese room.",
	"You are in a room whose walls resemble swiss cheese.\n"
	"Obvious passages go west, east, ne, and nw.\n"
	"Part of the room is occupied by a large bedrock block.",
	{	{ GO_NE,	65,		0 },
		{ GO_WEST,	67,		0 },
		{ GO_SOUTH,	LMSG (56),	80 },
		{ GO_CANYON,	77,		0 },
		{ GO_EAST,	96,		0 },
		{ GO_NW,	LMSG (56),	50 },
		{ GO_ORIENTAL,	ORIENT_ROOM,	0 },
		{ }}
    },{ // 67
	"You're at east end of twopit room.",
	"You are at the east end of the twopit room. The floor here is littered\n"
	"with thin rock slabs, which make it easy to descend the pits. There is\n"
	"a path here bypassing the pits to connect passages from east and west.\n"
	"There are holes all over, but the only bit one is on the wall directly\n"
	"over the west pit where you can't get at it.",
	{	{ GO_EAST,	66,		0 },
		{ GO_WEST,	23,		0 },
		{ GO_ACROSS,	23,		0 },
		{ GO_DOWN,	24,		0 },
		{ GO_PIT,	24,		0 },
		{ }}
    },{ // 68
	"You're in slab room.",
	"You are in a large low circular chamber whose floor is an immense slab\n"
	"fallen from the ceiling (slab room). East and west there once were large\n"
	"passages, but they are now filled with boulders. Low small passages go\n"
	"north and south, and the south one quickly bends west around the boulders.",
	{	{ GO_SOUTH,	23,		0 },
		{ GO_UP,	69,		0 },
		{ GO_CLIMB,	69,		0 },
		{ GO_NORTH,	65,		0 },
		{ }}
    },{ // 69
	"You are in a secret N/S canyon above a large room.",
	"You are in a secret N/S canyon above a large room.",
	{	{ GO_DOWN,	68,		0 },
		{ GO_SLAB,	68,		0 },
		{ GO_SOUTH,	DRAGON_LAIR,	LCO (3,DRAGON) },
		{ GO_SOUTH,	119,		0 },
		{ GO_NORTH,	109,		0 },
		{ GO_RESERVOIR,	113,		0 },
		{ }}
    },{ // 70
	"You are in a secret N/S canyon above a sizable passage.",
	"You are in a secret N/S canyon above a sizable passage.",
	{	{ GO_NORTH,	71,		0 },
		{ GO_DOWN,	65,		0 },
		{ GO_PASSAGE,	65,		0 },
		{ GO_SOUTH,	111,		0 },
		{ }}
    },{ // 71
	"You're at junction of three secret canyons.",
	"You are in a secret canyon at a junction of three canyons, bearing north,\n"
	"south and se. The north one is as tall as the other two combined.",
	{	{ GO_SE,	65,		0 },
		{ GO_SOUTH,	70,		0 },
		{ GO_NORTH,	110,		0 },
		{ }}
    },{ // 72
	"You are in a large low room. Crawls lead north, se, and sw.",
	"You are in a large low room. Crawls lead north, se, and sw.",
	{	{ GO_BEDQUILT,	65,		0 },
		{ GO_SW,	118,		0 },
		{ GO_NORTH,	73,		0 },
		{ GO_SE,	ORIENT_ROOM,	0 },
		{ GO_ORIENTAL,	ORIENT_ROOM,	0 },
		{ }}
    },{ // 73
	"Dead end crawl.",
	"Dead end crawl.",
	{	{ GO_SOUTH,	72,		0 },
		{ GO_CRAWL,	72,		0 },
		{ GO_OUTSIDE,	72,		0 },
		{ }}
    },{ // 74
	"You're at secret E/W canyon above tight canyon.",
	"You are in a secret canyon which here runs E/W. It crosses over a very tight\n"
	"canyon 15 feet below. If you go down you may not be able to get back up.",
	{	{ GO_EAST,	KING_HALL,	0 },
		{ GO_WEST,	DRAGON_LAIR,	LCO (3,DRAGON) },
		{ GO_WEST,	121,		0 },
		{ GO_DOWN,	75,		0 },
		{ }}
    },{ // 75
	"You are at a wide place in a very tight N/S canyon.",
	"You are at a wide place in a very tight N/S canyon.",
	{	{ GO_SOUTH,	76,		0 },
		{ GO_NORTH,	77,		0 },
		{ }}
    },{ // 76
	"The canyon here becomes too tight to go further south.",
	"The canyon here becomes too tight to go further south.",
	{	{ GO_NORTH,	75,		0 },
		{ }}
    },{ // 77
	"You are in a tall E/W canyon.\n"
	"A low tight crawl goes 3 feet north and seems to open up.",
	"You are in a tall E/W canyon.\n"
	"A low tight crawl goes 3 feet north and seems to open up.",
	{	{ GO_EAST,	75,		0 },
		{ GO_WEST,	78,		0 },
		{ GO_NORTH,	66,		0 },
		{ GO_CRAWL,	66,		0 },
		{ }}
    },{ // 78
	"The canyon runs into a mass of boulders -- dead end.",
	"The canyon runs into a mass of boulders -- dead end.",
	{	{ GO_SOUTH,	77,		0 },
		{ }}
    },{ // 79
	"The stream flows out through a pair of 1 foot diameter sewer pipes.\n"
	"It would be advisable to use the exit.",
	"The stream flows out through a pair of 1 foot diameter sewer pipes.\n"
	"It would be advisable to use the exit.",
	{	{ GO_FORWARD,	WELLHOUSE,	0 },
		{ GO_OUTSIDE,	WELLHOUSE,	0 },
		{ }}
    },{ // 80
	"You are in a maze of twisty little passages, all alike.",
	"You are in a maze of twisty little passages, all alike.",
	{	{ GO_NORTH,	42,		0 },
		{ GO_WEST,	80,		0 },
		{ GO_SOUTH,	80,		0 },
		{ GO_EAST,	81,		0 },
		{ }}
    },{ // 81
	"Dead end.",
	"Dead end.",
	{	{ GO_WEST,	80,		0 },
		{ GO_OUTSIDE,	80,		0 },
		{ }}
    },{ // 82
	"Dead end.",
	"Dead end.",
	{	{ GO_SOUTH,	44,		0 },
		{ GO_OUTSIDE,	44,		0 },
		{ }}
    },{ // 83
	"You are in a maze of twisty little passages, all alike.",
	"You are in a maze of twisty little passages, all alike.",
	{	{ GO_SOUTH,	57,		0 },
		{ GO_EAST,	84,		0 },
		{ GO_WEST,	85,		0 },
		{ }}
    },{ // 84
	"You are in a maze of twisty little passages, all alike.",
	"You are in a maze of twisty little passages, all alike.",
	{	{ GO_NORTH,	57,		0 },
		{ GO_WEST,	83,		0 },
		{ GO_NW,	CHEST_ROOM1,	0 },
		{ }}
    },{ // 85
	"Dead end.",
	"Dead end.",
	{	{ GO_EAST,	83,		0 },
		{ GO_OUTSIDE,	83,		0 },
		{ }}
    },{ // 86
	"Dead end.",
	"Dead end.",
	{	{ GO_UP,	52,		0 },
		{ GO_OUTSIDE,	52,		0 },
		{ }}
    },{ // 87
	"You are in a maze of twisty little passages, all alike.",
	"You are in a maze of twisty little passages, all alike.",
	{	{ GO_UP,	45,		0 },
		{ GO_DOWN,	45,		0 },
		{ }}
    },{ // 88
	"You're in narrow corridor.",
	"You are in a long, narrow corridor stretching out of sight to the west. At\n"
	"the eastern end is a hole through which you can see a profusion of leaves,",
	{	{ GO_DOWN,	25,		0 },
		{ GO_CLIMB,	25,		0 },
		{ GO_EAST,	25,		0 },
		{ GO_JUMP,	20,		0 },
		{ GO_WEST,	GIANT_ROOM,	0 },
		{ GO_GIANT,	GIANT_ROOM,	0 },
		{ }}
    },{ // 89
	"There is nothing here to climb. Use \"up\" or \"out\" to leave the pit.",
	"There is nothing here to climb. Use \"up\" or \"out\" to leave the pit.",
	{	{ GO_UP,	25,		0 },
		{ GO_OUTSIDE,	25,		0 },
		{ }}
    },{ // 90
	"You have climbed up the plant and out of the pit.",
	"You have climbed up the plant and out of the pit.",
	{	{ GO_UP,	23,		0 },
		{ GO_OUTSIDE,	23,		0 },
		{ }}
    },{ // 91
	"You're at steep incline above large room.",
	"You are at the top of a steep incline above a large room.\n"
	"You could climb down here, but you would not be able to climb up.\n"
	"There is a passage leading back to the north.",
	{	{ GO_NORTH,	95,		0 },
		{ GO_CAVERN,	95,		0 },
		{ GO_PASSAGE,	95,		0 },
		{ GO_DOWN,	72,		0 },
		{ GO_CLIMB,	72,		0 },
		{ }}
    },{ // 92, GIANT_ROOM
	"You're in giant room.",
	"You are in the giant room. The ceiling is too high up for your lamp to\n"
	"show it. Cavernous passages lead east, north, and south. On the west\n"
	"wall is scrawled the inscription:\n"
	"	\"Fee Fie Foe Foo\" {sic}",
	{	{ GO_SOUTH,	88,		0 },
		{ GO_EAST,	93,		0 },
		{ GO_NORTH,	94,		0 },
		{ }}
    },{ // 93
	"The passage here is blocked by a recent cave-in.",
	"The passage here is blocked by a recent cave-in.",
	{	{ GO_SOUTH,	GIANT_ROOM,	0 },
		{ GO_GIANT,	GIANT_ROOM,	0 },
		{ GO_OUTSIDE,	GIANT_ROOM,	0 },
		{ }}
    },{ // 94
	"You are at one end of an immense north/south passage.",
	"You are at one end of an immense north/south passage.",
	{	{ GO_SOUTH,	GIANT_ROOM,	0 },
		{ GO_GIANT,	GIANT_ROOM,	0 },
		{ GO_PASSAGE,	GIANT_ROOM,	0 },
		{ GO_NORTH,	95,		LCO (3,DOOR) },
		{ GO_ENTER,	95,		LCO (3,DOOR) },
		{ GO_CAVERN,	95,		LCO (3,DOOR) },
		{ GO_NORTH,	LMSG (111),	0 },
		{ }}
    },{ // 95
	"You're in cavern with waterfall.",
	"You are in a magnificent cavern with a rushing stream, which cascades\n"
	"over a sparkling waterfall into a roaring whirlpool which disappears\n"
	"through a hole in the floor. Passages exit to the south and west.",
	{	{ GO_SOUTH,	94,		0 },
		{ GO_OUTSIDE,	94,		0 },
		{ GO_GIANT,	GIANT_ROOM,	0 },
		{ GO_WEST,	91,		0 },
		{ }}
    },{ // 96
	"You're in soft room.",
	"You are in the soft room. The walls are covered with heavy curtains,\n"
	"the floor with a thick pile carpet. Moss covers the ceiling.",
	{	{ GO_WEST,	66,		0 },
		{ GO_OUTSIDE,	66,		0 },
		{ }}
    },{ // 97, ORIENT_ROOM
	"You're in oriental room.",
	"This is the oriental room. Ancient oriental cave drawings cover the walls.\n"
	"A gently sloping passage leads upward to the north, another passage leads se,\n"
	"and a hands and knees crawl leads west.",
	{	{ GO_SE,	66,		0 },
		{ GO_WEST,	72,		0 },
		{ GO_CRAWL,	72,		0 },
		{ GO_UP,	98,		0 },
		{ GO_NORTH,	98,		0 },
		{ GO_CAVERN,	98,		0 },
		{ }}
    },{ // 98
	"You're in misty cavern.",
	"You are following a wide path around the outer edge of a large cavern.\n"
	"Far below, through a heavy white mist, strange splashing noises can be heard.\n"
	"The mist rises up through a fissure in the ceiling.\n"
	"The path exits to the south and west.",
	{	{ GO_SOUTH,	ORIENT_ROOM,	0 },
		{ GO_ORIENTAL,	ORIENT_ROOM,	0 },
		{ GO_WEST,	99,		0 },
		{ }}
    },{ // 99
	"You're in alcove.",
	"You are in an alcove. A small nw path seems to widen after a short distance.\n"
	"An extremely tight tunnel leads east. It looks like a very tight squeeze.\n"
	"An eerie light can be seen at the other end.",
	{	{ GO_NW,	98,		0 },
		{ GO_CAVERN,	98,		0 },
		{ GO_EAST,	SPCM (1),	0 },
		{ GO_PASSAGE,	SPCM (1),	0 },
		{ GO_EAST,	PLOVER_ROOM,	0 },
		{ }}
    },{ // 100, PLOVER_ROOM
	"You're in plover room.",
	"You're in a small chamber lit by an eerie green light.\n"
	"An extremely narrow tunnel exits to the west.\n"
	"A dark corridor leads ne.",
	{	{ GO_WEST,	SPCM (1),	0 },
		{ GO_PASSAGE,	SPCM (1),	0 },
		{ GO_OUTSIDE,	SPCM (1),	0 },
		{ GO_WEST,	99,		0 },
		{ GO_PLOVER,	SPCM (2),	LCO (1,EMERALD) },
		{ GO_PLOVER,	Y2_ROOM,	0 },
		{ GO_NE,	101,		0 },
		{ GO_DARK,	101,		0 },
		{ }}
    },{ // 101
	"You're in dark-room.",
	"You're in the dark-room. A corridor leading south is the only exit.",
	{	{ GO_SOUTH,	PLOVER_ROOM,	0 },
		{ GO_PLOVER,	PLOVER_ROOM,	0 },
		{ GO_OUTSIDE,	PLOVER_ROOM,	0 },
		{ }}
    },{ // 102
	"You're in arched hall.",
	"You are in an arched hall. A coral passage once continued up and east\n"
	"from here, but is now blocked by debris. The air smells of sea water.",
	{	{ GO_DOWN,	103,		0 },
		{ GO_SHELL,	103,		0 },
		{ GO_OUTSIDE,	103,		0 },
		{ }}
    },{ // 103
	"You're in shell room.",
	"You're in a large room carved out of sedimentary rock. The floor and walls\n"
	"are littered with bits of shells imbedded in the stone. A shallow passage\n"
	"proceeds downward, and a somewhat steeper one leads up.\n"
	"A low hands and knees passage enters from the south.",
	{	{ GO_UP,	102,		0 },
		{ GO_HALL,	102,		0 },
		{ GO_DOWN,	104,		0 },
		{ GO_SOUTH,	LMSG (118),	LCO (1,CLAM) },
		{ GO_SOUTH,	LMSG (119),	LCO (1,OYSTER) },
		{ GO_SOUTH,	CO_JUNCTION,	0 },
		{ }}
    },{ // 104
	"You are in a long sloping corridor with ragged sharp walls.",
	"You are in a long sloping corridor with ragged sharp walls.",
	{	{ GO_UP,	103,		0 },
		{ GO_SHELL,	103,		0 },
		{ GO_DOWN,	105,		0 },
		{ }}
    },{ // 105
	"You are in a cul-de-sac about eight feet across.",
	"You are in a cul-de-sac about eight feet across.",
	{	{ GO_UP,	104,		0 },
		{ GO_OUTSIDE,	104,		0 },
		{ GO_SHELL,	103,		0 },
		{ }}
    },{ // 106
	"You're in anteroom.",
	"You are in an anteroom leading to a large passage to the east. Small\n"
	"passages go west and up. The remnants of recent digging are evident.\n"
	"A sign in midair here says:\n"
	"	\"Cave under construction beyond this point.\"\n"
	"		\"Proceed at your own risk.\"\n"
	"		\"Witt construction company\"",
	{	{ GO_UP,	CO_JUNCTION,	0 },
		{ GO_WEST,	65,		0 },
		{ GO_EAST,	WITTS_END,	0 },
		{ }}
    },{ // 107
	"You are in a maze of twisty little passages, all different.",
	"You are in a maze of twisty little passages, all different.",
	{	{ GO_SOUTH,	131,		0 },
		{ GO_SW,	132,		0 },
		{ GO_NE,	133,		0 },
		{ GO_SE,	134,		0 },
		{ GO_UP,	135,		0 },
		{ GO_NW,	136,		0 },
		{ GO_EAST,	137,		0 },
		{ GO_WEST,	138,		0 },
		{ GO_NORTH,	139,		0 },
		{ GO_DOWN,	61,		0 },
		{ }}
    },{ // 108, WITTS_END
	"You're at Witt's end.",
	"You are at Witt's end. Passages lead off in ALL directions.",
	{	{ GO_EAST,	LMSG (56),	95 },
		{ GO_NORTH,	LMSG (56),	95 },
		{ GO_SOUTH,	LMSG (56),	95 },
		{ GO_NE,	LMSG (56),	95 },
		{ GO_SE,	LMSG (56),	95 },
		{ GO_SW,	LMSG (56),	95 },
		{ GO_NW,	LMSG (56),	95 },
		{ GO_UP,	LMSG (56),	95 },
		{ GO_DOWN,	LMSG (56),	95 },
		{ GO_EAST,	106,		0 },
		{ GO_WEST,	LMSG (126),	0 },
		{ }}
    },{ // 109
	"You're in mirror canyon.",
	"You are in a north/south canyon about 25 feet across. The floor is covered by\n"
	"white mist seeping in from the north. The walls extend upward for well over 100\n"
	"feet. Suspended from some unseen point far above you, an enormous two-sided\n"
	"mirror is hanging paralled to and midway between the canyon walls. (The mirror\n"
	"is obviously provided for the use of the dwarves, who as you know, are extremely\n"
	"vain.) A small window can be seen in either wall, some fifty feet up.",
	{	{ GO_SOUTH,	69,		0 },
		{ GO_NORTH,	113,		0 },
		{ GO_RESERVOIR,	113,		0 },
		{ }}
    },{ // 110
	"You're at window on pit.",
	"You're at a low window overlooking a huge pit, which extends up out of sight.\n"
	"A floor is indistinctly visible over 50 feet below. Traces of white mist cover\n"
	"the floor of the pit, becoming thicker to the left. Marks in the dust around\n"
	"the window would seem to indicate that someone has been here recently. Directly\n"
	"across the pit from you and 25 feet away there is a similar window looking into\n"
	"a lighted room. A shadowy figure can be seen there peering back at you.",
	{	{ GO_WEST,	71,		0 },
		{ GO_JUMP,	20,		0 },
		{ }}
    },{ // 111
	"You're at top of stalactite.",
	"A large stalactite extends from the roof and almost reaches the floor below.\n"
	"You could climb down it, and jump from it to the floor,\n"
	"but having done so you would be unable to reach it to climb back up.",
	{	{ GO_NORTH,	70,		0 },
		{ GO_DOWN,	50,		40 },
		{ GO_JUMP,	50,		40 },
		{ GO_CLIMB,	50,		40 },
		{ GO_DOWN,	53,		50 },
		{ GO_DOWN,	45,		0 },
		{ }}
    },{ // 112
	"You are in a little maze of twisting passages, all different.",
	"You are in a little maze of twisting passages, all different.",
	{	{ GO_SW,	131,		0 },
		{ GO_NORTH,	132,		0 },
		{ GO_EAST,	133,		0 },
		{ GO_NW,	134,		0 },
		{ GO_SE,	135,		0 },
		{ GO_NE,	136,		0 },
		{ GO_WEST,	137,		0 },
		{ GO_DOWN,	138,		0 },
		{ GO_UP,	139,		0 },
		{ GO_SOUTH,	CHEST_ROOM2,	0 },
		{ }}
    },{ // 113
	"You're at reservoir.",
	"You are at the edge of a large underground reservoir. An opaque cloud of white\n"
	"mist fills the room and rises rapidly upward. The lake is fed by a stream which\n"
	"tumbles out of a hole in the wall about 10 feet overhead and splashes noisily\n"
	"into the water somewhere within the mist. The only passage goes back south.",
	{	{ GO_SOUTH,	109,		0 },
		{ GO_OUTSIDE,	109,		0 },
		{ 109,		109,		0 },
		{ }}
    },{ // 114, CHEST_ROOM1
	"Dead end.",
	"Dead end.",
	{	{ GO_SE,	84,		0 },
		{ }}
    },{ // 115, REPOSITORY1
	"You're at ne end of repository.",
	"You are at the northeast end of an immense room, even larger than the giant\n"
	"room. It appears to be a repository for the \"adventure\" program. Massive\n"
	"torches far overhead bathe the room with smoky yellow light. Scattered about\n"
	"you can be seen a pile of bottles (all of them empty), a nursery of young\n"
	"beanstalks murmuring quietly, a bed of oysters, a bundle of black rods with\n"
	"rusty stars on their ends, and a collection of brass lanterns. Off to one\n"
	"side a great many Dwarves are sleeping on the floor, snoring loudly. A sign\n"
	"nearby reads:\n"
	"	\"Do NOT disturb the Dwarves!\"\n"
	"An immense mirror is hanging against one wall, and stretches to the other end\n"
	"of the room, where various other objects can be glimpsed dimly in the distance.",
	{	{ GO_SW,	REPOSITORY2,	0 },
		{ }}
    },{ // 116, REPOSITORY2
	"You're at sw end of repository.",
	"You are at the southwest end of the repository. To one side is a pit full of\n"
	"fierce green snakes. On the other side is a row of small wicker cages, each of\n"
	"which contains a little sulking bird. In one corner is a bundle of black rods\n"
	"with rusty marks on their ends. A large number of velvet pillows are scattered\n"
	"about on the floor. A vast mirror stretches off to the northeast. At your feet\n"
	"is a large steel grate, next to which is a sign which reads:\n"
	"	\"Treasure vault. Keys in main office.\"",
	{	{ GO_NE,	REPOSITORY1,	0 },
		{ GO_DOWN,	LMSG (93),	0 },
		{ }}
    },{ // 117, CHASM_SW
	"You're on sw side of chasm.",
	"You are on one side of a large deep chasm. A heavy white mist rising up\n"
	"from below obscures all view of the far side. A sw path leads away from\n"
	"the chasm into a winding corridor.",
	{	{ GO_SW,	118,		0 },
		{ GO_OVER,	LMSG (160),	LCO (2,TROLL) },
		{ GO_ACROSS,	LMSG (160),	LCO (2,TROLL) },
		{ GO_CROSS,	LMSG (160),	LCO (2,TROLL) },
		{ GO_NE,	LMSG (160),	LCO (2,TROLL) },
		{ GO_OVER,	LMSG (161),	LCO (3,CHASM) },
		{ GO_OVER,	SPCM (3),	0 },
		{ GO_JUMP,	21,		LCO (3,CHASM) },
		{ GO_JUMP,	LMSG (96),	0 },
		{ }}
    },{ // 118
	"You're in sloping corridor.",
	"You are in a long winding corridor sloping out of sight in both directions.",
	{	{ GO_DOWN,	72,		0 },
		{ GO_UP,	CHASM_SW,	0 },
		{ }}
    },{ // 119
	"You are in a secret canyon which exits to the north and east.",
	"You are in a secret canyon which exits to the north and east.",
	{	{ GO_NORTH,	69,		0 },
		{ GO_OUTSIDE,	69,		0 },
		{ GO_EAST,	LMSG (153),	0 },
		{ GO_FORWARD,	LMSG (153),	0 },
		{ }}
    },{ // 120, DRAGON_LAIR
	"You are in a secret canyon which exits to the north and east.",
	"You are in a secret canyon which exits to the north and east.",
	{	{ GO_NORTH,	69,		0 },
		{ GO_EAST,	74,		0 },
		{ }}
    },{ // 121
	"You are in a secret canyon which exits to the north and east.",
	"You are in a secret canyon which exits to the north and east.",
	{	{ GO_EAST,	74,		0 },
		{ GO_OUTSIDE,	74,		0 },
		{ GO_NORTH,	LMSG (153),	0 },
		{ GO_FORWARD,	LMSG (153),	0 },
		{ }}
    },{ // 122, CHASM_NE
	"You're on ne side of chasm.",
	"You are on the far side of the chasm.\n"
	"A ne path leads away from the chasm on this side.",
	{	{ GO_NE,	123,		0 },
		{ GO_OVER,	LMSG (160),	LCO (2,TROLL) },
		{ GO_ACROSS,	LMSG (160),	LCO (2,TROLL) },
		{ GO_CROSS,	LMSG (160),	LCO (2,TROLL) },
		{ GO_SW,	LMSG (160),	LCO (2,TROLL) },
		{ GO_OVER,	SPCM (3),	0 },
		{ GO_JUMP,	LMSG (96),	0 },
		{ GO_FORK,	124,		0 },
		{ GO_VIEW,	126,		0 },
		{ GO_BARREN,	129,		0 },
		{ }}
    },{ // 123
	"You're in corridor.",
	"You're in a long east/west corridor.\n"
	"A faint rumbling noise can be heard in the distance.",
	{	{ GO_WEST,	CHASM_NE,	0 },
		{ GO_EAST,	124,		0 },
		{ GO_FORK,	124,		0 },
		{ GO_VIEW,	126,		0 },
		{ GO_BARREN,	129,		0 },
		{ }}
    },{ // 124
	"You're at fork in path.",
	"The path forks here. The left fork leads northeast. A dull rumbling\n"
	"seems to get louder in that direction. The right fork leads southeast\n"
	"down a gentle slope. The main corridor enters from the west.",
	{	{ GO_WEST,	123,		0 },
		{ GO_NE,	125,		0 },
		{ GO_LEFT,	125,		0 },
		{ GO_SE,	128,		0 },
		{ GO_RIGHT,	128,		0 },
		{ GO_DOWN,	128,		0 },
		{ GO_VIEW,	126,		0 },
		{ GO_BARREN,	129,		0 },
		{ }}
    },{ // 125
	"You're at junction with warm walls.",
	"The walls are quite warm here. From the north can be heard\n"
	"a steady roar, so loud that the entire cave seems to be trembling.\n"
	"Another passage leads south, and a low crawl goes east.",
	{	{ GO_SOUTH,	124,		0 },
		{ GO_FORK,	124,		0 },
		{ GO_NORTH,	126,		0 },
		{ GO_VIEW,	126,		0 },
		{ GO_EAST,	127,		0 },
		{ GO_CRAWL,	127,		0 },
		{ }}
    },{ // 126
	"You're at breath-taking view.",
	"You are on the edge of a breath-taking view. Far below you is an\n"
	"active volcano, from which great gouts of molten lava come surging out,\n"
	"cascading back down into the depths. The glowing rock fills the farthest\n"
	"reaches of the cavern with a blood-red glare, giving everything an eerie,\n"
	"macabre appearance.\n"
	"\n"
	"The air is filled with flickering sparks of ash and a heavy smell of\n"
	"brimstone. The walls are hot to the touch, and the thundering of the\n"
	"volcano drowns out all other sounds. Embedded in the jagged roof far\n"
	"overhead are myriad formations composed of pure white alabaster, which\n"
	"scatter their murky light into sinister apparitions upon the walls.\n"
	"To one side is a deep gorge, filled with a bizarre chaos of tortured rock\n"
	"which seems to have been crafted by the Devil Himself. An immense river\n"
	"of fire crashes out from the depths of the volcano, burns its way through\n"
	"the gorge, and plummets into a bottomless pit far off to your left.\n"
	"\n"
	"To the right, an immense geyser of blistering steam erupts continuously\n"
	"from a barren island in the center of a sulfurous lake, which bubbles\n"
	"ominously. The far right wall is aflame with an incandescence of its own,\n"
	"which lends an additional infernal splendor to the already hellish scene.\n"
	"\n"
	"A dark, foreboding passage exits to the south.",
	{	{ GO_SOUTH,	125,		0 },
		{ GO_PASSAGE,	125,		0 },
		{ GO_OUTSIDE,	125,		0 },
		{ GO_FORK,	124,		0 },
		{ GO_DOWN,	LMSG (110),	0 },
		{ GO_JUMP,	LMSG (110),	0 },
		{ }}
    },{ // 127
	"You're in chamber of boulders.",
	"You are in a small chamber filled with large boulders. The walls are very\n"
	"warm, causing the air in the room to be almost stifling from the heat. The\n"
	"only exit is a crawl heading west, through which is coming a low rumbling.",
	{	{ GO_WEST,	125,		0 },
		{ GO_OUTSIDE,	125,		0 },
		{ GO_CRAWL,	125,		0 },
		{ GO_FORK,	124,		0 },
		{ GO_VIEW,	126,		0 },
		{ }}
    },{ // 128
	"You're in limestone passage.",
	"You are walking along a gently sloping north/south passage\n"
	"lined with oddly shaped limestone formations.",
	{	{ GO_NORTH,	124,		0 },
		{ GO_UP,	124,		0 },
		{ GO_FORK,	124,		0 },
		{ GO_SOUTH,	129,		0 },
		{ GO_DOWN,	129,		0 },
		{ GO_BARREN,	129,		0 },
		{ GO_VIEW,	126,		0 },
		{ }}
    },{ // 129
	"You're in front of barren room.",
	"You are standing at the entrance to a large, barren room.\n"
	"A sign posted above the entrance reads:\n"
	"	\"Caution! Bear in room!\"",
	{	{ GO_WEST,	128,		0 },
		{ GO_UP,	128,		0 },
		{ GO_FORK,	124,		0 },
		{ GO_EAST,	130,		0 },
		{ GO_INSIDE,	130,		0 },
		{ GO_BARREN,	130,		0 },
		{ GO_ENTER,	130,		0 },
		{ GO_VIEW,	126,		0 },
		{ }}
    },{ // 130
	"You're in barren room.",
	"You are inside a barren room. The center of the room is completely empty\n"
	"except for some dust. Marks in the dust lead away toward the far end of\n"
	"the room. The only exit is the way you came in.",
	{	{ GO_WEST,	129,		0 },
		{ GO_FORK,	124,		0 },
		{ GO_VIEW,	126,		0 },
		{ }}
    },{ // 131
	"You are in a maze of twisting little passages, all different.",
	"You are in a maze of twisting little passages, all different.",
	{	{ GO_WEST,	107,		0 },
		{ GO_SE,	132,		0 },
		{ GO_NW,	133,		0 },
		{ GO_SW,	134,		0 },
		{ GO_NE,	135,		0 },
		{ GO_UP,	136,		0 },
		{ GO_DOWN,	137,		0 },
		{ GO_NORTH,	138,		0 },
		{ GO_SOUTH,	139,		0 },
		{ GO_EAST,	112,		0 },
		{ }}
    },{ // 132
	"You are in a little maze of twisty passages, all different.",
	"You are in a little maze of twisty passages, all different.",
	{	{ GO_NW,	107,		0 },
		{ GO_UP,	131,		0 },
		{ GO_NORTH,	133,		0 },
		{ GO_SOUTH,	134,		0 },
		{ GO_WEST,	135,		0 },
		{ GO_SW,	136,		0 },
		{ GO_NE,	137,		0 },
		{ GO_EAST,	138,		0 },
		{ GO_DOWN,	139,		0 },
		{ GO_SE,	112,		0 },
		{ }}
    },{ // 133
	"You are in a twisting maze of little passages, all different.",
	"You are in a twisting maze of little passages, all different.",
	{	{ GO_UP,	107,		0 },
		{ GO_DOWN,	131,		0 },
		{ GO_WEST,	132,		0 },
		{ GO_NE,	134,		0 },
		{ GO_SW,	135,		0 },
		{ GO_EAST,	136,		0 },
		{ GO_NORTH,	137,		0 },
		{ GO_NW,	138,		0 },
		{ GO_SE,	139,		0 },
		{ GO_SOUTH,	112,		0 },
		{ }}
    },{ // 134
	"You are in a twisting little maze of passages, all different.",
	"You are in a twisting little maze of passages, all different.",
	{	{ GO_NE,	107,		0 },
		{ GO_NORTH,	131,		0 },
		{ GO_NW,	132,		0 },
		{ GO_SE,	133,		0 },
		{ GO_EAST,	135,		0 },
		{ GO_DOWN,	136,		0 },
		{ GO_SOUTH,	137,		0 },
		{ GO_UP,	138,		0 },
		{ GO_WEST,	139,		0 },
		{ GO_SW,	112,		0 },
		{ }}
    },{ // 135
	"You are in a twisty little maze of passages, all different.",
	"You are in a twisty little maze of passages, all different.",
	{	{ GO_NORTH,	107,		0 },
		{ GO_SE,	131,		0 },
		{ GO_DOWN,	132,		0 },
		{ GO_SOUTH,	133,		0 },
		{ GO_EAST,	134,		0 },
		{ GO_WEST,	136,		0 },
		{ GO_SW,	137,		0 },
		{ GO_NE,	138,		0 },
		{ GO_NW,	139,		0 },
		{ GO_UP,	112,		0 },
		{ }}
    },{ // 136
	"You are in a twisty maze of little passages, all different.",
	"You are in a twisty maze of little passages, all different.",
	{	{ GO_EAST,	107,		0 },
		{ GO_WEST,	131,		0 },
		{ GO_UP,	132,		0 },
		{ GO_SW,	133,		0 },
		{ GO_DOWN,	134,		0 },
		{ GO_SOUTH,	135,		0 },
		{ GO_NW,	137,		0 },
		{ GO_SE,	138,		0 },
		{ GO_NE,	139,		0 },
		{ GO_NORTH,	112,		0 },
		{ }}
    },{ // 137
	"You are in a little twisty maze of passages, all different.",
	"You are in a little twisty maze of passages, all different.",
	{	{ GO_SE,	107,		0 },
		{ GO_NE,	131,		0 },
		{ GO_SOUTH,	132,		0 },
		{ GO_DOWN,	133,		0 },
		{ GO_UP,	134,		0 },
		{ GO_NW,	135,		0 },
		{ GO_NORTH,	136,		0 },
		{ GO_SW,	138,		0 },
		{ GO_EAST,	139,		0 },
		{ GO_WEST,	112,		0 },
		{ }}
    },{ // 138
	"You are in a maze of little twisting passages, all different.",
	"You are in a maze of little twisting passages, all different.",
	{	{ GO_DOWN,	107,		0 },
		{ GO_EAST,	131,		0 },
		{ GO_NE,	132,		0 },
		{ GO_UP,	133,		0 },
		{ GO_WEST,	134,		0 },
		{ GO_NORTH,	135,		0 },
		{ GO_SOUTH,	136,		0 },
		{ GO_SE,	137,		0 },
		{ GO_SW,	139,		0 },
		{ GO_NW,	112,		0 },
		{ }}
    },{ // 139
	"You are in a maze of little twisty passages, all different.",
	"You are in a maze of little twisty passages, all different.",
	{	{ GO_SW,	107,		0 },
		{ GO_NW,	131,		0 },
		{ GO_EAST,	132,		0 },
		{ GO_WEST,	133,		0 },
		{ GO_NORTH,	134,		0 },
		{ GO_DOWN,	135,		0 },
		{ GO_SE,	136,		0 },
		{ GO_UP,	137,		0 },
		{ GO_SOUTH,	138,		0 },
		{ GO_NE,	112,		0 },
		{ }}
    },{ // 140, CHEST_ROOM2
	"Dead end.",
	"Dead end.",
	{	{ GO_NORTH,	112,		0 },
		{ GO_OUTSIDE,	112,		0 },
		{ }}
    }
};

//}}}-------------------------------------------------------------------
//{{{ cond - location status

const uint8_t cond [MAXLOC+1] = {
    0,LIGHT|LIQUID,LIGHT,LIGHT|LIQUID,LIGHT|LIQUID,LIGHT,LIGHT,LIGHT|LIQUID,HINTC|LIGHT,LIGHT,
    LIGHT,0,0,HINTB,0,0,WATOIL,0,0,HINTS,
    WATOIL,WATOIL,WATOIL,0,WATOIL|LIQUID,0,WATOIL,0,0,0,
    0,WATOIL,WATOIL,0,0,0,0,0,LIQUID,0,
    WATOIL,0,HINTM,HINTM,HINTM,HINTM,HINTM|NOPIRAT,HINTM|NOPIRAT,HINTM|NOPIRAT,HINTM,
    HINTM,HINTM,HINTM,HINTM|NOPIRAT,HINTM,HINTM|NOPIRAT,0,NOPIRAT,0,WATOIL,
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,WATOIL,
    HINTM,HINTM,HINTM|NOPIRAT,0,0,NOPIRAT,HINTM|NOPIRAT,HINTM,0,WATOIL,
    WATOIL,0,0,0,0,LIQUID,0,0,0,0,
    LIGHT,0,0,0,0,0,0,0,0,0,
    0,0,0,LIQUID,0,LIGHT,LIGHT,0,0,0,
    0,0,NOPIRAT,NOPIRAT,NOPIRAT,NOPIRAT,NOPIRAT,NOPIRAT,NOPIRAT,NOPIRAT,
    NOPIRAT,0,0,0,0,0,0,0,0,0,
};

//}}}-------------------------------------------------------------------

// Print a long location description
void desclg (loc_t l)
{
    if (--l < ArraySize(c_locs))
	puts (c_locs[l].ldesc);
}

// Print a short location description
void descsh (loc_t l)
{
    if (--l < ArraySize(c_locs))
	puts (c_locs[l].sdesc);
}

// Routine to fill travel array for a given location
void gettrav (loc_t l)
{
    if (--l < ArraySize(c_locs))
	memcpy (travel, c_locs[l].travs, sizeof(travel));
}
