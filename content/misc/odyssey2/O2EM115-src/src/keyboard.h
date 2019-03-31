#ifndef __KEYBOARD_H
#define __KEYBOARD_H

void Set_Old_Int9(void);
void init_keyboard(void);
void handle_key(void);
void set_joykeys(int joy, int up, int down, int left, int right, int fire);
void set_defjoykeys(int joy, int sc);
Byte keyjoy(int jn);

extern	Byte new_int;
extern int NeedsPoll;
extern Byte key_done;
extern Byte key_debug;
extern int joykeys[2][5];
extern int joykeystab[128];

struct keyb{
	int keybcode;
	char *keybname;
};

extern struct keyb keybtab[];

#endif

