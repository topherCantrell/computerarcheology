// This file is free software, distributed under the BSD license.

#include "advent.h"
#include <signal.h>
#include <sys/uio.h>
#include <sys/stat.h>

//{{{ Global variables -------------------------------------------------

// Database variables
struct trav travel [MAXTRAV] = {};

// Command parser variables
int verb = 0;
int object = 0;
int motion = 0;
char word1 [MAXWORDLEN] = {};
char word2 [MAXWORDLEN] = {};

// Play variables
uint32_t	turns	= 0;
int16_t		clock1	= 30;		// timing variables
int16_t		clock2	= 50;
int16_t		limit	= 1000;		// time limit
uint8_t		tally	= 15;		// item counts
uint8_t		tally2	= 0;
uint8_t		holding	= 0;		// count of held items
uint8_t		numdie	= 0;		// number of deaths
uint8_t		dkill	= 0;		// dwarves killed
uint8_t		dflag	= 0;		// dwarf flag
uint8_t		foobar	= 0;		// fie fie foe foo...
uint8_t		bonus	= 0;		// to pass to end
loc_t		loc	= WELLHOUSE;	// location variables
loc_t		newloc	= END_OF_ROAD;
loc_t		oldloc	= END_OF_ROAD;
loc_t		oldloc2	= END_OF_ROAD;
loc_t		knfloc	= 0;		// knife location
loc_t		chloc	= CHEST_ROOM1;	// chest locations
loc_t		chloc2	= CHEST_ROOM2;
loc_t		daltloc	= 18;		// alternate appearance
obj_t		object1	= 0;		// to help intrans.
bool		lmwarn	= false;	// lamp warning flag
bool		wzdark	= 0;		// game state flags
bool		closing	= 0;
bool		closed	= 0;
bool		panic	= false;
bool		gaveup	= false;	// true if he quit early

bool		saveflg	= false;	// if game being saved

uint8_t	visited [(MAXLOC+1+7)/8] = {};	// true if has been here

// dwarf locations
loc_t	dloc [MAXDWARVES]  = { 0,KING_HALL,FISSURE_W,Y2_ROOM,44,CO_JUNCTION,CHEST_ROOM1 };
bool	dseen [MAXDWARVES] = {};	// dwarf seen flag
loc_t	odloc [MAXDWARVES] = {};	// dwarf old locations

struct Score game_score = {};

//}}}-------------------------------------------------------------------
//{{{ Local prototypes

static void initialize (void);
static _Noreturn void on_fatal_signal (int sig);
static uint16_t sum_save_array (void);
static bool save (void);
static int compare_scores (const void* v1, const void* v2);
static void save_score (void);

//}}}-------------------------------------------------------------------

int main (void)
{
    initialize();
    if (restore()) {
	printf ("Game restored.\n");
	describe();
    } else {
	rspeak (65);
	rspeak (1);
    }
    while (!saveflg)
	turn();
    if (saveflg)
	save();
    return EXIT_SUCCESS;
}

// normal end of game
_Noreturn void normend (void)
{
    score();
    save_score();
    exit (EXIT_SUCCESS);
}

//{{{ initialize and signal handling -----------------------------------

static void initialize (void)
{
    // Install signal handlers to ensure cleanup
    static const uint8_t c_sigs[] = {
	SIGINT, SIGQUIT, SIGTERM, SIGILL, SIGBUS,
	SIGABRT, SIGFPE, SIGSYS, SIGSEGV, SIGHUP
    };
    for (unsigned i = 0; i < ArraySize(c_sigs); ++i)
	signal (c_sigs[i], on_fatal_signal);
    srandrand();
}

#define S(s)	(1<<(s))
enum { sigset_Quit = S(SIGINT)|S(SIGQUIT)|S(SIGTERM) };
enum { exitcode_SignalBase = 128 };

static _Noreturn void on_fatal_signal (int sig)
{
    static volatile _Atomic(bool) s_once = false;
    int exitcode = exitcode_SignalBase+sig;
    if (false == atomic_exchange (&s_once, true)) {
	if (S(sig) & sigset_Quit)
	    exitcode = EXIT_SUCCESS;	// terminated by user
	else
	    psignal (sig, "Fatal error");
	save();	// try to save on crash
	exit (exitcode);
    }
    _Exit (exitcode);
}
#undef S

//}}}-------------------------------------------------------------------
//{{{ Game save and restore

//{{{2 s_save_array

#define WVAR(v)	{ &v, sizeof(v) }
#define WARR(v)	{ &v[0], sizeof(v) }

static struct iovec s_save_array[] = {
    WVAR (turns),
    WVAR (clock1),
    WVAR (clock2),
    WVAR (limit),
    WVAR (tally),
    WVAR (tally2),
    WVAR (holding),
    WVAR (numdie),
    WVAR (dkill),
    WVAR (dflag),
    WVAR (foobar),
    WVAR (bonus),
    WVAR (loc),
    WVAR (newloc),
    WVAR (oldloc),
    WVAR (oldloc2),
    WVAR (knfloc),
    WVAR (chloc),
    WVAR (chloc2),
    WVAR (daltloc),
    WVAR (object1),
    WVAR (lmwarn),
    WVAR (wzdark),
    WVAR (closing),
    WVAR (closed),
    WVAR (panic),
    WVAR (gaveup),
    WARR (visited),
    WARR (place),
    WARR (fixed),
    WARR (prop),
    WARR (dloc),
    WARR (dseen),
    WARR (odloc)
};
//}}}2

static uint16_t sum_save_array (void)
{
    uint16_t sum = 0;
    for (unsigned i = 0; i < ArraySize(s_save_array); ++i)
	sum = bsdsum ((const uint8_t*) s_save_array[i].iov_base, s_save_array[i].iov_len, sum);
    return sum;
}

struct save_header { char magictext[6]; uint16_t sum; };

static bool save (void)
{
    char savename [PATH_MAX];
    player_saved_game_dir (ArrayBlock(savename));
    if (0 != access (savename, R_OK))
	mkpath (savename, S_IRWXU);
    if (0 != access (savename, W_OK)) {
	printf ("Error: you are not allowed to write to '%s'\n", savename);
	return false;
    }
    player_saved_game_file (ArrayBlock(savename), ADVENTURE_SAVE_NAME);

    int fd = creat (savename, S_IRUSR| S_IWUSR);
    if (fd < 0) {
	printf ("Error: unable to create save file '%s': %s\n", savename, strerror(errno));
	return false;
    }
    struct save_header header = {{'a','d','v','e','n','t'}, sum_save_array()};
    if (sizeof(header) != write (fd, &header, sizeof(header))
	|| 0 >= writev (fd, s_save_array, ArraySize(s_save_array))
	|| 0 > close (fd)) {
	printf ("Error writing save file '%s': %s\n", savename, strerror(errno));
	close (fd);
	return false;
    }
    return true;
}

static bool verify_locations (void)
{
    if (loc > MAXLOC
	|| newloc > MAXLOC
	|| oldloc > MAXLOC
	|| oldloc2 > MAXLOC
	|| knfloc > CARRIED
	|| chloc > MAXLOC
	|| chloc2 > MAXLOC
	|| daltloc > MAXLOC)
	return false;
    for (unsigned i = 0; i < ArraySize(place); ++i)
	if (place[i] > CARRIED)
	    return false;
    for (unsigned i = 0; i < ArraySize(fixed); ++i)
	if (fixed[i] > CARRIED)
	    return false;
    for (unsigned i = 0; i < ArraySize(dloc); ++i)
	if (dloc[i] > MAXLOC)
	    return false;
    for (unsigned i = 0; i < ArraySize(odloc); ++i)
	if (odloc[i] > MAXLOC)
	    return false;
    return true;
}

bool restore (void)
{
    char savename [PATH_MAX];
    player_saved_game_file (ArrayBlock(savename), ADVENTURE_SAVE_NAME);
    int fd = open (savename, O_RDONLY);
    if (fd < 0)
	return false;

    struct save_header header;
    if (sizeof(header) != read (fd, &header, sizeof(header))
	|| 0 >= readv (fd, s_save_array, ArraySize(s_save_array))) {
	printf ("Error: reading '%s': %s\n", savename, strerror(errno));
	close (fd);
	exit (EXIT_FAILURE);
    }
    close (fd);
    if (memcmp (header.magictext, "advent", sizeof(header.magictext)) != 0
	|| header.sum != sum_save_array()
	|| !verify_locations()) {
	printf ("Error: saved game '%s' is corrupt. Please delete it.\n", savename);
	exit (EXIT_FAILURE);
    }
    unlink (savename);
    return true;
}

//}}}-------------------------------------------------------------------
//{{{ Scoring

// scoring
void score (void)
{
    unsigned k = 0, s = 0;
    for (obj_t i = NUGGET; i <= MAXTRS; ++i) {
	if (i == CHEST)
	    k = 14;
	else if (i > CHEST)
	    k = 16;
	else
	    k = 12;
	if (prop[i] >= 0)
	    s += 2;
	if (place[i] == WELLHOUSE && prop[i] == 0)
	    s += k - 2;
    }
    game_score.treasures = s;
    unsigned t = (MAXDIE - numdie) * 10;
    game_score.survival = t;
    s += t;
    if (!gaveup)
	s += 4;
    t = dflag ? 25 : 0;
    game_score.wellin = t;
    s += t;
    t = closing ? 25 : 0;
    game_score.masters = t;
    s += t;
    if (closed) {
	if (bonus == 0)
	    t = 10;
	else if (bonus == 135)
	    t = 25;
	else if (bonus == 134)
	    t = 30;
	else if (bonus == 133)
	    t = 45;
	game_score.bonus = t;
	s += t;
    }
    if (place[MAGAZINE] == WITTS_END)
	s += 1;
    s += 2;
    game_score.total = s;
    snprintf (ArrayBlock (game_score.name), "%s", player_name());

    printf ("%-20s%u\n", "Treasures:", game_score.treasures);
    if (game_score.survival)
	printf("%-20s%u\n", "Survival:", game_score.survival);
    if (game_score.wellin)
	printf("%-20s%d\n", "Getting well in:", game_score.wellin);
    if (game_score.masters)
	printf("%-20s%d\n", "Masters section:", game_score.masters);
    if (game_score.bonus)
	printf("%-20s%d\n", "Bonus:", game_score.bonus);
    printf ("%-20s%d\n", "Score:", game_score.total);
}

static int compare_scores (const void* v1, const void* v2)
    { return sign (((const struct Score*)v2)->total - ((const struct Score*)v1)->total); }

static void save_score (void)
{
    struct Score scores [MAXSCORES] = {};
    read_score_file (ADVENTURE_SCOREFILE, SCOREFILE_MAGIC, scores, sizeof(scores));

    // Check each score and zero if invalid
    for (struct Score *s = scores, *send = &scores[ArraySize(scores)]; s < send; ++s)
	if (!s->name[0] || s->name[sizeof(s->name)-1] || s->total > 350)
	    memset (s, 0, sizeof(*s));
    // Resort to account for the above zeroing
    qsort (ArrayBlock(scores), sizeof(scores[0]), compare_scores);

    // Add this game's score, if it is high enough
    struct Score* lowscore = &scores[ArraySize(scores)-1];
    if (game_score.name[0] && lowscore->total < game_score.total) {
	*lowscore = game_score;
	// Resort the new score
	qsort (ArrayBlock(scores), sizeof(scores[0]), compare_scores);
	// And write the score file
	write_score_file (ADVENTURE_SCOREFILE, SCOREFILE_MAGIC, scores, sizeof(scores));
    }

    // List top scores
    puts ("\n-#--Name-----Sco----T---E---M---B");
    for (unsigned i = 0; i < ArraySize(scores) && scores[i].total; ++i) {
	if (game_score.total == scores[i].total && game_score.treasures == scores[i].treasures && 0 == strcmp (game_score.name, scores[i].name))
	    printf (BOLD_ON);
	printf ("%2u: %-8s %3u  %3u %3u %3u %3u\n" BOLD_OFF, i+1, scores[i].name, scores[i].total, scores[i].treasures, scores[i].wellin, scores[i].masters, scores[i].bonus);
    }
}

//}}}-------------------------------------------------------------------
