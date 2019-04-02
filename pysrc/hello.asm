.include hardware.asm

._CPU = Z80
.CONST_A = 0x20

0x8000:
Start:

   LD  A  , CONST_A + 0x23     ; A constant
   LD  A,(0x10)
   LD  HL, ( Da taA  )
   LD  E,CONST_A
   JP  Start

DataA:
. 0x10,0x20,0x30

DataB:
. 0x20
