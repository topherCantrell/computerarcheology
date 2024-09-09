![Bank 3](KidIcarus.jpg)

# Bank 3

>>> cpu 6502

>>> binary 8000:roms/KidIcarus.nes[C010:10010]

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](Hardware.md)

```code
8000: 4C 5A 80        JMP     $805A               ; {}
8003: 4C D4 80        JMP     $80D4               ; {}
8006: 4C 66 99        JMP     $9966               ; {}
8009: 4C 40 DF        JMP     $DF40               
800C: 4C A8 96        JMP     $96A8               ; {}
800F: 4C D3 96        JMP     $96D3               ; {}
8012: 4C 2B 96        JMP     $962B               ; {}
8015: 4C 39 81        JMP     $8139               ; {}
8018: 4C DF 9B        JMP     $9BDF               ; {}
801B: 4C 76 85        JMP     $8576               ; {}
801E: 4C 39 81        JMP     $8139               ; {}
8021: 4C 11 96        JMP     $9611               ; {}
8024: 4C 8E 80        JMP     $808E               ; {}
8027: 4C 97 81        JMP     $8197               ; {}
802A: 4C 64 81        JMP     $8164               ; {}
802D: 4C B9 99        JMP     $99B9               ; {}
8030: 4C 08 9A        JMP     $9A08               ; {}
8033: 4C 04 98        JMP     $9804               ; {}
8036: 4C D5 98        JMP     $98D5               ; {}
8039: 4C B4 97        JMP     $97B4               ; {}
803C: 4C CE 97        JMP     $97CE               ; {}
803F: 4C 5D 85        JMP     $855D               ; {}
8042: 67 ; ????
8043: C5 E7           CMP     $E7                 
8045: C5 AB           CMP     $AB                 
8047: 81 EB           STA     ($EB,X)             
8049: 81 13           STA     ($13,X)             
804B: 82 ; ????
804C: 2B ; ????
804D: 82 ; ????
804E: 4B ; ????
804F: 82 ; ????
8050: 63 ; ????
8051: 82 ; ????
8052: 63 ; ????
8053: 82 ; ????
8054: 53 ; ????
8055: 83 ; ????
8056: 5D F0 59        EOR     $59F0,X             
8059: 79 20 07        ADC     $0720,Y             
805C: EB ; ????
805D: 20 F0 EE        JSR     $EEF0               
8060: 20 E5 EE        JSR     $EEE5               
8063: A9 02           LDA     #$02                
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
8082: 20 64 81        JSR     $8164               ; {}
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
80A4: 20 5F 97        JSR     $975F               ; {}
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
80C5: 20 9B EE        JSR     $EE9B               
80C8: 20 0E EE        JSR     $EE0E               
80CB: 20 B8 EE        JSR     $EEB8               
80CE: 4C 1F 81        JMP     $811F               ; {}
80D1: 4C 35 81        JMP     $8135               ; {}
80D4: 8A              TXA                         
80D5: 48              PHA                         
80D6: 98              TYA                         
80D7: 48              PHA                         
80D8: A5 45           LDA     $45                 
80DA: D0 F5           BNE     $80D1               ; {}
80DC: E6 45           INC     $45                 
80DE: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
80E1: 20 2E EB        JSR     $EB2E               
80E4: A5 38           LDA     $38                 
80E6: D0 DD           BNE     $80C5               ; {}
80E8: A5 37           LDA     $37                 
80EA: D0 4E           BNE     $813A               ; {}
80EC: A9 00           LDA     #$00                
80EE: 8D 01 20        STA     $2001               ; {hard.P_CNTRL_2}
80F1: 20 01 97        JSR     $9701               ; {}
80F4: 20 C9 EB        JSR     $EBC9               
80F7: A5 FF           LDA     $FF                 
80F9: 8D 01 20        STA     $2001               ; {hard.P_CNTRL_2}
80FC: 20 04 98        JSR     $9804               ; {}
80FF: 20 D5 98        JSR     $98D5               ; {}
8102: 20 9B EE        JSR     $EE9B               
8105: 20 76 81        JSR     $8176               ; {}
8108: 20 D9 EC        JSR     $ECD9               
810B: 20 B8 EE        JSR     $EEB8               
810E: 20 87 97        JSR     $9787               ; {}
8111: A5 5C           LDA     $5C                 
8113: 10 0A           BPL     $811F               ; {}
8115: A9 00           LDA     #$00                
8117: 85 3F           STA     $3F                 
8119: 85 40           STA     $40                 
811B: 85 41           STA     $41                 
811D: 85 42           STA     $42                 
811F: 20 5D E1        JSR     $E15D               
8122: 20 E0 C3        JSR     $C3E0               
8125: 20 53 C4        JSR     $C453               
8128: 20 6A EE        JSR     $EE6A               
812B: 20 94 EE        JSR     $EE94               
812E: 20 56 C8        JSR     $C856               
8131: A9 00           LDA     #$00                
8133: 85 45           STA     $45                 
8135: 68              PLA                         
8136: A8              TAY                         
8137: 68              PLA                         
8138: AA              TAX                         
8139: 60              RTS                         
813A: 4A              LSR     A                   
813B: B0 E2           BCS     $811F               ; {}
813D: 4A              LSR     A                   
813E: B0 06           BCS     $8146               ; {}
8140: 20 42 EE        JSR     $EE42               
8143: 4C F4 80        JMP     $80F4               ; {}
8146: A9 0A           LDA     #$0A                
8148: 20 90 CA        JSR     $CA90               
814B: A9 0C           LDA     #$0C                
814D: 20 90 CA        JSR     $CA90               
8150: 20 C9 EB        JSR     $EBC9               
8153: 20 9B EE        JSR     $EE9B               
8156: A9 02           LDA     #$02                
8158: 20 90 CA        JSR     $CA90               
815B: 20 D9 EC        JSR     $ECD9               
815E: 20 B8 EE        JSR     $EEB8               
8161: 4C 1F 81        JMP     $811F               ; {}
8164: 20 97 81        JSR     $8197               ; {}
8167: 20 43 D3        JSR     $D343               
816A: 20 89 94        JSR     $9489               ; {}
816D: 20 56 91        JSR     $9156               ; {}
8170: 20 FE 85        JSR     $85FE               ; {}
8173: 4C 23 84        JMP     $8423               ; {}
8176: 20 B6 CB        JSR     $CBB6               
8179: 20 D9 C3        JSR     $C3D9               
817C: AD 21 07        LDA     $0721               
817F: 29 70           AND     #$70                
8181: D0 B6           BNE     $8139               ; {}
8183: 20 A2 D4        JSR     $D4A2               
8186: 20 8A 94        JSR     $948A               ; {}
8189: 20 57 91        JSR     $9157               ; {}
818C: 20 FF 85        JSR     $85FF               ; {}
818F: 20 31 84        JSR     $8431               ; {}
8192: A2 F0           LDX     #$F0                
8194: 4C 23 94        JMP     $9423               ; {}
8197: A2 20           LDX     #$20                
8199: A9 AA           LDA     #$AA                
819B: 9D 00 07        STA     $0700,X             
819E: A9 80           LDA     #$80                
81A0: 9D 02 07        STA     $0702,X             
81A3: A9 20           LDA     #$20                
81A5: 9D 03 07        STA     $0703,X             
81A8: 4C BF C3        JMP     $C3BF               
81AB: 02 ; ????
81AC: 70 71           BVS     $821F               ; {}
81AE: 72 ; ????
81AF: 73 ; ????
81B0: 74 ; ????
81B1: 75 00           ADC     $00,X               ; {ram.GP_00}
81B3: 42 ; ????
81B4: 71 70           ADC     ($70),Y             
81B6: 73 ; ????
81B7: 72 ; ????
81B8: 75 74           ADC     $74,X               
81BA: 00              BRK                         
81BB: 02 ; ????
81BC: 70 71           BVS     $822F               ; {}
81BE: 72 ; ????
81BF: 73 ; ????
81C0: 76 77           ROR     $77,X               
81C2: 00              BRK                         
81C3: 42 ; ????
81C4: 71 70           ADC     ($70),Y             
81C6: 73 ; ????
81C7: 72 ; ????
81C8: 77 ; ????
81C9: 76 00           ROR     $00,X               ; {ram.GP_00}
81CB: 02 ; ????
81CC: B0 B1           BCS     $817F               ; {}
81CE: B2 ; ????
81CF: B3 ; ????
81D0: B4 B5           LDY     $B5,X               
81D2: 00              BRK                         
81D3: 42 ; ????
81D4: B1 B0           LDA     ($B0),Y             
81D6: B3 ; ????
81D7: B2 ; ????
81D8: B5 B4           LDA     $B4,X               
81DA: 00              BRK                         
81DB: 02 ; ????
81DC: B0 B1           BCS     $818F               ; {}
81DE: B2 ; ????
81DF: B3 ; ????
81E0: B6 B7           LDX     $B7,Y               
81E2: 00              BRK                         
81E3: 42 ; ????
81E4: B1 B0           LDA     ($B0),Y             
81E6: B3 ; ????
81E7: B2 ; ????
81E8: B7 ; ????
81E9: B6 00           LDX     $00,Y               ; {ram.GP_00}
81EB: 4B ; ????
81EC: 4B ; ????
81ED: 4B ; ????
81EE: 4B ; ????
81EF: 5A ; ????
81F0: 5A ; ????
81F1: 5A ; ????
81F2: 5A ; ????
81F3: 4A              LSR     A                   
81F4: 4A              LSR     A                   
81F5: 4A              LSR     A                   
81F6: 4A              LSR     A                   
81F7: 95 5F           STA     $5F,X               
81F9: 96 5F           STX     $5F,Y               
81FB: 9B ; ????
81FC: 5F ; ????
81FD: 9C ; ????
81FE: 5F ; ????
81FF: 3F ; ????
8200: 5F ; ????
8201: 4F ; ????
8202: 5F ; ????
8203: 48              PHA                         
8204: 5F ; ????
8205: 58              CLI                         
8206: 5F ; ????
8207: 49 5F           EOR     #$5F                
8209: 59 5F AA        EOR     $AA5F,Y             ; {}
820C: 5F ; ????
820D: AB ; ????
820E: 5F ; ????
820F: 34 ; ????
8210: 5F ; ????
8211: 55 5F           EOR     $5F,X               
8213: 16 17           ASL     $17,X               
8215: 90 91           BCC     $81A8               ; {}
8217: 17 ; ????
8218: 16 91           ASL     $91,X               
821A: 90 00           BCC     $821C               ; {}
821C: 00              BRK                         
821D: 00              BRK                         
821E: 00              BRK                         
821F: 00              BRK                         
8220: 00              BRK                         
8221: 00              BRK                         
8222: 00              BRK                         
8223: 78              SEI                         
8224: 79 7A 7B        ADC     $7B7A,Y             
8227: 79 78 7B        ADC     $7B78,Y             
822A: 7A ; ????
822B: E0 E1           CPX     #$E1                
822D: E2 ; ????
822E: E3 ; ????
822F: E1 E0           SBC     ($E0,X)             
8231: E3 ; ????
8232: E2 ; ????
8233: E4 E5           CPX     $E5                 
8235: E6 E7           INC     $E7                 
8237: E5 E4           SBC     $E4                 
8239: E7 ; ????
823A: E6 C0           INC     $C0                 
823C: C1 C4           CMP     ($C4,X)             
823E: C5 C1           CMP     $C1                 
8240: C0 C5           CPY     #$C5                
8242: C4 C2           CPY     $C2                 
8244: C3 ; ????
8245: C6 C7           DEC     $C7                 
8247: C3 ; ????
8248: C2 ; ????
8249: C7 ; ????
824A: C6 9F           DEC     $9F                 
824C: 5F ; ????
824D: AF ; ????
824E: 5F ; ????
824F: 8E 5F 8F        STX     $8F5F               ; {}
8252: 5F ; ????
8253: 34 ; ????
8254: 5F ; ????
8255: 8F ; ????
8256: 5F ; ????
8257: DB ; ????
8258: DA ; ????
8259: DF ; ????
825A: DE DA DB        DEC     $DBDA,X             
825D: DE DF D9        DEC     $D9DF,X             
8260: D8              CLD                         
8261: DD DC 7F        CMP     $7FDC,X             
8264: 00              BRK                         
8265: 00              BRK                         
8266: 00              BRK                         
8267: 7F ; ????
8268: 00              BRK                         
8269: 00              BRK                         
826A: 00              BRK                         
826B: 7F ; ????
826C: 00              BRK                         
826D: 00              BRK                         
826E: 00              BRK                         
826F: FC ; ????
8270: 27 ; ????
8271: 01 00           ORA     ($00,X)             ; {ram.GP_00}
8273: F8              SED                         
8274: 94 01           STY     $01,X               
8276: 00              BRK                         
8277: 7F ; ????
8278: 00              BRK                         
8279: 00              BRK                         
827A: 00              BRK                         
827B: 00              BRK                         
827C: AE 01 00        LDX     $0001               
827F: 7F ; ????
8280: 00              BRK                         
8281: 00              BRK                         
8282: 00              BRK                         
8283: F8              SED                         
8284: 5B ; ????
8285: 00              BRK                         
8286: FC ; ????
8287: F8              SED                         
8288: 5B ; ????
8289: 40              RTI                         
828A: 04 ; ????
828B: 00              BRK                         
828C: 5C ; ????
828D: 00              BRK                         
828E: FC ; ????
828F: 00              BRK                         
8290: 5C ; ????
8291: 40              RTI                         
8292: 04 ; ????
8293: F8              SED                         
8294: 0E 00 FC        ASL     $FC00               
8297: F8              SED                         
8298: 0E 40 04        ASL     $0440               
829B: 00              BRK                         
829C: 1E 00 FC        ASL     $FC00,X             
829F: 00              BRK                         
82A0: 1E 40 04        ASL     $0440,X             
82A3: F8              SED                         
82A4: EE 03 FC        INC     $FC03               
82A7: F8              SED                         
82A8: EF ; ????
82A9: 03 ; ????
82AA: 04 ; ????
82AB: 00              BRK                         
82AC: FE 03 FC        INC     $FC03,X             
82AF: 00              BRK                         
82B0: FF ; ????
82B1: 03 ; ????
82B2: 04 ; ????
82B3: F8              SED                         
82B4: EF ; ????
82B5: 43 ; ????
82B6: FC ; ????
82B7: F8              SED                         
82B8: EE 43 04        INC     $0443               
82BB: 00              BRK                         
82BC: FF ; ????
82BD: 43 ; ????
82BE: FC ; ????
82BF: 00              BRK                         
82C0: FE 43 04        INC     $0443,X             
82C3: F8              SED                         
82C4: EE 03 FC        INC     $FC03               
82C7: F8              SED                         
82C8: EF ; ????
82C9: 03 ; ????
82CA: 04 ; ????
82CB: 00              BRK                         
82CC: FF ; ????
82CD: 43 ; ????
82CE: FC ; ????
82CF: 00              BRK                         
82D0: FE 43 04        INC     $0443,X             
82D3: F8              SED                         
82D4: EF ; ????
82D5: 43 ; ????
82D6: FC ; ????
82D7: F8              SED                         
82D8: EE 43 04        INC     $0443               
82DB: 00              BRK                         
82DC: FE 03 FC        INC     $FC03,X             
82DF: 00              BRK                         
82E0: FF ; ????
82E1: 03 ; ????
82E2: 04 ; ????
82E3: 00              BRK                         
82E4: 00              BRK                         
82E5: 00              BRK                         
82E6: 00              BRK                         
82E7: 00              BRK                         
82E8: 00              BRK                         
82E9: 00              BRK                         
82EA: 00              BRK                         
82EB: 00              BRK                         
82EC: 00              BRK                         
82ED: 00              BRK                         
82EE: 00              BRK                         
82EF: 00              BRK                         
82F0: 00              BRK                         
82F1: 00              BRK                         
82F2: 00              BRK                         
82F3: 7F ; ????
82F4: 00              BRK                         
82F5: 00              BRK                         
82F6: 00              BRK                         
82F7: 7F ; ????
82F8: 00              BRK                         
82F9: 00              BRK                         
82FA: 00              BRK                         
82FB: 00              BRK                         
82FC: CA              DEX                         
82FD: 03 ; ????
82FE: FC ; ????
82FF: 00              BRK                         
8300: CA              DEX                         
8301: 43 ; ????
8302: 04 ; ????
8303: 7F ; ????
8304: 00              BRK                         
8305: 00              BRK                         
8306: 00              BRK                         
8307: 7F ; ????
8308: 00              BRK                         
8309: 00              BRK                         
830A: 00              BRK                         
830B: 00              BRK                         
830C: CB ; ????
830D: 03 ; ????
830E: FC ; ????
830F: 00              BRK                         
8310: CB ; ????
8311: 43 ; ????
8312: 04 ; ????
8313: 7F ; ????
8314: 00              BRK                         
8315: 00              BRK                         
8316: 00              BRK                         
8317: 7F ; ????
8318: 00              BRK                         
8319: 00              BRK                         
831A: 00              BRK                         
831B: 00              BRK                         
831C: CB ; ????
831D: 03 ; ????
831E: FC ; ????
831F: 00              BRK                         
8320: CB ; ????
8321: 43 ; ????
8322: 04 ; ????
8323: F8              SED                         
8324: CC 03 FC        CPY     $FC03               
8327: F8              SED                         
8328: CC 43 04        CPY     $0443               
832B: 00              BRK                         
832C: CD 03 FC        CMP     $FC03               
832F: 00              BRK                         
8330: CD 43 04        CMP     $0443               
8333: F8              SED                         
8334: CC 03 FC        CPY     $FC03               
8337: F8              SED                         
8338: CC 43 04        CPY     $0443               
833B: 00              BRK                         
833C: CD 03 FC        CMP     $FC03               
833F: 00              BRK                         
8340: CD 43 04        CMP     $0443               
8343: F8              SED                         
8344: 46 00           LSR     $00                 ; {ram.GP_00}
8346: FC ; ????
8347: F8              SED                         
8348: 47 ; ????
8349: 00              BRK                         
834A: 04 ; ????
834B: 00              BRK                         
834C: 56 00           LSR     $00,X               ; {ram.GP_00}
834E: FC ; ????
834F: 00              BRK                         
8350: 57 ; ????
8351: 00              BRK                         
8352: 04 ; ????
8353: F8              SED                         
8354: BD 02 FC        LDA     $FC02,X             
8357: F8              SED                         
8358: BD 42 04        LDA     $0442,X             
835B: 00              BRK                         
835C: BD 82 FC        LDA     $FC82,X             
835F: 00              BRK                         
8360: BD C2 04        LDA     $04C2,X             
8363: F8              SED                         
8364: BE 02 FC        LDX     $FC02,Y             
8367: F8              SED                         
8368: BE 42 04        LDX     $0442,Y             
836B: 00              BRK                         
836C: BF ; ????
836D: 02 ; ????
836E: FC ; ????
836F: 00              BRK                         
8370: BF ; ????
8371: 42 ; ????
8372: 04 ; ????
8373: F8              SED                         
8374: 2A              ROL     A                   
8375: 02 ; ????
8376: FC ; ????
8377: F8              SED                         
8378: 2A              ROL     A                   
8379: 02 ; ????
837A: 04 ; ????
837B: 00              BRK                         
837C: 2A              ROL     A                   
837D: 82 ; ????
837E: FC ; ????
837F: 00              BRK                         
8380: 2A              ROL     A                   
8381: 82 ; ????
8382: 04 ; ????
8383: F8              SED                         
8384: BF ; ????
8385: 82 ; ????
8386: FC ; ????
8387: F8              SED                         
8388: BF ; ????
8389: C2 ; ????
838A: 04 ; ????
838B: 00              BRK                         
838C: BE 82 FC        LDX     $FC82,Y             
838F: 00              BRK                         
8390: BE C2 04        LDX     $04C2,Y             
8393: F8              SED                         
8394: EA              NOP                         
8395: 02 ; ????
8396: FC ; ????
8397: F8              SED                         
8398: EA              NOP                         
8399: 42 ; ????
839A: 04 ; ????
839B: 00              BRK                         
839C: EC 02 FC        CPX     $FC02               
839F: 00              BRK                         
83A0: EC 42 04        CPX     $0442               
83A3: F8              SED                         
83A4: EB ; ????
83A5: 02 ; ????
83A6: FC ; ????
83A7: F8              SED                         
83A8: EB ; ????
83A9: 42 ; ????
83AA: 04 ; ????
83AB: 00              BRK                         
83AC: ED 02 FC        SBC     $FC02               
83AF: 00              BRK                         
83B0: ED 42 04        SBC     $0442               
83B3: F8              SED                         
83B4: 50 00           BVC     $83B6               ; {}
83B6: FC ; ????
83B7: F8              SED                         
83B8: 50 40           BVC     $83FA               ; {}
83BA: 04 ; ????
83BB: 00              BRK                         
83BC: 51 00           EOR     ($00),Y             ; {ram.GP_00}
83BE: FC ; ????
83BF: 00              BRK                         
83C0: 51 40           EOR     ($40),Y             
83C2: 04 ; ????
83C3: F8              SED                         
83C4: 3E 00 FC        ROL     $FC00,X             
83C7: 7F ; ????
83C8: 00              BRK                         
83C9: 00              BRK                         
83CA: 00              BRK                         
83CB: 00              BRK                         
83CC: 3E 80 FC        ROL     $FC80,X             
83CF: 7F ; ????
83D0: 00              BRK                         
83D1: 00              BRK                         
83D2: 00              BRK                         
83D3: F8              SED                         
83D4: 52 ; ????
83D5: 00              BRK                         
83D6: 04 ; ????
83D7: 7F ; ????
83D8: 00              BRK                         
83D9: 00              BRK                         
83DA: 00              BRK                         
83DB: 00              BRK                         
83DC: 52 ; ????
83DD: 80 ; ????
83DE: 04 ; ????
83DF: 7F ; ????
83E0: 00              BRK                         
83E1: 00              BRK                         
83E2: 00              BRK                         
83E3: F8              SED                         
83E4: 3D 00 FC        AND     $FC00,X             
83E7: F8              SED                         
83E8: 3D 40 03        AND     $0340,X             
83EB: 00              BRK                         
83EC: 4D 00 FC        EOR     $FC00               
83EF: 00              BRK                         
83F0: 4D 40 03        EOR     $0340               
83F3: F8              SED                         
83F4: 92 ; ????
83F5: 01 FD           ORA     ($FD,X)             
83F7: F8              SED                         
83F8: 94 01           STY     $01,X               
83FA: 03 ; ????
83FB: 00              BRK                         
83FC: 93 ; ????
83FD: 01 FD           ORA     ($FD,X)             
83FF: 00              BRK                         
8400: AE 01 03        LDX     $0301               
8403: F8              SED                         
8404: 9A              TXS                         
8405: 01 F4           ORA     ($F4,X)             
8407: F8              SED                         
8408: 9A              TXS                         
8409: 01 FC           ORA     ($FC,X)             
840B: F8              SED                         
840C: 9A              TXS                         
840D: 01 04           ORA     ($04,X)             
840F: F8              SED                         
8410: 9A              TXS                         
8411: 01 0C           ORA     ($0C,X)             
8413: F8              SED                         
8414: 0E 00 FC        ASL     $FC00               
8417: F8              SED                         
8418: 0E 40 04        ASL     $0440               
841B: 00              BRK                         
841C: 5C ; ????
841D: 00              BRK                         
841E: FC ; ????
841F: 00              BRK                         
8420: 5C ; ????
8421: 40              RTI                         
8422: 04 ; ????
8423: A2 50           LDX     #$50                
8425: A9 80           LDA     #$80                
8427: 9D 01 07        STA     $0701,X             
842A: 0A              ASL     A                   
842B: 9D 00 07        STA     $0700,X             
842E: 85 A1           STA     $A1                 
8430: 60              RTS                         
8431: A2 50           LDX     #$50                
8433: BD 01 07        LDA     $0701,X             
8436: 10 16           BPL     $844E               ; {}
8438: 20 E5 85        JSR     $85E5               ; {}
843B: BD 01 07        LDA     $0701,X             
843E: 29 0F           AND     #$0F                
8440: D0 4C           BNE     $848E               ; {}
8442: A5 A1           LDA     $A1                 
8444: CD 2C 79        CMP     $792C               
8447: 90 06           BCC     $844F               ; {}
8449: A9 00           LDA     #$00                
844B: 9D 01 07        STA     $0701,X             
844E: 60              RTS                         
844F: 85 00           STA     $00                 ; {ram.GP_00}
8451: 0A              ASL     A                   
8452: 18              CLC                         
8453: 65 00           ADC     $00                 ; {ram.GP_00}
8455: A8              TAY                         
8456: B9 2D 79        LDA     $792D,Y             
8459: CD 30 01        CMP     $0130               
845C: 90 17           BCC     $8475               ; {}
845E: D0 EE           BNE     $844E               ; {}
8460: B9 2E 79        LDA     $792E,Y             
8463: CD D1 04        CMP     $04D1               
8466: 90 0D           BCC     $8475               ; {}
8468: D0 E4           BNE     $844E               ; {}
846A: B9 2F 79        LDA     $792F,Y             
846D: 29 F0           AND     #$F0                
846F: C5 FD           CMP     $FD                 
8471: F0 06           BEQ     $8479               ; {}
8473: 90 D9           BCC     $844E               ; {}
8475: E6 A1           INC     $A1                 
8477: D0 C9           BNE     $8442               ; {}
8479: A9 00           LDA     #$00                
847B: 9D 00 07        STA     $0700,X             
847E: B9 2F 79        LDA     $792F,Y             
8481: 0A              ASL     A                   
8482: 0A              ASL     A                   
8483: 0A              ASL     A                   
8484: 0A              ASL     A                   
8485: 9D 03 07        STA     $0703,X             
8488: A9 81           LDA     #$81                
848A: 9D 01 07        STA     $0701,X             
848D: 60              RTS                         
848E: BD 00 07        LDA     $0700,X             
8491: C9 F8           CMP     #$F8                
8493: B0 0C           BCS     $84A1               ; {}
8495: 20 8A D9        JSR     $D98A               
8498: 90 03           BCC     $849D               ; {}
849A: 4C A9 84        JMP     $84A9               ; {}
849D: A9 FF           LDA     #$FF                
849F: 85 3E           STA     $3E                 
84A1: A9 80           LDA     #$80                
84A3: 9D 01 07        STA     $0701,X             
84A6: 4C 2B DD        JMP     $DD2B               
84A9: A9 19           LDA     #$19                
84AB: 4C 67 C6        JMP     $C667               
84AE: A9 08           LDA     #$08                
84B0: 9D 00 07        STA     $0700,X             
84B3: A9 44           LDA     #$44                
84B5: 9D 02 07        STA     $0702,X             
84B8: A9 50           LDA     #$50                
84BA: 9D 03 07        STA     $0703,X             
84BD: A9 00           LDA     #$00                
84BF: 9D 04 07        STA     $0704,X             
84C2: 9D 05 07        STA     $0705,X             
84C5: 4C 5D 85        JMP     $855D               ; {}
84C8: A2 F0           LDX     #$F0                
84CA: BD 01 07        LDA     $0701,X             
84CD: 29 F8           AND     #$F8                
84CF: C9 30           CMP     #$30                
84D1: D0 4D           BNE     $8520               ; {}
84D3: BD 01 07        LDA     $0701,X             
84D6: 29 07           AND     #$07                
84D8: 20 2B EE        JSR     $EE2B               
84DB: B9 85 E9        LDA     $E985,Y             
84DE: 84 81           STY     $81                 
84E0: 85 E3           STA     $E3                 
84E2: 84 20           STY     $20                 
84E4: E5 85           SBC     $85                 
84E6: 4C 65 DD        JMP     $DD65               
84E9: 20 08 DD        JSR     $DD08               
84EC: BD 02 07        LDA     $0702,X             
84EF: 29 0F           AND     #$0F                
84F1: C9 08           CMP     #$08                
84F3: B0 56           BCS     $854B               ; {}
84F5: A9 D8           LDA     #$D8                
84F7: 85 08           STA     $08                 
84F9: A9 30           LDA     #$30                
84FB: 85 09           STA     $09                 
84FD: A9 60           LDA     #$60                
84FF: 85 0A           STA     $0A                 
8501: 20 6D C7        JSR     $C76D               
8504: 20 C5 85        JSR     $85C5               ; {}
8507: 20 90 D9        JSR     $D990               
850A: 90 15           BCC     $8521               ; {}
850C: 20 E7 D9        JSR     $D9E7               
850F: 90 15           BCC     $8526               ; {}
8511: 20 09 DA        JSR     $DA09               
8514: 20 62 DF        JSR     $DF62               
8517: 20 C0 DB        JSR     $DBC0               
851A: 20 F1 85        JSR     $85F1               ; {}
851D: 4C DE DC        JMP     $DCDE               
8520: 60              RTS                         
8521: A9 F8           LDA     #$F8                
8523: 99 00 07        STA     $0700,Y             
8526: A9 80           LDA     #$80                
8528: 8D 80 03        STA     $0380               
852B: 20 A9 DC        JSR     $DCA9               
852E: BD 01 07        LDA     $0701,X             
8531: 29 F8           AND     #$F8                
8533: 09 03           ORA     #$03                
8535: 9D 01 07        STA     $0701,X             
8538: A9 FF           LDA     #$FF                
853A: 9D 02 07        STA     $0702,X             
853D: A9 08           LDA     #$08                
853F: 8D 81 03        STA     $0381               
8542: 20 76 85        JSR     $8576               ; {}
8545: 20 E1 E2        JSR     $E2E1               
8548: 4C F0 E2        JMP     $E2F0               
854B: A9 28           LDA     #$28                
854D: 85 08           STA     $08                 
854F: A9 30           LDA     #$30                
8551: 85 09           STA     $09                 
8553: A9 60           LDA     #$60                
8555: 85 0A           STA     $0A                 
8557: 20 8D C7        JSR     $C78D               
855A: 4C 07 85        JMP     $8507               ; {}
855D: 98              TYA                         
855E: 48              PHA                         
855F: BD 01 07        LDA     $0701,X             
8562: 29 F8           AND     #$F8                
8564: 4A              LSR     A                   
8565: 4A              LSR     A                   
8566: 4A              LSR     A                   
8567: A8              TAY                         
8568: B9 39 79        LDA     $7939,Y             
856B: 9D 07 07        STA     $0707,X             
856E: A9 00           LDA     #$00                
8570: 9D 08 07        STA     $0708,X             
8573: 68              PLA                         
8574: A8              TAY                         
8575: 60              RTS                         
8576: BD 01 07        LDA     $0701,X             
8579: 4A              LSR     A                   
857A: 4A              LSR     A                   
857B: 4A              LSR     A                   
857C: A8              TAY                         
857D: B9 49 79        LDA     $7949,Y             
8580: 60              RTS                         
8581: 20 08 DD        JSR     $DD08               
8584: BD 02 07        LDA     $0702,X             
8587: 29 0F           AND     #$0F                
8589: C9 08           CMP     #$08                
858B: B0 16           BCS     $85A3               ; {}
858D: AD 23 07        LDA     $0723               
8590: 18              CLC                         
8591: 69 10           ADC     #$10                
8593: 85 08           STA     $08                 
8595: A9 30           LDA     #$30                
8597: 85 09           STA     $09                 
8599: A9 F8           LDA     #$F8                
859B: 85 0A           STA     $0A                 
859D: 20 6D C7        JSR     $C76D               
85A0: 4C 07 85        JMP     $8507               ; {}
85A3: AD 23 07        LDA     $0723               
85A6: 38              SEC                         
85A7: E9 10           SBC     #$10                
85A9: 85 08           STA     $08                 
85AB: A9 30           LDA     #$30                
85AD: 85 09           STA     $09                 
85AF: A9 F8           LDA     #$F8                
85B1: 85 0A           STA     $0A                 
85B3: 20 8D C7        JSR     $C78D               
85B6: 4C 07 85        JMP     $8507               ; {}
85B9: 8A              TXA                         
85BA: C5 14           CMP     $14                 
85BC: D0 06           BNE     $85C4               ; {}
85BE: 20 AE 84        JSR     $84AE               ; {}
85C1: FE 01 07        INC     $0701,X             
85C4: 60              RTS                         
85C5: A5 15           LDA     $15                 
85C7: 29 01           AND     #$01                
85C9: D0 19           BNE     $85E4               ; {}
85CB: AD 23 07        LDA     $0723               
85CE: 38              SEC                         
85CF: FD 03 07        SBC     $0703,X             
85D2: B0 02           BCS     $85D6               ; {}
85D4: 49 FF           EOR     #$FF                
85D6: C9 08           CMP     #$08                
85D8: B0 0A           BCS     $85E4               ; {}
85DA: BD 01 07        LDA     $0701,X             
85DD: 29 F8           AND     #$F8                
85DF: 09 02           ORA     #$02                
85E1: 9D 01 07        STA     $0701,X             
85E4: 60              RTS                         
85E5: 48              PHA                         
85E6: A5 27           LDA     $27                 
85E8: 18              CLC                         
85E9: 7D 00 07        ADC     $0700,X             
85EC: 9D 00 07        STA     $0700,X             
85EF: 68              PLA                         
85F0: 60              RTS                         
85F1: A0 94           LDY     #$94                
85F3: A5 14           LDA     $14                 
85F5: 29 08           AND     #$08                
85F7: D0 01           BNE     $85FA               ; {}
85F9: C8              INY                         
85FA: 98              TYA                         
85FB: 4C CD C4        JMP     $C4CD               
85FE: 60              RTS                         
85FF: 20 C2 8D        JSR     $8DC2               ; {}
8602: 20 61 86        JSR     $8661               ; {}
8605: AD 61 07        LDA     $0761               
8608: 0D 71 07        ORA     $0771               
860B: 0D 81 07        ORA     $0781               
860E: 0D 91 07        ORA     $0791               
8611: F0 15           BEQ     $8628               ; {}
8613: 20 A5 8E        JSR     $8EA5               ; {}
8616: 20 F1 89        JSR     $89F1               ; {}
8619: 20 02 88        JSR     $8802               ; {}
861C: 20 97 8B        JSR     $8B97               ; {}
861F: 20 98 86        JSR     $8698               ; {}
8622: 20 DB 86        JSR     $86DB               ; {}
8625: 4C 1F 8E        JMP     $8E1F               ; {}
8628: AD 30 01        LDA     $0130               
862B: 0A              ASL     A                   
862C: A8              TAY                         
862D: B9 E1 77        LDA     $77E1,Y             
8630: 85 00           STA     $00                 ; {ram.GP_00}
8632: B9 E2 77        LDA     $77E2,Y             
8635: 85 01           STA     $01                 
8637: AC D1 04        LDY     $04D1               
863A: B1 00           LDA     ($00),Y             ; {ram.GP_00}
863C: C9 0D           CMP     #$0D                
863E: F0 20           BEQ     $8660               ; {}
8640: 0A              ASL     A                   
8641: 0A              ASL     A                   
8642: 0A              ASL     A                   
8643: 20 9D DC        JSR     $DC9D               
8646: 8D 61 07        STA     $0761               
8649: 8D 71 07        STA     $0771               
864C: 8D 81 07        STA     $0781               
864F: 8D 91 07        STA     $0791               
8652: A9 00           LDA     #$00                
8654: 8D 60 07        STA     $0760               
8657: 8D 70 07        STA     $0770               
865A: 8D 80 07        STA     $0780               
865D: 8D 90 07        STA     $0790               
8660: 60              RTS                         
8661: AD 61 07        LDA     $0761               
8664: 29 F8           AND     #$F8                
8666: C9 68           CMP     #$68                
8668: F0 2D           BEQ     $8697               ; {}
866A: AD 30 01        LDA     $0130               
866D: 0A              ASL     A                   
866E: A8              TAY                         
866F: B9 1B 78        LDA     $781B,Y             
8672: 85 00           STA     $00                 ; {ram.GP_00}
8674: B9 1C 78        LDA     $781C,Y             
8677: 85 01           STA     $01                 
8679: AC D1 04        LDY     $04D1               
867C: B1 00           LDA     ($00),Y             ; {ram.GP_00}
867E: F0 17           BEQ     $8697               ; {}
8680: 29 F0           AND     #$F0                
8682: 38              SEC                         
8683: E5 FD           SBC     $FD                 
8685: C9 FC           CMP     #$FC                
8687: 90 0E           BCC     $8697               ; {}
8689: B1 00           LDA     ($00),Y             ; {ram.GP_00}
868B: 0A              ASL     A                   
868C: 0A              ASL     A                   
868D: 0A              ASL     A                   
868E: 0A              ASL     A                   
868F: 8D 63 07        STA     $0763               
8692: A9 68           LDA     #$68                
8694: 8D 61 07        STA     $0761               
8697: 60              RTS                         
8698: A2 60           LDX     #$60                
869A: 20 A9 86        JSR     $86A9               ; {}
869D: A2 70           LDX     #$70                
869F: 20 A9 86        JSR     $86A9               ; {}
86A2: A2 80           LDX     #$80                
86A4: 20 A9 86        JSR     $86A9               ; {}
86A7: A2 90           LDX     #$90                
86A9: BD 01 07        LDA     $0701,X             
86AC: 29 F8           AND     #$F8                
86AE: C9 40           CMP     #$40                
86B0: D0 E5           BNE     $8697               ; {}
86B2: 4C D3 84        JMP     $84D3               ; {}
86B5: A9 02           LDA     #$02                
86B7: 9D 02 07        STA     $0702,X             
86BA: A9 00           LDA     #$00                
86BC: 9D 04 07        STA     $0704,X             
86BF: 9D 05 07        STA     $0705,X             
86C2: A9 80           LDA     #$80                
86C4: 9D 06 07        STA     $0706,X             
86C7: 20 5D 85        JSR     $855D               ; {}
86CA: A9 F0           LDA     #$F0                
86CC: 9D 00 07        STA     $0700,X             
86CF: 8A              TXA                         
86D0: 38              SEC                         
86D1: E9 60           SBC     #$60                
86D3: 0A              ASL     A                   
86D4: 18              CLC                         
86D5: 69 40           ADC     #$40                
86D7: 9D 03 07        STA     $0703,X             
86DA: 60              RTS                         
86DB: A2 60           LDX     #$60                
86DD: 20 EF 86        JSR     $86EF               ; {}
86E0: A2 70           LDX     #$70                
86E2: 20 EF 86        JSR     $86EF               ; {}
86E5: A2 80           LDX     #$80                
86E7: 20 EF 86        JSR     $86EF               ; {}
86EA: A2 90           LDX     #$90                
86EC: 4C EF 86        JMP     $86EF               ; {}
86EF: BD 01 07        LDA     $0701,X             
86F2: 29 F8           AND     #$F8                
86F4: C9 50           CMP     #$50                
86F6: D0 E2           BNE     $86DA               ; {}
86F8: 20 87 E0        JSR     $E087               
86FB: 20 E5 85        JSR     $85E5               ; {}
86FE: 20 0F DD        JSR     $DD0F               
8701: BD 01 07        LDA     $0701,X             
8704: 29 07           AND     #$07                
8706: F0 49           BEQ     $8751               ; {}
8708: C9 01           CMP     #$01                
870A: D0 1F           BNE     $872B               ; {}
870C: 20 90 D9        JSR     $D990               
870F: 90 1D           BCC     $872E               ; {}
8711: 20 E7 D9        JSR     $D9E7               
8714: 90 1D           BCC     $8733               ; {}
8716: 20 09 DA        JSR     $DA09               
8719: 20 62 DF        JSR     $DF62               
871C: 20 AD 87        JSR     $87AD               ; {}
871F: 20 DA DB        JSR     $DBDA               
8722: 20 C9 DB        JSR     $DBC9               
8725: 20 D5 87        JSR     $87D5               ; {}
8728: 4C DE DC        JMP     $DCDE               
872B: 4C 65 DD        JMP     $DD65               
872E: A9 F8           LDA     #$F8                
8730: 99 00 07        STA     $0700,Y             
8733: A9 80           LDA     #$80                
8735: 8D 80 03        STA     $0380               
8738: 20 A9 DC        JSR     $DCA9               
873B: FE 01 07        INC     $0701,X             
873E: A9 FF           LDA     #$FF                
8740: 9D 02 07        STA     $0702,X             
8743: A9 08           LDA     #$08                
8745: 8D 81 03        STA     $0381               
8748: 20 76 85        JSR     $8576               ; {}
874B: 20 E1 E2        JSR     $E2E1               
874E: 4C F0 E2        JMP     $E2F0               
8751: 8A              TXA                         
8752: 4A              LSR     A                   
8753: 4A              LSR     A                   
8754: 18              CLC                         
8755: 65 14           ADC     $14                 
8757: 29 3F           AND     #$3F                
8759: D0 06           BNE     $8761               ; {}
875B: 20 B5 86        JSR     $86B5               ; {}
875E: FE 01 07        INC     $0701,X             
8761: 60              RTS                         
8762: 20 87 D2        JSR     $D287               
8765: D0 0E           BNE     $8775               ; {}
8767: AD D3 04        LDA     $04D3               
876A: C9 40           CMP     #$40                
876C: B0 1A           BCS     $8788               ; {}
876E: AD D4 04        LDA     $04D4               
8771: C9 40           CMP     #$40                
8773: B0 13           BCS     $8788               ; {}
8775: BD 06 07        LDA     $0706,X             
8778: C9 78           CMP     #$78                
877A: B0 03           BCS     $877F               ; {}
877C: 18              CLC                         
877D: 69 02           ADC     #$02                
877F: 9D 06 07        STA     $0706,X             
8782: 29 F0           AND     #$F0                
8784: 9D 05 07        STA     $0705,X             
8787: 60              RTS                         
8788: A9 00           LDA     #$00                
878A: 9D 06 07        STA     $0706,X             
878D: 9D 04 07        STA     $0704,X             
8790: 9D 05 07        STA     $0705,X             
8793: 60              RTS                         
8794: BD 06 07        LDA     $0706,X             
8797: 18              CLC                         
8798: 69 02           ADC     #$02                
879A: 9D 06 07        STA     $0706,X             
879D: C9 F8           CMP     #$F8                
879F: B0 06           BCS     $87A7               ; {}
87A1: 29 F0           AND     #$F0                
87A3: 9D 05 07        STA     $0705,X             
87A6: 60              RTS                         
87A7: A9 01           LDA     #$01                
87A9: 9D 06 07        STA     $0706,X             
87AC: 60              RTS                         
87AD: BD 06 07        LDA     $0706,X             
87B0: 30 E2           BMI     $8794               ; {}
87B2: D0 AE           BNE     $8762               ; {}
87B4: 8A              TXA                         
87B5: 38              SEC                         
87B6: E9 60           SBC     #$60                
87B8: 18              CLC                         
87B9: 65 14           ADC     $14                 
87BB: 29 3F           AND     #$3F                
87BD: D0 15           BNE     $87D4               ; {}
87BF: A0 40           LDY     #$40                
87C1: AD 23 07        LDA     $0723               
87C4: DD 03 07        CMP     $0703,X             
87C7: B0 02           BCS     $87CB               ; {}
87C9: A0 B0           LDY     #$B0                
87CB: 98              TYA                         
87CC: 9D 04 07        STA     $0704,X             
87CF: A9 80           LDA     #$80                
87D1: 9D 06 07        STA     $0706,X             
87D4: 60              RTS                         
87D5: A0 50           LDY     #$50                
87D7: BD 04 07        LDA     $0704,X             
87DA: 30 01           BMI     $87DD               ; {}
87DC: C8              INY                         
87DD: A5 14           LDA     $14                 
87DF: 29 08           AND     #$08                
87E1: F0 02           BEQ     $87E5               ; {}
87E3: C8              INY                         
87E4: C8              INY                         
87E5: 98              TYA                         
87E6: 4C CD C4        JMP     $C4CD               
87E9: A9 40           LDA     #$40                
87EB: 9D 02 07        STA     $0702,X             
87EE: A9 80           LDA     #$80                
87F0: 9D 03 07        STA     $0703,X             
87F3: A9 00           LDA     #$00                
87F5: 9D 00 07        STA     $0700,X             
87F8: 9D 04 07        STA     $0704,X             
87FB: 9D 05 07        STA     $0705,X             
87FE: 20 5D 85        JSR     $855D               ; {}
8801: 60              RTS                         
8802: 20 08 88        JSR     $8808               ; {}
8805: 4C D2 88        JMP     $88D2               ; {}
8808: A2 60           LDX     #$60                
880A: BD 01 07        LDA     $0701,X             
880D: 29 F8           AND     #$F8                
880F: C9 58           CMP     #$58                
8811: D0 EE           BNE     $8801               ; {}
8813: 20 E5 85        JSR     $85E5               ; {}
8816: 20 08 DD        JSR     $DD08               
8819: BD 01 07        LDA     $0701,X             
881C: 29 07           AND     #$07                
881E: 20 2B EE        JSR     $EE2B               
8821: 4C 88 27        JMP     $2788               
8824: 88              DEY                         
8825: 56 88           LSR     $88,X               
8827: 20 90 D9        JSR     $D990               
882A: 90 18           BCC     $8844               ; {}
882C: 20 E7 D9        JSR     $D9E7               
882F: 90 18           BCC     $8849               ; {}
8831: 20 09 DA        JSR     $DA09               
8834: 20 62 DF        JSR     $DF62               
8837: 20 59 88        JSR     $8859               ; {}
883A: 20 C0 DB        JSR     $DBC0               
883D: 20 72 88        JSR     $8872               ; {}
8840: 20 DE DC        JSR     $DCDE               
8843: 60              RTS                         
8844: A9 F8           LDA     #$F8                
8846: 99 00 07        STA     $0700,Y             
8849: 4C 5A 92        JMP     $925A               ; {}
884C: 20 E9 87        JSR     $87E9               ; {}
884F: FE 01 07        INC     $0701,X             
8852: 20 80 88        JSR     $8880               ; {}
8855: 60              RTS                         
8856: 4C 65 DD        JMP     $DD65               
8859: A5 14           LDA     $14                 
885B: 29 20           AND     #$20                
885D: D0 06           BNE     $8865               ; {}
885F: A9 20           LDA     #$20                
8861: 9D 02 07        STA     $0702,X             
8864: 60              RTS                         
8865: BD 00 07        LDA     $0700,X             
8868: C9 30           CMP     #$30                
886A: 90 F3           BCC     $885F               ; {}
886C: A9 D0           LDA     #$D0                
886E: 9D 02 07        STA     $0702,X             
8871: 60              RTS                         
8872: A0 54           LDY     #$54                
8874: A5 14           LDA     $14                 
8876: 29 08           AND     #$08                
8878: D0 02           BNE     $887C               ; {}
887A: C8              INY                         
887B: C8              INY                         
887C: 98              TYA                         
887D: 4C CD C4        JMP     $C4CD               
8880: A2 70           LDX     #$70                
8882: A9 09           LDA     #$09                
8884: 20 C3 88        JSR     $88C3               ; {}
8887: A9 7C           LDA     #$7C                
8889: 9D 04 07        STA     $0704,X             
888C: AD 63 07        LDA     $0763               
888F: 9D 03 07        STA     $0703,X             
8892: 20 5D 85        JSR     $855D               ; {}
8895: A2 80           LDX     #$80                
8897: A9 0A           LDA     #$0A                
8899: 20 C3 88        JSR     $88C3               ; {}
889C: A9 7C           LDA     #$7C                
889E: 9D 04 07        STA     $0704,X             
88A1: AD 63 07        LDA     $0763               
88A4: 9D 03 07        STA     $0703,X             
88A7: 20 5D 85        JSR     $855D               ; {}
88AA: A2 90           LDX     #$90                
88AC: A9 09           LDA     #$09                
88AE: 20 C3 88        JSR     $88C3               ; {}
88B1: A9 FC           LDA     #$FC                
88B3: 9D 04 07        STA     $0704,X             
88B6: AD 63 07        LDA     $0763               
88B9: 18              CLC                         
88BA: 69 20           ADC     #$20                
88BC: 9D 03 07        STA     $0703,X             
88BF: 4C 5D 85        JMP     $855D               ; {}
88C2: 60              RTS                         
88C3: 9D 01 07        STA     $0701,X             
88C6: A9 00           LDA     #$00                
88C8: 9D 00 07        STA     $0700,X             
88CB: 9D 02 07        STA     $0702,X             
88CE: 9D 05 07        STA     $0705,X             
88D1: 60              RTS                         
88D2: A2 70           LDX     #$70                
88D4: 20 E1 88        JSR     $88E1               ; {}
88D7: A2 80           LDX     #$80                
88D9: 20 E1 88        JSR     $88E1               ; {}
88DC: A2 90           LDX     #$90                
88DE: 4C E1 88        JMP     $88E1               ; {}
88E1: BD 01 07        LDA     $0701,X             
88E4: 29 F8           AND     #$F8                
88E6: C9 08           CMP     #$08                
88E8: D0 41           BNE     $892B               ; {}
88EA: 20 E5 85        JSR     $85E5               ; {}
88ED: BD 01 07        LDA     $0701,X             
88F0: 29 07           AND     #$07                
88F2: 20 2B EE        JSR     $EE2B               
88F5: 0C ; ????
88F6: 89 ; ????
88F7: 4C 89 52        JMP     $5289               
88FA: 89 ; ????
88FB: 58              CLI                         
88FC: 89 ; ????
88FD: 49 89           EOR     #$89                
88FF: BD 00 07        LDA     $0700,X             
8902: C9 F8           CMP     #$F8                
8904: 90 05           BCC     $890B               ; {}
8906: 20 2F DF        JSR     $DF2F               
8909: 68              PLA                         
890A: 68              PLA                         
890B: 60              RTS                         
890C: 20 66 89        JSR     $8966               ; {}
890F: 20 90 D9        JSR     $D990               
8912: 90 18           BCC     $892C               ; {}
8914: 20 E7 D9        JSR     $D9E7               
8917: 90 18           BCC     $8931               ; {}
8919: 20 09 DA        JSR     $DA09               
891C: 20 65 DF        JSR     $DF65               
891F: 20 FF 88        JSR     $88FF               ; {}
8922: 20 C9 DB        JSR     $DBC9               
8925: 20 BB 89        JSR     $89BB               ; {}
8928: 20 DE DC        JSR     $DCDE               
892B: 60              RTS                         
892C: A9 F8           LDA     #$F8                
892E: 99 00 07        STA     $0700,Y             
8931: 20 A9 DC        JSR     $DCA9               
8934: BD 01 07        LDA     $0701,X             
8937: 29 F8           AND     #$F8                
8939: 09 04           ORA     #$04                
893B: 9D 01 07        STA     $0701,X             
893E: A9 FF           LDA     #$FF                
8940: 9D 02 07        STA     $0702,X             
8943: A9 08           LDA     #$08                
8945: 8D 81 03        STA     $0381               
8948: 60              RTS                         
8949: 4C B2 DE        JMP     $DEB2               
894C: 20 7D 89        JSR     $897D               ; {}
894F: 4C 0F 89        JMP     $890F               ; {}
8952: 20 8E 89        JSR     $898E               ; {}
8955: 4C 0F 89        JMP     $890F               ; {}
8958: 20 9F 89        JSR     $899F               ; {}
895B: 4C 0F 89        JMP     $890F               ; {}
895E: 18              CLC                         
895F: 7D 04 07        ADC     $0704,X             
8962: 9D 04 07        STA     $0704,X             
8965: 60              RTS                         
8966: AD 60 07        LDA     $0760               
8969: 38              SEC                         
896A: E9 02           SBC     #$02                
896C: 9D 00 07        STA     $0700,X             
896F: A9 FC           LDA     #$FC                
8971: 20 5E 89        JSR     $895E               ; {}
8974: 30 01           BMI     $8977               ; {}
8976: 60              RTS                         
8977: FE 01 07        INC     $0701,X             
897A: 68              PLA                         
897B: 68              PLA                         
897C: 60              RTS                         
897D: AD 60 07        LDA     $0760               
8980: 18              CLC                         
8981: 69 02           ADC     #$02                
8983: 9D 00 07        STA     $0700,X             
8986: A9 FC           LDA     #$FC                
8988: 20 5E 89        JSR     $895E               ; {}
898B: 10 EA           BPL     $8977               ; {}
898D: 60              RTS                         
898E: AD 60 07        LDA     $0760               
8991: 18              CLC                         
8992: 69 02           ADC     #$02                
8994: 9D 00 07        STA     $0700,X             
8997: A9 04           LDA     #$04                
8999: 20 5E 89        JSR     $895E               ; {}
899C: 10 D9           BPL     $8977               ; {}
899E: 60              RTS                         
899F: AD 60 07        LDA     $0760               
89A2: 38              SEC                         
89A3: E9 02           SBC     #$02                
89A5: 9D 00 07        STA     $0700,X             
89A8: A9 04           LDA     #$04                
89AA: 20 5E 89        JSR     $895E               ; {}
89AD: 30 01           BMI     $89B0               ; {}
89AF: 60              RTS                         
89B0: BD 01 07        LDA     $0701,X             
89B3: 29 F8           AND     #$F8                
89B5: 9D 01 07        STA     $0701,X             
89B8: 68              PLA                         
89B9: 68              PLA                         
89BA: 60              RTS                         
89BB: BD 00 07        LDA     $0700,X             
89BE: 9D 00 02        STA     $0200,X             
89C1: BD 03 07        LDA     $0703,X             
89C4: 9D 03 02        STA     $0203,X             
89C7: A9 02           LDA     #$02                
89C9: 9D 02 02        STA     $0202,X             
89CC: A0 C8           LDY     #$C8                
89CE: A5 14           LDA     $14                 
89D0: 29 08           AND     #$08                
89D2: D0 01           BNE     $89D5               ; {}
89D4: C8              INY                         
89D5: 98              TYA                         
89D6: 9D 01 02        STA     $0201,X             
89D9: 60              RTS                         
89DA: A9 02           LDA     #$02                
89DC: 9D 02 07        STA     $0702,X             
89DF: 4C 5D 85        JMP     $855D               ; {}
89E2: A9 00           LDA     #$00                
89E4: 9D 00 07        STA     $0700,X             
89E7: A5 14           LDA     $14                 
89E9: 0A              ASL     A                   
89EA: 0A              ASL     A                   
89EB: 0A              ASL     A                   
89EC: 0A              ASL     A                   
89ED: 9D 03 07        STA     $0703,X             
89F0: 60              RTS                         
89F1: A2 60           LDX     #$60                
89F3: 20 02 8A        JSR     $8A02               ; {}
89F6: A2 70           LDX     #$70                
89F8: 20 02 8A        JSR     $8A02               ; {}
89FB: A2 80           LDX     #$80                
89FD: 20 02 8A        JSR     $8A02               ; {}
8A00: A2 90           LDX     #$90                
8A02: BD 01 07        LDA     $0701,X             
8A05: 29 F8           AND     #$F8                
8A07: C9 38           CMP     #$38                
8A09: D0 3E           BNE     $8A49               ; {}
8A0B: 20 E5 85        JSR     $85E5               ; {}
8A0E: 20 08 DD        JSR     $DD08               
8A11: BD 01 07        LDA     $0701,X             
8A14: 29 07           AND     #$07                
8A16: 20 2B EE        JSR     $EE2B               
8A19: BB ; ????
8A1A: 8A              TXA                         
8A1B: 21 8A           AND     ($8A,X)             
8A1D: 21 8A           AND     ($8A,X)             
8A1F: B8              CLV                         
8A20: 8A              TXA                         
8A21: 20 87 E0        JSR     $E087               
8A24: 20 90 D9        JSR     $D990               
8A27: 90 21           BCC     $8A4A               ; {}
8A29: 20 E7 D9        JSR     $D9E7               
8A2C: 90 21           BCC     $8A4F               ; {}
8A2E: A0 20           LDY     #$20                
8A30: 20 86 D9        JSR     $D986               
8A33: B0 03           BCS     $8A38               ; {}
8A35: 20 52 8A        JSR     $8A52               ; {}
8A38: 20 83 8A        JSR     $8A83               ; {}
8A3B: D0 03           BNE     $8A40               ; {}
8A3D: 20 F8 8A        JSR     $8AF8               ; {}
8A40: 20 C0 DB        JSR     $DBC0               
8A43: 20 89 8B        JSR     $8B89               ; {}
8A46: 20 DE DC        JSR     $DCDE               
8A49: 60              RTS                         
8A4A: A9 F8           LDA     #$F8                
8A4C: 99 00 07        STA     $0700,Y             
8A4F: 60              RTS                         
8A50: A9 80           LDA     #$80                
8A52: BD 08 07        LDA     $0708,X             
8A55: D0 1E           BNE     $8A75               ; {}
8A57: A9 7F           LDA     #$7F                
8A59: 9D 08 07        STA     $0708,X             
8A5C: A9 20           LDA     #$20                
8A5E: 8D 81 03        STA     $0381               
8A61: A0 02           LDY     #$02                
8A63: B9 41 01        LDA     $0141,Y             
8A66: 85 00           STA     $00                 ; {ram.GP_00}
8A68: 29 F0           AND     #$F0                
8A6A: D0 06           BNE     $8A72               ; {}
8A6C: A5 00           LDA     $00                 ; {ram.GP_00}
8A6E: 29 0F           AND     #$0F                
8A70: D0 04           BNE     $8A76               ; {}
8A72: 88              DEY                         
8A73: 10 EE           BPL     $8A63               ; {}
8A75: 60              RTS                         
8A76: A8              TAY                         
8A77: 88              DEY                         
8A78: B9 3E 01        LDA     $013E,Y             
8A7B: 29 0F           AND     #$0F                
8A7D: 09 80           ORA     #$80                
8A7F: 99 3E 01        STA     $013E,Y             
8A82: 60              RTS                         
8A83: BD 01 07        LDA     $0701,X             
8A86: 29 07           AND     #$07                
8A88: C9 02           CMP     #$02                
8A8A: B0 11           BCS     $8A9D               ; {}
8A8C: BD 00 07        LDA     $0700,X             
8A8F: 38              SEC                         
8A90: ED 20 07        SBC     $0720               
8A93: 29 F8           AND     #$F8                
8A95: D0 0A           BNE     $8AA1               ; {}
8A97: FE 01 07        INC     $0701,X             
8A9A: 20 A4 8A        JSR     $8AA4               ; {}
8A9D: A9 FF           LDA     #$FF                
8A9F: 60              RTS                         
8AA0: 60              RTS                         
8AA1: A9 00           LDA     #$00                
8AA3: 60              RTS                         
8AA4: BD 03 07        LDA     $0703,X             
8AA7: CD 23 07        CMP     $0723               
8AAA: 90 06           BCC     $8AB2               ; {}
8AAC: A9 0A           LDA     #$0A                
8AAE: 9D 02 07        STA     $0702,X             
8AB1: 60              RTS                         
8AB2: A9 06           LDA     #$06                
8AB4: 9D 02 07        STA     $0702,X             
8AB7: 60              RTS                         
8AB8: 4C 65 DD        JMP     $DD65               
8ABB: 8A              TXA                         
8ABC: 38              SEC                         
8ABD: E9 60           SBC     #$60                
8ABF: 0A              ASL     A                   
8AC0: 0A              ASL     A                   
8AC1: 29 C0           AND     #$C0                
8AC3: 85 00           STA     $00                 ; {ram.GP_00}
8AC5: A5 FD           LDA     $FD                 
8AC7: 29 C0           AND     #$C0                
8AC9: C5 00           CMP     $00                 ; {ram.GP_00}
8ACB: D0 1A           BNE     $8AE7               ; {}
8ACD: 20 E2 89        JSR     $89E2               ; {}
8AD0: 20 87 E0        JSR     $E087               
8AD3: AD D3 04        LDA     $04D3               
8AD6: C9 40           CMP     #$40                
8AD8: 90 0D           BCC     $8AE7               ; {}
8ADA: AD D5 04        LDA     $04D5               
8ADD: C9 40           CMP     #$40                
8ADF: B0 06           BCS     $8AE7               ; {}
8AE1: 20 DA 89        JSR     $89DA               ; {}
8AE4: FE 01 07        INC     $0701,X             
8AE7: 60              RTS                         
8AE8: BD 03 07        LDA     $0703,X             
8AEB: CD 23 07        CMP     $0723               
8AEE: 90 4E           BCC     $8B3E               ; {}
8AF0: B0 75           BCS     $8B67               ; {}
8AF2: A9 50           LDA     #$50                
8AF4: 9D 02 07        STA     $0702,X             
8AF7: 60              RTS                         
8AF8: 20 87 D2        JSR     $D287               
8AFB: D0 F5           BNE     $8AF2               ; {}
8AFD: AD D3 04        LDA     $04D3               
8B00: C9 40           CMP     #$40                
8B02: B0 07           BCS     $8B0B               ; {}
8B04: AD D4 04        LDA     $04D4               
8B07: C9 40           CMP     #$40                
8B09: 90 E7           BCC     $8AF2               ; {}
8B0B: BD 02 07        LDA     $0702,X             
8B0E: 29 0F           AND     #$0F                
8B10: F0 D6           BEQ     $8AE8               ; {}
8B12: A9 00           LDA     #$00                
8B14: 9D 05 07        STA     $0705,X             
8B17: BD 02 07        LDA     $0702,X             
8B1A: 29 0F           AND     #$0F                
8B1C: C9 08           CMP     #$08                
8B1E: B0 29           BCS     $8B49               ; {}
8B20: BD 03 07        LDA     $0703,X             
8B23: C9 F0           CMP     #$F0                
8B25: B0 40           BCS     $8B67               ; {}
8B27: AD D3 04        LDA     $04D3               
8B2A: C9 40           CMP     #$40                
8B2C: 90 39           BCC     $8B67               ; {}
8B2E: AD D5 04        LDA     $04D5               
8B31: C9 40           CMP     #$40                
8B33: B0 32           BCS     $8B67               ; {}
8B35: BD 02 07        LDA     $0702,X             
8B38: 29 0F           AND     #$0F                
8B3A: 9D 02 07        STA     $0702,X             
8B3D: 60              RTS                         
8B3E: A9 02           LDA     #$02                
8B40: 9D 02 07        STA     $0702,X             
8B43: A9 00           LDA     #$00                
8B45: 9D 04 07        STA     $0704,X             
8B48: 60              RTS                         
8B49: BD 03 07        LDA     $0703,X             
8B4C: C9 08           CMP     #$08                
8B4E: 90 EE           BCC     $8B3E               ; {}
8B50: AD D4 04        LDA     $04D4               
8B53: C9 40           CMP     #$40                
8B55: 90 E7           BCC     $8B3E               ; {}
8B57: AD D6 04        LDA     $04D6               
8B5A: C9 40           CMP     #$40                
8B5C: B0 E0           BCS     $8B3E               ; {}
8B5E: BD 02 07        LDA     $0702,X             
8B61: 29 0F           AND     #$0F                
8B63: 9D 02 07        STA     $0702,X             
8B66: 60              RTS                         
8B67: A9 0D           LDA     #$0D                
8B69: 9D 02 07        STA     $0702,X             
8B6C: A9 00           LDA     #$00                
8B6E: 9D 04 07        STA     $0704,X             
8B71: 60              RTS                         
8B72: BD 02 07        LDA     $0702,X             
8B75: 48              PHA                         
8B76: 29 F0           AND     #$F0                
8B78: 9D 05 07        STA     $0705,X             
8B7B: 68              PLA                         
8B7C: 0A              ASL     A                   
8B7D: 0A              ASL     A                   
8B7E: 0A              ASL     A                   
8B7F: 0A              ASL     A                   
8B80: 9D 04 07        STA     $0704,X             
8B83: 20 DA DB        JSR     $DBDA               
8B86: 4C C9 DB        JMP     $DBC9               
8B89: A0 63           LDY     #$63                
8B8B: A5 14           LDA     $14                 
8B8D: 29 08           AND     #$08                
8B8F: D0 02           BNE     $8B93               ; {}
8B91: C8              INY                         
8B92: C8              INY                         
8B93: 98              TYA                         
8B94: 4C CD C4        JMP     $C4CD               
8B97: AD 61 07        LDA     $0761               
8B9A: 29 F8           AND     #$F8                
8B9C: C9 60           CMP     #$60                
8B9E: D0 0E           BNE     $8BAE               ; {}
8BA0: 20 CC 8B        JSR     $8BCC               ; {}
8BA3: 20 A1 8C        JSR     $8CA1               ; {}
8BA6: A9 00           LDA     #$00                
8BA8: 8D 71 07        STA     $0771               
8BAB: 8D 91 07        STA     $0791               
8BAE: 60              RTS                         
8BAF: A9 61           LDA     #$61                
8BB1: 9D 01 07        STA     $0701,X             
8BB4: A9 08           LDA     #$08                
8BB6: 9D 00 07        STA     $0700,X             
8BB9: A9 45           LDA     #$45                
8BBB: 9D 02 07        STA     $0702,X             
8BBE: A9 50           LDA     #$50                
8BC0: 9D 03 07        STA     $0703,X             
8BC3: A9 00           LDA     #$00                
8BC5: 9D 04 07        STA     $0704,X             
8BC8: 9D 05 07        STA     $0705,X             
8BCB: 60              RTS                         
8BCC: A2 60           LDX     #$60                
8BCE: BD 01 07        LDA     $0701,X             
8BD1: 29 F8           AND     #$F8                
8BD3: C9 60           CMP     #$60                
8BD5: D0 3F           BNE     $8C16               ; {}
8BD7: 20 E5 85        JSR     $85E5               ; {}
8BDA: BD 01 07        LDA     $0701,X             
8BDD: 29 07           AND     #$07                
8BDF: 20 2B EE        JSR     $EE2B               
8BE2: AF ; ????
8BE3: 8B ; ????
8BE4: E8              INX                         
8BE5: 8B ; ????
8BE6: 37 ; ????
8BE7: 8C BD 02        STY     $02BD               
8BEA: 07 ; ????
8BEB: 29 0F           AND     #$0F                
8BED: C9 08           CMP     #$08                
8BEF: B0 34           BCS     $8C25               ; {}
8BF1: A9 B0           LDA     #$B0                
8BF3: 85 08           STA     $08                 
8BF5: A9 30           LDA     #$30                
8BF7: 85 09           STA     $09                 
8BF9: A9 F0           LDA     #$F0                
8BFB: 85 0A           STA     $0A                 
8BFD: 20 6D C7        JSR     $C76D               
8C00: 20 90 D9        JSR     $D990               
8C03: 90 12           BCC     $8C17               ; {}
8C05: 20 E7 D9        JSR     $D9E7               
8C08: 90 12           BCC     $8C1C               ; {}
8C0A: 20 09 DA        JSR     $DA09               
8C0D: 20 4D 8C        JSR     $8C4D               ; {}
8C10: 20 C0 DB        JSR     $DBC0               
8C13: 20 17 8D        JSR     $8D17               ; {}
8C16: 60              RTS                         
8C17: A9 F8           LDA     #$F8                
8C19: 99 00 07        STA     $0700,Y             
8C1C: FE 01 07        INC     $0701,X             
8C1F: A9 FF           LDA     #$FF                
8C21: 9D 02 07        STA     $0702,X             
8C24: 60              RTS                         
8C25: A9 30           LDA     #$30                
8C27: 85 08           STA     $08                 
8C29: A9 30           LDA     #$30                
8C2B: 85 09           STA     $09                 
8C2D: A9 F0           LDA     #$F0                
8C2F: 85 0A           STA     $0A                 
8C31: 20 8D C7        JSR     $C78D               
8C34: 4C 00 8C        JMP     $8C00               ; {}
8C37: A9 F8           LDA     #$F8                
8C39: 9D 10 02        STA     $0210,X             
8C3C: 20 65 DD        JSR     $DD65               
8C3F: BD 02 07        LDA     $0702,X             
8C42: D0 08           BNE     $8C4C               ; {}
8C44: 20 2B DD        JSR     $DD2B               
8C47: A9 00           LDA     #$00                
8C49: 9D 01 07        STA     $0701,X             
8C4C: 60              RTS                         
8C4D: A0 80           LDY     #$80                
8C4F: B9 01 07        LDA     $0701,Y             
8C52: 29 F8           AND     #$F8                
8C54: C9 60           CMP     #$60                
8C56: D0 44           BNE     $8C9C               ; {}
8C58: A5 14           LDA     $14                 
8C5A: 29 7F           AND     #$7F                
8C5C: D0 3E           BNE     $8C9C               ; {}
8C5E: BD 00 07        LDA     $0700,X             
8C61: 99 00 07        STA     $0700,Y             
8C64: BD 03 07        LDA     $0703,X             
8C67: 99 03 07        STA     $0703,Y             
8C6A: BD 03 07        LDA     $0703,X             
8C6D: 38              SEC                         
8C6E: ED 23 07        SBC     $0723               
8C71: B0 02           BCS     $8C75               ; {}
8C73: 49 FF           EOR     #$FF                
8C75: 29 FC           AND     #$FC                
8C77: 85 00           STA     $00                 ; {ram.GP_00}
8C79: BD 00 07        LDA     $0700,X             
8C7C: 38              SEC                         
8C7D: ED 20 07        SBC     $0720               
8C80: B0 02           BCS     $8C84               ; {}
8C82: 49 FF           EOR     #$FF                
8C84: 29 FC           AND     #$FC                
8C86: C5 00           CMP     $00                 ; {ram.GP_00}
8C88: D0 12           BNE     $8C9C               ; {}
8C8A: BD 03 07        LDA     $0703,X             
8C8D: CD 23 07        CMP     $0723               
8C90: B0 0B           BCS     $8C9D               ; {}
8C92: A9 04           LDA     #$04                
8C94: 99 02 07        STA     $0702,Y             
8C97: A9 71           LDA     #$71                
8C99: 99 01 07        STA     $0701,Y             
8C9C: 60              RTS                         
8C9D: A9 0D           LDA     #$0D                
8C9F: D0 F3           BNE     $8C94               ; {}
8CA1: A2 80           LDX     #$80                
8CA3: BD 01 07        LDA     $0701,X             
8CA6: 29 F8           AND     #$F8                
8CA8: C9 70           CMP     #$70                
8CAA: D0 F0           BNE     $8C9C               ; {}
8CAC: BD 00 07        LDA     $0700,X             
8CAF: C9 C9           CMP     #$C9                
8CB1: B0 17           BCS     $8CCA               ; {}
8CB3: BD 03 07        LDA     $0703,X             
8CB6: C9 E8           CMP     #$E8                
8CB8: B0 10           BCS     $8CCA               ; {}
8CBA: C9 10           CMP     #$10                
8CBC: 90 0C           BCC     $8CCA               ; {}
8CBE: 20 E5 85        JSR     $85E5               ; {}
8CC1: 20 09 DA        JSR     $DA09               
8CC4: 20 D8 8C        JSR     $8CD8               ; {}
8CC7: 4C 05 8D        JMP     $8D05               ; {}
8CCA: A9 00           LDA     #$00                
8CCC: 9D 01 07        STA     $0701,X             
8CCF: A9 F8           LDA     #$F8                
8CD1: 9D 00 02        STA     $0200,X             
8CD4: 9D 00 07        STA     $0700,X             
8CD7: 60              RTS                         
8CD8: BD 02 07        LDA     $0702,X             
8CDB: 29 0F           AND     #$0F                
8CDD: C9 08           CMP     #$08                
8CDF: B0 12           BCS     $8CF3               ; {}
8CE1: FE 03 07        INC     $0703,X             
8CE4: FE 03 07        INC     $0703,X             
8CE7: FE 00 07        INC     $0700,X             
8CEA: FE 00 07        INC     $0700,X             
8CED: A9 42           LDA     #$42                
8CEF: 9D 02 02        STA     $0202,X             
8CF2: 60              RTS                         
8CF3: DE 03 07        DEC     $0703,X             
8CF6: DE 03 07        DEC     $0703,X             
8CF9: FE 00 07        INC     $0700,X             
8CFC: FE 00 07        INC     $0700,X             
8CFF: A9 02           LDA     #$02                
8D01: 9D 02 02        STA     $0202,X             
8D04: 60              RTS                         
8D05: A9 A9           LDA     #$A9                
8D07: 9D 01 02        STA     $0201,X             
8D0A: BD 00 07        LDA     $0700,X             
8D0D: 9D 00 02        STA     $0200,X             
8D10: BD 03 07        LDA     $0703,X             
8D13: 9D 03 02        STA     $0203,X             
8D16: 60              RTS                         
8D17: A0 00           LDY     #$00                
8D19: A5 14           LDA     $14                 
8D1B: 29 04           AND     #$04                
8D1D: D0 02           BNE     $8D21               ; {}
8D1F: A0 14           LDY     #$14                
8D21: BD 04 07        LDA     $0704,X             
8D24: 30 05           BMI     $8D2B               ; {}
8D26: 98              TYA                         
8D27: 18              CLC                         
8D28: 69 28           ADC     #$28                
8D2A: A8              TAY                         
8D2B: 98              TYA                         
8D2C: A8              TAY                         
8D2D: A9 04           LDA     #$04                
8D2F: 85 00           STA     $00                 ; {ram.GP_00}
8D31: BD 00 07        LDA     $0700,X             
8D34: 85 01           STA     $01                 
8D36: BD 03 07        LDA     $0703,X             
8D39: 85 02           STA     $02                 
8D3B: 8A              TXA                         
8D3C: 48              PHA                         
8D3D: B9 72 8D        LDA     $8D72,Y             ; {}
8D40: C9 7F           CMP     #$7F                
8D42: D0 04           BNE     $8D48               ; {}
8D44: A9 F8           LDA     #$F8                
8D46: D0 03           BNE     $8D4B               ; {}
8D48: 18              CLC                         
8D49: 65 01           ADC     $01                 
8D4B: 9D 00 02        STA     $0200,X             
8D4E: C8              INY                         
8D4F: E8              INX                         
8D50: B9 72 8D        LDA     $8D72,Y             ; {}
8D53: 9D 00 02        STA     $0200,X             
8D56: C8              INY                         
8D57: E8              INX                         
8D58: B9 72 8D        LDA     $8D72,Y             ; {}
8D5B: 9D 00 02        STA     $0200,X             
8D5E: C8              INY                         
8D5F: E8              INX                         
8D60: B9 72 8D        LDA     $8D72,Y             ; {}
8D63: 18              CLC                         
8D64: 65 02           ADC     $02                 
8D66: 9D 00 02        STA     $0200,X             
8D69: E8              INX                         
8D6A: C8              INY                         
8D6B: C6 00           DEC     $00                 ; {ram.GP_00}
8D6D: 10 CE           BPL     $8D3D               ; {}
8D6F: 68              PLA                         
8D70: AA              TAX                         
8D71: 60              RTS                         
8D72: F8              SED                         
8D73: D0 02           BNE     $8D77               ; {}
8D75: F8              SED                         
8D76: F8              SED                         
8D77: D1 02           CMP     ($02),Y             
8D79: 00              BRK                         
8D7A: F8              SED                         
8D7B: D2 ; ????
8D7C: 02 ; ????
8D7D: 08              PHP                         
8D7E: 00              BRK                         
8D7F: D3 ; ????
8D80: 02 ; ????
8D81: F8              SED                         
8D82: 00              BRK                         
8D83: D4 ; ????
8D84: 02 ; ????
8D85: 00              BRK                         
8D86: F8              SED                         
8D87: D5 02           CMP     $02,X               
8D89: F8              SED                         
8D8A: F8              SED                         
8D8B: D6 02           DEC     $02,X               
8D8D: 00              BRK                         
8D8E: F8              SED                         
8D8F: D7 ; ????
8D90: 02 ; ????
8D91: 08              PHP                         
8D92: 00              BRK                         
8D93: D3 ; ????
8D94: 02 ; ????
8D95: F8              SED                         
8D96: 00              BRK                         
8D97: D4 ; ????
8D98: 02 ; ????
8D99: 00              BRK                         
8D9A: F8              SED                         
8D9B: D2 ; ????
8D9C: 42 ; ????
8D9D: F8              SED                         
8D9E: F8              SED                         
8D9F: D1 42           CMP     ($42),Y             
8DA1: 00              BRK                         
8DA2: F8              SED                         
8DA3: D0 42           BNE     $8DE7               ; {}
8DA5: 08              PHP                         
8DA6: 00              BRK                         
8DA7: D4 ; ????
8DA8: 42 ; ????
8DA9: 00              BRK                         
8DAA: 00              BRK                         
8DAB: D3 ; ????
8DAC: 42 ; ????
8DAD: 08              PHP                         
8DAE: F8              SED                         
8DAF: D7 ; ????
8DB0: 42 ; ????
8DB1: F8              SED                         
8DB2: F8              SED                         
8DB3: D6 42           DEC     $42,X               
8DB5: 00              BRK                         
8DB6: F8              SED                         
8DB7: D5 42           CMP     $42,X               
8DB9: 08              PHP                         
8DBA: 00              BRK                         
8DBB: D4 ; ????
8DBC: 42 ; ????
8DBD: 00              BRK                         
8DBE: 00              BRK                         
8DBF: D3 ; ????
8DC0: 42 ; ????
8DC1: 08              PHP                         
8DC2: A2 60           LDX     #$60                
8DC4: A0 00           LDY     #$00                
8DC6: 20 DF 8D        JSR     $8DDF               ; {}
8DC9: A2 70           LDX     #$70                
8DCB: A0 20           LDY     #$20                
8DCD: 20 DF 8D        JSR     $8DDF               ; {}
8DD0: A2 80           LDX     #$80                
8DD2: A0 40           LDY     #$40                
8DD4: 20 DF 8D        JSR     $8DDF               ; {}
8DD7: A2 90           LDX     #$90                
8DD9: A0 60           LDY     #$60                
8DDB: 20 DF 8D        JSR     $8DDF               ; {}
8DDE: 60              RTS                         
8DDF: 20 EC 8D        JSR     $8DEC               ; {}
8DE2: C8              INY                         
8DE3: C8              INY                         
8DE4: C8              INY                         
8DE5: C8              INY                         
8DE6: 98              TYA                         
8DE7: 29 1F           AND     #$1F                
8DE9: D0 F4           BNE     $8DDF               ; {}
8DEB: 60              RTS                         
8DEC: B9 9B 76        LDA     $769B,Y             
8DEF: C9 FF           CMP     #$FF                
8DF1: F0 29           BEQ     $8E1C               ; {}
8DF3: CD 30 01        CMP     $0130               
8DF6: D0 23           BNE     $8E1B               ; {}
8DF8: AD D1 04        LDA     $04D1               
8DFB: D9 9C 76        CMP     $769C,Y             
8DFE: D0 1B           BNE     $8E1B               ; {}
8E00: A5 FD           LDA     $FD                 
8E02: D9 9D 76        CMP     $769D,Y             
8E05: D0 14           BNE     $8E1B               ; {}
8E07: A9 78           LDA     #$78                
8E09: 9D 01 07        STA     $0701,X             
8E0C: A9 0C           LDA     #$0C                
8E0E: 9D 02 07        STA     $0702,X             
8E11: A9 00           LDA     #$00                
8E13: 9D 00 07        STA     $0700,X             
8E16: A9 80           LDA     #$80                
8E18: 9D 03 07        STA     $0703,X             
8E1B: 60              RTS                         
8E1C: 68              PLA                         
8E1D: 68              PLA                         
8E1E: 60              RTS                         
8E1F: A2 60           LDX     #$60                
8E21: 20 33 8E        JSR     $8E33               ; {}
8E24: A2 70           LDX     #$70                
8E26: 20 33 8E        JSR     $8E33               ; {}
8E29: A2 80           LDX     #$80                
8E2B: 20 33 8E        JSR     $8E33               ; {}
8E2E: A2 90           LDX     #$90                
8E30: 4C 33 8E        JMP     $8E33               ; {}
8E33: BD 01 07        LDA     $0701,X             
8E36: 29 F8           AND     #$F8                
8E38: C9 78           CMP     #$78                
8E3A: D0 20           BNE     $8E5C               ; {}
8E3C: 20 49 E0        JSR     $E049               
8E3F: 20 E5 85        JSR     $85E5               ; {}
8E42: BD 01 07        LDA     $0701,X             
8E45: 29 07           AND     #$07                
8E47: BD 00 07        LDA     $0700,X             
8E4A: C9 F8           CMP     #$F8                
8E4C: B0 09           BCS     $8E57               ; {}
8E4E: 20 5D 8E        JSR     $8E5D               ; {}
8E51: 20 C0 DB        JSR     $DBC0               
8E54: 4C 85 8E        JMP     $8E85               ; {}
8E57: A9 00           LDA     #$00                
8E59: 9D 01 07        STA     $0701,X             
8E5C: 60              RTS                         
8E5D: A9 00           LDA     #$00                
8E5F: 9D 05 07        STA     $0705,X             
8E62: BD 02 07        LDA     $0702,X             
8E65: 29 0F           AND     #$0F                
8E67: C9 08           CMP     #$08                
8E69: B0 0D           BCS     $8E78               ; {}
8E6B: AD D5 04        LDA     $04D5               
8E6E: C9 40           CMP     #$40                
8E70: B0 0D           BCS     $8E7F               ; {}
8E72: A9 03           LDA     #$03                
8E74: 9D 02 07        STA     $0702,X             
8E77: 60              RTS                         
8E78: AD D6 04        LDA     $04D6               
8E7B: C9 40           CMP     #$40                
8E7D: B0 F3           BCS     $8E72               ; {}
8E7F: A9 0C           LDA     #$0C                
8E81: 9D 02 07        STA     $0702,X             
8E84: 60              RTS                         
8E85: A9 1B           LDA     #$1B                
8E87: 4C 67 C6        JMP     $C667               
8E8A: A9 02           LDA     #$02                
8E8C: 9D 02 07        STA     $0702,X             
8E8F: 20 5D 85        JSR     $855D               ; {}
8E92: A9 00           LDA     #$00                
8E94: 9D 04 07        STA     $0704,X             
8E97: 9D 05 07        STA     $0705,X             
8E9A: 9D 06 07        STA     $0706,X             
8E9D: F0 02           BEQ     $8EA1               ; {}
8E9F: A9 08           LDA     #$08                
8EA1: 9D 00 07        STA     $0700,X             
8EA4: 60              RTS                         
8EA5: A2 60           LDX     #$60                
8EA7: BD 01 07        LDA     $0701,X             
8EAA: 29 F8           AND     #$F8                
8EAC: C9 68           CMP     #$68                
8EAE: D0 12           BNE     $8EC2               ; {}
8EB0: 20 E0 8E        JSR     $8EE0               ; {}
8EB3: A2 78           LDX     #$78                
8EB5: 20 89 90        JSR     $9089               ; {}
8EB8: A2 78           LDX     #$78                
8EBA: 20 DC 90        JSR     $90DC               ; {}
8EBD: A2 7C           LDX     #$7C                
8EBF: 20 DC 90        JSR     $90DC               ; {}
8EC2: 60              RTS                         
8EC3: A2 C0           LDX     #$C0                
8EC5: BD 01 07        LDA     $0701,X             
8EC8: 29 F8           AND     #$F8                
8ECA: C9 68           CMP     #$68                
8ECC: D0 F4           BNE     $8EC2               ; {}
8ECE: 20 E0 8E        JSR     $8EE0               ; {}
8ED1: A2 D8           LDX     #$D8                
8ED3: 20 89 90        JSR     $9089               ; {}
8ED6: A2 D8           LDX     #$D8                
8ED8: 20 DC 90        JSR     $90DC               ; {}
8EDB: A2 DC           LDX     #$DC                
8EDD: 4C DC 90        JMP     $90DC               ; {}
8EE0: BD 01 07        LDA     $0701,X             
8EE3: 29 07           AND     #$07                
8EE5: 20 2B EE        JSR     $EE2B               
8EE8: B3 ; ????
8EE9: 8F ; ????
8EEA: F0 8E           BEQ     $8E7A               ; {}
8EEC: F0 8E           BEQ     $8E7C               ; {}
8EEE: A7 ; ????
8EEF: 8F ; ????
8EF0: 20 87 E0        JSR     $E087               
8EF3: 20 E5 85        JSR     $85E5               ; {}
8EF6: 20 08 DD        JSR     $DD08               
8EF9: 20 BC D9        JSR     $D9BC               
8EFC: 90 44           BCC     $8F42               ; {}
8EFE: 20 E7 D9        JSR     $D9E7               
8F01: 90 47           BCC     $8F4A               ; {}
8F03: 20 F3 8F        JSR     $8FF3               ; {}
8F06: BD 01 07        LDA     $0701,X             
8F09: 29 07           AND     #$07                
8F0B: C9 02           CMP     #$02                
8F0D: D0 03           BNE     $8F12               ; {}
8F0F: 4C 60 90        JMP     $9060               ; {}
8F12: BD 02 07        LDA     $0702,X             
8F15: 29 0F           AND     #$0F                
8F17: C9 03           CMP     #$03                
8F19: 90 10           BCC     $8F2B               ; {}
8F1B: C9 0D           CMP     #$0D                
8F1D: B0 0C           BCS     $8F2B               ; {}
8F1F: 20 09 DA        JSR     $DA09               
8F22: 20 3E 90        JSR     $903E               ; {}
8F25: 20 F8 8A        JSR     $8AF8               ; {}
8F28: 4C 38 8F        JMP     $8F38               ; {}
8F2B: BD 08 07        LDA     $0708,X             
8F2E: C9 04           CMP     #$04                
8F30: B0 09           BCS     $8F3B               ; {}
8F32: 20 F8 8A        JSR     $8AF8               ; {}
8F35: 20 D6 8F        JSR     $8FD6               ; {}
8F38: 20 C0 DB        JSR     $DBC0               
8F3B: 20 0D 90        JSR     $900D               ; {}
8F3E: 20 A2 8F        JSR     $8FA2               ; {}
8F41: 60              RTS                         
8F42: 20 8E 8F        JSR     $8F8E               ; {}
8F45: A9 F8           LDA     #$F8                
8F47: 99 00 07        STA     $0700,Y             
8F4A: A9 80           LDA     #$80                
8F4C: 8D 80 03        STA     $0380               
8F4F: 20 A9 DC        JSR     $DCA9               
8F52: BD 01 07        LDA     $0701,X             
8F55: 29 F8           AND     #$F8                
8F57: 09 03           ORA     #$03                
8F59: 9D 01 07        STA     $0701,X             
8F5C: A9 FF           LDA     #$FF                
8F5E: 9D 02 07        STA     $0702,X             
8F61: A9 08           LDA     #$08                
8F63: 8D 81 03        STA     $0381               
8F66: A9 F8           LDA     #$F8                
8F68: 9D 10 02        STA     $0210,X             
8F6B: 9D 14 02        STA     $0214,X             
8F6E: 20 76 85        JSR     $8576               ; {}
8F71: 20 E1 E2        JSR     $E2E1               
8F74: 4C F0 E2        JMP     $E2F0               
8F77: 20 8D 94        JSR     $948D               ; {}
8F7A: BD 03 07        LDA     $0703,X             
8F7D: CD 23 07        CMP     $0723               
8F80: 90 06           BCC     $8F88               ; {}
8F82: A9 0A           LDA     #$0A                
8F84: 9D 02 07        STA     $0702,X             
8F87: 60              RTS                         
8F88: A9 05           LDA     #$05                
8F8A: 9D 02 07        STA     $0702,X             
8F8D: 60              RTS                         
8F8E: BD 03 07        LDA     $0703,X             
8F91: CD 23 07        CMP     $0723               
8F94: 90 06           BCC     $8F9C               ; {}
8F96: A9 0D           LDA     #$0D                
8F98: 9D 02 07        STA     $0702,X             
8F9B: 60              RTS                         
8F9C: A9 02           LDA     #$02                
8F9E: 9D 02 07        STA     $0702,X             
8FA1: 60              RTS                         
8FA2: A9 14           LDA     #$14                
8FA4: 4C E0 DC        JMP     $DCE0               
8FA7: 20 87 E0        JSR     $E087               
8FAA: 20 E5 85        JSR     $85E5               ; {}
8FAD: 20 08 DD        JSR     $DD08               
8FB0: 4C 65 DD        JMP     $DD65               
8FB3: 20 9F 8E        JSR     $8E9F               ; {}
8FB6: 20 87 E0        JSR     $E087               
8FB9: AD D3 04        LDA     $04D3               
8FBC: C9 40           CMP     #$40                
8FBE: 90 15           BCC     $8FD5               ; {}
8FC0: AD D5 04        LDA     $04D5               
8FC3: C9 40           CMP     #$40                
8FC5: B0 0E           BCS     $8FD5               ; {}
8FC7: A5 FD           LDA     $FD                 
8FC9: 29 0F           AND     #$0F                
8FCB: C9 04           CMP     #$04                
8FCD: D0 06           BNE     $8FD5               ; {}
8FCF: 20 8A 8E        JSR     $8E8A               ; {}
8FD2: FE 01 07        INC     $0701,X             
8FD5: 60              RTS                         
8FD6: 8A              TXA                         
8FD7: 18              CLC                         
8FD8: 65 14           ADC     $14                 
8FDA: C9 20           CMP     #$20                
8FDC: B0 0E           BCS     $8FEC               ; {}
8FDE: BD 02 07        LDA     $0702,X             
8FE1: 29 0F           AND     #$0F                
8FE3: C9 08           CMP     #$08                
8FE5: B0 06           BCS     $8FED               ; {}
8FE7: A9 FC           LDA     #$FC                
8FE9: 9D 04 07        STA     $0704,X             
8FEC: 60              RTS                         
8FED: A9 04           LDA     #$04                
8FEF: 9D 04 07        STA     $0704,X             
8FF2: 60              RTS                         
8FF3: A5 3E           LDA     $3E                 
8FF5: F0 0F           BEQ     $9006               ; {}
8FF7: C9 01           CMP     #$01                
8FF9: F0 0C           BEQ     $9007               ; {}
8FFB: A9 F8           LDA     #$F8                
8FFD: 9D 10 02        STA     $0210,X             
9000: 9D 14 02        STA     $0214,X             
9003: 4C 62 DF        JMP     $DF62               
9006: 60              RTS                         
9007: 20 62 DF        JSR     $DF62               
900A: 68              PLA                         
900B: 68              PLA                         
900C: 60              RTS                         
900D: A0 20           LDY     #$20                
900F: BD 06 07        LDA     $0706,X             
9012: D0 0B           BNE     $901F               ; {}
9014: BD 04 07        LDA     $0704,X             
9017: C9 30           CMP     #$30                
9019: 90 19           BCC     $9034               ; {}
901B: C9 D0           CMP     #$D0                
901D: B0 15           BCS     $9034               ; {}
901F: A0 24           LDY     #$24                
9021: A5 14           LDA     $14                 
9023: 29 08           AND     #$08                
9025: D0 02           BNE     $9029               ; {}
9027: C8              INY                         
9028: C8              INY                         
9029: A5 14           LDA     $14                 
902B: 29 1F           AND     #$1F                
902D: D0 05           BNE     $9034               ; {}
902F: A9 02           LDA     #$02                
9031: 8D 83 03        STA     $0383               
9034: BD 04 07        LDA     $0704,X             
9037: 30 01           BMI     $903A               ; {}
9039: C8              INY                         
903A: 98              TYA                         
903B: 4C CD C4        JMP     $C4CD               
903E: BD 04 07        LDA     $0704,X             
9041: 30 15           BMI     $9058               ; {}
9043: AD D3 04        LDA     $04D3               
9046: C9 40           CMP     #$40                
9048: B0 0D           BCS     $9057               ; {}
904A: FE 01 07        INC     $0701,X             
904D: A9 80           LDA     #$80                
904F: 9D 06 07        STA     $0706,X             
9052: A9 02           LDA     #$02                
9054: 8D 83 03        STA     $0383               
9057: 60              RTS                         
9058: AD D4 04        LDA     $04D4               
905B: C9 40           CMP     #$40                
905D: 90 EB           BCC     $904A               ; {}
905F: 60              RTS                         
9060: BD 06 07        LDA     $0706,X             
9063: 29 0F           AND     #$0F                
9065: D0 09           BNE     $9070               ; {}
9067: BD 00 07        LDA     $0700,X             
906A: 38              SEC                         
906B: E9 04           SBC     #$04                
906D: 9D 00 07        STA     $0700,X             
9070: 20 F8 8A        JSR     $8AF8               ; {}
9073: 20 C0 DB        JSR     $DBC0               
9076: 20 0D 90        JSR     $900D               ; {}
9079: DE 06 07        DEC     $0706,X             
907C: D0 0A           BNE     $9088               ; {}
907E: BD 01 07        LDA     $0701,X             
9081: 29 F8           AND     #$F8                
9083: 09 01           ORA     #$01                
9085: 9D 01 07        STA     $0701,X             
9088: 60              RTS                         
9089: 8A              TXA                         
908A: 38              SEC                         
908B: E9 18           SBC     #$18                
908D: A8              TAY                         
908E: B9 01 07        LDA     $0701,Y             
9091: C9 69           CMP     #$69                
9093: F0 03           BEQ     $9098               ; {}
9095: 4C 19 91        JMP     $9119               ; {}
9098: BD 01 07        LDA     $0701,X             
909B: 29 F8           AND     #$F8                
909D: C9 70           CMP     #$70                
909F: F0 09           BEQ     $90AA               ; {}
90A1: B9 00 07        LDA     $0700,Y             
90A4: 38              SEC                         
90A5: E9 12           SBC     #$12                
90A7: 20 BD 90        JSR     $90BD               ; {}
90AA: E8              INX                         
90AB: E8              INX                         
90AC: E8              INX                         
90AD: E8              INX                         
90AE: BD 01 07        LDA     $0701,X             
90B1: 29 F8           AND     #$F8                
90B3: C9 70           CMP     #$70                
90B5: F0 1E           BEQ     $90D5               ; {}
90B7: B9 00 07        LDA     $0700,Y             
90BA: 38              SEC                         
90BB: E9 02           SBC     #$02                
90BD: 9D 00 07        STA     $0700,X             
90C0: A9 70           LDA     #$70                
90C2: 9D 01 07        STA     $0701,X             
90C5: B9 03 07        LDA     $0703,Y             
90C8: 9D 03 07        STA     $0703,X             
90CB: B9 04 07        LDA     $0704,Y             
90CE: 30 06           BMI     $90D6               ; {}
90D0: A9 04           LDA     #$04                
90D2: 9D 02 07        STA     $0702,X             
90D5: 60              RTS                         
90D6: A9 0C           LDA     #$0C                
90D8: 9D 02 07        STA     $0702,X             
90DB: 60              RTS                         
90DC: BD 01 07        LDA     $0701,X             
90DF: 29 F8           AND     #$F8                
90E1: C9 70           CMP     #$70                
90E3: D0 F0           BNE     $90D5               ; {}
90E5: BD 03 07        LDA     $0703,X             
90E8: C9 F8           CMP     #$F8                
90EA: B0 2D           BCS     $9119               ; {}
90EC: 20 E5 85        JSR     $85E5               ; {}
90EF: 20 35 E0        JSR     $E035               
90F2: D0 25           BNE     $9119               ; {}
90F4: 20 EF DA        JSR     $DAEF               
90F7: 90 06           BCC     $90FF               ; {}
90F9: 20 27 91        JSR     $9127               ; {}
90FC: 4C 44 91        JMP     $9144               ; {}
90FF: A0 60           LDY     #$60                
9101: E0 C0           CPX     #$C0                
9103: 90 02           BCC     $9107               ; {}
9105: A0 C0           LDY     #$C0                
9107: B9 01 07        LDA     $0701,Y             
910A: 29 07           AND     #$07                
910C: C9 01           CMP     #$01                
910E: D0 09           BNE     $9119               ; {}
9110: 8A              TXA                         
9111: 48              PHA                         
9112: 98              TYA                         
9113: AA              TAX                         
9114: 20 77 8F        JSR     $8F77               ; {}
9117: 68              PLA                         
9118: AA              TAX                         
9119: A9 00           LDA     #$00                
911B: 9D 01 07        STA     $0701,X             
911E: A9 F8           LDA     #$F8                
9120: 9D 00 02        STA     $0200,X             
9123: 9D 00 07        STA     $0700,X             
9126: 60              RTS                         
9127: BD 02 07        LDA     $0702,X             
912A: 29 0F           AND     #$0F                
912C: C9 08           CMP     #$08                
912E: B0 0A           BCS     $913A               ; {}
9130: BD 03 07        LDA     $0703,X             
9133: 18              CLC                         
9134: 69 04           ADC     #$04                
9136: 9D 03 07        STA     $0703,X             
9139: 60              RTS                         
913A: BD 03 07        LDA     $0703,X             
913D: 38              SEC                         
913E: E9 04           SBC     #$04                
9140: 9D 03 07        STA     $0703,X             
9143: 60              RTS                         
9144: A9 5F           LDA     #$5F                
9146: 9D 01 02        STA     $0201,X             
9149: BD 00 07        LDA     $0700,X             
914C: 9D 00 02        STA     $0200,X             
914F: BD 03 07        LDA     $0703,X             
9152: 9D 03 02        STA     $0203,X             
9155: 60              RTS                         
9156: 60              RTS                         
9157: 20 AB 91        JSR     $91AB               ; {}
915A: AD C1 07        LDA     $07C1               
915D: 0D C9 07        ORA     $07C9               
9160: 0D D1 07        ORA     $07D1               
9163: 0D D9 07        ORA     $07D9               
9166: F0 09           BEQ     $9171               ; {}
9168: 20 06 92        JSR     $9206               ; {}
916B: 20 FF 92        JSR     $92FF               ; {}
916E: 4C C3 8E        JMP     $8EC3               ; {}
9171: AD 30 01        LDA     $0130               
9174: 0A              ASL     A                   
9175: A8              TAY                         
9176: B9 55 78        LDA     $7855,Y             
9179: 85 00           STA     $00                 ; {ram.GP_00}
917B: B9 56 78        LDA     $7856,Y             
917E: 85 01           STA     $01                 
9180: AC D1 04        LDY     $04D1               
9183: B1 00           LDA     ($00),Y             ; {ram.GP_00}
9185: 0A              ASL     A                   
9186: 0A              ASL     A                   
9187: 0A              ASL     A                   
9188: C9 18           CMP     #$18                
918A: F0 14           BEQ     $91A0               ; {}
918C: C9 68           CMP     #$68                
918E: F0 16           BEQ     $91A6               ; {}
9190: 20 99 DC        JSR     $DC99               
9193: 8D C1 07        STA     $07C1               
9196: 8D C9 07        STA     $07C9               
9199: 8D D1 07        STA     $07D1               
919C: 8D D9 07        STA     $07D9               
919F: 60              RTS                         
91A0: 8D C1 07        STA     $07C1               
91A3: 8D D1 07        STA     $07D1               
91A6: 60              RTS                         
91A7: 8D C1 07        STA     $07C1               
91AA: 60              RTS                         
91AB: AD C1 07        LDA     $07C1               
91AE: 29 F8           AND     #$F8                
91B0: C9 68           CMP     #$68                
91B2: F0 32           BEQ     $91E6               ; {}
91B4: AD 30 01        LDA     $0130               
91B7: 0A              ASL     A                   
91B8: A8              TAY                         
91B9: B9 8F 78        LDA     $788F,Y             
91BC: 85 00           STA     $00                 ; {ram.GP_00}
91BE: B9 90 78        LDA     $7890,Y             
91C1: 85 01           STA     $01                 
91C3: AC D1 04        LDY     $04D1               
91C6: B1 00           LDA     ($00),Y             ; {ram.GP_00}
91C8: F0 1C           BEQ     $91E6               ; {}
91CA: 29 F0           AND     #$F0                
91CC: 38              SEC                         
91CD: E5 FD           SBC     $FD                 
91CF: C9 FC           CMP     #$FC                
91D1: 90 13           BCC     $91E6               ; {}
91D3: B1 00           LDA     ($00),Y             ; {ram.GP_00}
91D5: 0A              ASL     A                   
91D6: 0A              ASL     A                   
91D7: 0A              ASL     A                   
91D8: 0A              ASL     A                   
91D9: 8D C3 07        STA     $07C3               
91DC: A9 68           LDA     #$68                
91DE: 8D C1 07        STA     $07C1               
91E1: A9 00           LDA     #$00                
91E3: 8D D1 07        STA     $07D1               
91E6: 60              RTS                         
91E7: 60              RTS                         
91E8: 60              RTS                         
91E9: A9 10           LDA     #$10                
91EB: 9D 01 07        STA     $0701,X             
91EE: A9 02           LDA     #$02                
91F0: 9D 02 07        STA     $0702,X             
91F3: A9 00           LDA     #$00                
91F5: 9D 04 07        STA     $0704,X             
91F8: 9D 05 07        STA     $0705,X             
91FB: A9 08           LDA     #$08                
91FD: 9D 00 07        STA     $0700,X             
9200: A9 80           LDA     #$80                
9202: 9D 03 07        STA     $0703,X             
9205: 60              RTS                         
9206: A2 C0           LDX     #$C0                
9208: 20 1A 92        JSR     $921A               ; {}
920B: A2 C8           LDX     #$C8                
920D: 20 1A 92        JSR     $921A               ; {}
9210: A2 D0           LDX     #$D0                
9212: 20 1A 92        JSR     $921A               ; {}
9215: A2 D8           LDX     #$D8                
9217: 4C 1A 92        JMP     $921A               ; {}
921A: BD 01 07        LDA     $0701,X             
921D: 29 F8           AND     #$F8                
921F: C9 10           CMP     #$10                
9221: D0 31           BNE     $9254               ; {}
9223: BD 01 07        LDA     $0701,X             
9226: 29 07           AND     #$07                
9228: F0 59           BEQ     $9283               ; {}
922A: C9 01           CMP     #$01                
922C: D0 4C           BNE     $927A               ; {}
922E: 20 53 E0        JSR     $E053               
9231: 20 E5 85        JSR     $85E5               ; {}
9234: BD 00 07        LDA     $0700,X             
9237: C9 F8           CMP     #$F8                
9239: B0 3C           BCS     $9277               ; {}
923B: 20 90 D9        JSR     $D990               
923E: 90 15           BCC     $9255               ; {}
9240: 20 E7 D9        JSR     $D9E7               
9243: 90 15           BCC     $925A               ; {}
9245: 20 09 DA        JSR     $DA09               
9248: 20 65 DF        JSR     $DF65               
924B: 20 C3 92        JSR     $92C3               ; {}
924E: 20 C0 DB        JSR     $DBC0               
9251: 20 D5 C7        JSR     $C7D5               
9254: 60              RTS                         
9255: A9 F8           LDA     #$F8                
9257: 99 00 07        STA     $0700,Y             
925A: BD 01 07        LDA     $0701,X             
925D: 29 F8           AND     #$F8                
925F: 09 02           ORA     #$02                
9261: 9D 01 07        STA     $0701,X             
9264: A9 FF           LDA     #$FF                
9266: 9D 02 07        STA     $0702,X             
9269: A9 08           LDA     #$08                
926B: 8D 81 03        STA     $0381               
926E: 20 76 85        JSR     $8576               ; {}
9271: 20 E1 E2        JSR     $E2E1               
9274: 4C F0 E2        JMP     $E2F0               
9277: 4C 2F DF        JMP     $DF2F               
927A: 20 53 E0        JSR     $E053               
927D: 20 E5 85        JSR     $85E5               ; {}
9280: 4C B2 DE        JMP     $DEB2               
9283: 8A              TXA                         
9284: 38              SEC                         
9285: E9 C0           SBC     #$C0                
9287: 0A              ASL     A                   
9288: 0A              ASL     A                   
9289: 0A              ASL     A                   
928A: 85 00           STA     $00                 ; {ram.GP_00}
928C: A5 14           LDA     $14                 
928E: 29 C0           AND     #$C0                
9290: C5 00           CMP     $00                 ; {ram.GP_00}
9292: D0 1A           BNE     $92AE               ; {}
9294: 20 FB 91        JSR     $91FB               ; {}
9297: 20 53 E0        JSR     $E053               
929A: AD D5 04        LDA     $04D5               
929D: C9 40           CMP     #$40                
929F: B0 0D           BCS     $92AE               ; {}
92A1: AD D3 04        LDA     $04D3               
92A4: C9 40           CMP     #$40                
92A6: B0 06           BCS     $92AE               ; {}
92A8: 20 E9 91        JSR     $91E9               ; {}
92AB: FE 01 07        INC     $0701,X             
92AE: 60              RTS                         
92AF: AD 23 07        LDA     $0723               
92B2: DD 03 07        CMP     $0703,X             
92B5: 90 06           BCC     $92BD               ; {}
92B7: A9 60           LDA     #$60                
92B9: 9D 02 07        STA     $0702,X             
92BC: 60              RTS                         
92BD: A9 6F           LDA     #$6F                
92BF: 9D 02 07        STA     $0702,X             
92C2: 60              RTS                         
92C3: 20 87 D2        JSR     $D287               
92C6: D0 E7           BNE     $92AF               ; {}
92C8: AD D3 04        LDA     $04D3               
92CB: C9 40           CMP     #$40                
92CD: 90 E0           BCC     $92AF               ; {}
92CF: A9 00           LDA     #$00                
92D1: 9D 05 07        STA     $0705,X             
92D4: BD 02 07        LDA     $0702,X             
92D7: 29 0F           AND     #$0F                
92D9: C9 08           CMP     #$08                
92DB: B0 0D           BCS     $92EA               ; {}
92DD: AD D5 04        LDA     $04D5               
92E0: C9 40           CMP     #$40                
92E2: B0 0D           BCS     $92F1               ; {}
92E4: A9 03           LDA     #$03                
92E6: 9D 02 07        STA     $0702,X             
92E9: 60              RTS                         
92EA: AD D6 04        LDA     $04D6               
92ED: C9 40           CMP     #$40                
92EF: B0 F3           BCS     $92E4               ; {}
92F1: A9 0C           LDA     #$0C                
92F3: 9D 02 07        STA     $0702,X             
92F6: 60              RTS                         
92F7: A2 F0           LDX     #$F0                
92F9: A9 00           LDA     #$00                
92FB: 9D 01 07        STA     $0701,X             
92FE: 60              RTS                         
92FF: A2 C0           LDX     #$C0                
9301: 20 0A 93        JSR     $930A               ; {}
9304: A2 D0           LDX     #$D0                
9306: 20 0A 93        JSR     $930A               ; {}
9309: 60              RTS                         
930A: BD 01 07        LDA     $0701,X             
930D: 29 F8           AND     #$F8                
930F: C9 18           CMP     #$18                
9311: D0 EB           BNE     $92FE               ; {}
9313: 20 E5 85        JSR     $85E5               ; {}
9316: BD 01 07        LDA     $0701,X             
9319: 29 07           AND     #$07                
931B: F0 0D           BEQ     $932A               ; {}
931D: C9 01           CMP     #$01                
931F: D0 03           BNE     $9324               ; {}
9321: 4C 83 93        JMP     $9383               ; {}
9324: 20 08 DD        JSR     $DD08               
9327: 4C 65 DD        JMP     $DD65               
932A: 8A              TXA                         
932B: 38              SEC                         
932C: E9 C0           SBC     #$C0                
932E: 85 01           STA     $01                 
9330: 0A              ASL     A                   
9331: 18              CLC                         
9332: 65 14           ADC     $14                 
9334: 29 7F           AND     #$7F                
9336: D0 43           BNE     $937B               ; {}
9338: A5 26           LDA     $26                 
933A: 4A              LSR     A                   
933B: 4A              LSR     A                   
933C: 4A              LSR     A                   
933D: 29 03           AND     #$03                
933F: A8              TAY                         
9340: B9 7C 93        LDA     $937C,Y             ; {}
9343: 18              CLC                         
9344: 65 01           ADC     $01                 
9346: 85 00           STA     $00                 ; {ram.GP_00}
9348: AD 20 07        LDA     $0720               
934B: 9D 00 07        STA     $0700,X             
934E: AD 23 07        LDA     $0723               
9351: 18              CLC                         
9352: 65 00           ADC     $00                 ; {ram.GP_00}
9354: 9D 03 07        STA     $0703,X             
9357: A5 1E           LDA     $1E                 
9359: 29 C0           AND     #$C0                
935B: D0 1E           BNE     $937B               ; {}
935D: 20 87 E0        JSR     $E087               
9360: AD D3 04        LDA     $04D3               
9363: C9 40           CMP     #$40                
9365: 90 14           BCC     $937B               ; {}
9367: AD D4 04        LDA     $04D4               
936A: C9 40           CMP     #$40                
936C: 90 0D           BCC     $937B               ; {}
936E: AD D5 04        LDA     $04D5               
9371: D0 08           BNE     $937B               ; {}
9373: FE 01 07        INC     $0701,X             
9376: A9 00           LDA     #$00                
9378: 9D 06 07        STA     $0706,X             
937B: 60              RTS                         
937C: E0 00           CPX     #$00                
937E: 10 20           BPL     $93A0               ; {}
9380: 4C 1D DD        JMP     $DD1D               
9383: 20 08 DD        JSR     $DD08               
9386: BD 06 07        LDA     $0706,X             
9389: C9 40           CMP     #$40                
938B: 90 11           BCC     $939E               ; {}
938D: C9 60           CMP     #$60                
938F: B0 0D           BCS     $939E               ; {}
9391: 20 09 DA        JSR     $DA09               
9394: 20 90 D9        JSR     $D990               
9397: 90 0E           BCC     $93A7               ; {}
9399: 20 E7 D9        JSR     $D9E7               
939C: 90 0E           BCC     $93AC               ; {}
939E: FE 06 07        INC     $0706,X             
93A1: 20 62 DF        JSR     $DF62               
93A4: 4C C9 93        JMP     $93C9               ; {}
93A7: A9 F8           LDA     #$F8                
93A9: 99 00 07        STA     $0700,Y             
93AC: BD 01 07        LDA     $0701,X             
93AF: 29 F8           AND     #$F8                
93B1: 09 02           ORA     #$02                
93B3: 9D 01 07        STA     $0701,X             
93B6: A9 FF           LDA     #$FF                
93B8: 9D 02 07        STA     $0702,X             
93BB: A9 08           LDA     #$08                
93BD: 8D 81 03        STA     $0381               
93C0: 20 76 85        JSR     $8576               ; {}
93C3: 20 E1 E2        JSR     $E2E1               
93C6: 4C F0 E2        JMP     $E2F0               
93C9: BD 06 07        LDA     $0706,X             
93CC: C9 7F           CMP     #$7F                
93CE: F0 B0           BEQ     $9380               ; {}
93D0: C9 20           CMP     #$20                
93D2: 90 15           BCC     $93E9               ; {}
93D4: C9 40           CMP     #$40                
93D6: 90 04           BCC     $93DC               ; {}
93D8: C9 60           CMP     #$60                
93DA: 90 12           BCC     $93EE               ; {}
93DC: A0 0A           LDY     #$0A                
93DE: A5 14           LDA     $14                 
93E0: 29 04           AND     #$04                
93E2: D0 01           BNE     $93E5               ; {}
93E4: C8              INY                         
93E5: 98              TYA                         
93E6: 4C 67 C6        JMP     $C667               
93E9: A9 09           LDA     #$09                
93EB: 4C 67 C6        JMP     $C667               
93EE: 20 F5 93        JSR     $93F5               ; {}
93F1: A0 0C           LDY     #$0C                
93F3: D0 E9           BNE     $93DE               ; {}
93F5: A0 F0           LDY     #$F0                
93F7: B9 01 07        LDA     $0701,Y             
93FA: 29 F8           AND     #$F8                
93FC: D0 1E           BNE     $941C               ; {}
93FE: A9 70           LDA     #$70                
9400: 99 01 07        STA     $0701,Y             
9403: BD 00 07        LDA     $0700,X             
9406: 38              SEC                         
9407: E9 0C           SBC     #$0C                
9409: 99 00 07        STA     $0700,Y             
940C: BD 03 07        LDA     $0703,X             
940F: 99 03 07        STA     $0703,Y             
9412: CD 23 07        CMP     $0723               
9415: B0 06           BCS     $941D               ; {}
9417: A9 04           LDA     #$04                
9419: 99 02 07        STA     $0702,Y             
941C: 60              RTS                         
941D: A9 0D           LDA     #$0D                
941F: 99 02 07        STA     $0702,Y             
9422: 60              RTS                         
9423: BD 01 07        LDA     $0701,X             
9426: 29 F8           AND     #$F8                
9428: C9 70           CMP     #$70                
942A: D0 F0           BNE     $941C               ; {}
942C: BD 00 07        LDA     $0700,X             
942F: C9 F8           CMP     #$F8                
9431: B0 1D           BCS     $9450               ; {}
9433: BD 03 07        LDA     $0703,X             
9436: C9 F8           CMP     #$F8                
9438: B0 16           BCS     $9450               ; {}
943A: 20 E5 85        JSR     $85E5               ; {}
943D: BD 04 07        LDA     $0704,X             
9440: 48              PHA                         
9441: 20 09 DA        JSR     $DA09               
9444: 68              PLA                         
9445: 9D 04 07        STA     $0704,X             
9448: 90 06           BCC     $9450               ; {}
944A: 20 5E 94        JSR     $945E               ; {}
944D: 4C 6F 94        JMP     $946F               ; {}
9450: A9 00           LDA     #$00                
9452: 9D 01 07        STA     $0701,X             
9455: A9 F8           LDA     #$F8                
9457: 9D 00 02        STA     $0200,X             
945A: 9D 00 07        STA     $0700,X             
945D: 60              RTS                         
945E: BD 02 07        LDA     $0702,X             
9461: 29 0F           AND     #$0F                
9463: C9 08           CMP     #$08                
9465: 90 04           BCC     $946B               ; {}
9467: DE 03 07        DEC     $0703,X             
946A: 60              RTS                         
946B: FE 03 07        INC     $0703,X             
946E: 60              RTS                         
946F: A9 A9           LDA     #$A9                
9471: 9D 01 02        STA     $0201,X             
9474: BD 00 07        LDA     $0700,X             
9477: 38              SEC                         
9478: E9 04           SBC     #$04                
947A: 9D 00 02        STA     $0200,X             
947D: BD 03 07        LDA     $0703,X             
9480: 9D 03 02        STA     $0203,X             
9483: A9 01           LDA     #$01                
9485: 9D 02 02        STA     $0202,X             
9488: 60              RTS                         
9489: 60              RTS                         
948A: 4C AF 94        JMP     $94AF               ; {}
948D: AD A1 07        LDA     $07A1               
9490: 0D A9 07        ORA     $07A9               
9493: 0D B1 07        ORA     $07B1               
9496: 0D B9 07        ORA     $07B9               
9499: D0 13           BNE     $94AE               ; {}
949B: A9 08           LDA     #$08                
949D: 8D A1 07        STA     $07A1               
94A0: 8D A9 07        STA     $07A9               
94A3: 8D B1 07        STA     $07B1               
94A6: 8D B9 07        STA     $07B9               
94A9: A9 80           LDA     #$80                
94AB: 8D 85 03        STA     $0385               
94AE: 60              RTS                         
94AF: A2 A0           LDX     #$A0                
94B1: 20 C0 94        JSR     $94C0               ; {}
94B4: A2 A8           LDX     #$A8                
94B6: 20 C0 94        JSR     $94C0               ; {}
94B9: A2 B0           LDX     #$B0                
94BB: 20 C0 94        JSR     $94C0               ; {}
94BE: A2 B8           LDX     #$B8                
94C0: BD 01 07        LDA     $0701,X             
94C3: 29 F8           AND     #$F8                
94C5: C9 08           CMP     #$08                
94C7: D0 E5           BNE     $94AE               ; {}
94C9: BD 01 07        LDA     $0701,X             
94CC: 29 07           AND     #$07                
94CE: 20 2B EE        JSR     $EE2B               
94D1: A9 95           LDA     #$95                
94D3: F1 94           SBC     ($94),Y             
94D5: 74 ; ????
94D6: 95 D9           STA     $D9,X               
94D8: 94 20           STY     $20,X               
94DA: E5 85           SBC     $85                 
94DC: 20 B2 DE        JSR     $DEB2               
94DF: AD A1 07        LDA     $07A1               
94E2: 0D A9 07        ORA     $07A9               
94E5: 0D B1 07        ORA     $07B1               
94E8: 0D B9 07        ORA     $07B9               
94EB: D0 03           BNE     $94F0               ; {}
94ED: 20 70 CB        JSR     $CB70               
94F0: 60              RTS                         
94F1: 20 FB 95        JSR     $95FB               ; {}
94F4: BD 02 07        LDA     $0702,X             
94F7: 29 0F           AND     #$0F                
94F9: C9 08           CMP     #$08                
94FB: B0 59           BCS     $9556               ; {}
94FD: A9 D8           LDA     #$D8                
94FF: 85 08           STA     $08                 
9501: 20 63 95        JSR     $9563               ; {}
9504: 20 6D C7        JSR     $C76D               
9507: 20 C5 85        JSR     $85C5               ; {}
950A: 20 90 D9        JSR     $D990               
950D: 90 24           BCC     $9533               ; {}
950F: 20 E7 D9        JSR     $D9E7               
9512: 90 24           BCC     $9538               ; {}
9514: 20 09 DA        JSR     $DA09               
9517: F0 C6           BEQ     $94DF               ; {}
9519: 90 C4           BCC     $94DF               ; {}
951B: 20 62 DF        JSR     $DF62               
951E: 20 E5 85        JSR     $85E5               ; {}
9521: 20 C0 DB        JSR     $DBC0               
9524: 20 BB 95        JSR     $95BB               ; {}
9527: A5 14           LDA     $14                 
9529: 29 3F           AND     #$3F                
952B: D0 05           BNE     $9532               ; {}
952D: A9 01           LDA     #$01                
952F: 8D 83 03        STA     $0383               
9532: 60              RTS                         
9533: A9 F8           LDA     #$F8                
9535: 99 00 07        STA     $0700,Y             
9538: BD 01 07        LDA     $0701,X             
953B: 29 F8           AND     #$F8                
953D: 09 03           ORA     #$03                
953F: 9D 01 07        STA     $0701,X             
9542: A9 FF           LDA     #$FF                
9544: 9D 02 07        STA     $0702,X             
9547: 20 76 85        JSR     $8576               ; {}
954A: 20 E1 E2        JSR     $E2E1               
954D: 20 F0 E2        JSR     $E2F0               
9550: A9 01           LDA     #$01                
9552: 8D 83 03        STA     $0383               
9555: 60              RTS                         
9556: A9 28           LDA     #$28                
9558: 85 08           STA     $08                 
955A: 20 63 95        JSR     $9563               ; {}
955D: 20 8D C7        JSR     $C78D               
9560: 4C 0A 95        JMP     $950A               ; {}
9563: AD 20 07        LDA     $0720               
9566: 38              SEC                         
9567: E9 30           SBC     #$30                
9569: 85 09           STA     $09                 
956B: AD 20 07        LDA     $0720               
956E: 18              CLC                         
956F: 69 30           ADC     #$30                
9571: 85 0A           STA     $0A                 
9573: 60              RTS                         
9574: 20 FB 95        JSR     $95FB               ; {}
9577: BD 02 07        LDA     $0702,X             
957A: 29 0F           AND     #$0F                
957C: C9 08           CMP     #$08                
957E: B0 0F           BCS     $958F               ; {}
9580: AD 23 07        LDA     $0723               
9583: 18              CLC                         
9584: 69 10           ADC     #$10                
9586: 20 9E 95        JSR     $959E               ; {}
9589: 20 6D C7        JSR     $C76D               
958C: 4C 0A 95        JMP     $950A               ; {}
958F: AD 23 07        LDA     $0723               
9592: 38              SEC                         
9593: E9 10           SBC     #$10                
9595: 20 9E 95        JSR     $959E               ; {}
9598: 20 8D C7        JSR     $C78D               
959B: 4C 0A 95        JMP     $950A               ; {}
959E: 85 08           STA     $08                 
95A0: A9 30           LDA     #$30                
95A2: 85 09           STA     $09                 
95A4: A9 F8           LDA     #$F8                
95A6: 85 0A           STA     $0A                 
95A8: 60              RTS                         
95A9: 8A              TXA                         
95AA: 0A              ASL     A                   
95AB: C5 14           CMP     $14                 
95AD: D0 0B           BNE     $95BA               ; {}
95AF: 20 EE 91        JSR     $91EE               ; {}
95B2: A9 44           LDA     #$44                
95B4: 9D 02 07        STA     $0702,X             
95B7: FE 01 07        INC     $0701,X             
95BA: 60              RTS                         
95BB: A9 79           LDA     #$79                
95BD: 9D 01 02        STA     $0201,X             
95C0: A9 78           LDA     #$78                
95C2: 9D 05 02        STA     $0205,X             
95C5: BD 00 07        LDA     $0700,X             
95C8: 9D 00 02        STA     $0200,X             
95CB: 38              SEC                         
95CC: E9 08           SBC     #$08                
95CE: 9D 04 02        STA     $0204,X             
95D1: BD 03 07        LDA     $0703,X             
95D4: 9D 03 02        STA     $0203,X             
95D7: 48              PHA                         
95D8: A0 00           LDY     #$00                
95DA: BD 02 07        LDA     $0702,X             
95DD: 29 0F           AND     #$0F                
95DF: C9 08           CMP     #$08                
95E1: B0 02           BCS     $95E5               ; {}
95E3: A0 02           LDY     #$02                
95E5: 68              PLA                         
95E6: 18              CLC                         
95E7: 79 F7 95        ADC     $95F7,Y             ; {}
95EA: 9D 07 02        STA     $0207,X             
95ED: B9 F8 95        LDA     $95F8,Y             ; {}
95F0: 9D 02 02        STA     $0202,X             
95F3: 9D 06 02        STA     $0206,X             
95F6: 60              RTS                         
95F7: FE 02 02        INC     $0202,X             
95FA: 42 ; ????
95FB: BD 00 07        LDA     $0700,X             
95FE: C9 F0           CMP     #$F0                
9600: B0 07           BCS     $9609               ; {}
9602: BD 03 07        LDA     $0703,X             
9605: C9 FC           CMP     #$FC                
9607: 90 ED           BCC     $95F6               ; {}
9609: 68              PLA                         
960A: 68              PLA                         
960B: 20 2F DF        JSR     $DF2F               
960E: 4C DF 94        JMP     $94DF               ; {}
9611: AC 30 01        LDY     $0130               
9614: B9 C9 78        LDA     $78C9,Y             
9617: A8              TAY                         
9618: 20 1E 96        JSR     $961E               ; {}
961B: 60              RTS                         
961C: A0 1F           LDY     #$1F                
961E: A2 1F           LDX     #$1F                
9620: B9 CC 78        LDA     $78CC,Y             
9623: 9D 90 03        STA     $0390,X             
9626: 88              DEY                         
9627: CA              DEX                         
9628: 10 F6           BPL     $9620               ; {}
962A: 60              RTS                         
962B: 85 02           STA     $02                 
962D: 84 03           STY     $03                 
962F: A5 1A           LDA     $1A                 
9631: 29 01           AND     #$01                
9633: 0A              ASL     A                   
9634: A8              TAY                         
9635: B9 1B 77        LDA     $771B,Y             
9638: 85 00           STA     $00                 ; {ram.GP_00}
963A: B9 1C 77        LDA     $771C,Y             
963D: 85 01           STA     $01                 
963F: 98              TYA                         
9640: F0 03           BEQ     $9645               ; {}
9642: 4C 70 96        JMP     $9670               ; {}
9645: A5 FD           LDA     $FD                 
9647: 18              CLC                         
9648: 65 00           ADC     $00                 ; {ram.GP_00}
964A: 85 00           STA     $00                 ; {ram.GP_00}
964C: A9 00           LDA     #$00                
964E: 65 01           ADC     $01                 
9650: 85 01           STA     $01                 
9652: A5 02           LDA     $02                 
9654: 18              CLC                         
9655: 65 00           ADC     $00                 ; {ram.GP_00}
9657: 29 F0           AND     #$F0                
9659: 85 00           STA     $00                 ; {ram.GP_00}
965B: A9 00           LDA     #$00                
965D: 65 01           ADC     $01                 
965F: 85 01           STA     $01                 
9661: A5 03           LDA     $03                 
9663: 4A              LSR     A                   
9664: 4A              LSR     A                   
9665: 4A              LSR     A                   
9666: 4A              LSR     A                   
9667: 05 00           ORA     $00                 ; {ram.GP_00}
9669: 85 00           STA     $00                 ; {ram.GP_00}
966B: A0 00           LDY     #$00                
966D: B1 00           LDA     ($00),Y             ; {ram.GP_00}
966F: 60              RTS                         
9670: A5 FD           LDA     $FD                 
9672: 18              CLC                         
9673: 65 00           ADC     $00                 ; {ram.GP_00}
9675: 85 00           STA     $00                 ; {ram.GP_00}
9677: A9 00           LDA     #$00                
9679: 65 01           ADC     $01                 
967B: 85 01           STA     $01                 
967D: A5 00           LDA     $00                 ; {ram.GP_00}
967F: 18              CLC                         
9680: 65 02           ADC     $02                 
9682: 29 F0           AND     #$F0                
9684: 85 00           STA     $00                 ; {ram.GP_00}
9686: A5 01           LDA     $01                 
9688: 69 00           ADC     #$00                
968A: 85 01           STA     $01                 
968C: C9 07           CMP     #$07                
968E: B0 08           BCS     $9698               ; {}
9690: A5 00           LDA     $00                 ; {ram.GP_00}
9692: C9 E0           CMP     #$E0                
9694: B0 02           BCS     $9698               ; {}
9696: 90 C9           BCC     $9661               ; {}
9698: A5 00           LDA     $00                 ; {ram.GP_00}
969A: 38              SEC                         
969B: E9 E0           SBC     #$E0                
969D: 85 00           STA     $00                 ; {ram.GP_00}
969F: A5 01           LDA     $01                 
96A1: E9 01           SBC     #$01                
96A3: 85 01           STA     $01                 
96A5: 4C 61 96        JMP     $9661               ; {}
96A8: 20 BD 96        JSR     $96BD               ; {}
96AB: 24 5C           BIT     $5C                 
96AD: 70 07           BVS     $96B6               ; {}
96AF: BD 00 07        LDA     $0700,X             
96B2: C9 80           CMP     #$80                
96B4: 90 01           BCC     $96B7               ; {}
96B6: 60              RTS                         
96B7: FE 00 07        INC     $0700,X             
96BA: 4C 8D 97        JMP     $978D               ; {}
96BD: AD D5 04        LDA     $04D5               
96C0: C9 2A           CMP     #$2A                
96C2: F0 08           BEQ     $96CC               ; {}
96C4: AD D6 04        LDA     $04D6               
96C7: C9 2A           CMP     #$2A                
96C9: F0 01           BEQ     $96CC               ; {}
96CB: 60              RTS                         
96CC: A0 28           LDY     #$28                
96CE: A9 04           LDA     #$04                
96D0: 4C 90 CA        JMP     $CA90               
96D3: A5 1C           LDA     $1C                 
96D5: 10 15           BPL     $96EC               ; {}
96D7: AD D6 04        LDA     $04D6               
96DA: C9 50           CMP     #$50                
96DC: B0 08           BCS     $96E6               ; {}
96DE: AD D5 04        LDA     $04D5               
96E1: C9 50           CMP     #$50                
96E3: B0 04           BCS     $96E9               ; {}
96E5: 60              RTS                         
96E6: 4C 3C D0        JMP     $D03C               
96E9: 4C 40 D0        JMP     $D040               
96EC: AD D5 04        LDA     $04D5               
96EF: C9 50           CMP     #$50                
96F1: B0 08           BCS     $96FB               ; {}
96F3: AD D6 04        LDA     $04D6               
96F6: C9 50           CMP     #$50                
96F8: B0 04           BCS     $96FE               ; {}
96FA: 60              RTS                         
96FB: 4C 44 D0        JMP     $D044               
96FE: 4C 4E D0        JMP     $D04E               
9701: A5 FD           LDA     $FD                 
9703: C5 74           CMP     $74                 
9705: D0 03           BNE     $970A               ; {}
9707: 4C 42 EE        JMP     $EE42               
970A: 85 74           STA     $74                 
970C: 29 0F           AND     #$0F                
970E: C9 0D           CMP     #$0D                
9710: F0 19           BEQ     $972B               ; {}
9712: C9 0C           CMP     #$0C                
9714: F0 18           BEQ     $972E               ; {}
9716: A5 68           LDA     $68                 
9718: 0A              ASL     A                   
9719: A8              TAY                         
971A: B9 27 97        LDA     $9727,Y             ; {}
971D: 85 00           STA     $00                 ; {ram.GP_00}
971F: B9 28 97        LDA     $9728,Y             ; {}
9722: 85 01           STA     $01                 
9724: 6C 00 00        JMP     ($0000)             ; {ram.GP_00}
9727: 42 ; ????
9728: EE 31 97        INC     $9731               ; {}
972B: 4C B4 97        JMP     $97B4               ; {}
972E: 4C CE 97        JMP     $97CE               ; {}
9731: 20 49 97        JSR     $9749               ; {}
9734: A5 69           LDA     $69                 
9736: 18              CLC                         
9737: 69 20           ADC     #$20                
9739: 85 69           STA     $69                 
973B: A5 6A           LDA     $6A                 
973D: 69 00           ADC     #$00                
973F: 85 6A           STA     $6A                 
9741: 20 49 97        JSR     $9749               ; {}
9744: A9 00           LDA     #$00                
9746: 85 68           STA     $68                 
9748: 60              RTS                         
9749: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
974C: A5 6A           LDA     $6A                 
974E: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
9751: A5 69           LDA     $69                 
9753: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
9756: A9 12           LDA     #$12                
9758: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
975B: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
975E: 60              RTS                         
975F: A5 5C           LDA     $5C                 
9761: 10 FB           BPL     $975E               ; {}
9763: AD 00 01        LDA     $0100               
9766: 29 7F           AND     #$7F                
9768: 8D 00 01        STA     $0100               
976B: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
976E: 20 B9 99        JSR     $99B9               ; {}
9771: A5 5C           LDA     $5C                 
9773: 29 7F           AND     #$7F                
9775: 85 5C           STA     $5C                 
9777: AD 00 01        LDA     $0100               
977A: 09 80           ORA     #$80                
977C: 8D 00 01        STA     $0100               
977F: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
9782: 68              PLA                         
9783: 68              PLA                         
9784: 4C 95 80        JMP     $8095               ; {}
9787: A5 F3           LDA     $F3                 
9789: 29 80           AND     #$80                
978B: F0 22           BEQ     $97AF               ; {}
978D: A5 FD           LDA     $FD                 
978F: 38              SEC                         
9790: E9 01           SBC     #$01                
9792: 85 FD           STA     $FD                 
9794: A5 1A           LDA     $1A                 
9796: E9 00           SBC     #$00                
9798: 85 1A           STA     $1A                 
979A: A9 01           LDA     #$01                
979C: 85 27           STA     $27                 
979E: A5 FD           LDA     $FD                 
97A0: C9 F0           CMP     #$F0                
97A2: 90 0A           BCC     $97AE               ; {}
97A4: A9 EF           LDA     #$EF                
97A6: 85 FD           STA     $FD                 
97A8: A5 5C           LDA     $5C                 
97AA: 09 80           ORA     #$80                
97AC: 85 5C           STA     $5C                 
97AE: 60              RTS                         
97AF: A9 00           LDA     #$00                
97B1: 85 27           STA     $27                 
97B3: 60              RTS                         
97B4: AD 82 04        LDA     $0482               
97B7: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
97BA: AD 81 04        LDA     $0481               
97BD: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
97C0: A0 00           LDY     #$00                
97C2: B9 83 04        LDA     $0483,Y             
97C5: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
97C8: C8              INY                         
97C9: C0 40           CPY     #$40                
97CB: 90 F5           BCC     $97C2               ; {}
97CD: 60              RTS                         
97CE: 20 5D 99        JSR     $995D               ; {}
97D1: A5 00           LDA     $00                 ; {ram.GP_00}
97D3: 18              CLC                         
97D4: 69 C0           ADC     #$C0                
97D6: 85 01           STA     $01                 
97D8: A9 23           LDA     #$23                
97DA: 85 02           STA     $02                 
97DC: A5 1A           LDA     $1A                 
97DE: 29 01           AND     #$01                
97E0: D0 04           BNE     $97E6               ; {}
97E2: A9 2B           LDA     #$2B                
97E4: 85 02           STA     $02                 
97E6: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
97E9: A5 02           LDA     $02                 
97EB: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
97EE: A5 01           LDA     $01                 
97F0: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
97F3: 20 5D 99        JSR     $995D               ; {}
97F6: AA              TAX                         
97F7: A0 07           LDY     #$07                
97F9: BD B0 03        LDA     $03B0,X             
97FC: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
97FF: E8              INX                         
9800: 88              DEY                         
9801: 10 F6           BPL     $97F9               ; {}
9803: 60              RTS                         
9804: A5 FD           LDA     $FD                 
9806: 29 F0           AND     #$F0                
9808: 85 08           STA     $08                 
980A: A9 00           LDA     #$00                
980C: 85 01           STA     $01                 
980E: A5 08           LDA     $08                 
9810: 85 00           STA     $00                 ; {ram.GP_00}
9812: 06 00           ASL     $00                 ; {ram.GP_00}
9814: 26 01           ROL     $01                 
9816: 06 00           ASL     $00                 ; {ram.GP_00}
9818: 26 01           ROL     $01                 
981A: A9 00           LDA     #$00                
981C: 18              CLC                         
981D: 65 00           ADC     $00                 ; {ram.GP_00}
981F: 8D 81 04        STA     $0481               
9822: A9 20           LDA     #$20                
9824: 65 01           ADC     $01                 
9826: 8D 82 04        STA     $0482               
9829: A5 1A           LDA     $1A                 
982B: 29 01           AND     #$01                
982D: D0 09           BNE     $9838               ; {}
982F: AD 82 04        LDA     $0482               
9832: 18              CLC                         
9833: 69 08           ADC     #$08                
9835: 8D 82 04        STA     $0482               
9838: 20 4E 98        JSR     $984E               ; {}
983B: 20 59 98        JSR     $9859               ; {}
983E: A5 08           LDA     $08                 
9840: 18              CLC                         
9841: 65 62           ADC     $62                 
9843: 85 06           STA     $06                 
9845: A9 00           LDA     #$00                
9847: 65 63           ADC     $63                 
9849: 85 07           STA     $07                 
984B: 4C 6B 98        JMP     $986B               ; {}
984E: A5 1A           LDA     $1A                 
9850: 49 FF           EOR     #$FF                
9852: 8D D1 04        STA     $04D1               
9855: EE D1 04        INC     $04D1               
9858: 60              RTS                         
9859: AD D1 04        LDA     $04D1               
985C: 29 01           AND     #$01                
985E: 0A              ASL     A                   
985F: A8              TAY                         
9860: B9 1B 77        LDA     $771B,Y             
9863: 85 62           STA     $62                 
9865: B9 1C 77        LDA     $771C,Y             
9868: 85 63           STA     $63                 
986A: 60              RTS                         
986B: A0 0F           LDY     #$0F                
986D: 98              TYA                         
986E: 48              PHA                         
986F: B1 06           LDA     ($06),Y             
9871: 20 99 98        JSR     $9899               ; {}
9874: 68              PLA                         
9875: 48              PHA                         
9876: 0A              ASL     A                   
9877: A8              TAY                         
9878: A5 02           LDA     $02                 
987A: 99 83 04        STA     $0483,Y             
987D: C8              INY                         
987E: A5 03           LDA     $03                 
9880: 99 83 04        STA     $0483,Y             
9883: 98              TYA                         
9884: 18              CLC                         
9885: 69 1F           ADC     #$1F                
9887: A8              TAY                         
9888: A5 04           LDA     $04                 
988A: 99 83 04        STA     $0483,Y             
988D: C8              INY                         
988E: A5 05           LDA     $05                 
9890: 99 83 04        STA     $0483,Y             
9893: 68              PLA                         
9894: A8              TAY                         
9895: 88              DEY                         
9896: 10 D5           BPL     $986D               ; {}
9898: 60              RTS                         
9899: 85 00           STA     $00                 ; {ram.GP_00}
989B: A9 00           LDA     #$00                
989D: 85 01           STA     $01                 
989F: A0 03           LDY     #$03                
98A1: 06 00           ASL     $00                 ; {ram.GP_00}
98A3: 26 01           ROL     $01                 
98A5: 06 00           ASL     $00                 ; {ram.GP_00}
98A7: 26 01           ROL     $01                 
98A9: A5 3A           LDA     $3A                 
98AB: C9 10           CMP     #$10                
98AD: B0 16           BCS     $98C5               ; {}
98AF: A5 00           LDA     $00                 ; {ram.GP_00}
98B1: 18              CLC                         
98B2: 69 D7           ADC     #$D7                
98B4: 85 00           STA     $00                 ; {ram.GP_00}
98B6: A5 01           LDA     $01                 
98B8: 69 74           ADC     #$74                
98BA: 85 01           STA     $01                 
98BC: B1 00           LDA     ($00),Y             ; {ram.GP_00}
98BE: 99 02 00        STA     $0002,Y             
98C1: 88              DEY                         
98C2: 10 F8           BPL     $98BC               ; {}
98C4: 60              RTS                         
98C5: A5 00           LDA     $00                 ; {ram.GP_00}
98C7: 18              CLC                         
98C8: 69 D7           ADC     #$D7                
98CA: 85 00           STA     $00                 ; {ram.GP_00}
98CC: A5 01           LDA     $01                 
98CE: 69 74           ADC     #$74                
98D0: 85 01           STA     $01                 
98D2: 4C BC 98        JMP     $98BC               ; {}
98D5: 20 4E 98        JSR     $984E               ; {}
98D8: 20 4B 99        JSR     $994B               ; {}
98DB: 20 5D 99        JSR     $995D               ; {}
98DE: A2 00           LDX     #$00                
98E0: 18              CLC                         
98E1: 8A              TXA                         
98E2: 65 00           ADC     $00                 ; {ram.GP_00}
98E4: A8              TAY                         
98E5: B1 64           LDA     ($64),Y             
98E7: 9D F0 03        STA     $03F0,X             
98EA: E8              INX                         
98EB: E0 08           CPX     #$08                
98ED: 90 F1           BCC     $98E0               ; {}
98EF: A5 FD           LDA     $FD                 
98F1: 29 10           AND     #$10                
98F3: F0 2B           BEQ     $9920               ; {}
98F5: A0 00           LDY     #$00                
98F7: 18              CLC                         
98F8: 98              TYA                         
98F9: 65 00           ADC     $00                 ; {ram.GP_00}
98FB: 85 01           STA     $01                 
98FD: 98              TYA                         
98FE: AA              TAX                         
98FF: BD F0 03        LDA     $03F0,X             
9902: 29 F0           AND     #$F0                
9904: 85 02           STA     $02                 
9906: A5 01           LDA     $01                 
9908: AA              TAX                         
9909: BD B0 03        LDA     $03B0,X             
990C: 29 0F           AND     #$0F                
990E: 05 02           ORA     $02                 
9910: 85 02           STA     $02                 
9912: A5 01           LDA     $01                 
9914: AA              TAX                         
9915: A5 02           LDA     $02                 
9917: 9D B0 03        STA     $03B0,X             
991A: C8              INY                         
991B: C0 08           CPY     #$08                
991D: 90 D8           BCC     $98F7               ; {}
991F: 60              RTS                         
9920: A0 00           LDY     #$00                
9922: 18              CLC                         
9923: 98              TYA                         
9924: 65 00           ADC     $00                 ; {ram.GP_00}
9926: 85 01           STA     $01                 
9928: 98              TYA                         
9929: AA              TAX                         
992A: BD F0 03        LDA     $03F0,X             
992D: 29 0F           AND     #$0F                
992F: 85 02           STA     $02                 
9931: A5 01           LDA     $01                 
9933: AA              TAX                         
9934: BD B0 03        LDA     $03B0,X             
9937: 29 F0           AND     #$F0                
9939: 05 02           ORA     $02                 
993B: 85 02           STA     $02                 
993D: A5 01           LDA     $01                 
993F: AA              TAX                         
9940: A5 02           LDA     $02                 
9942: 9D B0 03        STA     $03B0,X             
9945: C8              INY                         
9946: C0 08           CPY     #$08                
9948: 90 D8           BCC     $9922               ; {}
994A: 60              RTS                         
994B: AD D1 04        LDA     $04D1               
994E: 29 01           AND     #$01                
9950: 0A              ASL     A                   
9951: A8              TAY                         
9952: B9 23 77        LDA     $7723,Y             
9955: 85 64           STA     $64                 
9957: B9 24 77        LDA     $7724,Y             
995A: 85 65           STA     $65                 
995C: 60              RTS                         
995D: A5 FD           LDA     $FD                 
995F: 29 E0           AND     #$E0                
9961: 4A              LSR     A                   
9962: 4A              LSR     A                   
9963: 85 00           STA     $00                 ; {ram.GP_00}
9965: 60              RTS                         
9966: 20 4E 98        JSR     $984E               ; {}
9969: A9 00           LDA     #$00                
996B: 85 5C           STA     $5C                 
996D: 8D D2 04        STA     $04D2               
9970: 20 D6 99        JSR     $99D6               ; {}
9973: A9 06           LDA     #$06                
9975: 20 90 CA        JSR     $CA90               
9978: A9 00           LDA     #$00                
997A: 8D D2 04        STA     $04D2               
997D: EE D1 04        INC     $04D1               
9980: 20 D9 99        JSR     $99D9               ; {}
9983: A9 06           LDA     #$06                
9985: 20 90 CA        JSR     $CA90               
9988: 20 C1 99        JSR     $99C1               ; {}
998B: A9 FF           LDA     #$FF                
998D: 85 1A           STA     $1A                 
998F: A9 EE           LDA     #$EE                
9991: 85 FD           STA     $FD                 
9993: 20 04 98        JSR     $9804               ; {}
9996: 20 D5 98        JSR     $98D5               ; {}
9999: 20 B4 97        JSR     $97B4               ; {}
999C: 20 CE 97        JSR     $97CE               ; {}
999F: A5 FD           LDA     $FD                 
99A1: 38              SEC                         
99A2: E9 10           SBC     #$10                
99A4: 85 FD           STA     $FD                 
99A6: A5 1A           LDA     $1A                 
99A8: E9 00           SBC     #$00                
99AA: 85 1A           STA     $1A                 
99AC: C9 FE           CMP     #$FE                
99AE: B0 E3           BCS     $9993               ; {}
99B0: A9 FF           LDA     #$FF                
99B2: 85 1A           STA     $1A                 
99B4: A9 EE           LDA     #$EE                
99B6: 85 FD           STA     $FD                 
99B8: 60              RTS                         
99B9: 20 D6 99        JSR     $99D6               ; {}
99BC: A9 06           LDA     #$06                
99BE: 20 90 CA        JSR     $CA90               
99C1: A0 0F           LDY     #$0F                
99C3: B9 00 05        LDA     $0500,Y             
99C6: 99 E0 06        STA     $06E0,Y             
99C9: 88              DEY                         
99CA: 10 F7           BPL     $99C3               ; {}
99CC: 60              RTS                         
99CD: A5 5C           LDA     $5C                 
99CF: 09 40           ORA     #$40                
99D1: 85 5C           STA     $5C                 
99D3: 68              PLA                         
99D4: 68              PLA                         
99D5: 60              RTS                         
99D6: 20 4E 98        JSR     $984E               ; {}
99D9: A9 00           LDA     #$00                
99DB: 8D D2 04        STA     $04D2               
99DE: AD 30 01        LDA     $0130               
99E1: 0A              ASL     A                   
99E2: A8              TAY                         
99E3: B9 2B 77        LDA     $772B,Y             
99E6: 85 00           STA     $00                 ; {ram.GP_00}
99E8: B9 2C 77        LDA     $772C,Y             
99EB: 85 01           STA     $01                 
99ED: AD D1 04        LDA     $04D1               
99F0: 0A              ASL     A                   
99F1: A8              TAY                         
99F2: B1 00           LDA     ($00),Y             ; {ram.GP_00}
99F4: 85 49           STA     $49                 
99F6: C8              INY                         
99F7: B1 00           LDA     ($00),Y             ; {ram.GP_00}
99F9: C9 FF           CMP     #$FF                
99FB: F0 D0           BEQ     $99CD               ; {}
99FD: 85 4A           STA     $4A                 
99FF: 20 59 98        JSR     $9859               ; {}
9A02: 20 4B 99        JSR     $994B               ; {}
9A05: 4C 25 9A        JMP     $9A25               ; {}
9A08: AD D1 04        LDA     $04D1               
9A0B: 0A              ASL     A                   
9A0C: A8              TAY                         
9A0D: B9 31 77        LDA     $7731,Y             
9A10: 85 49           STA     $49                 
9A12: B9 32 77        LDA     $7732,Y             
9A15: 85 4A           STA     $4A                 
9A17: A5 3A           LDA     $3A                 
9A19: C9 10           CMP     #$10                
9A1B: 90 E2           BCC     $99FF               ; {}
9A1D: A0 00           LDY     #$00                
9A1F: 20 60 98        JSR     $9860               ; {}
9A22: 20 52 99        JSR     $9952               ; {}
9A25: 20 FF 9A        JSR     $9AFF               ; {}
9A28: A0 00           LDY     #$00                
9A2A: B1 49           LDA     ($49),Y             
9A2C: 20 0A 9B        JSR     $9B0A               ; {}
9A2F: A0 01           LDY     #$01                
9A31: B1 49           LDA     ($49),Y             
9A33: C9 FD           CMP     #$FD                
9A35: F0 17           BEQ     $9A4E               ; {}
9A37: 85 4D           STA     $4D                 
9A39: C8              INY                         
9A3A: B1 49           LDA     ($49),Y             
9A3C: 85 4E           STA     $4E                 
9A3E: C8              INY                         
9A3F: B1 49           LDA     ($49),Y             
9A41: 85 4F           STA     $4F                 
9A43: 98              TYA                         
9A44: 48              PHA                         
9A45: 20 4F 9A        JSR     $9A4F               ; {}
9A48: 68              PLA                         
9A49: A8              TAY                         
9A4A: C8              INY                         
9A4B: 4C 31 9A        JMP     $9A31               ; {}
9A4E: 60              RTS                         
9A4F: 20 9B 9A        JSR     $9A9B               ; {}
9A52: A9 00           LDA     #$00                
9A54: 85 5F           STA     $5F                 
9A56: A5 4D           LDA     $4D                 
9A58: 29 F0           AND     #$F0                
9A5A: 85 61           STA     $61                 
9A5C: A5 5F           LDA     $5F                 
9A5E: 0A              ASL     A                   
9A5F: 0A              ASL     A                   
9A60: 0A              ASL     A                   
9A61: 0A              ASL     A                   
9A62: 18              CLC                         
9A63: 65 61           ADC     $61                 
9A65: C9 F0           CMP     #$F0                
9A67: B0 31           BCS     $9A9A               ; {}
9A69: A0 00           LDY     #$00                
9A6B: B1 51           LDA     ($51),Y             
9A6D: C9 FF           CMP     #$FF                
9A6F: F0 29           BEQ     $9A9A               ; {}
9A71: 85 53           STA     $53                 
9A73: 29 0F           AND     #$0F                
9A75: AA              TAX                         
9A76: C8              INY                         
9A77: B1 51           LDA     ($51),Y             
9A79: 99 53 00        STA     $0053,Y             
9A7C: C8              INY                         
9A7D: CA              DEX                         
9A7E: D0 F7           BNE     $9A77               ; {}
9A80: 20 1C 9B        JSR     $9B1C               ; {}
9A83: A5 53           LDA     $53                 
9A85: 29 0F           AND     #$0F                
9A87: 38              SEC                         
9A88: 65 51           ADC     $51                 
9A8A: 85 51           STA     $51                 
9A8C: A9 00           LDA     #$00                
9A8E: 65 52           ADC     $52                 
9A90: 85 52           STA     $52                 
9A92: 20 BB 9A        JSR     $9ABB               ; {}
9A95: E6 5F           INC     $5F                 
9A97: 4C 56 9A        JMP     $9A56               ; {}
9A9A: 60              RTS                         
9A9B: A5 4E           LDA     $4E                 
9A9D: 0A              ASL     A                   
9A9E: A8              TAY                         
9A9F: A5 3A           LDA     $3A                 
9AA1: C9 10           CMP     #$10                
9AA3: B0 0B           BCS     $9AB0               ; {}
9AA5: B9 AD 77        LDA     $77AD,Y             
9AA8: 85 51           STA     $51                 
9AAA: B9 AE 77        LDA     $77AE,Y             
9AAD: 85 52           STA     $52                 
9AAF: 60              RTS                         
9AB0: B9 AD 77        LDA     $77AD,Y             
9AB3: 85 51           STA     $51                 
9AB5: B9 AE 77        LDA     $77AE,Y             
9AB8: 85 52           STA     $52                 
9ABA: 60              RTS                         
9ABB: A5 5F           LDA     $5F                 
9ABD: 0A              ASL     A                   
9ABE: 0A              ASL     A                   
9ABF: 0A              ASL     A                   
9AC0: 0A              ASL     A                   
9AC1: 85 5D           STA     $5D                 
9AC3: A5 53           LDA     $53                 
9AC5: 29 F0           AND     #$F0                
9AC7: 4A              LSR     A                   
9AC8: 4A              LSR     A                   
9AC9: 4A              LSR     A                   
9ACA: 4A              LSR     A                   
9ACB: 18              CLC                         
9ACC: 65 5D           ADC     $5D                 
9ACE: 85 5D           STA     $5D                 
9AD0: 18              CLC                         
9AD1: A5 4D           LDA     $4D                 
9AD3: 65 5D           ADC     $5D                 
9AD5: 85 5D           STA     $5D                 
9AD7: A5 53           LDA     $53                 
9AD9: 29 0F           AND     #$0F                
9ADB: AA              TAX                         
9ADC: 18              CLC                         
9ADD: A5 62           LDA     $62                 
9ADF: 65 5D           ADC     $5D                 
9AE1: 85 5D           STA     $5D                 
9AE3: A9 00           LDA     #$00                
9AE5: 65 63           ADC     $63                 
9AE7: 85 5E           STA     $5E                 
9AE9: A0 00           LDY     #$00                
9AEB: B9 54 00        LDA     $0054,Y             
9AEE: 91 5D           STA     ($5D),Y             
9AF0: 98              TYA                         
9AF1: 18              CLC                         
9AF2: 65 5D           ADC     $5D                 
9AF4: 29 0F           AND     #$0F                
9AF6: C9 0F           CMP     #$0F                
9AF8: B0 04           BCS     $9AFE               ; {}
9AFA: C8              INY                         
9AFB: CA              DEX                         
9AFC: D0 ED           BNE     $9AEB               ; {}
9AFE: 60              RTS                         
9AFF: A0 00           LDY     #$00                
9B01: 98              TYA                         
9B02: 91 62           STA     ($62),Y             
9B04: C8              INY                         
9B05: C0 F0           CPY     #$F0                
9B07: 90 F9           BCC     $9B02               ; {}
9B09: 60              RTS                         
9B0A: 29 03           AND     #$03                
9B0C: A8              TAY                         
9B0D: B9 18 9B        LDA     $9B18,Y             ; {}
9B10: A0 40           LDY     #$40                
9B12: 91 64           STA     ($64),Y             
9B14: 88              DEY                         
9B15: 10 FB           BPL     $9B12               ; {}
9B17: 60              RTS                         
9B18: 00              BRK                         
9B19: 55 AA           EOR     $AA,X               
9B1B: FF ; ????
9B1C: A5 53           LDA     $53                 
9B1E: 29 F0           AND     #$F0                
9B20: 4A              LSR     A                   
9B21: 4A              LSR     A                   
9B22: 4A              LSR     A                   
9B23: 4A              LSR     A                   
9B24: 8D D0 04        STA     $04D0               
9B27: A5 53           LDA     $53                 
9B29: 29 0F           AND     #$0F                
9B2B: 18              CLC                         
9B2C: 6D D0 04        ADC     $04D0               
9B2F: 8D D0 04        STA     $04D0               
9B32: A5 4D           LDA     $4D                 
9B34: 29 0F           AND     #$0F                
9B36: 8D CD 04        STA     $04CD               
9B39: 18              CLC                         
9B3A: 6D D0 04        ADC     $04D0               
9B3D: C9 10           CMP     #$10                
9B3F: 90 09           BCC     $9B4A               ; {}
9B41: A9 10           LDA     #$10                
9B43: 38              SEC                         
9B44: ED CD 04        SBC     $04CD               
9B47: 8D D0 04        STA     $04D0               
9B4A: A9 00           LDA     #$00                
9B4C: 8D CD 04        STA     $04CD               
9B4F: A5 5F           LDA     $5F                 
9B51: 0A              ASL     A                   
9B52: 0A              ASL     A                   
9B53: 0A              ASL     A                   
9B54: 0A              ASL     A                   
9B55: 18              CLC                         
9B56: 65 4D           ADC     $4D                 
9B58: 18              CLC                         
9B59: 6D CD 04        ADC     $04CD               
9B5C: 85 60           STA     $60                 
9B5E: 29 E0           AND     #$E0                
9B60: 4A              LSR     A                   
9B61: 4A              LSR     A                   
9B62: 85 66           STA     $66                 
9B64: A5 60           LDA     $60                 
9B66: 29 0F           AND     #$0F                
9B68: 4A              LSR     A                   
9B69: 18              CLC                         
9B6A: 65 66           ADC     $66                 
9B6C: 18              CLC                         
9B6D: 65 64           ADC     $64                 
9B6F: 85 66           STA     $66                 
9B71: A9 00           LDA     #$00                
9B73: 65 65           ADC     $65                 
9B75: 85 67           STA     $67                 
9B77: A5 60           LDA     $60                 
9B79: 29 10           AND     #$10                
9B7B: 4A              LSR     A                   
9B7C: 4A              LSR     A                   
9B7D: 4A              LSR     A                   
9B7E: 8D CE 04        STA     $04CE               
9B81: A5 60           LDA     $60                 
9B83: 29 01           AND     #$01                
9B85: 0D CE 04        ORA     $04CE               
9B88: F0 0E           BEQ     $9B98               ; {}
9B8A: AA              TAX                         
9B8B: A9 03           LDA     #$03                
9B8D: 0A              ASL     A                   
9B8E: 0A              ASL     A                   
9B8F: CA              DEX                         
9B90: 8D CE 04        STA     $04CE               
9B93: F0 08           BEQ     $9B9D               ; {}
9B95: 4C 8D 9B        JMP     $9B8D               ; {}
9B98: A9 03           LDA     #$03                
9B9A: 8D CE 04        STA     $04CE               
9B9D: AD CE 04        LDA     $04CE               
9BA0: 49 FF           EOR     #$FF                
9BA2: A0 00           LDY     #$00                
9BA4: 31 66           AND     ($66),Y             
9BA6: 8D CF 04        STA     $04CF               
9BA9: A5 4F           LDA     $4F                 
9BAB: 29 02           AND     #$02                
9BAD: F0 0B           BEQ     $9BBA               ; {}
9BAF: A9 AA           LDA     #$AA                
9BB1: 2D CE 04        AND     $04CE               
9BB4: 0D CF 04        ORA     $04CF               
9BB7: 8D CF 04        STA     $04CF               
9BBA: A5 4F           LDA     $4F                 
9BBC: 29 01           AND     #$01                
9BBE: F0 0B           BEQ     $9BCB               ; {}
9BC0: A9 55           LDA     #$55                
9BC2: 2D CE 04        AND     $04CE               
9BC5: 0D CF 04        ORA     $04CF               
9BC8: 8D CF 04        STA     $04CF               
9BCB: AD CF 04        LDA     $04CF               
9BCE: 91 66           STA     ($66),Y             
9BD0: EE CD 04        INC     $04CD               
9BD3: AD CD 04        LDA     $04CD               
9BD6: CD D0 04        CMP     $04D0               
9BD9: B0 03           BCS     $9BDE               ; {}
9BDB: 4C 4F 9B        JMP     $9B4F               ; {}
9BDE: 60              RTS                         
9BDF: A9 10           LDA     #$10                
9BE1: 85 0A           STA     $0A                 
9BE3: E6 1A           INC     $1A                 
9BE5: 20 04 98        JSR     $9804               ; {}
9BE8: 20 D5 98        JSR     $98D5               ; {}
9BEB: 20 B4 97        JSR     $97B4               ; {}
9BEE: 20 CE 97        JSR     $97CE               ; {}
9BF1: A5 FD           LDA     $FD                 
9BF3: 38              SEC                         
9BF4: E9 10           SBC     #$10                
9BF6: 85 FD           STA     $FD                 
9BF8: A5 1A           LDA     $1A                 
9BFA: E9 00           SBC     #$00                
9BFC: 85 1A           STA     $1A                 
9BFE: C6 0A           DEC     $0A                 
9C00: 10 E3           BPL     $9BE5               ; {}
9C02: A5 FD           LDA     $FD                 
9C04: 18              CLC                         
9C05: 69 10           ADC     #$10                
9C07: 85 FD           STA     $FD                 
9C09: A5 1A           LDA     $1A                 
9C0B: 69 00           ADC     #$00                
9C0D: 85 1A           STA     $1A                 
9C0F: 60              RTS                         
9C10: FF ; ????
9C11: FF ; ????
9C12: FF ; ????
9C13: FF ; ????
9C14: FF ; ????
9C15: FF ; ????
9C16: FF ; ????
9C17: EF ; ????
9C18: FF ; ????
9C19: FF ; ????
9C1A: FF ; ????
9C1B: FF ; ????
9C1C: FF ; ????
9C1D: FF ; ????
9C1E: FF ; ????
9C1F: FF ; ????
9C20: FF ; ????
9C21: FF ; ????
9C22: FF ; ????
9C23: FF ; ????
9C24: FF ; ????
9C25: FF ; ????
9C26: FF ; ????
9C27: FF ; ????
9C28: FF ; ????
9C29: FF ; ????
9C2A: FF ; ????
9C2B: FF ; ????
9C2C: FF ; ????
9C2D: FF ; ????
9C2E: FF ; ????
9C2F: FD 4C 8A        SBC     $8A4C,X             ; {}
9C32: 9C ; ????
9C33: 4C 0B 9D        JMP     $9D0B               ; {}
9C36: 4C FD B7        JMP     $B7FD               ; {}
9C39: 4C 40 DF        JMP     $DF40               
9C3C: 4C 5E B5        JMP     $B55E               ; {}
9C3F: 4C A2 B5        JMP     $B5A2               ; {}
9C42: 4C DD B4        JMP     $B4DD               ; {}
9C45: 4C FB 9C        JMP     $9CFB               ; {}
9C48: 4C 4B BA        JMP     $BA4B               ; {}
9C4B: 4C 85 A0        JMP     $A085               ; {}
9C4E: 4C FB 9C        JMP     $9CFB               ; {}
9C51: 4C C3 B4        JMP     $B4C3               ; {}
9C54: 4C CE 9C        JMP     $9CCE               ; {}
9C57: 4C 64 9E        JMP     $9E64               ; {}
9C5A: 4C B9 9D        JMP     $9DB9               ; {}
9C5D: 4C 49 B8        JMP     $B849               ; {}
9C60: 4C 93 B8        JMP     $B893               ; {}
9C63: 4C BD B6        JMP     $B6BD               ; {}
9C66: 4C 6C B7        JMP     $B76C               ; {}
9C69: 4C 35 B6        JMP     $B635               ; {}
9C6C: 4C 89 B6        JMP     $B689               ; {}
9C6F: 4C 58 A0        JMP     $A058               ; {}
9C72: 67 ; ????
9C73: C5 E7           CMP     $E7                 
9C75: C5 78           CMP     $78                 
9C77: 9E ; ????
9C78: D8              CLD                         
9C79: 9E ; ????
9C7A: 00              BRK                         
9C7B: 9F ; ????
9C7C: 28              PLP                         
9C7D: 9F ; ????
9C7E: 48              PHA                         
9C7F: 9F ; ????
9C80: 58              CLI                         
9C81: 9F ; ????
9C82: 58              CLI                         
9C83: 9F ; ????
9C84: 88              DEY                         
9C85: 9F ; ????
9C86: 7F ; ????
9C87: F0 64           BEQ     $9CED               ; {}
9C89: BF ; ????
9C8A: 20 1D EB        JSR     $EB1D               
9C8D: 20 F0 EE        JSR     $EEF0               
9C90: 24 AB           BIT     $AB                 
9C92: 70 03           BVS     $9C97               ; {}
9C94: 4C 3B AC        JMP     $AC3B               ; {}
9C97: AD 70 01        LDA     $0170               
9C9A: 85 AA           STA     $AA                 
9C9C: 20 2E 9E        JSR     $9E2E               ; {}
9C9F: 20 21 7F        JSR     $7F21               
9CA2: 20 E5 EE        JSR     $EEE5               
9CA5: A9 00           LDA     #$00                
9CA7: 8D 30 01        STA     $0130               
9CAA: 20 01 EB        JSR     $EB01               
9CAD: 20 2A C4        JSR     $C42A               
9CB0: 20 20 EF        JSR     $EF20               
9CB3: 20 21 7F        JSR     $7F21               
9CB6: 20 42 EE        JSR     $EE42               
9CB9: 20 2E EF        JSR     $EF2E               
9CBC: 20 CA EE        JSR     $EECA               
9CBF: 20 E5 EE        JSR     $EEE5               
9CC2: 20 B9 9D        JSR     $9DB9               ; {}
9CC5: 20 2E 9E        JSR     $9E2E               ; {}
9CC8: 20 3D C8        JSR     $C83D               
9CCB: 20 70 CB        JSR     $CB70               
9CCE: A9 60           LDA     #$60                
9CD0: 85 43           STA     $43                 
9CD2: 20 01 EF        JSR     $EF01               
9CD5: 20 21 EB        JSR     $EB21               
9CD8: 24 AB           BIT     $AB                 
9CDA: 70 0B           BVS     $9CE7               ; {}
9CDC: 30 0C           BMI     $9CEA               ; {}
9CDE: 20 98 E1        JSR     $E198               
9CE1: 20 E6 B5        JSR     $B5E6               ; {}
9CE4: 4C D5 9C        JMP     $9CD5               ; {}
9CE7: 4C A0 C0        JMP     $C0A0               
9CEA: 20 F0 EE        JSR     $EEF0               
9CED: 20 89 EA        JSR     $EA89               
9CF0: A9 09           LDA     #$09                
9CF2: 85 A0           STA     $A0                 
9CF4: A9 00           LDA     #$00                
9CF6: 85 38           STA     $38                 
9CF8: 4C 6D C0        JMP     $C06D               
9CFB: 60              RTS                         
9CFC: 20 9B EE        JSR     $EE9B               
9CFF: 20 0E EE        JSR     $EE0E               
9D02: 20 B8 EE        JSR     $EEB8               
9D05: 4C 52 9D        JMP     $9D52               ; {}
9D08: 4C 6D 9D        JMP     $9D6D               ; {}
9D0B: 8A              TXA                         
9D0C: 48              PHA                         
9D0D: 98              TYA                         
9D0E: 48              PHA                         
9D0F: A5 45           LDA     $45                 
9D11: D0 F5           BNE     $9D08               ; {}
9D13: E6 45           INC     $45                 
9D15: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
9D18: 20 2E EB        JSR     $EB2E               
9D1B: A5 38           LDA     $38                 
9D1D: D0 DD           BNE     $9CFC               ; {}
9D1F: A5 37           LDA     $37                 
9D21: D0 4F           BNE     $9D72               ; {}
9D23: A9 00           LDA     #$00                
9D25: 8D 01 20        STA     $2001               ; {hard.P_CNTRL_2}
9D28: 20 A3 B5        JSR     $B5A3               ; {}
9D2B: AD D1 04        LDA     $04D1               
9D2E: C9 0F           CMP     #$0F                
9D30: 90 06           BCC     $9D38               ; {}
9D32: 20 42 EE        JSR     $EE42               
9D35: 4C 3B 9D        JMP     $9D3B               ; {}
9D38: 20 C9 EB        JSR     $EBC9               
9D3B: A5 FF           LDA     $FF                 
9D3D: 8D 01 20        STA     $2001               ; {hard.P_CNTRL_2}
9D40: 20 BD B6        JSR     $B6BD               ; {}
9D43: 20 6C B7        JSR     $B76C               ; {}
9D46: 20 9B EE        JSR     $EE9B               
9D49: 20 C9 9D        JSR     $9DC9               ; {}
9D4C: 20 D9 EC        JSR     $ECD9               
9D4F: 20 B8 EE        JSR     $EEB8               
9D52: 20 5D E1        JSR     $E15D               
9D55: 20 E0 C3        JSR     $C3E0               
9D58: 20 6A EE        JSR     $EE6A               
9D5B: 20 94 EE        JSR     $EE94               
9D5E: AD 80 03        LDA     $0380               
9D61: 29 FB           AND     #$FB                
9D63: 8D 80 03        STA     $0380               
9D66: 20 56 C8        JSR     $C856               
9D69: A9 00           LDA     #$00                
9D6B: 85 45           STA     $45                 
9D6D: 68              PLA                         
9D6E: A8              TAY                         
9D6F: 68              PLA                         
9D70: AA              TAX                         
9D71: 60              RTS                         
9D72: 4A              LSR     A                   
9D73: B0 DD           BCS     $9D52               ; {}
9D75: 4A              LSR     A                   
9D76: B0 0A           BCS     $9D82               ; {}
9D78: 24 37           BIT     $37                 
9D7A: 70 24           BVS     $9DA0               ; {}
9D7C: 20 42 EE        JSR     $EE42               
9D7F: 4C 38 9D        JMP     $9D38               ; {}
9D82: A9 0A           LDA     #$0A                
9D84: 20 90 CA        JSR     $CA90               
9D87: A9 0C           LDA     #$0C                
9D89: 20 90 CA        JSR     $CA90               
9D8C: 20 C9 EB        JSR     $EBC9               
9D8F: 20 9B EE        JSR     $EE9B               
9D92: A9 02           LDA     #$02                
9D94: 20 90 CA        JSR     $CA90               
9D97: 20 D9 EC        JSR     $ECD9               
9D9A: 20 B8 EE        JSR     $EEB8               
9D9D: 4C 52 9D        JMP     $9D52               ; {}
9DA0: A9 0A           LDA     #$0A                
9DA2: 20 90 CA        JSR     $CA90               
9DA5: 20 42 EE        JSR     $EE42               
9DA8: 20 F9 E3        JSR     $E3F9               
9DAB: 20 B5 B1        JSR     $B1B5               ; {}
9DAE: A9 0E           LDA     #$0E                
9DB0: 20 90 CA        JSR     $CA90               
9DB3: 20 BC AC        JSR     $ACBC               ; {}
9DB6: 4C 58 9D        JMP     $9D58               ; {}
9DB9: 20 64 9E        JSR     $9E64               ; {}
9DBC: 20 43 D3        JSR     $D343               
9DBF: 20 9F A7        JSR     $A79F               ; {}
9DC2: 20 01 A2        JSR     $A201               ; {}
9DC5: 20 87 AB        JSR     $AB87               ; {}
9DC8: 60              RTS                         
9DC9: A9 FF           LDA     #$FF                
9DCB: 85 A7           STA     $A7                 
9DCD: A5 81           LDA     $81                 
9DCF: C9 04           CMP     #$04                
9DD1: 90 04           BCC     $9DD7               ; {}
9DD3: A9 01           LDA     #$01                
9DD5: 85 16           STA     $16                 
9DD7: 20 F9 E3        JSR     $E3F9               
9DDA: 20 B6 CB        JSR     $CBB6               
9DDD: 20 D9 C3        JSR     $C3D9               
9DE0: AD 21 07        LDA     $0721               
9DE3: 29 70           AND     #$70                
9DE5: D0 19           BNE     $9E00               ; {}
9DE7: 20 A2 D4        JSR     $D4A2               
9DEA: A5 81           LDA     $81                 
9DEC: D0 29           BNE     $9E17               ; {}
9DEE: AD D1 04        LDA     $04D1               
9DF1: C9 0E           CMP     #$0E                
9DF3: B0 0C           BCS     $9E01               ; {}
9DF5: 20 A0 A7        JSR     $A7A0               ; {}
9DF8: 20 02 A2        JSR     $A202               ; {}
9DFB: A2 F0           LDX     #$F0                
9DFD: 20 3C A6        JSR     $A63C               ; {}
9E00: 60              RTS                         
9E01: A5 FE           LDA     $FE                 
9E03: C9 02           CMP     #$02                
9E05: F0 13           BEQ     $9E1A               ; {}
9E07: C9 FC           CMP     #$FC                
9E09: 90 16           BCC     $9E21               ; {}
9E0B: E6 81           INC     $81                 
9E0D: A9 00           LDA     #$00                
9E0F: 85 14           STA     $14                 
9E11: 20 98 AC        JSR     $AC98               ; {}
9E14: 20 6F AC        JSR     $AC6F               ; {}
9E17: 4C 50 AD        JMP     $AD50               ; {}
9E1A: A9 10           LDA     #$10                
9E1C: 8D 85 03        STA     $0385               
9E1F: D0 D4           BNE     $9DF5               ; {}
9E21: AD 23 07        LDA     $0723               
9E24: C9 B8           CMP     #$B8                
9E26: 90 03           BCC     $9E2B               ; {}
9E28: CE 23 07        DEC     $0723               
9E2B: 4C F5 9D        JMP     $9DF5               ; {}
9E2E: A9 00           LDA     #$00                
9E30: 85 38           STA     $38                 
9E32: 85 3C           STA     $3C                 
9E34: 85 81           STA     $81                 
9E36: 85 C9           STA     $C9                 
9E38: A9 03           LDA     #$03                
9E3A: 8D 2F 01        STA     $012F               
9E3D: A9 02           LDA     #$02                
9E3F: 8D 3F 01        STA     $013F               
9E42: A9 0A           LDA     #$0A                
9E44: 85 A5           STA     $A5                 
9E46: A9 8A           LDA     #$8A                
9E48: 8D 21 07        STA     $0721               
9E4B: A9 02           LDA     #$02                
9E4D: 8D 53 01        STA     $0153               
9E50: 8D 54 01        STA     $0154               
9E53: 8D 55 01        STA     $0155               
9E56: A9 27           LDA     #$27                
9E58: 85 A6           STA     $A6                 
9E5A: 60              RTS                         
9E5B: A5 C9           LDA     $C9                 
9E5D: C9 F0           CMP     #$F0                
9E5F: B0 02           BCS     $9E63               ; {}
9E61: E6 C9           INC     $C9                 
9E63: 60              RTS                         
9E64: A2 20           LDX     #$20                
9E66: A9 B0           LDA     #$B0                
9E68: 9D 00 07        STA     $0700,X             
9E6B: A9 00           LDA     #$00                
9E6D: 9D 02 07        STA     $0702,X             
9E70: A9 24           LDA     #$24                
9E72: 9D 03 07        STA     $0703,X             
9E75: 4C BF C3        JMP     $C3BF               
9E78: 02 ; ????
9E79: 70 71           BVS     $9EEC               ; {}
9E7B: 72 ; ????
9E7C: 73 ; ????
9E7D: 74 ; ????
9E7E: 75 00           ADC     $00,X               ; {ram.GP_00}
9E80: 42 ; ????
9E81: 71 70           ADC     ($70),Y             
9E83: 73 ; ????
9E84: 72 ; ????
9E85: 75 74           ADC     $74,X               
9E87: 00              BRK                         
9E88: 02 ; ????
9E89: 70 71           BVS     $9EFC               ; {}
9E8B: 72 ; ????
9E8C: 73 ; ????
9E8D: 76 77           ROR     $77,X               
9E8F: 00              BRK                         
9E90: 42 ; ????
9E91: 71 70           ADC     ($70),Y             
9E93: 73 ; ????
9E94: 72 ; ????
9E95: 77 ; ????
9E96: 76 00           ROR     $00,X               ; {ram.GP_00}
9E98: 02 ; ????
9E99: B0 B1           BCS     $9E4C               ; {}
9E9B: B2 ; ????
9E9C: B3 ; ????
9E9D: B4 B5           LDY     $B5,X               
9E9F: 00              BRK                         
9EA0: 42 ; ????
9EA1: B1 B0           LDA     ($B0),Y             
9EA3: B3 ; ????
9EA4: B2 ; ????
9EA5: B5 B4           LDA     $B4,X               
9EA7: 00              BRK                         
9EA8: 02 ; ????
9EA9: B0 B1           BCS     $9E5C               ; {}
9EAB: B2 ; ????
9EAC: B3 ; ????
9EAD: B6 B7           LDX     $B7,Y               
9EAF: 00              BRK                         
9EB0: 42 ; ????
9EB1: B1 B0           LDA     ($B0),Y             
9EB3: B3 ; ????
9EB4: B2 ; ????
9EB5: B7 ; ????
9EB6: B6 00           LDX     $00,Y               ; {ram.GP_00}
9EB8: 00              BRK                         
9EB9: 2E 2F 7A        ROL     $7A2F               
9EBC: 7B ; ????
9EBD: 7D 7C 00        ADC     $007C,X             
9EC0: 40              RTI                         
9EC1: 2F ; ????
9EC2: 2E 7B 7A        ROL     $7A7B               
9EC5: 7C ; ????
9EC6: 7D 00 00        ADC     $0000,X             ; {ram.GP_00}
9EC9: 2E 2F 7A        ROL     $7A2F               
9ECC: 7B ; ????
9ECD: 7E 7C 00        ROR     $007C,X             
9ED0: 40              RTI                         
9ED1: 2F ; ????
9ED2: 2E 7B 7A        ROL     $7A7B               
9ED5: 7C ; ????
9ED6: 7E 00 4B        ROR     $4B00,X             
9ED9: 4B ; ????
9EDA: 4B ; ????
9EDB: 4B ; ????
9EDC: 5A ; ????
9EDD: 5A ; ????
9EDE: 5A ; ????
9EDF: 5A ; ????
9EE0: 4A              LSR     A                   
9EE1: 4A              LSR     A                   
9EE2: 4A              LSR     A                   
9EE3: 4A              LSR     A                   
9EE4: 95 5F           STA     $5F,X               
9EE6: 96 5F           STX     $5F,Y               
9EE8: 9B ; ????
9EE9: 5F ; ????
9EEA: 9C ; ????
9EEB: 5F ; ????
9EEC: 3F ; ????
9EED: 5F ; ????
9EEE: 4F ; ????
9EEF: 5F ; ????
9EF0: 48              PHA                         
9EF1: 5F ; ????
9EF2: 58              CLI                         
9EF3: 5F ; ????
9EF4: 49 5F           EOR     #$5F                
9EF6: 59 5F AA        EOR     $AA5F,Y             ; {}
9EF9: 5F ; ????
9EFA: AB ; ????
9EFB: 5F ; ????
9EFC: 34 ; ????
9EFD: 5F ; ????
9EFE: 55 5F           EOR     $5F,X               
9F00: E0 E1           CPX     #$E1                
9F02: E4 E5           CPX     $E5                 
9F04: E1 E0           SBC     ($E0,X)             
9F06: E5 E4           SBC     $E4                 
9F08: E2 ; ????
9F09: E3 ; ????
9F0A: E4 E5           CPX     $E5                 
9F0C: E3 ; ????
9F0D: E2 ; ????
9F0E: E5 E4           SBC     $E4                 
9F10: 78              SEI                         
9F11: 79 7A 7B        ADC     $7B7A,Y             
9F14: 79 78 7B        ADC     $7B78,Y             
9F17: 7A ; ????
9F18: C2 ; ????
9F19: C3 ; ????
9F1A: C6 C7           DEC     $C7                 
9F1C: C3 ; ????
9F1D: C2 ; ????
9F1E: C7 ; ????
9F1F: C6 C0           DEC     $C0                 
9F21: C1 C4           CMP     ($C4,X)             
9F23: C5 C1           CMP     $C1                 
9F25: C0 C5           CPY     #$C5                
9F27: C4 D0           CPY     $D0                 
9F29: D1 D4           CMP     ($D4),Y             
9F2B: D5 D1           CMP     $D1,X               
9F2D: D0 D5           BNE     $9F04               ; {}
9F2F: D4 ; ????
9F30: D2 ; ????
9F31: D3 ; ????
9F32: D6 D7           DEC     $D7,X               
9F34: D3 ; ????
9F35: D2 ; ????
9F36: D7 ; ????
9F37: D6 F0           DEC     $F0,X               
9F39: F1 F2           SBC     ($F2),Y             
9F3B: F3 ; ????
9F3C: F1 F0           SBC     ($F0),Y             
9F3E: F3 ; ????
9F3F: F2 ; ????
9F40: 00              BRK                         
9F41: 00              BRK                         
9F42: 00              BRK                         
9F43: 00              BRK                         
9F44: 00              BRK                         
9F45: 00              BRK                         
9F46: 00              BRK                         
9F47: 00              BRK                         
9F48: 9F ; ????
9F49: 5F ; ????
9F4A: AF ; ????
9F4B: 5F ; ????
9F4C: 8E 5F 8F        STX     $8F5F               ; {}
9F4F: 5F ; ????
9F50: 34 ; ????
9F51: 5F ; ????
9F52: 8F ; ????
9F53: 5F ; ????
9F54: CD CC CF        CMP     $CFCC               
9F57: CE 7F 00        DEC     $007F               
9F5A: 00              BRK                         
9F5B: 00              BRK                         
9F5C: 7F ; ????
9F5D: 00              BRK                         
9F5E: 00              BRK                         
9F5F: 00              BRK                         
9F60: 7F ; ????
9F61: 00              BRK                         
9F62: 00              BRK                         
9F63: 00              BRK                         
9F64: FC ; ????
9F65: 27 ; ????
9F66: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9F68: F8              SED                         
9F69: 94 01           STY     $01,X               
9F6B: 00              BRK                         
9F6C: 7F ; ????
9F6D: 00              BRK                         
9F6E: 00              BRK                         
9F6F: 00              BRK                         
9F70: 00              BRK                         
9F71: AE 01 00        LDX     $0001               
9F74: 7F ; ????
9F75: 00              BRK                         
9F76: 00              BRK                         
9F77: 00              BRK                         
9F78: F8              SED                         
9F79: CC 03 FC        CPY     $FC03               
9F7C: F8              SED                         
9F7D: CC 43 04        CPY     $0443               
9F80: 00              BRK                         
9F81: CD 03 FC        CMP     $FC03               
9F84: 00              BRK                         
9F85: CD 43 04        CMP     $0443               
9F88: F8              SED                         
9F89: C8              INY                         
9F8A: 02 ; ????
9F8B: FC ; ????
9F8C: F8              SED                         
9F8D: C9 02           CMP     #$02                
9F8F: 04 ; ????
9F90: 00              BRK                         
9F91: C8              INY                         
9F92: 82 ; ????
9F93: FC ; ????
9F94: 00              BRK                         
9F95: C9 82           CMP     #$82                
9F97: 04 ; ????
9F98: F8              SED                         
9F99: C9 42           CMP     #$42                
9F9B: FC ; ????
9F9C: F8              SED                         
9F9D: C8              INY                         
9F9E: 42 ; ????
9F9F: 04 ; ????
9FA0: 00              BRK                         
9FA1: C9 C2           CMP     #$C2                
9FA3: FC ; ????
9FA4: 00              BRK                         
9FA5: C8              INY                         
9FA6: C2 ; ????
9FA7: 04 ; ????
9FA8: F8              SED                         
9FA9: CA              DEX                         
9FAA: 02 ; ????
9FAB: FC ; ????
9FAC: F8              SED                         
9FAD: CB ; ????
9FAE: 02 ; ????
9FAF: 04 ; ????
9FB0: 00              BRK                         
9FB1: CA              DEX                         
9FB2: 82 ; ????
9FB3: FC ; ????
9FB4: 00              BRK                         
9FB5: CB ; ????
9FB6: 82 ; ????
9FB7: 04 ; ????
9FB8: F8              SED                         
9FB9: CB ; ????
9FBA: 42 ; ????
9FBB: FC ; ????
9FBC: F8              SED                         
9FBD: CA              DEX                         
9FBE: 42 ; ????
9FBF: 04 ; ????
9FC0: 00              BRK                         
9FC1: CB ; ????
9FC2: C2 ; ????
9FC3: FC ; ????
9FC4: 00              BRK                         
9FC5: CA              DEX                         
9FC6: C2 ; ????
9FC7: 04 ; ????
9FC8: F8              SED                         
9FC9: DC ; ????
9FCA: 03 ; ????
9FCB: FC ; ????
9FCC: F8              SED                         
9FCD: DC ; ????
9FCE: 43 ; ????
9FCF: 04 ; ????
9FD0: 00              BRK                         
9FD1: DD 03 FC        CMP     $FC03,X             
9FD4: 00              BRK                         
9FD5: DD 43 04        CMP     $0443,X             
9FD8: F8              SED                         
9FD9: DE 03 FC        DEC     $FC03,X             
9FDC: F8              SED                         
9FDD: DE 43 04        DEC     $0443,X             
9FE0: 00              BRK                         
9FE1: DF ; ????
9FE2: 03 ; ????
9FE3: FC ; ????
9FE4: 00              BRK                         
9FE5: DF ; ????
9FE6: 43 ; ????
9FE7: 04 ; ????
9FE8: F8              SED                         
9FE9: 50 00           BVC     $9FEB               ; {}
9FEB: FC ; ????
9FEC: F8              SED                         
9FED: 50 40           BVC     $A02F               ; {}
9FEF: 04 ; ????
9FF0: 00              BRK                         
9FF1: 51 00           EOR     ($00),Y             ; {ram.GP_00}
9FF3: FC ; ????
9FF4: 00              BRK                         
9FF5: 51 40           EOR     ($40),Y             
9FF7: 04 ; ????
9FF8: F8              SED                         
9FF9: 3E 00 FC        ROL     $FC00,X             
9FFC: 7F ; ????
9FFD: 00              BRK                         
9FFE: 00              BRK                         
9FFF: 00              BRK                         
A000: 00              BRK                         
A001: 3E 80 FC        ROL     $FC80,X             
A004: 7F ; ????
A005: 00              BRK                         
A006: 00              BRK                         
A007: 00              BRK                         
A008: F8              SED                         
A009: 52 ; ????
A00A: 00              BRK                         
A00B: 04 ; ????
A00C: 7F ; ????
A00D: 00              BRK                         
A00E: 00              BRK                         
A00F: 00              BRK                         
A010: 00              BRK                         
A011: 52 ; ????
A012: 80 ; ????
A013: 04 ; ????
A014: 7F ; ????
A015: 00              BRK                         
A016: 00              BRK                         
A017: 00              BRK                         
A018: 00              BRK                         
A019: 00              BRK                         
A01A: 00              BRK                         
A01B: 00              BRK                         
A01C: 00              BRK                         
A01D: 00              BRK                         
A01E: 00              BRK                         
A01F: 00              BRK                         
A020: 00              BRK                         
A021: 00              BRK                         
A022: 00              BRK                         
A023: 00              BRK                         
A024: 00              BRK                         
A025: 00              BRK                         
A026: 00              BRK                         
A027: 00              BRK                         
A028: F8              SED                         
A029: 92 ; ????
A02A: 01 FD           ORA     ($FD,X)             
A02C: F8              SED                         
A02D: 94 01           STY     $01,X               
A02F: 03 ; ????
A030: 00              BRK                         
A031: 93 ; ????
A032: 01 FD           ORA     ($FD,X)             
A034: 00              BRK                         
A035: AE 01 03        LDX     $0301               
A038: F8              SED                         
A039: 9A              TXS                         
A03A: 01 F4           ORA     ($F4,X)             
A03C: F8              SED                         
A03D: 9A              TXS                         
A03E: 01 FC           ORA     ($FC,X)             
A040: F8              SED                         
A041: 9A              TXS                         
A042: 01 04           ORA     ($04,X)             
A044: F8              SED                         
A045: 9A              TXS                         
A046: 01 0C           ORA     ($0C,X)             
A048: F8              SED                         
A049: 0E 00 FC        ASL     $FC00               
A04C: F8              SED                         
A04D: 0E 40 04        ASL     $0440               
A050: 00              BRK                         
A051: 5C ; ????
A052: 00              BRK                         
A053: FC ; ????
A054: 00              BRK                         
A055: 5C ; ????
A056: 40              RTI                         
A057: 04 ; ????
A058: 98              TYA                         
A059: 48              PHA                         
A05A: BD 01 07        LDA     $0701,X             
A05D: 29 F8           AND     #$F8                
A05F: 4A              LSR     A                   
A060: 4A              LSR     A                   
A061: 4A              LSR     A                   
A062: A8              TAY                         
A063: B9 44 BF        LDA     $BF44,Y             ; {}
A066: 9D 07 07        STA     $0707,X             
A069: A9 00           LDA     #$00                
A06B: 9D 08 07        STA     $0708,X             
A06E: 68              PLA                         
A06F: A8              TAY                         
A070: 60              RTS                         
A071: 98              TYA                         
A072: 48              PHA                         
A073: BD 01 07        LDA     $0701,X             
A076: 29 F8           AND     #$F8                
A078: 4A              LSR     A                   
A079: 4A              LSR     A                   
A07A: 4A              LSR     A                   
A07B: A8              TAY                         
A07C: B9 44 BF        LDA     $BF44,Y             ; {}
A07F: 9D 07 07        STA     $0707,X             
A082: 68              PLA                         
A083: A8              TAY                         
A084: 60              RTS                         
A085: BD 01 07        LDA     $0701,X             
A088: 4A              LSR     A                   
A089: 4A              LSR     A                   
A08A: 4A              LSR     A                   
A08B: A8              TAY                         
A08C: B9 54 BF        LDA     $BF54,Y             ; {}
A08F: 60              RTS                         
A090: BD 01 07        LDA     $0701,X             
A093: 29 F8           AND     #$F8                
A095: C9 30           CMP     #$30                
A097: F0 1D           BEQ     $A0B6               ; {}
A099: A5 75           LDA     $75                 
A09B: 9D 00 07        STA     $0700,X             
A09E: A9 5A           LDA     #$5A                
A0A0: 9D 02 07        STA     $0702,X             
A0A3: A9 F7           LDA     #$F7                
A0A5: 9D 03 07        STA     $0703,X             
A0A8: A9 A0           LDA     #$A0                
A0AA: 9D 04 07        STA     $0704,X             
A0AD: A9 40           LDA     #$40                
A0AF: 9D 05 07        STA     $0705,X             
A0B2: 20 58 A0        JSR     $A058               ; {}
A0B5: 60              RTS                         
A0B6: 8A              TXA                         
A0B7: 38              SEC                         
A0B8: E9 60           SBC     #$60                
A0BA: 4A              LSR     A                   
A0BB: 4A              LSR     A                   
A0BC: 4A              LSR     A                   
A0BD: 4A              LSR     A                   
A0BE: A8              TAY                         
A0BF: B9 DD A0        LDA     $A0DD,Y             ; {}
A0C2: 9D 00 07        STA     $0700,X             
A0C5: A9 06           LDA     #$06                
A0C7: 9D 02 07        STA     $0702,X             
A0CA: A9 08           LDA     #$08                
A0CC: 9D 03 07        STA     $0703,X             
A0CF: A9 40           LDA     #$40                
A0D1: 9D 04 07        STA     $0704,X             
A0D4: A9 00           LDA     #$00                
A0D6: 9D 05 07        STA     $0705,X             
A0D9: 20 58 A0        JSR     $A058               ; {}
A0DC: 60              RTS                         
A0DD: 30 60           BMI     $A13F               ; {}
A0DF: 90 C0           BCC     $A0A1               ; {}
A0E1: A2 F0           LDX     #$F0                
A0E3: BD 01 07        LDA     $0701,X             
A0E6: 29 F8           AND     #$F8                
A0E8: C9 30           CMP     #$30                
A0EA: D0 C9           BNE     $A0B5               ; {}
A0EC: 20 D4 A1        JSR     $A1D4               ; {}
A0EF: 20 08 DD        JSR     $DD08               
A0F2: BD 01 07        LDA     $0701,X             
A0F5: 29 07           AND     #$07                
A0F7: 20 2B EE        JSR     $EE2B               
A0FA: AB ; ????
A0FB: A1 02           LDA     ($02,X)             
A0FD: A1 73           LDA     ($73,X)             
A0FF: A1 65           LDA     ($65,X)             
A101: DD BD 02        CMP     $02BD,X             
A104: 07 ; ????
A105: 29 0F           AND     #$0F                
A107: C9 08           CMP     #$08                
A109: B0 39           BCS     $A144               ; {}
A10B: A9 C0           LDA     #$C0                
A10D: 85 08           STA     $08                 
A10F: A5 76           LDA     $76                 
A111: 85 09           STA     $09                 
A113: A5 77           LDA     $77                 
A115: 85 0A           STA     $0A                 
A117: 20 6D C7        JSR     $C76D               
A11A: 20 90 D9        JSR     $D990               
A11D: 90 12           BCC     $A131               ; {}
A11F: 20 E7 D9        JSR     $D9E7               
A122: 90 0D           BCC     $A131               ; {}
A124: 20 09 DA        JSR     $DA09               
A127: 20 C0 DB        JSR     $DBC0               
A12A: 20 E0 A1        JSR     $A1E0               ; {}
A12D: 20 DE DC        JSR     $DCDE               
A130: 60              RTS                         
A131: 20 56 A1        JSR     $A156               ; {}
A134: 20 A9 DC        JSR     $DCA9               
A137: BD 01 07        LDA     $0701,X             
A13A: 29 F8           AND     #$F8                
A13C: 09 03           ORA     #$03                
A13E: 9D 01 07        STA     $0701,X             
A141: 4C 5C A1        JMP     $A15C               ; {}
A144: A9 08           LDA     #$08                
A146: 85 08           STA     $08                 
A148: A5 76           LDA     $76                 
A14A: 85 09           STA     $09                 
A14C: A5 77           LDA     $77                 
A14E: 85 0A           STA     $0A                 
A150: 20 8D C7        JSR     $C78D               
A153: 4C 1A A1        JMP     $A11A               ; {}
A156: A9 80           LDA     #$80                
A158: 8D 80 03        STA     $0380               
A15B: 60              RTS                         
A15C: A9 FF           LDA     #$FF                
A15E: 9D 02 07        STA     $0702,X             
A161: A9 08           LDA     #$08                
A163: 8D 81 03        STA     $0381               
A166: 20 85 A0        JSR     $A085               ; {}
A169: 20 E1 E2        JSR     $E2E1               
A16C: 20 F0 E2        JSR     $E2F0               
A16F: 20 5B 9E        JSR     $9E5B               ; {}
A172: 60              RTS                         
A173: 20 62 DF        JSR     $DF62               
A176: BD 02 07        LDA     $0702,X             
A179: 29 0F           AND     #$0F                
A17B: C9 08           CMP     #$08                
A17D: B0 16           BCS     $A195               ; {}
A17F: AD 23 07        LDA     $0723               
A182: 18              CLC                         
A183: 69 10           ADC     #$10                
A185: 85 08           STA     $08                 
A187: A9 30           LDA     #$30                
A189: 85 09           STA     $09                 
A18B: A9 F8           LDA     #$F8                
A18D: 85 0A           STA     $0A                 
A18F: 20 6D C7        JSR     $C76D               
A192: 4C 1A A1        JMP     $A11A               ; {}
A195: AD 23 07        LDA     $0723               
A198: 38              SEC                         
A199: E9 10           SBC     #$10                
A19B: 85 08           STA     $08                 
A19D: A9 30           LDA     #$30                
A19F: 85 09           STA     $09                 
A1A1: A9 F8           LDA     #$F8                
A1A3: 85 0A           STA     $0A                 
A1A5: 20 8D C7        JSR     $C78D               
A1A8: 4C 1A A1        JMP     $A11A               ; {}
A1AB: 8A              TXA                         
A1AC: 18              CLC                         
A1AD: 65 14           ADC     $14                 
A1AF: 29 7F           AND     #$7F                
A1B1: D0 06           BNE     $A1B9               ; {}
A1B3: 20 90 A0        JSR     $A090               ; {}
A1B6: FE 01 07        INC     $0701,X             
A1B9: 60              RTS                         
A1BA: AD 23 07        LDA     $0723               
A1BD: 38              SEC                         
A1BE: FD 03 07        SBC     $0703,X             
A1C1: B0 02           BCS     $A1C5               ; {}
A1C3: 49 FF           EOR     #$FF                
A1C5: C9 04           CMP     #$04                
A1C7: B0 0A           BCS     $A1D3               ; {}
A1C9: BD 01 07        LDA     $0701,X             
A1CC: 29 F8           AND     #$F8                
A1CE: 09 02           ORA     #$02                
A1D0: 9D 01 07        STA     $0701,X             
A1D3: 60              RTS                         
A1D4: 48              PHA                         
A1D5: BD 03 07        LDA     $0703,X             
A1D8: 38              SEC                         
A1D9: E5 27           SBC     $27                 
A1DB: 9D 03 07        STA     $0703,X             
A1DE: 68              PLA                         
A1DF: 60              RTS                         
A1E0: BD 01 07        LDA     $0701,X             
A1E3: 29 F8           AND     #$F8                
A1E5: C9 30           CMP     #$30                
A1E7: F0 14           BEQ     $A1FD               ; {}
A1E9: A0 40           LDY     #$40                
A1EB: BD 04 07        LDA     $0704,X             
A1EE: 30 01           BMI     $A1F1               ; {}
A1F0: C8              INY                         
A1F1: A5 14           LDA     $14                 
A1F3: 29 08           AND     #$08                
A1F5: D0 02           BNE     $A1F9               ; {}
A1F7: C8              INY                         
A1F8: C8              INY                         
A1F9: 98              TYA                         
A1FA: 4C CD C4        JMP     $C4CD               
A1FD: A0 90           LDY     #$90                
A1FF: D0 EA           BNE     $A1EB               ; {}
A201: 60              RTS                         
A202: AD 61 07        LDA     $0761               
A205: 0D 71 07        ORA     $0771               
A208: 0D 81 07        ORA     $0781               
A20B: 0D 91 07        ORA     $0791               
A20E: F0 10           BEQ     $A220               ; {}
A210: 20 76 A2        JSR     $A276               ; {}
A213: 20 DA A2        JSR     $A2DA               ; {}
A216: 20 98 A2        JSR     $A298               ; {}
A219: 20 D9 A3        JSR     $A3D9               ; {}
A21C: 20 B0 A6        JSR     $A6B0               ; {}
A21F: 60              RTS                         
A220: AD 30 01        LDA     $0130               
A223: 0A              ASL     A                   
A224: A8              TAY                         
A225: B9 F7 BE        LDA     $BEF7,Y             ; {}
A228: 85 00           STA     $00                 ; {ram.GP_00}
A22A: B9 F8 BE        LDA     $BEF8,Y             ; {}
A22D: 85 01           STA     $01                 
A22F: AC D1 04        LDY     $04D1               
A232: B1 00           LDA     ($00),Y             ; {ram.GP_00}
A234: C9 0D           CMP     #$0D                
A236: F0 3D           BEQ     $A275               ; {}
A238: 0A              ASL     A                   
A239: 0A              ASL     A                   
A23A: 0A              ASL     A                   
A23B: 20 9D DC        JSR     $DC9D               
A23E: 8D 61 07        STA     $0761               
A241: 8D 71 07        STA     $0771               
A244: 8D 81 07        STA     $0781               
A247: 8D 91 07        STA     $0791               
A24A: A9 9A           LDA     #$9A                
A24C: 8D 60 07        STA     $0760               
A24F: 8D 70 07        STA     $0770               
A252: 8D 80 07        STA     $0780               
A255: 8D 90 07        STA     $0790               
A258: A9 F7           LDA     #$F7                
A25A: 8D 63 07        STA     $0763               
A25D: 8D 73 07        STA     $0773               
A260: 8D 83 07        STA     $0783               
A263: 8D 93 07        STA     $0793               
A266: AD 20 07        LDA     $0720               
A269: 85 75           STA     $75                 
A26B: 38              SEC                         
A26C: E9 18           SBC     #$18                
A26E: 85 76           STA     $76                 
A270: 18              CLC                         
A271: 69 30           ADC     #$30                
A273: 85 77           STA     $77                 
A275: 60              RTS                         
A276: A2 60           LDX     #$60                
A278: 20 8B A2        JSR     $A28B               ; {}
A27B: A2 70           LDX     #$70                
A27D: 20 8B A2        JSR     $A28B               ; {}
A280: A2 80           LDX     #$80                
A282: 20 8B A2        JSR     $A28B               ; {}
A285: A2 90           LDX     #$90                
A287: 20 8B A2        JSR     $A28B               ; {}
A28A: 60              RTS                         
A28B: BD 01 07        LDA     $0701,X             
A28E: 29 F8           AND     #$F8                
A290: C9 40           CMP     #$40                
A292: D0 F6           BNE     $A28A               ; {}
A294: 20 EC A0        JSR     $A0EC               ; {}
A297: 60              RTS                         
A298: A2 60           LDX     #$60                
A29A: 20 AD A2        JSR     $A2AD               ; {}
A29D: A2 70           LDX     #$70                
A29F: 20 AD A2        JSR     $A2AD               ; {}
A2A2: A2 80           LDX     #$80                
A2A4: 20 AD A2        JSR     $A2AD               ; {}
A2A7: A2 90           LDX     #$90                
A2A9: 20 AD A2        JSR     $A2AD               ; {}
A2AC: 60              RTS                         
A2AD: BD 01 07        LDA     $0701,X             
A2B0: 29 F8           AND     #$F8                
A2B2: C9 30           CMP     #$30                
A2B4: D0 F6           BNE     $A2AC               ; {}
A2B6: 4C EC A0        JMP     $A0EC               ; {}
A2B9: A9 00           LDA     #$00                
A2BB: 9D 04 07        STA     $0704,X             
A2BE: 9D 05 07        STA     $0705,X             
A2C1: A9 80           LDA     #$80                
A2C3: 9D 06 07        STA     $0706,X             
A2C6: 20 58 A0        JSR     $A058               ; {}
A2C9: A9 F0           LDA     #$F0                
A2CB: 9D 00 07        STA     $0700,X             
A2CE: 8A              TXA                         
A2CF: 38              SEC                         
A2D0: E9 60           SBC     #$60                
A2D2: 0A              ASL     A                   
A2D3: 18              CLC                         
A2D4: 69 40           ADC     #$40                
A2D6: 9D 03 07        STA     $0703,X             
A2D9: 60              RTS                         
A2DA: A2 60           LDX     #$60                
A2DC: 20 EF A2        JSR     $A2EF               ; {}
A2DF: A2 70           LDX     #$70                
A2E1: 20 EF A2        JSR     $A2EF               ; {}
A2E4: A2 80           LDX     #$80                
A2E6: 20 EF A2        JSR     $A2EF               ; {}
A2E9: A2 90           LDX     #$90                
A2EB: 20 EF A2        JSR     $A2EF               ; {}
A2EE: 60              RTS                         
A2EF: BD 01 07        LDA     $0701,X             
A2F2: 29 F8           AND     #$F8                
A2F4: C9 50           CMP     #$50                
A2F6: D0 33           BNE     $A32B               ; {}
A2F8: 20 D4 A1        JSR     $A1D4               ; {}
A2FB: 20 08 DD        JSR     $DD08               
A2FE: BD 01 07        LDA     $0701,X             
A301: 29 07           AND     #$07                
A303: 20 2B EE        JSR     $EE2B               
A306: A1 A3           LDA     ($A3,X)             
A308: 0C ; ????
A309: A3 ; ????
A30A: 9E ; ????
A30B: A3 ; ????
A30C: 20 90 D9        JSR     $D990               
A30F: 90 1B           BCC     $A32C               ; {}
A311: 20 E7 D9        JSR     $D9E7               
A314: 90 16           BCC     $A32C               ; {}
A316: 20 62 DF        JSR     $DF62               
A319: 20 09 DA        JSR     $DA09               
A31C: 20 76 A3        JSR     $A376               ; {}
A31F: 20 DA DB        JSR     $DBDA               
A322: 20 C9 DB        JSR     $DBC9               
A325: 20 B1 A3        JSR     $A3B1               ; {}
A328: 20 DE DC        JSR     $DCDE               
A32B: 60              RTS                         
A32C: 20 56 A1        JSR     $A156               ; {}
A32F: 20 A9 DC        JSR     $DCA9               
A332: FE 01 07        INC     $0701,X             
A335: 4C 5C A1        JMP     $A15C               ; {}
A338: 20 87 D2        JSR     $D287               
A33B: D0 00           BNE     $A33D               ; {}
A33D: BD 06 07        LDA     $0706,X             
A340: C9 78           CMP     #$78                
A342: B0 03           BCS     $A347               ; {}
A344: 18              CLC                         
A345: 69 01           ADC     #$01                
A347: 9D 06 07        STA     $0706,X             
A34A: 29 F0           AND     #$F0                
A34C: 9D 05 07        STA     $0705,X             
A34F: 60              RTS                         
A350: A9 00           LDA     #$00                
A352: 9D 06 07        STA     $0706,X             
A355: 9D 04 07        STA     $0704,X             
A358: 9D 05 07        STA     $0705,X             
A35B: 60              RTS                         
A35C: BD 06 07        LDA     $0706,X             
A35F: 18              CLC                         
A360: 69 01           ADC     #$01                
A362: 9D 06 07        STA     $0706,X             
A365: C9 F8           CMP     #$F8                
A367: B0 06           BCS     $A36F               ; {}
A369: 29 F0           AND     #$F0                
A36B: 9D 05 07        STA     $0705,X             
A36E: 60              RTS                         
A36F: A9 01           LDA     #$01                
A371: 9D 06 07        STA     $0706,X             
A374: D0 DF           BNE     $A355               ; {}
A376: BD 06 07        LDA     $0706,X             
A379: 30 E1           BMI     $A35C               ; {}
A37B: D0 BB           BNE     $A338               ; {}
A37D: 8A              TXA                         
A37E: 38              SEC                         
A37F: E9 60           SBC     #$60                
A381: 18              CLC                         
A382: 65 14           ADC     $14                 
A384: 29 3F           AND     #$3F                
A386: D0 15           BNE     $A39D               ; {}
A388: A0 40           LDY     #$40                
A38A: AD 23 07        LDA     $0723               
A38D: DD 03 07        CMP     $0703,X             
A390: B0 02           BCS     $A394               ; {}
A392: A0 B0           LDY     #$B0                
A394: 98              TYA                         
A395: 9D 04 07        STA     $0704,X             
A398: A9 80           LDA     #$80                
A39A: 9D 06 07        STA     $0706,X             
A39D: 60              RTS                         
A39E: 4C 65 DD        JMP     $DD65               
A3A1: 8A              TXA                         
A3A2: 38              SEC                         
A3A3: E9 60           SBC     #$60                
A3A5: 0A              ASL     A                   
A3A6: C5 14           CMP     $14                 
A3A8: D0 06           BNE     $A3B0               ; {}
A3AA: 20 B9 A2        JSR     $A2B9               ; {}
A3AD: FE 01 07        INC     $0701,X             
A3B0: 60              RTS                         
A3B1: A0 14           LDY     #$14                
A3B3: A5 14           LDA     $14                 
A3B5: 29 08           AND     #$08                
A3B7: D0 01           BNE     $A3BA               ; {}
A3B9: C8              INY                         
A3BA: 98              TYA                         
A3BB: 4C 67 C6        JMP     $C667               
A3BE: A9 00           LDA     #$00                
A3C0: 9D 04 07        STA     $0704,X             
A3C3: 9D 05 07        STA     $0705,X             
A3C6: A9 B0           LDA     #$B0                
A3C8: 9D 02 07        STA     $0702,X             
A3CB: 20 58 A0        JSR     $A058               ; {}
A3CE: A9 80           LDA     #$80                
A3D0: 9D 00 07        STA     $0700,X             
A3D3: A9 F0           LDA     #$F0                
A3D5: 9D 03 07        STA     $0703,X             
A3D8: 60              RTS                         
A3D9: A2 60           LDX     #$60                
A3DB: 20 ED A3        JSR     $A3ED               ; {}
A3DE: A2 70           LDX     #$70                
A3E0: 20 ED A3        JSR     $A3ED               ; {}
A3E3: A2 80           LDX     #$80                
A3E5: 20 ED A3        JSR     $A3ED               ; {}
A3E8: A2 90           LDX     #$90                
A3EA: 4C ED A3        JMP     $A3ED               ; {}
A3ED: BD 01 07        LDA     $0701,X             
A3F0: 29 F8           AND     #$F8                
A3F2: C9 38           CMP     #$38                
A3F4: D0 3C           BNE     $A432               ; {}
A3F6: 20 D4 A1        JSR     $A1D4               ; {}
A3F9: 20 08 DD        JSR     $DD08               
A3FC: BD 01 07        LDA     $0701,X             
A3FF: 29 07           AND     #$07                
A401: 20 2B EE        JSR     $EE2B               
A404: 55 A4           EOR     $A4,X               
A406: 0A              ASL     A                   
A407: A4 52           LDY     $52                 
A409: A4 20           LDY     $20                 
A40B: 90 D9           BCC     $A3E6               ; {}
A40D: 90 24           BCC     $A433               ; {}
A40F: 20 E7 D9        JSR     $D9E7               
A412: 90 1F           BCC     $A433               ; {}
A414: 20 09 DA        JSR     $DA09               
A417: A9 F8           LDA     #$F8                
A419: 85 08           STA     $08                 
A41B: A9 30           LDA     #$30                
A41D: 85 09           STA     $09                 
A41F: A9 C0           LDA     #$C0                
A421: 85 0A           STA     $0A                 
A423: 20 6D C7        JSR     $C76D               
A426: 20 3F A4        JSR     $A43F               ; {}
A429: 20 C0 DB        JSR     $DBC0               
A42C: 20 68 A4        JSR     $A468               ; {}
A42F: 20 DE DC        JSR     $DCDE               
A432: 60              RTS                         
A433: 20 56 A1        JSR     $A156               ; {}
A436: 20 A9 DC        JSR     $DCA9               
A439: FE 01 07        INC     $0701,X             
A43C: 4C 5C A1        JMP     $A15C               ; {}
A43F: BD 02 07        LDA     $0702,X             
A442: 29 F0           AND     #$F0                
A444: 30 06           BMI     $A44C               ; {}
A446: A9 60           LDA     #$60                
A448: 9D 02 07        STA     $0702,X             
A44B: 60              RTS                         
A44C: A9 90           LDA     #$90                
A44E: 9D 02 07        STA     $0702,X             
A451: 60              RTS                         
A452: 4C 65 DD        JMP     $DD65               
A455: 8A              TXA                         
A456: 38              SEC                         
A457: E9 60           SBC     #$60                
A459: 0A              ASL     A                   
A45A: 18              CLC                         
A45B: 69 20           ADC     #$20                
A45D: C5 FE           CMP     $FE                 
A45F: D0 06           BNE     $A467               ; {}
A461: 20 BE A3        JSR     $A3BE               ; {}
A464: FE 01 07        INC     $0701,X             
A467: 60              RTS                         
A468: A9 46           LDA     #$46                
A46A: 4C CD C4        JMP     $C4CD               
A46D: A9 0D           LDA     #$0D                
A46F: 9D 02 07        STA     $0702,X             
A472: A9 00           LDA     #$00                
A474: 9D 04 07        STA     $0704,X             
A477: 9D 05 07        STA     $0705,X             
A47A: 20 58 A0        JSR     $A058               ; {}
A47D: 60              RTS                         
A47E: A5 14           LDA     $14                 
A480: 0A              ASL     A                   
A481: 0A              ASL     A                   
A482: 0A              ASL     A                   
A483: 0A              ASL     A                   
A484: 9D 00 07        STA     $0700,X             
A487: A9 F0           LDA     #$F0                
A489: 9D 03 07        STA     $0703,X             
A48C: 60              RTS                         
A48D: A2 60           LDX     #$60                
A48F: 20 A2 A4        JSR     $A4A2               ; {}
A492: A2 70           LDX     #$70                
A494: 20 A2 A4        JSR     $A4A2               ; {}
A497: A2 80           LDX     #$80                
A499: 20 A2 A4        JSR     $A4A2               ; {}
A49C: A2 90           LDX     #$90                
A49E: 20 A2 A4        JSR     $A4A2               ; {}
A4A1: 60              RTS                         
A4A2: BD 01 07        LDA     $0701,X             
A4A5: 29 F8           AND     #$F8                
A4A7: C9 38           CMP     #$38                
A4A9: D0 36           BNE     $A4E1               ; {}
A4AB: 20 D4 A1        JSR     $A1D4               ; {}
A4AE: 20 08 DD        JSR     $DD08               
A4B1: BD 01 07        LDA     $0701,X             
A4B4: 29 07           AND     #$07                
A4B6: 20 2B EE        JSR     $EE2B               
A4B9: F8              SED                         
A4BA: A4 BF           LDY     $BF                 
A4BC: A4 F5           LDY     $F5                 
A4BE: A4 20           LDY     $20                 
A4C0: 87 ; ????
A4C1: E0 20           CPX     #$20                
A4C3: 90 D9           BCC     $A49E               ; {}
A4C5: 90 1B           BCC     $A4E2               ; {}
A4C7: 20 E7 D9        JSR     $D9E7               
A4CA: 90 16           BCC     $A4E2               ; {}
A4CC: 20 62 DF        JSR     $DF62               
A4CF: 20 09 DA        JSR     $DA09               
A4D2: 20 33 A5        JSR     $A533               ; {}
A4D5: 20 C0 DB        JSR     $DBC0               
A4D8: 20 A2 A5        JSR     $A5A2               ; {}
A4DB: 20 DE DC        JSR     $DCDE               
A4DE: 20 B0 A5        JSR     $A5B0               ; {}
A4E1: 60              RTS                         
A4E2: 20 56 A1        JSR     $A156               ; {}
A4E5: 20 A9 DC        JSR     $DCA9               
A4E8: BD 01 07        LDA     $0701,X             
A4EB: 29 F8           AND     #$F8                
A4ED: 09 02           ORA     #$02                
A4EF: 9D 01 07        STA     $0701,X             
A4F2: 4C 5C A1        JMP     $A15C               ; {}
A4F5: 4C 65 DD        JMP     $DD65               
A4F8: 8A              TXA                         
A4F9: 38              SEC                         
A4FA: E9 60           SBC     #$60                
A4FC: 0A              ASL     A                   
A4FD: 29 60           AND     #$60                
A4FF: 85 00           STA     $00                 ; {ram.GP_00}
A501: A5 FE           LDA     $FE                 
A503: 29 60           AND     #$60                
A505: C5 00           CMP     $00                 ; {ram.GP_00}
A507: D0 D8           BNE     $A4E1               ; {}
A509: 20 7E A4        JSR     $A47E               ; {}
A50C: 20 87 E0        JSR     $E087               
A50F: AD D3 04        LDA     $04D3               
A512: C9 40           CMP     #$40                
A514: 90 CB           BCC     $A4E1               ; {}
A516: AD D5 04        LDA     $04D5               
A519: C9 40           CMP     #$40                
A51B: B0 C4           BCS     $A4E1               ; {}
A51D: 20 6D A4        JSR     $A46D               ; {}
A520: BD 00 07        LDA     $0700,X             
A523: 38              SEC                         
A524: E9 08           SBC     #$08                
A526: 9D 00 07        STA     $0700,X             
A529: FE 01 07        INC     $0701,X             
A52C: 60              RTS                         
A52D: A9 50           LDA     #$50                
A52F: 9D 02 07        STA     $0702,X             
A532: 60              RTS                         
A533: 20 87 D2        JSR     $D287               
A536: D0 F5           BNE     $A52D               ; {}
A538: AD D3 04        LDA     $04D3               
A53B: C9 40           CMP     #$40                
A53D: B0 07           BCS     $A546               ; {}
A53F: AD D4 04        LDA     $04D4               
A542: C9 40           CMP     #$40                
A544: 90 E7           BCC     $A52D               ; {}
A546: A9 00           LDA     #$00                
A548: 9D 05 07        STA     $0705,X             
A54B: BD 02 07        LDA     $0702,X             
A54E: 29 0F           AND     #$0F                
A550: C9 08           CMP     #$08                
A552: B0 1B           BCS     $A56F               ; {}
A554: BD 03 07        LDA     $0703,X             
A557: C9 F0           CMP     #$F0                
A559: B0 29           BCS     $A584               ; {}
A55B: AD D3 04        LDA     $04D3               
A55E: C9 40           CMP     #$40                
A560: 90 22           BCC     $A584               ; {}
A562: AD D5 04        LDA     $04D5               
A565: C9 40           CMP     #$40                
A567: B0 1B           BCS     $A584               ; {}
A569: A9 02           LDA     #$02                
A56B: 9D 02 07        STA     $0702,X             
A56E: 60              RTS                         
A56F: BD 03 07        LDA     $0703,X             
A572: C9 08           CMP     #$08                
A574: 90 F3           BCC     $A569               ; {}
A576: AD D4 04        LDA     $04D4               
A579: C9 40           CMP     #$40                
A57B: 90 EC           BCC     $A569               ; {}
A57D: AD D6 04        LDA     $04D6               
A580: C9 40           CMP     #$40                
A582: B0 E5           BCS     $A569               ; {}
A584: A9 0D           LDA     #$0D                
A586: 9D 02 07        STA     $0702,X             
A589: 60              RTS                         
A58A: BD 02 07        LDA     $0702,X             
A58D: 48              PHA                         
A58E: 29 F0           AND     #$F0                
A590: 9D 05 07        STA     $0705,X             
A593: 68              PLA                         
A594: 0A              ASL     A                   
A595: 0A              ASL     A                   
A596: 0A              ASL     A                   
A597: 0A              ASL     A                   
A598: 9D 04 07        STA     $0704,X             
A59B: 20 DA DB        JSR     $DBDA               
A59E: 20 C9 DB        JSR     $DBC9               
A5A1: 60              RTS                         
A5A2: A0 04           LDY     #$04                
A5A4: A5 14           LDA     $14                 
A5A6: 29 10           AND     #$10                
A5A8: D0 01           BNE     $A5AB               ; {}
A5AA: C8              INY                         
A5AB: 98              TYA                         
A5AC: 20 67 C6        JSR     $C667               
A5AF: 60              RTS                         
A5B0: A0 F0           LDY     #$F0                
A5B2: B9 01 07        LDA     $0701,Y             
A5B5: 29 F8           AND     #$F8                
A5B7: C9 70           CMP     #$70                
A5B9: F0 2A           BEQ     $A5E5               ; {}
A5BB: BD 00 07        LDA     $0700,X             
A5BE: 38              SEC                         
A5BF: E9 08           SBC     #$08                
A5C1: 99 00 07        STA     $0700,Y             
A5C4: BD 03 07        LDA     $0703,X             
A5C7: 99 03 07        STA     $0703,Y             
A5CA: CD 23 07        CMP     $0723               
A5CD: B0 17           BCS     $A5E6               ; {}
A5CF: BD 02 07        LDA     $0702,X             
A5D2: 29 0F           AND     #$0F                
A5D4: C9 08           CMP     #$08                
A5D6: B0 0D           BCS     $A5E5               ; {}
A5D8: A9 04           LDA     #$04                
A5DA: 99 02 07        STA     $0702,Y             
A5DD: 20 2A A6        JSR     $A62A               ; {}
A5E0: A9 70           LDA     #$70                
A5E2: 99 01 07        STA     $0701,Y             
A5E5: 60              RTS                         
A5E6: BD 02 07        LDA     $0702,X             
A5E9: 29 0F           AND     #$0F                
A5EB: C9 08           CMP     #$08                
A5ED: 90 F6           BCC     $A5E5               ; {}
A5EF: A9 0D           LDA     #$0D                
A5F1: 99 02 07        STA     $0702,Y             
A5F4: 20 2A A6        JSR     $A62A               ; {}
A5F7: A9 70           LDA     #$70                
A5F9: 99 01 07        STA     $0701,Y             
A5FC: 60              RTS                         
A5FD: 20 3C A6        JSR     $A63C               ; {}
A600: 60              RTS                         
A601: A0 F0           LDY     #$F0                
A603: B9 01 07        LDA     $0701,Y             
A606: 29 F8           AND     #$F8                
A608: C9 70           CMP     #$70                
A60A: F0 28           BEQ     $A634               ; {}
A60C: A9 70           LDA     #$70                
A60E: 99 01 07        STA     $0701,Y             
A611: BD 00 07        LDA     $0700,X             
A614: 38              SEC                         
A615: E9 08           SBC     #$08                
A617: 99 00 07        STA     $0700,Y             
A61A: BD 03 07        LDA     $0703,X             
A61D: 99 03 07        STA     $0703,Y             
A620: CD 23 07        CMP     $0723               
A623: B0 10           BCS     $A635               ; {}
A625: A9 04           LDA     #$04                
A627: 99 02 07        STA     $0702,Y             
A62A: A5 EF           LDA     $EF                 
A62C: 29 80           AND     #$80                
A62E: 19 02 07        ORA     $0702,Y             
A631: 99 02 07        STA     $0702,Y             
A634: 60              RTS                         
A635: A9 0D           LDA     #$0D                
A637: 99 02 07        STA     $0702,Y             
A63A: D0 EE           BNE     $A62A               ; {}
A63C: BD 01 07        LDA     $0701,X             
A63F: 29 F8           AND     #$F8                
A641: C9 70           CMP     #$70                
A643: D0 EF           BNE     $A634               ; {}
A645: BD 00 07        LDA     $0700,X             
A648: C9 F8           CMP     #$F8                
A64A: B0 1E           BCS     $A66A               ; {}
A64C: BD 03 07        LDA     $0703,X             
A64F: C9 F8           CMP     #$F8                
A651: B0 17           BCS     $A66A               ; {}
A653: 20 35 E0        JSR     $E035               
A656: 20 D4 A1        JSR     $A1D4               ; {}
A659: AD D3 04        LDA     $04D3               
A65C: C9 40           CMP     #$40                
A65E: B0 0A           BCS     $A66A               ; {}
A660: 20 09 DA        JSR     $DA09               
A663: 20 78 A6        JSR     $A678               ; {}
A666: 20 99 A6        JSR     $A699               ; {}
A669: 60              RTS                         
A66A: A9 00           LDA     #$00                
A66C: 9D 01 07        STA     $0701,X             
A66F: A9 F8           LDA     #$F8                
A671: 9D 00 02        STA     $0200,X             
A674: 9D 00 07        STA     $0700,X             
A677: 60              RTS                         
A678: BD 02 07        LDA     $0702,X             
A67B: 29 0F           AND     #$0F                
A67D: C9 08           CMP     #$08                
A67F: B0 0F           BCS     $A690               ; {}
A681: FE 03 07        INC     $0703,X             
A684: FE 03 07        INC     $0703,X             
A687: BD 02 07        LDA     $0702,X             
A68A: 10 03           BPL     $A68F               ; {}
A68C: DE 00 07        DEC     $0700,X             
A68F: 60              RTS                         
A690: DE 03 07        DEC     $0703,X             
A693: DE 03 07        DEC     $0703,X             
A696: 4C 87 A6        JMP     $A687               ; {}
A699: A9 A9           LDA     #$A9                
A69B: 9D 01 02        STA     $0201,X             
A69E: BD 00 07        LDA     $0700,X             
A6A1: 9D 00 02        STA     $0200,X             
A6A4: BD 03 07        LDA     $0703,X             
A6A7: 9D 03 02        STA     $0203,X             
A6AA: A9 01           LDA     #$01                
A6AC: 9D 02 02        STA     $0202,X             
A6AF: 60              RTS                         
A6B0: A2 60           LDX     #$60                
A6B2: 20 C5 A6        JSR     $A6C5               ; {}
A6B5: A2 70           LDX     #$70                
A6B7: 20 C5 A6        JSR     $A6C5               ; {}
A6BA: A2 80           LDX     #$80                
A6BC: 20 C5 A6        JSR     $A6C5               ; {}
A6BF: A2 90           LDX     #$90                
A6C1: 20 C5 A6        JSR     $A6C5               ; {}
A6C4: 60              RTS                         
A6C5: BD 01 07        LDA     $0701,X             
A6C8: 29 F8           AND     #$F8                
A6CA: C9 20           CMP     #$20                
A6CC: D0 F6           BNE     $A6C4               ; {}
A6CE: 20 87 E0        JSR     $E087               
A6D1: 20 D4 A1        JSR     $A1D4               ; {}
A6D4: 20 08 DD        JSR     $DD08               
A6D7: BD 01 07        LDA     $0701,X             
A6DA: 29 07           AND     #$07                
A6DC: 20 2B EE        JSR     $EE2B               
A6DF: E5 A6           SBC     $A6                 
A6E1: 18              CLC                         
A6E2: A7 ; ????
A6E3: 97 ; ????
A6E4: A7 ; ????
A6E5: 8A              TXA                         
A6E6: 38              SEC                         
A6E7: E9 60           SBC     #$60                
A6E9: 29 30           AND     #$30                
A6EB: 85 00           STA     $00                 ; {ram.GP_00}
A6ED: A5 14           LDA     $14                 
A6EF: 29 3F           AND     #$3F                
A6F1: C5 00           CMP     $00                 ; {ram.GP_00}
A6F3: D0 1D           BNE     $A712               ; {}
A6F5: A5 FE           LDA     $FE                 
A6F7: 49 FF           EOR     #$FF                
A6F9: 18              CLC                         
A6FA: 69 D8           ADC     #$D8                
A6FC: 9D 03 07        STA     $0703,X             
A6FF: A9 06           LDA     #$06                
A701: 9D 02 07        STA     $0702,X             
A704: A9 00           LDA     #$00                
A706: 9D 04 07        STA     $0704,X             
A709: 9D 05 07        STA     $0705,X             
A70C: 20 58 A0        JSR     $A058               ; {}
A70F: FE 01 07        INC     $0701,X             
A712: A9 30           LDA     #$30                
A714: 9D 00 07        STA     $0700,X             
A717: 60              RTS                         
A718: 20 08 DD        JSR     $DD08               
A71B: 20 90 D9        JSR     $D990               
A71E: 90 14           BCC     $A734               ; {}
A720: 20 E7 D9        JSR     $D9E7               
A723: 90 12           BCC     $A737               ; {}
A725: 20 09 DA        JSR     $DA09               
A728: 20 3A A7        JSR     $A73A               ; {}
A72B: 20 C0 DB        JSR     $DBC0               
A72E: 20 9A A7        JSR     $A79A               ; {}
A731: 4C DE DC        JMP     $DCDE               
A734: 4C E2 A4        JMP     $A4E2               ; {}
A737: 4C E2 A4        JMP     $A4E2               ; {}
A73A: BD 00 07        LDA     $0700,X             
A73D: 48              PHA                         
A73E: 18              CLC                         
A73F: 69 07           ADC     #$07                
A741: 9D 00 07        STA     $0700,X             
A744: 20 70 A7        JSR     $A770               ; {}
A747: 68              PLA                         
A748: 9D 00 07        STA     $0700,X             
A74B: 90 17           BCC     $A764               ; {}
A74D: AC 60 07        LDY     $0760               
A750: AD D3 04        LDA     $04D3               
A753: C9 40           CMP     #$40                
A755: B0 0D           BCS     $A764               ; {}
A757: AD D4 04        LDA     $04D4               
A75A: C9 40           CMP     #$40                
A75C: B0 06           BCS     $A764               ; {}
A75E: A9 60           LDA     #$60                
A760: 9D 02 07        STA     $0702,X             
A763: 60              RTS                         
A764: A9 00           LDA     #$00                
A766: 9D 02 07        STA     $0702,X             
A769: 9D 04 07        STA     $0704,X             
A76C: 9D 05 07        STA     $0705,X             
A76F: 60              RTS                         
A770: A0 60           LDY     #$60                
A772: 20 85 A7        JSR     $A785               ; {}
A775: A0 70           LDY     #$70                
A777: 20 85 A7        JSR     $A785               ; {}
A77A: A0 80           LDY     #$80                
A77C: 20 85 A7        JSR     $A785               ; {}
A77F: A0 90           LDY     #$90                
A781: 20 85 A7        JSR     $A785               ; {}
A784: 60              RTS                         
A785: 84 00           STY     $00                 ; {ram.GP_00}
A787: E4 00           CPX     $00                 ; {ram.GP_00}
A789: F0 0A           BEQ     $A795               ; {}
A78B: B9 01 07        LDA     $0701,Y             
A78E: C9 21           CMP     #$21                
A790: D0 03           BNE     $A795               ; {}
A792: 4C 5C D9        JMP     $D95C               
A795: 38              SEC                         
A796: 60              RTS                         
A797: 4C 65 DD        JMP     $DD65               
A79A: A9 02           LDA     #$02                
A79C: 4C 67 C6        JMP     $C667               
A79F: 60              RTS                         
A7A0: AD C1 07        LDA     $07C1               
A7A3: 0D C9 07        ORA     $07C9               
A7A6: 0D D1 07        ORA     $07D1               
A7A9: 0D D9 07        ORA     $07D9               
A7AC: F0 04           BEQ     $A7B2               ; {}
A7AE: 20 F1 A7        JSR     $A7F1               ; {}
A7B1: 60              RTS                         
A7B2: AD 30 01        LDA     $0130               
A7B5: 0A              ASL     A                   
A7B6: A8              TAY                         
A7B7: B9 0C BF        LDA     $BF0C,Y             ; {}
A7BA: 85 00           STA     $00                 ; {ram.GP_00}
A7BC: B9 0D BF        LDA     $BF0D,Y             ; {}
A7BF: 85 01           STA     $01                 
A7C1: AC D1 04        LDY     $04D1               
A7C4: B1 00           LDA     ($00),Y             ; {ram.GP_00}
A7C6: 0A              ASL     A                   
A7C7: 0A              ASL     A                   
A7C8: 0A              ASL     A                   
A7C9: 20 99 DC        JSR     $DC99               
A7CC: 8D C1 07        STA     $07C1               
A7CF: 8D C9 07        STA     $07C9               
A7D2: 8D D1 07        STA     $07D1               
A7D5: 8D D9 07        STA     $07D9               
A7D8: 60              RTS                         
A7D9: A9 0D           LDA     #$0D                
A7DB: 9D 02 07        STA     $0702,X             
A7DE: 60              RTS                         
A7DF: A5 14           LDA     $14                 
A7E1: 0A              ASL     A                   
A7E2: 0A              ASL     A                   
A7E3: 0A              ASL     A                   
A7E4: 0A              ASL     A                   
A7E5: 38              SEC                         
A7E6: E9 08           SBC     #$08                
A7E8: 9D 00 07        STA     $0700,X             
A7EB: A9 E8           LDA     #$E8                
A7ED: 9D 03 07        STA     $0703,X             
A7F0: 60              RTS                         
A7F1: A2 C0           LDX     #$C0                
A7F3: 20 00 A8        JSR     $A800               ; {}
A7F6: A2 C8           LDX     #$C8                
A7F8: 20 E3 A9        JSR     $A9E3               ; {}
A7FB: A2 D0           LDX     #$D0                
A7FD: 4C 88 AA        JMP     $AA88               ; {}
A800: BD 01 07        LDA     $0701,X             
A803: 29 F8           AND     #$F8                
A805: C9 48           CMP     #$48                
A807: D0 43           BNE     $A84C               ; {}
A809: A9 00           LDA     #$00                
A80B: 8D D9 07        STA     $07D9               
A80E: 20 19 AB        JSR     $AB19               ; {}
A811: 20 53 E0        JSR     $E053               
A814: 20 D4 A1        JSR     $A1D4               ; {}
A817: BD 01 07        LDA     $0701,X             
A81A: 29 07           AND     #$07                
A81C: 20 2B EE        JSR     $EE2B               
A81F: E7 ; ????
A820: A8              TAY                         
A821: 29 A8           AND     #$A8                
A823: 9B ; ????
A824: A8              TAY                         
A825: D0 A8           BNE     $A7CF               ; {}
A827: 97 ; ????
A828: A8              TAY                         
A829: BD 00 07        LDA     $0700,X             
A82C: C9 F8           CMP     #$F8                
A82E: B0 40           BCS     $A870               ; {}
A830: 20 BC D9        JSR     $D9BC               
A833: 90 18           BCC     $A84D               ; {}
A835: 20 E7 D9        JSR     $D9E7               
A838: 90 13           BCC     $A84D               ; {}
A83A: 20 09 DA        JSR     $DA09               
A83D: 20 28 A9        JSR     $A928               ; {}
A840: 20 08 A9        JSR     $A908               ; {}
A843: 20 C0 DB        JSR     $DBC0               
A846: 20 8A A9        JSR     $A98A               ; {}
A849: 20 B0 A5        JSR     $A5B0               ; {}
A84C: 60              RTS                         
A84D: FE 01 07        INC     $0701,X             
A850: EE C9 07        INC     $07C9               
A853: EE D1 07        INC     $07D1               
A856: A9 FF           LDA     #$FF                
A858: 9D 02 07        STA     $0702,X             
A85B: 20 85 A0        JSR     $A085               ; {}
A85E: 20 E1 E2        JSR     $E2E1               
A861: 20 F0 E2        JSR     $E2F0               
A864: A9 08           LDA     #$08                
A866: 8D 81 03        STA     $0381               
A869: 20 56 A1        JSR     $A156               ; {}
A86C: 20 5B 9E        JSR     $9E5B               ; {}
A86F: 60              RTS                         
A870: 8A              TXA                         
A871: 48              PHA                         
A872: 20 2F DF        JSR     $DF2F               
A875: A2 C8           LDX     #$C8                
A877: 20 2F DF        JSR     $DF2F               
A87A: A2 D0           LDX     #$D0                
A87C: 20 2F DF        JSR     $DF2F               
A87F: 68              PLA                         
A880: AA              TAX                         
A881: 60              RTS                         
A882: BD 00 07        LDA     $0700,X             
A885: C9 F8           CMP     #$F8                
A887: B0 08           BCS     $A891               ; {}
A889: BD 03 07        LDA     $0703,X             
A88C: C9 F8           CMP     #$F8                
A88E: B0 01           BCS     $A891               ; {}
A890: 60              RTS                         
A891: 20 2F DF        JSR     $DF2F               
A894: 68              PLA                         
A895: 68              PLA                         
A896: 60              RTS                         
A897: 20 B2 DE        JSR     $DEB2               
A89A: 60              RTS                         
A89B: 20 09 DA        JSR     $DA09               
A89E: BD 00 07        LDA     $0700,X             
A8A1: C9 18           CMP     #$18                
A8A3: 90 0D           BCC     $A8B2               ; {}
A8A5: 20 82 A8        JSR     $A882               ; {}
A8A8: DE 00 07        DEC     $0700,X             
A8AB: DE 00 07        DEC     $0700,X             
A8AE: 20 8A A9        JSR     $A98A               ; {}
A8B1: 60              RTS                         
A8B2: FE 01 07        INC     $0701,X             
A8B5: A9 00           LDA     #$00                
A8B7: 9D 04 07        STA     $0704,X             
A8BA: 9D 04 07        STA     $0704,X             
A8BD: A9 40           LDA     #$40                
A8BF: 9D 02 07        STA     $0702,X             
A8C2: 60              RTS                         
A8C3: BD 01 07        LDA     $0701,X             
A8C6: 29 F8           AND     #$F8                
A8C8: 09 04           ORA     #$04                
A8CA: 9D 01 07        STA     $0701,X             
A8CD: 4C 56 A8        JMP     $A856               ; {}
A8D0: 20 90 D9        JSR     $D990               
A8D3: 90 EE           BCC     $A8C3               ; {}
A8D5: 20 E7 D9        JSR     $D9E7               
A8D8: 90 E9           BCC     $A8C3               ; {}
A8DA: 20 09 DA        JSR     $DA09               
A8DD: 20 82 A8        JSR     $A882               ; {}
A8E0: 20 C0 DB        JSR     $DBC0               
A8E3: 20 8A A9        JSR     $A98A               ; {}
A8E6: 60              RTS                         
A8E7: 20 DF A7        JSR     $A7DF               ; {}
A8EA: 20 53 E0        JSR     $E053               
A8ED: AD D5 04        LDA     $04D5               
A8F0: C9 40           CMP     #$40                
A8F2: B0 13           BCS     $A907               ; {}
A8F4: AD D3 04        LDA     $04D3               
A8F7: C9 40           CMP     #$40                
A8F9: 90 0C           BCC     $A907               ; {}
A8FB: 20 D9 A7        JSR     $A7D9               ; {}
A8FE: FE 01 07        INC     $0701,X             
A901: EE C9 07        INC     $07C9               
A904: EE D1 07        INC     $07D1               
A907: 60              RTS                         
A908: A5 14           LDA     $14                 
A90A: 29 7F           AND     #$7F                
A90C: D0 0D           BNE     $A91B               ; {}
A90E: BD 03 07        LDA     $0703,X             
A911: CD 23 07        CMP     $0723               
A914: B0 06           BCS     $A91C               ; {}
A916: A9 02           LDA     #$02                
A918: 9D 02 07        STA     $0702,X             
A91B: 60              RTS                         
A91C: A9 0D           LDA     #$0D                
A91E: 9D 02 07        STA     $0702,X             
A921: 60              RTS                         
A922: A9 50           LDA     #$50                
A924: 9D 02 07        STA     $0702,X             
A927: 60              RTS                         
A928: 20 87 D2        JSR     $D287               
A92B: D0 F5           BNE     $A922               ; {}
A92D: AD D3 04        LDA     $04D3               
A930: C9 40           CMP     #$40                
A932: B0 07           BCS     $A93B               ; {}
A934: AD D4 04        LDA     $04D4               
A937: C9 40           CMP     #$40                
A939: 90 E7           BCC     $A922               ; {}
A93B: A9 00           LDA     #$00                
A93D: 9D 05 07        STA     $0705,X             
A940: BD 02 07        LDA     $0702,X             
A943: 29 0F           AND     #$0F                
A945: C9 08           CMP     #$08                
A947: B0 14           BCS     $A95D               ; {}
A949: AD D3 04        LDA     $04D3               
A94C: C9 40           CMP     #$40                
A94E: 90 1B           BCC     $A96B               ; {}
A950: AD D5 04        LDA     $04D5               
A953: C9 40           CMP     #$40                
A955: B0 14           BCS     $A96B               ; {}
A957: A9 02           LDA     #$02                
A959: 9D 02 07        STA     $0702,X             
A95C: 60              RTS                         
A95D: AD D4 04        LDA     $04D4               
A960: C9 40           CMP     #$40                
A962: 90 F3           BCC     $A957               ; {}
A964: AD D6 04        LDA     $04D6               
A967: C9 40           CMP     #$40                
A969: B0 EC           BCS     $A957               ; {}
A96B: A9 0D           LDA     #$0D                
A96D: 9D 02 07        STA     $0702,X             
A970: 60              RTS                         
A971: BD 00 07        LDA     $0700,X             
A974: 9D 00 02        STA     $0200,X             
A977: 9D 04 02        STA     $0204,X             
A97A: BD 03 07        LDA     $0703,X             
A97D: 38              SEC                         
A97E: E9 04           SBC     #$04                
A980: 9D 03 02        STA     $0203,X             
A983: 18              CLC                         
A984: 69 08           ADC     #$08                
A986: 9D 07 02        STA     $0207,X             
A989: 60              RTS                         
A98A: A9 10           LDA     #$10                
A98C: 85 00           STA     $00                 ; {ram.GP_00}
A98E: 20 71 A9        JSR     $A971               ; {}
A991: A5 14           LDA     $14                 
A993: 4A              LSR     A                   
A994: 4A              LSR     A                   
A995: 4A              LSR     A                   
A996: 0A              ASL     A                   
A997: 29 06           AND     #$06                
A999: 18              CLC                         
A99A: 65 00           ADC     $00                 ; {ram.GP_00}
A99C: A8              TAY                         
A99D: AD C2 07        LDA     $07C2               
A9A0: 29 0F           AND     #$0F                
A9A2: C9 08           CMP     #$08                
A9A4: B0 10           BCS     $A9B6               ; {}
A9A6: B9 CB A9        LDA     $A9CB,Y             ; {}
A9A9: 9D 05 02        STA     $0205,X             
A9AC: B9 CC A9        LDA     $A9CC,Y             ; {}
A9AF: 9D 01 02        STA     $0201,X             
A9B2: A9 42           LDA     #$42                
A9B4: D0 0E           BNE     $A9C4               ; {}
A9B6: B9 CB A9        LDA     $A9CB,Y             ; {}
A9B9: 9D 01 02        STA     $0201,X             
A9BC: B9 CC A9        LDA     $A9CC,Y             ; {}
A9BF: 9D 05 02        STA     $0205,X             
A9C2: A9 02           LDA     #$02                
A9C4: 9D 02 02        STA     $0202,X             
A9C7: 9D 06 02        STA     $0206,X             
A9CA: 60              RTS                         
A9CB: D0 D1           BNE     $A99E               ; {}
A9CD: D0 D1           BNE     $A9A0               ; {}
A9CF: D8              CLD                         
A9D0: D9 D8 D9        CMP     $D9D8,Y             
A9D3: D2 ; ????
A9D4: D3 ; ????
A9D5: D2 ; ????
A9D6: D3 ; ????
A9D7: DA ; ????
A9D8: DB ; ????
A9D9: DA ; ????
A9DA: DB ; ????
A9DB: D4 ; ????
A9DC: D5 D6           CMP     $D6,X               
A9DE: D7 ; ????
A9DF: D4 ; ????
A9E0: D5 D6           CMP     $D6,X               
A9E2: D7 ; ????
A9E3: BD 01 07        LDA     $0701,X             
A9E6: 29 F8           AND     #$F8                
A9E8: C9 48           CMP     #$48                
A9EA: D0 22           BNE     $AA0E               ; {}
A9EC: 20 19 AB        JSR     $AB19               ; {}
A9EF: 20 D4 A1        JSR     $A1D4               ; {}
A9F2: BD 01 07        LDA     $0701,X             
A9F5: 29 07           AND     #$07                
A9F7: 20 2B EE        JSR     $EE2B               
A9FA: 68              PLA                         
A9FB: AA              TAX                         
A9FC: 04 ; ????
A9FD: AA              TAX                         
A9FE: 1F ; ????
A9FF: AA              TAX                         
AA00: 4E AA 97        LSR     $97AA               ; {}
AA03: A8              TAY                         
AA04: A9 08           LDA     #$08                
AA06: 85 00           STA     $00                 ; {ram.GP_00}
AA08: 20 0F AA        JSR     $AA0F               ; {}
AA0B: 20 83 AA        JSR     $AA83               ; {}
AA0E: 60              RTS                         
AA0F: AD C3 07        LDA     $07C3               
AA12: 9D 03 07        STA     $0703,X             
AA15: AD C0 07        LDA     $07C0               
AA18: 38              SEC                         
AA19: E5 00           SBC     $00                 ; {ram.GP_00}
AA1B: 9D 00 07        STA     $0700,X             
AA1E: 60              RTS                         
AA1F: 20 09 DA        JSR     $DA09               
AA22: BD 00 07        LDA     $0700,X             
AA25: C9 18           CMP     #$18                
AA27: 90 10           BCC     $AA39               ; {}
AA29: 20 82 A8        JSR     $A882               ; {}
AA2C: FE 03 07        INC     $0703,X             
AA2F: DE 00 07        DEC     $0700,X             
AA32: DE 00 07        DEC     $0700,X             
AA35: 20 83 AA        JSR     $AA83               ; {}
AA38: 60              RTS                         
AA39: FE 01 07        INC     $0701,X             
AA3C: A9 00           LDA     #$00                
AA3E: 9D 04 07        STA     $0704,X             
AA41: 9D 05 07        STA     $0705,X             
AA44: 9D 02 07        STA     $0702,X             
AA47: 60              RTS                         
AA48: 4C C3 A8        JMP     $A8C3               ; {}
AA4B: 4C C3 A8        JMP     $A8C3               ; {}
AA4E: 20 90 D9        JSR     $D990               
AA51: 90 F5           BCC     $AA48               ; {}
AA53: 20 E7 D9        JSR     $D9E7               
AA56: 90 F3           BCC     $AA4B               ; {}
AA58: 20 09 DA        JSR     $DA09               
AA5B: 20 82 A8        JSR     $A882               ; {}
AA5E: 20 6C AA        JSR     $AA6C               ; {}
AA61: 20 C0 DB        JSR     $DBC0               
AA64: 20 83 AA        JSR     $AA83               ; {}
AA67: 60              RTS                         
AA68: 20 34 DF        JSR     $DF34               
AA6B: 60              RTS                         
AA6C: AD 23 07        LDA     $0723               
AA6F: 38              SEC                         
AA70: E9 10           SBC     #$10                
AA72: DD 03 07        CMP     $0703,X             
AA75: 90 06           BCC     $AA7D               ; {}
AA77: A9 47           LDA     #$47                
AA79: 9D 02 07        STA     $0702,X             
AA7C: 60              RTS                         
AA7D: A9 48           LDA     #$48                
AA7F: 9D 02 07        STA     $0702,X             
AA82: 60              RTS                         
AA83: A9 08           LDA     #$08                
AA85: 4C 8C A9        JMP     $A98C               ; {}
AA88: BD 01 07        LDA     $0701,X             
AA8B: 29 F8           AND     #$F8                
AA8D: C9 48           CMP     #$48                
AA8F: D0 22           BNE     $AAB3               ; {}
AA91: 20 19 AB        JSR     $AB19               ; {}
AA94: 20 D4 A1        JSR     $A1D4               ; {}
AA97: BD 01 07        LDA     $0701,X             
AA9A: 29 07           AND     #$07                
AA9C: 20 2B EE        JSR     $EE2B               
AA9F: 68              PLA                         
AAA0: AA              TAX                         
AAA1: A9 AA           LDA     #$AA                
AAA3: B4 AA           LDY     $AA,X               
AAA5: E3 ; ????
AAA6: AA              TAX                         
AAA7: 97 ; ????
AAA8: A8              TAY                         
AAA9: A9 10           LDA     #$10                
AAAB: 85 00           STA     $00                 ; {ram.GP_00}
AAAD: 20 0F AA        JSR     $AA0F               ; {}
AAB0: 20 14 AB        JSR     $AB14               ; {}
AAB3: 60              RTS                         
AAB4: 20 09 DA        JSR     $DA09               
AAB7: 20 82 A8        JSR     $A882               ; {}
AABA: BD 00 07        LDA     $0700,X             
AABD: C9 18           CMP     #$18                
AABF: 90 0D           BCC     $AACE               ; {}
AAC1: DE 00 07        DEC     $0700,X             
AAC4: DE 00 07        DEC     $0700,X             
AAC7: DE 03 07        DEC     $0703,X             
AACA: 20 14 AB        JSR     $AB14               ; {}
AACD: 60              RTS                         
AACE: FE 01 07        INC     $0701,X             
AAD1: A9 00           LDA     #$00                
AAD3: 9D 02 07        STA     $0702,X             
AAD6: 9D 04 07        STA     $0704,X             
AAD9: 9D 05 07        STA     $0705,X             
AADC: 60              RTS                         
AADD: 4C C3 A8        JMP     $A8C3               ; {}
AAE0: 4C C3 A8        JMP     $A8C3               ; {}
AAE3: 20 90 D9        JSR     $D990               
AAE6: 90 F5           BCC     $AADD               ; {}
AAE8: 20 E7 D9        JSR     $D9E7               
AAEB: 90 F3           BCC     $AAE0               ; {}
AAED: 20 09 DA        JSR     $DA09               
AAF0: 20 82 A8        JSR     $A882               ; {}
AAF3: 20 FD AA        JSR     $AAFD               ; {}
AAF6: 20 C0 DB        JSR     $DBC0               
AAF9: 20 14 AB        JSR     $AB14               ; {}
AAFC: 60              RTS                         
AAFD: AD 23 07        LDA     $0723               
AB00: 18              CLC                         
AB01: 69 10           ADC     #$10                
AB03: DD 03 07        CMP     $0703,X             
AB06: 90 06           BCC     $AB0E               ; {}
AB08: A9 47           LDA     #$47                
AB0A: 9D 02 07        STA     $0702,X             
AB0D: 60              RTS                         
AB0E: A9 48           LDA     #$48                
AB10: 9D 02 07        STA     $0702,X             
AB13: 60              RTS                         
AB14: A9 00           LDA     #$00                
AB16: 20 8C A9        JSR     $A98C               ; {}
AB19: A5 3E           LDA     $3E                 
AB1B: F0 12           BEQ     $AB2F               ; {}
AB1D: A9 00           LDA     #$00                
AB1F: 9D 01 07        STA     $0701,X             
AB22: A9 F8           LDA     #$F8                
AB24: 9D 00 07        STA     $0700,X             
AB27: 9D 00 02        STA     $0200,X             
AB2A: 9D 04 02        STA     $0204,X             
AB2D: 68              PLA                         
AB2E: 68              PLA                         
AB2F: 60              RTS                         
AB30: A5 00           LDA     $00                 ; {ram.GP_00}
AB32: 85 02           STA     $02                 
AB34: 38              SEC                         
AB35: E9 F0           SBC     #$F0                
AB37: 85 00           STA     $00                 ; {ram.GP_00}
AB39: A5 01           LDA     $01                 
AB3B: E9 05           SBC     #$05                
AB3D: 85 01           STA     $01                 
AB3F: B0 04           BCS     $AB45               ; {}
AB41: A5 02           LDA     $02                 
AB43: 85 00           STA     $00                 ; {ram.GP_00}
AB45: A9 08           LDA     #$08                
AB47: 85 01           STA     $01                 
AB49: A5 00           LDA     $00                 ; {ram.GP_00}
AB4B: 48              PHA                         
AB4C: 29 F0           AND     #$F0                
AB4E: 0A              ASL     A                   
AB4F: 26 01           ROL     $01                 
AB51: 0A              ASL     A                   
AB52: 26 01           ROL     $01                 
AB54: 85 00           STA     $00                 ; {ram.GP_00}
AB56: 68              PLA                         
AB57: 29 0F           AND     #$0F                
AB59: 0A              ASL     A                   
AB5A: 18              CLC                         
AB5B: 65 00           ADC     $00                 ; {ram.GP_00}
AB5D: 85 00           STA     $00                 ; {ram.GP_00}
AB5F: AD D1 04        LDA     $04D1               
AB62: 4A              LSR     A                   
AB63: B0 07           BCS     $AB6C               ; {}
AB65: A5 01           LDA     $01                 
AB67: 18              CLC                         
AB68: 69 04           ADC     #$04                
AB6A: 85 01           STA     $01                 
AB6C: 60              RTS                         
AB6D: A5 3E           LDA     $3E                 
AB6F: F0 0F           BEQ     $AB80               ; {}
AB71: C9 01           CMP     #$01                
AB73: F0 0C           BEQ     $AB81               ; {}
AB75: A9 F8           LDA     #$F8                
AB77: 9D 10 02        STA     $0210,X             
AB7A: 9D 14 02        STA     $0214,X             
AB7D: 4C 62 DF        JMP     $DF62               
AB80: 60              RTS                         
AB81: 20 62 DF        JSR     $DF62               
AB84: 68              PLA                         
AB85: 68              PLA                         
AB86: 60              RTS                         
AB87: A2 50           LDX     #$50                
AB89: A9 80           LDA     #$80                
AB8B: 9D 01 07        STA     $0701,X             
AB8E: 0A              ASL     A                   
AB8F: 9D 00 07        STA     $0700,X             
AB92: 85 A1           STA     $A1                 
AB94: 60              RTS                         
AB95: A2 50           LDX     #$50                
AB97: BD 01 07        LDA     $0701,X             
AB9A: 10 0F           BPL     $ABAB               ; {}
AB9C: 20 D4 A1        JSR     $A1D4               ; {}
AB9F: BD 01 07        LDA     $0701,X             
ABA2: 29 0F           AND     #$0F                
ABA4: 20 2B EE        JSR     $EE2B               
ABA7: AC AB F8        LDY     $F8AB               
ABAA: AB ; ????
ABAB: 60              RTS                         
ABAC: A5 A1           LDA     $A1                 
ABAE: CD EA BE        CMP     $BEEA               ; {}
ABB1: 90 06           BCC     $ABB9               ; {}
ABB3: A9 00           LDA     #$00                
ABB5: 9D 01 07        STA     $0701,X             
ABB8: 60              RTS                         
ABB9: 85 00           STA     $00                 ; {ram.GP_00}
ABBB: 0A              ASL     A                   
ABBC: 18              CLC                         
ABBD: 65 00           ADC     $00                 ; {ram.GP_00}
ABBF: A8              TAY                         
ABC0: B9 EB BE        LDA     $BEEB,Y             ; {}
ABC3: CD 30 01        CMP     $0130               
ABC6: 90 17           BCC     $ABDF               ; {}
ABC8: D0 E1           BNE     $ABAB               ; {}
ABCA: B9 EC BE        LDA     $BEEC,Y             ; {}
ABCD: CD D1 04        CMP     $04D1               
ABD0: 90 0D           BCC     $ABDF               ; {}
ABD2: D0 D7           BNE     $ABAB               ; {}
ABD4: B9 ED BE        LDA     $BEED,Y             ; {}
ABD7: 29 F0           AND     #$F0                
ABD9: C5 FE           CMP     $FE                 
ABDB: F0 06           BEQ     $ABE3               ; {}
ABDD: 90 CC           BCC     $ABAB               ; {}
ABDF: E6 A1           INC     $A1                 
ABE1: D0 C9           BNE     $ABAC               ; {}
ABE3: A9 00           LDA     #$00                
ABE5: 9D 00 07        STA     $0700,X             
ABE8: B9 ED BE        LDA     $BEED,Y             ; {}
ABEB: 0A              ASL     A                   
ABEC: 0A              ASL     A                   
ABED: 0A              ASL     A                   
ABEE: 0A              ASL     A                   
ABEF: 9D 03 07        STA     $0703,X             
ABF2: A9 81           LDA     #$81                
ABF4: 9D 01 07        STA     $0701,X             
ABF7: 60              RTS                         
ABF8: BD 00 07        LDA     $0700,X             
ABFB: C9 F8           CMP     #$F8                
ABFD: B0 0D           BCS     $AC0C               ; {}
ABFF: 20 8A D9        JSR     $D98A               
AC02: 90 04           BCC     $AC08               ; {}
AC04: 20 15 AC        JSR     $AC15               ; {}
AC07: 60              RTS                         
AC08: A9 FF           LDA     #$FF                
AC0A: 85 3E           STA     $3E                 
AC0C: A9 80           LDA     #$80                
AC0E: 9D 01 07        STA     $0701,X             
AC11: 20 2B DD        JSR     $DD2B               
AC14: 60              RTS                         
AC15: A9 19           LDA     #$19                
AC17: 20 67 C6        JSR     $C667               
AC1A: 60              RTS                         
AC1B: BD 00 07        LDA     $0700,X             
AC1E: C9 F8           CMP     #$F8                
AC20: B0 08           BCS     $AC2A               ; {}
AC22: BD 03 07        LDA     $0703,X             
AC25: C9 FC           CMP     #$FC                
AC27: B0 01           BCS     $AC2A               ; {}
AC29: 60              RTS                         
AC2A: 68              PLA                         
AC2B: 68              PLA                         
AC2C: 20 1D DD        JSR     $DD1D               
AC2F: 8A              TXA                         
AC30: 48              PHA                         
AC31: 18              CLC                         
AC32: 69 10           ADC     #$10                
AC34: 8A              TXA                         
AC35: 20 1D DD        JSR     $DD1D               
AC38: 68              PLA                         
AC39: AA              TAX                         
AC3A: 60              RTS                         
AC3B: 20 83 EF        JSR     $EF83               
AC3E: A9 40           LDA     #$40                
AC40: 85 37           STA     $37                 
AC42: 20 E5 EE        JSR     $EEE5               
AC45: A9 00           LDA     #$00                
AC47: 85 14           STA     $14                 
AC49: 85 15           STA     $15                 
AC4B: 85 82           STA     $82                 
AC4D: 85 81           STA     $81                 
AC4F: E6 1A           INC     $1A                 
AC51: 20 CA EE        JSR     $EECA               
AC54: 20 20 EF        JSR     $EF20               
AC57: 20 21 7F        JSR     $7F21               
AC5A: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
AC5D: 10 FB           BPL     $AC5A               ; {}
AC5F: 20 42 EE        JSR     $EE42               
AC62: 20 01 EF        JSR     $EF01               
AC65: A5 37           LDA     $37                 
AC67: D0 FC           BNE     $AC65               ; {}
AC69: 20 F0 EE        JSR     $EEF0               
AC6C: 4C 9C 9C        JMP     $9C9C               ; {}
AC6F: A2 A0           LDX     #$A0                
AC71: A0 23           LDY     #$23                
AC73: A9 00           LDA     #$00                
AC75: 9D 00 07        STA     $0700,X             
AC78: E8              INX                         
AC79: 88              DEY                         
AC7A: 10 F9           BPL     $AC75               ; {}
AC7C: A2 C4           LDX     #$C4                
AC7E: A9 70           LDA     #$70                
AC80: 9D 00 07        STA     $0700,X             
AC83: A9 C0           LDA     #$C0                
AC85: 9D 03 07        STA     $0703,X             
AC88: A9 96           LDA     #$96                
AC8A: 9D 01 07        STA     $0701,X             
AC8D: A9 00           LDA     #$00                
AC8F: 9D 02 07        STA     $0702,X             
AC92: A9 00           LDA     #$00                
AC94: 9D 04 07        STA     $0704,X             
AC97: 60              RTS                         
AC98: 48              PHA                         
AC99: 20 21 EB        JSR     $EB21               
AC9C: A0 10           LDY     #$10                
AC9E: 4A              LSR     A                   
AC9F: 90 02           BCC     $ACA3               ; {}
ACA1: A0 08           LDY     #$08                
ACA3: 4A              LSR     A                   
ACA4: 90 02           BCC     $ACA8               ; {}
ACA6: A0 00           LDY     #$00                
ACA8: 8C 63 07        STY     $0763               
ACAB: A9 40           LDA     #$40                
ACAD: 8D 60 07        STA     $0760               
ACB0: A9 00           LDA     #$00                
ACB2: 8D 61 07        STA     $0761               
ACB5: A9 C0           LDA     #$C0                
ACB7: 8D 62 07        STA     $0762               
ACBA: 68              PLA                         
ACBB: 60              RTS                         
ACBC: 20 F9 E3        JSR     $E3F9               
ACBF: A2 00           LDX     #$00                
ACC1: 86 82           STX     $82                 
ACC3: A5 14           LDA     $14                 
ACC5: 38              SEC                         
ACC6: FD 48 AD        SBC     $AD48,X             ; {}
ACC9: 85 00           STA     $00                 ; {ram.GP_00}
ACCB: A5 15           LDA     $15                 
ACCD: FD 49 AD        SBC     $AD49,X             ; {}
ACD0: 85 01           STA     $01                 
ACD2: 90 16           BCC     $ACEA               ; {}
ACD4: E8              INX                         
ACD5: E8              INX                         
ACD6: E6 82           INC     $82                 
ACD8: A5 00           LDA     $00                 ; {ram.GP_00}
ACDA: D0 E7           BNE     $ACC3               ; {}
ACDC: A5 01           LDA     $01                 
ACDE: D0 E3           BNE     $ACC3               ; {}
ACE0: A5 82           LDA     $82                 
ACE2: C9 01           CMP     #$01                
ACE4: D0 04           BNE     $ACEA               ; {}
ACE6: A9 01           LDA     #$01                
ACE8: 85 86           STA     $86                 
ACEA: A5 82           LDA     $82                 
ACEC: 20 2B EE        JSR     $EE2B               
ACEF: F7 ; ????
ACF0: AC 00 AD        LDY     $AD00               ; {}
ACF3: 10 AD           BPL     $ACA2               ; {}
ACF5: 43 ; ????
ACF6: AD A5 14        LDA     $14A5               
ACF9: 6A              ROR     A                   
ACFA: 90 01           BCC     $ACFD               ; {}
ACFC: 60              RTS                         
ACFD: 4C 05 B1        JMP     $B105               ; {}
AD00: A2 30           LDX     #$30                
AD02: BD 13 AD        LDA     $AD13,X             ; {}
AD05: 9D 00 61        STA     $6100,X             
AD08: CA              DEX                         
AD09: 10 F7           BPL     $AD02               ; {}
AD0B: A9 0E           LDA     #$0E                
AD0D: 8D E2 04        STA     $04E2               
AD10: 4C 05 B1        JMP     $B105               ; {}
AD13: FE E5 28        INC     $28E5,X             
AD16: 25 1E           AND     $1E                 
AD18: 29 12           AND     #$12                
AD1A: 1A ; ????
AD1B: 26 2A           ROL     $2A                 
AD1D: 1E 25 25        ASL     $2525,X             
AD20: 1A ; ????
AD21: 19 12 1D        ORA     $1D12,Y             
AD24: 1E 22 28        ASL     $2822,X             
AD27: 1A ; ????
AD28: 21 1B           AND     ($1B,X)             
AD2A: FE 25 29        INC     $2925,X             
AD2D: 2C 1E 29        BIT     $291E               
AD30: 1D 12 29        ORA     $2912,X             
AD33: 1D 1A 12        ORA     $121A,X             
AD36: 03 ; ????
AD37: 12 ; ????
AD38: 29 27           AND     #$27                
AD3A: 1A ; ????
AD3B: 16 28           ASL     $28,X               
AD3D: 2A              ROL     A                   
AD3E: 27 ; ????
AD3F: 1A ; ????
AD40: 28              PLP                         
AD41: 0E FF A9        ASL     $A9FF               ; {}
AD44: 00              BRK                         
AD45: 85 37           STA     $37                 
AD47: 60              RTS                         
AD48: 80 ; ????
AD49: 00              BRK                         
AD4A: 81 00           STA     ($00,X)             ; {ram.GP_00}
AD4C: 00              BRK                         
AD4D: 02 ; ????
AD4E: FF ; ????
AD4F: FF ; ????
AD50: 20 B5 B1        JSR     $B1B5               ; {}
AD53: A0 5C           LDY     #$5C                
AD55: A9 F8           LDA     #$F8                
AD57: 91 87           STA     ($87),Y             
AD59: 88              DEY                         
AD5A: 88              DEY                         
AD5B: 88              DEY                         
AD5C: 88              DEY                         
AD5D: 10 F8           BPL     $AD57               ; {}
AD5F: A5 81           LDA     $81                 
AD61: 29 07           AND     #$07                
AD63: 20 2B EE        JSR     $EE2B               
AD66: 70 AD           BVS     $AD15               ; {}
AD68: 70 AD           BVS     $AD17               ; {}
AD6A: E3 ; ????
AD6B: AD 87 AE        LDA     $AE87               ; {}
AD6E: E0 AE           CPX     #$AE                
AD70: AD 23 07        LDA     $0723               
AD73: C9 B8           CMP     #$B8                
AD75: 90 06           BCC     $AD7D               ; {}
AD77: CE 23 07        DEC     $0723               
AD7A: CE 23 07        DEC     $0723               
AD7D: A9 03           LDA     #$03                
AD7F: 8D FF 07        STA     $07FF               
AD82: 20 F7 AE        JSR     $AEF7               ; {}
AD85: A9 05           LDA     #$05                
AD87: 8D FF 07        STA     $07FF               
AD8A: 20 FE AF        JSR     $AFFE               ; {}
AD8D: 20 3B AE        JSR     $AE3B               ; {}
AD90: A2 C4           LDX     #$C4                
AD92: 20 90 D9        JSR     $D990               
AD95: B0 4B           BCS     $ADE2               ; {}
AD97: 98              TYA                         
AD98: 48              PHA                         
AD99: 20 81 B4        JSR     $B481               ; {}
AD9C: 68              PLA                         
AD9D: A8              TAY                         
AD9E: A9 F8           LDA     #$F8                
ADA0: 8D 38 07        STA     $0738               
ADA3: 8D 3C 07        STA     $073C               
ADA6: 8D 40 07        STA     $0740               
ADA9: 8D 44 07        STA     $0744               
ADAC: A9 10           LDA     #$10                
ADAE: 8D C8 07        STA     $07C8               
ADB1: AD 52 01        LDA     $0152               
ADB4: 29 07           AND     #$07                
ADB6: A8              TAY                         
ADB7: BD 01 07        LDA     $0701,X             
ADBA: 38              SEC                         
ADBB: F9 D6 DC        SBC     $DCD6,Y             
ADBE: 9D 01 07        STA     $0701,X             
ADC1: BD 02 07        LDA     $0702,X             
ADC4: E9 00           SBC     #$00                
ADC6: 9D 02 07        STA     $0702,X             
ADC9: B0 17           BCS     $ADE2               ; {}
ADCB: A9 19           LDA     #$19                
ADCD: 8D AD 03        STA     $03AD               
ADD0: A9 29           LDA     #$29                
ADD2: 8D AE 03        STA     $03AE               
ADD5: A9 38           LDA     #$38                
ADD7: 8D AF 03        STA     $03AF               
ADDA: A9 00           LDA     #$00                
ADDC: 85 14           STA     $14                 
ADDE: 85 15           STA     $15                 
ADE0: E6 81           INC     $81                 
ADE2: 60              RTS                         
ADE3: A9 00           LDA     #$00                
ADE5: 85 FD           STA     $FD                 
ADE7: A9 00           LDA     #$00                
ADE9: 20 53 AE        JSR     $AE53               ; {}
ADEC: A9 0F           LDA     #$0F                
ADEE: 8D 91 03        STA     $0391               
ADF1: 8D 92 03        STA     $0392               
ADF4: 8D A0 03        STA     $03A0               
ADF7: A0 02           LDY     #$02                
ADF9: A5 15           LDA     $15                 
ADFB: D0 36           BNE     $AE33               ; {}
ADFD: A5 14           LDA     $14                 
ADFF: C9 80           CMP     #$80                
AE01: B0 06           BCS     $AE09               ; {}
AE03: 29 03           AND     #$03                
AE05: F0 33           BEQ     $AE3A               ; {}
AE07: A0 00           LDY     #$00                
AE09: A9 08           LDA     #$08                
AE0B: C0 00           CPY     #$00                
AE0D: F0 02           BEQ     $AE11               ; {}
AE0F: A9 05           LDA     #$05                
AE11: 85 8C           STA     $8C                 
AE13: B9 A1 B3        LDA     $B3A1,Y             ; {}
AE16: 85 89           STA     $89                 
AE18: B9 A2 B3        LDA     $B3A2,Y             ; {}
AE1B: 85 8A           STA     $8A                 
AE1D: A9 70           LDA     #$70                
AE1F: 85 8D           STA     $8D                 
AE21: A9 C0           LDA     #$C0                
AE23: 18              CLC                         
AE24: 69 10           ADC     #$10                
AE26: 85 8E           STA     $8E                 
AE28: A9 00           LDA     #$00                
AE2A: 85 8B           STA     $8B                 
AE2C: A9 03           LDA     #$03                
AE2E: 85 8F           STA     $8F                 
AE30: 4C BE B1        JMP     $B1BE               ; {}
AE33: E6 81           INC     $81                 
AE35: A9 FF           LDA     #$FF                
AE37: 8D C8 07        STA     $07C8               
AE3A: 60              RTS                         
AE3B: AD C8 07        LDA     $07C8               
AE3E: F0 44           BEQ     $AE84               ; {}
AE40: 29 03           AND     #$03                
AE42: D0 05           BNE     $AE49               ; {}
AE44: A9 01           LDA     #$01                
AE46: 8D 84 03        STA     $0384               
AE49: CE C8 07        DEC     $07C8               
AE4C: AD C8 07        LDA     $07C8               
AE4F: 29 01           AND     #$01                
AE51: 0A              ASL     A                   
AE52: 0A              ASL     A                   
AE53: A8              TAY                         
AE54: A2 00           LDX     #$00                
AE56: B9 45 B3        LDA     $B345,Y             ; {}
AE59: 9D 90 03        STA     $0390,X             
AE5C: B9 4D B3        LDA     $B34D,Y             ; {}
AE5F: 9D 98 03        STA     $0398,X             
AE62: C8              INY                         
AE63: E8              INX                         
AE64: E0 04           CPX     #$04                
AE66: D0 EE           BNE     $AE56               ; {}
AE68: AD C8 07        LDA     $07C8               
AE6B: 29 01           AND     #$01                
AE6D: A8              TAY                         
AE6E: B9 85 AE        LDA     $AE85,Y             ; {}
AE71: 8D A0 03        STA     $03A0               
AE74: AD C8 07        LDA     $07C8               
AE77: 29 03           AND     #$03                
AE79: A8              TAY                         
AE7A: B9 80 AE        LDA     $AE80,Y             ; {}
AE7D: 85 FD           STA     $FD                 
AE7F: 60              RTS                         
AE80: 00              BRK                         
AE81: 02 ; ????
AE82: 04 ; ????
AE83: 02 ; ????
AE84: 60              RTS                         
AE85: 0F ; ????
AE86: 16 A0           ASL     $A0,X               
AE88: 02 ; ????
AE89: A9 05           LDA     #$05                
AE8B: 85 8C           STA     $8C                 
AE8D: B9 A1 B3        LDA     $B3A1,Y             ; {}
AE90: 85 89           STA     $89                 
AE92: B9 A2 B3        LDA     $B3A2,Y             ; {}
AE95: 85 8A           STA     $8A                 
AE97: A9 70           LDA     #$70                
AE99: 85 8D           STA     $8D                 
AE9B: A9 C0           LDA     #$C0                
AE9D: 18              CLC                         
AE9E: 69 10           ADC     #$10                
AEA0: 85 8E           STA     $8E                 
AEA2: A9 00           LDA     #$00                
AEA4: 85 8B           STA     $8B                 
AEA6: A9 03           LDA     #$03                
AEA8: 85 8F           STA     $8F                 
AEAA: 20 BE B1        JSR     $B1BE               ; {}
AEAD: 20 3B AE        JSR     $AE3B               ; {}
AEB0: AD A0 03        LDA     $03A0               
AEB3: 8D 91 03        STA     $0391               
AEB6: 8D 92 03        STA     $0392               
AEB9: AD C8 07        LDA     $07C8               
AEBC: C9 01           CMP     #$01                
AEBE: D0 C4           BNE     $AE84               ; {}
AEC0: A9 0F           LDA     #$0F                
AEC2: 8D A0 03        STA     $03A0               
AEC5: 8D 91 03        STA     $0391               
AEC8: 8D 92 03        STA     $0392               
AECB: E6 81           INC     $81                 
AECD: A9 00           LDA     #$00                
AECF: A2 03           LDX     #$03                
AED1: 9D AC 05        STA     $05AC,X             
AED4: 9D BC 05        STA     $05BC,X             
AED7: CA              DEX                         
AED8: 10 F7           BPL     $AED1               ; {}
AEDA: A9 20           LDA     #$20                
AEDC: 8D 84 03        STA     $0384               
AEDF: 60              RTS                         
AEE0: A2 20           LDX     #$20                
AEE2: BD 03 07        LDA     $0703,X             
AEE5: C9 F4           CMP     #$F4                
AEE7: B0 01           BCS     $AEEA               ; {}
AEE9: 60              RTS                         
AEEA: A0 03           LDY     #$03                
AEEC: 20 83 B4        JSR     $B483               ; {}
AEEF: 20 D9 B3        JSR     $B3D9               ; {}
AEF2: A9 80           LDA     #$80                
AEF4: 85 AB           STA     $AB                 
AEF6: 60              RTS                         
AEF7: CE 62 07        DEC     $0762               
AEFA: EE 61 07        INC     $0761               
AEFD: AD 61 07        LDA     $0761               
AF00: D0 03           BNE     $AF05               ; {}
AF02: 20 98 AC        JSR     $AC98               ; {}
AF05: C9 E0           CMP     #$E0                
AF07: 90 01           BCC     $AF0A               ; {}
AF09: 60              RTS                         
AF0A: 2C 60 07        BIT     $0760               
AF0D: 70 01           BVS     $AF10               ; {}
AF0F: 60              RTS                         
AF10: 20 3B AF        JSR     $AF3B               ; {}
AF13: 20 5A AF        JSR     $AF5A               ; {}
AF16: A2 64           LDX     #$64                
AF18: A0 20           LDY     #$20                
AF1A: 20 86 D9        JSR     $D986               
AF1D: B0 03           BCS     $AF22               ; {}
AF1F: 20 16 B1        JSR     $B116               ; {}
AF22: 20 90 D9        JSR     $D990               
AF25: B0 11           BCS     $AF38               ; {}
AF27: 20 56 A1        JSR     $A156               ; {}
AF2A: 20 81 B4        JSR     $B481               ; {}
AF2D: A9 80           LDA     #$80                
AF2F: 8D 60 07        STA     $0760               
AF32: A9 C0           LDA     #$C0                
AF34: 8D 61 07        STA     $0761               
AF37: 60              RTS                         
AF38: 4C A1 AF        JMP     $AFA1               ; {}
AF3B: A2 64           LDX     #$64                
AF3D: AD 62 07        LDA     $0762               
AF40: 9D 03 07        STA     $0703,X             
AF43: C9 C0           CMP     #$C0                
AF45: 90 04           BCC     $AF4B               ; {}
AF47: A9 F8           LDA     #$F8                
AF49: D0 0B           BNE     $AF56               ; {}
AF4B: AD 61 07        LDA     $0761               
AF4E: 18              CLC                         
AF4F: 6D 63 07        ADC     $0763               
AF52: A8              TAY                         
AF53: B9 45 B2        LDA     $B245,Y             ; {}
AF56: 9D 00 07        STA     $0700,X             
AF59: 60              RTS                         
AF5A: A9 0C           LDA     #$0C                
AF5C: 85 80           STA     $80                 
AF5E: A2 68           LDX     #$68                
AF60: A9 02           LDA     #$02                
AF62: 85 82           STA     $82                 
AF64: AD 62 07        LDA     $0762               
AF67: 18              CLC                         
AF68: 65 82           ADC     $82                 
AF6A: 9D 03 07        STA     $0703,X             
AF6D: C9 C0           CMP     #$C0                
AF6F: 90 04           BCC     $AF75               ; {}
AF71: A9 F8           LDA     #$F8                
AF73: D0 0E           BNE     $AF83               ; {}
AF75: AD 61 07        LDA     $0761               
AF78: 38              SEC                         
AF79: E5 82           SBC     $82                 
AF7B: 18              CLC                         
AF7C: 6D 63 07        ADC     $0763               
AF7F: A8              TAY                         
AF80: B9 45 B2        LDA     $B245,Y             ; {}
AF83: 9D 00 07        STA     $0700,X             
AF86: E6 82           INC     $82                 
AF88: E6 82           INC     $82                 
AF8A: 98              TYA                         
AF8B: 48              PHA                         
AF8C: A0 20           LDY     #$20                
AF8E: 20 86 D9        JSR     $D986               
AF91: B0 03           BCS     $AF96               ; {}
AF93: 20 16 B1        JSR     $B116               ; {}
AF96: 68              PLA                         
AF97: A8              TAY                         
AF98: E8              INX                         
AF99: E8              INX                         
AF9A: E8              INX                         
AF9B: E8              INX                         
AF9C: C6 80           DEC     $80                 
AF9E: D0 C4           BNE     $AF64               ; {}
AFA0: 60              RTS                         
AFA1: A2 64           LDX     #$64                
AFA3: BD 00 07        LDA     $0700,X             
AFA6: 85 8D           STA     $8D                 
AFA8: BD 03 07        LDA     $0703,X             
AFAB: 85 8E           STA     $8E                 
AFAD: A5 14           LDA     $14                 
AFAF: 29 08           AND     #$08                
AFB1: F0 02           BEQ     $AFB5               ; {}
AFB3: A9 01           LDA     #$01                
AFB5: 0A              ASL     A                   
AFB6: A8              TAY                         
AFB7: B9 71 B3        LDA     $B371,Y             ; {}
AFBA: 85 89           STA     $89                 
AFBC: B9 72 B3        LDA     $B372,Y             ; {}
AFBF: 85 8A           STA     $8A                 
AFC1: A9 04           LDA     #$04                
AFC3: 85 8C           STA     $8C                 
AFC5: A9 00           LDA     #$00                
AFC7: 85 8B           STA     $8B                 
AFC9: A9 03           LDA     #$03                
AFCB: 85 8F           STA     $8F                 
AFCD: 20 BE B1        JSR     $B1BE               ; {}
AFD0: A9 68           LDA     #$68                
AFD2: 48              PHA                         
AFD3: AA              TAX                         
AFD4: BD 00 07        LDA     $0700,X             
AFD7: 85 8D           STA     $8D                 
AFD9: BD 03 07        LDA     $0703,X             
AFDC: 85 8E           STA     $8E                 
AFDE: A9 95           LDA     #$95                
AFE0: 85 89           STA     $89                 
AFE2: A9 B3           LDA     #$B3                
AFE4: 85 8A           STA     $8A                 
AFE6: A9 01           LDA     #$01                
AFE8: 85 8C           STA     $8C                 
AFEA: A9 00           LDA     #$00                
AFEC: 85 8B           STA     $8B                 
AFEE: A9 03           LDA     #$03                
AFF0: 85 8F           STA     $8F                 
AFF2: 20 BE B1        JSR     $B1BE               ; {}
AFF5: 68              PLA                         
AFF6: 18              CLC                         
AFF7: 69 04           ADC     #$04                
AFF9: C9 98           CMP     #$98                
AFFB: D0 D5           BNE     $AFD2               ; {}
AFFD: 60              RTS                         
AFFE: A5 14           LDA     $14                 
B000: 29 1F           AND     #$1F                
B002: D0 1A           BNE     $B01E               ; {}
B004: A5 14           LDA     $14                 
B006: 29 60           AND     #$60                
B008: 18              CLC                         
B009: 2A              ROL     A                   
B00A: 2A              ROL     A                   
B00B: 2A              ROL     A                   
B00C: 2A              ROL     A                   
B00D: 85 00           STA     $00                 ; {ram.GP_00}
B00F: E6 00           INC     $00                 ; {ram.GP_00}
B011: A9 97           LDA     #$97                
B013: 18              CLC                         
B014: 69 09           ADC     #$09                
B016: C6 00           DEC     $00                 ; {ram.GP_00}
B018: D0 F9           BNE     $B013               ; {}
B01A: AA              TAX                         
B01B: 20 21 B0        JSR     $B021               ; {}
B01E: 4C 8F B0        JMP     $B08F               ; {}
B021: A0 20           LDY     #$20                
B023: A9 C0           LDA     #$C0                
B025: 9D 03 07        STA     $0703,X             
B028: 38              SEC                         
B029: F9 03 07        SBC     $0703,Y             
B02C: F0 02           BEQ     $B030               ; {}
B02E: B0 06           BCS     $B036               ; {}
B030: A9 00           LDA     #$00                
B032: 9D 01 07        STA     $0701,X             
B035: 60              RTS                         
B036: 85 03           STA     $03                 
B038: A9 00           LDA     #$00                
B03A: 85 04           STA     $04                 
B03C: A9 40           LDA     #$40                
B03E: 9D 01 07        STA     $0701,X             
B041: A9 70           LDA     #$70                
B043: 9D 00 07        STA     $0700,X             
B046: 38              SEC                         
B047: F9 00 07        SBC     $0700,Y             
B04A: 85 02           STA     $02                 
B04C: 10 0A           BPL     $B058               ; {}
B04E: A0 08           LDY     #$08                
B050: 49 FF           EOR     #$FF                
B052: 85 02           STA     $02                 
B054: E6 02           INC     $02                 
B056: D0 02           BNE     $B05A               ; {}
B058: A0 00           LDY     #$00                
B05A: A9 00           LDA     #$00                
B05C: 85 01           STA     $01                 
B05E: 84 08           STY     $08                 
B060: 20 56 B1        JSR     $B156               ; {}
B063: A0 06           LDY     #$06                
B065: 46 02           LSR     $02                 
B067: 66 01           ROR     $01                 
B069: 88              DEY                         
B06A: D0 F9           BNE     $B065               ; {}
B06C: A5 01           LDA     $01                 
B06E: 29 07           AND     #$07                
B070: 18              CLC                         
B071: 65 08           ADC     $08                 
B073: 0A              ASL     A                   
B074: 0A              ASL     A                   
B075: A8              TAY                         
B076: B9 09 B2        LDA     $B209,Y             ; {}
B079: 9D 06 07        STA     $0706,X             
B07C: B9 0A B2        LDA     $B20A,Y             ; {}
B07F: 9D 05 07        STA     $0705,X             
B082: B9 0B B2        LDA     $B20B,Y             ; {}
B085: 9D 08 07        STA     $0708,X             
B088: B9 0C B2        LDA     $B20C,Y             ; {}
B08B: 9D 07 07        STA     $0707,X             
B08E: 60              RTS                         
B08F: A9 04           LDA     #$04                
B091: 85 04           STA     $04                 
B093: A2 A0           LDX     #$A0                
B095: BD 01 07        LDA     $0701,X             
B098: F0 2F           BEQ     $B0C9               ; {}
B09A: 30 2D           BMI     $B0C9               ; {}
B09C: BD 02 07        LDA     $0702,X             
B09F: 18              CLC                         
B0A0: 7D 06 07        ADC     $0706,X             
B0A3: 9D 02 07        STA     $0702,X             
B0A6: BD 00 07        LDA     $0700,X             
B0A9: 7D 05 07        ADC     $0705,X             
B0AC: 9D 00 07        STA     $0700,X             
B0AF: BD 04 07        LDA     $0704,X             
B0B2: 18              CLC                         
B0B3: 7D 08 07        ADC     $0708,X             
B0B6: 9D 04 07        STA     $0704,X             
B0B9: BD 03 07        LDA     $0703,X             
B0BC: 7D 07 07        ADC     $0707,X             
B0BF: 9D 03 07        STA     $0703,X             
B0C2: 8A              TXA                         
B0C3: 48              PHA                         
B0C4: 20 7F B1        JSR     $B17F               ; {}
B0C7: 68              PLA                         
B0C8: AA              TAX                         
B0C9: 8A              TXA                         
B0CA: 18              CLC                         
B0CB: 69 09           ADC     #$09                
B0CD: AA              TAX                         
B0CE: C6 04           DEC     $04                 
B0D0: D0 C3           BNE     $B095               ; {}
B0D2: A9 04           LDA     #$04                
B0D4: A2 A0           LDX     #$A0                
B0D6: 48              PHA                         
B0D7: 8A              TXA                         
B0D8: 48              PHA                         
B0D9: BD 01 07        LDA     $0701,X             
B0DC: 29 40           AND     #$40                
B0DE: F0 19           BEQ     $B0F9               ; {}
B0E0: A0 20           LDY     #$20                
B0E2: 20 86 D9        JSR     $D986               
B0E5: B0 12           BCS     $B0F9               ; {}
B0E7: A5 1F           LDA     $1F                 
B0E9: D0 0B           BNE     $B0F6               ; {}
B0EB: A5 1C           LDA     $1C                 
B0ED: 30 07           BMI     $B0F6               ; {}
B0EF: A9 80           LDA     #$80                
B0F1: 9D 01 07        STA     $0701,X             
B0F4: D0 03           BNE     $B0F9               ; {}
B0F6: 20 16 B1        JSR     $B116               ; {}
B0F9: 68              PLA                         
B0FA: 18              CLC                         
B0FB: 69 09           ADC     #$09                
B0FD: AA              TAX                         
B0FE: 68              PLA                         
B0FF: A8              TAY                         
B100: 88              DEY                         
B101: 98              TYA                         
B102: D0 D2           BNE     $B0D6               ; {}
B104: 60              RTS                         
B105: A0 00           LDY     #$00                
B107: B9 55 B3        LDA     $B355,Y             ; {}
B10A: 99 00 02        STA     $0200,Y             
B10D: C8              INY                         
B10E: C0 1C           CPY     #$1C                
B110: D0 F5           BNE     $B107               ; {}
B112: 60              RTS                         
B113: 4C 05 DA        JMP     $DA05               
B116: A5 A2           LDA     $A2                 
B118: 30 F9           BMI     $B113               ; {}
B11A: B9 08 07        LDA     $0708,Y             
B11D: D0 F4           BNE     $B113               ; {}
B11F: B9 01 07        LDA     $0701,Y             
B122: 29 40           AND     #$40                
B124: D0 ED           BNE     $B113               ; {}
B126: B9 03 07        LDA     $0703,Y             
B129: C9 0C           CMP     #$0C                
B12B: 90 06           BCC     $B133               ; {}
B12D: 38              SEC                         
B12E: E9 08           SBC     #$08                
B130: 99 03 07        STA     $0703,Y             
B133: A9 7F           LDA     #$7F                
B135: 99 08 07        STA     $0708,Y             
B138: A9 40           LDA     #$40                
B13A: 8D 82 03        STA     $0382               
B13D: 98              TYA                         
B13E: 48              PHA                         
B13F: A9 03           LDA     #$03                
B141: 20 37 E3        JSR     $E337               
B144: 68              PLA                         
B145: A8              TAY                         
B146: A5 A6           LDA     $A6                 
B148: 38              SEC                         
B149: ED FF 07        SBC     $07FF               
B14C: B0 02           BCS     $B150               ; {}
B14E: A9 00           LDA     #$00                
B150: 85 A6           STA     $A6                 
B152: 20 69 DA        JSR     $DA69               
B155: 60              RTS                         
B156: A9 00           LDA     #$00                
B158: 85 05           STA     $05                 
B15A: 85 06           STA     $06                 
B15C: A0 0F           LDY     #$0F                
B15E: 06 01           ASL     $01                 
B160: 26 02           ROL     $02                 
B162: 26 05           ROL     $05                 
B164: 26 06           ROL     $06                 
B166: A5 05           LDA     $05                 
B168: 38              SEC                         
B169: E5 03           SBC     $03                 
B16B: 85 07           STA     $07                 
B16D: A5 06           LDA     $06                 
B16F: E5 04           SBC     $04                 
B171: 90 08           BCC     $B17B               ; {}
B173: 85 06           STA     $06                 
B175: A5 07           LDA     $07                 
B177: 85 05           STA     $05                 
B179: E6 01           INC     $01                 
B17B: 88              DEY                         
B17C: 10 E0           BPL     $B15E               ; {}
B17E: 60              RTS                         
B17F: BD 00 07        LDA     $0700,X             
B182: C9 F0           CMP     #$F0                
B184: B0 29           BCS     $B1AF               ; {}
B186: 85 8D           STA     $8D                 
B188: BD 03 07        LDA     $0703,X             
B18B: C9 C0           CMP     #$C0                
B18D: B0 20           BCS     $B1AF               ; {}
B18F: 85 8E           STA     $8E                 
B191: A9 99           LDA     #$99                
B193: 85 89           STA     $89                 
B195: A9 B3           LDA     #$B3                
B197: 85 8A           STA     $8A                 
B199: A9 02           LDA     #$02                
B19B: 85 8C           STA     $8C                 
B19D: A9 00           LDA     #$00                
B19F: 85 8B           STA     $8B                 
B1A1: A9 01           LDA     #$01                
B1A3: 85 8F           STA     $8F                 
B1A5: A5 14           LDA     $14                 
B1A7: 29 01           AND     #$01                
B1A9: D0 03           BNE     $B1AE               ; {}
B1AB: 20 BE B1        JSR     $B1BE               ; {}
B1AE: 60              RTS                         
B1AF: A9 00           LDA     #$00                
B1B1: 9D 01 07        STA     $0701,X             
B1B4: 60              RTS                         
B1B5: A9 60           LDA     #$60                
B1B7: 85 87           STA     $87                 
B1B9: A9 02           LDA     #$02                
B1BB: 85 88           STA     $88                 
B1BD: 60              RTS                         
B1BE: A0 00           LDY     #$00                
B1C0: B1 89           LDA     ($89),Y             
B1C2: 18              CLC                         
B1C3: 65 8D           ADC     $8D                 
B1C5: 91 87           STA     ($87),Y             
B1C7: C8              INY                         
B1C8: B1 89           LDA     ($89),Y             
B1CA: 91 87           STA     ($87),Y             
B1CC: C8              INY                         
B1CD: B1 89           LDA     ($89),Y             
B1CF: 05 8F           ORA     $8F                 
B1D1: 91 87           STA     ($87),Y             
B1D3: C8              INY                         
B1D4: B1 89           LDA     ($89),Y             
B1D6: 30 0B           BMI     $B1E3               ; {}
B1D8: 18              CLC                         
B1D9: 65 8E           ADC     $8E                 
B1DB: AA              TAX                         
B1DC: A5 8B           LDA     $8B                 
B1DE: 69 00           ADC     #$00                
B1E0: 4C EB B1        JMP     $B1EB               ; {}
B1E3: 18              CLC                         
B1E4: 65 8E           ADC     $8E                 
B1E6: AA              TAX                         
B1E7: A5 8B           LDA     $8B                 
B1E9: 69 FF           ADC     #$FF                
B1EB: D0 0F           BNE     $B1FC               ; {}
B1ED: 8A              TXA                         
B1EE: 91 87           STA     ($87),Y             
B1F0: C8              INY                         
B1F1: C6 8C           DEC     $8C                 
B1F3: D0 CB           BNE     $B1C0               ; {}
B1F5: 98              TYA                         
B1F6: 18              CLC                         
B1F7: 65 87           ADC     $87                 
B1F9: 85 87           STA     $87                 
B1FB: 60              RTS                         
B1FC: 88              DEY                         
B1FD: 88              DEY                         
B1FE: 88              DEY                         
B1FF: A9 F0           LDA     #$F0                
B201: 91 87           STA     ($87),Y             
B203: C8              INY                         
B204: C8              INY                         
B205: C8              INY                         
B206: 4C F0 B1        JMP     $B1F0               ; {}
B209: 00              BRK                         
B20A: 00              BRK                         
B20B: 00              BRK                         
B20C: FE 80 FF        INC     $FF80,X             
B20F: 20 FE 40        JSR     $40FE               
B212: FF ; ????
B213: 40              RTI                         
B214: FE 00 FF        INC     $FF00,X             
B217: 60              RTS                         
B218: FE 80 FE        INC     $FE80,X             
B21B: 80 ; ????
B21C: FE 60 FE        INC     $FE60,X             
B21F: 00              BRK                         
B220: FF ; ????
B221: 40              RTI                         
B222: FE 40 FF        INC     $FF40,X             
B225: 20 FE 80        JSR     $80FE               ; {}
B228: FF ; ????
B229: 80 ; ????
B22A: 00              BRK                         
B22B: 20 FE C0        JSR     $C0FE               
B22E: 00              BRK                         
B22F: 40              RTI                         
B230: FE 00 01        INC     $0100,X             
B233: 60              RTS                         
B234: FE 80 01        INC     $0180,X             
B237: 80 ; ????
B238: FE A0 01        INC     $01A0,X             
B23B: 00              BRK                         
B23C: FF ; ????
B23D: C0 01           CPY     #$01                
B23F: 40              RTI                         
B240: FF ; ????
B241: E0 01           CPX     #$01                
B243: 80 ; ????
B244: FF ; ????
B245: 20 22 24        JSR     $2422               
B248: 26 28           ROL     $28                 
B24A: 2A              ROL     A                   
B24B: 2C 2E 30        BIT     $302E               
B24E: 32 ; ????
B24F: 34 ; ????
B250: 36 38           ROL     $38,X               
B252: 3A ; ????
B253: 3C ; ????
B254: 3E 40 42        ROL     $4240,X             
B257: 44 ; ????
B258: 46 48           LSR     $48                 
B25A: 4A              LSR     A                   
B25B: 4C 4E 50        JMP     $504E               
B25E: 52 ; ????
B25F: 54 ; ????
B260: 56 58           LSR     $58,X               
B262: 5A ; ????
B263: 5C ; ????
B264: 5E 60 62        LSR     $6260,X             
B267: 64 ; ????
B268: 66 68           ROR     $68                 
B26A: 6A              ROR     A                   
B26B: 6C 6E 70        JMP     ($706E)             
B26E: 72 ; ????
B26F: 74 ; ????
B270: 76 78           ROR     $78,X               
B272: 7A ; ????
B273: 7C ; ????
B274: 7E 80 82        ROR     $8280,X             ; {}
B277: 84 86           STY     $86                 
B279: 88              DEY                         
B27A: 8A              TXA                         
B27B: 8C 8E 90        STY     $908E               ; {}
B27E: 94 98           STY     $98,X               
B280: 9C ; ????
B281: A0 A4           LDY     #$A4                
B283: A8              TAY                         
B284: AC B0 B4        LDY     $B4B0               ; {}
B287: B8              CLV                         
B288: BC C0 C4        LDY     $C4C0,X             
B28B: C8              INY                         
B28C: CC D0 CC        CPY     $CCD0               
B28F: C8              INY                         
B290: C4 C0           CPY     $C0                 
B292: BC B8 B4        LDY     $B4B8,X             ; {}
B295: B0 AC           BCS     $B243               ; {}
B297: A8              TAY                         
B298: A4 A0           LDY     $A0                 
B29A: 9C ; ????
B29B: 98              TYA                         
B29C: 94 90           STY     $90,X               
B29E: 8E 8C 8A        STX     $8A8C               ; {}
B2A1: 88              DEY                         
B2A2: 86 84           STX     $84                 
B2A4: 82 ; ????
B2A5: 80 ; ????
B2A6: 7E 7C 7A        ROR     $7A7C,X             
B2A9: 78              SEI                         
B2AA: 76 74           ROR     $74,X               
B2AC: 72 ; ????
B2AD: 70 6E           BVS     $B31D               ; {}
B2AF: 6C 6A 68        JMP     ($686A)             
B2B2: 66 64           ROR     $64                 
B2B4: 62 ; ????
B2B5: 60              RTS                         
B2B6: 5E 5C 5A        LSR     $5A5C,X             
B2B9: 58              CLI                         
B2BA: 56 55           LSR     $55,X               
B2BC: 54 ; ????
B2BD: 53 ; ????
B2BE: 54 ; ????
B2BF: 55 56           EOR     $56,X               
B2C1: 58              CLI                         
B2C2: 5A ; ????
B2C3: 5C ; ????
B2C4: 5E 60 62        LSR     $6260,X             
B2C7: 64 ; ????
B2C8: 66 68           ROR     $68                 
B2CA: 6A              ROR     A                   
B2CB: 6C 6E 70        JMP     ($706E)             
B2CE: 72 ; ????
B2CF: 74 ; ????
B2D0: 76 78           ROR     $78,X               
B2D2: 7A ; ????
B2D3: 7C ; ????
B2D4: 7E 80 82        ROR     $8280,X             ; {}
B2D7: 84 86           STY     $86                 
B2D9: 88              DEY                         
B2DA: 8A              TXA                         
B2DB: 8C 8E 90        STY     $908E               ; {}
B2DE: 94 98           STY     $98,X               
B2E0: 9C ; ????
B2E1: A0 A4           LDY     #$A4                
B2E3: A8              TAY                         
B2E4: AC B0 B4        LDY     $B4B0               ; {}
B2E7: B8              CLV                         
B2E8: BC C0 C4        LDY     $C4C0,X             
B2EB: C8              INY                         
B2EC: CC D0 CC        CPY     $CCD0               
B2EF: C8              INY                         
B2F0: C4 C0           CPY     $C0                 
B2F2: BC B8 B4        LDY     $B4B8,X             ; {}
B2F5: B0 AC           BCS     $B2A3               ; {}
B2F7: A8              TAY                         
B2F8: A4 A0           LDY     $A0                 
B2FA: 9C ; ????
B2FB: 98              TYA                         
B2FC: 94 90           STY     $90,X               
B2FE: 8E 8C 8A        STX     $8A8C               ; {}
B301: 88              DEY                         
B302: 86 84           STX     $84                 
B304: 82 ; ????
B305: 80 ; ????
B306: 7E 7C 7A        ROR     $7A7C,X             
B309: 78              SEI                         
B30A: 76 75           ROR     $75,X               
B30C: 74 ; ????
B30D: 73 ; ????
B30E: 74 ; ????
B30F: 75 76           ADC     $76,X               
B311: 78              SEI                         
B312: 7A ; ????
B313: 7C ; ????
B314: 7E 80 82        ROR     $8280,X             ; {}
B317: 84 86           STY     $86                 
B319: 88              DEY                         
B31A: 8A              TXA                         
B31B: 8C 8E 90        STY     $908E               ; {}
B31E: 94 98           STY     $98,X               
B320: 9C ; ????
B321: A0 A4           LDY     #$A4                
B323: A8              TAY                         
B324: AC B0 B4        LDY     $B4B0               ; {}
B327: B8              CLV                         
B328: BC C0 C4        LDY     $C4C0,X             
B32B: C8              INY                         
B32C: CC D0 CC        CPY     $CCD0               
B32F: C8              INY                         
B330: C4 C0           CPY     $C0                 
B332: BC B8 B4        LDY     $B4B8,X             ; {}
B335: B0 AC           BCS     $B2E3               ; {}
B337: A8              TAY                         
B338: A4 A0           LDY     $A0                 
B33A: 9C ; ????
B33B: 98              TYA                         
B33C: 94 90           STY     $90,X               
B33E: 8E 8C 8A        STX     $8A8C               ; {}
B341: 88              DEY                         
B342: 86 84           STX     $84                 
B344: 82 ; ????
B345: 0F ; ????
B346: 30 15           BMI     $B35D               ; {}
B348: 0C ; ????
B349: 0F ; ????
B34A: 0F ; ????
B34B: 0F ; ????
B34C: 0F ; ????
B34D: 0F ; ????
B34E: 27 ; ????
B34F: 18              CLC                         
B350: 09 0F           ORA     #$0F                
B352: 0F ; ????
B353: 0F ; ????
B354: 0F ; ????
B355: 88              DEY                         
B356: 9D 41 80        STA     $8041,X             ; {}
B359: 90 9E           BCC     $B2F9               ; {}
B35B: 41 80           EOR     ($80,X)             
B35D: 80 ; ????
B35E: 2E 40 80        ROL     $8040               ; {}
B361: 80 ; ????
B362: 2F ; ????
B363: 40              RTI                         
B364: 78              SEI                         
B365: 80 ; ????
B366: 7D 40 70        ADC     $7040,X             
B369: 88              DEY                         
B36A: 7B ; ????
B36B: 40              RTI                         
B36C: 78              SEI                         
B36D: 90 7C           BCC     $B3EB               ; {}
B36F: 40              RTI                         
B370: 78              SEI                         
B371: 75 B3           ADC     $B3,X               
B373: 85 B3           STA     $B3                 
B375: FC ; ????
B376: C1 00           CMP     ($00,X)             ; {ram.GP_00}
B378: F8              SED                         
B379: FC ; ????
B37A: C4 00           CPY     $00                 ; {ram.GP_00}
B37C: 00              BRK                         
B37D: 04 ; ????
B37E: C5 00           CMP     $00                 ; {ram.GP_00}
B380: F8              SED                         
B381: 04 ; ????
B382: CE 00 00        DEC     $0000               ; {ram.GP_00}
B385: FC ; ????
B386: C1 00           CMP     ($00,X)             ; {ram.GP_00}
B388: F8              SED                         
B389: FC ; ????
B38A: C4 00           CPY     $00                 ; {ram.GP_00}
B38C: 00              BRK                         
B38D: 04 ; ????
B38E: CF ; ????
B38F: 00              BRK                         
B390: F8              SED                         
B391: 04 ; ????
B392: E6 00           INC     $00                 ; {ram.GP_00}
B394: 00              BRK                         
B395: 00              BRK                         
B396: C0 00           CPY     #$00                
B398: 00              BRK                         
B399: F8              SED                         
B39A: E7 ; ????
B39B: 00              BRK                         
B39C: 00              BRK                         
B39D: 00              BRK                         
B39E: E7 ; ????
B39F: 80 ; ????
B3A0: 00              BRK                         
B3A1: A5 B3           LDA     $B3                 
B3A3: C5 B3           CMP     $B3                 
B3A5: F0 E8           BEQ     $B38F               ; {}
B3A7: 00              BRK                         
B3A8: F8              SED                         
B3A9: F0 E9           BEQ     $B394               ; {}
B3AB: 00              BRK                         
B3AC: 00              BRK                         
B3AD: F8              SED                         
B3AE: EA              NOP                         
B3AF: 00              BRK                         
B3B0: F8              SED                         
B3B1: F8              SED                         
B3B2: EB ; ????
B3B3: 00              BRK                         
B3B4: 00              BRK                         
B3B5: 00              BRK                         
B3B6: EC 00 F8        CPX     $F800               
B3B9: 00              BRK                         
B3BA: ED 00 00        SBC     $0000               ; {ram.GP_00}
B3BD: 08              PHP                         
B3BE: EE 00 F8        INC     $F800               
B3C1: 08              PHP                         
B3C2: EF ; ????
B3C3: 00              BRK                         
B3C4: 00              BRK                         
B3C5: 00              BRK                         
B3C6: F0 00           BEQ     $B3C8               ; {}
B3C8: F0 00           BEQ     $B3CA               ; {}
B3CA: F1 00           SBC     ($00),Y             ; {ram.GP_00}
B3CC: F8              SED                         
B3CD: 08              PHP                         
B3CE: F2 ; ????
B3CF: 00              BRK                         
B3D0: F0 08           BEQ     $B3DA               ; {}
B3D2: F3 ; ????
B3D3: 00              BRK                         
B3D4: F8              SED                         
B3D5: 08              PHP                         
B3D6: F4 ; ????
B3D7: 00              BRK                         
B3D8: 00              BRK                         
B3D9: 20 A0 B4        JSR     $B4A0               ; {}
B3DC: 20 00 B4        JSR     $B400               ; {}
B3DF: 20 22 B4        JSR     $B422               ; {}
B3E2: A5 B3           LDA     $B3                 
B3E4: 38              SEC                         
B3E5: E5 05           SBC     $05                 
B3E7: 85 B3           STA     $B3                 
B3E9: A5 B4           LDA     $B4                 
B3EB: E5 06           SBC     $06                 
B3ED: 85 B4           STA     $B4                 
B3EF: A5 B5           LDA     $B5                 
B3F1: E5 07           SBC     $07                 
B3F3: 85 B5           STA     $B5                 
B3F5: B0 08           BCS     $B3FF               ; {}
B3F7: A9 00           LDA     #$00                
B3F9: 85 B3           STA     $B3                 
B3FB: 85 B4           STA     $B4                 
B3FD: 85 B5           STA     $B5                 
B3FF: 60              RTS                         
B400: 20 43 B4        JSR     $B443               ; {}
B403: A5 AA           LDA     $AA                 
B405: 18              CLC                         
B406: 6D 52 01        ADC     $0152               
B409: 18              CLC                         
B40A: 69 02           ADC     #$02                
B40C: 85 03           STA     $03                 
B40E: A9 00           LDA     #$00                
B410: 85 04           STA     $04                 
B412: 20 38 B4        JSR     $B438               ; {}
B415: A5 05           LDA     $05                 
B417: 85 B3           STA     $B3                 
B419: A5 06           LDA     $06                 
B41B: 85 B4           STA     $B4                 
B41D: A5 07           LDA     $07                 
B41F: 85 B5           STA     $B5                 
B421: 60              RTS                         
B422: 20 43 B4        JSR     $B443               ; {}
B425: A5 AD           LDA     $AD                 
B427: 85 03           STA     $03                 
B429: A5 AE           LDA     $AE                 
B42B: 85 04           STA     $04                 
B42D: 4C 30 B4        JMP     $B430               ; {}
B430: A9 E8           LDA     #$E8                
B432: 85 01           STA     $01                 
B434: A9 03           LDA     #$03                
B436: D0 06           BNE     $B43E               ; {}
B438: A9 10           LDA     #$10                
B43A: 85 01           STA     $01                 
B43C: A9 27           LDA     #$27                
B43E: 85 02           STA     $02                 
B440: 4C 4E B4        JMP     $B44E               ; {}
B443: A9 00           LDA     #$00                
B445: 85 05           STA     $05                 
B447: 85 06           STA     $06                 
B449: 85 07           STA     $07                 
B44B: 85 08           STA     $08                 
B44D: 60              RTS                         
B44E: A0 0F           LDY     #$0F                
B450: A9 00           LDA     #$00                
B452: 85 09           STA     $09                 
B454: 85 0A           STA     $0A                 
B456: 46 04           LSR     $04                 
B458: 66 03           ROR     $03                 
B45A: 90 19           BCC     $B475               ; {}
B45C: A5 05           LDA     $05                 
B45E: 18              CLC                         
B45F: 65 01           ADC     $01                 
B461: 85 05           STA     $05                 
B463: A5 06           LDA     $06                 
B465: 65 02           ADC     $02                 
B467: 85 06           STA     $06                 
B469: A5 07           LDA     $07                 
B46B: 65 09           ADC     $09                 
B46D: 85 07           STA     $07                 
B46F: A5 08           LDA     $08                 
B471: 65 0A           ADC     $0A                 
B473: 85 08           STA     $08                 
B475: 06 01           ASL     $01                 
B477: 26 02           ROL     $02                 
B479: 26 09           ROL     $09                 
B47B: 26 0A           ROL     $0A                 
B47D: 88              DEY                         
B47E: 10 D6           BPL     $B456               ; {}
B480: 60              RTS                         
B481: A0 00           LDY     #$00                
B483: AD 31 01        LDA     $0131               
B486: 18              CLC                         
B487: 79 BD B4        ADC     $B4BD,Y             ; {}
B48A: 8D 31 01        STA     $0131               
B48D: AD 32 01        LDA     $0132               
B490: 79 BE B4        ADC     $B4BE,Y             ; {}
B493: 8D 32 01        STA     $0132               
B496: AD 33 01        LDA     $0133               
B499: 79 BF B4        ADC     $B4BF,Y             ; {}
B49C: 8D 33 01        STA     $0133               
B49F: 60              RTS                         
B4A0: AD 44 01        LDA     $0144               
B4A3: 18              CLC                         
B4A4: 6D 31 01        ADC     $0131               
B4A7: 8D 44 01        STA     $0144               
B4AA: AD 45 01        LDA     $0145               
B4AD: 6D 32 01        ADC     $0132               
B4B0: 8D 45 01        STA     $0145               
B4B3: AD 46 01        LDA     $0146               
B4B6: 6D 33 01        ADC     $0133               
B4B9: 8D 46 01        STA     $0146               
B4BC: 60              RTS                         
B4BD: 64 ; ????
B4BE: 00              BRK                         
B4BF: 00              BRK                         
B4C0: 40              RTI                         
B4C1: 1F ; ????
B4C2: 00              BRK                         
B4C3: AC 30 01        LDY     $0130               
B4C6: B9 21 BF        LDA     $BF21,Y             ; {}
B4C9: A8              TAY                         
B4CA: 20 D0 B4        JSR     $B4D0               ; {}
B4CD: 60              RTS                         
B4CE: A0 1F           LDY     #$1F                
B4D0: A2 1F           LDX     #$1F                
B4D2: B9 24 BF        LDA     $BF24,Y             ; {}
B4D5: 9D 90 03        STA     $0390,X             
B4D8: 88              DEY                         
B4D9: CA              DEX                         
B4DA: 10 F6           BPL     $B4D2               ; {}
B4DC: 60              RTS                         
B4DD: 85 02           STA     $02                 
B4DF: 84 03           STY     $03                 
B4E1: A5 1B           LDA     $1B                 
B4E3: 49 FF           EOR     #$FF                
B4E5: 29 01           AND     #$01                
B4E7: 0A              ASL     A                   
B4E8: A8              TAY                         
B4E9: A5 FE           LDA     $FE                 
B4EB: 18              CLC                         
B4EC: 65 03           ADC     $03                 
B4EE: 4A              LSR     A                   
B4EF: 4A              LSR     A                   
B4F0: 4A              LSR     A                   
B4F1: 4A              LSR     A                   
B4F2: 18              CLC                         
B4F3: 79 6C BE        ADC     $BE6C,Y             ; {}
B4F6: 85 00           STA     $00                 ; {ram.GP_00}
B4F8: A9 00           LDA     #$00                
B4FA: 79 6D BE        ADC     $BE6D,Y             ; {}
B4FD: 85 01           STA     $01                 
B4FF: A5 02           LDA     $02                 
B501: 29 F0           AND     #$F0                
B503: 18              CLC                         
B504: 65 00           ADC     $00                 ; {ram.GP_00}
B506: 85 00           STA     $00                 ; {ram.GP_00}
B508: A9 00           LDA     #$00                
B50A: 65 01           ADC     $01                 
B50C: 85 01           STA     $01                 
B50E: 18              CLC                         
B50F: A5 FE           LDA     $FE                 
B511: 65 03           ADC     $03                 
B513: 90 20           BCC     $B535               ; {}
B515: 98              TYA                         
B516: D0 10           BNE     $B528               ; {}
B518: A9 F0           LDA     #$F0                
B51A: 18              CLC                         
B51B: 65 00           ADC     $00                 ; {ram.GP_00}
B51D: 85 00           STA     $00                 ; {ram.GP_00}
B51F: A9 00           LDA     #$00                
B521: 65 01           ADC     $01                 
B523: 85 01           STA     $01                 
B525: 4C 35 B5        JMP     $B535               ; {}
B528: A5 00           LDA     $00                 ; {ram.GP_00}
B52A: 38              SEC                         
B52B: E9 F0           SBC     #$F0                
B52D: 85 00           STA     $00                 ; {ram.GP_00}
B52F: A5 01           LDA     $01                 
B531: E9 00           SBC     #$00                
B533: 85 01           STA     $01                 
B535: A0 00           LDY     #$00                
B537: B1 00           LDA     ($00),Y             ; {ram.GP_00}
B539: 60              RTS                         
B53A: AD D1 04        LDA     $04D1               
B53D: C9 0E           CMP     #$0E                
B53F: 90 06           BCC     $B547               ; {}
B541: A5 FE           LDA     $FE                 
B543: C9 FC           CMP     #$FC                
B545: B0 12           BCS     $B559               ; {}
B547: A5 14           LDA     $14                 
B549: 29 01           AND     #$01                
B54B: D0 0D           BNE     $B55A               ; {}
B54D: F0 03           BEQ     $B552               ; {}
B54F: DE 03 07        DEC     $0703,X             
B552: 20 18 B6        JSR     $B618               ; {}
B555: A9 01           LDA     #$01                
B557: 85 27           STA     $27                 
B559: 60              RTS                         
B55A: A9 00           LDA     #$00                
B55C: F0 F9           BEQ     $B557               ; {}
B55E: 20 3A B5        JSR     $B53A               ; {}
B561: 20 8D B5        JSR     $B58D               ; {}
B564: 24 5C           BIT     $5C                 
B566: 70 F2           BVS     $B55A               ; {}
B568: BD 03 07        LDA     $0703,X             
B56B: C9 F5           CMP     #$F5                
B56D: B0 0C           BCS     $B57B               ; {}
B56F: C9 10           CMP     #$10                
B571: 90 0E           BCC     $B581               ; {}
B573: BD 00 07        LDA     $0700,X             
B576: C9 30           CMP     #$30                
B578: 90 0D           BCC     $B587               ; {}
B57A: 60              RTS                         
B57B: A9 F5           LDA     #$F5                
B57D: 9D 03 07        STA     $0703,X             
B580: 60              RTS                         
B581: A9 10           LDA     #$10                
B583: 9D 03 07        STA     $0703,X             
B586: 60              RTS                         
B587: A9 30           LDA     #$30                
B589: 9D 00 07        STA     $0700,X             
B58C: 60              RTS                         
B58D: AD D5 04        LDA     $04D5               
B590: C9 29           CMP     #$29                
B592: F0 07           BEQ     $B59B               ; {}
B594: AD D6 04        LDA     $04D6               
B597: C9 29           CMP     #$29                
B599: D0 BE           BNE     $B559               ; {}
B59B: A0 58           LDY     #$58                
B59D: A9 04           LDA     #$04                
B59F: 4C 90 CA        JMP     $CA90               
B5A2: 60              RTS                         
B5A3: A5 FE           LDA     $FE                 
B5A5: 29 0F           AND     #$0F                
B5A7: C9 02           CMP     #$02                
B5A9: F0 19           BEQ     $B5C4               ; {}
B5AB: C9 03           CMP     #$03                
B5AD: F0 18           BEQ     $B5C7               ; {}
B5AF: A5 68           LDA     $68                 
B5B1: 0A              ASL     A                   
B5B2: A8              TAY                         
B5B3: B9 C0 B5        LDA     $B5C0,Y             ; {}
B5B6: 85 00           STA     $00                 ; {ram.GP_00}
B5B8: B9 C1 B5        LDA     $B5C1,Y             ; {}
B5BB: 85 01           STA     $01                 
B5BD: 6C 00 00        JMP     ($0000)             ; {ram.GP_00}
B5C0: 42 ; ????
B5C1: EE CA B5        INC     $B5CA               ; {}
B5C4: 4C 35 B6        JMP     $B635               ; {}
B5C7: 4C 89 B6        JMP     $B689               ; {}
B5CA: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
B5CD: A5 6A           LDA     $6A                 
B5CF: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
B5D2: A5 69           LDA     $69                 
B5D4: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
B5D7: A2 05           LDX     #$05                
B5D9: A9 12           LDA     #$12                
B5DB: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
B5DE: CA              DEX                         
B5DF: 10 FA           BPL     $B5DB               ; {}
B5E1: A9 00           LDA     #$00                
B5E3: 85 68           STA     $68                 
B5E5: 60              RTS                         
B5E6: A5 5C           LDA     $5C                 
B5E8: 10 2D           BPL     $B617               ; {}
B5EA: AD 00 01        LDA     $0100               
B5ED: 29 7F           AND     #$7F                
B5EF: 8D 00 01        STA     $0100               
B5F2: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
B5F5: 20 49 B8        JSR     $B849               ; {}
B5F8: 20 11 B6        JSR     $B611               ; {}
B5FB: A9 00           LDA     #$00                
B5FD: 85 40           STA     $40                 
B5FF: 85 41           STA     $41                 
B601: 68              PLA                         
B602: 68              PLA                         
B603: AD 00 01        LDA     $0100               
B606: 09 80           ORA     #$80                
B608: 8D 00 01        STA     $0100               
B60B: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
B60E: 4C D5 9C        JMP     $9CD5               ; {}
B611: A5 5C           LDA     $5C                 
B613: 29 7F           AND     #$7F                
B615: 85 5C           STA     $5C                 
B617: 60              RTS                         
B618: E6 FE           INC     $FE                 
B61A: D0 18           BNE     $B634               ; {}
B61C: E6 1B           INC     $1B                 
B61E: A5 C9           LDA     $C9                 
B620: C9 32           CMP     #$32                
B622: B0 0A           BCS     $B62E               ; {}
B624: A5 1B           LDA     $1B                 
B626: C9 0D           CMP     #$0D                
B628: 90 04           BCC     $B62E               ; {}
B62A: A9 01           LDA     #$01                
B62C: 85 1B           STA     $1B                 
B62E: A5 5C           LDA     $5C                 
B630: 09 80           ORA     #$80                
B632: 85 5C           STA     $5C                 
B634: 60              RTS                         
B635: AD 00 01        LDA     $0100               
B638: 09 04           ORA     #$04                
B63A: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
B63D: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
B640: AD 82 04        LDA     $0482               
B643: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
B646: AD 81 04        LDA     $0481               
B649: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
B64C: A0 00           LDY     #$00                
B64E: 98              TYA                         
B64F: 0A              ASL     A                   
B650: AA              TAX                         
B651: BD 83 04        LDA     $0483,X             
B654: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
B657: C8              INY                         
B658: C0 1E           CPY     #$1E                
B65A: 90 F2           BCC     $B64E               ; {}
B65C: AD 81 04        LDA     $0481               
B65F: 18              CLC                         
B660: 69 01           ADC     #$01                
B662: 48              PHA                         
B663: AD 82 04        LDA     $0482               
B666: 69 00           ADC     #$00                
B668: AC 02 20        LDY     $2002               ; {hard.P_STATUS}
B66B: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
B66E: 68              PLA                         
B66F: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
B672: A0 00           LDY     #$00                
B674: 98              TYA                         
B675: 0A              ASL     A                   
B676: AA              TAX                         
B677: BD 84 04        LDA     $0484,X             
B67A: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
B67D: C8              INY                         
B67E: C0 1E           CPY     #$1E                
B680: 90 F2           BCC     $B674               ; {}
B682: AD 00 01        LDA     $0100               
B685: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
B688: 60              RTS                         
B689: 20 EB B7        JSR     $B7EB               ; {}
B68C: A0 00           LDY     #$00                
B68E: 98              TYA                         
B68F: 0A              ASL     A                   
B690: 0A              ASL     A                   
B691: 0A              ASL     A                   
B692: 18              CLC                         
B693: 65 00           ADC     $00                 ; {ram.GP_00}
B695: 85 03           STA     $03                 
B697: 18              CLC                         
B698: 69 C0           ADC     #$C0                
B69A: 48              PHA                         
B69B: A5 1B           LDA     $1B                 
B69D: 49 01           EOR     #$01                
B69F: 29 01           AND     #$01                
B6A1: 0A              ASL     A                   
B6A2: 0A              ASL     A                   
B6A3: 09 23           ORA     #$23                
B6A5: AE 02 20        LDX     $2002               ; {hard.P_STATUS}
B6A8: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
B6AB: 68              PLA                         
B6AC: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
B6AF: A6 03           LDX     $03                 
B6B1: BD B0 03        LDA     $03B0,X             
B6B4: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
B6B7: C8              INY                         
B6B8: C0 08           CPY     #$08                
B6BA: 90 D2           BCC     $B68E               ; {}
B6BC: 60              RTS                         
B6BD: A5 FE           LDA     $FE                 
B6BF: 29 F0           AND     #$F0                
B6C1: 4A              LSR     A                   
B6C2: 4A              LSR     A                   
B6C3: 4A              LSR     A                   
B6C4: 85 00           STA     $00                 ; {ram.GP_00}
B6C6: 8D 81 04        STA     $0481               
B6C9: A5 1B           LDA     $1B                 
B6CB: 49 01           EOR     #$01                
B6CD: 29 01           AND     #$01                
B6CF: 0A              ASL     A                   
B6D0: 0A              ASL     A                   
B6D1: 09 20           ORA     #$20                
B6D3: 8D 82 04        STA     $0482               
B6D6: 20 F1 B6        JSR     $B6F1               ; {}
B6D9: 20 F7 B6        JSR     $B6F7               ; {}
B6DC: A5 FE           LDA     $FE                 
B6DE: 29 F0           AND     #$F0                
B6E0: 4A              LSR     A                   
B6E1: 4A              LSR     A                   
B6E2: 4A              LSR     A                   
B6E3: 4A              LSR     A                   
B6E4: 65 62           ADC     $62                 
B6E6: 85 06           STA     $06                 
B6E8: A9 00           LDA     #$00                
B6EA: 65 63           ADC     $63                 
B6EC: 85 07           STA     $07                 
B6EE: 4C 09 B7        JMP     $B709               ; {}
B6F1: A5 1B           LDA     $1B                 
B6F3: 8D D1 04        STA     $04D1               
B6F6: 60              RTS                         
B6F7: AD D1 04        LDA     $04D1               
B6FA: 29 01           AND     #$01                
B6FC: 0A              ASL     A                   
B6FD: A8              TAY                         
B6FE: B9 6C BE        LDA     $BE6C,Y             ; {}
B701: 85 62           STA     $62                 
B703: B9 6D BE        LDA     $BE6D,Y             ; {}
B706: 85 63           STA     $63                 
B708: 60              RTS                         
B709: A0 0E           LDY     #$0E                
B70B: 98              TYA                         
B70C: 48              PHA                         
B70D: 0A              ASL     A                   
B70E: 0A              ASL     A                   
B70F: 0A              ASL     A                   
B710: 0A              ASL     A                   
B711: A8              TAY                         
B712: B1 06           LDA     ($06),Y             
B714: 20 36 B7        JSR     $B736               ; {}
B717: 68              PLA                         
B718: 48              PHA                         
B719: 0A              ASL     A                   
B71A: 0A              ASL     A                   
B71B: A8              TAY                         
B71C: A5 02           LDA     $02                 
B71E: 99 83 04        STA     $0483,Y             
B721: A5 03           LDA     $03                 
B723: 99 84 04        STA     $0484,Y             
B726: A5 04           LDA     $04                 
B728: 99 85 04        STA     $0485,Y             
B72B: A5 05           LDA     $05                 
B72D: 99 86 04        STA     $0486,Y             
B730: 68              PLA                         
B731: A8              TAY                         
B732: 88              DEY                         
B733: 10 D6           BPL     $B70B               ; {}
B735: 60              RTS                         
B736: A0 00           LDY     #$00                
B738: 84 01           STY     $01                 
B73A: A0 03           LDY     #$03                
B73C: 0A              ASL     A                   
B73D: 26 01           ROL     $01                 
B73F: 0A              ASL     A                   
B740: 26 01           ROL     $01                 
B742: 85 00           STA     $00                 ; {ram.GP_00}
B744: A5 3A           LDA     $3A                 
B746: C9 10           CMP     #$10                
B748: B0 15           BCS     $B75F               ; {}
B74A: A5 00           LDA     $00                 ; {ram.GP_00}
B74C: 69 A8           ADC     #$A8                
B74E: 85 00           STA     $00                 ; {ram.GP_00}
B750: A5 01           LDA     $01                 
B752: 69 BC           ADC     #$BC                
B754: 85 01           STA     $01                 
B756: B1 00           LDA     ($00),Y             ; {ram.GP_00}
B758: 99 02 00        STA     $0002,Y             
B75B: 88              DEY                         
B75C: 10 F8           BPL     $B756               ; {}
B75E: 60              RTS                         
B75F: A5 00           LDA     $00                 ; {ram.GP_00}
B761: 18              CLC                         
B762: 69 A8           ADC     #$A8                
B764: 85 00           STA     $00                 ; {ram.GP_00}
B766: A5 01           LDA     $01                 
B768: 69 BC           ADC     #$BC                
B76A: D0 E8           BNE     $B754               ; {}
B76C: 20 F1 B6        JSR     $B6F1               ; {}
B76F: 20 D9 B7        JSR     $B7D9               ; {}
B772: 20 EB B7        JSR     $B7EB               ; {}
B775: A2 00           LDX     #$00                
B777: 8A              TXA                         
B778: 0A              ASL     A                   
B779: 0A              ASL     A                   
B77A: 0A              ASL     A                   
B77B: 18              CLC                         
B77C: 65 00           ADC     $00                 ; {ram.GP_00}
B77E: A8              TAY                         
B77F: B1 64           LDA     ($64),Y             
B781: 9D F0 03        STA     $03F0,X             
B784: E8              INX                         
B785: E0 08           CPX     #$08                
B787: 90 EE           BCC     $B777               ; {}
B789: A5 FE           LDA     $FE                 
B78B: 29 10           AND     #$10                
B78D: D0 1B           BNE     $B7AA               ; {}
B78F: A0 00           LDY     #$00                
B791: A9 33           LDA     #$33                
B793: 20 C8 B7        JSR     $B7C8               ; {}
B796: 29 CC           AND     #$CC                
B798: 20 C2 B7        JSR     $B7C2               ; {}
B79B: C8              INY                         
B79C: C0 07           CPY     #$07                
B79E: 90 F1           BCC     $B791               ; {}
B7A0: A9 03           LDA     #$03                
B7A2: 20 C8 B7        JSR     $B7C8               ; {}
B7A5: 29 FC           AND     #$FC                
B7A7: 4C C2 B7        JMP     $B7C2               ; {}
B7AA: A0 00           LDY     #$00                
B7AC: A9 CC           LDA     #$CC                
B7AE: 20 C8 B7        JSR     $B7C8               ; {}
B7B1: 29 33           AND     #$33                
B7B3: 20 C2 B7        JSR     $B7C2               ; {}
B7B6: C8              INY                         
B7B7: C0 07           CPY     #$07                
B7B9: 90 F1           BCC     $B7AC               ; {}
B7BB: A9 0C           LDA     #$0C                
B7BD: 20 C8 B7        JSR     $B7C8               ; {}
B7C0: 29 F3           AND     #$F3                
B7C2: 05 02           ORA     $02                 
B7C4: 9D B0 03        STA     $03B0,X             
B7C7: 60              RTS                         
B7C8: 39 F0 03        AND     $03F0,Y             
B7CB: 85 02           STA     $02                 
B7CD: 98              TYA                         
B7CE: 0A              ASL     A                   
B7CF: 0A              ASL     A                   
B7D0: 0A              ASL     A                   
B7D1: 18              CLC                         
B7D2: 65 00           ADC     $00                 ; {ram.GP_00}
B7D4: AA              TAX                         
B7D5: BD B0 03        LDA     $03B0,X             
B7D8: 60              RTS                         
B7D9: AD D1 04        LDA     $04D1               
B7DC: 29 01           AND     #$01                
B7DE: 0A              ASL     A                   
B7DF: A8              TAY                         
B7E0: B9 74 BE        LDA     $BE74,Y             ; {}
B7E3: 85 64           STA     $64                 
B7E5: B9 75 BE        LDA     $BE75,Y             ; {}
B7E8: 85 65           STA     $65                 
B7EA: 60              RTS                         
B7EB: A9 00           LDA     #$00                
B7ED: 85 00           STA     $00                 ; {ram.GP_00}
B7EF: A5 FE           LDA     $FE                 
B7F1: 29 E0           AND     #$E0                
B7F3: 0A              ASL     A                   
B7F4: 26 00           ROL     $00                 ; {ram.GP_00}
B7F6: 0A              ASL     A                   
B7F7: 26 00           ROL     $00                 ; {ram.GP_00}
B7F9: 0A              ASL     A                   
B7FA: 26 00           ROL     $00                 ; {ram.GP_00}
B7FC: 60              RTS                         
B7FD: A9 00           LDA     #$00                
B7FF: 85 5C           STA     $5C                 
B801: 8D D2 04        STA     $04D2               
B804: 20 66 B8        JSR     $B866               ; {}
B807: A9 06           LDA     #$06                
B809: 20 90 CA        JSR     $CA90               
B80C: A9 00           LDA     #$00                
B80E: 8D D2 04        STA     $04D2               
B811: EE D1 04        INC     $04D1               
B814: 20 69 B8        JSR     $B869               ; {}
B817: A9 06           LDA     #$06                
B819: 20 90 CA        JSR     $CA90               
B81C: 20 51 B8        JSR     $B851               ; {}
B81F: A9 00           LDA     #$00                
B821: 85 FE           STA     $FE                 
B823: 85 1B           STA     $1B                 
B825: 20 BD B6        JSR     $B6BD               ; {}
B828: 20 6C B7        JSR     $B76C               ; {}
B82B: 20 35 B6        JSR     $B635               ; {}
B82E: 20 89 B6        JSR     $B689               ; {}
B831: A5 FE           LDA     $FE                 
B833: 18              CLC                         
B834: 69 10           ADC     #$10                
B836: 85 FE           STA     $FE                 
B838: A5 1B           LDA     $1B                 
B83A: 69 00           ADC     #$00                
B83C: 85 1B           STA     $1B                 
B83E: C9 02           CMP     #$02                
B840: 90 E3           BCC     $B825               ; {}
B842: A9 01           LDA     #$01                
B844: 85 1B           STA     $1B                 
B846: 85 FE           STA     $FE                 
B848: 60              RTS                         
B849: 20 66 B8        JSR     $B866               ; {}
B84C: A9 06           LDA     #$06                
B84E: 20 90 CA        JSR     $CA90               
B851: A0 0F           LDY     #$0F                
B853: B9 00 05        LDA     $0500,Y             
B856: 99 E0 06        STA     $06E0,Y             
B859: 88              DEY                         
B85A: 10 F7           BPL     $B853               ; {}
B85C: 60              RTS                         
B85D: A5 5C           LDA     $5C                 
B85F: 09 40           ORA     #$40                
B861: 85 5C           STA     $5C                 
B863: 68              PLA                         
B864: 68              PLA                         
B865: 60              RTS                         
B866: 20 F1 B6        JSR     $B6F1               ; {}
B869: A9 00           LDA     #$00                
B86B: 8D D2 04        STA     $04D2               
B86E: AD 30 01        LDA     $0130               
B871: 0A              ASL     A                   
B872: A8              TAY                         
B873: B9 7C BE        LDA     $BE7C,Y             ; {}
B876: 85 00           STA     $00                 ; {ram.GP_00}
B878: B9 7D BE        LDA     $BE7D,Y             ; {}
B87B: 85 01           STA     $01                 
B87D: AD D1 04        LDA     $04D1               
B880: 0A              ASL     A                   
B881: A8              TAY                         
B882: B1 00           LDA     ($00),Y             ; {ram.GP_00}
B884: 85 49           STA     $49                 
B886: C8              INY                         
B887: B1 00           LDA     ($00),Y             ; {ram.GP_00}
B889: C9 FF           CMP     #$FF                
B88B: F0 D0           BEQ     $B85D               ; {}
B88D: 85 4A           STA     $4A                 
B88F: 20 A2 B8        JSR     $B8A2               ; {}
B892: 60              RTS                         
B893: AD D1 04        LDA     $04D1               
B896: 0A              ASL     A                   
B897: A8              TAY                         
B898: B9 82 BE        LDA     $BE82,Y             ; {}
B89B: 85 49           STA     $49                 
B89D: B9 83 BE        LDA     $BE83,Y             ; {}
B8A0: 85 4A           STA     $4A                 
B8A2: 20 F7 B6        JSR     $B6F7               ; {}
B8A5: 20 D9 B7        JSR     $B7D9               ; {}
B8A8: 20 6B B9        JSR     $B96B               ; {}
B8AB: A0 00           LDY     #$00                
B8AD: B1 49           LDA     ($49),Y             
B8AF: 20 78 B9        JSR     $B978               ; {}
B8B2: A0 01           LDY     #$01                
B8B4: B1 49           LDA     ($49),Y             
B8B6: C9 FD           CMP     #$FD                
B8B8: F0 17           BEQ     $B8D1               ; {}
B8BA: 85 4D           STA     $4D                 
B8BC: C8              INY                         
B8BD: B1 49           LDA     ($49),Y             
B8BF: 85 4E           STA     $4E                 
B8C1: C8              INY                         
B8C2: B1 49           LDA     ($49),Y             
B8C4: 85 4F           STA     $4F                 
B8C6: 98              TYA                         
B8C7: 48              PHA                         
B8C8: 20 D2 B8        JSR     $B8D2               ; {}
B8CB: 68              PLA                         
B8CC: A8              TAY                         
B8CD: C8              INY                         
B8CE: 4C B4 B8        JMP     $B8B4               ; {}
B8D1: 60              RTS                         
B8D2: 20 1D B9        JSR     $B91D               ; {}
B8D5: A9 00           LDA     #$00                
B8D7: 85 5F           STA     $5F                 
B8D9: A5 4D           LDA     $4D                 
B8DB: 29 F0           AND     #$F0                
B8DD: 85 61           STA     $61                 
B8DF: A5 5F           LDA     $5F                 
B8E1: 0A              ASL     A                   
B8E2: 0A              ASL     A                   
B8E3: 0A              ASL     A                   
B8E4: 0A              ASL     A                   
B8E5: 18              CLC                         
B8E6: 65 61           ADC     $61                 
B8E8: C9 F0           CMP     #$F0                
B8EA: B0 3F           BCS     $B92B               ; {}
B8EC: A0 00           LDY     #$00                
B8EE: B1 51           LDA     ($51),Y             
B8F0: C9 FF           CMP     #$FF                
B8F2: F0 37           BEQ     $B92B               ; {}
B8F4: 85 53           STA     $53                 
B8F6: 29 0F           AND     #$0F                
B8F8: AA              TAX                         
B8F9: C8              INY                         
B8FA: B1 51           LDA     ($51),Y             
B8FC: 99 53 00        STA     $0053,Y             
B8FF: C8              INY                         
B900: CA              DEX                         
B901: D0 F7           BNE     $B8FA               ; {}
B903: 20 8C B9        JSR     $B98C               ; {}
B906: A5 53           LDA     $53                 
B908: 29 0F           AND     #$0F                
B90A: 38              SEC                         
B90B: 65 51           ADC     $51                 
B90D: 85 51           STA     $51                 
B90F: A9 00           LDA     #$00                
B911: 65 52           ADC     $52                 
B913: 85 52           STA     $52                 
B915: 20 2C B9        JSR     $B92C               ; {}
B918: E6 5F           INC     $5F                 
B91A: 4C D9 B8        JMP     $B8D9               ; {}
B91D: A5 4E           LDA     $4E                 
B91F: 0A              ASL     A                   
B920: A8              TAY                         
B921: B9 C6 BE        LDA     $BEC6,Y             ; {}
B924: 85 51           STA     $51                 
B926: B9 C7 BE        LDA     $BEC7,Y             ; {}
B929: 85 52           STA     $52                 
B92B: 60              RTS                         
B92C: A5 5F           LDA     $5F                 
B92E: 0A              ASL     A                   
B92F: 0A              ASL     A                   
B930: 0A              ASL     A                   
B931: 0A              ASL     A                   
B932: 85 5D           STA     $5D                 
B934: A5 53           LDA     $53                 
B936: 29 F0           AND     #$F0                
B938: 4A              LSR     A                   
B939: 4A              LSR     A                   
B93A: 4A              LSR     A                   
B93B: 4A              LSR     A                   
B93C: 65 5D           ADC     $5D                 
B93E: 18              CLC                         
B93F: 65 4D           ADC     $4D                 
B941: 85 5D           STA     $5D                 
B943: A5 53           LDA     $53                 
B945: 29 0F           AND     #$0F                
B947: AA              TAX                         
B948: 18              CLC                         
B949: A5 62           LDA     $62                 
B94B: 65 5D           ADC     $5D                 
B94D: 85 5D           STA     $5D                 
B94F: A9 00           LDA     #$00                
B951: 65 63           ADC     $63                 
B953: 85 5E           STA     $5E                 
B955: A0 00           LDY     #$00                
B957: B9 54 00        LDA     $0054,Y             
B95A: 91 5D           STA     ($5D),Y             
B95C: 98              TYA                         
B95D: 18              CLC                         
B95E: 65 5D           ADC     $5D                 
B960: 29 0F           AND     #$0F                
B962: C9 0F           CMP     #$0F                
B964: B0 04           BCS     $B96A               ; {}
B966: C8              INY                         
B967: CA              DEX                         
B968: D0 ED           BNE     $B957               ; {}
B96A: 60              RTS                         
B96B: A0 00           LDY     #$00                
B96D: A9 00           LDA     #$00                
B96F: 91 62           STA     ($62),Y             
B971: C8              INY                         
B972: 98              TYA                         
B973: C9 F0           CMP     #$F0                
B975: 90 F6           BCC     $B96D               ; {}
B977: 60              RTS                         
B978: 29 03           AND     #$03                
B97A: A8              TAY                         
B97B: B9 88 B9        LDA     $B988,Y             ; {}
B97E: A0 00           LDY     #$00                
B980: 91 64           STA     ($64),Y             
B982: C8              INY                         
B983: C0 40           CPY     #$40                
B985: 90 F9           BCC     $B980               ; {}
B987: 60              RTS                         
B988: 00              BRK                         
B989: 55 AA           EOR     $AA,X               
B98B: FF ; ????
B98C: A5 53           LDA     $53                 
B98E: 29 F0           AND     #$F0                
B990: 4A              LSR     A                   
B991: 4A              LSR     A                   
B992: 4A              LSR     A                   
B993: 4A              LSR     A                   
B994: 8D D0 04        STA     $04D0               
B997: A5 53           LDA     $53                 
B999: 29 0F           AND     #$0F                
B99B: 6D D0 04        ADC     $04D0               
B99E: 8D D0 04        STA     $04D0               
B9A1: A5 4D           LDA     $4D                 
B9A3: 29 0F           AND     #$0F                
B9A5: 8D CD 04        STA     $04CD               
B9A8: 18              CLC                         
B9A9: 6D D0 04        ADC     $04D0               
B9AC: C9 10           CMP     #$10                
B9AE: 90 09           BCC     $B9B9               ; {}
B9B0: A9 10           LDA     #$10                
B9B2: 38              SEC                         
B9B3: ED CD 04        SBC     $04CD               
B9B6: 8D D0 04        STA     $04D0               
B9B9: A9 00           LDA     #$00                
B9BB: 8D CD 04        STA     $04CD               
B9BE: A5 5F           LDA     $5F                 
B9C0: 0A              ASL     A                   
B9C1: 0A              ASL     A                   
B9C2: 0A              ASL     A                   
B9C3: 0A              ASL     A                   
B9C4: 18              CLC                         
B9C5: 65 4D           ADC     $4D                 
B9C7: 18              CLC                         
B9C8: 6D CD 04        ADC     $04CD               
B9CB: 85 60           STA     $60                 
B9CD: 29 E0           AND     #$E0                
B9CF: 4A              LSR     A                   
B9D0: 4A              LSR     A                   
B9D1: 85 66           STA     $66                 
B9D3: A5 60           LDA     $60                 
B9D5: 29 0F           AND     #$0F                
B9D7: 4A              LSR     A                   
B9D8: 18              CLC                         
B9D9: 65 66           ADC     $66                 
B9DB: 18              CLC                         
B9DC: 65 64           ADC     $64                 
B9DE: 85 66           STA     $66                 
B9E0: A9 00           LDA     #$00                
B9E2: 65 65           ADC     $65                 
B9E4: 85 67           STA     $67                 
B9E6: A5 60           LDA     $60                 
B9E8: 29 10           AND     #$10                
B9EA: 4A              LSR     A                   
B9EB: 4A              LSR     A                   
B9EC: 4A              LSR     A                   
B9ED: 8D CE 04        STA     $04CE               
B9F0: A5 60           LDA     $60                 
B9F2: 29 01           AND     #$01                
B9F4: 0D CE 04        ORA     $04CE               
B9F7: F0 0E           BEQ     $BA07               ; {}
B9F9: AA              TAX                         
B9FA: A9 03           LDA     #$03                
B9FC: 0A              ASL     A                   
B9FD: 0A              ASL     A                   
B9FE: CA              DEX                         
B9FF: 8D CE 04        STA     $04CE               
BA02: F0 08           BEQ     $BA0C               ; {}
BA04: 4C FC B9        JMP     $B9FC               ; {}
BA07: A9 03           LDA     #$03                
BA09: 8D CE 04        STA     $04CE               
BA0C: AD CE 04        LDA     $04CE               
BA0F: 49 FF           EOR     #$FF                
BA11: A0 00           LDY     #$00                
BA13: 31 66           AND     ($66),Y             
BA15: 8D CF 04        STA     $04CF               
BA18: A5 4F           LDA     $4F                 
BA1A: 29 02           AND     #$02                
BA1C: F0 05           BEQ     $BA23               ; {}
BA1E: A9 AA           LDA     #$AA                
BA20: 20 41 BA        JSR     $BA41               ; {}
BA23: A5 4F           LDA     $4F                 
BA25: 29 01           AND     #$01                
BA27: F0 05           BEQ     $BA2E               ; {}
BA29: A9 55           LDA     #$55                
BA2B: 20 41 BA        JSR     $BA41               ; {}
BA2E: AD CF 04        LDA     $04CF               
BA31: 91 66           STA     ($66),Y             
BA33: EE CD 04        INC     $04CD               
BA36: AD CD 04        LDA     $04CD               
BA39: CD D0 04        CMP     $04D0               
BA3C: B0 0C           BCS     $BA4A               ; {}
BA3E: 4C BE B9        JMP     $B9BE               ; {}
BA41: 2D CE 04        AND     $04CE               
BA44: 0D CF 04        ORA     $04CF               
BA47: 8D CF 04        STA     $04CF               
BA4A: 60              RTS                         
BA4B: A9 10           LDA     #$10                
BA4D: 85 0A           STA     $0A                 
BA4F: C6 1B           DEC     $1B                 
BA51: 20 BD B6        JSR     $B6BD               ; {}
BA54: 20 6C B7        JSR     $B76C               ; {}
BA57: 20 35 B6        JSR     $B635               ; {}
BA5A: 20 89 B6        JSR     $B689               ; {}
BA5D: A5 FE           LDA     $FE                 
BA5F: 18              CLC                         
BA60: 69 10           ADC     #$10                
BA62: 85 FE           STA     $FE                 
BA64: A5 1B           LDA     $1B                 
BA66: 69 00           ADC     #$00                
BA68: 85 1B           STA     $1B                 
BA6A: C6 0A           DEC     $0A                 
BA6C: 10 E3           BPL     $BA51               ; {}
BA6E: A5 FE           LDA     $FE                 
BA70: 38              SEC                         
BA71: E9 10           SBC     #$10                
BA73: 85 FE           STA     $FE                 
BA75: A5 1B           LDA     $1B                 
BA77: E9 00           SBC     #$00                
BA79: 85 1B           STA     $1B                 
BA7B: 60              RTS                         
BA7C: 01 0C           ORA     ($0C,X)             
BA7E: 0E 01 10        ASL     $1001               
BA81: 0D 02 14        ORA     $1402               
BA84: 0D 02 18        ORA     $1802               
BA87: 0D 02 25        ORA     $2502               
BA8A: 09 01           ORA     #$01                
BA8C: 65 0A           ADC     $0A                 
BA8E: 01 6A           ORA     ($6A,X)             
BA90: 09 01           ORA     #$01                
BA92: 80 ; ????
BA93: 11 00           ORA     ($00),Y             ; {ram.GP_00}
BA95: 81 03           STA     ($03,X)             
BA97: 01 85           ORA     ($85,X)             
BA99: 0A              ASL     A                   
BA9A: 01 9C           ORA     ($9C,X)             
BA9C: 0E 01 AA        ASL     $AA01               ; {}
BA9F: 05 01           ORA     $01                 
BAA1: B0 0E           BCS     $BAB1               ; {}
BAA3: 00              BRK                         
BAA4: B5 05           LDA     $05,X               
BAA6: 01 D0           ORA     ($D0,X)             
BAA8: 07 ; ????
BAA9: 01 D8           ORA     ($D8,X)             
BAAB: 07 ; ????
BAAC: 01 FD           ORA     ($FD,X)             
BAAE: FF ; ????
BAAF: 01 00           ORA     ($00,X)             ; {ram.GP_00}
BAB1: 0D 01 04        ORA     $0401               
BAB4: 0D 01 08        ORA     $0801               
BAB7: 0D 01 0C        ORA     $0C01               
BABA: 0E 01 13        ASL     $1301               
BABD: 09 01           ORA     #$01                
BABF: 2C 0B 02        BIT     $020B               
BAC2: 37 ; ????
BAC3: 02 ; ????
BAC4: 02 ; ????
BAC5: 53 ; ????
BAC6: 0A              ASL     A                   
BAC7: 01 6C           ORA     ($6C,X)             
BAC9: 10 00           BPL     $BACB               ; {}
BACB: 6E 0F 02        ROR     $020F               
BACE: 8C 0C 02        STY     $020C               
BAD1: 92 ; ????
BAD2: 11 00           ORA     ($00),Y             ; {ram.GP_00}
BAD4: 93 ; ????
BAD5: 05 01           ORA     $01                 
BAD7: A6 11           LDX     $11                 
BAD9: 00              BRK                         
BADA: BC 0E 01        LDY     $010E,X             
BADD: C0 0D           CPY     #$0D                
BADF: 01 C4           ORA     ($C4,X)             
BAE1: 0D 01 C8        ORA     $C801               
BAE4: 0D 01 D0        ORA     $D001               
BAE7: 07 ; ????
BAE8: 01 D8           ORA     ($D8,X)             
BAEA: 07 ; ????
BAEB: 01 FD           ORA     ($FD,X)             
BAED: FF ; ????
BAEE: 01 27           ORA     ($27,X)             
BAF0: 09 01           ORA     #$01                
BAF2: 3E 02 02        ROL     $0202,X             
BAF5: 50 08           BVC     $BAFF               ; {}
BAF7: 00              BRK                         
BAF8: 59 06 01        EOR     $0106,Y             
BAFB: 64 ; ????
BAFC: 02 ; ????
BAFD: 03 ; ????
BAFE: 67 ; ????
BAFF: 0A              ASL     A                   
BB00: 01 6A           ORA     ($6A,X)             
BB02: 09 01           ORA     #$01                
BB04: 81 04           STA     ($04,X)             
BB06: 02 ; ????
BB07: 90 08           BCC     $BB11               ; {}
BB09: 00              BRK                         
BB0A: 91 08           STA     ($08),Y             
BB0C: 00              BRK                         
BB0D: A1 01           LDA     ($01,X)             
BB0F: 01 A7           ORA     ($A7,X)             
BB11: 05 01           ORA     $01                 
BB13: AA              TAX                         
BB14: 05 01           ORA     $01                 
BB16: D0 07           BNE     $BB1F               ; {}
BB18: 01 D8           ORA     ($D8,X)             
BB1A: 07 ; ????
BB1B: 01 FD           ORA     ($FD,X)             
BB1D: FF ; ????
BB1E: 01 21           ORA     ($21,X)             
BB20: 06 01           ASL     $01                 
BB22: 26 06           ROL     $06                 
BB24: 01 2A           ORA     ($2A,X)             
BB26: 06 01           ASL     $01                 
BB28: 32 ; ????
BB29: 09 01           ORA     #$01                
BB2B: 37 ; ????
BB2C: 09 01           ORA     #$01                
BB2E: 3C ; ????
BB2F: 09 01           ORA     #$01                
BB31: 64 ; ????
BB32: 02 ; ????
BB33: 02 ; ????
BB34: 72 ; ????
BB35: 0A              ASL     A                   
BB36: 01 77           ORA     ($77,X)             
BB38: 0A              ASL     A                   
BB39: 01 7C           ORA     ($7C,X)             
BB3B: 0A              ASL     A                   
BB3C: 01 B2           ORA     ($B2,X)             
BB3E: 05 01           ORA     $01                 
BB40: B7 ; ????
BB41: 05 01           ORA     $01                 
BB43: BC 05 01        LDY     $0105,X             
BB46: BE 02 03        LDX     $0302,Y             
BB49: D0 07           BNE     $BB52               ; {}
BB4B: 01 D8           ORA     ($D8,X)             
BB4D: 07 ; ????
BB4E: 01 FD           ORA     ($FD,X)             
BB50: FF ; ????
BB51: 01 12           ORA     ($12,X)             
BB53: 02 ; ????
BB54: 02 ; ????
BB55: 27 ; ????
BB56: 09 01           ORA     #$01                
BB58: 2D 02 03        AND     $0302               
BB5B: 63 ; ????
BB5C: 03 ; ????
BB5D: 01 67           ORA     ($67,X)             
BB5F: 05 01           ORA     $01                 
BB61: 6C 03 01        JMP     ($0103)             
BB64: 90 0E           BCC     $BB74               ; {}
BB66: 00              BRK                         
BB67: 94 0E           STY     $0E,X               
BB69: 00              BRK                         
BB6A: 98              TYA                         
BB6B: 0E 00 9C        ASL     $9C00               ; {}
BB6E: 0E 00 D0        ASL     $D000               
BB71: 07 ; ????
BB72: 01 D8           ORA     ($D8,X)             
BB74: 07 ; ????
BB75: 01 FD           ORA     ($FD,X)             
BB77: FF ; ????
BB78: 02 ; ????
BB79: 14 ; ????
BB7A: 0D 02 18        ORA     $1802               
BB7D: 0D 02 1C        ORA     $1C02               
BB80: 0D 02 3A        ORA     $3A02               
BB83: 08              PHP                         
BB84: 02 ; ????
BB85: 4D 02 03        EOR     $0302               
BB88: 55 08           EOR     $08,X               
BB8A: 02 ; ????
BB8B: 70 09           BVS     $BB96               ; {}
BB8D: 01 81           ORA     ($81,X)             
BB8F: 11 00           ORA     ($00),Y             ; {ram.GP_00}
BB91: 8F ; ????
BB92: 08              PHP                         
BB93: 02 ; ????
BB94: A5 11           LDA     $11                 
BB96: 00              BRK                         
BB97: B0 0E           BCS     $BBA7               ; {}
BB99: 02 ; ????
BB9A: C4 0D           CPY     $0D                 
BB9C: 02 ; ????
BB9D: C8              INY                         
BB9E: 0D 02 CC        ORA     $CC02               
BBA1: 0D 02 D0        ORA     $D002               
BBA4: 07 ; ????
BBA5: 01 D8           ORA     ($D8,X)             
BBA7: 07 ; ????
BBA8: 01 FD           ORA     ($FD,X)             
BBAA: FF ; ????
BBAB: 01 10           ORA     ($10,X)             
BBAD: 0D 02 14        ORA     $1402               
BBB0: 0D 02 18        ORA     $1802               
BBB3: 0D 02 1C        ORA     $1C02               
BBB6: 0D 02 22        ORA     $2202               
BBB9: 09 01           ORA     #$01                
BBBB: 2A              ROL     A                   
BBBC: 09 01           ORA     #$01                
BBBE: 62 ; ????
BBBF: 0A              ASL     A                   
BBC0: 01 6A           ORA     ($6A,X)             
BBC2: 0A              ASL     A                   
BBC3: 01 93           ORA     ($93,X)             
BBC5: 11 00           ORA     ($00),Y             ; {ram.GP_00}
BBC7: 96 03           STX     $03,Y               
BBC9: 01 9C           ORA     ($9C,X)             
BBCB: 11 00           ORA     ($00),Y             ; {ram.GP_00}
BBCD: 9D 03 01        STA     $0103,X             
BBD0: A2 05           LDX     #$05                
BBD2: 01 A8           ORA     ($A8,X)             
BBD4: 11 00           ORA     ($00),Y             ; {ram.GP_00}
BBD6: AA              TAX                         
BBD7: 05 01           ORA     $01                 
BBD9: B0 0E           BCS     $BBE9               ; {}
BBDB: 02 ; ????
BBDC: C4 0E           CPY     $0E                 
BBDE: 02 ; ????
BBDF: C8              INY                         
BBE0: 0E 02 CC        ASL     $CC02               
BBE3: 0E 02 D0        ASL     $D002               
BBE6: 07 ; ????
BBE7: 01 D8           ORA     ($D8,X)             
BBE9: 07 ; ????
BBEA: 01 FD           ORA     ($FD,X)             
BBEC: FF ; ????
BBED: 04 ; ????
BBEE: 30 30           BMI     $BC20               ; {}
BBF0: 30 30           BMI     $BC22               ; {}
BBF2: FF ; ????
BBF3: 01 50           ORA     ($50,X)             
BBF5: 01 51           ORA     ($51,X)             
BBF7: FF ; ????
BBF8: 01 05           ORA     ($05,X)             
BBFA: FF ; ????
BBFB: 01 06           ORA     ($06,X)             
BBFD: 01 07           ORA     ($07,X)             
BBFF: 01 08           ORA     ($08,X)             
BC01: FF ; ????
BC02: 01 14           ORA     ($14,X)             
BC04: 01 15           ORA     ($15,X)             
BC06: FF ; ????
BC07: 01 02           ORA     ($02,X)             
BC09: 01 02           ORA     ($02,X)             
BC0B: 01 02           ORA     ($02,X)             
BC0D: FF ; ????
BC0E: 04 ; ????
BC0F: 09 09           ORA     #$09                
BC11: 09 09           ORA     #$09                
BC13: FF ; ????
BC14: 08              PHP                         
BC15: 0C ; ????
BC16: 0A              ASL     A                   
BC17: 0B ; ????
BC18: 0A              ASL     A                   
BC19: 0B ; ????
BC1A: 0A              ASL     A                   
BC1B: 0B ; ????
BC1C: 0D 08 16        ORA     $1608               
BC1F: 16 16           ASL     $16,X               
BC21: 16 16           ASL     $16,X               
BC23: 16 16           ASL     $16,X               
BC25: 16 FF           ASL     $FF,X               
BC27: 01 52           ORA     ($52,X)             
BC29: 01 52           ORA     ($52,X)             
BC2B: 01 52           ORA     ($52,X)             
BC2D: 01 52           ORA     ($52,X)             
BC2F: FF ; ????
BC30: 01 01           ORA     ($01,X)             
BC32: 01 02           ORA     ($02,X)             
BC34: 01 03           ORA     ($03,X)             
BC36: 01 02           ORA     ($02,X)             
BC38: FF ; ????
BC39: 01 03           ORA     ($03,X)             
BC3B: 01 03           ORA     ($03,X)             
BC3D: 01 03           ORA     ($03,X)             
BC3F: 01 03           ORA     ($03,X)             
BC41: FF ; ????
BC42: 04 ; ????
BC43: 5F ; ????
BC44: 57 ; ????
BC45: 57 ; ????
BC46: 57 ; ????
BC47: 04 ; ????
BC48: 5F ; ????
BC49: 57 ; ????
BC4A: 57 ; ????
BC4B: 57 ; ????
BC4C: 04 ; ????
BC4D: 5F ; ????
BC4E: 60              RTS                         
BC4F: 60              RTS                         
BC50: 57 ; ????
BC51: 04 ; ????
BC52: 58              CLI                         
BC53: 59 5E 57        EOR     $575E,Y             
BC56: FF ; ????
BC57: 02 ; ????
BC58: 5A ; ????
BC59: 5B ; ????
BC5A: 02 ; ????
BC5B: 5C ; ????
BC5C: 5D 02 5F        EOR     $5F02,X             
BC5F: 57 ; ????
BC60: FF ; ????
BC61: 04 ; ????
BC62: 52 ; ????
BC63: 52 ; ????
BC64: 52 ; ????
BC65: 52 ; ????
BC66: FF ; ????
BC67: 04 ; ????
BC68: 52 ; ????
BC69: 52 ; ????
BC6A: 52 ; ????
BC6B: 52 ; ????
BC6C: 04 ; ????
BC6D: 52 ; ????
BC6E: 52 ; ????
BC6F: 52 ; ????
BC70: 52 ; ????
BC71: 04 ; ????
BC72: 52 ; ????
BC73: 52 ; ????
BC74: 52 ; ????
BC75: 52 ; ????
BC76: 04 ; ????
BC77: 52 ; ????
BC78: 52 ; ????
BC79: 52 ; ????
BC7A: 52 ; ????
BC7B: FF ; ????
BC7C: 02 ; ????
BC7D: 60              RTS                         
BC7E: 5E 02 60        LSR     $6002,X             
BC81: 57 ; ????
BC82: 02 ; ????
BC83: 60              RTS                         
BC84: 57 ; ????
BC85: 02 ; ????
BC86: 5E 57 02        LSR     $0257,X             
BC89: 57 ; ????
BC8A: 57 ; ????
BC8B: FF ; ????
BC8C: 02 ; ????
BC8D: 53 ; ????
BC8E: 54 ; ????
BC8F: 02 ; ????
BC90: 55 56           EOR     $56,X               
BC92: FF ; ????
BC93: 04 ; ????
BC94: 13 ; ????
BC95: 19 04 19        ORA     $1904,Y             
BC98: 04 ; ????
BC99: 04 ; ????
BC9A: 04 ; ????
BC9B: 04 ; ????
BC9C: 04 ; ????
BC9D: 04 ; ????
BC9E: 13 ; ????
BC9F: 04 ; ????
BCA0: 04 ; ????
BCA1: 13 ; ????
BCA2: 04 ; ????
BCA3: 04 ; ????
BCA4: 19 04 04        ORA     $0404,Y             
BCA7: FF ; ????
BCA8: 12 ; ????
BCA9: 12 ; ????
BCAA: 12 ; ????
BCAB: 12 ; ????
BCAC: 8B ; ????
BCAD: 8C 8D 8E        STY     $8E8D               ; {}
BCB0: 8F ; ????
BCB1: 90 6D           BCC     $BD20               ; {}
BCB3: 6E 91 92        ROR     $9291               ; {}
BCB6: 91 92           STA     ($92),Y             
BCB8: 6F ; ????
BCB9: 6F ; ????
BCBA: 6F ; ????
BCBB: 6F ; ????
BCBC: CE 12 12        DEC     $1212               
BCBF: 12 ; ????
BCC0: DE DF E0        DEC     $E0DF,X             
BCC3: E1 E2           SBC     ($E2,X)             
BCC5: E3 ; ????
BCC6: E4 E5           CPX     $E5                 
BCC8: E6 E7           INC     $E7                 
BCCA: E8              INX                         
BCCB: E9 EA           SBC     #$EA                
BCCD: EB ; ????
BCCE: EC D8 ED        CPX     $EDD8               
BCD1: EE F1 F2        INC     $F2F1               
BCD4: EF ; ????
BCD5: F0 F1           BEQ     $BCC8               ; {}
BCD7: F1 12           SBC     ($12),Y             
BCD9: F3 ; ????
BCDA: F3 ; ????
BCDB: F1 F4           SBC     ($F4),Y             
BCDD: 12 ; ????
BCDE: F1 F4           SBC     ($F4),Y             
BCE0: 7B ; ????
BCE1: 12 ; ????
BCE2: 12 ; ????
BCE3: 12 ; ????
BCE4: 7B ; ????
BCE5: 12 ; ????
BCE6: 12 ; ????
BCE7: 12 ; ????
BCE8: 7B ; ????
BCE9: 12 ; ????
BCEA: 12 ; ????
BCEB: 12 ; ????
BCEC: 7B ; ????
BCED: 12 ; ????
BCEE: 12 ; ????
BCEF: 12 ; ????
BCF0: 7B ; ????
BCF1: 12 ; ????
BCF2: 12 ; ????
BCF3: 12 ; ????
BCF4: 87 ; ????
BCF5: 88              DEY                         
BCF6: 6F ; ????
BCF7: 86 70           STX     $70                 
BCF9: 71 72           ADC     ($72),Y             
BCFB: 73 ; ????
BCFC: 72 ; ????
BCFD: 73 ; ????
BCFE: 72 ; ????
BCFF: 73 ; ????
BD00: F1 F1           SBC     ($F1),Y             
BD02: F1 F1           SBC     ($F1),Y             
BD04: 7B ; ????
BD05: 12 ; ????
BD06: 12 ; ????
BD07: 12 ; ????
BD08: 7B ; ????
BD09: 12 ; ????
BD0A: 12 ; ????
BD0B: 12 ; ????
BD0C: 85 86           STA     $86                 
BD0E: 87 ; ????
BD0F: 6F ; ????
BD10: 7B ; ????
BD11: 12 ; ????
BD12: 12 ; ????
BD13: 12 ; ????
BD14: 7B ; ????
BD15: 12 ; ????
BD16: 12 ; ????
BD17: 12 ; ????
BD18: 7B ; ????
BD19: 12 ; ????
BD1A: 12 ; ????
BD1B: 12 ; ????
BD1C: 7B ; ????
BD1D: 12 ; ????
BD1E: 12 ; ????
BD1F: 12 ; ????
BD20: 7B ; ????
BD21: 12 ; ????
BD22: 12 ; ????
BD23: 12 ; ????
BD24: 7B ; ????
BD25: 12 ; ????
BD26: 12 ; ????
BD27: 12 ; ????
BD28: 7B ; ????
BD29: 12 ; ????
BD2A: 12 ; ????
BD2B: 12 ; ????
BD2C: 7B ; ????
BD2D: 12 ; ????
BD2E: 12 ; ????
BD2F: 12 ; ????
BD30: 7B ; ????
BD31: 12 ; ????
BD32: 12 ; ????
BD33: 12 ; ????
BD34: 7B ; ????
BD35: 12 ; ????
BD36: 12 ; ????
BD37: 12 ; ????
BD38: 7B ; ????
BD39: 12 ; ????
BD3A: 12 ; ????
BD3B: 12 ; ????
BD3C: 7B ; ????
BD3D: 12 ; ????
BD3E: 12 ; ????
BD3F: 12 ; ????
BD40: 7B ; ????
BD41: 12 ; ????
BD42: 12 ; ????
BD43: 12 ; ????
BD44: 7B ; ????
BD45: 12 ; ????
BD46: 12 ; ????
BD47: 12 ; ????
BD48: 7B ; ????
BD49: 12 ; ????
BD4A: 12 ; ????
BD4B: 12 ; ????
BD4C: 7B ; ????
BD4D: 12 ; ????
BD4E: 12 ; ????
BD4F: 12 ; ????
BD50: 7B ; ????
BD51: 12 ; ????
BD52: 12 ; ????
BD53: 12 ; ????
BD54: 7B ; ????
BD55: 12 ; ????
BD56: 12 ; ????
BD57: 12 ; ????
BD58: 7B ; ????
BD59: 12 ; ????
BD5A: 12 ; ????
BD5B: 12 ; ????
BD5C: 7B ; ????
BD5D: 12 ; ????
BD5E: 12 ; ????
BD5F: 12 ; ????
BD60: 7B ; ????
BD61: 12 ; ????
BD62: 12 ; ????
BD63: 12 ; ????
BD64: 7B ; ????
BD65: 12 ; ????
BD66: 12 ; ????
BD67: 12 ; ????
BD68: AA              TAX                         
BD69: AA              TAX                         
BD6A: AB ; ????
BD6B: AB ; ????
BD6C: 7B ; ????
BD6D: 12 ; ????
BD6E: 12 ; ????
BD6F: 12 ; ????
BD70: 7B ; ????
BD71: 12 ; ????
BD72: 12 ; ????
BD73: 12 ; ????
BD74: 7B ; ????
BD75: 12 ; ????
BD76: 12 ; ????
BD77: 12 ; ????
BD78: 7B ; ????
BD79: 12 ; ????
BD7A: 12 ; ????
BD7B: 12 ; ????
BD7C: 7B ; ????
BD7D: 12 ; ????
BD7E: 12 ; ????
BD7F: 12 ; ????
BD80: 7B ; ????
BD81: 12 ; ????
BD82: 12 ; ????
BD83: 12 ; ????
BD84: 7B ; ????
BD85: 12 ; ????
BD86: 12 ; ????
BD87: 12 ; ????
BD88: 7B ; ????
BD89: 12 ; ????
BD8A: 12 ; ????
BD8B: 12 ; ????
BD8C: 7B ; ????
BD8D: 12 ; ????
BD8E: 12 ; ????
BD8F: 12 ; ????
BD90: 7B ; ????
BD91: 12 ; ????
BD92: 12 ; ????
BD93: 12 ; ????
BD94: 7B ; ????
BD95: 12 ; ????
BD96: 12 ; ????
BD97: 12 ; ????
BD98: 7B ; ????
BD99: 12 ; ????
BD9A: 12 ; ????
BD9B: 12 ; ????
BD9C: 7B ; ????
BD9D: 12 ; ????
BD9E: 12 ; ????
BD9F: 12 ; ????
BDA0: 7B ; ????
BDA1: 12 ; ????
BDA2: 12 ; ????
BDA3: 12 ; ????
BDA4: 7B ; ????
BDA5: 12 ; ????
BDA6: 12 ; ????
BDA7: 12 ; ????
BDA8: 7B ; ????
BDA9: 12 ; ????
BDAA: 12 ; ????
BDAB: 12 ; ????
BDAC: 7B ; ????
BDAD: 12 ; ????
BDAE: 12 ; ????
BDAF: 12 ; ????
BDB0: 7B ; ????
BDB1: 12 ; ????
BDB2: 12 ; ????
BDB3: 12 ; ????
BDB4: 7B ; ????
BDB5: 12 ; ????
BDB6: 12 ; ????
BDB7: 12 ; ????
BDB8: 7B ; ????
BDB9: 12 ; ????
BDBA: 12 ; ????
BDBB: 12 ; ????
BDBC: 7B ; ????
BDBD: 12 ; ????
BDBE: 12 ; ????
BDBF: 12 ; ????
BDC0: 7B ; ????
BDC1: 12 ; ????
BDC2: 12 ; ????
BDC3: 12 ; ????
BDC4: 7B ; ????
BDC5: 12 ; ????
BDC6: 12 ; ????
BDC7: 12 ; ????
BDC8: 7B ; ????
BDC9: 12 ; ????
BDCA: 12 ; ????
BDCB: 12 ; ????
BDCC: 7B ; ????
BDCD: 12 ; ????
BDCE: 12 ; ????
BDCF: 12 ; ????
BDD0: 7B ; ????
BDD1: 12 ; ????
BDD2: 12 ; ????
BDD3: 12 ; ????
BDD4: 7B ; ????
BDD5: 12 ; ????
BDD6: 12 ; ????
BDD7: 12 ; ????
BDD8: 7B ; ????
BDD9: 12 ; ????
BDDA: 12 ; ????
BDDB: 12 ; ????
BDDC: 7B ; ????
BDDD: 12 ; ????
BDDE: 12 ; ????
BDDF: 12 ; ????
BDE0: 7B ; ????
BDE1: 12 ; ????
BDE2: 12 ; ????
BDE3: 12 ; ????
BDE4: 7B ; ????
BDE5: 12 ; ????
BDE6: 12 ; ????
BDE7: 12 ; ????
BDE8: 60              RTS                         
BDE9: 61 62           ADC     ($62,X)             
BDEB: 63 ; ????
BDEC: 62 ; ????
BDED: 63 ; ????
BDEE: 62 ; ????
BDEF: 63 ; ????
BDF0: 4F ; ????
BDF1: 4E 4E 4F        LSR     $4F4E               
BDF4: C9 C1           CMP     #$C1                
BDF6: CC CD CA        CPY     $CACD               
BDF9: CB ; ????
BDFA: C1 D1           CMP     ($D1,X)             
BDFC: CF ; ????
BDFD: D0 D2           BNE     $BDD1               ; {}
BDFF: C1 C1           CMP     ($C1,X)             
BE01: D1 C1           CMP     ($C1),Y             
BE03: D3 ; ????
BE04: C0 C0           CPY     #$C0                
BE06: C0 C0           CPY     #$C0                
BE08: C2 ; ????
BE09: C3 ; ????
BE0A: C5 C6           CMP     $C6                 
BE0C: C4 D6           CPY     $D6                 
BE0E: C7 ; ????
BE0F: C8              INY                         
BE10: D4 ; ????
BE11: D5 D7           CMP     $D7,X               
BE13: D7 ; ????
BE14: D6 D5           DEC     $D5,X               
BE16: D7 ; ????
BE17: D9 DA D5        CMP     $D5DA,Y             
BE1A: DC ; ????
BE1B: D6 DB           DEC     $DB,X               
BE1D: DB ; ????
BE1E: D6 D5           DEC     $D5,X               
BE20: D5 C0           CMP     $C0,X               
BE22: D6 C0           DEC     $C0,X               
BE24: C0 C0           CPY     #$C0                
BE26: 12 ; ????
BE27: C0 D5           CPY     #$D5                
BE29: C0 D6           CPY     #$D6                
BE2B: D5 7B           CMP     $7B,X               
BE2D: 12 ; ????
BE2E: 12 ; ????
BE2F: 12 ; ????
BE30: 7B ; ????
BE31: 12 ; ????
BE32: 12 ; ????
BE33: 12 ; ????
BE34: 7B ; ????
BE35: 12 ; ????
BE36: 12 ; ????
BE37: 12 ; ????
BE38: 7B ; ????
BE39: 12 ; ????
BE3A: 12 ; ????
BE3B: 12 ; ????
BE3C: 7B ; ????
BE3D: 12 ; ????
BE3E: 12 ; ????
BE3F: 12 ; ????
BE40: 7B ; ????
BE41: 12 ; ????
BE42: 12 ; ????
BE43: 12 ; ????
BE44: 7B ; ????
BE45: 12 ; ????
BE46: 12 ; ????
BE47: 12 ; ????
BE48: 7B ; ????
BE49: 12 ; ????
BE4A: 12 ; ????
BE4B: 12 ; ????
BE4C: 7B ; ????
BE4D: 12 ; ????
BE4E: 12 ; ????
BE4F: 12 ; ????
BE50: 7B ; ????
BE51: 12 ; ????
BE52: 12 ; ????
BE53: 12 ; ????
BE54: 7B ; ????
BE55: 12 ; ????
BE56: 12 ; ????
BE57: 12 ; ????
BE58: 7B ; ????
BE59: 12 ; ????
BE5A: 12 ; ????
BE5B: 12 ; ????
BE5C: 7B ; ????
BE5D: 12 ; ????
BE5E: 12 ; ????
BE5F: 12 ; ????
BE60: 7B ; ????
BE61: 12 ; ????
BE62: 12 ; ????
BE63: 12 ; ????
BE64: 7B ; ????
BE65: 12 ; ????
BE66: 12 ; ????
BE67: 12 ; ????
BE68: 7B ; ????
BE69: 12 ; ????
BE6A: 12 ; ????
BE6B: 12 ; ????
BE6C: 00              BRK                         
BE6D: 05 F0           ORA     $F0                 
BE6F: 05 00           ORA     $00                 ; {ram.GP_00}
BE71: 05 F0           ORA     $F0                 
BE73: 05 00           ORA     $00                 ; {ram.GP_00}
BE75: 04 ; ????
BE76: 40              RTI                         
BE77: 04 ; ????
BE78: 00              BRK                         
BE79: 04 ; ????
BE7A: 40              RTI                         
BE7B: 04 ; ????
BE7C: A6 BE           LDX     $BE                 
BE7E: A6 BE           LDX     $BE                 
BE80: A6 BE           LDX     $BE                 
BE82: EE BA EE        INC     $EEBA               
BE85: BA              TSX                         
BE86: EE BA EE        INC     $EEBA               
BE89: BA              TSX                         
BE8A: EE BA EE        INC     $EEBA               
BE8D: BA              TSX                         
BE8E: EE BA EE        INC     $EEBA               
BE91: BA              TSX                         
BE92: EE BA EE        INC     $EEBA               
BE95: BA              TSX                         
BE96: EE BA EE        INC     $EEBA               
BE99: BA              TSX                         
BE9A: EE BA EE        INC     $EEBA               
BE9D: BA              TSX                         
BE9E: EE BA EE        INC     $EEBA               
BEA1: BA              TSX                         
BEA2: EE BA EE        INC     $EEBA               
BEA5: BA              TSX                         
BEA6: EE BA 1E        INC     $1EBA               
BEA9: BB ; ????
BEAA: 1E BB 1E        ASL     $1EBB,X             
BEAD: BB ; ????
BEAE: 1E BB 51        ASL     $51BB,X             
BEB1: BB ; ????
BEB2: 51 BB           EOR     ($BB),Y             
BEB4: 51 BB           EOR     ($BB),Y             
BEB6: 78              SEI                         
BEB7: BB ; ????
BEB8: 78              SEI                         
BEB9: BB ; ????
BEBA: AB ; ????
BEBB: BB ; ????
BEBC: AB ; ????
BEBD: BB ; ????
BEBE: AB ; ????
BEBF: BB ; ????
BEC0: 7C ; ????
BEC1: BA              TSX                         
BEC2: AF ; ????
BEC3: BA              TSX                         
BEC4: FF ; ????
BEC5: FF ; ????
BEC6: ED BB F3        SBC     $F3BB               
BEC9: BB ; ????
BECA: F8              SED                         
BECB: BB ; ????
BECC: FB ; ????
BECD: BB ; ????
BECE: 02 ; ????
BECF: BC 07 BC        LDY     $BC07,X             ; {}
BED2: 0E BC 14        ASL     $14BC               
BED5: BC 27 BC        LDY     $BC27,X             ; {}
BED8: 30 BC           BMI     $BE96               ; {}
BEDA: 39 BC 42        AND     $42BC,Y             
BEDD: BC 57 BC        LDY     $BC57,X             ; {}
BEE0: 61 BC           ADC     ($BC,X)             
BEE2: 67 ; ????
BEE3: BC 7C BC        LDY     $BC7C,X             ; {}
BEE6: 8C BC 93        STY     $93BC               ; {}
BEE9: BC 03 00        LDY     $0003,X             
BEEC: 02 ; ????
BEED: 88              DEY                         
BEEE: 00              BRK                         
BEEF: 00              BRK                         
BEF0: 03 ; ????
BEF1: 88              DEY                         
BEF2: 01 00           ORA     ($00,X)             ; {ram.GP_00}
BEF4: 04 ; ????
BEF5: 88              DEY                         
BEF6: 00              BRK                         
BEF7: FD BE FD        SBC     $FDBE,X             
BEFA: BE FD BE        LDX     $BEFD,Y             ; {}
BEFD: 00              BRK                         
BEFE: 04 ; ????
BEFF: 06 06           ASL     $06                 
BF01: 04 ; ????
BF02: 04 ; ????
BF03: 08              PHP                         
BF04: 08              PHP                         
BF05: 0A              ASL     A                   
BF06: 0A              ASL     A                   
BF07: 07 ; ????
BF08: 07 ; ????
BF09: 07 ; ????
BF0A: 00              BRK                         
BF0B: 00              BRK                         
BF0C: 12 ; ????
BF0D: BF ; ????
BF0E: 12 ; ????
BF0F: BF ; ????
BF10: 12 ; ????
BF11: BF ; ????
BF12: 00              BRK                         
BF13: 00              BRK                         
BF14: 00              BRK                         
BF15: 09 00           ORA     #$00                
BF17: 09 00           ORA     #$00                
BF19: 00              BRK                         
BF1A: 00              BRK                         
BF1B: 00              BRK                         
BF1C: 00              BRK                         
BF1D: 00              BRK                         
BF1E: 00              BRK                         
BF1F: 00              BRK                         
BF20: 00              BRK                         
BF21: 1F ; ????
BF22: 3F ; ????
BF23: 5F ; ????
BF24: 0F ; ????
BF25: 30 15           BMI     $BF3C               ; {}
BF27: 0C ; ????
BF28: 0F ; ????
BF29: 21 13           AND     ($13,X)             
BF2B: 02 ; ????
BF2C: 0F ; ????
BF2D: 27 ; ????
BF2E: 18              CLC                         
BF2F: 09 0F           ORA     #$0F                
BF31: 36 14           ROL     $14,X               
BF33: 15 0F           ORA     $0F,X               
BF35: 20 26 07        JSR     $0726               
BF38: 0F ; ????
BF39: 31 02           AND     ($02),Y             
BF3B: 15 0F           ORA     $0F,X               
BF3D: 12 ; ????
BF3E: 25 31           AND     $31                 
BF40: 0F ; ????
BF41: 09 2A           ORA     #$2A                
BF43: 37 ; ????
BF44: 00              BRK                         
BF45: 00              BRK                         
BF46: 00              BRK                         
BF47: 00              BRK                         
BF48: 04 ; ????
BF49: 00              BRK                         
BF4A: 02 ; ????
BF4B: 00              BRK                         
BF4C: 02 ; ????
BF4D: 0A              ASL     A                   
BF4E: 02 ; ????
BF4F: 00              BRK                         
BF50: 00              BRK                         
BF51: 0A              ASL     A                   
BF52: 00              BRK                         
BF53: 00              BRK                         
BF54: 01 01           ORA     ($01,X)             
BF56: 01 01           ORA     ($01,X)             
BF58: 03 ; ????
BF59: 02 ; ????
BF5A: 03 ; ????
BF5B: 02 ; ????
BF5C: 03 ; ????
BF5D: 05 03           ORA     $03                 
BF5F: 0A              ASL     A                   
BF60: 0A              ASL     A                   
BF61: 05 01           ORA     $01                 
BF63: 00              BRK                         
BF64: 01 01           ORA     ($01,X)             
BF66: 01 01           ORA     ($01,X)             
BF68: 03 ; ????
BF69: 02 ; ????
BF6A: 03 ; ????
BF6B: 02 ; ????
BF6C: 03 ; ????
BF6D: 04 ; ????
BF6E: 02 ; ????
BF6F: 0A              ASL     A                   
BF70: 0A              ASL     A                   
BF71: 02 ; ????
BF72: 01 00           ORA     ($00,X)             ; {ram.GP_00}
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
BFF8: 00              BRK                         
BFF9: 1C ; ????
BFFA: 80 ; ????
BFFB: 02 ; ????
BFFC: 04 ; ????
BFFD: 41 00           EOR     ($00,X)             ; {ram.GP_00}
BFFF: 00              BRK                         
```

