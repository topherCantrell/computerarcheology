
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
 *   O2EM built-in debugger
 */


#include <stdio.h>
#include <string.h>
#include "cpu.h"
#include "keyboard.h"
#include "vmachine.h"
#include "audio.h"
#include "vdc.h"
#include "table.h"
#include "debug.h"
#include "allegro.h"

#if defined(ALLEGRO_WINDOWS)
#include "winalleg.h"
#include <conio.h>
#define KBHIT _kbhit
#elif defined(ALLEGRO_DOS)
#include <conio.h>
#define KBHIT kbhit
#else
#define KBHIT() 0
#endif

static int disasm(ADDRESS p);
static void show_reg(void);


void debug(void) {
	int done,i,go,j;
	char inp[80];
	char *tok;
	ADDRESS ad,run_to;
	char cr[2],ff[2];
	Byte d,a;

	dbstick1=dbstick2=0;
	cr[0]=13;
	cr[1]=0;
	ff[0]=0x0c;
	ff[1]=0;

	done=go=0;

	set_display_switch_mode(SWITCH_BACKGROUND);
	
	if (sndlog) fclose(sndlog);

	#ifdef ALLEGRO_WINDOWS
	FreeConsole();
	AllocConsole();
	#endif

	printf("\nDebug mode\n\n");

	while (!done) {
		while (go > 0) {
			disasm(pc);
			cpu_exec();
			go--;
			if (KBHIT()) {
				go=0;
				disasm(pc);
				show_reg();
				cpu_exec();

			}
		}
		printf("> ");
		fgets(inp,76,stdin);
		if ((strlen(inp)>0) && (inp[strlen(inp)-1]=='\n')) inp[strlen(inp)-1]=0;
		strlwr(inp);
		strcat(inp," \n");
		tok=strtok(inp," ");
		if (!tok) tok="";
		if (!strcmp(tok,"h") || !strcmp(tok,"?") || !strcmp(tok,"help")) {
			printf("display - show display\n");
			#ifdef ALLEGRO_DOS
			printf("cls - clear screen\n");
			#endif
			printf("clrkey - clear keypresses\n");
			printf("setkey n - set key n pressed\n");
			printf("s - step\n");
			printf("reg - display registers\n");
			printf("stack - display stack\n");
			printf("video - display VDC registers\n");
			printf("exram - display external RAM contents\n");
			printf("run # - run to address #\n");
			printf("runvb - run to VBL\n");
			printf("runnvb - run to no VBL\n");
			printf("go # - execute # instructions\n");
			printf("intram - display internal ram\n");
			printf("di # - disassemble memory #\n");
			printf("md # - display memory #\n");
			printf("wvdc a d - write data d to VDC address a\n");
			printf("col - display collision table\n");
			printf("stick1 # - set stick1 to #\n");
			printf("stick2 # - set stick2 to #\n");
			printf("sndlog [file] - log raw sound to file\n");
			printf("showfps - display the number of frames per second\n");
			printf("q - quit debugger and return to emulation\n");
			printf("\n");
		} else if (!strcmp(tok,"display")) {
			grmode();
			clip_low = 0;
			clip_high = 85000;
			draw_display();
			finish_display();
			init_keyboard();
			do {
				rest(1);
			} while((key_done==0) && (!keypressed()));
			set_textmode();
			set_display_switch_mode(SWITCH_BACKGROUND);
		} else if (!strcmp(tok,"cls")) {
			#ifdef ALLEGRO_DOS
			clrscr();
			#endif
		} else if (!strcmp(tok,"clrkey")) {
			for(i=0; i<128; i++) key2[i]=0;
		} else if (!strcmp(tok,"setkey")) {
			tok=strtok(NULL," ");
			if (tok){
				sscanf(tok,"%d",&i);
				if ((i>0) && (i<128)){
					printf("Key %d set to pressed\n",i);
					key2[i]=1;
				}
				key2vcnt=0;
			}
		} else if (!strcmp(tok,"stick1")) {
			tok=strtok(NULL," ");
			if (tok) {
				i=0;
				sscanf(tok,"%x",&i);
				printf("Stick 1 set to %d\n",i);
				dbstick1=i;
				key2vcnt=0;
			}
		} else if (!strcmp(tok,"stick2")) {
			tok=strtok(NULL," ");
			if (tok) {
				i=0;
				sscanf(tok,"%x",&i);
				printf("Stick 2 set to %d\n",i);
				dbstick2=i;
				key2vcnt=0;
			}
		} else if (!strcmp(tok,"s")) {
			disasm(pc);
			show_reg();
			cpu_exec();
		} else if (!strcmp(tok,"reg")) {
			show_reg();
		} else if (!strcmp(tok,"stack")) {
			for(i=8; i<24; i+=2) {
				ad = intRAM[i];
				d = intRAM[i+1];
				ad = ad | ((d & 0x0F) << 8);
				printf("%x: PC=%x PSW=%x",i,ad,d);
				if (i == sp) printf(" <<SP");
				printf("\n");
			}
			printf("\n");
		} else if (!strcmp(tok,"q")) {
			printf("\nReturning to emulation\n\n");
			done=1;			
		} else if (!strcmp(tok,"pvideo")) {
			j=0;
			fprintf(stderr,"%02x:",0);
			for(i=0; i<256; i++) {
				fprintf(stderr,"%02x,",VDCwrite[i]);
				j++;
				if (j == 16) {
					fprintf(stderr,"%s\n",cr);
					fprintf(stderr,"%02x:",i+1);
					j=0;
				}
			}
			fprintf(stderr,"%s\n",cr);
			fprintf(stderr,"%s",ff);
		} else if (!strcmp(tok,"video")) {
			j=0;
			printf("%02x:",0);
			for(i=0; i<256; i++) {
				printf("%02x",VDCwrite[i]);
				if (j < 15) printf(",");
				j++;
				if (j == 16 && i != 255) {
					printf("\n");
					printf("%02x:",i+1);
					j=0;
				}
			}
			printf("\n");
		} else if (!strcmp(tok,"keys")) {
			j=0;
			printf("%02x:",0);
			for(i=0; i<128; i++) {
				printf("%02x,",key2[i]);
				j++;
				if (j == 16) {
					printf("\n");
					printf("%02x:",i+1);

					j=0;
				}
			}
			printf("\n");
		} else if (!strcmp(tok,"col")) {
			j=0;
			printf("%02x:",0);
			for(i=0; i<256; i++) {
				printf("%02x,",coltab[i]);
				j++;
				if (j == 16) {
					printf("\n");
					printf("%02x:",i+1);
					j=0;
				}
			}
			printf("\n");
			printf("Colreg: %x\n ",ext_read(0xA2));
		} else if (!strcmp(tok,"exram")) {
			j=0;
			printf("%02x:",0);
			for(i=0; i<256; i++) {
				printf("%02x",extRAM[i]);
				if (j < 15) printf(",");
				j++;
				if (j == 16 && i !=255) {
					printf("\n");
					printf("%02x:",i+1);

					j=0;
				}
			}
			printf("\n\n");
		} else if (!strcmp(tok,"intram")) {
			j=0;
			printf("%02x:",0);
			for(i=0; i<64; i++) {
				printf("%02x",intRAM[i]);
				if (j < 15) printf(",");
				j++;
				if (j == 16 && i != 63) {
					printf("\n");
					printf("%02x:",i+1);
					j=0;
				}
			}
			printf("\n\n");
		} else if (!strcmp(tok,"run")) {
			tok=strtok(NULL," ");
			if (tok){
				sscanf(tok,"%hx",&run_to);
				printf("Run to %x\n",run_to);
				while (pc != run_to) {
					cpu_exec();
					if (KBHIT()) break;
				}
				disasm(pc);
				show_reg();
				cpu_exec();
			}
		} else if (!strcmp(tok,"runvb")) {
			printf("Run to VBL\n");
			while (master_clk < 5500) {
				cpu_exec();
				if (KBHIT()) break;
			}
			disasm(pc);
			show_reg();
			cpu_exec();
		} else if (!strcmp(tok,"runnvb")) {
			printf("Run to no VBL\n");
			while (master_clk > 5500) {
				cpu_exec();
				if (KBHIT()) break;
			}
			disasm(pc);
			show_reg();
			cpu_exec();
		} else if (!strcmp(tok,"wvdc")) {
			int t;
			tok=strtok(NULL," ");
			if (tok){
				sscanf(tok,"%x",&t);
				a = (Byte)t;
				tok=strtok(NULL," ");
				if (tok){
					sscanf(tok,"%x",&t);
					d = (Byte)t;
					VDCwrite[a] = d;
				}
			}
		} else if (!strcmp(tok,"go")) {
			tok=strtok(NULL," ");
			if (tok) sscanf(tok,"%d",&go);
		} else if (!strcmp(tok,"di")) {
			tok=strtok(NULL," ");
			if (tok){
				ad=0;
				sscanf(tok,"%hx",&ad);
				if (ad<5100) {
					for(i=0; i<20; i++) {
						ad = ad + disasm(ad);
					}
				}
				printf("\n");
			}
		} else if (!strcmp(tok,"md")) {
			tok=strtok(NULL," ");
			if (tok){
				sscanf(tok,"%hx",&ad);
				printf("\n");

				for (j=0; j<10; j++){
					if (ad+j*16<5100) {
						printf("%04x : ",ad+j*16);
						for (i=0; i<16; i++) printf("%02x ",rom[ad+j*16+i]);
						printf("\n");
					}
				}
				printf("\n\n");
			}
		} else if (!strcmp(tok,"sndlog")) {
			if (app_data.sound_en) {
				tok=strtok(NULL," ");
				if (tok){
					char file[80]="";
					sscanf(tok,"%79s",file);
					if (strlen(file)>0){
						sndlog = fopen(file,"wb");
						if (sndlog)
							printf("Sound log file created\n");
						else
							printf("Sound log file creation failed\n");
					}
				}
				printf("\n");
			} else printf("Sound emulation disabled\n\n");
		} else if (!strcmp(tok,"showfps")) {
			show_fps=1;
		} else if ((strlen(tok)>0) && (strcmp(tok,"\n"))) {
			printf("Unknown command\n\n");
		}

	}
	
	#ifdef ALLEGRO_WINDOWS
	FreeConsole();
	#endif

}


static void show_reg(void) {
	int i;

		make_psw_debug();
		printf("PC: %04x  A: %02x PSW: %02x P1: %02x  P2: %02x",pc,acc,psw,p1,p2);
		printf("  clk: %d  reg:%d  count:%x  f:%x\n",master_clk,reg_pnt,itimer,frame);
		for (i=0; i<8; i++) {
			printf("R%d: %02x   R%d': %02x\n",i,intRAM[i],i,intRAM[i+24]);
		}
}


static int disasm(ADDRESS p) {
	Byte op,d;
	ADDRESS adr;

	op=rom[p++];
	printf("%04x: %02x",p-1,op);
	if (lookup[op].bytes == 2) printf(",%02x",rom[p]);
	printf("  %s",lookup[op].mnemonic);
	switch(lookup[op].type) {
		case 0:
			printf("\n");
			break;
		case 1:
			d=rom[p];
			printf(" #%02x\n",d);
			break;
		case 2:
			adr=rom[p];
			adr = adr | ((op & 0xE0) << 3);
			printf(" $%03x\n",adr);
			break;
		case 3:
			printf(" $%02x\n",rom[p]);
			break;
	}
	return lookup[op].bytes;
}

