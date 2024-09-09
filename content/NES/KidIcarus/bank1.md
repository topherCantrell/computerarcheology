![Bank 1](KidIcarus.jpg)

# Bank 1

>>> cpu 6502

>>> binary 8000:roms/KidIcarus.nes[4010:8010]

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](Hardware.md)

```code
8000: 00              BRK                         
8001: 00              BRK                         
8002: 3D 7E 7F        AND     $7F7E,X             
8005: 7F ; ????
8006: 7E 00 00        ROR     $0000,X             ; {ram.GP_00}
8009: 00              BRK                         
800A: 3A ; ????
800B: 4D 24 84        EOR     $8424               ; {}
800E: C9 FF           CMP     #$FF                
8010: 00              BRK                         
8011: 00              BRK                         
8012: 80 ; ????
8013: 60              RTS                         
8014: 30 38           BMI     $804E               ; {}
8016: 18              CLC                         
8017: 0C ; ????
8018: 00              BRK                         
8019: 00              BRK                         
801A: 00              BRK                         
801B: 80 ; ????
801C: C0 E0           CPY     #$E0                
801E: E0 F0           CPX     #$F0                
8020: 78              SEI                         
8021: FC ; ????
8022: 7E 3F 3E        ROR     $3E3F,X             
8025: 3E 3C 71        ROL     $713C,X             
8028: 87 ; ????
8029: 7B ; ????
802A: 7D 3E 7F        ADC     $7F3E,X             
802D: 5F ; ????
802E: 4F ; ????
802F: 86 0C           STX     $0C                 
8031: 0C ; ????
8032: 1C ; ????
8033: 06 22           ASL     $22                 
8035: 22 ; ????
8036: 61 DE           ADC     ($DE,X)             
8038: F0 F0           BEQ     $802A               ; {}
803A: E0 F8           CPX     #$F8                
803C: DC ; ????
803D: DC ; ????
803E: 9E ; ????
803F: 21 3E           AND     ($3E,X)             
8041: 7F ; ????
8042: 7F ; ????
8043: 7F ; ????
8044: 7F ; ????
8045: 00              BRK                         
8046: 78              SEI                         
8047: 1C ; ????
8048: 3D 4E 26        AND     $264E,X             
804B: 86 CC           STX     $CC                 
804D: FF ; ????
804E: 87 ; ????
804F: 03 ; ????
8050: 80 ; ????
8051: 60              RTS                         
8052: B0 88           BCS     $7FDC               
8054: 08              PHP                         
8055: 0C ; ????
8056: 0C ; ????
8057: 0C ; ????
8058: 00              BRK                         
8059: 80 ; ????
805A: 60              RTS                         
805B: 70 F0           BVS     $804D               ; {}
805D: F0 F0           BEQ     $804F               ; {}
805F: F0 0E           BEQ     $806F               ; {}
8061: 06 27           ASL     $27                 
8063: 1F ; ????
8064: 0F ; ????
8065: 07 ; ????
8066: 07 ; ????
8067: 0C ; ????
8068: 01 09           ORA     ($09,X)             
806A: 29 1F           AND     #$1F                
806C: 0F ; ????
806D: 0F ; ????
806E: 0B ; ????
806F: 10 0C           BPL     $807D               ; {}
8071: 04 ; ????
8072: 14 ; ????
8073: 14 ; ????
8074: 14 ; ????
8075: 92 ; ????
8076: BA              TSX                         
8077: 3D F0 F8        AND     $F8F0,X             
807A: E8              INX                         
807B: E8              INX                         
807C: E8              INX                         
807D: EC C4 D2        CPX     $D2C4               
8080: 00              BRK                         
8081: 00              BRK                         
8082: 00              BRK                         
8083: 00              BRK                         
8084: 00              BRK                         
8085: 00              BRK                         
8086: 00              BRK                         
8087: 00              BRK                         
8088: 00              BRK                         
8089: 00              BRK                         
808A: 00              BRK                         
808B: 00              BRK                         
808C: 00              BRK                         
808D: 00              BRK                         
808E: 07 ; ????
808F: 1F ; ????
8090: 00              BRK                         
8091: 00              BRK                         
8092: 00              BRK                         
8093: 00              BRK                         
8094: 00              BRK                         
8095: 00              BRK                         
8096: E2 ; ????
8097: 72 ; ????
8098: 00              BRK                         
8099: 00              BRK                         
809A: 00              BRK                         
809B: 00              BRK                         
809C: 00              BRK                         
809D: 00              BRK                         
809E: 00              BRK                         
809F: C0 00           CPY     #$00                
80A1: 00              BRK                         
80A2: 1C ; ????
80A3: 3F ; ????
80A4: 3F ; ????
80A5: 3F ; ????
80A6: 3F ; ????
80A7: FF ; ????
80A8: 3F ; ????
80A9: 3F ; ????
80AA: 67 ; ????
80AB: 52 ; ????
80AC: 42 ; ????
80AD: 66 DC           ROR     $DC                 
80AF: 00              BRK                         
80B0: 1B ; ????
80B1: 0D 01 3D        ORA     $3D01               
80B4: FF ; ????
80B5: CE 8E 3F        DEC     $3F8E               
80B8: E0 F2           CPX     #$F2                
80BA: FE C3 01        INC     $01C3,X             
80BD: 30 70           BMI     $812F               ; {}
80BF: C0 83           CPY     #$83                
80C1: 02 ; ????
80C2: 07 ; ????
80C3: FF ; ????
80C4: C1 E0           CMP     ($E0,X)             
80C6: C0 80           CPY     #$80                
80C8: 7C ; ????
80C9: FD F8 00        SBC     $00F8,X             
80CC: 00              BRK                         
80CD: 00              BRK                         
80CE: 00              BRK                         
80CF: 00              BRK                         
80D0: 02 ; ????
80D1: 1C ; ????
80D2: 06 F1           ASL     $F1                 
80D4: 81 7F           STA     ($7F,X)             
80D6: 3F ; ????
80D7: 3E FC E0        ROL     $E0FC,X             
80DA: 0E 00 7E        ASL     $7E00               
80DD: 50 00           BVC     $80DF               ; {}
80DF: 00              BRK                         
80E0: 83 ; ????
80E1: 64 ; ????
80E2: 18              CLC                         
80E3: 00              BRK                         
80E4: 00              BRK                         
80E5: 00              BRK                         
80E6: 00              BRK                         
80E7: 00              BRK                         
80E8: 83 ; ????
80E9: E6 7E           INC     $7E                 
80EB: 3C ; ????
80EC: 00              BRK                         
80ED: 00              BRK                         
80EE: 00              BRK                         
80EF: 00              BRK                         
80F0: 80 ; ????
80F1: 00              BRK                         
80F2: 40              RTI                         
80F3: 20 10 08        JSR     $0810               
80F6: 06 00           ASL     $00                 ; {ram.GP_00}
80F8: 80 ; ????
80F9: 80 ; ????
80FA: C0 60           CPY     #$60                
80FC: 30 38           BMI     $8136               ; {}
80FE: 1E 00 00        ASL     $0000,X             ; {ram.GP_00}
8101: 00              BRK                         
8102: 00              BRK                         
8103: 37 ; ????
8104: 40              RTI                         
8105: 7F ; ????
8106: 59 59 07        EOR     $0759,Y             
8109: 1F ; ????
810A: 3F ; ????
810B: 48              PHA                         
810C: 3F ; ????
810D: 80 ; ????
810E: F7 ; ????
810F: E7 ; ????
8110: 80 ; ????
8111: 60              RTS                         
8112: 30 B8           BMI     $80CC               ; {}
8114: 78              SEI                         
8115: FC ; ????
8116: FC ; ????
8117: FC ; ????
8118: 00              BRK                         
8119: 80 ; ????
811A: C0 40           CPY     #$40                
811C: 80 ; ????
811D: 00              BRK                         
811E: C0 C0           CPY     #$C0                
8120: 23 ; ????
8121: BF ; ????
8122: 1F ; ????
8123: 40              RTI                         
8124: 21 2B           AND     ($2B,X)             
8126: 14 ; ????
8127: 02 ; ????
8128: FF ; ????
8129: 5E 60 3F        LSR     $3F60,X             
812C: 5E 44 28        LSR     $2844,X             
812F: 04 ; ????
8130: FB ; ????
8131: FC ; ????
8132: F4 ; ????
8133: 72 ; ????
8134: F3 ; ????
8135: 90 10           BCC     $8147               ; {}
8137: 08              PHP                         
8138: 84 03           STY     $03                 
813A: 08              PHP                         
813B: 84 04           STY     $04                 
813D: 23 ; ????
813E: 20 10 00        JSR     $0010               
8141: 04 ; ????
8142: 18              CLC                         
8143: 20 40 40        JSR     $4040               
8146: 80 ; ????
8147: 80 ; ????
8148: 00              BRK                         
8149: 03 ; ????
814A: 07 ; ????
814B: 1F ; ????
814C: 3F ; ????
814D: 3F ; ????
814E: 7F ; ????
814F: 7F ; ????
8150: 4E 3F 1F        LSR     $1F3F               
8153: 1F ; ????
8154: 0F ; ????
8155: 00              BRK                         
8156: 00              BRK                         
8157: 00              BRK                         
8158: 31 1E           AND     ($1E),Y             
815A: 7A ; ????
815B: EC 90 CD        CPX     $CD90               
815E: 4C 06 04        JMP     $0406               
8161: 18              CLC                         
8162: 20 20 40        JSR     $4020               
8165: 41 4F           EOR     ($4F,X)             
8167: 5F ; ????
8168: 03 ; ????
8169: 07 ; ????
816A: 1F ; ????
816B: 1F ; ????
816C: 3F ; ????
816D: 3E 30 28        ROL     $2830,X             
8170: 5F ; ????
8171: 3F ; ????
8172: 1F ; ????
8173: 0E 02 00        ASL     $0002               
8176: 00              BRK                         
8177: 00              BRK                         
8178: 3C ; ????
8179: 1A ; ????
817A: 3E 3D 35        ROL     $353D,X             
817D: 36 12           ROL     $12,X               
817F: 0A              ASL     A                   
8180: 3F ; ????
8181: 7F ; ????
8182: E3 ; ????
8183: 60              RTS                         
8184: 60              RTS                         
8185: 00              BRK                         
8186: 00              BRK                         
8187: 01 40           ORA     ($40,X)             
8189: 80 ; ????
818A: 00              BRK                         
818B: 80 ; ????
818C: 00              BRK                         
818D: 00              BRK                         
818E: 01 01           ORA     ($01,X)             
8190: 08              PHP                         
8191: 0F ; ????
8192: 87 ; ????
8193: 03 ; ????
8194: 03 ; ????
8195: 07 ; ????
8196: 0C ; ????
8197: F8              SED                         
8198: F7 ; ????
8199: F0 78           BEQ     $8213               ; {}
819B: 3C ; ????
819C: 1C ; ????
819D: 38              SEC                         
819E: F0 40           BEQ     $81E0               ; {}
81A0: 41 C6           EOR     ($C6,X)             
81A2: E2 ; ????
81A3: F2 ; ????
81A4: C9 81           CMP     #$81                
81A6: 06 FC           ASL     $FC                 
81A8: BE 38 1C        LDX     $1C38,Y             
81AB: 0C ; ????
81AC: 06 06           ASL     $06                 
81AE: F8              SED                         
81AF: A0 07           LDY     #$07                
81B1: 04 ; ????
81B2: 00              BRK                         
81B3: 07 ; ????
81B4: 01 01           ORA     ($01,X)             
81B6: 03 ; ????
81B7: 07 ; ????
81B8: 00              BRK                         
81B9: 03 ; ????
81BA: 07 ; ????
81BB: 05 00           ORA     $00                 ; {ram.GP_00}
81BD: 00              BRK                         
81BE: 04 ; ????
81BF: 00              BRK                         
81C0: 07 ; ????
81C1: 1F ; ????
81C2: 3F ; ????
81C3: 3F ; ????
81C4: 7F ; ????
81C5: 7F ; ????
81C6: 7E FE 03        ROR     $03FE,X             
81C9: 0F ; ????
81CA: 1F ; ????
81CB: 1F ; ????
81CC: 3C ; ????
81CD: 38              SEC                         
81CE: 31 B1           AND     ($B1),Y             
81D0: BF ; ????
81D1: 3F ; ????
81D2: 3F ; ????
81D3: 6F ; ????
81D4: 5F ; ????
81D5: 37 ; ????
81D6: 27 ; ????
81D7: 03 ; ????
81D8: 1C ; ????
81D9: 07 ; ????
81DA: 2D 4D 00        AND     $004D               
81DD: 25 03           AND     $03                 
81DF: 00              BRK                         
81E0: F8              SED                         
81E1: FE D6 D5        INC     $D5D6,X             
81E4: 41 00           EOR     ($00,X)             ; {ram.GP_00}
81E6: 00              BRK                         
81E7: 08              PHP                         
81E8: 4F ; ????
81E9: 03 ; ????
81EA: 29 2A           AND     #$2A                
81EC: BE FF FF        LDX     $FFFF,Y             
81EF: F7 ; ????
81F0: C0 78           CPY     #$78                
81F2: 1C ; ????
81F3: 06 06           ASL     $06                 
81F5: 03 ; ????
81F6: 21 41           AND     ($41,X)             
81F8: 40              RTI                         
81F9: 88              DEY                         
81FA: E0 FA           CPX     #$FA                
81FC: F8              SED                         
81FD: FC ; ????
81FE: DF ; ????
81FF: BE 61 BF        LDX     $BF61,Y             ; {}
8202: 3F ; ????
8203: 63 ; ????
8204: D1 C1           CMP     ($C1),Y             
8206: E3 ; ????
8207: 7F ; ????
8208: 61 A1           ADC     ($A1,X)             
820A: 00              BRK                         
820B: 1C ; ????
820C: 3E 3E 1C        ROL     $1C3E,X             
820F: 00              BRK                         
8210: 80 ; ????
8211: 4C 9E FB        JMP     $FB9E               
8214: DC ; ????
8215: DE 92 A1        DEC     $A192,X             ; {}
8218: 80 ; ????
8219: 40              RTI                         
821A: 0C ; ????
821B: 0A              ASL     A                   
821C: 20 20 6C        JSR     $6C20               
821F: 5F ; ????
8220: 0F ; ????
8221: DF ; ????
8222: 77 ; ????
8223: A7 ; ????
8224: 1D 31 98        ORA     $9831,X             ; {}
8227: E1 00           SBC     ($00,X)             ; {ram.GP_00}
8229: 00              BRK                         
822A: 98              TYA                         
822B: 58              CLI                         
822C: E2 ; ????
822D: CE E7 9E        DEC     $9EE7               ; {}
8230: 00              BRK                         
8231: 87 ; ????
8232: 4F ; ????
8233: 9E ; ????
8234: F8              SED                         
8235: DC ; ????
8236: DE 92 00        DEC     $0092,X             
8239: 80 ; ????
823A: 47 ; ????
823B: 0E 18 20        ASL     $2018               
823E: 20 6C 60        JSR     $606C               
8241: 4F ; ????
8242: 0F ; ????
8243: 2E 1E 07        ROL     $071E               
8246: 07 ; ????
8247: 14 ; ????
8248: 7F ; ????
8249: 50 30           BVC     $827B               ; {}
824B: 31 11           AND     ($11),Y             
824D: 01 00           ORA     ($00,X)             ; {ram.GP_00}
824F: 1F ; ????
8250: F0 FD           BEQ     $824F               ; {}
8252: 1E FC FC        ASL     $FCFC,X             
8255: 40              RTI                         
8256: C0 00           CPY     #$00                
8258: CF ; ????
8259: 47 ; ????
825A: E0 00           CPX     #$00                
825C: 00              BRK                         
825D: FE 00 E0        INC     $E000,X             
8260: 7F ; ????
8261: 60              RTS                         
8262: 5F ; ????
8263: 3F ; ????
8264: 1D 0E 28        ORA     $280E,X             
8267: 01 00           ORA     ($00,X)             ; {ram.GP_00}
8269: 7F ; ????
826A: 40              RTI                         
826B: 00              BRK                         
826C: 02 ; ????
826D: 01 3F           ORA     ($3F,X)             
826F: 01 A2           ORA     ($A2,X)             
8271: E2 ; ????
8272: F6 FC           INC     $FC,X               
8274: FC ; ????
8275: FC ; ????
8276: F8              SED                         
8277: 40              RTI                         
8278: 5C ; ????
8279: DC ; ????
827A: 5C ; ????
827B: 08              PHP                         
827C: 00              BRK                         
827D: 00              BRK                         
827E: 00              BRK                         
827F: FE 00 00        INC     $0000,X             ; {ram.GP_00}
8282: 00              BRK                         
8283: 00              BRK                         
8284: 00              BRK                         
8285: 1F ; ????
8286: 70 C0           BVS     $8248               ; {}
8288: 00              BRK                         
8289: 00              BRK                         
828A: 00              BRK                         
828B: 00              BRK                         
828C: 00              BRK                         
828D: 00              BRK                         
828E: 0F ; ????
828F: 3F ; ????
8290: 00              BRK                         
8291: 04 ; ????
8292: 08              PHP                         
8293: 08              PHP                         
8294: 4B ; ????
8295: 21 60           AND     ($60,X)             
8297: C0 00           CPY     #$00                
8299: 02 ; ????
829A: 84 44           STY     $44                 
829C: 34 ; ????
829D: 1E 1F 3F        ASL     $3F1F,X             
82A0: 00              BRK                         
82A1: 20 42 82        JSR     $8242               ; {}
82A4: A4 58           LDY     $58                 
82A6: 0C ; ????
82A7: 07 ; ????
82A8: 50 14           BVC     $82BE               ; {}
82AA: 20 40 40        JSR     $4040               
82AD: E6 F8           INC     $F8                 
82AF: F8              SED                         
82B0: 00              BRK                         
82B1: 20 91 93        JSR     $9391               ; {}
82B4: 4E 32 51        LSR     $5132               
82B7: 1D 30 14        ORA     $1430,X             
82BA: 08              PHP                         
82BB: 49 39           EOR     #$39                
82BD: 0D 2F 3E        ORA     $3E2F               
82C0: 00              BRK                         
82C1: 40              RTI                         
82C2: 88              DEY                         
82C3: C8              INY                         
82C4: 30 D0           BMI     $8296               ; {}
82C6: E6 E8           INC     $E8                 
82C8: 40              RTI                         
82C9: 80 ; ????
82CA: 04 ; ????
82CB: 10 C0           BPL     $828D               ; {}
82CD: E0 D8           CPX     #$D8                
82CF: 10 5E           BPL     $832F               ; {}
82D1: 2F ; ????
82D2: 27 ; ????
82D3: 2F ; ????
82D4: 1F ; ????
82D5: 5F ; ????
82D6: 3F ; ????
82D7: DE 2D 90        DEC     $902D,X             ; {}
82DA: 1B ; ????
82DB: 14 ; ????
82DC: 08              PHP                         
82DD: 11 16           ORA     ($16),Y             
82DF: 29 4C           AND     #$4C                
82E1: C8              INY                         
82E2: E0 F2           CPX     #$F2                
82E4: F8              SED                         
82E5: FC ; ????
82E6: FA ; ????
82E7: 31 B0           AND     ($B0),Y             
82E9: 30 D0           BMI     $82BB               ; {}
82EB: 28              PLP                         
82EC: 16 CA           ASL     $CA,X               
82EE: 34 ; ????
82EF: CE FC 06        DEC     $06FC               
82F2: 03 ; ????
82F3: 01 01           ORA     ($01,X)             
82F5: 01 F9           ORA     ($F9,X)             
82F7: 81 48           STA     ($48,X)             
82F9: F8              SED                         
82FA: FD FE FE        SBC     $FEFE,X             
82FD: FE 07 7E        INC     $7E07,X             
8300: 1E 23 FD        ASL     $FD23,X             
8303: 98              TYA                         
8304: 4D 7C 39        EOR     $397C               
8307: 06 00           ASL     $00                 ; {ram.GP_00}
8309: 1C ; ????
830A: 9A              TXS                         
830B: 67 ; ????
830C: BA              TSX                         
830D: 0B ; ????
830E: 06 78           ASL     $78                 
8310: C0 B4           CPY     #$B4                
8312: 3E FF 96        ROL     $96FF,X             ; {}
8315: 82 ; ????
8316: 02 ; ????
8317: 83 ; ????
8318: 00              BRK                         
8319: C0 C0           CPY     #$C0                
831B: 00              BRK                         
831C: 69 7D           ADC     #$7D                
831E: FD 7C 00        SBC     $007C,X             
8321: 7C ; ????
8322: FE B7 A7        INC     $A7B7,X             ; {}
8325: 27 ; ????
8326: 05 01           ORA     $01                 
8328: 00              BRK                         
8329: 48              PHA                         
832A: 02 ; ????
832B: 48              PHA                         
832C: 59 D8 FB        EOR     $FBD8,Y             
832F: FE 00 03        INC     $0300,X             
8332: 04 ; ????
8333: 1F ; ????
8334: 03 ; ????
8335: 08              PHP                         
8336: 0F ; ????
8337: 00              BRK                         
8338: 00              BRK                         
8339: 00              BRK                         
833A: 03 ; ????
833B: 13 ; ????
833C: 1C ; ????
833D: 17 ; ????
833E: 00              BRK                         
833F: 0F ; ????
8340: 00              BRK                         
8341: 00              BRK                         
8342: 00              BRK                         
8343: 00              BRK                         
8344: 00              BRK                         
8345: 00              BRK                         
8346: 00              BRK                         
8347: 00              BRK                         
8348: 00              BRK                         
8349: 00              BRK                         
834A: 00              BRK                         
834B: 00              BRK                         
834C: 00              BRK                         
834D: 00              BRK                         
834E: 00              BRK                         
834F: 00              BRK                         
8350: 00              BRK                         
8351: 00              BRK                         
8352: 00              BRK                         
8353: 00              BRK                         
8354: 00              BRK                         
8355: 00              BRK                         
8356: 00              BRK                         
8357: 00              BRK                         
8358: 00              BRK                         
8359: 00              BRK                         
835A: 00              BRK                         
835B: 00              BRK                         
835C: 00              BRK                         
835D: 00              BRK                         
835E: 00              BRK                         
835F: 00              BRK                         
8360: 00              BRK                         
8361: 00              BRK                         
8362: 00              BRK                         
8363: 00              BRK                         
8364: 00              BRK                         
8365: 00              BRK                         
8366: 00              BRK                         
8367: 00              BRK                         
8368: 00              BRK                         
8369: 00              BRK                         
836A: 00              BRK                         
836B: 00              BRK                         
836C: 00              BRK                         
836D: 00              BRK                         
836E: 00              BRK                         
836F: 00              BRK                         
8370: 00              BRK                         
8371: 00              BRK                         
8372: 00              BRK                         
8373: 00              BRK                         
8374: 00              BRK                         
8375: 00              BRK                         
8376: 00              BRK                         
8377: 00              BRK                         
8378: 00              BRK                         
8379: 00              BRK                         
837A: 00              BRK                         
837B: 00              BRK                         
837C: 00              BRK                         
837D: 00              BRK                         
837E: 00              BRK                         
837F: 00              BRK                         
8380: 00              BRK                         
8381: 00              BRK                         
8382: 00              BRK                         
8383: 00              BRK                         
8384: 00              BRK                         
8385: 00              BRK                         
8386: 00              BRK                         
8387: 00              BRK                         
8388: 00              BRK                         
8389: 00              BRK                         
838A: 00              BRK                         
838B: 00              BRK                         
838C: 00              BRK                         
838D: 00              BRK                         
838E: 00              BRK                         
838F: 00              BRK                         
8390: 00              BRK                         
8391: 00              BRK                         
8392: 00              BRK                         
8393: 00              BRK                         
8394: 00              BRK                         
8395: 00              BRK                         
8396: 00              BRK                         
8397: 00              BRK                         
8398: 00              BRK                         
8399: 00              BRK                         
839A: 00              BRK                         
839B: 00              BRK                         
839C: 00              BRK                         
839D: 00              BRK                         
839E: 00              BRK                         
839F: 00              BRK                         
83A0: 00              BRK                         
83A1: 00              BRK                         
83A2: 00              BRK                         
83A3: 00              BRK                         
83A4: 00              BRK                         
83A5: 00              BRK                         
83A6: 00              BRK                         
83A7: 00              BRK                         
83A8: 00              BRK                         
83A9: 00              BRK                         
83AA: 00              BRK                         
83AB: 00              BRK                         
83AC: 00              BRK                         
83AD: 00              BRK                         
83AE: 00              BRK                         
83AF: 00              BRK                         
83B0: 00              BRK                         
83B1: 00              BRK                         
83B2: 00              BRK                         
83B3: 00              BRK                         
83B4: 00              BRK                         
83B5: 00              BRK                         
83B6: 00              BRK                         
83B7: 00              BRK                         
83B8: 00              BRK                         
83B9: 00              BRK                         
83BA: 00              BRK                         
83BB: 00              BRK                         
83BC: 00              BRK                         
83BD: 00              BRK                         
83BE: 00              BRK                         
83BF: 00              BRK                         
83C0: 00              BRK                         
83C1: 00              BRK                         
83C2: 00              BRK                         
83C3: 00              BRK                         
83C4: 00              BRK                         
83C5: 00              BRK                         
83C6: 00              BRK                         
83C7: 00              BRK                         
83C8: 00              BRK                         
83C9: 00              BRK                         
83CA: 00              BRK                         
83CB: 00              BRK                         
83CC: 00              BRK                         
83CD: 00              BRK                         
83CE: 00              BRK                         
83CF: 00              BRK                         
83D0: 00              BRK                         
83D1: 00              BRK                         
83D2: 00              BRK                         
83D3: 00              BRK                         
83D4: 00              BRK                         
83D5: 00              BRK                         
83D6: 00              BRK                         
83D7: 00              BRK                         
83D8: 00              BRK                         
83D9: 00              BRK                         
83DA: 00              BRK                         
83DB: 00              BRK                         
83DC: 00              BRK                         
83DD: 00              BRK                         
83DE: 00              BRK                         
83DF: 00              BRK                         
83E0: 00              BRK                         
83E1: 00              BRK                         
83E2: 00              BRK                         
83E3: 00              BRK                         
83E4: 00              BRK                         
83E5: 00              BRK                         
83E6: 00              BRK                         
83E7: 00              BRK                         
83E8: 00              BRK                         
83E9: 00              BRK                         
83EA: 00              BRK                         
83EB: 00              BRK                         
83EC: 00              BRK                         
83ED: 00              BRK                         
83EE: 00              BRK                         
83EF: 00              BRK                         
83F0: 00              BRK                         
83F1: 00              BRK                         
83F2: 00              BRK                         
83F3: 00              BRK                         
83F4: 00              BRK                         
83F5: 00              BRK                         
83F6: 00              BRK                         
83F7: 00              BRK                         
83F8: 00              BRK                         
83F9: 00              BRK                         
83FA: 00              BRK                         
83FB: 00              BRK                         
83FC: 00              BRK                         
83FD: 00              BRK                         
83FE: 00              BRK                         
83FF: 00              BRK                         
8400: 2C FE FC        BIT     $FCFE               
8403: FE F6 E4        INC     $E4F6,X             
8406: 00              BRK                         
8407: C0 D0           CPY     #$D0                
8409: C4 E8           CPY     $E8                 
840B: DC ; ????
840C: D4 ; ????
840D: E4 00           CPX     $00                 ; {ram.GP_00}
840F: 00              BRK                         
8410: C0 FF           CPY     #$FF                
8412: 7F ; ????
8413: 7F ; ????
8414: 73 ; ????
8415: 78              SEI                         
8416: 08              PHP                         
8417: 1A ; ????
8418: 3F ; ????
8419: 7F ; ????
841A: BF ; ????
841B: FF ; ????
841C: F3 ; ????
841D: F8              SED                         
841E: 00              BRK                         
841F: 00              BRK                         
8420: 80 ; ????
8421: 7F ; ????
8422: 7F ; ????
8423: 3F ; ????
8424: 1C ; ????
8425: 58              CLI                         
8426: 00              BRK                         
8427: 00              BRK                         
8428: 7F ; ????
8429: BF ; ????
842A: DF ; ????
842B: BF ; ????
842C: 9C ; ????
842D: D8              CLD                         
842E: 00              BRK                         
842F: 00              BRK                         
8430: 07 ; ????
8431: CA              DEX                         
8432: F6 FC           INC     $FC,X               
8434: FC ; ????
8435: FC ; ????
8436: 00              BRK                         
8437: 00              BRK                         
8438: F8              SED                         
8439: C0 E4           CPY     #$E4                
843B: EC FC FC        CPX     $FCFC               
843E: 00              BRK                         
843F: 00              BRK                         
8440: 26 65           ROL     $65                 
8442: D3 ; ????
8443: 76 E6           ROR     $E6,X               
8445: C2 ; ????
8446: 78              SEI                         
8447: ED 3E 7F        SBC     $7F3E               
844A: FF ; ????
844B: 7E FE FE        ROR     $FEFE,X             
844E: 78              SEI                         
844F: ED 66 A3        SBC     $A366               ; {}
8452: 85 63           STA     $63                 
8454: D6 EB           DEC     $EB,X               
8456: 81 43           STA     ($43,X)             
8458: 7E FF FF        ROR     $FFFF,X             
845B: F7 ; ????
845C: F6 FF           INC     $FF,X               
845E: BF ; ????
845F: 7F ; ????
8460: FF ; ????
8461: FF ; ????
8462: FF ; ????
8463: FF ; ????
8464: FF ; ????
8465: FF ; ????
8466: FF ; ????
8467: FF ; ????
8468: 1C ; ????
8469: 38              SEC                         
846A: 70 F1           BVS     $845D               ; {}
846C: E3 ; ????
846D: 87 ; ????
846E: 0E 1C 10        ASL     $101C               
8471: 38              SEC                         
8472: 7C ; ????
8473: 7C ; ????
8474: 7C ; ????
8475: 7C ; ????
8476: 3C ; ????
8477: 38              SEC                         
8478: 10 38           BPL     $84B2               ; {}
847A: 6C 64 44        JMP     ($4464)             
847D: 64 ; ????
847E: 2C 38 00        BIT     $0038               
8481: 00              BRK                         
8482: 54 ; ????
8483: 55 74           EOR     $74,X               
8485: 5E D7 FC        LSR     $FCD7,X             
8488: 00              BRK                         
8489: 54 ; ????
848A: FD FF FD        SBC     $FDFF,X             
848D: FF ; ????
848E: FF ; ????
848F: FD 74 55        SBC     $5574,X             
8492: D7 ; ????
8493: FF ; ????
8494: 7D 5D 54        ADC     $545D,X             
8497: 00              BRK                         
8498: FD FD FF        SBC     $FFFD,X             
849B: FF ; ????
849C: 7D 5D 54        ADC     $545D,X             
849F: 00              BRK                         
84A0: 00              BRK                         
84A1: 07 ; ????
84A2: 1C ; ????
84A3: 78              SEI                         
84A4: F0 DB           BEQ     $8481               ; {}
84A6: FE 90 00        INC     $0090,X             
84A9: 00              BRK                         
84AA: 00              BRK                         
84AB: 00              BRK                         
84AC: 80 ; ????
84AD: E0 90           CPX     #$90                
84AF: 00              BRK                         
84B0: 78              SEI                         
84B1: C7 ; ????
84B2: 00              BRK                         
84B3: 00              BRK                         
84B4: 38              SEC                         
84B5: E4 00           CPX     $00                 ; {ram.GP_00}
84B7: 00              BRK                         
84B8: 00              BRK                         
84B9: 00              BRK                         
84BA: 00              BRK                         
84BB: 00              BRK                         
84BC: 00              BRK                         
84BD: 00              BRK                         
84BE: 00              BRK                         
84BF: 00              BRK                         
84C0: 90 EE           BCC     $84B0               ; {}
84C2: 7B ; ????
84C3: 70 38           BVS     $84FD               ; {}
84C5: 0C ; ????
84C6: 07 ; ????
84C7: 00              BRK                         
84C8: 00              BRK                         
84C9: 90 E0           BCC     $84AB               ; {}
84CB: 80 ; ????
84CC: 00              BRK                         
84CD: 00              BRK                         
84CE: 00              BRK                         
84CF: 00              BRK                         
84D0: 00              BRK                         
84D1: 00              BRK                         
84D2: C6 78           DEC     $78                 
84D4: 00              BRK                         
84D5: 00              BRK                         
84D6: 8F ; ????
84D7: F0 00           BEQ     $84D9               ; {}
84D9: 00              BRK                         
84DA: 00              BRK                         
84DB: 00              BRK                         
84DC: 00              BRK                         
84DD: 00              BRK                         
84DE: 00              BRK                         
84DF: 00              BRK                         
84E0: 35 35           AND     $35,X               
84E2: 35 35           AND     $35,X               
84E4: 35 35           AND     $35,X               
84E6: 35 35           AND     $35,X               
84E8: 1F ; ????
84E9: 1F ; ????
84EA: 1F ; ????
84EB: 1F ; ????
84EC: 1F ; ????
84ED: 1F ; ????
84EE: 1F ; ????
84EF: 1F ; ????
84F0: AC AC AC        LDY     $ACAC               ; {}
84F3: AC AC AC        LDY     $ACAC               ; {}
84F6: AC AC F8        LDY     $F8AC               
84F9: F8              SED                         
84FA: F8              SED                         
84FB: F8              SED                         
84FC: F8              SED                         
84FD: F8              SED                         
84FE: F8              SED                         
84FF: F8              SED                         
8500: 00              BRK                         
8501: 1F ; ????
8502: 3F ; ????
8503: 7F ; ????
8504: 7D 7E 7B        ADC     $7B7E,X             
8507: 76 00           ROR     $00,X               ; {ram.GP_00}
8509: 1F ; ????
850A: 23 ; ????
850B: 4C 50 58        JMP     $5850               
850E: 70 64           BVS     $8574               ; {}
8510: 00              BRK                         
8511: FE FF EF        INC     $EFFF,X             
8514: F7 ; ????
8515: AB ; ????
8516: F5 FD           SBC     $FD,X               
8518: 00              BRK                         
8519: FE FD 0D        INC     $0DFD,X             
851C: E7 ; ????
851D: 03 ; ????
851E: 85 A5           STA     $A5                 
8520: 7A ; ????
8521: 7B ; ????
8522: 3D 3E 3F        AND     $3F3E,X             
8525: 1F ; ????
8526: 0F ; ????
8527: 00              BRK                         
8528: 68              PLA                         
8529: 68              PLA                         
852A: 2C 36 39        BIT     $3936               
852D: 1F ; ????
852E: 0F ; ????
852F: 00              BRK                         
8530: FD 3D FB        SBC     $FB3D,X             
8533: 1F ; ????
8534: FE FE FC        INC     $FCFE,X             
8537: 00              BRK                         
8538: A5 05           LDA     $05                 
853A: 33 ; ????
853B: 0F ; ????
853C: 9E ; ????
853D: 72 ; ????
853E: EC 00 7E        CPX     $7E00               
8541: FF ; ????
8542: DD FE 95        CMP     $95FE,X             ; {}
8545: 44 ; ????
8546: 85 4C           STA     $4C                 
8548: 28              PLP                         
8549: 82 ; ????
854A: 04 ; ????
854B: 80 ; ????
854C: 00              BRK                         
854D: 00              BRK                         
854E: F1 FD           SBC     ($FD),Y             
8550: 75 DB           ADC     $DB,X               
8552: 50 00           BVC     $8554               ; {}
8554: 00              BRK                         
8555: 00              BRK                         
8556: 00              BRK                         
8557: 00              BRK                         
8558: F7 ; ????
8559: DB ; ????
855A: 52 ; ????
855B: 00              BRK                         
855C: 00              BRK                         
855D: 00              BRK                         
855E: 00              BRK                         
855F: 00              BRK                         
8560: 00              BRK                         
8561: E0 38           CPX     #$38                
8563: 1E 0F DB        ASL     $DB0F,X             
8566: 7F ; ????
8567: 39 00 00        AND     $0000,Y             ; {ram.GP_00}
856A: 00              BRK                         
856B: 00              BRK                         
856C: 01 07           ORA     ($07,X)             
856E: 09 10           ORA     #$10                
8570: C2 ; ????
8571: 02 ; ????
8572: 00              BRK                         
8573: 00              BRK                         
8574: 00              BRK                         
8575: 00              BRK                         
8576: 00              BRK                         
8577: 00              BRK                         
8578: 36 26           ROL     $26,X               
857A: 00              BRK                         
857B: 00              BRK                         
857C: 00              BRK                         
857D: 00              BRK                         
857E: 00              BRK                         
857F: 00              BRK                         
8580: 00              BRK                         
8581: 00              BRK                         
8582: 63 ; ????
8583: 1E 00 00        ASL     $0000,X             ; {ram.GP_00}
8586: 71 0E           ADC     ($0E),Y             
8588: 00              BRK                         
8589: 00              BRK                         
858A: 00              BRK                         
858B: 00              BRK                         
858C: 00              BRK                         
858D: 00              BRK                         
858E: 00              BRK                         
858F: 00              BRK                         
8590: CF ; ????
8591: 08              PHP                         
8592: 08              PHP                         
8593: 00              BRK                         
8594: FC ; ????
8595: 80 ; ????
8596: 80 ; ????
8597: 00              BRK                         
8598: 20 E4 E5        JSR     $E5E4               
859B: 00              BRK                         
859C: 02 ; ????
859D: 7E 6E 00        ROR     $006E,X             
85A0: 1C ; ????
85A1: 63 ; ????
85A2: 00              BRK                         
85A3: 00              BRK                         
85A4: 1C ; ????
85A5: 67 ; ????
85A6: 00              BRK                         
85A7: 00              BRK                         
85A8: 00              BRK                         
85A9: 00              BRK                         
85AA: 00              BRK                         
85AB: 00              BRK                         
85AC: 00              BRK                         
85AD: 00              BRK                         
85AE: 00              BRK                         
85AF: 00              BRK                         
85B0: CC AA 99        CPY     $99AA               ; {}
85B3: 73 ; ????
85B4: CF ; ????
85B5: E3 ; ????
85B6: 41 30           EOR     ($30,X)             
85B8: FF ; ????
85B9: FF ; ????
85BA: FB ; ????
85BB: 73 ; ????
85BC: FF ; ????
85BD: FF ; ????
85BE: 7F ; ????
85BF: 3C ; ????
85C0: 39 77 CA        AND     $CA77,Y             
85C3: 0E 1C 30        ASL     $301C               
85C6: E0 00           CPX     #$00                
85C8: 10 09           BPL     $85D3               ; {}
85CA: 07 ; ????
85CB: 01 00           ORA     ($00,X)             ; {ram.GP_00}
85CD: 00              BRK                         
85CE: 00              BRK                         
85CF: 00              BRK                         
85D0: 62 ; ????
85D1: F6 9E           INC     $9E,X               
85D3: CE 4F 07        DEC     $074F               
85D6: 4E 8C FE        LSR     $FE8C               
85D9: FE 9F CE        INC     $CE9F,X             
85DC: FF ; ????
85DD: FF ; ????
85DE: FE EC 3C        INC     $3CEC,X             
85E1: 7E 63 C1        ROR     $C163,X             
85E4: C9 4F           CMP     #$4F                
85E6: 40              RTI                         
85E7: 26 3C           ROL     $3C                 
85E9: 7E 7F E3        ROR     $E37F,X             
85EC: EF ; ????
85ED: 7F ; ????
85EE: 5F ; ????
85EF: 26 3C           ROL     $3C                 
85F1: 7E C6 83        ROR     $83C6,X             ; {}
85F4: 93 ; ????
85F5: F2 ; ????
85F6: 02 ; ????
85F7: 64 ; ????
85F8: 3C ; ????
85F9: 7E FE C7        ROR     $C7FE,X             
85FC: F7 ; ????
85FD: FE FA 64        INC     $64FA,X             
8600: 7F ; ????
8601: F5 A5           SBC     $A5,X               
8603: A1 9F           LDA     ($9F,X)             
8605: 12 ; ????
8606: 14 ; ????
8607: 18              CLC                         
8608: 00              BRK                         
8609: 00              BRK                         
860A: 08              PHP                         
860B: 4A              LSR     A                   
860C: 5E FC FB        LSR     $FBFC,X             
860F: F7 ; ????
8610: FE 97 97        INC     $9797,X             ; {}
8613: 07 ; ????
8614: 79 3B 70        ADC     $703B,Y             
8617: E3 ; ????
8618: 00              BRK                         
8619: 00              BRK                         
861A: 22 ; ????
861B: 6A              ROR     A                   
861C: 60              RTS                         
861D: C6 8E           DEC     $8E                 
861F: 1F ; ????
8620: 11 23           ORA     ($23),Y             
8622: 00              BRK                         
8623: 00              BRK                         
8624: 00              BRK                         
8625: 00              BRK                         
8626: 00              BRK                         
8627: 00              BRK                         
8628: 66 40           ROR     $40                 
862A: 00              BRK                         
862B: 00              BRK                         
862C: 00              BRK                         
862D: 00              BRK                         
862E: 00              BRK                         
862F: 00              BRK                         
8630: 00              BRK                         
8631: 00              BRK                         
8632: 00              BRK                         
8633: 00              BRK                         
8634: 00              BRK                         
8635: 00              BRK                         
8636: 00              BRK                         
8637: 00              BRK                         
8638: 00              BRK                         
8639: 00              BRK                         
863A: 00              BRK                         
863B: 00              BRK                         
863C: 00              BRK                         
863D: 00              BRK                         
863E: 00              BRK                         
863F: 00              BRK                         
8640: 00              BRK                         
8641: 00              BRK                         
8642: 00              BRK                         
8643: 00              BRK                         
8644: 00              BRK                         
8645: 00              BRK                         
8646: 00              BRK                         
8647: 00              BRK                         
8648: 00              BRK                         
8649: 00              BRK                         
864A: 00              BRK                         
864B: 00              BRK                         
864C: 00              BRK                         
864D: 00              BRK                         
864E: 00              BRK                         
864F: 00              BRK                         
8650: 00              BRK                         
8651: 00              BRK                         
8652: 00              BRK                         
8653: 00              BRK                         
8654: 00              BRK                         
8655: 00              BRK                         
8656: 00              BRK                         
8657: 00              BRK                         
8658: 00              BRK                         
8659: 00              BRK                         
865A: 00              BRK                         
865B: 00              BRK                         
865C: 00              BRK                         
865D: 00              BRK                         
865E: 00              BRK                         
865F: 00              BRK                         
8660: 00              BRK                         
8661: 00              BRK                         
8662: 00              BRK                         
8663: 00              BRK                         
8664: 00              BRK                         
8665: 00              BRK                         
8666: 00              BRK                         
8667: 00              BRK                         
8668: 00              BRK                         
8669: 00              BRK                         
866A: 00              BRK                         
866B: 00              BRK                         
866C: 00              BRK                         
866D: 00              BRK                         
866E: 00              BRK                         
866F: 00              BRK                         
8670: 00              BRK                         
8671: 00              BRK                         
8672: 00              BRK                         
8673: 00              BRK                         
8674: 00              BRK                         
8675: 00              BRK                         
8676: 00              BRK                         
8677: 00              BRK                         
8678: 00              BRK                         
8679: 00              BRK                         
867A: 00              BRK                         
867B: 00              BRK                         
867C: 00              BRK                         
867D: 00              BRK                         
867E: 00              BRK                         
867F: 00              BRK                         
8680: 00              BRK                         
8681: 00              BRK                         
8682: 00              BRK                         
8683: 00              BRK                         
8684: 00              BRK                         
8685: 00              BRK                         
8686: 00              BRK                         
8687: 00              BRK                         
8688: 00              BRK                         
8689: 00              BRK                         
868A: 00              BRK                         
868B: 00              BRK                         
868C: 00              BRK                         
868D: 00              BRK                         
868E: 00              BRK                         
868F: 00              BRK                         
8690: 00              BRK                         
8691: 00              BRK                         
8692: 00              BRK                         
8693: 00              BRK                         
8694: 00              BRK                         
8695: 00              BRK                         
8696: 00              BRK                         
8697: 00              BRK                         
8698: 00              BRK                         
8699: 00              BRK                         
869A: 00              BRK                         
869B: 00              BRK                         
869C: 00              BRK                         
869D: 00              BRK                         
869E: 00              BRK                         
869F: 00              BRK                         
86A0: 00              BRK                         
86A1: 00              BRK                         
86A2: 00              BRK                         
86A3: 00              BRK                         
86A4: 00              BRK                         
86A5: 00              BRK                         
86A6: 00              BRK                         
86A7: 00              BRK                         
86A8: 00              BRK                         
86A9: 00              BRK                         
86AA: 00              BRK                         
86AB: 00              BRK                         
86AC: 00              BRK                         
86AD: 00              BRK                         
86AE: 00              BRK                         
86AF: 00              BRK                         
86B0: 00              BRK                         
86B1: 00              BRK                         
86B2: 00              BRK                         
86B3: 00              BRK                         
86B4: 00              BRK                         
86B5: 00              BRK                         
86B6: 00              BRK                         
86B7: 00              BRK                         
86B8: 00              BRK                         
86B9: 00              BRK                         
86BA: 00              BRK                         
86BB: 00              BRK                         
86BC: 00              BRK                         
86BD: 00              BRK                         
86BE: 00              BRK                         
86BF: 00              BRK                         
86C0: 00              BRK                         
86C1: 00              BRK                         
86C2: 00              BRK                         
86C3: 00              BRK                         
86C4: 00              BRK                         
86C5: 00              BRK                         
86C6: 00              BRK                         
86C7: 00              BRK                         
86C8: 00              BRK                         
86C9: 00              BRK                         
86CA: 00              BRK                         
86CB: 00              BRK                         
86CC: 00              BRK                         
86CD: 00              BRK                         
86CE: 00              BRK                         
86CF: 00              BRK                         
86D0: 00              BRK                         
86D1: 00              BRK                         
86D2: 00              BRK                         
86D3: 00              BRK                         
86D4: 00              BRK                         
86D5: 00              BRK                         
86D6: 00              BRK                         
86D7: 00              BRK                         
86D8: 00              BRK                         
86D9: 00              BRK                         
86DA: 00              BRK                         
86DB: 00              BRK                         
86DC: 00              BRK                         
86DD: 00              BRK                         
86DE: 00              BRK                         
86DF: 00              BRK                         
86E0: 00              BRK                         
86E1: 00              BRK                         
86E2: 00              BRK                         
86E3: 00              BRK                         
86E4: 00              BRK                         
86E5: 00              BRK                         
86E6: 00              BRK                         
86E7: 00              BRK                         
86E8: 00              BRK                         
86E9: 00              BRK                         
86EA: 00              BRK                         
86EB: 00              BRK                         
86EC: 00              BRK                         
86ED: 00              BRK                         
86EE: 00              BRK                         
86EF: 00              BRK                         
86F0: 00              BRK                         
86F1: 00              BRK                         
86F2: 00              BRK                         
86F3: 00              BRK                         
86F4: 00              BRK                         
86F5: 00              BRK                         
86F6: 00              BRK                         
86F7: 00              BRK                         
86F8: 00              BRK                         
86F9: 00              BRK                         
86FA: 00              BRK                         
86FB: 00              BRK                         
86FC: 00              BRK                         
86FD: 00              BRK                         
86FE: 00              BRK                         
86FF: 00              BRK                         
8700: 00              BRK                         
8701: 00              BRK                         
8702: 00              BRK                         
8703: 00              BRK                         
8704: 00              BRK                         
8705: 00              BRK                         
8706: 00              BRK                         
8707: 00              BRK                         
8708: 00              BRK                         
8709: 00              BRK                         
870A: 00              BRK                         
870B: 00              BRK                         
870C: 00              BRK                         
870D: 00              BRK                         
870E: 00              BRK                         
870F: 00              BRK                         
8710: 00              BRK                         
8711: 00              BRK                         
8712: 00              BRK                         
8713: 00              BRK                         
8714: 00              BRK                         
8715: 00              BRK                         
8716: 00              BRK                         
8717: 00              BRK                         
8718: 00              BRK                         
8719: 00              BRK                         
871A: 00              BRK                         
871B: 00              BRK                         
871C: 00              BRK                         
871D: 00              BRK                         
871E: 00              BRK                         
871F: 00              BRK                         
8720: 00              BRK                         
8721: 00              BRK                         
8722: 00              BRK                         
8723: 00              BRK                         
8724: 00              BRK                         
8725: 00              BRK                         
8726: 00              BRK                         
8727: 00              BRK                         
8728: 00              BRK                         
8729: 00              BRK                         
872A: 00              BRK                         
872B: 00              BRK                         
872C: 00              BRK                         
872D: 00              BRK                         
872E: 00              BRK                         
872F: 00              BRK                         
8730: 00              BRK                         
8731: 00              BRK                         
8732: 00              BRK                         
8733: 00              BRK                         
8734: 00              BRK                         
8735: 00              BRK                         
8736: 00              BRK                         
8737: 00              BRK                         
8738: 00              BRK                         
8739: 00              BRK                         
873A: 00              BRK                         
873B: 00              BRK                         
873C: 00              BRK                         
873D: 00              BRK                         
873E: 00              BRK                         
873F: 00              BRK                         
8740: 00              BRK                         
8741: 00              BRK                         
8742: 00              BRK                         
8743: 00              BRK                         
8744: 00              BRK                         
8745: 00              BRK                         
8746: 00              BRK                         
8747: 00              BRK                         
8748: 00              BRK                         
8749: 00              BRK                         
874A: 00              BRK                         
874B: 00              BRK                         
874C: 00              BRK                         
874D: 00              BRK                         
874E: 00              BRK                         
874F: 00              BRK                         
8750: 00              BRK                         
8751: 00              BRK                         
8752: 00              BRK                         
8753: 00              BRK                         
8754: 00              BRK                         
8755: 00              BRK                         
8756: 00              BRK                         
8757: 00              BRK                         
8758: 00              BRK                         
8759: 00              BRK                         
875A: 00              BRK                         
875B: 00              BRK                         
875C: 00              BRK                         
875D: 00              BRK                         
875E: 00              BRK                         
875F: 00              BRK                         
8760: 00              BRK                         
8761: 00              BRK                         
8762: 00              BRK                         
8763: 00              BRK                         
8764: 00              BRK                         
8765: 00              BRK                         
8766: 00              BRK                         
8767: 00              BRK                         
8768: 00              BRK                         
8769: 00              BRK                         
876A: 00              BRK                         
876B: 00              BRK                         
876C: 00              BRK                         
876D: 00              BRK                         
876E: 00              BRK                         
876F: 00              BRK                         
8770: 00              BRK                         
8771: 00              BRK                         
8772: 00              BRK                         
8773: 00              BRK                         
8774: 00              BRK                         
8775: 00              BRK                         
8776: 00              BRK                         
8777: 00              BRK                         
8778: 00              BRK                         
8779: 00              BRK                         
877A: 00              BRK                         
877B: 00              BRK                         
877C: 00              BRK                         
877D: 00              BRK                         
877E: 00              BRK                         
877F: 00              BRK                         
8780: 00              BRK                         
8781: 00              BRK                         
8782: 00              BRK                         
8783: 00              BRK                         
8784: 00              BRK                         
8785: 00              BRK                         
8786: 00              BRK                         
8787: 00              BRK                         
8788: 00              BRK                         
8789: 00              BRK                         
878A: 00              BRK                         
878B: 00              BRK                         
878C: 00              BRK                         
878D: 00              BRK                         
878E: 00              BRK                         
878F: 00              BRK                         
8790: 00              BRK                         
8791: 00              BRK                         
8792: 00              BRK                         
8793: 00              BRK                         
8794: 00              BRK                         
8795: 00              BRK                         
8796: 00              BRK                         
8797: 00              BRK                         
8798: 00              BRK                         
8799: 00              BRK                         
879A: 00              BRK                         
879B: 00              BRK                         
879C: 00              BRK                         
879D: 00              BRK                         
879E: 00              BRK                         
879F: 00              BRK                         
87A0: 00              BRK                         
87A1: 00              BRK                         
87A2: 00              BRK                         
87A3: 00              BRK                         
87A4: 00              BRK                         
87A5: 00              BRK                         
87A6: 00              BRK                         
87A7: 00              BRK                         
87A8: 00              BRK                         
87A9: 00              BRK                         
87AA: 00              BRK                         
87AB: 00              BRK                         
87AC: 00              BRK                         
87AD: 00              BRK                         
87AE: 00              BRK                         
87AF: 00              BRK                         
87B0: 00              BRK                         
87B1: 00              BRK                         
87B2: 00              BRK                         
87B3: 00              BRK                         
87B4: 00              BRK                         
87B5: 00              BRK                         
87B6: 00              BRK                         
87B7: 00              BRK                         
87B8: 00              BRK                         
87B9: 00              BRK                         
87BA: 00              BRK                         
87BB: 00              BRK                         
87BC: 00              BRK                         
87BD: 00              BRK                         
87BE: 00              BRK                         
87BF: 00              BRK                         
87C0: 00              BRK                         
87C1: 00              BRK                         
87C2: 00              BRK                         
87C3: 00              BRK                         
87C4: 00              BRK                         
87C5: 00              BRK                         
87C6: 00              BRK                         
87C7: 00              BRK                         
87C8: 00              BRK                         
87C9: 00              BRK                         
87CA: 00              BRK                         
87CB: 00              BRK                         
87CC: 00              BRK                         
87CD: 00              BRK                         
87CE: 00              BRK                         
87CF: 00              BRK                         
87D0: 00              BRK                         
87D1: 00              BRK                         
87D2: 00              BRK                         
87D3: 00              BRK                         
87D4: 00              BRK                         
87D5: 00              BRK                         
87D6: 00              BRK                         
87D7: 00              BRK                         
87D8: 00              BRK                         
87D9: 00              BRK                         
87DA: 00              BRK                         
87DB: 00              BRK                         
87DC: 00              BRK                         
87DD: 00              BRK                         
87DE: 00              BRK                         
87DF: 00              BRK                         
87E0: 00              BRK                         
87E1: 00              BRK                         
87E2: 00              BRK                         
87E3: 00              BRK                         
87E4: 00              BRK                         
87E5: 00              BRK                         
87E6: 00              BRK                         
87E7: 00              BRK                         
87E8: 00              BRK                         
87E9: 00              BRK                         
87EA: 00              BRK                         
87EB: 00              BRK                         
87EC: 00              BRK                         
87ED: 00              BRK                         
87EE: 00              BRK                         
87EF: 00              BRK                         
87F0: 00              BRK                         
87F1: 00              BRK                         
87F2: 00              BRK                         
87F3: 00              BRK                         
87F4: 00              BRK                         
87F5: 00              BRK                         
87F6: 00              BRK                         
87F7: 00              BRK                         
87F8: 00              BRK                         
87F9: 00              BRK                         
87FA: 00              BRK                         
87FB: 00              BRK                         
87FC: 00              BRK                         
87FD: 00              BRK                         
87FE: 00              BRK                         
87FF: 00              BRK                         
8800: 04 ; ????
8801: 02 ; ????
8802: 3A ; ????
8803: 1F ; ????
8804: 79 8C 02        ADC     $028C,Y             
8807: 00              BRK                         
8808: 18              CLC                         
8809: 3D 05 18        AND     $1805,X             
880C: 06 73           ASL     $73                 
880E: FD FF 12        SBC     $12FF,X             
8811: 04 ; ????
8812: FC ; ????
8813: FC ; ????
8814: FB ; ????
8815: E7 ; ????
8816: 0E 3B E4        ASL     $E43B               
8819: F8              SED                         
881A: 00              BRK                         
881B: F3 ; ????
881C: 64 ; ????
881D: 1B ; ????
881E: F2 ; ????
881F: C5 31           CMP     $31                 
8821: 7F ; ????
8822: FF ; ????
8823: 7F ; ????
8824: 0F ; ????
8825: 01 00           ORA     ($00,X)             ; {ram.GP_00}
8827: 00              BRK                         
8828: CE B1 1F        DEC     $1FB1               
882B: 4F ; ????
882C: 00              BRK                         
882D: 00              BRK                         
882E: 00              BRK                         
882F: 00              BRK                         
8830: EC EF F9        CPX     $F9EF               
8833: DC ; ????
8834: FE FF FF        INC     $FFFF,X             
8837: 7E 33 B0        ROR     $B033,X             ; {}
883A: A6 63           LDX     $63                 
883C: 11 E4           ORA     ($E4),Y             
883E: 0C ; ????
883F: 70 7C           BVS     $88BD               ; {}
8841: 83 ; ????
8842: 01 31           ORA     ($31,X)             
8844: 58              CLI                         
8845: 0E 0F 01        ASL     $010F               
8848: 01 7C           ORA     ($7C,X)             
884A: FE CE 87        INC     $87CE,X             ; {}
884D: 01 00           ORA     ($00,X)             ; {ram.GP_00}
884F: 26 10           ROL     $10                 
8851: E9 FB           SBC     #$FB                
8853: F6 E0           INC     $E0,X               
8855: 0F ; ????
8856: F7 ; ????
8857: D8              CLD                         
8858: E1 12           SBC     ($12,X)             
885A: E5 6A           SBC     $6A                 
885C: 1F ; ????
885D: F0 0F           BEQ     $886E               ; {}
885F: 66 05           ROR     $05                 
8861: 07 ; ????
8862: 07 ; ????
8863: 3F ; ????
8864: 3F ; ????
8865: 1F ; ????
8866: 00              BRK                         
8867: 00              BRK                         
8868: 1A ; ????
8869: 00              BRK                         
886A: 00              BRK                         
886B: 20 1F 00        JSR     $001F               
886E: 00              BRK                         
886F: 00              BRK                         
8870: DE BF F8        DEC     $F8BF,X             
8873: FC ; ????
8874: FE FF FF        INC     $FFFF,X             
8877: 7E 61 C8        ROR     $C861,X             
887A: 16 F3           ASL     $F3,X               
887C: 01 E4           ORA     ($E4,X)             
887E: 0C ; ????
887F: 70 00           BVS     $8881               ; {}
8881: 00              BRK                         
8882: 0D 1F 3F        ORA     $3F1F               
8885: 3F ; ????
8886: 78              SEI                         
8887: 70 00           BVS     $8889               ; {}
8889: 03 ; ????
888A: 0B ; ????
888B: 1C ; ????
888C: 3F ; ????
888D: 30 67           BMI     $88F6               ; {}
888F: 4F ; ????
8890: 70 60           BVS     $88F2               ; {}
8892: 6F ; ????
8893: 3F ; ????
8894: 3F ; ????
8895: 1F ; ????
8896: 0F ; ????
8897: 03 ; ????
8898: 4F ; ????
8899: 5F ; ????
889A: 10 0F           BPL     $88AB               ; {}
889C: 1F ; ????
889D: 0F ; ????
889E: 03 ; ????
889F: 00              BRK                         
88A0: 1F ; ????
88A1: 3E 3E 3E        ROL     $3E3E,X             
88A4: 1F ; ????
88A5: 1D 03 FF        ORA     $FF03,X             
88A8: 18              CLC                         
88A9: 2D 0D 3D        AND     $3D0D               
88AC: 79 E3 FD        ADC     $FDE3,Y             
88AF: 00              BRK                         
88B0: 00              BRK                         
88B1: C0 F0           CPY     #$F0                
88B3: 38              SEC                         
88B4: 0C ; ????
88B5: 0C ; ????
88B6: 06 06           ASL     $06                 
88B8: 00              BRK                         
88B9: 40              RTI                         
88BA: 10 C0           BPL     $887C               ; {}
88BC: F4 ; ????
88BD: F0 FA           BEQ     $88B9               ; {}
88BF: F8              SED                         
88C0: 02 ; ????
88C1: 09 14           ORA     #$14                
88C3: 20 04 7E        JSR     $7E04               
88C6: 1E 2C 01        ASL     $012C,X             
88C9: 07 ; ????
88CA: 0F ; ????
88CB: 1F ; ????
88CC: 3F ; ????
88CD: 3F ; ????
88CE: 73 ; ????
88CF: 7F ; ????
88D0: C0 30           CPY     #$30                
88D2: 78              SEI                         
88D3: 4C 9C F6        JMP     $F69C               
88D6: F6 6E           INC     $6E,X               
88D8: C0 F0           CPY     #$F0                
88DA: F8              SED                         
88DB: FC ; ????
88DC: FC ; ????
88DD: FE 9E FE        INC     $FE9E,X             
88E0: D1 37           CMP     ($37),Y             
88E2: 9C ; ????
88E3: 70 22           BVS     $8907               ; {}
88E5: 4F ; ????
88E6: 24 9E           BIT     $9E                 
88E8: 3F ; ????
88E9: FF ; ????
88EA: FF ; ????
88EB: 7F ; ????
88EC: 3F ; ????
88ED: 3F ; ????
88EE: 7C ; ????
88EF: 7E 1B D1        ROR     $D11B,X             
88F2: 6D 92 7C        ADC     $7C92               
88F5: E6 12           INC     $12                 
88F7: 0F ; ????
88F8: F7 ; ????
88F9: EF ; ????
88FA: FF ; ????
88FB: FE FC FE        INC     $FEFC,X             
88FE: 3E 7F 00        ROL     $007F,X             
8901: 00              BRK                         
8902: 00              BRK                         
8903: 3F ; ????
8904: 77 ; ????
8905: 7B ; ????
8906: FB ; ????
8907: F7 ; ????
8908: 00              BRK                         
8909: 00              BRK                         
890A: 00              BRK                         
890B: 00              BRK                         
890C: 38              SEC                         
890D: 6C 4C 38        JMP     ($384C)             
8910: 00              BRK                         
8911: 00              BRK                         
8912: 00              BRK                         
8913: C0 F0           CPY     #$F0                
8915: F8              SED                         
8916: F8              SED                         
8917: FC ; ????
8918: 00              BRK                         
8919: 00              BRK                         
891A: 00              BRK                         
891B: 00              BRK                         
891C: 40              RTI                         
891D: 00              BRK                         
891E: 00              BRK                         
891F: 00              BRK                         
8920: 3B ; ????
8921: 7D FB FF        ADC     $FFFB,X             
8924: 83 ; ????
8925: 01 19           ORA     ($19,X)             
8927: 4F ; ????
8928: 2C 4E 3C        BIT     $3C4E               
892B: 00              BRK                         
892C: 3C ; ????
892D: 0E 06 42        ASL     $4206               
8930: 9E ; ????
8931: F8              SED                         
8932: F0 F0           BEQ     $8924               ; {}
8934: F8              SED                         
8935: F8              SED                         
8936: FC ; ????
8937: FC ; ????
8938: 1E 78 E0        ASL     $E078,X             
893B: 00              BRK                         
893C: 00              BRK                         
893D: 00              BRK                         
893E: 00              BRK                         
893F: 00              BRK                         
8940: FF ; ????
8941: 9F ; ????
8942: 7F ; ????
8943: 3E 1E 0F        ROL     $0F1E,X             
8946: 03 ; ????
8947: 1F ; ????
8948: 00              BRK                         
8949: 60              RTS                         
894A: 70 39           BVS     $8985               ; {}
894C: 1F ; ????
894D: 03 ; ????
894E: 00              BRK                         
894F: 11 FC           ORA     ($FC),Y             
8951: FE 0E FF        INC     $FF0E,X             
8954: FE 7C 18        INC     $187C,X             
8957: FE F0 3C        INC     $3CF0,X             
895A: F0 00           BEQ     $895C               ; {}
895C: 00              BRK                         
895D: 80 ; ????
895E: 00              BRK                         
895F: 00              BRK                         
8960: 3F ; ????
8961: 1F ; ????
8962: 0F ; ????
8963: 07 ; ????
8964: 07 ; ????
8965: 03 ; ????
8966: 00              BRK                         
8967: 00              BRK                         
8968: 3E 1F 0F        ROL     $0F1F,X             
896B: 03 ; ????
896C: 01 00           ORA     ($00,X)             ; {ram.GP_00}
896E: 00              BRK                         
896F: 00              BRK                         
8970: FE BE 7C        INC     $7CBE,X             
8973: 70 F4           BVS     $8969               ; {}
8975: BC C6 63        LDY     $63C6,X             
8978: 00              BRK                         
8979: 40              RTI                         
897A: 80 ; ????
897B: 80 ; ????
897C: 80 ; ????
897D: 00              BRK                         
897E: 00              BRK                         
897F: 21 00           AND     ($00,X)             ; {ram.GP_00}
8981: 19 3F 7F        ORA     $7F3F,Y             
8984: 7F ; ????
8985: 7F ; ????
8986: 7F ; ????
8987: 7F ; ????
8988: 00              BRK                         
8989: 7F ; ????
898A: 3F ; ????
898B: 69 55           ADC     #$55                
898D: 40              RTI                         
898E: 65 7F           ADC     $7F                 
8990: 00              BRK                         
8991: 80 ; ????
8992: C0 F8           CPY     #$F8                
8994: FE FF FF        INC     $FFFF,X             
8997: FF ; ????
8998: 00              BRK                         
8999: 80 ; ????
899A: C0 F8           CPY     #$F8                
899C: E2 ; ????
899D: C1 81           CMP     ($81,X)             
899F: F1 19           SBC     ($19),Y             
89A1: 3F ; ????
89A2: 7F ; ????
89A3: 7F ; ????
89A4: 7F ; ????
89A5: 7F ; ????
89A6: 7F ; ????
89A7: 3F ; ????
89A8: 7F ; ????
89A9: 3F ; ????
89AA: 69 55           ADC     #$55                
89AC: 40              RTI                         
89AD: 65 7F           ADC     $7F                 
89AF: 3F ; ????
89B0: 80 ; ????
89B1: C0 F8           CPY     #$F8                
89B3: FE FF FF        INC     $FFFF,X             
89B6: E7 ; ????
89B7: E3 ; ????
89B8: 80 ; ????
89B9: C0 F8           CPY     #$F8                
89BB: E2 ; ????
89BC: C1 F9           CMP     ($F9,X)             
89BE: 3D 3D 27        AND     $273D,X             
89C1: 3F ; ????
89C2: 2B ; ????
89C3: 40              RTI                         
89C4: 3C ; ????
89C5: 7E 01 00        ROR     $0001,X             
89C8: 1B ; ????
89C9: 7F ; ????
89CA: 7E 7F 07        ROR     $077F,X             
89CD: 7F ; ????
89CE: 01 00           ORA     ($00,X)             ; {ram.GP_00}
89D0: EF ; ????
89D1: E7 ; ????
89D2: CF ; ????
89D3: 07 ; ????
89D4: 06 04           ASL     $04                 
89D6: BE 7C 39        LDX     $397C,Y             
89D9: 39 FB FF        AND     $FFFB,Y             
89DC: FE FC C2        INC     $C2FC,X             
89DF: 7C ; ????
89E0: 2B ; ????
89E1: 00              BRK                         
89E2: 28              PLP                         
89E3: 10 08           BPL     $89ED               ; {}
89E5: 01 07           ORA     ($07,X)             
89E7: 0F ; ????
89E8: 3E 3F 3F        ROL     $3F3F,X             
89EB: 1F ; ????
89EC: 0F ; ????
89ED: 07 ; ????
89EE: 00              BRK                         
89EF: 0F ; ????
89F0: C7 ; ????
89F1: 03 ; ????
89F2: 03 ; ????
89F3: 06 FC           ASL     $FC                 
89F5: F8              SED                         
89F6: 1C ; ????
89F7: D8              CLD                         
89F8: FD FF FF        SBC     $FFFF,X             
89FB: FE 0C F8        INC     $F80C,X             
89FE: FC ; ????
89FF: F8              SED                         
8A00: 1F ; ????
8A01: 3F ; ????
8A02: 3F ; ????
8A03: 13 ; ????
8A04: 43 ; ????
8A05: E7 ; ????
8A06: FF ; ????
8A07: 3F ; ????
8A08: 1F ; ????
8A09: 3F ; ????
8A0A: 00              BRK                         
8A0B: 3C ; ????
8A0C: 7C ; ????
8A0D: D8              CLD                         
8A0E: 21 3F           AND     ($3F,X)             
8A10: 80 ; ????
8A11: E0 F0           CPX     #$F0                
8A13: F0 F0           BEQ     $8A05               ; {}
8A15: F0 F0           BEQ     $8A07               ; {}
8A17: E0 00           CPX     #$00                
8A19: 80 ; ????
8A1A: 40              RTI                         
8A1B: C0 C0           CPY     #$C0                
8A1D: C0 C0           CPY     #$C0                
8A1F: 00              BRK                         
8A20: 03 ; ????
8A21: 1F ; ????
8A22: 67 ; ????
8A23: F7 ; ????
8A24: FF ; ????
8A25: FF ; ????
8A26: 3F ; ????
8A27: 7F ; ????
8A28: 3E 0F 61        ROL     $610F,X             
8A2B: F3 ; ????
8A2C: 3F ; ????
8A2D: FF ; ????
8A2E: 17 ; ????
8A2F: 40              RTI                         
8A30: F8              SED                         
8A31: FC ; ????
8A32: FC ; ????
8A33: FE FE FE        INC     $FEFE,X             
8A36: FE FE F0        INC     $F0FE,X             
8A39: F8              SED                         
8A3A: B8              CLV                         
8A3B: 38              SEC                         
8A3C: F8              SED                         
8A3D: F0 C2           BEQ     $8A01               ; {}
8A3F: 04 ; ????
8A40: FF ; ????
8A41: FF ; ????
8A42: 67 ; ????
8A43: 07 ; ????
8A44: 1F ; ????
8A45: 3F ; ????
8A46: 7E 78 D0        ROR     $D078,X             
8A49: 47 ; ????
8A4A: 07 ; ????
8A4B: 03 ; ????
8A4C: 1F ; ????
8A4D: 3E 78 70        ROL     $7078,X             
8A50: FE FE FE        INC     $FEFE,X             
8A53: FE FC FC        INC     $FCFC,X             
8A56: 78              SEI                         
8A57: F8              SED                         
8A58: 0C ; ????
8A59: FC ; ????
8A5A: FC ; ????
8A5B: F8              SED                         
8A5C: F8              SED                         
8A5D: 30 70           BMI     $8ACF               ; {}
8A5F: F0 3C           BEQ     $8A9D               ; {}
8A61: 1C ; ????
8A62: 3E 7F 00        ROL     $007F,X             
8A65: 00              BRK                         
8A66: 00              BRK                         
8A67: 00              BRK                         
8A68: 38              SEC                         
8A69: 18              CLC                         
8A6A: 3C ; ????
8A6B: 40              RTI                         
8A6C: 00              BRK                         
8A6D: 00              BRK                         
8A6E: 00              BRK                         
8A6F: 00              BRK                         
8A70: F0 F8           BEQ     $8A6A               ; {}
8A72: 78              SEI                         
8A73: 7C ; ????
8A74: 3C ; ????
8A75: 3E 7F FF        ROL     $FF7F,X             
8A78: E0 E0           CPX     #$E0                
8A7A: 70 70           BVS     $8AEC               ; {}
8A7C: 38              SEC                         
8A7D: 38              SEC                         
8A7E: 7C ; ????
8A7F: C0 FF           CPY     #$FF                
8A81: FF ; ????
8A82: 63 ; ????
8A83: 03 ; ????
8A84: 01 01           ORA     ($01,X)             
8A86: 03 ; ????
8A87: 03 ; ????
8A88: D7 ; ????
8A89: 47 ; ????
8A8A: 03 ; ????
8A8B: 03 ; ????
8A8C: 00              BRK                         
8A8D: 01 03           ORA     ($03,X)             
8A8F: 03 ; ????
8A90: FE FE FE        INC     $FEFE,X             
8A93: FC ; ????
8A94: F8              SED                         
8A95: F0 E0           BEQ     $8A77               ; {}
8A97: E0 FC           CPX     #$FC                
8A99: FC ; ????
8A9A: F8              SED                         
8A9B: F0 E0           BEQ     $8A7D               ; {}
8A9D: C0 A0           CPY     #$A0                
8A9F: A0 03           LDY     #$03                
8AA1: 01 00           ORA     ($00,X)             ; {ram.GP_00}
8AA3: 01 03           ORA     ($03,X)             
8AA5: 00              BRK                         
8AA6: 03 ; ????
8AA7: 07 ; ????
8AA8: 03 ; ????
8AA9: 01 00           ORA     ($00,X)             ; {ram.GP_00}
8AAB: 01 02           ORA     ($02,X)             
8AAD: 00              BRK                         
8AAE: 03 ; ????
8AAF: 04 ; ????
8AB0: E0 F0           CPX     #$F0                
8AB2: F8              SED                         
8AB3: FC ; ????
8AB4: FC ; ????
8AB5: F0 F8           BEQ     $8AAF               ; {}
8AB7: F8              SED                         
8AB8: 80 ; ????
8AB9: C0 E0           CPY     #$E0                
8ABB: F0 00           BEQ     $8ABD               ; {}
8ABD: E0 E0           CPX     #$E0                
8ABF: 00              BRK                         
8AC0: 02 ; ????
8AC1: 0C ; ????
8AC2: 18              CLC                         
8AC3: 30 3C           BMI     $8B01               ; {}
8AC5: 30 30           BMI     $8AF7               ; {}
8AC7: 3E 02 04        ROL     $0402,X             
8ACA: 08              PHP                         
8ACB: 10 1C           BPL     $8AE9               ; {}
8ACD: 10 10           BPL     $8ADF               ; {}
8ACF: 1E 18 18        ASL     $1818,X             
8AD2: 18              CLC                         
8AD3: 3C ; ????
8AD4: 3D 3B 23        AND     $233B,X             
8AD7: 47 ; ????
8AD8: 08              PHP                         
8AD9: 1B ; ????
8ADA: 07 ; ????
8ADB: 13 ; ????
8ADC: 03 ; ????
8ADD: 27 ; ????
8ADE: 3F ; ????
8ADF: 7F ; ????
8AE0: 00              BRK                         
8AE1: 00              BRK                         
8AE2: 00              BRK                         
8AE3: 40              RTI                         
8AE4: 80 ; ????
8AE5: 80 ; ????
8AE6: A0 E8           LDY     #$E8                
8AE8: 00              BRK                         
8AE9: 00              BRK                         
8AEA: 00              BRK                         
8AEB: 40              RTI                         
8AEC: 80 ; ????
8AED: 80 ; ????
8AEE: A0 68           LDY     #$68                
8AF0: 68              PLA                         
8AF1: 38              SEC                         
8AF2: 1C ; ????
8AF3: 30 78           BMI     $8B6D               ; {}
8AF5: 79 77 8F        ADC     $8F77,Y             ; {}
8AF8: 28              PLP                         
8AF9: 18              CLC                         
8AFA: 0D 0F 27        ORA     $270F               
8AFD: 07 ; ????
8AFE: 4F ; ????
8AFF: FF ; ????
8B00: 0F ; ????
8B01: 3F ; ????
8B02: 7F ; ????
8B03: 90 10           BCC     $8B15               ; {}
8B05: 00              BRK                         
8B06: 66 66           ROR     $66                 
8B08: 00              BRK                         
8B09: 01 00           ORA     ($00,X)             ; {ram.GP_00}
8B0B: 6F ; ????
8B0C: EF ; ????
8B0D: FF ; ????
8B0E: FF ; ????
8B0F: 66 80           ROR     $80                 
8B11: E0 F0           CPX     #$F0                
8B13: F8              SED                         
8B14: 78              SEI                         
8B15: 3C ; ????
8B16: 1C ; ????
8B17: DC ; ????
8B18: 00              BRK                         
8B19: 80 ; ????
8B1A: 20 00 80        JSR     $8000               ; {}
8B1D: C0 E0           CPY     #$E0                
8B1F: E0 00           CPX     #$00                
8B21: 00              BRK                         
8B22: 49 00           EOR     #$00                
8B24: 00              BRK                         
8B25: 01 0C           ORA     ($0C,X)             
8B27: 06 00           ASL     $00                 ; {ram.GP_00}
8B29: 00              BRK                         
8B2A: C9 FF           CMP     #$FF                
8B2C: 7F ; ????
8B2D: 3E 08 04        ROL     $0408,X             
8B30: 0F ; ????
8B31: 0F ; ????
8B32: 1C ; ????
8B33: 3C ; ????
8B34: F7 ; ????
8B35: B3 ; ????
8B36: 30 18           BMI     $8B50               ; {}
8B38: 34 ; ????
8B39: 33 ; ????
8B3A: E0 C0           CPX     #$C0                
8B3C: 04 ; ????
8B3D: 23 ; ????
8B3E: 20 10 0C        JSR     $0C10               
8B41: 06 C6           ASL     $C6                 
8B43: F7 ; ????
8B44: FC ; ????
8B45: FC ; ????
8B46: 7B ; ????
8B47: 68              PLA                         
8B48: 70 F8           BVS     $8B42               ; {}
8B4A: 39 C8 E2        AND     $E2C8,Y             
8B4D: 0B ; ????
8B4E: 34 ; ????
8B4F: 12 ; ????
8B50: 10 54           BPL     $8BA6               ; {}
8B52: 28              PLP                         
8B53: D6 28           DEC     $28,X               
8B55: 54 ; ????
8B56: 10 00           BPL     $8B58               ; {}
8B58: 10 44           BPL     $8B9E               ; {}
8B5A: 28              PLP                         
8B5B: 82 ; ????
8B5C: 28              PLP                         
8B5D: 44 ; ????
8B5E: 10 00           BPL     $8B60               ; {}
8B60: 00              BRK                         
8B61: 04 ; ????
8B62: 36 73           ROL     $73,X               
8B64: BF ; ????
8B65: 9E ; ????
8B66: 80 ; ????
8B67: C0 00           CPY     #$00                
8B69: 03 ; ????
8B6A: 1D 1E 4E        ORA     $4E1E,X             
8B6D: 61 7F           ADC     ($7F,X)             
8B6F: 3F ; ????
8B70: 7F ; ????
8B71: 7F ; ????
8B72: 7F ; ????
8B73: 3F ; ????
8B74: 3F ; ????
8B75: 1F ; ????
8B76: 0F ; ????
8B77: 03 ; ????
8B78: 70 4F           BVS     $8BC9               ; {}
8B7A: 1F ; ????
8B7B: 1F ; ????
8B7C: 1F ; ????
8B7D: 0F ; ????
8B7E: 03 ; ????
8B7F: 00              BRK                         
8B80: 63 ; ????
8B81: 3F ; ????
8B82: 07 ; ????
8B83: 07 ; ????
8B84: 1F ; ????
8B85: 3F ; ????
8B86: 37 ; ????
8B87: FB ; ????
8B88: 1C ; ????
8B89: 00              BRK                         
8B8A: 03 ; ????
8B8B: 03 ; ????
8B8C: 07 ; ????
8B8D: 17 ; ????
8B8E: 13 ; ????
8B8F: 78              SEI                         
8B90: C6 FC           DEC     $FC                 
8B92: E0 FC           CPX     #$FC                
8B94: F6 EF           INC     $EF,X               
8B96: C0 80           CPY     #$80                
8B98: 38              SEC                         
8B99: 00              BRK                         
8B9A: C0 E8           CPY     #$E8                
8B9C: E4 CF           CPX     $CF                 
8B9E: 80 ; ????
8B9F: 00              BRK                         
8BA0: 00              BRK                         
8BA1: 03 ; ????
8BA2: 0C ; ????
8BA3: 19 38 3C        ORA     $3C38,Y             
8BA6: 7F ; ????
8BA7: 7F ; ????
8BA8: 00              BRK                         
8BA9: 03 ; ????
8BAA: 0F ; ????
8BAB: 1F ; ????
8BAC: 3F ; ????
8BAD: 3B ; ????
8BAE: 7C ; ????
8BAF: 7F ; ????
8BB0: 00              BRK                         
8BB1: 00              BRK                         
8BB2: 00              BRK                         
8BB3: 00              BRK                         
8BB4: 00              BRK                         
8BB5: 00              BRK                         
8BB6: 00              BRK                         
8BB7: 00              BRK                         
8BB8: 00              BRK                         
8BB9: 00              BRK                         
8BBA: 00              BRK                         
8BBB: 00              BRK                         
8BBC: 00              BRK                         
8BBD: 00              BRK                         
8BBE: 00              BRK                         
8BBF: 00              BRK                         
8BC0: 00              BRK                         
8BC1: 00              BRK                         
8BC2: 00              BRK                         
8BC3: 00              BRK                         
8BC4: 00              BRK                         
8BC5: 00              BRK                         
8BC6: 00              BRK                         
8BC7: 00              BRK                         
8BC8: 00              BRK                         
8BC9: 00              BRK                         
8BCA: 00              BRK                         
8BCB: 00              BRK                         
8BCC: 00              BRK                         
8BCD: 00              BRK                         
8BCE: 00              BRK                         
8BCF: 00              BRK                         
8BD0: 00              BRK                         
8BD1: 00              BRK                         
8BD2: 00              BRK                         
8BD3: 00              BRK                         
8BD4: 00              BRK                         
8BD5: 00              BRK                         
8BD6: 00              BRK                         
8BD7: 00              BRK                         
8BD8: 00              BRK                         
8BD9: 00              BRK                         
8BDA: 00              BRK                         
8BDB: 00              BRK                         
8BDC: 00              BRK                         
8BDD: 00              BRK                         
8BDE: 00              BRK                         
8BDF: 00              BRK                         
8BE0: 00              BRK                         
8BE1: 00              BRK                         
8BE2: 00              BRK                         
8BE3: 00              BRK                         
8BE4: 00              BRK                         
8BE5: 00              BRK                         
8BE6: 00              BRK                         
8BE7: 00              BRK                         
8BE8: 00              BRK                         
8BE9: 00              BRK                         
8BEA: 00              BRK                         
8BEB: 00              BRK                         
8BEC: 00              BRK                         
8BED: 00              BRK                         
8BEE: 00              BRK                         
8BEF: 00              BRK                         
8BF0: 00              BRK                         
8BF1: 00              BRK                         
8BF2: 00              BRK                         
8BF3: 00              BRK                         
8BF4: 00              BRK                         
8BF5: 00              BRK                         
8BF6: 00              BRK                         
8BF7: 00              BRK                         
8BF8: 00              BRK                         
8BF9: 00              BRK                         
8BFA: 00              BRK                         
8BFB: 00              BRK                         
8BFC: 00              BRK                         
8BFD: 00              BRK                         
8BFE: 00              BRK                         
8BFF: 00              BRK                         
8C00: 00              BRK                         
8C01: 1F ; ????
8C02: 3F ; ????
8C03: 3F ; ????
8C04: 3F ; ????
8C05: 3F ; ????
8C06: 00              BRK                         
8C07: 00              BRK                         
8C08: 7F ; ????
8C09: E0 CF           CPX     #$CF                
8C0B: DF ; ????
8C0C: DF ; ????
8C0D: DF ; ????
8C0E: 7F ; ????
8C0F: 00              BRK                         
8C10: 00              BRK                         
8C11: F8              SED                         
8C12: F8              SED                         
8C13: F8              SED                         
8C14: F8              SED                         
8C15: F0 00           BEQ     $8C17               ; {}
8C17: 00              BRK                         
8C18: F0 00           BEQ     $8C1A               ; {}
8C1A: FC ; ????
8C1B: FC ; ????
8C1C: FC ; ????
8C1D: FC ; ????
8C1E: F0 00           BEQ     $8C20               ; {}
8C20: 00              BRK                         
8C21: F8              SED                         
8C22: F8              SED                         
8C23: F8              SED                         
8C24: F8              SED                         
8C25: F0 00           BEQ     $8C27               ; {}
8C27: 00              BRK                         
8C28: F0 00           BEQ     $8C2A               ; {}
8C2A: FC ; ????
8C2B: FC ; ????
8C2C: FC ; ????
8C2D: FC ; ????
8C2E: F0 00           BEQ     $8C30               ; {}
8C30: 00              BRK                         
8C31: 1F ; ????
8C32: 3F ; ????
8C33: 3F ; ????
8C34: 3F ; ????
8C35: 3F ; ????
8C36: 00              BRK                         
8C37: 00              BRK                         
8C38: 7F ; ????
8C39: E0 CF           CPX     #$CF                
8C3B: DF ; ????
8C3C: DF ; ????
8C3D: DF ; ????
8C3E: 7F ; ????
8C3F: 00              BRK                         
8C40: 00              BRK                         
8C41: 00              BRK                         
8C42: 40              RTI                         
8C43: 20 38 4C        JSR     $4C38               
8C46: 84 21           STY     $21                 
8C48: 00              BRK                         
8C49: 00              BRK                         
8C4A: 00              BRK                         
8C4B: 00              BRK                         
8C4C: 00              BRK                         
8C4D: 30 68           BMI     $8CB7               ; {}
8C4F: 0C ; ????
8C50: 00              BRK                         
8C51: 00              BRK                         
8C52: 00              BRK                         
8C53: 40              RTI                         
8C54: 60              RTS                         
8C55: 3F ; ????
8C56: E0 80           CPX     #$80                
8C58: 00              BRK                         
8C59: 00              BRK                         
8C5A: 00              BRK                         
8C5B: 00              BRK                         
8C5C: 00              BRK                         
8C5D: 00              BRK                         
8C5E: 1F ; ????
8C5F: 60              RTS                         
8C60: 00              BRK                         
8C61: 00              BRK                         
8C62: 00              BRK                         
8C63: 10 20           BPL     $8C85               ; {}
8C65: A4 7E           LDY     $7E                 
8C67: 08              PHP                         
8C68: 00              BRK                         
8C69: 00              BRK                         
8C6A: 00              BRK                         
8C6B: 00              BRK                         
8C6C: 00              BRK                         
8C6D: 40              RTI                         
8C6E: 80 ; ????
8C6F: F0 0F           BEQ     $8C80               ; {}
8C71: 03 ; ????
8C72: 39 7F 7F        AND     $7F7F,Y             
8C75: FF ; ????
8C76: 87 ; ????
8C77: 0F ; ????
8C78: 03 ; ????
8C79: 01 38           ORA     ($38,X)             
8C7B: 7E 7E 83        ROR     $837E,X             ; {}
8C7E: 01 0C           ORA     ($0C,X)             
8C80: 3C ; ????
8C81: 7E FE E7        ROR     $E7FE,X             
8C84: FD FE FF        SBC     $FFFE,X             
8C87: E1 3C           SBC     ($3C,X)             
8C89: 7E E2 C1        ROR     $C1E2,X             
8C8C: BC 7E 61        LDY     $617E,X             
8C8F: C0 90           CPY     #$90                
8C91: 04 ; ????
8C92: 14 ; ????
8C93: 8D 84 FC        STA     $FC84               
8C96: FE 83 F0        INC     $F083,X             
8C99: FD FF FF        SBC     $FFFF,X             
8C9C: FF ; ????
8C9D: FF ; ????
8C9E: FF ; ????
8C9F: FF ; ????
8CA0: 88              DEY                         
8CA1: 06 12           ASL     $12                 
8CA3: 03 ; ????
8CA4: 07 ; ????
8CA5: 4B ; ????
8CA6: 3B ; ????
8CA7: DF ; ????
8CA8: F8              SED                         
8CA9: FE FE FF        INC     $FFFE,X             
8CAC: FF ; ????
8CAD: FF ; ????
8CAE: FF ; ????
8CAF: FF ; ????
8CB0: 01 00           ORA     ($00,X)             ; {ram.GP_00}
8CB2: 92 ; ????
8CB3: 00              BRK                         
8CB4: 40              RTI                         
8CB5: 81 66           STA     ($66,X)             
8CB7: 3F ; ????
8CB8: FF ; ????
8CB9: FF ; ????
8CBA: FF ; ????
8CBB: FF ; ????
8CBC: FF ; ????
8CBD: FF ; ????
8CBE: 7F ; ????
8CBF: 3F ; ????
8CC0: F1 64           SBC     ($64),Y             
8CC2: 4D 41 83        EOR     $8341               ; {}
8CC5: 81 93           STA     ($93,X)             
8CC7: FC ; ????
8CC8: FF ; ????
8CC9: FF ; ????
8CCA: FF ; ????
8CCB: FF ; ????
8CCC: FF ; ????
8CCD: FF ; ????
8CCE: FF ; ????
8CCF: FC ; ????
8CD0: BD 9E DF        LDA     $DF9E,X             
8CD3: E7 ; ????
8CD4: F3 ; ????
8CD5: FB ; ????
8CD6: FB ; ????
8CD7: FB ; ????
8CD8: 7B ; ????
8CD9: 79 BC 9E        ADC     $9EBC,Y             ; {}
8CDC: CE C6 E7        DEC     $E7C6               
8CDF: E7 ; ????
8CE0: FF ; ????
8CE1: FB ; ????
8CE2: 7B ; ????
8CE3: 63 ; ????
8CE4: 77 ; ????
8CE5: BB ; ????
8CE6: FB ; ????
8CE7: BD E7 F7        LDA     $F7E7,X             
8CEA: E7 ; ????
8CEB: DF ; ????
8CEC: CF ; ????
8CED: 67 ; ????
8CEE: 37 ; ????
8CEF: 73 ; ????
8CF0: FB ; ????
8CF1: FB ; ????
8CF2: F7 ; ????
8CF3: F7 ; ????
8CF4: EF ; ????
8CF5: F3 ; ????
8CF6: FB ; ????
8CF7: FD F7 E6        SBC     $E6F7,X             
8CFA: CC 8C 9E        CPY     $9E8C               ; {}
8CFD: CF ; ????
8CFE: E7 ; ????
8CFF: F3 ; ????
8D00: BD FB 7B        LDA     $7BFB,X             
8D03: 7B ; ????
8D04: FB ; ????
8D05: BD BC 9F        LDA     $9FBC,X             ; {}
8D08: 73 ; ????
8D09: 67 ; ????
8D0A: E7 ; ????
8D0B: C7 ; ????
8D0C: 67 ; ????
8D0D: 73 ; ????
8D0E: 7B ; ????
8D0F: 78              SEI                         
8D10: 00              BRK                         
8D11: 00              BRK                         
8D12: 00              BRK                         
8D13: B5 FB           LDA     $FB,X               
8D15: DF ; ????
8D16: FD EF 00        SBC     $00EF,X             
8D19: 00              BRK                         
8D1A: 00              BRK                         
8D1B: 91 F1           STA     ($F1),Y             
8D1D: 5F ; ????
8D1E: ED EF B0        SBC     $B0EF               ; {}
8D21: F7 ; ????
8D22: F7 ; ????
8D23: FF ; ????
8D24: 23 ; ????
8D25: 7F ; ????
8D26: 7F ; ????
8D27: FF ; ????
8D28: DF ; ????
8D29: 99 18 FF        STA     $FF18,Y             
8D2C: FD B9 89        SBC     $89B9,X             ; {}
8D2F: FF ; ????
8D30: 7F ; ????
8D31: 7F ; ????
8D32: BF ; ????
8D33: FF ; ????
8D34: 7F ; ????
8D35: FF ; ????
8D36: 77 ; ????
8D37: FF ; ????
8D38: 6B ; ????
8D39: 5F ; ????
8D3A: 3F ; ????
8D3B: D7 ; ????
8D3C: 1B ; ????
8D3D: FE 77 DF        INC     $DF77,X             
8D40: FE FC FE        INC     $FEFC,X             
8D43: FF ; ????
8D44: FE FE FD        INC     $FDFE,X             
8D47: FE 3E FC        INC     $FC3E,X             
8D4A: FE EF FE        INC     $FEEF,X             
8D4D: FE FD FE        INC     $FEFD,X             
8D50: 90 04           BCC     $8D56               ; {}
8D52: 14 ; ????
8D53: 8D 84 FC        STA     $FC84               
8D56: FE 83 F0        INC     $F083,X             
8D59: FD FF FF        SBC     $FFFF,X             
8D5C: FF ; ????
8D5D: FF ; ????
8D5E: FF ; ????
8D5F: FF ; ????
8D60: 88              DEY                         
8D61: 06 12           ASL     $12                 
8D63: 03 ; ????
8D64: 07 ; ????
8D65: 4B ; ????
8D66: 3B ; ????
8D67: DF ; ????
8D68: F8              SED                         
8D69: FE FE FF        INC     $FFFE,X             
8D6C: FF ; ????
8D6D: FF ; ????
8D6E: FF ; ????
8D6F: FF ; ????
8D70: 0F ; ????
8D71: 3F ; ????
8D72: 7F ; ????
8D73: FF ; ????
8D74: FF ; ????
8D75: FE EA C0        INC     $C0EA,X             
8D78: 00              BRK                         
8D79: 00              BRK                         
8D7A: 01 21           ORA     ($21,X)             
8D7C: 6B ; ????
8D7D: 7F ; ????
8D7E: 7F ; ????
8D7F: FF ; ????
8D80: FF ; ????
8D81: FF ; ????
8D82: FF ; ????
8D83: FF ; ????
8D84: FF ; ????
8D85: F7 ; ????
8D86: 77 ; ????
8D87: 22 ; ????
8D88: 00              BRK                         
8D89: 00              BRK                         
8D8A: 08              PHP                         
8D8B: 4C DD FD        JMP     $FDDD               
8D8E: FF ; ????
8D8F: FF ; ????
8D90: F0 FC           BEQ     $8D8E               ; {}
8D92: FE FF FF        INC     $FFFF,X             
8D95: 7F ; ????
8D96: 2B ; ????
8D97: 02 ; ????
8D98: 00              BRK                         
8D99: 00              BRK                         
8D9A: 00              BRK                         
8D9B: D0 DA           BNE     $8D77               ; {}
8D9D: FE FE FE        INC     $FEFE,X             
8DA0: FF ; ????
8DA1: 81 BD           STA     ($BD,X)             
8DA3: A5 A5           LDA     $A5                 
8DA5: BD 81 FF        LDA     $FF81,X             
8DA8: 00              BRK                         
8DA9: 7F ; ????
8DAA: 43 ; ????
8DAB: 5F ; ????
8DAC: 5F ; ????
8DAD: 7F ; ????
8DAE: 7F ; ????
8DAF: FF ; ????
8DB0: 82 ; ????
8DB1: C6 5C           DEC     $5C                 
8DB3: 78              SEI                         
8DB4: 30 20           BMI     $8DD6               ; {}
8DB6: 20 00 7D        JSR     $7D00               
8DB9: 39 A3 87        AND     $87A3,Y             ; {}
8DBC: CF ; ????
8DBD: DF ; ????
8DBE: DF ; ????
8DBF: FF ; ????
8DC0: 07 ; ????
8DC1: 0C ; ????
8DC2: 3F ; ????
8DC3: 1C ; ????
8DC4: 38              SEC                         
8DC5: 7E E5 B0        ROR     $B0E5,X             ; {}
8DC8: 00              BRK                         
8DC9: 00              BRK                         
8DCA: 00              BRK                         
8DCB: 00              BRK                         
8DCC: 00              BRK                         
8DCD: 00              BRK                         
8DCE: 00              BRK                         
8DCF: 00              BRK                         
8DD0: 00              BRK                         
8DD1: 00              BRK                         
8DD2: 00              BRK                         
8DD3: 00              BRK                         
8DD4: 80 ; ????
8DD5: C0 20           CPY     #$20                
8DD7: 00              BRK                         
8DD8: 00              BRK                         
8DD9: 00              BRK                         
8DDA: 00              BRK                         
8DDB: 00              BRK                         
8DDC: 00              BRK                         
8DDD: 00              BRK                         
8DDE: 00              BRK                         
8DDF: 00              BRK                         
8DE0: 00              BRK                         
8DE1: 80 ; ????
8DE2: 00              BRK                         
8DE3: 00              BRK                         
8DE4: 40              RTI                         
8DE5: 10 10           BPL     $8DF7               ; {}
8DE7: 08              PHP                         
8DE8: 00              BRK                         
8DE9: 00              BRK                         
8DEA: 00              BRK                         
8DEB: 00              BRK                         
8DEC: 00              BRK                         
8DED: 00              BRK                         
8DEE: 00              BRK                         
8DEF: 00              BRK                         
8DF0: 14 ; ????
8DF1: 0F ; ????
8DF2: 07 ; ????
8DF3: 05 01           ORA     $01                 
8DF5: 01 00           ORA     ($00,X)             ; {ram.GP_00}
8DF7: 00              BRK                         
8DF8: 0B ; ????
8DF9: 00              BRK                         
8DFA: 00              BRK                         
8DFB: 00              BRK                         
8DFC: 00              BRK                         
8DFD: 00              BRK                         
8DFE: 00              BRK                         
8DFF: 00              BRK                         
8E00: 65 45           ADC     $45                 
8E02: C2 ; ????
8E03: A4 B6           LDY     $B6                 
8E05: 2D 27 01        AND     $0127               
8E08: 9A              TXS                         
8E09: BA              TSX                         
8E0A: 3D 5B 49        AND     $495B,X             
8E0D: 02 ; ????
8E0E: 00              BRK                         
8E0F: 00              BRK                         
8E10: 00              BRK                         
8E11: 42 ; ????
8E12: 44 ; ????
8E13: 54 ; ????
8E14: 84 00           STY     $00                 ; {ram.GP_00}
8E16: 00              BRK                         
8E17: 00              BRK                         
8E18: FF ; ????
8E19: BD BB A3        LDA     $A3BB,X             ; {}
8E1C: 70 E0           BVS     $8DFE               ; {}
8E1E: C0 80           CPY     #$80                
8E20: 10 60           BPL     $8E82               ; {}
8E22: 40              RTI                         
8E23: 00              BRK                         
8E24: 00              BRK                         
8E25: 00              BRK                         
8E26: 00              BRK                         
8E27: 00              BRK                         
8E28: EC 00 00        CPX     $0000               ; {ram.GP_00}
8E2B: 00              BRK                         
8E2C: 00              BRK                         
8E2D: 00              BRK                         
8E2E: 00              BRK                         
8E2F: 00              BRK                         
8E30: 00              BRK                         
8E31: 00              BRK                         
8E32: 00              BRK                         
8E33: 00              BRK                         
8E34: 00              BRK                         
8E35: 00              BRK                         
8E36: 00              BRK                         
8E37: 00              BRK                         
8E38: 10 10           BPL     $8E4A               ; {}
8E3A: 38              SEC                         
8E3B: FE 7C 38        INC     $387C,X             
8E3E: 6C 44 01        JMP     ($0144)             
8E41: 06 04           ASL     $04                 
8E43: 18              CLC                         
8E44: A0 0C           LDY     #$0C                
8E46: 04 ; ????
8E47: 02 ; ????
8E48: 00              BRK                         
8E49: 01 03           ORA     ($03,X)             
8E4B: 06 1C           ASL     $1C                 
8E4D: F2 ; ????
8E4E: 02 ; ????
8E4F: 01 00           ORA     ($00,X)             ; {ram.GP_00}
8E51: 02 ; ????
8E52: 22 ; ????
8E53: 14 ; ????
8E54: 01 08           ORA     ($08,X)             
8E56: 08              PHP                         
8E57: 10 C0           BPL     $8E19               ; {}
8E59: 80 ; ????
8E5A: 00              BRK                         
8E5B: 62 ; ????
8E5C: 3E 37 04        ROL     $0437,X             
8E5F: 00              BRK                         
8E60: 00              BRK                         
8E61: 00              BRK                         
8E62: 00              BRK                         
8E63: 40              RTI                         
8E64: 26 38           ROL     $38                 
8E66: F0 80           BEQ     $8DE8               ; {}
8E68: 00              BRK                         
8E69: 00              BRK                         
8E6A: 00              BRK                         
8E6B: 00              BRK                         
8E6C: 00              BRK                         
8E6D: 07 ; ????
8E6E: 0C ; ????
8E6F: 40              RTI                         
8E70: 00              BRK                         
8E71: 00              BRK                         
8E72: 00              BRK                         
8E73: 00              BRK                         
8E74: 00              BRK                         
8E75: 00              BRK                         
8E76: 00              BRK                         
8E77: 00              BRK                         
8E78: 00              BRK                         
8E79: 00              BRK                         
8E7A: 00              BRK                         
8E7B: 00              BRK                         
8E7C: 00              BRK                         
8E7D: 00              BRK                         
8E7E: 00              BRK                         
8E7F: 00              BRK                         
8E80: 00              BRK                         
8E81: 00              BRK                         
8E82: 00              BRK                         
8E83: 00              BRK                         
8E84: 00              BRK                         
8E85: 00              BRK                         
8E86: 00              BRK                         
8E87: 00              BRK                         
8E88: 00              BRK                         
8E89: 00              BRK                         
8E8A: 00              BRK                         
8E8B: 00              BRK                         
8E8C: 00              BRK                         
8E8D: 00              BRK                         
8E8E: 00              BRK                         
8E8F: 00              BRK                         
8E90: 00              BRK                         
8E91: 00              BRK                         
8E92: 00              BRK                         
8E93: 00              BRK                         
8E94: 00              BRK                         
8E95: 00              BRK                         
8E96: 00              BRK                         
8E97: 00              BRK                         
8E98: 00              BRK                         
8E99: 00              BRK                         
8E9A: 00              BRK                         
8E9B: 00              BRK                         
8E9C: 00              BRK                         
8E9D: 00              BRK                         
8E9E: 00              BRK                         
8E9F: 00              BRK                         
8EA0: 00              BRK                         
8EA1: 00              BRK                         
8EA2: 00              BRK                         
8EA3: 00              BRK                         
8EA4: 00              BRK                         
8EA5: 00              BRK                         
8EA6: 00              BRK                         
8EA7: 00              BRK                         
8EA8: 00              BRK                         
8EA9: 00              BRK                         
8EAA: 00              BRK                         
8EAB: 00              BRK                         
8EAC: 00              BRK                         
8EAD: 00              BRK                         
8EAE: 00              BRK                         
8EAF: 00              BRK                         
8EB0: 00              BRK                         
8EB1: 00              BRK                         
8EB2: 00              BRK                         
8EB3: 00              BRK                         
8EB4: 00              BRK                         
8EB5: 00              BRK                         
8EB6: 00              BRK                         
8EB7: 00              BRK                         
8EB8: 00              BRK                         
8EB9: 00              BRK                         
8EBA: 00              BRK                         
8EBB: 00              BRK                         
8EBC: 00              BRK                         
8EBD: 00              BRK                         
8EBE: 00              BRK                         
8EBF: 00              BRK                         
8EC0: 00              BRK                         
8EC1: 00              BRK                         
8EC2: 00              BRK                         
8EC3: 00              BRK                         
8EC4: 00              BRK                         
8EC5: 00              BRK                         
8EC6: 00              BRK                         
8EC7: 00              BRK                         
8EC8: 00              BRK                         
8EC9: 00              BRK                         
8ECA: 00              BRK                         
8ECB: 00              BRK                         
8ECC: 00              BRK                         
8ECD: 00              BRK                         
8ECE: 00              BRK                         
8ECF: 00              BRK                         
8ED0: 00              BRK                         
8ED1: 00              BRK                         
8ED2: 00              BRK                         
8ED3: 00              BRK                         
8ED4: 00              BRK                         
8ED5: 00              BRK                         
8ED6: 00              BRK                         
8ED7: 00              BRK                         
8ED8: 00              BRK                         
8ED9: 00              BRK                         
8EDA: 00              BRK                         
8EDB: 00              BRK                         
8EDC: 00              BRK                         
8EDD: 00              BRK                         
8EDE: 00              BRK                         
8EDF: 00              BRK                         
8EE0: 00              BRK                         
8EE1: 00              BRK                         
8EE2: 00              BRK                         
8EE3: 00              BRK                         
8EE4: 00              BRK                         
8EE5: 00              BRK                         
8EE6: 00              BRK                         
8EE7: 00              BRK                         
8EE8: 00              BRK                         
8EE9: 00              BRK                         
8EEA: 00              BRK                         
8EEB: 00              BRK                         
8EEC: 00              BRK                         
8EED: 00              BRK                         
8EEE: 00              BRK                         
8EEF: 00              BRK                         
8EF0: 00              BRK                         
8EF1: 00              BRK                         
8EF2: 00              BRK                         
8EF3: 00              BRK                         
8EF4: 00              BRK                         
8EF5: 00              BRK                         
8EF6: 00              BRK                         
8EF7: 00              BRK                         
8EF8: 00              BRK                         
8EF9: 00              BRK                         
8EFA: 00              BRK                         
8EFB: 00              BRK                         
8EFC: 00              BRK                         
8EFD: 00              BRK                         
8EFE: 00              BRK                         
8EFF: 00              BRK                         
8F00: 00              BRK                         
8F01: 00              BRK                         
8F02: 00              BRK                         
8F03: 00              BRK                         
8F04: 00              BRK                         
8F05: 00              BRK                         
8F06: 00              BRK                         
8F07: 00              BRK                         
8F08: 00              BRK                         
8F09: 00              BRK                         
8F0A: 00              BRK                         
8F0B: 00              BRK                         
8F0C: 00              BRK                         
8F0D: 00              BRK                         
8F0E: 00              BRK                         
8F0F: 00              BRK                         
8F10: 00              BRK                         
8F11: 00              BRK                         
8F12: 00              BRK                         
8F13: 00              BRK                         
8F14: 00              BRK                         
8F15: 00              BRK                         
8F16: 00              BRK                         
8F17: 00              BRK                         
8F18: 00              BRK                         
8F19: 00              BRK                         
8F1A: 00              BRK                         
8F1B: 00              BRK                         
8F1C: 00              BRK                         
8F1D: 00              BRK                         
8F1E: 00              BRK                         
8F1F: 00              BRK                         
8F20: 00              BRK                         
8F21: 00              BRK                         
8F22: 00              BRK                         
8F23: 00              BRK                         
8F24: 00              BRK                         
8F25: 00              BRK                         
8F26: 00              BRK                         
8F27: 00              BRK                         
8F28: 00              BRK                         
8F29: 00              BRK                         
8F2A: 00              BRK                         
8F2B: 00              BRK                         
8F2C: 00              BRK                         
8F2D: 00              BRK                         
8F2E: 00              BRK                         
8F2F: 00              BRK                         
8F30: 00              BRK                         
8F31: 00              BRK                         
8F32: 00              BRK                         
8F33: 00              BRK                         
8F34: 00              BRK                         
8F35: 00              BRK                         
8F36: 00              BRK                         
8F37: 00              BRK                         
8F38: 00              BRK                         
8F39: 00              BRK                         
8F3A: 00              BRK                         
8F3B: 00              BRK                         
8F3C: 00              BRK                         
8F3D: 00              BRK                         
8F3E: 00              BRK                         
8F3F: 00              BRK                         
8F40: 00              BRK                         
8F41: 00              BRK                         
8F42: 00              BRK                         
8F43: 00              BRK                         
8F44: 00              BRK                         
8F45: 00              BRK                         
8F46: 00              BRK                         
8F47: 00              BRK                         
8F48: 00              BRK                         
8F49: 00              BRK                         
8F4A: 00              BRK                         
8F4B: 00              BRK                         
8F4C: 00              BRK                         
8F4D: 00              BRK                         
8F4E: 00              BRK                         
8F4F: 00              BRK                         
8F50: 00              BRK                         
8F51: 00              BRK                         
8F52: 00              BRK                         
8F53: 00              BRK                         
8F54: 00              BRK                         
8F55: 00              BRK                         
8F56: 00              BRK                         
8F57: 00              BRK                         
8F58: 00              BRK                         
8F59: 00              BRK                         
8F5A: 00              BRK                         
8F5B: 00              BRK                         
8F5C: 00              BRK                         
8F5D: 00              BRK                         
8F5E: 00              BRK                         
8F5F: 00              BRK                         
8F60: 00              BRK                         
8F61: 00              BRK                         
8F62: 00              BRK                         
8F63: 00              BRK                         
8F64: 00              BRK                         
8F65: 00              BRK                         
8F66: 00              BRK                         
8F67: 00              BRK                         
8F68: 00              BRK                         
8F69: 00              BRK                         
8F6A: 00              BRK                         
8F6B: 00              BRK                         
8F6C: 00              BRK                         
8F6D: 00              BRK                         
8F6E: 00              BRK                         
8F6F: 00              BRK                         
8F70: 00              BRK                         
8F71: 00              BRK                         
8F72: 00              BRK                         
8F73: 00              BRK                         
8F74: 00              BRK                         
8F75: 00              BRK                         
8F76: 00              BRK                         
8F77: 00              BRK                         
8F78: 00              BRK                         
8F79: 00              BRK                         
8F7A: 00              BRK                         
8F7B: 00              BRK                         
8F7C: 00              BRK                         
8F7D: 00              BRK                         
8F7E: 00              BRK                         
8F7F: 00              BRK                         
8F80: 00              BRK                         
8F81: 00              BRK                         
8F82: 00              BRK                         
8F83: 00              BRK                         
8F84: 00              BRK                         
8F85: 00              BRK                         
8F86: 00              BRK                         
8F87: 00              BRK                         
8F88: 00              BRK                         
8F89: 00              BRK                         
8F8A: 00              BRK                         
8F8B: 00              BRK                         
8F8C: 00              BRK                         
8F8D: 00              BRK                         
8F8E: 00              BRK                         
8F8F: 00              BRK                         
8F90: 00              BRK                         
8F91: 00              BRK                         
8F92: 00              BRK                         
8F93: 00              BRK                         
8F94: 00              BRK                         
8F95: 00              BRK                         
8F96: 00              BRK                         
8F97: 00              BRK                         
8F98: 00              BRK                         
8F99: 00              BRK                         
8F9A: 00              BRK                         
8F9B: 00              BRK                         
8F9C: 00              BRK                         
8F9D: 00              BRK                         
8F9E: 00              BRK                         
8F9F: 00              BRK                         
8FA0: 00              BRK                         
8FA1: 00              BRK                         
8FA2: 00              BRK                         
8FA3: 00              BRK                         
8FA4: 00              BRK                         
8FA5: 00              BRK                         
8FA6: 00              BRK                         
8FA7: 00              BRK                         
8FA8: 00              BRK                         
8FA9: 00              BRK                         
8FAA: 00              BRK                         
8FAB: 00              BRK                         
8FAC: 00              BRK                         
8FAD: 00              BRK                         
8FAE: 00              BRK                         
8FAF: 00              BRK                         
8FB0: 00              BRK                         
8FB1: 00              BRK                         
8FB2: 00              BRK                         
8FB3: 00              BRK                         
8FB4: 00              BRK                         
8FB5: 00              BRK                         
8FB6: 00              BRK                         
8FB7: 00              BRK                         
8FB8: 00              BRK                         
8FB9: 00              BRK                         
8FBA: 00              BRK                         
8FBB: 00              BRK                         
8FBC: 00              BRK                         
8FBD: 00              BRK                         
8FBE: 00              BRK                         
8FBF: 00              BRK                         
8FC0: 00              BRK                         
8FC1: 00              BRK                         
8FC2: 00              BRK                         
8FC3: 00              BRK                         
8FC4: 00              BRK                         
8FC5: 00              BRK                         
8FC6: 00              BRK                         
8FC7: 00              BRK                         
8FC8: 00              BRK                         
8FC9: 00              BRK                         
8FCA: 00              BRK                         
8FCB: 00              BRK                         
8FCC: 00              BRK                         
8FCD: 00              BRK                         
8FCE: 00              BRK                         
8FCF: 00              BRK                         
8FD0: 00              BRK                         
8FD1: 00              BRK                         
8FD2: 00              BRK                         
8FD3: 00              BRK                         
8FD4: 00              BRK                         
8FD5: 00              BRK                         
8FD6: 00              BRK                         
8FD7: 00              BRK                         
8FD8: 00              BRK                         
8FD9: 00              BRK                         
8FDA: 00              BRK                         
8FDB: 00              BRK                         
8FDC: 00              BRK                         
8FDD: 00              BRK                         
8FDE: 00              BRK                         
8FDF: 00              BRK                         
8FE0: 00              BRK                         
8FE1: 00              BRK                         
8FE2: 00              BRK                         
8FE3: 00              BRK                         
8FE4: 00              BRK                         
8FE5: 00              BRK                         
8FE6: 00              BRK                         
8FE7: 00              BRK                         
8FE8: 00              BRK                         
8FE9: 00              BRK                         
8FEA: 00              BRK                         
8FEB: 00              BRK                         
8FEC: 00              BRK                         
8FED: 00              BRK                         
8FEE: 00              BRK                         
8FEF: 00              BRK                         
8FF0: 00              BRK                         
8FF1: 00              BRK                         
8FF2: 00              BRK                         
8FF3: 00              BRK                         
8FF4: 00              BRK                         
8FF5: 00              BRK                         
8FF6: 00              BRK                         
8FF7: 00              BRK                         
8FF8: 00              BRK                         
8FF9: 00              BRK                         
8FFA: 00              BRK                         
8FFB: 00              BRK                         
8FFC: 00              BRK                         
8FFD: 00              BRK                         
8FFE: 00              BRK                         
8FFF: 00              BRK                         
9000: 07 ; ????
9001: 0C ; ????
9002: 18              CLC                         
9003: 18              CLC                         
9004: 7F ; ????
9005: DF ; ????
9006: 99 79 00        STA     $0079,Y             
9009: 03 ; ????
900A: 07 ; ????
900B: 07 ; ????
900C: 00              BRK                         
900D: 20 66 06        JSR     $0666               
9010: E0 10           CPX     #$10                
9012: 28              PLP                         
9013: 08              PHP                         
9014: EA              NOP                         
9015: EB ; ????
9016: 89 ; ????
9017: 9E ; ????
9018: 00              BRK                         
9019: E0 F0           CPX     #$F0                
901B: F0 14           BEQ     $9031               ; {}
901D: 16 76           ASL     $76,X               
901F: 60              RTS                         
9020: 80 ; ????
9021: 87 ; ????
9022: CC F8 78        CPY     $78F8               
9025: 7F ; ????
9026: DF ; ????
9027: 99 80 80        STA     $8080,Y             ; {}
902A: C3 ; ????
902B: E7 ; ????
902C: 67 ; ????
902D: 00              BRK                         
902E: 20 66 02        JSR     $0266               
9031: E2 ; ????
9032: 16 2E           ASL     $2E,X               
9034: 0C ; ????
9035: EA              NOP                         
9036: EB ; ????
9037: 89 ; ????
9038: 02 ; ????
9039: 02 ; ????
903A: E6 F6           INC     $F6                 
903C: F4 ; ????
903D: 14 ; ????
903E: 16 76           ASL     $76,X               
9040: 9D 2F BF        STA     $BF2F,X             ; {}
9043: FB ; ????
9044: EE F2 9C        INC     $9CF2               ; {}
9047: 80 ; ????
9048: 62 ; ????
9049: D0 41           BNE     $908C               ; {}
904B: 84 D1           STY     $D1                 
904D: CC 80 80        CPY     $8080               ; {}
9050: B2 ; ????
9051: E9 FA           SBC     #$FA                
9053: DE 76 4E        DEC     $4E76,X             
9056: 3A ; ????
9057: 02 ; ????
9058: 4C 16 84        JMP     $8416               ; {}
905B: 22 ; ????
905C: 8A              TXA                         
905D: 36 02           ROL     $02,X               
905F: 02 ; ????
9060: 79 9D 2F        ADC     $2F9D,Y             
9063: BF ; ????
9064: FB ; ????
9065: 2E 32 1C        ROL     $1C32               
9068: 06 62           ASL     $62                 
906A: D0 41           BNE     $90AD               ; {}
906C: 04 ; ????
906D: 11 0C           ORA     ($0C),Y             
906F: 00              BRK                         
9070: 9E ; ????
9071: B0 E8           BCS     $905B               ; {}
9073: FA ; ????
9074: DE 74 4C        DEC     $4C74,X             
9077: 38              SEC                         
9078: 60              RTS                         
9079: 4C 16 84        JMP     $8416               ; {}
907C: 20 88 30        JSR     $3088               
907F: 00              BRK                         
9080: 3C ; ????
9081: 7E 7E 7E        ROR     $7E7E,X             
9084: 3C ; ????
9085: 18              CLC                         
9086: 18              CLC                         
9087: 0C ; ????
9088: 18              CLC                         
9089: 34 ; ????
908A: 24 18           BIT     $18                 
908C: 42 ; ????
908D: 52 ; ????
908E: D3 ; ????
908F: 89 ; ????
9090: 00              BRK                         
9091: 00              BRK                         
9092: 3C ; ????
9093: 7E 7E 7E        ROR     $7E7E,X             
9096: 3C ; ????
9097: 18              CLC                         
9098: 81 81           STA     ($81,X)             
909A: 99 B5 24        STA     $24B5,Y             
909D: 18              CLC                         
909E: 00              BRK                         
909F: 10 00           BPL     $90A1               ; {}
90A1: 00              BRK                         
90A2: 00              BRK                         
90A3: 00              BRK                         
90A4: 07 ; ????
90A5: 18              CLC                         
90A6: 20 40 00        JSR     $0040               
90A9: 00              BRK                         
90AA: 00              BRK                         
90AB: 00              BRK                         
90AC: 00              BRK                         
90AD: 07 ; ????
90AE: 1F ; ????
90AF: 3F ; ????
90B0: 0F ; ????
90B1: 70 43           BVS     $90F6               ; {}
90B3: 83 ; ????
90B4: 9C ; ????
90B5: 9C ; ????
90B6: E0 63           CPX     #$63                
90B8: 01 4F           ORA     ($4F,X)             
90BA: 3D 7C 6F        AND     $6F7C,X             
90BD: 63 ; ????
90BE: 5F ; ????
90BF: 1D 01 87        ORA     $8701,X             ; {}
90C2: D8              CLD                         
90C3: 61 43           ADC     ($43,X)             
90C5: 43 ; ????
90C6: 67 ; ????
90C7: 73 ; ????
90C8: 01 80           ORA     ($80,X)             
90CA: 47 ; ????
90CB: 5E 3D 3D        LSR     $3D3D,X             
90CE: 1B ; ????
90CF: 2D 79 5C        AND     $5C79               
90D2: 5C ; ????
90D3: 20 68 DC        JSR     $DC68               
90D6: 0E 0C 16        ASL     $160C               
90D9: 3B ; ????
90DA: 23 ; ????
90DB: 1F ; ????
90DC: 57 ; ????
90DD: 8B ; ????
90DE: 05 03           ORA     $03                 
90E0: 00              BRK                         
90E1: 40              RTI                         
90E2: 76 3A           ROR     $3A,X               
90E4: 12 ; ????
90E5: 23 ; ????
90E6: 3F ; ????
90E7: 07 ; ????
90E8: 00              BRK                         
90E9: 40              RTI                         
90EA: 31 15           AND     ($15),Y             
90EC: 0D 1C 01        ORA     $011C               
90EF: 3A ; ????
90F0: 1E 1C 1C        ASL     $1C1C,X             
90F3: 1C ; ????
90F4: 3E 3E 3D        ROL     $3D3E,X             
90F7: 38              SEC                         
90F8: 10 10           BPL     $910A               ; {}
90FA: 10 10           BPL     $910C               ; {}
90FC: 20 20 20        JSR     $2020               
90FF: 20 04 48        JSR     $4804               
9102: 4F ; ????
9103: A8              TAY                         
9104: 24 10           BIT     $10                 
9106: 18              CLC                         
9107: 1F ; ????
9108: 04 ; ????
9109: 48              PHA                         
910A: 08              PHP                         
910B: 47 ; ????
910C: CF ; ????
910D: 6F ; ????
910E: 07 ; ????
910F: 00              BRK                         
9110: 21 10           AND     ($10,X)             
9112: F0 F1           BEQ     $9105               ; {}
9114: 73 ; ????
9115: 7C ; ????
9116: FE BE 21        INC     $21BE,X             
9119: 10 10           BPL     $912B               ; {}
911B: 20 88 83        JSR     $8388               ; {}
911E: 00              BRK                         
911F: 41 80           EOR     ($80,X)             
9121: C0 B0           CPY     #$B0                
9123: 48              PHA                         
9124: 24 80           BIT     $80                 
9126: 00              BRK                         
9127: 00              BRK                         
9128: 80 ; ????
9129: 00              BRK                         
912A: 40              RTI                         
912B: B0 D8           BCS     $9105               ; {}
912D: 40              RTI                         
912E: 00              BRK                         
912F: 00              BRK                         
9130: 10 00           BPL     $9132               ; {}
9132: 08              PHP                         
9133: 0F ; ????
9134: 10 23           BPL     $9159               ; {}
9136: 01 03           ORA     ($03,X)             
9138: 17 ; ????
9139: 07 ; ????
913A: 07 ; ????
913B: 08              PHP                         
913C: 13 ; ????
913D: 20 00 02        JSR     $0200               
9140: B2 ; ????
9141: 6E ED 77        ROR     $77ED               
9144: FC ; ????
9145: B8              CLV                         
9146: 9C ; ????
9147: 38              SEC                         
9148: CD 91 12        CMP     $1291               
914B: 9C ; ????
914C: 02 ; ????
914D: 44 ; ????
914E: 42 ; ????
914F: A4 04           LDY     $04                 
9151: 08              PHP                         
9152: 0F ; ????
9153: 08              PHP                         
9154: 04 ; ????
9155: 70 98           BVS     $90EF               ; {}
9157: 1F ; ????
9158: 04 ; ????
9159: 08              PHP                         
915A: 08              PHP                         
915B: 07 ; ????
915C: 0F ; ????
915D: 4F ; ????
915E: 67 ; ????
915F: 00              BRK                         
9160: 20 10 D0        JSR     $D010               
9163: F0 71           BEQ     $91D6               ; {}
9165: 7E FC BE        ROR     $BEFC,X             ; {}
9168: 20 10 30        JSR     $3010               
916B: 20 88 81        JSR     $8188               ; {}
916E: 02 ; ????
916F: 41 00           EOR     ($00,X)             ; {ram.GP_00}
9171: 00              BRK                         
9172: 00              BRK                         
9173: 00              BRK                         
9174: F0 38           BEQ     $91AE               ; {}
9176: 06 00           ASL     $00                 ; {ram.GP_00}
9178: 00              BRK                         
9179: 00              BRK                         
917A: 00              BRK                         
917B: 00              BRK                         
917C: 30 C0           BMI     $913E               ; {}
917E: 78              SEI                         
917F: 00              BRK                         
9180: 00              BRK                         
9181: 80 ; ????
9182: C3 ; ????
9183: CF ; ????
9184: 7F ; ????
9185: 3F ; ????
9186: 1F ; ????
9187: 3F ; ????
9188: 00              BRK                         
9189: 04 ; ????
918A: 07 ; ????
918B: 0F ; ????
918C: 1A ; ????
918D: 18              CLC                         
918E: 1A ; ????
918F: 30 00           BMI     $9191               ; {}
9191: 02 ; ????
9192: 86 E6           STX     $E6                 
9194: FC ; ????
9195: F8              SED                         
9196: FE FF 00        INC     $00FF,X             
9199: 40              RTI                         
919A: C0 E0           CPY     #$E0                
919C: B0 30           BCS     $91CE               ; {}
919E: BE 19 00        LDX     $0019,Y             
91A1: 03 ; ????
91A2: 0F ; ????
91A3: 1F ; ????
91A4: 1F ; ????
91A5: 1F ; ????
91A6: 3F ; ????
91A7: 5F ; ????
91A8: 04 ; ????
91A9: 07 ; ????
91AA: 0F ; ????
91AB: 1A ; ????
91AC: 18              CLC                         
91AD: 1A ; ????
91AE: 30 3A           BMI     $91EA               ; {}
91B0: 00              BRK                         
91B1: 80 ; ????
91B2: E0 F0           CPX     #$F0                
91B4: F0 FE           BEQ     $91B4               ; {}
91B6: FF ; ????
91B7: FF ; ????
91B8: 40              RTI                         
91B9: C0 E0           CPY     #$E0                
91BB: B0 30           BCS     $91ED               ; {}
91BD: BE 19 BC        LDX     $BC19,Y             ; {}
91C0: 1F ; ????
91C1: 0F ; ????
91C2: 3C ; ????
91C3: 7F ; ????
91C4: 7A ; ????
91C5: 38              SEC                         
91C6: 0B ; ????
91C7: 0E 3A 7F        ASL     $7F3A               
91CA: 7B ; ????
91CB: 4F ; ????
91CC: 4F ; ????
91CD: 3F ; ????
91CE: 1F ; ????
91CF: 08              PHP                         
91D0: FF ; ????
91D1: FF ; ????
91D2: 7F ; ????
91D3: FF ; ????
91D4: F7 ; ????
91D5: 34 ; ????
91D6: A8              TAY                         
91D7: 70 BC           BVS     $9195               ; {}
91D9: E4 A4           CPX     $A4                 
91DB: FC ; ????
91DC: CD FC F8        CMP     $F8FC               
91DF: 10 8F           BPL     $9170               ; {}
91E1: BC FF FA        LDY     $FAFF,X             
91E4: F8              SED                         
91E5: 8B ; ????
91E6: 8E 00 7F        STX     $7F00               
91E9: 7B ; ????
91EA: 4F ; ????
91EB: 4F ; ????
91EC: 3F ; ????
91ED: 1F ; ????
91EE: 08              PHP                         
91EF: 00              BRK                         
91F0: FF ; ????
91F1: 7F ; ????
91F2: FF ; ????
91F3: F7 ; ????
91F4: 36 AA           ROL     $AA,X               
91F6: 72 ; ????
91F7: 00              BRK                         
91F8: E4 A4           CPX     $A4                 
91FA: FC ; ????
91FB: CD FE F8        CMP     $F8FE               
91FE: 10 00           BPL     $9200               ; {}
9200: 00              BRK                         
9201: 08              PHP                         
9202: 60              RTS                         
9203: 71 7B           ADC     ($7B),Y             
9205: 7B ; ????
9206: 7B ; ????
9207: 31 0F           AND     ($0F),Y             
9209: 3F ; ????
920A: 1F ; ????
920B: 4E 44 55        LSR     $5544               
920E: 35 4E           AND     $4E,X               
9210: 20 78 F4        JSR     $F478               
9213: FC ; ????
9214: FA ; ????
9215: FA ; ????
9216: FA ; ????
9217: F2 ; ????
9218: C0 80           CPY     #$80                
921A: 28              PLP                         
921B: 70 74           BVS     $9291               ; {}
921D: 74 ; ????
921E: E4 0C           CPX     $0C                 
9220: 7F ; ????
9221: 7F ; ????
9222: 7F ; ????
9223: 3F ; ????
9224: 12 ; ????
9225: 27 ; ????
9226: 4A              LSR     A                   
9227: 48              PHA                         
9228: 3F ; ????
9229: 40              RTI                         
922A: 3F ; ????
922B: 00              BRK                         
922C: 6D 48 90        ADC     $9048               ; {}
922F: 92 ; ????
9230: F2 ; ????
9231: FE F4 EE        INC     $EEF4,X             
9234: 30 C9           BMI     $91FF               ; {}
9236: 44 ; ????
9237: 04 ; ????
9238: EC 30 E8        CPX     $E830               
923B: 10 C6           BPL     $9203               ; {}
923D: 12 ; ????
923E: 09 49           ORA     #$49                
9240: 00              BRK                         
9241: 75 7B           ADC     $7B,X               
9243: 7B ; ????
9244: 7B ; ????
9245: 73 ; ????
9246: 3F ; ????
9247: 3F ; ????
9248: 00              BRK                         
9249: 0E 24 55        ASL     $5524               
924C: 55 2C           EOR     $2C,X               
924E: 5F ; ????
924F: 60              RTS                         
9250: 00              BRK                         
9251: F8              SED                         
9252: F8              SED                         
9253: FC ; ????
9254: FC ; ????
9255: FE F6 E2        INC     $E2F6,X             
9258: 00              BRK                         
9259: 00              BRK                         
925A: E0 70           CPX     #$70                
925C: 70 E0           BVS     $923E               ; {}
925E: 08              PHP                         
925F: DC ; ????
9260: 7F ; ????
9261: 7A ; ????
9262: 74 ; ????
9263: 70 7F           BVS     $92E4               ; {}
9265: 7F ; ????
9266: 9F ; ????
9267: 92 ; ????
9268: 40              RTI                         
9269: 45 4B           EOR     $4B                 
926B: 4F ; ????
926C: A0 9F           LDY     #$9F                
926E: 20 64 F2        JSR     $F264               
9271: F2 ; ????
9272: 74 ; ????
9273: F2 ; ????
9274: E9 E4           SBC     #$E4                
9276: E4 12           CPX     $12                 
9278: 2C 2C A8        BIT     $A82C               ; {}
927B: 2C 56 99        BIT     $9956               ; {}
927E: 09 25           ORA     #$25                
9280: 01 01           ORA     ($01,X)             
9282: 03 ; ????
9283: 02 ; ????
9284: 03 ; ????
9285: 01 1B           ORA     ($1B,X)             
9287: 2F ; ????
9288: 01 01           ORA     ($01,X)             
928A: 01 09           ORA     ($09,X)             
928C: 1C ; ????
928D: 0E 05 32        ASL     $3205               
9290: 00              BRK                         
9291: 00              BRK                         
9292: 80 ; ????
9293: 40              RTI                         
9294: C0 80           CPY     #$80                
9296: DC ; ????
9297: F7 ; ????
9298: 00              BRK                         
9299: 00              BRK                         
929A: 80 ; ????
929B: 90 38           BCC     $92D5               ; {}
929D: 70 A0           BVS     $923F               ; {}
929F: 4F ; ????
92A0: 00              BRK                         
92A1: 07 ; ????
92A2: 18              CLC                         
92A3: 22 ; ????
92A4: 24 74           BIT     $74                 
92A6: 50 80           BVC     $9228               ; {}
92A8: 00              BRK                         
92A9: 07 ; ????
92AA: 18              CLC                         
92AB: 21 23           AND     ($23,X)             
92AD: 41 4C           EOR     ($4C,X)             
92AF: 9E ; ????
92B0: 03 ; ????
92B1: 0C ; ????
92B2: 10 26           BPL     $92DA               ; {}
92B4: 34 ; ????
92B5: 54 ; ????
92B6: 54 ; ????
92B7: 40              RTI                         
92B8: 03 ; ????
92B9: 0D 13 21        ORA     $2113               
92BC: 20 40 40        JSR     $4040               
92BF: 58              CLI                         
92C0: 82 ; ????
92C1: 73 ; ????
92C2: 30 2F           BMI     $92F3               ; {}
92C4: 42 ; ????
92C5: 44 ; ????
92C6: 04 ; ????
92C7: 00              BRK                         
92C8: 8C 40 70        STY     $7040               
92CB: CF ; ????
92CC: 8C 88 08        STY     $0888               
92CF: 00              BRK                         
92D0: 40              RTI                         
92D1: 23 ; ????
92D2: 1C ; ????
92D3: 13 ; ????
92D4: 0A              ASL     A                   
92D5: 05 00           ORA     $00                 ; {ram.GP_00}
92D7: 00              BRK                         
92D8: 7C ; ????
92D9: 38              SEC                         
92DA: 3C ; ????
92DB: 27 ; ????
92DC: 14 ; ????
92DD: 0A              ASL     A                   
92DE: 00              BRK                         
92DF: 00              BRK                         
92E0: 00              BRK                         
92E1: 07 ; ????
92E2: 0F ; ????
92E3: 1F ; ????
92E4: 1F ; ????
92E5: 78              SEI                         
92E6: EF ; ????
92E7: EF ; ????
92E8: 00              BRK                         
92E9: 00              BRK                         
92EA: 07 ; ????
92EB: 0E 00 27        ASL     $2700               
92EE: 50 50           BVC     $9340               ; {}
92F0: 00              BRK                         
92F1: E0 F0           CPX     #$F0                
92F3: F8              SED                         
92F4: FC ; ????
92F5: F6 F7           INC     $F7,X               
92F7: FF ; ????
92F8: 00              BRK                         
92F9: 00              BRK                         
92FA: 80 ; ????
92FB: 80 ; ????
92FC: 40              RTI                         
92FD: 4C 0E 06        JMP     $060E               
9300: F7 ; ????
9301: 7B ; ????
9302: 7C ; ????
9303: 78              SEI                         
9304: 3F ; ????
9305: 0E 1E 3F        ASL     $3F1E               
9308: 68              PLA                         
9309: 04 ; ????
930A: 7B ; ????
930B: 37 ; ????
930C: 00              BRK                         
930D: 0C ; ????
930E: 04 ; ????
930F: 3A ; ????
9310: EF ; ????
9311: DE 3E 1E        DEC     $1E3E,X             
9314: FC ; ????
9315: FC ; ????
9316: 00              BRK                         
9317: 00              BRK                         
9318: 16 20           ASL     $20,X               
931A: DE EC 20        DEC     $20EC,X             
931D: 5C ; ????
931E: 00              BRK                         
931F: 00              BRK                         
9320: 07 ; ????
9321: 18              CLC                         
9322: 20 4C 4C        JSR     $4C4C               
9325: 80 ; ????
9326: 90 80           BCC     $92A8               ; {}
9328: 00              BRK                         
9329: 07 ; ????
932A: 1F ; ????
932B: 33 ; ????
932C: 33 ; ????
932D: 7F ; ????
932E: 6F ; ????
932F: 7F ; ????
9330: E0 18           CPX     #$18                
9332: 04 ; ????
9333: 02 ; ????
9334: 02 ; ????
9335: 01 01           ORA     ($01,X)             
9337: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9339: C0 E0           CPY     #$E0                
933B: F0 F0           BEQ     $932D               ; {}
933D: F0 E0           BEQ     $931F               ; {}
933F: E0 80           CPX     #$80                
9341: 80 ; ????
9342: 80 ; ????
9343: 40              RTI                         
9344: 40              RTI                         
9345: 20 18 07        JSR     $0718               
9348: 7F ; ????
9349: 7F ; ????
934A: 3E 00 00        ROL     $0000,X             ; {ram.GP_00}
934D: 00              BRK                         
934E: 00              BRK                         
934F: 00              BRK                         
9350: 01 01           ORA     ($01,X)             
9352: 01 02           ORA     ($02,X)             
9354: 02 ; ????
9355: 04 ; ????
9356: 18              CLC                         
9357: E0 C0           CPX     #$C0                
9359: 80 ; ????
935A: 00              BRK                         
935B: 00              BRK                         
935C: 00              BRK                         
935D: 00              BRK                         
935E: 00              BRK                         
935F: 00              BRK                         
9360: 00              BRK                         
9361: 00              BRK                         
9362: 00              BRK                         
9363: 00              BRK                         
9364: 03 ; ????
9365: 07 ; ????
9366: 0F ; ????
9367: 0E 00 00        ASL     $0000               ; {ram.GP_00}
936A: 00              BRK                         
936B: 00              BRK                         
936C: 03 ; ????
936D: 04 ; ????
936E: 08              PHP                         
936F: 08              PHP                         
9370: 01 03           ORA     ($03,X)             
9372: 0E FE FC        ASL     $FCFE               
9375: F0 80           BEQ     $92F7               ; {}
9377: 00              BRK                         
9378: 01 02           ORA     ($02,X)             
937A: 0C ; ????
937B: F0 00           BEQ     $937D               ; {}
937D: 00              BRK                         
937E: 00              BRK                         
937F: 00              BRK                         
9380: 00              BRK                         
9381: 00              BRK                         
9382: 00              BRK                         
9383: 00              BRK                         
9384: 00              BRK                         
9385: 00              BRK                         
9386: 00              BRK                         
9387: 00              BRK                         
9388: 00              BRK                         
9389: 00              BRK                         
938A: 00              BRK                         
938B: 00              BRK                         
938C: 00              BRK                         
938D: 00              BRK                         
938E: 00              BRK                         
938F: 00              BRK                         
9390: 00              BRK                         
9391: 00              BRK                         
9392: 00              BRK                         
9393: 00              BRK                         
9394: 00              BRK                         
9395: 00              BRK                         
9396: 00              BRK                         
9397: 00              BRK                         
9398: 00              BRK                         
9399: 00              BRK                         
939A: 00              BRK                         
939B: 00              BRK                         
939C: 00              BRK                         
939D: 00              BRK                         
939E: 00              BRK                         
939F: 00              BRK                         
93A0: 00              BRK                         
93A1: 00              BRK                         
93A2: 00              BRK                         
93A3: 00              BRK                         
93A4: 00              BRK                         
93A5: 00              BRK                         
93A6: 00              BRK                         
93A7: 00              BRK                         
93A8: 00              BRK                         
93A9: 00              BRK                         
93AA: 00              BRK                         
93AB: 00              BRK                         
93AC: 00              BRK                         
93AD: 00              BRK                         
93AE: 00              BRK                         
93AF: 00              BRK                         
93B0: 00              BRK                         
93B1: 00              BRK                         
93B2: 00              BRK                         
93B3: 00              BRK                         
93B4: 00              BRK                         
93B5: 00              BRK                         
93B6: 00              BRK                         
93B7: 00              BRK                         
93B8: 00              BRK                         
93B9: 00              BRK                         
93BA: 00              BRK                         
93BB: 00              BRK                         
93BC: 00              BRK                         
93BD: 00              BRK                         
93BE: 00              BRK                         
93BF: 00              BRK                         
93C0: 00              BRK                         
93C1: 00              BRK                         
93C2: 00              BRK                         
93C3: 00              BRK                         
93C4: 00              BRK                         
93C5: 00              BRK                         
93C6: 00              BRK                         
93C7: 00              BRK                         
93C8: 00              BRK                         
93C9: 00              BRK                         
93CA: 00              BRK                         
93CB: 00              BRK                         
93CC: 00              BRK                         
93CD: 00              BRK                         
93CE: 00              BRK                         
93CF: 00              BRK                         
93D0: 00              BRK                         
93D1: 00              BRK                         
93D2: 00              BRK                         
93D3: 00              BRK                         
93D4: 00              BRK                         
93D5: 00              BRK                         
93D6: 00              BRK                         
93D7: 00              BRK                         
93D8: 00              BRK                         
93D9: 00              BRK                         
93DA: 00              BRK                         
93DB: 00              BRK                         
93DC: 00              BRK                         
93DD: 00              BRK                         
93DE: 00              BRK                         
93DF: 00              BRK                         
93E0: 00              BRK                         
93E1: 00              BRK                         
93E2: 00              BRK                         
93E3: 00              BRK                         
93E4: 00              BRK                         
93E5: 00              BRK                         
93E6: 00              BRK                         
93E7: 00              BRK                         
93E8: 00              BRK                         
93E9: 00              BRK                         
93EA: 00              BRK                         
93EB: 00              BRK                         
93EC: 00              BRK                         
93ED: 00              BRK                         
93EE: 00              BRK                         
93EF: 00              BRK                         
93F0: 00              BRK                         
93F1: 00              BRK                         
93F2: 00              BRK                         
93F3: 00              BRK                         
93F4: 00              BRK                         
93F5: 00              BRK                         
93F6: 00              BRK                         
93F7: 00              BRK                         
93F8: 00              BRK                         
93F9: 00              BRK                         
93FA: 00              BRK                         
93FB: 00              BRK                         
93FC: 00              BRK                         
93FD: 00              BRK                         
93FE: 00              BRK                         
93FF: 00              BRK                         
9400: 04 ; ????
9401: 18              CLC                         
9402: 20 20 40        JSR     $4020               
9405: C0 80           CPY     #$80                
9407: 3F ; ????
9408: 3C ; ????
9409: 79 E3 A7        ADC     $A7E3,Y             ; {}
940C: CD DF 97        CMP     $97DF               ; {}
940F: 3F ; ????
9410: 04 ; ????
9411: 86 C3           STX     $C3                 
9413: 71 11           ADC     ($11),Y             
9415: 09 09           ORA     #$09                
9417: 6C 34 9E        JMP     ($9E34)             ; {}
941A: C7 ; ????
941B: 75 F3           ADC     $F3,X               
941D: AB ; ????
941E: F9 6C 00        SBC     $006C,Y             
9421: 00              BRK                         
9422: 00              BRK                         
9423: 00              BRK                         
9424: 40              RTI                         
9425: 40              RTI                         
9426: 20 01 00        JSR     $0001               
9429: 3B ; ????
942A: BF ; ????
942B: 96 5F           STX     $5F,Y               
942D: C7 ; ????
942E: 67 ; ????
942F: 31 00           AND     ($00),Y             ; {ram.GP_00}
9431: 04 ; ????
9432: 1D 12 14        ORA     $1412,X             
9435: E0 08           CPX     #$08                
9437: B0 00           BCS     $9439               ; {}
9439: DC ; ????
943A: FD F3 D7        SBC     $D7F3,X             
943D: E2 ; ????
943E: 0E BA FF        ASL     $FFBA               
9441: FF ; ????
9442: 7F ; ????
9443: 7F ; ????
9444: 3F ; ????
9445: 3F ; ????
9446: 1F ; ????
9447: 07 ; ????
9448: 00              BRK                         
9449: 00              BRK                         
944A: 00              BRK                         
944B: 60              RTS                         
944C: 20 30 1C        JSR     $1C30               
944F: 07 ; ????
9450: FF ; ????
9451: FF ; ????
9452: FF ; ????
9453: FF ; ????
9454: FF ; ????
9455: FF ; ????
9456: EF ; ????
9457: C7 ; ????
9458: 00              BRK                         
9459: 10 08           BPL     $9463               ; {}
945B: 08              PHP                         
945C: 18              CLC                         
945D: 30 EC           BMI     $944B               ; {}
945F: C7 ; ????
9460: FF ; ????
9461: FF ; ????
9462: FF ; ????
9463: FF ; ????
9464: FF ; ????
9465: C3 ; ????
9466: 81 00           STA     ($00,X)             ; {ram.GP_00}
9468: 00              BRK                         
9469: 30 18           BMI     $9483               ; {}
946B: 18              CLC                         
946C: 7E C3 81        ROR     $81C3,X             ; {}
946F: 00              BRK                         
9470: FF ; ????
9471: FF ; ????
9472: FF ; ????
9473: FE FC F8        INC     $F8FC,X             
9476: E0 00           CPX     #$00                
9478: 08              PHP                         
9479: 05 07           ORA     $07                 
947B: 0E 1C F8        ASL     $F81C               
947E: E0 00           CPX     #$00                
9480: 00              BRK                         
9481: 00              BRK                         
9482: 0C ; ????
9483: 10 7F           BPL     $9504               ; {}
9485: 3F ; ????
9486: 0E 00 3F        ASL     $3F00               
9489: 60              RTS                         
948A: C0 80           CPY     #$80                
948C: FF ; ????
948D: FF ; ????
948E: 7F ; ????
948F: 1F ; ????
9490: 00              BRK                         
9491: 00              BRK                         
9492: 00              BRK                         
9493: 00              BRK                         
9494: 83 ; ????
9495: 04 ; ????
9496: 00              BRK                         
9497: 00              BRK                         
9498: F3 ; ????
9499: 1B ; ????
949A: 16 2C           ASL     $2C,X               
949C: D8              CLD                         
949D: B0 A0           BCS     $943F               ; {}
949F: 60              RTS                         
94A0: 00              BRK                         
94A1: 00              BRK                         
94A2: 03 ; ????
94A3: 04 ; ????
94A4: 03 ; ????
94A5: 01 00           ORA     ($00,X)             ; {ram.GP_00}
94A7: 00              BRK                         
94A8: 9F ; ????
94A9: B0 D0           BCS     $947B               ; {}
94AB: 68              PLA                         
94AC: 37 ; ????
94AD: 1B ; ????
94AE: 0B ; ????
94AF: 0D 00 00        ORA     $0000               ; {ram.GP_00}
94B2: 00              BRK                         
94B3: 00              BRK                         
94B4: FC ; ????
94B5: F8              SED                         
94B6: E0 00           CPX     #$00                
94B8: F0 1C           BEQ     $94D6               ; {}
94BA: 06 02           ASL     $02                 
94BC: FE FE FC        INC     $FCFE,X             
94BF: F0 00           BEQ     $94C1               ; {}
94C1: 00              BRK                         
94C2: 00              BRK                         
94C3: 00              BRK                         
94C4: 00              BRK                         
94C5: 00              BRK                         
94C6: 00              BRK                         
94C7: 00              BRK                         
94C8: 0E 00 00        ASL     $0000               ; {ram.GP_00}
94CB: 00              BRK                         
94CC: 00              BRK                         
94CD: 00              BRK                         
94CE: 00              BRK                         
94CF: 00              BRK                         
94D0: 3F ; ????
94D1: 3F ; ????
94D2: 1F ; ????
94D3: 00              BRK                         
94D4: 00              BRK                         
94D5: 00              BRK                         
94D6: 00              BRK                         
94D7: 00              BRK                         
94D8: 7F ; ????
94D9: FF ; ????
94DA: FF ; ????
94DB: 7F ; ????
94DC: 1F ; ????
94DD: 00              BRK                         
94DE: 00              BRK                         
94DF: 00              BRK                         
94E0: F8              SED                         
94E1: F8              SED                         
94E2: F0 00           BEQ     $94E4               ; {}
94E4: 00              BRK                         
94E5: 00              BRK                         
94E6: 00              BRK                         
94E7: 00              BRK                         
94E8: FC ; ????
94E9: FE FE FC        INC     $FCFE,X             
94EC: F0 00           BEQ     $94EE               ; {}
94EE: 00              BRK                         
94EF: 00              BRK                         
94F0: 00              BRK                         
94F1: 00              BRK                         
94F2: 00              BRK                         
94F3: 00              BRK                         
94F4: 00              BRK                         
94F5: 00              BRK                         
94F6: 00              BRK                         
94F7: 00              BRK                         
94F8: E0 00           CPX     #$00                
94FA: 00              BRK                         
94FB: 00              BRK                         
94FC: 00              BRK                         
94FD: 00              BRK                         
94FE: 00              BRK                         
94FF: 00              BRK                         
9500: 06 1F           ASL     $1F                 
9502: 3F ; ????
9503: 7F ; ????
9504: 7F ; ????
9505: FF ; ????
9506: FF ; ????
9507: FF ; ????
9508: 00              BRK                         
9509: 00              BRK                         
950A: 00              BRK                         
950B: 00              BRK                         
950C: 00              BRK                         
950D: 00              BRK                         
950E: 00              BRK                         
950F: 00              BRK                         
9510: 3C ; ????
9511: 7F ; ????
9512: FF ; ????
9513: FF ; ????
9514: FF ; ????
9515: FF ; ????
9516: FF ; ????
9517: FF ; ????
9518: 00              BRK                         
9519: 00              BRK                         
951A: 00              BRK                         
951B: 00              BRK                         
951C: 00              BRK                         
951D: 00              BRK                         
951E: 00              BRK                         
951F: 00              BRK                         
9520: 00              BRK                         
9521: 01 1D           ORA     ($1D,X)             
9523: BF ; ????
9524: FF ; ????
9525: FF ; ????
9526: FF ; ????
9527: FF ; ????
9528: 00              BRK                         
9529: 00              BRK                         
952A: 00              BRK                         
952B: 00              BRK                         
952C: 00              BRK                         
952D: 00              BRK                         
952E: 00              BRK                         
952F: 00              BRK                         
9530: F0 FC           BEQ     $952E               ; {}
9532: FC ; ????
9533: FE FE FE        INC     $FEFE,X             
9536: FF ; ????
9537: FF ; ????
9538: 00              BRK                         
9539: 00              BRK                         
953A: 00              BRK                         
953B: 00              BRK                         
953C: 00              BRK                         
953D: 00              BRK                         
953E: 00              BRK                         
953F: 00              BRK                         
9540: 3C ; ????
9541: 7F ; ????
9542: D8              CLD                         
9543: E0 60           CPX     #$60                
9545: 00              BRK                         
9546: 80 ; ????
9547: E0 00           CPX     #$00                
9549: 00              BRK                         
954A: 3E 3F 30        ROL     $303F,X             
954D: 37 ; ????
954E: 34 ; ????
954F: 35 3C           AND     $3C,X               
9551: 7E 1A 06        ROR     $061A,X             
9554: 06 12           ASL     $12                 
9556: 12 ; ????
9557: 54 ; ????
9558: 00              BRK                         
9559: 02 ; ????
955A: 7E FE 0E        ROR     $0EFE,X             
955D: EE 2E AC        INC     $AC2E               ; {}
9560: E0 43           CPX     #$43                
9562: 00              BRK                         
9563: 6F ; ????
9564: E0 C1           CPX     #$C1                
9566: EE 00 35        INC     $3500               
9569: 34 ; ????
956A: 37 ; ????
956B: 30 3F           BMI     $95AC               ; {}
956D: 27 ; ????
956E: 6E 00 50        ROR     $5000               
9571: D2 ; ????
9572: 12 ; ????
9573: F6 06           INC     $06,X               
9575: 1A ; ????
9576: 7C ; ????
9577: 00              BRK                         
9578: A8              TAY                         
9579: 2E EE 0E        ROL     $0EEE               
957C: FE 7E 7C        INC     $7C7E,X             
957F: 00              BRK                         
9580: 70 FB           BVS     $957D               ; {}
9582: 9D 9D 4C        STA     $4C9D,X             
9585: 0E 3E 4F        ASL     $4F3E               
9588: 00              BRK                         
9589: 08              PHP                         
958A: 0C ; ????
958B: 04 ; ????
958C: 00              BRK                         
958D: 02 ; ????
958E: 02 ; ????
958F: 00              BRK                         
9590: 0E DF B9        ASL     $B9DF               ; {}
9593: B9 32 70        LDA     $7032,Y             
9596: 78              SEI                         
9597: F6 00           INC     $00,X               ; {ram.GP_00}
9599: C7 ; ????
959A: 89 ; ????
959B: 99 10 10        STA     $1010,Y             
959E: 38              SEC                         
959F: 56 67           LSR     $67,X               
95A1: 07 ; ????
95A2: 00              BRK                         
95A3: 3F ; ????
95A4: 7F ; ????
95A5: 3F ; ????
95A6: 7F ; ????
95A7: 00              BRK                         
95A8: 00              BRK                         
95A9: 00              BRK                         
95AA: 00              BRK                         
95AB: 00              BRK                         
95AC: 01 0A           ORA     ($0A,X)             
95AE: 0A              ASL     A                   
95AF: 00              BRK                         
95B0: E2 ; ????
95B1: E6 00           INC     $00                 ; {ram.GP_00}
95B3: FC ; ????
95B4: FE FC FE        INC     $FEFC,X             
95B7: 00              BRK                         
95B8: 62 ; ????
95B9: 62 ; ????
95BA: 00              BRK                         
95BB: FC ; ????
95BC: FE AC AE        INC     $AEAC,X             ; {}
95BF: 00              BRK                         
95C0: 00              BRK                         
95C1: 00              BRK                         
95C2: 00              BRK                         
95C3: 00              BRK                         
95C4: 03 ; ????
95C5: 0F ; ????
95C6: 3E F8 00        ROL     $00F8,X             
95C9: 00              BRK                         
95CA: 00              BRK                         
95CB: 00              BRK                         
95CC: 00              BRK                         
95CD: 00              BRK                         
95CE: 00              BRK                         
95CF: 00              BRK                         
95D0: 03 ; ????
95D1: 0F ; ????
95D2: 7F ; ????
95D3: FC ; ????
95D4: E0 80           CPX     #$80                
95D6: 00              BRK                         
95D7: 00              BRK                         
95D8: 00              BRK                         
95D9: 00              BRK                         
95DA: 00              BRK                         
95DB: 00              BRK                         
95DC: 01 0F           ORA     ($0F,X)             
95DE: 39 00 E1        AND     $E100,Y             
95E1: C5 1D           CMP     $1D                 
95E3: 51 91           EOR     ($91),Y             
95E5: 01 00           ORA     ($00,X)             ; {ram.GP_00}
95E7: 10 00           BPL     $95E9               ; {}
95E9: 00              BRK                         
95EA: 00              BRK                         
95EB: 08              PHP                         
95EC: 48              PHA                         
95ED: CC 00 CF        CPY     $CF00               
95F0: DC ; ????
95F1: 10 10           BPL     $9603               ; {}
95F3: 10 10           BPL     $9605               ; {}
95F5: 10 00           BPL     $95F7               ; {}
95F7: 60              RTS                         
95F8: 01 C9           ORA     ($C9,X)             
95FA: 8D 0D CD        STA     $CD0D               
95FD: C9 00           CMP     #$00                
95FF: 9F ; ????
9600: F0 C0           BEQ     $95C2               ; {}
9602: 1E 31 62        ASL     $6231,X             
9605: 41 10           EOR     ($10,X)             
9607: 00              BRK                         
9608: 01 00           ORA     ($00,X)             ; {ram.GP_00}
960A: 01 0E           ORA     ($0E,X)             
960C: 1C ; ????
960D: 3E 09 00        ROL     $0009,X             
9610: 00              BRK                         
9611: 00              BRK                         
9612: 46 10           LSR     $10                 
9614: A8              TAY                         
9615: 10 00           BPL     $9617               ; {}
9617: 00              BRK                         
9618: 00              BRK                         
9619: 00              BRK                         
961A: 98              TYA                         
961B: 66 02           ROR     $02                 
961D: 66 D8           ROR     $D8                 
961F: 00              BRK                         
9620: 39 61 41        AND     $4161,Y             
9623: 41 41           EOR     ($41,X)             
9625: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9627: 04 ; ????
9628: 04 ; ????
9629: 18              CLC                         
962A: 38              SEC                         
962B: 34 ; ????
962C: 3C ; ????
962D: 7C ; ????
962E: 00              BRK                         
962F: 78              SEI                         
9630: CE 08 08        DEC     $0808               
9633: 08              PHP                         
9634: 08              PHP                         
9635: 00              BRK                         
9636: 00              BRK                         
9637: 04 ; ????
9638: 00              BRK                         
9639: 86 E4           STX     $E4                 
963B: E4 E6           CPX     $E6                 
963D: C6 00           DEC     $00                 ; {ram.GP_00}
963F: FA ; ????
9640: 00              BRK                         
9641: 00              BRK                         
9642: 00              BRK                         
9643: 00              BRK                         
9644: 00              BRK                         
9645: 00              BRK                         
9646: 00              BRK                         
9647: 00              BRK                         
9648: 10 10           BPL     $965A               ; {}
964A: 38              SEC                         
964B: FE 7C 38        INC     $387C,X             
964E: 6C 44 00        JMP     ($0044)             
9651: 00              BRK                         
9652: 18              CLC                         
9653: 33 ; ????
9654: 26 0C           ROL     $0C                 
9656: 29 08           AND     #$08                
9658: 0F ; ????
9659: 3F ; ????
965A: 67 ; ????
965B: 4F ; ????
965C: DE FC D8        DEC     $D8FC,X             
965F: F9 00 00        SBC     $0000,Y             ; {ram.GP_00}
9662: 00              BRK                         
9663: C0 21           CPY     #$21                
9665: 01 03           ORA     ($03,X)             
9667: 43 ; ????
9668: F0 FC           BEQ     $9666               ; {}
966A: FE FE 3F        INC     $3FFE,X             
966D: 1F ; ????
966E: 8F ; ????
966F: CF ; ????
9670: 08              PHP                         
9671: 0C ; ????
9672: 04 ; ????
9673: 00              BRK                         
9674: 00              BRK                         
9675: 18              CLC                         
9676: 0F ; ????
9677: 00              BRK                         
9678: F8              SED                         
9679: FC ; ????
967A: FC ; ????
967B: 7F ; ????
967C: 7F ; ????
967D: 3F ; ????
967E: 0F ; ????
967F: 00              BRK                         
9680: C3 ; ????
9681: 03 ; ????
9682: 07 ; ????
9683: 06 0E           ASL     $0E                 
9685: 7C ; ????
9686: F0 00           BEQ     $9688               ; {}
9688: CF ; ????
9689: 1F ; ????
968A: 3F ; ????
968B: FE FE FC        INC     $FCFE,X             
968E: F0 00           BEQ     $9690               ; {}
9690: 00              BRK                         
9691: 00              BRK                         
9692: 00              BRK                         
9693: 00              BRK                         
9694: 00              BRK                         
9695: 03 ; ????
9696: 04 ; ????
9697: 08              PHP                         
9698: 08              PHP                         
9699: 90 49           BCC     $96E4               ; {}
969B: 2A              ROL     A                   
969C: 29 47           AND     #$47                
969E: 44 ; ????
969F: 39 00 00        AND     $0000,Y             ; {ram.GP_00}
96A2: 00              BRK                         
96A3: 00              BRK                         
96A4: 00              BRK                         
96A5: C0 20           CPY     #$20                
96A7: 10 80           BPL     $9629               ; {}
96A9: 93 ; ????
96AA: 24 22           BIT     $22                 
96AC: 12 ; ????
96AD: E4 29           CPX     $29                 
96AF: 9A              TXS                         
96B0: 78              SEI                         
96B1: F8              SED                         
96B2: FC ; ????
96B3: FF ; ????
96B4: 7F ; ????
96B5: 7F ; ????
96B6: 3F ; ????
96B7: 0F ; ????
96B8: 7A ; ????
96B9: FA ; ????
96BA: DD DF 6F        CMP     $6FDF,X             
96BD: 7F ; ????
96BE: 3F ; ????
96BF: 0F ; ????
96C0: 1E 1F 3F        ASL     $3F1F,X             
96C3: FF ; ????
96C4: FE FE FC        INC     $FCFE,X             
96C7: F0 5E           BEQ     $9727               ; {}
96C9: 5F ; ????
96CA: BF ; ????
96CB: FF ; ????
96CC: FE FE FC        INC     $FCFE,X             
96CF: F0 00           BEQ     $96D1               ; {}
96D1: 00              BRK                         
96D2: 00              BRK                         
96D3: 00              BRK                         
96D4: 00              BRK                         
96D5: 00              BRK                         
96D6: 00              BRK                         
96D7: 00              BRK                         
96D8: 00              BRK                         
96D9: 00              BRK                         
96DA: 00              BRK                         
96DB: 00              BRK                         
96DC: 00              BRK                         
96DD: 00              BRK                         
96DE: 00              BRK                         
96DF: 00              BRK                         
96E0: 00              BRK                         
96E1: 00              BRK                         
96E2: 00              BRK                         
96E3: 00              BRK                         
96E4: 00              BRK                         
96E5: 00              BRK                         
96E6: 00              BRK                         
96E7: 00              BRK                         
96E8: 00              BRK                         
96E9: 00              BRK                         
96EA: 00              BRK                         
96EB: 00              BRK                         
96EC: 00              BRK                         
96ED: 00              BRK                         
96EE: 00              BRK                         
96EF: 00              BRK                         
96F0: 00              BRK                         
96F1: 00              BRK                         
96F2: 00              BRK                         
96F3: 00              BRK                         
96F4: 00              BRK                         
96F5: 00              BRK                         
96F6: 00              BRK                         
96F7: 00              BRK                         
96F8: 00              BRK                         
96F9: 00              BRK                         
96FA: 00              BRK                         
96FB: 00              BRK                         
96FC: 00              BRK                         
96FD: 00              BRK                         
96FE: 00              BRK                         
96FF: 00              BRK                         
9700: 00              BRK                         
9701: 00              BRK                         
9702: 00              BRK                         
9703: 00              BRK                         
9704: 00              BRK                         
9705: 00              BRK                         
9706: 00              BRK                         
9707: 00              BRK                         
9708: 00              BRK                         
9709: 00              BRK                         
970A: 00              BRK                         
970B: 00              BRK                         
970C: 00              BRK                         
970D: 00              BRK                         
970E: 00              BRK                         
970F: 00              BRK                         
9710: 00              BRK                         
9711: 00              BRK                         
9712: 00              BRK                         
9713: 00              BRK                         
9714: 00              BRK                         
9715: 00              BRK                         
9716: 00              BRK                         
9717: 00              BRK                         
9718: 00              BRK                         
9719: 00              BRK                         
971A: 00              BRK                         
971B: 00              BRK                         
971C: 00              BRK                         
971D: 00              BRK                         
971E: 00              BRK                         
971F: 00              BRK                         
9720: 00              BRK                         
9721: 00              BRK                         
9722: 00              BRK                         
9723: 00              BRK                         
9724: 00              BRK                         
9725: 00              BRK                         
9726: 00              BRK                         
9727: 00              BRK                         
9728: 00              BRK                         
9729: 00              BRK                         
972A: 00              BRK                         
972B: 00              BRK                         
972C: 00              BRK                         
972D: 00              BRK                         
972E: 00              BRK                         
972F: 00              BRK                         
9730: 00              BRK                         
9731: 00              BRK                         
9732: 00              BRK                         
9733: 00              BRK                         
9734: 00              BRK                         
9735: 00              BRK                         
9736: 00              BRK                         
9737: 00              BRK                         
9738: 00              BRK                         
9739: 00              BRK                         
973A: 00              BRK                         
973B: 00              BRK                         
973C: 00              BRK                         
973D: 00              BRK                         
973E: 00              BRK                         
973F: 00              BRK                         
9740: 00              BRK                         
9741: 00              BRK                         
9742: 00              BRK                         
9743: 00              BRK                         
9744: 00              BRK                         
9745: 00              BRK                         
9746: 00              BRK                         
9747: 00              BRK                         
9748: 00              BRK                         
9749: 00              BRK                         
974A: 00              BRK                         
974B: 00              BRK                         
974C: 00              BRK                         
974D: 00              BRK                         
974E: 00              BRK                         
974F: 00              BRK                         
9750: 00              BRK                         
9751: 00              BRK                         
9752: 00              BRK                         
9753: 00              BRK                         
9754: 00              BRK                         
9755: 00              BRK                         
9756: 00              BRK                         
9757: 00              BRK                         
9758: 00              BRK                         
9759: 00              BRK                         
975A: 00              BRK                         
975B: 00              BRK                         
975C: 00              BRK                         
975D: 00              BRK                         
975E: 00              BRK                         
975F: 00              BRK                         
9760: 00              BRK                         
9761: 00              BRK                         
9762: 00              BRK                         
9763: 00              BRK                         
9764: 00              BRK                         
9765: 00              BRK                         
9766: 00              BRK                         
9767: 00              BRK                         
9768: 00              BRK                         
9769: 00              BRK                         
976A: 00              BRK                         
976B: 00              BRK                         
976C: 00              BRK                         
976D: 00              BRK                         
976E: 00              BRK                         
976F: 00              BRK                         
9770: 00              BRK                         
9771: 00              BRK                         
9772: 00              BRK                         
9773: 00              BRK                         
9774: 00              BRK                         
9775: 00              BRK                         
9776: 00              BRK                         
9777: 00              BRK                         
9778: 00              BRK                         
9779: 00              BRK                         
977A: 00              BRK                         
977B: 00              BRK                         
977C: 00              BRK                         
977D: 00              BRK                         
977E: 00              BRK                         
977F: 00              BRK                         
9780: 00              BRK                         
9781: 00              BRK                         
9782: 00              BRK                         
9783: 00              BRK                         
9784: 00              BRK                         
9785: 00              BRK                         
9786: 00              BRK                         
9787: 00              BRK                         
9788: 00              BRK                         
9789: 00              BRK                         
978A: 00              BRK                         
978B: 00              BRK                         
978C: 00              BRK                         
978D: 00              BRK                         
978E: 00              BRK                         
978F: 00              BRK                         
9790: 00              BRK                         
9791: 00              BRK                         
9792: 00              BRK                         
9793: 00              BRK                         
9794: 00              BRK                         
9795: 00              BRK                         
9796: 00              BRK                         
9797: 00              BRK                         
9798: 00              BRK                         
9799: 00              BRK                         
979A: 00              BRK                         
979B: 00              BRK                         
979C: 00              BRK                         
979D: 00              BRK                         
979E: 00              BRK                         
979F: 00              BRK                         
97A0: 00              BRK                         
97A1: 00              BRK                         
97A2: 00              BRK                         
97A3: 00              BRK                         
97A4: 00              BRK                         
97A5: 00              BRK                         
97A6: 00              BRK                         
97A7: 00              BRK                         
97A8: 00              BRK                         
97A9: 00              BRK                         
97AA: 00              BRK                         
97AB: 00              BRK                         
97AC: 00              BRK                         
97AD: 00              BRK                         
97AE: 00              BRK                         
97AF: 00              BRK                         
97B0: 00              BRK                         
97B1: 00              BRK                         
97B2: 00              BRK                         
97B3: 00              BRK                         
97B4: 00              BRK                         
97B5: 00              BRK                         
97B6: 00              BRK                         
97B7: 00              BRK                         
97B8: 00              BRK                         
97B9: 00              BRK                         
97BA: 00              BRK                         
97BB: 00              BRK                         
97BC: 00              BRK                         
97BD: 00              BRK                         
97BE: 00              BRK                         
97BF: 00              BRK                         
97C0: 00              BRK                         
97C1: 00              BRK                         
97C2: 00              BRK                         
97C3: 00              BRK                         
97C4: 00              BRK                         
97C5: 00              BRK                         
97C6: 00              BRK                         
97C7: 00              BRK                         
97C8: 00              BRK                         
97C9: 00              BRK                         
97CA: 00              BRK                         
97CB: 00              BRK                         
97CC: 00              BRK                         
97CD: 00              BRK                         
97CE: 00              BRK                         
97CF: 00              BRK                         
97D0: 00              BRK                         
97D1: 00              BRK                         
97D2: 00              BRK                         
97D3: 00              BRK                         
97D4: 00              BRK                         
97D5: 00              BRK                         
97D6: 00              BRK                         
97D7: 00              BRK                         
97D8: 00              BRK                         
97D9: 00              BRK                         
97DA: 00              BRK                         
97DB: 00              BRK                         
97DC: 00              BRK                         
97DD: 00              BRK                         
97DE: 00              BRK                         
97DF: 00              BRK                         
97E0: 00              BRK                         
97E1: 00              BRK                         
97E2: 00              BRK                         
97E3: 00              BRK                         
97E4: 00              BRK                         
97E5: 00              BRK                         
97E6: 00              BRK                         
97E7: 00              BRK                         
97E8: 00              BRK                         
97E9: 00              BRK                         
97EA: 00              BRK                         
97EB: 00              BRK                         
97EC: 00              BRK                         
97ED: 00              BRK                         
97EE: 00              BRK                         
97EF: 00              BRK                         
97F0: 00              BRK                         
97F1: 00              BRK                         
97F2: 00              BRK                         
97F3: 00              BRK                         
97F4: 00              BRK                         
97F5: 00              BRK                         
97F6: 00              BRK                         
97F7: 00              BRK                         
97F8: 00              BRK                         
97F9: 00              BRK                         
97FA: 00              BRK                         
97FB: 00              BRK                         
97FC: 00              BRK                         
97FD: 00              BRK                         
97FE: 00              BRK                         
97FF: 00              BRK                         
9800: 3C ; ????
9801: 46 A3           LSR     $A3                 
9803: 83 ; ????
9804: 83 ; ????
9805: C7 ; ????
9806: 7E 3C 00        ROR     $003C,X             
9809: 38              SEC                         
980A: 7C ; ????
980B: 7C ; ????
980C: 7C ; ????
980D: 38              SEC                         
980E: 00              BRK                         
980F: 00              BRK                         
9810: 00              BRK                         
9811: 00              BRK                         
9812: 02 ; ????
9813: 05 07           ORA     $07                 
9815: 03 ; ????
9816: 0F ; ????
9817: 39 00 00        AND     $0000,Y             ; {ram.GP_00}
981A: 01 02           ORA     ($02,X)             
981C: 01 0D           ORA     ($0D,X)             
981E: 71 C6           ADC     ($C6),Y             
9820: 3F ; ????
9821: 7F ; ????
9822: 7F ; ????
9823: FF ; ????
9824: FF ; ????
9825: FF ; ????
9826: FF ; ????
9827: C7 ; ????
9828: 3F ; ????
9829: 43 ; ????
982A: 3F ; ????
982B: 83 ; ????
982C: 00              BRK                         
982D: 46 6E           LSR     $6E                 
982F: B8              CLV                         
9830: C0 F0           CPY     #$F0                
9832: FC ; ????
9833: E0 F8           CPX     #$F8                
9835: FC ; ????
9836: FE FE 00        INC     $00FE,X             
9839: E0 F8           CPX     #$F8                
983B: 80 ; ????
983C: E0 78           CPX     #$78                
983E: 78              SEI                         
983F: FC ; ????
9840: 00              BRK                         
9841: 00              BRK                         
9842: 08              PHP                         
9843: F4 ; ????
9844: FA ; ????
9845: FA ; ????
9846: FF ; ????
9847: F1 00           SBC     ($00),Y             ; {ram.GP_00}
9849: 00              BRK                         
984A: F0 C8           BEQ     $9814               ; {}
984C: 64 ; ????
984D: 64 ; ????
984E: 40              RTI                         
984F: 0E C9 55        ASL     $55C9               
9852: 7F ; ????
9853: 55 1F           EOR     $1F,X               
9855: 03 ; ????
9856: 00              BRK                         
9857: 00              BRK                         
9858: 36 FF           ROL     $FF,X               
985A: 00              BRK                         
985B: FF ; ????
985C: 00              BRK                         
985D: 00              BRK                         
985E: 00              BRK                         
985F: 00              BRK                         
9860: CF ; ????
9861: 7F ; ????
9862: FF ; ????
9863: FF ; ????
9864: FF ; ????
9865: 3F ; ????
9866: 1F ; ????
9867: 07 ; ????
9868: B3 ; ????
9869: 47 ; ????
986A: BE BD 3D        LDX     $3DBD,Y             
986D: 1E 0F 01        ASL     $010F,X             
9870: FE FE FE        INC     $FEFE,X             
9873: FC ; ????
9874: FC ; ????
9875: F8              SED                         
9876: FD FE EC        SBC     $ECFE,X             
9879: 1C ; ????
987A: FC ; ????
987B: F8              SED                         
987C: 80 ; ????
987D: 60              RTS                         
987E: F0 FC           BEQ     $987C               ; {}
9880: 00              BRK                         
9881: 3D 1F 0F        AND     $0F1F,X             
9884: 03 ; ????
9885: 0F ; ????
9886: 7F ; ????
9887: FF ; ????
9888: 00              BRK                         
9889: 12 ; ????
988A: 0C ; ????
988B: 03 ; ????
988C: 01 01           ORA     ($01,X)             
988E: 0F ; ????
988F: 7F ; ????
9890: 00              BRK                         
9891: 00              BRK                         
9892: 40              RTI                         
9893: 90 C8           BCC     $985D               ; {}
9895: F4 ; ????
9896: C2 ; ????
9897: 81 00           STA     ($00,X)             ; {ram.GP_00}
9899: 00              BRK                         
989A: 80 ; ????
989B: 60              RTS                         
989C: 30 88           BMI     $9826               ; {}
989E: BC 7E 03        LDY     $037E,X             
98A1: 04 ; ????
98A2: 09 0A           ORA     #$0A                
98A4: 14 ; ????
98A5: 18              CLC                         
98A6: 08              PHP                         
98A7: 10 00           BPL     $98A9               ; {}
98A9: 03 ; ????
98AA: 06 05           ASL     $05                 
98AC: 0B ; ????
98AD: 07 ; ????
98AE: 17 ; ????
98AF: 0F ; ????
98B0: C0 20           CPY     #$20                
98B2: D0 68           BNE     $991C               ; {}
98B4: 38              SEC                         
98B5: 18              CLC                         
98B6: 0C ; ????
98B7: 04 ; ????
98B8: 00              BRK                         
98B9: C0 20           CPY     #$20                
98BB: 90 C0           BCC     $987D               ; {}
98BD: E0 F0           CPX     #$F0                
98BF: F8              SED                         
98C0: C0 7F           CPY     #$7F                
98C2: 60              RTS                         
98C3: 60              RTS                         
98C4: 3F ; ????
98C5: 7E 7D 6D        ROR     $6D7D,X             
98C8: BF ; ????
98C9: 80 ; ????
98CA: 5F ; ????
98CB: 5F ; ????
98CC: 00              BRK                         
98CD: 4D 43 53        EOR     $5343               
98D0: 79 6F 6C        ADC     $6C6F,Y             
98D3: 7B ; ????
98D4: 7B ; ????
98D5: 7C ; ????
98D6: 7F ; ????
98D7: C0 4F           CPY     #$4F                
98D9: 50 57           BVC     $9932               ; {}
98DB: 4C 4C 47        JMP     $474C               
98DE: 80 ; ????
98DF: BF ; ????
98E0: 08              PHP                         
98E1: 51 FF           EOR     ($FF),Y             
98E3: 57 ; ????
98E4: FE FC 00        INC     $00FC,X             
98E7: 00              BRK                         
98E8: F7 ; ????
98E9: FE 08 F8        INC     $F808,X             
98EC: 00              BRK                         
98ED: 00              BRK                         
98EE: 00              BRK                         
98EF: 00              BRK                         
98F0: 55 7F           EOR     $7F,X               
98F2: 00              BRK                         
98F3: 00              BRK                         
98F4: 00              BRK                         
98F5: 05 17           ORA     $17                 
98F7: 00              BRK                         
98F8: FF ; ????
98F9: 00              BRK                         
98FA: 0E 11 A0        ASL     $A011               ; {}
98FD: 47 ; ????
98FE: 98              TYA                         
98FF: 00              BRK                         
9900: 00              BRK                         
9901: 00              BRK                         
9902: 00              BRK                         
9903: 1F ; ????
9904: 3F ; ????
9905: 3F ; ????
9906: 3F ; ????
9907: 1F ; ????
9908: 00              BRK                         
9909: 0F ; ????
990A: 1F ; ????
990B: 20 1B 13        JSR     $131B               
990E: 0E 20 00        ASL     $0020               
9911: 40              RTI                         
9912: 10 04           BPL     $9918               ; {}
9914: C6 DE           DEC     $DE                 
9916: F3 ; ????
9917: E7 ; ????
9918: 00              BRK                         
9919: 80 ; ????
991A: E0 F8           CPX     #$F8                
991C: 38              SEC                         
991D: 20 0C 18        JSR     $180C               
9920: 1F ; ????
9921: 1F ; ????
9922: 7F ; ????
9923: FF ; ????
9924: FF ; ????
9925: 7F ; ????
9926: 1F ; ????
9927: 17 ; ????
9928: 00              BRK                         
9929: 00              BRK                         
992A: 70 A0           BVS     $98CC               ; {}
992C: 80 ; ????
992D: 01 22           ORA     ($22,X)             
992F: 22 ; ????
9930: E7 ; ????
9931: E7 ; ????
9932: F7 ; ????
9933: 8F ; ????
9934: 67 ; ????
9935: F7 ; ????
9936: F7 ; ????
9937: BF ; ????
9938: 18              CLC                         
9939: 18              CLC                         
993A: 08              PHP                         
993B: 70 98           BVS     $98D5               ; {}
993D: C8              INY                         
993E: 88              DEY                         
993F: C0 03           CPY     #$03                
9941: 01 01           ORA     ($01,X)             
9943: 01 01           ORA     ($01,X)             
9945: 01 01           ORA     ($01,X)             
9947: 01 04           ORA     ($04,X)             
9949: 02 ; ????
994A: 02 ; ????
994B: 02 ; ????
994C: 00              BRK                         
994D: 00              BRK                         
994E: 00              BRK                         
994F: 03 ; ????
9950: FE 7C 7C        INC     $7C7C,X             
9953: BC BC FE        LDY     $FEBC,X             
9956: FE F8 00        INC     $00F8,X             
9959: 80 ; ????
995A: 80 ; ????
995B: 40              RTI                         
995C: 40              RTI                         
995D: F0 00           BEQ     $995F               ; {}
995F: C0 03           CPY     #$03                
9961: 03 ; ????
9962: 0F ; ????
9963: 0F ; ????
9964: 0F ; ????
9965: 1F ; ????
9966: 00              BRK                         
9967: 00              BRK                         
9968: 04 ; ????
9969: 0C ; ????
996A: 10 10           BPL     $997C               ; {}
996C: 10 3C           BPL     $99AA               ; {}
996E: 00              BRK                         
996F: 00              BRK                         
9970: FE BE FC        INC     $FCBE,X             
9973: FC ; ????
9974: BC BC BE        LDY     $BEBC,X             ; {}
9977: 7F ; ????
9978: 00              BRK                         
9979: 40              RTI                         
997A: 00              BRK                         
997B: 00              BRK                         
997C: 40              RTI                         
997D: 40              RTI                         
997E: 40              RTI                         
997F: F8              SED                         
9980: CF ; ????
9981: 5F ; ????
9982: FF ; ????
9983: 7F ; ????
9984: 7F ; ????
9985: 7F ; ????
9986: 7C ; ????
9987: 3E C0 2D        ROL     $2DC0,X             
998A: 89 ; ????
998B: 07 ; ????
998C: 00              BRK                         
998D: 15 03           ORA     $03,X               
998F: 41 9C           EOR     ($9C,X)             
9991: CE EC FE        DEC     $FEEC               
9994: F7 ; ????
9995: F7 ; ????
9996: 77 ; ????
9997: 77 ; ????
9998: 6C B6 97        JMP     ($97B6)             ; {}
999B: 0D 0C 48        ORA     $480C               
999E: 88              DEY                         
999F: 88              DEY                         
99A0: 3E 3E 1F        ROL     $1F3E,X             
99A3: 07 ; ????
99A4: 01 07           ORA     ($07,X)             
99A6: 03 ; ????
99A7: 03 ; ????
99A8: 41 41           EOR     ($41,X)             
99AA: 45 08           EOR     $08                 
99AC: 06 00           ASL     $00                 ; {ram.GP_00}
99AE: 04 ; ????
99AF: 04 ; ????
99B0: 77 ; ????
99B1: 77 ; ????
99B2: F7 ; ????
99B3: F7 ; ????
99B4: F9 FF FE        SBC     $FEFF,Y             
99B7: FE 88 88        INC     $8888,X             ; {}
99BA: 48              PHA                         
99BB: 08              PHP                         
99BC: 06 00           ASL     $00                 ; {ram.GP_00}
99BE: 00              BRK                         
99BF: 00              BRK                         
99C0: 00              BRK                         
99C1: 01 00           ORA     ($00,X)             ; {ram.GP_00}
99C3: 04 ; ????
99C4: 02 ; ????
99C5: 03 ; ????
99C6: 43 ; ????
99C7: 47 ; ????
99C8: 00              BRK                         
99C9: 03 ; ????
99CA: 07 ; ????
99CB: 03 ; ????
99CC: 31 78           AND     ($78),Y             
99CE: 7D 38 38        ADC     $3838,X             
99D1: 00              BRK                         
99D2: 0D 43 31        ORA     $3143               
99D5: 1D 03 01        ORA     $0103,X             
99D8: 03 ; ????
99D9: 0F ; ????
99DA: 03 ; ????
99DB: 40              RTI                         
99DC: 70 3D           BVS     $9A1B               ; {}
99DE: 0D 01 07        ORA     $0701               
99E1: 1F ; ????
99E2: 3D 5B 77        AND     $775B,X             
99E5: 77 ; ????
99E6: 77 ; ????
99E7: 3B ; ????
99E8: 01 0C           ORA     ($0C,X)             
99EA: 1B ; ????
99EB: 37 ; ????
99EC: 2F ; ????
99ED: 2F ; ????
99EE: 0F ; ????
99EF: 07 ; ????
99F0: 0F ; ????
99F1: 01 01           ORA     ($01,X)             
99F3: 01 0F           ORA     ($0F,X)             
99F5: 31 20           AND     ($20),Y             
99F7: 40              RTI                         
99F8: 01 00           ORA     ($00,X)             ; {ram.GP_00}
99FA: 01 01           ORA     ($01,X)             
99FC: 0D 3D 30        ORA     $303D               
99FF: 60              RTS                         
9A00: 3F ; ????
9A01: 7F ; ????
9A02: 7F ; ????
9A03: FF ; ????
9A04: 7F ; ????
9A05: 7F ; ????
9A06: 2F ; ????
9A07: 3F ; ????
9A08: 00              BRK                         
9A09: 00              BRK                         
9A0A: 90 B8           BCC     $99C4               ; {}
9A0C: 00              BRK                         
9A0D: 2C 3C 18        BIT     $183C               
9A10: 00              BRK                         
9A11: 80 ; ????
9A12: 86 DF           STX     $DF                 
9A14: D8              CLD                         
9A15: BC B0 40        LDY     $40B0,X             
9A18: 00              BRK                         
9A19: 07 ; ????
9A1A: 1E 3F 38        ASL     $383F,X             
9A1D: 7C ; ????
9A1E: 70 C0           BVS     $99E0               ; {}
9A20: 3F ; ????
9A21: 7F ; ????
9A22: 7F ; ????
9A23: 7F ; ????
9A24: 7F ; ????
9A25: 7F ; ????
9A26: 2F ; ????
9A27: 7F ; ????
9A28: 00              BRK                         
9A29: 00              BRK                         
9A2A: 10 38           BPL     $9A64               ; {}
9A2C: 00              BRK                         
9A2D: 2C 3C D8        BIT     $D83C               
9A30: 00              BRK                         
9A31: 80 ; ????
9A32: 80 ; ????
9A33: C0 C0           CPY     #$C0                
9A35: E0 80           CPX     #$80                
9A37: 7E 00 00        ROR     $0000,X             ; {ram.GP_00}
9A3A: 00              BRK                         
9A3B: 00              BRK                         
9A3C: 00              BRK                         
9A3D: 00              BRK                         
9A3E: 7E BF 1F        ROR     $1FBF,X             
9A41: 1F ; ????
9A42: 0F ; ????
9A43: 0F ; ????
9A44: 02 ; ????
9A45: 1F ; ????
9A46: 06 04           ASL     $04                 
9A48: 03 ; ????
9A49: 0D 0D 00        ORA     $000D               
9A4C: 01 14           ORA     ($14,X)             
9A4E: 00              BRK                         
9A4F: 04 ; ????
9A50: E0 C0           CPX     #$C0                
9A52: C2 ; ????
9A53: B0 7C           BCS     $9AD1               ; {}
9A55: F8              SED                         
9A56: 10 00           BPL     $9A58               ; {}
9A58: 1A ; ????
9A59: BE BC 4C        LDX     $4CBC,Y             
9A5C: D0 00           BNE     $9A5E               ; {}
9A5E: 10 00           BPL     $9A60               ; {}
9A60: 51 F9           EOR     ($F9),Y             
9A62: EF ; ????
9A63: 7F ; ????
9A64: DE 7C C0        DEC     $C07C,X             
9A67: 00              BRK                         
9A68: EE 16 10        INC     $1016               
9A6B: 90 60           BCC     $9ACD               ; {}
9A6D: 80 ; ????
9A6E: 00              BRK                         
9A6F: 00              BRK                         
9A70: 01 12           ORA     ($12,X)             
9A72: 22 ; ????
9A73: 24 44           BIT     $44                 
9A75: 4C CC CC        JMP     $CCCC               
9A78: 00              BRK                         
9A79: 00              BRK                         
9A7A: 00              BRK                         
9A7B: 00              BRK                         
9A7C: 00              BRK                         
9A7D: 00              BRK                         
9A7E: 00              BRK                         
9A7F: 00              BRK                         
9A80: 2F ; ????
9A81: 66 7F           ROR     $7F                 
9A83: 51 59           EOR     ($59),Y             
9A85: 59 63 BF        EOR     $BF63,Y             ; {}
9A88: 10 99           BPL     $9A23               ; {}
9A8A: 00              BRK                         
9A8B: 2E BE 26        ROL     $26BE               
9A8E: 1C ; ????
9A8F: 00              BRK                         
9A90: 00              BRK                         
9A91: 80 ; ????
9A92: C0 80           CPY     #$80                
9A94: F0 E8           BEQ     $9A7E               ; {}
9A96: E0 C0           CPX     #$C0                
9A98: 80 ; ????
9A99: 00              BRK                         
9A9A: 10 60           BPL     $9AFC               ; {}
9A9C: 00              BRK                         
9A9D: 00              BRK                         
9A9E: 00              BRK                         
9A9F: 20 3B 19        JSR     $193B               
9AA2: 33 ; ????
9AA3: 7F ; ????
9AA4: 7F ; ????
9AA5: 7F ; ????
9AA6: 3F ; ????
9AA7: 0F ; ????
9AA8: 04 ; ????
9AA9: 16 2D           ASL     $2D,X               
9AAB: 63 ; ????
9AAC: 7F ; ????
9AAD: 37 ; ????
9AAE: 08              PHP                         
9AAF: 0F ; ????
9AB0: E0 A8           CPX     #$A8                
9AB2: C0 C0           CPY     #$C0                
9AB4: C0 EC           CPY     #$EC                
9AB6: FC ; ????
9AB7: FE 18 40        INC     $4018,X             
9ABA: A0 B0           LDY     #$B0                
9ABC: B8              CLV                         
9ABD: 10 0C           BPL     $9ACB               ; {}
9ABF: 1E 0F 0F        ASL     $0F0F,X             
9AC2: 0F ; ????
9AC3: 1F ; ????
9AC4: 1F ; ????
9AC5: 1F ; ????
9AC6: 1F ; ????
9AC7: 1F ; ????
9AC8: 0E 01 0F        ASL     $0F01               
9ACB: 1F ; ????
9ACC: 1F ; ????
9ACD: 1F ; ????
9ACE: 1F ; ????
9ACF: 1F ; ????
9AD0: EE EE E8        INC     $E8EE               
9AD3: E0 F0           CPX     #$F0                
9AD5: E0 F0           CPX     #$F0                
9AD7: F0 0E           BEQ     $9AE7               ; {}
9AD9: 88              DEY                         
9ADA: 87 ; ????
9ADB: CB ; ????
9ADC: C1 C0           CMP     ($C0,X)             
9ADE: E0 E0           CPX     #$E0                
9AE0: 1F ; ????
9AE1: 1F ; ????
9AE2: 1F ; ????
9AE3: 0F ; ????
9AE4: 0F ; ????
9AE5: 1F ; ????
9AE6: 07 ; ????
9AE7: 3F ; ????
9AE8: 1F ; ????
9AE9: 1F ; ????
9AEA: 19 07 09        ORA     $0907,Y             
9AED: 16 3B           ASL     $3B,X               
9AEF: 41 F8           EOR     ($F8,X)             
9AF1: F8              SED                         
9AF2: FC ; ????
9AF3: FC ; ????
9AF4: FE FE FF        INC     $FFFE,X             
9AF7: FF ; ????
9AF8: F0 F0           BEQ     $9AEA               ; {}
9AFA: F8              SED                         
9AFB: F8              SED                         
9AFC: FC ; ????
9AFD: FC ; ????
9AFE: 3E FE 00        ROL     $00FE,X             
9B01: 00              BRK                         
9B02: 03 ; ????
9B03: 07 ; ????
9B04: 07 ; ????
9B05: 0F ; ????
9B06: 0F ; ????
9B07: 0B ; ????
9B08: 00              BRK                         
9B09: 00              BRK                         
9B0A: 00              BRK                         
9B0B: 08              PHP                         
9B0C: 00              BRK                         
9B0D: 01 03           ORA     ($03,X)             
9B0F: 15 00           ORA     $00,X               ; {ram.GP_00}
9B11: 00              BRK                         
9B12: C0 E0           CPY     #$E0                
9B14: F0 F8           BEQ     $9B0E               ; {}
9B16: FC ; ????
9B17: FC ; ????
9B18: 00              BRK                         
9B19: 00              BRK                         
9B1A: 00              BRK                         
9B1B: 00              BRK                         
9B1C: 08              PHP                         
9B1D: C0 E0           CPY     #$E0                
9B1F: E0 09           CPX     #$09                
9B21: 09 03           ORA     #$03                
9B23: 01 30           ORA     ($30,X)             
9B25: 34 ; ????
9B26: 7C ; ????
9B27: 38              SEC                         
9B28: 06 06           ASL     $06                 
9B2A: 0C ; ????
9B2B: 0D 2C 28        ORA     $282C               
9B2E: 34 ; ????
9B2F: D8              CLD                         
9B30: FE FF FF        INC     $FFFF,X             
9B33: FF ; ????
9B34: 7F ; ????
9B35: 3F ; ????
9B36: 3F ; ????
9B37: 1F ; ????
9B38: F8              SED                         
9B39: E0 DF           CPX     #$DF                
9B3B: BF ; ????
9B3C: 3F ; ????
9B3D: 3F ; ????
9B3E: 3F ; ????
9B3F: 1F ; ????
9B40: 00              BRK                         
9B41: 00              BRK                         
9B42: 80 ; ????
9B43: C0 C0           CPY     #$C0                
9B45: F8              SED                         
9B46: FE F1 00        INC     $00F1,X             
9B49: 00              BRK                         
9B4A: 80 ; ????
9B4B: C0 C0           CPY     #$C0                
9B4D: F8              SED                         
9B4E: F2 ; ????
9B4F: CE 00 00        DEC     $0000               ; {ram.GP_00}
9B52: 00              BRK                         
9B53: 00              BRK                         
9B54: 00              BRK                         
9B55: 00              BRK                         
9B56: 00              BRK                         
9B57: 00              BRK                         
9B58: 00              BRK                         
9B59: 00              BRK                         
9B5A: 00              BRK                         
9B5B: 00              BRK                         
9B5C: 00              BRK                         
9B5D: 00              BRK                         
9B5E: 00              BRK                         
9B5F: 00              BRK                         
9B60: 00              BRK                         
9B61: 00              BRK                         
9B62: 00              BRK                         
9B63: 00              BRK                         
9B64: 00              BRK                         
9B65: 00              BRK                         
9B66: 00              BRK                         
9B67: 00              BRK                         
9B68: 00              BRK                         
9B69: 00              BRK                         
9B6A: 00              BRK                         
9B6B: 00              BRK                         
9B6C: 00              BRK                         
9B6D: 00              BRK                         
9B6E: 00              BRK                         
9B6F: 00              BRK                         
9B70: 00              BRK                         
9B71: 00              BRK                         
9B72: 00              BRK                         
9B73: 00              BRK                         
9B74: 00              BRK                         
9B75: 00              BRK                         
9B76: 00              BRK                         
9B77: 00              BRK                         
9B78: 00              BRK                         
9B79: 00              BRK                         
9B7A: 00              BRK                         
9B7B: 00              BRK                         
9B7C: 00              BRK                         
9B7D: 00              BRK                         
9B7E: 00              BRK                         
9B7F: 00              BRK                         
9B80: 00              BRK                         
9B81: 00              BRK                         
9B82: 00              BRK                         
9B83: 00              BRK                         
9B84: 00              BRK                         
9B85: 00              BRK                         
9B86: 00              BRK                         
9B87: 00              BRK                         
9B88: 00              BRK                         
9B89: 00              BRK                         
9B8A: 00              BRK                         
9B8B: 00              BRK                         
9B8C: 00              BRK                         
9B8D: 00              BRK                         
9B8E: 00              BRK                         
9B8F: 00              BRK                         
9B90: 00              BRK                         
9B91: 00              BRK                         
9B92: 00              BRK                         
9B93: 00              BRK                         
9B94: 00              BRK                         
9B95: 00              BRK                         
9B96: 00              BRK                         
9B97: 00              BRK                         
9B98: 00              BRK                         
9B99: 00              BRK                         
9B9A: 00              BRK                         
9B9B: 00              BRK                         
9B9C: 00              BRK                         
9B9D: 00              BRK                         
9B9E: 00              BRK                         
9B9F: 00              BRK                         
9BA0: 00              BRK                         
9BA1: 00              BRK                         
9BA2: 00              BRK                         
9BA3: 00              BRK                         
9BA4: 00              BRK                         
9BA5: 00              BRK                         
9BA6: 00              BRK                         
9BA7: 00              BRK                         
9BA8: 00              BRK                         
9BA9: 00              BRK                         
9BAA: 00              BRK                         
9BAB: 00              BRK                         
9BAC: 00              BRK                         
9BAD: 00              BRK                         
9BAE: 00              BRK                         
9BAF: 00              BRK                         
9BB0: 00              BRK                         
9BB1: 00              BRK                         
9BB2: 00              BRK                         
9BB3: 00              BRK                         
9BB4: 00              BRK                         
9BB5: 00              BRK                         
9BB6: 00              BRK                         
9BB7: 00              BRK                         
9BB8: 00              BRK                         
9BB9: 00              BRK                         
9BBA: 00              BRK                         
9BBB: 00              BRK                         
9BBC: 00              BRK                         
9BBD: 00              BRK                         
9BBE: 00              BRK                         
9BBF: 00              BRK                         
9BC0: 00              BRK                         
9BC1: 00              BRK                         
9BC2: 00              BRK                         
9BC3: 00              BRK                         
9BC4: 00              BRK                         
9BC5: 00              BRK                         
9BC6: 00              BRK                         
9BC7: 00              BRK                         
9BC8: 00              BRK                         
9BC9: 00              BRK                         
9BCA: 00              BRK                         
9BCB: 00              BRK                         
9BCC: 00              BRK                         
9BCD: 00              BRK                         
9BCE: 00              BRK                         
9BCF: 00              BRK                         
9BD0: 00              BRK                         
9BD1: 00              BRK                         
9BD2: 00              BRK                         
9BD3: 00              BRK                         
9BD4: 00              BRK                         
9BD5: 00              BRK                         
9BD6: 00              BRK                         
9BD7: 00              BRK                         
9BD8: 00              BRK                         
9BD9: 00              BRK                         
9BDA: 00              BRK                         
9BDB: 00              BRK                         
9BDC: 00              BRK                         
9BDD: 00              BRK                         
9BDE: 00              BRK                         
9BDF: 00              BRK                         
9BE0: 00              BRK                         
9BE1: 00              BRK                         
9BE2: 00              BRK                         
9BE3: 00              BRK                         
9BE4: 00              BRK                         
9BE5: 00              BRK                         
9BE6: 00              BRK                         
9BE7: 00              BRK                         
9BE8: 00              BRK                         
9BE9: 00              BRK                         
9BEA: 00              BRK                         
9BEB: 00              BRK                         
9BEC: 00              BRK                         
9BED: 00              BRK                         
9BEE: 00              BRK                         
9BEF: 00              BRK                         
9BF0: 00              BRK                         
9BF1: 00              BRK                         
9BF2: 00              BRK                         
9BF3: 00              BRK                         
9BF4: 00              BRK                         
9BF5: 00              BRK                         
9BF6: 00              BRK                         
9BF7: 00              BRK                         
9BF8: 00              BRK                         
9BF9: 00              BRK                         
9BFA: 00              BRK                         
9BFB: 00              BRK                         
9BFC: 00              BRK                         
9BFD: 00              BRK                         
9BFE: 00              BRK                         
9BFF: 00              BRK                         
9C00: 6C F6 C1        JMP     ($C1F6)             
9C03: 6D E4 7C        ADC     $7CE4               
9C06: 18              CLC                         
9C07: 21 00           AND     ($00,X)             ; {ram.GP_00}
9C09: 00              BRK                         
9C0A: 00              BRK                         
9C0B: 00              BRK                         
9C0C: 00              BRK                         
9C0D: 00              BRK                         
9C0E: 00              BRK                         
9C0F: 00              BRK                         
9C10: FF ; ????
9C11: FF ; ????
9C12: FF ; ????
9C13: FF ; ????
9C14: FF ; ????
9C15: FF ; ????
9C16: FF ; ????
9C17: FF ; ????
9C18: 00              BRK                         
9C19: 00              BRK                         
9C1A: 00              BRK                         
9C1B: 00              BRK                         
9C1C: 00              BRK                         
9C1D: 00              BRK                         
9C1E: 00              BRK                         
9C1F: 00              BRK                         
9C20: 01 01           ORA     ($01,X)             
9C22: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9C24: 01 02           ORA     ($02,X)             
9C26: 04 ; ????
9C27: 0C ; ????
9C28: 01 01           ORA     ($01,X)             
9C2A: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9C2C: 01 03           ORA     ($03,X)             
9C2E: 07 ; ????
9C2F: 0F ; ????
9C30: 5F ; ????
9C31: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9C33: 00              BRK                         
9C34: F8              SED                         
9C35: 07 ; ????
9C36: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9C38: FF ; ????
9C39: FF ; ????
9C3A: FF ; ????
9C3B: 13 ; ????
9C3C: F8              SED                         
9C3D: FF ; ????
9C3E: FF ; ????
9C3F: FF ; ????
9C40: FF ; ????
9C41: FF ; ????
9C42: FF ; ????
9C43: 5F ; ????
9C44: 07 ; ????
9C45: 80 ; ????
9C46: FC ; ????
9C47: 03 ; ????
9C48: FF ; ????
9C49: FF ; ????
9C4A: FF ; ????
9C4B: FF ; ????
9C4C: 3F ; ????
9C4D: 81 FC           STA     ($FC,X)             
9C4F: FF ; ????
9C50: 08              PHP                         
9C51: 0C ; ????
9C52: 08              PHP                         
9C53: 08              PHP                         
9C54: 0C ; ????
9C55: 06 03           ASL     $03                 
9C57: 00              BRK                         
9C58: 0F ; ????
9C59: 0F ; ????
9C5A: 0F ; ????
9C5B: 0F ; ????
9C5C: 0F ; ????
9C5D: 07 ; ????
9C5E: 03 ; ????
9C5F: 00              BRK                         
9C60: 00              BRK                         
9C61: 00              BRK                         
9C62: 40              RTI                         
9C63: 02 ; ????
9C64: 35 FF           AND     $FF,X               
9C66: 00              BRK                         
9C67: 00              BRK                         
9C68: FF ; ????
9C69: FF ; ????
9C6A: FF ; ????
9C6B: FF ; ????
9C6C: FF ; ????
9C6D: FF ; ????
9C6E: 00              BRK                         
9C6F: 00              BRK                         
9C70: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9C72: 02 ; ????
9C73: 08              PHP                         
9C74: FF ; ????
9C75: F7 ; ????
9C76: 02 ; ????
9C77: 00              BRK                         
9C78: FF ; ????
9C79: FF ; ????
9C7A: FF ; ????
9C7B: FF ; ????
9C7C: FF ; ????
9C7D: F7 ; ????
9C7E: 02 ; ????
9C7F: 00              BRK                         
9C80: E7 ; ????
9C81: 7B ; ????
9C82: 0B ; ????
9C83: 0D 07 F1        ORA     $F107               
9C86: 39 06 E7        AND     $E706,Y             
9C89: FB ; ????
9C8A: FB ; ????
9C8B: FD FF FF        SBC     $FFFF,X             
9C8E: 3F ; ????
9C8F: 07 ; ????
9C90: 00              BRK                         
9C91: 01 03           ORA     ($03,X)             
9C93: 07 ; ????
9C94: 07 ; ????
9C95: 0F ; ????
9C96: 0F ; ????
9C97: 0C ; ????
9C98: 00              BRK                         
9C99: 00              BRK                         
9C9A: 00              BRK                         
9C9B: 00              BRK                         
9C9C: 00              BRK                         
9C9D: 00              BRK                         
9C9E: 00              BRK                         
9C9F: 00              BRK                         
9CA0: 00              BRK                         
9CA1: E0 F8           CPX     #$F8                
9CA3: FC ; ????
9CA4: FE FF FF        INC     $FFFF,X             
9CA7: FF ; ????
9CA8: F0 1E           BEQ     $9CC8               ; {}
9CAA: 07 ; ????
9CAB: 03 ; ????
9CAC: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9CAE: 00              BRK                         
9CAF: 00              BRK                         
9CB0: 57 ; ????
9CB1: 06 01           ASL     $01                 
9CB3: 02 ; ????
9CB4: 00              BRK                         
9CB5: 01 80           ORA     ($80,X)             
9CB7: 80 ; ????
9CB8: 57 ; ????
9CB9: 06 81           ASL     $81                 
9CBB: E2 ; ????
9CBC: F0 F9           BEQ     $9CB7               ; {}
9CBE: 7C ; ????
9CBF: 7C ; ????
9CC0: 08              PHP                         
9CC1: 18              CLC                         
9CC2: 10 10           BPL     $9CD4               ; {}
9CC4: 10 14           BPL     $9CDA               ; {}
9CC6: 14 ; ????
9CC7: 14 ; ????
9CC8: 00              BRK                         
9CC9: 00              BRK                         
9CCA: 00              BRK                         
9CCB: 00              BRK                         
9CCC: 00              BRK                         
9CCD: 02 ; ????
9CCE: 02 ; ????
9CCF: 02 ; ????
9CD0: 7F ; ????
9CD1: 3F ; ????
9CD2: 3F ; ????
9CD3: 1F ; ????
9CD4: 1F ; ????
9CD5: 1F ; ????
9CD6: 1F ; ????
9CD7: 1F ; ????
9CD8: 00              BRK                         
9CD9: 00              BRK                         
9CDA: 00              BRK                         
9CDB: 00              BRK                         
9CDC: 00              BRK                         
9CDD: 00              BRK                         
9CDE: 00              BRK                         
9CDF: 00              BRK                         
9CE0: 00              BRK                         
9CE1: 00              BRK                         
9CE2: 00              BRK                         
9CE3: 00              BRK                         
9CE4: 00              BRK                         
9CE5: 00              BRK                         
9CE6: 00              BRK                         
9CE7: 00              BRK                         
9CE8: 10 10           BPL     $9CFA               ; {}
9CEA: 38              SEC                         
9CEB: FE 7C 38        INC     $387C,X             
9CEE: 6C 44 10        JMP     ($1044)             
9CF1: 10 14           BPL     $9D07               ; {}
9CF3: 10 10           BPL     $9D05               ; {}
9CF5: 10 18           BPL     $9D0F               ; {}
9CF7: 18              CLC                         
9CF8: 00              BRK                         
9CF9: 00              BRK                         
9CFA: 00              BRK                         
9CFB: 00              BRK                         
9CFC: 00              BRK                         
9CFD: 00              BRK                         
9CFE: 00              BRK                         
9CFF: 00              BRK                         
9D00: 1F ; ????
9D01: 1F ; ????
9D02: 1F ; ????
9D03: 1F ; ????
9D04: 1F ; ????
9D05: 3F ; ????
9D06: 3F ; ????
9D07: 7F ; ????
9D08: 00              BRK                         
9D09: 00              BRK                         
9D0A: 00              BRK                         
9D0B: 00              BRK                         
9D0C: 00              BRK                         
9D0D: 00              BRK                         
9D0E: 00              BRK                         
9D0F: 00              BRK                         
9D10: E0 E0           CPX     #$E0                
9D12: E0 E0           CPX     #$E0                
9D14: E0 E0           CPX     #$E0                
9D16: E0 E0           CPX     #$E0                
9D18: 1E 1E 1E        ASL     $1E1E,X             
9D1B: 1E 1E 1E        ASL     $1E1E,X             
9D1E: 1E 1E 1C        ASL     $1C1E,X             
9D21: 0F ; ????
9D22: 0F ; ????
9D23: 07 ; ????
9D24: 07 ; ????
9D25: 03 ; ????
9D26: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9D28: 00              BRK                         
9D29: 00              BRK                         
9D2A: 00              BRK                         
9D2B: 00              BRK                         
9D2C: 00              BRK                         
9D2D: 00              BRK                         
9D2E: 00              BRK                         
9D2F: 00              BRK                         
9D30: E0 C0           CPX     #$C0                
9D32: C0 C1           CPY     #$C1                
9D34: C1 87           CMP     ($87,X)             
9D36: 02 ; ????
9D37: 17 ; ????
9D38: 1E 3C 3C        ASL     $3C3C,X             
9D3B: 39 39 77        AND     $7739,Y             
9D3E: E2 ; ????
9D3F: 97 ; ????
9D40: 06 09           ASL     $09                 
9D42: 16 21           ASL     $21,X               
9D44: 23 ; ????
9D45: 41 45           EOR     ($45,X)             
9D47: 83 ; ????
9D48: 07 ; ????
9D49: 0F ; ????
9D4A: 1F ; ????
9D4B: 3F ; ????
9D4C: 3F ; ????
9D4D: 7F ; ????
9D4E: 7F ; ????
9D4F: FF ; ????
9D50: FF ; ????
9D51: D1 27           CMP     ($27),Y             
9D53: 86 89           STX     $89                 
9D55: 3F ; ????
9D56: 52 ; ????
9D57: 71 FF           ADC     ($FF),Y             
9D59: FF ; ????
9D5A: FF ; ????
9D5B: FF ; ????
9D5C: FF ; ????
9D5D: FF ; ????
9D5E: FF ; ????
9D5F: FF ; ????
9D60: FF ; ????
9D61: FF ; ????
9D62: EF ; ????
9D63: 7F ; ????
9D64: D3 ; ????
9D65: FF ; ????
9D66: BA              TSX                         
9D67: EF ; ????
9D68: FF ; ????
9D69: FF ; ????
9D6A: FF ; ????
9D6B: FF ; ????
9D6C: FF ; ????
9D6D: FF ; ????
9D6E: FF ; ????
9D6F: FF ; ????
9D70: CC AB 95        CPY     $95AB               ; {}
9D73: 9E ; ????
9D74: DF ; ????
9D75: 73 ; ????
9D76: 00              BRK                         
9D77: 02 ; ????
9D78: FF ; ????
9D79: FF ; ????
9D7A: FF ; ????
9D7B: FF ; ????
9D7C: FF ; ????
9D7D: 73 ; ????
9D7E: 00              BRK                         
9D7F: 02 ; ????
9D80: A2 26           LDX     #$26                
9D82: E6 06           INC     $06                 
9D84: 0C ; ????
9D85: 38              SEC                         
9D86: 00              BRK                         
9D87: 00              BRK                         
9D88: C2 ; ????
9D89: D6 1E           DEC     $1E,X               
9D8B: DE 9C 38        DEC     $389C,X             
9D8E: 00              BRK                         
9D8F: 00              BRK                         
9D90: 81 38           STA     ($38,X)             
9D92: 7C ; ????
9D93: 7C ; ????
9D94: 7C ; ????
9D95: 7C ; ????
9D96: 7C ; ????
9D97: 78              SEI                         
9D98: 81 06           STA     ($06,X)             
9D9A: 03 ; ????
9D9B: 03 ; ????
9D9C: 03 ; ????
9D9D: 03 ; ????
9D9E: 03 ; ????
9D9F: 06 7F           ASL     $7F                 
9DA1: 46 51           LSR     $51                 
9DA3: 2D 23 16        AND     $1623               
9DA6: 13 ; ????
9DA7: 06 7F           ASL     $7F                 
9DA9: 7F ; ????
9DAA: 7F ; ????
9DAB: 3F ; ????
9DAC: 3F ; ????
9DAD: 1F ; ????
9DAE: 1F ; ????
9DAF: 07 ; ????
9DB0: 38              SEC                         
9DB1: 38              SEC                         
9DB2: B8              CLV                         
9DB3: B8              CLV                         
9DB4: B8              CLV                         
9DB5: 30 E1           BMI     $9D98               ; {}
9DB7: 03 ; ????
9DB8: 06 06           ASL     $06                 
9DBA: 86 86           STX     $86                 
9DBC: 84 0C           STY     $0C                 
9DBE: 11 03           ORA     ($03),Y             
9DC0: 05 04           ORA     $04                 
9DC2: 06 01           ASL     $01                 
9DC4: 01 01           ORA     ($01,X)             
9DC6: 00              BRK                         
9DC7: 00              BRK                         
9DC8: 07 ; ????
9DC9: 07 ; ????
9DCA: 07 ; ????
9DCB: 01 01           ORA     ($01,X)             
9DCD: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9DCF: 00              BRK                         
9DD0: FF ; ????
9DD1: E8              INX                         
9DD2: B3 ; ????
9DD3: C5 DE           CMP     $DE                 
9DD5: E7 ; ????
9DD6: DF ; ????
9DD7: 19 FF E8        ORA     $E8FF,Y             
9DDA: E0 C0           CPX     #$C0                
9DDC: C0 C0           CPY     #$C0                
9DDE: 80 ; ????
9DDF: 00              BRK                         
9DE0: 00              BRK                         
9DE1: 00              BRK                         
9DE2: 00              BRK                         
9DE3: 00              BRK                         
9DE4: 01 01           ORA     ($01,X)             
9DE6: 00              BRK                         
9DE7: 00              BRK                         
9DE8: 00              BRK                         
9DE9: 00              BRK                         
9DEA: 01 03           ORA     ($03,X)             
9DEC: 03 ; ????
9DED: 03 ; ????
9DEE: 03 ; ????
9DEF: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9DF1: 00              BRK                         
9DF2: 50 F8           BVC     $9DEC               ; {}
9DF4: 98              TYA                         
9DF5: 18              CLC                         
9DF6: B0 10           BCS     $9E08               ; {}
9DF8: 00              BRK                         
9DF9: E0 F0           CPX     #$F0                
9DFB: F8              SED                         
9DFC: F8              SED                         
9DFD: F8              SED                         
9DFE: F0 F0           BEQ     $9DF0               ; {}
9E00: 00              BRK                         
9E01: 00              BRK                         
9E02: 00              BRK                         
9E03: 00              BRK                         
9E04: 00              BRK                         
9E05: 00              BRK                         
9E06: 00              BRK                         
9E07: 02 ; ????
9E08: 00              BRK                         
9E09: 00              BRK                         
9E0A: 00              BRK                         
9E0B: 01 07           ORA     ($07,X)             
9E0D: 0F ; ????
9E0E: 0F ; ????
9E0F: 1F ; ????
9E10: 30 60           BMI     $9E72               ; {}
9E12: 3C ; ????
9E13: 0E 07 03        ASL     $0307               
9E16: 03 ; ????
9E17: 22 ; ????
9E18: F0 E0           BEQ     $9DFA               ; {}
9E1A: FC ; ????
9E1B: FE FF FF        INC     $FFFF,X             
9E1E: FF ; ????
9E1F: FE 03 03        INC     $0303,X             
9E22: 03 ; ????
9E23: 0E 1C 00        ASL     $001C               
9E26: 00              BRK                         
9E27: 00              BRK                         
9E28: 1F ; ????
9E29: 1F ; ????
9E2A: 1F ; ????
9E2B: 1F ; ????
9E2C: 1F ; ????
9E2D: 03 ; ????
9E2E: 03 ; ????
9E2F: 03 ; ????
9E30: 26 DC           ROL     $DC                 
9E32: 8C 08 08        STY     $0808               
9E35: 08              PHP                         
9E36: 0C ; ????
9E37: 2C FE FC        BIT     $FCFE               
9E3A: FC ; ????
9E3B: F8              SED                         
9E3C: F8              SED                         
9E3D: F8              SED                         
9E3E: FC ; ????
9E3F: FC ; ????
9E40: 00              BRK                         
9E41: 00              BRK                         
9E42: 00              BRK                         
9E43: 00              BRK                         
9E44: 03 ; ????
9E45: 07 ; ????
9E46: 0F ; ????
9E47: 0F ; ????
9E48: 07 ; ????
9E49: 07 ; ????
9E4A: 07 ; ????
9E4B: 0F ; ????
9E4C: 0F ; ????
9E4D: 0F ; ????
9E4E: 0F ; ????
9E4F: 0F ; ????
9E50: 0C ; ????
9E51: 16 2E           ASL     $2E,X               
9E53: EE CC DC        INC     $DCCC               
9E56: A4 A8           LDY     $A8                 
9E58: FC ; ????
9E59: FE FE FE        INC     $FEFE,X             
9E5C: FC ; ????
9E5D: FC ; ????
9E5E: FC ; ????
9E5F: F8              SED                         
9E60: 0F ; ????
9E61: 07 ; ????
9E62: 04 ; ????
9E63: 04 ; ????
9E64: 00              BRK                         
9E65: 01 03           ORA     ($03,X)             
9E67: 03 ; ????
9E68: 0F ; ????
9E69: 0F ; ????
9E6A: 0F ; ????
9E6B: 0F ; ????
9E6C: 0F ; ????
9E6D: 07 ; ????
9E6E: 07 ; ????
9E6F: 07 ; ????
9E70: 6C 6C 68        JMP     ($686C)             
9E73: E8              INX                         
9E74: C8              INY                         
9E75: C8              INY                         
9E76: D8              CLD                         
9E77: 9C ; ????
9E78: FC ; ????
9E79: FC ; ????
9E7A: F8              SED                         
9E7B: F8              SED                         
9E7C: F8              SED                         
9E7D: F8              SED                         
9E7E: F8              SED                         
9E7F: FC ; ????
9E80: 03 ; ????
9E81: 03 ; ????
9E82: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9E84: 00              BRK                         
9E85: 00              BRK                         
9E86: 01 03           ORA     ($03,X)             
9E88: 07 ; ????
9E89: 03 ; ????
9E8A: 03 ; ????
9E8B: 01 01           ORA     ($01,X)             
9E8D: 01 03           ORA     ($03,X)             
9E8F: 03 ; ????
9E90: 9C ; ????
9E91: 1C ; ????
9E92: 1C ; ????
9E93: 1E 1E BE        ASL     $BE1E,X             ; {}
9E96: 76 20           ROR     $20,X               
9E98: FC ; ????
9E99: FC ; ????
9E9A: FC ; ????
9E9B: FE FE FE        INC     $FEFE,X             
9E9E: F6 20           INC     $20,X               
9EA0: 3E 7F E0        ROL     $E07F,X             
9EA3: C0 4F           CPY     #$4F                
9EA5: 08              PHP                         
9EA6: 0A              ASL     A                   
9EA7: 4B ; ????
9EA8: 00              BRK                         
9EA9: 00              BRK                         
9EAA: 1F ; ????
9EAB: 3F ; ????
9EAC: 3F ; ????
9EAD: 3F ; ????
9EAE: 1F ; ????
9EAF: 3F ; ????
9EB0: 18              CLC                         
9EB1: 3C ; ????
9EB2: 0E 06 E6        ASL     $E606               
9EB5: 26 A4           ROL     $A4                 
9EB7: A0 00           LDY     #$00                
9EB9: 00              BRK                         
9EBA: BE FE FE        LDX     $FEFE,Y             
9EBD: DE DC D8        DEC     $D8DC,X             
9EC0: CA              DEX                         
9EC1: C8              INY                         
9EC2: CF ; ????
9EC3: C0 E0           CPY     #$E0                
9EC5: 77 ; ????
9EC6: 00              BRK                         
9EC7: 00              BRK                         
9EC8: 3F ; ????
9EC9: 3F ; ????
9ECA: 30 3F           BMI     $9F0B               ; {}
9ECC: 3F ; ????
9ECD: 37 ; ????
9ECE: 00              BRK                         
9ECF: 00              BRK                         
9ED0: F0 FC           BEQ     $9ECE               ; {}
9ED2: FF ; ????
9ED3: FF ; ????
9ED4: FF ; ????
9ED5: FF ; ????
9ED6: FF ; ????
9ED7: FF ; ????
9ED8: 00              BRK                         
9ED9: 00              BRK                         
9EDA: 00              BRK                         
9EDB: 00              BRK                         
9EDC: 00              BRK                         
9EDD: 00              BRK                         
9EDE: 00              BRK                         
9EDF: 00              BRK                         
9EE0: 00              BRK                         
9EE1: 00              BRK                         
9EE2: 00              BRK                         
9EE3: 87 ; ????
9EE4: DF ; ????
9EE5: CF ; ????
9EE6: EF ; ????
9EE7: E7 ; ????
9EE8: 00              BRK                         
9EE9: 00              BRK                         
9EEA: 00              BRK                         
9EEB: 00              BRK                         
9EEC: 00              BRK                         
9EED: 00              BRK                         
9EEE: 00              BRK                         
9EEF: 00              BRK                         
9EF0: 00              BRK                         
9EF1: 00              BRK                         
9EF2: 01 C3           ORA     ($C3,X)             
9EF4: E7 ; ????
9EF5: F7 ; ????
9EF6: F7 ; ????
9EF7: F7 ; ????
9EF8: 00              BRK                         
9EF9: 00              BRK                         
9EFA: 00              BRK                         
9EFB: 00              BRK                         
9EFC: 00              BRK                         
9EFD: 00              BRK                         
9EFE: 00              BRK                         
9EFF: 00              BRK                         
9F00: 1F ; ????
9F01: FF ; ????
9F02: FF ; ????
9F03: FF ; ????
9F04: FF ; ????
9F05: FF ; ????
9F06: FF ; ????
9F07: FF ; ????
9F08: 00              BRK                         
9F09: 00              BRK                         
9F0A: 00              BRK                         
9F0B: 00              BRK                         
9F0C: 00              BRK                         
9F0D: 00              BRK                         
9F0E: 00              BRK                         
9F0F: 00              BRK                         
9F10: FF ; ????
9F11: FF ; ????
9F12: FF ; ????
9F13: FF ; ????
9F14: FF ; ????
9F15: FF ; ????
9F16: FF ; ????
9F17: FF ; ????
9F18: 00              BRK                         
9F19: 00              BRK                         
9F1A: 00              BRK                         
9F1B: 00              BRK                         
9F1C: 00              BRK                         
9F1D: 00              BRK                         
9F1E: 00              BRK                         
9F1F: 00              BRK                         
9F20: F3 ; ????
9F21: FB ; ????
9F22: FB ; ????
9F23: FB ; ????
9F24: FF ; ????
9F25: FF ; ????
9F26: FF ; ????
9F27: FF ; ????
9F28: 00              BRK                         
9F29: 00              BRK                         
9F2A: 00              BRK                         
9F2B: 00              BRK                         
9F2C: 00              BRK                         
9F2D: 00              BRK                         
9F2E: 00              BRK                         
9F2F: 00              BRK                         
9F30: 07 ; ????
9F31: 1F ; ????
9F32: 3F ; ????
9F33: 7F ; ????
9F34: 7F ; ????
9F35: 7F ; ????
9F36: FF ; ????
9F37: FF ; ????
9F38: 00              BRK                         
9F39: 00              BRK                         
9F3A: 00              BRK                         
9F3B: 00              BRK                         
9F3C: 00              BRK                         
9F3D: 00              BRK                         
9F3E: 00              BRK                         
9F3F: 00              BRK                         
9F40: E0 F8           CPX     #$F8                
9F42: FC ; ????
9F43: FE FE FE        INC     $FEFE,X             
9F46: FF ; ????
9F47: FF ; ????
9F48: 00              BRK                         
9F49: 00              BRK                         
9F4A: 00              BRK                         
9F4B: 00              BRK                         
9F4C: 00              BRK                         
9F4D: 00              BRK                         
9F4E: 00              BRK                         
9F4F: 00              BRK                         
9F50: 00              BRK                         
9F51: 00              BRK                         
9F52: 00              BRK                         
9F53: 00              BRK                         
9F54: 00              BRK                         
9F55: 00              BRK                         
9F56: 00              BRK                         
9F57: 00              BRK                         
9F58: 00              BRK                         
9F59: 00              BRK                         
9F5A: 00              BRK                         
9F5B: 00              BRK                         
9F5C: 00              BRK                         
9F5D: 00              BRK                         
9F5E: 00              BRK                         
9F5F: 00              BRK                         
9F60: 00              BRK                         
9F61: 00              BRK                         
9F62: 00              BRK                         
9F63: 00              BRK                         
9F64: 00              BRK                         
9F65: 00              BRK                         
9F66: 00              BRK                         
9F67: 00              BRK                         
9F68: 00              BRK                         
9F69: 00              BRK                         
9F6A: 00              BRK                         
9F6B: 00              BRK                         
9F6C: 00              BRK                         
9F6D: 00              BRK                         
9F6E: 00              BRK                         
9F6F: 00              BRK                         
9F70: 00              BRK                         
9F71: 00              BRK                         
9F72: 00              BRK                         
9F73: 00              BRK                         
9F74: 00              BRK                         
9F75: 00              BRK                         
9F76: 00              BRK                         
9F77: 00              BRK                         
9F78: 00              BRK                         
9F79: 00              BRK                         
9F7A: 00              BRK                         
9F7B: 00              BRK                         
9F7C: 00              BRK                         
9F7D: 00              BRK                         
9F7E: 00              BRK                         
9F7F: 00              BRK                         
9F80: 00              BRK                         
9F81: 00              BRK                         
9F82: 00              BRK                         
9F83: 00              BRK                         
9F84: 00              BRK                         
9F85: 00              BRK                         
9F86: 00              BRK                         
9F87: 00              BRK                         
9F88: 00              BRK                         
9F89: 00              BRK                         
9F8A: 00              BRK                         
9F8B: 00              BRK                         
9F8C: 00              BRK                         
9F8D: 00              BRK                         
9F8E: 00              BRK                         
9F8F: 00              BRK                         
9F90: 00              BRK                         
9F91: 00              BRK                         
9F92: 00              BRK                         
9F93: 00              BRK                         
9F94: 00              BRK                         
9F95: 00              BRK                         
9F96: 00              BRK                         
9F97: 00              BRK                         
9F98: 00              BRK                         
9F99: 00              BRK                         
9F9A: 00              BRK                         
9F9B: 00              BRK                         
9F9C: 00              BRK                         
9F9D: 00              BRK                         
9F9E: 00              BRK                         
9F9F: 00              BRK                         
9FA0: 00              BRK                         
9FA1: 00              BRK                         
9FA2: 00              BRK                         
9FA3: 00              BRK                         
9FA4: 00              BRK                         
9FA5: 00              BRK                         
9FA6: 00              BRK                         
9FA7: 00              BRK                         
9FA8: 00              BRK                         
9FA9: 00              BRK                         
9FAA: 00              BRK                         
9FAB: 00              BRK                         
9FAC: 00              BRK                         
9FAD: 00              BRK                         
9FAE: 00              BRK                         
9FAF: 00              BRK                         
9FB0: 00              BRK                         
9FB1: 00              BRK                         
9FB2: 00              BRK                         
9FB3: 00              BRK                         
9FB4: 00              BRK                         
9FB5: 00              BRK                         
9FB6: 00              BRK                         
9FB7: 00              BRK                         
9FB8: 00              BRK                         
9FB9: 00              BRK                         
9FBA: 00              BRK                         
9FBB: 00              BRK                         
9FBC: 00              BRK                         
9FBD: 00              BRK                         
9FBE: 00              BRK                         
9FBF: 00              BRK                         
9FC0: 00              BRK                         
9FC1: 00              BRK                         
9FC2: 00              BRK                         
9FC3: 00              BRK                         
9FC4: 00              BRK                         
9FC5: 00              BRK                         
9FC6: 00              BRK                         
9FC7: 00              BRK                         
9FC8: 00              BRK                         
9FC9: 00              BRK                         
9FCA: 00              BRK                         
9FCB: 00              BRK                         
9FCC: 00              BRK                         
9FCD: 00              BRK                         
9FCE: 00              BRK                         
9FCF: 00              BRK                         
9FD0: 00              BRK                         
9FD1: 00              BRK                         
9FD2: 00              BRK                         
9FD3: 00              BRK                         
9FD4: 00              BRK                         
9FD5: 00              BRK                         
9FD6: 00              BRK                         
9FD7: 00              BRK                         
9FD8: 00              BRK                         
9FD9: 00              BRK                         
9FDA: 00              BRK                         
9FDB: 00              BRK                         
9FDC: 00              BRK                         
9FDD: 00              BRK                         
9FDE: 00              BRK                         
9FDF: 00              BRK                         
9FE0: 00              BRK                         
9FE1: 00              BRK                         
9FE2: 00              BRK                         
9FE3: 00              BRK                         
9FE4: 00              BRK                         
9FE5: 00              BRK                         
9FE6: 00              BRK                         
9FE7: 00              BRK                         
9FE8: 00              BRK                         
9FE9: 00              BRK                         
9FEA: 00              BRK                         
9FEB: 00              BRK                         
9FEC: 00              BRK                         
9FED: 00              BRK                         
9FEE: 00              BRK                         
9FEF: 00              BRK                         
9FF0: 00              BRK                         
9FF1: 00              BRK                         
9FF2: 00              BRK                         
9FF3: 00              BRK                         
9FF4: 00              BRK                         
9FF5: 00              BRK                         
9FF6: 00              BRK                         
9FF7: 00              BRK                         
9FF8: 00              BRK                         
9FF9: 00              BRK                         
9FFA: 00              BRK                         
9FFB: 00              BRK                         
9FFC: 00              BRK                         
9FFD: 00              BRK                         
9FFE: 00              BRK                         
9FFF: 00              BRK                         
A000: 4C 5A A0        JMP     $A05A               ; {}
A003: 4C 54 A5        JMP     $A554               ; {}
A006: 4C 47 AD        JMP     $AD47               ; {}
A009: 4C 40 DF        JMP     $DF40               
A00C: 4C 47 AD        JMP     $AD47               ; {}
A00F: 4C 47 AD        JMP     $AD47               ; {}
A012: 4C 47 AD        JMP     $AD47               ; {}
A015: 4C 47 AD        JMP     $AD47               ; {}
A018: 4C 47 AD        JMP     $AD47               ; {}
A01B: 4C 47 AD        JMP     $AD47               ; {}
A01E: 4C 47 AD        JMP     $AD47               ; {}
A021: 4C 47 AD        JMP     $AD47               ; {}
A024: 4C 47 AD        JMP     $AD47               ; {}
A027: 4C 47 AD        JMP     $AD47               ; {}
A02A: 4C 47 AD        JMP     $AD47               ; {}
A02D: 4C 47 AD        JMP     $AD47               ; {}
A030: 4C 47 AD        JMP     $AD47               ; {}
A033: 4C 47 AD        JMP     $AD47               ; {}
A036: 4C 47 AD        JMP     $AD47               ; {}
A039: 4C 47 AD        JMP     $AD47               ; {}
A03C: 4C 47 AD        JMP     $AD47               ; {}
A03F: 4C 47 AD        JMP     $AD47               ; {}
A042: 67 ; ????
A043: C5 E7           CMP     $E7                 
A045: C5 47           CMP     $47                 
A047: AD 47 AD        LDA     $AD47               ; {}
A04A: 47 ; ????
A04B: AD 47 AD        LDA     $AD47               ; {}
A04E: 47 ; ????
A04F: AD 47 AD        LDA     $AD47               ; {}
A052: 47 ; ????
A053: AD 47 AD        LDA     $AD47               ; {}
A056: 47 ; ????
A057: AD 47 AD        LDA     $AD47               ; {}
A05A: A2 00           LDX     #$00                
A05C: BD 81 F0        LDA     $F081,X             
A05F: 9D 00 60        STA     $6000,X             
A062: E8              INX                         
A063: D0 F7           BNE     $A05C               ; {}
A065: 20 53 A5        JSR     $A553               ; {}
A068: 20 F0 EE        JSR     $EEF0               
A06B: 20 07 EB        JSR     $EB07               
A06E: A5 A0           LDA     $A0                 
A070: C9 01           CMP     #$01                
A072: F0 51           BEQ     $A0C5               ; {}
A074: A9 10           LDA     #$10                
A076: 85 85           STA     $85                 
A078: 20 E5 EE        JSR     $EEE5               
A07B: A9 00           LDA     #$00                
A07D: 85 A0           STA     $A0                 
A07F: 85 18           STA     $18                 
A081: 8D 00 06        STA     $0600               
A084: E6 1A           INC     $1A                 
A086: 20 F9 E3        JSR     $E3F9               
A089: 20 36 A2        JSR     $A236               ; {}
A08C: A9 00           LDA     #$00                
A08E: 20 00 A7        JSR     $A700               ; {}
A091: 20 1D A7        JSR     $A71D               ; {}
A094: 20 C4 A5        JSR     $A5C4               ; {}
A097: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
A09A: 10 FB           BPL     $A097               ; {}
A09C: 20 2E EB        JSR     $EB2E               
A09F: 20 42 EE        JSR     $EE42               
A0A2: 20 01 EF        JSR     $EF01               
A0A5: A5 1A           LDA     $1A                 
A0A7: 6A              ROR     A                   
A0A8: 90 0A           BCC     $A0B4               ; {}
A0AA: AD 8D 03        LDA     $038D               
A0AD: D0 05           BNE     $A0B4               ; {}
A0AF: A9 10           LDA     #$10                
A0B1: 8D 84 03        STA     $0384               
A0B4: A5 18           LDA     $18                 
A0B6: 29 10           AND     #$10                
A0B8: F0 EB           BEQ     $A0A5               ; {}
A0BA: A9 01           LDA     #$01                
A0BC: 8D 80 03        STA     $0380               
A0BF: 20 56 C8        JSR     $C856               
A0C2: 4C 6A A1        JMP     $A16A               ; {}
A0C5: A9 00           LDA     #$00                
A0C7: 85 AD           STA     $AD                 
A0C9: 85 AE           STA     $AE                 
A0CB: 20 77 EF        JSR     $EF77               
A0CE: A9 20           LDA     #$20                
A0D0: 85 85           STA     $85                 
A0D2: 20 E5 EE        JSR     $EEE5               
A0D5: E6 1A           INC     $1A                 
A0D7: 20 F9 E3        JSR     $E3F9               
A0DA: A9 01           LDA     #$01                
A0DC: 20 00 A7        JSR     $A700               ; {}
A0DF: 20 1D A7        JSR     $A71D               ; {}
A0E2: 20 5B A7        JSR     $A75B               ; {}
A0E5: A9 01           LDA     #$01                
A0E7: 85 B1           STA     $B1                 
A0E9: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
A0EC: 10 FB           BPL     $A0E9               ; {}
A0EE: 20 2E EB        JSR     $EB2E               
A0F1: 20 42 EE        JSR     $EE42               
A0F4: 20 01 EF        JSR     $EF01               
A0F7: A5 00           LDA     $00                 ; {ram.GP_00}
A0F9: A5 B1           LDA     $B1                 
A0FB: D0 FA           BNE     $A0F7               ; {}
A0FD: 20 F0 EE        JSR     $EEF0               
A100: A5 B2           LDA     $B2                 
A102: 20 2B EE        JSR     $EE2B               
A105: 09 A1           ORA     #$A1                
A107: 71 A1           ADC     ($A1),Y             
A109: A9 00           LDA     #$00                
A10B: 85 B2           STA     $B2                 
A10D: 20 E7 A1        JSR     $A1E7               ; {}
A110: A5 B2           LDA     $B2                 
A112: AA              TAX                         
A113: 85 AF           STA     $AF                 
A115: 18              CLC                         
A116: A9 05           LDA     #$05                
A118: 7D 6E A1        ADC     $A16E,X             ; {}
A11B: 85 08           STA     $08                 
A11D: A9 60           LDA     #$60                
A11F: 69 00           ADC     #$00                
A121: 85 09           STA     $09                 
A123: A0 07           LDY     #$07                
A125: B1 08           LDA     ($08),Y             
A127: 99 20 01        STA     $0120,Y             
A12A: 88              DEY                         
A12B: 10 F8           BPL     $A125               ; {}
A12D: 18              CLC                         
A12E: A9 0D           LDA     #$0D                
A130: 7D 6E A1        ADC     $A16E,X             ; {}
A133: 85 08           STA     $08                 
A135: A9 60           LDA     #$60                
A137: 69 00           ADC     #$00                
A139: 85 09           STA     $09                 
A13B: A0 1C           LDY     #$1C                
A13D: B1 08           LDA     ($08),Y             
A13F: 8D 30 01        STA     $0130               
A142: 88              DEY                         
A143: B1 08           LDA     ($08),Y             
A145: 85 A0           STA     $A0                 
A147: 88              DEY                         
A148: A9 0F           LDA     #$0F                
A14A: 85 A6           STA     $A6                 
A14C: 8D 71 01        STA     $0171               
A14F: 88              DEY                         
A150: B1 08           LDA     ($08),Y             
A152: 85 AA           STA     $AA                 
A154: 8D 70 01        STA     $0170               
A157: 88              DEY                         
A158: B1 08           LDA     ($08),Y             
A15A: 99 3E 01        STA     $013E,Y             
A15D: 99 57 01        STA     $0157,Y             
A160: 88              DEY                         
A161: 10 F5           BPL     $A158               ; {}
A163: A9 00           LDA     #$00                
A165: 85 38           STA     $38                 
A167: 4C 6D C0        JMP     $C06D               
A16A: E6 A0           INC     $A0                 
A16C: D0 F5           BNE     $A163               ; {}
A16E: 00              BRK                         
A16F: 27 ; ????
A170: 4E A9 03        LSR     $03A9               
A173: 85 B2           STA     $B2                 
A175: A5 B2           LDA     $B2                 
A177: 38              SEC                         
A178: E9 03           SBC     #$03                
A17A: 8D 00 61        STA     $6100               
A17D: 20 26 A8        JSR     $A826               ; {}
A180: A9 02           LDA     #$02                
A182: 85 B1           STA     $B1                 
A184: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
A187: 10 FB           BPL     $A184               ; {}
A189: 20 42 EE        JSR     $EE42               
A18C: 20 01 EF        JSR     $EF01               
A18F: A5 00           LDA     $00                 ; {ram.GP_00}
A191: A5 B1           LDA     $B1                 
A193: D0 FA           BNE     $A18F               ; {}
A195: 20 F0 EE        JSR     $EEF0               
A198: 20 C6 AB        JSR     $ABC6               ; {}
A19B: D0 03           BNE     $A1A0               ; {}
A19D: 4C 09 A1        JMP     $A109               ; {}
A1A0: 20 4D AC        JSR     $AC4D               ; {}
A1A3: A9 00           LDA     #$00                
A1A5: 85 14           STA     $14                 
A1A7: 85 15           STA     $15                 
A1A9: 85 85           STA     $85                 
A1AB: A9 08           LDA     #$08                
A1AD: 8D 84 03        STA     $0384               
A1B0: A9 00           LDA     #$00                
A1B2: 85 1A           STA     $1A                 
A1B4: A9 08           LDA     #$08                
A1B6: 85 FF           STA     $FF                 
A1B8: 20 C9 EB        JSR     $EBC9               
A1BB: 20 01 EF        JSR     $EF01               
A1BE: A5 14           LDA     $14                 
A1C0: C9 80           CMP     #$80                
A1C2: 90 FA           BCC     $A1BE               ; {}
A1C4: 20 F0 EE        JSR     $EEF0               
A1C7: AD 00 01        LDA     $0100               
A1CA: 29 FC           AND     #$FC                
A1CC: 8D 00 01        STA     $0100               
A1CF: A9 1E           LDA     #$1E                
A1D1: 85 FF           STA     $FF                 
A1D3: A9 20           LDA     #$20                
A1D5: 85 85           STA     $85                 
A1D7: A9 01           LDA     #$01                
A1D9: 85 1A           STA     $1A                 
A1DB: 4C 80 A1        JMP     $A180               ; {}
A1DE: A0 44           LDY     #$44                
A1E0: 88              DEY                         
A1E1: D0 FD           BNE     $A1E0               ; {}
A1E3: CA              DEX                         
A1E4: D0 F8           BNE     $A1DE               ; {}
A1E6: 60              RTS                         
A1E7: A9 00           LDA     #$00                
A1E9: A6 B2           LDX     $B2                 
A1EB: 18              CLC                         
A1EC: 7D 6E A1        ADC     $A16E,X             ; {}
A1EF: AA              TAX                         
A1F0: BD 28 60        LDA     $6028,X             
A1F3: C9 02           CMP     #$02                
A1F5: D0 11           BNE     $A208               ; {}
A1F7: BD 29 60        LDA     $6029,X             
A1FA: D0 0C           BNE     $A208               ; {}
A1FC: A9 00           LDA     #$00                
A1FE: A8              TAY                         
A1FF: 9D 0D 60        STA     $600D,X             
A202: E8              INX                         
A203: C8              INY                         
A204: C0 1A           CPY     #$1A                
A206: D0 F7           BNE     $A1FF               ; {}
A208: 60              RTS                         
A209: A5 14           LDA     $14                 
A20B: 29 01           AND     #$01                
A20D: F0 01           BEQ     $A210               ; {}
A20F: 60              RTS                         
A210: A5 15           LDA     $15                 
A212: D0 06           BNE     $A21A               ; {}
A214: A5 14           LDA     $14                 
A216: C9 80           CMP     #$80                
A218: 90 1B           BCC     $A235               ; {}
A21A: E6 FD           INC     $FD                 
A21C: 20 CA A5        JSR     $A5CA               ; {}
A21F: A5 FD           LDA     $FD                 
A221: C9 F0           CMP     #$F0                
A223: D0 10           BNE     $A235               ; {}
A225: A9 00           LDA     #$00                
A227: 85 14           STA     $14                 
A229: 85 15           STA     $15                 
A22B: A5 1A           LDA     $1A                 
A22D: 49 01           EOR     #$01                
A22F: 85 1A           STA     $1A                 
A231: A9 00           LDA     #$00                
A233: 85 FD           STA     $FD                 
A235: 60              RTS                         
A236: 20 77 EF        JSR     $EF77               
A239: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
A23C: A9 23           LDA     #$23                
A23E: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
A241: A9 C0           LDA     #$C0                
A243: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
A246: A0 3F           LDY     #$3F                
A248: A9 AA           LDA     #$AA                
A24A: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
A24D: 88              DEY                         
A24E: 10 FA           BPL     $A24A               ; {}
A250: A9 00           LDA     #$00                
A252: 85 46           STA     $46                 
A254: 20 63 A2        JSR     $A263               ; {}
A257: 20 B3 C2        JSR     $C2B3               
A25A: E6 46           INC     $46                 
A25C: A5 46           LDA     $46                 
A25E: C9 16           CMP     #$16                
A260: D0 F2           BNE     $A254               ; {}
A262: 60              RTS                         
A263: 85 00           STA     $00                 ; {ram.GP_00}
A265: 0A              ASL     A                   
A266: 0A              ASL     A                   
A267: 18              CLC                         
A268: 65 00           ADC     $00                 ; {ram.GP_00}
A26A: AA              TAX                         
A26B: A0 00           LDY     #$00                
A26D: BD 7A A2        LDA     $A27A,X             ; {}
A270: 99 41 00        STA     $0041,Y             
A273: E8              INX                         
A274: C8              INY                         
A275: C0 05           CPY     #$05                
A277: D0 F4           BNE     $A26D               ; {}
A279: 60              RTS                         
A27A: E7 ; ????
A27B: 21 E8           AND     ($E8,X)             
A27D: A2 12           LDX     #$12                
A27F: C0 2B           CPY     #$2B                
A281: FA ; ????
A282: A2 40           LDX     #$40                
A284: 35 28           AND     $28,X               
A286: 3A ; ????
A287: A3 ; ????
A288: 04 ; ????
A289: 53 ; ????
A28A: 28              PLP                         
A28B: 3E A3 08        ROL     $08A3,X             
A28E: 72 ; ????
A28F: 28              PLP                         
A290: 4B ; ????
A291: A3 ; ????
A292: 0E 80 28        ASL     $2880               
A295: 59 A3 20        EOR     $20A3,Y             
A298: A0 28           LDY     #$28                
A29A: 79 A3 20        ADC     $20A3,Y             
A29D: C0 28           CPY     #$28                
A29F: 99 A3 05        STA     $05A3,Y             
A2A2: E0 28           CPX     #$28                
A2A4: 9E ; ????
A2A5: A3 ; ????
A2A6: 04 ; ????
A2A7: 00              BRK                         
A2A8: 29 A2           AND     #$A2                
A2AA: A3 ; ????
A2AB: 80 ; ????
A2AC: 80 ; ????
A2AD: 29 22           AND     #$22                
A2AF: A4 80           LDY     $80                 
A2B1: 0A              ASL     A                   
A2B2: 2A              ROL     A                   
A2B3: A2 A4           LDX     #$A4                
A2B5: 13 ; ????
A2B6: 2A              ROL     A                   
A2B7: 2A              ROL     A                   
A2B8: B5 A4           LDA     $A4,X               
A2BA: 13 ; ????
A2BB: 58              CLI                         
A2BC: 2A              ROL     A                   
A2BD: C8              INY                         
A2BE: A4 05           LDY     $05                 
A2C0: 79 2A CD        ADC     $CD2A,Y             
A2C3: A4 03           LDY     $03                 
A2C5: 89 ; ????
A2C6: 2A              ROL     A                   
A2C7: D0 A4           BNE     $A26D               ; {}
A2C9: 0C ; ????
A2CA: B7 ; ????
A2CB: 2A              ROL     A                   
A2CC: DC ; ????
A2CD: A4 03           LDY     $03                 
A2CF: C6 2A           DEC     $2A                 
A2D1: DF ; ????
A2D2: A4 16           LDY     $16                 
A2D4: E3 ; ????
A2D5: 2A              ROL     A                   
A2D6: F5 A4           SBC     $A4,X               
A2D8: 19 01 2B        ORA     $2B01,Y             
A2DB: 0E A5 0B        ASL     $0BA5               
A2DE: 21 2B           AND     ($2B,X)             
A2E0: 19 A5 0B        ORA     $0BA5,Y             
A2E3: 43 ; ????
A2E4: 2B ; ????
A2E5: 24 A5           BIT     $A5                 
A2E7: 05 31           ORA     $31                 
A2E9: 5D C0 64        EOR     $64C0,X             
A2EC: 12 ; ????
A2ED: C0 C3           CPY     #$C3                
A2EF: A7 ; ????
A2F0: B6 C3           LDX     $C3,Y               
A2F2: 12 ; ????
A2F3: 65 5D           ADC     $5D                 
A2F5: C3 ; ????
A2F6: C3 ; ????
A2F7: B7 ; ????
A2F8: A6 12           LDX     $12                 
A2FA: 00              BRK                         
A2FB: 00              BRK                         
A2FC: 00              BRK                         
A2FD: 00              BRK                         
A2FE: 80 ; ????
A2FF: AA              TAX                         
A300: A2 A0           LDX     #$A0                
A302: AA              TAX                         
A303: 22 ; ????
A304: 00              BRK                         
A305: 00              BRK                         
A306: 08              PHP                         
A307: 0A              ASL     A                   
A308: 0A              ASL     A                   
A309: 0A              ASL     A                   
A30A: CE FF FC        DEC     $FCFF               
A30D: F0 55           BEQ     $A364               ; {}
A30F: 55 55           EOR     $55,X               
A311: 00              BRK                         
A312: CC FF FF        CPY     $FFFF               
A315: FF ; ????
A316: FF ; ????
A317: FF ; ????
A318: FF ; ????
A319: 03 ; ????
A31A: 00              BRK                         
A31B: 00              BRK                         
A31C: 0C ; ????
A31D: 0F ; ????
A31E: 0F ; ????
A31F: 0F ; ????
A320: FF ; ????
A321: 33 ; ????
A322: 80 ; ????
A323: A0 20           LDY     #$20                
A325: 00              BRK                         
A326: 00              BRK                         
A327: 88              DEY                         
A328: A2 00           LDX     #$00                
A32A: 8A              TXA                         
A32B: AA              TAX                         
A32C: 0A              ASL     A                   
A32D: 00              BRK                         
A32E: 00              BRK                         
A32F: 00              BRK                         
A330: 00              BRK                         
A331: 00              BRK                         
A332: 00              BRK                         
A333: 00              BRK                         
A334: 00              BRK                         
A335: 00              BRK                         
A336: 00              BRK                         
A337: 00              BRK                         
A338: 00              BRK                         
A339: 00              BRK                         
A33A: 1A ; ????
A33B: 1B ; ????
A33C: 1B ; ????
A33D: 1C ; ????
A33E: 1A ; ????
A33F: 1B ; ????
A340: 0F ; ????
A341: 0F ; ????
A342: 1E 0F 1C        ASL     $1C0F,X             
A345: 1C ; ????
A346: 12 ; ????
A347: 12 ; ????
A348: 12 ; ????
A349: 12 ; ????
A34A: 12 ; ????
A34B: 1A ; ????
A34C: 0F ; ????
A34D: 1D 1E 0F        ORA     $0F1E,X             
A350: 0F ; ????
A351: 0F ; ????
A352: 0F ; ????
A353: 1E 1C 1B        ASL     $1B1C,X             
A356: 1C ; ????
A357: 1A ; ????
A358: 1B ; ????
A359: 1A ; ????
A35A: 1B ; ????
A35B: 1C ; ????
A35C: 12 ; ????
A35D: 12 ; ????
A35E: 12 ; ????
A35F: 12 ; ????
A360: 12 ; ????
A361: 12 ; ????
A362: 12 ; ????
A363: 12 ; ????
A364: 12 ; ????
A365: 12 ; ????
A366: 12 ; ????
A367: 12 ; ????
A368: 12 ; ????
A369: 12 ; ????
A36A: 12 ; ????
A36B: 17 ; ????
A36C: 18              CLC                         
A36D: 18              CLC                         
A36E: 18              CLC                         
A36F: 1D 1E 1E        ORA     $1E1E,X             
A372: 1E 19 17        ASL     $1719,X             
A375: 18              CLC                         
A376: 18              CLC                         
A377: 1D 1E 1E        ORA     $1E1E,X             
A37A: 0F ; ????
A37B: 0F ; ????
A37C: 1C ; ????
A37D: 1C ; ????
A37E: 12 ; ????
A37F: 12 ; ????
A380: 12 ; ????
A381: 12 ; ????
A382: 12 ; ????
A383: 12 ; ????
A384: 12 ; ????
A385: 12 ; ????
A386: 12 ; ????
A387: 12 ; ????
A388: 12 ; ????
A389: 12 ; ????
A38A: 12 ; ????
A38B: 12 ; ????
A38C: 12 ; ????
A38D: 12 ; ????
A38E: 12 ; ????
A38F: 17 ; ????
A390: 18              CLC                         
A391: 18              CLC                         
A392: 19 12 12        ORA     $1212,Y             
A395: 12 ; ????
A396: 12 ; ????
A397: 17 ; ????
A398: 18              CLC                         
A399: 0F ; ????
A39A: 1D 1E 1E        ORA     $1E1E,X             
A39D: 19 1E 0F        ORA     $0F1E,Y             
A3A0: 18              CLC                         
A3A1: 19 18 19        ORA     $1918,Y             
A3A4: 12 ; ????
A3A5: 12 ; ????
A3A6: 12 ; ????
A3A7: 12 ; ????
A3A8: 12 ; ????
A3A9: 12 ; ????
A3AA: 12 ; ????
A3AB: 12 ; ????
A3AC: 12 ; ????
A3AD: 12 ; ????
A3AE: 12 ; ????
A3AF: 12 ; ????
A3B0: 12 ; ????
A3B1: 12 ; ????
A3B2: 1F ; ????
A3B3: A7 ; ????
A3B4: A6 B5           LDX     $B5                 
A3B6: 9F ; ????
A3B7: 7B ; ????
A3B8: 12 ; ????
A3B9: 7B ; ????
A3BA: A7 ; ????
A3BB: A6 BF           LDX     $BF                 
A3BD: 1F ; ????
A3BE: 12 ; ????
A3BF: 12 ; ????
A3C0: 12 ; ????
A3C1: 12 ; ????
A3C2: 12 ; ????
A3C3: 12 ; ????
A3C4: 12 ; ????
A3C5: 30 0F           BMI     $A3D6               ; {}
A3C7: 32 ; ????
A3C8: 33 ; ????
A3C9: 34 ; ????
A3CA: 12 ; ????
A3CB: 12 ; ????
A3CC: 3D 5E 12        AND     $125E,X             
A3CF: 12 ; ????
A3D0: 12 ; ????
A3D1: 12 ; ????
A3D2: 1F ; ????
A3D3: 1F ; ????
A3D4: 12 ; ????
A3D5: C0 C3           CPY     #$C3                
A3D7: B7 ; ????
A3D8: B6 AF           LDX     $AF,Y               
A3DA: 12 ; ????
A3DB: 12 ; ????
A3DC: 1F ; ????
A3DD: 1F ; ????
A3DE: 12 ; ????
A3DF: 12 ; ????
A3E0: 12 ; ????
A3E1: 12 ; ????
A3E2: 12 ; ????
A3E3: 12 ; ????
A3E4: 12 ; ????
A3E5: 35 36           AND     $36,X               
A3E7: 37 ; ????
A3E8: 38              SEC                         
A3E9: 39 12 12        AND     $1212,Y             
A3EC: 5F ; ????
A3ED: 60              RTS                         
A3EE: 61 62           ADC     ($62,X)             
A3F0: 63 ; ????
A3F1: 12 ; ????
A3F2: 12 ; ????
A3F3: 1F ; ????
A3F4: 1F ; ????
A3F5: 1F ; ????
A3F6: 1F ; ????
A3F7: 1F ; ????
A3F8: 1F ; ????
A3F9: 1F ; ????
A3FA: 1F ; ????
A3FB: 1F ; ????
A3FC: 1F ; ????
A3FD: 12 ; ????
A3FE: 12 ; ????
A3FF: 12 ; ????
A400: 12 ; ????
A401: 12 ; ????
A402: 12 ; ????
A403: 12 ; ????
A404: 12 ; ????
A405: 3A ; ????
A406: 3B ; ????
A407: 3C ; ????
A408: 12 ; ????
A409: 3D 3E 3F        AND     $3F3E,X             
A40C: 66 67           ROR     $67                 
A40E: 68              PLA                         
A40F: 69 6A           ADC     #$6A                
A411: 12 ; ????
A412: 12 ; ????
A413: 12 ; ????
A414: 12 ; ????
A415: 12 ; ????
A416: 12 ; ????
A417: 12 ; ????
A418: 12 ; ????
A419: 12 ; ????
A41A: 12 ; ????
A41B: 12 ; ????
A41C: 12 ; ????
A41D: 12 ; ????
A41E: 0C ; ????
A41F: 0D 12 12        ORA     $1212               
A422: 12 ; ????
A423: 12 ; ????
A424: 12 ; ????
A425: 40              RTI                         
A426: 41 42           EOR     ($42,X)             
A428: 12 ; ????
A429: 43 ; ????
A42A: 44 ; ????
A42B: 45 6D           EOR     $6D                 
A42D: 12 ; ????
A42E: 6E 6F D0        ROR     $D06F               
A431: D1 96           CMP     ($96),Y             
A433: 8E 99 9A        STX     $9A99               ; {}
A436: 9B ; ????
A437: 9C ; ????
A438: 9D 9E 3D        STA     $3D9E,X             
A43B: A0 CA           LDY     #$CA                
A43D: CB ; ????
A43E: CC 12 12        CPY     $1212               
A441: 12 ; ????
A442: 12 ; ????
A443: 12 ; ????
A444: 46 47           LSR     $47                 
A446: 48              PHA                         
A447: 49 4A           EOR     #$4A                
A449: 4B ; ????
A44A: 4C 4D 73        JMP     $734D               
A44D: 12 ; ????
A44E: 74 ; ????
A44F: 75 87           ADC     $87,X               
A451: 86 85           STX     $85                 
A453: 79 A1 A2        ADC     $A2A1,Y             ; {}
A456: A3 ; ????
A457: A4 A5           LDY     $A5                 
A459: 70 5F           BVS     $A4BA               ; {}
A45B: A8              TAY                         
A45C: CD CE CF        CMP     $CFCE               
A45F: 12 ; ????
A460: 12 ; ????
A461: 12 ; ????
A462: 12 ; ????
A463: 12 ; ????
A464: 4E 4F 50        LSR     $504F               
A467: 51 52           EOR     ($52),Y             
A469: 53 ; ????
A46A: 54 ; ????
A46B: 55 7A           EOR     $7A,X               
A46D: 12 ; ????
A46E: 7C ; ????
A46F: 80 ; ????
A470: 7F ; ????
A471: AC 12 81        LDY     $8112               ; {}
A474: A9 AA           LDA     #$AA                
A476: AB ; ????
A477: AC AD AE        LDY     $AEAD               ; {}
A47A: AD B0 27        LDA     $27B0               
A47D: 12 ; ????
A47E: 12 ; ????
A47F: 12 ; ????
A480: 12 ; ????
A481: 12 ; ????
A482: 12 ; ????
A483: 12 ; ????
A484: 56 57           LSR     $57,X               
A486: 12 ; ????
A487: 58              CLI                         
A488: 59 5A 5B        EOR     $5B5A,Y             
A48B: 5C ; ????
A48C: 82 ; ????
A48D: 12 ; ????
A48E: 83 ; ????
A48F: 7E 78 77        ROR     $7778,X             
A492: 76 88           ROR     $88,X               
A494: B1 B2           LDA     ($B2),Y             
A496: B3 ; ????
A497: B4 6D           LDY     $6D,X               
A499: B4 6D           LDY     $6D,X               
A49B: B8              CLV                         
A49C: 28              PLP                         
A49D: 29 12           AND     #$12                
A49F: 12 ; ????
A4A0: 12 ; ????
A4A1: 12 ; ????
A4A2: 89 ; ????
A4A3: 8A              TXA                         
A4A4: 8B ; ????
A4A5: 8C 8D 0F        STY     $0F8D               
A4A8: 8F ; ????
A4A9: 90 B9           BCC     $A464               ; {}
A4AB: BA              TSX                         
A4AC: BB ; ????
A4AD: BC BD BE        LDY     $BEBD,X             ; {}
A4B0: BB ; ????
A4B1: 12 ; ????
A4B2: 2A              ROL     A                   
A4B3: 2B ; ????
A4B4: 2C 91 92        BIT     $9291               ; {}
A4B7: 93 ; ????
A4B8: 94 95           STY     $95,X               
A4BA: 93 ; ????
A4BB: 97 ; ????
A4BC: 98              TYA                         
A4BD: C1 C2           CMP     ($C2,X)             
A4BF: 0E 12 C4        ASL     $C412               
A4C2: C5 C6           CMP     $C6                 
A4C4: C7 ; ????
A4C5: 12 ; ????
A4C6: 2D 2E C8        AND     $C82E               
A4C9: C9 2F           CMP     #$2F                
A4CB: 13 ; ????
A4CC: 14 ; ????
A4CD: 15 16           ORA     $16,X               
A4CF: 0E 0A 01        ASL     $010A               
A4D2: 09 08           ORA     #$08                
A4D4: 06 20           ASL     $20                 
A4D6: 21 22           AND     ($22,X)             
A4D8: 23 ; ????
A4D9: 24 25           BIT     $25                 
A4DB: 26 1A           ROL     $1A                 
A4DD: 1B ; ????
A4DE: 1C ; ????
A4DF: 1A ; ????
A4E0: 1C ; ????
A4E1: 1A ; ????
A4E2: 1C ; ????
A4E3: 12 ; ????
A4E4: 12 ; ????
A4E5: 12 ; ????
A4E6: 12 ; ????
A4E7: 12 ; ????
A4E8: 12 ; ????
A4E9: 12 ; ????
A4EA: 12 ; ????
A4EB: 12 ; ????
A4EC: 12 ; ????
A4ED: 12 ; ????
A4EE: 12 ; ????
A4EF: 1A ; ????
A4F0: 1D 1D 1E        ORA     $1E1D,X             
A4F3: 1B ; ????
A4F4: 1C ; ????
A4F5: 1A ; ????
A4F6: 1B ; ????
A4F7: 1A ; ????
A4F8: 0F ; ????
A4F9: 0F ; ????
A4FA: 1E 19 12        ASL     $1219,X             
A4FD: 12 ; ????
A4FE: 12 ; ????
A4FF: 12 ; ????
A500: 12 ; ????
A501: 12 ; ????
A502: 12 ; ????
A503: 12 ; ????
A504: 12 ; ????
A505: 12 ; ????
A506: 12 ; ????
A507: 12 ; ????
A508: 17 ; ????
A509: 18              CLC                         
A50A: 18              CLC                         
A50B: 19 17 19        ORA     $1917,Y             
A50E: 1A ; ????
A50F: 1B ; ????
A510: 0F ; ????
A511: 0F ; ????
A512: 1D 1E 0F        ORA     $0F1E,X             
A515: 0F ; ????
A516: 1C ; ????
A517: 1B ; ????
A518: 1C ; ????
A519: 17 ; ????
A51A: 18              CLC                         
A51B: 1E 1D 1E        ASL     $1E1D,X             
A51E: 0F ; ????
A51F: 1E 19 17        ASL     $1719,X             
A522: 18              CLC                         
A523: 19 17 18        ORA     $1817,Y             
A526: 19 17 19        ORA     $1917,Y             
A529: AD 00 06        LDA     $0600               
A52C: D0 03           BNE     $A531               ; {}
A52E: 4C 42 EE        JMP     $EE42               
A531: A8              TAY                         
A532: A2 00           LDX     #$00                
A534: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
A537: AD 02 06        LDA     $0602               
A53A: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
A53D: AD 01 06        LDA     $0601               
A540: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
A543: BD 03 06        LDA     $0603,X             
A546: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
A549: E8              INX                         
A54A: 88              DEY                         
A54B: D0 F6           BNE     $A543               ; {}
A54D: A9 00           LDA     #$00                
A54F: 8D 00 06        STA     $0600               
A552: 60              RTS                         
A553: 60              RTS                         
A554: 08              PHP                         
A555: 48              PHA                         
A556: 8A              TXA                         
A557: 48              PHA                         
A558: 98              TYA                         
A559: 48              PHA                         
A55A: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
A55D: 20 2E EB        JSR     $EB2E               
A560: A5 85           LDA     $85                 
A562: C9 10           CMP     #$10                
A564: F0 11           BEQ     $A577               ; {}
A566: C9 20           CMP     #$20                
A568: F0 1F           BEQ     $A589               ; {}
A56A: 20 94 EE        JSR     $EE94               
A56D: 20 56 C8        JSR     $C856               
A570: 68              PLA                         
A571: A8              TAY                         
A572: 68              PLA                         
A573: AA              TAX                         
A574: 68              PLA                         
A575: 28              PLP                         
A576: 60              RTS                         
A577: 20 29 A5        JSR     $A529               ; {}
A57A: 20 C9 EB        JSR     $EBC9               
A57D: 20 6A EE        JSR     $EE6A               
A580: 20 09 A2        JSR     $A209               ; {}
A583: 20 02 A6        JSR     $A602               ; {}
A586: 4C 6A A5        JMP     $A56A               ; {}
A589: A5 18           LDA     $18                 
A58B: F0 05           BEQ     $A592               ; {}
A58D: A9 01           LDA     #$01                
A58F: 8D 81 03        STA     $0381               
A592: A5 B1           LDA     $B1                 
A594: 20 2B EE        JSR     $EE2B               
A597: 6A              ROR     A                   
A598: A5 9D           LDA     $9D                 
A59A: A5 A9           LDA     $A9                 
A59C: A5 20           LDA     $20                 
A59E: 42 ; ????
A59F: EE 20 6A        INC     $6A20               
A5A2: EE 20 94        INC     $9420               ; {}
A5A5: A7 ; ????
A5A6: 4C 6A A5        JMP     $A56A               ; {}
A5A9: 20 0F AA        JSR     $AA0F               ; {}
A5AC: 20 42 EE        JSR     $EE42               
A5AF: 20 6A EE        JSR     $EE6A               
A5B2: 20 34 AA        JSR     $AA34               ; {}
A5B5: 20 7A A8        JSR     $A87A               ; {}
A5B8: 20 92 A8        JSR     $A892               ; {}
A5BB: 20 FE A8        JSR     $A8FE               ; {}
A5BE: 20 BC A9        JSR     $A9BC               ; {}
A5C1: 4C 6A A5        JMP     $A56A               ; {}
A5C4: A9 00           LDA     #$00                
A5C6: 8D 91 02        STA     $0291               
A5C9: 60              RTS                         
A5CA: CE 80 02        DEC     $0280               
A5CD: A5 FD           LDA     $FD                 
A5CF: C9 48           CMP     #$48                
A5D1: D0 14           BNE     $A5E7               ; {}
A5D3: A5 1A           LDA     $1A                 
A5D5: 4A              LSR     A                   
A5D6: 90 0F           BCC     $A5E7               ; {}
A5D8: A9 EF           LDA     #$EF                
A5DA: 8D 80 02        STA     $0280               
A5DD: A9 39           LDA     #$39                
A5DF: 8D 83 02        STA     $0283               
A5E2: A9 80           LDA     #$80                
A5E4: 8D 91 02        STA     $0291               
A5E7: 60              RTS                         
A5E8: A9 5F           LDA     #$5F                
A5EA: 8D 81 02        STA     $0281               
A5ED: 8D 85 02        STA     $0285               
A5F0: 8D 89 02        STA     $0289               
A5F3: 8D 8D 02        STA     $028D               
A5F6: A9 F0           LDA     #$F0                
A5F8: 8D 80 02        STA     $0280               
A5FB: 60              RTS                         
A5FC: A9 00           LDA     #$00                
A5FE: 8D 91 02        STA     $0291               
A601: 60              RTS                         
A602: AD 91 02        LDA     $0291               
A605: F0 E1           BEQ     $A5E8               ; {}
A607: AD 80 02        LDA     $0280               
A60A: C9 F0           CMP     #$F0                
A60C: F0 EE           BEQ     $A5FC               ; {}
A60E: 8D 84 02        STA     $0284               
A611: 18              CLC                         
A612: 69 08           ADC     #$08                
A614: 8D 88 02        STA     $0288               
A617: 8D 8C 02        STA     $028C               
A61A: AD 83 02        LDA     $0283               
A61D: 8D 8B 02        STA     $028B               
A620: 18              CLC                         
A621: 69 08           ADC     #$08                
A623: 8D 87 02        STA     $0287               
A626: 8D 8F 02        STA     $028F               
A629: A9 21           LDA     #$21                
A62B: 8D 82 02        STA     $0282               
A62E: 8D 86 02        STA     $0286               
A631: 8D 8A 02        STA     $028A               
A634: 8D 8E 02        STA     $028E               
A637: A9 92           LDA     #$92                
A639: 8D 81 02        STA     $0281               
A63C: A9 94           LDA     #$94                
A63E: 8D 85 02        STA     $0285               
A641: A9 93           LDA     #$93                
A643: 8D 89 02        STA     $0289               
A646: A9 AE           LDA     #$AE                
A648: 8D 8D 02        STA     $028D               
A64B: 60              RTS                         
A64C: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
A64F: A5 21           LDA     $21                 
A651: 18              CLC                         
A652: 69 C0           ADC     #$C0                
A654: A8              TAY                         
A655: A5 20           LDA     $20                 
A657: 69 03           ADC     #$03                
A659: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
A65C: 8C 06 20        STY     $2006               ; {hard.P_VRAM_ADDR}
A65F: A5 22           LDA     $22                 
A661: 0A              ASL     A                   
A662: 0A              ASL     A                   
A663: 0A              ASL     A                   
A664: 0A              ASL     A                   
A665: 0A              ASL     A                   
A666: 0A              ASL     A                   
A667: 18              CLC                         
A668: 69 80           ADC     #$80                
A66A: 85 23           STA     $23                 
A66C: A9 A6           LDA     #$A6                
A66E: 69 00           ADC     #$00                
A670: 85 24           STA     $24                 
A672: A2 40           LDX     #$40                
A674: A0 00           LDY     #$00                
A676: B1 23           LDA     ($23),Y             
A678: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
A67B: C8              INY                         
A67C: CA              DEX                         
A67D: D0 F7           BNE     $A676               ; {}
A67F: 60              RTS                         
A680: 00              BRK                         
A681: 00              BRK                         
A682: 00              BRK                         
A683: 00              BRK                         
A684: 00              BRK                         
A685: 00              BRK                         
A686: 00              BRK                         
A687: 00              BRK                         
A688: 00              BRK                         
A689: 00              BRK                         
A68A: 00              BRK                         
A68B: 00              BRK                         
A68C: 00              BRK                         
A68D: 00              BRK                         
A68E: 00              BRK                         
A68F: 00              BRK                         
A690: 00              BRK                         
A691: 00              BRK                         
A692: 00              BRK                         
A693: 00              BRK                         
A694: 00              BRK                         
A695: 00              BRK                         
A696: 00              BRK                         
A697: 00              BRK                         
A698: 00              BRK                         
A699: 00              BRK                         
A69A: 00              BRK                         
A69B: 00              BRK                         
A69C: 00              BRK                         
A69D: 00              BRK                         
A69E: 00              BRK                         
A69F: 00              BRK                         
A6A0: 00              BRK                         
A6A1: 00              BRK                         
A6A2: 00              BRK                         
A6A3: 00              BRK                         
A6A4: 00              BRK                         
A6A5: 00              BRK                         
A6A6: 00              BRK                         
A6A7: 00              BRK                         
A6A8: 00              BRK                         
A6A9: 00              BRK                         
A6AA: 00              BRK                         
A6AB: 00              BRK                         
A6AC: 00              BRK                         
A6AD: 00              BRK                         
A6AE: 00              BRK                         
A6AF: 00              BRK                         
A6B0: 00              BRK                         
A6B1: 0C ; ????
A6B2: 0F ; ????
A6B3: 0F ; ????
A6B4: 0F ; ????
A6B5: 0F ; ????
A6B6: 03 ; ????
A6B7: 00              BRK                         
A6B8: 00              BRK                         
A6B9: 00              BRK                         
A6BA: 00              BRK                         
A6BB: 00              BRK                         
A6BC: 00              BRK                         
A6BD: 00              BRK                         
A6BE: 00              BRK                         
A6BF: 00              BRK                         
A6C0: 00              BRK                         
A6C1: 00              BRK                         
A6C2: 00              BRK                         
A6C3: 00              BRK                         
A6C4: 00              BRK                         
A6C5: A0 A0           LDY     #$A0                
A6C7: 20 00 00        JSR     $0000               ; {ram.GP_00}
A6CA: 40              RTI                         
A6CB: 50 18           BVC     $A6E5               ; {}
A6CD: 8A              TXA                         
A6CE: AA              TAX                         
A6CF: 2A              ROL     A                   
A6D0: AA              TAX                         
A6D1: EC F7 F5        CPX     $F5F7               
A6D4: F1 FF           SBC     ($FF),Y             
A6D6: 33 ; ????
A6D7: 00              BRK                         
A6D8: 0A              ASL     A                   
A6D9: FE FF FF        INC     $FFFF,X             
A6DC: FF ; ????
A6DD: FF ; ????
A6DE: BB ; ????
A6DF: AA              TAX                         
A6E0: 00              BRK                         
A6E1: CF ; ????
A6E2: FF ; ????
A6E3: FF ; ????
A6E4: FF ; ????
A6E5: FF ; ????
A6E6: FF ; ????
A6E7: 0A              ASL     A                   
A6E8: 80 ; ????
A6E9: A0 20           LDY     #$20                
A6EB: 00              BRK                         
A6EC: 00              BRK                         
A6ED: 88              DEY                         
A6EE: A2 02           LDX     #$02                
A6F0: 8A              TXA                         
A6F1: AA              TAX                         
A6F2: 0A              ASL     A                   
A6F3: 00              BRK                         
A6F4: 00              BRK                         
A6F5: 00              BRK                         
A6F6: 00              BRK                         
A6F7: 00              BRK                         
A6F8: 00              BRK                         
A6F9: 00              BRK                         
A6FA: 00              BRK                         
A6FB: 00              BRK                         
A6FC: 00              BRK                         
A6FD: 00              BRK                         
A6FE: 00              BRK                         
A6FF: 00              BRK                         
A700: 0A              ASL     A                   
A701: 0A              ASL     A                   
A702: 0A              ASL     A                   
A703: 0A              ASL     A                   
A704: 18              CLC                         
A705: 69 2B           ADC     #$2B                
A707: 85 20           STA     $20                 
A709: A9 A7           LDA     #$A7                
A70B: 69 00           ADC     #$00                
A70D: 85 21           STA     $21                 
A70F: A0 00           LDY     #$00                
A711: A2 10           LDX     #$10                
A713: B1 20           LDA     ($20),Y             
A715: 99 90 03        STA     $0390,Y             
A718: C8              INY                         
A719: CA              DEX                         
A71A: D0 F7           BNE     $A713               ; {}
A71C: 60              RTS                         
A71D: A2 00           LDX     #$00                
A71F: B9 4B A7        LDA     $A74B,Y             ; {}
A722: 99 A0 03        STA     $03A0,Y             
A725: C8              INY                         
A726: C0 10           CPY     #$10                
A728: D0 F5           BNE     $A71F               ; {}
A72A: 60              RTS                         
A72B: 0F ; ????
A72C: 20 10 00        JSR     $0010               
A72F: 0F ; ????
A730: 24 2A           BIT     $2A                 
A732: 0A              ASL     A                   
A733: 0F ; ????
A734: 31 1C           AND     ($1C),Y             
A736: 0C ; ????
A737: 0F ; ????
A738: 27 ; ????
A739: 06 31           ASL     $31                 
A73B: 0F ; ????
A73C: 20 22 02        JSR     $0222               
A73F: 0F ; ????
A740: 27 ; ????
A741: 17 ; ????
A742: 07 ; ????
A743: 0F ; ????
A744: 2C 11 0A        BIT     $0A11               
A747: 0F ; ????
A748: 02 ; ????
A749: 27 ; ????
A74A: 15 0F           ORA     $0F,X               
A74C: 20 26 07        JSR     $0726               
A74F: 0F ; ????
A750: 31 02           AND     ($02),Y             
A752: 15 0F           ORA     $0F,X               
A754: 12 ; ????
A755: 24 31           BIT     $31                 
A757: 0F ; ????
A758: 05 16           ORA     $16                 
A75A: 38              SEC                         
A75B: 20 6B A7        JSR     $A76B               ; {}
A75E: 20 70 A7        JSR     $A770               ; {}
A761: 20 7C A7        JSR     $A77C               ; {}
A764: A9 04           LDA     #$04                
A766: 85 B2           STA     $B2                 
A768: 4C AD A7        JMP     $A7AD               ; {}
A76B: A9 00           LDA     #$00                
A76D: 85 B2           STA     $B2                 
A76F: 60              RTS                         
A770: A9 CB           LDA     #$CB                
A772: 85 08           STA     $08                 
A774: A9 A7           LDA     #$A7                
A776: 85 09           STA     $09                 
A778: 20 CB E7        JSR     $E7CB               
A77B: 60              RTS                         
A77C: 20 F9 E3        JSR     $E3F9               
A77F: 4C 82 A7        JMP     $A782               ; {}
A782: A2 00           LDX     #$00                
A784: BD 90 A7        LDA     $A790,X             ; {}
A787: 9D 30 02        STA     $0230,X             
A78A: E8              INX                         
A78B: E0 04           CPX     #$04                
A78D: 90 F5           BCC     $A784               ; {}
A78F: 60              RTS                         
A790: 27 ; ????
A791: 09 00           ORA     #$00                
A793: 18              CLC                         
A794: A5 00           LDA     $00                 ; {ram.GP_00}
A796: A5 B1           LDA     $B1                 
A798: C9 01           CMP     #$01                
A79A: F0 01           BEQ     $A79D               ; {}
A79C: 60              RTS                         
A79D: A5 F6           LDA     $F6                 
A79F: 0A              ASL     A                   
A7A0: 0A              ASL     A                   
A7A1: 0A              ASL     A                   
A7A2: B0 09           BCS     $A7AD               ; {}
A7A4: 0A              ASL     A                   
A7A5: B0 01           BCS     $A7A8               ; {}
A7A7: 60              RTS                         
A7A8: A9 00           LDA     #$00                
A7AA: 85 B1           STA     $B1                 
A7AC: 60              RTS                         
A7AD: A6 B2           LDX     $B2                 
A7AF: E0 01           CPX     #$01                
A7B1: 90 04           BCC     $A7B7               ; {}
A7B3: A2 00           LDX     #$00                
A7B5: F0 01           BEQ     $A7B8               ; {}
A7B7: E8              INX                         
A7B8: 86 B2           STX     $B2                 
A7BA: BD C7 A7        LDA     $A7C7,X             ; {}
A7BD: 8D 30 02        STA     $0230               
A7C0: BD C9 A7        LDA     $A7C9,X             ; {}
A7C3: 8D 33 02        STA     $0233               
A7C6: 60              RTS                         
A7C7: 60              RTS                         
A7C8: 70 50           BVS     $A81A               ; {}
A7CA: 50 01           BVC     $A7CD               ; {}
A7CC: 20 12 E6        JSR     $E612               
A7CF: A7 ; ????
A7D0: 04 ; ????
A7D1: 8C 01 05        STY     $0501               
A7D4: 28              PLP                         
A7D5: 29 16           AND     #$16                
A7D7: 27 ; ????
A7D8: 29 04           AND     #$04                
A7DA: CC 01 08        CPY     $0801               
A7DD: 18              CLC                         
A7DE: 24 23           BIT     $23                 
A7E0: 29 1E           AND     #$1E                
A7E2: 23 ; ????
A7E3: 2A              ROL     A                   
A7E4: 1A ; ????
A7E5: 00              BRK                         
A7E6: 00              BRK                         
A7E7: 80 ; ????
A7E8: A0 A0           LDY     #$A0                
A7EA: A0 A0           LDY     #$A0                
A7EC: 20 00 00        JSR     $0000               ; {ram.GP_00}
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
A800: 00              BRK                         
A801: 00              BRK                         
A802: 00              BRK                         
A803: 00              BRK                         
A804: 00              BRK                         
A805: 00              BRK                         
A806: 00              BRK                         
A807: 00              BRK                         
A808: 00              BRK                         
A809: 00              BRK                         
A80A: 00              BRK                         
A80B: 00              BRK                         
A80C: 00              BRK                         
A80D: 00              BRK                         
A80E: 00              BRK                         
A80F: 00              BRK                         
A810: 00              BRK                         
A811: 00              BRK                         
A812: 00              BRK                         
A813: 00              BRK                         
A814: 00              BRK                         
A815: 00              BRK                         
A816: 00              BRK                         
A817: 00              BRK                         
A818: 00              BRK                         
A819: 00              BRK                         
A81A: 00              BRK                         
A81B: 00              BRK                         
A81C: 00              BRK                         
A81D: 00              BRK                         
A81E: 00              BRK                         
A81F: 00              BRK                         
A820: 00              BRK                         
A821: 00              BRK                         
A822: 00              BRK                         
A823: 00              BRK                         
A824: 00              BRK                         
A825: 00              BRK                         
A826: 20 44 A8        JSR     $A844               ; {}
A829: 20 50 A8        JSR     $A850               ; {}
A82C: 20 60 A8        JSR     $A860               ; {}
A82F: A9 03           LDA     #$03                
A831: 8D 01 07        STA     $0701               
A834: A9 00           LDA     #$00                
A836: 8D 4E 07        STA     $074E               
A839: A2 2F           LDX     #$2F                
A83B: A9 00           LDA     #$00                
A83D: 9D 31 60        STA     $6031,X             
A840: CA              DEX                         
A841: 10 F8           BPL     $A83B               ; {}
A843: 60              RTS                         
A844: A9 00           LDA     #$00                
A846: 8D 02 07        STA     $0702               
A849: 8D 00 07        STA     $0700               
A84C: 8D 03 07        STA     $0703               
A84F: 60              RTS                         
A850: A9 AE           LDA     #$AE                
A852: 85 08           STA     $08                 
A854: A9 AA           LDA     #$AA                
A856: 85 09           STA     $09                 
A858: A9 20           LDA     #$20                
A85A: 85 00           STA     $00                 ; {ram.GP_00}
A85C: 20 CB E7        JSR     $E7CB               
A85F: 60              RTS                         
A860: 20 F9 E3        JSR     $E3F9               
A863: 20 67 A8        JSR     $A867               ; {}
A866: 60              RTS                         
A867: AD 00 61        LDA     $6100               
A86A: D0 0D           BNE     $A879               ; {}
A86C: A2 00           LDX     #$00                
A86E: BD 79 AA        LDA     $AA79,X             ; {}
A871: 9D 34 02        STA     $0234,X             
A874: E8              INX                         
A875: E0 08           CPX     #$08                
A877: 90 F5           BCC     $A86E               ; {}
A879: 60              RTS                         
A87A: A5 00           LDA     $00                 ; {ram.GP_00}
A87C: A5 B1           LDA     $B1                 
A87E: C9 02           CMP     #$02                
A880: D0 0A           BNE     $A88C               ; {}
A882: A5 F6           LDA     $F6                 
A884: 0A              ASL     A                   
A885: 0A              ASL     A                   
A886: 0A              ASL     A                   
A887: B0 04           BCS     $A88D               ; {}
A889: 0A              ASL     A                   
A88A: B0 01           BCS     $A88D               ; {}
A88C: 60              RTS                         
A88D: A9 00           LDA     #$00                
A88F: 85 B1           STA     $B1                 
A891: 60              RTS                         
A892: AE 03 07        LDX     $0703               
A895: A9 A8           LDA     #$A8                
A897: 48              PHA                         
A898: A9 AF           LDA     #$AF                
A89A: 48              PHA                         
A89B: AD 09 07        LDA     $0709               
A89E: A8              TAY                         
A89F: 4A              LSR     A                   
A8A0: B0 1C           BCS     $A8BE               ; {}
A8A2: 4A              LSR     A                   
A8A3: B0 21           BCS     $A8C6               ; {}
A8A5: 4A              LSR     A                   
A8A6: B0 24           BCS     $A8CC               ; {}
A8A8: 4A              LSR     A                   
A8A9: B0 2D           BCS     $A8D8               ; {}
A8AB: 68              PLA                         
A8AC: 68              PLA                         
A8AD: 4C B3 A8        JMP     $A8B3               ; {}
A8B0: 20 B1 A9        JSR     $A9B1               ; {}
A8B3: 8E 03 07        STX     $0703               
A8B6: 8A              TXA                         
A8B7: 20 E2 A8        JSR     $A8E2               ; {}
A8BA: 20 F7 A8        JSR     $A8F7               ; {}
A8BD: 60              RTS                         
A8BE: E8              INX                         
A8BF: E0 40           CPX     #$40                
A8C1: 90 02           BCC     $A8C5               ; {}
A8C3: A2 00           LDX     #$00                
A8C5: 60              RTS                         
A8C6: CA              DEX                         
A8C7: 10 02           BPL     $A8CB               ; {}
A8C9: A2 3F           LDX     #$3F                
A8CB: 60              RTS                         
A8CC: 8A              TXA                         
A8CD: 18              CLC                         
A8CE: 69 0C           ADC     #$0C                
A8D0: C9 40           CMP     #$40                
A8D2: 90 02           BCC     $A8D6               ; {}
A8D4: 60              RTS                         
A8D5: EA              NOP                         
A8D6: AA              TAX                         
A8D7: 60              RTS                         
A8D8: 8A              TXA                         
A8D9: 38              SEC                         
A8DA: E9 0C           SBC     #$0C                
A8DC: B0 02           BCS     $A8E0               ; {}
A8DE: 60              RTS                         
A8DF: EA              NOP                         
A8E0: AA              TAX                         
A8E1: 60              RTS                         
A8E2: A8              TAY                         
A8E3: A2 00           LDX     #$00                
A8E5: 38              SEC                         
A8E6: E9 0C           SBC     #$0C                
A8E8: 30 06           BMI     $A8F0               ; {}
A8EA: E8              INX                         
A8EB: A8              TAY                         
A8EC: E0 06           CPX     #$06                
A8EE: 90 F5           BCC     $A8E5               ; {}
A8F0: BD 81 AA        LDA     $AA81,X             ; {}
A8F3: 8D 04 07        STA     $0704               
A8F6: 60              RTS                         
A8F7: B9 87 AA        LDA     $AA87,Y             ; {}
A8FA: 8D 05 07        STA     $0705               
A8FD: 60              RTS                         
A8FE: A5 B1           LDA     $B1                 
A900: C9 02           CMP     #$02                
A902: D0 24           BNE     $A928               ; {}
A904: AD 09 07        LDA     $0709               
A907: 0A              ASL     A                   
A908: 90 12           BCC     $A91C               ; {}
A90A: 20 47 A9        JSR     $A947               ; {}
A90D: 20 5E A9        JSR     $A95E               ; {}
A910: 20 81 A9        JSR     $A981               ; {}
A913: 20 29 A9        JSR     $A929               ; {}
A916: 20 B1 A9        JSR     $A9B1               ; {}
A919: 4C 25 A9        JMP     $A925               ; {}
A91C: 0A              ASL     A                   
A91D: 90 06           BCC     $A925               ; {}
A91F: 20 3B A9        JSR     $A93B               ; {}
A922: 20 B1 A9        JSR     $A9B1               ; {}
A925: 20 81 A9        JSR     $A981               ; {}
A928: 60              RTS                         
A929: A8              TAY                         
A92A: AD 02 07        LDA     $0702               
A92D: 18              CLC                         
A92E: 69 01           ADC     #$01                
A930: C9 18           CMP     #$18                
A932: 90 02           BCC     $A936               ; {}
A934: A9 00           LDA     #$00                
A936: 8D 02 07        STA     $0702               
A939: 98              TYA                         
A93A: 60              RTS                         
A93B: AD 02 07        LDA     $0702               
A93E: 38              SEC                         
A93F: E9 01           SBC     #$01                
A941: B0 F3           BCS     $A936               ; {}
A943: A9 17           LDA     #$17                
A945: D0 EF           BNE     $A936               ; {}
A947: A0 00           LDY     #$00                
A949: B9 6E A1        LDA     $A16E,Y             ; {}
A94C: 18              CLC                         
A94D: 6D 02 07        ADC     $0702               
A950: A8              TAY                         
A951: AD 03 07        LDA     $0703               
A954: 99 31 60        STA     $6031,Y             
A957: AE 03 07        LDX     $0703               
A95A: BD 50 CA        LDA     $CA50,X             
A95D: 60              RTS                         
A95E: A8              TAY                         
A95F: A2 00           LDX     #$00                
A961: AD 02 07        LDA     $0702               
A964: C9 0C           CMP     #$0C                
A966: 90 01           BCC     $A969               ; {}
A968: E8              INX                         
A969: BD 93 AA        LDA     $AA93,X             ; {}
A96C: 8D 4F 07        STA     $074F               
A96F: AE 02 07        LDX     $0702               
A972: BD 96 AA        LDA     $AA96,X             ; {}
A975: 8D 50 07        STA     $0750               
A978: 8C 51 07        STY     $0751               
A97B: A9 01           LDA     #$01                
A97D: 8D 4E 07        STA     $074E               
A980: 60              RTS                         
A981: A2 37           LDX     #$37                
A983: AD 02 07        LDA     $0702               
A986: C9 0C           CMP     #$0C                
A988: 90 02           BCC     $A98C               ; {}
A98A: A2 47           LDX     #$47                
A98C: 8E 06 07        STX     $0706               
A98F: AE 02 07        LDX     $0702               
A992: BD 99 A9        LDA     $A999,X             ; {}
A995: 8D 07 07        STA     $0707               
A998: 60              RTS                         
A999: 48              PHA                         
A99A: 50 58           BVC     $A9F4               ; {}
A99C: 60              RTS                         
A99D: 68              PLA                         
A99E: 70 88           BVS     $A928               ; {}
A9A0: 90 98           BCC     $A93A               ; {}
A9A2: A0 A8           LDY     #$A8                
A9A4: B0 48           BCS     $A9EE               ; {}
A9A6: 50 58           BVC     $AA00               ; {}
A9A8: 60              RTS                         
A9A9: 68              PLA                         
A9AA: 70 88           BVS     $A934               ; {}
A9AC: 90 98           BCC     $A946               ; {}
A9AE: A0 A8           LDY     #$A8                
A9B0: B0 A9           BCS     $A95B               ; {}
A9B2: 40              RTI                         
A9B3: 8D 00 07        STA     $0700               
A9B6: A9 FF           LDA     #$FF                
A9B8: 8D 0B 07        STA     $070B               
A9BB: 60              RTS                         
A9BC: A5 B1           LDA     $B1                 
A9BE: C9 02           CMP     #$02                
A9C0: D0 4C           BNE     $AA0E               ; {}
A9C2: EE 0B 07        INC     $070B               
A9C5: 4C D1 A9        JMP     $A9D1               ; {}
A9C8: A9 F8           LDA     #$F8                
A9CA: 8D 34 02        STA     $0234               
A9CD: 8D 38 02        STA     $0238               
A9D0: 60              RTS                         
A9D1: AD 00 07        LDA     $0700               
A9D4: F0 0F           BEQ     $A9E5               ; {}
A9D6: AD 0B 07        LDA     $070B               
A9D9: 29 07           AND     #$07                
A9DB: F0 01           BEQ     $A9DE               ; {}
A9DD: 60              RTS                         
A9DE: AD 00 07        LDA     $0700               
A9E1: 29 80           AND     #$80                
A9E3: D0 1C           BNE     $AA01               ; {}
A9E5: AD 04 07        LDA     $0704               
A9E8: 8D 34 02        STA     $0234               
A9EB: AD 05 07        LDA     $0705               
A9EE: 8D 37 02        STA     $0237               
A9F1: AD 06 07        LDA     $0706               
A9F4: 8D 38 02        STA     $0238               
A9F7: AD 07 07        LDA     $0707               
A9FA: 8D 3B 02        STA     $023B               
A9FD: A9 C0           LDA     #$C0                
A9FF: D0 0A           BNE     $AA0B               ; {}
AA01: A9 F8           LDA     #$F8                
AA03: 8D 34 02        STA     $0234               
AA06: 8D 38 02        STA     $0238               
AA09: A9 40           LDA     #$40                
AA0B: 8D 00 07        STA     $0700               
AA0E: 60              RTS                         
AA0F: AE 4E 07        LDX     $074E               
AA12: D0 01           BNE     $AA15               ; {}
AA14: 60              RTS                         
AA15: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
AA18: AD 4F 07        LDA     $074F               
AA1B: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
AA1E: AD 50 07        LDA     $0750               
AA21: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
AA24: A0 00           LDY     #$00                
AA26: B9 51 07        LDA     $0751,Y             
AA29: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
AA2C: C8              INY                         
AA2D: CA              DEX                         
AA2E: D0 F6           BNE     $AA26               ; {}
AA30: 8E 4E 07        STX     $074E               
AA33: 60              RTS                         
AA34: A5 F6           LDA     $F6                 
AA36: D0 2F           BNE     $AA67               ; {}
AA38: A5 F8           LDA     $F8                 
AA3A: CD 08 07        CMP     $0708               
AA3D: D0 28           BNE     $AA67               ; {}
AA3F: AE 0A 07        LDX     $070A               
AA42: E0 30           CPX     #$30                
AA44: B0 05           BCS     $AA4B               ; {}
AA46: EE 0A 07        INC     $070A               
AA49: D0 0C           BNE     $AA57               ; {}
AA4B: F0 10           BEQ     $AA5D               ; {}
AA4D: E8              INX                         
AA4E: E0 37           CPX     #$37                
AA50: D0 02           BNE     $AA54               ; {}
AA52: A2 30           LDX     #$30                
AA54: 8E 0A 07        STX     $070A               
AA57: A9 00           LDA     #$00                
AA59: 8D 09 07        STA     $0709               
AA5C: 60              RTS                         
AA5D: AD 08 07        LDA     $0708               
AA60: 8D 09 07        STA     $0709               
AA63: EE 0A 07        INC     $070A               
AA66: 60              RTS                         
AA67: A5 F6           LDA     $F6                 
AA69: 8D 08 07        STA     $0708               
AA6C: 8D 09 07        STA     $0709               
AA6F: A9 00           LDA     #$00                
AA71: 8D 0A 07        STA     $070A               
AA74: 60              RTS                         
AA75: 27 ; ????
AA76: 09 00           ORA     #$00                
AA78: 30 F8           BMI     $AA72               ; {}
AA7A: 0A              ASL     A                   
AA7B: 21 30           AND     ($30,X)             
AA7D: F8              SED                         
AA7E: 0A              ASL     A                   
AA7F: 21 30           AND     ($30,X)             
AA81: 77 ; ????
AA82: 87 ; ????
AA83: 97 ; ????
AA84: A7 ; ????
AA85: B7 ; ????
AA86: C7 ; ????
AA87: 20 30 40        JSR     $4030               
AA8A: 50 60           BVC     $AAEC               ; {}
AA8C: 70 80           BVS     $AA0E               ; {}
AA8E: 90 A0           BCC     $AA30               ; {}
AA90: B0 C0           BCS     $AA52               ; {}
AA92: D0 20           BNE     $AAB4               ; {}
AA94: 21 21           AND     ($21,X)             
AA96: E9 EA           SBC     #$EA                
AA98: EB ; ????
AA99: EC ED EE        CPX     $EEED               
AA9C: F1 F2           SBC     ($F2),Y             
AA9E: F3 ; ????
AA9F: F4 ; ????
AAA0: F5 F6           SBC     $F6,X               
AAA2: 29 2A           AND     #$2A                
AAA4: 2B ; ????
AAA5: 2C 2D 2E        BIT     $2E2D               
AAA8: 31 32           AND     ($32),Y             
AAAA: 33 ; ????
AAAB: 34 ; ????
AAAC: 35 36           AND     $36,X               
AAAE: 01 20           ORA     ($20,X)             
AAB0: 12 ; ????
AAB1: 86 AB           STX     $AB                 
AAB3: 06 A2           ASL     $A2                 
AAB5: 01 0E           ORA     ($0E,X)             
AAB7: 79 79 06        ADC     $0679,Y             
AABA: 62 ; ????
AABB: 03 ; ????
AABC: 0E 79 79        ASL     $7979               
AABF: 05 C2           ORA     $C2                 
AAC1: 01 8D           ORA     ($8D,X)             
AAC3: 79 05 DD        ADC     $DD05,Y             
AAC6: 01 8D           ORA     ($8D,X)             
AAC8: 79 09 E4        ADC     $E409,Y             
AACB: 01 0C           ORA     ($0C,X)             
AACD: 12 ; ????
AACE: 00              BRK                         
AACF: 01 02           ORA     ($02,X)             
AAD1: 03 ; ????
AAD2: 04 ; ????
AAD3: 05 06           ORA     $06                 
AAD5: 07 ; ????
AAD6: 08              PHP                         
AAD7: 09 16           ORA     #$16                
AAD9: 17 ; ????
AADA: 09 24           ORA     #$24                
AADC: 02 ; ????
AADD: 0C ; ????
AADE: 12 ; ????
AADF: 18              CLC                         
AAE0: 19 1A 1B        ORA     $1B1A,Y             
AAE3: 1C ; ????
AAE4: 1D 1E 1F        ORA     $1F1E,X             
AAE7: 20 21 22        JSR     $2221               
AAEA: 23 ; ????
AAEB: 09 64           ORA     #$64                
AAED: 02 ; ????
AAEE: 0C ; ????
AAEF: 12 ; ????
AAF0: 24 25           BIT     $25                 
AAF2: 26 27           ROL     $27                 
AAF4: 28              PLP                         
AAF5: 29 2A           AND     #$2A                
AAF7: 2B ; ????
AAF8: 2C 2D 2E        BIT     $2E2D               
AAFB: 2F ; ????
AAFC: 09 A4           ORA     #$A4                
AAFE: 02 ; ????
AAFF: 0C ; ????
AB00: 12 ; ????
AB01: 30 31           BMI     $AB34               ; {}
AB03: 32 ; ????
AB04: 33 ; ????
AB05: 34 ; ????
AB06: 35 36           AND     $36,X               
AB08: 37 ; ????
AB09: 38              SEC                         
AB0A: 39 3A 3B        AND     $3B3A,Y             
AB0D: 09 E4           ORA     #$E4                
AB0F: 02 ; ????
AB10: 0C ; ????
AB11: 12 ; ????
AB12: 3C ; ????
AB13: 3D 3E 3F        AND     $3F3E,X             
AB16: 40              RTI                         
AB17: 41 42           EOR     ($42,X)             
AB19: 43 ; ????
AB1A: 44 ; ????
AB1B: 45 46           EOR     $46                 
AB1D: 47 ; ????
AB1E: 09 24           ORA     #$24                
AB20: 03 ; ????
AB21: 04 ; ????
AB22: 12 ; ????
AB23: 48              PHA                         
AB24: 49 0A           EOR     #$0A                
AB26: 0E 04 60        ASL     $6004               
AB29: 00              BRK                         
AB2A: 04 ; ????
AB2B: 4E 4F 4E        LSR     $4E4F               
AB2E: 4F ; ????
AB2F: 04 ; ????
AB30: 80 ; ????
AB31: 00              BRK                         
AB32: 04 ; ????
AB33: 4F ; ????
AB34: 4E 4F 4E        LSR     $4E4F               
AB37: 04 ; ????
AB38: 7C ; ????
AB39: 00              BRK                         
AB3A: 04 ; ????
AB3B: 4E 4F 4E        LSR     $4E4F               
AB3E: 4F ; ????
AB3F: 04 ; ????
AB40: 9C ; ????
AB41: 00              BRK                         
AB42: 04 ; ????
AB43: 4F ; ????
AB44: 4E 4F 4E        LSR     $4E4F               
AB47: 07 ; ????
AB48: 64 ; ????
AB49: 00              BRK                         
AB4A: 02 ; ????
AB4B: 80 ; ????
AB4C: 07 ; ????
AB4D: 84 00           STY     $00                 ; {ram.GP_00}
AB4F: 02 ; ????
AB50: 82 ; ????
AB51: 07 ; ????
AB52: 7A ; ????
AB53: 00              BRK                         
AB54: 02 ; ????
AB55: 7C ; ????
AB56: 07 ; ????
AB57: 9A              TXS                         
AB58: 00              BRK                         
AB59: 02 ; ????
AB5A: 7E 04 87        ROR     $8704,X             ; {}
AB5D: 00              BRK                         
AB5E: 12 ; ????
AB5F: 1A ; ????
AB60: 23 ; ????
AB61: 29 1A           AND     #$1A                
AB63: 27 ; ????
AB64: 12 ; ????
AB65: 28              PLP                         
AB66: 16 18           ASL     $18,X               
AB68: 27 ; ????
AB69: 1A ; ????
AB6A: 19 12 2C        ORA     $2C12,Y             
AB6D: 24 27           BIT     $27                 
AB6F: 19 28 05        ORA     $0528,Y             
AB72: E9 00           SBC     #$00                
AB74: 06 4A           ASL     $4A                 
AB76: 05 F1           ORA     $F1                 
AB78: 00              BRK                         
AB79: 06 4A           ASL     $4A                 
AB7B: 05 29           ORA     $29                 
AB7D: 01 06           ORA     ($06,X)             
AB7F: 4A              LSR     A                   
AB80: 05 31           ORA     $31                 
AB82: 01 06           ORA     ($06,X)             
AB84: 4A              LSR     A                   
AB85: 00              BRK                         
AB86: 00              BRK                         
AB87: 30 00           BMI     $AB89               ; {}
AB89: 00              BRK                         
AB8A: 00              BRK                         
AB8B: 00              BRK                         
AB8C: C0 00           CPY     #$00                
AB8E: 00              BRK                         
AB8F: 03 ; ????
AB90: 00              BRK                         
AB91: 00              BRK                         
AB92: 00              BRK                         
AB93: 00              BRK                         
AB94: 0C ; ????
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
ABC6: 20 D0 AB        JSR     $ABD0               ; {}
ABC9: 20 93 AC        JSR     $AC93               ; {}
ABCC: 20 36 AC        JSR     $AC36               ; {}
ABCF: 60              RTS                         
ABD0: A2 23           LDX     #$23                
ABD2: A9 00           LDA     #$00                
ABD4: 9D 0D 60        STA     $600D,X             
ABD7: CA              DEX                         
ABD8: 10 FA           BPL     $ABD4               ; {}
ABDA: A2 11           LDX     #$11                
ABDC: A9 00           LDA     #$00                
ABDE: 9D 61 60        STA     $6061,X             
ABE1: CA              DEX                         
ABE2: 10 FA           BPL     $ABDE               ; {}
ABE4: A9 00           LDA     #$00                
ABE6: A8              TAY                         
ABE7: B9 31 60        LDA     $6031,Y             
ABEA: 20 1D AC        JSR     $AC1D               ; {}
ABED: C8              INY                         
ABEE: C0 18           CPY     #$18                
ABF0: B0 21           BCS     $AC13               ; {}
ABF2: B9 31 60        LDA     $6031,Y             
ABF5: 20 1D AC        JSR     $AC1D               ; {}
ABF8: C8              INY                         
ABF9: C0 18           CPY     #$18                
ABFB: B0 16           BCS     $AC13               ; {}
ABFD: B9 31 60        LDA     $6031,Y             
AC00: 20 1D AC        JSR     $AC1D               ; {}
AC03: C8              INY                         
AC04: C0 18           CPY     #$18                
AC06: B0 0B           BCS     $AC13               ; {}
AC08: B9 31 60        LDA     $6031,Y             
AC0B: 20 1D AC        JSR     $AC1D               ; {}
AC0E: C8              INY                         
AC0F: C0 18           CPY     #$18                
AC11: 90 D4           BCC     $ABE7               ; {}
AC13: 60              RTS                         
AC14: A2 11           LDX     #$11                
AC16: 7E 61 60        ROR     $6061,X             
AC19: CA              DEX                         
AC1A: 10 FA           BPL     $AC16               ; {}
AC1C: 60              RTS                         
AC1D: 4A              LSR     A                   
AC1E: 20 14 AC        JSR     $AC14               ; {}
AC21: 4A              LSR     A                   
AC22: 20 14 AC        JSR     $AC14               ; {}
AC25: 4A              LSR     A                   
AC26: 20 14 AC        JSR     $AC14               ; {}
AC29: 4A              LSR     A                   
AC2A: 20 14 AC        JSR     $AC14               ; {}
AC2D: 4A              LSR     A                   
AC2E: 20 14 AC        JSR     $AC14               ; {}
AC31: 4A              LSR     A                   
AC32: 20 14 AC        JSR     $AC14               ; {}
AC35: 60              RTS                         
AC36: A2 00           LDX     #$00                
AC38: 86 00           STX     $00                 ; {ram.GP_00}
AC3A: A5 00           LDA     $00                 ; {ram.GP_00}
AC3C: 18              CLC                         
AC3D: 7D 61 60        ADC     $6061,X             
AC40: 85 00           STA     $00                 ; {ram.GP_00}
AC42: E8              INX                         
AC43: E0 11           CPX     #$11                
AC45: 90 F3           BCC     $AC3A               ; {}
AC47: BD 61 60        LDA     $6061,X             
AC4A: C5 00           CMP     $00                 ; {ram.GP_00}
AC4C: 60              RTS                         
AC4D: A9 28           LDA     #$28                
AC4F: A2 12           LDX     #$12                
AC51: A0 00           LDY     #$00                
AC53: 20 76 EB        JSR     $EB76               
AC56: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
AC59: A9 2A           LDA     #$2A                
AC5B: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
AC5E: A9 08           LDA     #$08                
AC60: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
AC63: A2 00           LDX     #$00                
AC65: BD 74 AC        LDA     $AC74,X             ; {}
AC68: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
AC6B: E8              INX                         
AC6C: E0 0F           CPX     #$0F                
AC6E: 90 F5           BCC     $AC65               ; {}
AC70: 20 C9 EB        JSR     $EBC9               
AC73: 60              RTS                         
AC74: 1A ; ????
AC75: 27 ; ????
AC76: 27 ; ????
AC77: 24 27           BIT     $27                 
AC79: 0E 29 27        ASL     $2729               
AC7C: 2E 12 16        ROL     $1612               
AC7F: 1C ; ????
AC80: 16 1E           ASL     $1E,X               
AC82: 23 ; ????
AC83: A0 00           LDY     #$00                
AC85: A2 00           LDX     #$00                
AC87: E8              INX                         
AC88: D0 FD           BNE     $AC87               ; {}
AC8A: C8              INY                         
AC8B: D0 F8           BNE     $AC85               ; {}
AC8D: 38              SEC                         
AC8E: E9 01           SBC     #$01                
AC90: D0 F1           BNE     $AC83               ; {}
AC92: 60              RTS                         
AC93: A0 02           LDY     #$02                
AC95: B9 61 60        LDA     $6061,Y             
AC98: 48              PHA                         
AC99: 29 F3           AND     #$F3                
AC9B: 99 0D 60        STA     $600D,Y             
AC9E: 68              PLA                         
AC9F: 29 0C           AND     #$0C                
ACA1: 4A              LSR     A                   
ACA2: 4A              LSR     A                   
ACA3: 99 10 60        STA     $6010,Y             
ACA6: 88              DEY                         
ACA7: 10 EC           BPL     $AC95               ; {}
ACA9: AD 64 60        LDA     $6064               
ACAC: 8D 13 60        STA     $6013               
ACAF: AD 65 60        LDA     $6065               
ACB2: 8D 14 60        STA     $6014               
ACB5: AD 66 60        LDA     $6066               
ACB8: 8D 15 60        STA     $6015               
ACBB: AD 67 60        LDA     $6067               
ACBE: 8D 19 60        STA     $6019               
ACC1: AD 68 60        LDA     $6068               
ACC4: 48              PHA                         
ACC5: 29 0F           AND     #$0F                
ACC7: 8D 1A 60        STA     $601A               
ACCA: 68              PLA                         
ACCB: 29 F0           AND     #$F0                
ACCD: 4A              LSR     A                   
ACCE: 4A              LSR     A                   
ACCF: 4A              LSR     A                   
ACD0: 4A              LSR     A                   
ACD1: 8D 1C 60        STA     $601C               
ACD4: AD 69 60        LDA     $6069               
ACD7: 8D 1B 60        STA     $601B               
ACDA: AD 6A 60        LDA     $606A               
ACDD: 29 01           AND     #$01                
ACDF: 8D 1D 60        STA     $601D               
ACE2: AD 6B 60        LDA     $606B               
ACE5: 8D 1E 60        STA     $601E               
ACE8: AD 6C 60        LDA     $606C               
ACEB: 8D 1F 60        STA     $601F               
ACEE: AD 6D 60        LDA     $606D               
ACF1: 8D 20 60        STA     $6020               
ACF4: AD 6E 60        LDA     $606E               
ACF7: 48              PHA                         
ACF8: 29 F0           AND     #$F0                
ACFA: 4A              LSR     A                   
ACFB: 4A              LSR     A                   
ACFC: 4A              LSR     A                   
ACFD: 4A              LSR     A                   
ACFE: 8D 21 60        STA     $6021               
AD01: 68              PLA                         
AD02: 29 0F           AND     #$0F                
AD04: 8D 26 60        STA     $6026               
AD07: AD 6F 60        LDA     $606F               
AD0A: 48              PHA                         
AD0B: 29 03           AND     #$03                
AD0D: 8D 22 60        STA     $6022               
AD10: 68              PLA                         
AD11: 48              PHA                         
AD12: 4A              LSR     A                   
AD13: 4A              LSR     A                   
AD14: 29 03           AND     #$03                
AD16: 8D 23 60        STA     $6023               
AD19: 68              PLA                         
AD1A: 4A              LSR     A                   
AD1B: 4A              LSR     A                   
AD1C: 4A              LSR     A                   
AD1D: 4A              LSR     A                   
AD1E: 29 03           AND     #$03                
AD20: 8D 24 60        STA     $6024               
AD23: AD 70 60        LDA     $6070               
AD26: 8D 25 60        STA     $6025               
AD29: AD 71 60        LDA     $6071               
AD2C: 48              PHA                         
AD2D: 29 F0           AND     #$F0                
AD2F: 4A              LSR     A                   
AD30: 4A              LSR     A                   
AD31: 4A              LSR     A                   
AD32: 4A              LSR     A                   
AD33: 8D 28 60        STA     $6028               
AD36: 68              PLA                         
AD37: 48              PHA                         
AD38: 29 07           AND     #$07                
AD3A: 8D 29 60        STA     $6029               
AD3D: 68              PLA                         
AD3E: 4A              LSR     A                   
AD3F: 4A              LSR     A                   
AD40: 4A              LSR     A                   
AD41: 29 01           AND     #$01                
AD43: 8D 2A 60        STA     $602A               
AD46: 60              RTS                         
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
ADC7: 08              PHP                         
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
AEB6: FF ; ????
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
AF50: 80 ; ????
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
B000: FF ; ????
B001: FF ; ????
B002: FF ; ????
B003: FF ; ????
B004: FF ; ????
B005: FF ; ????
B006: FF ; ????
B007: FF ; ????
B008: FF ; ????
B009: FF ; ????
B00A: FF ; ????
B00B: FF ; ????
B00C: FF ; ????
B00D: FF ; ????
B00E: FF ; ????
B00F: FF ; ????
B010: FF ; ????
B011: FF ; ????
B012: FF ; ????
B013: FF ; ????
B014: FF ; ????
B015: FF ; ????
B016: FF ; ????
B017: FF ; ????
B018: FF ; ????
B019: FF ; ????
B01A: FF ; ????
B01B: FF ; ????
B01C: FF ; ????
B01D: FF ; ????
B01E: FF ; ????
B01F: FF ; ????
B020: FF ; ????
B021: FF ; ????
B022: FF ; ????
B023: FF ; ????
B024: FF ; ????
B025: FF ; ????
B026: FF ; ????
B027: FF ; ????
B028: FF ; ????
B029: FF ; ????
B02A: FF ; ????
B02B: FF ; ????
B02C: FF ; ????
B02D: FF ; ????
B02E: FF ; ????
B02F: FF ; ????
B030: FF ; ????
B031: FF ; ????
B032: FF ; ????
B033: FF ; ????
B034: FF ; ????
B035: FF ; ????
B036: FF ; ????
B037: FF ; ????
B038: FF ; ????
B039: FF ; ????
B03A: FF ; ????
B03B: FF ; ????
B03C: FF ; ????
B03D: FF ; ????
B03E: FF ; ????
B03F: FF ; ????
B040: FF ; ????
B041: FF ; ????
B042: FF ; ????
B043: FF ; ????
B044: FF ; ????
B045: FF ; ????
B046: FF ; ????
B047: FF ; ????
B048: FF ; ????
B049: FF ; ????
B04A: FF ; ????
B04B: FF ; ????
B04C: FF ; ????
B04D: FF ; ????
B04E: FF ; ????
B04F: FF ; ????
B050: FF ; ????
B051: FF ; ????
B052: FF ; ????
B053: FF ; ????
B054: FF ; ????
B055: FF ; ????
B056: FF ; ????
B057: FF ; ????
B058: FF ; ????
B059: FF ; ????
B05A: FF ; ????
B05B: FF ; ????
B05C: FF ; ????
B05D: FF ; ????
B05E: FF ; ????
B05F: FF ; ????
B060: FF ; ????
B061: FF ; ????
B062: FF ; ????
B063: FF ; ????
B064: FF ; ????
B065: FF ; ????
B066: FF ; ????
B067: FF ; ????
B068: FF ; ????
B069: FF ; ????
B06A: FF ; ????
B06B: FF ; ????
B06C: FF ; ????
B06D: FF ; ????
B06E: FF ; ????
B06F: FF ; ????
B070: FF ; ????
B071: FF ; ????
B072: FF ; ????
B073: FF ; ????
B074: FF ; ????
B075: FF ; ????
B076: FF ; ????
B077: FF ; ????
B078: FF ; ????
B079: FF ; ????
B07A: FF ; ????
B07B: FF ; ????
B07C: FF ; ????
B07D: FF ; ????
B07E: FF ; ????
B07F: FF ; ????
B080: FF ; ????
B081: FF ; ????
B082: FF ; ????
B083: FF ; ????
B084: FF ; ????
B085: FF ; ????
B086: FF ; ????
B087: FF ; ????
B088: FF ; ????
B089: FF ; ????
B08A: FF ; ????
B08B: FF ; ????
B08C: FF ; ????
B08D: FF ; ????
B08E: FF ; ????
B08F: FF ; ????
B090: FF ; ????
B091: FF ; ????
B092: FF ; ????
B093: FF ; ????
B094: FF ; ????
B095: FF ; ????
B096: FF ; ????
B097: FF ; ????
B098: FF ; ????
B099: FF ; ????
B09A: FF ; ????
B09B: FF ; ????
B09C: FF ; ????
B09D: FF ; ????
B09E: FF ; ????
B09F: FF ; ????
B0A0: FF ; ????
B0A1: FF ; ????
B0A2: FF ; ????
B0A3: FF ; ????
B0A4: FF ; ????
B0A5: FF ; ????
B0A6: FF ; ????
B0A7: FF ; ????
B0A8: FF ; ????
B0A9: FF ; ????
B0AA: FF ; ????
B0AB: FF ; ????
B0AC: FF ; ????
B0AD: FF ; ????
B0AE: FF ; ????
B0AF: FF ; ????
B0B0: FF ; ????
B0B1: FF ; ????
B0B2: FF ; ????
B0B3: FF ; ????
B0B4: FF ; ????
B0B5: FF ; ????
B0B6: FF ; ????
B0B7: FF ; ????
B0B8: FF ; ????
B0B9: FF ; ????
B0BA: FF ; ????
B0BB: FF ; ????
B0BC: FF ; ????
B0BD: FF ; ????
B0BE: FF ; ????
B0BF: FF ; ????
B0C0: FF ; ????
B0C1: FF ; ????
B0C2: FF ; ????
B0C3: FF ; ????
B0C4: FF ; ????
B0C5: FF ; ????
B0C6: FF ; ????
B0C7: FF ; ????
B0C8: FF ; ????
B0C9: FF ; ????
B0CA: FF ; ????
B0CB: FF ; ????
B0CC: FF ; ????
B0CD: FF ; ????
B0CE: FF ; ????
B0CF: FF ; ????
B0D0: FF ; ????
B0D1: FF ; ????
B0D2: FF ; ????
B0D3: FF ; ????
B0D4: FF ; ????
B0D5: FF ; ????
B0D6: FF ; ????
B0D7: FF ; ????
B0D8: FF ; ????
B0D9: FF ; ????
B0DA: FF ; ????
B0DB: FF ; ????
B0DC: FF ; ????
B0DD: FF ; ????
B0DE: FF ; ????
B0DF: FF ; ????
B0E0: FF ; ????
B0E1: FF ; ????
B0E2: FF ; ????
B0E3: FF ; ????
B0E4: FF ; ????
B0E5: FF ; ????
B0E6: FF ; ????
B0E7: FF ; ????
B0E8: FF ; ????
B0E9: FF ; ????
B0EA: FF ; ????
B0EB: FF ; ????
B0EC: FF ; ????
B0ED: FF ; ????
B0EE: FF ; ????
B0EF: FF ; ????
B0F0: FF ; ????
B0F1: FF ; ????
B0F2: FF ; ????
B0F3: FF ; ????
B0F4: FF ; ????
B0F5: FF ; ????
B0F6: FF ; ????
B0F7: FF ; ????
B0F8: FF ; ????
B0F9: FF ; ????
B0FA: FF ; ????
B0FB: FF ; ????
B0FC: FF ; ????
B0FD: FF ; ????
B0FE: FF ; ????
B0FF: FF ; ????
B100: 00              BRK                         
B101: 00              BRK                         
B102: 00              BRK                         
B103: 00              BRK                         
B104: 00              BRK                         
B105: 00              BRK                         
B106: 00              BRK                         
B107: 00              BRK                         
B108: 00              BRK                         
B109: 00              BRK                         
B10A: 00              BRK                         
B10B: 00              BRK                         
B10C: 00              BRK                         
B10D: 00              BRK                         
B10E: 00              BRK                         
B10F: 00              BRK                         
B110: 00              BRK                         
B111: 00              BRK                         
B112: 00              BRK                         
B113: 00              BRK                         
B114: 00              BRK                         
B115: 00              BRK                         
B116: 00              BRK                         
B117: 00              BRK                         
B118: 00              BRK                         
B119: 00              BRK                         
B11A: 00              BRK                         
B11B: 00              BRK                         
B11C: 00              BRK                         
B11D: 00              BRK                         
B11E: 00              BRK                         
B11F: 00              BRK                         
B120: 00              BRK                         
B121: 00              BRK                         
B122: 00              BRK                         
B123: 00              BRK                         
B124: 00              BRK                         
B125: 00              BRK                         
B126: 00              BRK                         
B127: 00              BRK                         
B128: 00              BRK                         
B129: 00              BRK                         
B12A: 00              BRK                         
B12B: 00              BRK                         
B12C: 00              BRK                         
B12D: 00              BRK                         
B12E: 00              BRK                         
B12F: 00              BRK                         
B130: 00              BRK                         
B131: 00              BRK                         
B132: 00              BRK                         
B133: 00              BRK                         
B134: 00              BRK                         
B135: 00              BRK                         
B136: 00              BRK                         
B137: 00              BRK                         
B138: 00              BRK                         
B139: 00              BRK                         
B13A: 00              BRK                         
B13B: 00              BRK                         
B13C: 00              BRK                         
B13D: 00              BRK                         
B13E: 00              BRK                         
B13F: 00              BRK                         
B140: 00              BRK                         
B141: 00              BRK                         
B142: 00              BRK                         
B143: 00              BRK                         
B144: 00              BRK                         
B145: 00              BRK                         
B146: 00              BRK                         
B147: 00              BRK                         
B148: 00              BRK                         
B149: 00              BRK                         
B14A: 00              BRK                         
B14B: 00              BRK                         
B14C: 00              BRK                         
B14D: 00              BRK                         
B14E: 00              BRK                         
B14F: 00              BRK                         
B150: 00              BRK                         
B151: 00              BRK                         
B152: 00              BRK                         
B153: 00              BRK                         
B154: 00              BRK                         
B155: 00              BRK                         
B156: 00              BRK                         
B157: 00              BRK                         
B158: 00              BRK                         
B159: 00              BRK                         
B15A: 00              BRK                         
B15B: 00              BRK                         
B15C: 00              BRK                         
B15D: 00              BRK                         
B15E: 00              BRK                         
B15F: 00              BRK                         
B160: 00              BRK                         
B161: 00              BRK                         
B162: 00              BRK                         
B163: 00              BRK                         
B164: 00              BRK                         
B165: 00              BRK                         
B166: 00              BRK                         
B167: 00              BRK                         
B168: 00              BRK                         
B169: 00              BRK                         
B16A: 00              BRK                         
B16B: 00              BRK                         
B16C: 00              BRK                         
B16D: 00              BRK                         
B16E: 00              BRK                         
B16F: 00              BRK                         
B170: 00              BRK                         
B171: 00              BRK                         
B172: 00              BRK                         
B173: 00              BRK                         
B174: 00              BRK                         
B175: 00              BRK                         
B176: 00              BRK                         
B177: 00              BRK                         
B178: 00              BRK                         
B179: 00              BRK                         
B17A: 00              BRK                         
B17B: 00              BRK                         
B17C: 00              BRK                         
B17D: 00              BRK                         
B17E: 00              BRK                         
B17F: 00              BRK                         
B180: 00              BRK                         
B181: 00              BRK                         
B182: 00              BRK                         
B183: 00              BRK                         
B184: 00              BRK                         
B185: 00              BRK                         
B186: 00              BRK                         
B187: 00              BRK                         
B188: 00              BRK                         
B189: 00              BRK                         
B18A: 00              BRK                         
B18B: 00              BRK                         
B18C: 00              BRK                         
B18D: 00              BRK                         
B18E: 00              BRK                         
B18F: 00              BRK                         
B190: 00              BRK                         
B191: 00              BRK                         
B192: 00              BRK                         
B193: 00              BRK                         
B194: 00              BRK                         
B195: 00              BRK                         
B196: 00              BRK                         
B197: 00              BRK                         
B198: 00              BRK                         
B199: 00              BRK                         
B19A: 00              BRK                         
B19B: 00              BRK                         
B19C: 00              BRK                         
B19D: 00              BRK                         
B19E: 00              BRK                         
B19F: 00              BRK                         
B1A0: 00              BRK                         
B1A1: 00              BRK                         
B1A2: 00              BRK                         
B1A3: 00              BRK                         
B1A4: 00              BRK                         
B1A5: 00              BRK                         
B1A6: 00              BRK                         
B1A7: 00              BRK                         
B1A8: 00              BRK                         
B1A9: 00              BRK                         
B1AA: 00              BRK                         
B1AB: 00              BRK                         
B1AC: 00              BRK                         
B1AD: 00              BRK                         
B1AE: 00              BRK                         
B1AF: 00              BRK                         
B1B0: 00              BRK                         
B1B1: 00              BRK                         
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
B1BC: 00              BRK                         
B1BD: 00              BRK                         
B1BE: 00              BRK                         
B1BF: 00              BRK                         
B1C0: 00              BRK                         
B1C1: 00              BRK                         
B1C2: 00              BRK                         
B1C3: 00              BRK                         
B1C4: 00              BRK                         
B1C5: 00              BRK                         
B1C6: 00              BRK                         
B1C7: 00              BRK                         
B1C8: 00              BRK                         
B1C9: 00              BRK                         
B1CA: 00              BRK                         
B1CB: 00              BRK                         
B1CC: 00              BRK                         
B1CD: 00              BRK                         
B1CE: 00              BRK                         
B1CF: 00              BRK                         
B1D0: 00              BRK                         
B1D1: 00              BRK                         
B1D2: 00              BRK                         
B1D3: 00              BRK                         
B1D4: 00              BRK                         
B1D5: 00              BRK                         
B1D6: 00              BRK                         
B1D7: 00              BRK                         
B1D8: 00              BRK                         
B1D9: 00              BRK                         
B1DA: 00              BRK                         
B1DB: 00              BRK                         
B1DC: 00              BRK                         
B1DD: 00              BRK                         
B1DE: 00              BRK                         
B1DF: 00              BRK                         
B1E0: 00              BRK                         
B1E1: 00              BRK                         
B1E2: 00              BRK                         
B1E3: 00              BRK                         
B1E4: 00              BRK                         
B1E5: 00              BRK                         
B1E6: 00              BRK                         
B1E7: 00              BRK                         
B1E8: 00              BRK                         
B1E9: 00              BRK                         
B1EA: 00              BRK                         
B1EB: 00              BRK                         
B1EC: 00              BRK                         
B1ED: 00              BRK                         
B1EE: 00              BRK                         
B1EF: 00              BRK                         
B1F0: 00              BRK                         
B1F1: 00              BRK                         
B1F2: 00              BRK                         
B1F3: 00              BRK                         
B1F4: 00              BRK                         
B1F5: 00              BRK                         
B1F6: 00              BRK                         
B1F7: 00              BRK                         
B1F8: 00              BRK                         
B1F9: 00              BRK                         
B1FA: 00              BRK                         
B1FB: 00              BRK                         
B1FC: 00              BRK                         
B1FD: 00              BRK                         
B1FE: 00              BRK                         
B1FF: 00              BRK                         
B200: FF ; ????
B201: FF ; ????
B202: FF ; ????
B203: FF ; ????
B204: FF ; ????
B205: FF ; ????
B206: FF ; ????
B207: FF ; ????
B208: FF ; ????
B209: FF ; ????
B20A: FF ; ????
B20B: FF ; ????
B20C: FF ; ????
B20D: FF ; ????
B20E: FF ; ????
B20F: FF ; ????
B210: FF ; ????
B211: FF ; ????
B212: FF ; ????
B213: FF ; ????
B214: FF ; ????
B215: FF ; ????
B216: FF ; ????
B217: FF ; ????
B218: FF ; ????
B219: FF ; ????
B21A: FF ; ????
B21B: FF ; ????
B21C: FF ; ????
B21D: FF ; ????
B21E: FF ; ????
B21F: FF ; ????
B220: FF ; ????
B221: FF ; ????
B222: FF ; ????
B223: FF ; ????
B224: FF ; ????
B225: FF ; ????
B226: FF ; ????
B227: FF ; ????
B228: FF ; ????
B229: FF ; ????
B22A: FF ; ????
B22B: FF ; ????
B22C: FF ; ????
B22D: FF ; ????
B22E: FF ; ????
B22F: FF ; ????
B230: FF ; ????
B231: FF ; ????
B232: FF ; ????
B233: FF ; ????
B234: FF ; ????
B235: FF ; ????
B236: FF ; ????
B237: FF ; ????
B238: FF ; ????
B239: FF ; ????
B23A: FF ; ????
B23B: FF ; ????
B23C: FF ; ????
B23D: FF ; ????
B23E: FF ; ????
B23F: FF ; ????
B240: FF ; ????
B241: FF ; ????
B242: FF ; ????
B243: FF ; ????
B244: FF ; ????
B245: FF ; ????
B246: FF ; ????
B247: FF ; ????
B248: FF ; ????
B249: FF ; ????
B24A: FF ; ????
B24B: FF ; ????
B24C: FF ; ????
B24D: FF ; ????
B24E: FF ; ????
B24F: FF ; ????
B250: FF ; ????
B251: FF ; ????
B252: FF ; ????
B253: FF ; ????
B254: FF ; ????
B255: FF ; ????
B256: FF ; ????
B257: FF ; ????
B258: FF ; ????
B259: FF ; ????
B25A: FF ; ????
B25B: FF ; ????
B25C: FF ; ????
B25D: FF ; ????
B25E: FF ; ????
B25F: FF ; ????
B260: FF ; ????
B261: FF ; ????
B262: FF ; ????
B263: FF ; ????
B264: FF ; ????
B265: FF ; ????
B266: FF ; ????
B267: FF ; ????
B268: FF ; ????
B269: FF ; ????
B26A: FF ; ????
B26B: FF ; ????
B26C: FF ; ????
B26D: FF ; ????
B26E: FF ; ????
B26F: FF ; ????
B270: FF ; ????
B271: FF ; ????
B272: FF ; ????
B273: FF ; ????
B274: FF ; ????
B275: FF ; ????
B276: FF ; ????
B277: FF ; ????
B278: FF ; ????
B279: FF ; ????
B27A: FF ; ????
B27B: FF ; ????
B27C: FF ; ????
B27D: FF ; ????
B27E: FF ; ????
B27F: FF ; ????
B280: FF ; ????
B281: FF ; ????
B282: FF ; ????
B283: FF ; ????
B284: FF ; ????
B285: FF ; ????
B286: FF ; ????
B287: FF ; ????
B288: FF ; ????
B289: FF ; ????
B28A: FF ; ????
B28B: FF ; ????
B28C: FF ; ????
B28D: FF ; ????
B28E: FF ; ????
B28F: FF ; ????
B290: FF ; ????
B291: FF ; ????
B292: FF ; ????
B293: FF ; ????
B294: FF ; ????
B295: FF ; ????
B296: FF ; ????
B297: FF ; ????
B298: FF ; ????
B299: FF ; ????
B29A: FF ; ????
B29B: FF ; ????
B29C: FF ; ????
B29D: FF ; ????
B29E: FF ; ????
B29F: FF ; ????
B2A0: FF ; ????
B2A1: FF ; ????
B2A2: FF ; ????
B2A3: FF ; ????
B2A4: FF ; ????
B2A5: FF ; ????
B2A6: FF ; ????
B2A7: FF ; ????
B2A8: FF ; ????
B2A9: FF ; ????
B2AA: FF ; ????
B2AB: FF ; ????
B2AC: FF ; ????
B2AD: FF ; ????
B2AE: FF ; ????
B2AF: FF ; ????
B2B0: FF ; ????
B2B1: FF ; ????
B2B2: FF ; ????
B2B3: FF ; ????
B2B4: FF ; ????
B2B5: FF ; ????
B2B6: FF ; ????
B2B7: FF ; ????
B2B8: FF ; ????
B2B9: FF ; ????
B2BA: FF ; ????
B2BB: FF ; ????
B2BC: FF ; ????
B2BD: FF ; ????
B2BE: FF ; ????
B2BF: FF ; ????
B2C0: FF ; ????
B2C1: FF ; ????
B2C2: FF ; ????
B2C3: FF ; ????
B2C4: FF ; ????
B2C5: FF ; ????
B2C6: FF ; ????
B2C7: FF ; ????
B2C8: FF ; ????
B2C9: FF ; ????
B2CA: FF ; ????
B2CB: FF ; ????
B2CC: FF ; ????
B2CD: FF ; ????
B2CE: FF ; ????
B2CF: FF ; ????
B2D0: FF ; ????
B2D1: FF ; ????
B2D2: FF ; ????
B2D3: FF ; ????
B2D4: FF ; ????
B2D5: FF ; ????
B2D6: FF ; ????
B2D7: FF ; ????
B2D8: FF ; ????
B2D9: FF ; ????
B2DA: FF ; ????
B2DB: FF ; ????
B2DC: FF ; ????
B2DD: FF ; ????
B2DE: FF ; ????
B2DF: FF ; ????
B2E0: FF ; ????
B2E1: FF ; ????
B2E2: FF ; ????
B2E3: FF ; ????
B2E4: FF ; ????
B2E5: FF ; ????
B2E6: FF ; ????
B2E7: FF ; ????
B2E8: FF ; ????
B2E9: FF ; ????
B2EA: FF ; ????
B2EB: FF ; ????
B2EC: FF ; ????
B2ED: FF ; ????
B2EE: FF ; ????
B2EF: FF ; ????
B2F0: FF ; ????
B2F1: FF ; ????
B2F2: FF ; ????
B2F3: FF ; ????
B2F4: FF ; ????
B2F5: FF ; ????
B2F6: FF ; ????
B2F7: FF ; ????
B2F8: FF ; ????
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
B457: FF ; ????
B458: FF ; ????
B459: FF ; ????
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
B4D6: FF ; ????
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
B504: 01 00           ORA     ($00,X)             ; {ram.GP_00}
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
B593: 00              BRK                         
B594: 00              BRK                         
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
B800: FF ; ????
B801: FF ; ????
B802: FF ; ????
B803: FF ; ????
B804: FF ; ????
B805: FF ; ????
B806: FF ; ????
B807: FF ; ????
B808: FF ; ????
B809: FF ; ????
B80A: FF ; ????
B80B: FF ; ????
B80C: FF ; ????
B80D: FF ; ????
B80E: FF ; ????
B80F: FF ; ????
B810: FF ; ????
B811: FF ; ????
B812: FF ; ????
B813: FF ; ????
B814: FF ; ????
B815: FF ; ????
B816: FF ; ????
B817: FF ; ????
B818: FF ; ????
B819: FF ; ????
B81A: FF ; ????
B81B: FF ; ????
B81C: FF ; ????
B81D: FF ; ????
B81E: FF ; ????
B81F: FF ; ????
B820: FF ; ????
B821: FF ; ????
B822: FF ; ????
B823: FF ; ????
B824: FF ; ????
B825: FF ; ????
B826: FF ; ????
B827: FF ; ????
B828: FF ; ????
B829: FF ; ????
B82A: FF ; ????
B82B: FF ; ????
B82C: FF ; ????
B82D: FF ; ????
B82E: FF ; ????
B82F: FF ; ????
B830: FF ; ????
B831: FF ; ????
B832: FF ; ????
B833: FF ; ????
B834: FF ; ????
B835: FF ; ????
B836: FF ; ????
B837: FF ; ????
B838: FF ; ????
B839: FF ; ????
B83A: FF ; ????
B83B: FF ; ????
B83C: FF ; ????
B83D: FF ; ????
B83E: FF ; ????
B83F: FF ; ????
B840: FF ; ????
B841: FF ; ????
B842: FF ; ????
B843: FF ; ????
B844: FF ; ????
B845: FF ; ????
B846: FF ; ????
B847: FF ; ????
B848: FF ; ????
B849: FF ; ????
B84A: FF ; ????
B84B: FF ; ????
B84C: FF ; ????
B84D: FF ; ????
B84E: FF ; ????
B84F: FF ; ????
B850: FF ; ????
B851: FF ; ????
B852: FF ; ????
B853: FF ; ????
B854: FF ; ????
B855: FF ; ????
B856: FF ; ????
B857: FF ; ????
B858: FF ; ????
B859: FF ; ????
B85A: FF ; ????
B85B: FF ; ????
B85C: FF ; ????
B85D: FF ; ????
B85E: FF ; ????
B85F: FF ; ????
B860: FF ; ????
B861: FF ; ????
B862: FF ; ????
B863: FF ; ????
B864: FF ; ????
B865: FF ; ????
B866: FF ; ????
B867: FF ; ????
B868: FF ; ????
B869: FF ; ????
B86A: FF ; ????
B86B: FF ; ????
B86C: FF ; ????
B86D: FF ; ????
B86E: FF ; ????
B86F: FF ; ????
B870: FF ; ????
B871: FF ; ????
B872: FF ; ????
B873: FF ; ????
B874: FF ; ????
B875: FF ; ????
B876: FF ; ????
B877: FF ; ????
B878: FF ; ????
B879: FF ; ????
B87A: FF ; ????
B87B: FF ; ????
B87C: FF ; ????
B87D: FF ; ????
B87E: FF ; ????
B87F: FF ; ????
B880: FF ; ????
B881: FF ; ????
B882: FF ; ????
B883: FF ; ????
B884: FF ; ????
B885: FF ; ????
B886: FF ; ????
B887: FF ; ????
B888: FF ; ????
B889: FF ; ????
B88A: FF ; ????
B88B: FF ; ????
B88C: FF ; ????
B88D: FF ; ????
B88E: FF ; ????
B88F: FF ; ????
B890: FF ; ????
B891: FF ; ????
B892: FF ; ????
B893: FF ; ????
B894: FF ; ????
B895: FF ; ????
B896: FF ; ????
B897: FF ; ????
B898: FF ; ????
B899: FF ; ????
B89A: FF ; ????
B89B: FF ; ????
B89C: FF ; ????
B89D: FF ; ????
B89E: FF ; ????
B89F: FF ; ????
B8A0: FF ; ????
B8A1: FF ; ????
B8A2: FF ; ????
B8A3: FF ; ????
B8A4: FF ; ????
B8A5: FF ; ????
B8A6: FF ; ????
B8A7: FF ; ????
B8A8: FF ; ????
B8A9: FF ; ????
B8AA: FF ; ????
B8AB: FF ; ????
B8AC: FF ; ????
B8AD: FF ; ????
B8AE: FF ; ????
B8AF: FF ; ????
B8B0: FF ; ????
B8B1: FF ; ????
B8B2: FF ; ????
B8B3: FF ; ????
B8B4: FF ; ????
B8B5: FF ; ????
B8B6: FF ; ????
B8B7: FF ; ????
B8B8: FF ; ????
B8B9: FF ; ????
B8BA: FF ; ????
B8BB: FF ; ????
B8BC: FF ; ????
B8BD: FF ; ????
B8BE: FF ; ????
B8BF: FF ; ????
B8C0: FF ; ????
B8C1: FF ; ????
B8C2: FF ; ????
B8C3: FF ; ????
B8C4: FF ; ????
B8C5: FF ; ????
B8C6: FF ; ????
B8C7: FF ; ????
B8C8: FF ; ????
B8C9: FF ; ????
B8CA: FF ; ????
B8CB: FF ; ????
B8CC: FF ; ????
B8CD: FF ; ????
B8CE: FF ; ????
B8CF: FF ; ????
B8D0: FF ; ????
B8D1: FF ; ????
B8D2: FF ; ????
B8D3: FF ; ????
B8D4: FF ; ????
B8D5: FF ; ????
B8D6: FF ; ????
B8D7: FF ; ????
B8D8: FF ; ????
B8D9: FF ; ????
B8DA: FF ; ????
B8DB: FF ; ????
B8DC: FF ; ????
B8DD: FF ; ????
B8DE: FF ; ????
B8DF: FF ; ????
B8E0: FF ; ????
B8E1: FF ; ????
B8E2: FF ; ????
B8E3: FF ; ????
B8E4: FF ; ????
B8E5: FF ; ????
B8E6: FF ; ????
B8E7: FF ; ????
B8E8: FF ; ????
B8E9: FF ; ????
B8EA: FF ; ????
B8EB: FF ; ????
B8EC: FF ; ????
B8ED: FF ; ????
B8EE: FF ; ????
B8EF: FF ; ????
B8F0: FF ; ????
B8F1: FF ; ????
B8F2: FF ; ????
B8F3: FF ; ????
B8F4: FF ; ????
B8F5: FF ; ????
B8F6: FF ; ????
B8F7: FF ; ????
B8F8: FF ; ????
B8F9: FF ; ????
B8FA: FF ; ????
B8FB: FF ; ????
B8FC: FF ; ????
B8FD: FF ; ????
B8FE: FF ; ????
B8FF: FF ; ????
B900: 00              BRK                         
B901: 00              BRK                         
B902: 00              BRK                         
B903: 00              BRK                         
B904: 00              BRK                         
B905: 00              BRK                         
B906: 00              BRK                         
B907: 00              BRK                         
B908: 00              BRK                         
B909: 00              BRK                         
B90A: 00              BRK                         
B90B: 00              BRK                         
B90C: 00              BRK                         
B90D: 00              BRK                         
B90E: 00              BRK                         
B90F: 00              BRK                         
B910: 00              BRK                         
B911: 00              BRK                         
B912: 00              BRK                         
B913: 00              BRK                         
B914: 00              BRK                         
B915: 00              BRK                         
B916: 00              BRK                         
B917: 00              BRK                         
B918: 00              BRK                         
B919: 00              BRK                         
B91A: 00              BRK                         
B91B: 00              BRK                         
B91C: 00              BRK                         
B91D: 00              BRK                         
B91E: 00              BRK                         
B91F: 00              BRK                         
B920: 00              BRK                         
B921: 00              BRK                         
B922: 00              BRK                         
B923: 00              BRK                         
B924: 00              BRK                         
B925: 00              BRK                         
B926: 00              BRK                         
B927: 00              BRK                         
B928: 00              BRK                         
B929: 00              BRK                         
B92A: 00              BRK                         
B92B: 00              BRK                         
B92C: 00              BRK                         
B92D: 00              BRK                         
B92E: 00              BRK                         
B92F: 00              BRK                         
B930: 00              BRK                         
B931: 00              BRK                         
B932: 00              BRK                         
B933: 00              BRK                         
B934: 00              BRK                         
B935: 00              BRK                         
B936: 00              BRK                         
B937: 00              BRK                         
B938: 00              BRK                         
B939: 00              BRK                         
B93A: 00              BRK                         
B93B: 00              BRK                         
B93C: 00              BRK                         
B93D: 00              BRK                         
B93E: 00              BRK                         
B93F: 00              BRK                         
B940: 00              BRK                         
B941: 00              BRK                         
B942: 00              BRK                         
B943: 00              BRK                         
B944: 00              BRK                         
B945: 00              BRK                         
B946: 00              BRK                         
B947: 00              BRK                         
B948: 00              BRK                         
B949: 00              BRK                         
B94A: 00              BRK                         
B94B: 00              BRK                         
B94C: 00              BRK                         
B94D: 00              BRK                         
B94E: 00              BRK                         
B94F: 00              BRK                         
B950: 00              BRK                         
B951: 00              BRK                         
B952: 00              BRK                         
B953: 00              BRK                         
B954: 00              BRK                         
B955: 00              BRK                         
B956: 00              BRK                         
B957: 00              BRK                         
B958: 00              BRK                         
B959: 00              BRK                         
B95A: 00              BRK                         
B95B: 00              BRK                         
B95C: 00              BRK                         
B95D: 00              BRK                         
B95E: 00              BRK                         
B95F: 00              BRK                         
B960: 00              BRK                         
B961: 00              BRK                         
B962: 00              BRK                         
B963: 00              BRK                         
B964: 00              BRK                         
B965: 00              BRK                         
B966: 00              BRK                         
B967: 00              BRK                         
B968: 00              BRK                         
B969: 00              BRK                         
B96A: 00              BRK                         
B96B: 00              BRK                         
B96C: 00              BRK                         
B96D: 00              BRK                         
B96E: 00              BRK                         
B96F: 00              BRK                         
B970: 00              BRK                         
B971: 00              BRK                         
B972: 00              BRK                         
B973: 00              BRK                         
B974: 00              BRK                         
B975: 00              BRK                         
B976: 00              BRK                         
B977: 00              BRK                         
B978: 00              BRK                         
B979: 00              BRK                         
B97A: 00              BRK                         
B97B: 00              BRK                         
B97C: 00              BRK                         
B97D: 00              BRK                         
B97E: 00              BRK                         
B97F: 00              BRK                         
B980: 00              BRK                         
B981: 00              BRK                         
B982: 00              BRK                         
B983: 00              BRK                         
B984: 00              BRK                         
B985: 00              BRK                         
B986: 00              BRK                         
B987: 00              BRK                         
B988: 00              BRK                         
B989: 00              BRK                         
B98A: 00              BRK                         
B98B: 00              BRK                         
B98C: 00              BRK                         
B98D: 00              BRK                         
B98E: 00              BRK                         
B98F: 00              BRK                         
B990: 00              BRK                         
B991: 00              BRK                         
B992: 00              BRK                         
B993: 00              BRK                         
B994: 00              BRK                         
B995: 00              BRK                         
B996: 00              BRK                         
B997: 00              BRK                         
B998: 00              BRK                         
B999: 00              BRK                         
B99A: 00              BRK                         
B99B: 00              BRK                         
B99C: 00              BRK                         
B99D: 00              BRK                         
B99E: 00              BRK                         
B99F: 00              BRK                         
B9A0: 00              BRK                         
B9A1: 00              BRK                         
B9A2: 00              BRK                         
B9A3: 00              BRK                         
B9A4: 00              BRK                         
B9A5: 00              BRK                         
B9A6: 00              BRK                         
B9A7: 00              BRK                         
B9A8: 00              BRK                         
B9A9: 00              BRK                         
B9AA: 00              BRK                         
B9AB: 00              BRK                         
B9AC: 00              BRK                         
B9AD: 00              BRK                         
B9AE: 00              BRK                         
B9AF: 00              BRK                         
B9B0: 00              BRK                         
B9B1: 00              BRK                         
B9B2: 00              BRK                         
B9B3: 00              BRK                         
B9B4: 00              BRK                         
B9B5: 00              BRK                         
B9B6: 00              BRK                         
B9B7: 00              BRK                         
B9B8: 00              BRK                         
B9B9: 00              BRK                         
B9BA: 00              BRK                         
B9BB: 00              BRK                         
B9BC: 00              BRK                         
B9BD: 00              BRK                         
B9BE: 00              BRK                         
B9BF: 00              BRK                         
B9C0: 00              BRK                         
B9C1: 00              BRK                         
B9C2: 00              BRK                         
B9C3: 00              BRK                         
B9C4: 00              BRK                         
B9C5: 00              BRK                         
B9C6: 00              BRK                         
B9C7: 00              BRK                         
B9C8: 00              BRK                         
B9C9: 00              BRK                         
B9CA: 00              BRK                         
B9CB: 00              BRK                         
B9CC: 00              BRK                         
B9CD: 00              BRK                         
B9CE: 00              BRK                         
B9CF: 00              BRK                         
B9D0: 00              BRK                         
B9D1: 00              BRK                         
B9D2: 00              BRK                         
B9D3: 00              BRK                         
B9D4: 00              BRK                         
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
BA14: FF ; ????
BA15: FF ; ????
BA16: FF ; ????
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
BA34: FF ; ????
BA35: FF ; ????
BA36: FF ; ????
BA37: FF ; ????
BA38: FF ; ????
BA39: FF ; ????
BA3A: FF ; ????
BA3B: FF ; ????
BA3C: FF ; ????
BA3D: FF ; ????
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
BAA5: FF ; ????
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
BB79: 02 ; ????
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
BBF9: 01 00           ORA     ($00,X)             ; {ram.GP_00}
BBFB: 08              PHP                         
BBFC: 08              PHP                         
BBFD: 80 ; ????
BBFE: 00              BRK                         
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
BD87: 20 00 00        JSR     $0000               ; {ram.GP_00}
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
BF57: 40              RTI                         
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
BFF8: 00              BRK                         
BFF9: 00              BRK                         
BFFA: 00              BRK                         
BFFB: 00              BRK                         
BFFC: 02 ; ????
BFFD: 20 04 00        JSR     $0004               
```

