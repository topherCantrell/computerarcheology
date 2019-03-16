![Defender Sound Board Code](Defender.jpg)

# Defender Sound Board

cpu 6800

>>> memoryTable hard 
[Hardware Info](SoundHardware.md)

>>> memoryTable ram 
[RAM Usage](SoundRAMUse.md)

Harry Hurst. This is a disassembly of one of two ROM images that I have found for the Defender sound board. The other ROM image is largely the same, but with some 
significant omissions, and rerouting of jumps and subroutines. At this time I do not have any plans to disassemble that ROM.

```plainCode
F800: FF
 
RESET:
F801: 0F            SEI                     ;VECTOR at $FFFE and $FFFA, disable interrupts
F802: 8E 00 7F      LDS   #$007F            ;initialize stack pointer to top of RAM
F805: CE 04 00      LDX   #$0400            ;load PIA address
F808: 6F 01         CLR   $01,X             ;switch to DDR
F80A: 6F 03         CLR   $03,X             ;ditto for second port
F80C: 86 FF         LDAA  #$FF              ;
F80E: A7 00         STAA  $00,X             ;all outputs on channel A
F810: 6F 02         CLR   $02,X             ;all inputs on channel B
F812: 86 37         LDAA  #$37              ;CB2 is output,output reg selected,
F814: A7 03         STAA  $03,X             ;IRQB on low-to-high and enabled
F816: 86 3C         LDAA  #$3C              ;CA2 is output,output reg selected,
F818: A7 01         STAA  $01,X             ;IRQA on high-to-low and disabled
F81A: 97 09         STAA  <$09              ;store that setting
F81C: 4F            CLRA                    ;
F81D: 97 07         STAA  <$07              ;clear several mem locations
F81F: 97 04         STAA  <$04              ;
F821: 97 05         STAA  <$05              ;
F823: 97 06         STAA  <$06              ;
F825: 97 08         STAA  <$08              ;
F827: 0E            CLI                     ;enable interrupts
F828: 20 FE         BRA   $F828             ;just waiting for an interrupt

Multiply the number in the A register by 9, use that to index into a table starting at $FD76, and put a 9 in the B reg.

F82A: 16            TAB                     ; SUBRTN
F82B: 48            ASLA                    ;
F82C: 48            ASLA                    ;
F82D: 48            ASLA                    ;A x 8
F82E: 1B            ABA                     ;A x 8 + A = 9A
F82F: CE 00 13      LDX   #$0013            ;load 19 in X reg
F832: DF 0F         STX   <$0F              ;store in zero page
F834: CE FD 76      LDX   #$FD76            ;load table address
F837: BD FD 21      JSR   CalcOfst          ;calculate X + A -> X
F83A: C6 09         LDAB  #$09              ;put a 9 in B reg
F83C: 7E FB 0A      JMP   $FB0A             ;

F83F: 96 1B         LDAA  <$1B              ;SUBRTN
F841: B7 04 00      STAA  >$0400            ;
F844: 96 13         LDAA  <$13              ;
F846: 97 1C         STAA  <$1C              ;
F848: 96 14         LDAA  <$14              ;
F84A: 97 1D         STAA  <$1D              ;
F84C: DE 18         LDX   <$18              ;
F84E: 96 1C         LDAA  <$1C              ;
F850: 73 04 00      COM   >$0400            ;
F853: 09            DEX                     ;
F854: 27 10         BEQ   $F866             ;
F856: 4A            DECA                    ;
F857: 26 FA         BNE   $F853             ;
F859: 73 04 00      COM   >$0400            ;
F85C: 96 1D         LDAA  <$1D              ;
F85E: 09            DEX                     ;
F85F: 27 05         BEQ   $F866             ;
F861: 4A            DECA                    ;
F862: 26 FA         BNE   $F85E             ;
F864: 20 E8         BRA   $F84E             ;
F866: B6 04 00      LDAA  >$0400            ;
F869: 2B 01         BMI   $F86C             ;
F86B: 43            COMA                    ;
F86C: 8B 00         ADDA  #$00              ;
F86E: B7 04 00      STAA  >$0400            ;
F871: 96 1C         LDAA  <$1C              ;
F873: 9B 15         ADDA  <$15              ;
F875: 97 1C         STAA  <$1C              ;
F877: 96 1D         LDAA  <$1D              ;
F879: 9B 16         ADDA  <$16              ;
F87B: 97 1D         STAA  <$1D              ;
F87D: 91 17         CMPA  <$17              ;
F87F: 26 CB         BNE   $F84C             ;
F881: 96 1A         LDAA  <$1A              ;
F883: 27 06         BEQ   $F88B             ;
F885: 9B 13         ADDA  <$13              ;
F887: 97 13         STAA  <$13              ;
F889: 26 B9         BNE   $F844             ;
F88B: 39            RTS                     ;

F88C: 86 01         LDAA  #$01              ;W vector
F88E: 97 1A         STAA  <$1A              ;
F890: C6 03         LDAB  #$03              ;
F892: 20 0A         BRA   $F89E             ;
F894: 86 FE         LDAA  #$FE              ;W vector
F896: 97 1A         STAA  <$1A              ;
F898: 86 C0         LDAA  #$C0              ;
F89A: C6 10         LDAB  #$10              ;
F89C: 20 00         BRA   $F89E             ;really?
F89E: 97 19         STAA  <$19              ;
F8A0: 86 FF         LDAA  #$FF              ;
F8A2: B7 04 00      STAA  >$0400            ;
F8A5: D7 15         STAB  <$15              ;
F8A7: D6 15         LDAB  <$15              ;
F8A9: 96 0A         LDAA  <$0A              ;
F8AB: 44            LSRA                    ;
F8AC: 44            LSRA                    ;
F8AD: 44            LSRA                    ;
F8AE: 98 0A         EORA  <$0A              ;
F8B0: 44            LSRA                    ;
F8B1: 76 00 09      ROR   >$0009            ;
F8B4: 76 00 0A      ROR   >$000A            ;
F8B7: 24 03         BCC   $F8BC             ;
F8B9: 73 04 00      COM   >$0400            ;
F8BC: 96 19         LDAA  <$19              ;
F8BE: 4A            DECA                    ;
F8BF: 26 FD         BNE   $F8BE             ;
F8C1: 5A            DECB                    ;
F8C2: 26 E5         BNE   $F8A9             ;
F8C4: 96 19         LDAA  <$19              ;
F8C6: 9B 1A         ADDA  <$1A              ;
F8C8: 97 19         STAA  <$19              ;
F8CA: 26 DB         BNE   $F8A7             ;
F8CC: 39            RTS                     ;

F8CD: 86 20         LDAA  #$20              ;W vector
F8CF: 97 15         STAA  <$15              ;
F8D1: 97 18         STAA  <$18              ;
F8D3: 86 01         LDAA  #$01              ;
F8D5: CE 00 01      LDX   #$0001            ;
F8D8: C6 FF         LDAB  #$FF              ;
F8DA: 20 00         BRA   $F8DC             ;doing it again, must be a timing thing
F8DC: 97 13         STAA  <$13              ;
F8DE: DF 16         STX   <$16              ;
F8E0: D7 14         STAB  <$14              ;
F8E2: D6 15         LDAB  <$15              ;
F8E4: 96 0A         LDAA  <$0A              ;
F8E6: 44            LSRA                    ;
F8E7: 44            LSRA                    ;
F8E8: 44            LSRA                    ;
F8E9: 98 0A         EORA  <$0A              ;
F8EB: 44            LSRA                    ;
F8EC: 76 00 09      ROR   >$0009            ;
F8EF: 76 00 0A      ROR   >$000A            ;
F8F2: 86 00         LDAA  #$00              ;
F8F4: 24 02         BCC   $F8F8             ;
F8F6: 96 14         LDAA  <$14              ;
F8F8: B7 04 00      STAA  >$0400            ;
F8FB: DE 16         LDX   <$16              ;
F8FD: 09            DEX                     ;
F8FE: 26 FD         BNE   $F8FD             ;
F900: 5A            DECB                    ;
F901: 26 E1         BNE   $F8E4             ;
F903: D6 14         LDAB  <$14              ;
F905: D0 13         SUBB  <$13              ;
F907: 27 09         BEQ   $F912             ;
F909: DE 16         LDX   <$16              ;
F90B: 08            INX                     ;
F90C: 96 18         LDAA  <$18              ;
F90E: 27 D0         BEQ   $F8E0             ;
F910: 20 CC         BRA   $F8DE             ;
F912: 39            RTS                     ;

F913: C6 01         LDAB  #$01              ;W vector
F915: D7 04         STAB  <$04              ;
F917: 4F            CLRA                    ;
F918: 97 19         STAA  <$19              ;
F91A: 20 14         BRA   $F930             ;
F91C: 4F            CLRA                    ;W vector
F91D: 97 19         STAA  <$19              ;
F91F: C6 03         LDAB  #$03              ;
F921: 20 0D         BRA   $F930             ;
F923: 86 01         LDAA  #$01              ;W vector
F925: 97 19         STAA  <$19              ;
F927: CE 03 E8      LDX   #$03E8            ;
F92A: 86 01         LDAA  #$01              ;
F92C: C6 FF         LDAB  #$FF              ;
F92E: 20 00         BRA   $F930             ;
F930: 97 18         STAA  <$18              ;
F932: D7 13         STAB  <$13              ;
F934: DF 16         STX   <$16              ;
F936: 7F 00 15      CLR   >$0015            ;
F939: DE 16         LDX   <$16              ;
F93B: B6 04 00      LDAA  >$0400            ;
F93E: 16            TAB                     ;
F93F: 54            LSRB                    ;
F940: 54            LSRB                    ;
F941: 54            LSRB                    ;
F942: D8 0A         EORB  <$0A              ;
F944: 54            LSRB                    ;
F945: 76 00 09      ROR   >$0009            ;
F948: 76 00 0A      ROR   >$000A            ;
F94B: D6 13         LDAB  <$13              ;
F94D: 7D 00 19      TST   >$0019            ;
F950: 27 02         BEQ   $F954             ;
F952: D4 09         ANDB  <$09              ;
F954: D7 14         STAB  <$14              ;
F956: D6 15         LDAB  <$15              ;
F958: 91 0A         CMPA  <$0A              ;
F95A: 22 12         BHI   $F96E             ;
F95C: 09            DEX                     ;
F95D: 27 26         BEQ   $F985             ;
F95F: B7 04 00      STAA  >$0400            ;
F962: DB 15         ADDB  <$15              ;
F964: 99 14         ADCA  <$14              ;
F966: 25 16         BCS   $F97E             ;
F968: 91 0A         CMPA  <$0A              ;
F96A: 23 F0         BLS   $F95C             ;
F96C: 20 10         BRA   $F97E             ;
F96E: 09            DEX                     ;
F96F: 27 14         BEQ   $F985             ;
F971: B7 04 00      STAA  >$0400            ;
F974: D0 15         SUBB  <$15              ;
F976: 92 14         SBCA  <$14              ;
F978: 25 04         BCS   $F97E             ;
F97A: 91 0A         CMPA  <$0A              ;
F97C: 22 F0         BHI   $F96E             ;
F97E: 96 0A         LDAA  <$0A              ;
F980: B7 04 00      STAA  >$0400            ;
F983: 20 B9         BRA   $F93E             ;
F985: D6 18         LDAB  <$18              ;
F987: 27 B5         BEQ   $F93E             ;
F989: 96 13         LDAA  <$13              ;
F98B: D6 15         LDAB  <$15              ;
F98D: 44            LSRA                    ;
F98E: 56            RORB                    ;
F98F: 44            LSRA                    ;
F990: 56            RORB                    ;
F991: 44            LSRA                    ;
F992: 56            RORB                    ;
F993: 43            COMA                    ;
F994: 50            NEGB                    ;
F995: 82 FF         SBCA  #$FF              ;
F997: DB 15         ADDB  <$15              ;
F999: 99 13         ADCA  <$13              ;
F99B: D7 15         STAB  <$15              ;
F99D: 97 13         STAA  <$13              ;
F99F: 26 98         BNE   $F939             ;
F9A1: C1 07         CMPB  #$07              ;
F9A3: 26 94         BNE   $F939             ;
F9A5: 39            RTS                     ;

F9A6: 86 FD         LDAA  #$FD              ;W vector
F9A8: 97 0F         STAA  <$0F              ;
F9AA: CE 00 64      LDX   #$0064            ;
F9AD: DF 0B         STX   <$0B              ;
F9AF: DB 0C         ADDB  <$0C              ;
F9B1: 96 11         LDAA  <$11              ;
F9B3: 99 0B         ADCA  <$0B              ;
F9B5: 97 11         STAA  <$11              ;
F9B7: DE 0B         LDX   <$0B              ;
F9B9: 25 04         BCS   $F9BF             ;
F9BB: 20 00         BRA   $F9BD             ;
F9BD: 20 03         BRA   $F9C2             ;
F9BF: 08            INX                     ;
F9C0: 27 11         BEQ   $F9D3             ;
F9C2: DF 0B         STX   <$0B              ;
F9C4: 84 0F         ANDA  #$0F              ;
F9C6: 8B 9A         ADDA  #$9A              ;
F9C8: 97 10         STAA  <$10              ;
F9CA: DE 0F         LDX   <$0F              ;
F9CC: A6 00         LDAA  $00,X             ;
F9CE: B7 04 00      STAA  >$0400            ;
F9D1: 20 DC         BRA   $F9AF             ;
F9D3: 39            RTS                     ;

F9D4: 4F            CLRA                    ;W vector
F9D5: B7 04 00      STAA  >$0400            ;
F9D8: 97 11         STAA  <$11              ;
F9DA: 4F            CLRA                    ;
F9DB: 91 11         CMPA  <$11              ;
F9DD: 26 03         BNE   $F9E2             ;
F9DF: 73 04 00      COM   >$0400            ;
F9E2: C6 12         LDAB  #$12              ;
F9E4: 5A            DECB                    ;
F9E5: 26 FD         BNE   $F9E4             ;
F9E7: 4C            INCA                    ;
F9E8: 2A F1         BPL   $F9DB             ;
F9EA: 73 04 00      COM   >$0400            ;
F9ED: 7C 00 11      INC   >$0011            ;
F9F0: 2A E8         BPL   $F9DA             ;
F9F2: 39            RTS                     ;

F9F3: CE 00 13      LDX   #$0013            ;W vector
F9F6: 6F 00         CLR   $00,X             ;
F9F8: 08            INX                     ;
F9F9: 8C 00 1B      CPX   #$001B            ;
F9FC: 26 F8         BNE   $F9F6             ;
F9FE: 86 40         LDAA  #$40              ;
FA00: 97 13         STAA  <$13              ;
FA02: CE 00 13      LDX   #$0013            ;
FA05: 86 80         LDAA  #$80              ;
FA07: 97 11         STAA  <$11              ;
FA09: 5F            CLRB                    ;
FA0A: A6 01         LDAA  $01,X             ;
FA0C: AB 00         ADDA  $00,X             ;
FA0E: A7 01         STAA  $01,X             ;
FA10: 2A 02         BPL   $FA14             ;
FA12: DB 11         ADDB  <$11              ;
FA14: 74 00 11      LSR   >$0011            ;
FA17: 08            INX                     ;
FA18: 08            INX                     ;
FA19: 8C 00 1B      CPX   #$001B            ;
FA1C: 26 EC         BNE   $FA0A             ;
FA1E: F7 04 00      STAB  >$0400            ;
FA21: 7C 00 12      INC   >$0012            ;
FA24: 26 DC         BNE   $FA02             ;
FA26: CE 00 13      LDX   #$0013            ;
FA29: 5F            CLRB                    ;
FA2A: A6 00         LDAA  $00,X             ;
FA2C: 27 0B         BEQ   $FA39             ;
FA2E: 81 37         CMPA  #$37              ;
FA30: 26 04         BNE   $FA36             ;
FA32: C6 41         LDAB  #$41              ;
FA34: E7 02         STAB  $02,X             ;
FA36: 6A 00         DEC   $00,X             ;
FA38: 5C            INCB                    ;
FA39: 08            INX                     ;
FA3A: 08            INX                     ;
FA3B: 8C 00 1B      CPX   #$001B            ;
FA3E: 26 EA         BNE   $FA2A             ;
FA40: 5D            TSTB                    ;
FA41: 26 BF         BNE   $FA02             ;
FA43: 39            RTS                     ;

Will I ever know why this was made into a subroutine?
It is a subroutine because it is called through a jump table.

FA44: 7A 00 08      DEC   >$0008            ;W vector
FA47: 39            RTS                     ;

FA48: 7F 00 08      CLR   >$0008            ;SUBRTN
FA4B: 97 11         STAA  <$11              ;store the countdown value
FA4D: CE FD AA      LDX   #$FDAA            ;starting point always the same, $FDAA
FA50: A6 00         LDAA  $00,X             ;
FA52: 27 2D         BEQ   $FA81             ;get out on a zero
FA54: 7A 00 11      DEC   >$0011            ;
FA57: 27 06         BEQ   $FA5F             ;exit the loop when countdown has reached zero
FA59: 4C            INCA                    ;
FA5A: BD FD 21      JSR   CalcOfst          ;adjust X by A
FA5D: 20 F1         BRA   $FA50             ;loop until an exit condition is encountered
FA5F: 08            INX                     ;
FA60: DF 0F         STX   <$0F              ;
FA62: BD FD 21      JSR   CalcOfst          ;adjust X by A
FA65: DF 0D         STX   <$0D              ;
FA67: DE 0F         LDX   <$0F              ;
FA69: A6 00         LDAA  $00,X             ;
FA6B: 97 15         STAA  <$15              ;
FA6D: A6 01         LDAA  $01,X             ;
FA6F: EE 02         LDX   $02,X             ;
FA71: DF 13         STX   <$13              ;
FA73: 8D 3E         BSR   $FAB3             ;
FA75: DE 0F         LDX   <$0F              ;
FA77: 08            INX                     ;
FA78: 08            INX                     ;
FA79: 08            INX                     ;
FA7A: 08            INX                     ;
FA7B: DF 0F         STX   <$0F              ;
FA7D: 9C 0D         CPX   <$0D              ;
FA7F: 26 E8         BNE   $FA69             ;
FA81: 7E FD 0E      JMP   $FD0E             ;

Are you kidding? A subroutine to do this?
This is called from a jump table

FA84: 86 03         LDAA  #$03              ;W vector
FA86: 97 08         STAA  <$08              ;initiating a count?
FA88: 39            RTS                     ;

FA89: 7A 00 08      DEC   >$0008            ; SUBRTN
FA8C: 27 0C         BEQ   $FA9A             ;
FA8E: D6 15         LDAB  <$15              ;
FA90: 58            ASLB                    ;
FA91: 58            ASLB                    ;
FA92: 58            ASLB                    ;
FA93: 58            ASLB                    ;
FA94: 1B            ABA                     ;
FA95: 97 15         STAA  <$15              ;
FA97: 4F            CLRA                    ;
FA98: 20 FE         BRA   $FA98             ;
FA9A: 4A            DECA                    ;
FA9B: 81 0B         CMPA  #$0B              ;
FA9D: 23 01         BLS   $FAA0             ;
FA9F: 4F            CLRA                    ;
FAA0: CE FE 41      LDX   #$FE41            ;
FAA3: BD FD 21      JSR   CalcOfst          ;
FAA6: A6 00         LDAA  $00,X             ;
FAA8: CE FF FF      LDX   #$FFFF            ;
FAAB: DF 13         STX   <$13              ;
FAAD: 8D 04         BSR   $FAB3             ;
FAAF: 8D 2A         BSR   $FADB             ;
FAB1: 20 FC         BRA   $FAAF             ;

FAB3: CE 00 16      LDX   #$0016            ; SUBRTN
FAB6: 81 00         CMPA  #$00              ;
FAB8: 27 15         BEQ   $FACF             ;
FABA: 81 03         CMPA  #$03              ;
FABC: 27 09         BEQ   $FAC7             ;
FABE: C6 01         LDAB  #$01              ;
FAC0: E7 00         STAB  $00,X             ;
FAC2: 08            INX                     ;
FAC3: 80 02         SUBA  #$02              ;
FAC5: 20 EF         BRA   $FAB6             ;
FAC7: C6 91         LDAB  #$91              ;
FAC9: E7 00         STAB  $00,X             ;
FACB: 6F 01         CLR   $01,X             ;
FACD: 08            INX                     ;
FACE: 08            INX                     ;
FACF: C6 7E         LDAB  #$7E              ;
FAD1: E7 00         STAB  $00,X             ;
FAD3: C6 FA         LDAB  #$FA              ;
FAD5: E7 01         STAB  $01,X             ;
FAD7: C6 DD         LDAB  #$DD              ;
FAD9: E7 02         STAB  $02,X             ;
FADB: DE 13         LDX   <$13              ; SUBRTN
FADD: 4F            CLRA                    ;
FADE: F6 00 12      LDAB  >$0012            ;
FAE1: 5C            INCB                    ;
FAE2: D7 12         STAB  <$12              ;
FAE4: D4 15         ANDB  <$15              ;
FAE6: 54            LSRB                    ;
FAE7: 89 00         ADCA  #$00              ;
FAE9: 54            LSRB                    ;
FAEA: 89 00         ADCA  #$00              ;
FAEC: 54            LSRB                    ;
FAED: 89 00         ADCA  #$00              ;
FAEF: 54            LSRB                    ;
FAF0: 89 00         ADCA  #$00              ;
FAF2: 54            LSRB                    ;
FAF3: 89 00         ADCA  #$00              ;
FAF5: 54            LSRB                    ;
FAF6: 89 00         ADCA  #$00              ;
FAF8: 54            LSRB                    ;
FAF9: 89 00         ADCA  #$00              ;
FAFB: 1B            ABA                     ;
FAFC: 48            ASLA                    ;
FAFD: 48            ASLA                    ;
FAFE: 48            ASLA                    ;
FAFF: 48            ASLA                    ;
FB00: B7 04 00      STAA  >$0400            ;
FB03: 09            DEX                     ;
FB04: 27 03         BEQ   $FB09             ;
FB06: 7E 00 16      JMP   $0016             ;
FB09: 39            RTS                     ;

FB0A: 36            PSHA                    ;SUBRTN
FB0B: A6 00         LDAA  $00,X             ;load byte from X address
FB0D: DF 0D         STX   <$0D              ;save it
FB0F: DE 0F         LDX   <$0F              ;load address to write to
FB11: A7 00         STAA  $00,X             ;write it
FB13: 08            INX                     ;advance the write pointer
FB14: DF 0F         STX   <$0F              ;store the updated pointer
FB16: DE 0D         LDX   <$0D              ;get the source address back
FB18: 08            INX                     ;advance source as well
FB19: 5A            DECB                    ;decrement counter
FB1A: 26 EF         BNE   $FB0B             ;loop if not done yet
FB1C: 32            PULA                    ;get A reg contents back
FB1D: 39            RTS                     ;return to caller

FB1E: 4F            CLRA                    ;W vector
FB1F: 97 04         STAA  <$04              ;
FB21: 97 05         STAA  <$05              ;
FB23: 39            RTS                     ;

FB24: 7F 00 04      CLR   >$0004            ;W vector
FB27: 96 05         LDAA  <$05              ;
FB29: 84 7F         ANDA  #$7F              ;
FB2B: 81 1D         CMPA  #$1D              ;
FB2D: 26 01         BNE   $FB30             ;
FB2F: 4F            CLRA                    ;
FB30: 4C            INCA                    ;
FB31: 97 05         STAA  <$05              ;
FB33: 39            RTS                     ;
FB34: 86 0E         LDAA  #$0E              ;
FB36: BD FB 81      JSR   $FB81             ;
FB39: 96 05         LDAA  <$05              ;
FB3B: 48            ASLA                    ;
FB3C: 48            ASLA                    ;
FB3D: 43            COMA                    ;
FB3E: BD FC 39      JSR   $FC39             ;
FB41: 7C 00 17      INC   >$0017            ;
FB44: BD FC 3B      JSR   $FC3B             ;
FB47: 20 F8         BRA   $FB41             ;

FB49: 86 03         LDAA  #$03              ;W vector, get third set from table
FB4B: BD F8 2A      JSR   $F82A             ;go write it out from ROM
FB4E: D6 06         LDAB  <$06              ;
FB50: C1 1F         CMPB  #$1F              ;is it 31?
FB52: 26 01         BNE   $FB55             ;if not, go on
FB54: 5F            CLRB                    ;if it is, then set it to 0
FB55: 5C            INCB                    ;increment it
FB56: D7 06         STAB  <$06              ;store updated value
FB58: 86 20         LDAA  #$20              ;
FB5A: 10            SBA                     ;
FB5B: 5F            CLRB                    ;
FB5C: 81 14         CMPA  #$14              ;
FB5E: 23 05         BLS   $FB65             ;
FB60: CB 0E         ADDB  #$0E              ;
FB62: 4A            DECA                    ;
FB63: 20 F7         BRA   $FB5C             ;
FB65: CB 05         ADDB  #$05              ;
FB67: 4A            DECA                    ;
FB68: 26 FB         BNE   $FB65             ;
FB6A: D7 13         STAB  <$13              ;
FB6C: BD F8 3F      JSR   $F83F             ;
FB6F: 20 FB         BRA   $FB6C             ;

FB71: 96 07         LDAA  <$07              ;W vector
FB73: 26 09         BNE   $FB7E             ;
FB75: 7C 00 07      INC   >$0007            ;
FB78: 86 0D         LDAA  #$0D              ;
FB7A: 8D 05         BSR   $FB81             ;
FB7C: 20 69         BRA   $FBE7             ;
FB7E: 7E FC 2E      JMP   $FC2E             ;

FB81: 16            TAB                     ; SUBRTN
FB82: 58            ASLB                    ;
FB83: 1B            ABA                     ;
FB84: 1B            ABA                     ;
FB85: 1B            ABA                     ;
FB86: CE FE EC      LDX   #$FEEC            ;
FB89: BD FD 21      JSR   CalcOfst          ;
FB8C: A6 00         LDAA  $00,X             ;
FB8E: 16            TAB                     ;
FB8F: 84 0F         ANDA  #$0F              ;
FB91: 97 14         STAA  <$14              ;
FB93: 54            LSRB                    ;
FB94: 54            LSRB                    ;
FB95: 54            LSRB                    ;
FB96: 54            LSRB                    ;
FB97: D7 13         STAB  <$13              ;
FB99: A6 01         LDAA  $01,X             ;
FB9B: 16            TAB                     ;
FB9C: 54            LSRB                    ;
FB9D: 54            LSRB                    ;
FB9E: 54            LSRB                    ;
FB9F: 54            LSRB                    ;
FBA0: D7 15         STAB  <$15              ;
FBA2: 84 0F         ANDA  #$0F              ;
FBA4: 97 11         STAA  <$11              ;
FBA6: DF 0B         STX   <$0B              ;
FBA8: CE FE 4D      LDX   #$FE4D            ;
FBAB: 7A 00 11      DEC   >$0011            ;
FBAE: 2B 08         BMI   $FBB8             ;
FBB0: A6 00         LDAA  $00,X             ;
FBB2: 4C            INCA                    ;
FBB3: BD FD 21      JSR   CalcOfst          ;
FBB6: 20 F3         BRA   $FBAB             ;
FBB8: DF 18         STX   <$18              ;
FBBA: BD FC 75      JSR   $FC75             ;
FBBD: DE 0B         LDX   <$0B              ;
FBBF: A6 02         LDAA  $02,X             ;
FBC1: 97 1A         STAA  <$1A              ;
FBC3: BD FC 87      JSR   $FC87             ;
FBC6: DE 0B         LDX   <$0B              ;
FBC8: A6 03         LDAA  $03,X             ;
FBCA: 97 16         STAA  <$16              ;
FBCC: A6 04         LDAA  $04,X             ;
FBCE: 97 17         STAA  <$17              ;
FBD0: A6 05         LDAA  $05,X             ;
FBD2: 16            TAB                     ;
FBD3: A6 06         LDAA  $06,X             ;
FBD5: CE FF 55      LDX   #$FF55            ;
FBD8: BD FD 21      JSR   CalcOfst          ;
FBDB: 17            TBA                     ;
FBDC: DF 1B         STX   <$1B              ;
FBDE: 7F 00 23      CLR   >$0023            ;
FBE1: BD FD 21      JSR   CalcOfst          ;
FBE4: DF 1D         STX   <$1D              ;
FBE6: 39            RTS                     ;
FBE7: 96 13         LDAA  <$13              ;
FBE9: 97 22         STAA  <$22              ;
FBEB: DE 1B         LDX   <$1B              ;
FBED: DF 0D         STX   <$0D              ;
FBEF: DE 0D         LDX   <$0D              ;
FBF1: A6 00         LDAA  $00,X             ;
FBF3: 9B 23         ADDA  <$23              ;
FBF5: 97 21         STAA  <$21              ;
FBF7: 9C 1D         CPX   <$1D              ;
FBF9: 27 26         BEQ   $FC21             ;
FBFB: D6 14         LDAB  <$14              ;
FBFD: 08            INX                     ;
FBFE: DF 0D         STX   <$0D              ;
FC00: CE 00 24      LDX   #$0024            ;
FC03: 96 21         LDAA  <$21              ;
FC05: 4A            DECA                    ;
FC06: 26 FD         BNE   $FC05             ;
FC08: A6 00         LDAA  $00,X             ;
FC0A: B7 04 00      STAA  >$0400            ;
FC0D: 08            INX                     ;
FC0E: 9C 1F         CPX   <$1F              ;
FC10: 26 F1         BNE   $FC03             ;
FC12: 5A            DECB                    ;
FC13: 27 DA         BEQ   $FBEF             ;
FC15: 08            INX                     ;
FC16: 09            DEX                     ;
FC17: 08            INX                     ;
FC18: 09            DEX                     ;
FC19: 08            INX                     ;
FC1A: 09            DEX                     ;
FC1B: 08            INX                     ;
FC1C: 09            DEX                     ;
FC1D: 01            NOP                     ;
FC1E: 01            NOP                     ;
FC1F: 20 DF         BRA   $FC00             ;
FC21: 96 15         LDAA  <$15              ;
FC23: 8D 62         BSR   $FC87             ;
FC25: 7A 00 22      DEC   >$0022            ;
FC28: 26 C1         BNE   $FBEB             ;
FC2A: 96 07         LDAA  <$07              ;
FC2C: 26 46         BNE   $FC74             ;
FC2E: 96 16         LDAA  <$16              ;
FC30: 27 42         BEQ   $FC74             ;
FC32: 7A 00 17      DEC   >$0017            ;
FC35: 27 3D         BEQ   $FC74             ;
FC37: 9B 23         ADDA  <$23              ;
FC39: 97 23         STAA  <$23              ; SUBRTN
FC3B: DE 1B         LDX   <$1B              ; SUBRTN
FC3D: 5F            CLRB                    ;
FC3E: 96 23         LDAA  <$23              ;
FC40: 7D 00 16      TST   >$0016            ;
FC43: 2B 06         BMI   $FC4B             ;
FC45: AB 00         ADDA  $00,X             ;
FC47: 25 08         BCS   $FC51             ;
FC49: 20 0B         BRA   $FC56             ;
FC4B: AB 00         ADDA  $00,X             ;
FC4D: 27 02         BEQ   $FC51             ;
FC4F: 25 05         BCS   $FC56             ;
FC51: 5D            TSTB                    ;
FC52: 27 08         BEQ   $FC5C             ;
FC54: 20 0F         BRA   $FC65             ;
FC56: 5D            TSTB                    ;
FC57: 26 03         BNE   $FC5C             ;
FC59: DF 1B         STX   <$1B              ;
FC5B: 5C            INCB                    ;
FC5C: 08            INX                     ;
FC5D: 9C 1D         CPX   <$1D              ;
FC5F: 26 DD         BNE   $FC3E             ;
FC61: 5D            TSTB                    ;
FC62: 26 01         BNE   $FC65             ;
FC64: 39            RTS                     ;

FC65: DF 1D         STX   <$1D              ;
FC67: 96 15         LDAA  <$15              ;
FC69: 27 06         BEQ   $FC71             ;
FC6B: 8D 08         BSR   $FC75             ;
FC6D: 96 1A         LDAA  <$1A              ;
FC6F: 8D 16         BSR   $FC87             ;
FC71: 7E FB E7      JMP   $FBE7             ;
FC74: 39            RTS                     ;

FC75: CE 00 24      LDX   #$0024            ; SUBRTN
FC78: DF 0F         STX   <$0F              ;
FC7A: DE 18         LDX   <$18              ;
FC7C: E6 00         LDAB  $00,X             ;
FC7E: 08            INX                     ;
FC7F: BD FB 0A      JSR   $FB0A             ;
FC82: DE 0F         LDX   <$0F              ;
FC84: DF 1F         STX   <$1F              ;
FC86: 39            RTS                     ;

FC87: 4D            TSTA                    ; SUBRTN
FC88: 27 2B         BEQ   $FCB5             ;
FC8A: DE 18         LDX   <$18              ;
FC8C: DF 0D         STX   <$0D              ;
FC8E: CE 00 24      LDX   #$0024            ;
FC91: 97 12         STAA  <$12              ;
FC93: DF 0F         STX   <$0F              ;
FC95: DE 0D         LDX   <$0D              ;
FC97: D6 12         LDAB  <$12              ;
FC99: D7 11         STAB  <$11              ;
FC9B: E6 01         LDAB  $01,X             ;
FC9D: 54            LSRB                    ;
FC9E: 54            LSRB                    ;
FC9F: 54            LSRB                    ;
FCA0: 54            LSRB                    ;
FCA1: 08            INX                     ;
FCA2: DF 0D         STX   <$0D              ;
FCA4: DE 0F         LDX   <$0F              ;
FCA6: A6 00         LDAA  $00,X             ;
FCA8: 10            SBA                     ;
FCA9: 7A 00 11      DEC   >$0011            ;
FCAC: 26 FA         BNE   $FCA8             ;
FCAE: A7 00         STAA  $00,X             ;
FCB0: 08            INX                     ;
FCB1: 9C 1F         CPX   <$1F              ;
FCB3: 26 DE         BNE   $FC93             ;
FCB5: 39            RTS                     ;

Interrupt request handler

IRQ:
FCB6: 8E 00 7F      LDS   #$007F            ;VECTOR at $FFF8, toss int return values out
FCB9: B6 04 02      LDAA  >$0402            ;read in from PIA channel B
FCBC: 0E            CLI                     ;
FCBD: 43            COMA                    ;flip the bits just read
FCBE: 84 1F         ANDA  #$1F              ;mask out upper 3 bits
FCC0: D6 08         LDAB  <$08              ;
FCC2: 27 09         BEQ   $FCCD             ;
FCC4: 2A 03         BPL   $FCC9             ;
FCC6: BD FA 48      JSR   $FA48             ;do this if negative
FCC9: 4A            DECA                    ;start here greater that zero
FCCA: BD FA 89      JSR   $FA89             ;
FCCD: 5F            CLRB                    ;jump here if it's zero
FCCE: 81 0E         CMPA  #$0E              ;
FCD0: 27 02         BEQ   $FCD4             ;
FCD2: D7 06         STAB  <$06              ;
FCD4: 81 12         CMPA  #$12              ;
FCD6: 27 02         BEQ   $FCDA             ;
FCD8: D7 07         STAB  <$07              ;
FCDA: F6 EF FD      LDAB  >$EFFD            ; ???
FCDD: C1 7E         CMPB  #$7E              ;
FCDF: 26 03         BNE   $FCE4             ;
FCE1: BD EF FD      JSR   $EFFD             ; ???
FCE4: 4D            TSTA                    ;
FCE5: 27 27         BEQ   $FD0E             ;
FCE7: 4A            DECA                    ;
FCE8: 81 0C         CMPA  #$0C              ;
FCEA: 22 08         BHI   $FCF4             ;
FCEC: BD FB 81      JSR   $FB81             ;
FCEF: BD FB E7      JSR   $FBE7             ;
FCF2: 20 1A         BRA   $FD0E             ;
FCF4: 81 1B         CMPA  #$1B              ;
FCF6: 22 0E         BHI   $FD06             ;
FCF8: 80 0D         SUBA  #$0D              ;
FCFA: 48            ASLA                    ;x 2 for an offset into the table
FCFB: CE FD 58      LDX   #$FD58            ;address of VectorTblW table
FCFE: 8D 21         BSR   CalcOfst          ;calculate offset into the table
FD00: EE 00         LDX   $00,X             ;load the vector address from table
FD02: AD 00         JSR   $00,X             ;call the subroutine
FD04: 20 08         BRA   $FD0E             ;
FD06: 80 1C         SUBA  #$1C              ;
FD08: BD F8 2A      JSR   $F82A             ;
FD0B: BD F8 3F      JSR   $F83F             ;

FD0E: 96 04         LDAA  <$04              ;
FD10: 9A 05         ORAA  <$05              ;
FD12: 27 FE         BEQ   $FD12             ;
FD14: 4F            CLRA                    ;
FD15: 97 07         STAA  <$07              ;
FD17: 96 04         LDAA  <$04              ;
FD19: 27 03         BEQ   $FD1E             ;
FD1B: 7E F9 13      JMP   $F913             ;
FD1E: 7E FB 34      JMP   $FB34             ;

This subroutine calculates the unsigned offset of A + X and places the result in the X reg. The A reg is mangled by this function.

CalcOfst:
FD21: DF 0D         STX   <$0D              ;SUBRTN, store index base value
FD23: 9B 0E         ADDA  <$0E              ;add A reg to LSB of index base value
FD25: 97 0E         STAA  <$0E              ;store that in same
FD27: 24 03         BCC   $FD2C             ;if no carry, go on out of here
FD29: 7C 00 0D      INC   >$000D            ;otherwise, inc the MSB of index base value. Why extended addressing mode?
FD2C: DE 0D         LDX   <$0D              ;load up the modified index value
FD2E: 39            RTS                     ;

NMI:
FD2F: 0F            SEI                     ; VECTOR at $FFFC
FD30: 8E 00 7F      LDS   #$007F            ;
FD33: CE FF FF      LDX   #$FFFF            ;
FD36: 5F            CLRB                    ;
FD37: E9 00         ADCB  $00,X             ;
FD39: 09            DEX                     ;
FD3A: 8C F8 00      CPX   #$F800            ;
FD3D: 26 F8         BNE   $FD37             ;
FD3F: E1 00         CMPB  $00,X             ;
FD41: 27 01         BEQ   $FD44             ;
FD43: 3E            WAI                     ;
FD44: 86 01         LDAA  #$01              ;
FD46: BD F8 2A      JSR   $F82A             ;
FD49: BD F8 3F      JSR   $F83F             ;
FD4C: F6 EF FA      LDAB  >$EFFA            ; ???
FD4F: C1 7E         CMPB  #$7E              ;
FD51: 26 DC         BNE   NMI               ;
FD53: BD EF FA      JSR   $EFFA             ; ???
FD56: 20 D7         BRA   NMI               ;

W vector table here

VectorTblW:
FD58: FB 49         ; $FB49
FD5A: F9 13         ; $F913
FD5C: FB 24         ; $FB24
FD5E: F8 8C         ; $F88C
FD60: FB 71         ; $FB71
FD62: FB 1E         ; $FB1E
FD64: F8 CD         ; $F8CD
FD66: F8 94         ; $F894
FD68: F9 1C         ; $F91C
FD6A: F9 23         ; $F923
FD6C: F9 A6         ; $F9A6
FD6E: F9 D4         ; $F9D4
FD70: F9 F3         ; $F9F3
FD72: FA 44         ; $FA44
FD74: FA 84         ; $FA84

FD76:  40 01 00 10 E1 00 80 FF FF 28
FD80:  01 00 08 81 02 00 FF FF 28 81 00 FC 01 02 00 FC
FD90:  FF FF 01 00 18 41 04 80 00 FF 8C 5B B6 40 BF 49
FDA0:  A4 73 73 A4 49 BF 40 B6 5B 8C 0C 7F 1D 0F FB 7F
FDB0:  23 0F 15 FE 08 50 8B 88 3E 3F 02 3E 7C 04 03 FF
FDC0:  3E 3F 2C E2 7C 12 0D 74 7C 0D 0E 41 7C 23 0B 50
FDD0:  7C 1D 29 F2 7C 3F 02 3E F8 04 03 FF 7C 3F 2C E2
FDE0:  F8 12 0D 74 F8 0D 0E 41 F8 23 0B 50 F8 1D 2F F2
FDF0:  F8 23 05 A8 F8 12 06 BA F8 04 07 FF 7C 37 04 C1
FE00:  7C 23 05 A8 7C 12 06 BA 3E 04 07 FF 3E 37 04 C1
FE10:  3E 23 05 A8 1F 12 06 BA 1F 04 07 FF 1F 37 04 C1
FE20:  1F 23 16 A0 FE 1D 17 F9 7F 37 13 06 7F 3F 08 FA
FE30:  FE 04 0F FF FE 0D 0E 41 FE 23 0B 50 FE 1D 5F E4
FE40:  00 47 3F 37 30 29 23 1D 17 12 0D 08 04 08 7F D9
FE50:  FF D9 7F 24 00 24 08 00 40 80 00 FF 00 80 40 10
FE60:  7F B0 D9 F5 FF F5 D9 B0 7F 4E 24 09 00 09 24 4E
FE70:  10 7F C5 EC E7 BF 8D 6D 6A 7F 94 92 71 40 17 12
FE80:  39 10 FF FF FF FF 00 00 00 00 FF FF FF FF 00 00
FE90:  00 00 48 8A 95 A0 AB B5 BF C8 D1 DA E1 E8 EE F3
FEA0:  F7 FB FD FE FF FE FD FB F7 F3 EE E8 E1 DA D1 C8
FEB0:  BF B5 AB A0 95 8A 7F 75 6A 5F 54 4A 40 37 2E 25
FEC0:  1E 17 11 0C 08 04 02 01 00 01 02 04 08 0C 11 17
FED0:  1E 25 2E 37 40 4A 54 5F 6A 75 7F 10 59 7B 98 AC
FEE0:  B3 AC 98 7B 59 37 19 06 00 06 19 37 81 24 00 00
FEF0:  00 16 31 12 05 1A FF 00 27 6D 11 05 11 01 0F 01
FF00:  47 11 31 00 01 00 0D 1B F4 12 00 00 00 14 47 41
FF10:  45 00 00 00 0F 5B 21 35 11 FF 00 0D 1B 15 00 00
FF20:  FD 00 01 69 31 11 00 01 00 03 6A 01 15 01 01 01
FF30:  01 47 F6 53 03 00 02 06 94 6A 10 02 00 02 06 9A
FF40:  1F 12 00 FF 10 04 69 31 11 00 FF 00 0D 00 12 06
FF50:  00 FF 01 09 28 A0 98 90 88 80 78 70 68 60 58 50
FF60:  44 40 01 01 02 02 04 04 08 08 10 10 30 60 C0 E0
FF70:  01 01 02 02 03 04 05 06 07 08 09 0A 0C 80 7C 78
FF80:  74 70 74 78 7C 80 01 01 02 02 04 04 08 08 10 20
FF90:  28 30 38 40 48 50 60 70 80 A0 B0 C0 08 40 08 40
FFA0:  08 40 08 40 08 40 08 40 08 40 08 40 08 40 08 40
FFB0:  01 02 04 08 09 0A 0B 0C 0E 0F 10 12 14 16 40 10
FFC0:  08 01 01 01 01 01 02 02 03 03 04 04 05 06 08 0A
FFD0:  0C 10 14 18 20 30 40 50 40 30 20 10 0C 0A 08 07
FFE0:  06 05 04 03 02 02 01 01 01 07 08 09 0A 0C 08 17
FFF0:  18 19 1A 1B 1C 00 00 00 

Motorola vector table settings

FFF8: FC B6  ; IRQ
FFFA: F8 01  ; SWI (not used -- mapped to RESET)
FFFC: FD 2F  ; NMI
FFFE: F8 01  ; RESET
```