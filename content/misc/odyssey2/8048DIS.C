/*
    8048/8049 Disassembler for the PC.
		Written in Turbo 'C' by:
		Kirk Lanctot
		4511 E. Wood St.
		Phoenix,AZ 85040
*/

#include <stdio.h>
#include <dos.h>
#include <dir.h>
#include <fcntl.h>
#include <stat.h>
char *menom_array[256] =
{
     "NOP","X","OUTL BUS,A","ADD A,","JMP 0","EN I","X","DEC A",
     "INS A,BUS","IN A,P1","IN A,P2","X","MOVD A,P4","MOVD A,P5",
     "MOVD A,P6","MOVD A,P7",
     "INC @ R0","INC @ R1","JB0,","ADDC A,","CALL 0","DIS I","JTF ","INC A",
     "INC R0","INC R1","INC R2","INC R3","INC R4","INC R5","INC R6","INC R7",
     "XCHA,@ R0","XCHA,@ R1","X","MOV A,","JMP 1","EN TCNTI","JNT0,","CLR A",
     "XCH A,R0","XCH A,R1","XCH A,R2","XCH A,R3","XCH A,R4","XCH A,R5","XCH A,R6","XCH A,R7",
     "XCHD A,@ R0","XCHD A,@ R1","JB1,","X","CALL 1","DIS TCNTI","JT0,","CPL A",
     "X","OUTL P1,A","OUTL P2,A","X","MOVD P4,A","MOVD P5,A","MOVD P6,A","MOVD P7,A",
     "ORL A,@ R0","ORL A,@ R1","MOV A,T","ORL A,","JMP 2","STRT CNT","JNT1,","SWAP A",
     "ORL A,R0","ORL A,R1","ORL A,R2","ORL A,R3","ORL A,R4","ORL A,R5","ORL A,R6","ORL A,R7",
     "ANL A,@ R0","ANL A,@ R1","JB2,","ANL A,","CALL 2","STRT T","JT1,","DAA A",
     "ANL A,R0","ANL A,R1","ANL A,R2","ANL A,R3","ANL A,R4","ANL A,R5","ANL A,R6","ANL A,R7",
     "ADD A,@ R0","ADD A,@ R1","MOV T,A","X","JMP 3","STOP TCNT","X","RRC A",
     "ADD A,R0","ADD A,R1","ADD A,R2","ADD A,R3","ADD A,R4","ADD A,R5","ADD A,R6","ADD A,R7",
     "ADC A,@ R0","ADC A,@ R1","JB3,","X","CALL 3","ENTO CLK","JF1,","RR A",
     "ADC A,R0","ADC A,R1","ADC A,R2","ADC A,R3","ADC A,R4","ADC A,R5","ADC A,R6","ADC A,R7",
     "MOVX A,@ R0","MOVX A,@ R1","X","RET","JMP 4","CLR F0","JNI,","X",
     "ORL BUS,","ORL P1,","ORL P2,","X","ORLD P4,A","ORLD P5,A","ORLD P6,A","ORLD P7,A",
     "MOVX @ R0,A","MOVX @ R1,A","JB4,","RETR","CALL 4","CPL F0","JNZ,","CLR C",
     "X","ANL P1,","ANL P2,","X","ANLD P4,A","ANLD P5,A","ANLD P6,A","ANLD P7,A",
     "MOV @ R0,A","MOV @ R1,A","X","MOVP A,@ A","JMP 5","CLR F1","X","CPL C",
     "MOV R0,A","MOV R1,A","MOV R2,A","MOV R3,A","MOV R4,A","MOV R5,A","MOV R6,A","MOV R7,A",
     "MOV @ R0,","MOV @ R1,","JB5 ","JMPP @ A","CALL 5","CPL F1","JF0 ","X",
     "MOV R0,","MOV R1,","MOV R2,","MOV R3,","MOV R4,","MOV R5,","MOV R6,","MOV R7,",
     "X","X","X","X","JMP 6","SEL RB0","JZ ","MOV A,PSW",
     "DEC R0","DEC R1","DEC R2","DEC R3","DEC R4","DEC R5","DEC R6","DEC R7",
     "XRL A,@ R0","XRL A,@ R1","JB6 ","XRL A,","CALL 6","SEL RB1","X","MOV PSW,A",
     "XRL A,R0","XRL A,R1","XRL A,R2","XRL A,R3","XRL A,R4","XRL A,R5","XRL A,R6","XRL A,R7",
     "X","X","X","MOVP3 A,@ A","JMP 7","SEL MB0","JNC ","RL A",
     "DJNZ R0 ","DJNZ R1 ","DJNZ R2 ","DJNZ R3 ","DJNZ R4 ","DJNZ R5 ","DJNZ R6 ","DJNZ R7 ",
     "MOV A,@ R0","MOV A,@ R1","JB7 ","X","CALL 7","SEL MB1","JC ","RLC A",
     "MOV A,R0","MOV A,R1","MOV A,R2","MOV A,R3","MOV A,R4","MOV A,R5","MOV A,R6","MOV A,R7"
};

int count_array[256] =
{
     0,2,0,1,1,0,2,0,0,0,0,2,0,0,0,0,
     0,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,
     0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,
     0,0,1,2,1,0,1,0,2,0,0,2,0,0,0,0,
     0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,
     0,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,
     0,0,0,2,1,0,2,0,0,0,0,0,0,0,0,0,
     0,0,1,2,1,0,1,0,0,0,0,0,0,0,0,0,
     0,0,2,0,1,0,1,2,1,1,1,2,0,0,0,0,
     0,0,1,0,1,0,1,0,2,1,1,2,0,0,0,0,
     0,0,2,0,1,0,2,0,0,0,0,0,0,0,0,0,
     1,1,1,0,1,0,1,2,1,1,1,1,1,1,1,1,
     2,2,2,2,1,0,1,0,0,0,0,0,0,0,0,0,
     0,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,
     2,2,2,0,1,0,1,0,1,1,1,1,1,1,1,1,
     0,0,1,2,1,0,1,0,0,0,0,0,0,0,0,0
     };

int repeat,ok_value,read_byte,count_val,read_byte2;
int found,status,handle,offset,offsetread,startoff,endoff;
char response,filename[32],filename_out[32];
FILE *input_file,*output_file,*dummy_file;
union REGS REG;

/* start of main program */

main()
{
repeat=1;
while (repeat==1)
  {
  cls();
  gotoxy(0,0);
  directory("*.B48");
  printf("\n");
  open_file_input();
  printf("\n");
  directory("*.DIS");
  printf("\n");
  open_file_output();
  get_offset();
  process_line();
  dump_file();
  printf("\n");
  printf(" Type E to exit or Return to restart  ");
  if ((response=toupper(getche()))=='E')
    repeat=0;
  }
  fcloseall();
}
/* end of main program */

open_file_input()
		{
		found=0;
		while (found==0)
			{
				printf("Enter file name to disassemble \n");
				scanf("%s",filename);
        handle=open(filename,O_RDONLY|O_BINARY|O_DENYALL);
				input_file=fdopen(handle,"rb");
        if (input_file==NULL)
		      {
         	printf("failed to find file - try again \n");
					}
				else
				{
          printf("file found - please wait \n");
          found=1;
        }
		  }
    }

open_file_output()
		{
		found=0;
		while (found==0)
			  {
		    printf("Enter destination file name \n");
		    scanf("%s",filename_out);
        handle=creat(filename_out,O_CREAT|O_TEXT|S_IWRITE);
			  output_file=fdopen(handle,"wt");
				if (output_file==NULL)
		       printf("failed to open file - try again \n");
				else
           {
           printf("file opened - please wait \n");
           found=1;
           }
		    } /* end of found==1 */
    } /* end of open_file_output */

get_offset()
  {
  startoff=0x0;
  endoff=0x0;
  ok_value=0;
  while (ok_value==0)
  	{
  	printf("\n");
    printf("Enter starting offset (0-7fff)  ");
    scanf("%4x",&startoff);
    printf("Enter ending offset (0-7fff)    ");
    scanf("%4x",&endoff);
    if (startoff>=0 && endoff<=0x7fff && endoff>=startoff)
    ok_value=1;
    }
  }

process_line()
{
pout_eol();
fprintf(output_file,"DISASSEMBLY LISTING OF ");
fprintf(output_file,"%s",filename);
pout_eol();
pout_eol();
status=fseek(input_file,startoff,SEEK_SET);
for (offsetread=startoff;offsetread<=endoff;offsetread++)
  {
  read_byte=getc(input_file);
  count_val=count_array[read_byte];

   if (count_val== 0)
   	   {
   	   pout_address(offsetread);
   	   pout_byte(read_byte);
   	   pout_space();
   	   pout_menomic(read_byte);
			 pout_eol();	
   	   };
   if (count_val== 1)
   	   {
   	   pout_address(offsetread);
   	   pout_byte(read_byte);
       read_byte2=getc(input_file);
       pout_byte(read_byte2);
       pout_menomic(read_byte);
	     pout_bytetail(read_byte2);
   	   offsetread++;
       pout_eol();
   	   };
   if (count_val == 2)
       {
   	   pout_address(offsetread);
   	   pout_byte(read_byte);
   	   pout_space();
   	   pout_illeg_menom();
       pout_eol();
   	   };
  }
}  /* end of process_line */

/* functions */

cls()         /* Clear the screen  */
   {
   REG.x.ax = 0x0600;
   REG.h.bh = 0x07;
   REG.x.cx = 0X0000;
   REG.x.dx = 0x184f;
   int86(0x10, &REG, &REG);
   }

gotoxy(x, y)   /* position cursor at x,y  0,0 being upper left */
int x, y;
{
    union REGS REG;

    REG.h.ah = 02;
    REG.h.bh = 0; /* Get current page */
    REG.h.dh = x;
    REG.h.dl = y;
    int86(0x10, &REG, &REG);
}

directory(char *sear)
   {
   struct ffblk ffblk;
   int done;
   printf("Directory of files \n");
   done=findfirst(sear,&ffblk,0);
   while (!done)
      {
      printf("  %s\n", ffblk.ff_name);
      done=findnext(&ffblk);
      }
   pout_eol();
   }


pout_address(addr)
   {
   fprintf(output_file,"%.4X:  ",addr);
   }
pout_menomic(opcode)
   {
   fprintf(output_file,"%s",menom_array[opcode]);
   }
pout_space()
   {
   fprintf(output_file,"    ");
   }
pout_byte(code)
   {
   fprintf(output_file,"%.2X  ",code);
   }
pout_byte2(code)
   {
   fprintf(output_file,"%.2X",code);
   }
pout_bytetail(code)
   {
   fprintf(output_file,"%-.2X",code);
   }
pout_illeg_menom()
   {
   fprintf(output_file,"*** ILLEGAL *** ");
   }
pout_eol()
   {
   fprintf(output_file,"\n");
   }

dump_file()
   {
   pout_eol();
   pout_eol();
   printf("Starting Hex Dump Listing\n");
   fprintf(output_file,"Hex Dump Listing\n");
   get_offset();
   status=fseek(input_file,startoff,SEEK_SET);
   for(offsetread=startoff;offsetread<=endoff;offsetread++)
      {
      pout_address(offsetread);
      offsetread=offsetread+15;
      for(count_val=0;count_val<16 || !eof(input_file);count_val++)
        {
        if (count_val % 4 == 0 && count_val != 0)
           fprintf(output_file," - ");
        else
           fprintf(output_file," ");
        read_byte=getc(input_file);
        pout_byte2(read_byte);
        }
      pout_eol();
      }
   }
