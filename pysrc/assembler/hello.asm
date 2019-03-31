.include hardware.asm

._CPU = Z80
.CONST_A = 0x20

0x8000:
Start:

   LD  A,0x23     ; A constant
   LD  B,(0x10)
   LD  H,(DataA)
   LD  E,CONST_A
   JP  Start

DataA:
. 0x10,0x20,0x30

DataB:
. 0x20
