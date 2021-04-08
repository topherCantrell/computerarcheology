![Burger Time](A2600BT.jpg)

# Burger Time Bank 7

>>> cpu 6502

>>> memoryTable hard 
[Hardware Info](../Stella.md)

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

```code
; Bank 7 (Fixed bank)

; A 256-byte block of RAM maps to this 512-byte memory
; space. The first 256 bytes is where you write. The
; second 256 bytes is where you read.
;
; You select one of 4 256-byte blocks to map here by
; accessing FFE8, FFE9, FFEA, FFEB
F800: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F810: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F820: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F830: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F840: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F850: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F860: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F870: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F880: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F890: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F8A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F8B0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F8C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F8D0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F8E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F8F0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

F900: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F910: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F920: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F930: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F940: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F950: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F960: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F970: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F980: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F990: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F9A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F9B0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F9C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F9D0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F9E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F9F0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

FA00: 00              BRK                         
FA01: 00              BRK                         
FA02: 00              BRK                         
FA03: 00              BRK                         
FA04: 00              BRK                         
FA05: 00              BRK                         
FA06: 00              BRK                         
FA07: 00              BRK                         
FA08: 00              BRK                         
FA09: 00              BRK                         
FA0A: 00              BRK                         
FA0B: 00              BRK                         
FA0C: 00              BRK                         
FA0D: 00              BRK                         
FA0E: 00              BRK                         
FA0F: 00              BRK                         
FA10: 00              BRK                         
FA11: 00              BRK                         
FA12: 00              BRK                         
FA13: 00              BRK                         
FA14: 00              BRK                         
FA15: 00              BRK                         
FA16: 00              BRK                         
FA17: 00              BRK                         
FA18: 00              BRK                         
FA19: 00              BRK                         
FA1A: 00              BRK                         
FA1B: 00              BRK                         
FA1C: 00              BRK                         
FA1D: 00              BRK                         
FA1E: 00              BRK                         
FA1F: 00              BRK                         
FA20: 00              BRK                         
FA21: 00              BRK                         
FA22: 00              BRK                         
FA23: 00              BRK                         
FA24: 00              BRK                         
FA25: 00              BRK                         
FA26: 00              BRK                         
FA27: 00              BRK                         
FA28: 00              BRK                         
FA29: 00              BRK                         
FA2A: 00              BRK                         
FA2B: 00              BRK                         
FA2C: 00              BRK                         
FA2D: 00              BRK                         
FA2E: 00              BRK                         
FA2F: 00              BRK                         
FA30: 00              BRK                         
FA31: 00              BRK                         
FA32: 00              BRK                         
FA33: 00              BRK                         
FA34: 00              BRK                         
FA35: 00              BRK                         
FA36: 00              BRK                         
FA37: 00              BRK                         
FA38: 00              BRK                         
FA39: 00              BRK                         
FA3A: 00              BRK                         
FA3B: 00              BRK                         
FA3C: 00              BRK                         
FA3D: 00              BRK                         
FA3E: 00              BRK                         
FA3F: 00              BRK                         
FA40: 00              BRK                         
FA41: 00              BRK                         
FA42: 00              BRK                         
FA43: 00              BRK                         
FA44: 00              BRK                         
FA45: 00              BRK                         
FA46: 00              BRK                         
FA47: 00              BRK                         
FA48: 00              BRK                         
FA49: 00              BRK                         
FA4A: 00              BRK                         
FA4B: 00              BRK                         
FA4C: 00              BRK                         
FA4D: 00              BRK                         
FA4E: 00              BRK                         
FA4F: 00              BRK                         
FA50: 00              BRK                         
FA51: 00              BRK                         
FA52: 00              BRK                         
FA53: 00              BRK                         
FA54: 00              BRK                         
FA55: 00              BRK                         
FA56: 00              BRK                         
FA57: 00              BRK                         
FA58: 00              BRK                         
FA59: 00              BRK                         
FA5A: 00              BRK                         
FA5B: 00              BRK                         
FA5C: 00              BRK                         
FA5D: 00              BRK                         
FA5E: 00              BRK                         
FA5F: 00              BRK                         
FA60: 00              BRK                         
FA61: 00              BRK                         
FA62: 00              BRK                         
FA63: 00              BRK                         
FA64: 00              BRK                         
FA65: 00              BRK                         
FA66: 00              BRK                         
FA67: 00              BRK                         
FA68: 00              BRK                         
FA69: 00              BRK                         
FA6A: 00              BRK                         
FA6B: 00              BRK                         
FA6C: 00              BRK                         
FA6D: 00              BRK                         
FA6E: 00              BRK                         
FA6F: 00              BRK                         
FA70: 00              BRK                         
FA71: 00              BRK                         
FA72: 00              BRK                         
FA73: 00              BRK                         
FA74: 00              BRK                         
FA75: 00              BRK                         
FA76: 00              BRK                         
FA77: 22 ; ????
FA78: 22 ; ????
FA79: 22 ; ????
FA7A: 22 ; ????
FA7B: 22 ; ????
FA7C: 22 ; ????
FA7D: 22 ; ????
FA7E: 22 ; ????
FA7F: 22 ; ????
FA80: 22 ; ????
FA81: 62 ; ????
FA82: 62 ; ????
FA83: 62 ; ????
FA84: 62 ; ????
FA85: E0 E0           CPX     #$E0                  
FA87: E0 E0           CPX     #$E0                  
FA89: 00              BRK                         
FA8A: 00              BRK                         
FA8B: 00              BRK                         
FA8C: 00              BRK                         
FA8D: 00              BRK                         
FA8E: 00              BRK                         
FA8F: 00              BRK                         
FA90: 00              BRK                         
FA91: 00              BRK                         
FA92: 00              BRK                         
FA93: 00              BRK                         
FA94: 00              BRK                         
FA95: 00              BRK                         
FA96: 00              BRK                         
FA97: 00              BRK                         
FA98: 00              BRK                         
FA99: 00              BRK                         
FA9A: 00              BRK                         
FA9B: 00              BRK                         
FA9C: 00              BRK                         
FA9D: 00              BRK                         
FA9E: 00              BRK                         
FA9F: 00              BRK                         
FAA0: 00              BRK                         
FAA1: 00              BRK                         
FAA2: 00              BRK                         
FAA3: 00              BRK                         
FAA4: 00              BRK                         
FAA5: 00              BRK                         
FAA6: 00              BRK                         
FAA7: 00              BRK                         
FAA8: 00              BRK                         
FAA9: 00              BRK                         
FAAA: 00              BRK                         
FAAB: 00              BRK                         
FAAC: 00              BRK                         
FAAD: 00              BRK                         
FAAE: 00              BRK                         
FAAF: 00              BRK                         
FAB0: 00              BRK                         
FAB1: 00              BRK                         
FAB2: 00              BRK                         
FAB3: 00              BRK                         
FAB4: 00              BRK                         
FAB5: 00              BRK                         
FAB6: 00              BRK                         
FAB7: 00              BRK                         
FAB8: 00              BRK                         
FAB9: 00              BRK                         
FABA: 00              BRK                         
FABB: 00              BRK                         
FABC: 00              BRK                         
FABD: 00              BRK                         
FABE: 00              BRK                         
FABF: 00              BRK                         
FAC0: 00              BRK                         
FAC1: 00              BRK                         
FAC2: 00              BRK                         
FAC3: 00              BRK                         
FAC4: 00              BRK                         
FAC5: 00              BRK                         
FAC6: 00              BRK                         
FAC7: 00              BRK                         
FAC8: 00              BRK                         
FAC9: 00              BRK                         
FACA: 00              BRK                         
FACB: 00              BRK                         
FACC: 00              BRK                         
FACD: 00              BRK                         
FACE: 00              BRK                         
FACF: 00              BRK                         
FAD0: 00              BRK                         
FAD1: 00              BRK                         
FAD2: 00              BRK                         
FAD3: 00              BRK                         
FAD4: 00              BRK                         
FAD5: 00              BRK                         
FAD6: 00              BRK                         
FAD7: 00              BRK                         
FAD8: 00              BRK                         
FAD9: 00              BRK                         
FADA: 00              BRK                         
FADB: 00              BRK                         
FADC: 00              BRK                         
FADD: 00              BRK                         
FADE: 00              BRK                         
FADF: 00              BRK                         
FAE0: 00              BRK                         
FAE1: 00              BRK                         
FAE2: 00              BRK                         
FAE3: 00              BRK                         
FAE4: 00              BRK                         
FAE5: 00              BRK                         
FAE6: 00              BRK                         
FAE7: 00              BRK                         
FAE8: 00              BRK                         
FAE9: 00              BRK                         
FAEA: 00              BRK                         
FAEB: 00              BRK                         
FAEC: 00              BRK                         
FAED: 00              BRK                         
FAEE: 00              BRK                         
FAEF: 00              BRK                         
FAF0: 00              BRK                         
FAF1: 00              BRK                         
FAF2: 00              BRK                         
FAF3: 00              BRK                         
FAF4: 00              BRK                         
FAF5: 00              BRK                         
FAF6: 00              BRK                         
FAF7: 00              BRK                         
FAF8: 00              BRK                         
FAF9: 00              BRK                         
FAFA: 00              BRK                         
FAFB: 00              BRK                         
FAFC: 00              BRK                         
FAFD: 00              BRK                         
FAFE: 00              BRK                         
FAFF: 00              BRK                         
FB00: 00              BRK                         
FB01: F0 F0           BEQ     $FAF3                   
FB03: F0 C0           BEQ     $FAC5                   
FB05: 00              BRK                         
FB06: 00              BRK                         
FB07: 00              BRK                         
FB08: 80 ; ????
FB09: 00              BRK                         
FB0A: 00              BRK                         
FB0B: 00              BRK                         
FB0C: 00              BRK                         
FB0D: 80 ; ????
FB0E: 00              BRK                         
FB0F: 00              BRK                         
FB10: 00              BRK                         
FB11: 00              BRK                         
FB12: 80 ; ????
FB13: 00              BRK                         
FB14: 00              BRK                         
FB15: 00              BRK                         
FB16: 00              BRK                         
FB17: 80 ; ????
FB18: 00              BRK                         
FB19: 00              BRK                         
FB1A: F0 00           BEQ     $FB1C                   
FB1C: F0 00           BEQ     $FB1E                   
FB1E: 00              BRK                         
FB1F: 60              RTS                         
FB20: 00              BRK                         
FB21: 80 ; ????
FB22: 00              BRK                         
FB23: 00              BRK                         
FB24: 60              RTS                         
FB25: F0 80           BEQ     $FAA7                   
FB27: 00              BRK                         
FB28: 00              BRK                         
FB29: 60              RTS                         
FB2A: 60              RTS                         
FB2B: 80 ; ????
FB2C: 00              BRK                         
FB2D: F0 60           BEQ     $FB8F                   
FB2F: 60              RTS                         
FB30: 80 ; ????
FB31: F0 C0           BEQ     $FAF3                   
FB33: F0 60           BEQ     $FB95                   
FB35: E0 60           CPX     #$60                  
FB37: C0 00           CPY     #$00                  
FB39: 60              RTS                         
FB3A: 00              BRK                         
FB3B: 60              RTS                         
FB3C: C0 00           CPY     #$00                  
FB3E: 60              RTS                         
FB3F: 00              BRK                         
FB40: 60              RTS                         
FB41: F0 00           BEQ     $FB43                   
FB43: 60              RTS                         
FB44: 00              BRK                         
FB45: F0 C0           BEQ     $FB07                   
FB47: 00              BRK                         
FB48: F0 00           BEQ     $FB4A                   
FB4A: 60              RTS                         
FB4B: C0 F0           CPY     #$F0                  
FB4D: 00              BRK                         
FB4E: 00              BRK                         
FB4F: 60              RTS                         
FB50: C0 60           CPY     #$60                  
FB52: 00              BRK                         
FB53: E0 60           CPX     #$60                  
FB55: F0 60           BEQ     $FBB7                   
FB57: 00              BRK                         
FB58: 80 ; ????
FB59: F0 C0           BEQ     $FB1B                   
FB5B: 60              RTS                         
FB5C: 00              BRK                         
FB5D: 80 ; ????
FB5E: 60              RTS                         
FB5F: C0 60           CPY     #$60                  
FB61: 00              BRK                         
FB62: 80 ; ????
FB63: 60              RTS                         
FB64: C0 60           CPY     #$60                  
FB66: 00              BRK                         
FB67: 80 ; ????
FB68: 60              RTS                         
FB69: F0 F0           BEQ     $FB5B                   
FB6B: F0 F0           BEQ     $FB5D                   
FB6D: F0 00           BEQ     $FB6F                   
FB6F: 00              BRK                         
FB70: 00              BRK                         
FB71: 00              BRK                         
FB72: 00              BRK                         
FB73: 00              BRK                         
FB74: 00              BRK                         
FB75: 00              BRK                         
FB76: 00              BRK                         
FB77: 00              BRK                         
FB78: 00              BRK                         
FB79: 00              BRK                         
FB7A: 00              BRK                         
FB7B: 00              BRK                         
FB7C: 00              BRK                         
FB7D: 00              BRK                         
FB7E: 00              BRK                         
FB7F: 00              BRK                         
FB80: 00              BRK                         
FB81: FF ; ????
FB82: FF ; ????
FB83: FF ; ????
FB84: FF ; ????
FB85: 00              BRK                         
FB86: C3 ; ????
FB87: 06 80           ASL     $80                   
FB89: 19 00 C3        ORA     $C300,Y                 
FB8C: 06 80           ASL     $80                   
FB8E: 19 00 C3        ORA     $C300,Y                 
FB91: 1F ; ????
FB92: 80 ; ????
FB93: 19 00 C3        ORA     $C300,Y                 
FB96: 06 80           ASL     $80                   
FB98: 1B ; ????
FB99: 00              BRK                         
FB9A: FF ; ????
FB9B: 06 FF           ASL     $FF                   
FB9D: 18              CLC                         
FB9E: 00              BRK                         
FB9F: 18              CLC                         
FBA0: 06 99           ASL     $99                   
FBA2: 18              CLC                         
FBA3: 00              BRK                         
FBA4: 18              CLC                         
FBA5: FF ; ????
FBA6: 99 18 00        STA     $0018,Y                 
FBA9: 18              CLC                         
FBAA: 06 99           ASL     $99                   
FBAC: 18              CLC                         
FBAD: FF ; ????
FBAE: 18              CLC                         
FBAF: 06 99           ASL     $99                   
FBB1: FF ; ????
FBB2: 19 FF 1F        ORA     $1FFF,Y                 
FBB5: FF ; ????
FBB6: 01 19           ORA     ($19,X)               
FBB8: C3 ; ????
FBB9: 00              BRK                         
FBBA: 19 01 19        ORA     $1901,Y                 
FBBD: C3 ; ????
FBBE: 00              BRK                         
FBBF: 19 01 FF        ORA     $FF01,Y                 
FBC2: C3 ; ????
FBC3: 00              BRK                         
FBC4: 3F ; ????
FBC5: FF ; ????
FBC6: 19 C3 FF        ORA     $FFC3,Y                 
FBC9: 19 01 19        ORA     $1901,Y                 
FBCC: FF ; ????
FBCD: 06 19           ASL     $19                   
FBCF: 01 19           ORA     ($19,X)               
FBD1: 18              CLC                         
FBD2: 06 FF           ASL     $FF                   
FBD4: 01 FF           ORA     ($FF,X)               
FBD6: 18              CLC                         
FBD7: 1F ; ????
FBD8: 81 FF           STA     ($FF,X)               
FBDA: 19 18 06        ORA     $0618,Y                 
FBDD: 81 01           STA     ($01,X)               
FBDF: 19 18 06        ORA     $0618,Y                 
FBE2: 81 01           STA     ($01,X)               
FBE4: 19 18 06        ORA     $0618,Y                 
FBE7: 81 01           STA     ($01,X)               
FBE9: FF ; ????
FBEA: FF ; ????
FBEB: FF ; ????
FBEC: FF ; ????
FBED: FF ; ????
FBEE: 00              BRK                         
FBEF: 00              BRK                         
FBF0: 00              BRK                         
FBF1: 00              BRK                         
FBF2: 00              BRK                         
FBF3: 00              BRK                         
FBF4: 00              BRK                         
FBF5: 00              BRK                         
FBF6: 00              BRK                         
FBF7: 00              BRK                         
FBF8: 00              BRK                         
FBF9: 00              BRK                         
FBFA: 00              BRK                         
FBFB: 00              BRK                         
FBFC: 00              BRK                         
FBFD: 00              BRK                         
FBFE: 00              BRK                         
FBFF: 00              BRK                         
FC00: C0 FF           CPY     #$FF                  
FC02: 00              BRK                         
FC03: FF ; ????
FC04: FF ; ????
FC05: 80 ; ????
FC06: 30 00           BMI     $FC08                   
FC08: 18              CLC                         
FC09: 81 80           STA     ($80,X)               
FC0B: 30 00           BMI     $FC0D                   
FC0D: 18              CLC                         
FC0E: 81 80           STA     ($80,X)               
FC10: 30 FF           BMI     $FC11                   
FC12: 18              CLC                         
FC13: 81 80           STA     ($80,X)               
FC15: 30 18           BMI     $FC2F                   
FC17: 18              CLC                         
FC18: FF ; ????
FC19: FC ; ????
FC1A: FF ; ????
FC1B: 18              CLC                         
FC1C: FF ; ????
FC1D: 00              BRK                         
FC1E: 98              TYA                         
FC1F: 06 18           ASL     $18                   
FC21: 01 00           ORA     ($00,X)               
FC23: 98              TYA                         
FC24: 06 18           ASL     $18                   
FC26: 01 00           ORA     ($00,X)               
FC28: 98              TYA                         
FC29: 06 18           ASL     $18                   
FC2B: 01 00           ORA     ($00,X)               
FC2D: FF ; ????
FC2E: 06 18           ASL     $18                   
FC30: 01 03           ORA     ($03,X)               
FC32: 99 FF FF        STA     $FFFF,Y                 
FC35: 03 ; ????
FC36: 01 99           ORA     ($99,X)               
FC38: 30 18           BMI     $FC52                   
FC3A: 01 01           ORA     ($01,X)               
FC3C: 99 30 18        STA     $1830,Y                 
FC3F: 01 01           ORA     ($01,X)               
FC41: 9B ; ????
FC42: 30 18           BMI     $FC5C                   
FC44: FF ; ????
FC45: FF ; ????
FC46: 99 30 18        STA     $1830,Y                 
FC49: 19 81 99        ORA     $9981,Y                 
FC4C: FF ; ????
FC4D: 18              CLC                         
FC4E: 19 81 99        ORA     $9981,Y                 
FC51: 06 18           ASL     $18                   
FC53: 1B ; ????
FC54: 81 FF           STA     ($FF,X)               
FC56: 06 FF           ASL     $FF                   
FC58: 19 FF 99        ORA     $99FF,Y                 
FC5B: 06 18           ASL     $18                   
FC5D: 19 19 99        ORA     $9919,Y                 
FC60: 06 18           ASL     $18                   
FC62: 19 19 99        ORA     $9919,Y                 
FC65: 06 18           ASL     $18                   
FC67: 19 19 FF        ORA     $FF19,Y                 
FC6A: FF ; ????
FC6B: FE FF FF        INC     $FFFF,X                 
FC6E: 00              BRK                         
FC6F: 00              BRK                         
FC70: 00              BRK                         
FC71: 00              BRK                         
FC72: 00              BRK                         
FC73: 00              BRK                         
FC74: 00              BRK                         
FC75: 00              BRK                         
FC76: 00              BRK                         
FC77: 00              BRK                         
FC78: 00              BRK                         
FC79: 00              BRK                         
FC7A: 00              BRK                         
FC7B: 00              BRK                         
FC7C: 00              BRK                         
FC7D: 00              BRK                         
FC7E: 00              BRK                         
FC7F: 00              BRK                         
FC80: 7E 66 66        ROR     $6666,X                 
FC83: 66 66           ROR     $66                   
FC85: 7E 7E 18        ROR     $187E,X                 
FC88: 18              CLC                         
FC89: 18              CLC                         
FC8A: 18              CLC                         
FC8B: 78              SEI                         
FC8C: 7E 60 7E        ROR     $7E60,X                 
FC8F: 06 66           ASL     $66                   
FC91: 7E 7E 06        ROR     $067E,X                 
FC94: 06 7C           ASL     $7C                   
FC96: 06 7E           ASL     $7E                   
FC98: 06 06           ASL     $06                   
FC9A: 7E 66 66        ROR     $6666,X                 
FC9D: 66 7E           ROR     $7E                   
FC9F: 66 06           ROR     $06                   
FCA1: 7E 60 7E        ROR     $7E60,X                 
FCA4: 7E 66 66        ROR     $6666,X                 
FCA7: 7E 60 7E        ROR     $7E60,X                 
FCAA: 20 30 18        JSR     $1830                   
FCAD: 0C ; ????
FCAE: 06 7E           ASL     $7E                   
FCB0: 7E 66 66        ROR     $6666,X                 
FCB3: 3C ; ????
FCB4: 66 7E           ROR     $7E                   
FCB6: 7E 06 7E        ROR     $7E06,X                 
FCB9: 66 66           ROR     $66                   
FCBB: 7E 24 24        ROR     $2424,X                 
FCBE: FF ; ????
FCBF: 24 FF           BIT     $FF                   
FCC1: 24 3C           BIT     $3C                   
FCC3: 66 66           ROR     $66                   
FCC5: 66 66           ROR     $66                   
FCC7: 66 60           ROR     $60                   
FCC9: 60              RTS                         
FCCA: 7E 66 66        ROR     $6666,X                 
FCCD: 7E 

; Just data above?

FCCE: AD E0 FF        LDA     $FFE0 ; Switch in bank 0
FCD1: 20 B6 F1        JSR     $F1B6  
FCD4: AD E6 FF        LDA     $FFE6                   ; Switch in bank 6
FCD7: 20 09 F4        JSR     $F409                   
FCDA: 85 2C           STA     $2C                   ; CXCLR clear all collision flags
FCDC: AD 84 02        LDA     $0284                   ; ??? Time to draw the visible screen?
FCDF: 10 FB           BPL     $FCDC                   ; ??? No ... keep waiting
FCE1: 85 02           STA     $02                   ; WSYNC
FCE3: A2 03           LDX     #$03                  ; Start the ...
FCE5: 86 00           STX     $00                   ; ... VSYNC
FCE7: 85 02           STA     $02                   ; WSYNC
FCE9: AD E6 FF        LDA     $FFE6                   ; Switch in bank 6
FCEC: 20 CB F3        JSR     $F3CB                   
FCEF: 85 02           STA     $02                   ; WSYNC
FCF1: 86 00           STX     $00                   ; X has 0 at this point ... release the VSYNC
FCF3: A9 22           LDA     #$22                  ; 34 ticks = 2176 machine cycles ...
FCF5: 8D 96 02        STA     $0296                 ; ... 2176/(228/3) = 28.6 scanlines
FCF8: 24 F6           BIT     $F6                   
FCFA: 70 06           BVS     $FD02                   
FCFC: AD E1 FF        LDA     $FFE1                   ; Switch in bank 1
FCFF: 20 35 F0        JSR     $F035                   
FD02: AD E0 FF        LDA     $FFE0                   ; Switch in bank 0
FD05: 20 31 F5        JSR     $F531                   
FD08: AD E4 FF        LDA     $FFE4                   ; Switch in bank 4
FD0B: 20 5D F6        JSR     $F65D                   
FD0E: AD 84 02        LDA     $0284                   ; Time to draw the visible screen?
FD11: 10 FB           BPL     $FD0E                   ; No ... keep waiting

FD13: 20 27 FD        JSR     $FD27                   
FD16: 4C 18 FF        JMP     $FF18
                   
FD19: AD E1 FF        LDA     $FFE1                   ; Switch in bank 1
FD1C: 20 4D F3        JSR     $F34D                   
FD1F: AD E5 FF        LDA     $FFE5                   ; Switch in bank 5
FD22: 60              RTS 
                        
FD23: 00 00 00 00                 
         
FD27: 20 D7 F6        JSR     $F6D7                   
FD2A: A9 DF           LDA     #$DF                  
FD2C: 85 06           STA     $06                   ; COLUP0
FD2E: 85 07           STA     $07                   ; COLUP1
FD30: AD 58 F9        LDA     $F958                   
FD33: 85 F2           STA     $F2                   
FD35: A5 D1           LDA     $D1                   
FD37: 85 F3           STA     $F3                   
FD39: A2 03           LDX     #$03                  
FD3B: 20 96 F7        JSR     $F796                   
FD3E: A0 05           LDY     #$05                  
FD40: 20 4F F7        JSR     $F74F                   
FD43: A9 0D           LDA     #$0D                  
FD45: 85 06           STA     $06                   ; COLUP0
FD47: A9 35           LDA     #$35                  
FD49: 85 07           STA     $07                   ; COLUP1
FD4B: A9 31           LDA     #$31                  
FD4D: 85 0A           STA     $0A                   ; CTRLPF
FD4F: AD E6 FF        LDA     $FFE6                   ; Switch in bank 6
FD52: 20 AF F3        JSR     $F3AF                   
FD55: AD E5 FF        LDA     $FFE5                   ; Switch in bank 5
FD58: A0 01           LDY     #$01                  
FD5A: 20 22 F4        JSR     $F422                   
FD5D: AD E4 FF        LDA     $FFE4                   ; Switch in bank 4
FD60: AD 0A F9        LDA     $F90A                   
FD63: 10 05           BPL     $FD6A                   
FD65: A9 08           LDA     #$08                  ; Reflect ...
FD67: 85 0B           STA     $0B                   ; ... REFP0 player 1
FD69: EA              NOP                         
FD6A: 85 02           STA     $02                   ; WSYNC
FD6C: EA              NOP                         
FD6D: EA              NOP                         
FD6E: A0 78           LDY     #$78                  
FD70: B1 C9           LDA     ($C9),Y               
FD72: 4C 16 FE        JMP     $FE16                   
FD75: A9 00           LDA     #$00                  ; For clearing
FD77: 85 0A           STA     $0A                   ; CTRLPF
FD79: 85 02           STA     $02                   ; WSYNC
FD7B: 85 0D           STA     $0D                   ; PF0
FD7D: 85 0E           STA     $0E                   ; PF1
FD7F: 85 0F           STA     $0F                   ; PF2
FD81: 85 1D           STA     $1D                   ; ENAM0
FD83: 85 1E           STA     $1E                   ; ENAM1
FD85: 85 1F           STA     $1F                   ; ENABL
FD87: 85 1B           STA     $1B                   ; GRP0
FD89: 85 1C           STA     $1C                   ; GRP1
FD8B: A9 1F           LDA     #$1F                  
FD8D: 85 08           STA     $08                   ; COLUPF
FD8F: A0 12           LDY     #$12                  
FD91: A2 03           LDX     #$03                  
FD93: 86 C7           STX     $C7                   
FD95: A2 00           LDX     #$00                  
FD97: F0 12           BEQ     $FDAB                   
FD99: A9 03           LDA     #$03                  
FD9B: 85 02           STA     $02                   ; WSYNC
FD9D: 85 C7           STA     $C7                   
FD9F: A9 00           LDA     #$00                  ; Clear
FDA1: 85 0E           STA     $0E                   ; PF1
FDA3: 85 0F           STA     $0F                   ; PF2
FDA5: BD E8 F7        LDA     $F7E8,X                 
FDA8: 85 08           STA     $08                   ; COLUPF
FDAA: 88              DEY                         
FDAB: 85 02           STA     $02                   ; WSYNC
FDAD: B9 EC F7        LDA     $F7EC,Y                 
FDB0: 3D 72 F9        AND     $F972,X                 
FDB3: 85 0E           STA     $0E                   ; PF1
FDB5: B9 EC F7        LDA     $F7EC,Y                 
FDB8: 3D 77 F9        AND     $F977,X                 
FDBB: 85 0F           STA     $0F                   ; PF2
FDBD: EA              NOP                         
FDBE: EA              NOP                         
FDBF: B9 EC F7        LDA     $F7EC,Y                 
FDC2: 3D 7C F9        AND     $F97C,X                 
FDC5: 85 0E           STA     $0E                   ; PF1
FDC7: B9 EC F7        LDA     $F7EC,Y                 
FDCA: 3D 81 F9        AND     $F981,X                 
FDCD: 85 0F           STA     $0F                   ; PF2
FDCF: 88              DEY                         
FDD0: 30 08           BMI     $FDDA                   
FDD2: C6 C7           DEC     $C7                   
FDD4: 10 D5           BPL     $FDAB                   
FDD6: E8              INX                         
FDD7: 4C 99 FD        JMP     $FD99                   
FDDA: 85 02           STA     $02                   ; WSYNC
FDDC: A9 92           LDA     #$92                  
FDDE: 85 08           STA     $08                   ; COLUPF
FDE0: A9 42           LDA     #$42                  
FDE2: 85 0E           STA     $0E                   ; PF1
FDE4: 85 0F           STA     $0F                   ; PF2
FDE6: 85 02           STA     $02                   ; WSYNC
FDE8: A9 3C           LDA     #$3C                  
FDEA: 85 0E           STA     $0E                   ; PF1
FDEC: 85 0F           STA     $0F                   ; PF2
FDEE: 85 02           STA     $02                   ; WSYNC
FDF0: A9 00           LDA     #$00                  
FDF2: 85 0E           STA     $0E                   ; PF1
FDF4: 85 0F           STA     $0F                   ; PF2
FDF6: A0 00           LDY     #$00                  
FDF8: 85 02           STA     $02                   ; WSYNC
FDFA: 88              DEY                         
FDFB: 10 FB           BPL     $FDF8                   
FDFD: AD E5 FF        LDA     $FFE5                   ; Switch in bank 5
FE00: 60              RTS                         

FE01: 4C 75 FD        JMP     $FD75       
;            
FE04: A9 00           LDA     #$00                  
FE06: 85 85           STA     $85                   
FE08: A5 C7           LDA     $C7                   
FE0A: 4C 43 FE        JMP     $FE43
                   
FE0D: A9 00           LDA     #$00                  
FE0F: 85 87           STA     $87                   
FE11: A5 C7           LDA     $C7                   
FE13: 4C 76 FE        JMP     $FE76
                   
FE16: 85 02           STA     $02                   ; WSYNC
FE18: 85 0D           STA     $0D                   
FE1A: A5 B1           LDA     $B1                   
FE1C: 85 0A           STA     $0A                   
FE1E: B1 E4           LDA     ($E4),Y               
FE20: 85 1B           STA     $1B                   
FE22: B1 CB           LDA     ($CB),Y               
FE24: 85 0E           STA     $0E                   
FE26: B1 CD           LDA     ($CD),Y               
FE28: 85 0F           STA     $0F                   
FE2A: B1 EA           LDA     ($EA),Y               
FE2C: 85 1E           STA     $1E                   
FE2E: B1 EC           LDA     ($EC),Y               
FE30: 85 1F           STA     $1F                   
FE32: 88              DEY                         
FE33: 30 CC           BMI     $FE01                   
FE35: 98              TYA                         
FE36: A6 89           LDX     $89                   
FE38: D5 8D           CMP     $8D,X                 
FE3A: B0 C8           BCS     $FE04                   
FE3C: B5 A1           LDA     $A1,X                 
FE3E: 85 85           STA     $85                   
FE40: E8              INX                         
FE41: 86 89           STX     $89                   
FE43: A9 00           LDA     #$00                  
FE45: 85 0D           STA     $0D                   
FE47: A5 B2           LDA     $B2                   
FE49: 85 0A           STA     $0A                   
FE4B: B1 E4           LDA     ($E4),Y               
FE4D: 85 1B           STA     $1B                   
FE4F: A5 81           LDA     $81                   
FE51: 85 0E           STA     $0E                   
FE53: A5 82           LDA     $82                   
FE55: 85 0F           STA     $0F                   
FE57: B1 E2           LDA     ($E2),Y               
FE59: 85 1C           STA     $1C                   
FE5B: A5 83           LDA     $83                   
FE5D: 85 0E           STA     $0E                   
FE5F: B1 E8           LDA     ($E8),Y               
FE61: 85 1D           STA     $1D                   
FE63: A5 84           LDA     $84                   
FE65: 88              DEY                         
FE66: 85 0F           STA     $0F                   
FE68: 98              TYA                         
FE69: A6 8B           LDX     $8B                   
FE6B: D5 97           CMP     $97,X                 
FE6D: B0 9E           BCS     $FE0D                   
FE6F: B5 A9           LDA     $A9,X                 
FE71: 85 87           STA     $87                   
FE73: E8              INX                         
FE74: 86 8B           STX     $8B                   
FE76: B1 E4           LDA     ($E4),Y               
FE78: 85 1B           STA     $1B                   
FE7A: A5 81           LDA     $81                   
FE7C: 85 0E           STA     $0E                   
FE7E: B1 E2           LDA     ($E2),Y               
FE80: 85 1C           STA     $1C                   
FE82: A5 82           LDA     $82                   
FE84: 85 0F           STA     $0F                   
FE86: B1 EA           LDA     ($EA),Y               
FE88: 85 1E           STA     $1E                   
FE8A: A5 83           LDA     $83                   
FE8C: 85 0E           STA     $0E                   
FE8E: 88              DEY                         
FE8F: A5 84           LDA     $84                   
FE91: 85 0F           STA     $0F                   
FE93: B1 EC           LDA     ($EC),Y               
FE95: 85 1F           STA     $1F                   
FE97: A6 8A           LDX     $8A                   
FE99: 98              TYA                         
FE9A: D5 92           CMP     $92,X                 
FE9C: B0 58           BCS     $FEF6                   
FE9E: B5 A5           LDA     $A5,X                 
FEA0: 85 86           STA     $86                   
FEA2: E8              INX                         
FEA3: 86 8A           STX     $8A                   
FEA5: A5 81           LDA     $81                   
FEA7: 85 0E           STA     $0E                   
FEA9: B1 E4           LDA     ($E4),Y               
FEAB: 85 1B           STA     $1B                   
FEAD: A5 82           LDA     $82                   
FEAF: 85 0F           STA     $0F                   
FEB1: B1 E2           LDA     ($E2),Y               
FEB3: 85 1C           STA     $1C                   
FEB5: A5 83           LDA     $83                   
FEB7: 85 0E           STA     $0E                   
FEB9: 88              DEY                         
FEBA: A5 84           LDA     $84                   
FEBC: 85 0F           STA     $0F                   
FEBE: 98              TYA                         
FEBF: A6 8C           LDX     $8C                   
FEC1: D5 9C           CMP     $9C,X                 
FEC3: B0 3A           BCS     $FEFF                   
FEC5: B5 AD           LDA     $AD,X                 
FEC7: 85 88           STA     $88                   
FEC9: E8              INX                         
FECA: 86 8C           STX     $8C                   
FECC: B1 E4           LDA     ($E4),Y               
FECE: 85 1B           STA     $1B                   
FED0: A5 81           LDA     $81                   
FED2: 85 0E           STA     $0E                   
FED4: A5 82           LDA     $82                   
FED6: 85 0F           STA     $0F                   
FED8: A5 85           LDA     $85                   
FEDA: 85 81           STA     $81                   
FEDC: A5 86           LDA     $86                   
FEDE: 85 82           STA     $82                   
FEE0: A5 83           LDA     $83                   
FEE2: 85 0E           STA     $0E                   
FEE4: A5 87           LDA     $87                   
FEE6: 85 83           STA     $83                   
FEE8: A5 84           LDA     $84                   
FEEA: 85 0F           STA     $0F                   
FEEC: A5 88           LDA     $88                   
FEEE: 85 84           STA     $84                   
FEF0: 88              DEY                         
FEF1: B1 C9           LDA     ($C9),Y               
FEF3: 4C 16 FE        JMP     $FE16                   
FEF6: A9 00           LDA     #$00                  
FEF8: 85 86           STA     $86                   
FEFA: A5 C7           LDA     $C7                   
FEFC: 4C A5 FE        JMP     $FEA5                   
FEFF: A9 00           LDA     #$00                  
FF01: 85 88           STA     $88                   
FF03: A5 C7           LDA     $C7                   
FF05: 4C CC FE        JMP     $FECC      
             
; Startup comes here

Startup:
FF08: D8              CLD                         ; Clear decimal math flag
FF09: A2 FF           LDX     #$FF                ; Stack start at ...
FF0B: 9A              TXS                         ; ... end of RAM
FF0C: AD E5 FF        LDA     $FFE5               ; Switch in bank 5 (F000..F7FF)
FF0F: AD E8 FF        LDA     $FFE8               ; Set RAM to READ
FF12: 20 00 F0        JSR     $F000               ; bank5:F000             
FF15: 20 19 FD        JSR     $FD19                   

FF18: 85 02           STA     $02                   ; WSYNC
FF1A: 20 99 F6        JSR     $F699                   
FF1D: F0 64           BEQ     $FF83                   
FF1F: 90 E7           BCC     $FF08                   
FF21: 70 34           BVS     $FF57                   
FF23: E6 DE           INC     $DE                   
FF25: AD 56 F9        LDA     $F956                   
FF28: 29 10           AND     #$10                  
FF2A: F0 0A           BEQ     $FF36                   
FF2C: 24 80           BIT     $80                   
FF2E: 30 27           BMI     $FF57                   
FF30: 20 BA F6        JSR     $F6BA                   
FF33: 4C D4 FC        JMP     $FCD4                   
FF36: 2C 56 F9        BIT     $F956                   
FF39: 10 1F           BPL     $FF5A                   
FF3B: 24 80           BIT     $80                   
FF3D: 30 18           BMI     $FF57                   
FF3F: 20 27 F7        JSR     $F727                   
FF42: B0 1F           BCS     $FF63                   
FF44: 2C 09 F9        BIT     $F909                   
FF47: 10 0E           BPL     $FF57                   
FF49: 20 35 F7        JSR     $F735                   
FF4C: 10 28           BPL     $FF76                   
FF4E: A5 DE           LDA     $DE                   
FF50: 29 7F           AND     #$7F                  
FF52: D0 03           BNE     $FF57                   
FF54: 20 E2 F6        JSR     $F6E2                   
FF57: 4C D4 FC        JMP     $FCD4                   
FF5A: 2C 56 F9        BIT     $F956                   
FF5D: 50 2D           BVC     $FF8C                   
FF5F: 24 80           BIT     $80                   
FF61: 50 03           BVC     $FF66                   
FF63: 4C CE FC        JMP     $FCCE                   
FF66: 20 27 F7        JSR     $F727                   
FF69: B0 F8           BCS     $FF63                   
FF6B: 20 11 F7        JSR     $F711                   
FF6E: 10 06           BPL     $FF76                   
FF70: 20 0C F6        JSR     $F60C                   
FF73: 4C 83 FF        JMP     $FF83                   
FF76: AD 56 F9        LDA     $F956                   
FF79: 29 8F           AND     #$8F                  
FF7B: 8D 56 F8        STA     $F856                   
FF7E: 20 FD F5        JSR     $F5FD                   
FF81: D0 D4           BNE     $FF57                   
FF83: AD E1 FF        LDA     $FFE1                   ; Switch in bank 1
FF86: 20 4D F3        JSR     $F34D                   
FF89: 4C D4 FC        JMP     $FCD4                   
FF8C: AD E0 FF        LDA     $FFE0                   ; Switch in bank 0
FF8F: 20 4D F6        JSR     $F64D                   
FF92: A5 DE           LDA     $DE                   
FF94: D0 0F           BNE     $FFA5                   
FF96: AD E1 FF        LDA     $FFE1                   ; Switch in bank 1
FF99: 20 5C F2        JSR     $F25C                   
FF9C: AD E6 FF        LDA     $FFE6                   ; Switch in bank 6
FF9F: 20 22 F7        JSR     $F722                   
FFA2: 4C DA FC        JMP     $FCDA                   
FFA5: 20 B6 F6        JSR     $F6B6                   
FFA8: 90 06           BCC     $FFB0                   
FFAA: AD E5 FF        LDA     $FFE5                   ; Switch in bank 5
FFAD: 20 D9 F2        JSR     $F2D9                   
FFB0: AD E6 FF        LDA     $FFE6                   ; Switch in bank 6
FFB3: 20 04 F0        JSR     $F004                   
FFB6: A5 DE           LDA     $DE                   
FFB8: 29 03           AND     #$03                  
FFBA: D0 06           BNE     $FFC2                   
FFBC: AD E5 FF        LDA     $FFE5                   ; Switch in bank 5
FFBF: 20 03 F4        JSR     $F403                   
FFC2: AD 56 F9        LDA     $F956                   
FFC5: 29 01           AND     #$01                  
FFC7: D0 8E           BNE     $FF57                   
FFC9: A5 DE           LDA     $DE                   
FFCB: 29 03           AND     #$03                  
FFCD: D0 0C           BNE     $FFDB                   
FFCF: 20 FF F2        JSR     $F2FF                   
FFD2: 20 64 F5        JSR     $F564                   
FFD5: AD E0 FF        LDA     $FFE0                   ; Switch in bank 0
FFD8: 20 02 F0        JSR     $F002                   
FFDB: 4C CE FC        JMP     $FCCE
                   
FFDE: 00 00    
                    
FFE0: 00 ; Read here to switch ROM bank 0 into F000 - F7FF
FFE1: 00 ; ... bank 1
FFE2: 00 ; ... bank 2                      
FFE3: 00 ; ... bank 3                         
FFE4: 00 ; ... bank 4           
FFE5: 00 ; ... bank 5 
FFE6: 00 ; ... bank 6 
FFE7: 00 ; ... 1K of RAM (first 1K is for WRITE, second 1K is for READ) 
;                      
FFE8: 00 ; Read here to switch 256 bytes of RAM (bank 0) into F800 - F9FF. First 256 WRITE, 2nd 256 READ                   
FFE9: 00 ; bank 1                         
FFEA: 00 ; bank 2                         
FFEB: 00 ; bank 3
                        
FFEC: 00 00 00 00 00 00 00 00 00 00 00 00 00 00    
```

# Vectors

```code                  
FFFA: 08 FF ; NMI to FF08 (not available on the 6507)
FFFC: 08 FF ; Reset to FF08
FFFE: 08 FF ; IRQ to FF08 (not available on the 6507)
```