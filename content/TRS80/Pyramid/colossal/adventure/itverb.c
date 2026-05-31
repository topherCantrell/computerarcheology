// This file is free software, distributed under the BSD license.

#include "advent.h"

//----------------------------------------------------------------------

static void ivtake (void);
static void ivopen (void);
static void ivkill (void);
static void iveat (void);
static void ivdrink (void);
static void ivquit (void);
static void ivfill (void);
static void ivfoo (void);
static void inventory (void);
static void addobj (int obj);

//----------------------------------------------------------------------

// Routines to process intransitive verbs
void itverb (void)
{
    switch (verb) {
	case DROP:
	case SAY:
	case WAVE:
	case CALM:
	case RUB:
	case THROW:
	case FIND:
	case FEED:
	case BREAK:
	case WAKE:	needobj();	break;
	case TAKE:	ivtake();	break;
	case OPEN:
	case LOCK:	ivopen();	break;
	case NOTHING:	rspeak(54);	break;
	case ON:
	case OFF:
	case POUR:	trverb();	break;
	case WALK:	actspk(verb);	break;
	case KILL:	ivkill();	break;
	case EAT:	iveat();	break;
	case DRINK:	ivdrink();	break;
	case QUIT:	ivquit();	break;
	case FILL:	ivfill();	break;
	case BLAST:	vblast();	break;
	case SCORE:	score();	break;
	case FOO:	ivfoo();	break;
	case SUSPEND:	saveflg = 1;	break;
	case INVENTORY:	inventory();	break;
	case LOAD:	restore();	break;
	default:
	    printf ("This intransitive not implemented yet\n");
    }
}

// CARRY, TAKE etc.
static void ivtake (void)
{
    unsigned anobj = 0;
    for (unsigned item = 1; item < MAXOBJ; ++item) {
	if (place[item] == loc) {
	    if (anobj != 0) {
		needobj();
		return;
	    }
	    anobj = item;
	}
    }
    if (anobj == 0 || (dcheck() && dflag >= 2)) {
	needobj();
	return;
    }
    object = anobj;
    vtake();
}

// OPEN, LOCK, UNLOCK
static void ivopen (void)
{
    if (here(CLAM))
	object = CLAM;
    if (here(OYSTER))
	object = OYSTER;
    if (at(DOOR))
	object = DOOR;
    if (at(GRATE))
	object = GRATE;
    if (here(CHAIN)) {
	if (object != 0) {
	    needobj();
	    return;
	}
	object = CHAIN;
    }
    if (object == 0) {
	rspeak(28);
	return;
    }
    vopen();
}

// ATTACK, KILL etc
static void ivkill (void)
{
    object1 = 0;
    if (dcheck() && dflag >= 2)
	object = DWARF;
    if (here(SNAKE))
	addobj(SNAKE);
    if (at(DRAGON) && prop[DRAGON] == 0)
	addobj(DRAGON);
    if (at(TROLL))
	addobj(TROLL);
    if (here(BEAR) && prop[BEAR] == 0)
	addobj(BEAR);
    if (object1 != 0) {
	needobj();
	return;
    }
    if (object != 0) {
	vkill();
	return;
    }
    if (here(BIRD) && verb != THROW)
	object = BIRD;
    if (here(CLAM) || here(OYSTER))
	addobj(CLAM);
    if (object1 != 0) {
	needobj();
	return;
    }
    vkill();
}

// EAT
static void iveat (void)
{
    if (!here(FOOD))
	needobj();
    else {
	object = FOOD;
	veat();
    }
}

// DRINK
static void ivdrink (void)
{
    if (liqloc(loc) != WATER && (liq() != WATER || !here(BOTTLE)))
	needobj();
    else {
	object = WATER;
	vdrink();
    }
}

// QUIT
static void ivquit (void)
{
    if ((gaveup = yes (22, 54, 54)))
	normend();
}

// FILL
static void ivfill (void)
{
    if (!here(BOTTLE))
	needobj();
    else {
	object = BOTTLE;
	vfill();
    }
}

// Handle fee fie foe foo...
static void ivfoo (void)
{
    char k = parse_magic_word (word1);
    unsigned msg = 42;
    if (foobar != 1 - k) {
	if (foobar != 0)
	    msg = 151;
	rspeak(msg);
	return;
    }
    foobar = k;
    if (k != 4)
	return;
    foobar = 0;
    if (place[EGGS] == GIANT_ROOM || (toting(EGGS) && loc == GIANT_ROOM)) {
	rspeak(msg);
	return;
    }
    if (place[EGGS] == 0 && place[TROLL] == 0 && prop[TROLL] == 0)
	prop[TROLL] = 1;
    if (here(EGGS))
	k = 1;
    else if (loc == GIANT_ROOM)
	k = 0;
    else
	k = 2;
    move_object (EGGS, GIANT_ROOM);
    pspeak (EGGS, k);
}

// INVENTORY 
static void inventory (void)
{
    unsigned msg = 98;
    for (unsigned i = 1; i <= MAXOBJ; ++i) {
	if (i == BEAR || !toting(i))
	    continue;
	if (msg)
	    rspeak(99);
	msg = 0;
	pspeak (i, -1);
    }
    if (toting(BEAR))
	msg = 141;
    if (msg)
	rspeak(msg);
}

// ensure uniqueness as objects are searched
// out for an intransitive verb
static void addobj (int obj)
{
    if (object1 != 0)
	return;
    if (object != 0) {
	object1 = -1;
	return;
    }
    object = obj;
}
