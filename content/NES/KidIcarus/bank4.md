![Bank 4](KidIcarus.jpg)

# Bank 4

>>> cpu 6502

>>> binary 8000:roms/KidIcarus.nes[10010:14010]

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](Hardware.md)

```code
8000: 4C 5A 80        JMP     $805A               ; {}
8003: 4C 0E 88        JMP     $880E               ; {}
8006: 4C 91 94        JMP     $9491               ; {}
8009: 4C 40 DF        JMP     $DF40               
800C: 4C 91 94        JMP     $9491               ; {}
800F: 4C 91 94        JMP     $9491               ; {}
8012: 4C 91 94        JMP     $9491               ; {}
8015: 4C 91 94        JMP     $9491               ; {}
8018: 4C 91 94        JMP     $9491               ; {}
801B: 4C 91 94        JMP     $9491               ; {}
801E: 4C 91 94        JMP     $9491               ; {}
8021: 4C 91 94        JMP     $9491               ; {}
8024: 4C 91 94        JMP     $9491               ; {}
8027: 4C 91 94        JMP     $9491               ; {}
802A: 4C 91 94        JMP     $9491               ; {}
802D: 4C 91 94        JMP     $9491               ; {}
8030: 4C 91 94        JMP     $9491               ; {}
8033: 4C 91 94        JMP     $9491               ; {}
8036: 4C 91 94        JMP     $9491               ; {}
8039: 4C 91 94        JMP     $9491               ; {}
803C: 4C 91 94        JMP     $9491               ; {}
803F: 4C 91 94        JMP     $9491               ; {}
8042: 67 ; ????
8043: C5 E7           CMP     $E7                 
8045: C5 91           CMP     $91                 
8047: 94 91           STY     $91,X               
8049: 94 91           STY     $91,X               
804B: 94 91           STY     $91,X               
804D: 94 91           STY     $91,X               
804F: 94 91           STY     $91,X               
8051: 94 91           STY     $91,X               
8053: 94 91           STY     $91,X               
8055: 94 91           STY     $91,X               
8057: 94 91           STY     $91,X               
8059: 94 20           STY     $20,X               
805B: 07 ; ????
805C: EB ; ????
805D: 20 F0 EE        JSR     $EEF0               
8060: 20 83 EF        JSR     $EF83               
8063: A9 00           LDA     #$00                
8065: 8D 4C 07        STA     $074C               
8068: 8D 4D 07        STA     $074D               
806B: 85 FE           STA     $FE                 
806D: 85 FD           STA     $FD                 
806F: 85 83           STA     $83                 
8071: 85 82           STA     $82                 
8073: A9 01           LDA     #$01                
8075: 85 1A           STA     $1A                 
8077: 20 89 81        JSR     $8189               ; {}
807A: 86 4B           STX     $4B                 
807C: 20 8A 86        JSR     $868A               ; {}
807F: A9 01           LDA     #$01                
8081: 20 CA 87        JSR     $87CA               ; {}
8084: A9 00           LDA     #$00                
8086: 20 E6 87        JSR     $87E6               ; {}
8089: A9 00           LDA     #$00                
808B: 85 14           STA     $14                 
808D: 85 15           STA     $15                 
808F: A9 01           LDA     #$01                
8091: 85 81           STA     $81                 
8093: A9 67           LDA     #$67                
8095: 85 37           STA     $37                 
8097: A9 88           LDA     #$88                
8099: 85 38           STA     $38                 
809B: A9 00           LDA     #$00                
809D: 85 3A           STA     $3A                 
809F: 8D 34 07        STA     $0734               
80A2: 8D 3A 07        STA     $073A               
80A5: 8D 40 07        STA     $0740               
80A8: 8D 46 07        STA     $0746               
80AB: A9 77           LDA     #$77                
80AD: 85 3D           STA     $3D                 
80AF: A9 E8           LDA     #$E8                
80B1: 85 3E           STA     $3E                 
80B3: A9 FF           LDA     #$FF                
80B5: 85 3F           STA     $3F                 
80B7: 20 F9 E3        JSR     $E3F9               
80BA: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
80BD: 10 FB           BPL     $80BA               ; {}
80BF: 20 87 EF        JSR     $EF87               
80C2: 20 01 EF        JSR     $EF01               
80C5: A5 81           LDA     $81                 
80C7: C9 07           CMP     #$07                
80C9: D0 FA           BNE     $80C5               ; {}
80CB: 20 F0 EE        JSR     $EEF0               
80CE: 20 83 EF        JSR     $EF83               
80D1: 20 E0 82        JSR     $82E0               ; {}
80D4: 20 87 EF        JSR     $EF87               
80D7: 20 01 EF        JSR     $EF01               
80DA: A5 81           LDA     $81                 
80DC: C9 08           CMP     #$08                
80DE: D0 FA           BNE     $80DA               ; {}
80E0: 20 F0 EE        JSR     $EEF0               
80E3: 20 83 EF        JSR     $EF83               
80E6: A9 8A           LDA     #$8A                
80E8: 85 30           STA     $30                 
80EA: A9 23           LDA     #$23                
80EC: 85 31           STA     $31                 
80EE: 20 77 EF        JSR     $EF77               
80F1: 20 F9 E3        JSR     $E3F9               
80F4: 20 6B 86        JSR     $866B               ; {}
80F7: A9 00           LDA     #$00                
80F9: 85 FE           STA     $FE                 
80FB: 85 1A           STA     $1A                 
80FD: 85 83           STA     $83                 
80FF: 85 82           STA     $82                 
8101: 20 0C 87        JSR     $870C               ; {}
8104: 20 D0 86        JSR     $86D0               ; {}
8107: A9 01           LDA     #$01                
8109: 20 0C 87        JSR     $870C               ; {}
810C: 20 D0 86        JSR     $86D0               ; {}
810F: A9 CF           LDA     #$CF                
8111: 85 FD           STA     $FD                 
8113: A9 04           LDA     #$04                
8115: 20 CA 87        JSR     $87CA               ; {}
8118: 20 87 EF        JSR     $EF87               
811B: 20 01 EF        JSR     $EF01               
811E: A5 81           LDA     $81                 
8120: C9 09           CMP     #$09                
8122: D0 FA           BNE     $811E               ; {}
8124: A5 F6           LDA     $F6                 
8126: 29 10           AND     #$10                
8128: F0 FA           BEQ     $8124               ; {}
812A: 20 F0 EE        JSR     $EEF0               
812D: A9 00           LDA     #$00                
812F: AA              TAX                         
8130: 9D 00 02        STA     $0200,X             
8133: 9D 00 03        STA     $0300,X             
8136: 9D 00 04        STA     $0400,X             
8139: 9D 00 05        STA     $0500,X             
813C: 9D 00 06        STA     $0600,X             
813F: 9D 00 07        STA     $0700,X             
8142: E8              INX                         
8143: D0 EB           BNE     $8130               ; {}
8145: A5 AA           LDA     $AA                 
8147: 48              PHA                         
8148: A5 A6           LDA     $A6                 
814A: 48              PHA                         
814B: A9 F0           LDA     #$F0                
814D: 20 3D C2        JSR     $C23D               
8150: 68              PLA                         
8151: 85 A6           STA     $A6                 
8153: 68              PLA                         
8154: 85 AA           STA     $AA                 
8156: A9 02           LDA     #$02                
8158: 85 A0           STA     $A0                 
815A: A9 03           LDA     #$03                
815C: 8D FA 6F        STA     $6FFA               
815F: A9 7F           LDA     #$7F                
8161: 8D FB 6F        STA     $6FFB               
8164: 20 07 EB        JSR     $EB07               
8167: A9 00           LDA     #$00                
8169: 8D 53 01        STA     $0153               
816C: 8D 54 01        STA     $0154               
816F: 8D 55 01        STA     $0155               
8172: 8D 4E 01        STA     $014E               
8175: 8D 51 01        STA     $0151               
8178: 8D 4F 01        STA     $014F               
817B: 8D 50 01        STA     $0150               
817E: A9 01           LDA     #$01                
8180: 8D 2A 60        STA     $602A               
8183: 20 89 EA        JSR     $EA89               
8186: 4C 6D C0        JMP     $C06D               
8189: A2 00           LDX     #$00                
818B: 20 98 81        JSR     $8198               ; {}
818E: 20 A7 81        JSR     $81A7               ; {}
8191: 20 AF 81        JSR     $81AF               ; {}
8194: 20 B8 81        JSR     $81B8               ; {}
8197: 60              RTS                         
8198: AD 4A 01        LDA     $014A               
819B: 38              SEC                         
819C: E9 E7           SBC     #$E7                
819E: AD 4B 01        LDA     $014B               
81A1: E9 03           SBC     #$03                
81A3: 90 01           BCC     $81A6               ; {}
81A5: E8              INX                         
81A6: 60              RTS                         
81A7: A5 AA           LDA     $AA                 
81A9: C9 04           CMP     #$04                
81AB: 90 01           BCC     $81AE               ; {}
81AD: E8              INX                         
81AE: 60              RTS                         
81AF: AD 52 01        LDA     $0152               
81B2: C9 04           CMP     #$04                
81B4: 90 01           BCC     $81B7               ; {}
81B6: E8              INX                         
81B7: 60              RTS                         
81B8: A9 02           LDA     #$02                
81BA: 2D 3E 01        AND     $013E               
81BD: F0 0B           BEQ     $81CA               ; {}
81BF: 2D 3F 01        AND     $013F               
81C2: F0 06           BEQ     $81CA               ; {}
81C4: 2D 40 01        AND     $0140               
81C7: F0 01           BEQ     $81CA               ; {}
81C9: E8              INX                         
81CA: 60              RTS                         
81CB: A5 86           LDA     $86                 
81CD: D0 03           BNE     $81D2               ; {}
81CF: 4C 42 EE        JMP     $EE42               
81D2: 4C BD 86        JMP     $86BD               ; {}
81D5: A5 81           LDA     $81                 
81D7: 0A              ASL     A                   
81D8: AA              TAX                         
81D9: BD E6 81        LDA     $81E6,X             ; {}
81DC: 85 00           STA     $00                 ; {ram.GP_00}
81DE: BD E7 81        LDA     $81E7,X             ; {}
81E1: 85 01           STA     $01                 
81E3: 6C 00 00        JMP     ($0000)             ; {ram.GP_00}
81E6: FA ; ????
81E7: 81 56           STA     ($56,X)             
81E9: 83 ; ????
81EA: A5 83           LDA     $83                 
81EC: BB ; ????
81ED: 83 ; ????
81EE: 49 84           EOR     #$84                
81F0: 68              PLA                         
81F1: 84 C2           STY     $C2                 
81F3: 84 FF           STY     $FF                 
81F5: 82 ; ????
81F6: 2E 83 55        ROL     $5583               
81F9: 83 ; ????
81FA: 60              RTS                         
81FB: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
81FE: A2 00           LDX     #$00                
8200: 20 1C 82        JSR     $821C               ; {}
8203: E8              INX                         
8204: 20 1C 82        JSR     $821C               ; {}
8207: E8              INX                         
8208: 20 1C 82        JSR     $821C               ; {}
820B: E8              INX                         
820C: 20 1C 82        JSR     $821C               ; {}
820F: E8              INX                         
8210: 20 1C 82        JSR     $821C               ; {}
8213: E8              INX                         
8214: 20 1C 82        JSR     $821C               ; {}
8217: E8              INX                         
8218: 20 1C 82        JSR     $821C               ; {}
821B: 60              RTS                         
821C: 8A              TXA                         
821D: 0A              ASL     A                   
821E: A8              TAY                         
821F: B9 44 82        LDA     $8244,Y             ; {}
8222: 85 00           STA     $00                 ; {ram.GP_00}
8224: B9 45 82        LDA     $8245,Y             ; {}
8227: 85 01           STA     $01                 
8229: A0 00           LDY     #$00                
822B: B1 00           LDA     ($00),Y             ; {ram.GP_00}
822D: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
8230: C8              INY                         
8231: B1 00           LDA     ($00),Y             ; {ram.GP_00}
8233: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
8236: C8              INY                         
8237: B1 00           LDA     ($00),Y             ; {ram.GP_00}
8239: C9 FF           CMP     #$FF                
823B: F0 06           BEQ     $8243               ; {}
823D: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
8240: 4C 36 82        JMP     $8236               ; {}
8243: 60              RTS                         
8244: 52 ; ????
8245: 82 ; ????
8246: 69 82           ADC     #$82                
8248: 82 ; ????
8249: 82 ; ????
824A: 9C ; ????
824B: 82 ; ????
824C: AE 82 BF        LDX     $BF82               ; {}
824F: 82 ; ????
8250: D0 82           BNE     $81D4               ; {}
8252: 21 04           AND     ($04,X)             
8254: 22 ; ????
8255: 1A ; ????
8256: 19 2A 28        ORA     $282A,Y             
8259: 16 12           ASL     $12,X               
825B: 2C 16 28        BIT     $2816               
825E: 12 ; ????
825F: 19 1A 28        ORA     $281A,Y             
8262: 29 27           AND     #$27                
8264: 24 2E           BIT     $2E                 
8266: 1A ; ????
8267: 19 FF 21        ORA     $21FF,Y             
826A: 44 ; ????
826B: 16 23           ASL     $23,X               
826D: 19 12 29        ORA     $2912,Y             
8270: 1D 1A 12        ORA     $121A,X             
8273: 21 1E           AND     ($1E,X)             
8275: 1C ; ????
8276: 1D 29 12        ORA     $1229,X             
8279: 24 1B           BIT     $1B                 
827B: 12 ; ????
827C: 25 1A           AND     $1A                 
827E: 16 18           ASL     $18,X               
8280: 1A ; ????
8281: FF ; ????
8282: 21 84           AND     ($84,X)             
8284: 27 ; ????
8285: 1A ; ????
8286: 29 2A           AND     #$2A                
8288: 27 ; ????
8289: 23 ; ????
828A: 1A ; ????
828B: 19 12 29        ORA     $2912,Y             
828E: 24 12           BIT     $12                 
8290: 16 23           ASL     $23,X               
8292: 1C ; ????
8293: 1A ; ????
8294: 21 12           AND     ($12,X)             
8296: 21 16           AND     ($16,X)             
8298: 23 ; ????
8299: 19 0D FF        ORA     $FF0D,Y             
829C: 21 C4           AND     ($C4,X)             
829E: 17 ; ????
829F: 2A              ROL     A                   
82A0: 29 12           AND     #$12                
82A2: 1E 23 12        ASL     $1223,X             
82A5: 24 27           BIT     $27                 
82A7: 19 1A 27        ORA     $271A,Y             
82AA: 12 ; ????
82AB: 29 24           AND     #$24                
82AD: FF ; ????
82AE: 22 ; ????
82AF: 04 ; ????
82B0: 22 ; ????
82B1: 16 1E           ASL     $1E,X               
82B3: 23 ; ????
82B4: 29 16           AND     #$16                
82B6: 1E 23 12        ASL     $1223,X             
82B9: 25 1A           AND     $1A                 
82BB: 16 18           ASL     $18,X               
82BD: 1A ; ????
82BE: FF ; ????
82BF: 22 ; ????
82C0: 44 ; ????
82C1: 25 1E           AND     $1E                 
82C3: 29 10           AND     #$10                
82C5: 28              PLP                         
82C6: 12 ; ????
82C7: 28              PLP                         
82C8: 29 27           AND     #$27                
82CA: 2A              ROL     A                   
82CB: 1C ; ????
82CC: 1C ; ????
82CD: 21 1A           AND     ($1A,X)             
82CF: FF ; ????
82D0: 22 ; ????
82D1: 84 18           STY     $18                 
82D3: 24 23           BIT     $23                 
82D5: 29 1E           AND     #$1E                
82D7: 23 ; ????
82D8: 2A              ROL     A                   
82D9: 1A ; ????
82DA: 28              PLP                         
82DB: 0D 0D 0D        ORA     $0D0D               
82DE: 0D FF A9        ORA     $A9FF               ; {}
82E1: 00              BRK                         
82E2: 85 14           STA     $14                 
82E4: 85 15           STA     $15                 
82E6: A2 00           LDX     #$00                
82E8: A9 F8           LDA     #$F8                
82EA: 9D 00 02        STA     $0200,X             
82ED: E8              INX                         
82EE: D0 F8           BNE     $82E8               ; {}
82F0: 20 73 EF        JSR     $EF73               
82F3: 20 FB 81        JSR     $81FB               ; {}
82F6: 20 C9 EB        JSR     $EBC9               
82F9: A9 0F           LDA     #$0F                
82FB: 8D 91 03        STA     $0391               
82FE: 60              RTS                         
82FF: A5 15           LDA     $15                 
8301: F0 09           BEQ     $830C               ; {}
8303: C9 01           CMP     #$01                
8305: F0 17           BEQ     $831E               ; {}
8307: C9 02           CMP     #$02                
8309: B0 1A           BCS     $8325               ; {}
830B: 60              RTS                         
830C: A5 14           LDA     $14                 
830E: 4A              LSR     A                   
830F: 4A              LSR     A                   
8310: 4A              LSR     A                   
8311: 4A              LSR     A                   
8312: C9 04           CMP     #$04                
8314: B0 07           BCS     $831D               ; {}
8316: A8              TAY                         
8317: B9 2A 83        LDA     $832A,Y             ; {}
831A: 8D 91 03        STA     $0391               
831D: 60              RTS                         
831E: A5 14           LDA     $14                 
8320: 49 FF           EOR     #$FF                
8322: 4C 0E 83        JMP     $830E               ; {}
8325: A9 08           LDA     #$08                
8327: 85 81           STA     $81                 
8329: 60              RTS                         
832A: 0F ; ????
832B: 00              BRK                         
832C: 10 20           BPL     $834E               ; {}
832E: A5 14           LDA     $14                 
8330: 29 01           AND     #$01                
8332: D0 20           BNE     $8354               ; {}
8334: E6 FD           INC     $FD                 
8336: A5 FD           LDA     $FD                 
8338: C9 F0           CMP     #$F0                
833A: 90 06           BCC     $8342               ; {}
833C: E6 1A           INC     $1A                 
833E: A9 00           LDA     #$00                
8340: 85 FD           STA     $FD                 
8342: 29 07           AND     #$07                
8344: D0 0E           BNE     $8354               ; {}
8346: A5 83           LDA     $83                 
8348: C9 F2           CMP     #$F2                
834A: B0 03           BCS     $834F               ; {}
834C: 4C 1C 87        JMP     $871C               ; {}
834F: A9 09           LDA     #$09                
8351: 85 81           STA     $81                 
8353: 60              RTS                         
8354: 60              RTS                         
8355: 60              RTS                         
8356: 20 4B 85        JSR     $854B               ; {}
8359: A5 3D           LDA     $3D                 
835B: 85 8D           STA     $8D                 
835D: A5 3E           LDA     $3E                 
835F: 18              CLC                         
8360: 69 01           ADC     #$01                
8362: 85 3E           STA     $3E                 
8364: 85 8E           STA     $8E                 
8366: A5 3F           LDA     $3F                 
8368: 69 00           ADC     #$00                
836A: 85 3F           STA     $3F                 
836C: 85 8B           STA     $8B                 
836E: A5 3E           LDA     $3E                 
8370: C9 68           CMP     #$68                
8372: 90 1C           BCC     $8390               ; {}
8374: A5 8B           LDA     $8B                 
8376: D0 18           BNE     $8390               ; {}
8378: A9 68           LDA     #$68                
837A: 85 8E           STA     $8E                 
837C: 85 3E           STA     $3E                 
837E: A9 03           LDA     #$03                
8380: A6 14           LDX     $14                 
8382: E0 C0           CPX     #$C0                
8384: 90 1A           BCC     $83A0               ; {}
8386: 20 6B 86        JSR     $866B               ; {}
8389: E6 81           INC     $81                 
838B: A9 03           LDA     #$03                
838D: 4C A0 83        JMP     $83A0               ; {}
8390: A5 14           LDA     $14                 
8392: 29 03           AND     #$03                
8394: D0 0C           BNE     $83A2               ; {}
8396: E6 40           INC     $40                 
8398: A5 40           LDA     $40                 
839A: C9 03           CMP     #$03                
839C: 90 04           BCC     $83A2               ; {}
839E: A9 00           LDA     #$00                
83A0: 85 40           STA     $40                 
83A2: 4C 2F 85        JMP     $852F               ; {}
83A5: A5 14           LDA     $14                 
83A7: F0 0C           BEQ     $83B5               ; {}
83A9: C9 40           CMP     #$40                
83AB: F0 03           BEQ     $83B0               ; {}
83AD: 4C 14 85        JMP     $8514               ; {}
83B0: E6 81           INC     $81                 
83B2: 20 6B 86        JSR     $866B               ; {}
83B5: 20 5F 86        JSR     $865F               ; {}
83B8: 4C 0F 85        JMP     $850F               ; {}
83BB: A5 15           LDA     $15                 
83BD: D0 1F           BNE     $83DE               ; {}
83BF: A5 14           LDA     $14                 
83C1: F0 07           BEQ     $83CA               ; {}
83C3: C9 80           CMP     #$80                
83C5: B0 08           BCS     $83CF               ; {}
83C7: 4C 14 85        JMP     $8514               ; {}
83CA: A9 80           LDA     #$80                
83CC: 85 14           STA     $14                 
83CE: 60              RTS                         
83CF: A2 04           LDX     #$04                
83D1: A5 14           LDA     $14                 
83D3: 29 20           AND     #$20                
83D5: F0 02           BEQ     $83D9               ; {}
83D7: A2 03           LDX     #$03                
83D9: 86 40           STX     $40                 
83DB: 4C 14 85        JMP     $8514               ; {}
83DE: C9 02           CMP     #$02                
83E0: 90 03           BCC     $83E5               ; {}
83E2: 4C 2C 84        JMP     $842C               ; {}
83E5: A2 01           LDX     #$01                
83E7: A5 14           LDA     $14                 
83E9: C9 C0           CMP     #$C0                
83EB: 90 02           BCC     $83EF               ; {}
83ED: A2 00           LDX     #$00                
83EF: 86 3A           STX     $3A                 
83F1: A2 03           LDX     #$03                
83F3: A5 14           LDA     $14                 
83F5: C9 80           CMP     #$80                
83F7: 90 0D           BCC     $8406               ; {}
83F9: C9 C0           CMP     #$C0                
83FB: B0 04           BCS     $8401               ; {}
83FD: 29 04           AND     #$04                
83FF: F0 05           BEQ     $8406               ; {}
8401: A4 4B           LDY     $4B                 
8403: BE DE 91        LDX     $91DE,Y             ; {}
8406: 86 40           STX     $40                 
8408: A5 14           LDA     $14                 
840A: C9 C0           CMP     #$C0                
840C: B0 11           BCS     $841F               ; {}
840E: 29 01           AND     #$01                
8410: D0 0D           BNE     $841F               ; {}
8412: A9 05           LDA     #$05                
8414: 20 CA 87        JSR     $87CA               ; {}
8417: A9 01           LDA     #$01                
8419: 20 E6 87        JSR     $87E6               ; {}
841C: 4C 14 85        JMP     $8514               ; {}
841F: A9 01           LDA     #$01                
8421: 20 CA 87        JSR     $87CA               ; {}
8424: A9 00           LDA     #$00                
8426: 20 E6 87        JSR     $87E6               ; {}
8429: 4C 14 85        JMP     $8514               ; {}
842C: A5 15           LDA     $15                 
842E: C9 03           CMP     #$03                
8430: B0 25           BCS     $8457               ; {}
8432: A5 14           LDA     $14                 
8434: C9 C0           CMP     #$C0                
8436: 90 2D           BCC     $8465               ; {}
8438: A2 04           LDX     #$04                
843A: A5 4B           LDA     $4B                 
843C: C9 03           CMP     #$03                
843E: 90 17           BCC     $8457               ; {}
8440: F0 02           BEQ     $8444               ; {}
8442: A2 05           LDX     #$05                
8444: 86 81           STX     $81                 
8446: 4C 6B 86        JMP     $866B               ; {}
8449: A9 09           LDA     #$09                
844B: 85 40           STA     $40                 
844D: A5 15           LDA     $15                 
844F: D0 06           BNE     $8457               ; {}
8451: A5 14           LDA     $14                 
8453: C9 C0           CMP     #$C0                
8455: 90 0E           BCC     $8465               ; {}
8457: AD 4D 07        LDA     $074D               
845A: C9 06           CMP     #$06                
845C: 90 07           BCC     $8465               ; {}
845E: A9 07           LDA     #$07                
8460: 85 81           STA     $81                 
8462: 20 6B 86        JSR     $866B               ; {}
8465: 4C 14 85        JMP     $8514               ; {}
8468: A5 15           LDA     $15                 
846A: D0 26           BNE     $8492               ; {}
846C: A5 14           LDA     $14                 
846E: C9 40           CMP     #$40                
8470: B0 03           BCS     $8475               ; {}
8472: 4C 14 85        JMP     $8514               ; {}
8475: A0 0A           LDY     #$0A                
8477: A2 02           LDX     #$02                
8479: A9 70           LDA     #$70                
847B: C5 38           CMP     $38                 
847D: B0 0C           BCS     $848B               ; {}
847F: A0 08           LDY     #$08                
8481: A2 03           LDX     #$03                
8483: A5 14           LDA     $14                 
8485: 29 03           AND     #$03                
8487: D0 02           BNE     $848B               ; {}
8489: C6 38           DEC     $38                 
848B: 86 3A           STX     $3A                 
848D: 84 40           STY     $40                 
848F: 4C 14 85        JMP     $8514               ; {}
8492: A5 14           LDA     $14                 
8494: C9 04           CMP     #$04                
8496: B0 03           BCS     $849B               ; {}
8498: 4C 14 85        JMP     $8514               ; {}
849B: D0 06           BNE     $84A3               ; {}
849D: 20 72 86        JSR     $8672               ; {}
84A0: 4C 0F 85        JMP     $850F               ; {}
84A3: A9 09           LDA     #$09                
84A5: 85 40           STA     $40                 
84A7: A9 78           LDA     #$78                
84A9: 85 38           STA     $38                 
84AB: A9 03           LDA     #$03                
84AD: 85 3A           STA     $3A                 
84AF: A9 06           LDA     #$06                
84B1: 85 81           STA     $81                 
84B3: A2 18           LDX     #$18                
84B5: A9 00           LDA     #$00                
84B7: 9D 34 07        STA     $0734,X             
84BA: 95 4C           STA     $4C,X               
84BC: CA              DEX                         
84BD: D0 F8           BNE     $84B7               ; {}
84BF: 4C 6B 86        JMP     $866B               ; {}
84C2: A5 15           LDA     $15                 
84C4: D0 35           BNE     $84FB               ; {}
84C6: A2 00           LDX     #$00                
84C8: A5 14           LDA     $14                 
84CA: C9 40           CMP     #$40                
84CC: B0 2D           BCS     $84FB               ; {}
84CE: 29 3F           AND     #$3F                
84D0: F0 0F           BEQ     $84E1               ; {}
84D2: E8              INX                         
84D3: C9 10           CMP     #$10                
84D5: F0 0A           BEQ     $84E1               ; {}
84D7: E8              INX                         
84D8: C9 20           CMP     #$20                
84DA: F0 05           BEQ     $84E1               ; {}
84DC: E8              INX                         
84DD: C9 30           CMP     #$30                
84DF: D0 1A           BNE     $84FB               ; {}
84E1: 8A              TXA                         
84E2: 48              PHA                         
84E3: E8              INX                         
84E4: 8A              TXA                         
84E5: 20 CA 87        JSR     $87CA               ; {}
84E8: 68              PLA                         
84E9: 85 00           STA     $00                 ; {ram.GP_00}
84EB: F0 09           BEQ     $84F6               ; {}
84ED: A9 00           LDA     #$00                
84EF: 18              CLC                         
84F0: 69 06           ADC     #$06                
84F2: C6 00           DEC     $00                 ; {ram.GP_00}
84F4: D0 F9           BNE     $84EF               ; {}
84F6: AA              TAX                         
84F7: A9 01           LDA     #$01                
84F9: 95 4C           STA     $4C,X               
84FB: 20 AF 85        JSR     $85AF               ; {}
84FE: 20 EF 85        JSR     $85EF               ; {}
8501: AD 4D 07        LDA     $074D               
8504: C9 06           CMP     #$06                
8506: 90 04           BCC     $850C               ; {}
8508: A9 07           LDA     #$07                
850A: 85 81           STA     $81                 
850C: 4C 14 85        JMP     $8514               ; {}
850F: A9 00           LDA     #$00                
8511: 20 EE 86        JSR     $86EE               ; {}
8514: 20 4B 85        JSR     $854B               ; {}
8517: A5 81           LDA     $81                 
8519: C9 06           CMP     #$06                
851B: 90 06           BCC     $8523               ; {}
851D: 20 26 86        JSR     $8626               ; {}
8520: 20 77 85        JSR     $8577               ; {}
8523: A5 3D           LDA     $3D                 
8525: 85 8D           STA     $8D                 
8527: A5 3E           LDA     $3E                 
8529: 85 8E           STA     $8E                 
852B: A9 00           LDA     #$00                
852D: 85 8B           STA     $8B                 
852F: A5 40           LDA     $40                 
8531: 0A              ASL     A                   
8532: AA              TAX                         
8533: BD EF 91        LDA     $91EF,X             ; {}
8536: 85 89           STA     $89                 
8538: BD F0 91        LDA     $91F0,X             ; {}
853B: 85 8A           STA     $8A                 
853D: A6 40           LDX     $40                 
853F: BD E4 91        LDA     $91E4,X             ; {}
8542: 85 8C           STA     $8C                 
8544: A9 00           LDA     #$00                
8546: 85 8F           STA     $8F                 
8548: 4C 6E 87        JMP     $876E               ; {}
854B: A5 37           LDA     $37                 
854D: 85 8D           STA     $8D                 
854F: A5 38           LDA     $38                 
8551: 85 8E           STA     $8E                 
8553: A5 3A           LDA     $3A                 
8555: 0A              ASL     A                   
8556: AA              TAX                         
8557: BD 61 93        LDA     $9361,X             ; {}
855A: 85 89           STA     $89                 
855C: BD 62 93        LDA     $9362,X             ; {}
855F: 85 8A           STA     $8A                 
8561: A2 0E           LDX     #$0E                
8563: A5 3A           LDA     $3A                 
8565: C9 03           CMP     #$03                
8567: D0 01           BNE     $856A               ; {}
8569: CA              DEX                         
856A: 86 8C           STX     $8C                 
856C: A9 00           LDA     #$00                
856E: 85 8B           STA     $8B                 
8570: A9 03           LDA     #$03                
8572: 85 8F           STA     $8F                 
8574: 4C 63 87        JMP     $8763               ; {}
8577: A2 00           LDX     #$00                
8579: 20 88 85        JSR     $8588               ; {}
857C: A2 06           LDX     #$06                
857E: 20 88 85        JSR     $8588               ; {}
8581: A2 0C           LDX     #$0C                
8583: 20 88 85        JSR     $8588               ; {}
8586: A2 12           LDX     #$12                
8588: BD 34 07        LDA     $0734,X             
858B: D0 01           BNE     $858E               ; {}
858D: 60              RTS                         
858E: BD 36 07        LDA     $0736,X             
8591: 85 8D           STA     $8D                 
8593: BD 37 07        LDA     $0737,X             
8596: 85 8E           STA     $8E                 
8598: A9 8D           LDA     #$8D                
859A: 85 89           STA     $89                 
859C: A9 94           LDA     #$94                
859E: 85 8A           STA     $8A                 
85A0: A9 01           LDA     #$01                
85A2: 85 8C           STA     $8C                 
85A4: A9 00           LDA     #$00                
85A6: 85 8B           STA     $8B                 
85A8: A9 01           LDA     #$01                
85AA: 85 8F           STA     $8F                 
85AC: 4C 6E 87        JMP     $876E               ; {}
85AF: A2 00           LDX     #$00                
85B1: 20 C0 85        JSR     $85C0               ; {}
85B4: A2 06           LDX     #$06                
85B6: 20 C0 85        JSR     $85C0               ; {}
85B9: A2 0C           LDX     #$0C                
85BB: 20 C0 85        JSR     $85C0               ; {}
85BE: A2 12           LDX     #$12                
85C0: B5 4C           LDA     $4C,X               
85C2: F0 2A           BEQ     $85EE               ; {}
85C4: B4 4D           LDY     $4D,X               
85C6: B9 19 89        LDA     $8919,Y             ; {}
85C9: 95 4E           STA     $4E,X               
85CB: B9 41 88        LDA     $8841,Y             ; {}
85CE: 95 4F           STA     $4F,X               
85D0: A5 14           LDA     $14                 
85D2: 29 03           AND     #$03                
85D4: D0 06           BNE     $85DC               ; {}
85D6: B5 51           LDA     $51,X               
85D8: 49 01           EOR     #$01                
85DA: 95 51           STA     $51,X               
85DC: A5 14           LDA     $14                 
85DE: 29 01           AND     #$01                
85E0: D0 0C           BNE     $85EE               ; {}
85E2: F6 4D           INC     $4D,X               
85E4: B5 4D           LDA     $4D,X               
85E6: C9 D8           CMP     #$D8                
85E8: D0 04           BNE     $85EE               ; {}
85EA: A9 18           LDA     #$18                
85EC: 95 4D           STA     $4D,X               
85EE: 60              RTS                         
85EF: A2 00           LDX     #$00                
85F1: 20 00 86        JSR     $8600               ; {}
85F4: A2 06           LDX     #$06                
85F6: 20 00 86        JSR     $8600               ; {}
85F9: A2 0C           LDX     #$0C                
85FB: 20 00 86        JSR     $8600               ; {}
85FE: A2 12           LDX     #$12                
8600: A5 15           LDA     $15                 
8602: D0 06           BNE     $860A               ; {}
8604: A5 14           LDA     $14                 
8606: C9 40           CMP     #$40                
8608: 90 1B           BCC     $8625               ; {}
860A: A5 14           LDA     $14                 
860C: 29 3F           AND     #$3F                
860E: D0 12           BNE     $8622               ; {}
8610: B5 4E           LDA     $4E,X               
8612: 18              CLC                         
8613: 69 10           ADC     #$10                
8615: 9D 36 07        STA     $0736,X             
8618: B5 4F           LDA     $4F,X               
861A: 9D 37 07        STA     $0737,X             
861D: A9 01           LDA     #$01                
861F: 9D 34 07        STA     $0734,X             
8622: FE 36 07        INC     $0736,X             
8625: 60              RTS                         
8626: A2 00           LDX     #$00                
8628: 20 37 86        JSR     $8637               ; {}
862B: A2 06           LDX     #$06                
862D: 20 37 86        JSR     $8637               ; {}
8630: A2 0C           LDX     #$0C                
8632: 20 37 86        JSR     $8637               ; {}
8635: A2 12           LDX     #$12                
8637: B5 4C           LDA     $4C,X               
8639: D0 01           BNE     $863C               ; {}
863B: 60              RTS                         
863C: B5 4E           LDA     $4E,X               
863E: 85 8D           STA     $8D                 
8640: B5 4F           LDA     $4F,X               
8642: 85 8E           STA     $8E                 
8644: B5 51           LDA     $51,X               
8646: 0A              ASL     A                   
8647: A8              TAY                         
8648: B9 45 94        LDA     $9445,Y             ; {}
864B: 85 89           STA     $89                 
864D: B9 46 94        LDA     $9446,Y             ; {}
8650: 85 8A           STA     $8A                 
8652: A9 04           LDA     #$04                
8654: 85 8C           STA     $8C                 
8656: A9 00           LDA     #$00                
8658: 85 8B           STA     $8B                 
865A: 85 8F           STA     $8F                 
865C: 4C 6E 87        JMP     $876E               ; {}
865F: A9 14           LDA     #$14                
8661: 85 00           STA     $00                 ; {ram.GP_00}
8663: A9 8E           LDA     #$8E                
8665: 85 01           STA     $01                 
8667: 20 7D 86        JSR     $867D               ; {}
866A: 60              RTS                         
866B: A9 FF           LDA     #$FF                
866D: 85 14           STA     $14                 
866F: 85 15           STA     $15                 
8671: 60              RTS                         
8672: A9 12           LDA     #$12                
8674: A2 1F           LDX     #$1F                
8676: 9D 0C 07        STA     $070C,X             
8679: CA              DEX                         
867A: 10 FA           BPL     $8676               ; {}
867C: 60              RTS                         
867D: A0 00           LDY     #$00                
867F: B1 00           LDA     ($00),Y             ; {ram.GP_00}
8681: 99 0C 07        STA     $070C,Y             
8684: C8              INY                         
8685: C0 20           CPY     #$20                
8687: D0 F6           BNE     $867F               ; {}
8689: 60              RTS                         
868A: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
868D: A9 20           LDA     #$20                
868F: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
8692: A9 00           LDA     #$00                
8694: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
8697: AA              TAX                         
8698: BD F1 89        LDA     $89F1,X             ; {}
869B: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
869E: E8              INX                         
869F: D0 F7           BNE     $8698               ; {}
86A1: BD F1 8A        LDA     $8AF1,X             ; {}
86A4: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
86A7: E8              INX                         
86A8: D0 F7           BNE     $86A1               ; {}
86AA: BD F1 8B        LDA     $8BF1,X             ; {}
86AD: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
86B0: E8              INX                         
86B1: D0 F7           BNE     $86AA               ; {}
86B3: BD F1 8C        LDA     $8CF1,X             ; {}
86B6: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
86B9: E8              INX                         
86BA: D0 F7           BNE     $86B3               ; {}
86BC: 60              RTS                         
86BD: 20 D0 86        JSR     $86D0               ; {}
86C0: A5 81           LDA     $81                 
86C2: C9 07           CMP     #$07                
86C4: 90 01           BCC     $86C7               ; {}
86C6: 60              RTS                         
86C7: A2 04           LDX     #$04                
86C9: B5 46           LDA     $46,X               
86CB: 95 41           STA     $41,X               
86CD: CA              DEX                         
86CE: 10 F9           BPL     $86C9               ; {}
86D0: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
86D3: A5 42           LDA     $42                 
86D5: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
86D8: A5 41           LDA     $41                 
86DA: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
86DD: A0 00           LDY     #$00                
86DF: B1 43           LDA     ($43),Y             
86E1: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
86E4: C8              INY                         
86E5: C4 45           CPY     $45                 
86E7: D0 F6           BNE     $86DF               ; {}
86E9: A9 00           LDA     #$00                
86EB: 85 86           STA     $86                 
86ED: 60              RTS                         
86EE: 0A              ASL     A                   
86EF: 85 00           STA     $00                 ; {ram.GP_00}
86F1: 0A              ASL     A                   
86F2: 0A              ASL     A                   
86F3: 18              CLC                         
86F4: 65 00           ADC     $00                 ; {ram.GP_00}
86F6: AA              TAX                         
86F7: A9 0A           LDA     #$0A                
86F9: 85 01           STA     $01                 
86FB: A0 00           LDY     #$00                
86FD: BD F1 8D        LDA     $8DF1,X             ; {}
8700: 99 41 00        STA     $0041,Y             
8703: E8              INX                         
8704: C8              INY                         
8705: C6 01           DEC     $01                 
8707: D0 F4           BNE     $86FD               ; {}
8709: E6 86           INC     $86                 
870B: 60              RTS                         
870C: 85 00           STA     $00                 ; {ram.GP_00}
870E: 0A              ASL     A                   
870F: 0A              ASL     A                   
8710: 18              CLC                         
8711: 65 00           ADC     $00                 ; {ram.GP_00}
8713: 18              CLC                         
8714: 69 0A           ADC     #$0A                
8716: AA              TAX                         
8717: A9 05           LDA     #$05                
8719: 4C F9 86        JMP     $86F9               ; {}
871C: A6 83           LDX     $83                 
871E: BD 34 8E        LDA     $8E34,X             ; {}
8721: 0A              ASL     A                   
8722: AA              TAX                         
8723: BD 26 8F        LDA     $8F26,X             ; {}
8726: 85 43           STA     $43                 
8728: BD 27 8F        LDA     $8F27,X             ; {}
872B: 85 44           STA     $44                 
872D: A9 0C           LDA     #$0C                
872F: 85 45           STA     $45                 
8731: A5 30           LDA     $30                 
8733: 85 41           STA     $41                 
8735: A5 31           LDA     $31                 
8737: 85 42           STA     $42                 
8739: A5 30           LDA     $30                 
873B: 18              CLC                         
873C: 69 20           ADC     #$20                
873E: 85 30           STA     $30                 
8740: A5 31           LDA     $31                 
8742: 69 00           ADC     #$00                
8744: 85 31           STA     $31                 
8746: 29 03           AND     #$03                
8748: C9 03           CMP     #$03                
874A: D0 12           BNE     $875E               ; {}
874C: A5 30           LDA     $30                 
874E: C9 C0           CMP     #$C0                
8750: 90 0C           BCC     $875E               ; {}
8752: A9 0A           LDA     #$0A                
8754: 85 30           STA     $30                 
8756: A5 31           LDA     $31                 
8758: 29 28           AND     #$28                
875A: 49 08           EOR     #$08                
875C: 85 31           STA     $31                 
875E: E6 86           INC     $86                 
8760: E6 83           INC     $83                 
8762: 60              RTS                         
8763: 20 F9 E3        JSR     $E3F9               
8766: A9 00           LDA     #$00                
8768: 85 87           STA     $87                 
876A: A9 02           LDA     #$02                
876C: 85 88           STA     $88                 
876E: A0 00           LDY     #$00                
8770: B1 89           LDA     ($89),Y             
8772: 18              CLC                         
8773: 65 8D           ADC     $8D                 
8775: 91 87           STA     ($87),Y             
8777: C8              INY                         
8778: B1 89           LDA     ($89),Y             
877A: 91 87           STA     ($87),Y             
877C: C8              INY                         
877D: B1 89           LDA     ($89),Y             
877F: 05 8F           ORA     $8F                 
8781: 91 87           STA     ($87),Y             
8783: C8              INY                         
8784: B1 89           LDA     ($89),Y             
8786: 30 0B           BMI     $8793               ; {}
8788: 18              CLC                         
8789: 65 8E           ADC     $8E                 
878B: AA              TAX                         
878C: A5 8B           LDA     $8B                 
878E: 69 00           ADC     #$00                
8790: 4C 9B 87        JMP     $879B               ; {}
8793: 18              CLC                         
8794: 65 8E           ADC     $8E                 
8796: AA              TAX                         
8797: A5 8B           LDA     $8B                 
8799: 69 FF           ADC     #$FF                
879B: D0 0F           BNE     $87AC               ; {}
879D: 8A              TXA                         
879E: 91 87           STA     ($87),Y             
87A0: C8              INY                         
87A1: C6 8C           DEC     $8C                 
87A3: D0 CB           BNE     $8770               ; {}
87A5: 98              TYA                         
87A6: 18              CLC                         
87A7: 65 87           ADC     $87                 
87A9: 85 87           STA     $87                 
87AB: 60              RTS                         
87AC: 88              DEY                         
87AD: 88              DEY                         
87AE: 88              DEY                         
87AF: A9 F0           LDA     #$F0                
87B1: 91 87           STA     ($87),Y             
87B3: C8              INY                         
87B4: C8              INY                         
87B5: C8              INY                         
87B6: 4C A0 87        JMP     $87A0               ; {}
87B9: A2 00           LDX     #$00                
87BB: 86 21           STX     $21                 
87BD: 0A              ASL     A                   
87BE: 26 21           ROL     $21                 
87C0: 0A              ASL     A                   
87C1: 26 21           ROL     $21                 
87C3: 0A              ASL     A                   
87C4: 26 21           ROL     $21                 
87C6: 0A              ASL     A                   
87C7: 26 21           ROL     $21                 
87C9: 60              RTS                         
87CA: 20 B9 87        JSR     $87B9               ; {}
87CD: 18              CLC                         
87CE: 69 5E           ADC     #$5E                
87D0: 85 20           STA     $20                 
87D2: A9 91           LDA     #$91                
87D4: 65 21           ADC     $21                 
87D6: 85 21           STA     $21                 
87D8: A0 00           LDY     #$00                
87DA: A2 10           LDX     #$10                
87DC: B1 20           LDA     ($20),Y             
87DE: 99 90 03        STA     $0390,Y             
87E1: C8              INY                         
87E2: CA              DEX                         
87E3: D0 F7           BNE     $87DC               ; {}
87E5: 60              RTS                         
87E6: 20 B9 87        JSR     $87B9               ; {}
87E9: 18              CLC                         
87EA: 69 BE           ADC     #$BE                
87EC: 85 20           STA     $20                 
87EE: A9 91           LDA     #$91                
87F0: 65 21           ADC     $21                 
87F2: 85 21           STA     $21                 
87F4: A0 00           LDY     #$00                
87F6: A2 10           LDX     #$10                
87F8: B1 20           LDA     ($20),Y             
87FA: 99 A0 03        STA     $03A0,Y             
87FD: C8              INY                         
87FE: CA              DEX                         
87FF: D0 F7           BNE     $87F8               ; {}
8801: 60              RTS                         
8802: 01 00           ORA     ($00,X)             ; {ram.GP_00}
8804: 00              BRK                         
8805: 02 ; ????
8806: 00              BRK                         
8807: 00              BRK                         
8808: 03 ; ????
8809: 00              BRK                         
880A: 00              BRK                         
880B: 04 ; ????
880C: 00              BRK                         
880D: 00              BRK                         
880E: 8A              TXA                         
880F: 48              PHA                         
8810: 98              TYA                         
8811: 48              PHA                         
8812: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
8815: 20 2E EB        JSR     $EB2E               
8818: A9 00           LDA     #$00                
881A: 8D 01 20        STA     $2001               ; {hard.P_CNTRL_2}
881D: 20 CB 81        JSR     $81CB               ; {}
8820: A5 FF           LDA     $FF                 
8822: 8D 01 20        STA     $2001               ; {hard.P_CNTRL_2}
8825: 20 C9 EB        JSR     $EBC9               
8828: 20 6A EE        JSR     $EE6A               
882B: 20 56 C8        JSR     $C856               
882E: 20 94 EE        JSR     $EE94               
8831: EE 4C 07        INC     $074C               
8834: D0 03           BNE     $8839               ; {}
8836: EE 4D 07        INC     $074D               
8839: 20 D5 81        JSR     $81D5               ; {}
883C: 68              PLA                         
883D: A8              TAY                         
883E: 68              PLA                         
883F: AA              TAX                         
8840: 60              RTS                         
8841: 80 ; ????
8842: 7E 7C 7A        ROR     $7A7C,X             
8845: 78              SEI                         
8846: 76 74           ROR     $74,X               
8848: 72 ; ????
8849: 70 6E           BVS     $88B9               ; {}
884B: 6C 6A 68        JMP     ($686A)             
884E: 66 64           ROR     $64                 
8850: 62 ; ????
8851: 60              RTS                         
8852: 5E 5C 5A        LSR     $5A5C,X             
8855: 58              CLI                         
8856: 56 54           LSR     $54,X               
8858: 52 ; ????
8859: 50 4E           BVC     $88A9               ; {}
885B: 4C 4A 48        JMP     $484A               
885E: 46 44           LSR     $44                 
8860: 44 ; ????
8861: 40              RTI                         
8862: 3E 3C 3A        ROL     $3A3C,X             
8865: 38              SEC                         
8866: 36 34           ROL     $34,X               
8868: 32 ; ????
8869: 30 2F           BMI     $889A               ; {}
886B: 2E 2D 2C        ROL     $2C2D               
886E: 2B ; ????
886F: 2A              ROL     A                   
8870: 29 28           AND     #$28                
8872: 29 2A           AND     #$2A                
8874: 2B ; ????
8875: 2C 2D 2E        BIT     $2E2D               
8878: 2F ; ????
8879: 30 32           BMI     $88AD               ; {}
887B: 34 ; ????
887C: 36 38           ROL     $38,X               
887E: 3A ; ????
887F: 3C ; ????
8880: 3E 40 42        ROL     $4240,X             
8883: 44 ; ????
8884: 46 48           LSR     $48                 
8886: 4A              LSR     A                   
8887: 4C 4E 50        JMP     $504E               
888A: 52 ; ????
888B: 54 ; ????
888C: 56 58           LSR     $58,X               
888E: 5A ; ????
888F: 5C ; ????
8890: 5E 60 62        LSR     $6260,X             
8893: 64 ; ????
8894: 66 68           ROR     $68                 
8896: 6A              ROR     A                   
8897: 6C 6E 70        JMP     ($706E)             
889A: 72 ; ????
889B: 74 ; ????
889C: 76 78           ROR     $78,X               
889E: 7A ; ????
889F: 7C ; ????
88A0: 7E 80 82        ROR     $8280,X             ; {}
88A3: 84 86           STY     $86                 
88A5: 88              DEY                         
88A6: 8A              TXA                         
88A7: 8C 8E 90        STY     $908E               ; {}
88AA: 92 ; ????
88AB: 94 96           STY     $96,X               
88AD: 98              TYA                         
88AE: 9A              TXS                         
88AF: 9C ; ????
88B0: 9E ; ????
88B1: A0 A2           LDY     #$A2                
88B3: A4 A6           LDY     $A6                 
88B5: A8              TAY                         
88B6: AA              TAX                         
88B7: AC AE B0        LDY     $B0AE               ; {}
88BA: B2 ; ????
88BB: B4 B6           LDY     $B6,X               
88BD: B8              CLV                         
88BE: BA              TSX                         
88BF: BC BE C0        LDY     $C0BE,X             
88C2: C2 ; ????
88C3: C4 C6           CPY     $C6                 
88C5: C8              INY                         
88C6: CA              DEX                         
88C7: CC CE D0        CPY     $D0CE               
88CA: D1 D2           CMP     ($D2),Y             
88CC: D3 ; ????
88CD: D4 ; ????
88CE: D5 D6           CMP     $D6,X               
88D0: D7 ; ????
88D1: D8              CLD                         
88D2: D7 ; ????
88D3: D6 D5           DEC     $D5,X               
88D5: D4 ; ????
88D6: D3 ; ????
88D7: D2 ; ????
88D8: D1 D0           CMP     ($D0),Y             
88DA: CE CC CA        DEC     $CACC               
88DD: C8              INY                         
88DE: C6 C4           DEC     $C4                 
88E0: C2 ; ????
88E1: C0 BE           CPY     #$BE                
88E3: BC BA B8        LDY     $B8BA,X             ; {}
88E6: B6 B4           LDX     $B4,Y               
88E8: B2 ; ????
88E9: B0 AE           BCS     $8899               ; {}
88EB: AC AA A8        LDY     $A8AA               ; {}
88EE: A6 A4           LDX     $A4                 
88F0: A2 A0           LDX     #$A0                
88F2: 9E ; ????
88F3: 9C ; ????
88F4: 9A              TXS                         
88F5: 98              TYA                         
88F6: 96 94           STX     $94,Y               
88F8: 92 ; ????
88F9: 90 8E           BCC     $8889               ; {}
88FB: 8C 8A 88        STY     $888A               ; {}
88FE: 86 84           STX     $84                 
8900: 82 ; ????
8901: 80 ; ????
8902: 7E 7C 7A        ROR     $7A7C,X             
8905: 78              SEI                         
8906: 76 74           ROR     $74,X               
8908: 72 ; ????
8909: 70 6E           BVS     $8979               ; {}
890B: 6C 6A 68        JMP     ($686A)             
890E: 66 64           ROR     $64                 
8910: 62 ; ????
8911: 60              RTS                         
8912: 5E 5C 5A        LSR     $5A5C,X             
8915: 58              CLI                         
8916: 56 54           LSR     $54,X               
8918: 52 ; ????
8919: 00              BRK                         
891A: 01 03           ORA     ($03,X)             
891C: 04 ; ????
891D: 06 07           ASL     $07                 
891F: 09 0A           ORA     #$0A                
8921: 0C ; ????
8922: 0D 0F 10        ORA     $100F               
8925: 12 ; ????
8926: 13 ; ????
8927: 15 16           ORA     $16,X               
8929: 17 ; ????
892A: 18              CLC                         
892B: 19 1A 1B        ORA     $1B1A,Y             
892E: 1C ; ????
892F: 1E 1F 20        ASL     $201F,X             
8932: 20 20 20        JSR     $2020               
8935: 20 20 20        JSR     $2020               
8938: 20 20 20        JSR     $2020               
893B: 20 20 20        JSR     $2020               
893E: 20 20 20        JSR     $2020               
8941: 20 22 24        JSR     $2422               
8944: 26 28           ROL     $28                 
8946: 2A              ROL     A                   
8947: 2C 2E 30        BIT     $302E               
894A: 32 ; ????
894B: 34 ; ????
894C: 36 38           ROL     $38,X               
894E: 3A ; ????
894F: 3C ; ????
8950: 3E 40 40        ROL     $4040,X             
8953: 40              RTI                         
8954: 40              RTI                         
8955: 40              RTI                         
8956: 40              RTI                         
8957: 40              RTI                         
8958: 40              RTI                         
8959: 40              RTI                         
895A: 40              RTI                         
895B: 40              RTI                         
895C: 40              RTI                         
895D: 40              RTI                         
895E: 40              RTI                         
895F: 40              RTI                         
8960: 40              RTI                         
8961: 40              RTI                         
8962: 3F ; ????
8963: 3E 3D 3C        ROL     $3C3D,X             
8966: 3B ; ????
8967: 3A ; ????
8968: 39 38 38        AND     $3838,Y             
896B: 37 ; ????
896C: 37 ; ????
896D: 36 36           ROL     $36,X               
896F: 35 35           AND     $35,X               
8971: 34 ; ????
8972: 34 ; ????
8973: 33 ; ????
8974: 33 ; ????
8975: 32 ; ????
8976: 32 ; ????
8977: 31 31           AND     ($31),Y             
8979: 30 30           BMI     $89AB               ; {}
897B: 2F ; ????
897C: 2F ; ????
897D: 2E 2E 2D        ROL     $2D2E               
8980: 2D 2C 2C        AND     $2C2C               
8983: 2B ; ????
8984: 2B ; ????
8985: 2A              ROL     A                   
8986: 2A              ROL     A                   
8987: 29 29           AND     #$29                
8989: 28              PLP                         
898A: 27 ; ????
898B: 26 25           ROL     $25                 
898D: 24 23           BIT     $23                 
898F: 22 ; ????
8990: 21 20           AND     ($20,X)             
8992: 20 20 20        JSR     $2020               
8995: 20 20 20        JSR     $2020               
8998: 20 20 20        JSR     $2020               
899B: 20 20 20        JSR     $2020               
899E: 20 20 20        JSR     $2020               
89A1: 20 22 24        JSR     $2422               
89A4: 26 28           ROL     $28                 
89A6: 2A              ROL     A                   
89A7: 2C 2E 30        BIT     $302E               
89AA: 32 ; ????
89AB: 34 ; ????
89AC: 36 38           ROL     $38,X               
89AE: 3A ; ????
89AF: 3C ; ????
89B0: 3E 40 40        ROL     $4040,X             
89B3: 40              RTI                         
89B4: 40              RTI                         
89B5: 40              RTI                         
89B6: 40              RTI                         
89B7: 40              RTI                         
89B8: 40              RTI                         
89B9: 40              RTI                         
89BA: 40              RTI                         
89BB: 40              RTI                         
89BC: 40              RTI                         
89BD: 40              RTI                         
89BE: 40              RTI                         
89BF: 40              RTI                         
89C0: 40              RTI                         
89C1: 40              RTI                         
89C2: 40              RTI                         
89C3: 3F ; ????
89C4: 3F ; ????
89C5: 3E 3E 3D        ROL     $3D3E,X             
89C8: 3D 3C 3C        AND     $3C3C,X             
89CB: 3B ; ????
89CC: 3B ; ????
89CD: 3A ; ????
89CE: 3A ; ????
89CF: 39 39 38        AND     $3839,Y             
89D2: 37 ; ????
89D3: 36 35           ROL     $35,X               
89D5: 34 ; ????
89D6: 33 ; ????
89D7: 32 ; ????
89D8: 31 30           AND     ($30),Y             
89DA: 2F ; ????
89DB: 2E 2D 2C        ROL     $2C2D               
89DE: 2B ; ????
89DF: 2A              ROL     A                   
89E0: 29 28           AND     #$28                
89E2: 28              PLP                         
89E3: 27 ; ????
89E4: 27 ; ????
89E5: 26 26           ROL     $26                 
89E7: 25 25           AND     $25                 
89E9: 24 24           BIT     $24                 
89EB: 23 ; ????
89EC: 23 ; ????
89ED: 22 ; ????
89EE: 22 ; ????
89EF: 21 21           AND     ($21,X)             
89F1: C0 C1           CPY     #$C1                
89F3: C1 C1           CMP     ($C1,X)             
89F5: 12 ; ????
89F6: 4F ; ????
89F7: 4E 4F 4E        LSR     $4E4F               
89FA: 4F ; ????
89FB: 4E 4F 4E        LSR     $4E4F               
89FE: 4F ; ????
89FF: 4E 4F 4E        LSR     $4E4F               
8A02: 4F ; ????
8A03: 4E 4F 4E        LSR     $4E4F               
8A06: 4F ; ????
8A07: 4E 4F 4E        LSR     $4E4F               
8A0A: 4F ; ????
8A0B: 4E 12 CD        LSR     $CD12               
8A0E: CD CD CD        CMP     $CDCD               
8A11: C0 C1           CPY     #$C1                
8A13: C1 C1           CMP     ($C1,X)             
8A15: 12 ; ????
8A16: 4E 4F 4E        LSR     $4E4F               
8A19: 4F ; ????
8A1A: 4E 4F 4E        LSR     $4E4F               
8A1D: 4F ; ????
8A1E: 4E 4F 4E        LSR     $4E4F               
8A21: 4F ; ????
8A22: 4E 4F 4E        LSR     $4E4F               
8A25: 4F ; ????
8A26: 4E 4F 4E        LSR     $4E4F               
8A29: 4F ; ????
8A2A: 4E 4F 12        LSR     $124F               
8A2D: CD CD CD        CMP     $CDCD               
8A30: CD C0 C1        CMP     $C1C0               
8A33: C1 C1           CMP     ($C1,X)             
8A35: 4E 4F 4E        LSR     $4E4F               
8A38: 4F ; ????
8A39: 4E 4F 4E        LSR     $4E4F               
8A3C: 4F ; ????
8A3D: 4E 4F 4E        LSR     $4E4F               
8A40: 4F ; ????
8A41: 4E 4F 4E        LSR     $4E4F               
8A44: 4F ; ????
8A45: 4E 4F 4E        LSR     $4E4F               
8A48: 4F ; ????
8A49: 4E 4F 4E        LSR     $4E4F               
8A4C: 4F ; ????
8A4D: CD CD CD        CMP     $CDCD               
8A50: CD C0 C1        CMP     $C1C0               
8A53: C1 C1           CMP     ($C1,X)             
8A55: 4F ; ????
8A56: 4E 4F 4E        LSR     $4E4F               
8A59: 4F ; ????
8A5A: 4E 4F 4E        LSR     $4E4F               
8A5D: 4F ; ????
8A5E: 4E 4F 4E        LSR     $4E4F               
8A61: 4F ; ????
8A62: 4E 4F 4E        LSR     $4E4F               
8A65: 4F ; ????
8A66: 4E 4F 4E        LSR     $4E4F               
8A69: 4F ; ????
8A6A: 4E 4F 4F        LSR     $4F4F               
8A6D: CD CD CD        CMP     $CDCD               
8A70: CD C0 C1        CMP     $C1C0               
8A73: C1 C1           CMP     ($C1,X)             
8A75: 8B ; ????
8A76: 8C 12 12        STY     $1212               
8A79: 12 ; ????
8A7A: 12 ; ????
8A7B: 12 ; ????
8A7C: 12 ; ????
8A7D: 12 ; ????
8A7E: 12 ; ????
8A7F: 12 ; ????
8A80: 12 ; ????
8A81: 12 ; ????
8A82: 12 ; ????
8A83: 12 ; ????
8A84: 12 ; ????
8A85: 12 ; ????
8A86: 12 ; ????
8A87: 12 ; ????
8A88: 12 ; ????
8A89: 12 ; ????
8A8A: 12 ; ????
8A8B: 8B ; ????
8A8C: 8C CD CD        STY     $CDCD               
8A8F: CD CD C0        CMP     $C0CD               
8A92: C1 C1           CMP     ($C1,X)             
8A94: C1 8D           CMP     ($8D,X)             
8A96: 8E 12 12        STX     $1212               
8A99: 12 ; ????
8A9A: 12 ; ????
8A9B: 12 ; ????
8A9C: 12 ; ????
8A9D: 12 ; ????
8A9E: 12 ; ????
8A9F: 12 ; ????
8AA0: 12 ; ????
8AA1: 12 ; ????
8AA2: 12 ; ????
8AA3: 12 ; ????
8AA4: 12 ; ????
8AA5: 12 ; ????
8AA6: 12 ; ????
8AA7: 12 ; ????
8AA8: 12 ; ????
8AA9: 12 ; ????
8AAA: 12 ; ????
8AAB: 8D 8E CD        STA     $CD8E               
8AAE: CD CD CD        CMP     $CDCD               
8AB1: C0 C1           CPY     #$C1                
8AB3: C1 C1           CMP     ($C1,X)             
8AB5: 8F ; ????
8AB6: 90 12           BCC     $8ACA               ; {}
8AB8: E0 12           CPX     #$12                
8ABA: 12 ; ????
8ABB: 12 ; ????
8ABC: 12 ; ????
8ABD: 12 ; ????
8ABE: 12 ; ????
8ABF: 12 ; ????
8AC0: 12 ; ????
8AC1: 12 ; ????
8AC2: 12 ; ????
8AC3: 12 ; ????
8AC4: 12 ; ????
8AC5: 12 ; ????
8AC6: 12 ; ????
8AC7: 12 ; ????
8AC8: 12 ; ????
8AC9: E0 12           CPX     #$12                
8ACB: 8F ; ????
8ACC: 90 CD           BCC     $8A9B               ; {}
8ACE: CD CD CD        CMP     $CDCD               
8AD1: C0 C1           CPY     #$C1                
8AD3: C1 C5           CMP     ($C5,X)             
8AD5: 6D 6E 12        ADC     $126E               
8AD8: E1 12           SBC     ($12,X)             
8ADA: 12 ; ????
8ADB: 12 ; ????
8ADC: 12 ; ????
8ADD: 12 ; ????
8ADE: 12 ; ????
8ADF: 12 ; ????
8AE0: 12 ; ????
8AE1: 12 ; ????
8AE2: 12 ; ????
8AE3: 12 ; ????
8AE4: 12 ; ????
8AE5: 12 ; ????
8AE6: 12 ; ????
8AE7: 12 ; ????
8AE8: 12 ; ????
8AE9: E1 12           SBC     ($12,X)             
8AEB: 6D 6E CE        ADC     $CE6E               
8AEE: CD CD CD        CMP     $CDCD               
8AF1: C0 C1           CPY     #$C1                
8AF3: C1 12           CMP     ($12,X)             
8AF5: 91 92           STA     ($92),Y             
8AF7: 12 ; ????
8AF8: E1 12           SBC     ($12,X)             
8AFA: E0 12           CPX     #$12                
8AFC: 12 ; ????
8AFD: 12 ; ????
8AFE: 12 ; ????
8AFF: 12 ; ????
8B00: 12 ; ????
8B01: 12 ; ????
8B02: 12 ; ????
8B03: 12 ; ????
8B04: 12 ; ????
8B05: 12 ; ????
8B06: 12 ; ????
8B07: E0 12           CPX     #$12                
8B09: E1 12           SBC     ($12,X)             
8B0B: 91 92           STA     ($92),Y             
8B0D: 12 ; ????
8B0E: CD CD CD        CMP     $CDCD               
8B11: C0 C1           CPY     #$C1                
8B13: C5 12           CMP     $12                 
8B15: 91 92           STA     ($92),Y             
8B17: 12 ; ????
8B18: E2 ; ????
8B19: 12 ; ????
8B1A: E1 12           SBC     ($12,X)             
8B1C: 12 ; ????
8B1D: 12 ; ????
8B1E: 12 ; ????
8B1F: 12 ; ????
8B20: 12 ; ????
8B21: 12 ; ????
8B22: 12 ; ????
8B23: 12 ; ????
8B24: 12 ; ????
8B25: 12 ; ????
8B26: 12 ; ????
8B27: E1 12           SBC     ($12,X)             
8B29: E2 ; ????
8B2A: 12 ; ????
8B2B: 91 92           STA     ($92),Y             
8B2D: 12 ; ????
8B2E: CE CD CD        DEC     $CDCD               
8B31: C0 C5           CPY     #$C5                
8B33: 12 ; ????
8B34: 12 ; ????
8B35: 91 92           STA     ($92),Y             
8B37: 12 ; ????
8B38: E2 ; ????
8B39: 12 ; ????
8B3A: E1 E4           SBC     ($E4,X)             
8B3C: 12 ; ????
8B3D: 12 ; ????
8B3E: 12 ; ????
8B3F: 12 ; ????
8B40: 12 ; ????
8B41: 12 ; ????
8B42: 12 ; ????
8B43: 12 ; ????
8B44: 12 ; ????
8B45: 12 ; ????
8B46: E4 E1           CPX     $E1                 
8B48: 12 ; ????
8B49: E2 ; ????
8B4A: 12 ; ????
8B4B: 91 92           STA     ($92),Y             
8B4D: 12 ; ????
8B4E: 12 ; ????
8B4F: CE CD C6        DEC     $C6CD               
8B52: C7 ; ????
8B53: 12 ; ????
8B54: 12 ; ????
8B55: 91 92           STA     ($92),Y             
8B57: 12 ; ????
8B58: E2 ; ????
8B59: 12 ; ????
8B5A: E2 ; ????
8B5B: E5 E4           SBC     $E4                 
8B5D: 12 ; ????
8B5E: 12 ; ????
8B5F: 12 ; ????
8B60: 12 ; ????
8B61: 12 ; ????
8B62: 12 ; ????
8B63: 12 ; ????
8B64: 12 ; ????
8B65: E4 E5           CPX     $E5                 
8B67: E2 ; ????
8B68: 12 ; ????
8B69: E2 ; ????
8B6A: 12 ; ????
8B6B: 91 92           STA     ($92),Y             
8B6D: 12 ; ????
8B6E: 12 ; ????
8B6F: C8              INY                         
8B70: C9 C2           CMP     #$C2                
8B72: C3 ; ????
8B73: 12 ; ????
8B74: 12 ; ????
8B75: 91 92           STA     ($92),Y             
8B77: 12 ; ????
8B78: E2 ; ????
8B79: 12 ; ????
8B7A: E2 ; ????
8B7B: E5 E5           SBC     $E5                 
8B7D: 12 ; ????
8B7E: 12 ; ????
8B7F: 12 ; ????
8B80: 12 ; ????
8B81: 12 ; ????
8B82: 12 ; ????
8B83: 12 ; ????
8B84: 12 ; ????
8B85: E5 E5           SBC     $E5                 
8B87: E2 ; ????
8B88: 12 ; ????
8B89: E2 ; ????
8B8A: 12 ; ????
8B8B: 91 92           STA     ($92),Y             
8B8D: 12 ; ????
8B8E: 12 ; ????
8B8F: CA              DEX                         
8B90: CB ; ????
8B91: C0 C4           CPY     #$C4                
8B93: 12 ; ????
8B94: 12 ; ????
8B95: 91 92           STA     ($92),Y             
8B97: 12 ; ????
8B98: E2 ; ????
8B99: 12 ; ????
8B9A: E2 ; ????
8B9B: E5 E5           SBC     $E5                 
8B9D: 12 ; ????
8B9E: 12 ; ????
8B9F: 12 ; ????
8BA0: 12 ; ????
8BA1: 12 ; ????
8BA2: 12 ; ????
8BA3: 12 ; ????
8BA4: 12 ; ????
8BA5: E5 E5           SBC     $E5                 
8BA7: E2 ; ????
8BA8: 12 ; ????
8BA9: E2 ; ????
8BAA: 12 ; ????
8BAB: 91 92           STA     ($92),Y             
8BAD: 12 ; ????
8BAE: 12 ; ????
8BAF: CC C0 C0        CPY     $C0C0               
8BB2: C1 12           CMP     ($12,X)             
8BB4: 12 ; ????
8BB5: 91 92           STA     ($92),Y             
8BB7: 12 ; ????
8BB8: E2 ; ????
8BB9: 12 ; ????
8BBA: E2 ; ????
8BBB: E5 E5           SBC     $E5                 
8BBD: 12 ; ????
8BBE: 12 ; ????
8BBF: 12 ; ????
8BC0: 12 ; ????
8BC1: 12 ; ????
8BC2: 12 ; ????
8BC3: 12 ; ????
8BC4: 12 ; ????
8BC5: E5 E5           SBC     $E5                 
8BC7: E2 ; ????
8BC8: 12 ; ????
8BC9: E2 ; ????
8BCA: 12 ; ????
8BCB: 91 92           STA     ($92),Y             
8BCD: 12 ; ????
8BCE: 12 ; ????
8BCF: CD C0 C0        CMP     $C0C0               
8BD2: C1 12           CMP     ($12,X)             
8BD4: 12 ; ????
8BD5: 91 92           STA     ($92),Y             
8BD7: 12 ; ????
8BD8: E2 ; ????
8BD9: 12 ; ????
8BDA: E2 ; ????
8BDB: E5 E5           SBC     $E5                 
8BDD: 12 ; ????
8BDE: 12 ; ????
8BDF: 12 ; ????
8BE0: 12 ; ????
8BE1: 12 ; ????
8BE2: 12 ; ????
8BE3: 12 ; ????
8BE4: 12 ; ????
8BE5: E5 E5           SBC     $E5                 
8BE7: E2 ; ????
8BE8: 12 ; ????
8BE9: E2 ; ????
8BEA: 12 ; ????
8BEB: 91 92           STA     ($92),Y             
8BED: 12 ; ????
8BEE: 12 ; ????
8BEF: CD C0 C0        CMP     $C0C0               
8BF2: C1 12           CMP     ($12,X)             
8BF4: 12 ; ????
8BF5: 8F ; ????
8BF6: 90 12           BCC     $8C0A               ; {}
8BF8: E3 ; ????
8BF9: 12 ; ????
8BFA: E3 ; ????
8BFB: E5 E5           SBC     $E5                 
8BFD: 12 ; ????
8BFE: 12 ; ????
8BFF: 12 ; ????
8C00: 12 ; ????
8C01: 12 ; ????
8C02: 12 ; ????
8C03: 12 ; ????
8C04: 12 ; ????
8C05: E5 E5           SBC     $E5                 
8C07: E3 ; ????
8C08: 12 ; ????
8C09: E3 ; ????
8C0A: 12 ; ????
8C0B: 8F ; ????
8C0C: 90 12           BCC     $8C20               ; {}
8C0E: 12 ; ????
8C0F: CD C0 C0        CMP     $C0C0               
8C12: C1 12           CMP     ($12,X)             
8C14: 12 ; ????
8C15: 6D 6E 12        ADC     $126E               
8C18: E3 ; ????
8C19: 12 ; ????
8C1A: E3 ; ????
8C1B: E6 E6           INC     $E6                 
8C1D: 12 ; ????
8C1E: 12 ; ????
8C1F: 12 ; ????
8C20: 12 ; ????
8C21: 12 ; ????
8C22: 12 ; ????
8C23: 12 ; ????
8C24: 12 ; ????
8C25: E6 E6           INC     $E6                 
8C27: E3 ; ????
8C28: 12 ; ????
8C29: E3 ; ????
8C2A: 12 ; ????
8C2B: 6D 6E 12        ADC     $126E               
8C2E: 12 ; ????
8C2F: CD C0 4E        CMP     $4EC0               
8C32: 4F ; ????
8C33: 79 79 79        ADC     $7979,Y             
8C36: 79 79 79        ADC     $7979,Y             
8C39: 79 79 60        ADC     $6079,Y             
8C3C: 61 60           ADC     ($60,X)             
8C3E: 61 60           ADC     ($60,X)             
8C40: 61 60           ADC     ($60,X)             
8C42: 61 60           ADC     ($60,X)             
8C44: 61 60           ADC     ($60,X)             
8C46: 61 79           ADC     ($79,X)             
8C48: 79 79 79        ADC     $7979,Y             
8C4B: 79 79 79        ADC     $7979,Y             
8C4E: 79 4E 4F        ADC     $4F4E,Y             
8C51: 4F ; ????
8C52: 4E 4F 12        LSR     $124F               
8C55: 12 ; ????
8C56: 12 ; ????
8C57: 12 ; ????
8C58: 12 ; ????
8C59: 12 ; ????
8C5A: 12 ; ????
8C5B: 4F ; ????
8C5C: 4E 4F 4E        LSR     $4E4F               
8C5F: 4F ; ????
8C60: 4E 4F 4E        LSR     $4E4F               
8C63: 4F ; ????
8C64: 4E 4F 4E        LSR     $4E4F               
8C67: 12 ; ????
8C68: 12 ; ????
8C69: 12 ; ????
8C6A: 12 ; ????
8C6B: 12 ; ????
8C6C: 12 ; ????
8C6D: 12 ; ????
8C6E: 12 ; ????
8C6F: 4F ; ????
8C70: 4E 4E 4F        LSR     $4F4E               
8C73: 4E 4F 12        LSR     $124F               
8C76: 6F ; ????
8C77: 6F ; ????
8C78: 6F ; ????
8C79: 75 76           ADC     $76,X               
8C7B: 4E 4F 12        LSR     $124F               
8C7E: 12 ; ????
8C7F: 12 ; ????
8C80: 12 ; ????
8C81: 12 ; ????
8C82: 12 ; ????
8C83: 12 ; ????
8C84: 12 ; ????
8C85: 4E 4F 75        LSR     $754F               
8C88: 76 6F           ROR     $6F,X               
8C8A: 6F ; ????
8C8B: 6F ; ????
8C8C: 6F ; ????
8C8D: 6F ; ????
8C8E: 6F ; ????
8C8F: 4E 4F 4F        LSR     $4F4F               
8C92: 4E 4F 4E        LSR     $4E4F               
8C95: 12 ; ????
8C96: 6F ; ????
8C97: 6F ; ????
8C98: 6F ; ????
8C99: 77 ; ????
8C9A: 78              SEI                         
8C9B: 4F ; ????
8C9C: 4E 12 12        LSR     $1212               
8C9F: 12 ; ????
8CA0: 12 ; ????
8CA1: 12 ; ????
8CA2: 12 ; ????
8CA3: 12 ; ????
8CA4: 12 ; ????
8CA5: 4F ; ????
8CA6: 4E 77 78        LSR     $7877               
8CA9: 6F ; ????
8CAA: 6F ; ????
8CAB: 6F ; ????
8CAC: 6F ; ????
8CAD: 6F ; ????
8CAE: 6F ; ????
8CAF: 4F ; ????
8CB0: 4E 4E 4F        LSR     $4F4E               
8CB3: 4E 4F 12        LSR     $124F               
8CB6: 6F ; ????
8CB7: 6F ; ????
8CB8: 6F ; ????
8CB9: 60              RTS                         
8CBA: 61 60           ADC     ($60,X)             
8CBC: 61 12           ADC     ($12,X)             
8CBE: 12 ; ????
8CBF: 12 ; ????
8CC0: 12 ; ????
8CC1: 12 ; ????
8CC2: 12 ; ????
8CC3: 12 ; ????
8CC4: 12 ; ????
8CC5: 60              RTS                         
8CC6: 61 60           ADC     ($60,X)             
8CC8: 61 12           ADC     ($12,X)             
8CCA: 6F ; ????
8CCB: 6F ; ????
8CCC: 6F ; ????
8CCD: 6F ; ????
8CCE: 6F ; ????
8CCF: 4E 4F 4F        LSR     $4F4F               
8CD2: 4E 12 6F        LSR     $6F12               
8CD5: 6F ; ????
8CD6: 6F ; ????
8CD7: 6F ; ????
8CD8: 6F ; ????
8CD9: 4E 4F 4F        LSR     $4F4F               
8CDC: 4E 12 12        LSR     $1212               
8CDF: 12 ; ????
8CE0: 12 ; ????
8CE1: 12 ; ????
8CE2: 12 ; ????
8CE3: 12 ; ????
8CE4: 12 ; ????
8CE5: 4F ; ????
8CE6: 4E 4F 4E        LSR     $4E4F               
8CE9: 12 ; ????
8CEA: 6F ; ????
8CEB: 6F ; ????
8CEC: 6F ; ????
8CED: 6F ; ????
8CEE: 6F ; ????
8CEF: 4F ; ????
8CF0: 4E 4E 4F        LSR     $4F4E               
8CF3: 12 ; ????
8CF4: 6F ; ????
8CF5: 6F ; ????
8CF6: 6F ; ????
8CF7: 75 76           ADC     $76,X               
8CF9: 4F ; ????
8CFA: 4E 12 12        LSR     $1212               
8CFD: 12 ; ????
8CFE: 12 ; ????
8CFF: 12 ; ????
8D00: 12 ; ????
8D01: 12 ; ????
8D02: 12 ; ????
8D03: 12 ; ????
8D04: 12 ; ????
8D05: 12 ; ????
8D06: 12 ; ????
8D07: 4E 4F 75        LSR     $754F               
8D0A: 76 6F           ROR     $6F,X               
8D0C: 6F ; ????
8D0D: 6F ; ????
8D0E: 6F ; ????
8D0F: 4E 4F 4F        LSR     $4F4F               
8D12: 4E 12 6F        LSR     $6F12               
8D15: 6F ; ????
8D16: 6F ; ????
8D17: 77 ; ????
8D18: 78              SEI                         
8D19: 4E 4F 12        LSR     $124F               
8D1C: 12 ; ????
8D1D: 12 ; ????
8D1E: 12 ; ????
8D1F: 12 ; ????
8D20: 12 ; ????
8D21: 12 ; ????
8D22: 12 ; ????
8D23: 12 ; ????
8D24: 12 ; ????
8D25: 12 ; ????
8D26: 12 ; ????
8D27: 4F ; ????
8D28: 4E 77 78        LSR     $7877               
8D2B: 6F ; ????
8D2C: 6F ; ????
8D2D: 6F ; ????
8D2E: 6F ; ????
8D2F: 4F ; ????
8D30: 4E 4E 4F        LSR     $4F4E               
8D33: 12 ; ????
8D34: 6F ; ????
8D35: 6F ; ????
8D36: 6F ; ????
8D37: 60              RTS                         
8D38: 61 60           ADC     ($60,X)             
8D3A: 61 12           ADC     ($12,X)             
8D3C: 12 ; ????
8D3D: 12 ; ????
8D3E: 12 ; ????
8D3F: 12 ; ????
8D40: 12 ; ????
8D41: 12 ; ????
8D42: 12 ; ????
8D43: 12 ; ????
8D44: 12 ; ????
8D45: 12 ; ????
8D46: 12 ; ????
8D47: 60              RTS                         
8D48: 61 60           ADC     ($60,X)             
8D4A: 61 12           ADC     ($12,X)             
8D4C: 6F ; ????
8D4D: 6F ; ????
8D4E: 6F ; ????
8D4F: 4E 4F 4F        LSR     $4F4F               
8D52: 4E 12 6F        LSR     $6F12               
8D55: 6F ; ????
8D56: 6F ; ????
8D57: 4E 4F 4E        LSR     $4E4F               
8D5A: 4F ; ????
8D5B: 12 ; ????
8D5C: 12 ; ????
8D5D: 12 ; ????
8D5E: 12 ; ????
8D5F: 12 ; ????
8D60: 12 ; ????
8D61: 12 ; ????
8D62: 12 ; ????
8D63: 12 ; ????
8D64: 12 ; ????
8D65: 12 ; ????
8D66: 12 ; ????
8D67: 4F ; ????
8D68: 4E 4F 4E        LSR     $4E4F               
8D6B: 12 ; ????
8D6C: 6F ; ????
8D6D: 6F ; ????
8D6E: 6F ; ????
8D6F: 4F ; ????
8D70: 4E 4E 4F        LSR     $4F4E               
8D73: 12 ; ????
8D74: 6F ; ????
8D75: 6F ; ????
8D76: 6F ; ????
8D77: 4F ; ????
8D78: 4E 12 12        LSR     $1212               
8D7B: 12 ; ????
8D7C: 12 ; ????
8D7D: 12 ; ????
8D7E: 12 ; ????
8D7F: 12 ; ????
8D80: 12 ; ????
8D81: 12 ; ????
8D82: 12 ; ????
8D83: 12 ; ????
8D84: 12 ; ????
8D85: 12 ; ????
8D86: 12 ; ????
8D87: 12 ; ????
8D88: 12 ; ????
8D89: 4E 4F 12        LSR     $124F               
8D8C: 6F ; ????
8D8D: 6F ; ????
8D8E: 6F ; ????
8D8F: 4E 4F 4F        LSR     $4F4F               
8D92: 4E 12 6F        LSR     $6F12               
8D95: 6F ; ????
8D96: 6F ; ????
8D97: 4E 4F 12        LSR     $124F               
8D9A: 12 ; ????
8D9B: 12 ; ????
8D9C: 12 ; ????
8D9D: 12 ; ????
8D9E: 12 ; ????
8D9F: 12 ; ????
8DA0: 12 ; ????
8DA1: 12 ; ????
8DA2: 12 ; ????
8DA3: 12 ; ????
8DA4: 12 ; ????
8DA5: 12 ; ????
8DA6: 12 ; ????
8DA7: 12 ; ????
8DA8: 12 ; ????
8DA9: 4F ; ????
8DAA: 4E 12 6F        LSR     $6F12               
8DAD: 6F ; ????
8DAE: 6F ; ????
8DAF: 4F ; ????
8DB0: 4E FF 00        LSR     $00FF               
8DB3: 00              BRK                         
8DB4: 00              BRK                         
8DB5: 00              BRK                         
8DB6: 00              BRK                         
8DB7: 00              BRK                         
8DB8: FF ; ????
8DB9: FF ; ????
8DBA: A2 00           LDX     #$00                
8DBC: 00              BRK                         
8DBD: 00              BRK                         
8DBE: 00              BRK                         
8DBF: A8              TAY                         
8DC0: FF ; ????
8DC1: 3F ; ????
8DC2: AA              TAX                         
8DC3: A2 00           LDX     #$00                
8DC5: 00              BRK                         
8DC6: A8              TAY                         
8DC7: AA              TAX                         
8DC8: CF ; ????
8DC9: 33 ; ????
8DCA: AA              TAX                         
8DCB: AA              TAX                         
8DCC: 00              BRK                         
8DCD: 00              BRK                         
8DCE: AA              TAX                         
8DCF: AA              TAX                         
8DD0: CC 03 0A        CPY     $0A03               
8DD3: 0A              ASL     A                   
8DD4: 00              BRK                         
8DD5: 00              BRK                         
8DD6: 0A              ASL     A                   
8DD7: 0A              ASL     A                   
8DD8: 0C ; ????
8DD9: 00              BRK                         
8DDA: 00              BRK                         
8DDB: 01 00           ORA     ($00,X)             ; {ram.GP_00}
8DDD: 00              BRK                         
8DDE: 04 ; ????
8DDF: 00              BRK                         
8DE0: 00              BRK                         
8DE1: 00              BRK                         
8DE2: 04 ; ????
8DE3: 00              BRK                         
8DE4: 00              BRK                         
8DE5: 00              BRK                         
8DE6: 00              BRK                         
8DE7: 01 00           ORA     ($00,X)             ; {ram.GP_00}
8DE9: 00              BRK                         
8DEA: 00              BRK                         
8DEB: 00              BRK                         
8DEC: 00              BRK                         
8DED: 00              BRK                         
8DEE: 00              BRK                         
8DEF: 00              BRK                         
8DF0: 00              BRK                         
8DF1: A8              TAY                         
8DF2: 20 0C 07        JSR     $070C               
8DF5: 10 E8           BPL     $8DDF               ; {}
8DF7: 20 1C 07        JSR     $071C               
8DFA: 10 C0           BPL     $8DBC               ; {}
8DFC: 23 ; ????
8DFD: 1E 91 40        ASL     $4091,X             
8E00: C0 2B           CPY     #$2B                
8E02: 1E 91 40        ASL     $4091,X             
8E05: 67 ; ????
8E06: 37 ; ????
8E07: 24 46           BIT     $46                 
8E09: 12 ; ????
8E0A: 23 ; ????
8E0B: 42 ; ????
8E0C: 29 21           AND     #$21                
8E0E: 28              PLP                         
8E0F: 1D 25 10        ORA     $1025,X             
8E12: 20 17 12        JSR     $1217               
8E15: 29 1D           AND     #$1D                
8E17: 16 23           ASL     $23,X               
8E19: 20 0F 2E        JSR     $2E0F               
8E1C: 24 2A           BIT     $2A                 
8E1E: 0C ; ????
8E1F: 25 1E           AND     $1E                 
8E21: 29 12           AND     #$12                
8E23: 12 ; ????
8E24: 12 ; ????
8E25: 12 ; ????
8E26: 12 ; ????
8E27: 12 ; ????
8E28: 12 ; ????
8E29: 12 ; ????
8E2A: 12 ; ????
8E2B: 12 ; ????
8E2C: 12 ; ????
8E2D: 12 ; ????
8E2E: 12 ; ????
8E2F: 12 ; ????
8E30: 12 ; ????
8E31: 12 ; ????
8E32: 12 ; ????
8E33: 12 ; ????
8E34: 01 00           ORA     ($00,X)             ; {ram.GP_00}
8E36: 00              BRK                         
8E37: 00              BRK                         
8E38: 00              BRK                         
8E39: 00              BRK                         
8E3A: 00              BRK                         
8E3B: 00              BRK                         
8E3C: 00              BRK                         
8E3D: 00              BRK                         
8E3E: 00              BRK                         
8E3F: 00              BRK                         
8E40: 00              BRK                         
8E41: 00              BRK                         
8E42: 00              BRK                         
8E43: 00              BRK                         
8E44: 00              BRK                         
8E45: 00              BRK                         
8E46: 02 ; ????
8E47: 00              BRK                         
8E48: 00              BRK                         
8E49: 03 ; ????
8E4A: 00              BRK                         
8E4B: 00              BRK                         
8E4C: 00              BRK                         
8E4D: 00              BRK                         
8E4E: 00              BRK                         
8E4F: 00              BRK                         
8E50: 00              BRK                         
8E51: 00              BRK                         
8E52: 00              BRK                         
8E53: 00              BRK                         
8E54: 00              BRK                         
8E55: 00              BRK                         
8E56: 04 ; ????
8E57: 00              BRK                         
8E58: 00              BRK                         
8E59: 05 00           ORA     $00                 ; {ram.GP_00}
8E5B: 00              BRK                         
8E5C: 00              BRK                         
8E5D: 00              BRK                         
8E5E: 00              BRK                         
8E5F: 00              BRK                         
8E60: 00              BRK                         
8E61: 00              BRK                         
8E62: 00              BRK                         
8E63: 00              BRK                         
8E64: 06 00           ASL     $00                 ; {ram.GP_00}
8E66: 00              BRK                         
8E67: 07 ; ????
8E68: 00              BRK                         
8E69: 00              BRK                         
8E6A: 00              BRK                         
8E6B: 00              BRK                         
8E6C: 00              BRK                         
8E6D: 00              BRK                         
8E6E: 00              BRK                         
8E6F: 00              BRK                         
8E70: 00              BRK                         
8E71: 00              BRK                         
8E72: 00              BRK                         
8E73: 00              BRK                         
8E74: 08              PHP                         
8E75: 00              BRK                         
8E76: 00              BRK                         
8E77: 09 00           ORA     #$00                
8E79: 00              BRK                         
8E7A: 00              BRK                         
8E7B: 00              BRK                         
8E7C: 00              BRK                         
8E7D: 00              BRK                         
8E7E: 00              BRK                         
8E7F: 00              BRK                         
8E80: 00              BRK                         
8E81: 00              BRK                         
8E82: 0A              ASL     A                   
8E83: 00              BRK                         
8E84: 00              BRK                         
8E85: 0B ; ????
8E86: 00              BRK                         
8E87: 0C ; ????
8E88: 00              BRK                         
8E89: 0D 00 00        ORA     $0000               ; {ram.GP_00}
8E8C: 00              BRK                         
8E8D: 00              BRK                         
8E8E: 00              BRK                         
8E8F: 00              BRK                         
8E90: 00              BRK                         
8E91: 00              BRK                         
8E92: 0E 00 00        ASL     $0000               ; {ram.GP_00}
8E95: 0F ; ????
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
8EA0: 10 00           BPL     $8EA2               ; {}
8EA2: 00              BRK                         
8EA3: 11 00           ORA     ($00),Y             ; {ram.GP_00}
8EA5: 12 ; ????
8EA6: 00              BRK                         
8EA7: 13 ; ????
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
8EB3: 14 ; ????
8EB4: 00              BRK                         
8EB5: 15 00           ORA     $00,X               ; {ram.GP_00}
8EB7: 16 00           ASL     $00,X               ; {ram.GP_00}
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
8ECE: 17 ; ????
8ECF: 00              BRK                         
8ED0: 00              BRK                         
8ED1: 18              CLC                         
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
8EDC: 19 00 00        ORA     $0000,Y             ; {ram.GP_00}
8EDF: 1A ; ????
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
8EEC: 1B ; ????
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
8EF8: 1C ; ????
8EF9: 00              BRK                         
8EFA: 00              BRK                         
8EFB: 1D 00 00        ORA     $0000,X             ; {ram.GP_00}
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
8F0D: 1E 00 1F        ASL     $1F00,X             
8F10: 00              BRK                         
8F11: 00              BRK                         
8F12: 00              BRK                         
8F13: 00              BRK                         
8F14: 00              BRK                         
8F15: 00              BRK                         
8F16: 20 21 00        JSR     $0021               
8F19: 00              BRK                         
8F1A: 00              BRK                         
8F1B: 22 ; ????
8F1C: 00              BRK                         
8F1D: 23 ; ????
8F1E: 00              BRK                         
8F1F: 00              BRK                         
8F20: 00              BRK                         
8F21: 00              BRK                         
8F22: 00              BRK                         
8F23: 00              BRK                         
8F24: 00              BRK                         
8F25: 00              BRK                         
8F26: 6E 8F 7A        ROR     $7A8F               
8F29: 8F ; ????
8F2A: 86 8F           STX     $8F                 
8F2C: 92 ; ????
8F2D: 8F ; ????
8F2E: 9E ; ????
8F2F: 8F ; ????
8F30: AA              TAX                         
8F31: 8F ; ????
8F32: B6 8F           LDX     $8F,Y               
8F34: C2 ; ????
8F35: 8F ; ????
8F36: CE 8F DA        DEC     $DA8F               
8F39: 8F ; ????
8F3A: E6 8F           INC     $8F                 
8F3C: F2 ; ????
8F3D: 8F ; ????
8F3E: FE 8F 0A        INC     $0A8F,X             
8F41: 90 16           BCC     $8F59               ; {}
8F43: 90 22           BCC     $8F67               ; {}
8F45: 90 2E           BCC     $8F75               ; {}
8F47: 90 3A           BCC     $8F83               ; {}
8F49: 90 46           BCC     $8F91               ; {}
8F4B: 90 52           BCC     $8F9F               ; {}
8F4D: 90 5E           BCC     $8FAD               ; {}
8F4F: 90 6A           BCC     $8FBB               ; {}
8F51: 90 76           BCC     $8FC9               ; {}
8F53: 90 82           BCC     $8ED7               ; {}
8F55: 90 8E           BCC     $8EE5               ; {}
8F57: 90 9A           BCC     $8EF3               ; {}
8F59: 90 A6           BCC     $8F01               ; {}
8F5B: 90 B2           BCC     $8F0F               ; {}
8F5D: 90 BE           BCC     $8F1D               ; {}
8F5F: 90 CA           BCC     $8F2B               ; {}
8F61: 90 D6           BCC     $8F39               ; {}
8F63: 90 E2           BCC     $8F47               ; {}
8F65: 90 EE           BCC     $8F55               ; {}
8F67: 90 FA           BCC     $8F63               ; {}
8F69: 90 06           BCC     $8F71               ; {}
8F6B: 91 12           STA     ($12),Y             
8F6D: 91 12           STA     ($12),Y             
8F6F: 12 ; ????
8F70: 12 ; ????
8F71: 12 ; ????
8F72: 12 ; ????
8F73: 12 ; ????
8F74: 12 ; ????
8F75: 12 ; ????
8F76: 12 ; ????
8F77: 12 ; ????
8F78: 12 ; ????
8F79: 12 ; ????
8F7A: 12 ; ????
8F7B: 12 ; ????
8F7C: 12 ; ????
8F7D: 28              PLP                         
8F7E: 29 16           AND     #$16                
8F80: 1B ; ????
8F81: 1B ; ????
8F82: 12 ; ????
8F83: 12 ; ????
8F84: 12 ; ????
8F85: 12 ; ????
8F86: 12 ; ????
8F87: 12 ; ????
8F88: 12 ; ????
8F89: 28              PLP                         
8F8A: 29 24           AND     #$24                
8F8C: 27 ; ????
8F8D: 2E 12 12        ROL     $1212               
8F90: 12 ; ????
8F91: 12 ; ????
8F92: 12 ; ????
8F93: 12 ; ????
8F94: 1E 23 2A        ASL     $2A23,X             
8F97: 28              PLP                         
8F98: 16 2C           ASL     $2C,X               
8F9A: 16 12           ASL     $12,X               
8F9C: 12 ; ????
8F9D: 12 ; ????
8F9E: 12 ; ????
8F9F: 18              CLC                         
8FA0: 1D 16 27        ORA     $2716,X             
8FA3: 16 18           ASL     $18,X               
8FA5: 29 1A           AND     #$1A                
8FA7: 27 ; ????
8FA8: 12 ; ????
8FA9: 12 ; ????
8FAA: 12 ; ????
8FAB: 12 ; ????
8FAC: 12 ; ????
8FAD: 12 ; ????
8FAE: 29 16           AND     #$16                
8FB0: 27 ; ????
8FB1: 24 12           BIT     $12                 
8FB3: 12 ; ????
8FB4: 12 ; ????
8FB5: 12 ; ????
8FB6: 12 ; ????
8FB7: 16 27           ASL     $27,X               
8FB9: 29 12           AND     #$12                
8FBB: 19 1A 28        ORA     $281A,Y             
8FBE: 1E 1C 23        ASL     $231C,X             
8FC1: 12 ; ????
8FC2: 12 ; ????
8FC3: 12 ; ????
8FC4: 22 ; ????
8FC5: 27 ; ????
8FC6: 0D 1D 16        ORA     $161D               
8FC9: 1E 1C 24        ASL     $241C,X             
8FCC: 12 ; ????
8FCD: 12 ; ????
8FCE: 29 1E           AND     #$1E                
8FD0: 29 21           AND     #$21                
8FD2: 1A ; ????
8FD3: 12 ; ????
8FD4: 19 1A 28        ORA     $281A,Y             
8FD7: 1E 1C 23        ASL     $231C,X             
8FDA: 12 ; ????
8FDB: 12 ; ????
8FDC: 22 ; ????
8FDD: 16 20           ASL     $20,X               
8FDF: 24 27           BIT     $27                 
8FE1: 1E 23 12        ASL     $1223,X             
8FE4: 12 ; ????
8FE5: 12 ; ????
8FE6: 12 ; ????
8FE7: 25 27           AND     $27                 
8FE9: 24 1C           BIT     $1C                 
8FEB: 27 ; ????
8FEC: 16 22           ASL     $22,X               
8FEE: 22 ; ????
8FEF: 1A ; ????
8FF0: 27 ; ????
8FF1: 28              PLP                         
8FF2: 12 ; ????
8FF3: 12 ; ????
8FF4: 17 ; ????
8FF5: 16 23           ASL     $23,X               
8FF7: 12 ; ????
8FF8: 17 ; ????
8FF9: 16 23           ASL     $23,X               
8FFB: 12 ; ????
8FFC: 12 ; ????
8FFD: 12 ; ????
8FFE: 12 ; ????
8FFF: 2E 24 28        ROL     $2824               
9002: 1D 1E 20        ORA     $201E,X             
9005: 16 2C           ASL     $2C,X               
9007: 16 12           ASL     $12,X               
9009: 12 ; ????
900A: 12 ; ????
900B: 12 ; ????
900C: 29 24           AND     #$24                
900E: 1C ; ????
900F: 16 2C           ASL     $2C,X               
9011: 16 12           ASL     $12,X               
9013: 12 ; ????
9014: 12 ; ????
9015: 12 ; ????
9016: 12 ; ????
9017: 12 ; ????
9018: 12 ; ????
9019: 28              PLP                         
901A: 24 2A           BIT     $2A                 
901C: 23 ; ????
901D: 19 12 12        ORA     $1212,Y             
9020: 12 ; ????
9021: 12 ; ????
9022: 12 ; ????
9023: 1D 1E 25        ORA     $251E,X             
9026: 12 ; ????
9027: 29 16           AND     #$16                
9029: 23 ; ????
902A: 16 20           ASL     $20,X               
902C: 16 12           ASL     $12,X               
902E: 12 ; ????
902F: 16 28           ASL     $28,X               
9031: 28              PLP                         
9032: 1E 28 29        ASL     $2928,X             
9035: 16 23           ASL     $23,X               
9037: 29 28           AND     #$28                
9039: 12 ; ????
903A: 12 ; ????
903B: 12 ; ????
903C: 22 ; ????
903D: 16 28           ASL     $28,X               
903F: 28              PLP                         
9040: 16 24           ASL     $24,X               
9042: 0D 2E 12        ORA     $122E               
9045: 12 ; ????
9046: 12 ; ????
9047: 12 ; ????
9048: 28              PLP                         
9049: 1D 1E 20        ORA     $201E,X             
904C: 16 24           ASL     $24,X               
904E: 0D 28 12        ORA     $1228               
9051: 12 ; ????
9052: 12 ; ????
9053: 12 ; ????
9054: 12 ; ????
9055: 1D 16 29        ORA     $2916,X             
9058: 16 17           ASL     $17,X               
905A: 24 12           BIT     $12                 
905C: 12 ; ????
905D: 12 ; ????
905E: 12 ; ????
905F: 12 ; ????
9060: 12 ; ????
9061: 20 1A 23        JSR     $231A               
9064: 1F ; ????
9065: 1E 12 12        ASL     $1212,X             
9068: 12 ; ????
9069: 12 ; ????
906A: 12 ; ????
906B: 12 ; ????
906C: 1D 2E 16        ORA     $162E,X             
906F: 20 20 16        JSR     $1620               
9072: 23 ; ????
9073: 12 ; ????
9074: 12 ; ????
9075: 12 ; ????
9076: 12 ; ????
9077: 12 ; ????
9078: 20 1A 1D        JSR     $1D1A               
907B: 1E 27 24        ASL     $2427,X             
907E: 1F ; ????
907F: 1E 12 12        ASL     $1212,X             
9082: 12 ; ????
9083: 12 ; ????
9084: 19 1E 27        ORA     $271E,Y             
9087: 1A ; ????
9088: 18              CLC                         
9089: 29 24           AND     #$24                
908B: 27 ; ????
908C: 12 ; ????
908D: 12 ; ????
908E: 12 ; ????
908F: 12 ; ????
9090: 28              PLP                         
9091: 0D 24 20        ORA     $2024               
9094: 16 19           ASL     $19,X               
9096: 16 12           ASL     $12,X               
9098: 12 ; ????
9099: 12 ; ????
909A: 12 ; ????
909B: 12 ; ????
909C: 25 27           AND     $27                 
909E: 24 19           BIT     $19                 
90A0: 2A              ROL     A                   
90A1: 18              CLC                         
90A2: 1A ; ????
90A3: 27 ; ????
90A4: 12 ; ????
90A5: 12 ; ????
90A6: 12 ; ????
90A7: 12 ; ????
90A8: 1C ; ????
90A9: 0D 2E 24        ORA     $242E               
90AC: 20 24 1E        JSR     $1E24               
90AF: 12 ; ????
90B0: 12 ; ????
90B1: 12 ; ????
90B2: 12 ; ????
90B3: 12 ; ????
90B4: 12 ; ????
90B5: 12 ; ????
90B6: 16 23           ASL     $23,X               
90B8: 19 0D 0D        ORA     $0D0D,Y             
90BB: 0D 0D 12        ORA     $120D               
90BE: 12 ; ????
90BF: 29 1D           AND     #$1D                
90C1: 1A ; ????
90C2: 12 ; ????
90C3: 1D 1A 27        ORA     $271A,X             
90C6: 24 0E           BIT     $0E                 
90C8: 12 ; ????
90C9: 12 ; ????
90CA: 12 ; ????
90CB: 12 ; ????
90CC: 12 ; ????
90CD: 12 ; ????
90CE: 2E 24 2A        ROL     $2A24               
90D1: 12 ; ????
90D2: 12 ; ????
90D3: 12 ; ????
90D4: 12 ; ????
90D5: 12 ; ????
90D6: 12 ; ????
90D7: 18              CLC                         
90D8: 24 25           BIT     $25                 
90DA: 2E 27 1E        ROL     $1E27               
90DD: 1C ; ????
90DE: 1D 29 12        ORA     $1229,X             
90E1: 12 ; ????
90E2: 01 09           ORA     ($09,X)             
90E4: 08              PHP                         
90E5: 06 23           ASL     $23                 
90E7: 1E 23 29        ASL     $2923,X             
90EA: 1A ; ????
90EB: 23 ; ????
90EC: 19 24 29        ORA     $2924,Y             
90EF: 1D 1A D0        ORA     $D01A,X             
90F2: D1 D2           CMP     ($D2),Y             
90F4: D3 ; ????
90F5: D4 ; ????
90F6: D5 12           CMP     $12,X               
90F8: 12 ; ????
90F9: 12 ; ????
90FA: 12 ; ????
90FB: 12 ; ????
90FC: 12 ; ????
90FD: D6 D7           DEC     $D7,X               
90FF: D8              CLD                         
9100: D9 DA DB        CMP     $DBDA,Y             
9103: 12 ; ????
9104: 12 ; ????
9105: 12 ; ????
9106: 12 ; ????
9107: 12 ; ????
9108: 12 ; ????
9109: 12 ; ????
910A: 25 2A           AND     $2A                 
910C: 28              PLP                         
910D: 1D 12 12        ORA     $1212,X             
9110: 12 ; ????
9111: 12 ; ????
9112: 28              PLP                         
9113: 29 16           AND     #$16                
9115: 27 ; ????
9116: 29 12           AND     #$12                
9118: 17 ; ????
9119: 2A              ROL     A                   
911A: 29 29           AND     #$29                
911C: 24 23           BIT     $23                 
911E: F0 F0           BEQ     $9110               ; {}
9120: F0 F0           BEQ     $9112               ; {}
9122: F0 F0           BEQ     $9114               ; {}
9124: F0 F0           BEQ     $9116               ; {}
9126: 00              BRK                         
9127: 00              BRK                         
9128: 00              BRK                         
9129: 00              BRK                         
912A: 00              BRK                         
912B: 00              BRK                         
912C: 00              BRK                         
912D: 00              BRK                         
912E: 00              BRK                         
912F: 00              BRK                         
9130: 00              BRK                         
9131: 00              BRK                         
9132: 00              BRK                         
9133: 00              BRK                         
9134: 00              BRK                         
9135: 00              BRK                         
9136: 50 50           BVC     $9188               ; {}
9138: 50 50           BVC     $918A               ; {}
913A: 50 50           BVC     $918C               ; {}
913C: 50 50           BVC     $918E               ; {}
913E: 0F ; ????
913F: 0F ; ????
9140: 0F ; ????
9141: 0F ; ????
9142: 0F ; ????
9143: 0F ; ????
9144: 0F ; ????
9145: 0F ; ????
9146: 00              BRK                         
9147: 00              BRK                         
9148: 00              BRK                         
9149: 00              BRK                         
914A: 00              BRK                         
914B: 00              BRK                         
914C: 00              BRK                         
914D: 00              BRK                         
914E: 00              BRK                         
914F: 00              BRK                         
9150: 00              BRK                         
9151: 00              BRK                         
9152: 00              BRK                         
9153: 00              BRK                         
9154: 00              BRK                         
9155: 00              BRK                         
9156: 05 05           ORA     $05                 
9158: 05 05           ORA     $05                 
915A: 05 05           ORA     $05                 
915C: 05 05           ORA     $05                 
915E: 0F ; ????
915F: 30 30           BMI     $9191               ; {}
9161: 30 0F           BMI     $9172               ; {}
9163: 0F ; ????
9164: 0F ; ????
9165: 0F ; ????
9166: 0F ; ????
9167: 0F ; ????
9168: 0F ; ????
9169: 0F ; ????
916A: 0F ; ????
916B: 0F ; ????
916C: 0F ; ????
916D: 0F ; ????
916E: 0F ; ????
916F: 20 22 02        JSR     $0222               
9172: 0F ; ????
9173: 0F ; ????
9174: 0F ; ????
9175: 0F ; ????
9176: 0F ; ????
9177: 0F ; ????
9178: 0F ; ????
9179: 0F ; ????
917A: 0F ; ????
917B: 0F ; ????
917C: 0F ; ????
917D: 0F ; ????
917E: 0F ; ????
917F: 20 22 02        JSR     $0222               
9182: 0F ; ????
9183: 06 07           ASL     $07                 
9185: 0F ; ????
9186: 0F ; ????
9187: 00              BRK                         
9188: 0F ; ????
9189: 0F ; ????
918A: 0F ; ????
918B: 01 08           ORA     ($08,X)             
918D: 0F ; ????
918E: 0F ; ????
918F: 20 22 02        JSR     $0222               
9192: 0F ; ????
9193: 16 05           ASL     $05,X               
9195: 07 ; ????
9196: 0F ; ????
9197: 10 00           BPL     $9199               ; {}
9199: 0F ; ????
919A: 0F ; ????
919B: 11 17           ORA     ($17),Y             
919D: 0B ; ????
919E: 0F ; ????
919F: 20 22 02        JSR     $0222               
91A2: 0F ; ????
91A3: 24 25           BIT     $25                 
91A5: 06 0F           ASL     $0F                 
91A7: 37 ; ????
91A8: 10 00           BPL     $91AA               ; {}
91AA: 0F ; ????
91AB: 2C 27 1A        BIT     $1A27               
91AE: 10 20           BPL     $91D0               ; {}
91B0: 22 ; ????
91B1: 02 ; ????
91B2: 10 10           BPL     $91C4               ; {}
91B4: 10 10           BPL     $91C6               ; {}
91B6: 10 10           BPL     $91C8               ; {}
91B8: 10 10           BPL     $91CA               ; {}
91BA: 10 10           BPL     $91CC               ; {}
91BC: 10 10           BPL     $91CE               ; {}
91BE: 0F ; ????
91BF: 20 26 07        JSR     $0726               
91C2: 0F ; ????
91C3: 31 02           AND     ($02),Y             
91C5: 15 0F           ORA     $0F,X               
91C7: 11 24           ORA     ($24),Y             
91C9: 31 0F           AND     ($0F),Y             
91CB: 2A              ROL     A                   
91CC: 36 26           ROL     $26,X               
91CE: 10 30           BPL     $9200               ; {}
91D0: 30 30           BMI     $9202               ; {}
91D2: 10 31           BPL     $9205               ; {}
91D4: 02 ; ????
91D5: 15 10           ORA     $10,X               
91D7: 11 24           ORA     ($24),Y             
91D9: 31 10           AND     ($10),Y             
91DB: 2A              ROL     A                   
91DC: 36 26           ROL     $26,X               
91DE: 05 06           ORA     $06                 
91E0: 07 ; ????
91E1: 08              PHP                         
91E2: 08              PHP                         
91E3: 03 ; ????
91E4: 06 06           ASL     $06                 
91E6: 06 06           ASL     $06                 
91E8: 06 06           ASL     $06                 
91EA: 06 08           ASL     $08                 
91EC: 0D 0D 0B        ORA     $0B0D               
91EF: 05 92           ORA     $92                 
91F1: 1D 92 35        ORA     $3592,X             
91F4: 92 ; ????
91F5: 4D 92 65        EOR     $6592               
91F8: 92 ; ????
91F9: 7D 92 95        ADC     $9592,X             ; {}
91FC: 92 ; ????
91FD: AD 92 CD        LDA     $CD92               
9200: 92 ; ????
9201: 01 93           ORA     ($93,X)             
9203: 35 93           AND     $93,X               
9205: 00              BRK                         
9206: 01 40           ORA     ($40,X)             
9208: 01 00           ORA     ($00,X)             ; {ram.GP_00}
920A: 00              BRK                         
920B: 40              RTI                         
920C: 09 08           ORA     #$08                
920E: 11 40           ORA     ($40),Y             
9210: 01 08           ORA     ($08,X)             
9212: 10 40           BPL     $9254               ; {}
9214: 09 10           ORA     #$10                
9216: 21 40           AND     ($40,X)             
9218: 00              BRK                         
9219: 10 20           BPL     $923B               ; {}
921B: 40              RTI                         
921C: 08              PHP                         
921D: 01 01           ORA     ($01,X)             
921F: 40              RTI                         
9220: 00              BRK                         
9221: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9223: 40              RTI                         
9224: 08              PHP                         
9225: 09 11           ORA     #$11                
9227: 40              RTI                         
9228: 00              BRK                         
9229: 09 10           ORA     #$10                
922B: 40              RTI                         
922C: 08              PHP                         
922D: 10 23           BPL     $9252               ; {}
922F: 40              RTI                         
9230: 00              BRK                         
9231: 10 22           BPL     $9255               ; {}
9233: 40              RTI                         
9234: 08              PHP                         
9235: 00              BRK                         
9236: 01 40           ORA     ($40,X)             
9238: 00              BRK                         
9239: 00              BRK                         
923A: 00              BRK                         
923B: 40              RTI                         
923C: 08              PHP                         
923D: 08              PHP                         
923E: 11 40           ORA     ($40),Y             
9240: 00              BRK                         
9241: 08              PHP                         
9242: 10 40           BPL     $9284               ; {}
9244: 08              PHP                         
9245: 10 25           BPL     $926C               ; {}
9247: 40              RTI                         
9248: 00              BRK                         
9249: 10 24           BPL     $926F               ; {}
924B: 40              RTI                         
924C: 08              PHP                         
924D: 00              BRK                         
924E: E5 00           SBC     $00                 ; {ram.GP_00}
9250: 00              BRK                         
9251: 00              BRK                         
9252: E5 40           SBC     $40                 
9254: 08              PHP                         
9255: 08              PHP                         
9256: E6 00           INC     $00                 ; {ram.GP_00}
9258: 00              BRK                         
9259: 08              PHP                         
925A: E6 40           INC     $40                 
925C: 08              PHP                         
925D: 10 E7           BPL     $9246               ; {}
925F: 00              BRK                         
9260: 00              BRK                         
9261: 10 E7           BPL     $924A               ; {}
9263: 40              RTI                         
9264: 08              PHP                         
9265: 00              BRK                         
9266: E8              INX                         
9267: 00              BRK                         
9268: 00              BRK                         
9269: 00              BRK                         
926A: E8              INX                         
926B: 40              RTI                         
926C: 08              PHP                         
926D: 08              PHP                         
926E: E9 00           SBC     #$00                
9270: 00              BRK                         
9271: 08              PHP                         
9272: E9 40           SBC     #$40                
9274: 08              PHP                         
9275: 10 E7           BPL     $925E               ; {}
9277: 00              BRK                         
9278: 00              BRK                         
9279: 10 E7           BPL     $9262               ; {}
927B: 40              RTI                         
927C: 08              PHP                         
927D: 00              BRK                         
927E: DC ; ????
927F: 00              BRK                         
9280: 00              BRK                         
9281: 00              BRK                         
9282: DD 00 08        CMP     $0800,X             
9285: 08              PHP                         
9286: DE 00 00        DEC     $0000,X             ; {ram.GP_00}
9289: 08              PHP                         
928A: E6 40           INC     $40                 
928C: 08              PHP                         
928D: 10 E7           BPL     $9276               ; {}
928F: 00              BRK                         
9290: 00              BRK                         
9291: 10 E7           BPL     $927A               ; {}
9293: 40              RTI                         
9294: 08              PHP                         
9295: 00              BRK                         
9296: C0 00           CPY     #$00                
9298: 00              BRK                         
9299: 00              BRK                         
929A: C1 00           CMP     ($00,X)             ; {ram.GP_00}
929C: 08              PHP                         
929D: 08              PHP                         
929E: DE 00 00        DEC     $0000,X             ; {ram.GP_00}
92A1: 08              PHP                         
92A2: E6 40           INC     $40                 
92A4: 08              PHP                         
92A5: 10 E7           BPL     $928E               ; {}
92A7: 00              BRK                         
92A8: 00              BRK                         
92A9: 10 E7           BPL     $9292               ; {}
92AB: 40              RTI                         
92AC: 08              PHP                         
92AD: F8              SED                         
92AE: C2 ; ????
92AF: 01 00           ORA     ($00,X)             ; {ram.GP_00}
92B1: F8              SED                         
92B2: C3 ; ????
92B3: 01 08           ORA     ($08,X)             
92B5: 00              BRK                         
92B6: C0 00           CPY     #$00                
92B8: 00              BRK                         
92B9: 00              BRK                         
92BA: C1 00           CMP     ($00,X)             ; {ram.GP_00}
92BC: 08              PHP                         
92BD: 08              PHP                         
92BE: DE 00 00        DEC     $0000,X             ; {ram.GP_00}
92C1: 08              PHP                         
92C2: E6 40           INC     $40                 
92C4: 08              PHP                         
92C5: 10 E7           BPL     $92AE               ; {}
92C7: 00              BRK                         
92C8: 00              BRK                         
92C9: 10 E7           BPL     $92B2               ; {}
92CB: 40              RTI                         
92CC: 08              PHP                         
92CD: F0 EA           BEQ     $92B9               ; {}
92CF: 00              BRK                         
92D0: 00              BRK                         
92D1: F0 EB           BEQ     $92BE               ; {}
92D3: 00              BRK                         
92D4: 08              PHP                         
92D5: F0 EC           BEQ     $92C3               ; {}
92D7: 00              BRK                         
92D8: 10 F8           BPL     $92D2               ; {}
92DA: ED 00 00        SBC     $0000               ; {ram.GP_00}
92DD: F8              SED                         
92DE: EE 00 08        INC     $0800               
92E1: F8              SED                         
92E2: EF ; ????
92E3: 00              BRK                         
92E4: 10 00           BPL     $92E6               ; {}
92E6: D0 00           BNE     $92E8               ; {}
92E8: 00              BRK                         
92E9: 00              BRK                         
92EA: D1 00           CMP     ($00),Y             ; {ram.GP_00}
92EC: 08              PHP                         
92ED: 08              PHP                         
92EE: D2 ; ????
92EF: 00              BRK                         
92F0: 00              BRK                         
92F1: 08              PHP                         
92F2: D3 ; ????
92F3: 00              BRK                         
92F4: 08              PHP                         
92F5: 10 D4           BPL     $92CB               ; {}
92F7: 00              BRK                         
92F8: 00              BRK                         
92F9: 10 D5           BPL     $92D0               ; {}
92FB: 00              BRK                         
92FC: 08              PHP                         
92FD: 10 D6           BPL     $92D5               ; {}
92FF: 00              BRK                         
9300: 10 F0           BPL     $92F2               ; {}
9302: EA              NOP                         
9303: 00              BRK                         
9304: 00              BRK                         
9305: F0 EB           BEQ     $92F2               ; {}
9307: 00              BRK                         
9308: 08              PHP                         
9309: F0 EC           BEQ     $92F7               ; {}
930B: 00              BRK                         
930C: 10 F8           BPL     $9306               ; {}
930E: ED 00 00        SBC     $0000               ; {ram.GP_00}
9311: F8              SED                         
9312: FB ; ????
9313: 00              BRK                         
9314: 08              PHP                         
9315: F8              SED                         
9316: EF ; ????
9317: 00              BRK                         
9318: 10 00           BPL     $931A               ; {}
931A: D0 00           BNE     $931C               ; {}
931C: 00              BRK                         
931D: 00              BRK                         
931E: D1 00           CMP     ($00),Y             ; {ram.GP_00}
9320: 08              PHP                         
9321: 08              PHP                         
9322: D2 ; ????
9323: 00              BRK                         
9324: 00              BRK                         
9325: 08              PHP                         
9326: D3 ; ????
9327: 00              BRK                         
9328: 08              PHP                         
9329: 10 D4           BPL     $92FF               ; {}
932B: 00              BRK                         
932C: 00              BRK                         
932D: 10 D5           BPL     $9304               ; {}
932F: 00              BRK                         
9330: 08              PHP                         
9331: 10 D6           BPL     $9309               ; {}
9333: 00              BRK                         
9334: 10 F0           BPL     $9326               ; {}
9336: EA              NOP                         
9337: 00              BRK                         
9338: 00              BRK                         
9339: F0 EB           BEQ     $9326               ; {}
933B: 00              BRK                         
933C: 08              PHP                         
933D: F8              SED                         
933E: ED 00 00        SBC     $0000               ; {ram.GP_00}
9341: F8              SED                         
9342: FB ; ????
9343: 00              BRK                         
9344: 08              PHP                         
9345: 00              BRK                         
9346: D0 00           BNE     $9348               ; {}
9348: 00              BRK                         
9349: 00              BRK                         
934A: D1 00           CMP     ($00),Y             ; {ram.GP_00}
934C: 08              PHP                         
934D: 08              PHP                         
934E: D2 ; ????
934F: 00              BRK                         
9350: 00              BRK                         
9351: 08              PHP                         
9352: D3 ; ????
9353: 00              BRK                         
9354: 08              PHP                         
9355: 10 D4           BPL     $932B               ; {}
9357: 00              BRK                         
9358: 00              BRK                         
9359: 10 D5           BPL     $9330               ; {}
935B: 00              BRK                         
935C: 08              PHP                         
935D: 10 D6           BPL     $9335               ; {}
935F: 00              BRK                         
9360: 10 69           BPL     $93CB               ; {}
9362: 93 ; ????
9363: A1 93           LDA     ($93,X)             
9365: D9 93 11        CMP     $1193,Y             
9368: 94 00           STY     $00,X               ; {ram.GP_00}
936A: E0 00           CPX     #$00                
936C: 00              BRK                         
936D: 00              BRK                         
936E: F1 00           SBC     ($00),Y             ; {ram.GP_00}
9370: 08              PHP                         
9371: 00              BRK                         
9372: F2 ; ????
9373: 00              BRK                         
9374: 10 08           BPL     $937E               ; {}
9376: E1 00           SBC     ($00,X)             ; {ram.GP_00}
9378: 00              BRK                         
9379: 08              PHP                         
937A: F4 ; ????
937B: 00              BRK                         
937C: 08              PHP                         
937D: 08              PHP                         
937E: F5 00           SBC     $00,X               ; {ram.GP_00}
9380: 10 10           BPL     $9392               ; {}
9382: E2 ; ????
9383: 00              BRK                         
9384: 00              BRK                         
9385: 10 F7           BPL     $937E               ; {}
9387: 00              BRK                         
9388: 08              PHP                         
9389: 10 F8           BPL     $9383               ; {}
938B: 00              BRK                         
938C: 10 18           BPL     $93A6               ; {}
938E: E3 ; ????
938F: 00              BRK                         
9390: 00              BRK                         
9391: 18              CLC                         
9392: FA ; ????
9393: 00              BRK                         
9394: 08              PHP                         
9395: 20 E4 00        JSR     $00E4               
9398: 00              BRK                         
9399: 20 FD 00        JSR     $00FD               
939C: 08              PHP                         
939D: 20 FE 00        JSR     $00FE               
93A0: 10 00           BPL     $93A2               ; {}
93A2: F0 00           BEQ     $93A4               ; {}
93A4: 00              BRK                         
93A5: 00              BRK                         
93A6: F1 00           SBC     ($00),Y             ; {ram.GP_00}
93A8: 08              PHP                         
93A9: 00              BRK                         
93AA: F2 ; ????
93AB: 00              BRK                         
93AC: 10 08           BPL     $93B6               ; {}
93AE: F3 ; ????
93AF: 00              BRK                         
93B0: 00              BRK                         
93B1: 08              PHP                         
93B2: F4 ; ????
93B3: 00              BRK                         
93B4: 08              PHP                         
93B5: 08              PHP                         
93B6: F5 00           SBC     $00,X               ; {ram.GP_00}
93B8: 10 10           BPL     $93CA               ; {}
93BA: F6 00           INC     $00,X               ; {ram.GP_00}
93BC: 00              BRK                         
93BD: 10 F7           BPL     $93B6               ; {}
93BF: 00              BRK                         
93C0: 08              PHP                         
93C1: 10 F8           BPL     $93BB               ; {}
93C3: 00              BRK                         
93C4: 10 18           BPL     $93DE               ; {}
93C6: F9 00 00        SBC     $0000,Y             ; {ram.GP_00}
93C9: 18              CLC                         
93CA: FA ; ????
93CB: 00              BRK                         
93CC: 08              PHP                         
93CD: 20 FC 00        JSR     $00FC               
93D0: 00              BRK                         
93D1: 20 FD 00        JSR     $00FD               
93D4: 08              PHP                         
93D5: 20 FE 00        JSR     $00FE               
93D8: 10 00           BPL     $93DA               ; {}
93DA: C4 00           CPY     $00                 ; {ram.GP_00}
93DC: 00              BRK                         
93DD: 00              BRK                         
93DE: C5 00           CMP     $00                 ; {ram.GP_00}
93E0: 08              PHP                         
93E1: 00              BRK                         
93E2: C6 00           DEC     $00                 ; {ram.GP_00}
93E4: 10 08           BPL     $93EE               ; {}
93E6: C7 ; ????
93E7: 00              BRK                         
93E8: 00              BRK                         
93E9: 08              PHP                         
93EA: C8              INY                         
93EB: 00              BRK                         
93EC: 08              PHP                         
93ED: 08              PHP                         
93EE: F5 00           SBC     $00,X               ; {ram.GP_00}
93F0: 10 10           BPL     $9402               ; {}
93F2: C9 00           CMP     #$00                
93F4: 00              BRK                         
93F5: 10 F7           BPL     $93EE               ; {}
93F7: 00              BRK                         
93F8: 08              PHP                         
93F9: 10 F8           BPL     $93F3               ; {}
93FB: 00              BRK                         
93FC: 10 18           BPL     $9416               ; {}
93FE: CA              DEX                         
93FF: 00              BRK                         
9400: 00              BRK                         
9401: 18              CLC                         
9402: FA ; ????
9403: 00              BRK                         
9404: 08              PHP                         
9405: 20 FC 00        JSR     $00FC               
9408: 00              BRK                         
9409: 20 FD 00        JSR     $00FD               
940C: 08              PHP                         
940D: 20 FE 00        JSR     $00FE               
9410: 10 00           BPL     $9412               ; {}
9412: E0 00           CPX     #$00                
9414: 00              BRK                         
9415: 00              BRK                         
9416: F1 00           SBC     ($00),Y             ; {ram.GP_00}
9418: 08              PHP                         
9419: 00              BRK                         
941A: F2 ; ????
941B: 00              BRK                         
941C: 10 08           BPL     $9426               ; {}
941E: F4 ; ????
941F: 00              BRK                         
9420: 08              PHP                         
9421: 08              PHP                         
9422: F5 00           SBC     $00,X               ; {ram.GP_00}
9424: 10 10           BPL     $9436               ; {}
9426: C9 00           CMP     #$00                
9428: 00              BRK                         
9429: 10 F7           BPL     $9422               ; {}
942B: 00              BRK                         
942C: 08              PHP                         
942D: 10 F8           BPL     $9427               ; {}
942F: 00              BRK                         
9430: 10 18           BPL     $944A               ; {}
9432: CA              DEX                         
9433: 00              BRK                         
9434: 00              BRK                         
9435: 18              CLC                         
9436: FA ; ????
9437: 00              BRK                         
9438: 08              PHP                         
9439: 20 FC 00        JSR     $00FC               
943C: 00              BRK                         
943D: 20 FD 00        JSR     $00FD               
9440: 08              PHP                         
9441: 20 FE 00        JSR     $00FE               
9444: 10 4D           BPL     $9493               ; {}
9446: 94 5D           STY     $5D,X               
9448: 94 6D           STY     $6D,X               
944A: 94 7D           STY     $7D,X               
944C: 94 00           STY     $00,X               ; {ram.GP_00}
944E: D7 ; ????
944F: 00              BRK                         
9450: 00              BRK                         
9451: 00              BRK                         
9452: D8              CLD                         
9453: 00              BRK                         
9454: 08              PHP                         
9455: 08              PHP                         
9456: DA ; ????
9457: 00              BRK                         
9458: 00              BRK                         
9459: 08              PHP                         
945A: DB ; ????
945B: 00              BRK                         
945C: 08              PHP                         
945D: 00              BRK                         
945E: D7 ; ????
945F: 00              BRK                         
9460: 00              BRK                         
9461: 00              BRK                         
9462: D9 00 08        CMP     $0800,Y             
9465: 08              PHP                         
9466: DA ; ????
9467: 00              BRK                         
9468: 00              BRK                         
9469: 08              PHP                         
946A: DB ; ????
946B: 00              BRK                         
946C: 08              PHP                         
946D: 00              BRK                         
946E: D7 ; ????
946F: 40              RTI                         
9470: 08              PHP                         
9471: 00              BRK                         
9472: D8              CLD                         
9473: 40              RTI                         
9474: 00              BRK                         
9475: 08              PHP                         
9476: DA ; ????
9477: 40              RTI                         
9478: 08              PHP                         
9479: 08              PHP                         
947A: DB ; ????
947B: 40              RTI                         
947C: 00              BRK                         
947D: 00              BRK                         
947E: D7 ; ????
947F: 40              RTI                         
9480: 08              PHP                         
9481: 00              BRK                         
9482: D8              CLD                         
9483: 40              RTI                         
9484: 00              BRK                         
9485: 08              PHP                         
9486: DA ; ????
9487: 40              RTI                         
9488: 08              PHP                         
9489: 08              PHP                         
948A: DB ; ????
948B: 40              RTI                         
948C: 00              BRK                         
948D: 00              BRK                         
948E: FF ; ????
948F: 00              BRK                         
9490: 00              BRK                         
9491: FF ; ????
9492: FF ; ????
9493: FF ; ????
9494: FF ; ????
9495: FF ; ????
9496: FF ; ????
9497: FF ; ????
9498: FF ; ????
9499: FF ; ????
949A: FF ; ????
949B: FF ; ????
949C: FF ; ????
949D: FF ; ????
949E: FF ; ????
949F: FF ; ????
94A0: FF ; ????
94A1: FF ; ????
94A2: FF ; ????
94A3: FF ; ????
94A4: FF ; ????
94A5: FF ; ????
94A6: FF ; ????
94A7: FF ; ????
94A8: FF ; ????
94A9: FF ; ????
94AA: FF ; ????
94AB: FF ; ????
94AC: FF ; ????
94AD: FF ; ????
94AE: FF ; ????
94AF: FF ; ????
94B0: FF ; ????
94B1: FF ; ????
94B2: FF ; ????
94B3: FF ; ????
94B4: FF ; ????
94B5: FF ; ????
94B6: FF ; ????
94B7: FF ; ????
94B8: FF ; ????
94B9: FF ; ????
94BA: FF ; ????
94BB: FF ; ????
94BC: FF ; ????
94BD: FF ; ????
94BE: FF ; ????
94BF: FF ; ????
94C0: FF ; ????
94C1: FF ; ????
94C2: FF ; ????
94C3: FF ; ????
94C4: FF ; ????
94C5: FF ; ????
94C6: FF ; ????
94C7: FF ; ????
94C8: FF ; ????
94C9: FF ; ????
94CA: FF ; ????
94CB: FF ; ????
94CC: FF ; ????
94CD: FF ; ????
94CE: FF ; ????
94CF: FF ; ????
94D0: FF ; ????
94D1: FF ; ????
94D2: FF ; ????
94D3: FF ; ????
94D4: FF ; ????
94D5: FF ; ????
94D6: FF ; ????
94D7: FF ; ????
94D8: FF ; ????
94D9: FF ; ????
94DA: FF ; ????
94DB: FF ; ????
94DC: FF ; ????
94DD: FF ; ????
94DE: FF ; ????
94DF: FF ; ????
94E0: FF ; ????
94E1: FF ; ????
94E2: FF ; ????
94E3: FF ; ????
94E4: FF ; ????
94E5: FF ; ????
94E6: FF ; ????
94E7: FF ; ????
94E8: FF ; ????
94E9: FF ; ????
94EA: FF ; ????
94EB: FF ; ????
94EC: FF ; ????
94ED: FF ; ????
94EE: FF ; ????
94EF: FF ; ????
94F0: FF ; ????
94F1: FF ; ????
94F2: FF ; ????
94F3: FF ; ????
94F4: FF ; ????
94F5: FF ; ????
94F6: FF ; ????
94F7: FF ; ????
94F8: FF ; ????
94F9: FF ; ????
94FA: FF ; ????
94FB: FF ; ????
94FC: FF ; ????
94FD: FF ; ????
94FE: FF ; ????
94FF: FF ; ????
9500: 00              BRK                         
9501: 00              BRK                         
9502: 00              BRK                         
9503: 00              BRK                         
9504: 00              BRK                         
9505: 00              BRK                         
9506: 00              BRK                         
9507: 00              BRK                         
9508: 00              BRK                         
9509: 00              BRK                         
950A: 00              BRK                         
950B: 00              BRK                         
950C: 00              BRK                         
950D: 00              BRK                         
950E: 00              BRK                         
950F: 00              BRK                         
9510: 00              BRK                         
9511: 00              BRK                         
9512: 00              BRK                         
9513: 00              BRK                         
9514: 00              BRK                         
9515: 00              BRK                         
9516: 00              BRK                         
9517: 00              BRK                         
9518: 00              BRK                         
9519: 00              BRK                         
951A: 00              BRK                         
951B: 00              BRK                         
951C: 00              BRK                         
951D: 00              BRK                         
951E: 00              BRK                         
951F: 00              BRK                         
9520: 00              BRK                         
9521: 00              BRK                         
9522: 00              BRK                         
9523: 00              BRK                         
9524: 00              BRK                         
9525: 00              BRK                         
9526: 00              BRK                         
9527: 00              BRK                         
9528: 00              BRK                         
9529: 00              BRK                         
952A: 00              BRK                         
952B: 00              BRK                         
952C: 00              BRK                         
952D: 00              BRK                         
952E: 00              BRK                         
952F: 00              BRK                         
9530: 00              BRK                         
9531: 00              BRK                         
9532: 00              BRK                         
9533: 00              BRK                         
9534: 00              BRK                         
9535: 00              BRK                         
9536: 00              BRK                         
9537: 00              BRK                         
9538: 00              BRK                         
9539: 00              BRK                         
953A: 00              BRK                         
953B: 00              BRK                         
953C: 00              BRK                         
953D: 00              BRK                         
953E: 00              BRK                         
953F: 00              BRK                         
9540: 00              BRK                         
9541: 00              BRK                         
9542: 00              BRK                         
9543: 00              BRK                         
9544: 00              BRK                         
9545: 00              BRK                         
9546: 00              BRK                         
9547: 00              BRK                         
9548: 00              BRK                         
9549: 00              BRK                         
954A: 00              BRK                         
954B: 00              BRK                         
954C: 00              BRK                         
954D: 00              BRK                         
954E: 00              BRK                         
954F: 00              BRK                         
9550: 00              BRK                         
9551: 00              BRK                         
9552: 00              BRK                         
9553: 00              BRK                         
9554: 00              BRK                         
9555: 00              BRK                         
9556: 00              BRK                         
9557: 00              BRK                         
9558: 00              BRK                         
9559: 00              BRK                         
955A: 00              BRK                         
955B: 00              BRK                         
955C: 00              BRK                         
955D: 00              BRK                         
955E: 00              BRK                         
955F: 00              BRK                         
9560: 00              BRK                         
9561: 00              BRK                         
9562: 00              BRK                         
9563: 00              BRK                         
9564: 00              BRK                         
9565: 00              BRK                         
9566: 00              BRK                         
9567: 00              BRK                         
9568: 00              BRK                         
9569: 00              BRK                         
956A: 00              BRK                         
956B: 00              BRK                         
956C: 00              BRK                         
956D: 00              BRK                         
956E: 00              BRK                         
956F: 00              BRK                         
9570: 00              BRK                         
9571: 00              BRK                         
9572: 00              BRK                         
9573: 00              BRK                         
9574: 00              BRK                         
9575: 00              BRK                         
9576: 00              BRK                         
9577: 00              BRK                         
9578: 00              BRK                         
9579: 00              BRK                         
957A: 00              BRK                         
957B: 00              BRK                         
957C: 00              BRK                         
957D: 00              BRK                         
957E: 00              BRK                         
957F: 00              BRK                         
9580: 00              BRK                         
9581: 00              BRK                         
9582: 00              BRK                         
9583: 00              BRK                         
9584: 00              BRK                         
9585: 00              BRK                         
9586: 00              BRK                         
9587: 00              BRK                         
9588: 00              BRK                         
9589: 00              BRK                         
958A: 00              BRK                         
958B: 00              BRK                         
958C: 00              BRK                         
958D: 00              BRK                         
958E: 00              BRK                         
958F: 00              BRK                         
9590: 00              BRK                         
9591: 00              BRK                         
9592: 00              BRK                         
9593: 00              BRK                         
9594: 00              BRK                         
9595: 00              BRK                         
9596: 00              BRK                         
9597: 00              BRK                         
9598: 00              BRK                         
9599: 00              BRK                         
959A: 00              BRK                         
959B: 00              BRK                         
959C: 00              BRK                         
959D: 00              BRK                         
959E: 00              BRK                         
959F: 00              BRK                         
95A0: 00              BRK                         
95A1: 00              BRK                         
95A2: 00              BRK                         
95A3: 00              BRK                         
95A4: 00              BRK                         
95A5: 00              BRK                         
95A6: 00              BRK                         
95A7: 00              BRK                         
95A8: 00              BRK                         
95A9: 00              BRK                         
95AA: 00              BRK                         
95AB: 00              BRK                         
95AC: 00              BRK                         
95AD: 00              BRK                         
95AE: 00              BRK                         
95AF: 00              BRK                         
95B0: 00              BRK                         
95B1: 00              BRK                         
95B2: 00              BRK                         
95B3: 00              BRK                         
95B4: 00              BRK                         
95B5: 00              BRK                         
95B6: 00              BRK                         
95B7: 00              BRK                         
95B8: 00              BRK                         
95B9: 00              BRK                         
95BA: 00              BRK                         
95BB: 00              BRK                         
95BC: 00              BRK                         
95BD: 00              BRK                         
95BE: 00              BRK                         
95BF: 00              BRK                         
95C0: 00              BRK                         
95C1: 00              BRK                         
95C2: 00              BRK                         
95C3: 00              BRK                         
95C4: 00              BRK                         
95C5: 00              BRK                         
95C6: 00              BRK                         
95C7: 00              BRK                         
95C8: 00              BRK                         
95C9: 00              BRK                         
95CA: 00              BRK                         
95CB: 00              BRK                         
95CC: 00              BRK                         
95CD: 00              BRK                         
95CE: 00              BRK                         
95CF: 00              BRK                         
95D0: 00              BRK                         
95D1: 00              BRK                         
95D2: 00              BRK                         
95D3: 00              BRK                         
95D4: 00              BRK                         
95D5: 00              BRK                         
95D6: 00              BRK                         
95D7: 00              BRK                         
95D8: 00              BRK                         
95D9: 00              BRK                         
95DA: 00              BRK                         
95DB: 00              BRK                         
95DC: 00              BRK                         
95DD: 00              BRK                         
95DE: 00              BRK                         
95DF: 00              BRK                         
95E0: 00              BRK                         
95E1: 00              BRK                         
95E2: 00              BRK                         
95E3: 00              BRK                         
95E4: 00              BRK                         
95E5: 00              BRK                         
95E6: 00              BRK                         
95E7: 00              BRK                         
95E8: 00              BRK                         
95E9: 00              BRK                         
95EA: 00              BRK                         
95EB: 00              BRK                         
95EC: 00              BRK                         
95ED: 00              BRK                         
95EE: 00              BRK                         
95EF: 00              BRK                         
95F0: 00              BRK                         
95F1: 00              BRK                         
95F2: 00              BRK                         
95F3: 00              BRK                         
95F4: 00              BRK                         
95F5: 00              BRK                         
95F6: 00              BRK                         
95F7: 00              BRK                         
95F8: 00              BRK                         
95F9: 00              BRK                         
95FA: 00              BRK                         
95FB: 00              BRK                         
95FC: 00              BRK                         
95FD: 00              BRK                         
95FE: 00              BRK                         
95FF: 00              BRK                         
9600: FF ; ????
9601: FF ; ????
9602: FF ; ????
9603: FF ; ????
9604: FF ; ????
9605: FF ; ????
9606: FF ; ????
9607: FF ; ????
9608: FF ; ????
9609: FF ; ????
960A: FF ; ????
960B: FF ; ????
960C: FF ; ????
960D: FF ; ????
960E: FF ; ????
960F: FF ; ????
9610: FF ; ????
9611: FF ; ????
9612: FF ; ????
9613: FF ; ????
9614: FF ; ????
9615: FF ; ????
9616: FF ; ????
9617: FF ; ????
9618: FF ; ????
9619: FF ; ????
961A: FF ; ????
961B: FF ; ????
961C: FF ; ????
961D: FF ; ????
961E: FF ; ????
961F: FF ; ????
9620: FF ; ????
9621: FF ; ????
9622: FF ; ????
9623: FF ; ????
9624: FF ; ????
9625: FF ; ????
9626: FF ; ????
9627: FF ; ????
9628: FF ; ????
9629: FF ; ????
962A: FF ; ????
962B: FF ; ????
962C: FF ; ????
962D: FF ; ????
962E: FF ; ????
962F: FF ; ????
9630: FF ; ????
9631: FF ; ????
9632: FF ; ????
9633: FF ; ????
9634: FF ; ????
9635: FF ; ????
9636: FF ; ????
9637: FF ; ????
9638: FF ; ????
9639: FF ; ????
963A: FF ; ????
963B: FF ; ????
963C: FF ; ????
963D: FF ; ????
963E: FF ; ????
963F: FF ; ????
9640: FF ; ????
9641: FF ; ????
9642: FF ; ????
9643: FF ; ????
9644: FF ; ????
9645: FF ; ????
9646: FF ; ????
9647: FF ; ????
9648: FF ; ????
9649: FF ; ????
964A: FF ; ????
964B: FF ; ????
964C: FF ; ????
964D: FF ; ????
964E: FF ; ????
964F: FF ; ????
9650: FF ; ????
9651: FF ; ????
9652: FF ; ????
9653: FF ; ????
9654: FF ; ????
9655: FF ; ????
9656: FF ; ????
9657: FF ; ????
9658: FF ; ????
9659: FF ; ????
965A: FF ; ????
965B: FF ; ????
965C: FF ; ????
965D: FF ; ????
965E: FF ; ????
965F: FF ; ????
9660: FF ; ????
9661: FF ; ????
9662: FF ; ????
9663: FF ; ????
9664: FF ; ????
9665: FF ; ????
9666: FF ; ????
9667: FF ; ????
9668: FF ; ????
9669: FF ; ????
966A: FF ; ????
966B: FF ; ????
966C: FF ; ????
966D: FF ; ????
966E: FF ; ????
966F: FF ; ????
9670: FF ; ????
9671: FF ; ????
9672: FF ; ????
9673: FF ; ????
9674: FF ; ????
9675: FF ; ????
9676: FF ; ????
9677: FF ; ????
9678: FF ; ????
9679: FF ; ????
967A: FF ; ????
967B: FF ; ????
967C: FF ; ????
967D: FF ; ????
967E: FF ; ????
967F: FF ; ????
9680: FF ; ????
9681: FF ; ????
9682: FF ; ????
9683: FF ; ????
9684: FF ; ????
9685: FF ; ????
9686: FF ; ????
9687: FF ; ????
9688: FF ; ????
9689: FF ; ????
968A: FF ; ????
968B: FF ; ????
968C: FF ; ????
968D: FF ; ????
968E: FF ; ????
968F: FF ; ????
9690: FF ; ????
9691: FF ; ????
9692: FF ; ????
9693: FF ; ????
9694: FF ; ????
9695: FF ; ????
9696: FF ; ????
9697: FF ; ????
9698: FF ; ????
9699: FF ; ????
969A: FF ; ????
969B: FF ; ????
969C: FF ; ????
969D: FF ; ????
969E: FF ; ????
969F: FF ; ????
96A0: FF ; ????
96A1: FF ; ????
96A2: FF ; ????
96A3: FF ; ????
96A4: FF ; ????
96A5: FF ; ????
96A6: FF ; ????
96A7: FF ; ????
96A8: FF ; ????
96A9: FF ; ????
96AA: FF ; ????
96AB: FF ; ????
96AC: FF ; ????
96AD: FF ; ????
96AE: FF ; ????
96AF: FF ; ????
96B0: FF ; ????
96B1: FF ; ????
96B2: FF ; ????
96B3: FF ; ????
96B4: FF ; ????
96B5: FF ; ????
96B6: FF ; ????
96B7: FF ; ????
96B8: FF ; ????
96B9: FF ; ????
96BA: FF ; ????
96BB: FF ; ????
96BC: FF ; ????
96BD: FF ; ????
96BE: FF ; ????
96BF: FF ; ????
96C0: FF ; ????
96C1: FF ; ????
96C2: FF ; ????
96C3: FF ; ????
96C4: FF ; ????
96C5: FF ; ????
96C6: FF ; ????
96C7: FF ; ????
96C8: FF ; ????
96C9: FF ; ????
96CA: FF ; ????
96CB: FF ; ????
96CC: FF ; ????
96CD: FF ; ????
96CE: FF ; ????
96CF: FF ; ????
96D0: FF ; ????
96D1: FF ; ????
96D2: FF ; ????
96D3: FF ; ????
96D4: FF ; ????
96D5: FF ; ????
96D6: FF ; ????
96D7: FF ; ????
96D8: FF ; ????
96D9: FF ; ????
96DA: FF ; ????
96DB: FF ; ????
96DC: FF ; ????
96DD: FF ; ????
96DE: FF ; ????
96DF: FF ; ????
96E0: FF ; ????
96E1: FF ; ????
96E2: FF ; ????
96E3: FF ; ????
96E4: FF ; ????
96E5: FF ; ????
96E6: FF ; ????
96E7: FF ; ????
96E8: FF ; ????
96E9: FF ; ????
96EA: FF ; ????
96EB: FF ; ????
96EC: FF ; ????
96ED: FF ; ????
96EE: FF ; ????
96EF: FF ; ????
96F0: FF ; ????
96F1: FF ; ????
96F2: FF ; ????
96F3: FF ; ????
96F4: FF ; ????
96F5: FF ; ????
96F6: FF ; ????
96F7: FF ; ????
96F8: FF ; ????
96F9: FF ; ????
96FA: FF ; ????
96FB: FF ; ????
96FC: FF ; ????
96FD: FF ; ????
96FE: FF ; ????
96FF: FF ; ????
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
9800: FF ; ????
9801: FF ; ????
9802: FF ; ????
9803: FF ; ????
9804: FF ; ????
9805: FF ; ????
9806: FF ; ????
9807: FF ; ????
9808: FF ; ????
9809: FF ; ????
980A: FF ; ????
980B: FF ; ????
980C: FF ; ????
980D: FF ; ????
980E: FF ; ????
980F: FF ; ????
9810: FF ; ????
9811: FF ; ????
9812: FF ; ????
9813: FF ; ????
9814: FF ; ????
9815: FF ; ????
9816: FF ; ????
9817: FF ; ????
9818: FF ; ????
9819: FF ; ????
981A: FF ; ????
981B: FF ; ????
981C: FF ; ????
981D: FF ; ????
981E: FF ; ????
981F: FF ; ????
9820: FF ; ????
9821: FF ; ????
9822: FF ; ????
9823: FF ; ????
9824: FF ; ????
9825: FF ; ????
9826: FF ; ????
9827: FF ; ????
9828: FF ; ????
9829: FF ; ????
982A: FF ; ????
982B: FF ; ????
982C: FF ; ????
982D: FF ; ????
982E: FF ; ????
982F: FF ; ????
9830: FF ; ????
9831: FF ; ????
9832: FF ; ????
9833: FF ; ????
9834: FF ; ????
9835: FF ; ????
9836: FF ; ????
9837: FF ; ????
9838: FF ; ????
9839: FF ; ????
983A: FF ; ????
983B: FF ; ????
983C: FF ; ????
983D: FF ; ????
983E: FF ; ????
983F: FF ; ????
9840: FF ; ????
9841: FF ; ????
9842: FF ; ????
9843: FF ; ????
9844: FF ; ????
9845: FF ; ????
9846: FF ; ????
9847: FF ; ????
9848: FF ; ????
9849: FF ; ????
984A: FF ; ????
984B: FF ; ????
984C: FF ; ????
984D: FF ; ????
984E: FF ; ????
984F: FF ; ????
9850: FF ; ????
9851: FF ; ????
9852: FF ; ????
9853: FF ; ????
9854: FF ; ????
9855: FF ; ????
9856: FF ; ????
9857: FF ; ????
9858: FF ; ????
9859: FF ; ????
985A: FF ; ????
985B: FF ; ????
985C: FF ; ????
985D: FF ; ????
985E: FF ; ????
985F: FF ; ????
9860: FF ; ????
9861: FF ; ????
9862: FF ; ????
9863: FF ; ????
9864: FF ; ????
9865: FF ; ????
9866: FF ; ????
9867: FF ; ????
9868: FF ; ????
9869: FF ; ????
986A: FF ; ????
986B: FF ; ????
986C: FF ; ????
986D: FF ; ????
986E: FF ; ????
986F: FF ; ????
9870: FF ; ????
9871: FF ; ????
9872: FF ; ????
9873: FF ; ????
9874: FF ; ????
9875: FF ; ????
9876: FF ; ????
9877: FF ; ????
9878: FF ; ????
9879: FF ; ????
987A: FF ; ????
987B: FF ; ????
987C: FF ; ????
987D: FF ; ????
987E: FF ; ????
987F: FF ; ????
9880: FF ; ????
9881: FF ; ????
9882: FF ; ????
9883: FF ; ????
9884: FF ; ????
9885: FF ; ????
9886: FF ; ????
9887: FF ; ????
9888: FF ; ????
9889: FF ; ????
988A: FF ; ????
988B: FF ; ????
988C: FF ; ????
988D: FF ; ????
988E: FF ; ????
988F: FF ; ????
9890: FF ; ????
9891: FF ; ????
9892: FF ; ????
9893: FF ; ????
9894: FF ; ????
9895: FF ; ????
9896: 7F ; ????
9897: FF ; ????
9898: FF ; ????
9899: FF ; ????
989A: FF ; ????
989B: FF ; ????
989C: FF ; ????
989D: FF ; ????
989E: FF ; ????
989F: FF ; ????
98A0: FF ; ????
98A1: FF ; ????
98A2: FF ; ????
98A3: FF ; ????
98A4: FF ; ????
98A5: FF ; ????
98A6: FF ; ????
98A7: FF ; ????
98A8: FF ; ????
98A9: FF ; ????
98AA: FF ; ????
98AB: FF ; ????
98AC: FF ; ????
98AD: FF ; ????
98AE: FF ; ????
98AF: FF ; ????
98B0: FF ; ????
98B1: FF ; ????
98B2: FF ; ????
98B3: FF ; ????
98B4: FF ; ????
98B5: FF ; ????
98B6: FF ; ????
98B7: FF ; ????
98B8: FF ; ????
98B9: FF ; ????
98BA: FF ; ????
98BB: FF ; ????
98BC: FF ; ????
98BD: FF ; ????
98BE: FF ; ????
98BF: FF ; ????
98C0: FF ; ????
98C1: FF ; ????
98C2: FF ; ????
98C3: FF ; ????
98C4: FF ; ????
98C5: FF ; ????
98C6: FF ; ????
98C7: FF ; ????
98C8: FF ; ????
98C9: FF ; ????
98CA: FF ; ????
98CB: FF ; ????
98CC: FF ; ????
98CD: FF ; ????
98CE: FF ; ????
98CF: EF ; ????
98D0: FF ; ????
98D1: FF ; ????
98D2: FF ; ????
98D3: FF ; ????
98D4: FF ; ????
98D5: FF ; ????
98D6: FF ; ????
98D7: FF ; ????
98D8: FF ; ????
98D9: FF ; ????
98DA: FF ; ????
98DB: FF ; ????
98DC: FF ; ????
98DD: FF ; ????
98DE: FF ; ????
98DF: FF ; ????
98E0: FF ; ????
98E1: FF ; ????
98E2: FF ; ????
98E3: FF ; ????
98E4: FF ; ????
98E5: FF ; ????
98E6: FF ; ????
98E7: FF ; ????
98E8: FF ; ????
98E9: FF ; ????
98EA: FF ; ????
98EB: FF ; ????
98EC: FF ; ????
98ED: FF ; ????
98EE: FF ; ????
98EF: FF ; ????
98F0: FF ; ????
98F1: FF ; ????
98F2: FF ; ????
98F3: FF ; ????
98F4: FF ; ????
98F5: FF ; ????
98F6: FF ; ????
98F7: FF ; ????
98F8: FF ; ????
98F9: FF ; ????
98FA: FF ; ????
98FB: FF ; ????
98FC: FF ; ????
98FD: FF ; ????
98FE: FF ; ????
98FF: FF ; ????
9900: 00              BRK                         
9901: 00              BRK                         
9902: 00              BRK                         
9903: 00              BRK                         
9904: 00              BRK                         
9905: 00              BRK                         
9906: 00              BRK                         
9907: 00              BRK                         
9908: 00              BRK                         
9909: 00              BRK                         
990A: 00              BRK                         
990B: 00              BRK                         
990C: 00              BRK                         
990D: 00              BRK                         
990E: 00              BRK                         
990F: 00              BRK                         
9910: 00              BRK                         
9911: 00              BRK                         
9912: 00              BRK                         
9913: 00              BRK                         
9914: 00              BRK                         
9915: 00              BRK                         
9916: 00              BRK                         
9917: 00              BRK                         
9918: 00              BRK                         
9919: 00              BRK                         
991A: 00              BRK                         
991B: 00              BRK                         
991C: 00              BRK                         
991D: 00              BRK                         
991E: 00              BRK                         
991F: 00              BRK                         
9920: 00              BRK                         
9921: 00              BRK                         
9922: 00              BRK                         
9923: 00              BRK                         
9924: 00              BRK                         
9925: 00              BRK                         
9926: 00              BRK                         
9927: 00              BRK                         
9928: 00              BRK                         
9929: 00              BRK                         
992A: 00              BRK                         
992B: 00              BRK                         
992C: 00              BRK                         
992D: 00              BRK                         
992E: 00              BRK                         
992F: 00              BRK                         
9930: 00              BRK                         
9931: 00              BRK                         
9932: 00              BRK                         
9933: 00              BRK                         
9934: 00              BRK                         
9935: 00              BRK                         
9936: 00              BRK                         
9937: 00              BRK                         
9938: 00              BRK                         
9939: 00              BRK                         
993A: 00              BRK                         
993B: 00              BRK                         
993C: 00              BRK                         
993D: 00              BRK                         
993E: 00              BRK                         
993F: 00              BRK                         
9940: 00              BRK                         
9941: 00              BRK                         
9942: 00              BRK                         
9943: 00              BRK                         
9944: 00              BRK                         
9945: 00              BRK                         
9946: 00              BRK                         
9947: 00              BRK                         
9948: 00              BRK                         
9949: 00              BRK                         
994A: 00              BRK                         
994B: 00              BRK                         
994C: 00              BRK                         
994D: 00              BRK                         
994E: 00              BRK                         
994F: 00              BRK                         
9950: 00              BRK                         
9951: 00              BRK                         
9952: 00              BRK                         
9953: 00              BRK                         
9954: 00              BRK                         
9955: 00              BRK                         
9956: 00              BRK                         
9957: 00              BRK                         
9958: 00              BRK                         
9959: 00              BRK                         
995A: 00              BRK                         
995B: 00              BRK                         
995C: 00              BRK                         
995D: 00              BRK                         
995E: 00              BRK                         
995F: 00              BRK                         
9960: 00              BRK                         
9961: 00              BRK                         
9962: 00              BRK                         
9963: 00              BRK                         
9964: 00              BRK                         
9965: 00              BRK                         
9966: 00              BRK                         
9967: 00              BRK                         
9968: 00              BRK                         
9969: 00              BRK                         
996A: 00              BRK                         
996B: 00              BRK                         
996C: 00              BRK                         
996D: 00              BRK                         
996E: 00              BRK                         
996F: 00              BRK                         
9970: 00              BRK                         
9971: 00              BRK                         
9972: 00              BRK                         
9973: 00              BRK                         
9974: 00              BRK                         
9975: 00              BRK                         
9976: 00              BRK                         
9977: 00              BRK                         
9978: 00              BRK                         
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
99A0: 00              BRK                         
99A1: 00              BRK                         
99A2: 00              BRK                         
99A3: 00              BRK                         
99A4: 00              BRK                         
99A5: 00              BRK                         
99A6: 00              BRK                         
99A7: 00              BRK                         
99A8: 00              BRK                         
99A9: 00              BRK                         
99AA: 00              BRK                         
99AB: 00              BRK                         
99AC: 00              BRK                         
99AD: 00              BRK                         
99AE: 00              BRK                         
99AF: 00              BRK                         
99B0: 00              BRK                         
99B1: 00              BRK                         
99B2: 00              BRK                         
99B3: 00              BRK                         
99B4: 00              BRK                         
99B5: 00              BRK                         
99B6: 00              BRK                         
99B7: 00              BRK                         
99B8: 00              BRK                         
99B9: 00              BRK                         
99BA: 00              BRK                         
99BB: 00              BRK                         
99BC: 00              BRK                         
99BD: 00              BRK                         
99BE: 00              BRK                         
99BF: 00              BRK                         
99C0: 00              BRK                         
99C1: 00              BRK                         
99C2: 00              BRK                         
99C3: 00              BRK                         
99C4: 00              BRK                         
99C5: 00              BRK                         
99C6: 00              BRK                         
99C7: 00              BRK                         
99C8: 00              BRK                         
99C9: 00              BRK                         
99CA: 00              BRK                         
99CB: 00              BRK                         
99CC: 00              BRK                         
99CD: 00              BRK                         
99CE: 00              BRK                         
99CF: 00              BRK                         
99D0: 00              BRK                         
99D1: 00              BRK                         
99D2: 00              BRK                         
99D3: 00              BRK                         
99D4: 00              BRK                         
99D5: 00              BRK                         
99D6: 00              BRK                         
99D7: 00              BRK                         
99D8: 00              BRK                         
99D9: 00              BRK                         
99DA: 00              BRK                         
99DB: 00              BRK                         
99DC: 00              BRK                         
99DD: 00              BRK                         
99DE: 00              BRK                         
99DF: 00              BRK                         
99E0: 00              BRK                         
99E1: 00              BRK                         
99E2: 00              BRK                         
99E3: 00              BRK                         
99E4: 00              BRK                         
99E5: 00              BRK                         
99E6: 00              BRK                         
99E7: 00              BRK                         
99E8: 00              BRK                         
99E9: 00              BRK                         
99EA: 00              BRK                         
99EB: 00              BRK                         
99EC: 00              BRK                         
99ED: 00              BRK                         
99EE: 00              BRK                         
99EF: 00              BRK                         
99F0: 00              BRK                         
99F1: 00              BRK                         
99F2: 00              BRK                         
99F3: 00              BRK                         
99F4: 00              BRK                         
99F5: 00              BRK                         
99F6: 00              BRK                         
99F7: 00              BRK                         
99F8: 00              BRK                         
99F9: 00              BRK                         
99FA: 00              BRK                         
99FB: 00              BRK                         
99FC: 00              BRK                         
99FD: 00              BRK                         
99FE: 00              BRK                         
99FF: 00              BRK                         
9A00: FF ; ????
9A01: FF ; ????
9A02: FF ; ????
9A03: FF ; ????
9A04: FF ; ????
9A05: FF ; ????
9A06: FF ; ????
9A07: FF ; ????
9A08: FF ; ????
9A09: FF ; ????
9A0A: FF ; ????
9A0B: FF ; ????
9A0C: FF ; ????
9A0D: FF ; ????
9A0E: FF ; ????
9A0F: FF ; ????
9A10: FF ; ????
9A11: FF ; ????
9A12: FF ; ????
9A13: FF ; ????
9A14: FF ; ????
9A15: FF ; ????
9A16: FF ; ????
9A17: FF ; ????
9A18: FF ; ????
9A19: FF ; ????
9A1A: FF ; ????
9A1B: FF ; ????
9A1C: FF ; ????
9A1D: FF ; ????
9A1E: FF ; ????
9A1F: FF ; ????
9A20: FF ; ????
9A21: FF ; ????
9A22: FF ; ????
9A23: FF ; ????
9A24: FF ; ????
9A25: FF ; ????
9A26: FF ; ????
9A27: FF ; ????
9A28: FF ; ????
9A29: FF ; ????
9A2A: FF ; ????
9A2B: FF ; ????
9A2C: FF ; ????
9A2D: FF ; ????
9A2E: FF ; ????
9A2F: FF ; ????
9A30: FF ; ????
9A31: FF ; ????
9A32: FF ; ????
9A33: FF ; ????
9A34: FF ; ????
9A35: FF ; ????
9A36: FF ; ????
9A37: FF ; ????
9A38: FF ; ????
9A39: FF ; ????
9A3A: FF ; ????
9A3B: FF ; ????
9A3C: FF ; ????
9A3D: FF ; ????
9A3E: FF ; ????
9A3F: FF ; ????
9A40: FF ; ????
9A41: FF ; ????
9A42: FF ; ????
9A43: FF ; ????
9A44: FF ; ????
9A45: FF ; ????
9A46: FF ; ????
9A47: FF ; ????
9A48: FF ; ????
9A49: FF ; ????
9A4A: FF ; ????
9A4B: FF ; ????
9A4C: FF ; ????
9A4D: FF ; ????
9A4E: FF ; ????
9A4F: FF ; ????
9A50: FF ; ????
9A51: FF ; ????
9A52: FF ; ????
9A53: FF ; ????
9A54: FF ; ????
9A55: FF ; ????
9A56: FF ; ????
9A57: FF ; ????
9A58: FF ; ????
9A59: FF ; ????
9A5A: FF ; ????
9A5B: FF ; ????
9A5C: FF ; ????
9A5D: FF ; ????
9A5E: FF ; ????
9A5F: FF ; ????
9A60: FF ; ????
9A61: FF ; ????
9A62: FF ; ????
9A63: FF ; ????
9A64: FF ; ????
9A65: FF ; ????
9A66: FF ; ????
9A67: FF ; ????
9A68: FF ; ????
9A69: FF ; ????
9A6A: FF ; ????
9A6B: FF ; ????
9A6C: FF ; ????
9A6D: FF ; ????
9A6E: FF ; ????
9A6F: FF ; ????
9A70: FF ; ????
9A71: FF ; ????
9A72: FF ; ????
9A73: FF ; ????
9A74: FF ; ????
9A75: FF ; ????
9A76: FF ; ????
9A77: FF ; ????
9A78: FF ; ????
9A79: FF ; ????
9A7A: FF ; ????
9A7B: FF ; ????
9A7C: FF ; ????
9A7D: FF ; ????
9A7E: FF ; ????
9A7F: FF ; ????
9A80: FF ; ????
9A81: FF ; ????
9A82: FF ; ????
9A83: FF ; ????
9A84: FF ; ????
9A85: FF ; ????
9A86: FF ; ????
9A87: FF ; ????
9A88: FF ; ????
9A89: FF ; ????
9A8A: FF ; ????
9A8B: FF ; ????
9A8C: FF ; ????
9A8D: FF ; ????
9A8E: FF ; ????
9A8F: FF ; ????
9A90: FF ; ????
9A91: FF ; ????
9A92: FF ; ????
9A93: FF ; ????
9A94: FF ; ????
9A95: FF ; ????
9A96: FF ; ????
9A97: FF ; ????
9A98: FF ; ????
9A99: FF ; ????
9A9A: FF ; ????
9A9B: FF ; ????
9A9C: FF ; ????
9A9D: FF ; ????
9A9E: FF ; ????
9A9F: FF ; ????
9AA0: FF ; ????
9AA1: FF ; ????
9AA2: FF ; ????
9AA3: FF ; ????
9AA4: FF ; ????
9AA5: FF ; ????
9AA6: FF ; ????
9AA7: FF ; ????
9AA8: FF ; ????
9AA9: FF ; ????
9AAA: FF ; ????
9AAB: FF ; ????
9AAC: FF ; ????
9AAD: FF ; ????
9AAE: FF ; ????
9AAF: FF ; ????
9AB0: FF ; ????
9AB1: FF ; ????
9AB2: FF ; ????
9AB3: FF ; ????
9AB4: FF ; ????
9AB5: FF ; ????
9AB6: FF ; ????
9AB7: FF ; ????
9AB8: FF ; ????
9AB9: FF ; ????
9ABA: FF ; ????
9ABB: FF ; ????
9ABC: FF ; ????
9ABD: FF ; ????
9ABE: FF ; ????
9ABF: FF ; ????
9AC0: FF ; ????
9AC1: FF ; ????
9AC2: FF ; ????
9AC3: FF ; ????
9AC4: FF ; ????
9AC5: FF ; ????
9AC6: FF ; ????
9AC7: FF ; ????
9AC8: FF ; ????
9AC9: FF ; ????
9ACA: FF ; ????
9ACB: FF ; ????
9ACC: FF ; ????
9ACD: FF ; ????
9ACE: FF ; ????
9ACF: FF ; ????
9AD0: FF ; ????
9AD1: FF ; ????
9AD2: FF ; ????
9AD3: FF ; ????
9AD4: FF ; ????
9AD5: FF ; ????
9AD6: FF ; ????
9AD7: FF ; ????
9AD8: FF ; ????
9AD9: FF ; ????
9ADA: FF ; ????
9ADB: FF ; ????
9ADC: FF ; ????
9ADD: FF ; ????
9ADE: FF ; ????
9ADF: FF ; ????
9AE0: FF ; ????
9AE1: FF ; ????
9AE2: FF ; ????
9AE3: FF ; ????
9AE4: FF ; ????
9AE5: FF ; ????
9AE6: FF ; ????
9AE7: FF ; ????
9AE8: FF ; ????
9AE9: FF ; ????
9AEA: FF ; ????
9AEB: FF ; ????
9AEC: FF ; ????
9AED: FF ; ????
9AEE: FF ; ????
9AEF: FF ; ????
9AF0: FF ; ????
9AF1: FF ; ????
9AF2: FF ; ????
9AF3: FF ; ????
9AF4: FF ; ????
9AF5: FF ; ????
9AF6: FF ; ????
9AF7: FF ; ????
9AF8: FF ; ????
9AF9: FF ; ????
9AFA: FF ; ????
9AFB: FF ; ????
9AFC: FF ; ????
9AFD: FF ; ????
9AFE: FF ; ????
9AFF: FF ; ????
9B00: 00              BRK                         
9B01: 00              BRK                         
9B02: 00              BRK                         
9B03: 00              BRK                         
9B04: 00              BRK                         
9B05: 00              BRK                         
9B06: 00              BRK                         
9B07: 00              BRK                         
9B08: 00              BRK                         
9B09: 00              BRK                         
9B0A: 00              BRK                         
9B0B: 00              BRK                         
9B0C: 00              BRK                         
9B0D: 00              BRK                         
9B0E: 00              BRK                         
9B0F: 00              BRK                         
9B10: 00              BRK                         
9B11: 00              BRK                         
9B12: 00              BRK                         
9B13: 00              BRK                         
9B14: 00              BRK                         
9B15: 00              BRK                         
9B16: 00              BRK                         
9B17: 00              BRK                         
9B18: 00              BRK                         
9B19: 00              BRK                         
9B1A: 00              BRK                         
9B1B: 00              BRK                         
9B1C: 00              BRK                         
9B1D: 00              BRK                         
9B1E: 00              BRK                         
9B1F: 00              BRK                         
9B20: 00              BRK                         
9B21: 00              BRK                         
9B22: 00              BRK                         
9B23: 00              BRK                         
9B24: 00              BRK                         
9B25: 00              BRK                         
9B26: 00              BRK                         
9B27: 00              BRK                         
9B28: 00              BRK                         
9B29: 00              BRK                         
9B2A: 00              BRK                         
9B2B: 00              BRK                         
9B2C: 00              BRK                         
9B2D: 00              BRK                         
9B2E: 00              BRK                         
9B2F: 00              BRK                         
9B30: 00              BRK                         
9B31: 00              BRK                         
9B32: 00              BRK                         
9B33: 00              BRK                         
9B34: 00              BRK                         
9B35: 00              BRK                         
9B36: 00              BRK                         
9B37: 00              BRK                         
9B38: 00              BRK                         
9B39: 00              BRK                         
9B3A: 00              BRK                         
9B3B: 00              BRK                         
9B3C: 00              BRK                         
9B3D: 00              BRK                         
9B3E: 00              BRK                         
9B3F: 00              BRK                         
9B40: 00              BRK                         
9B41: 00              BRK                         
9B42: 00              BRK                         
9B43: 00              BRK                         
9B44: 00              BRK                         
9B45: 00              BRK                         
9B46: 00              BRK                         
9B47: 00              BRK                         
9B48: 00              BRK                         
9B49: 00              BRK                         
9B4A: 00              BRK                         
9B4B: 00              BRK                         
9B4C: 00              BRK                         
9B4D: 00              BRK                         
9B4E: 00              BRK                         
9B4F: 00              BRK                         
9B50: 00              BRK                         
9B51: 00              BRK                         
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
9BF8: 04 ; ????
9BF9: 02 ; ????
9BFA: 00              BRK                         
9BFB: 89 ; ????
9BFC: 00              BRK                         
9BFD: 10 00           BPL     $9BFF               ; {}
9BFF: 80 ; ????
9C00: FF ; ????
9C01: FF ; ????
9C02: FF ; ????
9C03: FF ; ????
9C04: FF ; ????
9C05: FF ; ????
9C06: FF ; ????
9C07: FF ; ????
9C08: FF ; ????
9C09: FF ; ????
9C0A: FF ; ????
9C0B: FF ; ????
9C0C: FF ; ????
9C0D: FF ; ????
9C0E: FF ; ????
9C0F: FF ; ????
9C10: FF ; ????
9C11: FF ; ????
9C12: FF ; ????
9C13: FF ; ????
9C14: FF ; ????
9C15: FF ; ????
9C16: FF ; ????
9C17: FF ; ????
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
9C2F: FF ; ????
9C30: FF ; ????
9C31: FF ; ????
9C32: FF ; ????
9C33: FF ; ????
9C34: FF ; ????
9C35: FF ; ????
9C36: FF ; ????
9C37: FF ; ????
9C38: FF ; ????
9C39: FF ; ????
9C3A: FF ; ????
9C3B: FF ; ????
9C3C: FF ; ????
9C3D: FF ; ????
9C3E: FF ; ????
9C3F: FF ; ????
9C40: FF ; ????
9C41: FF ; ????
9C42: FF ; ????
9C43: FF ; ????
9C44: FF ; ????
9C45: FF ; ????
9C46: DF ; ????
9C47: FF ; ????
9C48: FF ; ????
9C49: FF ; ????
9C4A: FF ; ????
9C4B: FF ; ????
9C4C: FF ; ????
9C4D: FF ; ????
9C4E: FF ; ????
9C4F: FF ; ????
9C50: FF ; ????
9C51: FF ; ????
9C52: FF ; ????
9C53: FF ; ????
9C54: FF ; ????
9C55: FF ; ????
9C56: FF ; ????
9C57: FF ; ????
9C58: FF ; ????
9C59: FF ; ????
9C5A: FF ; ????
9C5B: FF ; ????
9C5C: FF ; ????
9C5D: FF ; ????
9C5E: FF ; ????
9C5F: FF ; ????
9C60: FF ; ????
9C61: FF ; ????
9C62: FF ; ????
9C63: FF ; ????
9C64: FF ; ????
9C65: FF ; ????
9C66: FF ; ????
9C67: FF ; ????
9C68: FF ; ????
9C69: FF ; ????
9C6A: FF ; ????
9C6B: FF ; ????
9C6C: FF ; ????
9C6D: FF ; ????
9C6E: FF ; ????
9C6F: FF ; ????
9C70: FF ; ????
9C71: FF ; ????
9C72: FF ; ????
9C73: FF ; ????
9C74: FF ; ????
9C75: FF ; ????
9C76: FF ; ????
9C77: FF ; ????
9C78: FF ; ????
9C79: FF ; ????
9C7A: FF ; ????
9C7B: FF ; ????
9C7C: FF ; ????
9C7D: FF ; ????
9C7E: FF ; ????
9C7F: FF ; ????
9C80: FF ; ????
9C81: FF ; ????
9C82: FF ; ????
9C83: FF ; ????
9C84: FF ; ????
9C85: FF ; ????
9C86: FF ; ????
9C87: FF ; ????
9C88: FF ; ????
9C89: FF ; ????
9C8A: FF ; ????
9C8B: FF ; ????
9C8C: FF ; ????
9C8D: FF ; ????
9C8E: FF ; ????
9C8F: FF ; ????
9C90: FF ; ????
9C91: FF ; ????
9C92: FF ; ????
9C93: FF ; ????
9C94: FF ; ????
9C95: FF ; ????
9C96: FF ; ????
9C97: FF ; ????
9C98: FF ; ????
9C99: FF ; ????
9C9A: FF ; ????
9C9B: FF ; ????
9C9C: FF ; ????
9C9D: FF ; ????
9C9E: FF ; ????
9C9F: FF ; ????
9CA0: FF ; ????
9CA1: FF ; ????
9CA2: FF ; ????
9CA3: FF ; ????
9CA4: FF ; ????
9CA5: FF ; ????
9CA6: FF ; ????
9CA7: FF ; ????
9CA8: FF ; ????
9CA9: FF ; ????
9CAA: FF ; ????
9CAB: FF ; ????
9CAC: FF ; ????
9CAD: FF ; ????
9CAE: FF ; ????
9CAF: FF ; ????
9CB0: FF ; ????
9CB1: FF ; ????
9CB2: FF ; ????
9CB3: FF ; ????
9CB4: FF ; ????
9CB5: FF ; ????
9CB6: FF ; ????
9CB7: FF ; ????
9CB8: FF ; ????
9CB9: FF ; ????
9CBA: FF ; ????
9CBB: FF ; ????
9CBC: FF ; ????
9CBD: FF ; ????
9CBE: FF ; ????
9CBF: FF ; ????
9CC0: FF ; ????
9CC1: FF ; ????
9CC2: FF ; ????
9CC3: FF ; ????
9CC4: FF ; ????
9CC5: FF ; ????
9CC6: FF ; ????
9CC7: FF ; ????
9CC8: FF ; ????
9CC9: FF ; ????
9CCA: FF ; ????
9CCB: FF ; ????
9CCC: FF ; ????
9CCD: FF ; ????
9CCE: FF ; ????
9CCF: FF ; ????
9CD0: FF ; ????
9CD1: FF ; ????
9CD2: FF ; ????
9CD3: FF ; ????
9CD4: FF ; ????
9CD5: FF ; ????
9CD6: FF ; ????
9CD7: FF ; ????
9CD8: FF ; ????
9CD9: FF ; ????
9CDA: FF ; ????
9CDB: FF ; ????
9CDC: FF ; ????
9CDD: FF ; ????
9CDE: FF ; ????
9CDF: FF ; ????
9CE0: FF ; ????
9CE1: FF ; ????
9CE2: FF ; ????
9CE3: FF ; ????
9CE4: FF ; ????
9CE5: FF ; ????
9CE6: FF ; ????
9CE7: FF ; ????
9CE8: FF ; ????
9CE9: FF ; ????
9CEA: FF ; ????
9CEB: FF ; ????
9CEC: FF ; ????
9CED: FF ; ????
9CEE: FF ; ????
9CEF: FF ; ????
9CF0: FF ; ????
9CF1: FF ; ????
9CF2: FF ; ????
9CF3: FF ; ????
9CF4: FF ; ????
9CF5: FF ; ????
9CF6: FF ; ????
9CF7: FF ; ????
9CF8: FF ; ????
9CF9: FF ; ????
9CFA: FF ; ????
9CFB: FF ; ????
9CFC: FF ; ????
9CFD: FF ; ????
9CFE: FF ; ????
9CFF: FF ; ????
9D00: 00              BRK                         
9D01: 00              BRK                         
9D02: 00              BRK                         
9D03: 00              BRK                         
9D04: 00              BRK                         
9D05: 00              BRK                         
9D06: 00              BRK                         
9D07: 00              BRK                         
9D08: 00              BRK                         
9D09: 00              BRK                         
9D0A: 00              BRK                         
9D0B: 00              BRK                         
9D0C: 00              BRK                         
9D0D: 00              BRK                         
9D0E: 00              BRK                         
9D0F: 00              BRK                         
9D10: 00              BRK                         
9D11: 00              BRK                         
9D12: 00              BRK                         
9D13: 00              BRK                         
9D14: 00              BRK                         
9D15: 00              BRK                         
9D16: 00              BRK                         
9D17: 00              BRK                         
9D18: 00              BRK                         
9D19: 00              BRK                         
9D1A: 00              BRK                         
9D1B: 00              BRK                         
9D1C: 00              BRK                         
9D1D: 00              BRK                         
9D1E: 00              BRK                         
9D1F: 00              BRK                         
9D20: 00              BRK                         
9D21: 00              BRK                         
9D22: 00              BRK                         
9D23: 00              BRK                         
9D24: 00              BRK                         
9D25: 00              BRK                         
9D26: 00              BRK                         
9D27: 00              BRK                         
9D28: 00              BRK                         
9D29: 00              BRK                         
9D2A: 00              BRK                         
9D2B: 00              BRK                         
9D2C: 00              BRK                         
9D2D: 00              BRK                         
9D2E: 00              BRK                         
9D2F: 00              BRK                         
9D30: 00              BRK                         
9D31: 00              BRK                         
9D32: 00              BRK                         
9D33: 00              BRK                         
9D34: 00              BRK                         
9D35: 00              BRK                         
9D36: 00              BRK                         
9D37: 00              BRK                         
9D38: 00              BRK                         
9D39: 00              BRK                         
9D3A: 00              BRK                         
9D3B: 00              BRK                         
9D3C: 00              BRK                         
9D3D: 00              BRK                         
9D3E: 00              BRK                         
9D3F: 00              BRK                         
9D40: 00              BRK                         
9D41: 00              BRK                         
9D42: 00              BRK                         
9D43: 00              BRK                         
9D44: 00              BRK                         
9D45: 00              BRK                         
9D46: 00              BRK                         
9D47: 00              BRK                         
9D48: 00              BRK                         
9D49: 00              BRK                         
9D4A: 00              BRK                         
9D4B: 00              BRK                         
9D4C: 00              BRK                         
9D4D: 00              BRK                         
9D4E: 00              BRK                         
9D4F: 00              BRK                         
9D50: 00              BRK                         
9D51: 00              BRK                         
9D52: 00              BRK                         
9D53: 00              BRK                         
9D54: 00              BRK                         
9D55: 00              BRK                         
9D56: 00              BRK                         
9D57: 00              BRK                         
9D58: 00              BRK                         
9D59: 00              BRK                         
9D5A: 00              BRK                         
9D5B: 00              BRK                         
9D5C: 00              BRK                         
9D5D: 00              BRK                         
9D5E: 00              BRK                         
9D5F: 00              BRK                         
9D60: 00              BRK                         
9D61: 00              BRK                         
9D62: 00              BRK                         
9D63: 00              BRK                         
9D64: 00              BRK                         
9D65: 00              BRK                         
9D66: 00              BRK                         
9D67: 00              BRK                         
9D68: 00              BRK                         
9D69: 00              BRK                         
9D6A: 00              BRK                         
9D6B: 00              BRK                         
9D6C: 00              BRK                         
9D6D: 00              BRK                         
9D6E: 00              BRK                         
9D6F: 00              BRK                         
9D70: 00              BRK                         
9D71: 00              BRK                         
9D72: 00              BRK                         
9D73: 00              BRK                         
9D74: 00              BRK                         
9D75: 00              BRK                         
9D76: 00              BRK                         
9D77: 00              BRK                         
9D78: 00              BRK                         
9D79: 00              BRK                         
9D7A: 00              BRK                         
9D7B: 00              BRK                         
9D7C: 00              BRK                         
9D7D: 00              BRK                         
9D7E: 00              BRK                         
9D7F: 00              BRK                         
9D80: 00              BRK                         
9D81: 00              BRK                         
9D82: 00              BRK                         
9D83: 00              BRK                         
9D84: 00              BRK                         
9D85: 00              BRK                         
9D86: 00              BRK                         
9D87: 00              BRK                         
9D88: 00              BRK                         
9D89: 00              BRK                         
9D8A: 00              BRK                         
9D8B: 00              BRK                         
9D8C: 00              BRK                         
9D8D: 00              BRK                         
9D8E: 00              BRK                         
9D8F: 00              BRK                         
9D90: 00              BRK                         
9D91: 00              BRK                         
9D92: 00              BRK                         
9D93: 00              BRK                         
9D94: 00              BRK                         
9D95: 00              BRK                         
9D96: 00              BRK                         
9D97: 00              BRK                         
9D98: 00              BRK                         
9D99: 00              BRK                         
9D9A: 00              BRK                         
9D9B: 00              BRK                         
9D9C: 00              BRK                         
9D9D: 00              BRK                         
9D9E: 00              BRK                         
9D9F: 00              BRK                         
9DA0: 00              BRK                         
9DA1: 00              BRK                         
9DA2: 00              BRK                         
9DA3: 00              BRK                         
9DA4: 00              BRK                         
9DA5: 00              BRK                         
9DA6: 00              BRK                         
9DA7: 00              BRK                         
9DA8: 00              BRK                         
9DA9: 00              BRK                         
9DAA: 00              BRK                         
9DAB: 00              BRK                         
9DAC: 00              BRK                         
9DAD: 00              BRK                         
9DAE: 00              BRK                         
9DAF: 00              BRK                         
9DB0: 00              BRK                         
9DB1: 00              BRK                         
9DB2: 00              BRK                         
9DB3: 00              BRK                         
9DB4: 00              BRK                         
9DB5: 00              BRK                         
9DB6: 00              BRK                         
9DB7: 00              BRK                         
9DB8: 00              BRK                         
9DB9: 00              BRK                         
9DBA: 00              BRK                         
9DBB: 00              BRK                         
9DBC: 00              BRK                         
9DBD: 00              BRK                         
9DBE: 00              BRK                         
9DBF: 00              BRK                         
9DC0: 00              BRK                         
9DC1: 00              BRK                         
9DC2: 00              BRK                         
9DC3: 00              BRK                         
9DC4: 00              BRK                         
9DC5: 00              BRK                         
9DC6: 00              BRK                         
9DC7: 00              BRK                         
9DC8: 00              BRK                         
9DC9: 00              BRK                         
9DCA: 00              BRK                         
9DCB: 00              BRK                         
9DCC: 00              BRK                         
9DCD: 00              BRK                         
9DCE: 00              BRK                         
9DCF: 00              BRK                         
9DD0: 00              BRK                         
9DD1: 00              BRK                         
9DD2: 00              BRK                         
9DD3: 00              BRK                         
9DD4: 00              BRK                         
9DD5: 00              BRK                         
9DD6: 00              BRK                         
9DD7: 00              BRK                         
9DD8: 00              BRK                         
9DD9: 00              BRK                         
9DDA: 00              BRK                         
9DDB: 00              BRK                         
9DDC: 00              BRK                         
9DDD: 00              BRK                         
9DDE: 00              BRK                         
9DDF: 00              BRK                         
9DE0: 00              BRK                         
9DE1: 00              BRK                         
9DE2: 00              BRK                         
9DE3: 00              BRK                         
9DE4: 00              BRK                         
9DE5: 00              BRK                         
9DE6: 00              BRK                         
9DE7: 00              BRK                         
9DE8: 00              BRK                         
9DE9: 00              BRK                         
9DEA: 00              BRK                         
9DEB: 00              BRK                         
9DEC: 00              BRK                         
9DED: 00              BRK                         
9DEE: 00              BRK                         
9DEF: 00              BRK                         
9DF0: 00              BRK                         
9DF1: 00              BRK                         
9DF2: 00              BRK                         
9DF3: 00              BRK                         
9DF4: 00              BRK                         
9DF5: 00              BRK                         
9DF6: 00              BRK                         
9DF7: 00              BRK                         
9DF8: 00              BRK                         
9DF9: 00              BRK                         
9DFA: 00              BRK                         
9DFB: 00              BRK                         
9DFC: 00              BRK                         
9DFD: 00              BRK                         
9DFE: 00              BRK                         
9DFF: 00              BRK                         
9E00: FF ; ????
9E01: FF ; ????
9E02: FF ; ????
9E03: FF ; ????
9E04: FF ; ????
9E05: FF ; ????
9E06: FF ; ????
9E07: FF ; ????
9E08: FF ; ????
9E09: FF ; ????
9E0A: FF ; ????
9E0B: FF ; ????
9E0C: FF ; ????
9E0D: FF ; ????
9E0E: FF ; ????
9E0F: FF ; ????
9E10: FF ; ????
9E11: FF ; ????
9E12: FF ; ????
9E13: FF ; ????
9E14: FF ; ????
9E15: FF ; ????
9E16: FF ; ????
9E17: FF ; ????
9E18: FF ; ????
9E19: FF ; ????
9E1A: FF ; ????
9E1B: FF ; ????
9E1C: FF ; ????
9E1D: FF ; ????
9E1E: FF ; ????
9E1F: FF ; ????
9E20: FF ; ????
9E21: FF ; ????
9E22: FF ; ????
9E23: FF ; ????
9E24: FF ; ????
9E25: FF ; ????
9E26: FF ; ????
9E27: FF ; ????
9E28: FF ; ????
9E29: FF ; ????
9E2A: FF ; ????
9E2B: FF ; ????
9E2C: FF ; ????
9E2D: FF ; ????
9E2E: FF ; ????
9E2F: FF ; ????
9E30: FF ; ????
9E31: FF ; ????
9E32: FF ; ????
9E33: FF ; ????
9E34: FF ; ????
9E35: FF ; ????
9E36: FF ; ????
9E37: FF ; ????
9E38: FF ; ????
9E39: FF ; ????
9E3A: FF ; ????
9E3B: FF ; ????
9E3C: FF ; ????
9E3D: FF ; ????
9E3E: FF ; ????
9E3F: FF ; ????
9E40: FF ; ????
9E41: FF ; ????
9E42: FF ; ????
9E43: FF ; ????
9E44: FF ; ????
9E45: FF ; ????
9E46: FF ; ????
9E47: FF ; ????
9E48: FF ; ????
9E49: FF ; ????
9E4A: FF ; ????
9E4B: FF ; ????
9E4C: FF ; ????
9E4D: FF ; ????
9E4E: FF ; ????
9E4F: FF ; ????
9E50: FF ; ????
9E51: FF ; ????
9E52: FF ; ????
9E53: FF ; ????
9E54: FF ; ????
9E55: FF ; ????
9E56: FF ; ????
9E57: FF ; ????
9E58: FF ; ????
9E59: FF ; ????
9E5A: FF ; ????
9E5B: FF ; ????
9E5C: FF ; ????
9E5D: FF ; ????
9E5E: FF ; ????
9E5F: FF ; ????
9E60: FF ; ????
9E61: FF ; ????
9E62: FF ; ????
9E63: FF ; ????
9E64: FF ; ????
9E65: FF ; ????
9E66: FF ; ????
9E67: FF ; ????
9E68: FF ; ????
9E69: FF ; ????
9E6A: FF ; ????
9E6B: FF ; ????
9E6C: FF ; ????
9E6D: FF ; ????
9E6E: FF ; ????
9E6F: FF ; ????
9E70: FF ; ????
9E71: FF ; ????
9E72: FF ; ????
9E73: FF ; ????
9E74: FF ; ????
9E75: FF ; ????
9E76: FF ; ????
9E77: FF ; ????
9E78: FF ; ????
9E79: FF ; ????
9E7A: FF ; ????
9E7B: FF ; ????
9E7C: FF ; ????
9E7D: FF ; ????
9E7E: FF ; ????
9E7F: FF ; ????
9E80: FF ; ????
9E81: FF ; ????
9E82: FF ; ????
9E83: FF ; ????
9E84: FF ; ????
9E85: FF ; ????
9E86: FF ; ????
9E87: FF ; ????
9E88: FF ; ????
9E89: FF ; ????
9E8A: FF ; ????
9E8B: FF ; ????
9E8C: FF ; ????
9E8D: FF ; ????
9E8E: FF ; ????
9E8F: FF ; ????
9E90: FF ; ????
9E91: FF ; ????
9E92: FF ; ????
9E93: FF ; ????
9E94: FF ; ????
9E95: FF ; ????
9E96: FF ; ????
9E97: FF ; ????
9E98: FF ; ????
9E99: FF ; ????
9E9A: FF ; ????
9E9B: FF ; ????
9E9C: FF ; ????
9E9D: FF ; ????
9E9E: FF ; ????
9E9F: FF ; ????
9EA0: FF ; ????
9EA1: FF ; ????
9EA2: FF ; ????
9EA3: FF ; ????
9EA4: FF ; ????
9EA5: FF ; ????
9EA6: FF ; ????
9EA7: FF ; ????
9EA8: FF ; ????
9EA9: FF ; ????
9EAA: FF ; ????
9EAB: FF ; ????
9EAC: FF ; ????
9EAD: FF ; ????
9EAE: FF ; ????
9EAF: FF ; ????
9EB0: FF ; ????
9EB1: FF ; ????
9EB2: FF ; ????
9EB3: FF ; ????
9EB4: FF ; ????
9EB5: FF ; ????
9EB6: FF ; ????
9EB7: FF ; ????
9EB8: FF ; ????
9EB9: FF ; ????
9EBA: FF ; ????
9EBB: FF ; ????
9EBC: FF ; ????
9EBD: FF ; ????
9EBE: FF ; ????
9EBF: FF ; ????
9EC0: FF ; ????
9EC1: FF ; ????
9EC2: FF ; ????
9EC3: FF ; ????
9EC4: FF ; ????
9EC5: FF ; ????
9EC6: FF ; ????
9EC7: FF ; ????
9EC8: FF ; ????
9EC9: FF ; ????
9ECA: FF ; ????
9ECB: FF ; ????
9ECC: FF ; ????
9ECD: FF ; ????
9ECE: FF ; ????
9ECF: FF ; ????
9ED0: FF ; ????
9ED1: FF ; ????
9ED2: FF ; ????
9ED3: FF ; ????
9ED4: FF ; ????
9ED5: FF ; ????
9ED6: FF ; ????
9ED7: FF ; ????
9ED8: FF ; ????
9ED9: FF ; ????
9EDA: FF ; ????
9EDB: FF ; ????
9EDC: FF ; ????
9EDD: FF ; ????
9EDE: FF ; ????
9EDF: FF ; ????
9EE0: FF ; ????
9EE1: FF ; ????
9EE2: FF ; ????
9EE3: FF ; ????
9EE4: FF ; ????
9EE5: FF ; ????
9EE6: FF ; ????
9EE7: FF ; ????
9EE8: FF ; ????
9EE9: FF ; ????
9EEA: FF ; ????
9EEB: FF ; ????
9EEC: FF ; ????
9EED: FF ; ????
9EEE: FF ; ????
9EEF: FF ; ????
9EF0: FF ; ????
9EF1: FF ; ????
9EF2: FF ; ????
9EF3: FF ; ????
9EF4: FF ; ????
9EF5: FF ; ????
9EF6: FF ; ????
9EF7: FF ; ????
9EF8: FF ; ????
9EF9: FF ; ????
9EFA: FF ; ????
9EFB: FF ; ????
9EFC: FF ; ????
9EFD: FF ; ????
9EFE: FF ; ????
9EFF: FF ; ????
9F00: 00              BRK                         
9F01: 00              BRK                         
9F02: 00              BRK                         
9F03: 00              BRK                         
9F04: 00              BRK                         
9F05: 00              BRK                         
9F06: 00              BRK                         
9F07: 00              BRK                         
9F08: 00              BRK                         
9F09: 00              BRK                         
9F0A: 00              BRK                         
9F0B: 00              BRK                         
9F0C: 00              BRK                         
9F0D: 00              BRK                         
9F0E: 00              BRK                         
9F0F: 00              BRK                         
9F10: 00              BRK                         
9F11: 00              BRK                         
9F12: 00              BRK                         
9F13: 00              BRK                         
9F14: 00              BRK                         
9F15: 00              BRK                         
9F16: 00              BRK                         
9F17: 00              BRK                         
9F18: 00              BRK                         
9F19: 00              BRK                         
9F1A: 00              BRK                         
9F1B: 00              BRK                         
9F1C: 00              BRK                         
9F1D: 00              BRK                         
9F1E: 00              BRK                         
9F1F: 00              BRK                         
9F20: 00              BRK                         
9F21: 00              BRK                         
9F22: 00              BRK                         
9F23: 00              BRK                         
9F24: 00              BRK                         
9F25: 00              BRK                         
9F26: 00              BRK                         
9F27: 00              BRK                         
9F28: 00              BRK                         
9F29: 00              BRK                         
9F2A: 00              BRK                         
9F2B: 00              BRK                         
9F2C: 00              BRK                         
9F2D: 00              BRK                         
9F2E: 00              BRK                         
9F2F: 00              BRK                         
9F30: 00              BRK                         
9F31: 00              BRK                         
9F32: 00              BRK                         
9F33: 00              BRK                         
9F34: 00              BRK                         
9F35: 00              BRK                         
9F36: 00              BRK                         
9F37: 00              BRK                         
9F38: 00              BRK                         
9F39: 00              BRK                         
9F3A: 00              BRK                         
9F3B: 00              BRK                         
9F3C: 00              BRK                         
9F3D: 00              BRK                         
9F3E: 00              BRK                         
9F3F: 00              BRK                         
9F40: 00              BRK                         
9F41: 00              BRK                         
9F42: 00              BRK                         
9F43: 00              BRK                         
9F44: 00              BRK                         
9F45: 00              BRK                         
9F46: 00              BRK                         
9F47: 00              BRK                         
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
9FF8: 22 ; ????
9FF9: 08              PHP                         
9FFA: 40              RTI                         
9FFB: 61 00           ADC     ($00,X)             ; {ram.GP_00}
9FFD: 00              BRK                         
9FFE: 10 40           BPL     $A040               ; {}
A000: 4C 06 A0        JMP     $A006               ; {}
A003: 4C FD A0        JMP     $A0FD               ; {}
A006: A9 00           LDA     #$00                
A008: 8D 10 40        STA     $4010               ; {hard.S_DMC_A}
A00B: 8D 11 40        STA     $4011               ; {hard.S_DMC_B}
A00E: A9 0F           LDA     #$0F                
A010: 8D 15 40        STA     $4015               ; {hard.S_Status}
A013: A9 C0           LDA     #$C0                
A015: 8D 17 40        STA     $4017               ; {hard.S_FrameCntr}
A018: A9 10           LDA     #$10                
A01A: 8D 00 40        STA     $4000               ; {hard.S_SQR1_A}
A01D: 8D 04 40        STA     $4004               ; {hard.S_SQR2_A}
A020: 8D 0C 40        STA     $400C               ; {hard.S_NOI_A}
A023: A9 00           LDA     #$00                
A025: 8D 08 40        STA     $4008               ; {hard.S_TRI_A}
A028: A9 00           LDA     #$00                
A02A: AA              TAX                         
A02B: 9D 00 03        STA     $0300,X             
A02E: E8              INX                         
A02F: D0 FA           BNE     $A02B               ; {}
A031: 85 DF           STA     $DF                 
A033: A9 AA           LDA     #$AA                
A035: 85 EF           STA     $EF                 
A037: 60              RTS                         
A038: FF ; ????
A039: FF ; ????
A03A: FF ; ????
A03B: FF ; ????
A03C: FF ; ????
A03D: FF ; ????
A03E: FF ; ????
A03F: FF ; ????
A040: FF ; ????
A041: FF ; ????
A042: FF ; ????
A043: FF ; ????
A044: FF ; ????
A045: FF ; ????
A046: FF ; ????
A047: FF ; ????
A048: FF ; ????
A049: FF ; ????
A04A: FF ; ????
A04B: FF ; ????
A04C: FF ; ????
A04D: FF ; ????
A04E: FF ; ????
A04F: FF ; ????
A050: FF ; ????
A051: FF ; ????
A052: FF ; ????
A053: FF ; ????
A054: FF ; ????
A055: FF ; ????
A056: FF ; ????
A057: FF ; ????
A058: FF ; ????
A059: FF ; ????
A05A: FF ; ????
A05B: FF ; ????
A05C: FF ; ????
A05D: FF ; ????
A05E: FF ; ????
A05F: FF ; ????
A060: FF ; ????
A061: FF ; ????
A062: FF ; ????
A063: FF ; ????
A064: FF ; ????
A065: FF ; ????
A066: FF ; ????
A067: FF ; ????
A068: FF ; ????
A069: FF ; ????
A06A: FF ; ????
A06B: FF ; ????
A06C: FF ; ????
A06D: FF ; ????
A06E: 7F ; ????
A06F: FF ; ????
A070: FF ; ????
A071: FF ; ????
A072: FF ; ????
A073: FF ; ????
A074: FF ; ????
A075: FF ; ????
A076: FF ; ????
A077: FF ; ????
A078: FF ; ????
A079: FF ; ????
A07A: FF ; ????
A07B: FF ; ????
A07C: FF ; ????
A07D: FF ; ????
A07E: FF ; ????
A07F: FF ; ????
A080: FF ; ????
A081: FF ; ????
A082: FF ; ????
A083: FF ; ????
A084: FF ; ????
A085: FF ; ????
A086: FF ; ????
A087: FF ; ????
A088: FF ; ????
A089: FF ; ????
A08A: FF ; ????
A08B: FF ; ????
A08C: FF ; ????
A08D: FF ; ????
A08E: FF ; ????
A08F: FF ; ????
A090: FF ; ????
A091: FF ; ????
A092: FF ; ????
A093: FF ; ????
A094: FF ; ????
A095: FF ; ????
A096: FF ; ????
A097: FF ; ????
A098: FF ; ????
A099: FF ; ????
A09A: FF ; ????
A09B: FF ; ????
A09C: FF ; ????
A09D: FF ; ????
A09E: FF ; ????
A09F: FF ; ????
A0A0: FF ; ????
A0A1: FF ; ????
A0A2: FF ; ????
A0A3: FF ; ????
A0A4: FF ; ????
A0A5: FF ; ????
A0A6: FF ; ????
A0A7: FF ; ????
A0A8: FF ; ????
A0A9: FF ; ????
A0AA: FF ; ????
A0AB: FF ; ????
A0AC: FF ; ????
A0AD: FF ; ????
A0AE: FF ; ????
A0AF: FF ; ????
A0B0: FF ; ????
A0B1: FF ; ????
A0B2: FF ; ????
A0B3: FF ; ????
A0B4: FF ; ????
A0B5: FF ; ????
A0B6: FF ; ????
A0B7: FF ; ????
A0B8: FF ; ????
A0B9: FF ; ????
A0BA: FF ; ????
A0BB: FF ; ????
A0BC: FF ; ????
A0BD: FF ; ????
A0BE: FF ; ????
A0BF: FF ; ????
A0C0: FF ; ????
A0C1: FF ; ????
A0C2: FF ; ????
A0C3: FF ; ????
A0C4: FF ; ????
A0C5: FF ; ????
A0C6: FF ; ????
A0C7: FF ; ????
A0C8: FF ; ????
A0C9: FF ; ????
A0CA: FF ; ????
A0CB: FF ; ????
A0CC: FF ; ????
A0CD: FF ; ????
A0CE: FF ; ????
A0CF: FF ; ????
A0D0: FF ; ????
A0D1: FF ; ????
A0D2: FF ; ????
A0D3: FF ; ????
A0D4: FF ; ????
A0D5: FF ; ????
A0D6: FF ; ????
A0D7: FF ; ????
A0D8: FF ; ????
A0D9: FF ; ????
A0DA: FF ; ????
A0DB: FF ; ????
A0DC: FF ; ????
A0DD: FF ; ????
A0DE: FF ; ????
A0DF: FF ; ????
A0E0: FF ; ????
A0E1: FF ; ????
A0E2: FF ; ????
A0E3: FF ; ????
A0E4: FF ; ????
A0E5: FF ; ????
A0E6: FF ; ????
A0E7: FF ; ????
A0E8: FF ; ????
A0E9: FF ; ????
A0EA: FF ; ????
A0EB: FF ; ????
A0EC: FF ; ????
A0ED: FF ; ????
A0EE: FF ; ????
A0EF: FF ; ????
A0F0: FF ; ????
A0F1: FF ; ????
A0F2: FF ; ????
A0F3: FF ; ????
A0F4: FF ; ????
A0F5: FF ; ????
A0F6: FF ; ????
A0F7: BF ; ????
A0F8: FF ; ????
A0F9: FF ; ????
A0FA: FF ; ????
A0FB: FF ; ????
A0FC: FF ; ????
A0FD: 4C CD A2        JMP     $A2CD               ; {}
A100: 00              BRK                         
A101: 10 00           BPL     $A103               ; {}
A103: 18              CLC                         
A104: 06 02           ASL     $02                 
A106: 18              CLC                         
A107: 02 ; ????
A108: 03 ; ????
A109: 40              RTI                         
A10A: 1D 7F 0F        ORA     $0F7F,X             
A10D: A0 06           LDY     #$06                
A10F: 7F ; ????
A110: 00              BRK                         
A111: 40              RTI                         
A112: 1A ; ????
A113: 7F ; ????
A114: 0B ; ????
A115: 18              CLC                         
A116: 19 7F 00        ORA     $007F,Y             
A119: 40              RTI                         
A11A: 09 7F           ORA     #$7F                
A11C: 02 ; ????
A11D: 40              RTI                         
A11E: DA ; ????
A11F: A5 B1           LDA     $B1                 
A121: 41 1A           EOR     ($1A,X)             
A123: A5 F9           LDA     $F9                 
A125: 41 DA           EOR     ($DA,X)             
A127: BC 49 C0        LDY     $C049,X             
A12A: DA ; ????
A12B: BC A5 C0        LDY     $C0A5,X             
A12E: DA ; ????
A12F: 86 30           STX     $30                 
A131: 42 ; ????
A132: DB ; ????
A133: 86 40           STX     $40                 
A135: 41 5A           EOR     ($5A,X)             
A137: 7F ; ????
A138: 50 8A           BVC     $A0C4               ; {}
A13A: 5A ; ????
A13B: 7F ; ????
A13C: 12 ; ????
A13D: 8A              TXA                         
A13E: 1B ; ????
A13F: 9E ; ????
A140: 73 ; ????
A141: 58              CLI                         
A142: 1B ; ????
A143: 8E 72 69        STX     $6972               
A146: D5 83           CMP     $83,X               
A148: 10 68           BPL     $A1B2               ; {}
A14A: 93 ; ????
A14B: 8D 27 F9        STA     $F927               
A14E: 98              TYA                         
A14F: 89 ; ????
A150: F0 18           BEQ     $A16A               ; {}
A152: 1F ; ????
A153: 7F ; ????
A154: 7C ; ????
A155: F9 9D DB        SBC     $DB9D,Y             
A158: 20 88 9E        JSR     $9E88               ; {}
A15B: 7F ; ????
A15C: 22 ; ????
A15D: 18              CLC                         
A15E: D8              CLD                         
A15F: A6 4B           LDX     $4B                 
A161: F8              SED                         
A162: D6 A6           DEC     $A6,X               
A164: 60              RTS                         
A165: F8              SED                         
A166: D9 97 56        CMP     $5697,Y             
A169: F8              SED                         
A16A: 7F ; ????
A16B: 7F ; ????
A16C: 20 88 7F        JSR     $7F88               
A16F: 7F ; ????
A170: 68              PLA                         
A171: F8              SED                         
A172: 09 7F           ORA     #$7F                
A174: 20 38 04        JSR     $0438               
A177: 7F ; ????
A178: A9 28           LDA     #$28                
A17A: 07 ; ????
A17B: 7F ; ????
A17C: 20 28 B0        JSR     $B028               ; {}
A17F: A1 17           LDA     ($17,X)             
A181: A2 00           LDX     #$00                
A183: C0 A1           CPY     #$A1                
A185: 04 ; ????
A186: A4 00           LDY     $00                 ; {ram.GP_00}
A188: D0 A1           BNE     $A12B               ; {}
A18A: 25 A2           AND     $A2                 
A18C: 01 E0           ORA     ($E0,X)             
A18E: A1 04           LDA     ($04,X)             
A190: A4 01           LDY     $01                 
A192: F0 A1           BEQ     $A135               ; {}
A194: 3A ; ????
A195: A2 03           LDX     #$03                
A197: 00              BRK                         
A198: A2 04           LDX     #$04                
A19A: A4 03           LDY     $03                 
A19C: B7 ; ????
A19D: AB ; ????
A19E: 53 ; ????
A19F: A2 04           LDX     #$04                
A1A1: C7 ; ????
A1A2: AB ; ????
A1A3: 5B ; ????
A1A4: A2 04           LDX     #$04                
A1A6: D7 ; ????
A1A7: AB ; ????
A1A8: FC ; ????
A1A9: AB ; ????
A1AA: 00              BRK                         
A1AB: D7 ; ????
A1AC: AB ; ????
A1AD: EE AB 00        INC     $00AB               
A1B0: 84 A4           STY     $A4                 
A1B2: 7E A4 5D        ROR     $5DA4,X             
A1B5: A4 A9           LDY     $A9                 
A1B7: A4 B8           LDY     $B8                 
A1B9: A4 BE           LDY     $BE                 
A1BB: A4 23           LDY     $23                 
A1BD: A4 04           LDY     $04                 
A1BF: A4 91           LDY     $91                 
A1C1: A4 6C           LDY     $6C                 
A1C3: A4 64           LDY     $64                 
A1C5: A4 9B           LDY     $9B                 
A1C7: A4 9B           LDY     $9B                 
A1C9: A4 C4           LDY     $C4                 
A1CB: A4 2A           LDY     $2A                 
A1CD: A4 04           LDY     $04                 
A1CF: A4 FF           LDY     $FF                 
A1D1: A5 5E           LDA     $5E                 
A1D3: A6 7A           LDX     $7A                 
A1D5: A6 9C           LDX     $9C                 
A1D7: A6 F5           LDX     $F5                 
A1D9: A6 E7           LDX     $E7                 
A1DB: A6 8E           LDX     $8E                 
A1DD: A6 B0           LDX     $B0                 
A1DF: A6 06           LDX     $06                 
A1E1: A6 4A           LDX     $4A                 
A1E3: A6 85           LDX     $85                 
A1E5: A6 A7           LDX     $A7                 
A1E7: A6 03           LDX     $03                 
A1E9: A7 ; ????
A1EA: 64 ; ????
A1EB: A6 64           LDX     $64                 
A1ED: A6 BD           LDX     $BD                 
A1EF: A6 7A           LDX     $7A                 
A1F1: A7 ; ????
A1F2: 08              PHP                         
A1F3: A8              TAY                         
A1F4: 04 ; ????
A1F5: A4 04           LDY     $04                 
A1F7: A4 D6           LDY     $D6                 
A1F9: A7 ; ????
A1FA: 04 ; ????
A1FB: A4 4A           LDY     $4A                 
A1FD: A7 ; ????
A1FE: C2 ; ????
A1FF: A7 ; ????
A200: 84 A7           STY     $A7                 
A202: 0F ; ????
A203: A8              TAY                         
A204: 04 ; ????
A205: A4 04           LDY     $04                 
A207: A4 E7           LDY     $E7                 
A209: A7 ; ????
A20A: 04 ; ????
A20B: A4 58           LDY     $58                 
A20D: A7 ; ????
A20E: 9E ; ????
A20F: A7 ; ????
A210: AD 80 03        LDA     $0380               
A213: A2 7E           LDX     #$7E                
A215: D0 15           BNE     $A22C               ; {}
A217: AD 88 03        LDA     $0388               
A21A: A2 83           LDX     #$83                
A21C: D0 0E           BNE     $A22C               ; {}
A21E: AD 81 03        LDA     $0381               
A221: A2 88           LDX     #$88                
A223: D0 07           BNE     $A22C               ; {}
A225: AD 89 03        LDA     $0389               
A228: A2 8D           LDX     #$8D                
A22A: D0 00           BNE     $A22C               ; {}
A22C: 20 D7 A3        JSR     $A3D7               ; {}
A22F: 6C EB 00        JMP     ($00EB)             
A232: AD 83 03        LDA     $0383               
A235: A2 92           LDX     #$92                
A237: 4C 2C A2        JMP     $A22C               ; {}
A23A: AD 8B 03        LDA     $038B               
A23D: A2 97           LDX     #$97                
A23F: 4C 2C A2        JMP     $A22C               ; {}
A242: AD 84 03        LDA     $0384               
A245: A2 9C           LDX     #$9C                
A247: 20 D7 A3        JSR     $A3D7               ; {}
A24A: 20 0D AC        JSR     $AC0D               ; {}
A24D: 20 1D AC        JSR     $AC1D               ; {}
A250: 6C EB 00        JMP     ($00EB)             
A253: AD 8C 03        LDA     $038C               
A256: A2 A1           LDX     #$A1                
A258: 4C 2C A2        JMP     $A22C               ; {}
A25B: 20 1E A2        JSR     $A21E               ; {}
A25E: 60              RTS                         
A25F: A5 EF           LDA     $EF                 
A261: 29 02           AND     #$02                
A263: 8D 1F 03        STA     $031F               
A266: A5 F0           LDA     $F0                 
A268: 29 02           AND     #$02                
A26A: 4D 1F 03        EOR     $031F               
A26D: 18              CLC                         
A26E: F0 01           BEQ     $A271               ; {}
A270: 38              SEC                         
A271: 66 EF           ROR     $EF                 
A273: 66 F0           ROR     $F0                 
A275: 60              RTS                         
A276: A9 00           LDA     #$00                
A278: F0 0A           BEQ     $A284               ; {}
A27A: A9 08           LDA     #$08                
A27C: D0 06           BNE     $A284               ; {}
A27E: A9 0C           LDA     #$0C                
A280: D0 02           BNE     $A284               ; {}
A282: A9 04           LDA     #$04                
A284: 85 E9           STA     $E9                 
A286: A9 40           LDA     #$40                
A288: 85 EA           STA     $EA                 
A28A: 84 EB           STY     $EB                 
A28C: A9 A1           LDA     #$A1                
A28E: 85 EC           STA     $EC                 
A290: A0 00           LDY     #$00                
A292: B1 EB           LDA     ($EB),Y             
A294: 91 E9           STA     ($E9),Y             
A296: C8              INY                         
A297: 98              TYA                         
A298: C9 04           CMP     #$04                
A29A: D0 F6           BNE     $A292               ; {}
A29C: 60              RTS                         
A29D: EE 02 03        INC     $0302               
A2A0: 20 5A A3        JSR     $A35A               ; {}
A2A3: 8D 03 03        STA     $0303               
A2A6: 60              RTS                         
A2A7: AD 02 03        LDA     $0302               
A2AA: F0 F1           BEQ     $A29D               ; {}
A2AC: AD 03 03        LDA     $0303               
A2AF: F0 13           BEQ     $A2C4               ; {}
A2B1: C9 12           CMP     #$12                
A2B3: F0 17           BEQ     $A2CC               ; {}
A2B5: 29 02           AND     #$02                
A2B7: F0 04           BEQ     $A2BD               ; {}
A2B9: A9 84           LDA     #$84                
A2BB: D0 02           BNE     $A2BF               ; {}
A2BD: A9 8B           LDA     #$8B                
A2BF: 8D 01 40        STA     $4001               ; {hard.S_SQR1_B}
A2C2: D0 05           BNE     $A2C9               ; {}
A2C4: A0 4A           LDY     #$4A                
A2C6: 20 76 A2        JSR     $A276               ; {}
A2C9: EE 03 03        INC     $0303               
A2CC: 60              RTS                         
A2CD: A9 C0           LDA     #$C0                
A2CF: 8D 17 40        STA     $4017               ; {hard.S_FrameCntr}
A2D2: 20 5F A2        JSR     $A25F               ; {}
A2D5: AD 80 03        LDA     $0380               
A2D8: 4A              LSR     A                   
A2D9: B0 2A           BCS     $A305               ; {}
A2DB: A5 DF           LDA     $DF                 
A2DD: D0 C8           BNE     $A2A7               ; {}
A2DF: A9 00           LDA     #$00                
A2E1: 8D 02 03        STA     $0302               
A2E4: 20 10 A2        JSR     $A210               ; {}
A2E7: 20 42 A2        JSR     $A242               ; {}
A2EA: 20 32 A2        JSR     $A232               ; {}
A2ED: 20 E7 AB        JSR     $ABE7               ; {}
A2F0: A9 00           LDA     #$00                
A2F2: 8D 80 03        STA     $0380               
A2F5: 8D 81 03        STA     $0381               
A2F8: 8D 82 03        STA     $0382               
A2FB: 8D 83 03        STA     $0383               
A2FE: 8D 84 03        STA     $0384               
A301: 8D 85 03        STA     $0385               
A304: 60              RTS                         
A305: 20 1D A3        JSR     $A31D               ; {}
A308: F0 E6           BEQ     $A2F0               ; {}
A30A: AD 2C 03        LDA     $032C               
A30D: F0 0E           BEQ     $A31D               ; {}
A30F: AD 8D 03        LDA     $038D               
A312: 8D 4F 03        STA     $034F               
A315: 60              RTS                         
A316: AD 8D 03        LDA     $038D               
A319: C5 E8           CMP     $E8                 
A31B: F0 06           BEQ     $A323               ; {}
A31D: 20 36 A3        JSR     $A336               ; {}
A320: 20 5A A3        JSR     $A35A               ; {}
A323: 20 27 A3        JSR     $A327               ; {}
A326: 60              RTS                         
A327: A9 00           LDA     #$00                
A329: 8D 2D 03        STA     $032D               
A32C: 8D 02 03        STA     $0302               
A32F: 8D 4F 03        STA     $034F               
A332: 8D 2C 03        STA     $032C               
A335: 60              RTS                         
A336: A9 00           LDA     #$00                
A338: 8D 4A 03        STA     $034A               
A33B: 8D 4B 03        STA     $034B               
A33E: 8D 4C 03        STA     $034C               
A341: 8D 4D 03        STA     $034D               
A344: 8D 07 03        STA     $0307               
A347: 8D 88 03        STA     $0388               
A34A: 8D 89 03        STA     $0389               
A34D: 8D 8A 03        STA     $038A               
A350: 8D 8B 03        STA     $038B               
A353: 8D 8C 03        STA     $038C               
A356: 8D 8D 03        STA     $038D               
A359: 60              RTS                         
A35A: A9 10           LDA     #$10                
A35C: 8D 00 40        STA     $4000               ; {hard.S_SQR1_A}
A35F: 8D 04 40        STA     $4004               ; {hard.S_SQR2_A}
A362: 8D 0C 40        STA     $400C               ; {hard.S_NOI_A}
A365: A9 00           LDA     #$00                
A367: 8D 08 40        STA     $4008               ; {hard.S_TRI_A}
A36A: 8D 11 40        STA     $4011               ; {hard.S_DMC_B}
A36D: 60              RTS                         
A36E: AE 4E 03        LDX     $034E               
A371: 9D 51 03        STA     $0351,X             
A374: 8A              TXA                         
A375: F0 1C           BEQ     $A393               ; {}
A377: C9 01           CMP     #$01                
A379: F0 09           BEQ     $A384               ; {}
A37B: C9 02           CMP     #$02                
A37D: F0 0B           BEQ     $A38A               ; {}
A37F: C9 03           CMP     #$03                
A381: F0 0A           BEQ     $A38D               ; {}
A383: 60              RTS                         
A384: 20 76 A2        JSR     $A276               ; {}
A387: 4C 96 A3        JMP     $A396               ; {}
A38A: 4C 96 A3        JMP     $A396               ; {}
A38D: 20 7A A2        JSR     $A27A               ; {}
A390: 4C 96 A3        JMP     $A396               ; {}
A393: 20 7E A2        JSR     $A27E               ; {}
A396: 20 AF A3        JSR     $A3AF               ; {}
A399: 8A              TXA                         
A39A: 9D 49 03        STA     $0349,X             
A39D: A9 00           LDA     #$00                
A39F: 9D 56 03        STA     $0356,X             
A3A2: 9D 60 03        STA     $0360,X             
A3A5: 9D 64 03        STA     $0364,X             
A3A8: 9D 68 03        STA     $0368,X             
A3AB: 8D 07 03        STA     $0307               
A3AE: 60              RTS                         
A3AF: AE 4E 03        LDX     $034E               
A3B2: BD 88 03        LDA     $0388,X             
A3B5: 29 00           AND     #$00                
A3B7: 05 E8           ORA     $E8                 
A3B9: 9D 88 03        STA     $0388,X             
A3BC: 60              RTS                         
A3BD: A9 00           LDA     #$00                
A3BF: 85 E8           STA     $E8                 
A3C1: F0 EC           BEQ     $A3AF               ; {}
A3C3: AE 4E 03        LDX     $034E               
A3C6: FE 56 03        INC     $0356,X             
A3C9: BD 56 03        LDA     $0356,X             
A3CC: DD 51 03        CMP     $0351,X             
A3CF: D0 05           BNE     $A3D6               ; {}
A3D1: A9 00           LDA     #$00                
A3D3: 9D 56 03        STA     $0356,X             
A3D6: 60              RTS                         
A3D7: 85 E8           STA     $E8                 
A3D9: 86 ED           STX     $ED                 
A3DB: A0 A1           LDY     #$A1                
A3DD: 84 EE           STY     $EE                 
A3DF: A0 00           LDY     #$00                
A3E1: B1 ED           LDA     ($ED),Y             
A3E3: 99 E9 00        STA     $00E9,Y             
A3E6: C8              INY                         
A3E7: 98              TYA                         
A3E8: C9 04           CMP     #$04                
A3EA: D0 F5           BNE     $A3E1               ; {}
A3EC: B1 ED           LDA     ($ED),Y             
A3EE: 8D 4E 03        STA     $034E               
A3F1: A0 00           LDY     #$00                
A3F3: A5 E8           LDA     $E8                 
A3F5: 48              PHA                         
A3F6: 06 E8           ASL     $E8                 
A3F8: B0 0B           BCS     $A405               ; {}
A3FA: C8              INY                         
A3FB: C8              INY                         
A3FC: 98              TYA                         
A3FD: C9 10           CMP     #$10                
A3FF: D0 F5           BNE     $A3F6               ; {}
A401: 68              PLA                         
A402: 85 E8           STA     $E8                 
A404: 60              RTS                         
A405: B1 E9           LDA     ($E9),Y             
A407: 85 EB           STA     $EB                 
A409: C8              INY                         
A40A: B1 E9           LDA     ($E9),Y             
A40C: 85 EC           STA     $EC                 
A40E: 4C 01 A4        JMP     $A401               ; {}
A411: 0D 09 00        ORA     $0009               
A414: 01 02           ORA     ($02,X)             
A416: 03 ; ????
A417: 04 ; ????
A418: 05 06           ORA     $06                 
A41A: 07 ; ????
A41B: 08              PHP                         
A41C: 07 ; ????
A41D: 06 05           ASL     $05                 
A41F: 04 ; ????
A420: 03 ; ????
A421: 03 ; ????
A422: 02 ; ????
A423: A9 10           LDA     #$10                
A425: A0 1A           LDY     #$1A                
A427: 4C 6E A3        JMP     $A36E               ; {}
A42A: 20 C3 A3        JSR     $A3C3               ; {}
A42D: D0 03           BNE     $A432               ; {}
A42F: 4C A0 A4        JMP     $A4A0               ; {}
A432: AC 60 03        LDY     $0360               
A435: B9 11 A4        LDA     $A411,Y             ; {}
A438: 8D 0E 40        STA     $400E               ; {hard.S_NOI_C}
A43B: EE 60 03        INC     $0360               
A43E: 60              RTS                         
A43F: 60              RTS                         
A440: 0F ; ????
A441: 09 0B           ORA     #$0B                
A443: 0F ; ????
A444: 0E 03 0F        ASL     $0F03               
A447: 0D 0F 08        ORA     $080F               
A44A: 07 ; ????
A44B: 06 05           ASL     $05                 
A44D: 03 ; ????
A44E: 02 ; ????
A44F: 02 ; ????
A450: EE 60 03        INC     $0360               
A453: AC 60 03        LDY     $0360               
A456: B9 40 A4        LDA     $A440,Y             ; {}
A459: 8D 0E 40        STA     $400E               ; {hard.S_NOI_C}
A45C: 60              RTS                         
A45D: A9 11           LDA     #$11                
A45F: A0 0A           LDY     #$0A                
A461: 4C B5 A4        JMP     $A4B5               ; {}
A464: 20 C3 A3        JSR     $A3C3               ; {}
A467: D0 E7           BNE     $A450               ; {}
A469: 4C A0 A4        JMP     $A4A0               ; {}
A46C: 20 C3 A3        JSR     $A3C3               ; {}
A46F: D0 EB           BNE     $A45C               ; {}
A471: EE 60 03        INC     $0360               
A474: AD 60 03        LDA     $0360               
A477: C9 10           CMP     #$10                
A479: F0 EE           BEQ     $A469               ; {}
A47B: 4C 59 A4        JMP     $A459               ; {}
A47E: A9 02           LDA     #$02                
A480: A0 16           LDY     #$16                
A482: D0 DD           BNE     $A461               ; {}
A484: A9 06           LDA     #$06                
A486: A0 0A           LDY     #$0A                
A488: 20 6E A3        JSR     $A36E               ; {}
A48B: A9 09           LDA     #$09                
A48D: 8D 60 03        STA     $0360               
A490: 60              RTS                         
A491: 20 C3 A3        JSR     $A3C3               ; {}
A494: F0 0A           BEQ     $A4A0               ; {}
A496: EE 60 03        INC     $0360               
A499: D0 2E           BNE     $A4C9               ; {}
A49B: 20 C3 A3        JSR     $A3C3               ; {}
A49E: D0 08           BNE     $A4A8               ; {}
A4A0: 20 BD A3        JSR     $A3BD               ; {}
A4A3: A9 10           LDA     #$10                
A4A5: 8D 0C 40        STA     $400C               ; {hard.S_NOI_A}
A4A8: 60              RTS                         
A4A9: AD 81 03        LDA     $0381               
A4AC: 09 04           ORA     #$04                
A4AE: 8D 81 03        STA     $0381               
A4B1: A9 16           LDA     #$16                
A4B3: A0 0E           LDY     #$0E                
A4B5: 4C 6E A3        JMP     $A36E               ; {}
A4B8: A9 02           LDA     #$02                
A4BA: A0 12           LDY     #$12                
A4BC: D0 F7           BNE     $A4B5               ; {}
A4BE: A9 04           LDA     #$04                
A4C0: A0 16           LDY     #$16                
A4C2: D0 F1           BNE     $A4B5               ; {}
A4C4: 20 C3 A3        JSR     $A3C3               ; {}
A4C7: F0 D7           BEQ     $A4A0               ; {}
A4C9: EE 60 03        INC     $0360               
A4CC: AD 60 03        LDA     $0360               
A4CF: 8D 0E 40        STA     $400E               ; {hard.S_NOI_C}
A4D2: 60              RTS                         
A4D3: A0 36           LDY     #$36                
A4D5: 20 76 A2        JSR     $A276               ; {}
A4D8: A9 0F           LDA     #$0F                
A4DA: A0 3A           LDY     #$3A                
A4DC: 4C 17 A5        JMP     $A517               ; {}
A4DF: 20 C3 A3        JSR     $A3C3               ; {}
A4E2: D0 C4           BNE     $A4A8               ; {}
A4E4: A0 36           LDY     #$36                
A4E6: 20 76 A2        JSR     $A276               ; {}
A4E9: A0 3A           LDY     #$3A                
A4EB: 20 82 A2        JSR     $A282               ; {}
A4EE: EE 61 03        INC     $0361               
A4F1: AD 61 03        LDA     $0361               
A4F4: C9 03           CMP     #$03                
A4F6: D0 B0           BNE     $A4A8               ; {}
A4F8: 4C 3F A5        JMP     $A53F               ; {}
A4FB: A0 2E           LDY     #$2E                
A4FD: 20 76 A2        JSR     $A276               ; {}
A500: A9 0F           LDA     #$0F                
A502: A0 32           LDY     #$32                
A504: 4C 17 A5        JMP     $A517               ; {}
A507: 20 C3 A3        JSR     $A3C3               ; {}
A50A: F0 33           BEQ     $A53F               ; {}
A50C: A5 EF           LDA     $EF                 
A50E: 09 80           ORA     #$80                
A510: 8D 02 40        STA     $4002               ; {hard.S_SQR1_C}
A513: 8D 06 40        STA     $4006               ; {hard.S_SQR2_C}
A516: 60              RTS                         
A517: 8D 55 03        STA     $0355               
A51A: 20 82 A2        JSR     $A282               ; {}
A51D: 20 AF A3        JSR     $A3AF               ; {}
A520: A9 01           LDA     #$01                
A522: 8D 4A 03        STA     $034A               
A525: A9 02           LDA     #$02                
A527: 8D 4B 03        STA     $034B               
A52A: A9 00           LDA     #$00                
A52C: 8D 89 03        STA     $0389               
A52F: 8D 61 03        STA     $0361               
A532: 8D 65 03        STA     $0365               
A535: 8D 69 03        STA     $0369               
A538: 8D 5A 03        STA     $035A               
A53B: 8D 07 03        STA     $0307               
A53E: 60              RTS                         
A53F: A9 10           LDA     #$10                
A541: 8D 00 40        STA     $4000               ; {hard.S_SQR1_A}
A544: 8D 04 40        STA     $4004               ; {hard.S_SQR2_A}
A547: A9 7F           LDA     #$7F                
A549: 8D 01 40        STA     $4001               ; {hard.S_SQR1_B}
A54C: 8D 05 40        STA     $4005               ; {hard.S_SQR2_B}
A54F: 20 BD A3        JSR     $A3BD               ; {}
A552: A9 00           LDA     #$00                
A554: 8D 4A 03        STA     $034A               
A557: 8D 4B 03        STA     $034B               
A55A: EE 07 03        INC     $0307               
A55D: 60              RTS                         
A55E: AD 89 03        LDA     $0389               
A561: 29 80           AND     #$80                
A563: D0 F8           BNE     $A55D               ; {}
A565: A0 1E           LDY     #$1E                
A567: 20 76 A2        JSR     $A276               ; {}
A56A: A5 EF           LDA     $EF                 
A56C: 29 03           AND     #$03                
A56E: 09 41           ORA     #$41                
A570: 8D 03 40        STA     $4003               ; {hard.S_SQR1_D}
A573: A9 02           LDA     #$02                
A575: A0 22           LDY     #$22                
A577: 20 17 A5        JSR     $A517               ; {}
A57A: A5 EF           LDA     $EF                 
A57C: 4A              LSR     A                   
A57D: 4A              LSR     A                   
A57E: 4A              LSR     A                   
A57F: 29 03           AND     #$03                
A581: 09 41           ORA     #$41                
A583: 8D 07 40        STA     $4007               ; {hard.S_SQR2_D}
A586: 60              RTS                         
A587: 20 C3 A3        JSR     $A3C3               ; {}
A58A: D0 D1           BNE     $A55D               ; {}
A58C: AD 65 03        LDA     $0365               
A58F: D0 0C           BNE     $A59D               ; {}
A591: A5 EF           LDA     $EF                 
A593: 09 C0           ORA     #$C0                
A595: 8D 02 40        STA     $4002               ; {hard.S_SQR1_C}
A598: E9 28           SBC     #$28                
A59A: 8D 06 40        STA     $4006               ; {hard.S_SQR2_C}
A59D: EE 61 03        INC     $0361               
A5A0: AD 61 03        LDA     $0361               
A5A3: C9 05           CMP     #$05                
A5A5: F0 07           BEQ     $A5AE               ; {}
A5A7: C9 0B           CMP     #$0B                
A5A9: D0 06           BNE     $A5B1               ; {}
A5AB: 4C 3F A5        JMP     $A53F               ; {}
A5AE: EE 65 03        INC     $0365               
A5B1: 60              RTS                         
A5B2: A0 26           LDY     #$26                
A5B4: 20 76 A2        JSR     $A276               ; {}
A5B7: A9 02           LDA     #$02                
A5B9: A0 2A           LDY     #$2A                
A5BB: 4C 17 A5        JMP     $A517               ; {}
A5BE: 20 C3 A3        JSR     $A3C3               ; {}
A5C1: D0 EE           BNE     $A5B1               ; {}
A5C3: AC 61 03        LDY     $0361               
A5C6: B9 D5 A5        LDA     $A5D5,Y             ; {}
A5C9: F0 E0           BEQ     $A5AB               ; {}
A5CB: 8D 01 40        STA     $4001               ; {hard.S_SQR1_B}
A5CE: 8D 05 40        STA     $4005               ; {hard.S_SQR2_B}
A5D1: EE 61 03        INC     $0361               
A5D4: 60              RTS                         
A5D5: A4 AC           LDY     $AC                 
A5D7: A4 AC           LDY     $AC                 
A5D9: A3 ; ????
A5DA: AC A3 AC        LDY     $ACA3               ; {}
A5DD: A3 ; ????
A5DE: AC 00 9B        LDY     $9B00               ; {}
A5E1: 97 ; ????
A5E2: 95 94           STA     $94,X               
A5E4: 93 ; ????
A5E5: 00              BRK                         
A5E6: 19 22 19        ORA     $1922,Y             
A5E9: 22 ; ????
A5EA: 19 22 40        ORA     $4022,Y             
A5ED: 48              PHA                         
A5EE: 40              RTI                         
A5EF: 48              PHA                         
A5F0: 40              RTI                         
A5F1: 48              PHA                         
A5F2: 0C ; ????
A5F3: 1C ; ????
A5F4: 93 ; ????
A5F5: AB ; ????
A5F6: 2D 3F 60        AND     $603F               
A5F9: A4 AC           LDY     $AC                 
A5FB: A3 ; ????
A5FC: AC A4 AC        LDY     $ACA4               ; {}
A5FF: A9 08           LDA     #$08                
A601: A0 5E           LDY     #$5E                
A603: 4C 6E A3        JMP     $A36E               ; {}
A606: 20 C3 A3        JSR     $A3C3               ; {}
A609: F0 1D           BEQ     $A628               ; {}
A60B: AD 69 03        LDA     $0369               
A60E: C9 02           CMP     #$02                
A610: D0 12           BNE     $A624               ; {}
A612: A9 00           LDA     #$00                
A614: 8D 69 03        STA     $0369               
A617: AC 65 03        LDY     $0365               
A61A: EE 65 03        INC     $0365               
A61D: B9 F9 A5        LDA     $A5F9,Y             ; {}
A620: 8D 01 40        STA     $4001               ; {hard.S_SQR1_B}
A623: 60              RTS                         
A624: EE 69 03        INC     $0369               
A627: 60              RTS                         
A628: A9 00           LDA     #$00                
A62A: 8D 65 03        STA     $0365               
A62D: AD 61 03        LDA     $0361               
A630: F0 0B           BEQ     $A63D               ; {}
A632: C9 01           CMP     #$01                
A634: F0 0B           BEQ     $A641               ; {}
A636: C9 02           CMP     #$02                
A638: D0 3F           BNE     $A679               ; {}
A63A: 4C 69 A6        JMP     $A669               ; {}
A63D: A0 62           LDY     #$62                
A63F: D0 02           BNE     $A643               ; {}
A641: A0 66           LDY     #$66                
A643: 20 76 A2        JSR     $A276               ; {}
A646: EE 61 03        INC     $0361               
A649: 60              RTS                         
A64A: 20 C3 A3        JSR     $A3C3               ; {}
A64D: D0 A9           BNE     $A5F8               ; {}
A64F: EE 61 03        INC     $0361               
A652: AD 61 03        LDA     $0361               
A655: C9 02           CMP     #$02                
A657: F0 10           BEQ     $A669               ; {}
A659: A0 3E           LDY     #$3E                
A65B: 4C 76 A2        JMP     $A276               ; {}
A65E: A9 0A           LDA     #$0A                
A660: A0 42           LDY     #$42                
A662: D0 35           BNE     $A699               ; {}
A664: 20 C3 A3        JSR     $A3C3               ; {}
A667: D0 8F           BNE     $A5F8               ; {}
A669: A9 10           LDA     #$10                
A66B: 8D 00 40        STA     $4000               ; {hard.S_SQR1_A}
A66E: A9 00           LDA     #$00                
A670: 8D 4A 03        STA     $034A               
A673: 20 BD A3        JSR     $A3BD               ; {}
A676: EE 07 03        INC     $0307               
A679: 60              RTS                         
A67A: A9 05           LDA     #$05                
A67C: A0 52           LDY     #$52                
A67E: 20 99 A6        JSR     $A699               ; {}
A681: A9 0D           LDA     #$0D                
A683: D0 34           BNE     $A6B9               ; {}
A685: 20 C3 A3        JSR     $A3C3               ; {}
A688: D0 EF           BNE     $A679               ; {}
A68A: A0 52           LDY     #$52                
A68C: D0 36           BNE     $A6C4               ; {}
A68E: AD 89 03        LDA     $0389               
A691: 29 18           AND     #$18                
A693: D0 27           BNE     $A6BC               ; {}
A695: A9 07           LDA     #$07                
A697: A0 4A           LDY     #$4A                
A699: 4C 6E A3        JMP     $A36E               ; {}
A69C: A9 08           LDA     #$08                
A69E: A0 56           LDY     #$56                
A6A0: 20 99 A6        JSR     $A699               ; {}
A6A3: A9 06           LDA     #$06                
A6A5: D0 12           BNE     $A6B9               ; {}
A6A7: 20 C3 A3        JSR     $A3C3               ; {}
A6AA: D0 CD           BNE     $A679               ; {}
A6AC: A0 56           LDY     #$56                
A6AE: D0 14           BNE     $A6C4               ; {}
A6B0: A9 04           LDA     #$04                
A6B2: A0 5A           LDY     #$5A                
A6B4: 20 99 A6        JSR     $A699               ; {}
A6B7: A9 00           LDA     #$00                
A6B9: 8D 65 03        STA     $0365               
A6BC: 60              RTS                         
A6BD: 20 C3 A3        JSR     $A3C3               ; {}
A6C0: D0 FA           BNE     $A6BC               ; {}
A6C2: A0 5A           LDY     #$5A                
A6C4: 20 76 A2        JSR     $A276               ; {}
A6C7: 18              CLC                         
A6C8: AD 65 03        LDA     $0365               
A6CB: 6D 61 03        ADC     $0361               
A6CE: A8              TAY                         
A6CF: B9 E6 A5        LDA     $A5E6,Y             ; {}
A6D2: 8D 02 40        STA     $4002               ; {hard.S_SQR1_C}
A6D5: AC 61 03        LDY     $0361               
A6D8: B9 E0 A5        LDA     $A5E0,Y             ; {}
A6DB: 8D 00 40        STA     $4000               ; {hard.S_SQR1_A}
A6DE: D0 03           BNE     $A6E3               ; {}
A6E0: 4C 69 A6        JMP     $A669               ; {}
A6E3: EE 61 03        INC     $0361               
A6E6: 60              RTS                         
A6E7: AD 89 03        LDA     $0389               
A6EA: 29 18           AND     #$18                
A6EC: D0 F8           BNE     $A6E6               ; {}
A6EE: A9 05           LDA     #$05                
A6F0: A0 46           LDY     #$46                
A6F2: 4C 6E A3        JMP     $A36E               ; {}
A6F5: A9 02           LDA     #$02                
A6F7: A0 4E           LDY     #$4E                
A6F9: 20 6E A3        JSR     $A36E               ; {}
A6FC: AD 50 A1        LDA     $A150               ; {}
A6FF: 8D 61 03        STA     $0361               
A702: 60              RTS                         
A703: 20 C3 A3        JSR     $A3C3               ; {}
A706: D0 DE           BNE     $A6E6               ; {}
A708: EE 65 03        INC     $0365               
A70B: AD 65 03        LDA     $0365               
A70E: C9 09           CMP     #$09                
A710: D0 03           BNE     $A715               ; {}
A712: 4C 69 A6        JMP     $A669               ; {}
A715: AD 61 03        LDA     $0361               
A718: 4A              LSR     A                   
A719: 4A              LSR     A                   
A71A: 4A              LSR     A                   
A71B: 8D 69 03        STA     $0369               
A71E: AD 61 03        LDA     $0361               
A721: 18              CLC                         
A722: ED 69 03        SBC     $0369               
A725: 8D 61 03        STA     $0361               
A728: 8D 02 40        STA     $4002               ; {hard.S_SQR1_C}
A72B: A9 18           LDA     #$18                
A72D: 8D 03 40        STA     $4003               ; {hard.S_SQR1_D}
A730: 60              RTS                         
A731: 4A              LSR     A                   
A732: 7E 4A 7E        ROR     $7E4A,X             
A735: 46 70           LSR     $70                 
A737: 46 70           LSR     $70                 
A739: 42 ; ????
A73A: 69 42           ADC     #$42                
A73C: 69 3E           ADC     #$3E                
A73E: 63 ; ????
A73F: 3E 63 3E        ROL     $3E63,X             
A742: 63 ; ????
A743: 3E 63 3E        ROL     $3E63,X             
A746: 63 ; ????
A747: 3E 63 00        ROL     $0063,X             
A74A: A9 0A           LDA     #$0A                
A74C: A0 6E           LDY     #$6E                
A74E: 20 6E A3        JSR     $A36E               ; {}
A751: AD 70 A1        LDA     $A170               ; {}
A754: 8D 63 03        STA     $0363               
A757: 60              RTS                         
A758: 20 C3 A3        JSR     $A3C3               ; {}
A75B: F0 59           BEQ     $A7B6               ; {}
A75D: AD 63 03        LDA     $0363               
A760: E9 06           SBC     #$06                
A762: 8D 63 03        STA     $0363               
A765: A5 EF           LDA     $EF                 
A767: 29 3F           AND     #$3F                
A769: 09 10           ORA     #$10                
A76B: 8D 67 03        STA     $0367               
A76E: AD 63 03        LDA     $0363               
A771: 29 C0           AND     #$C0                
A773: 0D 67 03        ORA     $0367               
A776: 8D 0A 40        STA     $400A               ; {hard.S_TRI_C}
A779: 60              RTS                         
A77A: A9 03           LDA     #$03                
A77C: A0 72           LDY     #$72                
A77E: 20 6E A3        JSR     $A36E               ; {}
A781: 4C 89 A7        JMP     $A789               ; {}
A784: 20 C3 A3        JSR     $A3C3               ; {}
A787: D0 38           BNE     $A7C1               ; {}
A789: AC 63 03        LDY     $0363               
A78C: B9 31 A7        LDA     $A731,Y             ; {}
A78F: F0 25           BEQ     $A7B6               ; {}
A791: 8D 0A 40        STA     $400A               ; {hard.S_TRI_C}
A794: AD 75 A1        LDA     $A175               ; {}
A797: 8D 0B 40        STA     $400B               ; {hard.S_TRI_D}
A79A: EE 63 03        INC     $0363               
A79D: 60              RTS                         
A79E: 20 C3 A3        JSR     $A3C3               ; {}
A7A1: F0 13           BEQ     $A7B6               ; {}
A7A3: CE 63 03        DEC     $0363               
A7A6: CE 63 03        DEC     $0363               
A7A9: CE 63 03        DEC     $0363               
A7AC: CE 63 03        DEC     $0363               
A7AF: AD 63 03        LDA     $0363               
A7B2: 8D 0A 40        STA     $400A               ; {hard.S_TRI_C}
A7B5: 60              RTS                         
A7B6: A9 00           LDA     #$00                
A7B8: 8D 08 40        STA     $4008               ; {hard.S_TRI_A}
A7BB: 8D 4C 03        STA     $034C               
A7BE: 20 BD A3        JSR     $A3BD               ; {}
A7C1: 60              RTS                         
A7C2: A9 03           LDA     #$03                
A7C4: A0 6A           LDY     #$6A                
A7C6: 20 6E A3        JSR     $A36E               ; {}
A7C9: A5 EF           LDA     $EF                 
A7CB: 29 3F           AND     #$3F                
A7CD: 09 60           ORA     #$60                
A7CF: 8D 0A 40        STA     $400A               ; {hard.S_TRI_C}
A7D2: 8D 63 03        STA     $0363               
A7D5: 60              RTS                         
A7D6: A9 03           LDA     #$03                
A7D8: A0 76           LDY     #$76                
A7DA: 20 6E A3        JSR     $A36E               ; {}
A7DD: A5 EF           LDA     $EF                 
A7DF: 29 0F           AND     #$0F                
A7E1: 09 06           ORA     #$06                
A7E3: 8D 6B 03        STA     $036B               
A7E6: 60              RTS                         
A7E7: 20 C3 A3        JSR     $A3C3               ; {}
A7EA: D0 D5           BNE     $A7C1               ; {}
A7EC: A5 EF           LDA     $EF                 
A7EE: 09 90           ORA     #$90                
A7F0: 8D 0A 40        STA     $400A               ; {hard.S_TRI_C}
A7F3: AD 79 A1        LDA     $A179               ; {}
A7F6: 8D 0B 40        STA     $400B               ; {hard.S_TRI_D}
A7F9: EE 63 03        INC     $0363               
A7FC: AD 63 03        LDA     $0363               
A7FF: CD 6B 03        CMP     $036B               
A802: D0 BD           BNE     $A7C1               ; {}
A804: 4C B6 A7        JMP     $A7B6               ; {}
A807: 60              RTS                         
A808: A9 05           LDA     #$05                
A80A: A0 7A           LDY     #$7A                
A80C: 4C 6E A3        JMP     $A36E               ; {}
A80F: 20 C3 A3        JSR     $A3C3               ; {}
A812: F0 01           BEQ     $A815               ; {}
A814: 60              RTS                         
A815: A0 7A           LDY     #$7A                
A817: 20 7A A2        JSR     $A27A               ; {}
A81A: EE 63 03        INC     $0363               
A81D: AD 63 03        LDA     $0363               
A820: C9 02           CMP     #$02                
A822: D0 F0           BNE     $A814               ; {}
A824: 4C B6 A7        JMP     $A7B6               ; {}
A827: 18              CLC                         
A828: AD 10 03        LDA     $0310               
A82B: 6D 12 03        ADC     $0312               
A82E: 8D 10 03        STA     $0310               
A831: AD 11 03        LDA     $0311               
A834: 6D 13 03        ADC     $0313               
A837: 8D 11 03        STA     $0311               
A83A: 60              RTS                         
A83B: 38              SEC                         
A83C: AD 10 03        LDA     $0310               
A83F: ED 12 03        SBC     $0312               
A842: 8D 10 03        STA     $0310               
A845: AD 11 03        LDA     $0311               
A848: ED 13 03        SBC     $0313               
A84B: 8D 11 03        STA     $0311               
A84E: 60              RTS                         
A84F: AD 10 03        LDA     $0310               
A852: 48              PHA                         
A853: AD 11 03        LDA     $0311               
A856: 48              PHA                         
A857: A9 00           LDA     #$00                
A859: 8D 17 03        STA     $0317               
A85C: A2 10           LDX     #$10                
A85E: 2E 10 03        ROL     $0310               
A861: 2E 11 03        ROL     $0311               
A864: 2E 17 03        ROL     $0317               
A867: AD 17 03        LDA     $0317               
A86A: CD 16 03        CMP     $0316               
A86D: 90 06           BCC     $A875               ; {}
A86F: ED 16 03        SBC     $0316               
A872: 8D 17 03        STA     $0317               
A875: 2E 10 03        ROL     $0310               
A878: 2E 11 03        ROL     $0311               
A87B: CA              DEX                         
A87C: D0 E6           BNE     $A864               ; {}
A87E: AD 10 03        LDA     $0310               
A881: 8D 14 03        STA     $0314               
A884: AD 11 03        LDA     $0311               
A887: 8D 15 03        STA     $0315               
A88A: 68              PLA                         
A88B: 8D 11 03        STA     $0311               
A88E: 68              PLA                         
A88F: 8D 10 03        STA     $0310               
A892: 60              RTS                         
A893: 20 16 A3        JSR     $A316               ; {}
A896: A5 E8           LDA     $E8                 
A898: 8D 8D 03        STA     $038D               
A89B: AD 50 03        LDA     $0350               
A89E: A8              TAY                         
A89F: B9 AB AB        LDA     $ABAB,Y             ; {}
A8A2: A8              TAY                         
A8A3: A2 00           LDX     #$00                
A8A5: B9 88 AC        LDA     $AC88,Y             ; {}
A8A8: 9D 2B 03        STA     $032B,X             
A8AB: C8              INY                         
A8AC: E8              INX                         
A8AD: 8A              TXA                         
A8AE: C9 0D           CMP     #$0D                
A8B0: D0 F3           BNE     $A8A5               ; {}
A8B2: A9 01           LDA     #$01                
A8B4: 8D 40 03        STA     $0340               
A8B7: 8D 41 03        STA     $0341               
A8BA: 8D 42 03        STA     $0342               
A8BD: 8D 43 03        STA     $0343               
A8C0: A9 00           LDA     #$00                
A8C2: 8D 38 03        STA     $0338               
A8C5: 8D 39 03        STA     $0339               
A8C8: 8D 3A 03        STA     $033A               
A8CB: 8D 3B 03        STA     $033B               
A8CE: 60              RTS                         
A8CF: A9 7F           LDA     #$7F                
A8D1: 8D 44 03        STA     $0344               
A8D4: 8D 45 03        STA     $0345               
A8D7: 8E 28 03        STX     $0328               
A8DA: 8C 29 03        STY     $0329               
A8DD: 60              RTS                         
A8DE: AD 40 03        LDA     $0340               
A8E1: C9 01           CMP     #$01                
A8E3: D0 03           BNE     $A8E8               ; {}
A8E5: 8D 5B 03        STA     $035B               
A8E8: AD 41 03        LDA     $0341               
A8EB: C9 01           CMP     #$01                
A8ED: D0 03           BNE     $A8F2               ; {}
A8EF: 8D 5C 03        STA     $035C               
A8F2: 60              RTS                         
A8F3: AD 07 03        LDA     $0307               
A8F6: F0 29           BEQ     $A921               ; {}
A8F8: A9 00           LDA     #$00                
A8FA: 8D 07 03        STA     $0307               
A8FD: AD 44 03        LDA     $0344               
A900: 8D 01 40        STA     $4001               ; {hard.S_SQR1_B}
A903: AD 00 03        LDA     $0300               
A906: 8D 02 40        STA     $4002               ; {hard.S_SQR1_C}
A909: AD 01 03        LDA     $0301               
A90C: 8D 03 40        STA     $4003               ; {hard.S_SQR1_D}
A90F: AD 45 03        LDA     $0345               
A912: 8D 05 40        STA     $4005               ; {hard.S_SQR2_B}
A915: AD 04 03        LDA     $0304               
A918: 8D 06 40        STA     $4006               ; {hard.S_SQR2_C}
A91B: AD 05 03        LDA     $0305               
A91E: 8D 07 40        STA     $4007               ; {hard.S_SQR2_D}
A921: 60              RTS                         
A922: A2 00           LDX     #$00                
A924: 20 2C A9        JSR     $A92C               ; {}
A927: E8              INX                         
A928: 20 2C A9        JSR     $A92C               ; {}
A92B: 60              RTS                         
A92C: BD 2E 03        LDA     $032E,X             
A92F: F0 45           BEQ     $A976               ; {}
A931: 85 E1           STA     $E1                 
A933: 20 F3 A8        JSR     $A8F3               ; {}
A936: BD 5D 03        LDA     $035D,X             
A939: C9 10           CMP     #$10                
A93B: F0 47           BEQ     $A984               ; {}
A93D: A0 00           LDY     #$00                
A93F: C6 E1           DEC     $E1                 
A941: F0 04           BEQ     $A947               ; {}
A943: C8              INY                         
A944: C8              INY                         
A945: D0 F8           BNE     $A93F               ; {}
A947: B9 64 AC        LDA     $AC64,Y             ; {}
A94A: 85 E2           STA     $E2                 
A94C: B9 65 AC        LDA     $AC65,Y             ; {}
A94F: 85 E3           STA     $E3                 
A951: BC 5B 03        LDY     $035B,X             
A954: B1 E2           LDA     ($E2),Y             
A956: 85 E0           STA     $E0                 
A958: C9 FF           CMP     #$FF                
A95A: F0 1F           BEQ     $A97B               ; {}
A95C: C9 F0           CMP     #$F0                
A95E: F0 20           BEQ     $A980               ; {}
A960: BD 28 03        LDA     $0328,X             
A963: 29 F0           AND     #$F0                
A965: 05 E0           ORA     $E0                 
A967: A8              TAY                         
A968: FE 5B 03        INC     $035B,X             
A96B: BD 4A 03        LDA     $034A,X             
A96E: D0 06           BNE     $A976               ; {}
A970: 8A              TXA                         
A971: F0 04           BEQ     $A977               ; {}
A973: 8C 04 40        STY     $4004               ; {hard.S_SQR2_A}
A976: 60              RTS                         
A977: 8C 00 40        STY     $4000               ; {hard.S_SQR1_A}
A97A: 60              RTS                         
A97B: BC 28 03        LDY     $0328,X             
A97E: D0 EB           BNE     $A96B               ; {}
A980: A0 10           LDY     #$10                
A982: D0 E7           BNE     $A96B               ; {}
A984: A0 10           LDY     #$10                
A986: D0 E0           BNE     $A968               ; {}
A988: BC 38 03        LDY     $0338,X             
A98B: FE 38 03        INC     $0338,X             
A98E: D0 14           BNE     $A9A4               ; {}
A990: 8A              TXA                         
A991: 0A              ASL     A                   
A992: AA              TAX                         
A993: FE 31 03        INC     $0331,X             
A996: 8A              TXA                         
A997: 4A              LSR     A                   
A998: AA              TAX                         
A999: B1 E6           LDA     ($E6),Y             
A99B: 85 E9           STA     $E9                 
A99D: E6 E7           INC     $E7                 
A99F: A5 E9           LDA     $E9                 
A9A1: 4C A6 A9        JMP     $A9A6               ; {}
A9A4: B1 E6           LDA     ($E6),Y             
A9A6: 60              RTS                         
A9A7: 20 0A A3        JSR     $A30A               ; {}
A9AA: 60              RTS                         
A9AB: 20 22 A9        JSR     $A922               ; {}
A9AE: 60              RTS                         
A9AF: 20 DE A8        JSR     $A8DE               ; {}
A9B2: A9 00           LDA     #$00                
A9B4: AA              TAX                         
A9B5: 8D 47 03        STA     $0347               
A9B8: F0 12           BEQ     $A9CC               ; {}
A9BA: 8A              TXA                         
A9BB: 4A              LSR     A                   
A9BC: AA              TAX                         
A9BD: E8              INX                         
A9BE: 8A              TXA                         
A9BF: C9 04           CMP     #$04                
A9C1: F0 E8           BEQ     $A9AB               ; {}
A9C3: AD 47 03        LDA     $0347               
A9C6: 18              CLC                         
A9C7: 69 04           ADC     #$04                
A9C9: 8D 47 03        STA     $0347               
A9CC: 8A              TXA                         
A9CD: 0A              ASL     A                   
A9CE: AA              TAX                         
A9CF: BD 30 03        LDA     $0330,X             
A9D2: 85 E6           STA     $E6                 
A9D4: BD 31 03        LDA     $0331,X             
A9D7: 85 E7           STA     $E7                 
A9D9: BD 31 03        LDA     $0331,X             
A9DC: F0 DC           BEQ     $A9BA               ; {}
A9DE: 8A              TXA                         
A9DF: 4A              LSR     A                   
A9E0: AA              TAX                         
A9E1: DE 40 03        DEC     $0340,X             
A9E4: D0 D7           BNE     $A9BD               ; {}
A9E6: 20 88 A9        JSR     $A988               ; {}
A9E9: F0 BC           BEQ     $A9A7               ; {}
A9EB: A8              TAY                         
A9EC: C9 FF           CMP     #$FF                
A9EE: F0 09           BEQ     $A9F9               ; {}
A9F0: 29 C0           AND     #$C0                
A9F2: C9 C0           CMP     #$C0                
A9F4: F0 13           BEQ     $AA09               ; {}
A9F6: 4C 21 AA        JMP     $AA21               ; {}
A9F9: BD 24 03        LDA     $0324,X             
A9FC: F0 1A           BEQ     $AA18               ; {}
A9FE: DE 24 03        DEC     $0324,X             
AA01: BD 3C 03        LDA     $033C,X             
AA04: 9D 38 03        STA     $0338,X             
AA07: D0 0F           BNE     $AA18               ; {}
AA09: 98              TYA                         
AA0A: 29 3F           AND     #$3F                
AA0C: 9D 24 03        STA     $0324,X             
AA0F: DE 24 03        DEC     $0324,X             
AA12: BD 38 03        LDA     $0338,X             
AA15: 9D 3C 03        STA     $033C,X             
AA18: 4C E6 A9        JMP     $A9E6               ; {}
AA1B: 4C DE AA        JMP     $AADE               ; {}
AA1E: 4C B7 AA        JMP     $AAB7               ; {}
AA21: 98              TYA                         
AA22: 29 B0           AND     #$B0                
AA24: C9 B0           CMP     #$B0                
AA26: D0 18           BNE     $AA40               ; {}
AA28: 98              TYA                         
AA29: 29 0F           AND     #$0F                
AA2B: 18              CLC                         
AA2C: 6D 2B 03        ADC     $032B               
AA2F: A8              TAY                         
AA30: B9 86 AB        LDA     $AB86,Y             ; {}
AA33: 9D 20 03        STA     $0320,X             
AA36: A8              TAY                         
AA37: 8A              TXA                         
AA38: C9 02           CMP     #$02                
AA3A: F0 E2           BEQ     $AA1E               ; {}
AA3C: 20 88 A9        JSR     $A988               ; {}
AA3F: A8              TAY                         
AA40: 8A              TXA                         
AA41: C9 03           CMP     #$03                
AA43: F0 D6           BEQ     $AA1B               ; {}
AA45: 48              PHA                         
AA46: AE 47 03        LDX     $0347               
AA49: B9 FB AA        LDA     $AAFB,Y             ; {}
AA4C: F0 0B           BEQ     $AA59               ; {}
AA4E: 9D 00 03        STA     $0300,X             
AA51: B9 FA AA        LDA     $AAFA,Y             ; {}
AA54: 09 08           ORA     #$08                
AA56: 9D 01 03        STA     $0301,X             
AA59: A8              TAY                         
AA5A: 68              PLA                         
AA5B: AA              TAX                         
AA5C: 98              TYA                         
AA5D: D0 0F           BNE     $AA6E               ; {}
AA5F: A9 00           LDA     #$00                
AA61: 85 E0           STA     $E0                 
AA63: 8A              TXA                         
AA64: C9 02           CMP     #$02                
AA66: F0 0B           BEQ     $AA73               ; {}
AA68: A9 10           LDA     #$10                
AA6A: 85 E0           STA     $E0                 
AA6C: D0 05           BNE     $AA73               ; {}
AA6E: BD 28 03        LDA     $0328,X             
AA71: 85 E0           STA     $E0                 
AA73: 8A              TXA                         
AA74: DE 4A 03        DEC     $034A,X             
AA77: DD 4A 03        CMP     $034A,X             
AA7A: F0 35           BEQ     $AAB1               ; {}
AA7C: FE 4A 03        INC     $034A,X             
AA7F: AC 47 03        LDY     $0347               
AA82: 8A              TXA                         
AA83: C9 02           CMP     #$02                
AA85: F0 05           BEQ     $AA8C               ; {}
AA87: BD 2E 03        LDA     $032E,X             
AA8A: D0 05           BNE     $AA91               ; {}
AA8C: A5 E0           LDA     $E0                 
AA8E: 99 00 40        STA     $4000,Y             ; {hard.S_SQR1_A}
AA91: A5 E0           LDA     $E0                 
AA93: 9D 5D 03        STA     $035D,X             
AA96: B9 00 03        LDA     $0300,Y             
AA99: 99 02 40        STA     $4002,Y             ; {hard.S_SQR1_C}
AA9C: B9 01 03        LDA     $0301,Y             
AA9F: 99 03 40        STA     $4003,Y             ; {hard.S_SQR1_D}
AAA2: BD 44 03        LDA     $0344,X             
AAA5: 99 01 40        STA     $4001,Y             ; {hard.S_SQR1_B}
AAA8: BD 20 03        LDA     $0320,X             
AAAB: 9D 40 03        STA     $0340,X             
AAAE: 4C BD A9        JMP     $A9BD               ; {}
AAB1: FE 4A 03        INC     $034A,X             
AAB4: 4C A8 AA        JMP     $AAA8               ; {}
AAB7: AD 2D 03        LDA     $032D               
AABA: 29 0F           AND     #$0F                
AABC: D0 1A           BNE     $AAD8               ; {}
AABE: AD 2D 03        LDA     $032D               
AAC1: 29 F0           AND     #$F0                
AAC3: D0 04           BNE     $AAC9               ; {}
AAC5: 98              TYA                         
AAC6: 4C CD AA        JMP     $AACD               ; {}
AAC9: A9 FF           LDA     #$FF                
AACB: D0 0B           BNE     $AAD8               ; {}
AACD: 18              CLC                         
AACE: 69 FF           ADC     #$FF                
AAD0: 0A              ASL     A                   
AAD1: 0A              ASL     A                   
AAD2: C9 3C           CMP     #$3C                
AAD4: 90 02           BCC     $AAD8               ; {}
AAD6: A9 3C           LDA     #$3C                
AAD8: 8D 2A 03        STA     $032A               
AADB: 4C 3C AA        JMP     $AA3C               ; {}
AADE: AD 88 03        LDA     $0388               
AAE1: 29 FE           AND     #$FE                
AAE3: D0 12           BNE     $AAF7               ; {}
AAE5: B9 00 A1        LDA     $A100,Y             ; {}
AAE8: 8D 0C 40        STA     $400C               ; {hard.S_NOI_A}
AAEB: B9 01 A1        LDA     $A101,Y             ; {}
AAEE: 8D 0E 40        STA     $400E               ; {hard.S_NOI_C}
AAF1: B9 02 A1        LDA     $A102,Y             ; {}
AAF4: 8D 0F 40        STA     $400F               ; {hard.S_NOI_D}
AAF7: 4C A8 AA        JMP     $AAA8               ; {}
AAFA: 07 ; ????
AAFB: F0 00           BEQ     $AAFD               ; {}
AAFD: 00              BRK                         
AAFE: 06 AE           ASL     $AE                 
AB00: 06 4E           ASL     $4E                 
AB02: 05 F3           ORA     $F3                 
AB04: 05 9E           ORA     $9E                 
AB06: 05 4D           ORA     $4D                 
AB08: 05 01           ORA     $01                 
AB0A: 04 ; ????
AB0B: B9 04 75        LDA     $7504,Y             
AB0E: 04 ; ????
AB0F: 35 03           AND     $03,X               
AB11: F8              SED                         
AB12: 03 ; ????
AB13: BF ; ????
AB14: 03 ; ????
AB15: 89 ; ????
AB16: 03 ; ????
AB17: 57 ; ????
AB18: 03 ; ????
AB19: 27 ; ????
AB1A: 02 ; ????
AB1B: F9 02 CF        SBC     $CF02,Y             
AB1E: 02 ; ????
AB1F: A6 02           LDX     $02                 
AB21: 80 ; ????
AB22: 02 ; ????
AB23: 5C ; ????
AB24: 02 ; ????
AB25: 3A ; ????
AB26: 02 ; ????
AB27: 1A ; ????
AB28: 01 FC           ORA     ($FC,X)             
AB2A: 01 DF           ORA     ($DF,X)             
AB2C: 01 C4           ORA     ($C4,X)             
AB2E: 01 AB           ORA     ($AB,X)             
AB30: 01 93           ORA     ($93,X)             
AB32: 01 7C           ORA     ($7C,X)             
AB34: 01 67           ORA     ($67,X)             
AB36: 01 52           ORA     ($52,X)             
AB38: 01 3F           ORA     ($3F,X)             
AB3A: 01 2D           ORA     ($2D,X)             
AB3C: 01 1C           ORA     ($1C,X)             
AB3E: 01 0C           ORA     ($0C,X)             
AB40: 00              BRK                         
AB41: FD 00 EE        SBC     $EE00,X             
AB44: 00              BRK                         
AB45: E1 00           SBC     ($00,X)             ; {ram.GP_00}
AB47: D4 ; ????
AB48: 00              BRK                         
AB49: C8              INY                         
AB4A: 00              BRK                         
AB4B: BD 00 B2        LDA     $B200,X             ; {}
AB4E: 00              BRK                         
AB4F: A8              TAY                         
AB50: 00              BRK                         
AB51: 9F ; ????
AB52: 00              BRK                         
AB53: 96 00           STX     $00,Y               ; {ram.GP_00}
AB55: 8D 00 85        STA     $8500               ; {}
AB58: 00              BRK                         
AB59: 7E 00 76        ROR     $7600,X             
AB5C: 00              BRK                         
AB5D: 70 00           BVS     $AB5F               ; {}
AB5F: 69 00           ADC     #$00                
AB61: 63 ; ????
AB62: 00              BRK                         
AB63: 5E 00 58        LSR     $5800,X             
AB66: 00              BRK                         
AB67: 53 ; ????
AB68: 00              BRK                         
AB69: 4F ; ????
AB6A: 00              BRK                         
AB6B: 4A              LSR     A                   
AB6C: 00              BRK                         
AB6D: 46 00           LSR     $00                 ; {ram.GP_00}
AB6F: 42 ; ????
AB70: 00              BRK                         
AB71: 3E 00 3A        ROL     $3A00,X             
AB74: 00              BRK                         
AB75: 37 ; ????
AB76: 00              BRK                         
AB77: 34 ; ????
AB78: 00              BRK                         
AB79: 31 00           AND     ($00),Y             ; {ram.GP_00}
AB7B: 2E 00 2B        ROL     $2B00               
AB7E: 00              BRK                         
AB7F: 29 00           AND     #$00                
AB81: 27 ; ????
AB82: 00              BRK                         
AB83: 24 00           BIT     $00                 ; {ram.GP_00}
AB85: 22 ; ????
AB86: 03 ; ????
AB87: 06 0C           ASL     $0C                 
AB89: 18              CLC                         
AB8A: 30 12           BMI     $AB9E               ; {}
AB8C: 24 09           BIT     $09                 
AB8E: 08              PHP                         
AB8F: 04 ; ????
AB90: 01 10           ORA     ($10,X)             
AB92: 04 ; ????
AB93: 08              PHP                         
AB94: 10 20           BPL     $ABB6               ; {}
AB96: 40              RTI                         
AB97: 18              CLC                         
AB98: 30 0C           BMI     $ABA6               ; {}
AB9A: 0B ; ????
AB9B: 05 02           ORA     $02                 
AB9D: 01 06           ORA     ($06,X)             
AB9F: 0C ; ????
ABA0: 18              CLC                         
ABA1: 30 60           BMI     $AC03               ; {}
ABA3: 24 48           BIT     $48                 
ABA5: 12 ; ????
ABA6: 10 08           BPL     $ABB0               ; {}
ABA8: 03 ; ????
ABA9: 10 02           BPL     $ABAD               ; {}
ABAB: 41 27           EOR     ($27,X)             
ABAD: 00              BRK                         
ABAE: 1A ; ????
ABAF: 34 ; ????
ABB0: 0D 8F 82        ORA     $828F               ; {}
ABB3: 68              PLA                         
ABB4: 75 4E           ADC     $4E,X               
ABB6: 5B ; ????
ABB7: 3C ; ????
ABB8: AC 30 AC        LDY     $AC30               ; {}
ABBB: 27 ; ????
ABBC: AC 2A AC        LDY     $AC2A               ; {}
ABBF: D3 ; ????
ABC0: A4 FB           LDY     $FB                 
ABC2: A4 B2           LDY     $B2                 
ABC4: A5 5E           LDA     $5E                 
ABC6: A5 04           LDA     $04                 
ABC8: A4 04           LDY     $04                 
ABCA: A4 04           LDY     $04                 
ABCC: A4 04           LDY     $04                 
ABCE: A4 DF           LDY     $DF                 
ABD0: A4 07           LDY     $07                 
ABD2: A5 BE           LDA     $BE                 
ABD4: A5 87           LDA     $87                 
ABD6: A5 39           LDA     $39                 
ABD8: AC 2D AC        LDY     $AC2D               ; {}
ABDB: 36 AC           ROL     $AC,X               
ABDD: 2D AC 33        AND     $33AC               
ABE0: AC 36 AC        LDY     $AC36               ; {}
ABE3: 36 AC           ROL     $AC,X               
ABE5: 36 AC           ROL     $AC,X               
ABE7: AD 4F 03        LDA     $034F               
ABEA: A2 AB           LDX     #$AB                
ABEC: D0 05           BNE     $ABF3               ; {}
ABEE: AD 85 03        LDA     $0385               
ABF1: A2 A6           LDX     #$A6                
ABF3: 20 D7 A3        JSR     $A3D7               ; {}
ABF6: 20 0D AC        JSR     $AC0D               ; {}
ABF9: 6C EB 00        JMP     ($00EB)             
ABFC: AD 8D 03        LDA     $038D               
ABFF: F0 0B           BEQ     $AC0C               ; {}
AC01: 4C AF A9        JMP     $A9AF               ; {}
AC04: AD 8D 03        LDA     $038D               
AC07: 09 F0           ORA     #$F0                
AC09: 8D 8D 03        STA     $038D               
AC0C: 60              RTS                         
AC0D: A9 FF           LDA     #$FF                
AC0F: 8D 50 03        STA     $0350               
AC12: A5 E8           LDA     $E8                 
AC14: F0 06           BEQ     $AC1C               ; {}
AC16: EE 50 03        INC     $0350               
AC19: 0A              ASL     A                   
AC1A: 90 FA           BCC     $AC16               ; {}
AC1C: 60              RTS                         
AC1D: AD 50 03        LDA     $0350               
AC20: 18              CLC                         
AC21: 69 08           ADC     #$08                
AC23: 8D 50 03        STA     $0350               
AC26: 60              RTS                         
AC27: 4C 3F AC        JMP     $AC3F               ; {}
AC2A: 4C 4C AC        JMP     $AC4C               ; {}
AC2D: 4C 5E AC        JMP     $AC5E               ; {}
AC30: 4C 52 AC        JMP     $AC52               ; {}
AC33: 4C 58 AC        JMP     $AC58               ; {}
AC36: 4C 3F AC        JMP     $AC3F               ; {}
AC39: 4C 52 AC        JMP     $AC52               ; {}
AC3C: 4C 52 AC        JMP     $AC52               ; {}
AC3F: A9 B4           LDA     #$B4                
AC41: AA              TAX                         
AC42: A8              TAY                         
AC43: 20 CF A8        JSR     $A8CF               ; {}
AC46: 20 93 A8        JSR     $A893               ; {}
AC49: 4C AF A9        JMP     $A9AF               ; {}
AC4C: A2 F6           LDX     #$F6                
AC4E: A0 F8           LDY     #$F8                
AC50: D0 F1           BNE     $AC43               ; {}
AC52: A2 F5           LDX     #$F5                
AC54: A0 F6           LDY     #$F6                
AC56: D0 EB           BNE     $AC43               ; {}
AC58: A2 B3           LDX     #$B3                
AC5A: A0 B1           LDY     #$B1                
AC5C: D0 E5           BNE     $AC43               ; {}
AC5E: A2 93           LDX     #$93                
AC60: A0 96           LDY     #$96                
AC62: D0 DF           BNE     $AC43               ; {}
AC64: 6A              ROR     A                   
AC65: AC 73 AC        LDY     $AC73               ; {}
AC68: 7E AC 03        ROR     $03AC,X             
AC6B: 05 07           ORA     $07                 
AC6D: 08              PHP                         
AC6E: 07 ; ????
AC6F: 06 05           ASL     $05                 
AC71: 04 ; ????
AC72: FF ; ????
AC73: 01 01           ORA     ($01,X)             
AC75: 02 ; ????
AC76: 02 ; ????
AC77: 03 ; ????
AC78: 03 ; ????
AC79: 04 ; ????
AC7A: 04 ; ????
AC7B: 05 05           ORA     $05                 
AC7D: FF ; ????
AC7E: 02 ; ????
AC7F: 04 ; ????
AC80: 05 06           ORA     $06                 
AC82: 07 ; ????
AC83: 08              PHP                         
AC84: 07 ; ????
AC85: 06 05           ASL     $05                 
AC87: FF ; ????
AC88: 18              CLC                         
AC89: FF ; ????
AC8A: F0 01           BEQ     $AC8D               ; {}
AC8C: 02 ; ????
AC8D: 7C ; ????
AC8E: AD 70 AD        LDA     $AD70               ; {}
AC91: 94 AD           STY     $AD,X               
AC93: 00              BRK                         
AC94: 00              BRK                         
AC95: 0C ; ????
AC96: FF ; ????
AC97: 00              BRK                         
AC98: 02 ; ????
AC99: 03 ; ????
AC9A: 10 B2           BPL     $AC4E               ; {}
AC9C: 70 B1           BVS     $AC4F               ; {}
AC9E: 8B ; ????
AC9F: B2 ; ????
ACA0: 02 ; ????
ACA1: B3 ; ????
ACA2: 18              CLC                         
ACA3: FF ; ????
ACA4: F0 00           BEQ     $ACA6               ; {}
ACA6: 00              BRK                         
ACA7: E7 ; ????
ACA8: B4 E9           LDY     $E9,X               
ACAA: B4 04           LDY     $04,X               
ACAC: B5 1C           LDA     $1C,X               
ACAE: B5 0C           LDA     $0C,X               
ACB0: FF ; ????
ACB1: 0A              ASL     A                   
ACB2: 00              BRK                         
ACB3: 00              BRK                         
ACB4: 09 B3           ORA     #$B3                
ACB6: 0B ; ????
ACB7: B3 ; ????
ACB8: 72 ; ????
ACB9: B3 ; ????
ACBA: 79 B3 18        ADC     $18B3,Y             
ACBD: FF ; ????
ACBE: 00              BRK                         
ACBF: 03 ; ????
ACC0: 01 E2           ORA     ($E2,X)             
ACC2: B3 ; ????
ACC3: 5E B4 83        LSR     $83B4,X             ; {}
ACC6: B3 ; ????
ACC7: DC ; ????
ACC8: B4 18           LDY     $18,X               
ACCA: FF ; ????
ACCB: 00              BRK                         
ACCC: 02 ; ????
ACCD: 02 ; ????
ACCE: 24 AD           BIT     $AD                 
ACD0: 3E AD 57        ROL     $57AD,X             
ACD3: AD 6B AD        LDA     $AD6B               ; {}
ACD6: 18              CLC                         
ACD7: 00              BRK                         
ACD8: F0 01           BEQ     $ACDB               ; {}
ACDA: 01 98           ORA     ($98,X)             
ACDC: B7 ; ????
ACDD: A0 B8           LDY     #$B8                
ACDF: CA              DEX                         
ACE0: B9 D5 BA        LDA     $BAD5,Y             ; {}
ACE3: 18              CLC                         
ACE4: 00              BRK                         
ACE5: F0 03           BEQ     $ACEA               ; {}
ACE7: 03 ; ????
ACE8: 23 ; ????
ACE9: B5 21           LDA     $21,X               
ACEB: B6 F0           LDX     $F0,Y               
ACED: B6 7E           LDX     $7E,Y               
ACEF: B7 ; ????
ACF0: 18              CLC                         
ACF1: 00              BRK                         
ACF2: 00              BRK                         
ACF3: 01 01           ORA     ($01,X)             
ACF5: C7 ; ????
ACF6: AD D8 AD        LDA     $ADD8               ; {}
ACF9: E8              INX                         
ACFA: AD 00 00        LDA     $0000               ; {ram.GP_00}
ACFD: 18              CLC                         
ACFE: 00              BRK                         
ACFF: F0 01           BEQ     $AD02               ; {}
AD01: 01 AA           ORA     ($AA,X)             
AD03: AD BC AD        LDA     $ADBC               ; {}
AD06: B6 AD           LDX     $AD,Y               
AD08: 00              BRK                         
AD09: 00              BRK                         
AD0A: 18              CLC                         
AD0B: FF ; ????
AD0C: 00              BRK                         
AD0D: 02 ; ????
AD0E: 03 ; ????
AD0F: 7F ; ????
AD10: AE FB AD        LDX     $ADFB               ; {}
AD13: 12 ; ????
AD14: AF ; ????
AD15: 80 ; ????
AD16: AF ; ????
AD17: 00              BRK                         
AD18: FF ; ????
AD19: F0 03           BEQ     $AD1E               ; {}
AD1B: 03 ; ????
AD1C: 6E B0 9C        ROR     $9CB0               ; {}
AD1F: AF ; ????
AD20: E3 ; ????
AD21: B0 58           BCS     $AD7B               ; {}
AD23: B1 B9           LDA     ($B9),Y             
AD25: 52 ; ????
AD26: 02 ; ????
AD27: 52 ; ????
AD28: 5C ; ????
AD29: 02 ; ????
AD2A: 52 ; ????
AD2B: 5C ; ????
AD2C: 02 ; ????
AD2D: 64 ; ????
AD2E: B2 ; ????
AD2F: 5C ; ????
AD30: B9 5C 02        LDA     $025C,Y             
AD33: 5C ; ????
AD34: 64 ; ????
AD35: 02 ; ????
AD36: 5C ; ????
AD37: 6A              ROR     A                   
AD38: 02 ; ????
AD39: 02 ; ????
AD3A: 6A              ROR     A                   
AD3B: 02 ; ????
AD3C: 02 ; ????
AD3D: 00              BRK                         
AD3E: B9 54 02        LDA     $0254,Y             
AD41: 54 ; ????
AD42: 5E 02 54        LSR     $5402,X             
AD45: 5E 02 66        LSR     $6602,X             
AD48: B2 ; ????
AD49: 5E B9 5E        LSR     $5EB9,X             
AD4C: 02 ; ????
AD4D: 5E 66 02        LSR     $0266,X             
AD50: 5E 6C 02        LSR     $026C,X             
AD53: 02 ; ????
AD54: 6C 02 02        JMP     ($0202)             
AD57: B2 ; ????
AD58: 02 ; ????
AD59: C2 ; ????
AD5A: B2 ; ????
AD5B: 46 B9           LSR     $B9                 
AD5D: 5E 02 5E        LSR     $5E02,X             
AD60: B1 02           LDA     ($02),Y             
AD62: B0 5E           BCS     $ADC2               ; {}
AD64: 5E B9 5E        LSR     $5EB9,X             
AD67: 02 ; ????
AD68: 5E FF 00        LSR     $00FF,X             
AD6B: B2 ; ????
AD6C: 01 D0           ORA     ($D0,X)             
AD6E: 04 ; ????
AD6F: FF ; ????
AD70: D0 B0           BNE     $AD22               ; {}
AD72: 46 48           LSR     $48                 
AD74: 46 48           LSR     $48                 
AD76: 4C 4E 4C        JMP     $4C4E               
AD79: 4E FF 00        LSR     $00FF               
AD7C: BA              TSX                         
AD7D: 02 ; ????
AD7E: C2 ; ????
AD7F: B6 24           LDX     $24,Y               
AD81: B1 20           LDA     ($20),Y             
AD83: 24 B3           BIT     $B3                 
AD85: 26 B2           ROL     $B2                 
AD87: 2A              ROL     A                   
AD88: 26 B4           ROL     $B4                 
AD8A: 24 B3           BIT     $B3                 
AD8C: 1A ; ????
AD8D: B2 ; ????
AD8E: 1C ; ????
AD8F: 14 ; ????
AD90: B4 16           LDY     $16,X               
AD92: 22 ; ????
AD93: FF ; ????
AD94: C2 ; ????
AD95: B6 2E           LDX     $2E,Y               
AD97: B1 2A           LDA     ($2A),Y             
AD99: 2E B3 30        ROL     $30B3               
AD9C: B2 ; ????
AD9D: 34 ; ????
AD9E: 30 B4           BMI     $AD54               ; {}
ADA0: 2E B3 24        ROL     $24B3               
ADA3: B2 ; ????
ADA4: 26 1E           ROL     $1E                 
ADA6: B4 20           LDY     $20,X               
ADA8: 2C FF B9        BIT     $B9FF               ; {}
ADAB: 58              CLI                         
ADAC: 58              CLI                         
ADAD: 58              CLI                         
ADAE: 60              RTS                         
ADAF: 02 ; ????
ADB0: 4E B2 52        LSR     $52B2               
ADB3: B6 4A           LDX     $4A,Y               
ADB5: 00              BRK                         
ADB6: B2 ; ????
ADB7: 28              PLP                         
ADB8: 24 1A           BIT     $1A                 
ADBA: B4 2C           LDY     $2C,X               
ADBC: B9 4E 4E        LDA     $4E4E,Y             
ADBF: 4E 58 02        LSR     $0258               
ADC2: 48              PHA                         
ADC3: B2 ; ????
ADC4: 40              RTI                         
ADC5: B4 3A           LDY     $3A,X               
ADC7: B2 ; ????
ADC8: 54 ; ????
ADC9: B9 5E 02        LDA     $025E,Y             
ADCC: 5E B2 5E        LSR     $5EB2,X             
ADCF: 02 ; ????
ADD0: 36 38           ROL     $38,X               
ADD2: B1 36           LDA     ($36),Y             
ADD4: 02 ; ????
ADD5: B2 ; ????
ADD6: 16 00           ASL     $00,X               ; {ram.GP_00}
ADD8: B2 ; ????
ADD9: 52 ; ????
ADDA: B9 5C 02        LDA     $025C,Y             
ADDD: 5C ; ????
ADDE: B2 ; ????
ADDF: 5C ; ????
ADE0: 02 ; ????
ADE1: 2E 30 B1        ROL     $B130               ; {}
ADE4: 2E 02 B2        ROL     $B202               ; {}
ADE7: 24 C2           BIT     $C2                 
ADE9: B1 46           LDA     ($46),Y             
ADEB: B0 5E           BCS     $AE4B               ; {}
ADED: 5E B9 5E        LSR     $5EB9,X             
ADF0: 02 ; ????
ADF1: 5E FF B2        LSR     $B2FF,X             ; {}
ADF4: 24 30           BIT     $30                 
ADF6: B1 2E           LDA     ($2E),Y             
ADF8: 02 ; ????
ADF9: B2 ; ????
ADFA: 16 B4           ASL     $B4,X               
ADFC: 02 ; ????
ADFD: 02 ; ????
ADFE: C2 ; ????
ADFF: B9 2C 2C        LDA     $2C2C,Y             
AE02: 2C 34 02        BIT     $0234               
AE05: 22 ; ????
AE06: B2 ; ????
AE07: 2C B9 2C        BIT     $2CB9               
AE0A: 34 ; ????
AE0B: 3A ; ????
AE0C: B3 ; ????
AE0D: 42 ; ????
AE0E: 3E B9 3A        ROL     $3AB9,X             
AE11: 3A ; ????
AE12: 3A ; ????
AE13: 44 ; ????
AE14: 02 ; ????
AE15: 34 ; ????
AE16: B2 ; ????
AE17: 3A ; ????
AE18: B9 3A 44        LDA     $443A,Y             
AE1B: 34 ; ????
AE1C: B3 ; ????
AE1D: 48              PHA                         
AE1E: 4E FF B9        LSR     $B9FF               ; {}
AE21: 44 ; ????
AE22: 02 ; ????
AE23: 44 ; ????
AE24: B2 ; ????
AE25: 48              PHA                         
AE26: 4C 4E B6        JMP     $B64E               ; {}
AE29: 52 ; ????
AE2A: B9 52 4A        LDA     $4A52,Y             
AE2D: 52 ; ????
AE2E: B6 4C           LDX     $4C,Y               
AE30: B2 ; ????
AE31: 02 ; ????
AE32: B9 44 02        LDA     $0244,Y             
AE35: 44 ; ????
AE36: B2 ; ????
AE37: 48              PHA                         
AE38: 4C 4E B6        JMP     $B64E               ; {}
AE3B: 52 ; ????
AE3C: B9 52 4A        LDA     $4A52,Y             
AE3F: 52 ; ????
AE40: B6 4C           LDX     $4C,Y               
AE42: B9 44 4C        LDA     $4C44,Y             
AE45: 4E B6 52        LSR     $52B6               
AE48: B7 ; ????
AE49: 4E B0 4C        LSR     $4CB0               
AE4C: B3 ; ????
AE4D: 4E B2 44        LSR     $44B2               
AE50: 48              PHA                         
AE51: 4C B7 4E        JMP     $4EB7               
AE54: B0 4C           BCS     $AEA2               ; {}
AE56: B2 ; ????
AE57: 48              PHA                         
AE58: 44 ; ????
AE59: 44 ; ????
AE5A: 42 ; ????
AE5B: 3E 42 B9        ROL     $B942,X             ; {}
AE5E: 44 ; ????
AE5F: 3A ; ????
AE60: 44 ; ????
AE61: 4C 44 4C        JMP     $4C44               
AE64: 52 ; ????
AE65: 02 ; ????
AE66: 02 ; ????
AE67: 4C 02 44        JMP     $4402               
AE6A: B2 ; ????
AE6B: 4E B7 4C        LSR     $4CB7               
AE6E: B0 48           BCS     $AEB8               ; {}
AE70: B2 ; ????
AE71: 44 ; ????
AE72: 48              PHA                         
AE73: B4 44           LDY     $44,X               
AE75: 44 ; ????
AE76: 44 ; ????
AE77: B3 ; ????
AE78: 36 B9           ROL     $B9,X               
AE7A: 3A ; ????
AE7B: 36 3A           ROL     $3A,X               
AE7D: B2 ; ????
AE7E: 3E E0 B0        ROL     $B0E0,X             ; {}
AE81: 02 ; ????
AE82: FF ; ????
AE83: C2 ; ????
AE84: B9 22 22        LDA     $2222,Y             
AE87: 22 ; ????
AE88: 2C 02 1C        BIT     $1C02               
AE8B: B2 ; ????
AE8C: 22 ; ????
AE8D: B9 22 2C        LDA     $2C22,Y             
AE90: 34 ; ????
AE91: B2 ; ????
AE92: 38              SEC                         
AE93: 32 ; ????
AE94: 38              SEC                         
AE95: 32 ; ????
AE96: B9 34 34        LDA     $3434,Y             
AE99: 34 ; ????
AE9A: 3A ; ????
AE9B: 02 ; ????
AE9C: 2C B2 34        BIT     $34B2               
AE9F: B9 34 3A        LDA     $3A34,Y             
AEA2: 44 ; ????
AEA3: B2 ; ????
AEA4: 40              RTI                         
AEA5: B9 28 30        LDA     $3028,Y             
AEA8: 36 3E           ROL     $3E,X               
AEAA: 36 2C           ROL     $2C,X               
AEAC: 26 2C           ROL     $2C                 
AEAE: 36 FF           ROL     $FF,X               
AEB0: C2 ; ????
AEB1: B4 02           LDY     $02,X               
AEB3: B2 ; ????
AEB4: 44 ; ????
AEB5: B7 ; ????
AEB6: 32 ; ????
AEB7: B0 44           BCS     $AEFD               ; {}
AEB9: B9 48 40        LDA     $4048,Y             
AEBC: 48              PHA                         
AEBD: 4A              LSR     A                   
AEBE: 44 ; ????
AEBF: 4A              LSR     A                   
AEC0: 3A ; ????
AEC1: 3A ; ????
AEC2: 3E B7 42        ROL     $42B7,X             
AEC5: B0 3E           BCS     $AF05               ; {}
AEC7: B2 ; ????
AEC8: 3A ; ????
AEC9: 02 ; ????
AECA: FF ; ????
AECB: B3 ; ????
AECC: 48              PHA                         
AECD: B2 ; ????
AECE: 4C 48 B3        JMP     $B348               ; {}
AED1: 44 ; ????
AED2: 36 B2           ROL     $B2,X               
AED4: 44 ; ????
AED5: B7 ; ????
AED6: 48              PHA                         
AED7: B0 44           BCS     $AF1D               ; {}
AED9: B2 ; ????
AEDA: 3E 3E 3E        ROL     $3E3E,X             
AEDD: 3A ; ????
AEDE: 36 3A           ROL     $3A,X               
AEE0: B3 ; ????
AEE1: 3A ; ????
AEE2: 48              PHA                         
AEE3: B2 ; ????
AEE4: 44 ; ????
AEE5: B9 3A 02        LDA     $023A,Y             
AEE8: 36 B2           ROL     $B2,X               
AEEA: 34 ; ????
AEEB: 36 B9           ROL     $B9,X               
AEED: 26 2C           ROL     $2C                 
AEEF: 36 3A           ROL     $3A,X               
AEF1: 36 3A           ROL     $3A,X               
AEF3: B3 ; ????
AEF4: 3E B9 22        ROL     $22B9,X             
AEF7: 2C 30 3A        BIT     $3A30               
AEFA: 44 ; ????
AEFB: 4E B3 4C        LSR     $4CB3               
AEFE: B2 ; ????
AEFF: 36 B9           ROL     $B9,X               
AF01: 34 ; ????
AF02: 36 3A           ROL     $3A,X               
AF04: B2 ; ????
AF05: 3E 42 44        ROL     $4442,X             
AF08: B9 48 44        LDA     $4448,Y             
AF0B: 48              PHA                         
AF0C: 4C 48 4C        JMP     $4C48               
AF0F: B2 ; ????
AF10: 4E 00 D4        LSR     $D400               
AF13: B9 2C 2C        LDA     $2C2C,Y             
AF16: 2C B2 2C        BIT     $2CB2               
AF19: FF ; ????
AF1A: C2 ; ????
AF1B: B9 44 02        LDA     $0244,Y             
AF1E: 44 ; ????
AF1F: B2 ; ????
AF20: 42 ; ????
AF21: 40              RTI                         
AF22: 3E 24 B9        ROL     $B924,X             ; {}
AF25: 24 24           BIT     $24                 
AF27: 24 B2           BIT     $B2                 
AF29: 24 B9           BIT     $B9                 
AF2B: 24 24           BIT     $24                 
AF2D: 24 B2           BIT     $B2                 
AF2F: 2C B9 2C        BIT     $2CB9               
AF32: 2C 2C B2        BIT     $B22C               ; {}
AF35: 2C 02 FF        BIT     $FF02               
AF38: C2 ; ????
AF39: B2 ; ????
AF3A: 28              PLP                         
AF3B: B9 28 02        LDA     $0228,Y             
AF3E: 28              PLP                         
AF3F: FF ; ????
AF40: C2 ; ????
AF41: B2 ; ????
AF42: 26 B9           ROL     $B9                 
AF44: 26 02           ROL     $02                 
AF46: 26 FF           ROL     $FF                 
AF48: C2 ; ????
AF49: 22 ; ????
AF4A: 02 ; ????
AF4B: 22 ; ????
AF4C: FF ; ????
AF4D: C2 ; ????
AF4E: 20 02 20        JSR     $2002               ; {hard.P_STATUS}
AF51: FF ; ????
AF52: C2 ; ????
AF53: 1E 02 1E        ASL     $1E02,X             
AF56: FF ; ????
AF57: C2 ; ????
AF58: 22 ; ????
AF59: 22 ; ????
AF5A: 22 ; ????
AF5B: FF ; ????
AF5C: B2 ; ????
AF5D: 2C 2C 28        BIT     $282C               
AF60: 28              PLP                         
AF61: 26 26           ROL     $26                 
AF63: 22 ; ????
AF64: 22 ; ????
AF65: C2 ; ????
AF66: B2 ; ????
AF67: 36 B9           ROL     $B9,X               
AF69: 36 36           ROL     $36,X               
AF6B: 36 FF           ROL     $FF,X               
AF6D: C2 ; ????
AF6E: B2 ; ????
AF6F: 34 ; ????
AF70: B9 34 34        LDA     $3434,Y             
AF73: 34 ; ????
AF74: FF ; ????
AF75: B2 ; ????
AF76: 30 34           BMI     $AFAC               ; {}
AF78: 36 38           ROL     $38,X               
AF7A: 22 ; ????
AF7B: 22 ; ????
AF7C: C6 B9           DEC     $B9                 
AF7E: 22 ; ????
AF7F: FF ; ????
AF80: D0 B2           BNE     $AF34               ; {}
AF82: 04 ; ????
AF83: 04 ; ????
AF84: 04 ; ????
AF85: B9 04 04        LDA     $0404,Y             
AF88: 04 ; ????
AF89: FF ; ????
AF8A: C8              INY                         
AF8B: B9 04 01        LDA     $0104,Y             
AF8E: 04 ; ????
AF8F: B2 ; ????
AF90: 07 ; ????
AF91: FF ; ????
AF92: E0 B2           CPX     #$B2                
AF94: 04 ; ????
AF95: 04 ; ????
AF96: 07 ; ????
AF97: B9 04 04        LDA     $0404,Y             
AF9A: 04 ; ????
AF9B: FF ; ????
AF9C: C4 B4           CPY     $B4                 
AF9E: 02 ; ????
AF9F: FF ; ????
AFA0: B6 5E           LDX     $5E,Y               
AFA2: B9 5E 5C        LDA     $5C5E,Y             
AFA5: 5A ; ????
AFA6: B4 58           LDY     $58,X               
AFA8: 5A ; ????
AFA9: B3 ; ????
AFAA: 60              RTS                         
AFAB: B5 5E           LDA     $5E,X               
AFAD: B1 5A           LDA     ($5A),Y             
AFAF: B4 5E           LDY     $5E,X               
AFB1: B6 2E           LDX     $2E,Y               
AFB3: B2 ; ????
AFB4: 28              PLP                         
AFB5: B4 2A           LDY     $2A,X               
AFB7: B3 ; ????
AFB8: 30 B5           BMI     $AF6F               ; {}
AFBA: 2E B1 2A        ROL     $2AB1               
AFBD: B6 5E           LDX     $5E,Y               
AFBF: B9 5E 5C        LDA     $5C5E,Y             
AFC2: 5A ; ????
AFC3: B4 58           LDY     $58,X               
AFC5: 5A ; ????
AFC6: B3 ; ????
AFC7: 60              RTS                         
AFC8: B5 5E           LDA     $5E,X               
AFCA: B1 5A           LDA     ($5A),Y             
AFCC: B4 5E           LDY     $5E,X               
AFCE: 46 BB           LSR     $BB                 
AFD0: 3A ; ????
AFD1: 42 ; ????
AFD2: 46 48           LSR     $48                 
AFD4: 50 52           BVC     $B028               ; {}
AFD6: C2 ; ????
AFD7: B6 58           LDX     $58,Y               
AFD9: B2 ; ????
AFDA: 50 B6           BVC     $AF92               ; {}
AFDC: 46 B2           LSR     $B2                 
AFDE: 40              RTI                         
AFDF: B1 42           LDA     ($42),Y             
AFE1: 3A ; ????
AFE2: 42 ; ????
AFE3: 48              PHA                         
AFE4: 52 ; ????
AFE5: 48              PHA                         
AFE6: 52 ; ????
AFE7: 5A ; ????
AFE8: 60              RTS                         
AFE9: 5A ; ????
AFEA: 60              RTS                         
AFEB: 6A              ROR     A                   
AFEC: B2 ; ????
AFED: 72 ; ????
AFEE: 6A              ROR     A                   
AFEF: B4 68           LDY     $68,X               
AFF1: B3 ; ????
AFF2: 50 46           BVC     $B03A               ; {}
AFF4: B1 2E           LDA     ($2E),Y             
AFF6: 30 38           BMI     $B030               ; {}
AFF8: 3A ; ????
AFF9: 42 ; ????
AFFA: 46 48           LSR     $48                 
AFFC: 50 50           BVC     $B04E               ; {}
AFFE: 52 ; ????
AFFF: 5A ; ????
B000: 5E 60 02        LSR     $0260,X             
B003: 02 ; ????
B004: 02 ; ????
B005: FF ; ????
B006: C2 ; ????
B007: B1 58           LDA     ($58),Y             
B009: 02 ; ????
B00A: 58              CLI                         
B00B: 5A ; ????
B00C: 5E 02 58        LSR     $5802,X             
B00F: 02 ; ????
B010: 58              CLI                         
B011: 5A ; ????
B012: 5E 02 58        LSR     $5802,X             
B015: 02 ; ????
B016: 5E 02 5A        LSR     $5A02,X             
B019: 02 ; ????
B01A: 5A ; ????
B01B: 5E 60 02        LSR     $0260,X             
B01E: 5A ; ????
B01F: 02 ; ????
B020: 60              RTS                         
B021: 5E 60 02        LSR     $0260,X             
B024: 6A              ROR     A                   
B025: 02 ; ????
B026: 60              RTS                         
B027: 02 ; ????
B028: FF ; ????
B029: B4 02           LDY     $02,X               
B02B: B6 02           LDX     $02,Y               
B02D: B1 68           LDA     ($68),Y             
B02F: 66 B2           ROR     $B2                 
B031: 62 ; ????
B032: 5E 58 50        LSR     $5058,X             
B035: B1 54           LDA     ($54),Y             
B037: 58              CLI                         
B038: 54 ; ????
B039: 50 B2           BVC     $AFED               ; {}
B03B: 4A              LSR     A                   
B03C: 46 50           LSR     $50                 
B03E: 50 B1           BVC     $AFF1               ; {}
B040: 50 54           BVC     $B096               ; {}
B042: 58              CLI                         
B043: 5A ; ????
B044: B2 ; ????
B045: 5E 02 58        LSR     $5802,X             
B048: B1 68           LDA     ($68),Y             
B04A: 66 B2           ROR     $B2                 
B04C: 62 ; ????
B04D: 5E 58 50        LSR     $5058,X             
B050: B1 54           LDA     ($54),Y             
B052: 58              CLI                         
B053: 54 ; ????
B054: 50 B2           BVC     $B008               ; {}
B056: 4A              LSR     A                   
B057: 46 50           LSR     $50                 
B059: 5A ; ????
B05A: 54 ; ????
B05B: 4E B4 50        LSR     $50B4               
B05E: 02 ; ????
B05F: 02 ; ????
B060: E0 B1           CPX     #$B1                
B062: 38              SEC                         
B063: 02 ; ????
B064: FF ; ????
B065: E0 34           CPX     #$34                
B067: 02 ; ????
B068: FF ; ????
B069: E0 34           CPX     #$34                
B06B: 02 ; ????
B06C: FF ; ????
B06D: 00              BRK                         
B06E: BA              TSX                         
B06F: 02 ; ????
B070: E0 B2           CPX     #$B2                
B072: 02 ; ????
B073: FF ; ????
B074: B6 40           LDX     $40,Y               
B076: B1 3C           LDA     ($3C),Y             
B078: 38              SEC                         
B079: B4 02           LDY     $02,X               
B07B: 02 ; ????
B07C: 02 ; ????
B07D: 40              RTI                         
B07E: 38              SEC                         
B07F: 30 B3           BMI     $B034               ; {}
B081: 2A              ROL     A                   
B082: B5 28           LDA     $28,X               
B084: B1 24           LDA     ($24),Y             
B086: B4 28           LDY     $28,X               
B088: 02 ; ????
B089: BB ; ????
B08A: 2A              ROL     A                   
B08B: 30 34           BMI     $B0C1               ; {}
B08D: 38              SEC                         
B08E: 3E 42 C2        ROL     $C242,X             
B091: B6 46           LDX     $46,Y               
B093: B2 ; ????
B094: 40              RTI                         
B095: B6 38           LDX     $38,Y               
B097: B2 ; ????
B098: 2E B3 3A        ROL     $3AB3               
B09B: 42 ; ????
B09C: 48              PHA                         
B09D: 5A ; ????
B09E: 40              RTI                         
B09F: 46 B4           LSR     $B4                 
B0A1: 02 ; ????
B0A2: 02 ; ????
B0A3: 02 ; ????
B0A4: FF ; ????
B0A5: C2 ; ????
B0A6: B1 38           LDA     ($38),Y             
B0A8: 02 ; ????
B0A9: 38              SEC                         
B0AA: 3C ; ????
B0AB: 40              RTI                         
B0AC: 02 ; ????
B0AD: 38              SEC                         
B0AE: 02 ; ????
B0AF: 38              SEC                         
B0B0: 3C ; ????
B0B1: 40              RTI                         
B0B2: 02 ; ????
B0B3: 38              SEC                         
B0B4: 02 ; ????
B0B5: 40              RTI                         
B0B6: 02 ; ????
B0B7: 3A ; ????
B0B8: 02 ; ????
B0B9: 3A ; ????
B0BA: 3E 42 02        ROL     $0242,X             
B0BD: 3A ; ????
B0BE: 02 ; ????
B0BF: 42 ; ????
B0C0: 3E 42 02        ROL     $0242,X             
B0C3: 48              PHA                         
B0C4: 02 ; ????
B0C5: 42 ; ????
B0C6: 02 ; ????
B0C7: FF ; ????
B0C8: CC B6 08        CPY     $08B6               
B0CB: B2 ; ????
B0CC: 02 ; ????
B0CD: FF ; ????
B0CE: E0 B1           CPX     #$B1                
B0D0: 34 ; ????
B0D1: 02 ; ????
B0D2: FF ; ????
B0D3: D8              CLD                         
B0D4: 30 02           BMI     $B0D8               ; {}
B0D6: FF ; ????
B0D7: C8              INY                         
B0D8: 2E 02 FF        ROL     $FF02               
B0DB: D0 30           BNE     $B10D               ; {}
B0DD: 02 ; ????
B0DE: FF ; ????
B0DF: D0 2E           BNE     $B10F               ; {}
B0E1: 02 ; ????
B0E2: FF ; ????
B0E3: C8              INY                         
B0E4: B1 38           LDA     ($38),Y             
B0E6: 02 ; ????
B0E7: 46 02           LSR     $02                 
B0E9: FF ; ????
B0EA: C4 38           CPY     $38                 
B0EC: 02 ; ????
B0ED: 46 02           LSR     $02                 
B0EF: 38              SEC                         
B0F0: 02 ; ????
B0F1: 46 02           LSR     $02                 
B0F3: 38              SEC                         
B0F4: 02 ; ????
B0F5: 46 02           LSR     $02                 
B0F7: 38              SEC                         
B0F8: 02 ; ????
B0F9: 46 02           LSR     $02                 
B0FB: 3A ; ????
B0FC: 02 ; ????
B0FD: 48              PHA                         
B0FE: 02 ; ????
B0FF: 3A ; ????
B100: 02 ; ????
B101: 48              PHA                         
B102: 02 ; ????
B103: 3A ; ????
B104: 02 ; ????
B105: 48              PHA                         
B106: 02 ; ????
B107: 3A ; ????
B108: 02 ; ????
B109: 48              PHA                         
B10A: 02 ; ????
B10B: FF ; ????
B10C: C6 B5           DEC     $B5                 
B10E: 20 B1 2E        JSR     $2EB1               
B111: B2 ; ????
B112: 38              SEC                         
B113: 2E B0 20        ROL     $20B0               
B116: 02 ; ????
B117: 20 02 B1        JSR     $B102               ; {}
B11A: 02 ; ????
B11B: 2E B2 38        ROL     $38B2               
B11E: 2E B5 22        ROL     $22B5               
B121: B1 30           LDA     ($30),Y             
B123: B2 ; ????
B124: 3A ; ????
B125: 30 B1           BMI     $B0D8               ; {}
B127: 3E 22 02        ROL     $0222,X             
B12A: 22 ; ????
B12B: B2 ; ????
B12C: 3A ; ????
B12D: 30 FF           BMI     $B12E               ; {}
B12F: D8              CLD                         
B130: B0 38           BCS     $B16A               ; {}
B132: B7 ; ????
B133: 02 ; ????
B134: B0 46           BCS     $B17C               ; {}
B136: B7 ; ????
B137: 02 ; ????
B138: FF ; ????
B139: B4 30           LDY     $30,X               
B13B: 30 B6           BMI     $B0F3               ; {}
B13D: 34 ; ????
B13E: 38              SEC                         
B13F: B3 ; ????
B140: 30 C4           BMI     $B106               ; {}
B142: B4 2E           LDY     $2E,X               
B144: FF ; ????
B145: 28              PLP                         
B146: 28              PLP                         
B147: B6 30           LDX     $30,Y               
B149: 2C B3 28        BIT     $28B3               
B14C: C4 B4           CPY     $B4                 
B14E: 26 FF           ROL     $FF                 
B150: 22 ; ????
B151: 22 ; ????
B152: 2A              ROL     A                   
B153: 30 26           BMI     $B17B               ; {}
B155: 22 ; ????
B156: 1E 1C CA        ASL     $CA1C,X             
B159: B2 ; ????
B15A: 04 ; ????
B15B: 01 04           ORA     ($04,X)             
B15D: 04 ; ????
B15E: 04 ; ????
B15F: 04 ; ????
B160: 04 ; ????
B161: 01 FF           ORA     ($FF,X)             
B163: E0 B1           CPX     #$B1                
B165: 04 ; ????
B166: 01 04           ORA     ($04,X)             
B168: 04 ; ????
B169: FF ; ????
B16A: FC ; ????
B16B: B2 ; ????
B16C: 04 ; ????
B16D: 04 ; ????
B16E: 04 ; ????
B16F: FF ; ????
B170: C2 ; ????
B171: B1 76           LDA     ($76),Y             
B173: 6C 02 66        JMP     ($6602)             
B176: 02 ; ????
B177: 6C 02 66        JMP     ($6602)             
B17A: FF ; ????
B17B: B1 44           LDA     ($44),Y             
B17D: 46 48           LSR     $48                 
B17F: 4A              LSR     A                   
B180: 4E 50 52        LSR     $5250               
B183: 54 ; ????
B184: B0 5C           BCS     $B1E2               ; {}
B186: 5E 60 62        LSR     $6260,X             
B189: 64 ; ????
B18A: 66 68           ROR     $68                 
B18C: 6A              ROR     A                   
B18D: 6C 02 02        JMP     ($0202)             
B190: 02 ; ????
B191: B2 ; ????
B192: 44 ; ????
B193: C2 ; ????
B194: B1 4E           LDA     ($4E),Y             
B196: 50 02           BVC     $B19A               ; {}
B198: 54 ; ????
B199: 02 ; ????
B19A: B0 62           BCS     $B1FE               ; {}
B19C: 54 ; ????
B19D: 62 ; ????
B19E: 54 ; ????
B19F: 62 ; ????
B1A0: 54 ; ????
B1A1: 5E 50 5E        LSR     $5E50,X             
B1A4: 50 5E           BVC     $B204               ; {}
B1A6: 50 5E           BVC     $B206               ; {}
B1A8: 50 B3           BVC     $B15D               ; {}
B1AA: 02 ; ????
B1AB: B0 46           BCS     $B1F3               ; {}
B1AD: 38              SEC                         
B1AE: 46 38           LSR     $38                 
B1B0: B2 ; ????
B1B1: 58              CLI                         
B1B2: 54 ; ????
B1B3: B0 4E           BCS     $B203               ; {}
B1B5: 46 4E           LSR     $4E                 
B1B7: 46 4A           LSR     $4A                 
B1B9: 42 ; ????
B1BA: 4A              LSR     A                   
B1BB: 42 ; ????
B1BC: 4A              LSR     A                   
B1BD: 42 ; ????
B1BE: 4A              LSR     A                   
B1BF: 42 ; ????
B1C0: B3 ; ????
B1C1: 02 ; ????
B1C2: FF ; ????
B1C3: B1 58           LDA     ($58),Y             
B1C5: 58              CLI                         
B1C6: 54 ; ????
B1C7: 58              CLI                         
B1C8: 02 ; ????
B1C9: 5C ; ????
B1CA: 02 ; ????
B1CB: 02 ; ????
B1CC: 5E 02 02        LSR     $0202,X             
B1CF: 02 ; ????
B1D0: 54 ; ????
B1D1: 02 ; ????
B1D2: 02 ; ????
B1D3: 02 ; ????
B1D4: C3 ; ????
B1D5: B0 58           BCS     $B22F               ; {}
B1D7: 38              SEC                         
B1D8: FF ; ????
B1D9: C3 ; ????
B1DA: 5E 58 FF        LSR     $FF58,X             
B1DD: C2 ; ????
B1DE: 68              PLA                         
B1DF: 5E FF C4        LSR     $C4FF,X             
B1E2: 66 5E           ROR     $5E                 
B1E4: FF ; ????
B1E5: C4 54           CPY     $54                 
B1E7: 4E FF B1        LSR     $B1FF               ; {}
B1EA: 58              CLI                         
B1EB: 58              CLI                         
B1EC: 54 ; ????
B1ED: 58              CLI                         
B1EE: 02 ; ????
B1EF: 5C ; ????
B1F0: 02 ; ????
B1F1: 02 ; ????
B1F2: 5E 02 02        LSR     $0202,X             
B1F5: 02 ; ????
B1F6: B3 ; ????
B1F7: 66 B6           ROR     $B6                 
B1F9: 5E B2 02        LSR     $02B2,X             
B1FC: B4 54           LDY     $54,X               
B1FE: B1 5E           LDA     ($5E),Y             
B200: 5E 5E 5E        LSR     $5E5E,X             
B203: 02 ; ????
B204: 5E 02 5E        LSR     $5E02,X             
B207: 5E 02 02        LSR     $0202,X             
B20A: 02 ; ????
B20B: 02 ; ????
B20C: 02 ; ????
B20D: 02 ; ????
B20E: 02 ; ????
B20F: 00              BRK                         
B210: C2 ; ????
B211: B1 66           LDA     ($66),Y             
B213: 62 ; ????
B214: 02 ; ????
B215: 54 ; ????
B216: 02 ; ????
B217: 62 ; ????
B218: 02 ; ????
B219: 5E FF B1        LSR     $B1FF,X             ; {}
B21C: 02 ; ????
B21D: 02 ; ????
B21E: 02 ; ????
B21F: 02 ; ????
B220: 02 ; ????
B221: 02 ; ????
B222: 02 ; ????
B223: 02 ; ????
B224: B0 4A           BCS     $B270               ; {}
B226: 02 ; ????
B227: 02 ; ????
B228: 02 ; ????
B229: 54 ; ????
B22A: 02 ; ????
B22B: 02 ; ????
B22C: 02 ; ????
B22D: 62 ; ????
B22E: 02 ; ????
B22F: 02 ; ????
B230: 02 ; ????
B231: B2 ; ????
B232: 24 C2           BIT     $C2                 
B234: B2 ; ????
B235: 02 ; ????
B236: 3C ; ????
B237: 02 ; ????
B238: 3C ; ????
B239: 02 ; ????
B23A: 40              RTI                         
B23B: 02 ; ????
B23C: 44 ; ????
B23D: 02 ; ????
B23E: 46 02           LSR     $02                 
B240: 46 02           LSR     $02                 
B242: 38              SEC                         
B243: 02 ; ????
B244: 38              SEC                         
B245: FF ; ????
B246: B1 46           LDA     ($46),Y             
B248: 46 46           LSR     $46                 
B24A: 46 02           LSR     $02                 
B24C: 4A              LSR     A                   
B24D: 02 ; ????
B24E: 02 ; ????
B24F: 4E 02 02        LSR     $0202               
B252: 02 ; ????
B253: 46 02           LSR     $02                 
B255: 02 ; ????
B256: 02 ; ????
B257: B2 ; ????
B258: 02 ; ????
B259: 58              CLI                         
B25A: 02 ; ????
B25B: 58              CLI                         
B25C: 02 ; ????
B25D: 4E 02 4E        LSR     $4E02               
B260: B1 46           LDA     ($46),Y             
B262: 46 46           LSR     $46                 
B264: 46 02           LSR     $02                 
B266: 4A              LSR     A                   
B267: 02 ; ????
B268: 02 ; ????
B269: 4E 02 02        LSR     $0202               
B26C: 02 ; ????
B26D: 5E 54 4E        LSR     $4E54,X             
B270: 46 C4           LSR     $C4                 
B272: B1 3C           LDA     ($3C),Y             
B274: 40              RTI                         
B275: FF ; ????
B276: C4 46           CPY     $46                 
B278: 4A              LSR     A                   
B279: FF ; ????
B27A: B1 58           LDA     ($58),Y             
B27C: 58              CLI                         
B27D: 58              CLI                         
B27E: 58              CLI                         
B27F: 02 ; ????
B280: 58              CLI                         
B281: 02 ; ????
B282: 58              CLI                         
B283: 58              CLI                         
B284: 02 ; ????
B285: 02 ; ????
B286: 02 ; ????
B287: 02 ; ????
B288: 02 ; ????
B289: 02 ; ????
B28A: 02 ; ????
B28B: B4 2E           LDY     $2E,X               
B28D: 2A              ROL     A                   
B28E: B1 6C           LDA     ($6C),Y             
B290: 70 72           BVS     $B304               ; {}
B292: 74 ; ????
B293: 76 7A           ROR     $7A,X               
B295: 7C ; ????
B296: 7E B0 6C        ROR     $6CB0,X             
B299: 70 72           BVS     $B30D               ; {}
B29B: 6C 76 78        JMP     ($7876)             
B29E: 7A ; ????
B29F: 7C ; ????
B2A0: 84 02           STY     $02                 
B2A2: 02 ; ????
B2A3: 02 ; ????
B2A4: B2 ; ????
B2A5: 24 C2           BIT     $C2                 
B2A7: B2 ; ????
B2A8: 2E 66 1E        ROL     $1E66               
B2AB: 5E 1A 68        LSR     $681A,X             
B2AE: 24 68           BIT     $68                 
B2B0: 20 68 1E        JSR     $1E68               
B2B3: 6C 2A 62        JMP     ($622A)             
B2B6: 24 5C           BIT     $5C                 
B2B8: FF ; ????
B2B9: B1 20           LDA     ($20),Y             
B2BB: 20 1E 20        JSR     $201E               
B2BE: 02 ; ????
B2BF: 24 02           BIT     $02                 
B2C1: 02 ; ????
B2C2: 28              PLP                         
B2C3: 02 ; ????
B2C4: 02 ; ????
B2C5: 02 ; ????
B2C6: 1E 02 02        ASL     $0202,X             
B2C9: 02 ; ????
B2CA: B2 ; ????
B2CB: 20 5E 20        JSR     $205E               
B2CE: 5E 2E 54        LSR     $542E,X             
B2D1: 2E 54 B1        ROL     $B154               ; {}
B2D4: 20 20 1E        JSR     $1E20               
B2D7: 20 02 24        JSR     $2402               
B2DA: 02 ; ????
B2DB: 02 ; ????
B2DC: 28              PLP                         
B2DD: 02 ; ????
B2DE: 02 ; ????
B2DF: 02 ; ????
B2E0: 2A              ROL     A                   
B2E1: 2A              ROL     A                   
B2E2: 2A              ROL     A                   
B2E3: 2A              ROL     A                   
B2E4: C2 ; ????
B2E5: B2 ; ????
B2E6: 20 B1 38        JSR     $38B1               
B2E9: 38              SEC                         
B2EA: FF ; ????
B2EB: C2 ; ????
B2EC: B2 ; ????
B2ED: 1E B1 36        ASL     $36B1,X             
B2F0: 36 FF           ROL     $FF,X               
B2F2: 24 24           BIT     $24                 
B2F4: 24 24           BIT     $24                 
B2F6: 02 ; ????
B2F7: 24 02           BIT     $02                 
B2F9: 24 24           BIT     $24                 
B2FB: 02 ; ????
B2FC: 02 ; ????
B2FD: 02 ; ????
B2FE: 02 ; ????
B2FF: 02 ; ????
B300: 02 ; ????
B301: 02 ; ????
B302: F0 B2           BEQ     $B2B6               ; {}
B304: 01 B1           ORA     ($B1,X)             
B306: 04 ; ????
B307: 04 ; ????
B308: FF ; ????
B309: B8              CLV                         
B30A: 02 ; ????
B30B: C4 B4           CPY     $B4                 
B30D: 02 ; ????
B30E: FF ; ????
B30F: C8              INY                         
B310: B1 3C           LDA     ($3C),Y             
B312: 3E FF C8        ROL     $C8FF,X             
B315: 44 ; ????
B316: 3E FF B4        ROL     $B4FF,X             ; {}
B319: 3C ; ????
B31A: 02 ; ????
B31B: 02 ; ????
B31C: 02 ; ????
B31D: C8              INY                         
B31E: B1 3C           LDA     ($3C),Y             
B320: 3E FF C8        ROL     $C8FF,X             
B323: 44 ; ????
B324: 3E FF B4        ROL     $B4FF,X             ; {}
B327: 3C ; ????
B328: 02 ; ????
B329: 02 ; ????
B32A: 02 ; ????
B32B: B6 30           LDX     $30,Y               
B32D: B0 36           BCS     $B365               ; {}
B32F: 38              SEC                         
B330: 3A ; ????
B331: 3C ; ????
B332: B3 ; ????
B333: 3E B5 38        ROL     $38B5,X             
B336: B0 38           BCS     $B370               ; {}
B338: 3A ; ????
B339: B4 3C           LDY     $3C,X               
B33B: 02 ; ????
B33C: C2 ; ????
B33D: 02 ; ????
B33E: FF ; ????
B33F: B6 30           LDX     $30,Y               
B341: B0 36           BCS     $B379               ; {}
B343: 38              SEC                         
B344: 3A ; ????
B345: 3C ; ????
B346: B3 ; ????
B347: 3E B5 38        ROL     $38B5,X             
B34A: B0 38           BCS     $B384               ; {}
B34C: 3A ; ????
B34D: B4 3C           LDY     $3C,X               
B34F: 02 ; ????
B350: C2 ; ????
B351: 02 ; ????
B352: FF ; ????
B353: C2 ; ????
B354: B4 46           LDY     $46,X               
B356: B5 44           LDA     $44,X               
B358: B0 42           BCS     $B39C               ; {}
B35A: 40              RTI                         
B35B: B3 ; ????
B35C: 3E B4 3C        ROL     $3CB4,X             
B35F: 02 ; ????
B360: FF ; ????
B361: B0 38           BCS     $B39B               ; {}
B363: 3A ; ????
B364: B1 3C           LDA     ($3C),Y             
B366: 3E 02 B5        ROL     $B502,X             ; {}
B369: 3C ; ????
B36A: B0 3A           BCS     $B3A6               ; {}
B36C: 38              SEC                         
B36D: B3 ; ????
B36E: 34 ; ????
B36F: 38              SEC                         
B370: 30 00           BMI     $B372               ; {}
B372: E8              INX                         
B373: B2 ; ????
B374: 2E 3C 2E        ROL     $2E3C               
B377: 3C ; ????
B378: FF ; ????
B379: E0 B3           CPX     #$B3                
B37B: 04 ; ????
B37C: 04 ; ????
B37D: B2 ; ????
B37E: 04 ; ????
B37F: 04 ; ????
B380: B3 ; ????
B381: 04 ; ????
B382: FF ; ????
B383: B6 2A           LDX     $2A,Y               
B385: B9 20 22        LDA     $2220,Y             
B388: 24 B6           BIT     $B6                 
B38A: 26 B9           ROL     $B9                 
B38C: 22 ; ????
B38D: 20 1C B6        JSR     $B61C               ; {}
B390: 18              CLC                         
B391: B9 18 18        LDA     $1818,Y             
B394: 18              CLC                         
B395: 16 02           ASL     $02,X               
B397: 16 16           ASL     $16,X               
B399: 16 16           ASL     $16,X               
B39B: 20 20 20        JSR     $2020               
B39E: 20 02 20        JSR     $2002               ; {hard.P_STATUS}
B3A1: C2 ; ????
B3A2: B2 ; ????
B3A3: 2A              ROL     A                   
B3A4: 2A              ROL     A                   
B3A5: 2A              ROL     A                   
B3A6: 2A              ROL     A                   
B3A7: 26 26           ROL     $26                 
B3A9: 2A              ROL     A                   
B3AA: 26 24           ROL     $24                 
B3AC: 24 24           BIT     $24                 
B3AE: 24 20           BIT     $20                 
B3B0: 20 20 20        JSR     $2020               
B3B3: 1C ; ????
B3B4: 1C ; ????
B3B5: 1C ; ????
B3B6: 1C ; ????
B3B7: 1A ; ????
B3B8: 1A ; ????
B3B9: 1A ; ????
B3BA: 1A ; ????
B3BB: 16 1A           ASL     $1A,X               
B3BD: 1C ; ????
B3BE: 1E 20 20        ASL     $2020,X             
B3C1: B9 20 20        LDA     $2020,Y             
B3C4: 20 20 20        JSR     $2020               
B3C7: 20 FF C4        JSR     $C4FF               
B3CA: B2 ; ????
B3CB: 22 ; ????
B3CC: FF ; ????
B3CD: C4 26           CPY     $26                 
B3CF: FF ; ????
B3D0: C4 2C           CPY     $2C                 
B3D2: FF ; ????
B3D3: C4 2A           CPY     $2A                 
B3D5: FF ; ????
B3D6: C4 30           CPY     $30                 
B3D8: FF ; ????
B3D9: C4 1C           CPY     $1C                 
B3DB: FF ; ????
B3DC: C4 22           CPY     $22                 
B3DE: FF ; ????
B3DF: C4 20           CPY     $20                 
B3E1: FF ; ????
B3E2: C4 B4           CPY     $B4                 
B3E4: 02 ; ????
B3E5: FF ; ????
B3E6: C2 ; ????
B3E7: B9 38 38        LDA     $3838,Y             
B3EA: 38              SEC                         
B3EB: B7 ; ????
B3EC: 42 ; ????
B3ED: B0 32           BCS     $B421               ; {}
B3EF: B2 ; ????
B3F0: 38              SEC                         
B3F1: B9 32 34        LDA     $3432,Y             
B3F4: 38              SEC                         
B3F5: B6 34           LDX     $34,Y               
B3F7: B9 32 34        LDA     $3432,Y             
B3FA: 38              SEC                         
B3FB: B3 ; ????
B3FC: 2A              ROL     A                   
B3FD: 34 ; ????
B3FE: 32 ; ????
B3FF: B2 ; ????
B400: 34 ; ????
B401: 38              SEC                         
B402: B6 24           LDX     $24,Y               
B404: B9 3C 2A        LDA     $2A3C,Y             
B407: 3C ; ????
B408: B6 38           LDX     $38,Y               
B40A: B9 38 2A        LDA     $2A38,Y             
B40D: 38              SEC                         
B40E: B6 34           LDX     $34,Y               
B410: B9 34 2A        LDA     $2A34,Y             
B413: 34 ; ????
B414: B2 ; ????
B415: 3C ; ????
B416: 38              SEC                         
B417: 34 ; ????
B418: 2E FF B2        ROL     $B2FF               ; {}
B41B: 42 ; ????
B41C: B9 30 3A        LDA     $3A30,Y             
B41F: 42 ; ????
B420: B2 ; ????
B421: 50 B7           BVC     $B3DA               ; {}
B423: 4C B0 48        JMP     $48B0               
B426: B2 ; ????
B427: 3A ; ????
B428: B9 3A 38        LDA     $383A,Y             
B42B: 36 B3           ROL     $B3,X               
B42D: 34 ; ????
B42E: B9 3A 3E        LDA     $3E3A,Y             
B431: 42 ; ????
B432: 42 ; ????
B433: 44 ; ????
B434: 48              PHA                         
B435: B2 ; ????
B436: 3A ; ????
B437: B9 34 3A        LDA     $3A34,Y             
B43A: 44 ; ????
B43B: B5 38           LDA     $38,X               
B43D: B1 44           LDA     ($44),Y             
B43F: B9 42 3E        LDA     $3E42,Y             
B442: 3A ; ????
B443: 38              SEC                         
B444: 34 ; ????
B445: 32 ; ????
B446: B3 ; ????
B447: 26 B2           ROL     $B2                 
B449: 34 ; ????
B44A: B7 ; ????
B44B: 30 B0           BMI     $B3FD               ; {}
B44D: 26 B2           ROL     $B2                 
B44F: 38              SEC                         
B450: B9 38 38        LDA     $3838,Y             
B453: 3E B3 3C        ROL     $3CB3,X             
B456: B3 ; ????
B457: 3E 30 B2        ROL     $B230,X             ; {}
B45A: 34 ; ????
B45B: 28              PLP                         
B45C: 24 28           BIT     $28                 
B45E: C2 ; ????
B45F: B9 42 42        LDA     $4242,Y             
B462: 42 ; ????
B463: B7 ; ????
B464: 4A              LSR     A                   
B465: B0 38           BCS     $B49F               ; {}
B467: B3 ; ????
B468: 42 ; ????
B469: FF ; ????
B46A: B9 42 42        LDA     $4242,Y             
B46D: 42 ; ????
B46E: B7 ; ????
B46F: 48              PHA                         
B470: B0 38           BCS     $B4AA               ; {}
B472: B3 ; ????
B473: 42 ; ????
B474: B2 ; ????
B475: 42 ; ????
B476: 36 40           ROL     $40,X               
B478: 34 ; ????
B479: C2 ; ????
B47A: B9 42 42        LDA     $4242,Y             
B47D: 42 ; ????
B47E: B7 ; ????
B47F: 4A              LSR     A                   
B480: B0 38           BCS     $B4BA               ; {}
B482: B3 ; ????
B483: 42 ; ????
B484: B9 42 42        LDA     $4242,Y             
B487: 42 ; ????
B488: B7 ; ????
B489: 4A              LSR     A                   
B48A: B0 38           BCS     $B4C4               ; {}
B48C: B3 ; ????
B48D: 42 ; ????
B48E: B2 ; ????
B48F: 4C 4A 46        JMP     $464A               
B492: 42 ; ????
B493: B9 42 42        LDA     $4242,Y             
B496: 42 ; ????
B497: B7 ; ????
B498: 4A              LSR     A                   
B499: B0 38           BCS     $B4D3               ; {}
B49B: B3 ; ????
B49C: 42 ; ????
B49D: B9 42 42        LDA     $4242,Y             
B4A0: 42 ; ????
B4A1: B7 ; ????
B4A2: 4A              LSR     A                   
B4A3: B0 38           BCS     $B4DD               ; {}
B4A5: B3 ; ????
B4A6: 42 ; ????
B4A7: B9 42 42        LDA     $4242,Y             
B4AA: 42 ; ????
B4AB: B7 ; ????
B4AC: 4A              LSR     A                   
B4AD: B0 38           BCS     $B4E7               ; {}
B4AF: B3 ; ????
B4B0: 42 ; ????
B4B1: B2 ; ????
B4B2: 46 42           LSR     $42                 
B4B4: 40              RTI                         
B4B5: 3C ; ????
B4B6: 42 ; ????
B4B7: 40              RTI                         
B4B8: 3C ; ????
B4B9: 40              RTI                         
B4BA: FF ; ????
B4BB: B6 48           LDX     $48,Y               
B4BD: B9 3A 42        LDA     $423A,Y             
B4C0: 44 ; ????
B4C1: B4 46           LDY     $46,X               
B4C3: B6 4C           LDX     $4C,Y               
B4C5: B9 3A 44        LDA     $443A,Y             
B4C8: 4C B4 4A        JMP     $4AB4               
B4CB: B6 50           LDX     $50,Y               
B4CD: B7 ; ????
B4CE: 48              PHA                         
B4CF: B0 3E           BCS     $B50F               ; {}
B4D1: B4 42           LDY     $42,X               
B4D3: B3 ; ????
B4D4: 48              PHA                         
B4D5: 42 ; ????
B4D6: B2 ; ????
B4D7: 40              RTI                         
B4D8: 38              SEC                         
B4D9: 34 ; ????
B4DA: 2E 00 E0        ROL     $E000               
B4DD: B2 ; ????
B4DE: 04 ; ????
B4DF: B9 04 04        LDA     $0404,Y             
B4E2: 04 ; ????
B4E3: B2 ; ????
B4E4: 04 ; ????
B4E5: 04 ; ????
B4E6: FF ; ????
B4E7: B8              CLV                         
B4E8: 02 ; ????
B4E9: F0 B0           BEQ     $B49B               ; {}
B4EB: 0C ; ????
B4EC: 12 ; ????
B4ED: 0C ; ????
B4EE: 12 ; ????
B4EF: 18              CLC                         
B4F0: 12 ; ????
B4F1: 18              CLC                         
B4F2: 12 ; ????
B4F3: 1E 18 1E        ASL     $1E18,X             
B4F6: 18              CLC                         
B4F7: 1C ; ????
B4F8: 16 1C           ASL     $1C,X               
B4FA: 16 10           ASL     $10,X               
B4FC: 16 10           ASL     $10,X               
B4FE: 16 0A           ASL     $0A,X               
B500: 10 0A           BPL     $B50C               ; {}
B502: 10 FF           BPL     $B503               ; {}
B504: B3 ; ????
B505: 24 2A           BIT     $2A                 
B507: 28              PLP                         
B508: 26 B2           ROL     $B2                 
B50A: 24 30           BIT     $30                 
B50C: 3A ; ????
B50D: 46 22           LSR     $22                 
B50F: 2E 38 44        ROL     $4438               
B512: B3 ; ????
B513: 2E 3A 38        ROL     $383A               
B516: 2C 2A 36        BIT     $362A               
B519: 34 ; ????
B51A: 28              PLP                         
B51B: 00              BRK                         
B51C: F0 B1           BEQ     $B4CF               ; {}
B51E: 04 ; ????
B51F: 04 ; ????
B520: B2 ; ????
B521: 07 ; ????
B522: FF ; ????
B523: B9 7C 72        LDA     $727C,Y             
B526: 7C ; ????
B527: 84 7C           STY     $7C                 
B529: 84 8A           STY     $8A                 
B52B: 02 ; ????
B52C: 02 ; ????
B52D: 84 02           STY     $02                 
B52F: 7C ; ????
B530: 86 02           STX     $02                 
B532: 02 ; ????
B533: 84 02           STY     $02                 
B535: 7C ; ????
B536: B2 ; ????
B537: 76 7A           ROR     $7A,X               
B539: B9 7C 72        LDA     $727C,Y             
B53C: 7C ; ????
B53D: 84 7C           STY     $7C                 
B53F: 84 8A           STY     $8A                 
B541: 02 ; ????
B542: 02 ; ????
B543: 8A              TXA                         
B544: 02 ; ????
B545: 7C ; ????
B546: B2 ; ????
B547: 76 7A           ROR     $7A,X               
B549: 7C ; ????
B54A: 80 ; ????
B54B: F0 B9           BEQ     $B506               ; {}
B54D: 72 ; ????
B54E: FF ; ????
B54F: B2 ; ????
B550: 1C ; ????
B551: 02 ; ????
B552: 02 ; ????
B553: 02 ; ????
B554: 42 ; ????
B555: B9 42 02        LDA     $0242,Y             
B558: 42 ; ????
B559: B2 ; ????
B55A: 3E 46 1C        ROL     $1C46,X             
B55D: 02 ; ????
B55E: 02 ; ????
B55F: 02 ; ????
B560: 3E 42 44        ROL     $4442,X             
B563: 44 ; ????
B564: C4 B3           CPY     $B3                 
B566: 4C FF B4        JMP     $B4FF               ; {}
B569: 4C 02 C2        JMP     $C202               
B56C: B9 5A 42        LDA     $425A,Y             
B56F: 4A              LSR     A                   
B570: 50 4A           BVC     $B5BC               ; {}
B572: 50 B2           BVC     $B526               ; {}
B574: 5A ; ????
B575: 50 B9           BVC     $B530               ; {}
B577: 5A ; ????
B578: 5A ; ????
B579: 02 ; ????
B57A: 50 02           BVC     $B57E               ; {}
B57C: 4A              LSR     A                   
B57D: B2 ; ????
B57E: 50 4A           BVC     $B5CA               ; {}
B580: B9 56 3E        LDA     $3E56,Y             
B583: 46 4C           LSR     $4C                 
B585: 46 4C           LSR     $4C                 
B587: B2 ; ????
B588: 56 4C           LSR     $4C,X               
B58A: 46 B9           LSR     $B9                 
B58C: 4A              LSR     A                   
B58D: 02 ; ????
B58E: 4C B2 56        JMP     $56B2               
B591: 4C FF C2        JMP     $C2FF               
B594: B9 76 68        LDA     $6876,Y             
B597: 6E 64 68        ROR     $6864               
B59A: 5E 4C 56        LSR     $564C,X             
B59D: 5E 50 56        LSR     $5650,X             
B5A0: 4C FF C2        JMP     $C2FF               
B5A3: 6E 60 66        ROR     $6660               
B5A6: 5A ; ????
B5A7: 60              RTS                         
B5A8: 56 5A           LSR     $5A,X               
B5AA: 4E 56 48        LSR     $4856               
B5AD: 4E 42 FF        LSR     $FF42               
B5B0: C2 ; ????
B5B1: B9 3C 3C        LDA     $3C3C,Y             
B5B4: 3C ; ????
B5B5: 42 ; ????
B5B6: 02 ; ????
B5B7: 34 ; ????
B5B8: B2 ; ????
B5B9: 3C ; ????
B5BA: 02 ; ????
B5BB: FF ; ????
B5BC: B9 40 40        LDA     $4040,Y             
B5BF: 40              RTI                         
B5C0: 46 02           LSR     $02                 
B5C2: 34 ; ????
B5C3: B2 ; ????
B5C4: 40              RTI                         
B5C5: 02 ; ????
B5C6: 40              RTI                         
B5C7: 3E 3C 3A        ROL     $3A3C,X             
B5CA: B2 ; ????
B5CB: 48              PHA                         
B5CC: B9 46 02        LDA     $0246,Y             
B5CF: 42 ; ????
B5D0: B2 ; ????
B5D1: 46 42           LSR     $42                 
B5D3: 48              PHA                         
B5D4: 4C 50 54        JMP     $5450               
B5D7: 50 B9           BVC     $B592               ; {}
B5D9: 4C 02 48        JMP     $4802               
B5DC: B2 ; ????
B5DD: 4C B9 48        JMP     $48B9               
B5E0: 02 ; ????
B5E1: 46 B2           LSR     $B2                 
B5E3: 48              PHA                         
B5E4: 46 B9           LSR     $B9                 
B5E6: 48              PHA                         
B5E7: 4A              LSR     A                   
B5E8: 4C B2 4E        JMP     $4EB2               
B5EB: C4 B9           CPY     $B9                 
B5ED: 76 5E           ROR     $5E,X               
B5EF: 6E 5E 64        ROR     $645E               
B5F2: 5E 5E 46        LSR     $465E,X             
B5F5: 56 46           LSR     $46,X               
B5F7: 4C 46 6C        JMP     $6C46               
B5FA: 60              RTS                         
B5FB: 66 60           ROR     $60                 
B5FD: 66 72           ROR     $72                 
B5FF: 54 ; ????
B600: 48              PHA                         
B601: 4E 48 4E        LSR     $4E48               
B604: 5A ; ????
B605: FF ; ????
B606: C2 ; ????
B607: 34 ; ????
B608: 3E 46 56        ROL     $5646,X             
B60B: 4C 46 FF        JMP     $FF46               
B60E: C2 ; ????
B60F: 3A ; ????
B610: 42 ; ????
B611: 48              PHA                         
B612: 4C 48 44        JMP     $4448               
B615: FF ; ????
B616: C2 ; ????
B617: 3E 48 4C        ROL     $4C48,X             
B61A: 50 4C           BVC     $B668               ; {}
B61C: 48              PHA                         
B61D: FF ; ????
B61E: B2 ; ????
B61F: 2E 00 BC        ROL     $BC00               ; {}
B622: 02 ; ????
B623: B4 02           LDY     $02,X               
B625: 02 ; ????
B626: B9 6C 64        LDA     $646C,Y             
B629: 6C 72 6C        JMP     ($6C72)             
B62C: 72 ; ????
B62D: 7C ; ????
B62E: 02 ; ????
B62F: 02 ; ????
B630: 72 ; ????
B631: 02 ; ????
B632: 6C 6E 64        JMP     ($646E)             
B635: 6E 72 6E        ROR     $6E72               
B638: 72 ; ????
B639: 74 ; ????
B63A: 6E 74 74        ROR     $7474               
B63D: 6E 74 C4        ROR     $C474               
B640: 6E 6E 6E        ROR     $6E6E               
B643: 6C 6C 6C        JMP     ($6C6C)             
B646: 68              PLA                         
B647: 68              PLA                         
B648: 68              PLA                         
B649: 6C 6C 6C        JMP     ($6C6C)             
B64C: FF ; ????
B64D: B9 4C 42        LDA     $424C,Y             
B650: 4C 54 4C        JMP     $4C54               
B653: 54 ; ????
B654: 5A ; ????
B655: 02 ; ????
B656: 02 ; ????
B657: 54 ; ????
B658: 02 ; ????
B659: 4C B2 56        JMP     $56B2               
B65C: B9 54 02        LDA     $0254,Y             
B65F: 50 B2           BVC     $B613               ; {}
B661: 4C 50 B9        JMP     $B950               ; {}
B664: 42 ; ????
B665: 38              SEC                         
B666: 5A ; ????
B667: 4A              LSR     A                   
B668: 42 ; ????
B669: 4A              LSR     A                   
B66A: 50 02           BVC     $B66E               ; {}
B66C: 02 ; ????
B66D: 4A              LSR     A                   
B66E: 02 ; ????
B66F: 42 ; ????
B670: B2 ; ????
B671: 46 4A           LSR     $4A                 
B673: 50 54           BVC     $B6C9               ; {}
B675: B9 34 3C        LDA     $3C34,Y             
B678: 42 ; ????
B679: 34 ; ????
B67A: 42 ; ????
B67B: 3C ; ????
B67C: 3A ; ????
B67D: 42 ; ????
B67E: 48              PHA                         
B67F: 34 ; ????
B680: 48              PHA                         
B681: 42 ; ????
B682: 3E 46 34        ROL     $3446,X             
B685: 46 3E           LSR     $3E                 
B687: 38              SEC                         
B688: 36 3E           ROL     $3E,X               
B68A: 42 ; ????
B68B: 44 ; ????
B68C: 42 ; ????
B68D: 3E B4 3C        ROL     $3CB4,X             
B690: 04 ; ????
B691: C2 ; ????
B692: B4 32           LDY     $32,X               
B694: B2 ; ????
B695: 20 2A B2        JSR     $B22A               ; {}
B698: 32 ; ????
B699: 34 ; ????
B69A: B4 2E           LDY     $2E,X               
B69C: B2 ; ????
B69D: 3E B9 42        ROL     $42B9,X             
B6A0: 02 ; ????
B6A1: 46 B2           LSR     $B2                 
B6A3: 4C 46 FF        JMP     $FF46               
B6A6: B4 2E           LDY     $2E,X               
B6A8: B3 ; ????
B6A9: 02 ; ????
B6AA: B2 ; ????
B6AB: 2E 30 B4        ROL     $B430               ; {}
B6AE: 2A              ROL     A                   
B6AF: B3 ; ????
B6B0: 02 ; ????
B6B1: B2 ; ????
B6B2: 26 1E           ROL     $1E                 
B6B4: B4 34           LDY     $34,X               
B6B6: B3 ; ????
B6B7: 02 ; ????
B6B8: B2 ; ????
B6B9: 2E 3C B4        ROL     $B43C               ; {}
B6BC: 38              SEC                         
B6BD: B3 ; ????
B6BE: 02 ; ????
B6BF: 2A              ROL     A                   
B6C0: B4 26           LDY     $26,X               
B6C2: B2 ; ????
B6C3: 20 24 26        JSR     $2624               
B6C6: 2A              ROL     A                   
B6C7: B4 26           LDY     $26,X               
B6C9: B3 ; ????
B6CA: 26 2A           ROL     $2A                 
B6CC: C2 ; ????
B6CD: B3 ; ????
B6CE: 26 B2           ROL     $B2                 
B6D0: 16 1C           ASL     $1C,X               
B6D2: B3 ; ????
B6D3: 1E B2 24        ASL     $24B2,X             
B6D6: 2A              ROL     A                   
B6D7: FF ; ????
B6D8: B3 ; ????
B6D9: 2E B2 26        ROL     $26B2               
B6DC: 2E 2A 2E        ROL     $2E2A               
B6DF: 30 2A           BMI     $B70B               ; {}
B6E1: B3 ; ????
B6E2: 2E B2 26        ROL     $26B2               
B6E5: 2E 2A 36        ROL     $362A               
B6E8: 3C ; ????
B6E9: 42 ; ????
B6EA: C3 ; ????
B6EB: B4 3E           LDY     $3E,X               
B6ED: FF ; ????
B6EE: B4 0E           LDY     $0E,X               
B6F0: C4 B4           CPY     $B4                 
B6F2: 02 ; ????
B6F3: FF ; ????
B6F4: 7C ; ????
B6F5: 78              SEI                         
B6F6: 76 74           ROR     $74,X               
B6F8: B2 ; ????
B6F9: 1C ; ????
B6FA: 02 ; ????
B6FB: 02 ; ????
B6FC: 02 ; ????
B6FD: 26 24           ROL     $24                 
B6FF: 20 2A 1C        JSR     $1C2A               
B702: 02 ; ????
B703: 02 ; ????
B704: 02 ; ????
B705: B9 3E 02        LDA     $023E,Y             
B708: 3E B2 26        ROL     $26B2,X             
B70B: B9 44 3E        LDA     $3E44,Y             
B70E: 34 ; ????
B70F: B2 ; ????
B710: 2C B2 1C        BIT     $1CB2               
B713: B9 02 02        LDA     $0202,Y             
B716: 1C ; ????
B717: B2 ; ????
B718: 22 ; ????
B719: B9 02 02        LDA     $0202,Y             
B71C: 22 ; ????
B71D: B2 ; ????
B71E: 20 B9 02        JSR     $02B9               
B721: 02 ; ????
B722: 20 B2 1E        JSR     $1EB2               
B725: B9 02 02        LDA     $0202,Y             
B728: 1E D4 B2        ASL     $B2D4,X             ; {}
B72B: 1C ; ????
B72C: B9 1C 02        LDA     $021C,Y             
B72F: B0 1C           BCS     $B74D               ; {}
B731: BC 02 FF        LDY     $FF02,X             
B734: C8              INY                         
B735: B2 ; ????
B736: 18              CLC                         
B737: B9 18 02        LDA     $0218,Y             
B73A: B0 18           BCS     $B754               ; {}
B73C: BC 02 FF        LDY     $FF02,X             
B73F: C4 B2           CPY     $B2                 
B741: 2E B9 2E        ROL     $2EB9               
B744: 02 ; ????
B745: B0 2E           BCS     $B775               ; {}
B747: BC 02 FF        LDY     $FF02,X             
B74A: C4 B2           CPY     $B2                 
B74C: 20 B9 20        JSR     $20B9               
B74F: 02 ; ????
B750: B0 20           BCS     $B772               ; {}
B752: BC 02 FF        LDY     $FF02,X             
B755: C4 B2           CPY     $B2                 
B757: 2A              ROL     A                   
B758: B9 2A 02        LDA     $022A,Y             
B75B: B0 2A           BCS     $B787               ; {}
B75D: BC 02 FF        LDY     $FF02,X             
B760: C4 B2           CPY     $B2                 
B762: 1C ; ????
B763: B9 1C 02        LDA     $021C,Y             
B766: B0 1C           BCS     $B784               ; {}
B768: BC 02 FF        LDY     $FF02,X             
B76B: D0 B2           BNE     $B71F               ; {}
B76D: 26 B9           ROL     $B9                 
B76F: 3E 02 34        ROL     $3402,X             
B772: FF ; ????
B773: E0 B2           CPX     #$B2                
B775: 26 B9           ROL     $B9                 
B777: 3E 02 B0        ROL     $B002,X             ; {}
B77A: 26 BC           ROL     $BC                 
B77C: 02 ; ????
B77D: FF ; ????
B77E: CA              DEX                         
B77F: B2 ; ????
B780: 04 ; ????
B781: B9 01 01        LDA     $0101,Y             
B784: 04 ; ????
B785: B3 ; ????
B786: 04 ; ????
B787: FF ; ????
B788: F0 B2           BEQ     $B73C               ; {}
B78A: 04 ; ????
B78B: B9 04 04        LDA     $0404,Y             
B78E: 04 ; ????
B78F: FF ; ????
B790: F0 B2           BEQ     $B744               ; {}
B792: 04 ; ????
B793: B9 04 04        LDA     $0404,Y             
B796: 04 ; ????
B797: FF ; ????
B798: CC B1 72        CPY     $72B1               
B79B: 76 FF           ROR     $FF,X               
B79D: CC B9 72        CPY     $72B9               
B7A0: FF ; ????
B7A1: 02 ; ????
B7A2: 02 ; ????
B7A3: 02 ; ????
B7A4: 60              RTS                         
B7A5: 60              RTS                         
B7A6: 60              RTS                         
B7A7: 5E 5E 5E        LSR     $5E5E,X             
B7AA: 5C ; ????
B7AB: 5C ; ????
B7AC: 5C ; ????
B7AD: CC 72 FF        CPY     $FF72               
B7B0: 02 ; ????
B7B1: 02 ; ????
B7B2: 02 ; ????
B7B3: 60              RTS                         
B7B4: 60              RTS                         
B7B5: 60              RTS                         
B7B6: 5E 5E 5E        LSR     $5E5E,X             
B7B9: 5C ; ????
B7BA: 5C ; ????
B7BB: 5C ; ????
B7BC: C4 54           CPY     $54                 
B7BE: 54 ; ????
B7BF: 54 ; ????
B7C0: 4C 4C 4C        JMP     $4C4C               
B7C3: 50 50           BVC     $B815               ; {}
B7C5: 50 56           BVC     $B81D               ; {}
B7C7: 56 56           LSR     $56,X               
B7C9: FF ; ????
B7CA: CC 54 56        CPY     $5654               
B7CD: FF ; ????
B7CE: B4 54           LDY     $54,X               
B7D0: 02 ; ????
B7D1: B4 3C           LDY     $3C,X               
B7D3: 3A ; ????
B7D4: 3C ; ????
B7D5: B6 3E           LDX     $3E,Y               
B7D7: B9 38 3E        LDA     $3E38,Y             
B7DA: 48              PHA                         
B7DB: B6 3A           LDX     $3A,Y               
B7DD: B9 3A 44        LDA     $443A,Y             
B7E0: 4C B3 48        JMP     $48B3               
B7E3: 3E 3A 40        ROL     $403A,X             
B7E6: B6 46           LDX     $46,Y               
B7E8: B9 2E 34        LDA     $342E,Y             
B7EB: 3E C2 B6        ROL     $B6C2,X             ; {}
B7EE: 30 B9           BMI     $B7A9               ; {}
B7F0: 30 02           BMI     $B7F4               ; {}
B7F2: 30 B4           BMI     $B7A8               ; {}
B7F4: 2E FF C2        ROL     $C2FF               
B7F7: B3 ; ????
B7F8: 30 B2           BMI     $B7AC               ; {}
B7FA: 2E B9 26        ROL     $26B9               
B7FD: 2E 34 FF        ROL     $FF34               
B800: CC B9 30        CPY     $30B9               
B803: 2E FF C2        ROL     $C2FF               
B806: B9 42 02        LDA     $0242,Y             
B809: 42 ; ????
B80A: B2 ; ????
B80B: 42 ; ????
B80C: 42 ; ????
B80D: 42 ; ????
B80E: B3 ; ????
B80F: 42 ; ????
B810: B2 ; ????
B811: 5A ; ????
B812: B7 ; ????
B813: 5A ; ????
B814: B0 5E           BCS     $B874               ; {}
B816: B4 50           LDY     $50,X               
B818: B2 ; ????
B819: 46 4A           LSR     $4A                 
B81B: 4C 44 FF        JMP     $FF44               
B81E: C2 ; ????
B81F: B4 34           LDY     $34,X               
B821: 38              SEC                         
B822: 3C ; ????
B823: B3 ; ????
B824: 3E B2 34        ROL     $34B2,X             
B827: 38              SEC                         
B828: FF ; ????
B829: B3 ; ????
B82A: 3C ; ????
B82B: B2 ; ????
B82C: 42 ; ????
B82D: 4C B3 46        JMP     $46B3               
B830: B2 ; ????
B831: 4A              LSR     A                   
B832: 46 B3           LSR     $B3                 
B834: 3C ; ????
B835: B2 ; ????
B836: 42 ; ????
B837: 4C B3 50        JMP     $50B3               
B83A: B2 ; ????
B83B: 4A              LSR     A                   
B83C: B9 4A 4C        LDA     $4C4A,Y             
B83F: 50 B2           BVC     $B7F3               ; {}
B841: 4C 54 5A        JMP     $5A54               
B844: B9 4C 54        LDA     $544C,Y             
B847: 5A ; ????
B848: B2 ; ????
B849: 58              CLI                         
B84A: 54 ; ????
B84B: 50 4C           BVC     $B899               ; {}
B84D: 32 ; ????
B84E: 34 ; ????
B84F: 38              SEC                         
B850: 34 ; ????
B851: 46 3E           LSR     $3E                 
B853: 4A              LSR     A                   
B854: 44 ; ????
B855: C2 ; ????
B856: B9 72 68        LDA     $6872,Y             
B859: 6A              ROR     A                   
B85A: 60              RTS                         
B85B: 64 ; ????
B85C: 5A ; ????
B85D: 60              RTS                         
B85E: 52 ; ????
B85F: 5A ; ????
B860: 4C 50 48        JMP     $4850               
B863: 7A ; ????
B864: 6C 72 68        JMP     ($6872)             
B867: 6C 62 68        JMP     ($6862)             
B86A: 5E 62 54        LSR     $5462,X             
B86D: 5A ; ????
B86E: 50 FF           BVC     $B86F               ; {}
B870: 72 ; ????
B871: 68              PLA                         
B872: 6A              ROR     A                   
B873: 60              RTS                         
B874: 64 ; ????
B875: 5A ; ????
B876: 60              RTS                         
B877: 52 ; ????
B878: 5A ; ????
B879: 4C 50 48        JMP     $4850               
B87C: 2A              ROL     A                   
B87D: 2A              ROL     A                   
B87E: 2A              ROL     A                   
B87F: 34 ; ????
B880: 02 ; ????
B881: 24 34           BIT     $34                 
B883: 34 ; ????
B884: 34 ; ????
B885: 3C ; ????
B886: 02 ; ????
B887: 2A              ROL     A                   
B888: 3C ; ????
B889: 3C ; ????
B88A: 3C ; ????
B88B: 42 ; ????
B88C: 02 ; ????
B88D: 3C ; ????
B88E: B2 ; ????
B88F: 4C 02 4C        JMP     $4C02               
B892: 02 ; ????
B893: 4C 02 B4        JMP     $B402               ; {}
B896: 1C ; ????
B897: B2 ; ????
B898: 02 ; ????
B899: B1 12           LDA     ($12),Y             
B89B: 12 ; ????
B89C: 12 ; ????
B89D: B2 ; ????
B89E: 12 ; ????
B89F: 00              BRK                         
B8A0: CC B1 6C        CPY     $6CB1               
B8A3: 6E FF C2        ROR     $C2FF               
B8A6: B9 02 02        LDA     $0202,Y             
B8A9: 02 ; ????
B8AA: 6E 6E 6E        ROR     $6E6E               
B8AD: 6C 6C 6C        JMP     ($6C6C)             
B8B0: 68              PLA                         
B8B1: 68              PLA                         
B8B2: 68              PLA                         
B8B3: 64 ; ????
B8B4: 64 ; ????
B8B5: 64 ; ????
B8B6: 68              PLA                         
B8B7: 68              PLA                         
B8B8: 68              PLA                         
B8B9: 6C 6C 6C        JMP     ($6C6C)             
B8BC: 6E 6E 6E        ROR     $6E6E               
B8BF: FF ; ????
B8C0: C4 42           CPY     $42                 
B8C2: 42 ; ????
B8C3: 42 ; ????
B8C4: 42 ; ????
B8C5: 42 ; ????
B8C6: 42 ; ????
B8C7: 44 ; ????
B8C8: 44 ; ????
B8C9: 44 ; ????
B8CA: 44 ; ????
B8CB: 44 ; ????
B8CC: 44 ; ????
B8CD: FF ; ????
B8CE: CC 42 44        CPY     $4442               
B8D1: FF ; ????
B8D2: B4 42           LDY     $42,X               
B8D4: 2A              ROL     A                   
B8D5: B9 1C 1C        LDA     $1C1C,Y             
B8D8: 1C ; ????
B8D9: 24 02           BIT     $02                 
B8DB: 12 ; ????
B8DC: B2 ; ????
B8DD: 1C ; ????
B8DE: B9 1C 24        LDA     $241C,Y             
B8E1: 2A              ROL     A                   
B8E2: B4 28           LDY     $28,X               
B8E4: B9 24 24        LDA     $2424,Y             
B8E7: 24 2A           BIT     $2A                 
B8E9: 02 ; ????
B8EA: 1C ; ????
B8EB: B2 ; ????
B8EC: 24 B9           BIT     $B9                 
B8EE: 24 2A           BIT     $2A                 
B8F0: 34 ; ????
B8F1: B4 30           LDY     $30,X               
B8F3: B9 2C 2C        LDA     $2C2C,Y             
B8F6: 2C 34 02        BIT     $0234               
B8F9: 22 ; ????
B8FA: B2 ; ????
B8FB: 2C B9 2C        BIT     $2CB9               
B8FE: 34 ; ????
B8FF: 3A ; ????
B900: B4 38           LDY     $38,X               
B902: B9 32 32        LDA     $3232,Y             
B905: 32 ; ????
B906: 3A ; ????
B907: 02 ; ????
B908: 28              PLP                         
B909: B2 ; ????
B90A: 32 ; ????
B90B: B9 32 3A        LDA     $3A32,Y             
B90E: 40              RTI                         
B90F: B4 3E           LDY     $3E,X               
B911: C2 ; ????
B912: B6 40           LDX     $40,Y               
B914: B9 40 02        LDA     $0240,Y             
B917: 40              RTI                         
B918: B4 3E           LDY     $3E,X               
B91A: FF ; ????
B91B: C2 ; ????
B91C: B3 ; ????
B91D: 40              RTI                         
B91E: B2 ; ????
B91F: 3E B9 2E        ROL     $2EB9,X             
B922: 34 ; ????
B923: 3E FF CC        ROL     $CCFF,X             
B926: B9 40 3E        LDA     $3E40,Y             
B929: FF ; ????
B92A: C2 ; ????
B92B: B9 4C 02        LDA     $024C,Y             
B92E: 4C B2 50        JMP     $50B2               
B931: 54 ; ????
B932: 56 B3           LSR     $B3,X               
B934: 5A ; ????
B935: B2 ; ????
B936: 64 ; ????
B937: B7 ; ????
B938: 62 ; ????
B939: B0 64           BCS     $B99F               ; {}
B93B: B3 ; ????
B93C: 5A ; ????
B93D: B7 ; ????
B93E: 02 ; ????
B93F: B0 56           BCS     $B997               ; {}
B941: B7 ; ????
B942: 54 ; ????
B943: B0 4C           BCS     $B991               ; {}
B945: B3 ; ????
B946: 4C 50 FF        JMP     $FF50               
B949: C2 ; ????
B94A: B6 42           LDX     $42,Y               
B94C: B7 ; ????
B94D: 4C B0 42        JMP     $42B0               
B950: B4 46           LDY     $46,X               
B952: B6 4C           LDX     $4C,Y               
B954: B7 ; ????
B955: 42 ; ????
B956: B0 4C           BCS     $B9A4               ; {}
B958: B3 ; ????
B959: 4C B2 3E        JMP     $3EB2               
B95C: 3E FF B9        ROL     $B9FF,X             ; {}
B95F: 2A              ROL     A                   
B960: 2A              ROL     A                   
B961: 2A              ROL     A                   
B962: 34 ; ????
B963: 02 ; ????
B964: 24 B2           BIT     $B2                 
B966: 2A              ROL     A                   
B967: B9 2A 34        LDA     $342A,Y             
B96A: 3C ; ????
B96B: B4 38           LDY     $38,X               
B96D: B9 34 34        LDA     $3434,Y             
B970: 34 ; ????
B971: 3C ; ????
B972: 02 ; ????
B973: 2A              ROL     A                   
B974: B2 ; ????
B975: 34 ; ????
B976: B9 34 3C        LDA     $3C34,Y             
B979: 42 ; ????
B97A: B4 3E           LDY     $3E,X               
B97C: B9 3C 3C        LDA     $3C3C,Y             
B97F: 3C ; ????
B980: 42 ; ????
B981: 02 ; ????
B982: 34 ; ????
B983: B2 ; ????
B984: 3C ; ????
B985: B9 3C 42        LDA     $423C,Y             
B988: 4C B3 46        JMP     $46B3               
B98B: B2 ; ????
B98C: 4A              LSR     A                   
B98D: 46 B3           LSR     $B3                 
B98F: 42 ; ????
B990: B2 ; ????
B991: 3E 3C B3        ROL     $B33C,X             ; {}
B994: 4C 50 B4        JMP     $B450               ; {}
B997: 4C B3 38        JMP     $38B3               
B99A: B2 ; ????
B99B: 3C ; ????
B99C: 42 ; ????
B99D: B4 34           LDY     $34,X               
B99F: B3 ; ????
B9A0: 38              SEC                         
B9A1: B2 ; ????
B9A2: 42 ; ????
B9A3: 4C B4 48        JMP     $48B4               
B9A6: B9 1C 1C        LDA     $1C1C,Y             
B9A9: 1C ; ????
B9AA: 24 02           BIT     $02                 
B9AC: 2A              ROL     A                   
B9AD: 24 24           BIT     $24                 
B9AF: 24 2A           BIT     $2A                 
B9B1: 02 ; ????
B9B2: 1C ; ????
B9B3: 2A              ROL     A                   
B9B4: 2A              ROL     A                   
B9B5: 2A              ROL     A                   
B9B6: 34 ; ????
B9B7: 02 ; ????
B9B8: 2A              ROL     A                   
B9B9: B2 ; ????
B9BA: 3C ; ????
B9BB: 02 ; ????
B9BC: 3C ; ????
B9BD: 02 ; ????
B9BE: 3C ; ????
B9BF: 02 ; ????
B9C0: B4 2A           LDY     $2A,X               
B9C2: B2 ; ????
B9C3: 02 ; ????
B9C4: B1 04           LDA     ($04),Y             
B9C6: 04 ; ????
B9C7: 04 ; ????
B9C8: B2 ; ????
B9C9: 04 ; ????
B9CA: C7 ; ????
B9CB: B4 02           LDY     $02,X               
B9CD: FF ; ????
B9CE: B2 ; ????
B9CF: 42 ; ????
B9D0: 34 ; ????
B9D1: 38              SEC                         
B9D2: B7 ; ????
B9D3: 3C ; ????
B9D4: B0 3E           BCS     $BA14               ; {}
B9D6: B2 ; ????
B9D7: 42 ; ????
B9D8: 4C 50 B7        JMP     $B750               ; {}
B9DB: 54 ; ????
B9DC: B0 56           BCS     $BA34               ; {}
B9DE: C2 ; ????
B9DF: B2 ; ????
B9E0: 5A ; ????
B9E1: 64 ; ????
B9E2: 68              PLA                         
B9E3: B7 ; ????
B9E4: 6C B0 6E        JMP     ($6EB0)             
B9E7: FF ; ????
B9E8: B4 72           LDY     $72,X               
B9EA: 1C ; ????
B9EB: 1C ; ????
B9EC: 1C ; ????
B9ED: E0 B2           CPX     #$B2                
B9EF: 1C ; ????
B9F0: B9 34 02        LDA     $0234,Y             
B9F3: B0 1C           BCS     $BA11               ; {}
B9F5: BC 02 FF        LDY     $FF02,X             
B9F8: C2 ; ????
B9F9: B2 ; ????
B9FA: 34 ; ????
B9FB: 32 ; ????
B9FC: 2E 2A B4        ROL     $B42A               ; {}
B9FF: 26 24           ROL     $24                 
BA01: 2A              ROL     A                   
BA02: FF ; ????
BA03: C2 ; ????
BA04: B1 3C           LDA     ($3C),Y             
BA06: 02 ; ????
BA07: 3C ; ????
BA08: 02 ; ????
BA09: 3C ; ????
BA0A: 02 ; ????
BA0B: B0 3C           BCS     $BA49               ; {}
BA0D: BC 02 B0        LDY     $B002,X             ; {}
BA10: 3C ; ????
BA11: BC 02 B0        LDY     $B002,X             ; {}
BA14: 3C ; ????
BA15: BC 02 B1        LDY     $B102,X             ; {}
BA18: 3E 02 3E        ROL     $3E02,X             
BA1B: 02 ; ????
BA1C: 3E 02 B0        ROL     $B002,X             ; {}
BA1F: 3E BC 02        ROL     $02BC,X             
BA22: B0 3E           BCS     $BA62               ; {}
BA24: BC 02 B0        LDY     $B002,X             ; {}
BA27: 3E BC 02        ROL     $02BC,X             
BA2A: B1 42           LDA     ($42),Y             
BA2C: 02 ; ????
BA2D: 42 ; ????
BA2E: 02 ; ????
BA2F: 42 ; ????
BA30: 02 ; ????
BA31: B0 42           BCS     $BA75               ; {}
BA33: BC 02 B0        LDY     $B002,X             ; {}
BA36: 42 ; ????
BA37: BC 02 B0        LDY     $B002,X             ; {}
BA3A: 42 ; ????
BA3B: BC 02 B1        LDY     $B102,X             ; {}
BA3E: 48              PHA                         
BA3F: 02 ; ????
BA40: B9 48 30        LDA     $3048,Y             
BA43: 48              PHA                         
BA44: B1 46           LDA     ($46),Y             
BA46: 02 ; ????
BA47: 44 ; ????
BA48: 02 ; ????
BA49: FF ; ????
BA4A: C2 ; ????
BA4B: B2 ; ????
BA4C: 24 B9           BIT     $B9                 
BA4E: 24 02           BIT     $02                 
BA50: B0 24           BCS     $BA76               ; {}
BA52: BC 02 FF        LDY     $FF02,X             
BA55: C2 ; ????
BA56: B2 ; ????
BA57: 26 B9           ROL     $B9                 
BA59: 26 02           ROL     $02                 
BA5B: B0 26           BCS     $BA83               ; {}
BA5D: BC 02 FF        LDY     $FF02,X             
BA60: C2 ; ????
BA61: B2 ; ????
BA62: 2A              ROL     A                   
BA63: B9 2A 02        LDA     $022A,Y             
BA66: B0 2A           BCS     $BA92               ; {}
BA68: BC 02 FF        LDY     $FF02,X             
BA6B: C2 ; ????
BA6C: B2 ; ????
BA6D: 2C B9 2C        BIT     $2CB9               
BA70: 02 ; ????
BA71: B0 2C           BCS     $BA9F               ; {}
BA73: BC 02 FF        LDY     $FF02,X             
BA76: B2 ; ????
BA77: 2E B9 2E        ROL     $2EB9               
BA7A: 02 ; ????
BA7B: 2E B2 2E        ROL     $2EB2               
BA7E: B9 2E 3C        LDA     $3C2E,Y             
BA81: 2E B2 20        ROL     $20B2               
BA84: 34 ; ????
BA85: 32 ; ????
BA86: 2E C4 B7        ROL     $B7C4               ; {}
BA89: 2A              ROL     A                   
BA8A: B0 02           BCS     $BA8E               ; {}
BA8C: B9 2A 02        LDA     $022A,Y             
BA8F: B0 2A           BCS     $BABB               ; {}
BA91: BC 02 FF        LDY     $FF02,X             
BA94: C2 ; ????
BA95: B2 ; ????
BA96: 30 B9           BMI     $BA51               ; {}
BA98: 18              CLC                         
BA99: 02 ; ????
BA9A: 22 ; ????
BA9B: FF ; ????
BA9C: C2 ; ????
BA9D: B2 ; ????
BA9E: 34 ; ????
BA9F: B9 1C 02        LDA     $021C,Y             
BAA2: 2A              ROL     A                   
BAA3: FF ; ????
BAA4: C2 ; ????
BAA5: B2 ; ????
BAA6: 30 B9           BMI     $BA61               ; {}
BAA8: 18              CLC                         
BAA9: 02 ; ????
BAAA: 22 ; ????
BAAB: FF ; ????
BAAC: C2 ; ????
BAAD: B2 ; ????
BAAE: 34 ; ????
BAAF: B9 1C 02        LDA     $021C,Y             
BAB2: 2A              ROL     A                   
BAB3: FF ; ????
BAB4: C2 ; ????
BAB5: B2 ; ????
BAB6: 30 B9           BMI     $BA71               ; {}
BAB8: 18              CLC                         
BAB9: 02 ; ????
BABA: 22 ; ????
BABB: FF ; ????
BABC: D2 ; ????
BABD: B0 1C           BCS     $BADB               ; {}
BABF: BC 02 FF        LDY     $FF02,X             
BAC2: B2 ; ????
BAC3: 1C ; ????
BAC4: 02 ; ????
BAC5: 1C ; ????
BAC6: 02 ; ????
BAC7: 1C ; ????
BAC8: 02 ; ????
BAC9: B4 1C           LDY     $1C,X               
BACB: B2 ; ????
BACC: 02 ; ????
BACD: 1C ; ????
BACE: 02 ; ????
BACF: 1C ; ????
BAD0: 02 ; ????
BAD1: 1C ; ????
BAD2: 02 ; ????
BAD3: B3 ; ????
BAD4: 1C ; ????
BAD5: C3 ; ????
BAD6: B4 01           LDY     $01,X               
BAD8: FF ; ????
BAD9: F0 B2           BEQ     $BA8D               ; {}
BADB: 04 ; ????
BADC: FF ; ????
BADD: DC ; ????
BADE: B2 ; ????
BADF: 04 ; ????
BAE0: B9 04 04        LDA     $0404,Y             
BAE3: 04 ; ????
BAE4: FF ; ????
BAE5: D8              CLD                         
BAE6: 04 ; ????
BAE7: FF ; ????
BAE8: D0 B3           BNE     $BA9D               ; {}
BAEA: 04 ; ????
BAEB: FF ; ????
BAEC: C7 ; ????
BAED: B2 ; ????
BAEE: 04 ; ????
BAEF: 04 ; ????
BAF0: 04 ; ????
BAF1: B9 04 04        LDA     $0404,Y             
BAF4: 04 ; ????
BAF5: FF ; ????
BAF6: CC B9 04        CPY     $04B9               
BAF9: FF ; ????
BAFA: D0 B9           BNE     $BAB5               ; {}
BAFC: 04 ; ????
BAFD: 01 04           ORA     ($04,X)             
BAFF: B2 ; ????
BB00: 07 ; ????
BB01: FF ; ????
BB02: CA              DEX                         
BB03: B9 04 04        LDA     $0404,Y             
BB06: 04 ; ????
BB07: B2 ; ????
BB08: 04 ; ????
BB09: FF ; ????
BB0A: C3 ; ????
BB0B: B9 04 04        LDA     $0404,Y             
BB0E: 04 ; ????
BB0F: 07 ; ????
BB10: 01 07           ORA     ($07,X)             
BB12: FF ; ????
BB13: C3 ; ????
BB14: B2 ; ????
BB15: 07 ; ????
BB16: 01 FF           ORA     ($FF,X)             
BB18: D0 B0           BNE     $BACA               ; {}
BB1A: 04 ; ????
BB1B: FF ; ????
BB1C: B2 ; ????
BB1D: 01 C4           ORA     ($C4,X)             
BB1F: B1 04           LDA     ($04),Y             
BB21: FF ; ????
BB22: B4 01           LDY     $01,X               
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
BBF9: 04 ; ????
BBFA: 08              PHP                         
BBFB: 01 40           ORA     ($40,X)             
BBFD: 00              BRK                         
BBFE: 20 00 FF        JSR     $FF00               
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
BC6E: 7F ; ????
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
BC96: BF ; ????
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
BFF8: 48              PHA                         
BFF9: 82 ; ????
BFFA: 23 ; ????
BFFB: 64 ; ????
BFFC: 00              BRK                         
BFFD: 08              PHP                         
BFFE: 00              BRK                         
BFFF: 00              BRK                         
```

