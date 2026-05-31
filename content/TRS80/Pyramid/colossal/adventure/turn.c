// This file is free software, distributed under the BSD license.

#include "advent.h"

//----------------------------------------------------------------------

static void descitem (void);
static void domove (void);
static void goback (void);
static void dotrav (void);
static void badmove (void);
static void spcmove (unsigned rdest);
static void death (void);
static void doobj (void);
static void trobj (void);
static void dwarves (void);
static void dopirate (void);
static bool stimer (void);

//----------------------------------------------------------------------

// Routine to take 1 turn
void turn (void)
{
    // if closing, then he can't leave except via the main office.
    if (newloc <= AT_GRATE && newloc != 0 && closing) {
	rspeak (130);
	newloc = loc;
	if (!panic)
	    clock2 = 15;
	panic = 1;
    }

    // see if a dwarf has seen him and has come from where he wants to go.
    if (newloc != loc && !forced(loc) && !(cond[loc] & NOPIRAT)) {
	for (unsigned i = 1; i < (MAXDWARVES - 1); ++i) {
	    if (odloc[i] == newloc && dseen[i]) {
		newloc = loc;
		rspeak (2);
		break;
	    }
	}
    }
    dwarves();	// & special dwarf (pirate who steals)

    // added by BDS C conversion
    if (loc != newloc) {
	++turns;
	loc = newloc;

	// check for death
	if (loc == 0) {
	    death();
	    return;
	}

	// check for forced move
	if (forced(loc)) {
	    describe();
	    domove();
	    return;
	}

	// check for wandering in dark
	if (wzdark && dark() && pct(35)) {
	    rspeak (23);
	    oldloc2 = loc;
	    death();
	    return;
	}

	// describe his situation
	describe();

	// causes occasional "move" with no describe & descitem
    }

    if (closed) {
	if (prop[OYSTER] < 0 && toting(OYSTER))
	    pspeak (OYSTER, 1);
	for (unsigned i = 1; i <= MAXOBJ; ++i)
	    if (toting(i) && prop[i] < 0)
		prop[i] = -1 - prop[i];
    }

    wzdark = dark();
    if (knfloc > 0 && knfloc != loc)
	knfloc = 0;

    if (stimer())	       // as the grains of sand slip by
	return;

    while (!english())	       // retrieve player instructions
	{}

    if (motion)		       // execute player instructions
	domove();
    else if (object)
	doobj();
    else
	itverb();
}

// Routine to describe current location
void describe (void)
{
    if (toting(BEAR))
	rspeak (141);
    if (dark())
	rspeak (16);
    else if (visited_location (loc))
	descsh(loc);
    else {
	set_location_visited (loc);
	desclg(loc);
    }
    if (loc == Y2_ROOM && pct(25) && !closing)
	rspeak (8);
    if (!dark())
	descitem();
}

// Routine to describe visible items
static void descitem (void)
{
    for (unsigned i = 1; i < MAXOBJ; ++i) {
	if (!at(i))
	    continue;
	if (i == STEPS && toting(NUGGET))
	    continue;
	if (prop[i] < 0) {
	    if (closed)
		continue;
	    else {
		prop[i] = 0;
		if (i == RUG || i == CHAIN)
		    ++prop[i];
		--tally;
	    }
	}
	int state;
	if (i == STEPS && loc == fixed[STEPS])
	    state = 1;
	else
	    state = prop[i];
	pspeak (i, state);
    }
    if (tally == tally2 && tally != 0 && limit > 35)
	limit = 35;
}

// Routine to handle motion requests
static void domove (void)
{
    gettrav (loc);
    switch (motion) {
	case GO_NOWHERE:
	    break;
	case GO_BACK:
	    goback();
	    break;
	case GO_LOOK:
	    wzdark = 0;
	    set_location_not_visited (loc);
	    newloc = loc;
	    loc = 0;
	    break;
	case GO_CAVE:
	    if (loc < AT_GRATE)
		rspeak (57);
	    else
		rspeak (58);
	    break;
	default:
	    oldloc2 = oldloc;
	    oldloc = loc;
	    dotrav();
    }
}

// Routine to handle request to return
// from whence we came!
static void goback (void)
{
    loc_t want = forced (oldloc) ? oldloc2 : oldloc;
    oldloc2 = oldloc;
    oldloc = loc;

    if (want == loc) {
	rspeak (91);
	return;
    }

    struct trav strav [MAXTRAV];
    memcpy (strav, travel, sizeof(strav));

    int k2 = 0;
    for (unsigned kk = 0; travel[kk].tdest; ++kk) {
	if (!travel[kk].tcond && travel[kk].tdest == want) {
	    motion = travel[kk].tverb;
	    dotrav();
	    return;
	}
	if (!travel[kk].tcond) {
	    k2 = kk;
	    loc_t tdl = travel[kk].tdest;
	    gettrav (tdl);
	    if (forced(tdl) && travel[0].tdest == want)
		k2 = tdl;
	    memcpy (travel, strav, sizeof(travel));
	}
    }
    if (k2) {
	motion = travel[k2].tverb;
	dotrav();
    } else
	rspeak (140);
}

// Routine to figure out a new location
// given current location and a motion.
static void dotrav (void)
{
    newloc = loc;
    unsigned rdest = 0;
    int pctt = rand() % 100;
    bool mvflag = false, hitflag = false;
    for (unsigned kk = 0; travel[kk].tdest && !mvflag; ++kk) {
	rdest = travel[kk].tdest;
	int rverb = travel[kk].tverb;
	int rcond = travel[kk].tcond;
	obj_t robject = rcond % 100;

	if (rverb != 1 && rverb != motion && !hitflag)
	    continue;
	hitflag = true;
	switch (rcond / 100) {
	    case 0:
		if (rcond == 0 || pctt < rcond)
		    mvflag = true;
		break;
	    case 1:
		if (robject == 0)
		    mvflag = true;
		else if (toting(robject))
		    mvflag = true;
		break;
	    case 2:
		if (toting(robject) || at(robject))
		    mvflag = true;
		break;
	    default:
		if (prop[robject] != rcond/100-3)
		    mvflag = true;
		break;
	}
    }
    if (!mvflag)
	badmove();
    else if (rdest > 500)
	rspeak (rdest - 500);
    else if (rdest > 300)
	spcmove (rdest);
    else
	newloc = rdest;
}

// The player tried a poor move option.
static void badmove (void)
{
    unsigned msg = 12;
    if (motion >= 43 && motion <= 50)
	msg = 9;
    if (motion == 29 || motion == 30)
	msg = 9;
    if (motion == 7 || motion == 36 || motion == 37)
	msg = 10;
    if (motion == 11 || motion == 19)
	msg = 11;
    if (verb == FIND || verb == INVENTORY)
	msg = 59;
    if (motion == 62 || motion == 65)
	msg = 42;
    if (motion == 17)
	msg = 80;
    rspeak (msg);
}

// Routine to handle very special movement.
static void spcmove (unsigned rdest)
{
    unsigned smdest = rdest - 300;
    if (smdest == 1) { // plover movement via alcove
	if (!holding || (holding == 1 && toting(EMERALD)))
	    newloc = (PLOVER_ROOM + 99) - loc;
	else
	    rspeak (117);
    } else if (smdest == 3) { // troll bridge
	if (prop[TROLL] == 1) {
	    pspeak (TROLL, 1);
	    prop[TROLL] = 0;
	    move_object (TROLL2, 0);
	    move_object ((TROLL2 + MAXOBJ), 0);
	    move_object (TROLL, CHASM_SW);
	    move_object ((TROLL + MAXOBJ), CHASM_NE);
	    newloc = loc;
	} else {
	    newloc = (loc == CHASM_SW ? CHASM_NE : CHASM_SW);
	    if (prop[TROLL] == 0)
		++prop[TROLL];
	    if (!toting (BEAR))
		return;
	    rspeak (162);
	    prop[CHASM] = 1;
	    prop[TROLL] = 2;
	    drop (BEAR, newloc);
	    fixed[BEAR] = -1;
	    prop[BEAR] = 3;
	    if (prop[SPICES] < 0)
		++tally2;
	    oldloc2 = newloc;
	    death();
	}
    } else // trying to remove plover, bad route
	drop (EMERALD, loc);
}

// Routine to handle player's demise via waking up the dwarves...
void dwarfend (void)
{
    death();
    normend();
}

// Routine to handle the passing on of one of the player's incarnations...
static void death (void)
{
    if (!closing) {
	bool yea = yes (81 + numdie * 2, 82 + numdie * 2, 54);
	if (++numdie >= MAXDIE || !yea)
	    normend();
	place[WATER] = 0;
	place[OIL] = 0;
	if (toting(LAMP))
	    prop[LAMP] = 0;
	for (unsigned j = 1; j < 101; ++j) {
	    unsigned i = 101 - j;
	    if (toting(i))
		drop (i, i == LAMP ? 1 : oldloc2);
	}
	newloc = 3;
	oldloc = loc;
	return;
    }

    // closing -- no resurrection...
    rspeak (131);
    ++numdie;
    normend();
}

// Routine to process an object.
static void doobj (void)
{
    // is object here?  if so, transitive
    if (fixed[object] == loc || here(object))
	trobj();

    // did he give grate as destination?
    else if (object == GRATE) {
	if (loc == END_OF_ROAD || loc == IN_VALLEY || loc == STREAM_SLIT) {
	    motion = GO_DEPRESSION;
	    domove();
	} else if (loc > UNDER_GRATE && loc < MIST_HALL) {
	    motion = GO_ENTRANCE;
	    domove();
	}
    }

    // is it a dwarf he is after?
    else if (dcheck() && dflag >= 2) {
	object = DWARF;
	trobj();
    }

    // is he trying to get/use a liquid?
    else if ((liq() == object && here(BOTTLE)) || liqloc(loc) == object)
	trobj();
    else if (object == PLANT && at(PLANT2) && prop[PLANT2] == 0) {
	object = PLANT2;
	trobj();
    }

    // is he trying to grab a knife?
    else if (object == KNIFE && knfloc == loc) {
	rspeak (116);
	knfloc = -1;
    }

    // is he trying to get at dynamite?
    else if (object == ROD && here(ROD2)) {
	object = ROD2;
	trobj();
    } else
	printf("I see no %s here.\n", probj(object));
}

// Routine to process an object being referred to.
static void trobj (void)
{
    if (verb)
	trverb();
    else
	printf("What do you want to do with the %s?\n", probj(object));
}

// Routine to print word corresponding to object
const char* probj (obj_t o UNUSED)
{
    int wtype, wval;
    analyze (word1, &wtype, &wval);
    return wtype == 1 ? word1 : word2;
}

// dwarf stuff.
static void dwarves (void)
{
    // see if dwarves allowed here
    if (newloc == 0 || forced(newloc) || (cond[newloc] & NOPIRAT))
	return;

    // see if dwarves are active.
    if (!dflag) {
	if (newloc > MIST_HALL)
	    ++dflag;
	return;
    }

    // if first close encounter (of 3rd kind)
    // kill 0, 1 or 2
    if (dflag == 1) {
	if (newloc < MIST_HALL || pct(95))
	    return;
	++dflag;
	for (unsigned i = 1; i < 3; ++i)
	    if (pct(50))
		dloc[rand() % 5 + 1] = 0;
	for (unsigned i = 1; i < MAXDWARVES-1; ++i) {
	    if (dloc[i] == newloc)
		dloc[i] = daltloc;
	    odloc[i] = dloc[i];
	}
	rspeak (3);
	drop (AXE, newloc);
	return;
    }
    unsigned dtotal = 0, attack = 0, stick = 0;
    for (unsigned i = 1; i < MAXDWARVES; ++i) {
	if (dloc[i] == 0)
	    continue;
	// Move a dwarf at random. we don't have a matrix around to do it as in the original version...
	unsigned j;
	for (unsigned tryl = 1; tryl < 20; ++tryl) {
	    j = MIST_HALL + rand() % 106;	// allowed area
	    if (j != odloc[i] && j != dloc[i] && !(i == (MAXDWARVES - 1) && (cond[j] & NOPIRAT)))
		break;
	}
	if (j == 0)
	    j = odloc[i];
	odloc[i] = dloc[i];
	dloc[i] = j;
	if ((dseen[i] && newloc >= MIST_HALL) || dloc[i] == newloc || odloc[i] == newloc)
	    dseen[i] = true;
	else
	    dseen[i] = false;
	if (!dseen[i])
	    continue;
	dloc[i] = newloc;
	if (i == 6)
	    dopirate();
	else {
	    ++dtotal;
	    if (odloc[i] == dloc[i]) {
		++attack;
		if (knfloc != CARRIED)
		    knfloc = newloc;
		if (rand() % 1000 < 95 * (dflag - 2))
		    ++stick;
	    }
	}
    }
    if (dtotal == 0)
	return;
    if (dtotal > 1)
	printf("There are %d threatening little dwarves in the room with you!\n", dtotal);
    else
	rspeak (4);
    if (attack == 0)
	return;
    if (dflag == 2)
	++dflag;
    unsigned k;
    if (attack > 1) {
	printf("%d of them throw knives at you!!\n", attack);
	k = 6;
    } else {
	rspeak (5);
	k = 52;
    }
    if (stick <= 1) {
	rspeak (stick + k);
	if (stick == 0)
	    return;
    } else
	printf("%d of them get you !!!\n", stick);
    oldloc2 = newloc;
    death();
}

// pirate stuff
static void dopirate (void)
{
    if (newloc == chloc || prop[CHEST] >= 0)
	return;
    unsigned k = 0;
    for (unsigned j = 50; j <= MAXTRS; ++j) {
	if (j != PYRAMID || (newloc != place[PYRAMID] && newloc != place[EMERALD])) {
	    if (toting(j)) {
		// Pirate steals treasure
		rspeak (128);
		if (place[MESSAGE] == 0)
		    move_object (CHEST, chloc);
		move_object (MESSAGE, chloc2);
		for (unsigned i = NUGGET; i <= MAXTRS; ++i) {
		    if (i == PYRAMID && (newloc == place[PYRAMID] || newloc == place[EMERALD]))
			continue;
		    if (at(i) && fixed[i] == 0)
			carry(i);
		    if (toting(i))
			drop (i, chloc);
		}
		dloc[6] = chloc;
		odloc[6] = chloc;
		dseen[6] = false;
		return;
	    }
	    if (here(j))
		++k;
	}
    }
    if (tally == tally2 + 1 && k == 0 && place[CHEST] == 0 && here(LAMP) && prop[LAMP] == 1) {
	rspeak (186);
	move_object (CHEST, chloc);
	move_object (MESSAGE, chloc2);
	dloc[6] = chloc;
	odloc[6] = chloc;
	dseen[6] = false;
    } else if (odloc[6] != dloc[6] && pct(20))
	rspeak (127);
}

// special time limit stuff...
static bool stimer (void)
{
    foobar = foobar > 0 ? -foobar : 0;
    if (tally == 0 && loc >= MIST_HALL && loc != Y2_ROOM)
	--clock1;
    if (clock1 == 0) {
	// start closing the cave
	prop[GRATE] = 0;
	prop[FISSURE] = 0;
	for (unsigned i = 1; i < MAXDWARVES; ++i)
	    dseen[i] = false;
	move_object (TROLL, 0);
	move_object ((TROLL + MAXOBJ), 0);
	move_object (TROLL2, CHASM_SW);
	move_object ((TROLL2 + MAXOBJ), CHASM_NE);
	if (prop[BEAR] != 3)
	    destroy_object (BEAR);
	prop[CHAIN] = 0;
	fixed[CHAIN] = 0;
	prop[AXE] = 0;
	fixed[AXE] = 0;
	rspeak (129);
	clock1 = -1;
	closing = 1;
	return false;
    }
    if (clock1 < 0)
	--clock2;
    if (clock2 == 0) {
	//
	// set up storage room...
	// and close the cave...

	prop[BOTTLE] = put (BOTTLE, REPOSITORY1, 1);
	prop[PLANT] = put (PLANT, REPOSITORY1, 0);
	prop[OYSTER] = put (OYSTER, REPOSITORY1, 0);
	prop[LAMP] = put (LAMP, REPOSITORY1, 0);
	prop[ROD] = put (ROD, REPOSITORY1, 0);
	prop[DWARF] = put (DWARF, REPOSITORY1, 0);
	loc = REPOSITORY1;
	oldloc = REPOSITORY1;
	newloc = REPOSITORY1;
	put (GRATE, REPOSITORY2, 0);
	prop[SNAKE] = put (SNAKE, REPOSITORY2, 1);
	prop[BIRD] = put (BIRD, REPOSITORY2, 1);
	prop[CAGE] = put (CAGE, REPOSITORY2, 0);
	prop[ROD2] = put (ROD2, REPOSITORY2, 0);
	prop[PILLOW] = put (PILLOW, REPOSITORY2, 0);
	prop[MIRROR] = put (MIRROR, REPOSITORY2, 0);
	fixed[MIRROR] = REPOSITORY2;
	for (unsigned i = 1; i <= MAXOBJ; ++i)
	    if (toting(i))
		destroy_object (i);
	rspeak (132);
	closed = 1;
	return true;
    }
    if (prop[LAMP] == 1)
	--limit;
    if (limit <= 30 && here(BATTERIES) && prop[BATTERIES] == 0 && here(LAMP)) {
	rspeak (188);
	prop[BATTERIES] = 1;
	if (toting(BATTERIES))
	    drop (BATTERIES, loc);
	limit += 2500;
	lmwarn = false;
	return false;
    }
    if (limit == 0) {
	--limit;
	prop[LAMP] = 0;
	if (here(LAMP))
	    rspeak (184);
	return false;
    }
    if (limit < 0 && loc <= 8) {
	rspeak (185);
	gaveup = 1;
	normend();
    }
    if (limit <= 30) {
	if (lmwarn || !here(LAMP))
	    return false;
	lmwarn = true;
	unsigned i = 187;
	if (place[BATTERIES] == 0)
	    i = 183;
	if (prop[BATTERIES] == 1)
	    i = 189;
	rspeak (i);
	return false;
    }
    return false;
}
