
/*
 *   O2/8048 disassembler
 */


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "types.h"
#include "table.h"

#define BIOSLEN 1024
#define MAXLEN 8192


Byte rom[MAXLEN+BIOSLEN];


int disasm (ADDRESS p) {
	Byte op,d;
	ADDRESS adr;
	Byte nb;

	op=rom[p++];
	printf("%04x:",p-1);
	printf("  %s",lookup[op].mnemonic);
	nb = lookup[op].bytes;
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
	if (op == 0x83 || op == 0x93) printf("\n");
	return nb;
}


int main(int argc, char **argv){
	int n;
	long len;
	FILE *fn;
	ADDRESS pc;

	if (argc<2) {
		printf("Usage: dis48 [file]\n");
		exit(0);
	}

	/* load image */

	fn=fopen(argv[1],"rb");
	if (!fn) {
		printf("Error loading %s\n",argv[1]);
		exit(0);
	}
	fseek(fn, 0L, SEEK_END);
	len=ftell(fn);
	
	if (len>MAXLEN) {
		printf("Invalid image size");
		fclose(fn);
		exit(0);
	}
	
	rewind(fn);
	if (fread(&rom[BIOSLEN],1,len,fn) != (size_t)len) {
		printf("Error loading %s\n",argv[1]);
		fclose(fn);
		exit(0);
	}
	fclose(fn);

	pc = BIOSLEN;
	while (pc < BIOSLEN+len) {
		n = disasm(pc);
		pc = pc + n;
	}
	exit(0);
}

