![Bank 4](Zelda.jpg)

# Bank 4

>>> cpu 6502

>>> binary 8000:roms/Zelda.nes[10010:14010]

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](Hardware.md)

```code
8000: BD F0 04        LDA     $04F0,X             ; {ram.04F0}
8003: C9 10           CMP     #$10                ; 
8005: D0 05           BNE     $800C               ; {}
8007: A9 02           LDA     #$02                ; 
8009: 8D 01 06        STA     $0601               ; {ram.??SND_601??}
800C: 60              RTS                         ; 
800D: BD 05 04        LDA     $0405,X             ; {ram.0405}
8010: F0 FA           BEQ     $800C               ; {}
8012: 4C 10 B0        JMP     $B010               ; {}
8015: A9 C0           LDA     #$C0                ; 
8017: D0 02           BNE     $801B               ; {}
8019: A9 E0           LDA     #$E0                ; 
801B: 9D BC 03        STA     $03BC,X             ; {ram.03BC}
801E: 4C DA FE        JMP     $FEDA               ; 
8021: A9 80           LDA     #$80                ; 
8023: 95 28           STA     $28,X               ; {ram.0028}
8025: B5 98           LDA     $98,X               ; {ram.0098}
8027: D0 25           BNE     $804E               ; {}
8029: A0 02           LDY     #$02                ; 
802B: A5 61           LDA     <$61                ; {ram.0061}
802D: 38              SEC                         ; 
802E: F5 70           SBC     $70,X               ; {ram.0070}
8030: B0 01           BCS     $8033               ; {}
8032: 88              DEY                         ; 
8033: 85 00           STA     <$00                ; {ram.GP_00}
8035: 84 01           STY     <$01                ; {ram.GP_01}
8037: 94 98           STY     $98,X               ; {ram.0098}
8039: A0 04           LDY     #$04                ; 
803B: A5 62           LDA     <$62                ; {ram.0062}
803D: 38              SEC                         ; 
803E: F5 84           SBC     $84,X               ; {ram.0084}
8040: B0 02           BCS     $8044               ; {}
8042: A0 08           LDY     #$08                ; 
8044: 94 98           STY     $98,X               ; {ram.0098}
8046: C5 00           CMP     <$00                ; {ram.GP_00}
8048: 90 04           BCC     $804E               ; {}
804A: A5 01           LDA     <$01                ; {ram.GP_01}
804C: 95 98           STA     $98,X               ; {ram.0098}
804E: 60              RTS                         ; 
804F: 20 A7 7A        JSR     $7AA7               ; {ram.7AA7}
8052: A9 02           LDA     #$02                ; 
8054: 20 88 79        JSR     $7988               ; {ram.7988}
8057: A9 08           LDA     #$08                ; 
8059: 95 98           STA     $98,X               ; {ram.0098}
805B: 20 4F FA        JSR     $FA4F               ; 
805E: BD 4F 03        LDA     $034F,X             ; {ram.034F}
8061: C9 40           CMP     #$40                ; 
8063: F0 04           BEQ     $8069               ; {}
8065: A9 00           LDA     #$00                ; 
8067: 85 0F           STA     <$0F                ; {ram.000F}
8069: A9 00           LDA     #$00                ; 
806B: 4C DF 77        JMP     $77DF               ; {ram.77DF}
806E: 9D 1F 04        STA     $041F,X             ; {ram.041F}
8071: B5 C0           LDA     $C0,X               ; {ram.00C0}
8073: F0 03           BEQ     $8078               ; {}
8075: 4C B8 EE        JMP     $EEB8               ; 
8078: AD 6C 06        LDA     $066C               ; {ram.066C}
807B: 15 3D           ORA     $3D,X               ; {ram.003D}
807D: D0 24           BNE     $80A3               ; {}
807F: 4C 94 80        JMP     $8094               ; {}
8082: A9 70           LDA     #$70                ; 
8084: BC 4F 03        LDY     $034F,X             ; {ram.034F}
8087: C0 05           CPY     #$05                ; 
8089: F0 02           BEQ     $808D               ; {}
808B: A9 A0           LDA     #$A0                ; 
808D: 9D 1F 04        STA     $041F,X             ; {ram.041F}
8090: B5 AC           LDA     $AC,X               ; {ram.00AC}
8092: 30 0F           BMI     $80A3               ; {}
8094: BD 78 04        LDA     $0478,X             ; 
8097: F0 03           BEQ     $809C               ; {}
8099: DE 78 04        DEC     $0478,X             ; 
809C: 20 D0 EF        JSR     $EFD0               ; 
809F: B5 C0           LDA     $C0,X               ; {ram.00C0}
80A1: F0 01           BEQ     $80A4               ; {}
80A3: 60              RTS                         ; 
80A4: BD BC 03        LDA     $03BC,X             ; {ram.03BC}
80A7: F0 6D           BEQ     $8116               ; {}
80A9: BD 94 03        LDA     $0394,X             ; {ram.0394}
80AC: 29 0F           AND     #$0F                ; 
80AE: D0 66           BNE     $8116               ; {}
80B0: 9D 94 03        STA     $0394,X             ; {ram.0394}
80B3: BD 1F 04        LDA     $041F,X             ; {ram.041F}
80B6: D5 19           CMP     $19,X               ; {ram.0019}
80B8: 90 4A           BCC     $8104               ; {}
80BA: A5 AC           LDA     <$AC                ; {ram.00AC}
80BC: C9 FF           CMP     #$FF                ; 
80BE: F0 44           BEQ     $8104               ; {}
80C0: A5 61           LDA     <$61                ; {ram.0061}
80C2: 38              SEC                         ; 
80C3: F5 70           SBC     $70,X               ; {ram.0070}
80C5: 10 05           BPL     $80CC               ; {}
80C7: 49 FF           EOR     #$FF                ; 
80C9: 18              CLC                         ; 
80CA: 69 01           ADC     #$01                ; 
80CC: C9 09           CMP     #$09                ; 
80CE: B0 0C           BCS     $80DC               ; {}
80D0: A0 08           LDY     #$08                ; 
80D2: A5 62           LDA     <$62                ; {ram.0062}
80D4: D5 84           CMP     $84,X               ; {ram.0084}
80D6: 90 1D           BCC     $80F5               ; {}
80D8: A0 04           LDY     #$04                ; 
80DA: D0 19           BNE     $80F5               ; {}
80DC: A5 62           LDA     <$62                ; {ram.0062}
80DE: 38              SEC                         ; 
80DF: F5 84           SBC     $84,X               ; {ram.0084}
80E1: 10 05           BPL     $80E8               ; {}
80E3: 49 FF           EOR     #$FF                ; 
80E5: 18              CLC                         ; 
80E6: 69 01           ADC     #$01                ; 
80E8: C9 09           CMP     #$09                ; 
80EA: B0 18           BCS     $8104               ; {}
80EC: A0 01           LDY     #$01                ; 
80EE: A5 61           LDA     <$61                ; {ram.0061}
80F0: D5 70           CMP     $70,X               ; {ram.0070}
80F2: B0 01           BCS     $80F5               ; {}
80F4: C8              INY                         ; 
80F5: 94 98           STY     $98,X               ; {ram.0098}
80F7: B5 18           LDA     $18,X               ; {ram.0018}
80F9: 9D 78 04        STA     $0478,X             ; 
80FC: A9 01           LDA     #$01                ; 
80FE: 9D 12 04        STA     $0412,X             ; {ram.0412}
8101: 4C 90 81        JMP     $8190               ; {}
8104: A9 00           LDA     #$00                ; 
8106: 9D 12 04        STA     $0412,X             ; {ram.0412}
8109: BD 78 04        LDA     $0478,X             ; 
810C: D0 08           BNE     $8116               ; {}
810E: B5 98           LDA     $98,X               ; {ram.0098}
8110: 29 0C           AND     #$0C                ; 
8112: D0 D8           BNE     $80EC               ; {}
8114: F0 BA           BEQ     $80D0               ; {}
8116: 4C 90 81        JMP     $8190               ; {}
8119: BD 50 03        LDA     $0350,X             ; {ram.0350}
811C: C9 1E           CMP     #$1E                ; 
811E: F0 04           BEQ     $8124               ; {}
8120: B5 AC           LDA     $AC,X               ; {ram.00AC}
8122: 30 07           BMI     $812B               ; {}
8124: 20 D0 EF        JSR     $EFD0               ; 
8127: B5 C0           LDA     $C0,X               ; {ram.00C0}
8129: F0 01           BEQ     $812C               ; {}
812B: 60              RTS                         ; 
812C: BD BC 03        LDA     $03BC,X             ; {ram.03BC}
812F: F0 5F           BEQ     $8190               ; {}
8131: BD 94 03        LDA     $0394,X             ; {ram.0394}
8134: 29 0F           AND     #$0F                ; 
8136: D0 58           BNE     $8190               ; {}
8138: 9D 94 03        STA     $0394,X             ; {ram.0394}
813B: A5 AC           LDA     <$AC                ; {ram.00AC}
813D: C9 FF           CMP     #$FF                ; 
813F: F0 4F           BEQ     $8190               ; {}
8141: A9 04           LDA     #$04                ; 
8143: 85 02           STA     <$02                ; {ram.GP_02}
8145: A5 62           LDA     <$62                ; {ram.0062}
8147: B4 84           LDY     $84,X               ; {ram.0084}
8149: D5 84           CMP     $84,X               ; {ram.0084}
814B: B0 06           BCS     $8153               ; {}
814D: B5 84           LDA     $84,X               ; {ram.0084}
814F: A4 62           LDY     <$62                ; {ram.0062}
8151: 06 02           ASL     <$02                ; {ram.GP_02}
8153: 84 0E           STY     <$0E                ; {ram.000E}
8155: 38              SEC                         ; 
8156: E5 0E           SBC     <$0E                ; {ram.000E}
8158: 85 00           STA     <$00                ; {ram.GP_00}
815A: A9 01           LDA     #$01                ; 
815C: 85 03           STA     <$03                ; {ram.GP_03}
815E: A5 61           LDA     <$61                ; {ram.0061}
8160: B4 70           LDY     $70,X               ; {ram.0070}
8162: D5 70           CMP     $70,X               ; {ram.0070}
8164: B0 06           BCS     $816C               ; {}
8166: B5 70           LDA     $70,X               ; {ram.0070}
8168: A4 61           LDY     <$61                ; {ram.0061}
816A: 06 03           ASL     <$03                ; {ram.GP_03}
816C: 84 0E           STY     <$0E                ; {ram.000E}
816E: 38              SEC                         ; 
816F: E5 0E           SBC     <$0E                ; {ram.000E}
8171: 85 01           STA     <$01                ; {ram.GP_01}
8173: A0 00           LDY     #$00                ; 
8175: A5 00           LDA     <$00                ; {ram.GP_00}
8177: C5 01           CMP     <$01                ; {ram.GP_01}
8179: B0 01           BCS     $817C               ; {}
817B: C8              INY                         ; 
817C: A9 00           LDA     #$00                ; 
817E: 9D 12 04        STA     $0412,X             ; {ram.0412}
8181: B9 00 00        LDA     $0000,Y             ; {ram.GP_00}
8184: C9 51           CMP     #$51                ; 
8186: B0 08           BCS     $8190               ; {}
8188: FE 12 04        INC     $0412,X             ; {ram.0412}
818B: B9 02 00        LDA     $0002,Y             ; {ram.GP_02}
818E: 95 98           STA     $98,X               ; {ram.0098}
8190: B5 98           LDA     $98,X               ; {ram.0098}
8192: 9D F8 03        STA     $03F8,X             ; {ram.03F8}
8195: A9 5C           LDA     #$5C                ; 
8197: BC 4F 03        LDY     $034F,X             ; {ram.034F}
819A: C0 05           CPY     #$05                ; 
819C: F0 10           BEQ     $81AE               ; {}
819E: C0 06           CPY     #$06                ; 
81A0: D0 50           BNE     $81F2               ; {}
81A2: B5 18           LDA     $18,X               ; {ram.0018}
81A4: C9 23           CMP     #$23                ; 
81A6: F0 04           BEQ     $81AC               ; {}
81A8: C9 77           CMP     #$77                ; 
81AA: D0 46           BNE     $81F2               ; {}
81AC: A9 5C           LDA     #$5C                ; 
81AE: B4 28           LDY     $28,X               ; {ram.0028}
81B0: D0 40           BNE     $81F2               ; {}
81B2: 85 00           STA     <$00                ; {ram.GP_00}
81B4: AD 6C 06        LDA     $066C               ; {ram.066C}
81B7: 15 3D           ORA     $3D,X               ; {ram.003D}
81B9: D0 37           BNE     $81F2               ; {}
81BB: A5 00           LDA     <$00                ; {ram.GP_00}
81BD: 20 79 B1        JSR     $B179               ; {}
81C0: 90 30           BCC     $81F2               ; {}
81C2: A9 80           LDA     #$80                ; 
81C4: 95 AC           STA     $AC,X               ; {ram.00AC}
81C6: A9 00           LDA     #$00                ; 
81C8: 9D 12 04        STA     $0412,X             ; {ram.0412}
81CB: 8A              TXA                         ; 
81CC: 99 2C 04        STA     $042C,Y             ; {ram.!SplashMode}
81CF: 98              TYA                         ; 
81D0: 9D 2C 04        STA     $042C,X             ; {ram.!SplashMode}
81D3: A9 10           LDA     #$10                ; 
81D5: 99 AC 00        STA     $00AC,Y             ; {ram.00AC}
81D8: A9 A0           LDA     #$A0                ; 
81DA: 99 BC 03        STA     $03BC,Y             ; {ram.03BC}
81DD: A9 51           LDA     #$51                ; 
81DF: 99 80 03        STA     $0380,Y             ; 
81E2: A9 00           LDA     #$00                ; 
81E4: 99 05 04        STA     $0405,Y             ; {ram.0405}
81E7: A9 03           LDA     #$03                ; 
81E9: 99 D0 03        STA     $03D0,Y             ; {ram.03D0}
81EC: B5 18           LDA     $18,X               ; {ram.0018}
81EE: 29 3F           AND     #$3F                ; 
81F0: 95 28           STA     $28,X               ; {ram.0028}
81F2: 60              RTS                         ; 
81F3: 08              PHP                         ; 
81F4: 04                              ;
81F5: 02                              ;
81F6: 01 B5           ORA     ($B5,X)             ; {ram.00B5}
81F8: AC 29 03        LDY     $0329               ; {ram.0329}
81FB: 20 E2 E5        JSR     $E5E2               ; 
81FE: 04                              ;
81FF: 82                              ;
8200: 63                              ;
8201: 82                              ;
8202: 89                              ;
8203: 82                              ;
8204: AD 4D 03        LDA     $034D               ; {ram.034D}
8207: F0 54           BEQ     $825D               ; {}
8209: A5 70           LDA     <$70                ; {ram.0070}
820B: D5 70           CMP     $70,X               ; {ram.0070}
820D: D0 0D           BNE     $821C               ; {}
820F: A0 00           LDY     #$00                ; 
8211: A5 84           LDA     <$84                ; {ram.0084}
8213: 18              CLC                         ; 
8214: 69 03           ADC     #$03                ; 
8216: 38              SEC                         ; 
8217: F5 84           SBC     $84,X               ; {ram.0084}
8219: 4C 2C 82        JMP     $822C               ; {}
821C: A5 84           LDA     <$84                ; {ram.0084}
821E: 18              CLC                         ; 
821F: 69 03           ADC     #$03                ; 
8221: D5 84           CMP     $84,X               ; {ram.0084}
8223: D0 38           BNE     $825D               ; {}
8225: A0 02           LDY     #$02                ; 
8227: A5 70           LDA     <$70                ; {ram.0070}
8229: 38              SEC                         ; 
822A: F5 70           SBC     $70,X               ; {ram.0070}
822C: 10 04           BPL     $8232               ; {}
822E: C8              INY                         ; 
822F: 20 21 70        JSR     $7021               ; {ram.7021}
8232: C9 11           CMP     #$11                ; 
8234: B0 27           BCS     $825D               ; {}
8236: AD F8 03        LDA     $03F8               ; {ram.03F8}
8239: D9 F3 81        CMP     $81F3,Y             ; {}
823C: D0 1F           BNE     $825D               ; {}
823E: FE 12 04        INC     $0412,X             ; {ram.0412}
8241: BC 12 04        LDY     $0412,X             ; {ram.0412}
8244: C0 10           CPY     #$10                ; 
8246: 90 1A           BCC     $8262               ; {}
8248: 95 98           STA     $98,X               ; {ram.0098}
824A: F6 AC           INC     $AC,X               ; {ram.00AC}
824C: E6 F7           INC     <$F7                ; {ram.00F7}
824E: A9 74           LDA     #$74                ; 
8250: 20 62 E8        JSR     $E862               ; 
8253: 20 93 FA        JSR     $FA93               ; 
8256: C6 01           DEC     <$01                ; {ram.GP_01}
8258: A9 00           LDA     #$00                ; 
825A: 4C DF 77        JMP     $77DF               ; {ram.77DF}
825D: A9 00           LDA     #$00                ; 
825F: 9D 12 04        STA     $0412,X             ; {ram.0412}
8262: 60              RTS                         ; 
8263: B5 98           LDA     $98,X               ; {ram.0098}
8265: 85 0F           STA     <$0F                ; {ram.000F}
8267: 20 8D F0        JSR     $F08D               ; 
826A: 20 53 82        JSR     $8253               ; {}
826D: BD 94 03        LDA     $0394,X             ; {ram.0394}
8270: C9 10           CMP     #$10                ; 
8272: F0 04           BEQ     $8278               ; {}
8274: C9 F0           CMP     #$F0                ; 
8276: D0 11           BNE     $8289               ; {}
8278: A9 04           LDA     #$04                ; 
827A: 8D 02 06        STA     $0602               ; {ram.SND_ReqMusEff}
827D: E6 F7           INC     <$F7                ; {ram.00F7}
827F: A9 B0           LDA     #$B0                ; 
8281: 20 62 E8        JSR     $E862               ; 
8284: F6 AC           INC     $AC,X               ; {ram.00AC}
8286: EE CF 04        INC     $04CF               ; {ram.04CF}
8289: 60              RTS                         ; 
828A: A9 F8           LDA     #$F8                ; 
828C: 8D 40 02        STA     $0240               ; {ram.0240}
828F: 8D 44 02        STA     $0244               ; {ram.0244}
8292: 60              RTS                         ; 
8293: A0 00           LDY     #$00                ; 
8295: F0 02           BEQ     $8299               ; {}
8297: A0 01           LDY     #$01                ; 
8299: 84 0C           STY     <$0C                ; {ram.000C}
829B: BC 4F 03        LDY     $034F,X             ; {ram.034F}
829E: C8              INY                         ; 
829F: 85 0D           STA     <$0D                ; {ram.000D}
82A1: 84 0E           STY     <$0E                ; {ram.000E}
82A3: 86 08           STX     <$08                ; {ram.0008}
82A5: A9 40           LDA     #$40                ; 
82A7: 8D 43 03        STA     $0343               ; {ram.0343}
82AA: A9 44           LDA     #$44                ; 
82AC: 4C 04 78        JMP     $7804               ; {ram.7804}
82AF: 85 00           STA     <$00                ; {ram.GP_00}
82B1: 20 BB FE        JSR     $FEBB               ; 
82B4: F0 1A           BEQ     $82D0               ; {}
82B6: 8A              TXA                         ; 
82B7: 48              PHA                         ; 
82B8: 98              TYA                         ; 
82B9: AA              TAX                         ; 
82BA: A5 00           LDA     <$00                ; {ram.GP_00}
82BC: 20 B3 FE        JSR     $FEB3               ; 
82BF: 8A              TXA                         ; 
82C0: A8              TAY                         ; 
82C1: 68              PLA                         ; 
82C2: AA              TAX                         ; 
82C3: B5 70           LDA     $70,X               ; {ram.0070}
82C5: 18              CLC                         ; 
82C6: 69 04           ADC     #$04                ; 
82C8: 99 70 00        STA     $0070,Y             ; {ram.0070}
82CB: B5 84           LDA     $84,X               ; {ram.0084}
82CD: 99 84 00        STA     $0084,Y             ; {ram.0084}
82D0: 60              RTS                         ; 
82D1: 01 FF           ORA     ($FF,X)             ; {ram.CUR_2000}
82D3: FE 02 FF        INC     $FF02,X             ; 
82D6: FF                              ;
82D7: B5 98           LDA     $98,X               ; {ram.0098}
82D9: 85 0F           STA     <$0F                ; {ram.000F}
82DB: B5 AC           LDA     $AC,X               ; {ram.00AC}
82DD: 29 F0           AND     #$F0                ; 
82DF: C9 10           CMP     #$10                ; 
82E1: D0 69           BNE     $834C               ; {}
82E3: BD 4F 03        LDA     $034F,X             ; {ram.034F}
82E6: C9 55           CMP     #$55                ; 
82E8: B0 0C           BCS     $82F6               ; {}
82EA: B5 28           LDA     $28,X               ; {ram.0028}
82EC: D0 10           BNE     $82FE               ; {}
82EE: 20 FA ED        JSR     $EDFA               ; 
82F1: CD 4A 03        CMP     $034A               ; {ram.034A}
82F4: B0 45           BCS     $833B               ; {}
82F6: 20 B8 6F        JSR     $6FB8               ; {ram.6FB8}
82F9: F0 40           BEQ     $833B               ; {}
82FB: 20 8D F0        JSR     $F08D               ; 
82FE: 20 71 83        JSR     $8371               ; {}
8301: A5 06           LDA     <$06                ; {ram.0006}
8303: D0 36           BNE     $833B               ; {}
8305: BD 4F 03        LDA     $034F,X             ; {ram.034F}
8308: C9 5B           CMP     #$5B                ; 
830A: D0 03           BNE     $830F               ; {}
830C: 4C 7B F5        JMP     $F57B               ; 
830F: C9 57           CMP     #$57                ; 
8311: 90 07           BCC     $831A               ; {}
8313: C9 5A           CMP     #$5A                ; 
8315: B0 03           BCS     $831A               ; {}
8317: 4C 91 F3        JMP     $F391               ; 
831A: 20 93 FA        JSR     $FA93               ; 
831D: 85 0D           STA     <$0D                ; {ram.000D}
831F: A5 15           LDA     <$15                ; {ram.0015}
8321: 29 03           AND     #$03                ; 
8323: BC 4F 03        LDY     $034F,X             ; {ram.034F}
8326: C0 55           CPY     #$55                ; 
8328: B0 09           BCS     $8333               ; {}
832A: A0 03           LDY     #$03                ; 
832C: E6 00           INC     <$00                ; {ram.GP_00}
832E: 88              DEY                         ; 
832F: 10 FB           BPL     $832C               ; {}
8331: A9 00           LDA     #$00                ; 
8333: 20 88 79        JSR     $7988               ; {ram.7988}
8336: A5 0D           LDA     <$0D                ; {ram.000D}
8338: 4C DF 77        JMP     $77DF               ; {ram.77DF}
833B: BD 4F 03        LDA     $034F,X             ; {ram.034F}
833E: C9 55           CMP     #$55                ; 
8340: F0 07           BEQ     $8349               ; {}
8342: C9 56           CMP     #$56                ; 
8344: F0 03           BEQ     $8349               ; {}
8346: CE 4C 03        DEC     $034C               ; {ram.034C}
8349: 4C B1 FE        JMP     $FEB1               ; 
834C: BD 80 03        LDA     $0380,X             ; 
834F: 20 13 70        JSR     $7013               ; {ram.7013}
8352: B5 84           LDA     $84,X               ; {ram.0084}
8354: 18              CLC                         ; 
8355: 79 D3 82        ADC     $82D3,Y             ; {}
8358: 95 84           STA     $84,X               ; {ram.0084}
835A: B5 70           LDA     $70,X               ; {ram.0070}
835C: 18              CLC                         ; 
835D: 79 D1 82        ADC     $82D1,Y             ; {}
8360: 95 70           STA     $70,X               ; {ram.0070}
8362: BD 94 03        LDA     $0394,X             ; {ram.0394}
8365: 18              CLC                         ; 
8366: 69 02           ADC     #$02                ; 
8368: 9D 94 03        STA     $0394,X             ; {ram.0394}
836B: C9 20           CMP     #$20                ; 
836D: B0 CC           BCS     $833B               ; {}
836F: 90 94           BCC     $8305               ; {}
8371: A9 00           LDA     #$00                ; 
8373: 9D 94 03        STA     $0394,X             ; {ram.0394}
8376: 20 A7 7A        JSR     $7AA7               ; {ram.7AA7}
8379: AD 4B 03        LDA     $034B               ; {ram.034B}
837C: F0 09           BEQ     $8387               ; {}
837E: A5 98           LDA     <$98                ; {ram.0098}
8380: 9D 80 03        STA     $0380,X             ; 
8383: A9 30           LDA     #$30                ; 
8385: 95 AC           STA     $AC,X               ; {ram.00AC}
8387: 60              RTS                         ; 
8388: 70 68           BVS     $83F2               ; {}
838A: 60              RTS                         ; 
838B: 58              CLI                         ; 
838C: 50 3C           BVC     $83CA               ; {}
838E: 26 10           ROL     <$10                ; {ram.0010}
8390: 00              BRK                         ; 
8391: 10 26           BPL     $83B9               ; {}
8393: 3C                              ;
8394: 50 58           BVC     $83EE               ; {}
8396: 60              RTS                         ; 
8397: 68              PLA                         ; 
8398: 70 B5           BVS     $834F               ; {}
839A: AC D0 2F        LDY     $2FD0               ; 
839D: 9D 51 04        STA     $0451,X             ; 
83A0: 9D 5E 04        STA     $045E,X             ; 
83A3: 20 4A 70        JSR     $704A               ; {ram.704A}
83A6: A5 0B           LDA     <$0B                ; {ram.000B}
83A8: 9D 12 04        STA     $0412,X             ; {ram.0412}
83AB: A5 0A           LDA     <$0A                ; {ram.000A}
83AD: 9D 37 04        STA     $0437,X             ; {ram.0437}
83B0: 05 0B           ORA     <$0B                ; {ram.000B}
83B2: 95 98           STA     $98,X               ; {ram.0098}
83B4: A0 04           LDY     #$04                ; 
83B6: 20 6F 70        JSR     $706F               ; {ram.706F}
83B9: B9 88 83        LDA     $8388,Y             ; {}
83BC: 9D 1F 04        STA     $041F,X             ; {ram.041F}
83BF: B9 90 83        LDA     $8390,Y             ; {}
83C2: 9D 44 04        STA     $0444,X             ; 
83C5: A9 10           LDA     #$10                ; 
83C7: 95 AC           STA     $AC,X               ; {ram.00AC}
83C9: 95 28           STA     $28,X               ; {ram.0028}
83CB: 60              RTS                         ; 
83CC: B5 28           LDA     $28,X               ; {ram.0028}
83CE: D0 2C           BNE     $83FC               ; {}
83D0: B5 98           LDA     $98,X               ; {ram.0098}
83D2: 20 B6 6F        JSR     $6FB6               ; {ram.6FB6}
83D5: D0 03           BNE     $83DA               ; {}
83D7: 4C B1 FE        JMP     $FEB1               ; 
83DA: BD 12 04        LDA     $0412,X             ; {ram.0412}
83DD: 85 0F           STA     <$0F                ; {ram.000F}
83DF: BD 1F 04        LDA     $041F,X             ; {ram.041F}
83E2: BC 51 04        LDY     $0451,X             ; 
83E5: 20 07 84        JSR     $8407               ; {}
83E8: 9D 51 04        STA     $0451,X             ; 
83EB: BD 37 04        LDA     $0437,X             ; {ram.0437}
83EE: 85 0F           STA     <$0F                ; {ram.000F}
83F0: BD 44 04        LDA     $0444,X             ; 
83F3: BC 5E 04        LDY     $045E,X             ; 
83F6: 20 07 84        JSR     $8407               ; {}
83F9: 9D 5E 04        STA     $045E,X             ; 
83FC: 20 71 83        JSR     $8371               ; {}
83FF: AD 4B 03        LDA     $034B               ; {ram.034B}
8402: D0 D3           BNE     $83D7               ; {}
8404: 4C 05 83        JMP     $8305               ; {}
8407: 9D BC 03        STA     $03BC,X             ; {ram.03BC}
840A: 98              TYA                         ; 
840B: 9D A8 03        STA     $03A8,X             ; {ram.03A8}
840E: 20 8D F0        JSR     $F08D               ; 
8411: BD A8 03        LDA     $03A8,X             ; {ram.03A8}
8414: 60              RTS                         ; 
8415: A9 40           LDA     #$40                ; 
8417: 9D BC 03        STA     $03BC,X             ; {ram.03BC}
841A: 4C 25 80        JMP     $8025               ; {}
841D: B5 18           LDA     $18,X               ; {ram.0018}
841F: 29 07           AND     #$07                ; 
8421: A8              TAY                         ; 
8422: B9 4E B2        LDA     $B24E,Y             ; {}
8425: 95 98           STA     $98,X               ; {ram.0098}
8427: 20 0B B2        JSR     $B20B               ; {}
842A: A9 C0           LDA     #$C0                ; 
842C: 8D D1 04        STA     $04D1               ; {ram.04D1}
842F: A9 1F           LDA     #$1F                ; 
8431: 9D 1F 04        STA     $041F,X             ; {ram.041F}
8434: 60              RTS                         ; 
8435: 20 1D 84        JSR     $841D               ; {}
8438: A9 7F           LDA     #$7F                ; 
843A: 9D 1F 04        STA     $041F,X             ; {ram.041F}
843D: 60              RTS                         ; 
843E: A9 40           LDA     #$40                ; 
8440: 20 6E 80        JSR     $806E               ; {}
8443: BD 4F 03        LDA     $034F,X             ; {ram.034F}
8446: C9 2B           CMP     #$2B                ; 
8448: F0 06           BEQ     $8450               ; {}
844A: 38              SEC                         ; 
844B: E9 2B           SBC     #$2B                ; 
844D: 4C 54 84        JMP     $8454               ; {}
8450: A5 15           LDA     <$15                ; {ram.0015}
8452: 29 03           AND     #$03                ; 
8454: 20 88 79        JSR     $7988               ; {ram.7988}
8457: A9 01           LDA     #$01                ; 
8459: 20 76 84        JSR     $8476               ; {}
845C: 20 A7 7A        JSR     $7AA7               ; {ram.7AA7}
845F: A5 06           LDA     <$06                ; {ram.0006}
8461: F0 0B           BEQ     $846E               ; {}
8463: BD 4F 03        LDA     $034F,X             ; {ram.034F}
8466: C9 2B           CMP     #$2B                ; 
8468: D0 05           BNE     $846F               ; {}
846A: A9 10           LDA     #$10                ; 
846C: 85 4C           STA     <$4C                ; {ram.004C}
846E: 60              RTS                         ; 
846F: 38              SEC                         ; 
8470: E9 2C           SBC     #$2C                ; 
8472: 8D 2E 05        STA     $052E               ; {ram.052E}
8475: 60              RTS                         ; 
8476: 20 89 FA        JSR     $FA89               ; 
8479: 20 72 FA        JSR     $FA72               ; 
847C: A9 00           LDA     #$00                ; 
847E: 4C DF 77        JMP     $77DF               ; {ram.77DF}
8481: AD 6C 06        LDA     $066C               ; {ram.066C}
8484: 0D 06 05        ORA     $0506               ; {ram.0506}
8487: D0 06           BNE     $848F               ; {}
8489: 20 A1 84        JSR     $84A1               ; {}
848C: 20 88 B2        JSR     $B288               ; {}
848F: 20 93 FA        JSR     $FA93               ; 
8492: BD 37 04        LDA     $0437,X             ; {ram.0437}
8495: 29 02           AND     #$02                ; 
8497: 4A              LSR     A                   ; 
8498: 20 DB 77        JSR     $77DB               ; {ram.77DB}
849B: 20 D0 79        JSR     $79D0               ; {ram.79D0}
849E: 4C E4 EE        JMP     $EEE4               ; 
84A1: BD 44 04        LDA     $0444,X             ; 
84A4: 20 E2 E5        JSR     $E5E2               ; 
84A7: 66 B2           ROR     <$B2                ; {ram.00B2}
84A9: B3                              ;
84AA: 84 08           STY     <$08                ; {ram.0008}
84AC: B3                              ;
84AD: 78              SEI                         ; 
84AE: B3                              ;
84AF: 60              RTS                         ; 
84B0: B2                              ;
84B1: 56 B2           LSR     $B2,X               ; {ram.00B2}
84B3: A0 02           LDY     #$02                ; 
84B5: B5 19           LDA     $19,X               ; {ram.0019}
84B7: C9 A0           CMP     #$A0                ; 
84B9: B0 06           BCS     $84C1               ; {}
84BB: C8              INY                         ; 
84BC: C9 20           CMP     #$20                ; 
84BE: B0 01           BCS     $84C1               ; {}
84C0: C8              INY                         ; 
84C1: 98              TYA                         ; 
84C2: 9D 44 04        STA     $0444,X             ; 
84C5: A9 06           LDA     #$06                ; 
84C7: 9D 2C 04        STA     $042C,X             ; {ram.!SplashMode}
84CA: 60              RTS                         ; 
84CB: 20 E1 84        JSR     $84E1               ; {}
84CE: 20 2C 85        JSR     $852C               ; {}
84D1: 20 93 FA        JSR     $FA93               ; 
84D4: A0 00           LDY     #$00                ; 
84D6: A5 15           LDA     <$15                ; {ram.0015}
84D8: 29 08           AND     #$08                ; 
84DA: D0 01           BNE     $84DD               ; {}
84DC: C8              INY                         ; 
84DD: 98              TYA                         ; 
84DE: 4C DB 77        JMP     $77DB               ; {ram.77DB}
84E1: B5 AC           LDA     $AC,X               ; {ram.00AC}
84E3: 20 E2 E5        JSR     $E5E2               ; 
84E6: EC 84 F1        CPX     $F184               ; 
84E9: 84 F9           STY     <$F9                ; {ram.00F9}
84EB: 84 A9           STY     <$A9                ; {ram.00A9}
84ED: 18              CLC                         ; 
84EE: 4C C8 85        JMP     $85C8               ; {}
84F1: 20 FE 85        JSR     $85FE               ; {}
84F4: 90 02           BCC     $84F8               ; {}
84F6: F6 AC           INC     $AC,X               ; {ram.00AC}
84F8: 60              RTS                         ; 
84F9: EE 4E 03        INC     $034E               ; {ram.034E}
84FC: 20 B1 FE        JSR     $FEB1               ; 
84FF: 20 19 85        JSR     $8519               ; {}
8502: B5 98           LDA     $98,X               ; {ram.0098}
8504: C9 04           CMP     #$04                ; 
8506: A9 02           LDA     #$02                ; 
8508: B0 02           BCS     $850C               ; {}
850A: A9 08           LDA     #$08                ; 
850C: 99 98 00        STA     $0098,Y             ; {ram.0098}
850F: 48              PHA                         ; 
8510: 20 19 85        JSR     $8519               ; {}
8513: 68              PLA                         ; 
8514: 4A              LSR     A                   ; 
8515: 99 98 00        STA     $0098,Y             ; {ram.0098}
8518: 60              RTS                         ; 
8519: A9 14           LDA     #$14                ; 
851B: 85 00           STA     <$00                ; {ram.GP_00}
851D: 20 80 B1        JSR     $B180               ; {}
8520: A9 00           LDA     #$00                ; 
8522: 99 AC 00        STA     $00AC,Y             ; {ram.00AC}
8525: BD 94 03        LDA     $0394,X             ; {ram.0394}
8528: 99 94 03        STA     $0394,Y             ; {ram.0394}
852B: 60              RTS                         ; 
852C: B5 AC           LDA     $AC,X               ; {ram.00AC}
852E: D0 30           BNE     $8560               ; {}
8530: 20 29 86        JSR     $8629               ; {}
8533: BD 05 04        LDA     $0405,X             ; {ram.0405}
8536: D0 28           BNE     $8560               ; {}
8538: BD F0 04        LDA     $04F0,X             ; {ram.04F0}
853B: F0 23           BEQ     $8560               ; {}
853D: A0 00           LDY     #$00                ; 
853F: B5 84           LDA     $84,X               ; {ram.0084}
8541: 29 0F           AND     #$0F                ; 
8543: C9 0D           CMP     #$0D                ; 
8545: D0 02           BNE     $8549               ; {}
8547: A0 03           LDY     #$03                ; 
8549: 84 00           STY     <$00                ; {ram.GP_00}
854B: A0 00           LDY     #$00                ; 
854D: B5 70           LDA     $70,X               ; {ram.0070}
854F: 29 0F           AND     #$0F                ; 
8551: D0 02           BNE     $8555               ; {}
8553: A0 0C           LDY     #$0C                ; 
8555: 98              TYA                         ; 
8556: 05 00           ORA     <$00                ; {ram.GP_00}
8558: 25 98           AND     <$98                ; {ram.0098}
855A: D0 02           BNE     $855E               ; {}
855C: F6 AC           INC     $AC,X               ; {ram.00AC}
855E: F6 AC           INC     $AC,X               ; {ram.00AC}
8560: 60              RTS                         ; 
8561: A9 02           LDA     #$02                ; 
8563: 95 AC           STA     $AC,X               ; {ram.00AC}
8565: 4C 25 80        JMP     $8025               ; {}
8568: 20 8F 85        JSR     $858F               ; {}
856B: 20 29 86        JSR     $8629               ; {}
856E: B5 70           LDA     $70,X               ; {ram.0070}
8570: 48              PHA                         ; 
8571: 18              CLC                         ; 
8572: 69 04           ADC     #$04                ; 
8574: 95 70           STA     $70,X               ; {ram.0070}
8576: 20 93 FA        JSR     $FA93               ; 
8579: A0 00           LDY     #$00                ; 
857B: A5 15           LDA     <$15                ; {ram.0015}
857D: 29 02           AND     #$02                ; 
857F: D0 01           BNE     $8582               ; {}
8581: C8              INY                         ; 
8582: A9 03           LDA     #$03                ; 
8584: 20 88 79        JSR     $7988               ; {ram.7988}
8587: 98              TYA                         ; 
8588: 20 DF 77        JSR     $77DF               ; {ram.77DF}
858B: 68              PLA                         ; 
858C: 95 70           STA     $70,X               ; {ram.0070}
858E: 60              RTS                         ; 
858F: B4 AC           LDY     $AC,X               ; {ram.00AC}
8591: F0 27           BEQ     $85BA               ; {}
8593: 88              DEY                         ; 
8594: D0 30           BNE     $85C6               ; {}
8596: B5 28           LDA     $28,X               ; {ram.0028}
8598: F0 05           BEQ     $859F               ; {}
859A: 20 FE 85        JSR     $85FE               ; {}
859D: 90 1A           BCC     $85B9               ; {}
859F: B5 70           LDA     $70,X               ; {ram.0070}
85A1: 18              CLC                         ; 
85A2: 69 08           ADC     #$08                ; 
85A4: 29 F0           AND     #$F0                ; 
85A6: 95 70           STA     $70,X               ; {ram.0070}
85A8: B5 84           LDA     $84,X               ; {ram.0084}
85AA: 69 08           ADC     #$08                ; 
85AC: 29 F0           AND     #$F0                ; 
85AE: 09 0D           ORA     #$0D                ; 
85B0: 95 84           STA     $84,X               ; {ram.0084}
85B2: A9 00           LDA     #$00                ; 
85B4: 9D 94 03        STA     $0394,X             ; {ram.0394}
85B7: F6 AC           INC     $AC,X               ; {ram.00AC}
85B9: 60              RTS                         ; 
85BA: A9 20           LDA     #$20                ; 
85BC: 9D BC 03        STA     $03BC,X             ; {ram.03BC}
85BF: A9 05           LDA     #$05                ; 
85C1: 95 28           STA     $28,X               ; {ram.0028}
85C3: F6 AC           INC     $AC,X               ; {ram.00AC}
85C5: 60              RTS                         ; 
85C6: A9 40           LDA     #$40                ; 
85C8: 9D BC 03        STA     $03BC,X             ; {ram.03BC}
85CB: B5 28           LDA     $28,X               ; {ram.0028}
85CD: C9 05           CMP     #$05                ; 
85CF: B0 24           BCS     $85F5               ; {}
85D1: A9 20           LDA     #$20                ; 
85D3: 9D 1F 04        STA     $041F,X             ; {ram.041F}
85D6: 20 94 80        JSR     $8094               ; {}
85D9: BD 94 03        LDA     $0394,X             ; {ram.0394}
85DC: 15 28           ORA     $28,X               ; {ram.0028}
85DE: D0 15           BNE     $85F5               ; {}
85E0: B5 18           LDA     $18,X               ; {ram.0018}
85E2: 29 03           AND     #$03                ; 
85E4: A8              TAY                         ; 
85E5: BD 4F 03        LDA     $034F,X             ; {ram.034F}
85E8: C9 13           CMP     #$13                ; 
85EA: F0 04           BEQ     $85F0               ; {}
85EC: C8              INY                         ; 
85ED: C8              INY                         ; 
85EE: C8              INY                         ; 
85EF: C8              INY                         ; 
85F0: B9 F6 85        LDA     $85F6,Y             ; {}
85F3: 95 28           STA     $28,X               ; {ram.0028}
85F5: 60              RTS                         ; 
85F6: 18              CLC                         ; 
85F7: 28              PLP                         ; 
85F8: 38              SEC                         ; 
85F9: 48              PHA                         ; 
85FA: 08              PHP                         ; 
85FB: 18              CLC                         ; 
85FC: 28              PLP                         ; 
85FD: 38              SEC                         ; 
85FE: A9 FF           LDA     #$FF                ; 
8600: 9D BC 03        STA     $03BC,X             ; {ram.03BC}
8603: B5 98           LDA     $98,X               ; {ram.0098}
8605: 85 0F           STA     <$0F                ; {ram.000F}
8607: BD 94 03        LDA     $0394,X             ; {ram.0394}
860A: D0 08           BNE     $8614               ; {}
860C: 20 FA ED        JSR     $EDFA               ; 
860F: CD 4A 03        CMP     $034A               ; {ram.034A}
8612: B0 14           BCS     $8628               ; {}
8614: 20 B8 6F        JSR     $6FB8               ; {ram.6FB8}
8617: 38              SEC                         ; 
8618: F0 0E           BEQ     $8628               ; {}
861A: 20 8D F0        JSR     $F08D               ; 
861D: BD 94 03        LDA     $0394,X             ; {ram.0394}
8620: 29 0F           AND     #$0F                ; 
8622: 18              CLC                         ; 
8623: D0 03           BNE     $8628               ; {}
8625: 9D 94 03        STA     $0394,X             ; {ram.0394}
8628: 60              RTS                         ; 
8629: B5 70           LDA     $70,X               ; {ram.0070}
862B: 85 02           STA     <$02                ; {ram.GP_02}
862D: B5 84           LDA     $84,X               ; {ram.0084}
862F: 85 03           STA     <$03                ; {ram.GP_03}
8631: 4C D0 79        JMP     $79D0               ; {ram.79D0}
8634: 24 23           BIT     <$23                ; {ram.0023}
8636: 03                              ;
8637: 01 01           ORA     ($01,X)             ; {ram.GP_01}
8639: 50 80           BVC     $85BB               ; {}
863B: F0 60           BEQ     $869D               ; {}
863D: 00              BRK                         ; 
863E: 04                              ;
863F: 06 24           ASL     <$24                ; {ram.0024}
8641: C8              INY                         ; 
8642: 24 C8           BIT     <$C8                ; {ram.00C8}
8644: 64                              ;
8645: 88              DEY                         ; 
8646: 48              PHA                         ; 
8647: A8              TAY                         ; 
8648: C0 BC           CPY     #$BC                ; 
864A: 64                              ;
864B: 5C                              ;
864C: 94 8C           STY     $8C,X               ; {ram.008C}
864E: 82                              ;
864F: 86 A0           STX     <$A0                ; {ram.00A0}
8651: 02                              ;
8652: AD CC 04        LDA     $04CC               ; {ram.04CC}
8655: D0 0E           BNE     $8665               ; {}
8657: 20 5A E8        JSR     $E85A               ; 
865A: A0 01           LDY     #$01                ; 
865C: D9 34 86        CMP     $8634,Y             ; {}
865F: F0 04           BEQ     $8665               ; {}
8661: 88              DEY                         ; 
8662: 10 F8           BPL     $865C               ; {}
8664: 60              RTS                         ; 
8665: 98              TYA                         ; 
8666: 48              PHA                         ; 
8667: 20 BB FE        JSR     $FEBB               ; 
866A: C9 01           CMP     #$01                ; 
866C: 68              PLA                         ; 
866D: B0 6D           BCS     $86DC               ; {}
866F: C0 06           CPY     #$06                ; 
8671: 90 69           BCC     $86DC               ; {}
8673: 84 0A           STY     <$0A                ; {ram.000A}
8675: 85 0B           STA     <$0B                ; {ram.000B}
8677: A8              TAY                         ; 
8678: BE 36 86        LDX     $8636,Y             ; {}
867B: BC E8 04        LDY     $04E8,X             ; 
867E: 88              DEY                         ; 
867F: 98              TYA                         ; 
8680: 9D E8 04        STA     $04E8,X             ; 
8683: C8              INY                         ; 
8684: D0 53           BNE     $86D9               ; {}
8686: B5 18           LDA     $18,X               ; {ram.0018}
8688: C9 F0           CMP     #$F0                ; 
868A: B0 4D           BCS     $86D9               ; {}
868C: 29 03           AND     #$03                ; 
868E: A8              TAY                         ; 
868F: B9 39 86        LDA     $8639,Y             ; {}
8692: 9D E8 04        STA     $04E8,X             ; 
8695: A4 0B           LDY     <$0B                ; {ram.000B}
8697: 8A              TXA                         ; 
8698: 18              CLC                         ; 
8699: 79 3D 86        ADC     $863D,Y             ; {}
869C: A8              TAY                         ; 
869D: 8A              TXA                         ; 
869E: 48              PHA                         ; 
869F: A2 00           LDX     #$00                ; 
86A1: 20 93 FA        JSR     $FA93               ; 
86A4: A6 0A           LDX     <$0A                ; {ram.000A}
86A6: B9 40 86        LDA     $8640,Y             ; {}
86A9: 85 02           STA     <$02                ; {ram.GP_02}
86AB: 95 70           STA     $70,X               ; {ram.0070}
86AD: B9 48 86        LDA     $8648,Y             ; {}
86B0: 85 03           STA     <$03                ; {ram.GP_03}
86B2: 95 84           STA     $84,X               ; {ram.0084}
86B4: A9 03           LDA     #$03                ; 
86B6: 85 04           STA     <$04                ; {ram.0004}
86B8: A0 01           LDY     #$01                ; 
86BA: B9 00 00        LDA     $0000,Y             ; {ram.GP_00}
86BD: 38              SEC                         ; 
86BE: F9 02 00        SBC     $0002,Y             ; {ram.GP_02}
86C1: C9 18           CMP     #$18                ; 
86C3: 10 06           BPL     $86CB               ; {}
86C5: C9 E8           CMP     #$E8                ; 
86C7: 30 02           BMI     $86CB               ; {}
86C9: 46 04           LSR     <$04                ; {ram.0004}
86CB: 88              DEY                         ; 
86CC: 10 EC           BPL     $86BA               ; {}
86CE: A5 04           LDA     <$04                ; {ram.0004}
86D0: F0 05           BEQ     $86D7               ; {}
86D2: A9 55           LDA     #$55                ; 
86D4: 20 AF 82        JSR     $82AF               ; {}
86D7: 68              PLA                         ; 
86D8: AA              TAX                         ; 
86D9: CA              DEX                         ; 
86DA: 10 9F           BPL     $867B               ; {}
86DC: 60              RTS                         ; 
86DD: FF                              ;
86DE: FF                              ;
86DF: FF                              ;
86E0: A4 EB           LDY     <$EB                ; {ram.00EB}
86E2: B9 7E 68        LDA     $687E,Y             ; 
86E5: 29 08           AND     #$08                ; 
86E7: F0 49           BEQ     $8732               ; {}
86E9: AD 14 05        LDA     $0514               ; {ram.0514}
86EC: D0 44           BNE     $8732               ; {}
86EE: 20 BB FE        JSR     $FEBB               ; 
86F1: F0 3F           BEQ     $8732               ; {}
86F3: A9 0D           LDA     #$0D                ; 
86F5: 85 0D           STA     <$0D                ; {ram.000D}
86F7: A6 59           LDX     <$59                ; {ram.0059}
86F9: A4 0D           LDY     <$0D                ; {ram.000D}
86FB: B9 18 00        LDA     $0018,Y             ; {ram.0018}
86FE: 29 F0           AND     #$F0                ; 
8700: 95 70           STA     $70,X               ; {ram.0070}
8702: F0 2A           BEQ     $872E               ; {}
8704: C9 F0           CMP     #$F0                ; 
8706: F0 26           BEQ     $872E               ; {}
8708: B9 18 00        LDA     $0018,Y             ; {ram.0018}
870B: 0A              ASL     A                   ; 
870C: 0A              ASL     A                   ; 
870D: 0A              ASL     A                   ; 
870E: 0A              ASL     A                   ; 
870F: C9 50           CMP     #$50                ; 
8711: 90 1B           BCC     $872E               ; {}
8713: C9 E0           CMP     #$E0                ; 
8715: B0 17           BCS     $872E               ; {}
8717: 09 0D           ORA     #$0D                ; 
8719: 95 84           STA     $84,X               ; {ram.0084}
871B: 20 F4 ED        JSR     $EDF4               ; 
871E: C9 8D           CMP     #$8D                ; 
8720: 90 0C           BCC     $872E               ; {}
8722: C9 99           CMP     #$99                ; 
8724: B0 08           BCS     $872E               ; {}
8726: EE 14 05        INC     $0514               ; {ram.0514}
8729: A9 11           LDA     #$11                ; 
872B: 4C B3 FE        JMP     $FEB3               ; 
872E: C6 0D           DEC     <$0D                ; {ram.000D}
8730: D0 C7           BNE     $86F9               ; {}
8732: 60              RTS                         ; 
8733: 01 02           ORA     ($02,X)             ; {ram.GP_02}
8735: 05 0A           ORA     <$0A                ; {ram.000A}
8737: A9 00           LDA     #$00                ; 
8739: 8D 15 05        STA     $0515               ; {ram.0515}
873C: 20 D6 FE        JSR     $FED6               ; 
873F: B5 19           LDA     $19,X               ; {ram.0019}
8741: 29 03           AND     #$03                ; 
8743: A8              TAY                         ; 
8744: B9 33 87        LDA     $8733,Y             ; {}
8747: 95 98           STA     $98,X               ; {ram.0098}
8749: 0A              ASL     A                   ; 
874A: 0A              ASL     A                   ; 
874B: 95 28           STA     $28,X               ; {ram.0028}
874D: 60              RTS                         ; 
874E: A9 05           LDA     #$05                ; 
8750: 85 4D           STA     <$4D                ; {ram.004D}
8752: 20 D6 FE        JSR     $FED6               ; 
8755: A9 20           LDA     #$20                ; 
8757: D0 02           BNE     $875B               ; {}
8759: A9 30           LDA     #$30                ; 
875B: 9D BC 03        STA     $03BC,X             ; {ram.03BC}
875E: E8              INX                         ; 
875F: 8A              TXA                         ; 
8760: CA              DEX                         ; 
8761: 0A              ASL     A                   ; 
8762: 0A              ASL     A                   ; 
8763: 0A              ASL     A                   ; 
8764: 0A              ASL     A                   ; 
8765: 95 28           STA     $28,X               ; {ram.0028}
8767: 20 55 F8        JSR     $F855               ; 
876A: 9D E4 03        STA     $03E4,X             ; {ram.03E4}
876D: A9 06           LDA     #$06                ; 
876F: 9D D0 03        STA     $03D0,X             ; {ram.03D0}
8772: 4C 25 80        JMP     $8025               ; {}
8775: 20 D6 FE        JSR     $FED6               ; 
8778: A9 08           LDA     #$08                ; 
877A: 95 98           STA     $98,X               ; {ram.0098}
877C: 20 0B B2        JSR     $B20B               ; {}
877F: A9 A0           LDA     #$A0                ; 
8781: 8D D1 04        STA     $04D1               ; {ram.04D1}
8784: A9 1F           LDA     #$1F                ; 
8786: 9D 1F 04        STA     $041F,X             ; {ram.041F}
8789: 60              RTS                         ; 
878A: A9 08           LDA     #$08                ; 
878C: 8D 02 06        STA     $0602               ; {ram.SND_ReqMusEff}
878F: A9 78           LDA     #$78                ; 
8791: 95 70           STA     $70,X               ; {ram.0070}
8793: A9 7D           LDA     #$7D                ; 
8795: 95 84           STA     $84,X               ; {ram.0084}
8797: 60              RTS                         ; 
8798: AD 6C 06        LDA     $066C               ; {ram.066C}
879B: D0 FA           BNE     $8797               ; {}
879D: 20 6D 8A        JSR     $8A6D               ; {}
87A0: B5 AC           LDA     $AC,X               ; {ram.00AC}
87A2: C9 03           CMP     #$03                ; 
87A4: D0 0F           BNE     $87B5               ; {}
87A6: B5 28           LDA     $28,X               ; {ram.0028}
87A8: C9 FD           CMP     #$FD                ; 
87AA: D0 09           BNE     $87B5               ; {}
87AC: A9 55           LDA     #$55                ; 
87AE: 20 AF 82        JSR     $82AF               ; {}
87B1: A9 20           LDA     #$20                ; 
87B3: 95 28           STA     $28,X               ; {ram.0028}
87B5: B5 AC           LDA     $AC,X               ; {ram.00AC}
87B7: D0 DE           BNE     $8797               ; {}
87B9: CE 14 05        DEC     $0514               ; {ram.0514}
87BC: 4C B1 FE        JMP     $FEB1               ; 
87BF: A9 A0           LDA     #$A0                ; 
87C1: 9D 1F 04        STA     $041F,X             ; {ram.041F}
87C4: 20 94 80        JSR     $8094               ; {}
87C7: A0 5B           LDY     #$5B                ; 
87C9: 4C D1 87        JMP     $87D1               ; {}
87CC: 20 19 81        JSR     $8119               ; {}
87CF: A0 57           LDY     #$57                ; 
87D1: A9 20           LDA     #$20                ; 
87D3: 85 01           STA     <$01                ; {ram.GP_01}
87D5: BD 4F 03        LDA     $034F,X             ; {ram.034F}
87D8: C9 03           CMP     #$03                ; 
87DA: F0 17           BEQ     $87F3               ; {}
87DC: C9 01           CMP     #$01                ; 
87DE: F0 13           BEQ     $87F3               ; {}
87E0: C9 09           CMP     #$09                ; 
87E2: F0 0F           BEQ     $87F3               ; {}
87E4: C9 0A           CMP     #$0A                ; 
87E6: F0 0B           BEQ     $87F3               ; {}
87E8: BD 51 04        LDA     $0451,X             ; 
87EB: D0 06           BNE     $87F3               ; {}
87ED: B5 18           LDA     $18,X               ; {ram.0018}
87EF: C9 F8           CMP     #$F8                ; 
87F1: 90 3E           BCC     $8831               ; {}
87F3: A5 01           LDA     <$01                ; {ram.GP_01}
87F5: 84 00           STY     <$00                ; {ram.GP_00}
87F7: 48              PHA                         ; 
87F8: A0 00           LDY     #$00                ; 
87FA: BD F0 04        LDA     $04F0,X             ; {ram.04F0}
87FD: D0 0D           BNE     $880C               ; {}
87FF: BC 51 04        LDY     $0451,X             ; 
8802: 88              DEY                         ; 
8803: 10 07           BPL     $880C               ; {}
8805: BD 12 04        LDA     $0412,X             ; {ram.0412}
8808: F0 23           BEQ     $882D               ; {}
880A: A0 30           LDY     #$30                ; 
880C: 98              TYA                         ; 
880D: 9D 51 04        STA     $0451,X             ; 
8810: F0 1B           BEQ     $882D               ; {}
8812: C0 10           CPY     #$10                ; 
8814: D0 13           BNE     $8829               ; {}
8816: AD 6C 06        LDA     $066C               ; {ram.066C}
8819: 15 3D           ORA     $3D,X               ; {ram.003D}
881B: D0 0C           BNE     $8829               ; {}
881D: A5 00           LDA     <$00                ; {ram.GP_00}
881F: 20 32 88        JSR     $8832               ; {}
8822: 90 09           BCC     $882D               ; {}
8824: A9 00           LDA     #$00                ; 
8826: 9D 12 04        STA     $0412,X             ; {ram.0412}
8829: 68              PLA                         ; 
882A: A9 00           LDA     #$00                ; 
882C: 48              PHA                         ; 
882D: 68              PLA                         ; 
882E: 9D BC 03        STA     $03BC,X             ; {ram.03BC}
8831: 60              RTS                         ; 
8832: 20 79 B1        JSR     $B179               ; {}
8835: 90 07           BCC     $883E               ; {}
8837: A9 80           LDA     #$80                ; 
8839: 95 28           STA     $28,X               ; {ram.0028}
883B: DE 37 04        DEC     $0437,X             ; {ram.0437}
883E: 60              RTS                         ; 
883F: A9 80           LDA     #$80                ; 
8841: 9D BC 03        STA     $03BC,X             ; {ram.03BC}
8844: B5 28           LDA     $28,X               ; {ram.0028}
8846: D0 14           BNE     $885C               ; {}
8848: BD AC 00        LDA     $00AC,X             ; {ram.00AC}
884B: 29 F0           AND     #$F0                ; 
884D: C9 20           CMP     #$20                ; 
884F: F0 18           BEQ     $8869               ; {}
8851: C9 10           CMP     #$10                ; 
8853: D0 2A           BNE     $887F               ; {}
8855: B5 98           LDA     $98,X               ; {ram.0098}
8857: 85 0F           STA     <$0F                ; {ram.000F}
8859: 4C 69 88        JMP     $8869               ; {}
885C: BC 2C 04        LDY     $042C,X             ; {ram.!SplashMode}
885F: B9 4F 03        LDA     $034F,Y             ; {ram.034F}
8862: D0 02           BNE     $8866               ; {}
8864: 95 28           STA     $28,X               ; {ram.0028}
8866: 4C 7B F5        JMP     $F57B               ; 
8869: 20 19 F5        JSR     $F519               ; 
886C: BD AC 00        LDA     $00AC,X             ; {ram.00AC}
886F: 29 F0           AND     #$F0                ; 
8871: C9 10           CMP     #$10                ; 
8873: D0 0A           BNE     $887F               ; {}
8875: 20 71 83        JSR     $8371               ; {}
8878: A5 06           LDA     <$06                ; {ram.0006}
887A: F0 C2           BEQ     $883E               ; {}
887C: 4C 46 83        JMP     $8346               ; {}
887F: C9 30           CMP     #$30                ; 
8881: D0 BB           BNE     $883E               ; {}
8883: 4C 4C 83        JMP     $834C               ; {}
8886: B5 28           LDA     $28,X               ; {ram.0028}
8888: D0 3F           BNE     $88C9               ; {}
888A: AD 15 05        LDA     $0515               ; {ram.0515}
888D: C9 03           CMP     #$03                ; 
888F: F0 31           BEQ     $88C2               ; {}
8891: 20 BB FE        JSR     $FEBB               ; 
8894: F0 33           BEQ     $88C9               ; {}
8896: A6 59           LDX     <$59                ; {ram.0059}
8898: EE 15 05        INC     $0515               ; {ram.0515}
889B: A9 20           LDA     #$20                ; 
889D: 20 B3 FE        JSR     $FEB3               ; 
88A0: B5 19           LDA     $19,X               ; {ram.0019}
88A2: A4 61           LDY     <$61                ; {ram.0061}
88A4: C0 80           CPY     #$80                ; 
88A6: B0 05           BCS     $88AD               ; {}
88A8: 29 7F           AND     #$7F                ; 
88AA: 4C AF 88        JMP     $88AF               ; {}
88AD: 09 80           ORA     #$80                ; 
88AF: 95 70           STA     $70,X               ; {ram.0070}
88B1: A9 40           LDA     #$40                ; 
88B3: 95 84           STA     $84,X               ; {ram.0084}
88B5: AE 40 03        LDX     $0340               ; {ram.0340}
88B8: A9 08           LDA     #$08                ; 
88BA: 18              CLC                         ; 
88BB: 75 19           ADC     <$19,X              ; {ram.0019}
88BD: 29 1F           AND     #$1F                ; 
88BF: 95 28           STA     $28,X               ; {ram.0028}
88C1: 60              RTS                         ; 
88C2: B5 28           LDA     $28,X               ; {ram.0028}
88C4: 18              CLC                         ; 
88C5: 75 19           ADC     <$19,X              ; {ram.0019}
88C7: 95 28           STA     $28,X               ; {ram.0028}
88C9: 60              RTS                         ; 
88CA: 00              BRK                         ; 
88CB: 00              BRK                         ; 
88CC: 00              BRK                         ; 
88CD: 00              BRK                         ; 
88CE: 00              BRK                         ; 
88CF: 20 20 00        JSR     $0020               ; {ram.0020}
88D2: 00              BRK                         ; 
88D3: E0 E0           CPX     #$E0                ; 
88D5: 00              BRK                         ; 
88D6: 40              RTI                         ; 
88D7: 40              RTI                         ; 
88D8: 00              BRK                         ; 
88D9: 00              BRK                         ; 
88DA: 40              RTI                         ; 
88DB: 40              RTI                         ; 
88DC: 00              BRK                         ; 
88DD: 00              BRK                         ; 
88DE: 30 30           BMI     $8910               ; {}
88E0: 00              BRK                         ; 
88E1: 80                              ;
88E2: 80                              ;
88E3: 00              BRK                         ; 
88E4: 00              BRK                         ; 
88E5: 80                              ;
88E6: 80                              ;
88E7: 00              BRK                         ; 
88E8: 00              BRK                         ; 
88E9: 50 50           BVC     $893B               ; {}
88EB: 60              RTS                         ; 
88EC: 60              RTS                         ; 
88ED: 60              RTS                         ; 
88EE: 60              RTS                         ; 
88EF: 60              RTS                         ; 
88F0: 60              RTS                         ; 
88F1: 60              RTS                         ; 
88F2: FD FC FE        SBC     $FEFC,X             ; 
88F5: 00              BRK                         ; 
88F6: 0B                              ;
88F7: 16 B5           ASL     $B5,X               ; {ram.00B5}
88F9: C0 F0           CPY     #$F0                ; 
88FB: 06 4C           ASL     <$4C                ; {ram.004C}
88FD: B8              CLV                         ; 
88FE: EE 4C CB        INC     $CB4C               ; 
8901: 89                              ;
8902: AD 6C 06        LDA     $066C               ; {ram.066C}
8905: 15 3D           ORA     $3D,X               ; {ram.003D}
8907: D0 F6           BNE     $88FF               ; {}
8909: B5 AC           LDA     $AC,X               ; {ram.00AC}
890B: D0 4C           BNE     $8959               ; {}
890D: B5 28           LDA     $28,X               ; {ram.0028}
890F: D0 45           BNE     $8956               ; {}
8911: 20 1A B3        JSR     $B31A               ; {}
8914: B5 98           LDA     $98,X               ; {ram.0098}
8916: 29 03           AND     #$03                ; 
8918: D0 0E           BNE     $8928               ; {}
891A: A0 02           LDY     #$02                ; 
891C: A5 61           LDA     <$61                ; {ram.0061}
891E: D5 70           CMP     $70,X               ; {ram.0070}
8920: 90 01           BCC     $8923               ; {}
8922: 88              DEY                         ; 
8923: 98              TYA                         ; 
8924: 15 98           ORA     $98,X               ; {ram.0098}
8926: 95 98           STA     $98,X               ; {ram.0098}
8928: F6 AC           INC     $AC,X               ; {ram.00AC}
892A: BD 51 04        LDA     $0451,X             ; 
892D: C9 02           CMP     #$02                ; 
892F: 90 0B           BCC     $893C               ; {}
8931: B5 98           LDA     $98,X               ; {ram.0098}
8933: 49 03           EOR     #$03                ; 
8935: 95 98           STA     $98,X               ; {ram.0098}
8937: A9 00           LDA     #$00                ; 
8939: 9D 51 04        STA     $0451,X             ; 
893C: 20 11 8A        JSR     $8A11               ; {}
893F: B4 98           LDY     $98,X               ; {ram.0098}
8941: B5 84           LDA     $84,X               ; {ram.0084}
8943: 18              CLC                         ; 
8944: 79 CA 88        ADC     $88CA,Y             ; {}
8947: 9D 44 04        STA     $0444,X             ; 
894A: 20 03 8A        JSR     $8A03               ; {}
894D: B9 F2 88        LDA     $88F2,Y             ; {}
8950: 9D 12 04        STA     $0412,X             ; {ram.0412}
8953: 20 4D 8A        JSR     $8A4D               ; {}
8956: 4C CB 89        JMP     $89CB               ; {}
8959: 20 CD B2        JSR     $B2CD               ; {}
895C: A5 0F           LDA     <$0F                ; {ram.000F}
895E: D0 06           BNE     $8966               ; {}
8960: FE 51 04        INC     $0451,X             ; 
8963: 4C 2A 89        JMP     $892A               ; {}
8966: 20 11 8A        JSR     $8A11               ; {}
8969: A9 00           LDA     #$00                ; 
896B: 9D 51 04        STA     $0451,X             ; 
896E: 20 03 8A        JSR     $8A03               ; {}
8971: B9 F5 88        LDA     $88F5,Y             ; {}
8974: 18              CLC                         ; 
8975: 75 98           ADC     <$98,X              ; {ram.0098}
8977: A8              TAY                         ; 
8978: B9 D5 88        LDA     $88D5,Y             ; {}
897B: A0 02           LDY     #$02                ; 
897D: 20 21 8A        JSR     $8A21               ; {}
8980: A0 FF           LDY     #$FF                ; 
8982: B5 98           LDA     $98,X               ; {ram.0098}
8984: 29 02           AND     #$02                ; 
8986: D0 02           BNE     $898A               ; {}
8988: A0 01           LDY     #$01                ; 
898A: 98              TYA                         ; 
898B: 18              CLC                         ; 
898C: 75 70           ADC     <$70,X              ; {ram.0070}
898E: 95 70           STA     $70,X               ; {ram.0070}
8990: BD 12 04        LDA     $0412,X             ; {ram.0412}
8993: 30 36           BMI     $89CB               ; {}
8995: B5 84           LDA     $84,X               ; {ram.0084}
8997: 38              SEC                         ; 
8998: FD 44 04        SBC     $0444,X             ; 
899B: 20 1F 70        JSR     $701F               ; {ram.701F}
899E: C9 03           CMP     #$03                ; 
89A0: B0 29           BCS     $89CB               ; {}
89A2: 20 55 F8        JSR     $F855               ; 
89A5: BC 4F 03        LDY     $034F,X             ; {ram.034F}
89A8: C0 20           CPY     #$20                ; 
89AA: F0 1D           BEQ     $89C9               ; {}
89AC: A9 10           LDA     #$10                ; 
89AE: 18              CLC                         ; 
89AF: 75 19           ADC     <$19,X              ; {ram.0019}
89B1: C9 20           CMP     #$20                ; 
89B3: B0 03           BCS     $89B8               ; {}
89B5: 38              SEC                         ; 
89B6: E9 40           SBC     #$40                ; 
89B8: BC 4F 03        LDY     $034F,X             ; {ram.034F}
89BB: C0 0D           CPY     #$0D                ; 
89BD: F0 0A           BEQ     $89C9               ; {}
89BF: 29 7F           AND     #$7F                ; 
89C1: B4 19           LDY     $19,X               ; {ram.0019}
89C3: C0 A0           CPY     #$A0                ; 
89C5: 90 02           BCC     $89C9               ; {}
89C7: 29 0F           AND     #$0F                ; 
89C9: 95 28           STA     $28,X               ; {ram.0028}
89CB: 20 93 FA        JSR     $FA93               ; 
89CE: 85 0D           STA     <$0D                ; {ram.000D}
89D0: BD 4F 03        LDA     $034F,X             ; {ram.034F}
89D3: C9 20           CMP     #$20                ; 
89D5: F0 15           BEQ     $89EC               ; {}
89D7: B5 AC           LDA     $AC,X               ; {ram.00AC}
89D9: D0 0E           BNE     $89E9               ; {}
89DB: B4 28           LDY     $28,X               ; {ram.0028}
89DD: C0 21           CPY     #$21                ; 
89DF: 90 08           BCC     $89E9               ; {}
89E1: A9 10           LDA     #$10                ; 
89E3: 20 89 FA        JSR     $FA89               ; 
89E6: BD E4 03        LDA     $03E4,X             ; {ram.03E4}
89E9: 4C 65 8C        JMP     $8C65               ; {}
89EC: A9 06           LDA     #$06                ; 
89EE: 20 89 FA        JSR     $FA89               ; 
89F1: BD E4 03        LDA     $03E4,X             ; {ram.03E4}
89F4: 20 AC 8C        JSR     $8CAC               ; {}
89F7: B5 84           LDA     $84,X               ; {ram.0084}
89F9: C9 F0           CMP     #$F0                ; 
89FB: 90 13           BCC     $8A10               ; {}
89FD: CE 15 05        DEC     $0515               ; {ram.0515}
8A00: 4C B1 FE        JMP     $FEB1               ; 
8A03: BD 4F 03        LDA     $034F,X             ; {ram.034F}
8A06: 38              SEC                         ; 
8A07: E9 0D           SBC     #$0D                ; 
8A09: A8              TAY                         ; 
8A0A: C0 02           CPY     #$02                ; 
8A0C: 90 02           BCC     $8A10               ; {}
8A0E: A0 02           LDY     #$02                ; 
8A10: 60              RTS                         ; 
8A11: BD 4F 03        LDA     $034F,X             ; {ram.034F}
8A14: C9 20           CMP     #$20                ; 
8A16: D0 08           BNE     $8A20               ; {}
8A18: B5 98           LDA     $98,X               ; {ram.0098}
8A1A: 29 03           AND     #$03                ; 
8A1C: 09 04           ORA     #$04                ; 
8A1E: 95 98           STA     $98,X               ; {ram.0098}
8A20: 60              RTS                         ; 
8A21: 85 00           STA     <$00                ; {ram.GP_00}
8A23: 84 02           STY     <$02                ; {ram.GP_02}
8A25: BD 12 04        LDA     $0412,X             ; {ram.0412}
8A28: 75 84           ADC     <$84,X              ; {ram.0084}
8A2A: 95 84           STA     $84,X               ; {ram.0084}
8A2C: BD 1F 04        LDA     $041F,X             ; {ram.041F}
8A2F: 18              CLC                         ; 
8A30: 65 00           ADC     <$00                ; {ram.GP_00}
8A32: 9D 1F 04        STA     $041F,X             ; {ram.041F}
8A35: BD 12 04        LDA     $0412,X             ; {ram.0412}
8A38: 69 00           ADC     #$00                ; 
8A3A: 9D 12 04        STA     $0412,X             ; {ram.0412}
8A3D: C5 02           CMP     <$02                ; {ram.GP_02}
8A3F: 30 11           BMI     $8A52               ; {}
8A41: BD 1F 04        LDA     $041F,X             ; {ram.041F}
8A44: C9 80           CMP     #$80                ; 
8A46: 90 0A           BCC     $8A52               ; {}
8A48: A5 02           LDA     <$02                ; {ram.GP_02}
8A4A: 9D 12 04        STA     $0412,X             ; {ram.0412}
8A4D: A9 00           LDA     #$00                ; 
8A4F: 9D 1F 04        STA     $041F,X             ; {ram.041F}
8A52: 60              RTS                         ; 
8A53: 08              PHP                         ; 
8A54: 0A              ASL     A                   ; 
8A55: 10 20           BPL     $8A77               ; {}
8A57: 10 0A           BPL     $8A63               ; {}
8A59: 80                              ;
8A5A: 20 0F FF        JSR     $FF0F               ; 
8A5D: 10 60           BPL     $8ABF               ; {}
8A5F: 10 0B           BPL     $8A6C               ; {}
8A61: 01 05           ORA     ($05,X)             ; {ram.0005}
8A63: 01 0B           ORA     ($0B,X)             ; {ram.000B}
8A65: A9 A0           LDA     #$A0                ; 
8A67: 9D 1F 04        STA     $041F,X             ; {ram.041F}
8A6A: 20 94 80        JSR     $8094               ; {}
8A6D: B5 28           LDA     $28,X               ; {ram.0028}
8A6F: D0 30           BNE     $8AA1               ; {}
8A71: BD 4F 03        LDA     $034F,X             ; {ram.034F}
8A74: C9 11           CMP     #$11                ; 
8A76: D0 10           BNE     $8A88               ; {}
8A78: B4 AC           LDY     $AC,X               ; {ram.00AC}
8A7A: 88              DEY                         ; 
8A7B: D0 0B           BNE     $8A88               ; {}
8A7D: A0 03           LDY     #$03                ; 
8A7F: B5 84           LDA     $84,X               ; {ram.0084}
8A81: C5 84           CMP     <$84                ; {ram.0084}
8A83: B0 01           BCS     $8A86               ; {}
8A85: 88              DEY                         ; 
8A86: 94 98           STY     $98,X               ; {ram.0098}
8A88: B5 AC           LDA     $AC,X               ; {ram.00AC}
8A8A: 18              CLC                         ; 
8A8B: 69 01           ADC     #$01                ; 
8A8D: C9 06           CMP     #$06                ; 
8A8F: 90 02           BCC     $8A93               ; {}
8A91: A9 00           LDA     #$00                ; 
8A93: 95 AC           STA     $AC,X               ; {ram.00AC}
8A95: A8              TAY                         ; 
8A96: B9 53 8A        LDA     $8A53,Y             ; {}
8A99: 9D BC 03        STA     $03BC,X             ; {ram.03BC}
8A9C: B9 59 8A        LDA     $8A59,Y             ; {}
8A9F: 95 28           STA     $28,X               ; {ram.0028}
8AA1: B4 AC           LDY     $AC,X               ; {ram.00AC}
8AA3: B9 5F 8A        LDA     $8A5F,Y             ; {}
8AA6: 20 89 FA        JSR     $FA89               ; 
8AA9: B5 AC           LDA     $AC,X               ; {ram.00AC}
8AAB: F0 49           BEQ     $8AF6               ; {}
8AAD: BC 4F 03        LDY     $034F,X             ; {ram.034F}
8AB0: C0 11           CPY     #$11                ; 
8AB2: D0 0E           BNE     $8AC2               ; {}
8AB4: B4 AC           LDY     $AC,X               ; {ram.00AC}
8AB6: C0 02           CPY     #$02                ; 
8AB8: 90 08           BCC     $8AC2               ; {}
8ABA: C0 05           CPY     #$05                ; 
8ABC: B0 04           BCS     $8AC2               ; {}
8ABE: B5 98           LDA     $98,X               ; {ram.0098}
8AC0: D0 08           BNE     $8ACA               ; {}
8AC2: 38              SEC                         ; 
8AC3: E9 01           SBC     #$01                ; 
8AC5: 0A              ASL     A                   ; 
8AC6: 18              CLC                         ; 
8AC7: 7D E4 03        ADC     $03E4,X             ; {ram.03E4}
8ACA: 20 DB 77        JSR     $77DB               ; {ram.77DB}
8ACD: BD 4F 03        LDA     $034F,X             ; {ram.034F}
8AD0: C9 11           CMP     #$11                ; 
8AD2: D0 0A           BNE     $8ADE               ; {}
8AD4: B5 AC           LDA     $AC,X               ; {ram.00AC}
8AD6: C9 02           CMP     #$02                ; 
8AD8: F0 0A           BEQ     $8AE4               ; {}
8ADA: C9 04           CMP     #$04                ; 
8ADC: F0 06           BEQ     $8AE4               ; {}
8ADE: B5 AC           LDA     $AC,X               ; {ram.00AC}
8AE0: C9 03           CMP     #$03                ; 
8AE2: D0 12           BNE     $8AF6               ; {}
8AE4: 20 D0 79        JSR     $79D0               ; {ram.79D0}
8AE7: BD 05 04        LDA     $0405,X             ; {ram.0405}
8AEA: F0 0A           BEQ     $8AF6               ; {}
8AEC: BD 4F 03        LDA     $034F,X             ; {ram.034F}
8AEF: C9 10           CMP     #$10                ; 
8AF1: D0 03           BNE     $8AF6               ; {}
8AF3: CE 10 05        DEC     $0510               ; {ram.0510}
8AF6: 60              RTS                         ; 
8AF7: 00              BRK                         ; 
8AF8: 00              BRK                         ; 
8AF9: 00              BRK                         ; 
8AFA: 20 00 00        JSR     $0000               ; {ram.GP_00}
8AFD: 00              BRK                         ; 
8AFE: 10 08           BPL     $8B08               ; {}
8B00: FF                              ;
8B01: 08              PHP                         ; 
8B02: 10 10           BPL     $8B14               ; {}
8B04: 08              PHP                         ; 
8B05: 08              PHP                         ; 
8B06: 05 08           ORA     <$08                ; {ram.0008}
8B08: 08              PHP                         ; 
8B09: B5 AC           LDA     $AC,X               ; {ram.00AC}
8B0B: F0 03           BEQ     $8B10               ; {}
8B0D: 4C 9D 8B        JMP     $8B9D               ; {}
8B10: A5 4D           LDA     <$4D                ; {ram.004D}
8B12: D0 39           BNE     $8B4D               ; {}
8B14: AD 10 05        LDA     $0510               ; {ram.0510}
8B17: C9 02           CMP     #$02                ; 
8B19: B0 32           BCS     $8B4D               ; {}
8B1B: A5 98           LDA     <$98                ; {ram.0098}
8B1D: 95 98           STA     $98,X               ; {ram.0098}
8B1F: B5 19           LDA     $19,X               ; {ram.0019}
8B21: C9 C0           CMP     #$C0                ; 
8B23: 90 03           BCC     $8B28               ; {}
8B25: 20 D0 F1        JSR     $F1D0               ; 
8B28: B5 98           LDA     $98,X               ; {ram.0098}
8B2A: 29 0C           AND     #$0C                ; 
8B2C: F0 20           BEQ     $8B4E               ; {}
8B2E: A5 70           LDA     <$70                ; {ram.0070}
8B30: 95 70           STA     $70,X               ; {ram.0070}
8B32: A0 28           LDY     #$28                ; 
8B34: B5 98           LDA     $98,X               ; {ram.0098}
8B36: 29 08           AND     #$08                ; 
8B38: F0 02           BEQ     $8B3C               ; {}
8B3A: A0 D8           LDY     #$D8                ; 
8B3C: 84 00           STY     <$00                ; {ram.GP_00}
8B3E: A5 84           LDA     <$84                ; {ram.0084}
8B40: 18              CLC                         ; 
8B41: 65 00           ADC     <$00                ; {ram.GP_00}
8B43: 29 F0           AND     #$F0                ; 
8B45: 09 0D           ORA     #$0D                ; 
8B47: 95 84           STA     $84,X               ; {ram.0084}
8B49: C9 5D           CMP     #$5D                ; 
8B4B: B0 37           BCS     $8B84               ; {}
8B4D: 60              RTS                         ; 
8B4E: A5 84           LDA     <$84                ; {ram.0084}
8B50: 95 84           STA     $84,X               ; {ram.0084}
8B52: C9 5D           CMP     #$5D                ; 
8B54: 90 F7           BCC     $8B4D               ; {}
8B56: A0 28           LDY     #$28                ; 
8B58: B5 98           LDA     $98,X               ; {ram.0098}
8B5A: 29 02           AND     #$02                ; 
8B5C: F0 02           BEQ     $8B60               ; {}
8B5E: A0 D8           LDY     #$D8                ; 
8B60: 84 00           STY     <$00                ; {ram.GP_00}
8B62: A5 70           LDA     <$70                ; {ram.0070}
8B64: 85 01           STA     <$01                ; {ram.GP_01}
8B66: 18              CLC                         ; 
8B67: 65 00           ADC     <$00                ; {ram.GP_00}
8B69: 29 F8           AND     #$F8                ; 
8B6B: 95 70           STA     $70,X               ; {ram.0070}
8B6D: 85 02           STA     <$02                ; {ram.GP_02}
8B6F: C5 01           CMP     <$01                ; {ram.GP_01}
8B71: 90 08           BCC     $8B7B               ; {}
8B73: 48              PHA                         ; 
8B74: A5 01           LDA     <$01                ; {ram.GP_01}
8B76: 85 02           STA     <$02                ; {ram.GP_02}
8B78: 68              PLA                         ; 
8B79: 85 01           STA     <$01                ; {ram.GP_01}
8B7B: A5 01           LDA     <$01                ; {ram.GP_01}
8B7D: 38              SEC                         ; 
8B7E: E5 02           SBC     <$02                ; {ram.GP_02}
8B80: C9 30           CMP     #$30                ; 
8B82: B0 C9           BCS     $8B4D               ; {}
8B84: 20 F4 ED        JSR     $EDF4               ; 
8B87: CD 4A 03        CMP     $034A               ; {ram.034A}
8B8A: B0 C1           BCS     $8B4D               ; {}
8B8C: EE 10 05        INC     $0510               ; {ram.0510}
8B8F: A9 01           LDA     #$01                ; 
8B91: 9D D0 03        STA     $03D0,X             ; {ram.03D0}
8B94: 0A              ASL     A                   ; 
8B95: 85 4D           STA     <$4D                ; {ram.004D}
8B97: 20 DA 8B        JSR     $8BDA               ; {}
8B9A: 20 D0 F1        JSR     $F1D0               ; 
8B9D: B5 AC           LDA     $AC,X               ; {ram.00AC}
8B9F: C9 03           CMP     #$03                ; 
8BA1: D0 33           BNE     $8BD6               ; {}
8BA3: B5 C0           LDA     $C0,X               ; {ram.00C0}
8BA5: F0 06           BEQ     $8BAD               ; {}
8BA7: 20 B8 EE        JSR     $EEB8               ; 
8BAA: 4C F6 8B        JMP     $8BF6               ; {}
8BAD: AD 6C 06        LDA     $066C               ; {ram.066C}
8BB0: 15 3D           ORA     $3D,X               ; {ram.003D}
8BB2: D0 42           BNE     $8BF6               ; {}
8BB4: B5 98           LDA     $98,X               ; {ram.0098}
8BB6: 85 0F           STA     <$0F                ; {ram.000F}
8BB8: 20 FA ED        JSR     $EDFA               ; 
8BBB: CD 4A 03        CMP     $034A               ; {ram.034A}
8BBE: B0 1A           BCS     $8BDA               ; {}
8BC0: 20 B8 6F        JSR     $6FB8               ; {ram.6FB8}
8BC3: F0 15           BEQ     $8BDA               ; {}
8BC5: 20 8D F0        JSR     $F08D               ; 
8BC8: BD 94 03        LDA     $0394,X             ; {ram.0394}
8BCB: 29 0F           AND     #$0F                ; 
8BCD: D0 03           BNE     $8BD2               ; {}
8BCF: 9D 94 03        STA     $0394,X             ; {ram.0394}
8BD2: A9 FF           LDA     #$FF                ; 
8BD4: 95 28           STA     $28,X               ; {ram.0028}
8BD6: B5 28           LDA     $28,X               ; {ram.0028}
8BD8: D0 1C           BNE     $8BF6               ; {}
8BDA: B5 AC           LDA     $AC,X               ; {ram.00AC}
8BDC: 18              CLC                         ; 
8BDD: 69 01           ADC     #$01                ; 
8BDF: C9 06           CMP     #$06                ; 
8BE1: 90 05           BCC     $8BE8               ; {}
8BE3: CE 10 05        DEC     $0510               ; {ram.0510}
8BE6: A9 00           LDA     #$00                ; 
8BE8: 95 AC           STA     $AC,X               ; {ram.00AC}
8BEA: A8              TAY                         ; 
8BEB: B9 F7 8A        LDA     $8AF7,Y             ; {}
8BEE: 9D BC 03        STA     $03BC,X             ; {ram.03BC}
8BF1: B9 FD 8A        LDA     $8AFD,Y             ; {}
8BF4: 95 28           STA     $28,X               ; {ram.0028}
8BF6: B4 AC           LDY     $AC,X               ; {ram.00AC}
8BF8: B9 03 8B        LDA     $8B03,Y             ; {}
8BFB: 4C A6 8A        JMP     $8AA6               ; {}
8BFE: 60              RTS                         ; 
8BFF: A9 A0           LDA     #$A0                ; 
8C01: BC 4F 03        LDY     $034F,X             ; {ram.034F}
8C04: C0 09           CPY     #$09                ; 
8C06: B0 02           BCS     $8C0A               ; {}
8C08: A9 70           LDA     #$70                ; 
8C0A: 9D 1F 04        STA     $041F,X             ; {ram.041F}
8C0D: 20 94 80        JSR     $8094               ; {}
8C10: A9 20           LDA     #$20                ; 
8C12: BC 4F 03        LDY     $034F,X             ; {ram.034F}
8C15: C0 07           CPY     #$07                ; 
8C17: F0 05           BEQ     $8C1E               ; {}
8C19: C0 09           CPY     #$09                ; 
8C1B: F0 01           BEQ     $8C1E               ; {}
8C1D: 0A              ASL     A                   ; 
8C1E: A0 53           LDY     #$53                ; 
8C20: 20 D3 87        JSR     $87D3               ; {}
8C23: 20 93 FA        JSR     $FA93               ; 
8C26: B5 98           LDA     $98,X               ; {ram.0098}
8C28: A8              TAY                         ; 
8C29: 29 0C           AND     #$0C                ; 
8C2B: F0 0A           BEQ     $8C37               ; {}
8C2D: A9 02           LDA     #$02                ; 
8C2F: C0 08           CPY     #$08                ; 
8C31: D0 0C           BNE     $8C3F               ; {}
8C33: A9 01           LDA     #$01                ; 
8C35: D0 08           BNE     $8C3F               ; {}
8C37: C0 01           CPY     #$01                ; 
8C39: D0 02           BNE     $8C3D               ; {}
8C3B: E6 0F           INC     <$0F                ; {ram.000F}
8C3D: A9 00           LDA     #$00                ; 
8C3F: 48              PHA                         ; 
8C40: DE D0 03        DEC     $03D0,X             ; {ram.03D0}
8C43: D0 0C           BNE     $8C51               ; {}
8C45: A9 06           LDA     #$06                ; 
8C47: 9D D0 03        STA     $03D0,X             ; {ram.03D0}
8C4A: 4A              LSR     A                   ; 
8C4B: 5D E4 03        EOR     $03E4,X             ; {ram.03E4}
8C4E: 9D E4 03        STA     $03E4,X             ; {ram.03E4}
8C51: 68              PLA                         ; 
8C52: 18              CLC                         ; 
8C53: 7D E4 03        ADC     $03E4,X             ; {ram.03E4}
8C56: 48              PHA                         ; 
8C57: B5 98           LDA     $98,X               ; {ram.0098}
8C59: 29 0C           AND     #$0C                ; 
8C5B: D0 07           BNE     $8C64               ; {}
8C5D: 68              PLA                         ; 
8C5E: 20 DF 77        JSR     $77DF               ; {ram.77DF}
8C61: 4C D0 79        JMP     $79D0               ; {ram.79D0}
8C64: 68              PLA                         ; 
8C65: 20 DB 77        JSR     $77DB               ; {ram.77DB}
8C68: 4C D0 79        JMP     $79D0               ; {ram.79D0}
8C6B: A9 FF           LDA     #$FF                ; 
8C6D: 20 6E 80        JSR     $806E               ; {}
8C70: 20 8D 8C        JSR     $8C8D               ; {}
8C73: 20 D0 79        JSR     $79D0               ; {ram.79D0}
8C76: BD 05 04        LDA     $0405,X             ; {ram.0405}
8C79: F0 11           BEQ     $8C8C               ; {}
8C7B: A0 0B           LDY     #$0B                ; 
8C7D: B9 4F 03        LDA     $034F,Y             ; {ram.034F}
8C80: C9 22           CMP     #$22                ; 
8C82: D0 05           BNE     $8C89               ; {}
8C84: A9 11           LDA     #$11                ; 
8C86: 99 05 04        STA     $0405,Y             ; {ram.0405}
8C89: 88              DEY                         ; 
8C8A: D0 F1           BNE     $8C7D               ; {}
8C8C: 60              RTS                         ; 
8C8D: 20 93 FA        JSR     $FA93               ; 
8C90: 85 0D           STA     <$0D                ; {ram.000D}
8C92: B5 98           LDA     $98,X               ; {ram.0098}
8C94: 29 08           AND     #$08                ; 
8C96: D0 0A           BNE     $8CA2               ; {}
8C98: E6 0D           INC     <$0D                ; {ram.000D}
8C9A: B5 98           LDA     $98,X               ; {ram.0098}
8C9C: 29 01           AND     #$01                ; 
8C9E: F0 0A           BEQ     $8CAA               ; {}
8CA0: D0 06           BNE     $8CA8               ; {}
8CA2: B5 98           LDA     $98,X               ; {ram.0098}
8CA4: 29 02           AND     #$02                ; 
8CA6: F0 02           BEQ     $8CAA               ; {}
8CA8: E6 0F           INC     <$0F                ; {ram.000F}
8CAA: A5 0D           LDA     <$0D                ; {ram.000D}
8CAC: 20 DF 77        JSR     $77DF               ; {ram.77DF}
8CAF: 4C A7 7A        JMP     $7AA7               ; {ram.7AA7}
8CB2: 24 0B           BIT     <$0B                ; {ram.000B}
8CB4: 1C                              ;
8CB5: 22                              ;
8CB6: 34                              ;
8CB7: 3D 4E E0        AND     $E04E,X             ; 
8CBA: B0 B0           BCS     $8C6C               ; {}
8CBC: 30 40           BMI     $8CFE               ; {}
8CBE: 90 A0           BCC     $8C60               ; {}
8CC0: B5 28           LDA     $28,X               ; {ram.0028}
8CC2: 9D 92 04        STA     $0492,X             ; 
8CC5: D0 64           BNE     $8D2B               ; {}
8CC7: BD 4F 03        LDA     $034F,X             ; {ram.034F}
8CCA: C9 22           CMP     #$22                ; 
8CCC: F0 5D           BEQ     $8D2B               ; {}
8CCE: A9 70           LDA     #$70                ; 
8CD0: 85 00           STA     <$00                ; {ram.GP_00}
8CD2: A0 06           LDY     #$06                ; 
8CD4: A5 EB           LDA     <$EB                ; {ram.00EB}
8CD6: D9 B2 8C        CMP     $8CB2,Y             ; {}
8CD9: D0 27           BNE     $8D02               ; {}
8CDB: B5 70           LDA     $70,X               ; {ram.0070}
8CDD: D9 B9 8C        CMP     $8CB9,Y             ; {}
8CE0: D0 20           BNE     $8D02               ; {}
8CE2: B5 84           LDA     $84,X               ; {ram.0084}
8CE4: C9 80           CMP     #$80                ; 
8CE6: D0 1A           BNE     $8D02               ; {}
8CE8: C0 00           CPY     #$00                ; 
8CEA: D0 1D           BNE     $8D09               ; {}
8CEC: 85 97           STA     <$97                ; {ram.0097}
8CEE: B5 70           LDA     $70,X               ; {ram.0070}
8CF0: 85 83           STA     <$83                ; {ram.0083}
8CF2: 84 BF           STY     <$BF                ; {ram.00BF}
8CF4: A9 14           LDA     #$14                ; 
8CF6: 85 AB           STA     <$AB                ; {ram.00AB}
8CF8: 20 14 73        JSR     $7314               ; {ram.7314}
8CFB: D0 08           BNE     $8D05               ; {}
8CFD: 20 81 90        JSR     $9081               ; {}
8D00: D0 03           BNE     $8D05               ; {}
8D02: 88              DEY                         ; 
8D03: 10 CF           BPL     $8CD4               ; {}
8D05: A9 26           LDA     #$26                ; 
8D07: 85 00           STA     <$00                ; {ram.GP_00}
8D09: A5 00           LDA     <$00                ; {ram.GP_00}
8D0B: 48              PHA                         ; 
8D0C: C9 70           CMP     #$70                ; 
8D0E: D0 03           BNE     $8D13               ; {}
8D10: 20 81 90        JSR     $9081               ; {}
8D13: E6 F7           INC     <$F7                ; {ram.00F7}
8D15: 68              PLA                         ; 
8D16: 20 62 E8        JSR     $E862               ; 
8D19: A9 03           LDA     #$03                ; 
8D1B: 9D 94 03        STA     $0394,X             ; {ram.0394}
8D1E: A9 20           LDA     #$20                ; 
8D20: B4 19           LDY     $19,X               ; {ram.0019}
8D22: C0 80           CPY     #$80                ; 
8D24: 90 02           BCC     $8D28               ; {}
8D26: A9 60           LDA     #$60                ; 
8D28: 9D BC 03        STA     $03BC,X             ; {ram.03BC}
8D2B: A9 04           LDA     #$04                ; 
8D2D: 9D F8 03        STA     $03F8,X             ; {ram.03F8}
8D30: 95 98           STA     $98,X               ; {ram.0098}
8D32: B5 28           LDA     $28,X               ; {ram.0028}
8D34: 4A              LSR     A                   ; 
8D35: B0 0A           BCS     $8D41               ; {}
8D37: BD 4F 03        LDA     $034F,X             ; {ram.034F}
8D3A: C9 22           CMP     #$22                ; 
8D3C: F0 04           BEQ     $8D42               ; {}
8D3E: 20 69 8D        JSR     $8D69               ; {}
8D41: 60              RTS                         ; 
8D42: 20 8D 8C        JSR     $8C8D               ; {}
8D45: BD 92 04        LDA     $0492,X             ; 
8D48: D0 F7           BNE     $8D41               ; {}
8D4A: 20 D6 FE        JSR     $FED6               ; 
8D4D: 4C 7C 87        JMP     $877C               ; {}
8D50: 20 19 81        JSR     $8119               ; {}
8D53: B5 C0           LDA     $C0,X               ; {ram.00C0}
8D55: D0 12           BNE     $8D69               ; {}
8D57: DE D0 03        DEC     $03D0,X             ; {ram.03D0}
8D5A: D0 0D           BNE     $8D69               ; {}
8D5C: A9 06           LDA     #$06                ; 
8D5E: 9D D0 03        STA     $03D0,X             ; {ram.03D0}
8D61: BD E4 03        LDA     $03E4,X             ; {ram.03E4}
8D64: 49 02           EOR     #$02                ; 
8D66: 9D E4 03        STA     $03E4,X             ; {ram.03E4}
8D69: 20 93 FA        JSR     $FA93               ; 
8D6C: B4 98           LDY     $98,X               ; {ram.0098}
8D6E: C0 08           CPY     #$08                ; 
8D70: D0 02           BNE     $8D74               ; {}
8D72: A9 01           LDA     #$01                ; 
8D74: 18              CLC                         ; 
8D75: 7D E4 03        ADC     $03E4,X             ; {ram.03E4}
8D78: 20 DF 77        JSR     $77DF               ; {ram.77DF}
8D7B: B5 28           LDA     $28,X               ; {ram.0028}
8D7D: D0 0E           BNE     $8D8D               ; {}
8D7F: 20 D0 79        JSR     $79D0               ; {ram.79D0}
8D82: BD 05 04        LDA     $0405,X             ; {ram.0405}
8D85: F0 05           BEQ     $8D8C               ; {}
8D87: A9 5D           LDA     #$5D                ; 
8D89: 9D 4F 03        STA     $034F,X             ; {ram.034F}
8D8C: 60              RTS                         ; 
8D8D: 4C A7 7A        JMP     $7AA7               ; {ram.7AA7}
8D90: 20 23 B2        JSR     $B223               ; {}
8D93: A5 AD           LDA     <$AD                ; {ram.00AD}
8D95: D0 19           BNE     $8DB0               ; {}
8D97: A5 84           LDA     <$84                ; {ram.0084}
8D99: C9 AD           CMP     #$AD                ; 
8D9B: D0 12           BNE     $8DAF               ; {}
8D9D: A5 70           LDA     <$70                ; {ram.0070}
8D9F: C9 70           CMP     #$70                ; 
8DA1: 90 0C           BCC     $8DAF               ; {}
8DA3: C9 81           CMP     #$81                ; 
8DA5: B0 08           BCS     $8DAF               ; {}
8DA7: E6 AD           INC     <$AD                ; {ram.00AD}
8DA9: A9 40           LDA     #$40                ; 
8DAB: 85 AC           STA     <$AC                ; {ram.00AC}
8DAD: 85 63           STA     <$63                ; {ram.0063}
8DAF: 60              RTS                         ; 
8DB0: C9 01           CMP     #$01                ; 
8DB2: D0 0A           BNE     $8DBE               ; {}
8DB4: A5 63           LDA     <$63                ; {ram.0063}
8DB6: D0 14           BNE     $8DCC               ; {}
8DB8: E6 AD           INC     <$AD                ; {ram.00AD}
8DBA: A9 50           LDA     #$50                ; 
8DBC: 85 29           STA     <$29                ; {ram.0029}
8DBE: C9 02           CMP     #$02                ; 
8DC0: D0 20           BNE     $8DE2               ; {}
8DC2: A5 29           LDA     <$29                ; {ram.0029}
8DC4: D0 06           BNE     $8DCC               ; {}
8DC6: E6 AD           INC     <$AD                ; {ram.00AD}
8DC8: A9 00           LDA     #$00                ; 
8DCA: 85 AC           STA     <$AC                ; {ram.00AC}
8DCC: A0 00           LDY     #$00                ; 
8DCE: 8C F8 03        STY     $03F8               ; {ram.03F8}
8DD1: A5 AC           LDA     <$AC                ; {ram.00AC}
8DD3: 48              PHA                         ; 
8DD4: 84 AC           STY     <$AC                ; {ram.00AC}
8DD6: 20 13 F2        JSR     $F213               ; 
8DD9: 68              PLA                         ; 
8DDA: 85 AC           STA     <$AC                ; {ram.00AC}
8DDC: 20 EA 8D        JSR     $8DEA               ; {}
8DDF: AE 40 03        LDX     $0340               ; {ram.0340}
8DE2: 60              RTS                         ; 
8DE3: 14                              ;
8DE4: 10 0C           BPL     $8DF2               ; {}
8DE6: 08              PHP                         ; 
8DE7: 04                              ;
8DE8: 00              BRK                         ; 
8DE9: 1C                              ;
8DEA: A2 02           LDX     #$02                ; 
8DEC: B5 AC           LDA     $AC,X               ; {ram.00AC}
8DEE: D0 2B           BNE     $8E1B               ; {}
8DF0: E0 02           CPX     #$02                ; 
8DF2: F0 11           BEQ     $8E05               ; {}
8DF4: A5 AE           LDA     <$AE                ; {ram.00AE}
8DF6: F0 F4           BEQ     $8DEC               ; {}
8DF8: 8A              TXA                         ; 
8DF9: 38              SEC                         ; 
8DFA: E9 03           SBC     #$03                ; 
8DFC: A8              TAY                         ; 
8DFD: AD 96 03        LDA     $0396               ; {ram.0396}
8E00: D9 E3 8D        CMP     $8DE3,Y             ; {}
8E03: D0 37           BNE     $8E3C               ; {}
8E05: F6 AC           INC     $AC,X               ; {ram.00AC}
8E07: A9 80           LDA     #$80                ; 
8E09: 95 98           STA     $98,X               ; {ram.0098}
8E0B: A9 18           LDA     #$18                ; 
8E0D: 9D 94 03        STA     $0394,X             ; {ram.0394}
8E10: A5 71           LDA     <$71                ; {ram.0071}
8E12: 95 70           STA     $70,X               ; {ram.0070}
8E14: A5 85           LDA     <$85                ; {ram.0085}
8E16: 38              SEC                         ; 
8E17: E9 1C           SBC     #$1C                ; 
8E19: 95 84           STA     $84,X               ; {ram.0084}
8E1B: A9 00           LDA     #$00                ; 
8E1D: 85 0B           STA     <$0B                ; {ram.000B}
8E1F: A9 60           LDA     #$60                ; 
8E21: 20 59 B4        JSR     $B459               ; {}
8E24: A9 06           LDA     #$06                ; 
8E26: A8              TAY                         ; 
8E27: 20 BD B3        JSR     $B3BD               ; {}
8E2A: 95 84           STA     $84,X               ; {ram.0084}
8E2C: 8A              TXA                         ; 
8E2D: 48              PHA                         ; 
8E2E: 20 86 79        JSR     $7986               ; {ram.7986}
8E31: 20 93 FA        JSR     $FA93               ; 
8E34: AE 40 03        LDX     $0340               ; {ram.0340}
8E37: 20 DF 77        JSR     $77DF               ; {ram.77DF}
8E3A: 68              PLA                         ; 
8E3B: AA              TAX                         ; 
8E3C: E8              INX                         ; 
8E3D: E0 0A           CPX     #$0A                ; 
8E3F: D0 AB           BNE     $8DEC               ; {}
8E41: 60              RTS                         ; 
8E42: 08              PHP                         ; 
8E43: 04                              ;
8E44: B5 AC           LDA     $AC,X               ; {ram.00AC}
8E46: D0 4A           BNE     $8E92               ; {}
8E48: BD 4F 03        LDA     $034F,X             ; {ram.034F}
8E4B: C9 65           CMP     #$65                ; 
8E4D: F0 05           BEQ     $8E54               ; {}
8E4F: AD 65 06        LDA     $0665               ; {ram.0665}
8E52: F0 3D           BEQ     $8E91               ; {}
8E54: 20 5A 8F        JSR     $8F5A               ; {}
8E57: B0 38           BCS     $8E91               ; {}
8E59: A5 70           LDA     <$70                ; {ram.0070}
8E5B: D5 70           CMP     $70,X               ; {ram.0070}
8E5D: D0 32           BNE     $8E91               ; {}
8E5F: A0 00           LDY     #$00                ; 
8E61: A5 84           LDA     <$84                ; {ram.0084}
8E63: 18              CLC                         ; 
8E64: 69 03           ADC     #$03                ; 
8E66: 38              SEC                         ; 
8E67: F5 84           SBC     $84,X               ; {ram.0084}
8E69: 10 06           BPL     $8E71               ; {}
8E6B: C8              INY                         ; 
8E6C: 49 FF           EOR     #$FF                ; 
8E6E: 18              CLC                         ; 
8E6F: 69 01           ADC     #$01                ; 
8E71: C9 11           CMP     #$11                ; 
8E73: B0 1C           BCS     $8E91               ; {}
8E75: AD F8 03        LDA     $03F8               ; {ram.03F8}
8E78: 29 0C           AND     #$0C                ; 
8E7A: F0 15           BEQ     $8E91               ; {}
8E7C: D9 42 8E        CMP     $8E42,Y             ; {}
8E7F: D0 10           BNE     $8E91               ; {}
8E81: 95 98           STA     $98,X               ; {ram.0098}
8E83: F6 AC           INC     $AC,X               ; {ram.00AC}
8E85: A5 EB           LDA     <$EB                ; {ram.00EB}
8E87: 9D 12 04        STA     $0412,X             ; {ram.0412}
8E8A: E6 F7           INC     <$F7                ; {ram.00F7}
8E8C: A9 26           LDA     #$26                ; 
8E8E: 20 62 E8        JSR     $E862               ; 
8E91: 60              RTS                         ; 
8E92: B5 98           LDA     $98,X               ; {ram.0098}
8E94: 85 0F           STA     <$0F                ; {ram.000F}
8E96: 20 8D F0        JSR     $F08D               ; 
8E99: 20 93 FA        JSR     $FA93               ; 
8E9C: C6 01           DEC     <$01                ; {ram.GP_01}
8E9E: 20 DF 77        JSR     $77DF               ; {ram.77DF}
8EA1: BD 94 03        LDA     $0394,X             ; {ram.0394}
8EA4: C9 10           CMP     #$10                ; 
8EA6: F0 04           BEQ     $8EAC               ; {}
8EA8: C9 F0           CMP     #$F0                ; 
8EAA: D0 E5           BNE     $8E91               ; {}
8EAC: A5 EB           LDA     <$EB                ; {ram.00EB}
8EAE: 48              PHA                         ; 
8EAF: BD 12 04        LDA     $0412,X             ; {ram.0412}
8EB2: 85 EB           STA     <$EB                ; {ram.00EB}
8EB4: 20 C6 E6        JSR     $E6C6               ; 
8EB7: 68              PLA                         ; 
8EB8: 85 EB           STA     <$EB                ; {ram.00EB}
8EBA: A9 C8           LDA     #$C8                ; 
8EBC: BC 4F 03        LDY     $034F,X             ; {ram.034F}
8EBF: C0 62           CPY     #$62                ; 
8EC1: F0 08           BEQ     $8ECB               ; {}
8EC3: A9 BC           LDA     #$BC                ; 
8EC5: C0 65           CPY     #$65                ; 
8EC7: F0 02           BEQ     $8ECB               ; {}
8EC9: A9 C0           LDA     #$C0                ; 
8ECB: E6 F7           INC     <$F7                ; {ram.00F7}
8ECD: 20 62 E8        JSR     $E862               ; 
8ED0: A9 70           LDA     #$70                ; 
8ED2: 85 00           STA     <$00                ; {ram.GP_00}
8ED4: BC 12 04        LDY     $0412,X             ; {ram.0412}
8ED7: 20 8C 71        JSR     $718C               ; {ram.718C}
8EDA: 95 70           STA     $70,X               ; {ram.0070}
8EDC: 94 84           STY     $84,X               ; {ram.0084}
8EDE: A5 00           LDA     <$00                ; {ram.GP_00}
8EE0: E6 F7           INC     <$F7                ; {ram.00F7}
8EE2: 20 62 E8        JSR     $E862               ; 
8EE5: 20 5F B1        JSR     $B15F               ; {}
8EE8: 4C 81 90        JMP     $9081               ; {}
8EEB: 20 5A 8F        JSR     $8F5A               ; {}
8EEE: B0 1D           BCS     $8F0D               ; {}
8EF0: A0 10           LDY     #$10                ; 
8EF2: B9 AC 00        LDA     $00AC,Y             ; {ram.00AC}
8EF5: C9 13           CMP     #$13                ; 
8EF7: F0 08           BEQ     $8F01               ; {}
8EF9: C8              INY                         ; 
8EFA: B9 AC 00        LDA     $00AC,Y             ; {ram.00AC}
8EFD: C9 13           CMP     #$13                ; 
8EFF: D0 0C           BNE     $8F0D               ; {}
8F01: 84 00           STY     <$00                ; {ram.GP_00}
8F03: 20 3F 8F        JSR     $8F3F               ; {}
8F06: F0 05           BEQ     $8F0D               ; {}
8F08: A9 24           LDA     #$24                ; 
8F0A: 20 34 8F        JSR     $8F34               ; {}
8F0D: 60              RTS                         ; 
8F0E: 20 5A 8F        JSR     $8F5A               ; {}
8F11: B0 2B           BCS     $8F3E               ; {}
8F13: A0 10           LDY     #$10                ; 
8F15: B9 AC 00        LDA     $00AC,Y             ; {ram.00AC}
8F18: C9 22           CMP     #$22                ; 
8F1A: F0 08           BEQ     $8F24               ; {}
8F1C: C8              INY                         ; 
8F1D: B9 AC 00        LDA     $00AC,Y             ; {ram.00AC}
8F20: C9 22           CMP     #$22                ; 
8F22: D0 1A           BNE     $8F3E               ; {}
8F24: 84 00           STY     <$00                ; {ram.GP_00}
8F26: B9 28 00        LDA     $0028,Y             ; {ram.0028}
8F29: C9 02           CMP     #$02                ; 
8F2B: B0 11           BCS     $8F3E               ; {}
8F2D: 20 3F 8F        JSR     $8F3F               ; {}
8F30: F0 0C           BEQ     $8F3E               ; {}
8F32: A9 70           LDA     #$70                ; 
8F34: 20 E0 8E        JSR     $8EE0               ; {}
8F37: 20 CE E6        JSR     $E6CE               ; 
8F3A: 09 80           ORA     #$80                ; 
8F3C: 91 00           STA     ($00),Y             ; {ram.GP_00}
8F3E: 60              RTS                         ; 
8F3F: B9 70 00        LDA     $0070,Y             ; {ram.0070}
8F42: 18              CLC                         ; 
8F43: 69 08           ADC     #$08                ; 
8F45: 85 04           STA     <$04                ; {ram.0004}
8F47: B9 84 00        LDA     $0084,Y             ; {ram.0084}
8F4A: 18              CLC                         ; 
8F4B: 69 08           ADC     #$08                ; 
8F4D: 85 05           STA     <$05                ; {ram.0005}
8F4F: 20 2D 7A        JSR     $7A2D               ; {ram.7A2D}
8F52: A9 10           LDA     #$10                ; 
8F54: 4C FB 7D        JMP     $7DFB               ; {ram.7DFB}
8F57: 00              BRK                         ; 
8F58: 00              BRK                         ; 
8F59: 01 AD           ORA     ($AD,X)             ; {ram.00AD}
8F5B: CD 04 4A        CMP     $4A04               ; 
8F5E: 4A              LSR     A                   ; 
8F5F: 4A              LSR     A                   ; 
8F60: 4A              LSR     A                   ; 
8F61: 4A              LSR     A                   ; 
8F62: 4A              LSR     A                   ; 
8F63: F0 0D           BEQ     $8F72               ; {}
8F65: A8              TAY                         ; 
8F66: B9 57 8F        LDA     $8F57,Y             ; {}
8F69: A4 16           LDY     <$16                ; {ram.0016}
8F6B: D9 2D 06        CMP     $062D,Y             ; 
8F6E: F0 02           BEQ     $8F72               ; {}
8F70: 38              SEC                         ; 
8F71: 60              RTS                         ; 
8F72: 18              CLC                         ; 
8F73: 60              RTS                         ; 
8F74: 04                              ;
8F75: 08              PHP                         ; 
8F76: AD 60 06        LDA     $0660               ; {ram.0660}
8F79: F0 34           BEQ     $8FAF               ; {}
8F7B: B5 AC           LDA     $AC,X               ; {ram.00AC}
8F7D: D0 31           BNE     $8FB0               ; {}
8F7F: A9 80           LDA     #$80                ; 
8F81: A4 EB           LDY     <$EB                ; {ram.00EB}
8F83: C0 55           CPY     #$55                ; 
8F85: F0 02           BEQ     $8F89               ; {}
8F87: A9 60           LDA     #$60                ; 
8F89: C5 70           CMP     <$70                ; {ram.0070}
8F8B: D0 22           BNE     $8FAF               ; {}
8F8D: 95 70           STA     $70,X               ; {ram.0070}
8F8F: A0 01           LDY     #$01                ; 
8F91: A5 84           LDA     <$84                ; {ram.0084}
8F93: C9 3D           CMP     #$3D                ; 
8F95: F0 05           BEQ     $8F9C               ; {}
8F97: C8              INY                         ; 
8F98: C9 7D           CMP     #$7D                ; 
8F9A: D0 13           BNE     $8FAF               ; {}
8F9C: 94 AC           STY     $AC,X               ; {ram.00AC}
8F9E: 18              CLC                         ; 
8F9F: 69 06           ADC     #$06                ; 
8FA1: 95 84           STA     $84,X               ; {ram.0084}
8FA3: 20 81 90        JSR     $9081               ; {}
8FA6: A9 40           LDA     #$40                ; 
8FA8: 85 AC           STA     <$AC                ; {ram.00AC}
8FAA: B9 73 8F        LDA     $8F73,Y             ; {}
8FAD: 85 98           STA     <$98                ; {ram.0098}
8FAF: 60              RTS                         ; 
8FB0: B4 AC           LDY     $AC,X               ; {ram.00AC}
8FB2: 88              DEY                         ; 
8FB3: F0 14           BEQ     $8FC9               ; {}
8FB5: D6 84           DEC     $84,X               ; {ram.0084}
8FB7: C6 84           DEC     <$84                ; {ram.0084}
8FB9: A5 84           LDA     <$84                ; {ram.0084}
8FBB: C9 3D           CMP     #$3D                ; 
8FBD: D0 1F           BNE     $8FDE               ; {}
8FBF: 8A              TXA                         ; 
8FC0: 48              PHA                         ; 
8FC1: 20 82 F1        JSR     $F182               ; 
8FC4: 68              PLA                         ; 
8FC5: AA              TAX                         ; 
8FC6: 4C D8 8F        JMP     $8FD8               ; {}
8FC9: F6 84           INC     $84,X               ; {ram.0084}
8FCB: E6 84           INC     <$84                ; {ram.0084}
8FCD: A5 84           LDA     <$84                ; {ram.0084}
8FCF: C9 7F           CMP     #$7F                ; 
8FD1: D0 0B           BNE     $8FDE               ; {}
8FD3: A9 02           LDA     #$02                ; 
8FD5: 8D 94 03        STA     $0394               ; {ram.0394}
8FD8: A9 00           LDA     #$00                ; 
8FDA: 85 AC           STA     <$AC                ; {ram.00AC}
8FDC: 95 AC           STA     $AC,X               ; {ram.00AC}
8FDE: 8A              TXA                         ; 
8FDF: 48              PHA                         ; 
8FE0: 20 13 F2        JSR     $F213               ; 
8FE3: 68              PLA                         ; 
8FE4: AA              TAX                         ; 
8FE5: 20 4F FA        JSR     $FA4F               ; 
8FE8: A9 00           LDA     #$00                ; 
8FEA: A0 09           LDY     #$09                ; 
8FEC: 4C 0C 79        JMP     $790C               ; {ram.790C}
8FEF: AD 6C 06        LDA     $066C               ; {ram.066C}
8FF2: D0 06           BNE     $8FFA               ; {}
8FF4: 20 05 90        JSR     $9005               ; {}
8FF7: 20 88 B2        JSR     $B288               ; {}
8FFA: 20 93 FA        JSR     $FA93               ; 
8FFD: BD 37 04        LDA     $0437,X             ; {ram.0437}
9000: 29 01           AND     #$01                ; 
9002: 4C 8D 8C        JMP     $8C8D               ; {}
9005: BD 44 04        LDA     $0444,X             ; 
9008: 20 E2 E5        JSR     $E5E2               ; 
900B: 66 B2           ROR     <$B2                ; {ram.00B2}
900D: 17                              ;
900E: 90 08           BCC     $9018               ; {}
9010: B3                              ;
9011: 78              SEI                         ; 
9012: B3                              ;
9013: 60              RTS                         ; 
9014: B2                              ;
9015: 56 B2           LSR     $B2,X               ; {ram.00B2}
9017: A0 02           LDY     #$02                ; 
9019: B5 18           LDA     $18,X               ; {ram.0018}
901B: C9 A0           CMP     #$A0                ; 
901D: B0 06           BCS     $9025               ; {}
901F: C8              INY                         ; 
9020: C9 08           CMP     #$08                ; 
9022: B0 01           BCS     $9025               ; {}
9024: C8              INY                         ; 
9025: 4C 77 90        JMP     $9077               ; {}
9028: B5 C0           LDA     $C0,X               ; {ram.00C0}
902A: F0 06           BEQ     $9032               ; {}
902C: 20 B8 EE        JSR     $EEB8               ; 
902F: 4C 3F 90        JMP     $903F               ; {}
9032: AD 6C 06        LDA     $066C               ; {ram.066C}
9035: 15 3D           ORA     $3D,X               ; {ram.003D}
9037: D0 F6           BNE     $902F               ; {}
9039: 20 57 90        JSR     $9057               ; {}
903C: 20 88 B2        JSR     $B288               ; {}
903F: 20 93 FA        JSR     $FA93               ; 
9042: BD 37 04        LDA     $0437,X             ; {ram.0437}
9045: 29 01           AND     #$01                ; 
9047: 20 DB 77        JSR     $77DB               ; {ram.77DB}
904A: BD 44 04        LDA     $0444,X             ; 
904D: C9 05           CMP     #$05                ; 
904F: F0 03           BEQ     $9054               ; {}
9051: 4C A7 7A        JMP     $7AA7               ; {ram.7AA7}
9054: 4C D0 79        JMP     $79D0               ; {ram.79D0}
9057: BD 44 04        LDA     $0444,X             ; 
905A: 20 E2 E5        JSR     $E5E2               ; 
905D: 66 B2           ROR     <$B2                ; {ram.00B2}
905F: 69 90           ADC     #$90                ; 
9061: 08              PHP                         ; 
9062: B3                              ;
9063: 78              SEI                         ; 
9064: B3                              ;
9065: 60              RTS                         ; 
9066: B2                              ;
9067: 56 B2           LSR     $B2,X               ; {ram.00B2}
9069: A0 02           LDY     #$02                ; 
906B: B5 18           LDA     $18,X               ; {ram.0018}
906D: C9 B0           CMP     #$B0                ; 
906F: B0 06           BCS     $9077               ; {}
9071: C8              INY                         ; 
9072: C9 20           CMP     #$20                ; 
9074: B0 01           BCS     $9077               ; {}
9076: C8              INY                         ; 
9077: 98              TYA                         ; 
9078: 9D 44 04        STA     $0444,X             ; 
907B: A9 06           LDA     #$06                ; 
907D: 9D 2C 04        STA     $042C,X             ; {ram.!SplashMode}
9080: 60              RTS                         ; 
9081: A9 04           LDA     #$04                ; 
9083: 8D 02 06        STA     $0602               ; {ram.SND_ReqMusEff}
9086: 60              RTS                         ; 
9087: FF                              ;
9088: FF                              ;
9089: FF                              ;
908A: FF                              ;
908B: FF                              ;
908C: FF                              ;
908D: FF                              ;
908E: FF                              ;
908F: FF                              ;
9090: FF                              ;
9091: FF                              ;
9092: FF                              ;
9093: FF                              ;
9094: FF                              ;
9095: FF                              ;
9096: FF                              ;
9097: FF                              ;
9098: FF                              ;
9099: FF                              ;
909A: FF                              ;
909B: FF                              ;
909C: FF                              ;
909D: FF                              ;
909E: FF                              ;
909F: FF                              ;
90A0: 01 01           ORA     ($01,X)             ; {ram.GP_01}
90A2: 08              PHP                         ; 
90A3: 08              PHP                         ; 
90A4: 08              PHP                         ; 
90A5: 02                              ;
90A6: 02                              ;
90A7: 02                              ;
90A8: C1 C1           CMP     ($C1,X)             ; {ram.00C1}
90AA: C4 C4           CPY     <$C4                ; {ram.00C4}
90AC: C4 C2           CPY     <$C2                ; {ram.00C2}
90AE: C2                              ;
90AF: C2                              ;
90B0: 42                              ;
90B1: 42                              ;
90B2: 48              PHA                         ; 
90B3: 48              PHA                         ; 
90B4: 48              PHA                         ; 
90B5: 41 41           EOR     ($41,X)             ; {ram.0041}
90B7: 41 82           EOR     ($82,X)             ; {ram.0082}
90B9: 82                              ;
90BA: 84 84           STY     <$84                ; {ram.0084}
90BC: 84 81           STY     <$81                ; {ram.0081}
90BE: 81 81           STA     ($81,X)             ; {ram.0081}
90C0: C4 C4           CPY     <$C4                ; {ram.00C4}
90C2: C2                              ;
90C3: C2                              ;
90C4: C2                              ;
90C5: C8              INY                         ; 
90C6: C8              INY                         ; 
90C7: C8              INY                         ; 
90C8: 84 84           STY     <$84                ; {ram.0084}
90CA: 81 81           STA     ($81,X)             ; {ram.0081}
90CC: 81 88           STA     ($88,X)             ; 
90CE: 88              DEY                         ; 
90CF: 88              DEY                         ; 
90D0: 48              PHA                         ; 
90D1: 48              PHA                         ; 
90D2: 42                              ;
90D3: 42                              ;
90D4: 42                              ;
90D5: 44                              ;
90D6: 44                              ;
90D7: 44                              ;
90D8: 08              PHP                         ; 
90D9: 08              PHP                         ; 
90DA: 01 01           ORA     ($01,X)             ; {ram.GP_01}
90DC: 01 04           ORA     ($04,X)             ; {ram.0004}
90DE: 04                              ;
90DF: 04                              ;
90E0: 00              BRK                         ; 
90E1: F0 3D           BEQ     $9120               ; {}
90E3: DD B5 AC        CMP     $ACB5,X             ; {}
90E6: F0 03           BEQ     $90EB               ; {}
90E8: 4C 7D 91        JMP     $917D               ; {}
90EB: A5 29           LDA     <$29                ; {ram.0029}
90ED: D0 06           BNE     $90F5               ; {}
90EF: A5 AC           LDA     <$AC                ; {ram.00AC}
90F1: C9 40           CMP     #$40                ; 
90F3: D0 01           BNE     $90F6               ; {}
90F5: 60              RTS                         ; 
90F6: A5 70           LDA     <$70                ; {ram.0070}
90F8: C9 29           CMP     #$29                ; 
90FA: 90 04           BCC     $9100               ; {}
90FC: C9 C8           CMP     #$C8                ; 
90FE: 90 0A           BCC     $910A               ; {}
9100: A5 84           LDA     <$84                ; {ram.0084}
9102: C9 6D           CMP     #$6D                ; 
9104: 90 EF           BCC     $90F5               ; {}
9106: C9 B5           CMP     #$B5                ; 
9108: B0 EB           BCS     $90F5               ; {}
910A: A5 70           LDA     <$70                ; {ram.0070}
910C: C9 20           CMP     #$20                ; 
910E: F0 04           BEQ     $9114               ; {}
9110: C9 D0           CMP     #$D0                ; 
9112: D0 1D           BNE     $9131               ; {}
9114: A5 84           LDA     <$84                ; {ram.0084}
9116: 85 00           STA     <$00                ; {ram.GP_00}
9118: A5 70           LDA     <$70                ; {ram.0070}
911A: 85 01           STA     <$01                ; {ram.GP_01}
911C: A9 08           LDA     #$08                ; 
911E: 85 02           STA     <$02                ; {ram.GP_02}
9120: A0 20           LDY     #$20                ; 
9122: A9 00           LDA     #$00                ; 
9124: 20 62 92        JSR     $9262               ; {}
9127: A5 04           LDA     <$04                ; {ram.0004}
9129: 95 84           STA     $84,X               ; {ram.0084}
912B: B9 E0 90        LDA     $90E0,Y             ; {}
912E: 4C 55 91        JMP     $9155               ; {}
9131: A5 84           LDA     <$84                ; {ram.0084}
9133: C9 5D           CMP     #$5D                ; 
9135: F0 04           BEQ     $913B               ; {}
9137: C9 BD           CMP     #$BD                ; 
9139: D0 BA           BNE     $90F5               ; {}
913B: A5 70           LDA     <$70                ; {ram.0070}
913D: 85 00           STA     <$00                ; {ram.GP_00}
913F: A5 84           LDA     <$84                ; {ram.0084}
9141: 85 01           STA     <$01                ; {ram.GP_01}
9143: A9 02           LDA     #$02                ; 
9145: 85 02           STA     <$02                ; {ram.GP_02}
9147: A0 5D           LDY     #$5D                ; 
9149: A9 20           LDA     #$20                ; 
914B: 20 62 92        JSR     $9262               ; {}
914E: B9 E2 90        LDA     $90E2,Y             ; {}
9151: 95 84           STA     $84,X               ; {ram.0084}
9153: A5 04           LDA     <$04                ; {ram.0004}
9155: 95 70           STA     $70,X               ; {ram.0070}
9157: BC 12 04        LDY     $0412,X             ; {ram.0412}
915A: B9 A0 90        LDA     $90A0,Y             ; {}
915D: 29 0F           AND     #$0F                ; 
915F: 95 98           STA     $98,X               ; {ram.0098}
9161: A9 60           LDA     #$60                ; 
9163: 85 29           STA     <$29                ; {ram.0029}
9165: A9 18           LDA     #$18                ; 
9167: 9D BC 03        STA     $03BC,X             ; {ram.03BC}
916A: A9 08           LDA     #$08                ; 
916C: 9D D0 03        STA     $03D0,X             ; {ram.03D0}
916F: A9 00           LDA     #$00                ; 
9171: 9D 94 03        STA     $0394,X             ; {ram.0394}
9174: 9D 1F 04        STA     $041F,X             ; {ram.041F}
9177: 9D E4 03        STA     $03E4,X             ; {ram.03E4}
917A: F6 AC           INC     $AC,X               ; {ram.00AC}
917C: 60              RTS                         ; 
917D: B5 C0           LDA     $C0,X               ; {ram.00C0}
917F: F0 06           BEQ     $9187               ; {}
9181: 20 B8 EE        JSR     $EEB8               ; 
9184: 4C D3 91        JMP     $91D3               ; {}
9187: AD 6C 06        LDA     $066C               ; {ram.066C}
918A: 15 3D           ORA     $3D,X               ; {ram.003D}
918C: D0 F6           BNE     $9184               ; {}
918E: B5 98           LDA     $98,X               ; {ram.0098}
9190: 85 0F           STA     <$0F                ; {ram.000F}
9192: 20 8D F0        JSR     $F08D               ; 
9195: BD 94 03        LDA     $0394,X             ; {ram.0394}
9198: C9 10           CMP     #$10                ; 
919A: F0 04           BEQ     $91A0               ; {}
919C: C9 F0           CMP     #$F0                ; 
919E: D0 33           BNE     $91D3               ; {}
91A0: A9 00           LDA     #$00                ; 
91A2: 9D 94 03        STA     $0394,X             ; {ram.0394}
91A5: FE 12 04        INC     $0412,X             ; {ram.0412}
91A8: BC 12 04        LDY     $0412,X             ; {ram.0412}
91AB: B9 A0 90        LDA     $90A0,Y             ; {}
91AE: 29 0F           AND     #$0F                ; 
91B0: 95 98           STA     $98,X               ; {ram.0098}
91B2: FE 1F 04        INC     $041F,X             ; {ram.041F}
91B5: BD 1F 04        LDA     $041F,X             ; {ram.041F}
91B8: C9 07           CMP     #$07                ; 
91BA: 90 17           BCC     $91D3               ; {}
91BC: BD 2C 04        LDA     $042C,X             ; {ram.!SplashMode}
91BF: F0 0F           BEQ     $91D0               ; {}
91C1: 20 8A 82        JSR     $828A               ; {}
91C4: A9 03           LDA     #$03                ; 
91C6: 85 12           STA     <$12                ; {ram.0012}
91C8: A9 00           LDA     #$00                ; 
91CA: 85 AC           STA     <$AC                ; {ram.00AC}
91CC: 85 11           STA     <$11                ; {ram.0011}
91CE: 85 13           STA     <$13                ; {ram.0013}
91D0: 95 AC           STA     $AC,X               ; {ram.00AC}
91D2: 60              RTS                         ; 
91D3: BD 2C 04        LDA     $042C,X             ; {ram.!SplashMode}
91D6: D0 45           BNE     $921D               ; {}
91D8: 20 D0 79        JSR     $79D0               ; {ram.79D0}
91DB: BD 2C 04        LDA     $042C,X             ; {ram.!SplashMode}
91DE: F0 08           BEQ     $91E8               ; {}
91E0: A9 40           LDA     #$40                ; 
91E2: 85 AC           STA     <$AC                ; {ram.00AC}
91E4: A9 00           LDA     #$00                ; 
91E6: 85 C0           STA     <$C0                ; {ram.00C0}
91E8: AD 41 03        LDA     $0341               ; {ram.0341}
91EB: 48              PHA                         ; 
91EC: 20 42 92        JSR     $9242               ; {}
91EF: BD E4 03        LDA     $03E4,X             ; {ram.03E4}
91F2: 20 DF 77        JSR     $77DF               ; {ram.77DF}
91F5: 68              PLA                         ; 
91F6: A8              TAY                         ; 
91F7: B9 AB 77        LDA     $77AB,Y             ; 
91FA: 85 00           STA     <$00                ; {ram.GP_00}
91FC: B9 AC 77        LDA     $77AC,Y             ; 
91FF: 85 01           STA     <$01                ; {ram.GP_01}
9201: 20 9E 92        JSR     $929E               ; {}
9204: AE 40 03        LDX     $0340               ; {ram.0340}
9207: BD E4 03        LDA     $03E4,X             ; {ram.03E4}
920A: F0 10           BEQ     $921C               ; {}
920C: A4 00           LDY     <$00                ; {ram.GP_00}
920E: B9 01 02        LDA     $0201,Y             ; {ram.0201}
9211: C9 9C           CMP     #$9C                ; 
9213: F0 02           BEQ     $9217               ; {}
9215: A4 01           LDY     <$01                ; {ram.GP_01}
9217: A9 AC           LDA     #$AC                ; 
9219: 99 01 02        STA     $0201,Y             ; {ram.0201}
921C: 60              RTS                         ; 
921D: B5 70           LDA     $70,X               ; {ram.0070}
921F: 85 70           STA     <$70                ; {ram.0070}
9221: B5 84           LDA     $84,X               ; {ram.0084}
9223: 85 84           STA     <$84                ; {ram.0084}
9225: 20 13 F2        JSR     $F213               ; 
9228: 20 FB 6E        JSR     $6EFB               ; {ram.6EFB}
922B: AE 40 03        LDX     $0340               ; {ram.0340}
922E: 20 42 92        JSR     $9242               ; {}
9231: A9 01           LDA     #$01                ; 
9233: 9D E4 03        STA     $03E4,X             ; {ram.03E4}
9236: 20 93 82        JSR     $8293               ; {}
9239: A9 40           LDA     #$40                ; 
923B: 85 00           STA     <$00                ; {ram.GP_00}
923D: A9 44           LDA     #$44                ; 
923F: 4C FF 91        JMP     $91FF               ; {}
9242: A9 08           LDA     #$08                ; 
9244: 20 89 FA        JSR     $FA89               ; 
9247: BC 12 04        LDY     $0412,X             ; {ram.0412}
924A: B9 A0 90        LDA     $90A0,Y             ; {}
924D: 29 F0           AND     #$F0                ; 
924F: 09 01           ORA     #$01                ; 
9251: 20 88 79        JSR     $7988               ; {ram.7988}
9254: 29 40           AND     #$40                ; 
9256: F0 09           BEQ     $9261               ; {}
9258: A5 04           LDA     <$04                ; {ram.0004}
925A: 29 8F           AND     #$8F                ; 
925C: 20 88 79        JSR     $7988               ; {ram.7988}
925F: E6 0F           INC     <$0F                ; {ram.000F}
9261: 60              RTS                         ; 
9262: 9D 12 04        STA     $0412,X             ; {ram.0412}
9265: 84 03           STY     <$03                ; {ram.GP_03}
9267: A9 24           LDA     #$24                ; 
9269: AC F8 03        LDY     $03F8               ; {ram.03F8}
926C: F0 02           BEQ     $9270               ; {}
926E: A9 32           LDA     #$32                ; 
9270: A4 98           LDY     <$98                ; {ram.0098}
9272: C4 02           CPY     <$02                ; {ram.GP_02}
9274: D0 10           BNE     $9286               ; {}
9276: 48              PHA                         ; 
9277: BD 12 04        LDA     $0412,X             ; {ram.0412}
927A: 18              CLC                         ; 
927B: 69 08           ADC     #$08                ; 
927D: 9D 12 04        STA     $0412,X             ; {ram.0412}
9280: 68              PLA                         ; 
9281: 49 FF           EOR     #$FF                ; 
9283: 18              CLC                         ; 
9284: 69 01           ADC     #$01                ; 
9286: 18              CLC                         ; 
9287: 65 00           ADC     <$00                ; {ram.GP_00}
9289: 85 04           STA     <$04                ; {ram.0004}
928B: A0 00           LDY     #$00                ; 
928D: A5 01           LDA     <$01                ; {ram.GP_01}
928F: C5 03           CMP     <$03                ; {ram.GP_03}
9291: F0 0A           BEQ     $929D               ; {}
9293: BD 12 04        LDA     $0412,X             ; {ram.0412}
9296: 18              CLC                         ; 
9297: 69 10           ADC     #$10                ; 
9299: 9D 12 04        STA     $0412,X             ; {ram.0412}
929C: C8              INY                         ; 
929D: 60              RTS                         ; 
929E: A4 00           LDY     <$00                ; {ram.GP_00}
92A0: 20 A5 92        JSR     $92A5               ; {}
92A3: A4 01           LDY     <$01                ; {ram.GP_01}
92A5: A2 01           LDX     #$01                ; 
92A7: B9 03 02        LDA     $0203,Y             ; 
92AA: 18              CLC                         ; 
92AB: 7D F9 6E        ADC     $6EF9,X             ; 
92AE: C9 E9           CMP     #$E9                ; 
92B0: B0 04           BCS     $92B6               ; {}
92B2: C9 18           CMP     #$18                ; 
92B4: B0 08           BCS     $92BE               ; {}
92B6: B9 02 02        LDA     $0202,Y             ; {ram.0202}
92B9: 09 20           ORA     #$20                ; 
92BB: 99 02 02        STA     $0202,Y             ; {ram.0202}
92BE: CA              DEX                         ; 
92BF: 10 E6           BPL     $92A7               ; {}
92C1: 60              RTS                         ; 
92C2: A9 10           LDA     #$10                ; 
92C4: 9D 85 04        STA     $0485,X             ; 
92C7: A4 16           LDY     <$16                ; {ram.0016}
92C9: B9 2D 06        LDA     $062D,Y             ; 
92CC: F0 05           BEQ     $92D3               ; {}
92CE: A9 40           LDA     #$40                ; 
92D0: 9D 85 04        STA     $0485,X             ; 
92D3: 4C 25 80        JMP     $8025               ; {}
92D6: B5 98           LDA     $98,X               ; {ram.0098}
92D8: 9D F8 03        STA     $03F8,X             ; {ram.03F8}
92DB: 48              PHA                         ; 
92DC: AD 6C 06        LDA     $066C               ; {ram.066C}
92DF: 15 3D           ORA     $3D,X               ; {ram.003D}
92E1: D0 21           BNE     $9304               ; {}
92E3: 20 D0 EF        JSR     $EFD0               ; 
92E6: BD 94 03        LDA     $0394,X             ; {ram.0394}
92E9: 29 0F           AND     #$0F                ; 
92EB: D0 03           BNE     $92F0               ; {}
92ED: 9D 94 03        STA     $0394,X             ; {ram.0394}
92F0: BD BC 03        LDA     $03BC,X             ; {ram.03BC}
92F3: C9 60           CMP     #$60                ; 
92F5: F0 0D           BEQ     $9304               ; {}
92F7: B5 28           LDA     $28,X               ; {ram.0028}
92F9: D0 09           BNE     $9304               ; {}
92FB: B5 18           LDA     $18,X               ; {ram.0018}
92FD: 29 3F           AND     #$3F                ; 
92FF: 95 28           STA     $28,X               ; {ram.0028}
9301: 20 DF F1        JSR     $F1DF               ; 
9304: 68              PLA                         ; 
9305: D5 98           CMP     $98,X               ; {ram.0098}
9307: F0 05           BEQ     $930E               ; {}
9309: A9 20           LDA     #$20                ; 
930B: 9D BC 03        STA     $03BC,X             ; {ram.03BC}
930E: BD BC 03        LDA     $03BC,X             ; {ram.03BC}
9311: C9 20           CMP     #$20                ; 
9313: D0 22           BNE     $9337               ; {}
9315: BD 94 03        LDA     $0394,X             ; {ram.0394}
9318: D0 1D           BNE     $9337               ; {}
931A: A5 70           LDA     <$70                ; {ram.0070}
931C: 38              SEC                         ; 
931D: F5 70           SBC     $70,X               ; {ram.0070}
931F: 20 1F 70        JSR     $701F               ; {ram.701F}
9322: C9 08           CMP     #$08                ; 
9324: B0 39           BCS     $935F               ; {}
9326: A9 08           LDA     #$08                ; 
9328: 95 98           STA     $98,X               ; {ram.0098}
932A: A5 84           LDA     <$84                ; {ram.0084}
932C: D5 84           CMP     $84,X               ; {ram.0084}
932E: 90 02           BCC     $9332               ; {}
9330: 56 98           LSR     $98,X               ; {ram.0098}
9332: A9 60           LDA     #$60                ; 
9334: 9D BC 03        STA     $03BC,X             ; {ram.03BC}
9337: A9 0A           LDA     #$0A                ; 
9339: 20 89 FA        JSR     $FA89               ; 
933C: B5 98           LDA     $98,X               ; {ram.0098}
933E: 29 02           AND     #$02                ; 
9340: 4A              LSR     A                   ; 
9341: 85 0F           STA     <$0F                ; {ram.000F}
9343: A9 02           LDA     #$02                ; 
9345: 20 88 79        JSR     $7988               ; {ram.7988}
9348: A4 16           LDY     <$16                ; {ram.0016}
934A: B9 2D 06        LDA     $062D,Y             ; 
934D: F0 07           BEQ     $9356               ; {}
934F: A5 15           LDA     <$15                ; {ram.0015}
9351: 29 03           AND     #$03                ; 
9353: 20 88 79        JSR     $7988               ; {ram.7988}
9356: BD E4 03        LDA     $03E4,X             ; {ram.03E4}
9359: 20 DF 77        JSR     $77DF               ; {ram.77DF}
935C: 4C D0 79        JMP     $79D0               ; {ram.79D0}
935F: A5 84           LDA     <$84                ; {ram.0084}
9361: 38              SEC                         ; 
9362: F5 84           SBC     $84,X               ; {ram.0084}
9364: 20 1F 70        JSR     $701F               ; {ram.701F}
9367: C9 08           CMP     #$08                ; 
9369: B0 CC           BCS     $9337               ; {}
936B: A9 02           LDA     #$02                ; 
936D: 95 98           STA     $98,X               ; {ram.0098}
936F: A5 70           LDA     <$70                ; {ram.0070}
9371: D5 70           CMP     $70,X               ; {ram.0070}
9373: B0 BB           BCS     $9330               ; {}
9375: 90 BB           BCC     $9332               ; {}
9377: A9 80           LDA     #$80                ; 
9379: 20 6E 80        JSR     $806E               ; {}
937C: 20 D0 79        JSR     $79D0               ; {ram.79D0}
937F: A9 08           LDA     #$08                ; 
9381: 20 76 84        JSR     $8476               ; {}
9384: A9 20           LDA     #$20                ; 
9386: 85 01           STA     <$01                ; {ram.GP_01}
9388: A4 16           LDY     <$16                ; {ram.0016}
938A: B9 2D 06        LDA     $062D,Y             ; 
938D: F0 52           BEQ     $93E1               ; {}
938F: BD 51 04        LDA     $0451,X             ; 
9392: D0 06           BNE     $939A               ; {}
9394: B5 18           LDA     $18,X               ; {ram.0018}
9396: C9 F8           CMP     #$F8                ; 
9398: 90 47           BCC     $93E1               ; {}
939A: A5 01           LDA     <$01                ; {ram.GP_01}
939C: 48              PHA                         ; 
939D: A0 00           LDY     #$00                ; 
939F: BD F0 04        LDA     $04F0,X             ; {ram.04F0}
93A2: D0 0D           BNE     $93B1               ; {}
93A4: BC 51 04        LDY     $0451,X             ; 
93A7: 88              DEY                         ; 
93A8: 10 07           BPL     $93B1               ; {}
93AA: BD 12 04        LDA     $0412,X             ; {ram.0412}
93AD: F0 2E           BEQ     $93DD               ; {}
93AF: A0 30           LDY     #$30                ; 
93B1: 98              TYA                         ; 
93B2: 9D 51 04        STA     $0451,X             ; 
93B5: F0 26           BEQ     $93DD               ; {}
93B7: C0 10           CPY     #$10                ; 
93B9: D0 1E           BNE     $93D9               ; {}
93BB: AD 6C 06        LDA     $066C               ; {ram.066C}
93BE: 15 3D           ORA     $3D,X               ; {ram.003D}
93C0: D0 17           BNE     $93D9               ; {}
93C2: A9 57           LDA     #$57                ; 
93C4: 85 00           STA     <$00                ; {ram.GP_00}
93C6: 20 79 B1        JSR     $B179               ; {}
93C9: 90 07           BCC     $93D2               ; {}
93CB: A9 80           LDA     #$80                ; 
93CD: 95 28           STA     $28,X               ; {ram.0028}
93CF: DE 37 04        DEC     $0437,X             ; {ram.0437}
93D2: 90 09           BCC     $93DD               ; {}
93D4: A9 00           LDA     #$00                ; 
93D6: 9D 12 04        STA     $0412,X             ; {ram.0412}
93D9: 68              PLA                         ; 
93DA: A9 00           LDA     #$00                ; 
93DC: 48              PHA                         ; 
93DD: 68              PLA                         ; 
93DE: 9D BC 03        STA     $03BC,X             ; {ram.03BC}
93E1: 60              RTS                         ; 
93E2: A0 09           LDY     #$09                ; 
93E4: A9 80           LDA     #$80                ; 
93E6: 99 71 00        STA     $0071,Y             ; {ram.0071}
93E9: A9 70           LDA     #$70                ; 
93EB: 99 85 00        STA     $0085,Y             ; {ram.0085}
93EE: A9 00           LDA     #$00                ; 
93F0: 99 99 00        STA     $0099,Y             ; {ram.0099}
93F3: 99 BD 03        STA     $03BD,Y             ; 
93F6: 99 06 04        STA     $0406,Y             ; {ram.0406}
93F9: 99 93 04        STA     $0493,Y             ; 
93FC: AD C0 04        LDA     $04C0               ; {ram.04C0}
93FF: 99 C0 04        STA     $04C0,Y             ; {ram.04C0}
9402: AD 86 04        LDA     $0486               ; {ram.0486}
9405: 99 86 04        STA     $0486,Y             ; {ram.0486}
9408: A9 80           LDA     #$80                ; 
940A: 99 20 04        STA     $0420,Y             ; {ram.0420}
940D: A9 02           LDA     #$02                ; 
940F: 99 45 04        STA     $0445,Y             ; {ram.0445}
9412: A9 41           LDA     #$41                ; 
9414: 99 50 03        STA     $0350,Y             ; {ram.0350}
9417: 88              DEY                         ; 
9418: 10 CA           BPL     $93E4               ; {}
941A: A5 1D           LDA     <$1D                ; {ram.001D}
941C: 29 07           AND     #$07                ; 
941E: A8              TAY                         ; 
941F: B9 4E B2        LDA     $B24E,Y             ; {}
9422: 85 9D           STA     <$9D                ; {ram.009D}
9424: 8D 85 03        STA     $0385               ; {ram.0385}
9427: A5 22           LDA     <$22                ; {ram.0022}
9429: 29 07           AND     #$07                ; 
942B: A8              TAY                         ; 
942C: B9 4E B2        LDA     $B24E,Y             ; {}
942F: 85 A2           STA     <$A2                ; {ram.00A2}
9431: 8D 8A 03        STA     $038A               ; {ram.038A}
9434: A9 01           LDA     #$01                ; 
9436: 8D 31 04        STA     $0431               ; {ram.0431}
9439: 8D 36 04        STA     $0436               ; {ram.0436}
943C: A9 80           LDA     #$80                ; 
943E: 8D D1 04        STA     $04D1               ; {ram.04D1}
9441: A9 08           LDA     #$08                ; 
9443: 8D 4E 03        STA     $034E               ; {ram.034E}
9446: 60              RTS                         ; 
9447: A9 E2           LDA     #$E2                ; 
9449: 9D B2 04        STA     $04B2,X             ; 
944C: A9 10           LDA     #$10                ; 
944E: 8D 01 06        STA     $0601               ; {ram.??SND_601??} ??SND_601??
9451: A9 B0           LDA     #$B0                ; 
9453: 95 70           STA     $70,X               ; {ram.0070}
9455: A9 80           LDA     #$80                ; 
9457: 95 84           STA     $84,X               ; {ram.0084}
9459: 60              RTS                         ; 
945A: A9 40           LDA     #$40                ; 
945C: 8D 01 06        STA     $0601               ; {ram.??SND_601??}
945F: B5 18           LDA     $18,X               ; {ram.0018}
9461: 29 07           AND     #$07                ; 
9463: A8              TAY                         ; 
9464: B9 4E B2        LDA     $B24E,Y             ; {}
9467: 95 98           STA     $98,X               ; {ram.0098}
9469: A9 3F           LDA     #$3F                ; 
946B: 9D 1F 04        STA     $041F,X             ; {ram.041F}
946E: A9 80           LDA     #$80                ; 
9470: 9D 37 04        STA     $0437,X             ; {ram.0437}
9473: A9 03           LDA     #$03                ; 
9475: 8D 07 05        STA     $0507               ; {ram.0507}
9478: 60              RTS                         ; 
9479: 20 5A 94        JSR     $945A               ; {}
947C: A9 38           LDA     #$38                ; 
947E: 9D 4F 03        STA     $034F,X             ; {ram.034F}
9481: A9 01           LDA     #$01                ; 
9483: 8D 07 05        STA     $0507               ; {ram.0507}
9486: 60              RTS                         ; 
9487: A9 20           LDA     #$20                ; 
9489: 8D 01 06        STA     $0601               ; {ram.??SND_601??}
948C: A0 01           LDY     #$01                ; 
948E: B5 18           LDA     $18,X               ; {ram.0018}
9490: C9 80           CMP     #$80                ; 
9492: 90 01           BCC     $9495               ; {}
9494: C8              INY                         ; 
9495: 94 98           STY     $98,X               ; {ram.0098}
9497: 60              RTS                         ; 
9498: B5 98           LDA     $98,X               ; {ram.0098}
949A: F0 65           BEQ     $9501               ; {}
949C: AD 6C 06        LDA     $066C               ; {ram.066C}
949F: D0 06           BNE     $94A7               ; {}
94A1: 20 02 95        JSR     $9502               ; {}
94A4: 20 88 B2        JSR     $B288               ; {}
94A7: A9 02           LDA     #$02                ; 
94A9: 85 03           STA     <$03                ; {ram.GP_03}
94AB: A9 44           LDA     #$44                ; 
94AD: 20 91 79        JSR     $7991               ; {ram.7991}
94B0: B5 98           LDA     $98,X               ; {ram.0098}
94B2: 48              PHA                         ; 
94B3: B5 28           LDA     $28,X               ; {ram.0028}
94B5: 48              PHA                         ; 
94B6: 20 D0 79        JSR     $79D0               ; {ram.79D0}
94B9: 68              PLA                         ; 
94BA: 95 28           STA     $28,X               ; {ram.0028}
94BC: 68              PLA                         ; 
94BD: 95 98           STA     $98,X               ; {ram.0098}
94BF: BD 05 04        LDA     $0405,X             ; {ram.0405}
94C2: F0 3D           BEQ     $9501               ; {}
94C4: A9 20           LDA     #$20                ; 
94C6: 9D 85 04        STA     $0485,X             ; 
94C9: 20 9A 97        JSR     $979A               ; {}
94CC: A0 FF           LDY     #$FF                ; 
94CE: E0 06           CPX     #$06                ; 
94D0: 90 02           BCC     $94D4               ; {}
94D2: A0 04           LDY     #$04                ; 
94D4: C8              INY                         ; 
94D5: B9 50 03        LDA     $0350,Y             ; {ram.0350}
94D8: C9 41           CMP     #$41                ; 
94DA: D0 F8           BNE     $94D4               ; {}
94DC: A9 11           LDA     #$11                ; 
94DE: 99 29 00        STA     $0029,Y             ; {ram.0029}
94E1: BD F0 04        LDA     $04F0,X             ; {ram.04F0}
94E4: 99 F1 04        STA     $04F1,Y             ; 
94E7: B5 70           LDA     $70,X               ; {ram.0070}
94E9: 99 71 00        STA     $0071,Y             ; {ram.0071}
94EC: B5 84           LDA     $84,X               ; {ram.0084}
94EE: 99 85 00        STA     $0085,Y             ; {ram.0085}
94F1: C0 04           CPY     #$04                ; 
94F3: F0 0C           BEQ     $9501               ; {}
94F5: C0 09           CPY     #$09                ; 
94F7: F0 08           BEQ     $9501               ; {}
94F9: A9 5D           LDA     #$5D                ; 
94FB: 99 50 03        STA     $0350,Y             ; {ram.0350}
94FE: 20 DA FE        JSR     $FEDA               ; 
9501: 60              RTS                         ; 
9502: BD 44 04        LDA     $0444,X             ; 
9505: 20 E2 E5        JSR     $E5E2               ; 
9508: 10 95           BPL     $949F               ; {}
950A: 10 95           BPL     $94A1               ; {}
950C: 10 95           BPL     $94A3               ; {}
950E: 2B                              ;
950F: 95 E0           STA     $E0,X               ; {ram.??SND_E0??}
9511: 05 F0           ORA     <$F0                ; {ram.00F0}
9513: 04                              ;
9514: E0 0A           CPX     #$0A                ; 
9516: D0 53           BNE     $956B               ; {}
9518: 20 08 B3        JSR     $B308               ; {}
951B: B5 28           LDA     $28,X               ; {ram.0028}
951D: D0 1B           BNE     $953A               ; {}
951F: 20 6C 95        JSR     $956C               ; {}
9522: A9 10           LDA     #$10                ; 
9524: 95 28           STA     $28,X               ; {ram.0028}
9526: B5 97           LDA     $97,X               ; {ram.0097}
9528: D0 10           BNE     $953A               ; {}
952A: 60              RTS                         ; 
952B: E0 05           CPX     #$05                ; 
952D: F0 04           BEQ     $9533               ; {}
952F: E0 0A           CPX     #$0A                ; 
9531: D0 38           BNE     $956B               ; {}
9533: 20 78 B3        JSR     $B378               ; {}
9536: B5 28           LDA     $28,X               ; {ram.0028}
9538: F0 E5           BEQ     $951F               ; {}
953A: B5 28           LDA     $28,X               ; {ram.0028}
953C: C9 10           CMP     #$10                ; 
953E: D0 2B           BNE     $956B               ; {}
9540: BD BC 03        LDA     $03BC,X             ; {ram.03BC}
9543: F0 07           BEQ     $954C               ; {}
9545: 95 98           STA     $98,X               ; {ram.0098}
9547: A9 00           LDA     #$00                ; 
9549: 9D BC 03        STA     $03BC,X             ; {ram.03BC}
954C: A9 04           LDA     #$04                ; 
954E: 85 00           STA     <$00                ; {ram.GP_00}
9550: A0 00           LDY     #$00                ; 
9552: E0 05           CPX     #$05                ; 
9554: F0 02           BEQ     $9558               ; {}
9556: A0 05           LDY     #$05                ; 
9558: B9 82 03        LDA     $0382,Y             ; {ram.0382}
955B: 99 81 03        STA     $0381,Y             ; {ram.0381}
955E: 99 99 00        STA     $0099,Y             ; {ram.0099}
9561: C8              INY                         ; 
9562: C6 00           DEC     <$00                ; {ram.GP_00}
9564: D0 F2           BNE     $9558               ; {}
9566: B5 98           LDA     $98,X               ; {ram.0098}
9568: 9D 80 03        STA     $0380,X             ; 
956B: 60              RTS                         ; 
956C: A0 02           LDY     #$02                ; 
956E: B5 18           LDA     $18,X               ; {ram.0018}
9570: C9 40           CMP     #$40                ; 
9572: B0 01           BCS     $9575               ; {}
9574: C8              INY                         ; 
9575: 98              TYA                         ; 
9576: 9D 44 04        STA     $0444,X             ; 
9579: A9 08           LDA     #$08                ; 
957B: 9D 2C 04        STA     $042C,X             ; {ram.!SplashMode}
957E: 60              RTS                         ; 
957F: 00              BRK                         ; 
9580: 10 00           BPL     $9582               ; {}
9582: F0 00           BEQ     $9584               ; {}
9584: 10 F0           BPL     $9576               ; {}
9586: 10 88           BPL     $9510               ; {}
9588: D0 0F           BNE     $9599               ; {}
958A: BD 6B 04        LDA     $046B,X             ; 
958D: D0 6D           BNE     $95FC               ; {}
958F: A9 40           LDA     #$40                ; 
9591: 95 28           STA     $28,X               ; {ram.0028}
9593: EE 1B 05        INC     $051B               ; {ram.051B}
9596: 4C 21 96        JMP     $9621               ; {}
9599: B5 28           LDA     $28,X               ; {ram.0028}
959B: F0 11           BEQ     $95AE               ; {}
959D: 29 07           AND     #$07                ; 
959F: D0 0A           BNE     $95AB               ; {}
95A1: BD 6B 04        LDA     $046B,X             ; 
95A4: 49 01           EOR     #$01                ; 
95A6: 9D 6B 04        STA     $046B,X             ; 
95A9: F0 76           BEQ     $9621               ; {}
95AB: 4C 58 96        JMP     $9658               ; {}
95AE: CE 1B 05        DEC     $051B               ; {ram.051B}
95B1: AD 07 05        LDA     $0507               ; {ram.0507}
95B4: 85 00           STA     <$00                ; {ram.GP_00}
95B6: 8D 4E 03        STA     $034E               ; {ram.034E}
95B9: 8A              TXA                         ; 
95BA: 48              PHA                         ; 
95BB: E8              INX                         ; 
95BC: 20 5A 94        JSR     $945A               ; {}
95BF: A9 18           LDA     #$18                ; 
95C1: 9D 4F 03        STA     $034F,X             ; {ram.034F}
95C4: FE 44 04        INC     $0444,X             ; 
95C7: A9 01           LDA     #$01                ; 
95C9: 9D 6B 04        STA     $046B,X             ; 
95CC: A9 00           LDA     #$00                ; 
95CE: 9D 5E 04        STA     $045E,X             ; 
95D1: A5 71           LDA     <$71                ; {ram.0071}
95D3: 95 70           STA     $70,X               ; {ram.0070}
95D5: A5 85           LDA     <$85                ; {ram.0085}
95D7: 95 84           STA     $84,X               ; {ram.0084}
95D9: C6 00           DEC     <$00                ; {ram.GP_00}
95DB: D0 DE           BNE     $95BB               ; {}
95DD: 68              PLA                         ; 
95DE: AA              TAX                         ; 
95DF: 20 10 B0        JSR     $B010               ; {}
95E2: A9 00           LDA     #$00                ; 
95E4: 9D 4F 03        STA     $034F,X             ; {ram.034F}
95E7: 4C 58 96        JMP     $9658               ; {}
95EA: 20 1A B3        JSR     $B31A               ; {}
95ED: 4C 10 96        JMP     $9610               ; {}
95F0: AD 6C 06        LDA     $066C               ; {ram.066C}
95F3: 15 3D           ORA     $3D,X               ; {ram.003D}
95F5: D0 1C           BNE     $9613               ; {}
95F7: AC 1B 05        LDY     $051B               ; {ram.051B}
95FA: D0 8B           BNE     $9587               ; {}
95FC: 20 8E 96        JSR     $968E               ; {}
95FF: B5 28           LDA     $28,X               ; {ram.0028}
9601: D0 0D           BNE     $9610               ; {}
9603: A9 10           LDA     #$10                ; 
9605: 95 28           STA     $28,X               ; {ram.0028}
9607: B5 18           LDA     $18,X               ; {ram.0018}
9609: C9 80           CMP     #$80                ; 
960B: B0 DD           BCS     $95EA               ; {}
960D: 20 88 B3        JSR     $B388               ; {}
9610: 20 EB 96        JSR     $96EB               ; {}
9613: BD 6B 04        LDA     $046B,X             ; 
9616: F0 09           BEQ     $9621               ; {}
9618: 20 CD B2        JSR     $B2CD               ; {}
961B: 20 D0 79        JSR     $79D0               ; {ram.79D0}
961E: 4C 48 97        JMP     $9748               ; {}
9621: B5 70           LDA     $70,X               ; {ram.0070}
9623: 48              PHA                         ; 
9624: B5 84           LDA     $84,X               ; {ram.0084}
9626: 48              PHA                         ; 
9627: A9 00           LDA     #$00                ; 
9629: 9D 78 04        STA     $0478,X             ; 
962C: BC 78 04        LDY     $0478,X             ; 
962F: B5 70           LDA     $70,X               ; {ram.0070}
9631: 18              CLC                         ; 
9632: 79 7F 95        ADC     $957F,Y             ; {}
9635: 95 70           STA     $70,X               ; {ram.0070}
9637: B5 84           LDA     $84,X               ; {ram.0084}
9639: 18              CLC                         ; 
963A: 79 83 95        ADC     $9583,Y             ; {}
963D: 95 84           STA     $84,X               ; {ram.0084}
963F: 20 CD B2        JSR     $B2CD               ; {}
9642: 20 D0 79        JSR     $79D0               ; {ram.79D0}
9645: FE 78 04        INC     $0478,X             ; 
9648: BD 78 04        LDA     $0478,X             ; 
964B: C9 04           CMP     #$04                ; 
964D: 90 DD           BCC     $962C               ; {}
964F: 68              PLA                         ; 
9650: 95 84           STA     $84,X               ; {ram.0084}
9652: 68              PLA                         ; 
9653: 95 70           STA     $70,X               ; {ram.0070}
9655: 20 48 97        JSR     $9748               ; {}
9658: B5 70           LDA     $70,X               ; {ram.0070}
965A: 48              PHA                         ; 
965B: B5 84           LDA     $84,X               ; {ram.0084}
965D: 48              PHA                         ; 
965E: 18              CLC                         ; 
965F: 69 08           ADC     #$08                ; 
9661: 95 84           STA     $84,X               ; {ram.0084}
9663: B5 70           LDA     $70,X               ; {ram.0070}
9665: 18              CLC                         ; 
9666: 69 08           ADC     #$08                ; 
9668: 95 70           STA     $70,X               ; {ram.0070}
966A: BD 6B 04        LDA     $046B,X             ; 
966D: 48              PHA                         ; 
966E: BD 4F 03        LDA     $034F,X             ; {ram.034F}
9671: 48              PHA                         ; 
9672: A9 18           LDA     #$18                ; 
9674: 9D 4F 03        STA     $034F,X             ; {ram.034F}
9677: A9 01           LDA     #$01                ; 
9679: 9D 6B 04        STA     $046B,X             ; 
967C: 20 48 97        JSR     $9748               ; {}
967F: 68              PLA                         ; 
9680: 9D 4F 03        STA     $034F,X             ; {ram.034F}
9683: 68              PLA                         ; 
9684: 9D 6B 04        STA     $046B,X             ; 
9687: 68              PLA                         ; 
9688: 95 84           STA     $84,X               ; {ram.0084}
968A: 68              PLA                         ; 
968B: 95 70           STA     $70,X               ; {ram.0070}
968D: 60              RTS                         ; 
968E: BD 5E 04        LDA     $045E,X             ; 
9691: 20 E2 E5        JSR     $E5E2               ; 
9694: 98              TYA                         ; 
9695: 96 B8           STX     $B8,Y               ; 
9697: 96 FE           STX     $FE,Y               ; {ram.CUR_2001}
9699: 1F                              ;
969A: 04                              ;
969B: D0 03           BNE     $96A0               ; {}
969D: FE 2C 04        INC     $042C,X             ; {ram.!SplashMode}
96A0: BD 1F 04        LDA     $041F,X             ; {ram.041F}
96A3: DD 37 04        CMP     $0437,X             ; {ram.0437}
96A6: D0 42           BNE     $96EA               ; {}
96A8: BD 2C 04        LDA     $042C,X             ; {ram.!SplashMode}
96AB: DD 44 04        CMP     $0444,X             ; 
96AE: D0 3A           BNE     $96EA               ; {}
96B0: FE 5E 04        INC     $045E,X             ; 
96B3: A9 40           LDA     #$40                ; 
96B5: 4C DA 96        JMP     $96DA               ; {}
96B8: DE 1F 04        DEC     $041F,X             ; {ram.041F}
96BB: BD 1F 04        LDA     $041F,X             ; {ram.041F}
96BE: C9 FF           CMP     #$FF                ; 
96C0: D0 03           BNE     $96C5               ; {}
96C2: DE 2C 04        DEC     $042C,X             ; {ram.!SplashMode}
96C5: BD 1F 04        LDA     $041F,X             ; {ram.041F}
96C8: DD 37 04        CMP     $0437,X             ; {ram.0437}
96CB: D0 1D           BNE     $96EA               ; {}
96CD: BD 2C 04        LDA     $042C,X             ; {ram.!SplashMode}
96D0: DD 44 04        CMP     $0444,X             ; 
96D3: D0 15           BNE     $96EA               ; {}
96D5: DE 5E 04        DEC     $045E,X             ; 
96D8: A9 80           LDA     #$80                ; 
96DA: 9D 37 04        STA     $0437,X             ; {ram.0437}
96DD: A9 00           LDA     #$00                ; 
96DF: 9D 44 04        STA     $0444,X             ; 
96E2: BD 6B 04        LDA     $046B,X             ; 
96E5: F0 03           BEQ     $96EA               ; {}
96E7: FE 44 04        INC     $0444,X             ; 
96EA: 60              RTS                         ; 
96EB: BD 1F 04        LDA     $041F,X             ; {ram.041F}
96EE: 29 E0           AND     #$E0                ; 
96F0: 18              CLC                         ; 
96F1: 7D 12 04        ADC     $0412,X             ; {ram.0412}
96F4: 9D 12 04        STA     $0412,X             ; {ram.0412}
96F7: BD 2C 04        LDA     $042C,X             ; {ram.!SplashMode}
96FA: 69 00           ADC     #$00                ; 
96FC: 85 03           STA     <$03                ; {ram.GP_03}
96FE: A9 A1           LDA     #$A1                ; 
9700: 85 02           STA     <$02                ; {ram.GP_02}
9702: B5 98           LDA     $98,X               ; {ram.0098}
9704: 24 02           BIT     <$02                ; {ram.GP_02}
9706: F0 07           BEQ     $970F               ; {}
9708: B5 70           LDA     $70,X               ; {ram.0070}
970A: 18              CLC                         ; 
970B: 65 03           ADC     <$03                ; {ram.GP_03}
970D: 95 70           STA     $70,X               ; {ram.0070}
970F: B5 98           LDA     $98,X               ; {ram.0098}
9711: 06 02           ASL     <$02                ; {ram.GP_02}
9713: 24 02           BIT     <$02                ; {ram.GP_02}
9715: F0 06           BEQ     $971D               ; {}
9717: B5 70           LDA     $70,X               ; {ram.0070}
9719: E5 03           SBC     <$03                ; {ram.GP_03}
971B: 95 70           STA     $70,X               ; {ram.0070}
971D: B5 98           LDA     $98,X               ; {ram.0098}
971F: 06 02           ASL     <$02                ; {ram.GP_02}
9721: 24 02           BIT     <$02                ; {ram.GP_02}
9723: F0 06           BEQ     $972B               ; {}
9725: B5 84           LDA     $84,X               ; {ram.0084}
9727: 65 03           ADC     <$03                ; {ram.GP_03}
9729: 95 84           STA     $84,X               ; {ram.0084}
972B: B5 98           LDA     $98,X               ; {ram.0098}
972D: 06 02           ASL     <$02                ; {ram.GP_02}
972F: 24 02           BIT     <$02                ; {ram.GP_02}
9731: F0 06           BEQ     $9739               ; {}
9733: B5 84           LDA     $84,X               ; {ram.0084}
9735: E5 03           SBC     <$03                ; {ram.GP_03}
9737: 95 84           STA     $84,X               ; {ram.0084}
9739: 4C 93 FA        JMP     $FA93               ; 
973C: 00              BRK                         ; 
973D: 10 00           BPL     $973F               ; {}
973F: 10 00           BPL     $9741               ; {}
9741: 00              BRK                         ; 
9742: 10 10           BPL     $9754               ; {}
9744: 03                              ;
9745: 03                              ;
9746: 83                              ;
9747: 83                              ;
9748: A9 06           LDA     #$06                ; 
974A: 20 89 FA        JSR     $FA89               ; 
974D: BD 6B 04        LDA     $046B,X             ; 
9750: D0 2B           BNE     $977D               ; {}
9752: A0 00           LDY     #$00                ; 
9754: B5 70           LDA     $70,X               ; {ram.0070}
9756: 18              CLC                         ; 
9757: 79 3C 97        ADC     $973C,Y             ; {}
975A: 85 00           STA     <$00                ; {ram.GP_00}
975C: B5 84           LDA     $84,X               ; {ram.0084}
975E: 18              CLC                         ; 
975F: 79 40 97        ADC     $9740,Y             ; {}
9762: 85 01           STA     <$01                ; {ram.GP_01}
9764: B9 44 97        LDA     $9744,Y             ; {}
9767: 20 88 79        JSR     $7988               ; {ram.7988}
976A: 98              TYA                         ; 
976B: 48              PHA                         ; 
976C: 29 01           AND     #$01                ; 
976E: 85 0F           STA     <$0F                ; {ram.000F}
9770: A9 00           LDA     #$00                ; 
9772: 20 DF 77        JSR     $77DF               ; {ram.77DF}
9775: 68              PLA                         ; 
9776: A8              TAY                         ; 
9777: C8              INY                         ; 
9778: C0 04           CPY     #$04                ; 
977A: D0 D8           BNE     $9754               ; {}
977C: 60              RTS                         ; 
977D: 20 FB 9A        JSR     $9AFB               ; {}
9780: BD E4 03        LDA     $03E4,X             ; {ram.03E4}
9783: 4C DB 77        JMP     $77DB               ; {ram.77DB}
9786: AD 6C 06        LDA     $066C               ; {ram.066C}
9789: D0 06           BNE     $9791               ; {}
978B: 20 A2 97        JSR     $97A2               ; {}
978E: 20 EF 97        JSR     $97EF               ; {}
9791: 20 4C 98        JSR     $984C               ; {}
9794: 20 D0 79        JSR     $79D0               ; {ram.79D0}
9797: 20 00 80        JSR     $8000               ; {}
979A: 20 0D 80        JSR     $800D               ; {}
979D: 4C E4 EE        JMP     $EEE4               ; 
97A0: 01 FF           ORA     ($FF,X)             ; {ram.CUR_2000}
97A2: BD 94 03        LDA     $0394,X             ; {ram.0394}
97A5: D0 12           BNE     $97B9               ; {}
97A7: B5 18           LDA     $18,X               ; {ram.0018}
97A9: 48              PHA                         ; 
97AA: 29 0F           AND     #$0F                ; 
97AC: 09 07           ORA     #$07                ; 
97AE: 9D 94 03        STA     $0394,X             ; {ram.0394}
97B1: 68              PLA                         ; 
97B2: 29 01           AND     #$01                ; 
97B4: A8              TAY                         ; 
97B5: C8              INY                         ; 
97B6: 94 98           STY     $98,X               ; {ram.0098}
97B8: 60              RTS                         ; 
97B9: A5 15           LDA     <$15                ; {ram.0015}
97BB: 29 07           AND     #$07                ; 
97BD: D0 2F           BNE     $97EE               ; {}
97BF: B5 70           LDA     $70,X               ; {ram.0070}
97C1: C9 88           CMP     #$88                ; 
97C3: B0 0A           BCS     $97CF               ; {}
97C5: A9 88           LDA     #$88                ; 
97C7: 95 70           STA     $70,X               ; {ram.0070}
97C9: A9 01           LDA     #$01                ; 
97CB: 95 98           STA     $98,X               ; {ram.0098}
97CD: D0 0C           BNE     $97DB               ; {}
97CF: C9 C8           CMP     #$C8                ; 
97D1: 90 0D           BCC     $97E0               ; {}
97D3: A9 C7           LDA     #$C7                ; 
97D5: 95 70           STA     $70,X               ; {ram.0070}
97D7: A9 02           LDA     #$02                ; 
97D9: 95 98           STA     $98,X               ; {ram.0098}
97DB: A9 07           LDA     #$07                ; 
97DD: 9D 94 03        STA     $0394,X             ; {ram.0394}
97E0: B4 98           LDY     $98,X               ; {ram.0098}
97E2: 88              DEY                         ; 
97E3: B5 70           LDA     $70,X               ; {ram.0070}
97E5: 18              CLC                         ; 
97E6: 79 A0 97        ADC     $97A0,Y             ; {}
97E9: 95 70           STA     $70,X               ; {ram.0070}
97EB: DE 94 03        DEC     $0394,X             ; {ram.0394}
97EE: 60              RTS                         ; 
97EF: B5 28           LDA     $28,X               ; {ram.0028}
97F1: D0 1F           BNE     $9812               ; {}
97F3: B5 18           LDA     $18,X               ; {ram.0018}
97F5: 09 70           ORA     #$70                ; 
97F7: 95 28           STA     $28,X               ; {ram.0028}
97F9: 20 2F 98        JSR     $982F               ; {}
97FC: A9 00           LDA     #$00                ; 
97FE: 99 78 04        STA     $0478,Y             ; 
9801: 20 2F 98        JSR     $982F               ; {}
9804: A9 01           LDA     #$01                ; 
9806: 99 78 04        STA     $0478,Y             ; 
9809: 20 2F 98        JSR     $982F               ; {}
980C: A9 FF           LDA     #$FF                ; 
980E: 99 78 04        STA     $0478,Y             ; 
9811: 60              RTS                         ; 
9812: A2 0B           LDX     #$0B                ; 
9814: BD 4F 03        LDA     $034F,X             ; {ram.034F}
9817: C9 55           CMP     #$55                ; 
9819: D0 0D           BNE     $9828               ; {}
981B: A5 15           LDA     <$15                ; {ram.0015}
981D: 4A              LSR     A                   ; 
981E: B0 08           BCS     $9828               ; {}
9820: B5 84           LDA     $84,X               ; {ram.0084}
9822: 18              CLC                         ; 
9823: 7D 78 04        ADC     $0478,X             ; 
9826: 95 84           STA     $84,X               ; {ram.0084}
9828: CA              DEX                         ; 
9829: 10 E9           BPL     $9814               ; {}
982B: AE 40 03        LDX     $0340               ; {ram.0340}
982E: 60              RTS                         ; 
982F: A9 55           LDA     #$55                ; 
9831: 4C AF 82        JMP     $82AF               ; {}
9834: CC C4 C8        CPY     $C8C4               ; 
9837: C2                              ;
9838: C6 CA           DEC     <$CA                ; {ram.00CA}
983A: CC C4 C8        CPY     $C8C4               ; 
983D: CE D0 D2        DEC     $D2D0               ; 
9840: 00              BRK                         ; 
9841: 00              BRK                         ; 
9842: 00              BRK                         ; 
9843: 10 10           BPL     $9855               ; {}
9845: 10 00           BPL     $9847               ; {}
9847: 08              PHP                         ; 
9848: 10 00           BPL     $984A               ; {}
984A: 08              PHP                         ; 
984B: 10 A0           BPL     $97ED               ; {}
984D: 05 A5           ORA     <$A5                ; {ram.00A5}
984F: 15 29           ORA     $29,X               ; {ram.0029}
9851: 10 D0           BPL     $9823               ; {}
9853: 02                              ;
9854: A0 0B           LDY     #$0B                ; 
9856: 84 0A           STY     <$0A                ; {ram.000A}
9858: A9 05           LDA     #$05                ; 
985A: 85 0B           STA     <$0B                ; {ram.000B}
985C: A4 0B           LDY     <$0B                ; {ram.000B}
985E: B5 70           LDA     $70,X               ; {ram.0070}
9860: 18              CLC                         ; 
9861: 79 46 98        ADC     $9846,Y             ; {}
9864: 85 00           STA     <$00                ; {ram.GP_00}
9866: B5 84           LDA     $84,X               ; {ram.0084}
9868: 18              CLC                         ; 
9869: 79 40 98        ADC     $9840,Y             ; {}
986C: 85 01           STA     <$01                ; {ram.GP_01}
986E: BD F0 04        LDA     $04F0,X             ; {ram.04F0}
9871: 29 03           AND     #$03                ; 
9873: 49 03           EOR     #$03                ; 
9875: 85 03           STA     <$03                ; {ram.GP_03}
9877: A4 0A           LDY     <$0A                ; {ram.000A}
9879: B9 34 98        LDA     $9834,Y             ; {}
987C: CD 34 98        CMP     $9834               ; {}
987F: D0 08           BNE     $9889               ; {}
9881: B4 28           LDY     $28,X               ; {ram.0028}
9883: C0 20           CPY     #$20                ; 
9885: B0 02           BCS     $9889               ; {}
9887: A9 C0           LDA     #$C0                ; 
9889: 20 93 98        JSR     $9893               ; {}
988C: C6 0A           DEC     <$0A                ; {ram.000A}
988E: C6 0B           DEC     <$0B                ; {ram.000B}
9890: 10 CA           BPL     $985C               ; {}
9892: 60              RTS                         ; 
9893: 48              PHA                         ; 
9894: AC 41 03        LDY     $0341               ; {ram.0341}
9897: B9 AB 77        LDA     $77AB,Y             ; 
989A: A8              TAY                         ; 
989B: 68              PLA                         ; 
989C: 99 01 02        STA     $0201,Y             ; {ram.0201}
989F: A5 00           LDA     <$00                ; {ram.GP_00}
98A1: 99 03 02        STA     $0203,Y             ; 
98A4: A5 01           LDA     <$01                ; {ram.GP_01}
98A6: 4C AF 79        JMP     $79AF               ; {ram.79AF}
98A9: 20 BD 98        JSR     $98BD               ; {}
98AC: 20 5F 99        JSR     $995F               ; {}
98AF: 20 B9 99        JSR     $99B9               ; {}
98B2: 4C 84 9A        JMP     $9A84               ; {}
98B5: 10 F0           BPL     $98A7               ; {}
98B7: 10 FF           BPL     $98B8               ; {}
98B9: F0 20           BEQ     $98DB               ; {}
98BB: 40              RTI                         ; 
98BC: 40              RTI                         ; 
98BD: B5 AC           LDA     $AC,X               ; {ram.00AC}
98BF: 20 E2 E5        JSR     $E5E2               ; 
98C2: C8              INY                         ; 
98C3: 98              TYA                         ; 
98C4: 00              BRK                         ; 
98C5: 99 F2 98        STA     $98F2,Y             ; {}
98C8: A0 00           LDY     #$00                ; 
98CA: B5 98           LDA     $98,X               ; {ram.0098}
98CC: 29 0D           AND     #$0D                ; 
98CE: F0 09           BEQ     $98D9               ; {}
98D0: B5 70           LDA     $70,X               ; {ram.0070}
98D2: 18              CLC                         ; 
98D3: 69 10           ADC     #$10                ; 
98D5: 95 70           STA     $70,X               ; {ram.0070}
98D7: A0 F0           LDY     #$F0                ; 
98D9: 98              TYA                         ; 
98DA: 48              PHA                         ; 
98DB: A9 20           LDA     #$20                ; 
98DD: 9D 1F 04        STA     $041F,X             ; {ram.041F}
98E0: 20 94 80        JSR     $8094               ; {}
98E3: 68              PLA                         ; 
98E4: 18              CLC                         ; 
98E5: 75 70           ADC     <$70,X              ; {ram.0070}
98E7: 95 70           STA     $70,X               ; {ram.0070}
98E9: C9 20           CMP     #$20                ; 
98EB: B0 04           BCS     $98F1               ; {}
98ED: A9 01           LDA     #$01                ; 
98EF: 95 98           STA     $98,X               ; {ram.0098}
98F1: 60              RTS                         ; 
98F2: BC 3D 00        LDY     $003D,X             ; {ram.003D}
98F5: 88              DEY                         ; 
98F6: F0 60           BEQ     $9958               ; {}
98F8: 10 05           BPL     $98FF               ; {}
98FA: A9 20           LDA     #$20                ; 
98FC: 9D 3D 00        STA     $003D,X             ; {ram.003D}
98FF: 60              RTS                         ; 
9900: BD 2C 04        LDA     $042C,X             ; {ram.!SplashMode}
9903: 20 E2 E5        JSR     $E5E2               ; 
9906: 10 99           BPL     $98A1               ; {}
9908: 10 99           BPL     $98A3               ; {}
990A: 10 99           BPL     $98A5               ; {}
990C: 52                              ;
990D: 99 58 99        STA     $9958,Y             ; {}
9910: BC 5E 04        LDY     $045E,X             ; 
9913: 88              DEY                         ; 
9914: F0 22           BEQ     $9938               ; {}
9916: 10 36           BPL     $994E               ; {}
9918: BC 2C 04        LDY     $042C,X             ; {ram.!SplashMode}
991B: B9 BA 98        LDA     $98BA,Y             ; {}
991E: 9D 5E 04        STA     $045E,X             ; 
9921: C0 00           CPY     #$00                ; 
9923: D0 29           BNE     $994E               ; {}
9925: A0 10           LDY     #$10                ; 
9927: A9 00           LDA     #$00                ; 
9929: 99 AC 00        STA     $00AC,Y             ; {ram.00AC}
992C: BD 37 04        LDA     $0437,X             ; {ram.0437}
992F: 18              CLC                         ; 
9930: 69 01           ADC     #$01                ; 
9932: 9D 37 04        STA     $0437,X             ; {ram.0437}
9935: 4C 4E 99        JMP     $994E               ; {}
9938: FE 2C 04        INC     $042C,X             ; {ram.!SplashMode}
993B: BD 2C 04        LDA     $042C,X             ; {ram.!SplashMode}
993E: C9 02           CMP     #$02                ; 
9940: 90 0C           BCC     $994E               ; {}
9942: BC 37 04        LDY     $0437,X             ; {ram.0437}
9945: C0 02           CPY     #$02                ; 
9947: B0 05           BCS     $994E               ; {}
9949: A9 04           LDA     #$04                ; 
994B: 9D 2C 04        STA     $042C,X             ; {ram.!SplashMode}
994E: DE 5E 04        DEC     $045E,X             ; 
9951: 60              RTS                         ; 
9952: 20 A6 FE        JSR     $FEA6               ; 
9955: 20 10 B0        JSR     $B010               ; {}
9958: 20 55 F8        JSR     $F855               ; 
995B: 9D 2C 04        STA     $042C,X             ; {ram.!SplashMode}
995E: 60              RTS                         ; 
995F: 20 8A 99        JSR     $998A               ; {}
9962: BD F0 04        LDA     $04F0,X             ; {ram.04F0}
9965: D0 19           BNE     $9980               ; {}
9967: B5 98           LDA     $98,X               ; {ram.0098}
9969: C9 04           CMP     #$04                ; 
996B: B0 1C           BCS     $9989               ; {}
996D: B5 70           LDA     $70,X               ; {ram.0070}
996F: 48              PHA                         ; 
9970: 18              CLC                         ; 
9971: 69 10           ADC     #$10                ; 
9973: 95 70           STA     $70,X               ; {ram.0070}
9975: 20 8A 99        JSR     $998A               ; {}
9978: 68              PLA                         ; 
9979: 95 70           STA     $70,X               ; {ram.0070}
997B: BD F0 04        LDA     $04F0,X             ; {ram.04F0}
997E: F0 09           BEQ     $9989               ; {}
9980: 20 52 99        JSR     $9952               ; {}
9983: A9 0A           LDA     #$0A                ; 
9985: 85 50           STA     <$50                ; {ram.0050}
9987: 85 51           STA     <$51                ; {ram.0051}
9989: 60              RTS                         ; 
998A: A9 FF           LDA     #$FF                ; 
998C: 9D B2 04        STA     $04B2,X             ; 
998F: 20 D0 79        JSR     $79D0               ; {ram.79D0}
9992: B5 AC           LDA     $AC,X               ; {ram.00AC}
9994: C9 02           CMP     #$02                ; 
9996: D0 F1           BNE     $9989               ; {}
9998: A9 FE           LDA     #$FE                ; 
999A: 9D B2 04        STA     $04B2,X             ; 
999D: 20 2D 7A        JSR     $7A2D               ; {ram.7A2D}
99A0: A0 0D           LDY     #$0D                ; 
99A2: 4C 29 7D        JMP     $7D29               ; {ram.7D29}
99A5: F0 00           BEQ     $99A7               ; {}
99A7: F8              SED                         ; 
99A8: FF                              ;
99A9: F8              SED                         ; 
99AA: 00              BRK                         ; 
99AB: 10 08           BPL     $99B5               ; {}
99AD: FF                              ;
99AE: 08              PHP                         ; 
99AF: FC                              ;
99B0: FC                              ;
99B1: F0 FF           BEQ     $99B2               ; {}
99B3: 00              BRK                         ; 
99B4: 04                              ;
99B5: 04                              ;
99B6: 00              BRK                         ; 
99B7: FF                              ;
99B8: 10 B5           BPL     $996F               ; {}
99BA: AC D0 3D        LDY     $3DD0               ; 
99BD: B5 70           LDA     $70,X               ; {ram.0070}
99BF: 18              CLC                         ; 
99C0: 69 08           ADC     #$08                ; 
99C2: B4 98           LDY     $98,X               ; {ram.0098}
99C4: C0 04           CPY     #$04                ; 
99C6: B0 02           BCS     $99CA               ; {}
99C8: 69 08           ADC     #$08                ; 
99CA: 85 00           STA     <$00                ; {ram.GP_00}
99CC: B5 84           LDA     $84,X               ; {ram.0084}
99CE: 69 08           ADC     #$08                ; 
99D0: 85 01           STA     <$01                ; {ram.GP_01}
99D2: A0 10           LDY     #$10                ; 
99D4: B9 70 00        LDA     $0070,Y             ; {ram.0070}
99D7: 69 08           ADC     #$08                ; 
99D9: 85 02           STA     <$02                ; {ram.GP_02}
99DB: B9 84 00        LDA     $0084,Y             ; {ram.0084}
99DE: 69 08           ADC     #$08                ; 
99E0: 85 03           STA     <$03                ; {ram.GP_03}
99E2: B9 AC 00        LDA     $00AC,Y             ; {ram.00AC}
99E5: F0 13           BEQ     $99FA               ; {}
99E7: C9 12           CMP     #$12                ; 
99E9: F0 10           BEQ     $99FB               ; {}
99EB: C9 20           CMP     #$20                ; 
99ED: B0 0B           BCS     $99FA               ; {}
99EF: A0 00           LDY     #$00                ; 
99F1: 20 32 9A        JSR     $9A32               ; {}
99F4: D0 04           BNE     $99FA               ; {}
99F6: A9 02           LDA     #$02                ; 
99F8: 95 AC           STA     $AC,X               ; {ram.00AC}
99FA: 60              RTS                         ; 
99FB: A0 01           LDY     #$01                ; 
99FD: 20 32 9A        JSR     $9A32               ; {}
9A00: D0 2B           BNE     $9A2D               ; {}
9A02: A9 01           LDA     #$01                ; 
9A04: 85 00           STA     <$00                ; {ram.GP_00}
9A06: B5 98           LDA     $98,X               ; {ram.0098}
9A08: 4A              LSR     A                   ; 
9A09: A8              TAY                         ; 
9A0A: A5 04           LDA     <$04                ; {ram.0004}
9A0C: D9 A5 99        CMP     $99A5,Y             ; {}
9A0F: 30 1C           BMI     $9A2D               ; {}
9A11: D9 AA 99        CMP     $99AA,Y             ; {}
9A14: 10 17           BPL     $9A2D               ; {}
9A16: 98              TYA                         ; 
9A17: 18              CLC                         ; 
9A18: 69 0A           ADC     #$0A                ; 
9A1A: A8              TAY                         ; 
9A1B: A5 05           LDA     <$05                ; {ram.0005}
9A1D: C6 00           DEC     <$00                ; {ram.GP_00}
9A1F: 10 EB           BPL     $9A0C               ; {}
9A21: F6 AC           INC     $AC,X               ; {ram.00AC}
9A23: A0 10           LDY     #$10                ; 
9A25: A9 00           LDA     #$00                ; 
9A27: 99 AC 00        STA     $00AC,Y             ; {ram.00AC}
9A2A: 9D 2C 04        STA     $042C,X             ; {ram.!SplashMode}
9A2D: 60              RTS                         ; 
9A2E: 0C                              ;
9A2F: 11 F4           ORA     ($F4),Y             ; {ram.??!BatRamInit??}
9A31: F0 B9           BEQ     $99EC               ; {}
9A33: 2E 9A 85        ROL     $859A               ; {}
9A36: 06 B9           ASL     <$B9                ; {ram.00B9}
9A38: 30 9A           BMI     $99D4               ; {}
9A3A: 85 07           STA     <$07                ; {ram.0007}
9A3C: A9 03           LDA     #$03                ; 
9A3E: 85 08           STA     <$08                ; {ram.0008}
9A40: A0 01           LDY     #$01                ; 
9A42: B9 00 00        LDA     $0000,Y             ; {ram.GP_00}
9A45: 38              SEC                         ; 
9A46: F9 02 00        SBC     $0002,Y             ; {ram.GP_02}
9A49: C5 06           CMP     <$06                ; {ram.0006}
9A4B: 10 09           BPL     $9A56               ; {}
9A4D: C5 07           CMP     <$07                ; {ram.0007}
9A4F: 30 05           BMI     $9A56               ; {}
9A51: 99 04 00        STA     $0004,Y             ; {ram.0004}
9A54: 46 08           LSR     <$08                ; {ram.0008}
9A56: 88              DEY                         ; 
9A57: 10 E9           BPL     $9A42               ; {}
9A59: A5 08           LDA     <$08                ; {ram.0008}
9A5B: 60              RTS                         ; 
9A5C: 00              BRK                         ; 
9A5D: 01 06           ORA     ($06,X)             ; {ram.0006}
9A5F: FF                              ;
9A60: 08              PHP                         ; 
9A61: 02                              ;
9A62: 03                              ;
9A63: 06 FF           ASL     <$FF                ; {ram.CUR_2000}
9A65: 08              PHP                         ; 
9A66: 00              BRK                         ; 
9A67: 40              RTI                         ; 
9A68: 00              BRK                         ; 
9A69: FF                              ;
9A6A: 00              BRK                         ; 
9A6B: 00              BRK                         ; 
9A6C: 40              RTI                         ; 
9A6D: 40              RTI                         ; 
9A6E: FF                              ;
9A6F: 40              RTI                         ; 
9A70: 04                              ;
9A71: 05 07           ORA     <$07                ; {ram.0007}
9A73: FF                              ;
9A74: 09 04           ORA     #$04                ; 
9A76: 05 07           ORA     <$07                ; {ram.0007}
9A78: FF                              ;
9A79: 09 00           ORA     #$00                ; 
9A7B: 40              RTI                         ; 
9A7C: 00              BRK                         ; 
9A7D: FF                              ;
9A7E: 00              BRK                         ; 
9A7F: 00              BRK                         ; 
9A80: 40              RTI                         ; 
9A81: 00              BRK                         ; 
9A82: FF                              ;
9A83: 00              BRK                         ; 
9A84: 20 FB 9A        JSR     $9AFB               ; {}
9A87: B5 98           LDA     $98,X               ; {ram.0098}
9A89: 4A              LSR     A                   ; 
9A8A: 85 00           STA     <$00                ; {ram.GP_00}
9A8C: B4 AC           LDY     $AC,X               ; {ram.00AC}
9A8E: F0 26           BEQ     $9AB6               ; {}
9A90: A9 20           LDA     #$20                ; 
9A92: 88              DEY                         ; 
9A93: D0 23           BNE     $9AB8               ; {}
9A95: BC 2C 04        LDY     $042C,X             ; {ram.!SplashMode}
9A98: F0 1C           BEQ     $9AB6               ; {}
9A9A: C0 02           CPY     #$02                ; 
9A9C: F0 0D           BEQ     $9AAB               ; {}
9A9E: C0 03           CPY     #$03                ; 
9AA0: F0 09           BEQ     $9AAB               ; {}
9AA2: A5 00           LDA     <$00                ; {ram.GP_00}
9AA4: 18              CLC                         ; 
9AA5: 69 14           ADC     #$14                ; 
9AA7: A8              TAY                         ; 
9AA8: 4C C3 9A        JMP     $9AC3               ; {}
9AAB: A5 15           LDA     <$15                ; {ram.0015}
9AAD: 29 02           AND     #$02                ; 
9AAF: F0 4F           BEQ     $9B00               ; {}
9AB1: A4 00           LDY     <$00                ; {ram.GP_00}
9AB3: 4C C3 9A        JMP     $9AC3               ; {}
9AB6: A9 08           LDA     #$08                ; 
9AB8: A4 00           LDY     <$00                ; {ram.GP_00}
9ABA: 25 15           AND     <$15                ; {ram.0015}
9ABC: F0 05           BEQ     $9AC3               ; {}
9ABE: 98              TYA                         ; 
9ABF: 18              CLC                         ; 
9AC0: 69 05           ADC     #$05                ; 
9AC2: A8              TAY                         ; 
9AC3: 20 93 FA        JSR     $FA93               ; 
9AC6: 98              TYA                         ; 
9AC7: 48              PHA                         ; 
9AC8: B9 66 9A        LDA     $9A66,Y             ; {}
9ACB: 85 0F           STA     <$0F                ; {ram.000F}
9ACD: B9 5C 9A        LDA     $9A5C,Y             ; {}
9AD0: C9 07           CMP     #$07                ; 
9AD2: F0 04           BEQ     $9AD8               ; {}
9AD4: C9 09           CMP     #$09                ; 
9AD6: D0 06           BNE     $9ADE               ; {}
9AD8: 20 DB 77        JSR     $77DB               ; {ram.77DB}
9ADB: 4C E1 9A        JMP     $9AE1               ; {}
9ADE: 20 DF 77        JSR     $77DF               ; {ram.77DF}
9AE1: 68              PLA                         ; 
9AE2: A8              TAY                         ; 
9AE3: B5 98           LDA     $98,X               ; {ram.0098}
9AE5: 29 03           AND     #$03                ; 
9AE7: F0 17           BEQ     $9B00               ; {}
9AE9: B5 70           LDA     $70,X               ; {ram.0070}
9AEB: 18              CLC                         ; 
9AEC: 69 10           ADC     #$10                ; 
9AEE: 85 00           STA     <$00                ; {ram.GP_00}
9AF0: 20 FB 9A        JSR     $9AFB               ; {}
9AF3: B9 5C 9A        LDA     $9A5C,Y             ; {}
9AF6: 49 01           EOR     #$01                ; 
9AF8: 4C DF 77        JMP     $77DF               ; {ram.77DF}
9AFB: A9 03           LDA     #$03                ; 
9AFD: 20 88 79        JSR     $7988               ; {ram.7988}
9B00: 60              RTS                         ; 
9B01: FF                              ;
9B02: FF                              ;
9B03: FF                              ;
9B04: FF                              ;
9B05: FF                              ;
9B06: FF                              ;
9B07: FF                              ;
9B08: FF                              ;
9B09: FF                              ;
9B0A: FF                              ;
9B0B: FF                              ;
9B0C: FF                              ;
9B0D: FF                              ;
9B0E: FF                              ;
9B0F: FF                              ;
9B10: FF                              ;
9B11: FF                              ;
9B12: FF                              ;
9B13: FF                              ;
9B14: FF                              ;
9B15: FF                              ;
9B16: FF                              ;
9B17: FF                              ;
9B18: FF                              ;
9B19: FF                              ;
9B1A: FF                              ;
9B1B: FF                              ;
9B1C: FF                              ;
9B1D: FF                              ;
9B1E: FF                              ;
9B1F: FF                              ;
9B20: A9 F6           LDA     #$F6                ; 
9B22: 9D B2 04        STA     $04B2,X             ; 
9B25: A9 20           LDA     #$20                ; 
9B27: BC 4F 03        LDY     $034F,X             ; {ram.034F}
9B2A: C0 0B           CPY     #$0B                ; 
9B2C: F0 02           BEQ     $9B30               ; {}
9B2E: A9 28           LDA     #$28                ; 
9B30: 9D BC 03        STA     $03BC,X             ; {ram.03BC}
9B33: 4C 25 80        JMP     $8025               ; {}
9B36: A9 80           LDA     #$80                ; 
9B38: 20 6E 80        JSR     $806E               ; {}
9B3B: 20 D0 79        JSR     $79D0               ; {ram.79D0}
9B3E: A9 08           LDA     #$08                ; 
9B40: 20 89 FA        JSR     $FA89               ; 
9B43: 20 72 FA        JSR     $FA72               ; 
9B46: A9 00           LDA     #$00                ; 
9B48: 4C DF 77        JMP     $77DF               ; {ram.77DF}
9B4B: A9 80           LDA     #$80                ; 
9B4D: 20 6E 80        JSR     $806E               ; {}
9B50: 20 D0 79        JSR     $79D0               ; {ram.79D0}
9B53: A9 00           LDA     #$00                ; 
9B55: 95 3D           STA     $3D,X               ; {ram.003D}
9B57: A9 08           LDA     #$08                ; 
9B59: 20 89 FA        JSR     $FA89               ; 
9B5C: B5 98           LDA     $98,X               ; {ram.0098}
9B5E: C9 02           CMP     #$02                ; 
9B60: D0 02           BNE     $9B64               ; {}
9B62: E6 0F           INC     <$0F                ; {ram.000F}
9B64: 4A              LSR     A                   ; 
9B65: 4A              LSR     A                   ; 
9B66: BC E4 03        LDY     $03E4,X             ; {ram.03E4}
9B69: F0 0B           BEQ     $9B76               ; {}
9B6B: 18              CLC                         ; 
9B6C: 69 03           ADC     #$03                ; 
9B6E: B4 98           LDY     $98,X               ; {ram.0098}
9B70: C0 08           CPY     #$08                ; 
9B72: D0 02           BNE     $9B76               ; {}
9B74: E6 0F           INC     <$0F                ; {ram.000F}
9B76: 20 DF 77        JSR     $77DF               ; {ram.77DF}
9B79: 60              RTS                         ; 
9B7A: 01 FF           ORA     ($FF,X)             ; {ram.CUR_2000}
9B7C: 00              BRK                         ; 
9B7D: 00              BRK                         ; 
9B7E: 01 FF           ORA     ($FF,X)             ; {ram.CUR_2000}
9B80: 00              BRK                         ; 
9B81: 00              BRK                         ; 
9B82: 01 FF           ORA     ($FF,X)             ; {ram.CUR_2000}
9B84: 00              BRK                         ; 
9B85: 00              BRK                         ; 
9B86: 00              BRK                         ; 
9B87: 01 01           ORA     ($01,X)             ; {ram.GP_01}
9B89: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9B8B: FF                              ;
9B8C: FF                              ;
9B8D: FF                              ;
9B8E: FD FD FF        SBC     $FFFD,X             ; 
9B91: FF                              ;
9B92: FF                              ;
9B93: FF                              ;
9B94: FF                              ;
9B95: FC                              ;
9B96: 00              BRK                         ; 
9B97: 00              BRK                         ; 
9B98: 20 20 20        JSR     $2020               ; 
9B9B: 20 20 E0        JSR     $E020               ; 
9B9E: 01 02           ORA     ($02,X)             ; {ram.GP_02}
9BA0: 04                              ;
9BA1: 08              PHP                         ; 
9BA2: E0 01           CPX     #$01                ; 
9BA4: D0 00           BNE     $9BA6               ; {}
9BA6: AD 6C 06        LDA     $066C               ; {ram.066C}
9BA9: 15 3D           ORA     $3D,X               ; {ram.003D}
9BAB: D0 4D           BNE     $9BFA               ; {}
9BAD: A5 15           LDA     <$15                ; {ram.0015}
9BAF: 4A              LSR     A                   ; 
9BB0: B0 74           BCS     $9C26               ; {}
9BB2: 20 BD 9C        JSR     $9CBD               ; {}
9BB5: B5 AC           LDA     $AC,X               ; {ram.00AC}
9BB7: F0 06           BEQ     $9BBF               ; {}
9BB9: 20 3A 9C        JSR     $9C3A               ; {}
9BBC: 4C CF 9B        JMP     $9BCF               ; {}
9BBF: BD 94 03        LDA     $0394,X             ; {ram.0394}
9BC2: F0 39           BEQ     $9BFD               ; {}
9BC4: DE 94 03        DEC     $0394,X             ; {ram.0394}
9BC7: B5 84           LDA     $84,X               ; {ram.0084}
9BC9: 18              CLC                         ; 
9BCA: 79 84 9B        ADC     $9B84,Y             ; {}
9BCD: 95 84           STA     $84,X               ; {ram.0084}
9BCF: 20 8F 9C        JSR     $9C8F               ; {}
9BD2: 90 26           BCC     $9BFA               ; {}
9BD4: BD 1F 04        LDA     $041F,X             ; {ram.041F}
9BD7: 29 FC           AND     #$FC                ; 
9BD9: C9 B0           CMP     #$B0                ; 
9BDB: F0 20           BEQ     $9BFD               ; {}
9BDD: C9 F4           CMP     #$F4                ; 
9BDF: B0 1C           BCS     $9BFD               ; {}
9BE1: B5 98           LDA     $98,X               ; {ram.0098}
9BE3: 29 03           AND     #$03                ; 
9BE5: D0 09           BNE     $9BF0               ; {}
9BE7: B5 98           LDA     $98,X               ; {ram.0098}
9BE9: 49 0C           EOR     #$0C                ; 
9BEB: 95 98           STA     $98,X               ; {ram.0098}
9BED: 4C 26 9C        JMP     $9C26               ; {}
9BF0: 49 03           EOR     #$03                ; 
9BF2: 95 98           STA     $98,X               ; {ram.0098}
9BF4: 20 BD 9C        JSR     $9CBD               ; {}
9BF7: 20 BD 9C        JSR     $9CBD               ; {}
9BFA: 4C 26 9C        JMP     $9C26               ; {}
9BFD: B5 AC           LDA     $AC,X               ; {ram.00AC}
9BFF: D0 25           BNE     $9C26               ; {}
9C01: F6 AC           INC     $AC,X               ; {ram.00AC}
9C03: B4 98           LDY     $98,X               ; {ram.0098}
9C05: 88              DEY                         ; 
9C06: B5 84           LDA     $84,X               ; {ram.0084}
9C08: C9 78           CMP     #$78                ; 
9C0A: B0 02           BCS     $9C0E               ; {}
9C0C: A0 03           LDY     #$03                ; 
9C0E: C9 A8           CMP     #$A8                ; 
9C10: 90 02           BCC     $9C14               ; {}
9C12: A0 07           LDY     #$07                ; 
9C14: B9 8E 9B        LDA     $9B8E,Y             ; {}
9C17: 9D 12 04        STA     $0412,X             ; {ram.0412}
9C1A: B5 84           LDA     $84,X               ; {ram.0084}
9C1C: 18              CLC                         ; 
9C1D: 79 96 9B        ADC     $9B96,Y             ; {}
9C20: 9D 2C 04        STA     $042C,X             ; {ram.!SplashMode}
9C23: C8              INY                         ; 
9C24: 94 98           STY     $98,X               ; {ram.0098}
9C26: A9 08           LDA     #$08                ; 
9C28: 20 89 FA        JSR     $FA89               ; 
9C2B: BD E4 03        LDA     $03E4,X             ; {ram.03E4}
9C2E: 20 DB 77        JSR     $77DB               ; {ram.77DB}
9C31: A9 FE           LDA     #$FE                ; 
9C33: 9D B2 04        STA     $04B2,X             ; 
9C36: 20 D0 79        JSR     $79D0               ; {ram.79D0}
9C39: 60              RTS                         ; 
9C3A: BD 44 04        LDA     $0444,X             ; 
9C3D: 18              CLC                         ; 
9C3E: 69 38           ADC     #$38                ; 
9C40: 9D 44 04        STA     $0444,X             ; 
9C43: BD 12 04        LDA     $0412,X             ; {ram.0412}
9C46: 69 00           ADC     #$00                ; 
9C48: 9D 12 04        STA     $0412,X             ; {ram.0412}
9C4B: 18              CLC                         ; 
9C4C: 75 84           ADC     <$84,X              ; {ram.0084}
9C4E: 95 84           STA     $84,X               ; {ram.0084}
9C50: BD 12 04        LDA     $0412,X             ; {ram.0412}
9C53: 30 39           BMI     $9C8E               ; {}
9C55: B5 84           LDA     $84,X               ; {ram.0084}
9C57: DD 2C 04        CMP     $042C,X             ; {ram.!SplashMode}
9C5A: 90 32           BCC     $9C8E               ; {}
9C5C: A9 00           LDA     #$00                ; 
9C5E: 95 AC           STA     $AC,X               ; {ram.00AC}
9C60: 9D 44 04        STA     $0444,X             ; 
9C63: 9D 12 04        STA     $0412,X             ; {ram.0412}
9C66: B5 18           LDA     $18,X               ; {ram.0018}
9C68: 29 03           AND     #$03                ; 
9C6A: A8              TAY                         ; 
9C6B: B9 9E 9B        LDA     $9B9E,Y             ; {}
9C6E: 95 98           STA     $98,X               ; {ram.0098}
9C70: B5 18           LDA     $18,X               ; {ram.0018}
9C72: 29 40           AND     #$40                ; 
9C74: 69 30           ADC     #$30                ; 
9C76: 9D 94 03        STA     $0394,X             ; {ram.0394}
9C79: B5 70           LDA     $70,X               ; {ram.0070}
9C7B: 18              CLC                         ; 
9C7C: 69 08           ADC     #$08                ; 
9C7E: 29 F0           AND     #$F0                ; 
9C80: 95 70           STA     $70,X               ; {ram.0070}
9C82: B5 84           LDA     $84,X               ; {ram.0084}
9C84: 18              CLC                         ; 
9C85: 69 08           ADC     #$08                ; 
9C87: 29 F0           AND     #$F0                ; 
9C89: 38              SEC                         ; 
9C8A: E9 03           SBC     #$03                ; 
9C8C: 95 84           STA     $84,X               ; {ram.0084}
9C8E: 60              RTS                         ; 
9C8F: 20 AE 9C        JSR     $9CAE               ; {}
9C92: B0 19           BCS     $9CAD               ; {}
9C94: B5 70           LDA     $70,X               ; {ram.0070}
9C96: 48              PHA                         ; 
9C97: 18              CLC                         ; 
9C98: 69 0E           ADC     #$0E                ; 
9C9A: 95 70           STA     $70,X               ; {ram.0070}
9C9C: B5 84           LDA     $84,X               ; {ram.0084}
9C9E: 48              PHA                         ; 
9C9F: 18              CLC                         ; 
9CA0: 69 06           ADC     #$06                ; 
9CA2: 95 84           STA     $84,X               ; {ram.0084}
9CA4: 20 AE 9C        JSR     $9CAE               ; {}
9CA7: 68              PLA                         ; 
9CA8: 95 84           STA     $84,X               ; {ram.0084}
9CAA: 68              PLA                         ; 
9CAB: 95 70           STA     $70,X               ; {ram.0070}
9CAD: 60              RTS                         ; 
9CAE: A0 00           LDY     #$00                ; 
9CB0: 20 10 EE        JSR     $EE10               ; 
9CB3: BD 9E 04        LDA     $049E,X             ; {ram.049E}
9CB6: CD 4A 03        CMP     $034A               ; {ram.034A}
9CB9: 9D 1F 04        STA     $041F,X             ; {ram.041F}
9CBC: 60              RTS                         ; 
9CBD: B4 98           LDY     $98,X               ; {ram.0098}
9CBF: 88              DEY                         ; 
9CC0: B5 70           LDA     $70,X               ; {ram.0070}
9CC2: 18              CLC                         ; 
9CC3: 79 7A 9B        ADC     $9B7A,Y             ; {}
9CC6: 95 70           STA     $70,X               ; {ram.0070}
9CC8: 60              RTS                         ; 
9CC9: BD 2C 04        LDA     $042C,X             ; {ram.!SplashMode}
9CCC: D0 49           BNE     $9D17               ; {}
9CCE: A9 80           LDA     #$80                ; 
9CD0: 20 6E 80        JSR     $806E               ; {}
9CD3: DE D0 03        DEC     $03D0,X             ; {ram.03D0}
9CD6: D0 0F           BNE     $9CE7               ; {}
9CD8: A9 08           LDA     #$08                ; 
9CDA: 9D D0 03        STA     $03D0,X             ; {ram.03D0}
9CDD: BC E4 03        LDY     $03E4,X             ; {ram.03E4}
9CE0: C8              INY                         ; 
9CE1: 98              TYA                         ; 
9CE2: 29 03           AND     #$03                ; 
9CE4: 9D E4 03        STA     $03E4,X             ; {ram.03E4}
9CE7: 20 93 FA        JSR     $FA93               ; 
9CEA: BD E4 03        LDA     $03E4,X             ; {ram.03E4}
9CED: 20 DB 77        JSR     $77DB               ; {ram.77DB}
9CF0: 20 D0 79        JSR     $79D0               ; {ram.79D0}
9CF3: BD 2C 04        LDA     $042C,X             ; {ram.!SplashMode}
9CF6: F0 1E           BEQ     $9D16               ; {}
9CF8: A5 70           LDA     <$70                ; {ram.0070}
9CFA: 95 70           STA     $70,X               ; {ram.0070}
9CFC: A5 84           LDA     <$84                ; {ram.0084}
9CFE: 95 84           STA     $84,X               ; {ram.0084}
9D00: A9 00           LDA     #$00                ; 
9D02: 85 28           STA     <$28                ; {ram.0028}
9D04: 8D 05 04        STA     $0405               ; {ram.0405}
9D07: 85 C0           STA     <$C0                ; {ram.00C0}
9D09: 85 D3           STA     <$D3                ; {ram.00D3}
9D0B: 9D E4 03        STA     $03E4,X             ; {ram.03E4}
9D0E: A9 04           LDA     #$04                ; 
9D10: 9D D0 03        STA     $03D0,X             ; {ram.03D0}
9D13: EE 12 05        INC     $0512               ; {ram.0512}
9D16: 60              RTS                         ; 
9D17: A9 02           LDA     #$02                ; 
9D19: DD E4 03        CMP     $03E4,X             ; {ram.03E4}
9D1C: 90 0C           BCC     $9D2A               ; {}
9D1E: DE D0 03        DEC     $03D0,X             ; {ram.03D0}
9D21: D0 07           BNE     $9D2A               ; {}
9D23: 0A              ASL     A                   ; 
9D24: 9D D0 03        STA     $03D0,X             ; {ram.03D0}
9D27: FE E4 03        INC     $03E4,X             ; {ram.03E4}
9D2A: FE 2C 04        INC     $042C,X             ; {ram.!SplashMode}
9D2D: BD 2C 04        LDA     $042C,X             ; {ram.!SplashMode}
9D30: C9 60           CMP     #$60                ; 
9D32: 90 0A           BCC     $9D3E               ; {}
9D34: A9 00           LDA     #$00                ; 
9D36: 8D 76 06        STA     $0676               ; {ram.0676}
9D39: A9 C0           LDA     #$C0                ; 
9D3B: 9D 2C 04        STA     $042C,X             ; {ram.!SplashMode}
9D3E: 20 93 FA        JSR     $FA93               ; 
9D41: BD E4 03        LDA     $03E4,X             ; {ram.03E4}
9D44: 20 97 82        JSR     $8297               ; {}
9D47: 20 D0 79        JSR     $79D0               ; {ram.79D0}
9D4A: BD 05 04        LDA     $0405,X             ; {ram.0405}
9D4D: F0 C7           BEQ     $9D16               ; {}
9D4F: A9 00           LDA     #$00                ; 
9D51: 8D 12 05        STA     $0512               ; {ram.0512}
9D54: 4C 8A 82        JMP     $828A               ; {}
9D57: 20 82 9D        JSR     $9D82               ; {}
9D5A: B5 AC           LDA     $AC,X               ; {ram.00AC}
9D5C: C9 02           CMP     #$02                ; 
9D5E: B0 06           BCS     $9D66               ; {}
9D60: 20 BD 9D        JSR     $9DBD               ; {}
9D63: 4C D1 9D        JMP     $9DD1               ; {}
9D66: EE 4E 03        INC     $034E               ; {ram.034E}
9D69: 20 B1 FE        JSR     $FEB1               ; 
9D6C: A0 01           LDY     #$01                ; 
9D6E: 98              TYA                         ; 
9D6F: 48              PHA                         ; 
9D70: 20 BB FE        JSR     $FEBB               ; 
9D73: F0 07           BEQ     $9D7C               ; {}
9D75: A9 1C           LDA     #$1C                ; 
9D77: 85 00           STA     <$00                ; {ram.GP_00}
9D79: 20 95 B1        JSR     $B195               ; {}
9D7C: 68              PLA                         ; 
9D7D: A8              TAY                         ; 
9D7E: 88              DEY                         ; 
9D7F: 10 ED           BPL     $9D6E               ; {}
9D81: 60              RTS                         ; 
9D82: B5 AC           LDA     $AC,X               ; {ram.00AC}
9D84: 20 E2 E5        JSR     $E5E2               ; 
9D87: 9B                              ;
9D88: 9D F1 84        STA     $84F1,X             ; {}
9D8B: 00              BRK                         ; 
9D8C: FD FE FF        SBC     $FFFE,X             ; 
9D8F: FF                              ;
9D90: 00              BRK                         ; 
9D91: FF                              ;
9D92: 00              BRK                         ; 
9D93: 00              BRK                         ; 
9D94: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9D96: 01 01           ORA     ($01,X)             ; {ram.GP_01}
9D98: 02                              ;
9D99: 03                              ;
9D9A: 00              BRK                         ; 
9D9B: A9 80           LDA     #$80                ; 
9D9D: 20 6E 80        JSR     $806E               ; {}
9DA0: AD 6C 06        LDA     $066C               ; {ram.066C}
9DA3: 15 3D           ORA     $3D,X               ; {ram.003D}
9DA5: D0 15           BNE     $9DBC               ; {}
9DA7: B5 98           LDA     $98,X               ; {ram.0098}
9DA9: 29 03           AND     #$03                ; 
9DAB: F0 0F           BEQ     $9DBC               ; {}
9DAD: BD 94 03        LDA     $0394,X             ; {ram.0394}
9DB0: 20 1F 70        JSR     $701F               ; {ram.701F}
9DB3: A8              TAY                         ; 
9DB4: B5 84           LDA     $84,X               ; {ram.0084}
9DB6: 18              CLC                         ; 
9DB7: 79 8B 9D        ADC     $9D8B,Y             ; {}
9DBA: 95 84           STA     $84,X               ; {ram.0084}
9DBC: 60              RTS                         ; 
9DBD: B5 AC           LDA     $AC,X               ; {ram.00AC}
9DBF: D0 0F           BNE     $9DD0               ; {}
9DC1: 20 D0 79        JSR     $79D0               ; {ram.79D0}
9DC4: BD 05 04        LDA     $0405,X             ; {ram.0405}
9DC7: D0 07           BNE     $9DD0               ; {}
9DC9: BD F0 04        LDA     $04F0,X             ; {ram.04F0}
9DCC: F0 02           BEQ     $9DD0               ; {}
9DCE: F6 AC           INC     $AC,X               ; {ram.00AC}
9DD0: 60              RTS                         ; 
9DD1: A9 0A           LDA     #$0A                ; 
9DD3: 20 89 FA        JSR     $FA89               ; 
9DD6: B5 98           LDA     $98,X               ; {ram.0098}
9DD8: 29 08           AND     #$08                ; 
9DDA: 4A              LSR     A                   ; 
9DDB: 4A              LSR     A                   ; 
9DDC: 18              CLC                         ; 
9DDD: 7D E4 03        ADC     $03E4,X             ; {ram.03E4}
9DE0: 4C DB 77        JMP     $77DB               ; {ram.77DB}
9DE3: AD 6C 06        LDA     $066C               ; {ram.066C}
9DE6: D0 0C           BNE     $9DF4               ; {}
9DE8: 20 F7 9D        JSR     $9DF7               ; {}
9DEB: 20 58 9F        JSR     $9F58               ; {}
9DEE: BD 94 03        LDA     $0394,X             ; {ram.0394}
9DF1: 4A              LSR     A                   ; 
9DF2: B0 23           BCS     $9E17               ; {}
9DF4: 4C 40 A0        JMP     $A040               ; {}
9DF7: B5 28           LDA     $28,X               ; {ram.0028}
9DF9: D0 11           BNE     $9E0C               ; {}
9DFB: BD 94 03        LDA     $0394,X             ; {ram.0394}
9DFE: F0 06           BEQ     $9E06               ; {}
9E00: DE 94 03        DEC     $0394,X             ; {ram.0394}
9E03: 4C 20 9E        JMP     $9E20               ; {}
9E06: 20 FC 9E        JSR     $9EFC               ; {}
9E09: 4C 62 9E        JMP     $9E62               ; {}
9E0C: C9 10           CMP     #$10                ; 
9E0E: B0 08           BCS     $9E18               ; {}
9E10: C9 01           CMP     #$01                ; 
9E12: D0 03           BNE     $9E17               ; {}
9E14: 20 BC 9E        JSR     $9EBC               ; {}
9E17: 60              RTS                         ; 
9E18: A5 15           LDA     <$15                ; {ram.0015}
9E1A: 4A              LSR     A                   ; 
9E1B: B0 3E           BCS     $9E5B               ; {}
9E1D: 20 58 9E        JSR     $9E58               ; {}
9E20: 20 9D 9E        JSR     $9E9D               ; {}
9E23: 20 2C 9F        JSR     $9F2C               ; {}
9E26: 90 2F           BCC     $9E57               ; {}
9E28: BD 1F 04        LDA     $041F,X             ; {ram.041F}
9E2B: 29 FC           AND     #$FC                ; 
9E2D: C9 B0           CMP     #$B0                ; 
9E2F: F0 04           BEQ     $9E35               ; {}
9E31: C9 F4           CMP     #$F4                ; 
9E33: 90 08           BCC     $9E3D               ; {}
9E35: BD 94 03        LDA     $0394,X             ; {ram.0394}
9E38: D0 DD           BNE     $9E17               ; {}
9E3A: 4C EB 9E        JMP     $9EEB               ; {}
9E3D: B4 98           LDY     $98,X               ; {ram.0098}
9E3F: 98              TYA                         ; 
9E40: 29 0C           AND     #$0C                ; 
9E42: F0 06           BEQ     $9E4A               ; {}
9E44: 98              TYA                         ; 
9E45: 49 0C           EOR     #$0C                ; 
9E47: 95 98           STA     $98,X               ; {ram.0098}
9E49: A8              TAY                         ; 
9E4A: 98              TYA                         ; 
9E4B: 29 03           AND     #$03                ; 
9E4D: F0 05           BEQ     $9E54               ; {}
9E4F: 98              TYA                         ; 
9E50: 49 03           EOR     #$03                ; 
9E52: 95 98           STA     $98,X               ; {ram.0098}
9E54: 4C 9D 9E        JMP     $9E9D               ; {}
9E57: 60              RTS                         ; 
9E58: FE 12 04        INC     $0412,X             ; {ram.0412}
9E5B: BD 12 04        LDA     $0412,X             ; {ram.0412}
9E5E: 29 3F           AND     #$3F                ; 
9E60: D0 4D           BNE     $9EAF               ; {}
9E62: BD 12 04        LDA     $0412,X             ; {ram.0412}
9E65: 29 40           AND     #$40                ; 
9E67: D0 0C           BNE     $9E75               ; {}
9E69: A9 02           LDA     #$02                ; 
9E6B: B4 70           LDY     $70,X               ; {ram.0070}
9E6D: C4 70           CPY     <$70                ; {ram.0070}
9E6F: B0 01           BCS     $9E72               ; {}
9E71: 4A              LSR     A                   ; 
9E72: 4C 7E 9E        JMP     $9E7E               ; {}
9E75: A9 08           LDA     #$08                ; 
9E77: B4 84           LDY     $84,X               ; {ram.0084}
9E79: C4 84           CPY     <$84                ; {ram.0084}
9E7B: B0 01           BCS     $9E7E               ; {}
9E7D: 4A              LSR     A                   ; 
9E7E: D5 98           CMP     $98,X               ; {ram.0098}
9E80: F0 2D           BEQ     $9EAF               ; {}
9E82: 95 98           STA     $98,X               ; {ram.0098}
9E84: 4C 02 9F        JMP     $9F02               ; {}
9E87: 00              BRK                         ; 
9E88: 01 FF           ORA     ($FF,X)             ; {ram.CUR_2000}
9E8A: 00              BRK                         ; 
9E8B: 00              BRK                         ; 
9E8C: 01 FF           ORA     ($FF,X)             ; {ram.CUR_2000}
9E8E: 00              BRK                         ; 
9E8F: 00              BRK                         ; 
9E90: 01 FF           ORA     ($FF,X)             ; {ram.CUR_2000}
9E92: 00              BRK                         ; 
9E93: 00              BRK                         ; 
9E94: 00              BRK                         ; 
9E95: 00              BRK                         ; 
9E96: 01 01           ORA     ($01,X)             ; {ram.GP_01}
9E98: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9E9A: FF                              ;
9E9B: FF                              ;
9E9C: FF                              ;
9E9D: B4 98           LDY     $98,X               ; {ram.0098}
9E9F: B5 70           LDA     $70,X               ; {ram.0070}
9EA1: 18              CLC                         ; 
9EA2: 79 87 9E        ADC     $9E87,Y             ; {}
9EA5: 95 70           STA     $70,X               ; {ram.0070}
9EA7: B5 84           LDA     $84,X               ; {ram.0084}
9EA9: 18              CLC                         ; 
9EAA: 79 92 9E        ADC     $9E92,Y             ; {}
9EAD: 95 84           STA     $84,X               ; {ram.0084}
9EAF: 60              RTS                         ; 
9EB0: E0 20           CPX     #$20                ; 
9EB2: E0 20           CPX     #$20                ; 
9EB4: E0 E0           CPX     #$E0                ; 
9EB6: 20 20 0A        JSR     $0A20               ; 
9EB9: 09 06           ORA     #$06                ; 
9EBB: 05 B5           ORA     <$B5                ; {ram.00B5}
9EBD: 18              CLC                         ; 
9EBE: 29 03           AND     #$03                ; 
9EC0: A8              TAY                         ; 
9EC1: B5 70           LDA     $70,X               ; {ram.0070}
9EC3: 48              PHA                         ; 
9EC4: 18              CLC                         ; 
9EC5: 79 B0 9E        ADC     $9EB0,Y             ; {}
9EC8: 95 70           STA     $70,X               ; {ram.0070}
9ECA: B5 84           LDA     $84,X               ; {ram.0084}
9ECC: 48              PHA                         ; 
9ECD: 18              CLC                         ; 
9ECE: 79 B4 9E        ADC     $9EB4,Y             ; {}
9ED1: 95 84           STA     $84,X               ; {ram.0084}
9ED3: 98              TYA                         ; 
9ED4: 48              PHA                         ; 
9ED5: B9 B8 9E        LDA     $9EB8,Y             ; {}
9ED8: A8              TAY                         ; 
9ED9: 20 2E 9F        JSR     $9F2E               ; {}
9EDC: 68              PLA                         ; 
9EDD: A8              TAY                         ; 
9EDE: 68              PLA                         ; 
9EDF: 95 84           STA     $84,X               ; {ram.0084}
9EE1: 68              PLA                         ; 
9EE2: 95 70           STA     $70,X               ; {ram.0070}
9EE4: B0 16           BCS     $9EFC               ; {}
9EE6: B9 B8 9E        LDA     $9EB8,Y             ; {}
9EE9: 95 98           STA     $98,X               ; {ram.0098}
9EEB: A9 20           LDA     #$20                ; 
9EED: 9D 94 03        STA     $0394,X             ; {ram.0394}
9EF0: BD 12 04        LDA     $0412,X             ; {ram.0412}
9EF3: 49 40           EOR     #$40                ; 
9EF5: 9D 12 04        STA     $0412,X             ; {ram.0412}
9EF8: A9 00           LDA     #$00                ; 
9EFA: F0 04           BEQ     $9F00               ; {}
9EFC: B5 18           LDA     $18,X               ; {ram.0018}
9EFE: 09 70           ORA     #$70                ; 
9F00: 95 28           STA     $28,X               ; {ram.0028}
9F02: B5 70           LDA     $70,X               ; {ram.0070}
9F04: 18              CLC                         ; 
9F05: 69 08           ADC     #$08                ; 
9F07: 29 F0           AND     #$F0                ; 
9F09: 95 70           STA     $70,X               ; {ram.0070}
9F0B: B5 84           LDA     $84,X               ; {ram.0084}
9F0D: 18              CLC                         ; 
9F0E: 69 08           ADC     #$08                ; 
9F10: 29 F0           AND     #$F0                ; 
9F12: 38              SEC                         ; 
9F13: E9 03           SBC     #$03                ; 
9F15: 95 84           STA     $84,X               ; {ram.0084}
9F17: 60              RTS                         ; 
9F18: 0F                              ;
9F19: 00              BRK                         ; 
9F1A: 00              BRK                         ; 
9F1B: 04                              ;
9F1C: 08              PHP                         ; 
9F1D: 00              BRK                         ; 
9F1E: 00              BRK                         ; 
9F1F: 04                              ;
9F20: 08              PHP                         ; 
9F21: 00              BRK                         ; 
9F22: 04                              ;
9F23: 04                              ;
9F24: 00              BRK                         ; 
9F25: 08              PHP                         ; 
9F26: 08              PHP                         ; 
9F27: 08              PHP                         ; 
9F28: 00              BRK                         ; 
9F29: F8              SED                         ; 
9F2A: 00              BRK                         ; 
9F2B: 00              BRK                         ; 
9F2C: B4 98           LDY     $98,X               ; {ram.0098}
9F2E: 88              DEY                         ; 
9F2F: B5 70           LDA     $70,X               ; {ram.0070}
9F31: 48              PHA                         ; 
9F32: 18              CLC                         ; 
9F33: 79 18 9F        ADC     $9F18,Y             ; {}
9F36: 95 70           STA     $70,X               ; {ram.0070}
9F38: B5 84           LDA     $84,X               ; {ram.0084}
9F3A: 48              PHA                         ; 
9F3B: 18              CLC                         ; 
9F3C: 79 22 9F        ADC     $9F22,Y             ; {}
9F3F: 95 84           STA     $84,X               ; {ram.0084}
9F41: 20 4B 9F        JSR     $9F4B               ; {}
9F44: 68              PLA                         ; 
9F45: 95 84           STA     $84,X               ; {ram.0084}
9F47: 68              PLA                         ; 
9F48: 95 70           STA     $70,X               ; {ram.0070}
9F4A: 60              RTS                         ; 
9F4B: 20 F4 ED        JSR     $EDF4               ; 
9F4E: BD 9E 04        LDA     $049E,X             ; {ram.049E}
9F51: CD 4A 03        CMP     $034A               ; {ram.034A}
9F54: 9D 1F 04        STA     $041F,X             ; {ram.041F}
9F57: 60              RTS                         ; 
9F58: BD 94 03        LDA     $0394,X             ; {ram.0394}
9F5B: D0 21           BNE     $9F7E               ; {}
9F5D: A5 15           LDA     <$15                ; {ram.0015}
9F5F: 29 1F           AND     #$1F                ; 
9F61: D0 1B           BNE     $9F7E               ; {}
9F63: B5 84           LDA     $84,X               ; {ram.0084}
9F65: 29 F0           AND     #$F0                ; 
9F67: 85 00           STA     <$00                ; {ram.GP_00}
9F69: A5 84           LDA     <$84                ; {ram.0084}
9F6B: 29 F0           AND     #$F0                ; 
9F6D: C5 00           CMP     <$00                ; {ram.GP_00}
9F6F: D0 0E           BNE     $9F7F               ; {}
9F71: A9 02           LDA     #$02                ; 
9F73: B4 70           LDY     $70,X               ; {ram.0070}
9F75: C4 70           CPY     <$70                ; {ram.0070}
9F77: B0 01           BCS     $9F7A               ; {}
9F79: 4A              LSR     A                   ; 
9F7A: D5 98           CMP     $98,X               ; {ram.0098}
9F7C: F0 1A           BEQ     $9F98               ; {}
9F7E: 60              RTS                         ; 
9F7F: B5 70           LDA     $70,X               ; {ram.0070}
9F81: 29 F0           AND     #$F0                ; 
9F83: 85 00           STA     <$00                ; {ram.GP_00}
9F85: A5 70           LDA     <$70                ; {ram.0070}
9F87: C5 00           CMP     <$00                ; {ram.GP_00}
9F89: D0 F3           BNE     $9F7E               ; {}
9F8B: A9 08           LDA     #$08                ; 
9F8D: B4 84           LDY     $84,X               ; {ram.0084}
9F8F: C4 84           CPY     <$84                ; {ram.0084}
9F91: B0 01           BCS     $9F94               ; {}
9F93: 4A              LSR     A                   ; 
9F94: D5 98           CMP     $98,X               ; {ram.0098}
9F96: D0 E6           BNE     $9F7E               ; {}
9F98: A9 58           LDA     #$58                ; 
9F9A: 85 00           STA     <$00                ; {ram.GP_00}
9F9C: AD 6C 06        LDA     $066C               ; {ram.066C}
9F9F: D0 DD           BNE     $9F7E               ; {}
9FA1: A9 04           LDA     #$04                ; 
9FA3: 8D 04 06        STA     $0604               ; {ram.SND_Request}
9FA6: 4C 80 B1        JMP     $B180               ; {}
9FA9: AD 6C 06        LDA     $066C               ; {ram.066C}
9FAC: F0 03           BEQ     $9FB1               ; {}
9FAE: 4C 40 A0        JMP     $A040               ; {}
9FB1: FE 12 04        INC     $0412,X             ; {ram.0412}
9FB4: D6 AC           DEC     $AC,X               ; {ram.00AC}
9FB6: B5 AC           LDA     $AC,X               ; {ram.00AC}
9FB8: 4A              LSR     A                   ; 
9FB9: 4A              LSR     A                   ; 
9FBA: 4A              LSR     A                   ; 
9FBB: 4A              LSR     A                   ; 
9FBC: 4A              LSR     A                   ; 
9FBD: 4A              LSR     A                   ; 
9FBE: 20 E2 E5        JSR     $E5E2               ; 
9FC1: 34                              ;
9FC2: A0 ED           LDY     #$ED                ; 
9FC4: 9F                              ;
9FC5: 35 A0           AND     $A0,X               ; {ram.00A0}
9FC7: FD 9F 00        SBC     $009F,X             ; 
9FCA: 00              BRK                         ; 
9FCB: E0 20           CPX     #$20                ; 
9FCD: 00              BRK                         ; 
9FCE: 00              BRK                         ; 
9FCF: C0 40           CPY     #$40                ; 
9FD1: 00              BRK                         ; 
9FD2: 00              BRK                         ; 
9FD3: D0 30           BNE     $A005               ; {}
9FD5: 00              BRK                         ; 
9FD6: 00              BRK                         ; 
9FD7: B0 50           BCS     $A029               ; {}
9FD9: E0 20           CPX     #$20                ; 
9FDB: 00              BRK                         ; 
9FDC: 00              BRK                         ; 
9FDD: C0 40           CPY     #$40                ; 
9FDF: 00              BRK                         ; 
9FE0: 00              BRK                         ; 
9FE1: D0 30           BNE     $A013               ; {}
9FE3: 00              BRK                         ; 
9FE4: 00              BRK                         ; 
9FE5: B0 50           BCS     $A037               ; {}
9FE7: 00              BRK                         ; 
9FE8: 00              BRK                         ; 
9FE9: 04                              ;
9FEA: 08              PHP                         ; 
9FEB: 01 02           ORA     ($02,X)             ; {ram.GP_02}
9FED: B5 AC           LDA     $AC,X               ; {ram.00AC}
9FEF: C9 7F           CMP     #$7F                ; 
9FF1: D0 04           BNE     $9FF7               ; {}
9FF3: A9 4F           LDA     #$4F                ; 
9FF5: 95 AC           STA     $AC,X               ; {ram.00AC}
9FF7: FE 94 03        INC     $0394,X             ; {ram.0394}
9FFA: 4C EE 9D        JMP     $9DEE               ; {}
9FFD: B4 AC           LDY     $AC,X               ; {ram.00AC}
9FFF: C8              INY                         ; 
A000: D0 EB           BNE     $9FED               ; {}
A002: B5 18           LDA     $18,X               ; {ram.0018}
A004: 48              PHA                         ; 
A005: 29 03           AND     #$03                ; 
A007: A8              TAY                         ; 
A008: B9 E9 9F        LDA     $9FE9,Y             ; {}
A00B: 95 98           STA     $98,X               ; {ram.0098}
A00D: 68              PLA                         ; 
A00E: 29 0F           AND     #$0F                ; 
A010: A8              TAY                         ; 
A011: A5 70           LDA     <$70                ; {ram.0070}
A013: 79 C9 9F        ADC     $9FC9,Y             ; {}
A016: 29 F0           AND     #$F0                ; 
A018: 95 70           STA     $70,X               ; {ram.0070}
A01A: A5 84           LDA     <$84                ; {ram.0084}
A01C: 18              CLC                         ; 
A01D: 69 03           ADC     #$03                ; 
A01F: 79 D9 9F        ADC     $9FD9,Y             ; {}
A022: 20 10 9F        JSR     $9F10               ; {}
A025: C9 5D           CMP     #$5D                ; 
A027: 90 09           BCC     $A032               ; {}
A029: C9 C4           CMP     #$C4                ; 
A02B: B0 05           BCS     $A032               ; {}
A02D: 20 2C 9F        JSR     $9F2C               ; {}
A030: 90 02           BCC     $A034               ; {}
A032: F6 AC           INC     $AC,X               ; {ram.00AC}
A034: 60              RTS                         ; 
A035: B5 AC           LDA     $AC,X               ; {ram.00AC}
A037: C9 B0           CMP     #$B0                ; 
A039: D0 05           BNE     $A040               ; {}
A03B: A9 59           LDA     #$59                ; 
A03D: 20 9A 9F        JSR     $9F9A               ; {}
A040: A9 F6           LDA     #$F6                ; 
A042: 9D B2 04        STA     $04B2,X             ; 
A045: 20 2D 7A        JSR     $7A2D               ; {ram.7A2D}
A048: BD F0 04        LDA     $04F0,X             ; {ram.04F0}
A04B: D0 14           BNE     $A061               ; {}
A04D: A0 0E           LDY     #$0E                ; 
A04F: 20 9D 7C        JSR     $7C9D               ; {ram.7C9D}
A052: A0 10           LDY     #$10                ; 
A054: 20 DC 7C        JSR     $7CDC               ; {ram.7CDC}
A057: A0 11           LDY     #$11                ; 
A059: 20 DC 7C        JSR     $7CDC               ; {ram.7CDC}
A05C: A0 0D           LDY     #$0D                ; 
A05E: 20 29 7D        JSR     $7D29               ; {ram.7D29}
A061: 20 A7 7A        JSR     $7AA7               ; {ram.7AA7}
A064: BD 12 04        LDA     $0412,X             ; {ram.0412}
A067: 4A              LSR     A                   ; 
A068: 4A              LSR     A                   ; 
A069: 29 01           AND     #$01                ; 
A06B: 48              PHA                         ; 
A06C: 20 93 FA        JSR     $FA93               ; 
A06F: B5 98           LDA     $98,X               ; {ram.0098}
A071: 29 08           AND     #$08                ; 
A073: D0 0B           BNE     $A080               ; {}
A075: B5 98           LDA     $98,X               ; {ram.0098}
A077: 4A              LSR     A                   ; 
A078: 29 01           AND     #$01                ; 
A07A: 85 0F           STA     <$0F                ; {ram.000F}
A07C: 68              PLA                         ; 
A07D: 4C DF 77        JMP     $77DF               ; {ram.77DF}
A080: 68              PLA                         ; 
A081: 18              CLC                         ; 
A082: 69 02           ADC     #$02                ; 
A084: 4C DB 77        JMP     $77DB               ; {ram.77DB}
A087: 6F                              ;
A088: 74                              ;
A089: 79 7E 83        ADC     $837E,Y             ; {}
A08C: 88              DEY                         ; 
A08D: A9 10           LDA     #$10                ; 
A08F: 8D 01 06        STA     $0601               ; {ram.??SND_601??}
A092: A2 05           LDX     #$05                ; 
A094: A9 7C           LDA     #$7C                ; 
A096: 9D 38 04        STA     $0438,X             ; {ram.0438}
A099: 9D 52 04        STA     $0452,X             ; 
A09C: 9D 6C 04        STA     $046C,X             ; {ram.046C}
A09F: 9D 95 03        STA     $0395,X             ; 
A0A2: 95 71           STA     $71,X               ; {ram.0071}
A0A4: BD 87 A0        LDA     $A087,X             ; {}
A0A7: 9D 45 04        STA     $0445,X             ; {ram.0445}
A0AA: 9D 5F 04        STA     $045F,X             ; {ram.045F}
A0AD: 9D 79 04        STA     $0479,X             ; {ram.0479}
A0B0: 9D BD 03        STA     $03BD,X             ; 
A0B3: 95 85           STA     $85,X               ; {ram.0085}
A0B5: A9 A0           LDA     #$A0                ; 
A0B7: 9D 86 04        STA     $0486,X             ; {ram.0486}
A0BA: A9 00           LDA     #$00                ; 
A0BC: 9D 06 04        STA     $0406,X             ; {ram.0406}
A0BF: 9D 94 04        STA     $0494,X             ; 
A0C2: A9 FE           LDA     #$FE                ; 
A0C4: 9D B3 04        STA     $04B3,X             ; 
A0C7: CA              DEX                         ; 
A0C8: 10 CA           BPL     $A094               ; {}
A0CA: 8E 22 04        STX     $0422               ; {ram.0422}
A0CD: 8E 30 04        STX     $0430               ; {ram.0430}
A0D0: 8E 83 03        STX     $0383               ; {ram.0383}
A0D3: 8E AC 03        STX     $03AC               ; {ram.03AC}
A0D6: A9 03           LDA     #$03                ; 
A0D8: 8D 21 04        STA     $0421               ; {ram.0421}
A0DB: 8D 2E 04        STA     $042E               ; {ram.042E}
A0DE: 8D 82 03        STA     $0382               ; {ram.0382}
A0E1: 8D AA 03        STA     $03AA               ; {ram.03AA}
A0E4: 0A              ASL     A                   ; 
A0E5: 8D 20 04        STA     $0420               ; {ram.0420}
A0E8: 8D 2D 04        STA     $042D               ; {ram.!SplashSeq}
A0EB: 8D 81 03        STA     $0381               ; {ram.0381}
A0EE: 8D A9 03        STA     $03A9               ; {ram.03A9}
A0F1: 0A              ASL     A                   ; 
A0F2: 8D 32 04        STA     $0432               ; {ram.0432}
A0F5: 0A              ASL     A                   ; 
A0F6: 8D 86 03        STA     $0386               ; {ram.0386}
A0F9: 6D 32 04        ADC     $0432               ; {ram.0432}
A0FC: 8D AE 03        STA     $03AE               ; {ram.03AE}
A0FF: 60              RTS                         ; 
A100: 00              BRK                         ; 
A101: 80                              ;
A102: 02                              ;
A103: 42                              ;
A104: 04                              ;
A105: 00              BRK                         ; 
A106: 00              BRK                         ; 
A107: F0 10           BEQ     $A119               ; {}
A109: 00              BRK                         ; 
A10A: 00              BRK                         ; 
A10B: 00              BRK                         ; 
A10C: A9 40           LDA     #$40                ; 
A10E: 8D 01 06        STA     $0601               ; {ram.??SND_601??}
A111: B5 18           LDA     $18,X               ; {ram.0018}
A113: 29 07           AND     #$07                ; 
A115: A8              TAY                         ; 
A116: B9 4E B2        LDA     $B24E,Y             ; {}
A119: 95 98           STA     $98,X               ; {ram.0098}
A11B: A0 04           LDY     #$04                ; 
A11D: A5 99           LDA     <$99                ; {ram.0099}
A11F: 99 99 00        STA     $0099,Y             ; {ram.0099}
A122: A9 3C           LDA     #$3C                ; 
A124: 99 50 03        STA     $0350,Y             ; {ram.0350}
A127: A9 E2           LDA     #$E2                ; 
A129: 99 B3 04        STA     $04B3,Y             ; 
A12C: B9 00 A1        LDA     $A100,Y             ; {}
A12F: 99 79 04        STA     $0479,Y             ; {ram.0479}
A132: A9 00           LDA     #$00                ; 
A134: 99 06 04        STA     $0406,Y             ; {ram.0406}
A137: 99 93 04        STA     $0493,Y             ; 
A13A: AD C0 04        LDA     $04C0               ; {ram.04C0}
A13D: 99 C0 04        STA     $04C0,Y             ; {ram.04C0}
A140: AD 86 04        LDA     $0486               ; {ram.0486}
A143: 99 86 04        STA     $0486,Y             ; {ram.0486}
A146: A5 75           LDA     <$75                ; {ram.0075}
A148: 18              CLC                         ; 
A149: 79 05 A1        ADC     $A105,Y             ; {}
A14C: 99 71 00        STA     $0071,Y             ; {ram.0071}
A14F: A5 89           LDA     <$89                ; {ram.0089}
A151: 18              CLC                         ; 
A152: 79 07 A1        ADC     $A107,Y             ; {}
A155: 99 85 00        STA     $0085,Y             ; {ram.0085}
A158: A9 80           LDA     #$80                ; 
A15A: 99 20 04        STA     $0420,Y             ; {ram.0420}
A15D: 88              DEY                         ; 
A15E: 10 BD           BPL     $A11D               ; {}
A160: 60              RTS                         ; 
A161: A9 20           LDA     #$20                ; 
A163: 8D 01 06        STA     $0601               ; {ram.??SND_601??}
A166: A9 FB           LDA     #$FB                ; 
A168: 9D B2 04        STA     $04B2,X             ; 
A16B: FE 80 03        INC     $0380,X             ; 
A16E: A9 80           LDA     #$80                ; 
A170: 95 70           STA     $70,X               ; {ram.0070}
A172: A9 70           LDA     #$70                ; 
A174: 95 84           STA     $84,X               ; {ram.0084}
A176: 4C D6 FE        JMP     $FED6               ; 
A179: 20 1D 84        JSR     $841D               ; {}
A17C: A9 E0           LDA     #$E0                ; 
A17E: 8D D1 04        STA     $04D1               ; {ram.04D1}
A181: A9 BF           LDA     #$BF                ; 
A183: 9D 1F 04        STA     $041F,X             ; {ram.041F}
A186: 60              RTS                         ; 
A187: E0 05           CPX     #$05                ; 
A189: D0 41           BNE     $A1CC               ; {}
A18B: AD 83 03        LDA     $0383               ; {ram.0383}
A18E: F0 1B           BEQ     $A1AB               ; {}
A190: A0 04           LDY     #$04                ; 
A192: B9 20 04        LDA     $0420,Y             ; {ram.0420}
A195: 18              CLC                         ; 
A196: 69 80           ADC     #$80                ; 
A198: 99 20 04        STA     $0420,Y             ; {ram.0420}
A19B: B9 2D 04        LDA     $042D,Y             ; {ram.!SplashSeq}
A19E: 69 00           ADC     #$00                ; 
A1A0: 99 2D 04        STA     $042D,Y             ; {ram.!SplashSeq}
A1A3: 88              DEY                         ; 
A1A4: 10 EC           BPL     $A192               ; {}
A1A6: A9 00           LDA     #$00                ; 
A1A8: 8D 83 03        STA     $0383               ; {ram.0383}
A1AB: AD 85 03        LDA     $0385               ; {ram.0385}
A1AE: F0 03           BEQ     $A1B3               ; {}
A1B0: 20 85 A2        JSR     $A285               ; {}
A1B3: B5 28           LDA     $28,X               ; {ram.0028}
A1B5: D0 15           BNE     $A1CC               ; {}
A1B7: A9 10           LDA     #$10                ; 
A1B9: 95 28           STA     $28,X               ; {ram.0028}
A1BB: B5 18           LDA     $18,X               ; {ram.0018}
A1BD: C9 80           CMP     #$80                ; 
A1BF: B0 5E           BCS     $A21F               ; {}
A1C1: 20 88 B3        JSR     $B388               ; {}
A1C4: A5 9D           LDA     <$9D                ; {ram.009D}
A1C6: 8D 85 03        STA     $0385               ; {ram.0385}
A1C9: 20 85 A2        JSR     $A285               ; {}
A1CC: E0 05           CPX     #$05                ; 
A1CE: D0 05           BNE     $A1D5               ; {}
A1D0: B5 98           LDA     $98,X               ; {ram.0098}
A1D2: 8D 84 03        STA     $0384               ; {ram.0384}
A1D5: 20 8E A2        JSR     $A28E               ; {}
A1D8: 20 25 A2        JSR     $A225               ; {}
A1DB: B5 98           LDA     $98,X               ; {ram.0098}
A1DD: CD 84 03        CMP     $0384               ; {ram.0384}
A1E0: F0 03           BEQ     $A1E5               ; {}
A1E2: 8D 85 03        STA     $0385               ; {ram.0385}
A1E5: BD 51 04        LDA     $0451,X             ; 
A1E8: 29 10           AND     #$10                ; 
A1EA: 4A              LSR     A                   ; 
A1EB: 4A              LSR     A                   ; 
A1EC: 4A              LSR     A                   ; 
A1ED: 4A              LSR     A                   ; 
A1EE: 85 00           STA     <$00                ; {ram.GP_00}
A1F0: BD 78 04        LDA     $0478,X             ; 
A1F3: 29 FE           AND     #$FE                ; 
A1F5: 05 00           ORA     <$00                ; {ram.GP_00}
A1F7: 9D 78 04        STA     $0478,X             ; 
A1FA: E0 05           CPX     #$05                ; 
A1FC: F0 1E           BEQ     $A21C               ; {}
A1FE: BD 78 04        LDA     $0478,X             ; 
A201: DD 37 04        CMP     $0437,X             ; {ram.0437}
A204: F0 16           BEQ     $A21C               ; {}
A206: 9D 37 04        STA     $0437,X             ; {ram.0437}
A209: 4A              LSR     A                   ; 
A20A: B0 10           BCS     $A21C               ; {}
A20C: B5 19           LDA     $19,X               ; {ram.0019}
A20E: C9 E0           CMP     #$E0                ; 
A210: 90 0A           BCC     $A21C               ; {}
A212: AD 56 03        LDA     $0356               ; {ram.0356}
A215: D0 05           BNE     $A21C               ; {}
A217: A9 56           LDA     #$56                ; 
A219: 20 AF 82        JSR     $82AF               ; {}
A21C: 4C EF A2        JMP     $A2EF               ; {}
A21F: 20 1A B3        JSR     $B31A               ; {}
A222: 4C C4 A1        JMP     $A1C4               ; {}
A225: B5 98           LDA     $98,X               ; {ram.0098}
A227: 48              PHA                         ; 
A228: B5 28           LDA     $28,X               ; {ram.0028}
A22A: 48              PHA                         ; 
A22B: 20 D0 79        JSR     $79D0               ; {ram.79D0}
A22E: 68              PLA                         ; 
A22F: 95 28           STA     $28,X               ; {ram.0028}
A231: 68              PLA                         ; 
A232: 95 98           STA     $98,X               ; {ram.0098}
A234: E0 05           CPX     #$05                ; 
A236: D0 05           BNE     $A23D               ; {}
A238: A9 00           LDA     #$00                ; 
A23A: 9D F0 04        STA     $04F0,X             ; {ram.04F0}
A23D: 20 00 80        JSR     $8000               ; {}
A240: BD 05 04        LDA     $0405,X             ; {ram.0405}
A243: F0 37           BEQ     $A27C               ; {}
A245: 20 E4 EE        JSR     $EEE4               ; 
A248: E0 05           CPX     #$05                ; 
A24A: D0 06           BNE     $A252               ; {}
A24C: 9D 05 04        STA     $0405,X             ; {ram.0405}
A24F: 4C 7C A2        JMP     $A27C               ; {}
A252: A0 03           LDY     #$03                ; 
A254: A9 00           LDA     #$00                ; 
A256: 85 00           STA     <$00                ; {ram.GP_00}
A258: B9 50 03        LDA     $0350,Y             ; {ram.0350}
A25B: C9 3C           CMP     #$3C                ; 
A25D: D0 02           BNE     $A261               ; {}
A25F: E6 00           INC     <$00                ; {ram.GP_00}
A261: 88              DEY                         ; 
A262: 10 F4           BPL     $A258               ; {}
A264: C6 00           DEC     <$00                ; {ram.GP_00}
A266: 30 02           BMI     $A26A               ; {}
A268: D0 13           BNE     $A27D               ; {}
A26A: 20 10 B0        JSR     $B010               ; {}
A26D: A9 5D           LDA     #$5D                ; 
A26F: 8D 54 03        STA     $0354               ; {ram.0354}
A272: A9 10           LDA     #$10                ; 
A274: 8D 0A 04        STA     $040A               ; {ram.040A}
A277: 85 2D           STA     <$2D                ; {ram.002D}
A279: EE 83 03        INC     $0383               ; {ram.0383}
A27C: 60              RTS                         ; 
A27D: A9 5D           LDA     #$5D                ; 
A27F: 9D 4F 03        STA     $034F,X             ; {ram.034F}
A282: 4C 79 A2        JMP     $A279               ; {}
A285: A0 04           LDY     #$04                ; 
A287: 99 99 00        STA     $0099,Y             ; {ram.0099}
A28A: 88              DEY                         ; 
A28B: 10 FA           BPL     $A287               ; {}
A28D: 60              RTS                         ; 
A28E: BD 1F 04        LDA     $041F,X             ; {ram.041F}
A291: 29 E0           AND     #$E0                ; 
A293: 18              CLC                         ; 
A294: 7D 12 04        ADC     $0412,X             ; {ram.0412}
A297: 9D 12 04        STA     $0412,X             ; {ram.0412}
A29A: BD 2C 04        LDA     $042C,X             ; {ram.!SplashMode}
A29D: 69 00           ADC     #$00                ; 
A29F: 85 03           STA     <$03                ; {ram.GP_03}
A2A1: A9 A1           LDA     #$A1                ; 
A2A3: 85 02           STA     <$02                ; {ram.GP_02}
A2A5: B5 98           LDA     $98,X               ; {ram.0098}
A2A7: 24 02           BIT     <$02                ; {ram.GP_02}
A2A9: F0 07           BEQ     $A2B2               ; {}
A2AB: B5 70           LDA     $70,X               ; {ram.0070}
A2AD: 18              CLC                         ; 
A2AE: 65 03           ADC     <$03                ; {ram.GP_03}
A2B0: 95 70           STA     $70,X               ; {ram.0070}
A2B2: B5 98           LDA     $98,X               ; {ram.0098}
A2B4: 06 02           ASL     <$02                ; {ram.GP_02}
A2B6: 24 02           BIT     <$02                ; {ram.GP_02}
A2B8: F0 06           BEQ     $A2C0               ; {}
A2BA: B5 70           LDA     $70,X               ; {ram.0070}
A2BC: E5 03           SBC     <$03                ; {ram.GP_03}
A2BE: 95 70           STA     $70,X               ; {ram.0070}
A2C0: B5 98           LDA     $98,X               ; {ram.0098}
A2C2: 06 02           ASL     <$02                ; {ram.GP_02}
A2C4: 24 02           BIT     <$02                ; {ram.GP_02}
A2C6: F0 06           BEQ     $A2CE               ; {}
A2C8: B5 84           LDA     $84,X               ; {ram.0084}
A2CA: 65 03           ADC     <$03                ; {ram.GP_03}
A2CC: 95 84           STA     $84,X               ; {ram.0084}
A2CE: B5 98           LDA     $98,X               ; {ram.0098}
A2D0: 06 02           ASL     <$02                ; {ram.GP_02}
A2D2: 24 02           BIT     <$02                ; {ram.GP_02}
A2D4: F0 06           BEQ     $A2DC               ; {}
A2D6: B5 84           LDA     $84,X               ; {ram.0084}
A2D8: E5 03           SBC     <$03                ; {ram.GP_03}
A2DA: 95 84           STA     $84,X               ; {ram.0084}
A2DC: B5 19           LDA     $19,X               ; {ram.0019}
A2DE: 29 03           AND     #$03                ; 
A2E0: 18              CLC                         ; 
A2E1: 65 03           ADC     <$03                ; {ram.GP_03}
A2E3: 7D 51 04        ADC     $0451,X             ; 
A2E6: 9D 51 04        STA     $0451,X             ; 
A2E9: 20 CD B2        JSR     $B2CD               ; {}
A2EC: 4C 93 FA        JMP     $FA93               ; 
A2EF: 20 93 FA        JSR     $FA93               ; 
A2F2: BD 78 04        LDA     $0478,X             ; 
A2F5: 48              PHA                         ; 
A2F6: 29 80           AND     #$80                ; 
A2F8: 09 01           ORA     #$01                ; 
A2FA: 20 88 79        JSR     $7988               ; {ram.7988}
A2FD: 68              PLA                         ; 
A2FE: 48              PHA                         ; 
A2FF: 29 40           AND     #$40                ; 
A301: F0 02           BEQ     $A305               ; {}
A303: E6 0F           INC     <$0F                ; {ram.000F}
A305: 68              PLA                         ; 
A306: 29 0F           AND     #$0F                ; 
A308: C9 02           CMP     #$02                ; 
A30A: F0 07           BEQ     $A313               ; {}
A30C: C9 03           CMP     #$03                ; 
A30E: F0 03           BEQ     $A313               ; {}
A310: 4C DB 77        JMP     $77DB               ; {ram.77DB}
A313: 4C DF 77        JMP     $77DF               ; {ram.77DF}
A316: BD 51 04        LDA     $0451,X             ; 
A319: D0 16           BNE     $A331               ; {}
A31B: A9 01           LDA     #$01                ; 
A31D: B4 18           LDY     $18,X               ; {ram.0018}
A31F: C0 B0           CPY     #$B0                ; 
A321: B0 06           BCS     $A329               ; {}
A323: 0A              ASL     A                   ; 
A324: C0 60           CPY     #$60                ; 
A326: B0 01           BCS     $A329               ; {}
A328: 0A              ASL     A                   ; 
A329: 95 98           STA     $98,X               ; {ram.0098}
A32B: FE 51 04        INC     $0451,X             ; 
A32E: 4C 80 A3        JMP     $A380               ; {}
A331: BD 1F 04        LDA     $041F,X             ; {ram.041F}
A334: 18              CLC                         ; 
A335: 69 80           ADC     #$80                ; 
A337: 9D 1F 04        STA     $041F,X             ; {ram.041F}
A33A: 90 44           BCC     $A380               ; {}
A33C: FE 12 04        INC     $0412,X             ; {ram.0412}
A33F: A9 01           LDA     #$01                ; 
A341: 85 02           STA     <$02                ; {ram.GP_02}
A343: B5 98           LDA     $98,X               ; {ram.0098}
A345: 24 02           BIT     <$02                ; {ram.GP_02}
A347: F0 02           BEQ     $A34B               ; {}
A349: F6 70           INC     $70,X               ; {ram.0070}
A34B: 06 02           ASL     <$02                ; {ram.GP_02}
A34D: 24 02           BIT     <$02                ; {ram.GP_02}
A34F: F0 02           BEQ     $A353               ; {}
A351: D6 70           DEC     $70,X               ; {ram.0070}
A353: 06 02           ASL     <$02                ; {ram.GP_02}
A355: 24 02           BIT     <$02                ; {ram.GP_02}
A357: F0 02           BEQ     $A35B               ; {}
A359: F6 84           INC     $84,X               ; {ram.0084}
A35B: 06 02           ASL     <$02                ; {ram.GP_02}
A35D: 24 02           BIT     <$02                ; {ram.GP_02}
A35F: F0 02           BEQ     $A363               ; {}
A361: D6 84           DEC     $84,X               ; {ram.0084}
A363: BD 12 04        LDA     $0412,X             ; {ram.0412}
A366: C9 20           CMP     #$20                ; 
A368: D0 16           BNE     $A380               ; {}
A36A: A9 00           LDA     #$00                ; 
A36C: 9D 12 04        STA     $0412,X             ; {ram.0412}
A36F: 20 E2 B2        JSR     $B2E2               ; {}
A372: BD 5E 04        LDA     $045E,X             ; 
A375: FE 5E 04        INC     $045E,X             ; 
A378: 4A              LSR     A                   ; 
A379: 90 05           BCC     $A380               ; {}
A37B: A9 00           LDA     #$00                ; 
A37D: 9D 51 04        STA     $0451,X             ; 
A380: BD 2C 04        LDA     $042C,X             ; {ram.!SplashMode}
A383: D0 0C           BNE     $A391               ; {}
A385: A9 80           LDA     #$80                ; 
A387: 9D 44 04        STA     $0444,X             ; 
A38A: A9 C0           LDA     #$C0                ; 
A38C: 15 18           ORA     $18,X               ; {ram.0018}
A38E: 9D 2C 04        STA     $042C,X             ; {ram.!SplashMode}
A391: A5 15           LDA     <$15                ; {ram.0015}
A393: 4A              LSR     A                   ; 
A394: 90 03           BCC     $A399               ; {}
A396: DE 2C 04        DEC     $042C,X             ; {ram.!SplashMode}
A399: BD 44 04        LDA     $0444,X             ; 
A39C: F0 2A           BEQ     $A3C8               ; {}
A39E: DE 44 04        DEC     $0444,X             ; 
A3A1: A0 02           LDY     #$02                ; 
A3A3: C9 70           CMP     #$70                ; 
A3A5: B0 05           BCS     $A3AC               ; {}
A3A7: C9 10           CMP     #$10                ; 
A3A9: 90 01           BCC     $A3AC               ; {}
A3AB: C8              INY                         ; 
A3AC: 98              TYA                         ; 
A3AD: 9D 6B 04        STA     $046B,X             ; 
A3B0: DE 80 03        DEC     $0380,X             ; 
A3B3: D0 0A           BNE     $A3BF               ; {}
A3B5: A9 41           LDA     #$41                ; 
A3B7: 9D 80 03        STA     $0380,X             ; 
A3BA: A9 56           LDA     #$56                ; 
A3BC: 20 AF 82        JSR     $82AF               ; {}
A3BF: BD 6B 04        LDA     $046B,X             ; 
A3C2: 20 E3 A3        JSR     $A3E3               ; {}
A3C5: 4C 22 A4        JMP     $A422               ; {}
A3C8: FE 78 04        INC     $0478,X             ; 
A3CB: BD 78 04        LDA     $0478,X             ; 
A3CE: C9 08           CMP     #$08                ; 
A3D0: D0 DE           BNE     $A3B0               ; {}
A3D2: A9 00           LDA     #$00                ; 
A3D4: 9D 78 04        STA     $0478,X             ; 
A3D7: BD 6B 04        LDA     $046B,X             ; 
A3DA: 29 01           AND     #$01                ; 
A3DC: 49 01           EOR     #$01                ; 
A3DE: 4C AD A3        JMP     $A3AD               ; {}
A3E1: F0 10           BEQ     $A3F3               ; {}
A3E3: 48              PHA                         ; 
A3E4: 20 93 FA        JSR     $FA93               ; 
A3E7: 20 19 A4        JSR     $A419               ; {}
A3EA: 68              PLA                         ; 
A3EB: 20 DB 77        JSR     $77DB               ; {ram.77DB}
A3EE: A9 10           LDA     #$10                ; 
A3F0: 20 89 FA        JSR     $FA89               ; 
A3F3: A0 01           LDY     #$01                ; 
A3F5: 20 FA A3        JSR     $A3FA               ; {}
A3F8: A0 00           LDY     #$00                ; 
A3FA: B5 70           LDA     $70,X               ; {ram.0070}
A3FC: 18              CLC                         ; 
A3FD: 79 E1 A3        ADC     $A3E1,Y             ; {}
A400: 85 00           STA     <$00                ; {ram.GP_00}
A402: B5 84           LDA     $84,X               ; {ram.0084}
A404: 85 01           STA     <$01                ; {ram.GP_01}
A406: 20 19 A4        JSR     $A419               ; {}
A409: 20 72 FA        JSR     $FA72               ; 
A40C: 98              TYA                         ; 
A40D: 18              CLC                         ; 
A40E: 7D E4 03        ADC     $03E4,X             ; {ram.03E4}
A411: 29 01           AND     #$01                ; 
A413: 18              CLC                         ; 
A414: 69 04           ADC     #$04                ; 
A416: 4C DF 77        JMP     $77DF               ; {ram.77DF}
A419: BD 4F 03        LDA     $034F,X             ; {ram.034F}
A41C: 38              SEC                         ; 
A41D: E9 32           SBC     #$32                ; 
A41F: 4C 88 79        JMP     $7988               ; {ram.7988}
A422: B5 70           LDA     $70,X               ; {ram.0070}
A424: 48              PHA                         ; 
A425: 38              SEC                         ; 
A426: E9 10           SBC     #$10                ; 
A428: 95 70           STA     $70,X               ; {ram.0070}
A42A: A9 05           LDA     #$05                ; 
A42C: 85 0F           STA     <$0F                ; {ram.000F}
A42E: 20 D0 79        JSR     $79D0               ; {ram.79D0}
A431: B5 70           LDA     $70,X               ; {ram.0070}
A433: 18              CLC                         ; 
A434: 69 08           ADC     #$08                ; 
A436: 95 70           STA     $70,X               ; {ram.0070}
A438: C6 0F           DEC     <$0F                ; {ram.000F}
A43A: D0 F2           BNE     $A42E               ; {}
A43C: 68              PLA                         ; 
A43D: 95 70           STA     $70,X               ; {ram.0070}
A43F: 60              RTS                         ; 
A440: C0 12           CPY     #$12                ; 
A442: D0 0A           BNE     $A44E               ; {}
A444: A9 28           LDA     #$28                ; 
A446: 99 AC 00        STA     $00AC,Y             ; {ram.00AC}
A449: A9 04           LDA     #$04                ; 
A44B: 99 D0 03        STA     $03D0,Y             ; {ram.03D0}
A44E: A5 0F           LDA     <$0F                ; {ram.000F}
A450: C9 03           CMP     #$03                ; 
A452: F0 04           BEQ     $A458               ; {}
A454: C9 04           CMP     #$04                ; 
A456: D0 19           BNE     $A471               ; {}
A458: BD 6B 04        LDA     $046B,X             ; 
A45B: C9 03           CMP     #$03                ; 
A45D: D0 12           BNE     $A471               ; {}
A45F: B9 98 00        LDA     $0098,Y             ; {ram.0098}
A462: C9 08           CMP     #$08                ; 
A464: D0 0B           BNE     $A471               ; {}
A466: A9 02           LDA     #$02                ; 
A468: 8D 01 06        STA     $0601               ; {ram.??SND_601??}
A46B: 20 54 7C        JSR     $7C54               ; {ram.7C54}
A46E: 20 0D 80        JSR     $800D               ; {}
A471: A9 01           LDA     #$01                ; 
A473: 8D 04 06        STA     $0604               ; {ram.SND_Request}
A476: 60              RTS                         ; 
A477: 20 AC A4        JSR     $A4AC               ; {}
A47A: 20 88 B2        JSR     $B288               ; {}
A47D: BD 37 04        LDA     $0437,X             ; {ram.0437}
A480: 29 01           AND     #$01                ; 
A482: D0 10           BNE     $A494               ; {}
A484: B5 19           LDA     $19,X               ; {ram.0019}
A486: C9 20           CMP     #$20                ; 
A488: B0 0A           BCS     $A494               ; {}
A48A: AD 5A 03        LDA     $035A               ; {ram.035A}
A48D: D0 05           BNE     $A494               ; {}
A48F: A9 56           LDA     #$56                ; 
A491: 20 AF 82        JSR     $82AF               ; {}
A494: A9 01           LDA     #$01                ; 
A496: 20 89 FA        JSR     $FA89               ; 
A499: BD E4 03        LDA     $03E4,X             ; {ram.03E4}
A49C: 20 DB 77        JSR     $77DB               ; {ram.77DB}
A49F: 20 D0 79        JSR     $79D0               ; {ram.79D0}
A4A2: 20 DA FE        JSR     $FEDA               ; 
A4A5: 20 E6 EE        JSR     $EEE6               ; 
A4A8: 9D F0 04        STA     $04F0,X             ; {ram.04F0}
A4AB: 60              RTS                         ; 
A4AC: BD 44 04        LDA     $0444,X             ; 
A4AF: 20 E2 E5        JSR     $E5E2               ; 
A4B2: 66 B2           ROR     <$B2                ; {ram.00B2}
A4B4: BA              TSX                         ; 
A4B5: A4 08           LDY     <$08                ; {ram.0008}
A4B7: B3                              ;
A4B8: 78              SEI                         ; 
A4B9: B3                              ;
A4BA: A0 02           LDY     #$02                ; 
A4BC: B5 19           LDA     $19,X               ; {ram.0019}
A4BE: C9 D0           CMP     #$D0                ; 
A4C0: 90 01           BCC     $A4C3               ; {}
A4C2: C8              INY                         ; 
A4C3: 4C C1 84        JMP     $84C1               ; {}
A4C6: 38              SEC                         ; 
A4C7: 52                              ;
A4C8: 6C 95 04        JMP     ($0495)             ; {ram.0495}
A4CB: 04                              ;
A4CC: 04                              ;
A4CD: 03                              ;
A4CE: 45 5F           EOR     <$5F                ; {ram.005F}
A4D0: 79 BD 04        ADC     $04BD,Y             ; 
A4D3: 04                              ;
A4D4: 04                              ;
A4D5: 03                              ;
A4D6: 20 2D 81        JSR     $812D               ; {}
A4D9: A9 04           LDA     #$04                ; 
A4DB: 04                              ;
A4DC: 03                              ;
A4DD: 03                              ;
A4DE: 20 25 A8        JSR     $A825               ; {}
A4E1: AD 50 03        LDA     $0350               ; {ram.0350}
A4E4: 38              SEC                         ; 
A4E5: E9 42           SBC     #$42                ; 
A4E7: 8D D7 04        STA     $04D7               ; {ram.04D7}
A4EA: AC D7 04        LDY     $04D7               ; {ram.04D7}
A4ED: B9 BE E6        LDA     $E6BE,Y             ; 
A4F0: 2C 11 05        BIT     $0511               ; {ram.0511}
A4F3: F0 03           BEQ     $A4F8               ; {}
A4F5: 4C 47 A5        JMP     $A547               ; {}
A4F8: 20 4D A5        JSR     $A54D               ; {}
A4FB: B1 00           LDA     ($00),Y             ; {ram.GP_00}
A4FD: 99 71 00        STA     $0071,Y             ; {ram.0071}
A500: B1 02           LDA     ($02),Y             ; {ram.GP_02}
A502: 99 85 00        STA     $0085,Y             ; {ram.0085}
A505: B1 04           LDA     ($04),Y             ; {ram.0004}
A507: 99 13 04        STA     $0413,Y             ; {ram.0413}
A50A: 88              DEY                         ; 
A50B: 10 EE           BPL     $A4FB               ; {}
A50D: A5 15           LDA     <$15                ; {ram.0015}
A50F: 29 03           AND     #$03                ; 
A511: 85 00           STA     <$00                ; {ram.GP_00}
A513: E4 00           CPX     <$00                ; {ram.GP_00}
A515: D0 18           BNE     $A52F               ; {}
A517: 20 76 A5        JSR     $A576               ; {}
A51A: 20 A4 A7        JSR     $A7A4               ; {}
A51D: A2 05           LDX     #$05                ; 
A51F: B5 18           LDA     $18,X               ; {ram.0018}
A521: C9 20           CMP     #$20                ; 
A523: B0 0A           BCS     $A52F               ; {}
A525: AD 5A 03        LDA     $035A               ; {ram.035A}
A528: D0 05           BNE     $A52F               ; {}
A52A: A9 56           LDA     #$56                ; 
A52C: 20 AF 82        JSR     $82AF               ; {}
A52F: 20 E5 A6        JSR     $A6E5               ; {}
A532: 20 4D A5        JSR     $A54D               ; {}
A535: B9 71 00        LDA     $0071,Y             ; {ram.0071}
A538: 91 00           STA     ($00),Y             ; {ram.GP_00}
A53A: B9 85 00        LDA     $0085,Y             ; {ram.0085}
A53D: 91 02           STA     ($02),Y             ; {ram.GP_02}
A53F: B9 13 04        LDA     $0413,Y             ; {ram.0413}
A542: 91 04           STA     ($04),Y             ; {ram.0004}
A544: 88              DEY                         ; 
A545: 10 EE           BPL     $A535               ; {}
A547: CE D7 04        DEC     $04D7               ; {ram.04D7}
A54A: 10 9E           BPL     $A4EA               ; {}
A54C: 60              RTS                         ; 
A54D: AE D7 04        LDX     $04D7               ; {ram.04D7}
A550: BD C6 A4        LDA     $A4C6,X             ; {}
A553: 85 00           STA     <$00                ; {ram.GP_00}
A555: BD CA A4        LDA     $A4CA,X             ; {}
A558: 85 01           STA     <$01                ; {ram.GP_01}
A55A: BD CE A4        LDA     $A4CE,X             ; {}
A55D: 85 02           STA     <$02                ; {ram.GP_02}
A55F: BD D2 A4        LDA     $A4D2,X             ; {}
A562: 85 03           STA     <$03                ; {ram.GP_03}
A564: BD D6 A4        LDA     $A4D6,X             ; {}
A567: 85 04           STA     <$04                ; {ram.0004}
A569: BD DA A4        LDA     $A4DA,X             ; {}
A56C: 85 05           STA     <$05                ; {ram.0005}
A56E: A0 05           LDY     #$05                ; 
A570: 60              RTS                         ; 
A571: 4A              LSR     A                   ; 
A572: 4A              LSR     A                   ; 
A573: 4C 85 A5        JMP     $A585               ; {}
A576: A5 75           LDA     <$75                ; {ram.0075}
A578: 38              SEC                         ; 
A579: E5 71           SBC     <$71                ; {ram.0071}
A57B: 10 F4           BPL     $A571               ; {}
A57D: 20 21 70        JSR     $7021               ; {ram.7021}
A580: 4A              LSR     A                   ; 
A581: 4A              LSR     A                   ; 
A582: 20 21 70        JSR     $7021               ; {ram.7021}
A585: 8D D8 04        STA     $04D8               ; {ram.04D8}
A588: 20 1F 70        JSR     $701F               ; {ram.701F}
A58B: A2 00           LDX     #$00                ; 
A58D: 20 21 A6        JSR     $A621               ; {}
A590: A5 89           LDA     <$89                ; {ram.0089}
A592: 38              SEC                         ; 
A593: E5 85           SBC     <$85                ; {ram.0085}
A595: 20 1F 70        JSR     $701F               ; {ram.701F}
A598: 4A              LSR     A                   ; 
A599: 4A              LSR     A                   ; 
A59A: E8              INX                         ; 
A59B: 20 21 A6        JSR     $A621               ; {}
A59E: A2 00           LDX     #$00                ; 
A5A0: B5 71           LDA     $71,X               ; {ram.0071}
A5A2: 38              SEC                         ; 
A5A3: F5 72           SBC     $72,X               ; {ram.0072}
A5A5: 20 1F 70        JSR     $701F               ; {ram.701F}
A5A8: CD DD 04        CMP     $04DD               ; {ram.04DD}
A5AB: 90 0F           BCC     $A5BC               ; {}
A5AD: B5 72           LDA     $72,X               ; {ram.0072}
A5AF: A8              TAY                         ; 
A5B0: C8              INY                         ; 
A5B1: C8              INY                         ; 
A5B2: D5 71           CMP     $71,X               ; {ram.0071}
A5B4: 90 04           BCC     $A5BA               ; {}
A5B6: 88              DEY                         ; 
A5B7: 88              DEY                         ; 
A5B8: 88              DEY                         ; 
A5B9: 88              DEY                         ; 
A5BA: 94 72           STY     $72,X               ; {ram.0072}
A5BC: B5 85           LDA     $85,X               ; {ram.0085}
A5BE: 38              SEC                         ; 
A5BF: F5 86           SBC     $86,X               ; {ram.0086}
A5C1: 20 1F 70        JSR     $701F               ; {ram.701F}
A5C4: CD DE 04        CMP     $04DE               ; {ram.04DE}
A5C7: 90 0F           BCC     $A5D8               ; {}
A5C9: B5 86           LDA     $86,X               ; {ram.0086}
A5CB: A8              TAY                         ; 
A5CC: C8              INY                         ; 
A5CD: C8              INY                         ; 
A5CE: D5 85           CMP     $85,X               ; {ram.0085}
A5D0: 90 04           BCC     $A5D6               ; {}
A5D2: 88              DEY                         ; 
A5D3: 88              DEY                         ; 
A5D4: 88              DEY                         ; 
A5D5: 88              DEY                         ; 
A5D6: 94 86           STY     $86,X               ; {ram.0086}
A5D8: E8              INX                         ; 
A5D9: E0 04           CPX     #$04                ; 
A5DB: D0 C3           BNE     $A5A0               ; {}
A5DD: A2 00           LDX     #$00                ; 
A5DF: 20 43 A6        JSR     $A643               ; {}
A5E2: E8              INX                         ; 
A5E3: E0 03           CPX     #$03                ; 
A5E5: 90 F8           BCC     $A5DF               ; {}
A5E7: A2 02           LDX     #$02                ; 
A5E9: 8A              TXA                         ; 
A5EA: A8              TAY                         ; 
A5EB: A5 71           LDA     <$71                ; {ram.0071}
A5ED: 18              CLC                         ; 
A5EE: 6D D8 04        ADC     $04D8               ; {ram.04D8}
A5F1: 88              DEY                         ; 
A5F2: 10 F9           BPL     $A5ED               ; {}
A5F4: B4 72           LDY     $72,X               ; {ram.0072}
A5F6: C8              INY                         ; 
A5F7: D5 72           CMP     $72,X               ; {ram.0072}
A5F9: B0 02           BCS     $A5FD               ; {}
A5FB: 88              DEY                         ; 
A5FC: 88              DEY                         ; 
A5FD: 94 72           STY     $72,X               ; {ram.0072}
A5FF: CA              DEX                         ; 
A600: 10 E7           BPL     $A5E9               ; {}
A602: A2 01           LDX     #$01                ; 
A604: B5 87           LDA     $87,X               ; {ram.0087}
A606: D5 86           CMP     $86,X               ; {ram.0086}
A608: B0 09           BCS     $A613               ; {}
A60A: D5 88           CMP     $88,X               ; 
A60C: B0 0F           BCS     $A61D               ; {}
A60E: F6 87           INC     $87,X               ; {ram.0087}
A610: 4C 1D A6        JMP     $A61D               ; {}
A613: D5 86           CMP     $86,X               ; {ram.0086}
A615: 90 06           BCC     $A61D               ; {}
A617: D5 88           CMP     $88,X               ; 
A619: 90 02           BCC     $A61D               ; {}
A61B: D6 87           DEC     $87,X               ; {ram.0087}
A61D: CA              DEX                         ; 
A61E: 10 E4           BPL     $A604               ; {}
A620: 60              RTS                         ; 
A621: C9 04           CMP     #$04                ; 
A623: 90 02           BCC     $A627               ; {}
A625: A9 04           LDA     #$04                ; 
A627: 9D D9 04        STA     $04D9,X             ; {ram.04D9}
A62A: 18              CLC                         ; 
A62B: 69 04           ADC     #$04                ; 
A62D: C9 08           CMP     #$08                ; 
A62F: 90 02           BCC     $A633               ; {}
A631: A9 08           LDA     #$08                ; 
A633: 9D DB 04        STA     $04DB,X             ; {ram.04DB}
A636: 18              CLC                         ; 
A637: 69 04           ADC     #$04                ; 
A639: C9 0B           CMP     #$0B                ; 
A63B: 90 02           BCC     $A63F               ; {}
A63D: A9 0B           LDA     #$0B                ; 
A63F: 9D DD 04        STA     $04DD,X             ; {ram.04DD}
A642: 60              RTS                         ; 
A643: A0 00           LDY     #$00                ; 
A645: B5 73           LDA     $73,X               ; {ram.0073}
A647: 38              SEC                         ; 
A648: F5 73           SBC     $73,X               ; {ram.0073}
A64A: 20 1F 70        JSR     $701F               ; {ram.701F}
A64D: CD D9 04        CMP     $04D9               ; {ram.04D9}
A650: 90 01           BCC     $A653               ; {}
A652: C8              INY                         ; 
A653: CD DB 04        CMP     $04DB               ; {ram.04DB}
A656: 90 01           BCC     $A659               ; {}
A658: C8              INY                         ; 
A659: B5 87           LDA     $87,X               ; {ram.0087}
A65B: 38              SEC                         ; 
A65C: F5 86           SBC     $86,X               ; {ram.0086}
A65E: 20 1F 70        JSR     $701F               ; {ram.701F}
A661: CD DA 04        CMP     $04DA               ; {ram.04DA}
A664: 90 03           BCC     $A669               ; {}
A666: C8              INY                         ; 
A667: C8              INY                         ; 
A668: C8              INY                         ; 
A669: CD DC 04        CMP     $04DC               ; {ram.04DC}
A66C: 90 03           BCC     $A671               ; {}
A66E: C8              INY                         ; 
A66F: C8              INY                         ; 
A670: C8              INY                         ; 
A671: 98              TYA                         ; 
A672: 20 E2 E5        JSR     $E5E2               ; 
A675: 87                              ;
A676: A6 9C           LDX     <$9C                ; {ram.009C}
A678: A6 B5           LDX     <$B5                ; {ram.00B5}
A67A: A6 9C           LDX     <$9C                ; {ram.009C}
A67C: A6 9C           LDX     <$9C                ; {ram.009C}
A67E: A6 B5           LDX     <$B5                ; {ram.00B5}
A680: A6 9D           LDX     <$9D                ; {ram.009D}
A682: A6 9D           LDX     <$9D                ; {ram.009D}
A684: A6 C5           LDX     <$C5                ; {ram.00C5}
A686: A6 A5           LDX     <$A5                ; {ram.00A5}
A688: 18              CLC                         ; 
A689: 10 1F           BPL     $A6AA               ; {}
A68B: B5 86           LDA     $86,X               ; {ram.0086}
A68D: A8              TAY                         ; 
A68E: C8              INY                         ; 
A68F: C8              INY                         ; 
A690: D5 87           CMP     $87,X               ; {ram.0087}
A692: F0 02           BEQ     $A696               ; {}
A694: B0 04           BCS     $A69A               ; {}
A696: 88              DEY                         ; 
A697: 88              DEY                         ; 
A698: 88              DEY                         ; 
A699: 88              DEY                         ; 
A69A: 94 86           STY     $86,X               ; {ram.0086}
A69C: 60              RTS                         ; 
A69D: B5 86           LDA     $86,X               ; {ram.0086}
A69F: A8              TAY                         ; 
A6A0: C8              INY                         ; 
A6A1: C8              INY                         ; 
A6A2: D5 87           CMP     $87,X               ; {ram.0087}
A6A4: F0 F4           BEQ     $A69A               ; {}
A6A6: 90 F2           BCC     $A69A               ; {}
A6A8: B0 EC           BCS     $A696               ; {}
A6AA: B5 72           LDA     $72,X               ; {ram.0072}
A6AC: A8              TAY                         ; 
A6AD: C8              INY                         ; 
A6AE: C8              INY                         ; 
A6AF: D5 73           CMP     $73,X               ; {ram.0073}
A6B1: B0 0F           BCS     $A6C2               ; {}
A6B3: 90 09           BCC     $A6BE               ; {}
A6B5: B5 72           LDA     $72,X               ; {ram.0072}
A6B7: A8              TAY                         ; 
A6B8: C8              INY                         ; 
A6B9: C8              INY                         ; 
A6BA: D5 73           CMP     $73,X               ; {ram.0073}
A6BC: 90 04           BCC     $A6C2               ; {}
A6BE: 88              DEY                         ; 
A6BF: 88              DEY                         ; 
A6C0: 88              DEY                         ; 
A6C1: 88              DEY                         ; 
A6C2: 94 72           STY     $72,X               ; {ram.0072}
A6C4: 60              RTS                         ; 
A6C5: A5 18           LDA     <$18                ; {ram.0018}
A6C7: 10 EC           BPL     $A6B5               ; {}
A6C9: 30 D2           BMI     $A69D               ; {}
A6CB: A0 03           LDY     #$03                ; 
A6CD: 84 03           STY     <$03                ; {ram.GP_03}
A6CF: 48              PHA                         ; 
A6D0: AD D7 04        LDA     $04D7               ; {ram.04D7}
A6D3: 0A              ASL     A                   ; 
A6D4: 0A              ASL     A                   ; 
A6D5: 0A              ASL     A                   ; 
A6D6: E0 05           CPX     #$05                ; 
A6D8: F0 03           BEQ     $A6DD               ; {}
A6DA: 18              CLC                         ; 
A6DB: 69 20           ADC     #$20                ; 
A6DD: A8              TAY                         ; 
A6DE: 68              PLA                         ; 
A6DF: 20 A5 79        JSR     $79A5               ; {ram.79A5}
A6E2: 4C FA A6        JMP     $A6FA               ; {}
A6E5: A2 05           LDX     #$05                ; 
A6E7: A9 DA           LDA     #$DA                ; 
A6E9: E0 05           CPX     #$05                ; 
A6EB: D0 02           BNE     $A6EF               ; {}
A6ED: A9 DC           LDA     #$DC                ; 
A6EF: E0 05           CPX     #$05                ; 
A6F1: F0 D8           BEQ     $A6CB               ; {}
A6F3: E0 01           CPX     #$01                ; 
A6F5: F0 D4           BEQ     $A6CB               ; {}
A6F7: 20 8D 79        JSR     $798D               ; {ram.798D}
A6FA: E0 05           CPX     #$05                ; 
A6FC: F0 07           BEQ     $A705               ; {}
A6FE: E0 01           CPX     #$01                ; 
A700: F0 03           BEQ     $A705               ; {}
A702: 4C 84 A7        JMP     $A784               ; {}
A705: 20 D0 79        JSR     $79D0               ; {ram.79D0}
A708: BD C0 00        LDA     $00C0,X             ; {ram.00C0}
A70B: F0 08           BEQ     $A715               ; {}
A70D: A9 06           LDA     #$06                ; 
A70F: 8D E6 04        STA     $04E6               ; {ram.04E6}
A712: 8D 10 05        STA     $0510               ; {ram.0510}
A715: 20 E4 EE        JSR     $EEE4               ; 
A718: E0 01           CPX     #$01                ; 
A71A: F0 65           BEQ     $A781               ; {}
A71C: 20 00 80        JSR     $8000               ; {}
A71F: BD 05 04        LDA     $0405,X             ; {ram.0405}
A722: F0 60           BEQ     $A784               ; {}
A724: A9 60           LDA     #$60                ; 
A726: 9D 85 04        STA     $0485,X             ; 
A729: 8A              TXA                         ; 
A72A: 48              PHA                         ; 
A72B: E0 05           CPX     #$05                ; 
A72D: D0 19           BNE     $A748               ; {}
A72F: AD D7 04        LDA     $04D7               ; {ram.04D7}
A732: 18              CLC                         ; 
A733: 69 07           ADC     #$07                ; 
A735: AA              TAX                         ; 
A736: A9 FF           LDA     #$FF                ; 
A738: 9D 92 04        STA     $0492,X             ; 
A73B: A5 75           LDA     <$75                ; {ram.0075}
A73D: 95 70           STA     $70,X               ; {ram.0070}
A73F: A5 89           LDA     <$89                ; {ram.0089}
A741: 95 84           STA     $84,X               ; {ram.0084}
A743: A9 46           LDA     #$46                ; 
A745: 9D 4F 03        STA     $034F,X             ; {ram.034F}
A748: 68              PLA                         ; 
A749: AA              TAX                         ; 
A74A: AD D7 04        LDA     $04D7               ; {ram.04D7}
A74D: 0A              ASL     A                   ; 
A74E: 0A              ASL     A                   ; 
A74F: 0A              ASL     A                   ; 
A750: A8              TAY                         ; 
A751: A9 F8           LDA     #$F8                ; 
A753: 99 00 02        STA     $0200,Y             ; {ram.0200}
A756: 99 20 02        STA     $0220,Y             ; {ram.0220}
A759: AC D7 04        LDY     $04D7               ; {ram.04D7}
A75C: B9 BE E6        LDA     $E6BE,Y             ; 
A75F: 0D 11 05        ORA     $0511               ; {ram.0511}
A762: 8D 11 05        STA     $0511               ; {ram.0511}
A765: 85 00           STA     <$00                ; {ram.GP_00}
A767: A9 00           LDA     #$00                ; 
A769: A0 04           LDY     #$04                ; 
A76B: 46 00           LSR     <$00                ; {ram.GP_00}
A76D: 69 00           ADC     #$00                ; 
A76F: 88              DEY                         ; 
A770: D0 F9           BNE     $A76B               ; {}
A772: 85 00           STA     <$00                ; {ram.GP_00}
A774: AD 50 03        LDA     $0350               ; {ram.0350}
A777: 38              SEC                         ; 
A778: E9 41           SBC     #$41                ; 
A77A: C5 00           CMP     <$00                ; {ram.GP_00}
A77C: F0 0E           BEQ     $A78C               ; {}
A77E: 4C DA FE        JMP     $FEDA               ; 
A781: 20 DA FE        JSR     $FEDA               ; 
A784: CA              DEX                         ; 
A785: E0 01           CPX     #$01                ; 
A787: 90 71           BCC     $A7FA               ; {}
A789: 4C E7 A6        JMP     $A6E7               ; {}
A78C: 20 12 75        JSR     $7512               ; {ram.7512}
A78F: 20 10 B0        JSR     $B010               ; {}
A792: A9 11           LDA     #$11                ; 
A794: 8D 06 04        STA     $0406               ; {ram.0406}
A797: A0 01           LDY     #$01                ; 
A799: A9 00           LDA     #$00                ; 
A79B: 99 50 03        STA     $0350,Y             ; {ram.0350}
A79E: C8              INY                         ; 
A79F: C0 0A           CPY     #$0A                ; 
A7A1: 90 F6           BCC     $A799               ; {}
A7A3: 60              RTS                         ; 
A7A4: AD 18 04        LDA     $0418               ; {ram.0418}
A7A7: D0 52           BNE     $A7FB               ; {}
A7A9: A5 75           LDA     <$75                ; {ram.0075}
A7AB: AC 15 04        LDY     $0415               ; {ram.0415}
A7AE: 20 FF A7        JSR     $A7FF               ; {}
A7B1: 85 75           STA     <$75                ; {ram.0075}
A7B3: A5 89           LDA     <$89                ; {ram.0089}
A7B5: AC 16 04        LDY     $0416               ; {ram.0416}
A7B8: 20 FF A7        JSR     $A7FF               ; {}
A7BB: 85 89           STA     <$89                ; {ram.0089}
A7BD: EE 17 04        INC     $0417               ; {ram.0417}
A7C0: AD 17 04        LDA     $0417               ; {ram.0417}
A7C3: C9 04           CMP     #$04                ; 
A7C5: 90 33           BCC     $A7FA               ; {}
A7C7: A9 00           LDA     #$00                ; 
A7C9: 8D 17 04        STA     $0417               ; {ram.0417}
A7CC: EE 13 04        INC     $0413               ; {ram.0413}
A7CF: AD 13 04        LDA     $0413               ; {ram.0413}
A7D2: C9 0C           CMP     #$0C                ; 
A7D4: 90 0D           BCC     $A7E3               ; {}
A7D6: A9 00           LDA     #$00                ; 
A7D8: 8D 13 04        STA     $0413               ; {ram.0413}
A7DB: AD 15 04        LDA     $0415               ; {ram.0415}
A7DE: 49 FF           EOR     #$FF                ; 
A7E0: 8D 15 04        STA     $0415               ; {ram.0415}
A7E3: EE 14 04        INC     $0414               ; {ram.0414}
A7E6: AD 14 04        LDA     $0414               ; {ram.0414}
A7E9: C9 06           CMP     #$06                ; 
A7EB: 90 0D           BCC     $A7FA               ; {}
A7ED: A9 00           LDA     #$00                ; 
A7EF: 8D 14 04        STA     $0414               ; {ram.0414}
A7F2: AD 16 04        LDA     $0416               ; {ram.0416}
A7F5: 49 FF           EOR     #$FF                ; 
A7F7: 8D 16 04        STA     $0416               ; {ram.0416}
A7FA: 60              RTS                         ; 
A7FB: CE 18 04        DEC     $0418               ; {ram.0418}
A7FE: 60              RTS                         ; 
A7FF: D0 04           BNE     $A805               ; {}
A801: 18              CLC                         ; 
A802: 69 01           ADC     #$01                ; 
A804: 60              RTS                         ; 
A805: 38              SEC                         ; 
A806: E9 01           SBC     #$01                ; 
A808: 60              RTS                         ; 
A809: C0 C4           CPY     #$C4                ; 
A80B: C8              INY                         ; 
A80C: C2                              ;
A80D: C6 CA           DEC     <$CA                ; {ram.00CA}
A80F: CC C4 CE        CPY     $CEC4               ; 
A812: C2                              ;
A813: C6 D0           DEC     <$D0                ; {ram.00D0}
A815: D2                              ;
A816: D6 D8           DEC     $D8,X               ; {ram.00D8}
A818: D4                              ;
A819: C6 D0           DEC     <$D0                ; {ram.00D0}
A81B: 06 00           ASL     <$00                ; {ram.GP_00}
A81D: 06 0C           ASL     <$0C                ; {ram.000C}
A81F: CE E6 04        DEC     $04E6               ; {ram.04E6}
A822: 4C 44 A8        JMP     $A844               ; {}
A825: AD E6 04        LDA     $04E6               ; {ram.04E6}
A828: D0 F5           BNE     $A81F               ; {}
A82A: A9 10           LDA     #$10                ; 
A82C: AC 10 05        LDY     $0510               ; {ram.0510}
A82F: F0 05           BEQ     $A836               ; {}
A831: CE 10 05        DEC     $0510               ; {ram.0510}
A834: A9 06           LDA     #$06                ; 
A836: 8D E6 04        STA     $04E6               ; {ram.04E6}
A839: AD E7 04        LDA     $04E7               ; {ram.04E7}
A83C: 18              CLC                         ; 
A83D: 69 01           ADC     #$01                ; 
A83F: 29 03           AND     #$03                ; 
A841: 8D E7 04        STA     $04E7               ; {ram.04E7}
A844: A9 00           LDA     #$00                ; 
A846: 85 06           STA     <$06                ; {ram.0006}
A848: AC E7 04        LDY     $04E7               ; {ram.04E7}
A84B: BE 1B A8        LDX     $A81B,Y             ; {}
A84E: A9 00           LDA     #$00                ; 
A850: 85 07           STA     <$07                ; {ram.0007}
A852: AC 41 03        LDY     $0341               ; {ram.0341}
A855: B9 AB 77        LDA     $77AB,Y             ; 
A858: A8              TAY                         ; 
A859: A5 06           LDA     <$06                ; {ram.0006}
A85B: 0A              ASL     A                   ; 
A85C: 0A              ASL     A                   ; 
A85D: 0A              ASL     A                   ; 
A85E: 0A              ASL     A                   ; 
A85F: 69 57           ADC     #$57                ; 
A861: 99 00 02        STA     $0200,Y             ; {ram.0200}
A864: BD 09 A8        LDA     $A809,X             ; {}
A867: 99 01 02        STA     $0201,Y             ; {ram.0201}
A86A: AD F5 04        LDA     $04F5               ; {ram.04F5}
A86D: D0 02           BNE     $A871               ; {}
A86F: A9 03           LDA     #$03                ; 
A871: 29 03           AND     #$03                ; 
A873: 99 02 02        STA     $0202,Y             ; {ram.0202}
A876: A5 07           LDA     <$07                ; {ram.0007}
A878: 0A              ASL     A                   ; 
A879: 0A              ASL     A                   ; 
A87A: 0A              ASL     A                   ; 
A87B: 69 74           ADC     #$74                ; 
A87D: 99 03 02        STA     $0203,Y             ; 
A880: E8              INX                         ; 
A881: 20 36 6E        JSR     $6E36               ; {ram.6E36}
A884: E6 07           INC     <$07                ; {ram.0007}
A886: A5 07           LDA     <$07                ; {ram.0007}
A888: C9 03           CMP     #$03                ; 
A88A: 90 C6           BCC     $A852               ; {}
A88C: E6 06           INC     <$06                ; {ram.0006}
A88E: A5 06           LDA     <$06                ; {ram.0006}
A890: C9 02           CMP     #$02                ; 
A892: 90 BA           BCC     $A84E               ; {}
A894: 60              RTS                         ; 
A895: FF                              ;
A896: FF                              ;
A897: FF                              ;
A898: FF                              ;
A899: FF                              ;
A89A: FF                              ;
A89B: FF                              ;
A89C: FF                              ;
A89D: FF                              ;
A89E: FF                              ;
A89F: FF                              ;
A8A0: FF                              ;
A8A1: FF                              ;
A8A2: FF                              ;
A8A3: FF                              ;
A8A4: FF                              ;
A8A5: FF                              ;
A8A6: FF                              ;
A8A7: FF                              ;
A8A8: FF                              ;
A8A9: FF                              ;
A8AA: FF                              ;
A8AB: FF                              ;
A8AC: FF                              ;
A8AD: FF                              ;
A8AE: FF                              ;
A8AF: FF                              ;
A8B0: FF                              ;
A8B1: FF                              ;
A8B2: FF                              ;
A8B3: FF                              ;
A8B4: FF                              ;
A8B5: FF                              ;
A8B6: FF                              ;
A8B7: FF                              ;
A8B8: FF                              ;
A8B9: FF                              ;
A8BA: FF                              ;
A8BB: FF                              ;
A8BC: FF                              ;
A8BD: FF                              ;
A8BE: FF                              ;
A8BF: FF                              ;
A8C0: 78              SEI                         ; 
A8C1: 60              RTS                         ; 
A8C2: 70 80           BVS     $A844               ; {}
A8C4: 90 88           BCC     $A84E               ; {}
A8C6: B5 9D           LDA     $9D,X               ; {ram.009D}
A8C8: 9D B5 A2        STA     $A2B5,X             ; {}
A8CB: 05 BD           ORA     <$BD                ; {ram.00BD}
A8CD: BF                              ;
A8CE: A8              TAY                         ; 
A8CF: 95 70           STA     $70,X               ; {ram.0070}
A8D1: BD C4 A8        LDA     $A8C4,X             ; {}
A8D4: 95 84           STA     $84,X               ; {ram.0084}
A8D6: A9 3F           LDA     #$3F                ; 
A8D8: 9D 4F 03        STA     $034F,X             ; {ram.034F}
A8DB: CA              DEX                         ; 
A8DC: D0 EE           BNE     $A8CC               ; {}
A8DE: A9 37           LDA     #$37                ; 
A8E0: 8D 50 03        STA     $0350               ; {ram.0350}
A8E3: 60              RTS                         ; 
A8E4: A0 09           LDY     #$09                ; 
A8E6: A9 40           LDA     #$40                ; 
A8E8: 99 71 00        STA     $0071,Y             ; {ram.0071}
A8EB: A9 8D           LDA     #$8D                ; 
A8ED: 99 85 00        STA     $0085,Y             ; {ram.0085}
A8F0: A9 00           LDA     #$00                ; 
A8F2: 99 99 00        STA     $0099,Y             ; {ram.0099}
A8F5: 99 06 04        STA     $0406,Y             ; {ram.0406}
A8F8: 99 93 04        STA     $0493,Y             ; 
A8FB: AD C0 04        LDA     $04C0               ; {ram.04C0}
A8FE: 99 C0 04        STA     $04C0,Y             ; {ram.04C0}
A901: AD 86 04        LDA     $0486               ; {ram.0486}
A904: 99 86 04        STA     $0486,Y             ; {ram.0486}
A907: AD 50 03        LDA     $0350               ; {ram.0350}
A90A: 99 50 03        STA     $0350,Y             ; {ram.0350}
A90D: 88              DEY                         ; 
A90E: 10 D6           BPL     $A8E6               ; {}
A910: A9 08           LDA     #$08                ; 
A912: 85 9D           STA     <$9D                ; {ram.009D}
A914: 8D 85 03        STA     $0385               ; {ram.0385}
A917: 85 A2           STA     <$A2                ; {ram.00A2}
A919: 8D 8A 03        STA     $038A               ; {ram.038A}
A91C: AD 50 03        LDA     $0350               ; {ram.0350}
A91F: 8D E7 04        STA     $04E7               ; {ram.04E7}
A922: 38              SEC                         ; 
A923: E9 39           SBC     #$39                ; 
A925: 8D E6 04        STA     $04E6               ; {ram.04E6}
A928: A9 08           LDA     #$08                ; 
A92A: 8D 4E 03        STA     $034E               ; {ram.034E}
A92D: 60              RTS                         ; 
A92E: A9 FE           LDA     #$FE                ; 
A930: 9D B2 04        STA     $04B2,X             ; 
A933: A9 80           LDA     #$80                ; 
A935: 95 70           STA     $70,X               ; {ram.0070}
A937: A9 70           LDA     #$70                ; 
A939: 95 84           STA     $84,X               ; {ram.0084}
A93B: A9 08           LDA     #$08                ; 
A93D: 95 98           STA     $98,X               ; {ram.0098}
A93F: A9 1F           LDA     #$1F                ; 
A941: 9D 1F 04        STA     $041F,X             ; {ram.041F}
A944: A9 40           LDA     #$40                ; 
A946: 8D D1 04        STA     $04D1               ; {ram.04D1}
A949: 8D 01 06        STA     $0601               ; {ram.??SND_601??}
A94C: A9 FF           LDA     #$FF                ; 
A94E: 95 29           STA     $29,X               ; {ram.0029}
A950: A9 25           LDA     #$25                ; 
A952: AC 50 03        LDY     $0350               ; {ram.0350}
A955: C0 47           CPY     #$47                ; 
A957: F0 02           BEQ     $A95B               ; {}
A959: A9 26           LDA     #$26                ; 
A95B: A0 02           LDY     #$02                ; 
A95D: 85 00           STA     <$00                ; {ram.GP_00}
A95F: A5 00           LDA     <$00                ; {ram.GP_00}
A961: 99 4F 03        STA     $034F,Y             ; {ram.034F}
A964: A9 FE           LDA     #$FE                ; 
A966: 99 B2 04        STA     $04B2,Y             ; 
A969: C8              INY                         ; 
A96A: C0 0A           CPY     #$0A                ; 
A96C: D0 F1           BNE     $A95F               ; {}
A96E: 60              RTS                         ; 
A96F: A9 FA           LDA     #$FA                ; 
A971: 9D B2 04        STA     $04B2,X             ; 
A974: A9 40           LDA     #$40                ; 
A976: 85 AC           STA     <$AC                ; {ram.00AC}
A978: 85 28           STA     <$28                ; {ram.0028}
A97A: A9 02           LDA     #$02                ; 
A97C: 8D 01 06        STA     $0601               ; {ram.??SND_601??}
A97F: A9 10           LDA     #$10                ; 
A981: 20 7C 6D        JSR     $6D7C               ; {ram.6D7C}
A984: 4C D6 FE        JMP     $FED6               ; 
A987: 20 CA 79        JSR     $79CA               ; {ram.79CA}
A98A: B5 AC           LDA     $AC,X               ; {ram.00AC}
A98C: D0 2A           BNE     $A9B8               ; {}
A98E: A5 70           LDA     <$70                ; {ram.0070}
A990: C9 70           CMP     #$70                ; 
A992: 90 23           BCC     $A9B7               ; {}
A994: C9 81           CMP     #$81                ; 
A996: B0 1F           BCS     $A9B7               ; {}
A998: A5 84           LDA     <$84                ; {ram.0084}
A99A: C9 95           CMP     #$95                ; 
A99C: D0 19           BNE     $A9B7               ; {}
A99E: F6 AC           INC     $AC,X               ; {ram.00AC}
A9A0: A9 40           LDA     #$40                ; 
A9A2: 85 AC           STA     <$AC                ; {ram.00AC}
A9A4: A9 88           LDA     #$88                ; 
A9A6: 85 70           STA     <$70                ; {ram.0070}
A9A8: 85 84           STA     <$84                ; {ram.0084}
A9AA: A9 02           LDA     #$02                ; 
A9AC: 85 98           STA     <$98                ; {ram.0098}
A9AE: A9 06           LDA     #$06                ; 
A9B0: 8D 00 06        STA     $0600               ; {ram.SND_ReqMusic}
A9B3: A9 80           LDA     #$80                ; 
A9B5: 95 28           STA     $28,X               ; {ram.0028}
A9B7: 60              RTS                         ; 
A9B8: 20 29 F2        JSR     $F229               ; 
A9BB: B5 28           LDA     $28,X               ; {ram.0028}
A9BD: D0 F8           BNE     $A9B7               ; {}
A9BF: 85 11           STA     <$11                ; {ram.0011}
A9C1: 85 13           STA     <$13                ; {ram.0013}
A9C3: 85 AC           STA     <$AC                ; {ram.00AC}
A9C5: A9 13           LDA     #$13                ; 
A9C7: 85 12           STA     <$12                ; {ram.0012}
A9C9: A9 20           LDA     #$20                ; 
A9CB: 85 7C           STA     <$7C                ; {ram.007C}
A9CD: A9 01           LDA     #$01                ; 
A9CF: 85 7D           STA     <$7D                ; {ram.007D}
A9D1: A9 24           LDA     #$24                ; 
A9D3: 85 0A           STA     <$0A                ; {ram.000A}
A9D5: 4C D8 E8        JMP     $E8D8               ; 
A9D8: A9 06           LDA     #$06                ; 
A9DA: 20 76 84        JSR     $8476               ; {}
A9DD: 20 D0 79        JSR     $79D0               ; {ram.79D0}
A9E0: BD 05 04        LDA     $0405,X             ; {ram.0405}
A9E3: F0 05           BEQ     $A9EA               ; {}
A9E5: A9 5D           LDA     #$5D                ; 
A9E7: 9D 4F 03        STA     $034F,X             ; {ram.034F}
A9EA: 60              RTS                         ; 
A9EB: B5 98           LDA     $98,X               ; {ram.0098}
A9ED: F0 FB           BEQ     $A9EA               ; {}
A9EF: AD 6C 06        LDA     $066C               ; {ram.066C}
A9F2: D0 0E           BNE     $AA02               ; {}
A9F4: 20 24 AB        JSR     $AB24               ; {}
A9F7: E0 05           CPX     #$05                ; 
A9F9: F0 04           BEQ     $A9FF               ; {}
A9FB: E0 0A           CPX     #$0A                ; 
A9FD: D0 03           BNE     $AA02               ; {}
A9FF: 20 70 AA        JSR     $AA70               ; {}
AA02: B5 70           LDA     $70,X               ; {ram.0070}
AA04: 48              PHA                         ; 
AA05: 18              CLC                         ; 
AA06: 69 04           ADC     #$04                ; 
AA08: 95 70           STA     $70,X               ; {ram.0070}
AA0A: AD E6 04        LDA     $04E6               ; {ram.04E6}
AA0D: 49 03           EOR     #$03                ; 
AA0F: 85 03           STA     <$03                ; {ram.GP_03}
AA11: A9 9E           LDA     #$9E                ; 
AA13: E0 05           CPX     #$05                ; 
AA15: F0 06           BEQ     $AA1D               ; {}
AA17: E0 0A           CPX     #$0A                ; 
AA19: F0 02           BEQ     $AA1D               ; {}
AA1B: A9 A0           LDA     #$A0                ; 
AA1D: 20 91 79        JSR     $7991               ; {ram.7991}
AA20: 68              PLA                         ; 
AA21: 95 70           STA     $70,X               ; {ram.0070}
AA23: B5 98           LDA     $98,X               ; {ram.0098}
AA25: 48              PHA                         ; 
AA26: 20 D0 79        JSR     $79D0               ; {ram.79D0}
AA29: 68              PLA                         ; 
AA2A: 95 98           STA     $98,X               ; {ram.0098}
AA2C: BD 05 04        LDA     $0405,X             ; {ram.0405}
AA2F: F0 B9           BEQ     $A9EA               ; {}
AA31: 20 E4 EE        JSR     $EEE4               ; 
AA34: A9 20           LDA     #$20                ; 
AA36: 9D 85 04        STA     $0485,X             ; 
AA39: A0 FF           LDY     #$FF                ; 
AA3B: E0 06           CPX     #$06                ; 
AA3D: 90 02           BCC     $AA41               ; {}
AA3F: A0 04           LDY     #$04                ; 
AA41: C8              INY                         ; 
AA42: B9 50 03        LDA     $0350,Y             ; {ram.0350}
AA45: CD E7 04        CMP     $04E7               ; {ram.04E7}
AA48: D0 F7           BNE     $AA41               ; {}
AA4A: A9 11           LDA     #$11                ; 
AA4C: 99 29 00        STA     $0029,Y             ; {ram.0029}
AA4F: BD F0 04        LDA     $04F0,X             ; {ram.04F0}
AA52: 99 F1 04        STA     $04F1,Y             ; 
AA55: B5 70           LDA     $70,X               ; {ram.0070}
AA57: 99 71 00        STA     $0071,Y             ; {ram.0071}
AA5A: B5 84           LDA     $84,X               ; {ram.0084}
AA5C: 99 85 00        STA     $0085,Y             ; {ram.0085}
AA5F: C0 04           CPY     #$04                ; 
AA61: F0 87           BEQ     $A9EA               ; {}
AA63: C0 09           CPY     #$09                ; 
AA65: F0 83           BEQ     $A9EA               ; {}
AA67: A9 5D           LDA     #$5D                ; 
AA69: 99 50 03        STA     $0350,Y             ; {ram.0350}
AA6C: 4C DA FE        JMP     $FEDA               ; 
AA6F: 60              RTS                         ; 
AA70: B5 70           LDA     $70,X               ; {ram.0070}
AA72: 29 07           AND     #$07                ; 
AA74: D0 F9           BNE     $AA6F               ; {}
AA76: B5 84           LDA     $84,X               ; {ram.0084}
AA78: 18              CLC                         ; 
AA79: 69 03           ADC     #$03                ; 
AA7B: 29 07           AND     #$07                ; 
AA7D: D0 F0           BNE     $AA6F               ; {}
AA7F: A9 04           LDA     #$04                ; 
AA81: 85 00           STA     <$00                ; {ram.GP_00}
AA83: A0 00           LDY     #$00                ; 
AA85: E0 05           CPX     #$05                ; 
AA87: F0 02           BEQ     $AA8B               ; {}
AA89: A0 05           LDY     #$05                ; 
AA8B: B9 9A 00        LDA     $009A,Y             ; {ram.009A}
AA8E: 99 99 00        STA     $0099,Y             ; {ram.0099}
AA91: C8              INY                         ; 
AA92: C6 00           DEC     <$00                ; {ram.GP_00}
AA94: D0 F5           BNE     $AA8B               ; {}
AA96: B5 70           LDA     $70,X               ; {ram.0070}
AA98: 29 0F           AND     #$0F                ; 
AA9A: D0 5D           BNE     $AAF9               ; {}
AA9C: B5 84           LDA     $84,X               ; {ram.0084}
AA9E: 18              CLC                         ; 
AA9F: 69 03           ADC     #$03                ; 
AAA1: 29 0F           AND     #$0F                ; 
AAA3: D0 54           BNE     $AAF9               ; {}
AAA5: B5 98           LDA     $98,X               ; {ram.0098}
AAA7: 4A              LSR     A                   ; 
AAA8: 29 05           AND     #$05                ; 
AAAA: 85 00           STA     <$00                ; {ram.GP_00}
AAAC: B5 98           LDA     $98,X               ; {ram.0098}
AAAE: 0A              ASL     A                   ; 
AAAF: 29 0A           AND     #$0A                ; 
AAB1: 05 00           ORA     <$00                ; {ram.GP_00}
AAB3: 49 0F           EOR     #$0F                ; 
AAB5: 8D 0F 05        STA     $050F               ; {ram.050F}
AAB8: B5 18           LDA     $18,X               ; {ram.0018}
AABA: C9 80           CMP     #$80                ; 
AABC: 90 3C           BCC     $AAFA               ; {}
AABE: B5 98           LDA     $98,X               ; {ram.0098}
AAC0: B4 19           LDY     $19,X               ; {ram.0019}
AAC2: C0 80           CPY     #$80                ; 
AAC4: B0 12           BCS     $AAD8               ; {}
AAC6: 4A              LSR     A                   ; 
AAC7: 90 02           BCC     $AACB               ; {}
AAC9: A9 08           LDA     #$08                ; 
AACB: 2C 0F 05        BIT     $050F               ; {ram.050F}
AACE: F0 F6           BEQ     $AAC6               ; {}
AAD0: C0 40           CPY     #$40                ; 
AAD2: B0 04           BCS     $AAD8               ; {}
AAD4: A0 40           LDY     #$40                ; 
AAD6: 90 EE           BCC     $AAC6               ; {}
AAD8: 95 98           STA     $98,X               ; {ram.0098}
AADA: 85 0F           STA     <$0F                ; {ram.000F}
AADC: 20 B8 6F        JSR     $6FB8               ; {ram.6FB8}
AADF: A5 0F           LDA     <$0F                ; {ram.000F}
AAE1: D0 0E           BNE     $AAF1               ; {}
AAE3: B5 98           LDA     $98,X               ; {ram.0098}
AAE5: 4A              LSR     A                   ; 
AAE6: 90 02           BCC     $AAEA               ; {}
AAE8: A9 08           LDA     #$08                ; 
AAEA: 2C 0F 05        BIT     $050F               ; {ram.050F}
AAED: D0 E9           BNE     $AAD8               ; {}
AAEF: F0 F4           BEQ     $AAE5               ; {}
AAF1: 20 FA ED        JSR     $EDFA               ; 
AAF4: CD 4A 03        CMP     $034A               ; {ram.034A}
AAF7: B0 EA           BCS     $AAE3               ; {}
AAF9: 60              RTS                         ; 
AAFA: A9 01           LDA     #$01                ; 
AAFC: 85 02           STA     <$02                ; {ram.GP_02}
AAFE: A5 70           LDA     <$70                ; {ram.0070}
AB00: 38              SEC                         ; 
AB01: F5 70           SBC     $70,X               ; {ram.0070}
AB03: B0 02           BCS     $AB07               ; {}
AB05: 06 02           ASL     <$02                ; {ram.GP_02}
AB07: A9 04           LDA     #$04                ; 
AB09: 85 03           STA     <$03                ; {ram.GP_03}
AB0B: A5 84           LDA     <$84                ; {ram.0084}
AB0D: 38              SEC                         ; 
AB0E: F5 84           SBC     $84,X               ; {ram.0084}
AB10: B0 02           BCS     $AB14               ; {}
AB12: 06 03           ASL     <$03                ; {ram.GP_03}
AB14: A5 02           LDA     <$02                ; {ram.GP_02}
AB16: 2C 0F 05        BIT     $050F               ; {ram.050F}
AB19: F0 04           BEQ     $AB1F               ; {}
AB1B: 24 98           BIT     <$98                ; {ram.0098}
AB1D: D0 02           BNE     $AB21               ; {}
AB1F: A5 03           LDA     <$03                ; {ram.GP_03}
AB21: 4C D8 AA        JMP     $AAD8               ; {}
AB24: A9 A1           LDA     #$A1                ; 
AB26: 85 02           STA     <$02                ; {ram.GP_02}
AB28: B5 98           LDA     $98,X               ; {ram.0098}
AB2A: 24 02           BIT     <$02                ; {ram.GP_02}
AB2C: F0 08           BEQ     $AB36               ; {}
AB2E: B5 70           LDA     $70,X               ; {ram.0070}
AB30: 18              CLC                         ; 
AB31: 6D E6 04        ADC     $04E6               ; {ram.04E6}
AB34: 95 70           STA     $70,X               ; {ram.0070}
AB36: B5 98           LDA     $98,X               ; {ram.0098}
AB38: 06 02           ASL     <$02                ; {ram.GP_02}
AB3A: 24 02           BIT     <$02                ; {ram.GP_02}
AB3C: F0 07           BEQ     $AB45               ; {}
AB3E: B5 70           LDA     $70,X               ; {ram.0070}
AB40: ED E6 04        SBC     $04E6               ; {ram.04E6}
AB43: 95 70           STA     $70,X               ; {ram.0070}
AB45: B5 98           LDA     $98,X               ; {ram.0098}
AB47: 06 02           ASL     <$02                ; {ram.GP_02}
AB49: 24 02           BIT     <$02                ; {ram.GP_02}
AB4B: F0 07           BEQ     $AB54               ; {}
AB4D: B5 84           LDA     $84,X               ; {ram.0084}
AB4F: 6D E6 04        ADC     $04E6               ; {ram.04E6}
AB52: 95 84           STA     $84,X               ; {ram.0084}
AB54: B5 98           LDA     $98,X               ; {ram.0098}
AB56: 06 02           ASL     <$02                ; {ram.GP_02}
AB58: 24 02           BIT     <$02                ; {ram.GP_02}
AB5A: F0 07           BEQ     $AB63               ; {}
AB5C: B5 84           LDA     $84,X               ; {ram.0084}
AB5E: ED E6 04        SBC     $04E6               ; {ram.04E6}
AB61: 95 84           STA     $84,X               ; {ram.0084}
AB63: 60              RTS                         ; 
AB64: FF                              ;
AB65: 50 20           BVC     $AB87               ; {}
AB67: AE AB A9        LDX     $A9AB               ; {}
AB6A: 00              BRK                         ; 
AB6B: 9D 6B 04        STA     $046B,X             ; 
AB6E: 9D 78 04        STA     $0478,X             ; 
AB71: 20 88 B2        JSR     $B288               ; {}
AB74: A9 02           LDA     #$02                ; 
AB76: 20 76 84        JSR     $8476               ; {}
AB79: A0 08           LDY     #$08                ; 
AB7B: B9 50 03        LDA     $0350,Y             ; {ram.0350}
AB7E: C9 25           CMP     #$25                ; 
AB80: F0 13           BEQ     $AB95               ; {}
AB82: C9 26           CMP     #$26                ; 
AB84: F0 0F           BEQ     $AB95               ; {}
AB86: 88              DEY                         ; 
AB87: D0 F2           BNE     $AB7B               ; {}
AB89: 20 D0 79        JSR     $79D0               ; {ram.79D0}
AB8C: 20 00 80        JSR     $8000               ; {}
AB8F: 20 0D 80        JSR     $800D               ; {}
AB92: 4C 98 AB        JMP     $AB98               ; {}
AB95: 20 A7 7A        JSR     $7AA7               ; {ram.7AA7}
AB98: B5 29           LDA     $29,X               ; {ram.0029}
AB9A: 0D 97 03        ORA     $0397               ; {ram.0397}
AB9D: D0 0E           BNE     $ABAD               ; {}
AB9F: BD 5E 04        LDA     $045E,X             ; 
ABA2: 49 01           EOR     #$01                ; 
ABA4: 9D 5E 04        STA     $045E,X             ; 
ABA7: 98              TYA                         ; 
ABA8: B9 64 AB        LDA     $AB64,Y             ; {}
ABAB: 95 29           STA     $29,X               ; {ram.0029}
ABAD: 60              RTS                         ; 
ABAE: BD 44 04        LDA     $0444,X             ; 
ABB1: 20 E2 E5        JSR     $E5E2               ; 
ABB4: 66 B2           ROR     <$B2                ; {ram.00B2}
ABB6: BC AB 08        LDY     $08AB,X             ; 
ABB9: B3                              ;
ABBA: 78              SEI                         ; 
ABBB: B3                              ;
ABBC: A0 02           LDY     #$02                ; 
ABBE: B5 18           LDA     $18,X               ; {ram.0018}
ABC0: C9 40           CMP     #$40                ; 
ABC2: B0 01           BCS     $ABC5               ; {}
ABC4: C8              INY                         ; 
ABC5: 98              TYA                         ; 
ABC6: 9D 44 04        STA     $0444,X             ; 
ABC9: A9 08           LDA     #$08                ; 
ABCB: 9D 2C 04        STA     $042C,X             ; {ram.!SplashMode}
ABCE: 60              RTS                         ; 
ABCF: 14                              ;
ABD0: 10 0C           BPL     $ABDE               ; {}
ABD2: 08              PHP                         ; 
ABD3: 04                              ;
ABD4: 00              BRK                         ; 
ABD5: 1C                              ;
ABD6: 06 05           ASL     <$05                ; {ram.0005}
ABD8: 06 06           ASL     <$06                ; {ram.0006}
ABDA: B5 AC           LDA     $AC,X               ; {ram.00AC}
ABDC: D0 3F           BNE     $AC1D               ; {}
ABDE: E0 02           CPX     #$02                ; 
ABE0: F0 11           BEQ     $ABF3               ; {}
ABE2: A5 AE           LDA     <$AE                ; {ram.00AE}
ABE4: F0 36           BEQ     $AC1C               ; {}
ABE6: 8A              TXA                         ; 
ABE7: 38              SEC                         ; 
ABE8: E9 03           SBC     #$03                ; 
ABEA: A8              TAY                         ; 
ABEB: AD 96 03        LDA     $0396               ; {ram.0396}
ABEE: D9 CF AB        CMP     $ABCF,Y             ; {}
ABF1: D0 29           BNE     $AC1C               ; {}
ABF3: E0 09           CPX     #$09                ; 
ABF5: D0 02           BNE     $ABF9               ; {}
ABF7: E6 AD           INC     <$AD                ; {ram.00AD}
ABF9: F6 AC           INC     $AC,X               ; {ram.00AC}
ABFB: A9 80           LDA     #$80                ; 
ABFD: 95 98           STA     $98,X               ; {ram.0098}
ABFF: A9 18           LDA     #$18                ; 
AC01: 9D 94 03        STA     $0394,X             ; {ram.0394}
AC04: A5 71           LDA     <$71                ; {ram.0071}
AC06: 95 70           STA     $70,X               ; {ram.0070}
AC08: A9 2C           LDA     #$2C                ; 
AC0A: BC 4F 03        LDY     $034F,X             ; {ram.034F}
AC0D: C0 25           CPY     #$25                ; 
AC0F: F0 02           BEQ     $AC13               ; {}
AC11: A9 18           LDA     #$18                ; 
AC13: 85 00           STA     <$00                ; {ram.GP_00}
AC15: A5 85           LDA     <$85                ; {ram.0085}
AC17: 38              SEC                         ; 
AC18: E5 00           SBC     <$00                ; {ram.GP_00}
AC1A: 95 84           STA     $84,X               ; {ram.0084}
AC1C: 60              RTS                         ; 
AC1D: B5 70           LDA     $70,X               ; {ram.0070}
AC1F: 18              CLC                         ; 
AC20: 6D 6C 04        ADC     $046C               ; {ram.046C}
AC23: 95 70           STA     $70,X               ; {ram.0070}
AC25: B5 84           LDA     $84,X               ; {ram.0084}
AC27: 18              CLC                         ; 
AC28: 6D 79 04        ADC     $0479               ; {ram.0479}
AC2B: 95 84           STA     $84,X               ; {ram.0084}
AC2D: A9 00           LDA     #$00                ; 
AC2F: 85 0B           STA     <$0B                ; {ram.000B}
AC31: A9 70           LDA     #$70                ; 
AC33: BC 4F 03        LDY     $034F,X             ; {ram.034F}
AC36: C0 25           CPY     #$25                ; 
AC38: F0 02           BEQ     $AC3C               ; {}
AC3A: A9 60           LDA     #$60                ; 
AC3C: 20 59 B4        JSR     $B459               ; {}
AC3F: AC 5F 04        LDY     $045F               ; {ram.045F}
AC42: BD 4F 03        LDA     $034F,X             ; {ram.034F}
AC45: C9 25           CMP     #$25                ; 
AC47: D0 0C           BNE     $AC55               ; {}
AC49: B9 D6 AB        LDA     $ABD6,Y             ; {}
AC4C: 48              PHA                         ; 
AC4D: B9 D8 AB        LDA     $ABD8,Y             ; {}
AC50: A8              TAY                         ; 
AC51: 68              PLA                         ; 
AC52: 4C 59 AC        JMP     $AC59               ; {}
AC55: B9 D7 AB        LDA     $ABD7,Y             ; {}
AC58: A8              TAY                         ; 
AC59: 20 BD B3        JSR     $B3BD               ; {}
AC5C: 95 84           STA     $84,X               ; {ram.0084}
AC5E: 20 71 AC        JSR     $AC71               ; {}
AC61: A5 AD           LDA     <$AD                ; {ram.00AD}
AC63: F0 0B           BEQ     $AC70               ; {}
AC65: 20 D0 79        JSR     $79D0               ; {ram.79D0}
AC68: BD 05 04        LDA     $0405,X             ; {ram.0405}
AC6B: F0 03           BEQ     $AC70               ; {}
AC6D: 20 E5 A9        JSR     $A9E5               ; {}
AC70: 60              RTS                         ; 
AC71: 20 86 79        JSR     $7986               ; {ram.7986}
AC74: 20 89 FA        JSR     $FA89               ; 
AC77: BD E4 03        LDA     $03E4,X             ; {ram.03E4}
AC7A: 4C DF 77        JMP     $77DF               ; {ram.77DF}
AC7D: AD 45 04        LDA     $0445               ; {ram.0445}
AC80: 20 E2 E5        JSR     $E5E2               ; 
AC83: 89                              ;
AC84: AC C6 AC        LDY     $ACC6               ; {}
AC87: E4 AC           CPX     <$AC                ; {ram.00AC}
AC89: A9 1B           LDA     #$1B                ; 
AC8B: 8D 05 05        STA     $0505               ; {ram.0505}
AC8E: A5 28           LDA     <$28                ; {ram.0028}
AC90: D0 2A           BNE     $ACBC               ; {}
AC92: 8A              TXA                         ; 
AC93: 48              PHA                         ; 
AC94: 20 BE B1        JSR     $B1BE               ; {}
AC97: 68              PLA                         ; 
AC98: AA              TAX                         ; 
AC99: A9 00           LDA     #$00                ; 
AC9B: 8D 1E 05        STA     $051E               ; {ram.051E}
AC9E: AD 1C 05        LDA     $051C               ; {ram.051C}
ACA1: C9 C0           CMP     #$C0                ; 
ACA3: D0 05           BNE     $ACAA               ; {}
ACA5: A9 02           LDA     #$02                ; 
ACA7: 8D 00 06        STA     $0600               ; {ram.SND_ReqMusic}
ACAA: AD 1C 05        LDA     $051C               ; {ram.051C}
ACAD: 29 0F           AND     #$0F                ; 
ACAF: C9 04           CMP     #$04                ; 
ACB1: D0 29           BNE     $ACDC               ; {}
ACB3: A9 C0           LDA     #$C0                ; 
ACB5: 85 28           STA     <$28                ; {ram.0028}
ACB7: EE 45 04        INC     $0445               ; {ram.0445}
ACBA: D0 20           BNE     $ACDC               ; {}
ACBC: C9 01           CMP     #$01                ; 
ACBE: D0 05           BNE     $ACC5               ; {}
ACC0: A9 02           LDA     #$02                ; 
ACC2: 8D 01 06        STA     $0601               ; {ram.??SND_601??}
ACC5: 60              RTS                         ; 
ACC6: A9 1B           LDA     #$1B                ; 
ACC8: 8D 05 05        STA     $0505               ; {ram.0505}
ACCB: A5 28           LDA     <$28                ; {ram.0028}
ACCD: D0 0D           BNE     $ACDC               ; {}
ACCF: 85 AC           STA     <$AC                ; {ram.00AC}
ACD1: 8D 05 05        STA     $0505               ; {ram.0505}
ACD4: A9 20           LDA     #$20                ; 
ACD6: 8D 00 06        STA     $0600               ; {ram.SND_ReqMusic}
ACD9: EE 45 04        INC     $0445               ; {ram.0445}
ACDC: A9 00           LDA     #$00                ; 
ACDE: 9D 6B 04        STA     $046B,X             ; 
ACE1: 4C B5 AE        JMP     $AEB5               ; {}
ACE4: BD 2C 04        LDA     $042C,X             ; {ram.!SplashMode}
ACE7: D0 64           BNE     $AD4D               ; {}
ACE9: 20 E4 AE        JSR     $AEE4               ; {}
ACEC: 20 00 80        JSR     $8000               ; {}
ACEF: B5 AC           LDA     $AC,X               ; {ram.00AC}
ACF1: D0 3C           BNE     $AD2F               ; {}
ACF3: B5 28           LDA     $28,X               ; {ram.0028}
ACF5: F0 13           BEQ     $AD0A               ; {}
ACF7: C9 01           CMP     #$01                ; 
ACF9: D0 4E           BNE     $AD49               ; {}
ACFB: A9 A0           LDA     #$A0                ; 
ACFD: 95 84           STA     $84,X               ; {ram.0084}
ACFF: A5 15           LDA     <$15                ; {ram.0015}
AD01: 29 01           AND     #$01                ; 
AD03: A8              TAY                         ; 
AD04: B9 2D AD        LDA     $AD2D,Y             ; {}
AD07: 95 70           STA     $70,X               ; {ram.0070}
AD09: 60              RTS                         ; 
AD0A: FE 6B 04        INC     $046B,X             ; 
AD0D: BD 6B 04        LDA     $046B,X             ; 
AD10: C9 06           CMP     #$06                ; 
AD12: D0 05           BNE     $AD19               ; {}
AD14: A9 00           LDA     #$00                ; 
AD16: 9D 6B 04        STA     $046B,X             ; 
AD19: A9 01           LDA     #$01                ; 
AD1B: 9D 94 03        STA     $0394,X             ; {ram.0394}
AD1E: 20 1D 9E        JSR     $9E1D               ; {}
AD21: A5 15           LDA     <$15                ; {ram.0015}
AD23: 29 3F           AND     #$3F                ; 
AD25: D0 05           BNE     $AD2C               ; {}
AD27: A9 56           LDA     #$56                ; 
AD29: 20 AF 82        JSR     $82AF               ; {}
AD2C: 60              RTS                         ; 
AD2D: 30 B0           BMI     $ACDF               ; {}
AD2F: A5 15           LDA     <$15                ; {ram.0015}
AD31: 4A              LSR     A                   ; 
AD32: 90 0A           BCC     $AD3E               ; {}
AD34: D6 AC           DEC     $AC,X               ; {ram.00AC}
AD36: D0 06           BNE     $AD3E               ; {}
AD38: 20 FB AC        JSR     $ACFB               ; {}
AD3B: 4C 71 AF        JMP     $AF71               ; {}
AD3E: B5 AC           LDA     $AC,X               ; {ram.00AC}
AD40: C9 30           CMP     #$30                ; 
AD42: B0 05           BCS     $AD49               ; {}
AD44: A5 15           LDA     <$15                ; {ram.0015}
AD46: 4A              LSR     A                   ; 
AD47: 90 03           BCC     $AD4C               ; {}
AD49: 20 B5 AE        JSR     $AEB5               ; {}
AD4C: 60              RTS                         ; 
AD4D: FE 2C 04        INC     $042C,X             ; {ram.!SplashMode}
AD50: BD 2C 04        LDA     $042C,X             ; {ram.!SplashMode}
AD53: D0 05           BNE     $AD5A               ; {}
AD55: A9 FF           LDA     #$FF                ; 
AD57: 9D 2C 04        STA     $042C,X             ; {ram.!SplashMode}
AD5A: C9 50           CMP     #$50                ; 
AD5C: 90 EB           BCC     $AD49               ; {}
AD5E: D0 1A           BNE     $AD7A               ; {}
AD60: 20 75 AF        JSR     $AF75               ; {}
AD63: B5 70           LDA     $70,X               ; {ram.0070}
AD65: 69 07           ADC     #$07                ; 
AD67: 95 70           STA     $70,X               ; {ram.0070}
AD69: B5 84           LDA     $84,X               ; {ram.0084}
AD6B: 69 08           ADC     #$08                ; 
AD6D: 95 84           STA     $84,X               ; {ram.0084}
AD6F: 20 B1 AD        JSR     $ADB1               ; {}
AD72: 20 10 B0        JSR     $B010               ; {}
AD75: A9 02           LDA     #$02                ; 
AD77: 8D 00 06        STA     $0600               ; {ram.SND_ReqMusic}
AD7A: 20 9F AF        JSR     $AF9F               ; {}
AD7D: BD 2C 04        LDA     $042C,X             ; {ram.!SplashMode}
AD80: C9 A0           CMP     #$A0                ; 
AD82: 90 67           BCC     $ADEB               ; {}
AD84: D0 0E           BNE     $AD94               ; {}
AD86: 20 A7 AF        JSR     $AFA7               ; {}
AD89: B5 70           LDA     $70,X               ; {ram.0070}
AD8B: 85 83           STA     <$83                ; {ram.0083}
AD8D: B5 84           LDA     $84,X               ; {ram.0084}
AD8F: 85 97           STA     <$97                ; {ram.0097}
AD91: EE 4F 03        INC     $034F               ; {ram.034F}
AD94: 60              RTS                         ; 
AD95: 01 02           ORA     ($02,X)             ; {ram.GP_02}
AD97: 04                              ;
AD98: 05 06           ORA     <$06                ; {ram.0006}
AD9A: 08              PHP                         ; 
AD9B: 09 0A           ORA     #$0A                ; 
AD9D: 00              BRK                         ; 
AD9E: 00              BRK                         ; 
AD9F: 40              RTI                         ; 
ADA0: 00              BRK                         ; 
ADA1: 80                              ;
ADA2: C0 80           CPY     #$80                ; 
ADA4: 00              BRK                         ; 
ADA5: 40              RTI                         ; 
ADA6: 00              BRK                         ; 
ADA7: 00              BRK                         ; 
ADA8: 00              BRK                         ; 
ADA9: EE EE E8        INC     $E8EE               ; 
ADAC: 30 30           BMI     $ADDE               ; {}
ADAE: E8              INX                         ; 
ADAF: 30 30           BMI     $ADE1               ; {}
ADB1: A0 07           LDY     #$07                ; 
ADB3: B5 70           LDA     $70,X               ; {ram.0070}
ADB5: 18              CLC                         ; 
ADB6: 69 04           ADC     #$04                ; 
ADB8: 99 72 00        STA     $0072,Y             ; {ram.0072}
ADBB: B5 84           LDA     $84,X               ; {ram.0084}
ADBD: 69 04           ADC     #$04                ; 
ADBF: 99 86 00        STA     $0086,Y             ; {ram.0086}
ADC2: B9 95 AD        LDA     $AD95,Y             ; {}
ADC5: 99 9A 00        STA     $009A,Y             ; {ram.009A}
ADC8: 88              DEY                         ; 
ADC9: 10 E8           BPL     $ADB3               ; {}
ADCB: 60              RTS                         ; 
ADCC: A5 00           LDA     <$00                ; {ram.GP_00}
ADCE: 48              PHA                         ; 
ADCF: A5 01           LDA     <$01                ; {ram.GP_01}
ADD1: 48              PHA                         ; 
ADD2: A9 0C           LDA     #$0C                ; 
ADD4: BC 78 04        LDY     $0478,X             ; 
ADD7: C0 06           CPY     #$06                ; 
ADD9: B0 02           BCS     $ADDD               ; {}
ADDB: A9 0D           LDA     #$0D                ; 
ADDD: A0 00           LDY     #$00                ; 
ADDF: 84 0F           STY     <$0F                ; {ram.000F}
ADE1: 20 DB 77        JSR     $77DB               ; {ram.77DB}
ADE4: 68              PLA                         ; 
ADE5: 85 01           STA     <$01                ; {ram.GP_01}
ADE7: 68              PLA                         ; 
ADE8: 85 00           STA     <$00                ; {ram.GP_00}
ADEA: 60              RTS                         ; 
ADEB: BD 78 04        LDA     $0478,X             ; 
ADEE: F0 09           BEQ     $ADF9               ; {}
ADF0: A5 15           LDA     <$15                ; {ram.0015}
ADF2: 29 07           AND     #$07                ; 
ADF4: D0 03           BNE     $ADF9               ; {}
ADF6: DE 78 04        DEC     $0478,X             ; 
ADF9: 20 6D AE        JSR     $AE6D               ; {}
ADFC: 20 7F AE        JSR     $AE7F               ; {}
ADFF: 20 CC AD        JSR     $ADCC               ; {}
AE02: 20 76 AE        JSR     $AE76               ; {}
AE05: 20 CC AD        JSR     $ADCC               ; {}
AE08: 20 6D AE        JSR     $AE6D               ; {}
AE0B: 20 88 AE        JSR     $AE88               ; {}
AE0E: 20 CC AD        JSR     $ADCC               ; {}
AE11: 20 76 AE        JSR     $AE76               ; {}
AE14: 20 CC AD        JSR     $ADCC               ; {}
AE17: B5 70           LDA     $70,X               ; {ram.0070}
AE19: 85 00           STA     <$00                ; {ram.GP_00}
AE1B: 20 7F AE        JSR     $AE7F               ; {}
AE1E: 20 CC AD        JSR     $ADCC               ; {}
AE21: 20 88 AE        JSR     $AE88               ; {}
AE24: 20 CC AD        JSR     $ADCC               ; {}
AE27: 20 6D AE        JSR     $AE6D               ; {}
AE2A: B5 84           LDA     $84,X               ; {ram.0084}
AE2C: 85 01           STA     <$01                ; {ram.GP_01}
AE2E: 20 CC AD        JSR     $ADCC               ; {}
AE31: 20 76 AE        JSR     $AE76               ; {}
AE34: 20 CC AD        JSR     $ADCC               ; {}
AE37: AD 40 03        LDA     $0340               ; {ram.0340}
AE3A: 48              PHA                         ; 
AE3B: A2 02           LDX     #$02                ; 
AE3D: 8E 40 03        STX     $0340               ; {ram.0340}
AE40: E0 05           CPX     #$05                ; 
AE42: 90 0A           BCC     $AE4E               ; {}
AE44: E0 07           CPX     #$07                ; 
AE46: F0 06           BEQ     $AE4E               ; {}
AE48: A5 15           LDA     <$15                ; {ram.0015}
AE4A: 29 03           AND     #$03                ; 
AE4C: F0 03           BEQ     $AE51               ; {}
AE4E: 20 9D 9E        JSR     $9E9D               ; {}
AE51: 20 93 FA        JSR     $FA93               ; 
AE54: A5 15           LDA     <$15                ; {ram.0015}
AE56: 29 03           AND     #$03                ; 
AE58: 1D 9D AD        ORA     $AD9D,X             ; {}
AE5B: 85 03           STA     <$03                ; {ram.GP_03}
AE5D: BD A7 AD        LDA     $ADA7,X             ; {}
AE60: 20 91 79        JSR     $7991               ; {ram.7991}
AE63: E8              INX                         ; 
AE64: E0 0A           CPX     #$0A                ; 
AE66: 90 D5           BCC     $AE3D               ; {}
AE68: 68              PLA                         ; 
AE69: 8D 40 03        STA     $0340               ; {ram.0340}
AE6C: 60              RTS                         ; 
AE6D: B5 70           LDA     $70,X               ; {ram.0070}
AE6F: 38              SEC                         ; 
AE70: FD 78 04        SBC     $0478,X             ; 
AE73: 85 00           STA     <$00                ; {ram.GP_00}
AE75: 60              RTS                         ; 
AE76: B5 70           LDA     $70,X               ; {ram.0070}
AE78: 18              CLC                         ; 
AE79: 7D 78 04        ADC     $0478,X             ; 
AE7C: 85 00           STA     <$00                ; {ram.GP_00}
AE7E: 60              RTS                         ; 
AE7F: B5 84           LDA     $84,X               ; {ram.0084}
AE81: 38              SEC                         ; 
AE82: FD 78 04        SBC     $0478,X             ; 
AE85: 85 01           STA     <$01                ; {ram.GP_01}
AE87: 60              RTS                         ; 
AE88: B5 84           LDA     $84,X               ; {ram.0084}
AE8A: 18              CLC                         ; 
AE8B: 7D 78 04        ADC     $0478,X             ; 
AE8E: 85 01           STA     <$01                ; {ram.GP_01}
AE90: 60              RTS                         ; 
AE91: 06 08           ASL     <$08                ; {ram.0008}
AE93: 07                              ;
AE94: 09 00           ORA     #$00                ; 
AE96: 00              BRK                         ; 
AE97: 01 01           ORA     ($01,X)             ; {ram.GP_01}
AE99: 02                              ;
AE9A: 02                              ;
AE9B: 03                              ;
AE9C: 03                              ;
AE9D: 04                              ;
AE9E: 00              BRK                         ; 
AE9F: 05 01           ORA     <$01                ; {ram.GP_01}
AEA1: 04                              ;
AEA2: 04                              ;
AEA3: 05 05           ORA     <$05                ; {ram.0005}
AEA5: 00              BRK                         ; 
AEA6: 04                              ;
AEA7: 01 05           ORA     ($05,X)             ; {ram.0005}
AEA9: 00              BRK                         ; 
AEAA: 10 00           BPL     $AEAC               ; {}
AEAC: 10 00           BPL     $AEAE               ; {}
AEAE: 00              BRK                         ; 
AEAF: 10 10           BPL     $AEC1               ; {}
AEB1: 00              BRK                         ; 
AEB2: 01 00           ORA     ($00,X)             ; {ram.GP_00}
AEB4: 01 A0           ORA     ($A0,X)             ; {ram.00A0}
AEB6: 03                              ;
AEB7: B5 70           LDA     $70,X               ; {ram.0070}
AEB9: 18              CLC                         ; 
AEBA: 79 A9 AE        ADC     $AEA9,Y             ; {}
AEBD: 85 00           STA     <$00                ; {ram.GP_00}
AEBF: B5 84           LDA     $84,X               ; {ram.0084}
AEC1: 18              CLC                         ; 
AEC2: 79 AD AE        ADC     $AEAD,Y             ; {}
AEC5: 85 01           STA     <$01                ; {ram.GP_01}
AEC7: B9 B1 AE        LDA     $AEB1,Y             ; {}
AECA: 85 0F           STA     <$0F                ; {ram.000F}
AECC: 98              TYA                         ; 
AECD: 48              PHA                         ; 
AECE: 85 07           STA     <$07                ; {ram.0007}
AED0: BD 6B 04        LDA     $046B,X             ; 
AED3: 0A              ASL     A                   ; 
AED4: 0A              ASL     A                   ; 
AED5: 65 07           ADC     <$07                ; {ram.0007}
AED7: A8              TAY                         ; 
AED8: B9 91 AE        LDA     $AE91,Y             ; {}
AEDB: 20 DF 77        JSR     $77DF               ; {ram.77DF}
AEDE: 68              PLA                         ; 
AEDF: A8              TAY                         ; 
AEE0: 88              DEY                         ; 
AEE1: 10 D4           BPL     $AEB7               ; {}
AEE3: 60              RTS                         ; 
AEE4: B5 70           LDA     $70,X               ; {ram.0070}
AEE6: 18              CLC                         ; 
AEE7: 69 10           ADC     #$10                ; 
AEE9: 85 02           STA     <$02                ; {ram.GP_02}
AEEB: B5 84           LDA     $84,X               ; {ram.0084}
AEED: 18              CLC                         ; 
AEEE: 69 10           ADC     #$10                ; 
AEF0: 85 03           STA     <$03                ; {ram.GP_03}
AEF2: AD F0 04        LDA     $04F0               ; {ram.04F0}
AEF5: D0 0D           BNE     $AF04               ; {}
AEF7: 85 06           STA     <$06                ; {ram.0006}
AEF9: 85 09           STA     <$09                ; {ram.0009}
AEFB: 85 0C           STA     <$0C                ; {ram.000C}
AEFD: A0 00           LDY     #$00                ; 
AEFF: 84 00           STY     <$00                ; {ram.GP_00}
AF01: 20 C5 7A        JSR     $7AC5               ; {ram.7AC5}
AF04: B5 AC           LDA     $AC,X               ; {ram.00AC}
AF06: D0 2B           BNE     $AF33               ; {}
AF08: B5 28           LDA     $28,X               ; {ram.0028}
AF0A: D0 26           BNE     $AF32               ; {}
AF0C: A0 0D           LDY     #$0D                ; 
AF0E: 20 29 7D        JSR     $7D29               ; {ram.7D29}
AF11: BD 05 04        LDA     $0405,X             ; {ram.0405}
AF14: F0 0A           BEQ     $AF20               ; {}
AF16: A9 F0           LDA     #$F0                ; 
AF18: 9D 85 04        STA     $0485,X             ; 
AF1B: D6 AC           DEC     $AC,X               ; {ram.00AC}
AF1D: 20 6D AF        JSR     $AF6D               ; {}
AF20: BD F0 04        LDA     $04F0,X             ; {ram.04F0}
AF23: F0 07           BEQ     $AF2C               ; {}
AF25: 20 00 80        JSR     $8000               ; {}
AF28: A9 40           LDA     #$40                ; 
AF2A: 95 28           STA     $28,X               ; {ram.0028}
AF2C: 20 DA FE        JSR     $FEDA               ; 
AF2F: 20 96 7C        JSR     $7C96               ; {ram.7C96}
AF32: 60              RTS                         ; 
AF33: AD 59 06        LDA     $0659               ; {ram.0659}
AF36: C9 02           CMP     #$02                ; 
AF38: D0 F8           BNE     $AF32               ; {}
AF3A: A9 00           LDA     #$00                ; 
AF3C: 85 06           STA     <$06                ; {ram.0006}
AF3E: A0 12           LDY     #$12                ; 
AF40: B9 AC 00        LDA     $00AC,Y             ; {ram.00AC}
AF43: C9 10           CMP     #$10                ; 
AF45: D0 EB           BNE     $AF32               ; {}
AF47: 20 5F 7D        JSR     $7D5F               ; {ram.7D5F}
AF4A: A5 06           LDA     <$06                ; {ram.0006}
AF4C: F0 E4           BEQ     $AF32               ; {}
AF4E: FE 2C 04        INC     $042C,X             ; {ram.!SplashMode}
AF51: A9 28           LDA     #$28                ; 
AF53: 9D F0 04        STA     $04F0,X             ; {ram.04F0}
AF56: A9 08           LDA     #$08                ; 
AF58: 9D 78 04        STA     $0478,X             ; 
AF5B: 60              RTS                         ; 
AF5C: 3F                              ;
AF5D: 1C                              ;
AF5E: 04                              ;
AF5F: 0F                              ;
AF60: 07                              ;
AF61: 17                              ;
AF62: 27                              ;
AF63: FF                              ;
AF64: 07                              ;
AF65: 17                              ;
AF66: 30 16           BMI     $AF7E               ; {}
AF68: 2C 3C 27        BIT     $273C               ; 
AF6B: 06 16           ASL     <$16                ; {ram.0016}
AF6D: A0 02           LDY     #$02                ; 
AF6F: D0 06           BNE     $AF77               ; {}
AF71: A0 05           LDY     #$05                ; 
AF73: D0 02           BNE     $AF77               ; {}
AF75: A0 08           LDY     #$08                ; 
AF77: 98              TYA                         ; 
AF78: 48              PHA                         ; 
AF79: AE 01 03        LDX     $0301               ; {ram.0301}
AF7C: A0 00           LDY     #$00                ; 
AF7E: B9 5C AF        LDA     $AF5C,Y             ; {}
AF81: 9D 02 03        STA     $0302,X             ; {ram.0302}
AF84: E8              INX                         ; 
AF85: C8              INY                         ; 
AF86: C0 08           CPY     #$08                ; 
AF88: D0 F4           BNE     $AF7E               ; {}
AF8A: 8E 01 03        STX     $0301               ; {ram.0301}
AF8D: 68              PLA                         ; 
AF8E: A8              TAY                         ; 
AF8F: A2 02           LDX     #$02                ; 
AF91: B9 64 AF        LDA     $AF64,Y             ; {}
AF94: 9D 06 03        STA     $0306,X             ; {ram.0306}
AF97: 88              DEY                         ; 
AF98: CA              DEX                         ; 
AF99: 10 F6           BPL     $AF91               ; {}
AF9B: AE 40 03        LDX     $0340               ; {ram.0340}
AF9E: 60              RTS                         ; 
AF9F: 20 93 FA        JSR     $FA93               ; 
AFA2: A9 0B           LDA     #$0B                ; 
AFA4: 4C DF 77        JMP     $77DF               ; {ram.77DF}
AFA7: A5 BF           LDA     <$BF                ; {ram.00BF}
AFA9: F0 0E           BEQ     $AFB9               ; {}
AFAB: 20 14 73        JSR     $7314               ; {ram.7314}
AFAE: D0 09           BNE     $AFB9               ; {}
AFB0: A9 00           LDA     #$00                ; 
AFB2: 85 BF           STA     <$BF                ; {ram.00BF}
AFB4: A9 02           LDA     #$02                ; 
AFB6: 8D 02 06        STA     $0602               ; {ram.SND_ReqMusEff}
AFB9: 60              RTS                         ; 
AFBA: FF                              ;
AFBB: FF                              ;
AFBC: FF                              ;
AFBD: FF                              ;
AFBE: FF                              ;
AFBF: FF                              ;
AFC0: FF                              ;
AFC1: FF                              ;
AFC2: FF                              ;
AFC3: FF                              ;
AFC4: FF                              ;
AFC5: FF                              ;
AFC6: FF                              ;
AFC7: FF                              ;
AFC8: FF                              ;
AFC9: FF                              ;
AFCA: FF                              ;
AFCB: FF                              ;
AFCC: FF                              ;
AFCD: FF                              ;
AFCE: FF                              ;
AFCF: FF                              ;
AFD0: FF                              ;
AFD1: FF                              ;
AFD2: FF                              ;
AFD3: FF                              ;
AFD4: FF                              ;
AFD5: FF                              ;
AFD6: FF                              ;
AFD7: FF                              ;
AFD8: FF                              ;
AFD9: FF                              ;
AFDA: FF                              ;
AFDB: FF                              ;
AFDC: FF                              ;
AFDD: FF                              ;
AFDE: FF                              ;
AFDF: FF                              ;
AFE0: FF                              ;
AFE1: FF                              ;
AFE2: FF                              ;
AFE3: FF                              ;
AFE4: FF                              ;
AFE5: FF                              ;
AFE6: FF                              ;
AFE7: FF                              ;
AFE8: FF                              ;
AFE9: FF                              ;
AFEA: FF                              ;
AFEB: FF                              ;
AFEC: FF                              ;
AFED: FF                              ;
AFEE: FF                              ;
AFEF: FF                              ;
AFF0: FF                              ;
AFF1: FF                              ;
AFF2: FF                              ;
AFF3: FF                              ;
AFF4: FF                              ;
AFF5: FF                              ;
AFF6: FF                              ;
AFF7: FF                              ;
AFF8: FF                              ;
AFF9: FF                              ;
AFFA: FF                              ;
AFFB: FF                              ;
AFFC: FF                              ;
AFFD: FF                              ;
AFFE: FF                              ;
AFFF: FF                              ;
B000: 48              PHA                         ; 
B001: A5 00           LDA     <$00                ; {ram.GP_00}
B003: 4A              LSR     A                   ; 
B004: B0 04           BCS     $B00A               ; {}
B006: 68              PLA                         ; 
B007: 29 F0           AND     #$F0                ; 
B009: 60              RTS                         ; 
B00A: 68              PLA                         ; 
B00B: 0A              ASL     A                   ; 
B00C: 0A              ASL     A                   ; 
B00D: 0A              ASL     A                   ; 
B00E: 0A              ASL     A                   ; 
B00F: 60              RTS                         ; 
B010: A9 02           LDA     #$02                ; 
B012: 8D 01 06        STA     $0601               ; {ram.??SND_601??}
B015: A9 80           LDA     #$80                ; 
B017: 8D 03 06        STA     $0603               ; {ram.??SND_603??}
B01A: 60              RTS                         ; 
B01B: 5D 14 15        EOR     $1514,X             ; 
B01E: 1B                              ;
B01F: 1C                              ;
B020: 1D 17 07        ORA     $0717,X             ; 
B023: 08              PHP                         ; 
B024: 0E 04 0F        ASL     $0F04               ; 
B027: 23                              ;
B028: 21 22           AND     ($22,X)             ; {ram.0022}
B02A: 0D 10 13        ORA     $1310               ; 
B02D: 28              PLP                         ; 
B02E: 2A              ROL     A                   ; 
B02F: 27                              ;
B030: 16 09           ASL     $09,X               ; {ram.0009}
B032: 0A              ASL     A                   ; 
B033: 03                              ;
B034: 01 12           ORA     ($12,X)             ; {ram.0012}
B036: 06 0B           ASL     <$0B                ; {ram.000B}
B038: 24 30           BIT     <$30                ; {ram.0030}
B03A: 00              BRK                         ; 
B03B: 0A              ASL     A                   ; 
B03C: 14                              ;
B03D: 1E 50 98        ASL     $9850,X             ; {}
B040: 68              PLA                         ; 
B041: 68              PLA                         ; 
B042: 22                              ;
B043: 18              CLC                         ; 
B044: 22                              ;
B045: 18              CLC                         ; 
B046: 23                              ;
B047: 18              CLC                         ; 
B048: 22                              ;
B049: 22                              ;
B04A: 18              CLC                         ; 
B04B: 18              CLC                         ; 
B04C: 0F                              ;
B04D: 18              CLC                         ; 
B04E: 22                              ;
B04F: 18              CLC                         ; 
B050: 0F                              ;
B051: 22                              ;
B052: 21 18           AND     ($18,X)             ; {ram.0018}
B054: 18              CLC                         ; 
B055: 18              CLC                         ; 
B056: 22                              ;
B057: 00              BRK                         ; 
B058: 18              CLC                         ; 
B059: 21 18           AND     ($18,X)             ; {ram.0018}
B05B: 22                              ;
B05C: 00              BRK                         ; 
B05D: 18              CLC                         ; 
B05E: 00              BRK                         ; 
B05F: 22                              ;
B060: 22                              ;
B061: 22                              ;
B062: 23                              ;
B063: 18              CLC                         ; 
B064: 22                              ;
B065: 23                              ;
B066: 22                              ;
B067: 22                              ;
B068: 22                              ;
B069: 18              CLC                         ; 
B06A: A9 00           LDA     #$00                ; 
B06C: 85 01           STA     <$01                ; {ram.GP_01}
B06E: BD 12 04        LDA     $0412,X             ; {ram.0412}
B071: A0 06           LDY     #$06                ; 
B073: D9 1B B0        CMP     $B01B,Y             ; {}
B076: F0 7D           BEQ     $B0F5               ; {}
B078: 88              DEY                         ; 
B079: 10 F8           BPL     $B073               ; {}
B07B: A0 05           LDY     #$05                ; 
B07D: D9 22 B0        CMP     $B022,Y             ; {}
B080: F0 1D           BEQ     $B09F               ; {}
B082: 88              DEY                         ; 
B083: 10 F8           BPL     $B07D               ; {}
B085: E6 01           INC     <$01                ; {ram.GP_01}
B087: A0 08           LDY     #$08                ; 
B089: D9 28 B0        CMP     $B028,Y             ; {}
B08C: F0 11           BEQ     $B09F               ; {}
B08E: 88              DEY                         ; 
B08F: 10 F8           BPL     $B089               ; {}
B091: E6 01           INC     <$01                ; {ram.GP_01}
B093: A0 08           LDY     #$08                ; 
B095: D9 31 B0        CMP     $B031,Y             ; {}
B098: F0 05           BEQ     $B09F               ; {}
B09A: 88              DEY                         ; 
B09B: 10 F8           BPL     $B095               ; {}
B09D: E6 01           INC     <$01                ; {ram.GP_01}
B09F: E0 01           CPX     #$01                ; 
B0A1: D0 08           BNE     $B0AB               ; {}
B0A3: C9 2A           CMP     #$2A                ; 
B0A5: F0 4E           BEQ     $B0F5               ; {}
B0A7: C9 30           CMP     #$30                ; 
B0A9: F0 4A           BEQ     $B0F5               ; {}
B0AB: A4 01           LDY     <$01                ; {ram.GP_01}
B0AD: B9 3A B0        LDA     $B03A,Y             ; {}
B0B0: 18              CLC                         ; 
B0B1: 6D 2A 05        ADC     $052A               ; {ram.052A}
B0B4: A8              TAY                         ; 
B0B5: B9 42 B0        LDA     $B042,Y             ; {}
B0B8: 85 00           STA     <$00                ; {ram.GP_00}
B0BA: A9 23           LDA     #$23                ; 
B0BC: AC 27 06        LDY     $0627               ; {ram.0627}
B0BF: C0 10           CPY     #$10                ; 
B0C1: F0 0E           BEQ     $B0D1               ; {}
B0C3: A5 50           LDA     <$50                ; {ram.0050}
B0C5: C9 0A           CMP     #$0A                ; 
B0C7: 90 12           BCC     $B0DB               ; {}
B0C9: A9 0F           LDA     #$0F                ; 
B0CB: A4 51           LDY     <$51                ; {ram.0051}
B0CD: F0 02           BEQ     $B0D1               ; {}
B0CF: A9 00           LDA     #$00                ; 
B0D1: 85 00           STA     <$00                ; {ram.GP_00}
B0D3: A9 00           LDA     #$00                ; 
B0D5: 85 50           STA     <$50                ; {ram.0050}
B0D7: 85 51           STA     <$51                ; {ram.0051}
B0D9: F0 09           BEQ     $B0E4               ; {}
B0DB: A4 01           LDY     <$01                ; {ram.GP_01}
B0DD: B5 18           LDA     $18,X               ; {ram.0018}
B0DF: D9 3E B0        CMP     $B03E,Y             ; {}
B0E2: B0 11           BCS     $B0F5               ; {}
B0E4: A9 FF           LDA     #$FF                ; 
B0E6: 9D A8 03        STA     $03A8,X             ; {ram.03A8}
B0E9: A5 00           LDA     <$00                ; {ram.GP_00}
B0EB: 95 AC           STA     $AC,X               ; {ram.00AC}
B0ED: C9 23           CMP     #$23                ; 
B0EF: D0 03           BNE     $B0F4               ; {}
B0F1: 4C F4 B1        JMP     $B1F4               ; {}
B0F4: 60              RTS                         ; 
B0F5: 4C 5F B1        JMP     $B15F               ; {}
B0F8: 00              BRK                         ; 
B0F9: 0F                              ;
B0FA: 0D 12 A5        ORA     $A512               ; {}
B0FD: 15 4A           ORA     $4A,X               ; {ram.004A}
B0FF: 90 03           BCC     $B104               ; {}
B101: DE A8 03        DEC     $03A8,X             ; {ram.03A8}
B104: BD A8 03        LDA     $03A8,X             ; {ram.03A8}
B107: F0 56           BEQ     $B15F               ; {}
B109: B5 AC           LDA     $AC,X               ; {ram.00AC}
B10B: C9 23           CMP     #$23                ; 
B10D: F0 06           BEQ     $B115               ; {}
B10F: 20 0E E7        JSR     $E70E               ; 
B112: 4C 18 B1        JMP     $B118               ; {}
B115: 20 1D B2        JSR     $B21D               ; {}
B118: A5 AC           LDA     <$AC                ; {ram.00AC}
B11A: 29 C0           AND     #$C0                ; 
B11C: C9 40           CMP     #$40                ; 
B11E: F0 3E           BEQ     $B15E               ; {}
B120: A9 04           LDA     #$04                ; 
B122: 85 0D           STA     <$0D                ; {ram.000D}
B124: A5 70           LDA     <$70                ; {ram.0070}
B126: 48              PHA                         ; 
B127: A5 84           LDA     <$84                ; {ram.0084}
B129: 48              PHA                         ; 
B12A: A4 0D           LDY     <$0D                ; {ram.000D}
B12C: BE F7 B0        LDX     $B0F7,Y             ; {}
B12F: B5 70           LDA     $70,X               ; {ram.0070}
B131: 85 70           STA     <$70                ; {ram.0070}
B133: B5 84           LDA     $84,X               ; {ram.0084}
B135: 85 84           STA     <$84                ; {ram.0084}
B137: E0 00           CPX     #$00                ; 
B139: F0 06           BEQ     $B141               ; {}
B13B: B5 AC           LDA     $AC,X               ; {ram.00AC}
B13D: F0 0C           BEQ     $B14B               ; {}
B13F: 30 0A           BMI     $B14B               ; {}
B141: AE 40 03        LDX     $0340               ; {ram.0340}
B144: B5 AC           LDA     $AC,X               ; {ram.00AC}
B146: 85 04           STA     <$04                ; {ram.0004}
B148: 20 3F 73        JSR     $733F               ; {ram.733F}
B14B: 68              PLA                         ; 
B14C: 85 84           STA     <$84                ; {ram.0084}
B14E: 68              PLA                         ; 
B14F: 85 70           STA     <$70                ; {ram.0070}
B151: AE 40 03        LDX     $0340               ; {ram.0340}
B154: B5 AC           LDA     $AC,X               ; {ram.00AC}
B156: C9 FF           CMP     #$FF                ; 
B158: F0 05           BEQ     $B15F               ; {}
B15A: C6 0D           DEC     <$0D                ; {ram.000D}
B15C: D0 C6           BNE     $B124               ; {}
B15E: 60              RTS                         ; 
B15F: A9 00           LDA     #$00                ; 
B161: 9D 4F 03        STA     $034F,X             ; {ram.034F}
B164: 20 E6 EE        JSR     $EEE6               ; 
B167: 95 28           STA     $28,X               ; {ram.0028}
B169: 95 AC           STA     $AC,X               ; {ram.00AC}
B16B: 9D F0 04        STA     $04F0,X             ; {ram.04F0}
B16E: A9 FF           LDA     #$FF                ; 
B170: 9D 92 04        STA     $0492,X             ; 
B173: A9 01           LDA     #$01                ; 
B175: 9D 05 04        STA     $0405,X             ; {ram.0405}
B178: 60              RTS                         ; 
B179: 85 00           STA     <$00                ; {ram.GP_00}
B17B: BD 12 04        LDA     $0412,X             ; {ram.0412}
B17E: F0 3C           BEQ     $B1BC               ; {}
B180: 20 BB FE        JSR     $FEBB               ; 
B183: F0 37           BEQ     $B1BC               ; {}
B185: A5 00           LDA     <$00                ; {ram.GP_00}
B187: C9 53           CMP     #$53                ; 
B189: 90 0A           BCC     $B195               ; {}
B18B: AD 4C 03        LDA     $034C               ; {ram.034C}
B18E: C9 04           CMP     #$04                ; 
B190: B0 2A           BCS     $B1BC               ; {}
B192: EE 4C 03        INC     $034C               ; {ram.034C}
B195: A6 59           LDX     <$59                ; {ram.0059}
B197: A5 00           LDA     <$00                ; {ram.GP_00}
B199: 20 B3 FE        JSR     $FEB3               ; 
B19C: A4 59           LDY     <$59                ; {ram.0059}
B19E: AE 40 03        LDX     $0340               ; {ram.0340}
B1A1: A9 10           LDA     #$10                ; 
B1A3: 99 AC 00        STA     $00AC,Y             ; {ram.00AC}
B1A6: A9 00           LDA     #$00                ; 
B1A8: 99 28 00        STA     $0028,Y             ; {ram.0028}
B1AB: B5 98           LDA     $98,X               ; {ram.0098}
B1AD: 99 98 00        STA     $0098,Y             ; {ram.0098}
B1B0: B5 70           LDA     $70,X               ; {ram.0070}
B1B2: 99 70 00        STA     $0070,Y             ; {ram.0070}
B1B5: B5 84           LDA     $84,X               ; {ram.0084}
B1B7: 99 84 00        STA     $0084,Y             ; {ram.0084}
B1BA: 38              SEC                         ; 
B1BB: 60              RTS                         ; 
B1BC: 18              CLC                         ; 
B1BD: 60              RTS                         ; 
B1BE: AD 1F 05        LDA     $051F               ; {ram.051F}
B1C1: 20 E2 E5        JSR     $E5E2               ; 
B1C4: CA              DEX                         ; 
B1C5: B1 E4           LDA     ($E4),Y             ; {ram.00E4}
B1C7: B1 DC           LDA     ($DC),Y             ; 
B1C9: B1 A4           LDA     ($A4),Y             ; {ram.00A4}
B1CB: EB                              ;
B1CC: 20 EA B1        JSR     $B1EA               ; {}
B1CF: F0 0B           BEQ     $B1DC               ; {}
B1D1: A9 C0           LDA     #$C0                ; 
B1D3: 8D 1C 05        STA     $051C               ; {ram.051C}
B1D6: EE 1E 05        INC     $051E               ; {ram.051E}
B1D9: EE 1F 05        INC     $051F               ; {ram.051F}
B1DC: 60              RTS                         ; 
B1DD: A9 00           LDA     #$00                ; 
B1DF: 8D 1E 05        STA     $051E               ; {ram.051E}
B1E2: F0 F5           BEQ     $B1D9               ; {}
B1E4: 20 B7 74        JSR     $74B7               ; {ram.74B7}
B1E7: F0 F4           BEQ     $B1DD               ; {}
B1E9: 60              RTS                         ; 
B1EA: A5 10           LDA     <$10                ; {ram.0010}
B1EC: F0 05           BEQ     $B1F3               ; {}
B1EE: B9 7E 6A        LDA     $6A7E,Y             ; 
B1F1: 29 80           AND     #$80                ; 
B1F3: 60              RTS                         ; 
B1F4: A9 08           LDA     #$08                ; 
B1F6: 8D 02 06        STA     $0602               ; {ram.SND_ReqMusEff}
B1F9: 20 0B B2        JSR     $B20B               ; {}
B1FC: A9 08           LDA     #$08                ; 
B1FE: 95 98           STA     $98,X               ; {ram.0098}
B200: A9 7F           LDA     #$7F                ; 
B202: 9D 1F 04        STA     $041F,X             ; {ram.041F}
B205: A9 A0           LDA     #$A0                ; 
B207: 8D D1 04        STA     $04D1               ; {ram.04D1}
B20A: 60              RTS                         ; 
B20B: A9 00           LDA     #$00                ; 
B20D: 9D 12 04        STA     $0412,X             ; {ram.0412}
B210: 9D 2C 04        STA     $042C,X             ; {ram.!SplashMode}
B213: 9D 37 04        STA     $0437,X             ; {ram.0437}
B216: 9D 44 04        STA     $0444,X             ; 
B219: 9D F0 04        STA     $04F0,X             ; {ram.04F0}
B21C: 60              RTS                         ; 
B21D: 20 35 B2        JSR     $B235               ; {}
B220: 20 88 B2        JSR     $B288               ; {}
B223: 20 93 FA        JSR     $FA93               ; 
B226: 20 86 79        JSR     $7986               ; {ram.7986}
B229: 0A              ASL     A                   ; 
B22A: 25 15           AND     <$15                ; {ram.0015}
B22C: 4A              LSR     A                   ; 
B22D: 4A              LSR     A                   ; 
B22E: 85 0C           STA     <$0C                ; {ram.000C}
B230: A0 14           LDY     #$14                ; 
B232: 4C 15 79        JMP     $7915               ; {ram.7915}
B235: BD 44 04        LDA     $0444,X             ; 
B238: 20 E2 E5        JSR     $E5E2               ; 
B23B: 66 B2           ROR     <$B2                ; {ram.00B2}
B23D: 43                              ;
B23E: B2                              ;
B23F: 4D B2 78        EOR     $78B2               ; {ram.78B2}
B242: B3                              ;
B243: A9 03           LDA     #$03                ; 
B245: 9D 44 04        STA     $0444,X             ; 
B248: A9 06           LDA     #$06                ; 
B24A: 9D 2C 04        STA     $042C,X             ; {ram.!SplashMode}
B24D: 60              RTS                         ; 
B24E: 08              PHP                         ; 
B24F: 09 01           ORA     #$01                ; 
B251: 05 04           ORA     <$04                ; {ram.0004}
B253: 06 02           ASL     <$02                ; {ram.GP_02}
B255: 0A              ASL     A                   ; 
B256: B5 28           LDA     $28,X               ; {ram.0028}
B258: D0 05           BNE     $B25F               ; {}
B25A: A9 00           LDA     #$00                ; 
B25C: 9D 44 04        STA     $0444,X             ; 
B25F: 60              RTS                         ; 
B260: DE 1F 04        DEC     $041F,X             ; {ram.041F}
B263: 4C 69 B2        JMP     $B269               ; {}
B266: FE 1F 04        INC     $041F,X             ; {ram.041F}
B269: BD 1F 04        LDA     $041F,X             ; {ram.041F}
B26C: 29 E0           AND     #$E0                ; 
B26E: D0 0E           BNE     $B27E               ; {}
B270: B5 18           LDA     $18,X               ; {ram.0018}
B272: 29 3F           AND     #$3F                ; 
B274: 09 40           ORA     #$40                ; 
B276: 95 28           STA     $28,X               ; {ram.0028}
B278: A9 05           LDA     #$05                ; 
B27A: 9D 44 04        STA     $0444,X             ; 
B27D: 60              RTS                         ; 
B27E: CD D1 04        CMP     $04D1               ; {ram.04D1}
B281: 90 FA           BCC     $B27D               ; {}
B283: A9 01           LDA     #$01                ; 
B285: 4C 7A B2        JMP     $B27A               ; {}
B288: BD 1F 04        LDA     $041F,X             ; {ram.041F}
B28B: 29 E0           AND     #$E0                ; 
B28D: 18              CLC                         ; 
B28E: 7D 12 04        ADC     $0412,X             ; {ram.0412}
B291: 9D 12 04        STA     $0412,X             ; {ram.0412}
B294: 90 36           BCC     $B2CC               ; {}
B296: A9 01           LDA     #$01                ; 
B298: 85 02           STA     <$02                ; {ram.GP_02}
B29A: B5 98           LDA     $98,X               ; {ram.0098}
B29C: 24 02           BIT     <$02                ; {ram.GP_02}
B29E: F0 05           BEQ     $B2A5               ; {}
B2A0: F6 70           INC     $70,X               ; {ram.0070}
B2A2: FE 6B 04        INC     $046B,X             ; 
B2A5: 06 02           ASL     <$02                ; {ram.GP_02}
B2A7: 24 02           BIT     <$02                ; {ram.GP_02}
B2A9: F0 05           BEQ     $B2B0               ; {}
B2AB: D6 70           DEC     $70,X               ; {ram.0070}
B2AD: DE 6B 04        DEC     $046B,X             ; 
B2B0: 06 02           ASL     <$02                ; {ram.GP_02}
B2B2: 24 02           BIT     <$02                ; {ram.GP_02}
B2B4: F0 05           BEQ     $B2BB               ; {}
B2B6: F6 84           INC     $84,X               ; {ram.0084}
B2B8: FE 78 04        INC     $0478,X             ; 
B2BB: 06 02           ASL     <$02                ; {ram.GP_02}
B2BD: 24 02           BIT     <$02                ; {ram.GP_02}
B2BF: F0 05           BEQ     $B2C6               ; {}
B2C1: D6 84           DEC     $84,X               ; {ram.0084}
B2C3: DE 78 04        DEC     $0478,X             ; 
B2C6: FE 37 04        INC     $0437,X             ; {ram.0437}
B2C9: 20 CD B2        JSR     $B2CD               ; {}
B2CC: 60              RTS                         ; 
B2CD: B5 98           LDA     $98,X               ; {ram.0098}
B2CF: 85 0F           STA     <$0F                ; {ram.000F}
B2D1: 20 29 6F        JSR     $6F29               ; {ram.6F29}
B2D4: BD 4F 03        LDA     $034F,X             ; {ram.034F}
B2D7: C9 20           CMP     #$20                ; 
B2D9: F0 03           BEQ     $B2DE               ; {}
B2DB: 20 73 6F        JSR     $6F73               ; {ram.6F73}
B2DE: A5 0F           LDA     <$0F                ; {ram.000F}
B2E0: D0 16           BNE     $B2F8               ; {}
B2E2: 20 9F B3        JSR     $B39F               ; {}
B2E5: 98              TYA                         ; 
B2E6: 18              CLC                         ; 
B2E7: 69 04           ADC     #$04                ; 
B2E9: 29 07           AND     #$07                ; 
B2EB: A8              TAY                         ; 
B2EC: BD 4F 03        LDA     $034F,X             ; {ram.034F}
B2EF: C9 41           CMP     #$41                ; 
B2F1: F0 06           BEQ     $B2F9               ; {}
B2F3: B9 4E B2        LDA     $B24E,Y             ; {}
B2F6: 95 98           STA     $98,X               ; {ram.0098}
B2F8: 60              RTS                         ; 
B2F9: E0 05           CPX     #$05                ; 
B2FB: F0 04           BEQ     $B301               ; {}
B2FD: E0 0A           CPX     #$0A                ; 
B2FF: D0 06           BNE     $B307               ; {}
B301: B9 4E B2        LDA     $B24E,Y             ; {}
B304: 9D BC 03        STA     $03BC,X             ; {ram.03BC}
B307: 60              RTS                         ; 
B308: B5 28           LDA     $28,X               ; {ram.0028}
B30A: D0 FB           BNE     $B307               ; {}
B30C: DE 2C 04        DEC     $042C,X             ; {ram.!SplashMode}
B30F: D0 05           BNE     $B316               ; {}
B311: A9 01           LDA     #$01                ; 
B313: 4C 7A B2        JMP     $B27A               ; {}
B316: A9 10           LDA     #$10                ; 
B318: 95 28           STA     $28,X               ; {ram.0028}
B31A: A0 00           LDY     #$00                ; 
B31C: 84 00           STY     <$00                ; {ram.GP_00}
B31E: C8              INY                         ; 
B31F: A5 61           LDA     <$61                ; {ram.0061}
B321: D5 70           CMP     $70,X               ; {ram.0070}
B323: F0 05           BEQ     $B32A               ; {}
B325: B0 01           BCS     $B328               ; {}
B327: C8              INY                         ; 
B328: 84 00           STY     <$00                ; {ram.GP_00}
B32A: A0 01           LDY     #$01                ; 
B32C: A5 62           LDA     <$62                ; {ram.0062}
B32E: D5 84           CMP     $84,X               ; {ram.0084}
B330: F0 0A           BEQ     $B33C               ; {}
B332: B0 01           BCS     $B335               ; {}
B334: C8              INY                         ; 
B335: 98              TYA                         ; 
B336: 0A              ASL     A                   ; 
B337: 0A              ASL     A                   ; 
B338: 05 00           ORA     <$00                ; {ram.GP_00}
B33A: 85 00           STA     <$00                ; {ram.GP_00}
B33C: 20 9F B3        JSR     $B39F               ; {}
B33F: A9 03           LDA     #$03                ; 
B341: 85 01           STA     <$01                ; {ram.GP_01}
B343: C8              INY                         ; 
B344: 98              TYA                         ; 
B345: 29 07           AND     #$07                ; 
B347: A8              TAY                         ; 
B348: B9 4E B2        LDA     $B24E,Y             ; {}
B34B: C5 00           CMP     <$00                ; {ram.GP_00}
B34D: F0 20           BEQ     $B36F               ; {}
B34F: 88              DEY                         ; 
B350: C6 01           DEC     <$01                ; {ram.GP_01}
B352: D0 F0           BNE     $B344               ; {}
B354: A9 03           LDA     #$03                ; 
B356: 85 01           STA     <$01                ; {ram.GP_01}
B358: C8              INY                         ; 
B359: 98              TYA                         ; 
B35A: 29 07           AND     #$07                ; 
B35C: A8              TAY                         ; 
B35D: B9 4E B2        LDA     $B24E,Y             ; {}
B360: 24 00           BIT     <$00                ; {ram.GP_00}
B362: D0 0C           BNE     $B370               ; {}
B364: C8              INY                         ; 
B365: C6 01           DEC     <$01                ; {ram.GP_01}
B367: D0 F0           BNE     $B359               ; {}
B369: 88              DEY                         ; 
B36A: B9 4E B2        LDA     $B24E,Y             ; {}
B36D: 95 98           STA     $98,X               ; {ram.0098}
B36F: 60              RTS                         ; 
B370: 05 00           ORA     <$00                ; {ram.GP_00}
B372: C9 07           CMP     #$07                ; 
B374: B0 EE           BCS     $B364               ; {}
B376: 90 F2           BCC     $B36A               ; {}
B378: B5 28           LDA     $28,X               ; {ram.0028}
B37A: D0 30           BNE     $B3AC               ; {}
B37C: DE 2C 04        DEC     $042C,X             ; {ram.!SplashMode}
B37F: D0 03           BNE     $B384               ; {}
B381: 4C 11 B3        JMP     $B311               ; {}
B384: A9 10           LDA     #$10                ; 
B386: 95 28           STA     $28,X               ; {ram.0028}
B388: 20 9F B3        JSR     $B39F               ; {}
B38B: B5 19           LDA     $19,X               ; {ram.0019}
B38D: C9 A0           CMP     #$A0                ; 
B38F: B0 07           BCS     $B398               ; {}
B391: C8              INY                         ; 
B392: C9 50           CMP     #$50                ; 
B394: B0 02           BCS     $B398               ; {}
B396: 88              DEY                         ; 
B397: 88              DEY                         ; 
B398: 98              TYA                         ; 
B399: 29 07           AND     #$07                ; 
B39B: A8              TAY                         ; 
B39C: 4C 6A B3        JMP     $B36A               ; {}
B39F: A0 07           LDY     #$07                ; 
B3A1: B5 98           LDA     $98,X               ; {ram.0098}
B3A3: D9 4E B2        CMP     $B24E,Y             ; {}
B3A6: F0 04           BEQ     $B3AC               ; {}
B3A8: 88              DEY                         ; 
B3A9: 10 F6           BPL     $B3A1               ; {}
B3AB: C8              INY                         ; 
B3AC: 60              RTS                         ; 
B3AD: 00              BRK                         ; 
B3AE: 18              CLC                         ; 
B3AF: 30 47           BMI     $B3F8               ; {}
B3B1: 5A                              ;
B3B2: 6A              ROR     A                   ; 
B3B3: 76 7D           ROR     <$7D,X              ; {ram.007D}
B3B5: 80                              ;
B3B6: 7D 76 6A        ADC     $6A76,X             ; 
B3B9: 5A                              ;
B3BA: 47                              ;
B3BB: 30 18           BMI     $B3D5               ; {}
B3BD: 85 06           STA     <$06                ; {ram.0006}
B3BF: 84 05           STY     <$05                ; {ram.0005}
B3C1: BD 94 03        LDA     $0394,X             ; {ram.0394}
B3C4: 29 0F           AND     #$0F                ; 
B3C6: A8              TAY                         ; 
B3C7: B9 AD B3        LDA     $B3AD,Y             ; {}
B3CA: 85 00           STA     <$00                ; {ram.GP_00}
B3CC: BD BC 03        LDA     $03BC,X             ; {ram.03BC}
B3CF: A4 05           LDY     <$05                ; {ram.0005}
B3D1: 20 3A B4        JSR     $B43A               ; {}
B3D4: BD 94 03        LDA     $0394,X             ; {ram.0394}
B3D7: 29 18           AND     #$18                ; 
B3D9: C9 10           CMP     #$10                ; 
B3DB: 90 10           BCC     $B3ED               ; {}
B3DD: BD 12 04        LDA     $0412,X             ; {ram.0412}
B3E0: 38              SEC                         ; 
B3E1: E5 02           SBC     <$02                ; {ram.GP_02}
B3E3: 9D 12 04        STA     $0412,X             ; {ram.0412}
B3E6: B5 70           LDA     $70,X               ; {ram.0070}
B3E8: E5 03           SBC     <$03                ; {ram.GP_03}
B3EA: 4C FA B3        JMP     $B3FA               ; {}
B3ED: BD 12 04        LDA     $0412,X             ; {ram.0412}
B3F0: 18              CLC                         ; 
B3F1: 65 02           ADC     <$02                ; {ram.GP_02}
B3F3: 9D 12 04        STA     $0412,X             ; {ram.0412}
B3F6: B5 70           LDA     $70,X               ; {ram.0070}
B3F8: 65 03           ADC     <$03                ; {ram.GP_03}
B3FA: 95 70           STA     $70,X               ; {ram.0070}
B3FC: BD 94 03        LDA     $0394,X             ; {ram.0394}
B3FF: 18              CLC                         ; 
B400: 69 08           ADC     #$08                ; 
B402: 29 0F           AND     #$0F                ; 
B404: A8              TAY                         ; 
B405: B9 AD B3        LDA     $B3AD,Y             ; {}
B408: 85 00           STA     <$00                ; {ram.GP_00}
B40A: BD BC 03        LDA     $03BC,X             ; {ram.03BC}
B40D: A4 06           LDY     <$06                ; {ram.0006}
B40F: 20 3A B4        JSR     $B43A               ; {}
B412: BD 94 03        LDA     $0394,X             ; {ram.0394}
B415: 38              SEC                         ; 
B416: E9 08           SBC     #$08                ; 
B418: 29 18           AND     #$18                ; 
B41A: C9 10           CMP     #$10                ; 
B41C: 90 0E           BCC     $B42C               ; {}
B41E: BD 1F 04        LDA     $041F,X             ; {ram.041F}
B421: 38              SEC                         ; 
B422: E5 02           SBC     <$02                ; {ram.GP_02}
B424: 9D 1F 04        STA     $041F,X             ; {ram.041F}
B427: B5 84           LDA     $84,X               ; {ram.0084}
B429: E5 03           SBC     <$03                ; {ram.GP_03}
B42B: 60              RTS                         ; 
B42C: BD 1F 04        LDA     $041F,X             ; {ram.041F}
B42F: 18              CLC                         ; 
B430: 65 02           ADC     <$02                ; {ram.GP_02}
B432: 9D 1F 04        STA     $041F,X             ; {ram.041F}
B435: B5 84           LDA     $84,X               ; {ram.0084}
B437: 65 03           ADC     <$03                ; {ram.GP_03}
B439: 60              RTS                         ; 
B43A: 85 01           STA     <$01                ; {ram.GP_01}
B43C: A9 00           LDA     #$00                ; 
B43E: 85 02           STA     <$02                ; {ram.GP_02}
B440: 85 03           STA     <$03                ; {ram.GP_03}
B442: 06 02           ASL     <$02                ; {ram.GP_02}
B444: 26 03           ROL     <$03                ; {ram.GP_03}
B446: 06 00           ASL     <$00                ; {ram.GP_00}
B448: 90 0B           BCC     $B455               ; {}
B44A: A5 02           LDA     <$02                ; {ram.GP_02}
B44C: 18              CLC                         ; 
B44D: 65 01           ADC     <$01                ; {ram.GP_01}
B44F: 85 02           STA     <$02                ; {ram.GP_02}
B451: 90 02           BCC     $B455               ; {}
B453: E6 03           INC     <$03                ; {ram.GP_03}
B455: 88              DEY                         ; 
B456: D0 EA           BNE     $B442               ; {}
B458: 60              RTS                         ; 
B459: 85 0A           STA     <$0A                ; {ram.000A}
B45B: BD 80 03        LDA     $0380,X             ; 
B45E: 38              SEC                         ; 
B45F: E5 0A           SBC     <$0A                ; {ram.000A}
B461: 9D 80 03        STA     $0380,X             ; 
B464: BD 94 03        LDA     $0394,X             ; {ram.0394}
B467: E5 0B           SBC     <$0B                ; {ram.000B}
B469: 29 1F           AND     #$1F                ; 
B46B: 9D 94 03        STA     $0394,X             ; {ram.0394}
B46E: 60              RTS                         ; 


B46F: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B480: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B4A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B4C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B4E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B500: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B520: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B540: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B560: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B580: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B5A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B5C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B5E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B600: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B620: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B640: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B660: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B680: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B6A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B6C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B6E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B700: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B720: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B740: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B760: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B780: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B7A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B7C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B7E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B800: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B820: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B840: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B860: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B880: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B8A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B8C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B8E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B900: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B920: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B940: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B960: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B980: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B9A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B9C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B9E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BA00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BA20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BA40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BA60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BA80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BAA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BAC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BAE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BB00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BB20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BB40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BB60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BB80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BBA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BBC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BBE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BC00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BC20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BC40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BC60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BC80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BCA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BCC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BCE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BD00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BD20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BD40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BD60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BD80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BDA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BDC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BDE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BE00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BE20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BE40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BE60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BE80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BEA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BEC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BEE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BF00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BF20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BF40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 

; From here down is the same in all banks (except for the origin
; difference in bank 7). 
```

# RESET

```code
RESET: 
;
; Configure the MMC1 and jump to E440 (Bank 7) for startup.
;
BF50: 78              SEI                         ; Disable interrupts
BF51: D8              CLD                         ; Clear decimal flag
BF52: A9 00           LDA     #$00                ; Clear the PPU control register ...
BF54: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1} -_P_CNTRL_1 ... truns off NMIs
BF57: A2 FF           LDX     #$FF                ; Stack to ...
BF59: 9A              TXS                         ; ... 01FF
BF5A: AD 02 20        LDA     $2002               ; {hard.P_STATUS} Wait ...
BF5D: 29 80           AND     #$80                ; ... for ...
BF5F: F0 F9           BEQ     $BF5A               ; {} ... VBLANK
BF61: AD 02 20        LDA     $2002               ; {hard.P_STATUS} Wait ...
BF64: 29 80           AND     #$80                ; ... for another ...
BF66: F0 F9           BEQ     $BF61               ; {} ... VBLANK (1st might have been a leftover flag)
BF68: 09 FF           ORA     #$FF                ; Reset ...
BF6A: 8D 00 80        STA     $8000               ; {} ... ...
BF6D: 8D 00 A0        STA     $A000               ; {} ... all ...
BF70: 8D 00 C0        STA     $C000               ; ... four ...
BF73: 8D 00 E0        STA     $E000               ; ... MMC1 registers
BF76: A9 0F           LDA     #$0F                ; Set MMC control to 8K CHR ROM, fixed/bank 16K PRG pages, ...
BF78: 20 98 BF        JSR     $BF98               ; {code.MMC_Control} ... and horizontal mirroring (vertical scrolling)
BF7B: A9 00           LDA     #$00                ; Set MMC reg1 VROM bank
BF7D: 8D 00 A0        STA     $A000               ; {} The cartridge doesn't ...
BF80: 4A              LSR     A                   ; ... swap VROM pages. ...
BF81: 8D 00 A0        STA     $A000               ; {} ... Just ...
BF84: 4A              LSR     A                   ; ... set ...
BF85: 8D 00 A0        STA     $A000               ; {} ... to ...
BF88: 4A              LSR     A                   ; ...
BF89: 8D 00 A0        STA     $A000               ; {} ...
BF8C: 4A              LSR     A                   ; ...
BF8D: 8D 00 A0        STA     $A000               ; {} ... --00000
BF90: A9 07           LDA     #$07                ; Interesting! Put bank 7 ...
BF92: 20 AC BF        JSR     $BFAC               ; {code.MMC_Bank} ... in the low ROM bank
BF95: 4C 40 E4        JMP     $E440               ; Start of game

; MMC1 Info
; R0 - Control ***CPPMM
;  C CHR ROM bank mode. Zelda uses 0: 8KB at a time
;  PP Program ROM switch mode. Zelda uses 3: 16K fixed, 16K switched banks
;  MM Name table mirroring. Zelda uses 2 or 3: vertical or horizontal
; R1 - CHR bank size ***CCCCC
;  Ignored in Zelda since R0.C is 0
; R2 - CHR bank select ***CCCCC
;  Ignored in Zelda since R0.C is 0
; R3 - PRG bank select ***RPPPP
;  R PRG RAM enabled. Zelda sends 0, but battery-backed RAM is always enabled.
;  PPPP bank select. Zelda switches banks 0-6.
```

# MMC Control

```code
MMC_Control: 
; Set the MMC Control register (0) to value in A
BF98: 8D 00 80        STA     $8000               ; {} MMC Register 0 (control): --edcba ...
BF9B: 4A              LSR     A                   ; ... mirroring
BF9C: 8D 00 80        STA     $8000               ; {} ... mirroring
BF9F: 4A              LSR     A                   ; ... switch: c=0 high ROM, C=1 low ROM
BFA0: 8D 00 80        STA     $8000               ; {} ... size: d=0 32K (full), D=1 16K (half)
BFA3: 4A              LSR     A                   ; ... chrrom mode: e=0 8K banks, B=1 4K banks
BFA4: 8D 00 80        STA     $8000               ; {} The MMC is write-trigger (write to ROM ...
BFA7: 4A              LSR     A                   ; .. has no affect anyway).
BFA8: 8D 00 80        STA     $8000               ; {} Bits are written from LSB to MSB ...
BFAB: 60              RTS                         ; ... only 5 bits
```

# MMC Bank

```code
MMC_Bank: 
; Set the MMC Bank register (3) to value in A
BFAC: 8D 00 E0        STA     $E000               ; MMC Register 3 (ROM page switching): --edcba ...
BFAF: 4A              LSR     A                   ; ...
BFB0: 8D 00 E0        STA     $E000               ; ... Write the ...
BFB3: 4A              LSR     A                   ; ... switching ...
BFB4: 8D 00 E0        STA     $E000               ; ... page ...
BFB7: 4A              LSR     A                   ; ... number
BFB8: 8D 00 E0        STA     $E000               ; The MMC is write-trigger (write to ROM ...
BFBB: 4A              LSR     A                   ; .. has no affect anyway).
BFBC: 8D 00 E0        STA     $E000               ; Bits are written from LSB to MSB ...
BFBF: 60              RTS                         ; ... only 5 bits

BFC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
BFD0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
BFE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
BFF0: FF FF FF FF FF FF FF FF FF FF
```

# Vectors

```code
BFFA: 84 E4       ; NMI to E484
BFFC: 50 BF       ; RESET to BF50
BFFE: F0 BF       ; IRQ to BFF0 (this bank should never be at end)
```

