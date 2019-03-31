#ifndef __VDC_H
#define __VDC_H

#define BMPW 340
#define BMPH 250
#define WNDW 320
#define WNDH 240

extern Byte coltab[];
extern long clip_low;
extern long clip_high;
extern int show_fps;

void init_display(void);
void draw_display(void);
void set_textmode(void);
void draw_region(void);
void finish_display();
void close_display(void);
void grmode(void);
void display_info(void);
void clear_collision(void);
void clearscr(void);

#endif


