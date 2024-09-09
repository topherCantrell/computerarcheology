![Bank 5](KidIcarus.jpg)

# Bank 5

>>> cpu 6502

>>> binary 8000:roms/KidIcarus.nes[14010:18010]

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](Hardware.md)

```code
8000: 4C 5A 80        JMP     $805A               ; {}
8003: 4C D1 80        JMP     $80D1               ; {}
8006: 4C AA 8D        JMP     $8DAA               ; {}
8009: 4C 40 DF        JMP     $DF40               
800C: 4C 73 8B        JMP     $8B73               ; {}
800F: 4C 74 8B        JMP     $8B74               ; {}
8012: 4C 0B 8B        JMP     $8B0B               ; {}
8015: 4C 76 93        JMP     $9376               ; {}
8018: 4C 88 8F        JMP     $8F88               ; {}
801B: 4C A4 84        JMP     $84A4               ; {}
801E: 4C AC 92        JMP     $92AC               ; {}
8021: 4C EA 8A        JMP     $8AEA               ; {}
8024: 4C 8D 80        JMP     $808D               ; {}
8027: 4C 4D 81        JMP     $814D               ; {}
802A: 4C 43 81        JMP     $8143               ; {}
802D: 4C AB 8D        JMP     $8DAB               ; {}
8030: 4C B5 8D        JMP     $8DB5               ; {}
8033: 4C 48 8C        JMP     $8C48               ; {}
8036: 4C 19 8D        JMP     $8D19               ; {}
8039: 4C F8 8B        JMP     $8BF8               ; {}
803C: 4C 12 8C        JMP     $8C12               ; {}
803F: 4C 8B 84        JMP     $848B               ; {}
8042: 67 ; ????
8043: C5 E7           CMP     $E7                 
8045: C5 60           CMP     $60                 
8047: 81 80           STA     ($80,X)             
8049: 81 BC           STA     ($BC,X)             
804B: 81 BC           STA     ($BC,X)             
804D: 81 C0           STA     ($C0,X)             
804F: 81 AC           STA     ($AC,X)             
8051: 81 E4           STA     ($E4,X)             
8053: 81 14           STA     ($14,X)             
8055: 82 ; ????
8056: 21 70           AND     ($70,X)             
8058: 43 ; ????
8059: 72 ; ????
805A: 20 07 EB        JSR     $EB07               
805D: 20 F0 EE        JSR     $EEF0               
8060: 20 E5 EE        JSR     $EEE5               
8063: 20 06 70        JSR     $7006               
8066: 20 2A C4        JSR     $C42A               
8069: A9 20           LDA     #$20                
806B: 20 27 EF        JSR     $EF27               
806E: A9 28           LDA     #$28                
8070: 20 27 EF        JSR     $EF27               
8073: 20 21 7F        JSR     $7F21               
8076: 20 42 EE        JSR     $EE42               
8079: 20 2E EF        JSR     $EF2E               
807C: 20 CA EE        JSR     $EECA               
807F: A9 08           LDA     #$08                
8081: 20 90 CA        JSR     $CA90               
8084: 20 43 81        JSR     $8143               ; {}
8087: 20 53 C4        JSR     $C453               
808A: 20 76 93        JSR     $9376               ; {}
808D: A9 60           LDA     #$60                
808F: 85 43           STA     $43                 
8091: 20 01 EF        JSR     $EF01               
8094: 20 21 EB        JSR     $EB21               
8097: 24 AB           BIT     $AB                 
8099: 70 0E           BVS     $80A9               ; {}
809B: 30 0F           BMI     $80AC               ; {}
809D: 20 98 E1        JSR     $E198               
80A0: 20 D7 EA        JSR     $EAD7               
80A3: 20 F0 90        JSR     $90F0               ; {}
80A6: 4C 94 80        JMP     $8094               ; {}
80A9: 4C A0 C0        JMP     $C0A0               
80AC: 20 F0 EE        JSR     $EEF0               
80AF: 20 89 EA        JSR     $EA89               
80B2: E6 A0           INC     $A0                 
80B4: A0 00           LDY     #$00                
80B6: A5 A0           LDA     $A0                 
80B8: C9 08           CMP     #$08                
80BA: D0 01           BNE     $80BD               ; {}
80BC: EA              NOP                         
80BD: 84 38           STY     $38                 
80BF: 4C 6D C0        JMP     $C06D               
80C2: 20 9B EE        JSR     $EE9B               
80C5: 20 0E EE        JSR     $EE0E               
80C8: 20 B8 EE        JSR     $EEB8               
80CB: 4C F2 80        JMP     $80F2               ; {}
80CE: 4C 05 81        JMP     $8105               ; {}
80D1: 8A              TXA                         
80D2: 48              PHA                         
80D3: 98              TYA                         
80D4: 48              PHA                         
80D5: A5 45           LDA     $45                 
80D7: D0 F5           BNE     $80CE               ; {}
80D9: E6 45           INC     $45                 
80DB: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
80DE: 20 2E EB        JSR     $EB2E               
80E1: A5 38           LDA     $38                 
80E3: D0 DD           BNE     $80C2               ; {}
80E5: A5 37           LDA     $37                 
80E7: D0 21           BNE     $810A               ; {}
80E9: 20 42 EE        JSR     $EE42               
80EC: 20 B6 CB        JSR     $CBB6               
80EF: 20 C9 EB        JSR     $EBC9               
80F2: 20 5D E1        JSR     $E15D               
80F5: 20 E0 C3        JSR     $C3E0               
80F8: 20 6A EE        JSR     $EE6A               
80FB: 20 94 EE        JSR     $EE94               
80FE: 20 56 C8        JSR     $C856               
8101: A9 00           LDA     #$00                
8103: 85 45           STA     $45                 
8105: 68              PLA                         
8106: A8              TAY                         
8107: 68              PLA                         
8108: AA              TAX                         
8109: 60              RTS                         
810A: 4A              LSR     A                   
810B: B0 E5           BCS     $80F2               ; {}
810D: 4A              LSR     A                   
810E: B0 09           BCS     $8119               ; {}
8110: 20 42 EE        JSR     $EE42               
8113: 20 F7 E0        JSR     $E0F7               
8116: 4C EF 80        JMP     $80EF               ; {}
8119: 4A              LSR     A                   
811A: B0 F4           BCS     $8110               ; {}
811C: A9 0A           LDA     #$0A                
811E: 20 90 CA        JSR     $CA90               
8121: A9 0C           LDA     #$0C                
8123: 20 90 CA        JSR     $CA90               
8126: 20 B9 8F        JSR     $8FB9               ; {}
8129: 20 AE 8B        JSR     $8BAE               ; {}
812C: 20 C9 EB        JSR     $EBC9               
812F: 20 9B EE        JSR     $EE9B               
8132: A9 02           LDA     #$02                
8134: 20 90 CA        JSR     $CA90               
8137: 20 BD 92        JSR     $92BD               ; {}
813A: 20 B3 EC        JSR     $ECB3               
813D: 20 B8 EE        JSR     $EEB8               
8140: 4C F2 80        JMP     $80F2               ; {}
8143: 20 4D 81        JSR     $814D               ; {}
8146: 20 43 D3        JSR     $D343               
8149: 20 CD 89        JSR     $89CD               ; {}
814C: 60              RTS                         
814D: A2 20           LDX     #$20                
814F: A9 7A           LDA     #$7A                
8151: 9D 00 07        STA     $0700,X             
8154: A9 80           LDA     #$80                
8156: 9D 03 07        STA     $0703,X             
8159: 0A              ASL     A                   
815A: 9D 02 07        STA     $0702,X             
815D: 4C BF C3        JMP     $C3BF               
8160: 01 A0           ORA     ($A0,X)             
8162: A1 A2           LDA     ($A2,X)             
8164: A3 ; ????
8165: A4 A5           LDY     $A5                 
8167: 00              BRK                         
8168: 41 A1           EOR     ($A1,X)             
816A: A0 A3           LDY     #$A3                
816C: A2 A5           LDX     #$A5                
816E: A4 00           LDY     $00                 ; {ram.GP_00}
8170: 01 A0           ORA     ($A0,X)             
8172: A1 A2           LDA     ($A2,X)             
8174: A3 ; ????
8175: A6 A7           LDX     $A7                 
8177: 00              BRK                         
8178: 41 A1           EOR     ($A1,X)             
817A: A0 A3           LDY     #$A3                
817C: A2 A7           LDX     #$A7                
817E: A6 00           LDX     $00                 ; {ram.GP_00}
8180: 4B ; ????
8181: 4B ; ????
8182: 4B ; ????
8183: 4B ; ????
8184: 5A ; ????
8185: 5A ; ????
8186: 5A ; ????
8187: 5A ; ????
8188: 4A              LSR     A                   
8189: 4A              LSR     A                   
818A: 4A              LSR     A                   
818B: 4A              LSR     A                   
818C: 95 5F           STA     $5F,X               
818E: 96 5F           STX     $5F,Y               
8190: 9B ; ????
8191: 5F ; ????
8192: 9C ; ????
8193: 5F ; ????
8194: 3F ; ????
8195: 5F ; ????
8196: 4F ; ????
8197: 5F ; ????
8198: 48              PHA                         
8199: 5F ; ????
819A: 58              CLI                         
819B: 5F ; ????
819C: 49 5F           EOR     #$5F                
819E: 59 5F AA        EOR     $AA5F,Y             ; {}
81A1: 5F ; ????
81A2: AB ; ????
81A3: 5F ; ????
81A4: 34 ; ????
81A5: 5F ; ????
81A6: 55 5F           EOR     $5F,X               
81A8: 43 ; ????
81A9: 5F ; ????
81AA: 44 ; ????
81AB: 5F ; ????
81AC: 00              BRK                         
81AD: 6A              ROR     A                   
81AE: 6B ; ????
81AF: 6C 6D 6E        JMP     ($6E6D)             
81B2: 6F ; ????
81B3: 00              BRK                         
81B4: 40              RTI                         
81B5: 6B ; ????
81B6: 6A              ROR     A                   
81B7: 6D 6C 6F        ADC     $6F6C               
81BA: 6E 00 00        ROR     $0000               ; {ram.GP_00}
81BD: 00              BRK                         
81BE: 00              BRK                         
81BF: 00              BRK                         
81C0: 9F ; ????
81C1: 5F ; ????
81C2: AF ; ????
81C3: 5F ; ????
81C4: 8E 5F 8F        STX     $8F5F               ; {}
81C7: 5F ; ????
81C8: 34 ; ????
81C9: 5F ; ????
81CA: 8F ; ????
81CB: 5F ; ????
81CC: 52 ; ????
81CD: 5F ; ????
81CE: 53 ; ????
81CF: 5F ; ????
81D0: B8              CLV                         
81D1: B9 BB BC        LDA     $BCBB,Y             ; {}
81D4: B9 B8 BC        LDA     $BCB8,Y             ; {}
81D7: BB ; ????
81D8: B8              CLV                         
81D9: BA              TSX                         
81DA: BB ; ????
81DB: BC BA B8        LDY     $B8BA,X             ; {}
81DE: BC BB 38        LDY     $38BB,X             
81E1: 5F ; ????
81E2: 39 5F 7F        AND     $7F5F,Y             
81E5: 00              BRK                         
81E6: 00              BRK                         
81E7: 00              BRK                         
81E8: 7F ; ????
81E9: 00              BRK                         
81EA: 00              BRK                         
81EB: 00              BRK                         
81EC: 7F ; ????
81ED: 00              BRK                         
81EE: 00              BRK                         
81EF: 00              BRK                         
81F0: FC ; ????
81F1: 27 ; ????
81F2: 01 00           ORA     ($00,X)             ; {ram.GP_00}
81F4: F8              SED                         
81F5: 94 01           STY     $01,X               
81F7: 00              BRK                         
81F8: 7F ; ????
81F9: 00              BRK                         
81FA: 00              BRK                         
81FB: 00              BRK                         
81FC: 00              BRK                         
81FD: AE 01 00        LDX     $0001               
8200: 7F ; ????
8201: 00              BRK                         
8202: 00              BRK                         
8203: 00              BRK                         
8204: F8              SED                         
8205: 5B ; ????
8206: 00              BRK                         
8207: FC ; ????
8208: F8              SED                         
8209: 5B ; ????
820A: 40              RTI                         
820B: 04 ; ????
820C: 00              BRK                         
820D: 5C ; ????
820E: 00              BRK                         
820F: FC ; ????
8210: 00              BRK                         
8211: 5C ; ????
8212: 40              RTI                         
8213: 04 ; ????
8214: 00              BRK                         
8215: 88              DEY                         
8216: 22 ; ????
8217: 00              BRK                         
8218: 00              BRK                         
8219: 89 ; ????
821A: 22 ; ????
821B: 00              BRK                         
821C: 00              BRK                         
821D: 89 ; ????
821E: 22 ; ????
821F: 00              BRK                         
8220: 00              BRK                         
8221: 89 ; ????
8222: 22 ; ????
8223: 00              BRK                         
8224: 00              BRK                         
8225: 88              DEY                         
8226: A2 00           LDX     #$00                
8228: 00              BRK                         
8229: 89 ; ????
822A: A2 00           LDX     #$00                
822C: 00              BRK                         
822D: 89 ; ????
822E: A2 00           LDX     #$00                
8230: 00              BRK                         
8231: 89 ; ????
8232: A2 00           LDX     #$00                
8234: 00              BRK                         
8235: 97 ; ????
8236: 22 ; ????
8237: 00              BRK                         
8238: 00              BRK                         
8239: 98              TYA                         
823A: 22 ; ????
823B: 00              BRK                         
823C: 00              BRK                         
823D: 98              TYA                         
823E: 22 ; ????
823F: 00              BRK                         
8240: 00              BRK                         
8241: 98              TYA                         
8242: 22 ; ????
8243: 00              BRK                         
8244: 00              BRK                         
8245: 97 ; ????
8246: 62 ; ????
8247: 00              BRK                         
8248: 00              BRK                         
8249: 98              TYA                         
824A: 62 ; ????
824B: 00              BRK                         
824C: 00              BRK                         
824D: 98              TYA                         
824E: 62 ; ????
824F: 00              BRK                         
8250: 00              BRK                         
8251: 98              TYA                         
8252: 62 ; ????
8253: 00              BRK                         
8254: F8              SED                         
8255: BB ; ????
8256: 83 ; ????
8257: FC ; ????
8258: F8              SED                         
8259: BC 83 04        LDY     $0483,X             
825C: 00              BRK                         
825D: B8              CLV                         
825E: 83 ; ????
825F: FC ; ????
8260: 00              BRK                         
8261: B9 83 04        LDA     $0483,Y             
8264: 00              BRK                         
8265: 00              BRK                         
8266: 00              BRK                         
8267: 00              BRK                         
8268: 00              BRK                         
8269: 00              BRK                         
826A: 00              BRK                         
826B: 00              BRK                         
826C: 00              BRK                         
826D: 00              BRK                         
826E: 00              BRK                         
826F: 00              BRK                         
8270: 00              BRK                         
8271: 00              BRK                         
8272: 00              BRK                         
8273: 00              BRK                         
8274: F8              SED                         
8275: 5D 00 FC        EOR     $FC00,X             
8278: F8              SED                         
8279: 5D 40 04        EOR     $0440,X             
827C: 00              BRK                         
827D: 5E 00 FC        LSR     $FC00,X             
8280: 00              BRK                         
8281: 5E 40 04        LSR     $0440,X             
8284: 00              BRK                         
8285: 00              BRK                         
8286: 00              BRK                         
8287: 00              BRK                         
8288: 00              BRK                         
8289: 00              BRK                         
828A: 00              BRK                         
828B: 00              BRK                         
828C: 00              BRK                         
828D: 00              BRK                         
828E: 00              BRK                         
828F: 00              BRK                         
8290: 00              BRK                         
8291: 00              BRK                         
8292: 00              BRK                         
8293: 00              BRK                         
8294: F8              SED                         
8295: 52 ; ????
8296: 00              BRK                         
8297: 04 ; ????
8298: 7F ; ????
8299: 00              BRK                         
829A: 00              BRK                         
829B: 00              BRK                         
829C: 00              BRK                         
829D: 52 ; ????
829E: 80 ; ????
829F: 04 ; ????
82A0: 7F ; ????
82A1: 00              BRK                         
82A2: 00              BRK                         
82A3: 00              BRK                         
82A4: 00              BRK                         
82A5: 00              BRK                         
82A6: 00              BRK                         
82A7: 00              BRK                         
82A8: 00              BRK                         
82A9: 00              BRK                         
82AA: 00              BRK                         
82AB: 00              BRK                         
82AC: 00              BRK                         
82AD: 00              BRK                         
82AE: 00              BRK                         
82AF: 00              BRK                         
82B0: 00              BRK                         
82B1: 00              BRK                         
82B2: 00              BRK                         
82B3: 00              BRK                         
82B4: F8              SED                         
82B5: 92 ; ????
82B6: 01 FD           ORA     ($FD,X)             
82B8: F8              SED                         
82B9: 94 01           STY     $01,X               
82BB: 03 ; ????
82BC: 00              BRK                         
82BD: 93 ; ????
82BE: 01 FD           ORA     ($FD,X)             
82C0: 00              BRK                         
82C1: AE 01 03        LDX     $0301               
82C4: 20 E3 82        JSR     $82E3               ; {}
82C7: 4A              LSR     A                   
82C8: 4A              LSR     A                   
82C9: 4A              LSR     A                   
82CA: 4A              LSR     A                   
82CB: C9 0F           CMP     #$0F                
82CD: F0 11           BEQ     $82E0               ; {}
82CF: 20 2B EE        JSR     $EE2B               
82D2: EB ; ????
82D3: 82 ; ????
82D4: 96 83           STX     $83,Y               
82D6: A1 83           LDA     ($83,X)             
82D8: 5D 83 60        EOR     $6083,X             
82DB: 83 ; ????
82DC: 89 ; ????
82DD: 83 ; ????
82DE: 85 83           STA     $83                 
82E0: 4C 00 70        JMP     $7000               
82E3: A5 46           LDA     $46                 
82E5: 29 3F           AND     #$3F                
82E7: A8              TAY                         
82E8: B9 2F 71        LDA     $712F,Y             
82EB: 60              RTS                         
82EC: 20 E3 82        JSR     $82E3               ; {}
82EF: 4A              LSR     A                   
82F0: 4A              LSR     A                   
82F1: 4A              LSR     A                   
82F2: 4A              LSR     A                   
82F3: C9 0F           CMP     #$0F                
82F5: F0 16           BEQ     $830D               ; {}
82F7: 48              PHA                         
82F8: 20 CE 89        JSR     $89CE               ; {}
82FB: 68              PLA                         
82FC: 20 2B EE        JSR     $EE2B               
82FF: 16 83           ASL     $83,X               
8301: A7 ; ????
8302: 83 ; ????
8303: A7 ; ????
8304: 83 ; ????
8305: 63 ; ????
8306: 83 ; ????
8307: 63 ; ????
8308: 83 ; ????
8309: 7F ; ????
830A: 83 ; ????
830B: 8A              TXA                         
830C: 83 ; ????
830D: 20 07 97        JSR     $9707               ; {}
8310: 20 64 99        JSR     $9964               ; {}
8313: 4C 03 70        JMP     $7003               
8316: 20 1C 83        JSR     $831C               ; {}
8319: 4C AB 94        JMP     $94AB               ; {}
831C: AD C1 07        LDA     $07C1               
831F: 0D C9 07        ORA     $07C9               
8322: 0D D1 07        ORA     $07D1               
8325: 0D D9 07        ORA     $07D9               
8328: F0 09           BEQ     $8333               ; {}
832A: 4C F4 84        JMP     $84F4               ; {}
832D: A9 00           LDA     #$00                
832F: 8D E0 04        STA     $04E0               
8332: 60              RTS                         
8333: A2 C0           LDX     #$C0                
8335: 20 E4 84        JSR     $84E4               ; {}
8338: 20 53 E0        JSR     $E053               
833B: AD D5 04        LDA     $04D5               
833E: C9 6F           CMP     #$6F                
8340: D0 EB           BNE     $832D               ; {}
8342: BD 00 07        LDA     $0700,X             
8345: 8D E0 04        STA     $04E0               
8348: BD 03 07        LDA     $0703,X             
834B: 8D E1 04        STA     $04E1               
834E: A9 10           LDA     #$10                
8350: 8D C1 07        STA     $07C1               
8353: 8D C9 07        STA     $07C9               
8356: 8D D1 07        STA     $07D1               
8359: 8D D9 07        STA     $07D9               
835C: 60              RTS                         
835D: 4C 6C 83        JMP     $836C               ; {}
8360: 4C 7B 83        JMP     $837B               ; {}
8363: 20 F0 85        JSR     $85F0               ; {}
8366: 20 AB 94        JSR     $94AB               ; {}
8369: 4C 1C 83        JMP     $831C               ; {}
836C: A9 38           LDA     #$38                
836E: 8D 71 07        STA     $0771               
8371: 8D 91 07        STA     $0791               
8374: 8D 61 07        STA     $0761               
8377: 8D 81 07        STA     $0781               
837A: 60              RTS                         
837B: A9 40           LDA     #$40                
837D: D0 EF           BNE     $836E               ; {}
837F: 20 C9 88        JSR     $88C9               ; {}
8382: 4C 90 83        JMP     $8390               ; {}
8385: A9 68           LDA     #$68                
8387: D0 EB           BNE     $8374               ; {}
8389: 60              RTS                         
838A: 20 C4 87        JSR     $87C4               ; {}
838D: 20 4E 87        JSR     $874E               ; {}
8390: 20 1C 83        JSR     $831C               ; {}
8393: 4C AB 94        JMP     $94AB               ; {}
8396: A2 60           LDX     #$60                
8398: A9 48           LDA     #$48                
839A: 85 00           STA     $00                 ; {ram.GP_00}
839C: A9 12           LDA     #$12                
839E: 4C 90 CA        JMP     $CA90               
83A1: A2 60           LDX     #$60                
83A3: A9 50           LDA     #$50                
83A5: D0 F3           BNE     $839A               ; {}
83A7: A2 60           LDX     #$60                
83A9: 20 CC 83        JSR     $83CC               ; {}
83AC: A2 70           LDX     #$70                
83AE: 20 CC 83        JSR     $83CC               ; {}
83B1: A2 80           LDX     #$80                
83B3: 20 CC 83        JSR     $83CC               ; {}
83B6: A2 90           LDX     #$90                
83B8: 20 CC 83        JSR     $83CC               ; {}
83BB: A2 A0           LDX     #$A0                
83BD: 20 CC 83        JSR     $83CC               ; {}
83C0: A2 B0           LDX     #$B0                
83C2: 20 CC 83        JSR     $83CC               ; {}
83C5: A2 C0           LDX     #$C0                
83C7: 20 CC 83        JSR     $83CC               ; {}
83CA: A2 D0           LDX     #$D0                
83CC: BD 01 07        LDA     $0701,X             
83CF: F0 3B           BEQ     $840C               ; {}
83D1: 29 07           AND     #$07                
83D3: 20 2B EE        JSR     $EE2B               
83D6: DE 83 E3        DEC     $E383,X             
83D9: 83 ; ????
83DA: E8              INX                         
83DB: 83 ; ????
83DC: 65 DD           ADC     $DD                 
83DE: A9 14           LDA     #$14                
83E0: 4C 90 CA        JMP     $CA90               
83E3: A9 16           LDA     #$16                
83E5: 4C 90 CA        JMP     $CA90               
83E8: 20 90 D9        JSR     $D990               
83EB: 90 0F           BCC     $83FC               ; {}
83ED: 20 09 DA        JSR     $DA09               
83F0: 20 4A 84        JSR     $844A               ; {}
83F3: 20 C0 DB        JSR     $DBC0               
83F6: 20 0D 84        JSR     $840D               ; {}
83F9: 4C DE DC        JMP     $DCDE               
83FC: A9 F8           LDA     #$F8                
83FE: 99 00 07        STA     $0700,Y             
8401: A9 80           LDA     #$80                
8403: 8D 80 03        STA     $0380               
8406: 20 A9 DC        JSR     $DCA9               
8409: 4C 41 85        JMP     $8541               ; {}
840C: 60              RTS                         
840D: AD 2F 01        LDA     $012F               
8410: C9 01           CMP     #$01                
8412: F0 14           BEQ     $8428               ; {}
8414: C9 02           CMP     #$02                
8416: F0 27           BEQ     $843F               ; {}
8418: 20 E3 82        JSR     $82E3               ; {}
841B: 29 10           AND     #$10                
841D: D0 05           BNE     $8424               ; {}
841F: A0 05           LDY     #$05                
8421: 4C F5 86        JMP     $86F5               ; {}
8424: A0 04           LDY     #$04                
8426: D0 F9           BNE     $8421               ; {}
8428: 20 E3 82        JSR     $82E3               ; {}
842B: 29 10           AND     #$10                
842D: D0 0C           BNE     $843B               ; {}
842F: A0 06           LDY     #$06                
8431: A5 14           LDA     $14                 
8433: 29 08           AND     #$08                
8435: D0 01           BNE     $8438               ; {}
8437: C8              INY                         
8438: 4C 21 84        JMP     $8421               ; {}
843B: A0 04           LDY     #$04                
843D: D0 F2           BNE     $8431               ; {}
843F: 20 E3 82        JSR     $82E3               ; {}
8442: 29 10           AND     #$10                
8444: D0 F5           BNE     $843B               ; {}
8446: A0 0A           LDY     #$0A                
8448: D0 E7           BNE     $8431               ; {}
844A: BD 02 07        LDA     $0702,X             
844D: 29 0F           AND     #$0F                
844F: C9 08           CMP     #$08                
8451: B0 08           BCS     $845B               ; {}
8453: A9 D0           LDA     #$D0                
8455: 20 63 84        JSR     $8463               ; {}
8458: 4C 6D C7        JMP     $C76D               
845B: A9 30           LDA     #$30                
845D: 20 63 84        JSR     $8463               ; {}
8460: 4C 8D C7        JMP     $C78D               
8463: 85 08           STA     $08                 
8465: A9 C0           LDA     #$C0                
8467: 85 0A           STA     $0A                 
8469: A9 30           LDA     #$30                
846B: 85 09           STA     $09                 
846D: 60              RTS                         
846E: A9 F8           LDA     #$F8                
8470: 99 00 07        STA     $0700,Y             
8473: 20 A9 DC        JSR     $DCA9               
8476: BD 01 07        LDA     $0701,X             
8479: 29 F8           AND     #$F8                
847B: 09 03           ORA     #$03                
847D: 9D 01 07        STA     $0701,X             
8480: A9 FF           LDA     #$FF                
8482: 9D 02 07        STA     $0702,X             
8485: A9 08           LDA     #$08                
8487: 8D 81 03        STA     $0381               
848A: 60              RTS                         
848B: 98              TYA                         
848C: 48              PHA                         
848D: BD 01 07        LDA     $0701,X             
8490: 29 F8           AND     #$F8                
8492: 4A              LSR     A                   
8493: 4A              LSR     A                   
8494: 4A              LSR     A                   
8495: A8              TAY                         
8496: B9 21 72        LDA     $7221,Y             
8499: 9D 07 07        STA     $0707,X             
849C: A9 00           LDA     #$00                
849E: 9D 08 07        STA     $0708,X             
84A1: 68              PLA                         
84A2: A8              TAY                         
84A3: 60              RTS                         
84A4: BD 01 07        LDA     $0701,X             
84A7: 4A              LSR     A                   
84A8: 4A              LSR     A                   
84A9: 4A              LSR     A                   
84AA: A8              TAY                         
84AB: B9 32 72        LDA     $7232,Y             
84AE: 60              RTS                         
84AF: A5 15           LDA     $15                 
84B1: 29 03           AND     #$03                
84B3: C9 03           CMP     #$03                
84B5: D0 19           BNE     $84D0               ; {}
84B7: AD 23 07        LDA     $0723               
84BA: 38              SEC                         
84BB: FD 03 07        SBC     $0703,X             
84BE: B0 02           BCS     $84C2               ; {}
84C0: 49 FF           EOR     #$FF                
84C2: C9 04           CMP     #$04                
84C4: B0 0A           BCS     $84D0               ; {}
84C6: BD 01 07        LDA     $0701,X             
84C9: 29 F8           AND     #$F8                
84CB: 09 02           ORA     #$02                
84CD: 9D 01 07        STA     $0701,X             
84D0: 60              RTS                         
84D1: A9 10           LDA     #$10                
84D3: 9D 01 07        STA     $0701,X             
84D6: A9 02           LDA     #$02                
84D8: 9D 02 07        STA     $0702,X             
84DB: A9 00           LDA     #$00                
84DD: 9D 04 07        STA     $0704,X             
84E0: 9D 05 07        STA     $0705,X             
84E3: 60              RTS                         
84E4: A5 14           LDA     $14                 
84E6: 0A              ASL     A                   
84E7: 0A              ASL     A                   
84E8: 0A              ASL     A                   
84E9: 0A              ASL     A                   
84EA: 9D 00 07        STA     $0700,X             
84ED: AD 23 07        LDA     $0723               
84F0: 9D 03 07        STA     $0703,X             
84F3: 60              RTS                         
84F4: A2 C0           LDX     #$C0                
84F6: 20 05 85        JSR     $8505               ; {}
84F9: A2 C8           LDX     #$C8                
84FB: 20 05 85        JSR     $8505               ; {}
84FE: A2 D0           LDX     #$D0                
8500: 20 05 85        JSR     $8505               ; {}
8503: A2 D8           LDX     #$D8                
8505: BD 01 07        LDA     $0701,X             
8508: 29 F8           AND     #$F8                
850A: C9 10           CMP     #$10                
850C: D0 49           BNE     $8557               ; {}
850E: BD 01 07        LDA     $0701,X             
8511: 29 07           AND     #$07                
8513: 20 2B EE        JSR     $EE2B               
8516: 5B ; ????
8517: 85 1C           STA     $1C                 
8519: 85 B2           STA     $B2                 
851B: DE 20 53        DEC     $5320,X             
851E: E0 BD           CPX     #$BD                
8520: 00              BRK                         
8521: 07 ; ????
8522: C9 F8           CMP     #$F8                
8524: B0 32           BCS     $8558               ; {}
8526: 20 90 D9        JSR     $D990               
8529: 90 11           BCC     $853C               ; {}
852B: 20 E7 D9        JSR     $D9E7               
852E: 90 11           BCC     $8541               ; {}
8530: 20 09 DA        JSR     $DA09               
8533: 20 91 85        JSR     $8591               ; {}
8536: 20 C0 DB        JSR     $DBC0               
8539: 4C D5 C7        JMP     $C7D5               
853C: A9 F8           LDA     #$F8                
853E: 99 00 07        STA     $0700,Y             
8541: FE 01 07        INC     $0701,X             
8544: A9 FF           LDA     #$FF                
8546: 9D 02 07        STA     $0702,X             
8549: A9 08           LDA     #$08                
854B: 8D 81 03        STA     $0381               
854E: 20 A4 84        JSR     $84A4               ; {}
8551: 20 E1 E2        JSR     $E2E1               
8554: 20 F0 E2        JSR     $E2F0               
8557: 60              RTS                         
8558: 4C 2F DF        JMP     $DF2F               
855B: 8A              TXA                         
855C: 38              SEC                         
855D: E9 C0           SBC     #$C0                
855F: 0A              ASL     A                   
8560: 0A              ASL     A                   
8561: 0A              ASL     A                   
8562: 85 00           STA     $00                 ; {ram.GP_00}
8564: A5 14           LDA     $14                 
8566: 29 C0           AND     #$C0                
8568: C5 00           CMP     $00                 ; {ram.GP_00}
856A: F0 01           BEQ     $856D               ; {}
856C: 60              RTS                         
856D: AD E0 04        LDA     $04E0               
8570: 9D 00 07        STA     $0700,X             
8573: AD E1 04        LDA     $04E1               
8576: 9D 03 07        STA     $0703,X             
8579: 20 D1 84        JSR     $84D1               ; {}
857C: FE 01 07        INC     $0701,X             
857F: 60              RTS                         
8580: A0 6F           LDY     #$6F                
8582: AD 23 07        LDA     $0723               
8585: DD 03 07        CMP     $0703,X             
8588: 90 02           BCC     $858C               ; {}
858A: A0 60           LDY     #$60                
858C: 98              TYA                         
858D: 9D 02 07        STA     $0702,X             
8590: 60              RTS                         
8591: 20 87 D2        JSR     $D287               
8594: D0 EA           BNE     $8580               ; {}
8596: AD D3 04        LDA     $04D3               
8599: C9 40           CMP     #$40                
859B: 90 E3           BCC     $8580               ; {}
859D: A9 00           LDA     #$00                
859F: 9D 05 07        STA     $0705,X             
85A2: BD 02 07        LDA     $0702,X             
85A5: 29 0F           AND     #$0F                
85A7: C9 08           CMP     #$08                
85A9: B0 0B           BCS     $85B6               ; {}
85AB: AD D5 04        LDA     $04D5               
85AE: C9 40           CMP     #$40                
85B0: B0 0B           BCS     $85BD               ; {}
85B2: A9 03           LDA     #$03                
85B4: D0 D7           BNE     $858D               ; {}
85B6: AD D6 04        LDA     $04D6               
85B9: C9 40           CMP     #$40                
85BB: B0 F5           BCS     $85B2               ; {}
85BD: A9 0C           LDA     #$0C                
85BF: D0 CC           BNE     $858D               ; {}
85C1: A9 02           LDA     #$02                
85C3: 9D 02 07        STA     $0702,X             
85C6: 20 8B 84        JSR     $848B               ; {}
85C9: 20 E3 82        JSR     $82E3               ; {}
85CC: 29 0F           AND     #$0F                
85CE: 0A              ASL     A                   
85CF: 0A              ASL     A                   
85D0: 85 00           STA     $00                 ; {ram.GP_00}
85D2: 8A              TXA                         
85D3: 38              SEC                         
85D4: E9 60           SBC     #$60                
85D6: 4A              LSR     A                   
85D7: 4A              LSR     A                   
85D8: 4A              LSR     A                   
85D9: 4A              LSR     A                   
85DA: 18              CLC                         
85DB: 65 00           ADC     $00                 ; {ram.GP_00}
85DD: A8              TAY                         
85DE: B9 6F 71        LDA     $716F,Y             
85E1: 48              PHA                         
85E2: 29 F0           AND     #$F0                
85E4: 9D 00 07        STA     $0700,X             
85E7: 68              PLA                         
85E8: 0A              ASL     A                   
85E9: 0A              ASL     A                   
85EA: 0A              ASL     A                   
85EB: 0A              ASL     A                   
85EC: 9D 03 07        STA     $0703,X             
85EF: 60              RTS                         
85F0: A2 60           LDX     #$60                
85F2: 20 05 86        JSR     $8605               ; {}
85F5: A2 70           LDX     #$70                
85F7: 20 05 86        JSR     $8605               ; {}
85FA: A2 80           LDX     #$80                
85FC: 20 05 86        JSR     $8605               ; {}
85FF: A2 90           LDX     #$90                
8601: 20 05 86        JSR     $8605               ; {}
8604: 60              RTS                         
8605: BD 01 07        LDA     $0701,X             
8608: 29 F8           AND     #$F8                
860A: C9 38           CMP     #$38                
860C: F0 04           BEQ     $8612               ; {}
860E: C9 40           CMP     #$40                
8610: D0 F2           BNE     $8604               ; {}
8612: 20 87 E0        JSR     $E087               
8615: BD 01 07        LDA     $0701,X             
8618: 29 07           AND     #$07                
861A: 20 2B EE        JSR     $EE2B               
861D: 53 ; ????
861E: 86 23           STX     $23                 
8620: 86 65           STX     $65                 
8622: DD 20 90        CMP     $9020,X             ; {}
8625: D9 90 1B        CMP     $1B90,Y             
8628: 20 E7 D9        JSR     $D9E7               
862B: 90 20           BCC     $864D               ; {}
862D: 20 09 DA        JSR     $DA09               
8630: 20 62 DF        JSR     $DF62               
8633: 20 69 86        JSR     $8669               ; {}
8636: 20 C0 DB        JSR     $DBC0               
8639: 20 D3 86        JSR     $86D3               ; {}
863C: 20 DE DC        JSR     $DCDE               
863F: 20 1E 87        JSR     $871E               ; {}
8642: 60              RTS                         
8643: A9 80           LDA     #$80                
8645: 8D 80 03        STA     $0380               
8648: A9 F8           LDA     #$F8                
864A: 99 00 07        STA     $0700,Y             
864D: 20 A9 DC        JSR     $DCA9               
8650: 4C 41 85        JMP     $8541               ; {}
8653: 8A              TXA                         
8654: 38              SEC                         
8655: E9 60           SBC     #$60                
8657: 0A              ASL     A                   
8658: 29 60           AND     #$60                
865A: 85 00           STA     $00                 ; {ram.GP_00}
865C: 20 C1 85        JSR     $85C1               ; {}
865F: FE 01 07        INC     $0701,X             
8662: 60              RTS                         
8663: A9 50           LDA     #$50                
8665: 9D 02 07        STA     $0702,X             
8668: 60              RTS                         
8669: 20 87 D2        JSR     $D287               
866C: D0 F5           BNE     $8663               ; {}
866E: AD D3 04        LDA     $04D3               
8671: C9 40           CMP     #$40                
8673: B0 07           BCS     $867C               ; {}
8675: AD D4 04        LDA     $04D4               
8678: C9 40           CMP     #$40                
867A: 90 E7           BCC     $8663               ; {}
867C: A9 00           LDA     #$00                
867E: 9D 05 07        STA     $0705,X             
8681: BD 02 07        LDA     $0702,X             
8684: 29 0F           AND     #$0F                
8686: C9 08           CMP     #$08                
8688: B0 19           BCS     $86A3               ; {}
868A: BD 03 07        LDA     $0703,X             
868D: C9 F0           CMP     #$F0                
868F: B0 27           BCS     $86B8               ; {}
8691: AD D3 04        LDA     $04D3               
8694: C9 40           CMP     #$40                
8696: 90 20           BCC     $86B8               ; {}
8698: AD D5 04        LDA     $04D5               
869B: C9 40           CMP     #$40                
869D: B0 19           BCS     $86B8               ; {}
869F: A9 02           LDA     #$02                
86A1: D0 C2           BNE     $8665               ; {}
86A3: BD 03 07        LDA     $0703,X             
86A6: C9 08           CMP     #$08                
86A8: 90 F5           BCC     $869F               ; {}
86AA: AD D4 04        LDA     $04D4               
86AD: C9 40           CMP     #$40                
86AF: 90 EE           BCC     $869F               ; {}
86B1: AD D6 04        LDA     $04D6               
86B4: C9 40           CMP     #$40                
86B6: B0 E7           BCS     $869F               ; {}
86B8: A9 0D           LDA     #$0D                
86BA: D0 A9           BNE     $8665               ; {}
86BC: BD 02 07        LDA     $0702,X             
86BF: 48              PHA                         
86C0: 29 F0           AND     #$F0                
86C2: 9D 05 07        STA     $0705,X             
86C5: 68              PLA                         
86C6: 0A              ASL     A                   
86C7: 0A              ASL     A                   
86C8: 0A              ASL     A                   
86C9: 0A              ASL     A                   
86CA: 9D 04 07        STA     $0704,X             
86CD: 20 DA DB        JSR     $DBDA               
86D0: 4C C9 DB        JMP     $DBC9               
86D3: AD 2F 01        LDA     $012F               
86D6: C9 01           CMP     #$01                
86D8: F0 2F           BEQ     $8709               ; {}
86DA: 20 E3 82        JSR     $82E3               ; {}
86DD: 29 10           AND     #$10                
86DF: D0 04           BNE     $86E5               ; {}
86E1: A0 06           LDY     #$06                
86E3: D0 02           BNE     $86E7               ; {}
86E5: A0 00           LDY     #$00                
86E7: BD 04 07        LDA     $0704,X             
86EA: 30 01           BMI     $86ED               ; {}
86EC: C8              INY                         
86ED: A5 14           LDA     $14                 
86EF: 29 10           AND     #$10                
86F1: D0 02           BNE     $86F5               ; {}
86F3: C8              INY                         
86F4: C8              INY                         
86F5: A9 54           LDA     #$54                
86F7: 85 08           STA     $08                 
86F9: A9 72           LDA     #$72                
86FB: 85 09           STA     $09                 
86FD: A9 03           LDA     #$03                
86FF: 85 00           STA     $00                 ; {ram.GP_00}
8701: 98              TYA                         
8702: 0A              ASL     A                   
8703: 0A              ASL     A                   
8704: 0A              ASL     A                   
8705: 0A              ASL     A                   
8706: 4C AB 9B        JMP     $9BAB               ; {}
8709: 20 E3 82        JSR     $82E3               ; {}
870C: A0 00           LDY     #$00                
870E: 29 10           AND     #$10                
8710: D0 02           BNE     $8714               ; {}
8712: C8              INY                         
8713: C8              INY                         
8714: A5 14           LDA     $14                 
8716: 29 08           AND     #$08                
8718: D0 01           BNE     $871B               ; {}
871A: C8              INY                         
871B: 4C F5 86        JMP     $86F5               ; {}
871E: 60              RTS                         
871F: A9 02           LDA     #$02                
8721: 9D 02 07        STA     $0702,X             
8724: 20 8B 84        JSR     $848B               ; {}
8727: 20 E3 82        JSR     $82E3               ; {}
872A: 29 0F           AND     #$0F                
872C: 0A              ASL     A                   
872D: 85 00           STA     $00                 ; {ram.GP_00}
872F: 8A              TXA                         
8730: 38              SEC                         
8731: E9 60           SBC     #$60                
8733: 4A              LSR     A                   
8734: 4A              LSR     A                   
8735: 4A              LSR     A                   
8736: 4A              LSR     A                   
8737: 4A              LSR     A                   
8738: 18              CLC                         
8739: 65 00           ADC     $00                 ; {ram.GP_00}
873B: A8              TAY                         
873C: B9 B3 71        LDA     $71B3,Y             
873F: 48              PHA                         
8740: 29 F0           AND     #$F0                
8742: 9D 00 07        STA     $0700,X             
8745: 68              PLA                         
8746: 0A              ASL     A                   
8747: 0A              ASL     A                   
8748: 0A              ASL     A                   
8749: 0A              ASL     A                   
874A: 9D 03 07        STA     $0703,X             
874D: 60              RTS                         
874E: A2 60           LDX     #$60                
8750: 20 55 87        JSR     $8755               ; {}
8753: A2 80           LDX     #$80                
8755: BD 01 07        LDA     $0701,X             
8758: 29 F8           AND     #$F8                
875A: C9 68           CMP     #$68                
875C: D0 51           BNE     $87AF               ; {}
875E: 20 87 E0        JSR     $E087               
8761: BD 01 07        LDA     $0701,X             
8764: 29 07           AND     #$07                
8766: 20 2B EE        JSR     $EE2B               
8769: A0 87           LDY     #$87                
876B: 6F ; ????
876C: 87 ; ????
876D: 65 DD           ADC     $DD                 
876F: 20 90 D9        JSR     $D990               
8772: 90 14           BCC     $8788               ; {}
8774: 20 E7 D9        JSR     $D9E7               
8777: 90 14           BCC     $878D               ; {}
8779: 20 09 DA        JSR     $DA09               
877C: 20 69 86        JSR     $8669               ; {}
877F: 20 C0 DB        JSR     $DBC0               
8782: 20 B0 87        JSR     $87B0               ; {}
8785: 4C DE DC        JMP     $DCDE               
8788: A9 F8           LDA     #$F8                
878A: 99 00 07        STA     $0700,Y             
878D: A9 80           LDA     #$80                
878F: 8D 80 03        STA     $0380               
8792: 20 A9 DC        JSR     $DCA9               
8795: A9 F8           LDA     #$F8                
8797: 9D 10 02        STA     $0210,X             
879A: 9D 14 02        STA     $0214,X             
879D: 4C 41 85        JMP     $8541               ; {}
87A0: 8A              TXA                         
87A1: 38              SEC                         
87A2: E9 60           SBC     #$60                
87A4: 0A              ASL     A                   
87A5: 29 60           AND     #$60                
87A7: 85 00           STA     $00                 ; {ram.GP_00}
87A9: 20 1F 87        JSR     $871F               ; {}
87AC: FE 01 07        INC     $0701,X             
87AF: 60              RTS                         
87B0: A0 20           LDY     #$20                
87B2: BD 04 07        LDA     $0704,X             
87B5: 30 01           BMI     $87B8               ; {}
87B7: C8              INY                         
87B8: A5 14           LDA     $14                 
87BA: 29 10           AND     #$10                
87BC: D0 02           BNE     $87C0               ; {}
87BE: C8              INY                         
87BF: C8              INY                         
87C0: 98              TYA                         
87C1: 4C CD C4        JMP     $C4CD               
87C4: A2 78           LDX     #$78                
87C6: 20 CB 87        JSR     $87CB               ; {}
87C9: A2 98           LDX     #$98                
87CB: 20 87 E0        JSR     $E087               
87CE: BD 01 07        LDA     $0701,X             
87D1: 29 03           AND     #$03                
87D3: 20 2B EE        JSR     $EE2B               
87D6: DA ; ????
87D7: 87 ; ????
87D8: 18              CLC                         
87D9: 88              DEY                         
87DA: 8A              TXA                         
87DB: 38              SEC                         
87DC: E9 18           SBC     #$18                
87DE: A8              TAY                         
87DF: B9 01 07        LDA     $0701,Y             
87E2: 29 07           AND     #$07                
87E4: C9 01           CMP     #$01                
87E6: D0 2F           BNE     $8817               ; {}
87E8: B9 03 07        LDA     $0703,Y             
87EB: 9D 03 07        STA     $0703,X             
87EE: B9 00 07        LDA     $0700,Y             
87F1: 38              SEC                         
87F2: E9 10           SBC     #$10                
87F4: 9D 00 07        STA     $0700,X             
87F7: A0 40           LDY     #$40                
87F9: AD 23 07        LDA     $0723               
87FC: DD 03 07        CMP     $0703,X             
87FF: B0 02           BCS     $8803               ; {}
8801: A0 B0           LDY     #$B0                
8803: 98              TYA                         
8804: 9D 04 07        STA     $0704,X             
8807: A9 80           LDA     #$80                
8809: 24 26           BIT     $26                 
880B: 50 02           BVC     $880F               ; {}
880D: A9 A0           LDA     #$A0                
880F: 9D 06 07        STA     $0706,X             
8812: A9 09           LDA     #$09                
8814: 9D 01 07        STA     $0701,X             
8817: 60              RTS                         
8818: BD 00 07        LDA     $0700,X             
881B: C9 F0           CMP     #$F0                
881D: B0 27           BCS     $8846               ; {}
881F: BD 03 07        LDA     $0703,X             
8822: C9 F8           CMP     #$F8                
8824: B0 20           BCS     $8846               ; {}
8826: 20 49 88        JSR     $8849               ; {}
8829: 20 09 DA        JSR     $DA09               
882C: F0 0B           BEQ     $8839               ; {}
882E: 90 09           BCC     $8839               ; {}
8830: 20 DA DB        JSR     $DBDA               
8833: 20 C9 DB        JSR     $DBC9               
8836: 4C 61 88        JMP     $8861               ; {}
8839: A5 6F           LDA     $6F                 
883B: D0 09           BNE     $8846               ; {}
883D: A9 01           LDA     #$01                
883F: 85 6F           STA     $6F                 
8841: A9 20           LDA     #$20                
8843: 8D 81 03        STA     $0381               
8846: 4C 2F DF        JMP     $DF2F               
8849: BD 06 07        LDA     $0706,X             
884C: 30 03           BMI     $8851               ; {}
884E: D0 28           BNE     $8878               ; {}
8850: 60              RTS                         
8851: BD 06 07        LDA     $0706,X             
8854: 18              CLC                         
8855: 69 02           ADC     #$02                
8857: C9 F8           CMP     #$F8                
8859: 90 26           BCC     $8881               ; {}
885B: A9 08           LDA     #$08                
885D: 9D 06 07        STA     $0706,X             
8860: 60              RTS                         
8861: BD 00 07        LDA     $0700,X             
8864: 9D 00 02        STA     $0200,X             
8867: BD 03 07        LDA     $0703,X             
886A: 9D 03 02        STA     $0203,X             
886D: A9 A8           LDA     #$A8                
886F: 9D 01 02        STA     $0201,X             
8872: A9 01           LDA     #$01                
8874: 9D 02 02        STA     $0202,X             
8877: 60              RTS                         
8878: BD 06 07        LDA     $0706,X             
887B: C9 78           CMP     #$78                
887D: B0 02           BCS     $8881               ; {}
887F: 69 02           ADC     #$02                
8881: 9D 06 07        STA     $0706,X             
8884: 29 F0           AND     #$F0                
8886: 9D 05 07        STA     $0705,X             
8889: 60              RTS                         
888A: 20 E3 82        JSR     $82E3               ; {}
888D: 29 0F           AND     #$0F                
888F: 0A              ASL     A                   
8890: 0A              ASL     A                   
8891: 0A              ASL     A                   
8892: 85 00           STA     $00                 ; {ram.GP_00}
8894: A9 00           LDA     #$00                
8896: 9D 06 07        STA     $0706,X             
8899: A9 70           LDA     #$70                
889B: 9D 01 07        STA     $0701,X             
889E: 8A              TXA                         
889F: 38              SEC                         
88A0: E9 60           SBC     #$60                
88A2: 4A              LSR     A                   
88A3: 4A              LSR     A                   
88A4: 4A              LSR     A                   
88A5: 4A              LSR     A                   
88A6: 0A              ASL     A                   
88A7: 18              CLC                         
88A8: 65 00           ADC     $00                 ; {ram.GP_00}
88AA: A8              TAY                         
88AB: B9 93 71        LDA     $7193,Y             
88AE: 48              PHA                         
88AF: 29 F0           AND     #$F0                
88B1: 18              CLC                         
88B2: 69 04           ADC     #$04                
88B4: 9D 00 07        STA     $0700,X             
88B7: 68              PLA                         
88B8: 0A              ASL     A                   
88B9: 0A              ASL     A                   
88BA: 0A              ASL     A                   
88BB: 0A              ASL     A                   
88BC: 18              CLC                         
88BD: 69 04           ADC     #$04                
88BF: 9D 03 07        STA     $0703,X             
88C2: B9 94 71        LDA     $7194,Y             
88C5: 9D 02 07        STA     $0702,X             
88C8: 60              RTS                         
88C9: A2 60           LDX     #$60                
88CB: 20 DA 88        JSR     $88DA               ; {}
88CE: A2 70           LDX     #$70                
88D0: 20 DA 88        JSR     $88DA               ; {}
88D3: A2 80           LDX     #$80                
88D5: 20 DA 88        JSR     $88DA               ; {}
88D8: A2 90           LDX     #$90                
88DA: BD 01 07        LDA     $0701,X             
88DD: 29 07           AND     #$07                
88DF: 20 2B EE        JSR     $EE2B               
88E2: 01 89           ORA     ($89,X)             
88E4: EA              NOP                         
88E5: 88              DEY                         
88E6: FB ; ????
88E7: 88              DEY                         
88E8: 34 ; ????
88E9: 89 ; ????
88EA: 20 18 89        JSR     $8918               ; {}
88ED: BD 03 07        LDA     $0703,X             
88F0: 48              PHA                         
88F1: 20 1D 8A        JSR     $8A1D               ; {}
88F4: 68              PLA                         
88F5: 9D 03 07        STA     $0703,X             
88F8: 4C 3B 89        JMP     $893B               ; {}
88FB: 20 27 89        JSR     $8927               ; {}
88FE: 4C ED 88        JMP     $88ED               ; {}
8901: 8A              TXA                         
8902: 38              SEC                         
8903: E9 60           SBC     #$60                
8905: 18              CLC                         
8906: 65 14           ADC     $14                 
8908: 29 7F           AND     #$7F                
890A: D0 0B           BNE     $8917               ; {}
890C: 20 8A 88        JSR     $888A               ; {}
890F: FE 01 07        INC     $0701,X             
8912: A9 40           LDA     #$40                
8914: 8D 80 03        STA     $0380               
8917: 60              RTS                         
8918: BD 06 07        LDA     $0706,X             
891B: C9 20           CMP     #$20                
891D: B0 04           BCS     $8923               ; {}
891F: FE 06 07        INC     $0706,X             
8922: 60              RTS                         
8923: FE 01 07        INC     $0701,X             
8926: 60              RTS                         
8927: BD 06 07        LDA     $0706,X             
892A: D0 0B           BNE     $8937               ; {}
892C: BD 01 07        LDA     $0701,X             
892F: 29 F0           AND     #$F0                
8931: 9D 01 07        STA     $0701,X             
8934: 4C 89 DD        JMP     $DD89               
8937: DE 06 07        DEC     $0706,X             
893A: 60              RTS                         
893B: BD 02 07        LDA     $0702,X             
893E: 18              CLC                         
893F: 69 10           ADC     #$10                
8941: 20 67 C6        JSR     $C667               
8944: BD 06 07        LDA     $0706,X             
8947: 85 09           STA     $09                 
8949: 4A              LSR     A                   
894A: 4A              LSR     A                   
894B: 85 08           STA     $08                 
894D: BD 02 07        LDA     $0702,X             
8950: 29 03           AND     #$03                
8952: 20 2B EE        JSR     $EE2B               
8955: 5D 89 A3        EOR     $A389,X             ; {}
8958: 89 ; ????
8959: 8F ; ????
895A: 89 ; ????
895B: 99 89 BD        STA     $BD89,Y             ; {}
895E: 00              BRK                         
895F: 07 ; ????
8960: 38              SEC                         
8961: E5 09           SBC     $09                 
8963: 9D 00 02        STA     $0200,X             
8966: A5 09           LDA     $09                 
8968: 4A              LSR     A                   
8969: 18              CLC                         
896A: 65 08           ADC     $08                 
896C: 85 0A           STA     $0A                 
896E: BD 00 07        LDA     $0700,X             
8971: 38              SEC                         
8972: E5 0A           SBC     $0A                 
8974: 9D 04 02        STA     $0204,X             
8977: A5 09           LDA     $09                 
8979: 4A              LSR     A                   
897A: 85 0A           STA     $0A                 
897C: BD 00 07        LDA     $0700,X             
897F: 38              SEC                         
8980: E5 0A           SBC     $0A                 
8982: 9D 08 02        STA     $0208,X             
8985: BD 00 07        LDA     $0700,X             
8988: 38              SEC                         
8989: E5 08           SBC     $08                 
898B: 9D 0C 02        STA     $020C,X             
898E: 60              RTS                         
898F: 8A              TXA                         
8990: 48              PHA                         
8991: E8              INX                         
8992: E8              INX                         
8993: E8              INX                         
8994: 20 5D 89        JSR     $895D               ; {}
8997: 68              PLA                         
8998: 60              RTS                         
8999: 8A              TXA                         
899A: 48              PHA                         
899B: E8              INX                         
899C: E8              INX                         
899D: E8              INX                         
899E: 20 A3 89        JSR     $89A3               ; {}
89A1: 68              PLA                         
89A2: 60              RTS                         
89A3: A5 09           LDA     $09                 
89A5: 18              CLC                         
89A6: 7D 00 07        ADC     $0700,X             
89A9: 9D 00 02        STA     $0200,X             
89AC: A5 09           LDA     $09                 
89AE: 4A              LSR     A                   
89AF: 18              CLC                         
89B0: 65 08           ADC     $08                 
89B2: 18              CLC                         
89B3: 7D 00 07        ADC     $0700,X             
89B6: 9D 04 02        STA     $0204,X             
89B9: A5 09           LDA     $09                 
89BB: 4A              LSR     A                   
89BC: 18              CLC                         
89BD: 7D 00 07        ADC     $0700,X             
89C0: 9D 08 02        STA     $0208,X             
89C3: A5 08           LDA     $08                 
89C5: 18              CLC                         
89C6: 7D 00 07        ADC     $0700,X             
89C9: 9D 0C 02        STA     $020C,X             
89CC: 60              RTS                         
89CD: 60              RTS                         
89CE: A2 50           LDX     #$50                
89D0: BD 01 07        LDA     $0701,X             
89D3: 4A              LSR     A                   
89D4: B0 22           BCS     $89F8               ; {}
89D6: AD BB 71        LDA     $71BB               
89D9: C9 FF           CMP     #$FF                
89DB: F0 1A           BEQ     $89F7               ; {}
89DD: 29 3F           AND     #$3F                
89DF: C5 46           CMP     $46                 
89E1: D0 14           BNE     $89F7               ; {}
89E3: AD BC 71        LDA     $71BC               
89E6: 48              PHA                         
89E7: 29 F0           AND     #$F0                
89E9: 9D 00 07        STA     $0700,X             
89EC: 68              PLA                         
89ED: 0A              ASL     A                   
89EE: 0A              ASL     A                   
89EF: 0A              ASL     A                   
89F0: 0A              ASL     A                   
89F1: 9D 03 07        STA     $0703,X             
89F4: FE 01 07        INC     $0701,X             
89F7: 60              RTS                         
89F8: 20 8A D9        JSR     $D98A               
89FB: 90 03           BCC     $8A00               ; {}
89FD: 4C 18 8A        JMP     $8A18               ; {}
8A00: A9 01           LDA     #$01                
8A02: 8D 3D 01        STA     $013D               
8A05: A9 FF           LDA     #$FF                
8A07: 8D BB 71        STA     $71BB               
8A0A: 20 1D DD        JSR     $DD1D               
8A0D: A9 00           LDA     #$00                
8A0F: 9D 01 07        STA     $0701,X             
8A12: A9 10           LDA     #$10                
8A14: 8D 81 03        STA     $0381               
8A17: 60              RTS                         
8A18: A9 63           LDA     #$63                
8A1A: 4C CD C4        JMP     $C4CD               
8A1D: BD 00 07        LDA     $0700,X             
8A20: C9 F8           CMP     #$F8                
8A22: B0 65           BCS     $8A89               ; {}
8A24: A0 20           LDY     #$20                
8A26: B9 08 07        LDA     $0708,Y             
8A29: D0 5E           BNE     $8A89               ; {}
8A2B: A9 8A           LDA     #$8A                
8A2D: 48              PHA                         
8A2E: A9 42           LDA     #$42                
8A30: 48              PHA                         
8A31: 98              TYA                         
8A32: 48              PHA                         
8A33: BD 02 07        LDA     $0702,X             
8A36: 29 03           AND     #$03                
8A38: 20 2B EE        JSR     $EE2B               
8A3B: 73 ; ????
8A3C: 8A              TXA                         
8A3D: 63 ; ????
8A3E: 8A              TXA                         
8A3F: 58              CLI                         
8A40: 8A              TXA                         
8A41: 48              PHA                         
8A42: 8A              TXA                         
8A43: B0 44           BCS     $8A89               ; {}
8A45: 4C 53 DA        JMP     $DA53               
8A48: 68              PLA                         
8A49: A8              TAY                         
8A4A: BD 03 07        LDA     $0703,X             
8A4D: 20 7E 8A        JSR     $8A7E               ; {}
8A50: 20 AD 8A        JSR     $8AAD               ; {}
8A53: B0 34           BCS     $8A89               ; {}
8A55: 4C 93 8A        JMP     $8A93               ; {}
8A58: 68              PLA                         
8A59: A8              TAY                         
8A5A: BD 03 07        LDA     $0703,X             
8A5D: 20 8A 8A        JSR     $8A8A               ; {}
8A60: 4C 50 8A        JMP     $8A50               ; {}
8A63: 68              PLA                         
8A64: A8              TAY                         
8A65: BD 00 07        LDA     $0700,X             
8A68: 20 7E 8A        JSR     $8A7E               ; {}
8A6B: 20 BF 8A        JSR     $8ABF               ; {}
8A6E: B0 19           BCS     $8A89               ; {}
8A70: 4C A0 8A        JMP     $8AA0               ; {}
8A73: 68              PLA                         
8A74: A8              TAY                         
8A75: BD 00 07        LDA     $0700,X             
8A78: 20 8A 8A        JSR     $8A8A               ; {}
8A7B: 4C 6B 8A        JMP     $8A6B               ; {}
8A7E: 18              CLC                         
8A7F: 69 08           ADC     #$08                
8A81: 85 00           STA     $00                 ; {ram.GP_00}
8A83: 18              CLC                         
8A84: 7D 06 07        ADC     $0706,X             
8A87: 85 01           STA     $01                 
8A89: 60              RTS                         
8A8A: 85 01           STA     $01                 
8A8C: 38              SEC                         
8A8D: FD 06 07        SBC     $0706,X             
8A90: 85 00           STA     $00                 ; {ram.GP_00}
8A92: 60              RTS                         
8A93: BD 00 07        LDA     $0700,X             
8A96: 85 00           STA     $00                 ; {ram.GP_00}
8A98: 18              CLC                         
8A99: 69 08           ADC     #$08                
8A9B: 85 01           STA     $01                 
8A9D: 4C BF 8A        JMP     $8ABF               ; {}
8AA0: BD 03 07        LDA     $0703,X             
8AA3: 85 00           STA     $00                 ; {ram.GP_00}
8AA5: 18              CLC                         
8AA6: 69 08           ADC     #$08                
8AA8: 85 01           STA     $01                 
8AAA: 4C AD 8A        JMP     $8AAD               ; {}
8AAD: B9 03 07        LDA     $0703,Y             
8AB0: 48              PHA                         
8AB1: 38              SEC                         
8AB2: E9 04           SBC     #$04                
8AB4: 85 02           STA     $02                 
8AB6: 68              PLA                         
8AB7: 18              CLC                         
8AB8: 69 08           ADC     #$08                
8ABA: 85 03           STA     $03                 
8ABC: 4C DD 8A        JMP     $8ADD               ; {}
8ABF: B9 00 07        LDA     $0700,Y             
8AC2: 18              CLC                         
8AC3: 69 08           ADC     #$08                
8AC5: 85 03           STA     $03                 
8AC7: A5 F8           LDA     $F8                 
8AC9: 29 04           AND     #$04                
8ACB: 08              PHP                         
8ACC: A9 13           LDA     #$13                
8ACE: 28              PLP                         
8ACF: F0 02           BEQ     $8AD3               ; {}
8AD1: A9 08           LDA     #$08                
8AD3: 85 05           STA     $05                 
8AD5: 38              SEC                         
8AD6: B9 00 07        LDA     $0700,Y             
8AD9: E5 05           SBC     $05                 
8ADB: 85 02           STA     $02                 
8ADD: 38              SEC                         
8ADE: A5 02           LDA     $02                 
8AE0: E5 01           SBC     $01                 
8AE2: B0 05           BCS     $8AE9               ; {}
8AE4: 38              SEC                         
8AE5: A5 00           LDA     $00                 ; {ram.GP_00}
8AE7: E5 03           SBC     $03                 
8AE9: 60              RTS                         
8AEA: AC 30 01        LDY     $0130               
8AED: B9 FE 71        LDA     $71FE,Y             
8AF0: A8              TAY                         
8AF1: 4C F6 8A        JMP     $8AF6               ; {}
8AF4: A0 1F           LDY     #$1F                
8AF6: A2 1F           LDX     #$1F                
8AF8: B9 01 72        LDA     $7201,Y             
8AFB: 9D 90 03        STA     $0390,X             
8AFE: 88              DEY                         
8AFF: CA              DEX                         
8B00: 10 F6           BPL     $8AF8               ; {}
8B02: 60              RTS                         
8B03: A9 4F           LDA     #$4F                
8B05: 85 FB           STA     $FB                 
8B07: 8D 25 40        STA     $4025               
8B0A: 60              RTS                         
8B0B: 85 02           STA     $02                 
8B0D: 84 03           STY     $03                 
8B0F: A5 1A           LDA     $1A                 
8B11: 29 01           AND     #$01                
8B13: 0A              ASL     A                   
8B14: A8              TAY                         
8B15: B9 11 70        LDA     $7011,Y             
8B18: 85 00           STA     $00                 ; {ram.GP_00}
8B1A: B9 12 70        LDA     $7012,Y             
8B1D: 85 01           STA     $01                 
8B1F: 98              TYA                         
8B20: F0 03           BEQ     $8B25               ; {}
8B22: 4C 37 8B        JMP     $8B37               ; {}
8B25: 20 56 8B        JSR     $8B56               ; {}
8B28: A5 03           LDA     $03                 
8B2A: 4A              LSR     A                   
8B2B: 4A              LSR     A                   
8B2C: 4A              LSR     A                   
8B2D: 4A              LSR     A                   
8B2E: 05 00           ORA     $00                 ; {ram.GP_00}
8B30: 85 00           STA     $00                 ; {ram.GP_00}
8B32: A0 00           LDY     #$00                
8B34: B1 00           LDA     ($00),Y             ; {ram.GP_00}
8B36: 60              RTS                         
8B37: 20 56 8B        JSR     $8B56               ; {}
8B3A: C9 07           CMP     #$07                
8B3C: B0 08           BCS     $8B46               ; {}
8B3E: A5 00           LDA     $00                 ; {ram.GP_00}
8B40: C9 E0           CMP     #$E0                
8B42: B0 02           BCS     $8B46               ; {}
8B44: 90 E2           BCC     $8B28               ; {}
8B46: A5 00           LDA     $00                 ; {ram.GP_00}
8B48: 38              SEC                         
8B49: E9 E0           SBC     #$E0                
8B4B: 85 00           STA     $00                 ; {ram.GP_00}
8B4D: A5 01           LDA     $01                 
8B4F: E9 01           SBC     #$01                
8B51: 85 01           STA     $01                 
8B53: 4C 28 8B        JMP     $8B28               ; {}
8B56: A5 FD           LDA     $FD                 
8B58: 18              CLC                         
8B59: 65 00           ADC     $00                 ; {ram.GP_00}
8B5B: 85 00           STA     $00                 ; {ram.GP_00}
8B5D: A9 00           LDA     #$00                
8B5F: 65 01           ADC     $01                 
8B61: 85 01           STA     $01                 
8B63: A5 00           LDA     $00                 ; {ram.GP_00}
8B65: 18              CLC                         
8B66: 65 02           ADC     $02                 
8B68: 29 F0           AND     #$F0                
8B6A: 85 00           STA     $00                 ; {ram.GP_00}
8B6C: A5 01           LDA     $01                 
8B6E: 69 00           ADC     #$00                
8B70: 85 01           STA     $01                 
8B72: 60              RTS                         
8B73: 60              RTS                         
8B74: A5 1C           LDA     $1C                 
8B76: 10 15           BPL     $8B8D               ; {}
8B78: AD D6 04        LDA     $04D6               
8B7B: C9 50           CMP     #$50                
8B7D: B0 08           BCS     $8B87               ; {}
8B7F: AD D5 04        LDA     $04D5               
8B82: C9 50           CMP     #$50                
8B84: B0 04           BCS     $8B8A               ; {}
8B86: 60              RTS                         
8B87: 4C 3C D0        JMP     $D03C               
8B8A: 4C 40 D0        JMP     $D040               
8B8D: AD D5 04        LDA     $04D5               
8B90: C9 50           CMP     #$50                
8B92: B0 08           BCS     $8B9C               ; {}
8B94: AD D6 04        LDA     $04D6               
8B97: C9 50           CMP     #$50                
8B99: B0 04           BCS     $8B9F               ; {}
8B9B: 60              RTS                         
8B9C: 4C 44 D0        JMP     $D044               
8B9F: 4C 4E D0        JMP     $D04E               
8BA2: A5 FD           LDA     $FD                 
8BA4: 29 0F           AND     #$0F                
8BA6: C9 0D           CMP     #$0D                
8BA8: F0 1A           BEQ     $8BC4               ; {}
8BAA: C9 0C           CMP     #$0C                
8BAC: F0 19           BEQ     $8BC7               ; {}
8BAE: A5 68           LDA     $68                 
8BB0: 0A              ASL     A                   
8BB1: A8              TAY                         
8BB2: B9 BF 8B        LDA     $8BBF,Y             ; {}
8BB5: 85 00           STA     $00                 ; {ram.GP_00}
8BB7: B9 C0 8B        LDA     $8BC0,Y             ; {}
8BBA: 85 01           STA     $01                 
8BBC: 6C 00 00        JMP     ($0000)             ; {ram.GP_00}
8BBF: C3 ; ????
8BC0: 8B ; ????
8BC1: CA              DEX                         
8BC2: 8B ; ????
8BC3: 60              RTS                         
8BC4: 4C F8 8B        JMP     $8BF8               ; {}
8BC7: 4C 12 8C        JMP     $8C12               ; {}
8BCA: 20 E2 8B        JSR     $8BE2               ; {}
8BCD: A5 69           LDA     $69                 
8BCF: 18              CLC                         
8BD0: 69 20           ADC     #$20                
8BD2: 85 69           STA     $69                 
8BD4: A5 6A           LDA     $6A                 
8BD6: 69 00           ADC     #$00                
8BD8: 85 6A           STA     $6A                 
8BDA: 20 E2 8B        JSR     $8BE2               ; {}
8BDD: A9 00           LDA     #$00                
8BDF: 85 68           STA     $68                 
8BE1: 60              RTS                         
8BE2: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
8BE5: A5 6A           LDA     $6A                 
8BE7: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
8BEA: A5 69           LDA     $69                 
8BEC: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
8BEF: A9 12           LDA     #$12                
8BF1: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
8BF4: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
8BF7: 60              RTS                         
8BF8: AD 82 04        LDA     $0482               
8BFB: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
8BFE: AD 81 04        LDA     $0481               
8C01: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
8C04: A0 00           LDY     #$00                
8C06: B9 83 04        LDA     $0483,Y             
8C09: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
8C0C: C8              INY                         
8C0D: C0 40           CPY     #$40                
8C0F: 90 F5           BCC     $8C06               ; {}
8C11: 60              RTS                         
8C12: 20 A1 8D        JSR     $8DA1               ; {}
8C15: A5 00           LDA     $00                 ; {ram.GP_00}
8C17: 18              CLC                         
8C18: 69 C0           ADC     #$C0                
8C1A: 85 01           STA     $01                 
8C1C: A9 23           LDA     #$23                
8C1E: 85 02           STA     $02                 
8C20: A5 1A           LDA     $1A                 
8C22: 29 01           AND     #$01                
8C24: D0 04           BNE     $8C2A               ; {}
8C26: A9 2B           LDA     #$2B                
8C28: 85 02           STA     $02                 
8C2A: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
8C2D: A5 02           LDA     $02                 
8C2F: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
8C32: A5 01           LDA     $01                 
8C34: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
8C37: 20 A1 8D        JSR     $8DA1               ; {}
8C3A: AA              TAX                         
8C3B: A0 07           LDY     #$07                
8C3D: BD B0 03        LDA     $03B0,X             
8C40: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
8C43: E8              INX                         
8C44: 88              DEY                         
8C45: 10 F6           BPL     $8C3D               ; {}
8C47: 60              RTS                         
8C48: A5 FD           LDA     $FD                 
8C4A: 29 F0           AND     #$F0                
8C4C: 85 08           STA     $08                 
8C4E: A9 00           LDA     #$00                
8C50: 85 01           STA     $01                 
8C52: A5 08           LDA     $08                 
8C54: 85 00           STA     $00                 ; {ram.GP_00}
8C56: 06 00           ASL     $00                 ; {ram.GP_00}
8C58: 26 01           ROL     $01                 
8C5A: 06 00           ASL     $00                 ; {ram.GP_00}
8C5C: 26 01           ROL     $01                 
8C5E: A9 00           LDA     #$00                
8C60: 18              CLC                         
8C61: 65 00           ADC     $00                 ; {ram.GP_00}
8C63: 8D 81 04        STA     $0481               
8C66: A9 20           LDA     #$20                
8C68: 65 01           ADC     $01                 
8C6A: 8D 82 04        STA     $0482               
8C6D: A5 1A           LDA     $1A                 
8C6F: 29 01           AND     #$01                
8C71: D0 09           BNE     $8C7C               ; {}
8C73: AD 82 04        LDA     $0482               
8C76: 18              CLC                         
8C77: 69 08           ADC     #$08                
8C79: 8D 82 04        STA     $0482               
8C7C: 20 92 8C        JSR     $8C92               ; {}
8C7F: 20 9D 8C        JSR     $8C9D               ; {}
8C82: A5 08           LDA     $08                 
8C84: 18              CLC                         
8C85: 65 62           ADC     $62                 
8C87: 85 06           STA     $06                 
8C89: A9 00           LDA     #$00                
8C8B: 65 63           ADC     $63                 
8C8D: 85 07           STA     $07                 
8C8F: 4C AF 8C        JMP     $8CAF               ; {}
8C92: A5 1A           LDA     $1A                 
8C94: 49 FF           EOR     #$FF                
8C96: 8D D1 04        STA     $04D1               
8C99: EE D1 04        INC     $04D1               
8C9C: 60              RTS                         
8C9D: AD D1 04        LDA     $04D1               
8CA0: 29 01           AND     #$01                
8CA2: 0A              ASL     A                   
8CA3: A8              TAY                         
8CA4: B9 11 70        LDA     $7011,Y             
8CA7: 85 62           STA     $62                 
8CA9: B9 12 70        LDA     $7012,Y             
8CAC: 85 63           STA     $63                 
8CAE: 60              RTS                         
8CAF: A0 0F           LDY     #$0F                
8CB1: 98              TYA                         
8CB2: 48              PHA                         
8CB3: B1 06           LDA     ($06),Y             
8CB5: 20 DD 8C        JSR     $8CDD               ; {}
8CB8: 68              PLA                         
8CB9: 48              PHA                         
8CBA: 0A              ASL     A                   
8CBB: A8              TAY                         
8CBC: A5 02           LDA     $02                 
8CBE: 99 83 04        STA     $0483,Y             
8CC1: C8              INY                         
8CC2: A5 03           LDA     $03                 
8CC4: 99 83 04        STA     $0483,Y             
8CC7: 98              TYA                         
8CC8: 18              CLC                         
8CC9: 69 1F           ADC     #$1F                
8CCB: A8              TAY                         
8CCC: A5 04           LDA     $04                 
8CCE: 99 83 04        STA     $0483,Y             
8CD1: C8              INY                         
8CD2: A5 05           LDA     $05                 
8CD4: 99 83 04        STA     $0483,Y             
8CD7: 68              PLA                         
8CD8: A8              TAY                         
8CD9: 88              DEY                         
8CDA: 10 D5           BPL     $8CB1               ; {}
8CDC: 60              RTS                         
8CDD: 85 00           STA     $00                 ; {ram.GP_00}
8CDF: A9 00           LDA     #$00                
8CE1: 85 01           STA     $01                 
8CE3: A0 03           LDY     #$03                
8CE5: 06 00           ASL     $00                 ; {ram.GP_00}
8CE7: 26 01           ROL     $01                 
8CE9: 06 00           ASL     $00                 ; {ram.GP_00}
8CEB: 26 01           ROL     $01                 
8CED: A5 3A           LDA     $3A                 
8CEF: C9 10           CMP     #$10                
8CF1: B0 16           BCS     $8D09               ; {}
8CF3: A5 00           LDA     $00                 ; {ram.GP_00}
8CF5: 18              CLC                         
8CF6: 69 0E           ADC     #$0E                
8CF8: 85 00           STA     $00                 ; {ram.GP_00}
8CFA: A5 01           LDA     $01                 
8CFC: 69 A3           ADC     #$A3                
8CFE: 85 01           STA     $01                 
8D00: B1 00           LDA     ($00),Y             ; {ram.GP_00}
8D02: 99 02 00        STA     $0002,Y             
8D05: 88              DEY                         
8D06: 10 F8           BPL     $8D00               ; {}
8D08: 60              RTS                         
8D09: A5 00           LDA     $00                 ; {ram.GP_00}
8D0B: 18              CLC                         
8D0C: 69 0E           ADC     #$0E                
8D0E: 85 00           STA     $00                 ; {ram.GP_00}
8D10: A5 01           LDA     $01                 
8D12: 69 A3           ADC     #$A3                
8D14: 85 01           STA     $01                 
8D16: 4C 00 8D        JMP     $8D00               ; {}
8D19: 20 92 8C        JSR     $8C92               ; {}
8D1C: 20 8F 8D        JSR     $8D8F               ; {}
8D1F: 20 A1 8D        JSR     $8DA1               ; {}
8D22: A2 00           LDX     #$00                
8D24: 18              CLC                         
8D25: 8A              TXA                         
8D26: 65 00           ADC     $00                 ; {ram.GP_00}
8D28: A8              TAY                         
8D29: B1 64           LDA     ($64),Y             
8D2B: 9D F0 03        STA     $03F0,X             
8D2E: E8              INX                         
8D2F: E0 08           CPX     #$08                
8D31: 90 F1           BCC     $8D24               ; {}
8D33: A5 FD           LDA     $FD                 
8D35: 29 10           AND     #$10                
8D37: F0 2B           BEQ     $8D64               ; {}
8D39: A0 00           LDY     #$00                
8D3B: 18              CLC                         
8D3C: 98              TYA                         
8D3D: 65 00           ADC     $00                 ; {ram.GP_00}
8D3F: 85 01           STA     $01                 
8D41: 98              TYA                         
8D42: AA              TAX                         
8D43: BD F0 03        LDA     $03F0,X             
8D46: 29 F0           AND     #$F0                
8D48: 85 02           STA     $02                 
8D4A: A5 01           LDA     $01                 
8D4C: AA              TAX                         
8D4D: BD B0 03        LDA     $03B0,X             
8D50: 29 0F           AND     #$0F                
8D52: 05 02           ORA     $02                 
8D54: 85 02           STA     $02                 
8D56: A5 01           LDA     $01                 
8D58: AA              TAX                         
8D59: A5 02           LDA     $02                 
8D5B: 9D B0 03        STA     $03B0,X             
8D5E: C8              INY                         
8D5F: C0 08           CPY     #$08                
8D61: 90 D8           BCC     $8D3B               ; {}
8D63: 60              RTS                         
8D64: A0 00           LDY     #$00                
8D66: 18              CLC                         
8D67: 98              TYA                         
8D68: 65 00           ADC     $00                 ; {ram.GP_00}
8D6A: 85 01           STA     $01                 
8D6C: 98              TYA                         
8D6D: AA              TAX                         
8D6E: BD F0 03        LDA     $03F0,X             
8D71: 29 0F           AND     #$0F                
8D73: 85 02           STA     $02                 
8D75: A5 01           LDA     $01                 
8D77: AA              TAX                         
8D78: BD B0 03        LDA     $03B0,X             
8D7B: 29 F0           AND     #$F0                
8D7D: 05 02           ORA     $02                 
8D7F: 85 02           STA     $02                 
8D81: A5 01           LDA     $01                 
8D83: AA              TAX                         
8D84: A5 02           LDA     $02                 
8D86: 9D B0 03        STA     $03B0,X             
8D89: C8              INY                         
8D8A: C0 08           CPY     #$08                
8D8C: 90 D8           BCC     $8D66               ; {}
8D8E: 60              RTS                         
8D8F: AD D1 04        LDA     $04D1               
8D92: 29 01           AND     #$01                
8D94: 0A              ASL     A                   
8D95: A8              TAY                         
8D96: B9 19 70        LDA     $7019,Y             
8D99: 85 64           STA     $64                 
8D9B: B9 1A 70        LDA     $701A,Y             
8D9E: 85 65           STA     $65                 
8DA0: 60              RTS                         
8DA1: A5 FD           LDA     $FD                 
8DA3: 29 E0           AND     #$E0                
8DA5: 4A              LSR     A                   
8DA6: 4A              LSR     A                   
8DA7: 85 00           STA     $00                 ; {ram.GP_00}
8DA9: 60              RTS                         
8DAA: 60              RTS                         
8DAB: 60              RTS                         
8DAC: 20 9D 8C        JSR     $8C9D               ; {}
8DAF: 20 8F 8D        JSR     $8D8F               ; {}
8DB2: 4C D2 8D        JMP     $8DD2               ; {}
8DB5: AD D1 04        LDA     $04D1               
8DB8: 0A              ASL     A                   
8DB9: A8              TAY                         
8DBA: B9 27 70        LDA     $7027,Y             
8DBD: 85 49           STA     $49                 
8DBF: B9 28 70        LDA     $7028,Y             
8DC2: 85 4A           STA     $4A                 
8DC4: A5 3A           LDA     $3A                 
8DC6: C9 10           CMP     #$10                
8DC8: 90 E2           BCC     $8DAC               ; {}
8DCA: A0 00           LDY     #$00                
8DCC: 20 A4 8C        JSR     $8CA4               ; {}
8DCF: 20 96 8D        JSR     $8D96               ; {}
8DD2: 20 AA 8E        JSR     $8EAA               ; {}
8DD5: A0 00           LDY     #$00                
8DD7: B1 49           LDA     ($49),Y             
8DD9: 20 B5 8E        JSR     $8EB5               ; {}
8DDC: A0 01           LDY     #$01                
8DDE: B1 49           LDA     ($49),Y             
8DE0: C9 FD           CMP     #$FD                
8DE2: F0 17           BEQ     $8DFB               ; {}
8DE4: 85 4D           STA     $4D                 
8DE6: C8              INY                         
8DE7: B1 49           LDA     ($49),Y             
8DE9: 85 4E           STA     $4E                 
8DEB: C8              INY                         
8DEC: B1 49           LDA     ($49),Y             
8DEE: 85 4F           STA     $4F                 
8DF0: 98              TYA                         
8DF1: 48              PHA                         
8DF2: 20 FC 8D        JSR     $8DFC               ; {}
8DF5: 68              PLA                         
8DF6: A8              TAY                         
8DF7: C8              INY                         
8DF8: 4C DE 8D        JMP     $8DDE               ; {}
8DFB: 60              RTS                         
8DFC: 20 48 8E        JSR     $8E48               ; {}
8DFF: A9 00           LDA     #$00                
8E01: 85 5F           STA     $5F                 
8E03: A5 4D           LDA     $4D                 
8E05: 29 F0           AND     #$F0                
8E07: 85 61           STA     $61                 
8E09: A5 5F           LDA     $5F                 
8E0B: 0A              ASL     A                   
8E0C: 0A              ASL     A                   
8E0D: 0A              ASL     A                   
8E0E: 0A              ASL     A                   
8E0F: 18              CLC                         
8E10: 65 61           ADC     $61                 
8E12: C9 F0           CMP     #$F0                
8E14: B0 31           BCS     $8E47               ; {}
8E16: A0 00           LDY     #$00                
8E18: B1 51           LDA     ($51),Y             
8E1A: C9 FF           CMP     #$FF                
8E1C: F0 29           BEQ     $8E47               ; {}
8E1E: 85 53           STA     $53                 
8E20: 29 0F           AND     #$0F                
8E22: AA              TAX                         
8E23: C8              INY                         
8E24: B1 51           LDA     ($51),Y             
8E26: 99 53 00        STA     $0053,Y             
8E29: C8              INY                         
8E2A: CA              DEX                         
8E2B: D0 F7           BNE     $8E24               ; {}
8E2D: 20 C7 8E        JSR     $8EC7               ; {}
8E30: A5 53           LDA     $53                 
8E32: 29 0F           AND     #$0F                
8E34: 38              SEC                         
8E35: 65 51           ADC     $51                 
8E37: 85 51           STA     $51                 
8E39: A9 00           LDA     #$00                
8E3B: 65 52           ADC     $52                 
8E3D: 85 52           STA     $52                 
8E3F: 20 68 8E        JSR     $8E68               ; {}
8E42: E6 5F           INC     $5F                 
8E44: 4C 03 8E        JMP     $8E03               ; {}
8E47: 60              RTS                         
8E48: A5 4E           LDA     $4E                 
8E4A: 0A              ASL     A                   
8E4B: A8              TAY                         
8E4C: A5 3A           LDA     $3A                 
8E4E: C9 10           CMP     #$10                
8E50: B0 0B           BCS     $8E5D               ; {}
8E52: B9 7B 70        LDA     $707B,Y             
8E55: 85 51           STA     $51                 
8E57: B9 7C 70        LDA     $707C,Y             
8E5A: 85 52           STA     $52                 
8E5C: 60              RTS                         
8E5D: B9 7B 70        LDA     $707B,Y             
8E60: 85 51           STA     $51                 
8E62: B9 7C 70        LDA     $707C,Y             
8E65: 85 52           STA     $52                 
8E67: 60              RTS                         
8E68: A5 5F           LDA     $5F                 
8E6A: 0A              ASL     A                   
8E6B: 0A              ASL     A                   
8E6C: 0A              ASL     A                   
8E6D: 0A              ASL     A                   
8E6E: 85 5D           STA     $5D                 
8E70: A5 53           LDA     $53                 
8E72: 4A              LSR     A                   
8E73: 4A              LSR     A                   
8E74: 4A              LSR     A                   
8E75: 4A              LSR     A                   
8E76: 18              CLC                         
8E77: 65 5D           ADC     $5D                 
8E79: 85 5D           STA     $5D                 
8E7B: 18              CLC                         
8E7C: A5 4D           LDA     $4D                 
8E7E: 65 5D           ADC     $5D                 
8E80: 85 5D           STA     $5D                 
8E82: A5 53           LDA     $53                 
8E84: 29 0F           AND     #$0F                
8E86: AA              TAX                         
8E87: 18              CLC                         
8E88: A5 62           LDA     $62                 
8E8A: 65 5D           ADC     $5D                 
8E8C: 85 5D           STA     $5D                 
8E8E: A9 00           LDA     #$00                
8E90: 65 63           ADC     $63                 
8E92: 85 5E           STA     $5E                 
8E94: A0 00           LDY     #$00                
8E96: B9 54 00        LDA     $0054,Y             
8E99: 91 5D           STA     ($5D),Y             
8E9B: 98              TYA                         
8E9C: 18              CLC                         
8E9D: 65 5D           ADC     $5D                 
8E9F: 29 0F           AND     #$0F                
8EA1: C9 0F           CMP     #$0F                
8EA3: B0 04           BCS     $8EA9               ; {}
8EA5: C8              INY                         
8EA6: CA              DEX                         
8EA7: D0 ED           BNE     $8E96               ; {}
8EA9: 60              RTS                         
8EAA: A0 00           LDY     #$00                
8EAC: 98              TYA                         
8EAD: 91 62           STA     ($62),Y             
8EAF: C8              INY                         
8EB0: C0 F0           CPY     #$F0                
8EB2: 90 F9           BCC     $8EAD               ; {}
8EB4: 60              RTS                         
8EB5: 29 03           AND     #$03                
8EB7: A8              TAY                         
8EB8: B9 C3 8E        LDA     $8EC3,Y             ; {}
8EBB: A0 40           LDY     #$40                
8EBD: 91 64           STA     ($64),Y             
8EBF: 88              DEY                         
8EC0: 10 FB           BPL     $8EBD               ; {}
8EC2: 60              RTS                         
8EC3: 00              BRK                         
8EC4: 55 AA           EOR     $AA,X               
8EC6: FF ; ????
8EC7: A5 53           LDA     $53                 
8EC9: 4A              LSR     A                   
8ECA: 4A              LSR     A                   
8ECB: 4A              LSR     A                   
8ECC: 4A              LSR     A                   
8ECD: 8D D0 04        STA     $04D0               
8ED0: A5 53           LDA     $53                 
8ED2: 29 0F           AND     #$0F                
8ED4: 18              CLC                         
8ED5: 6D D0 04        ADC     $04D0               
8ED8: 8D D0 04        STA     $04D0               
8EDB: A5 4D           LDA     $4D                 
8EDD: 29 0F           AND     #$0F                
8EDF: 8D CD 04        STA     $04CD               
8EE2: 18              CLC                         
8EE3: 6D D0 04        ADC     $04D0               
8EE6: C9 10           CMP     #$10                
8EE8: 90 09           BCC     $8EF3               ; {}
8EEA: A9 10           LDA     #$10                
8EEC: 38              SEC                         
8EED: ED CD 04        SBC     $04CD               
8EF0: 8D D0 04        STA     $04D0               
8EF3: A9 00           LDA     #$00                
8EF5: 8D CD 04        STA     $04CD               
8EF8: A5 5F           LDA     $5F                 
8EFA: 0A              ASL     A                   
8EFB: 0A              ASL     A                   
8EFC: 0A              ASL     A                   
8EFD: 0A              ASL     A                   
8EFE: 18              CLC                         
8EFF: 65 4D           ADC     $4D                 
8F01: 18              CLC                         
8F02: 6D CD 04        ADC     $04CD               
8F05: 85 60           STA     $60                 
8F07: 29 E0           AND     #$E0                
8F09: 4A              LSR     A                   
8F0A: 4A              LSR     A                   
8F0B: 85 66           STA     $66                 
8F0D: A5 60           LDA     $60                 
8F0F: 29 0F           AND     #$0F                
8F11: 4A              LSR     A                   
8F12: 18              CLC                         
8F13: 65 66           ADC     $66                 
8F15: 18              CLC                         
8F16: 65 64           ADC     $64                 
8F18: 85 66           STA     $66                 
8F1A: A9 00           LDA     #$00                
8F1C: 65 65           ADC     $65                 
8F1E: 85 67           STA     $67                 
8F20: A5 60           LDA     $60                 
8F22: 29 10           AND     #$10                
8F24: 4A              LSR     A                   
8F25: 4A              LSR     A                   
8F26: 4A              LSR     A                   
8F27: 8D CE 04        STA     $04CE               
8F2A: A5 60           LDA     $60                 
8F2C: 29 01           AND     #$01                
8F2E: 0D CE 04        ORA     $04CE               
8F31: F0 0E           BEQ     $8F41               ; {}
8F33: AA              TAX                         
8F34: A9 03           LDA     #$03                
8F36: 0A              ASL     A                   
8F37: 0A              ASL     A                   
8F38: CA              DEX                         
8F39: 8D CE 04        STA     $04CE               
8F3C: F0 08           BEQ     $8F46               ; {}
8F3E: 4C 36 8F        JMP     $8F36               ; {}
8F41: A9 03           LDA     #$03                
8F43: 8D CE 04        STA     $04CE               
8F46: AD CE 04        LDA     $04CE               
8F49: 49 FF           EOR     #$FF                
8F4B: A0 00           LDY     #$00                
8F4D: 31 66           AND     ($66),Y             
8F4F: 8D CF 04        STA     $04CF               
8F52: A5 4F           LDA     $4F                 
8F54: 29 02           AND     #$02                
8F56: F0 0B           BEQ     $8F63               ; {}
8F58: A9 AA           LDA     #$AA                
8F5A: 2D CE 04        AND     $04CE               
8F5D: 0D CF 04        ORA     $04CF               
8F60: 8D CF 04        STA     $04CF               
8F63: A5 4F           LDA     $4F                 
8F65: 29 01           AND     #$01                
8F67: F0 0B           BEQ     $8F74               ; {}
8F69: A9 55           LDA     #$55                
8F6B: 2D CE 04        AND     $04CE               
8F6E: 0D CF 04        ORA     $04CF               
8F71: 8D CF 04        STA     $04CF               
8F74: AD CF 04        LDA     $04CF               
8F77: 91 66           STA     ($66),Y             
8F79: EE CD 04        INC     $04CD               
8F7C: AD CD 04        LDA     $04CD               
8F7F: CD D0 04        CMP     $04D0               
8F82: B0 03           BCS     $8F87               ; {}
8F84: 4C F8 8E        JMP     $8EF8               ; {}
8F87: 60              RTS                         
8F88: A9 10           LDA     #$10                
8F8A: 85 0A           STA     $0A                 
8F8C: E6 1A           INC     $1A                 
8F8E: 20 48 8C        JSR     $8C48               ; {}
8F91: 20 19 8D        JSR     $8D19               ; {}
8F94: 20 F8 8B        JSR     $8BF8               ; {}
8F97: 20 12 8C        JSR     $8C12               ; {}
8F9A: A5 FD           LDA     $FD                 
8F9C: 38              SEC                         
8F9D: E9 10           SBC     #$10                
8F9F: 85 FD           STA     $FD                 
8FA1: A5 1A           LDA     $1A                 
8FA3: E9 00           SBC     #$00                
8FA5: 85 1A           STA     $1A                 
8FA7: C6 0A           DEC     $0A                 
8FA9: 10 E3           BPL     $8F8E               ; {}
8FAB: A5 FD           LDA     $FD                 
8FAD: 18              CLC                         
8FAE: 69 10           ADC     #$10                
8FB0: 85 FD           STA     $FD                 
8FB2: A5 1A           LDA     $1A                 
8FB4: 69 00           ADC     #$00                
8FB6: 85 1A           STA     $1A                 
8FB8: 60              RTS                         
8FB9: A5 3A           LDA     $3A                 
8FBB: C9 0A           CMP     #$0A                
8FBD: 90 2E           BCC     $8FED               ; {}
8FBF: AD E2 04        LDA     $04E2               
8FC2: D0 29           BNE     $8FED               ; {}
8FC4: AA              TAX                         
8FC5: 86 00           STX     $00                 ; {ram.GP_00}
8FC7: 86 01           STX     $01                 
8FC9: A9 2B           LDA     #$2B                
8FCB: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
8FCE: BD EE 8F        LDA     $8FEE,X             ; {}
8FD1: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
8FD4: BC F2 8F        LDY     $8FF2,X             ; {}
8FD7: A6 00           LDX     $00                 ; {ram.GP_00}
8FD9: BD 07 01        LDA     $0107,X             
8FDC: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
8FDF: E8              INX                         
8FE0: 88              DEY                         
8FE1: D0 F6           BNE     $8FD9               ; {}
8FE3: 86 00           STX     $00                 ; {ram.GP_00}
8FE5: E6 01           INC     $01                 
8FE7: A6 01           LDX     $01                 
8FE9: E0 04           CPX     #$04                
8FEB: D0 DC           BNE     $8FC9               ; {}
8FED: 60              RTS                         
8FEE: 43 ; ????
8FEF: 46 3B           LSR     $3B                 
8FF1: 5B ; ????
8FF2: 02 ; ????
8FF3: 02 ; ????
8FF4: 03 ; ????
8FF5: 03 ; ????
8FF6: AD E2 04        LDA     $04E2               
8FF9: D0 F2           BNE     $8FED               ; {}
8FFB: A2 4F           LDX     #$4F                
8FFD: A0 01           LDY     #$01                
8FFF: A9 02           LDA     #$02                
9001: 20 64 90        JSR     $9064               ; {}
9004: A2 07           LDX     #$07                
9006: A0 01           LDY     #$01                
9008: A9 02           LDA     #$02                
900A: 20 4B 90        JSR     $904B               ; {}
900D: A4 3C           LDY     $3C                 
900F: D0 08           BNE     $9019               ; {}
9011: A9 12           LDA     #$12                
9013: 8D 07 01        STA     $0107               
9016: 8D 08 01        STA     $0108               
9019: A2 56           LDX     #$56                
901B: A0 01           LDY     #$01                
901D: A9 02           LDA     #$02                
901F: 20 64 90        JSR     $9064               ; {}
9022: A2 09           LDX     #$09                
9024: A0 01           LDY     #$01                
9026: A9 02           LDA     #$02                
9028: 20 4B 90        JSR     $904B               ; {}
902B: AC 2F 01        LDY     $012F               
902E: C8              INY                         
902F: 8C 0B 01        STY     $010B               
9032: A9 0F           LDA     #$0F                
9034: 8D 0C 01        STA     $010C               
9037: A2 04           LDX     #$04                
9039: 8E 0D 01        STX     $010D               
903C: A2 6B           LDX     #$6B                
903E: A0 00           LDY     #$00                
9040: A9 03           LDA     #$03                
9042: 20 64 90        JSR     $9064               ; {}
9045: A2 0E           LDX     #$0E                
9047: A0 01           LDY     #$01                
9049: A9 03           LDA     #$03                
904B: 86 00           STX     $00                 ; {ram.GP_00}
904D: 84 01           STY     $01                 
904F: 85 02           STA     $02                 
9051: AA              TAX                         
9052: BD 5D EA        LDA     $EA5D,X             
9055: AA              TAX                         
9056: A0 00           LDY     #$00                
9058: BD 28 01        LDA     $0128,X             
905B: 91 00           STA     ($00),Y             ; {ram.GP_00}
905D: C8              INY                         
905E: E8              INX                         
905F: C4 02           CPY     $02                 
9061: 90 F5           BCC     $9058               ; {}
9063: 60              RTS                         
9064: 85 02           STA     $02                 
9066: 86 0C           STX     $0C                 
9068: 84 0D           STY     $0D                 
906A: AA              TAX                         
906B: A9 00           LDA     #$00                
906D: 85 05           STA     $05                 
906F: 85 06           STA     $06                 
9071: 85 07           STA     $07                 
9073: A9 12           LDA     #$12                
9075: 85 03           STA     $03                 
9077: BD 55 EA        LDA     $EA55,X             
907A: A8              TAY                         
907B: B1 0C           LDA     ($0C),Y             
907D: 99 05 00        STA     $0005,Y             
9080: 88              DEY                         
9081: 10 F8           BPL     $907B               ; {}
9083: A2 06           LDX     #$06                
9085: A9 00           LDA     #$00                
9087: 9D 28 01        STA     $0128,X             
908A: CA              DEX                         
908B: 10 FA           BPL     $9087               ; {}
908D: 20 CF E9        JSR     $E9CF               
9090: B0 05           BCS     $9097               ; {}
9092: 20 E6 E9        JSR     $E9E6               
9095: B0 03           BCS     $909A               ; {}
9097: 20 1C EA        JSR     $EA1C               
909A: 4C 27 EA        JMP     $EA27               
909D: AD 4F 01        LDA     $014F               
90A0: F0 0A           BEQ     $90AC               ; {}
90A2: A5 18           LDA     $18                 
90A4: 29 20           AND     #$20                
90A6: D0 09           BNE     $90B1               ; {}
90A8: A5 3C           LDA     $3C                 
90AA: D0 2F           BNE     $90DB               ; {}
90AC: 85 3C           STA     $3C                 
90AE: 4C CA 90        JMP     $90CA               ; {}
90B1: A5 3C           LDA     $3C                 
90B3: 18              CLC                         
90B4: 69 01           ADC     #$01                
90B6: 29 01           AND     #$01                
90B8: 85 3C           STA     $3C                 
90BA: A2 38           LDX     #$38                
90BC: A9 F8           LDA     #$F8                
90BE: 9D 00 02        STA     $0200,X             
90C1: 9D 04 02        STA     $0204,X             
90C4: A9 00           LDA     #$00                
90C6: 9D 02 07        STA     $0702,X             
90C9: 60              RTS                         
90CA: A0 00           LDY     #$00                
90CC: A2 E4           LDX     #$E4                
90CE: B9 DF 90        LDA     $90DF,Y             ; {}
90D1: 9D 00 02        STA     $0200,X             
90D4: E8              INX                         
90D5: C8              INY                         
90D6: E0 EC           CPX     #$EC                
90D8: 90 F4           BCC     $90CE               ; {}
90DA: 60              RTS                         
90DB: A0 08           LDY     #$08                
90DD: D0 ED           BNE     $90CC               ; {}
90DF: C2 ; ????
90E0: 3F ; ????
90E1: 00              BRK                         
90E2: 18              CLC                         
90E3: CA              DEX                         
90E4: 4F ; ????
90E5: 00              BRK                         
90E6: 18              CLC                         
90E7: C2 ; ????
90E8: AA              TAX                         
90E9: 01 18           ORA     ($18,X)             
90EB: CA              DEX                         
90EC: AB ; ????
90ED: 01 18           ORA     ($18,X)             
90EF: 60              RTS                         
90F0: A5 3A           LDA     $3A                 
90F2: C9 10           CMP     #$10                
90F4: 90 F9           BCC     $90EF               ; {}
90F6: 29 0F           AND     #$0F                
90F8: 0A              ASL     A                   
90F9: A8              TAY                         
90FA: B9 07 91        LDA     $9107,Y             ; {}
90FD: 85 10           STA     $10                 
90FF: B9 08 91        LDA     $9108,Y             ; {}
9102: 85 11           STA     $11                 
9104: 6C 10 00        JMP     ($0010)             
9107: EF ; ????
9108: 90 EF           BCC     $90F9               ; {}
910A: 90 EF           BCC     $90FB               ; {}
910C: 90 1A           BCC     $9128               ; {}
910E: 91 EF           STA     ($EF),Y             
9110: 90 EF           BCC     $9101               ; {}
9112: 90 EF           BCC     $9103               ; {}
9114: 90 EF           BCC     $9105               ; {}
9116: 90 64           BCC     $917C               ; {}
9118: C8              INY                         
9119: C8              INY                         
911A: 20 F0 EE        JSR     $EEF0               
911D: E6 3A           INC     $3A                 
911F: 20 CA EE        JSR     $EECA               
9122: 20 74 92        JSR     $9274               ; {}
9125: 20 5B E2        JSR     $E25B               
9128: A5 46           LDA     $46                 
912A: C9 40           CMP     #$40                
912C: B0 37           BCS     $9165               ; {}
912E: 20 6F 91        JSR     $916F               ; {}
9131: 20 C0 91        JSR     $91C0               ; {}
9134: 20 AC 92        JSR     $92AC               ; {}
9137: 20 55 E1        JSR     $E155               
913A: 20 07 98        JSR     $9807               ; {}
913D: A9 04           LDA     #$04                
913F: 8D B9 07        STA     $07B9               
9142: AC 2F 01        LDY     $012F               
9145: B9 17 91        LDA     $9117,Y             ; {}
9148: 85 6B           STA     $6B                 
914A: 20 C4 82        JSR     $82C4               ; {}
914D: A9 08           LDA     #$08                
914F: 20 90 CA        JSR     $CA90               
9152: 20 70 CB        JSR     $CB70               
9155: 68              PLA                         
9156: 68              PLA                         
9157: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
915A: 10 FB           BPL     $9157               ; {}
915C: 20 2E EB        JSR     $EB2E               
915F: 20 C9 EB        JSR     $EBC9               
9162: 4C 8D 80        JMP     $808D               ; {}
9165: A9 80           LDA     #$80                
9167: 85 AB           STA     $AB                 
9169: 0A              ASL     A                   
916A: 8D 24 07        STA     $0724               
916D: F0 E6           BEQ     $9155               ; {}
916F: A9 00           LDA     #$00                
9171: 20 52 95        JSR     $9552               ; {}
9174: 85 3B           STA     $3B                 
9176: 29 3F           AND     #$3F                
9178: 8D D1 04        STA     $04D1               
917B: A9 00           LDA     #$00                
917D: 8D D2 04        STA     $04D2               
9180: 20 B5 8D        JSR     $8DB5               ; {}
9183: 20 5F 95        JSR     $955F               ; {}
9186: 20 0E 96        JSR     $960E               ; {}
9189: 20 03 96        JSR     $9603               ; {}
918C: A9 FE           LDA     #$FE                
918E: 85 1A           STA     $1A                 
9190: A9 EE           LDA     #$EE                
9192: 85 FD           STA     $FD                 
9194: 20 33 7F        JSR     $7F33               
9197: 20 36 7F        JSR     $7F36               
919A: 20 39 7F        JSR     $7F39               
919D: 20 3C 7F        JSR     $7F3C               
91A0: A5 FD           LDA     $FD                 
91A2: 38              SEC                         
91A3: E9 10           SBC     #$10                
91A5: 85 FD           STA     $FD                 
91A7: A5 1A           LDA     $1A                 
91A9: E9 00           SBC     #$00                
91AB: 85 1A           STA     $1A                 
91AD: C9 FE           CMP     #$FE                
91AF: B0 E3           BCS     $9194               ; {}
91B1: 20 21 7F        JSR     $7F21               
91B4: 20 42 EE        JSR     $EE42               
91B7: A9 FF           LDA     #$FF                
91B9: 85 1A           STA     $1A                 
91BB: A9 EE           LDA     #$EE                
91BD: 85 FD           STA     $FD                 
91BF: 60              RTS                         
91C0: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
91C3: A9 04           LDA     #$04                
91C5: 20 D4 91        JSR     $91D4               ; {}
91C8: A9 05           LDA     #$05                
91CA: 20 D4 91        JSR     $91D4               ; {}
91CD: A9 06           LDA     #$06                
91CF: 20 D4 91        JSR     $91D4               ; {}
91D2: A9 07           LDA     #$07                
91D4: 0A              ASL     A                   
91D5: A8              TAY                         
91D6: B9 FA 91        LDA     $91FA,Y             ; {}
91D9: 85 00           STA     $00                 ; {ram.GP_00}
91DB: B9 FB 91        LDA     $91FB,Y             ; {}
91DE: 85 01           STA     $01                 
91E0: A0 00           LDY     #$00                
91E2: B1 00           LDA     ($00),Y             ; {ram.GP_00}
91E4: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
91E7: C8              INY                         
91E8: B1 00           LDA     ($00),Y             ; {ram.GP_00}
91EA: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
91ED: C8              INY                         
91EE: B1 00           LDA     ($00),Y             ; {ram.GP_00}
91F0: C9 FF           CMP     #$FF                
91F2: F0 CB           BEQ     $91BF               ; {}
91F4: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
91F7: 4C ED 91        JMP     $91ED               ; {}
91FA: 0A              ASL     A                   
91FB: 92 ; ????
91FC: 0A              ASL     A                   
91FD: 92 ; ????
91FE: 17 ; ????
91FF: 92 ; ????
9200: 17 ; ????
9201: 92 ; ????
9202: 1F ; ????
9203: 92 ; ????
9204: 23 ; ????
9205: 92 ; ????
9206: 27 ; ????
9207: 92 ; ????
9208: 32 ; ????
9209: 92 ; ????
920A: 28              PLP                         
920B: E6 29           INC     $29                 
920D: 24 29           BIT     $29                 
920F: 16 21           ASL     $21,X               
9211: 28              PLP                         
9212: 18              CLC                         
9213: 24 27           BIT     $27                 
9215: 1A ; ????
9216: FF ; ????
9217: 29 0B           AND     #$0B                
9219: 28              PLP                         
921A: 18              CLC                         
921B: 24 27           BIT     $27                 
921D: 1A ; ????
921E: FF ; ????
921F: 2B ; ????
9220: F3 ; ????
9221: 03 ; ????
9222: FF ; ????
9223: 2B ; ????
9224: 36 22           ROL     $22,X               
9226: FF ; ????
9227: 2B ; ????
9228: 36 28           ROL     $28,X               
922A: 29 16           AND     #$16                
922C: 1C ; ????
922D: 1A ; ????
922E: 12 ; ????
922F: 0F ; ????
9230: 12 ; ????
9231: FF ; ????
9232: 2B ; ????
9233: 56 17           LSR     $17,X               
9235: 24 28           BIT     $28                 
9237: 28              PLP                         
9238: FF ; ????
9239: AD 3B 01        LDA     $013B               
923C: F0 81           BEQ     $91BF               ; {}
923E: A5 46           LDA     $46                 
9240: 29 07           AND     #$07                
9242: 85 00           STA     $00                 ; {ram.GP_00}
9244: A9 00           LDA     #$00                
9246: 85 02           STA     $02                 
9248: A5 46           LDA     $46                 
924A: 29 38           AND     #$38                
924C: 0A              ASL     A                   
924D: 26 02           ROL     $02                 
924F: 0A              ASL     A                   
9250: 26 02           ROL     $02                 
9252: 18              CLC                         
9253: 65 00           ADC     $00                 ; {ram.GP_00}
9255: 18              CLC                         
9256: 69 94           ADC     #$94                
9258: 85 01           STA     $01                 
925A: A5 02           LDA     $02                 
925C: 69 20           ADC     #$20                
925E: AA              TAX                         
925F: A4 01           LDY     $01                 
9261: A9 13           LDA     #$13                
9263: 8E 06 20        STX     $2006               ; {hard.P_VRAM_ADDR}
9266: 8C 06 20        STY     $2006               ; {hard.P_VRAM_ADDR}
9269: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
926C: 60              RTS                         
926D: 20 63 92        JSR     $9263               ; {}
9270: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
9273: 60              RTS                         
9274: A5 47           LDA     $47                 
9276: D0 C1           BNE     $9239               ; {}
9278: 20 AC E1        JSR     $E1AC               
927B: A9 94           LDA     #$94                
927D: 85 00           STA     $00                 ; {ram.GP_00}
927F: A9 20           LDA     #$20                
9281: 85 01           STA     $01                 
9283: A0 07           LDY     #$07                
9285: A2 07           LDX     #$07                
9287: A5 01           LDA     $01                 
9289: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
928C: A5 00           LDA     $00                 ; {ram.GP_00}
928E: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
9291: A9 7A           LDA     #$7A                
9293: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
9296: CA              DEX                         
9297: 10 FA           BPL     $9293               ; {}
9299: A5 00           LDA     $00                 ; {ram.GP_00}
929B: 18              CLC                         
929C: 69 20           ADC     #$20                
929E: 85 00           STA     $00                 ; {ram.GP_00}
92A0: A5 01           LDA     $01                 
92A2: 69 00           ADC     #$00                
92A4: 85 01           STA     $01                 
92A6: 88              DEY                         
92A7: 10 DC           BPL     $9285               ; {}
92A9: 4C 39 92        JMP     $9239               ; {}
92AC: A2 EC           LDX     #$EC                
92AE: A9 C8           LDA     #$C8                
92B0: 9D 00 07        STA     $0700,X             
92B3: A9 32           LDA     #$32                
92B5: 9D 03 07        STA     $0703,X             
92B8: A9 64           LDA     #$64                
92BA: 4C CD C4        JMP     $C4CD               
92BD: A5 3A           LDA     $3A                 
92BF: C9 10           CMP     #$10                
92C1: 90 2B           BCC     $92EE               ; {}
92C3: A9 0E           LDA     #$0E                
92C5: 20 90 CA        JSR     $CA90               
92C8: A5 3A           LDA     $3A                 
92CA: 29 0F           AND     #$0F                
92CC: 20 2B EE        JSR     $EE2B               
92CF: EF ; ????
92D0: 90 DD           BCC     $92AF               ; {}
92D2: 92 ; ????
92D3: F7 ; ????
92D4: E0 EF           CPX     #$EF                
92D6: 90 EF           BCC     $92C7               ; {}
92D8: 92 ; ????
92D9: 1C ; ????
92DA: 93 ; ????
92DB: 69 93           ADC     #$93                
92DD: A9 1B           LDA     #$1B                
92DF: 85 46           STA     $46                 
92E1: A9 00           LDA     #$00                
92E3: 85 47           STA     $47                 
92E5: 8D 56 01        STA     $0156               
92E8: 85 6F           STA     $6F                 
92EA: 85 A5           STA     $A5                 
92EC: E6 3A           INC     $3A                 
92EE: 60              RTS                         
92EF: 20 07 98        JSR     $9807               ; {}
92F2: A9 1A           LDA     #$1A                
92F4: 20 90 CA        JSR     $CA90               
92F7: E6 3A           INC     $3A                 
92F9: A9 00           LDA     #$00                
92FB: 8D B9 07        STA     $07B9               
92FE: 60              RTS                         
92FF: 20 B5 98        JSR     $98B5               ; {}
9302: 20 AA 99        JSR     $99AA               ; {}
9305: A5 6F           LDA     $6F                 
9307: D0 09           BNE     $9312               ; {}
9309: 20 60 D6        JSR     $D660               
930C: 20 EF 93        JSR     $93EF               ; {}
930F: 4C 9D 90        JMP     $909D               ; {}
9312: A2 38           LDX     #$38                
9314: 20 9D D6        JSR     $D69D               
9317: A2 3C           LDX     #$3C                
9319: 4C 9D D6        JMP     $D69D               
931C: 20 FF 92        JSR     $92FF               ; {}
931F: A5 3A           LDA     $3A                 
9321: 29 0F           AND     #$0F                
9323: C9 03           CMP     #$03                
9325: 90 D7           BCC     $92FE               ; {}
9327: A5 46           LDA     $46                 
9329: 0A              ASL     A                   
932A: A8              TAY                         
932B: B9 AF 70        LDA     $70AF,Y             
932E: C9 16           CMP     #$16                
9330: F0 07           BEQ     $9339               ; {}
9332: C9 15           CMP     #$15                
9334: F0 08           BEQ     $933E               ; {}
9336: 4C EC 82        JMP     $82EC               ; {}
9339: A9 1C           LDA     #$1C                
933B: 4C 90 CA        JMP     $CA90               
933E: A5 6F           LDA     $6F                 
9340: F0 12           BEQ     $9354               ; {}
9342: A9 1E           LDA     #$1E                
9344: 20 90 CA        JSR     $CA90               
9347: AD 24 07        LDA     $0724               
934A: D0 09           BNE     $9355               ; {}
934C: EE 24 07        INC     $0724               
934F: A9 0C           LDA     #$0C                
9351: 8D E2 04        STA     $04E2               
9354: 60              RTS                         
9355: AD E2 04        LDA     $04E2               
9358: D0 FA           BNE     $9354               ; {}
935A: AD 23 07        LDA     $0723               
935D: 30 F5           BMI     $9354               ; {}
935F: A9 00           LDA     #$00                
9361: 85 6F           STA     $6F                 
9363: A9 10           LDA     #$10                
9365: 8D 81 03        STA     $0381               
9368: 60              RTS                         
9369: 20 FF 92        JSR     $92FF               ; {}
936C: AD 21 07        LDA     $0721               
936F: 29 04           AND     #$04                
9371: D0 12           BNE     $9385               ; {}
9373: 4C BE 93        JMP     $93BE               ; {}
9376: A5 3A           LDA     $3A                 
9378: D0 0B           BNE     $9385               ; {}
937A: 8D 24 07        STA     $0724               
937D: A9 11           LDA     #$11                
937F: 85 3A           STA     $3A                 
9381: A9 02           LDA     #$02                
9383: 85 37           STA     $37                 
9385: 60              RTS                         
9386: A9 00           LDA     #$00                
9388: 8D 24 07        STA     $0724               
938B: 8D 26 07        STA     $0726               
938E: A5 3A           LDA     $3A                 
9390: 29 F0           AND     #$F0                
9392: 09 05           ORA     #$05                
9394: 85 3A           STA     $3A                 
9396: A9 1A           LDA     #$1A                
9398: 4C 90 CA        JMP     $CA90               
939B: A9 FF           LDA     #$FF                
939D: D0 02           BNE     $93A1               ; {}
939F: A9 08           LDA     #$08                
93A1: 8D E2 04        STA     $04E2               
93A4: 60              RTS                         
93A5: A5 14           LDA     $14                 
93A7: 29 03           AND     #$03                
93A9: D0 12           BNE     $93BD               ; {}
93AB: EE 24 07        INC     $0724               
93AE: AD 24 07        LDA     $0724               
93B1: C9 F8           CMP     #$F8                
93B3: B0 D1           BCS     $9386               ; {}
93B5: C9 D0           CMP     #$D0                
93B7: F0 E2           BEQ     $939B               ; {}
93B9: C9 90           CMP     #$90                
93BB: F0 E2           BEQ     $939F               ; {}
93BD: 60              RTS                         
93BE: AD 24 07        LDA     $0724               
93C1: 30 E2           BMI     $93A5               ; {}
93C3: A9 20           LDA     #$20                
93C5: 20 90 CA        JSR     $CA90               
93C8: AD 24 07        LDA     $0724               
93CB: D0 15           BNE     $93E2               ; {}
93CD: A9 22           LDA     #$22                
93CF: 20 90 CA        JSR     $CA90               
93D2: A9 24           LDA     #$24                
93D4: 20 90 CA        JSR     $CA90               
93D7: AD 71 07        LDA     $0771               
93DA: 0D 81 07        ORA     $0781               
93DD: 0D 91 07        ORA     $0791               
93E0: 10 05           BPL     $93E7               ; {}
93E2: A9 26           LDA     #$26                
93E4: 4C 90 CA        JMP     $CA90               
93E7: A9 80           LDA     #$80                
93E9: 8D 24 07        STA     $0724               
93EC: 4C 9B 93        JMP     $939B               ; {}
93EF: A2 38           LDX     #$38                
93F1: A5 3C           LDA     $3C                 
93F3: F0 6F           BEQ     $9464               ; {}
93F5: BD 02 07        LDA     $0702,X             
93F8: F0 6A           BEQ     $9464               ; {}
93FA: C9 08           CMP     #$08                
93FC: B0 66           BCS     $9464               ; {}
93FE: 20 35 E0        JSR     $E035               
9401: C9 6A           CMP     #$6A                
9403: F0 0D           BEQ     $9412               ; {}
9405: C9 6B           CMP     #$6B                
9407: F0 09           BEQ     $9412               ; {}
9409: C9 6C           CMP     #$6C                
940B: F0 15           BEQ     $9422               ; {}
940D: C9 6D           CMP     #$6D                
940F: F0 18           BEQ     $9429               ; {}
9411: 60              RTS                         
9412: 20 4D 94        JSR     $944D               ; {}
9415: A9 80           LDA     #$80                
9417: 20 65 94        JSR     $9465               ; {}
941A: A9 20           LDA     #$20                
941C: 8D 80 03        STA     $0380               
941F: 4C D5 D9        JMP     $D9D5               
9422: 20 4D 94        JSR     $944D               ; {}
9425: A9 90           LDA     #$90                
9427: D0 EE           BNE     $9417               ; {}
9429: 20 4D 94        JSR     $944D               ; {}
942C: A9 A0           LDA     #$A0                
942E: 20 17 94        JSR     $9417               ; {}
9431: AD 4A 01        LDA     $014A               
9434: 38              SEC                         
9435: E9 0A           SBC     #$0A                
9437: 8D 4A 01        STA     $014A               
943A: AD 4B 01        LDA     $014B               
943D: E9 00           SBC     #$00                
943F: 8D 4B 01        STA     $014B               
9442: B0 08           BCS     $944C               ; {}
9444: A9 00           LDA     #$00                
9446: 8D 4A 01        STA     $014A               
9449: 8D 4B 01        STA     $014B               
944C: 60              RTS                         
944D: A0 00           LDY     #$00                
944F: 98              TYA                         
9450: 91 00           STA     ($00),Y             ; {ram.GP_00}
9452: 20 3D 96        JSR     $963D               ; {}
9455: 20 FA 99        JSR     $99FA               ; {}
9458: A9 01           LDA     #$01                
945A: 85 68           STA     $68                 
945C: A5 00           LDA     $00                 ; {ram.GP_00}
945E: 85 69           STA     $69                 
9460: A5 01           LDA     $01                 
9462: 85 6A           STA     $6A                 
9464: 60              RTS                         
9465: A2 A0           LDX     #$A0                
9467: A0 38           LDY     #$38                
9469: 9D 01 07        STA     $0701,X             
946C: A9 18           LDA     #$18                
946E: 9D 06 07        STA     $0706,X             
9471: EE 56 01        INC     $0156               
9474: B9 00 07        LDA     $0700,Y             
9477: 18              CLC                         
9478: 69 04           ADC     #$04                
947A: 9D 00 07        STA     $0700,X             
947D: B9 03 07        LDA     $0703,Y             
9480: 9D 03 07        STA     $0703,X             
9483: 30 04           BMI     $9489               ; {}
9485: A9 A5           LDA     #$A5                
9487: D0 02           BNE     $948B               ; {}
9489: A9 AA           LDA     #$AA                
948B: 9D 02 07        STA     $0702,X             
948E: 60              RTS                         
948F: A0 20           LDY     #$20                
9491: 20 86 D9        JSR     $D986               
9494: 90 04           BCC     $949A               ; {}
9496: A9 36           LDA     #$36                
9498: D0 48           BNE     $94E2               ; {}
949A: A9 07           LDA     #$07                
949C: 85 A6           STA     $A6                 
949E: 4C 1D DD        JMP     $DD1D               
94A1: 20 1B 95        JSR     $951B               ; {}
94A4: 20 C0 DB        JSR     $DBC0               
94A7: A9 3A           LDA     #$3A                
94A9: D0 37           BNE     $94E2               ; {}
94AB: A2 A0           LDX     #$A0                
94AD: BD 01 07        LDA     $0701,X             
94B0: F0 36           BEQ     $94E8               ; {}
94B2: BD 00 07        LDA     $0700,X             
94B5: C9 04           CMP     #$04                
94B7: 90 2C           BCC     $94E5               ; {}
94B9: BD 06 07        LDA     $0706,X             
94BC: D0 2B           BNE     $94E9               ; {}
94BE: BD 01 07        LDA     $0701,X             
94C1: 29 30           AND     #$30                
94C3: C9 10           CMP     #$10                
94C5: F0 C8           BEQ     $948F               ; {}
94C7: C9 20           CMP     #$20                
94C9: F0 D6           BEQ     $94A1               ; {}
94CB: 20 1B 95        JSR     $951B               ; {}
94CE: 20 C0 DB        JSR     $DBC0               
94D1: A0 64           LDY     #$64                
94D3: A5 14           LDA     $14                 
94D5: 29 08           AND     #$08                
94D7: D0 02           BNE     $94DB               ; {}
94D9: C8              INY                         
94DA: C8              INY                         
94DB: BD 04 07        LDA     $0704,X             
94DE: 30 01           BMI     $94E1               ; {}
94E0: C8              INY                         
94E1: 98              TYA                         
94E2: 4C CD C4        JMP     $C4CD               
94E5: 20 1D DD        JSR     $DD1D               
94E8: 60              RTS                         
94E9: DE 06 07        DEC     $0706,X             
94EC: C9 10           CMP     #$10                
94EE: B0 27           BCS     $9517               ; {}
94F0: C9 08           CMP     #$08                
94F2: B0 1F           BCS     $9513               ; {}
94F4: A9 4A           LDA     #$4A                
94F6: 9D 01 02        STA     $0201,X             
94F9: 9D 05 02        STA     $0205,X             
94FC: 9D 09 02        STA     $0209,X             
94FF: 9D 0D 02        STA     $020D,X             
9502: A9 00           LDA     #$00                
9504: 9D 02 02        STA     $0202,X             
9507: 9D 06 02        STA     $0206,X             
950A: 9D 0A 02        STA     $020A,X             
950D: 9D 0E 02        STA     $020E,X             
9510: 4C 3D DD        JMP     $DD3D               
9513: A9 5A           LDA     #$5A                
9515: D0 DF           BNE     $94F6               ; {}
9517: A9 4B           LDA     #$4B                
9519: D0 DB           BNE     $94F6               ; {}
951B: BD 03 07        LDA     $0703,X             
951E: 30 04           BMI     $9524               ; {}
9520: A9 A7           LDA     #$A7                
9522: D0 02           BNE     $9526               ; {}
9524: A9 A8           LDA     #$A8                
9526: 9D 02 07        STA     $0702,X             
9529: 60              RTS                         
952A: A5 46           LDA     $46                 
952C: 38              SEC                         
952D: E9 08           SBC     #$08                
952F: 85 46           STA     $46                 
9531: A5 3A           LDA     $3A                 
9533: 29 F0           AND     #$F0                
9535: 09 02           ORA     #$02                
9537: 85 3A           STA     $3A                 
9539: A5 37           LDA     $37                 
953B: 09 04           ORA     #$04                
953D: 85 37           STA     $37                 
953F: 60              RTS                         
9540: A5 46           LDA     $46                 
9542: 18              CLC                         
9543: 69 08           ADC     #$08                
9545: 4C 2F 95        JMP     $952F               ; {}
9548: E6 46           INC     $46                 
954A: 4C 31 95        JMP     $9531               ; {}
954D: C6 46           DEC     $46                 
954F: 4C 31 95        JMP     $9531               ; {}
9552: 85 00           STA     $00                 ; {ram.GP_00}
9554: A5 46           LDA     $46                 
9556: 0A              ASL     A                   
9557: 18              CLC                         
9558: 65 00           ADC     $00                 ; {ram.GP_00}
955A: A8              TAY                         
955B: B9 AF 70        LDA     $70AF,Y             
955E: 60              RTS                         
955F: A9 01           LDA     #$01                
9561: 20 52 95        JSR     $9552               ; {}
9564: 29 0F           AND     #$0F                
9566: 85 08           STA     $08                 
9568: A0 00           LDY     #$00                
956A: 20 79 95        JSR     $9579               ; {}
956D: A0 10           LDY     #$10                
956F: 20 79 95        JSR     $9579               ; {}
9572: A0 20           LDY     #$20                
9574: 20 79 95        JSR     $9579               ; {}
9577: A0 30           LDY     #$30                
9579: A5 08           LDA     $08                 
957B: 39 C3 95        AND     $95C3,Y             ; {}
957E: F0 42           BEQ     $95C2               ; {}
9580: BE C5 95        LDX     $95C5,Y             ; {}
9583: B9 C6 95        LDA     $95C6,Y             ; {}
9586: 9D 00 05        STA     $0500,X             
9589: BE C7 95        LDX     $95C7,Y             ; {}
958C: B9 C8 95        LDA     $95C8,Y             ; {}
958F: 9D 00 05        STA     $0500,X             
9592: BE C9 95        LDX     $95C9,Y             ; {}
9595: B9 CA 95        LDA     $95CA,Y             ; {}
9598: 9D 00 05        STA     $0500,X             
959B: BE CB 95        LDX     $95CB,Y             ; {}
959E: B9 CC 95        LDA     $95CC,Y             ; {}
95A1: 9D 00 05        STA     $0500,X             
95A4: BE CD 95        LDX     $95CD,Y             ; {}
95A7: BD 00 04        LDA     $0400,X             
95AA: 39 CE 95        AND     $95CE,Y             ; {}
95AD: 19 CF 95        ORA     $95CF,Y             ; {}
95B0: 9D 00 04        STA     $0400,X             
95B3: BE D0 95        LDX     $95D0,Y             ; {}
95B6: BD 00 04        LDA     $0400,X             
95B9: 39 D1 95        AND     $95D1,Y             ; {}
95BC: 19 D2 95        ORA     $95D2,Y             ; {}
95BF: 9D 00 04        STA     $0400,X             
95C2: 60              RTS                         
95C3: 01 04           ORA     ($04,X)             
95C5: 07 ; ????
95C6: 2E 08 2F        ROL     $2F08               
95C9: 17 ; ????
95CA: 2E 18 2F        ROL     $2F18               
95CD: 03 ; ????
95CE: 33 ; ????
95CF: 88              DEY                         
95D0: 04 ; ????
95D1: CC 22 02        CPY     $0222               
95D4: 08              PHP                         
95D5: 6F ; ????
95D6: 50 6F           BVC     $9647               ; {}
95D8: 50 7F           BVC     $9659               ; {}
95DA: 2A              ROL     A                   
95DB: 7F ; ????
95DC: 2A              ROL     A                   
95DD: 1F ; ????
95DE: 33 ; ????
95DF: 88              DEY                         
95E0: 1F ; ????
95E1: 33 ; ????
95E2: 88              DEY                         
95E3: 04 ; ????
95E4: 0C ; ????
95E5: B7 ; ????
95E6: 68              PLA                         
95E7: B8              CLV                         
95E8: 69 B7           ADC     #$B7                
95EA: 68              PLA                         
95EB: B8              CLV                         
95EC: 69 2B           ADC     #$2B                
95EE: 3F ; ????
95EF: 80 ; ????
95F0: 2C CF 20        BIT     $20CF               
95F3: 08              PHP                         
95F4: 10 60           BPL     $9656               ; {}
95F6: 50 60           BVC     $9658               ; {}
95F8: 50 70           BVC     $966A               ; {}
95FA: 2A              ROL     A                   
95FB: 70 2A           BVS     $9627               ; {}
95FD: 18              CLC                         
95FE: CC 22 18        CPY     $1822               
9601: CC 22 A0        CPY     $A022               ; {}
9604: 07 ; ????
9605: A9 00           LDA     #$00                
9607: 99 30 04        STA     $0430,Y             
960A: 88              DEY                         
960B: 10 FA           BPL     $9607               ; {}
960D: 60              RTS                         
960E: A0 00           LDY     #$00                
9610: B9 BD 71        LDA     $71BD,Y             
9613: C9 FF           CMP     #$FF                
9615: F0 0A           BEQ     $9621               ; {}
9617: 29 3F           AND     #$3F                
9619: C5 46           CMP     $46                 
961B: F0 05           BEQ     $9622               ; {}
961D: C8              INY                         
961E: C8              INY                         
961F: D0 EF           BNE     $9610               ; {}
9621: 60              RTS                         
9622: B9 BE 71        LDA     $71BE,Y             
9625: F0 F6           BEQ     $961D               ; {}
9627: AA              TAX                         
9628: B9 BD 71        LDA     $71BD,Y             
962B: 29 C0           AND     #$C0                
962D: 18              CLC                         
962E: 2A              ROL     A                   
962F: 2A              ROL     A                   
9630: 2A              ROL     A                   
9631: 18              CLC                         
9632: 69 6A           ADC     #$6A                
9634: 9D 00 05        STA     $0500,X             
9637: 20 63 96        JSR     $9663               ; {}
963A: 4C 1D 96        JMP     $961D               ; {}
963D: A0 00           LDY     #$00                
963F: B9 BD 71        LDA     $71BD,Y             
9642: C9 FF           CMP     #$FF                
9644: F0 0A           BEQ     $9650               ; {}
9646: 29 3F           AND     #$3F                
9648: C5 46           CMP     $46                 
964A: F0 05           BEQ     $9651               ; {}
964C: C8              INY                         
964D: C8              INY                         
964E: D0 EF           BNE     $963F               ; {}
9650: 60              RTS                         
9651: B9 BE 71        LDA     $71BE,Y             
9654: C5 00           CMP     $00                 ; {ram.GP_00}
9656: F0 05           BEQ     $965D               ; {}
9658: C8              INY                         
9659: C8              INY                         
965A: D0 F5           BNE     $9651               ; {}
965C: 60              RTS                         
965D: A9 00           LDA     #$00                
965F: 99 BE 71        STA     $71BE,Y             
9662: 60              RTS                         
9663: 98              TYA                         
9664: 48              PHA                         
9665: 8A              TXA                         
9666: 4A              LSR     A                   
9667: 4A              LSR     A                   
9668: 48              PHA                         
9669: 29 30           AND     #$30                
966B: 85 00           STA     $00                 ; {ram.GP_00}
966D: 68              PLA                         
966E: 29 08           AND     #$08                
9670: 85 01           STA     $01                 
9672: 8A              TXA                         
9673: 4A              LSR     A                   
9674: 29 07           AND     #$07                
9676: 05 01           ORA     $01                 
9678: 05 00           ORA     $00                 ; {ram.GP_00}
967A: A8              TAY                         
967B: 8A              TXA                         
967C: 29 10           AND     #$10                
967E: 4A              LSR     A                   
967F: 4A              LSR     A                   
9680: 4A              LSR     A                   
9681: 85 01           STA     $01                 
9683: 8A              TXA                         
9684: 29 01           AND     #$01                
9686: 05 01           ORA     $01                 
9688: AA              TAX                         
9689: B9 00 04        LDA     $0400,Y             
968C: 3D 98 96        AND     $9698,X             ; {}
968F: 1D 9C 96        ORA     $969C,X             ; {}
9692: 99 00 04        STA     $0400,Y             
9695: 68              PLA                         
9696: A8              TAY                         
9697: 60              RTS                         
9698: FC ; ????
9699: F3 ; ????
969A: CF ; ????
969B: 3F ; ????
969C: 03 ; ????
969D: 0C ; ????
969E: 30 C0           BMI     $9660               ; {}
96A0: AD 71 07        LDA     $0771               
96A3: 0D 81 07        ORA     $0781               
96A6: 0D 91 07        ORA     $0791               
96A9: D0 1E           BNE     $96C9               ; {}
96AB: AD 56 01        LDA     $0156               
96AE: F0 19           BEQ     $96C9               ; {}
96B0: 30 18           BMI     $96CA               ; {}
96B2: C9 01           CMP     #$01                
96B4: F0 0E           BEQ     $96C4               ; {}
96B6: C9 02           CMP     #$02                
96B8: F0 05           BEQ     $96BF               ; {}
96BA: A2 70           LDX     #$70                
96BC: 20 D0 96        JSR     $96D0               ; {}
96BF: A2 80           LDX     #$80                
96C1: 20 D0 96        JSR     $96D0               ; {}
96C4: A2 90           LDX     #$90                
96C6: 20 D0 96        JSR     $96D0               ; {}
96C9: 60              RTS                         
96CA: A9 00           LDA     #$00                
96CC: 8D 56 01        STA     $0156               
96CF: 60              RTS                         
96D0: BD 01 07        LDA     $0701,X             
96D3: D0 31           BNE     $9706               ; {}
96D5: 9D 00 07        STA     $0700,X             
96D8: 9D 04 07        STA     $0704,X             
96DB: 9D 05 07        STA     $0705,X             
96DE: 9D 07 07        STA     $0707,X             
96E1: AD 23 07        LDA     $0723               
96E4: 9D 03 07        STA     $0703,X             
96E7: CE 56 01        DEC     $0156               
96EA: A9 80           LDA     #$80                
96EC: 9D 01 07        STA     $0701,X             
96EF: A5 1C           LDA     $1C                 
96F1: 30 09           BMI     $96FC               ; {}
96F3: A9 D5           LDA     #$D5                
96F5: 9D 02 07        STA     $0702,X             
96F8: A9 20           LDA     #$20                
96FA: D0 07           BNE     $9703               ; {}
96FC: A9 DB           LDA     #$DB                
96FE: 9D 02 07        STA     $0702,X             
9701: A9 E0           LDA     #$E0                
9703: 9D 04 07        STA     $0704,X             
9706: 60              RTS                         
9707: 20 A0 96        JSR     $96A0               ; {}
970A: A2 70           LDX     #$70                
970C: 20 16 97        JSR     $9716               ; {}
970F: A2 80           LDX     #$80                
9711: 20 16 97        JSR     $9716               ; {}
9714: A2 90           LDX     #$90                
9716: BD 01 07        LDA     $0701,X             
9719: F0 EB           BEQ     $9706               ; {}
971B: 29 07           AND     #$07                
971D: C9 01           CMP     #$01                
971F: F0 1F           BEQ     $9740               ; {}
9721: 20 54 97        JSR     $9754               ; {}
9724: 20 62 97        JSR     $9762               ; {}
9727: 20 AA 97        JSR     $97AA               ; {}
972A: 20 C0 DB        JSR     $DBC0               
972D: A0 64           LDY     #$64                
972F: A5 14           LDA     $14                 
9731: 29 08           AND     #$08                
9733: D0 02           BNE     $9737               ; {}
9735: C8              INY                         
9736: C8              INY                         
9737: A5 1C           LDA     $1C                 
9739: 30 01           BMI     $973C               ; {}
973B: C8              INY                         
973C: 98              TYA                         
973D: 4C CD C4        JMP     $C4CD               
9740: BD 00 07        LDA     $0700,X             
9743: C9 F8           CMP     #$F8                
9745: B0 0A           BCS     $9751               ; {}
9747: FE 00 07        INC     $0700,X             
974A: FE 00 07        INC     $0700,X             
974D: A9 94           LDA     #$94                
974F: D0 EC           BNE     $973D               ; {}
9751: 4C 1D DD        JMP     $DD1D               
9754: A0 01           LDY     #$01                
9756: E0 70           CPX     #$70                
9758: F0 07           BEQ     $9761               ; {}
975A: 88              DEY                         
975B: E0 80           CPX     #$80                
975D: F0 02           BEQ     $9761               ; {}
975F: A0 02           LDY     #$02                
9761: 60              RTS                         
9762: AD 23 07        LDA     $0723               
9765: 20 9C 97        JSR     $979C               ; {}
9768: 38              SEC                         
9769: FD 03 07        SBC     $0703,X             
976C: 90 17           BCC     $9785               ; {}
976E: C9 08           CMP     #$08                
9770: 90 0A           BCC     $977C               ; {}
9772: BD 02 07        LDA     $0702,X             
9775: 29 F0           AND     #$F0                
9777: 19 93 97        ORA     $9793,Y             ; {}
977A: D0 05           BNE     $9781               ; {}
977C: BD 02 07        LDA     $0702,X             
977F: 29 F0           AND     #$F0                
9781: 9D 02 07        STA     $0702,X             
9784: 60              RTS                         
9785: C9 F0           CMP     #$F0                
9787: B0 F3           BCS     $977C               ; {}
9789: BD 02 07        LDA     $0702,X             
978C: 29 F0           AND     #$F0                
978E: 19 96 97        ORA     $9796,Y             ; {}
9791: D0 EE           BNE     $9781               ; {}
9793: 06 04           ASL     $04                 
9795: 03 ; ????
9796: 09 0A           ORA     #$0A                
9798: 0B ; ????
9799: 18              CLC                         
979A: 10 08           BPL     $97A4               ; {}
979C: 24 1C           BIT     $1C                 
979E: 30 05           BMI     $97A5               ; {}
97A0: 18              CLC                         
97A1: 79 99 97        ADC     $9799,Y             ; {}
97A4: 60              RTS                         
97A5: 38              SEC                         
97A6: F9 99 97        SBC     $9799,Y             ; {}
97A9: 60              RTS                         
97AA: AD 20 07        LDA     $0720               
97AD: 38              SEC                         
97AE: F9 D6 97        SBC     $97D6,Y             ; {}
97B1: 38              SEC                         
97B2: FD 00 07        SBC     $0700,X             
97B5: 90 09           BCC     $97C0               ; {}
97B7: BD 02 07        LDA     $0702,X             
97BA: 29 0F           AND     #$0F                
97BC: 09 40           ORA     #$40                
97BE: D0 C1           BNE     $9781               ; {}
97C0: AD 20 07        LDA     $0720               
97C3: 38              SEC                         
97C4: F9 D9 97        SBC     $97D9,Y             ; {}
97C7: 38              SEC                         
97C8: FD 00 07        SBC     $0700,X             
97CB: B0 DC           BCS     $97A9               ; {}
97CD: BD 02 07        LDA     $0702,X             
97D0: 29 0F           AND     #$0F                
97D2: 09 B0           ORA     #$B0                
97D4: D0 AB           BNE     $9781               ; {}
97D6: 18              CLC                         
97D7: 30 48           BMI     $9821               ; {}
97D9: 10 28           BPL     $9803               ; {}
97DB: 40              RTI                         
97DC: A0 70           LDY     #$70                
97DE: 20 EC 97        JSR     $97EC               ; {}
97E1: 90 23           BCC     $9806               ; {}
97E3: A0 80           LDY     #$80                
97E5: 20 EC 97        JSR     $97EC               ; {}
97E8: 90 1C           BCC     $9806               ; {}
97EA: A0 90           LDY     #$90                
97EC: B9 01 07        LDA     $0701,Y             
97EF: 30 02           BMI     $97F3               ; {}
97F1: 38              SEC                         
97F2: 60              RTS                         
97F3: 20 86 D9        JSR     $D986               
97F6: 60              RTS                         
97F7: 20 DC 97        JSR     $97DC               ; {}
97FA: B0 0A           BCS     $9806               ; {}
97FC: A9 81           LDA     #$81                
97FE: 99 01 07        STA     $0701,Y             
9801: A9 80           LDA     #$80                
9803: 8D 80 03        STA     $0380               
9806: 60              RTS                         
9807: 20 4D 81        JSR     $814D               ; {}
980A: A5 47           LDA     $47                 
980C: 0A              ASL     A                   
980D: 0A              ASL     A                   
980E: A8              TAY                         
980F: B9 27 98        LDA     $9827,Y             ; {}
9812: 9D 00 07        STA     $0700,X             
9815: B9 28 98        LDA     $9828,Y             ; {}
9818: 9D 03 07        STA     $0703,X             
981B: B9 29 98        LDA     $9829,Y             ; {}
981E: 9D 01 07        STA     $0701,X             
9821: B9 2A 98        LDA     $982A,Y             ; {}
9824: 85 1C           STA     $1C                 
9826: 60              RTS                         
9827: 78              SEI                         
9828: 14 ; ????
9829: 81 00           STA     ($00,X)             ; {ram.GP_00}
982B: 04 ; ????
982C: 7C ; ????
982D: 85 00           STA     $00                 ; {ram.GP_00}
982F: 7A ; ????
9830: E0 81           CPX     #$81                
9832: FF ; ????
9833: D0 7C           BNE     $98B1               ; {}
9835: 86 00           STX     $00                 ; {ram.GP_00}
9837: 7A ; ????
9838: 18              CLC                         
9839: 81 00           STA     ($00,X)             ; {ram.GP_00}
983B: BD 00 07        LDA     $0700,X             
983E: C9 28           CMP     #$28                
9840: B0 06           BCS     $9848               ; {}
9842: FE 00 07        INC     $0700,X             
9845: 4C 8C 98        JMP     $988C               ; {}
9848: A9 81           LDA     #$81                
984A: 9D 01 07        STA     $0701,X             
984D: 60              RTS                         
984E: BD 00 07        LDA     $0700,X             
9851: C9 AA           CMP     #$AA                
9853: 90 F3           BCC     $9848               ; {}
9855: DE 00 07        DEC     $0700,X             
9858: 4C 8C 98        JMP     $988C               ; {}
985B: F0 0F           BEQ     $986C               ; {}
985D: C9 04           CMP     #$04                
985F: F0 38           BEQ     $9899               ; {}
9861: C9 05           CMP     #$05                
9863: F0 D6           BEQ     $983B               ; {}
9865: C9 06           CMP     #$06                
9867: F0 E5           BEQ     $984E               ; {}
9869: 4C CD 98        JMP     $98CD               ; {}
986C: BD 00 07        LDA     $0700,X             
986F: C9 04           CMP     #$04                
9871: B0 0F           BCS     $9882               ; {}
9873: A9 00           LDA     #$00                
9875: 9D 04 07        STA     $0704,X             
9878: 4C 2A 95        JMP     $952A               ; {}
987B: FE 04 07        INC     $0704,X             
987E: A9 70           LDA     #$70                
9880: D0 14           BNE     $9896               ; {}
9882: BD 04 07        LDA     $0704,X             
9885: C9 08           CMP     #$08                
9887: 90 F2           BCC     $987B               ; {}
9889: DE 00 07        DEC     $0700,X             
988C: A0 70           LDY     #$70                
988E: A5 14           LDA     $14                 
9890: 29 08           AND     #$08                
9892: D0 01           BNE     $9895               ; {}
9894: C8              INY                         
9895: 98              TYA                         
9896: 4C CD C4        JMP     $C4CD               
9899: BD 04 07        LDA     $0704,X             
989C: C9 08           CMP     #$08                
989E: 90 DB           BCC     $987B               ; {}
98A0: BD 00 07        LDA     $0700,X             
98A3: C9 D0           CMP     #$D0                
98A5: 90 08           BCC     $98AF               ; {}
98A7: A9 00           LDA     #$00                
98A9: 9D 04 07        STA     $0704,X             
98AC: 4C 40 95        JMP     $9540               ; {}
98AF: FE 00 07        INC     $0700,X             
98B2: 4C 8C 98        JMP     $988C               ; {}
98B5: 20 F6 8F        JSR     $8FF6               ; {}
98B8: A2 20           LDX     #$20                
98BA: 20 B8 DF        JSR     $DFB8               
98BD: BD 01 07        LDA     $0701,X             
98C0: 29 40           AND     #$40                
98C2: D0 19           BNE     $98DD               ; {}
98C4: BD 01 07        LDA     $0701,X             
98C7: 29 0F           AND     #$0F                
98C9: C9 03           CMP     #$03                
98CB: B0 8E           BCS     $985B               ; {}
98CD: A5 6F           LDA     $6F                 
98CF: D0 03           BNE     $98D4               ; {}
98D1: 20 48 CF        JSR     $CF48               
98D4: 20 A9 CF        JSR     $CFA9               
98D7: 20 D9 C3        JSR     $C3D9               
98DA: 4C E0 98        JMP     $98E0               ; {}
98DD: 4C 5C CC        JMP     $CC5C               
98E0: AD D5 04        LDA     $04D5               
98E3: C9 2F           CMP     #$2F                
98E5: F0 24           BEQ     $990B               ; {}
98E7: AD D6 04        LDA     $04D6               
98EA: C9 2E           CMP     #$2E                
98EC: F0 1D           BEQ     $990B               ; {}
98EE: AD D5 04        LDA     $04D5               
98F1: C9 2A           CMP     #$2A                
98F3: F0 39           BEQ     $992E               ; {}
98F5: AD D6 04        LDA     $04D6               
98F8: C9 2A           CMP     #$2A                
98FA: F0 32           BEQ     $992E               ; {}
98FC: AD D3 04        LDA     $04D3               
98FF: C9 69           CMP     #$69                
9901: F0 3E           BEQ     $9941               ; {}
9903: AD D4 04        LDA     $04D4               
9906: C9 68           CMP     #$68                
9908: F0 37           BEQ     $9941               ; {}
990A: 60              RTS                         
990B: A5 16           LDA     $16                 
990D: 29 08           AND     #$08                
990F: F0 F9           BEQ     $990A               ; {}
9911: BD 00 07        LDA     $0700,X             
9914: 29 F8           AND     #$F8                
9916: C9 20           CMP     #$20                
9918: D0 F0           BNE     $990A               ; {}
991A: BD 01 07        LDA     $0701,X             
991D: 29 F0           AND     #$F0                
991F: 09 03           ORA     #$03                
9921: 9D 01 07        STA     $0701,X             
9924: A9 03           LDA     #$03                
9926: 85 47           STA     $47                 
9928: A9 00           LDA     #$00                
992A: 9D 04 07        STA     $0704,X             
992D: 60              RTS                         
992E: BD 03 07        LDA     $0703,X             
9931: 10 07           BPL     $993A               ; {}
9933: A9 04           LDA     #$04                
9935: 85 47           STA     $47                 
9937: 4C 48 95        JMP     $9548               ; {}
993A: A9 02           LDA     #$02                
993C: 85 47           STA     $47                 
993E: 4C 4D 95        JMP     $954D               ; {}
9941: A5 16           LDA     $16                 
9943: 29 04           AND     #$04                
9945: F0 C3           BEQ     $990A               ; {}
9947: BD 01 07        LDA     $0701,X             
994A: 29 F0           AND     #$F0                
994C: 09 04           ORA     #$04                
994E: 9D 01 07        STA     $0701,X             
9951: A9 00           LDA     #$00                
9953: 9D 04 07        STA     $0704,X             
9956: BD 00 07        LDA     $0700,X             
9959: 18              CLC                         
995A: 69 08           ADC     #$08                
995C: 9D 00 07        STA     $0700,X             
995F: A9 01           LDA     #$01                
9961: 85 47           STA     $47                 
9963: 60              RTS                         
9964: A2 40           LDX     #$40                
9966: A0 70           LDY     #$70                
9968: 20 82 99        JSR     $9982               ; {}
996B: 20 6B D6        JSR     $D66B               
996E: A2 44           LDX     #$44                
9970: A0 80           LDY     #$80                
9972: 20 82 99        JSR     $9982               ; {}
9975: 20 6B D6        JSR     $D66B               
9978: A2 48           LDX     #$48                
997A: A0 90           LDY     #$90                
997C: 20 82 99        JSR     $9982               ; {}
997F: 4C 6B D6        JMP     $D66B               
9982: BD 01 07        LDA     $0701,X             
9985: 30 1E           BMI     $99A5               ; {}
9987: 24 18           BIT     $18                 
9989: 50 1A           BVC     $99A5               ; {}
998B: A9 80           LDA     #$80                
998D: 9D 02 07        STA     $0702,X             
9990: B9 00 07        LDA     $0700,Y             
9993: 9D 00 07        STA     $0700,X             
9996: B9 03 07        LDA     $0703,Y             
9999: 9D 03 07        STA     $0703,X             
999C: A5 1C           LDA     $1C                 
999E: 30 06           BMI     $99A6               ; {}
99A0: A9 84           LDA     #$84                
99A2: 9D 01 07        STA     $0701,X             
99A5: 60              RTS                         
99A6: A9 8C           LDA     #$8C                
99A8: D0 F8           BNE     $99A2               ; {}
99AA: A5 6F           LDA     $6F                 
99AC: F0 33           BEQ     $99E1               ; {}
99AE: 8A              TXA                         
99AF: 48              PHA                         
99B0: A0 04           LDY     #$04                
99B2: A9 0C           LDA     #$0C                
99B4: 85 00           STA     $00                 ; {ram.GP_00}
99B6: A5 16           LDA     $16                 
99B8: 29 04           AND     #$04                
99BA: F0 02           BEQ     $99BE               ; {}
99BC: A0 00           LDY     #$00                
99BE: A5 1C           LDA     $1C                 
99C0: 30 07           BMI     $99C9               ; {}
99C2: 98              TYA                         
99C3: 18              CLC                         
99C4: 69 0C           ADC     #$0C                
99C6: A8              TAY                         
99C7: 06 00           ASL     $00                 ; {ram.GP_00}
99C9: B9 E2 99        LDA     $99E2,Y             ; {}
99CC: 9D 01 02        STA     $0201,X             
99CF: B9 E3 99        LDA     $99E3,Y             ; {}
99D2: 9D 02 02        STA     $0202,X             
99D5: E8              INX                         
99D6: E8              INX                         
99D7: E8              INX                         
99D8: E8              INX                         
99D9: C8              INY                         
99DA: C8              INY                         
99DB: C4 00           CPY     $00                 ; {ram.GP_00}
99DD: 90 EA           BCC     $99C9               ; {}
99DF: 68              PLA                         
99E0: AA              TAX                         
99E1: 60              RTS                         
99E2: 5F ; ????
99E3: 01 5F           ORA     ($5F,X)             
99E5: 01 5F           ORA     ($5F,X)             
99E7: 01 35           ORA     ($35,X)             
99E9: 01 36           ORA     ($36,X)             
99EB: 01 37           ORA     ($37,X)             
99ED: 01 5F           ORA     ($5F,X)             
99EF: 01 5F           ORA     ($5F,X)             
99F1: 01 35           ORA     ($35,X)             
99F3: 41 5F           EOR     ($5F,X)             
99F5: 41 37           EOR     ($37,X)             
99F7: 41 36           EOR     ($36,X)             
99F9: 41 A5           EOR     ($A5,X)             
99FB: 00              BRK                         
99FC: 85 02           STA     $02                 
99FE: 38              SEC                         
99FF: E9 F0           SBC     #$F0                
9A01: 85 00           STA     $00                 ; {ram.GP_00}
9A03: A5 01           LDA     $01                 
9A05: E9 05           SBC     #$05                
9A07: B0 04           BCS     $9A0D               ; {}
9A09: A5 02           LDA     $02                 
9A0B: 85 00           STA     $00                 ; {ram.GP_00}
9A0D: A9 08           LDA     #$08                
9A0F: 85 01           STA     $01                 
9A11: A5 00           LDA     $00                 ; {ram.GP_00}
9A13: 48              PHA                         
9A14: 29 F0           AND     #$F0                
9A16: 0A              ASL     A                   
9A17: 26 01           ROL     $01                 
9A19: 0A              ASL     A                   
9A1A: 26 01           ROL     $01                 
9A1C: 85 00           STA     $00                 ; {ram.GP_00}
9A1E: 68              PLA                         
9A1F: 29 0F           AND     #$0F                
9A21: 0A              ASL     A                   
9A22: 18              CLC                         
9A23: 65 00           ADC     $00                 ; {ram.GP_00}
9A25: 85 00           STA     $00                 ; {ram.GP_00}
9A27: AD D1 04        LDA     $04D1               
9A2A: 4A              LSR     A                   
9A2B: B0 06           BCS     $9A33               ; {}
9A2D: A5 01           LDA     $01                 
9A2F: 69 08           ADC     #$08                
9A31: 85 01           STA     $01                 
9A33: 60              RTS                         
9A34: 20 43 9A        JSR     $9A43               ; {}
9A37: 20 69 9A        JSR     $9A69               ; {}
9A3A: 20 76 9A        JSR     $9A76               ; {}
9A3D: A9 05           LDA     #$05                
9A3F: 8D 74 01        STA     $0174               
9A42: 60              RTS                         
9A43: 8D 77 01        STA     $0177               
9A46: 85 06           STA     $06                 
9A48: 86 07           STX     $07                 
9A4A: 0A              ASL     A                   
9A4B: 0A              ASL     A                   
9A4C: 85 05           STA     $05                 
9A4E: A9 07           LDA     #$07                
9A50: 85 09           STA     $09                 
9A52: A9 02           LDA     #$02                
9A54: 85 0B           STA     $0B                 
9A56: 60              RTS                         
9A57: AD 77 01        LDA     $0177               
9A5A: 4C 46 9A        JMP     $9A46               ; {}
9A5D: 18              CLC                         
9A5E: 65 07           ADC     $07                 
9A60: 85 0A           STA     $0A                 
9A62: 60              RTS                         
9A63: 18              CLC                         
9A64: 65 07           ADC     $07                 
9A66: 85 08           STA     $08                 
9A68: 60              RTS                         
9A69: 86 0A           STX     $0A                 
9A6B: A4 05           LDY     $05                 
9A6D: 88              DEY                         
9A6E: A9 F8           LDA     #$F8                
9A70: 91 0A           STA     ($0A),Y             
9A72: 88              DEY                         
9A73: 10 FB           BPL     $9A70               ; {}
9A75: 60              RTS                         
9A76: A9 0C           LDA     #$0C                
9A78: 20 63 9A        JSR     $9A63               ; {}
9A7B: A0 20           LDY     #$20                
9A7D: 88              DEY                         
9A7E: A9 00           LDA     #$00                
9A80: 91 08           STA     ($08),Y             
9A82: 88              DEY                         
9A83: 10 FB           BPL     $9A80               ; {}
9A85: 60              RTS                         
9A86: 20 57 9A        JSR     $9A57               ; {}
9A89: AD 74 01        LDA     $0174               
9A8C: F0 F7           BEQ     $9A85               ; {}
9A8E: A8              TAY                         
9A8F: A9 20           LDA     #$20                
9A91: 8D 80 03        STA     $0380               
9A94: 88              DEY                         
9A95: B9 A2 9B        LDA     $9BA2,Y             ; {}
9A98: 8D 73 01        STA     $0173               
9A9B: 20 C1 9A        JSR     $9AC1               ; {}
9A9E: 20 E4 9A        JSR     $9AE4               ; {}
9AA1: 20 64 9B        JSR     $9B64               ; {}
9AA4: BD 15 07        LDA     $0715,X             
9AA7: CD 73 01        CMP     $0173               
9AAA: B0 07           BCS     $9AB3               ; {}
9AAC: BD 0E 07        LDA     $070E,X             
9AAF: 49 FF           EOR     #$FF                
9AB1: D0 D2           BNE     $9A85               ; {}
9AB3: CE 74 01        DEC     $0174               
9AB6: F0 03           BEQ     $9ABB               ; {}
9AB8: 4C 76 9A        JMP     $9A76               ; {}
9ABB: 20 69 9A        JSR     $9A69               ; {}
9ABE: 4C 64 9B        JMP     $9B64               ; {}
9AC1: 18              CLC                         
9AC2: BD 12 07        LDA     $0712,X             
9AC5: 69 DB           ADC     #$DB                
9AC7: 9D 12 07        STA     $0712,X             
9ACA: BD 15 07        LDA     $0715,X             
9ACD: 69 03           ADC     #$03                
9ACF: 9D 15 07        STA     $0715,X             
9AD2: 18              CLC                         
9AD3: BD 16 07        LDA     $0716,X             
9AD6: 69 BC           ADC     #$BC                
9AD8: 9D 16 07        STA     $0716,X             
9ADB: BD 19 07        LDA     $0719,X             
9ADE: 69 02           ADC     #$02                
9AE0: 9D 19 07        STA     $0719,X             
9AE3: 60              RTS                         
9AE4: A9 07           LDA     #$07                
9AE6: 85 00           STA     $00                 ; {ram.GP_00}
9AE8: 20 F0 9A        JSR     $9AF0               ; {}
9AEB: C6 00           DEC     $00                 ; {ram.GP_00}
9AED: 10 F9           BPL     $9AE8               ; {}
9AEF: 60              RTS                         
9AF0: A5 00           LDA     $00                 ; {ram.GP_00}
9AF2: 0A              ASL     A                   
9AF3: 0A              ASL     A                   
9AF4: 85 01           STA     $01                 
9AF6: A8              TAY                         
9AF7: A9 0C           LDA     #$0C                
9AF9: 20 63 9A        JSR     $9A63               ; {}
9AFC: B1 08           LDA     ($08),Y             
9AFE: C9 F8           CMP     #$F8                
9B00: B0 2A           BCS     $9B2C               ; {}
9B02: A5 01           LDA     $01                 
9B04: 85 02           STA     $02                 
9B06: BD 00 07        LDA     $0700,X             
9B09: 85 03           STA     $03                 
9B0B: A5 00           LDA     $00                 ; {ram.GP_00}
9B0D: 20 38 9B        JSR     $9B38               ; {}
9B10: 18              CLC                         
9B11: A5 01           LDA     $01                 
9B13: 69 03           ADC     #$03                
9B15: 85 02           STA     $02                 
9B17: BD 03 07        LDA     $0703,X             
9B1A: 85 03           STA     $03                 
9B1C: 18              CLC                         
9B1D: A5 00           LDA     $00                 ; {ram.GP_00}
9B1F: 69 02           ADC     #$02                
9B21: 29 07           AND     #$07                
9B23: 4C 38 9B        JMP     $9B38               ; {}
9B26: A4 01           LDY     $01                 
9B28: A9 F8           LDA     #$F8                
9B2A: 91 08           STA     ($08),Y             
9B2C: A4 00           LDY     $00                 ; {ram.GP_00}
9B2E: BD 0E 07        LDA     $070E,X             
9B31: 19 9A 9B        ORA     $9B9A,Y             ; {}
9B34: 9D 0E 07        STA     $070E,X             
9B37: 60              RTS                         
9B38: A8              TAY                         
9B39: B9 91 9B        LDA     $9B91,Y             ; {}
9B3C: 08              PHP                         
9B3D: B9 89 9B        LDA     $9B89,Y             ; {}
9B40: 20 63 9A        JSR     $9A63               ; {}
9B43: A0 00           LDY     #$00                
9B45: B1 08           LDA     ($08),Y             
9B47: 85 04           STA     $04                 
9B49: A9 0C           LDA     #$0C                
9B4B: 20 63 9A        JSR     $9A63               ; {}
9B4E: A5 03           LDA     $03                 
9B50: 28              PLP                         
9B51: D0 07           BNE     $9B5A               ; {}
9B53: 18              CLC                         
9B54: 65 04           ADC     $04                 
9B56: B0 CE           BCS     $9B26               ; {}
9B58: 90 05           BCC     $9B5F               ; {}
9B5A: 38              SEC                         
9B5B: E5 04           SBC     $04                 
9B5D: 90 C7           BCC     $9B26               ; {}
9B5F: A4 02           LDY     $02                 
9B61: 91 08           STA     ($08),Y             
9B63: 60              RTS                         
9B64: A9 08           LDA     #$08                
9B66: 85 00           STA     $00                 ; {ram.GP_00}
9B68: 86 08           STX     $08                 
9B6A: 86 0A           STX     $0A                 
9B6C: A0 0C           LDY     #$0C                
9B6E: B1 08           LDA     ($08),Y             
9B70: 91 0A           STA     ($0A),Y             
9B72: C8              INY                         
9B73: AD 75 01        LDA     $0175               
9B76: 91 0A           STA     ($0A),Y             
9B78: C8              INY                         
9B79: AD 76 01        LDA     $0176               
9B7C: 91 0A           STA     ($0A),Y             
9B7E: C8              INY                         
9B7F: B1 08           LDA     ($08),Y             
9B81: 91 0A           STA     ($0A),Y             
9B83: C8              INY                         
9B84: C6 00           DEC     $00                 ; {ram.GP_00}
9B86: D0 E6           BNE     $9B6E               ; {}
9B88: 60              RTS                         
9B89: 15 19           ORA     $19,X               
9B8B: 0D 19 15        ORA     $1519               
9B8E: 19 0D 19        ORA     $190D,Y             
9B91: 01 01           ORA     ($01,X)             
9B93: 00              BRK                         
9B94: 00              BRK                         
9B95: 00              BRK                         
9B96: 00              BRK                         
9B97: 00              BRK                         
9B98: 01 80           ORA     ($80,X)             
9B9A: 01 02           ORA     ($02,X)             
9B9C: 04 ; ????
9B9D: 08              PHP                         
9B9E: 10 20           BPL     $9BC0               ; {}
9BA0: 40              RTI                         
9BA1: 80 ; ????
9BA2: FF ; ????
9BA3: 40              RTI                         
9BA4: 40              RTI                         
9BA5: 20 20 00        JSR     $0020               
9BA8: 60              RTS                         
9BA9: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9BAB: A8              TAY                         
9BAC: BD 00 07        LDA     $0700,X             
9BAF: 85 01           STA     $01                 
9BB1: BD 03 07        LDA     $0703,X             
9BB4: 85 02           STA     $02                 
9BB6: 8A              TXA                         
9BB7: 48              PHA                         
9BB8: B1 08           LDA     ($08),Y             
9BBA: C9 7F           CMP     #$7F                
9BBC: D0 04           BNE     $9BC2               ; {}
9BBE: A9 F8           LDA     #$F8                
9BC0: D0 03           BNE     $9BC5               ; {}
9BC2: 18              CLC                         
9BC3: 65 01           ADC     $01                 
9BC5: 20 DD 9B        JSR     $9BDD               ; {}
9BC8: 20 DD 9B        JSR     $9BDD               ; {}
9BCB: 20 DD 9B        JSR     $9BDD               ; {}
9BCE: 18              CLC                         
9BCF: 65 02           ADC     $02                 
9BD1: 9D 00 02        STA     $0200,X             
9BD4: E8              INX                         
9BD5: C8              INY                         
9BD6: C6 00           DEC     $00                 ; {ram.GP_00}
9BD8: 10 DE           BPL     $9BB8               ; {}
9BDA: 68              PLA                         
9BDB: AA              TAX                         
9BDC: 60              RTS                         
9BDD: 9D 00 02        STA     $0200,X             
9BE0: C8              INY                         
9BE1: E8              INX                         
9BE2: B1 08           LDA     ($08),Y             
9BE4: 60              RTS                         
9BE5: 01 60           ORA     ($60,X)             
9BE7: 05 01           ORA     $01                 
9BE9: 64 ; ????
9BEA: 05 01           ORA     $01                 
9BEC: 68              PLA                         
9BED: 05 01           ORA     $01                 
9BEF: 6C 05 01        JMP     ($0105)             
9BF2: 70 0B           BVS     $9BFF               ; {}
9BF4: 00              BRK                         
9BF5: 7F ; ????
9BF6: 0B ; ????
9BF7: 00              BRK                         
9BF8: A0 0A           LDY     #$0A                
9BFA: 01 A4           ORA     ($A4,X)             
9BFC: 05 01           ORA     $01                 
9BFE: A8              TAY                         
9BFF: 05 01           ORA     $01                 
9C01: AC 0A 01        LDY     $010A               
9C04: FD FF 01        SBC     $01FF,X             
9C07: 00              BRK                         
9C08: 0A              ASL     A                   
9C09: 01 04           ORA     ($04,X)             
9C0B: 05 01           ORA     $01                 
9C0D: 08              PHP                         
9C0E: 05 01           ORA     $01                 
9C10: 0C ; ????
9C11: 0A              ASL     A                   
9C12: 01 15           ORA     ($15,X)             
9C14: 0B ; ????
9C15: 00              BRK                         
9C16: 1A ; ????
9C17: 0B ; ????
9C18: 00              BRK                         
9C19: 40              RTI                         
9C1A: 04 ; ????
9C1B: 01 43           ORA     ($43,X)             
9C1D: 09 00           ORA     #$00                
9C1F: 4C 09 00        JMP     $0009               
9C22: 4F ; ????
9C23: 04 ; ????
9C24: 01 55           ORA     ($55,X)             
9C26: 05 01           ORA     $01                 
9C28: 57 ; ????
9C29: 05 01           ORA     $01                 
9C2B: 60              RTS                         
9C2C: 00              BRK                         
9C2D: 00              BRK                         
9C2E: 7F ; ????
9C2F: 04 ; ????
9C30: 01 80           ORA     ($80,X)             
9C32: 0A              ASL     A                   
9C33: 01 81           ORA     ($81,X)             
9C35: 05 01           ORA     $01                 
9C37: 8B ; ????
9C38: 05 01           ORA     $01                 
9C3A: B4 01           LDY     $01,X               
9C3C: 00              BRK                         
9C3D: B8              CLV                         
9C3E: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9C40: FD FF 01        SBC     $01FF,X             
9C43: 00              BRK                         
9C44: 05 01           ORA     $01                 
9C46: 04 ; ????
9C47: 05 01           ORA     $01                 
9C49: 08              PHP                         
9C4A: 05 01           ORA     $01                 
9C4C: 0C ; ????
9C4D: 05 01           ORA     $01                 
9C4F: 10 09           BPL     $9C5A               ; {}
9C51: 00              BRK                         
9C52: 1F ; ????
9C53: 09 00           ORA     #$00                
9C55: 20 04 01        JSR     $0104               
9C58: 2F ; ????
9C59: 04 ; ????
9C5A: 01 70           ORA     ($70,X)             
9C5C: 04 ; ????
9C5D: 01 7F           ORA     ($7F,X)             
9C5F: 04 ; ????
9C60: 01 81           ORA     ($81,X)             
9C62: 07 ; ????
9C63: 01 8D           ORA     ($8D,X)             
9C65: 07 ; ????
9C66: 01 B1           ORA     ($B1,X)             
9C68: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9C6A: B8              CLV                         
9C6B: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9C6D: FD FF 01        SBC     $01FF,X             
9C70: 00              BRK                         
9C71: 05 01           ORA     $01                 
9C73: 04 ; ????
9C74: 05 01           ORA     $01                 
9C76: 08              PHP                         
9C77: 05 01           ORA     $01                 
9C79: 0C ; ????
9C7A: 05 01           ORA     $01                 
9C7C: 15 10           ORA     $10,X               
9C7E: 03 ; ????
9C7F: 1A ; ????
9C80: 10 03           BPL     $9C85               ; {}
9C82: 20 04 01        JSR     $0104               
9C85: 2F ; ????
9C86: 04 ; ????
9C87: 01 46           ORA     ($46,X)             
9C89: 06 01           ASL     $01                 
9C8B: 65 07           ADC     $07                 
9C8D: 01 70           ORA     ($70,X)             
9C8F: 04 ; ????
9C90: 01 79           ORA     ($79,X)             
9C92: 07 ; ????
9C93: 01 7F           ORA     ($7F,X)             
9C95: 04 ; ????
9C96: 01 80           ORA     ($80,X)             
9C98: 0A              ASL     A                   
9C99: 01 8D           ORA     ($8D,X)             
9C9B: 07 ; ????
9C9C: 01 B4           ORA     ($B4,X)             
9C9E: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9CA0: B8              CLV                         
9CA1: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9CA3: FD FF 01        SBC     $01FF,X             
9CA6: 00              BRK                         
9CA7: 04 ; ????
9CA8: 01 01           ORA     ($01,X)             
9CAA: 05 01           ORA     $01                 
9CAC: 05 05           ORA     $05                 
9CAE: 01 09           ORA     ($09,X)             
9CB0: 05 01           ORA     $01                 
9CB2: 0D 05 01        ORA     $0105               
9CB5: 0F ; ????
9CB6: 04 ; ????
9CB7: 01 11           ORA     ($11,X)             
9CB9: 10 03           BPL     $9CBE               ; {}
9CBB: 12 ; ????
9CBC: 09 00           ORA     #$00                
9CBE: 13 ; ????
9CBF: 10 03           BPL     $9CC4               ; {}
9CC1: 1E 09 00        ASL     $0009,X             
9CC4: 20 04 01        JSR     $0104               
9CC7: 2F ; ????
9CC8: 04 ; ????
9CC9: 01 32           ORA     ($32,X)             
9CCB: 09 00           ORA     #$00                
9CCD: 53 ; ????
9CCE: 06 01           ASL     $01                 
9CD0: 57 ; ????
9CD1: 06 01           ASL     $01                 
9CD3: 5B ; ????
9CD4: 06 01           ASL     $01                 
9CD6: 70 04           BVS     $9CDC               ; {}
9CD8: 01 72           ORA     ($72,X)             
9CDA: 06 01           ASL     $01                 
9CDC: 76 06           ROR     $06,X               
9CDE: 01 7A           ORA     ($7A,X)             
9CE0: 06 01           ASL     $01                 
9CE2: 7F ; ????
9CE3: 04 ; ????
9CE4: 01 93           ORA     ($93,X)             
9CE6: 06 01           ASL     $01                 
9CE8: 97 ; ????
9CE9: 06 01           ASL     $01                 
9CEB: 9B ; ????
9CEC: 06 01           ASL     $01                 
9CEE: B1 05           LDA     ($05),Y             
9CF0: 01 B5           ORA     ($B5,X)             
9CF2: 05 01           ORA     $01                 
9CF4: B9 05 01        LDA     $0105,Y             
9CF7: BD 05 01        LDA     $0105,X             
9CFA: FD FF 01        SBC     $01FF,X             
9CFD: 00              BRK                         
9CFE: 05 01           ORA     $01                 
9D00: 04 ; ????
9D01: 0A              ASL     A                   
9D02: 01 08           ORA     ($08,X)             
9D04: 0A              ASL     A                   
9D05: 01 0C           ORA     ($0C,X)             
9D07: 05 01           ORA     $01                 
9D09: 20 04 01        JSR     $0104               
9D0C: 2F ; ????
9D0D: 04 ; ????
9D0E: 01 32           ORA     ($32,X)             
9D10: 07 ; ????
9D11: 01 35           ORA     ($35,X)             
9D13: 10 03           BPL     $9D18               ; {}
9D15: 3B ; ????
9D16: 10 03           BPL     $9D1B               ; {}
9D18: 3C ; ????
9D19: 07 ; ????
9D1A: 01 51           ORA     ($51,X)             
9D1C: 07 ; ????
9D1D: 01 5D           ORA     ($5D,X)             
9D1F: 0E 03 70        ASL     $7003               
9D22: 04 ; ????
9D23: 01 75           ORA     ($75,X)             
9D25: 0C ; ????
9D26: 00              BRK                         
9D27: 7F ; ????
9D28: 04 ; ????
9D29: 01 81           ORA     ($81,X)             
9D2B: 0F ; ????
9D2C: 03 ; ????
9D2D: 85 0D           STA     $0D                 
9D2F: 01 89           ORA     ($89,X)             
9D31: 0D 01 8A        ORA     $8A01               ; {}
9D34: 0C ; ????
9D35: 00              BRK                         
9D36: 8B ; ????
9D37: 0F ; ????
9D38: 03 ; ????
9D39: 99 0D 01        STA     $010D,Y             
9D3C: B1 05           LDA     ($05),Y             
9D3E: 01 B5           ORA     ($B5,X)             
9D40: 05 01           ORA     $01                 
9D42: B9 05 01        LDA     $0105,Y             
9D45: BD 05 01        LDA     $0105,X             
9D48: FD FF 01        SBC     $01FF,X             
9D4B: 00              BRK                         
9D4C: 0A              ASL     A                   
9D4D: 01 04           ORA     ($04,X)             
9D4F: 05 01           ORA     $01                 
9D51: 08              PHP                         
9D52: 05 01           ORA     $01                 
9D54: 0C ; ????
9D55: 0A              ASL     A                   
9D56: 01 16           ORA     ($16,X)             
9D58: 10 03           BPL     $9D5D               ; {}
9D5A: 19 10 03        ORA     $0310,Y             
9D5D: 20 04 01        JSR     $0104               
9D60: 2F ; ????
9D61: 04 ; ????
9D62: 01 43           ORA     ($43,X)             
9D64: 0C ; ????
9D65: 00              BRK                         
9D66: 65 07           ADC     $07                 
9D68: 01 70           ORA     ($70,X)             
9D6A: 04 ; ????
9D6B: 01 73           ORA     ($73,X)             
9D6D: 07 ; ????
9D6E: 01 7F           ORA     ($7F,X)             
9D70: 04 ; ????
9D71: 01 81           ORA     ($81,X)             
9D73: 07 ; ????
9D74: 01 8D           ORA     ($8D,X)             
9D76: 07 ; ????
9D77: 01 AB           ORA     ($AB,X)             
9D79: 0C ; ????
9D7A: 00              BRK                         
9D7B: B1 05           LDA     ($05),Y             
9D7D: 01 B5           ORA     ($B5,X)             
9D7F: 05 01           ORA     $01                 
9D81: B9 05 01        LDA     $0105,Y             
9D84: BD 05 01        LDA     $0105,X             
9D87: FD FF 01        SBC     $01FF,X             
9D8A: 00              BRK                         
9D8B: 04 ; ????
9D8C: 01 01           ORA     ($01,X)             
9D8E: 05 01           ORA     $01                 
9D90: 05 05           ORA     $05                 
9D92: 01 09           ORA     ($09,X)             
9D94: 05 01           ORA     $01                 
9D96: 0D 05 01        ORA     $0105               
9D99: 10 05           BPL     $9DA0               ; {}
9D9B: 01 15           ORA     ($15,X)             
9D9D: 10 03           BPL     $9DA2               ; {}
9D9F: 1A ; ????
9DA0: 10 03           BPL     $9DA5               ; {}
9DA2: 1C ; ????
9DA3: 05 01           ORA     $01                 
9DA5: 20 04 01        JSR     $0104               
9DA8: 2F ; ????
9DA9: 04 ; ????
9DAA: 01 57           ORA     ($57,X)             
9DAC: 06 01           ASL     $01                 
9DAE: 5B ; ????
9DAF: 07 ; ????
9DB0: 01 63           ORA     ($63,X)             
9DB2: 06 01           ASL     $01                 
9DB4: 70 04           BVS     $9DBA               ; {}
9DB6: 01 76           ORA     ($76,X)             
9DB8: 04 ; ????
9DB9: 01 7A           ORA     ($7A,X)             
9DBB: 0D 02 7F        ORA     $7F02               
9DBE: 04 ; ????
9DBF: 01 81           ORA     ($81,X)             
9DC1: 07 ; ????
9DC2: 01 8E           ORA     ($8E,X)             
9DC4: 0A              ASL     A                   
9DC5: 01 99           ORA     ($99,X)             
9DC7: 0D 02 B1        ORA     $B102               ; {}
9DCA: 05 01           ORA     $01                 
9DCC: B5 05           LDA     $05,X               
9DCE: 01 B9           ORA     ($B9,X)             
9DD0: 05 01           ORA     $01                 
9DD2: BD 05 01        LDA     $0105,X             
9DD5: FD FF 01        SBC     $01FF,X             
9DD8: 00              BRK                         
9DD9: 05 01           ORA     $01                 
9DDB: 04 ; ????
9DDC: 05 01           ORA     $01                 
9DDE: 08              PHP                         
9DDF: 05 01           ORA     $01                 
9DE1: 0C ; ????
9DE2: 05 01           ORA     $01                 
9DE4: 10 02           BPL     $9DE8               ; {}
9DE6: 01 11           ORA     ($11,X)             
9DE8: 08              PHP                         
9DE9: 01 1F           ORA     ($1F,X)             
9DEB: 02 ; ????
9DEC: 01 50           ORA     ($50,X)             
9DEE: 02 ; ????
9DEF: 01 5E           ORA     ($5E,X)             
9DF1: 07 ; ????
9DF2: 01 5F           ORA     ($5F,X)             
9DF4: 02 ; ????
9DF5: 01 60           ORA     ($60,X)             
9DF7: 00              BRK                         
9DF8: 00              BRK                         
9DF9: 69 07           ADC     #$07                
9DFB: 01 74           ORA     ($74,X)             
9DFD: 07 ; ????
9DFE: 01 80           ORA     ($80,X)             
9E00: 0A              ASL     A                   
9E01: 01 82           ORA     ($82,X)             
9E03: 12 ; ????
9E04: 03 ; ????
9E05: 84 0A           STY     $0A                 
9E07: 01 85           ORA     ($85,X)             
9E09: 12 ; ????
9E0A: 03 ; ????
9E0B: 88              DEY                         
9E0C: 0A              ASL     A                   
9E0D: 01 89           ORA     ($89,X)             
9E0F: 12 ; ????
9E10: 03 ; ????
9E11: 8C 0A 01        STY     $010A               
9E14: 8D 12 03        STA     $0312               
9E17: FD FF 01        SBC     $01FF,X             
9E1A: 00              BRK                         
9E1B: 0A              ASL     A                   
9E1C: 01 03           ORA     ($03,X)             
9E1E: 0A              ASL     A                   
9E1F: 01 07           ORA     ($07,X)             
9E21: 05 01           ORA     $01                 
9E23: 09 0A           ORA     #$0A                
9E25: 01 0C           ORA     ($0C,X)             
9E27: 0A              ASL     A                   
9E28: 01 33           ORA     ($33,X)             
9E2A: 10 03           BPL     $9E2F               ; {}
9E2C: 37 ; ????
9E2D: 0E 03 3C        ASL     $3C03               
9E30: 10 03           BPL     $9E35               ; {}
9E32: 40              RTI                         
9E33: 04 ; ????
9E34: 01 46           ORA     ($46,X)             
9E36: 09 00           ORA     #$00                
9E38: 49 09           EOR     #$09                
9E3A: 00              BRK                         
9E3B: 4F ; ????
9E3C: 04 ; ????
9E3D: 01 57           ORA     ($57,X)             
9E3F: 0E 03 80        ASL     $8003               ; {}
9E42: 0A              ASL     A                   
9E43: 01 83           ORA     ($83,X)             
9E45: 0A              ASL     A                   
9E46: 01 87           ORA     ($87,X)             
9E48: 0E 03 89        ASL     $8903               ; {}
9E4B: 0A              ASL     A                   
9E4C: 01 8D           ORA     ($8D,X)             
9E4E: 0A              ASL     A                   
9E4F: 01 B7           ORA     ($B7,X)             
9E51: 05 01           ORA     $01                 
9E53: FD FF 01        SBC     $01FF,X             
9E56: 00              BRK                         
9E57: 05 01           ORA     $01                 
9E59: 04 ; ????
9E5A: 05 01           ORA     $01                 
9E5C: 08              PHP                         
9E5D: 05 01           ORA     $01                 
9E5F: 0C ; ????
9E60: 05 01           ORA     $01                 
9E62: 13 ; ????
9E63: 09 00           ORA     #$00                
9E65: 1B ; ????
9E66: 09 00           ORA     #$00                
9E68: 1C ; ????
9E69: 10 03           BPL     $9E6E               ; {}
9E6B: 20 04 01        JSR     $0104               
9E6E: 2F ; ????
9E6F: 04 ; ????
9E70: 01 4B           ORA     ($4B,X)             
9E72: 09 00           ORA     #$00                
9E74: 51 06           EOR     ($06),Y             
9E76: 01 55           ORA     ($55,X)             
9E78: 05 01           ORA     $01                 
9E7A: 59 17 00        EOR     $0017,Y             
9E7D: 66 10           ROR     $10                 
9E7F: 03 ; ????
9E80: 70 04           BVS     $9E86               ; {}
9E82: 01 7F           ORA     ($7F,X)             
9E84: 04 ; ????
9E85: 01 81           ORA     ($81,X)             
9E87: 07 ; ????
9E88: 01 89           ORA     ($89,X)             
9E8A: 06 01           ASL     $01                 
9E8C: 8D 07 01        STA     $0107               
9E8F: B1 01           LDA     ($01),Y             
9E91: 00              BRK                         
9E92: B8              CLV                         
9E93: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9E95: FD FF 01        SBC     $01FF,X             
9E98: 00              BRK                         
9E99: 05 01           ORA     $01                 
9E9B: 04 ; ????
9E9C: 05 01           ORA     $01                 
9E9E: 08              PHP                         
9E9F: 05 01           ORA     $01                 
9EA1: 0C ; ????
9EA2: 05 01           ORA     $01                 
9EA4: 10 05           BPL     $9EAB               ; {}
9EA6: 01 1A           ORA     ($1A,X)             
9EA8: 10 03           BPL     $9EAD               ; {}
9EAA: 1C ; ????
9EAB: 05 01           ORA     $01                 
9EAD: 20 09 00        JSR     $0009               
9EB0: 2F ; ????
9EB1: 09 00           ORA     #$00                
9EB3: 30 04           BMI     $9EB9               ; {}
9EB5: 01 3F           ORA     ($3F,X)             
9EB7: 04 ; ????
9EB8: 01 46           ORA     ($46,X)             
9EBA: 06 01           ASL     $01                 
9EBC: 4C 0B 00        JMP     $000B               
9EBF: 54 ; ????
9EC0: 0E 03 70        ASL     $7003               
9EC3: 04 ; ????
9EC4: 01 71           ORA     ($71,X)             
9EC6: 0B ; ????
9EC7: 00              BRK                         
9EC8: 7F ; ????
9EC9: 04 ; ????
9ECA: 01 82           ORA     ($82,X)             
9ECC: 0B ; ????
9ECD: 00              BRK                         
9ECE: 84 0E           STY     $0E                 
9ED0: 03 ; ????
9ED1: 8B ; ????
9ED2: 06 01           ASL     $01                 
9ED4: B1 01           LDA     ($01),Y             
9ED6: 00              BRK                         
9ED7: B8              CLV                         
9ED8: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9EDA: FD FF 01        SBC     $01FF,X             
9EDD: 00              BRK                         
9EDE: 05 01           ORA     $01                 
9EE0: 04 ; ????
9EE1: 05 01           ORA     $01                 
9EE3: 08              PHP                         
9EE4: 05 01           ORA     $01                 
9EE6: 0C ; ????
9EE7: 05 01           ORA     $01                 
9EE9: 10 09           BPL     $9EF4               ; {}
9EEB: 00              BRK                         
9EEC: 12 ; ????
9EED: 0B ; ????
9EEE: 00              BRK                         
9EEF: 19 0B 00        ORA     $000B,Y             
9EF2: 1E 0B 00        ASL     $000B,X             
9EF5: 1F ; ????
9EF6: 09 00           ORA     #$00                
9EF8: 20 04 01        JSR     $0104               
9EFB: 2F ; ????
9EFC: 04 ; ????
9EFD: 01 42           ORA     ($42,X)             
9EFF: 09 00           ORA     #$00                
9F01: 46 07           LSR     $07                 
9F03: 01 59           ORA     ($59,X)             
9F05: 09 00           ORA     #$00                
9F07: 5E 09 00        LSR     $0009,X             
9F0A: 60              RTS                         
9F0B: 00              BRK                         
9F0C: 00              BRK                         
9F0D: 64 ; ????
9F0E: 07 ; ????
9F0F: 01 7E           ORA     ($7E,X)             
9F11: 09 00           ORA     #$00                
9F13: 7F ; ????
9F14: 04 ; ????
9F15: 01 80           ORA     ($80,X)             
9F17: 0D 01 81        ORA     $8101               ; {}
9F1A: 07 ; ????
9F1B: 01 86           ORA     ($86,X)             
9F1D: 07 ; ????
9F1E: 01 89           ORA     ($89,X)             
9F20: 09 00           ORA     #$00                
9F22: A0 0D           LDY     #$0D                
9F24: 01 B0           ORA     ($B0,X)             
9F26: 05 01           ORA     $01                 
9F28: B4 05           LDY     $05,X               
9F2A: 01 B8           ORA     ($B8,X)             
9F2C: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9F2E: FD FF 01        SBC     $01FF,X             
9F31: 00              BRK                         
9F32: 0A              ASL     A                   
9F33: 01 03           ORA     ($03,X)             
9F35: 0A              ASL     A                   
9F36: 01 07           ORA     ($07,X)             
9F38: 05 01           ORA     $01                 
9F3A: 09 0A           ORA     #$0A                
9F3C: 01 0C           ORA     ($0C,X)             
9F3E: 0A              ASL     A                   
9F3F: 01 20           ORA     ($20,X)             
9F41: 0A              ASL     A                   
9F42: 01 2C           ORA     ($2C,X)             
9F44: 0A              ASL     A                   
9F45: 01 60           ORA     ($60,X)             
9F47: 04 ; ????
9F48: 01 65           ORA     ($65,X)             
9F4A: 07 ; ????
9F4B: 01 69           ORA     ($69,X)             
9F4D: 07 ; ????
9F4E: 01 6F           ORA     ($6F,X)             
9F50: 04 ; ????
9F51: 01 80           ORA     ($80,X)             
9F53: 0A              ASL     A                   
9F54: 01 84           ORA     ($84,X)             
9F56: 0A              ASL     A                   
9F57: 01 88           ORA     ($88,X)             
9F59: 0A              ASL     A                   
9F5A: 01 8C           ORA     ($8C,X)             
9F5C: 0A              ASL     A                   
9F5D: 01 FD           ORA     ($FD,X)             
9F5F: FF ; ????
9F60: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9F62: 0A              ASL     A                   
9F63: 01 04           ORA     ($04,X)             
9F65: 05 01           ORA     $01                 
9F67: 08              PHP                         
9F68: 05 01           ORA     $01                 
9F6A: 0C ; ????
9F6B: 0A              ASL     A                   
9F6C: 01 40           ORA     ($40,X)             
9F6E: 04 ; ????
9F6F: 01 43           ORA     ($43,X)             
9F71: 0C ; ????
9F72: 00              BRK                         
9F73: 4C 0C 00        JMP     $000C               
9F76: 4F ; ????
9F77: 04 ; ????
9F78: 01 76           ORA     ($76,X)             
9F7A: 0C ; ????
9F7B: 00              BRK                         
9F7C: 80 ; ????
9F7D: 0A              ASL     A                   
9F7E: 01 86           ORA     ($86,X)             
9F80: 17 ; ????
9F81: 00              BRK                         
9F82: 89 ; ????
9F83: 0A              ASL     A                   
9F84: 01 8A           ORA     ($8A,X)             
9F86: 12 ; ????
9F87: 03 ; ????
9F88: 8C 0A 01        STY     $010A               
9F8B: 8D 0C 00        STA     $000C               
9F8E: A2 12           LDX     #$12                
9F90: 03 ; ????
9F91: B4 05           LDY     $05,X               
9F93: 01 B8           ORA     ($B8,X)             
9F95: 05 01           ORA     $01                 
9F97: FD FF 01        SBC     $01FF,X             
9F9A: 00              BRK                         
9F9B: 05 01           ORA     $01                 
9F9D: 04 ; ????
9F9E: 05 01           ORA     $01                 
9FA0: 08              PHP                         
9FA1: 05 01           ORA     $01                 
9FA3: 0C ; ????
9FA4: 05 01           ORA     $01                 
9FA6: 20 04 01        JSR     $0104               
9FA9: 2F ; ????
9FAA: 04 ; ????
9FAB: 01 43           ORA     ($43,X)             
9FAD: 09 00           ORA     #$00                
9FAF: 47 ; ????
9FB0: 07 ; ????
9FB1: 01 55           ORA     ($55,X)             
9FB3: 07 ; ????
9FB4: 01 70           ORA     ($70,X)             
9FB6: 04 ; ????
9FB7: 01 7F           ORA     ($7F,X)             
9FB9: 04 ; ????
9FBA: 01 81           ORA     ($81,X)             
9FBC: 06 01           ASL     $01                 
9FBE: 8D 07 01        STA     $0107               
9FC1: 96 07           STX     $07,Y               
9FC3: 01 9A           ORA     ($9A,X)             
9FC5: 07 ; ????
9FC6: 01 A1           ORA     ($A1,X)             
9FC8: 12 ; ????
9FC9: 03 ; ????
9FCA: A5 12           LDA     $12                 
9FCC: 03 ; ????
9FCD: A9 12           LDA     #$12                
9FCF: 03 ; ????
9FD0: AB ; ????
9FD1: 12 ; ????
9FD2: 03 ; ????
9FD3: B1 05           LDA     ($05),Y             
9FD5: 01 B5           ORA     ($B5,X)             
9FD7: 05 01           ORA     $01                 
9FD9: B9 05 01        LDA     $0105,Y             
9FDC: BD 05 01        LDA     $0105,X             
9FDF: FD FF 00        SBC     $00FF,X             
9FE2: 00              BRK                         
9FE3: 14 ; ????
9FE4: 00              BRK                         
9FE5: 01 15           ORA     ($15,X)             
9FE7: 00              BRK                         
9FE8: 05 15           ORA     $15                 
9FEA: 00              BRK                         
9FEB: 09 15           ORA     #$15                
9FED: 00              BRK                         
9FEE: 0D 15 00        ORA     $0015               
9FF1: 11 16           ORA     ($16),Y             
9FF3: 00              BRK                         
9FF4: 1E 16 00        ASL     $0016,X             
9FF7: 1F ; ????
9FF8: 14 ; ????
9FF9: 00              BRK                         
9FFA: 40              RTI                         
9FFB: 14 ; ????
9FFC: 00              BRK                         
9FFD: 5F ; ????
9FFE: 14 ; ????
9FFF: 00              BRK                         
A000: 7F ; ????
A001: 14 ; ????
A002: 00              BRK                         
A003: 80 ; ????
A004: 14 ; ????
A005: 00              BRK                         
A006: 8D 15 00        STA     $0015               
A009: B1 15           LDA     ($15),Y             
A00B: 00              BRK                         
A00C: B5 15           LDA     $15,X               
A00E: 00              BRK                         
A00F: B9 15 00        LDA     $0015,Y             
A012: BD 15 00        LDA     $0015,X             
A015: FD FF 02        SBC     $02FF,X             
A018: 00              BRK                         
A019: 18              CLC                         
A01A: 02 ; ????
A01B: 04 ; ????
A01C: 18              CLC                         
A01D: 02 ; ????
A01E: 08              PHP                         
A01F: 18              CLC                         
A020: 02 ; ????
A021: 0C ; ????
A022: 18              CLC                         
A023: 02 ; ????
A024: 10 09           BPL     $A02F               ; {}
A026: 01 1F           ORA     ($1F,X)             
A028: 09 01           ORA     #$01                
A02A: 20 17 02        JSR     $0217               
A02D: 2F ; ????
A02E: 17 ; ????
A02F: 02 ; ????
A030: 60              RTS                         
A031: 17 ; ????
A032: 02 ; ????
A033: 6F ; ????
A034: 17 ; ????
A035: 02 ; ????
A036: 80 ; ????
A037: 17 ; ????
A038: 02 ; ????
A039: 81 17           STA     ($17,X)             
A03B: 02 ; ????
A03C: 8E 17 02        STX     $0217               
A03F: 8F ; ????
A040: 17 ; ????
A041: 02 ; ????
A042: B2 ; ????
A043: 18              CLC                         
A044: 02 ; ????
A045: B6 18           LDX     $18,Y               
A047: 02 ; ????
A048: BA              TSX                         
A049: 18              CLC                         
A04A: 02 ; ????
A04B: FD FF 01        SBC     $01FF,X             
A04E: 00              BRK                         
A04F: 19 01 04        ORA     $0401,Y             
A052: 19 01 08        ORA     $0801,Y             
A055: 19 01 0C        ORA     $0C01,Y             
A058: 19 01 10        ORA     $1001,Y             
A05B: 08              PHP                         
A05C: 01 1C           ORA     ($1C,X)             
A05E: 08              PHP                         
A05F: 01 20           ORA     ($20,X)             
A061: 04 ; ????
A062: 01 2F           ORA     ($2F,X)             
A064: 04 ; ????
A065: 01 47           ORA     ($47,X)             
A067: 13 ; ????
A068: 02 ; ????
A069: 53 ; ????
A06A: 13 ; ????
A06B: 02 ; ????
A06C: 69 13           ADC     #$13                
A06E: 02 ; ????
A06F: 70 04           BVS     $A075               ; {}
A071: 01 7F           ORA     ($7F,X)             
A073: 04 ; ????
A074: 01 81           ORA     ($81,X)             
A076: 13 ; ????
A077: 02 ; ????
A078: 86 13           STX     $13                 
A07A: 02 ; ????
A07B: 8D 13 02        STA     $0213               
A07E: B0 19           BCS     $A099               ; {}
A080: 01 B4           ORA     ($B4,X)             
A082: 19 01 B8        ORA     $B801,Y             ; {}
A085: 19 01 BC        ORA     $BC01,Y             ; {}
A088: 19 01 FD        ORA     $FD01,Y             
A08B: FF ; ????
A08C: 01 00           ORA     ($00,X)             ; {ram.GP_00}
A08E: 19 01 04        ORA     $0401,Y             
A091: 10 03           BPL     $A096               ; {}
A093: 05 19           ORA     $19                 
A095: 01 09           ORA     ($09,X)             
A097: 19 01 0D        ORA     $0D01,Y             
A09A: 19 01 10        ORA     $1001,Y             
A09D: 09 00           ORA     #$00                
A09F: 19 02 01        ORA     $0102,Y             
A0A2: 1A ; ????
A0A3: 10 03           BPL     $A0A8               ; {}
A0A5: 1B ; ????
A0A6: 08              PHP                         
A0A7: 01 1F           ORA     ($1F,X)             
A0A9: 09 00           ORA     #$00                
A0AB: 20 02 01        JSR     $0102               
A0AE: 2F ; ????
A0AF: 02 ; ????
A0B0: 01 4D           ORA     ($4D,X)             
A0B2: 19 01 59        ORA     $5901,Y             
A0B5: 02 ; ????
A0B6: 01 60           ORA     ($60,X)             
A0B8: 02 ; ????
A0B9: 01 6F           ORA     ($6F,X)             
A0BB: 02 ; ????
A0BC: 01 7C           ORA     ($7C,X)             
A0BE: 02 ; ????
A0BF: 01 80           ORA     ($80,X)             
A0C1: 02 ; ????
A0C2: 01 81           ORA     ($81,X)             
A0C4: 19 01 85        ORA     $8501,Y             ; {}
A0C7: 19 01 8E        ORA     $8E01,Y             ; {}
A0CA: 13 ; ????
A0CB: 02 ; ????
A0CC: 8F ; ????
A0CD: 02 ; ????
A0CE: 01 B0           ORA     ($B0,X)             
A0D0: 19 01 B4        ORA     $B401,Y             ; {}
A0D3: 19 01 B8        ORA     $B801,Y             ; {}
A0D6: 19 01 BC        ORA     $BC01,Y             ; {}
A0D9: 19 01 FD        ORA     $FD01,Y             
A0DC: FF ; ????
A0DD: 01 00           ORA     ($00,X)             ; {ram.GP_00}
A0DF: 0A              ASL     A                   
A0E0: 01 03           ORA     ($03,X)             
A0E2: 19 01 07        ORA     $0701,Y             
A0E5: 19 01 0B        ORA     $0B01,Y             
A0E8: 0A              ASL     A                   
A0E9: 01 35           ORA     ($35,X)             
A0EB: 0C ; ????
A0EC: 00              BRK                         
A0ED: 42 ; ????
A0EE: 0A              ASL     A                   
A0EF: 01 47           ORA     ($47,X)             
A0F1: 19 01 4A        ORA     $4A01,Y             
A0F4: 0A              ASL     A                   
A0F5: 01 65           ORA     ($65,X)             
A0F7: 0C ; ????
A0F8: 00              BRK                         
A0F9: 74 ; ????
A0FA: 19 01 82        ORA     $8201,Y             ; {}
A0FD: 0A              ASL     A                   
A0FE: 01 86           ORA     ($86,X)             
A100: 0C ; ????
A101: 00              BRK                         
A102: 8A              TXA                         
A103: 0C ; ????
A104: 00              BRK                         
A105: 8B ; ????
A106: 0A              ASL     A                   
A107: 01 99           ORA     ($99,X)             
A109: 19 01 B4        ORA     $B401,Y             ; {}
A10C: 19 01 B8        ORA     $B801,Y             ; {}
A10F: 19 01 FD        ORA     $FD01,Y             
A112: FF ; ????
A113: 01 00           ORA     ($00,X)             ; {ram.GP_00}
A115: 19 01 04        ORA     $0401,Y             
A118: 19 01 08        ORA     $0801,Y             
A11B: 19 01 0C        ORA     $0C01,Y             
A11E: 19 01 10        ORA     $1001,Y             
A121: 02 ; ????
A122: 01 1C           ORA     ($1C,X)             
A124: 19 01 2F        ORA     $2F01,Y             
A127: 02 ; ????
A128: 01 45           ORA     ($45,X)             
A12A: 02 ; ????
A12B: 01 46           ORA     ($46,X)             
A12D: 19 01 50        ORA     $5001,Y             
A130: 02 ; ????
A131: 01 6A           ORA     ($6A,X)             
A133: 13 ; ????
A134: 02 ; ????
A135: 6F ; ????
A136: 02 ; ????
A137: 01 76           ORA     ($76,X)             
A139: 02 ; ????
A13A: 01 80           ORA     ($80,X)             
A13C: 02 ; ????
A13D: 01 81           ORA     ($81,X)             
A13F: 13 ; ????
A140: 02 ; ????
A141: 8D 19 01        STA     $0119               
A144: 8F ; ????
A145: 02 ; ????
A146: 01 B1           ORA     ($B1,X)             
A148: 05 01           ORA     $01                 
A14A: B5 05           LDA     $05,X               
A14C: 01 B9           ORA     ($B9,X)             
A14E: 05 01           ORA     $01                 
A150: BB ; ????
A151: 05 01           ORA     $01                 
A153: FD FF 01        SBC     $01FF,X             
A156: 00              BRK                         
A157: 0A              ASL     A                   
A158: 01 03           ORA     ($03,X)             
A15A: 0A              ASL     A                   
A15B: 01 07           ORA     ($07,X)             
A15D: 05 01           ORA     $01                 
A15F: 09 0A           ORA     #$0A                
A161: 01 0C           ORA     ($0C,X)             
A163: 0A              ASL     A                   
A164: 01 20           ORA     ($20,X)             
A166: 02 ; ????
A167: 01 2F           ORA     ($2F,X)             
A169: 02 ; ????
A16A: 01 37           ORA     ($37,X)             
A16C: 0E 03 43        ASL     $4303               
A16F: 02 ; ????
A170: 01 46           ORA     ($46,X)             
A172: 02 ; ????
A173: 01 49           ORA     ($49,X)             
A175: 02 ; ????
A176: 01 4C           ORA     ($4C,X)             
A178: 02 ; ????
A179: 01 57           ORA     ($57,X)             
A17B: 0E 03 60        ASL     $6003               
A17E: 02 ; ????
A17F: 01 6F           ORA     ($6F,X)             
A181: 02 ; ????
A182: 01 80           ORA     ($80,X)             
A184: 02 ; ????
A185: 01 81           ORA     ($81,X)             
A187: 02 ; ????
A188: 01 83           ORA     ($83,X)             
A18A: 0C ; ????
A18B: 00              BRK                         
A18C: 86 0C           STX     $0C                 
A18E: 00              BRK                         
A18F: 87 ; ????
A190: 0E 03 89        ASL     $8903               ; {}
A193: 0C ; ????
A194: 00              BRK                         
A195: 8C 0C 00        STY     $000C               
A198: 8E 02 01        STX     $0102               
A19B: 8F ; ????
A19C: 02 ; ????
A19D: 01 B1           ORA     ($B1,X)             
A19F: 01 00           ORA     ($00,X)             ; {ram.GP_00}
A1A1: B8              CLV                         
A1A2: 01 00           ORA     ($00,X)             ; {ram.GP_00}
A1A4: FD FF 01        SBC     $01FF,X             
A1A7: 00              BRK                         
A1A8: 0A              ASL     A                   
A1A9: 01 03           ORA     ($03,X)             
A1AB: 19 01 06        ORA     $0601,Y             
A1AE: 04 ; ????
A1AF: 01 07           ORA     ($07,X)             
A1B1: 19 01 09        ORA     $0901,Y             
A1B4: 19 01 1C        ORA     $1C01,Y             
A1B7: 19 01 20        ORA     $2001,Y             ; {hard.P_CNTRL_2}
A1BA: 04 ; ????
A1BB: 01 2F           ORA     ($2F,X)             
A1BD: 0A              ASL     A                   
A1BE: 01 46           ORA     ($46,X)             
A1C0: 19 01 57        ORA     $5701,Y             
A1C3: 02 ; ????
A1C4: 01 58           ORA     ($58,X)             
A1C6: 19 01 6F        ORA     $6F01,Y             
A1C9: 04 ; ????
A1CA: 01 70           ORA     ($70,X)             
A1CC: 04 ; ????
A1CD: 01 81           ORA     ($81,X)             
A1CF: 17 ; ????
A1D0: 02 ; ????
A1D1: 85 19           STA     $19                 
A1D3: 01 86           ORA     ($86,X)             
A1D5: 17 ; ????
A1D6: 02 ; ????
A1D7: 8D 0A 01        STA     $010A               
A1DA: A2 12           LDX     #$12                
A1DC: 03 ; ????
A1DD: B1 05           LDA     ($05),Y             
A1DF: 01 B5           ORA     ($B5,X)             
A1E1: 05 01           ORA     $01                 
A1E3: B9 05 01        LDA     $0105,Y             
A1E6: FD FF 01        SBC     $01FF,X             
A1E9: 00              BRK                         
A1EA: 05 01           ORA     $01                 
A1EC: 04 ; ????
A1ED: 05 01           ORA     $01                 
A1EF: 08              PHP                         
A1F0: 05 01           ORA     $01                 
A1F2: 0C ; ????
A1F3: 05 01           ORA     $01                 
A1F5: 10 09           BPL     $A200               ; {}
A1F7: 00              BRK                         
A1F8: 1F ; ????
A1F9: 09 00           ORA     #$00                
A1FB: 20 04 01        JSR     $0104               
A1FE: 2F ; ????
A1FF: 04 ; ????
A200: 01 47           ORA     ($47,X)             
A202: 07 ; ????
A203: 01 5C           ORA     ($5C,X)             
A205: 05 01           ORA     $01                 
A207: 65 07           ADC     $07                 
A209: 01 66           ORA     ($66,X)             
A20B: 05 01           ORA     $01                 
A20D: 70 04           BVS     $A213               ; {}
A20F: 01 76           ORA     ($76,X)             
A211: 04 ; ????
A212: 01 7F           ORA     ($7F,X)             
A214: 04 ; ????
A215: 01 81           ORA     ($81,X)             
A217: 07 ; ????
A218: 01 8E           ORA     ($8E,X)             
A21A: 05 01           ORA     $01                 
A21C: B1 01           LDA     ($01),Y             
A21E: 00              BRK                         
A21F: B8              CLV                         
A220: 01 00           ORA     ($00,X)             ; {ram.GP_00}
A222: FD FF 02        SBC     $02FF,X             
A225: 00              BRK                         
A226: 15 02           ORA     $02,X               
A228: 04 ; ????
A229: 15 02           ORA     $02,X               
A22B: 08              PHP                         
A22C: 15 02           ORA     $02,X               
A22E: 0C ; ????
A22F: 15 02           ORA     $02,X               
A231: 10 14           BPL     $A247               ; {}
A233: 02 ; ????
A234: 1F ; ????
A235: 14 ; ????
A236: 02 ; ????
A237: 42 ; ????
A238: 09 02           ORA     #$02                
A23A: 4D 09 02        EOR     $0209               
A23D: 50 14           BVC     $A253               ; {}
A23F: 02 ; ????
A240: 5F ; ????
A241: 14 ; ????
A242: 02 ; ????
A243: 81 15           STA     ($15,X)             
A245: 02 ; ????
A246: 8B ; ????
A247: 15 02           ORA     $02,X               
A249: 91 15           STA     ($15),Y             
A24B: 02 ; ????
A24C: 95 11           STA     $11,X               
A24E: 03 ; ????
A24F: 98              TYA                         
A250: 11 03           ORA     ($03),Y             
A252: 9B ; ????
A253: 15 02           ORA     $02,X               
A255: A4 15           LDY     $15                 
A257: 02 ; ????
A258: A8              TAY                         
A259: 15 02           ORA     $02,X               
A25B: FD FF 01        SBC     $01FF,X             
A25E: 55 01           EOR     $01,X               
A260: 5E FF 07        LSR     $07FF,X             
A263: 51 51           EOR     ($51),Y             
A265: 51 51           EOR     ($51),Y             
A267: 51 51           EOR     ($51),Y             
A269: 51 FF           EOR     ($FF),Y             
A26B: 01 5C           ORA     ($5C,X)             
A26D: 01 5C           ORA     ($5C,X)             
A26F: 01 5C           ORA     ($5C,X)             
A271: 01 5C           ORA     ($5C,X)             
A273: FF ; ????
A274: 01 50           ORA     ($50,X)             
A276: 01 2A           ORA     ($2A,X)             
A278: FF ; ????
A279: 01 52           ORA     ($52,X)             
A27B: 01 52           ORA     ($52,X)             
A27D: 01 52           ORA     ($52,X)             
A27F: 01 52           ORA     ($52,X)             
A281: 01 52           ORA     ($52,X)             
A283: FF ; ????
A284: 04 ; ????
A285: 52 ; ????
A286: 52 ; ????
A287: 52 ; ????
A288: 52 ; ????
A289: FF ; ????
A28A: 04 ; ????
A28B: 70 70           BVS     $A2FD               ; {}
A28D: 70 70           BVS     $A2FF               ; {}
A28F: FF ; ????
A290: 02 ; ????
A291: 70 70           BVS     $A303               ; {}
A293: FF ; ????
A294: 04 ; ????
A295: 08              PHP                         
A296: 07 ; ????
A297: 07 ; ????
A298: 08              PHP                         
A299: FF ; ????
A29A: 01 01           ORA     ($01,X)             
A29C: 01 03           ORA     ($03,X)             
A29E: 01 04           ORA     ($04,X)             
A2A0: 01 01           ORA     ($01,X)             
A2A2: FF ; ????
A2A3: 04 ; ????
A2A4: 52 ; ????
A2A5: 52 ; ????
A2A6: 52 ; ????
A2A7: 52 ; ????
A2A8: 04 ; ????
A2A9: 52 ; ????
A2AA: 52 ; ????
A2AB: 52 ; ????
A2AC: 52 ; ????
A2AD: 04 ; ????
A2AE: 52 ; ????
A2AF: 52 ; ????
A2B0: 52 ; ????
A2B1: 52 ; ????
A2B2: 04 ; ????
A2B3: 52 ; ????
A2B4: 52 ; ????
A2B5: 52 ; ????
A2B6: 52 ; ????
A2B7: FF ; ????
A2B8: 01 05           ORA     ($05,X)             
A2BA: 01 06           ORA     ($06,X)             
A2BC: 01 01           ORA     ($01,X)             
A2BE: 01 01           ORA     ($01,X)             
A2C0: FF ; ????
A2C1: 01 5D           ORA     ($5D,X)             
A2C3: FF ; ????
A2C4: 02 ; ????
A2C5: 54 ; ????
A2C6: 54 ; ????
A2C7: 02 ; ????
A2C8: 54 ; ????
A2C9: 54 ; ????
A2CA: FF ; ????
A2CB: 02 ; ????
A2CC: 40              RTI                         
A2CD: 40              RTI                         
A2CE: FF ; ????
A2CF: 04 ; ????
A2D0: 40              RTI                         
A2D1: 40              RTI                         
A2D2: 40              RTI                         
A2D3: 40              RTI                         
A2D4: FF ; ????
A2D5: 01 6F           ORA     ($6F,X)             
A2D7: FF ; ????
A2D8: 03 ; ????
A2D9: 38              SEC                         
A2DA: 38              SEC                         
A2DB: 38              SEC                         
A2DC: FF ; ????
A2DD: 04 ; ????
A2DE: 30 30           BMI     $A310               ; {}
A2E0: 30 30           BMI     $A312               ; {}
A2E2: FF ; ????
A2E3: 02 ; ????
A2E4: 48              PHA                         
A2E5: 49 FF           EOR     #$FF                
A2E7: 01 56           ORA     ($56,X)             
A2E9: 01 56           ORA     ($56,X)             
A2EB: 01 56           ORA     ($56,X)             
A2ED: 01 56           ORA     ($56,X)             
A2EF: FF ; ????
A2F0: 04 ; ????
A2F1: 56 56           LSR     $56,X               
A2F3: 56 56           LSR     $56,X               
A2F5: FF ; ????
A2F6: 01 57           ORA     ($57,X)             
A2F8: FF ; ????
A2F9: 01 58           ORA     ($58,X)             
A2FB: 01 58           ORA     ($58,X)             
A2FD: 01 58           ORA     ($58,X)             
A2FF: 01 58           ORA     ($58,X)             
A301: FF ; ????
A302: 04 ; ????
A303: 58              CLI                         
A304: 58              CLI                         
A305: 58              CLI                         
A306: 58              CLI                         
A307: FF ; ????
A308: 04 ; ????
A309: 5C ; ????
A30A: 5C ; ????
A30B: 5C ; ????
A30C: 5C ; ????
A30D: FF ; ????
A30E: 12 ; ????
A30F: 12 ; ????
A310: 12 ; ????
A311: 12 ; ????
A312: 8F ; ????
A313: 90 6D           BCC     $A382               ; {}
A315: 6E 91 92        ROR     $9291               ; {}
A318: 91 92           STA     ($92),Y             
A31A: 8F ; ????
A31B: 90 91           BCC     $A2AE               ; {}
A31D: 92 ; ????
A31E: 91 92           STA     ($92),Y             
A320: 6D 6E 69        ADC     $696E               
A323: 6A              ROR     A                   
A324: 6B ; ????
A325: 6C A5 A6        JMP     ($A6A5)             ; {}
A328: A7 ; ????
A329: A8              TAY                         
A32A: AF ; ????
A32B: AE 12 12        LDX     $1212               
A32E: A9 AE           LDA     #$AE                
A330: AF ; ????
A331: 12 ; ????
A332: 4D 4D B2        EOR     $B24D               ; {}
A335: B2 ; ????
A336: B2 ; ????
A337: B2 ; ????
A338: B2 ; ????
A339: B2 ; ????
A33A: 2B ; ????
A33B: 12 ; ????
A33C: 12 ; ????
A33D: 12 ; ????
A33E: 2B ; ????
A33F: 12 ; ????
A340: 12 ; ????
A341: 12 ; ????
A342: 2B ; ????
A343: 12 ; ????
A344: 12 ; ????
A345: 12 ; ????
A346: 2B ; ????
A347: 12 ; ????
A348: 12 ; ????
A349: 12 ; ????
A34A: 2B ; ????
A34B: 12 ; ????
A34C: 12 ; ????
A34D: 12 ; ????
A34E: 2B ; ????
A34F: 12 ; ????
A350: 12 ; ????
A351: 12 ; ????
A352: 2B ; ????
A353: 12 ; ????
A354: 12 ; ????
A355: 12 ; ????
A356: 2B ; ????
A357: 12 ; ????
A358: 12 ; ????
A359: 12 ; ????
A35A: 2B ; ????
A35B: 12 ; ????
A35C: 12 ; ????
A35D: 12 ; ????
A35E: 2B ; ????
A35F: 12 ; ????
A360: 12 ; ????
A361: 12 ; ????
A362: 2B ; ????
A363: 12 ; ????
A364: 12 ; ????
A365: 12 ; ????
A366: 2B ; ????
A367: 12 ; ????
A368: 12 ; ????
A369: 12 ; ????
A36A: 2B ; ????
A36B: 12 ; ????
A36C: 12 ; ????
A36D: 12 ; ????
A36E: 2B ; ????
A36F: 12 ; ????
A370: 12 ; ????
A371: 12 ; ????
A372: 2B ; ????
A373: 12 ; ????
A374: 12 ; ????
A375: 12 ; ????
A376: 2B ; ????
A377: 12 ; ????
A378: 12 ; ????
A379: 12 ; ????
A37A: 2B ; ????
A37B: 12 ; ????
A37C: 12 ; ????
A37D: 12 ; ????
A37E: 2B ; ????
A37F: 12 ; ????
A380: 12 ; ????
A381: 12 ; ????
A382: 2B ; ????
A383: 12 ; ????
A384: 12 ; ????
A385: 12 ; ????
A386: 2B ; ????
A387: 12 ; ????
A388: 12 ; ????
A389: 12 ; ????
A38A: 2B ; ????
A38B: 12 ; ????
A38C: 12 ; ????
A38D: 12 ; ????
A38E: 2B ; ????
A38F: 12 ; ????
A390: 12 ; ????
A391: 12 ; ????
A392: 2B ; ????
A393: 12 ; ????
A394: 12 ; ????
A395: 12 ; ????
A396: 2B ; ????
A397: 12 ; ????
A398: 12 ; ????
A399: 12 ; ????
A39A: 2B ; ????
A39B: 12 ; ????
A39C: 12 ; ????
A39D: 12 ; ????
A39E: 2B ; ????
A39F: 12 ; ????
A3A0: 12 ; ????
A3A1: 12 ; ????
A3A2: 2B ; ????
A3A3: 12 ; ????
A3A4: 12 ; ????
A3A5: 12 ; ????
A3A6: 2B ; ????
A3A7: 12 ; ????
A3A8: 12 ; ????
A3A9: 12 ; ????
A3AA: 2B ; ????
A3AB: 12 ; ????
A3AC: 12 ; ????
A3AD: 12 ; ????
A3AE: 2B ; ????
A3AF: 12 ; ????
A3B0: 12 ; ????
A3B1: 12 ; ????
A3B2: 2B ; ????
A3B3: 12 ; ????
A3B4: 12 ; ????
A3B5: 12 ; ????
A3B6: 64 ; ????
A3B7: 65 64           ADC     $64                 
A3B9: 65 2B           ADC     $2B                 
A3BB: 12 ; ????
A3BC: 12 ; ????
A3BD: 12 ; ????
A3BE: 2B ; ????
A3BF: 12 ; ????
A3C0: 12 ; ????
A3C1: 12 ; ????
A3C2: 2B ; ????
A3C3: 12 ; ????
A3C4: 12 ; ????
A3C5: 12 ; ????
A3C6: 9F ; ????
A3C7: A0 9F           LDY     #$9F                
A3C9: A0 A0           LDY     #$A0                
A3CB: 9F ; ????
A3CC: A0 9F           LDY     #$9F                
A3CE: AA              TAX                         
A3CF: AA              TAX                         
A3D0: AB ; ????
A3D1: AB ; ????
A3D2: 2B ; ????
A3D3: 12 ; ????
A3D4: 12 ; ????
A3D5: 12 ; ????
A3D6: 2B ; ????
A3D7: 12 ; ????
A3D8: 12 ; ????
A3D9: 12 ; ????
A3DA: 2B ; ????
A3DB: 12 ; ????
A3DC: 12 ; ????
A3DD: 12 ; ????
A3DE: 2B ; ????
A3DF: 12 ; ????
A3E0: 12 ; ????
A3E1: 12 ; ????
A3E2: 2B ; ????
A3E3: 12 ; ????
A3E4: 12 ; ????
A3E5: 12 ; ????
A3E6: 2B ; ????
A3E7: 12 ; ????
A3E8: 12 ; ????
A3E9: 12 ; ????
A3EA: 2B ; ????
A3EB: 12 ; ????
A3EC: 12 ; ????
A3ED: 12 ; ????
A3EE: 4D 4D B2        EOR     $B24D               ; {}
A3F1: B2 ; ????
A3F2: 2B ; ????
A3F3: 12 ; ????
A3F4: 12 ; ????
A3F5: 12 ; ????
A3F6: 2B ; ????
A3F7: 12 ; ????
A3F8: 12 ; ????
A3F9: 12 ; ????
A3FA: 2B ; ????
A3FB: 12 ; ????
A3FC: 12 ; ????
A3FD: 12 ; ????
A3FE: 2B ; ????
A3FF: 12 ; ????
A400: 12 ; ????
A401: 12 ; ????
A402: 2B ; ????
A403: 12 ; ????
A404: 12 ; ????
A405: 12 ; ????
A406: 2B ; ????
A407: 12 ; ????
A408: 12 ; ????
A409: 12 ; ????
A40A: 2B ; ????
A40B: 12 ; ????
A40C: 12 ; ????
A40D: 12 ; ????
A40E: B0 B0           BCS     $A3C0               ; {}
A410: 12 ; ????
A411: 12 ; ????
A412: 2B ; ????
A413: 12 ; ????
A414: 12 ; ????
A415: 12 ; ????
A416: 2B ; ????
A417: 12 ; ????
A418: 12 ; ????
A419: 12 ; ????
A41A: 2B ; ????
A41B: 12 ; ????
A41C: 12 ; ????
A41D: 12 ; ????
A41E: 2B ; ????
A41F: 12 ; ????
A420: 12 ; ????
A421: 12 ; ????
A422: 2B ; ????
A423: 12 ; ????
A424: 12 ; ????
A425: 12 ; ????
A426: 2B ; ????
A427: 12 ; ????
A428: 12 ; ????
A429: 12 ; ????
A42A: 2B ; ????
A42B: 12 ; ????
A42C: 12 ; ????
A42D: 12 ; ????
A42E: D7 ; ????
A42F: D8              CLD                         
A430: DF ; ????
A431: E0 D8           CPX     #$D8                
A433: D9 E1 E2        CMP     $E2E1,Y             
A436: 2B ; ????
A437: 12 ; ????
A438: 12 ; ????
A439: 12 ; ????
A43A: 2B ; ????
A43B: 12 ; ????
A43C: 12 ; ????
A43D: 12 ; ????
A43E: 2B ; ????
A43F: 12 ; ????
A440: 12 ; ????
A441: 12 ; ????
A442: 2B ; ????
A443: 12 ; ????
A444: 12 ; ????
A445: 12 ; ????
A446: 2B ; ????
A447: 12 ; ????
A448: 12 ; ????
A449: 12 ; ????
A44A: 2B ; ????
A44B: 12 ; ????
A44C: 12 ; ????
A44D: 12 ; ????
A44E: 60              RTS                         
A44F: 61 64           ADC     ($64,X)             
A451: 65 14           ADC     $14                 
A453: 15 15           ORA     $15,X               
A455: 14 ; ????
A456: C0 C1           CPY     #$C1                
A458: C2 ; ????
A459: C3 ; ????
A45A: 8F ; ????
A45B: 90 6D           BCC     $A4CA               ; {}
A45D: 6E B1 B1        ROR     $B1B1               ; {}
A460: B1 B1           LDA     ($B1),Y             
A462: 60              RTS                         
A463: 61 62           ADC     ($62,X)             
A465: 63 ; ????
A466: 52 ; ????
A467: 53 ; ????
A468: 53 ; ????
A469: 52 ; ????
A46A: 54 ; ????
A46B: 55 56           EOR     $56,X               
A46D: 57 ; ????
A46E: 4E 4F 4F        LSR     $4F4F               
A471: 4E AA AA        LSR     $AAAA               ; {}
A474: AB ; ????
A475: AB ; ????
A476: AB ; ????
A477: AB ; ????
A478: AB ; ????
A479: AB ; ????
A47A: 9A              TXS                         
A47B: 9A              TXS                         
A47C: 12 ; ????
A47D: 12 ; ????
A47E: 9B ; ????
A47F: 9C ; ????
A480: 9D 9E 58        STA     $589E,X             
A483: 59 5A 66        EOR     $665A,Y             
A486: 62 ; ????
A487: 63 ; ????
A488: 62 ; ????
A489: 63 ; ????
A48A: 2B ; ????
A48B: 12 ; ????
A48C: 12 ; ????
A48D: 12 ; ????
A48E: 2B ; ????
A48F: 12 ; ????
A490: 12 ; ????
A491: 12 ; ????
A492: 2B ; ????
A493: 12 ; ????
A494: 12 ; ????
A495: 12 ; ????
A496: 2B ; ????
A497: 12 ; ????
A498: 12 ; ????
A499: 12 ; ????
A49A: 2B ; ????
A49B: 12 ; ????
A49C: 12 ; ????
A49D: 12 ; ????
A49E: 2B ; ????
A49F: 12 ; ????
A4A0: 12 ; ????
A4A1: 12 ; ????
A4A2: 2B ; ????
A4A3: 12 ; ????
A4A4: 12 ; ????
A4A5: 12 ; ????
A4A6: 2B ; ????
A4A7: 12 ; ????
A4A8: 12 ; ????
A4A9: 12 ; ????
A4AA: 2B ; ????
A4AB: 12 ; ????
A4AC: 12 ; ????
A4AD: 12 ; ????
A4AE: 9F ; ????
A4AF: A0 9F           LDY     #$9F                
A4B1: A0 A0           LDY     #$A0                
A4B3: 9F ; ????
A4B4: A0 9F           LDY     #$9F                
A4B6: 75 76           ADC     $76,X               
A4B8: 77 ; ????
A4B9: 78              SEI                         
A4BA: 2B ; ????
A4BB: 12 ; ????
A4BC: 12 ; ????
A4BD: 12 ; ????
A4BE: 2B ; ????
A4BF: 12 ; ????
A4C0: 12 ; ????
A4C1: 12 ; ????
A4C2: 2B ; ????
A4C3: 12 ; ????
A4C4: 12 ; ????
A4C5: 12 ; ????
A4C6: 2B ; ????
A4C7: 12 ; ????
A4C8: 12 ; ????
A4C9: 12 ; ????
A4CA: A1 A2           LDA     ($A2,X)             
A4CC: A3 ; ????
A4CD: A4 C0           LDY     $C0                 
A4CF: C1 12           CMP     ($12,X)             
A4D1: 12 ; ????
A4D2: FF ; ????
A4D3: FF ; ????
A4D4: FF ; ????
A4D5: FF ; ????
A4D6: FF ; ????
A4D7: FF ; ????
A4D8: FF ; ????
A4D9: FF ; ????
A4DA: FF ; ????
A4DB: FF ; ????
A4DC: FF ; ????
A4DD: FF ; ????
A4DE: FF ; ????
A4DF: FF ; ????
A4E0: FF ; ????
A4E1: FF ; ????
A4E2: FF ; ????
A4E3: FF ; ????
A4E4: FF ; ????
A4E5: FF ; ????
A4E6: EF ; ????
A4E7: FF ; ????
A4E8: FF ; ????
A4E9: FF ; ????
A4EA: FF ; ????
A4EB: FF ; ????
A4EC: FF ; ????
A4ED: FF ; ????
A4EE: FF ; ????
A4EF: FF ; ????
A4F0: FF ; ????
A4F1: FF ; ????
A4F2: FF ; ????
A4F3: FF ; ????
A4F4: FF ; ????
A4F5: FF ; ????
A4F6: FF ; ????
A4F7: FF ; ????
A4F8: FF ; ????
A4F9: FF ; ????
A4FA: FF ; ????
A4FB: FF ; ????
A4FC: FF ; ????
A4FD: FF ; ????
A4FE: FF ; ????
A4FF: FF ; ????
A500: 00              BRK                         
A501: 00              BRK                         
A502: 00              BRK                         
A503: 00              BRK                         
A504: 00              BRK                         
A505: 00              BRK                         
A506: 00              BRK                         
A507: 00              BRK                         
A508: 00              BRK                         
A509: 00              BRK                         
A50A: 00              BRK                         
A50B: 00              BRK                         
A50C: 00              BRK                         
A50D: 00              BRK                         
A50E: 00              BRK                         
A50F: 00              BRK                         
A510: 00              BRK                         
A511: 00              BRK                         
A512: 00              BRK                         
A513: 00              BRK                         
A514: 00              BRK                         
A515: 00              BRK                         
A516: 00              BRK                         
A517: 00              BRK                         
A518: 00              BRK                         
A519: 00              BRK                         
A51A: 00              BRK                         
A51B: 00              BRK                         
A51C: 00              BRK                         
A51D: 00              BRK                         
A51E: 00              BRK                         
A51F: 00              BRK                         
A520: 00              BRK                         
A521: 00              BRK                         
A522: 00              BRK                         
A523: 00              BRK                         
A524: 00              BRK                         
A525: 00              BRK                         
A526: 00              BRK                         
A527: 00              BRK                         
A528: 00              BRK                         
A529: 00              BRK                         
A52A: 00              BRK                         
A52B: 00              BRK                         
A52C: 00              BRK                         
A52D: 00              BRK                         
A52E: 00              BRK                         
A52F: 00              BRK                         
A530: 00              BRK                         
A531: 00              BRK                         
A532: 00              BRK                         
A533: 00              BRK                         
A534: 00              BRK                         
A535: 00              BRK                         
A536: 00              BRK                         
A537: 00              BRK                         
A538: 00              BRK                         
A539: 00              BRK                         
A53A: 00              BRK                         
A53B: 00              BRK                         
A53C: 00              BRK                         
A53D: 00              BRK                         
A53E: 00              BRK                         
A53F: 00              BRK                         
A540: 00              BRK                         
A541: 00              BRK                         
A542: 00              BRK                         
A543: 00              BRK                         
A544: 00              BRK                         
A545: 00              BRK                         
A546: 00              BRK                         
A547: 00              BRK                         
A548: 00              BRK                         
A549: 00              BRK                         
A54A: 00              BRK                         
A54B: 00              BRK                         
A54C: 00              BRK                         
A54D: 00              BRK                         
A54E: 00              BRK                         
A54F: 00              BRK                         
A550: 00              BRK                         
A551: 00              BRK                         
A552: 00              BRK                         
A553: 00              BRK                         
A554: 00              BRK                         
A555: 00              BRK                         
A556: 00              BRK                         
A557: 00              BRK                         
A558: 00              BRK                         
A559: 00              BRK                         
A55A: 00              BRK                         
A55B: 00              BRK                         
A55C: 00              BRK                         
A55D: 00              BRK                         
A55E: 00              BRK                         
A55F: 00              BRK                         
A560: 00              BRK                         
A561: 00              BRK                         
A562: 00              BRK                         
A563: 00              BRK                         
A564: 00              BRK                         
A565: 00              BRK                         
A566: 00              BRK                         
A567: 00              BRK                         
A568: 00              BRK                         
A569: 00              BRK                         
A56A: 00              BRK                         
A56B: 00              BRK                         
A56C: 00              BRK                         
A56D: 00              BRK                         
A56E: 00              BRK                         
A56F: 00              BRK                         
A570: 00              BRK                         
A571: 00              BRK                         
A572: 00              BRK                         
A573: 00              BRK                         
A574: 00              BRK                         
A575: 00              BRK                         
A576: 00              BRK                         
A577: 00              BRK                         
A578: 00              BRK                         
A579: 00              BRK                         
A57A: 00              BRK                         
A57B: 00              BRK                         
A57C: 00              BRK                         
A57D: 00              BRK                         
A57E: 00              BRK                         
A57F: 00              BRK                         
A580: 00              BRK                         
A581: 00              BRK                         
A582: 00              BRK                         
A583: 00              BRK                         
A584: 00              BRK                         
A585: 00              BRK                         
A586: 00              BRK                         
A587: 00              BRK                         
A588: 00              BRK                         
A589: 00              BRK                         
A58A: 00              BRK                         
A58B: 00              BRK                         
A58C: 00              BRK                         
A58D: 00              BRK                         
A58E: 00              BRK                         
A58F: 00              BRK                         
A590: 00              BRK                         
A591: 00              BRK                         
A592: 00              BRK                         
A593: 00              BRK                         
A594: 00              BRK                         
A595: 00              BRK                         
A596: 00              BRK                         
A597: 00              BRK                         
A598: 00              BRK                         
A599: 00              BRK                         
A59A: 00              BRK                         
A59B: 00              BRK                         
A59C: 00              BRK                         
A59D: 00              BRK                         
A59E: 00              BRK                         
A59F: 00              BRK                         
A5A0: 00              BRK                         
A5A1: 00              BRK                         
A5A2: 00              BRK                         
A5A3: 00              BRK                         
A5A4: 00              BRK                         
A5A5: 00              BRK                         
A5A6: 00              BRK                         
A5A7: 00              BRK                         
A5A8: 00              BRK                         
A5A9: 00              BRK                         
A5AA: 00              BRK                         
A5AB: 00              BRK                         
A5AC: 00              BRK                         
A5AD: 00              BRK                         
A5AE: 00              BRK                         
A5AF: 00              BRK                         
A5B0: 00              BRK                         
A5B1: 00              BRK                         
A5B2: 00              BRK                         
A5B3: 00              BRK                         
A5B4: 00              BRK                         
A5B5: 00              BRK                         
A5B6: 00              BRK                         
A5B7: 00              BRK                         
A5B8: 00              BRK                         
A5B9: 00              BRK                         
A5BA: 00              BRK                         
A5BB: 00              BRK                         
A5BC: 00              BRK                         
A5BD: 00              BRK                         
A5BE: 00              BRK                         
A5BF: 00              BRK                         
A5C0: 00              BRK                         
A5C1: 00              BRK                         
A5C2: 00              BRK                         
A5C3: 00              BRK                         
A5C4: 00              BRK                         
A5C5: 00              BRK                         
A5C6: 00              BRK                         
A5C7: 00              BRK                         
A5C8: 00              BRK                         
A5C9: 00              BRK                         
A5CA: 00              BRK                         
A5CB: 00              BRK                         
A5CC: 00              BRK                         
A5CD: 00              BRK                         
A5CE: 00              BRK                         
A5CF: 00              BRK                         
A5D0: 00              BRK                         
A5D1: 00              BRK                         
A5D2: 00              BRK                         
A5D3: 00              BRK                         
A5D4: 00              BRK                         
A5D5: 00              BRK                         
A5D6: 00              BRK                         
A5D7: 00              BRK                         
A5D8: 00              BRK                         
A5D9: 00              BRK                         
A5DA: 00              BRK                         
A5DB: 00              BRK                         
A5DC: 00              BRK                         
A5DD: 00              BRK                         
A5DE: 00              BRK                         
A5DF: 00              BRK                         
A5E0: 00              BRK                         
A5E1: 00              BRK                         
A5E2: 00              BRK                         
A5E3: 00              BRK                         
A5E4: 00              BRK                         
A5E5: 00              BRK                         
A5E6: 00              BRK                         
A5E7: 00              BRK                         
A5E8: 00              BRK                         
A5E9: 00              BRK                         
A5EA: 00              BRK                         
A5EB: 00              BRK                         
A5EC: 00              BRK                         
A5ED: 00              BRK                         
A5EE: 00              BRK                         
A5EF: 00              BRK                         
A5F0: 00              BRK                         
A5F1: 00              BRK                         
A5F2: 00              BRK                         
A5F3: 00              BRK                         
A5F4: 00              BRK                         
A5F5: 00              BRK                         
A5F6: 00              BRK                         
A5F7: 00              BRK                         
A5F8: 00              BRK                         
A5F9: 00              BRK                         
A5FA: 00              BRK                         
A5FB: 00              BRK                         
A5FC: 00              BRK                         
A5FD: 00              BRK                         
A5FE: 00              BRK                         
A5FF: 00              BRK                         
A600: FF ; ????
A601: FF ; ????
A602: FF ; ????
A603: FF ; ????
A604: FF ; ????
A605: FF ; ????
A606: FF ; ????
A607: FF ; ????
A608: FF ; ????
A609: FF ; ????
A60A: FF ; ????
A60B: FF ; ????
A60C: FF ; ????
A60D: FF ; ????
A60E: FF ; ????
A60F: FF ; ????
A610: FF ; ????
A611: FF ; ????
A612: FF ; ????
A613: FF ; ????
A614: FF ; ????
A615: FF ; ????
A616: FF ; ????
A617: FF ; ????
A618: FF ; ????
A619: FF ; ????
A61A: FF ; ????
A61B: FF ; ????
A61C: FF ; ????
A61D: FF ; ????
A61E: FF ; ????
A61F: FF ; ????
A620: FF ; ????
A621: FF ; ????
A622: FF ; ????
A623: FF ; ????
A624: FF ; ????
A625: FF ; ????
A626: FF ; ????
A627: FF ; ????
A628: FF ; ????
A629: FF ; ????
A62A: FF ; ????
A62B: FF ; ????
A62C: FF ; ????
A62D: FF ; ????
A62E: FF ; ????
A62F: FF ; ????
A630: FF ; ????
A631: FF ; ????
A632: FF ; ????
A633: FF ; ????
A634: FF ; ????
A635: FF ; ????
A636: FF ; ????
A637: FF ; ????
A638: FF ; ????
A639: FF ; ????
A63A: FF ; ????
A63B: FF ; ????
A63C: FF ; ????
A63D: FF ; ????
A63E: FF ; ????
A63F: FF ; ????
A640: FF ; ????
A641: FF ; ????
A642: FF ; ????
A643: FF ; ????
A644: FF ; ????
A645: FF ; ????
A646: FF ; ????
A647: FF ; ????
A648: FF ; ????
A649: FF ; ????
A64A: FF ; ????
A64B: FF ; ????
A64C: FF ; ????
A64D: FF ; ????
A64E: FF ; ????
A64F: FF ; ????
A650: FF ; ????
A651: FF ; ????
A652: FF ; ????
A653: FF ; ????
A654: FF ; ????
A655: FF ; ????
A656: FF ; ????
A657: FF ; ????
A658: FF ; ????
A659: FF ; ????
A65A: FF ; ????
A65B: FF ; ????
A65C: FF ; ????
A65D: FF ; ????
A65E: FF ; ????
A65F: FF ; ????
A660: FF ; ????
A661: FF ; ????
A662: FF ; ????
A663: FF ; ????
A664: FF ; ????
A665: FF ; ????
A666: FF ; ????
A667: FF ; ????
A668: FF ; ????
A669: FF ; ????
A66A: FF ; ????
A66B: FF ; ????
A66C: FF ; ????
A66D: FF ; ????
A66E: FF ; ????
A66F: FF ; ????
A670: FF ; ????
A671: FF ; ????
A672: FF ; ????
A673: FF ; ????
A674: FF ; ????
A675: FF ; ????
A676: FF ; ????
A677: FF ; ????
A678: FF ; ????
A679: FF ; ????
A67A: FF ; ????
A67B: FF ; ????
A67C: FF ; ????
A67D: FF ; ????
A67E: FF ; ????
A67F: FF ; ????
A680: FF ; ????
A681: FF ; ????
A682: FF ; ????
A683: FF ; ????
A684: FF ; ????
A685: FF ; ????
A686: FF ; ????
A687: FF ; ????
A688: FF ; ????
A689: FF ; ????
A68A: FF ; ????
A68B: FF ; ????
A68C: FF ; ????
A68D: FF ; ????
A68E: FF ; ????
A68F: FF ; ????
A690: FF ; ????
A691: FF ; ????
A692: FF ; ????
A693: FF ; ????
A694: FF ; ????
A695: FF ; ????
A696: FF ; ????
A697: FF ; ????
A698: FF ; ????
A699: FF ; ????
A69A: FF ; ????
A69B: FF ; ????
A69C: FF ; ????
A69D: FF ; ????
A69E: FF ; ????
A69F: FF ; ????
A6A0: FF ; ????
A6A1: FF ; ????
A6A2: FF ; ????
A6A3: FF ; ????
A6A4: FF ; ????
A6A5: FF ; ????
A6A6: FF ; ????
A6A7: FF ; ????
A6A8: FF ; ????
A6A9: FF ; ????
A6AA: FF ; ????
A6AB: FF ; ????
A6AC: FF ; ????
A6AD: FF ; ????
A6AE: FF ; ????
A6AF: FF ; ????
A6B0: FF ; ????
A6B1: FF ; ????
A6B2: FF ; ????
A6B3: FF ; ????
A6B4: FF ; ????
A6B5: FF ; ????
A6B6: FF ; ????
A6B7: FF ; ????
A6B8: FF ; ????
A6B9: FF ; ????
A6BA: FF ; ????
A6BB: FF ; ????
A6BC: FF ; ????
A6BD: FF ; ????
A6BE: FF ; ????
A6BF: FF ; ????
A6C0: FF ; ????
A6C1: FF ; ????
A6C2: FF ; ????
A6C3: FF ; ????
A6C4: FF ; ????
A6C5: FF ; ????
A6C6: FF ; ????
A6C7: FF ; ????
A6C8: FF ; ????
A6C9: FF ; ????
A6CA: FF ; ????
A6CB: FF ; ????
A6CC: FF ; ????
A6CD: FF ; ????
A6CE: FF ; ????
A6CF: FF ; ????
A6D0: FF ; ????
A6D1: FF ; ????
A6D2: FF ; ????
A6D3: FF ; ????
A6D4: FF ; ????
A6D5: FF ; ????
A6D6: FF ; ????
A6D7: FF ; ????
A6D8: FF ; ????
A6D9: FF ; ????
A6DA: FF ; ????
A6DB: FF ; ????
A6DC: FF ; ????
A6DD: FF ; ????
A6DE: FF ; ????
A6DF: FF ; ????
A6E0: FF ; ????
A6E1: FF ; ????
A6E2: FF ; ????
A6E3: FF ; ????
A6E4: FF ; ????
A6E5: FF ; ????
A6E6: FF ; ????
A6E7: FF ; ????
A6E8: FF ; ????
A6E9: FF ; ????
A6EA: FF ; ????
A6EB: FF ; ????
A6EC: FF ; ????
A6ED: FF ; ????
A6EE: FF ; ????
A6EF: FF ; ????
A6F0: FF ; ????
A6F1: FF ; ????
A6F2: FF ; ????
A6F3: FF ; ????
A6F4: FF ; ????
A6F5: FF ; ????
A6F6: FF ; ????
A6F7: FF ; ????
A6F8: FF ; ????
A6F9: FF ; ????
A6FA: FF ; ????
A6FB: FF ; ????
A6FC: FF ; ????
A6FD: FF ; ????
A6FE: FF ; ????
A6FF: FF ; ????
A700: 00              BRK                         
A701: 00              BRK                         
A702: 00              BRK                         
A703: 00              BRK                         
A704: 00              BRK                         
A705: 00              BRK                         
A706: 00              BRK                         
A707: 00              BRK                         
A708: 00              BRK                         
A709: 00              BRK                         
A70A: 00              BRK                         
A70B: 00              BRK                         
A70C: 00              BRK                         
A70D: 00              BRK                         
A70E: 00              BRK                         
A70F: 00              BRK                         
A710: 00              BRK                         
A711: 00              BRK                         
A712: 00              BRK                         
A713: 00              BRK                         
A714: 00              BRK                         
A715: 00              BRK                         
A716: 00              BRK                         
A717: 00              BRK                         
A718: 00              BRK                         
A719: 00              BRK                         
A71A: 00              BRK                         
A71B: 00              BRK                         
A71C: 00              BRK                         
A71D: 00              BRK                         
A71E: 00              BRK                         
A71F: 00              BRK                         
A720: 00              BRK                         
A721: 00              BRK                         
A722: 00              BRK                         
A723: 00              BRK                         
A724: 00              BRK                         
A725: 00              BRK                         
A726: 00              BRK                         
A727: 00              BRK                         
A728: 00              BRK                         
A729: 00              BRK                         
A72A: 00              BRK                         
A72B: 00              BRK                         
A72C: 00              BRK                         
A72D: 00              BRK                         
A72E: 00              BRK                         
A72F: 00              BRK                         
A730: 00              BRK                         
A731: 00              BRK                         
A732: 00              BRK                         
A733: 00              BRK                         
A734: 00              BRK                         
A735: 00              BRK                         
A736: 00              BRK                         
A737: 00              BRK                         
A738: 00              BRK                         
A739: 00              BRK                         
A73A: 00              BRK                         
A73B: 00              BRK                         
A73C: 00              BRK                         
A73D: 00              BRK                         
A73E: 00              BRK                         
A73F: 00              BRK                         
A740: 00              BRK                         
A741: 00              BRK                         
A742: 00              BRK                         
A743: 00              BRK                         
A744: 00              BRK                         
A745: 00              BRK                         
A746: 00              BRK                         
A747: 00              BRK                         
A748: 00              BRK                         
A749: 00              BRK                         
A74A: 00              BRK                         
A74B: 00              BRK                         
A74C: 00              BRK                         
A74D: 00              BRK                         
A74E: 00              BRK                         
A74F: 00              BRK                         
A750: 00              BRK                         
A751: 00              BRK                         
A752: 00              BRK                         
A753: 00              BRK                         
A754: 00              BRK                         
A755: 00              BRK                         
A756: 00              BRK                         
A757: 00              BRK                         
A758: 00              BRK                         
A759: 00              BRK                         
A75A: 00              BRK                         
A75B: 00              BRK                         
A75C: 00              BRK                         
A75D: 00              BRK                         
A75E: 00              BRK                         
A75F: 00              BRK                         
A760: 00              BRK                         
A761: 00              BRK                         
A762: 00              BRK                         
A763: 00              BRK                         
A764: 00              BRK                         
A765: 00              BRK                         
A766: 00              BRK                         
A767: 00              BRK                         
A768: 00              BRK                         
A769: 00              BRK                         
A76A: 00              BRK                         
A76B: 00              BRK                         
A76C: 00              BRK                         
A76D: 00              BRK                         
A76E: 00              BRK                         
A76F: 00              BRK                         
A770: 00              BRK                         
A771: 00              BRK                         
A772: 00              BRK                         
A773: 00              BRK                         
A774: 00              BRK                         
A775: 00              BRK                         
A776: 00              BRK                         
A777: 00              BRK                         
A778: 00              BRK                         
A779: 00              BRK                         
A77A: 00              BRK                         
A77B: 00              BRK                         
A77C: 00              BRK                         
A77D: 00              BRK                         
A77E: 00              BRK                         
A77F: 00              BRK                         
A780: 00              BRK                         
A781: 00              BRK                         
A782: 00              BRK                         
A783: 00              BRK                         
A784: 00              BRK                         
A785: 00              BRK                         
A786: 00              BRK                         
A787: 00              BRK                         
A788: 00              BRK                         
A789: 00              BRK                         
A78A: 00              BRK                         
A78B: 00              BRK                         
A78C: 00              BRK                         
A78D: 00              BRK                         
A78E: 00              BRK                         
A78F: 00              BRK                         
A790: 00              BRK                         
A791: 00              BRK                         
A792: 00              BRK                         
A793: 00              BRK                         
A794: 00              BRK                         
A795: 00              BRK                         
A796: 00              BRK                         
A797: 00              BRK                         
A798: 00              BRK                         
A799: 00              BRK                         
A79A: 00              BRK                         
A79B: 00              BRK                         
A79C: 00              BRK                         
A79D: 00              BRK                         
A79E: 00              BRK                         
A79F: 00              BRK                         
A7A0: 00              BRK                         
A7A1: 00              BRK                         
A7A2: 00              BRK                         
A7A3: 00              BRK                         
A7A4: 00              BRK                         
A7A5: 00              BRK                         
A7A6: 00              BRK                         
A7A7: 00              BRK                         
A7A8: 00              BRK                         
A7A9: 00              BRK                         
A7AA: 00              BRK                         
A7AB: 00              BRK                         
A7AC: 00              BRK                         
A7AD: 00              BRK                         
A7AE: 00              BRK                         
A7AF: 00              BRK                         
A7B0: 00              BRK                         
A7B1: 00              BRK                         
A7B2: 00              BRK                         
A7B3: 00              BRK                         
A7B4: 00              BRK                         
A7B5: 00              BRK                         
A7B6: 00              BRK                         
A7B7: 00              BRK                         
A7B8: 00              BRK                         
A7B9: 00              BRK                         
A7BA: 00              BRK                         
A7BB: 00              BRK                         
A7BC: 00              BRK                         
A7BD: 00              BRK                         
A7BE: 00              BRK                         
A7BF: 00              BRK                         
A7C0: 00              BRK                         
A7C1: 00              BRK                         
A7C2: 00              BRK                         
A7C3: 00              BRK                         
A7C4: 00              BRK                         
A7C5: 00              BRK                         
A7C6: 00              BRK                         
A7C7: 00              BRK                         
A7C8: 00              BRK                         
A7C9: 00              BRK                         
A7CA: 00              BRK                         
A7CB: 00              BRK                         
A7CC: 00              BRK                         
A7CD: 00              BRK                         
A7CE: 00              BRK                         
A7CF: 00              BRK                         
A7D0: 00              BRK                         
A7D1: 00              BRK                         
A7D2: 00              BRK                         
A7D3: 00              BRK                         
A7D4: 00              BRK                         
A7D5: 00              BRK                         
A7D6: 00              BRK                         
A7D7: 00              BRK                         
A7D8: 00              BRK                         
A7D9: 00              BRK                         
A7DA: 00              BRK                         
A7DB: 00              BRK                         
A7DC: 00              BRK                         
A7DD: 00              BRK                         
A7DE: 00              BRK                         
A7DF: 00              BRK                         
A7E0: 00              BRK                         
A7E1: 00              BRK                         
A7E2: 00              BRK                         
A7E3: 00              BRK                         
A7E4: 00              BRK                         
A7E5: 00              BRK                         
A7E6: 00              BRK                         
A7E7: 00              BRK                         
A7E8: 00              BRK                         
A7E9: 00              BRK                         
A7EA: 00              BRK                         
A7EB: 00              BRK                         
A7EC: 00              BRK                         
A7ED: 00              BRK                         
A7EE: 00              BRK                         
A7EF: 00              BRK                         
A7F0: 00              BRK                         
A7F1: 00              BRK                         
A7F2: 00              BRK                         
A7F3: 00              BRK                         
A7F4: 00              BRK                         
A7F5: 00              BRK                         
A7F6: 00              BRK                         
A7F7: 00              BRK                         
A7F8: 00              BRK                         
A7F9: 00              BRK                         
A7FA: 00              BRK                         
A7FB: 00              BRK                         
A7FC: 00              BRK                         
A7FD: 00              BRK                         
A7FE: 00              BRK                         
A7FF: 00              BRK                         
A800: 60              RTS                         
A801: A9 00           LDA     #$00                
A803: 8D 2F 01        STA     $012F               
A806: 20 0C A8        JSR     $A80C               ; {}
A809: 4C 83 AA        JMP     $AA83               ; {}
A80C: 20 12 A8        JSR     $A812               ; {}
A80F: 4C 83 AA        JMP     $AA83               ; {}
A812: A2 B8           LDX     #$B8                
A814: 20 87 E0        JSR     $E087               
A817: BD 01 07        LDA     $0701,X             
A81A: 29 07           AND     #$07                
A81C: 20 2B EE        JSR     $EE2B               
A81F: 2B ; ????
A820: A8              TAY                         
A821: 4D A8 58        EOR     $58A8               
A824: A8              TAY                         
A825: 86 A8           STX     $A8                 
A827: A1 A8           LDA     ($A8,X)             
A829: B8              CLV                         
A82A: A8              TAY                         
A82B: A9 D0           LDA     #$D0                
A82D: 9D 03 07        STA     $0703,X             
A830: A9 A8           LDA     #$A8                
A832: 9D 00 07        STA     $0700,X             
A835: A9 02           LDA     #$02                
A837: 9D 02 07        STA     $0702,X             
A83A: A9 FF           LDA     #$FF                
A83C: 9D 04 07        STA     $0704,X             
A83F: A9 00           LDA     #$00                
A841: 9D 05 07        STA     $0705,X             
A844: A9 81           LDA     #$81                
A846: 9D 01 07        STA     $0701,X             
A849: A9 C0           LDA     #$C0                
A84B: D0 05           BNE     $A852               ; {}
A84D: FE 01 07        INC     $0701,X             
A850: A9 00           LDA     #$00                
A852: 9D 06 07        STA     $0706,X             
A855: 4C A6 A9        JMP     $A9A6               ; {}
A858: 20 1E A9        JSR     $A91E               ; {}
A85B: 20 90 D9        JSR     $D990               
A85E: 90 0F           BCC     $A86F               ; {}
A860: 20 F7 97        JSR     $97F7               ; {}
A863: 20 09 DA        JSR     $DA09               
A866: 20 DA DB        JSR     $DBDA               
A869: 20 C9 DB        JSR     $DBC9               
A86C: 4C A6 A9        JMP     $A9A6               ; {}
A86F: 20 31 AB        JSR     $AB31               ; {}
A872: A9 F8           LDA     #$F8                
A874: 99 00 07        STA     $0700,Y             
A877: A9 04           LDA     #$04                
A879: 8D 84 03        STA     $0384               
A87C: BD 00 07        LDA     $0700,X             
A87F: 38              SEC                         
A880: E9 10           SBC     #$10                
A882: 9D 00 07        STA     $0700,X             
A885: 60              RTS                         
A886: BD 03 07        LDA     $0703,X             
A889: C9 D0           CMP     #$D0                
A88B: 90 09           BCC     $A896               ; {}
A88D: DE 01 07        DEC     $0701,X             
A890: A9 D0           LDA     #$D0                
A892: 9D 04 07        STA     $0704,X             
A895: 60              RTS                         
A896: A9 40           LDA     #$40                
A898: 9D 04 07        STA     $0704,X             
A89B: 20 2B A9        JSR     $A92B               ; {}
A89E: 4C 5B A8        JMP     $A85B               ; {}
A8A1: AD 74 01        LDA     $0174               
A8A4: F0 03           BEQ     $A8A9               ; {}
A8A6: 4C 86 9A        JMP     $9A86               ; {}
A8A9: A2 B8           LDX     #$B8                
A8AB: FE 01 07        INC     $0701,X             
A8AE: A9 00           LDA     #$00                
A8B0: 9D 06 07        STA     $0706,X             
A8B3: A9 68           LDA     #$68                
A8B5: 4C CD C4        JMP     $C4CD               
A8B8: DE 06 07        DEC     $0706,X             
A8BB: D0 D8           BNE     $A895               ; {}
A8BD: A9 F8           LDA     #$F8                
A8BF: 9D 00 07        STA     $0700,X             
A8C2: 9D 00 02        STA     $0200,X             
A8C5: 9D 08 02        STA     $0208,X             
A8C8: A9 80           LDA     #$80                
A8CA: 9D 06 07        STA     $0706,X             
A8CD: FE 01 07        INC     $0701,X             
A8D0: A9 01           LDA     #$01                
A8D2: 8D 53 01        STA     $0153               
A8D5: 85 20           STA     $20                 
A8D7: A0 29           LDY     #$29                
A8D9: A9 00           LDA     #$00                
A8DB: 85 3A           STA     $3A                 
A8DD: A9 04           LDA     #$04                
A8DF: 4C 90 CA        JMP     $CA90               
A8E2: 20 87 D2        JSR     $D287               
A8E5: D0 0E           BNE     $A8F5               ; {}
A8E7: AD D3 04        LDA     $04D3               
A8EA: C9 40           CMP     #$40                
A8EC: B0 19           BCS     $A907               ; {}
A8EE: AD D4 04        LDA     $04D4               
A8F1: C9 40           CMP     #$40                
A8F3: B0 12           BCS     $A907               ; {}
A8F5: BD 06 07        LDA     $0706,X             
A8F8: C9 78           CMP     #$78                
A8FA: B0 02           BCS     $A8FE               ; {}
A8FC: 69 02           ADC     #$02                
A8FE: 9D 06 07        STA     $0706,X             
A901: 29 F0           AND     #$F0                
A903: 9D 05 07        STA     $0705,X             
A906: 60              RTS                         
A907: A9 00           LDA     #$00                
A909: 9D 06 07        STA     $0706,X             
A90C: 9D 05 07        STA     $0705,X             
A90F: 60              RTS                         
A910: BD 06 07        LDA     $0706,X             
A913: 18              CLC                         
A914: 69 02           ADC     #$02                
A916: C9 F8           CMP     #$F8                
A918: 90 E4           BCC     $A8FE               ; {}
A91A: A9 08           LDA     #$08                
A91C: D0 50           BNE     $A96E               ; {}
A91E: BD 06 07        LDA     $0706,X             
A921: 30 ED           BMI     $A910               ; {}
A923: D0 BD           BNE     $A8E2               ; {}
A925: 20 35 A9        JSR     $A935               ; {}
A928: 4C 72 A9        JMP     $A972               ; {}
A92B: BD 06 07        LDA     $0706,X             
A92E: 30 E0           BMI     $A910               ; {}
A930: D0 B0           BNE     $A8E2               ; {}
A932: 4C 72 A9        JMP     $A972               ; {}
A935: BD 03 07        LDA     $0703,X             
A938: C9 D8           CMP     #$D8                
A93A: B0 21           BCS     $A95D               ; {}
A93C: CD 23 07        CMP     $0723               
A93F: F0 18           BEQ     $A959               ; {}
A941: B0 04           BCS     $A947               ; {}
A943: A0 20           LDY     #$20                
A945: D0 09           BNE     $A950               ; {}
A947: BD 03 07        LDA     $0703,X             
A94A: C9 20           CMP     #$20                
A94C: 90 0B           BCC     $A959               ; {}
A94E: A0 D0           LDY     #$D0                
A950: A5 14           LDA     $14                 
A952: D0 04           BNE     $A958               ; {}
A954: 98              TYA                         
A955: 9D 04 07        STA     $0704,X             
A958: 60              RTS                         
A959: FE 01 07        INC     $0701,X             
A95C: 60              RTS                         
A95D: BD 01 07        LDA     $0701,X             
A960: 29 F8           AND     #$F8                
A962: 09 01           ORA     #$01                
A964: 9D 01 07        STA     $0701,X             
A967: A9 D0           LDA     #$D0                
A969: 9D 03 07        STA     $0703,X             
A96C: A9 40           LDA     #$40                
A96E: 9D 06 07        STA     $0706,X             
A971: 60              RTS                         
A972: BD 00 07        LDA     $0700,X             
A975: C9 A0           CMP     #$A0                
A977: B0 1A           BCS     $A993               ; {}
A979: CD 20 07        CMP     $0720               
A97C: B0 04           BCS     $A982               ; {}
A97E: A9 01           LDA     #$01                
A980: D0 EC           BNE     $A96E               ; {}
A982: 8A              TXA                         
A983: 18              CLC                         
A984: 65 14           ADC     $14                 
A986: 29 3F           AND     #$3F                
A988: D0 E7           BNE     $A971               ; {}
A98A: A5 26           LDA     $26                 
A98C: 29 3F           AND     #$3F                
A98E: 18              CLC                         
A98F: 69 A0           ADC     #$A0                
A991: D0 DB           BNE     $A96E               ; {}
A993: A5 14           LDA     $14                 
A995: 29 7F           AND     #$7F                
A997: D0 D8           BNE     $A971               ; {}
A999: 24 26           BIT     $26                 
A99B: 70 D4           BVS     $A971               ; {}
A99D: A9 80           LDA     #$80                
A99F: D0 CD           BNE     $A96E               ; {}
A9A1: A9 10           LDA     #$10                
A9A3: 4C B9 A9        JMP     $A9B9               ; {}
A9A6: A9 D3           LDA     #$D3                
A9A8: 85 08           STA     $08                 
A9AA: A9 A9           LDA     #$A9                
A9AC: 85 09           STA     $09                 
A9AE: BD 01 07        LDA     $0701,X             
A9B1: 29 07           AND     #$07                
A9B3: C9 03           CMP     #$03                
A9B5: F0 EA           BEQ     $A9A1               ; {}
A9B7: A9 20           LDA     #$20                
A9B9: A0 00           LDY     #$00                
A9BB: 25 14           AND     $14                 
A9BD: D0 02           BNE     $A9C1               ; {}
A9BF: A0 58           LDY     #$58                
A9C1: BD 04 07        LDA     $0704,X             
A9C4: 30 05           BMI     $A9CB               ; {}
A9C6: 98              TYA                         
A9C7: 18              CLC                         
A9C8: 69 2C           ADC     #$2C                
A9CA: A8              TAY                         
A9CB: A9 0A           LDA     #$0A                
A9CD: 85 00           STA     $00                 ; {ram.GP_00}
A9CF: 98              TYA                         
A9D0: 4C AB 9B        JMP     $9BAB               ; {}
A9D3: F0 F0           BEQ     $A9C5               ; {}
A9D5: 03 ; ????
A9D6: F8              SED                         
A9D7: F0 F1           BEQ     $A9CA               ; {}
A9D9: 03 ; ????
A9DA: 00              BRK                         
A9DB: F0 F2           BEQ     $A9CF               ; {}
A9DD: 03 ; ????
A9DE: 08              PHP                         
A9DF: F8              SED                         
A9E0: F3 ; ????
A9E1: 03 ; ????
A9E2: F8              SED                         
A9E3: F8              SED                         
A9E4: E2 ; ????
A9E5: 03 ; ????
A9E6: 00              BRK                         
A9E7: F8              SED                         
A9E8: DE 03 08        DEC     $0803,X             
A9EB: F8              SED                         
A9EC: DF ; ????
A9ED: 03 ; ????
A9EE: 10 00           BPL     $A9F0               ; {}
A9F0: D8              CLD                         
A9F1: 03 ; ????
A9F2: 00              BRK                         
A9F3: 00              BRK                         
A9F4: D9 03 08        CMP     $0803,Y             
A9F7: 00              BRK                         
A9F8: DA ; ????
A9F9: 03 ; ????
A9FA: 10 00           BPL     $A9FC               ; {}
A9FC: CE 03 18        DEC     $1803               
A9FF: F0 F2           BEQ     $A9F3               ; {}
AA01: 43 ; ????
AA02: F8              SED                         
AA03: F0 F1           BEQ     $A9F6               ; {}
AA05: 43 ; ????
AA06: 00              BRK                         
AA07: F0 F0           BEQ     $A9F9               ; {}
AA09: 43 ; ????
AA0A: 08              PHP                         
AA0B: F8              SED                         
AA0C: DF ; ????
AA0D: 43 ; ????
AA0E: F0 F8           BEQ     $AA08               ; {}
AA10: DE 43 F8        DEC     $F843,X             
AA13: F8              SED                         
AA14: E2 ; ????
AA15: 43 ; ????
AA16: 00              BRK                         
AA17: F8              SED                         
AA18: F3 ; ????
AA19: 43 ; ????
AA1A: 08              PHP                         
AA1B: 00              BRK                         
AA1C: CE 43 E8        DEC     $E843               
AA1F: 00              BRK                         
AA20: DA ; ????
AA21: 43 ; ????
AA22: F0 00           BEQ     $AA24               ; {}
AA24: D9 43 F8        CMP     $F843,Y             
AA27: 00              BRK                         
AA28: D8              CLD                         
AA29: 43 ; ????
AA2A: 00              BRK                         
AA2B: F0 F3           BEQ     $AA20               ; {}
AA2D: 03 ; ????
AA2E: F8              SED                         
AA2F: F0 E2           BEQ     $AA13               ; {}
AA31: 03 ; ????
AA32: 00              BRK                         
AA33: F0 F2           BEQ     $AA27               ; {}
AA35: 03 ; ????
AA36: 08              PHP                         
AA37: F8              SED                         
AA38: F0 03           BEQ     $AA3D               ; {}
AA3A: F8              SED                         
AA3B: F8              SED                         
AA3C: F1 03           SBC     ($03),Y             
AA3E: 00              BRK                         
AA3F: F8              SED                         
AA40: DE 03 08        DEC     $0803,X             
AA43: F8              SED                         
AA44: EF ; ????
AA45: 03 ; ????
AA46: 10 00           BPL     $AA48               ; {}
AA48: DB ; ????
AA49: 03 ; ????
AA4A: 00              BRK                         
AA4B: 00              BRK                         
AA4C: CC 03 08        CPY     $0803               
AA4F: 00              BRK                         
AA50: CD 03 10        CMP     $1003               
AA53: 00              BRK                         
AA54: CF ; ????
AA55: 03 ; ????
AA56: 18              CLC                         
AA57: F0 F2           BEQ     $AA4B               ; {}
AA59: 43 ; ????
AA5A: F8              SED                         
AA5B: F0 E2           BEQ     $AA3F               ; {}
AA5D: 43 ; ????
AA5E: 00              BRK                         
AA5F: F0 F3           BEQ     $AA54               ; {}
AA61: 43 ; ????
AA62: 08              PHP                         
AA63: F8              SED                         
AA64: EF ; ????
AA65: 43 ; ????
AA66: F0 F8           BEQ     $AA60               ; {}
AA68: DE 43 F8        DEC     $F843,X             
AA6B: F8              SED                         
AA6C: F1 43           SBC     ($43),Y             
AA6E: 00              BRK                         
AA6F: F8              SED                         
AA70: F0 43           BEQ     $AAB5               ; {}
AA72: 08              PHP                         
AA73: 00              BRK                         
AA74: CF ; ????
AA75: 43 ; ????
AA76: E8              INX                         
AA77: 00              BRK                         
AA78: CD 43 F0        CMP     $F043               
AA7B: 00              BRK                         
AA7C: CC 43 F8        CPY     $F843               
AA7F: 00              BRK                         
AA80: DB ; ????
AA81: 43 ; ????
AA82: 00              BRK                         
AA83: A2 A0           LDX     #$A0                
AA85: A9 A0           LDA     #$A0                
AA87: 20 95 AA        JSR     $AA95               ; {}
AA8A: A2 A8           LDX     #$A8                
AA8C: A9 B0           LDA     #$B0                
AA8E: 20 95 AA        JSR     $AA95               ; {}
AA91: A2 B0           LDX     #$B0                
AA93: A9 00           LDA     #$00                
AA95: 85 07           STA     $07                 
AA97: 20 F7 97        JSR     $97F7               ; {}
AA9A: 90 71           BCC     $AB0D               ; {}
AA9C: 20 87 E0        JSR     $E087               
AA9F: BD 01 07        LDA     $0701,X             
AAA2: 29 07           AND     #$07                
AAA4: 20 2B EE        JSR     $EE2B               
AAA7: AB ; ????
AAA8: AA              TAX                         
AAA9: EC AA 8A        CPX     $8AAA               ; {}
AAAC: 18              CLC                         
AAAD: 65 14           ADC     $14                 
AAAF: D0 3A           BNE     $AAEB               ; {}
AAB1: AD B9 07        LDA     $07B9               
AAB4: 29 0F           AND     #$0F                
AAB6: C9 04           CMP     #$04                
AAB8: B0 31           BCS     $AAEB               ; {}
AABA: AD B8 07        LDA     $07B8               
AABD: E9 03           SBC     #$03                
AABF: 24 26           BIT     $26                 
AAC1: 70 03           BVS     $AAC6               ; {}
AAC3: 38              SEC                         
AAC4: E9 08           SBC     #$08                
AAC6: 9D 00 07        STA     $0700,X             
AAC9: AD BB 07        LDA     $07BB               
AACC: 9D 03 07        STA     $0703,X             
AACF: A0 A0           LDY     #$A0                
AAD1: AD BC 07        LDA     $07BC               
AAD4: 30 02           BMI     $AAD8               ; {}
AAD6: A0 50           LDY     #$50                
AAD8: 98              TYA                         
AAD9: 9D 04 07        STA     $0704,X             
AADC: A5 07           LDA     $07                 
AADE: 9D 05 07        STA     $0705,X             
AAE1: A9 09           LDA     #$09                
AAE3: 9D 01 07        STA     $0701,X             
AAE6: A9 04           LDA     #$04                
AAE8: 8D 84 03        STA     $0384               
AAEB: 60              RTS                         
AAEC: BD 00 07        LDA     $0700,X             
AAEF: C9 F0           CMP     #$F0                
AAF1: B0 1A           BCS     $AB0D               ; {}
AAF3: BD 03 07        LDA     $0703,X             
AAF6: C9 F8           CMP     #$F8                
AAF8: B0 13           BCS     $AB0D               ; {}
AAFA: 20 F7 97        JSR     $97F7               ; {}
AAFD: 20 09 DA        JSR     $DA09               
AB00: F0 0B           BEQ     $AB0D               ; {}
AB02: 90 09           BCC     $AB0D               ; {}
AB04: 20 DA DB        JSR     $DBDA               
AB07: 20 C9 DB        JSR     $DBC9               
AB0A: 4C 10 AB        JMP     $AB10               ; {}
AB0D: 4C 2F DF        JMP     $DF2F               
AB10: BD 00 07        LDA     $0700,X             
AB13: 9D 00 02        STA     $0200,X             
AB16: BD 03 07        LDA     $0703,X             
AB19: 9D 03 02        STA     $0203,X             
AB1C: A9 01           LDA     #$01                
AB1E: 9D 02 02        STA     $0202,X             
AB21: A5 14           LDA     $14                 
AB23: 29 04           AND     #$04                
AB25: D0 04           BNE     $AB2B               ; {}
AB27: A9 3B           LDA     #$3B                
AB29: D0 02           BNE     $AB2D               ; {}
AB2B: A9 3A           LDA     #$3A                
AB2D: 9D 01 02        STA     $0201,X             
AB30: 60              RTS                         
AB31: A5 3C           LDA     $3C                 
AB33: D0 08           BNE     $AB3D               ; {}
AB35: C0 38           CPY     #$38                
AB37: F0 08           BEQ     $AB41               ; {}
AB39: C0 3C           CPY     #$3C                
AB3B: F0 04           BEQ     $AB41               ; {}
AB3D: A9 05           LDA     #$05                
AB3F: D0 06           BNE     $AB47               ; {}
AB41: 18              CLC                         
AB42: AD 52 01        LDA     $0152               
AB45: 69 01           ADC     #$01                
AB47: 85 00           STA     $00                 ; {ram.GP_00}
AB49: A5 6B           LDA     $6B                 
AB4B: 38              SEC                         
AB4C: E5 00           SBC     $00                 ; {ram.GP_00}
AB4E: 90 05           BCC     $AB55               ; {}
AB50: F0 03           BEQ     $AB55               ; {}
AB52: 85 6B           STA     $6B                 
AB54: 60              RTS                         
AB55: AD B9 07        LDA     $07B9               
AB58: 29 F0           AND     #$F0                
AB5A: 09 04           ORA     #$04                
AB5C: 8D B9 07        STA     $07B9               
AB5F: A9 00           LDA     #$00                
AB61: 85 6B           STA     $6B                 
AB63: A9 80           LDA     #$80                
AB65: 20 E1 E2        JSR     $E2E1               
AB68: 20 F0 E2        JSR     $E2F0               
AB6B: A9 3B           LDA     #$3B                
AB6D: 8D 75 01        STA     $0175               
AB70: A9 01           LDA     #$01                
AB72: 8D 76 01        STA     $0176               
AB75: A9 05           LDA     #$05                
AB77: 8D 74 01        STA     $0174               
AB7A: A9 0B           LDA     #$0B                
AB7C: 4C 34 9A        JMP     $9A34               ; {}
AB7F: 00              BRK                         
AB80: 00              BRK                         
AB81: 00              BRK                         
AB82: 00              BRK                         
AB83: 00              BRK                         
AB84: 00              BRK                         
AB85: 00              BRK                         
AB86: 00              BRK                         
AB87: 00              BRK                         
AB88: 00              BRK                         
AB89: 00              BRK                         
AB8A: 00              BRK                         
AB8B: 00              BRK                         
AB8C: 00              BRK                         
AB8D: 00              BRK                         
AB8E: 00              BRK                         
AB8F: 00              BRK                         
AB90: 00              BRK                         
AB91: 00              BRK                         
AB92: 00              BRK                         
AB93: 00              BRK                         
AB94: 00              BRK                         
AB95: 00              BRK                         
AB96: 00              BRK                         
AB97: 00              BRK                         
AB98: 00              BRK                         
AB99: 00              BRK                         
AB9A: 00              BRK                         
AB9B: 00              BRK                         
AB9C: 00              BRK                         
AB9D: 00              BRK                         
AB9E: 00              BRK                         
AB9F: 00              BRK                         
ABA0: 00              BRK                         
ABA1: 00              BRK                         
ABA2: 00              BRK                         
ABA3: 00              BRK                         
ABA4: 00              BRK                         
ABA5: 00              BRK                         
ABA6: 00              BRK                         
ABA7: 00              BRK                         
ABA8: 00              BRK                         
ABA9: 00              BRK                         
ABAA: 00              BRK                         
ABAB: 00              BRK                         
ABAC: 00              BRK                         
ABAD: 00              BRK                         
ABAE: 00              BRK                         
ABAF: 00              BRK                         
ABB0: 00              BRK                         
ABB1: 00              BRK                         
ABB2: 00              BRK                         
ABB3: 00              BRK                         
ABB4: 00              BRK                         
ABB5: 00              BRK                         
ABB6: 00              BRK                         
ABB7: 00              BRK                         
ABB8: 00              BRK                         
ABB9: 00              BRK                         
ABBA: 00              BRK                         
ABBB: 00              BRK                         
ABBC: 00              BRK                         
ABBD: 00              BRK                         
ABBE: 00              BRK                         
ABBF: 00              BRK                         
ABC0: 00              BRK                         
ABC1: 00              BRK                         
ABC2: 00              BRK                         
ABC3: 00              BRK                         
ABC4: 00              BRK                         
ABC5: 00              BRK                         
ABC6: 00              BRK                         
ABC7: 00              BRK                         
ABC8: 00              BRK                         
ABC9: 00              BRK                         
ABCA: 00              BRK                         
ABCB: 00              BRK                         
ABCC: 00              BRK                         
ABCD: 00              BRK                         
ABCE: 00              BRK                         
ABCF: 00              BRK                         
ABD0: 00              BRK                         
ABD1: 00              BRK                         
ABD2: 00              BRK                         
ABD3: 00              BRK                         
ABD4: 00              BRK                         
ABD5: 00              BRK                         
ABD6: 00              BRK                         
ABD7: 00              BRK                         
ABD8: 00              BRK                         
ABD9: 00              BRK                         
ABDA: 00              BRK                         
ABDB: 00              BRK                         
ABDC: 00              BRK                         
ABDD: 00              BRK                         
ABDE: 00              BRK                         
ABDF: 00              BRK                         
ABE0: 00              BRK                         
ABE1: 00              BRK                         
ABE2: 00              BRK                         
ABE3: 00              BRK                         
ABE4: 00              BRK                         
ABE5: 00              BRK                         
ABE6: 00              BRK                         
ABE7: 00              BRK                         
ABE8: 00              BRK                         
ABE9: 00              BRK                         
ABEA: 00              BRK                         
ABEB: 00              BRK                         
ABEC: 00              BRK                         
ABED: 00              BRK                         
ABEE: 00              BRK                         
ABEF: 00              BRK                         
ABF0: 00              BRK                         
ABF1: 00              BRK                         
ABF2: 00              BRK                         
ABF3: 00              BRK                         
ABF4: 00              BRK                         
ABF5: 00              BRK                         
ABF6: 00              BRK                         
ABF7: 00              BRK                         
ABF8: 00              BRK                         
ABF9: 00              BRK                         
ABFA: 00              BRK                         
ABFB: 00              BRK                         
ABFC: 00              BRK                         
ABFD: 00              BRK                         
ABFE: 00              BRK                         
ABFF: 00              BRK                         
AC00: FF ; ????
AC01: FF ; ????
AC02: FF ; ????
AC03: FF ; ????
AC04: FF ; ????
AC05: FF ; ????
AC06: FF ; ????
AC07: FF ; ????
AC08: FF ; ????
AC09: FF ; ????
AC0A: FF ; ????
AC0B: FF ; ????
AC0C: FF ; ????
AC0D: FF ; ????
AC0E: FF ; ????
AC0F: FF ; ????
AC10: FF ; ????
AC11: FF ; ????
AC12: FF ; ????
AC13: FF ; ????
AC14: FF ; ????
AC15: FF ; ????
AC16: FF ; ????
AC17: FF ; ????
AC18: FF ; ????
AC19: FF ; ????
AC1A: FF ; ????
AC1B: FF ; ????
AC1C: FF ; ????
AC1D: FF ; ????
AC1E: FF ; ????
AC1F: FF ; ????
AC20: FF ; ????
AC21: FF ; ????
AC22: FF ; ????
AC23: FF ; ????
AC24: FF ; ????
AC25: FF ; ????
AC26: FF ; ????
AC27: FF ; ????
AC28: FF ; ????
AC29: FF ; ????
AC2A: FF ; ????
AC2B: FF ; ????
AC2C: FF ; ????
AC2D: FF ; ????
AC2E: FF ; ????
AC2F: FF ; ????
AC30: FF ; ????
AC31: FF ; ????
AC32: FF ; ????
AC33: FF ; ????
AC34: FF ; ????
AC35: FF ; ????
AC36: FF ; ????
AC37: FF ; ????
AC38: FF ; ????
AC39: FF ; ????
AC3A: FF ; ????
AC3B: FF ; ????
AC3C: FF ; ????
AC3D: FF ; ????
AC3E: FF ; ????
AC3F: FF ; ????
AC40: FF ; ????
AC41: FF ; ????
AC42: FF ; ????
AC43: FF ; ????
AC44: FF ; ????
AC45: FF ; ????
AC46: FF ; ????
AC47: FF ; ????
AC48: FF ; ????
AC49: FF ; ????
AC4A: FF ; ????
AC4B: FF ; ????
AC4C: FF ; ????
AC4D: FF ; ????
AC4E: FF ; ????
AC4F: FF ; ????
AC50: FF ; ????
AC51: FF ; ????
AC52: FF ; ????
AC53: FF ; ????
AC54: FF ; ????
AC55: FF ; ????
AC56: FF ; ????
AC57: FF ; ????
AC58: FF ; ????
AC59: FF ; ????
AC5A: FF ; ????
AC5B: FF ; ????
AC5C: FF ; ????
AC5D: FF ; ????
AC5E: FF ; ????
AC5F: FF ; ????
AC60: FF ; ????
AC61: FF ; ????
AC62: FF ; ????
AC63: FF ; ????
AC64: FF ; ????
AC65: FF ; ????
AC66: FF ; ????
AC67: FF ; ????
AC68: FF ; ????
AC69: FF ; ????
AC6A: FF ; ????
AC6B: FF ; ????
AC6C: FF ; ????
AC6D: FF ; ????
AC6E: FF ; ????
AC6F: FF ; ????
AC70: FF ; ????
AC71: FF ; ????
AC72: FF ; ????
AC73: FF ; ????
AC74: FF ; ????
AC75: FF ; ????
AC76: FF ; ????
AC77: FF ; ????
AC78: FF ; ????
AC79: FF ; ????
AC7A: FF ; ????
AC7B: FF ; ????
AC7C: FF ; ????
AC7D: FF ; ????
AC7E: FF ; ????
AC7F: FF ; ????
AC80: FF ; ????
AC81: FF ; ????
AC82: FF ; ????
AC83: FF ; ????
AC84: FF ; ????
AC85: FF ; ????
AC86: FF ; ????
AC87: FF ; ????
AC88: FF ; ????
AC89: FF ; ????
AC8A: FF ; ????
AC8B: FF ; ????
AC8C: FF ; ????
AC8D: FF ; ????
AC8E: FF ; ????
AC8F: FF ; ????
AC90: FF ; ????
AC91: FF ; ????
AC92: FF ; ????
AC93: FF ; ????
AC94: FF ; ????
AC95: FF ; ????
AC96: FF ; ????
AC97: FF ; ????
AC98: FF ; ????
AC99: FF ; ????
AC9A: FF ; ????
AC9B: FF ; ????
AC9C: FF ; ????
AC9D: FF ; ????
AC9E: FF ; ????
AC9F: FF ; ????
ACA0: FF ; ????
ACA1: FF ; ????
ACA2: FF ; ????
ACA3: FF ; ????
ACA4: FF ; ????
ACA5: FF ; ????
ACA6: FF ; ????
ACA7: FF ; ????
ACA8: FF ; ????
ACA9: FF ; ????
ACAA: FF ; ????
ACAB: FF ; ????
ACAC: FF ; ????
ACAD: FF ; ????
ACAE: FF ; ????
ACAF: FF ; ????
ACB0: FF ; ????
ACB1: FF ; ????
ACB2: FF ; ????
ACB3: FF ; ????
ACB4: FF ; ????
ACB5: FF ; ????
ACB6: FF ; ????
ACB7: FF ; ????
ACB8: FF ; ????
ACB9: FF ; ????
ACBA: FF ; ????
ACBB: FF ; ????
ACBC: FF ; ????
ACBD: FF ; ????
ACBE: FF ; ????
ACBF: FF ; ????
ACC0: FF ; ????
ACC1: FF ; ????
ACC2: FF ; ????
ACC3: FF ; ????
ACC4: FF ; ????
ACC5: FF ; ????
ACC6: FF ; ????
ACC7: FF ; ????
ACC8: FF ; ????
ACC9: FF ; ????
ACCA: FF ; ????
ACCB: FF ; ????
ACCC: FF ; ????
ACCD: FF ; ????
ACCE: FF ; ????
ACCF: FF ; ????
ACD0: FF ; ????
ACD1: FF ; ????
ACD2: FF ; ????
ACD3: FF ; ????
ACD4: FF ; ????
ACD5: FF ; ????
ACD6: FF ; ????
ACD7: FF ; ????
ACD8: FF ; ????
ACD9: FF ; ????
ACDA: FF ; ????
ACDB: FF ; ????
ACDC: FF ; ????
ACDD: FF ; ????
ACDE: FF ; ????
ACDF: FF ; ????
ACE0: FF ; ????
ACE1: FF ; ????
ACE2: FF ; ????
ACE3: FF ; ????
ACE4: 7F ; ????
ACE5: FF ; ????
ACE6: FF ; ????
ACE7: FF ; ????
ACE8: FF ; ????
ACE9: FF ; ????
ACEA: FF ; ????
ACEB: FF ; ????
ACEC: FF ; ????
ACED: FF ; ????
ACEE: FF ; ????
ACEF: FF ; ????
ACF0: FF ; ????
ACF1: FF ; ????
ACF2: FF ; ????
ACF3: FF ; ????
ACF4: FF ; ????
ACF5: EF ; ????
ACF6: FF ; ????
ACF7: FF ; ????
ACF8: FF ; ????
ACF9: FF ; ????
ACFA: FF ; ????
ACFB: FF ; ????
ACFC: FF ; ????
ACFD: FF ; ????
ACFE: FF ; ????
ACFF: FF ; ????
AD00: 00              BRK                         
AD01: 00              BRK                         
AD02: 00              BRK                         
AD03: 00              BRK                         
AD04: 00              BRK                         
AD05: 00              BRK                         
AD06: 00              BRK                         
AD07: 00              BRK                         
AD08: 00              BRK                         
AD09: 00              BRK                         
AD0A: 00              BRK                         
AD0B: 00              BRK                         
AD0C: 00              BRK                         
AD0D: 00              BRK                         
AD0E: 00              BRK                         
AD0F: 00              BRK                         
AD10: 00              BRK                         
AD11: 00              BRK                         
AD12: 00              BRK                         
AD13: 00              BRK                         
AD14: 00              BRK                         
AD15: 00              BRK                         
AD16: 00              BRK                         
AD17: 00              BRK                         
AD18: 00              BRK                         
AD19: 00              BRK                         
AD1A: 00              BRK                         
AD1B: 00              BRK                         
AD1C: 00              BRK                         
AD1D: 00              BRK                         
AD1E: 00              BRK                         
AD1F: 00              BRK                         
AD20: 00              BRK                         
AD21: 00              BRK                         
AD22: 00              BRK                         
AD23: 00              BRK                         
AD24: 00              BRK                         
AD25: 00              BRK                         
AD26: 00              BRK                         
AD27: 00              BRK                         
AD28: 00              BRK                         
AD29: 00              BRK                         
AD2A: 00              BRK                         
AD2B: 00              BRK                         
AD2C: 00              BRK                         
AD2D: 00              BRK                         
AD2E: 00              BRK                         
AD2F: 00              BRK                         
AD30: 00              BRK                         
AD31: 00              BRK                         
AD32: 00              BRK                         
AD33: 00              BRK                         
AD34: 00              BRK                         
AD35: 00              BRK                         
AD36: 00              BRK                         
AD37: 00              BRK                         
AD38: 00              BRK                         
AD39: 00              BRK                         
AD3A: 00              BRK                         
AD3B: 00              BRK                         
AD3C: 00              BRK                         
AD3D: 00              BRK                         
AD3E: 00              BRK                         
AD3F: 00              BRK                         
AD40: 00              BRK                         
AD41: 00              BRK                         
AD42: 00              BRK                         
AD43: 00              BRK                         
AD44: 00              BRK                         
AD45: 00              BRK                         
AD46: 00              BRK                         
AD47: 00              BRK                         
AD48: 00              BRK                         
AD49: 00              BRK                         
AD4A: 00              BRK                         
AD4B: 00              BRK                         
AD4C: 00              BRK                         
AD4D: 00              BRK                         
AD4E: 00              BRK                         
AD4F: 00              BRK                         
AD50: 00              BRK                         
AD51: 00              BRK                         
AD52: 00              BRK                         
AD53: 00              BRK                         
AD54: 00              BRK                         
AD55: 00              BRK                         
AD56: 00              BRK                         
AD57: 00              BRK                         
AD58: 00              BRK                         
AD59: 00              BRK                         
AD5A: 00              BRK                         
AD5B: 00              BRK                         
AD5C: 00              BRK                         
AD5D: 00              BRK                         
AD5E: 00              BRK                         
AD5F: 00              BRK                         
AD60: 00              BRK                         
AD61: 00              BRK                         
AD62: 00              BRK                         
AD63: 00              BRK                         
AD64: 00              BRK                         
AD65: 00              BRK                         
AD66: 00              BRK                         
AD67: 00              BRK                         
AD68: 00              BRK                         
AD69: 00              BRK                         
AD6A: 00              BRK                         
AD6B: 00              BRK                         
AD6C: 00              BRK                         
AD6D: 00              BRK                         
AD6E: 00              BRK                         
AD6F: 00              BRK                         
AD70: 00              BRK                         
AD71: 00              BRK                         
AD72: 00              BRK                         
AD73: 00              BRK                         
AD74: 00              BRK                         
AD75: 00              BRK                         
AD76: 00              BRK                         
AD77: 00              BRK                         
AD78: 00              BRK                         
AD79: 00              BRK                         
AD7A: 00              BRK                         
AD7B: 00              BRK                         
AD7C: 00              BRK                         
AD7D: 00              BRK                         
AD7E: 00              BRK                         
AD7F: 00              BRK                         
AD80: 00              BRK                         
AD81: 00              BRK                         
AD82: 00              BRK                         
AD83: 00              BRK                         
AD84: 00              BRK                         
AD85: 00              BRK                         
AD86: 00              BRK                         
AD87: 00              BRK                         
AD88: 00              BRK                         
AD89: 00              BRK                         
AD8A: 00              BRK                         
AD8B: 00              BRK                         
AD8C: 00              BRK                         
AD8D: 00              BRK                         
AD8E: 00              BRK                         
AD8F: 00              BRK                         
AD90: 00              BRK                         
AD91: 00              BRK                         
AD92: 00              BRK                         
AD93: 00              BRK                         
AD94: 00              BRK                         
AD95: 00              BRK                         
AD96: 00              BRK                         
AD97: 00              BRK                         
AD98: 00              BRK                         
AD99: 00              BRK                         
AD9A: 00              BRK                         
AD9B: 00              BRK                         
AD9C: 00              BRK                         
AD9D: 00              BRK                         
AD9E: 00              BRK                         
AD9F: 00              BRK                         
ADA0: 00              BRK                         
ADA1: 00              BRK                         
ADA2: 00              BRK                         
ADA3: 00              BRK                         
ADA4: 00              BRK                         
ADA5: 00              BRK                         
ADA6: 00              BRK                         
ADA7: 00              BRK                         
ADA8: 00              BRK                         
ADA9: 00              BRK                         
ADAA: 00              BRK                         
ADAB: 00              BRK                         
ADAC: 00              BRK                         
ADAD: 00              BRK                         
ADAE: 00              BRK                         
ADAF: 00              BRK                         
ADB0: 00              BRK                         
ADB1: 00              BRK                         
ADB2: 00              BRK                         
ADB3: 00              BRK                         
ADB4: 00              BRK                         
ADB5: 00              BRK                         
ADB6: 00              BRK                         
ADB7: 00              BRK                         
ADB8: 00              BRK                         
ADB9: 00              BRK                         
ADBA: 00              BRK                         
ADBB: 00              BRK                         
ADBC: 00              BRK                         
ADBD: 00              BRK                         
ADBE: 00              BRK                         
ADBF: 00              BRK                         
ADC0: 00              BRK                         
ADC1: 00              BRK                         
ADC2: 00              BRK                         
ADC3: 00              BRK                         
ADC4: 00              BRK                         
ADC5: 00              BRK                         
ADC6: 00              BRK                         
ADC7: 00              BRK                         
ADC8: 00              BRK                         
ADC9: 00              BRK                         
ADCA: 00              BRK                         
ADCB: 00              BRK                         
ADCC: 00              BRK                         
ADCD: 00              BRK                         
ADCE: 00              BRK                         
ADCF: 00              BRK                         
ADD0: 00              BRK                         
ADD1: 00              BRK                         
ADD2: 00              BRK                         
ADD3: 00              BRK                         
ADD4: 00              BRK                         
ADD5: 00              BRK                         
ADD6: 00              BRK                         
ADD7: 00              BRK                         
ADD8: 00              BRK                         
ADD9: 00              BRK                         
ADDA: 00              BRK                         
ADDB: 00              BRK                         
ADDC: 00              BRK                         
ADDD: 00              BRK                         
ADDE: 00              BRK                         
ADDF: 00              BRK                         
ADE0: 00              BRK                         
ADE1: 00              BRK                         
ADE2: 00              BRK                         
ADE3: 00              BRK                         
ADE4: 00              BRK                         
ADE5: 00              BRK                         
ADE6: 00              BRK                         
ADE7: 00              BRK                         
ADE8: 00              BRK                         
ADE9: 00              BRK                         
ADEA: 00              BRK                         
ADEB: 00              BRK                         
ADEC: 00              BRK                         
ADED: 00              BRK                         
ADEE: 00              BRK                         
ADEF: 00              BRK                         
ADF0: 00              BRK                         
ADF1: 00              BRK                         
ADF2: 00              BRK                         
ADF3: 00              BRK                         
ADF4: 00              BRK                         
ADF5: 00              BRK                         
ADF6: 00              BRK                         
ADF7: 00              BRK                         
ADF8: 00              BRK                         
ADF9: 00              BRK                         
ADFA: 00              BRK                         
ADFB: 00              BRK                         
ADFC: 00              BRK                         
ADFD: 00              BRK                         
ADFE: 00              BRK                         
ADFF: 00              BRK                         
AE00: FF ; ????
AE01: FF ; ????
AE02: FF ; ????
AE03: FF ; ????
AE04: FF ; ????
AE05: FF ; ????
AE06: FF ; ????
AE07: FF ; ????
AE08: FF ; ????
AE09: FF ; ????
AE0A: FF ; ????
AE0B: FF ; ????
AE0C: FF ; ????
AE0D: FF ; ????
AE0E: FF ; ????
AE0F: FF ; ????
AE10: FF ; ????
AE11: FF ; ????
AE12: FF ; ????
AE13: FF ; ????
AE14: FF ; ????
AE15: FF ; ????
AE16: FF ; ????
AE17: FF ; ????
AE18: FF ; ????
AE19: FF ; ????
AE1A: FF ; ????
AE1B: FF ; ????
AE1C: FF ; ????
AE1D: FF ; ????
AE1E: FF ; ????
AE1F: FF ; ????
AE20: FF ; ????
AE21: FF ; ????
AE22: FF ; ????
AE23: FF ; ????
AE24: FF ; ????
AE25: FF ; ????
AE26: FF ; ????
AE27: FF ; ????
AE28: FF ; ????
AE29: FF ; ????
AE2A: FF ; ????
AE2B: FF ; ????
AE2C: FF ; ????
AE2D: FF ; ????
AE2E: FF ; ????
AE2F: FF ; ????
AE30: FF ; ????
AE31: FF ; ????
AE32: FF ; ????
AE33: FF ; ????
AE34: FF ; ????
AE35: FF ; ????
AE36: FF ; ????
AE37: FF ; ????
AE38: FF ; ????
AE39: FF ; ????
AE3A: FF ; ????
AE3B: FF ; ????
AE3C: FF ; ????
AE3D: FF ; ????
AE3E: FF ; ????
AE3F: FF ; ????
AE40: FF ; ????
AE41: FF ; ????
AE42: FF ; ????
AE43: FF ; ????
AE44: FF ; ????
AE45: FF ; ????
AE46: FF ; ????
AE47: FF ; ????
AE48: FF ; ????
AE49: FF ; ????
AE4A: FF ; ????
AE4B: FF ; ????
AE4C: FF ; ????
AE4D: FF ; ????
AE4E: FF ; ????
AE4F: FF ; ????
AE50: FF ; ????
AE51: FF ; ????
AE52: FF ; ????
AE53: FF ; ????
AE54: FF ; ????
AE55: FF ; ????
AE56: FF ; ????
AE57: FF ; ????
AE58: FF ; ????
AE59: FF ; ????
AE5A: FF ; ????
AE5B: FF ; ????
AE5C: FF ; ????
AE5D: FF ; ????
AE5E: FF ; ????
AE5F: FF ; ????
AE60: FF ; ????
AE61: FF ; ????
AE62: FF ; ????
AE63: FF ; ????
AE64: FF ; ????
AE65: FF ; ????
AE66: FF ; ????
AE67: FF ; ????
AE68: FF ; ????
AE69: FF ; ????
AE6A: FF ; ????
AE6B: FF ; ????
AE6C: FF ; ????
AE6D: FF ; ????
AE6E: FF ; ????
AE6F: FF ; ????
AE70: FF ; ????
AE71: FF ; ????
AE72: FF ; ????
AE73: FF ; ????
AE74: FF ; ????
AE75: FF ; ????
AE76: FF ; ????
AE77: FF ; ????
AE78: FF ; ????
AE79: FF ; ????
AE7A: FF ; ????
AE7B: FF ; ????
AE7C: FF ; ????
AE7D: FF ; ????
AE7E: FF ; ????
AE7F: FF ; ????
AE80: FF ; ????
AE81: FF ; ????
AE82: FF ; ????
AE83: FF ; ????
AE84: FF ; ????
AE85: FF ; ????
AE86: FF ; ????
AE87: FF ; ????
AE88: FF ; ????
AE89: FF ; ????
AE8A: FF ; ????
AE8B: FF ; ????
AE8C: FF ; ????
AE8D: FF ; ????
AE8E: FF ; ????
AE8F: FF ; ????
AE90: FF ; ????
AE91: FF ; ????
AE92: FF ; ????
AE93: FF ; ????
AE94: FF ; ????
AE95: FF ; ????
AE96: FF ; ????
AE97: FF ; ????
AE98: FF ; ????
AE99: FF ; ????
AE9A: FF ; ????
AE9B: FF ; ????
AE9C: FF ; ????
AE9D: FF ; ????
AE9E: FF ; ????
AE9F: FF ; ????
AEA0: FF ; ????
AEA1: FF ; ????
AEA2: FF ; ????
AEA3: FF ; ????
AEA4: FF ; ????
AEA5: FF ; ????
AEA6: FF ; ????
AEA7: FF ; ????
AEA8: FF ; ????
AEA9: FF ; ????
AEAA: FF ; ????
AEAB: FF ; ????
AEAC: FF ; ????
AEAD: FF ; ????
AEAE: FF ; ????
AEAF: FF ; ????
AEB0: FF ; ????
AEB1: FF ; ????
AEB2: FF ; ????
AEB3: FF ; ????
AEB4: FF ; ????
AEB5: FF ; ????
AEB6: DF ; ????
AEB7: FF ; ????
AEB8: FF ; ????
AEB9: FF ; ????
AEBA: FF ; ????
AEBB: FF ; ????
AEBC: FF ; ????
AEBD: FF ; ????
AEBE: FF ; ????
AEBF: FF ; ????
AEC0: FF ; ????
AEC1: FF ; ????
AEC2: FF ; ????
AEC3: FF ; ????
AEC4: FF ; ????
AEC5: FF ; ????
AEC6: FF ; ????
AEC7: FF ; ????
AEC8: FF ; ????
AEC9: FF ; ????
AECA: FF ; ????
AECB: FF ; ????
AECC: FF ; ????
AECD: FF ; ????
AECE: FF ; ????
AECF: FF ; ????
AED0: FF ; ????
AED1: FF ; ????
AED2: FF ; ????
AED3: FF ; ????
AED4: FF ; ????
AED5: FF ; ????
AED6: FF ; ????
AED7: FF ; ????
AED8: FF ; ????
AED9: FF ; ????
AEDA: FF ; ????
AEDB: FF ; ????
AEDC: FF ; ????
AEDD: FF ; ????
AEDE: FF ; ????
AEDF: FF ; ????
AEE0: FF ; ????
AEE1: FF ; ????
AEE2: FF ; ????
AEE3: FF ; ????
AEE4: FF ; ????
AEE5: FF ; ????
AEE6: FF ; ????
AEE7: FF ; ????
AEE8: FF ; ????
AEE9: FF ; ????
AEEA: FF ; ????
AEEB: FF ; ????
AEEC: FF ; ????
AEED: FF ; ????
AEEE: FF ; ????
AEEF: FF ; ????
AEF0: FF ; ????
AEF1: FF ; ????
AEF2: FF ; ????
AEF3: FF ; ????
AEF4: FF ; ????
AEF5: FF ; ????
AEF6: FF ; ????
AEF7: FF ; ????
AEF8: FF ; ????
AEF9: FF ; ????
AEFA: FF ; ????
AEFB: FF ; ????
AEFC: FF ; ????
AEFD: FF ; ????
AEFE: FF ; ????
AEFF: FF ; ????
AF00: 00              BRK                         
AF01: 00              BRK                         
AF02: 00              BRK                         
AF03: 00              BRK                         
AF04: 00              BRK                         
AF05: 00              BRK                         
AF06: 00              BRK                         
AF07: 00              BRK                         
AF08: 00              BRK                         
AF09: 00              BRK                         
AF0A: 00              BRK                         
AF0B: 00              BRK                         
AF0C: 00              BRK                         
AF0D: 00              BRK                         
AF0E: 00              BRK                         
AF0F: 00              BRK                         
AF10: 00              BRK                         
AF11: 00              BRK                         
AF12: 00              BRK                         
AF13: 00              BRK                         
AF14: 00              BRK                         
AF15: 00              BRK                         
AF16: 00              BRK                         
AF17: 00              BRK                         
AF18: 00              BRK                         
AF19: 00              BRK                         
AF1A: 00              BRK                         
AF1B: 00              BRK                         
AF1C: 00              BRK                         
AF1D: 00              BRK                         
AF1E: 00              BRK                         
AF1F: 00              BRK                         
AF20: 00              BRK                         
AF21: 00              BRK                         
AF22: 00              BRK                         
AF23: 00              BRK                         
AF24: 00              BRK                         
AF25: 00              BRK                         
AF26: 00              BRK                         
AF27: 00              BRK                         
AF28: 00              BRK                         
AF29: 00              BRK                         
AF2A: 00              BRK                         
AF2B: 00              BRK                         
AF2C: 00              BRK                         
AF2D: 00              BRK                         
AF2E: 00              BRK                         
AF2F: 00              BRK                         
AF30: 00              BRK                         
AF31: 00              BRK                         
AF32: 00              BRK                         
AF33: 00              BRK                         
AF34: 00              BRK                         
AF35: 00              BRK                         
AF36: 00              BRK                         
AF37: 00              BRK                         
AF38: 00              BRK                         
AF39: 00              BRK                         
AF3A: 00              BRK                         
AF3B: 00              BRK                         
AF3C: 00              BRK                         
AF3D: 00              BRK                         
AF3E: 00              BRK                         
AF3F: 00              BRK                         
AF40: 00              BRK                         
AF41: 00              BRK                         
AF42: 00              BRK                         
AF43: 00              BRK                         
AF44: 00              BRK                         
AF45: 00              BRK                         
AF46: 00              BRK                         
AF47: 00              BRK                         
AF48: 00              BRK                         
AF49: 00              BRK                         
AF4A: 00              BRK                         
AF4B: 00              BRK                         
AF4C: 00              BRK                         
AF4D: 00              BRK                         
AF4E: 00              BRK                         
AF4F: 00              BRK                         
AF50: 00              BRK                         
AF51: 00              BRK                         
AF52: 00              BRK                         
AF53: 00              BRK                         
AF54: 00              BRK                         
AF55: 00              BRK                         
AF56: 00              BRK                         
AF57: 00              BRK                         
AF58: 00              BRK                         
AF59: 00              BRK                         
AF5A: 00              BRK                         
AF5B: 00              BRK                         
AF5C: 00              BRK                         
AF5D: 00              BRK                         
AF5E: 00              BRK                         
AF5F: 00              BRK                         
AF60: 00              BRK                         
AF61: 00              BRK                         
AF62: 00              BRK                         
AF63: 00              BRK                         
AF64: 00              BRK                         
AF65: 00              BRK                         
AF66: 00              BRK                         
AF67: 00              BRK                         
AF68: 00              BRK                         
AF69: 00              BRK                         
AF6A: 00              BRK                         
AF6B: 00              BRK                         
AF6C: 00              BRK                         
AF6D: 00              BRK                         
AF6E: 00              BRK                         
AF6F: 00              BRK                         
AF70: 00              BRK                         
AF71: 00              BRK                         
AF72: 00              BRK                         
AF73: 00              BRK                         
AF74: 00              BRK                         
AF75: 00              BRK                         
AF76: 00              BRK                         
AF77: 00              BRK                         
AF78: 00              BRK                         
AF79: 00              BRK                         
AF7A: 00              BRK                         
AF7B: 00              BRK                         
AF7C: 00              BRK                         
AF7D: 00              BRK                         
AF7E: 00              BRK                         
AF7F: 00              BRK                         
AF80: 00              BRK                         
AF81: 00              BRK                         
AF82: 00              BRK                         
AF83: 00              BRK                         
AF84: 00              BRK                         
AF85: 00              BRK                         
AF86: 00              BRK                         
AF87: 00              BRK                         
AF88: 00              BRK                         
AF89: 00              BRK                         
AF8A: 00              BRK                         
AF8B: 00              BRK                         
AF8C: 00              BRK                         
AF8D: 00              BRK                         
AF8E: 00              BRK                         
AF8F: 00              BRK                         
AF90: 00              BRK                         
AF91: 00              BRK                         
AF92: 00              BRK                         
AF93: 00              BRK                         
AF94: 00              BRK                         
AF95: 00              BRK                         
AF96: 00              BRK                         
AF97: 00              BRK                         
AF98: 00              BRK                         
AF99: 00              BRK                         
AF9A: 00              BRK                         
AF9B: 00              BRK                         
AF9C: 00              BRK                         
AF9D: 00              BRK                         
AF9E: 00              BRK                         
AF9F: 00              BRK                         
AFA0: 00              BRK                         
AFA1: 00              BRK                         
AFA2: 00              BRK                         
AFA3: 00              BRK                         
AFA4: 00              BRK                         
AFA5: 00              BRK                         
AFA6: 00              BRK                         
AFA7: 00              BRK                         
AFA8: 00              BRK                         
AFA9: 00              BRK                         
AFAA: 00              BRK                         
AFAB: 00              BRK                         
AFAC: 00              BRK                         
AFAD: 00              BRK                         
AFAE: 00              BRK                         
AFAF: 00              BRK                         
AFB0: 00              BRK                         
AFB1: 00              BRK                         
AFB2: 00              BRK                         
AFB3: 00              BRK                         
AFB4: 00              BRK                         
AFB5: 00              BRK                         
AFB6: 00              BRK                         
AFB7: 00              BRK                         
AFB8: 00              BRK                         
AFB9: 00              BRK                         
AFBA: 00              BRK                         
AFBB: 00              BRK                         
AFBC: 00              BRK                         
AFBD: 00              BRK                         
AFBE: 00              BRK                         
AFBF: 00              BRK                         
AFC0: 00              BRK                         
AFC1: 00              BRK                         
AFC2: 00              BRK                         
AFC3: 00              BRK                         
AFC4: 00              BRK                         
AFC5: 00              BRK                         
AFC6: 00              BRK                         
AFC7: 00              BRK                         
AFC8: 00              BRK                         
AFC9: 00              BRK                         
AFCA: 00              BRK                         
AFCB: 00              BRK                         
AFCC: 00              BRK                         
AFCD: 00              BRK                         
AFCE: 00              BRK                         
AFCF: 00              BRK                         
AFD0: 00              BRK                         
AFD1: 00              BRK                         
AFD2: 00              BRK                         
AFD3: 00              BRK                         
AFD4: 00              BRK                         
AFD5: 00              BRK                         
AFD6: 00              BRK                         
AFD7: 00              BRK                         
AFD8: 00              BRK                         
AFD9: 00              BRK                         
AFDA: 00              BRK                         
AFDB: 00              BRK                         
AFDC: 00              BRK                         
AFDD: 00              BRK                         
AFDE: 00              BRK                         
AFDF: 00              BRK                         
AFE0: 00              BRK                         
AFE1: 00              BRK                         
AFE2: 00              BRK                         
AFE3: 00              BRK                         
AFE4: 00              BRK                         
AFE5: 00              BRK                         
AFE6: 00              BRK                         
AFE7: 00              BRK                         
AFE8: 00              BRK                         
AFE9: 00              BRK                         
AFEA: 00              BRK                         
AFEB: 00              BRK                         
AFEC: 00              BRK                         
AFED: 00              BRK                         
AFEE: 00              BRK                         
AFEF: 00              BRK                         
AFF0: 00              BRK                         
AFF1: 00              BRK                         
AFF2: 00              BRK                         
AFF3: 00              BRK                         
AFF4: 00              BRK                         
AFF5: 00              BRK                         
AFF6: 00              BRK                         
AFF7: 00              BRK                         
AFF8: 00              BRK                         
AFF9: 00              BRK                         
AFFA: 00              BRK                         
AFFB: 00              BRK                         
AFFC: 00              BRK                         
AFFD: 00              BRK                         
AFFE: 00              BRK                         
AFFF: 00              BRK                         
B000: 60              RTS                         
B001: A9 01           LDA     #$01                
B003: 8D 2F 01        STA     $012F               
B006: 4C 09 B0        JMP     $B009               ; {}
B009: A2 50           LDX     #$50                
B00B: BD 01 07        LDA     $0701,X             
B00E: 29 07           AND     #$07                
B010: 20 2B EE        JSR     $EE2B               
B013: 2B ; ????
B014: B0 DC           BCS     $AFF2               ; {}
B016: B0 27           BCS     $B03F               ; {}
B018: B2 ; ????
B019: 42 ; ????
B01A: B2 ; ????
B01B: A2 50           LDX     #$50                
B01D: FE 01 07        INC     $0701,X             
B020: BD 01 07        LDA     $0701,X             
B023: 29 07           AND     #$07                
B025: 09 80           ORA     #$80                
B027: 9D 01 07        STA     $0701,X             
B02A: 60              RTS                         
B02B: 20 54 B0        JSR     $B054               ; {}
B02E: A0 D4           LDY     #$D4                
B030: A9 81           LDA     #$81                
B032: 9D 01 07        STA     $0701,X             
B035: 99 01 07        STA     $0701,Y             
B038: A9 00           LDA     #$00                
B03A: 9D 0C 07        STA     $070C,X             
B03D: A0 2F           LDY     #$2F                
B03F: A9 F8           LDA     #$F8                
B041: 99 A0 07        STA     $07A0,Y             
B044: 88              DEY                         
B045: 10 FA           BPL     $B041               ; {}
B047: 20 5D B1        JSR     $B15D               ; {}
B04A: 20 83 B0        JSR     $B083               ; {}
B04D: 60              RTS                         
B04E: A2 50           LDX     #$50                
B050: A0 A0           LDY     #$A0                
B052: D0 14           BNE     $B068               ; {}
B054: A2 50           LDX     #$50                
B056: A0 A0           LDY     #$A0                
B058: A9 F0           LDA     #$F0                
B05A: 9D 03 07        STA     $0703,X             
B05D: 18              CLC                         
B05E: 69 04           ADC     #$04                
B060: 99 02 07        STA     $0702,Y             
B063: A9 00           LDA     #$00                
B065: 9D 07 07        STA     $0707,X             
B068: A9 A0           LDA     #$A0                
B06A: 9D 00 07        STA     $0700,X             
B06D: 18              CLC                         
B06E: 69 04           ADC     #$04                
B070: 99 01 07        STA     $0701,Y             
B073: A9 00           LDA     #$00                
B075: 9D 0D 07        STA     $070D,X             
B078: A9 00           LDA     #$00                
B07A: 9D 0E 07        STA     $070E,X             
B07D: A9 F8           LDA     #$F8                
B07F: 9D 0F 07        STA     $070F,X             
B082: 60              RTS                         
B083: A9 CC           LDA     #$CC                
B085: 85 0E           STA     $0E                 
B087: A9 0C           LDA     #$0C                
B089: 85 0F           STA     $0F                 
B08B: A4 0E           LDY     $0E                 
B08D: A2 D4           LDX     #$D4                
B08F: B9 02 07        LDA     $0702,Y             
B092: 9D 03 07        STA     $0703,X             
B095: 99 06 07        STA     $0706,Y             
B098: 99 07 07        STA     $0707,Y             
B09B: 99 07 02        STA     $0207,Y             
B09E: 38              SEC                         
B09F: B9 01 07        LDA     $0701,Y             
B0A2: 9D 00 07        STA     $0700,X             
B0A5: 99 05 07        STA     $0705,Y             
B0A8: 99 04 07        STA     $0704,Y             
B0AB: 99 04 02        STA     $0204,Y             
B0AE: 20 F7 97        JSR     $97F7               ; {}
B0B1: 20 09 DA        JSR     $DA09               
B0B4: A4 0E           LDY     $0E                 
B0B6: C8              INY                         
B0B7: C8              INY                         
B0B8: C8              INY                         
B0B9: C8              INY                         
B0BA: A9 F4           LDA     #$F4                
B0BC: 99 01 02        STA     $0201,Y             
B0BF: A9 22           LDA     #$22                
B0C1: 99 02 02        STA     $0202,Y             
B0C4: BD 03 07        LDA     $0703,X             
B0C7: 99 03 07        STA     $0703,Y             
B0CA: 99 02 07        STA     $0702,Y             
B0CD: 38              SEC                         
B0CE: A5 0E           LDA     $0E                 
B0D0: E9 04           SBC     #$04                
B0D2: 85 0E           STA     $0E                 
B0D4: C6 0F           DEC     $0F                 
B0D6: F0 03           BEQ     $B0DB               ; {}
B0D8: 4C 8B B0        JMP     $B08B               ; {}
B0DB: 60              RTS                         
B0DC: A5 14           LDA     $14                 
B0DE: 29 01           AND     #$01                
B0E0: F0 01           BEQ     $B0E3               ; {}
B0E2: 60              RTS                         
B0E3: 20 F2 B0        JSR     $B0F2               ; {}
B0E6: 20 5D B1        JSR     $B15D               ; {}
B0E9: 20 85 B1        JSR     $B185               ; {}
B0EC: 20 70 B2        JSR     $B270               ; {}
B0EF: 4C 83 B0        JMP     $B083               ; {}
B0F2: A0 A0           LDY     #$A0                
B0F4: 18              CLC                         
B0F5: BD 00 07        LDA     $0700,X             
B0F8: 69 04           ADC     #$04                
B0FA: 99 01 07        STA     $0701,Y             
B0FD: BD 07 07        LDA     $0707,X             
B100: 08              PHP                         
B101: BD 03 07        LDA     $0703,X             
B104: 28              PLP                         
B105: D0 03           BNE     $B10A               ; {}
B107: 18              CLC                         
B108: 69 08           ADC     #$08                
B10A: 99 02 07        STA     $0702,Y             
B10D: BD 07 07        LDA     $0707,X             
B110: D0 0F           BNE     $B121               ; {}
B112: DE 03 07        DEC     $0703,X             
B115: BD 03 07        LDA     $0703,X             
B118: C9 10           CMP     #$10                
B11A: B0 15           BCS     $B131               ; {}
B11C: FE 07 07        INC     $0707,X             
B11F: D0 10           BNE     $B131               ; {}
B121: FE 03 07        INC     $0703,X             
B124: BD 03 07        LDA     $0703,X             
B127: C9 E0           CMP     #$E0                
B129: 90 06           BCC     $B131               ; {}
B12B: DE 03 07        DEC     $0703,X             
B12E: DE 07 07        DEC     $0707,X             
B131: 18              CLC                         
B132: BD 0E 07        LDA     $070E,X             
B135: 69 40           ADC     #$40                
B137: 9D 0E 07        STA     $070E,X             
B13A: BD 0F 07        LDA     $070F,X             
B13D: 69 00           ADC     #$00                
B13F: 9D 0F 07        STA     $070F,X             
B142: 18              CLC                         
B143: BD 0D 07        LDA     $070D,X             
B146: 7D 0E 07        ADC     $070E,X             
B149: 9D 0D 07        STA     $070D,X             
B14C: BD 00 07        LDA     $0700,X             
B14F: 7D 0F 07        ADC     $070F,X             
B152: 9D 00 07        STA     $0700,X             
B155: C9 A0           CMP     #$A0                
B157: 90 03           BCC     $B15C               ; {}
B159: 20 4E B0        JSR     $B04E               ; {}
B15C: 60              RTS                         
B15D: A2 50           LDX     #$50                
B15F: A9 03           LDA     #$03                
B161: 85 00           STA     $00                 ; {ram.GP_00}
B163: A0 00           LDY     #$00                
B165: A5 14           LDA     $14                 
B167: 29 10           AND     #$10                
B169: D0 02           BNE     $B16D               ; {}
B16B: A0 10           LDY     #$10                
B16D: BD 07 07        LDA     $0707,X             
B170: 08              PHP                         
B171: 98              TYA                         
B172: 28              PLP                         
B173: F0 03           BEQ     $B178               ; {}
B175: 18              CLC                         
B176: 69 20           ADC     #$20                
B178: A8              TAY                         
B179: A9 A8           LDA     #$A8                
B17B: 85 08           STA     $08                 
B17D: A9 B2           LDA     #$B2                
B17F: 85 09           STA     $09                 
B181: 98              TYA                         
B182: 4C AB 9B        JMP     $9BAB               ; {}
B185: A2 50           LDX     #$50                
B187: 20 90 D9        JSR     $D990               
B18A: B0 12           BCS     $B19E               ; {}
B18C: A9 F8           LDA     #$F8                
B18E: 99 00 07        STA     $0700,Y             
B191: A9 02           LDA     #$02                
B193: 8D 84 03        STA     $0384               
B196: A9 20           LDA     #$20                
B198: 9D 0C 07        STA     $070C,X             
B19B: 20 A4 B1        JSR     $B1A4               ; {}
B19E: 20 F7 97        JSR     $97F7               ; {}
B1A1: 4C 09 DA        JMP     $DA09               
B1A4: A5 3C           LDA     $3C                 
B1A6: D0 08           BNE     $B1B0               ; {}
B1A8: C0 38           CPY     #$38                
B1AA: F0 08           BEQ     $B1B4               ; {}
B1AC: C0 3C           CPY     #$3C                
B1AE: F0 04           BEQ     $B1B4               ; {}
B1B0: A9 05           LDA     #$05                
B1B2: D0 06           BNE     $B1BA               ; {}
B1B4: 18              CLC                         
B1B5: AD 52 01        LDA     $0152               
B1B8: 69 01           ADC     #$01                
B1BA: 85 00           STA     $00                 ; {ram.GP_00}
B1BC: A5 6B           LDA     $6B                 
B1BE: 38              SEC                         
B1BF: E5 00           SBC     $00                 ; {ram.GP_00}
B1C1: 90 05           BCC     $B1C8               ; {}
B1C3: F0 03           BEQ     $B1C8               ; {}
B1C5: 85 6B           STA     $6B                 
B1C7: 60              RTS                         
B1C8: A9 00           LDA     #$00                
B1CA: 85 6B           STA     $6B                 
B1CC: A9 80           LDA     #$80                
B1CE: 20 E1 E2        JSR     $E2E1               
B1D1: 20 F0 E2        JSR     $E2F0               
B1D4: A9 80           LDA     #$80                
B1D6: 9D 06 07        STA     $0706,X             
B1D9: 20 1B B0        JSR     $B01B               ; {}
B1DC: A9 A0           LDA     #$A0                
B1DE: 85 0A           STA     $0A                 
B1E0: 85 08           STA     $08                 
B1E2: A9 07           LDA     #$07                
B1E4: 85 09           STA     $09                 
B1E6: A9 02           LDA     #$02                
B1E8: 85 0B           STA     $0B                 
B1EA: A0 3F           LDY     #$3F                
B1EC: A9 00           LDA     #$00                
B1EE: 91 08           STA     ($08),Y             
B1F0: A9 F8           LDA     #$F8                
B1F2: 91 0A           STA     ($0A),Y             
B1F4: 88              DEY                         
B1F5: 10 F5           BPL     $B1EC               ; {}
B1F7: A2 A0           LDX     #$A0                
B1F9: A0 50           LDY     #$50                
B1FB: B9 00 07        LDA     $0700,Y             
B1FE: 9D 00 07        STA     $0700,X             
B201: B9 03 07        LDA     $0703,Y             
B204: 9D 03 07        STA     $0703,X             
B207: A9 F4           LDA     #$F4                
B209: 8D 75 01        STA     $0175               
B20C: A9 02           LDA     #$02                
B20E: 8D 76 01        STA     $0176               
B211: A9 05           LDA     #$05                
B213: 8D 74 01        STA     $0174               
B216: A9 40           LDA     #$40                
B218: 20 34 9A        JSR     $9A34               ; {}
B21B: A2 50           LDX     #$50                
B21D: 8A              TXA                         
B21E: 85 08           STA     $08                 
B220: 85 0A           STA     $0A                 
B222: A0 20           LDY     #$20                
B224: 4C 6D 9A        JMP     $9A6D               ; {}
B227: A2 A0           LDX     #$A0                
B229: AD 74 01        LDA     $0174               
B22C: F0 03           BEQ     $B231               ; {}
B22E: 4C 86 9A        JMP     $9A86               ; {}
B231: A2 50           LDX     #$50                
B233: A9 00           LDA     #$00                
B235: 9D 06 07        STA     $0706,X             
B238: A2 A0           LDX     #$A0                
B23A: A9 68           LDA     #$68                
B23C: 20 E0 D2        JSR     $D2E0               
B23F: 4C 1B B0        JMP     $B01B               ; {}
B242: A2 50           LDX     #$50                
B244: DE 06 07        DEC     $0706,X             
B247: D0 5E           BNE     $B2A7               ; {}
B249: A2 A0           LDX     #$A0                
B24B: A9 F8           LDA     #$F8                
B24D: 9D 00 07        STA     $0700,X             
B250: 9D 00 02        STA     $0200,X             
B253: 9D 08 02        STA     $0208,X             
B256: A2 50           LDX     #$50                
B258: 20 1B B0        JSR     $B01B               ; {}
B25B: A9 01           LDA     #$01                
B25D: 8D 54 01        STA     $0154               
B260: 85 20           STA     $20                 
B262: A0 29           LDY     #$29                
B264: A9 00           LDA     #$00                
B266: 85 3A           STA     $3A                 
B268: 8D 2F 01        STA     $012F               
B26B: A9 04           LDA     #$04                
B26D: 4C 90 CA        JMP     $CA90               
B270: BD 0C 07        LDA     $070C,X             
B273: F0 11           BEQ     $B286               ; {}
B275: DE 0C 07        DEC     $070C,X             
B278: BD 0C 07        LDA     $070C,X             
B27B: A8              TAY                         
B27C: 29 01           AND     #$01                
B27E: F0 06           BEQ     $B286               ; {}
B280: 98              TYA                         
B281: 29 03           AND     #$03                
B283: 4C 88 B2        JMP     $B288               ; {}
B286: A9 02           LDA     #$02                
B288: 85 01           STA     $01                 
B28A: 09 20           ORA     #$20                
B28C: EA              NOP                         
B28D: EA              NOP                         
B28E: EA              NOP                         
B28F: A9 0F           LDA     #$0F                
B291: 85 00           STA     $00                 ; {ram.GP_00}
B293: A0 02           LDY     #$02                
B295: B9 A8 B2        LDA     $B2A8,Y             ; {}
B298: 29 FC           AND     #$FC                
B29A: 05 01           ORA     $01                 
B29C: EA              NOP                         
B29D: EA              NOP                         
B29E: EA              NOP                         
B29F: C8              INY                         
B2A0: C8              INY                         
B2A1: C8              INY                         
B2A2: C8              INY                         
B2A3: C6 00           DEC     $00                 ; {ram.GP_00}
B2A5: 10 EE           BPL     $B295               ; {}
B2A7: 60              RTS                         
B2A8: 00              BRK                         
B2A9: C0 22           CPY     #$22                
B2AB: 00              BRK                         
B2AC: 00              BRK                         
B2AD: C1 22           CMP     ($22,X)             
B2AF: 08              PHP                         
B2B0: 08              PHP                         
B2B1: C2 ; ????
B2B2: 22 ; ????
B2B3: 00              BRK                         
B2B4: 08              PHP                         
B2B5: C3 ; ????
B2B6: 22 ; ????
B2B7: 08              PHP                         
B2B8: 00              BRK                         
B2B9: C4 22           CPY     $22                 
B2BB: 00              BRK                         
B2BC: 00              BRK                         
B2BD: C5 22           CMP     $22                 
B2BF: 08              PHP                         
B2C0: 08              PHP                         
B2C1: C6 22           DEC     $22                 
B2C3: 00              BRK                         
B2C4: 08              PHP                         
B2C5: C7 ; ????
B2C6: 22 ; ????
B2C7: 08              PHP                         
B2C8: 00              BRK                         
B2C9: C1 62           CMP     ($62,X)             
B2CB: 00              BRK                         
B2CC: 00              BRK                         
B2CD: C0 62           CPY     #$62                
B2CF: 08              PHP                         
B2D0: 08              PHP                         
B2D1: C3 ; ????
B2D2: 62 ; ????
B2D3: 00              BRK                         
B2D4: 08              PHP                         
B2D5: C2 ; ????
B2D6: 62 ; ????
B2D7: 08              PHP                         
B2D8: 00              BRK                         
B2D9: C5 62           CMP     $62                 
B2DB: 00              BRK                         
B2DC: 00              BRK                         
B2DD: C4 62           CPY     $62                 
B2DF: 08              PHP                         
B2E0: 08              PHP                         
B2E1: C7 ; ????
B2E2: 62 ; ????
B2E3: 00              BRK                         
B2E4: 08              PHP                         
B2E5: C6 62           DEC     $62                 
B2E7: 08              PHP                         
B2E8: 00              BRK                         
B2E9: FE 02 FE        INC     $FE02,X             
B2EC: 02 ; ????
B2ED: 00              BRK                         
B2EE: 02 ; ????
B2EF: 02 ; ????
B2F0: 00              BRK                         
B2F1: 02 ; ????
B2F2: FE 02 FE        INC     $FE02,X             
B2F5: 00              BRK                         
B2F6: FE FE FF        INC     $FFFE,X             
B2F9: FF ; ????
B2FA: FF ; ????
B2FB: FF ; ????
B2FC: FF ; ????
B2FD: FF ; ????
B2FE: FF ; ????
B2FF: FF ; ????
B300: 00              BRK                         
B301: 00              BRK                         
B302: 00              BRK                         
B303: 00              BRK                         
B304: 00              BRK                         
B305: 00              BRK                         
B306: 00              BRK                         
B307: 00              BRK                         
B308: 00              BRK                         
B309: 00              BRK                         
B30A: 00              BRK                         
B30B: 00              BRK                         
B30C: 00              BRK                         
B30D: 00              BRK                         
B30E: 00              BRK                         
B30F: 00              BRK                         
B310: 00              BRK                         
B311: 00              BRK                         
B312: 00              BRK                         
B313: 00              BRK                         
B314: 00              BRK                         
B315: 00              BRK                         
B316: 00              BRK                         
B317: 00              BRK                         
B318: 00              BRK                         
B319: 00              BRK                         
B31A: 00              BRK                         
B31B: 00              BRK                         
B31C: 00              BRK                         
B31D: 00              BRK                         
B31E: 00              BRK                         
B31F: 00              BRK                         
B320: 00              BRK                         
B321: 00              BRK                         
B322: 00              BRK                         
B323: 00              BRK                         
B324: 00              BRK                         
B325: 00              BRK                         
B326: 00              BRK                         
B327: 00              BRK                         
B328: 00              BRK                         
B329: 00              BRK                         
B32A: 00              BRK                         
B32B: 00              BRK                         
B32C: 00              BRK                         
B32D: 00              BRK                         
B32E: 00              BRK                         
B32F: 00              BRK                         
B330: 00              BRK                         
B331: 00              BRK                         
B332: 00              BRK                         
B333: 00              BRK                         
B334: 00              BRK                         
B335: 00              BRK                         
B336: 00              BRK                         
B337: 00              BRK                         
B338: 00              BRK                         
B339: 00              BRK                         
B33A: 00              BRK                         
B33B: 00              BRK                         
B33C: 00              BRK                         
B33D: 00              BRK                         
B33E: 00              BRK                         
B33F: 00              BRK                         
B340: 00              BRK                         
B341: 00              BRK                         
B342: 00              BRK                         
B343: 00              BRK                         
B344: 00              BRK                         
B345: 00              BRK                         
B346: 00              BRK                         
B347: 00              BRK                         
B348: 00              BRK                         
B349: 00              BRK                         
B34A: 00              BRK                         
B34B: 00              BRK                         
B34C: 00              BRK                         
B34D: 00              BRK                         
B34E: 00              BRK                         
B34F: 00              BRK                         
B350: 00              BRK                         
B351: 00              BRK                         
B352: 00              BRK                         
B353: 00              BRK                         
B354: 00              BRK                         
B355: 00              BRK                         
B356: 00              BRK                         
B357: 00              BRK                         
B358: 00              BRK                         
B359: 00              BRK                         
B35A: 00              BRK                         
B35B: 00              BRK                         
B35C: 00              BRK                         
B35D: 00              BRK                         
B35E: 00              BRK                         
B35F: 00              BRK                         
B360: 00              BRK                         
B361: 00              BRK                         
B362: 00              BRK                         
B363: 00              BRK                         
B364: 00              BRK                         
B365: 00              BRK                         
B366: 00              BRK                         
B367: 00              BRK                         
B368: 00              BRK                         
B369: 00              BRK                         
B36A: 00              BRK                         
B36B: 00              BRK                         
B36C: 00              BRK                         
B36D: 00              BRK                         
B36E: 00              BRK                         
B36F: 00              BRK                         
B370: 00              BRK                         
B371: 00              BRK                         
B372: 00              BRK                         
B373: 00              BRK                         
B374: 00              BRK                         
B375: 00              BRK                         
B376: 00              BRK                         
B377: 00              BRK                         
B378: 00              BRK                         
B379: 00              BRK                         
B37A: 00              BRK                         
B37B: 00              BRK                         
B37C: 00              BRK                         
B37D: 00              BRK                         
B37E: 00              BRK                         
B37F: 00              BRK                         
B380: 00              BRK                         
B381: 00              BRK                         
B382: 00              BRK                         
B383: 00              BRK                         
B384: 00              BRK                         
B385: 00              BRK                         
B386: 00              BRK                         
B387: 00              BRK                         
B388: 00              BRK                         
B389: 00              BRK                         
B38A: 00              BRK                         
B38B: 00              BRK                         
B38C: 00              BRK                         
B38D: 00              BRK                         
B38E: 00              BRK                         
B38F: 00              BRK                         
B390: 00              BRK                         
B391: 00              BRK                         
B392: 00              BRK                         
B393: 00              BRK                         
B394: 00              BRK                         
B395: 00              BRK                         
B396: 00              BRK                         
B397: 00              BRK                         
B398: 00              BRK                         
B399: 00              BRK                         
B39A: 00              BRK                         
B39B: 00              BRK                         
B39C: 00              BRK                         
B39D: 00              BRK                         
B39E: 00              BRK                         
B39F: 00              BRK                         
B3A0: 00              BRK                         
B3A1: 00              BRK                         
B3A2: 00              BRK                         
B3A3: 00              BRK                         
B3A4: 00              BRK                         
B3A5: 00              BRK                         
B3A6: 00              BRK                         
B3A7: 00              BRK                         
B3A8: 00              BRK                         
B3A9: 00              BRK                         
B3AA: 00              BRK                         
B3AB: 00              BRK                         
B3AC: 00              BRK                         
B3AD: 00              BRK                         
B3AE: 00              BRK                         
B3AF: 00              BRK                         
B3B0: 00              BRK                         
B3B1: 00              BRK                         
B3B2: 00              BRK                         
B3B3: 00              BRK                         
B3B4: 00              BRK                         
B3B5: 00              BRK                         
B3B6: 00              BRK                         
B3B7: 00              BRK                         
B3B8: 00              BRK                         
B3B9: 00              BRK                         
B3BA: 00              BRK                         
B3BB: 00              BRK                         
B3BC: 00              BRK                         
B3BD: 00              BRK                         
B3BE: 00              BRK                         
B3BF: 00              BRK                         
B3C0: 00              BRK                         
B3C1: 00              BRK                         
B3C2: 00              BRK                         
B3C3: 00              BRK                         
B3C4: 00              BRK                         
B3C5: 00              BRK                         
B3C6: 00              BRK                         
B3C7: 00              BRK                         
B3C8: 00              BRK                         
B3C9: 00              BRK                         
B3CA: 00              BRK                         
B3CB: 00              BRK                         
B3CC: 00              BRK                         
B3CD: 00              BRK                         
B3CE: 00              BRK                         
B3CF: 00              BRK                         
B3D0: 00              BRK                         
B3D1: 00              BRK                         
B3D2: 00              BRK                         
B3D3: 00              BRK                         
B3D4: 00              BRK                         
B3D5: 00              BRK                         
B3D6: 00              BRK                         
B3D7: 00              BRK                         
B3D8: 00              BRK                         
B3D9: 00              BRK                         
B3DA: 00              BRK                         
B3DB: 00              BRK                         
B3DC: 00              BRK                         
B3DD: 00              BRK                         
B3DE: 00              BRK                         
B3DF: 00              BRK                         
B3E0: 00              BRK                         
B3E1: 00              BRK                         
B3E2: 00              BRK                         
B3E3: 00              BRK                         
B3E4: 00              BRK                         
B3E5: 00              BRK                         
B3E6: 00              BRK                         
B3E7: 00              BRK                         
B3E8: 00              BRK                         
B3E9: 00              BRK                         
B3EA: 00              BRK                         
B3EB: 00              BRK                         
B3EC: 00              BRK                         
B3ED: 00              BRK                         
B3EE: 00              BRK                         
B3EF: 00              BRK                         
B3F0: 00              BRK                         
B3F1: 00              BRK                         
B3F2: 00              BRK                         
B3F3: 00              BRK                         
B3F4: 00              BRK                         
B3F5: 00              BRK                         
B3F6: 00              BRK                         
B3F7: 00              BRK                         
B3F8: 00              BRK                         
B3F9: 00              BRK                         
B3FA: 00              BRK                         
B3FB: 00              BRK                         
B3FC: 00              BRK                         
B3FD: 00              BRK                         
B3FE: 00              BRK                         
B3FF: 00              BRK                         
B400: FF ; ????
B401: FF ; ????
B402: FF ; ????
B403: FF ; ????
B404: FF ; ????
B405: FF ; ????
B406: FF ; ????
B407: FF ; ????
B408: FF ; ????
B409: FF ; ????
B40A: FF ; ????
B40B: FF ; ????
B40C: FF ; ????
B40D: FF ; ????
B40E: FF ; ????
B40F: FF ; ????
B410: FF ; ????
B411: FF ; ????
B412: FF ; ????
B413: FF ; ????
B414: FF ; ????
B415: FF ; ????
B416: FF ; ????
B417: FF ; ????
B418: FF ; ????
B419: FF ; ????
B41A: FF ; ????
B41B: FF ; ????
B41C: FF ; ????
B41D: FF ; ????
B41E: FF ; ????
B41F: FF ; ????
B420: FF ; ????
B421: FF ; ????
B422: FF ; ????
B423: FF ; ????
B424: FF ; ????
B425: FF ; ????
B426: FF ; ????
B427: FF ; ????
B428: FF ; ????
B429: FF ; ????
B42A: FF ; ????
B42B: FF ; ????
B42C: FF ; ????
B42D: FF ; ????
B42E: FF ; ????
B42F: FF ; ????
B430: FF ; ????
B431: FF ; ????
B432: FF ; ????
B433: FF ; ????
B434: FF ; ????
B435: FF ; ????
B436: FF ; ????
B437: FF ; ????
B438: FF ; ????
B439: FF ; ????
B43A: FF ; ????
B43B: FF ; ????
B43C: FF ; ????
B43D: FF ; ????
B43E: FF ; ????
B43F: FF ; ????
B440: FF ; ????
B441: FF ; ????
B442: FF ; ????
B443: FF ; ????
B444: FF ; ????
B445: FF ; ????
B446: FF ; ????
B447: FF ; ????
B448: FF ; ????
B449: FF ; ????
B44A: FF ; ????
B44B: FF ; ????
B44C: FF ; ????
B44D: FF ; ????
B44E: FF ; ????
B44F: FF ; ????
B450: FF ; ????
B451: FF ; ????
B452: FF ; ????
B453: FF ; ????
B454: FF ; ????
B455: FF ; ????
B456: FF ; ????
B457: FE FF FF        INC     $FFFF,X             
B45A: FF ; ????
B45B: FF ; ????
B45C: FF ; ????
B45D: FF ; ????
B45E: FF ; ????
B45F: FF ; ????
B460: FF ; ????
B461: FF ; ????
B462: FF ; ????
B463: FF ; ????
B464: FF ; ????
B465: FF ; ????
B466: FF ; ????
B467: FF ; ????
B468: FF ; ????
B469: FF ; ????
B46A: FF ; ????
B46B: FF ; ????
B46C: FF ; ????
B46D: FF ; ????
B46E: FF ; ????
B46F: FF ; ????
B470: FF ; ????
B471: FF ; ????
B472: FF ; ????
B473: FF ; ????
B474: FF ; ????
B475: FF ; ????
B476: FF ; ????
B477: FF ; ????
B478: FF ; ????
B479: FF ; ????
B47A: FF ; ????
B47B: FF ; ????
B47C: FF ; ????
B47D: FF ; ????
B47E: FF ; ????
B47F: FF ; ????
B480: FF ; ????
B481: FF ; ????
B482: FF ; ????
B483: FF ; ????
B484: FF ; ????
B485: FF ; ????
B486: FF ; ????
B487: FF ; ????
B488: FF ; ????
B489: FF ; ????
B48A: FF ; ????
B48B: FF ; ????
B48C: FF ; ????
B48D: FF ; ????
B48E: FF ; ????
B48F: FF ; ????
B490: FF ; ????
B491: FF ; ????
B492: FF ; ????
B493: FF ; ????
B494: FF ; ????
B495: FF ; ????
B496: FF ; ????
B497: FF ; ????
B498: FF ; ????
B499: FF ; ????
B49A: FF ; ????
B49B: FF ; ????
B49C: FF ; ????
B49D: FF ; ????
B49E: FF ; ????
B49F: FF ; ????
B4A0: FF ; ????
B4A1: FF ; ????
B4A2: FF ; ????
B4A3: FF ; ????
B4A4: FF ; ????
B4A5: FF ; ????
B4A6: FF ; ????
B4A7: FF ; ????
B4A8: FF ; ????
B4A9: FF ; ????
B4AA: FF ; ????
B4AB: FF ; ????
B4AC: FF ; ????
B4AD: FF ; ????
B4AE: FF ; ????
B4AF: FF ; ????
B4B0: FF ; ????
B4B1: FF ; ????
B4B2: FF ; ????
B4B3: FF ; ????
B4B4: FF ; ????
B4B5: FF ; ????
B4B6: FF ; ????
B4B7: FF ; ????
B4B8: FF ; ????
B4B9: FF ; ????
B4BA: FF ; ????
B4BB: FF ; ????
B4BC: FF ; ????
B4BD: FF ; ????
B4BE: FF ; ????
B4BF: FF ; ????
B4C0: FF ; ????
B4C1: FF ; ????
B4C2: FF ; ????
B4C3: FF ; ????
B4C4: FF ; ????
B4C5: FF ; ????
B4C6: FF ; ????
B4C7: FF ; ????
B4C8: FF ; ????
B4C9: FF ; ????
B4CA: FF ; ????
B4CB: FF ; ????
B4CC: FF ; ????
B4CD: FF ; ????
B4CE: FF ; ????
B4CF: FF ; ????
B4D0: FF ; ????
B4D1: FF ; ????
B4D2: FF ; ????
B4D3: FF ; ????
B4D4: FF ; ????
B4D5: FF ; ????
B4D6: 7F ; ????
B4D7: FF ; ????
B4D8: FF ; ????
B4D9: FF ; ????
B4DA: FF ; ????
B4DB: FF ; ????
B4DC: FF ; ????
B4DD: FF ; ????
B4DE: FF ; ????
B4DF: FF ; ????
B4E0: FF ; ????
B4E1: FF ; ????
B4E2: FF ; ????
B4E3: FF ; ????
B4E4: FF ; ????
B4E5: FF ; ????
B4E6: FF ; ????
B4E7: FF ; ????
B4E8: FF ; ????
B4E9: FF ; ????
B4EA: FF ; ????
B4EB: FF ; ????
B4EC: FF ; ????
B4ED: FF ; ????
B4EE: FF ; ????
B4EF: FF ; ????
B4F0: FF ; ????
B4F1: FF ; ????
B4F2: FF ; ????
B4F3: FF ; ????
B4F4: FF ; ????
B4F5: FF ; ????
B4F6: FF ; ????
B4F7: FF ; ????
B4F8: FF ; ????
B4F9: FF ; ????
B4FA: FF ; ????
B4FB: FF ; ????
B4FC: FF ; ????
B4FD: FF ; ????
B4FE: FF ; ????
B4FF: FF ; ????
B500: 00              BRK                         
B501: 00              BRK                         
B502: 00              BRK                         
B503: 00              BRK                         
B504: 00              BRK                         
B505: 00              BRK                         
B506: 00              BRK                         
B507: 00              BRK                         
B508: 00              BRK                         
B509: 00              BRK                         
B50A: 00              BRK                         
B50B: 00              BRK                         
B50C: 00              BRK                         
B50D: 00              BRK                         
B50E: 00              BRK                         
B50F: 00              BRK                         
B510: 00              BRK                         
B511: 00              BRK                         
B512: 00              BRK                         
B513: 00              BRK                         
B514: 00              BRK                         
B515: 00              BRK                         
B516: 00              BRK                         
B517: 00              BRK                         
B518: 00              BRK                         
B519: 00              BRK                         
B51A: 00              BRK                         
B51B: 00              BRK                         
B51C: 00              BRK                         
B51D: 00              BRK                         
B51E: 00              BRK                         
B51F: 00              BRK                         
B520: 00              BRK                         
B521: 00              BRK                         
B522: 00              BRK                         
B523: 00              BRK                         
B524: 00              BRK                         
B525: 00              BRK                         
B526: 00              BRK                         
B527: 00              BRK                         
B528: 00              BRK                         
B529: 00              BRK                         
B52A: 00              BRK                         
B52B: 00              BRK                         
B52C: 00              BRK                         
B52D: 00              BRK                         
B52E: 00              BRK                         
B52F: 00              BRK                         
B530: 00              BRK                         
B531: 00              BRK                         
B532: 00              BRK                         
B533: 00              BRK                         
B534: 00              BRK                         
B535: 00              BRK                         
B536: 00              BRK                         
B537: 00              BRK                         
B538: 00              BRK                         
B539: 00              BRK                         
B53A: 00              BRK                         
B53B: 00              BRK                         
B53C: 00              BRK                         
B53D: 00              BRK                         
B53E: 00              BRK                         
B53F: 00              BRK                         
B540: 00              BRK                         
B541: 00              BRK                         
B542: 00              BRK                         
B543: 00              BRK                         
B544: 00              BRK                         
B545: 00              BRK                         
B546: 00              BRK                         
B547: 00              BRK                         
B548: 00              BRK                         
B549: 00              BRK                         
B54A: 00              BRK                         
B54B: 00              BRK                         
B54C: 00              BRK                         
B54D: 00              BRK                         
B54E: 00              BRK                         
B54F: 00              BRK                         
B550: 00              BRK                         
B551: 00              BRK                         
B552: 00              BRK                         
B553: 00              BRK                         
B554: 00              BRK                         
B555: 00              BRK                         
B556: 00              BRK                         
B557: 00              BRK                         
B558: 00              BRK                         
B559: 00              BRK                         
B55A: 00              BRK                         
B55B: 00              BRK                         
B55C: 00              BRK                         
B55D: 00              BRK                         
B55E: 00              BRK                         
B55F: 00              BRK                         
B560: 00              BRK                         
B561: 00              BRK                         
B562: 00              BRK                         
B563: 00              BRK                         
B564: 00              BRK                         
B565: 00              BRK                         
B566: 00              BRK                         
B567: 00              BRK                         
B568: 00              BRK                         
B569: 00              BRK                         
B56A: 00              BRK                         
B56B: 00              BRK                         
B56C: 00              BRK                         
B56D: 00              BRK                         
B56E: 00              BRK                         
B56F: 00              BRK                         
B570: 00              BRK                         
B571: 00              BRK                         
B572: 00              BRK                         
B573: 00              BRK                         
B574: 00              BRK                         
B575: 00              BRK                         
B576: 00              BRK                         
B577: 00              BRK                         
B578: 00              BRK                         
B579: 00              BRK                         
B57A: 00              BRK                         
B57B: 00              BRK                         
B57C: 00              BRK                         
B57D: 00              BRK                         
B57E: 00              BRK                         
B57F: 00              BRK                         
B580: 00              BRK                         
B581: 00              BRK                         
B582: 00              BRK                         
B583: 00              BRK                         
B584: 00              BRK                         
B585: 00              BRK                         
B586: 00              BRK                         
B587: 00              BRK                         
B588: 00              BRK                         
B589: 00              BRK                         
B58A: 00              BRK                         
B58B: 00              BRK                         
B58C: 00              BRK                         
B58D: 00              BRK                         
B58E: 00              BRK                         
B58F: 00              BRK                         
B590: 00              BRK                         
B591: 00              BRK                         
B592: 00              BRK                         
B593: 01 00           ORA     ($00,X)             ; {ram.GP_00}
B595: 00              BRK                         
B596: 00              BRK                         
B597: 00              BRK                         
B598: 00              BRK                         
B599: 00              BRK                         
B59A: 00              BRK                         
B59B: 00              BRK                         
B59C: 00              BRK                         
B59D: 00              BRK                         
B59E: 00              BRK                         
B59F: 00              BRK                         
B5A0: 00              BRK                         
B5A1: 00              BRK                         
B5A2: 00              BRK                         
B5A3: 00              BRK                         
B5A4: 00              BRK                         
B5A5: 00              BRK                         
B5A6: 00              BRK                         
B5A7: 00              BRK                         
B5A8: 00              BRK                         
B5A9: 00              BRK                         
B5AA: 00              BRK                         
B5AB: 00              BRK                         
B5AC: 00              BRK                         
B5AD: 00              BRK                         
B5AE: 00              BRK                         
B5AF: 00              BRK                         
B5B0: 00              BRK                         
B5B1: 00              BRK                         
B5B2: 00              BRK                         
B5B3: 00              BRK                         
B5B4: 00              BRK                         
B5B5: 00              BRK                         
B5B6: 00              BRK                         
B5B7: 00              BRK                         
B5B8: 00              BRK                         
B5B9: 00              BRK                         
B5BA: 00              BRK                         
B5BB: 00              BRK                         
B5BC: 00              BRK                         
B5BD: 00              BRK                         
B5BE: 00              BRK                         
B5BF: 00              BRK                         
B5C0: 00              BRK                         
B5C1: 00              BRK                         
B5C2: 00              BRK                         
B5C3: 00              BRK                         
B5C4: 00              BRK                         
B5C5: 00              BRK                         
B5C6: 00              BRK                         
B5C7: 00              BRK                         
B5C8: 00              BRK                         
B5C9: 00              BRK                         
B5CA: 00              BRK                         
B5CB: 00              BRK                         
B5CC: 00              BRK                         
B5CD: 00              BRK                         
B5CE: 00              BRK                         
B5CF: 00              BRK                         
B5D0: 00              BRK                         
B5D1: 00              BRK                         
B5D2: 00              BRK                         
B5D3: 00              BRK                         
B5D4: 00              BRK                         
B5D5: 00              BRK                         
B5D6: 00              BRK                         
B5D7: 00              BRK                         
B5D8: 00              BRK                         
B5D9: 00              BRK                         
B5DA: 00              BRK                         
B5DB: 00              BRK                         
B5DC: 00              BRK                         
B5DD: 00              BRK                         
B5DE: 00              BRK                         
B5DF: 00              BRK                         
B5E0: 00              BRK                         
B5E1: 00              BRK                         
B5E2: 00              BRK                         
B5E3: 00              BRK                         
B5E4: 00              BRK                         
B5E5: 00              BRK                         
B5E6: 00              BRK                         
B5E7: 00              BRK                         
B5E8: 00              BRK                         
B5E9: 00              BRK                         
B5EA: 00              BRK                         
B5EB: 00              BRK                         
B5EC: 00              BRK                         
B5ED: 00              BRK                         
B5EE: 00              BRK                         
B5EF: 00              BRK                         
B5F0: 00              BRK                         
B5F1: 00              BRK                         
B5F2: 00              BRK                         
B5F3: 00              BRK                         
B5F4: 00              BRK                         
B5F5: 00              BRK                         
B5F6: 00              BRK                         
B5F7: 00              BRK                         
B5F8: 00              BRK                         
B5F9: 00              BRK                         
B5FA: 00              BRK                         
B5FB: 00              BRK                         
B5FC: 00              BRK                         
B5FD: 00              BRK                         
B5FE: 00              BRK                         
B5FF: 00              BRK                         
B600: FF ; ????
B601: FF ; ????
B602: FF ; ????
B603: FF ; ????
B604: FF ; ????
B605: FF ; ????
B606: FF ; ????
B607: FF ; ????
B608: FF ; ????
B609: FF ; ????
B60A: FF ; ????
B60B: FF ; ????
B60C: FF ; ????
B60D: FF ; ????
B60E: FF ; ????
B60F: FF ; ????
B610: FF ; ????
B611: FF ; ????
B612: FF ; ????
B613: FF ; ????
B614: FF ; ????
B615: FF ; ????
B616: FF ; ????
B617: FF ; ????
B618: FF ; ????
B619: FF ; ????
B61A: FF ; ????
B61B: FF ; ????
B61C: FF ; ????
B61D: FF ; ????
B61E: FF ; ????
B61F: FF ; ????
B620: FF ; ????
B621: FF ; ????
B622: FF ; ????
B623: FF ; ????
B624: FF ; ????
B625: FF ; ????
B626: FF ; ????
B627: FF ; ????
B628: FF ; ????
B629: FF ; ????
B62A: FF ; ????
B62B: FF ; ????
B62C: FF ; ????
B62D: FF ; ????
B62E: FF ; ????
B62F: FF ; ????
B630: FF ; ????
B631: FF ; ????
B632: FF ; ????
B633: FF ; ????
B634: FF ; ????
B635: FF ; ????
B636: FF ; ????
B637: FF ; ????
B638: FF ; ????
B639: FF ; ????
B63A: FF ; ????
B63B: FF ; ????
B63C: FF ; ????
B63D: FF ; ????
B63E: FF ; ????
B63F: FF ; ????
B640: FF ; ????
B641: FF ; ????
B642: FF ; ????
B643: FF ; ????
B644: FF ; ????
B645: FF ; ????
B646: FF ; ????
B647: FF ; ????
B648: FF ; ????
B649: FF ; ????
B64A: FF ; ????
B64B: FF ; ????
B64C: FF ; ????
B64D: FF ; ????
B64E: FF ; ????
B64F: FF ; ????
B650: FF ; ????
B651: FF ; ????
B652: FF ; ????
B653: FF ; ????
B654: FF ; ????
B655: FF ; ????
B656: FF ; ????
B657: FF ; ????
B658: FF ; ????
B659: FF ; ????
B65A: FF ; ????
B65B: FF ; ????
B65C: FF ; ????
B65D: FF ; ????
B65E: FF ; ????
B65F: FF ; ????
B660: FF ; ????
B661: FF ; ????
B662: FF ; ????
B663: FF ; ????
B664: FF ; ????
B665: FF ; ????
B666: FF ; ????
B667: FF ; ????
B668: FF ; ????
B669: FF ; ????
B66A: FF ; ????
B66B: FF ; ????
B66C: FF ; ????
B66D: FF ; ????
B66E: FF ; ????
B66F: FF ; ????
B670: FF ; ????
B671: FF ; ????
B672: FF ; ????
B673: FF ; ????
B674: FF ; ????
B675: FF ; ????
B676: FF ; ????
B677: FF ; ????
B678: FF ; ????
B679: FF ; ????
B67A: FF ; ????
B67B: FF ; ????
B67C: FF ; ????
B67D: FF ; ????
B67E: FF ; ????
B67F: FF ; ????
B680: FF ; ????
B681: FF ; ????
B682: FF ; ????
B683: FF ; ????
B684: FF ; ????
B685: FF ; ????
B686: FF ; ????
B687: FF ; ????
B688: FF ; ????
B689: FF ; ????
B68A: FF ; ????
B68B: FF ; ????
B68C: FF ; ????
B68D: FF ; ????
B68E: FF ; ????
B68F: FF ; ????
B690: FF ; ????
B691: FF ; ????
B692: FF ; ????
B693: FF ; ????
B694: FF ; ????
B695: FF ; ????
B696: FF ; ????
B697: FF ; ????
B698: FF ; ????
B699: FF ; ????
B69A: FF ; ????
B69B: FF ; ????
B69C: FF ; ????
B69D: FF ; ????
B69E: FF ; ????
B69F: FF ; ????
B6A0: FF ; ????
B6A1: FF ; ????
B6A2: FF ; ????
B6A3: FF ; ????
B6A4: FF ; ????
B6A5: FF ; ????
B6A6: FF ; ????
B6A7: FF ; ????
B6A8: FF ; ????
B6A9: FF ; ????
B6AA: FF ; ????
B6AB: FF ; ????
B6AC: FF ; ????
B6AD: FF ; ????
B6AE: FF ; ????
B6AF: FF ; ????
B6B0: FF ; ????
B6B1: FF ; ????
B6B2: FF ; ????
B6B3: FF ; ????
B6B4: FF ; ????
B6B5: FF ; ????
B6B6: FF ; ????
B6B7: FF ; ????
B6B8: FF ; ????
B6B9: FF ; ????
B6BA: FF ; ????
B6BB: FF ; ????
B6BC: FF ; ????
B6BD: FF ; ????
B6BE: FF ; ????
B6BF: FF ; ????
B6C0: FF ; ????
B6C1: FF ; ????
B6C2: FF ; ????
B6C3: FF ; ????
B6C4: FF ; ????
B6C5: FF ; ????
B6C6: FF ; ????
B6C7: FF ; ????
B6C8: FF ; ????
B6C9: FF ; ????
B6CA: FF ; ????
B6CB: FF ; ????
B6CC: FF ; ????
B6CD: FF ; ????
B6CE: FF ; ????
B6CF: FF ; ????
B6D0: FF ; ????
B6D1: FF ; ????
B6D2: FF ; ????
B6D3: FF ; ????
B6D4: FF ; ????
B6D5: FF ; ????
B6D6: FF ; ????
B6D7: FF ; ????
B6D8: FF ; ????
B6D9: FF ; ????
B6DA: FF ; ????
B6DB: FF ; ????
B6DC: FF ; ????
B6DD: FF ; ????
B6DE: FF ; ????
B6DF: FF ; ????
B6E0: FF ; ????
B6E1: FF ; ????
B6E2: FF ; ????
B6E3: FF ; ????
B6E4: FF ; ????
B6E5: FF ; ????
B6E6: FF ; ????
B6E7: FF ; ????
B6E8: FF ; ????
B6E9: FF ; ????
B6EA: FF ; ????
B6EB: FF ; ????
B6EC: FF ; ????
B6ED: FF ; ????
B6EE: FF ; ????
B6EF: FF ; ????
B6F0: FF ; ????
B6F1: FF ; ????
B6F2: FF ; ????
B6F3: FF ; ????
B6F4: FF ; ????
B6F5: FF ; ????
B6F6: FF ; ????
B6F7: FF ; ????
B6F8: FF ; ????
B6F9: FF ; ????
B6FA: FF ; ????
B6FB: FF ; ????
B6FC: FF ; ????
B6FD: FF ; ????
B6FE: FF ; ????
B6FF: FF ; ????
B700: 00              BRK                         
B701: 00              BRK                         
B702: 00              BRK                         
B703: 00              BRK                         
B704: 00              BRK                         
B705: 00              BRK                         
B706: 00              BRK                         
B707: 00              BRK                         
B708: 00              BRK                         
B709: 00              BRK                         
B70A: 00              BRK                         
B70B: 00              BRK                         
B70C: 00              BRK                         
B70D: 00              BRK                         
B70E: 00              BRK                         
B70F: 00              BRK                         
B710: 00              BRK                         
B711: 00              BRK                         
B712: 00              BRK                         
B713: 00              BRK                         
B714: 00              BRK                         
B715: 00              BRK                         
B716: 00              BRK                         
B717: 00              BRK                         
B718: 00              BRK                         
B719: 00              BRK                         
B71A: 00              BRK                         
B71B: 00              BRK                         
B71C: 00              BRK                         
B71D: 00              BRK                         
B71E: 00              BRK                         
B71F: 00              BRK                         
B720: 00              BRK                         
B721: 00              BRK                         
B722: 00              BRK                         
B723: 00              BRK                         
B724: 00              BRK                         
B725: 00              BRK                         
B726: 00              BRK                         
B727: 00              BRK                         
B728: 00              BRK                         
B729: 00              BRK                         
B72A: 00              BRK                         
B72B: 00              BRK                         
B72C: 00              BRK                         
B72D: 00              BRK                         
B72E: 00              BRK                         
B72F: 00              BRK                         
B730: 00              BRK                         
B731: 00              BRK                         
B732: 00              BRK                         
B733: 00              BRK                         
B734: 00              BRK                         
B735: 00              BRK                         
B736: 00              BRK                         
B737: 00              BRK                         
B738: 00              BRK                         
B739: 00              BRK                         
B73A: 00              BRK                         
B73B: 00              BRK                         
B73C: 00              BRK                         
B73D: 00              BRK                         
B73E: 00              BRK                         
B73F: 00              BRK                         
B740: 00              BRK                         
B741: 00              BRK                         
B742: 00              BRK                         
B743: 00              BRK                         
B744: 00              BRK                         
B745: 00              BRK                         
B746: 00              BRK                         
B747: 00              BRK                         
B748: 00              BRK                         
B749: 00              BRK                         
B74A: 00              BRK                         
B74B: 00              BRK                         
B74C: 00              BRK                         
B74D: 00              BRK                         
B74E: 00              BRK                         
B74F: 00              BRK                         
B750: 00              BRK                         
B751: 00              BRK                         
B752: 00              BRK                         
B753: 00              BRK                         
B754: 00              BRK                         
B755: 00              BRK                         
B756: 00              BRK                         
B757: 00              BRK                         
B758: 00              BRK                         
B759: 00              BRK                         
B75A: 00              BRK                         
B75B: 00              BRK                         
B75C: 00              BRK                         
B75D: 00              BRK                         
B75E: 00              BRK                         
B75F: 00              BRK                         
B760: 00              BRK                         
B761: 00              BRK                         
B762: 00              BRK                         
B763: 00              BRK                         
B764: 00              BRK                         
B765: 00              BRK                         
B766: 00              BRK                         
B767: 00              BRK                         
B768: 00              BRK                         
B769: 00              BRK                         
B76A: 00              BRK                         
B76B: 00              BRK                         
B76C: 00              BRK                         
B76D: 00              BRK                         
B76E: 00              BRK                         
B76F: 00              BRK                         
B770: 00              BRK                         
B771: 00              BRK                         
B772: 00              BRK                         
B773: 00              BRK                         
B774: 00              BRK                         
B775: 00              BRK                         
B776: 00              BRK                         
B777: 00              BRK                         
B778: 00              BRK                         
B779: 00              BRK                         
B77A: 00              BRK                         
B77B: 00              BRK                         
B77C: 00              BRK                         
B77D: 00              BRK                         
B77E: 00              BRK                         
B77F: 00              BRK                         
B780: 00              BRK                         
B781: 00              BRK                         
B782: 00              BRK                         
B783: 00              BRK                         
B784: 00              BRK                         
B785: 00              BRK                         
B786: 00              BRK                         
B787: 00              BRK                         
B788: 00              BRK                         
B789: 00              BRK                         
B78A: 00              BRK                         
B78B: 00              BRK                         
B78C: 00              BRK                         
B78D: 00              BRK                         
B78E: 00              BRK                         
B78F: 00              BRK                         
B790: 00              BRK                         
B791: 00              BRK                         
B792: 00              BRK                         
B793: 00              BRK                         
B794: 00              BRK                         
B795: 00              BRK                         
B796: 00              BRK                         
B797: 00              BRK                         
B798: 00              BRK                         
B799: 00              BRK                         
B79A: 00              BRK                         
B79B: 00              BRK                         
B79C: 00              BRK                         
B79D: 00              BRK                         
B79E: 00              BRK                         
B79F: 00              BRK                         
B7A0: 00              BRK                         
B7A1: 00              BRK                         
B7A2: 00              BRK                         
B7A3: 00              BRK                         
B7A4: 00              BRK                         
B7A5: 00              BRK                         
B7A6: 00              BRK                         
B7A7: 00              BRK                         
B7A8: 00              BRK                         
B7A9: 00              BRK                         
B7AA: 00              BRK                         
B7AB: 00              BRK                         
B7AC: 00              BRK                         
B7AD: 00              BRK                         
B7AE: 00              BRK                         
B7AF: 00              BRK                         
B7B0: 00              BRK                         
B7B1: 00              BRK                         
B7B2: 00              BRK                         
B7B3: 00              BRK                         
B7B4: 00              BRK                         
B7B5: 00              BRK                         
B7B6: 00              BRK                         
B7B7: 00              BRK                         
B7B8: 00              BRK                         
B7B9: 00              BRK                         
B7BA: 00              BRK                         
B7BB: 00              BRK                         
B7BC: 00              BRK                         
B7BD: 00              BRK                         
B7BE: 00              BRK                         
B7BF: 00              BRK                         
B7C0: 00              BRK                         
B7C1: 00              BRK                         
B7C2: 00              BRK                         
B7C3: 00              BRK                         
B7C4: 00              BRK                         
B7C5: 00              BRK                         
B7C6: 00              BRK                         
B7C7: 00              BRK                         
B7C8: 00              BRK                         
B7C9: 00              BRK                         
B7CA: 00              BRK                         
B7CB: 00              BRK                         
B7CC: 00              BRK                         
B7CD: 00              BRK                         
B7CE: 00              BRK                         
B7CF: 00              BRK                         
B7D0: 00              BRK                         
B7D1: 00              BRK                         
B7D2: 00              BRK                         
B7D3: 00              BRK                         
B7D4: 00              BRK                         
B7D5: 00              BRK                         
B7D6: 00              BRK                         
B7D7: 00              BRK                         
B7D8: 00              BRK                         
B7D9: 00              BRK                         
B7DA: 00              BRK                         
B7DB: 00              BRK                         
B7DC: 00              BRK                         
B7DD: 00              BRK                         
B7DE: 00              BRK                         
B7DF: 00              BRK                         
B7E0: 00              BRK                         
B7E1: 00              BRK                         
B7E2: 00              BRK                         
B7E3: 00              BRK                         
B7E4: 00              BRK                         
B7E5: 00              BRK                         
B7E6: 00              BRK                         
B7E7: 00              BRK                         
B7E8: 00              BRK                         
B7E9: 00              BRK                         
B7EA: 00              BRK                         
B7EB: 00              BRK                         
B7EC: 00              BRK                         
B7ED: 00              BRK                         
B7EE: 00              BRK                         
B7EF: 00              BRK                         
B7F0: 00              BRK                         
B7F1: 00              BRK                         
B7F2: 00              BRK                         
B7F3: 00              BRK                         
B7F4: 00              BRK                         
B7F5: 00              BRK                         
B7F6: 00              BRK                         
B7F7: 00              BRK                         
B7F8: 00              BRK                         
B7F9: 00              BRK                         
B7FA: 00              BRK                         
B7FB: 00              BRK                         
B7FC: 00              BRK                         
B7FD: 00              BRK                         
B7FE: 00              BRK                         
B7FF: 00              BRK                         
B800: 60              RTS                         
B801: A9 02           LDA     #$02                
B803: 8D 2F 01        STA     $012F               
B806: 4C A9 B8        JMP     $B8A9               ; {}
B809: 00              BRK                         
B80A: 45 02           EOR     $02                 
B80C: 00              BRK                         
B80D: 00              BRK                         
B80E: 45 02           EOR     $02                 
B810: 08              PHP                         
B811: 08              PHP                         
B812: 03 ; ????
B813: 02 ; ????
B814: 00              BRK                         
B815: 08              PHP                         
B816: 03 ; ????
B817: 42 ; ????
B818: 08              PHP                         
B819: F8              SED                         
B81A: F6 02           INC     $02,X               
B81C: F8              SED                         
B81D: F8              SED                         
B81E: F7 ; ????
B81F: 02 ; ????
B820: 00              BRK                         
B821: F8              SED                         
B822: F7 ; ????
B823: 42 ; ????
B824: 08              PHP                         
B825: F8              SED                         
B826: F6 42           INC     $42,X               
B828: 10 00           BPL     $B82A               ; {}
B82A: CF ; ????
B82B: 02 ; ????
B82C: F8              SED                         
B82D: 00              BRK                         
B82E: CF ; ????
B82F: 42 ; ????
B830: 10 08           BPL     $B83A               ; {}
B832: CF ; ????
B833: 82 ; ????
B834: F8              SED                         
B835: 08              PHP                         
B836: CF ; ????
B837: C2 ; ????
B838: 10 10           BPL     $B84A               ; {}
B83A: F6 82           INC     $82,X               
B83C: F8              SED                         
B83D: 10 54           BPL     $B893               ; {}
B83F: 02 ; ????
B840: 00              BRK                         
B841: 10 54           BPL     $B897               ; {}
B843: 42 ; ????
B844: 08              PHP                         
B845: 10 F6           BPL     $B83D               ; {}
B847: C2 ; ????
B848: 10 00           BPL     $B84A               ; {}
B84A: 42 ; ????
B84B: 02 ; ????
B84C: 00              BRK                         
B84D: 00              BRK                         
B84E: 42 ; ????
B84F: 02 ; ????
B850: 08              PHP                         
B851: 08              PHP                         
B852: 02 ; ????
B853: 02 ; ????
B854: 00              BRK                         
B855: 08              PHP                         
B856: 02 ; ????
B857: 42 ; ????
B858: 08              PHP                         
B859: 00              BRK                         
B85A: F2 ; ????
B85B: 01 00           ORA     ($00,X)             ; {ram.GP_00}
B85D: 00              BRK                         
B85E: F3 ; ????
B85F: 01 08           ORA     ($08,X)             
B861: 08              PHP                         
B862: F4 ; ????
B863: 01 00           ORA     ($00,X)             ; {ram.GP_00}
B865: 08              PHP                         
B866: F5 01           SBC     $01,X               
B868: 08              PHP                         
B869: 00              BRK                         
B86A: 07 ; ????
B86B: 06 05           ASL     $05                 
B86D: 04 ; ????
B86E: 05 06           ORA     $06                 
B870: 07 ; ????
B871: 00              BRK                         
B872: 01 02           ORA     ($02,X)             
B874: 03 ; ????
B875: 04 ; ????
B876: 03 ; ????
B877: 02 ; ????
B878: 01 00           ORA     ($00,X)             ; {ram.GP_00}
B87A: 01 02           ORA     ($02,X)             
B87C: 01 00           ORA     ($00,X)             ; {ram.GP_00}
B87E: 07 ; ????
B87F: 06 07           ASL     $07                 
B881: 04 ; ????
B882: 03 ; ????
B883: 02 ; ????
B884: 03 ; ????
B885: 04 ; ????
B886: 05 06           ORA     $06                 
B888: 05 07           ORA     $07                 
B88A: 01 00           ORA     ($00,X)             ; {ram.GP_00}
B88C: 01 05           ORA     ($05,X)             
B88E: 03 ; ????
B88F: 04 ; ????
B890: 03 ; ????
B891: 06 02           ASL     $02                 
B893: 00              BRK                         
B894: 02 ; ????
B895: 05 03           ORA     $03                 
B897: 04 ; ????
B898: 03 ; ????
B899: FF ; ????
B89A: FF ; ????
B89B: 00              BRK                         
B89C: 01 01           ORA     ($01,X)             
B89E: 01 00           ORA     ($00,X)             ; {ram.GP_00}
B8A0: FF ; ????
B8A1: 00              BRK                         
B8A2: 01 01           ORA     ($01,X)             
B8A4: 01 00           ORA     ($00,X)             ; {ram.GP_00}
B8A6: FF ; ????
B8A7: FF ; ????
B8A8: FF ; ????
B8A9: A2 A0           LDX     #$A0                
B8AB: BD 01 07        LDA     $0701,X             
B8AE: 29 07           AND     #$07                
B8B0: 20 2B EE        JSR     $EE2B               
B8B3: BD B8 DC        LDA     $DCB8,X             
B8B6: B8              CLV                         
B8B7: E0 B8           CPX     #$B8                
B8B9: 36 BA           ROL     $BA,X               
B8BB: 85 BA           STA     $BA                 
B8BD: A9 10           LDA     #$10                
B8BF: 9D 00 07        STA     $0700,X             
B8C2: A9 D0           LDA     #$D0                
B8C4: 9D 03 07        STA     $0703,X             
B8C7: A9 00           LDA     #$00                
B8C9: 9D 06 07        STA     $0706,X             
B8CC: 9D 08 07        STA     $0708,X             
B8CF: A9 80           LDA     #$80                
B8D1: 9D 01 07        STA     $0701,X             
B8D4: A9 05           LDA     #$05                
B8D6: 9D 07 07        STA     $0707,X             
B8D9: 20 3C B9        JSR     $B93C               ; {}
B8DC: FE 01 07        INC     $0701,X             
B8DF: 60              RTS                         
B8E0: BD 08 07        LDA     $0708,X             
B8E3: F0 03           BEQ     $B8E8               ; {}
B8E5: DE 08 07        DEC     $0708,X             
B8E8: FE 06 07        INC     $0706,X             
B8EB: D0 03           BNE     $B8F0               ; {}
B8ED: 20 D0 B9        JSR     $B9D0               ; {}
B8F0: 20 12 B9        JSR     $B912               ; {}
B8F3: 20 4A B9        JSR     $B94A               ; {}
B8F6: 20 65 B9        JSR     $B965               ; {}
B8F9: 20 83 B9        JSR     $B983               ; {}
B8FC: 20 B3 B9        JSR     $B9B3               ; {}
B8FF: A2 50           LDX     #$50                
B901: 20 06 B9        JSR     $B906               ; {}
B904: A2 60           LDX     #$60                
B906: BD 01 07        LDA     $0701,X             
B909: 29 07           AND     #$07                
B90B: 20 2B EE        JSR     $EE2B               
B90E: 4B ; ????
B90F: BA              TSX                         
B910: AD BA A0        LDA     $A0BA               ; {}
B913: 00              BRK                         
B914: BD 03 07        LDA     $0703,X             
B917: C9 E0           CMP     #$E0                
B919: B0 12           BCS     $B92D               ; {}
B91B: C8              INY                         
B91C: C9 08           CMP     #$08                
B91E: 90 0D           BCC     $B92D               ; {}
B920: C8              INY                         
B921: BD 00 07        LDA     $0700,X             
B924: C9 A0           CMP     #$A0                
B926: B0 05           BCS     $B92D               ; {}
B928: C8              INY                         
B929: C9 08           CMP     #$08                
B92B: B0 B2           BCS     $B8DF               ; {}
B92D: 98              TYA                         
B92E: 0A              ASL     A                   
B92F: 0A              ASL     A                   
B930: 0A              ASL     A                   
B931: 18              CLC                         
B932: 7D 07 07        ADC     $0707,X             
B935: A8              TAY                         
B936: B9 69 B8        LDA     $B869,Y             ; {}
B939: 9D 07 07        STA     $0707,X             
B93C: A8              TAY                         
B93D: B9 99 B8        LDA     $B899,Y             ; {}
B940: 9D 05 07        STA     $0705,X             
B943: B9 A1 B8        LDA     $B8A1,Y             ; {}
B946: 9D 04 07        STA     $0704,X             
B949: 60              RTS                         
B94A: A5 14           LDA     $14                 
B94C: 29 01           AND     #$01                
B94E: D0 14           BNE     $B964               ; {}
B950: 18              CLC                         
B951: BD 00 07        LDA     $0700,X             
B954: 7D 05 07        ADC     $0705,X             
B957: 9D 00 07        STA     $0700,X             
B95A: 18              CLC                         
B95B: BD 03 07        LDA     $0703,X             
B95E: 7D 04 07        ADC     $0704,X             
B961: 9D 03 07        STA     $0703,X             
B964: 60              RTS                         
B965: A9 0F           LDA     #$0F                
B967: 48              PHA                         
B968: A0 00           LDY     #$00                
B96A: BD 06 07        LDA     $0706,X             
B96D: 29 10           AND     #$10                
B96F: A8              TAY                         
B970: 68              PLA                         
B971: 85 00           STA     $00                 ; {ram.GP_00}
B973: 84 01           STY     $01                 
B975: A9 09           LDA     #$09                
B977: 85 08           STA     $08                 
B979: A9 B8           LDA     #$B8                
B97B: 85 09           STA     $09                 
B97D: A5 01           LDA     $01                 
B97F: 20 AB 9B        JSR     $9BAB               ; {}
B982: 60              RTS                         
B983: 86 00           STX     $00                 ; {ram.GP_00}
B985: BD 08 07        LDA     $0708,X             
B988: F0 0B           BEQ     $B995               ; {}
B98A: DE 08 07        DEC     $0708,X             
B98D: A5 14           LDA     $14                 
B98F: 29 02           AND     #$02                
B991: F0 08           BEQ     $B99B               ; {}
B993: D0 0C           BNE     $B9A1               ; {}
B995: A5 14           LDA     $14                 
B997: 29 80           AND     #$80                
B999: D0 06           BNE     $B9A1               ; {}
B99B: A9 0F           LDA     #$0F                
B99D: AA              TAX                         
B99E: A8              TAY                         
B99F: D0 06           BNE     $B9A7               ; {}
B9A1: A9 11           LDA     #$11                
B9A3: A2 24           LDX     #$24                
B9A5: A0 32           LDY     #$32                
B9A7: 8D A9 03        STA     $03A9               
B9AA: 8E AA 03        STX     $03AA               
B9AD: 8C AB 03        STY     $03AB               
B9B0: A6 00           LDX     $00                 ; {ram.GP_00}
B9B2: 60              RTS                         
B9B3: 20 90 D9        JSR     $D990               
B9B6: B0 12           BCS     $B9CA               ; {}
B9B8: A9 40           LDA     #$40                
B9BA: 9D 08 07        STA     $0708,X             
B9BD: 20 DA B9        JSR     $B9DA               ; {}
B9C0: A9 F8           LDA     #$F8                
B9C2: 99 00 07        STA     $0700,Y             
B9C5: A9 08           LDA     #$08                
B9C7: 8D 83 03        STA     $0383               
B9CA: 20 F7 97        JSR     $97F7               ; {}
B9CD: 4C 09 DA        JMP     $DA09               
B9D0: A5 EF           LDA     $EF                 
B9D2: 29 07           AND     #$07                
B9D4: 9D 07 07        STA     $0707,X             
B9D7: 4C 3C B9        JMP     $B93C               ; {}
B9DA: A5 3C           LDA     $3C                 
B9DC: D0 08           BNE     $B9E6               ; {}
B9DE: C0 38           CPY     #$38                
B9E0: F0 08           BEQ     $B9EA               ; {}
B9E2: C0 3C           CPY     #$3C                
B9E4: F0 04           BEQ     $B9EA               ; {}
B9E6: A9 05           LDA     #$05                
B9E8: D0 06           BNE     $B9F0               ; {}
B9EA: 18              CLC                         
B9EB: AD 52 01        LDA     $0152               
B9EE: 69 01           ADC     #$01                
B9F0: 85 00           STA     $00                 ; {ram.GP_00}
B9F2: A5 6B           LDA     $6B                 
B9F4: 38              SEC                         
B9F5: E5 00           SBC     $00                 ; {ram.GP_00}
B9F7: 90 05           BCC     $B9FE               ; {}
B9F9: F0 03           BEQ     $B9FE               ; {}
B9FB: 85 6B           STA     $6B                 
B9FD: 60              RTS                         
B9FE: A9 00           LDA     #$00                
BA00: 85 6B           STA     $6B                 
BA02: A9 80           LDA     #$80                
BA04: 20 E1 E2        JSR     $E2E1               
BA07: 20 F0 E2        JSR     $E2F0               
BA0A: A9 80           LDA     #$80                
BA0C: 9D 06 07        STA     $0706,X             
BA0F: 20 DC B8        JSR     $B8DC               ; {}
BA12: A9 F0           LDA     #$F0                
BA14: 8D 75 01        STA     $0175               
BA17: A9 01           LDA     #$01                
BA19: 8D 76 01        STA     $0176               
BA1C: A9 05           LDA     #$05                
BA1E: 8D 74 01        STA     $0174               
BA21: A9 10           LDA     #$10                
BA23: 20 34 9A        JSR     $9A34               ; {}
BA26: A9 50           LDA     #$50                
BA28: 85 08           STA     $08                 
BA2A: 85 0A           STA     $0A                 
BA2C: A0 20           LDY     #$20                
BA2E: 20 6D 9A        JSR     $9A6D               ; {}
BA31: A0 20           LDY     #$20                
BA33: 4C 7D 9A        JMP     $9A7D               ; {}
BA36: AD 74 01        LDA     $0174               
BA39: F0 03           BEQ     $BA3E               ; {}
BA3B: 4C 86 9A        JMP     $9A86               ; {}
BA3E: A9 00           LDA     #$00                
BA40: 9D 06 07        STA     $0706,X             
BA43: FE 01 07        INC     $0701,X             
BA46: A9 68           LDA     #$68                
BA48: 4C E0 D2        JMP     $D2E0               
BA4B: A5 14           LDA     $14                 
BA4D: A8              TAY                         
BA4E: 29 1F           AND     #$1F                
BA50: D0 32           BNE     $BA84               ; {}
BA52: E0 50           CPX     #$50                
BA54: F0 07           BEQ     $BA5D               ; {}
BA56: 98              TYA                         
BA57: 29 20           AND     #$20                
BA59: D0 29           BNE     $BA84               ; {}
BA5B: F0 05           BEQ     $BA62               ; {}
BA5D: 98              TYA                         
BA5E: 29 20           AND     #$20                
BA60: F0 22           BEQ     $BA84               ; {}
BA62: A9 00           LDA     #$00                
BA64: 9D 06 07        STA     $0706,X             
BA67: A0 A0           LDY     #$A0                
BA69: B9 00 07        LDA     $0700,Y             
BA6C: 9D 00 07        STA     $0700,X             
BA6F: B9 03 07        LDA     $0703,Y             
BA72: 9D 03 07        STA     $0703,X             
BA75: A9 81           LDA     #$81                
BA77: 9D 01 07        STA     $0701,X             
BA7A: A5 EF           LDA     $EF                 
BA7C: 29 07           AND     #$07                
BA7E: 9D 07 07        STA     $0707,X             
BA81: 20 3C B9        JSR     $B93C               ; {}
BA84: 60              RTS                         
BA85: DE 06 07        DEC     $0706,X             
BA88: D0 FA           BNE     $BA84               ; {}
BA8A: A9 F8           LDA     #$F8                
BA8C: 9D 00 07        STA     $0700,X             
BA8F: 9D 00 02        STA     $0200,X             
BA92: 9D 08 02        STA     $0208,X             
BA95: 20 DC B8        JSR     $B8DC               ; {}
BA98: A9 01           LDA     #$01                
BA9A: 8D 55 01        STA     $0155               
BA9D: 85 20           STA     $20                 
BA9F: A0 29           LDY     #$29                
BAA1: A9 00           LDA     #$00                
BAA3: 85 3A           STA     $3A                 
BAA5: 8D 2F 01        STA     $012F               
BAA8: A9 04           LDA     #$04                
BAAA: 4C 90 CA        JMP     $CA90               
BAAD: FE 06 07        INC     $0706,X             
BAB0: D0 03           BNE     $BAB5               ; {}
BAB2: 20 D0 B9        JSR     $B9D0               ; {}
BAB5: 20 12 B9        JSR     $B912               ; {}
BAB8: 20 50 B9        JSR     $B950               ; {}
BABB: 20 C1 BA        JSR     $BAC1               ; {}
BABE: 4C CA B9        JMP     $B9CA               ; {}
BAC1: A0 50           LDY     #$50                
BAC3: A9 03           LDA     #$03                
BAC5: 4C 71 B9        JMP     $B971               ; {}
BAC8: FF ; ????
BAC9: FF ; ????
BACA: FF ; ????
BACB: FF ; ????
BACC: FF ; ????
BACD: FF ; ????
BACE: FF ; ????
BACF: FF ; ????
BAD0: FF ; ????
BAD1: FF ; ????
BAD2: FF ; ????
BAD3: FF ; ????
BAD4: FF ; ????
BAD5: FF ; ????
BAD6: FF ; ????
BAD7: FF ; ????
BAD8: FF ; ????
BAD9: FF ; ????
BADA: FF ; ????
BADB: FF ; ????
BADC: FF ; ????
BADD: FF ; ????
BADE: FF ; ????
BADF: FF ; ????
BAE0: FF ; ????
BAE1: FF ; ????
BAE2: FF ; ????
BAE3: FF ; ????
BAE4: FF ; ????
BAE5: FF ; ????
BAE6: FF ; ????
BAE7: FF ; ????
BAE8: FF ; ????
BAE9: FF ; ????
BAEA: FF ; ????
BAEB: FF ; ????
BAEC: FF ; ????
BAED: FF ; ????
BAEE: FF ; ????
BAEF: FF ; ????
BAF0: FF ; ????
BAF1: FF ; ????
BAF2: FF ; ????
BAF3: FF ; ????
BAF4: FF ; ????
BAF5: FF ; ????
BAF6: FF ; ????
BAF7: FF ; ????
BAF8: FF ; ????
BAF9: FF ; ????
BAFA: FF ; ????
BAFB: FF ; ????
BAFC: FF ; ????
BAFD: FF ; ????
BAFE: FF ; ????
BAFF: FF ; ????
BB00: 00              BRK                         
BB01: 00              BRK                         
BB02: 00              BRK                         
BB03: 00              BRK                         
BB04: 00              BRK                         
BB05: 00              BRK                         
BB06: 00              BRK                         
BB07: 00              BRK                         
BB08: 00              BRK                         
BB09: 00              BRK                         
BB0A: 00              BRK                         
BB0B: 00              BRK                         
BB0C: 00              BRK                         
BB0D: 00              BRK                         
BB0E: 00              BRK                         
BB0F: 00              BRK                         
BB10: 00              BRK                         
BB11: 00              BRK                         
BB12: 00              BRK                         
BB13: 00              BRK                         
BB14: 00              BRK                         
BB15: 00              BRK                         
BB16: 00              BRK                         
BB17: 00              BRK                         
BB18: 00              BRK                         
BB19: 00              BRK                         
BB1A: 00              BRK                         
BB1B: 00              BRK                         
BB1C: 00              BRK                         
BB1D: 00              BRK                         
BB1E: 00              BRK                         
BB1F: 00              BRK                         
BB20: 00              BRK                         
BB21: 00              BRK                         
BB22: 00              BRK                         
BB23: 00              BRK                         
BB24: 00              BRK                         
BB25: 00              BRK                         
BB26: 00              BRK                         
BB27: 00              BRK                         
BB28: 00              BRK                         
BB29: 00              BRK                         
BB2A: 00              BRK                         
BB2B: 00              BRK                         
BB2C: 00              BRK                         
BB2D: 00              BRK                         
BB2E: 00              BRK                         
BB2F: 00              BRK                         
BB30: 00              BRK                         
BB31: 00              BRK                         
BB32: 00              BRK                         
BB33: 00              BRK                         
BB34: 00              BRK                         
BB35: 00              BRK                         
BB36: 00              BRK                         
BB37: 00              BRK                         
BB38: 00              BRK                         
BB39: 00              BRK                         
BB3A: 00              BRK                         
BB3B: 00              BRK                         
BB3C: 00              BRK                         
BB3D: 00              BRK                         
BB3E: 00              BRK                         
BB3F: 00              BRK                         
BB40: 00              BRK                         
BB41: 00              BRK                         
BB42: 00              BRK                         
BB43: 00              BRK                         
BB44: 00              BRK                         
BB45: 00              BRK                         
BB46: 00              BRK                         
BB47: 00              BRK                         
BB48: 00              BRK                         
BB49: 00              BRK                         
BB4A: 00              BRK                         
BB4B: 00              BRK                         
BB4C: 00              BRK                         
BB4D: 00              BRK                         
BB4E: 00              BRK                         
BB4F: 00              BRK                         
BB50: 00              BRK                         
BB51: 00              BRK                         
BB52: 00              BRK                         
BB53: 00              BRK                         
BB54: 00              BRK                         
BB55: 00              BRK                         
BB56: 00              BRK                         
BB57: 00              BRK                         
BB58: 00              BRK                         
BB59: 00              BRK                         
BB5A: 00              BRK                         
BB5B: 00              BRK                         
BB5C: 00              BRK                         
BB5D: 00              BRK                         
BB5E: 00              BRK                         
BB5F: 00              BRK                         
BB60: 00              BRK                         
BB61: 00              BRK                         
BB62: 00              BRK                         
BB63: 00              BRK                         
BB64: 00              BRK                         
BB65: 00              BRK                         
BB66: 00              BRK                         
BB67: 00              BRK                         
BB68: 00              BRK                         
BB69: 00              BRK                         
BB6A: 00              BRK                         
BB6B: 00              BRK                         
BB6C: 00              BRK                         
BB6D: 00              BRK                         
BB6E: 00              BRK                         
BB6F: 00              BRK                         
BB70: 00              BRK                         
BB71: 00              BRK                         
BB72: 00              BRK                         
BB73: 00              BRK                         
BB74: 00              BRK                         
BB75: 00              BRK                         
BB76: 00              BRK                         
BB77: 00              BRK                         
BB78: 00              BRK                         
BB79: 00              BRK                         
BB7A: 00              BRK                         
BB7B: 00              BRK                         
BB7C: 00              BRK                         
BB7D: 00              BRK                         
BB7E: 00              BRK                         
BB7F: 00              BRK                         
BB80: 00              BRK                         
BB81: 00              BRK                         
BB82: 00              BRK                         
BB83: 00              BRK                         
BB84: 00              BRK                         
BB85: 00              BRK                         
BB86: 00              BRK                         
BB87: 00              BRK                         
BB88: 00              BRK                         
BB89: 00              BRK                         
BB8A: 00              BRK                         
BB8B: 00              BRK                         
BB8C: 00              BRK                         
BB8D: 00              BRK                         
BB8E: 00              BRK                         
BB8F: 00              BRK                         
BB90: 00              BRK                         
BB91: 00              BRK                         
BB92: 00              BRK                         
BB93: 00              BRK                         
BB94: 00              BRK                         
BB95: 00              BRK                         
BB96: 00              BRK                         
BB97: 00              BRK                         
BB98: 00              BRK                         
BB99: 00              BRK                         
BB9A: 00              BRK                         
BB9B: 00              BRK                         
BB9C: 00              BRK                         
BB9D: 00              BRK                         
BB9E: 00              BRK                         
BB9F: 00              BRK                         
BBA0: 00              BRK                         
BBA1: 00              BRK                         
BBA2: 00              BRK                         
BBA3: 00              BRK                         
BBA4: 00              BRK                         
BBA5: 00              BRK                         
BBA6: 00              BRK                         
BBA7: 00              BRK                         
BBA8: 00              BRK                         
BBA9: 00              BRK                         
BBAA: 00              BRK                         
BBAB: 00              BRK                         
BBAC: 00              BRK                         
BBAD: 00              BRK                         
BBAE: 00              BRK                         
BBAF: 00              BRK                         
BBB0: 00              BRK                         
BBB1: 00              BRK                         
BBB2: 00              BRK                         
BBB3: 00              BRK                         
BBB4: 00              BRK                         
BBB5: 00              BRK                         
BBB6: 00              BRK                         
BBB7: 00              BRK                         
BBB8: 00              BRK                         
BBB9: 00              BRK                         
BBBA: 00              BRK                         
BBBB: 00              BRK                         
BBBC: 00              BRK                         
BBBD: 00              BRK                         
BBBE: 00              BRK                         
BBBF: 00              BRK                         
BBC0: 00              BRK                         
BBC1: 00              BRK                         
BBC2: 00              BRK                         
BBC3: 00              BRK                         
BBC4: 00              BRK                         
BBC5: 00              BRK                         
BBC6: 00              BRK                         
BBC7: 00              BRK                         
BBC8: 00              BRK                         
BBC9: 00              BRK                         
BBCA: 00              BRK                         
BBCB: 00              BRK                         
BBCC: 00              BRK                         
BBCD: 00              BRK                         
BBCE: 00              BRK                         
BBCF: 00              BRK                         
BBD0: 00              BRK                         
BBD1: 00              BRK                         
BBD2: 00              BRK                         
BBD3: 00              BRK                         
BBD4: 00              BRK                         
BBD5: 00              BRK                         
BBD6: 00              BRK                         
BBD7: 00              BRK                         
BBD8: 00              BRK                         
BBD9: 00              BRK                         
BBDA: 00              BRK                         
BBDB: 00              BRK                         
BBDC: 00              BRK                         
BBDD: 00              BRK                         
BBDE: 00              BRK                         
BBDF: 00              BRK                         
BBE0: 00              BRK                         
BBE1: 00              BRK                         
BBE2: 00              BRK                         
BBE3: 00              BRK                         
BBE4: 00              BRK                         
BBE5: 00              BRK                         
BBE6: 00              BRK                         
BBE7: 00              BRK                         
BBE8: 00              BRK                         
BBE9: 00              BRK                         
BBEA: 00              BRK                         
BBEB: 00              BRK                         
BBEC: 00              BRK                         
BBED: 00              BRK                         
BBEE: 00              BRK                         
BBEF: 00              BRK                         
BBF0: 00              BRK                         
BBF1: 00              BRK                         
BBF2: 00              BRK                         
BBF3: 00              BRK                         
BBF4: 00              BRK                         
BBF5: 00              BRK                         
BBF6: 00              BRK                         
BBF7: 00              BRK                         
BBF8: 00              BRK                         
BBF9: CC 00 14        CPY     $1400               
BBFC: 20 21 00        JSR     $0021               
BBFF: 00              BRK                         
BC00: FF ; ????
BC01: FF ; ????
BC02: FF ; ????
BC03: FF ; ????
BC04: FF ; ????
BC05: FF ; ????
BC06: FF ; ????
BC07: FF ; ????
BC08: FF ; ????
BC09: FF ; ????
BC0A: FF ; ????
BC0B: FF ; ????
BC0C: FF ; ????
BC0D: FF ; ????
BC0E: FF ; ????
BC0F: FF ; ????
BC10: FF ; ????
BC11: FF ; ????
BC12: FF ; ????
BC13: FF ; ????
BC14: FF ; ????
BC15: BF ; ????
BC16: FF ; ????
BC17: FF ; ????
BC18: FF ; ????
BC19: FF ; ????
BC1A: FF ; ????
BC1B: FF ; ????
BC1C: FF ; ????
BC1D: FF ; ????
BC1E: FF ; ????
BC1F: FF ; ????
BC20: FF ; ????
BC21: FF ; ????
BC22: FF ; ????
BC23: FF ; ????
BC24: FF ; ????
BC25: FF ; ????
BC26: FF ; ????
BC27: FF ; ????
BC28: FF ; ????
BC29: FF ; ????
BC2A: FF ; ????
BC2B: FF ; ????
BC2C: FF ; ????
BC2D: FF ; ????
BC2E: FF ; ????
BC2F: FF ; ????
BC30: FF ; ????
BC31: FF ; ????
BC32: FF ; ????
BC33: FF ; ????
BC34: FF ; ????
BC35: FF ; ????
BC36: FF ; ????
BC37: FF ; ????
BC38: FF ; ????
BC39: FF ; ????
BC3A: FF ; ????
BC3B: FF ; ????
BC3C: FF ; ????
BC3D: FF ; ????
BC3E: FF ; ????
BC3F: FF ; ????
BC40: FF ; ????
BC41: FF ; ????
BC42: FF ; ????
BC43: FF ; ????
BC44: FF ; ????
BC45: FF ; ????
BC46: FF ; ????
BC47: FF ; ????
BC48: FF ; ????
BC49: FF ; ????
BC4A: FF ; ????
BC4B: FF ; ????
BC4C: FF ; ????
BC4D: FF ; ????
BC4E: FF ; ????
BC4F: FF ; ????
BC50: FF ; ????
BC51: FF ; ????
BC52: FF ; ????
BC53: FF ; ????
BC54: FF ; ????
BC55: FF ; ????
BC56: FF ; ????
BC57: FF ; ????
BC58: FF ; ????
BC59: FF ; ????
BC5A: FF ; ????
BC5B: FF ; ????
BC5C: FF ; ????
BC5D: FF ; ????
BC5E: FF ; ????
BC5F: FF ; ????
BC60: FF ; ????
BC61: FF ; ????
BC62: FF ; ????
BC63: FF ; ????
BC64: FF ; ????
BC65: FF ; ????
BC66: FF ; ????
BC67: FF ; ????
BC68: FF ; ????
BC69: FF ; ????
BC6A: FF ; ????
BC6B: FF ; ????
BC6C: FF ; ????
BC6D: FF ; ????
BC6E: FF ; ????
BC6F: FF ; ????
BC70: FF ; ????
BC71: FF ; ????
BC72: FF ; ????
BC73: FF ; ????
BC74: FF ; ????
BC75: FF ; ????
BC76: FF ; ????
BC77: FF ; ????
BC78: FF ; ????
BC79: FF ; ????
BC7A: FF ; ????
BC7B: FF ; ????
BC7C: FF ; ????
BC7D: FF ; ????
BC7E: FF ; ????
BC7F: FF ; ????
BC80: FF ; ????
BC81: FF ; ????
BC82: FF ; ????
BC83: FF ; ????
BC84: FF ; ????
BC85: FF ; ????
BC86: FF ; ????
BC87: FF ; ????
BC88: FF ; ????
BC89: FF ; ????
BC8A: FF ; ????
BC8B: FF ; ????
BC8C: FF ; ????
BC8D: FF ; ????
BC8E: FF ; ????
BC8F: FF ; ????
BC90: FF ; ????
BC91: FF ; ????
BC92: FF ; ????
BC93: FF ; ????
BC94: FF ; ????
BC95: FF ; ????
BC96: FF ; ????
BC97: FF ; ????
BC98: FF ; ????
BC99: FF ; ????
BC9A: FF ; ????
BC9B: FF ; ????
BC9C: FF ; ????
BC9D: FF ; ????
BC9E: FF ; ????
BC9F: FF ; ????
BCA0: FF ; ????
BCA1: FF ; ????
BCA2: FF ; ????
BCA3: FF ; ????
BCA4: FF ; ????
BCA5: FF ; ????
BCA6: FF ; ????
BCA7: FF ; ????
BCA8: FF ; ????
BCA9: FF ; ????
BCAA: FF ; ????
BCAB: FF ; ????
BCAC: FF ; ????
BCAD: FF ; ????
BCAE: FF ; ????
BCAF: FF ; ????
BCB0: FF ; ????
BCB1: FF ; ????
BCB2: FF ; ????
BCB3: FF ; ????
BCB4: FF ; ????
BCB5: FF ; ????
BCB6: FF ; ????
BCB7: FF ; ????
BCB8: FF ; ????
BCB9: FF ; ????
BCBA: FF ; ????
BCBB: FF ; ????
BCBC: FF ; ????
BCBD: FF ; ????
BCBE: FF ; ????
BCBF: FF ; ????
BCC0: FF ; ????
BCC1: FF ; ????
BCC2: FF ; ????
BCC3: FF ; ????
BCC4: FF ; ????
BCC5: FF ; ????
BCC6: FF ; ????
BCC7: FF ; ????
BCC8: FF ; ????
BCC9: FF ; ????
BCCA: FF ; ????
BCCB: FF ; ????
BCCC: FF ; ????
BCCD: FF ; ????
BCCE: FF ; ????
BCCF: FF ; ????
BCD0: FF ; ????
BCD1: FF ; ????
BCD2: FF ; ????
BCD3: FF ; ????
BCD4: FF ; ????
BCD5: FF ; ????
BCD6: FF ; ????
BCD7: FF ; ????
BCD8: FF ; ????
BCD9: FF ; ????
BCDA: FF ; ????
BCDB: FF ; ????
BCDC: FF ; ????
BCDD: FF ; ????
BCDE: FF ; ????
BCDF: FF ; ????
BCE0: FF ; ????
BCE1: FF ; ????
BCE2: FF ; ????
BCE3: FF ; ????
BCE4: FF ; ????
BCE5: FF ; ????
BCE6: FF ; ????
BCE7: FF ; ????
BCE8: FF ; ????
BCE9: FF ; ????
BCEA: FF ; ????
BCEB: FF ; ????
BCEC: FF ; ????
BCED: FF ; ????
BCEE: FF ; ????
BCEF: FF ; ????
BCF0: FF ; ????
BCF1: FF ; ????
BCF2: FF ; ????
BCF3: FF ; ????
BCF4: FF ; ????
BCF5: FF ; ????
BCF6: FF ; ????
BCF7: FF ; ????
BCF8: FF ; ????
BCF9: FF ; ????
BCFA: FF ; ????
BCFB: FF ; ????
BCFC: FF ; ????
BCFD: FF ; ????
BCFE: FF ; ????
BCFF: FF ; ????
BD00: 00              BRK                         
BD01: 00              BRK                         
BD02: 00              BRK                         
BD03: 00              BRK                         
BD04: 00              BRK                         
BD05: 00              BRK                         
BD06: 00              BRK                         
BD07: 00              BRK                         
BD08: 00              BRK                         
BD09: 00              BRK                         
BD0A: 00              BRK                         
BD0B: 00              BRK                         
BD0C: 00              BRK                         
BD0D: 00              BRK                         
BD0E: 00              BRK                         
BD0F: 00              BRK                         
BD10: 00              BRK                         
BD11: 00              BRK                         
BD12: 00              BRK                         
BD13: 00              BRK                         
BD14: 00              BRK                         
BD15: 00              BRK                         
BD16: 00              BRK                         
BD17: 00              BRK                         
BD18: 00              BRK                         
BD19: 00              BRK                         
BD1A: 00              BRK                         
BD1B: 00              BRK                         
BD1C: 00              BRK                         
BD1D: 00              BRK                         
BD1E: 00              BRK                         
BD1F: 00              BRK                         
BD20: 00              BRK                         
BD21: 00              BRK                         
BD22: 00              BRK                         
BD23: 00              BRK                         
BD24: 00              BRK                         
BD25: 00              BRK                         
BD26: 00              BRK                         
BD27: 00              BRK                         
BD28: 00              BRK                         
BD29: 00              BRK                         
BD2A: 00              BRK                         
BD2B: 00              BRK                         
BD2C: 00              BRK                         
BD2D: 00              BRK                         
BD2E: 00              BRK                         
BD2F: 00              BRK                         
BD30: 00              BRK                         
BD31: 00              BRK                         
BD32: 00              BRK                         
BD33: 00              BRK                         
BD34: 00              BRK                         
BD35: 00              BRK                         
BD36: 00              BRK                         
BD37: 00              BRK                         
BD38: 00              BRK                         
BD39: 00              BRK                         
BD3A: 00              BRK                         
BD3B: 00              BRK                         
BD3C: 00              BRK                         
BD3D: 00              BRK                         
BD3E: 00              BRK                         
BD3F: 00              BRK                         
BD40: 00              BRK                         
BD41: 00              BRK                         
BD42: 00              BRK                         
BD43: 00              BRK                         
BD44: 00              BRK                         
BD45: 00              BRK                         
BD46: 00              BRK                         
BD47: 00              BRK                         
BD48: 00              BRK                         
BD49: 00              BRK                         
BD4A: 00              BRK                         
BD4B: 00              BRK                         
BD4C: 00              BRK                         
BD4D: 00              BRK                         
BD4E: 00              BRK                         
BD4F: 00              BRK                         
BD50: 00              BRK                         
BD51: 00              BRK                         
BD52: 00              BRK                         
BD53: 00              BRK                         
BD54: 00              BRK                         
BD55: 00              BRK                         
BD56: 00              BRK                         
BD57: 00              BRK                         
BD58: 00              BRK                         
BD59: 00              BRK                         
BD5A: 00              BRK                         
BD5B: 00              BRK                         
BD5C: 00              BRK                         
BD5D: 00              BRK                         
BD5E: 00              BRK                         
BD5F: 00              BRK                         
BD60: 00              BRK                         
BD61: 00              BRK                         
BD62: 00              BRK                         
BD63: 00              BRK                         
BD64: 00              BRK                         
BD65: 00              BRK                         
BD66: 00              BRK                         
BD67: 00              BRK                         
BD68: 00              BRK                         
BD69: 00              BRK                         
BD6A: 00              BRK                         
BD6B: 00              BRK                         
BD6C: 00              BRK                         
BD6D: 00              BRK                         
BD6E: 00              BRK                         
BD6F: 00              BRK                         
BD70: 00              BRK                         
BD71: 00              BRK                         
BD72: 00              BRK                         
BD73: 00              BRK                         
BD74: 00              BRK                         
BD75: 00              BRK                         
BD76: 00              BRK                         
BD77: 00              BRK                         
BD78: 00              BRK                         
BD79: 00              BRK                         
BD7A: 00              BRK                         
BD7B: 00              BRK                         
BD7C: 00              BRK                         
BD7D: 00              BRK                         
BD7E: 00              BRK                         
BD7F: 00              BRK                         
BD80: 00              BRK                         
BD81: 00              BRK                         
BD82: 00              BRK                         
BD83: 00              BRK                         
BD84: 00              BRK                         
BD85: 00              BRK                         
BD86: 00              BRK                         
BD87: 00              BRK                         
BD88: 00              BRK                         
BD89: 00              BRK                         
BD8A: 00              BRK                         
BD8B: 00              BRK                         
BD8C: 00              BRK                         
BD8D: 00              BRK                         
BD8E: 00              BRK                         
BD8F: 00              BRK                         
BD90: 00              BRK                         
BD91: 00              BRK                         
BD92: 00              BRK                         
BD93: 00              BRK                         
BD94: 00              BRK                         
BD95: 00              BRK                         
BD96: 00              BRK                         
BD97: 00              BRK                         
BD98: 00              BRK                         
BD99: 00              BRK                         
BD9A: 00              BRK                         
BD9B: 00              BRK                         
BD9C: 00              BRK                         
BD9D: 00              BRK                         
BD9E: 00              BRK                         
BD9F: 00              BRK                         
BDA0: 00              BRK                         
BDA1: 00              BRK                         
BDA2: 00              BRK                         
BDA3: 00              BRK                         
BDA4: 00              BRK                         
BDA5: 00              BRK                         
BDA6: 00              BRK                         
BDA7: 00              BRK                         
BDA8: 00              BRK                         
BDA9: 00              BRK                         
BDAA: 00              BRK                         
BDAB: 00              BRK                         
BDAC: 00              BRK                         
BDAD: 00              BRK                         
BDAE: 00              BRK                         
BDAF: 00              BRK                         
BDB0: 00              BRK                         
BDB1: 00              BRK                         
BDB2: 00              BRK                         
BDB3: 00              BRK                         
BDB4: 00              BRK                         
BDB5: 00              BRK                         
BDB6: 00              BRK                         
BDB7: 00              BRK                         
BDB8: 00              BRK                         
BDB9: 00              BRK                         
BDBA: 00              BRK                         
BDBB: 00              BRK                         
BDBC: 00              BRK                         
BDBD: 00              BRK                         
BDBE: 00              BRK                         
BDBF: 00              BRK                         
BDC0: 00              BRK                         
BDC1: 00              BRK                         
BDC2: 00              BRK                         
BDC3: 00              BRK                         
BDC4: 00              BRK                         
BDC5: 00              BRK                         
BDC6: 00              BRK                         
BDC7: 00              BRK                         
BDC8: 00              BRK                         
BDC9: 00              BRK                         
BDCA: 00              BRK                         
BDCB: 00              BRK                         
BDCC: 00              BRK                         
BDCD: 00              BRK                         
BDCE: 00              BRK                         
BDCF: 00              BRK                         
BDD0: 00              BRK                         
BDD1: 00              BRK                         
BDD2: 00              BRK                         
BDD3: 00              BRK                         
BDD4: 00              BRK                         
BDD5: 00              BRK                         
BDD6: 00              BRK                         
BDD7: 00              BRK                         
BDD8: 00              BRK                         
BDD9: 00              BRK                         
BDDA: 00              BRK                         
BDDB: 00              BRK                         
BDDC: 00              BRK                         
BDDD: 00              BRK                         
BDDE: 00              BRK                         
BDDF: 00              BRK                         
BDE0: 00              BRK                         
BDE1: 00              BRK                         
BDE2: 00              BRK                         
BDE3: 00              BRK                         
BDE4: 00              BRK                         
BDE5: 00              BRK                         
BDE6: 00              BRK                         
BDE7: 00              BRK                         
BDE8: 00              BRK                         
BDE9: 00              BRK                         
BDEA: 00              BRK                         
BDEB: 00              BRK                         
BDEC: 00              BRK                         
BDED: 00              BRK                         
BDEE: 00              BRK                         
BDEF: 00              BRK                         
BDF0: 00              BRK                         
BDF1: 00              BRK                         
BDF2: 00              BRK                         
BDF3: 00              BRK                         
BDF4: 00              BRK                         
BDF5: 00              BRK                         
BDF6: 00              BRK                         
BDF7: 00              BRK                         
BDF8: 00              BRK                         
BDF9: 00              BRK                         
BDFA: 00              BRK                         
BDFB: 00              BRK                         
BDFC: 00              BRK                         
BDFD: 00              BRK                         
BDFE: 00              BRK                         
BDFF: 00              BRK                         
BE00: FF ; ????
BE01: FF ; ????
BE02: FF ; ????
BE03: FF ; ????
BE04: FF ; ????
BE05: FF ; ????
BE06: FF ; ????
BE07: FF ; ????
BE08: FF ; ????
BE09: FF ; ????
BE0A: FF ; ????
BE0B: FF ; ????
BE0C: FF ; ????
BE0D: FF ; ????
BE0E: FF ; ????
BE0F: FF ; ????
BE10: FF ; ????
BE11: FF ; ????
BE12: FF ; ????
BE13: FF ; ????
BE14: FF ; ????
BE15: FF ; ????
BE16: FF ; ????
BE17: FF ; ????
BE18: FF ; ????
BE19: FF ; ????
BE1A: FF ; ????
BE1B: FF ; ????
BE1C: FF ; ????
BE1D: FF ; ????
BE1E: FF ; ????
BE1F: FF ; ????
BE20: FF ; ????
BE21: FF ; ????
BE22: FF ; ????
BE23: FF ; ????
BE24: FF ; ????
BE25: FF ; ????
BE26: FF ; ????
BE27: FF ; ????
BE28: FF ; ????
BE29: FF ; ????
BE2A: FF ; ????
BE2B: FF ; ????
BE2C: FF ; ????
BE2D: FF ; ????
BE2E: FF ; ????
BE2F: FF ; ????
BE30: FF ; ????
BE31: FF ; ????
BE32: FF ; ????
BE33: FF ; ????
BE34: FF ; ????
BE35: FF ; ????
BE36: FF ; ????
BE37: FF ; ????
BE38: FF ; ????
BE39: FF ; ????
BE3A: FF ; ????
BE3B: FF ; ????
BE3C: FF ; ????
BE3D: FF ; ????
BE3E: FF ; ????
BE3F: FF ; ????
BE40: FF ; ????
BE41: FF ; ????
BE42: FF ; ????
BE43: FF ; ????
BE44: FF ; ????
BE45: FF ; ????
BE46: FF ; ????
BE47: FF ; ????
BE48: FF ; ????
BE49: FF ; ????
BE4A: FF ; ????
BE4B: FF ; ????
BE4C: FF ; ????
BE4D: FF ; ????
BE4E: FF ; ????
BE4F: FF ; ????
BE50: FF ; ????
BE51: FF ; ????
BE52: FF ; ????
BE53: FF ; ????
BE54: FF ; ????
BE55: FF ; ????
BE56: FF ; ????
BE57: FF ; ????
BE58: FF ; ????
BE59: FF ; ????
BE5A: FF ; ????
BE5B: FF ; ????
BE5C: FF ; ????
BE5D: FF ; ????
BE5E: FF ; ????
BE5F: FF ; ????
BE60: FF ; ????
BE61: FF ; ????
BE62: FF ; ????
BE63: FF ; ????
BE64: FF ; ????
BE65: FF ; ????
BE66: FF ; ????
BE67: FF ; ????
BE68: FF ; ????
BE69: FF ; ????
BE6A: FF ; ????
BE6B: FF ; ????
BE6C: FF ; ????
BE6D: FF ; ????
BE6E: FF ; ????
BE6F: FF ; ????
BE70: FF ; ????
BE71: FF ; ????
BE72: FF ; ????
BE73: FF ; ????
BE74: FF ; ????
BE75: FF ; ????
BE76: FF ; ????
BE77: FF ; ????
BE78: FF ; ????
BE79: FF ; ????
BE7A: FF ; ????
BE7B: FF ; ????
BE7C: FF ; ????
BE7D: FF ; ????
BE7E: FF ; ????
BE7F: FF ; ????
BE80: FF ; ????
BE81: FF ; ????
BE82: FF ; ????
BE83: FF ; ????
BE84: FF ; ????
BE85: FF ; ????
BE86: FF ; ????
BE87: FF ; ????
BE88: FF ; ????
BE89: FF ; ????
BE8A: FF ; ????
BE8B: FF ; ????
BE8C: FF ; ????
BE8D: FF ; ????
BE8E: FF ; ????
BE8F: FF ; ????
BE90: FF ; ????
BE91: FF ; ????
BE92: FF ; ????
BE93: FF ; ????
BE94: FF ; ????
BE95: FF ; ????
BE96: FF ; ????
BE97: FF ; ????
BE98: FF ; ????
BE99: FF ; ????
BE9A: FF ; ????
BE9B: FF ; ????
BE9C: FF ; ????
BE9D: FF ; ????
BE9E: FF ; ????
BE9F: FF ; ????
BEA0: FF ; ????
BEA1: FF ; ????
BEA2: FF ; ????
BEA3: FF ; ????
BEA4: FF ; ????
BEA5: FF ; ????
BEA6: FF ; ????
BEA7: FF ; ????
BEA8: FF ; ????
BEA9: FF ; ????
BEAA: FF ; ????
BEAB: FF ; ????
BEAC: FF ; ????
BEAD: FF ; ????
BEAE: FF ; ????
BEAF: FF ; ????
BEB0: FF ; ????
BEB1: FF ; ????
BEB2: FF ; ????
BEB3: FF ; ????
BEB4: FF ; ????
BEB5: FF ; ????
BEB6: FF ; ????
BEB7: FF ; ????
BEB8: FF ; ????
BEB9: FF ; ????
BEBA: FF ; ????
BEBB: FF ; ????
BEBC: FF ; ????
BEBD: FF ; ????
BEBE: FF ; ????
BEBF: FF ; ????
BEC0: FF ; ????
BEC1: FF ; ????
BEC2: FF ; ????
BEC3: FF ; ????
BEC4: FF ; ????
BEC5: FF ; ????
BEC6: FF ; ????
BEC7: FF ; ????
BEC8: FF ; ????
BEC9: FF ; ????
BECA: FF ; ????
BECB: FF ; ????
BECC: FF ; ????
BECD: FF ; ????
BECE: FF ; ????
BECF: FF ; ????
BED0: FF ; ????
BED1: FF ; ????
BED2: FF ; ????
BED3: FF ; ????
BED4: FF ; ????
BED5: FF ; ????
BED6: FF ; ????
BED7: FF ; ????
BED8: FF ; ????
BED9: FF ; ????
BEDA: FF ; ????
BEDB: FF ; ????
BEDC: FF ; ????
BEDD: FF ; ????
BEDE: FF ; ????
BEDF: FF ; ????
BEE0: FF ; ????
BEE1: FF ; ????
BEE2: FF ; ????
BEE3: FF ; ????
BEE4: FF ; ????
BEE5: FF ; ????
BEE6: FF ; ????
BEE7: FF ; ????
BEE8: FF ; ????
BEE9: FF ; ????
BEEA: FF ; ????
BEEB: FF ; ????
BEEC: FF ; ????
BEED: FF ; ????
BEEE: FF ; ????
BEEF: FF ; ????
BEF0: FF ; ????
BEF1: FF ; ????
BEF2: FF ; ????
BEF3: FF ; ????
BEF4: FF ; ????
BEF5: FF ; ????
BEF6: FF ; ????
BEF7: FF ; ????
BEF8: FF ; ????
BEF9: FF ; ????
BEFA: FF ; ????
BEFB: FF ; ????
BEFC: FF ; ????
BEFD: FF ; ????
BEFE: FF ; ????
BEFF: FF ; ????
BF00: 00              BRK                         
BF01: 00              BRK                         
BF02: 00              BRK                         
BF03: 00              BRK                         
BF04: 00              BRK                         
BF05: 00              BRK                         
BF06: 00              BRK                         
BF07: 00              BRK                         
BF08: 00              BRK                         
BF09: 00              BRK                         
BF0A: 00              BRK                         
BF0B: 00              BRK                         
BF0C: 00              BRK                         
BF0D: 00              BRK                         
BF0E: 00              BRK                         
BF0F: 00              BRK                         
BF10: 00              BRK                         
BF11: 00              BRK                         
BF12: 00              BRK                         
BF13: 00              BRK                         
BF14: 00              BRK                         
BF15: 00              BRK                         
BF16: 00              BRK                         
BF17: 00              BRK                         
BF18: 00              BRK                         
BF19: 00              BRK                         
BF1A: 00              BRK                         
BF1B: 00              BRK                         
BF1C: 00              BRK                         
BF1D: 00              BRK                         
BF1E: 00              BRK                         
BF1F: 00              BRK                         
BF20: 00              BRK                         
BF21: 00              BRK                         
BF22: 00              BRK                         
BF23: 00              BRK                         
BF24: 00              BRK                         
BF25: 00              BRK                         
BF26: 00              BRK                         
BF27: 00              BRK                         
BF28: 00              BRK                         
BF29: 00              BRK                         
BF2A: 00              BRK                         
BF2B: 00              BRK                         
BF2C: 00              BRK                         
BF2D: 00              BRK                         
BF2E: 00              BRK                         
BF2F: 00              BRK                         
BF30: 00              BRK                         
BF31: 00              BRK                         
BF32: 00              BRK                         
BF33: 00              BRK                         
BF34: 00              BRK                         
BF35: 00              BRK                         
BF36: 00              BRK                         
BF37: 00              BRK                         
BF38: 00              BRK                         
BF39: 00              BRK                         
BF3A: 00              BRK                         
BF3B: 00              BRK                         
BF3C: 00              BRK                         
BF3D: 00              BRK                         
BF3E: 00              BRK                         
BF3F: 00              BRK                         
BF40: 00              BRK                         
BF41: 00              BRK                         
BF42: 00              BRK                         
BF43: 00              BRK                         
BF44: 00              BRK                         
BF45: 00              BRK                         
BF46: 00              BRK                         
BF47: 00              BRK                         
BF48: 00              BRK                         
BF49: 00              BRK                         
BF4A: 00              BRK                         
BF4B: 00              BRK                         
BF4C: 00              BRK                         
BF4D: 00              BRK                         
BF4E: 00              BRK                         
BF4F: 00              BRK                         
BF50: 00              BRK                         
BF51: 00              BRK                         
BF52: 00              BRK                         
BF53: 00              BRK                         
BF54: 00              BRK                         
BF55: 00              BRK                         
BF56: 00              BRK                         
BF57: 00              BRK                         
BF58: 00              BRK                         
BF59: 00              BRK                         
BF5A: 00              BRK                         
BF5B: 00              BRK                         
BF5C: 00              BRK                         
BF5D: 00              BRK                         
BF5E: 00              BRK                         
BF5F: 00              BRK                         
BF60: 00              BRK                         
BF61: 00              BRK                         
BF62: 00              BRK                         
BF63: 00              BRK                         
BF64: 00              BRK                         
BF65: 00              BRK                         
BF66: 00              BRK                         
BF67: 00              BRK                         
BF68: 00              BRK                         
BF69: 00              BRK                         
BF6A: 00              BRK                         
BF6B: 00              BRK                         
BF6C: 00              BRK                         
BF6D: 00              BRK                         
BF6E: 00              BRK                         
BF6F: 00              BRK                         
BF70: 00              BRK                         
BF71: 00              BRK                         
BF72: 00              BRK                         
BF73: 00              BRK                         
BF74: 00              BRK                         
BF75: 00              BRK                         
BF76: 00              BRK                         
BF77: 00              BRK                         
BF78: 00              BRK                         
BF79: 00              BRK                         
BF7A: 00              BRK                         
BF7B: 00              BRK                         
BF7C: 00              BRK                         
BF7D: 00              BRK                         
BF7E: 00              BRK                         
BF7F: 00              BRK                         
BF80: 00              BRK                         
BF81: 00              BRK                         
BF82: 00              BRK                         
BF83: 00              BRK                         
BF84: 00              BRK                         
BF85: 00              BRK                         
BF86: 00              BRK                         
BF87: 00              BRK                         
BF88: 00              BRK                         
BF89: 00              BRK                         
BF8A: 00              BRK                         
BF8B: 00              BRK                         
BF8C: 00              BRK                         
BF8D: 00              BRK                         
BF8E: 00              BRK                         
BF8F: 00              BRK                         
BF90: 00              BRK                         
BF91: 00              BRK                         
BF92: 00              BRK                         
BF93: 00              BRK                         
BF94: 00              BRK                         
BF95: 00              BRK                         
BF96: 00              BRK                         
BF97: 00              BRK                         
BF98: 00              BRK                         
BF99: 00              BRK                         
BF9A: 00              BRK                         
BF9B: 00              BRK                         
BF9C: 00              BRK                         
BF9D: 00              BRK                         
BF9E: 00              BRK                         
BF9F: 00              BRK                         
BFA0: 00              BRK                         
BFA1: 00              BRK                         
BFA2: 00              BRK                         
BFA3: 00              BRK                         
BFA4: 00              BRK                         
BFA5: 00              BRK                         
BFA6: 00              BRK                         
BFA7: 00              BRK                         
BFA8: 00              BRK                         
BFA9: 00              BRK                         
BFAA: 00              BRK                         
BFAB: 00              BRK                         
BFAC: 00              BRK                         
BFAD: 00              BRK                         
BFAE: 00              BRK                         
BFAF: 00              BRK                         
BFB0: 00              BRK                         
BFB1: 00              BRK                         
BFB2: 00              BRK                         
BFB3: 00              BRK                         
BFB4: 00              BRK                         
BFB5: 00              BRK                         
BFB6: 00              BRK                         
BFB7: 00              BRK                         
BFB8: 00              BRK                         
BFB9: 00              BRK                         
BFBA: 00              BRK                         
BFBB: 00              BRK                         
BFBC: 00              BRK                         
BFBD: 00              BRK                         
BFBE: 00              BRK                         
BFBF: 00              BRK                         
BFC0: 00              BRK                         
BFC1: 00              BRK                         
BFC2: 00              BRK                         
BFC3: 00              BRK                         
BFC4: 00              BRK                         
BFC5: 00              BRK                         
BFC6: 00              BRK                         
BFC7: 00              BRK                         
BFC8: 00              BRK                         
BFC9: 00              BRK                         
BFCA: 00              BRK                         
BFCB: 00              BRK                         
BFCC: 00              BRK                         
BFCD: 00              BRK                         
BFCE: 00              BRK                         
BFCF: 00              BRK                         
BFD0: 00              BRK                         
BFD1: 00              BRK                         
BFD2: 00              BRK                         
BFD3: 00              BRK                         
BFD4: 00              BRK                         
BFD5: 00              BRK                         
BFD6: 00              BRK                         
BFD7: 00              BRK                         
BFD8: 00              BRK                         
BFD9: 00              BRK                         
BFDA: 00              BRK                         
BFDB: 00              BRK                         
BFDC: 00              BRK                         
BFDD: 00              BRK                         
BFDE: 00              BRK                         
BFDF: 00              BRK                         
BFE0: 00              BRK                         
BFE1: 00              BRK                         
BFE2: 00              BRK                         
BFE3: 00              BRK                         
BFE4: 00              BRK                         
BFE5: 00              BRK                         
BFE6: 00              BRK                         
BFE7: 00              BRK                         
BFE8: 00              BRK                         
BFE9: 00              BRK                         
BFEA: 00              BRK                         
BFEB: 00              BRK                         
BFEC: 00              BRK                         
BFED: 00              BRK                         
BFEE: 00              BRK                         
BFEF: 00              BRK                         
BFF0: 00              BRK                         
BFF1: 00              BRK                         
BFF2: 00              BRK                         
BFF3: 00              BRK                         
BFF4: 00              BRK                         
BFF5: 00              BRK                         
BFF6: 00              BRK                         
BFF7: 00              BRK                         
BFF8: 80 ; ????
BFF9: 60              RTS                         
BFFA: 08              PHP                         
BFFB: 80 ; ????
BFFC: 10 00           BPL     $BFFE               ; {}
BFFE: 00              BRK                         
BFFF: 01 ; ????
```

