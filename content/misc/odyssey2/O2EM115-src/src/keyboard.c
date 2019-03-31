
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
 *   Keyboard emulation
 */


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "types.h"
#include "cpu.h"
#include "vmachine.h"
#include "vdc.h"
#include "audio.h"
#include "voice.h"
#include "vpp.h"
#include "keyboard.h"
#include "allegro.h"


int NeedsPoll = 0;

Byte keycode;
Byte last_key;
Byte new_int=0;	/* Is new interrupt installed */

Byte key_done=0;
Byte key_debug=0;

struct keyb keybtab[] = {
	{KEY_A,"A"},
	{KEY_B,"B"},
	{KEY_C,"C"},
	{KEY_D,"D"},
	{KEY_E,"E"},
	{KEY_F,"F"},
	{KEY_G,"G"},
	{KEY_H,"H"},
	{KEY_I,"I"},
	{KEY_J,"J"},
	{KEY_K,"K"},
	{KEY_L,"L"},
	{KEY_M,"M"},
	{KEY_N,"N"},
	{KEY_O,"O"},
	{KEY_P,"P"},
	{KEY_Q,"Q"},
	{KEY_R,"R"},
	{KEY_S,"S"},
	{KEY_T,"T"},
	{KEY_U,"U"},
	{KEY_V,"V"},
	{KEY_W,"W"},
	{KEY_X,"X"},
	{KEY_Y,"Y"},
	{KEY_Z,"Z"},
	{KEY_0,"0"},
	{KEY_1,"1"},
	{KEY_2,"2"},
	{KEY_3,"3"},
	{KEY_4,"4"},
	{KEY_5,"5"},
	{KEY_6,"6"},
	{KEY_7,"7"},
	{KEY_8,"8"},
	{KEY_9,"9"},
	{KEY_0_PAD,"0_PAD"},
	{KEY_1_PAD,"1_PAD"},
	{KEY_2_PAD,"2_PAD"},
	{KEY_3_PAD,"3_PAD"},
	{KEY_4_PAD,"4_PAD"},
	{KEY_5_PAD,"5_PAD"},
	{KEY_6_PAD,"6_PAD"},
	{KEY_7_PAD,"7_PAD"},
	{KEY_8_PAD,"8_PAD"},
	{KEY_9_PAD,"9_PAD"},
	{KEY_TILDE,"TILDE"},
	{KEY_MINUS,"MINUS"},
	{KEY_EQUALS,"EQUALS"},
	{KEY_BACKSPACE,"BACKSPACE"},
	{KEY_TAB,"TAB"},
	{KEY_OPENBRACE,"OPENBRACE"},
	{KEY_CLOSEBRACE,"CLOSEBRACE"},
	{KEY_ENTER,"ENTER"},
	{KEY_COLON,"COLON"},
	{KEY_QUOTE,"QUOTE"},
	{KEY_BACKSLASH,"BACKSLASH"},
	{KEY_BACKSLASH2,"BACKSLASH2"},
	{KEY_COMMA,"COMMA"},
	{KEY_STOP,"STOP"},
	{KEY_SLASH,"SLASH"},
	{KEY_SPACE,"SPACE"},
	{KEY_INSERT,"INSERT"},
	{KEY_DEL,"DEL"},
	{KEY_HOME,"HOME"},
	{KEY_END,"END"},
	{KEY_PGUP,"PGUP"},
	{KEY_PGDN,"PGDN"},
	{KEY_LEFT,"LEFT"},
	{KEY_RIGHT,"RIGHT"},
	{KEY_UP,"UP"},
	{KEY_DOWN,"DOWN"},
	{KEY_SLASH_PAD,"SLASH_PAD"},
	{KEY_ASTERISK,"ASTERISK"},
	{KEY_MINUS_PAD,"MINUS_PAD"},
	{KEY_PLUS_PAD,"PLUS_PAD"},
	{KEY_DEL_PAD,"DEL_PAD"},
	{KEY_ENTER_PAD,"ENTER_PAD"},
	{KEY_PRTSCR,"PRTSCR"},
	{KEY_PAUSE,"PAUSE"},
	{KEY_ABNT_C1,"ABNT_C1"},
	{KEY_YEN,"YEN"},
	{KEY_KANA,"KANA"},
	{KEY_AT,"AT"},
	{KEY_CIRCUMFLEX,"CIRCUMFLEX"},
	{KEY_COLON2,"COLON2"},
	{KEY_KANJI,"KANJI"},
	{KEY_LSHIFT,"LSHIFT"},
	{KEY_RSHIFT,"RSHIFT"},
	{KEY_LCONTROL,"LCONTROL"},
	{KEY_RCONTROL,"RCONTROL"},
	{KEY_ALT,"ALT"},
	{KEY_ALTGR,"ALTGR"},
	{KEY_LWIN,"LWIN"},
	{KEY_RWIN,"RWIN"},
	{KEY_MENU,"MENU"},
	{KEY_SCRLOCK,"SCRLOCK"},
	{KEY_NUMLOCK,"NUMLOCK"},
	{0,""}
};


int joykeys[2][5] = {{0,0,0,0,0},{0,0,0,0,0}};
int joykeystab[128];


void set_defjoykeys(int jn, int sc){
	if (sc)
		set_joykeys(jn,KEY_W,KEY_S,KEY_A,KEY_D,KEY_SPACE);
	else
		set_joykeys(jn,KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT,KEY_RSHIFT);
}
	

void set_joykeys(int jn, int up, int down, int left, int right, int fire){
	int i,j;
	if ((jn<0) || (jn>1)) return;
	joykeys[jn][0] = up;
	joykeys[jn][1] = down;
	joykeys[jn][2] = left;
	joykeys[jn][3] = right;
	joykeys[jn][4] = fire;

	for (i=0; i<128; i++) joykeystab[i]=0;

	for (j=0; j<2; j++)
		for (i=0; i<5; i++) {
			if ((joykeys[j][i]<1) || (joykeys[j][i]>127))
				joykeys[j][i] = 0;
			else
				joykeystab[joykeys[j][i]] = 1;
		}
}
	

void handle_key(void){
	if (NeedsPoll) poll_keyboard();
	if (key[KEY_ESC] || key[KEY_F12]) {
		do {
			rest(5);
			if (NeedsPoll) poll_keyboard();
		} while (key[KEY_ESC] || key[KEY_F12]);
		key_done=1;
	}
    if (key[KEY_F5]) {
    	init_cpu();
		init_roms();
		init_vpp();
		clearscr();
		do {
			rest(5);
			if (NeedsPoll) poll_keyboard();
		} while (key[KEY_F5]);
    }

	if (key[KEY_F4]) key_debug=1;

	if (key[KEY_F1]) {
		do {
			rest(5);
			if (NeedsPoll) poll_keyboard();
		} while (key[KEY_F1]);

		mute_audio();
		mute_voice();
		display_info();

		do {
			rest(5);
			if (NeedsPoll) poll_keyboard();

			if (key[KEY_ALT] && key[KEY_ENTER]) {
				app_data.fullscreen = app_data.fullscreen ? 0 : 1;
				grmode();
				display_info();
				do {
					rest(5);
					if (NeedsPoll) poll_keyboard();
				} while (key[KEY_ENTER]);
			}		

		} while ((!key[KEY_F1]) && (!key[KEY_ESC]) && (!key[KEY_F12]));
		do {
			rest(5);
			if (NeedsPoll) poll_keyboard();
		} while (key[KEY_F1]);
		
		init_sound_stream();
	}		

	if (key[KEY_F8]) {
		BITMAP *bmp;
		PALETTE pal;
		char *p;
		static char name[1024];
		static int scshot_counter = 0;

		if (strlen(app_data.scshot)>0){
			if ((p=strchr(app_data.scshot,'@'))) {
				*p = 0;
				sprintf(name, "%s%02d%s", app_data.scshot, scshot_counter++, p+1);
				*p = '@';
			} else {
				strcpy(name, app_data.scshot);
			}
			get_palette(pal);
			bmp = create_sub_bitmap(screen, 0, 0, SCREEN_W, SCREEN_H);
			save_bitmap(name, bmp, pal);
			destroy_bitmap(bmp);
			do {
				rest(5);
				if (NeedsPoll) poll_keyboard();
			} while (key[KEY_F8]);
		}
	}


	if (key[KEY_ALT] && key[KEY_ENTER]) {
		app_data.fullscreen = app_data.fullscreen ? 0 : 1;
		grmode();
		do {
			rest(5);
			if (NeedsPoll) poll_keyboard();
		} while (key[KEY_ENTER]);
	}		

}


Byte keyjoy(int jn){
	Byte d;
	d=0xFF;
	if ((jn>=0) && (jn<=1)){
		if (NeedsPoll) poll_keyboard();
		if (key[joykeys[jn][0]]) d &= 0xFE;
		if (key[joykeys[jn][1]]) d &= 0xFB;
		if (key[joykeys[jn][2]]) d &= 0xF7;
		if (key[joykeys[jn][3]]) d &= 0xFD;
		if (key[joykeys[jn][4]]) d &= 0xEF;
	}
	return d;
}


void init_keyboard(void){
	key_done=0;
	key_debug=0;   
	install_keyboard();		
	new_int=1;
	NeedsPoll = keyboard_needs_poll();
}


void Set_Old_Int9(void){
   remove_keyboard();
   new_int=0;
}

