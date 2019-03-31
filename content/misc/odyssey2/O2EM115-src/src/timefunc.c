
/*
 *   O2EM Free Odyssey2 / Videopac+ Emulator
 *
 *   Created by Daniel Boris <dboris@comcast.net>  (c) 1997,1998
 *
 *   Developed by Andre de la Rocha <adlroc@users.sourceforge.net>
 *
 *   http://o2em.sourceforge.net
 *
 *
 *
 *   Timing functions
 */


#include <time.h>
#include "allegro.h"
#ifdef ALLEGRO_WINDOWS
#include "winalleg.h"
#elif defined(ALLEGRO_UNIX) || defined(ALLEGRO_LINUX)
#include <sys/time.h>
#include <sys/times.h>
#endif
#include "timefunc.h"



#ifdef ALLEGRO_WINDOWS

/* Windows */
long gettimeticks(void){
	LARGE_INTEGER counter, freq;
	static LONG_LONG first=-1;
	if (QueryPerformanceCounter(&counter))
		if (QueryPerformanceFrequency(&freq)) {
			if (first<0) first = counter.QuadPart;
			return (long)(((counter.QuadPart-first)*TICKSPERSEC)/freq.QuadPart);
		}
	return (long)((((LONG_LONG)clock())*TICKSPERSEC)/CLOCKS_PER_SEC);
}

#elif defined(ALLEGRO_UNIX) || defined(ALLEGRO_LINUX)

#ifdef _BSD_SOURCE

/* Unix with gettimeofday */
long gettimeticks(void){
	struct timeval tv;
	static LONG_LONG first=-1;
	LONG_LONG ll;
	if (first<0) {
		if (gettimeofday(&tv, NULL) != 0)
			return (long)((((LONG_LONG)clock())*TICKSPERSEC)/CLOCKS_PER_SEC);
		first = ((LONG_LONG)tv.tv_sec)*1000000 + tv.tv_usec;
	}
	if (gettimeofday(&tv, NULL) == 0) {
		ll = ((LONG_LONG)tv.tv_sec)*1000000 + tv.tv_usec;
		return (long) (((ll-first)*TICKSPERSEC)/1000000);
	}
	return (long)((((LONG_LONG)clock())*TICKSPERSEC)/CLOCKS_PER_SEC);
}

#else

/* Unix without gettimeofday */
long gettimeticks(void){
	struct tms t;
	return (long)((((LONG_LONG)times(&t))*TICKSPERSEC)/sysconf(_SC_CLK_TCK));
}

#endif

#else

/* Default (use Allegro timers) */

volatile long ticks_counter = 0;
static int timer_init = 0;

void inc_ticks_counter(void){
   ticks_counter++;
}

END_OF_FUNCTION(inc_ticks_counter);

long gettimeticks(void){
	if (timer_init==0) {
		ticks_counter=0;
		LOCK_VARIABLE(ticks_counter);
		LOCK_FUNCTION(inc_ticks_counter);
   		install_int(inc_ticks_counter, 1);
   		timer_init=1;
	}
	return (long)(((LONG_LONG)ticks_counter*TICKSPERSEC)/1000);
}

#endif

