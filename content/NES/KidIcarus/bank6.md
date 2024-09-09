![Bank 6](KidIcarus.jpg)

# Bank 6

>>> cpu 6502

>>> binary 8000:roms/KidIcarus.nes[18010:1C010]

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](Hardware.md)

```code
8000: 35 81           AND     $81,X               
8002: 28              PLP                         
8003: 80 ; ????
8004: 75 80           ADC     $80,X               
8006: FE 94 43        INC     $4394,X             
8009: 95 4C           STA     $4C,X               
800B: 95 4A           STA     $4A,X               
800D: 8F ; ????
800E: D4 ; ????
800F: 95 D0           STA     $D0,X               
8011: 98              TYA                         
8012: E5 87           SBC     $87                 
8014: 00              BRK                         
8015: 88              DEY                         
8016: A7 ; ????
8017: 88              DEY                         
8018: 1F ; ????
8019: 83 ; ????
801A: 5D 8B 92        EOR     $928B,X             ; {}
801D: 8B ; ????
801E: BF ; ????
801F: 8B ; ????
8020: 5E 8C C6        LSR     $C68C,X             
8023: 8B ; ????
8024: EB ; ????
8025: 8C 47 8C        STY     $8C47               ; {}
8028: 20 C6 98        JSR     $98C6               ; {}
802B: A5 3A           LDA     $3A                 
802D: 29 F0           AND     #$F0                
802F: D0 5F           BNE     $8090               ; {}
8031: 20 D4 95        JSR     $95D4               ; {}
8034: A5 3B           LDA     $3B                 
8036: 29 0F           AND     #$0F                
8038: C9 08           CMP     #$08                
803A: B0 13           BCS     $804F               ; {}
803C: 20 2B EE        JSR     $EE2B               
803F: 52 ; ????
8040: 80 ; ????
8041: 52 ; ????
8042: 80 ; ????
8043: 7E 86 91        ROR     $9186,X             ; {}
8046: 87 ; ????
8047: 5B ; ????
8048: 8A              TXA                         
8049: 3D 8B F4        AND     $F48B,X             
804C: 8F ; ????
804D: C4 90           CPY     $90                 
804F: 4C 21 91        JMP     $9121               ; {}
8052: A5 3A           LDA     $3A                 
8054: 20 2B EE        JSR     $EE2B               
8057: 90 80           BCC     $7FD9               
8059: F7 ; ????
805A: E0 6F           CPX     #$6F                
805C: 80 ; ????
805D: 83 ; ????
805E: 91 8E           STA     ($8E),Y             
8060: 80 ; ????
8061: 6F ; ????
8062: 80 ; ????
8063: 91 80           STA     ($80),Y             
8065: 3B ; ????
8066: E1 C9           SBC     ($C9,X)             
8068: 80 ; ????
8069: E6 80           INC     $80                 
806B: 20 81 6F        JSR     $6F81               
806E: 80 ; ????
806F: A9 00           LDA     #$00                
8071: 8D 24 07        STA     $0724               
8074: 60              RTS                         
8075: 20 C6 98        JSR     $98C6               ; {}
8078: A5 3A           LDA     $3A                 
807A: D0 14           BNE     $8090               ; {}
807C: 84 3B           STY     $3B                 
807E: A9 00           LDA     #$00                
8080: 8D 24 07        STA     $0724               
8083: E6 3A           INC     $3A                 
8085: A9 02           LDA     #$02                
8087: 85 37           STA     $37                 
8089: A9 03           LDA     #$03                
808B: 4C F0 E2        JMP     $E2F0               
808E: E6 3A           INC     $3A                 
8090: 60              RTS                         
8091: 20 9D 80        JSR     $809D               ; {}
8094: 20 62 83        JSR     $8362               ; {}
8097: A9 00           LDA     #$00                
8099: 8D 28 07        STA     $0728               
809C: 60              RTS                         
809D: E6 3A           INC     $3A                 
809F: A9 00           LDA     #$00                
80A1: 85 16           STA     $16                 
80A3: 85 18           STA     $18                 
80A5: 8D 24 07        STA     $0724               
80A8: A9 CB           LDA     #$CB                
80AA: 48              PHA                         
80AB: A9 B5           LDA     #$B5                
80AD: 48              PHA                         
80AE: 20 F7 CA        JSR     $CAF7               
80B1: 60              RTS                         
80B2: A2 20           LDX     #$20                
80B4: A9 CD           LDA     #$CD                
80B6: 48              PHA                         
80B7: A9 04           LDA     #$04                
80B9: 48              PHA                         
80BA: 20 F7 CA        JSR     $CAF7               
80BD: A9 C3           LDA     #$C3                
80BF: 48              PHA                         
80C0: A9 D8           LDA     #$D8                
80C2: 48              PHA                         
80C3: 20 F7 CA        JSR     $CAF7               
80C6: 4C DB 80        JMP     $80DB               ; {}
80C9: 20 B2 80        JSR     $80B2               ; {}
80CC: F0 06           BEQ     $80D4               ; {}
80CE: 20 F0 90        JSR     $90F0               ; {}
80D1: 4C D7 83        JMP     $83D7               ; {}
80D4: E6 3A           INC     $3A                 
80D6: E6 3A           INC     $3A                 
80D8: 4C DB 87        JMP     $87DB               ; {}
80DB: A9 21           LDA     #$21                
80DD: CD D5 04        CMP     $04D5               
80E0: F0 03           BEQ     $80E5               ; {}
80E2: CD D6 04        CMP     $04D6               
80E5: 60              RTS                         
80E6: CE 24 07        DEC     $0724               
80E9: D0 FA           BNE     $80E5               ; {}
80EB: E6 3A           INC     $3A                 
80ED: A9 80           LDA     #$80                
80EF: 8D 24 07        STA     $0724               
80F2: A2 60           LDX     #$60                
80F4: BD 01 07        LDA     $0701,X             
80F7: 29 0F           AND     #$0F                
80F9: C9 04           CMP     #$04                
80FB: F0 18           BEQ     $8115               ; {}
80FD: A9 F8           LDA     #$F8                
80FF: 9D 00 02        STA     $0200,X             
8102: 9D 04 02        STA     $0204,X             
8105: 9D 08 02        STA     $0208,X             
8108: 9D 0C 02        STA     $020C,X             
810B: 8A              TXA                         
810C: 18              CLC                         
810D: 69 10           ADC     #$10                
810F: AA              TAX                         
8110: E0 E0           CPX     #$E0                
8112: 90 E0           BCC     $80F4               ; {}
8114: 60              RTS                         
8115: A9 0E           LDA     #$0E                
8117: 20 32 99        JSR     $9932               ; {}
811A: 20 23 85        JSR     $8523               ; {}
811D: 4C 0B 81        JMP     $810B               ; {}
8120: 20 F2 80        JSR     $80F2               ; {}
8123: CE 24 07        DEC     $0724               
8126: AD 24 07        LDA     $0724               
8129: 29 3F           AND     #$3F                
812B: D0 B8           BNE     $80E5               ; {}
812D: E6 3A           INC     $3A                 
812F: A9 80           LDA     #$80                
8131: 8D 24 07        STA     $0724               
8134: 60              RTS                         
8135: 20 C6 98        JSR     $98C6               ; {}
8138: A5 3A           LDA     $3A                 
813A: 29 F0           AND     #$F0                
813C: D0 F6           BNE     $8134               ; {}
813E: A5 3B           LDA     $3B                 
8140: 29 0F           AND     #$0F                
8142: C9 08           CMP     #$08                
8144: B0 1F           BCS     $8165               ; {}
8146: 0A              ASL     A                   
8147: A8              TAY                         
8148: B9 55 81        LDA     $8155,Y             ; {}
814B: 85 10           STA     $10                 
814D: B9 56 81        LDA     $8156,Y             ; {}
8150: 85 11           STA     $11                 
8152: 6C 10 00        JMP     ($0010)             
8155: 68              PLA                         
8156: 81 68           STA     ($68,X)             
8158: 81 B3           STA     ($B3,X)             
815A: 86 2E           STX     $2E                 
815C: 8A              TXA                         
815D: 14 ; ????
815E: 8B ; ????
815F: AD 8E 9B        LDA     $9B8E               ; {}
8162: 90 FA           BCC     $815E               ; {}
8164: 90 4C           BCC     $81B2               ; {}
8166: 4E 91 A5        LSR     $A591               ; {}
8169: 3A ; ????
816A: 0A              ASL     A                   
816B: A8              TAY                         
816C: B9 79 81        LDA     $8179,Y             ; {}
816F: 85 10           STA     $10                 
8171: B9 7A 81        LDA     $817A,Y             ; {}
8174: 85 11           STA     $11                 
8176: 6C 10 00        JMP     ($0010)             
8179: D5 81           CMP     $81,X               
817B: D5 81           CMP     $81,X               
817D: D6 81           DEC     $81,X               
817F: D5 81           CMP     $81,X               
8181: D5 81           CMP     $81,X               
8183: 6C 82 D5        JMP     ($D582)             
8186: 81 D5           STA     ($D5,X)             
8188: 81 D5           STA     ($D5,X)             
818A: 81 D5           STA     ($D5,X)             
818C: 81 D5           STA     ($D5,X)             
818E: 81 12           STA     ($12,X)             
8190: 82 ; ????
8191: 20 F0 EE        JSR     $EEF0               
8194: E6 3A           INC     $3A                 
8196: A5 FE           LDA     $FE                 
8198: 8D DD 04        STA     $04DD               
819B: A5 1B           LDA     $1B                 
819D: 8D DC 04        STA     $04DC               
81A0: A5 1A           LDA     $1A                 
81A2: 8D DA 04        STA     $04DA               
81A5: A5 FD           LDA     $FD                 
81A7: 8D DB 04        STA     $04DB               
81AA: AD 20 07        LDA     $0720               
81AD: 8D DE 04        STA     $04DE               
81B0: AD 23 07        LDA     $0723               
81B3: 8D DF 04        STA     $04DF               
81B6: 20 CA EE        JSR     $EECA               
81B9: A9 7F           LDA     #$7F                
81BB: 48              PHA                         
81BC: A9 26           LDA     #$26                
81BE: 48              PHA                         
81BF: 20 F7 CA        JSR     $CAF7               
81C2: A9 80           LDA     #$80                
81C4: 9D 01 07        STA     $0701,X             
81C7: A9 99           LDA     #$99                
81C9: 9D 00 07        STA     $0700,X             
81CC: A9 C8           LDA     #$C8                
81CE: 9D 03 07        STA     $0703,X             
81D1: A9 FF           LDA     #$FF                
81D3: 85 1C           STA     $1C                 
81D5: 60              RTS                         
81D6: 20 91 81        JSR     $8191               ; {}
81D9: E6 3A           INC     $3A                 
81DB: E6 3A           INC     $3A                 
81DD: 20 EE 81        JSR     $81EE               ; {}
81E0: 68              PLA                         
81E1: 68              PLA                         
81E2: 68              PLA                         
81E3: 68              PLA                         
81E4: 68              PLA                         
81E5: A9 7F           LDA     #$7F                
81E7: 48              PHA                         
81E8: A9 23           LDA     #$23                
81EA: 48              PHA                         
81EB: 4C 49 CB        JMP     $CB49               
81EE: A5 3B           LDA     $3B                 
81F0: 29 0F           AND     #$0F                
81F2: C9 0A           CMP     #$0A                
81F4: 90 02           BCC     $81F8               ; {}
81F6: A9 08           LDA     #$08                
81F8: A8              TAY                         
81F9: B9 08 82        LDA     $8208,Y             ; {}
81FC: 8D D1 04        STA     $04D1               
81FF: 20 BC 82        JSR     $82BC               ; {}
8202: A9 00           LDA     #$00                
8204: 8D 24 07        STA     $0724               
8207: 60              RTS                         
8208: 00              BRK                         
8209: 00              BRK                         
820A: 02 ; ????
820B: 04 ; ????
820C: 06 08           ASL     $08                 
820E: 0A              ASL     A                   
820F: 0C ; ????
8210: 0E 10 20        ASL     $2010               
8213: F0 EE           BEQ     $8203               ; {}
8215: 20 43 95        JSR     $9543               ; {}
8218: 20 CA EE        JSR     $EECA               
821B: A9 7F           LDA     #$7F                
821D: 48              PHA                         
821E: A9 29           LDA     #$29                
8220: 48              PHA                         
8221: 20 F7 CA        JSR     $CAF7               
8224: A9 00           LDA     #$00                
8226: 85 3A           STA     $3A                 
8228: 85 37           STA     $37                 
822A: AD DB 04        LDA     $04DB               
822D: 85 FD           STA     $FD                 
822F: AD DA 04        LDA     $04DA               
8232: 85 1A           STA     $1A                 
8234: AD DD 04        LDA     $04DD               
8237: 85 FE           STA     $FE                 
8239: AD DC 04        LDA     $04DC               
823C: 85 1B           STA     $1B                 
823E: AD DF 04        LDA     $04DF               
8241: 8D 23 07        STA     $0723               
8244: AD DE 04        LDA     $04DE               
8247: 8D 20 07        STA     $0720               
824A: 20 99 82        JSR     $8299               ; {}
824D: 20 33 83        JSR     $8333               ; {}
8250: A9 7F           LDA     #$7F                
8252: 48              PHA                         
8253: A9 20           LDA     #$20                
8255: 48              PHA                         
8256: 20 F7 CA        JSR     $CAF7               
8259: A9 7F           LDA     #$7F                
825B: 48              PHA                         
825C: A9 17           LDA     #$17                
825E: 48              PHA                         
825F: 20 F7 CA        JSR     $CAF7               
8262: A9 00           LDA     #$00                
8264: 85 5C           STA     $5C                 
8266: 20 70 CB        JSR     $CB70               
8269: 4C E0 81        JMP     $81E0               ; {}
826C: 20 F0 EE        JSR     $EEF0               
826F: E6 3A           INC     $3A                 
8271: A9 00           LDA     #$00                
8273: 8D 24 07        STA     $0724               
8276: 20 70 CB        JSR     $CB70               
8279: AD 2F 01        LDA     $012F               
827C: 4A              LSR     A                   
827D: B0 0D           BCS     $828C               ; {}
827F: A9 FE           LDA     #$FE                
8281: 85 1A           STA     $1A                 
8283: A9 00           LDA     #$00                
8285: 85 FE           STA     $FE                 
8287: 85 1B           STA     $1B                 
8289: 4C E0 81        JMP     $81E0               ; {}
828C: A9 02           LDA     #$02                
828E: 85 1B           STA     $1B                 
8290: A9 00           LDA     #$00                
8292: 85 FD           STA     $FD                 
8294: 85 1A           STA     $1A                 
8296: 4C E0 81        JMP     $81E0               ; {}
8299: AD 2F 01        LDA     $012F               
829C: 4A              LSR     A                   
829D: B0 0A           BCS     $82A9               ; {}
829F: E6 1A           INC     $1A                 
82A1: 20 B0 82        JSR     $82B0               ; {}
82A4: C6 1A           DEC     $1A                 
82A6: 4C B0 82        JMP     $82B0               ; {}
82A9: C6 1B           DEC     $1B                 
82AB: 20 B0 82        JSR     $82B0               ; {}
82AE: E6 1B           INC     $1B                 
82B0: A9 7F           LDA     #$7F                
82B2: 48              PHA                         
82B3: A9 2C           LDA     #$2C                
82B5: 48              PHA                         
82B6: 20 F7 CA        JSR     $CAF7               
82B9: 60              RTS                         
82BA: A9 00           LDA     #$00                
82BC: 20 F5 82        JSR     $82F5               ; {}
82BF: 20 4E CB        JSR     $CB4E               
82C2: AD 2F 01        LDA     $012F               
82C5: 4A              LSR     A                   
82C6: B0 09           BCS     $82D1               ; {}
82C8: 20 25 83        JSR     $8325               ; {}
82CB: C9 FE           CMP     #$FE                
82CD: B0 F0           BCS     $82BF               ; {}
82CF: 90 45           BCC     $8316               ; {}
82D1: A5 FE           LDA     $FE                 
82D3: 18              CLC                         
82D4: 69 10           ADC     #$10                
82D6: 85 FE           STA     $FE                 
82D8: A5 1B           LDA     $1B                 
82DA: 69 00           ADC     #$00                
82DC: 85 1B           STA     $1B                 
82DE: C9 03           CMP     #$03                
82E0: 90 DD           BCC     $82BF               ; {}
82E2: A9 01           LDA     #$01                
82E4: 85 1B           STA     $1B                 
82E6: A9 00           LDA     #$00                
82E8: 85 FE           STA     $FE                 
82EA: 60              RTS                         
82EB: A9 7F           LDA     #$7F                
82ED: 48              PHA                         
82EE: A9 2F           LDA     #$2F                
82F0: 48              PHA                         
82F1: 20 F7 CA        JSR     $CAF7               
82F4: 60              RTS                         
82F5: 8D D1 04        STA     $04D1               
82F8: 48              PHA                         
82F9: A9 00           LDA     #$00                
82FB: 8D D2 04        STA     $04D2               
82FE: 20 EB 82        JSR     $82EB               ; {}
8301: A9 00           LDA     #$00                
8303: 8D D2 04        STA     $04D2               
8306: 68              PLA                         
8307: 18              CLC                         
8308: 69 01           ADC     #$01                
830A: 8D D1 04        STA     $04D1               
830D: 20 EB 82        JSR     $82EB               ; {}
8310: AD 2F 01        LDA     $012F               
8313: 4A              LSR     A                   
8314: B0 CC           BCS     $82E2               ; {}
8316: A9 FF           LDA     #$FF                
8318: 85 1A           STA     $1A                 
831A: A9 EE           LDA     #$EE                
831C: 85 FD           STA     $FD                 
831E: 60              RTS                         
831F: 20 C6 98        JSR     $98C6               ; {}
8322: 20 4E CB        JSR     $CB4E               
8325: A5 FD           LDA     $FD                 
8327: 38              SEC                         
8328: E9 10           SBC     #$10                
832A: 85 FD           STA     $FD                 
832C: A5 1A           LDA     $1A                 
832E: E9 00           SBC     #$00                
8330: 85 1A           STA     $1A                 
8332: 60              RTS                         
8333: A0 00           LDY     #$00                
8335: B9 00 05        LDA     $0500,Y             
8338: C5 3B           CMP     $3B                 
833A: D0 0A           BNE     $8346               ; {}
833C: A9 52           LDA     #$52                
833E: 99 00 05        STA     $0500,Y             
8341: A9 51           LDA     #$51                
8343: 99 F0 04        STA     $04F0,Y             
8346: C8              INY                         
8347: C0 F0           CPY     #$F0                
8349: 90 EA           BCC     $8335               ; {}
834B: A0 00           LDY     #$00                
834D: B9 F0 05        LDA     $05F0,Y             
8350: C5 3B           CMP     $3B                 
8352: D0 0A           BNE     $835E               ; {}
8354: A9 52           LDA     #$52                
8356: 99 F0 05        STA     $05F0,Y             
8359: A9 51           LDA     #$51                
835B: 99 E0 05        STA     $05E0,Y             
835E: C8              INY                         
835F: D0 EC           BNE     $834D               ; {}
8361: 60              RTS                         
8362: A2 60           LDX     #$60                
8364: A0 00           LDY     #$00                
8366: 20 90 83        JSR     $8390               ; {}
8369: A2 70           LDX     #$70                
836B: C8              INY                         
836C: 20 90 83        JSR     $8390               ; {}
836F: A2 80           LDX     #$80                
8371: C8              INY                         
8372: 20 90 83        JSR     $8390               ; {}
8375: A2 90           LDX     #$90                
8377: C8              INY                         
8378: 20 90 83        JSR     $8390               ; {}
837B: A2 A0           LDX     #$A0                
837D: C8              INY                         
837E: 20 90 83        JSR     $8390               ; {}
8381: A2 B0           LDX     #$B0                
8383: C8              INY                         
8384: 20 90 83        JSR     $8390               ; {}
8387: A2 C0           LDX     #$C0                
8389: C8              INY                         
838A: 20 90 83        JSR     $8390               ; {}
838D: A2 D0           LDX     #$D0                
838F: C8              INY                         
8390: 98              TYA                         
8391: 48              PHA                         
8392: 85 00           STA     $00                 ; {ram.GP_00}
8394: 18              CLC                         
8395: 65 26           ADC     $26                 
8397: 29 07           AND     #$07                
8399: 09 80           ORA     #$80                
839B: 9D 01 07        STA     $0701,X             
839E: A9 C0           LDA     #$C0                
83A0: 9D 02 07        STA     $0702,X             
83A3: AD 2F 01        LDA     $012F               
83A6: 0A              ASL     A                   
83A7: 0A              ASL     A                   
83A8: 0A              ASL     A                   
83A9: 18              CLC                         
83AA: 65 00           ADC     $00                 ; {ram.GP_00}
83AC: A8              TAY                         
83AD: B9 C7 83        LDA     $83C7,Y             ; {}
83B0: 48              PHA                         
83B1: 29 F0           AND     #$F0                
83B3: 18              CLC                         
83B4: 69 09           ADC     #$09                
83B6: 9D 00 07        STA     $0700,X             
83B9: 68              PLA                         
83BA: 0A              ASL     A                   
83BB: 0A              ASL     A                   
83BC: 0A              ASL     A                   
83BD: 0A              ASL     A                   
83BE: 18              CLC                         
83BF: 69 05           ADC     #$05                
83C1: 9D 03 07        STA     $0703,X             
83C4: 68              PLA                         
83C5: A8              TAY                         
83C6: 60              RTS                         
83C7: 31 61           AND     ($61),Y             
83C9: 91 C1           STA     ($C1),Y             
83CB: 3E 6E 97        ROL     $976E,X             ; {}
83CE: CD 3E 6E        CMP     $6E3E               
83D1: B1 BC           LDA     ($BC),Y             
83D3: 81 88           STA     ($88,X)             
83D5: 21 51           AND     ($51,X)             
83D7: A2 60           LDX     #$60                
83D9: 20 23 84        JSR     $8423               ; {}
83DC: A2 70           LDX     #$70                
83DE: 20 23 84        JSR     $8423               ; {}
83E1: A2 80           LDX     #$80                
83E3: 20 23 84        JSR     $8423               ; {}
83E6: A2 90           LDX     #$90                
83E8: 20 23 84        JSR     $8423               ; {}
83EB: A2 A0           LDX     #$A0                
83ED: 20 23 84        JSR     $8423               ; {}
83F0: A2 B0           LDX     #$B0                
83F2: 20 23 84        JSR     $8423               ; {}
83F5: A2 C0           LDX     #$C0                
83F7: 20 23 84        JSR     $8423               ; {}
83FA: A2 D0           LDX     #$D0                
83FC: 20 23 84        JSR     $8423               ; {}
83FF: AD 62 07        LDA     $0762               
8402: 0D 72 07        ORA     $0772               
8405: 0D 82 07        ORA     $0782               
8408: 0D 92 07        ORA     $0792               
840B: 0D A2 07        ORA     $07A2               
840E: 0D B2 07        ORA     $07B2               
8411: 0D C2 07        ORA     $07C2               
8414: 0D D2 07        ORA     $07D2               
8417: D0 09           BNE     $8422               ; {}
8419: A9 80           LDA     #$80                
841B: 8D 24 07        STA     $0724               
841E: E6 3A           INC     $3A                 
8420: E6 3A           INC     $3A                 
8422: 60              RTS                         
8423: A9 0E           LDA     #$0E                
8425: 20 32 99        JSR     $9932               ; {}
8428: BD 01 07        LDA     $0701,X             
842B: 30 03           BMI     $8430               ; {}
842D: 4C D4 84        JMP     $84D4               ; {}
8430: A0 38           LDY     #$38                
8432: 20 86 D9        JSR     $D986               
8435: 90 07           BCC     $843E               ; {}
8437: A0 3C           LDY     #$3C                
8439: 20 86 D9        JSR     $D986               
843C: B0 E4           BCS     $8422               ; {}
843E: A9 F8           LDA     #$F8                
8440: 99 00 07        STA     $0700,Y             
8443: 99 00 02        STA     $0200,Y             
8446: AD 4B 01        LDA     $014B               
8449: D0 07           BNE     $8452               ; {}
844B: AD 4A 01        LDA     $014A               
844E: C9 05           CMP     #$05                
8450: 90 D0           BCC     $8422               ; {}
8452: 20 6D 84        JSR     $846D               ; {}
8455: A9 05           LDA     #$05                
8457: 20 52 DE        JSR     $DE52               
845A: BD 01 07        LDA     $0701,X             
845D: 29 7F           AND     #$7F                
845F: 9D 01 07        STA     $0701,X             
8462: A9 C0           LDA     #$C0                
8464: 9D 02 07        STA     $0702,X             
8467: A9 80           LDA     #$80                
8469: 8D 80 03        STA     $0380               
846C: 60              RTS                         
846D: A9 00           LDA     #$00                
846F: 85 00           STA     $00                 ; {ram.GP_00}
8471: A0 70           LDY     #$70                
8473: B9 61 07        LDA     $0761,Y             
8476: 30 02           BMI     $847A               ; {}
8478: E6 00           INC     $00                 ; {ram.GP_00}
847A: 98              TYA                         
847B: 38              SEC                         
847C: E9 10           SBC     #$10                
847E: A8              TAY                         
847F: 10 F2           BPL     $8473               ; {}
8481: A5 00           LDA     $00                 ; {ram.GP_00}
8483: C9 07           CMP     #$07                
8485: 90 23           BCC     $84AA               ; {}
8487: BD 01 07        LDA     $0701,X             
848A: 29 F0           AND     #$F0                
848C: 85 00           STA     $00                 ; {ram.GP_00}
848E: AD 4E 01        LDA     $014E               
8491: D0 18           BNE     $84AB               ; {}
8493: AD 51 01        LDA     $0151               
8496: 29 C0           AND     #$C0                
8498: D0 2E           BNE     $84C8               ; {}
849A: A5 EF           LDA     $EF                 
849C: 29 03           AND     #$03                
849E: 05 00           ORA     $00                 ; {ram.GP_00}
84A0: 09 08           ORA     #$08                
84A2: 9D 01 07        STA     $0701,X             
84A5: A9 80           LDA     #$80                
84A7: 8D 83 03        STA     $0383               
84AA: 60              RTS                         
84AB: AD 51 01        LDA     $0151               
84AE: 29 C0           AND     #$C0                
84B0: F0 0A           BEQ     $84BC               ; {}
84B2: A5 EF           LDA     $EF                 
84B4: 29 01           AND     #$01                
84B6: 09 08           ORA     #$08                
84B8: 05 00           ORA     $00                 ; {ram.GP_00}
84BA: D0 E6           BNE     $84A2               ; {}
84BC: A5 EF           LDA     $EF                 
84BE: 29 03           AND     #$03                
84C0: C9 03           CMP     #$03                
84C2: 90 F2           BCC     $84B6               ; {}
84C4: A9 00           LDA     #$00                
84C6: F0 EE           BEQ     $84B6               ; {}
84C8: A5 EF           LDA     $EF                 
84CA: 29 03           AND     #$03                
84CC: C9 02           CMP     #$02                
84CE: D0 E6           BNE     $84B6               ; {}
84D0: A9 01           LDA     #$01                
84D2: D0 E2           BNE     $84B6               ; {}
84D4: BD 02 07        LDA     $0702,X             
84D7: F0 2D           BEQ     $8506               ; {}
84D9: C9 01           CMP     #$01                
84DB: D0 03           BNE     $84E0               ; {}
84DD: 4C 7B 85        JMP     $857B               ; {}
84E0: DE 02 07        DEC     $0702,X             
84E3: C9 A8           CMP     #$A8                
84E5: 90 2E           BCC     $8515               ; {}
84E7: C9 B0           CMP     #$B0                
84E9: 90 13           BCC     $84FE               ; {}
84EB: C9 B8           CMP     #$B8                
84ED: 90 13           BCC     $8502               ; {}
84EF: A9 4A           LDA     #$4A                
84F1: 9D 01 02        STA     $0201,X             
84F4: 9D 05 02        STA     $0205,X             
84F7: 9D 09 02        STA     $0209,X             
84FA: 9D 0D 02        STA     $020D,X             
84FD: 60              RTS                         
84FE: A9 4B           LDA     #$4B                
8500: D0 EF           BNE     $84F1               ; {}
8502: A9 5A           LDA     #$5A                
8504: D0 EB           BNE     $84F1               ; {}
8506: A9 F8           LDA     #$F8                
8508: 9D 00 02        STA     $0200,X             
850B: 9D 04 02        STA     $0204,X             
850E: 9D 08 02        STA     $0208,X             
8511: 9D 0C 02        STA     $020C,X             
8514: 60              RTS                         
8515: A9 01           LDA     #$01                
8517: 9D 02 07        STA     $0702,X             
851A: BD 01 07        LDA     $0701,X             
851D: 29 0F           AND     #$0F                
851F: C9 04           CMP     #$04                
8521: F0 48           BEQ     $856B               ; {}
8523: BD 01 07        LDA     $0701,X             
8526: 29 0F           AND     #$0F                
8528: 0A              ASL     A                   
8529: 0A              ASL     A                   
852A: A8              TAY                         
852B: B9 4E 86        LDA     $864E,Y             ; {}
852E: 9D 02 02        STA     $0202,X             
8531: B9 4F 86        LDA     $864F,Y             ; {}
8534: 9D 06 02        STA     $0206,X             
8537: B9 50 86        LDA     $8650,Y             ; {}
853A: 9D 0A 02        STA     $020A,X             
853D: B9 51 86        LDA     $8651,Y             ; {}
8540: 9D 0E 02        STA     $020E,X             
8543: B9 1E 86        LDA     $861E,Y             ; {}
8546: 9D 01 02        STA     $0201,X             
8549: B9 1F 86        LDA     $861F,Y             ; {}
854C: 9D 05 02        STA     $0205,X             
854F: B9 20 86        LDA     $8620,Y             ; {}
8552: 9D 09 02        STA     $0209,X             
8555: B9 21 86        LDA     $8621,Y             ; {}
8558: 9D 0D 02        STA     $020D,X             
855B: BD 01 07        LDA     $0701,X             
855E: 29 0F           AND     #$0F                
8560: C9 04           CMP     #$04                
8562: B0 16           BCS     $857A               ; {}
8564: FE 03 02        INC     $0203,X             
8567: FE 0B 02        INC     $020B,X             
856A: 60              RTS                         
856B: 20 23 85        JSR     $8523               ; {}
856E: A9 FF           LDA     #$FF                
8570: 8D 24 07        STA     $0724               
8573: E6 3A           INC     $3A                 
8575: A9 80           LDA     #$80                
8577: 8D 85 03        STA     $0385               
857A: 60              RTS                         
857B: 20 23 85        JSR     $8523               ; {}
857E: A0 20           LDY     #$20                
8580: 20 86 D9        JSR     $D986               
8583: B0 49           BCS     $85CE               ; {}
8585: A9 C0           LDA     #$C0                
8587: 8D 24 07        STA     $0724               
858A: A9 10           LDA     #$10                
858C: 8D 81 03        STA     $0381               
858F: 20 07 86        JSR     $8607               ; {}
8592: 20 A5 85        JSR     $85A5               ; {}
8595: BD 01 07        LDA     $0701,X             
8598: 29 0F           AND     #$0F                
859A: C9 08           CMP     #$08                
859C: B0 1C           BCS     $85BA               ; {}
859E: C9 04           CMP     #$04                
85A0: 90 13           BCC     $85B5               ; {}
85A2: 4C C6 EA        JMP     $EAC6               
85A5: BD 00 07        LDA     $0700,X             
85A8: 29 0F           AND     #$0F                
85AA: 9D 00 07        STA     $0700,X             
85AD: A9 00           LDA     #$00                
85AF: 9D 02 07        STA     $0702,X             
85B2: 4C 06 85        JMP     $8506               ; {}
85B5: A9 05           LDA     #$05                
85B7: 4C CC DD        JMP     $DDCC               
85BA: C9 08           CMP     #$08                
85BC: F0 1C           BEQ     $85DA               ; {}
85BE: C9 09           CMP     #$09                
85C0: F0 0D           BEQ     $85CF               ; {}
85C2: C9 0A           CMP     #$0A                
85C4: F0 30           BEQ     $85F6               ; {}
85C6: AD 4E 01        LDA     $014E               
85C9: D0 03           BNE     $85CE               ; {}
85CB: EE 4E 01        INC     $014E               
85CE: 60              RTS                         
85CF: AD 50 01        LDA     $0150               
85D2: C9 63           CMP     #$63                
85D4: B0 F8           BCS     $85CE               ; {}
85D6: EE 50 01        INC     $0150               
85D9: 60              RTS                         
85DA: AD 51 01        LDA     $0151               
85DD: 29 C0           AND     #$C0                
85DF: D0 11           BNE     $85F2               ; {}
85E1: A9 01           LDA     #$01                
85E3: 85 00           STA     $00                 ; {ram.GP_00}
85E5: AD 51 01        LDA     $0151               
85E8: 29 3F           AND     #$3F                
85EA: C5 00           CMP     $00                 ; {ram.GP_00}
85EC: B0 03           BCS     $85F1               ; {}
85EE: EE 51 01        INC     $0151               
85F1: 60              RTS                         
85F2: A9 08           LDA     #$08                
85F4: D0 ED           BNE     $85E3               ; {}
85F6: AD 51 01        LDA     $0151               
85F9: 29 C0           AND     #$C0                
85FB: D0 D1           BNE     $85CE               ; {}
85FD: AD 51 01        LDA     $0151               
8600: 18              CLC                         
8601: 69 40           ADC     #$40                
8603: 8D 51 01        STA     $0151               
8606: 60              RTS                         
8607: A0 70           LDY     #$70                
8609: B9 61 07        LDA     $0761,Y             
860C: 10 08           BPL     $8616               ; {}
860E: A9 00           LDA     #$00                
8610: 99 61 07        STA     $0761,Y             
8613: 99 62 07        STA     $0762,Y             
8616: 98              TYA                         
8617: 38              SEC                         
8618: E9 10           SBC     #$10                
861A: A8              TAY                         
861B: 10 EC           BPL     $8609               ; {}
861D: 60              RTS                         
861E: 92 ; ????
861F: 94 93           STY     $93,X               
8621: 93 ; ????
8622: 92 ; ????
8623: 94 93           STY     $93,X               
8625: 93 ; ????
8626: 92 ; ????
8627: 94 93           STY     $93,X               
8629: 93 ; ????
862A: 92 ; ????
862B: 94 93           STY     $93,X               
862D: 93 ; ????
862E: 43 ; ????
862F: 5F ; ????
8630: 44 ; ????
8631: 5F ; ????
8632: AA              TAX                         
8633: 5F ; ????
8634: AB ; ????
8635: 5F ; ????
8636: AA              TAX                         
8637: 5F ; ????
8638: AB ; ????
8639: 5F ; ????
863A: AA              TAX                         
863B: 5F ; ????
863C: AB ; ????
863D: 5F ; ????
863E: 49 5F           EOR     #$5F                
8640: 59 5F 9F        EOR     $9F5F,Y             ; {}
8643: 5F ; ????
8644: AF ; ????
8645: 5F ; ????
8646: 50 50           BVC     $8698               ; {}
8648: 51 51           EOR     ($51),Y             
864A: 32 ; ????
864B: 5F ; ????
864C: 33 ; ????
864D: 5F ; ????
864E: 01 01           ORA     ($01,X)             
8650: 01 41           ORA     ($41,X)             
8652: 01 01           ORA     ($01,X)             
8654: 01 41           ORA     ($41,X)             
8656: 01 01           ORA     ($01,X)             
8658: 01 41           ORA     ($41,X)             
865A: 01 01           ORA     ($01,X)             
865C: 01 41           ORA     ($41,X)             
865E: 01 01           ORA     ($01,X)             
8660: 01 01           ORA     ($01,X)             
8662: 01 01           ORA     ($01,X)             
8664: 01 01           ORA     ($01,X)             
8666: 01 01           ORA     ($01,X)             
8668: 01 01           ORA     ($01,X)             
866A: 01 01           ORA     ($01,X)             
866C: 01 01           ORA     ($01,X)             
866E: 01 01           ORA     ($01,X)             
8670: 01 01           ORA     ($01,X)             
8672: 00              BRK                         
8673: 00              BRK                         
8674: 00              BRK                         
8675: 00              BRK                         
8676: 00              BRK                         
8677: 40              RTI                         
8678: 00              BRK                         
8679: 40              RTI                         
867A: 01 01           ORA     ($01,X)             
867C: 01 01           ORA     ($01,X)             
867E: A5 3A           LDA     $3A                 
8680: 20 2B EE        JSR     $EE2B               
8683: 90 80           BCC     $8605               ; {}
8685: F7 ; ????
8686: E0 6F           CPX     #$6F                
8688: 80 ; ????
8689: 83 ; ????
868A: 91 8E           STA     ($8E),Y             
868C: 80 ; ????
868D: 6F ; ????
868E: 80 ; ????
868F: 99 86 3B        STA     $3B86,Y             
8692: E1 A5           SBC     ($A5,X)             
8694: 86 23           STX     $23                 
8696: 81 6F           STA     ($6F,X)             
8698: 80 ; ????
8699: 20 9D 80        JSR     $809D               ; {}
869C: 20 DA 86        JSR     $86DA               ; {}
869F: A9 00           LDA     #$00                
86A1: 8D 28 07        STA     $0728               
86A4: 60              RTS                         
86A5: 20 B2 80        JSR     $80B2               ; {}
86A8: F0 06           BEQ     $86B0               ; {}
86AA: 20 F0 90        JSR     $90F0               ; {}
86AD: 4C E3 86        JMP     $86E3               ; {}
86B0: 4C FD 88        JMP     $88FD               ; {}
86B3: A5 3A           LDA     $3A                 
86B5: 0A              ASL     A                   
86B6: A8              TAY                         
86B7: B9 C4 86        LDA     $86C4,Y             ; {}
86BA: 85 10           STA     $10                 
86BC: B9 C5 86        LDA     $86C5,Y             ; {}
86BF: 85 11           STA     $11                 
86C1: 6C 10 00        JMP     ($0010)             
86C4: D5 81           CMP     $81,X               
86C6: D5 81           CMP     $81,X               
86C8: D6 81           DEC     $81,X               
86CA: D5 81           CMP     $81,X               
86CC: D5 81           CMP     $81,X               
86CE: 6C 82 D5        JMP     ($D582)             
86D1: 81 D5           STA     ($D5,X)             
86D3: 81 D5           STA     ($D5,X)             
86D5: 81 D5           STA     ($D5,X)             
86D7: 81 12           STA     ($12,X)             
86D9: 82 ; ????
86DA: A2 60           LDX     #$60                
86DC: A9 68           LDA     #$68                
86DE: 85 00           STA     $00                 ; {ram.GP_00}
86E0: 4C E5 87        JMP     $87E5               ; {}
86E3: A2 60           LDX     #$60                
86E5: 20 08 87        JSR     $8708               ; {}
86E8: A2 70           LDX     #$70                
86EA: 20 08 87        JSR     $8708               ; {}
86ED: A2 80           LDX     #$80                
86EF: 20 08 87        JSR     $8708               ; {}
86F2: A2 90           LDX     #$90                
86F4: 20 08 87        JSR     $8708               ; {}
86F7: A2 A0           LDX     #$A0                
86F9: 20 08 87        JSR     $8708               ; {}
86FC: A2 B0           LDX     #$B0                
86FE: 20 08 87        JSR     $8708               ; {}
8701: A2 C0           LDX     #$C0                
8703: 20 08 87        JSR     $8708               ; {}
8706: A2 D0           LDX     #$D0                
8708: BD 01 07        LDA     $0701,X             
870B: F0 39           BEQ     $8746               ; {}
870D: BD 01 07        LDA     $0701,X             
8710: 29 07           AND     #$07                
8712: 20 2B EE        JSR     $EE2B               
8715: 00              BRK                         
8716: 89 ; ????
8717: A7 ; ????
8718: 88              DEY                         
8719: 1D 87 87        ORA     $8787,X             ; {}
871C: 87 ; ????
871D: 20 90 D9        JSR     $D990               
8720: 90 12           BCC     $8734               ; {}
8722: A9 DA           LDA     #$DA                
8724: 48              PHA                         
8725: A9 08           LDA     #$08                
8727: 48              PHA                         
8728: 20 F7 CA        JSR     $CAF7               
872B: 20 62 87        JSR     $8762               ; {}
872E: 20 C0 DB        JSR     $DBC0               
8731: 4C 55 87        JMP     $8755               ; {}
8734: A9 F8           LDA     #$F8                
8736: 99 00 07        STA     $0700,Y             
8739: FE 01 07        INC     $0701,X             
873C: A9 FF           LDA     #$FF                
873E: 9D 02 07        STA     $0702,X             
8741: A9 08           LDA     #$08                
8743: 8D 81 03        STA     $0381               
8746: 60              RTS                         
8747: A5 3A           LDA     $3A                 
8749: 29 F0           AND     #$F0                
874B: 09 09           ORA     #$09                
874D: 85 3A           STA     $3A                 
874F: A9 80           LDA     #$80                
8751: 8D 24 07        STA     $0724               
8754: 60              RTS                         
8755: A0 40           LDY     #$40                
8757: A5 14           LDA     $14                 
8759: 29 08           AND     #$08                
875B: D0 01           BNE     $875E               ; {}
875D: C8              INY                         
875E: 98              TYA                         
875F: 4C 24 99        JMP     $9924               ; {}
8762: BD 02 07        LDA     $0702,X             
8765: 29 0F           AND     #$0F                
8767: C9 08           CMP     #$08                
8769: B0 0F           BCS     $877A               ; {}
876B: A9 D0           LDA     #$D0                
876D: 85 08           STA     $08                 
876F: A9 30           LDA     #$30                
8771: 85 09           STA     $09                 
8773: A9 C0           LDA     #$C0                
8775: 85 0A           STA     $0A                 
8777: 4C 6D C7        JMP     $C76D               
877A: A9 30           LDA     #$30                
877C: 85 08           STA     $08                 
877E: 85 09           STA     $09                 
8780: A9 C0           LDA     #$C0                
8782: 85 0A           STA     $0A                 
8784: 4C 8D C7        JMP     $C78D               
8787: A9 DD           LDA     #$DD                
8789: 48              PHA                         
878A: A9 64           LDA     #$64                
878C: 48              PHA                         
878D: 20 F7 CA        JSR     $CAF7               
8790: 60              RTS                         
8791: A5 3A           LDA     $3A                 
8793: 20 2B EE        JSR     $EE2B               
8796: 90 80           BCC     $8718               ; {}
8798: F7 ; ????
8799: E0 6F           CPX     #$6F                
879B: 80 ; ????
879C: 83 ; ????
879D: 91 8E           STA     ($8E),Y             
879F: 80 ; ????
87A0: 6F ; ????
87A1: 80 ; ????
87A2: B2 ; ????
87A3: 87 ; ????
87A4: 3B ; ????
87A5: E1 14           SBC     ($14,X)             
87A7: 89 ; ????
87A8: BE 87 41        LDX     $4187,Y             
87AB: 89 ; ????
87AC: 8B ; ????
87AD: 89 ; ????
87AE: 23 ; ????
87AF: 81 6F           STA     ($6F,X)             
87B1: 80 ; ????
87B2: 20 9D 80        JSR     $809D               ; {}
87B5: 20 DF 87        JSR     $87DF               ; {}
87B8: A9 00           LDA     #$00                
87BA: 8D 28 07        STA     $0728               
87BD: 60              RTS                         
87BE: 20 B2 80        JSR     $80B2               ; {}
87C1: F0 06           BEQ     $87C9               ; {}
87C3: 20 F0 90        JSR     $90F0               ; {}
87C6: 4C 64 88        JMP     $8864               ; {}
87C9: E6 3A           INC     $3A                 
87CB: A9 00           LDA     #$00                
87CD: 8D 24 07        STA     $0724               
87D0: 60              RTS                         
87D1: 85 00           STA     $00                 ; {ram.GP_00}
87D3: A5 3A           LDA     $3A                 
87D5: 29 F0           AND     #$F0                
87D7: 05 00           ORA     $00                 ; {ram.GP_00}
87D9: 85 3A           STA     $3A                 
87DB: A9 80           LDA     #$80                
87DD: D0 EE           BNE     $87CD               ; {}
87DF: A2 60           LDX     #$60                
87E1: A9 08           LDA     #$08                
87E3: 85 00           STA     $00                 ; {ram.GP_00}
87E5: 20 C6 98        JSR     $98C6               ; {}
87E8: A5 00           LDA     $00                 ; {ram.GP_00}
87EA: 9D 01 07        STA     $0701,X             
87ED: A9 7F           LDA     #$7F                
87EF: 48              PHA                         
87F0: A9 3E           LDA     #$3E                
87F2: 48              PHA                         
87F3: 20 F7 CA        JSR     $CAF7               
87F6: 8A              TXA                         
87F7: 18              CLC                         
87F8: 69 10           ADC     #$10                
87FA: AA              TAX                         
87FB: E0 E0           CPX     #$E0                
87FD: 90 E6           BCC     $87E5               ; {}
87FF: 60              RTS                         
8800: 20 C6 98        JSR     $98C6               ; {}
8803: 8A              TXA                         
8804: 38              SEC                         
8805: E9 60           SBC     #$60                
8807: 85 00           STA     $00                 ; {ram.GP_00}
8809: 4A              LSR     A                   
880A: 4A              LSR     A                   
880B: 4A              LSR     A                   
880C: 4A              LSR     A                   
880D: A8              TAY                         
880E: A5 14           LDA     $14                 
8810: 29 7F           AND     #$7F                
8812: C5 00           CMP     $00                 ; {ram.GP_00}
8814: D0 35           BNE     $884B               ; {}
8816: A9 00           LDA     #$00                
8818: 9D 06 07        STA     $0706,X             
881B: 9D 04 07        STA     $0704,X             
881E: 9D 05 07        STA     $0705,X             
8821: FE 01 07        INC     $0701,X             
8824: 98              TYA                         
8825: 0A              ASL     A                   
8826: A8              TAY                         
8827: A5 26           LDA     $26                 
8829: 29 3C           AND     #$3C                
882B: 4A              LSR     A                   
882C: 4A              LSR     A                   
882D: 79 54 88        ADC     $8854,Y             ; {}
8830: 9D 00 07        STA     $0700,X             
8833: A5 26           LDA     $26                 
8835: 4A              LSR     A                   
8836: 4A              LSR     A                   
8837: 4A              LSR     A                   
8838: 4A              LSR     A                   
8839: 18              CLC                         
883A: 79 55 88        ADC     $8855,Y             ; {}
883D: 9D 03 07        STA     $0703,X             
8840: A5 26           LDA     $26                 
8842: 29 07           AND     #$07                
8844: A8              TAY                         
8845: B9 4C 88        LDA     $884C,Y             ; {}
8848: 9D 02 07        STA     $0702,X             
884B: 60              RTS                         
884C: 46 66           LSR     $66                 
884E: 74 ; ????
884F: 70 7C           BVS     $88CD               ; {}
8851: 69 49           ADC     #$49                
8853: 09 78           ORA     #$78                
8855: 40              RTI                         
8856: 70 C0           BVS     $8818               ; {}
8858: 70 80           BVS     $87DA               ; {}
885A: 48              PHA                         
885B: D8              CLD                         
885C: 50 60           BVC     $88BE               ; {}
885E: 50 A0           BVC     $8800               ; {}
8860: 48              PHA                         
8861: 28              PLP                         
8862: 28              PLP                         
8863: 80 ; ????
8864: A5 14           LDA     $14                 
8866: 29 1F           AND     #$1F                
8868: D0 08           BNE     $8872               ; {}
886A: CE 26 07        DEC     $0726               
886D: D0 03           BNE     $8872               ; {}
886F: 4C C9 87        JMP     $87C9               ; {}
8872: A2 60           LDX     #$60                
8874: 20 97 88        JSR     $8897               ; {}
8877: A2 70           LDX     #$70                
8879: 20 97 88        JSR     $8897               ; {}
887C: A2 80           LDX     #$80                
887E: 20 97 88        JSR     $8897               ; {}
8881: A2 90           LDX     #$90                
8883: 20 97 88        JSR     $8897               ; {}
8886: A2 A0           LDX     #$A0                
8888: 20 97 88        JSR     $8897               ; {}
888B: A2 B0           LDX     #$B0                
888D: 20 97 88        JSR     $8897               ; {}
8890: A2 C0           LDX     #$C0                
8892: 20 97 88        JSR     $8897               ; {}
8895: A2 D0           LDX     #$D0                
8897: BD 01 07        LDA     $0701,X             
889A: 29 07           AND     #$07                
889C: 20 2B EE        JSR     $EE2B               
889F: 00              BRK                         
88A0: 89 ; ????
88A1: A7 ; ????
88A2: 88              DEY                         
88A3: CD 88 87        CMP     $8788               ; {}
88A6: 87 ; ????
88A7: 20 C6 98        JSR     $98C6               ; {}
88AA: FE 06 07        INC     $0706,X             
88AD: BD 06 07        LDA     $0706,X             
88B0: C9 08           CMP     #$08                
88B2: 90 0C           BCC     $88C0               ; {}
88B4: C9 10           CMP     #$10                
88B6: 90 0C           BCC     $88C4               ; {}
88B8: C9 18           CMP     #$18                
88BA: 90 0C           BCC     $88C8               ; {}
88BC: FE 01 07        INC     $0701,X             
88BF: 60              RTS                         
88C0: A9 30           LDA     #$30                
88C2: D0 06           BNE     $88CA               ; {}
88C4: A9 31           LDA     #$31                
88C6: D0 02           BNE     $88CA               ; {}
88C8: A9 32           LDA     #$32                
88CA: 4C 24 99        JMP     $9924               ; {}
88CD: 20 08 DD        JSR     $DD08               
88D0: 20 90 D9        JSR     $D990               
88D3: 90 12           BCC     $88E7               ; {}
88D5: A9 DA           LDA     #$DA                
88D7: 48              PHA                         
88D8: A9 08           LDA     #$08                
88DA: 48              PHA                         
88DB: 20 F7 CA        JSR     $CAF7               
88DE: 20 C0 DB        JSR     $DBC0               
88E1: 20 03 89        JSR     $8903               ; {}
88E4: 4C DE DC        JMP     $DCDE               
88E7: A9 F8           LDA     #$F8                
88E9: 99 00 07        STA     $0700,Y             
88EC: 20 A9 DC        JSR     $DCA9               
88EF: FE 01 07        INC     $0701,X             
88F2: A9 FF           LDA     #$FF                
88F4: 9D 02 07        STA     $0702,X             
88F7: A9 08           LDA     #$08                
88F9: 8D 81 03        STA     $0381               
88FC: 60              RTS                         
88FD: 4C C9 87        JMP     $87C9               ; {}
8900: 4C 00 88        JMP     $8800               ; {}
8903: 8A              TXA                         
8904: 4A              LSR     A                   
8905: 4A              LSR     A                   
8906: 4A              LSR     A                   
8907: 18              CLC                         
8908: 65 14           ADC     $14                 
890A: 29 0C           AND     #$0C                
890C: 4A              LSR     A                   
890D: 4A              LSR     A                   
890E: 18              CLC                         
890F: 69 10           ADC     #$10                
8911: 4C 32 99        JMP     $9932               ; {}
8914: AD 24 07        LDA     $0724               
8917: D0 07           BNE     $8920               ; {}
8919: EE 24 07        INC     $0724               
891C: A9 02           LDA     #$02                
891E: D0 13           BNE     $8933               ; {}
8920: AD E2 04        LDA     $04E2               
8923: D0 12           BNE     $8937               ; {}
8925: E6 3A           INC     $3A                 
8927: A9 00           LDA     #$00                
8929: 8D 24 07        STA     $0724               
892C: A9 3C           LDA     #$3C                
892E: 8D 26 07        STA     $0726               
8931: A9 FF           LDA     #$FF                
8933: 8D E2 04        STA     $04E2               
8936: 60              RTS                         
8937: A9 68           LDA     #$68                
8939: 20 D5 8B        JSR     $8BD5               ; {}
893C: A9 03           LDA     #$03                
893E: 4C 32 99        JMP     $9932               ; {}
8941: AD 26 07        LDA     $0726               
8944: F0 06           BEQ     $894C               ; {}
8946: A9 00           LDA     #$00                
8948: 85 16           STA     $16                 
894A: 85 18           STA     $18                 
894C: 20 B2 80        JSR     $80B2               ; {}
894F: 20 F0 90        JSR     $90F0               ; {}
8952: AD 24 07        LDA     $0724               
8955: D0 1E           BNE     $8975               ; {}
8957: A0 03           LDY     #$03                
8959: AD 26 07        LDA     $0726               
895C: D0 01           BNE     $895F               ; {}
895E: C8              INY                         
895F: 8C E2 04        STY     $04E2               
8962: EE 24 07        INC     $0724               
8965: A9 F8           LDA     #$F8                
8967: A0 60           LDY     #$60                
8969: 99 00 02        STA     $0200,Y             
896C: C8              INY                         
896D: C8              INY                         
896E: C8              INY                         
896F: C8              INY                         
8970: C0 E0           CPY     #$E0                
8972: 90 F5           BCC     $8969               ; {}
8974: 60              RTS                         
8975: AD E2 04        LDA     $04E2               
8978: D0 BD           BNE     $8937               ; {}
897A: AD 26 07        LDA     $0726               
897D: F0 02           BEQ     $8981               ; {}
897F: E6 3A           INC     $3A                 
8981: E6 3A           INC     $3A                 
8983: A9 FF           LDA     #$FF                
8985: 8D 24 07        STA     $0724               
8988: 4C A1 89        JMP     $89A1               ; {}
898B: 20 B2 80        JSR     $80B2               ; {}
898E: F0 09           BEQ     $8999               ; {}
8990: 20 DC 89        JSR     $89DC               ; {}
8993: 20 37 89        JSR     $8937               ; {}
8996: 4C F0 90        JMP     $90F0               ; {}
8999: E6 3A           INC     $3A                 
899B: A9 80           LDA     #$80                
899D: 8D 24 07        STA     $0724               
89A0: 60              RTS                         
89A1: A2 70           LDX     #$70                
89A3: A0 00           LDY     #$00                
89A5: 20 B3 89        JSR     $89B3               ; {}
89A8: A2 80           LDX     #$80                
89AA: A0 04           LDY     #$04                
89AC: 20 B3 89        JSR     $89B3               ; {}
89AF: A2 90           LDX     #$90                
89B1: A0 08           LDY     #$08                
89B3: B9 CC 89        LDA     $89CC,Y             ; {}
89B6: 9D 00 07        STA     $0700,X             
89B9: B9 CD 89        LDA     $89CD,Y             ; {}
89BC: 9D 01 07        STA     $0701,X             
89BF: B9 CE 89        LDA     $89CE,Y             ; {}
89C2: 9D 02 07        STA     $0702,X             
89C5: B9 CF 89        LDA     $89CF,Y             ; {}
89C8: 9D 03 07        STA     $0703,X             
89CB: 60              RTS                         
89CC: 88              DEY                         
89CD: 80 ; ????
89CE: 00              BRK                         
89CF: 58              CLI                         
89D0: 88              DEY                         
89D1: 81 00           STA     ($00,X)             ; {ram.GP_00}
89D3: 78              SEI                         
89D4: 88              DEY                         
89D5: 82 ; ????
89D6: 00              BRK                         
89D7: 9C ; ????
89D8: 88              DEY                         
89D9: 83 ; ????
89DA: 00              BRK                         
89DB: 78              SEI                         
89DC: A2 70           LDX     #$70                
89DE: 20 E8 89        JSR     $89E8               ; {}
89E1: A2 80           LDX     #$80                
89E3: 20 E8 89        JSR     $89E8               ; {}
89E6: A2 90           LDX     #$90                
89E8: 20 C6 98        JSR     $98C6               ; {}
89EB: 20 E1 8C        JSR     $8CE1               ; {}
89EE: 10 1B           BPL     $8A0B               ; {}
89F0: A0 20           LDY     #$20                
89F2: 20 86 D9        JSR     $D986               
89F5: 90 0C           BCC     $8A03               ; {}
89F7: BD 01 07        LDA     $0701,X             
89FA: 29 03           AND     #$03                
89FC: A8              TAY                         
89FD: B9 20 8D        LDA     $8D20,Y             ; {}
8A00: 4C 24 99        JMP     $9924               ; {}
8A03: 20 13 8A        JSR     $8A13               ; {}
8A06: A9 10           LDA     #$10                
8A08: 8D 81 03        STA     $0381               
8A0B: A9 00           LDA     #$00                
8A0D: 9D 01 07        STA     $0701,X             
8A10: 4C 1D DD        JMP     $DD1D               
8A13: BD 01 07        LDA     $0701,X             
8A16: 29 03           AND     #$03                
8A18: A8              TAY                         
8A19: B9 3E 01        LDA     $013E,Y             
8A1C: 29 0F           AND     #$0F                
8A1E: D0 02           BNE     $8A22               ; {}
8A20: A9 01           LDA     #$01                
8A22: 99 3E 01        STA     $013E,Y             
8A25: A9 10           LDA     #$10                
8A27: 4C F0 E2        JMP     $E2F0               
8A2A: 01 02           ORA     ($02,X)             
8A2C: 04 ; ????
8A2D: 04 ; ????
8A2E: A5 3A           LDA     $3A                 
8A30: 0A              ASL     A                   
8A31: A8              TAY                         
8A32: B9 3F 8A        LDA     $8A3F,Y             ; {}
8A35: 85 10           STA     $10                 
8A37: B9 40 8A        LDA     $8A40,Y             ; {}
8A3A: 85 11           STA     $11                 
8A3C: 6C 10 00        JMP     ($0010)             
8A3F: D5 81           CMP     $81,X               
8A41: D5 81           CMP     $81,X               
8A43: D6 81           DEC     $81,X               
8A45: D5 81           CMP     $81,X               
8A47: D5 81           CMP     $81,X               
8A49: 6C 82 D5        JMP     ($D582)             
8A4C: 81 D5           STA     ($D5,X)             
8A4E: 81 D5           STA     ($D5,X)             
8A50: 81 D5           STA     ($D5,X)             
8A52: 81 D5           STA     ($D5,X)             
8A54: 81 D5           STA     ($D5,X)             
8A56: 81 D5           STA     ($D5,X)             
8A58: 81 12           STA     ($12,X)             
8A5A: 82 ; ????
8A5B: A5 3A           LDA     $3A                 
8A5D: 20 2B EE        JSR     $EE2B               
8A60: 90 80           BCC     $89E2               ; {}
8A62: F7 ; ????
8A63: E0 6F           CPX     #$6F                
8A65: 80 ; ????
8A66: 83 ; ????
8A67: 91 8E           STA     ($8E),Y             
8A69: 80 ; ????
8A6A: 6F ; ????
8A6B: 80 ; ????
8A6C: 9D 80 3B        STA     $3B80,X             
8A6F: E1 78           SBC     ($78,X)             
8A71: 8A              TXA                         
8A72: D2 ; ????
8A73: 8A              TXA                         
8A74: 23 ; ????
8A75: 81 6F           STA     ($6F,X)             
8A77: 80 ; ????
8A78: AD 24 07        LDA     $0724               
8A7B: D0 0E           BNE     $8A8B               ; {}
8A7D: 20 A0 8A        JSR     $8AA0               ; {}
8A80: 90 1B           BCC     $8A9D               ; {}
8A82: A9 01           LDA     #$01                
8A84: 8D E2 04        STA     $04E2               
8A87: EE 24 07        INC     $0724               
8A8A: 60              RTS                         
8A8B: AD E2 04        LDA     $04E2               
8A8E: F0 03           BEQ     $8A93               ; {}
8A90: 4C 37 89        JMP     $8937               ; {}
8A93: E6 3A           INC     $3A                 
8A95: A9 00           LDA     #$00                
8A97: 8D 24 07        STA     $0724               
8A9A: 4C E5 8A        JMP     $8AE5               ; {}
8A9D: E6 3A           INC     $3A                 
8A9F: 60              RTS                         
8AA0: A9 00           LDA     #$00                
8AA2: 8D 27 07        STA     $0727               
8AA5: AD 37 01        LDA     $0137               
8AA8: D0 12           BNE     $8ABC               ; {}
8AAA: 38              SEC                         
8AAB: AD 34 01        LDA     $0134               
8AAE: E9 10           SBC     #$10                
8AB0: AD 35 01        LDA     $0135               
8AB3: E9 27           SBC     #$27                
8AB5: AD 36 01        LDA     $0136               
8AB8: E9 00           SBC     #$00                
8ABA: B0 02           BCS     $8ABE               ; {}
8ABC: 18              CLC                         
8ABD: 60              RTS                         
8ABE: AD 52 01        LDA     $0152               
8AC1: C9 04           CMP     #$04                
8AC3: B0 F7           BCS     $8ABC               ; {}
8AC5: EE 27 07        INC     $0727               
8AC8: EE 37 01        INC     $0137               
8ACB: A9 10           LDA     #$10                
8ACD: 20 F0 E2        JSR     $E2F0               
8AD0: 38              SEC                         
8AD1: 60              RTS                         
8AD2: 20 B2 80        JSR     $80B2               ; {}
8AD5: F0 0B           BEQ     $8AE2               ; {}
8AD7: 20 F0 90        JSR     $90F0               ; {}
8ADA: AD 27 07        LDA     $0727               
8ADD: F0 F2           BEQ     $8AD1               ; {}
8ADF: 4C EC 8A        JMP     $8AEC               ; {}
8AE2: 4C C9 87        JMP     $87C9               ; {}
8AE5: A2 70           LDX     #$70                
8AE7: A0 0C           LDY     #$0C                
8AE9: 4C B3 89        JMP     $89B3               ; {}
8AEC: A2 70           LDX     #$70                
8AEE: BD 01 07        LDA     $0701,X             
8AF1: 10 20           BPL     $8B13               ; {}
8AF3: A0 20           LDY     #$20                
8AF5: 20 86 D9        JSR     $D986               
8AF8: 90 05           BCC     $8AFF               ; {}
8AFA: A9 35           LDA     #$35                
8AFC: 4C 24 99        JMP     $9924               ; {}
8AFF: 20 1D DD        JSR     $DD1D               
8B02: AD 52 01        LDA     $0152               
8B05: 29 07           AND     #$07                
8B07: C9 05           CMP     #$05                
8B09: B0 08           BCS     $8B13               ; {}
8B0B: EE 52 01        INC     $0152               
8B0E: A9 80           LDA     #$80                
8B10: 8D 83 03        STA     $0383               
8B13: 60              RTS                         
8B14: A5 3A           LDA     $3A                 
8B16: 0A              ASL     A                   
8B17: A8              TAY                         
8B18: B9 25 8B        LDA     $8B25,Y             ; {}
8B1B: 85 10           STA     $10                 
8B1D: B9 26 8B        LDA     $8B26,Y             ; {}
8B20: 85 11           STA     $11                 
8B22: 6C 10 00        JMP     ($0010)             
8B25: D5 81           CMP     $81,X               
8B27: D5 81           CMP     $81,X               
8B29: D6 81           DEC     $81,X               
8B2B: D5 81           CMP     $81,X               
8B2D: D5 81           CMP     $81,X               
8B2F: 6C 82 D5        JMP     ($D582)             
8B32: 81 D5           STA     ($D5,X)             
8B34: 81 D5           STA     ($D5,X)             
8B36: 81 D5           STA     ($D5,X)             
8B38: 81 D5           STA     ($D5,X)             
8B3A: 81 12           STA     ($12,X)             
8B3C: 82 ; ????
8B3D: A5 3A           LDA     $3A                 
8B3F: 20 2B EE        JSR     $EE2B               
8B42: 90 80           BCC     $8AC4               ; {}
8B44: F7 ; ????
8B45: E0 6F           CPX     #$6F                
8B47: 80 ; ????
8B48: 83 ; ????
8B49: 91 8E           STA     ($8E),Y             
8B4B: 80 ; ????
8B4C: 6F ; ????
8B4D: 80 ; ????
8B4E: 5A ; ????
8B4F: 8B ; ????
8B50: 3B ; ????
8B51: E1 92           SBC     ($92,X)             
8B53: 8B ; ????
8B54: 26 8C           ROL     $8C                 
8B56: 23 ; ????
8B57: 81 6F           STA     ($6F,X)             
8B59: 80 ; ????
8B5A: 20 9D 80        JSR     $809D               ; {}
8B5D: 20 C6 98        JSR     $98C6               ; {}
8B60: 20 6F 8B        JSR     $8B6F               ; {}
8B63: 8D EB 04        STA     $04EB               
8B66: 20 D6 8E        JSR     $8ED6               ; {}
8B69: 20 7E 8F        JSR     $8F7E               ; {}
8B6C: 4C AE 8F        JMP     $8FAE               ; {}
8B6F: A5 3A           LDA     $3A                 
8B71: C9 10           CMP     #$10                
8B73: B0 11           BCS     $8B86               ; {}
8B75: A5 3B           LDA     $3B                 
8B77: C9 26           CMP     #$26                
8B79: F0 14           BEQ     $8B8F               ; {}
8B7B: A5 26           LDA     $26                 
8B7D: 29 03           AND     #$03                
8B7F: C9 02           CMP     #$02                
8B81: 90 02           BCC     $8B85               ; {}
8B83: A9 02           LDA     #$02                
8B85: 60              RTS                         
8B86: 20 7B 8B        JSR     $8B7B               ; {}
8B89: 29 01           AND     #$01                
8B8B: 18              CLC                         
8B8C: 69 03           ADC     #$03                
8B8E: 60              RTS                         
8B8F: A9 05           LDA     #$05                
8B91: 60              RTS                         
8B92: 20 C6 98        JSR     $98C6               ; {}
8B95: A9 05           LDA     #$05                
8B97: 20 9D 8B        JSR     $8B9D               ; {}
8B9A: 4C C6 8B        JMP     $8BC6               ; {}
8B9D: 85 00           STA     $00                 ; {ram.GP_00}
8B9F: AD 24 07        LDA     $0724               
8BA2: D0 0B           BNE     $8BAF               ; {}
8BA4: EE 24 07        INC     $0724               
8BA7: A5 00           LDA     $00                 ; {ram.GP_00}
8BA9: 8D E2 04        STA     $04E2               
8BAC: 4C BF 8C        JMP     $8CBF               ; {}
8BAF: AD E2 04        LDA     $04E2               
8BB2: D0 08           BNE     $8BBC               ; {}
8BB4: E6 3A           INC     $3A                 
8BB6: A9 00           LDA     #$00                
8BB8: 8D 24 07        STA     $0724               
8BBB: 60              RTS                         
8BBC: 4C EB 8C        JMP     $8CEB               ; {}
8BBF: 20 C6 98        JSR     $98C6               ; {}
8BC2: A9 16           LDA     #$16                
8BC4: D0 05           BNE     $8BCB               ; {}
8BC6: 20 C6 98        JSR     $98C6               ; {}
8BC9: A9 02           LDA     #$02                
8BCB: 48              PHA                         
8BCC: A9 58           LDA     #$58                
8BCE: 20 D5 8B        JSR     $8BD5               ; {}
8BD1: 68              PLA                         
8BD2: 4C 32 99        JMP     $9932               ; {}
8BD5: A2 60           LDX     #$60                
8BD7: A9 58           LDA     #$58                
8BD9: 9D 00 07        STA     $0700,X             
8BDC: A9 78           LDA     #$78                
8BDE: 9D 03 07        STA     $0703,X             
8BE1: 60              RTS                         
8BE2: A9 00           LDA     #$00                
8BE4: 8D 24 07        STA     $0724               
8BE7: 8D 26 07        STA     $0726               
8BEA: A5 3A           LDA     $3A                 
8BEC: 29 F0           AND     #$F0                
8BEE: 09 08           ORA     #$08                
8BF0: 85 3A           STA     $3A                 
8BF2: 4C 5D 8B        JMP     $8B5D               ; {}
8BF5: A9 FF           LDA     #$FF                
8BF7: 8D E2 04        STA     $04E2               
8BFA: D0 1F           BNE     $8C1B               ; {}
8BFC: A9 08           LDA     #$08                
8BFE: 8D E2 04        STA     $04E2               
8C01: D0 18           BNE     $8C1B               ; {}
8C03: A5 14           LDA     $14                 
8C05: 29 03           AND     #$03                
8C07: D0 12           BNE     $8C1B               ; {}
8C09: EE 24 07        INC     $0724               
8C0C: AD 24 07        LDA     $0724               
8C0F: C9 F8           CMP     #$F8                
8C11: B0 CF           BCS     $8BE2               ; {}
8C13: C9 D0           CMP     #$D0                
8C15: F0 DE           BEQ     $8BF5               ; {}
8C17: C9 90           CMP     #$90                
8C19: F0 E1           BEQ     $8BFC               ; {}
8C1B: 20 B2 80        JSR     $80B2               ; {}
8C1E: F0 30           BEQ     $8C50               ; {}
8C20: 20 F0 90        JSR     $90F0               ; {}
8C23: 4C C6 8B        JMP     $8BC6               ; {}
8C26: AD 24 07        LDA     $0724               
8C29: 30 D8           BMI     $8C03               ; {}
8C2B: 20 B2 80        JSR     $80B2               ; {}
8C2E: F0 20           BEQ     $8C50               ; {}
8C30: 20 F0 90        JSR     $90F0               ; {}
8C33: 20 5E 8C        JSR     $8C5E               ; {}
8C36: 20 C6 8B        JSR     $8BC6               ; {}
8C39: 20 EB 8C        JSR     $8CEB               ; {}
8C3C: AD 71 07        LDA     $0771               
8C3F: 0D 81 07        ORA     $0781               
8C42: 0D 91 07        ORA     $0791               
8C45: 10 0C           BPL     $8C53               ; {}
8C47: 20 C6 98        JSR     $98C6               ; {}
8C4A: 20 7E 8F        JSR     $8F7E               ; {}
8C4D: 4C AE 8F        JMP     $8FAE               ; {}
8C50: 4C FD 88        JMP     $88FD               ; {}
8C53: A9 80           LDA     #$80                
8C55: 8D 24 07        STA     $0724               
8C58: A9 FF           LDA     #$FF                
8C5A: 8D E2 04        STA     $04E2               
8C5D: 60              RTS                         
8C5E: 20 C6 98        JSR     $98C6               ; {}
8C61: AD 24 07        LDA     $0724               
8C64: D0 16           BNE     $8C7C               ; {}
8C66: A5 71           LDA     $71                 
8C68: D0 24           BNE     $8C8E               ; {}
8C6A: A5 F9           LDA     $F9                 
8C6C: 29 40           AND     #$40                
8C6E: F0 1E           BEQ     $8C8E               ; {}
8C70: A5 F9           LDA     $F9                 
8C72: 29 80           AND     #$80                
8C74: F0 18           BEQ     $8C8E               ; {}
8C76: E6 71           INC     $71                 
8C78: A9 01           LDA     #$01                
8C7A: D0 D9           BNE     $8C55               ; {}
8C7C: C9 10           CMP     #$10                
8C7E: 90 3B           BCC     $8CBB               ; {}
8C80: F0 0D           BEQ     $8C8F               ; {}
8C82: AD E2 04        LDA     $04E2               
8C85: D0 07           BNE     $8C8E               ; {}
8C87: 8D 24 07        STA     $0724               
8C8A: A9 01           LDA     #$01                
8C8C: 85 70           STA     $70                 
8C8E: 60              RTS                         
8C8F: A9 01           LDA     #$01                
8C91: 85 70           STA     $70                 
8C93: AD EC 04        LDA     $04EC               
8C96: 48              PHA                         
8C97: 20 7E 8F        JSR     $8F7E               ; {}
8C9A: A0 06           LDY     #$06                
8C9C: AD EC 04        LDA     $04EC               
8C9F: C9 02           CMP     #$02                
8CA1: B0 07           BCS     $8CAA               ; {}
8CA3: A9 08           LDA     #$08                
8CA5: 8D 82 03        STA     $0382               
8CA8: D0 06           BNE     $8CB0               ; {}
8CAA: A9 04           LDA     #$04                
8CAC: 8D 82 03        STA     $0382               
8CAF: C8              INY                         
8CB0: 8C E2 04        STY     $04E2               
8CB3: 68              PLA                         
8CB4: 8D EC 04        STA     $04EC               
8CB7: A9 00           LDA     #$00                
8CB9: 85 70           STA     $70                 
8CBB: EE 24 07        INC     $0724               
8CBE: 60              RTS                         
8CBF: A2 70           LDX     #$70                
8CC1: A0 00           LDY     #$00                
8CC3: 20 D1 8C        JSR     $8CD1               ; {}
8CC6: A2 80           LDX     #$80                
8CC8: A0 04           LDY     #$04                
8CCA: 20 D1 8C        JSR     $8CD1               ; {}
8CCD: A2 90           LDX     #$90                
8CCF: A0 08           LDY     #$08                
8CD1: 20 B3 89        JSR     $89B3               ; {}
8CD4: 98              TYA                         
8CD5: 4A              LSR     A                   
8CD6: 4A              LSR     A                   
8CD7: A8              TAY                         
8CD8: B9 EE 04        LDA     $04EE,Y             
8CDB: 09 80           ORA     #$80                
8CDD: 9D 01 07        STA     $0701,X             
8CE0: 60              RTS                         
8CE1: AD 71 07        LDA     $0771               
8CE4: 2D 81 07        AND     $0781               
8CE7: 2D 91 07        AND     $0791               
8CEA: 60              RTS                         
8CEB: A2 70           LDX     #$70                
8CED: 20 F7 8C        JSR     $8CF7               ; {}
8CF0: A2 80           LDX     #$80                
8CF2: 20 F7 8C        JSR     $8CF7               ; {}
8CF5: A2 90           LDX     #$90                
8CF7: 20 E1 8C        JSR     $8CE1               ; {}
8CFA: 10 1C           BPL     $8D18               ; {}
8CFC: A0 20           LDY     #$20                
8CFE: 20 86 D9        JSR     $D986               
8D01: 90 0C           BCC     $8D0F               ; {}
8D03: BD 01 07        LDA     $0701,X             
8D06: 29 0F           AND     #$0F                
8D08: A8              TAY                         
8D09: B9 20 8D        LDA     $8D20,Y             ; {}
8D0C: 4C 24 99        JMP     $9924               ; {}
8D0F: 86 0C           STX     $0C                 
8D11: 20 2B 8D        JSR     $8D2B               ; {}
8D14: A6 0C           LDX     $0C                 
8D16: 90 EB           BCC     $8D03               ; {}
8D18: A9 00           LDA     #$00                
8D1A: 9D 01 07        STA     $0701,X             
8D1D: 4C 1D DD        JMP     $DD1D               
8D20: 34 ; ????
8D21: 97 ; ????
8D22: 33 ; ????
8D23: 35 96           AND     $96,X               
8D25: 36 37           ROL     $37,X               
8D27: 38              SEC                         
8D28: 60              RTS                         
8D29: 61 39           ADC     ($39,X)             
8D2B: AD EB 04        LDA     $04EB               
8D2E: C9 05           CMP     #$05                
8D30: D0 05           BNE     $8D37               ; {}
8D32: A9 00           LDA     #$00                
8D34: 8D ED 04        STA     $04ED               
8D37: 20 78 8D        JSR     $8D78               ; {}
8D3A: BD F1 04        LDA     $04F1,X             
8D3D: 20 8E 8D        JSR     $8D8E               ; {}
8D40: 20 A3 8D        JSR     $8DA3               ; {}
8D43: 20 CB 8D        JSR     $8DCB               ; {}
8D46: 90 08           BCC     $8D50               ; {}
8D48: 20 03 8E        JSR     $8E03               ; {}
8D4B: 90 29           BCC     $8D76               ; {}
8D4D: 4C DB 8D        JMP     $8DDB               ; {}
8D50: AD EB 04        LDA     $04EB               
8D53: C9 05           CMP     #$05                
8D55: D0 1F           BNE     $8D76               ; {}
8D57: AD 4E 01        LDA     $014E               
8D5A: F0 1A           BEQ     $8D76               ; {}
8D5C: AD 4C 01        LDA     $014C               
8D5F: D0 15           BNE     $8D76               ; {}
8D61: AD 4D 01        LDA     $014D               
8D64: D0 10           BNE     $8D76               ; {}
8D66: A9 01           LDA     #$01                
8D68: 8D ED 04        STA     $04ED               
8D6B: 20 03 8E        JSR     $8E03               ; {}
8D6E: 90 06           BCC     $8D76               ; {}
8D70: 20 E8 8D        JSR     $8DE8               ; {}
8D73: 4C FA 8D        JMP     $8DFA               ; {}
8D76: 18              CLC                         
8D77: 60              RTS                         
8D78: BD 01 07        LDA     $0701,X             
8D7B: 29 0F           AND     #$0F                
8D7D: 85 0D           STA     $0D                 
8D7F: A2 00           LDX     #$00                
8D81: BD EE 04        LDA     $04EE,X             
8D84: C5 0D           CMP     $0D                 
8D86: F0 05           BEQ     $8D8D               ; {}
8D88: E8              INX                         
8D89: E0 02           CPX     #$02                
8D8B: 90 F4           BCC     $8D81               ; {}
8D8D: 60              RTS                         
8D8E: A8              TAY                         
8D8F: A2 00           LDX     #$00                
8D91: 86 0A           STX     $0A                 
8D93: 86 0B           STX     $0B                 
8D95: A2 04           LDX     #$04                
8D97: 0A              ASL     A                   
8D98: 26 0B           ROL     $0B                 
8D9A: CA              DEX                         
8D9B: D0 FA           BNE     $8D97               ; {}
8D9D: 98              TYA                         
8D9E: 29 0F           AND     #$0F                
8DA0: 85 0A           STA     $0A                 
8DA2: 60              RTS                         
8DA3: A9 00           LDA     #$00                
8DA5: 85 08           STA     $08                 
8DA7: 85 09           STA     $09                 
8DA9: A6 0B           LDX     $0B                 
8DAB: A0 64           LDY     #$64                
8DAD: 20 B4 8D        JSR     $8DB4               ; {}
8DB0: A6 0A           LDX     $0A                 
8DB2: A0 0A           LDY     #$0A                
8DB4: 84 0F           STY     $0F                 
8DB6: E0 00           CPX     #$00                
8DB8: F0 10           BEQ     $8DCA               ; {}
8DBA: 18              CLC                         
8DBB: A5 08           LDA     $08                 
8DBD: 65 0F           ADC     $0F                 
8DBF: 85 08           STA     $08                 
8DC1: A5 09           LDA     $09                 
8DC3: 69 00           ADC     #$00                
8DC5: 85 09           STA     $09                 
8DC7: CA              DEX                         
8DC8: D0 F0           BNE     $8DBA               ; {}
8DCA: 60              RTS                         
8DCB: 38              SEC                         
8DCC: AD 4A 01        LDA     $014A               
8DCF: E5 08           SBC     $08                 
8DD1: 85 0A           STA     $0A                 
8DD3: AD 4B 01        LDA     $014B               
8DD6: E5 09           SBC     $09                 
8DD8: 85 0B           STA     $0B                 
8DDA: 60              RTS                         
8DDB: A2 00           LDX     #$00                
8DDD: B5 0A           LDA     $0A,X               
8DDF: 9D 4A 01        STA     $014A,X             
8DE2: E8              INX                         
8DE3: E0 02           CPX     #$02                
8DE5: 90 F6           BCC     $8DDD               ; {}
8DE7: 60              RTS                         
8DE8: 38              SEC                         
8DE9: A5 08           LDA     $08                 
8DEB: ED 4A 01        SBC     $014A               
8DEE: 8D 4C 01        STA     $014C               
8DF1: A5 09           LDA     $09                 
8DF3: ED 4B 01        SBC     $014B               
8DF6: 8D 4D 01        STA     $014D               
8DF9: 60              RTS                         
8DFA: A9 00           LDA     #$00                
8DFC: 8D 4A 01        STA     $014A               
8DFF: 8D 4B 01        STA     $014B               
8E02: 60              RTS                         
8E03: A5 0D           LDA     $0D                 
8E05: 20 2B EE        JSR     $EE2B               
8E08: 1E 8E 1E        ASL     $1E8E,X             
8E0B: 8E 1E 8E        STX     $8E1E               ; {}
8E0E: 31 8E           AND     ($8E),Y             
8E10: 34 ; ????
8E11: 8E 4C 8E        STX     $8E4C               ; {}
8E14: 56 8E           LSR     $8E,X               
8E16: 70 8E           BVS     $8DA6               ; {}
8E18: 77 ; ????
8E19: 8E 83 8E        STX     $8E83               ; {}
8E1C: 8D 8E 18        STA     $188E               
8E1F: A5 0D           LDA     $0D                 
8E21: AA              TAX                         
8E22: BD 3E 01        LDA     $013E,X             
8E25: 29 0F           AND     #$0F                
8E27: D0 02           BNE     $8E2B               ; {}
8E29: A9 01           LDA     #$01                
8E2B: 9D 3E 01        STA     $013E,X             
8E2E: 4C 99 8E        JMP     $8E99               ; {}
8E31: 4C 97 8E        JMP     $8E97               ; {}
8E34: A9 00           LDA     #$00                
8E36: 85 0E           STA     $0E                 
8E38: AD 51 01        LDA     $0151               
8E3B: A8              TAY                         
8E3C: 29 C0           AND     #$C0                
8E3E: C9 40           CMP     #$40                
8E40: B0 55           BCS     $8E97               ; {}
8E42: 18              CLC                         
8E43: 98              TYA                         
8E44: 09 40           ORA     #$40                
8E46: 8D 51 01        STA     $0151               
8E49: 4C A1 8E        JMP     $8EA1               ; {}
8E4C: 18              CLC                         
8E4D: A5 A6           LDA     $A6                 
8E4F: 69 07           ADC     #$07                
8E51: 85 A6           STA     $A6                 
8E53: D0 51           BNE     $8EA6               ; {}
8E55: 60              RTS                         
8E56: AD 51 01        LDA     $0151               
8E59: A8              TAY                         
8E5A: A2 01           LDX     #$01                
8E5C: 29 C0           AND     #$C0                
8E5E: F0 02           BEQ     $8E62               ; {}
8E60: A2 08           LDX     #$08                
8E62: 86 0E           STX     $0E                 
8E64: 98              TYA                         
8E65: 29 3F           AND     #$3F                
8E67: C5 0E           CMP     $0E                 
8E69: B0 2C           BCS     $8E97               ; {}
8E6B: EE 51 01        INC     $0151               
8E6E: D0 31           BNE     $8EA1               ; {}
8E70: 20 C6 EA        JSR     $EAC6               
8E73: B0 22           BCS     $8E97               ; {}
8E75: 90 2F           BCC     $8EA6               ; {}
8E77: AD 50 01        LDA     $0150               
8E7A: C9 63           CMP     #$63                
8E7C: B0 19           BCS     $8E97               ; {}
8E7E: EE 50 01        INC     $0150               
8E81: D0 1E           BNE     $8EA1               ; {}
8E83: AD 3A 01        LDA     $013A               
8E86: D0 0F           BNE     $8E97               ; {}
8E88: EE 3A 01        INC     $013A               
8E8B: D0 14           BNE     $8EA1               ; {}
8E8D: AD 3B 01        LDA     $013B               
8E90: D0 05           BNE     $8E97               ; {}
8E92: EE 3B 01        INC     $013B               
8E95: D0 0A           BNE     $8EA1               ; {}
8E97: 18              CLC                         
8E98: 60              RTS                         
8E99: A9 10           LDA     #$10                
8E9B: 20 F0 E2        JSR     $E2F0               
8E9E: 4C A6 8E        JMP     $8EA6               ; {}
8EA1: A9 01           LDA     #$01                
8EA3: 20 F0 E2        JSR     $E2F0               
8EA6: A9 10           LDA     #$10                
8EA8: 8D 81 03        STA     $0381               
8EAB: 38              SEC                         
8EAC: 60              RTS                         
8EAD: A5 3A           LDA     $3A                 
8EAF: 0A              ASL     A                   
8EB0: A8              TAY                         
8EB1: B9 BE 8E        LDA     $8EBE,Y             ; {}
8EB4: 85 10           STA     $10                 
8EB6: B9 BF 8E        LDA     $8EBF,Y             ; {}
8EB9: 85 11           STA     $11                 
8EBB: 6C 10 00        JMP     ($0010)             
8EBE: D5 81           CMP     $81,X               
8EC0: D5 81           CMP     $81,X               
8EC2: D6 81           DEC     $81,X               
8EC4: D5 81           CMP     $81,X               
8EC6: D5 81           CMP     $81,X               
8EC8: 6C 82 D5        JMP     ($D582)             
8ECB: 81 D5           STA     ($D5,X)             
8ECD: 81 D5           STA     ($D5,X)             
8ECF: 81 D5           STA     ($D5,X)             
8ED1: 81 D5           STA     ($D5,X)             
8ED3: 81 12           STA     ($12,X)             
8ED5: 82 ; ????
8ED6: A9 00           LDA     #$00                
8ED8: 85 73           STA     $73                 
8EDA: 85 70           STA     $70                 
8EDC: 85 71           STA     $71                 
8EDE: AE EB 04        LDX     $04EB               
8EE1: E0 05           CPX     #$05                
8EE3: B0 06           BCS     $8EEB               ; {}
8EE5: 20 F4 8E        JSR     $8EF4               ; {}
8EE8: 4C EE 8E        JMP     $8EEE               ; {}
8EEB: 20 07 8F        JSR     $8F07               ; {}
8EEE: A9 00           LDA     #$00                
8EF0: 8D EC 04        STA     $04EC               
8EF3: 60              RTS                         
8EF4: BD E9 8F        LDA     $8FE9,X             ; {}
8EF7: AA              TAX                         
8EF8: A0 00           LDY     #$00                
8EFA: BD 8D EF        LDA     $EF8D,X             
8EFD: 99 EE 04        STA     $04EE,Y             
8F00: E8              INX                         
8F01: C8              INY                         
8F02: C0 03           CPY     #$03                
8F04: 90 F4           BCC     $8EFA               ; {}
8F06: 60              RTS                         
8F07: A2 00           LDX     #$00                
8F09: BD 3E 01        LDA     $013E,X             
8F0C: 30 06           BMI     $8F14               ; {}
8F0E: BD 9C EF        LDA     $EF9C,X             
8F11: 4C 17 8F        JMP     $8F17               ; {}
8F14: BD 9F EF        LDA     $EF9F,X             
8F17: 9D EE 04        STA     $04EE,X             
8F1A: E8              INX                         
8F1B: E0 03           CPX     #$03                
8F1D: 90 EA           BCC     $8F09               ; {}
8F1F: 60              RTS                         
8F20: A5 3A           LDA     $3A                 
8F22: C9 10           CMP     #$10                
8F24: B0 11           BCS     $8F37               ; {}
8F26: C9 06           CMP     #$06                
8F28: 90 13           BCC     $8F3D               ; {}
8F2A: A5 3B           LDA     $3B                 
8F2C: C9 25           CMP     #$25                
8F2E: F0 10           BEQ     $8F40               ; {}
8F30: C9 26           CMP     #$26                
8F32: F0 0C           BEQ     $8F40               ; {}
8F34: 68              PLA                         
8F35: 68              PLA                         
8F36: 60              RTS                         
8F37: A5 3B           LDA     $3B                 
8F39: C9 16           CMP     #$16                
8F3B: F0 08           BEQ     $8F45               ; {}
8F3D: 68              PLA                         
8F3E: 68              PLA                         
8F3F: 60              RTS                         
8F40: A9 21           LDA     #$21                
8F42: 85 00           STA     $00                 ; {ram.GP_00}
8F44: 60              RTS                         
8F45: A9 29           LDA     #$29                
8F47: 85 00           STA     $00                 ; {ram.GP_00}
8F49: 60              RTS                         
8F4A: 20 C6 98        JSR     $98C6               ; {}
8F4D: 20 20 8F        JSR     $8F20               ; {}
8F50: A2 00           LDX     #$00                
8F52: A0 C9           LDY     #$C9                
8F54: 20 5E 8F        JSR     $8F5E               ; {}
8F57: A0 CE           LDY     #$CE                
8F59: 20 5E 8F        JSR     $8F5E               ; {}
8F5C: A0 D3           LDY     #$D3                
8F5E: A5 00           LDA     $00                 ; {ram.GP_00}
8F60: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
8F63: 8C 06 20        STY     $2006               ; {hard.P_VRAM_ADDR}
8F66: BD F1 04        LDA     $04F1,X             
8F69: A8              TAY                         
8F6A: 4A              LSR     A                   
8F6B: 4A              LSR     A                   
8F6C: 4A              LSR     A                   
8F6D: 4A              LSR     A                   
8F6E: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
8F71: 98              TYA                         
8F72: 29 0F           AND     #$0F                
8F74: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
8F77: A9 00           LDA     #$00                
8F79: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
8F7C: E8              INX                         
8F7D: 60              RTS                         
8F7E: AD EB 04        LDA     $04EB               
8F81: C9 05           CMP     #$05                
8F83: B0 28           BCS     $8FAD               ; {}
8F85: A5 71           LDA     $71                 
8F87: F0 24           BEQ     $8FAD               ; {}
8F89: A5 70           LDA     $70                 
8F8B: F0 20           BEQ     $8FAD               ; {}
8F8D: AE 2F 01        LDX     $012F               
8F90: E0 03           CPX     #$03                
8F92: 90 02           BCC     $8F96               ; {}
8F94: A2 02           LDX     #$02                
8F96: AD 52 01        LDA     $0152               
8F99: C9 05           CMP     #$05                
8F9B: 90 02           BCC     $8F9F               ; {}
8F9D: A9 04           LDA     #$04                
8F9F: 18              CLC                         
8FA0: 7D F0 8F        ADC     $8FF0,X             ; {}
8FA3: AA              TAX                         
8FA4: BD BA EF        LDA     $EFBA,X             
8FA7: 18              CLC                         
8FA8: 69 01           ADC     #$01                
8FAA: 8D EC 04        STA     $04EC               
8FAD: 60              RTS                         
8FAE: A2 00           LDX     #$00                
8FB0: AD EB 04        LDA     $04EB               
8FB3: C9 05           CMP     #$05                
8FB5: B0 1B           BCS     $8FD2               ; {}
8FB7: BD EE 04        LDA     $04EE,X             
8FBA: 38              SEC                         
8FBB: E9 05           SBC     #$05                
8FBD: A8              TAY                         
8FBE: B9 E9 8F        LDA     $8FE9,Y             ; {}
8FC1: 18              CLC                         
8FC2: 6D EC 04        ADC     $04EC               
8FC5: A8              TAY                         
8FC6: B9 A2 EF        LDA     $EFA2,Y             
8FC9: 9D F1 04        STA     $04F1,X             
8FCC: E8              INX                         
8FCD: E0 03           CPX     #$03                
8FCF: 90 E6           BCC     $8FB7               ; {}
8FD1: 60              RTS                         
8FD2: BD 3E 01        LDA     $013E,X             
8FD5: 30 06           BMI     $8FDD               ; {}
8FD7: BD B4 EF        LDA     $EFB4,X             
8FDA: 4C E0 8F        JMP     $8FE0               ; {}
8FDD: BD B7 EF        LDA     $EFB7,X             
8FE0: 9D F1 04        STA     $04F1,X             
8FE3: E8              INX                         
8FE4: E0 03           CPX     #$03                
8FE6: 90 EA           BCC     $8FD2               ; {}
8FE8: 60              RTS                         
8FE9: 00              BRK                         
8FEA: 03 ; ????
8FEB: 06 09           ASL     $09                 
8FED: 0C ; ????
8FEE: 0F ; ????
8FEF: 12 ; ????
8FF0: 00              BRK                         
8FF1: 05 0A           ORA     $0A                 
8FF3: 0F ; ????
8FF4: A5 3A           LDA     $3A                 
8FF6: 20 2B EE        JSR     $EE2B               
8FF9: 90 80           BCC     $8F7B               ; {}
8FFB: F7 ; ????
8FFC: E0 6F           CPX     #$6F                
8FFE: 80 ; ????
8FFF: 83 ; ????
9000: 91 8E           STA     ($8E),Y             
9002: 80 ; ????
9003: 6F ; ????
9004: 80 ; ????
9005: 11 90           ORA     ($90),Y             
9007: 3B ; ????
9008: E1 17           SBC     ($17,X)             
900A: 90 67           BCC     $9073               ; {}
900C: 90 23           BCC     $9031               ; {}
900E: 81 6F           STA     ($6F,X)             
9010: 80 ; ????
9011: 20 9D 80        JSR     $809D               ; {}
9014: 4C 5D 8B        JMP     $8B5D               ; {}
9017: A9 09           LDA     #$09                
9019: 20 9D 8B        JSR     $8B9D               ; {}
901C: 4C 1F 90        JMP     $901F               ; {}
901F: A9 9C           LDA     #$9C                
9021: 4C CB 8B        JMP     $8BCB               ; {}
9024: A9 FF           LDA     #$FF                
9026: 8D E2 04        STA     $04E2               
9029: D0 31           BNE     $905C               ; {}
902B: A9 0B           LDA     #$0B                
902D: 38              SEC                         
902E: ED ED 04        SBC     $04ED               
9031: 8D E2 04        STA     $04E2               
9034: AD ED 04        LDA     $04ED               
9037: F0 23           BEQ     $905C               ; {}
9039: A9 10           LDA     #$10                
903B: 20 37 E3        JSR     $E337               
903E: 4C 5C 90        JMP     $905C               ; {}
9041: AD 24 07        LDA     $0724               
9044: C9 F8           CMP     #$F8                
9046: B0 14           BCS     $905C               ; {}
9048: A5 14           LDA     $14                 
904A: 29 03           AND     #$03                
904C: D0 0E           BNE     $905C               ; {}
904E: EE 24 07        INC     $0724               
9051: AD 24 07        LDA     $0724               
9054: C9 F0           CMP     #$F0                
9056: F0 CC           BEQ     $9024               ; {}
9058: C9 90           CMP     #$90                
905A: F0 CF           BEQ     $902B               ; {}
905C: 20 B2 80        JSR     $80B2               ; {}
905F: F0 2C           BEQ     $908D               ; {}
9061: 20 F0 90        JSR     $90F0               ; {}
9064: 4C 1F 90        JMP     $901F               ; {}
9067: AD 24 07        LDA     $0724               
906A: 30 D5           BMI     $9041               ; {}
906C: D0 19           BNE     $9087               ; {}
906E: 20 B2 80        JSR     $80B2               ; {}
9071: F0 1A           BEQ     $908D               ; {}
9073: 20 F0 90        JSR     $90F0               ; {}
9076: 20 1F 90        JSR     $901F               ; {}
9079: 20 EB 8C        JSR     $8CEB               ; {}
907C: AD 71 07        LDA     $0771               
907F: 0D 81 07        ORA     $0781               
9082: 0D 91 07        ORA     $0791               
9085: 10 09           BPL     $9090               ; {}
9087: 20 7E 8F        JSR     $8F7E               ; {}
908A: 4C AE 8F        JMP     $8FAE               ; {}
908D: 4C FD 88        JMP     $88FD               ; {}
9090: A9 FF           LDA     #$FF                
9092: 8D E2 04        STA     $04E2               
9095: A9 80           LDA     #$80                
9097: 8D 24 07        STA     $0724               
909A: 60              RTS                         
909B: A5 3A           LDA     $3A                 
909D: 0A              ASL     A                   
909E: A8              TAY                         
909F: B9 AC 90        LDA     $90AC,Y             ; {}
90A2: 85 10           STA     $10                 
90A4: B9 AD 90        LDA     $90AD,Y             ; {}
90A7: 85 11           STA     $11                 
90A9: 6C 10 00        JMP     ($0010)             
90AC: D5 81           CMP     $81,X               
90AE: D5 81           CMP     $81,X               
90B0: D6 81           DEC     $81,X               
90B2: D5 81           CMP     $81,X               
90B4: D5 81           CMP     $81,X               
90B6: 6C 82 D5        JMP     ($D582)             
90B9: 81 D5           STA     ($D5,X)             
90BB: 81 D5           STA     ($D5,X)             
90BD: 81 D5           STA     ($D5,X)             
90BF: 81 D5           STA     ($D5,X)             
90C1: 81 12           STA     ($12,X)             
90C3: 82 ; ????
90C4: A5 3A           LDA     $3A                 
90C6: 20 2B EE        JSR     $EE2B               
90C9: 90 80           BCC     $904B               ; {}
90CB: F7 ; ????
90CC: E0 6F           CPX     #$6F                
90CE: 80 ; ????
90CF: 83 ; ????
90D0: 91 8E           STA     ($8E),Y             
90D2: 80 ; ????
90D3: 6F ; ????
90D4: 80 ; ????
90D5: 9D 80 3B        STA     $3B80,X             
90D8: E1 DF           SBC     ($DF,X)             
90DA: 90 23           BCC     $90FF               ; {}
90DC: 81 6F           STA     ($6F,X)             
90DE: 80 ; ????
90DF: 20 B2 80        JSR     $80B2               ; {}
90E2: F0 09           BEQ     $90ED               ; {}
90E4: A9 D4           LDA     #$D4                
90E6: 48              PHA                         
90E7: A9 A1           LDA     #$A1                
90E9: 48              PHA                         
90EA: 4C 49 CB        JMP     $CB49               
90ED: 4C FD 88        JMP     $88FD               ; {}
90F0: A9 D4           LDA     #$D4                
90F2: 48              PHA                         
90F3: A9 A1           LDA     #$A1                
90F5: 48              PHA                         
90F6: 20 F7 CA        JSR     $CAF7               
90F9: 60              RTS                         
90FA: A5 3A           LDA     $3A                 
90FC: 0A              ASL     A                   
90FD: A8              TAY                         
90FE: B9 0B 91        LDA     $910B,Y             ; {}
9101: 85 10           STA     $10                 
9103: B9 0C 91        LDA     $910C,Y             ; {}
9106: 85 11           STA     $11                 
9108: 6C 10 00        JMP     ($0010)             
910B: D5 81           CMP     $81,X               
910D: D5 81           CMP     $81,X               
910F: D6 81           DEC     $81,X               
9111: D5 81           CMP     $81,X               
9113: D5 81           CMP     $81,X               
9115: 6C 82 D5        JMP     ($D582)             
9118: 81 D5           STA     ($D5,X)             
911A: 81 D5           STA     ($D5,X)             
911C: 81 D5           STA     ($D5,X)             
911E: 81 12           STA     ($12,X)             
9120: 82 ; ????
9121: A5 3A           LDA     $3A                 
9123: 20 2B EE        JSR     $EE2B               
9126: 90 80           BCC     $90A8               ; {}
9128: F7 ; ????
9129: E0 6F           CPX     #$6F                
912B: 80 ; ????
912C: 6F ; ????
912D: 80 ; ????
912E: 6F ; ????
912F: 80 ; ????
9130: 6F ; ????
9131: 80 ; ????
9132: 83 ; ????
9133: 91 8E           STA     ($8E),Y             
9135: 80 ; ????
9136: 38              SEC                         
9137: 91 A9           STA     ($A9),Y             
9139: 00              BRK                         
913A: 85 3A           STA     $3A                 
913C: 85 37           STA     $37                 
913E: A0 00           LDY     #$00                
9140: A5 A0           LDA     $A0                 
9142: C9 07           CMP     #$07                
9144: D0 01           BNE     $9147               ; {}
9146: EA              NOP                         
9147: 84 38           STY     $38                 
9149: A9 80           LDA     #$80                
914B: 85 AB           STA     $AB                 
914D: 60              RTS                         
914E: A5 3A           LDA     $3A                 
9150: 0A              ASL     A                   
9151: A8              TAY                         
9152: B9 5F 91        LDA     $915F,Y             ; {}
9155: 85 10           STA     $10                 
9157: B9 60 91        LDA     $9160,Y             ; {}
915A: 85 11           STA     $11                 
915C: 6C 10 00        JMP     ($0010)             
915F: D5 81           CMP     $81,X               
9161: D5 81           CMP     $81,X               
9163: 73 ; ????
9164: 91 D5           STA     ($D5),Y             
9166: 81 D5           STA     ($D5,X)             
9168: 81 6C           STA     ($6C,X)             
916A: 82 ; ????
916B: D5 81           CMP     $81,X               
916D: D5 81           CMP     $81,X               
916F: D5 81           CMP     $81,X               
9171: D5 81           CMP     $81,X               
9173: 20 91 81        JSR     $8191               ; {}
9176: 20 EE 81        JSR     $81EE               ; {}
9179: E6 3A           INC     $3A                 
917B: E6 3A           INC     $3A                 
917D: 20 AF 92        JSR     $92AF               ; {}
9180: 4C E0 81        JMP     $81E0               ; {}
9183: AD 24 07        LDA     $0724               
9186: F0 2F           BEQ     $91B7               ; {}
9188: C9 01           CMP     #$01                
918A: F0 51           BEQ     $91DD               ; {}
918C: C9 02           CMP     #$02                
918E: F0 58           BEQ     $91E8               ; {}
9190: AD 23 07        LDA     $0723               
9193: C9 F8           CMP     #$F8                
9195: B0 13           BCS     $91AA               ; {}
9197: A9 01           LDA     #$01                
9199: 85 16           STA     $16                 
919B: A9 00           LDA     #$00                
919D: 85 18           STA     $18                 
919F: A2 20           LDX     #$20                
91A1: A9 CD           LDA     #$CD                
91A3: 48              PHA                         
91A4: A9 04           LDA     #$04                
91A6: 48              PHA                         
91A7: 4C 49 CB        JMP     $CB49               
91AA: E6 3A           INC     $3A                 
91AC: A9 FF           LDA     #$FF                
91AE: 8D 23 07        STA     $0723               
91B1: A9 00           LDA     #$00                
91B3: 8D 24 07        STA     $0724               
91B6: 60              RTS                         
91B7: EE 24 07        INC     $0724               
91BA: A2 20           LDX     #$20                
91BC: 20 C9 C3        JSR     $C3C9               
91BF: A9 80           LDA     #$80                
91C1: 9D 01 07        STA     $0701,X             
91C4: A9 08           LDA     #$08                
91C6: 9D 03 07        STA     $0703,X             
91C9: A9 90           LDA     #$90                
91CB: 9D 00 07        STA     $0700,X             
91CE: A9 00           LDA     #$00                
91D0: 8D 80 03        STA     $0380               
91D3: A9 40           LDA     #$40                
91D5: 8D 84 03        STA     $0384               
91D8: A9 FF           LDA     #$FF                
91DA: 85 1A           STA     $1A                 
91DC: 60              RTS                         
91DD: AD 23 07        LDA     $0723               
91E0: C9 80           CMP     #$80                
91E2: D0 B3           BNE     $9197               ; {}
91E4: EE 24 07        INC     $0724               
91E7: 60              RTS                         
91E8: 20 07 93        JSR     $9307               ; {}
91EB: AD 60 07        LDA     $0760               
91EE: D0 1C           BNE     $920C               ; {}
91F0: AD 63 07        LDA     $0763               
91F3: C9 04           CMP     #$04                
91F5: F0 28           BEQ     $921F               ; {}
91F7: A5 AA           LDA     $AA                 
91F9: 85 00           STA     $00                 ; {ram.GP_00}
91FB: AD 67 07        LDA     $0767               
91FE: 85 AA           STA     $AA                 
9200: C5 00           CMP     $00                 ; {ram.GP_00}
9202: F0 05           BEQ     $9209               ; {}
9204: A9 80           LDA     #$80                
9206: 8D 83 03        STA     $0383               
9209: EE 24 07        INC     $0724               
920C: A9 08           LDA     #$08                
920E: 85 16           STA     $16                 
9210: A0 00           LDY     #$00                
9212: A5 14           LDA     $14                 
9214: 29 1F           AND     #$1F                
9216: D0 02           BNE     $921A               ; {}
9218: A0 80           LDY     #$80                
921A: 84 18           STY     $18                 
921C: 4C 9F 91        JMP     $919F               ; {}
921F: AD 62 07        LDA     $0762               
9222: D0 E8           BNE     $920C               ; {}
9224: A9 00           LDA     #$00                
9226: 8D 66 07        STA     $0766               
9229: 20 85 93        JSR     $9385               ; {}
922C: 20 FF 93        JSR     $93FF               ; {}
922F: 90 06           BCC     $9237               ; {}
9231: 20 0B 94        JSR     $940B               ; {}
9234: 4C 2C 92        JMP     $922C               ; {}
9237: EE 66 07        INC     $0766               
923A: AD 66 07        LDA     $0766               
923D: C9 07           CMP     #$07                
923F: 90 E8           BCC     $9229               ; {}
9241: A9 00           LDA     #$00                
9243: 8D 67 07        STA     $0767               
9246: A2 02           LDX     #$02                
9248: BD 44 01        LDA     $0144,X             
924B: 9D 28 01        STA     $0128,X             
924E: CA              DEX                         
924F: 10 F7           BPL     $9248               ; {}
9251: A9 28           LDA     #$28                
9253: 85 00           STA     $00                 ; {ram.GP_00}
9255: A9 01           LDA     #$01                
9257: 85 01           STA     $01                 
9259: A9 02           LDA     #$02                
925B: 8D 66 07        STA     $0766               
925E: 20 85 93        JSR     $9385               ; {}
9261: A9 02           LDA     #$02                
9263: 20 A3 92        JSR     $92A3               ; {}
9266: 90 27           BCC     $928F               ; {}
9268: EE 67 07        INC     $0767               
926B: A9 03           LDA     #$03                
926D: 20 A3 92        JSR     $92A3               ; {}
9270: 90 1D           BCC     $928F               ; {}
9272: EE 67 07        INC     $0767               
9275: A9 05           LDA     #$05                
9277: 20 A3 92        JSR     $92A3               ; {}
927A: 90 13           BCC     $928F               ; {}
927C: EE 67 07        INC     $0767               
927F: CE 66 07        DEC     $0766               
9282: 20 85 93        JSR     $9385               ; {}
9285: A9 01           LDA     #$01                
9287: 20 A3 92        JSR     $92A3               ; {}
928A: 90 03           BCC     $928F               ; {}
928C: EE 67 07        INC     $0767               
928F: A5 AA           LDA     $AA                 
9291: CD 67 07        CMP     $0767               
9294: D0 05           BNE     $929B               ; {}
9296: A9 00           LDA     #$00                
9298: 8D 63 07        STA     $0763               
929B: A9 04           LDA     #$04                
929D: 8D 60 07        STA     $0760               
92A0: 4C 0C 92        JMP     $920C               ; {}
92A3: 85 09           STA     $09                 
92A5: 20 AC 93        JSR     $93AC               ; {}
92A8: 90 04           BCC     $92AE               ; {}
92AA: C6 09           DEC     $09                 
92AC: D0 F7           BNE     $92A5               ; {}
92AE: 60              RTS                         
92AF: A9 05           LDA     #$05                
92B1: 8D 66 07        STA     $0766               
92B4: A9 00           LDA     #$00                
92B6: 8D 62 07        STA     $0762               
92B9: 8D 61 07        STA     $0761               
92BC: 8D 64 07        STA     $0764               
92BF: 8D 65 07        STA     $0765               
92C2: AA              TAX                         
92C3: 20 E0 92        JSR     $92E0               ; {}
92C6: E8              INX                         
92C7: AD 30 01        LDA     $0130               
92CA: C9 03           CMP     #$03                
92CC: B0 05           BCS     $92D3               ; {}
92CE: E0 03           CPX     #$03                
92D0: 4C D5 92        JMP     $92D5               ; {}
92D3: E0 04           CPX     #$04                
92D5: 90 EC           BCC     $92C3               ; {}
92D7: 20 11 94        JSR     $9411               ; {}
92DA: A9 01           LDA     #$01                
92DC: 8D 60 07        STA     $0760               
92DF: 60              RTS                         
92E0: 8A              TXA                         
92E1: 0A              ASL     A                   
92E2: A8              TAY                         
92E3: B9 73 94        LDA     $9473,Y             ; {}
92E6: 85 00           STA     $00                 ; {ram.GP_00}
92E8: B9 74 94        LDA     $9474,Y             ; {}
92EB: 85 01           STA     $01                 
92ED: A0 00           LDY     #$00                
92EF: B1 00           LDA     ($00),Y             ; {ram.GP_00}
92F1: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
92F4: C8              INY                         
92F5: B1 00           LDA     ($00),Y             ; {ram.GP_00}
92F7: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
92FA: C8              INY                         
92FB: B1 00           LDA     ($00),Y             ; {ram.GP_00}
92FD: C9 FF           CMP     #$FF                
92FF: F0 DE           BEQ     $92DF               ; {}
9301: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
9304: 4C FA 92        JMP     $92FA               ; {}
9307: EE 64 07        INC     $0764               
930A: D0 03           BNE     $930F               ; {}
930C: EE 65 07        INC     $0765               
930F: AD 60 07        LDA     $0760               
9312: F0 1D           BEQ     $9331               ; {}
9314: AD 61 07        LDA     $0761               
9317: D0 09           BNE     $9322               ; {}
9319: AD 60 07        LDA     $0760               
931C: 8D 61 07        STA     $0761               
931F: EE 60 07        INC     $0760               
9322: 20 2B EE        JSR     $EE2B               
9325: 31 93           AND     ($93),Y             
9327: 58              CLI                         
9328: 93 ; ????
9329: 60              RTS                         
932A: 93 ; ????
932B: 32 ; ????
932C: 93 ; ????
932D: 58              CLI                         
932E: 94 32           STY     $32,X               
9330: 93 ; ????
9331: 60              RTS                         
9332: AD 60 07        LDA     $0760               
9335: 8D 63 07        STA     $0763               
9338: A9 00           LDA     #$00                
933A: 8D 60 07        STA     $0760               
933D: A9 00           LDA     #$00                
933F: 8D 61 07        STA     $0761               
9342: 8D 62 07        STA     $0762               
9345: 8D 65 07        STA     $0765               
9348: 8D 64 07        STA     $0764               
934B: 60              RTS                         
934C: A5 14           LDA     $14                 
934E: 29 0F           AND     #$0F                
9350: D0 05           BNE     $9357               ; {}
9352: A9 01           LDA     #$01                
9354: 8D 81 03        STA     $0381               
9357: 60              RTS                         
9358: A9 04           LDA     #$04                
935A: 8D 66 07        STA     $0766               
935D: 4C 3D 93        JMP     $933D               ; {}
9360: 20 4C 93        JSR     $934C               ; {}
9363: AD 66 07        LDA     $0766               
9366: C9 07           CMP     #$07                
9368: B0 D3           BCS     $933D               ; {}
936A: 20 85 93        JSR     $9385               ; {}
936D: 20 F9 93        JSR     $93F9               ; {}
9370: 90 06           BCC     $9378               ; {}
9372: 20 05 94        JSR     $9405               ; {}
9375: 4C 11 94        JMP     $9411               ; {}
9378: EE 66 07        INC     $0766               
937B: 4C 60 93        JMP     $9360               ; {}
937E: AA              TAX                         
937F: 4C 88 93        JMP     $9388               ; {}
9382: 8D 66 07        STA     $0766               
9385: AE 66 07        LDX     $0766               
9388: BD 9B 93        LDA     $939B,X             ; {}
938B: AA              TAX                         
938C: A0 00           LDY     #$00                
938E: BD 70 EA        LDA     $EA70,X             
9391: 99 68 07        STA     $0768,Y             
9394: E8              INX                         
9395: C8              INY                         
9396: C0 03           CPY     #$03                
9398: 90 F4           BCC     $938E               ; {}
939A: 60              RTS                         
939B: 00              BRK                         
939C: 03 ; ????
939D: 06 09           ASL     $09                 
939F: 0C ; ????
93A0: 0F ; ????
93A1: 12 ; ????
93A2: 8D 66 07        STA     $0766               
93A5: 20 85 93        JSR     $9385               ; {}
93A8: 86 00           STX     $00                 ; {ram.GP_00}
93AA: 84 01           STY     $01                 
93AC: A0 00           LDY     #$00                
93AE: 38              SEC                         
93AF: B1 00           LDA     ($00),Y             ; {ram.GP_00}
93B1: ED 68 07        SBC     $0768               
93B4: 85 02           STA     $02                 
93B6: C8              INY                         
93B7: B1 00           LDA     ($00),Y             ; {ram.GP_00}
93B9: ED 69 07        SBC     $0769               
93BC: 85 03           STA     $03                 
93BE: C8              INY                         
93BF: B1 00           LDA     ($00),Y             ; {ram.GP_00}
93C1: ED 6A 07        SBC     $076A               
93C4: B0 01           BCS     $93C7               ; {}
93C6: 60              RTS                         
93C7: 91 00           STA     ($00),Y             ; {ram.GP_00}
93C9: A5 03           LDA     $03                 
93CB: 88              DEY                         
93CC: 91 00           STA     ($00),Y             ; {ram.GP_00}
93CE: A5 02           LDA     $02                 
93D0: 88              DEY                         
93D1: 91 00           STA     ($00),Y             ; {ram.GP_00}
93D3: 60              RTS                         
93D4: 8D 66 07        STA     $0766               
93D7: 20 85 93        JSR     $9385               ; {}
93DA: 86 00           STX     $00                 ; {ram.GP_00}
93DC: 84 01           STY     $01                 
93DE: A0 00           LDY     #$00                
93E0: 18              CLC                         
93E1: B1 00           LDA     ($00),Y             ; {ram.GP_00}
93E3: 6D 68 07        ADC     $0768               
93E6: 85 02           STA     $02                 
93E8: C8              INY                         
93E9: B1 00           LDA     ($00),Y             ; {ram.GP_00}
93EB: 6D 69 07        ADC     $0769               
93EE: 85 03           STA     $03                 
93F0: C8              INY                         
93F1: B1 00           LDA     ($00),Y             ; {ram.GP_00}
93F3: 6D 6A 07        ADC     $076A               
93F6: 90 CF           BCC     $93C7               ; {}
93F8: 60              RTS                         
93F9: A2 31           LDX     #$31                
93FB: A0 01           LDY     #$01                
93FD: D0 A9           BNE     $93A8               ; {}
93FF: A2 34           LDX     #$34                
9401: A0 01           LDY     #$01                
9403: D0 A3           BNE     $93A8               ; {}
9405: A2 44           LDX     #$44                
9407: A0 01           LDY     #$01                
9409: D0 CF           BNE     $93DA               ; {}
940B: A2 47           LDX     #$47                
940D: A0 01           LDY     #$01                
940F: D0 C9           BNE     $93DA               ; {}
9411: 20 33 94        JSR     $9433               ; {}
9414: A2 31           LDX     #$31                
9416: A0 01           LDY     #$01                
9418: A9 07           LDA     #$07                
941A: 20 A7 94        JSR     $94A7               ; {}
941D: A9 29           LDA     #$29                
941F: 8D 10 01        STA     $0110               
9422: A9 11           LDA     #$11                
9424: 8D 0F 01        STA     $010F               
9427: A9 07           LDA     #$07                
9429: 8D 0E 01        STA     $010E               
942C: A2 11           LDX     #$11                
942E: A0 01           LDY     #$01                
9430: 4C E5 94        JMP     $94E5               ; {}
9433: A2 44           LDX     #$44                
9435: A0 01           LDY     #$01                
9437: A9 07           LDA     #$07                
9439: 20 A7 94        JSR     $94A7               ; {}
943C: A9 28           LDA     #$28                
943E: 8D 06 01        STA     $0106               
9441: A9 F1           LDA     #$F1                
9443: 8D 05 01        STA     $0105               
9446: A9 07           LDA     #$07                
9448: 8D 04 01        STA     $0104               
944B: A2 07           LDX     #$07                
944D: A0 01           LDY     #$01                
944F: 4C E5 94        JMP     $94E5               ; {}
9452: A9 00           LDA     #$00                
9454: 8D 18 01        STA     $0118               
9457: 60              RTS                         
9458: AD 63 07        LDA     $0763               
945B: F0 13           BEQ     $9470               ; {}
945D: AD 62 07        LDA     $0762               
9460: D0 09           BNE     $946B               ; {}
9462: A9 0D           LDA     #$0D                
9464: 8D E2 04        STA     $04E2               
9467: EE 62 07        INC     $0762               
946A: 60              RTS                         
946B: AD E2 04        LDA     $04E2               
946E: D0 FA           BNE     $946A               ; {}
9470: 4C 3D 93        JMP     $933D               ; {}
9473: 83 ; ????
9474: 94 83           STY     $83,X               
9476: 94 91           STY     $91,X               
9478: 94 91           STY     $91,X               
947A: 94 99           STY     $99,X               
947C: 94 9D           STY     $9D,X               
947E: 94 A1           STY     $A1,X               
9480: 94 A1           STY     $A1,X               
9482: 94 28           STY     $28,X               
9484: E5 29           SBC     $29                 
9486: 24 29           BIT     $29                 
9488: 16 21           ASL     $21,X               
948A: 12 ; ????
948B: 28              PLP                         
948C: 18              CLC                         
948D: 24 27           BIT     $27                 
948F: 1A ; ????
9490: FF ; ????
9491: 29 0B           AND     #$0B                
9493: 28              PLP                         
9494: 18              CLC                         
9495: 24 27           BIT     $27                 
9497: 1A ; ????
9498: FF ; ????
9499: 2B ; ????
949A: F3 ; ????
949B: 03 ; ????
949C: FF ; ????
949D: 2B ; ????
949E: 36 22           ROL     $22,X               
94A0: FF ; ????
94A1: 2B ; ????
94A2: 57 ; ????
94A3: 33 ; ????
94A4: 10 22           BPL     $94C8               ; {}
94A6: FF ; ????
94A7: 20 BB 94        JSR     $94BB               ; {}
94AA: 20 CF E9        JSR     $E9CF               
94AD: B0 05           BCS     $94B4               ; {}
94AF: 20 E6 E9        JSR     $E9E6               
94B2: B0 03           BCS     $94B7               ; {}
94B4: 20 1C EA        JSR     $EA1C               
94B7: 20 27 EA        JSR     $EA27               
94BA: 60              RTS                         
94BB: 85 02           STA     $02                 
94BD: 86 0C           STX     $0C                 
94BF: 84 0D           STY     $0D                 
94C1: AA              TAX                         
94C2: A9 00           LDA     #$00                
94C4: 85 05           STA     $05                 
94C6: 85 06           STA     $06                 
94C8: 85 07           STA     $07                 
94CA: A9 12           LDA     #$12                
94CC: 85 03           STA     $03                 
94CE: BD 55 EA        LDA     $EA55,X             
94D1: A8              TAY                         
94D2: B1 0C           LDA     ($0C),Y             
94D4: 99 05 00        STA     $0005,Y             
94D7: 88              DEY                         
94D8: 10 F8           BPL     $94D2               ; {}
94DA: A2 06           LDX     #$06                
94DC: A9 00           LDA     #$00                
94DE: 9D 28 01        STA     $0128,X             
94E1: CA              DEX                         
94E2: 10 FA           BPL     $94DE               ; {}
94E4: 60              RTS                         
94E5: 86 00           STX     $00                 ; {ram.GP_00}
94E7: 84 01           STY     $01                 
94E9: 85 02           STA     $02                 
94EB: AA              TAX                         
94EC: BD 5D EA        LDA     $EA5D,X             
94EF: AA              TAX                         
94F0: A0 00           LDY     #$00                
94F2: BD 28 01        LDA     $0128,X             
94F5: 91 00           STA     ($00),Y             ; {ram.GP_00}
94F7: C8              INY                         
94F8: E8              INX                         
94F9: C4 02           CPY     $02                 
94FB: 90 F5           BCC     $94F2               ; {}
94FD: 60              RTS                         
94FE: 20 C6 98        JSR     $98C6               ; {}
9501: A0 00           LDY     #$00                
9503: AD 56 7F        LDA     $7F56               
9506: 85 00           STA     $00                 ; {ram.GP_00}
9508: AD 57 7F        LDA     $7F57               
950B: 85 01           STA     $01                 
950D: B1 00           LDA     ($00),Y             ; {ram.GP_00}
950F: C9 FF           CMP     #$FF                
9511: F0 0B           BEQ     $951E               ; {}
9513: CD 30 01        CMP     $0130               
9516: F0 07           BEQ     $951F               ; {}
9518: C8              INY                         
9519: C8              INY                         
951A: C8              INY                         
951B: C8              INY                         
951C: D0 EF           BNE     $950D               ; {}
951E: 60              RTS                         
951F: C8              INY                         
9520: B1 00           LDA     ($00),Y             ; {ram.GP_00}
9522: CD D1 04        CMP     $04D1               
9525: D0 F2           BNE     $9519               ; {}
9527: 98              TYA                         
9528: 48              PHA                         
9529: C8              INY                         
952A: C8              INY                         
952B: B1 00           LDA     ($00),Y             ; {ram.GP_00}
952D: 48              PHA                         
952E: 88              DEY                         
952F: B1 00           LDA     ($00),Y             ; {ram.GP_00}
9531: A8              TAY                         
9532: A9 50           LDA     #$50                
9534: 91 62           STA     ($62),Y             
9536: 98              TYA                         
9537: 18              CLC                         
9538: 69 10           ADC     #$10                
953A: A8              TAY                         
953B: 68              PLA                         
953C: 91 62           STA     ($62),Y             
953E: 68              PLA                         
953F: A8              TAY                         
9540: 4C 19 95        JMP     $9519               ; {}
9543: 20 C6 98        JSR     $98C6               ; {}
9546: 20 8A 96        JSR     $968A               ; {}
9549: 4C 98 96        JMP     $9698               ; {}
954C: 20 C6 98        JSR     $98C6               ; {}
954F: A2 00           LDX     #$00                
9551: BC 04 01        LDY     $0104,X             
9554: D0 18           BNE     $956E               ; {}
9556: AC E2 04        LDY     $04E2               
9559: C0 F0           CPY     #$F0                
955B: 90 09           BCC     $9566               ; {}
955D: 20 8D 95        JSR     $958D               ; {}
9560: A9 00           LDA     #$00                
9562: 8D 04 01        STA     $0104               
9565: 60              RTS                         
9566: A9 00           LDA     #$00                
9568: 8D 04 01        STA     $0104               
956B: 4C 42 EE        JMP     $EE42               
956E: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
9571: BD 06 01        LDA     $0106,X             
9574: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
9577: BD 05 01        LDA     $0105,X             
957A: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
957D: BD 07 01        LDA     $0107,X             
9580: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
9583: E8              INX                         
9584: 88              DEY                         
9585: D0 F6           BNE     $957D               ; {}
9587: E8              INX                         
9588: E8              INX                         
9589: E8              INX                         
958A: 4C 51 95        JMP     $9551               ; {}
958D: C0 FF           CPY     #$FF                
958F: D0 18           BNE     $95A9               ; {}
9591: A2 20           LDX     #$20                
9593: A5 3A           LDA     $3A                 
9595: C9 10           CMP     #$10                
9597: 90 02           BCC     $959B               ; {}
9599: A2 28           LDX     #$28                
959B: 86 00           STX     $00                 ; {ram.GP_00}
959D: A0 C8           LDY     #$C8                
959F: 20 BD 95        JSR     $95BD               ; {}
95A2: A6 00           LDX     $00                 ; {ram.GP_00}
95A4: E8              INX                         
95A5: A0 08           LDY     #$08                
95A7: D0 14           BNE     $95BD               ; {}
95A9: AE 06 01        LDX     $0106               
95AC: AC 05 01        LDY     $0105               
95AF: 20 BD 95        JSR     $95BD               ; {}
95B2: 98              TYA                         
95B3: 18              CLC                         
95B4: 69 40           ADC     #$40                
95B6: A8              TAY                         
95B7: AD 06 01        LDA     $0106               
95BA: 69 00           ADC     #$00                
95BC: AA              TAX                         
95BD: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
95C0: 8E 06 20        STX     $2006               ; {hard.P_VRAM_ADDR}
95C3: 8C 06 20        STY     $2006               ; {hard.P_VRAM_ADDR}
95C6: A2 16           LDX     #$16                
95C8: A9 12           LDA     #$12                
95CA: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
95CD: CA              DEX                         
95CE: D0 FA           BNE     $95CA               ; {}
95D0: 8E E2 04        STX     $04E2               
95D3: 60              RTS                         
95D4: AD E2 04        LDA     $04E2               
95D7: F0 26           BEQ     $95FF               ; {}
95D9: 30 24           BMI     $95FF               ; {}
95DB: EE E3 04        INC     $04E3               
95DE: AD E3 04        LDA     $04E3               
95E1: 29 07           AND     #$07                
95E3: D0 1A           BNE     $95FF               ; {}
95E5: AC E4 04        LDY     $04E4               
95E8: D0 03           BNE     $95ED               ; {}
95EA: 20 A1 96        JSR     $96A1               ; {}
95ED: 20 CC 96        JSR     $96CC               ; {}
95F0: C9 FC           CMP     #$FC                
95F2: B0 0C           BCS     $9600               ; {}
95F4: 20 EC 96        JSR     $96EC               ; {}
95F7: EE E4 04        INC     $04E4               
95FA: A9 01           LDA     #$01                
95FC: 8D 81 03        STA     $0381               
95FF: 60              RTS                         
9600: D0 04           BNE     $9606               ; {}
9602: 20 1A 96        JSR     $961A               ; {}
9605: 60              RTS                         
9606: C9 FD           CMP     #$FD                
9608: D0 03           BNE     $960D               ; {}
960A: 4C 42 96        JMP     $9642               ; {}
960D: C9 FE           CMP     #$FE                
960F: D0 06           BNE     $9617               ; {}
9611: 20 65 96        JSR     $9665               ; {}
9614: 4C ED 95        JMP     $95ED               ; {}
9617: 4C 8A 96        JMP     $968A               ; {}
961A: AD E5 04        LDA     $04E5               
961D: D0 0C           BNE     $962B               ; {}
961F: EE E4 04        INC     $04E4               
9622: 20 CC 96        JSR     $96CC               ; {}
9625: 8D E6 04        STA     $04E6               
9628: CE E4 04        DEC     $04E4               
962B: EE E5 04        INC     $04E5               
962E: AD E5 04        LDA     $04E5               
9631: CD E6 04        CMP     $04E6               
9634: 90 0B           BCC     $9641               ; {}
9636: A9 00           LDA     #$00                
9638: 8D E5 04        STA     $04E5               
963B: 8D E6 04        STA     $04E6               
963E: EE E4 04        INC     $04E4               
9641: 60              RTS                         
9642: AD E5 04        LDA     $04E5               
9645: D0 03           BNE     $964A               ; {}
9647: 20 B5 96        JSR     $96B5               ; {}
964A: 20 DC 96        JSR     $96DC               ; {}
964D: 20 EC 96        JSR     $96EC               ; {}
9650: EE E5 04        INC     $04E5               
9653: CE E6 04        DEC     $04E6               
9656: D0 0C           BNE     $9664               ; {}
9658: 20 98 96        JSR     $9698               ; {}
965B: AD E4 04        LDA     $04E4               
965E: 18              CLC                         
965F: 69 04           ADC     #$04                
9661: 8D E4 04        STA     $04E4               
9664: 60              RTS                         
9665: EE E4 04        INC     $04E4               
9668: 20 CC 96        JSR     $96CC               ; {}
966B: 8D 05 01        STA     $0105               
966E: EE E4 04        INC     $04E4               
9671: 20 CC 96        JSR     $96CC               ; {}
9674: 8D 06 01        STA     $0106               
9677: EE E4 04        INC     $04E4               
967A: A5 3A           LDA     $3A                 
967C: C9 10           CMP     #$10                
967E: 90 09           BCC     $9689               ; {}
9680: AD 06 01        LDA     $0106               
9683: 18              CLC                         
9684: 69 08           ADC     #$08                
9686: 8D 06 01        STA     $0106               
9689: 60              RTS                         
968A: A9 00           LDA     #$00                
968C: 8D E2 04        STA     $04E2               
968F: 8D E3 04        STA     $04E3               
9692: 8D E4 04        STA     $04E4               
9695: 8D 04 01        STA     $0104               
9698: A9 00           LDA     #$00                
969A: 8D E5 04        STA     $04E5               
969D: 8D E6 04        STA     $04E6               
96A0: 60              RTS                         
96A1: AE E2 04        LDX     $04E2               
96A4: CA              DEX                         
96A5: 8A              TXA                         
96A6: 0A              ASL     A                   
96A7: AA              TAX                         
96A8: BD 02 97        LDA     $9702,X             ; {}
96AB: 8D E7 04        STA     $04E7               
96AE: BD 03 97        LDA     $9703,X             ; {}
96B1: 8D E8 04        STA     $04E8               
96B4: 60              RTS                         
96B5: 84 02           STY     $02                 
96B7: C8              INY                         
96B8: B1 00           LDA     ($00),Y             ; {ram.GP_00}
96BA: 8D E6 04        STA     $04E6               
96BD: C8              INY                         
96BE: B1 00           LDA     ($00),Y             ; {ram.GP_00}
96C0: 8D E9 04        STA     $04E9               
96C3: C8              INY                         
96C4: B1 00           LDA     ($00),Y             ; {ram.GP_00}
96C6: 8D EA 04        STA     $04EA               
96C9: A4 02           LDY     $02                 
96CB: 60              RTS                         
96CC: AD E7 04        LDA     $04E7               
96CF: 85 00           STA     $00                 ; {ram.GP_00}
96D1: AD E8 04        LDA     $04E8               
96D4: 85 01           STA     $01                 
96D6: AC E4 04        LDY     $04E4               
96D9: B1 00           LDA     ($00),Y             ; {ram.GP_00}
96DB: 60              RTS                         
96DC: AD E9 04        LDA     $04E9               
96DF: 85 00           STA     $00                 ; {ram.GP_00}
96E1: AD EA 04        LDA     $04EA               
96E4: 85 01           STA     $01                 
96E6: AC E5 04        LDY     $04E5               
96E9: B1 00           LDA     ($00),Y             ; {ram.GP_00}
96EB: 60              RTS                         
96EC: EE 05 01        INC     $0105               
96EF: D0 03           BNE     $96F4               ; {}
96F1: EE 06 01        INC     $0106               
96F4: 8D 07 01        STA     $0107               
96F7: A9 01           LDA     #$01                
96F9: 8D 04 01        STA     $0104               
96FC: A9 00           LDA     #$00                
96FE: 8D 08 01        STA     $0108               
9701: 60              RTS                         
9702: 1E 97 46        ASL     $4697,X             
9705: 97 ; ????
9706: 6F ; ????
9707: 97 ; ????
9708: 80 ; ????
9709: 97 ; ????
970A: A4 97           LDY     $97                 
970C: CD 97 E5        CMP     $E597               
970F: 97 ; ????
9710: 08              PHP                         
9711: 98              TYA                         
9712: 20 98 49        JSR     $4998               
9715: 98              TYA                         
9716: 75 98           ADC     $98,X               
9718: 92 ; ????
9719: 98              TYA                         
971A: B9 98 00        LDA     $0098,Y             
971D: 61 FE           ADC     ($FE,X)             
971F: C8              INY                         
9720: 20 10 1C        JSR     $1C10               
9723: 21 16           AND     ($16,X)             
9725: 19 12 2E        ORA     $2E12,Y             
9728: 24 2A           BIT     $2A                 
972A: 12 ; ????
972B: 18              CLC                         
972C: 16 22           ASL     $22,X               
972E: 1A ; ????
972F: FD 07 20        SBC     $2007,X             ; {hard.P_VRAM_DATA}
9732: 01 FE           ORA     ($FE,X)             
9734: 08              PHP                         
9735: 21 1D           AND     ($1D,X)             
9737: 1A ; ????
9738: 27 ; ????
9739: 1A ; ????
973A: 0C ; ????
973B: 29 16           AND     #$16                
973D: 20 1A 12        JSR     $121A               
9740: 29 1D           AND     #$1D                
9742: 1E 28 0E        ASL     $0E28,X             
9745: FF ; ????
9746: FE C8 20        INC     $20C8,X             
9749: 18              CLC                         
974A: 16 23           ASL     $23,X               
974C: 12 ; ????
974D: 2E 24 2A        ROL     $2A24               
9750: 12 ; ????
9751: 1A ; ????
9752: 23 ; ????
9753: 19 2A 27        ORA     $272A,Y             
9756: 1A ; ????
9757: FE 08 21        INC     $2108,X             
975A: 29 1D           AND     #$1D                
975C: 1E 28 12        ASL     $1228,X             
975F: 1D 16 27        ORA     $2716,X             
9762: 28              PLP                         
9763: 1D 12 29        ORA     $2912,X             
9766: 27 ; ????
9767: 16 1E           ASL     $1E,X               
9769: 23 ; ????
976A: 1E 23 1C        ASL     $1C23,X             
976D: 0A              ASL     A                   
976E: FF ; ????
976F: FE C8 20        INC     $20C8,X             
9772: 2E 24 2A        ROL     $2A24               
9775: 12 ; ????
9776: 2C 1A 16        BIT     $161A               
9779: 20 21 1E        JSR     $1E21               
977C: 23 ; ????
977D: 1C ; ????
977E: 0E FF FE        ASL     $FEFF               
9781: C8              INY                         
9782: 20 2C 1A        JSR     $1A2C               
9785: 21 21           AND     ($21,X)             
9787: 12 ; ????
9788: 19 24 23        ORA     $2324,Y             
978B: 1A ; ????
978C: FD 06 20        SBC     $2006,X             ; {hard.P_VRAM_ADDR}
978F: 01 0E           ORA     ($0E,X)             
9791: FE 08 21        INC     $2108,X             
9794: 29 16           AND     #$16                
9796: 20 1A 12        JSR     $121A               
9799: 2E 24 2A        ROL     $2A24               
979C: 27 ; ????
979D: 12 ; ????
979E: 25 1E           AND     $1E                 
97A0: 18              CLC                         
97A1: 20 0D FF        JSR     $FF0D               
97A4: FE C8 20        INC     $20C8,X             
97A7: 22 ; ????
97A8: 16 2E           ASL     $2E,X               
97AA: 12 ; ????
97AB: 1E 12 1D        ASL     $1D12,X             
97AE: 1A ; ????
97AF: 21 25           AND     ($25,X)             
97B1: 12 ; ????
97B2: 2E 24 2A        ROL     $2A24               
97B5: 0A              ASL     A                   
97B6: FE 08 21        INC     $2108,X             
97B9: 2C 1A 12        BIT     $121A               
97BC: 1D 16 2B        ORA     $2B16,X             
97BF: 1A ; ????
97C0: 12 ; ????
97C1: 1A ; ????
97C2: 2B ; ????
97C3: 1A ; ????
97C4: 27 ; ????
97C5: 2E 29 1D        ROL     $1D29               
97C8: 1E 23 1C        ASL     $1C23,X             
97CB: 0D FF FE        ORA     $FEFF               
97CE: C8              INY                         
97CF: 20 1E 12        JSR     $121E               
97D2: 1C ; ????
97D3: 2A              ROL     A                   
97D4: 1A ; ????
97D5: 28              PLP                         
97D6: 28              PLP                         
97D7: 12 ; ????
97D8: 1E 12 18        ASL     $1812,X             
97DB: 16 23           ASL     $23,X               
97DD: 10 29           BPL     $9808               ; {}
97DF: 12 ; ????
97E0: 2C 1E 23        BIT     $231E               
97E3: 0E FF FE        ASL     $FEFF               
97E6: C8              INY                         
97E7: 20 1C 24        JSR     $241C               
97EA: 12 ; ????
97EB: 24 23           BIT     $23                 
97ED: 0E 12 2C        ASL     $2C12               
97F0: 1D 24 12        ORA     $1224,X             
97F3: 19 24 12        ORA     $1224,Y             
97F6: 2E 24 2A        ROL     $2A24               
97F9: FE 08 21        INC     $2108,X             
97FC: 29 1D           AND     #$1D                
97FE: 1E 23 20        ASL     $2023,X             
9801: 12 ; ????
9802: 1E 12 16        ASL     $1612,X             
9805: 22 ; ????
9806: 0A              ASL     A                   
9807: FF ; ????
9808: FE C8 20        INC     $20C8,X             
980B: 29 1D           AND     #$1D                
980D: 16 23           ASL     $23,X               
980F: 20 0F 2E        JSR     $2E0F               
9812: 24 2A           BIT     $2A                 
9814: 12 ; ????
9815: 2B ; ????
9816: 1A ; ????
9817: 27 ; ????
9818: 2E 12 22        ROL     $2212               
981B: 2A              ROL     A                   
981C: 18              CLC                         
981D: 1D 0D FF        ORA     $FF0D,X             
9820: FE C8 20        INC     $20C8,X             
9823: 2C 1D 16        BIT     $161D               
9826: 29 12           AND     #$12                
9828: 19 24 12        ORA     $1224,Y             
982B: 2E 16 12        ROL     $1216               
982E: 28              PLP                         
982F: 16 2E           ASL     $2E,X               
9831: 0E FE 08        ASL     $08FE               
9834: 21 29           AND     ($29,X)             
9836: 27 ; ????
9837: 2E 12 17        ROL     $1712               
983A: 2A              ROL     A                   
983B: 2E 1E 23        ROL     $231E               
983E: 1C ; ????
983F: 12 ; ????
9840: 1B ; ????
9841: 27 ; ????
9842: 24 22           BIT     $22                 
9844: 12 ; ????
9845: 22 ; ????
9846: 1A ; ????
9847: 0D FF FE        ORA     $FEFF               
984A: C8              INY                         
984B: 20 24 20        JSR     $2024               
984E: 12 ; ????
984F: 20 1E 19        JSR     $191E               
9852: 0C ; ????
9853: 1E 10 21        ASL     $2110,X             
9856: 21 12           AND     ($12,X)             
9858: 21 1A           AND     ($1A,X)             
985A: 29 12           AND     #$12                
985C: 2E 24 2A        ROL     $2A24               
985F: FE 08 21        INC     $2108,X             
9862: 1D 16 2B        ORA     $2B16,X             
9865: 1A ; ????
9866: 12 ; ????
9867: 1E 29 12        ASL     $1229,X             
986A: 24 23           BIT     $23                 
986C: 12 ; ????
986D: 18              CLC                         
986E: 27 ; ????
986F: 1A ; ????
9870: 19 1E 29        ORA     $291E,Y             
9873: 0D FF FE        ORA     $FEFF               
9876: C8              INY                         
9877: 20 1D 16        JSR     $161D               
987A: 0C ; ????
987B: 1D 16 0C        ORA     $0C16,X             
987E: 1D 16 0C        ORA     $0C16,X             
9881: FE 08 21        INC     $2108,X             
9884: 29 1D           AND     #$1D                
9886: 16 23           ASL     $23,X               
9888: 20 28 12        JSR     $1228               
988B: 16 12           ASL     $12,X               
988D: 21 24           AND     ($24,X)             
988F: 29 0D           AND     #$0D                
9891: FF ; ????
9892: FE C8 20        INC     $20C8,X             
9895: 21 1A           AND     ($1A,X)             
9897: 29 12           AND     #$12                
9899: 22 ; ????
989A: 1A ; ????
989B: 12 ; ????
989C: 27 ; ????
989D: 1A ; ????
989E: 22 ; ????
989F: 24 2B           BIT     $2B                 
98A1: 1A ; ????
98A2: FE 08 21        INC     $2108,X             
98A5: 29 1D           AND     #$1D                
98A7: 1A ; ????
98A8: 12 ; ????
98A9: 1A ; ????
98AA: 1C ; ????
98AB: 1C ; ????
98AC: 25 21           AND     $21                 
98AE: 16 23           ASL     $23,X               
98B0: 29 12           AND     #$12                
98B2: 18              CLC                         
98B3: 2A              ROL     A                   
98B4: 27 ; ????
98B5: 28              PLP                         
98B6: 1A ; ????
98B7: 0D FF FE        ORA     $FEFF               
98BA: CC 29 25        CPY     $2529               
98BD: 24 2C           BIT     $2C                 
98BF: 1A ; ????
98C0: 27 ; ????
98C1: 12 ; ????
98C2: 2A              ROL     A                   
98C3: 25 0E           AND     $0E                 
98C5: FF ; ????
98C6: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
98C9: AD 00 01        LDA     $0100               
98CC: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
98CF: 60              RTS                         
98D0: A5 A0           LDA     $A0                 
98D2: C9 02           CMP     #$02                
98D4: 90 F9           BCC     $98CF               ; {}
98D6: 4A              LSR     A                   
98D7: B0 32           BCS     $990B               ; {}
98D9: 4A              LSR     A                   
98DA: 90 F3           BCC     $98CF               ; {}
98DC: C9 02           CMP     #$02                
98DE: B0 EF           BCS     $98CF               ; {}
98E0: 0A              ASL     A                   
98E1: AA              TAX                         
98E2: BD 07 99        LDA     $9907,X             ; {}
98E5: 85 00           STA     $00                 ; {ram.GP_00}
98E7: BD 08 99        LDA     $9908,X             ; {}
98EA: 85 01           STA     $01                 
98EC: A9 00           LDA     #$00                
98EE: 85 02           STA     $02                 
98F0: A9 70           LDA     #$70                
98F2: 85 03           STA     $03                 
98F4: A2 0F           LDX     #$0F                
98F6: A0 00           LDY     #$00                
98F8: B1 00           LDA     ($00),Y             ; {ram.GP_00}
98FA: 91 02           STA     ($02),Y             
98FC: C8              INY                         
98FD: D0 F9           BNE     $98F8               ; {}
98FF: E6 01           INC     $01                 
9901: E6 03           INC     $03                 
9903: CA              DEX                         
9904: D0 F2           BNE     $98F8               ; {}
9906: 60              RTS                         
9907: 40              RTI                         
9908: 99 90 A7        STA     $A790,Y             ; {}
990B: C9 04           CMP     #$04                
990D: B0 C0           BCS     $98CF               ; {}
990F: 0A              ASL     A                   
9910: AA              TAX                         
9911: BD 1C 99        LDA     $991C,X             ; {}
9914: 85 00           STA     $00                 ; {ram.GP_00}
9916: BD 1D 99        LDA     $991D,X             ; {}
9919: 85 01           STA     $01                 
991B: 4C EC 98        JMP     $98EC               ; {}
991E: F9 B0 ED        SBC     $EDB0,Y             
9921: B3 ; ????
9922: C1 B6           CMP     ($B6,X)             
9924: 85 C8           STA     $C8                 
9926: A9 C4           LDA     #$C4                
9928: 48              PHA                         
9929: A9 CC           LDA     #$CC                
992B: 48              PHA                         
992C: A5 C8           LDA     $C8                 
992E: 20 F7 CA        JSR     $CAF7               
9931: 60              RTS                         
9932: 85 C8           STA     $C8                 
9934: A9 C6           LDA     #$C6                
9936: 48              PHA                         
9937: A9 66           LDA     #$66                
9939: 48              PHA                         
993A: A5 C8           LDA     $C8                 
993C: 20 F7 CA        JSR     $CAF7               
993F: 60              RTS                         
9940: 00              BRK                         
9941: 46 14           LSR     $14                 
9943: 02 ; ????
9944: 54 ; ????
9945: 09 00           ORA     #$00                
9947: 5C ; ????
9948: 09 00           ORA     #$00                
994A: 60              RTS                         
994B: 09 00           ORA     #$00                
994D: 68              PLA                         
994E: 09 00           ORA     #$00                
9950: 6B ; ????
9951: 26 00           ROL     $00                 ; {ram.GP_00}
9953: 77 ; ????
9954: 26 00           ROL     $00                 ; {ram.GP_00}
9956: 7B ; ????
9957: 26 00           ROL     $00                 ; {ram.GP_00}
9959: 7D 09 00        ADC     $0009,X             
995C: 80 ; ????
995D: 08              PHP                         
995E: 00              BRK                         
995F: 9E ; ????
9960: 24 00           BIT     $00                 ; {ram.GP_00}
9962: 9F ; ????
9963: 09 00           ORA     #$00                
9965: B4 09           LDY     $09,X               
9967: 00              BRK                         
9968: B8              CLV                         
9969: 09 00           ORA     #$00                
996B: BC 09 00        LDY     $0009,X             
996E: C0 08           CPY     #$08                
9970: 00              BRK                         
9971: C3 ; ????
9972: 08              PHP                         
9973: 00              BRK                         
9974: D1 08           CMP     ($08),Y             
9976: 00              BRK                         
9977: FD FF 00        SBC     $00FF,X             
997A: 50 09           BVC     $9985               ; {}
997C: 00              BRK                         
997D: 54 ; ????
997E: 09 00           ORA     #$00                
9980: 58              CLI                         
9981: 09 00           ORA     #$00                
9983: 5C ; ????
9984: 14 ; ????
9985: 02 ; ????
9986: 68              PLA                         
9987: 27 ; ????
9988: 01 6C           ORA     ($6C,X)             
998A: 27 ; ????
998B: 01 70           ORA     ($70,X)             
998D: 09 00           ORA     #$00                
998F: 7A ; ????
9990: 26 00           ROL     $00                 ; {ram.GP_00}
9992: 7C ; ????
9993: 26 00           ROL     $00                 ; {ram.GP_00}
9995: 7E 09 00        ROR     $0009,X             
9998: 90 08           BCC     $99A2               ; {}
999A: 00              BRK                         
999B: 91 26           STA     ($26),Y             
999D: 00              BRK                         
999E: 9E ; ????
999F: 24 00           BIT     $00                 ; {ram.GP_00}
99A1: 9F ; ????
99A2: 09 00           ORA     #$00                
99A4: B6 09           LDX     $09,Y               
99A6: 00              BRK                         
99A7: B8              CLV                         
99A8: 09 00           ORA     #$00                
99AA: BC 09 00        LDY     $0009,X             
99AD: C2 ; ????
99AE: 14 ; ????
99AF: 03 ; ????
99B0: D0 09           BNE     $99BB               ; {}
99B2: 00              BRK                         
99B3: D9 09 00        CMP     $0009,Y             
99B6: FD FF 00        SBC     $00FF,X             
99B9: 20 09 00        JSR     $0009               
99BC: 26 14           ROL     $14                 
99BE: 02 ; ????
99BF: 34 ; ????
99C0: 09 00           ORA     #$00                
99C2: 40              RTI                         
99C3: 08              PHP                         
99C4: 00              BRK                         
99C5: 48              PHA                         
99C6: 09 00           ORA     #$00                
99C8: 55 26           EOR     $26,X               
99CA: 00              BRK                         
99CB: 5C ; ????
99CC: 09 00           ORA     #$00                
99CE: 69 26           ADC     #$26                
99D0: 00              BRK                         
99D1: 6B ; ????
99D2: 26 00           ROL     $00                 ; {ram.GP_00}
99D4: 7E 09 00        ROR     $0009,X             
99D7: 80 ; ????
99D8: 08              PHP                         
99D9: 00              BRK                         
99DA: 94 09           STY     $09,X               
99DC: 00              BRK                         
99DD: 9E ; ????
99DE: 24 00           BIT     $00                 ; {ram.GP_00}
99E0: 9F ; ????
99E1: 09 00           ORA     #$00                
99E3: A8              TAY                         
99E4: 09 00           ORA     #$00                
99E6: B1 08           LDA     ($08),Y             
99E8: 00              BRK                         
99E9: BC 09 00        LDY     $0009,X             
99EC: C0 08           CPY     #$08                
99EE: 00              BRK                         
99EF: D8              CLD                         
99F0: 14 ; ????
99F1: 00              BRK                         
99F2: DD 09 00        CMP     $0009,X             
99F5: E2 ; ????
99F6: 09 00           ORA     #$00                
99F8: E6 09           INC     $09                 
99FA: 00              BRK                         
99FB: FD FF 01        SBC     $01FF,X             
99FE: 00              BRK                         
99FF: 1A ; ????
9A00: 01 02           ORA     ($02,X)             
9A02: 06 03           ASL     $03                 
9A04: 0E 1A 01        ASL     $011A               
9A07: 12 ; ????
9A08: 0B ; ????
9A09: 03 ; ????
9A0A: 22 ; ????
9A0B: 0F ; ????
9A0C: 02 ; ????
9A0D: 36 14           ROL     $14,X               
9A0F: 02 ; ????
9A10: 40              RTI                         
9A11: 1A ; ????
9A12: 01 46           ORA     ($46,X)             
9A14: 0B ; ????
9A15: 03 ; ????
9A16: 4E 1A 01        LSR     $011A               
9A19: 58              CLI                         
9A1A: 0C ; ????
9A1B: 02 ; ????
9A1C: 72 ; ????
9A1D: 03 ; ????
9A1E: 03 ; ????
9A1F: 76 05           ROR     $05,X               
9A21: 01 79           ORA     ($79,X)             
9A23: 14 ; ????
9A24: 02 ; ????
9A25: 80 ; ????
9A26: 1A ; ????
9A27: 01 87           ORA     ($87,X)             
9A29: 03 ; ????
9A2A: 03 ; ????
9A2B: 8E 1A 01        STX     $011A               
9A2E: 91 25           STA     ($25),Y             
9A30: 00              BRK                         
9A31: 96 0C           STX     $0C,Y               
9A33: 02 ; ????
9A34: 9A              TXS                         
9A35: 0C ; ????
9A36: 02 ; ????
9A37: B1 03           LDA     ($03),Y             
9A39: 03 ; ????
9A3A: BC 19 01        LDY     $0119,X             
9A3D: C0 19           CPY     #$19                
9A3F: 01 C4           ORA     ($C4,X)             
9A41: 0B ; ????
9A42: 03 ; ????
9A43: D4 ; ????
9A44: 19 01 D8        ORA     $D801,Y             
9A47: 19 01 FD        ORA     $FD01,Y             
9A4A: FF ; ????
9A4B: 01 0C           ORA     ($0C,X)             
9A4D: 03 ; ????
9A4E: 03 ; ????
9A4F: 19 14 02        ORA     $0214,Y             
9A52: 1C ; ????
9A53: 05 01           ORA     $01                 
9A55: 29 03           AND     #$03                
9A57: 03 ; ????
9A58: 39 05 01        AND     $0105,Y             
9A5B: 46 03           LSR     $03                 
9A5D: 03 ; ????
9A5E: 56 05           LSR     $05,X               
9A60: 01 63           ORA     ($63,X)             
9A62: 03 ; ????
9A63: 03 ; ????
9A64: 73 ; ????
9A65: 05 01           ORA     $01                 
9A67: 75 0F           ADC     $0F,X               
9A69: 02 ; ????
9A6A: 8B ; ????
9A6B: 07 ; ????
9A6C: 00              BRK                         
9A6D: 90 19           BCC     $9A88               ; {}
9A6F: 01 9E           ORA     ($9E,X)             
9A71: 19 01 C8        ORA     $C801,Y             
9A74: 0B ; ????
9A75: 03 ; ????
9A76: D3 ; ????
9A77: 04 ; ????
9A78: 01 D5           ORA     ($D5,X)             
9A7A: 06 03           ASL     $03                 
9A7C: FD FF 01        SBC     $01FF,X             
9A7F: 02 ; ????
9A80: 05 01           ORA     $01                 
9A82: 13 ; ????
9A83: 03 ; ????
9A84: 03 ; ????
9A85: 25 05           AND     $05                 
9A87: 01 36           ORA     ($36,X)             
9A89: 03 ; ????
9A8A: 03 ; ????
9A8B: 3E 0D 02        ROL     $020D,X             
9A8E: 48              PHA                         
9A8F: 05 01           ORA     $01                 
9A91: 54 ; ????
9A92: 0D 02 59        ORA     $5902               
9A95: 03 ; ????
9A96: 03 ; ????
9A97: 61 14           ADC     ($14,X)             
9A99: 02 ; ????
9A9A: 6B ; ????
9A9B: 05 01           ORA     $01                 
9A9D: 70 03           BVS     $9AA2               ; {}
9A9F: 03 ; ????
9AA0: 7C ; ????
9AA1: 03 ; ????
9AA2: 03 ; ????
9AA3: 82 ; ????
9AA4: 05 01           ORA     $01                 
9AA6: 8F ; ????
9AA7: 04 ; ????
9AA8: 01 93           ORA     ($93,X)             
9AAA: 03 ; ????
9AAB: 03 ; ????
9AAC: A5 05           LDA     $05                 
9AAE: 01 A8           ORA     ($A8,X)             
9AB0: 14 ; ????
9AB1: 02 ; ????
9AB2: B6 03           LDX     $03,Y               
9AB4: 03 ; ????
9AB5: BF ; ????
9AB6: 04 ; ????
9AB7: 01 C8           ORA     ($C8,X)             
9AB9: 0F ; ????
9ABA: 02 ; ????
9ABB: C9 05           CMP     #$05                
9ABD: 01 FD           ORA     ($FD,X)             
9ABF: FF ; ????
9AC0: 01 06           ORA     ($06,X)             
9AC2: 00              BRK                         
9AC3: 01 0A           ORA     ($0A,X)             
9AC5: 01 01           ORA     ($01,X)             
9AC7: 33 ; ????
9AC8: 07 ; ????
9AC9: 00              BRK                         
9ACA: 35 00           AND     $00,X               ; {ram.GP_00}
9ACC: 01 36           ORA     ($36,X)             
9ACE: 02 ; ????
9ACF: 01 63           ORA     ($63,X)             
9AD1: 02 ; ????
9AD2: 01 69           ORA     ($69,X)             
9AD4: 02 ; ????
9AD5: 01 97           ORA     ($97,X)             
9AD7: 01 01           ORA     ($01,X)             
9AD9: 9B ; ????
9ADA: 02 ; ????
9ADB: 01 C5           ORA     ($C5,X)             
9ADD: 01 01           ORA     ($01,X)             
9ADF: C9 01           CMP     #$01                
9AE1: 01 FD           ORA     ($FD,X)             
9AE3: FF ; ????
9AE4: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9AE6: 04 ; ????
9AE7: 01 03           ORA     ($03,X)             
9AE9: 04 ; ????
9AEA: 01 04           ORA     ($04,X)             
9AEC: 17 ; ????
9AED: 02 ; ????
9AEE: 0F ; ????
9AEF: 16 02           ASL     $02,X               
9AF1: 22 ; ????
9AF2: 00              BRK                         
9AF3: 01 29           ORA     ($29,X)             
9AF5: 17 ; ????
9AF6: 02 ; ????
9AF7: 33 ; ????
9AF8: 04 ; ????
9AF9: 01 40           ORA     ($40,X)             
9AFB: 04 ; ????
9AFC: 01 4E           ORA     ($4E,X)             
9AFE: 16 02           ASL     $02,X               
9B00: 51 00           EOR     ($00),Y             ; {ram.GP_00}
9B02: 01 65           ORA     ($65,X)             
9B04: 07 ; ????
9B05: 00              BRK                         
9B06: 68              PLA                         
9B07: 14 ; ????
9B08: 02 ; ????
9B09: 73 ; ????
9B0A: 04 ; ????
9B0B: 01 77           ORA     ($77,X)             
9B0D: 1A ; ????
9B0E: 01 78           ORA     ($78,X)             
9B10: 17 ; ????
9B11: 02 ; ????
9B12: 7C ; ????
9B13: 17 ; ????
9B14: 02 ; ????
9B15: 82 ; ????
9B16: 00              BRK                         
9B17: 01 A5           ORA     ($A5,X)             
9B19: 01 01           ORA     ($01,X)             
9B1B: B0 19           BCS     $9B36               ; {}
9B1D: 01 B7           ORA     ($B7,X)             
9B1F: 1A ; ????
9B20: 01 BE           ORA     ($BE,X)             
9B22: 19 01 CC        ORA     $CC01,Y             
9B25: 01 01           ORA     ($01,X)             
9B27: D4 ; ????
9B28: 01 01           ORA     ($01,X)             
9B2A: FD FF 01        SBC     $01FF,X             
9B2D: 00              BRK                         
9B2E: 04 ; ????
9B2F: 01 03           ORA     ($03,X)             
9B31: 04 ; ????
9B32: 01 0A           ORA     ($0A,X)             
9B34: 17 ; ????
9B35: 02 ; ????
9B36: 0E 16 02        ASL     $0216               
9B39: 21 00           AND     ($00,X)             ; {ram.GP_00}
9B3B: 01 30           ORA     ($30,X)             
9B3D: 04 ; ????
9B3E: 01 33           ORA     ($33,X)             
9B40: 04 ; ????
9B41: 01 35           ORA     ($35,X)             
9B43: 17 ; ????
9B44: 02 ; ????
9B45: 4E 19 01        LSR     $0119               
9B48: 52 ; ????
9B49: 00              BRK                         
9B4A: 01 56           ORA     ($56,X)             
9B4C: 1E 02 66        ASL     $6602,X             
9B4F: 07 ; ????
9B50: 00              BRK                         
9B51: 69 17           ADC     #$17                
9B53: 02 ; ????
9B54: 70 04           BVS     $9B5A               ; {}
9B56: 01 73           ORA     ($73,X)             
9B58: 04 ; ????
9B59: 01 7E           ORA     ($7E,X)             
9B5B: 16 02           ASL     $02,X               
9B5D: 81 00           STA     ($00,X)             ; {ram.GP_00}
9B5F: 01 94           ORA     ($94,X)             
9B61: 17 ; ????
9B62: 02 ; ????
9B63: B0 04           BCS     $9B69               ; {}
9B65: 01 B2           ORA     ($B2,X)             
9B67: 00              BRK                         
9B68: 01 B3           ORA     ($B3,X)             
9B6A: 04 ; ????
9B6B: 01 BA           ORA     ($BA,X)             
9B6D: 14 ; ????
9B6E: 02 ; ????
9B6F: BF ; ????
9B70: 16 02           ASL     $02,X               
9B72: C8              INY                         
9B73: 17 ; ????
9B74: 02 ; ????
9B75: E1 00           SBC     ($00,X)             ; {ram.GP_00}
9B77: 01 FD           ORA     ($FD,X)             
9B79: FF ; ????
9B7A: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9B7C: 0B ; ????
9B7D: 03 ; ????
9B7E: 28              PLP                         
9B7F: 00              BRK                         
9B80: 01 2D           ORA     ($2D,X)             
9B82: 1E 02 36        ASL     $3602,X             
9B85: 1E 02 3D        ASL     $3D02,X             
9B88: 07 ; ????
9B89: 00              BRK                         
9B8A: 46 07           LSR     $07                 
9B8C: 00              BRK                         
9B8D: 48              PHA                         
9B8E: 00              BRK                         
9B8F: 01 70           ORA     ($70,X)             
9B91: 04 ; ????
9B92: 01 76           ORA     ($76,X)             
9B94: 02 ; ????
9B95: 01 7B           ORA     ($7B,X)             
9B97: 02 ; ????
9B98: 01 7F           ORA     ($7F,X)             
9B9A: 00              BRK                         
9B9B: 01 AB           ORA     ($AB,X)             
9B9D: 05 01           ORA     $01                 
9B9F: B0 04           BCS     $9BA5               ; {}
9BA1: 01 B7           ORA     ($B7,X)             
9BA3: 14 ; ????
9BA4: 02 ; ????
9BA5: BF ; ????
9BA6: 16 02           ASL     $02,X               
9BA8: C6 0B           DEC     $0B                 
9BAA: 03 ; ????
9BAB: D6 05           DEC     $05,X               
9BAD: 01 E3           ORA     ($E3,X)             
9BAF: 03 ; ????
9BB0: 03 ; ????
9BB1: FD FF 01        SBC     $01FF,X             
9BB4: 12 ; ????
9BB5: 18              CLC                         
9BB6: 00              BRK                         
9BB7: 35 18           AND     $18,X               
9BB9: 00              BRK                         
9BBA: 38              SEC                         
9BBB: 18              CLC                         
9BBC: 00              BRK                         
9BBD: 3B ; ????
9BBE: 18              CLC                         
9BBF: 00              BRK                         
9BC0: 42 ; ????
9BC1: 1E 02 52        ASL     $5202,X             
9BC4: 07 ; ????
9BC5: 01 68           ORA     ($68,X)             
9BC7: 1E 02 6D        ASL     $6D02,X             
9BCA: 08              PHP                         
9BCB: 00              BRK                         
9BCC: 78              SEI                         
9BCD: 07 ; ????
9BCE: 01 92           ORA     ($92,X)             
9BD0: 04 ; ????
9BD1: 01 93           ORA     ($93,X)             
9BD3: 01 01           ORA     ($01,X)             
9BD5: 95 04           STA     $04,X               
9BD7: 01 98           ORA     ($98,X)             
9BD9: 04 ; ????
9BDA: 01 9B           ORA     ($9B,X)             
9BDC: 04 ; ????
9BDD: 01 C0           ORA     ($C0,X)             
9BDF: 01 01           ORA     ($01,X)             
9BE1: FD FF 00        SBC     $00FF,X             
9BE4: 00              BRK                         
9BE5: 0B ; ????
9BE6: 03 ; ????
9BE7: 0C ; ????
9BE8: 23 ; ????
9BE9: 00              BRK                         
9BEA: 29 14           AND     #$14                
9BEC: 02 ; ????
9BED: 38              SEC                         
9BEE: 23 ; ????
9BEF: 00              BRK                         
9BF0: 48              PHA                         
9BF1: 05 01           ORA     $01                 
9BF3: 4A              LSR     A                   
9BF4: 05 01           ORA     $01                 
9BF6: 56 23           LSR     $23,X               
9BF8: 00              BRK                         
9BF9: 6A              ROR     A                   
9BFA: 0C ; ????
9BFB: 02 ; ????
9BFC: 73 ; ????
9BFD: 23 ; ????
9BFE: 00              BRK                         
9BFF: 83 ; ????
9C00: 05 01           ORA     $01                 
9C02: 90 23           BCC     $9C27               ; {}
9C04: 00              BRK                         
9C05: 9A              TXS                         
9C06: 0B ; ????
9C07: 03 ; ????
9C08: AA              TAX                         
9C09: 05 01           ORA     $01                 
9C0B: B7 ; ????
9C0C: 23 ; ????
9C0D: 00              BRK                         
9C0E: D4 ; ????
9C0F: 02 ; ????
9C10: 01 FD           ORA     ($FD,X)             
9C12: FF ; ????
9C13: 00              BRK                         
9C14: 00              BRK                         
9C15: 08              PHP                         
9C16: 00              BRK                         
9C17: 07 ; ????
9C18: 26 00           ROL     $00                 ; {ram.GP_00}
9C1A: 0F ; ????
9C1B: 08              PHP                         
9C1C: 00              BRK                         
9C1D: 12 ; ????
9C1E: 00              BRK                         
9C1F: 01 40           ORA     ($40,X)             
9C21: 09 00           ORA     #$00                
9C23: 44 ; ????
9C24: 23 ; ????
9C25: 00              BRK                         
9C26: 48              PHA                         
9C27: 14 ; ????
9C28: 02 ; ????
9C29: 4F ; ????
9C2A: 08              PHP                         
9C2B: 00              BRK                         
9C2C: 54 ; ????
9C2D: 0F ; ????
9C2E: 02 ; ????
9C2F: 57 ; ????
9C30: 23 ; ????
9C31: 00              BRK                         
9C32: 7B ; ????
9C33: 01 01           ORA     ($01,X)             
9C35: 86 1E           STX     $1E                 
9C37: 02 ; ????
9C38: 8F ; ????
9C39: 08              PHP                         
9C3A: 00              BRK                         
9C3B: 96 07           STX     $07,Y               
9C3D: 01 AD           ORA     ($AD,X)             
9C3F: 01 01           ORA     ($01,X)             
9C41: C6 1A           DEC     $1A                 
9C43: 01 C8           ORA     ($C8,X)             
9C45: 0B ; ????
9C46: 03 ; ????
9C47: FD FF 00        SBC     $00FF,X             
9C4A: 00              BRK                         
9C4B: 1A ; ????
9C4C: 01 08           ORA     ($08,X)             
9C4E: 1B ; ????
9C4F: 02 ; ????
9C50: 0A              ASL     A                   
9C51: 1B ; ????
9C52: 02 ; ????
9C53: 0E 19 01        ASL     $0119               
9C56: 30 19           BMI     $9C71               ; {}
9C58: 01 3F           ORA     ($3F,X)             
9C5A: 08              PHP                         
9C5B: 00              BRK                         
9C5C: 40              RTI                         
9C5D: 08              PHP                         
9C5E: 00              BRK                         
9C5F: 5A ; ????
9C60: 14 ; ????
9C61: 03 ; ????
9C62: 64 ; ????
9C63: 09 00           ORA     #$00                
9C65: 68              PLA                         
9C66: 09 00           ORA     #$00                
9C68: 70 09           BVS     $9C73               ; {}
9C6A: 00              BRK                         
9C6B: 7B ; ????
9C6C: 26 00           ROL     $00                 ; {ram.GP_00}
9C6E: 7F ; ????
9C6F: 08              PHP                         
9C70: 00              BRK                         
9C71: 86 26           STX     $26                 
9C73: 00              BRK                         
9C74: 8E 23 00        STX     $0023               
9C77: 90 08           BCC     $9C81               ; {}
9C79: 00              BRK                         
9C7A: 91 25           STA     ($25),Y             
9C7C: 00              BRK                         
9C7D: B1 09           LDA     ($09),Y             
9C7F: 00              BRK                         
9C80: B8              CLV                         
9C81: 09 00           ORA     #$00                
9C83: BC 09 00        LDY     $0009,X             
9C86: C4 09           CPY     $09                 
9C88: 00              BRK                         
9C89: FD FF 02        SBC     $02FF,X             
9C8C: 00              BRK                         
9C8D: 1A ; ????
9C8E: 01 02           ORA     ($02,X)             
9C90: 03 ; ????
9C91: 03 ; ????
9C92: 0A              ASL     A                   
9C93: 03 ; ????
9C94: 03 ; ????
9C95: 0E 1A 01        ASL     $011A               
9C98: 31 0D           AND     ($0D),Y             
9C9A: 02 ; ????
9C9B: 36 1B           ROL     $1B,X               
9C9D: 02 ; ????
9C9E: 3E 0D 02        ROL     $020D,X             
9CA1: 49 1B           EOR     #$1B                
9CA3: 02 ; ????
9CA4: 70 1A           BVS     $9CC0               ; {}
9CA6: 01 7D           ORA     ($7D,X)             
9CA8: 1C ; ????
9CA9: 02 ; ????
9CAA: 7E 1A 01        ROR     $011A,X             
9CAD: 86 14           STX     $14                 
9CAF: 03 ; ????
9CB0: 92 ; ????
9CB1: 1B ; ????
9CB2: 02 ; ????
9CB3: 95 03           STA     $03,X               
9CB5: 03 ; ????
9CB6: B1 0D           LDA     ($0D),Y             
9CB8: 02 ; ????
9CB9: BE 0D 02        LDX     $020D,Y             
9CBC: C9 1B           CMP     #$1B                
9CBE: 02 ; ????
9CBF: FD FF 02        SBC     $02FF,X             
9CC2: 06 1B           ASL     $1B                 
9CC4: 02 ; ????
9CC5: 32 ; ????
9CC6: 1B ; ????
9CC7: 02 ; ????
9CC8: 3A ; ????
9CC9: 1B ; ????
9CCA: 02 ; ????
9CCB: 60              RTS                         
9CCC: 1B ; ????
9CCD: 02 ; ????
9CCE: 6B ; ????
9CCF: 1B ; ????
9CD0: 02 ; ????
9CD1: 6C 1B 02        JMP     ($021B)             
9CD4: 93 ; ????
9CD5: 1B ; ????
9CD6: 02 ; ????
9CD7: 9E ; ????
9CD8: 07 ; ????
9CD9: 02 ; ????
9CDA: C0 1A           CPY     #$1A                
9CDC: 01 C7           ORA     ($C7,X)             
9CDE: 1B ; ????
9CDF: 02 ; ????
9CE0: CE 1A 01        DEC     $011A               
9CE3: FD FF 02        SBC     $02FF,X             
9CE6: 03 ; ????
9CE7: 03 ; ????
9CE8: 03 ; ????
9CE9: 05 03           ORA     $03                 
9CEB: 03 ; ????
9CEC: 19 14 03        ORA     $0314,Y             
9CEF: 28              PLP                         
9CF0: 1B ; ????
9CF1: 02 ; ????
9CF2: 40              RTI                         
9CF3: 1B ; ????
9CF4: 02 ; ????
9CF5: 44 ; ????
9CF6: 1B ; ????
9CF7: 02 ; ????
9CF8: 4C 1B 02        JMP     $021B               
9CFB: 75 1B           ADC     $1B,X               
9CFD: 02 ; ????
9CFE: 94 1C           STY     $1C,X               
9D00: 02 ; ????
9D01: 99 1B 02        STA     $021B,Y             
9D04: BC 14 03        LDY     $0314,X             
9D07: C2 ; ????
9D08: 1B ; ????
9D09: 02 ; ????
9D0A: CB ; ????
9D0B: 1B ; ????
9D0C: 02 ; ????
9D0D: FD FF 02        SBC     $02FF,X             
9D10: 00              BRK                         
9D11: 04 ; ????
9D12: 01 01           ORA     ($01,X)             
9D14: 1B ; ????
9D15: 02 ; ????
9D16: 05 1B           ORA     $1B                 
9D18: 02 ; ????
9D19: 0D 19 01        ORA     $0119               
9D1C: 33 ; ????
9D1D: 1C ; ????
9D1E: 02 ; ????
9D1F: 39 1E 02        AND     $021E,Y             
9D22: 49 07           EOR     #$07                
9D24: 01 61           ORA     ($61,X)             
9D26: 1C ; ????
9D27: 02 ; ????
9D28: 84 1C           STY     $1C                 
9D2A: 02 ; ????
9D2B: 88              DEY                         
9D2C: 1A ; ????
9D2D: 01 B9           ORA     ($B9,X)             
9D2F: 03 ; ????
9D30: 03 ; ????
9D31: C0 1B           CPY     #$1B                
9D33: 02 ; ????
9D34: CC 17 01        CPY     $0117               
9D37: FD FF 02        SBC     $02FF,X             
9D3A: 03 ; ????
9D3B: 1B ; ????
9D3C: 02 ; ????
9D3D: 26 1B           ROL     $1B                 
9D3F: 02 ; ????
9D40: 39 0F 02        AND     $020F,Y             
9D43: 49 1B           EOR     #$1B                
9D45: 02 ; ????
9D46: 5C ; ????
9D47: 0F ; ????
9D48: 02 ; ????
9D49: 60              RTS                         
9D4A: 03 ; ????
9D4B: 03 ; ????
9D4C: 6C 1B 02        JMP     ($021B)             
9D4F: 73 ; ????
9D50: 0F ; ????
9D51: 02 ; ????
9D52: 83 ; ????
9D53: 1B ; ????
9D54: 02 ; ????
9D55: 96 0F           STX     $0F,Y               
9D57: 02 ; ????
9D58: A6 03           LDX     $03                 
9D5A: 03 ; ????
9D5B: B9 0F 02        LDA     $020F,Y             
9D5E: C9 1B           CMP     #$1B                
9D60: 02 ; ????
9D61: FD FF 02        SBC     $02FF,X             
9D64: 06 1B           ASL     $1B                 
9D66: 02 ; ????
9D67: 16 0F           ASL     $0F,X               
9D69: 02 ; ????
9D6A: 23 ; ????
9D6B: 1B ; ????
9D6C: 02 ; ????
9D6D: 2A              ROL     A                   
9D6E: 22 ; ????
9D6F: 02 ; ????
9D70: 2C 22 02        BIT     $0222               
9D73: 33 ; ????
9D74: 0C ; ????
9D75: 02 ; ????
9D76: 50 1B           BVC     $9D93               ; {}
9D78: 02 ; ????
9D79: 5A ; ????
9D7A: 1B ; ????
9D7B: 02 ; ????
9D7C: 5E 1B 02        LSR     $021B,X             
9D7F: 60              RTS                         
9D80: 04 ; ????
9D81: 01 6A           ORA     ($6A,X)             
9D83: 0C ; ????
9D84: 02 ; ????
9D85: 87 ; ????
9D86: 1B ; ????
9D87: 02 ; ????
9D88: 97 ; ????
9D89: 0C ; ????
9D8A: 02 ; ????
9D8B: A0 1A           LDY     #$1A                
9D8D: 01 B4           ORA     ($B4,X)             
9D8F: 1B ; ????
9D90: 02 ; ????
9D91: D1 1B           CMP     ($1B),Y             
9D93: 02 ; ????
9D94: FD FF 02        SBC     $02FF,X             
9D97: 08              PHP                         
9D98: 1B ; ????
9D99: 02 ; ????
9D9A: 1D 07 02        ORA     $0207,X             
9D9D: 22 ; ????
9D9E: 1E 02 2E        ASL     $2E02,X             
9DA1: 1C ; ????
9DA2: 02 ; ????
9DA3: 32 ; ????
9DA4: 07 ; ????
9DA5: 02 ; ????
9DA6: 55 04           EOR     $04,X               
9DA8: 01 59           ORA     ($59,X)             
9DAA: 04 ; ????
9DAB: 01 5D           ORA     ($5D,X)             
9DAD: 04 ; ????
9DAE: 01 62           ORA     ($62,X)             
9DB0: 04 ; ????
9DB1: 01 94           ORA     ($94,X)             
9DB3: 1C ; ????
9DB4: 02 ; ????
9DB5: C4 1B           CPY     $1B                 
9DB7: 02 ; ????
9DB8: C8              INY                         
9DB9: 1C ; ????
9DBA: 02 ; ????
9DBB: FD FF 02        SBC     $02FF,X             
9DBE: 00              BRK                         
9DBF: 1D 01 0C        ORA     $0C01,X             
9DC2: 1D 01 23        ORA     $2301,X             
9DC5: 03 ; ????
9DC6: 03 ; ????
9DC7: 2C 1D 01        BIT     $011D               
9DCA: 3A ; ????
9DCB: 1C ; ????
9DCC: 02 ; ????
9DCD: 40              RTI                         
9DCE: 16 02           ASL     $02,X               
9DD0: 58              CLI                         
9DD1: 14 ; ????
9DD2: 03 ; ????
9DD3: 66 1B           ROR     $1B                 
9DD5: 02 ; ????
9DD6: 68              PLA                         
9DD7: 0B ; ????
9DD8: 03 ; ????
9DD9: 70 16           BVS     $9DF1               ; {}
9DDB: 02 ; ????
9DDC: 92 ; ????
9DDD: 1B ; ????
9DDE: 02 ; ????
9DDF: C5 1B           CMP     $1B                 
9DE1: 02 ; ????
9DE2: FD FF 02        SBC     $02FF,X             
9DE5: 02 ; ????
9DE6: 1B ; ????
9DE7: 02 ; ????
9DE8: 3C ; ????
9DE9: 06 03           ASL     $03                 
9DEB: 52 ; ????
9DEC: 1E 02 5E        ASL     $5E02,X             
9DEF: 07 ; ????
9DF0: 02 ; ????
9DF1: 62 ; ????
9DF2: 07 ; ????
9DF3: 02 ; ????
9DF4: 68              PLA                         
9DF5: 06 03           ASL     $03                 
9DF7: 90 03           BCC     $9DFC               ; {}
9DF9: 03 ; ????
9DFA: 9E ; ????
9DFB: 1A ; ????
9DFC: 01 A0           ORA     ($A0,X)             
9DFE: 04 ; ????
9DFF: 01 D0           ORA     ($D0,X)             
9E01: 16 02           ASL     $02,X               
9E03: FD FF 01        SBC     $01FF,X             
9E06: 00              BRK                         
9E07: 1D 01 0E        ORA     $0E01,X             
9E0A: 19 01 2B        ORA     $2B01,Y             
9E0D: 14 ; ????
9E0E: 03 ; ????
9E0F: 3A ; ????
9E10: 03 ; ????
9E11: 03 ; ????
9E12: 81 06           STA     ($06,X)             
9E14: 03 ; ????
9E15: 90 16           BCC     $9E2D               ; {}
9E17: 01 9C           ORA     ($9C,X)             
9E19: 17 ; ????
9E1A: 01 DA           ORA     ($DA,X)             
9E1C: 16 01           ASL     $01,X               
9E1E: FD FF 02        SBC     $02FF,X             
9E21: 00              BRK                         
9E22: 16 02           ASL     $02,X               
9E24: 0C ; ????
9E25: 23 ; ????
9E26: 00              BRK                         
9E27: 22 ; ????
9E28: 14 ; ????
9E29: 03 ; ????
9E2A: 30 19           BMI     $9E45               ; {}
9E2C: 01 68           ORA     ($68,X)             
9E2E: 08              PHP                         
9E2F: 00              BRK                         
9E30: 9A              TXS                         
9E31: 1C ; ????
9E32: 02 ; ????
9E33: C8              INY                         
9E34: 06 02           ASL     $02                 
9E36: FD FF 00        SBC     $00FF,X             
9E39: 00              BRK                         
9E3A: 09 00           ORA     #$00                
9E3C: 0C ; ????
9E3D: 1D 01 15        ORA     $1501,X             
9E40: 1C ; ????
9E41: 02 ; ????
9E42: 20 08 00        JSR     $0008               
9E45: 2C 12 03        BIT     $0312               
9E48: 32 ; ????
9E49: 22 ; ????
9E4A: 02 ; ????
9E4B: 44 ; ????
9E4C: 1C ; ????
9E4D: 02 ; ????
9E4E: 47 ; ????
9E4F: 23 ; ????
9E50: 00              BRK                         
9E51: 4B ; ????
9E52: 23 ; ????
9E53: 00              BRK                         
9E54: 4F ; ????
9E55: 08              PHP                         
9E56: 00              BRK                         
9E57: 60              RTS                         
9E58: 08              PHP                         
9E59: 00              BRK                         
9E5A: 71 09           ADC     ($09),Y             
9E5C: 00              BRK                         
9E5D: 75 23           ADC     $23,X               
9E5F: 00              BRK                         
9E60: 84 0D           STY     $0D                 
9E62: 02 ; ????
9E63: 99 1C 02        STA     $021C,Y             
9E66: C4 0B           CPY     $0B                 
9E68: 03 ; ????
9E69: DB ; ????
9E6A: 08              PHP                         
9E6B: 00              BRK                         
9E6C: FD FF 00        SBC     $00FF,X             
9E6F: 00              BRK                         
9E70: 08              PHP                         
9E71: 00              BRK                         
9E72: 0C ; ????
9E73: 05 01           ORA     $01                 
9E75: 0E 19 01        ASL     $0119               
9E78: 12 ; ????
9E79: 22 ; ????
9E7A: 02 ; ????
9E7B: 14 ; ????
9E7C: 27 ; ????
9E7D: 01 16           ORA     ($16,X)             
9E7F: 27 ; ????
9E80: 01 1A           ORA     ($1A,X)             
9E82: 27 ; ????
9E83: 01 40           ORA     ($40,X)             
9E85: 09 00           ORA     #$00                
9E87: 4E 19 01        LSR     $0119               
9E8A: 54 ; ????
9E8B: 09 00           ORA     #$00                
9E8D: 60              RTS                         
9E8E: 27 ; ????
9E8F: 01 68           ORA     ($68,X)             
9E91: 27 ; ????
9E92: 01 70           ORA     ($70,X)             
9E94: 08              PHP                         
9E95: 00              BRK                         
9E96: 71 08           ADC     ($08),Y             
9E98: 00              BRK                         
9E99: 74 ; ????
9E9A: 26 00           ROL     $00                 ; {ram.GP_00}
9E9C: 78              SEI                         
9E9D: 26 00           ROL     $00                 ; {ram.GP_00}
9E9F: 7B ; ????
9EA0: 26 00           ROL     $00                 ; {ram.GP_00}
9EA2: 8D 19 01        STA     $0119               
9EA5: 91 25           STA     ($25),Y             
9EA7: 00              BRK                         
9EA8: B0 09           BCS     $9EB3               ; {}
9EAA: 00              BRK                         
9EAB: B4 09           LDY     $09,X               
9EAD: 00              BRK                         
9EAE: B8              CLV                         
9EAF: 09 00           ORA     #$00                
9EB1: BC 09 00        LDY     $0009,X             
9EB4: FD FF 01        SBC     $01FF,X             
9EB7: 15 00           ORA     $00,X               ; {ram.GP_00}
9EB9: 01 44           ORA     ($44,X)             
9EBB: 02 ; ????
9EBC: 01 5A           ORA     ($5A,X)             
9EBE: 12 ; ????
9EBF: 03 ; ????
9EC0: 68              PLA                         
9EC1: 02 ; ????
9EC2: 01 70           ORA     ($70,X)             
9EC4: 04 ; ????
9EC5: 01 7E           ORA     ($7E,X)             
9EC7: 19 01 A6        ORA     $A601,Y             ; {}
9ECA: 0B ; ????
9ECB: 03 ; ????
9ECC: B0 04           BCS     $9ED2               ; {}
9ECE: 01 B3           ORA     ($B3,X)             
9ED0: 03 ; ????
9ED1: 03 ; ????
9ED2: E1 03           SBC     ($03,X)             
9ED4: 03 ; ????
9ED5: FD FF 03        SBC     $03FF,X             
9ED8: 0D 19 01        ORA     $0119               
9EDB: 2B ; ????
9EDC: 00              BRK                         
9EDD: 01 37           ORA     ($37,X)             
9EDF: 06 03           ASL     $03                 
9EE1: 38              SEC                         
9EE2: 15 03           ORA     $03,X               
9EE4: 3B ; ????
9EE5: 15 03           ORA     $03,X               
9EE7: 45 00           EOR     $00                 ; {ram.GP_00}
9EE9: 01 47           ORA     ($47,X)             
9EEB: 0B ; ????
9EEC: 03 ; ????
9EED: 4D 0F 02        EOR     $020F               
9EF0: 70 19           BVS     $9F0B               ; {}
9EF2: 01 94           ORA     ($94,X)             
9EF4: 15 03           ORA     $03,X               
9EF6: 97 ; ????
9EF7: 06 03           ASL     $03                 
9EF9: A1 0B           LDA     ($0B,X)             
9EFB: 03 ; ????
9EFC: A6 0F           LDX     $0F                 
9EFE: 02 ; ????
9EFF: D8              CLD                         
9F00: 02 ; ????
9F01: 01 FD           ORA     ($FD,X)             
9F03: FF ; ????
9F04: 03 ; ????
9F05: 09 03           ORA     #$03                
9F07: 03 ; ????
9F08: 0D 03 03        ORA     $0303               
9F0B: 1B ; ????
9F0C: 0F ; ????
9F0D: 02 ; ????
9F0E: 23 ; ????
9F0F: 12 ; ????
9F10: 03 ; ????
9F11: 27 ; ????
9F12: 03 ; ????
9F13: 03 ; ????
9F14: 2E 22 02        ROL     $0222               
9F17: 33 ; ????
9F18: 06 03           ASL     $03                 
9F1A: 34 ; ????
9F1B: 15 03           ORA     $03,X               
9F1D: 37 ; ????
9F1E: 0F ; ????
9F1F: 02 ; ????
9F20: 43 ; ????
9F21: 03 ; ????
9F22: 03 ; ????
9F23: 60              RTS                         
9F24: 03 ; ????
9F25: 03 ; ????
9F26: 6D 03 03        ADC     $0303               
9F29: 74 ; ????
9F2A: 22 ; ????
9F2B: 02 ; ????
9F2C: 8B ; ????
9F2D: 03 ; ????
9F2E: 03 ; ????
9F2F: 97 ; ????
9F30: 06 03           ASL     $03                 
9F32: 98              TYA                         
9F33: 15 03           ORA     $03,X               
9F35: 9B ; ????
9F36: 0F ; ????
9F37: 02 ; ????
9F38: A7 ; ????
9F39: 03 ; ????
9F3A: 03 ; ????
9F3B: B4 06           LDY     $06,X               
9F3D: 03 ; ????
9F3E: B5 15           LDA     $15,X               
9F40: 03 ; ????
9F41: B8              CLV                         
9F42: 0F ; ????
9F43: 02 ; ????
9F44: C0 0B           CPY     #$0B                
9F46: 03 ; ????
9F47: CF ; ????
9F48: 04 ; ????
9F49: 01 FD           ORA     ($FD,X)             
9F4B: FF ; ????
9F4C: 01 0C           ORA     ($0C,X)             
9F4E: 00              BRK                         
9F4F: 01 14           ORA     ($14,X)             
9F51: 01 01           ORA     ($01,X)             
9F53: 19 01 01        ORA     $0101,Y             
9F56: 29 12           AND     #$12                
9F58: 03 ; ????
9F59: 45 02           EOR     $02                 
9F5B: 01 49           ORA     ($49,X)             
9F5D: 01 01           ORA     ($01,X)             
9F5F: 4B ; ????
9F60: 00              BRK                         
9F61: 01 64           ORA     ($64,X)             
9F63: 12 ; ????
9F64: 03 ; ????
9F65: 73 ; ????
9F66: 02 ; ????
9F67: 01 79           ORA     ($79,X)             
9F69: 02 ; ????
9F6A: 01 88           ORA     ($88,X)             
9F6C: 12 ; ????
9F6D: 03 ; ????
9F6E: A6 02           LDX     $02                 
9F70: 01 BD           ORA     ($BD,X)             
9F72: 12 ; ????
9F73: 03 ; ????
9F74: CA              DEX                         
9F75: 02 ; ????
9F76: 01 FD           ORA     ($FD,X)             
9F78: FF ; ????
9F79: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9F7B: 04 ; ????
9F7C: 01 05           ORA     ($05,X)             
9F7E: 1A ; ????
9F7F: 01 0E           ORA     ($0E,X)             
9F81: 19 01 11        ORA     $1101,Y             
9F84: 01 01           ORA     ($01,X)             
9F86: 1B ; ????
9F87: 03 ; ????
9F88: 03 ; ????
9F89: 20 04 01        JSR     $0104               
9F8C: 24 1F           BIT     $1F                 
9F8E: 01 3B           ORA     ($3B,X)             
9F90: 14 ; ????
9F91: 00              BRK                         
9F92: 43 ; ????
9F93: 01 01           ORA     ($01,X)             
9F95: 47 ; ????
9F96: 19 01 49        ORA     $4901,Y             
9F99: 03 ; ????
9F9A: 03 ; ????
9F9B: 4F ; ????
9F9C: 19 01 60        ORA     $6001,Y             
9F9F: 1A ; ????
9FA0: 01 6D           ORA     ($6D,X)             
9FA2: 00              BRK                         
9FA3: 01 72           ORA     ($72,X)             
9FA5: 29 01           AND     #$01                
9FA7: 86 1A           STX     $1A                 
9FA9: 01 8F           ORA     ($8F,X)             
9FAB: 19 01 92        ORA     $9201,Y             ; {}
9FAE: 01 01           ORA     ($01,X)             
9FB0: 9D 00 01        STA     $0100,X             
9FB3: B5 00           LDA     $00,X               ; {ram.GP_00}
9FB5: 01 C7           ORA     ($C7,X)             
9FB7: 04 ; ????
9FB8: 01 CC           ORA     ($CC,X)             
9FBA: 01 01           ORA     ($01,X)             
9FBC: D3 ; ????
9FBD: 01 01           ORA     ($01,X)             
9FBF: FD FF 01        SBC     $01FF,X             
9FC2: 00              BRK                         
9FC3: 04 ; ????
9FC4: 01 0E           ORA     ($0E,X)             
9FC6: 19 01 20        ORA     $2001,Y             ; {hard.P_CNTRL_2}
9FC9: 28              PLP                         
9FCA: 01 23           ORA     ($23,X)             
9FCC: 29 01           AND     #$01                
9FCE: 2B ; ????
9FCF: 1F ; ????
9FD0: 01 2C           ORA     ($2C,X)             
9FD2: 28              PLP                         
9FD3: 01 35           ORA     ($35,X)             
9FD5: 22 ; ????
9FD6: 02 ; ????
9FD7: 40              RTI                         
9FD8: 04 ; ????
9FD9: 01 4F           ORA     ($4F,X)             
9FDB: 04 ; ????
9FDC: 01 64           ORA     ($64,X)             
9FDE: 03 ; ????
9FDF: 03 ; ????
9FE0: 90 04           BCC     $9FE6               ; {}
9FE2: 01 9F           ORA     ($9F,X)             
9FE4: 04 ; ????
9FE5: 01 B1           ORA     ($B1,X)             
9FE7: 29 01           AND     #$01                
9FE9: BD 1F 01        LDA     $011F,X             
9FEC: BE 28 01        LDX     $0128,Y             
9FEF: FD FF 03        SBC     $03FF,X             
9FF2: 27 ; ????
9FF3: 0B ; ????
9FF4: 03 ; ????
9FF5: 31 03           AND     ($03),Y             
9FF7: 03 ; ????
9FF8: 36 22           ROL     $22,X               
9FFA: 02 ; ????
9FFB: 64 ; ????
9FFC: 03 ; ????
9FFD: 03 ; ????
9FFE: 80 ; ????
9FFF: 03 ; ????
A000: 03 ; ????
A001: 8B ; ????
A002: 22 ; ????
A003: 02 ; ????
A004: 8E 1A 01        STX     $011A               
A007: B1 22           LDA     ($22),Y             
A009: 02 ; ????
A00A: BB ; ????
A00B: 03 ; ????
A00C: 03 ; ????
A00D: C4 03           CPY     $03                 
A00F: 03 ; ????
A010: C8              INY                         
A011: 06 03           ASL     $03                 
A013: E0 03           CPX     #$03                
A015: 03 ; ????
A016: EE 03 03        INC     $0303               
A019: FD FF 01        SBC     $01FF,X             
A01C: 00              BRK                         
A01D: 1A ; ????
A01E: 01 0C           ORA     ($0C,X)             
A020: 19 01 22        ORA     $2201,Y             
A023: 28              PLP                         
A024: 01 25           ORA     ($25,X)             
A026: 28              PLP                         
A027: 01 28           ORA     ($28,X)             
A029: 29 01           AND     #$01                
A02B: 30 19           BMI     $A046               ; {}
A02D: 01 3A           ORA     ($3A,X)             
A02F: 19 01 54        ORA     $5401,Y             
A032: 29 01           AND     #$01                
A034: 56 1F           LSR     $1F,X               
A036: 01 57           ORA     ($57,X)             
A038: 28              PLP                         
A039: 01 70           ORA     ($70,X)             
A03B: 1A ; ????
A03C: 01 7D           ORA     ($7D,X)             
A03E: 19 01 84        ORA     $8401,Y             ; {}
A041: 01 01           ORA     ($01,X)             
A043: B1 19           LDA     ($19),Y             
A045: 01 B5           ORA     ($B5,X)             
A047: 28              PLP                         
A048: 01 B8           ORA     ($B8,X)             
A04A: 29 01           AND     #$01                
A04C: BB ; ????
A04D: 19 01 E9        ORA     $E901,Y             
A050: 1F ; ????
A051: 01 EA           ORA     ($EA,X)             
A053: 28              PLP                         
A054: 01 FD           ORA     ($FD,X)             
A056: FF ; ????
A057: 03 ; ????
A058: 00              BRK                         
A059: 04 ; ????
A05A: 01 0F           ORA     ($0F,X)             
A05C: 04 ; ????
A05D: 01 25           ORA     ($25,X)             
A05F: 06 03           ASL     $03                 
A061: 31 22           AND     ($22),Y             
A063: 02 ; ????
A064: 53 ; ????
A065: 06 03           ASL     $03                 
A067: 70 03           BVS     $A06C               ; {}
A069: 03 ; ????
A06A: 72 ; ????
A06B: 15 03           ORA     $03,X               
A06D: 75 15           ADC     $15,X               
A06F: 03 ; ????
A070: 78              SEI                         
A071: 06 03           ASL     $03                 
A073: 7B ; ????
A074: 06 03           ASL     $03                 
A076: 7C ; ????
A077: 15 03           ORA     $03,X               
A079: 7F ; ????
A07A: 04 ; ????
A07B: 01 81           ORA     ($81,X)             
A07D: 03 ; ????
A07E: 03 ; ????
A07F: 85 03           STA     $03                 
A081: 03 ; ????
A082: 8B ; ????
A083: 03 ; ????
A084: 03 ; ????
A085: 99 00 01        STA     $0100,Y             
A088: CA              DEX                         
A089: 00              BRK                         
A08A: 01 FD           ORA     ($FD,X)             
A08C: FF ; ????
A08D: 01 00           ORA     ($00,X)             ; {ram.GP_00}
A08F: 23 ; ????
A090: 00              BRK                         
A091: 04 ; ????
A092: 23 ; ????
A093: 00              BRK                         
A094: 09 22           ORA     #$22                
A096: 02 ; ????
A097: 0C ; ????
A098: 19 01 36        ORA     $3601,Y             
A09B: 1A ; ????
A09C: 01 37           ORA     ($37,X)             
A09E: 0B ; ????
A09F: 03 ; ????
A0A0: 4A              LSR     A                   
A0A1: 0D 02 60        ORA     $6002               
A0A4: 17 ; ????
A0A5: 01 64           ORA     ($64,X)             
A0A7: 17 ; ????
A0A8: 01 6C           ORA     ($6C,X)             
A0AA: 23 ; ????
A0AB: 00              BRK                         
A0AC: 89 ; ????
A0AD: 23 ; ????
A0AE: 00              BRK                         
A0AF: A4 22           LDY     $22                 
A0B1: 02 ; ????
A0B2: A6 17           LDX     $17                 
A0B4: 01 B6           ORA     ($B6,X)             
A0B6: 05 01           ORA     $01                 
A0B8: B8              CLV                         
A0B9: 0F ; ????
A0BA: 02 ; ????
A0BB: C3 ; ????
A0BC: 23 ; ????
A0BD: 00              BRK                         
A0BE: D1 14           CMP     ($14),Y             
A0C0: 02 ; ????
A0C1: D3 ; ????
A0C2: 05 01           ORA     $01                 
A0C4: E0 17           CPX     #$17                
A0C6: 01 EE           ORA     ($EE,X)             
A0C8: 17 ; ????
A0C9: 01 FD           ORA     ($FD,X)             
A0CB: FF ; ????
A0CC: 00              BRK                         
A0CD: 00              BRK                         
A0CE: 09 00           ORA     #$00                
A0D0: 0F ; ????
A0D1: 08              PHP                         
A0D2: 00              BRK                         
A0D3: 29 23           AND     #$23                
A0D5: 00              BRK                         
A0D6: 30 1A           BMI     $A0F2               ; {}
A0D8: 01 36           ORA     ($36,X)             
A0DA: 14 ; ????
A0DB: 02 ; ????
A0DC: 39 05 01        AND     $0105,Y             
A0DF: 3E 08 00        ROL     $0008,X             
A0E2: 46 23           LSR     $23                 
A0E4: 00              BRK                         
A0E5: 56 0C           LSR     $0C,X               
A0E7: 02 ; ????
A0E8: 61 23           ADC     ($23,X)             
A0EA: 00              BRK                         
A0EB: 68              PLA                         
A0EC: 22 ; ????
A0ED: 02 ; ????
A0EE: 7E 1A 01        ROR     $011A,X             
A0F1: 83 ; ????
A0F2: 23 ; ????
A0F3: 00              BRK                         
A0F4: 95 05           STA     $05,X               
A0F6: 01 A6           ORA     ($A6,X)             
A0F8: 23 ; ????
A0F9: 00              BRK                         
A0FA: BF ; ????
A0FB: 0D 02 C4        ORA     $C402               
A0FE: 22 ; ????
A0FF: 02 ; ????
A100: D9 23 00        CMP     $0023,Y             
A103: FD FF 01        SBC     $01FF,X             
A106: 00              BRK                         
A107: 21 01           AND     ($01,X)             
A109: 04 ; ????
A10A: 21 01           AND     ($01,X)             
A10C: 08              PHP                         
A10D: 21 01           AND     ($01,X)             
A10F: 0C ; ????
A110: 21 01           AND     ($01,X)             
A112: 20 20 01        JSR     $0120               
A115: 2F ; ????
A116: 20 01 41        JSR     $4101               
A119: 06 03           ASL     $03                 
A11B: 4D 0E 01        EOR     $010E               
A11E: 60              RTS                         
A11F: 20 01 6F        JSR     $6F01               
A122: 20 01 71        JSR     $7101               
A125: 0E 01 7C        ASL     $7C01               
A128: 0A              ASL     A                   
A129: 01 7E           ORA     ($7E,X)             
A12B: 20 01 8E        JSR     $8E01               ; {}
A12E: 11 00           ORA     ($00),Y             ; {ram.GP_00}
A130: A0 20           LDY     #$20                
A132: 01 A1           ORA     ($A1,X)             
A134: 0A              ASL     A                   
A135: 01 A7           ORA     ($A7,X)             
A137: 0E 01 AB        ASL     $AB01               ; {}
A13A: 03 ; ????
A13B: 03 ; ????
A13C: AF ; ????
A13D: 20 01 BE        JSR     $BE01               ; {}
A140: 20 01 D0        JSR     $D001               
A143: 21 01           AND     ($01,X)             
A145: D4 ; ????
A146: 21 01           AND     ($01,X)             
A148: D8              CLD                         
A149: 21 01           AND     ($01,X)             
A14B: DC ; ????
A14C: 21 01           AND     ($01,X)             
A14E: FD FF 01        SBC     $01FF,X             
A151: 00              BRK                         
A152: 13 ; ????
A153: 01 04           ORA     ($04,X)             
A155: 13 ; ????
A156: 01 08           ORA     ($08,X)             
A158: 13 ; ????
A159: 01 0C           ORA     ($0C,X)             
A15B: 13 ; ????
A15C: 01 20           ORA     ($20,X)             
A15E: 10 01           BPL     $A161               ; {}
A160: 2F ; ????
A161: 10 01           BPL     $A164               ; {}
A163: 60              RTS                         
A164: 10 01           BPL     $A167               ; {}
A166: 6F ; ????
A167: 10 01           BPL     $A16A               ; {}
A169: 80 ; ????
A16A: 10 01           BPL     $A16D               ; {}
A16C: 8E 11 00        STX     $0011               
A16F: AD 13 01        LDA     $0113               
A172: C0 13           CPY     #$13                
A174: 01 C1           ORA     ($C1,X)             
A176: 15 03           ORA     $03,X               
A178: C4 13           CPY     $13                 
A17A: 01 C8           ORA     ($C8,X)             
A17C: 13 ; ????
A17D: 01 CC           ORA     ($CC,X)             
A17F: 15 03           ORA     $03,X               
A181: CE 13 01        DEC     $0113               
A184: DC ; ????
A185: 27 ; ????
A186: 01 FD           ORA     ($FD,X)             
A188: FF ; ????
A189: 00              BRK                         
A18A: 60              RTS                         
A18B: 23 ; ????
A18C: 00              BRK                         
A18D: 64 ; ????
A18E: 23 ; ????
A18F: 00              BRK                         
A190: 68              PLA                         
A191: 23 ; ????
A192: 00              BRK                         
A193: 6C 23 00        JMP     ($0023)             
A196: 70 0C           BVS     $A1A4               ; {}
A198: 02 ; ????
A199: 7F ; ????
A19A: 0C ; ????
A19B: 02 ; ????
A19C: A0 09           LDY     #$09                
A19E: 00              BRK                         
A19F: A4 09           LDY     $09                 
A1A1: 00              BRK                         
A1A2: A8              TAY                         
A1A3: 09 00           ORA     #$00                
A1A5: AC 09 00        LDY     $0009               
A1A8: FD FF 01        SBC     $01FF,X             
A1AB: 40              RTI                         
A1AC: FF ; ????
A1AD: 02 ; ????
A1AE: 40              RTI                         
A1AF: 40              RTI                         
A1B0: FF ; ????
A1B1: 04 ; ????
A1B2: 40              RTI                         
A1B3: 40              RTI                         
A1B4: 40              RTI                         
A1B5: 40              RTI                         
A1B6: FF ; ????
A1B7: 04 ; ????
A1B8: 59 59 59        EOR     $5959,Y             
A1BB: 59 FF 01        EOR     $01FF,Y             
A1BE: 58              CLI                         
A1BF: 01 58           ORA     ($58,X)             
A1C1: 01 58           ORA     ($58,X)             
A1C3: 01 58           ORA     ($58,X)             
A1C5: FF ; ????
A1C6: 02 ; ????
A1C7: 58              CLI                         
A1C8: 58              CLI                         
A1C9: 02 ; ????
A1CA: 58              CLI                         
A1CB: 58              CLI                         
A1CC: FF ; ????
A1CD: 01 59           ORA     ($59,X)             
A1CF: FF ; ????
A1D0: 01 08           ORA     ($08,X)             
A1D2: 01 09           ORA     ($09,X)             
A1D4: 01 09           ORA     ($09,X)             
A1D6: 01 09           ORA     ($09,X)             
A1D8: FF ; ????
A1D9: 01 53           ORA     ($53,X)             
A1DB: 01 53           ORA     ($53,X)             
A1DD: 01 53           ORA     ($53,X)             
A1DF: 01 53           ORA     ($53,X)             
A1E1: FF ; ????
A1E2: 04 ; ????
A1E3: 53 ; ????
A1E4: 53 ; ????
A1E5: 53 ; ????
A1E6: 53 ; ????
A1E7: 04 ; ????
A1E8: 53 ; ????
A1E9: 53 ; ????
A1EA: 53 ; ????
A1EB: 53 ; ????
A1EC: FF ; ????
A1ED: 03 ; ????
A1EE: 5B ; ????
A1EF: 5B ; ????
A1F0: 5B ; ????
A1F1: FF ; ????
A1F2: 08              PHP                         
A1F3: 59 59 59        EOR     $5959,Y             
A1F6: 59 59 59        EOR     $5959,Y             
A1F9: 59 59 FF        EOR     $FF59,Y             
A1FC: 01 0A           ORA     ($0A,X)             
A1FE: 01 0D           ORA     ($0D,X)             
A200: 01 0C           ORA     ($0C,X)             
A202: FF ; ????
A203: 01 0A           ORA     ($0A,X)             
A205: 01 0E           ORA     ($0E,X)             
A207: 01 0D           ORA     ($0D,X)             
A209: 01 0C           ORA     ($0C,X)             
A20B: FF ; ????
A20C: 02 ; ????
A20D: 5B ; ????
A20E: 5B ; ????
A20F: FF ; ????
A210: 01 0A           ORA     ($0A,X)             
A212: 01 10           ORA     ($10,X)             
A214: FF ; ????
A215: 01 5C           ORA     ($5C,X)             
A217: 01 5C           ORA     ($5C,X)             
A219: 01 5C           ORA     ($5C,X)             
A21B: 01 5C           ORA     ($5C,X)             
A21D: FF ; ????
A21E: 01 50           ORA     ($50,X)             
A220: 01 21           ORA     ($21,X)             
A222: FF ; ????
A223: 01 11           ORA     ($11,X)             
A225: 01 12           ORA     ($12,X)             
A227: FF ; ????
A228: 04 ; ????
A229: 5C ; ????
A22A: 5C ; ????
A22B: 5C ; ????
A22C: 5C ; ????
A22D: 04 ; ????
A22E: 5C ; ????
A22F: 5C ; ????
A230: 5C ; ????
A231: 5C ; ????
A232: FF ; ????
A233: 02 ; ????
A234: 13 ; ????
A235: 13 ; ????
A236: FF ; ????
A237: 03 ; ????
A238: 30 30           BMI     $A26A               ; {}
A23A: 30 FF           BMI     $A23B               ; {}
A23C: 02 ; ????
A23D: 5A ; ????
A23E: 5A ; ????
A23F: 02 ; ????
A240: 5A ; ????
A241: 5A ; ????
A242: 02 ; ????
A243: 5A ; ????
A244: 5A ; ????
A245: 02 ; ????
A246: 5A ; ????
A247: 5A ; ????
A248: FF ; ????
A249: 04 ; ????
A24A: 5A ; ????
A24B: 5A ; ????
A24C: 5A ; ????
A24D: 5A ; ????
A24E: FF ; ????
A24F: 01 53           ORA     ($53,X)             
A251: FF ; ????
A252: 04 ; ????
A253: 58              CLI                         
A254: 58              CLI                         
A255: 58              CLI                         
A256: 58              CLI                         
A257: 04 ; ????
A258: 58              CLI                         
A259: 58              CLI                         
A25A: 58              CLI                         
A25B: 58              CLI                         
A25C: 04 ; ????
A25D: 58              CLI                         
A25E: 58              CLI                         
A25F: 58              CLI                         
A260: 58              CLI                         
A261: 04 ; ????
A262: 58              CLI                         
A263: 58              CLI                         
A264: 58              CLI                         
A265: 58              CLI                         
A266: FF ; ????
A267: 02 ; ????
A268: 58              CLI                         
A269: 58              CLI                         
A26A: 02 ; ????
A26B: 58              CLI                         
A26C: 58              CLI                         
A26D: 02 ; ????
A26E: 58              CLI                         
A26F: 58              CLI                         
A270: 02 ; ????
A271: 58              CLI                         
A272: 58              CLI                         
A273: FF ; ????
A274: 04 ; ????
A275: 48              PHA                         
A276: 48              PHA                         
A277: 48              PHA                         
A278: 48              PHA                         
A279: FF ; ????
A27A: 01 48           ORA     ($48,X)             
A27C: FF ; ????
A27D: 04 ; ????
A27E: 5A ; ????
A27F: 5A ; ????
A280: 5A ; ????
A281: 5A ; ????
A282: 04 ; ????
A283: 5A ; ????
A284: 5A ; ????
A285: 5A ; ????
A286: 5A ; ????
A287: 04 ; ????
A288: 5A ; ????
A289: 5A ; ????
A28A: 5A ; ????
A28B: 5A ; ????
A28C: 04 ; ????
A28D: 5A ; ????
A28E: 5A ; ????
A28F: 5A ; ????
A290: 5A ; ????
A291: FF ; ????
A292: 01 13           ORA     ($13,X)             
A294: FF ; ????
A295: 01 32           ORA     ($32,X)             
A297: FF ; ????
A298: 01 54           ORA     ($54,X)             
A29A: 01 54           ORA     ($54,X)             
A29C: 01 54           ORA     ($54,X)             
A29E: 01 54           ORA     ($54,X)             
A2A0: FF ; ????
A2A1: 04 ; ????
A2A2: 54 ; ????
A2A3: 54 ; ????
A2A4: 54 ; ????
A2A5: 54 ; ????
A2A6: 04 ; ????
A2A7: 54 ; ????
A2A8: 54 ; ????
A2A9: 54 ; ????
A2AA: 54 ; ????
A2AB: FF ; ????
A2AC: 01 02           ORA     ($02,X)             
A2AE: 01 01           ORA     ($01,X)             
A2B0: 01 07           ORA     ($07,X)             
A2B2: 01 0C           ORA     ($0C,X)             
A2B4: FF ; ????
A2B5: 04 ; ????
A2B6: 53 ; ????
A2B7: 53 ; ????
A2B8: 53 ; ????
A2B9: 53 ; ????
A2BA: FF ; ????
A2BB: 01 50           ORA     ($50,X)             
A2BD: 01 29           ORA     ($29,X)             
A2BF: FF ; ????
A2C0: 01 51           ORA     ($51,X)             
A2C2: 01 52           ORA     ($52,X)             
A2C4: FF ; ????
A2C5: 01 04           ORA     ($04,X)             
A2C7: 01 03           ORA     ($03,X)             
A2C9: 01 03           ORA     ($03,X)             
A2CB: 01 04           ORA     ($04,X)             
A2CD: FF ; ????
A2CE: 04 ; ????
A2CF: 55 55           EOR     $55,X               
A2D1: 55 55           EOR     $55,X               
A2D3: FF ; ????
A2D4: 03 ; ????
A2D5: 56 56           LSR     $56,X               
A2D7: 56 FF           LSR     $FF,X               
A2D9: 01 31           ORA     ($31,X)             
A2DB: FF ; ????
A2DC: 12 ; ????
A2DD: 12 ; ????
A2DE: 12 ; ????
A2DF: 12 ; ????
A2E0: A5 A6           LDA     $A6                 
A2E2: A7 ; ????
A2E3: A8              TAY                         
A2E4: 69 6A           ADC     #$6A                
A2E6: 6B ; ????
A2E7: 6C CE CF        JMP     ($CFCE)             
A2EA: CE CF DE        DEC     $DECF               
A2ED: DF ; ????
A2EE: DE DF 6F        DEC     $6FDF,X             
A2F1: 6F ; ????
A2F2: 6F ; ????
A2F3: 6F ; ????
A2F4: 2B ; ????
A2F5: 12 ; ????
A2F6: 12 ; ????
A2F7: 12 ; ????
A2F8: 7A ; ????
A2F9: 7A ; ????
A2FA: 6D 6E 74        ADC     $746E               
A2FD: 12 ; ????
A2FE: 89 ; ????
A2FF: 8A              TXA                         
A300: 89 ; ????
A301: 8A              TXA                         
A302: 89 ; ????
A303: 8A              TXA                         
A304: 8F ; ????
A305: 90 91           BCC     $A298               ; {}
A307: 92 ; ????
A308: 91 92           STA     ($92),Y             
A30A: 91 92           STA     ($92),Y             
A30C: 91 92           STA     ($92),Y             
A30E: 6D 6E 93        ADC     $936E               ; {}
A311: 92 ; ????
A312: 95 92           STA     $92,X               
A314: 91 94           STA     ($94),Y             
A316: 91 96           STA     ($96),Y             
A318: 2B ; ????
A319: 12 ; ????
A31A: 12 ; ????
A31B: 12 ; ????
A31C: 91 92           STA     ($92),Y             
A31E: 93 ; ????
A31F: 94 C7           STY     $C7,X               
A321: 12 ; ????
A322: C6 12           DEC     $12                 
A324: C6 12           DEC     $12                 
A326: C6 12           DEC     $12                 
A328: 70 71           BVS     $A39B               ; {}
A32A: 72 ; ????
A32B: 73 ; ????
A32C: 2B ; ????
A32D: 12 ; ????
A32E: 12 ; ????
A32F: 12 ; ????
A330: 2B ; ????
A331: 12 ; ????
A332: 12 ; ????
A333: 12 ; ????
A334: 2B ; ????
A335: 12 ; ????
A336: 12 ; ????
A337: 12 ; ????
A338: 2B ; ????
A339: 12 ; ????
A33A: 12 ; ????
A33B: 12 ; ????
A33C: 2B ; ????
A33D: 12 ; ????
A33E: 12 ; ????
A33F: 12 ; ????
A340: 2B ; ????
A341: 12 ; ????
A342: 12 ; ????
A343: 12 ; ????
A344: 2B ; ????
A345: 12 ; ????
A346: 12 ; ????
A347: 12 ; ????
A348: 2B ; ????
A349: 12 ; ????
A34A: 12 ; ????
A34B: 12 ; ????
A34C: 2B ; ????
A34D: 12 ; ????
A34E: 12 ; ????
A34F: 12 ; ????
A350: 2B ; ????
A351: 12 ; ????
A352: 12 ; ????
A353: 12 ; ????
A354: 2B ; ????
A355: 12 ; ????
A356: 12 ; ????
A357: 12 ; ????
A358: 2B ; ????
A359: 12 ; ????
A35A: 12 ; ????
A35B: 12 ; ????
A35C: 64 ; ????
A35D: 65 64           ADC     $64                 
A35F: 65 64           ADC     $64                 
A361: 65 64           ADC     $64                 
A363: 65 64           ADC     $64                 
A365: 65 64           ADC     $64                 
A367: 65 64           ADC     $64                 
A369: 65 64           ADC     $64                 
A36B: 65 64           ADC     $64                 
A36D: 65 64           ADC     $64                 
A36F: 65 64           ADC     $64                 
A371: 65 64           ADC     $64                 
A373: 65 64           ADC     $64                 
A375: 65 64           ADC     $64                 
A377: 65 64           ADC     $64                 
A379: 65 64           ADC     $64                 
A37B: 65 2B           ADC     $2B                 
A37D: 12 ; ????
A37E: 12 ; ????
A37F: 12 ; ????
A380: 64 ; ????
A381: 65 64           ADC     $64                 
A383: 65 64           ADC     $64                 
A385: 65 64           ADC     $64                 
A387: 65 2B           ADC     $2B                 
A389: 12 ; ????
A38A: 12 ; ????
A38B: 12 ; ????
A38C: 2B ; ????
A38D: 12 ; ????
A38E: 12 ; ????
A38F: 12 ; ????
A390: 2B ; ????
A391: 12 ; ????
A392: 12 ; ????
A393: 12 ; ????
A394: 2B ; ????
A395: 12 ; ????
A396: 12 ; ????
A397: 12 ; ????
A398: 2B ; ????
A399: 12 ; ????
A39A: 12 ; ????
A39B: 12 ; ????
A39C: AA              TAX                         
A39D: AA              TAX                         
A39E: AB ; ????
A39F: AB ; ????
A3A0: CA              DEX                         
A3A1: CB ; ????
A3A2: CC CD DA        CPY     $DACD               
A3A5: D6 D8           DEC     $D8,X               
A3A7: DC ; ????
A3A8: 2B ; ????
A3A9: 12 ; ????
A3AA: 12 ; ????
A3AB: 12 ; ????
A3AC: 2B ; ????
A3AD: 12 ; ????
A3AE: 12 ; ????
A3AF: 12 ; ????
A3B0: 2B ; ????
A3B1: 12 ; ????
A3B2: 12 ; ????
A3B3: 12 ; ????
A3B4: 2B ; ????
A3B5: 12 ; ????
A3B6: 12 ; ????
A3B7: 12 ; ????
A3B8: 2B ; ????
A3B9: 12 ; ????
A3BA: 12 ; ????
A3BB: 12 ; ????
A3BC: 4D 4D B2        EOR     $B24D               ; {}
A3BF: B2 ; ????
A3C0: 2B ; ????
A3C1: 12 ; ????
A3C2: 12 ; ????
A3C3: 12 ; ????
A3C4: 2B ; ????
A3C5: 12 ; ????
A3C6: 12 ; ????
A3C7: 12 ; ????
A3C8: 2B ; ????
A3C9: 12 ; ????
A3CA: 12 ; ????
A3CB: 12 ; ????
A3CC: 2B ; ????
A3CD: 12 ; ????
A3CE: 12 ; ????
A3CF: 12 ; ????
A3D0: 2B ; ????
A3D1: 12 ; ????
A3D2: 12 ; ????
A3D3: 12 ; ????
A3D4: 2B ; ????
A3D5: 12 ; ????
A3D6: 12 ; ????
A3D7: 12 ; ????
A3D8: 2B ; ????
A3D9: 12 ; ????
A3DA: 12 ; ????
A3DB: 12 ; ????
A3DC: D4 ; ????
A3DD: D4 ; ????
A3DE: D5 D5           CMP     $D5,X               
A3E0: 2B ; ????
A3E1: 12 ; ????
A3E2: 12 ; ????
A3E3: 12 ; ????
A3E4: 2B ; ????
A3E5: 12 ; ????
A3E6: 12 ; ????
A3E7: 12 ; ????
A3E8: 2B ; ????
A3E9: 12 ; ????
A3EA: 12 ; ????
A3EB: 12 ; ????
A3EC: 2B ; ????
A3ED: 12 ; ????
A3EE: 12 ; ????
A3EF: 12 ; ????
A3F0: 2B ; ????
A3F1: 12 ; ????
A3F2: 12 ; ????
A3F3: 12 ; ????
A3F4: 2B ; ????
A3F5: 12 ; ????
A3F6: 12 ; ????
A3F7: 12 ; ????
A3F8: 2B ; ????
A3F9: 12 ; ????
A3FA: 12 ; ????
A3FB: 12 ; ????
A3FC: E0 E1           CPX     #$E1                
A3FE: E2 ; ????
A3FF: D7 ; ????
A400: 2B ; ????
A401: 12 ; ????
A402: 12 ; ????
A403: 12 ; ????
A404: 2B ; ????
A405: 12 ; ????
A406: 12 ; ????
A407: 12 ; ????
A408: 2B ; ????
A409: 12 ; ????
A40A: 12 ; ????
A40B: 12 ; ????
A40C: 2B ; ????
A40D: 12 ; ????
A40E: 12 ; ????
A40F: 12 ; ????
A410: 2B ; ????
A411: 12 ; ????
A412: 12 ; ????
A413: 12 ; ????
A414: 2B ; ????
A415: 12 ; ????
A416: 12 ; ????
A417: 12 ; ????
A418: 2B ; ????
A419: 12 ; ????
A41A: 12 ; ????
A41B: 12 ; ????
A41C: 60              RTS                         
A41D: 61 64           ADC     ($64,X)             
A41F: 65 60           ADC     $60                 
A421: 61 62           ADC     ($62,X)             
A423: 63 ; ????
A424: 62 ; ????
A425: 63 ; ????
A426: 62 ; ????
A427: 63 ; ????
A428: 4E 4F 4F        LSR     $4F4F               
A42B: 4E 5C 5D        LSR     $5D5C               
A42E: 5E 5F B1        LSR     $B15F,X             ; {}
A431: B1 B1           LDA     ($B1),Y             
A433: B1 C8           LDA     ($C8),Y             
A435: C8              INY                         
A436: C9 C9           CMP     #$C9                
A438: 2B ; ????
A439: 12 ; ????
A43A: 12 ; ????
A43B: 12 ; ????
A43C: C4 C5           CPY     $C5                 
A43E: DB ; ????
A43F: DD D9 D9        CMP     $D9D9,X             
A442: D9 D9 D0        CMP     $D0D9,Y             
A445: D1 D2           CMP     ($D2),Y             
A447: D3 ; ????
A448: 5B ; ????
A449: 5B ; ????
A44A: 79 79 51        ADC     $5179,Y             
A44D: 50 50           BVC     $A49F               ; {}
A44F: 51 2B           EOR     ($2B),Y             
A451: 12 ; ????
A452: 12 ; ????
A453: 12 ; ????
A454: 2B ; ????
A455: 12 ; ????
A456: 12 ; ????
A457: 12 ; ????
A458: 2B ; ????
A459: 12 ; ????
A45A: 12 ; ????
A45B: 12 ; ????
A45C: 2B ; ????
A45D: 12 ; ????
A45E: 12 ; ????
A45F: 12 ; ????
A460: 2B ; ????
A461: 12 ; ????
A462: 12 ; ????
A463: 12 ; ????
A464: 2B ; ????
A465: 12 ; ????
A466: 12 ; ????
A467: 12 ; ????
A468: 2B ; ????
A469: 12 ; ????
A46A: 12 ; ????
A46B: 12 ; ????
A46C: 2B ; ????
A46D: 12 ; ????
A46E: 12 ; ????
A46F: 12 ; ????
A470: 2B ; ????
A471: 12 ; ????
A472: 12 ; ????
A473: 12 ; ????
A474: 2B ; ????
A475: 12 ; ????
A476: 12 ; ????
A477: 12 ; ????
A478: 2B ; ????
A479: 12 ; ????
A47A: 12 ; ????
A47B: 12 ; ????
A47C: 2B ; ????
A47D: 12 ; ????
A47E: 12 ; ????
A47F: 12 ; ????
A480: 2B ; ????
A481: 12 ; ????
A482: 12 ; ????
A483: 12 ; ????
A484: 2B ; ????
A485: 12 ; ????
A486: 12 ; ????
A487: 12 ; ????
A488: 2B ; ????
A489: 12 ; ????
A48A: 12 ; ????
A48B: 12 ; ????
A48C: 2B ; ????
A48D: 12 ; ????
A48E: 12 ; ????
A48F: 12 ; ????
A490: 2B ; ????
A491: 12 ; ????
A492: 12 ; ????
A493: 12 ; ????
A494: 2B ; ????
A495: 12 ; ????
A496: 12 ; ????
A497: 12 ; ????
A498: A1 A2           LDA     ($A2,X)             
A49A: A3 ; ????
A49B: A4 2B           LDY     $2B                 
A49D: 12 ; ????
A49E: 12 ; ????
A49F: 12 ; ????
A4A0: 01 09           ORA     ($09,X)             
A4A2: C7 ; ????
A4A3: 00              BRK                         
A4A4: 01 0A           ORA     ($0A,X)             
A4A6: C7 ; ????
A4A7: 00              BRK                         
A4A8: 02 ; ????
A4A9: 08              PHP                         
A4AA: C7 ; ????
A4AB: 00              BRK                         
A4AC: 02 ; ????
A4AD: 0F ; ????
A4AE: 07 ; ????
A4AF: 00              BRK                         
A4B0: FF ; ????
A4B1: FF ; ????
A4B2: FF ; ????
A4B3: FF ; ????
A4B4: FF ; ????
A4B5: FF ; ????
A4B6: FF ; ????
A4B7: FF ; ????
A4B8: FF ; ????
A4B9: FF ; ????
A4BA: FF ; ????
A4BB: FF ; ????
A4BC: FF ; ????
A4BD: FF ; ????
A4BE: FF ; ????
A4BF: FF ; ????
A4C0: 01 09           ORA     ($09,X)             
A4C2: 97 ; ????
A4C3: 00              BRK                         
A4C4: 01 0A           ORA     ($0A,X)             
A4C6: 67 ; ????
A4C7: 00              BRK                         
A4C8: 02 ; ????
A4C9: 08              PHP                         
A4CA: 97 ; ????
A4CB: 00              BRK                         
A4CC: 02 ; ????
A4CD: 10 C7           BPL     $A496               ; {}
A4CF: 00              BRK                         
A4D0: FF ; ????
A4D1: FF ; ????
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
A4E0: 01 09           ORA     ($09,X)             
A4E2: 67 ; ????
A4E3: 00              BRK                         
A4E4: 01 0B           ORA     ($0B,X)             
A4E6: C7 ; ????
A4E7: 00              BRK                         
A4E8: 02 ; ????
A4E9: 08              PHP                         
A4EA: 37 ; ????
A4EB: 00              BRK                         
A4EC: 02 ; ????
A4ED: 10 97           BPL     $A486               ; {}
A4EF: 00              BRK                         
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
A500: 01 09           ORA     ($09,X)             
A502: 37 ; ????
A503: 00              BRK                         
A504: 01 0B           ORA     ($0B,X)             
A506: 37 ; ????
A507: 00              BRK                         
A508: 02 ; ????
A509: 10 37           BPL     $A542               ; {}
A50B: 00              BRK                         
A50C: FF ; ????
A50D: FF ; ????
A50E: FF ; ????
A50F: FF ; ????
A510: FF ; ????
A511: FF ; ????
A512: FF ; ????
A513: FF ; ????
A514: FF ; ????
A515: FF ; ????
A516: FF ; ????
A517: FF ; ????
A518: FF ; ????
A519: FF ; ????
A51A: FF ; ????
A51B: FF ; ????
A51C: FF ; ????
A51D: FF ; ????
A51E: FF ; ????
A51F: FF ; ????
A520: 00              BRK                         
A521: 05 F0           ORA     $F0                 
A523: 05 00           ORA     $00                 ; {ram.GP_00}
A525: 05 F0           ORA     $F0                 
A527: 05 00           ORA     $00                 ; {ram.GP_00}
A529: 04 ; ????
A52A: 40              RTI                         
A52B: 04 ; ????
A52C: 00              BRK                         
A52D: 04 ; ????
A52E: 40              RTI                         
A52F: 04 ; ????
A530: 1A ; ????
A531: 7C ; ????
A532: 34 ; ????
A533: 7C ; ????
A534: 52 ; ????
A535: 7C ; ????
A536: 49 78           EOR     #$78                
A538: C5 77           CMP     $77                 
A53A: 49 78           EOR     #$78                
A53C: C5 77           CMP     $77                 
A53E: 49 78           EOR     #$78                
A540: 10 78           BPL     $A5BA               ; {}
A542: 49 78           EOR     #$78                
A544: 10 78           BPL     $A5BE               ; {}
A546: 49 78           EOR     #$78                
A548: 10 78           BPL     $A5C2               ; {}
A54A: 49 78           EOR     #$78                
A54C: 10 78           BPL     $A5C6               ; {}
A54E: 49 78           EOR     #$78                
A550: 10 78           BPL     $A5CA               ; {}
A552: 49 78           EOR     #$78                
A554: 10 78           BPL     $A5CE               ; {}
A556: 49 78           EOR     #$78                
A558: 49 78           EOR     #$78                
A55A: BD 70 0B        LDA     $0B70,X             
A55D: 71 3E           ADC     ($3E),Y             
A55F: 71 80           ADC     ($80),Y             
A561: 71 80           ADC     ($80),Y             
A563: 71 A4           ADC     ($A4),Y             
A565: 71 EC           ADC     ($EC),Y             
A567: 71 3A           ADC     ($3A),Y             
A569: 72 ; ????
A56A: 73 ; ????
A56B: 72 ; ????
A56C: A3 ; ????
A56D: 72 ; ????
A56E: D3 ; ????
A56F: 72 ; ????
A570: 00              BRK                         
A571: 70 FF           BVS     $A572               ; {}
A573: FF ; ????
A574: 09 73           ORA     #$73                
A576: 4B ; ????
A577: 73 ; ????
A578: 81 73           STA     ($73,X)             
A57A: A5 73           LDA     $73                 
A57C: CF ; ????
A57D: 73 ; ????
A57E: F9 73 23        SBC     $2373,Y             
A581: 74 ; ????
A582: 56 74           LSR     $74,X               
A584: 7D 74 A4        ADC     $A474,X             ; {}
A587: 74 ; ????
A588: C5 74           CMP     $74                 
A58A: E0 74           CPX     #$74                
A58C: F8              SED                         
A58D: 74 ; ????
A58E: 39 70 FF        AND     $FF70,Y             
A591: FF ; ????
A592: 2E 75 3E        ROL     $3E75               
A595: 71 76           ADC     ($76),Y             
A597: 75 97           ADC     $97,X               
A599: 75 C4           ADC     $C4,X               
A59B: 75 0C           ADC     $0C,X               
A59D: 76 39           ROR     $39,X               
A59F: 76 39           ROR     $39,X               
A5A1: 76 81           ROR     $81,X               
A5A3: 76 97           ROR     $97,X               
A5A5: 75 B1           ADC     $B1,X               
A5A7: 76 B1           ROR     $B1,X               
A5A9: 76 DB           ROR     $DB,X               
A5AB: 76 DB           ROR     $DB,X               
A5AD: 76 DB           ROR     $DB,X               
A5AF: 76 17           ROR     $17,X               
A5B1: 77 ; ????
A5B2: 81 76           STA     ($76,X)             
A5B4: 4D 77 8C        EOR     $8C77               ; {}
A5B7: 77 ; ????
A5B8: 78              SEI                         
A5B9: 70 FF           BVS     $A5BA               ; {}
A5BB: FF ; ????
A5BC: 6A              ROR     A                   
A5BD: 78              SEI                         
A5BE: 6D 78 71        ADC     $7178               
A5C1: 78              SEI                         
A5C2: 77 ; ????
A5C3: 78              SEI                         
A5C4: 7D 78 86        ADC     $8678,X             ; {}
A5C7: 78              SEI                         
A5C8: 8D 78 90        STA     $9078               ; {}
A5CB: 78              SEI                         
A5CC: 99 78 A2        STA     $A278,Y             ; {}
A5CF: 78              SEI                         
A5D0: AD 78 B2        LDA     $B278               ; {}
A5D3: 78              SEI                         
A5D4: BC 78 C3        LDY     $C378,X             
A5D7: 78              SEI                         
A5D8: CC 78 D0        CPY     $D078               
A5DB: 78              SEI                         
A5DC: D5 78           CMP     $78,X               
A5DE: DE 78 E3        DEC     $E378,X             
A5E1: 78              SEI                         
A5E2: E8              INX                         
A5E3: 78              SEI                         
A5E4: F3 ; ????
A5E5: 78              SEI                         
A5E6: F7 ; ????
A5E7: 78              SEI                         
A5E8: FC ; ????
A5E9: 78              SEI                         
A5EA: 09 79           ORA     #$79                
A5EC: 0F ; ????
A5ED: 79 12 79        ADC     $7912,Y             
A5F0: 27 ; ????
A5F1: 79 34 79        ADC     $7934,Y             
A5F4: 3A ; ????
A5F5: 79 3D 79        ADC     $793D,Y             
A5F8: 52 ; ????
A5F9: 79 55 79        ADC     $7955,Y             
A5FC: 58              CLI                         
A5FD: 79 61 79        ADC     $7961,Y             
A600: 6C 79 75        JMP     ($7579)             
A603: 79 7B 79        ADC     $797B,Y             
A606: 80 ; ????
A607: 79 85 79        ADC     $7985,Y             
A60A: 8E 79 94        STX     $9479               ; {}
A60D: 79 99 79        ADC     $7999,Y             
A610: D6 7C           DEC     $7C,X               
A612: E2 ; ????
A613: 7C ; ????
A614: F0 7C           BEQ     $A692               ; {}
A616: 00              BRK                         
A617: 00              BRK                         
A618: 00              BRK                         
A619: 08              PHP                         
A61A: 08              PHP                         
A61B: 00              BRK                         
A61C: 08              PHP                         
A61D: 00              BRK                         
A61E: 00              BRK                         
A61F: 0D 05 00        ORA     $0005               
A622: 00              BRK                         
A623: 08              PHP                         
A624: 08              PHP                         
A625: 08              PHP                         
A626: 00              BRK                         
A627: 00              BRK                         
A628: 0D 00 08        ORA     $0800               
A62B: 08              PHP                         
A62C: 00              BRK                         
A62D: 00              BRK                         
A62E: 0A              ASL     A                   
A62F: 0A              ASL     A                   
A630: 00              BRK                         
A631: 05 00           ORA     $00                 ; {ram.GP_00}
A633: 00              BRK                         
A634: 08              PHP                         
A635: 00              BRK                         
A636: 08              PHP                         
A637: 08              PHP                         
A638: 00              BRK                         
A639: 0A              ASL     A                   
A63A: 0A              ASL     A                   
A63B: 0A              ASL     A                   
A63C: 0A              ASL     A                   
A63D: 0A              ASL     A                   
A63E: 0A              ASL     A                   
A63F: 0A              ASL     A                   
A640: 00              BRK                         
A641: 0A              ASL     A                   
A642: 00              BRK                         
A643: 0D 08 0B        ORA     $0B08               
A646: 7D 17 7D        ADC     $7D17,X             
A649: 25 7D           AND     $7D                 
A64B: 00              BRK                         
A64C: 00              BRK                         
A64D: 00              BRK                         
A64E: 00              BRK                         
A64F: 00              BRK                         
A650: 00              BRK                         
A651: 00              BRK                         
A652: 00              BRK                         
A653: 00              BRK                         
A654: 65 00           ADC     $00                 ; {ram.GP_00}
A656: 00              BRK                         
A657: 00              BRK                         
A658: 00              BRK                         
A659: 00              BRK                         
A65A: 00              BRK                         
A65B: 00              BRK                         
A65C: 00              BRK                         
A65D: E2 ; ????
A65E: 00              BRK                         
A65F: 00              BRK                         
A660: 00              BRK                         
A661: 00              BRK                         
A662: 00              BRK                         
A663: 00              BRK                         
A664: 00              BRK                         
A665: 00              BRK                         
A666: 00              BRK                         
A667: 00              BRK                         
A668: 00              BRK                         
A669: 00              BRK                         
A66A: 00              BRK                         
A66B: 00              BRK                         
A66C: 00              BRK                         
A66D: 00              BRK                         
A66E: 00              BRK                         
A66F: 00              BRK                         
A670: 00              BRK                         
A671: 00              BRK                         
A672: 00              BRK                         
A673: 00              BRK                         
A674: 00              BRK                         
A675: 00              BRK                         
A676: 00              BRK                         
A677: 00              BRK                         
A678: E5 00           SBC     $00                 ; {ram.GP_00}
A67A: 40              RTI                         
A67B: 7D 4C 7D        ADC     $7D4C,X             
A67E: 5A ; ????
A67F: 7D 00 02        ADC     $0200,X             
A682: 02 ; ????
A683: 00              BRK                         
A684: 00              BRK                         
A685: 0D 00 0D        ORA     $0D00               
A688: 00              BRK                         
A689: 0D 03 00        ORA     $0003               
A68C: 00              BRK                         
A68D: 02 ; ????
A68E: 02 ; ????
A68F: 00              BRK                         
A690: 0D 00 02        ORA     $0200               
A693: 02 ; ????
A694: 02 ; ????
A695: 00              BRK                         
A696: 0D 03 03        ORA     $0303               
A699: 0D 00 02        ORA     $0200               
A69C: 02 ; ????
A69D: 03 ; ????
A69E: 00              BRK                         
A69F: 02 ; ????
A6A0: 00              BRK                         
A6A1: 02 ; ????
A6A2: 02 ; ????
A6A3: 02 ; ????
A6A4: 02 ; ????
A6A5: 02 ; ????
A6A6: 02 ; ????
A6A7: 03 ; ????
A6A8: 0D 02 00        ORA     $0002               
A6AB: 0D 00 03        ORA     $0300               
A6AE: 03 ; ????
A6AF: 75 7D           ADC     $7D,X               
A6B1: 81 7D           STA     ($7D,X)             
A6B3: 8F ; ????
A6B4: 7D 00 00        ADC     $0000,X             ; {ram.GP_00}
A6B7: 00              BRK                         
A6B8: 00              BRK                         
A6B9: 00              BRK                         
A6BA: 38              SEC                         
A6BB: 00              BRK                         
A6BC: C8              INY                         
A6BD: 00              BRK                         
A6BE: 59 00 00        EOR     $0000,Y             ; {ram.GP_00}
A6C1: 00              BRK                         
A6C2: 00              BRK                         
A6C3: 00              BRK                         
A6C4: 00              BRK                         
A6C5: EA              NOP                         
A6C6: 00              BRK                         
A6C7: 00              BRK                         
A6C8: 00              BRK                         
A6C9: 00              BRK                         
A6CA: 00              BRK                         
A6CB: EB ; ????
A6CC: 00              BRK                         
A6CD: 00              BRK                         
A6CE: AC 00 00        LDY     $0000               ; {ram.GP_00}
A6D1: 00              BRK                         
A6D2: 00              BRK                         
A6D3: 00              BRK                         
A6D4: 00              BRK                         
A6D5: 00              BRK                         
A6D6: 00              BRK                         
A6D7: 00              BRK                         
A6D8: 00              BRK                         
A6D9: 00              BRK                         
A6DA: 00              BRK                         
A6DB: 00              BRK                         
A6DC: 00              BRK                         
A6DD: 63 ; ????
A6DE: 00              BRK                         
A6DF: 00              BRK                         
A6E0: 53 ; ????
A6E1: 00              BRK                         
A6E2: 00              BRK                         
A6E3: 00              BRK                         
A6E4: 1F ; ????
A6E5: 3F ; ????
A6E6: 5F ; ????
A6E7: 0F ; ????
A6E8: 30 14           BMI     $A6FE               ; {}
A6EA: 02 ; ????
A6EB: 0F ; ????
A6EC: 28              PLP                         
A6ED: 17 ; ????
A6EE: 07 ; ????
A6EF: 0F ; ????
A6F0: 2C 19 01        BIT     $0119               
A6F3: 0F ; ????
A6F4: 25 00           AND     $00                 ; {ram.GP_00}
A6F6: 15 0F           ORA     $0F,X               
A6F8: 30 26           BMI     $A720               ; {}
A6FA: 07 ; ????
A6FB: 0F ; ????
A6FC: 31 02           AND     ($02),Y             
A6FE: 15 0F           ORA     $0F,X               
A700: 12 ; ????
A701: 23 ; ????
A702: 31 0F           AND     ($0F),Y             
A704: 06 16           ASL     $16                 
A706: 38              SEC                         
A707: 0F ; ????
A708: 30 14           BMI     $A71E               ; {}
A70A: 02 ; ????
A70B: 0F ; ????
A70C: 2B ; ????
A70D: 13 ; ????
A70E: 01 0F           ORA     ($0F,X)             
A710: 30 2C           BMI     $A73E               ; {}
A712: 11 0F           ORA     ($0F),Y             
A714: 27 ; ????
A715: 00              BRK                         
A716: 15 0F           ORA     $0F,X               
A718: 20 26 07        JSR     $0726               
A71B: 0F ; ????
A71C: 31 02           AND     ($02),Y             
A71E: 15 0F           ORA     $0F,X               
A720: 12 ; ????
A721: 23 ; ????
A722: 31 0F           AND     ($0F),Y             
A724: 06 16           ASL     $16                 
A726: 38              SEC                         
A727: 0F ; ????
A728: 30 14           BMI     $A73E               ; {}
A72A: 02 ; ????
A72B: 0F ; ????
A72C: 27 ; ????
A72D: 19 0C 0F        ORA     $0F0C,Y             
A730: 2C 19 01        BIT     $0119               
A733: 0F ; ????
A734: 27 ; ????
A735: 16 15           ASL     $15,X               
A737: 0F ; ????
A738: 20 26 07        JSR     $0726               
A73B: 0F ; ????
A73C: 31 02           AND     ($02),Y             
A73E: 15 0F           ORA     $0F,X               
A740: 12 ; ????
A741: 23 ; ????
A742: 31 0F           AND     ($0F),Y             
A744: 06 16           ASL     $16                 
A746: 38              SEC                         
A747: 05 00           ORA     $00                 ; {ram.GP_00}
A749: 03 ; ????
A74A: 5C ; ????
A74B: 00              BRK                         
A74C: 00              BRK                         
A74D: 07 ; ????
A74E: A8              TAY                         
A74F: 01 01           ORA     ($01,X)             
A751: 01 57           ORA     ($57,X)             
A753: 01 01           ORA     ($01,X)             
A755: 04 ; ????
A756: 5B ; ????
A757: 01 02           ORA     ($02,X)             
A759: 0B ; ????
A75A: AA              TAX                         
A75B: 00              BRK                         
A75C: 02 ; ????
A75D: 05 09           ORA     $09                 
A75F: 00              BRK                         
A760: 01 01           ORA     ($01,X)             
A762: 01 01           ORA     ($01,X)             
A764: 01 02           ORA     ($02,X)             
A766: 01 02           ORA     ($02,X)             
A768: 01 04           ORA     ($04,X)             
A76A: 02 ; ????
A76B: 0A              ASL     A                   
A76C: 08              PHP                         
A76D: 0A              ASL     A                   
A76E: 02 ; ????
A76F: 00              BRK                         
A770: 01 01           ORA     ($01,X)             
A772: 01 03           ORA     ($03,X)             
A774: 05 03           ORA     $03                 
A776: 01 02           ORA     ($02,X)             
A778: 03 ; ????
A779: 04 ; ????
A77A: 03 ; ????
A77B: 0A              ASL     A                   
A77C: 08              PHP                         
A77D: 05 02           ORA     $02                 
A77F: 00              BRK                         
A780: 01 02           ORA     ($02,X)             
A782: 01 01           ORA     ($01,X)             
A784: 02 ; ????
A785: 01 01           ORA     ($01,X)             
A787: 02 ; ????
A788: 01 04           ORA     ($04,X)             
A78A: 01 0A           ORA     ($0A,X)             
A78C: 08              PHP                         
A78D: 02 ; ????
A78E: 02 ; ????
A78F: 00              BRK                         
A790: 02 ; ????
A791: 3E 01 02        ROL     $0201,X             
A794: 4D 01 02        EOR     $0201               
A797: 58              CLI                         
A798: 0B ; ????
A799: 03 ; ????
A79A: 5C ; ????
A79B: 0D 02 6A        ORA     $6A02               
A79E: 08              PHP                         
A79F: 02 ; ????
A7A0: 72 ; ????
A7A1: 03 ; ????
A7A2: 01 7A           ORA     ($7A,X)             
A7A4: 07 ; ????
A7A5: 00              BRK                         
A7A6: 7C ; ????
A7A7: 07 ; ????
A7A8: 00              BRK                         
A7A9: 9E ; ????
A7AA: 10 00           BPL     $A7AC               ; {}
A7AC: 9F ; ????
A7AD: 0D 02 B9        ORA     $B902               ; {}
A7B0: 06 03           ASL     $03                 
A7B2: BD 06 03        LDA     $0306,X             
A7B5: CC 05 01        CPY     $0105               
A7B8: D6 05           DEC     $05,X               
A7BA: 01 FD           ORA     ($FD,X)             
A7BC: FF ; ????
A7BD: 00              BRK                         
A7BE: 3D 0D 02        AND     $020D,X             
A7C1: 40              RTI                         
A7C2: 0C ; ????
A7C3: 02 ; ????
A7C4: 41 05           EOR     ($05,X)             
A7C6: 01 56           ORA     ($56,X)             
A7C8: 0B ; ????
A7C9: 03 ; ????
A7CA: 5B ; ????
A7CB: 0B ; ????
A7CC: 03 ; ????
A7CD: 68              PLA                         
A7CE: 08              PHP                         
A7CF: 02 ; ????
A7D0: 6B ; ????
A7D1: 08              PHP                         
A7D2: 02 ; ????
A7D3: 78              SEI                         
A7D4: 07 ; ????
A7D5: 00              BRK                         
A7D6: 7B ; ????
A7D7: 07 ; ????
A7D8: 00              BRK                         
A7D9: 7E 0D 02        ROR     $020D,X             
A7DC: 80 ; ????
A7DD: 0C ; ????
A7DE: 02 ; ????
A7DF: 9E ; ????
A7E0: 10 00           BPL     $A7E2               ; {}
A7E2: B6 06           LDX     $06,Y               
A7E4: 00              BRK                         
A7E5: BA              TSX                         
A7E6: 06 00           ASL     $00                 ; {ram.GP_00}
A7E8: BC 06 00        LDY     $0006,X             
A7EB: C8              INY                         
A7EC: 05 01           ORA     $01                 
A7EE: D4 ; ????
A7EF: 05 01           ORA     $01                 
A7F1: E0 03           CPX     #$03                
A7F3: 01 FD           ORA     ($FD,X)             
A7F5: FF ; ????
A7F6: 02 ; ????
A7F7: 14 ; ????
A7F8: 19 03 1D        ORA     $1D03,Y             
A7FB: 19 03 39        ORA     $3903,Y             
A7FE: 19 03 3C        ORA     $3C03,Y             
A801: 0A              ASL     A                   
A802: 01 40           ORA     ($40,X)             
A804: 05 01           ORA     $01                 
A806: 50 0C           BVC     $A814               ; {}
A808: 02 ; ????
A809: 52 ; ????
A80A: 0A              ASL     A                   
A80B: 01 56           ORA     ($56,X)             
A80D: 04 ; ????
A80E: 01 5C           ORA     ($5C,X)             
A810: 0B ; ????
A811: 03 ; ????
A812: 65 04           ADC     $04                 
A814: 01 6B           ORA     ($6B,X)             
A816: 0B ; ????
A817: 03 ; ????
A818: 72 ; ????
A819: 0B ; ????
A81A: 03 ; ????
A81B: 76 0B           ROR     $0B,X               
A81D: 03 ; ????
A81E: 7B ; ????
A81F: 08              PHP                         
A820: 02 ; ????
A821: 7E 0D 02        ROR     $020D,X             
A824: 82 ; ????
A825: 08              PHP                         
A826: 02 ; ????
A827: 87 ; ????
A828: 08              PHP                         
A829: 02 ; ????
A82A: 8B ; ????
A82B: 07 ; ????
A82C: 00              BRK                         
A82D: 90 0C           BCC     $A83B               ; {}
A82F: 02 ; ????
A830: 92 ; ????
A831: 07 ; ????
A832: 00              BRK                         
A833: 97 ; ????
A834: 07 ; ????
A835: 00              BRK                         
A836: 9E ; ????
A837: 10 00           BPL     $A839               ; {}
A839: BC 06 02        LDY     $0206,X             
A83C: C8              INY                         
A83D: 06 02           ASL     $02                 
A83F: D0 05           BNE     $A846               ; {}
A841: 01 DA           ORA     ($DA,X)             
A843: 05 01           ORA     $01                 
A845: FD FF 02        SBC     $02FF,X             
A848: 19 03 01        ORA     $0103,Y             
A84B: 30 0C           BMI     $A859               ; {}
A84D: 02 ; ????
A84E: 3C ; ????
A84F: 05 01           ORA     $01                 
A851: 41 01           EOR     ($01,X)             
A853: 02 ; ????
A854: 4F ; ????
A855: 0C ; ????
A856: 02 ; ????
A857: 61 0C           ADC     ($0C,X)             
A859: 02 ; ????
A85A: 62 ; ????
A85B: 0E 02 65        ASL     $6502               
A85E: 0E 02 70        ASL     $7002               
A861: 0C ; ????
A862: 02 ; ????
A863: 74 ; ????
A864: 07 ; ????
A865: 00              BRK                         
A866: 77 ; ????
A867: 07 ; ????
A868: 00              BRK                         
A869: 8A              TXA                         
A86A: 05 01           ORA     $01                 
A86C: 91 00           STA     ($00),Y             ; {ram.GP_00}
A86E: 00              BRK                         
A86F: 9F ; ????
A870: 0C ; ????
A871: 02 ; ????
A872: B0 04           BCS     $A878               ; {}
A874: 01 B4           ORA     ($B4,X)             
A876: 06 03           ASL     $03                 
A878: B8              CLV                         
A879: 06 03           ASL     $03                 
A87B: C2 ; ????
A87C: 05 01           ORA     $01                 
A87E: D9 05 01        CMP     $0105,Y             
A881: FD FF 01        SBC     $01FF,X             
A884: 24 04           BIT     $04                 
A886: 01 3A           ORA     ($3A,X)             
A888: 03 ; ????
A889: 01 49           ORA     ($49,X)             
A88B: 07 ; ????
A88C: 00              BRK                         
A88D: 68              PLA                         
A88E: 04 ; ????
A88F: 01 73           ORA     ($73,X)             
A891: 07 ; ????
A892: 00              BRK                         
A893: 82 ; ????
A894: 05 01           ORA     $01                 
A896: B0 04           BCS     $A89C               ; {}
A898: 01 E6           ORA     ($E6,X)             
A89A: 03 ; ????
A89B: 01 FD           ORA     ($FD,X)             
A89D: FF ; ????
A89E: 01 09           ORA     ($09,X)             
A8A0: 18              CLC                         
A8A1: 01 25           ORA     ($25,X)             
A8A3: 18              CLC                         
A8A4: 01 3B           ORA     ($3B,X)             
A8A6: 18              CLC                         
A8A7: 01 64           ORA     ($64,X)             
A8A9: 19 03 6D        ORA     $6D03,Y             
A8AC: 18              CLC                         
A8AD: 01 97           ORA     ($97,X)             
A8AF: 18              CLC                         
A8B0: 01 9B           ORA     ($9B,X)             
A8B2: 18              CLC                         
A8B3: 01 B4           ORA     ($B4,X)             
A8B5: 18              CLC                         
A8B6: 01 CC           ORA     ($CC,X)             
A8B8: 19 03 E3        ORA     $E303,Y             
A8BB: 18              CLC                         
A8BC: 01 FD           ORA     ($FD,X)             
A8BE: FF ; ????
A8BF: 02 ; ????
A8C0: 04 ; ????
A8C1: 16 01           ASL     $01,X               
A8C3: 30 0E           BMI     $A8D3               ; {}
A8C5: 02 ; ????
A8C6: 3D 0E 02        AND     $020E,X             
A8C9: 4C 16 01        JMP     $0116               
A8CC: 56 0E           LSR     $0E,X               
A8CE: 02 ; ????
A8CF: 8A              TXA                         
A8D0: 0E 02 A3        ASL     $A302               ; {}
A8D3: 12 ; ????
A8D4: 03 ; ????
A8D5: A7 ; ????
A8D6: 12 ; ????
A8D7: 03 ; ????
A8D8: E7 ; ????
A8D9: 02 ; ????
A8DA: 01 FD           ORA     ($FD,X)             
A8DC: FF ; ????
A8DD: 02 ; ????
A8DE: 12 ; ????
A8DF: 07 ; ????
A8E0: 00              BRK                         
A8E1: 20 05 01        JSR     $0105               
A8E4: 39 04 01        AND     $0104,Y             
A8E7: 50 0E           BVC     $A8F7               ; {}
A8E9: 02 ; ????
A8EA: 58              CLI                         
A8EB: 07 ; ????
A8EC: 00              BRK                         
A8ED: 5C ; ????
A8EE: 0E 02 62        ASL     $6202               
A8F1: 07 ; ????
A8F2: 00              BRK                         
A8F3: 6E 07 00        ROR     $0007               
A8F6: 85 04           STA     $04                 
A8F8: 01 98           ORA     ($98,X)             
A8FA: 07 ; ????
A8FB: 00              BRK                         
A8FC: 9C ; ????
A8FD: 01 02           ORA     ($02,X)             
A8FF: A0 0E           LDY     #$0E                
A901: 02 ; ????
A902: AC 0D 02        LDY     $020D               
A905: CA              DEX                         
A906: 01 02           ORA     ($02,X)             
A908: CB ; ????
A909: 0C ; ????
A90A: 02 ; ????
A90B: D7 ; ????
A90C: 0E 02 E6        ASL     $E602               
A90F: 05 01           ORA     $01                 
A911: E8              INX                         
A912: 05 01           ORA     $01                 
A914: FD FF 02        SBC     $02FF,X             
A917: 03 ; ????
A918: 0D 02 09        ORA     $0902               
A91B: 03 ; ????
A91C: 01 1A           ORA     ($1A,X)             
A91E: 0D 02 21        ORA     $2102               
A921: 03 ; ????
A922: 01 34           ORA     ($34,X)             
A924: 0D 02 5A        ORA     $5A02               
A927: 0D 02 64        ORA     $6402               
A92A: 0D 02 69        ORA     $6902               
A92D: 05 01           ORA     $01                 
A92F: 95 04           STA     $04,X               
A931: 01 9A           ORA     ($9A,X)             
A933: 0D 02 C9        ORA     $C902               
A936: 03 ; ????
A937: 01 D7           ORA     ($D7,X)             
A939: 12 ; ????
A93A: 03 ; ????
A93B: FD FF 02        SBC     $02FF,X             
A93E: 00              BRK                         
A93F: 0D 02 08        ORA     $0802               
A942: 0E 02 0C        ASL     $0C02               
A945: 0D 02 30        ORA     $3002               
A948: 0D 02 31        ORA     $3102               
A94B: 05 01           ORA     $01                 
A94D: 4C 0D 02        JMP     $020D               
A950: 69 04           ADC     #$04                
A952: 01 70           ORA     ($70,X)             
A954: 0D 02 8C        ORA     $8C02               ; {}
A957: 0D 02 96        ORA     $9602               ; {}
A95A: 0E 02 98        ASL     $9802               ; {}
A95D: 0E 02 B0        ASL     $B002               ; {}
A960: 0D 02 BC        ORA     $BC02               ; {}
A963: 0D 02 C2        ORA     $C202               
A966: 04 ; ????
A967: 01 FD           ORA     ($FD,X)             
A969: FF ; ????
A96A: 02 ; ????
A96B: 0E 17 02        ASL     $0217               
A96E: 1C ; ????
A96F: 04 ; ????
A970: 01 2E           ORA     ($2E,X)             
A972: 17 ; ????
A973: 02 ; ????
A974: 49 0C           EOR     #$0C                
A976: 02 ; ????
A977: 65 12           ADC     $12                 
A979: 03 ; ????
A97A: 6D 12 03        ADC     $0312               
A97D: A3 ; ????
A97E: 0C ; ????
A97F: 02 ; ????
A980: C1 12           CMP     ($12,X)             
A982: 03 ; ????
A983: C7 ; ????
A984: 12 ; ????
A985: 03 ; ????
A986: FD FF 03        SBC     $03FF,X             
A989: 00              BRK                         
A98A: 17 ; ????
A98B: 02 ; ????
A98C: 24 12           BIT     $12                 
A98E: 03 ; ????
A98F: 2D 12 03        AND     $0312               
A992: 65 02           ADC     $02                 
A994: 01 83           ORA     ($83,X)             
A996: 12 ; ????
A997: 03 ; ????
A998: 89 ; ????
A999: 12 ; ????
A99A: 03 ; ????
A99B: 9F ; ????
A99C: 17 ; ????
A99D: 02 ; ????
A99E: B2 ; ????
A99F: 12 ; ????
A9A0: 03 ; ????
A9A1: BB ; ????
A9A2: 12 ; ????
A9A3: 03 ; ????
A9A4: FD FF 03        SBC     $03FF,X             
A9A7: 00              BRK                         
A9A8: 0F ; ????
A9A9: 03 ; ????
A9AA: 03 ; ????
A9AB: 0F ; ????
A9AC: 03 ; ????
A9AD: 08              PHP                         
A9AE: 07 ; ????
A9AF: 00              BRK                         
A9B0: 26 04           ROL     $04                 
A9B2: 01 41           ORA     ($41,X)             
A9B4: 01 02           ORA     ($02,X)             
A9B6: 48              PHA                         
A9B7: 07 ; ????
A9B8: 00              BRK                         
A9B9: 49 0F           EOR     #$0F                
A9BB: 03 ; ????
A9BC: 52 ; ????
A9BD: 01 02           ORA     ($02,X)             
A9BF: 60              RTS                         
A9C0: 0F ; ????
A9C1: 03 ; ????
A9C2: 68              PLA                         
A9C3: 07 ; ????
A9C4: 00              BRK                         
A9C5: 6C 0F 03        JMP     ($030F)             
A9C8: 75 12           ADC     $12,X               
A9CA: 03 ; ????
A9CB: 84 03           STY     $03                 
A9CD: 01 A6           ORA     ($A6,X)             
A9CF: 0F ; ????
A9D0: 03 ; ????
A9D1: C9 0F           CMP     #$0F                
A9D3: 03 ; ????
A9D4: FD FF 03        SBC     $03FF,X             
A9D7: 09 0F           ORA     #$0F                
A9D9: 03 ; ????
A9DA: 0D 0F 03        ORA     $030F               
A9DD: 18              CLC                         
A9DE: 07 ; ????
A9DF: 00              BRK                         
A9E0: 26 0F           ROL     $0F                 
A9E2: 03 ; ????
A9E3: 34 ; ????
A9E4: 07 ; ????
A9E5: 00              BRK                         
A9E6: 43 ; ????
A9E7: 04 ; ????
A9E8: 01 58           ORA     ($58,X)             
A9EA: 07 ; ????
A9EB: 00              BRK                         
A9EC: 5E 12 03        LSR     $0312,X             
A9EF: 60              RTS                         
A9F0: 0F ; ????
A9F1: 03 ; ????
A9F2: 68              PLA                         
A9F3: 07 ; ????
A9F4: 00              BRK                         
A9F5: 6C 0F 03        JMP     ($030F)             
A9F8: 74 ; ????
A9F9: 07 ; ????
A9FA: 00              BRK                         
A9FB: 89 ; ????
A9FC: 04 ; ????
A9FD: 01 A6           ORA     ($A6,X)             
A9FF: 0F ; ????
AA00: 03 ; ????
AA01: B4 07           LDY     $07,X               
AA03: 00              BRK                         
AA04: C3 ; ????
AA05: 0F ; ????
AA06: 03 ; ????
AA07: FD FF 01        SBC     $01FF,X             
AA0A: 01 04           ORA     ($04,X)             
AA0C: 01 19           ORA     ($19,X)             
AA0E: 19 03 30        ORA     $3003,Y             
AA11: 0D 02 56        ORA     $5602               
AA14: 04 ; ????
AA15: 01 68           ORA     ($68,X)             
AA17: 08              PHP                         
AA18: 02 ; ????
AA19: 70 0C           BVS     $AA27               ; {}
AA1B: 02 ; ????
AA1C: 71 0C           ADC     ($0C),Y             
AA1E: 02 ; ????
AA1F: 73 ; ????
AA20: 07 ; ????
AA21: 00              BRK                         
AA22: 78              SEI                         
AA23: 07 ; ????
AA24: 00              BRK                         
AA25: 7F ; ????
AA26: 0C ; ????
AA27: 02 ; ????
AA28: 8C 05 01        STY     $0105               
AA2B: 91 00           STA     ($00),Y             ; {ram.GP_00}
AA2D: 00              BRK                         
AA2E: B0 0E           BCS     $AA3E               ; {}
AA30: 02 ; ????
AA31: B3 ; ????
AA32: 06 01           ASL     $01                 
AA34: B7 ; ????
AA35: 06 01           ASL     $01                 
AA37: CD 19 03        CMP     $0319               
AA3A: D3 ; ????
AA3B: 05 01           ORA     $01                 
AA3D: FD FF 02        SBC     $02FF,X             
AA40: 00              BRK                         
AA41: 0D 02 0C        ORA     $0C02               
AA44: 0D 02 23        ORA     $2302               
AA47: 15 02           ORA     $02,X               
AA49: 30 16           BMI     $AA61               ; {}
AA4B: 01 3E           ORA     ($3E,X)             
AA4D: 16 01           ASL     $01,X               
AA4F: 57 ; ????
AA50: 15 02           ORA     $02,X               
AA52: 70 0D           BVS     $AA61               ; {}
AA54: 02 ; ????
AA55: 7C ; ????
AA56: 0D 02 82        ORA     $8202               ; {}
AA59: 15 02           ORA     $02,X               
AA5B: B0 16           BCS     $AA73               ; {}
AA5D: 01 B6           ORA     ($B6,X)             
AA5F: 05 01           ORA     $01                 
AA61: BE 16 01        LDX     $0116,Y             
AA64: E1 04           SBC     ($04,X)             
AA66: 01 E8           ORA     ($E8,X)             
AA68: 12 ; ????
AA69: 03 ; ????
AA6A: FD FF 00        SBC     $00FF,X             
AA6D: 02 ; ????
AA6E: 07 ; ????
AA6F: 00              BRK                         
AA70: 0D 07 00        ORA     $0007               
AA73: 31 04           AND     ($04),Y             
AA75: 01 3D           ORA     ($3D,X)             
AA77: 07 ; ????
AA78: 00              BRK                         
AA79: 42 ; ????
AA7A: 07 ; ????
AA7B: 00              BRK                         
AA7C: 67 ; ????
AA7D: 02 ; ????
AA7E: 01 72           ORA     ($72,X)             
AA80: 07 ; ????
AA81: 00              BRK                         
AA82: 7D 07 00        ADC     $0007,X             
AA85: 85 19           STA     $19                 
AA87: 03 ; ????
AA88: 9B ; ????
AA89: 04 ; ????
AA8A: 01 B2           ORA     ($B2,X)             
AA8C: 07 ; ????
AA8D: 00              BRK                         
AA8E: BD 07 00        LDA     $0007,X             
AA91: C1 05           CMP     ($05,X)             
AA93: 01 FD           ORA     ($FD,X)             
AA95: FF ; ????
AA96: 01 06           ORA     ($06,X)             
AA98: 19 03 0C        ORA     $0C03,Y             
AA9B: 06 02           ASL     $02                 
AA9D: 10 0B           BPL     $AAAA               ; {}
AA9F: 01 22           ORA     ($22,X)             
AAA1: 07 ; ????
AAA2: 00              BRK                         
AAA3: 2A              ROL     A                   
AAA4: 05 01           ORA     $01                 
AAA6: 37 ; ????
AAA7: 06 02           ASL     $02                 
AAA9: 47 ; ????
AAAA: 04 ; ????
AAAB: 01 58           ORA     ($58,X)             
AAAD: 07 ; ????
AAAE: 00              BRK                         
AAAF: 5C ; ????
AAB0: 0A              ASL     A                   
AAB1: 02 ; ????
AAB2: 61 06           ADC     ($06,X)             
AAB4: 02 ; ????
AAB5: 70 02           BVS     $AAB9               ; {}
AAB7: 01 7C           ORA     ($7C,X)             
AAB9: 0B ; ????
AABA: 01 8D           ORA     ($8D,X)             
AABC: 07 ; ????
AABD: 00              BRK                         
AABE: 96 06           STX     $06,Y               
AAC0: 02 ; ????
AAC1: A0 05           LDY     #$05                
AAC3: 01 CC           ORA     ($CC,X)             
AAC5: 06 02           ASL     $02                 
AAC7: D2 ; ????
AAC8: 19 03 E8        ORA     $E803,Y             
AACB: 05 01           ORA     $01                 
AACD: FD FF 00        SBC     $00FF,X             
AAD0: 0C ; ????
AAD1: 0A              ASL     A                   
AAD2: 00              BRK                         
AAD3: 11 05           ORA     ($05),Y             
AAD5: 01 2C           ORA     ($2C,X)             
AAD7: 0B ; ????
AAD8: 03 ; ????
AAD9: 3C ; ????
AADA: 07 ; ????
AADB: 00              BRK                         
AADC: 48              PHA                         
AADD: 03 ; ????
AADE: 01 52           ORA     ($52,X)             
AAE0: 08              PHP                         
AAE1: 02 ; ????
AAE2: 62 ; ????
AAE3: 07 ; ????
AAE4: 00              BRK                         
AAE5: 70 03           BVS     $AAEA               ; {}
AAE7: 01 78           ORA     ($78,X)             
AAE9: 08              PHP                         
AAEA: 02 ; ????
AAEB: 7C ; ????
AAEC: 06 02           ASL     $02                 
AAEE: 88              DEY                         
AAEF: 07 ; ????
AAF0: 00              BRK                         
AAF1: 9C ; ????
AAF2: 05 01           ORA     $01                 
AAF4: A0 06           LDY     #$06                
AAF6: 02 ; ????
AAF7: AD 08 02        LDA     $0208               
AAFA: BD 07 00        LDA     $0007,X             
AAFD: C2 ; ????
AAFE: 05 01           ORA     $01                 
AB00: FD FF 02        SBC     $02FF,X             
AB03: 60              RTS                         
AB04: 05 01           ORA     $01                 
AB06: 68              PLA                         
AB07: 05 01           ORA     $01                 
AB09: A0 06           LDY     #$06                
AB0B: 02 ; ????
AB0C: A4 06           LDY     $06                 
AB0E: 02 ; ????
AB0F: A8              TAY                         
AB10: 06 02           ASL     $02                 
AB12: AC 06 02        LDY     $0206               
AB15: FD FF 01        SBC     $01FF,X             
AB18: 10 05           BPL     $AB1F               ; {}
AB1A: 01 18           ORA     ($18,X)             
AB1C: 05 01           ORA     $01                 
AB1E: 20 0C 01        JSR     $010C               
AB21: 2F ; ????
AB22: 0C ; ????
AB23: 01 41           ORA     ($41,X)             
AB25: 17 ; ????
AB26: 03 ; ????
AB27: 4D 0E 03        EOR     $030E               
AB2A: 60              RTS                         
AB2B: 0C ; ????
AB2C: 01 6F           ORA     ($6F,X)             
AB2E: 0C ; ????
AB2F: 01 71           ORA     ($71,X)             
AB31: 02 ; ????
AB32: 01 7C           ORA     ($7C,X)             
AB34: 0E 03 8E        ASL     $8E03               ; {}
AB37: 13 ; ????
AB38: 00              BRK                         
AB39: 90 0C           BCC     $AB47               ; {}
AB3B: 01 A0           ORA     ($A0,X)             
AB3D: 0E 03 A6        ASL     $A603               ; {}
AB40: 03 ; ????
AB41: 01 AB           ORA     ($AB,X)             
AB43: 0E 03 AE        ASL     $AE03               ; {}
AB46: 16 00           ASL     $00,X               ; {ram.GP_00}
AB48: D0 05           BNE     $AB4F               ; {}
AB4A: 01 D8           ORA     ($D8,X)             
AB4C: 05 01           ORA     $01                 
AB4E: FD FF 02        SBC     $02FF,X             
AB51: 10 0B           BPL     $AB5E               ; {}
AB53: 02 ; ????
AB54: 14 ; ????
AB55: 0B ; ????
AB56: 02 ; ????
AB57: 18              CLC                         
AB58: 0B ; ????
AB59: 02 ; ????
AB5A: 1C ; ????
AB5B: 0B ; ????
AB5C: 02 ; ????
AB5D: 20 16 00        JSR     $0016               
AB60: 2F ; ????
AB61: 16 00           ASL     $00,X               ; {ram.GP_00}
AB63: 40              RTI                         
AB64: 0C ; ????
AB65: 02 ; ????
AB66: 6E 16 00        ROR     $0016               
AB69: 80 ; ????
AB6A: 0C ; ????
AB6B: 02 ; ????
AB6C: 8E 13 02        STX     $0213               
AB6F: AD 0D 02        LDA     $020D               
AB72: C0 0D           CPY     #$0D                
AB74: 02 ; ????
AB75: C1 09           CMP     ($09,X)             
AB77: 03 ; ????
AB78: C4 0D           CPY     $0D                 
AB7A: 02 ; ????
AB7B: C8              INY                         
AB7C: 0D 02 CC        ORA     $CC02               
AB7F: 09 03           ORA     #$03                
AB81: DC ; ????
AB82: 0D 02 FD        ORA     $FD02               
AB85: FF ; ????
AB86: 01 46           ORA     ($46,X)             
AB88: 05 01           ORA     $01                 
AB8A: 4E 14 01        LSR     $0114               
AB8D: 50 05           BVC     $AB94               ; {}
AB8F: 01 60           ORA     ($60,X)             
AB91: 14 ; ????
AB92: 01 6F           ORA     ($6F,X)             
AB94: 14 ; ????
AB95: 01 8E           ORA     ($8E,X)             
AB97: 13 ; ????
AB98: 00              BRK                         
AB99: A0 15           LDY     #$15                
AB9B: 01 A5           ORA     ($A5,X)             
AB9D: 08              PHP                         
AB9E: 02 ; ????
AB9F: A9 08           LDA     #$08                
ABA1: 02 ; ????
ABA2: AC 15 01        LDY     $0115               
ABA5: B2 ; ????
ABA6: 15 01           ORA     $01,X               
ABA8: B6 11           LDX     $11,Y               
ABAA: 03 ; ????
ABAB: B9 15 01        LDA     $0115,Y             
ABAE: C4 15           CPY     $15                 
ABB0: 01 C8           ORA     ($C8,X)             
ABB2: 15 01           ORA     $01,X               
ABB4: FD FF 01        SBC     $01FF,X             
ABB7: 51 01           EOR     ($01),Y             
ABB9: 52 ; ????
ABBA: FF ; ????
ABBB: 01 05           ORA     ($05,X)             
ABBD: 01 06           ORA     ($06,X)             
ABBF: FF ; ????
ABC0: 02 ; ????
ABC1: 40              RTI                         
ABC2: 42 ; ????
ABC3: FF ; ????
ABC4: 03 ; ????
ABC5: 40              RTI                         
ABC6: 41 42           EOR     ($42,X)             
ABC8: FF ; ????
ABC9: 04 ; ????
ABCA: 40              RTI                         
ABCB: 41 41           EOR     ($41,X)             
ABCD: 42 ; ????
ABCE: FF ; ????
ABCF: 08              PHP                         
ABD0: 40              RTI                         
ABD1: 41 41           EOR     ($41,X)             
ABD3: 41 41           EOR     ($41,X)             
ABD5: 41 41           EOR     ($41,X)             
ABD7: 42 ; ????
ABD8: FF ; ????
ABD9: 04 ; ????
ABDA: 58              CLI                         
ABDB: 58              CLI                         
ABDC: 58              CLI                         
ABDD: 58              CLI                         
ABDE: 04 ; ????
ABDF: 07 ; ????
ABE0: 07 ; ????
ABE1: 07 ; ????
ABE2: 07 ; ????
ABE3: FF ; ????
ABE4: 01 07           ORA     ($07,X)             
ABE6: 01 08           ORA     ($08,X)             
ABE8: 01 08           ORA     ($08,X)             
ABEA: 01 07           ORA     ($07,X)             
ABEC: FF ; ????
ABED: 01 0C           ORA     ($0C,X)             
ABEF: FF ; ????
ABF0: 03 ; ????
ABF1: 30 30           BMI     $AC23               ; {}
ABF3: 30 FF           BMI     $ABF4               ; {}
ABF5: 04 ; ????
ABF6: 00              BRK                         
ABF7: 00              BRK                         
ABF8: 09 0A           ORA     #$0A                
ABFA: 04 ; ????
ABFB: 09 0A           ORA     #$0A                
ABFD: 5E 5E FF        LSR     $FF5E,X             
AC00: 04 ; ????
AC01: 56 56           LSR     $56,X               
AC03: 56 56           LSR     $56,X               
AC05: FF ; ????
AC06: 01 5E           ORA     ($5E,X)             
AC08: 01 5F           ORA     ($5F,X)             
AC0A: 01 5E           ORA     ($5E,X)             
AC0C: 01 5F           ORA     ($5F,X)             
AC0E: FF ; ????
AC0F: 04 ; ????
AC10: 5E 5F 5E        LSR     $5E5F,X             
AC13: 5F ; ????
AC14: 04 ; ????
AC15: 5F ; ????
AC16: 5E 5F 5E        LSR     $5E5F,X             
AC19: 04 ; ????
AC1A: 5E 5F 5E        LSR     $5E5F,X             
AC1D: 5F ; ????
AC1E: 04 ; ????
AC1F: 5F ; ????
AC20: 5E 5F 5E        LSR     $5E5F,X             
AC23: FF ; ????
AC24: 04 ; ????
AC25: 5E 5F 5E        LSR     $5E5F,X             
AC28: 5F ; ????
AC29: FF ; ????
AC2A: 04 ; ????
AC2B: 53 ; ????
AC2C: 54 ; ????
AC2D: 54 ; ????
AC2E: 55 FF           EOR     $FF,X               
AC30: 01 50           ORA     ($50,X)             
AC32: 01 29           ORA     ($29,X)             
AC34: FF ; ????
AC35: 03 ; ????
AC36: 38              SEC                         
AC37: 38              SEC                         
AC38: 38              SEC                         
AC39: FF ; ????
AC3A: 01 33           ORA     ($33,X)             
AC3C: FF ; ????
AC3D: 01 50           ORA     ($50,X)             
AC3F: 01 21           ORA     ($21,X)             
AC41: FF ; ????
AC42: 01 60           ORA     ($60,X)             
AC44: 01 60           ORA     ($60,X)             
AC46: 01 60           ORA     ($60,X)             
AC48: 01 60           ORA     ($60,X)             
AC4A: FF ; ????
AC4B: 04 ; ????
AC4C: 60              RTS                         
AC4D: 60              RTS                         
AC4E: 60              RTS                         
AC4F: 60              RTS                         
AC50: FF ; ????
AC51: 02 ; ????
AC52: 57 ; ????
AC53: 57 ; ????
AC54: 02 ; ????
AC55: 57 ; ????
AC56: 57 ; ????
AC57: 02 ; ????
AC58: 57 ; ????
AC59: 57 ; ????
AC5A: 02 ; ????
AC5B: 57 ; ????
AC5C: 57 ; ????
AC5D: FF ; ????
AC5E: 01 5E           ORA     ($5E,X)             
AC60: FF ; ????
AC61: 01 57           ORA     ($57,X)             
AC63: FF ; ????
AC64: 01 0B           ORA     ($0B,X)             
AC66: FF ; ????
AC67: 12 ; ????
AC68: 12 ; ????
AC69: 12 ; ????
AC6A: 12 ; ????
AC6B: 7B ; ????
AC6C: 12 ; ????
AC6D: 12 ; ????
AC6E: 12 ; ????
AC6F: 7B ; ????
AC70: 12 ; ????
AC71: 12 ; ????
AC72: 12 ; ????
AC73: 7B ; ????
AC74: 12 ; ????
AC75: 12 ; ????
AC76: 12 ; ????
AC77: 7B ; ????
AC78: 12 ; ????
AC79: 12 ; ????
AC7A: 12 ; ????
AC7B: 70 71           BVS     $ACEE               ; {}
AC7D: 72 ; ????
AC7E: 73 ; ????
AC7F: 72 ; ????
AC80: 73 ; ????
AC81: 72 ; ????
AC82: 73 ; ????
AC83: 8F ; ????
AC84: 90 6D           BCC     $ACF3               ; {}
AC86: 6E 91 92        ROR     $9291               ; {}
AC89: 91 92           STA     ($92),Y             
AC8B: 12 ; ????
AC8C: 12 ; ????
AC8D: DC ; ????
AC8E: DD DC DD        CMP     $DDDC,X             
AC91: DE DF E4        DEC     $E4DF,X             
AC94: 12 ; ????
AC95: 12 ; ????
AC96: 12 ; ????
AC97: D8              CLD                         
AC98: D9 DA DB        CMP     $DBDA,Y             
AC9B: 7B ; ????
AC9C: 12 ; ????
AC9D: 12 ; ????
AC9E: 12 ; ????
AC9F: 7B ; ????
ACA0: 12 ; ????
ACA1: 12 ; ????
ACA2: 12 ; ????
ACA3: 7B ; ????
ACA4: 12 ; ????
ACA5: 12 ; ????
ACA6: 12 ; ????
ACA7: 7B ; ????
ACA8: 12 ; ????
ACA9: 12 ; ????
ACAA: 12 ; ????
ACAB: 7B ; ????
ACAC: 12 ; ????
ACAD: 12 ; ????
ACAE: 12 ; ????
ACAF: 7B ; ????
ACB0: 12 ; ????
ACB1: 12 ; ????
ACB2: 12 ; ????
ACB3: 7B ; ????
ACB4: 12 ; ????
ACB5: 12 ; ????
ACB6: 12 ; ????
ACB7: 7B ; ????
ACB8: 12 ; ????
ACB9: 12 ; ????
ACBA: 12 ; ????
ACBB: 7B ; ????
ACBC: 12 ; ????
ACBD: 12 ; ????
ACBE: 12 ; ????
ACBF: 7B ; ????
ACC0: 12 ; ????
ACC1: 12 ; ????
ACC2: 12 ; ????
ACC3: 7B ; ????
ACC4: 12 ; ????
ACC5: 12 ; ????
ACC6: 12 ; ????
ACC7: 7B ; ????
ACC8: 12 ; ????
ACC9: 12 ; ????
ACCA: 12 ; ????
ACCB: 7B ; ????
ACCC: 12 ; ????
ACCD: 12 ; ????
ACCE: 12 ; ????
ACCF: 7B ; ????
ACD0: 12 ; ????
ACD1: 12 ; ????
ACD2: 12 ; ????
ACD3: 7B ; ????
ACD4: 12 ; ????
ACD5: 12 ; ????
ACD6: 12 ; ????
ACD7: 7B ; ????
ACD8: 12 ; ????
ACD9: 12 ; ????
ACDA: 12 ; ????
ACDB: 7B ; ????
ACDC: 12 ; ????
ACDD: 12 ; ????
ACDE: 12 ; ????
ACDF: 7B ; ????
ACE0: 12 ; ????
ACE1: 12 ; ????
ACE2: 12 ; ????
ACE3: 7B ; ????
ACE4: 12 ; ????
ACE5: 12 ; ????
ACE6: 12 ; ????
ACE7: 64 ; ????
ACE8: 65 64           ADC     $64                 
ACEA: 65 64           ADC     $64                 
ACEC: 65 64           ADC     $64                 
ACEE: 65 64           ADC     $64                 
ACF0: 65 64           ADC     $64                 
ACF2: 65 64           ADC     $64                 
ACF4: 65 64           ADC     $64                 
ACF6: 65 64           ADC     $64                 
ACF8: 65 64           ADC     $64                 
ACFA: 65 64           ADC     $64                 
ACFC: 65 64           ADC     $64                 
ACFE: 65 64           ADC     $64                 
AD00: 65 64           ADC     $64                 
AD02: 65 64           ADC     $64                 
AD04: 65 64           ADC     $64                 
AD06: 65 7B           ADC     $7B                 
AD08: 12 ; ????
AD09: 12 ; ????
AD0A: 12 ; ????
AD0B: 64 ; ????
AD0C: 65 64           ADC     $64                 
AD0E: 65 7B           ADC     $7B                 
AD10: 12 ; ????
AD11: 12 ; ????
AD12: 12 ; ????
AD13: 7B ; ????
AD14: 12 ; ????
AD15: 12 ; ????
AD16: 12 ; ????
AD17: 7B ; ????
AD18: 12 ; ????
AD19: 12 ; ????
AD1A: 12 ; ????
AD1B: 7B ; ????
AD1C: 12 ; ????
AD1D: 12 ; ????
AD1E: 12 ; ????
AD1F: 7B ; ????
AD20: 12 ; ????
AD21: 12 ; ????
AD22: 12 ; ????
AD23: 7B ; ????
AD24: 12 ; ????
AD25: 12 ; ????
AD26: 12 ; ????
AD27: AA              TAX                         
AD28: AA              TAX                         
AD29: AB ; ????
AD2A: AB ; ????
AD2B: 7B ; ????
AD2C: 12 ; ????
AD2D: 12 ; ????
AD2E: 12 ; ????
AD2F: 7B ; ????
AD30: 12 ; ????
AD31: 12 ; ????
AD32: 12 ; ????
AD33: E9 EA           SBC     #$EA                
AD35: EB ; ????
AD36: EC 7B 12        CPX     $127B               
AD39: 12 ; ????
AD3A: 12 ; ????
AD3B: 7B ; ????
AD3C: 12 ; ????
AD3D: 12 ; ????
AD3E: 12 ; ????
AD3F: 7B ; ????
AD40: 12 ; ????
AD41: 12 ; ????
AD42: 12 ; ????
AD43: 7B ; ????
AD44: 12 ; ????
AD45: 12 ; ????
AD46: 12 ; ????
AD47: 4D 4D B2        EOR     $B24D               ; {}
AD4A: B2 ; ????
AD4B: 7B ; ????
AD4C: 12 ; ????
AD4D: 12 ; ????
AD4E: 12 ; ????
AD4F: 7B ; ????
AD50: 12 ; ????
AD51: 12 ; ????
AD52: 12 ; ????
AD53: 7B ; ????
AD54: 12 ; ????
AD55: 12 ; ????
AD56: 12 ; ????
AD57: 7B ; ????
AD58: 12 ; ????
AD59: 12 ; ????
AD5A: 12 ; ????
AD5B: 7B ; ????
AD5C: 12 ; ????
AD5D: 12 ; ????
AD5E: 12 ; ????
AD5F: 7B ; ????
AD60: 12 ; ????
AD61: 12 ; ????
AD62: 12 ; ????
AD63: 7B ; ????
AD64: 12 ; ????
AD65: 12 ; ????
AD66: 12 ; ????
AD67: D0 D1           BNE     $AD3A               ; {}
AD69: C4 C5           CPY     $C5                 
AD6B: D2 ; ????
AD6C: D1 C5           CMP     ($C5),Y             
AD6E: C6 D2           DEC     $D2                 
AD70: D3 ; ????
AD71: C5 C7           CMP     $C7                 
AD73: 7B ; ????
AD74: 12 ; ????
AD75: 12 ; ????
AD76: 12 ; ????
AD77: 7B ; ????
AD78: 12 ; ????
AD79: 12 ; ????
AD7A: 12 ; ????
AD7B: 7B ; ????
AD7C: 12 ; ????
AD7D: 12 ; ????
AD7E: 12 ; ????
AD7F: 7B ; ????
AD80: 12 ; ????
AD81: 12 ; ????
AD82: 12 ; ????
AD83: 7B ; ????
AD84: 12 ; ????
AD85: 12 ; ????
AD86: 12 ; ????
AD87: 7B ; ????
AD88: 12 ; ????
AD89: 12 ; ????
AD8A: 12 ; ????
AD8B: 7B ; ????
AD8C: 12 ; ????
AD8D: 12 ; ????
AD8E: 12 ; ????
AD8F: 7B ; ????
AD90: 12 ; ????
AD91: 12 ; ????
AD92: 12 ; ????
AD93: 7B ; ????
AD94: 12 ; ????
AD95: 12 ; ????
AD96: 12 ; ????
AD97: 7B ; ????
AD98: 12 ; ????
AD99: 12 ; ????
AD9A: 12 ; ????
AD9B: 7B ; ????
AD9C: 12 ; ????
AD9D: 12 ; ????
AD9E: 12 ; ????
AD9F: 7B ; ????
ADA0: 12 ; ????
ADA1: 12 ; ????
ADA2: 12 ; ????
ADA3: 7B ; ????
ADA4: 12 ; ????
ADA5: 12 ; ????
ADA6: 12 ; ????
ADA7: 60              RTS                         
ADA8: 61 64           ADC     ($64,X)             
ADAA: 65 60           ADC     $60                 
ADAC: 61 62           ADC     ($62,X)             
ADAE: 63 ; ????
ADAF: 62 ; ????
ADB0: 63 ; ????
ADB1: 62 ; ????
ADB2: 63 ; ????
ADB3: C8              INY                         
ADB4: C9 CC           CMP     #$CC                
ADB6: CD CA C9        CMP     $C9CA               
ADB9: CE CD CA        DEC     $CACD               
ADBC: CB ; ????
ADBD: CE CF D4        DEC     $D4CF               
ADC0: D5 D6           CMP     $D6,X               
ADC2: D7 ; ????
ADC3: E5 E6           SBC     $E6                 
ADC5: E7 ; ????
ADC6: E8              INX                         
ADC7: 53 ; ????
ADC8: 52 ; ????
ADC9: 52 ; ????
ADCA: 53 ; ????
ADCB: 79 79 79        ADC     $7979,Y             
ADCE: 79 7B 12        ADC     $127B,Y             
ADD1: 12 ; ????
ADD2: 12 ; ????
ADD3: 7B ; ????
ADD4: 12 ; ????
ADD5: 12 ; ????
ADD6: 12 ; ????
ADD7: 7B ; ????
ADD8: 12 ; ????
ADD9: 12 ; ????
ADDA: 12 ; ????
ADDB: 7B ; ????
ADDC: 12 ; ????
ADDD: 12 ; ????
ADDE: 12 ; ????
ADDF: E0 E1           CPX     #$E1                
ADE1: E2 ; ????
ADE2: E3 ; ????
ADE3: DF ; ????
ADE4: DE DE E3        DEC     $E3DE,X             
ADE7: B1 B1           LDA     ($B1),Y             
ADE9: B1 B1           LDA     ($B1),Y             
ADEB: 7B ; ????
ADEC: 12 ; ????
ADED: 12 ; ????
ADEE: 12 ; ????
ADEF: 7B ; ????
ADF0: 12 ; ????
ADF1: 12 ; ????
ADF2: 12 ; ????
ADF3: 7B ; ????
ADF4: 12 ; ????
ADF5: 12 ; ????
ADF6: 12 ; ????
ADF7: 7B ; ????
ADF8: 12 ; ????
ADF9: 12 ; ????
ADFA: 12 ; ????
ADFB: 7B ; ????
ADFC: 12 ; ????
ADFD: 12 ; ????
ADFE: 12 ; ????
ADFF: 7B ; ????
AE00: 12 ; ????
AE01: 12 ; ????
AE02: 12 ; ????
AE03: 7B ; ????
AE04: 12 ; ????
AE05: 12 ; ????
AE06: 12 ; ????
AE07: 7B ; ????
AE08: 12 ; ????
AE09: 12 ; ????
AE0A: 12 ; ????
AE0B: 7B ; ????
AE0C: 12 ; ????
AE0D: 12 ; ????
AE0E: 12 ; ????
AE0F: 7B ; ????
AE10: 12 ; ????
AE11: 12 ; ????
AE12: 12 ; ????
AE13: 7B ; ????
AE14: 12 ; ????
AE15: 12 ; ????
AE16: 12 ; ????
AE17: 7B ; ????
AE18: 12 ; ????
AE19: 12 ; ????
AE1A: 12 ; ????
AE1B: 7B ; ????
AE1C: 12 ; ????
AE1D: 12 ; ????
AE1E: 12 ; ????
AE1F: 7B ; ????
AE20: 12 ; ????
AE21: 12 ; ????
AE22: 12 ; ????
AE23: A1 A2           LDA     ($A2,X)             
AE25: A3 ; ????
AE26: A4 7B           LDY     $7B                 
AE28: 12 ; ????
AE29: 12 ; ????
AE2A: 12 ; ????
AE2B: 00              BRK                         
AE2C: 06 B7           ASL     $B7                 
AE2E: 00              BRK                         
AE2F: 01 02           ORA     ($02,X)             
AE31: D7 ; ????
AE32: 00              BRK                         
AE33: 01 06           ORA     ($06,X)             
AE35: 97 ; ????
AE36: 00              BRK                         
AE37: 01 07           ORA     ($07,X)             
AE39: 97 ; ????
AE3A: 00              BRK                         
AE3B: 02 ; ????
AE3C: 02 ; ????
AE3D: 97 ; ????
AE3E: 00              BRK                         
AE3F: 02 ; ????
AE40: 03 ; ????
AE41: 97 ; ????
AE42: 00              BRK                         
AE43: 02 ; ????
AE44: 07 ; ????
AE45: 07 ; ????
AE46: 00              BRK                         
AE47: FF ; ????
AE48: FF ; ????
AE49: FF ; ????
AE4A: FF ; ????
AE4B: 00              BRK                         
AE4C: 08              PHP                         
AE4D: E7 ; ????
AE4E: 00              BRK                         
AE4F: 01 02           ORA     ($02,X)             
AE51: 77 ; ????
AE52: 00              BRK                         
AE53: 01 06           ORA     ($06,X)             
AE55: 37 ; ????
AE56: 00              BRK                         
AE57: 01 07           ORA     ($07,X)             
AE59: 37 ; ????
AE5A: 00              BRK                         
AE5B: 02 ; ????
AE5C: 02 ; ????
AE5D: 37 ; ????
AE5E: 00              BRK                         
AE5F: 02 ; ????
AE60: 03 ; ????
AE61: 37 ; ????
AE62: 00              BRK                         
AE63: FF ; ????
AE64: FF ; ????
AE65: FF ; ????
AE66: FF ; ????
AE67: FF ; ????
AE68: FF ; ????
AE69: FF ; ????
AE6A: FF ; ????
AE6B: 01 01           ORA     ($01,X)             
AE6D: D7 ; ????
AE6E: 00              BRK                         
AE6F: 01 03           ORA     ($03,X)             
AE71: E7 ; ????
AE72: 00              BRK                         
AE73: 01 06           ORA     ($06,X)             
AE75: 07 ; ????
AE76: 00              BRK                         
AE77: 01 07           ORA     ($07,X)             
AE79: 07 ; ????
AE7A: 00              BRK                         
AE7B: 02 ; ????
AE7C: 02 ; ????
AE7D: 07 ; ????
AE7E: 00              BRK                         
AE7F: 02 ; ????
AE80: 03 ; ????
AE81: 07 ; ????
AE82: 00              BRK                         
AE83: FF ; ????
AE84: FF ; ????
AE85: FF ; ????
AE86: FF ; ????
AE87: FF ; ????
AE88: FF ; ????
AE89: FF ; ????
AE8A: FF ; ????
AE8B: 01 01           ORA     ($01,X)             
AE8D: 77 ; ????
AE8E: 00              BRK                         
AE8F: 01 06           ORA     ($06,X)             
AE91: C7 ; ????
AE92: 00              BRK                         
AE93: 01 07           ORA     ($07,X)             
AE95: C7 ; ????
AE96: 00              BRK                         
AE97: 02 ; ????
AE98: 02 ; ????
AE99: C7 ; ????
AE9A: 00              BRK                         
AE9B: 02 ; ????
AE9C: 03 ; ????
AE9D: C7 ; ????
AE9E: 00              BRK                         
AE9F: 02 ; ????
AEA0: 06 07           ASL     $07                 
AEA2: 00              BRK                         
AEA3: FF ; ????
AEA4: FF ; ????
AEA5: FF ; ????
AEA6: FF ; ????
AEA7: FF ; ????
AEA8: FF ; ????
AEA9: FF ; ????
AEAA: FF ; ????
AEAB: 00              BRK                         
AEAC: 05 F0           ORA     $F0                 
AEAE: 05 00           ORA     $00                 ; {ram.GP_00}
AEB0: 05 F0           ORA     $F0                 
AEB2: 05 00           ORA     $00                 ; {ram.GP_00}
AEB4: 04 ; ????
AEB5: 40              RTI                         
AEB6: 04 ; ????
AEB7: 00              BRK                         
AEB8: 04 ; ????
AEB9: 40              RTI                         
AEBA: 04 ; ????
AEBB: 55 77           EOR     $77,X               
AEBD: 6D 77 8B        ADC     $8B77               ; {}
AEC0: 77 ; ????
AEC1: 72 ; ????
AEC2: 73 ; ????
AEC3: 87 ; ????
AEC4: 73 ; ????
AEC5: 72 ; ????
AEC6: 73 ; ????
AEC7: 87 ; ????
AEC8: 73 ; ????
AEC9: 72 ; ????
AECA: 73 ; ????
AECB: C0 73           CPY     #$73                
AECD: 72 ; ????
AECE: 73 ; ????
AECF: C0 73           CPY     #$73                
AED1: 72 ; ????
AED2: 73 ; ????
AED3: C0 73           CPY     #$73                
AED5: 72 ; ????
AED6: 73 ; ????
AED7: C0 73           CPY     #$73                
AED9: 72 ; ????
AEDA: 73 ; ????
AEDB: F6 73           INC     $73,X               
AEDD: 72 ; ????
AEDE: 73 ; ????
AEDF: 87 ; ????
AEE0: 73 ; ????
AEE1: 72 ; ????
AEE2: 73 ; ????
AEE3: 72 ; ????
AEE4: 73 ; ????
AEE5: B7 ; ????
AEE6: 70 F3           BVS     $AEDB               ; {}
AEE8: 70 F3           BVS     $AEDD               ; {}
AEEA: 70 F3           BVS     $AEDF               ; {}
AEEC: 70 0E           BVS     $AEFC               ; {}
AEEE: 71 0E           ADC     ($0E),Y             
AEF0: 71 2F           ADC     ($2F),Y             
AEF2: 71 4D           ADC     ($4D),Y             
AEF4: 71 86           ADC     ($86),Y             
AEF6: 71 86           ADC     ($86),Y             
AEF8: 71 00           ADC     ($00),Y             ; {ram.GP_00}
AEFA: 70 FF           BVS     $AEFB               ; {}
AEFC: FF ; ????
AEFD: B7 ; ????
AEFE: 70 DA           BVS     $AEDA               ; {}
AF00: 71 DA           ADC     ($DA),Y             
AF02: 71 86           ADC     ($86),Y             
AF04: 71 AD           ADC     ($AD),Y             
AF06: 71 AD           ADC     ($AD),Y             
AF08: 71 F8           ADC     ($F8),Y             
AF0A: 71 F8           ADC     ($F8),Y             
AF0C: 71 16           ADC     ($16),Y             
AF0E: 72 ; ????
AF0F: 46 72           LSR     $72                 
AF11: 16 72           ASL     $72,X               
AF13: 46 72           LSR     $72                 
AF15: F3 ; ????
AF16: 70 2D           BVS     $AF45               ; {}
AF18: 70 FF           BVS     $AF19               ; {}
AF1A: FF ; ????
AF1B: 79 72 0E        ADC     $0E72,Y             
AF1E: 71 F8           ADC     ($F8),Y             
AF20: 71 F8           ADC     ($F8),Y             
AF22: 71 AF           ADC     ($AF),Y             
AF24: 72 ; ????
AF25: AF ; ????
AF26: 72 ; ????
AF27: DC ; ????
AF28: 72 ; ????
AF29: DC ; ????
AF2A: 72 ; ????
AF2B: 16 72           ASL     $72,X               
AF2D: 46 72           LSR     $72                 
AF2F: 86 71           STX     $71                 
AF31: F3 ; ????
AF32: 70 4D           BVS     $AF81               ; {}
AF34: 71 06           ADC     ($06),Y             
AF36: 73 ; ????
AF37: 3F ; ????
AF38: 73 ; ????
AF39: 66 70           ROR     $70                 
AF3B: FF ; ????
AF3C: FF ; ????
AF3D: 26 74           ROL     $74                 
AF3F: 2B ; ????
AF40: 74 ; ????
AF41: 30 74           BMI     $AFB7               ; {}
AF43: 34 ; ????
AF44: 74 ; ????
AF45: 39 74 3F        AND     $3F74,Y             
AF48: 74 ; ????
AF49: 49 74           EOR     #$74                
AF4B: 54 ; ????
AF4C: 74 ; ????
AF4D: 5D 74 60        EOR     $6074,X             
AF50: 74 ; ????
AF51: 65 74           ADC     $74                 
AF53: 70 74           BVS     $AFC9               ; {}
AF55: 76 74           ROR     $74,X               
AF57: 7F ; ????
AF58: 74 ; ????
AF59: 94 74           STY     $74,X               
AF5B: 9A              TXS                         
AF5C: 74 ; ????
AF5D: A0 74           LDY     #$74                
AF5F: A5 74           LDA     $74                 
AF61: AA              TAX                         
AF62: 74 ; ????
AF63: AD 74 B2        LDA     $B274               ; {}
AF66: 74 ; ????
AF67: BB ; ????
AF68: 74 ; ????
AF69: C1 74           CMP     ($74,X)             
AF6B: CE 74 D1        DEC     $D174               
AF6E: 74 ; ????
AF6F: D4 ; ????
AF70: 74 ; ????
AF71: E7 ; ????
AF72: 77 ; ????
AF73: F2 ; ????
AF74: 77 ; ????
AF75: 07 ; ????
AF76: 78              SEI                         
AF77: 00              BRK                         
AF78: 00              BRK                         
AF79: 0B ; ????
AF7A: 0B ; ????
AF7B: 0B ; ????
AF7C: 00              BRK                         
AF7D: 00              BRK                         
AF7E: 07 ; ????
AF7F: 07 ; ????
AF80: 0B ; ????
AF81: 0C ; ????
AF82: 00              BRK                         
AF83: 00              BRK                         
AF84: 00              BRK                         
AF85: 00              BRK                         
AF86: 08              PHP                         
AF87: 08              PHP                         
AF88: 00              BRK                         
AF89: 00              BRK                         
AF8A: 00              BRK                         
AF8B: 0A              ASL     A                   
AF8C: 0A              ASL     A                   
AF8D: 0A              ASL     A                   
AF8E: 0A              ASL     A                   
AF8F: 08              PHP                         
AF90: 00              BRK                         
AF91: 0B ; ????
AF92: 0B ; ????
AF93: 00              BRK                         
AF94: 0A              ASL     A                   
AF95: 0B ; ????
AF96: 0B ; ????
AF97: 00              BRK                         
AF98: 08              PHP                         
AF99: 08              PHP                         
AF9A: 00              BRK                         
AF9B: 00              BRK                         
AF9C: 0A              ASL     A                   
AF9D: 0A              ASL     A                   
AF9E: 0A              ASL     A                   
AF9F: 0A              ASL     A                   
AFA0: 0A              ASL     A                   
AFA1: 0A              ASL     A                   
AFA2: 0A              ASL     A                   
AFA3: 0B ; ????
AFA4: 0A              ASL     A                   
AFA5: 08              PHP                         
AFA6: 0A              ASL     A                   
AFA7: 00              BRK                         
AFA8: 0A              ASL     A                   
AFA9: 0A              ASL     A                   
AFAA: 0A              ASL     A                   
AFAB: 21 78           AND     ($78,X)             
AFAD: 2C 78 41        BIT     $4178               
AFB0: 78              SEI                         
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
AFE5: 5B ; ????
AFE6: 78              SEI                         
AFE7: 66 78           ROR     $78                 
AFE9: 7B ; ????
AFEA: 78              SEI                         
AFEB: 00              BRK                         
AFEC: 02 ; ????
AFED: 03 ; ????
AFEE: 03 ; ????
AFEF: 03 ; ????
AFF0: 00              BRK                         
AFF1: 0D 03 02        ORA     $0203               
AFF4: 02 ; ????
AFF5: 03 ; ????
AFF6: 00              BRK                         
AFF7: 0D 0D 02        ORA     $020D               
AFFA: 00              BRK                         
AFFB: 0D 00 00        ORA     $0000               ; {ram.GP_00}
AFFE: 03 ; ????
AFFF: 02 ; ????
B000: 02 ; ????
B001: 02 ; ????
B002: 02 ; ????
B003: 02 ; ????
B004: 03 ; ????
B005: 03 ; ????
B006: 00              BRK                         
B007: 0D 00 03        ORA     $0300               
B00A: 03 ; ????
B00B: 00              BRK                         
B00C: 02 ; ????
B00D: 03 ; ????
B00E: 03 ; ????
B00F: 03 ; ????
B010: 03 ; ????
B011: 03 ; ????
B012: 03 ; ????
B013: 02 ; ????
B014: 02 ; ????
B015: 03 ; ????
B016: 00              BRK                         
B017: 0D 00 0D        ORA     $0D00               
B01A: 00              BRK                         
B01B: 02 ; ????
B01C: 03 ; ????
B01D: 03 ; ????
B01E: 02 ; ????
B01F: 95 78           STA     $78,X               
B021: A0 78           LDY     #$78                
B023: B5 78           LDA     $78,X               
B025: 00              BRK                         
B026: 00              BRK                         
B027: 00              BRK                         
B028: 00              BRK                         
B029: 00              BRK                         
B02A: 00              BRK                         
B02B: D8              CLD                         
B02C: 00              BRK                         
B02D: 00              BRK                         
B02E: 00              BRK                         
B02F: 00              BRK                         
B030: 00              BRK                         
B031: 93 ; ????
B032: 39 00 00        AND     $0000,Y             ; {ram.GP_00}
B035: EA              NOP                         
B036: 00              BRK                         
B037: 95 00           STA     $00,X               ; {ram.GP_00}
B039: 00              BRK                         
B03A: 00              BRK                         
B03B: 00              BRK                         
B03C: 00              BRK                         
B03D: 00              BRK                         
B03E: 00              BRK                         
B03F: 00              BRK                         
B040: 00              BRK                         
B041: 55 00           EOR     $00,X               ; {ram.GP_00}
B043: 00              BRK                         
B044: 00              BRK                         
B045: 00              BRK                         
B046: 00              BRK                         
B047: 00              BRK                         
B048: 00              BRK                         
B049: 00              BRK                         
B04A: 00              BRK                         
B04B: 00              BRK                         
B04C: 00              BRK                         
B04D: 00              BRK                         
B04E: 00              BRK                         
B04F: 00              BRK                         
B050: 00              BRK                         
B051: 5C ; ????
B052: 00              BRK                         
B053: 7E 00 00        ROR     $0000,X             ; {ram.GP_00}
B056: 00              BRK                         
B057: 00              BRK                         
B058: 00              BRK                         
B059: 1F ; ????
B05A: 3F ; ????
B05B: 5F ; ????
B05C: 0F ; ????
B05D: 30 0C           BMI     $B06B               ; {}
B05F: 0F ; ????
B060: 0F ; ????
B061: 2B ; ????
B062: 14 ; ????
B063: 13 ; ????
B064: 0F ; ????
B065: 27 ; ????
B066: 00              BRK                         
B067: 09 0F           ORA     #$0F                
B069: 35 27           AND     $27,X               
B06B: 15 0F           ORA     $0F,X               
B06D: 30 26           BMI     $B095               ; {}
B06F: 07 ; ????
B070: 0F ; ????
B071: 31 02           AND     ($02),Y             
B073: 15 0F           ORA     $0F,X               
B075: 12 ; ????
B076: 23 ; ????
B077: 31 0F           AND     ($0F),Y             
B079: 06 28           ASL     $28                 
B07B: 35 0F           AND     $0F,X               
B07D: 30 0C           BMI     $B08B               ; {}
B07F: 0F ; ????
B080: 0F ; ????
B081: 25 22           AND     $22                 
B083: 02 ; ????
B084: 0F ; ????
B085: 27 ; ????
B086: 00              BRK                         
B087: 16 0F           ASL     $0F,X               
B089: 35 27           AND     $27,X               
B08B: 15 0F           ORA     $0F,X               
B08D: 20 26 07        JSR     $0726               
B090: 0F ; ????
B091: 31 02           AND     ($02),Y             
B093: 15 0F           ORA     $0F,X               
B095: 12 ; ????
B096: 23 ; ????
B097: 31 0F           AND     ($0F),Y             
B099: 06 28           ASL     $28                 
B09B: 35 0F           AND     $0F,X               
B09D: 30 0C           BMI     $B0AB               ; {}
B09F: 0F ; ????
B0A0: 0F ; ????
B0A1: 20 1A 08        JSR     $081A               
B0A4: 0F ; ????
B0A5: 27 ; ????
B0A6: 0B ; ????
B0A7: 01 0F           ORA     ($0F,X)             
B0A9: 26 2B           ROL     $2B                 
B0AB: 15 0F           ORA     $0F,X               
B0AD: 20 26 07        JSR     $0726               
B0B0: 0F ; ????
B0B1: 31 02           AND     ($02),Y             
B0B3: 15 0F           ORA     $0F,X               
B0B5: 12 ; ????
B0B6: 23 ; ????
B0B7: 31 0F           AND     ($0F),Y             
B0B9: 06 28           ASL     $28                 
B0BB: 35 04           AND     $04,X               
B0BD: 02 ; ????
B0BE: 01 15           ORA     ($15,X)             
B0C0: 00              BRK                         
B0C1: 02 ; ????
B0C2: 07 ; ????
B0C3: AF ; ????
B0C4: 01 02           ORA     ($02,X)             
B0C6: 09 B8           ORA     #$B8                
B0C8: 01 01           ORA     ($01,X)             
B0CA: 01 01           ORA     ($01,X)             
B0CC: 01 01           ORA     ($01,X)             
B0CE: 02 ; ????
B0CF: 02 ; ????
B0D0: 06 03           ASL     $03                 
B0D2: 04 ; ????
B0D3: 04 ; ????
B0D4: 0A              ASL     A                   
B0D5: 0A              ASL     A                   
B0D6: 0A              ASL     A                   
B0D7: 01 00           ORA     ($00,X)             ; {ram.GP_00}
B0D9: 01 01           ORA     ($01,X)             
B0DB: 01 03           ORA     ($03,X)             
B0DD: 05 02           ORA     $02                 
B0DF: 02 ; ????
B0E0: 00              BRK                         
B0E1: 03 ; ????
B0E2: 04 ; ????
B0E3: 05 05           ORA     $05                 
B0E5: 05 05           ORA     $05                 
B0E7: 01 00           ORA     ($00,X)             ; {ram.GP_00}
B0E9: 01 02           ORA     ($02,X)             
B0EB: 01 02           ORA     ($02,X)             
B0ED: 02 ; ????
B0EE: 02 ; ????
B0EF: 02 ; ????
B0F0: 00              BRK                         
B0F1: 02 ; ????
B0F2: 04 ; ????
B0F3: 03 ; ????
B0F4: 03 ; ????
B0F5: 03 ; ????
B0F6: 02 ; ????
B0F7: 01 00           ORA     ($00,X)             ; {ram.GP_00}
B0F9: 4C 00 A8        JMP     $A800               ; {}
B0FC: 4C 01 A8        JMP     $A801               ; {}
B0FF: A9 00           LDA     #$00                
B101: 8D 30 01        STA     $0130               
B104: A9 00           LDA     #$00                
B106: 8D 2F 01        STA     $012F               
B109: 60              RTS                         
B10A: 00              BRK                         
B10B: 05 F0           ORA     $F0                 
B10D: 05 00           ORA     $00                 ; {ram.GP_00}
B10F: 05 F0           ORA     $F0                 
B111: 05 00           ORA     $00                 ; {ram.GP_00}
B113: 04 ; ????
B114: 40              RTI                         
B115: 04 ; ????
B116: 00              BRK                         
B117: 04 ; ????
B118: 40              RTI                         
B119: 04 ; ????
B11A: 27 ; ????
B11B: 70 27           BVS     $B144               ; {}
B11D: 70 27           BVS     $B146               ; {}
B11F: 70 E5           BVS     $B106               ; {}
B121: 9B ; ????
B122: 06 9C           ASL     $9C                 
B124: 42 ; ????
B125: 9C ; ????
B126: 6F ; ????
B127: 9C ; ????
B128: A5 9C           LDA     $9C                 
B12A: A5 9C           LDA     $9C                 
B12C: A5 9C           LDA     $9C                 
B12E: FC ; ????
B12F: 9C ; ????
B130: 4A              LSR     A                   
B131: 9D 4A 9D        STA     $9D4A,X             ; {}
B134: 89 ; ????
B135: 9D D7 9D        STA     $9DD7,X             ; {}
B138: 19 9E 19        ORA     $199E,Y             
B13B: 9E ; ????
B13C: 55 9E           EOR     $9E,X               
B13E: 97 ; ????
B13F: 9E ; ????
B140: E5 9B           SBC     $9B                 
B142: 97 ; ????
B143: 9E ; ????
B144: 30 9F           BMI     $B0E5               ; {}
B146: 60              RTS                         
B147: 9F ; ????
B148: 99 9F E1        STA     $E19F,Y             
B14B: 9F ; ????
B14C: 17 ; ????
B14D: A0 17           LDY     #$17                
B14F: A0 17           LDY     #$17                
B151: A0 4D           LDY     #$4D                
B153: A0 4D           LDY     #$4D                
B155: A0 8C           LDY     #$8C                
B157: A0 DD           LDY     #$DD                
B159: A0 DD           LDY     #$DD                
B15B: A0 13           LDY     #$13                
B15D: A1 13           LDA     ($13,X)             
B15F: A1 55           LDA     ($55,X)             
B161: A1 A6           LDA     ($A6,X)             
B163: A1 A6           LDA     ($A6,X)             
B165: A1 A6           LDA     ($A6,X)             
B167: A1 A6           LDA     ($A6,X)             
B169: A1 A6           LDA     ($A6,X)             
B16B: A1 E8           LDA     ($E8,X)             
B16D: A1 E8           LDA     ($E8,X)             
B16F: A1 24           LDA     ($24,X)             
B171: A2 DC           LDX     #$DC                
B173: 9E ; ????
B174: 5D A2 62        EOR     $62A2,X             
B177: A2 6B           LDX     #$6B                
B179: A2 74           LDX     #$74                
B17B: A2 79           LDX     #$79                
B17D: A2 84           LDX     #$84                
B17F: A2 8A           LDX     #$8A                
B181: A2 90           LDX     #$90                
B183: A2 94           LDX     #$94                
B185: A2 9A           LDX     #$9A                
B187: A2 A3           LDX     #$A3                
B189: A2 B8           LDX     #$B8                
B18B: A2 C1           LDX     #$C1                
B18D: A2 C4           LDX     #$C4                
B18F: A2 CB           LDX     #$CB                
B191: A2 CF           LDX     #$CF                
B193: A2 D5           LDX     #$D5                
B195: A2 D8           LDX     #$D8                
B197: A2 DD           LDX     #$DD                
B199: A2 E3           LDX     #$E3                
B19B: A2 E7           LDX     #$E7                
B19D: A2 F0           LDX     #$F0                
B19F: A2 F6           LDX     #$F6                
B1A1: A2 F9           LDX     #$F9                
B1A3: A2 02           LDX     #$02                
B1A5: A3 ; ????
B1A6: 08              PHP                         
B1A7: A3 ; ????
B1A8: 00              BRK                         
B1A9: 00              BRK                         
B1AA: 00              BRK                         
B1AB: 00              BRK                         
B1AC: 00              BRK                         
B1AD: 00              BRK                         
B1AE: 00              BRK                         
B1AF: 00              BRK                         
B1B0: 16 04           ASL     $04,X               
B1B2: 00              BRK                         
B1B3: 00              BRK                         
B1B4: 00              BRK                         
B1B5: 00              BRK                         
B1B6: 00              BRK                         
B1B7: 00              BRK                         
B1B8: 00              BRK                         
B1B9: 00              BRK                         
B1BA: 00              BRK                         
B1BB: 00              BRK                         
B1BC: 07 ; ????
B1BD: 06 03           ASL     $03                 
B1BF: 0A              ASL     A                   
B1C0: 03 ; ????
B1C1: 0B ; ????
B1C2: 0C ; ????
B1C3: 0C ; ????
B1C4: 00              BRK                         
B1C5: 00              BRK                         
B1C6: 00              BRK                         
B1C7: 00              BRK                         
B1C8: 00              BRK                         
B1C9: 00              BRK                         
B1CA: 00              BRK                         
B1CB: 00              BRK                         
B1CC: 04 ; ????
B1CD: 05 00           ORA     $00                 ; {ram.GP_00}
B1CF: 00              BRK                         
B1D0: 00              BRK                         
B1D1: 00              BRK                         
B1D2: 04 ; ????
B1D3: 05 15           ORA     $15                 
B1D5: 04 ; ????
B1D6: 00              BRK                         
B1D7: 00              BRK                         
B1D8: 00              BRK                         
B1D9: 00              BRK                         
B1DA: 02 ; ????
B1DB: 06 08           ASL     $08                 
B1DD: 0D 01 02        ORA     $0201               
B1E0: 02 ; ????
B1E1: 0A              ASL     A                   
B1E2: 03 ; ????
B1E3: 0F ; ????
B1E4: 0C ; ????
B1E5: 0F ; ????
B1E6: 16 08           ASL     $08,X               
B1E8: 00              BRK                         
B1E9: 00              BRK                         
B1EA: 03 ; ????
B1EB: 05 03           ORA     $03                 
B1ED: 03 ; ????
B1EE: 03 ; ????
B1EF: 0A              ASL     A                   
B1F0: 0A              ASL     A                   
B1F1: 0E 03 09        ASL     $0903               
B1F4: 03 ; ????
B1F5: 05 00           ORA     $00                 ; {ram.GP_00}
B1F7: 00              BRK                         
B1F8: 28              PLP                         
B1F9: 02 ; ????
B1FA: 12 ; ????
B1FB: 0B ; ????
B1FC: 13 ; ????
B1FD: 0A              ASL     A                   
B1FE: 02 ; ????
B1FF: 0A              ASL     A                   
B200: 14 ; ????
B201: 0B ; ????
B202: 13 ; ????
B203: 0A              ASL     A                   
B204: 0E 0D 00        ASL     $000D               
B207: 00              BRK                         
B208: 00              BRK                         
B209: 00              BRK                         
B20A: 00              BRK                         
B20B: 00              BRK                         
B20C: 00              BRK                         
B20D: 00              BRK                         
B20E: 00              BRK                         
B20F: 00              BRK                         
B210: 00              BRK                         
B211: 00              BRK                         
B212: 00              BRK                         
B213: 00              BRK                         
B214: 0F ; ????
B215: 03 ; ????
B216: 29 00           AND     #$00                
B218: 00              BRK                         
B219: 00              BRK                         
B21A: 00              BRK                         
B21B: 00              BRK                         
B21C: 00              BRK                         
B21D: 00              BRK                         
B21E: 00              BRK                         
B21F: 00              BRK                         
B220: 00              BRK                         
B221: 00              BRK                         
B222: 00              BRK                         
B223: 00              BRK                         
B224: 00              BRK                         
B225: 00              BRK                         
B226: 00              BRK                         
B227: 00              BRK                         
B228: 00              BRK                         
B229: 00              BRK                         
B22A: 00              BRK                         
B22B: 00              BRK                         
B22C: 00              BRK                         
B22D: 00              BRK                         
B22E: 00              BRK                         
B22F: 00              BRK                         
B230: 00              BRK                         
B231: 00              BRK                         
B232: 51 61           EOR     ($61),Y             
B234: 60              RTS                         
B235: 36 00           ROL     $00,X               ; {ram.GP_00}
B237: 00              BRK                         
B238: 00              BRK                         
B239: 00              BRK                         
B23A: 00              BRK                         
B23B: 00              BRK                         
B23C: 00              BRK                         
B23D: 38              SEC                         
B23E: 00              BRK                         
B23F: 00              BRK                         
B240: 00              BRK                         
B241: 34 ; ????
B242: 52 ; ????
B243: 00              BRK                         
B244: 10 37           BPL     $B27D               ; {}
B246: 46 00           LSR     $00                 ; {ram.GP_00}
B248: 00              BRK                         
B249: 37 ; ????
B24A: 00              BRK                         
B24B: 37 ; ????
B24C: 35 37           AND     $37,X               
B24E: 47 ; ????
B24F: 00              BRK                         
B250: 00              BRK                         
B251: 32 ; ????
B252: 50 20           BVC     $B274               ; {}
B254: 62 ; ????
B255: 50 41           BVC     $B298               ; {}
B257: 00              BRK                         
B258: 00              BRK                         
B259: 00              BRK                         
B25A: 00              BRK                         
B25B: 00              BRK                         
B25C: 00              BRK                         
B25D: 00              BRK                         
B25E: 40              RTI                         
B25F: F0 00           BEQ     $B261               ; {}
B261: 00              BRK                         
B262: 00              BRK                         
B263: 00              BRK                         
B264: 00              BRK                         
B265: 00              BRK                         
B266: 00              BRK                         
B267: 00              BRK                         
B268: 44 ; ????
B269: 74 ; ????
B26A: A8              TAY                         
B26B: 7C ; ????
B26C: 44 ; ????
B26D: 6D A2 AA        ADC     $AAA2               ; {}
B270: 74 ; ????
B271: 56 5A           LSR     $5A,X               
B273: 7B ; ????
B274: 73 ; ????
B275: 77 ; ????
B276: 7D AA 44        ADC     $44AA,X             
B279: 72 ; ????
B27A: 19 AD A2        ORA     $A2AD,Y             ; {}
B27D: 54 ; ????
B27E: 49 AC           EOR     #$AC                
B280: 48              PHA                         
B281: 77 ; ????
B282: 73 ; ????
B283: 7A ; ????
B284: 56 5A           LSR     $5A,X               
B286: A5 AD           LDA     $AD                 
B288: 4C 64 8C        JMP     $8C64               ; {}
B28B: A4 43           LDY     $43                 
B28D: 01 4C           ORA     ($4C,X)             
B28F: 01 76           ORA     ($76,X)             
B291: 00              BRK                         
B292: 8D 00 75        STA     $7500               
B295: 02 ; ????
B296: 75 00           ADC     $00,X               ; {ram.GP_00}
B298: 75 03           ADC     $03,X               
B29A: 8A              TXA                         
B29B: 00              BRK                         
B29C: 43 ; ????
B29D: 01 43           ORA     ($43,X)             
B29F: 03 ; ????
B2A0: AB ; ????
B2A1: 00              BRK                         
B2A2: AB ; ????
B2A3: 02 ; ????
B2A4: 54 ; ????
B2A5: 00              BRK                         
B2A6: 54 ; ????
B2A7: 02 ; ????
B2A8: 4A              LSR     A                   
B2A9: 00              BRK                         
B2AA: 4A              LSR     A                   
B2AB: 03 ; ????
B2AC: 44 ; ????
B2AD: A6 A4           LDX     $A4                 
B2AF: A8              TAY                         
B2B0: 36 87           ROL     $87,X               
B2B2: 36 87           ROL     $87,X               
B2B4: 1D AD 0A        ORA     $0AAD,X             
B2B7: 23 ; ????
B2B8: 0B ; ????
B2B9: 45 0B           EOR     $0B                 
B2BB: 4A              LSR     A                   
B2BC: 0C ; ????
B2BD: 45 0C           EOR     $0C                 
B2BF: 4A              LSR     A                   
B2C0: 0D 27 0D        ORA     $0D27               
B2C3: 7E 15 A1        ROR     $A115,X             ; {}
B2C6: 19 71 1A        ORA     $1A71,Y             
B2C9: AE 1A A1        LDX     $A11A               ; {}
B2CC: 1D A4 1D        ORA     $1DA4,X             
B2CF: AE 1E 75        LDX     $751E               
B2D2: 21 7E           AND     ($7E,X)             
B2D4: 22 ; ????
B2D5: 71 22           ADC     ($22),Y             
B2D7: AE 23 37        LDX     $3723               
B2DA: 24 A5           BIT     $A5                 
B2DC: 24 89           BIT     $89                 
B2DE: 26 71           ROL     $71                 
B2E0: 26 AE           ROL     $AE                 
B2E2: 2C 8A 2D        BIT     $2D8A               
B2E5: A9 2E           LDA     #$2E                
B2E7: 7E 2E AC        ROR     $AC2E,X             ; {}
B2EA: 36 A3           ROL     $A3,X               
B2EC: 36 AE           ROL     $AE,X               
B2EE: FF ; ????
B2EF: 36 A3           ROL     $A3,X               
B2F1: 36 AE           ROL     $AE,X               
B2F3: 36 AE           ROL     $AE,X               
B2F5: 36 AE           ROL     $AE,X               
B2F7: 1F ; ????
B2F8: 3F ; ????
B2F9: 5F ; ????
B2FA: 0F ; ????
B2FB: 30 00           BMI     $B2FD               ; {}
B2FD: 06 0F           ASL     $0F                 
B2FF: 19 28 07        ORA     $0728,Y             
B302: 0F ; ????
B303: 38              SEC                         
B304: 1B ; ????
B305: 0C ; ????
B306: 0F ; ????
B307: 27 ; ????
B308: 00              BRK                         
B309: 15 0F           ORA     $0F,X               
B30B: 20 26 07        JSR     $0726               
B30E: 0F ; ????
B30F: 31 02           AND     ($02),Y             
B311: 15 0F           ORA     $0F,X               
B313: 12 ; ????
B314: 23 ; ????
B315: 31 0F           AND     ($0F),Y             
B317: 06 16           ASL     $16                 
B319: 38              SEC                         
B31A: 01 01           ORA     ($01,X)             
B31C: 01 01           ORA     ($01,X)             
B31E: 01 01           ORA     ($01,X)             
B320: 01 02           ORA     ($02,X)             
B322: 06 01           ASL     $01                 
B324: 02 ; ????
B325: 01 01           ORA     ($01,X)             
B327: 0A              ASL     A                   
B328: 01 01           ORA     ($01,X)             
B32A: 01 01           ORA     ($01,X)             
B32C: 01 01           ORA     ($01,X)             
B32E: 01 01           ORA     ($01,X)             
B330: 01 01           ORA     ($01,X)             
B332: 01 03           ORA     ($03,X)             
B334: 03 ; ????
B335: 05 01           ORA     $01                 
B337: 01 05           ORA     ($05,X)             
B339: 01 01           ORA     ($01,X)             
B33B: 01 01           ORA     ($01,X)             
B33D: 02 ; ????
B33E: 01 01           ORA     ($01,X)             
B340: 01 01           ORA     ($01,X)             
B342: 01 01           ORA     ($01,X)             
B344: 02 ; ????
B345: 01 02           ORA     ($02,X)             
B347: 01 01           ORA     ($01,X)             
B349: 02 ; ????
B34A: 01 01           ORA     ($01,X)             
B34C: 01 F8           ORA     ($F8,X)             
B34E: E0 02           CPX     #$02                
B350: FC ; ????
B351: F8              SED                         
B352: E1 02           SBC     ($02,X)             
B354: 04 ; ????
B355: 00              BRK                         
B356: E4 02           CPX     $02                 
B358: FC ; ????
B359: 00              BRK                         
B35A: E5 02           SBC     $02                 
B35C: 04 ; ????
B35D: F8              SED                         
B35E: E1 42           SBC     ($42,X)             
B360: FC ; ????
B361: F8              SED                         
B362: E0 42           CPX     #$42                
B364: 04 ; ????
B365: 00              BRK                         
B366: E5 42           SBC     $42                 
B368: FC ; ????
B369: 00              BRK                         
B36A: E4 42           CPX     $42                 
B36C: 04 ; ????
B36D: F9 E0 02        SBC     $02E0,Y             
B370: FC ; ????
B371: F9 E3 02        SBC     $02E3,Y             
B374: 04 ; ????
B375: 00              BRK                         
B376: E6 02           INC     $02                 
B378: FC ; ????
B379: 00              BRK                         
B37A: E7 ; ????
B37B: 02 ; ????
B37C: 04 ; ????
B37D: F9 E3 42        SBC     $42E3,Y             
B380: FC ; ????
B381: F9 E0 42        SBC     $42E0,Y             
B384: 04 ; ????
B385: 00              BRK                         
B386: E7 ; ????
B387: 42 ; ????
B388: FC ; ????
B389: 00              BRK                         
B38A: E6 42           INC     $42                 
B38C: 04 ; ????
B38D: F8              SED                         
B38E: DC ; ????
B38F: 02 ; ????
B390: FC ; ????
B391: F8              SED                         
B392: DC ; ????
B393: 42 ; ????
B394: 04 ; ????
B395: 00              BRK                         
B396: DD 02 FC        CMP     $FC02,X             
B399: 00              BRK                         
B39A: DD 42 04        CMP     $0442,X             
B39D: F8              SED                         
B39E: DC ; ????
B39F: 03 ; ????
B3A0: FC ; ????
B3A1: F8              SED                         
B3A2: DC ; ????
B3A3: 43 ; ????
B3A4: 04 ; ????
B3A5: 00              BRK                         
B3A6: DD 03 FC        CMP     $FC03,X             
B3A9: 00              BRK                         
B3AA: DD 43 04        CMP     $0443,X             
B3AD: F8              SED                         
B3AE: E0 03           CPX     #$03                
B3B0: FC ; ????
B3B1: F8              SED                         
B3B2: E1 03           SBC     ($03,X)             
B3B4: 04 ; ????
B3B5: 00              BRK                         
B3B6: E4 03           CPX     $03                 
B3B8: FC ; ????
B3B9: 00              BRK                         
B3BA: E5 03           SBC     $03                 
B3BC: 04 ; ????
B3BD: F8              SED                         
B3BE: E1 43           SBC     ($43,X)             
B3C0: FC ; ????
B3C1: F8              SED                         
B3C2: E0 43           CPX     #$43                
B3C4: 04 ; ????
B3C5: 00              BRK                         
B3C6: E5 43           SBC     $43                 
B3C8: FC ; ????
B3C9: 00              BRK                         
B3CA: E4 43           CPX     $43                 
B3CC: 04 ; ????
B3CD: F9 E0 03        SBC     $03E0,Y             
B3D0: FC ; ????
B3D1: F9 E3 03        SBC     $03E3,Y             
B3D4: 04 ; ????
B3D5: 00              BRK                         
B3D6: E6 03           INC     $03                 
B3D8: FC ; ????
B3D9: 00              BRK                         
B3DA: E7 ; ????
B3DB: 03 ; ????
B3DC: 04 ; ????
B3DD: F9 E3 43        SBC     $43E3,Y             
B3E0: FC ; ????
B3E1: F9 E0 43        SBC     $43E0,Y             
B3E4: 04 ; ????
B3E5: 00              BRK                         
B3E6: E7 ; ????
B3E7: 43 ; ????
B3E8: FC ; ????
B3E9: 00              BRK                         
B3EA: E6 43           INC     $43                 
B3EC: 04 ; ????
B3ED: 4C 00 B0        JMP     $B000               ; {}
B3F0: 4C 01 B0        JMP     $B001               ; {}
B3F3: A9 00           LDA     #$00                
B3F5: 8D 30 01        STA     $0130               
B3F8: A9 01           LDA     #$01                
B3FA: 8D 2F 01        STA     $012F               
B3FD: 60              RTS                         
B3FE: 00              BRK                         
B3FF: 05 F0           ORA     $F0                 
B401: 05 00           ORA     $00                 ; {ram.GP_00}
B403: 05 F0           ORA     $F0                 
B405: 05 00           ORA     $00                 ; {ram.GP_00}
B407: 04 ; ????
B408: 40              RTI                         
B409: 04 ; ????
B40A: 00              BRK                         
B40B: 04 ; ????
B40C: 40              RTI                         
B40D: 04 ; ????
B40E: 27 ; ????
B40F: 70 27           BVS     $B438               ; {}
B411: 70 27           BVS     $B43A               ; {}
B413: 70 E5           BVS     $B3FA               ; {}
B415: 9B ; ????
B416: 06 9C           ASL     $9C                 
B418: 42 ; ????
B419: 9C ; ????
B41A: 6F ; ????
B41B: 9C ; ????
B41C: A5 9C           LDA     $9C                 
B41E: A5 9C           LDA     $9C                 
B420: A5 9C           LDA     $9C                 
B422: FC ; ????
B423: 9C ; ????
B424: 4A              LSR     A                   
B425: 9D 4A 9D        STA     $9D4A,X             ; {}
B428: 89 ; ????
B429: 9D D7 9D        STA     $9DD7,X             ; {}
B42C: 19 9E 19        ORA     $199E,Y             
B42F: 9E ; ????
B430: 55 9E           EOR     $9E,X               
B432: 97 ; ????
B433: 9E ; ????
B434: E5 9B           SBC     $9B                 
B436: 97 ; ????
B437: 9E ; ????
B438: 30 9F           BMI     $B3D9               ; {}
B43A: 60              RTS                         
B43B: 9F ; ????
B43C: 99 9F E1        STA     $E19F,Y             
B43F: 9F ; ????
B440: 17 ; ????
B441: A0 17           LDY     #$17                
B443: A0 17           LDY     #$17                
B445: A0 4D           LDY     #$4D                
B447: A0 4D           LDY     #$4D                
B449: A0 8C           LDY     #$8C                
B44B: A0 DD           LDY     #$DD                
B44D: A0 DD           LDY     #$DD                
B44F: A0 13           LDY     #$13                
B451: A1 13           LDA     ($13,X)             
B453: A1 55           LDA     ($55,X)             
B455: A1 A6           LDA     ($A6,X)             
B457: A1 A6           LDA     ($A6,X)             
B459: A1 A6           LDA     ($A6,X)             
B45B: A1 A6           LDA     ($A6,X)             
B45D: A1 A6           LDA     ($A6,X)             
B45F: A1 E8           LDA     ($E8,X)             
B461: A1 E8           LDA     ($E8,X)             
B463: A1 24           LDA     ($24,X)             
B465: A2 DC           LDX     #$DC                
B467: 9E ; ????
B468: 5D A2 62        EOR     $62A2,X             
B46B: A2 6B           LDX     #$6B                
B46D: A2 74           LDX     #$74                
B46F: A2 79           LDX     #$79                
B471: A2 84           LDX     #$84                
B473: A2 8A           LDX     #$8A                
B475: A2 90           LDX     #$90                
B477: A2 94           LDX     #$94                
B479: A2 9A           LDX     #$9A                
B47B: A2 A3           LDX     #$A3                
B47D: A2 B8           LDX     #$B8                
B47F: A2 C1           LDX     #$C1                
B481: A2 C4           LDX     #$C4                
B483: A2 CB           LDX     #$CB                
B485: A2 CF           LDX     #$CF                
B487: A2 D5           LDX     #$D5                
B489: A2 D8           LDX     #$D8                
B48B: A2 DD           LDX     #$DD                
B48D: A2 E3           LDX     #$E3                
B48F: A2 E7           LDX     #$E7                
B491: A2 F0           LDX     #$F0                
B493: A2 F6           LDX     #$F6                
B495: A2 F9           LDX     #$F9                
B497: A2 02           LDX     #$02                
B499: A3 ; ????
B49A: 08              PHP                         
B49B: A3 ; ????
B49C: 0A              ASL     A                   
B49D: 06 28           ASL     $28                 
B49F: 0A              ASL     A                   
B4A0: 20 0E 16        JSR     $160E               
B4A3: 0E 0C 0A        ASL     $0A0C               
B4A6: 14 ; ????
B4A7: 0A              ASL     A                   
B4A8: 19 0C 00        ORA     $000C,Y             
B4AB: 00              BRK                         
B4AC: 19 05 00        ORA     $0005,Y             
B4AF: 00              BRK                         
B4B0: 02 ; ????
B4B1: 05 04           ORA     $04                 
B4B3: 07 ; ????
B4B4: 14 ; ????
B4B5: 0A              ASL     A                   
B4B6: 20 0C 1C        JSR     $1C0C               
B4B9: 05 00           ORA     $00                 ; {ram.GP_00}
B4BB: 00              BRK                         
B4BC: 1C ; ????
B4BD: 05 16           ORA     $16                 
B4BF: 06 1B           ASL     $1B                 
B4C1: 0F ; ????
B4C2: 19 0B 19        ORA     $190B,Y             
B4C5: 0C ; ????
B4C6: 13 ; ????
B4C7: 05 13           ORA     $13                 
B4C9: 07 ; ????
B4CA: 15 0C           ORA     $0C,X               
B4CC: 1C ; ????
B4CD: 05 13           ORA     $13                 
B4CF: 05 04           ORA     $04                 
B4D1: 05 01           ORA     $01                 
B4D3: 04 ; ????
B4D4: 14 ; ????
B4D5: 03 ; ????
B4D6: 03 ; ????
B4D7: 0B ; ????
B4D8: 0E 0F 19        ASL     $190F               
B4DB: 0D 03 03        ORA     $0303               
B4DE: 0E 0F 14        ASL     $140F               
B4E1: 0B ; ????
B4E2: 02 ; ????
B4E3: 0F ; ????
B4E4: 02 ; ????
B4E5: 0A              ASL     A                   
B4E6: 16 0A           ASL     $0A,X               
B4E8: 20 0B 21        JSR     $210B               
B4EB: 0D 00 00        ORA     $0000               ; {ram.GP_00}
B4EE: 1C ; ????
B4EF: 05 00           ORA     $00                 ; {ram.GP_00}
B4F1: 00              BRK                         
B4F2: 0C ; ????
B4F3: 05 00           ORA     $00                 ; {ram.GP_00}
B4F5: 00              BRK                         
B4F6: 0F ; ????
B4F7: 06 0B           ASL     $0B                 
B4F9: 00              BRK                         
B4FA: 1C ; ????
B4FB: 05 15           ORA     $15                 
B4FD: 02 ; ????
B4FE: 20 0B 0C        JSR     $0C0B               
B501: 0A              ASL     A                   
B502: 12 ; ????
B503: 0B ; ????
B504: 1E 0A 14        ASL     $140A,X             
B507: 0B ; ????
B508: 16 0A           ASL     $0A,X               
B50A: 19 09 00        ORA     $0009,Y             
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
B51C: 60              RTS                         
B51D: 00              BRK                         
B51E: 53 ; ????
B51F: 53 ; ????
B520: 00              BRK                         
B521: 61 41           ADC     ($41,X)             
B523: 00              BRK                         
B524: 20 00 38        JSR     $3800               
B527: 10 20           BPL     $B549               ; {}
B529: 53 ; ????
B52A: 52 ; ????
B52B: 00              BRK                         
B52C: 52 ; ????
B52D: 00              BRK                         
B52E: 46 00           LSR     $00                 ; {ram.GP_00}
B530: 20 51 51        JSR     $5151               
B533: 32 ; ????
B534: 52 ; ????
B535: 51 62           EOR     ($62),Y             
B537: 00              BRK                         
B538: 20 00 43        JSR     $4300               
B53B: 10 62           BPL     $B59F               ; {}
B53D: 42 ; ????
B53E: 20 10 10        JSR     $1010               
B541: 47 ; ????
B542: 53 ; ????
B543: 00              BRK                         
B544: 00              BRK                         
B545: 52 ; ????
B546: 00              BRK                         
B547: 00              BRK                         
B548: 00              BRK                         
B549: 44 ; ????
B54A: F0 52           BEQ     $B59E               ; {}
B54C: 00              BRK                         
B54D: 53 ; ????
B54E: 00              BRK                         
B54F: 30 63           BMI     $B5B4               ; {}
B551: 62 ; ????
B552: 00              BRK                         
B553: 41 00           EOR     ($00,X)             ; {ram.GP_00}
B555: 00              BRK                         
B556: 00              BRK                         
B557: 00              BRK                         
B558: 00              BRK                         
B559: 00              BRK                         
B55A: 00              BRK                         
B55B: 00              BRK                         
B55C: 74 ; ????
B55D: 77 ; ????
B55E: 7A ; ????
B55F: 7C ; ????
B560: 5A ; ????
B561: 43 ; ????
B562: 5B ; ????
B563: 77 ; ????
B564: 74 ; ????
B565: 76 A4           ROR     $A4,X               
B567: A2 42           LDX     #$42                
B569: 45 A3           EOR     $A3                 
B56B: AA              TAX                         
B56C: 7E 7C A4        ROR     $A47C,X             ; {}
B56F: AC 48 65        LDY     $6548               
B572: 83 ; ????
B573: AB ; ????
B574: 6C 75 78        JMP     ($7875)             
B577: A3 ; ????
B578: A3 ; ????
B579: A7 ; ????
B57A: AA              TAX                         
B57B: AD 15 16        LDA     $1615               
B57E: 19 1A 87        ORA     $871A,Y             ; {}
B581: 00              BRK                         
B582: 8B ; ????
B583: 00              BRK                         
B584: 8B ; ????
B585: 01 8B           ORA     ($8B,X)             
B587: 03 ; ????
B588: 43 ; ????
B589: 01 4C           ORA     ($4C,X)             
B58B: 01 76           ORA     ($76,X)             
B58D: 00              BRK                         
B58E: 8D 00 35        STA     $3500               
B591: 03 ; ????
B592: 65 03           ADC     $03                 
B594: 86 03           STX     $03                 
B596: 8A              TXA                         
B597: 02 ; ????
B598: 83 ; ????
B599: 01 86           ORA     ($86,X)             
B59B: 01 89           ORA     ($89,X)             
B59D: 01 8C           ORA     ($8C,X)             
B59F: 01 54           ORA     ($54,X)             
B5A1: 38              SEC                         
B5A2: A8              TAY                         
B5A3: 7A ; ????
B5A4: 87 ; ????
B5A5: 45 28           EOR     $28                 
B5A7: A8              TAY                         
B5A8: 2B ; ????
B5A9: 7C ; ????
B5AA: 00              BRK                         
B5AB: AB ; ????
B5AC: 00              BRK                         
B5AD: A1 06           LDA     ($06,X)             
B5AF: 44 ; ????
B5B0: 06 38           ASL     $38                 
B5B2: 06 59           ASL     $59                 
B5B4: 08              PHP                         
B5B5: 47 ; ????
B5B6: 08              PHP                         
B5B7: 48              PHA                         
B5B8: 0D 7E 13        ORA     $137E               
B5BB: A8              TAY                         
B5BC: 13 ; ????
B5BD: A5 15           LDA     $15                 
B5BF: 71 15           ADC     ($15),Y             
B5C1: 7E 16 71        ROR     $7116,X             
B5C4: 18              CLC                         
B5C5: 3A ; ????
B5C6: 19 71 19        ORA     $1971,Y             
B5C9: 7E 1D 69        ROR     $691D,X             
B5CC: 1E A1 1E        ASL     $1EA1,X             
B5CF: 7A ; ????
B5D0: 21 59           AND     ($59,X)             
B5D2: 21 69           AND     ($69,X)             
B5D4: 21 79           AND     ($79,X)             
B5D6: 27 ; ????
B5D7: 76 27           ROR     $27,X               
B5D9: 7E 29 3A        ROR     $3A29,X             
B5DC: 2B ; ????
B5DD: 71 2B           ADC     ($2B),Y             
B5DF: 7E 2D 44        ROR     $442D,X             
B5E2: 31 85           AND     ($85),Y             
B5E4: 31 8A           AND     ($8A),Y             
B5E6: 32 ; ????
B5E7: 77 ; ????
B5E8: 33 ; ????
B5E9: 55 FF           EOR     $FF,X               
B5EB: 1F ; ????
B5EC: 3F ; ????
B5ED: 5F ; ????
B5EE: 0F ; ????
B5EF: 30 16           BMI     $B607               ; {}
B5F1: 0F ; ????
B5F2: 0F ; ????
B5F3: 31 22           AND     ($22),Y             
B5F5: 02 ; ????
B5F6: 0F ; ????
B5F7: 30 1C           BMI     $B615               ; {}
B5F9: 02 ; ????
B5FA: 0F ; ????
B5FB: 27 ; ????
B5FC: 00              BRK                         
B5FD: 15 0F           ORA     $0F,X               
B5FF: 20 26 07        JSR     $0726               
B602: 0F ; ????
B603: 31 02           AND     ($02),Y             
B605: 15 0F           ORA     $0F,X               
B607: 12 ; ????
B608: 23 ; ????
B609: 31 0F           AND     ($0F),Y             
B60B: 06 16           ASL     $16                 
B60D: 38              SEC                         
B60E: 01 02           ORA     ($02,X)             
B610: 01 01           ORA     ($01,X)             
B612: 01 01           ORA     ($01,X)             
B614: 01 03           ORA     ($03,X)             
B616: 08              PHP                         
B617: 02 ; ????
B618: 03 ; ????
B619: 01 01           ORA     ($01,X)             
B61B: 0A              ASL     A                   
B61C: 01 01           ORA     ($01,X)             
B61E: 03 ; ????
B61F: 01 01           ORA     ($01,X)             
B621: 01 01           ORA     ($01,X)             
B623: 01 01           ORA     ($01,X)             
B625: 01 01           ORA     ($01,X)             
B627: 03 ; ????
B628: 03 ; ????
B629: 05 01           ORA     $01                 
B62B: 01 05           ORA     ($05,X)             
B62D: 01 01           ORA     ($01,X)             
B62F: 01 01           ORA     ($01,X)             
B631: 01 01           ORA     ($01,X)             
B633: 01 01           ORA     ($01,X)             
B635: 01 01           ORA     ($01,X)             
B637: 01 02           ORA     ($02,X)             
B639: 01 02           ORA     ($02,X)             
B63B: 01 01           ORA     ($01,X)             
B63D: 02 ; ????
B63E: 01 01           ORA     ($01,X)             
B640: 03 ; ????
B641: F8              SED                         
B642: F6 02           INC     $02,X               
B644: FC ; ????
B645: F8              SED                         
B646: F6 42           INC     $42,X               
B648: 04 ; ????
B649: 00              BRK                         
B64A: F8              SED                         
B64B: 02 ; ????
B64C: FC ; ????
B64D: 00              BRK                         
B64E: F9 02 04        SBC     $0402,Y             
B651: F8              SED                         
B652: F6 02           INC     $02,X               
B654: FC ; ????
B655: F8              SED                         
B656: F6 42           INC     $42,X               
B658: 04 ; ????
B659: 00              BRK                         
B65A: F9 42 FC        SBC     $FC42,Y             
B65D: 00              BRK                         
B65E: F8              SED                         
B65F: 42 ; ????
B660: 04 ; ????
B661: F8              SED                         
B662: F6 03           INC     $03,X               
B664: FC ; ????
B665: F8              SED                         
B666: F6 43           INC     $43,X               
B668: 04 ; ????
B669: 00              BRK                         
B66A: F8              SED                         
B66B: 03 ; ????
B66C: FC ; ????
B66D: 00              BRK                         
B66E: F9 03 04        SBC     $0403,Y             
B671: F8              SED                         
B672: F6 03           INC     $03,X               
B674: FC ; ????
B675: F8              SED                         
B676: F6 43           INC     $43,X               
B678: 04 ; ????
B679: 00              BRK                         
B67A: F9 43 FC        SBC     $FC43,Y             
B67D: 00              BRK                         
B67E: F8              SED                         
B67F: 43 ; ????
B680: 04 ; ????
B681: F8              SED                         
B682: FA ; ????
B683: 02 ; ????
B684: FC ; ????
B685: F8              SED                         
B686: FA ; ????
B687: 42 ; ????
B688: 04 ; ????
B689: 00              BRK                         
B68A: F7 ; ????
B68B: 02 ; ????
B68C: FC ; ????
B68D: 00              BRK                         
B68E: F7 ; ????
B68F: 42 ; ????
B690: 04 ; ????
B691: F8              SED                         
B692: C8              INY                         
B693: 02 ; ????
B694: FC ; ????
B695: F8              SED                         
B696: C8              INY                         
B697: 42 ; ????
B698: 04 ; ????
B699: 00              BRK                         
B69A: C9 02           CMP     #$02                
B69C: FC ; ????
B69D: 00              BRK                         
B69E: C9 42           CMP     #$42                
B6A0: 04 ; ????
B6A1: F8              SED                         
B6A2: FA ; ????
B6A3: 03 ; ????
B6A4: FC ; ????
B6A5: F8              SED                         
B6A6: FA ; ????
B6A7: 43 ; ????
B6A8: 04 ; ????
B6A9: 00              BRK                         
B6AA: F7 ; ????
B6AB: 03 ; ????
B6AC: FC ; ????
B6AD: 00              BRK                         
B6AE: F7 ; ????
B6AF: 43 ; ????
B6B0: 04 ; ????
B6B1: F8              SED                         
B6B2: C8              INY                         
B6B3: 03 ; ????
B6B4: FC ; ????
B6B5: F8              SED                         
B6B6: C8              INY                         
B6B7: 43 ; ????
B6B8: 04 ; ????
B6B9: 00              BRK                         
B6BA: C9 03           CMP     #$03                
B6BC: FC ; ????
B6BD: 00              BRK                         
B6BE: C9 43           CMP     #$43                
B6C0: 04 ; ????
B6C1: 4C 00 B8        JMP     $B800               ; {}
B6C4: 4C 01 B8        JMP     $B801               ; {}
B6C7: A9 00           LDA     #$00                
B6C9: 8D 30 01        STA     $0130               
B6CC: A9 02           LDA     #$02                
B6CE: 8D 2F 01        STA     $012F               
B6D1: 60              RTS                         
B6D2: 00              BRK                         
B6D3: 05 F0           ORA     $F0                 
B6D5: 05 00           ORA     $00                 ; {ram.GP_00}
B6D7: 05 F0           ORA     $F0                 
B6D9: 05 00           ORA     $00                 ; {ram.GP_00}
B6DB: 04 ; ????
B6DC: 40              RTI                         
B6DD: 04 ; ????
B6DE: 00              BRK                         
B6DF: 04 ; ????
B6E0: 40              RTI                         
B6E1: 04 ; ????
B6E2: 27 ; ????
B6E3: 70 27           BVS     $B70C               ; {}
B6E5: 70 27           BVS     $B70E               ; {}
B6E7: 70 E5           BVS     $B6CE               ; {}
B6E9: 9B ; ????
B6EA: 06 9C           ASL     $9C                 
B6EC: 42 ; ????
B6ED: 9C ; ????
B6EE: 6F ; ????
B6EF: 9C ; ????
B6F0: A5 9C           LDA     $9C                 
B6F2: A5 9C           LDA     $9C                 
B6F4: A5 9C           LDA     $9C                 
B6F6: FC ; ????
B6F7: 9C ; ????
B6F8: 4A              LSR     A                   
B6F9: 9D 4A 9D        STA     $9D4A,X             ; {}
B6FC: 89 ; ????
B6FD: 9D D7 9D        STA     $9DD7,X             ; {}
B700: 19 9E 19        ORA     $199E,Y             
B703: 9E ; ????
B704: 55 9E           EOR     $9E,X               
B706: 97 ; ????
B707: 9E ; ????
B708: E5 9B           SBC     $9B                 
B70A: 97 ; ????
B70B: 9E ; ????
B70C: 30 9F           BMI     $B6AD               ; {}
B70E: 60              RTS                         
B70F: 9F ; ????
B710: 99 9F E1        STA     $E19F,Y             
B713: 9F ; ????
B714: 17 ; ????
B715: A0 17           LDY     #$17                
B717: A0 17           LDY     #$17                
B719: A0 4D           LDY     #$4D                
B71B: A0 4D           LDY     #$4D                
B71D: A0 8C           LDY     #$8C                
B71F: A0 DD           LDY     #$DD                
B721: A0 DD           LDY     #$DD                
B723: A0 13           LDY     #$13                
B725: A1 13           LDA     ($13,X)             
B727: A1 55           LDA     ($55,X)             
B729: A1 A6           LDA     ($A6,X)             
B72B: A1 A6           LDA     ($A6,X)             
B72D: A1 A6           LDA     ($A6,X)             
B72F: A1 A6           LDA     ($A6,X)             
B731: A1 A6           LDA     ($A6,X)             
B733: A1 E8           LDA     ($E8,X)             
B735: A1 E8           LDA     ($E8,X)             
B737: A1 24           LDA     ($24,X)             
B739: A2 DC           LDX     #$DC                
B73B: 9E ; ????
B73C: 5D A2 62        EOR     $62A2,X             
B73F: A2 6B           LDX     #$6B                
B741: A2 74           LDX     #$74                
B743: A2 79           LDX     #$79                
B745: A2 84           LDX     #$84                
B747: A2 8A           LDX     #$8A                
B749: A2 90           LDX     #$90                
B74B: A2 94           LDX     #$94                
B74D: A2 9A           LDX     #$9A                
B74F: A2 A3           LDX     #$A3                
B751: A2 B8           LDX     #$B8                
B753: A2 C1           LDX     #$C1                
B755: A2 C4           LDX     #$C4                
B757: A2 CB           LDX     #$CB                
B759: A2 CF           LDX     #$CF                
B75B: A2 D5           LDX     #$D5                
B75D: A2 D8           LDX     #$D8                
B75F: A2 DD           LDX     #$DD                
B761: A2 E3           LDX     #$E3                
B763: A2 E7           LDX     #$E7                
B765: A2 F0           LDX     #$F0                
B767: A2 F6           LDX     #$F6                
B769: A2 F9           LDX     #$F9                
B76B: A2 02           LDX     #$02                
B76D: A3 ; ????
B76E: 08              PHP                         
B76F: A3 ; ????
B770: 0A              ASL     A                   
B771: 06 0C           ASL     $0C                 
B773: 0A              ASL     A                   
B774: 13 ; ????
B775: 0E 14 0A        ASL     $0A14               
B778: 20 0E 26        JSR     $260E               
B77B: 0E 16 0E        ASL     $0E16               
B77E: 29 00           AND     #$00                
B780: 1C ; ????
B781: 05 0F           ORA     $0F                 
B783: 06 02           ASL     $02                 
B785: 0D 15 02        ORA     $0215               
B788: 08              PHP                         
B789: 0F ; ????
B78A: 13 ; ????
B78B: 0B ; ????
B78C: 13 ; ????
B78D: 0B ; ????
B78E: 08              PHP                         
B78F: 0C ; ????
B790: 19 07 1B        ORA     $1B07,Y             
B793: 0F ; ????
B794: 03 ; ????
B795: 0F ; ????
B796: 12 ; ????
B797: 0A              ASL     A                   
B798: 21 0F           AND     ($0F,X)             
B79A: 13 ; ????
B79B: 08              PHP                         
B79C: 28              PLP                         
B79D: 02 ; ????
B79E: 13 ; ????
B79F: 0D 26 07        ORA     $0726               
B7A2: 08              PHP                         
B7A3: 0B ; ????
B7A4: 19 0D 01        ORA     $010D,Y             
B7A7: 06 04           ASL     $04                 
B7A9: 0F ; ????
B7AA: 0C ; ????
B7AB: 0A              ASL     A                   
B7AC: 0C ; ????
B7AD: 0A              ASL     A                   
B7AE: 13 ; ????
B7AF: 0D 0C 07        ORA     $070C               
B7B2: 13 ; ????
B7B3: 0C ; ????
B7B4: 1C ; ????
B7B5: 05 02           ORA     $02                 
B7B7: 05 03           ORA     $03                 
B7B9: 03 ; ????
B7BA: 1E 0A 1E        ASL     $1E0A,X             
B7BD: 0A              ASL     A                   
B7BE: 19 0D 1C        ORA     $1C0D,Y             
B7C1: 05 16           ORA     $16                 
B7C3: 05 1C           ORA     $1C                 
B7C5: 05 02           ORA     $02                 
B7C7: 05 03           ORA     $03                 
B7C9: 06 0C           ASL     $0C                 
B7CB: 0A              ASL     A                   
B7CC: 15 0C           ORA     $0C,X               
B7CE: 1C ; ????
B7CF: 05 13           ORA     $13                 
B7D1: 05 14           ORA     $14                 
B7D3: 03 ; ????
B7D4: 04 ; ????
B7D5: 0F ; ????
B7D6: 02 ; ????
B7D7: 0F ; ????
B7D8: 20 0B 20        JSR     $200B               
B7DB: 0A              ASL     A                   
B7DC: 21 0F           AND     ($0F,X)             
B7DE: 0E 09 28        ASL     $2809               
B7E1: 03 ; ????
B7E2: 20 0A 14        JSR     $140A               
B7E5: 09 14           ORA     #$14                
B7E7: 01 03           ORA     ($03,X)             
B7E9: 02 ; ????
B7EA: 02 ; ????
B7EB: 0A              ASL     A                   
B7EC: 0D 0B 16        ORA     $160B               
B7EF: 08              PHP                         
B7F0: 00              BRK                         
B7F1: 61 53           ADC     ($53,X)             
B7F3: 10 50           BPL     $B845               ; {}
B7F5: 41 20           EOR     ($20,X)             
B7F7: F0 51           BEQ     $B84A               ; {}
B7F9: 60              RTS                         
B7FA: 10 00           BPL     $B7FC               ; {}
B7FC: 52 ; ????
B7FD: 53 ; ????
B7FE: 53 ; ????
B7FF: 52 ; ????
B800: 20 00 42        JSR     $4200               
B803: 00              BRK                         
B804: 10 53           BPL     $B859               ; {}
B806: 00              BRK                         
B807: 53 ; ????
B808: 41 10           EOR     ($10,X)             
B80A: 20 00 00        JSR     $0000               ; {ram.GP_00}
B80D: 00              BRK                         
B80E: 00              BRK                         
B80F: 53 ; ????
B810: 00              BRK                         
B811: 53 ; ????
B812: 51 61           EOR     ($61),Y             
B814: 42 ; ????
B815: 40              RTI                         
B816: 30 10           BMI     $B828               ; {}
B818: 51 03           EOR     ($03),Y             
B81A: 51 10           EOR     ($10),Y             
B81C: 32 ; ????
B81D: 00              BRK                         
B81E: 32 ; ????
B81F: 51 53           EOR     ($53),Y             
B821: 00              BRK                         
B822: 00              BRK                         
B823: 20 50 50        JSR     $5050               
B826: 00              BRK                         
B827: 00              BRK                         
B828: 00              BRK                         
B829: 50 61           BVC     $B88C               ; {}
B82B: 00              BRK                         
B82C: 42 ; ????
B82D: 20 00 00        JSR     $0000               ; {ram.GP_00}
B830: 35 39           AND     $39,X               
B832: 5A ; ????
B833: A8              TAY                         
B834: 55 58           EOR     $58,X               
B836: 4E AD 56        LSR     $56AD               
B839: 59 14 1B        EOR     $1B14,Y             
B83C: 56 59           LSR     $59,X               
B83E: 14 ; ????
B83F: 1B ; ????
B840: 56 59           LSR     $59,X               
B842: 14 ; ????
B843: 1B ; ????
B844: 56 59           LSR     $59,X               
B846: 14 ; ????
B847: 1B ; ????
B848: 56 59           LSR     $59,X               
B84A: 14 ; ????
B84B: 1B ; ????
B84C: 56 59           LSR     $59,X               
B84E: 14 ; ????
B84F: 1B ; ????
B850: 56 59           LSR     $59,X               
B852: 14 ; ????
B853: 1B ; ????
B854: 83 ; ????
B855: 01 86           ORA     ($86,X)             
B857: 01 89           ORA     ($89,X)             
B859: 01 8C           ORA     ($8C,X)             
B85B: 01 35           ORA     ($35,X)             
B85D: 03 ; ????
B85E: 65 03           ADC     $03                 
B860: 86 03           STX     $03                 
B862: 8A              TXA                         
B863: 02 ; ????
B864: 43 ; ????
B865: 03 ; ????
B866: 43 ; ????
B867: 01 AB           ORA     ($AB,X)             
B869: 02 ; ????
B86A: AB ; ????
B86B: 00              BRK                         
B86C: 43 ; ????
B86D: 01 76           ORA     ($76,X)             
B86F: 00              BRK                         
B870: 4C 01 8D        JMP     $8D01               ; {}
B873: 00              BRK                         
B874: 74 ; ????
B875: A4 A8           LDY     $A8                 
B877: 77 ; ????
B878: A8              TAY                         
B879: 77 ; ????
B87A: A8              TAY                         
B87B: 77 ; ????
B87C: 15 7E           ORA     $7E,X               
B87E: 08              PHP                         
B87F: 6A              ROR     A                   
B880: 09 AE           ORA     #$AE                
B882: 09 44           ORA     #$44                
B884: 0C ; ????
B885: A1 11           LDA     ($11,X)             
B887: 78              SEI                         
B888: 12 ; ????
B889: AD 13 76        LDA     $7613               
B88C: 1C ; ????
B88D: 4D 1D 78        EOR     $781D               
B890: 1E A7 1F        ASL     $1FA7,X             
B893: 7E 24 A7        ROR     $A724,X             ; {}
B896: 2C 36 31        BIT     $3136               
B899: 86 36           STX     $36                 
B89B: 76 37           ROR     $37,X               
B89D: AE 3B 7E        LDX     $7E3B               
B8A0: 3C ; ????
B8A1: 71 3C           ADC     ($3C),Y             
B8A3: 72 ; ????
B8A4: FF ; ????
B8A5: 12 ; ????
B8A6: AD 13 76        LDA     $7613               
B8A9: 1C ; ????
B8AA: 4D 1D 78        EOR     $781D               
B8AD: 1E A7 1F        ASL     $1FA7,X             
B8B0: 7E 24 A7        ROR     $A724,X             ; {}
B8B3: 2C 36 31        BIT     $3136               
B8B6: 86 36           STX     $36                 
B8B8: 76 37           ROR     $37,X               
B8BA: AE 3B 7E        LDX     $7E3B               
B8BD: 3C ; ????
B8BE: 71 1F           ADC     ($1F),Y             
B8C0: 3F ; ????
B8C1: 5F ; ????
B8C2: 0F ; ????
B8C3: 30 16           BMI     $B8DB               ; {}
B8C5: 0F ; ????
B8C6: 0F ; ????
B8C7: 38              SEC                         
B8C8: 10 00           BPL     $B8CA               ; {}
B8CA: 0F ; ????
B8CB: 30 03           BMI     $B8D0               ; {}
B8CD: 0F ; ????
B8CE: 0F ; ????
B8CF: 27 ; ????
B8D0: 00              BRK                         
B8D1: 15 0F           ORA     $0F,X               
B8D3: 20 26 07        JSR     $0726               
B8D6: 0F ; ????
B8D7: 31 02           AND     ($02),Y             
B8D9: 15 0F           ORA     $0F,X               
B8DB: 12 ; ????
B8DC: 23 ; ????
B8DD: 31 0F           AND     ($0F),Y             
B8DF: 06 16           ASL     $16                 
B8E1: 38              SEC                         
B8E2: 01 0A           ORA     ($0A,X)             
B8E4: 01 01           ORA     ($01,X)             
B8E6: 01 01           ORA     ($01,X)             
B8E8: 01 04           ORA     ($04,X)             
B8EA: 0A              ASL     A                   
B8EB: 03 ; ????
B8EC: 04 ; ????
B8ED: 01 01           ORA     ($01,X)             
B8EF: 0A              ASL     A                   
B8F0: 01 01           ORA     ($01,X)             
B8F2: 05 01           ORA     $01                 
B8F4: 05 01           ORA     $01                 
B8F6: 01 01           ORA     ($01,X)             
B8F8: 01 01           ORA     ($01,X)             
B8FA: 01 03           ORA     ($03,X)             
B8FC: 03 ; ????
B8FD: 05 01           ORA     $01                 
B8FF: 01 05           ORA     ($05,X)             
B901: 01 01           ORA     ($01,X)             
B903: 01 01           ORA     ($01,X)             
B905: 02 ; ????
B906: 01 01           ORA     ($01,X)             
B908: 01 01           ORA     ($01,X)             
B90A: 01 02           ORA     ($02,X)             
B90C: 03 ; ????
B90D: 02 ; ????
B90E: 03 ; ????
B90F: 01 01           ORA     ($01,X)             
B911: 02 ; ????
B912: 01 01           ORA     ($01,X)             
B914: 05 F8           ORA     $F8                 
B916: EE 02 FC        INC     $FC02               
B919: F8              SED                         
B91A: EF ; ????
B91B: 02 ; ????
B91C: 04 ; ????
B91D: 00              BRK                         
B91E: F0 02           BEQ     $B922               ; {}
B920: FC ; ????
B921: 00              BRK                         
B922: F1 02           SBC     ($02),Y             
B924: 04 ; ????
B925: F8              SED                         
B926: EF ; ????
B927: 42 ; ????
B928: FC ; ????
B929: F8              SED                         
B92A: EE 42 04        INC     $0442               
B92D: 00              BRK                         
B92E: F1 42           SBC     ($42),Y             
B930: FC ; ????
B931: 00              BRK                         
B932: F0 42           BEQ     $B976               ; {}
B934: 04 ; ????
B935: F8              SED                         
B936: EE 02 FC        INC     $FC02               
B939: F8              SED                         
B93A: EF ; ????
B93B: 02 ; ????
B93C: 04 ; ????
B93D: 00              BRK                         
B93E: F1 42           SBC     ($42),Y             
B940: FC ; ????
B941: 00              BRK                         
B942: F0 42           BEQ     $B986               ; {}
B944: 04 ; ????
B945: F8              SED                         
B946: EF ; ????
B947: 42 ; ????
B948: FC ; ????
B949: F8              SED                         
B94A: EE 42 04        INC     $0442               
B94D: 00              BRK                         
B94E: F0 02           BEQ     $B952               ; {}
B950: FC ; ????
B951: 00              BRK                         
B952: F1 02           SBC     ($02),Y             
B954: 04 ; ????
B955: F8              SED                         
B956: E8              INX                         
B957: 02 ; ????
B958: FC ; ????
B959: F8              SED                         
B95A: E9 02           SBC     #$02                
B95C: 04 ; ????
B95D: 00              BRK                         
B95E: E9 C2           SBC     #$C2                
B960: FC ; ????
B961: 00              BRK                         
B962: E8              INX                         
B963: C2 ; ????
B964: 04 ; ????
B965: F8              SED                         
B966: CE 02 FC        DEC     $FC02               
B969: F8              SED                         
B96A: CE 42 04        DEC     $0442               
B96D: 00              BRK                         
B96E: CE 82 FC        DEC     $FC82               
B971: 00              BRK                         
B972: CE C2 04        DEC     $04C2               
B975: F8              SED                         
B976: EE 03 FC        INC     $FC03               
B979: F8              SED                         
B97A: EF ; ????
B97B: 03 ; ????
B97C: 04 ; ????
B97D: 00              BRK                         
B97E: F0 03           BEQ     $B983               ; {}
B980: FC ; ????
B981: 00              BRK                         
B982: F1 03           SBC     ($03),Y             
B984: 04 ; ????
B985: F8              SED                         
B986: EF ; ????
B987: 43 ; ????
B988: FC ; ????
B989: F8              SED                         
B98A: EE 43 04        INC     $0443               
B98D: 00              BRK                         
B98E: F1 43           SBC     ($43),Y             
B990: FC ; ????
B991: 00              BRK                         
B992: F0 43           BEQ     $B9D7               ; {}
B994: 04 ; ????
B995: F8              SED                         
B996: EE 03 FC        INC     $FC03               
B999: F8              SED                         
B99A: EF ; ????
B99B: 03 ; ????
B99C: 04 ; ????
B99D: 00              BRK                         
B99E: F1 43           SBC     ($43),Y             
B9A0: FC ; ????
B9A1: 00              BRK                         
B9A2: F0 43           BEQ     $B9E7               ; {}
B9A4: 04 ; ????
B9A5: F8              SED                         
B9A6: EF ; ????
B9A7: 43 ; ????
B9A8: FC ; ????
B9A9: F8              SED                         
B9AA: EE 43 04        INC     $0443               
B9AD: 00              BRK                         
B9AE: F0 03           BEQ     $B9B3               ; {}
B9B0: FC ; ????
B9B1: 00              BRK                         
B9B2: F1 03           SBC     ($03),Y             
B9B4: 04 ; ????
B9B5: F8              SED                         
B9B6: E8              INX                         
B9B7: 03 ; ????
B9B8: FC ; ????
B9B9: F8              SED                         
B9BA: E9 03           SBC     #$03                
B9BC: 04 ; ????
B9BD: 00              BRK                         
B9BE: E9 C3           SBC     #$C3                
B9C0: FC ; ????
B9C1: 00              BRK                         
B9C2: E8              INX                         
B9C3: C3 ; ????
B9C4: 04 ; ????
B9C5: F8              SED                         
B9C6: CE 03 FC        DEC     $FC03               
B9C9: F8              SED                         
B9CA: CE 43 04        DEC     $0443               
B9CD: 00              BRK                         
B9CE: CE 83 FC        DEC     $FC83               
B9D1: 00              BRK                         
B9D2: CE C3 04        DEC     $04C3               
B9D5: 00              BRK                         
B9D6: 00              BRK                         
B9D7: 00              BRK                         
B9D8: 00              BRK                         
B9D9: 00              BRK                         
B9DA: 00              BRK                         
B9DB: 00              BRK                         
B9DC: 00              BRK                         
B9DD: 00              BRK                         
B9DE: 00              BRK                         
B9DF: 00              BRK                         
B9E0: 00              BRK                         
B9E1: 00              BRK                         
B9E2: 00              BRK                         
B9E3: 00              BRK                         
B9E4: 00              BRK                         
B9E5: 00              BRK                         
B9E6: 00              BRK                         
B9E7: 00              BRK                         
B9E8: 00              BRK                         
B9E9: 00              BRK                         
B9EA: 00              BRK                         
B9EB: 00              BRK                         
B9EC: 00              BRK                         
B9ED: 00              BRK                         
B9EE: 00              BRK                         
B9EF: 00              BRK                         
B9F0: 00              BRK                         
B9F1: 00              BRK                         
B9F2: 00              BRK                         
B9F3: 00              BRK                         
B9F4: 00              BRK                         
B9F5: 00              BRK                         
B9F6: 00              BRK                         
B9F7: 00              BRK                         
B9F8: 00              BRK                         
B9F9: 00              BRK                         
B9FA: 00              BRK                         
B9FB: 00              BRK                         
B9FC: 00              BRK                         
B9FD: 00              BRK                         
B9FE: 00              BRK                         
B9FF: 00              BRK                         
BA00: FF ; ????
BA01: FF ; ????
BA02: FF ; ????
BA03: FF ; ????
BA04: FF ; ????
BA05: FF ; ????
BA06: FF ; ????
BA07: FF ; ????
BA08: FF ; ????
BA09: FF ; ????
BA0A: FF ; ????
BA0B: FF ; ????
BA0C: FF ; ????
BA0D: FF ; ????
BA0E: FF ; ????
BA0F: FF ; ????
BA10: FF ; ????
BA11: FF ; ????
BA12: FF ; ????
BA13: FF ; ????
BA14: FE FF FF        INC     $FFFF,X             
BA17: FF ; ????
BA18: FF ; ????
BA19: FF ; ????
BA1A: FF ; ????
BA1B: FF ; ????
BA1C: FF ; ????
BA1D: FF ; ????
BA1E: FF ; ????
BA1F: FF ; ????
BA20: FF ; ????
BA21: FF ; ????
BA22: FF ; ????
BA23: FF ; ????
BA24: FF ; ????
BA25: FF ; ????
BA26: FF ; ????
BA27: FF ; ????
BA28: FF ; ????
BA29: FF ; ????
BA2A: FF ; ????
BA2B: FF ; ????
BA2C: FF ; ????
BA2D: FF ; ????
BA2E: FF ; ????
BA2F: FF ; ????
BA30: FF ; ????
BA31: FF ; ????
BA32: FF ; ????
BA33: FF ; ????
BA34: BF ; ????
BA35: FF ; ????
BA36: FF ; ????
BA37: FF ; ????
BA38: FF ; ????
BA39: FF ; ????
BA3A: FF ; ????
BA3B: FF ; ????
BA3C: FF ; ????
BA3D: FB ; ????
BA3E: FF ; ????
BA3F: FF ; ????
BA40: FF ; ????
BA41: FF ; ????
BA42: FF ; ????
BA43: FF ; ????
BA44: FF ; ????
BA45: FF ; ????
BA46: FF ; ????
BA47: FF ; ????
BA48: FF ; ????
BA49: FF ; ????
BA4A: FF ; ????
BA4B: FF ; ????
BA4C: FF ; ????
BA4D: FF ; ????
BA4E: FF ; ????
BA4F: FF ; ????
BA50: FF ; ????
BA51: FF ; ????
BA52: FF ; ????
BA53: FF ; ????
BA54: FF ; ????
BA55: FF ; ????
BA56: FF ; ????
BA57: FF ; ????
BA58: FF ; ????
BA59: FF ; ????
BA5A: FF ; ????
BA5B: FF ; ????
BA5C: FF ; ????
BA5D: FF ; ????
BA5E: FF ; ????
BA5F: FF ; ????
BA60: FF ; ????
BA61: FF ; ????
BA62: FF ; ????
BA63: FF ; ????
BA64: FF ; ????
BA65: FF ; ????
BA66: FF ; ????
BA67: FF ; ????
BA68: FF ; ????
BA69: FF ; ????
BA6A: FF ; ????
BA6B: FF ; ????
BA6C: FF ; ????
BA6D: FF ; ????
BA6E: FF ; ????
BA6F: FF ; ????
BA70: FF ; ????
BA71: FF ; ????
BA72: FF ; ????
BA73: FF ; ????
BA74: FF ; ????
BA75: FF ; ????
BA76: FF ; ????
BA77: FF ; ????
BA78: FF ; ????
BA79: FF ; ????
BA7A: FF ; ????
BA7B: FF ; ????
BA7C: FF ; ????
BA7D: FF ; ????
BA7E: FF ; ????
BA7F: FF ; ????
BA80: FF ; ????
BA81: FF ; ????
BA82: FF ; ????
BA83: FF ; ????
BA84: FF ; ????
BA85: FF ; ????
BA86: FF ; ????
BA87: FF ; ????
BA88: FF ; ????
BA89: FF ; ????
BA8A: FF ; ????
BA8B: FF ; ????
BA8C: FF ; ????
BA8D: FF ; ????
BA8E: FF ; ????
BA8F: FF ; ????
BA90: FF ; ????
BA91: FF ; ????
BA92: FF ; ????
BA93: FF ; ????
BA94: FF ; ????
BA95: FF ; ????
BA96: FF ; ????
BA97: FF ; ????
BA98: FF ; ????
BA99: FF ; ????
BA9A: FF ; ????
BA9B: FF ; ????
BA9C: FF ; ????
BA9D: FF ; ????
BA9E: FF ; ????
BA9F: FF ; ????
BAA0: FF ; ????
BAA1: FF ; ????
BAA2: FF ; ????
BAA3: FF ; ????
BAA4: FF ; ????
BAA5: FB ; ????
BAA6: FF ; ????
BAA7: FF ; ????
BAA8: FF ; ????
BAA9: FF ; ????
BAAA: FF ; ????
BAAB: FF ; ????
BAAC: FF ; ????
BAAD: FF ; ????
BAAE: FF ; ????
BAAF: FF ; ????
BAB0: FF ; ????
BAB1: FF ; ????
BAB2: FF ; ????
BAB3: FF ; ????
BAB4: FF ; ????
BAB5: FF ; ????
BAB6: FF ; ????
BAB7: FF ; ????
BAB8: FF ; ????
BAB9: FF ; ????
BABA: FF ; ????
BABB: FF ; ????
BABC: FF ; ????
BABD: FF ; ????
BABE: FF ; ????
BABF: FF ; ????
BAC0: FF ; ????
BAC1: FF ; ????
BAC2: FF ; ????
BAC3: FF ; ????
BAC4: FF ; ????
BAC5: FF ; ????
BAC6: FF ; ????
BAC7: FF ; ????
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
BBF8: 10 B0           BPL     $BBAA               ; {}
BBFA: 01 00           ORA     ($00,X)             ; {ram.GP_00}
BBFC: 00              BRK                         
BBFD: 00              BRK                         
BBFE: 10 00           BPL     $BC00               ; {}
BC00: FF ; ????
BC01: FF ; ????
BC02: FF ; ????
BC03: FF ; ????
BC04: FF ; ????
BC05: FF ; ????
BC06: BF ; ????
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
BC15: FF ; ????
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
BC24: F7 ; ????
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
BC6F: EF ; ????
BC70: FF ; ????
BC71: FF ; ????
BC72: FF ; ????
BC73: FF ; ????
BC74: FF ; ????
BC75: FF ; ????
BC76: FF ; ????
BC77: F7 ; ????
BC78: FF ; ????
BC79: FD FF FF        SBC     $FFFF,X             
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
BCF9: FE FA FD        INC     $FDFA,X             
BCFC: FF ; ????
BCFD: FA ; ????
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
BE2F: BF ; ????
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
BE9C: F7 ; ????
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
BFF8: 81 00           STA     ($00,X)             ; {ram.GP_00}
BFFA: 00              BRK                         
BFFB: D0 00           BNE     $BFFD               ; {}
BFFD: 01 00           ORA     ($00,X)             ; {ram.GP_00}
BFFF: 42 ; ????
```

