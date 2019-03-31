
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
 *   O2 Video Display Controller emulation
 */


#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "types.h"
#include "vmachine.h"
#include "config.h"
#include "keyboard.h"
#include "cset.h"
#include "timefunc.h"
#include "cpu.h"
#include "vpp.h"
#include "vdc.h"
#include "allegro.h"


#define COL_SP0   0x01
#define COL_SP1   0x02
#define COL_SP2   0x04
#define COL_SP3   0x08
#define COL_VGRID 0x10
#define COL_HGRID 0x20
#define COL_VPP   0x40
#define COL_CHAR  0x80

#define X_START     8
#define Y_START		24


static long colortable[16]={
	0x000000,
	0x0000b6,
	0x00b600,
	0x00b6b6,
	0xb60000,
	0xb600b6,
	0xb6b600,
	0xb6b6b6,
	0x494949,
	0x4949ff,
	0x49ff49,
	0x49ffff,
	0xff4949,
	0xff49ff,
	0xffff49,
	0xffffff
};


/* Collision buffer */
static Byte *col = NULL;

static PALETTE colors,oldcol;

/* The pointer to the graphics buffer */
static Byte *vscreen = NULL;

static BITMAP *bmp, *bmpcache;
static int cached_lines[MAXLINES];

Byte coltab[256];

long clip_low;
long clip_high;

int show_fps=0;

int wsize;

static void create_cmap(void);
static void draw_char(Byte ypos,Byte xpos,Byte chr,Byte col);
static void draw_grid(void);
INLINE void mputvid(unsigned int ad, unsigned int len, Byte d, Byte c);


void draw_region(void){
	int i;
	
	if (regionoff == 0xffff)
		i = master_clk/(LINECNT-1)-5;
	else
		i = master_clk/22+regionoff;

	i = snapline(i, VDCwrite[0xA0], 0);

	if (i<0) i=0;
 	clip_low = last_line * (long)BMPW;
	clip_high = i * (long)BMPW;
	if (clip_high > BMPW*BMPH) clip_high = BMPW*BMPH;
	if (clip_low < 0) clip_low=0; 
	if (clip_low < clip_high) draw_display();
	last_line=i;
}


static void create_cmap(void){
  int i;

  /* Initialise parts of the colors array */
  for (i = 0; i < 16; i++) {
      /* Use the color values from the color table */
      colors[i+32].r = colors[i].r = (colortable[i] & 0xff0000) >> 18;
      colors[i+32].g = colors[i].g = (colortable[i] & 0x00ff00) >> 10;
      colors[i+32].b = colors[i].b = (colortable[i] & 0x0000ff) >> 2;
  }

  for (i = 16; i < 32; i++) {
      /* Half-bright colors for the 50% scanlines */
      colors[i+32].r = colors[i].r = colors[i-16].r/2;
      colors[i+32].g = colors[i].g = colors[i-16].g/2;
      colors[i+32].b = colors[i].b = colors[i-16].b/2;
  }
	
  for (i = 64; i < 256; i++) colors[i].r = colors[i].g = colors[i].b = 0;
}


void grmode(void){

	set_color_depth(8);

	wsize = app_data.wsize;
	
	if (app_data.fullscreen){
		if (app_data.scanlines){
			wsize = 2;		
			if (set_gfx_mode(GFX_AUTODETECT_FULLSCREEN, 640, 480, 0, 0)){
				wsize = 1;
				if (set_gfx_mode(GFX_AUTODETECT_FULLSCREEN, 320, 240, 0, 0)) {
					fprintf(stderr,"Error: could not create screen.\n");
					exit(EXIT_FAILURE);
				}
			}
		} else {
			#ifdef ALLEGRO_DOS
			wsize = 1;
			if (set_gfx_mode(GFX_AUTODETECT_FULLSCREEN, 320, 240, 0, 0)){
				wsize = 2;
				if (set_gfx_mode(GFX_AUTODETECT_FULLSCREEN, 640, 480, 0, 0)){
					fprintf(stderr,"Error: could not create screen.\n");
					exit(EXIT_FAILURE);
				}
			}
			#else
			wsize = 2;
			if (set_gfx_mode(GFX_AUTODETECT_FULLSCREEN, 640, 480, 0, 0)){
				wsize = 1;
				if (set_gfx_mode(GFX_AUTODETECT_FULLSCREEN, 320, 240, 0, 0)){
					fprintf(stderr,"Error: could not create screen.\n");
					exit(EXIT_FAILURE);
				}
			}
			#endif
		}
	} else {
		if (set_gfx_mode(GFX_AUTODETECT_WINDOWED, WNDW*wsize, WNDH*wsize, 0, 0)){
			wsize = 2;
			if (set_gfx_mode(GFX_AUTODETECT_WINDOWED, WNDW*2, WNDH*2, 0, 0)){
				if (set_gfx_mode(GFX_AUTODETECT, WNDW*2, WNDH*2, 0, 0)){
					fprintf(stderr,"Error: could not create window.\n");
					exit(EXIT_FAILURE);
				}
			}
			#ifndef ALLEGRO_DOS
			printf("Could not set the requested window size\n");
			#endif
		}
	}

	if ((app_data.scanlines) && (wsize==1)) {
		#ifndef ALLEGRO_DOS
		printf("Could not set scanlines\n");
		#endif
	}

	set_palette(colors);
	set_window_title(app_data.window_title);
	clearscr();
	set_display_switch_mode(SWITCH_PAUSE);
}


void set_textmode(void){
	set_palette(oldcol);
	set_gfx_mode(GFX_TEXT, 0, 0, 0, 0);
	if (new_int) Set_Old_Int9();
}


void clearscr(void){
	acquire_screen();
	clear(screen);
	release_screen();
	clear(bmpcache);
}


INLINE void mputvid(unsigned int ad, unsigned int len, Byte d, Byte c){
	if ((ad > (unsigned long)clip_low) && (ad < (unsigned long)clip_high)) {
		unsigned int i;
		if (((len & 3)==0) && (sizeof(unsigned long) == 4)) {
			unsigned long dddd = (((unsigned long)d) & 0xff) | ((((unsigned long)d) & 0xff) << 8) | ((((unsigned long)d) & 0xff) << 16) | ((((unsigned long)d) & 0xff) << 24);
			unsigned long cccc = (((unsigned long)c) & 0xff) | ((((unsigned long)c) & 0xff) << 8) | ((((unsigned long)c) & 0xff) << 16) | ((((unsigned long)c) & 0xff) << 24);
			for (i=0; i<len>>2; i++) {
				*((unsigned long*)(vscreen+ad)) = dddd;
				cccc |= *((unsigned long*)(col+ad));
				*((unsigned long*)(col+ad)) = cccc;
				coltab[c] |= ((cccc | (cccc >> 8) | (cccc >> 16) | (cccc >> 24)) & 0xff);
				ad += 4;
			}
		} else {
			for (i=0; i<len; i++) {
				vscreen[ad]=d;
				col[ad] |= c;
				coltab[c] |= col[ad++];
			}
		}
	}
}


static void draw_grid(void){
	unsigned int pnt, pn1;
	Byte mask,d;
	int j,i,x,w;
	Byte color;

	if (VDCwrite[0xA0] & 0x40) {
		for(j=0; j<9; j++) {
			pnt = (((j*24)+24) * BMPW);
			for (i=0; i<9; i++) {
				pn1 = pnt + (i * 32) + 20;
				color = ColorVector[j*24+24];
				mputvid(pn1, 4, (color & 0x07) | ((color & 0x40) >> 3) | (color & 0x80 ? 0 : 8), COL_HGRID);
				color = ColorVector[j*24+25];
				mputvid(pn1+BMPW, 4, (color & 0x07) | ((color & 0x40) >> 3) | (color & 0x80 ? 0 : 8), COL_HGRID);
				color = ColorVector[j*24+26];
				mputvid(pn1+BMPW*2, 4, (color & 0x07) | ((color & 0x40) >> 3) | (color & 0x80 ? 0 : 8), COL_HGRID);
			}
		}
	}

	mask=0x01;
	for(j=0; j<9; j++) {
		pnt = (((j*24)+24) * BMPW);
		for (i=0; i<9; i++) {
			pn1 = pnt + (i * 32) + 20;
			if ((pn1+BMPW*3 >= (unsigned long)clip_low) && (pn1 <= (unsigned long)clip_high)) {
				d=VDCwrite[0xC0 + i];
				if (j == 8) {
					d=VDCwrite[0xD0+i];
					mask=1;
				}
				if (d & mask)	{
					color = ColorVector[j*24+24];
					mputvid(pn1, 36, (color & 0x07) | ((color & 0x40) >> 3) | (color & 0x80 ? 0 : 8), COL_HGRID);
					color = ColorVector[j*24+25];
					mputvid(pn1+BMPW, 36, (color & 0x07) | ((color & 0x40) >> 3) | (color & 0x80 ? 0 : 8), COL_HGRID);
					color = ColorVector[j*24+26];
					mputvid(pn1+BMPW*2, 36, (color & 0x07) | ((color & 0x40) >> 3) | (color & 0x80 ? 0 : 8), COL_HGRID);
				}
			}
		}
		mask = mask << 1;
	}

	mask=0x01;
	w=4;
	if (VDCwrite[0xA0] & 0x80) w=32;
	for(j=0; j<10; j++) {
		pnt=(j*32);
		mask=0x01;
		d=VDCwrite[0xE0+j];
		for (x=0; x<8; x++) {
			pn1 = pnt + (((x*24)+24) * BMPW) + 20;
			if (d & mask) {
				for(i=0; i<24; i++) {
					if ((pn1 >= (unsigned long)clip_low) && (pn1 <= (unsigned long)clip_high)) {
						color = ColorVector[x*24+24+i];
						mputvid(pn1, w, (color & 0x07) | ((color & 0x40) >> 3) | (color & 0x80 ? 0 : 8), COL_VGRID);
					}
					pn1+=BMPW;
				}
			}
			mask = mask << 1;
		}
	}

}


void finish_display(void){
	int x,y,sn;
	static int cache_counter=0;

	vpp_finish_bmp(vscreen, 9, 5, BMPW-9, BMPH-5, bmp->w, bmp->h);

	if (show_fps) {
		static long last=-1, index=0, curr=0, t=0;
		if (last<0) last=gettimeticks();
		index = (index+1)%200;
		if (!index) {
			t=gettimeticks();
			curr=t-last;
			last=t;
		}
		if (curr) {
			text_mode(0);
			textprintf(bmp, font, 20 , 4, 7, "FPS: %3d",(int)((200.0*TICKSPERSEC)/curr+0.5));
		}
	}

	for (y=0; y<bmp->h; y++){
		cached_lines[y] = !memcmp(bmpcache->line[y], bmp->line[y], bmp->w);
		if (!cached_lines[y]) memcpy(bmpcache->line[y], bmp->line[y], bmp->w);
	}

	for (y=0; y<10; y++) cached_lines[(y+cache_counter) % bmp->h] = 0;
	cache_counter = (cache_counter+10) % bmp->h;

	acquire_screen();

	sn = ((wsize>1) && (app_data.scanlines)) ? 1 : 0;

	for (y=0; y<WNDH; y++){
		if (!cached_lines[y+2])
			stretch_blit(bmp,screen,7,2+y,WNDW,1,0,y*wsize,WNDW*wsize,wsize-sn);
	}

	if (sn){
		for (y=0; y<WNDH; y++) {
			if (!cached_lines[y+2]) {
				for (x=0; x<bmp->w; x++) bmp->line[y+2][x] += 16;
				stretch_blit(bmp,screen,7,2+y,WNDW,1,0,(y+1)*wsize-1,WNDW*wsize,1);
				memcpy(bmp->line[y+2], bmpcache->line[y+2], bmp->w);
			}
		}
	}

	release_screen();

}


void clear_collision(void){
	load_colplus(col);
	coltab[0x01]=coltab[0x02]=0;
	coltab[0x04]=coltab[0x08]=0;
	coltab[0x10]=coltab[0x20]=0;
	coltab[0x40]=coltab[0x80]=0;
}


void draw_display(void){
	int i,j,x,sm,t;
	Byte y,xt,yt,b,d1,cl,c;
	unsigned int pnt,pnt2;

	for (i=clip_low/BMPW; i<clip_high/BMPW; i++) memset(vscreen+i*BMPW, ((ColorVector[i] & 0x38) >> 3) | (ColorVector[i] & 0x80 ? 0 : 8), BMPW);
	
	if (VDCwrite[0xA0] & 0x08) draw_grid();

	if (useforen && (!(VDCwrite[0xA0] & 0x20))) return;
	
	for(i=0x10; i<0x40; i+=4) draw_char(VDCwrite[i],VDCwrite[i+1],VDCwrite[i+2],VDCwrite[i+3]);

	pnt=0x40;
	for(i=0; i<4; i++) {
		x=y=248;
		for (j=0; j<4; j++){
			xt = VDCwrite[pnt+j*4+1];
			yt = VDCwrite[pnt+j*4];
			if ((xt<240) && (yt<240)){
				x=xt;
				y=yt;
				break;
			}
		}
		for(j=0; j<4; j++) {
			draw_char(y,x,VDCwrite[pnt+2],VDCwrite[pnt+3]);
			x+=16;
			pnt+=4;
		}
	}
	c=8;
	for (i=12; i>=0; i -=4) {
		pnt2 = 0x80 + (i * 2);
		y = VDCwrite[i];
		x = VDCwrite[i+1]-8;
		t = VDCwrite[i+2];
		cl = ((t & 0x38) >> 3);
		cl = ((cl&2) | ((cl&1)<<2) | ((cl&4)>>2)) + 8;
		if ((x<164) && (y>0) && (y<232)) {
			pnt = y * BMPW + (x * 2) + 20 + sproff;
			if (t & 4) {
				if ((pnt+BMPW*32 >= (unsigned long)clip_low) && (pnt <= (unsigned long)clip_high)) {
					for (j=0; j<8; j++) {
						sm = (((j%2==0) && (((t>>1) & 1) != (t & 1))) || ((j%2==1) && (t & 1))) ? 1 : 0;
						d1 = VDCwrite[pnt2++];
						for (b=0; b<8; b++) {
							if (d1 & 0x01) {
								if ((x+b+sm < 159) && (y+j < 247)) {
									mputvid(sm+pnt,4,cl,c);
									mputvid(sm+pnt+BMPW,4,cl,c);
									mputvid(sm+pnt+2*BMPW,4,cl,c);
									mputvid(sm+pnt+3*BMPW,4,cl,c);
								}
							}
							pnt += 4;
							d1 = d1 >> 1;
						}
						pnt += BMPW*4-32;
					}
				}
			} else {
				if ((pnt+BMPW*16 >= (unsigned long)clip_low) && (pnt <= (unsigned long)clip_high)) {
					for (j=0; j<8; j++) {
						sm = (((j%2==0) && (((t>>1) & 1) != (t & 1))) || ((j%2==1) && (t & 1))) ? 1 : 0;
						d1 = VDCwrite[pnt2++];
						for (b=0; b<8; b++) {
							if (d1 & 0x01) {
								if ((x+b+sm<160) && (y+j<249)) {
									mputvid(sm+pnt,2,cl,c);
									mputvid(sm+pnt+BMPW,2,cl,c);
								}
							}
							pnt += 2;
							d1 = d1 >> 1;
						}
						pnt += BMPW*2-16;
					}
				}
			}
		}
		c = c >> 1;
	}
}


void draw_char(Byte ypos,Byte xpos,Byte chr,Byte col){
	int j,c;
	Byte cl,d1;
	int y,b,n;
	unsigned int pnt;

	y=(ypos & 0xFE); 
	pnt = y * BMPW + ((xpos-8) * 2)+20;

	ypos = ypos >> 1;
	n = 8 - (ypos % 8) - (chr % 8);
	if (n < 3) n = n + 7;
	
	if ((pnt+BMPW*2*n >= (unsigned long)clip_low) && (pnt <= (unsigned long)clip_high)) {

		c=(int)chr + ypos;
		if (col & 0x01) c+=256;
		if (c > 511) c=c-512;

		cl = ((col & 0x0E) >> 1);
		cl = ((cl&2) | ((cl&1)<<2) | ((cl&4)>>2)) + 8;

		if ((y>0) && (y<232) && (xpos<157)) {
			for (j=0; j<n; j++) {
				d1 = cset[c+j];
				for (b=0; b<8; b++) {
					if (d1 & 0x80) {
						if ((xpos-8+b < 160) && (y+j < 240)) {
							mputvid(pnt,2,cl,COL_CHAR);
							mputvid(pnt+BMPW,2,cl,COL_CHAR);
						}
					}
					pnt+=2;
					d1 = d1 << 1;
				}
				pnt += BMPW*2-16;
			}
		}
	}
}


void close_display(void) {
	free(vscreen);
	free(col);
}


void window_close_hook(void){
	key_debug=0;
	key_done=1;
}


static void txtmsg(int x, int y, int c, const char *s){
	text_mode(-1);
	textout_centre(bmp, font, s, x+1 , y+1, 32);
	textout_centre(bmp, font, s, x , y, c);
}


void display_info(void){
	char *ver;

	rectfill(bmp,20,72,311,158,9+32);
	line(bmp,20,72,311,72,15+32);
	line(bmp,20,72,20,158,15+32);
	line(bmp,21,158,311,158,1+32);
	line(bmp,311,158,311,72,1+32);

	#if defined(ALLEGRO_WINDOWS)
	ver = "Windows version";
	#elif defined(ALLEGRO_DOS)
	ver = "DOS version";
	#elif defined(ALLEGRO_LINUX)
	ver = "Linux version";
	#elif defined(ALLEGRO_BEOS)
	ver = "BEOS version";
	#elif defined(ALLEGRO_QNX)
	ver = "QNX version";
	#elif defined(ALLEGRO_UNIX)
	ver = "UNIX version";
	#elif defined(ALLEGRO_MPW)
	ver = "MacOS version";
	#else
	ver = "Unknown platform";
	#endif

	txtmsg(166,76,15+32,"O2EM v" O2EM_VERSION "  " RELEASE_DATE);
	txtmsg(166,90,15+32,"Free Odyssey2 / VP+ Emulator");
	txtmsg(166,104,15+32,ver);
	txtmsg(166,118,15+32,"Developed by Andre de la Rocha");
	txtmsg(166,132,15+32,"Copyright 1996/1998 by Daniel Boris");
	txtmsg(166,148,15+32,"Press F1 to continue");

	finish_display();
}


void init_display(void) {

	get_palette(oldcol);
	create_cmap();

	bmp = create_bitmap(BMPW,BMPH);
	bmpcache = create_bitmap(BMPW,BMPH);
	
	if ((!bmp) || (!bmpcache)) {
		fprintf(stderr,"Could not allocate memory for screen buffer.\n");
		exit(EXIT_FAILURE);
	}

	vscreen = (Byte *) bmp->dat;

    clear(bmp);
    clear(bmpcache);

	col = (Byte *)malloc(BMPW*BMPH);
	if (!col) {
		fprintf(stderr,"Could not allocate memory for collision buffer.\n");
		free(vscreen);
		exit(EXIT_FAILURE);
	}
	memset(col,0,BMPW*BMPH);

	if (!app_data.debug) {
		grmode();
		init_keyboard();
	}

	set_window_close_button(TRUE);
	set_window_close_hook(window_close_hook);

}

