// This file is free software, distributed under the BSD license.

#include "advent.h"

//----------------------------------------------------------------------

static void vdrop (void);
static void vsay (void);
static void von (void);
static void voff (void);
static void vwave (void);
static void vpour (void);
static void vthrow (void);
static void vfind (void);
static void vfeed (void);
static void vread (void);
static void vbreak (void);
static void vwake (void);

//----------------------------------------------------------------------

// Routine to process a transitive verb
void trverb (void)
{
    switch (verb) {
	case CALM:
	case WALK:
	case QUIT:
	case SCORE:
	case FOO:
	case BRIEF:
	case SUSPEND:
	case HOURS:
	case LOG:	actspk (verb);	break;
	case TAKE:	vtake();	break;
	case DROP:	vdrop ();	break;
	case OPEN:
	case LOCK:	vopen();	break;
	case SAY:	vsay();		break;
	default:
	case NOTHING:	rspeak (54);	break;
	case ON:	von();		break;
	case OFF:	voff();		break;
	case WAVE:	vwave();	break;
	case KILL:	vkill();	break;
	case POUR:	vpour();	break;
	case EAT:	veat();		break;
	case DRINK:	vdrink();	break;
	case RUB:
	    if (object != LAMP)
		rspeak (76);
	    else
		actspk (RUB);
	    break;
	case THROW:	vthrow();	break;
	case FEED:	vfeed();	break;
	case FIND:
	case INVENTORY:	vfind();	break;
	case FILL:	vfill();	break;
	case READ:	vread();	break;
	case BLAST:	vblast();	break;
	case BREAK:	vbreak();	break;
	case WAKE:	vwake();	break;
    }
}

// CARRY TAKE etc.
void vtake (void)
{
    if (toting(object)) {
	actspk (verb);
	return;
    }

    // special case objects and fixed objects
    uint8_t msg = 25;
    if (object == PLANT && prop[PLANT] <= 0)
	msg = 115;
    if (object == BEAR && prop[BEAR] == 1)
	msg = 169;
    if (object == CHAIN && prop[BEAR] != 0)
	msg = 170;
    if (fixed[object]) {
	rspeak (msg);
	return;
    }

    // special case for liquids
    if (object == WATER || object == OIL) {
	if (!here(BOTTLE) || liq() != object) {
	    object = BOTTLE;
	    if (toting(BOTTLE) && prop[BOTTLE] == 1) {
		vfill();
		return;
	    }
	    if (prop[BOTTLE] != 1)
		msg = 105;
	    if (!toting(BOTTLE))
		msg = 104;
	    rspeak (msg);
	    return;
	}
	object = BOTTLE;
    }
    if (holding >= 7) {
	rspeak (92);
	return;
    }

    // special case for bird.
    if (object == BIRD && prop[BIRD] == 0) {
	if (toting(ROD)) {
	    rspeak (26);
	    return;
	}
	if (!toting(CAGE)) {
	    rspeak (27);
	    return;
	}
	prop[BIRD] = 1;
    }
    if ((object == BIRD || object == CAGE) && prop[BIRD] != 0)
	carry((BIRD + CAGE) - object);
    carry(object);

    // handle liquid in bottle
    int i = liq();
    if (object == BOTTLE && i != 0)
	place[i] = CARRIED;
    rspeak (54);
}

// DROP etc.
static void vdrop (void)
{
    // check for dynamite
    if (toting(ROD2) && object == ROD && !toting(ROD))
	object = ROD2;
    if (!toting(object)) {
	actspk (verb);
	return;
    }

    if (object == BIRD && here(SNAKE)) {
	// snake and bird
	rspeak (30);
	if (closed)
	    dwarfend();
	destroy_object (SNAKE);
	prop[SNAKE] = -1;
    } else if (object == COINS && here(VEND)) {
	// coins and vending machine
	destroy_object (COINS);
	drop (BATTERIES, loc);
	pspeak(BATTERIES, 0);
	return;
    } else if (object == BIRD && at(DRAGON) && prop[DRAGON] == 0) {
	// bird and dragon (ouch!!)
	rspeak (154);
	destroy_object (BIRD);
	prop[BIRD] = 0;
	if (place[SNAKE] != 0)
	    ++tally2;
	return;
    }

    if (object == BEAR && at(TROLL)) {
	// Bear and troll
	rspeak (163);
	move_object (TROLL, 0);
	move_object ((TROLL + MAXOBJ), 0);
	move_object (TROLL2, CHASM_SW);
	move_object ((TROLL2 + MAXOBJ), CHASM_NE);
	prop[TROLL] = 2;
    } else if (object == VASE) {
	// Vase
	if (loc == 96)
	    rspeak (54);
	else {
	    prop[VASE] = at(PILLOW) ? 0 : 2;
	    pspeak(VASE, prop[VASE] + 1);
	    if (prop[VASE] != 0)
		fixed[VASE] = -1;
	}
    }

    // handle liquid and bottle
    int i = liq();
    if (i == object)
	object = BOTTLE;
    if (object == BOTTLE && i != 0)
	place[i] = 0;

    // handle bird and cage
    if (object == CAGE && prop[BIRD] != 0)
	drop (BIRD, loc);
    if (object == BIRD)
	prop[BIRD] = 0;
    drop (object, loc);
}

// LOCK, UNLOCK, OPEN, CLOSE etc.
void vopen (void)
{
    unsigned msg = 33;
    switch (object) {
	case CLAM:
	case OYSTER: {
	    bool oyclam = (object == OYSTER);
	    if (verb == LOCK)
		msg = 61;
	    else if (!toting(TRIDENT))
		msg = 122 + oyclam;
	    else if (toting(object))
		msg = 120 + oyclam;
	    else {
		msg = 124 + oyclam;
		destroy_object (CLAM);
		drop (OYSTER, loc);
		drop (PEARL, 105);
	    }
	}   break;
	case DOOR:
	    msg = (prop[DOOR] == 1 ? 54 : 111);
	    break;
	case CAGE:
	    msg = 32;
	    break;
	case KEYS:
	    msg = 55;
	    break;
	case CHAIN:
	    if (!here(KEYS))
		msg = 31;
	    else if (verb == LOCK) {
		if (prop[CHAIN] != 0)
		    msg = 34;
		else if (loc != 130)
		    msg = 173;
		else {
		    prop[CHAIN] = 2;
		    if (toting(CHAIN))
			drop (CHAIN, loc);
		    fixed[CHAIN] = -1;
		    msg = 172;
		}
	    } else {
		if (prop[BEAR] == 0)
		    msg = 41;
		else if (prop[CHAIN] == 0)
		    msg = 37;
		else {
		    prop[CHAIN] = 0;
		    fixed[CHAIN] = 0;
		    if (prop[BEAR] != 3)
			prop[BEAR] = 2;
		    fixed[BEAR] = 2 - prop[BEAR];
		    msg = 171;
		}
	    }
	    break;
	case GRATE:
	    if (!here(KEYS))
		msg = 31;
	    else if (closing) {
		if (!panic) {
		    clock2 = 15;
		    panic = true;
		}
		msg = 130;
	    } else {
		msg = 34 + prop[GRATE];
		prop[GRATE] = (verb == LOCK ? 0 : 1);
		msg += 2 * prop[GRATE];
	    }
	    break;
    }
    rspeak (msg);
}

// SAY etc.
static void vsay (void)
{
    int wtype, wval;
    analyze (word1, &wtype, &wval);
    printf ("Okay.\n%s\n", wval == SAY ? word2 : word1);
}

// ON etc.
static void von (void)
{
    if (!here(LAMP))
	actspk (verb);
    else if (limit < 0)
	rspeak (184);
    else {
	prop[LAMP] = 1;
	rspeak (39);
	if (wzdark) {
	    wzdark = 0;
	    describe();
	}
    }
}

// OFF etc.
static void voff (void)
{
    if (!here(LAMP))
	actspk (verb);
    else {
	prop[LAMP] = 0;
	rspeak (40);
    }
}

// WAVE etc.
static void vwave (void)
{
    if (!toting(object) && (object != ROD || !toting(ROD2)))
	rspeak (29);
    else if (object != ROD || !at(FISSURE) || !toting(object) || closing)
	actspk (verb);
    else {
	prop[FISSURE] = 1 - prop[FISSURE];
	pspeak(FISSURE, 2 - prop[FISSURE]);
    }
}

// ATTACK, KILL etc.
void vkill (void)
{
    unsigned msg = 44;
    switch (object) {
	case BIRD:
	    if (closed)
		msg = 137;
	    else {
		destroy_object (BIRD);
		prop[BIRD] = 0;
		if (place[SNAKE] == KING_HALL)
		    ++tally2;
		msg = 45;
	    }
	    break;
	case 0:
	    msg = 44;
	    break;
	case CLAM:
	case OYSTER:
	    msg = 150;
	    break;
	case SNAKE:
	    msg = 46;
	    break;
	case DWARF:
	    if (closed)
		dwarfend();
	    msg = 49;
	    break;
	case TROLL:
	    msg = 157;
	    break;
	case BEAR:
	    msg = 165 + (prop[BEAR] + 1) / 2;
	    break;
	case DRAGON:
	    if (prop[DRAGON] != 0) {
		msg = 167;
		break;
	    }
	    if (!yes(49, 0, 0))
		break;
	    pspeak(DRAGON, 1);
	    prop[DRAGON] = 2;
	    prop[RUG] = 0;
	    move_object ((DRAGON + MAXOBJ), -1);
	    move_object ((RUG + MAXOBJ), 0);
	    move_object (DRAGON, DRAGON_LAIR);
	    move_object (RUG, DRAGON_LAIR);
	    for (unsigned i = 1; i < MAXOBJ; ++i)
		if (place[i] == DRAGON_LAIR-1 || place[i] == DRAGON_LAIR+1)
		    move_object (i, DRAGON_LAIR);
	    newloc = DRAGON_LAIR;
	    return;
	default:
	    actspk (verb);
	    return;
    }
    rspeak (msg);
}

// POUR
static void vpour (void)
{
    if (object == BOTTLE || object == 0)
	object = liq();
    if (object == 0) {
	needobj();
	return;
    }
    if (!toting(object)) {
	actspk (verb);
	return;
    }
    if (object != OIL && object != WATER) {
	rspeak (78);
	return;
    }
    prop[BOTTLE] = 1;
    place[object] = 0;
    if (at(PLANT)) {
	if (object != WATER)
	    rspeak (112);
	else {
	    pspeak(PLANT, prop[PLANT] + 1);
	    prop[PLANT] = (prop[PLANT] + 2) % 6;
	    prop[PLANT2] = prop[PLANT] / 2;
	    describe();
	}
    } else if (at(DOOR)) {
	prop[DOOR] = (object == OIL ? 1 : 0);
	rspeak (113 + prop[DOOR]);
    } else
	rspeak (77);
}

// EAT
void veat (void)
{
    unsigned msg;
    switch (object) {
	case FOOD:
	    destroy_object (FOOD);
	    msg = 72;
	    break;
	case BIRD:
	case SNAKE:
	case CLAM:
	case OYSTER:
	case DWARF:
	case DRAGON:
	case TROLL:
	case BEAR:
	    msg = 71;
	    break;
	default:
	    actspk (verb);
	    return;
    }
    rspeak (msg);
}

// DRINK
void vdrink (void)
{
    if (object != WATER)
	rspeak (110);
    else if (liq() != WATER || !here(BOTTLE))
	actspk (verb);
    else {
	prop[BOTTLE] = 1;
	place[WATER] = 0;
	rspeak (74);
    }
}

// THROW etc.
static void vthrow (void)
{
    if (toting(ROD2) && object == ROD && !toting(ROD))
	object = ROD2;
    if (!toting(object)) {
	actspk (verb);
	return;
    }

    // treasure to troll
    if (at(TROLL) && object >= NUGGET && object < MAXOBJ) {
	rspeak (159);
	drop (object, 0);
	move_object (TROLL, 0);
	move_object ((TROLL + MAXOBJ), 0);
	drop (TROLL2, CHASM_SW);
	drop ((TROLL2 + MAXOBJ), CHASM_NE);
	return;
    }

    // feed the bears...
    if (object == FOOD && here(BEAR)) {
	object = BEAR;
	vfeed();
	return;
    }

    // if not axe, same as drop...
    if (object != AXE) {
	vdrop ();
	return;
    }

    // AXE is THROWN
    unsigned msg = 48;
    unsigned i = dcheck();
    if (i) { // at a dwarf...
	if (pct(33)) {
	    dseen[i] = false;
	    dloc[i] = 0;
	    msg = 47;
	    if (++dkill == 1)
		msg = 149;
	}
    } else if (at(DRAGON) && prop[DRAGON] == 0) // at a dragon...
	msg = 152;
    else if (at(TROLL))	// at the troll...
	msg = 158;
    else if (here(BEAR) && prop[BEAR] == 0) { // at the bear...
	rspeak (164);
	drop (AXE, loc);
	fixed[AXE] = -1;
	prop[AXE] = 1;
	return;
    } else { // otherwise it is an attack
	verb = KILL;
	object = 0;
	itverb();
	return;
    }
    rspeak (msg);
    // handle the left over axe...
    drop (AXE, loc);
    describe();
}

// INVENTORY, FIND etc.
static void vfind (void)
{
    unsigned msg;
    if (toting(object))
	msg = 24;
    else if (closed)
	msg = 138;
    else if (dcheck() && dflag >= 2 && object == DWARF)
	msg = 94;
    else if (at(object) || (liq() == object && here(BOTTLE)) || object == liqloc(loc))
	msg = 94;
    else {
	actspk (verb);
	return;
    }
    rspeak (msg);
}

// FILL
void vfill (void)
{
    unsigned msg = 29;
    switch (object) {
	case BOTTLE:
	    if (liq() != 0)
		msg = 105;
	    else if (liqloc(loc) == 0)
		msg = 106;
	    else {
		prop[BOTTLE] = cond[loc] & WATOIL;
		int i = liq();
		if (toting(BOTTLE))
		    place[i] = CARRIED;
		msg = (i == OIL ? 108 : 107);
	    }
	    break;
	case VASE:
	    if (liqloc(loc) == 0) {
		msg = 144;
		break;
	    }
	    if (!toting(VASE)) {
		msg = 29;
		break;
	    }
	    rspeak (145);
	    vdrop ();
	    return;
    }
    rspeak (msg);
}

// FEED
static void vfeed (void)
{
    unsigned msg = 14;
    switch (object) {
	case BIRD:
	    msg = 100;
	    break;
	case DWARF:
	    if (!here(FOOD)) {
		actspk (verb);
		return;
	    }
	    ++dflag;
	    msg = 103;
	    break;
	case BEAR:
	    if (!here(FOOD)) {
		if (prop[BEAR] == 0)
		    msg = 102;
		else if (prop[BEAR] == 3)
		    msg = 110;
		else {
		    actspk (verb);
		    return;
		}
		break;
	    }
	    destroy_object (FOOD);
	    prop[BEAR] = 1;
	    fixed[AXE] = 0;
	    prop[AXE] = 0;
	    msg = 168;
	    break;
	case DRAGON:
	    msg = (prop[DRAGON] != 0 ? 110 : 102);
	    break;
	case TROLL:
	    msg = 182;
	    break;
	case SNAKE:
	    if (closed || !here(BIRD)) {
		msg = 102;
		break;
	    }
	    msg = 101;
	    destroy_object (BIRD);
	    prop[BIRD] = 0;
	    ++tally2;
	    break;
    }
    rspeak (msg);
}

// READ etc.
static void vread (void)
{
    if (dark()) {
	printf ("It's too dark to see the %s.\n", probj(object));
	return;
    }
    unsigned msg;
    switch (object) {
	case MAGAZINE:	msg = 190;	break;
	case TABLET:	msg = 196;	break;
	case MESSAGE:	msg = 191;	break;
	case OYSTER:	if (toting(OYSTER) && closed)
			    yes (192, 193, 54);
			return;
	default:	actspk (verb);	return;
    }
    rspeak (msg);
}

// BLAST etc.
void vblast (void)
{
    if (prop[ROD2] < 0 || !closed)
	actspk (verb);
    else {
	bonus = 133;
	if (loc == REPOSITORY1)
	    bonus = 134;
	if (here(ROD2))
	    bonus = 135;
	rspeak (bonus);
	normend();
    }
}

// BREAK etc.
static void vbreak (void)
{
    unsigned msg;
    if (object == MIRROR) {
	msg = 148;
	if (closed) {
	    rspeak (197);
	    dwarfend();
	}
    } else if (object == VASE && prop[VASE] == 0) {
	msg = 198;
	if (toting(VASE))
	    drop (VASE, loc);
	prop[VASE] = 2;
	fixed[VASE] = -1;
    } else {
	actspk (verb);
	return;
    }
    rspeak (msg);
}

// WAKE etc.
static void vwake (void)
{
    if (object != DWARF || !closed)
	actspk (verb);
    else {
	rspeak (199);
	dwarfend();
    }
}

// Routine to indicate no reasonable object for verb found.
// Used mostly by intransitive verbs.
void needobj (void)
{
    int wtype, wval;
    analyze (word1, &wtype, &wval);
    printf ("%s what?\n", wtype == 2 ? word1 : word2);
}

// Routine to check for presence of dwarves..
unsigned dcheck (void)
{
    for (unsigned i = 1; i < MAXDWARVES-1; ++i)
	if (dloc[i] == loc)
	    return i;
    return 0;
}
