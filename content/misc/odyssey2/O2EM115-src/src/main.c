
/*
 *   O2EM Free Odyssey2 / Videopac+ Emulator
 *
 *   Created by Daniel Boris <dboris@comcast.net>  (c) 1997,1998
 *
 *   Developed by Andre de la Rocha <adlroc@users.sourceforge.net>
 *
 *   http://o2em.sourceforge.net
 *
 */


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <time.h>
#include "crc32.h"
#include "audio.h"
#include "vmachine.h"
#include "config.h"
#include "vdc.h"
#include "cpu.h"
#include "debug.h"
#include "keyboard.h"
#include "voice.h"
#include "allegro.h"
#ifdef ALLEGRO_WINDOWS
#include "winalleg.h"
#endif


#define MAXC 1024


static char bios[MAXC], scshot[MAXC];


static long filesize(FILE *stream);
static void load_bios(const char *biosname);
static void load_cart(char *file);
int parse_option(char *attr, char *val);
void read_default_config(void);


int main(int argc, char *argv[]){
	int i;
	static char file[MAXC], attr[MAXC], val[MAXC], *p, *binver;

	#if defined(ALLEGRO_WINDOWS)
	binver = "Windows binary";
	#elif defined(ALLEGRO_DOS)
	binver = "DOS binary";
	#elif defined(ALLEGRO_LINUX)
	binver = "Linux binary";
	#elif defined(ALLEGRO_BEOS)
	binver = "BEOS binary";
	#elif defined(ALLEGRO_QNX)
	binver = "QNX binary";
	#elif defined(ALLEGRO_UNIX)
	binver = "UNIX binary";
	#elif defined(ALLEGRO_MPW)
	binver = "MacOS binary";
	#else
	binver = "Unknown binary";
	#endif

	printf("%s %s\n","\nO2EM v" O2EM_VERSION " " RELEASE_DATE "  - ", binver);
	printf("Free Odyssey2 / Videopac+ Emulator - http://o2em.sourceforge.net\n");
	printf("Developed by Andre de la Rocha\n");
	printf("Created by Daniel Boris (c)1996/1998\n");
	printf("\n");
	
	if (argc < 2) {
		printf("Use: o2em <file> [options]\n");
		printf("<file> = file to load with extension\n");
		#ifndef ALLEGRO_DOS
		printf("-wsize=n         Window size (1-4)\n");
		printf("-fullscreen      Full screen mode\n");
		#endif
		printf("-scanlines       Enable scanlines\n");
		printf("-nosound         Turn off sound emulation\n");
		printf("-novoice         Turn off voice emulation\n");
		printf("-svolume=n       Set sound volume (0-100)\n");
		printf("-vvolume=n       Set voice volume (0-100)\n");
		printf("-filter          Enable low-pass audio filter\n");
		printf("-debug	         Start the emulator in debug mode\n");
		printf("-speed=n         Relative speed (100 = original)\n");
		printf("-nolimit         Turn off speed limiter\n");
		printf("-bios=file       Set the O2 bios file name/dir (default=o2rom.bin)\n");
		printf("-scshot=file     Set the screenshot file name/template\n");
		printf("-euro            Use European timing / 50Hz mode\n");
		printf("-exrom           Use special 3K program/1K data ROM mode\n");
		printf("-3k              Use 3K rom mapping mode\n");
		printf("-s<n>=mode/keys  Define stick n mode/keys (n=1-2)\n");
		printf("\nPress Enter...");
		fflush(stdout);
		getchar();
		exit(EXIT_SUCCESS);
	}

	app_data.debug = 0;
	app_data.stick[0] = app_data.stick[1] = 1;
	set_defjoykeys(0,0);
	set_defjoykeys(1,1);
	app_data.bank = 0;
    app_data.limit = 1;
    app_data.sound_en = 1;
	app_data.speed = 100;
	app_data.wsize = 2;
	#ifdef ALLEGRO_DOS
	app_data.fullscreen = 1;
	#else
	app_data.fullscreen = 0;
	#endif
	app_data.scanlines = 0;
	app_data.voice = 1;
	app_data.window_title = "O2EM v" O2EM_VERSION;
	app_data.svolume = 100;
	app_data.vvolume = 100;
	app_data.filter = 0;
	app_data.exrom = 0;
	app_data.three_k = 0;
	app_data.crc = 0;
	app_data.scshot = scshot;
	app_data.euro = 0;
	app_data.openb = 0;

	strcpy(file,"");
	strcpy(bios,"");
	strcpy(scshot,"");

	read_default_config();

	for(i=1; i<argc; i++) {
		if (argv[i][0] != '-') 	{
			strncpy(file,argv[i],MAXC-1);
			file[MAXC-1]=0;
		} else {
			p=strtok(argv[i],"=");
			if (p){
				strncpy(attr,p+1,MAXC-1);
				attr[MAXC-1]=0;
			} else
				strcpy(attr,"");
			p=strtok(NULL,"=");
			if (p){
				strncpy(val,p,MAXC-1);
				val[MAXC-1]=0;
			} else
				strcpy(val,"");
			strlwr(attr);

			if (!parse_option(attr, val)) exit(EXIT_FAILURE);

		}
	}

	if (strlen(file)==0) {
		fprintf(stderr,"Error: file name missing\n");
		exit(EXIT_FAILURE);
	}

	printf("Starting emulation ...\n");

	allegro_init();
	install_timer();
    init_audio();
	printf("Using Allegro %s\n",allegro_id);
	load_bios(bios);
	load_cart(file);
	
	if (app_data.voice) load_voice_samples();

	init_display();
	init_cpu();
	init_system();
	if (app_data.debug) key_debug=1;
	#ifndef _DEBUG
	#ifdef ALLEGRO_WINDOWS
	FreeConsole();
	#endif
	#endif
	run();
	exit(EXIT_SUCCESS);
}

END_OF_MAIN();


int parse_option(char *attr, char *val){
	int t;

	if (!strcmp(attr,"nolimit")) {
		app_data.limit = !(val[0]!='0');
	} else if (!strcmp(attr,"nosound")) {
		app_data.sound_en = !(val[0]!='0');
	} else if (!strcmp(attr,"novoice")) {
		app_data.voice = !(val[0]!='0');
	} else if (!strcmp(attr,"filter")) {
		app_data.filter = (val[0]!='0');
	} else if (!strcmp(attr,"debug")) {
		app_data.debug = (val[0]!='0');
	} else if ((!strcmp(attr,"s1")) || (!strcmp(attr,"s2"))) {
		int sn;
		sn = (!strcmp(attr,"s1"))? 0 : 1;
		if (strlen(val)<2){
			t = -1;
			sscanf(val,"%d",&t);
			if ((t>=0) && (t<=3)) {
				if ((t==1)||(t==2)){
					app_data.stick[sn] = 1;
					set_defjoykeys(sn,t-1);
				} else {
					app_data.stick[sn] = (t==0) ? 0 : 2;
					set_joykeys(sn,0,0,0,0,0);
				}
			} else {
				fprintf(stderr,"Invalid value for option %s\n",attr);
				return 0;
			}
		} else {
			char *p,*s;
			int i,k,code,nk,codes[5];
			strupr(val);
			nk = 0;
			p = strtok(val,",");
			while (p) {
				i = code = 0;
				k = keybtab[i].keybcode;
				s = keybtab[i].keybname;
				while (k && (code==0)) {
					if (strcmp(s,p)==0) code = k;
					i++;
					k = keybtab[i].keybcode;
					s = keybtab[i].keybname;
				}
				if (!code) {
					fprintf(stderr,"Invalid value for option %s : key %s unknown\n",attr,p);
					return 0;
				}					
				codes[nk] = code;
				p = strtok(NULL,",");
				nk++;
				if (nk>5) {
					fprintf(stderr,"Invalid value for option %s : invalid number of keys\n",attr);
					return 0;
				}
			}
			if (nk != 5) {
				fprintf(stderr,"Invalid value for option %s : invalid number of keys\n",attr);
				return 0;
			}
			app_data.stick[sn] = 1;
			set_joykeys(sn,codes[0],codes[1],codes[2],codes[3],codes[4]);
		}
	} else if (!strcmp(attr,"speed")) {
		t = -1;
		sscanf(val,"%d",&t);
		if ((t>0) && (t<=10000))
			app_data.speed = t;
		else {
			fprintf(stderr,"Invalid value for option %s\n",attr);
			return 0;
		}
	} else if (!strcmp(attr,"svolume")) {
		t = -1;
		sscanf(val,"%d",&t);
		if ((t>=0) && (t<=100))
			app_data.svolume = t;
		else {
			fprintf(stderr,"Invalid value for option %s\n",attr);
			return 0;
		}
		if (t==0) app_data.sound_en=0;
	} else if (!strcmp(attr,"vvolume")) {
		t = -1;
		sscanf(val,"%d",&t);
		if ((t>=0) && (t<=100))
			app_data.vvolume = t;
		else {
			fprintf(stderr,"Invalid value for option %s\n",attr);
			return 0;
		}
		if (t==0) app_data.voice=0;
	} else if (!strcmp(attr,"wsize")) {
		t = -1;
		sscanf(val,"%d",&t);
		if ((t>0) && (t<5)) {
			app_data.wsize = t;
			app_data.fullscreen = 0;
		} else {
			fprintf(stderr,"Invalid value for option %s\n",attr);
			return 0;
		}
	} else if (!strcmp(attr,"fullscreen")) {
		app_data.fullscreen = (val[0]!='0');
	} else if (!strcmp(attr,"scanlines")) {
		app_data.scanlines = (val[0]!='0');
	} else if (!strcmp(attr,"scshot")) {
		strcpy(scshot,val);
	} else if (!strcmp(attr,"euro")) {
		app_data.euro = (val[0]!='0');
	} else if (!strcmp(attr,"exrom")) {
		app_data.exrom = (val[0]!='0');
	} else if (!strcmp(attr,"3k")) {
		app_data.three_k = (val[0]!='0');
	} else if (!strcmp(attr,"bios")) {
		strcpy(bios,val);
	} else {
		fprintf(stderr,"Invalid option : %s\n",attr);
		return 0;
	}
	return 1;
}


void read_default_config(void){
	FILE *f;
	static char attr[MAXC], val[MAXC], s[MAXC];
	char *p, *fn;
	int i,l;
	
	fn = "o2em_def.cfg";
	f = fopen(fn,"r");
	if (!f) {
		fn = "O2EM_DEF.CFG";
		f = fopen(fn,"r");
	}
	if (!f) return;

	l=0;
	while (fgets(s,MAXC-1,f)){
		l++;
		p=s;
		while (*p && (isspace(*p))) p++;
		if (*p && (*p != '#')) {
			i=0;
			while (*p && (!isspace(*p)) && (*p != '=')) attr[i++] = *p++;
			attr[i]=0;
			while (*p && (isspace(*p))) p++;
			i=0;
			if (*p == '='){
				p++;
				while (*p && (isspace(*p))) p++;
				if (*p == '"'){
					p++;
					while (*p && (*p != '"') && (*p != '\n') && (*p != '\r')) val[i++] = *p++;
				} else {
					while (*p && (!isspace(*p))) val[i++] = *p++;
				}
			}
			val[i]=0;
			if (strlen(attr)>0) {
				strlwr(attr);
				if (!parse_option(attr,val)) {
					printf("Error in the %s file at line number %d !\n\n",fn,l);
				}
			}
		}
	}
	fclose(f);
}


static long filesize(FILE *stream){
   long curpos, length;

   curpos = ftell(stream);
   fseek(stream, 0L, SEEK_END);
   length = ftell(stream);
   fseek(stream, curpos, SEEK_SET);
   return length;
}


static void load_bios(const char *biosname){
	FILE *fn;
	static char s[MAXC+10];
	unsigned long crc;
	int i;

	if ((!biosname) || (strlen(biosname)==0)) {
		strcpy(s,"o2rom.bin");
		fn = fopen("o2rom.bin","rb");
		if (!fn) fn = fopen("O2ROM.BIN","rb");
	} else if ((biosname[strlen(biosname)-1]=='/') || (biosname[strlen(biosname)-1]=='\\') || (biosname[strlen(biosname)-1]==':')) {
		strcpy(s,biosname);
		strcat(s,"O2ROM.BIN");
		fn = fopen(s,"rb");
		if (!fn) {
			strcpy(s,biosname);
			strcat(s,"o2rom.bin");
			fn = fopen(s,"rb");
		}
	} else {
		strcpy(s,biosname);
		fn = fopen(biosname,"rb");
	}

	if (!fn) {
		fprintf(stderr,"Error loading bios ROM (%s)\n",s);
		exit(EXIT_FAILURE);
	}
	
 	if (fread(rom_table[0],1024,1,fn) != 1) {
 		fprintf(stderr,"Error loading bios ROM o2rom.bin\n");
 		exit(EXIT_FAILURE);
 	}
	fclose(fn);

	for (i=1; i<8; i++) memcpy(rom_table[i],rom_table[0],1024);

	crc = crc32_buf(rom_table[0],1024);

	if (crc==0x8016A315)
		printf("Odyssey2 bios ROM loaded\n");
	else if (crc==0xE20A9F41)
		printf("Videopac+ G7400 bios ROM loaded\n");
	else if (crc==0xA318E8D6)
		printf("C52 bios ROM loaded\n");
	else if (crc==0x11647CA5)
		printf("Jopac bios ROM loaded\n");
	else
		printf("Bios ROM loaded (unknown version)\n");
}


static void load_cart(char *file){
	FILE *fn;
	long l;
	int i, nb;

	app_data.crc = crc32_file(file);

	if (app_data.crc == 0xAFB23F89) app_data.exrom = 1;  /* Musician */
	if (app_data.crc == 0x3BFEF56B) app_data.exrom = 1;  /* Four in 1 Row! */
	if (app_data.crc == 0x9B5E9356) app_data.exrom = 1;  /* Four in 1 Row! (french) */

	if ((app_data.crc == 0x4E2CC6D3) || (app_data.crc == 0xBCF1EFC9)) app_data.three_k = 1;  /* Kill the Attacking Aliens */

	if (((app_data.crc == 0x975AB8DA) || (app_data.crc == 0xE246A812)) && (!app_data.debug)) {
		fprintf(stderr,"Error: file %s is an incomplete ROM dump\n",file);
		exit(EXIT_FAILURE);
	}
	
	fn=fopen(file,"rb");
	if (!fn) {
		fprintf(stderr,"Error loading %s\n",file);
		exit(EXIT_FAILURE);
	}
	printf("Loading: \"%s\"  Size: ",file);
	l = filesize(fn);

	if ((l % 1024) != 0) {
		fprintf(stderr,"Error: file %s is an invalid ROM dump\n",file);
		exit(EXIT_FAILURE);
	}

	if (((l % 3072) == 0) && app_data.three_k) {

		nb = l/3072;

		for (i=nb-1; i>=0; i--) {
			if (fread(&rom_table[i][1024],3072,1,fn) != 1) {
				fprintf(stderr,"Error loading %s\n",file);
				exit(EXIT_FAILURE);
			}
		}
		printf("%dK",nb*2);

	} else {

		nb = l/2048;

		if ((nb == 2) && (app_data.exrom)) {

			if (fread(&extROM[0], 1024,1,fn) != 1) {
				fprintf(stderr,"Error loading %s\n",file);
				exit(EXIT_FAILURE);
			}
			if (fread(&rom_table[0][1024],3072,1,fn) != 1) {
				fprintf(stderr,"Error loading %s\n",file);
				exit(EXIT_FAILURE);
			}
			printf("3K EXROM");

		} else {

			for (i=nb-1; i>=0; i--) {
				if (fread(&rom_table[i][1024],2048,1,fn) != 1) {
					fprintf(stderr,"Error loading %s\n",file);
					exit(EXIT_FAILURE);
				}
				memcpy(&rom_table[i][3072],&rom_table[i][2048],1024); /* simulate missing A10 */
			}
			printf("%dK",nb*2);

		}
	}
	fclose(fn);

	rom = rom_table[0];

	if (nb==1)
			app_data.bank = 1;
	else if (nb==2)
		app_data.bank = app_data.exrom ? 1 : 2;
	else if (nb==4)
		app_data.bank = 3;
	else 
		app_data.bank = 4;

	if ((rom_table[nb-1][1024+12]=='O') && (rom_table[nb-1][1024+13]=='P') && (rom_table[nb-1][1024+14]=='N') && (rom_table[nb-1][1024+15]=='B')) app_data.openb=1;

	printf("  CRC: %08lX\n",app_data.crc);
	
}


