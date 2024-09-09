![Bank 2](KidIcarus.jpg)

# Bank 2

>>> cpu 6502

>>> binary 8000:roms/KidIcarus.nes[8010:C010]

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](Hardware.md)

```code
8000: 4C 5A 80        JMP     $805A               ; {}
8003: 4C D5 80        JMP     $80D5               ; {}
8006: 4C CF 96        JMP     $96CF               ; {}
8009: 4C 40 DF        JMP     $DF40               
800C: 4C 11 94        JMP     $9411               ; {}
800F: 4C 3C 94        JMP     $943C               ; {}
8012: 4C 94 93        JMP     $9394               ; {}
8015: 4C C5 80        JMP     $80C5               ; {}
8018: 4C 48 99        JMP     $9948               ; {}
801B: 4C 9E 85        JMP     $859E               ; {}
801E: 4C C5 80        JMP     $80C5               ; {}
8021: 4C 7B 93        JMP     $937B               ; {}
8024: 4C 8E 80        JMP     $808E               ; {}
8027: 4C 96 81        JMP     $8196               ; {}
802A: 4C 63 81        JMP     $8163               ; {}
802D: 4C 22 97        JMP     $9722               ; {}
8030: 4C 71 97        JMP     $9771               ; {}
8033: 4C 6D 95        JMP     $956D               ; {}
8036: 4C 3E 96        JMP     $963E               ; {}
8039: 4C 1D 95        JMP     $951D               ; {}
803C: 4C 37 95        JMP     $9537               ; {}
803F: 4C 85 85        JMP     $8585               ; {}
8042: 67 ; ????
8043: C5 E7           CMP     $E7                 
8045: C5 AA           CMP     $AA                 
8047: 81 EA           STA     ($EA,X)             
8049: 81 12           STA     ($12,X)             
804B: 82 ; ????
804C: 2A              ROL     A                   
804D: 82 ; ????
804E: 4A              LSR     A                   
804F: 82 ; ????
8050: 56 82           LSR     $82,X               
8052: 56 82           LSR     $82,X               
8054: 56 83           LSR     $83,X               
8056: C9 EF           CMP     #$EF                
8058: 40              RTI                         
8059: 7E 20 07        ROR     $0720,X             
805C: EB ; ????
805D: 20 F0 EE        JSR     $EEF0               
8060: 20 E5 EE        JSR     $EEE5               
8063: A9 00           LDA     #$00                
8065: 8D 2F 01        STA     $012F               
8068: 20 2A C4        JSR     $C42A               
806B: 20 20 EF        JSR     $EF20               
806E: 20 21 7F        JSR     $7F21               
8071: 20 42 EE        JSR     $EE42               
8074: 20 2E EF        JSR     $EF2E               
8077: 20 CA EE        JSR     $EECA               
807A: 20 E5 EE        JSR     $EEE5               
807D: A9 08           LDA     #$08                
807F: 20 90 CA        JSR     $CA90               
8082: 20 63 81        JSR     $8163               ; {}
8085: 20 53 C4        JSR     $C453               
8088: 20 3D C8        JSR     $C83D               
808B: 20 70 CB        JSR     $CB70               
808E: A9 60           LDA     #$60                
8090: 85 43           STA     $43                 
8092: 20 01 EF        JSR     $EF01               
8095: 20 21 EB        JSR     $EB21               
8098: 24 AB           BIT     $AB                 
809A: 70 13           BVS     $80AF               ; {}
809C: 30 14           BMI     $80B2               ; {}
809E: 20 98 E1        JSR     $E198               
80A1: 20 D7 EA        JSR     $EAD7               
80A4: 20 C8 94        JSR     $94C8               ; {}
80A7: 4C 95 80        JMP     $8095               ; {}
80AA: E6 A0           INC     $A0                 
80AC: 4C 6D C0        JMP     $C06D               
80AF: 4C A0 C0        JMP     $C0A0               
80B2: 20 F0 EE        JSR     $EEF0               
80B5: 20 89 EA        JSR     $EA89               
80B8: EE 30 01        INC     $0130               
80BB: AD 30 01        LDA     $0130               
80BE: C9 03           CMP     #$03                
80C0: B0 E8           BCS     $80AA               ; {}
80C2: 4C 68 80        JMP     $8068               ; {}
80C5: 60              RTS                         
80C6: 20 9B EE        JSR     $EE9B               
80C9: 20 0E EE        JSR     $EE0E               
80CC: 20 B8 EE        JSR     $EEB8               
80CF: 4C 1E 81        JMP     $811E               ; {}
80D2: 4C 34 81        JMP     $8134               ; {}
80D5: 8A              TXA                         
80D6: 48              PHA                         
80D7: 98              TYA                         
80D8: 48              PHA                         
80D9: A5 45           LDA     $45                 
80DB: D0 F5           BNE     $80D2               ; {}
80DD: E6 45           INC     $45                 
80DF: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
80E2: 20 2E EB        JSR     $EB2E               
80E5: A5 38           LDA     $38                 
80E7: D0 DD           BNE     $80C6               ; {}
80E9: A5 37           LDA     $37                 
80EB: D0 4C           BNE     $8139               ; {}
80ED: 8D 01 20        STA     $2001               ; {hard.P_CNTRL_2}
80F0: 20 6A 94        JSR     $946A               ; {}
80F3: 20 C9 EB        JSR     $EBC9               
80F6: A5 FF           LDA     $FF                 
80F8: 8D 01 20        STA     $2001               ; {hard.P_CNTRL_2}
80FB: 20 6D 95        JSR     $956D               ; {}
80FE: 20 3E 96        JSR     $963E               ; {}
8101: 20 9B EE        JSR     $EE9B               
8104: 20 75 81        JSR     $8175               ; {}
8107: 20 D9 EC        JSR     $ECD9               
810A: 20 B8 EE        JSR     $EEB8               
810D: 20 F0 94        JSR     $94F0               ; {}
8110: A5 5C           LDA     $5C                 
8112: 10 0A           BPL     $811E               ; {}
8114: A9 00           LDA     #$00                
8116: 85 3F           STA     $3F                 
8118: 85 40           STA     $40                 
811A: 85 41           STA     $41                 
811C: 85 42           STA     $42                 
811E: 20 5D E1        JSR     $E15D               
8121: 20 E0 C3        JSR     $C3E0               
8124: 20 53 C4        JSR     $C453               
8127: 20 6A EE        JSR     $EE6A               
812A: 20 94 EE        JSR     $EE94               
812D: 20 56 C8        JSR     $C856               
8130: A9 00           LDA     #$00                
8132: 85 45           STA     $45                 
8134: 68              PLA                         
8135: A8              TAY                         
8136: 68              PLA                         
8137: AA              TAX                         
8138: 60              RTS                         
8139: 4A              LSR     A                   
813A: B0 E2           BCS     $811E               ; {}
813C: 4A              LSR     A                   
813D: B0 06           BCS     $8145               ; {}
813F: 20 42 EE        JSR     $EE42               
8142: 4C F3 80        JMP     $80F3               ; {}
8145: A9 0A           LDA     #$0A                
8147: 20 90 CA        JSR     $CA90               
814A: A9 0C           LDA     #$0C                
814C: 20 90 CA        JSR     $CA90               
814F: 20 C9 EB        JSR     $EBC9               
8152: 20 9B EE        JSR     $EE9B               
8155: A9 02           LDA     #$02                
8157: 20 90 CA        JSR     $CA90               
815A: 20 D9 EC        JSR     $ECD9               
815D: 20 B8 EE        JSR     $EEB8               
8160: 4C 1E 81        JMP     $811E               ; {}
8163: 20 96 81        JSR     $8196               ; {}
8166: 20 43 D3        JSR     $D343               
8169: 20 F3 91        JSR     $91F3               ; {}
816C: 20 BB 8E        JSR     $8EBB               ; {}
816F: 20 29 86        JSR     $8629               ; {}
8172: 4C 26 84        JMP     $8426               ; {}
8175: 20 B6 CB        JSR     $CBB6               
8178: 20 D9 C3        JSR     $C3D9               
817B: AD 21 07        LDA     $0721               
817E: 29 70           AND     #$70                
8180: D0 B6           BNE     $8138               ; {}
8182: 20 A2 D4        JSR     $D4A2               
8185: 20 F4 91        JSR     $91F4               ; {}
8188: 20 BC 8E        JSR     $8EBC               ; {}
818B: 20 2A 86        JSR     $862A               ; {}
818E: 20 34 84        JSR     $8434               ; {}
8191: A2 F0           LDX     #$F0                
8193: 4C 75 91        JMP     $9175               ; {}
8196: A2 20           LDX     #$20                
8198: A9 AA           LDA     #$AA                
819A: 9D 00 07        STA     $0700,X             
819D: A9 80           LDA     #$80                
819F: 9D 02 07        STA     $0702,X             
81A2: A9 20           LDA     #$20                
81A4: 9D 03 07        STA     $0703,X             
81A7: 4C BF C3        JMP     $C3BF               
81AA: 02 ; ????
81AB: 70 71           BVS     $821E               ; {}
81AD: 72 ; ????
81AE: 73 ; ????
81AF: 74 ; ????
81B0: 75 00           ADC     $00,X               ; {ram.GP_00}
81B2: 42 ; ????
81B3: 71 70           ADC     ($70),Y             
81B5: 73 ; ????
81B6: 72 ; ????
81B7: 75 74           ADC     $74,X               
81B9: 00              BRK                         
81BA: 02 ; ????
81BB: 70 71           BVS     $822E               ; {}
81BD: 72 ; ????
81BE: 73 ; ????
81BF: 76 77           ROR     $77,X               
81C1: 00              BRK                         
81C2: 42 ; ????
81C3: 71 70           ADC     ($70),Y             
81C5: 73 ; ????
81C6: 72 ; ????
81C7: 77 ; ????
81C8: 76 00           ROR     $00,X               ; {ram.GP_00}
81CA: 02 ; ????
81CB: B0 B1           BCS     $817E               ; {}
81CD: B2 ; ????
81CE: B3 ; ????
81CF: B4 B5           LDY     $B5,X               
81D1: 00              BRK                         
81D2: 42 ; ????
81D3: B1 B0           LDA     ($B0),Y             
81D5: B3 ; ????
81D6: B2 ; ????
81D7: B5 B4           LDA     $B4,X               
81D9: 00              BRK                         
81DA: 02 ; ????
81DB: B0 B1           BCS     $818E               ; {}
81DD: B2 ; ????
81DE: B3 ; ????
81DF: B6 B7           LDX     $B7,Y               
81E1: 00              BRK                         
81E2: 42 ; ????
81E3: B1 B0           LDA     ($B0),Y             
81E5: B3 ; ????
81E6: B2 ; ????
81E7: B7 ; ????
81E8: B6 00           LDX     $00,Y               ; {ram.GP_00}
81EA: 4B ; ????
81EB: 4B ; ????
81EC: 4B ; ????
81ED: 4B ; ????
81EE: 5A ; ????
81EF: 5A ; ????
81F0: 5A ; ????
81F1: 5A ; ????
81F2: 4A              LSR     A                   
81F3: 4A              LSR     A                   
81F4: 4A              LSR     A                   
81F5: 4A              LSR     A                   
81F6: 95 5F           STA     $5F,X               
81F8: 96 5F           STX     $5F,Y               
81FA: 9B ; ????
81FB: 5F ; ????
81FC: 9C ; ????
81FD: 5F ; ????
81FE: 3F ; ????
81FF: 5F ; ????
8200: 4F ; ????
8201: 5F ; ????
8202: 48              PHA                         
8203: 5F ; ????
8204: 58              CLI                         
8205: 5F ; ????
8206: 49 5F           EOR     #$5F                
8208: 59 5F AA        EOR     $AA5F,Y             ; {}
820B: 5F ; ????
820C: AB ; ????
820D: 5F ; ????
820E: 34 ; ????
820F: 5F ; ????
8210: 55 5F           EOR     $5F,X               
8212: 16 17           ASL     $17,X               
8214: 90 91           BCC     $81A7               ; {}
8216: 17 ; ????
8217: 16 91           ASL     $91,X               
8219: 90 00           BCC     $821B               ; {}
821B: 00              BRK                         
821C: 00              BRK                         
821D: 00              BRK                         
821E: 00              BRK                         
821F: 00              BRK                         
8220: 00              BRK                         
8221: 00              BRK                         
8222: 78              SEI                         
8223: 79 7A 7B        ADC     $7B7A,Y             
8226: 79 78 7B        ADC     $7B78,Y             
8229: 7A ; ????
822A: C0 C1           CPY     #$C1                
822C: C2 ; ????
822D: C3 ; ????
822E: C1 C0           CMP     ($C0,X)             
8230: C3 ; ????
8231: C2 ; ????
8232: C4 C5           CPY     $C5                 
8234: C6 C7           DEC     $C7                 
8236: C5 C4           CMP     $C4                 
8238: C7 ; ????
8239: C6 C8           DEC     $C8                 
823B: C9 CA           CMP     #$CA                
823D: CB ; ????
823E: C9 C8           CMP     #$C8                
8240: CB ; ????
8241: CA              DEX                         
8242: D0 D1           BNE     $8215               ; {}
8244: D2 ; ????
8245: D3 ; ????
8246: D1 D0           CMP     ($D0),Y             
8248: D3 ; ????
8249: D2 ; ????
824A: 9F ; ????
824B: 5F ; ????
824C: AF ; ????
824D: 5F ; ????
824E: 8E 5F 8F        STX     $8F5F               ; {}
8251: 5F ; ????
8252: 34 ; ????
8253: 5F ; ????
8254: 8F ; ????
8255: 5F ; ????
8256: 7F ; ????
8257: 00              BRK                         
8258: 00              BRK                         
8259: 00              BRK                         
825A: 7F ; ????
825B: 00              BRK                         
825C: 00              BRK                         
825D: 00              BRK                         
825E: 7F ; ????
825F: 00              BRK                         
8260: 00              BRK                         
8261: 00              BRK                         
8262: FC ; ????
8263: 27 ; ????
8264: 01 00           ORA     ($00,X)             ; {ram.GP_00}
8266: F8              SED                         
8267: 94 01           STY     $01,X               
8269: 00              BRK                         
826A: 7F ; ????
826B: 00              BRK                         
826C: 00              BRK                         
826D: 00              BRK                         
826E: 00              BRK                         
826F: AE 01 00        LDX     $0001               
8272: 7F ; ????
8273: 00              BRK                         
8274: 00              BRK                         
8275: 00              BRK                         
8276: F8              SED                         
8277: 5B ; ????
8278: 00              BRK                         
8279: FC ; ????
827A: F8              SED                         
827B: 5B ; ????
827C: 40              RTI                         
827D: 04 ; ????
827E: 00              BRK                         
827F: 5C ; ????
8280: 00              BRK                         
8281: FC ; ????
8282: 00              BRK                         
8283: 5C ; ????
8284: 40              RTI                         
8285: 04 ; ????
8286: F8              SED                         
8287: 0E 00 FC        ASL     $FC00               
828A: F8              SED                         
828B: 0E 40 04        ASL     $0440               
828E: 00              BRK                         
828F: 1E 00 FC        ASL     $FC00,X             
8292: 00              BRK                         
8293: 1E 40 04        ASL     $0440,X             
8296: F8              SED                         
8297: 71 42           ADC     ($42),Y             
8299: FC ; ????
829A: F8              SED                         
829B: 70 42           BVS     $82DF               ; {}
829D: 04 ; ????
829E: 00              BRK                         
829F: 75 42           ADC     $42,X               
82A1: FC ; ????
82A2: 00              BRK                         
82A3: 74 ; ????
82A4: 42 ; ????
82A5: 04 ; ????
82A6: F8              SED                         
82A7: 70 02           BVS     $82AB               ; {}
82A9: FC ; ????
82AA: F8              SED                         
82AB: 73 ; ????
82AC: 02 ; ????
82AD: 04 ; ????
82AE: 00              BRK                         
82AF: 76 02           ROR     $02,X               
82B1: FC ; ????
82B2: 00              BRK                         
82B3: 77 ; ????
82B4: 02 ; ????
82B5: 04 ; ????
82B6: F8              SED                         
82B7: 73 ; ????
82B8: 42 ; ????
82B9: FC ; ????
82BA: F8              SED                         
82BB: 70 42           BVS     $82FF               ; {}
82BD: 04 ; ????
82BE: 00              BRK                         
82BF: 77 ; ????
82C0: 42 ; ????
82C1: FC ; ????
82C2: 00              BRK                         
82C3: 76 42           ROR     $42,X               
82C5: 04 ; ????
82C6: F8              SED                         
82C7: 80 ; ????
82C8: 02 ; ????
82C9: FC ; ????
82CA: F8              SED                         
82CB: 81 02           STA     ($02,X)             
82CD: 04 ; ????
82CE: 00              BRK                         
82CF: 84 02           STY     $02                 
82D1: FC ; ????
82D2: 00              BRK                         
82D3: 85 02           STA     $02                 
82D5: 04 ; ????
82D6: F8              SED                         
82D7: 82 ; ????
82D8: 02 ; ????
82D9: FC ; ????
82DA: F8              SED                         
82DB: 83 ; ????
82DC: 02 ; ????
82DD: 04 ; ????
82DE: 00              BRK                         
82DF: 86 02           STX     $02                 
82E1: FC ; ????
82E2: 00              BRK                         
82E3: 87 ; ????
82E4: 02 ; ????
82E5: 04 ; ????
82E6: 7F ; ????
82E7: 00              BRK                         
82E8: 00              BRK                         
82E9: 00              BRK                         
82EA: 7F ; ????
82EB: 00              BRK                         
82EC: 00              BRK                         
82ED: 00              BRK                         
82EE: 00              BRK                         
82EF: E8              INX                         
82F0: 03 ; ????
82F1: FC ; ????
82F2: 00              BRK                         
82F3: E8              INX                         
82F4: 43 ; ????
82F5: 04 ; ????
82F6: 7F ; ????
82F7: 00              BRK                         
82F8: 00              BRK                         
82F9: 00              BRK                         
82FA: 7F ; ????
82FB: 00              BRK                         
82FC: 00              BRK                         
82FD: 00              BRK                         
82FE: 00              BRK                         
82FF: E9 03           SBC     #$03                
8301: FC ; ????
8302: 00              BRK                         
8303: EA              NOP                         
8304: 03 ; ????
8305: 04 ; ????
8306: 7F ; ????
8307: 00              BRK                         
8308: 00              BRK                         
8309: 00              BRK                         
830A: 7F ; ????
830B: 00              BRK                         
830C: 00              BRK                         
830D: 00              BRK                         
830E: 00              BRK                         
830F: EA              NOP                         
8310: 43 ; ????
8311: FC ; ????
8312: 00              BRK                         
8313: E9 43           SBC     #$43                
8315: 04 ; ????
8316: F8              SED                         
8317: EB ; ????
8318: 03 ; ????
8319: FC ; ????
831A: F8              SED                         
831B: EC 03 04        CPX     $0403               
831E: 00              BRK                         
831F: ED 03 FC        SBC     $FC03               
8322: 00              BRK                         
8323: EE 03 04        INC     $0403               
8326: F8              SED                         
8327: EC 43 FC        CPX     $FC43               
832A: F8              SED                         
832B: EB ; ????
832C: 43 ; ????
832D: 04 ; ????
832E: 00              BRK                         
832F: EE 43 FC        INC     $FC43               
8332: 00              BRK                         
8333: ED 43 04        SBC     $0443               
8336: F8              SED                         
8337: 46 00           LSR     $00                 ; {ram.GP_00}
8339: FC ; ????
833A: F8              SED                         
833B: 47 ; ????
833C: 00              BRK                         
833D: 04 ; ????
833E: 00              BRK                         
833F: 56 00           LSR     $00,X               ; {ram.GP_00}
8341: FC ; ????
8342: 00              BRK                         
8343: 57 ; ????
8344: 00              BRK                         
8345: 04 ; ????
8346: F8              SED                         
8347: EC 02 FC        CPX     $FC02               
834A: F8              SED                         
834B: ED 02 04        SBC     $0402               
834E: 00              BRK                         
834F: EE 02 FC        INC     $FC02               
8352: 00              BRK                         
8353: EF ; ????
8354: 02 ; ????
8355: 04 ; ????
8356: F8              SED                         
8357: BD 02 FC        LDA     $FC02,X             
835A: F8              SED                         
835B: BD 42 04        LDA     $0442,X             
835E: 00              BRK                         
835F: BD 82 FC        LDA     $FC82,X             
8362: 00              BRK                         
8363: BD C2 04        LDA     $04C2,X             
8366: F8              SED                         
8367: BE 02 FC        LDX     $FC02,Y             
836A: F8              SED                         
836B: BE 42 04        LDX     $0442,Y             
836E: 00              BRK                         
836F: BF ; ????
8370: 02 ; ????
8371: FC ; ????
8372: 00              BRK                         
8373: BF ; ????
8374: 42 ; ????
8375: 04 ; ????
8376: F8              SED                         
8377: 2A              ROL     A                   
8378: 02 ; ????
8379: FC ; ????
837A: F8              SED                         
837B: 2A              ROL     A                   
837C: 02 ; ????
837D: 04 ; ????
837E: 00              BRK                         
837F: 2A              ROL     A                   
8380: 82 ; ????
8381: FC ; ????
8382: 00              BRK                         
8383: 2A              ROL     A                   
8384: 82 ; ????
8385: 04 ; ????
8386: F8              SED                         
8387: BF ; ????
8388: 82 ; ????
8389: FC ; ????
838A: F8              SED                         
838B: BF ; ????
838C: C2 ; ????
838D: 04 ; ????
838E: 00              BRK                         
838F: BE 82 FC        LDX     $FC82,Y             
8392: 00              BRK                         
8393: BE C2 04        LDX     $04C2,Y             
8396: F8              SED                         
8397: D4 ; ????
8398: 03 ; ????
8399: FC ; ????
839A: F8              SED                         
839B: D4 ; ????
839C: 43 ; ????
839D: 04 ; ????
839E: 00              BRK                         
839F: D5 03           CMP     $03,X               
83A1: FC ; ????
83A2: 00              BRK                         
83A3: D5 43           CMP     $43,X               
83A5: 04 ; ????
83A6: F8              SED                         
83A7: D6 03           DEC     $03,X               
83A9: FC ; ????
83AA: F8              SED                         
83AB: D6 43           DEC     $43,X               
83AD: 04 ; ????
83AE: 00              BRK                         
83AF: D7 ; ????
83B0: 03 ; ????
83B1: FC ; ????
83B2: 00              BRK                         
83B3: D7 ; ????
83B4: 43 ; ????
83B5: 04 ; ????
83B6: F8              SED                         
83B7: 50 00           BVC     $83B9               ; {}
83B9: FC ; ????
83BA: F8              SED                         
83BB: 50 40           BVC     $83FD               ; {}
83BD: 04 ; ????
83BE: 00              BRK                         
83BF: 51 00           EOR     ($00),Y             ; {ram.GP_00}
83C1: FC ; ????
83C2: 00              BRK                         
83C3: 51 40           EOR     ($40),Y             
83C5: 04 ; ????
83C6: F8              SED                         
83C7: 3E 00 FC        ROL     $FC00,X             
83CA: 7F ; ????
83CB: 00              BRK                         
83CC: 00              BRK                         
83CD: 00              BRK                         
83CE: 00              BRK                         
83CF: 3E 80 FC        ROL     $FC80,X             
83D2: 7F ; ????
83D3: 00              BRK                         
83D4: 00              BRK                         
83D5: 00              BRK                         
83D6: F8              SED                         
83D7: 52 ; ????
83D8: 00              BRK                         
83D9: 04 ; ????
83DA: 7F ; ????
83DB: 00              BRK                         
83DC: 00              BRK                         
83DD: 00              BRK                         
83DE: 00              BRK                         
83DF: 52 ; ????
83E0: 80 ; ????
83E1: 04 ; ????
83E2: 7F ; ????
83E3: 00              BRK                         
83E4: 00              BRK                         
83E5: 00              BRK                         
83E6: F8              SED                         
83E7: 3D 00 FC        AND     $FC00,X             
83EA: F8              SED                         
83EB: 3D 40 03        AND     $0340,X             
83EE: 00              BRK                         
83EF: 4D 00 FC        EOR     $FC00               
83F2: 00              BRK                         
83F3: 4D 40 03        EOR     $0340               
83F6: F8              SED                         
83F7: 92 ; ????
83F8: 01 FD           ORA     ($FD,X)             
83FA: F8              SED                         
83FB: 94 01           STY     $01,X               
83FD: 03 ; ????
83FE: 00              BRK                         
83FF: 93 ; ????
8400: 01 FD           ORA     ($FD,X)             
8402: 00              BRK                         
8403: AE 01 03        LDX     $0301               
8406: F8              SED                         
8407: 9A              TXS                         
8408: 01 F4           ORA     ($F4,X)             
840A: F8              SED                         
840B: 9A              TXS                         
840C: 01 FC           ORA     ($FC,X)             
840E: F8              SED                         
840F: 9A              TXS                         
8410: 01 04           ORA     ($04,X)             
8412: F8              SED                         
8413: 9A              TXS                         
8414: 01 0C           ORA     ($0C,X)             
8416: F8              SED                         
8417: 0E 00 FC        ASL     $FC00               
841A: F8              SED                         
841B: 0E 40 04        ASL     $0440               
841E: 00              BRK                         
841F: 5C ; ????
8420: 00              BRK                         
8421: FC ; ????
8422: 00              BRK                         
8423: 5C ; ????
8424: 40              RTI                         
8425: 04 ; ????
8426: A2 50           LDX     #$50                
8428: A9 80           LDA     #$80                
842A: 9D 01 07        STA     $0701,X             
842D: 0A              ASL     A                   
842E: 9D 00 07        STA     $0700,X             
8431: 85 A1           STA     $A1                 
8433: 60              RTS                         
8434: A2 50           LDX     #$50                
8436: BD 01 07        LDA     $0701,X             
8439: 10 0C           BPL     $8447               ; {}
843B: 20 0D 86        JSR     $860D               ; {}
843E: BD 01 07        LDA     $0701,X             
8441: 29 0F           AND     #$0F                
8443: F0 03           BEQ     $8448               ; {}
8445: D0 51           BNE     $8498               ; {}
8447: 60              RTS                         
8448: A5 A1           LDA     $A1                 
844A: CD 07 7E        CMP     $7E07               
844D: 90 06           BCC     $8455               ; {}
844F: A9 00           LDA     #$00                
8451: 9D 01 07        STA     $0701,X             
8454: 60              RTS                         
8455: 85 00           STA     $00                 ; {ram.GP_00}
8457: 0A              ASL     A                   
8458: 0A              ASL     A                   
8459: A8              TAY                         
845A: B9 08 7E        LDA     $7E08,Y             
845D: CD 30 01        CMP     $0130               
8460: 90 17           BCC     $8479               ; {}
8462: D0 E3           BNE     $8447               ; {}
8464: B9 09 7E        LDA     $7E09,Y             
8467: CD D1 04        CMP     $04D1               
846A: 90 0D           BCC     $8479               ; {}
846C: D0 D9           BNE     $8447               ; {}
846E: B9 0A 7E        LDA     $7E0A,Y             
8471: 29 F0           AND     #$F0                
8473: C5 FD           CMP     $FD                 
8475: F0 06           BEQ     $847D               ; {}
8477: 90 CE           BCC     $8447               ; {}
8479: E6 A1           INC     $A1                 
847B: D0 CB           BNE     $8448               ; {}
847D: A9 00           LDA     #$00                
847F: 9D 00 07        STA     $0700,X             
8482: B9 0A 7E        LDA     $7E0A,Y             
8485: 0A              ASL     A                   
8486: 0A              ASL     A                   
8487: 0A              ASL     A                   
8488: 0A              ASL     A                   
8489: 9D 03 07        STA     $0703,X             
848C: A9 81           LDA     #$81                
848E: 9D 01 07        STA     $0701,X             
8491: B9 0B 7E        LDA     $7E0B,Y             
8494: 9D 02 07        STA     $0702,X             
8497: 60              RTS                         
8498: BD 00 07        LDA     $0700,X             
849B: C9 F8           CMP     #$F8                
849D: B0 11           BCS     $84B0               ; {}
849F: 20 8A D9        JSR     $D98A               
84A2: 90 03           BCC     $84A7               ; {}
84A4: 4C C6 84        JMP     $84C6               ; {}
84A7: BD 02 07        LDA     $0702,X             
84AA: D0 11           BNE     $84BD               ; {}
84AC: A9 FF           LDA     #$FF                
84AE: 85 3E           STA     $3E                 
84B0: A9 10           LDA     #$10                
84B2: 8D 81 03        STA     $0381               
84B5: A9 80           LDA     #$80                
84B7: 9D 01 07        STA     $0701,X             
84BA: 4C 2B DD        JMP     $DD2B               
84BD: A5 A6           LDA     $A6                 
84BF: 18              CLC                         
84C0: 69 07           ADC     #$07                
84C2: 85 A6           STA     $A6                 
84C4: D0 EA           BNE     $84B0               ; {}
84C6: BD 02 07        LDA     $0702,X             
84C9: D0 05           BNE     $84D0               ; {}
84CB: A9 19           LDA     #$19                
84CD: 4C 67 C6        JMP     $C667               
84D0: A9 36           LDA     #$36                
84D2: 4C CD C4        JMP     $C4CD               
84D5: A9 08           LDA     #$08                
84D7: 9D 00 07        STA     $0700,X             
84DA: A9 44           LDA     #$44                
84DC: 9D 02 07        STA     $0702,X             
84DF: A9 50           LDA     #$50                
84E1: 9D 03 07        STA     $0703,X             
84E4: A9 00           LDA     #$00                
84E6: 9D 04 07        STA     $0704,X             
84E9: 9D 05 07        STA     $0705,X             
84EC: 20 85 85        JSR     $8585               ; {}
84EF: 60              RTS                         
84F0: A2 F0           LDX     #$F0                
84F2: BD 01 07        LDA     $0701,X             
84F5: 29 F8           AND     #$F8                
84F7: C9 30           CMP     #$30                
84F9: D0 F4           BNE     $84EF               ; {}
84FB: BD 01 07        LDA     $0701,X             
84FE: 29 07           AND     #$07                
8500: 20 2B EE        JSR     $EE2B               
8503: E1 85           SBC     ($85,X)             
8505: 11 85           ORA     ($85),Y             
8507: A9 85           LDA     #$85                
8509: 0B ; ????
850A: 85 20           STA     $20                 
850C: 0D 86 4C        ORA     $4C86               
850F: 65 DD           ADC     $DD                 
8511: 20 08 DD        JSR     $DD08               
8514: 20 0D 86        JSR     $860D               ; {}
8517: BD 02 07        LDA     $0702,X             
851A: 29 0F           AND     #$0F                
851C: C9 08           CMP     #$08                
851E: B0 4F           BCS     $856F               ; {}
8520: A9 D8           LDA     #$D8                
8522: 20 7A 85        JSR     $857A               ; {}
8525: 20 6D C7        JSR     $C76D               
8528: 20 ED 85        JSR     $85ED               ; {}
852B: 20 90 D9        JSR     $D990               
852E: 90 15           BCC     $8545               ; {}
8530: 20 E7 D9        JSR     $D9E7               
8533: 90 15           BCC     $854A               ; {}
8535: 20 09 DA        JSR     $DA09               
8538: 20 62 DF        JSR     $DF62               
853B: 20 C0 DB        JSR     $DBC0               
853E: 20 19 86        JSR     $8619               ; {}
8541: 20 DE DC        JSR     $DCDE               
8544: 60              RTS                         
8545: A9 F8           LDA     #$F8                
8547: 99 00 07        STA     $0700,Y             
854A: A9 80           LDA     #$80                
854C: 8D 80 03        STA     $0380               
854F: 20 A9 DC        JSR     $DCA9               
8552: BD 01 07        LDA     $0701,X             
8555: 29 F8           AND     #$F8                
8557: 09 03           ORA     #$03                
8559: 9D 01 07        STA     $0701,X             
855C: A9 FF           LDA     #$FF                
855E: 9D 02 07        STA     $0702,X             
8561: A9 08           LDA     #$08                
8563: 8D 81 03        STA     $0381               
8566: 20 9E 85        JSR     $859E               ; {}
8569: 20 E1 E2        JSR     $E2E1               
856C: 4C F0 E2        JMP     $E2F0               
856F: A9 28           LDA     #$28                
8571: 20 7A 85        JSR     $857A               ; {}
8574: 20 8D C7        JSR     $C78D               
8577: 4C 2B 85        JMP     $852B               ; {}
857A: 85 08           STA     $08                 
857C: A9 30           LDA     #$30                
857E: 85 09           STA     $09                 
8580: A9 60           LDA     #$60                
8582: 85 0A           STA     $0A                 
8584: 60              RTS                         
8585: 98              TYA                         
8586: 48              PHA                         
8587: BD 01 07        LDA     $0701,X             
858A: 29 F8           AND     #$F8                
858C: 4A              LSR     A                   
858D: 4A              LSR     A                   
858E: 4A              LSR     A                   
858F: A8              TAY                         
8590: B9 20 7E        LDA     $7E20,Y             
8593: 9D 07 07        STA     $0707,X             
8596: A9 00           LDA     #$00                
8598: 9D 08 07        STA     $0708,X             
859B: 68              PLA                         
859C: A8              TAY                         
859D: 60              RTS                         
859E: BD 01 07        LDA     $0701,X             
85A1: 4A              LSR     A                   
85A2: 4A              LSR     A                   
85A3: 4A              LSR     A                   
85A4: A8              TAY                         
85A5: B9 30 7E        LDA     $7E30,Y             
85A8: 60              RTS                         
85A9: 20 08 DD        JSR     $DD08               
85AC: 20 0D 86        JSR     $860D               ; {}
85AF: BD 02 07        LDA     $0702,X             
85B2: 29 0F           AND     #$0F                
85B4: C9 08           CMP     #$08                
85B6: B0 0F           BCS     $85C7               ; {}
85B8: AD 23 07        LDA     $0723               
85BB: 18              CLC                         
85BC: 69 10           ADC     #$10                
85BE: 20 D6 85        JSR     $85D6               ; {}
85C1: 20 6D C7        JSR     $C76D               
85C4: 4C 2B 85        JMP     $852B               ; {}
85C7: AD 23 07        LDA     $0723               
85CA: 38              SEC                         
85CB: E9 10           SBC     #$10                
85CD: 20 D6 85        JSR     $85D6               ; {}
85D0: 20 8D C7        JSR     $C78D               
85D3: 4C 2B 85        JMP     $852B               ; {}
85D6: 85 08           STA     $08                 
85D8: A9 30           LDA     #$30                
85DA: 85 09           STA     $09                 
85DC: A9 F8           LDA     #$F8                
85DE: 85 0A           STA     $0A                 
85E0: 60              RTS                         
85E1: 8A              TXA                         
85E2: C5 14           CMP     $14                 
85E4: D0 06           BNE     $85EC               ; {}
85E6: 20 D5 84        JSR     $84D5               ; {}
85E9: FE 01 07        INC     $0701,X             
85EC: 60              RTS                         
85ED: A5 15           LDA     $15                 
85EF: 29 01           AND     #$01                
85F1: D0 19           BNE     $860C               ; {}
85F3: AD 23 07        LDA     $0723               
85F6: 38              SEC                         
85F7: FD 03 07        SBC     $0703,X             
85FA: B0 02           BCS     $85FE               ; {}
85FC: 49 FF           EOR     #$FF                
85FE: C9 08           CMP     #$08                
8600: B0 0A           BCS     $860C               ; {}
8602: BD 01 07        LDA     $0701,X             
8605: 29 F8           AND     #$F8                
8607: 09 02           ORA     #$02                
8609: 9D 01 07        STA     $0701,X             
860C: 60              RTS                         
860D: 48              PHA                         
860E: A5 27           LDA     $27                 
8610: 18              CLC                         
8611: 7D 00 07        ADC     $0700,X             
8614: 9D 00 07        STA     $0700,X             
8617: 68              PLA                         
8618: 60              RTS                         
8619: A0 56           LDY     #$56                
861B: BD 02 07        LDA     $0702,X             
861E: 29 0F           AND     #$0F                
8620: C9 08           CMP     #$08                
8622: B0 01           BCS     $8625               ; {}
8624: C8              INY                         
8625: 98              TYA                         
8626: 4C CD C4        JMP     $C4CD               
8629: 60              RTS                         
862A: 20 2B 8B        JSR     $8B2B               ; {}
862D: 20 86 86        JSR     $8686               ; {}
8630: AD 61 07        LDA     $0761               
8633: 0D 71 07        ORA     $0771               
8636: 0D 81 07        ORA     $0781               
8639: 0D 91 07        ORA     $0791               
863C: F0 0F           BEQ     $864D               ; {}
863E: 20 0A 8C        JSR     $8C0A               ; {}
8641: 20 DF 89        JSR     $89DF               ; {}
8644: 20 BD 86        JSR     $86BD               ; {}
8647: 20 04 87        JSR     $8704               ; {}
864A: 4C 84 8B        JMP     $8B84               ; {}
864D: AD 30 01        LDA     $0130               
8650: 0A              ASL     A                   
8651: A8              TAY                         
8652: B9 D0 7C        LDA     $7CD0,Y             
8655: 85 00           STA     $00                 ; {ram.GP_00}
8657: B9 D1 7C        LDA     $7CD1,Y             
865A: 85 01           STA     $01                 
865C: AC D1 04        LDY     $04D1               
865F: B1 00           LDA     ($00),Y             ; {ram.GP_00}
8661: C9 0D           CMP     #$0D                
8663: F0 20           BEQ     $8685               ; {}
8665: 0A              ASL     A                   
8666: 0A              ASL     A                   
8667: 0A              ASL     A                   
8668: 20 9D DC        JSR     $DC9D               
866B: 8D 61 07        STA     $0761               
866E: 8D 71 07        STA     $0771               
8671: 8D 81 07        STA     $0781               
8674: 8D 91 07        STA     $0791               
8677: A9 00           LDA     #$00                
8679: 8D 60 07        STA     $0760               
867C: 8D 70 07        STA     $0770               
867F: 8D 80 07        STA     $0780               
8682: 8D 90 07        STA     $0790               
8685: 60              RTS                         
8686: AD 61 07        LDA     $0761               
8689: 29 F8           AND     #$F8                
868B: C9 68           CMP     #$68                
868D: F0 2D           BEQ     $86BC               ; {}
868F: AD 30 01        LDA     $0130               
8692: 0A              ASL     A                   
8693: A8              TAY                         
8694: B9 05 7D        LDA     $7D05,Y             
8697: 85 00           STA     $00                 ; {ram.GP_00}
8699: B9 06 7D        LDA     $7D06,Y             
869C: 85 01           STA     $01                 
869E: AC D1 04        LDY     $04D1               
86A1: B1 00           LDA     ($00),Y             ; {ram.GP_00}
86A3: F0 17           BEQ     $86BC               ; {}
86A5: 29 F0           AND     #$F0                
86A7: 38              SEC                         
86A8: E5 FD           SBC     $FD                 
86AA: C9 FC           CMP     #$FC                
86AC: 90 0E           BCC     $86BC               ; {}
86AE: B1 00           LDA     ($00),Y             ; {ram.GP_00}
86B0: 0A              ASL     A                   
86B1: 0A              ASL     A                   
86B2: 0A              ASL     A                   
86B3: 0A              ASL     A                   
86B4: 8D 63 07        STA     $0763               
86B7: A9 68           LDA     #$68                
86B9: 8D 61 07        STA     $0761               
86BC: 60              RTS                         
86BD: A2 60           LDX     #$60                
86BF: 20 D2 86        JSR     $86D2               ; {}
86C2: A2 70           LDX     #$70                
86C4: 20 D2 86        JSR     $86D2               ; {}
86C7: A2 80           LDX     #$80                
86C9: 20 D2 86        JSR     $86D2               ; {}
86CC: A2 90           LDX     #$90                
86CE: 20 D2 86        JSR     $86D2               ; {}
86D1: 60              RTS                         
86D2: BD 01 07        LDA     $0701,X             
86D5: 29 F8           AND     #$F8                
86D7: C9 40           CMP     #$40                
86D9: D0 F6           BNE     $86D1               ; {}
86DB: 4C FB 84        JMP     $84FB               ; {}
86DE: A9 02           LDA     #$02                
86E0: 9D 02 07        STA     $0702,X             
86E3: A9 00           LDA     #$00                
86E5: 9D 04 07        STA     $0704,X             
86E8: 9D 05 07        STA     $0705,X             
86EB: A9 80           LDA     #$80                
86ED: 9D 06 07        STA     $0706,X             
86F0: 20 85 85        JSR     $8585               ; {}
86F3: A9 F0           LDA     #$F0                
86F5: 9D 00 07        STA     $0700,X             
86F8: 8A              TXA                         
86F9: 38              SEC                         
86FA: E9 60           SBC     #$60                
86FC: 0A              ASL     A                   
86FD: 18              CLC                         
86FE: 69 40           ADC     #$40                
8700: 9D 03 07        STA     $0703,X             
8703: 60              RTS                         
8704: A2 60           LDX     #$60                
8706: 20 18 87        JSR     $8718               ; {}
8709: A2 70           LDX     #$70                
870B: 20 18 87        JSR     $8718               ; {}
870E: A2 80           LDX     #$80                
8710: 20 18 87        JSR     $8718               ; {}
8713: A2 90           LDX     #$90                
8715: 4C 18 87        JMP     $8718               ; {}
8718: BD 01 07        LDA     $0701,X             
871B: 29 F8           AND     #$F8                
871D: C9 50           CMP     #$50                
871F: D0 49           BNE     $876A               ; {}
8721: 20 87 E0        JSR     $E087               
8724: 20 0D 86        JSR     $860D               ; {}
8727: 20 0F DD        JSR     $DD0F               
872A: BD 01 07        LDA     $0701,X             
872D: 29 07           AND     #$07                
872F: F0 06           BEQ     $8737               ; {}
8731: C9 01           CMP     #$01                
8733: F0 16           BEQ     $874B               ; {}
8735: D0 11           BNE     $8748               ; {}
8737: 8A              TXA                         
8738: 4A              LSR     A                   
8739: 4A              LSR     A                   
873A: 18              CLC                         
873B: 65 14           ADC     $14                 
873D: 29 3F           AND     #$3F                
873F: D0 06           BNE     $8747               ; {}
8741: 20 DE 86        JSR     $86DE               ; {}
8744: FE 01 07        INC     $0701,X             
8747: 60              RTS                         
8748: 4C 65 DD        JMP     $DD65               
874B: 20 90 D9        JSR     $D990               
874E: 90 1B           BCC     $876B               ; {}
8750: 20 E7 D9        JSR     $D9E7               
8753: 90 1B           BCC     $8770               ; {}
8755: 20 09 DA        JSR     $DA09               
8758: 20 62 DF        JSR     $DF62               
875B: 20 D8 87        JSR     $87D8               ; {}
875E: 20 DA DB        JSR     $DBDA               
8761: 20 C9 DB        JSR     $DBC9               
8764: 20 00 88        JSR     $8800               ; {}
8767: 20 DE DC        JSR     $DCDE               
876A: 60              RTS                         
876B: A9 F8           LDA     #$F8                
876D: 99 00 07        STA     $0700,Y             
8770: A9 80           LDA     #$80                
8772: 8D 80 03        STA     $0380               
8775: 20 A9 DC        JSR     $DCA9               
8778: FE 01 07        INC     $0701,X             
877B: A9 FF           LDA     #$FF                
877D: 9D 02 07        STA     $0702,X             
8780: A9 08           LDA     #$08                
8782: 8D 81 03        STA     $0381               
8785: 20 9E 85        JSR     $859E               ; {}
8788: 20 E1 E2        JSR     $E2E1               
878B: 4C F0 E2        JMP     $E2F0               
878E: 20 87 D2        JSR     $D287               
8791: D0 0E           BNE     $87A1               ; {}
8793: AD D3 04        LDA     $04D3               
8796: C9 40           CMP     #$40                
8798: B0 19           BCS     $87B3               ; {}
879A: AD D4 04        LDA     $04D4               
879D: C9 40           CMP     #$40                
879F: B0 12           BCS     $87B3               ; {}
87A1: BD 06 07        LDA     $0706,X             
87A4: C9 78           CMP     #$78                
87A6: B0 02           BCS     $87AA               ; {}
87A8: 69 02           ADC     #$02                
87AA: 9D 06 07        STA     $0706,X             
87AD: 29 F0           AND     #$F0                
87AF: 9D 05 07        STA     $0705,X             
87B2: 60              RTS                         
87B3: A9 00           LDA     #$00                
87B5: 9D 06 07        STA     $0706,X             
87B8: 9D 04 07        STA     $0704,X             
87BB: 9D 05 07        STA     $0705,X             
87BE: 60              RTS                         
87BF: BD 06 07        LDA     $0706,X             
87C2: 18              CLC                         
87C3: 69 02           ADC     #$02                
87C5: 9D 06 07        STA     $0706,X             
87C8: C9 F8           CMP     #$F8                
87CA: B0 06           BCS     $87D2               ; {}
87CC: 29 F0           AND     #$F0                
87CE: 9D 05 07        STA     $0705,X             
87D1: 60              RTS                         
87D2: A9 01           LDA     #$01                
87D4: 9D 06 07        STA     $0706,X             
87D7: 60              RTS                         
87D8: BD 06 07        LDA     $0706,X             
87DB: 30 E2           BMI     $87BF               ; {}
87DD: D0 AF           BNE     $878E               ; {}
87DF: 8A              TXA                         
87E0: 38              SEC                         
87E1: E9 60           SBC     #$60                
87E3: 18              CLC                         
87E4: 65 14           ADC     $14                 
87E6: 29 3F           AND     #$3F                
87E8: D0 15           BNE     $87FF               ; {}
87EA: A0 40           LDY     #$40                
87EC: AD 23 07        LDA     $0723               
87EF: DD 03 07        CMP     $0703,X             
87F2: B0 02           BCS     $87F6               ; {}
87F4: A0 B0           LDY     #$B0                
87F6: 98              TYA                         
87F7: 9D 04 07        STA     $0704,X             
87FA: A9 80           LDA     #$80                
87FC: 9D 06 07        STA     $0706,X             
87FF: 60              RTS                         
8800: A0 14           LDY     #$14                
8802: A5 14           LDA     $14                 
8804: 29 08           AND     #$08                
8806: F0 01           BEQ     $8809               ; {}
8808: C8              INY                         
8809: 98              TYA                         
880A: 4C 67 C6        JMP     $C667               
880D: A9 02           LDA     #$02                
880F: 9D 02 07        STA     $0702,X             
8812: 20 85 85        JSR     $8585               ; {}
8815: A9 00           LDA     #$00                
8817: 9D 00 07        STA     $0700,X             
881A: A9 20           LDA     #$20                
881C: 9D 03 07        STA     $0703,X             
881F: 60              RTS                         
8820: A2 60           LDX     #$60                
8822: 20 39 88        JSR     $8839               ; {}
8825: A2 70           LDX     #$70                
8827: 20 39 88        JSR     $8839               ; {}
882A: A2 80           LDX     #$80                
882C: 20 39 88        JSR     $8839               ; {}
882F: A2 90           LDX     #$90                
8831: 20 39 88        JSR     $8839               ; {}
8834: A2 F0           LDX     #$F0                
8836: 4C C2 89        JMP     $89C2               ; {}
8839: BD 01 07        LDA     $0701,X             
883C: 29 F8           AND     #$F8                
883E: C9 38           CMP     #$38                
8840: D0 33           BNE     $8875               ; {}
8842: 20 87 E0        JSR     $E087               
8845: 20 0D 86        JSR     $860D               ; {}
8848: 20 08 DD        JSR     $DD08               
884B: BD 01 07        LDA     $0701,X             
884E: 29 07           AND     #$07                
8850: F0 51           BEQ     $88A3               ; {}
8852: C9 01           CMP     #$01                
8854: D0 4A           BNE     $88A0               ; {}
8856: 20 90 D9        JSR     $D990               
8859: 90 1B           BCC     $8876               ; {}
885B: 20 E7 D9        JSR     $D9E7               
885E: 90 1B           BCC     $887B               ; {}
8860: 20 09 DA        JSR     $DA09               
8863: 20 62 DF        JSR     $DF62               
8866: 20 DF 88        JSR     $88DF               ; {}
8869: 20 C0 DB        JSR     $DBC0               
886C: 20 70 89        JSR     $8970               ; {}
886F: 20 DE DC        JSR     $DCDE               
8872: 20 85 89        JSR     $8985               ; {}
8875: 60              RTS                         
8876: A9 F8           LDA     #$F8                
8878: 99 00 07        STA     $0700,Y             
887B: A9 80           LDA     #$80                
887D: 8D 80 03        STA     $0380               
8880: 20 A9 DC        JSR     $DCA9               
8883: BD 01 07        LDA     $0701,X             
8886: 29 F8           AND     #$F8                
8888: 09 02           ORA     #$02                
888A: 9D 01 07        STA     $0701,X             
888D: A9 FF           LDA     #$FF                
888F: 9D 02 07        STA     $0702,X             
8892: A9 08           LDA     #$08                
8894: 8D 81 03        STA     $0381               
8897: 20 9E 85        JSR     $859E               ; {}
889A: 20 E1 E2        JSR     $E2E1               
889D: 4C F0 E2        JMP     $E2F0               
88A0: 4C 65 DD        JMP     $DD65               
88A3: 8A              TXA                         
88A4: 38              SEC                         
88A5: E9 60           SBC     #$60                
88A7: 0A              ASL     A                   
88A8: 29 60           AND     #$60                
88AA: 85 00           STA     $00                 ; {ram.GP_00}
88AC: A5 FD           LDA     $FD                 
88AE: 29 60           AND     #$60                
88B0: C5 00           CMP     $00                 ; {ram.GP_00}
88B2: D0 C1           BNE     $8875               ; {}
88B4: 20 15 88        JSR     $8815               ; {}
88B7: 20 87 E0        JSR     $E087               
88BA: AD D3 04        LDA     $04D3               
88BD: C9 40           CMP     #$40                
88BF: B0 B4           BCS     $8875               ; {}
88C1: AD D5 04        LDA     $04D5               
88C4: C9 40           CMP     #$40                
88C6: B0 AD           BCS     $8875               ; {}
88C8: 20 0D 88        JSR     $880D               ; {}
88CB: FE 01 07        INC     $0701,X             
88CE: 60              RTS                         
88CF: BD 03 07        LDA     $0703,X             
88D2: CD 23 07        CMP     $0723               
88D5: 90 4E           BCC     $8925               ; {}
88D7: B0 75           BCS     $894E               ; {}
88D9: A9 50           LDA     #$50                
88DB: 9D 02 07        STA     $0702,X             
88DE: 60              RTS                         
88DF: 20 87 D2        JSR     $D287               
88E2: D0 F5           BNE     $88D9               ; {}
88E4: AD D3 04        LDA     $04D3               
88E7: C9 40           CMP     #$40                
88E9: B0 07           BCS     $88F2               ; {}
88EB: AD D4 04        LDA     $04D4               
88EE: C9 40           CMP     #$40                
88F0: 90 E7           BCC     $88D9               ; {}
88F2: BD 02 07        LDA     $0702,X             
88F5: 29 0F           AND     #$0F                
88F7: F0 D6           BEQ     $88CF               ; {}
88F9: A9 00           LDA     #$00                
88FB: 9D 05 07        STA     $0705,X             
88FE: BD 02 07        LDA     $0702,X             
8901: 29 0F           AND     #$0F                
8903: C9 08           CMP     #$08                
8905: B0 29           BCS     $8930               ; {}
8907: BD 03 07        LDA     $0703,X             
890A: C9 F0           CMP     #$F0                
890C: B0 40           BCS     $894E               ; {}
890E: AD D3 04        LDA     $04D3               
8911: C9 40           CMP     #$40                
8913: 90 39           BCC     $894E               ; {}
8915: AD D5 04        LDA     $04D5               
8918: C9 40           CMP     #$40                
891A: B0 32           BCS     $894E               ; {}
891C: BD 02 07        LDA     $0702,X             
891F: 29 0F           AND     #$0F                
8921: 9D 02 07        STA     $0702,X             
8924: 60              RTS                         
8925: A9 02           LDA     #$02                
8927: 9D 02 07        STA     $0702,X             
892A: A9 00           LDA     #$00                
892C: 9D 04 07        STA     $0704,X             
892F: 60              RTS                         
8930: BD 03 07        LDA     $0703,X             
8933: C9 08           CMP     #$08                
8935: 90 EE           BCC     $8925               ; {}
8937: AD D4 04        LDA     $04D4               
893A: C9 40           CMP     #$40                
893C: 90 E7           BCC     $8925               ; {}
893E: AD D6 04        LDA     $04D6               
8941: C9 40           CMP     #$40                
8943: B0 E0           BCS     $8925               ; {}
8945: BD 02 07        LDA     $0702,X             
8948: 29 0F           AND     #$0F                
894A: 9D 02 07        STA     $0702,X             
894D: 60              RTS                         
894E: A9 0D           LDA     #$0D                
8950: 9D 02 07        STA     $0702,X             
8953: A9 00           LDA     #$00                
8955: 9D 04 07        STA     $0704,X             
8958: 60              RTS                         
8959: BD 02 07        LDA     $0702,X             
895C: 48              PHA                         
895D: 29 F0           AND     #$F0                
895F: 9D 05 07        STA     $0705,X             
8962: 68              PLA                         
8963: 0A              ASL     A                   
8964: 0A              ASL     A                   
8965: 0A              ASL     A                   
8966: 0A              ASL     A                   
8967: 9D 04 07        STA     $0704,X             
896A: 20 DA DB        JSR     $DBDA               
896D: 4C C9 DB        JMP     $DBC9               
8970: A0 03           LDY     #$03                
8972: BD 04 07        LDA     $0704,X             
8975: 30 01           BMI     $8978               ; {}
8977: C8              INY                         
8978: A5 14           LDA     $14                 
897A: 29 10           AND     #$10                
897C: D0 02           BNE     $8980               ; {}
897E: C8              INY                         
897F: C8              INY                         
8980: 98              TYA                         
8981: 20 67 C6        JSR     $C667               
8984: 60              RTS                         
8985: A0 F0           LDY     #$F0                
8987: B9 01 07        LDA     $0701,Y             
898A: 29 F8           AND     #$F8                
898C: D0 23           BNE     $89B1               ; {}
898E: BD 00 07        LDA     $0700,X             
8991: 38              SEC                         
8992: E9 08           SBC     #$08                
8994: 99 00 07        STA     $0700,Y             
8997: BD 03 07        LDA     $0703,X             
899A: 99 03 07        STA     $0703,Y             
899D: CD 23 07        CMP     $0723               
89A0: B0 10           BCS     $89B2               ; {}
89A2: BD 04 07        LDA     $0704,X             
89A5: 30 0A           BMI     $89B1               ; {}
89A7: A9 04           LDA     #$04                
89A9: 99 02 07        STA     $0702,Y             
89AC: A9 70           LDA     #$70                
89AE: 99 01 07        STA     $0701,Y             
89B1: 60              RTS                         
89B2: BD 04 07        LDA     $0704,X             
89B5: 10 FA           BPL     $89B1               ; {}
89B7: A9 0D           LDA     #$0D                
89B9: 99 02 07        STA     $0702,Y             
89BC: A9 70           LDA     #$70                
89BE: 99 01 07        STA     $0701,Y             
89C1: 60              RTS                         
89C2: 4C 75 91        JMP     $9175               ; {}
89C5: A9 02           LDA     #$02                
89C7: 9D 02 07        STA     $0702,X             
89CA: 20 85 85        JSR     $8585               ; {}
89CD: 60              RTS                         
89CE: A9 08           LDA     #$08                
89D0: 9D 00 07        STA     $0700,X             
89D3: A9 50           LDA     #$50                
89D5: 24 26           BIT     $26                 
89D7: 10 02           BPL     $89DB               ; {}
89D9: A9 B0           LDA     #$B0                
89DB: 9D 03 07        STA     $0703,X             
89DE: 60              RTS                         
89DF: A2 60           LDX     #$60                
89E1: 20 24 8A        JSR     $8A24               ; {}
89E4: A2 70           LDX     #$70                
89E6: 20 24 8A        JSR     $8A24               ; {}
89E9: A2 80           LDX     #$80                
89EB: 20 24 8A        JSR     $8A24               ; {}
89EE: A2 90           LDX     #$90                
89F0: 4C 24 8A        JMP     $8A24               ; {}
89F3: 8A              TXA                         
89F4: 38              SEC                         
89F5: E9 60           SBC     #$60                
89F7: 29 30           AND     #$30                
89F9: 85 00           STA     $00                 ; {ram.GP_00}
89FB: A5 14           LDA     $14                 
89FD: 29 30           AND     #$30                
89FF: C5 00           CMP     $00                 ; {ram.GP_00}
8A01: D0 20           BNE     $8A23               ; {}
8A03: A5 FD           LDA     $FD                 
8A05: 29 0F           AND     #$0F                
8A07: D0 1A           BNE     $8A23               ; {}
8A09: 20 CE 89        JSR     $89CE               ; {}
8A0C: 20 53 E0        JSR     $E053               
8A0F: AD D5 04        LDA     $04D5               
8A12: C9 40           CMP     #$40                
8A14: B0 0D           BCS     $8A23               ; {}
8A16: AD D3 04        LDA     $04D3               
8A19: C9 40           CMP     #$40                
8A1B: 90 06           BCC     $8A23               ; {}
8A1D: 20 C5 89        JSR     $89C5               ; {}
8A20: FE 01 07        INC     $0701,X             
8A23: 60              RTS                         
8A24: BD 01 07        LDA     $0701,X             
8A27: 29 F8           AND     #$F8                
8A29: C9 28           CMP     #$28                
8A2B: D0 45           BNE     $8A72               ; {}
8A2D: 20 0D 86        JSR     $860D               ; {}
8A30: 20 0F DD        JSR     $DD0F               
8A33: BD 01 07        LDA     $0701,X             
8A36: 29 07           AND     #$07                
8A38: F0 B9           BEQ     $89F3               ; {}
8A3A: C9 01           CMP     #$01                
8A3C: D0 7F           BNE     $8ABD               ; {}
8A3E: 20 53 E0        JSR     $E053               
8A41: BD 00 07        LDA     $0700,X             
8A44: 38              SEC                         
8A45: ED 20 07        SBC     $0720               
8A48: B0 02           BCS     $8A4C               ; {}
8A4A: 49 FF           EOR     #$FF                
8A4C: C9 08           CMP     #$08                
8A4E: B0 06           BCS     $8A56               ; {}
8A50: A5 1F           LDA     $1F                 
8A52: C9 08           CMP     #$08                
8A54: B0 1D           BCS     $8A73               ; {}
8A56: 20 90 D9        JSR     $D990               
8A59: 90 38           BCC     $8A93               ; {}
8A5B: 20 E7 D9        JSR     $D9E7               
8A5E: 90 38           BCC     $8A98               ; {}
8A60: 20 09 DA        JSR     $DA09               
8A63: 20 62 DF        JSR     $DF62               
8A66: 20 D7 8A        JSR     $8AD7               ; {}
8A69: 20 C0 DB        JSR     $DBC0               
8A6C: 20 0D 8B        JSR     $8B0D               ; {}
8A6F: 20 DE DC        JSR     $DCDE               
8A72: 60              RTS                         
8A73: BD 02 07        LDA     $0702,X             
8A76: 48              PHA                         
8A77: 29 08           AND     #$08                
8A79: F0 0F           BEQ     $8A8A               ; {}
8A7B: 68              PLA                         
8A7C: 09 0F           ORA     #$0F                
8A7E: 9D 02 07        STA     $0702,X             
8A81: 20 D7 8A        JSR     $8AD7               ; {}
8A84: 20 C0 DB        JSR     $DBC0               
8A87: 4C 27 8B        JMP     $8B27               ; {}
8A8A: 68              PLA                         
8A8B: 29 F0           AND     #$F0                
8A8D: 9D 02 07        STA     $0702,X             
8A90: 4C 81 8A        JMP     $8A81               ; {}
8A93: A9 F8           LDA     #$F8                
8A95: 99 00 07        STA     $0700,Y             
8A98: A9 80           LDA     #$80                
8A9A: 8D 80 03        STA     $0380               
8A9D: 20 A9 DC        JSR     $DCA9               
8AA0: BD 01 07        LDA     $0701,X             
8AA3: 29 F8           AND     #$F8                
8AA5: 09 02           ORA     #$02                
8AA7: 9D 01 07        STA     $0701,X             
8AAA: A9 FF           LDA     #$FF                
8AAC: 9D 02 07        STA     $0702,X             
8AAF: A9 08           LDA     #$08                
8AB1: 8D 81 03        STA     $0381               
8AB4: 20 9E 85        JSR     $859E               ; {}
8AB7: 20 E1 E2        JSR     $E2E1               
8ABA: 4C F0 E2        JMP     $E2F0               
8ABD: 20 53 E0        JSR     $E053               
8AC0: 4C 65 DD        JMP     $DD65               
8AC3: AD 23 07        LDA     $0723               
8AC6: DD 03 07        CMP     $0703,X             
8AC9: 90 06           BCC     $8AD1               ; {}
8ACB: A9 60           LDA     #$60                
8ACD: 9D 02 07        STA     $0702,X             
8AD0: 60              RTS                         
8AD1: A9 6F           LDA     #$6F                
8AD3: 9D 02 07        STA     $0702,X             
8AD6: 60              RTS                         
8AD7: AD D3 04        LDA     $04D3               
8ADA: C9 40           CMP     #$40                
8ADC: B0 07           BCS     $8AE5               ; {}
8ADE: AD D4 04        LDA     $04D4               
8AE1: C9 40           CMP     #$40                
8AE3: 90 DE           BCC     $8AC3               ; {}
8AE5: A9 00           LDA     #$00                
8AE7: 9D 05 07        STA     $0705,X             
8AEA: BD 02 07        LDA     $0702,X             
8AED: 29 0F           AND     #$0F                
8AEF: C9 08           CMP     #$08                
8AF1: B0 0D           BCS     $8B00               ; {}
8AF3: AD D5 04        LDA     $04D5               
8AF6: C9 40           CMP     #$40                
8AF8: B0 0D           BCS     $8B07               ; {}
8AFA: A9 03           LDA     #$03                
8AFC: 9D 02 07        STA     $0702,X             
8AFF: 60              RTS                         
8B00: AD D6 04        LDA     $04D6               
8B03: C9 40           CMP     #$40                
8B05: B0 F3           BCS     $8AFA               ; {}
8B07: A9 0C           LDA     #$0C                
8B09: 9D 02 07        STA     $0702,X             
8B0C: 60              RTS                         
8B0D: A5 14           LDA     $14                 
8B0F: 29 08           AND     #$08                
8B11: D0 10           BNE     $8B23               ; {}
8B13: A0 50           LDY     #$50                
8B15: BD 02 07        LDA     $0702,X             
8B18: 29 0F           AND     #$0F                
8B1A: C9 08           CMP     #$08                
8B1C: B0 01           BCS     $8B1F               ; {}
8B1E: C8              INY                         
8B1F: 98              TYA                         
8B20: 4C CD C4        JMP     $C4CD               
8B23: A0 52           LDY     #$52                
8B25: D0 EE           BNE     $8B15               ; {}
8B27: A0 54           LDY     #$54                
8B29: D0 EA           BNE     $8B15               ; {}
8B2B: A2 60           LDX     #$60                
8B2D: A0 00           LDY     #$00                
8B2F: 20 44 8B        JSR     $8B44               ; {}
8B32: A2 70           LDX     #$70                
8B34: A0 20           LDY     #$20                
8B36: 20 44 8B        JSR     $8B44               ; {}
8B39: A2 80           LDX     #$80                
8B3B: A0 40           LDY     #$40                
8B3D: 20 44 8B        JSR     $8B44               ; {}
8B40: A2 90           LDX     #$90                
8B42: A0 60           LDY     #$60                
8B44: 20 51 8B        JSR     $8B51               ; {}
8B47: C8              INY                         
8B48: C8              INY                         
8B49: C8              INY                         
8B4A: C8              INY                         
8B4B: 98              TYA                         
8B4C: 29 1F           AND     #$1F                
8B4E: D0 F4           BNE     $8B44               ; {}
8B50: 60              RTS                         
8B51: B9 60 7B        LDA     $7B60,Y             
8B54: C9 FF           CMP     #$FF                
8B56: F0 29           BEQ     $8B81               ; {}
8B58: CD 30 01        CMP     $0130               
8B5B: D0 23           BNE     $8B80               ; {}
8B5D: AD D1 04        LDA     $04D1               
8B60: D9 61 7B        CMP     $7B61,Y             
8B63: D0 1B           BNE     $8B80               ; {}
8B65: A5 FD           LDA     $FD                 
8B67: D9 62 7B        CMP     $7B62,Y             
8B6A: D0 14           BNE     $8B80               ; {}
8B6C: A9 78           LDA     #$78                
8B6E: 9D 01 07        STA     $0701,X             
8B71: A9 0C           LDA     #$0C                
8B73: 9D 02 07        STA     $0702,X             
8B76: A9 00           LDA     #$00                
8B78: 9D 00 07        STA     $0700,X             
8B7B: A9 80           LDA     #$80                
8B7D: 9D 03 07        STA     $0703,X             
8B80: 60              RTS                         
8B81: 68              PLA                         
8B82: 68              PLA                         
8B83: 60              RTS                         
8B84: A2 60           LDX     #$60                
8B86: 20 98 8B        JSR     $8B98               ; {}
8B89: A2 70           LDX     #$70                
8B8B: 20 98 8B        JSR     $8B98               ; {}
8B8E: A2 80           LDX     #$80                
8B90: 20 98 8B        JSR     $8B98               ; {}
8B93: A2 90           LDX     #$90                
8B95: 4C 98 8B        JMP     $8B98               ; {}
8B98: BD 01 07        LDA     $0701,X             
8B9B: 29 F8           AND     #$F8                
8B9D: C9 78           CMP     #$78                
8B9F: D0 20           BNE     $8BC1               ; {}
8BA1: 20 49 E0        JSR     $E049               
8BA4: 20 0D 86        JSR     $860D               ; {}
8BA7: BD 01 07        LDA     $0701,X             
8BAA: 29 07           AND     #$07                
8BAC: BD 00 07        LDA     $0700,X             
8BAF: C9 F8           CMP     #$F8                
8BB1: B0 09           BCS     $8BBC               ; {}
8BB3: 20 C2 8B        JSR     $8BC2               ; {}
8BB6: 20 C0 DB        JSR     $DBC0               
8BB9: 4C EA 8B        JMP     $8BEA               ; {}
8BBC: A9 00           LDA     #$00                
8BBE: 9D 01 07        STA     $0701,X             
8BC1: 60              RTS                         
8BC2: A9 00           LDA     #$00                
8BC4: 9D 05 07        STA     $0705,X             
8BC7: BD 02 07        LDA     $0702,X             
8BCA: 29 0F           AND     #$0F                
8BCC: C9 08           CMP     #$08                
8BCE: B0 0D           BCS     $8BDD               ; {}
8BD0: AD D5 04        LDA     $04D5               
8BD3: C9 40           CMP     #$40                
8BD5: B0 0D           BCS     $8BE4               ; {}
8BD7: A9 03           LDA     #$03                
8BD9: 9D 02 07        STA     $0702,X             
8BDC: 60              RTS                         
8BDD: AD D6 04        LDA     $04D6               
8BE0: C9 40           CMP     #$40                
8BE2: B0 F3           BCS     $8BD7               ; {}
8BE4: A9 0C           LDA     #$0C                
8BE6: 9D 02 07        STA     $0702,X             
8BE9: 60              RTS                         
8BEA: A9 1B           LDA     #$1B                
8BEC: 4C 67 C6        JMP     $C667               
8BEF: A9 02           LDA     #$02                
8BF1: 9D 02 07        STA     $0702,X             
8BF4: 20 85 85        JSR     $8585               ; {}
8BF7: A9 00           LDA     #$00                
8BF9: 9D 04 07        STA     $0704,X             
8BFC: 9D 05 07        STA     $0705,X             
8BFF: 9D 06 07        STA     $0706,X             
8C02: F0 02           BEQ     $8C06               ; {}
8C04: A9 08           LDA     #$08                
8C06: 9D 00 07        STA     $0700,X             
8C09: 60              RTS                         
8C0A: A2 60           LDX     #$60                
8C0C: BD 01 07        LDA     $0701,X             
8C0F: 29 F8           AND     #$F8                
8C11: C9 68           CMP     #$68                
8C13: D0 12           BNE     $8C27               ; {}
8C15: 20 45 8C        JSR     $8C45               ; {}
8C18: A2 78           LDX     #$78                
8C1A: 20 EE 8D        JSR     $8DEE               ; {}
8C1D: A2 78           LDX     #$78                
8C1F: 20 41 8E        JSR     $8E41               ; {}
8C22: A2 7C           LDX     #$7C                
8C24: 20 41 8E        JSR     $8E41               ; {}
8C27: 60              RTS                         
8C28: A2 C0           LDX     #$C0                
8C2A: BD 01 07        LDA     $0701,X             
8C2D: 29 F8           AND     #$F8                
8C2F: C9 68           CMP     #$68                
8C31: D0 F4           BNE     $8C27               ; {}
8C33: 20 45 8C        JSR     $8C45               ; {}
8C36: A2 D8           LDX     #$D8                
8C38: 20 EE 8D        JSR     $8DEE               ; {}
8C3B: A2 D8           LDX     #$D8                
8C3D: 20 41 8E        JSR     $8E41               ; {}
8C40: A2 DC           LDX     #$DC                
8C42: 4C 41 8E        JMP     $8E41               ; {}
8C45: BD 01 07        LDA     $0701,X             
8C48: 29 07           AND     #$07                
8C4A: 20 2B EE        JSR     $EE2B               
8C4D: 18              CLC                         
8C4E: 8D 55 8C        STA     $8C55               ; {}
8C51: 55 8C           EOR     $8C,X               
8C53: 0C ; ????
8C54: 8D 20 87        STA     $8720               ; {}
8C57: E0 20           CPX     #$20                
8C59: 0D 86 20        ORA     $2086               
8C5C: 08              PHP                         
8C5D: DD 20 BC        CMP     $BC20,X             ; {}
8C60: D9 90 44        CMP     $4490,Y             
8C63: 20 E7 D9        JSR     $D9E7               
8C66: 90 47           BCC     $8CAF               ; {}
8C68: 20 58 8D        JSR     $8D58               ; {}
8C6B: BD 01 07        LDA     $0701,X             
8C6E: 29 07           AND     #$07                
8C70: C9 02           CMP     #$02                
8C72: D0 03           BNE     $8C77               ; {}
8C74: 4C C5 8D        JMP     $8DC5               ; {}
8C77: BD 02 07        LDA     $0702,X             
8C7A: 29 0F           AND     #$0F                
8C7C: C9 03           CMP     #$03                
8C7E: 90 10           BCC     $8C90               ; {}
8C80: C9 0D           CMP     #$0D                
8C82: B0 0C           BCS     $8C90               ; {}
8C84: 20 09 DA        JSR     $DA09               
8C87: 20 A3 8D        JSR     $8DA3               ; {}
8C8A: 20 DF 88        JSR     $88DF               ; {}
8C8D: 4C 9D 8C        JMP     $8C9D               ; {}
8C90: BD 08 07        LDA     $0708,X             
8C93: C9 04           CMP     #$04                
8C95: B0 09           BCS     $8CA0               ; {}
8C97: 20 DF 88        JSR     $88DF               ; {}
8C9A: 20 3B 8D        JSR     $8D3B               ; {}
8C9D: 20 C0 DB        JSR     $DBC0               
8CA0: 20 72 8D        JSR     $8D72               ; {}
8CA3: 20 07 8D        JSR     $8D07               ; {}
8CA6: 60              RTS                         
8CA7: 20 F3 8C        JSR     $8CF3               ; {}
8CAA: A9 F8           LDA     #$F8                
8CAC: 99 00 07        STA     $0700,Y             
8CAF: A9 80           LDA     #$80                
8CB1: 8D 80 03        STA     $0380               
8CB4: 20 A9 DC        JSR     $DCA9               
8CB7: BD 01 07        LDA     $0701,X             
8CBA: 29 F8           AND     #$F8                
8CBC: 09 03           ORA     #$03                
8CBE: 9D 01 07        STA     $0701,X             
8CC1: A9 FF           LDA     #$FF                
8CC3: 9D 02 07        STA     $0702,X             
8CC6: A9 08           LDA     #$08                
8CC8: 8D 81 03        STA     $0381               
8CCB: A9 F8           LDA     #$F8                
8CCD: 9D 10 02        STA     $0210,X             
8CD0: 9D 14 02        STA     $0214,X             
8CD3: 20 9E 85        JSR     $859E               ; {}
8CD6: 20 E1 E2        JSR     $E2E1               
8CD9: 4C F0 E2        JMP     $E2F0               
8CDC: 20 F7 91        JSR     $91F7               ; {}
8CDF: BD 03 07        LDA     $0703,X             
8CE2: CD 23 07        CMP     $0723               
8CE5: 90 06           BCC     $8CED               ; {}
8CE7: A9 0A           LDA     #$0A                
8CE9: 9D 02 07        STA     $0702,X             
8CEC: 60              RTS                         
8CED: A9 05           LDA     #$05                
8CEF: 9D 02 07        STA     $0702,X             
8CF2: 60              RTS                         
8CF3: BD 03 07        LDA     $0703,X             
8CF6: CD 23 07        CMP     $0723               
8CF9: 90 06           BCC     $8D01               ; {}
8CFB: A9 0D           LDA     #$0D                
8CFD: 9D 02 07        STA     $0702,X             
8D00: 60              RTS                         
8D01: A9 02           LDA     #$02                
8D03: 9D 02 07        STA     $0702,X             
8D06: 60              RTS                         
8D07: A9 14           LDA     #$14                
8D09: 4C E0 DC        JMP     $DCE0               
8D0C: 20 87 E0        JSR     $E087               
8D0F: 20 0D 86        JSR     $860D               ; {}
8D12: 20 08 DD        JSR     $DD08               
8D15: 4C 65 DD        JMP     $DD65               
8D18: 20 04 8C        JSR     $8C04               ; {}
8D1B: 20 87 E0        JSR     $E087               
8D1E: AD D3 04        LDA     $04D3               
8D21: C9 40           CMP     #$40                
8D23: 90 15           BCC     $8D3A               ; {}
8D25: AD D5 04        LDA     $04D5               
8D28: C9 40           CMP     #$40                
8D2A: B0 0E           BCS     $8D3A               ; {}
8D2C: A5 FD           LDA     $FD                 
8D2E: 29 0F           AND     #$0F                
8D30: C9 04           CMP     #$04                
8D32: D0 06           BNE     $8D3A               ; {}
8D34: 20 EF 8B        JSR     $8BEF               ; {}
8D37: FE 01 07        INC     $0701,X             
8D3A: 60              RTS                         
8D3B: 8A              TXA                         
8D3C: 18              CLC                         
8D3D: 65 14           ADC     $14                 
8D3F: C9 20           CMP     #$20                
8D41: B0 0E           BCS     $8D51               ; {}
8D43: BD 02 07        LDA     $0702,X             
8D46: 29 0F           AND     #$0F                
8D48: C9 08           CMP     #$08                
8D4A: B0 06           BCS     $8D52               ; {}
8D4C: A9 FC           LDA     #$FC                
8D4E: 9D 04 07        STA     $0704,X             
8D51: 60              RTS                         
8D52: A9 04           LDA     #$04                
8D54: 9D 04 07        STA     $0704,X             
8D57: 60              RTS                         
8D58: A5 3E           LDA     $3E                 
8D5A: F0 0F           BEQ     $8D6B               ; {}
8D5C: C9 01           CMP     #$01                
8D5E: F0 0C           BEQ     $8D6C               ; {}
8D60: A9 F8           LDA     #$F8                
8D62: 9D 10 02        STA     $0210,X             
8D65: 9D 14 02        STA     $0214,X             
8D68: 4C 62 DF        JMP     $DF62               
8D6B: 60              RTS                         
8D6C: 20 62 DF        JSR     $DF62               
8D6F: 68              PLA                         
8D70: 68              PLA                         
8D71: 60              RTS                         
8D72: A0 20           LDY     #$20                
8D74: BD 06 07        LDA     $0706,X             
8D77: D0 0B           BNE     $8D84               ; {}
8D79: BD 04 07        LDA     $0704,X             
8D7C: C9 30           CMP     #$30                
8D7E: 90 19           BCC     $8D99               ; {}
8D80: C9 D0           CMP     #$D0                
8D82: B0 15           BCS     $8D99               ; {}
8D84: A0 24           LDY     #$24                
8D86: A5 14           LDA     $14                 
8D88: 29 08           AND     #$08                
8D8A: D0 02           BNE     $8D8E               ; {}
8D8C: C8              INY                         
8D8D: C8              INY                         
8D8E: A5 14           LDA     $14                 
8D90: 29 1F           AND     #$1F                
8D92: D0 05           BNE     $8D99               ; {}
8D94: A9 02           LDA     #$02                
8D96: 8D 83 03        STA     $0383               
8D99: BD 04 07        LDA     $0704,X             
8D9C: 30 01           BMI     $8D9F               ; {}
8D9E: C8              INY                         
8D9F: 98              TYA                         
8DA0: 4C CD C4        JMP     $C4CD               
8DA3: BD 04 07        LDA     $0704,X             
8DA6: 30 15           BMI     $8DBD               ; {}
8DA8: AD D3 04        LDA     $04D3               
8DAB: C9 40           CMP     #$40                
8DAD: B0 0D           BCS     $8DBC               ; {}
8DAF: FE 01 07        INC     $0701,X             
8DB2: A9 80           LDA     #$80                
8DB4: 9D 06 07        STA     $0706,X             
8DB7: A9 02           LDA     #$02                
8DB9: 8D 83 03        STA     $0383               
8DBC: 60              RTS                         
8DBD: AD D4 04        LDA     $04D4               
8DC0: C9 40           CMP     #$40                
8DC2: 90 EB           BCC     $8DAF               ; {}
8DC4: 60              RTS                         
8DC5: BD 06 07        LDA     $0706,X             
8DC8: 29 0F           AND     #$0F                
8DCA: D0 09           BNE     $8DD5               ; {}
8DCC: BD 00 07        LDA     $0700,X             
8DCF: 38              SEC                         
8DD0: E9 04           SBC     #$04                
8DD2: 9D 00 07        STA     $0700,X             
8DD5: 20 DF 88        JSR     $88DF               ; {}
8DD8: 20 C0 DB        JSR     $DBC0               
8DDB: 20 72 8D        JSR     $8D72               ; {}
8DDE: DE 06 07        DEC     $0706,X             
8DE1: D0 0A           BNE     $8DED               ; {}
8DE3: BD 01 07        LDA     $0701,X             
8DE6: 29 F8           AND     #$F8                
8DE8: 09 01           ORA     #$01                
8DEA: 9D 01 07        STA     $0701,X             
8DED: 60              RTS                         
8DEE: 8A              TXA                         
8DEF: 38              SEC                         
8DF0: E9 18           SBC     #$18                
8DF2: A8              TAY                         
8DF3: B9 01 07        LDA     $0701,Y             
8DF6: C9 69           CMP     #$69                
8DF8: F0 03           BEQ     $8DFD               ; {}
8DFA: 4C 7E 8E        JMP     $8E7E               ; {}
8DFD: BD 01 07        LDA     $0701,X             
8E00: 29 F8           AND     #$F8                
8E02: C9 70           CMP     #$70                
8E04: F0 09           BEQ     $8E0F               ; {}
8E06: B9 00 07        LDA     $0700,Y             
8E09: 38              SEC                         
8E0A: E9 12           SBC     #$12                
8E0C: 20 22 8E        JSR     $8E22               ; {}
8E0F: E8              INX                         
8E10: E8              INX                         
8E11: E8              INX                         
8E12: E8              INX                         
8E13: BD 01 07        LDA     $0701,X             
8E16: 29 F8           AND     #$F8                
8E18: C9 70           CMP     #$70                
8E1A: F0 1E           BEQ     $8E3A               ; {}
8E1C: B9 00 07        LDA     $0700,Y             
8E1F: 38              SEC                         
8E20: E9 02           SBC     #$02                
8E22: 9D 00 07        STA     $0700,X             
8E25: A9 70           LDA     #$70                
8E27: 9D 01 07        STA     $0701,X             
8E2A: B9 03 07        LDA     $0703,Y             
8E2D: 9D 03 07        STA     $0703,X             
8E30: B9 04 07        LDA     $0704,Y             
8E33: 30 06           BMI     $8E3B               ; {}
8E35: A9 04           LDA     #$04                
8E37: 9D 02 07        STA     $0702,X             
8E3A: 60              RTS                         
8E3B: A9 0C           LDA     #$0C                
8E3D: 9D 02 07        STA     $0702,X             
8E40: 60              RTS                         
8E41: BD 01 07        LDA     $0701,X             
8E44: 29 F8           AND     #$F8                
8E46: C9 70           CMP     #$70                
8E48: D0 F0           BNE     $8E3A               ; {}
8E4A: BD 03 07        LDA     $0703,X             
8E4D: C9 F8           CMP     #$F8                
8E4F: B0 2D           BCS     $8E7E               ; {}
8E51: 20 0D 86        JSR     $860D               ; {}
8E54: 20 35 E0        JSR     $E035               
8E57: D0 25           BNE     $8E7E               ; {}
8E59: 20 EF DA        JSR     $DAEF               
8E5C: 90 06           BCC     $8E64               ; {}
8E5E: 20 8C 8E        JSR     $8E8C               ; {}
8E61: 4C A9 8E        JMP     $8EA9               ; {}
8E64: A0 60           LDY     #$60                
8E66: E0 C0           CPX     #$C0                
8E68: 90 02           BCC     $8E6C               ; {}
8E6A: A0 C0           LDY     #$C0                
8E6C: B9 01 07        LDA     $0701,Y             
8E6F: 29 07           AND     #$07                
8E71: C9 01           CMP     #$01                
8E73: D0 09           BNE     $8E7E               ; {}
8E75: 8A              TXA                         
8E76: 48              PHA                         
8E77: 98              TYA                         
8E78: AA              TAX                         
8E79: 20 DC 8C        JSR     $8CDC               ; {}
8E7C: 68              PLA                         
8E7D: AA              TAX                         
8E7E: A9 00           LDA     #$00                
8E80: 9D 01 07        STA     $0701,X             
8E83: A9 F8           LDA     #$F8                
8E85: 9D 00 02        STA     $0200,X             
8E88: 9D 00 07        STA     $0700,X             
8E8B: 60              RTS                         
8E8C: BD 02 07        LDA     $0702,X             
8E8F: 29 0F           AND     #$0F                
8E91: C9 08           CMP     #$08                
8E93: B0 0A           BCS     $8E9F               ; {}
8E95: BD 03 07        LDA     $0703,X             
8E98: 18              CLC                         
8E99: 69 04           ADC     #$04                
8E9B: 9D 03 07        STA     $0703,X             
8E9E: 60              RTS                         
8E9F: BD 03 07        LDA     $0703,X             
8EA2: 38              SEC                         
8EA3: E9 04           SBC     #$04                
8EA5: 9D 03 07        STA     $0703,X             
8EA8: 60              RTS                         
8EA9: A9 5F           LDA     #$5F                
8EAB: 9D 01 02        STA     $0201,X             
8EAE: BD 00 07        LDA     $0700,X             
8EB1: 9D 00 02        STA     $0200,X             
8EB4: BD 03 07        LDA     $0703,X             
8EB7: 9D 03 02        STA     $0203,X             
8EBA: 60              RTS                         
8EBB: 60              RTS                         
8EBC: 20 09 8F        JSR     $8F09               ; {}
8EBF: AD C1 07        LDA     $07C1               
8EC2: 0D C9 07        ORA     $07C9               
8EC5: 0D D1 07        ORA     $07D1               
8EC8: 0D D9 07        ORA     $07D9               
8ECB: F0 09           BEQ     $8ED6               ; {}
8ECD: 20 61 8F        JSR     $8F61               ; {}
8ED0: 20 51 90        JSR     $9051               ; {}
8ED3: 4C 28 8C        JMP     $8C28               ; {}
8ED6: AD 30 01        LDA     $0130               
8ED9: 0A              ASL     A                   
8EDA: A8              TAY                         
8EDB: B9 3A 7D        LDA     $7D3A,Y             
8EDE: 85 00           STA     $00                 ; {ram.GP_00}
8EE0: B9 3B 7D        LDA     $7D3B,Y             
8EE3: 85 01           STA     $01                 
8EE5: AC D1 04        LDY     $04D1               
8EE8: B1 00           LDA     ($00),Y             ; {ram.GP_00}
8EEA: 0A              ASL     A                   
8EEB: 0A              ASL     A                   
8EEC: 0A              ASL     A                   
8EED: C9 18           CMP     #$18                
8EEF: F0 0D           BEQ     $8EFE               ; {}
8EF1: C9 68           CMP     #$68                
8EF3: F0 0F           BEQ     $8F04               ; {}
8EF5: 20 99 DC        JSR     $DC99               
8EF8: 8D C9 07        STA     $07C9               
8EFB: 8D D9 07        STA     $07D9               
8EFE: 8D C1 07        STA     $07C1               
8F01: 8D D1 07        STA     $07D1               
8F04: 60              RTS                         
8F05: 8D C1 07        STA     $07C1               
8F08: 60              RTS                         
8F09: AD C1 07        LDA     $07C1               
8F0C: 29 F8           AND     #$F8                
8F0E: C9 68           CMP     #$68                
8F10: F0 31           BEQ     $8F43               ; {}
8F12: AD 30 01        LDA     $0130               
8F15: 0A              ASL     A                   
8F16: A8              TAY                         
8F17: B9 6F 7D        LDA     $7D6F,Y             
8F1A: 85 00           STA     $00                 ; {ram.GP_00}
8F1C: B9 70 7D        LDA     $7D70,Y             
8F1F: 85 01           STA     $01                 
8F21: AC D1 04        LDY     $04D1               
8F24: B1 00           LDA     ($00),Y             ; {ram.GP_00}
8F26: F0 1B           BEQ     $8F43               ; {}
8F28: 29 F0           AND     #$F0                
8F2A: 38              SEC                         
8F2B: E5 FD           SBC     $FD                 
8F2D: C9 FC           CMP     #$FC                
8F2F: 90 12           BCC     $8F43               ; {}
8F31: B1 00           LDA     ($00),Y             ; {ram.GP_00}
8F33: 0A              ASL     A                   
8F34: 0A              ASL     A                   
8F35: 0A              ASL     A                   
8F36: 0A              ASL     A                   
8F37: 8D C3 07        STA     $07C3               
8F3A: A9 68           LDA     #$68                
8F3C: 8D C1 07        STA     $07C1               
8F3F: A9 00           LDA     #$00                
8F41: F0 BE           BEQ     $8F01               ; {}
8F43: 60              RTS                         
8F44: A9 10           LDA     #$10                
8F46: 9D 01 07        STA     $0701,X             
8F49: A9 02           LDA     #$02                
8F4B: 9D 02 07        STA     $0702,X             
8F4E: A9 00           LDA     #$00                
8F50: 9D 04 07        STA     $0704,X             
8F53: 9D 05 07        STA     $0705,X             
8F56: A9 08           LDA     #$08                
8F58: 9D 00 07        STA     $0700,X             
8F5B: A9 80           LDA     #$80                
8F5D: 9D 03 07        STA     $0703,X             
8F60: 60              RTS                         
8F61: A2 C0           LDX     #$C0                
8F63: 20 72 8F        JSR     $8F72               ; {}
8F66: A2 C8           LDX     #$C8                
8F68: 20 72 8F        JSR     $8F72               ; {}
8F6B: A2 D0           LDX     #$D0                
8F6D: 20 72 8F        JSR     $8F72               ; {}
8F70: A2 D8           LDX     #$D8                
8F72: BD 01 07        LDA     $0701,X             
8F75: 29 F8           AND     #$F8                
8F77: C9 10           CMP     #$10                
8F79: D0 31           BNE     $8FAC               ; {}
8F7B: BD 01 07        LDA     $0701,X             
8F7E: 29 07           AND     #$07                
8F80: F0 59           BEQ     $8FDB               ; {}
8F82: C9 01           CMP     #$01                
8F84: D0 4C           BNE     $8FD2               ; {}
8F86: 20 53 E0        JSR     $E053               
8F89: 20 0D 86        JSR     $860D               ; {}
8F8C: BD 00 07        LDA     $0700,X             
8F8F: C9 F8           CMP     #$F8                
8F91: B0 3C           BCS     $8FCF               ; {}
8F93: 20 90 D9        JSR     $D990               
8F96: 90 15           BCC     $8FAD               ; {}
8F98: 20 E7 D9        JSR     $D9E7               
8F9B: 90 15           BCC     $8FB2               ; {}
8F9D: 20 09 DA        JSR     $DA09               
8FA0: 20 65 DF        JSR     $DF65               
8FA3: 20 17 90        JSR     $9017               ; {}
8FA6: 20 C0 DB        JSR     $DBC0               
8FA9: 20 D5 C7        JSR     $C7D5               
8FAC: 60              RTS                         
8FAD: A9 F8           LDA     #$F8                
8FAF: 99 00 07        STA     $0700,Y             
8FB2: BD 01 07        LDA     $0701,X             
8FB5: 29 F8           AND     #$F8                
8FB7: 09 02           ORA     #$02                
8FB9: 9D 01 07        STA     $0701,X             
8FBC: A9 FF           LDA     #$FF                
8FBE: 9D 02 07        STA     $0702,X             
8FC1: A9 08           LDA     #$08                
8FC3: 8D 81 03        STA     $0381               
8FC6: 20 9E 85        JSR     $859E               ; {}
8FC9: 20 E1 E2        JSR     $E2E1               
8FCC: 4C F0 E2        JMP     $E2F0               
8FCF: 4C 2F DF        JMP     $DF2F               
8FD2: 20 53 E0        JSR     $E053               
8FD5: 20 0D 86        JSR     $860D               ; {}
8FD8: 4C B2 DE        JMP     $DEB2               
8FDB: 8A              TXA                         
8FDC: 38              SEC                         
8FDD: E9 C0           SBC     #$C0                
8FDF: 0A              ASL     A                   
8FE0: 0A              ASL     A                   
8FE1: 0A              ASL     A                   
8FE2: 85 00           STA     $00                 ; {ram.GP_00}
8FE4: A5 14           LDA     $14                 
8FE6: 29 C0           AND     #$C0                
8FE8: C5 00           CMP     $00                 ; {ram.GP_00}
8FEA: D0 1A           BNE     $9006               ; {}
8FEC: 20 56 8F        JSR     $8F56               ; {}
8FEF: 20 53 E0        JSR     $E053               
8FF2: AD D5 04        LDA     $04D5               
8FF5: C9 40           CMP     #$40                
8FF7: B0 0D           BCS     $9006               ; {}
8FF9: AD D3 04        LDA     $04D3               
8FFC: C9 40           CMP     #$40                
8FFE: B0 06           BCS     $9006               ; {}
9000: 20 44 8F        JSR     $8F44               ; {}
9003: FE 01 07        INC     $0701,X             
9006: 60              RTS                         
9007: AD 23 07        LDA     $0723               
900A: DD 03 07        CMP     $0703,X             
900D: 90 04           BCC     $9013               ; {}
900F: A9 60           LDA     #$60                
9011: D0 32           BNE     $9045               ; {}
9013: A9 6F           LDA     #$6F                
9015: D0 2E           BNE     $9045               ; {}
9017: 20 87 D2        JSR     $D287               
901A: D0 EB           BNE     $9007               ; {}
901C: AD D3 04        LDA     $04D3               
901F: C9 40           CMP     #$40                
9021: 90 E4           BCC     $9007               ; {}
9023: A9 00           LDA     #$00                
9025: 9D 05 07        STA     $0705,X             
9028: BD 02 07        LDA     $0702,X             
902B: 29 0F           AND     #$0F                
902D: C9 08           CMP     #$08                
902F: B0 0B           BCS     $903C               ; {}
9031: AD D5 04        LDA     $04D5               
9034: C9 40           CMP     #$40                
9036: B0 0B           BCS     $9043               ; {}
9038: A9 03           LDA     #$03                
903A: D0 09           BNE     $9045               ; {}
903C: AD D6 04        LDA     $04D6               
903F: C9 40           CMP     #$40                
9041: B0 F5           BCS     $9038               ; {}
9043: A9 0C           LDA     #$0C                
9045: 9D 02 07        STA     $0702,X             
9048: 60              RTS                         
9049: A2 F0           LDX     #$F0                
904B: A9 00           LDA     #$00                
904D: 9D 01 07        STA     $0701,X             
9050: 60              RTS                         
9051: A2 C0           LDX     #$C0                
9053: 20 62 90        JSR     $9062               ; {}
9056: A2 D0           LDX     #$D0                
9058: 20 62 90        JSR     $9062               ; {}
905B: 60              RTS                         
905C: 20 08 DD        JSR     $DD08               
905F: 4C 65 DD        JMP     $DD65               
9062: BD 01 07        LDA     $0701,X             
9065: 29 F8           AND     #$F8                
9067: C9 18           CMP     #$18                
9069: D0 E5           BNE     $9050               ; {}
906B: 20 0D 86        JSR     $860D               ; {}
906E: BD 01 07        LDA     $0701,X             
9071: 29 07           AND     #$07                
9073: F0 07           BEQ     $907C               ; {}
9075: C9 01           CMP     #$01                
9077: D0 E3           BNE     $905C               ; {}
9079: 4C D5 90        JMP     $90D5               ; {}
907C: 8A              TXA                         
907D: 38              SEC                         
907E: E9 C0           SBC     #$C0                
9080: 85 01           STA     $01                 
9082: 0A              ASL     A                   
9083: 18              CLC                         
9084: 65 14           ADC     $14                 
9086: 29 7F           AND     #$7F                
9088: D0 43           BNE     $90CD               ; {}
908A: A5 26           LDA     $26                 
908C: 4A              LSR     A                   
908D: 4A              LSR     A                   
908E: 4A              LSR     A                   
908F: 29 03           AND     #$03                
9091: A8              TAY                         
9092: B9 CE 90        LDA     $90CE,Y             ; {}
9095: 18              CLC                         
9096: 65 01           ADC     $01                 
9098: 85 00           STA     $00                 ; {ram.GP_00}
909A: AD 20 07        LDA     $0720               
909D: 9D 00 07        STA     $0700,X             
90A0: AD 23 07        LDA     $0723               
90A3: 18              CLC                         
90A4: 65 00           ADC     $00                 ; {ram.GP_00}
90A6: 9D 03 07        STA     $0703,X             
90A9: A5 1E           LDA     $1E                 
90AB: 29 C0           AND     #$C0                
90AD: D0 1E           BNE     $90CD               ; {}
90AF: 20 87 E0        JSR     $E087               
90B2: AD D3 04        LDA     $04D3               
90B5: C9 40           CMP     #$40                
90B7: 90 14           BCC     $90CD               ; {}
90B9: AD D4 04        LDA     $04D4               
90BC: C9 40           CMP     #$40                
90BE: 90 0D           BCC     $90CD               ; {}
90C0: AD D5 04        LDA     $04D5               
90C3: D0 08           BNE     $90CD               ; {}
90C5: FE 01 07        INC     $0701,X             
90C8: A9 00           LDA     #$00                
90CA: 9D 06 07        STA     $0706,X             
90CD: 60              RTS                         
90CE: E0 00           CPX     #$00                
90D0: 10 20           BPL     $90F2               ; {}
90D2: 4C 1D DD        JMP     $DD1D               
90D5: 20 08 DD        JSR     $DD08               
90D8: BD 06 07        LDA     $0706,X             
90DB: C9 40           CMP     #$40                
90DD: 90 11           BCC     $90F0               ; {}
90DF: C9 60           CMP     #$60                
90E1: B0 0D           BCS     $90F0               ; {}
90E3: 20 09 DA        JSR     $DA09               
90E6: 20 90 D9        JSR     $D990               
90E9: 90 0E           BCC     $90F9               ; {}
90EB: 20 E7 D9        JSR     $D9E7               
90EE: 90 0E           BCC     $90FE               ; {}
90F0: FE 06 07        INC     $0706,X             
90F3: 20 62 DF        JSR     $DF62               
90F6: 4C 1B 91        JMP     $911B               ; {}
90F9: A9 F8           LDA     #$F8                
90FB: 99 00 07        STA     $0700,Y             
90FE: BD 01 07        LDA     $0701,X             
9101: 29 F8           AND     #$F8                
9103: 09 02           ORA     #$02                
9105: 9D 01 07        STA     $0701,X             
9108: A9 FF           LDA     #$FF                
910A: 9D 02 07        STA     $0702,X             
910D: A9 08           LDA     #$08                
910F: 8D 81 03        STA     $0381               
9112: 20 9E 85        JSR     $859E               ; {}
9115: 20 E1 E2        JSR     $E2E1               
9118: 4C F0 E2        JMP     $E2F0               
911B: BD 06 07        LDA     $0706,X             
911E: C9 7F           CMP     #$7F                
9120: F0 B0           BEQ     $90D2               ; {}
9122: C9 20           CMP     #$20                
9124: 90 15           BCC     $913B               ; {}
9126: C9 40           CMP     #$40                
9128: 90 04           BCC     $912E               ; {}
912A: C9 60           CMP     #$60                
912C: 90 12           BCC     $9140               ; {}
912E: A0 0A           LDY     #$0A                
9130: A5 14           LDA     $14                 
9132: 29 04           AND     #$04                
9134: D0 01           BNE     $9137               ; {}
9136: C8              INY                         
9137: 98              TYA                         
9138: 4C 67 C6        JMP     $C667               
913B: A9 09           LDA     #$09                
913D: 4C 67 C6        JMP     $C667               
9140: 20 47 91        JSR     $9147               ; {}
9143: A0 0C           LDY     #$0C                
9145: D0 E9           BNE     $9130               ; {}
9147: A0 F0           LDY     #$F0                
9149: B9 01 07        LDA     $0701,Y             
914C: 29 F8           AND     #$F8                
914E: D0 1E           BNE     $916E               ; {}
9150: A9 70           LDA     #$70                
9152: 99 01 07        STA     $0701,Y             
9155: BD 00 07        LDA     $0700,X             
9158: 38              SEC                         
9159: E9 0C           SBC     #$0C                
915B: 99 00 07        STA     $0700,Y             
915E: BD 03 07        LDA     $0703,X             
9161: 99 03 07        STA     $0703,Y             
9164: CD 23 07        CMP     $0723               
9167: B0 06           BCS     $916F               ; {}
9169: A9 04           LDA     #$04                
916B: 99 02 07        STA     $0702,Y             
916E: 60              RTS                         
916F: A9 0D           LDA     #$0D                
9171: 99 02 07        STA     $0702,Y             
9174: 60              RTS                         
9175: BD 01 07        LDA     $0701,X             
9178: 29 F8           AND     #$F8                
917A: C9 70           CMP     #$70                
917C: D0 F0           BNE     $916E               ; {}
917E: BD 00 07        LDA     $0700,X             
9181: C9 F8           CMP     #$F8                
9183: B0 1D           BCS     $91A2               ; {}
9185: BD 03 07        LDA     $0703,X             
9188: C9 F8           CMP     #$F8                
918A: B0 16           BCS     $91A2               ; {}
918C: 20 0D 86        JSR     $860D               ; {}
918F: BD 04 07        LDA     $0704,X             
9192: 48              PHA                         
9193: 20 09 DA        JSR     $DA09               
9196: 68              PLA                         
9197: 9D 04 07        STA     $0704,X             
919A: 90 06           BCC     $91A2               ; {}
919C: 20 B0 91        JSR     $91B0               ; {}
919F: 4C D9 91        JMP     $91D9               ; {}
91A2: A9 00           LDA     #$00                
91A4: 9D 01 07        STA     $0701,X             
91A7: A9 F8           LDA     #$F8                
91A9: 9D 00 02        STA     $0200,X             
91AC: 9D 00 07        STA     $0700,X             
91AF: 60              RTS                         
91B0: BD 02 07        LDA     $0702,X             
91B3: 29 0F           AND     #$0F                
91B5: C9 07           CMP     #$07                
91B7: F0 14           BEQ     $91CD               ; {}
91B9: C9 08           CMP     #$08                
91BB: B0 04           BCS     $91C1               ; {}
91BD: FE 03 07        INC     $0703,X             
91C0: 60              RTS                         
91C1: DE 03 07        DEC     $0703,X             
91C4: A5 14           LDA     $14                 
91C6: 4A              LSR     A                   
91C7: 90 03           BCC     $91CC               ; {}
91C9: DE 03 07        DEC     $0703,X             
91CC: 60              RTS                         
91CD: FE 03 07        INC     $0703,X             
91D0: A5 14           LDA     $14                 
91D2: 4A              LSR     A                   
91D3: 90 03           BCC     $91D8               ; {}
91D5: FE 03 07        INC     $0703,X             
91D8: 60              RTS                         
91D9: A9 A9           LDA     #$A9                
91DB: 9D 01 02        STA     $0201,X             
91DE: BD 00 07        LDA     $0700,X             
91E1: 38              SEC                         
91E2: E9 04           SBC     #$04                
91E4: 9D 00 02        STA     $0200,X             
91E7: BD 03 07        LDA     $0703,X             
91EA: 9D 03 02        STA     $0203,X             
91ED: A9 01           LDA     #$01                
91EF: 9D 02 02        STA     $0202,X             
91F2: 60              RTS                         
91F3: 60              RTS                         
91F4: 4C 19 92        JMP     $9219               ; {}
91F7: AD A1 07        LDA     $07A1               
91FA: 0D A9 07        ORA     $07A9               
91FD: 0D B1 07        ORA     $07B1               
9200: 0D B9 07        ORA     $07B9               
9203: D0 13           BNE     $9218               ; {}
9205: A9 08           LDA     #$08                
9207: 8D A1 07        STA     $07A1               
920A: 8D A9 07        STA     $07A9               
920D: 8D B1 07        STA     $07B1               
9210: 8D B9 07        STA     $07B9               
9213: A9 80           LDA     #$80                
9215: 8D 85 03        STA     $0385               
9218: 60              RTS                         
9219: A2 A0           LDX     #$A0                
921B: 20 2A 92        JSR     $922A               ; {}
921E: A2 A8           LDX     #$A8                
9220: 20 2A 92        JSR     $922A               ; {}
9223: A2 B0           LDX     #$B0                
9225: 20 2A 92        JSR     $922A               ; {}
9228: A2 B8           LDX     #$B8                
922A: BD 01 07        LDA     $0701,X             
922D: 29 F8           AND     #$F8                
922F: C9 08           CMP     #$08                
9231: D0 E5           BNE     $9218               ; {}
9233: BD 01 07        LDA     $0701,X             
9236: 29 07           AND     #$07                
9238: 20 2B EE        JSR     $EE2B               
923B: 13 ; ????
923C: 93 ; ????
923D: 5B ; ????
923E: 92 ; ????
923F: DE 92 43        DEC     $4392,X             
9242: 92 ; ????
9243: 20 0D 86        JSR     $860D               ; {}
9246: 20 B2 DE        JSR     $DEB2               
9249: AD A1 07        LDA     $07A1               
924C: 0D A9 07        ORA     $07A9               
924F: 0D B1 07        ORA     $07B1               
9252: 0D B9 07        ORA     $07B9               
9255: D0 03           BNE     $925A               ; {}
9257: 20 70 CB        JSR     $CB70               
925A: 60              RTS                         
925B: 20 65 93        JSR     $9365               ; {}
925E: BD 02 07        LDA     $0702,X             
9261: 29 0F           AND     #$0F                
9263: C9 08           CMP     #$08                
9265: B0 59           BCS     $92C0               ; {}
9267: A9 D8           LDA     #$D8                
9269: 85 08           STA     $08                 
926B: 20 CD 92        JSR     $92CD               ; {}
926E: 20 6D C7        JSR     $C76D               
9271: 20 ED 85        JSR     $85ED               ; {}
9274: 20 90 D9        JSR     $D990               
9277: 90 24           BCC     $929D               ; {}
9279: 20 E7 D9        JSR     $D9E7               
927C: 90 24           BCC     $92A2               ; {}
927E: 20 09 DA        JSR     $DA09               
9281: F0 C6           BEQ     $9249               ; {}
9283: 90 C4           BCC     $9249               ; {}
9285: 20 62 DF        JSR     $DF62               
9288: 20 0D 86        JSR     $860D               ; {}
928B: 20 C0 DB        JSR     $DBC0               
928E: 20 25 93        JSR     $9325               ; {}
9291: A5 14           LDA     $14                 
9293: 29 3F           AND     #$3F                
9295: D0 05           BNE     $929C               ; {}
9297: A9 01           LDA     #$01                
9299: 8D 83 03        STA     $0383               
929C: 60              RTS                         
929D: A9 F8           LDA     #$F8                
929F: 99 00 07        STA     $0700,Y             
92A2: BD 01 07        LDA     $0701,X             
92A5: 29 F8           AND     #$F8                
92A7: 09 03           ORA     #$03                
92A9: 9D 01 07        STA     $0701,X             
92AC: A9 FF           LDA     #$FF                
92AE: 9D 02 07        STA     $0702,X             
92B1: 20 9E 85        JSR     $859E               ; {}
92B4: 20 E1 E2        JSR     $E2E1               
92B7: 20 F0 E2        JSR     $E2F0               
92BA: A9 01           LDA     #$01                
92BC: 8D 83 03        STA     $0383               
92BF: 60              RTS                         
92C0: A9 28           LDA     #$28                
92C2: 85 08           STA     $08                 
92C4: 20 CD 92        JSR     $92CD               ; {}
92C7: 20 8D C7        JSR     $C78D               
92CA: 4C 74 92        JMP     $9274               ; {}
92CD: AD 20 07        LDA     $0720               
92D0: 38              SEC                         
92D1: E9 30           SBC     #$30                
92D3: 85 09           STA     $09                 
92D5: AD 20 07        LDA     $0720               
92D8: 18              CLC                         
92D9: 69 30           ADC     #$30                
92DB: 85 0A           STA     $0A                 
92DD: 60              RTS                         
92DE: 20 65 93        JSR     $9365               ; {}
92E1: BD 02 07        LDA     $0702,X             
92E4: 29 0F           AND     #$0F                
92E6: C9 08           CMP     #$08                
92E8: B0 0F           BCS     $92F9               ; {}
92EA: AD 23 07        LDA     $0723               
92ED: 18              CLC                         
92EE: 69 10           ADC     #$10                
92F0: 20 08 93        JSR     $9308               ; {}
92F3: 20 6D C7        JSR     $C76D               
92F6: 4C 74 92        JMP     $9274               ; {}
92F9: AD 23 07        LDA     $0723               
92FC: 38              SEC                         
92FD: E9 10           SBC     #$10                
92FF: 20 08 93        JSR     $9308               ; {}
9302: 20 8D C7        JSR     $C78D               
9305: 4C 74 92        JMP     $9274               ; {}
9308: 85 08           STA     $08                 
930A: A9 30           LDA     #$30                
930C: 85 09           STA     $09                 
930E: A9 F8           LDA     #$F8                
9310: 85 0A           STA     $0A                 
9312: 60              RTS                         
9313: 8A              TXA                         
9314: 0A              ASL     A                   
9315: C5 14           CMP     $14                 
9317: D0 0B           BNE     $9324               ; {}
9319: 20 49 8F        JSR     $8F49               ; {}
931C: A9 44           LDA     #$44                
931E: 9D 02 07        STA     $0702,X             
9321: FE 01 07        INC     $0701,X             
9324: 60              RTS                         
9325: A9 79           LDA     #$79                
9327: 9D 01 02        STA     $0201,X             
932A: A9 78           LDA     #$78                
932C: 9D 05 02        STA     $0205,X             
932F: BD 00 07        LDA     $0700,X             
9332: 9D 00 02        STA     $0200,X             
9335: 38              SEC                         
9336: E9 08           SBC     #$08                
9338: 9D 04 02        STA     $0204,X             
933B: BD 03 07        LDA     $0703,X             
933E: 9D 03 02        STA     $0203,X             
9341: 48              PHA                         
9342: A0 00           LDY     #$00                
9344: BD 02 07        LDA     $0702,X             
9347: 29 0F           AND     #$0F                
9349: C9 08           CMP     #$08                
934B: B0 02           BCS     $934F               ; {}
934D: A0 02           LDY     #$02                
934F: 68              PLA                         
9350: 18              CLC                         
9351: 79 61 93        ADC     $9361,Y             ; {}
9354: 9D 07 02        STA     $0207,X             
9357: B9 62 93        LDA     $9362,Y             ; {}
935A: 9D 02 02        STA     $0202,X             
935D: 9D 06 02        STA     $0206,X             
9360: 60              RTS                         
9361: FE 02 02        INC     $0202,X             
9364: 42 ; ????
9365: BD 00 07        LDA     $0700,X             
9368: C9 F0           CMP     #$F0                
936A: B0 07           BCS     $9373               ; {}
936C: BD 03 07        LDA     $0703,X             
936F: C9 FC           CMP     #$FC                
9371: 90 ED           BCC     $9360               ; {}
9373: 68              PLA                         
9374: 68              PLA                         
9375: 20 2F DF        JSR     $DF2F               
9378: 4C 49 92        JMP     $9249               ; {}
937B: AC 30 01        LDY     $0130               
937E: B9 A4 7D        LDA     $7DA4,Y             
9381: A8              TAY                         
9382: 4C 87 93        JMP     $9387               ; {}
9385: A0 1F           LDY     #$1F                
9387: A2 1F           LDX     #$1F                
9389: B9 A7 7D        LDA     $7DA7,Y             
938C: 9D 90 03        STA     $0390,X             
938F: 88              DEY                         
9390: CA              DEX                         
9391: 10 F6           BPL     $9389               ; {}
9393: 60              RTS                         
9394: 85 02           STA     $02                 
9396: 84 03           STY     $03                 
9398: A5 1A           LDA     $1A                 
939A: 29 01           AND     #$01                
939C: 0A              ASL     A                   
939D: A8              TAY                         
939E: B9 E0 7B        LDA     $7BE0,Y             
93A1: 85 00           STA     $00                 ; {ram.GP_00}
93A3: B9 E1 7B        LDA     $7BE1,Y             
93A6: 85 01           STA     $01                 
93A8: 98              TYA                         
93A9: F0 03           BEQ     $93AE               ; {}
93AB: 4C D9 93        JMP     $93D9               ; {}
93AE: A5 FD           LDA     $FD                 
93B0: 18              CLC                         
93B1: 65 00           ADC     $00                 ; {ram.GP_00}
93B3: 85 00           STA     $00                 ; {ram.GP_00}
93B5: A9 00           LDA     #$00                
93B7: 65 01           ADC     $01                 
93B9: 85 01           STA     $01                 
93BB: A5 02           LDA     $02                 
93BD: 18              CLC                         
93BE: 65 00           ADC     $00                 ; {ram.GP_00}
93C0: 29 F0           AND     #$F0                
93C2: 85 00           STA     $00                 ; {ram.GP_00}
93C4: A9 00           LDA     #$00                
93C6: 65 01           ADC     $01                 
93C8: 85 01           STA     $01                 
93CA: A5 03           LDA     $03                 
93CC: 4A              LSR     A                   
93CD: 4A              LSR     A                   
93CE: 4A              LSR     A                   
93CF: 4A              LSR     A                   
93D0: 05 00           ORA     $00                 ; {ram.GP_00}
93D2: 85 00           STA     $00                 ; {ram.GP_00}
93D4: A0 00           LDY     #$00                
93D6: B1 00           LDA     ($00),Y             ; {ram.GP_00}
93D8: 60              RTS                         
93D9: A5 FD           LDA     $FD                 
93DB: 18              CLC                         
93DC: 65 00           ADC     $00                 ; {ram.GP_00}
93DE: 85 00           STA     $00                 ; {ram.GP_00}
93E0: A9 00           LDA     #$00                
93E2: 65 01           ADC     $01                 
93E4: 85 01           STA     $01                 
93E6: A5 00           LDA     $00                 ; {ram.GP_00}
93E8: 18              CLC                         
93E9: 65 02           ADC     $02                 
93EB: 29 F0           AND     #$F0                
93ED: 85 00           STA     $00                 ; {ram.GP_00}
93EF: A5 01           LDA     $01                 
93F1: 69 00           ADC     #$00                
93F3: 85 01           STA     $01                 
93F5: C9 07           CMP     #$07                
93F7: B0 08           BCS     $9401               ; {}
93F9: A5 00           LDA     $00                 ; {ram.GP_00}
93FB: C9 E0           CMP     #$E0                
93FD: B0 02           BCS     $9401               ; {}
93FF: 90 C9           BCC     $93CA               ; {}
9401: A5 00           LDA     $00                 ; {ram.GP_00}
9403: 38              SEC                         
9404: E9 E0           SBC     #$E0                
9406: 85 00           STA     $00                 ; {ram.GP_00}
9408: A5 01           LDA     $01                 
940A: E9 01           SBC     #$01                
940C: 85 01           STA     $01                 
940E: 4C CA 93        JMP     $93CA               ; {}
9411: 20 26 94        JSR     $9426               ; {}
9414: 24 5C           BIT     $5C                 
9416: 70 07           BVS     $941F               ; {}
9418: BD 00 07        LDA     $0700,X             
941B: C9 80           CMP     #$80                
941D: 90 01           BCC     $9420               ; {}
941F: 60              RTS                         
9420: FE 00 07        INC     $0700,X             
9423: 4C F6 94        JMP     $94F6               ; {}
9426: AD D5 04        LDA     $04D5               
9429: C9 2A           CMP     #$2A                
942B: F0 08           BEQ     $9435               ; {}
942D: AD D6 04        LDA     $04D6               
9430: C9 2A           CMP     #$2A                
9432: F0 01           BEQ     $9435               ; {}
9434: 60              RTS                         
9435: A0 28           LDY     #$28                
9437: A9 04           LDA     #$04                
9439: 4C 90 CA        JMP     $CA90               
943C: A5 1C           LDA     $1C                 
943E: 10 15           BPL     $9455               ; {}
9440: AD D6 04        LDA     $04D6               
9443: C9 50           CMP     #$50                
9445: B0 08           BCS     $944F               ; {}
9447: AD D5 04        LDA     $04D5               
944A: C9 50           CMP     #$50                
944C: B0 04           BCS     $9452               ; {}
944E: 60              RTS                         
944F: 4C 3C D0        JMP     $D03C               
9452: 4C 40 D0        JMP     $D040               
9455: AD D5 04        LDA     $04D5               
9458: C9 50           CMP     #$50                
945A: B0 08           BCS     $9464               ; {}
945C: AD D6 04        LDA     $04D6               
945F: C9 50           CMP     #$50                
9461: B0 04           BCS     $9467               ; {}
9463: 60              RTS                         
9464: 4C 44 D0        JMP     $D044               
9467: 4C 4E D0        JMP     $D04E               
946A: A5 FD           LDA     $FD                 
946C: C5 74           CMP     $74                 
946E: D0 03           BNE     $9473               ; {}
9470: 4C 42 EE        JMP     $EE42               
9473: 85 74           STA     $74                 
9475: 29 0F           AND     #$0F                
9477: C9 0D           CMP     #$0D                
9479: F0 19           BEQ     $9494               ; {}
947B: C9 0C           CMP     #$0C                
947D: F0 18           BEQ     $9497               ; {}
947F: A5 68           LDA     $68                 
9481: 0A              ASL     A                   
9482: A8              TAY                         
9483: B9 90 94        LDA     $9490,Y             ; {}
9486: 85 00           STA     $00                 ; {ram.GP_00}
9488: B9 91 94        LDA     $9491,Y             ; {}
948B: 85 01           STA     $01                 
948D: 6C 00 00        JMP     ($0000)             ; {ram.GP_00}
9490: 42 ; ????
9491: EE 9A 94        INC     $949A               ; {}
9494: 4C 1D 95        JMP     $951D               ; {}
9497: 4C 37 95        JMP     $9537               ; {}
949A: 20 B2 94        JSR     $94B2               ; {}
949D: A5 69           LDA     $69                 
949F: 18              CLC                         
94A0: 69 20           ADC     #$20                
94A2: 85 69           STA     $69                 
94A4: A5 6A           LDA     $6A                 
94A6: 69 00           ADC     #$00                
94A8: 85 6A           STA     $6A                 
94AA: 20 B2 94        JSR     $94B2               ; {}
94AD: A9 00           LDA     #$00                
94AF: 85 68           STA     $68                 
94B1: 60              RTS                         
94B2: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
94B5: A5 6A           LDA     $6A                 
94B7: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
94BA: A5 69           LDA     $69                 
94BC: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
94BF: A9 12           LDA     #$12                
94C1: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
94C4: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
94C7: 60              RTS                         
94C8: A5 5C           LDA     $5C                 
94CA: 10 FB           BPL     $94C7               ; {}
94CC: AD 00 01        LDA     $0100               
94CF: 29 7F           AND     #$7F                
94D1: 8D 00 01        STA     $0100               
94D4: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
94D7: 20 22 97        JSR     $9722               ; {}
94DA: A5 5C           LDA     $5C                 
94DC: 29 7F           AND     #$7F                
94DE: 85 5C           STA     $5C                 
94E0: AD 00 01        LDA     $0100               
94E3: 09 80           ORA     #$80                
94E5: 8D 00 01        STA     $0100               
94E8: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
94EB: 68              PLA                         
94EC: 68              PLA                         
94ED: 4C 95 80        JMP     $8095               ; {}
94F0: A5 F3           LDA     $F3                 
94F2: 29 80           AND     #$80                
94F4: F0 22           BEQ     $9518               ; {}
94F6: A5 FD           LDA     $FD                 
94F8: 38              SEC                         
94F9: E9 01           SBC     #$01                
94FB: 85 FD           STA     $FD                 
94FD: A5 1A           LDA     $1A                 
94FF: E9 00           SBC     #$00                
9501: 85 1A           STA     $1A                 
9503: A9 01           LDA     #$01                
9505: 85 27           STA     $27                 
9507: A5 FD           LDA     $FD                 
9509: C9 F0           CMP     #$F0                
950B: 90 0A           BCC     $9517               ; {}
950D: A9 EF           LDA     #$EF                
950F: 85 FD           STA     $FD                 
9511: A5 5C           LDA     $5C                 
9513: 09 80           ORA     #$80                
9515: 85 5C           STA     $5C                 
9517: 60              RTS                         
9518: A9 00           LDA     #$00                
951A: 85 27           STA     $27                 
951C: 60              RTS                         
951D: AD 82 04        LDA     $0482               
9520: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
9523: AD 81 04        LDA     $0481               
9526: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
9529: A0 00           LDY     #$00                
952B: B9 83 04        LDA     $0483,Y             
952E: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
9531: C8              INY                         
9532: C0 40           CPY     #$40                
9534: 90 F5           BCC     $952B               ; {}
9536: 60              RTS                         
9537: 20 C6 96        JSR     $96C6               ; {}
953A: A5 00           LDA     $00                 ; {ram.GP_00}
953C: 18              CLC                         
953D: 69 C0           ADC     #$C0                
953F: 85 01           STA     $01                 
9541: A9 23           LDA     #$23                
9543: 85 02           STA     $02                 
9545: A5 1A           LDA     $1A                 
9547: 29 01           AND     #$01                
9549: D0 04           BNE     $954F               ; {}
954B: A9 2B           LDA     #$2B                
954D: 85 02           STA     $02                 
954F: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
9552: A5 02           LDA     $02                 
9554: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
9557: A5 01           LDA     $01                 
9559: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
955C: 20 C6 96        JSR     $96C6               ; {}
955F: AA              TAX                         
9560: A0 07           LDY     #$07                
9562: BD B0 03        LDA     $03B0,X             
9565: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
9568: E8              INX                         
9569: 88              DEY                         
956A: 10 F6           BPL     $9562               ; {}
956C: 60              RTS                         
956D: A5 FD           LDA     $FD                 
956F: 29 F0           AND     #$F0                
9571: 85 08           STA     $08                 
9573: A9 00           LDA     #$00                
9575: 85 01           STA     $01                 
9577: A5 08           LDA     $08                 
9579: 85 00           STA     $00                 ; {ram.GP_00}
957B: 06 00           ASL     $00                 ; {ram.GP_00}
957D: 26 01           ROL     $01                 
957F: 06 00           ASL     $00                 ; {ram.GP_00}
9581: 26 01           ROL     $01                 
9583: A9 00           LDA     #$00                
9585: 18              CLC                         
9586: 65 00           ADC     $00                 ; {ram.GP_00}
9588: 8D 81 04        STA     $0481               
958B: A9 20           LDA     #$20                
958D: 65 01           ADC     $01                 
958F: 8D 82 04        STA     $0482               
9592: A5 1A           LDA     $1A                 
9594: 29 01           AND     #$01                
9596: D0 09           BNE     $95A1               ; {}
9598: AD 82 04        LDA     $0482               
959B: 18              CLC                         
959C: 69 08           ADC     #$08                
959E: 8D 82 04        STA     $0482               
95A1: 20 B7 95        JSR     $95B7               ; {}
95A4: 20 C2 95        JSR     $95C2               ; {}
95A7: A5 08           LDA     $08                 
95A9: 18              CLC                         
95AA: 65 62           ADC     $62                 
95AC: 85 06           STA     $06                 
95AE: A9 00           LDA     #$00                
95B0: 65 63           ADC     $63                 
95B2: 85 07           STA     $07                 
95B4: 4C D4 95        JMP     $95D4               ; {}
95B7: A5 1A           LDA     $1A                 
95B9: 49 FF           EOR     #$FF                
95BB: 8D D1 04        STA     $04D1               
95BE: EE D1 04        INC     $04D1               
95C1: 60              RTS                         
95C2: AD D1 04        LDA     $04D1               
95C5: 29 01           AND     #$01                
95C7: 0A              ASL     A                   
95C8: A8              TAY                         
95C9: B9 E0 7B        LDA     $7BE0,Y             
95CC: 85 62           STA     $62                 
95CE: B9 E1 7B        LDA     $7BE1,Y             
95D1: 85 63           STA     $63                 
95D3: 60              RTS                         
95D4: A0 0F           LDY     #$0F                
95D6: 98              TYA                         
95D7: 48              PHA                         
95D8: B1 06           LDA     ($06),Y             
95DA: 20 02 96        JSR     $9602               ; {}
95DD: 68              PLA                         
95DE: 48              PHA                         
95DF: 0A              ASL     A                   
95E0: A8              TAY                         
95E1: A5 02           LDA     $02                 
95E3: 99 83 04        STA     $0483,Y             
95E6: C8              INY                         
95E7: A5 03           LDA     $03                 
95E9: 99 83 04        STA     $0483,Y             
95EC: 98              TYA                         
95ED: 18              CLC                         
95EE: 69 1F           ADC     #$1F                
95F0: A8              TAY                         
95F1: A5 04           LDA     $04                 
95F3: 99 83 04        STA     $0483,Y             
95F6: C8              INY                         
95F7: A5 05           LDA     $05                 
95F9: 99 83 04        STA     $0483,Y             
95FC: 68              PLA                         
95FD: A8              TAY                         
95FE: 88              DEY                         
95FF: 10 D5           BPL     $95D6               ; {}
9601: 60              RTS                         
9602: 85 00           STA     $00                 ; {ram.GP_00}
9604: A9 00           LDA     #$00                
9606: 85 01           STA     $01                 
9608: A0 03           LDY     #$03                
960A: 06 00           ASL     $00                 ; {ram.GP_00}
960C: 26 01           ROL     $01                 
960E: 06 00           ASL     $00                 ; {ram.GP_00}
9610: 26 01           ROL     $01                 
9612: A5 3A           LDA     $3A                 
9614: C9 10           CMP     #$10                
9616: B0 16           BCS     $962E               ; {}
9618: A5 00           LDA     $00                 ; {ram.GP_00}
961A: 18              CLC                         
961B: 69 9C           ADC     #$9C                
961D: 85 00           STA     $00                 ; {ram.GP_00}
961F: A5 01           LDA     $01                 
9621: 69 79           ADC     #$79                
9623: 85 01           STA     $01                 
9625: B1 00           LDA     ($00),Y             ; {ram.GP_00}
9627: 99 02 00        STA     $0002,Y             
962A: 88              DEY                         
962B: 10 F8           BPL     $9625               ; {}
962D: 60              RTS                         
962E: A5 00           LDA     $00                 ; {ram.GP_00}
9630: 18              CLC                         
9631: 69 9C           ADC     #$9C                
9633: 85 00           STA     $00                 ; {ram.GP_00}
9635: A5 01           LDA     $01                 
9637: 69 79           ADC     #$79                
9639: 85 01           STA     $01                 
963B: 4C 25 96        JMP     $9625               ; {}
963E: 20 B7 95        JSR     $95B7               ; {}
9641: 20 B4 96        JSR     $96B4               ; {}
9644: 20 C6 96        JSR     $96C6               ; {}
9647: A2 00           LDX     #$00                
9649: 18              CLC                         
964A: 8A              TXA                         
964B: 65 00           ADC     $00                 ; {ram.GP_00}
964D: A8              TAY                         
964E: B1 64           LDA     ($64),Y             
9650: 9D F0 03        STA     $03F0,X             
9653: E8              INX                         
9654: E0 08           CPX     #$08                
9656: 90 F1           BCC     $9649               ; {}
9658: A5 FD           LDA     $FD                 
965A: 29 10           AND     #$10                
965C: F0 2B           BEQ     $9689               ; {}
965E: A0 00           LDY     #$00                
9660: 18              CLC                         
9661: 98              TYA                         
9662: 65 00           ADC     $00                 ; {ram.GP_00}
9664: 85 01           STA     $01                 
9666: 98              TYA                         
9667: AA              TAX                         
9668: BD F0 03        LDA     $03F0,X             
966B: 29 F0           AND     #$F0                
966D: 85 02           STA     $02                 
966F: A5 01           LDA     $01                 
9671: AA              TAX                         
9672: BD B0 03        LDA     $03B0,X             
9675: 29 0F           AND     #$0F                
9677: 05 02           ORA     $02                 
9679: 85 02           STA     $02                 
967B: A5 01           LDA     $01                 
967D: AA              TAX                         
967E: A5 02           LDA     $02                 
9680: 9D B0 03        STA     $03B0,X             
9683: C8              INY                         
9684: C0 08           CPY     #$08                
9686: 90 D8           BCC     $9660               ; {}
9688: 60              RTS                         
9689: A0 00           LDY     #$00                
968B: 18              CLC                         
968C: 98              TYA                         
968D: 65 00           ADC     $00                 ; {ram.GP_00}
968F: 85 01           STA     $01                 
9691: 98              TYA                         
9692: AA              TAX                         
9693: BD F0 03        LDA     $03F0,X             
9696: 29 0F           AND     #$0F                
9698: 85 02           STA     $02                 
969A: A5 01           LDA     $01                 
969C: AA              TAX                         
969D: BD B0 03        LDA     $03B0,X             
96A0: 29 F0           AND     #$F0                
96A2: 05 02           ORA     $02                 
96A4: 85 02           STA     $02                 
96A6: A5 01           LDA     $01                 
96A8: AA              TAX                         
96A9: A5 02           LDA     $02                 
96AB: 9D B0 03        STA     $03B0,X             
96AE: C8              INY                         
96AF: C0 08           CPY     #$08                
96B1: 90 D8           BCC     $968B               ; {}
96B3: 60              RTS                         
96B4: AD D1 04        LDA     $04D1               
96B7: 29 01           AND     #$01                
96B9: 0A              ASL     A                   
96BA: A8              TAY                         
96BB: B9 E8 7B        LDA     $7BE8,Y             
96BE: 85 64           STA     $64                 
96C0: B9 E9 7B        LDA     $7BE9,Y             
96C3: 85 65           STA     $65                 
96C5: 60              RTS                         
96C6: A5 FD           LDA     $FD                 
96C8: 29 E0           AND     #$E0                
96CA: 4A              LSR     A                   
96CB: 4A              LSR     A                   
96CC: 85 00           STA     $00                 ; {ram.GP_00}
96CE: 60              RTS                         
96CF: 20 B7 95        JSR     $95B7               ; {}
96D2: A9 00           LDA     #$00                
96D4: 85 5C           STA     $5C                 
96D6: 8D D2 04        STA     $04D2               
96D9: 20 3F 97        JSR     $973F               ; {}
96DC: A9 06           LDA     #$06                
96DE: 20 90 CA        JSR     $CA90               
96E1: A9 00           LDA     #$00                
96E3: 8D D2 04        STA     $04D2               
96E6: EE D1 04        INC     $04D1               
96E9: 20 42 97        JSR     $9742               ; {}
96EC: A9 06           LDA     #$06                
96EE: 20 90 CA        JSR     $CA90               
96F1: 20 2A 97        JSR     $972A               ; {}
96F4: A9 FF           LDA     #$FF                
96F6: 85 1A           STA     $1A                 
96F8: A9 EE           LDA     #$EE                
96FA: 85 FD           STA     $FD                 
96FC: 20 6D 95        JSR     $956D               ; {}
96FF: 20 3E 96        JSR     $963E               ; {}
9702: 20 1D 95        JSR     $951D               ; {}
9705: 20 37 95        JSR     $9537               ; {}
9708: A5 FD           LDA     $FD                 
970A: 38              SEC                         
970B: E9 10           SBC     #$10                
970D: 85 FD           STA     $FD                 
970F: A5 1A           LDA     $1A                 
9711: E9 00           SBC     #$00                
9713: 85 1A           STA     $1A                 
9715: C9 FE           CMP     #$FE                
9717: B0 E3           BCS     $96FC               ; {}
9719: A9 FF           LDA     #$FF                
971B: 85 1A           STA     $1A                 
971D: A9 EE           LDA     #$EE                
971F: 85 FD           STA     $FD                 
9721: 60              RTS                         
9722: 20 3F 97        JSR     $973F               ; {}
9725: A9 06           LDA     #$06                
9727: 20 90 CA        JSR     $CA90               
972A: A0 0F           LDY     #$0F                
972C: B9 00 05        LDA     $0500,Y             
972F: 99 E0 06        STA     $06E0,Y             
9732: 88              DEY                         
9733: 10 F7           BPL     $972C               ; {}
9735: 60              RTS                         
9736: A5 5C           LDA     $5C                 
9738: 09 40           ORA     #$40                
973A: 85 5C           STA     $5C                 
973C: 68              PLA                         
973D: 68              PLA                         
973E: 60              RTS                         
973F: 20 B7 95        JSR     $95B7               ; {}
9742: A9 00           LDA     #$00                
9744: 8D D2 04        STA     $04D2               
9747: AD 30 01        LDA     $0130               
974A: 0A              ASL     A                   
974B: A8              TAY                         
974C: B9 F0 7B        LDA     $7BF0,Y             
974F: 85 00           STA     $00                 ; {ram.GP_00}
9751: B9 F1 7B        LDA     $7BF1,Y             
9754: 85 01           STA     $01                 
9756: AD D1 04        LDA     $04D1               
9759: 0A              ASL     A                   
975A: A8              TAY                         
975B: B1 00           LDA     ($00),Y             ; {ram.GP_00}
975D: 85 49           STA     $49                 
975F: C8              INY                         
9760: B1 00           LDA     ($00),Y             ; {ram.GP_00}
9762: C9 FF           CMP     #$FF                
9764: F0 D0           BEQ     $9736               ; {}
9766: 85 4A           STA     $4A                 
9768: 20 C2 95        JSR     $95C2               ; {}
976B: 20 B4 96        JSR     $96B4               ; {}
976E: 4C 8E 97        JMP     $978E               ; {}
9771: AD D1 04        LDA     $04D1               
9774: 0A              ASL     A                   
9775: A8              TAY                         
9776: B9 F6 7B        LDA     $7BF6,Y             
9779: 85 49           STA     $49                 
977B: B9 F7 7B        LDA     $7BF7,Y             
977E: 85 4A           STA     $4A                 
9780: A5 3A           LDA     $3A                 
9782: C9 10           CMP     #$10                
9784: 90 E2           BCC     $9768               ; {}
9786: A0 00           LDY     #$00                
9788: 20 C9 95        JSR     $95C9               ; {}
978B: 20 BB 96        JSR     $96BB               ; {}
978E: 20 68 98        JSR     $9868               ; {}
9791: A0 00           LDY     #$00                
9793: B1 49           LDA     ($49),Y             
9795: 20 73 98        JSR     $9873               ; {}
9798: A0 01           LDY     #$01                
979A: B1 49           LDA     ($49),Y             
979C: C9 FD           CMP     #$FD                
979E: F0 17           BEQ     $97B7               ; {}
97A0: 85 4D           STA     $4D                 
97A2: C8              INY                         
97A3: B1 49           LDA     ($49),Y             
97A5: 85 4E           STA     $4E                 
97A7: C8              INY                         
97A8: B1 49           LDA     ($49),Y             
97AA: 85 4F           STA     $4F                 
97AC: 98              TYA                         
97AD: 48              PHA                         
97AE: 20 B8 97        JSR     $97B8               ; {}
97B1: 68              PLA                         
97B2: A8              TAY                         
97B3: C8              INY                         
97B4: 4C 9A 97        JMP     $979A               ; {}
97B7: 60              RTS                         
97B8: 20 04 98        JSR     $9804               ; {}
97BB: A9 00           LDA     #$00                
97BD: 85 5F           STA     $5F                 
97BF: A5 4D           LDA     $4D                 
97C1: 29 F0           AND     #$F0                
97C3: 85 61           STA     $61                 
97C5: A5 5F           LDA     $5F                 
97C7: 0A              ASL     A                   
97C8: 0A              ASL     A                   
97C9: 0A              ASL     A                   
97CA: 0A              ASL     A                   
97CB: 18              CLC                         
97CC: 65 61           ADC     $61                 
97CE: C9 F0           CMP     #$F0                
97D0: B0 31           BCS     $9803               ; {}
97D2: A0 00           LDY     #$00                
97D4: B1 51           LDA     ($51),Y             
97D6: C9 FF           CMP     #$FF                
97D8: F0 29           BEQ     $9803               ; {}
97DA: 85 53           STA     $53                 
97DC: 29 0F           AND     #$0F                
97DE: AA              TAX                         
97DF: C8              INY                         
97E0: B1 51           LDA     ($51),Y             
97E2: 99 53 00        STA     $0053,Y             
97E5: C8              INY                         
97E6: CA              DEX                         
97E7: D0 F7           BNE     $97E0               ; {}
97E9: 20 85 98        JSR     $9885               ; {}
97EC: A5 53           LDA     $53                 
97EE: 29 0F           AND     #$0F                
97F0: 38              SEC                         
97F1: 65 51           ADC     $51                 
97F3: 85 51           STA     $51                 
97F5: A9 00           LDA     #$00                
97F7: 65 52           ADC     $52                 
97F9: 85 52           STA     $52                 
97FB: 20 24 98        JSR     $9824               ; {}
97FE: E6 5F           INC     $5F                 
9800: 4C BF 97        JMP     $97BF               ; {}
9803: 60              RTS                         
9804: A5 4E           LDA     $4E                 
9806: 0A              ASL     A                   
9807: A8              TAY                         
9808: A5 3A           LDA     $3A                 
980A: C9 10           CMP     #$10                
980C: B0 0B           BCS     $9819               ; {}
980E: B9 7C 7C        LDA     $7C7C,Y             
9811: 85 51           STA     $51                 
9813: B9 7D 7C        LDA     $7C7D,Y             
9816: 85 52           STA     $52                 
9818: 60              RTS                         
9819: B9 7C 7C        LDA     $7C7C,Y             
981C: 85 51           STA     $51                 
981E: B9 7D 7C        LDA     $7C7D,Y             
9821: 85 52           STA     $52                 
9823: 60              RTS                         
9824: A5 5F           LDA     $5F                 
9826: 0A              ASL     A                   
9827: 0A              ASL     A                   
9828: 0A              ASL     A                   
9829: 0A              ASL     A                   
982A: 85 5D           STA     $5D                 
982C: A5 53           LDA     $53                 
982E: 29 F0           AND     #$F0                
9830: 4A              LSR     A                   
9831: 4A              LSR     A                   
9832: 4A              LSR     A                   
9833: 4A              LSR     A                   
9834: 18              CLC                         
9835: 65 5D           ADC     $5D                 
9837: 85 5D           STA     $5D                 
9839: 18              CLC                         
983A: A5 4D           LDA     $4D                 
983C: 65 5D           ADC     $5D                 
983E: 85 5D           STA     $5D                 
9840: A5 53           LDA     $53                 
9842: 29 0F           AND     #$0F                
9844: AA              TAX                         
9845: 18              CLC                         
9846: A5 62           LDA     $62                 
9848: 65 5D           ADC     $5D                 
984A: 85 5D           STA     $5D                 
984C: A9 00           LDA     #$00                
984E: 65 63           ADC     $63                 
9850: 85 5E           STA     $5E                 
9852: A0 00           LDY     #$00                
9854: B9 54 00        LDA     $0054,Y             
9857: 91 5D           STA     ($5D),Y             
9859: 98              TYA                         
985A: 18              CLC                         
985B: 65 5D           ADC     $5D                 
985D: 29 0F           AND     #$0F                
985F: C9 0F           CMP     #$0F                
9861: B0 04           BCS     $9867               ; {}
9863: C8              INY                         
9864: CA              DEX                         
9865: D0 ED           BNE     $9854               ; {}
9867: 60              RTS                         
9868: A0 00           LDY     #$00                
986A: 98              TYA                         
986B: 91 62           STA     ($62),Y             
986D: C8              INY                         
986E: C0 F0           CPY     #$F0                
9870: 90 F9           BCC     $986B               ; {}
9872: 60              RTS                         
9873: 29 03           AND     #$03                
9875: A8              TAY                         
9876: B9 81 98        LDA     $9881,Y             ; {}
9879: A0 40           LDY     #$40                
987B: 91 64           STA     ($64),Y             
987D: 88              DEY                         
987E: 10 FB           BPL     $987B               ; {}
9880: 60              RTS                         
9881: 00              BRK                         
9882: 55 AA           EOR     $AA,X               
9884: FF ; ????
9885: A5 53           LDA     $53                 
9887: 29 F0           AND     #$F0                
9889: 4A              LSR     A                   
988A: 4A              LSR     A                   
988B: 4A              LSR     A                   
988C: 4A              LSR     A                   
988D: 8D D0 04        STA     $04D0               
9890: A5 53           LDA     $53                 
9892: 29 0F           AND     #$0F                
9894: 18              CLC                         
9895: 6D D0 04        ADC     $04D0               
9898: 8D D0 04        STA     $04D0               
989B: A5 4D           LDA     $4D                 
989D: 29 0F           AND     #$0F                
989F: 8D CD 04        STA     $04CD               
98A2: 18              CLC                         
98A3: 6D D0 04        ADC     $04D0               
98A6: C9 10           CMP     #$10                
98A8: 90 09           BCC     $98B3               ; {}
98AA: A9 10           LDA     #$10                
98AC: 38              SEC                         
98AD: ED CD 04        SBC     $04CD               
98B0: 8D D0 04        STA     $04D0               
98B3: A9 00           LDA     #$00                
98B5: 8D CD 04        STA     $04CD               
98B8: A5 5F           LDA     $5F                 
98BA: 0A              ASL     A                   
98BB: 0A              ASL     A                   
98BC: 0A              ASL     A                   
98BD: 0A              ASL     A                   
98BE: 18              CLC                         
98BF: 65 4D           ADC     $4D                 
98C1: 18              CLC                         
98C2: 6D CD 04        ADC     $04CD               
98C5: 85 60           STA     $60                 
98C7: 29 E0           AND     #$E0                
98C9: 4A              LSR     A                   
98CA: 4A              LSR     A                   
98CB: 85 66           STA     $66                 
98CD: A5 60           LDA     $60                 
98CF: 29 0F           AND     #$0F                
98D1: 4A              LSR     A                   
98D2: 18              CLC                         
98D3: 65 66           ADC     $66                 
98D5: 18              CLC                         
98D6: 65 64           ADC     $64                 
98D8: 85 66           STA     $66                 
98DA: A9 00           LDA     #$00                
98DC: 65 65           ADC     $65                 
98DE: 85 67           STA     $67                 
98E0: A5 60           LDA     $60                 
98E2: 29 10           AND     #$10                
98E4: 4A              LSR     A                   
98E5: 4A              LSR     A                   
98E6: 4A              LSR     A                   
98E7: 8D CE 04        STA     $04CE               
98EA: A5 60           LDA     $60                 
98EC: 29 01           AND     #$01                
98EE: 0D CE 04        ORA     $04CE               
98F1: F0 0E           BEQ     $9901               ; {}
98F3: AA              TAX                         
98F4: A9 03           LDA     #$03                
98F6: 0A              ASL     A                   
98F7: 0A              ASL     A                   
98F8: CA              DEX                         
98F9: 8D CE 04        STA     $04CE               
98FC: F0 08           BEQ     $9906               ; {}
98FE: 4C F6 98        JMP     $98F6               ; {}
9901: A9 03           LDA     #$03                
9903: 8D CE 04        STA     $04CE               
9906: AD CE 04        LDA     $04CE               
9909: 49 FF           EOR     #$FF                
990B: A0 00           LDY     #$00                
990D: 31 66           AND     ($66),Y             
990F: 8D CF 04        STA     $04CF               
9912: A5 4F           LDA     $4F                 
9914: 29 02           AND     #$02                
9916: F0 0B           BEQ     $9923               ; {}
9918: A9 AA           LDA     #$AA                
991A: 2D CE 04        AND     $04CE               
991D: 0D CF 04        ORA     $04CF               
9920: 8D CF 04        STA     $04CF               
9923: A5 4F           LDA     $4F                 
9925: 29 01           AND     #$01                
9927: F0 0B           BEQ     $9934               ; {}
9929: A9 55           LDA     #$55                
992B: 2D CE 04        AND     $04CE               
992E: 0D CF 04        ORA     $04CF               
9931: 8D CF 04        STA     $04CF               
9934: AD CF 04        LDA     $04CF               
9937: 91 66           STA     ($66),Y             
9939: EE CD 04        INC     $04CD               
993C: AD CD 04        LDA     $04CD               
993F: CD D0 04        CMP     $04D0               
9942: B0 03           BCS     $9947               ; {}
9944: 4C B8 98        JMP     $98B8               ; {}
9947: 60              RTS                         
9948: A9 10           LDA     #$10                
994A: 85 0A           STA     $0A                 
994C: E6 1A           INC     $1A                 
994E: 20 6D 95        JSR     $956D               ; {}
9951: 20 3E 96        JSR     $963E               ; {}
9954: 20 1D 95        JSR     $951D               ; {}
9957: 20 37 95        JSR     $9537               ; {}
995A: A5 FD           LDA     $FD                 
995C: 38              SEC                         
995D: E9 10           SBC     #$10                
995F: 85 FD           STA     $FD                 
9961: A5 1A           LDA     $1A                 
9963: E9 00           SBC     #$00                
9965: 85 1A           STA     $1A                 
9967: C6 0A           DEC     $0A                 
9969: 10 E3           BPL     $994E               ; {}
996B: A5 FD           LDA     $FD                 
996D: 18              CLC                         
996E: 69 10           ADC     #$10                
9970: 85 FD           STA     $FD                 
9972: A5 1A           LDA     $1A                 
9974: 69 00           ADC     #$00                
9976: 85 1A           STA     $1A                 
9978: 60              RTS                         
9979: 00              BRK                         
997A: 00              BRK                         
997B: 00              BRK                         
997C: 00              BRK                         
997D: 00              BRK                         
997E: 00              BRK                         
997F: 00              BRK                         
9980: 00              BRK                         
9981: 00              BRK                         
9982: 00              BRK                         
9983: 00              BRK                         
9984: 00              BRK                         
9985: 00              BRK                         
9986: 00              BRK                         
9987: 00              BRK                         
9988: 00              BRK                         
9989: 00              BRK                         
998A: 00              BRK                         
998B: 00              BRK                         
998C: 00              BRK                         
998D: 00              BRK                         
998E: 00              BRK                         
998F: 00              BRK                         
9990: 00              BRK                         
9991: 00              BRK                         
9992: 00              BRK                         
9993: 00              BRK                         
9994: 00              BRK                         
9995: 00              BRK                         
9996: 00              BRK                         
9997: 00              BRK                         
9998: 00              BRK                         
9999: 00              BRK                         
999A: 00              BRK                         
999B: 00              BRK                         
999C: 00              BRK                         
999D: 00              BRK                         
999E: 00              BRK                         
999F: 00              BRK                         
99A0: 4C FA 99        JMP     $99FA               ; {}
99A3: 4C 78 9A        JMP     $9A78               ; {}
99A6: 4C BB AD        JMP     $ADBB               ; {}
99A9: 4C 40 DF        JMP     $DF40               
99AC: 4C 3E AB        JMP     $AB3E               ; {}
99AF: 4C 70 AB        JMP     $AB70               ; {}
99B2: 4C E1 AA        JMP     $AAE1               ; {}
99B5: 4C 68 9A        JMP     $9A68               ; {}
99B8: 4C 09 B0        JMP     $B009               ; {}
99BB: 4C 03 9E        JMP     $9E03               ; {}
99BE: 4C 68 9A        JMP     $9A68               ; {}
99C1: 4C C7 AA        JMP     $AAC7               ; {}
99C4: 4C 31 9A        JMP     $9A31               ; {}
99C7: 4C 24 9B        JMP     $9B24               ; {}
99CA: 4C F7 9A        JMP     $9AF7               ; {}
99CD: 4C 07 AE        JMP     $AE07               ; {}
99D0: 4C 51 AE        JMP     $AE51               ; {}
99D3: 4C 7B AC        JMP     $AC7B               ; {}
99D6: 4C 2A AD        JMP     $AD2A               ; {}
99D9: 4C F3 AB        JMP     $ABF3               ; {}
99DC: 4C 47 AC        JMP     $AC47               ; {}
99DF: 4C D6 9D        JMP     $9DD6               ; {}
99E2: 67 ; ????
99E3: C5 E7           CMP     $E7                 
99E5: C5 38           CMP     $38                 
99E7: 9B ; ????
99E8: 78              SEI                         
99E9: 9B ; ????
99EA: A0 9B           LDY     #$9B                
99EC: C0 9B           CPY     #$9B                
99EE: E0 9B           CPX     #$9B                
99F0: 00              BRK                         
99F1: 9C ; ????
99F2: 00              BRK                         
99F3: 9C ; ????
99F4: 00              BRK                         
99F5: 9D FF EF        STA     $EFFF,X             
99F8: B4 BE           LDY     $BE,X               
99FA: 20 1D EB        JSR     $EB1D               
99FD: 20 F0 EE        JSR     $EEF0               
9A00: 20 E5 EE        JSR     $EEE5               
9A03: A9 01           LDA     #$01                
9A05: 8D 2F 01        STA     $012F               
9A08: 20 01 EB        JSR     $EB01               
9A0B: 20 2A C4        JSR     $C42A               
9A0E: 20 20 EF        JSR     $EF20               
9A11: 20 21 7F        JSR     $7F21               
9A14: 20 42 EE        JSR     $EE42               
9A17: 20 2E EF        JSR     $EF2E               
9A1A: 20 CA EE        JSR     $EECA               
9A1D: 20 E5 EE        JSR     $EEE5               
9A20: A9 08           LDA     #$08                
9A22: 20 90 CA        JSR     $CA90               
9A25: 20 F7 9A        JSR     $9AF7               ; {}
9A28: 20 53 C4        JSR     $C453               
9A2B: 20 3D C8        JSR     $C83D               
9A2E: 20 64 CB        JSR     $CB64               
9A31: A9 60           LDA     #$60                
9A33: 85 43           STA     $43                 
9A35: 20 01 EF        JSR     $EF01               
9A38: 20 21 EB        JSR     $EB21               
9A3B: 24 AB           BIT     $AB                 
9A3D: 70 13           BVS     $9A52               ; {}
9A3F: 30 14           BMI     $9A55               ; {}
9A41: 20 98 E1        JSR     $E198               
9A44: 20 D7 EA        JSR     $EAD7               
9A47: 20 B4 AB        JSR     $ABB4               ; {}
9A4A: 4C 38 9A        JMP     $9A38               ; {}
9A4D: E6 A0           INC     $A0                 
9A4F: 4C 6D C0        JMP     $C06D               
9A52: 4C A0 C0        JMP     $C0A0               
9A55: 20 F0 EE        JSR     $EEF0               
9A58: 20 89 EA        JSR     $EA89               
9A5B: EE 30 01        INC     $0130               
9A5E: AD 30 01        LDA     $0130               
9A61: C9 03           CMP     #$03                
9A63: B0 E8           BCS     $9A4D               ; {}
9A65: 4C 08 9A        JMP     $9A08               ; {}
9A68: 60              RTS                         
9A69: 20 9B EE        JSR     $EE9B               
9A6C: 20 0E EE        JSR     $EE0E               
9A6F: 20 B8 EE        JSR     $EEB8               
9A72: 4C B2 9A        JMP     $9AB2               ; {}
9A75: 4C C8 9A        JMP     $9AC8               ; {}
9A78: 8A              TXA                         
9A79: 48              PHA                         
9A7A: 98              TYA                         
9A7B: 48              PHA                         
9A7C: A5 45           LDA     $45                 
9A7E: D0 F5           BNE     $9A75               ; {}
9A80: E6 45           INC     $45                 
9A82: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
9A85: 20 2E EB        JSR     $EB2E               
9A88: A5 38           LDA     $38                 
9A8A: D0 DD           BNE     $9A69               ; {}
9A8C: A5 37           LDA     $37                 
9A8E: D0 3D           BNE     $9ACD               ; {}
9A90: A9 00           LDA     #$00                
9A92: 8D 01 20        STA     $2001               ; {hard.P_CNTRL_2}
9A95: 20 71 AB        JSR     $AB71               ; {}
9A98: 20 C9 EB        JSR     $EBC9               
9A9B: A5 FF           LDA     $FF                 
9A9D: 8D 01 20        STA     $2001               ; {hard.P_CNTRL_2}
9AA0: 20 7B AC        JSR     $AC7B               ; {}
9AA3: 20 2A AD        JSR     $AD2A               ; {}
9AA6: 20 9B EE        JSR     $EE9B               
9AA9: 20 07 9B        JSR     $9B07               ; {}
9AAC: 20 D9 EC        JSR     $ECD9               
9AAF: 20 B8 EE        JSR     $EEB8               
9AB2: 20 5D E1        JSR     $E15D               
9AB5: 20 E0 C3        JSR     $C3E0               
9AB8: 20 53 C4        JSR     $C453               
9ABB: 20 6A EE        JSR     $EE6A               
9ABE: 20 94 EE        JSR     $EE94               
9AC1: 20 56 C8        JSR     $C856               
9AC4: A9 00           LDA     #$00                
9AC6: 85 45           STA     $45                 
9AC8: 68              PLA                         
9AC9: A8              TAY                         
9ACA: 68              PLA                         
9ACB: AA              TAX                         
9ACC: 60              RTS                         
9ACD: 4A              LSR     A                   
9ACE: B0 E2           BCS     $9AB2               ; {}
9AD0: 4A              LSR     A                   
9AD1: B0 06           BCS     $9AD9               ; {}
9AD3: 20 42 EE        JSR     $EE42               
9AD6: 4C 98 9A        JMP     $9A98               ; {}
9AD9: A9 0A           LDA     #$0A                
9ADB: 20 90 CA        JSR     $CA90               
9ADE: A9 0C           LDA     #$0C                
9AE0: 20 90 CA        JSR     $CA90               
9AE3: 20 C9 EB        JSR     $EBC9               
9AE6: 20 9B EE        JSR     $EE9B               
9AE9: A9 02           LDA     #$02                
9AEB: 20 90 CA        JSR     $CA90               
9AEE: 20 D9 EC        JSR     $ECD9               
9AF1: 20 B8 EE        JSR     $EEB8               
9AF4: 4C B2 9A        JMP     $9AB2               ; {}
9AF7: 20 24 9B        JSR     $9B24               ; {}
9AFA: 20 43 D3        JSR     $D343               
9AFD: 20 96 A5        JSR     $A596               ; {}
9B00: 20 2F 9F        JSR     $9F2F               ; {}
9B03: 20 F9 A9        JSR     $A9F9               ; {}
9B06: 60              RTS                         
9B07: 20 B6 CB        JSR     $CBB6               
9B0A: 20 D9 C3        JSR     $C3D9               
9B0D: AD 21 07        LDA     $0721               
9B10: 29 70           AND     #$70                
9B12: D0 0F           BNE     $9B23               ; {}
9B14: 20 A2 D4        JSR     $D4A2               
9B17: 20 97 A5        JSR     $A597               ; {}
9B1A: 20 30 9F        JSR     $9F30               ; {}
9B1D: 20 27 A3        JSR     $A327               ; {}
9B20: 20 07 AA        JSR     $AA07               ; {}
9B23: 60              RTS                         
9B24: A2 20           LDX     #$20                
9B26: A9 BA           LDA     #$BA                
9B28: 9D 00 07        STA     $0700,X             
9B2B: A9 00           LDA     #$00                
9B2D: 9D 02 07        STA     $0702,X             
9B30: A9 34           LDA     #$34                
9B32: 9D 03 07        STA     $0703,X             
9B35: 4C BF C3        JMP     $C3BF               
9B38: 02 ; ????
9B39: 70 71           BVS     $9BAC               ; {}
9B3B: 72 ; ????
9B3C: 73 ; ????
9B3D: 74 ; ????
9B3E: 75 00           ADC     $00,X               ; {ram.GP_00}
9B40: 42 ; ????
9B41: 71 70           ADC     ($70),Y             
9B43: 73 ; ????
9B44: 72 ; ????
9B45: 75 74           ADC     $74,X               
9B47: 00              BRK                         
9B48: 02 ; ????
9B49: 70 71           BVS     $9BBC               ; {}
9B4B: 72 ; ????
9B4C: 73 ; ????
9B4D: 76 77           ROR     $77,X               
9B4F: 00              BRK                         
9B50: 42 ; ????
9B51: 71 70           ADC     ($70),Y             
9B53: 73 ; ????
9B54: 72 ; ????
9B55: 77 ; ????
9B56: 76 00           ROR     $00,X               ; {ram.GP_00}
9B58: 02 ; ????
9B59: B0 B1           BCS     $9B0C               ; {}
9B5B: B2 ; ????
9B5C: B3 ; ????
9B5D: B4 B5           LDY     $B5,X               
9B5F: 00              BRK                         
9B60: 42 ; ????
9B61: B1 B0           LDA     ($B0),Y             
9B63: B3 ; ????
9B64: B2 ; ????
9B65: B5 B4           LDA     $B4,X               
9B67: 00              BRK                         
9B68: 02 ; ????
9B69: B0 B1           BCS     $9B1C               ; {}
9B6B: B2 ; ????
9B6C: B3 ; ????
9B6D: B6 B7           LDX     $B7,Y               
9B6F: 00              BRK                         
9B70: 42 ; ????
9B71: B1 B0           LDA     ($B0),Y             
9B73: B3 ; ????
9B74: B2 ; ????
9B75: B7 ; ????
9B76: B6 00           LDX     $00,Y               ; {ram.GP_00}
9B78: 4B ; ????
9B79: 4B ; ????
9B7A: 4B ; ????
9B7B: 4B ; ????
9B7C: 5A ; ????
9B7D: 5A ; ????
9B7E: 5A ; ????
9B7F: 5A ; ????
9B80: 4A              LSR     A                   
9B81: 4A              LSR     A                   
9B82: 4A              LSR     A                   
9B83: 4A              LSR     A                   
9B84: 95 5F           STA     $5F,X               
9B86: 96 5F           STX     $5F,Y               
9B88: 9B ; ????
9B89: 5F ; ????
9B8A: 9C ; ????
9B8B: 5F ; ????
9B8C: 3F ; ????
9B8D: 5F ; ????
9B8E: 4F ; ????
9B8F: 5F ; ????
9B90: 48              PHA                         
9B91: 5F ; ????
9B92: 58              CLI                         
9B93: 5F ; ????
9B94: 49 5F           EOR     #$5F                
9B96: 59 5F AA        EOR     $AA5F,Y             ; {}
9B99: 5F ; ????
9B9A: AB ; ????
9B9B: 5F ; ????
9B9C: 34 ; ????
9B9D: 5F ; ????
9B9E: 55 5F           EOR     $5F,X               
9BA0: 16 17           ASL     $17,X               
9BA2: 90 91           BCC     $9B35               ; {}
9BA4: 17 ; ????
9BA5: 16 91           ASL     $91,X               
9BA7: 90 E0           BCC     $9B89               ; {}
9BA9: E1 E2           SBC     ($E2,X)             
9BAB: E3 ; ????
9BAC: E1 E0           SBC     ($E0,X)             
9BAE: E3 ; ????
9BAF: E2 ; ????
9BB0: E4 E5           CPX     $E5                 
9BB2: E6 E7           INC     $E7                 
9BB4: E5 E4           SBC     $E4                 
9BB6: E7 ; ????
9BB7: E6 E8           INC     $E8                 
9BB9: E9 EA           SBC     #$EA                
9BBB: EB ; ????
9BBC: E9 E8           SBC     #$E8                
9BBE: EB ; ????
9BBF: EA              NOP                         
9BC0: D0 D1           BNE     $9B93               ; {}
9BC2: D4 ; ????
9BC3: D5 D1           CMP     $D1,X               
9BC5: D0 D5           BNE     $9B9C               ; {}
9BC7: D4 ; ????
9BC8: D2 ; ????
9BC9: D3 ; ????
9BCA: D6 D7           DEC     $D7,X               
9BCC: D3 ; ????
9BCD: D2 ; ????
9BCE: D7 ; ????
9BCF: D6 F0           DEC     $F0,X               
9BD1: F1 F2           SBC     ($F2),Y             
9BD3: F3 ; ????
9BD4: F1 F0           SBC     ($F0),Y             
9BD6: F3 ; ????
9BD7: F2 ; ????
9BD8: 00              BRK                         
9BD9: 00              BRK                         
9BDA: 00              BRK                         
9BDB: 00              BRK                         
9BDC: 00              BRK                         
9BDD: 00              BRK                         
9BDE: 00              BRK                         
9BDF: 00              BRK                         
9BE0: 9F ; ????
9BE1: 5F ; ????
9BE2: AF ; ????
9BE3: 5F ; ????
9BE4: 8E 5F 8F        STX     $8F5F               ; {}
9BE7: 5F ; ????
9BE8: 34 ; ????
9BE9: 5F ; ????
9BEA: 8F ; ????
9BEB: 5F ; ????
9BEC: CD CC CF        CMP     $CFCC               
9BEF: CE D8 D9        DEC     $D9D8               
9BF2: DC ; ????
9BF3: DD D9 D8        CMP     $D8D9,X             
9BF6: DD DC DA        CMP     $DADC,X             
9BF9: DB ; ????
9BFA: DE DF DB        DEC     $DBDF,X             
9BFD: DA ; ????
9BFE: DF ; ????
9BFF: DE 7F 00        DEC     $007F,X             
9C02: 00              BRK                         
9C03: 00              BRK                         
9C04: 7F ; ????
9C05: 00              BRK                         
9C06: 00              BRK                         
9C07: 00              BRK                         
9C08: 7F ; ????
9C09: 00              BRK                         
9C0A: 00              BRK                         
9C0B: 00              BRK                         
9C0C: FC ; ????
9C0D: 27 ; ????
9C0E: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9C10: F8              SED                         
9C11: 94 01           STY     $01,X               
9C13: 00              BRK                         
9C14: 7F ; ????
9C15: 00              BRK                         
9C16: 00              BRK                         
9C17: 00              BRK                         
9C18: 00              BRK                         
9C19: AE 01 00        LDX     $0001               
9C1C: 7F ; ????
9C1D: 00              BRK                         
9C1E: 00              BRK                         
9C1F: 00              BRK                         
9C20: F8              SED                         
9C21: 5B ; ????
9C22: 00              BRK                         
9C23: FC ; ????
9C24: F8              SED                         
9C25: 5B ; ????
9C26: 40              RTI                         
9C27: 04 ; ????
9C28: 00              BRK                         
9C29: 5C ; ????
9C2A: 00              BRK                         
9C2B: FC ; ????
9C2C: 00              BRK                         
9C2D: 5C ; ????
9C2E: 40              RTI                         
9C2F: 04 ; ????
9C30: F8              SED                         
9C31: 0E 00 FC        ASL     $FC00               
9C34: F8              SED                         
9C35: 0E 40 04        ASL     $0440               
9C38: 00              BRK                         
9C39: 1E 00 FC        ASL     $FC00,X             
9C3C: 00              BRK                         
9C3D: 1E 40 04        ASL     $0440,X             
9C40: F8              SED                         
9C41: CA              DEX                         
9C42: 02 ; ????
9C43: FC ; ????
9C44: F8              SED                         
9C45: CB ; ????
9C46: 02 ; ????
9C47: 04 ; ????
9C48: 00              BRK                         
9C49: CB ; ????
9C4A: C2 ; ????
9C4B: FC ; ????
9C4C: 00              BRK                         
9C4D: CB ; ????
9C4E: 82 ; ????
9C4F: 04 ; ????
9C50: F8              SED                         
9C51: 98              TYA                         
9C52: 00              BRK                         
9C53: F4 ; ????
9C54: F8              SED                         
9C55: 98              TYA                         
9C56: 00              BRK                         
9C57: FC ; ????
9C58: F8              SED                         
9C59: 98              TYA                         
9C5A: 00              BRK                         
9C5B: 04 ; ????
9C5C: F8              SED                         
9C5D: 98              TYA                         
9C5E: 00              BRK                         
9C5F: 0C ; ????
9C60: 7F ; ????
9C61: 00              BRK                         
9C62: 00              BRK                         
9C63: 00              BRK                         
9C64: F8              SED                         
9C65: 98              TYA                         
9C66: 00              BRK                         
9C67: FC ; ????
9C68: F8              SED                         
9C69: 98              TYA                         
9C6A: 00              BRK                         
9C6B: 04 ; ????
9C6C: 7F ; ????
9C6D: 00              BRK                         
9C6E: 00              BRK                         
9C6F: 00              BRK                         
9C70: 00              BRK                         
9C71: 00              BRK                         
9C72: 00              BRK                         
9C73: 00              BRK                         
9C74: 00              BRK                         
9C75: 00              BRK                         
9C76: 00              BRK                         
9C77: 00              BRK                         
9C78: 00              BRK                         
9C79: 00              BRK                         
9C7A: 00              BRK                         
9C7B: 00              BRK                         
9C7C: 00              BRK                         
9C7D: 00              BRK                         
9C7E: 00              BRK                         
9C7F: 00              BRK                         
9C80: 00              BRK                         
9C81: 00              BRK                         
9C82: 00              BRK                         
9C83: 00              BRK                         
9C84: 00              BRK                         
9C85: 00              BRK                         
9C86: 00              BRK                         
9C87: 00              BRK                         
9C88: 00              BRK                         
9C89: 00              BRK                         
9C8A: 00              BRK                         
9C8B: 00              BRK                         
9C8C: 00              BRK                         
9C8D: 00              BRK                         
9C8E: 00              BRK                         
9C8F: 00              BRK                         
9C90: 00              BRK                         
9C91: 00              BRK                         
9C92: 00              BRK                         
9C93: 00              BRK                         
9C94: 00              BRK                         
9C95: 00              BRK                         
9C96: 00              BRK                         
9C97: 00              BRK                         
9C98: 00              BRK                         
9C99: 00              BRK                         
9C9A: 00              BRK                         
9C9B: 00              BRK                         
9C9C: 00              BRK                         
9C9D: 00              BRK                         
9C9E: 00              BRK                         
9C9F: 00              BRK                         
9CA0: 7F ; ????
9CA1: 00              BRK                         
9CA2: 00              BRK                         
9CA3: 00              BRK                         
9CA4: 7F ; ????
9CA5: 00              BRK                         
9CA6: 00              BRK                         
9CA7: 00              BRK                         
9CA8: 00              BRK                         
9CA9: EC 03 FC        CPX     $FC03               
9CAC: 00              BRK                         
9CAD: EC 43 04        CPX     $0443               
9CB0: 7F ; ????
9CB1: 00              BRK                         
9CB2: 00              BRK                         
9CB3: 00              BRK                         
9CB4: 7F ; ????
9CB5: 00              BRK                         
9CB6: 00              BRK                         
9CB7: 00              BRK                         
9CB8: 00              BRK                         
9CB9: EE 03 FC        INC     $FC03               
9CBC: 00              BRK                         
9CBD: EE 43 04        INC     $0443               
9CC0: F8              SED                         
9CC1: EC 03 FC        CPX     $FC03               
9CC4: F8              SED                         
9CC5: EC 43 04        CPX     $0443               
9CC8: 00              BRK                         
9CC9: ED 03 FC        SBC     $FC03               
9CCC: 00              BRK                         
9CCD: ED 43 04        SBC     $0443               
9CD0: F8              SED                         
9CD1: EE 03 FC        INC     $FC03               
9CD4: F8              SED                         
9CD5: EE 43 04        INC     $0443               
9CD8: 00              BRK                         
9CD9: EF ; ????
9CDA: 03 ; ????
9CDB: FC ; ????
9CDC: 00              BRK                         
9CDD: EF ; ????
9CDE: 43 ; ????
9CDF: 04 ; ????
9CE0: F8              SED                         
9CE1: 46 00           LSR     $00                 ; {ram.GP_00}
9CE3: FC ; ????
9CE4: F8              SED                         
9CE5: 47 ; ????
9CE6: 00              BRK                         
9CE7: 04 ; ????
9CE8: 00              BRK                         
9CE9: 56 00           LSR     $00,X               ; {ram.GP_00}
9CEB: FC ; ????
9CEC: 00              BRK                         
9CED: 57 ; ????
9CEE: 00              BRK                         
9CEF: 04 ; ????
9CF0: 00              BRK                         
9CF1: 00              BRK                         
9CF2: 00              BRK                         
9CF3: 00              BRK                         
9CF4: 00              BRK                         
9CF5: 00              BRK                         
9CF6: 00              BRK                         
9CF7: 00              BRK                         
9CF8: 00              BRK                         
9CF9: 00              BRK                         
9CFA: 00              BRK                         
9CFB: 00              BRK                         
9CFC: 00              BRK                         
9CFD: 00              BRK                         
9CFE: 00              BRK                         
9CFF: 00              BRK                         
9D00: F8              SED                         
9D01: BD 02 FC        LDA     $FC02,X             
9D04: F8              SED                         
9D05: BD 42 04        LDA     $0442,X             
9D08: 00              BRK                         
9D09: BD 82 FC        LDA     $FC82,X             
9D0C: 00              BRK                         
9D0D: BD C2 04        LDA     $04C2,X             
9D10: F8              SED                         
9D11: BE 02 FC        LDX     $FC02,Y             
9D14: F8              SED                         
9D15: BE 42 04        LDX     $0442,Y             
9D18: 00              BRK                         
9D19: BF ; ????
9D1A: 02 ; ????
9D1B: FC ; ????
9D1C: 00              BRK                         
9D1D: BF ; ????
9D1E: 42 ; ????
9D1F: 04 ; ????
9D20: F8              SED                         
9D21: 2A              ROL     A                   
9D22: 02 ; ????
9D23: FC ; ????
9D24: F8              SED                         
9D25: 2A              ROL     A                   
9D26: 02 ; ????
9D27: 04 ; ????
9D28: 00              BRK                         
9D29: 2A              ROL     A                   
9D2A: 82 ; ????
9D2B: FC ; ????
9D2C: 00              BRK                         
9D2D: 2A              ROL     A                   
9D2E: 82 ; ????
9D2F: 04 ; ????
9D30: F8              SED                         
9D31: BF ; ????
9D32: 82 ; ????
9D33: FC ; ????
9D34: F8              SED                         
9D35: BF ; ????
9D36: C2 ; ????
9D37: 04 ; ????
9D38: 00              BRK                         
9D39: BE 82 FC        LDX     $FC82,Y             
9D3C: 00              BRK                         
9D3D: BE C2 04        LDX     $04C2,Y             
9D40: F8              SED                         
9D41: FA ; ????
9D42: 02 ; ????
9D43: FC ; ????
9D44: F8              SED                         
9D45: FA ; ????
9D46: 42 ; ????
9D47: 04 ; ????
9D48: 00              BRK                         
9D49: F7 ; ????
9D4A: 02 ; ????
9D4B: FC ; ????
9D4C: 00              BRK                         
9D4D: F7 ; ????
9D4E: 42 ; ????
9D4F: 04 ; ????
9D50: F8              SED                         
9D51: C8              INY                         
9D52: 02 ; ????
9D53: FC ; ????
9D54: F8              SED                         
9D55: C8              INY                         
9D56: 42 ; ????
9D57: 04 ; ????
9D58: 00              BRK                         
9D59: C9 02           CMP     #$02                
9D5B: FC ; ????
9D5C: 00              BRK                         
9D5D: C9 42           CMP     #$42                
9D5F: 04 ; ????
9D60: F8              SED                         
9D61: 50 00           BVC     $9D63               ; {}
9D63: FC ; ????
9D64: F8              SED                         
9D65: 50 40           BVC     $9DA7               ; {}
9D67: 04 ; ????
9D68: 00              BRK                         
9D69: 51 00           EOR     ($00),Y             ; {ram.GP_00}
9D6B: FC ; ????
9D6C: 00              BRK                         
9D6D: 51 40           EOR     ($40),Y             
9D6F: 04 ; ????
9D70: F8              SED                         
9D71: 3E 00 FC        ROL     $FC00,X             
9D74: 7F ; ????
9D75: 00              BRK                         
9D76: 00              BRK                         
9D77: 00              BRK                         
9D78: 00              BRK                         
9D79: 3E 80 FC        ROL     $FC80,X             
9D7C: 7F ; ????
9D7D: 00              BRK                         
9D7E: 00              BRK                         
9D7F: 00              BRK                         
9D80: F8              SED                         
9D81: 52 ; ????
9D82: 00              BRK                         
9D83: 04 ; ????
9D84: 7F ; ????
9D85: 00              BRK                         
9D86: 00              BRK                         
9D87: 00              BRK                         
9D88: 00              BRK                         
9D89: 52 ; ????
9D8A: 80 ; ????
9D8B: 04 ; ????
9D8C: 7F ; ????
9D8D: 00              BRK                         
9D8E: 00              BRK                         
9D8F: 00              BRK                         
9D90: F8              SED                         
9D91: 3D 00 FC        AND     $FC00,X             
9D94: F8              SED                         
9D95: 3D 40 03        AND     $0340,X             
9D98: 00              BRK                         
9D99: 4D 00 FC        EOR     $FC00               
9D9C: 00              BRK                         
9D9D: 4D 40 03        EOR     $0340               
9DA0: F8              SED                         
9DA1: 92 ; ????
9DA2: 01 FD           ORA     ($FD,X)             
9DA4: F8              SED                         
9DA5: 94 01           STY     $01,X               
9DA7: 03 ; ????
9DA8: 00              BRK                         
9DA9: 93 ; ????
9DAA: 01 FD           ORA     ($FD,X)             
9DAC: 00              BRK                         
9DAD: AE 01 03        LDX     $0301               
9DB0: F8              SED                         
9DB1: 9A              TXS                         
9DB2: 01 F4           ORA     ($F4,X)             
9DB4: F8              SED                         
9DB5: 9A              TXS                         
9DB6: 01 FC           ORA     ($FC,X)             
9DB8: F8              SED                         
9DB9: 9A              TXS                         
9DBA: 01 04           ORA     ($04,X)             
9DBC: F8              SED                         
9DBD: 9A              TXS                         
9DBE: 01 0C           ORA     ($0C,X)             
9DC0: F8              SED                         
9DC1: 0E 00 FC        ASL     $FC00               
9DC4: F8              SED                         
9DC5: 0E 40 04        ASL     $0440               
9DC8: 00              BRK                         
9DC9: 5C ; ????
9DCA: 00              BRK                         
9DCB: FC ; ????
9DCC: 00              BRK                         
9DCD: 5C ; ????
9DCE: 40              RTI                         
9DCF: 04 ; ????
9DD0: A9 80           LDA     #$80                
9DD2: 8D 80 03        STA     $0380               
9DD5: 60              RTS                         
9DD6: 98              TYA                         
9DD7: 48              PHA                         
9DD8: BD 01 07        LDA     $0701,X             
9DDB: 29 F8           AND     #$F8                
9DDD: 4A              LSR     A                   
9DDE: 4A              LSR     A                   
9DDF: 4A              LSR     A                   
9DE0: A8              TAY                         
9DE1: B9 96 BE        LDA     $BE96,Y             ; {}
9DE4: 9D 07 07        STA     $0707,X             
9DE7: A9 00           LDA     #$00                
9DE9: 9D 08 07        STA     $0708,X             
9DEC: 68              PLA                         
9DED: A8              TAY                         
9DEE: 60              RTS                         
9DEF: 98              TYA                         
9DF0: 48              PHA                         
9DF1: BD 01 07        LDA     $0701,X             
9DF4: 29 F8           AND     #$F8                
9DF6: 4A              LSR     A                   
9DF7: 4A              LSR     A                   
9DF8: 4A              LSR     A                   
9DF9: A8              TAY                         
9DFA: B9 96 BE        LDA     $BE96,Y             ; {}
9DFD: 9D 07 07        STA     $0707,X             
9E00: 68              PLA                         
9E01: A8              TAY                         
9E02: 60              RTS                         
9E03: BD 01 07        LDA     $0701,X             
9E06: 4A              LSR     A                   
9E07: 4A              LSR     A                   
9E08: 4A              LSR     A                   
9E09: A8              TAY                         
9E0A: B9 A5 BE        LDA     $BEA5,Y             ; {}
9E0D: 60              RTS                         
9E0E: A9 A0           LDA     #$A0                
9E10: 9D 00 07        STA     $0700,X             
9E13: A5 26           LDA     $26                 
9E15: 29 10           AND     #$10                
9E17: 18              CLC                         
9E18: 69 CA           ADC     #$CA                
9E1A: 9D 02 07        STA     $0702,X             
9E1D: A9 F0           LDA     #$F0                
9E1F: 9D 03 07        STA     $0703,X             
9E22: A9 00           LDA     #$00                
9E24: 9D 04 07        STA     $0704,X             
9E27: 9D 05 07        STA     $0705,X             
9E2A: 20 D6 9D        JSR     $9DD6               ; {}
9E2D: 60              RTS                         
9E2E: A2 F0           LDX     #$F0                
9E30: BD 01 07        LDA     $0701,X             
9E33: 29 F8           AND     #$F8                
9E35: C9 30           CMP     #$30                
9E37: D0 F4           BNE     $9E2D               ; {}
9E39: 20 08 DD        JSR     $DD08               
9E3C: BD 01 07        LDA     $0701,X             
9E3F: 29 07           AND     #$07                
9E41: 20 2B EE        JSR     $EE2B               
9E44: E6 9E           INC     $9E                 
9E46: 52 ; ????
9E47: 9E ; ????
9E48: B1 9E           LDA     ($9E),Y             
9E4A: 4C 9E 20        JMP     $209E               
9E4D: 17 ; ????
9E4E: 9F ; ????
9E4F: 4C 65 DD        JMP     $DD65               
9E52: BD 02 07        LDA     $0702,X             
9E55: 29 0F           AND     #$0F                
9E57: C9 08           CMP     #$08                
9E59: B0 44           BCS     $9E9F               ; {}
9E5B: A9 B0           LDA     #$B0                
9E5D: 85 08           STA     $08                 
9E5F: A9 30           LDA     #$30                
9E61: 85 09           STA     $09                 
9E63: A9 60           LDA     #$60                
9E65: 85 0A           STA     $0A                 
9E67: 20 6D C7        JSR     $C76D               
9E6A: 20 F5 9E        JSR     $9EF5               ; {}
9E6D: 20 90 D9        JSR     $D990               
9E70: 90 15           BCC     $9E87               ; {}
9E72: 20 E7 D9        JSR     $D9E7               
9E75: 90 15           BCC     $9E8C               ; {}
9E77: 20 09 DA        JSR     $DA09               
9E7A: 20 62 DF        JSR     $DF62               
9E7D: 20 C0 DB        JSR     $DBC0               
9E80: 20 23 9F        JSR     $9F23               ; {}
9E83: 20 DE DC        JSR     $DCDE               
9E86: 60              RTS                         
9E87: A9 F8           LDA     #$F8                
9E89: 99 00 07        STA     $0700,Y             
9E8C: 20 D0 9D        JSR     $9DD0               ; {}
9E8F: 20 A9 DC        JSR     $DCA9               
9E92: BD 01 07        LDA     $0701,X             
9E95: 29 F8           AND     #$F8                
9E97: 09 03           ORA     #$03                
9E99: 9D 01 07        STA     $0701,X             
9E9C: 4C 45 A6        JMP     $A645               ; {}
9E9F: A9 30           LDA     #$30                
9EA1: 85 08           STA     $08                 
9EA3: A9 30           LDA     #$30                
9EA5: 85 09           STA     $09                 
9EA7: A9 60           LDA     #$60                
9EA9: 85 0A           STA     $0A                 
9EAB: 20 8D C7        JSR     $C78D               
9EAE: 4C 6D 9E        JMP     $9E6D               ; {}
9EB1: BD 02 07        LDA     $0702,X             
9EB4: 29 0F           AND     #$0F                
9EB6: C9 08           CMP     #$08                
9EB8: B0 16           BCS     $9ED0               ; {}
9EBA: AD 23 07        LDA     $0723               
9EBD: 18              CLC                         
9EBE: 69 10           ADC     #$10                
9EC0: 85 08           STA     $08                 
9EC2: A9 30           LDA     #$30                
9EC4: 85 09           STA     $09                 
9EC6: A9 F8           LDA     #$F8                
9EC8: 85 0A           STA     $0A                 
9ECA: 20 6D C7        JSR     $C76D               
9ECD: 4C 6D 9E        JMP     $9E6D               ; {}
9ED0: AD 23 07        LDA     $0723               
9ED3: 38              SEC                         
9ED4: E9 10           SBC     #$10                
9ED6: 85 08           STA     $08                 
9ED8: A9 30           LDA     #$30                
9EDA: 85 09           STA     $09                 
9EDC: A9 F8           LDA     #$F8                
9EDE: 85 0A           STA     $0A                 
9EE0: 20 8D C7        JSR     $C78D               
9EE3: 4C 6D 9E        JMP     $9E6D               ; {}
9EE6: 8A              TXA                         
9EE7: 18              CLC                         
9EE8: 65 14           ADC     $14                 
9EEA: 29 7F           AND     #$7F                
9EEC: D0 06           BNE     $9EF4               ; {}
9EEE: 20 0E 9E        JSR     $9E0E               ; {}
9EF1: FE 01 07        INC     $0701,X             
9EF4: 60              RTS                         
9EF5: A5 15           LDA     $15                 
9EF7: 29 03           AND     #$03                
9EF9: C9 03           CMP     #$03                
9EFB: D0 19           BNE     $9F16               ; {}
9EFD: AD 23 07        LDA     $0723               
9F00: 38              SEC                         
9F01: FD 03 07        SBC     $0703,X             
9F04: B0 02           BCS     $9F08               ; {}
9F06: 49 FF           EOR     #$FF                
9F08: C9 04           CMP     #$04                
9F0A: B0 0A           BCS     $9F16               ; {}
9F0C: BD 01 07        LDA     $0701,X             
9F0F: 29 F8           AND     #$F8                
9F11: 09 02           ORA     #$02                
9F13: 9D 01 07        STA     $0701,X             
9F16: 60              RTS                         
9F17: 48              PHA                         
9F18: BD 03 07        LDA     $0703,X             
9F1B: 38              SEC                         
9F1C: E5 27           SBC     $27                 
9F1E: 9D 03 07        STA     $0703,X             
9F21: 68              PLA                         
9F22: 60              RTS                         
9F23: A0 54           LDY     #$54                
9F25: BD 04 07        LDA     $0704,X             
9F28: 30 01           BMI     $9F2B               ; {}
9F2A: C8              INY                         
9F2B: 98              TYA                         
9F2C: 4C CD C4        JMP     $C4CD               
9F2F: 60              RTS                         
9F30: 20 36 A9        JSR     $A936               ; {}
9F33: AD 61 07        LDA     $0761               
9F36: 0D 71 07        ORA     $0771               
9F39: 0D 81 07        ORA     $0781               
9F3C: 0D 91 07        ORA     $0791               
9F3F: F0 13           BEQ     $9F54               ; {}
9F41: 20 C6 A3        JSR     $A3C6               ; {}
9F44: 20 DB A0        JSR     $A0DB               ; {}
9F47: 20 9C 9F        JSR     $9F9C               ; {}
9F4A: 20 DD 9F        JSR     $9FDD               ; {}
9F4D: 20 93 A9        JSR     $A993               ; {}
9F50: 20 01 A5        JSR     $A501               ; {}
9F53: 60              RTS                         
9F54: AD 30 01        LDA     $0130               
9F57: 0A              ASL     A                   
9F58: A8              TAY                         
9F59: B9 3F BC        LDA     $BC3F,Y             ; {}
9F5C: 85 00           STA     $00                 ; {ram.GP_00}
9F5E: B9 40 BC        LDA     $BC40,Y             ; {}
9F61: 85 01           STA     $01                 
9F63: AC D1 04        LDY     $04D1               
9F66: B1 00           LDA     ($00),Y             ; {ram.GP_00}
9F68: C9 0D           CMP     #$0D                
9F6A: F0 2E           BEQ     $9F9A               ; {}
9F6C: 0A              ASL     A                   
9F6D: 0A              ASL     A                   
9F6E: 0A              ASL     A                   
9F6F: 20 9D DC        JSR     $DC9D               
9F72: 8D 61 07        STA     $0761               
9F75: 8D 71 07        STA     $0771               
9F78: 8D 81 07        STA     $0781               
9F7B: 8D 91 07        STA     $0791               
9F7E: A9 9A           LDA     #$9A                
9F80: 8D 60 07        STA     $0760               
9F83: 8D 70 07        STA     $0770               
9F86: 8D 80 07        STA     $0780               
9F89: 8D 90 07        STA     $0790               
9F8C: A9 F7           LDA     #$F7                
9F8E: 8D 63 07        STA     $0763               
9F91: 8D 73 07        STA     $0773               
9F94: 8D 83 07        STA     $0783               
9F97: 8D 93 07        STA     $0793               
9F9A: 60              RTS                         
9F9B: 60              RTS                         
9F9C: A2 60           LDX     #$60                
9F9E: 20 B0 9F        JSR     $9FB0               ; {}
9FA1: A2 70           LDX     #$70                
9FA3: 20 B0 9F        JSR     $9FB0               ; {}
9FA6: A2 80           LDX     #$80                
9FA8: 20 B0 9F        JSR     $9FB0               ; {}
9FAB: A2 90           LDX     #$90                
9FAD: 4C B0 9F        JMP     $9FB0               ; {}
9FB0: BD 01 07        LDA     $0701,X             
9FB3: 29 F8           AND     #$F8                
9FB5: C9 40           CMP     #$40                
9FB7: D0 E2           BNE     $9F9B               ; {}
9FB9: 4C 39 9E        JMP     $9E39               ; {}
9FBC: A9 00           LDA     #$00                
9FBE: 9D 04 07        STA     $0704,X             
9FC1: 9D 05 07        STA     $0705,X             
9FC4: A9 80           LDA     #$80                
9FC6: 9D 06 07        STA     $0706,X             
9FC9: 20 D6 9D        JSR     $9DD6               ; {}
9FCC: A9 F0           LDA     #$F0                
9FCE: 9D 00 07        STA     $0700,X             
9FD1: 8A              TXA                         
9FD2: 38              SEC                         
9FD3: E9 60           SBC     #$60                
9FD5: 0A              ASL     A                   
9FD6: 18              CLC                         
9FD7: 69 40           ADC     #$40                
9FD9: 9D 03 07        STA     $0703,X             
9FDC: 60              RTS                         
9FDD: A2 60           LDX     #$60                
9FDF: 20 EE 9F        JSR     $9FEE               ; {}
9FE2: A2 70           LDX     #$70                
9FE4: 20 EE 9F        JSR     $9FEE               ; {}
9FE7: A2 80           LDX     #$80                
9FE9: 20 EE 9F        JSR     $9FEE               ; {}
9FEC: A2 90           LDX     #$90                
9FEE: BD 01 07        LDA     $0701,X             
9FF1: 29 F8           AND     #$F8                
9FF3: C9 50           CMP     #$50                
9FF5: D0 33           BNE     $A02A               ; {}
9FF7: 20 87 E0        JSR     $E087               
9FFA: 20 17 9F        JSR     $9F17               ; {}
9FFD: 20 08 DD        JSR     $DD08               
A000: BD 01 07        LDA     $0701,X             
A003: 29 07           AND     #$07                
A005: F0 35           BEQ     $A03C               ; {}
A007: C9 01           CMP     #$01                
A009: D0 2E           BNE     $A039               ; {}
A00B: 20 90 D9        JSR     $D990               
A00E: 90 1B           BCC     $A02B               ; {}
A010: 20 E7 D9        JSR     $D9E7               
A013: 90 1B           BCC     $A030               ; {}
A015: 20 09 DA        JSR     $DA09               
A018: 20 62 DF        JSR     $DF62               
A01B: 20 8A A0        JSR     $A08A               ; {}
A01E: 20 DA DB        JSR     $DBDA               
A021: 20 C9 DB        JSR     $DBC9               
A024: 20 B2 A0        JSR     $A0B2               ; {}
A027: 20 DE DC        JSR     $DCDE               
A02A: 60              RTS                         
A02B: A9 F8           LDA     #$F8                
A02D: 99 00 07        STA     $0700,Y             
A030: 20 D0 9D        JSR     $9DD0               ; {}
A033: 20 A9 DC        JSR     $DCA9               
A036: 4C 42 A6        JMP     $A642               ; {}
A039: 4C 65 DD        JMP     $DD65               
A03C: 8A              TXA                         
A03D: 38              SEC                         
A03E: E9 60           SBC     #$60                
A040: 0A              ASL     A                   
A041: C5 14           CMP     $14                 
A043: D0 06           BNE     $A04B               ; {}
A045: 20 BC 9F        JSR     $9FBC               ; {}
A048: FE 01 07        INC     $0701,X             
A04B: 60              RTS                         
A04C: 20 87 D2        JSR     $D287               
A04F: D0 00           BNE     $A051               ; {}
A051: BD 06 07        LDA     $0706,X             
A054: C9 78           CMP     #$78                
A056: B0 03           BCS     $A05B               ; {}
A058: 18              CLC                         
A059: 69 01           ADC     #$01                
A05B: 9D 06 07        STA     $0706,X             
A05E: 29 F0           AND     #$F0                
A060: 9D 05 07        STA     $0705,X             
A063: 60              RTS                         
A064: A9 00           LDA     #$00                
A066: 9D 06 07        STA     $0706,X             
A069: 9D 04 07        STA     $0704,X             
A06C: 9D 05 07        STA     $0705,X             
A06F: 60              RTS                         
A070: BD 06 07        LDA     $0706,X             
A073: 18              CLC                         
A074: 69 01           ADC     #$01                
A076: 9D 06 07        STA     $0706,X             
A079: C9 F8           CMP     #$F8                
A07B: B0 06           BCS     $A083               ; {}
A07D: 29 F0           AND     #$F0                
A07F: 9D 05 07        STA     $0705,X             
A082: 60              RTS                         
A083: A9 01           LDA     #$01                
A085: 9D 06 07        STA     $0706,X             
A088: D0 DF           BNE     $A069               ; {}
A08A: BD 06 07        LDA     $0706,X             
A08D: 30 E1           BMI     $A070               ; {}
A08F: D0 BB           BNE     $A04C               ; {}
A091: 8A              TXA                         
A092: 38              SEC                         
A093: E9 60           SBC     #$60                
A095: 18              CLC                         
A096: 65 14           ADC     $14                 
A098: 29 3F           AND     #$3F                
A09A: D0 15           BNE     $A0B1               ; {}
A09C: A0 40           LDY     #$40                
A09E: AD 23 07        LDA     $0723               
A0A1: DD 03 07        CMP     $0703,X             
A0A4: B0 02           BCS     $A0A8               ; {}
A0A6: A0 B0           LDY     #$B0                
A0A8: 98              TYA                         
A0A9: 9D 04 07        STA     $0704,X             
A0AC: A9 80           LDA     #$80                
A0AE: 9D 06 07        STA     $0706,X             
A0B1: 60              RTS                         
A0B2: A9 04           LDA     #$04                
A0B4: 4C 67 C6        JMP     $C667               
A0B7: A9 0D           LDA     #$0D                
A0B9: 9D 02 07        STA     $0702,X             
A0BC: A9 FF           LDA     #$FF                
A0BE: 9D 04 07        STA     $0704,X             
A0C1: A9 00           LDA     #$00                
A0C3: 9D 05 07        STA     $0705,X             
A0C6: 9D 06 07        STA     $0706,X             
A0C9: 4C D6 9D        JMP     $9DD6               ; {}
A0CC: A5 14           LDA     $14                 
A0CE: 0A              ASL     A                   
A0CF: 0A              ASL     A                   
A0D0: 0A              ASL     A                   
A0D1: 0A              ASL     A                   
A0D2: 9D 00 07        STA     $0700,X             
A0D5: A9 F0           LDA     #$F0                
A0D7: 9D 03 07        STA     $0703,X             
A0DA: 60              RTS                         
A0DB: A2 60           LDX     #$60                
A0DD: 20 EC A0        JSR     $A0EC               ; {}
A0E0: A2 70           LDX     #$70                
A0E2: 20 EC A0        JSR     $A0EC               ; {}
A0E5: A2 80           LDX     #$80                
A0E7: 20 EC A0        JSR     $A0EC               ; {}
A0EA: A2 90           LDX     #$90                
A0EC: BD 01 07        LDA     $0701,X             
A0EF: 29 F8           AND     #$F8                
A0F1: C9 38           CMP     #$38                
A0F3: D0 37           BNE     $A12C               ; {}
A0F5: 20 17 9F        JSR     $9F17               ; {}
A0F8: 20 08 DD        JSR     $DD08               
A0FB: BD 01 07        LDA     $0701,X             
A0FE: 29 07           AND     #$07                
A100: F0 34           BEQ     $A136               ; {}
A102: C9 01           CMP     #$01                
A104: D0 2D           BNE     $A133               ; {}
A106: 20 87 E0        JSR     $E087               
A109: 20 90 D9        JSR     $D990               
A10C: 90 1F           BCC     $A12D               ; {}
A10E: 20 E7 D9        JSR     $D9E7               
A111: 90 1F           BCC     $A132               ; {}
A113: A0 20           LDY     #$20                
A115: 20 86 D9        JSR     $D986               
A118: B0 03           BCS     $A11D               ; {}
A11A: 20 6B A1        JSR     $A16B               ; {}
A11D: 20 3D A4        JSR     $A43D               ; {}
A120: 20 DA DB        JSR     $DBDA               
A123: 20 C9 DB        JSR     $DBC9               
A126: 20 10 A2        JSR     $A210               ; {}
A129: 20 DE DC        JSR     $DCDE               
A12C: 60              RTS                         
A12D: A9 F8           LDA     #$F8                
A12F: 99 00 07        STA     $0700,Y             
A132: 60              RTS                         
A133: 4C 65 DD        JMP     $DD65               
A136: 8A              TXA                         
A137: 38              SEC                         
A138: E9 60           SBC     #$60                
A13A: 0A              ASL     A                   
A13B: 29 60           AND     #$60                
A13D: 85 00           STA     $00                 ; {ram.GP_00}
A13F: A5 FE           LDA     $FE                 
A141: 29 60           AND     #$60                
A143: C5 00           CMP     $00                 ; {ram.GP_00}
A145: D0 E5           BNE     $A12C               ; {}
A147: 20 CC A0        JSR     $A0CC               ; {}
A14A: 20 87 E0        JSR     $E087               
A14D: AD D3 04        LDA     $04D3               
A150: C9 40           CMP     #$40                
A152: 90 D8           BCC     $A12C               ; {}
A154: AD D5 04        LDA     $04D5               
A157: C9 40           CMP     #$40                
A159: B0 D1           BCS     $A12C               ; {}
A15B: 20 B7 A0        JSR     $A0B7               ; {}
A15E: BD 00 07        LDA     $0700,X             
A161: 38              SEC                         
A162: E9 08           SBC     #$08                
A164: 9D 00 07        STA     $0700,X             
A167: FE 01 07        INC     $0701,X             
A16A: 60              RTS                         
A16B: BD 08 07        LDA     $0708,X             
A16E: D0 1E           BNE     $A18E               ; {}
A170: A9 7F           LDA     #$7F                
A172: 9D 08 07        STA     $0708,X             
A175: A9 20           LDA     #$20                
A177: 8D 81 03        STA     $0381               
A17A: A0 02           LDY     #$02                
A17C: B9 41 01        LDA     $0141,Y             
A17F: 85 00           STA     $00                 ; {ram.GP_00}
A181: 29 F0           AND     #$F0                
A183: D0 06           BNE     $A18B               ; {}
A185: A5 00           LDA     $00                 ; {ram.GP_00}
A187: 29 0F           AND     #$0F                
A189: D0 04           BNE     $A18F               ; {}
A18B: 88              DEY                         
A18C: 10 EE           BPL     $A17C               ; {}
A18E: 60              RTS                         
A18F: A8              TAY                         
A190: 88              DEY                         
A191: B9 3E 01        LDA     $013E,Y             
A194: 29 0F           AND     #$0F                
A196: 09 80           ORA     #$80                
A198: 99 3E 01        STA     $013E,Y             
A19B: 60              RTS                         
A19C: A9 50           LDA     #$50                
A19E: 9D 02 07        STA     $0702,X             
A1A1: 60              RTS                         
A1A2: 20 87 D2        JSR     $D287               
A1A5: D0 F5           BNE     $A19C               ; {}
A1A7: AD D3 04        LDA     $04D3               
A1AA: C9 40           CMP     #$40                
A1AC: B0 07           BCS     $A1B5               ; {}
A1AE: AD D4 04        LDA     $04D4               
A1B1: C9 40           CMP     #$40                
A1B3: 90 E7           BCC     $A19C               ; {}
A1B5: A9 00           LDA     #$00                
A1B7: 9D 05 07        STA     $0705,X             
A1BA: BD 02 07        LDA     $0702,X             
A1BD: 29 0F           AND     #$0F                
A1BF: C9 08           CMP     #$08                
A1C1: B0 1B           BCS     $A1DE               ; {}
A1C3: BD 03 07        LDA     $0703,X             
A1C6: C9 F0           CMP     #$F0                
A1C8: B0 29           BCS     $A1F3               ; {}
A1CA: AD D3 04        LDA     $04D3               
A1CD: C9 40           CMP     #$40                
A1CF: 90 22           BCC     $A1F3               ; {}
A1D1: AD D5 04        LDA     $04D5               
A1D4: C9 40           CMP     #$40                
A1D6: B0 1B           BCS     $A1F3               ; {}
A1D8: A9 02           LDA     #$02                
A1DA: 9D 02 07        STA     $0702,X             
A1DD: 60              RTS                         
A1DE: BD 03 07        LDA     $0703,X             
A1E1: C9 08           CMP     #$08                
A1E3: 90 F3           BCC     $A1D8               ; {}
A1E5: AD D4 04        LDA     $04D4               
A1E8: C9 40           CMP     #$40                
A1EA: 90 EC           BCC     $A1D8               ; {}
A1EC: AD D6 04        LDA     $04D6               
A1EF: C9 40           CMP     #$40                
A1F1: B0 E5           BCS     $A1D8               ; {}
A1F3: A9 0D           LDA     #$0D                
A1F5: 9D 02 07        STA     $0702,X             
A1F8: 60              RTS                         
A1F9: BD 02 07        LDA     $0702,X             
A1FC: 48              PHA                         
A1FD: 29 F0           AND     #$F0                
A1FF: 9D 05 07        STA     $0705,X             
A202: 68              PLA                         
A203: 0A              ASL     A                   
A204: 0A              ASL     A                   
A205: 0A              ASL     A                   
A206: 0A              ASL     A                   
A207: 9D 04 07        STA     $0704,X             
A20A: 20 DA DB        JSR     $DBDA               
A20D: 4C C9 DB        JMP     $DBC9               
A210: A0 64           LDY     #$64                
A212: BD 04 07        LDA     $0704,X             
A215: 30 01           BMI     $A218               ; {}
A217: C8              INY                         
A218: A5 14           LDA     $14                 
A21A: 29 10           AND     #$10                
A21C: D0 02           BNE     $A220               ; {}
A21E: C8              INY                         
A21F: C8              INY                         
A220: 98              TYA                         
A221: 4C CD C4        JMP     $C4CD               
A224: A2 F0           LDX     #$F0                
A226: A9 00           LDA     #$00                
A228: 9D 01 07        STA     $0701,X             
A22B: 60              RTS                         
A22C: A2 C0           LDX     #$C0                
A22E: 20 33 A2        JSR     $A233               ; {}
A231: A2 D0           LDX     #$D0                
A233: BD 01 07        LDA     $0701,X             
A236: 29 F8           AND     #$F8                
A238: C9 18           CMP     #$18                
A23A: D0 EF           BNE     $A22B               ; {}
A23C: 20 17 9F        JSR     $9F17               ; {}
A23F: BD 01 07        LDA     $0701,X             
A242: 29 07           AND     #$07                
A244: F0 07           BEQ     $A24D               ; {}
A246: C9 01           CMP     #$01                
A248: F0 55           BEQ     $A29F               ; {}
A24A: 4C 65 DD        JMP     $DD65               
A24D: 8A              TXA                         
A24E: 38              SEC                         
A24F: E9 C0           SBC     #$C0                
A251: 85 01           STA     $01                 
A253: 0A              ASL     A                   
A254: 18              CLC                         
A255: 65 14           ADC     $14                 
A257: D0 42           BNE     $A29B               ; {}
A259: A9 E0           LDA     #$E0                
A25B: 24 26           BIT     $26                 
A25D: 30 02           BMI     $A261               ; {}
A25F: A9 20           LDA     #$20                
A261: 85 00           STA     $00                 ; {ram.GP_00}
A263: A5 01           LDA     $01                 
A265: 18              CLC                         
A266: 65 00           ADC     $00                 ; {ram.GP_00}
A268: 85 00           STA     $00                 ; {ram.GP_00}
A26A: AD 20 07        LDA     $0720               
A26D: 9D 00 07        STA     $0700,X             
A270: AD 23 07        LDA     $0723               
A273: 18              CLC                         
A274: 65 00           ADC     $00                 ; {ram.GP_00}
A276: 9D 03 07        STA     $0703,X             
A279: A5 1E           LDA     $1E                 
A27B: 29 C0           AND     #$C0                
A27D: D0 1C           BNE     $A29B               ; {}
A27F: 20 87 E0        JSR     $E087               
A282: AD D3 04        LDA     $04D3               
A285: C9 40           CMP     #$40                
A287: 90 12           BCC     $A29B               ; {}
A289: AD D4 04        LDA     $04D4               
A28C: C9 40           CMP     #$40                
A28E: 90 0B           BCC     $A29B               ; {}
A290: FE 01 07        INC     $0701,X             
A293: A9 00           LDA     #$00                
A295: 9D 06 07        STA     $0706,X             
A298: 20 D6 9D        JSR     $9DD6               ; {}
A29B: 60              RTS                         
A29C: 4C 1D DD        JMP     $DD1D               
A29F: 20 08 DD        JSR     $DD08               
A2A2: BD 06 07        LDA     $0706,X             
A2A5: C9 80           CMP     #$80                
A2A7: 90 14           BCC     $A2BD               ; {}
A2A9: C9 C0           CMP     #$C0                
A2AB: B0 10           BCS     $A2BD               ; {}
A2AD: 20 90 D9        JSR     $D990               
A2B0: 90 14           BCC     $A2C6               ; {}
A2B2: 20 E7 D9        JSR     $D9E7               
A2B5: 90 12           BCC     $A2C9               ; {}
A2B7: 20 09 DA        JSR     $DA09               
A2BA: 20 62 DF        JSR     $DF62               
A2BD: FE 06 07        INC     $0706,X             
A2C0: 20 CC A2        JSR     $A2CC               ; {}
A2C3: 4C DE DC        JMP     $DCDE               
A2C6: 4C 14 A4        JMP     $A414               ; {}
A2C9: 4C 19 A4        JMP     $A419               ; {}
A2CC: BD 06 07        LDA     $0706,X             
A2CF: C9 FF           CMP     #$FF                
A2D1: F0 C9           BEQ     $A29C               ; {}
A2D3: C9 40           CMP     #$40                
A2D5: 90 15           BCC     $A2EC               ; {}
A2D7: C9 80           CMP     #$80                
A2D9: 90 04           BCC     $A2DF               ; {}
A2DB: C9 C0           CMP     #$C0                
A2DD: 90 11           BCC     $A2F0               ; {}
A2DF: A0 0A           LDY     #$0A                
A2E1: A5 14           LDA     $14                 
A2E3: 29 08           AND     #$08                
A2E5: D0 01           BNE     $A2E8               ; {}
A2E7: C8              INY                         
A2E8: 98              TYA                         
A2E9: 4C 67 C6        JMP     $C667               
A2EC: A9 0A           LDA     #$0A                
A2EE: D0 F9           BNE     $A2E9               ; {}
A2F0: 20 F7 A2        JSR     $A2F7               ; {}
A2F3: A0 0C           LDY     #$0C                
A2F5: D0 EA           BNE     $A2E1               ; {}
A2F7: A0 F0           LDY     #$F0                
A2F9: B9 01 07        LDA     $0701,Y             
A2FC: 29 F8           AND     #$F8                
A2FE: C9 70           CMP     #$70                
A300: F0 1E           BEQ     $A320               ; {}
A302: A9 70           LDA     #$70                
A304: 99 01 07        STA     $0701,Y             
A307: BD 00 07        LDA     $0700,X             
A30A: 38              SEC                         
A30B: E9 10           SBC     #$10                
A30D: 99 00 07        STA     $0700,Y             
A310: BD 03 07        LDA     $0703,X             
A313: 99 03 07        STA     $0703,Y             
A316: CD 23 07        CMP     $0723               
A319: B0 06           BCS     $A321               ; {}
A31B: A9 05           LDA     #$05                
A31D: 99 02 07        STA     $0702,Y             
A320: 60              RTS                         
A321: A9 0D           LDA     #$0D                
A323: 99 02 07        STA     $0702,Y             
A326: 60              RTS                         
A327: A2 F0           LDX     #$F0                
A329: BD 01 07        LDA     $0701,X             
A32C: 29 F8           AND     #$F8                
A32E: C9 70           CMP     #$70                
A330: D0 EE           BNE     $A320               ; {}
A332: BD 00 07        LDA     $0700,X             
A335: C9 F8           CMP     #$F8                
A337: B0 1D           BCS     $A356               ; {}
A339: BD 03 07        LDA     $0703,X             
A33C: C9 F8           CMP     #$F8                
A33E: B0 16           BCS     $A356               ; {}
A340: 20 35 E0        JSR     $E035               
A343: 20 17 9F        JSR     $9F17               ; {}
A346: AD D3 04        LDA     $04D3               
A349: C9 40           CMP     #$40                
A34B: B0 09           BCS     $A356               ; {}
A34D: 20 09 DA        JSR     $DA09               
A350: 20 64 A3        JSR     $A364               ; {}
A353: 4C 7B A3        JMP     $A37B               ; {}
A356: A9 00           LDA     #$00                
A358: 9D 01 07        STA     $0701,X             
A35B: A9 F8           LDA     #$F8                
A35D: 9D 00 02        STA     $0200,X             
A360: 9D 00 07        STA     $0700,X             
A363: 60              RTS                         
A364: BD 02 07        LDA     $0702,X             
A367: 29 0F           AND     #$0F                
A369: C9 08           CMP     #$08                
A36B: B0 07           BCS     $A374               ; {}
A36D: FE 03 07        INC     $0703,X             
A370: FE 03 07        INC     $0703,X             
A373: 60              RTS                         
A374: DE 03 07        DEC     $0703,X             
A377: DE 03 07        DEC     $0703,X             
A37A: 60              RTS                         
A37B: BD 00 07        LDA     $0700,X             
A37E: 9D 00 02        STA     $0200,X             
A381: BD 03 07        LDA     $0703,X             
A384: 9D 03 02        STA     $0203,X             
A387: BD 01 07        LDA     $0701,X             
A38A: 29 01           AND     #$01                
A38C: D0 0B           BNE     $A399               ; {}
A38E: A9 01           LDA     #$01                
A390: 9D 02 02        STA     $0202,X             
A393: A9 A9           LDA     #$A9                
A395: 9D 01 02        STA     $0201,X             
A398: 60              RTS                         
A399: A9 02           LDA     #$02                
A39B: 9D 02 02        STA     $0202,X             
A39E: A9 F5           LDA     #$F5                
A3A0: 9D 01 02        STA     $0201,X             
A3A3: 60              RTS                         
A3A4: A9 0D           LDA     #$0D                
A3A6: 9D 02 07        STA     $0702,X             
A3A9: A9 00           LDA     #$00                
A3AB: 9D 05 07        STA     $0705,X             
A3AE: A9 D0           LDA     #$D0                
A3B0: 9D 04 07        STA     $0704,X             
A3B3: 20 D6 9D        JSR     $9DD6               ; {}
A3B6: A9 9A           LDA     #$9A                
A3B8: 9D 00 07        STA     $0700,X             
A3BB: A9 F7           LDA     #$F7                
A3BD: 9D 03 07        STA     $0703,X             
A3C0: A9 80           LDA     #$80                
A3C2: 9D 06 07        STA     $0706,X             
A3C5: 60              RTS                         
A3C6: A2 60           LDX     #$60                
A3C8: 20 D7 A3        JSR     $A3D7               ; {}
A3CB: A2 70           LDX     #$70                
A3CD: 20 D7 A3        JSR     $A3D7               ; {}
A3D0: A2 80           LDX     #$80                
A3D2: 20 D7 A3        JSR     $A3D7               ; {}
A3D5: A2 90           LDX     #$90                
A3D7: BD 01 07        LDA     $0701,X             
A3DA: 29 F8           AND     #$F8                
A3DC: C9 28           CMP     #$28                
A3DE: D0 33           BNE     $A413               ; {}
A3E0: 20 53 E0        JSR     $E053               
A3E3: 20 17 9F        JSR     $9F17               ; {}
A3E6: 20 08 DD        JSR     $DD08               
A3E9: BD 01 07        LDA     $0701,X             
A3EC: 29 07           AND     #$07                
A3EE: F0 35           BEQ     $A425               ; {}
A3F0: C9 01           CMP     #$01                
A3F2: D0 2E           BNE     $A422               ; {}
A3F4: 20 90 D9        JSR     $D990               
A3F7: 90 1B           BCC     $A414               ; {}
A3F9: 20 E7 D9        JSR     $D9E7               
A3FC: 90 1B           BCC     $A419               ; {}
A3FE: 20 09 DA        JSR     $DA09               
A401: 20 62 DF        JSR     $DF62               
A404: 20 BE A4        JSR     $A4BE               ; {}
A407: 20 DA DB        JSR     $DBDA               
A40A: 20 C9 DB        JSR     $DBC9               
A40D: 20 E6 A4        JSR     $A4E6               ; {}
A410: 20 DE DC        JSR     $DCDE               
A413: 60              RTS                         
A414: A9 F8           LDA     #$F8                
A416: 99 00 07        STA     $0700,Y             
A419: 20 D0 9D        JSR     $9DD0               ; {}
A41C: 20 A9 DC        JSR     $DCA9               
A41F: 4C 42 A6        JMP     $A642               ; {}
A422: 4C 65 DD        JMP     $DD65               
A425: 8A              TXA                         
A426: 38              SEC                         
A427: E9 60           SBC     #$60                
A429: 29 30           AND     #$30                
A42B: 0A              ASL     A                   
A42C: 85 00           STA     $00                 ; {ram.GP_00}
A42E: A5 FE           LDA     $FE                 
A430: 29 60           AND     #$60                
A432: C5 00           CMP     $00                 ; {ram.GP_00}
A434: D0 06           BNE     $A43C               ; {}
A436: 20 A4 A3        JSR     $A3A4               ; {}
A439: FE 01 07        INC     $0701,X             
A43C: 60              RTS                         
A43D: BD 06 07        LDA     $0706,X             
A440: 30 5E           BMI     $A4A0               ; {}
A442: D0 20           BNE     $A464               ; {}
A444: 8A              TXA                         
A445: 38              SEC                         
A446: E9 60           SBC     #$60                
A448: 18              CLC                         
A449: 65 14           ADC     $14                 
A44B: 29 1F           AND     #$1F                
A44D: D0 14           BNE     $A463               ; {}
A44F: A5 26           LDA     $26                 
A451: 29 1F           AND     #$1F                
A453: 18              CLC                         
A454: 69 A0           ADC     #$A0                
A456: 9D 04 07        STA     $0704,X             
A459: A5 26           LDA     $26                 
A45B: 29 3F           AND     #$3F                
A45D: 18              CLC                         
A45E: 69 80           ADC     #$80                
A460: 9D 06 07        STA     $0706,X             
A463: 60              RTS                         
A464: 20 87 D2        JSR     $D287               
A467: D0 0E           BNE     $A477               ; {}
A469: AD D3 04        LDA     $04D3               
A46C: C9 40           CMP     #$40                
A46E: B0 1A           BCS     $A48A               ; {}
A470: AD D4 04        LDA     $04D4               
A473: C9 40           CMP     #$40                
A475: B0 13           BCS     $A48A               ; {}
A477: BD 06 07        LDA     $0706,X             
A47A: C9 78           CMP     #$78                
A47C: B0 03           BCS     $A481               ; {}
A47E: 18              CLC                         
A47F: 69 03           ADC     #$03                
A481: 9D 06 07        STA     $0706,X             
A484: 29 F0           AND     #$F0                
A486: 9D 05 07        STA     $0705,X             
A489: 60              RTS                         
A48A: A9 00           LDA     #$00                
A48C: 9D 06 07        STA     $0706,X             
A48F: 9D 05 07        STA     $0705,X             
A492: A0 00           LDY     #$00                
A494: BD 04 07        LDA     $0704,X             
A497: 10 02           BPL     $A49B               ; {}
A499: A0 FF           LDY     #$FF                
A49B: 98              TYA                         
A49C: 9D 04 07        STA     $0704,X             
A49F: 60              RTS                         
A4A0: BD 06 07        LDA     $0706,X             
A4A3: 18              CLC                         
A4A4: 69 03           ADC     #$03                
A4A6: 9D 06 07        STA     $0706,X             
A4A9: C9 F8           CMP     #$F8                
A4AB: B0 06           BCS     $A4B3               ; {}
A4AD: 29 F0           AND     #$F0                
A4AF: 9D 05 07        STA     $0705,X             
A4B2: 60              RTS                         
A4B3: A9 01           LDA     #$01                
A4B5: 9D 06 07        STA     $0706,X             
A4B8: A9 00           LDA     #$00                
A4BA: 9D 05 07        STA     $0705,X             
A4BD: 60              RTS                         
A4BE: BD 06 07        LDA     $0706,X             
A4C1: 30 DD           BMI     $A4A0               ; {}
A4C3: D0 9F           BNE     $A464               ; {}
A4C5: 8A              TXA                         
A4C6: 38              SEC                         
A4C7: E9 60           SBC     #$60                
A4C9: 18              CLC                         
A4CA: 65 14           ADC     $14                 
A4CC: 29 7F           AND     #$7F                
A4CE: D0 15           BNE     $A4E5               ; {}
A4D0: A0 40           LDY     #$40                
A4D2: AD 23 07        LDA     $0723               
A4D5: DD 03 07        CMP     $0703,X             
A4D8: B0 02           BCS     $A4DC               ; {}
A4DA: A0 B0           LDY     #$B0                
A4DC: 98              TYA                         
A4DD: 9D 04 07        STA     $0704,X             
A4E0: A9 80           LDA     #$80                
A4E2: 9D 06 07        STA     $0706,X             
A4E5: 60              RTS                         
A4E6: BD 06 07        LDA     $0706,X             
A4E9: D0 12           BNE     $A4FD               ; {}
A4EB: A5 14           LDA     $14                 
A4ED: 29 08           AND     #$08                
A4EF: D0 0C           BNE     $A4FD               ; {}
A4F1: A0 50           LDY     #$50                
A4F3: BD 04 07        LDA     $0704,X             
A4F6: 30 01           BMI     $A4F9               ; {}
A4F8: C8              INY                         
A4F9: 98              TYA                         
A4FA: 4C CD C4        JMP     $C4CD               
A4FD: A0 52           LDY     #$52                
A4FF: D0 F2           BNE     $A4F3               ; {}
A501: A2 60           LDX     #$60                
A503: 20 16 A5        JSR     $A516               ; {}
A506: A2 70           LDX     #$70                
A508: 20 16 A5        JSR     $A516               ; {}
A50B: A2 80           LDX     #$80                
A50D: 20 16 A5        JSR     $A516               ; {}
A510: A2 90           LDX     #$90                
A512: 20 16 A5        JSR     $A516               ; {}
A515: 60              RTS                         
A516: BD 01 07        LDA     $0701,X             
A519: 29 F8           AND     #$F8                
A51B: C9 20           CMP     #$20                
A51D: D0 F6           BNE     $A515               ; {}
A51F: 20 17 9F        JSR     $9F17               ; {}
A522: 20 08 DD        JSR     $DD08               
A525: BD 01 07        LDA     $0701,X             
A528: 29 07           AND     #$07                
A52A: F0 07           BEQ     $A533               ; {}
A52C: C9 01           CMP     #$01                
A52E: F0 36           BEQ     $A566               ; {}
A530: 4C 65 DD        JMP     $DD65               
A533: 8A              TXA                         
A534: 38              SEC                         
A535: E9 60           SBC     #$60                
A537: 29 30           AND     #$30                
A539: 85 00           STA     $00                 ; {ram.GP_00}
A53B: 18              CLC                         
A53C: 65 14           ADC     $14                 
A53E: 29 7F           AND     #$7F                
A540: D0 23           BNE     $A565               ; {}
A542: A5 00           LDA     $00                 ; {ram.GP_00}
A544: 0A              ASL     A                   
A545: 18              CLC                         
A546: 85 00           STA     $00                 ; {ram.GP_00}
A548: A5 26           LDA     $26                 
A54A: 29 7F           AND     #$7F                
A54C: 65 00           ADC     $00                 ; {ram.GP_00}
A54E: 9D 03 07        STA     $0703,X             
A551: A9 00           LDA     #$00                
A553: 9D 00 07        STA     $0700,X             
A556: 9D 02 07        STA     $0702,X             
A559: 9D 04 07        STA     $0704,X             
A55C: 9D 05 07        STA     $0705,X             
A55F: 20 D6 9D        JSR     $9DD6               ; {}
A562: FE 01 07        INC     $0701,X             
A565: 60              RTS                         
A566: 20 08 DD        JSR     $DD08               
A569: 20 90 D9        JSR     $D990               
A56C: 90 17           BCC     $A585               ; {}
A56E: 20 E7 D9        JSR     $D9E7               
A571: 90 15           BCC     $A588               ; {}
A573: 20 09 DA        JSR     $DA09               
A576: 20 62 DF        JSR     $DF62               
A579: 20 8B A5        JSR     $A58B               ; {}
A57C: 20 C0 DB        JSR     $DBC0               
A57F: 20 91 A5        JSR     $A591               ; {}
A582: 4C DE DC        JMP     $DCDE               
A585: 4C 14 A4        JMP     $A414               ; {}
A588: 4C 19 A4        JMP     $A419               ; {}
A58B: A9 60           LDA     #$60                
A58D: 9D 02 07        STA     $0702,X             
A590: 60              RTS                         
A591: A9 63           LDA     #$63                
A593: 4C CD C4        JMP     $C4CD               
A596: 60              RTS                         
A597: AD C1 07        LDA     $07C1               
A59A: 0D C9 07        ORA     $07C9               
A59D: 0D D1 07        ORA     $07D1               
A5A0: 0D D9 07        ORA     $07D9               
A5A3: F0 0A           BEQ     $A5AF               ; {}
A5A5: 20 E7 A5        JSR     $A5E7               ; {}
A5A8: 20 F1 A6        JSR     $A6F1               ; {}
A5AB: 20 2C A2        JSR     $A22C               ; {}
A5AE: 60              RTS                         
A5AF: AD 30 01        LDA     $0130               
A5B2: 0A              ASL     A                   
A5B3: A8              TAY                         
A5B4: B9 F9 BC        LDA     $BCF9,Y             ; {}
A5B7: 85 00           STA     $00                 ; {ram.GP_00}
A5B9: B9 FA BC        LDA     $BCFA,Y             ; {}
A5BC: 85 01           STA     $01                 
A5BE: AC D1 04        LDY     $04D1               
A5C1: B1 00           LDA     ($00),Y             ; {ram.GP_00}
A5C3: 0A              ASL     A                   
A5C4: 0A              ASL     A                   
A5C5: 0A              ASL     A                   
A5C6: 20 99 DC        JSR     $DC99               
A5C9: 8D C1 07        STA     $07C1               
A5CC: 8D C9 07        STA     $07C9               
A5CF: 8D D1 07        STA     $07D1               
A5D2: 8D D9 07        STA     $07D9               
A5D5: 60              RTS                         
A5D6: A9 0D           LDA     #$0D                
A5D8: 9D 02 07        STA     $0702,X             
A5DB: A9 00           LDA     #$00                
A5DD: 9D 04 07        STA     $0704,X             
A5E0: 9D 05 07        STA     $0705,X             
A5E3: 4C EF 9D        JMP     $9DEF               ; {}
A5E6: 60              RTS                         
A5E7: A2 C0           LDX     #$C0                
A5E9: 20 F8 A5        JSR     $A5F8               ; {}
A5EC: A2 C8           LDX     #$C8                
A5EE: 20 F8 A5        JSR     $A5F8               ; {}
A5F1: A2 D0           LDX     #$D0                
A5F3: 20 F8 A5        JSR     $A5F8               ; {}
A5F6: A2 D8           LDX     #$D8                
A5F8: BD 01 07        LDA     $0701,X             
A5FB: 29 F8           AND     #$F8                
A5FD: C9 10           CMP     #$10                
A5FF: D0 3B           BNE     $A63C               ; {}
A601: 20 17 9F        JSR     $9F17               ; {}
A604: BD 01 07        LDA     $0701,X             
A607: 29 07           AND     #$07                
A609: F0 50           BEQ     $A65B               ; {}
A60B: C9 01           CMP     #$01                
A60D: F0 03           BEQ     $A612               ; {}
A60F: 4C B2 DE        JMP     $DEB2               
A612: 20 53 E0        JSR     $E053               
A615: BD 00 07        LDA     $0700,X             
A618: C9 F8           CMP     #$F8                
A61A: B0 3C           BCS     $A658               ; {}
A61C: BD 03 07        LDA     $0703,X             
A61F: C9 FC           CMP     #$FC                
A621: B0 35           BCS     $A658               ; {}
A623: 20 90 D9        JSR     $D990               
A626: 90 15           BCC     $A63D               ; {}
A628: 20 E7 D9        JSR     $D9E7               
A62B: 90 15           BCC     $A642               ; {}
A62D: 20 09 DA        JSR     $DA09               
A630: 20 65 DF        JSR     $DF65               
A633: 20 A3 A6        JSR     $A6A3               ; {}
A636: 20 C0 DB        JSR     $DBC0               
A639: 20 D5 C7        JSR     $C7D5               
A63C: 60              RTS                         
A63D: A9 F8           LDA     #$F8                
A63F: 99 00 07        STA     $0700,Y             
A642: FE 01 07        INC     $0701,X             
A645: A9 FF           LDA     #$FF                
A647: 9D 02 07        STA     $0702,X             
A64A: A9 08           LDA     #$08                
A64C: 8D 81 03        STA     $0381               
A64F: 20 03 9E        JSR     $9E03               ; {}
A652: 20 E1 E2        JSR     $E2E1               
A655: 4C F0 E2        JMP     $E2F0               
A658: 4C 2F DF        JMP     $DF2F               
A65B: 8A              TXA                         
A65C: 38              SEC                         
A65D: E9 C0           SBC     #$C0                
A65F: 0A              ASL     A                   
A660: 0A              ASL     A                   
A661: 0A              ASL     A                   
A662: 18              CLC                         
A663: 65 14           ADC     $14                 
A665: 85 00           STA     $00                 ; {ram.GP_00}
A667: 29 F0           AND     #$F0                
A669: 9D 00 07        STA     $0700,X             
A66C: A5 00           LDA     $00                 ; {ram.GP_00}
A66E: 0A              ASL     A                   
A66F: 0A              ASL     A                   
A670: 0A              ASL     A                   
A671: 0A              ASL     A                   
A672: 9D 03 07        STA     $0703,X             
A675: 20 53 E0        JSR     $E053               
A678: AD D3 04        LDA     $04D3               
A67B: C9 6F           CMP     #$6F                
A67D: D0 0F           BNE     $A68E               ; {}
A67F: 20 D6 A5        JSR     $A5D6               ; {}
A682: BD 03 07        LDA     $0703,X             
A685: 18              CLC                         
A686: 69 04           ADC     #$04                
A688: 9D 03 07        STA     $0703,X             
A68B: FE 01 07        INC     $0701,X             
A68E: 60              RTS                         
A68F: AD 23 07        LDA     $0723               
A692: DD 03 07        CMP     $0703,X             
A695: 90 06           BCC     $A69D               ; {}
A697: A9 60           LDA     #$60                
A699: 9D 02 07        STA     $0702,X             
A69C: 60              RTS                         
A69D: A9 6F           LDA     #$6F                
A69F: 9D 02 07        STA     $0702,X             
A6A2: 60              RTS                         
A6A3: 20 87 D2        JSR     $D287               
A6A6: D0 E7           BNE     $A68F               ; {}
A6A8: AD D3 04        LDA     $04D3               
A6AB: C9 40           CMP     #$40                
A6AD: 90 E0           BCC     $A68F               ; {}
A6AF: A9 00           LDA     #$00                
A6B1: 9D 05 07        STA     $0705,X             
A6B4: BD 02 07        LDA     $0702,X             
A6B7: 29 0F           AND     #$0F                
A6B9: C9 08           CMP     #$08                
A6BB: B0 0D           BCS     $A6CA               ; {}
A6BD: AD D5 04        LDA     $04D5               
A6C0: C9 40           CMP     #$40                
A6C2: B0 0D           BCS     $A6D1               ; {}
A6C4: A9 03           LDA     #$03                
A6C6: 9D 02 07        STA     $0702,X             
A6C9: 60              RTS                         
A6CA: AD D6 04        LDA     $04D6               
A6CD: C9 40           CMP     #$40                
A6CF: B0 F3           BCS     $A6C4               ; {}
A6D1: A9 0C           LDA     #$0C                
A6D3: 9D 02 07        STA     $0702,X             
A6D6: 60              RTS                         
A6D7: A9 0D           LDA     #$0D                
A6D9: 9D 02 07        STA     $0702,X             
A6DC: 4C D6 9D        JMP     $9DD6               ; {}
A6DF: A5 14           LDA     $14                 
A6E1: 0A              ASL     A                   
A6E2: 0A              ASL     A                   
A6E3: 0A              ASL     A                   
A6E4: 0A              ASL     A                   
A6E5: 38              SEC                         
A6E6: E9 08           SBC     #$08                
A6E8: 9D 00 07        STA     $0700,X             
A6EB: A9 F7           LDA     #$F7                
A6ED: 9D 03 07        STA     $0703,X             
A6F0: 60              RTS                         
A6F1: A2 C0           LDX     #$C0                
A6F3: BD 01 07        LDA     $0701,X             
A6F6: 29 F8           AND     #$F8                
A6F8: C9 48           CMP     #$48                
A6FA: D0 44           BNE     $A740               ; {}
A6FC: 20 17 9F        JSR     $9F17               ; {}
A6FF: BD 01 07        LDA     $0701,X             
A702: 29 07           AND     #$07                
A704: 20 2B EE        JSR     $EE2B               
A707: 8A              TXA                         
A708: A7 ; ????
A709: 0D A7 76        ORA     $76A7               
A70C: A7 ; ????
A70D: 20 53 E0        JSR     $E053               
A710: 20 A7 AA        JSR     $AAA7               ; {}
A713: BD 00 07        LDA     $0700,X             
A716: 48              PHA                         
A717: 38              SEC                         
A718: E9 08           SBC     #$08                
A71A: 9D 00 07        STA     $0700,X             
A71D: 20 BC D9        JSR     $D9BC               
A720: 90 1F           BCC     $A741               ; {}
A722: 20 E7 D9        JSR     $D9E7               
A725: 90 1F           BCC     $A746               ; {}
A727: 68              PLA                         
A728: 9D 00 07        STA     $0700,X             
A72B: 20 09 DA        JSR     $DA09               
A72E: 20 65 DF        JSR     $DF65               
A731: 20 C4 A7        JSR     $A7C4               ; {}
A734: 20 C0 DB        JSR     $DBC0               
A737: 20 12 A8        JSR     $A812               ; {}
A73A: 20 85 A7        JSR     $A785               ; {}
A73D: 20 5C A8        JSR     $A85C               ; {}
A740: 60              RTS                         
A741: A9 F8           LDA     #$F8                
A743: 99 00 07        STA     $0700,Y             
A746: 68              PLA                         
A747: 9D 00 07        STA     $0700,X             
A74A: 8A              TXA                         
A74B: 48              PHA                         
A74C: 18              CLC                         
A74D: 69 10           ADC     #$10                
A74F: AA              TAX                         
A750: 20 89 DD        JSR     $DD89               
A753: 68              PLA                         
A754: AA              TAX                         
A755: 20 D0 9D        JSR     $9DD0               ; {}
A758: 20 A9 DC        JSR     $DCA9               
A75B: 4C 42 A6        JMP     $A642               ; {}
A75E: 4C B8 AA        JMP     $AAB8               ; {}
A761: BD 00 07        LDA     $0700,X             
A764: C9 F8           CMP     #$F8                
A766: B0 08           BCS     $A770               ; {}
A768: BD 03 07        LDA     $0703,X             
A76B: C9 F8           CMP     #$F8                
A76D: B0 01           BCS     $A770               ; {}
A76F: 60              RTS                         
A770: 20 2F DF        JSR     $DF2F               
A773: 68              PLA                         
A774: 68              PLA                         
A775: 60              RTS                         
A776: 20 65 DD        JSR     $DD65               
A779: 8A              TXA                         
A77A: 48              PHA                         
A77B: 18              CLC                         
A77C: 69 10           ADC     #$10                
A77E: AA              TAX                         
A77F: 20 89 DD        JSR     $DD89               
A782: 68              PLA                         
A783: AA              TAX                         
A784: 60              RTS                         
A785: A9 1C           LDA     #$1C                
A787: 4C E0 DC        JMP     $DCE0               
A78A: 20 DF A6        JSR     $A6DF               ; {}
A78D: 20 53 E0        JSR     $E053               
A790: AD D5 04        LDA     $04D5               
A793: C9 40           CMP     #$40                
A795: B0 0D           BCS     $A7A4               ; {}
A797: AD D3 04        LDA     $04D3               
A79A: C9 40           CMP     #$40                
A79C: 90 06           BCC     $A7A4               ; {}
A79E: 20 D7 A6        JSR     $A6D7               ; {}
A7A1: FE 01 07        INC     $0701,X             
A7A4: 60              RTS                         
A7A5: BD 02 07        LDA     $0702,X             
A7A8: 29 F0           AND     #$F0                
A7AA: 48              PHA                         
A7AB: BD 03 07        LDA     $0703,X             
A7AE: D9 03 07        CMP     $0703,Y             
A7B1: 68              PLA                         
A7B2: 90 06           BCC     $A7BA               ; {}
A7B4: 09 0D           ORA     #$0D                
A7B6: 9D 02 07        STA     $0702,X             
A7B9: 60              RTS                         
A7BA: 09 02           ORA     #$02                
A7BC: D0 F8           BNE     $A7B6               ; {}
A7BE: A9 50           LDA     #$50                
A7C0: 9D 02 07        STA     $0702,X             
A7C3: 60              RTS                         
A7C4: A0 20           LDY     #$20                
A7C6: 20 A5 A7        JSR     $A7A5               ; {}
A7C9: 20 87 D2        JSR     $D287               
A7CC: D0 F0           BNE     $A7BE               ; {}
A7CE: AD D3 04        LDA     $04D3               
A7D1: C9 40           CMP     #$40                
A7D3: B0 07           BCS     $A7DC               ; {}
A7D5: AD D4 04        LDA     $04D4               
A7D8: C9 40           CMP     #$40                
A7DA: 90 E2           BCC     $A7BE               ; {}
A7DC: A9 00           LDA     #$00                
A7DE: 9D 05 07        STA     $0705,X             
A7E1: BD 02 07        LDA     $0702,X             
A7E4: 29 0F           AND     #$0F                
A7E6: C9 08           CMP     #$08                
A7E8: B0 14           BCS     $A7FE               ; {}
A7EA: AD D3 04        LDA     $04D3               
A7ED: C9 40           CMP     #$40                
A7EF: 90 1B           BCC     $A80C               ; {}
A7F1: AD D5 04        LDA     $04D5               
A7F4: C9 40           CMP     #$40                
A7F6: B0 14           BCS     $A80C               ; {}
A7F8: A9 02           LDA     #$02                
A7FA: 9D 02 07        STA     $0702,X             
A7FD: 60              RTS                         
A7FE: AD D4 04        LDA     $04D4               
A801: C9 40           CMP     #$40                
A803: 90 F3           BCC     $A7F8               ; {}
A805: AD D6 04        LDA     $04D6               
A808: C9 40           CMP     #$40                
A80A: B0 EC           BCS     $A7F8               ; {}
A80C: A9 0D           LDA     #$0D                
A80E: 9D 02 07        STA     $0702,X             
A811: 60              RTS                         
A812: BD 00 07        LDA     $0700,X             
A815: 38              SEC                         
A816: E9 10           SBC     #$10                
A818: 9D 10 07        STA     $0710,X             
A81B: BD 03 07        LDA     $0703,X             
A81E: 9D 13 07        STA     $0713,X             
A821: A9 00           LDA     #$00                
A823: 9D 12 07        STA     $0712,X             
A826: A5 14           LDA     $14                 
A828: 29 30           AND     #$30                
A82A: 4A              LSR     A                   
A82B: 4A              LSR     A                   
A82C: 4A              LSR     A                   
A82D: 4A              LSR     A                   
A82E: A8              TAY                         
A82F: 4A              LSR     A                   
A830: 90 03           BCC     $A835               ; {}
A832: FE 10 07        INC     $0710,X             
A835: B9 58 A8        LDA     $A858,Y             ; {}
A838: A8              TAY                         
A839: BD 04 07        LDA     $0704,X             
A83C: 30 01           BMI     $A83F               ; {}
A83E: C8              INY                         
A83F: 98              TYA                         
A840: 20 CD C4        JSR     $C4CD               
A843: A0 42           LDY     #$42                
A845: BD 04 07        LDA     $0704,X             
A848: 30 01           BMI     $A84B               ; {}
A84A: C8              INY                         
A84B: 8A              TXA                         
A84C: 48              PHA                         
A84D: 18              CLC                         
A84E: 69 10           ADC     #$10                
A850: AA              TAX                         
A851: 98              TYA                         
A852: 20 CD C4        JSR     $C4CD               
A855: 68              PLA                         
A856: AA              TAX                         
A857: 60              RTS                         
A858: 44 ; ????
A859: 46 44           LSR     $44                 
A85B: 46 A0           LSR     $A0                 
A85D: F0 B9           BEQ     $A818               ; {}
A85F: 01 07           ORA     ($07,X)             
A861: 29 F8           AND     #$F8                
A863: C9 70           CMP     #$70                
A865: F0 26           BEQ     $A88D               ; {}
A867: 8A              TXA                         
A868: 18              CLC                         
A869: 65 14           ADC     $14                 
A86B: 29 7F           AND     #$7F                
A86D: D0 1E           BNE     $A88D               ; {}
A86F: A9 71           LDA     #$71                
A871: 99 01 07        STA     $0701,Y             
A874: BD 00 07        LDA     $0700,X             
A877: 38              SEC                         
A878: E9 0E           SBC     #$0E                
A87A: 99 00 07        STA     $0700,Y             
A87D: BD 03 07        LDA     $0703,X             
A880: 99 03 07        STA     $0703,Y             
A883: CD 23 07        CMP     $0723               
A886: B0 06           BCS     $A88E               ; {}
A888: A9 04           LDA     #$04                
A88A: 99 02 07        STA     $0702,Y             
A88D: 60              RTS                         
A88E: A9 0D           LDA     #$0D                
A890: 99 02 07        STA     $0702,Y             
A893: 60              RTS                         
A894: A5 00           LDA     $00                 ; {ram.GP_00}
A896: 85 02           STA     $02                 
A898: 38              SEC                         
A899: E9 F0           SBC     #$F0                
A89B: 85 00           STA     $00                 ; {ram.GP_00}
A89D: A5 01           LDA     $01                 
A89F: E9 05           SBC     #$05                
A8A1: 85 01           STA     $01                 
A8A3: B0 04           BCS     $A8A9               ; {}
A8A5: A5 02           LDA     $02                 
A8A7: 85 00           STA     $00                 ; {ram.GP_00}
A8A9: A9 08           LDA     #$08                
A8AB: 85 01           STA     $01                 
A8AD: A5 00           LDA     $00                 ; {ram.GP_00}
A8AF: 48              PHA                         
A8B0: 29 F0           AND     #$F0                
A8B2: 0A              ASL     A                   
A8B3: 26 01           ROL     $01                 
A8B5: 0A              ASL     A                   
A8B6: 26 01           ROL     $01                 
A8B8: 85 00           STA     $00                 ; {ram.GP_00}
A8BA: 68              PLA                         
A8BB: 29 0F           AND     #$0F                
A8BD: 0A              ASL     A                   
A8BE: 18              CLC                         
A8BF: 65 00           ADC     $00                 ; {ram.GP_00}
A8C1: 85 00           STA     $00                 ; {ram.GP_00}
A8C3: AD D1 04        LDA     $04D1               
A8C6: 4A              LSR     A                   
A8C7: 90 07           BCC     $A8D0               ; {}
A8C9: A5 01           LDA     $01                 
A8CB: 18              CLC                         
A8CC: 69 04           ADC     #$04                
A8CE: 85 01           STA     $01                 
A8D0: 60              RTS                         
A8D1: A0 E0           LDY     #$E0                
A8D3: B9 01 07        LDA     $0701,Y             
A8D6: D0 42           BNE     $A91A               ; {}
A8D8: AD D3 04        LDA     $04D3               
A8DB: C9 6E           CMP     #$6E                
A8DD: D0 3B           BNE     $A91A               ; {}
A8DF: AD D4 04        LDA     $04D4               
A8E2: C9 6E           CMP     #$6E                
A8E4: D0 34           BNE     $A91A               ; {}
A8E6: A5 1E           LDA     $1E                 
A8E8: 29 C0           AND     #$C0                
A8EA: D0 2E           BNE     $A91A               ; {}
A8EC: 98              TYA                         
A8ED: 48              PHA                         
A8EE: A0 00           LDY     #$00                
A8F0: A9 00           LDA     #$00                
A8F2: 91 12           STA     ($12),Y             
A8F4: C8              INY                         
A8F5: 91 12           STA     ($12),Y             
A8F7: 20 1B A9        JSR     $A91B               ; {}
A8FA: 68              PLA                         
A8FB: A8              TAY                         
A8FC: A9 80           LDA     #$80                
A8FE: 99 01 07        STA     $0701,Y             
A901: A9 04           LDA     #$04                
A903: 99 02 07        STA     $0702,Y             
A906: A9 00           LDA     #$00                
A908: 99 06 07        STA     $0706,Y             
A90B: BD 00 07        LDA     $0700,X             
A90E: 18              CLC                         
A90F: 69 0C           ADC     #$0C                
A911: 99 00 07        STA     $0700,Y             
A914: BD 03 07        LDA     $0703,X             
A917: 99 03 07        STA     $0703,Y             
A91A: 60              RTS                         
A91B: A5 12           LDA     $12                 
A91D: 85 00           STA     $00                 ; {ram.GP_00}
A91F: A5 13           LDA     $13                 
A921: 85 01           STA     $01                 
A923: 20 94 A8        JSR     $A894               ; {}
A926: A9 01           LDA     #$01                
A928: 85 68           STA     $68                 
A92A: A5 00           LDA     $00                 ; {ram.GP_00}
A92C: 38              SEC                         
A92D: E9 02           SBC     #$02                
A92F: 85 69           STA     $69                 
A931: A5 01           LDA     $01                 
A933: 85 6A           STA     $6A                 
A935: 60              RTS                         
A936: A2 60           LDX     #$60                
A938: A0 00           LDY     #$00                
A93A: 20 53 A9        JSR     $A953               ; {}
A93D: A2 70           LDX     #$70                
A93F: A0 20           LDY     #$20                
A941: 20 53 A9        JSR     $A953               ; {}
A944: A2 80           LDX     #$80                
A946: A0 40           LDY     #$40                
A948: 20 53 A9        JSR     $A953               ; {}
A94B: A2 90           LDX     #$90                
A94D: A0 60           LDY     #$60                
A94F: 20 53 A9        JSR     $A953               ; {}
A952: 60              RTS                         
A953: 20 60 A9        JSR     $A960               ; {}
A956: C8              INY                         
A957: C8              INY                         
A958: C8              INY                         
A959: C8              INY                         
A95A: 98              TYA                         
A95B: 29 1F           AND     #$1F                
A95D: D0 F4           BNE     $A953               ; {}
A95F: 60              RTS                         
A960: B9 B3 BD        LDA     $BDB3,Y             ; {}
A963: C9 FF           CMP     #$FF                
A965: F0 29           BEQ     $A990               ; {}
A967: CD 30 01        CMP     $0130               
A96A: D0 23           BNE     $A98F               ; {}
A96C: AD D1 04        LDA     $04D1               
A96F: D9 B4 BD        CMP     $BDB4,Y             ; {}
A972: D0 1B           BNE     $A98F               ; {}
A974: A5 FE           LDA     $FE                 
A976: D9 B5 BD        CMP     $BDB5,Y             ; {}
A979: D0 14           BNE     $A98F               ; {}
A97B: A9 78           LDA     #$78                
A97D: 9D 01 07        STA     $0701,X             
A980: A9 C0           LDA     #$C0                
A982: 9D 02 07        STA     $0702,X             
A985: A9 80           LDA     #$80                
A987: 9D 00 07        STA     $0700,X             
A98A: A9 F8           LDA     #$F8                
A98C: 9D 03 07        STA     $0703,X             
A98F: 60              RTS                         
A990: 68              PLA                         
A991: 68              PLA                         
A992: 60              RTS                         
A993: A2 60           LDX     #$60                
A995: 20 A4 A9        JSR     $A9A4               ; {}
A998: A2 70           LDX     #$70                
A99A: 20 A4 A9        JSR     $A9A4               ; {}
A99D: A2 80           LDX     #$80                
A99F: 20 A4 A9        JSR     $A9A4               ; {}
A9A2: A2 90           LDX     #$90                
A9A4: BD 01 07        LDA     $0701,X             
A9A7: 29 F8           AND     #$F8                
A9A9: C9 78           CMP     #$78                
A9AB: D0 1B           BNE     $A9C8               ; {}
A9AD: 20 49 E0        JSR     $E049               
A9B0: 20 17 9F        JSR     $9F17               ; {}
A9B3: BD 01 07        LDA     $0701,X             
A9B6: 29 07           AND     #$07                
A9B8: BD 03 07        LDA     $0703,X             
A9BB: C9 08           CMP     #$08                
A9BD: 90 0A           BCC     $A9C9               ; {}
A9BF: 20 CC A9        JSR     $A9CC               ; {}
A9C2: 20 C0 DB        JSR     $DBC0               
A9C5: 20 F4 A9        JSR     $A9F4               ; {}
A9C8: 60              RTS                         
A9C9: 4C 1D DD        JMP     $DD1D               
A9CC: A9 00           LDA     #$00                
A9CE: 9D 04 07        STA     $0704,X             
A9D1: BD 02 07        LDA     $0702,X             
A9D4: 29 F0           AND     #$F0                
A9D6: C9 80           CMP     #$80                
A9D8: B0 0D           BCS     $A9E7               ; {}
A9DA: BD 00 07        LDA     $0700,X             
A9DD: C9 C0           CMP     #$C0                
A9DF: B0 0D           BCS     $A9EE               ; {}
A9E1: A9 30           LDA     #$30                
A9E3: 9D 02 07        STA     $0702,X             
A9E6: 60              RTS                         
A9E7: BD 00 07        LDA     $0700,X             
A9EA: C9 40           CMP     #$40                
A9EC: 90 F3           BCC     $A9E1               ; {}
A9EE: A9 C0           LDA     #$C0                
A9F0: 9D 02 07        STA     $0702,X             
A9F3: 60              RTS                         
A9F4: A9 1B           LDA     #$1B                
A9F6: 4C 67 C6        JMP     $C667               
A9F9: A2 50           LDX     #$50                
A9FB: A9 80           LDA     #$80                
A9FD: 9D 01 07        STA     $0701,X             
AA00: 0A              ASL     A                   
AA01: 9D 03 07        STA     $0703,X             
AA04: 85 A1           STA     $A1                 
AA06: 60              RTS                         
AA07: A2 50           LDX     #$50                
AA09: BD 01 07        LDA     $0701,X             
AA0C: 10 F8           BPL     $AA06               ; {}
AA0E: 20 17 9F        JSR     $9F17               ; {}
AA11: BD 01 07        LDA     $0701,X             
AA14: 29 0F           AND     #$0F                
AA16: D0 52           BNE     $AA6A               ; {}
AA18: A5 A1           LDA     $A1                 
AA1A: CD 2A BC        CMP     $BC2A               ; {}
AA1D: 90 06           BCC     $AA25               ; {}
AA1F: A9 00           LDA     #$00                
AA21: 9D 01 07        STA     $0701,X             
AA24: 60              RTS                         
AA25: 85 00           STA     $00                 ; {ram.GP_00}
AA27: 0A              ASL     A                   
AA28: 0A              ASL     A                   
AA29: A8              TAY                         
AA2A: B9 2B BC        LDA     $BC2B,Y             ; {}
AA2D: CD 30 01        CMP     $0130               
AA30: 90 1B           BCC     $AA4D               ; {}
AA32: D0 D2           BNE     $AA06               ; {}
AA34: B9 2C BC        LDA     $BC2C,Y             ; {}
AA37: CD D1 04        CMP     $04D1               
AA3A: 90 11           BCC     $AA4D               ; {}
AA3C: D0 C8           BNE     $AA06               ; {}
AA3E: B9 2D BC        LDA     $BC2D,Y             ; {}
AA41: 29 0F           AND     #$0F                
AA43: 0A              ASL     A                   
AA44: 0A              ASL     A                   
AA45: 0A              ASL     A                   
AA46: 0A              ASL     A                   
AA47: C5 FE           CMP     $FE                 
AA49: F0 06           BEQ     $AA51               ; {}
AA4B: B0 B9           BCS     $AA06               ; {}
AA4D: E6 A1           INC     $A1                 
AA4F: D0 C7           BNE     $AA18               ; {}
AA51: A9 00           LDA     #$00                
AA53: 9D 03 07        STA     $0703,X             
AA56: B9 2D BC        LDA     $BC2D,Y             ; {}
AA59: 29 F0           AND     #$F0                
AA5B: 9D 00 07        STA     $0700,X             
AA5E: A9 81           LDA     #$81                
AA60: 9D 01 07        STA     $0701,X             
AA63: B9 2E BC        LDA     $BC2E,Y             ; {}
AA66: 9D 02 07        STA     $0702,X             
AA69: 60              RTS                         
AA6A: BD 03 07        LDA     $0703,X             
AA6D: C9 02           CMP     #$02                
AA6F: 90 11           BCC     $AA82               ; {}
AA71: 20 8A D9        JSR     $D98A               
AA74: 90 03           BCC     $AA79               ; {}
AA76: 4C 98 AA        JMP     $AA98               ; {}
AA79: BD 02 07        LDA     $0702,X             
AA7C: D0 11           BNE     $AA8F               ; {}
AA7E: A9 FF           LDA     #$FF                
AA80: 85 3E           STA     $3E                 
AA82: A9 10           LDA     #$10                
AA84: 8D 81 03        STA     $0381               
AA87: A9 80           LDA     #$80                
AA89: 9D 01 07        STA     $0701,X             
AA8C: 4C 2B DD        JMP     $DD2B               
AA8F: A5 A6           LDA     $A6                 
AA91: 18              CLC                         
AA92: 69 07           ADC     #$07                
AA94: 85 A6           STA     $A6                 
AA96: D0 EA           BNE     $AA82               ; {}
AA98: BD 02 07        LDA     $0702,X             
AA9B: D0 05           BNE     $AAA2               ; {}
AA9D: A9 19           LDA     #$19                
AA9F: 4C 67 C6        JMP     $C667               
AAA2: A9 36           LDA     #$36                
AAA4: 4C CD C4        JMP     $C4CD               
AAA7: BD 00 07        LDA     $0700,X             
AAAA: C9 F8           CMP     #$F8                
AAAC: B0 08           BCS     $AAB6               ; {}
AAAE: BD 03 07        LDA     $0703,X             
AAB1: C9 FC           CMP     #$FC                
AAB3: B0 01           BCS     $AAB6               ; {}
AAB5: 60              RTS                         
AAB6: 68              PLA                         
AAB7: 68              PLA                         
AAB8: 20 1D DD        JSR     $DD1D               
AABB: 8A              TXA                         
AABC: 48              PHA                         
AABD: 18              CLC                         
AABE: 69 10           ADC     #$10                
AAC0: AA              TAX                         
AAC1: 20 1D DD        JSR     $DD1D               
AAC4: 68              PLA                         
AAC5: AA              TAX                         
AAC6: 60              RTS                         
AAC7: AC 30 01        LDY     $0130               
AACA: B9 33 BE        LDA     $BE33,Y             ; {}
AACD: A8              TAY                         
AACE: 20 D4 AA        JSR     $AAD4               ; {}
AAD1: 60              RTS                         
AAD2: A0 1F           LDY     #$1F                
AAD4: A2 1F           LDX     #$1F                
AAD6: B9 36 BE        LDA     $BE36,Y             ; {}
AAD9: 9D 90 03        STA     $0390,X             
AADC: 88              DEY                         
AADD: CA              DEX                         
AADE: 10 F6           BPL     $AAD6               ; {}
AAE0: 60              RTS                         
AAE1: 85 02           STA     $02                 
AAE3: 84 03           STY     $03                 
AAE5: A5 1B           LDA     $1B                 
AAE7: 49 FF           EOR     #$FF                
AAE9: 29 01           AND     #$01                
AAEB: 0A              ASL     A                   
AAEC: A8              TAY                         
AAED: A5 FE           LDA     $FE                 
AAEF: 18              CLC                         
AAF0: 65 03           ADC     $03                 
AAF2: 4A              LSR     A                   
AAF3: 4A              LSR     A                   
AAF4: 4A              LSR     A                   
AAF5: 4A              LSR     A                   
AAF6: 18              CLC                         
AAF7: 79 F4 BA        ADC     $BAF4,Y             ; {}
AAFA: 85 00           STA     $00                 ; {ram.GP_00}
AAFC: A9 00           LDA     #$00                
AAFE: 79 F5 BA        ADC     $BAF5,Y             ; {}
AB01: 85 01           STA     $01                 
AB03: A5 02           LDA     $02                 
AB05: 29 F0           AND     #$F0                
AB07: 18              CLC                         
AB08: 65 00           ADC     $00                 ; {ram.GP_00}
AB0A: 85 00           STA     $00                 ; {ram.GP_00}
AB0C: A9 00           LDA     #$00                
AB0E: 65 01           ADC     $01                 
AB10: 85 01           STA     $01                 
AB12: 18              CLC                         
AB13: A5 FE           LDA     $FE                 
AB15: 65 03           ADC     $03                 
AB17: 90 20           BCC     $AB39               ; {}
AB19: 98              TYA                         
AB1A: D0 10           BNE     $AB2C               ; {}
AB1C: A9 F0           LDA     #$F0                
AB1E: 18              CLC                         
AB1F: 65 00           ADC     $00                 ; {ram.GP_00}
AB21: 85 00           STA     $00                 ; {ram.GP_00}
AB23: A9 00           LDA     #$00                
AB25: 65 01           ADC     $01                 
AB27: 85 01           STA     $01                 
AB29: 4C 39 AB        JMP     $AB39               ; {}
AB2C: A5 00           LDA     $00                 ; {ram.GP_00}
AB2E: 38              SEC                         
AB2F: E9 F0           SBC     #$F0                
AB31: 85 00           STA     $00                 ; {ram.GP_00}
AB33: A5 01           LDA     $01                 
AB35: E9 00           SBC     #$00                
AB37: 85 01           STA     $01                 
AB39: A0 00           LDY     #$00                
AB3B: B1 00           LDA     ($00),Y             ; {ram.GP_00}
AB3D: 60              RTS                         
AB3E: 20 5B AB        JSR     $AB5B               ; {}
AB41: 24 5C           BIT     $5C                 
AB43: 70 07           BVS     $AB4C               ; {}
AB45: BD 03 07        LDA     $0703,X             
AB48: C9 80           CMP     #$80                
AB4A: B0 04           BCS     $AB50               ; {}
AB4C: A9 00           LDA     #$00                
AB4E: F0 08           BEQ     $AB58               ; {}
AB50: DE 03 07        DEC     $0703,X             
AB53: 20 E6 AB        JSR     $ABE6               ; {}
AB56: A9 01           LDA     #$01                
AB58: 85 27           STA     $27                 
AB5A: 60              RTS                         
AB5B: AD D5 04        LDA     $04D5               
AB5E: C9 29           CMP     #$29                
AB60: F0 07           BEQ     $AB69               ; {}
AB62: AD D6 04        LDA     $04D6               
AB65: C9 29           CMP     #$29                
AB67: D0 F1           BNE     $AB5A               ; {}
AB69: A0 58           LDY     #$58                
AB6B: A9 04           LDA     #$04                
AB6D: 4C 90 CA        JMP     $CA90               
AB70: 60              RTS                         
AB71: A5 FE           LDA     $FE                 
AB73: 29 0F           AND     #$0F                
AB75: C9 02           CMP     #$02                
AB77: F0 19           BEQ     $AB92               ; {}
AB79: C9 03           CMP     #$03                
AB7B: F0 18           BEQ     $AB95               ; {}
AB7D: A5 68           LDA     $68                 
AB7F: 0A              ASL     A                   
AB80: A8              TAY                         
AB81: B9 8E AB        LDA     $AB8E,Y             ; {}
AB84: 85 00           STA     $00                 ; {ram.GP_00}
AB86: B9 8F AB        LDA     $AB8F,Y             ; {}
AB89: 85 01           STA     $01                 
AB8B: 6C 00 00        JMP     ($0000)             ; {ram.GP_00}
AB8E: 42 ; ????
AB8F: EE 98 AB        INC     $AB98               ; {}
AB92: 4C F3 AB        JMP     $ABF3               ; {}
AB95: 4C 47 AC        JMP     $AC47               ; {}
AB98: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
AB9B: A5 6A           LDA     $6A                 
AB9D: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
ABA0: A5 69           LDA     $69                 
ABA2: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
ABA5: A2 05           LDX     #$05                
ABA7: A9 12           LDA     #$12                
ABA9: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
ABAC: CA              DEX                         
ABAD: 10 FA           BPL     $ABA9               ; {}
ABAF: A9 00           LDA     #$00                
ABB1: 85 68           STA     $68                 
ABB3: 60              RTS                         
ABB4: A5 5C           LDA     $5C                 
ABB6: 10 2D           BPL     $ABE5               ; {}
ABB8: AD 00 01        LDA     $0100               
ABBB: 29 7F           AND     #$7F                
ABBD: 8D 00 01        STA     $0100               
ABC0: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
ABC3: 20 07 AE        JSR     $AE07               ; {}
ABC6: 20 DF AB        JSR     $ABDF               ; {}
ABC9: A9 00           LDA     #$00                
ABCB: 85 40           STA     $40                 
ABCD: 85 41           STA     $41                 
ABCF: 68              PLA                         
ABD0: 68              PLA                         
ABD1: AD 00 01        LDA     $0100               
ABD4: 09 80           ORA     #$80                
ABD6: 8D 00 01        STA     $0100               
ABD9: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
ABDC: 4C 38 9A        JMP     $9A38               ; {}
ABDF: A5 5C           LDA     $5C                 
ABE1: 29 7F           AND     #$7F                
ABE3: 85 5C           STA     $5C                 
ABE5: 60              RTS                         
ABE6: E6 FE           INC     $FE                 
ABE8: D0 08           BNE     $ABF2               ; {}
ABEA: E6 1B           INC     $1B                 
ABEC: A5 5C           LDA     $5C                 
ABEE: 09 80           ORA     #$80                
ABF0: 85 5C           STA     $5C                 
ABF2: 60              RTS                         
ABF3: AD 00 01        LDA     $0100               
ABF6: 09 04           ORA     #$04                
ABF8: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
ABFB: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
ABFE: AD 82 04        LDA     $0482               
AC01: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
AC04: AD 81 04        LDA     $0481               
AC07: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
AC0A: A0 00           LDY     #$00                
AC0C: 98              TYA                         
AC0D: 0A              ASL     A                   
AC0E: AA              TAX                         
AC0F: BD 83 04        LDA     $0483,X             
AC12: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
AC15: C8              INY                         
AC16: C0 1E           CPY     #$1E                
AC18: 90 F2           BCC     $AC0C               ; {}
AC1A: AD 81 04        LDA     $0481               
AC1D: 18              CLC                         
AC1E: 69 01           ADC     #$01                
AC20: 48              PHA                         
AC21: AD 82 04        LDA     $0482               
AC24: 69 00           ADC     #$00                
AC26: AC 02 20        LDY     $2002               ; {hard.P_STATUS}
AC29: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
AC2C: 68              PLA                         
AC2D: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
AC30: A0 00           LDY     #$00                
AC32: 98              TYA                         
AC33: 0A              ASL     A                   
AC34: AA              TAX                         
AC35: BD 84 04        LDA     $0484,X             
AC38: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
AC3B: C8              INY                         
AC3C: C0 1E           CPY     #$1E                
AC3E: 90 F2           BCC     $AC32               ; {}
AC40: AD 00 01        LDA     $0100               
AC43: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
AC46: 60              RTS                         
AC47: 20 A9 AD        JSR     $ADA9               ; {}
AC4A: A0 00           LDY     #$00                
AC4C: 98              TYA                         
AC4D: 0A              ASL     A                   
AC4E: 0A              ASL     A                   
AC4F: 0A              ASL     A                   
AC50: 18              CLC                         
AC51: 65 00           ADC     $00                 ; {ram.GP_00}
AC53: 85 03           STA     $03                 
AC55: 18              CLC                         
AC56: 69 C0           ADC     #$C0                
AC58: 48              PHA                         
AC59: A5 1B           LDA     $1B                 
AC5B: 49 01           EOR     #$01                
AC5D: 29 01           AND     #$01                
AC5F: 0A              ASL     A                   
AC60: 0A              ASL     A                   
AC61: 09 23           ORA     #$23                
AC63: AE 02 20        LDX     $2002               ; {hard.P_STATUS}
AC66: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
AC69: 68              PLA                         
AC6A: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
AC6D: A6 03           LDX     $03                 
AC6F: BD B0 03        LDA     $03B0,X             
AC72: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
AC75: C8              INY                         
AC76: C0 08           CPY     #$08                
AC78: 90 D2           BCC     $AC4C               ; {}
AC7A: 60              RTS                         
AC7B: A5 FE           LDA     $FE                 
AC7D: 29 F0           AND     #$F0                
AC7F: 4A              LSR     A                   
AC80: 4A              LSR     A                   
AC81: 4A              LSR     A                   
AC82: 85 00           STA     $00                 ; {ram.GP_00}
AC84: 8D 81 04        STA     $0481               
AC87: A5 1B           LDA     $1B                 
AC89: 49 01           EOR     #$01                
AC8B: 29 01           AND     #$01                
AC8D: 0A              ASL     A                   
AC8E: 0A              ASL     A                   
AC8F: 09 20           ORA     #$20                
AC91: 8D 82 04        STA     $0482               
AC94: 20 AF AC        JSR     $ACAF               ; {}
AC97: 20 B5 AC        JSR     $ACB5               ; {}
AC9A: A5 FE           LDA     $FE                 
AC9C: 29 F0           AND     #$F0                
AC9E: 4A              LSR     A                   
AC9F: 4A              LSR     A                   
ACA0: 4A              LSR     A                   
ACA1: 4A              LSR     A                   
ACA2: 65 62           ADC     $62                 
ACA4: 85 06           STA     $06                 
ACA6: A9 00           LDA     #$00                
ACA8: 65 63           ADC     $63                 
ACAA: 85 07           STA     $07                 
ACAC: 4C C7 AC        JMP     $ACC7               ; {}
ACAF: A5 1B           LDA     $1B                 
ACB1: 8D D1 04        STA     $04D1               
ACB4: 60              RTS                         
ACB5: AD D1 04        LDA     $04D1               
ACB8: 29 01           AND     #$01                
ACBA: 0A              ASL     A                   
ACBB: A8              TAY                         
ACBC: B9 F4 BA        LDA     $BAF4,Y             ; {}
ACBF: 85 62           STA     $62                 
ACC1: B9 F5 BA        LDA     $BAF5,Y             ; {}
ACC4: 85 63           STA     $63                 
ACC6: 60              RTS                         
ACC7: A0 0E           LDY     #$0E                
ACC9: 98              TYA                         
ACCA: 48              PHA                         
ACCB: 0A              ASL     A                   
ACCC: 0A              ASL     A                   
ACCD: 0A              ASL     A                   
ACCE: 0A              ASL     A                   
ACCF: A8              TAY                         
ACD0: B1 06           LDA     ($06),Y             
ACD2: 20 F4 AC        JSR     $ACF4               ; {}
ACD5: 68              PLA                         
ACD6: 48              PHA                         
ACD7: 0A              ASL     A                   
ACD8: 0A              ASL     A                   
ACD9: A8              TAY                         
ACDA: A5 02           LDA     $02                 
ACDC: 99 83 04        STA     $0483,Y             
ACDF: A5 03           LDA     $03                 
ACE1: 99 84 04        STA     $0484,Y             
ACE4: A5 04           LDA     $04                 
ACE6: 99 85 04        STA     $0485,Y             
ACE9: A5 05           LDA     $05                 
ACEB: 99 86 04        STA     $0486,Y             
ACEE: 68              PLA                         
ACEF: A8              TAY                         
ACF0: 88              DEY                         
ACF1: 10 D6           BPL     $ACC9               ; {}
ACF3: 60              RTS                         
ACF4: A0 00           LDY     #$00                
ACF6: 84 01           STY     $01                 
ACF8: A0 03           LDY     #$03                
ACFA: 0A              ASL     A                   
ACFB: 26 01           ROL     $01                 
ACFD: 0A              ASL     A                   
ACFE: 26 01           ROL     $01                 
AD00: 85 00           STA     $00                 ; {ram.GP_00}
AD02: A5 3A           LDA     $3A                 
AD04: C9 10           CMP     #$10                
AD06: B0 15           BCS     $AD1D               ; {}
AD08: A5 00           LDA     $00                 ; {ram.GP_00}
AD0A: 69 30           ADC     #$30                
AD0C: 85 00           STA     $00                 ; {ram.GP_00}
AD0E: A5 01           LDA     $01                 
AD10: 69 B9           ADC     #$B9                
AD12: 85 01           STA     $01                 
AD14: B1 00           LDA     ($00),Y             ; {ram.GP_00}
AD16: 99 02 00        STA     $0002,Y             
AD19: 88              DEY                         
AD1A: 10 F8           BPL     $AD14               ; {}
AD1C: 60              RTS                         
AD1D: A5 00           LDA     $00                 ; {ram.GP_00}
AD1F: 18              CLC                         
AD20: 69 30           ADC     #$30                
AD22: 85 00           STA     $00                 ; {ram.GP_00}
AD24: A5 01           LDA     $01                 
AD26: 69 B9           ADC     #$B9                
AD28: D0 E8           BNE     $AD12               ; {}
AD2A: 20 AF AC        JSR     $ACAF               ; {}
AD2D: 20 97 AD        JSR     $AD97               ; {}
AD30: 20 A9 AD        JSR     $ADA9               ; {}
AD33: A2 00           LDX     #$00                
AD35: 8A              TXA                         
AD36: 0A              ASL     A                   
AD37: 0A              ASL     A                   
AD38: 0A              ASL     A                   
AD39: 18              CLC                         
AD3A: 65 00           ADC     $00                 ; {ram.GP_00}
AD3C: A8              TAY                         
AD3D: B1 64           LDA     ($64),Y             
AD3F: 9D F0 03        STA     $03F0,X             
AD42: E8              INX                         
AD43: E0 08           CPX     #$08                
AD45: 90 EE           BCC     $AD35               ; {}
AD47: A5 FE           LDA     $FE                 
AD49: 29 10           AND     #$10                
AD4B: D0 1B           BNE     $AD68               ; {}
AD4D: A0 00           LDY     #$00                
AD4F: A9 33           LDA     #$33                
AD51: 20 86 AD        JSR     $AD86               ; {}
AD54: 29 CC           AND     #$CC                
AD56: 20 80 AD        JSR     $AD80               ; {}
AD59: C8              INY                         
AD5A: C0 07           CPY     #$07                
AD5C: 90 F1           BCC     $AD4F               ; {}
AD5E: A9 03           LDA     #$03                
AD60: 20 86 AD        JSR     $AD86               ; {}
AD63: 29 FC           AND     #$FC                
AD65: 4C 80 AD        JMP     $AD80               ; {}
AD68: A0 00           LDY     #$00                
AD6A: A9 CC           LDA     #$CC                
AD6C: 20 86 AD        JSR     $AD86               ; {}
AD6F: 29 33           AND     #$33                
AD71: 20 80 AD        JSR     $AD80               ; {}
AD74: C8              INY                         
AD75: C0 07           CPY     #$07                
AD77: 90 F1           BCC     $AD6A               ; {}
AD79: A9 0C           LDA     #$0C                
AD7B: 20 86 AD        JSR     $AD86               ; {}
AD7E: 29 F3           AND     #$F3                
AD80: 05 02           ORA     $02                 
AD82: 9D B0 03        STA     $03B0,X             
AD85: 60              RTS                         
AD86: 39 F0 03        AND     $03F0,Y             
AD89: 85 02           STA     $02                 
AD8B: 98              TYA                         
AD8C: 0A              ASL     A                   
AD8D: 0A              ASL     A                   
AD8E: 0A              ASL     A                   
AD8F: 18              CLC                         
AD90: 65 00           ADC     $00                 ; {ram.GP_00}
AD92: AA              TAX                         
AD93: BD B0 03        LDA     $03B0,X             
AD96: 60              RTS                         
AD97: AD D1 04        LDA     $04D1               
AD9A: 29 01           AND     #$01                
AD9C: 0A              ASL     A                   
AD9D: A8              TAY                         
AD9E: B9 FC BA        LDA     $BAFC,Y             ; {}
ADA1: 85 64           STA     $64                 
ADA3: B9 FD BA        LDA     $BAFD,Y             ; {}
ADA6: 85 65           STA     $65                 
ADA8: 60              RTS                         
ADA9: A9 00           LDA     #$00                
ADAB: 85 00           STA     $00                 ; {ram.GP_00}
ADAD: A5 FE           LDA     $FE                 
ADAF: 29 E0           AND     #$E0                
ADB1: 0A              ASL     A                   
ADB2: 26 00           ROL     $00                 ; {ram.GP_00}
ADB4: 0A              ASL     A                   
ADB5: 26 00           ROL     $00                 ; {ram.GP_00}
ADB7: 0A              ASL     A                   
ADB8: 26 00           ROL     $00                 ; {ram.GP_00}
ADBA: 60              RTS                         
ADBB: A9 00           LDA     #$00                
ADBD: 85 5C           STA     $5C                 
ADBF: 8D D2 04        STA     $04D2               
ADC2: 20 24 AE        JSR     $AE24               ; {}
ADC5: A9 06           LDA     #$06                
ADC7: 20 90 CA        JSR     $CA90               
ADCA: A9 00           LDA     #$00                
ADCC: 8D D2 04        STA     $04D2               
ADCF: EE D1 04        INC     $04D1               
ADD2: 20 27 AE        JSR     $AE27               ; {}
ADD5: A9 06           LDA     #$06                
ADD7: 20 90 CA        JSR     $CA90               
ADDA: 20 0F AE        JSR     $AE0F               ; {}
ADDD: A9 00           LDA     #$00                
ADDF: 85 FE           STA     $FE                 
ADE1: 85 1B           STA     $1B                 
ADE3: 20 7B AC        JSR     $AC7B               ; {}
ADE6: 20 2A AD        JSR     $AD2A               ; {}
ADE9: 20 F3 AB        JSR     $ABF3               ; {}
ADEC: 20 47 AC        JSR     $AC47               ; {}
ADEF: A5 FE           LDA     $FE                 
ADF1: 18              CLC                         
ADF2: 69 10           ADC     #$10                
ADF4: 85 FE           STA     $FE                 
ADF6: A5 1B           LDA     $1B                 
ADF8: 69 00           ADC     #$00                
ADFA: 85 1B           STA     $1B                 
ADFC: C9 02           CMP     #$02                
ADFE: 90 E3           BCC     $ADE3               ; {}
AE00: A9 01           LDA     #$01                
AE02: 85 1B           STA     $1B                 
AE04: 85 FE           STA     $FE                 
AE06: 60              RTS                         
AE07: 20 24 AE        JSR     $AE24               ; {}
AE0A: A9 06           LDA     #$06                
AE0C: 20 90 CA        JSR     $CA90               
AE0F: A0 0F           LDY     #$0F                
AE11: B9 00 05        LDA     $0500,Y             
AE14: 99 E0 06        STA     $06E0,Y             
AE17: 88              DEY                         
AE18: 10 F7           BPL     $AE11               ; {}
AE1A: 60              RTS                         
AE1B: A5 5C           LDA     $5C                 
AE1D: 09 40           ORA     #$40                
AE1F: 85 5C           STA     $5C                 
AE21: 68              PLA                         
AE22: 68              PLA                         
AE23: 60              RTS                         
AE24: 20 AF AC        JSR     $ACAF               ; {}
AE27: A9 00           LDA     #$00                
AE29: 8D D2 04        STA     $04D2               
AE2C: AD 30 01        LDA     $0130               
AE2F: 0A              ASL     A                   
AE30: A8              TAY                         
AE31: B9 04 BB        LDA     $BB04,Y             ; {}
AE34: 85 00           STA     $00                 ; {ram.GP_00}
AE36: B9 05 BB        LDA     $BB05,Y             ; {}
AE39: 85 01           STA     $01                 
AE3B: AD D1 04        LDA     $04D1               
AE3E: 0A              ASL     A                   
AE3F: A8              TAY                         
AE40: B1 00           LDA     ($00),Y             ; {ram.GP_00}
AE42: 85 49           STA     $49                 
AE44: C8              INY                         
AE45: B1 00           LDA     ($00),Y             ; {ram.GP_00}
AE47: C9 FF           CMP     #$FF                
AE49: F0 D0           BEQ     $AE1B               ; {}
AE4B: 85 4A           STA     $4A                 
AE4D: 20 60 AE        JSR     $AE60               ; {}
AE50: 60              RTS                         
AE51: AD D1 04        LDA     $04D1               
AE54: 0A              ASL     A                   
AE55: A8              TAY                         
AE56: B9 0A BB        LDA     $BB0A,Y             ; {}
AE59: 85 49           STA     $49                 
AE5B: B9 0B BB        LDA     $BB0B,Y             ; {}
AE5E: 85 4A           STA     $4A                 
AE60: 20 B5 AC        JSR     $ACB5               ; {}
AE63: 20 97 AD        JSR     $AD97               ; {}
AE66: 20 29 AF        JSR     $AF29               ; {}
AE69: A0 00           LDY     #$00                
AE6B: B1 49           LDA     ($49),Y             
AE6D: 20 36 AF        JSR     $AF36               ; {}
AE70: A0 01           LDY     #$01                
AE72: B1 49           LDA     ($49),Y             
AE74: C9 FD           CMP     #$FD                
AE76: F0 17           BEQ     $AE8F               ; {}
AE78: 85 4D           STA     $4D                 
AE7A: C8              INY                         
AE7B: B1 49           LDA     ($49),Y             
AE7D: 85 4E           STA     $4E                 
AE7F: C8              INY                         
AE80: B1 49           LDA     ($49),Y             
AE82: 85 4F           STA     $4F                 
AE84: 98              TYA                         
AE85: 48              PHA                         
AE86: 20 90 AE        JSR     $AE90               ; {}
AE89: 68              PLA                         
AE8A: A8              TAY                         
AE8B: C8              INY                         
AE8C: 4C 72 AE        JMP     $AE72               ; {}
AE8F: 60              RTS                         
AE90: 20 DB AE        JSR     $AEDB               ; {}
AE93: A9 00           LDA     #$00                
AE95: 85 5F           STA     $5F                 
AE97: A5 4D           LDA     $4D                 
AE99: 29 F0           AND     #$F0                
AE9B: 85 61           STA     $61                 
AE9D: A5 5F           LDA     $5F                 
AE9F: 0A              ASL     A                   
AEA0: 0A              ASL     A                   
AEA1: 0A              ASL     A                   
AEA2: 0A              ASL     A                   
AEA3: 18              CLC                         
AEA4: 65 61           ADC     $61                 
AEA6: C9 F0           CMP     #$F0                
AEA8: B0 3F           BCS     $AEE9               ; {}
AEAA: A0 00           LDY     #$00                
AEAC: B1 51           LDA     ($51),Y             
AEAE: C9 FF           CMP     #$FF                
AEB0: F0 37           BEQ     $AEE9               ; {}
AEB2: 85 53           STA     $53                 
AEB4: 29 0F           AND     #$0F                
AEB6: AA              TAX                         
AEB7: C8              INY                         
AEB8: B1 51           LDA     ($51),Y             
AEBA: 99 53 00        STA     $0053,Y             
AEBD: C8              INY                         
AEBE: CA              DEX                         
AEBF: D0 F7           BNE     $AEB8               ; {}
AEC1: 20 4A AF        JSR     $AF4A               ; {}
AEC4: A5 53           LDA     $53                 
AEC6: 29 0F           AND     #$0F                
AEC8: 38              SEC                         
AEC9: 65 51           ADC     $51                 
AECB: 85 51           STA     $51                 
AECD: A9 00           LDA     #$00                
AECF: 65 52           ADC     $52                 
AED1: 85 52           STA     $52                 
AED3: 20 EA AE        JSR     $AEEA               ; {}
AED6: E6 5F           INC     $5F                 
AED8: 4C 97 AE        JMP     $AE97               ; {}
AEDB: A5 4E           LDA     $4E                 
AEDD: 0A              ASL     A                   
AEDE: A8              TAY                         
AEDF: B9 E2 BB        LDA     $BBE2,Y             ; {}
AEE2: 85 51           STA     $51                 
AEE4: B9 E3 BB        LDA     $BBE3,Y             ; {}
AEE7: 85 52           STA     $52                 
AEE9: 60              RTS                         
AEEA: A5 5F           LDA     $5F                 
AEEC: 0A              ASL     A                   
AEED: 0A              ASL     A                   
AEEE: 0A              ASL     A                   
AEEF: 0A              ASL     A                   
AEF0: 85 5D           STA     $5D                 
AEF2: A5 53           LDA     $53                 
AEF4: 29 F0           AND     #$F0                
AEF6: 4A              LSR     A                   
AEF7: 4A              LSR     A                   
AEF8: 4A              LSR     A                   
AEF9: 4A              LSR     A                   
AEFA: 65 5D           ADC     $5D                 
AEFC: 18              CLC                         
AEFD: 65 4D           ADC     $4D                 
AEFF: 85 5D           STA     $5D                 
AF01: A5 53           LDA     $53                 
AF03: 29 0F           AND     #$0F                
AF05: AA              TAX                         
AF06: 18              CLC                         
AF07: A5 62           LDA     $62                 
AF09: 65 5D           ADC     $5D                 
AF0B: 85 5D           STA     $5D                 
AF0D: A9 00           LDA     #$00                
AF0F: 65 63           ADC     $63                 
AF11: 85 5E           STA     $5E                 
AF13: A0 00           LDY     #$00                
AF15: B9 54 00        LDA     $0054,Y             
AF18: 91 5D           STA     ($5D),Y             
AF1A: 98              TYA                         
AF1B: 18              CLC                         
AF1C: 65 5D           ADC     $5D                 
AF1E: 29 0F           AND     #$0F                
AF20: C9 0F           CMP     #$0F                
AF22: B0 04           BCS     $AF28               ; {}
AF24: C8              INY                         
AF25: CA              DEX                         
AF26: D0 ED           BNE     $AF15               ; {}
AF28: 60              RTS                         
AF29: A0 00           LDY     #$00                
AF2B: A9 00           LDA     #$00                
AF2D: 91 62           STA     ($62),Y             
AF2F: C8              INY                         
AF30: 98              TYA                         
AF31: C9 F0           CMP     #$F0                
AF33: 90 F6           BCC     $AF2B               ; {}
AF35: 60              RTS                         
AF36: 29 03           AND     #$03                
AF38: A8              TAY                         
AF39: B9 46 AF        LDA     $AF46,Y             ; {}
AF3C: A0 00           LDY     #$00                
AF3E: 91 64           STA     ($64),Y             
AF40: C8              INY                         
AF41: C0 40           CPY     #$40                
AF43: 90 F9           BCC     $AF3E               ; {}
AF45: 60              RTS                         
AF46: 00              BRK                         
AF47: 55 AA           EOR     $AA,X               
AF49: FF ; ????
AF4A: A5 53           LDA     $53                 
AF4C: 29 F0           AND     #$F0                
AF4E: 4A              LSR     A                   
AF4F: 4A              LSR     A                   
AF50: 4A              LSR     A                   
AF51: 4A              LSR     A                   
AF52: 8D D0 04        STA     $04D0               
AF55: A5 53           LDA     $53                 
AF57: 29 0F           AND     #$0F                
AF59: 6D D0 04        ADC     $04D0               
AF5C: 8D D0 04        STA     $04D0               
AF5F: A5 4D           LDA     $4D                 
AF61: 29 0F           AND     #$0F                
AF63: 8D CD 04        STA     $04CD               
AF66: 18              CLC                         
AF67: 6D D0 04        ADC     $04D0               
AF6A: C9 10           CMP     #$10                
AF6C: 90 09           BCC     $AF77               ; {}
AF6E: A9 10           LDA     #$10                
AF70: 38              SEC                         
AF71: ED CD 04        SBC     $04CD               
AF74: 8D D0 04        STA     $04D0               
AF77: A9 00           LDA     #$00                
AF79: 8D CD 04        STA     $04CD               
AF7C: A5 5F           LDA     $5F                 
AF7E: 0A              ASL     A                   
AF7F: 0A              ASL     A                   
AF80: 0A              ASL     A                   
AF81: 0A              ASL     A                   
AF82: 18              CLC                         
AF83: 65 4D           ADC     $4D                 
AF85: 18              CLC                         
AF86: 6D CD 04        ADC     $04CD               
AF89: 85 60           STA     $60                 
AF8B: 29 E0           AND     #$E0                
AF8D: 4A              LSR     A                   
AF8E: 4A              LSR     A                   
AF8F: 85 66           STA     $66                 
AF91: A5 60           LDA     $60                 
AF93: 29 0F           AND     #$0F                
AF95: 4A              LSR     A                   
AF96: 18              CLC                         
AF97: 65 66           ADC     $66                 
AF99: 18              CLC                         
AF9A: 65 64           ADC     $64                 
AF9C: 85 66           STA     $66                 
AF9E: A9 00           LDA     #$00                
AFA0: 65 65           ADC     $65                 
AFA2: 85 67           STA     $67                 
AFA4: A5 60           LDA     $60                 
AFA6: 29 10           AND     #$10                
AFA8: 4A              LSR     A                   
AFA9: 4A              LSR     A                   
AFAA: 4A              LSR     A                   
AFAB: 8D CE 04        STA     $04CE               
AFAE: A5 60           LDA     $60                 
AFB0: 29 01           AND     #$01                
AFB2: 0D CE 04        ORA     $04CE               
AFB5: F0 0E           BEQ     $AFC5               ; {}
AFB7: AA              TAX                         
AFB8: A9 03           LDA     #$03                
AFBA: 0A              ASL     A                   
AFBB: 0A              ASL     A                   
AFBC: CA              DEX                         
AFBD: 8D CE 04        STA     $04CE               
AFC0: F0 08           BEQ     $AFCA               ; {}
AFC2: 4C BA AF        JMP     $AFBA               ; {}
AFC5: A9 03           LDA     #$03                
AFC7: 8D CE 04        STA     $04CE               
AFCA: AD CE 04        LDA     $04CE               
AFCD: 49 FF           EOR     #$FF                
AFCF: A0 00           LDY     #$00                
AFD1: 31 66           AND     ($66),Y             
AFD3: 8D CF 04        STA     $04CF               
AFD6: A5 4F           LDA     $4F                 
AFD8: 29 02           AND     #$02                
AFDA: F0 05           BEQ     $AFE1               ; {}
AFDC: A9 AA           LDA     #$AA                
AFDE: 20 FF AF        JSR     $AFFF               ; {}
AFE1: A5 4F           LDA     $4F                 
AFE3: 29 01           AND     #$01                
AFE5: F0 05           BEQ     $AFEC               ; {}
AFE7: A9 55           LDA     #$55                
AFE9: 20 FF AF        JSR     $AFFF               ; {}
AFEC: AD CF 04        LDA     $04CF               
AFEF: 91 66           STA     ($66),Y             
AFF1: EE CD 04        INC     $04CD               
AFF4: AD CD 04        LDA     $04CD               
AFF7: CD D0 04        CMP     $04D0               
AFFA: B0 0C           BCS     $B008               ; {}
AFFC: 4C 7C AF        JMP     $AF7C               ; {}
AFFF: 2D CE 04        AND     $04CE               
B002: 0D CF 04        ORA     $04CF               
B005: 8D CF 04        STA     $04CF               
B008: 60              RTS                         
B009: A9 10           LDA     #$10                
B00B: 85 0A           STA     $0A                 
B00D: C6 1B           DEC     $1B                 
B00F: 20 7B AC        JSR     $AC7B               ; {}
B012: 20 2A AD        JSR     $AD2A               ; {}
B015: 20 F3 AB        JSR     $ABF3               ; {}
B018: 20 47 AC        JSR     $AC47               ; {}
B01B: A5 FE           LDA     $FE                 
B01D: 18              CLC                         
B01E: 69 10           ADC     #$10                
B020: 85 FE           STA     $FE                 
B022: A5 1B           LDA     $1B                 
B024: 69 00           ADC     #$00                
B026: 85 1B           STA     $1B                 
B028: C6 0A           DEC     $0A                 
B02A: 10 E3           BPL     $B00F               ; {}
B02C: A5 FE           LDA     $FE                 
B02E: 38              SEC                         
B02F: E9 10           SBC     #$10                
B031: 85 FE           STA     $FE                 
B033: A5 1B           LDA     $1B                 
B035: E9 00           SBC     #$00                
B037: 85 1B           STA     $1B                 
B039: 60              RTS                         
B03A: 00              BRK                         
B03B: 33 ; ????
B03C: 05 00           ORA     $00                 ; {ram.GP_00}
B03E: 3E 09 02        ROL     $0209,X             
B041: 4D 07 00        EOR     $0007               
B044: 4E 0E 00        LSR     $000E               
B047: 77 ; ????
B048: 0F ; ????
B049: 00              BRK                         
B04A: 7D 09 02        ADC     $0209,X             
B04D: 88              DEY                         
B04E: 0C ; ????
B04F: 02 ; ????
B050: 8A              TXA                         
B051: 0C ; ????
B052: 02 ; ????
B053: 8C 07 00        STY     $0007               
B056: 8D 0E 00        STA     $000E               
B059: 8F ; ????
B05A: 0E 00 A2        ASL     $A200               ; {}
B05D: 09 02           ORA     #$02                
B05F: AD 23 00        LDA     $0023               
B062: C0 16           CPY     #$16                
B064: 00              BRK                         
B065: C4 16           CPY     $16                 
B067: 00              BRK                         
B068: C8              INY                         
B069: 16 00           ASL     $00,X               ; {ram.GP_00}
B06B: CC 16 00        CPY     $0016               
B06E: FD FF 00        SBC     $00FF,X             
B071: 38              SEC                         
B072: 05 00           ORA     $00                 ; {ram.GP_00}
B074: 4D 07 00        EOR     $0007               
B077: 5E 0E 00        LSR     $000E,X             
B07A: 6D 07 00        ADC     $0007               
B07D: 83 ; ????
B07E: 0B ; ????
B07F: 02 ; ????
B080: 87 ; ????
B081: 0B ; ????
B082: 02 ; ????
B083: 8C 07 00        STY     $0007               
B086: 8D 0E 00        STA     $000E               
B089: 8F ; ????
B08A: 0E 00 AD        ASL     $AD00               ; {}
B08D: 23 ; ????
B08E: 00              BRK                         
B08F: B0 0F           BCS     $B0A0               ; {}
B091: 00              BRK                         
B092: B4 0F           LDY     $0F,X               
B094: 00              BRK                         
B095: B8              CLV                         
B096: 0E 00 C0        ASL     $C000               
B099: 12 ; ????
B09A: 03 ; ????
B09B: C4 12           CPY     $12                 
B09D: 03 ; ????
B09E: CA              DEX                         
B09F: 0F ; ????
B0A0: 00              BRK                         
B0A1: CE 0F 00        DEC     $000F               
B0A4: DA ; ????
B0A5: 12 ; ????
B0A6: 03 ; ????
B0A7: DE 12 03        DEC     $0312,X             
B0AA: FD FF 00        SBC     $00FF,X             
B0AD: 12 ; ????
B0AE: 1D 03 28        ORA     $2803,X             
B0B1: 17 ; ????
B0B2: 03 ; ????
B0B3: 45 05           EOR     $05                 
B0B5: 00              BRK                         
B0B6: 4E 0E 02        LSR     $020E               
B0B9: 53 ; ????
B0BA: 0B ; ????
B0BB: 02 ; ????
B0BC: 69 0B           ADC     #$0B                
B0BE: 02 ; ????
B0BF: 6E 07 01        ROR     $0107               
B0C2: 73 ; ????
B0C3: 0C ; ????
B0C4: 00              BRK                         
B0C5: 89 ; ????
B0C6: 0C ; ????
B0C7: 00              BRK                         
B0C8: 8C 07 01        STY     $0107               
B0CB: 8D 0E 02        STA     $020E               
B0CE: 8F ; ????
B0CF: 0E 02 AD        ASL     $AD02               ; {}
B0D2: 23 ; ????
B0D3: 02 ; ????
B0D4: B0 0F           BCS     $B0E5               ; {}
B0D6: 00              BRK                         
B0D7: C0 10           CPY     #$10                
B0D9: 02 ; ????
B0DA: C3 ; ????
B0DB: 0F ; ????
B0DC: 00              BRK                         
B0DD: C7 ; ????
B0DE: 0F ; ????
B0DF: 00              BRK                         
B0E0: CB ; ????
B0E1: 0F ; ????
B0E2: 00              BRK                         
B0E3: FD FF 00        SBC     $00FF,X             
B0E6: 20 0D 02        JSR     $020D               
B0E9: 28              PLP                         
B0EA: 05 00           ORA     $00                 ; {ram.GP_00}
B0EC: 40              RTI                         
B0ED: 0E 00 42        ASL     $4200               
B0F0: 06 00           ASL     $00                 ; {ram.GP_00}
B0F2: 72 ; ????
B0F3: 0D 02 80        ORA     $8002               ; {}
B0F6: 0E 00 81        ASL     $8100               ; {}
B0F9: 0E 00 83        ASL     $8300               ; {}
B0FC: 06 00           ASL     $00                 ; {ram.GP_00}
B0FE: 9F ; ????
B0FF: 0D 02 A2        ORA     $A202               ; {}
B102: 00              BRK                         
B103: 00              BRK                         
B104: C0 0F           CPY     #$0F                
B106: 00              BRK                         
B107: C4 0F           CPY     $0F                 
B109: 00              BRK                         
B10A: C8              INY                         
B10B: 0F ; ????
B10C: 00              BRK                         
B10D: CC 02 01        CPY     $0102               
B110: D0 02           BNE     $B114               ; {}
B112: 01 D4           ORA     ($D4,X)             
B114: 02 ; ????
B115: 01 D8           ORA     ($D8,X)             
B117: 02 ; ????
B118: 01 FD           ORA     ($FD,X)             
B11A: FF ; ????
B11B: 02 ; ????
B11C: 1B ; ????
B11D: 05 00           ORA     $00                 ; {ram.GP_00}
B11F: 88              DEY                         
B120: 14 ; ????
B121: 03 ; ????
B122: 9F ; ????
B123: 0D 02 A4        ORA     $A402               ; {}
B126: 0D 02 AE        ORA     $AE02               ; {}
B129: 0D 02 B0        ORA     $B002               ; {}
B12C: 0D 02 B5        ORA     $B502               ; {}
B12F: 0D 02 C0        ORA     $C002               
B132: 02 ; ????
B133: 01 C4           ORA     ($C4,X)             
B135: 02 ; ????
B136: 01 C8           ORA     ($C8,X)             
B138: 02 ; ????
B139: 01 CC           ORA     ($CC,X)             
B13B: 02 ; ????
B13C: 01 FD           ORA     ($FD,X)             
B13E: FF ; ????
B13F: 01 65           ORA     ($65,X)             
B141: 01 01           ORA     ($01,X)             
B143: 6E 01 01        ROR     $0101               
B146: 7C ; ????
B147: 0D 02 8B        ORA     $8B02               ; {}
B14A: 0D 02 90        ORA     $9002               ; {}
B14D: 01 01           ORA     ($01,X)             
B14F: 9A              TXS                         
B150: 02 ; ????
B151: 01 B5           ORA     ($B5,X)             
B153: 03 ; ????
B154: 01 C0           ORA     ($C0,X)             
B156: 02 ; ????
B157: 01 C4           ORA     ($C4,X)             
B159: 02 ; ????
B15A: 01 C8           ORA     ($C8,X)             
B15C: 02 ; ????
B15D: 01 CC           ORA     ($CC,X)             
B15F: 02 ; ????
B160: 01 FD           ORA     ($FD,X)             
B162: FF ; ????
B163: 01 34           ORA     ($34,X)             
B165: 05 00           ORA     $00                 ; {ram.GP_00}
B167: 6D 13 01        ADC     $0113               
B16A: 88              DEY                         
B16B: 08              PHP                         
B16C: 02 ; ????
B16D: 98              TYA                         
B16E: 02 ; ????
B16F: 01 A7           ORA     ($A7,X)             
B171: 01 01           ORA     ($01,X)             
B173: B0 13           BCS     $B188               ; {}
B175: 01 B1           ORA     ($B1,X)             
B177: 08              PHP                         
B178: 02 ; ????
B179: C0 04           CPY     #$04                
B17B: 01 C4           ORA     ($C4,X)             
B17D: 04 ; ????
B17E: 01 C5           ORA     ($C5,X)             
B180: 11 03           ORA     ($03),Y             
B182: C8              INY                         
B183: 04 ; ????
B184: 01 CC           ORA     ($CC,X)             
B186: 04 ; ????
B187: 01 CE           ORA     ($CE,X)             
B189: 11 03           ORA     ($03),Y             
B18B: FD FF 01        SBC     $01FF,X             
B18E: 1B ; ????
B18F: 14 ; ????
B190: 03 ; ????
B191: 22 ; ????
B192: 05 00           ORA     $00                 ; {ram.GP_00}
B194: 79 08 02        ADC     $0208,Y             
B197: 87 ; ????
B198: 08              PHP                         
B199: 02 ; ????
B19A: 89 ; ????
B19B: 02 ; ????
B19C: 01 94           ORA     ($94,X)             
B19E: 08              PHP                         
B19F: 02 ; ????
B1A0: 97 ; ????
B1A1: 02 ; ????
B1A2: 01 9D           ORA     ($9D,X)             
B1A4: 08              PHP                         
B1A5: 02 ; ????
B1A6: A4 02           LDY     $02                 
B1A8: 01 AD           ORA     ($AD,X)             
B1AA: 02 ; ????
B1AB: 01 B0           ORA     ($B0,X)             
B1AD: 08              PHP                         
B1AE: 02 ; ????
B1AF: C0 04           CPY     #$04                
B1B1: 01 C4           ORA     ($C4,X)             
B1B3: 04 ; ????
B1B4: 01 C8           ORA     ($C8,X)             
B1B6: 04 ; ????
B1B7: 01 CC           ORA     ($CC,X)             
B1B9: 04 ; ????
B1BA: 01 FD           ORA     ($FD,X)             
B1BC: FF ; ????
B1BD: 01 34           ORA     ($34,X)             
B1BF: 05 00           ORA     $00                 ; {ram.GP_00}
B1C1: B2 ; ????
B1C2: 08              PHP                         
B1C3: 02 ; ????
B1C4: B8              CLV                         
B1C5: 08              PHP                         
B1C6: 02 ; ????
B1C7: BE 08 02        LDX     $0208,Y             
B1CA: C2 ; ????
B1CB: 04 ; ????
B1CC: 01 C8           ORA     ($C8,X)             
B1CE: 02 ; ????
B1CF: 01 CE           ORA     ($CE,X)             
B1D1: 04 ; ????
B1D2: 01 FD           ORA     ($FD,X)             
B1D4: FF ; ????
B1D5: 01 14           ORA     ($14,X)             
B1D7: 05 00           ORA     $00                 ; {ram.GP_00}
B1D9: 3A ; ????
B1DA: 0D 02 49        ORA     $4902               
B1DD: 0D 02 5C        ORA     $5C02               
B1E0: 08              PHP                         
B1E1: 02 ; ????
B1E2: 66 02           ROR     $02                 
B1E4: 01 68           ORA     ($68,X)             
B1E6: 04 ; ????
B1E7: 01 6C           ORA     ($6C,X)             
B1E9: 04 ; ????
B1EA: 01 81           ORA     ($81,X)             
B1EC: 13 ; ????
B1ED: 01 90           ORA     ($90,X)             
B1EF: 01 01           ORA     ($01,X)             
B1F1: 94 01           STY     $01,X               
B1F3: 01 9A           ORA     ($9A,X)             
B1F5: 14 ; ????
B1F6: 03 ; ????
B1F7: B0 08           BCS     $B201               ; {}
B1F9: 02 ; ????
B1FA: C0 04           CPY     #$04                
B1FC: 01 C4           ORA     ($C4,X)             
B1FE: 04 ; ????
B1FF: 01 C8           ORA     ($C8,X)             
B201: 04 ; ????
B202: 01 CC           ORA     ($CC,X)             
B204: 04 ; ????
B205: 01 FD           ORA     ($FD,X)             
B207: FF ; ????
B208: 01 19           ORA     ($19,X)             
B20A: 05 00           ORA     $00                 ; {ram.GP_00}
B20C: 50 08           BVC     $B216               ; {}
B20E: 02 ; ????
B20F: 60              RTS                         
B210: 01 01           ORA     ($01,X)             
B212: 64 ; ????
B213: 01 01           ORA     ($01,X)             
B215: 66 01           ROR     $01                 
B217: 01 6C           ORA     ($6C,X)             
B219: 08              PHP                         
B21A: 02 ; ????
B21B: 75 14           ADC     $14,X               
B21D: 03 ; ????
B21E: 7C ; ????
B21F: 01 01           ORA     ($01,X)             
B221: B0 08           BCS     $B22B               ; {}
B223: 02 ; ????
B224: B4 0B           LDY     $0B,X               
B226: 02 ; ????
B227: B5 08           LDA     $08,X               
B229: 02 ; ????
B22A: BE 0B 02        LDX     $020B,Y             
B22D: C0 04           CPY     #$04                
B22F: 01 C4           ORA     ($C4,X)             
B231: 04 ; ????
B232: 01 C8           ORA     ($C8,X)             
B234: 04 ; ????
B235: 01 CA           ORA     ($CA,X)             
B237: 11 03           ORA     ($03),Y             
B239: CC 04 01        CPY     $0104               
B23C: FD FF 01        SBC     $01FF,X             
B23F: 4B ; ????
B240: 09 02           ORA     #$02                
B242: 5B ; ????
B243: 0A              ASL     A                   
B244: 01 8A           ORA     ($8A,X)             
B246: 1A ; ????
B247: 01 9E           ORA     ($9E,X)             
B249: 09 02           ORA     #$02                
B24B: A9 1A           LDA     #$1A                
B24D: 01 AC           ORA     ($AC,X)             
B24F: 02 ; ????
B250: 01 B1           ORA     ($B1,X)             
B252: 13 ; ????
B253: 01 B2           ORA     ($B2,X)             
B255: 08              PHP                         
B256: 02 ; ????
B257: C0 04           CPY     #$04                
B259: 01 C4           ORA     ($C4,X)             
B25B: 04 ; ????
B25C: 01 C8           ORA     ($C8,X)             
B25E: 04 ; ????
B25F: 01 CC           ORA     ($CC,X)             
B261: 04 ; ????
B262: 01 FD           ORA     ($FD,X)             
B264: FF ; ????
B265: 01 24           ORA     ($24,X)             
B267: 05 00           ORA     $00                 ; {ram.GP_00}
B269: 9F ; ????
B26A: 03 ; ????
B26B: 01 A6           ORA     ($A6,X)             
B26D: 03 ; ????
B26E: 01 B2           ORA     ($B2,X)             
B270: 0B ; ????
B271: 02 ; ????
B272: B8              CLV                         
B273: 0B ; ????
B274: 02 ; ????
B275: BB ; ????
B276: 03 ; ????
B277: 01 BE           ORA     ($BE,X)             
B279: 0B ; ????
B27A: 02 ; ????
B27B: C0 02           CPY     #$02                
B27D: 01 C4           ORA     ($C4,X)             
B27F: 02 ; ????
B280: 01 C8           ORA     ($C8,X)             
B282: 02 ; ????
B283: 01 CC           ORA     ($CC,X)             
B285: 02 ; ????
B286: 01 FD           ORA     ($FD,X)             
B288: FF ; ????
B289: 01 0E           ORA     ($0E,X)             
B28B: 02 ; ????
B28C: 01 3C           ORA     ($3C,X)             
B28E: 01 01           ORA     ($01,X)             
B290: 6B ; ????
B291: 13 ; ????
B292: 01 98           ORA     ($98,X)             
B294: 13 ; ????
B295: 01 B3           ORA     ($B3,X)             
B297: 09 02           ORA     #$02                
B299: C3 ; ????
B29A: 04 ; ????
B29B: 01 C6           ORA     ($C6,X)             
B29D: 11 03           ORA     ($03),Y             
B29F: C9 11           CMP     #$11                
B2A1: 03 ; ????
B2A2: CC 11 03        CPY     $0311               
B2A5: CF ; ????
B2A6: 02 ; ????
B2A7: 01 D6           ORA     ($D6,X)             
B2A9: 02 ; ????
B2AA: 01 DA           ORA     ($DA,X)             
B2AC: 02 ; ????
B2AD: 01 DE           ORA     ($DE,X)             
B2AF: 02 ; ????
B2B0: 01 FD           ORA     ($FD,X)             
B2B2: FF ; ????
B2B3: 01 28           ORA     ($28,X)             
B2B5: 05 00           ORA     $00                 ; {ram.GP_00}
B2B7: 7E 09 02        ROR     $0209,X             
B2BA: 94 09           STY     $09,X               
B2BC: 02 ; ????
B2BD: 9E ; ????
B2BE: 02 ; ????
B2BF: 01 B4           ORA     ($B4,X)             
B2C1: 03 ; ????
B2C2: 01 C3           ORA     ($C3,X)             
B2C4: 03 ; ????
B2C5: 01 C4           ORA     ($C4,X)             
B2C7: 03 ; ????
B2C8: 01 C5           ORA     ($C5,X)             
B2CA: 12 ; ????
B2CB: 03 ; ????
B2CC: C8              INY                         
B2CD: 04 ; ????
B2CE: 01 CC           ORA     ($CC,X)             
B2D0: 04 ; ????
B2D1: 01 FD           ORA     ($FD,X)             
B2D3: FF ; ????
B2D4: 00              BRK                         
B2D5: 20 0D 02        JSR     $020D               
B2D8: 31 0D           AND     ($0D),Y             
B2DA: 02 ; ????
B2DB: 40              RTI                         
B2DC: 0E 00 52        ASL     $5200               
B2DF: 06 00           ASL     $00                 ; {ram.GP_00}
B2E1: 75 0F           ADC     $0F,X               
B2E3: 00              BRK                         
B2E4: 79 0F 00        ADC     $000F,Y             
B2E7: 80 ; ????
B2E8: 0E 00 81        ASL     $8100               ; {}
B2EB: 0E 00 83        ASL     $8300               ; {}
B2EE: 06 00           ASL     $00                 ; {ram.GP_00}
B2F0: 86 0C           STX     $0C                 
B2F2: 02 ; ????
B2F3: 8A              TXA                         
B2F4: 0C ; ????
B2F5: 02 ; ????
B2F6: A2 00           LDX     #$00                
B2F8: 00              BRK                         
B2F9: BE 0D 02        LDX     $020D,Y             
B2FC: C0 16           CPY     #$16                
B2FE: 00              BRK                         
B2FF: C4 16           CPY     $16                 
B301: 00              BRK                         
B302: C8              INY                         
B303: 16 00           ASL     $00,X               ; {ram.GP_00}
B305: CC 16 00        CPY     $0016               
B308: FD FF 00        SBC     $00FF,X             
B30B: 27 ; ????
B30C: 05 00           ORA     $00                 ; {ram.GP_00}
B30E: 9A              TXS                         
B30F: 0D 02 AB        ORA     $AB02               ; {}
B312: 0D 02 C0        ORA     $C002               
B315: 12 ; ????
B316: 03 ; ????
B317: C2 ; ????
B318: 16 00           ASL     $00,X               ; {ram.GP_00}
B31A: C6 12           DEC     $12                 
B31C: 03 ; ????
B31D: C9 16           CMP     #$16                
B31F: 00              BRK                         
B320: CD 12 03        CMP     $0312               
B323: CF ; ????
B324: 16 00           ASL     $00,X               ; {ram.GP_00}
B326: FD FF 01        SBC     $01FF,X             
B329: 2C 0D 02        BIT     $020D               
B32C: 3B ; ????
B32D: 0D 02 5A        ORA     $5A02               
B330: 02 ; ????
B331: 01 85           ORA     ($85,X)             
B333: 08              PHP                         
B334: 02 ; ????
B335: 88              DEY                         
B336: 01 01           ORA     ($01,X)             
B338: 95 01           STA     $01,X               
B33A: 01 B3           ORA     ($B3,X)             
B33C: 08              PHP                         
B33D: 02 ; ????
B33E: C0 12           CPY     #$12                
B340: 03 ; ????
B341: C3 ; ????
B342: 04 ; ????
B343: 01 C7           ORA     ($C7,X)             
B345: 04 ; ????
B346: 01 CB           ORA     ($CB,X)             
B348: 12 ; ????
B349: 03 ; ????
B34A: CC 03 01        CPY     $0103               
B34D: CE 02 01        DEC     $0102               
B350: FD FF 01        SBC     $01FF,X             
B353: 27 ; ????
B354: 05 00           ORA     $00                 ; {ram.GP_00}
B356: 84 09           STY     $09                 
B358: 02 ; ????
B359: 94 0A           STY     $0A,X               
B35B: 01 99           ORA     ($99,X)             
B35D: 09 02           ORA     #$02                
B35F: A9 0A           LDA     #$0A                
B361: 01 AD           ORA     ($AD,X)             
B363: 17 ; ????
B364: 03 ; ????
B365: B0 17           BCS     $B37E               ; {}
B367: 03 ; ????
B368: C0 12           CPY     #$12                
B36A: 03 ; ????
B36B: C3 ; ????
B36C: 04 ; ????
B36D: 01 C7           ORA     ($C7,X)             
B36F: 12 ; ????
B370: 03 ; ????
B371: C8              INY                         
B372: 04 ; ????
B373: 01 CC           ORA     ($CC,X)             
B375: 12 ; ????
B376: 03 ; ????
B377: CE 04 01        DEC     $0104               
B37A: FD FF 01        SBC     $01FF,X             
B37D: 2A              ROL     A                   
B37E: 17 ; ????
B37F: 03 ; ????
B380: 36 09           ROL     $09,X               
B382: 02 ; ????
B383: 46 0A           LSR     $0A                 
B385: 01 6E           ORA     ($6E,X)             
B387: 09 02           ORA     #$02                
B389: 76 02           ROR     $02,X               
B38B: 01 7E           ORA     ($7E,X)             
B38D: 0A              ASL     A                   
B38E: 01 84           ORA     ($84,X)             
B390: 01 01           ORA     ($01,X)             
B392: 9E ; ????
B393: 13 ; ????
B394: 01 AA           ORA     ($AA,X)             
B396: 01 01           ORA     ($01,X)             
B398: AE 01 01        LDX     $0101               
B39B: B1 01           LDA     ($01),Y             
B39D: 01 C0           ORA     ($C0,X)             
B39F: 12 ; ????
B3A0: 03 ; ????
B3A1: C4 12           CPY     $12                 
B3A3: 03 ; ????
B3A4: C8              INY                         
B3A5: 12 ; ????
B3A6: 03 ; ????
B3A7: CC 12 03        CPY     $0312               
B3AA: FD FF 03        SBC     $03FF,X             
B3AD: 17 ; ????
B3AE: 05 00           ORA     $00                 ; {ram.GP_00}
B3B0: 67 ; ????
B3B1: 0B ; ????
B3B2: 02 ; ????
B3B3: 82 ; ????
B3B4: 0B ; ????
B3B5: 02 ; ????
B3B6: 86 01           STX     $01                 
B3B8: 01 8D           ORA     ($8D,X)             
B3BA: 0B ; ????
B3BB: 02 ; ????
B3BC: A0 01           LDY     #$01                
B3BE: 01 AB           ORA     ($AB,X)             
B3C0: 01 01           ORA     ($01,X)             
B3C2: C0 12           CPY     #$12                
B3C4: 03 ; ????
B3C5: C4 12           CPY     $12                 
B3C7: 03 ; ????
B3C8: C8              INY                         
B3C9: 12 ; ????
B3CA: 03 ; ????
B3CB: CC 12 03        CPY     $0312               
B3CE: FD FF 01        SBC     $01FF,X             
B3D1: 28              PLP                         
B3D2: 05 00           ORA     $00                 ; {ram.GP_00}
B3D4: 92 ; ????
B3D5: 13 ; ????
B3D6: 01 96           ORA     ($96,X)             
B3D8: 13 ; ????
B3D9: 01 A8           ORA     ($A8,X)             
B3DB: 18              CLC                         
B3DC: 01 BC           ORA     ($BC,X)             
B3DE: 18              CLC                         
B3DF: 01 C0           ORA     ($C0,X)             
B3E1: 12 ; ????
B3E2: 03 ; ????
B3E3: C4 12           CPY     $12                 
B3E5: 03 ; ????
B3E6: C8              INY                         
B3E7: 12 ; ????
B3E8: 03 ; ????
B3E9: CC 12 03        CPY     $0312               
B3EC: FD FF 01        SBC     $01FF,X             
B3EF: 14 ; ????
B3F0: 05 00           ORA     $00                 ; {ram.GP_00}
B3F2: 2E 0A 01        ROL     $010A               
B3F5: 5D 19 01        EOR     $0119,X             
B3F8: 63 ; ????
B3F9: 0A              ASL     A                   
B3FA: 01 65           ORA     ($65,X)             
B3FC: 18              CLC                         
B3FD: 01 82           ORA     ($82,X)             
B3FF: 18              CLC                         
B400: 01 88           ORA     ($88,X)             
B402: 19 01 8C        ORA     $8C01,Y             ; {}
B405: 18              CLC                         
B406: 01 A4           ORA     ($A4,X)             
B408: 18              CLC                         
B409: 01 B0           ORA     ($B0,X)             
B40B: 18              CLC                         
B40C: 01 B9           ORA     ($B9,X)             
B40E: 18              CLC                         
B40F: 01 C0           ORA     ($C0,X)             
B411: 12 ; ????
B412: 03 ; ????
B413: C4 12           CPY     $12                 
B415: 03 ; ????
B416: C8              INY                         
B417: 12 ; ????
B418: 03 ; ????
B419: CC 12 03        CPY     $0312               
B41C: FD FF 01        SBC     $01FF,X             
B41F: 35 05           AND     $05,X               
B421: 00              BRK                         
B422: 3D 0A 01        AND     $010A,X             
B425: 6B ; ????
B426: 18              CLC                         
B427: 01 91           ORA     ($91,X)             
B429: 17 ; ????
B42A: 01 9A           ORA     ($9A,X)             
B42C: 18              CLC                         
B42D: 01 AC           ORA     ($AC,X)             
B42F: 18              CLC                         
B430: 01 B0           ORA     ($B0,X)             
B432: 18              CLC                         
B433: 01 B7           ORA     ($B7,X)             
B435: 19 01 C0        ORA     $C001,Y             
B438: 12 ; ????
B439: 03 ; ????
B43A: C4 12           CPY     $12                 
B43C: 03 ; ????
B43D: C8              INY                         
B43E: 12 ; ????
B43F: 03 ; ????
B440: CC 12 03        CPY     $0312               
B443: FD FF 01        SBC     $01FF,X             
B446: 23 ; ????
B447: 05 00           ORA     $00                 ; {ram.GP_00}
B449: 6D 19 01        ADC     $0119               
B44C: 7A ; ????
B44D: 0B ; ????
B44E: 02 ; ????
B44F: 8A              TXA                         
B450: 02 ; ????
B451: 01 8E           ORA     ($8E,X)             
B453: 19 01 9B        ORA     $9B01,Y             ; {}
B456: 1A ; ????
B457: 01 A2           ORA     ($A2,X)             
B459: 0B ; ????
B45A: 02 ; ????
B45B: A3 ; ????
B45C: 17 ; ????
B45D: 01 B0           ORA     ($B0,X)             
B45F: 18              CLC                         
B460: 01 B4           ORA     ($B4,X)             
B462: 18              CLC                         
B463: 01 B8           ORA     ($B8,X)             
B465: 18              CLC                         
B466: 01 BC           ORA     ($BC,X)             
B468: 18              CLC                         
B469: 01 C0           ORA     ($C0,X)             
B46B: 12 ; ????
B46C: 03 ; ????
B46D: C4 12           CPY     $12                 
B46F: 03 ; ????
B470: C8              INY                         
B471: 12 ; ????
B472: 03 ; ????
B473: CC 12 03        CPY     $0312               
B476: FD FF 01        SBC     $01FF,X             
B479: 41 0A           EOR     ($0A,X)             
B47B: 01 4B           ORA     ($4B,X)             
B47D: 1B ; ????
B47E: 01 54           ORA     ($54,X)             
B480: 1B ; ????
B481: 01 6E           ORA     ($6E,X)             
B483: 1B ; ????
B484: 01 71           ORA     ($71,X)             
B486: 19 01 79        ORA     $7901,Y             
B489: 1B ; ????
B48A: 01 97           ORA     ($97,X)             
B48C: 1B ; ????
B48D: 01 A0           ORA     ($A0,X)             
B48F: 19 01 AB        ORA     $AB01,Y             ; {}
B492: 17 ; ????
B493: 01 B2           ORA     ($B2,X)             
B495: 19 01 C0        ORA     $C001,Y             
B498: 12 ; ????
B499: 03 ; ????
B49A: C4 12           CPY     $12                 
B49C: 03 ; ????
B49D: C8              INY                         
B49E: 12 ; ????
B49F: 03 ; ????
B4A0: CC 12 03        CPY     $0312               
B4A3: FD FF 03        SBC     $03FF,X             
B4A6: 8F ; ????
B4A7: 13 ; ????
B4A8: 01 C0           ORA     ($C0,X)             
B4AA: 12 ; ????
B4AB: 03 ; ????
B4AC: C4 12           CPY     $12                 
B4AE: 03 ; ????
B4AF: C8              INY                         
B4B0: 12 ; ????
B4B1: 03 ; ????
B4B2: CC 12 03        CPY     $0312               
B4B5: FD FF 01        SBC     $01FF,X             
B4B8: 80 ; ????
B4B9: 1B ; ????
B4BA: 01 82           ORA     ($82,X)             
B4BC: 1B ; ????
B4BD: 01 9D           ORA     ($9D,X)             
B4BF: 1A ; ????
B4C0: 01 A1           ORA     ($A1,X)             
B4C2: 17 ; ????
B4C3: 01 B7           ORA     ($B7,X)             
B4C5: 1A ; ????
B4C6: 01 BA           ORA     ($BA,X)             
B4C8: 1A ; ????
B4C9: 01 BD           ORA     ($BD,X)             
B4CB: 1A ; ????
B4CC: 01 C0           ORA     ($C0,X)             
B4CE: 12 ; ????
B4CF: 03 ; ????
B4D0: C4 12           CPY     $12                 
B4D2: 03 ; ????
B4D3: C8              INY                         
B4D4: 12 ; ????
B4D5: 03 ; ????
B4D6: CC 12 03        CPY     $0312               
B4D9: FD FF 01        SBC     $01FF,X             
B4DC: 29 05           AND     #$05                
B4DE: 00              BRK                         
B4DF: A3 ; ????
B4E0: 0B ; ????
B4E1: 02 ; ????
B4E2: A7 ; ????
B4E3: 0B ; ????
B4E4: 02 ; ????
B4E5: AB ; ????
B4E6: 0B ; ????
B4E7: 02 ; ????
B4E8: B0 1A           BCS     $B504               ; {}
B4EA: 01 B3           ORA     ($B3,X)             
B4EC: 1A ; ????
B4ED: 01 B6           ORA     ($B6,X)             
B4EF: 1A ; ????
B4F0: 01 B9           ORA     ($B9,X)             
B4F2: 1A ; ????
B4F3: 01 BC           ORA     ($BC,X)             
B4F5: 1A ; ????
B4F6: 01 C0           ORA     ($C0,X)             
B4F8: 12 ; ????
B4F9: 03 ; ????
B4FA: C4 12           CPY     $12                 
B4FC: 03 ; ????
B4FD: C8              INY                         
B4FE: 12 ; ????
B4FF: 03 ; ????
B500: CC 12 03        CPY     $0312               
B503: FD FF 00        SBC     $00FF,X             
B506: 28              PLP                         
B507: 1D 03 42        ORA     $4203,X             
B50A: 06 00           ASL     $00                 ; {ram.GP_00}
B50C: 50 0E           BVC     $B51C               ; {}
B50E: 00              BRK                         
B50F: 62 ; ????
B510: 06 00           ASL     $00                 ; {ram.GP_00}
B512: 80 ; ????
B513: 0E 00 81        ASL     $8100               ; {}
B516: 0E 00 83        ASL     $8300               ; {}
B519: 06 00           ASL     $00                 ; {ram.GP_00}
B51B: 97 ; ????
B51C: 0B ; ????
B51D: 02 ; ????
B51E: 9B ; ????
B51F: 0B ; ????
B520: 02 ; ????
B521: A2 00           LDX     #$00                
B523: 00              BRK                         
B524: BE 09 02        LDX     $0209,Y             
B527: C0 0F           CPY     #$0F                
B529: 00              BRK                         
B52A: C4 0F           CPY     $0F                 
B52C: 00              BRK                         
B52D: C8              INY                         
B52E: 0F ; ????
B52F: 00              BRK                         
B530: CC 02 01        CPY     $0102               
B533: D0 12           BNE     $B547               ; {}
B535: 03 ; ????
B536: D4 ; ????
B537: 12 ; ????
B538: 03 ; ????
B539: D8              CLD                         
B53A: 02 ; ????
B53B: 01 FD           ORA     ($FD,X)             
B53D: FF ; ????
B53E: 01 13           ORA     ($13,X)             
B540: 1D 03 26        ORA     $2603,X             
B543: 17 ; ????
B544: 01 3D           ORA     ($3D,X)             
B546: 1D 03 7E        ORA     $7E03,X             
B549: 14 ; ????
B54A: 03 ; ????
B54B: 91 0B           STA     ($0B),Y             
B54D: 02 ; ????
B54E: 9A              TXS                         
B54F: 0B ; ????
B550: 02 ; ????
B551: C0 02           CPY     #$02                
B553: 01 C4           ORA     ($C4,X)             
B555: 02 ; ????
B556: 01 C5           ORA     ($C5,X)             
B558: 10 02           BPL     $B55C               ; {}
B55A: C8              INY                         
B55B: 02 ; ????
B55C: 01 CC           ORA     ($CC,X)             
B55E: 02 ; ????
B55F: 01 FD           ORA     ($FD,X)             
B561: FF ; ????
B562: 01 14           ORA     ($14,X)             
B564: 1D 03 3C        ORA     $3C03,X             
B567: 1D 03 88        ORA     $8803,X             ; {}
B56A: 09 02           ORA     #$02                
B56C: 98              TYA                         
B56D: 02 ; ????
B56E: 01 B1           ORA     ($B1,X)             
B570: 13 ; ????
B571: 01 B4           ORA     ($B4,X)             
B573: 09 02           ORA     #$02                
B575: C0 02           CPY     #$02                
B577: 01 C2           ORA     ($C2,X)             
B579: 11 03           ORA     ($03),Y             
B57B: C4 02           CPY     $02                 
B57D: 01 CC           ORA     ($CC,X)             
B57F: 04 ; ????
B580: 01 D8           ORA     ($D8,X)             
B582: 04 ; ????
B583: 01 FD           ORA     ($FD,X)             
B585: FF ; ????
B586: 03 ; ????
B587: 13 ; ????
B588: 1D 03 4C        ORA     $4C03,X             
B58B: 1D 03 94        ORA     $9403,X             ; {}
B58E: 17 ; ????
B58F: 01 98           ORA     ($98,X)             
B591: 03 ; ????
B592: 01 C0           ORA     ($C0,X)             
B594: 02 ; ????
B595: 01 C1           ORA     ($C1,X)             
B597: 11 03           ORA     ($03),Y             
B599: C4 11           CPY     $11                 
B59B: 03 ; ????
B59C: C7 ; ????
B59D: 11 03           ORA     ($03),Y             
B59F: CA              DEX                         
B5A0: 11 03           ORA     ($03),Y             
B5A2: CD 11 03        CMP     $0311               
B5A5: D4 ; ????
B5A6: 04 ; ????
B5A7: 01 D8           ORA     ($D8,X)             
B5A9: 04 ; ????
B5AA: 01 DC           ORA     ($DC,X)             
B5AC: 02 ; ????
B5AD: 01 FD           ORA     ($FD,X)             
B5AF: FF ; ????
B5B0: 01 18           ORA     ($18,X)             
B5B2: 17 ; ????
B5B3: 01 41           ORA     ($41,X)             
B5B5: 01 01           ORA     ($01,X)             
B5B7: 4A              LSR     A                   
B5B8: 01 01           ORA     ($01,X)             
B5BA: 53 ; ????
B5BB: 0C ; ????
B5BC: 02 ; ????
B5BD: 5A ; ????
B5BE: 14 ; ????
B5BF: 03 ; ????
B5C0: 5C ; ????
B5C1: 0C ; ????
B5C2: 02 ; ????
B5C3: 75 01           ADC     $01,X               
B5C5: 01 85           ORA     ($85,X)             
B5C7: 0C ; ????
B5C8: 02 ; ????
B5C9: 88              DEY                         
B5CA: 0C ; ????
B5CB: 02 ; ????
B5CC: 8F ; ????
B5CD: 09 02           ORA     #$02                
B5CF: 90 01           BCC     $B5D2               ; {}
B5D1: 01 9C           ORA     ($9C,X)             
B5D3: 01 01           ORA     ($01,X)             
B5D5: A0 0C           LDY     #$0C                
B5D7: 02 ; ????
B5D8: C0 04           CPY     #$04                
B5DA: 01 C4           ORA     ($C4,X)             
B5DC: 04 ; ????
B5DD: 01 C8           ORA     ($C8,X)             
B5DF: 04 ; ????
B5E0: 01 CC           ORA     ($CC,X)             
B5E2: 04 ; ????
B5E3: 01 FD           ORA     ($FD,X)             
B5E5: FF ; ????
B5E6: 02 ; ????
B5E7: 22 ; ????
B5E8: 17 ; ????
B5E9: 01 4B           ORA     ($4B,X)             
B5EB: 17 ; ????
B5EC: 03 ; ????
B5ED: 7D 0C 02        ADC     $020C,X             
B5F0: 82 ; ????
B5F1: 09 02           ORA     #$02                
B5F3: 92 ; ????
B5F4: 0C ; ????
B5F5: 02 ; ????
B5F6: AB ; ????
B5F7: 09 02           ORA     #$02                
B5F9: BB ; ????
B5FA: 01 01           ORA     ($01,X)             
B5FC: C0 04           CPY     #$04                
B5FE: 00              BRK                         
B5FF: C4 12           CPY     $12                 
B601: 03 ; ????
B602: C8              INY                         
B603: 12 ; ????
B604: 03 ; ????
B605: CC 04 01        CPY     $0104               
B608: FD FF 01        SBC     $01FF,X             
B60B: 2B ; ????
B60C: 1D 03 60        ORA     $6003,X             
B60F: 01 01           ORA     ($01,X)             
B611: 64 ; ????
B612: 10 02           BPL     $B616               ; {}
B614: 69 10           ADC     #$10                
B616: 02 ; ????
B617: 6C 01 01        JMP     ($0101)             
B61A: 6F ; ????
B61B: 14 ; ????
B61C: 03 ; ????
B61D: 74 ; ????
B61E: 01 01           ORA     ($01,X)             
B620: 78              SEI                         
B621: 01 01           ORA     ($01,X)             
B623: 84 0C           STY     $0C                 
B625: 00              BRK                         
B626: 8B ; ????
B627: 0C ; ????
B628: 00              BRK                         
B629: 9E ; ????
B62A: 02 ; ????
B62B: 01 B9           ORA     ($B9,X)             
B62D: 03 ; ????
B62E: 01 C0           ORA     ($C0,X)             
B630: 02 ; ????
B631: 01 C2           ORA     ($C2,X)             
B633: 10 02           BPL     $B637               ; {}
B635: C4 02           CPY     $02                 
B637: 01 C6           ORA     ($C6,X)             
B639: 11 03           ORA     ($03),Y             
B63B: C8              INY                         
B63C: 02 ; ????
B63D: 01 CC           ORA     ($CC,X)             
B63F: 02 ; ????
B640: 01 FD           ORA     ($FD,X)             
B642: FF ; ????
B643: 01 00           ORA     ($00,X)             ; {ram.GP_00}
B645: 02 ; ????
B646: 01 08           ORA     ($08,X)             
B648: 02 ; ????
B649: 01 0C           ORA     ($0C,X)             
B64B: 02 ; ????
B64C: 01 3C           ORA     ($3C,X)             
B64E: 14 ; ????
B64F: 03 ; ????
B650: 48              PHA                         
B651: 1F ; ????
B652: 01 4E           ORA     ($4E,X)             
B654: 0C ; ????
B655: 00              BRK                         
B656: 8E 02 01        STX     $0102               
B659: 92 ; ????
B65A: 0C ; ????
B65B: 00              BRK                         
B65C: A7 ; ????
B65D: 03 ; ????
B65E: 01 B0           ORA     ($B0,X)             
B660: 02 ; ????
B661: 01 B8           ORA     ($B8,X)             
B663: 02 ; ????
B664: 01 BC           ORA     ($BC,X)             
B666: 02 ; ????
B667: 01 C4           ORA     ($C4,X)             
B669: 12 ; ????
B66A: 03 ; ????
B66B: FD FF 01        SBC     $01FF,X             
B66E: 00              BRK                         
B66F: 02 ; ????
B670: 01 03           ORA     ($03,X)             
B672: 02 ; ????
B673: 01 0F           ORA     ($0F,X)             
B675: 02 ; ????
B676: 01 3C           ORA     ($3C,X)             
B678: 10 02           BPL     $B67C               ; {}
B67A: 40              RTI                         
B67B: 1F ; ????
B67C: 01 43           ORA     ($43,X)             
B67E: 02 ; ????
B67F: 01 73           ORA     ($73,X)             
B681: 1F ; ????
B682: 01 75           ORA     ($75,X)             
B684: 0C ; ????
B685: 00              BRK                         
B686: 76 14           ROR     $14,X               
B688: 03 ; ????
B689: A9 10           LDA     #$10                
B68B: 02 ; ????
B68C: B0 02           BCS     $B690               ; {}
B68E: 01 B4           ORA     ($B4,X)             
B690: 02 ; ????
B691: 01 BF           ORA     ($BF,X)             
B693: 03 ; ????
B694: 01 C7           ORA     ($C7,X)             
B696: 12 ; ????
B697: 03 ; ????
B698: CB ; ????
B699: 12 ; ????
B69A: 03 ; ????
B69B: FD FF 01        SBC     $01FF,X             
B69E: 00              BRK                         
B69F: 02 ; ????
B6A0: 01 28           ORA     ($28,X)             
B6A2: 05 00           ORA     $00                 ; {ram.GP_00}
B6A4: 30 1F           BMI     $B6C5               ; {}
B6A6: 01 4B           ORA     ($4B,X)             
B6A8: 17 ; ????
B6A9: 02 ; ????
B6AA: 85 17           STA     $17                 
B6AC: 03 ; ????
B6AD: 9C ; ????
B6AE: 0D 02 AB        ORA     $AB02               ; {}
B6B1: 0D 02 AE        ORA     $AE02               ; {}
B6B4: 0D 02 B0        ORA     $B002               ; {}
B6B7: 08              PHP                         
B6B8: 02 ; ????
B6B9: BB ; ????
B6BA: 02 ; ????
B6BB: 01 C0           ORA     ($C0,X)             
B6BD: 02 ; ????
B6BE: 01 C4           ORA     ($C4,X)             
B6C0: 02 ; ????
B6C1: 01 C8           ORA     ($C8,X)             
B6C3: 02 ; ????
B6C4: 01 C9           ORA     ($C9,X)             
B6C6: 11 03           ORA     ($03),Y             
B6C8: CE 12 03        DEC     $0312               
B6CB: FD FF 01        SBC     $01FF,X             
B6CE: 33 ; ????
B6CF: 17 ; ????
B6D0: 03 ; ????
B6D1: 5A ; ????
B6D2: 1E 02 69        ASL     $6902,X             
B6D5: 01 01           ORA     ($01,X)             
B6D7: 85 1E           STA     $1E                 
B6D9: 02 ; ????
B6DA: 86 1E           STX     $1E                 
B6DC: 02 ; ????
B6DD: 94 01           STY     $01,X               
B6DF: 01 9D           ORA     ($9D,X)             
B6E1: 1E 02 AB        ASL     $AB02,X             ; {}
B6E4: 02 ; ????
B6E5: 01 B3           ORA     ($B3,X)             
B6E7: 1E 02 B7        ASL     $B702,X             ; {}
B6EA: 1E 02 C0        ASL     $C002,X             
B6ED: 12 ; ????
B6EE: 03 ; ????
B6EF: C2 ; ????
B6F0: 04 ; ????
B6F1: 01 C6           ORA     ($C6,X)             
B6F3: 04 ; ????
B6F4: 01 C9           ORA     ($C9,X)             
B6F6: 11 03           ORA     ($03),Y             
B6F8: CC 04 01        CPY     $0104               
B6FB: DA ; ????
B6FC: 02 ; ????
B6FD: 01 FD           ORA     ($FD,X)             
B6FF: FF ; ????
B700: 01 12           ORA     ($12,X)             
B702: 1D 03 1B        ORA     $1B03,X             
B705: 17 ; ????
B706: 03 ; ????
B707: 42 ; ????
B708: 17 ; ????
B709: 03 ; ????
B70A: 8B ; ????
B70B: 03 ; ????
B70C: 01 96           ORA     ($96,X)             
B70E: 0B ; ????
B70F: 02 ; ????
B710: 99 03 01        STA     $0103,Y             
B713: AE 03 01        LDX     $0103               
B716: C0 02           CPY     #$02                
B718: 01 C1           ORA     ($C1,X)             
B71A: 10 02           BPL     $B71E               ; {}
B71C: C4 02           CPY     $02                 
B71E: 01 C8           ORA     ($C8,X)             
B720: 12 ; ????
B721: 03 ; ????
B722: CC 12 03        CPY     $0312               
B725: FD FF 00        SBC     $00FF,X             
B728: 1C ; ????
B729: 17 ; ????
B72A: 03 ; ????
B72B: 32 ; ????
B72C: 1D 03 4A        ORA     $4A03,X             
B72F: 0B ; ????
B730: 02 ; ????
B731: 58              CLI                         
B732: 0B ; ????
B733: 02 ; ????
B734: 5D 05 00        EOR     $0005,X             
B737: 78              SEI                         
B738: 0C ; ????
B739: 00              BRK                         
B73A: 7A ; ????
B73B: 0C ; ????
B73C: 00              BRK                         
B73D: A2 03           LDX     #$03                
B73F: 01 A4           ORA     ($A4,X)             
B741: 03 ; ????
B742: 01 AE           ORA     ($AE,X)             
B744: 10 02           BPL     $B748               ; {}
B746: B0 03           BCS     $B74B               ; {}
B748: 01 B7           ORA     ($B7,X)             
B74A: 02 ; ????
B74B: 01 BB           ORA     ($BB,X)             
B74D: 0F ; ????
B74E: 00              BRK                         
B74F: BF ; ????
B750: 0F ; ????
B751: 00              BRK                         
B752: C0 12           CPY     #$12                
B754: 03 ; ????
B755: C4 12           CPY     $12                 
B757: 03 ; ????
B758: CA              DEX                         
B759: 10 02           BPL     $B75D               ; {}
B75B: CD 10 02        CMP     $0210               
B75E: FD FF 01        SBC     $01FF,X             
B761: 00              BRK                         
B762: 03 ; ????
B763: 01 01           ORA     ($01,X)             
B765: 01 01           ORA     ($01,X)             
B767: 05 01           ORA     $01                 
B769: 01 09           ORA     ($09,X)             
B76B: 01 01           ORA     ($01,X)             
B76D: 0D 01 01        ORA     $0101               
B770: 0F ; ????
B771: 03 ; ????
B772: 01 31           ORA     ($31,X)             
B774: 21 02           AND     ($02,X)             
B776: 40              RTI                         
B777: 03 ; ????
B778: 01 4E           ORA     ($4E,X)             
B77A: 21 02           AND     ($02,X)             
B77C: 4F ; ????
B77D: 03 ; ????
B77E: 01 61           ORA     ($61,X)             
B780: 15 02           ORA     $02,X               
B782: 7C ; ????
B783: 15 02           ORA     $02,X               
B785: 7E 02 01        ROR     $0102,X             
B788: 80 ; ????
B789: 03 ; ????
B78A: 01 8E           ORA     ($8E,X)             
B78C: 20 00 91        JSR     $9100               ; {}
B78F: 22 ; ????
B790: 02 ; ????
B791: 97 ; ????
B792: 22 ; ????
B793: 02 ; ????
B794: AD 02 01        LDA     $0102               
B797: C0 02           CPY     #$02                
B799: 01 C4           ORA     ($C4,X)             
B79B: 02 ; ????
B79C: 01 C8           ORA     ($C8,X)             
B79E: 02 ; ????
B79F: 01 CC           ORA     ($CC,X)             
B7A1: 02 ; ????
B7A2: 01 FD           ORA     ($FD,X)             
B7A4: FF ; ????
B7A5: 01 10           ORA     ($10,X)             
B7A7: 03 ; ????
B7A8: 01 11           ORA     ($11,X)             
B7AA: 01 01           ORA     ($01,X)             
B7AC: 15 01           ORA     $01,X               
B7AE: 01 19           ORA     ($19,X)             
B7B0: 01 01           ORA     ($01,X)             
B7B2: 1D 01 01        ORA     $0101,X             
B7B5: 2F ; ????
B7B6: 02 ; ????
B7B7: 01 50           ORA     ($50,X)             
B7B9: 03 ; ????
B7BA: 01 6E           ORA     ($6E,X)             
B7BC: 02 ; ????
B7BD: 01 8E           ORA     ($8E,X)             
B7BF: 20 00 90        JSR     $9000               ; {}
B7C2: 03 ; ????
B7C3: 01 AD           ORA     ($AD,X)             
B7C5: 02 ; ????
B7C6: 01 C1           ORA     ($C1,X)             
B7C8: 11 03           ORA     ($03),Y             
B7CA: C4 1A           CPY     $1A                 
B7CC: 01 C7           ORA     ($C7,X)             
B7CE: 1A ; ????
B7CF: 01 CA           ORA     ($CA,X)             
B7D1: 1A ; ????
B7D2: 01 CC           ORA     ($CC,X)             
B7D4: 11 03           ORA     ($03),Y             
B7D6: D0 01           BNE     $B7D9               ; {}
B7D8: 01 FD           ORA     ($FD,X)             
B7DA: FF ; ????
B7DB: 00              BRK                         
B7DC: 52 ; ????
B7DD: 0F ; ????
B7DE: 00              BRK                         
B7DF: 56 0F           LSR     $0F,X               
B7E1: 00              BRK                         
B7E2: 5A ; ????
B7E3: 0F ; ????
B7E4: 00              BRK                         
B7E5: 62 ; ????
B7E6: 06 02           ASL     $02                 
B7E8: 6D 07 02        ADC     $0207               
B7EB: 70 0E           BVS     $B7FB               ; {}
B7ED: 00              BRK                         
B7EE: 7E 0E 00        ROR     $000E,X             
B7F1: 8E 20 01        STX     $0120               
B7F4: A2 02           LDX     #$02                
B7F6: 01 A6           ORA     ($A6,X)             
B7F8: 02 ; ????
B7F9: 01 A7           ORA     ($A7,X)             
B7FB: 1C ; ????
B7FC: 02 ; ????
B7FD: AA              TAX                         
B7FE: 02 ; ????
B7FF: 01 FD           ORA     ($FD,X)             
B801: FF ; ????
B802: 01 60           ORA     ($60,X)             
B804: 01 01           ORA     ($01,X)             
B806: 64 ; ????
B807: 01 01           ORA     ($01,X)             
B809: 68              PLA                         
B80A: 01 01           ORA     ($01,X)             
B80C: 6C 01 01        JMP     ($0101)             
B80F: A0 04           LDY     #$04                
B811: 01 A4           ORA     ($A4,X)             
B813: 04 ; ????
B814: 01 A8           ORA     ($A8,X)             
B816: 04 ; ????
B817: 01 AC           ORA     ($AC,X)             
B819: 04 ; ????
B81A: 01 FD           ORA     ($FD,X)             
B81C: FF ; ????
B81D: 01 51           ORA     ($51,X)             
B81F: 01 52           ORA     ($52,X)             
B821: FF ; ????
B822: 04 ; ????
B823: 53 ; ????
B824: 53 ; ????
B825: 53 ; ????
B826: 53 ; ????
B827: FF ; ????
B828: 04 ; ????
B829: 53 ; ????
B82A: 53 ; ????
B82B: 53 ; ????
B82C: 53 ; ????
B82D: 04 ; ????
B82E: 54 ; ????
B82F: 54 ; ????
B830: 54 ; ????
B831: 54 ; ????
B832: 04 ; ????
B833: 53 ; ????
B834: 53 ; ????
B835: 53 ; ????
B836: 53 ; ????
B837: 04 ; ????
B838: 54 ; ????
B839: 54 ; ????
B83A: 54 ; ????
B83B: 54 ; ????
B83C: FF ; ????
B83D: 01 53           ORA     ($53,X)             
B83F: 01 54           ORA     ($54,X)             
B841: 01 53           ORA     ($53,X)             
B843: 01 54           ORA     ($54,X)             
B845: FF ; ????
B846: 04 ; ????
B847: 53 ; ????
B848: 53 ; ????
B849: 53 ; ????
B84A: 53 ; ????
B84B: 04 ; ????
B84C: 55 55           EOR     $55,X               
B84E: 55 55           EOR     $55,X               
B850: 04 ; ????
B851: 54 ; ????
B852: 54 ; ????
B853: 54 ; ????
B854: 54 ; ????
B855: FF ; ????
B856: 02 ; ????
B857: 09 0A           ORA     #$0A                
B859: FF ; ????
B85A: 01 57           ORA     ($57,X)             
B85C: 01 59           ORA     ($59,X)             
B85E: FF ; ????
B85F: 01 58           ORA     ($58,X)             
B861: 01 5A           ORA     ($5A,X)             
B863: FF ; ????
B864: 04 ; ????
B865: 06 06           ASL     $06                 
B867: 06 06           ASL     $06                 
B869: FF ; ????
B86A: 01 05           ORA     ($05,X)             
B86C: 01 05           ORA     ($05,X)             
B86E: FF ; ????
B86F: 01 08           ORA     ($08,X)             
B871: 01 08           ORA     ($08,X)             
B873: 01 08           ORA     ($08,X)             
B875: FF ; ????
B876: 01 0B           ORA     ($0B,X)             
B878: 01 0C           ORA     ($0C,X)             
B87A: 01 0D           ORA     ($0D,X)             
B87C: FF ; ????
B87D: 01 0D           ORA     ($0D,X)             
B87F: 01 0E           ORA     ($0E,X)             
B881: 01 0E           ORA     ($0E,X)             
B883: 01 0D           ORA     ($0D,X)             
B885: FF ; ????
B886: 01 11           ORA     ($11,X)             
B888: 01 12           ORA     ($12,X)             
B88A: 01 12           ORA     ($12,X)             
B88C: FF ; ????
B88D: 02 ; ????
B88E: 5B ; ????
B88F: 5B ; ????
B890: 02 ; ????
B891: 5B ; ????
B892: 5B ; ????
B893: 02 ; ????
B894: 5B ; ????
B895: 5B ; ????
B896: 02 ; ????
B897: 5B ; ????
B898: 5B ; ????
B899: FF ; ????
B89A: 04 ; ????
B89B: 5C ; ????
B89C: 5C ; ????
B89D: 5C ; ????
B89E: 5C ; ????
B89F: FF ; ????
B8A0: 03 ; ????
B8A1: 31 32           AND     ($32),Y             
B8A3: 31 FF           AND     ($FF),Y             
B8A5: 03 ; ????
B8A6: 30 30           BMI     $B8D8               ; {}
B8A8: 30 FF           BMI     $B8A9               ; {}
B8AA: 04 ; ????
B8AB: 0F ; ????
B8AC: 0F ; ????
B8AD: 0F ; ????
B8AE: 0F ; ????
B8AF: 04 ; ????
B8B0: 10 10           BPL     $B8C2               ; {}
B8B2: 10 10           BPL     $B8C4               ; {}
B8B4: 04 ; ????
B8B5: 10 10           BPL     $B8C7               ; {}
B8B7: 10 10           BPL     $B8C9               ; {}
B8B9: FF ; ????
B8BA: 01 53           ORA     ($53,X)             
B8BC: FF ; ????
B8BD: 01 6F           ORA     ($6F,X)             
B8BF: FF ; ????
B8C0: 02 ; ????
B8C1: 63 ; ????
B8C2: 63 ; ????
B8C3: FF ; ????
B8C4: 04 ; ????
B8C5: 5E 5E 5E        LSR     $5E5E,X             
B8C8: 5E 04 5F        LSR     $5F04,X             
B8CB: 5F ; ????
B8CC: 5F ; ????
B8CD: 5F ; ????
B8CE: 04 ; ????
B8CF: 5F ; ????
B8D0: 5F ; ????
B8D1: 5F ; ????
B8D2: 5F ; ????
B8D3: FF ; ????
B8D4: 03 ; ????
B8D5: 00              BRK                         
B8D6: 14 ; ????
B8D7: 15 04           ORA     $04,X               
B8D9: 14 ; ????
B8DA: 15 00           ORA     $00,X               ; {ram.GP_00}
B8DC: 16 FF           ASL     $FF,X               
B8DE: 04 ; ????
B8DF: 48              PHA                         
B8E0: 49 49           EOR     #$49                
B8E2: 4A              LSR     A                   
B8E3: 04 ; ????
B8E4: 13 ; ????
B8E5: 13 ; ????
B8E6: 13 ; ????
B8E7: 13 ; ????
B8E8: 04 ; ????
B8E9: 13 ; ????
B8EA: 13 ; ????
B8EB: 13 ; ????
B8EC: 13 ; ????
B8ED: 04 ; ????
B8EE: 13 ; ????
B8EF: 13 ; ????
B8F0: 13 ; ????
B8F1: 13 ; ????
B8F2: FF ; ????
B8F3: 02 ; ????
B8F4: 48              PHA                         
B8F5: 4A              LSR     A                   
B8F6: 02 ; ????
B8F7: 13 ; ????
B8F8: 13 ; ????
B8F9: 02 ; ????
B8FA: 13 ; ????
B8FB: 13 ; ????
B8FC: 02 ; ????
B8FD: 13 ; ????
B8FE: 13 ; ????
B8FF: FF ; ????
B900: 03 ; ????
B901: 60              RTS                         
B902: 60              RTS                         
B903: 60              RTS                         
B904: 03 ; ????
B905: 60              RTS                         
B906: 60              RTS                         
B907: 60              RTS                         
B908: FF ; ????
B909: 02 ; ????
B90A: 4B ; ????
B90B: 4C FF 03        JMP     $03FF               
B90E: 38              SEC                         
B90F: 38              SEC                         
B910: 38              SEC                         
B911: FF ; ????
B912: 01 02           ORA     ($02,X)             
B914: FF ; ????
B915: 01 03           ORA     ($03,X)             
B917: FF ; ????
B918: 04 ; ????
B919: 61 62           ADC     ($62,X)             
B91B: 61 61           ADC     ($61,X)             
B91D: FF ; ????
B91E: 01 50           ORA     ($50,X)             
B920: 01 21           ORA     ($21,X)             
B922: FF ; ????
B923: 01 63           ORA     ($63,X)             
B925: FF ; ????
B926: 03 ; ????
B927: 63 ; ????
B928: 63 ; ????
B929: 63 ; ????
B92A: FF ; ????
B92B: 01 50           ORA     ($50,X)             
B92D: 01 29           ORA     ($29,X)             
B92F: FF ; ????
B930: 12 ; ????
B931: 12 ; ????
B932: 12 ; ????
B933: 12 ; ????
B934: 2B ; ????
B935: 12 ; ????
B936: 12 ; ????
B937: 12 ; ????
B938: E3 ; ????
B939: 12 ; ????
B93A: 12 ; ????
B93B: 12 ; ????
B93C: B4 B5           LDY     $B5,X               
B93E: B6 B7           LDX     $B7,Y               
B940: 7B ; ????
B941: 12 ; ????
B942: 12 ; ????
B943: 12 ; ????
B944: C7 ; ????
B945: C8              INY                         
B946: C7 ; ????
B947: C8              INY                         
B948: 12 ; ????
B949: 12 ; ????
B94A: D1 D1           CMP     ($D1),Y             
B94C: 2B ; ????
B94D: 12 ; ????
B94E: 12 ; ????
B94F: 12 ; ????
B950: 89 ; ????
B951: 8A              TXA                         
B952: 89 ; ????
B953: 8A              TXA                         
B954: 97 ; ????
B955: 98              TYA                         
B956: 12 ; ????
B957: 97 ; ????
B958: 99 12 99        STA     $9912,Y             ; {}
B95B: 99 69 6A        STA     $6A69,Y             
B95E: 6B ; ????
B95F: 6C A5 A6        JMP     ($A6A5)             ; {}
B962: A7 ; ????
B963: A8              TAY                         
B964: 8F ; ????
B965: 90 6D           BCC     $B9D4               ; {}
B967: 6E 91 92        ROR     $9291               ; {}
B96A: 91 92           STA     ($92),Y             
B96C: 4D 4D B2        EOR     $B24D               ; {}
B96F: B2 ; ????
B970: B2 ; ????
B971: B2 ; ????
B972: B2 ; ????
B973: B2 ; ????
B974: 70 71           BVS     $B9E7               ; {}
B976: D3 ; ????
B977: D4 ; ????
B978: D3 ; ????
B979: D4 ; ????
B97A: D3 ; ????
B97B: D4 ; ????
B97C: DB ; ????
B97D: DB ; ????
B97E: DB ; ????
B97F: DB ; ????
B980: 12 ; ????
B981: DC ; ????
B982: DC ; ????
B983: DC ; ????
B984: DE 12 DD        DEC     $DD12,X             
B987: DE DE 12        DEC     $12DE,X             
B98A: 12 ; ????
B98B: 12 ; ????
B98C: 7B ; ????
B98D: 12 ; ????
B98E: 12 ; ????
B98F: 12 ; ????
B990: 7B ; ????
B991: 12 ; ????
B992: 12 ; ????
B993: 12 ; ????
B994: 7B ; ????
B995: 12 ; ????
B996: 12 ; ????
B997: 12 ; ????
B998: 7B ; ????
B999: 12 ; ????
B99A: 12 ; ????
B99B: 12 ; ????
B99C: 7B ; ????
B99D: 12 ; ????
B99E: 12 ; ????
B99F: 12 ; ????
B9A0: 7B ; ????
B9A1: 12 ; ????
B9A2: 12 ; ????
B9A3: 12 ; ????
B9A4: 7B ; ????
B9A5: 12 ; ????
B9A6: 12 ; ????
B9A7: 12 ; ????
B9A8: 7B ; ????
B9A9: 12 ; ????
B9AA: 12 ; ????
B9AB: 12 ; ????
B9AC: 7B ; ????
B9AD: 12 ; ????
B9AE: 12 ; ????
B9AF: 12 ; ????
B9B0: 64 ; ????
B9B1: 65 64           ADC     $64                 
B9B3: 65 64           ADC     $64                 
B9B5: 65 64           ADC     $64                 
B9B7: 65 64           ADC     $64                 
B9B9: 65 64           ADC     $64                 
B9BB: 65 64           ADC     $64                 
B9BD: 65 64           ADC     $64                 
B9BF: 65 64           ADC     $64                 
B9C1: 65 64           ADC     $64                 
B9C3: 65 64           ADC     $64                 
B9C5: 65 64           ADC     $64                 
B9C7: 65 64           ADC     $64                 
B9C9: 65 64           ADC     $64                 
B9CB: 65 64           ADC     $64                 
B9CD: 65 64           ADC     $64                 
B9CF: 65 7B           ADC     $7B                 
B9D1: 12 ; ????
B9D2: 12 ; ????
B9D3: 12 ; ????
B9D4: 64 ; ????
B9D5: 65 64           ADC     $64                 
B9D7: 65 7B           ADC     $7B                 
B9D9: 12 ; ????
B9DA: 12 ; ????
B9DB: 12 ; ????
B9DC: 7B ; ????
B9DD: 12 ; ????
B9DE: 12 ; ????
B9DF: 12 ; ????
B9E0: 7B ; ????
B9E1: 12 ; ????
B9E2: 12 ; ????
B9E3: 12 ; ????
B9E4: 7B ; ????
B9E5: 12 ; ????
B9E6: 12 ; ????
B9E7: 12 ; ????
B9E8: 7B ; ????
B9E9: 12 ; ????
B9EA: 12 ; ????
B9EB: 12 ; ????
B9EC: 7B ; ????
B9ED: 12 ; ????
B9EE: 12 ; ????
B9EF: 12 ; ????
B9F0: AA              TAX                         
B9F1: AA              TAX                         
B9F2: AB ; ????
B9F3: AB ; ????
B9F4: C4 C5           CPY     $C5                 
B9F6: E4 E5           CPX     $E5                 
B9F8: C6 E6           DEC     $E6                 
B9FA: E4 B3           CPX     $B3                 
B9FC: 7B ; ????
B9FD: 12 ; ????
B9FE: 12 ; ????
B9FF: 12 ; ????
BA00: 7B ; ????
BA01: 12 ; ????
BA02: 12 ; ????
BA03: 12 ; ????
BA04: 7B ; ????
BA05: 12 ; ????
BA06: 12 ; ????
BA07: 12 ; ????
BA08: 7B ; ????
BA09: 12 ; ????
BA0A: 12 ; ????
BA0B: 12 ; ????
BA0C: 7B ; ????
BA0D: 12 ; ????
BA0E: 12 ; ????
BA0F: 12 ; ????
BA10: 4D 4D B2        EOR     $B24D               ; {}
BA13: B2 ; ????
BA14: 7B ; ????
BA15: 12 ; ????
BA16: 12 ; ????
BA17: 12 ; ????
BA18: 7B ; ????
BA19: 12 ; ????
BA1A: 12 ; ????
BA1B: 12 ; ????
BA1C: 7B ; ????
BA1D: 12 ; ????
BA1E: 12 ; ????
BA1F: 12 ; ????
BA20: 7B ; ????
BA21: 12 ; ????
BA22: 12 ; ????
BA23: 12 ; ????
BA24: 7B ; ????
BA25: 12 ; ????
BA26: 12 ; ????
BA27: 12 ; ????
BA28: 7B ; ????
BA29: 12 ; ????
BA2A: 12 ; ????
BA2B: 12 ; ????
BA2C: 7B ; ????
BA2D: 12 ; ????
BA2E: 12 ; ????
BA2F: 12 ; ????
BA30: 7B ; ????
BA31: 12 ; ????
BA32: 12 ; ????
BA33: 12 ; ????
BA34: 7B ; ????
BA35: 12 ; ????
BA36: 12 ; ????
BA37: 12 ; ????
BA38: 7B ; ????
BA39: 12 ; ????
BA3A: 12 ; ????
BA3B: 12 ; ????
BA3C: 7B ; ????
BA3D: 12 ; ????
BA3E: 12 ; ????
BA3F: 12 ; ????
BA40: 7B ; ????
BA41: 12 ; ????
BA42: 12 ; ????
BA43: 12 ; ????
BA44: 7B ; ????
BA45: 12 ; ????
BA46: 12 ; ????
BA47: 12 ; ????
BA48: 7B ; ????
BA49: 12 ; ????
BA4A: 12 ; ????
BA4B: 12 ; ????
BA4C: 7B ; ????
BA4D: 12 ; ????
BA4E: 12 ; ????
BA4F: 12 ; ????
BA50: D7 ; ????
BA51: D8              CLD                         
BA52: DB ; ????
BA53: DB ; ????
BA54: D8              CLD                         
BA55: D8              CLD                         
BA56: DB ; ????
BA57: DB ; ????
BA58: D8              CLD                         
BA59: D9 DB DB        CMP     $DBDB,Y             
BA5C: D7 ; ????
BA5D: D8              CLD                         
BA5E: DF ; ????
BA5F: E0 D8           CPX     #$D8                
BA61: D9 E1 E2        CMP     $E2E1,Y             
BA64: 7B ; ????
BA65: 12 ; ????
BA66: 12 ; ????
BA67: 12 ; ????
BA68: 7B ; ????
BA69: 12 ; ????
BA6A: 12 ; ????
BA6B: 12 ; ????
BA6C: 7B ; ????
BA6D: 12 ; ????
BA6E: 12 ; ????
BA6F: 12 ; ????
BA70: 60              RTS                         
BA71: 61 64           ADC     ($64,X)             
BA73: 65 60           ADC     $60                 
BA75: 61 62           ADC     ($62,X)             
BA77: 63 ; ????
BA78: 62 ; ????
BA79: 63 ; ????
BA7A: 62 ; ????
BA7B: 63 ; ????
BA7C: C9 CA           CMP     #$CA                
BA7E: CB ; ????
BA7F: CC CA C9        CPY     $C9CA               
BA82: CC CB CD        CPY     $CDCB               
BA85: CE CF D0        DEC     $D0CF               
BA88: 7B ; ????
BA89: 12 ; ????
BA8A: 12 ; ????
BA8B: 12 ; ????
BA8C: 80 ; ????
BA8D: 81 82           STA     ($82,X)             
BA8F: 83 ; ????
BA90: 7C ; ????
BA91: 7D 7E 7F        ADC     $7F7E,X             
BA94: 80 ; ????
BA95: 12 ; ????
BA96: 80 ; ????
BA97: 12 ; ????
BA98: 12 ; ????
BA99: 7D 12 7D        ADC     $7D12,X             
BA9C: 79 79 79        ADC     $7979,Y             
BA9F: 79 79 63        ADC     $6379,Y             
BAA2: 63 ; ????
BAA3: 79 D2 D2        ADC     $D2D2,Y             
BAA6: D2 ; ????
BAA7: D2 ; ????
BAA8: BA              TSX                         
BAA9: BB ; ????
BAAA: BC BD BE        LDY     $BEBD,X             ; {}
BAAD: BF ; ????
BAAE: B8              CLV                         
BAAF: B9 DA DA        LDA     $DADA,Y             
BAB2: DA ; ????
BAB3: DA ; ????
BAB4: A9 AE           LDA     #$AE                
BAB6: AF ; ????
BAB7: 12 ; ????
BAB8: AF ; ????
BAB9: AE 12 12        LDX     $1212               
BABC: 50 51           BVC     $BB0F               ; {}
BABE: 5B ; ????
BABF: 5B ; ????
BAC0: 7B ; ????
BAC1: 12 ; ????
BAC2: 12 ; ????
BAC3: 12 ; ????
BAC4: 7B ; ????
BAC5: 12 ; ????
BAC6: 12 ; ????
BAC7: 12 ; ????
BAC8: 7B ; ????
BAC9: 12 ; ????
BACA: 12 ; ????
BACB: 12 ; ????
BACC: 7B ; ????
BACD: 12 ; ????
BACE: 12 ; ????
BACF: 12 ; ????
BAD0: 7B ; ????
BAD1: 12 ; ????
BAD2: 12 ; ????
BAD3: 12 ; ????
BAD4: 7B ; ????
BAD5: 12 ; ????
BAD6: 12 ; ????
BAD7: 12 ; ????
BAD8: 7B ; ????
BAD9: 12 ; ????
BADA: 12 ; ????
BADB: 12 ; ????
BADC: 7B ; ????
BADD: 12 ; ????
BADE: 12 ; ????
BADF: 12 ; ????
BAE0: 7B ; ????
BAE1: 12 ; ????
BAE2: 12 ; ????
BAE3: 12 ; ????
BAE4: 7B ; ????
BAE5: 12 ; ????
BAE6: 12 ; ????
BAE7: 12 ; ????
BAE8: 7B ; ????
BAE9: 12 ; ????
BAEA: 12 ; ????
BAEB: 12 ; ????
BAEC: A1 A2           LDA     ($A2,X)             
BAEE: A3 ; ????
BAEF: A4 7B           LDY     $7B                 
BAF1: 12 ; ????
BAF2: 12 ; ????
BAF3: 12 ; ????
BAF4: 00              BRK                         
BAF5: 05 F0           ORA     $F0                 
BAF7: 05 00           ORA     $00                 ; {ram.GP_00}
BAF9: 05 F0           ORA     $F0                 
BAFB: 05 00           ORA     $00                 ; {ram.GP_00}
BAFD: 04 ; ????
BAFE: 40              RTI                         
BAFF: 04 ; ????
BB00: 00              BRK                         
BB01: 04 ; ????
BB02: 40              RTI                         
BB03: 04 ; ????
BB04: 2E BB 66        ROL     $66BB               
BB07: BB ; ????
BB08: A4 BB           LDY     $BB                 
BB0A: 02 ; ????
BB0B: B8              CLV                         
BB0C: 60              RTS                         
BB0D: B7 ; ????
BB0E: 02 ; ????
BB0F: B8              CLV                         
BB10: 60              RTS                         
BB11: B7 ; ????
BB12: 02 ; ????
BB13: B8              CLV                         
BB14: A5 B7           LDA     $B7                 
BB16: 02 ; ????
BB17: B8              CLV                         
BB18: A5 B7           LDA     $B7                 
BB1A: 02 ; ????
BB1B: B8              CLV                         
BB1C: A5 B7           LDA     $B7                 
BB1E: 02 ; ????
BB1F: B8              CLV                         
BB20: A5 B7           LDA     $B7                 
BB22: 02 ; ????
BB23: B8              CLV                         
BB24: DB ; ????
BB25: B7 ; ????
BB26: 02 ; ????
BB27: B8              CLV                         
BB28: DB ; ????
BB29: B7 ; ????
BB2A: 02 ; ????
BB2B: B8              CLV                         
BB2C: 02 ; ????
BB2D: B8              CLV                         
BB2E: E5 B0           SBC     $B0                 
BB30: 1B ; ????
BB31: B1 1B           LDA     ($1B),Y             
BB33: B1 3F           LDA     ($3F),Y             
BB35: B1 1B           LDA     ($1B),Y             
BB37: B1 3F           LDA     ($3F),Y             
BB39: B1 3F           LDA     ($3F),Y             
BB3B: B1 63           LDA     ($63),Y             
BB3D: B1 8D           LDA     ($8D),Y             
BB3F: B1 BD           LDA     ($BD),Y             
BB41: B1 8D           LDA     ($8D),Y             
BB43: B1 BD           LDA     ($BD),Y             
BB45: B1 BD           LDA     ($BD),Y             
BB47: B1 D5           LDA     ($D5),Y             
BB49: B1 08           LDA     ($08),Y             
BB4B: B2 ; ????
BB4C: 08              PHP                         
BB4D: B2 ; ????
BB4E: 08              PHP                         
BB4F: B2 ; ????
BB50: D5 B1           CMP     $B1,X               
BB52: 63 ; ????
BB53: B1 1B           LDA     ($1B),Y             
BB55: B1 3E           LDA     ($3E),Y             
BB57: B2 ; ????
BB58: 65 B2           ADC     $B2                 
BB5A: 65 B2           ADC     $B2                 
BB5C: 89 ; ????
BB5D: B2 ; ????
BB5E: B3 ; ????
BB5F: B2 ; ????
BB60: 0A              ASL     A                   
BB61: B3 ; ????
BB62: 3A ; ????
BB63: B0 FF           BCS     $BB64               ; {}
BB65: FF ; ????
BB66: D4 ; ????
BB67: B2 ; ????
BB68: 0A              ASL     A                   
BB69: B3 ; ????
BB6A: 0A              ASL     A                   
BB6B: B3 ; ????
BB6C: 0A              ASL     A                   
BB6D: B3 ; ????
BB6E: 28              PLP                         
BB6F: B3 ; ????
BB70: 52 ; ????
BB71: B3 ; ????
BB72: 52 ; ????
BB73: B3 ; ????
BB74: 7C ; ????
BB75: B3 ; ????
BB76: AC B3 AC        LDY     $ACB3               ; {}
BB79: B3 ; ????
BB7A: AC B3 D0        LDY     $D0B3               
BB7D: B3 ; ????
BB7E: EE B3 1E        INC     $1EB3               
BB81: B4 1E           LDY     $1E,X               
BB83: B4 EE           LDY     $EE,X               
BB85: B3 ; ????
BB86: 45 B4           EOR     $B4                 
BB88: 78              SEI                         
BB89: B4 78           LDY     $78,X               
BB8B: B4 A5           LDY     $A5,X               
BB8D: B4 A5           LDY     $A5,X               
BB8F: B4 A5           LDY     $A5,X               
BB91: B4 78           LDY     $78,X               
BB93: B4 EE           LDY     $EE,X               
BB95: B3 ; ????
BB96: EE B3 A5        INC     $A5B3               ; {}
BB99: B4 B7           LDY     $B7,X               
BB9B: B4 DB           LDY     $DB,X               
BB9D: B4 DB           LDY     $DB,X               
BB9F: B4 70           LDY     $70,X               
BBA1: B0 FF           BCS     $BBA2               ; {}
BBA3: FF ; ????
BBA4: 05 B5           ORA     $B5                 
BBA6: 3E B5 3E        ROL     $3EB5,X             
BBA9: B5 65           LDA     $65,X               
BBAB: B2 ; ????
BBAC: DB ; ????
BBAD: B4 A5           LDY     $A5,X               
BBAF: B4 DB           LDY     $DB,X               
BBB1: B4 62           LDY     $62,X               
BBB3: B5 86           LDA     $86,X               
BBB5: B5 86           LDA     $86,X               
BBB7: B5 62           LDA     $62,X               
BBB9: B5 B0           LDA     $B0,X               
BBBB: B5 B0           LDA     $B0,X               
BBBD: B5 D5           LDA     $D5,X               
BBBF: B1 0A           LDA     ($0A),Y             
BBC1: B6 0A           LDX     $0A,Y               
BBC3: B6 43           LDX     $43,Y               
BBC5: B6 6D           LDX     $6D,Y               
BBC7: B6 6D           LDX     $6D,Y               
BBC9: B6 43           LDX     $43,Y               
BBCB: B6 9D           LDX     $9D,Y               
BBCD: B6 CD           LDX     $CD,Y               
BBCF: B6 CD           LDX     $CD,Y               
BBD1: B6 86           LDX     $86,Y               
BBD3: B5 00           LDA     $00,X               ; {ram.GP_00}
BBD5: B7 ; ????
BBD6: 3E B5 3E        ROL     $3EB5,X             
BBD9: B5 00           LDA     $00,X               ; {ram.GP_00}
BBDB: B7 ; ????
BBDC: 27 ; ????
BBDD: B7 ; ????
BBDE: AC B0 FF        LDY     $FFB0               
BBE1: FF ; ????
BBE2: 1D B8 22        ORA     $22B8,X             
BBE5: B8              CLV                         
BBE6: 28              PLP                         
BBE7: B8              CLV                         
BBE8: 3D B8 46        AND     $46B8,X             
BBEB: B8              CLV                         
BBEC: 56 B8           LSR     $B8,X               
BBEE: 5A ; ????
BBEF: B8              CLV                         
BBF0: 5F ; ????
BBF1: B8              CLV                         
BBF2: 64 ; ????
BBF3: B8              CLV                         
BBF4: 6A              ROR     A                   
BBF5: B8              CLV                         
BBF6: 6F ; ????
BBF7: B8              CLV                         
BBF8: 76 B8           ROR     $B8,X               
BBFA: 7D B8 86        ADC     $86B8,X             ; {}
BBFD: B8              CLV                         
BBFE: 8D B8 9A        STA     $9AB8               ; {}
BC01: B8              CLV                         
BC02: A0 B8           LDY     #$B8                
BC04: A5 B8           LDA     $B8                 
BC06: AA              TAX                         
BC07: B8              CLV                         
BC08: BA              TSX                         
BC09: B8              CLV                         
BC0A: BD B8 C0        LDA     $C0B8,X             
BC0D: B8              CLV                         
BC0E: C4 B8           CPY     $B8                 
BC10: D4 ; ????
BC11: B8              CLV                         
BC12: DE B8 F3        DEC     $F3B8,X             
BC15: B8              CLV                         
BC16: 00              BRK                         
BC17: B9 09 B9        LDA     $B909,Y             ; {}
BC1A: 0D B9 12        ORA     $12B9               
BC1D: B9 15 B9        LDA     $B915,Y             ; {}
BC20: 18              CLC                         
BC21: B9 1E B9        LDA     $B91E,Y             ; {}
BC24: 23 ; ????
BC25: B9 26 B9        LDA     $B926,Y             ; {}
BC28: 2B ; ????
BC29: B9 03 00        LDA     $0003,Y             
BC2C: 01 8E           ORA     ($8E,X)             
BC2E: 00              BRK                         
BC2F: 00              BRK                         
BC30: 0D AE 01        ORA     $01AE               
BC33: 00              BRK                         
BC34: 04 ; ????
BC35: 88              DEY                         
BC36: 01 02           ORA     ($02,X)             
BC38: 01 81           ORA     ($81,X)             
BC3A: 01 02           ORA     ($02,X)             
BC3C: 05 35           ORA     $35                 
BC3E: 01 45           ORA     ($45,X)             
BC40: BC 60 BC        LDY     $BC60,X             ; {}
BC43: 7E BC 00        ROR     $00BC,X             
BC46: 00              BRK                         
BC47: 04 ; ????
BC48: 04 ; ????
BC49: 04 ; ????
BC4A: 04 ; ????
BC4B: 00              BRK                         
BC4C: 0A              ASL     A                   
BC4D: 0A              ASL     A                   
BC4E: 08              PHP                         
BC4F: 00              BRK                         
BC50: 04 ; ????
BC51: 04 ; ????
BC52: 0A              ASL     A                   
BC53: 0A              ASL     A                   
BC54: 00              BRK                         
BC55: 05 05           ORA     $05                 
BC57: 00              BRK                         
BC58: 0A              ASL     A                   
BC59: 00              BRK                         
BC5A: 05 00           ORA     $00                 ; {ram.GP_00}
BC5C: 04 ; ????
BC5D: 0A              ASL     A                   
BC5E: 04 ; ????
BC5F: 0A              ASL     A                   
BC60: 00              BRK                         
BC61: 00              BRK                         
BC62: 00              BRK                         
BC63: 00              BRK                         
BC64: 04 ; ????
BC65: 0A              ASL     A                   
BC66: 0A              ASL     A                   
BC67: 00              BRK                         
BC68: 07 ; ????
BC69: 08              PHP                         
BC6A: 00              BRK                         
BC6B: 08              PHP                         
BC6C: 00              BRK                         
BC6D: 08              PHP                         
BC6E: 08              PHP                         
BC6F: 00              BRK                         
BC70: 05 00           ORA     $00                 ; {ram.GP_00}
BC72: 08              PHP                         
BC73: 00              BRK                         
BC74: 00              BRK                         
BC75: 00              BRK                         
BC76: 05 08           ORA     $08                 
BC78: 00              BRK                         
BC79: 00              BRK                         
BC7A: 00              BRK                         
BC7B: 05 0A           ORA     $0A                 
BC7D: 0A              ASL     A                   
BC7E: 00              BRK                         
BC7F: 04 ; ????
BC80: 04 ; ????
BC81: 05 05           ORA     $05                 
BC83: 0A              ASL     A                   
BC84: 0A              ASL     A                   
BC85: 0A              ASL     A                   
BC86: 00              BRK                         
BC87: 07 ; ????
BC88: 08              PHP                         
BC89: 04 ; ????
BC8A: 05 00           ORA     $00                 ; {ram.GP_00}
BC8C: 0A              ASL     A                   
BC8D: 08              PHP                         
BC8E: 0A              ASL     A                   
BC8F: 00              BRK                         
BC90: 00              BRK                         
BC91: 05 00           ORA     $00                 ; {ram.GP_00}
BC93: 07 ; ????
BC94: 00              BRK                         
BC95: 00              BRK                         
BC96: 05 00           ORA     $00                 ; {ram.GP_00}
BC98: 0A              ASL     A                   
BC99: 04 ; ????
BC9A: 05 05           ORA     $05                 
BC9C: A2 BC           LDX     #$BC                
BC9E: BD BC DB        LDA     $DBBC,X             
BCA1: BC 00 00        LDY     $0000,X             ; {ram.GP_00}
BCA4: 00              BRK                         
BCA5: 00              BRK                         
BCA6: 00              BRK                         
BCA7: 00              BRK                         
BCA8: 00              BRK                         
BCA9: 00              BRK                         
BCAA: 00              BRK                         
BCAB: 00              BRK                         
BCAC: 00              BRK                         
BCAD: 00              BRK                         
BCAE: 00              BRK                         
BCAF: 00              BRK                         
BCB0: 00              BRK                         
BCB1: 00              BRK                         
BCB2: 00              BRK                         
BCB3: 00              BRK                         
BCB4: 00              BRK                         
BCB5: 00              BRK                         
BCB6: 00              BRK                         
BCB7: 00              BRK                         
BCB8: 00              BRK                         
BCB9: 00              BRK                         
BCBA: 00              BRK                         
BCBB: 00              BRK                         
BCBC: 00              BRK                         
BCBD: 00              BRK                         
BCBE: 00              BRK                         
BCBF: 00              BRK                         
BCC0: 00              BRK                         
BCC1: 00              BRK                         
BCC2: 00              BRK                         
BCC3: 00              BRK                         
BCC4: 00              BRK                         
BCC5: 00              BRK                         
BCC6: 00              BRK                         
BCC7: 00              BRK                         
BCC8: 00              BRK                         
BCC9: 00              BRK                         
BCCA: 00              BRK                         
BCCB: 00              BRK                         
BCCC: 00              BRK                         
BCCD: 00              BRK                         
BCCE: 00              BRK                         
BCCF: 00              BRK                         
BCD0: 00              BRK                         
BCD1: 00              BRK                         
BCD2: 00              BRK                         
BCD3: 00              BRK                         
BCD4: 00              BRK                         
BCD5: 00              BRK                         
BCD6: 00              BRK                         
BCD7: 00              BRK                         
BCD8: 00              BRK                         
BCD9: 00              BRK                         
BCDA: 00              BRK                         
BCDB: 00              BRK                         
BCDC: 00              BRK                         
BCDD: 00              BRK                         
BCDE: 00              BRK                         
BCDF: 00              BRK                         
BCE0: 00              BRK                         
BCE1: 00              BRK                         
BCE2: 00              BRK                         
BCE3: 00              BRK                         
BCE4: 00              BRK                         
BCE5: 00              BRK                         
BCE6: 00              BRK                         
BCE7: 00              BRK                         
BCE8: 00              BRK                         
BCE9: 00              BRK                         
BCEA: 00              BRK                         
BCEB: 00              BRK                         
BCEC: 00              BRK                         
BCED: 00              BRK                         
BCEE: 00              BRK                         
BCEF: 00              BRK                         
BCF0: 00              BRK                         
BCF1: 00              BRK                         
BCF2: 00              BRK                         
BCF3: 00              BRK                         
BCF4: 00              BRK                         
BCF5: 00              BRK                         
BCF6: 00              BRK                         
BCF7: 00              BRK                         
BCF8: 00              BRK                         
BCF9: FF ; ????
BCFA: BC 1A BD        LDY     $BD1A,X             ; {}
BCFD: 38              SEC                         
BCFE: BD 00 02        LDA     $0200,X             
BD01: 02 ; ????
BD02: 00              BRK                         
BD03: 02 ; ????
BD04: 03 ; ????
BD05: 03 ; ????
BD06: 00              BRK                         
BD07: 02 ; ????
BD08: 02 ; ????
BD09: 02 ; ????
BD0A: 02 ; ????
BD0B: 00              BRK                         
BD0C: 02 ; ????
BD0D: 02 ; ????
BD0E: 02 ; ????
BD0F: 02 ; ????
BD10: 02 ; ????
BD11: 00              BRK                         
BD12: 02 ; ????
BD13: 00              BRK                         
BD14: 03 ; ????
BD15: 03 ; ????
BD16: 00              BRK                         
BD17: 03 ; ????
BD18: 03 ; ????
BD19: 03 ; ????
BD1A: 00              BRK                         
BD1B: 00              BRK                         
BD1C: 00              BRK                         
BD1D: 00              BRK                         
BD1E: 02 ; ????
BD1F: 02 ; ????
BD20: 00              BRK                         
BD21: 00              BRK                         
BD22: 00              BRK                         
BD23: 00              BRK                         
BD24: 00              BRK                         
BD25: 00              BRK                         
BD26: 00              BRK                         
BD27: 09 09           ORA     #$09                
BD29: 09 00           ORA     #$00                
BD2B: 00              BRK                         
BD2C: 00              BRK                         
BD2D: 00              BRK                         
BD2E: 09 00           ORA     #$00                
BD30: 09 09           ORA     #$09                
BD32: 00              BRK                         
BD33: 00              BRK                         
BD34: 09 00           ORA     #$00                
BD36: 00              BRK                         
BD37: 00              BRK                         
BD38: 00              BRK                         
BD39: 02 ; ????
BD3A: 02 ; ????
BD3B: 00              BRK                         
BD3C: 00              BRK                         
BD3D: 00              BRK                         
BD3E: 09 00           ORA     #$00                
BD40: 00              BRK                         
BD41: 09 00           ORA     #$00                
BD43: 02 ; ????
BD44: 02 ; ????
BD45: 02 ; ????
BD46: 02 ; ????
BD47: 02 ; ????
BD48: 02 ; ????
BD49: 02 ; ????
BD4A: 02 ; ????
BD4B: 02 ; ????
BD4C: 09 03           ORA     #$03                
BD4E: 03 ; ????
BD4F: 03 ; ????
BD50: 00              BRK                         
BD51: 02 ; ????
BD52: 02 ; ????
BD53: 03 ; ????
BD54: 09 09           ORA     #$09                
BD56: 5C ; ????
BD57: BD 77 BD        LDA     $BD77,X             ; {}
BD5A: 95 BD           STA     $BD,X               
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
BDB3: 01 13           ORA     ($13,X)             
BDB5: 26 00           ROL     $00                 ; {ram.GP_00}
BDB7: 01 14           ORA     ($14,X)             
BDB9: 76 00           ROR     $00,X               ; {ram.GP_00}
BDBB: 01 15           ORA     ($15,X)             
BDBD: B6 00           LDX     $00,Y               ; {ram.GP_00}
BDBF: 02 ; ????
BDC0: 05 26           ORA     $26                 
BDC2: 00              BRK                         
BDC3: 02 ; ????
BDC4: 08              PHP                         
BDC5: C6 00           DEC     $00                 ; {ram.GP_00}
BDC7: 02 ; ????
BDC8: 12 ; ????
BDC9: B6 00           LDX     $00,Y               ; {ram.GP_00}
BDCB: FF ; ????
BDCC: FF ; ????
BDCD: FF ; ????
BDCE: FF ; ????
BDCF: FF ; ????
BDD0: FF ; ????
BDD1: FF ; ????
BDD2: FF ; ????
BDD3: 01 13           ORA     ($13,X)             
BDD5: 76 00           ROR     $00,X               ; {ram.GP_00}
BDD7: 01 14           ORA     ($14,X)             
BDD9: B6 00           LDX     $00,Y               ; {ram.GP_00}
BDDB: 01 19           ORA     ($19,X)             
BDDD: 26 00           ROL     $00                 ; {ram.GP_00}
BDDF: 02 ; ????
BDE0: 05 76           ORA     $76                 
BDE2: 00              BRK                         
BDE3: 02 ; ????
BDE4: 09 46           ORA     #$46                
BDE6: 00              BRK                         
BDE7: 02 ; ????
BDE8: 17 ; ????
BDE9: 46 00           LSR     $00                 ; {ram.GP_00}
BDEB: FF ; ????
BDEC: FF ; ????
BDED: FF ; ????
BDEE: FF ; ????
BDEF: FF ; ????
BDF0: FF ; ????
BDF1: FF ; ????
BDF2: FF ; ????
BDF3: 01 13           ORA     ($13,X)             
BDF5: B6 00           LDX     $00,Y               ; {ram.GP_00}
BDF7: 01 15           ORA     ($15,X)             
BDF9: 26 00           ROL     $00                 ; {ram.GP_00}
BDFB: 01 19           ORA     ($19,X)             
BDFD: 76 00           ROR     $00,X               ; {ram.GP_00}
BDFF: 02 ; ????
BE00: 05 B6           ORA     $B6                 
BE02: 00              BRK                         
BE03: 02 ; ????
BE04: 09 C6           ORA     #$C6                
BE06: 00              BRK                         
BE07: 02 ; ????
BE08: 17 ; ????
BE09: B6 00           LDX     $00,Y               ; {ram.GP_00}
BE0B: FF ; ????
BE0C: FF ; ????
BE0D: FF ; ????
BE0E: FF ; ????
BE0F: FF ; ????
BE10: FF ; ????
BE11: FF ; ????
BE12: FF ; ????
BE13: 01 14           ORA     ($14,X)             
BE15: 26 00           ROL     $00                 ; {ram.GP_00}
BE17: 01 15           ORA     ($15,X)             
BE19: 76 00           ROR     $00,X               ; {ram.GP_00}
BE1B: 01 19           ORA     ($19,X)             
BE1D: B6 00           LDX     $00,Y               ; {ram.GP_00}
BE1F: 02 ; ????
BE20: 08              PHP                         
BE21: 46 00           LSR     $00                 ; {ram.GP_00}
BE23: 02 ; ????
BE24: 11 B6           ORA     ($B6),Y             
BE26: 00              BRK                         
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
BE33: 1F ; ????
BE34: 3F ; ????
BE35: 5F ; ????
BE36: 02 ; ????
BE37: 30 00           BMI     $BE39               ; {}
BE39: 0F ; ????
BE3A: 02 ; ????
BE3B: 36 17           ROL     $17,X               
BE3D: 0F ; ????
BE3E: 02 ; ????
BE3F: 28              PLP                         
BE40: 27 ; ????
BE41: 1A ; ????
BE42: 02 ; ????
BE43: 21 27           AND     ($27,X)             
BE45: 15 02           ORA     $02,X               
BE47: 20 26 07        JSR     $0726               
BE4A: 02 ; ????
BE4B: 31 11           AND     ($11),Y             
BE4D: 15 02           ORA     $02,X               
BE4F: 00              BRK                         
BE50: 25 3B           AND     $3B                 
BE52: 02 ; ????
BE53: 19 14 37        ORA     $3714,Y             
BE56: 02 ; ????
BE57: 30 00           BMI     $BE59               ; {}
BE59: 0F ; ????
BE5A: 02 ; ????
BE5B: 30 11           BMI     $BE6E               ; {}
BE5D: 0F ; ????
BE5E: 02 ; ????
BE5F: 28              PLP                         
BE60: 15 0F           ORA     $0F,X               
BE62: 02 ; ????
BE63: 21 27           AND     ($27,X)             
BE65: 15 02           ORA     $02,X               
BE67: 20 26 07        JSR     $0726               
BE6A: 02 ; ????
BE6B: 31 0C           AND     ($0C),Y             
BE6D: 16 02           ASL     $02,X               
BE6F: 05 25           ORA     $25                 
BE71: 3B ; ????
BE72: 02 ; ????
BE73: 19 15 39        ORA     $3915,Y             
BE76: 0F ; ????
BE77: 30 03           BMI     $BE7C               ; {}
BE79: 0F ; ????
BE7A: 0F ; ????
BE7B: 10 00           BPL     $BE7D               ; {}
BE7D: 0F ; ????
BE7E: 0F ; ????
BE7F: 28              PLP                         
BE80: 1B ; ????
BE81: 01 0F           ORA     ($0F,X)             
BE83: 21 27           AND     ($27,X)             
BE85: 15 0F           ORA     $0F,X               
BE87: 20 26 07        JSR     $0726               
BE8A: 0F ; ????
BE8B: 30 11           BMI     $BE9E               ; {}
BE8D: 15 0F           ORA     $0F,X               
BE8F: 11 25           ORA     ($25),Y             
BE91: 3B ; ????
BE92: 0F ; ????
BE93: 1A ; ????
BE94: 25 37           AND     $37                 
BE96: 01 02           ORA     ($02,X)             
BE98: 01 01           ORA     ($01,X)             
BE9A: 02 ; ????
BE9B: 03 ; ????
BE9C: 01 00           ORA     ($00,X)             ; {ram.GP_00}
BE9E: 02 ; ????
BE9F: 0A              ASL     A                   
BEA0: 02 ; ????
BEA1: 01 01           ORA     ($01,X)             
BEA3: 0A              ASL     A                   
BEA4: 01 01           ORA     ($01,X)             
BEA6: 01 01           ORA     ($01,X)             
BEA8: 03 ; ????
BEA9: 05 03           ORA     $03                 
BEAB: 01 00           ORA     ($00,X)             ; {ram.GP_00}
BEAD: 03 ; ????
BEAE: 05 03           ORA     $03                 
BEB0: 01 01           ORA     ($01,X)             
BEB2: 05 01           ORA     $01                 
BEB4: 01 02           ORA     ($02,X)             
BEB6: 01 01           ORA     ($01,X)             
BEB8: 03 ; ????
BEB9: 01 01           ORA     ($01,X)             
BEBB: 00              BRK                         
BEBC: 01 03           ORA     ($03,X)             
BEBE: 01 01           ORA     ($01,X)             
BEC0: 01 02           ORA     ($02,X)             
BEC2: 01 FF           ORA     ($FF,X)             
BEC4: FF ; ????
BEC5: FF ; ????
BEC6: F7 ; ????
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
BEF6: DF ; ????
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
BFF9: 00              BRK                         
BFFA: 00              BRK                         
BFFB: 80 ; ????
BFFC: 00              BRK                         
BFFD: 00              BRK                         
BFFE: 00              BRK                         
BFFF: 00              BRK                         
```

