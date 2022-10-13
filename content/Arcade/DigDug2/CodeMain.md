; CPU: 6809
; ORIGIN: 0x8000
; FILES: d:/git/computerarcheology/content/arcade/digdug2/roms/main.bin

8000: B7 50 02        STA     $5002                   
8003: B6 80 00        LDA     $8000                   
8006: B6 10 06        LDA     $1006                   
8009: B4 10 05        ANDA    $1005                   
800C: B7 10 07        STA     $1007                   
800F: 8E 50 04        LDX     #$5004                  
8012: A7 86           STA     A,X                 
8014: B6 10 08        LDA     $1008                   
8017: C6 08           LDB     #$08                  
8019: 3D              MUL                         
801A: 8E 38 00        LDX     #$3800                  
801D: A7 8B           STA     D,X                 
801F: 8E 1F 16        LDX     #$1F16                  
8022: CE 1F 80        LDU     #$1F80                  
8025: EC 04           LDD     4,X                 
8027: ED C9 F8 00     STD     $F800,U                 
802B: EC 02           LDD     2,X                 
802D: ED C9 08 00     STD     $0800,U                 
8031: EC 84           LDD     ,X                  
8033: ED C1           STD     ,U++                
8035: 30 88 20        LEAX    $20,X                 
8038: 8C 1F 96        CMPX    #$1F96                  
803B: 26 E8           BNE     $8025                   
803D: 8E 20 16        LDX     #$2016                  
8040: EC 04           LDD     4,X                 
8042: ED C9 F8 00     STD     $F800,U                 
8046: EC 02           LDD     2,X                 
8048: ED C9 08 00     STD     $0800,U                 
804C: EC 84           LDD     ,X                  
804E: ED C1           STD     ,U++                
8050: 30 88 20        LEAX    $20,X                 
8053: 8C 27 96        CMPX    #$2796                  
8056: 26 E8           BNE     $8040                   
8058: B6 25 00        LDA     $2500                   
805B: 27 03           BEQ     $8060                   
805D: BD 8E 81        JSR     $8E81                   
8060: 7C 10 01        INC     $1001                   
8063: 7C 10 00        INC     $1000                   
8066: B6 10 50        LDA     $1050                   
8069: 26 02           BNE     $806D                   
806B: 86 3C           LDA     #$3C                  
806D: 4A              DECA                        
806E: B7 10 50        STA     $1050                   
8071: 3B              RTI                         
8072: 10 CE 19 00     LDS     #$1900                  
8076: 86 10           LDA     #$10                  
8078: 1F 8B           TFR     A,DP                   
807A: CE 00 00        LDU     #$0000                  
807D: 8E 10 00        LDX     #$1000                  
8080: B6 80 00        LDA     $8000                   
8083: EF 81           STU     ,X++                
8085: 8C 28 00        CMPX    #$2800                  
8088: 26 F6           BNE     $8080                   
808A: CE 19 0E        LDU     #$190E                  
808D: 8E 18 00        LDX     #$1800                  
8090: BD 81 6B        JSR     $816B                   
8093: 30 02           LEAX    2,X                 
8095: 8C 18 40        CMPX    #$1840                  
8098: 26 F6           BNE     $8090                   
809A: 8E 1F 10        LDX     #$1F10                  
809D: BD 81 5B        JSR     $815B                   
80A0: 30 88 20        LEAX    $20,X                 
80A3: 8C 1F 90        CMPX    #$1F90                  
80A6: 26 F5           BNE     $809D                   
80A8: 8E 20 10        LDX     #$2010                  
80AB: BD 81 5B        JSR     $815B                   
80AE: 30 88 20        LEAX    $20,X                 
80B1: 8C 27 90        CMPX    #$2790                  
80B4: 26 F5           BNE     $80AB                   
80B6: CC 81 D9        LDD     #$81D9                  
80B9: FD 19 0E        STD     $190E                   
80BC: 1C EF           ANDCC   #$EF                  
80BE: B7 50 03        STA     $5003                   
80C1: B6 10 00        LDA     $1000                   
80C4: 27 FB           BEQ     $80C1                   
80C6: 7F 10 00        CLR     $1000                   
80C9: B6 48 14        LDA     $4814                   
80CC: 84 01           ANDA    #$01                  
80CE: 10 26 64 E8     LBNE    $E5BA                   
80D2: B6 48 17        LDA     $4817                   
80D5: 84 08           ANDA    #$08                  
80D7: 10 26 64 DF     LBNE    $E5BA                   
80DB: B6 48 00        LDA     $4800                   
80DE: 84 0F           ANDA    #$0F                  
80E0: BB 40 54        ADDA    $4054                   
80E3: B7 40 54        STA     $4054                   
80E6: 7F 48 00        CLR     $4800                   
80E9: B6 10 E7        LDA     $10E7                   
80EC: 26 03           BNE     $80F1                   
80EE: BD 86 35        JSR     $8635                   
80F1: B6 10 EF        LDA     $10EF                   
80F4: 27 25           BEQ     $811B                   
80F6: B6 10 1B        LDA     $101B                   
80F9: 27 20           BEQ     $811B                   
80FB: B6 48 05        LDA     $4805                   
80FE: F6 10 5B        LDB     $105B                   
8101: 58 ; ????
8102: 85 08           BITA    #$08                  
8104: 27 01           BEQ     $8107                   
8106: 5C              INCB                        
8107: C4 03           ANDB    #$03                  
8109: F7 10 5B        STB     $105B                   
810C: B6 10 DE        LDA     $10DE                   
810F: C1 01           CMPB    #$01                  
8111: 26 03           BNE     $8116                   
8113: 4C              INCA                        
8114: 84 01           ANDA    #$01                  
8116: B7 10 DE        STA     $10DE                   
8119: 26 0C           BNE     $8127                   
811B: 8E 18 00        LDX     #$1800                  
811E: 8D 6A           BSR     $818A                   
8120: 30 02           LEAX    2,X                 
8122: 8C 18 30        CMPX    #$1830                  
8125: 26 F7           BNE     $811E                   
8127: B6 25 00        LDA     $2500                   
812A: 27 03           BEQ     $812F                   
812C: BD 8E AD        JSR     $8EAD                   
812F: 8E 1F 10        LDX     #$1F10                  
8132: 8D 56           BSR     $818A                   
8134: 8D 68           BSR     $819E                   
8136: 30 88 20        LEAX    $20,X                 
8139: 8C 1F 90        CMPX    #$1F90                  
813C: 26 F4           BNE     $8132                   
813E: 8E 20 10        LDX     #$2010                  
8141: 8D 47           BSR     $818A                   
8143: 8D 59           BSR     $819E                   
8145: 30 88 20        LEAX    $20,X                 
8148: 8C 27 90        CMPX    #$2790                  
814B: 26 F4           BNE     $8141                   
814D: 7E 80 BE        JMP     $80BE                   
8150: BE 10 02        LDX     $1002                   
8153: 10 EF 84        STS     ,X                  
8156: 10 CE 18 FE     LDS     #$18FE                  
815A: 39              RTS                         
815B: CC 10 10        LDD     #$1010                  
815E: 6F 80           CLR     ,X+                 
8160: 5A              DECB                        
8161: 26 FB           BNE     $815E                   
8163: 30 88 E0        LEAX    $E0,X                 
8166: E7 80           STB     ,X+                 
8168: 4A              DECA                        
8169: 26 FB           BNE     $8166                   
816B: B6 80 00        LDA     $8000                   
816E: CC 81 91        LDD     #$8191                  
8171: EF 84           STU     ,X                  
8173: 33 C8 10        LEAU    $10,U                 
8176: ED 94           STD     [,X]                
8178: 39              RTS                         
8179: CC 81 91        LDD     #$8191                  
817C: EE 84           LDU     ,X                  
817E: ED C3           STD     ,--U                
8180: EF 84           STU     ,X                  
8182: 39              RTS                         
8183: EE 84           LDU     ,X                  
8185: EC C1           LDD     ,U++                
8187: EF 84           STU     ,X                  
8189: 39              RTS                         
818A: BF 10 02        STX     $1002                   
818D: 10 EE 84        LDS     ,X                  
8190: 39              RTS                         
8191: CC 81 99        LDD     #$8199                  
8194: BE 10 02        LDX     $1002                   
8197: ED 94           STD     [,X]                
8199: 10 CE 18 FE     LDS     #$18FE                  
819D: 39              RTS                         
819E: A6 0C           LDA     12,X                
81A0: 26 36           BNE     $81D8                   
81A2: 6C 0C           INC     12,X                
81A4: EC 0E           LDD     14,X                
81A6: 7D 10 07        TST     $1007                   
81A9: 27 05           BEQ     $81B0                   
81AB: 53              COMB                        
81AC: 43              COMA                        
81AD: C3 01 01        ADDD    #$0101                  
81B0: C3 00 28        ADDD    #$0028                  
81B3: 34 02           PSHS    A                   
81B5: A6 08           LDA     8,X                 
81B7: 85 04           BITA    #$04                  
81B9: 35 02           PULS    A                   
81BB: 26 03           BNE     $81C0                   
81BD: C3 00 08        ADDD    #$0008                  
81C0: E7 07           STB     7,X                 
81C2: A7 09           STA     9,X                 
81C4: E6 0D           LDB     13,X                
81C6: B6 10 07        LDA     $1007                   
81C9: 26 01           BNE     $81CC                   
81CB: 50              NEGB                        
81CC: CB F1           ADDB    #$F1                  
81CE: A6 08           LDA     8,X                 
81D0: 85 08           BITA    #$08                  
81D2: 26 02           BNE     $81D6                   
81D4: CB 08           ADDB    #$08                  
81D6: E7 06           STB     6,X                 
81D8: 39              RTS                         
81D9: BD 81 50        JSR     $8150                   
81DC: BD 87 01        JSR     $8701                   
81DF: 8E 48 00        LDX     #$4800                  
81E2: CC 00 00        LDD     #$0000                  
81E5: A7 80           STA     ,X+                 
81E7: 8C 48 09        CMPX    #$4809                  
81EA: 26 F9           BNE     $81E5                   
81EC: 8E 48 10        LDX     #$4810                  
81EF: ED 81           STD     ,X++                
81F1: 8C 48 20        CMPX    #$4820                  
81F4: 26 F9           BNE     $81EF                   
81F6: BD 81 50        JSR     $8150                   
81F9: BD 81 50        JSR     $8150                   
81FC: B7 50 0B        STA     $500B                   
81FF: B7 50 09        STA     $5009                   
8202: BD 81 50        JSR     $8150                   
8205: BD 81 50        JSR     $8150                   
8208: 86 04           LDA     #$04                  
820A: B7 48 18        STA     $4818                   
820D: BD 81 50        JSR     $8150                   
8210: BD 81 50        JSR     $8150                   
8213: BD 85 6A        JSR     $856A                   
8216: BD 8C 05        JSR     $8C05                   
8219: BD 9A C4        JSR     $9AC4                   
821C: BD 81 50        JSR     $8150                   
821F: BD 81 50        JSR     $8150                   
8222: CC 01 03        LDD     #$0103                  
8225: B7 48 0A        STA     $480A                   
8228: B7 48 0C        STA     $480C                   
822B: F7 48 08        STB     $4808                   
822E: F6 48 15        LDB     $4815                   
8231: C4 08           ANDB    #$08                  
8233: 26 01           BNE     $8236                   
8235: 4F              CLRA                        
8236: B7 10 06        STA     $1006                   
8239: B6 48 14        LDA     $4814                   
823C: 84 02           ANDA    #$02                  
823E: 8B 03           ADDA    #$03                  
8240: B7 10 CC        STA     $10CC                   
8243: B6 48 16        LDA     $4816                   
8246: 84 03           ANDA    #$03                  
8248: 48 ; ????
8249: B7 10 70        STA     $1070                   
824C: B6 48 16        LDA     $4816                   
824F: 84 08           ANDA    #$08                  
8251: B7 10 EF        STA     $10EF                   
8254: B6 48 16        LDA     $4816                   
8257: 84 04           ANDA    #$04                  
8259: B7 10 F0        STA     $10F0                   
825C: BD 8F 67        JSR     $8F67                   
825F: BD 81 50        JSR     $8150                   
8262: BD 8A B2        JSR     $8AB2                   
8265: 4F              CLRA                        
8266: B7 10 05        STA     $1005                   
8269: B7 10 07        STA     $1007                   
826C: B7 10 0A        STA     $100A                   
826F: B7 10 1B        STA     $101B                   
8272: B7 10 E7        STA     $10E7                   
8275: B7 48 01        STA     $4801                   
8278: B7 48 09        STA     $4809                   
827B: BD 87 06        JSR     $8706                   
827E: BD 8B 3D        JSR     $8B3D                   
8281: BD 8B DF        JSR     $8BDF                   
8284: FC 48 02        LDD     $4802                   
8287: 84 0F           ANDA    #$0F                  
8289: 26 6A           BNE     $82F5                   
828B: C4 0F           ANDB    #$0F                  
828D: 26 66           BNE     $82F5                   
828F: BD 87 06        JSR     $8706                   
8292: BD 86 9E        JSR     $869E                   
8295: BD 85 CA        JSR     $85CA                   
8298: CC 01 08        LDD     #$0108                  
829B: B7 10 E2        STA     $10E2                   
829E: F7 10 4F        STB     $104F                   
82A1: BD 81 50        JSR     $8150                   
82A4: FC 48 02        LDD     $4802                   
82A7: 84 0F           ANDA    #$0F                  
82A9: 26 4A           BNE     $82F5                   
82AB: C4 0F           ANDB    #$0F                  
82AD: 26 46           BNE     $82F5                   
82AF: B6 10 50        LDA     $1050                   
82B2: 26 ED           BNE     $82A1                   
82B4: 7A 10 4F        DEC     $104F                   
82B7: 26 E8           BNE     $82A1                   
82B9: BD 9A D7        JSR     $9AD7                   
82BC: CC 00 05        LDD     #$0005                  
82BF: B7 10 E2        STA     $10E2                   
82C2: F7 10 4F        STB     $104F                   
82C5: BD 81 50        JSR     $8150                   
82C8: FC 48 02        LDD     $4802                   
82CB: 84 0F           ANDA    #$0F                  
82CD: 26 26           BNE     $82F5                   
82CF: C4 0F           ANDB    #$0F                  
82D1: 26 22           BNE     $82F5                   
82D3: B6 10 50        LDA     $1050                   
82D6: 26 ED           BNE     $82C5                   
82D8: 7A 10 4F        DEC     $104F                   
82DB: 26 E8           BNE     $82C5                   
82DD: 7C 10 10        INC     $1010                   
82E0: BD 81 50        JSR     $8150                   
82E3: FC 48 02        LDD     $4802                   
82E6: 84 0F           ANDA    #$0F                  
82E8: 26 0B           BNE     $82F5                   
82EA: C4 0F           ANDB    #$0F                  
82EC: 26 07           BNE     $82F5                   
82EE: B6 10 10        LDA     $1010                   
82F1: 26 ED           BNE     $82E0                   
82F3: 20 9A           BRA     $828F                   
82F5: 7F 10 10        CLR     $1010                   
82F8: 7F 10 E2        CLR     $10E2                   
82FB: 7C 10 E3        INC     $10E3                   
82FE: BD 87 06        JSR     $8706                   
8301: BD 8B 3D        JSR     $8B3D                   
8304: BD 8B DF        JSR     $8BDF                   
8307: BD 8C B6        JSR     $8CB6                   
830A: BD 85 CA        JSR     $85CA                   
830D: BD 86 5B        JSR     $865B                   
8310: BD 8A A0        JSR     $8AA0                   
8313: BD 81 50        JSR     $8150                   
8316: B6 48 01        LDA     $4801                   
8319: 84 0F           ANDA    #$0F                  
831B: 27 F0           BEQ     $830D                   
831D: 7F 10 E3        CLR     $10E3                   
8320: 7C 10 E7        INC     $10E7                   
8323: BD 84 D5        JSR     $84D5                   
8326: B6 10 EF        LDA     $10EF                   
8329: 27 25           BEQ     $8350                   
832B: 7C 10 E1        INC     $10E1                   
832E: 7F 48 00        CLR     $4800                   
8331: B6 48 01        LDA     $4801                   
8334: 84 0F           ANDA    #$0F                  
8336: 4A              DECA                        
8337: B7 10 04        STA     $1004                   
833A: 43              COMA                        
833B: 84 01           ANDA    #$01                  
833D: B7 10 DE        STA     $10DE                   
8340: 7F 48 01        CLR     $4801                   
8343: 7C 48 09        INC     $4809                   
8346: BD 81 50        JSR     $8150                   
8349: B6 10 E1        LDA     $10E1                   
834C: 26 F8           BNE     $8346                   
834E: 20 2F           BRA     $837F                   
8350: B6 17 25        LDA     $1725                   
8353: 26 30           BNE     $8385                   
8355: 7C 10 E9        INC     $10E9                   
8358: B6 10 05        LDA     $1005                   
835B: 26 15           BNE     $8372                   
835D: 7F 48 00        CLR     $4800                   
8360: B6 48 01        LDA     $4801                   
8363: 84 0F           ANDA    #$0F                  
8365: 4A              DECA                        
8366: B7 10 04        STA     $1004                   
8369: BD 8B 3D        JSR     $8B3D                   
836C: 7F 48 01        CLR     $4801                   
836F: 7C 48 09        INC     $4809                   
8372: BD 81 50        JSR     $8150                   
8375: B6 10 E9        LDA     $10E9                   
8378: 26 F8           BNE     $8372                   
837A: B6 10 05        LDA     $1005                   
837D: 26 03           BNE     $8382                   
837F: BD 84 BC        JSR     $84BC                   
8382: BD C4 A8        JSR     $C4A8                   
8385: BD 87 06        JSR     $8706                   
8388: BD 87 67        JSR     $8767                   
838B: BD 87 B3        JSR     $87B3                   
838E: BD 88 24        JSR     $8824                   
8391: 86 3C           LDA     #$3C                  
8393: B7 10 4F        STA     $104F                   
8396: 7C 40 40        INC     $4040                   
8399: BD 81 50        JSR     $8150                   
839C: 7A 10 4F        DEC     $104F                   
839F: 26 F8           BNE     $8399                   
83A1: BD 85 38        JSR     $8538                   
83A4: BD C1 2A        JSR     $C12A                   
83A7: BD 81 50        JSR     $8150                   
83AA: BD 88 24        JSR     $8824                   
83AD: BD 81 50        JSR     $8150                   
83B0: B6 10 D0        LDA     $10D0                   
83B3: 26 4A           BNE     $83FF                   
83B5: B6 10 D1        LDA     $10D1                   
83B8: 26 0B           BNE     $83C5                   
83BA: FC 10 DC        LDD     $10DC                   
83BD: B7 40 41        STA     $4041                   
83C0: F7 40 42        STB     $4042                   
83C3: 20 E8           BRA     $83AD                   
83C5: CC 00 00        LDD     #$0000                  
83C8: B7 40 41        STA     $4041                   
83CB: B7 40 42        STA     $4042                   
83CE: FD 10 DC        STD     $10DC                   
83D1: 7C 40 52        INC     $4052                   
83D4: BD 81 50        JSR     $8150                   
83D7: B6 40 52        LDA     $4052                   
83DA: BA 10 D7        ORA     $10D7                   
83DD: BA 10 D9        ORA     $10D9                   
83E0: BA 10 DF        ORA     $10DF                   
83E3: BA 10 E6        ORA     $10E6                   
83E6: BA 10 5E        ORA     $105E                   
83E9: 26 E9           BNE     $83D4                   
83EB: BD C4 A8        JSR     $C4A8                   
83EE: BD C0 E9        JSR     $C0E9                   
83F1: B6 10 D0        LDA     $10D0                   
83F4: 26 45           BNE     $843B                   
83F6: BD C4 9B        JSR     $C49B                   
83F9: BD 85 4D        JSR     $854D                   
83FC: 7E 83 50        JMP     $8350                   
83FF: CC 00 00        LDD     #$0000                  
8402: B7 40 41        STA     $4041                   
8405: B7 40 42        STA     $4042                   
8408: FD 10 DC        STD     $10DC                   
840B: 7F 10 E8        CLR     $10E8                   
840E: BD 81 50        JSR     $8150                   
8411: B6 40 51        LDA     $4051                   
8414: BA 40 4D        ORA     $404D                   
8417: BA 10 4F        ORA     $104F                   
841A: BA 10 D7        ORA     $10D7                   
841D: BA 10 D9        ORA     $10D9                   
8420: BA 10 DF        ORA     $10DF                   
8423: BA 10 E6        ORA     $10E6                   
8426: BA 10 5E        ORA     $105E                   
8429: 26 E3           BNE     $840E                   
842B: B6 10 D1        LDA     $10D1                   
842E: 27 08           BEQ     $8438                   
8430: BD C4 A8        JSR     $C4A8                   
8433: BD C0 E9        JSR     $C0E9                   
8436: 20 03           BRA     $843B                   
8438: BD 84 E3        JSR     $84E3                   
843B: B6 10 D0        LDA     $10D0                   
843E: B4 10 D1        ANDA    $10D1                   
8441: B7 10 E0        STA     $10E0                   
8444: BD C4 9B        JSR     $C49B                   
8447: BD 85 4D        JSR     $854D                   
844A: 7A 17 03        DEC     $1703                   
844D: 27 14           BEQ     $8463                   
844F: B6 10 04        LDA     $1004                   
8452: 10 27 FE FA     LBEQ    $8350                   
8456: B6 17 43        LDA     $1743                   
8459: 10 27 FE F3     LBEQ    $8350                   
845D: BD 84 F2        JSR     $84F2                   
8460: 7E 83 50        JMP     $8350                   
8463: BD 87 06        JSR     $8706                   
8466: BD 87 50        JSR     $8750                   
8469: CC 00 00        LDD     #$0000                  
846C: B7 40 41        STA     $4041                   
846F: B7 40 42        STA     $4042                   
8472: FD 10 DC        STD     $10DC                   
8475: 7C 40 44        INC     $4044                   
8478: 7C 10 E3        INC     $10E3                   
847B: BD 81 50        JSR     $8150                   
847E: B6 40 44        LDA     $4044                   
8481: 26 F8           BNE     $847B                   
8483: 7F 10 E3        CLR     $10E3                   
8486: BD 81 50        JSR     $8150                   
8489: BD 9B 69        JSR     $9B69                   
848C: B6 10 E5        LDA     $10E5                   
848F: 27 05           BEQ     $8496                   
8491: BD 81 50        JSR     $8150                   
8494: 20 F6           BRA     $848C                   
8496: B6 17 43        LDA     $1743                   
8499: 26 C2           BNE     $845D                   
849B: B6 10 05        LDA     $1005                   
849E: 10 27 FD C3     LBEQ    $8265                   
84A2: 8E 17 00        LDX     #$1700                  
84A5: EC 84           LDD     ,X                  
84A7: EE 88 40        LDU     $40,X                 
84AA: ED 88 40        STD     $40,X                 
84AD: EF 81           STU     ,X++                
84AF: A6 84           LDA     ,X                  
84B1: E6 88 40        LDB     $40,X                 
84B4: A7 88 40        STA     $40,X                 
84B7: E7 84           STB     ,X                  
84B9: 7E 82 65        JMP     $8265                   
84BC: 7C 10 0A        INC     $100A                   
84BF: CC 00 00        LDD     #$0000                  
84C2: FD 10 D0        STD     $10D0                   
84C5: FD 10 DC        STD     $10DC                   
84C8: BD 8C 81        JSR     $8C81                   
84CB: BD 88 15        JSR     $8815                   
84CE: BD 8B 3D        JSR     $8B3D                   
84D1: BD 8B DF        JSR     $8BDF                   
84D4: 39              RTS                         

84D5: CC 00 00        LDD     #$0000                  
84D8: 8E 17 00        LDX     #$1700                  
84DB: ED 81           STD     ,X++                
84DD: 8C 17 80        CMPX    #$1780                  
84E0: 26 F9           BNE     $84DB                   
84E2: 39              RTS                         

84E3: 8E 15 00        LDX     #$1500                  
84E6: EC 81           LDD     ,X++                
84E8: ED 89 FD FE     STD     $FDFE,X                 
84EC: 8C 15 78        CMPX    #$1578                  
84EF: 26 F5           BNE     $84E6                   
84F1: 39              RTS                         

84F2: 8E 17 00        LDX     #$1700                  
84F5: EC 84           LDD     ,X                  
84F7: EE 88 40        LDU     $40,X                 
84FA: EF 81           STU     ,X++                
84FC: ED 88 3E        STD     $3E,X                 
84FF: 8C 17 40        CMPX    #$1740                  
8502: 26 F1           BNE     $84F5                   
8504: 7F 10 E8        CLR     $10E8                   
8507: 8E 15 80        LDX     #$1580                  
850A: EC 84           LDD     ,X                  
850C: EE 89 00 C0     LDU     $00C0,X                 
8510: EF 81           STU     ,X++                
8512: ED 89 00 BE     STD     $00BE,X                 
8516: 8C 16 40        CMPX    #$1640                  
8519: 26 EF           BNE     $850A                   
851B: 8E 13 00        LDX     #$1300                  
851E: EC 84           LDD     ,X                  
8520: EE 89 00 80     LDU     $0080,X                 
8524: EF 81           STU     ,X++                
8526: ED 88 7E        STD     $7E,X                 
8529: 8C 13 78        CMPX    #$1378                  
852C: 26 F0           BNE     $851E                   
852E: B6 10 05        LDA     $1005                   
8531: 4C              INCA                        
8532: 84 01           ANDA    #$01                  
8534: B7 10 05        STA     $1005                   
8537: 39              RTS                         

8538: 86 01           LDA     #$01                  
853A: B7 10 1B        STA     $101B                   
853D: B7 25 00        STA     $2500                   
8540: B7 10 D6        STA     $10D6                   
8543: B7 10 D2        STA     $10D2                   
8546: B7 10 D4        STA     $10D4                   
8549: B7 10 E8        STA     $10E8                   
854C: 39              RTS                         

854D: 4F              CLRA                        
854E: B7 10 D1        STA     $10D1                   
8551: B7 10 D0        STA     $10D0                   
8554: B7 10 1B        STA     $101B                   
8557: B7 10 E4        STA     $10E4                   
855A: B7 10 D6        STA     $10D6                   
855D: B7 25 00        STA     $2500                   
8560: B7 1F 60        STA     $1F60                   
8563: B7 10 D2        STA     $10D2                   
8566: B7 10 D4        STA     $10D4                   
8569: 39              RTS                         

856A: 8E 48 00        LDX     #$4800                  
856D: CE 85 88        LDU     #$8588                  
8570: A6 88 14        LDA     $14,X                 
8573: 84 0C           ANDA    #$0C                  
8575: 44              LSRA                        
8576: EC C6           LDD     A,U                 
8578: ED 09           STD     9,X                 
857A: ED 0B           STD     11,X                
857C: CC 01 00        LDD     #$0100                  
857F: ED 0D           STD     13,X                
8581: E7 0F           STB     15,X                
8583: 86 02           LDA     #$02                  
8585: A7 08           STA     8,X                 
8587: 39              RTS                         

8588: 01 ; ????
8589: 01 ; ????
858A: 02 ; ????
858B: 01 ; ????
858C: 01 ; ????
858D: 02 ; ????
858E: 03 01           COM     $01                   
8590: B7 10 09        STA     $1009                   
8593: A6 C0           LDA     ,U+                 
8595: A7 84           STA     ,X                  
8597: 30 88 E0        LEAX    $E0,X                 
859A: 7A 10 09        DEC     $1009                   
859D: 26 F4           BNE     $8593                   
859F: 39              RTS                         
85A0: F7 10 09        STB     $1009                   
85A3: A7 84           STA     ,X                  
85A5: 30 88 E0        LEAX    $E0,X                 
85A8: 7A 10 09        DEC     $1009                   
85AB: 26 F6           BNE     $85A3                   
85AD: 39              RTS                         
85AE: B7 10 09        STA     $1009                   
85B1: 30 01           LEAX    1,X                 
85B3: A6 C0           LDA     ,U+                 
85B5: A7 82           STA     ,-X                 
85B7: 7A 10 09        DEC     $1009                   
85BA: 26 F7           BNE     $85B3                   
85BC: 39              RTS                         
85BD: F7 10 09        STB     $1009                   
85C0: 30 01           LEAX    1,X                 
85C2: A7 82           STA     ,-X                 
85C4: 7A 10 09        DEC     $1009                   
85C7: 26 F9           BNE     $85C2                   
85C9: 39              RTS                         
85CA: 8E 0B 17        LDX     #$0B17                  
85CD: 86 00           LDA     #$00                  
85CF: C6 16           LDB     #$16                  
85D1: BD 85 A0        JSR     $85A0                   
85D4: 8E 0A F9        LDX     #$0AF9                  
85D7: 86 00           LDA     #$00                  
85D9: C6 13           LDB     #$13                  
85DB: BD 85 A0        JSR     $85A0                   
85DE: 8E 0A 3C        LDX     #$0A3C                  
85E1: 86 0D           LDA     #$0D                  
85E3: C6 07           LDB     #$07                  
85E5: BD 85 A0        JSR     $85A0                   
85E8: 8E 02 D7        LDX     #$02D7                  
85EB: CE 86 0A        LDU     #$860A                  
85EE: 86 11           LDA     #$11                  
85F0: BD 85 90        JSR     $8590                   
85F3: 8E 02 F9        LDX     #$02F9                  
85F6: CE 86 1B        LDU     #$861B                  
85F9: 86 13           LDA     #$13                  
85FB: BD 85 90        JSR     $8590                   
85FE: 8E 02 3C        LDX     #$023C                  
8601: CE 86 2E        LDU     #$862E                  
8604: 86 07           LDA     #$07                  
8606: BD 85 90        JSR     $8590                   
8609: 39              RTS                         
860A: 70 20 31        NEG     $2031                   
860D: 39              RTS                         
860E: 38 ; ????
860F: 32 20           LEAS    0,Y                 
8611: 31 39           LEAY    -7,Y                
8613: 38 ; ????
8614: 35 20           PULS    Y                   
8616: 4E ; ????
8617: 41 ; ????
8618: 4D              TSTA                        
8619: 43              COMA                        
861A: 4F              CLRA                        
861B: 41 ; ????
861C: 4C              INCA                        
861D: 4C              INCA                        
861E: 20 52           BRA     $8672                   
8620: 49              ROLA                        
8621: 47              ASRA                        
8622: 48 ; ????
8623: 54              LSRB                        
8624: 53              COMB                        
8625: 20 52           BRA     $8679                   
8627: 45 ; ????
8628: 53              COMB                        
8629: 45 ; ????
862A: 52 ; ????
862B: 56              RORB                        
862C: 45 ; ????
862D: 44              LSRA                        
862E: 71 ; ????
862F: 74 75 78        LSR     $7578                   
8632: 7C F6 F7        INC     $F6F7                   
8635: 8E 07 AB        LDX     #$07AB                  
8638: CE 86 B4        LDU     #$86B4                  
863B: 86 08           LDA     #$08                  
863D: BD 85 AE        JSR     $85AE                   
8640: 8E 0F AB        LDX     #$0FAB                  
8643: 86 0E           LDA     #$0E                  
8645: C6 06           LDB     #$06                  
8647: BD 85 BD        JSR     $85BD                   
864A: FC 48 02        LDD     $4802                   
864D: C4 0F           ANDB    #$0F                  
864F: F7 07 A3        STB     $07A3                   
8652: 84 0F           ANDA    #$0F                  
8654: 26 01           BNE     $8657                   
8656: 39              RTS                         
8657: B7 07 A4        STA     $07A4                   
865A: 39              RTS                         
865B: B6 10 01        LDA     $1001                   
865E: 85 08           BITA    #$08                  
8660: 26 0C           BNE     $866E                   
8662: 8E 02 89        LDX     #$0289                  
8665: 86 20           LDA     #$20                  
8667: C6 0D           LDB     #$0D                  
8669: BD 85 A0        JSR     $85A0                   
866C: 20 0B           BRA     $8679                   
866E: 8E 02 89        LDX     #$0289                  
8671: CE 86 BD        LDU     #$86BD                  
8674: 86 0D           LDA     #$0D                  
8676: BD 85 90        JSR     $8590                   
8679: FC 48 02        LDD     $4802                   
867C: 84 0F           ANDA    #$0F                  
867E: 26 06           BNE     $8686                   
8680: C4 0F           ANDB    #$0F                  
8682: C1 01           CMPB    #$01                  
8684: 27 0C           BEQ     $8692                   
8686: 8E 03 0B        LDX     #$030B                  
8689: CE 86 E0        LDU     #$86E0                  
868C: 86 16           LDA     #$16                  
868E: BD 85 90        JSR     $8590                   
8691: 39              RTS                         
8692: 8E 03 0B        LDX     #$030B                  
8695: CE 86 CA        LDU     #$86CA                  
8698: 86 16           LDA     #$16                  
869A: BD 85 90        JSR     $8590                   
869D: 39              RTS                         
869E: 8E 02 73        LDX     #$0273                  
86A1: CE 86 F6        LDU     #$86F6                  
86A4: 86 0B           LDA     #$0B                  
86A6: BD 85 90        JSR     $8590                   
86A9: 8E 0A 73        LDX     #$0A73                  
86AC: 86 0E           LDA     #$0E                  
86AE: C6 0B           LDB     #$0B                  
86B0: BD 85 A0        JSR     $85A0                   
86B3: 39              RTS                         
86B4: 43              COMA                        
86B5: 52 ; ????
86B6: 45 ; ????
86B7: 44              LSRA                        
86B8: 49              ROLA                        
86B9: 54              LSRB                        
86BA: 20 20           BRA     $86DC                   
86BC: 20 54           BRA     $8712                   
86BE: 4F              CLRA                        
86BF: 20 53           BRA     $8714                   
86C1: 54              LSRB                        
86C2: 41 ; ????
86C3: 52 ; ????
86C4: 54              LSRB                        
86C5: 20 50           BRA     $8717                   
86C7: 55 ; ????
86C8: 53              COMB                        
86C9: 48 ; ????
86CA: 4F              CLRA                        
86CB: 4E ; ????
86CC: 4C              INCA                        
86CD: 59              ROLB                        
86CE: 20 31           BRA     $8701                   
86D0: 20 50           BRA     $8722                   
86D2: 4C              INCA                        
86D3: 41 ; ????
86D4: 59              ROLB                        
86D5: 45 ; ????
86D6: 52 ; ????
86D7: 5D              TSTB                        
86D8: 53              COMB                        
86D9: 20 42           BRA     $871D                   
86DB: 55 ; ????
86DC: 54              LSRB                        
86DD: 54              LSRB                        
86DE: 4F              CLRA                        
86DF: 4E ; ????
86E0: 31 20           LEAY    0,Y                 
86E2: 4F              CLRA                        
86E3: 52 ; ????
86E4: 20 32           BRA     $8718                   
86E6: 20 50           BRA     $8738                   
86E8: 4C              INCA                        
86E9: 41 ; ????
86EA: 59              ROLB                        
86EB: 45 ; ????
86EC: 52 ; ????
86ED: 53              COMB                        
86EE: 5D              TSTB                        
86EF: 20 42           BRA     $8733                   
86F1: 55 ; ????
86F2: 54              LSRB                        
86F3: 54              LSRB                        
86F4: 4F              CLRA                        
86F5: 4E ; ????
86F6: 49              ROLA                        
86F7: 4E ; ????
86F8: 53              COMB                        
86F9: 45 ; ????
86FA: 52 ; ????
86FB: 54              LSRB                        
86FC: 20 43           BRA     $8741                   
86FE: 4F              CLRA                        
86FF: 49              ROLA                        
8700: 4E ; ????
8701: 8D 03           BSR     $8706                   
8703: 8D 17           BSR     $871C                   
8705: 39              RTS                         
8706: CC 20 20        LDD     #$2020                  
8709: 8E 00 00        LDX     #$0000                  
870C: 6F 89 08 00     CLR     $0800,X                 
8710: 6F 89 08 01     CLR     $0801,X                 
8714: ED 81           STD     ,X++                
8716: 8C 07 80        CMPX    #$0780                  
8719: 26 F1           BNE     $870C                   
871B: 39              RTS                         
871C: CC 20 20        LDD     #$2020                  
871F: 8E 07 80        LDX     #$0780                  
8722: 6F 89 08 00     CLR     $0800,X                 
8726: 6F 89 08 01     CLR     $0801,X                 
872A: ED 81           STD     ,X++                
872C: 8C 08 00        CMPX    #$0800                  
872F: 26 F1           BNE     $8722                   
8731: 39              RTS                         
8732: EC 84           LDD     ,X                  
8734: FD 10 30        STD     $1030                   
8737: EC 06           LDD     6,X                 
8739: FD 10 32        STD     $1032                   
873C: 86 F0           LDA     #$F0                  
873E: 6F 86           CLR     A,X                 
8740: 4C              INCA                        
8741: 81 10           CMPA    #$10                  
8743: 26 F9           BNE     $873E                   
8745: FC 10 30        LDD     $1030                   
8748: ED 84           STD     ,X                  
874A: FC 10 32        LDD     $1032                   
874D: ED 06           STD     6,X                 
874F: 39              RTS                         
8750: 8E 02 70        LDX     #$0270                  
8753: CE 87 A9        LDU     #$87A9                  
8756: 86 0A           LDA     #$0A                  
8758: BD 85 90        JSR     $8590                   
875B: 8E 0A 4E        LDX     #$0A4E                  
875E: 86 0A           LDA     #$0A                  
8760: C6 0D           LDB     #$0D                  
8762: BD 85 A0        JSR     $85A0                   
8765: 20 1F           BRA     $8786                   
8767: 8E 02 4C        LDX     #$024C                  
876A: CE 87 9E        LDU     #$879E                  
876D: 86 05           LDA     #$05                  
876F: BD 85 90        JSR     $8590                   
8772: 8E 0A 4C        LDX     #$0A4C                  
8775: 86 0A           LDA     #$0A                  
8777: C6 05           LDB     #$05                  
8779: BD 85 A0        JSR     $85A0                   
877C: 8E 0A 4E        LDX     #$0A4E                  
877F: 86 0A           LDA     #$0A                  
8781: C6 0A           LDB     #$0A                  
8783: BD 85 A0        JSR     $85A0                   
8786: 8E 02 4E        LDX     #$024E                  
8789: CE 87 A3        LDU     #$87A3                  
878C: 86 06           LDA     #$06                  
878E: BD 85 90        JSR     $8590                   
8791: B6 10 05        LDA     $1005                   
8794: 4C              INCA                        
8795: B7 01 6E        STA     $016E                   
8798: 86 0B           LDA     #$0B                  
879A: B7 09 6E        STA     $096E                   
879D: 39              RTS                         
879E: 52 ; ????
879F: 45 ; ????
87A0: 41 ; ????
87A1: 44              LSRA                        
87A2: 59              ROLB                        
87A3: 50              NEGB                        
87A4: 4C              INCA                        
87A5: 41 ; ????
87A6: 59              ROLB                        
87A7: 45 ; ????
87A8: 52 ; ????
87A9: 47              ASRA                        
87AA: 41 ; ????
87AB: 4D              TSTA                        
87AC: 45 ; ????
87AD: 20 20           BRA     $87CF                   
87AF: 4F              CLRA                        
87B0: 56              RORB                        
87B1: 45 ; ????
87B2: 52 ; ????
87B3: 8E 0A 50        LDX     #$0A50                  
87B6: 86 0A           LDA     #$0A                  
87B8: C6 05           LDB     #$05                  
87BA: BD 85 A0        JSR     $85A0                   
87BD: 86 0B           LDA     #$0B                  
87BF: B7 09 90        STA     $0990                   
87C2: B7 09 70        STA     $0970                   
87C5: 8E 02 50        LDX     #$0250                  
87C8: CE 88 0D        LDU     #$880D                  
87CB: 86 05           LDA     #$05                  
87CD: BD 85 90        JSR     $8590                   
87D0: B6 10 E7        LDA     $10E7                   
87D3: 27 0B           BEQ     $87E0                   
87D5: 8E 07 AB        LDX     #$07AB                  
87D8: CE 88 0D        LDU     #$880D                  
87DB: 86 08           LDA     #$08                  
87DD: BD 85 AE        JSR     $85AE                   
87E0: B6 17 05        LDA     $1705                   
87E3: 84 0F           ANDA    #$0F                  
87E5: B7 01 70        STA     $0170                   
87E8: B7 10 34        STA     $1034                   
87EB: B6 17 05        LDA     $1705                   
87EE: 84 F0           ANDA    #$F0                  
87F0: 27 06           BEQ     $87F8                   
87F2: 44              LSRA                        
87F3: 44              LSRA                        
87F4: 44              LSRA                        
87F5: 44              LSRA                        
87F6: 20 02           BRA     $87FA                   
87F8: 86 20           LDA     #$20                  
87FA: B7 01 90        STA     $0190                   
87FD: B7 10 35        STA     $1035                   
8800: B6 10 E7        LDA     $10E7                   
8803: 26 01           BNE     $8806                   
8805: 39              RTS                         
8806: FC 10 34        LDD     $1034                   
8809: FD 07 A3        STD     $07A3                   
880C: 39              RTS                         
880D: 52 ; ????
880E: 4F              CLRA                        
880F: 55 ; ????
8810: 4E ; ????
8811: 44              LSRA                        
8812: 20 20           BRA     $8834                   
8814: 20 F6           BRA     $880C                   
8816: 10 ; ????
8817: CC F7 17        LDD     #$F717                  
881A: 03 B6           COM     $B6                   
881C: 10 ; ????
881D: 04 27           LSR     $27                   
881F: 03 F7           COM     $F7                   
8821: 17 43 39        LBSR    $CB5D                   
8824: 8E 07 BC        LDX     #$07BC                  
8827: 86 20           LDA     #$20                  
8829: C6 0A           LDB     #$0A                  
882B: BD 85 BD        JSR     $85BD                   
882E: 8E 07 9C        LDX     #$079C                  
8831: 86 20           LDA     #$20                  
8833: C6 0A           LDB     #$0A                  
8835: BD 85 BD        JSR     $85BD                   
8838: 8E 0F BC        LDX     #$0FBC                  
883B: 86 00           LDA     #$00                  
883D: C6 0A           LDB     #$0A                  
883F: BD 85 BD        JSR     $85BD                   
8842: 8E 0F 9C        LDX     #$0F9C                  
8845: 86 00           LDA     #$00                  
8847: C6 0A           LDB     #$0A                  
8849: BD 85 BD        JSR     $85BD                   
884C: B6 17 03        LDA     $1703                   
884F: B0 10 E8        SUBA    $10E8                   
8852: 26 01           BNE     $8855                   
8854: 39              RTS                         
8855: 81 05           CMPA    #$05                  
8857: 23 02           BLS     $885B                   
8859: 86 05           LDA     #$05                  
885B: B7 10 CE        STA     $10CE                   
885E: 8E 88 80        LDX     #$8880                  
8861: CE 07 BC        LDU     #$07BC                  
8864: EC 81           LDD     ,X++                
8866: 33 CB           LEAU    D,U                 
8868: B6 10 CE        LDA     $10CE                   
886B: B7 10 09        STA     $1009                   
886E: EC 81           LDD     ,X++                
8870: 8D 06           BSR     $8878                   
8872: 8C 88 90        CMPX    #$8890                  
8875: 26 EA           BNE     $8861                   
8877: 39              RTS                         
8878: ED C3           STD     ,--U                
887A: 7A 10 09        DEC     $1009                   
887D: 26 F9           BNE     $8878                   
887F: 39              RTS                         
8880: FF E1 24        STU     $E124                   
8883: 26 00           BNE     $8885                   
8885: 01 ; ????
8886: 25 ; ????
8887: 27 07           BEQ     $8890                   
8889: E1 08           CMPB    8,X                 
888B: 0D 08           TST     $08                   
888D: 01 ; ????
888E: 0D 0D           TST     $0D                   
8890: BD 81 50        JSR     $8150                   
8893: B6 10 E2        LDA     $10E2                   
8896: 27 F8           BEQ     $8890                   
8898: 8E 20 10        LDX     #$2010                  
889B: CE 8A 05        LDU     #$8A05                  
889E: BD 8A A0        JSR     $8AA0                   
88A1: 84 1F           ANDA    #$1F                  
88A3: 4C              INCA                        
88A4: A7 04           STA     4,X                 
88A6: A6 C0           LDA     ,U+                 
88A8: A7 0A           STA     10,X                
88AA: 6C 0B           INC     11,X                
88AC: EC C1           LDD     ,U++                
88AE: A7 0F           STA     15,X                
88B0: E7 0D           STB     13,X                
88B2: 6F 0C           CLR     12,X                
88B4: 30 88 20        LEAX    $20,X                 
88B7: 8C 24 30        CMPX    #$2430                  
88BA: 26 E2           BNE     $889E                   
88BC: 8E 0B 09        LDX     #$0B09                  
88BF: 86 40           LDA     #$40                  
88C1: C6 15           LDB     #$15                  
88C3: BD 85 A0        JSR     $85A0                   
88C6: 8E 0B 0A        LDX     #$0B0A                  
88C9: 86 40           LDA     #$40                  
88CB: C6 15           LDB     #$15                  
88CD: BD 85 A0        JSR     $85A0                   
88D0: 8E 0B 0B        LDX     #$0B0B                  
88D3: 86 40           LDA     #$40                  
88D5: C6 15           LDB     #$15                  
88D7: BD 85 A0        JSR     $85A0                   
88DA: 8E 0B 0C        LDX     #$0B0C                  
88DD: 86 40           LDA     #$40                  
88DF: C6 15           LDB     #$15                  
88E1: BD 85 A0        JSR     $85A0                   
88E4: 8E 0B 0D        LDX     #$0B0D                  
88E7: 86 40           LDA     #$40                  
88E9: C6 15           LDB     #$15                  
88EB: BD 85 A0        JSR     $85A0                   
88EE: 8E 0B 0E        LDX     #$0B0E                  
88F1: 86 40           LDA     #$40                  
88F3: C6 15           LDB     #$15                  
88F5: BD 85 A0        JSR     $85A0                   
88F8: 8E 0B 0F        LDX     #$0B0F                  
88FB: 86 40           LDA     #$40                  
88FD: C6 15           LDB     #$15                  
88FF: BD 85 A0        JSR     $85A0                   
8902: 86 30           LDA     #$30                  
8904: B7 20 14        STA     $2014                   
8907: BD 81 50        JSR     $8150                   
890A: B6 10 E2        LDA     $10E2                   
890D: 10 27 00 E3     LBEQ    $89F4                   
8911: B6 10 01        LDA     $1001                   
8914: 85 01           BITA    #$01                  
8916: 26 EF           BNE     $8907                   
8918: 8E 24 10        LDX     #$2410                  
891B: 6A 0F           DEC     15,X                
891D: 6F 0C           CLR     12,X                
891F: 30 88 E0        LEAX    $E0,X                 
8922: 8C 1F F0        CMPX    #$1FF0                  
8925: 26 F4           BNE     $891B                   
8927: 6A 88 24        DEC     $24,X                 
892A: 26 DB           BNE     $8907                   
892C: 86 3C           LDA     #$3C                  
892E: A7 88 24        STA     $24,X                 
8931: BD 81 50        JSR     $8150                   
8934: B6 10 E2        LDA     $10E2                   
8937: 10 27 00 B9     LBEQ    $89F4                   
893B: 7A 20 14        DEC     $2014                   
893E: 26 F1           BNE     $8931                   
8940: 8E 01 EA        LDX     #$01EA                  
8943: CE 8A 68        LDU     #$8A68                  
8946: 86 05           LDA     #$05                  
8948: BD 85 90        JSR     $8590                   
894B: 8E 02 0B        LDX     #$020B                  
894E: CE 8A 6D        LDU     #$8A6D                  
8951: 86 06           LDA     #$06                  
8953: BD 85 90        JSR     $8590                   
8956: 8E 02 0C        LDX     #$020C                  
8959: CE 8A 73        LDU     #$8A73                  
895C: 86 06           LDA     #$06                  
895E: BD 85 90        JSR     $8590                   
8961: 8E 02 0D        LDX     #$020D                  
8964: CE 8A 79        LDU     #$8A79                  
8967: 86 05           LDA     #$05                  
8969: BD 85 90        JSR     $8590                   
896C: 8E 02 0E        LDX     #$020E                  
896F: CE 8A 7E        LDU     #$8A7E                  
8972: 86 06           LDA     #$06                  
8974: BD 85 90        JSR     $8590                   
8977: 8E 02 0F        LDX     #$020F                  
897A: CE 8A 84        LDU     #$8A84                  
897D: 86 05           LDA     #$05                  
897F: BD 85 90        JSR     $8590                   
8982: 8E 09 EA        LDX     #$09EA                  
8985: 86 10           LDA     #$10                  
8987: C6 05           LDB     #$05                  
8989: BD 85 A0        JSR     $85A0                   
898C: 8E 0A 0B        LDX     #$0A0B                  
898F: CE 8A 89        LDU     #$8A89                  
8992: 86 06           LDA     #$06                  
8994: BD 85 90        JSR     $8590                   
8997: 8E 0A 0C        LDX     #$0A0C                  
899A: CE 8A 8F        LDU     #$8A8F                  
899D: 86 06           LDA     #$06                  
899F: BD 85 90        JSR     $8590                   
89A2: 8E 0A 0D        LDX     #$0A0D                  
89A5: CE 8A 95        LDU     #$8A95                  
89A8: 86 05           LDA     #$05                  
89AA: BD 85 90        JSR     $8590                   
89AD: 8E 0A 0E        LDX     #$0A0E                  
89B0: CE 8A 9A        LDU     #$8A9A                  
89B3: 86 06           LDA     #$06                  
89B5: BD 85 90        JSR     $8590                   
89B8: 8E 0A 0F        LDX     #$0A0F                  
89BB: 86 0A           LDA     #$0A                  
89BD: C6 05           LDB     #$05                  
89BF: BD 85 A0        JSR     $85A0                   
89C2: 86 1F           LDA     #$1F                  
89C4: B7 20 14        STA     $2014                   
89C7: BD 81 50        JSR     $8150                   
89CA: B6 10 E2        LDA     $10E2                   
89CD: 27 25           BEQ     $89F4                   
89CF: 7A 20 14        DEC     $2014                   
89D2: 26 F3           BNE     $89C7                   
89D4: BD 81 50        JSR     $8150                   
89D7: B6 10 E2        LDA     $10E2                   
89DA: 27 18           BEQ     $89F4                   
89DC: B6 10 01        LDA     $1001                   
89DF: 85 08           BITA    #$08                  
89E1: 26 05           BNE     $89E8                   
89E3: BD 86 A9        JSR     $86A9                   
89E6: 20 EC           BRA     $89D4                   
89E8: 8E 0A 73        LDX     #$0A73                  
89EB: 86 00           LDA     #$00                  
89ED: C6 0B           LDB     #$0B                  
89EF: BD 85 A0        JSR     $85A0                   
89F2: 20 E0           BRA     $89D4                   
89F4: 8E 20 10        LDX     #$2010                  
89F7: BD 87 32        JSR     $8732                   
89FA: 30 88 20        LEAX    $20,X                 
89FD: 8C 24 30        CMPX    #$2430                  
8A00: 26 F5           BNE     $89F7                   
8A02: 7E 88 90        JMP     $8890                   
8A05: E4 50           ANDB    -16,U               
8A07: 3A              ABX                         
8A08: E9 60           ADCB    0,S                 
8A0A: 3A              ABX                         
8A0B: EE 70           LDU     -16,S               
8A0D: 3A              ABX                         
8A0E: E3 50           ADDD    -16,U               
8A10: 4A              DECA                        
8A11: E8 60           EORB    0,S                 
8A13: 4A              DECA                        
8A14: ED 70           STD     -16,S               
8A16: 4A              DECA                        
8A17: E2 50           SBCB    -16,U               
8A19: 5A              DECB                        
8A1A: E7 60           STB     0,S                 
8A1C: 5A              DECB                        
8A1D: EC 70           LDD     -16,S               
8A1F: 5A              DECB                        
8A20: E1 50           CMPB    -16,U               
8A22: 6A E6           DEC     A,S                 
8A24: 60 6A           NEG     10,S                
8A26: EB 70           ADDB    -16,S               
8A28: 6A E0           DEC     ,S+                 
8A2A: 50              NEGB                        
8A2B: 7A E5 60        DEC     $E560                   
8A2E: 7A EA 70        DEC     $EA70                   
8A31: 7A E4 50        DEC     $E450                   
8A34: 86 E9           LDA     #$E9                  
8A36: 60 86           NEG     A,X                 
8A38: EE 70           LDU     -16,S               
8A3A: 86 E3           LDA     #$E3                  
8A3C: 50              NEGB                        
8A3D: 96 E8           LDA     $E8                   
8A3F: 60 96           NEG     [A,X]               
8A41: ED 70           STD     -16,S               
8A43: 96 E1           LDA     $E1                   
8A45: 50              NEGB                        
8A46: B6 E6 60        LDA     $E660                   
8A49: B6 EB 70        LDA     $EB70                   
8A4C: B6 E0 50        LDA     $E050                   
8A4F: C6 E5           LDB     #$E5                  
8A51: 60 C6           NEG     A,U                 
8A53: EA 70           ORB     -16,S               
8A55: C6 F0           LDB     #$F0                  
8A57: 50              NEGB                        
8A58: 9E F2           LDX     $F2                   
8A5A: 60 ; ????
8A5B: 9E F4           LDX     $F4                   
8A5D: 70 9E EF        NEG     $9EEF                   
8A60: 50              NEGB                        
8A61: AE F1           LDX     [,S++]              
8A63: 60 ; ????
8A64: AE F3           LDX     [,--S]              
8A66: 70 AE 90        NEG     $AE90                   
8A69: 91 92           CMPA    $92                   
8A6B: 93 94           SUBD    $94                   
8A6D: 95 96           BITA    $96                   
8A6F: 97 98           STA     $98                   
8A71: 99 9A           ADCA    $9A                   
8A73: 9B 9C           ADDA    $9C                   
8A75: 9D 9E           JSR     $9E                   
8A77: 9F 21           STX     $21                   
8A79: 22 23           BHI     $8A9E                   
8A7B: 28 29           BVC     $8AA6                   
8A7D: 2A 2C           BPL     $8AAB                   
8A7F: 2D 2E           BLT     $8AAF                   
8A81: 2F 3A           BLE     $8ABD                   
8A83: 3B              RTI                         
8A84: 3C 3D           CWAI    $3D                   
8A86: 3E              RESET                       
8A87: 3F              SWI                         
8A88: 2B 0E           BMI     $8A98                   
8A8A: 11 ; ????
8A8B: 11 ; ????
8A8C: 11 ; ????
8A8D: 11 ; ????
8A8E: 0A 0A           DEC     $0A                   
8A90: 11 ; ????
8A91: 24 ; ????
8A92: 0A 10           DEC     $10                   
8A94: 0A 0A           DEC     $0A                   
8A96: 11 ; ????
8A97: 10 ; ????
8A98: 24 ; ????
8A99: 10 ; ????
8A9A: 24 ; ????
8A9B: 11 ; ????
8A9C: 11 ; ????
8A9D: 11 ; ????
8A9E: 11 ; ????
8A9F: 24 ; ????
8AA0: B6 10 11        LDA     $1011                   
8AA3: 48 ; ????
8AA4: 48 ; ????
8AA5: 48 ; ????
8AA6: B8 10 11        EORA    $1011                   
8AA9: 43              COMA                        
8AAA: 48 ; ????
8AAB: 79 10 11        ROL     $1011                   
8AAE: B6 10 11        LDA     $1011                   
8AB1: 39              RTS                         
8AB2: 8E 0F FD        LDX     #$0FFD                  
8AB5: 86 00           LDA     #$00                  
8AB7: C6 07           LDB     #$07                  
8AB9: BD 85 BD        JSR     $85BD                   
8ABC: 8E 0F F4        LDX     #$0FF4                  
8ABF: 86 00           LDA     #$00                  
8AC1: C6 0A           LDB     #$0A                  
8AC3: BD 85 BD        JSR     $85BD                   
8AC6: 8E 0F E1        LDX     #$0FE1                  
8AC9: 86 00           LDA     #$00                  
8ACB: C6 02           LDB     #$02                  
8ACD: BD 85 BD        JSR     $85BD                   
8AD0: 8E 0F EA        LDX     #$0FEA                  
8AD3: 86 00           LDA     #$00                  
8AD5: C6 07           LDB     #$07                  
8AD7: BD 85 BD        JSR     $85BD                   
8ADA: 39              RTS                         
8ADB: 7D 10 10        TST     $1010                   
8ADE: 27 01           BEQ     $8AE1                   
8AE0: 39              RTS                         

;
; Add a 4-digit BCD value to the 6-digit BCD score
; Amount to add in D (D is 4-digit BCD number)
; Score is at 1700,1701,1702 (two digits per byte, left to right)
;
; Once the upper digit is non-zero, we set the other digits to 00s and ignore any
; new additions.
8AE1: 7D 17 26        TST     $1726                 ; Have we already overflowed into the upper digit?
8AE4: 27 01           BEQ     $8AE7                 ; No ... we can add more to it
8AE6: 39              RTS                           ; Yes ... just ignore
;
8AE7: 1E 89           EXG     A,B                   ; Start with the low part
8AE9: BB 17 02        ADDA    $1702                 ; Add in the lower 2 digits
8AEC: 19              DAA                           ; Correct binary math to BCD result
8AED: B7 17 02        STA     $1702                 ; New lower 2 digits
8AF0: 1F 98           TFR     B,A                   ; Now for the middle 2 digits
8AF2: B9 17 01        ADCA    $1701                 ; Add the upper 2 digits
8AF5: 19              DAA                           ; Correct binary math to BCD result
8AF6: B7 17 01        STA     $1701                 ; New upper 2 digits
8AF9: B6 17 00        LDA     $1700                 ; Upper most 2 digits
8AFC: 89 00           ADCA    #$00                  ; Any carry from the last addition
8AFE: 19              DAA                           ; Correct binary math to BCD result
8AFF: B7 17 00        STA     $1700                 ; Update the upper digit
8B02: 84 F0           ANDA    #$F0                  ; Did anything carry into the upper digit?
8B04: 27 22           BEQ     $8B28                 ; Upper digit is 0 ... ??
8B06: B7 17 26        STA     $1726                 ; Upper digit is not 0. Note the overflow.
8B09: 7F 17 01        CLR     $1701                 ; Set middle digits to 00
8B0C: 7F 17 02        CLR     $1702                 ; Set lower digits to 00
8B0F: 8E 0F F4        LDX     #$0FF4                  
8B12: 86 0B           LDA     #$0B                  
8B14: C6 0A           LDB     #$0A                  
8B16: BD 85 BD        JSR     $85BD                   
8B19: 8E 0F E1        LDX     #$0FE1                  
8B1C: 86 0B           LDA     #$0B                  
8B1E: C6 02           LDB     #$02                  
8B20: BD 85 BD        JSR     $85BD                   
8B23: 7C 40 55        INC     $4055                   
8B26: 20 15           BRA     $8B3D                   
;
8B28: BD 8C 17        JSR     $8C17                   
8B2B: 8E 17 00        LDX     #$1700                  
8B2E: A6 06           LDA     6,X                 
8B30: 2B 0B           BMI     $8B3D                   
8B32: A6 88 27        LDA     $27,X                 
8B35: A1 88 22        CMPA    $22,X                 
8B38: 25 ; ????
8B39: 03 BD           COM     $BD                   
8B3B: 8C 31 34        CMPX    #$3134                  
8B3E: 10 ; ????
8B3F: BD 8B BE        JSR     $8BBE                   
8B42: 8E 10 0B        LDX     #$100B                  
8B45: CE 07 F3        LDU     #$07F3                  
8B48: 8D 29           BSR     $8B73                   
8B4A: 8D 09           BSR     $8B55                   
8B4C: FC 07 F0        LDD     $07F0                   
8B4F: FD 07 E0        STD     $07E0                   
8B52: 35 10           PULS    X                   
8B54: 39              RTS                         

8B55: 8E 17 00        LDX     #$1700                  ; Current player score
8B58: CE 17 40        LDU     #$1740                  
8B5B: 7D 10 05        TST     $1005                   ; Player number ??
8B5E: 27 02           BEQ     $8B62                   
8B60: 1E 13           EXG     X,U                   
8B62: 34 40           PSHS    U                   
8B64: CE 07 FD        LDU     #$07FD                  
8B67: 8D 0A           BSR     $8B73                   
8B69: 35 10           PULS    X                   
8B6B: CE 07 EA        LDU     #$07EA                  
8B6E: 7D 10 04        TST     $1004                   
8B71: 27 0B           BEQ     $8B7E                   
8B73: 10 8E 05 03     LDY     #$0503                  
8B77: 8D 10           BSR     $8B89                   
8B79: 86 30           LDA     #$30                  
8B7B: A7 C4           STA     ,U                  
8B7D: 39              RTS                         
8B7E: CC 20 07        LDD     #$2007                  
8B81: A7 C4           STA     ,U                  
8B83: 33 5F           LEAU    -1,U                
8B85: 5A              DECB                        
8B86: 26 F9           BNE     $8B81                   
8B88: 39              RTS                         
8B89: C6 FF           LDB     #$FF                  
8B8B: 20 02           BRA     $8B8F                   
8B8D: C6 E0           LDB     #$E0                  
8B8F: 10 BF 10 0E     STY     $100E                   
8B93: A6 84           LDA     ,X                  
8B95: 44              LSRA                        
8B96: 44              LSRA                        
8B97: 44              LSRA                        
8B98: 44              LSRA                        
8B99: 84 0F           ANDA    #$0F                  
8B9B: 8D 0C           BSR     $8BA9                   
8B9D: A6 80           LDA     ,X+                 
8B9F: 84 0F           ANDA    #$0F                  
8BA1: 8D 06           BSR     $8BA9                   
8BA3: 7A 10 0F        DEC     $100F                   
8BA6: 26 EB           BNE     $8B93                   
8BA8: 39              RTS                         
8BA9: 81 00           CMPA    #$00                  
8BAB: 26 09           BNE     $8BB6                   
8BAD: 7A 10 0E        DEC     $100E                   
8BB0: 2B 04           BMI     $8BB6                   
8BB2: 86 20           LDA     #$20                  
8BB4: 20 03           BRA     $8BB9                   
8BB6: 7F 10 0E        CLR     $100E                   
8BB9: A7 C4           STA     ,U                  
8BBB: 33 C5           LEAU    B,U                 
8BBD: 39              RTS                         
8BBE: 8E 17 00        LDX     #$1700                  
8BC1: CE 10 0B        LDU     #$100B                  
8BC4: C6 03           LDB     #$03                  
8BC6: A6 84           LDA     ,X                  
8BC8: A1 C4           CMPA    ,U                  
8BCA: 24 ; ????
8BCB: 01 ; ????
8BCC: 39              RTS                         
8BCD: 26 08           BNE     $8BD7                   
8BCF: 30 01           LEAX    1,X                 
8BD1: 33 41           LEAU    1,U                 
8BD3: 5A              DECB                        
8BD4: 26 F0           BNE     $8BC6                   
8BD6: 39              RTS                         
8BD7: A6 80           LDA     ,X+                 
8BD9: A7 C0           STA     ,U+                 
8BDB: 5A              DECB                        
8BDC: 26 F9           BNE     $8BD7                   
8BDE: 39              RTS                         
8BDF: 8E 0F D4        LDX     #$0FD4                  
8BE2: 86 0D           LDA     #$0D                  
8BE4: C6 0A           LDB     #$0A                  
8BE6: BD 85 BD        JSR     $85BD                   
8BE9: 8E 0F C1        LDX     #$0FC1                  
8BEC: 86 0D           LDA     #$0D                  
8BEE: C6 02           LDB     #$02                  
8BF0: BD 85 BD        JSR     $85BD                   
8BF3: 8E 07 D4        LDX     #$07D4                  
8BF6: CE 8C 0C        LDU     #$8C0C                  
8BF9: 86 0A           LDA     #$0A                  
8BFB: BD 85 AE        JSR     $85AE                   
8BFE: FC 07 D0        LDD     $07D0                   
8C01: FD 07 C0        STD     $07C0                   
8C04: 39              RTS                         
8C05: B6 8C 16        LDA     $8C16                   
8C08: B7 10 0C        STA     $100C                   
8C0B: 39              RTS                         
8C0C: 48 ; ????
8C0D: 49              ROLA                        
8C0E: 47              ASRA                        
8C0F: 48 ; ????
8C10: 20 53           BRA     $8C65                   
8C12: 43              COMA                        
8C13: 4F              CLRA                        
8C14: 52 ; ????
8C15: 45 ; ????
8C16: 20 B6           BRA     $8BCE                   
8C18: 17 06 2B        LBSR    $9246                   
8C1B: 64 ; ????
8C1C: 8E 17 00        LDX     #$1700                  
8C1F: EC 84           LDD     ,X                  
8C21: 44              LSRA                        
8C22: 56              RORB                        
8C23: 44              LSRA                        
8C24: 56              RORB                        
8C25: 44              LSRA                        
8C26: 56              RORB                        
8C27: 44              LSRA                        
8C28: 56              RORB                        
8C29: E1 88 22        CMPB    $22,X                 
8C2C: 25 ; ????
8C2D: 52 ; ????
8C2E: E7 88 27        STB     $27,X                 
8C31: A6 03           LDA     3,X                 
8C33: 81 FF           CMPA    #$FF                  
8C35: 27 05           BEQ     $8C3C                   
8C37: 6C 03           INC     3,X                 
8C39: 7C 40 53        INC     $4053                   
8C3C: A6 06           LDA     6,X                 
8C3E: 85 01           BITA    #$01                  
8C40: 26 1B           BNE     $8C5D                   
8C42: 6A 88 24        DEC     $24,X                 
8C45: 27 32           BEQ     $8C79                   
8C47: E6 88 23        LDB     $23,X                 
8C4A: E7 88 22        STB     $22,X                 
8C4D: CE 8D 20        LDU     #$8D20                  
8C50: 48 ; ????
8C51: AB 88 24        ADDA    $24,X                 
8C54: E6 C6           LDB     A,U                 
8C56: E7 88 23        STB     $23,X                 
8C59: BD 88 24        JSR     $8824                   
8C5C: 39              RTS                         
8C5D: E6 88 23        LDB     $23,X                 
8C60: E7 88 22        STB     $22,X                 
8C63: CE 8D 21        LDU     #$8D21                  
8C66: 84 02           ANDA    #$02                  
8C68: 48 ; ????
8C69: AB 88 24        ADDA    $24,X                 
8C6C: A6 C6           LDA     A,U                 
8C6E: AB 88 23        ADDA    $23,X                 
8C71: 19              DAA                         
8C72: A7 88 23        STA     $23,X                 
8C75: BD 88 24        JSR     $8824                   
8C78: 39              RTS                         
8C79: 86 FF           LDA     #$FF                  
8C7B: A7 06           STA     6,X                 
8C7D: BD 88 24        JSR     $8824                   
8C80: 39              RTS                         
8C81: 8E 17 00        LDX     #$1700                  
8C84: CE 8D 19        LDU     #$8D19                  
8C87: B6 10 70        LDA     $1070                   
8C8A: 44              LSRA                        
8C8B: A7 06           STA     6,X                 
8C8D: F6 10 04        LDB     $1004                   
8C90: 27 03           BEQ     $8C95                   
8C92: A7 88 46        STA     $46,X                 
8C95: C6 05           LDB     #$05                  
8C97: 85 01           BITA    #$01                  
8C99: 26 0B           BNE     $8CA6                   
8C9B: E7 88 24        STB     $24,X                 
8C9E: 7D 10 04        TST     $1004                   
8CA1: 27 03           BEQ     $8CA6                   
8CA3: E7 88 64        STB     $64,X                 
8CA6: 48 ; ????
8CA7: EC C6           LDD     A,U                 
8CA9: ED 88 22        STD     $22,X                 
8CAC: 7D 10 04        TST     $1004                   
8CAF: 26 01           BNE     $8CB2                   
8CB1: 39              RTS                         
8CB2: ED 88 62        STD     $62,X                 
8CB5: 39              RTS                         
8CB6: 8E 0A 89        LDX     #$0A89                  
8CB9: 86 0D           LDA     #$0D                  
8CBB: C6 0D           LDB     #$0D                  
8CBD: BD 85 A0        JSR     $85A0                   
8CC0: 8E 0B 0B        LDX     #$0B0B                  
8CC3: 86 0B           LDA     #$0B                  
8CC5: C6 16           LDB     #$16                  
8CC7: BD 85 A0        JSR     $85A0                   
8CCA: 8E 03 2D        LDX     #$032D                  
8CCD: CE 8D 29        LDU     #$8D29                  
8CD0: 86 18           LDA     #$18                  
8CD2: BD 85 90        JSR     $8590                   
8CD5: 8E 02 AF        LDX     #$02AF                  
8CD8: CE 8D 2D        LDU     #$8D2D                  
8CDB: 86 14           LDA     #$14                  
8CDD: BD 85 90        JSR     $8590                   
8CE0: 8E 03 31        LDX     #$0331                  
8CE3: CE 8D 41        LDU     #$8D41                  
8CE6: 86 07           LDA     #$07                  
8CE8: BD 85 90        JSR     $8590                   
8CEB: 86 02           LDA     #$02                  
8CED: B7 03 2F        STA     $032F                   
8CF0: CC 4E 44        LDD     #$4E44                  
8CF3: B7 03 0F        STA     $030F                   
8CF6: F7 02 EF        STB     $02EF                   
8CF9: CE 8D 19        LDU     #$8D19                  
8CFC: B6 10 70        LDA     $1070                   
8CFF: EC C6           LDD     A,U                 
8D01: 84 0F           ANDA    #$0F                  
8D03: B7 01 4D        STA     $014D                   
8D06: 1F 98           TFR     B,A                   
8D08: 84 F0           ANDA    #$F0                  
8D0A: 27 07           BEQ     $8D13                   
8D0C: 44              LSRA                        
8D0D: 44              LSRA                        
8D0E: 44              LSRA                        
8D0F: 44              LSRA                        
8D10: B7 01 6F        STA     $016F                   
8D13: C4 0F           ANDB    #$0F                  
8D15: F7 01 4F        STB     $014F                   
8D18: 39              RTS                         
8D19: 03 08           COM     $08                   
8D1B: 03 10           COM     $10                   
8D1D: 03 12           COM     $12                   
8D1F: 03 15           COM     $15                   
8D21: 10 ; ????
8D22: 50              NEGB                        
8D23: 30 15           LEAX    -11,X               
8D25: 15 ; ????
8D26: 70 50 30        NEG     $5030                   
8D29: 31 53           LEAY    -13,U               
8D2B: 54              LSRB                        
8D2C: 20 42           BRA     $8D70                   
8D2E: 4F              CLRA                        
8D2F: 4E ; ????
8D30: 55 ; ????
8D31: 53              COMB                        
8D32: 20 46           BRA     $8D7A                   
8D34: 4F              CLRA                        
8D35: 52 ; ????
8D36: 20 20           BRA     $8D58                   
8D38: 20 30           BRA     $8D6A                   
8D3A: 30 30           LEAX    -16,Y               
8D3C: 30 20           LEAX    0,Y                 
8D3E: 50              NEGB                        
8D3F: 54              LSRB                        
8D40: 53              COMB                        
8D41: 41 ; ????
8D42: 4E ; ????
8D43: 44              LSRA                        
8D44: 20 5B           BRA     $8DA1                   
8D46: 5B ; ????
8D47: 5B ; ????
8D48: BD 81 50        JSR     $8150                   
8D4B: B6 10 E6        LDA     $10E6                   
8D4E: 27 F8           BEQ     $8D48                   
8D50: 8E 12 F7        LDX     #$12F7                  
8D53: 86 04           LDA     #$04                  
8D55: E6 86           LDB     A,X                 
8D57: 2B 11           BMI     $8D6A                   
8D59: 4A              DECA                        
8D5A: 26 F9           BNE     $8D55                   
8D5C: F6 10 CB        LDB     $10CB                   
8D5F: 27 04           BEQ     $8D65                   
8D61: C1 0B           CMPB    #$0B                  
8D63: 25 ; ????
8D64: 19              DAA                         
8D65: 7A 10 E6        DEC     $10E6                   
8D68: 20 DE           BRA     $8D48                   
8D6A: B7 10 34        STA     $1034                   
8D6D: 6F 86           CLR     A,X                 
8D6F: 8B 04           ADDA    #$04                  
8D71: E6 86           LDB     A,X                 
8D73: 6F 86           CLR     A,X                 
8D75: 5D              TSTB                        
8D76: 27 2D           BEQ     $8DA5                   
8D78: C1 0B           CMPB    #$0B                  
8D7A: 24 ; ????
8D7B: 29 20           BVS     $8D9D                   
8D7D: 05 ; ????
8D7E: 86 FF           LDA     #$FF                  
8D80: B7 10 CB        STA     $10CB                   
8D83: 8E 14 77        LDX     #$1477                  
8D86: 7C 10 5E        INC     $105E                   
8D89: B6 10 5E        LDA     $105E                   
8D8C: E7 86           STB     A,X                 
8D8E: 58 ; ????
8D8F: 8E 8D E4        LDX     #$8DE4                  
8D92: EC 85           LDD     B,X                 
8D94: BD 8A DB        JSR     $8ADB                   
8D97: 5F              CLRB                        
8D98: B6 10 CB        LDA     $10CB                   
8D9B: 2A 08           BPL     $8DA5                   
8D9D: F7 10 CB        STB     $10CB                   
8DA0: 7A 10 E6        DEC     $10E6                   
8DA3: 20 A3           BRA     $8D48                   
8DA5: 8E 12 88        LDX     #$1288                  
8DA8: B6 10 34        LDA     $1034                   
8DAB: A1 80           CMPA    ,X+                 
8DAD: 26 02           BNE     $8DB1                   
8DAF: E7 1F           STB     -1,X                
8DB1: 8C 12 F0        CMPX    #$12F0                  
8DB4: 26 F5           BNE     $8DAB                   
8DB6: 7A 10 E6        DEC     $10E6                   
8DB9: 20 8D           BRA     $8D48                   
8DBB: 8E 12 88        LDX     #$1288                  
8DBE: CC 00 00        LDD     #$0000                  
8DC1: ED 81           STD     ,X++                
8DC3: 8C 12 F0        CMPX    #$12F0                  
8DC6: 26 F9           BNE     $8DC1                   
8DC8: FD 14 78        STD     $1478                   
8DCB: FD 14 7A        STD     $147A                   
8DCE: B7 10 5E        STA     $105E                   
8DD1: B7 10 CB        STA     $10CB                   
8DD4: FD 12 F8        STD     $12F8                   
8DD7: FD 12 FA        STD     $12FA                   
8DDA: FD 12 FC        STD     $12FC                   
8DDD: FD 12 FE        STD     $12FE                   
8DE0: 86 04           LDA     #$04                  
8DE2: B7 10 5D        STA     $105D                   
8DE5: 39              RTS                         
8DE6: 01 ; ????
8DE7: 00 02           NEG     $02                   
8DE9: 00 04           NEG     $04                   
8DEB: 00 07           NEG     $07                   
8DED: 00 10           NEG     $10                   
8DEF: 00 15           NEG     $15                   
8DF1: 00 20           NEG     $20                   
8DF3: 00 30           NEG     $30                   
8DF5: 00 50           NEG     $50                   
8DF7: 00 80           NEG     $80                   
8DF9: 00 BD           NEG     $BD                   
8DFB: 81 50           CMPA    #$50                  
8DFD: B6 10 5E        LDA     $105E                   
8E00: 27 F8           BEQ     $8DFA                   
8E02: 8E 1F 10        LDX     #$1F10                  
8E05: 7A 10 5F        DEC     $105F                   
8E08: B6 10 5F        LDA     $105F                   
8E0B: CE 8E 7D        LDU     #$8E7D                  
8E0E: 84 01           ANDA    #$01                  
8E10: 48 ; ????
8E11: EC C6           LDD     A,U                 
8E13: A7 12           STA     -14,X               
8E15: E7 0D           STB     13,X                
8E17: CB F0           ADDB    #$F0                  
8E19: E7 88 2D        STB     $2D,X                 
8E1C: CC F5 0D        LDD     #$F50D                  
8E1F: ED 88 2A        STD     $2A,X                 
8E22: BB 14 78        ADDA    $1478                   
8E25: 7F 14 78        CLR     $1478                   
8E28: ED 0A           STD     10,X                
8E2A: CC 00 C8        LDD     #$00C8                  
8E2D: E7 0F           STB     15,X                
8E2F: E7 88 2F        STB     $2F,X                 
8E32: A7 0C           STA     12,X                
8E34: A7 88 2C        STA     $2C,X                 
8E37: BD 81 50        JSR     $8150                   
8E3A: 8E 1F 10        LDX     #$1F10                  
8E3D: A6 12           LDA     -14,X               
8E3F: AB 0D           ADDA    13,X                
8E41: 27 1A           BEQ     $8E5D                   
8E43: A7 0D           STA     13,X                
8E45: 8B F0           ADDA    #$F0                  
8E47: 27 14           BEQ     $8E5D                   
8E49: A7 88 2D        STA     $2D,X                 
8E4C: B6 10 01        LDA     $1001                   
8E4F: 84 08           ANDA    #$08                  
8E51: 27 02           BEQ     $8E55                   
8E53: 86 0D           LDA     #$0D                  
8E55: A7 0B           STA     11,X                
8E57: A7 88 2B        STA     $2B,X                 
8E5A: 4F              CLRA                        
8E5B: 20 D5           BRA     $8E32                   
8E5D: BD 87 32        JSR     $8732                   
8E60: 8E 1F 30        LDX     #$1F30                  
8E63: BD 87 32        JSR     $8732                   
8E66: 7A 10 5E        DEC     $105E                   
8E69: 27 8F           BEQ     $8DFA                   
8E6B: B6 10 5E        LDA     $105E                   
8E6E: 8E 14 78        LDX     #$1478                  
8E71: E6 01           LDB     1,X                 
8E73: E7 80           STB     ,X+                 
8E75: 4A              DECA                        
8E76: 26 F9           BNE     $8E71                   
8E78: A7 84           STA     ,X                  
8E7A: 7E 8D FA        JMP     $8DFA                   
8E7D: 02 ; ????
8E7E: 10 FE F0 8E     LDS     $F08E                   
8E82: 25 ; ????
8E83: 10 CE 11 00     LDS     #$1100                  
8E87: A6 10           LDA     -16,X               
8E89: 27 17           BEQ     $8EA2                   
8E8B: A6 41           LDA     1,U                 
8E8D: A7 08           STA     8,X                 
8E8F: EC 42           LDD     2,U                 
8E91: ED 0A           STD     10,X                
8E93: EC 44           LDD     4,U                 
8E95: 5D              TSTB                        
8E96: 26 02           BNE     $8E9A                   
8E98: 1E 89           EXG     A,B                   
8E9A: A7 0D           STA     13,X                
8E9C: E7 0F           STB     15,X                
8E9E: 6F C4           CLR     ,U                  
8EA0: 6F 45           CLR     5,U                 
8EA2: 33 46           LEAU    6,U                 
8EA4: 30 88 20        LEAX    $20,X                 
8EA7: 8C 27 90        CMPX    #$2790                  
8EAA: 26 DB           BNE     $8E87                   
8EAC: 39              RTS                         
8EAD: 8E 25 10        LDX     #$2510                  
8EB0: CC 00 00        LDD     #$0000                  
8EB3: FD 10 34        STD     $1034                   
8EB6: 7C 10 34        INC     $1034                   
8EB9: A6 10           LDA     -16,X               
8EBB: 26 05           BNE     $8EC2                   
8EBD: 7C 10 35        INC     $1035                   
8EC0: 20 4C           BRA     $8F0E                   
8EC2: CE 11 00        LDU     #$1100                  
8EC5: E6 0D           LDB     13,X                
8EC7: 27 1B           BEQ     $8EE4                   
8EC9: 5F              CLRB                        
8ECA: B6 10 34        LDA     $1034                   
8ECD: B7 10 09        STA     $1009                   
8ED0: A6 0F           LDA     15,X                
8ED2: A1 45           CMPA    5,U                 
8ED4: 24 ; ????
8ED5: 04 6C           LSR     $6C                   
8ED7: C4 20           ANDB    #$20                  
8ED9: 01 ; ????
8EDA: 5C              INCB                        
8EDB: 7A 10 09        DEC     $1009                   
8EDE: 27 1B           BEQ     $8EFB                   
8EE0: 33 46           LEAU    6,U                 
8EE2: 20 EE           BRA     $8ED2                   
8EE4: B6 10 34        LDA     $1034                   
8EE7: 4A              DECA                        
8EE8: B7 10 CE        STA     $10CE                   
8EEB: 48 ; ????
8EEC: BB 10 CE        ADDA    $10CE                   
8EEF: 48 ; ????
8EF0: 33 C6           LEAU    A,U                 
8EF2: A6 0F           LDA     15,X                
8EF4: 1E 89           EXG     A,B                   
8EF6: 7C 10 35        INC     $1035                   
8EF9: 20 07           BRA     $8F02                   
8EFB: F0 10 35        SUBB    $1035                   
8EFE: E7 C4           STB     ,U                  
8F00: E6 0D           LDB     13,X                
8F02: E7 44           STB     4,U                 
8F04: A7 45           STA     5,U                 
8F06: A6 08           LDA     8,X                 
8F08: A7 41           STA     1,U                 
8F0A: EC 0A           LDD     10,X                
8F0C: ED 42           STD     2,U                 
8F0E: 30 88 20        LEAX    $20,X                 
8F11: 8C 27 90        CMPX    #$2790                  
8F14: 26 A0           BNE     $8EB6                   
8F16: 8E 25 10        LDX     #$2510                  
8F19: CE 11 78        LDU     #$1178                  
8F1C: 4F              CLRA                        
8F1D: E6 10           LDB     -16,X               
8F1F: 27 08           BEQ     $8F29                   
8F21: E6 0D           LDB     13,X                
8F23: 27 02           BEQ     $8F27                   
8F25: A7 C0           STA     ,U+                 
8F27: 6F 0C           CLR     12,X                
8F29: 4C              INCA                        
8F2A: 30 88 20        LEAX    $20,X                 
8F2D: 8C 27 90        CMPX    #$2790                  
8F30: 26 EB           BNE     $8F1D                   
8F32: CE 11 00        LDU     #$1100                  
8F35: A6 C4           LDA     ,U                  
8F37: 27 25           BEQ     $8F5E                   
8F39: 8E 11 77        LDX     #$1177                  
8F3C: E6 86           LDB     A,X                 
8F3E: 6F 86           CLR     A,X                 
8F40: 86 20           LDA     #$20                  
8F42: 3D              MUL                         
8F43: 8E 25 10        LDX     #$2510                  
8F46: 30 8B           LEAX    D,X                 
8F48: EC 42           LDD     2,U                 
8F4A: ED 0A           STD     10,X                
8F4C: EC 44           LDD     4,U                 
8F4E: A7 0D           STA     13,X                
8F50: CB F5           ADDB    #$F5                  
8F52: A6 41           LDA     1,U                 
8F54: 85 04           BITA    #$04                  
8F56: 27 02           BEQ     $8F5A                   
8F58: CB FB           ADDB    #$FB                  
8F5A: A7 08           STA     8,X                 
8F5C: E7 0F           STB     15,X                
8F5E: 33 46           LEAU    6,U                 
8F60: 11 83 11 78     CMPU    #$1178                  
8F64: 26 CF           BNE     $8F35                   
8F66: 39              RTS                         
8F67: 8E 19 1E        LDX     #$191E                  
8F6A: 10 8E 8F 80     LDY     #$8F80                  
8F6E: 86 16           LDA     #$16                  
8F70: B7 10 09        STA     $1009                   
8F73: EC A1           LDD     ,Y++                
8F75: ED 84           STD     ,X                  
8F77: 30 88 10        LEAX    $10,X                 
8F7A: 7A 10 09        DEC     $1009                   
8F7D: 26 F4           BNE     $8F73                   
8F7F: 39              RTS                         
8F80: 90 2B           SUBA    $2B                   
8F82: 8F ; ????
8F83: F3 8F AC        ADDD    $8FAC                   
8F86: 90 9C           SUBA    $9C                   
8F88: A0 8B           SUBA    D,X                 
8F8A: 9F 03           STX     $03                   
8F8C: A2 32           SBCA    -14,Y               
8F8E: A5 5B           BITA    -5,U                
8F90: A6 ; ????
8F91: 97 AA           STA     $AA                   
8F93: 6F ; ????
8F94: AA BD AB 85     ORA     [$3B1D,PC]              
8F98: A8 59           EORA    -7,U                
8F9A: 8D 48           BSR     $8FE4                   
8F9C: 8D FA           BSR     $8F98                   
8F9E: B6 E2 88        LDA     $E288                   
8FA1: 90 99           SUBA    $99                   
8FA3: 55 ; ????
8FA4: 94 E4           ANDA    $E4                   
8FA6: 94 38           ANDA    $38                   
8FA8: 9C B6           CMPX    $B6                   
8FAA: 9D 20           JSR     $20                   
8FAC: BD 81 50        JSR     $8150                   
8FAF: B6 10 1B        LDA     $101B                   
8FB2: 27 F8           BEQ     $8FAC                   
8FB4: B6 10 04        LDA     $1004                   
8FB7: B4 10 05        ANDA    $1005                   
8FBA: B4 10 06        ANDA    $1006                   
8FBD: C6 02           LDB     #$02                  
8FBF: 3D              MUL                         
8FC0: 8E 48 05        LDX     #$4805                  
8FC3: 3A              ABX                         
8FC4: F6 10 15        LDB     $1015                   
8FC7: 58 ; ????
8FC8: A6 84           LDA     ,X                  
8FCA: 84 02           ANDA    #$02                  
8FCC: 27 01           BEQ     $8FCF                   
8FCE: 5C              INCB                        
8FCF: C4 03           ANDB    #$03                  
8FD1: F7 10 15        STB     $1015                   
8FD4: A6 88 10        LDA     $10,X                 
8FD7: F6 40 4A        LDB     $404A                   
8FDA: 27 10           BEQ     $8FEC                   
8FDC: F6 10 14        LDB     $1014                   
8FDF: 58 ; ????
8FE0: 84 02           ANDA    #$02                  
8FE2: 27 01           BEQ     $8FE5                   
8FE4: 5C              INCB                        
8FE5: C4 03           ANDB    #$03                  
8FE7: F7 10 14        STB     $1014                   
8FEA: 20 C0           BRA     $8FAC                   
8FEC: 84 02           ANDA    #$02                  
8FEE: B7 10 14        STA     $1014                   
8FF1: 20 B9           BRA     $8FAC                   
8FF3: BD 81 50        JSR     $8150                   
8FF6: B6 10 1B        LDA     $101B                   
8FF9: 27 F8           BEQ     $8FF3                   
8FFB: B6 10 04        LDA     $1004                   
8FFE: B4 10 05        ANDA    $1005                   
9001: B4 10 06        ANDA    $1006                   
9004: C6 02           LDB     #$02                  
9006: 3D              MUL                         
9007: 8E 48 04        LDX     #$4804                  
900A: A6 85           LDA     B,X                 
900C: 84 0F           ANDA    #$0F                  
900E: B7 10 12        STA     $1012                   
9011: 8E 90 1B        LDX     #$901B                  
9014: E6 86           LDB     A,X                 
9016: F7 10 13        STB     $1013                   
9019: 20 D8           BRA     $8FF3                   
901B: FF 00 02        STU     $0002                   
901E: FF 04 FF        STU     $04FF                   
9021: FF FF 06        STU     $FF06                   
9024: FF FF FF        STU     $FFFF                   
9027: FF FF FF        STU     $FFFF                   
902A: FF BD 81        STU     $BD81                   
902D: 50              NEGB                        
902E: 8E 0F C7        LDX     #$0FC7                  
9031: 86 0D           LDA     #$0D                  
9033: C6 03           LDB     #$03                  
9035: BD 85 BD        JSR     $85BD                   
9038: 8E 0F DA        LDX     #$0FDA                  
903B: 86 0D           LDA     #$0D                  
903D: C6 03           LDB     #$03                  
903F: BD 85 BD        JSR     $85BD                   
9042: 8D 02           BSR     $9046                   
9044: 20 E5           BRA     $902B                   
9046: B6 10 0A        LDA     $100A                   
9049: 2A 01           BPL     $904C                   
904B: 39              RTS                         
904C: B6 10 01        LDA     $1001                   
904F: 84 0F           ANDA    #$0F                  
9051: 27 01           BEQ     $9054                   
9053: 39              RTS                         
9054: CE 07 DB        LDU     #$07DB                  
9057: 8E 07 C8        LDX     #$07C8                  
905A: F6 10 05        LDB     $1005                   
905D: 27 02           BEQ     $9061                   
905F: 1E 13           EXG     X,U                   
9061: 34 54           PSHS    U,X,B                   
9063: 8D 0F           BSR     $9074                   
9065: 35 54           PULS    B,X,U                   
9067: 1E 13           EXG     X,U                   
9069: C8 01           EORB    #$01                  
906B: 7D 10 04        TST     $1004                   
906E: 26 12           BNE     $9082                   
9070: C6 02           LDB     #$02                  
9072: 20 0E           BRA     $9082                   
9074: B6 10 01        LDA     $1001                   
9077: 44              LSRA                        
9078: 44              LSRA                        
9079: 44              LSRA                        
907A: 44              LSRA                        
907B: B4 10 0A        ANDA    $100A                   
907E: 27 02           BEQ     $9082                   
9080: C6 02           LDB     #$02                  
9082: 86 03           LDA     #$03                  
9084: 3D              MUL                         
9085: 8E 90 93        LDX     #$9093                  
9088: 3A              ABX                         
9089: C6 03           LDB     #$03                  
908B: A6 80           LDA     ,X+                 
908D: A7 C2           STA     ,-U                 
908F: 5A              DECB                        
9090: 26 F9           BNE     $908B                   
9092: 39              RTS                         
9093: 31 55           LEAY    -11,U               
9095: 50              NEGB                        
9096: 32 55           LEAS    -11,U               
9098: 50              NEGB                        
9099: 20 20           BRA     $90BB                   
909B: 20 BD           BRA     $905A                   
909D: 81 50           CMPA    #$50                  
909F: B6 10 10        LDA     $1010                   
90A2: 27 F8           BEQ     $909C                   
90A4: 8E 15 80        LDX     #$1580                  
90A7: CE 92 12        LDU     #$9212                  
90AA: 86 3C           LDA     #$3C                  
90AC: B7 10 09        STA     $1009                   
90AF: BD C1 08        JSR     $C108                   
90B2: 8E 16 3C        LDX     #$163C                  
90B5: CC 00 3C        LDD     #$003C                  
90B8: A7 82           STA     ,-X                 
90BA: 5A              DECB                        
90BB: 26 FB           BNE     $90B8                   
90BD: CE 92 4E        LDU     #$924E                  
90C0: BD C1 BD        JSR     $C1BD                   
90C3: 8E 13 78        LDX     #$1378                  
90C6: CC 00 00        LDD     #$0000                  
90C9: ED 83           STD     ,--X                
90CB: 8C 13 00        CMPX    #$1300                  
90CE: 26 F9           BNE     $90C9                   
90D0: BF 10 36        STX     $1036                   
90D3: CE 92 5B        LDU     #$925B                  
90D6: A6 5F           LDA     -1,U                
90D8: B7 10 09        STA     $1009                   
90DB: BD C8 03        JSR     $C803                   
90DE: BD C1 2A        JSR     $C12A                   
90E1: 8E 17 07        LDX     #$1707                  
90E4: CE 92 99        LDU     #$9299                  
90E7: BD C4 DB        JSR     $C4DB                   
90EA: 86 01           LDA     #$01                  
90EC: B7 25 00        STA     $2500                   
90EF: B7 10 D2        STA     $10D2                   
90F2: B7 10 D6        STA     $10D6                   
90F5: B7 10 D4        STA     $10D4                   
90F8: B7 40 B1        STA     $40B1                   
90FB: 8E 92 B2        LDX     #$92B2                  
90FE: EC 81           LDD     ,X++                
9100: B7 10 13        STA     $1013                   
9103: F7 10 60        STB     $1060                   
9106: BF 10 63        STX     $1063                   
9109: 8E 93 34        LDX     #$9334                  
910C: EC 81           LDD     ,X++                
910E: B7 10 14        STA     $1014                   
9111: F7 10 61        STB     $1061                   
9114: BF 10 65        STX     $1065                   
9117: 8E 93 84        LDX     #$9384                  
911A: EC 81           LDD     ,X++                
911C: B7 10 15        STA     $1015                   
911F: F7 10 62        STB     $1062                   
9122: BF 10 67        STX     $1067                   
9125: 8E 27 50        LDX     #$2750                  
9128: CC 88 78        LDD     #$8878                  
912B: A7 0F           STA     15,X                
912D: A7 88 2F        STA     $2F,X                 
9130: A7 0D           STA     13,X                
9132: E7 88 2D        STB     $2D,X                 
9135: 6F 0C           CLR     12,X                
9137: 6F 88 2C        CLR     $2C,X                 
913A: CC 3C 01        LDD     #$3C01                  
913D: ED 0A           STD     10,X                
913F: 86 3D           LDA     #$3D                  
9141: ED 88 2A        STD     $2A,X                 
9144: BD 81 50        JSR     $8150                   
9147: B6 10 10        LDA     $1010                   
914A: 27 52           BEQ     $919E                   
914C: FC 10 D0        LDD     $10D0                   
914F: 26 3B           BNE     $918C                   
9151: 7A 10 60        DEC     $1060                   
9154: 26 0E           BNE     $9164                   
9156: BE 10 63        LDX     $1063                   
9159: EC 81           LDD     ,X++                
915B: BF 10 63        STX     $1063                   
915E: B7 10 13        STA     $1013                   
9161: F7 10 60        STB     $1060                   
9164: 7A 10 61        DEC     $1061                   
9167: 26 0E           BNE     $9177                   
9169: BE 10 65        LDX     $1065                   
916C: EC 81           LDD     ,X++                
916E: BF 10 65        STX     $1065                   
9171: B7 10 14        STA     $1014                   
9174: F7 10 61        STB     $1061                   
9177: 7A 10 62        DEC     $1062                   
917A: 26 C8           BNE     $9144                   
917C: BE 10 67        LDX     $1067                   
917F: EC 81           LDD     ,X++                
9181: BF 10 67        STX     $1067                   
9184: B7 10 15        STA     $1015                   
9187: F7 10 62        STB     $1062                   
918A: 20 B8           BRA     $9144                   
918C: 86 4F           LDA     #$4F                  
918E: B7 10 4F        STA     $104F                   
9191: BD 81 50        JSR     $8150                   
9194: B6 10 10        LDA     $1010                   
9197: 27 05           BEQ     $919E                   
9199: 7A 10 4F        DEC     $104F                   
919C: 26 F3           BNE     $9191                   
919E: B6 40 54        LDA     $4054                   
91A1: B7 10 34        STA     $1034                   
91A4: CC 00 00        LDD     #$0000                  
91A7: 8E 14 00        LDX     #$1400                  
91AA: ED 81           STD     ,X++                
91AC: 8C 14 78        CMPX    #$1478                  
91AF: 26 F9           BNE     $91AA                   
91B1: B7 10 10        STA     $1010                   
91B4: B7 10 50        STA     $1050                   
91B7: B7 25 00        STA     $2500                   
91BA: B7 10 D2        STA     $10D2                   
91BD: FD 10 D0        STD     $10D0                   
91C0: B7 10 08        STA     $1008                   
91C3: FD 10 DC        STD     $10DC                   
91C6: B7 10 D6        STA     $10D6                   
91C9: B7 10 D9        STA     $10D9                   
91CC: B7 10 D4        STA     $10D4                   
91CF: B7 1F 60        STA     $1F60                   
91D2: B7 10 DA        STA     $10DA                   
91D5: B7 40 B1        STA     $40B1                   
91D8: B7 1F 02        STA     $1F02                   
91DB: B7 1F 1D        STA     $1F1D                   
91DE: 8E 40 40        LDX     #$4040                  
91E1: ED 81           STD     ,X++                
91E3: 8C 40 60        CMPX    #$4060                  
91E6: 26 F9           BNE     $91E1                   
91E8: B6 10 34        LDA     $1034                   
91EB: B7 40 54        STA     $4054                   
91EE: 8E 20 10        LDX     #$2010                  
91F1: A6 10           LDA     -16,X               
91F3: 27 03           BEQ     $91F8                   
91F5: BD 87 32        JSR     $8732                   
91F8: 30 88 20        LEAX    $20,X                 
91FB: 8C 24 D0        CMPX    #$24D0                  
91FE: 26 F1           BNE     $91F1                   
9200: BD A5 4F        JSR     $A54F                   
9203: 8E 27 50        LDX     #$2750                  
9206: BD 87 32        JSR     $8732                   
9209: 8E 27 70        LDX     #$2770                  
920C: BD 87 32        JSR     $8732                   
920F: 7E 90 9C        JMP     $909C                   
9212: AA ; ????
9213: AA ; ????
9214: AA ; ????
9215: AA ; ????
9216: AA ; ????
9217: AA ; ????
9218: AA ; ????
9219: AA ; ????
921A: AA ; ????
921B: AA ; ????
921C: AA ; ????
921D: AA ; ????
921E: AA ; ????
921F: AA ; ????
9220: AA ; ????
9221: AA A8 88        ORA     $88,Y                 
9224: 88 8B           EORA    #$8B                  
9226: A8 B8 88        EORA    [$88,Y]               
9229: 8B A8           ADDA    #$A8                  
922B: 88 88           EORA    #$88                  
922D: 8B A8           ADDA    #$A8                  
922F: 88 88           EORA    #$88                  
9231: 8B A8           ADDA    #$A8                  
9233: 88 88           EORA    #$88                  
9235: 8B A8           ADDA    #$A8                  
9237: 88 8B           EORA    #$8B                  
9239: 8B A8           ADDA    #$A8                  
923B: 88 88           EORA    #$88                  
923D: 8B AA           ADDA    #$AA                  
923F: AA ; ????
9240: AA ; ????
9241: AA ; ????
9242: AA ; ????
9243: AA ; ????
9244: AA ; ????
9245: AA ; ????
9246: AA ; ????
9247: AA ; ????
9248: AA ; ????
9249: AA ; ????
924A: AA ; ????
924B: AA ; ????
924C: AA ; ????
924D: AA 00           ORA     0,X                 
924F: 00 00           NEG     $00                   
9251: 38 ; ????
9252: 38 ; ????
9253: B8 80 00        EORA    $8000                   
9256: 20 00           BRA     $9258                   
9258: 00 00           NEG     $00                   
925A: 1F 04           TFR     D,X                   
925C: 22 05           BHI     $9263                   
925E: 23 01           BLS     $9261                   
9260: 24 ; ????
9261: 04 25           LSR     $25                   
9263: 01 ; ????
9264: 26 01           BNE     $9267                   
9266: 52 ; ????
9267: 04 2B           LSR     $2B                   
9269: 05 ; ????
926A: 2C 09           BGE     $9275                   
926C: 2D 08           BLT     $9276                   
926E: 2E 08           BGT     $9278                   
9270: 3A              ABX                         
9271: 04 32           LSR     $32                   
9273: 01 ; ????
9274: 33 02           LEAU    2,X                 
9276: 35 02           PULS    A                   
9278: 36 01           PSHU    CC                   
927A: 4C              INCA                        
927B: 02 ; ????
927C: 4E ; ????
927D: 08 ; ????
927E: 3B              RTI                         
927F: 0A 3C           DEC     $3C                   
9281: 08 ; ????
9282: 3D              MUL                         
9283: 08 ; ????
9284: 3E              RESET                       
9285: 04 51           LSR     $51                   
9287: 0A 42           DEC     $42                   
9289: 06 43           ROR     $43                   
928B: 03 44           COM     $44                   
928D: 02 ; ????
928E: 45 ; ????
928F: 0A 46           DEC     $46                   
9291: 04 49           LSR     $49                   
9293: 03 4A           COM     $4A                   
9295: 04 4B           LSR     $4B                   
9297: 08 ; ????
9298: 34 80           PSHS    PC                   
929A: 50              NEGB                        
929B: 47              ASRA                        
929C: 67 60           ASR     0,S                 
929E: 3C 22           CWAI    $22                   
92A0: A6 ; ????
92A1: CA 4E           ORB     #$4E                  
92A3: 2E AD           BGT     $9252                   
92A5: 4C              INCA                        
92A6: 00 00           NEG     $00                   
92A8: 00 07           NEG     $07                   
92AA: 0F 01           CLR     $01                   
92AC: 10 FF 01 50     STS     $0150                   
92B0: 50              NEGB                        
92B1: FF FF 40        STU     $FF40                   
92B4: 02 ; ????
92B5: 10 ; ????
92B6: 04 10           LSR     $10                   
92B8: 04 10           LSR     $10                   
92BA: 04 10           LSR     $10                   
92BC: 04 30           LSR     $30                   
92BE: 04 30           LSR     $30                   
92C0: 06 30           ROR     $30                   
92C2: 06 07           ROR     $07                   
92C4: FF 80 FF        STU     $80FF                   
92C7: 30 06           LEAX    6,X                 
92C9: 40              NEGA                        
92CA: 00 40           NEG     $40                   
92CC: 02 ; ????
92CD: 50              NEGB                        
92CE: 00 80           NEG     $80                   
92D0: 00 90           NEG     $90                   
92D2: 02 ; ????
92D3: 10 ; ????
92D4: 04 80           LSR     $80                   
92D6: 02 ; ????
92D7: 40              NEGA                        
92D8: 04 40           LSR     $40                   
92DA: 06 40           ROR     $40                   
92DC: 00 20           NEG     $20                   
92DE: 02 ; ????
92DF: 40              NEGA                        
92E0: 00 60           NEG     $60                   
92E2: 04 30           LSR     $30                   
92E4: 06 20           ROR     $20                   
92E6: 02 ; ????
92E7: 40              NEGA                        
92E8: 00 20           NEG     $20                   
92EA: 02 ; ????
92EB: 40              NEGA                        
92EC: 04 20           LSR     $20                   
92EE: 04 40           LSR     $40                   
92F0: 06 80           ROR     $80                   
92F2: 00 80           NEG     $80                   
92F4: 06 40           ROR     $40                   
92F6: 02 ; ????
92F7: 40              NEGA                        
92F8: 04 80           LSR     $80                   
92FA: 02 ; ????
92FB: 80 04           SUBA    #$04                  
92FD: F0 06 50        SUBB    $0650                   
9300: 00 FF           NEG     $FF                   
9302: FF FF FF        STU     $FFFF                   
9305: FF FF FF        STU     $FFFF                   
9308: FF FF FF        STU     $FFFF                   
930B: FF FF FF        STU     $FFFF                   
930E: FF FF FF        STU     $FFFF                   
9311: FF FF FF        STU     $FFFF                   
9314: FF FF FF        STU     $FFFF                   
9317: FF FF FF        STU     $FFFF                   
931A: FF FF FF        STU     $FFFF                   
931D: FF FF FF        STU     $FFFF                   
9320: FF FF FF        STU     $FFFF                   
9323: FF FF FF        STU     $FFFF                   
9326: FF FF FF        STU     $FFFF                   
9329: FF FF FF        STU     $FFFF                   
932C: FF FF FF        STU     $FFFF                   
932F: FF FF FF        STU     $FFFF                   
9332: FF FF 00        STU     $FF00                   
9335: 40              NEGA                        
9336: 00 10           NEG     $10                   
9338: 00 10           NEG     $10                   
933A: 01 ; ????
933B: 10 ; ????
933C: 00 10           NEG     $10                   
933E: 01 ; ????
933F: 30 00           LEAX    0,X                 
9341: 30 00           LEAX    0,X                 
9343: 30 00           LEAX    0,X                 
9345: 87 ; ????
9346: 00 70           NEG     $70                   
9348: 00 90           NEG     $90                   
934A: 00 40           NEG     $40                   
934C: 01 ; ????
934D: 90 00           SUBA    $00                   
934F: 40              NEGA                        
9350: 00 F0           NEG     $F0                   
9352: 00 F0           NEG     $F0                   
9354: 01 ; ????
9355: 60 00           NEG     0,X                 
9357: 80 00           SUBA    #$00                  
9359: 80 01           SUBA    #$01                  
935B: 80 00           SUBA    #$00                  
935D: 40              NEGA                        
935E: 01 ; ????
935F: 80 00           SUBA    #$00                  
9361: A0 01           SUBA    1,X                 
9363: 60 00           NEG     0,X                 
9365: 40              NEGA                        
9366: 01 ; ????
9367: 50              NEGB                        
9368: 00 FF           NEG     $FF                   
936A: 00 FF           NEG     $FF                   
936C: 00 FF           NEG     $FF                   
936E: 00 FF           NEG     $FF                   
9370: 00 FF           NEG     $FF                   
9372: 00 FF           NEG     $FF                   
9374: 00 FF           NEG     $FF                   
9376: 00 FF           NEG     $FF                   
9378: 00 FF           NEG     $FF                   
937A: 00 FF           NEG     $FF                   
937C: 00 FF           NEG     $FF                   
937E: 00 FF           NEG     $FF                   
9380: 00 FF           NEG     $FF                   
9382: 00 FF           NEG     $FF                   
9384: 00 40           NEG     $40                   
9386: 00 10           NEG     $10                   
9388: 00 10           NEG     $10                   
938A: 00 10           NEG     $10                   
938C: 00 10           NEG     $10                   
938E: 00 30           NEG     $30                   
9390: 00 30           NEG     $30                   
9392: 00 30           NEG     $30                   
9394: 00 07           NEG     $07                   
9396: 01 ; ????
9397: 01 ; ????
9398: 03 7F           COM     $7F                   
939A: 00 70           NEG     $70                   
939C: 00 F0           NEG     $F0                   
939E: 00 D0           NEG     $D0                   
93A0: 01 ; ????
93A1: 01 ; ????
93A2: 03 08           COM     $08                   
93A4: 01 ; ????
93A5: 01 ; ????
93A6: 03 08           COM     $08                   
93A8: 01 ; ????
93A9: 01 ; ????
93AA: 03 08           COM     $08                   
93AC: 03 08           COM     $08                   
93AE: 01 ; ????
93AF: 01 ; ????
93B0: 03 08           COM     $08                   
93B2: 01 ; ????
93B3: 01 ; ????
93B4: 00 80           NEG     $80                   
93B6: 01 ; ????
93B7: 01 ; ????
93B8: 03 08           COM     $08                   
93BA: 01 ; ????
93BB: 01 ; ????
93BC: 03 08           COM     $08                   
93BE: 01 ; ????
93BF: 01 ; ????
93C0: 03 08           COM     $08                   
93C2: 01 ; ????
93C3: 01 ; ????
93C4: 03 08           COM     $08                   
93C6: 01 ; ????
93C7: 01 ; ????
93C8: 03 08           COM     $08                   
93CA: 00 A0           NEG     $A0                   
93CC: 01 ; ????
93CD: 01 ; ????
93CE: 03 08           COM     $08                   
93D0: 01 ; ????
93D1: 01 ; ????
93D2: 03 08           COM     $08                   
93D4: 01 ; ????
93D5: 01 ; ????
93D6: 03 08           COM     $08                   
93D8: 01 ; ????
93D9: 01 ; ????
93DA: 03 08           COM     $08                   
93DC: 01 ; ????
93DD: 01 ; ????
93DE: 03 08           COM     $08                   
93E0: 00 80           NEG     $80                   
93E2: 01 ; ????
93E3: 01 ; ????
93E4: 03 08           COM     $08                   
93E6: 01 ; ????
93E7: 01 ; ????
93E8: 03 08           COM     $08                   
93EA: 01 ; ????
93EB: 01 ; ????
93EC: 03 08           COM     $08                   
93EE: 01 ; ????
93EF: 01 ; ????
93F0: 03 08           COM     $08                   
93F2: 01 ; ????
93F3: 01 ; ????
93F4: 03 08           COM     $08                   
93F6: 01 ; ????
93F7: 01 ; ????
93F8: 03 08           COM     $08                   
93FA: 00 FF           NEG     $FF                   
93FC: 00 FF           NEG     $FF                   
93FE: 00 FF           NEG     $FF                   
9400: 00 FF           NEG     $FF                   
9402: 00 FF           NEG     $FF                   
9404: 00 FF           NEG     $FF                   
9406: 00 FF           NEG     $FF                   
9408: 00 FF           NEG     $FF                   
940A: 00 FF           NEG     $FF                   
940C: 00 FF           NEG     $FF                   
940E: 00 FF           NEG     $FF                   
9410: 00 FF           NEG     $FF                   
9412: 00 FF           NEG     $FF                   
9414: 00 FF           NEG     $FF                   
9416: 00 FF           NEG     $FF                   
9418: 00 FF           NEG     $FF                   
941A: 00 FF           NEG     $FF                   
941C: 00 FF           NEG     $FF                   
941E: 00 FF           NEG     $FF                   
9420: 00 FF           NEG     $FF                   
9422: 00 FF           NEG     $FF                   
9424: 00 FF           NEG     $FF                   
9426: 00 FF           NEG     $FF                   
9428: 00 FF           NEG     $FF                   
942A: 00 FF           NEG     $FF                   
942C: 00 FF           NEG     $FF                   
942E: 00 FF           NEG     $FF                   
9430: 00 FF           NEG     $FF                   
9432: 00 FF           NEG     $FF                   
9434: 00 FF           NEG     $FF                   
9436: 00 FF           NEG     $FF                   
9438: BD 81 50        JSR     $8150                   
943B: B6 10 D4        LDA     $10D4                   
943E: 27 F8           BEQ     $9438                   
9440: 8E 00 00        LDX     #$0000                  
9443: F6 10 08        LDB     $1008                   
9446: C4 F8           ANDB    #$F8                  
9448: 4F              CLRA                        
9449: 58 ; ????
944A: 49              ROLA                        
944B: 58 ; ????
944C: 49              ROLA                        
944D: 30 8B           LEAX    D,X                 
944F: BF 10 36        STX     $1036                   
9452: F6 10 01        LDB     $1001                   
9455: C4 1F           ANDB    #$1F                  
9457: 3A              ABX                         
9458: C6 1F           LDB     #$1F                  
945A: F7 10 09        STB     $1009                   
945D: A6 89 08 00     LDA     $0800,X                 
9461: 2A 06           BPL     $9469                   
9463: 84 3F           ANDA    #$3F                  
9465: A7 89 08 00     STA     $0800,X                 
9469: 30 88 20        LEAX    $20,X                 
946C: 5A              DECB                        
946D: 26 EE           BNE     $945D                   
946F: B6 10 6C        LDA     $106C                   
9472: BB 10 6D        ADDA    $106D                   
9475: 24 ; ????
9476: 2E B7           BGT     $942F                   
9478: 10 ; ????
9479: 6D ; ????
947A: BE 10 36        LDX     $1036                   
947D: B6 10 11        LDA     $1011                   
9480: 48 ; ????
9481: 48 ; ????
9482: 48 ; ????
9483: B8 10 11        EORA    $1011                   
9486: 43              COMA                        
9487: 48 ; ????
9488: 79 10 11        ROL     $1011                   
948B: B6 10 11        LDA     $1011                   
948E: 84 1F           ANDA    #$1F                  
9490: E6 86           LDB     A,X                 
9492: C1 FC           CMPB    #$FC                  
9494: 25 ; ????
9495: 05 ; ????
9496: 5C              INCB                        
9497: CA FC           ORB     #$FC                  
9499: E7 86           STB     A,X                 
949B: 7A 10 09        DEC     $1009                   
949E: 27 08           BEQ     $94A8                   
94A0: 30 88 20        LEAX    $20,X                 
94A3: 20 D8           BRA     $947D                   
94A5: B7 10 6D        STA     $106D                   
94A8: B6 10 50        LDA     $1050                   
94AB: BA 10 D9        ORA     $10D9                   
94AE: BA 10 D7        ORA     $10D7                   
94B1: BA 10 E6        ORA     $10E6                   
94B4: BA 10 D0        ORA     $10D0                   
94B7: BA 10 D1        ORA     $10D1                   
94BA: BA 10 DA        ORA     $10DA                   
94BD: 10 26 FF 77     LBNE    $9438                   
94C1: 7C 10 EC        INC     $10EC                   
94C4: 7C 10 EB        INC     $10EB                   
94C7: BD CC 7F        JSR     $CC7F                   
94CA: 7F 10 EC        CLR     $10EC                   
94CD: B6 10 CB        LDA     $10CB                   
94D0: 10 27 FF 64     LBEQ    $9438                   
94D4: 7C 10 E6        INC     $10E6                   
94D7: 7E 94 38        JMP     $9438                   
94DA: 80 80           SUBA    #$80                  
94DC: 80 80           SUBA    #$80                  
94DE: 80 40           SUBA    #$40                  
94E0: 20 10           BRA     $94F2                   
94E2: 05 ; ????
94E3: 05 ; ????
94E4: BD 81 50        JSR     $8150                   
94E7: B6 10 E3        LDA     $10E3                   
94EA: 27 F8           BEQ     $94E4                   
94EC: 8E 20 10        LDX     #$2010                  
94EF: B6 40 44        LDA     $4044                   
94F2: 26 64           BNE     $9558                   
94F4: CE 99 3B        LDU     #$993B                  
94F7: EC C1           LDD     ,U++                
94F9: A7 0F           STA     15,X                
94FB: E7 0D           STB     13,X                
94FD: A6 C0           LDA     ,U+                 
94FF: A7 0A           STA     10,X                
9501: 6C 0B           INC     11,X                
9503: 6F 0C           CLR     12,X                
9505: 30 88 20        LEAX    $20,X                 
9508: 8C 20 90        CMPX    #$2090                  
950B: 26 EA           BNE     $94F7                   
950D: 8E 20 10        LDX     #$2010                  
9510: CE 99 47        LDU     #$9947                  
9513: EF 15           STU     -11,X               
9515: CC 04 08        LDD     #$0408                  
9518: A7 88 1A        STA     $1A,X                 
951B: E7 88 3A        STB     $3A,X                 
951E: CC 02 B4        LDD     #$02B4                  
9521: A7 88 48        STA     $48,X                 
9524: E7 88 44        STB     $44,X                 
9527: BD 81 50        JSR     $8150                   
952A: B6 10 E3        LDA     $10E3                   
952D: 27 15           BEQ     $9544                   
952F: 8E 20 10        LDX     #$2010                  
9532: CE 96 1D        LDU     #$961D                  
9535: A6 1A           LDA     -6,X                
9537: 48 ; ????
9538: AD D6           JSR     [A,U]               
953A: 30 88 20        LEAX    $20,X                 
953D: 8C 20 70        CMPX    #$2070                  
9540: 26 F3           BNE     $9535                   
9542: 20 E3           BRA     $9527                   
9544: 8E 20 10        LDX     #$2010                  
9547: A6 0D           LDA     13,X                
9549: 27 03           BEQ     $954E                   
954B: BD 87 32        JSR     $8732                   
954E: 30 88 20        LEAX    $20,X                 
9551: 8C 21 B0        CMPX    #$21B0                  
9554: 26 F1           BNE     $9547                   
9556: 20 8C           BRA     $94E4                   
9558: 10 8E 99 33     LDY     #$9933                  
955C: BD 8A A0        JSR     $8AA0                   
955F: 84 7E           ANDA    #$7E                  
9561: 8B 30           ADDA    #$30                  
9563: A7 0F           STA     15,X                
9565: BD 8A A0        JSR     $8AA0                   
9568: 84 7E           ANDA    #$7E                  
956A: 8B 30           ADDA    #$30                  
956C: A7 0D           STA     13,X                
956E: BD 8A A0        JSR     $8AA0                   
9571: 84 07           ANDA    #$07                  
9573: A7 05           STA     5,X                 
9575: E6 05           LDB     5,X                 
9577: BD 8A A0        JSR     $8AA0                   
957A: 84 08           ANDA    #$08                  
957C: AB A5           ADDA    B,Y                 
957E: A7 0A           STA     10,X                
9580: CE 99 13        LDU     #$9913                  
9583: 58 ; ????
9584: 58 ; ????
9585: 33 C5           LEAU    B,U                 
9587: EC C1           LDD     ,U++                
9589: ED 11           STD     -15,X               
958B: EC C4           LDD     ,U                  
958D: ED 13           STD     -13,X               
958F: CC 00 01        LDD     #$0001                  
9592: A7 08           STA     8,X                 
9594: A7 0C           STA     12,X                
9596: E7 0B           STB     11,X                
9598: 30 88 20        LEAX    $20,X                 
959B: 8C 20 B0        CMPX    #$20B0                  
959E: 26 BC           BNE     $955C                   
95A0: BD 81 50        JSR     $8150                   
95A3: B6 10 E3        LDA     $10E3                   
95A6: 27 64           BEQ     $960C                   
95A8: B6 10 01        LDA     $1001                   
95AB: 84 04           ANDA    #$04                  
95AD: 44              LSRA                        
95AE: 44              LSRA                        
95AF: B7 10 34        STA     $1034                   
95B2: 8E 20 10        LDX     #$2010                  
95B5: EC 11           LDD     -15,X               
95B7: AB 0F           ADDA    15,X                
95B9: A1 13           CMPA    -13,X               
95BB: 27 17           BEQ     $95D4                   
95BD: A7 0F           STA     15,X                
95BF: EB 0D           ADDB    13,X                
95C1: E1 14           CMPB    -12,X               
95C3: 27 0F           BEQ     $95D4                   
95C5: E7 0D           STB     13,X                
95C7: A6 0A           LDA     10,X                
95C9: 81 6A           CMPA    #$6A                  
95CB: 24 ; ????
95CC: 33 84           LEAU    ,X                  
95CE: 1E BA           EXG     DP,CC                   
95D0: 10 ; ????
95D1: 34 20           PSHS    Y                   
95D3: 2A A6           BPL     $957B                   
95D5: 05 ; ????
95D6: CE 99 13        LDU     #$9913                  
95D9: 85 01           BITA    #$01                  
95DB: 26 02           BNE     $95DF                   
95DD: 8B 02           ADDA    #$02                  
95DF: 8B 02           ADDA    #$02                  
95E1: 84 07           ANDA    #$07                  
95E3: A7 05           STA     5,X                 
95E5: 48 ; ????
95E6: 48 ; ????
95E7: 33 C6           LEAU    A,U                 
95E9: EC C1           LDD     ,U++                
95EB: ED 11           STD     -15,X               
95ED: EC C4           LDD     ,U                  
95EF: ED 13           STD     -13,X               
95F1: A6 0A           LDA     10,X                
95F3: 81 6A           CMPA    #$6A                  
95F5: 24 ; ????
95F6: 09 84           ROL     $84                   
95F8: 08 ; ????
95F9: 44              LSRA                        
95FA: 44              LSRA                        
95FB: 44              LSRA                        
95FC: 8B 6A           ADDA    #$6A                  
95FE: A7 0A           STA     10,X                
9600: 6F 0C           CLR     12,X                
9602: 30 88 20        LEAX    $20,X                 
9605: 8C 20 B0        CMPX    #$20B0                  
9608: 26 AB           BNE     $95B5                   
960A: 20 94           BRA     $95A0                   
960C: 8E 20 10        LDX     #$2010                  
960F: BD 87 32        JSR     $8732                   
9612: 30 88 20        LEAX    $20,X                 
9615: 8C 20 B0        CMPX    #$20B0                  
9618: 26 F5           BNE     $960F                   
961A: 7E 94 E4        JMP     $94E4                   
961D: 96 39           LDA     $39                   
961F: 96 7F           LDA     $7F                   
9621: 96 8C           LDA     $8C                   
9623: 99 11           ADCA    $11                   
9625: 96 E3           LDA     $E3                   
9627: 97 29           STA     $29                   
9629: 97 41           STA     $41                   
962B: 97 6C           STA     $6C                   
962D: 97 81           STA     $81                   
962F: 97 93           STA     $93                   
9631: 97 DC           STA     $DC                   
9633: 98 2C           EORA    $2C                   
9635: 98 84           EORA    $84                   
9637: 98 E9           EORA    $E9                   
9639: A6 0D           LDA     13,X                
963B: 4A              DECA                        
963C: A7 0D           STA     13,X                
963E: 81 B0           CMPA    #$B0                  
9640: 27 0E           BEQ     $9650                   
9642: B6 10 01        LDA     $1001                   
9645: 84 0C           ANDA    #$0C                  
9647: 44              LSRA                        
9648: 44              LSRA                        
9649: 8B 04           ADDA    #$04                  
964B: A7 0A           STA     10,X                
964D: 6F 0C           CLR     12,X                
964F: 39              RTS                         
9650: 6C 1A           INC     -6,X                
9652: CC 79 05        LDD     #$7905                  
9655: ED 0A           STD     10,X                
9657: A6 04           LDA     4,X                 
9659: C6 20           LDB     #$20                  
965B: 3D              MUL                         
965C: CE 21 50        LDU     #$2150                  
965F: 33 CB           LEAU    D,U                 
9661: 10 AE 15        LDY     -11,X               
9664: EC A1           LDD     ,Y++                
9666: 10 AF 15        STY     -11,X               
9669: ED 4A           STD     10,U                
966B: A6 0F           LDA     15,X                
966D: A7 4F           STA     15,U                
966F: A6 0D           LDA     13,X                
9671: A7 4D           STA     13,U                
9673: CC 00 08        LDD     #$0008                  
9676: A7 4C           STA     12,U                
9678: E7 1B           STB     -5,X                
967A: 6C 04           INC     4,X                 
967C: CE 96 1D        LDU     #$961D                  
967F: 86 FE           LDA     #$FE                  
9681: AB 0D           ADDA    13,X                
9683: A7 0D           STA     13,X                
9685: 6F 0C           CLR     12,X                
9687: 6A 1B           DEC     -5,X                
9689: 27 20           BEQ     $96AB                   
968B: 39              RTS                         
968C: CC 04 02        LDD     #$0402                  
968F: B4 10 01        ANDA    $1001                   
9692: 44              LSRA                        
9693: 44              LSRA                        
9694: 8B 4A           ADDA    #$4A                  
9696: A7 89 01 4A     STA     $014A,X                 
969A: F4 10 01        ANDB    $1001                   
969D: 54              LSRB                        
969E: CB 06           ADDB    #$06                  
96A0: E7 0B           STB     11,X                
96A2: E7 89 01 6B     STB     $016B,X                 
96A6: E7 89 01 8B     STB     $018B,X                 
96AA: 39              RTS                         
96AB: A6 04           LDA     4,X                 
96AD: 81 03           CMPA    #$03                  
96AF: 26 A8           BNE     $9659                   
96B1: CC 01 08        LDD     #$0108                  
96B4: A7 04           STA     4,X                 
96B6: A7 1A           STA     -6,X                
96B8: E7 1B           STB     -5,X                
96BA: CC 00 B0        LDD     #$00B0                  
96BD: A7 0C           STA     12,X                
96BF: E7 0D           STB     13,X                
96C1: CC 79 05        LDD     #$7905                  
96C4: ED 0A           STD     10,X                
96C6: 86 4A           LDA     #$4A                  
96C8: A7 89 01 4A     STA     $014A,X                 
96CC: 10 8E 99 49     LDY     #$9949                  
96D0: 10 AF 15        STY     -11,X               
96D3: 8E 21 70        LDX     #$2170                  
96D6: BD 87 32        JSR     $8732                   
96D9: 8E 21 90        LDX     #$2190                  
96DC: BD 87 32        JSR     $8732                   
96DF: 8E 20 10        LDX     #$2010                  
96E2: 39              RTS                         
96E3: 6C 0D           INC     13,X                
96E5: A6 88 ED        LDA     $ED,X                 
96E8: A0 0D           SUBA    13,X                
96EA: 81 08           CMPA    #$08                  
96EC: 23 16           BLS     $9704                   
96EE: B6 10 01        LDA     $1001                   
96F1: 84 04           ANDA    #$04                  
96F3: 44              LSRA                        
96F4: 44              LSRA                        
96F5: B7 10 34        STA     $1034                   
96F8: A6 0A           LDA     10,X                
96FA: 84 1E           ANDA    #$1E                  
96FC: BB 10 34        ADDA    $1034                   
96FF: A7 0A           STA     10,X                
9701: 6F 0C           CLR     12,X                
9703: 39              RTS                         
9704: 86 02           LDA     #$02                  
9706: A7 88 DA        STA     $DA,X                 
9709: 6C 1A           INC     -6,X                
970B: CC 03 24        LDD     #$0324                  
970E: A7 04           STA     4,X                 
9710: E7 1B           STB     -5,X                
9712: 10 8E 99 4D     LDY     #$994D                  
9716: A6 0A           LDA     10,X                
9718: 84 08           ANDA    #$08                  
971A: 44              LSRA                        
971B: 31 A6           LEAY    A,Y                 
971D: 10 AF 15        STY     -11,X               
9720: 44              LSRA                        
9721: 44              LSRA                        
9722: 8B 6A           ADDA    #$6A                  
9724: A7 0A           STA     10,X                
9726: 6F 0C           CLR     12,X                
9728: 39              RTS                         
9729: 6A 1B           DEC     -5,X                
972B: 27 01           BEQ     $972E                   
972D: 39              RTS                         
972E: CC 24 0C        LDD     #$240C                  
9731: A7 1B           STA     -5,X                
9733: E7 08           STB     8,X                 
9735: A6 0F           LDA     15,X                
9737: 8B F8           ADDA    #$F8                  
9739: A7 0F           STA     15,X                
973B: 6F 0C           CLR     12,X                
973D: 6C 1A           INC     -6,X                
973F: 20 0D           BRA     $974E                   
9741: 6A 1B           DEC     -5,X                
9743: 27 01           BEQ     $9746                   
9745: 39              RTS                         
9746: 6A 04           DEC     4,X                 
9748: 27 0F           BEQ     $9759                   
974A: 86 0F           LDA     #$0F                  
974C: A7 1B           STA     -5,X                
974E: 10 AE 15        LDY     -11,X               
9751: A6 A0           LDA     ,Y+                 
9753: 10 AF 15        STY     -11,X               
9756: A7 0A           STA     10,X                
9758: 39              RTS                         
9759: CC 00 07        LDD     #$0007                  
975C: A7 0D           STA     13,X                
975E: A7 0C           STA     12,X                
9760: E7 1A           STB     -6,X                
9762: 8E 20 10        LDX     #$2010                  
9765: BD 96 B1        JSR     $96B1                   
9768: 8E 20 30        LDX     #$2030                  
976B: 39              RTS                         
976C: CC 04 00        LDD     #$0400                  
976F: A7 1A           STA     -6,X                
9771: A6 98 F5        LDA     [$F5,X]               
9774: A7 0A           STA     10,X                
9776: E7 0C           STB     12,X                
9778: E7 08           STB     8,X                 
977A: 86 08           LDA     #$08                  
977C: AB 0F           ADDA    15,X                
977E: A7 0F           STA     15,X                
9780: 39              RTS                         
9781: 6A 04           DEC     4,X                 
9783: 27 01           BEQ     $9786                   
9785: 39              RTS                         
9786: 6C 1A           INC     -6,X                
9788: CC 3F 69        LDD     #$3F69                  
978B: A7 04           STA     4,X                 
978D: E7 0A           STB     10,X                
978F: E7 88 2A        STB     $2A,X                 
9792: 39              RTS                         
9793: 6A 04           DEC     4,X                 
9795: 27 12           BEQ     $97A9                   
9797: A6 04           LDA     4,X                 
9799: 85 04           BITA    #$04                  
979B: 26 04           BNE     $97A1                   
979D: 86 1A           LDA     #$1A                  
979F: 20 02           BRA     $97A3                   
97A1: 86 69           LDA     #$69                  
97A3: A7 0A           STA     10,X                
97A5: A7 88 2A        STA     $2A,X                 
97A8: 39              RTS                         
97A9: 6C 1A           INC     -6,X                
97AB: CC 40 C0        LDD     #$40C0                  
97AE: A7 88 4D        STA     $4D,X                 
97B1: E7 88 6D        STB     $6D,X                 
97B4: 86 5A           LDA     #$5A                  
97B6: A7 0A           STA     10,X                
97B8: A7 88 2A        STA     $2A,X                 
97BB: CC 58 01        LDD     #$5801                  
97BE: ED 88 4A        STD     $4A,X                 
97C1: ED 88 6A        STD     $6A,X                 
97C4: CC 02 A8        LDD     #$02A8                  
97C7: A7 88 48        STA     $48,X                 
97CA: E7 88 4F        STB     $4F,X                 
97CD: E7 88 6F        STB     $6F,X                 
97D0: CC 00 05        LDD     #$0005                  
97D3: A7 88 4C        STA     $4C,X                 
97D6: A7 88 6C        STA     $6C,X                 
97D9: E7 04           STB     4,X                 
97DB: 39              RTS                         
97DC: 6A 04           DEC     4,X                 
97DE: 27 01           BEQ     $97E1                   
97E0: 39              RTS                         
97E1: 6C 1A           INC     -6,X                
97E3: CC 5B 59        LDD     #$5B59                  
97E6: A7 0A           STA     10,X                
97E8: A7 88 2A        STA     $2A,X                 
97EB: E7 88 4A        STB     $4A,X                 
97EE: E7 88 6A        STB     $6A,X                 
97F1: CC 50 B0        LDD     #$50B0                  
97F4: A7 89 00 8D     STA     $008D,X                 
97F8: E7 89 00 AD     STB     $00AD,X                 
97FC: CC 02 A8        LDD     #$02A8                  
97FF: A7 89 00 88     STA     $0088,X                 
9803: E7 89 00 8F     STB     $008F,X                 
9807: E7 89 00 AF     STB     $00AF,X                 
980B: CC 00 68        LDD     #$0068                  
980E: A7 89 00 8C     STA     $008C,X                 
9812: A7 89 00 AC     STA     $00AC,X                 
9816: E7 89 00 8A     STB     $008A,X                 
981A: E7 89 00 AA     STB     $00AA,X                 
981E: CC 01 07        LDD     #$0107                  
9821: A7 89 00 8B     STA     $008B,X                 
9825: A7 89 00 AB     STA     $00AB,X                 
9829: E7 04           STB     4,X                 
982B: 39              RTS                         
982C: 6A 04           DEC     4,X                 
982E: 27 01           BEQ     $9831                   
9830: 39              RTS                         
9831: 6C 1A           INC     -6,X                
9833: CC 60 A0        LDD     #$60A0                  
9836: A7 89 00 CD     STA     $00CD,X                 
983A: E7 89 00 ED     STB     $00ED,X                 
983E: CC 02 A8        LDD     #$02A8                  
9841: A7 89 00 C8     STA     $00C8,X                 
9845: E7 89 00 CF     STB     $00CF,X                 
9849: E7 89 00 EF     STB     $00EF,X                 
984D: CC 00 3F        LDD     #$003F                  
9850: A7 89 00 CC     STA     $00CC,X                 
9854: A7 89 00 EC     STA     $00EC,X                 
9858: E7 04           STB     4,X                 
985A: CC 5E 5C        LDD     #$5E5C                  
985D: A7 0A           STA     10,X                
985F: A7 88 2A        STA     $2A,X                 
9862: E7 88 4A        STB     $4A,X                 
9865: E7 88 6A        STB     $6A,X                 
9868: CC 63 61        LDD     #$6361                  
986B: A7 89 00 8A     STA     $008A,X                 
986F: A7 89 00 AA     STA     $00AA,X                 
9873: E7 89 00 CA     STB     $00CA,X                 
9877: E7 89 00 EA     STB     $00EA,X                 
987B: 6C 89 00 CB     INC     $00CB,X                 
987F: 6C 89 00 EB     INC     $00EB,X                 
9883: 39              RTS                         
9884: 6A 04           DEC     4,X                 
9886: 27 39           BEQ     $98C1                   
9888: A6 04           LDA     4,X                 
988A: 84 04           ANDA    #$04                  
988C: 44              LSRA                        
988D: 44              LSRA                        
988E: B7 10 34        STA     $1034                   
9891: A6 0A           LDA     10,X                
9893: 84 5E           ANDA    #$5E                  
9895: BA 10 34        ORA     $1034                   
9898: A7 0A           STA     10,X                
989A: A7 88 2A        STA     $2A,X                 
989D: 80 02           SUBA    #$02                  
989F: A7 88 4A        STA     $4A,X                 
98A2: A7 88 6A        STA     $6A,X                 
98A5: 86 03           LDA     #$03                  
98A7: BB 10 34        ADDA    $1034                   
98AA: 84 05           ANDA    #$05                  
98AC: 8A 60           ORA     #$60                  
98AE: A7 89 00 CA     STA     $00CA,X                 
98B2: A7 89 00 EA     STA     $00EA,X                 
98B6: 8B 02           ADDA    #$02                  
98B8: A7 89 00 8A     STA     $008A,X                 
98BC: A7 89 00 AA     STA     $00AA,X                 
98C0: 39              RTS                         
98C1: 6C 1A           INC     -6,X                
98C3: CC 62 60        LDD     #$6260                  
98C6: A7 0A           STA     10,X                
98C8: A7 88 2A        STA     $2A,X                 
98CB: E7 88 4A        STB     $4A,X                 
98CE: E7 88 6A        STB     $6A,X                 
98D1: CC 67 65        LDD     #$6765                  
98D4: A7 89 00 8A     STA     $008A,X                 
98D8: A7 89 00 AA     STA     $00AA,X                 
98DC: E7 89 00 CA     STB     $00CA,X                 
98E0: E7 89 00 EA     STB     $00EA,X                 
98E4: 86 07           LDA     #$07                  
98E6: A7 04           STA     4,X                 
98E8: 39              RTS                         
98E9: 6A 04           DEC     4,X                 
98EB: 27 01           BEQ     $98EE                   
98ED: 39              RTS                         
98EE: BF 10 36        STX     $1036                   
98F1: 8E 20 90        LDX     #$2090                  
98F4: BD 87 32        JSR     $8732                   
98F7: 30 88 20        LEAX    $20,X                 
98FA: 8C 21 50        CMPX    #$2150                  
98FD: 26 F5           BNE     $98F4                   
98FF: BE 10 36        LDX     $1036                   
9902: 86 1A           LDA     #$1A                  
9904: A7 0A           STA     10,X                
9906: A7 88 2A        STA     $2A,X                 
9909: CC 08 B4        LDD     #$08B4                  
990C: A7 1A           STA     -6,X                
990E: E7 04           STB     4,X                 
9910: 39              RTS                         
9911: 12              NOP                         
9912: 39              RTS                         
9913: FE 00 10        LDU     $0010                   
9916: FF FE FE        STU     $FEFE                   
9919: 10 ; ????
991A: 20 00           BRA     $991C                   
991C: FE FF 20        LDU     $FF20                   
991F: 02 ; ????
9920: FE F0 20        LDU     $F020                   
9923: 02 ; ????
9924: 00 F0           NEG     $F0                   
9926: FF 02 02        STU     $0202                   
9929: F0 E0 00        SUBB    $E000                   
992C: 02 ; ????
992D: FF E0 FE        STU     $E0FE                   
9930: 02 ; ????
9931: 10 ; ????
9932: E0 10           SUBB    -16,X               
9934: 12              NOP                         
9935: 12              NOP                         
9936: 12              NOP                         
9937: 14 ; ????
9938: 16 16 16        LBRA    $AF51                   
993B: 30 ; ????
993C: D0 04           SUBB    $04                   
993E: 30 30           LEAX    -16,Y               
9940: 16 A8 30        LBRA    $4173                   
9943: 1A A8           ORCC    #$A8                  
9945: D0 1A           SUBB    $1A                   
9947: 4A              DECA                        
9948: 01 ; ????
9949: 74 05 76        LSR     $0576                   
994C: 05 ; ????
994D: C8 CC           EORB    #$CC                  
994F: D0 1E           SUBB    $1E                   
9951: D4 D8           ANDB    $D8                   
9953: DC 16           LDD     $16                   
9955: BD 81 50        JSR     $8150                   
9958: B6 10 E5        LDA     $10E5                   
995B: 27 F8           BEQ     $9955                   
995D: BD 9A D7        JSR     $9AD7                   
9960: CC 01 2E        LDD     #$012E                  
9963: B7 40 4A        STA     $404A                   
9966: F7 10 4F        STB     $104F                   
9969: CC 06 08        LDD     #$0608                  
996C: B7 10 59        STA     $1059                   
996F: F7 10 5A        STB     $105A                   
9972: 8E 9C 87        LDX     #$9C87                  
9975: BF 10 57        STX     $1057                   
9978: 7C 10 1B        INC     $101B                   
997B: 86 41           LDA     #$41                  
997D: BE 10 C7        LDX     $10C7                   
9980: A7 84           STA     ,X                  
9982: 30 89 09 60     LEAX    $0960,X                 
9986: BF 10 C9        STX     $10C9                   
9989: CC 0A 16        LDD     #$0A16                  
998C: BD 85 A0        JSR     $85A0                   
998F: B6 10 ED        LDA     $10ED                   
9992: 27 15           BEQ     $99A9                   
9994: 8E 02 FB        LDX     #$02FB                  
9997: CE 9C A2        LDU     #$9CA2                  
999A: 86 14           LDA     #$14                  
999C: BD 85 90        JSR     $8590                   
999F: 8E 0A FB        LDX     #$0AFB                  
99A2: 86 0B           LDA     #$0B                  
99A4: C6 14           LDB     #$14                  
99A6: BD 85 A0        JSR     $85A0                   
99A9: BD 81 50        JSR     $8150                   
99AC: B6 48 05        LDA     $4805                   
99AF: 84 08           ANDA    #$08                  
99B1: 10 26 01 03     LBNE    $9AB8                   
99B5: B6 48 07        LDA     $4807                   
99B8: 84 08           ANDA    #$08                  
99BA: 10 26 00 FA     LBNE    $9AB8                   
99BE: B6 10 50        LDA     $1050                   
99C1: 26 07           BNE     $99CA                   
99C3: 7A 10 4F        DEC     $104F                   
99C6: 10 27 00 92     LBEQ    $9A5C                   
99CA: B6 10 ED        LDA     $10ED                   
99CD: 27 1E           BEQ     $99ED                   
99CF: B6 10 01        LDA     $1001                   
99D2: 84 08           ANDA    #$08                  
99D4: 26 0D           BNE     $99E3                   
99D6: 8E 02 FB        LDX     #$02FB                  
99D9: CE 9C A2        LDU     #$9CA2                  
99DC: 86 14           LDA     #$14                  
99DE: BD 85 90        JSR     $8590                   
99E1: 20 0A           BRA     $99ED                   
99E3: 8E 02 FB        LDX     #$02FB                  
99E6: 86 20           LDA     #$20                  
99E8: C6 14           LDB     #$14                  
99EA: BD 85 A0        JSR     $85A0                   
99ED: 86 01           LDA     #$01                  
99EF: B7 40 4A        STA     $404A                   
99F2: B1 10 15        CMPA    $1015                   
99F5: 27 3B           BEQ     $9A32                   
99F7: B1 10 14        CMPA    $1014                   
99FA: 27 36           BEQ     $9A32                   
99FC: 7A 10 5A        DEC     $105A                   
99FF: 26 A8           BNE     $99A9                   
9A01: BE 10 57        LDX     $1057                   
9A04: B6 10 13        LDA     $1013                   
9A07: 2B 4B           BMI     $9A54                   
9A09: 81 02           CMPA    #$02                  
9A0B: 23 0C           BLS     $9A19                   
9A0D: 30 1F           LEAX    -1,X                
9A0F: 8C 9C 85        CMPX    #$9C85                  
9A12: 26 0F           BNE     $9A23                   
9A14: 8E 9C A1        LDX     #$9CA1                  
9A17: 20 0A           BRA     $9A23                   
9A19: 30 01           LEAX    1,X                 
9A1B: 8C 9C A2        CMPX    #$9CA2                  
9A1E: 26 03           BNE     $9A23                   
9A20: 8E 9C 86        LDX     #$9C86                  
9A23: A6 84           LDA     ,X                  
9A25: A7 9F 10 C5     STA     [$10C5]                 
9A29: A7 9F 10 C7     STA     [$10C7]                 
9A2D: BF 10 57        STX     $1057                   
9A30: 20 22           BRA     $9A54                   
9A32: A6 9F 10 57     LDA     [$1057]                 
9A36: A7 9F 10 C5     STA     [$10C5]                 
9A3A: 7A 10 59        DEC     $1059                   
9A3D: 27 1D           BEQ     $9A5C                   
9A3F: BE 10 C5        LDX     $10C5                   
9A42: 30 01           LEAX    1,X                 
9A44: BF 10 C5        STX     $10C5                   
9A47: A7 84           STA     ,X                  
9A49: BE 10 C7        LDX     $10C7                   
9A4C: 30 88 E0        LEAX    $E0,X                 
9A4F: BF 10 C7        STX     $10C7                   
9A52: A7 84           STA     ,X                  
9A54: 86 08           LDA     #$08                  
9A56: B7 10 5A        STA     $105A                   
9A59: 7E 99 A9        JMP     $99A9                   
9A5C: BE 10 C7        LDX     $10C7                   
9A5F: CC 00 01        LDD     #$0001                  
9A62: F7 40 4A        STB     $404A                   
9A65: A7 89 08 00     STA     $0800,X                 
9A69: B7 10 1B        STA     $101B                   
9A6C: BD 81 50        JSR     $8150                   
9A6F: B6 48 05        LDA     $4805                   
9A72: 84 08           ANDA    #$08                  
9A74: 26 42           BNE     $9AB8                   
9A76: B6 48 07        LDA     $4807                   
9A79: 84 08           ANDA    #$08                  
9A7B: 26 3B           BNE     $9AB8                   
9A7D: B6 10 ED        LDA     $10ED                   
9A80: 27 1E           BEQ     $9AA0                   
9A82: B6 10 01        LDA     $1001                   
9A85: 84 08           ANDA    #$08                  
9A87: 26 0D           BNE     $9A96                   
9A89: 8E 02 FB        LDX     #$02FB                  
9A8C: CE 9C A2        LDU     #$9CA2                  
9A8F: 86 14           LDA     #$14                  
9A91: BD 85 90        JSR     $8590                   
9A94: 20 0A           BRA     $9AA0                   
9A96: 8E 02 FB        LDX     #$02FB                  
9A99: 86 20           LDA     #$20                  
9A9B: C6 14           LDB     #$14                  
9A9D: BD 85 A0        JSR     $85A0                   
9AA0: B6 40 4A        LDA     $404A                   
9AA3: 27 13           BEQ     $9AB8                   
9AA5: C6 16           LDB     #$16                  
9AA7: B6 10 01        LDA     $1001                   
9AAA: 84 08           ANDA    #$08                  
9AAC: 27 02           BEQ     $9AB0                   
9AAE: 8B 02           ADDA    #$02                  
9AB0: BE 10 C9        LDX     $10C9                   
9AB3: BD 85 A0        JSR     $85A0                   
9AB6: 20 B4           BRA     $9A6C                   
9AB8: 7F 40 4A        CLR     $404A                   
9ABB: 7F 10 E5        CLR     $10E5                   
9ABE: 7F 10 ED        CLR     $10ED                   
9AC1: 7E 99 55        JMP     $9955                   
9AC4: 8E 11 B0        LDX     #$11B0                  
9AC7: CE 9C 17        LDU     #$9C17                  
9ACA: B6 80 00        LDA     $8000                   
9ACD: EC C1           LDD     ,U++                
9ACF: ED 81           STD     ,X++                
9AD1: 8C 12 00        CMPX    #$1200                  
9AD4: 26 F4           BNE     $9ACA                   
9AD6: 39              RTS                         
9AD7: BD 87 06        JSR     $8706                   
9ADA: 8E 02 28        LDX     #$0228                  
9ADD: CE 9C 67        LDU     #$9C67                  
9AE0: 86 06           LDA     #$06                  
9AE2: BD 85 90        JSR     $8590                   
9AE5: 8E 03 4B        LDX     #$034B                  
9AE8: CE 9C 6D        LDU     #$9C6D                  
9AEB: 86 19           LDA     #$19                  
9AED: BD 85 90        JSR     $8590                   
9AF0: 8E 0A 28        LDX     #$0A28                  
9AF3: 86 0D           LDA     #$0D                  
9AF5: C6 06           LDB     #$06                  
9AF7: BD 85 A0        JSR     $85A0                   
9AFA: 8E 0B 4B        LDX     #$0B4B                  
9AFD: 86 0E           LDA     #$0E                  
9AFF: C6 19           LDB     #$19                  
9B01: BD 85 A0        JSR     $85A0                   
9B04: 86 05           LDA     #$05                  
9B06: 8E 03 18        LDX     #$0318                  
9B09: A7 83           STA     ,--X                
9B0B: 6F 89 FF 00     CLR     $FF00,X                 
9B0F: 4A              DECA                        
9B10: 26 F7           BNE     $9B09                   
9B12: 8E 02 CE        LDX     #$02CE                  
9B15: CE 11 B0        LDU     #$11B0                  
9B18: 86 05           LDA     #$05                  
9B1A: B7 10 CE        STA     $10CE                   
9B1D: CC 20 06        LDD     #$2006                  
9B20: B7 10 CF        STA     $10CF                   
9B23: A6 C0           LDA     ,U+                 
9B25: 26 07           BNE     $9B2E                   
9B27: B6 10 CF        LDA     $10CF                   
9B2A: A7 84           STA     ,X                  
9B2C: 20 05           BRA     $9B33                   
9B2E: A7 84           STA     ,X                  
9B30: 7F 10 CF        CLR     $10CF                   
9B33: 30 88 E0        LEAX    $E0,X                 
9B36: 5A              DECB                        
9B37: 26 EA           BNE     $9B23                   
9B39: C6 06           LDB     #$06                  
9B3B: 30 88 C0        LEAX    $C0,X                 
9B3E: 30 88 E0        LEAX    $E0,X                 
9B41: A6 C0           LDA     ,U+                 
9B43: A7 84           STA     ,X                  
9B45: 5A              DECB                        
9B46: 26 F6           BNE     $9B3E                   
9B48: A6 43           LDA     3,U                 
9B4A: 33 44           LEAU    4,U                 
9B4C: 1F 89           TFR     A,B                   
9B4E: 84 F0           ANDA    #$F0                  
9B50: 27 07           BEQ     $9B59                   
9B52: 44              LSRA                        
9B53: 44              LSRA                        
9B54: 44              LSRA                        
9B55: 44              LSRA                        
9B56: A7 88 80        STA     $80,X                 
9B59: C4 0F           ANDB    #$0F                  
9B5B: E7 89 FF 60     STB     $FF60,X                 
9B5F: 30 89 01 C2     LEAX    $01C2,X                 
9B63: 7A 10 CE        DEC     $10CE                   
9B66: 26 B5           BNE     $9B1D                   
9B68: 39              RTS                         
9B69: 86 03           LDA     #$03                  
9B6B: B7 10 09        STA     $1009                   
9B6E: 8E 10 51        LDX     #$1051                  
9B71: CE 17 00        LDU     #$1700                  
9B74: A6 C0           LDA     ,U+                 
9B76: 1F 89           TFR     A,B                   
9B78: 84 F0           ANDA    #$F0                  
9B7A: 44              LSRA                        
9B7B: 44              LSRA                        
9B7C: 44              LSRA                        
9B7D: 44              LSRA                        
9B7E: A7 80           STA     ,X+                 
9B80: C4 0F           ANDB    #$0F                  
9B82: E7 80           STB     ,X+                 
9B84: 7A 10 09        DEC     $1009                   
9B87: 26 EB           BNE     $9B74                   
9B89: CE 10 51        LDU     #$1051                  
9B8C: 8E 11 F0        LDX     #$11F0                  
9B8F: EC C4           LDD     ,U                  
9B91: 10 A3 84        CMPD    ,X                  
9B94: 22 12           BHI     $9BA8                   
9B96: 25 ; ????
9B97: 1A EC           ORCC    #$EC                  
9B99: 42 ; ????
9B9A: 10 A3 02        CMPD    2,X                 
9B9D: 22 09           BHI     $9BA8                   
9B9F: 25 ; ????
9BA0: 11 ; ????
9BA1: EC 44           LDD     4,U                 
9BA3: 10 A3 04        CMPD    4,X                 
9BA6: 25 ; ????
9BA7: 0A 7C           DEC     $7C                   
9BA9: 10 ; ????
9BAA: 09 30           ROL     $30                   
9BAC: 10 8C 11 A0     CMPY    #$11A0                  
9BB0: 26 DD           BNE     $9B8F                   
9BB2: B6 10 09        LDA     $1009                   
9BB5: 26 01           BNE     $9BB8                   
9BB7: 39              RTS                         
9BB8: 81 05           CMPA    #$05                  
9BBA: 26 03           BNE     $9BBF                   
9BBC: 7C 10 ED        INC     $10ED                   
9BBF: 1F 89           TFR     A,B                   
9BC1: 53              COMB                        
9BC2: C4 07           ANDB    #$07                  
9BC4: C0 02           SUBB    #$02                  
9BC6: 58 ; ????
9BC7: 8E 01 AE        LDX     #$01AE                  
9BCA: 3A              ABX                         
9BCB: BF 10 C7        STX     $10C7                   
9BCE: 8E 11 F0        LDX     #$11F0                  
9BD1: 4A              DECA                        
9BD2: 27 0F           BEQ     $9BE3                   
9BD4: C6 08           LDB     #$08                  
9BD6: EE 10           LDU     -16,X               
9BD8: EF 81           STU     ,X++                
9BDA: 5A              DECB                        
9BDB: 26 F9           BNE     $9BD6                   
9BDD: 30 88 E0        LEAX    $E0,X                 
9BE0: 4A              DECA                        
9BE1: 26 F1           BNE     $9BD4                   
9BE3: FC 10 51        LDD     $1051                   
9BE6: ED 81           STD     ,X++                
9BE8: FC 10 53        LDD     $1053                   
9BEB: ED 81           STD     ,X++                
9BED: FC 10 55        LDD     $1055                   
9BF0: ED 81           STD     ,X++                
9BF2: 86 41           LDA     #$41                  
9BF4: BF 10 C5        STX     $10C5                   
9BF7: A7 80           STA     ,X+                 
9BF9: CC 20 08        LDD     #$2008                  
9BFC: A7 80           STA     ,X+                 
9BFE: 5A              DECB                        
9BFF: 26 FB           BNE     $9BFC                   
9C01: B6 17 05        LDA     $1705                   
9C04: F6 10 E0        LDB     $10E0                   
9C07: 27 03           BEQ     $9C0C                   
9C09: 8B 99           ADDA    #$99                  
9C0B: 19              DAA                         
9C0C: A7 84           STA     ,X                  
9C0E: 86 01           LDA     #$01                  
9C10: B7 10 E5        STA     $10E5                   
9C13: B7 40 4A        STA     $404A                   
9C16: 39              RTS                         
9C17: 00 00           NEG     $00                   
9C19: 02 ; ????
9C1A: 00 00           NEG     $00                   
9C1C: 00 20           NEG     $20                   
9C1E: 4B ; ????
9C1F: 41 ; ????
9C20: 5A              DECB                        
9C21: 55 ; ????
9C22: 20 FF           BRA     $9C23                   
9C24: FF FF 05        STU     $FF05                   
9C27: 00 00           NEG     $00                   
9C29: 02 ; ????
9C2A: 00 00           NEG     $00                   
9C2C: 00 20           NEG     $20                   
9C2E: 59              ROLB                        
9C2F: 41 ; ????
9C30: 4D              TSTA                        
9C31: 41 ; ????
9C32: 20 FF           BRA     $9C33                   
9C34: FF FF 04        STU     $FF04                   
9C37: 00 00           NEG     $00                   
9C39: 02 ; ????
9C3A: 00 00           NEG     $00                   
9C3C: 00 53           NEG     $53                   
9C3E: 49              ROLA                        
9C3F: 47              ASRA                        
9C40: 45 ; ????
9C41: 52 ; ????
9C42: 55 ; ????
9C43: FF FF FF        STU     $FFFF                   
9C46: 03 00           COM     $00                   
9C48: 00 02           NEG     $02                   
9C4A: 00 00           NEG     $00                   
9C4C: 00 4A           NEG     $4A                   
9C4E: 55 ; ????
9C4F: 4E ; ????
9C50: 4B ; ????
9C51: 4F              CLRA                        
9C52: 20 FF           BRA     $9C53                   
9C54: FF FF 02        STU     $FF02                   
9C57: 00 00           NEG     $00                   
9C59: 02 ; ????
9C5A: 00 00           NEG     $00                   
9C5C: 00 4D           NEG     $4D                   
9C5E: 49              ROLA                        
9C5F: 59              ROLB                        
9C60: 55 ; ????
9C61: 4B ; ????
9C62: 49              ROLA                        
9C63: FF FF FF        STU     $FFFF                   
9C66: 01 ; ????
9C67: 42 ; ????
9C68: 45 ; ????
9C69: 53              COMB                        
9C6A: 54              LSRB                        
9C6B: 20 35           BRA     $9CA2                   
9C6D: 52 ; ????
9C6E: 41 ; ????
9C6F: 4E ; ????
9C70: 4B ; ????
9C71: 20 20           BRA     $9C93                   
9C73: 53              COMB                        
9C74: 43              COMA                        
9C75: 4F              CLRA                        
9C76: 52 ; ????
9C77: 45 ; ????
9C78: 20 20           BRA     $9C9A                   
9C7A: 20 4E           BRA     $9CCA                   
9C7C: 41 ; ????
9C7D: 4D              TSTA                        
9C7E: 45 ; ????
9C7F: 20 20           BRA     $9CA1                   
9C81: 52 ; ????
9C82: 4F              CLRA                        
9C83: 55 ; ????
9C84: 4E ; ????
9C85: 44              LSRA                        
9C86: 20 41           BRA     $9CC9                   
9C88: 42 ; ????
9C89: 43              COMA                        
9C8A: 44              LSRA                        
9C8B: 45 ; ????
9C8C: 46              RORA                        
9C8D: 47              ASRA                        
9C8E: 48 ; ????
9C8F: 49              ROLA                        
9C90: 4A              DECA                        
9C91: 4B ; ????
9C92: 4C              INCA                        
9C93: 4D              TSTA                        
9C94: 4E ; ????
9C95: 4F              CLRA                        
9C96: 50              NEGB                        
9C97: 51 ; ????
9C98: 52 ; ????
9C99: 53              COMB                        
9C9A: 54              LSRB                        
9C9B: 55 ; ????
9C9C: 56              RORB                        
9C9D: 57              ASRB                        
9C9E: 58 ; ????
9C9F: 59              ROLB                        
9CA0: 5A              DECB                        
9CA1: 5B ; ????
9CA2: 59              ROLB                        
9CA3: 4F              CLRA                        
9CA4: 55 ; ????
9CA5: 20 41           BRA     $9CE8                   
9CA7: 52 ; ????
9CA8: 45 ; ????
9CA9: 20 54           BRA     $9CFF                   
9CAB: 48 ; ????
9CAC: 45 ; ????
9CAD: 20 43           BRA     $9CF2                   
9CAF: 48 ; ????
9CB0: 41 ; ????
9CB1: 4D              TSTA                        
9CB2: 50              NEGB                        
9CB3: 49              ROLA                        
9CB4: 4F              CLRA                        
9CB5: 4E ; ????
9CB6: BD 81 50        JSR     $8150                   
9CB9: B6 10 E1        LDA     $10E1                   
9CBC: 27 F8           BEQ     $9CB6                   
9CBE: BD 87 06        JSR     $8706                   
9CC1: BD 8B 3D        JSR     $8B3D                   
9CC4: CC 01 01        LDD     #$0101                  
9CC7: FD 17 04        STD     $1704                   
9CCA: B7 10 1B        STA     $101B                   
9CCD: BD 87 C5        JSR     $87C5                   
9CD0: BD 81 50        JSR     $8150                   
9CD3: B6 10 14        LDA     $1014                   
9CD6: 26 31           BNE     $9D09                   
9CD8: B6 10 01        LDA     $1001                   
9CDB: 84 07           ANDA    #$07                  
9CDD: 26 F1           BNE     $9CD0                   
9CDF: F6 10 13        LDB     $1013                   
9CE2: 2B EC           BMI     $9CD0                   
9CE4: C5 02           BITB    #$02                  
9CE6: 26 E8           BNE     $9CD0                   
9CE8: 8E 17 00        LDX     #$1700                  
9CEB: A6 05           LDA     5,X                 
9CED: C5 04           BITB    #$04                  
9CEF: 26 0B           BNE     $9CFC                   
9CF1: 81 32           CMPA    #$32                  
9CF3: 27 DB           BEQ     $9CD0                   
9CF5: 6C 04           INC     4,X                 
9CF7: 8B 01           ADDA    #$01                  
9CF9: 19              DAA                         
9CFA: 20 09           BRA     $9D05                   
9CFC: 81 01           CMPA    #$01                  
9CFE: 27 D0           BEQ     $9CD0                   
9D00: 6A 04           DEC     4,X                 
9D02: 8B 99           ADDA    #$99                  
9D04: 19              DAA                         
9D05: A7 05           STA     5,X                 
9D07: 20 C4           BRA     $9CCD                   
9D09: 7F 10 E1        CLR     $10E1                   
9D0C: 7F 10 1B        CLR     $101B                   
9D0F: 7A 17 04        DEC     $1704                   
9D12: B6 17 05        LDA     $1705                   
9D15: 8B 99           ADDA    #$99                  
9D17: 19              DAA                         
9D18: B7 17 05        STA     $1705                   
9D1B: 7C 17 25        INC     $1725                   
9D1E: 20 96           BRA     $9CB6                   
9D20: BD 81 50        JSR     $8150                   
9D23: B6 10 E9        LDA     $10E9                   
9D26: 27 F8           BEQ     $9D20                   
9D28: B6 10 F0        LDA     $10F0                   
9D2B: 10 27 01 99     LBEQ    $9EC8                   
9D2F: BD 87 06        JSR     $8706                   
9D32: B6 10 05        LDA     $1005                   
9D35: 27 28           BEQ     $9D5F                   
9D37: 8E 07 BC        LDX     #$07BC                  
9D3A: 86 20           LDA     #$20                  
9D3C: C6 0A           LDB     #$0A                  
9D3E: BD 85 BD        JSR     $85BD                   
9D41: 8E 07 9C        LDX     #$079C                  
9D44: 86 20           LDA     #$20                  
9D46: C6 0A           LDB     #$0A                  
9D48: BD 85 BD        JSR     $85BD                   
9D4B: 8E 0F BC        LDX     #$0FBC                  
9D4E: 86 00           LDA     #$00                  
9D50: C6 0A           LDB     #$0A                  
9D52: BD 85 BD        JSR     $85BD                   
9D55: 8E 0F 9C        LDX     #$0F9C                  
9D58: 86 00           LDA     #$00                  
9D5A: C6 0A           LDB     #$0A                  
9D5C: BD 85 BD        JSR     $85BD                   
9D5F: 8E 03 2A        LDX     #$032A                  
9D62: CE 9E D7        LDU     #$9ED7                  
9D65: 86 18           LDA     #$18                  
9D67: BD 85 90        JSR     $8590                   
9D6A: 8E 02 16        LDX     #$0216                  
9D6D: CE 9E F7        LDU     #$9EF7                  
9D70: 86 04           LDA     #$04                  
9D72: BD 85 90        JSR     $8590                   
9D75: 8E 07 AB        LDX     #$07AB                  
9D78: CE 88 0D        LDU     #$880D                  
9D7B: 86 08           LDA     #$08                  
9D7D: BD 85 AE        JSR     $85AE                   
9D80: 8E 0B 2A        LDX     #$0B2A                  
9D83: 86 0D           LDA     #$0D                  
9D85: C6 18           LDB     #$18                  
9D87: BD 85 A0        JSR     $85A0                   
9D8A: 8E 0A 16        LDX     #$0A16                  
9D8D: 86 0A           LDA     #$0A                  
9D8F: C6 04           LDB     #$04                  
9D91: BD 85 A0        JSR     $85A0                   
9D94: CC 3C 06        LDD     #$3C06                  
9D97: B7 10 50        STA     $1050                   
9D9A: F7 01 76        STB     $0176                   
9D9D: 8E 0A AF        LDX     #$0AAF                  
9DA0: BF 10 C9        STX     $10C9                   
9DA3: 8E 02 AF        LDX     #$02AF                  
9DA6: CE 9E EF        LDU     #$9EEF                  
9DA9: CC 04 0B        LDD     #$040B                  
9DAC: B7 10 09        STA     $1009                   
9DAF: F7 09 76        STB     $0976                   
9DB2: EC C1           LDD     ,U++                
9DB4: A7 84           STA     ,X                  
9DB6: E7 88 E0        STB     $E0,X                 
9DB9: 30 88 80        LEAX    $80,X                 
9DBC: 7A 10 09        DEC     $1009                   
9DBF: 26 F1           BNE     $9DB2                   
9DC1: 8E 25 10        LDX     #$2510                  
9DC4: 6C 0B           INC     11,X                
9DC6: CC 98 B2        LDD     #$98B2                  
9DC9: A7 0F           STA     15,X                
9DCB: E7 0D           STB     13,X                
9DCD: CC 00 00        LDD     #$0000                  
9DD0: FD 10 14        STD     $1014                   
9DD3: 7C 10 1B        INC     $101B                   
9DD6: CC 08 0B        LDD     #$080B                  
9DD9: A7 0A           STA     10,X                
9DDB: 6F 0C           CLR     12,X                
9DDD: BE 10 C9        LDX     $10C9                   
9DE0: E7 84           STB     ,X                  
9DE2: E7 88 E0        STB     $E0,X                 
9DE5: A6 89 F7 E0     LDA     $F7E0,X                 
9DE9: E6 89 F8 00     LDB     $F800,X                 
9DED: FD 07 A3        STD     $07A3                   
9DF0: BD 81 50        JSR     $8150                   
9DF3: 8E 25 10        LDX     #$2510                  
9DF6: B6 10 50        LDA     $1050                   
9DF9: 26 07           BNE     $9E02                   
9DFB: 7A 01 76        DEC     $0176                   
9DFE: 10 27 00 83     LBEQ    $9E85                   
9E02: FC 10 14        LDD     $1014                   
9E05: 26 7E           BNE     $9E85                   
9E07: B6 01 76        LDA     $0176                   
9E0A: 27 79           BEQ     $9E85                   
9E0C: B6 10 13        LDA     $1013                   
9E0F: 2B C5           BMI     $9DD6                   
9E11: 85 02           BITA    #$02                  
9E13: 27 C1           BEQ     $9DD6                   
9E15: 85 04           BITA    #$04                  
9E17: 26 18           BNE     $9E31                   
9E19: A6 04           LDA     4,X                 
9E1B: 81 03           CMPA    #$03                  
9E1D: 27 B7           BEQ     $9DD6                   
9E1F: CC FE 04        LDD     #$FE04                  
9E22: 6C 04           INC     4,X                 
9E24: FE 10 C9        LDU     $10C9                   
9E27: 6F C4           CLR     ,U                  
9E29: 6F C8 E0        CLR     $E0,U                 
9E2C: 33 C8 80        LEAU    $80,U                 
9E2F: 20 15           BRA     $9E46                   
9E31: A6 04           LDA     4,X                 
9E33: 27 A1           BEQ     $9DD6                   
9E35: CC 02 0C        LDD     #$020C                  
9E38: 6A 04           DEC     4,X                 
9E3A: FE 10 C9        LDU     $10C9                   
9E3D: 6F C4           CLR     ,U                  
9E3F: 6F C8 E0        CLR     $E0,U                 
9E42: 33 C9 00 80     LEAU    $0080,U                 
9E46: FF 10 C9        STU     $10C9                   
9E49: A7 05           STA     5,X                 
9E4B: E7 0A           STB     10,X                
9E4D: 86 0F           LDA     #$0F                  
9E4F: A7 1B           STA     -5,X                
9E51: A6 1B           LDA     -5,X                
9E53: 27 B2           BEQ     $9E07                   
9E55: A6 05           LDA     5,X                 
9E57: AB 0D           ADDA    13,X                
9E59: A7 0D           STA     13,X                
9E5B: 6A 1B           DEC     -5,X                
9E5D: A6 0A           LDA     10,X                
9E5F: 84 0C           ANDA    #$0C                  
9E61: B7 10 34        STA     $1034                   
9E64: A6 1B           LDA     -5,X                
9E66: 84 06           ANDA    #$06                  
9E68: 44              LSRA                        
9E69: BB 10 34        ADDA    $1034                   
9E6C: A7 0A           STA     10,X                
9E6E: 6F 0C           CLR     12,X                
9E70: BD 81 50        JSR     $8150                   
9E73: 8E 25 10        LDX     #$2510                  
9E76: B6 10 50        LDA     $1050                   
9E79: 26 D6           BNE     $9E51                   
9E7B: B6 01 76        LDA     $0176                   
9E7E: 27 D1           BEQ     $9E51                   
9E80: 7A 01 76        DEC     $0176                   
9E83: 20 CC           BRA     $9E51                   
9E85: CC 3F 08        LDD     #$3F08                  
9E88: B7 10 4F        STA     $104F                   
9E8B: F7 25 1A        STB     $251A                   
9E8E: BE 10 C9        LDX     $10C9                   
9E91: A6 89 F7 E0     LDA     $F7E0,X                 
9E95: E6 89 F8 00     LDB     $F800,X                 
9E99: FD 07 A3        STD     $07A3                   
9E9C: BD 81 50        JSR     $8150                   
9E9F: 7A 10 4F        DEC     $104F                   
9EA2: 27 13           BEQ     $9EB7                   
9EA4: B6 10 01        LDA     $1001                   
9EA7: 84 08           ANDA    #$08                  
9EA9: 27 02           BEQ     $9EAD                   
9EAB: 86 0B           LDA     #$0B                  
9EAD: BE 10 C9        LDX     $10C9                   
9EB0: A7 84           STA     ,X                  
9EB2: A7 88 E0        STA     $E0,X                 
9EB5: 20 E5           BRA     $9E9C                   
9EB7: 8E 25 10        LDX     #$2510                  
9EBA: A6 04           LDA     4,X                 
9EBC: CE 9E FB        LDU     #$9EFB                  
9EBF: 48 ; ????
9EC0: EC C6           LDD     A,U                 
9EC2: FD 17 04        STD     $1704                   
9EC5: BD 87 32        JSR     $8732                   
9EC8: CC 00 01        LDD     #$0001                  
9ECB: B7 10 1B        STA     $101B                   
9ECE: B7 10 E9        STA     $10E9                   
9ED1: F7 17 25        STB     $1725                   
9ED4: 7E 9D 20        JMP     $9D20                   
9ED7: 53              COMB                        
9ED8: 45 ; ????
9ED9: 4C              INCA                        
9EDA: 45 ; ????
9EDB: 43              COMA                        
9EDC: 54              LSRB                        
9EDD: 20 59           BRA     $9F38                   
9EDF: 4F              CLRA                        
9EE0: 55 ; ????
9EE1: 52 ; ????
9EE2: 20 52           BRA     $9F36                   
9EE4: 4F              CLRA                        
9EE5: 55 ; ????
9EE6: 4E ; ????
9EE7: 44              LSRA                        
9EE8: 20 4E           BRA     $9F38                   
9EEA: 55 ; ????
9EEB: 4D              TSTA                        
9EEC: 42 ; ????
9EED: 45 ; ????
9EEE: 52 ; ????
9EEF: 20 31           BRA     $9F22                   
9EF1: 20 35           BRA     $9F28                   
9EF3: 31 30           LEAY    -16,Y               
9EF5: 31 35           LEAY    -11,Y               
9EF7: 54              LSRB                        
9EF8: 49              ROLA                        
9EF9: 4D              TSTA                        
9EFA: 45 ; ????
9EFB: 00 00           NEG     $00                   
9EFD: 04 04           LSR     $04                   
9EFF: 09 09           ROL     $09                   
9F01: 0E 14           JMP     $14                   
9F03: BD 81 50        JSR     $8150                   
9F06: B6 10 DA        LDA     $10DA                   
9F09: 27 F8           BEQ     $9F03                   
9F0B: B7 40 48        STA     $4048                   
9F0E: BD 81 50        JSR     $8150                   
9F11: B6 10 DA        LDA     $10DA                   
9F14: 27 ED           BEQ     $9F03                   
9F16: 7A 25 14        DEC     $2514                   
9F19: B6 25 14        LDA     $2514                   
9F1C: 81 50           CMPA    #$50                  
9F1E: 23 14           BLS     $9F34                   
9F20: 84 04           ANDA    #$04                  
9F22: 44              LSRA                        
9F23: 44              LSRA                        
9F24: B7 10 34        STA     $1034                   
9F27: B6 25 1A        LDA     $251A                   
9F2A: 84 46           ANDA    #$46                  
9F2C: BA 10 34        ORA     $1034                   
9F2F: B7 25 1A        STA     $251A                   
9F32: 20 DA           BRA     $9F0E                   
9F34: BD 81 50        JSR     $8150                   
9F37: B6 10 DA        LDA     $10DA                   
9F3A: 27 C7           BEQ     $9F03                   
9F3C: 8E 25 10        LDX     #$2510                  
9F3F: 6A 04           DEC     4,X                 
9F41: 27 7D           BEQ     $9FC0                   
9F43: A6 04           LDA     4,X                 
9F45: 84 04           ANDA    #$04                  
9F47: 44              LSRA                        
9F48: 44              LSRA                        
9F49: B7 10 34        STA     $1034                   
9F4C: A6 0A           LDA     10,X                
9F4E: 84 46           ANDA    #$46                  
9F50: BA 10 34        ORA     $1034                   
9F53: A7 0A           STA     10,X                
9F55: B6 10 13        LDA     $1013                   
9F58: 2B DA           BMI     $9F34                   
9F5A: B7 10 34        STA     $1034                   
9F5D: BD C9 B8        JSR     $C9B8                   
9F60: B6 10 D8        LDA     $10D8                   
9F63: 26 CF           BNE     $9F34                   
9F65: B6 10 34        LDA     $1034                   
9F68: A7 05           STA     5,X                 
9F6A: 48 ; ????
9F6B: A7 0A           STA     10,X                
9F6D: B6 17 07        LDA     $1707                   
9F70: A7 03           STA     3,X                 
9F72: 6F 1D           CLR     -3,X                
9F74: CC 00 08        LDD     #$0008                  
9F77: A7 08           STA     8,X                 
9F79: EB 0F           ADDB    15,X                
9F7B: C4 F0           ANDB    #$F0                  
9F7D: E7 0F           STB     15,X                
9F7F: EC 1E           LDD     -2,X                
9F81: C3 00 08        ADDD    #$0008                  
9F84: C4 F0           ANDB    #$F0                  
9F86: ED 1E           STD     -2,X                
9F88: 86 10           LDA     #$10                  
9F8A: A7 1B           STA     -5,X                
9F8C: BD C0 00        JSR     $C000                   
9F8F: BD C0 9F        JSR     $C09F                   
9F92: BD C4 80        JSR     $C480                   
9F95: BD 81 50        JSR     $8150                   
9F98: B6 10 DA        LDA     $10DA                   
9F9B: 10 27 FF 64     LBEQ    $9F03                   
9F9F: 8E 25 10        LDX     #$2510                  
9FA2: A6 05           LDA     5,X                 
9FA4: 85 02           BITA    #$02                  
9FA6: 26 08           BNE     $9FB0                   
9FA8: A6 0F           LDA     15,X                
9FAA: 84 0F           ANDA    #$0F                  
9FAC: 26 DE           BNE     $9F8C                   
9FAE: 20 06           BRA     $9FB6                   
9FB0: A6 1F           LDA     -1,X                
9FB2: 84 0F           ANDA    #$0F                  
9FB4: 26 D6           BNE     $9F8C                   
9FB6: CC 00 01        LDD     #$0001                  
9FB9: A7 1B           STA     -5,X                
9FBB: E7 1A           STB     -6,X                
9FBD: 7E A0 76        JMP     $A076                   
9FC0: FC 10 D0        LDD     $10D0                   
9FC3: 10 26 00 AF     LBNE    $A076                   
9FC7: CC 01 05        LDD     #$0105                  
9FCA: B7 40 51        STA     $4051                   
9FCD: B7 10 D0        STA     $10D0                   
9FD0: E7 1A           STB     -6,X                
9FD2: CC 00 3F        LDD     #$003F                  
9FD5: B7 10 4F        STA     $104F                   
9FD8: E7 04           STB     4,X                 
9FDA: C6 08           LDB     #$08                  
9FDC: A6 0A           LDA     10,X                
9FDE: 84 07           ANDA    #$07                  
9FE0: 85 04           BITA    #$04                  
9FE2: 26 5B           BNE     $A03F                   
9FE4: 81 01           CMPA    #$01                  
9FE6: 23 4F           BLS     $A037                   
9FE8: 86 10           LDA     #$10                  
9FEA: E6 08           LDB     8,X                 
9FEC: 26 02           BNE     $9FF0                   
9FEE: 86 F0           LDA     #$F0                  
9FF0: EE 1E           LDU     -2,X                
9FF2: 33 C6           LEAU    A,U                 
9FF4: EF 1E           STU     -2,X                
9FF6: AB 0D           ADDA    13,X                
9FF8: A7 0D           STA     13,X                
9FFA: 86 06           LDA     #$06                  
9FFC: AB 0F           ADDA    15,X                
9FFE: A7 0F           STA     15,X                
A000: BD CD 83        JSR     $CD83                   
A003: CE 15 7F        LDU     #$157F                  
A006: A6 C5           LDA     B,U                 
A008: 81 0A           CMPA    #$0A                  
A00A: 24 ; ????
A00B: 68 ; ????
A00C: 5C              INCB                        
A00D: A6 C5           LDA     B,U                 
A00F: C1 0A           CMPB    #$0A                  
A011: 25 ; ????
A012: 61 ; ????
A013: E6 0F           LDB     15,X                
A015: CB 18           ADDB    #$18                  
A017: C4 F0           ANDB    #$F0                  
A019: CA 1E           ORB     #$1E                  
A01B: C1 F0           CMPB    #$F0                  
A01D: 25 ; ????
A01E: 02 ; ????
A01F: C6 06           LDB     #$06                  
A021: E7 0F           STB     15,X                
A023: 86 01           LDA     #$01                  
A025: B7 10 C0        STA     $10C0                   
A028: BD C5 34        JSR     $C534                   
A02B: 81 FC           CMPA    #$FC                  
A02D: 24 ; ????
A02E: 45 ; ????
A02F: 86 E0           LDA     #$E0                  
A031: AB 0F           ADDA    15,X                
A033: A7 0F           STA     15,X                
A035: 20 3D           BRA     $A074                   
A037: A6 0F           LDA     15,X                
A039: 8B F8           ADDA    #$F8                  
A03B: A7 0F           STA     15,X                
A03D: 20 04           BRA     $A043                   
A03F: A6 0F           LDA     15,X                
A041: 8B 1E           ADDA    #$1E                  
A043: A7 0F           STA     15,X                
A045: 86 01           LDA     #$01                  
A047: B7 10 C0        STA     $10C0                   
A04A: BD C5 34        JSR     $C534                   
A04D: CC 00 70        LDD     #$0070                  
A050: E1 C8 40        CMPB    $40,U                 
A053: 22 02           BHI     $A057                   
A055: 8A 01           ORA     #$01                  
A057: E1 C8 20        CMPB    $20,U                 
A05A: 22 02           BHI     $A05E                   
A05C: 8A 02           ORA     #$02                  
A05E: E1 C4           CMPB    ,U                  
A060: 22 02           BHI     $A064                   
A062: 8A 04           ORA     #$04                  
A064: A1 C8 E0        CMPA    $E0,U                 
A067: 22 02           BHI     $A06B                   
A069: 8A 08           ORA     #$08                  
A06B: CE A0 7B        LDU     #$A07B                  
A06E: E6 C6           LDB     A,U                 
A070: EB 0D           ADDB    13,X                
A072: E7 0D           STB     13,X                
A074: 6F 08           CLR     8,X                 
A076: 7F 10 DA        CLR     $10DA                   
A079: 7E 9F 03        JMP     $9F03                   
A07C: 10 ; ????
A07D: 00 10           NEG     $10                   
A07F: F0 10 00        SUBB    $1000                   
A082: 08 ; ????
A083: F0 00 10        SUBB    $0010                   
A086: 10 ; ????
A087: F0 F0 F8        SUBB    $F0F8                   
A08A: 00 BD           NEG     $BD                   
A08C: 81 50           CMPA    #$50                  
A08E: B6 25 00        LDA     $2500                   
A091: 27 F8           BEQ     $A08B                   
A093: BD A0 FF        JSR     $A0FF                   
A096: BD 8D BB        JSR     $8DBB                   
A099: BD 81 50        JSR     $8150                   
A09C: B6 40 40        LDA     $4040                   
A09F: 26 F8           BNE     $A099                   
A0A1: 7C 10 DC        INC     $10DC                   
A0A4: BD 81 50        JSR     $8150                   
A0A7: B6 25 00        LDA     $2500                   
A0AA: 27 3F           BEQ     $A0EB                   
A0AC: B6 10 D1        LDA     $10D1                   
A0AF: 26 1F           BNE     $A0D0                   
A0B1: B6 10 DA        LDA     $10DA                   
A0B4: 26 EE           BNE     $A0A4                   
A0B6: B6 25 02        LDA     $2502                   
A0B9: 26 E9           BNE     $A0A4                   
A0BB: B6 25 01        LDA     $2501                   
A0BE: 26 E4           BNE     $A0A4                   
A0C0: B6 25 0A        LDA     $250A                   
A0C3: 27 DF           BEQ     $A0A4                   
A0C5: 8E 25 10        LDX     #$2510                  
A0C8: CE A0 F1        LDU     #$A0F1                  
A0CB: 48 ; ????
A0CC: AD D6           JSR     [A,U]               
A0CE: 20 D4           BRA     $A0A4                   
A0D0: B6 25 02        LDA     $2502                   
A0D3: 27 06           BEQ     $A0DB                   
A0D5: BD A5 4F        JSR     $A54F                   
A0D8: 7F 25 02        CLR     $2502                   
A0DB: B6 25 01        LDA     $2501                   
A0DE: 27 03           BEQ     $A0E3                   
A0E0: 7F 25 01        CLR     $2501                   
A0E3: BD 81 50        JSR     $8150                   
A0E6: B6 25 00        LDA     $2500                   
A0E9: 26 F8           BNE     $A0E3                   
A0EB: 8E 25 10        LDX     #$2510                  
A0EE: BD 87 32        JSR     $8732                   
A0F1: 20 98           BRA     $A08B                   
A0F3: A1 17           CMPA    -9,X                
A0F5: A1 CB           CMPA    D,U                 
A0F7: A1 ; ????
A0F8: D2 00           SBCB    $00                   
A0FA: 00 A1           NEG     $A1                   
A0FC: F2 A2 0A        SBCB    $A20A                   
A0FF: 8E 25 10        LDX     #$2510                  
A102: CC 08 01        LDD     #$0801                  
A105: ED 0A           STD     10,X                
A107: 44              LSRA                        
A108: A7 05           STA     5,X                 
A10A: E7 1A           STB     -6,X                
A10C: B6 17 07        LDA     $1707                   
A10F: A7 03           STA     3,X                 
A111: BD C8 EA        JSR     $C8EA                   
A114: 7E C4 80        JMP     $C480                   
A117: B6 10 14        LDA     $1014                   
A11A: 27 04           BEQ     $A120                   
A11C: 7C 25 01        INC     $2501                   
A11F: 39              RTS                         
A120: B6 10 13        LDA     $1013                   
A123: 2A 01           BPL     $A126                   
A125: 39              RTS                         
A126: A1 05           CMPA    5,X                 
A128: 27 7A           BEQ     $A1A4                   
A12A: F6 10 13        LDB     $1013                   
A12D: CB 04           ADDB    #$04                  
A12F: C4 06           ANDB    #$06                  
A131: E1 05           CMPB    5,X                 
A133: 27 63           BEQ     $A198                   
A135: E6 1B           LDB     -5,X                
A137: 10 27 00 83     LBEQ    $A1BE                   
A13B: C1 10           CMPB    #$10                  
A13D: 27 7F           BEQ     $A1BE                   
A13F: B7 10 C3        STA     $10C3                   
A142: 7F 10 C4        CLR     $10C4                   
A145: C1 04           CMPB    #$04                  
A147: 23 07           BLS     $A150                   
A149: C1 0C           CMPB    #$0C                  
A14B: 25 ; ????
A14C: 68 ; ????
A14D: 7C 10 C4        INC     $10C4                   
A150: BD C9 78        JSR     $C978                   
A153: B6 10 D8        LDA     $10D8                   
A156: 26 5D           BNE     $A1B5                   
A158: E6 1B           LDB     -5,X                
A15A: B6 10 C4        LDA     $10C4                   
A15D: 27 14           BEQ     $A173                   
A15F: 53              COMB                        
A160: C4 0F           ANDB    #$0F                  
A162: 5C              INCB                        
A163: E7 1B           STB     -5,X                
A165: F7 10 C2        STB     $10C2                   
A168: E6 05           LDB     5,X                 
A16A: CB 04           ADDB    #$04                  
A16C: 5C              INCB                        
A16D: C4 06           ANDB    #$06                  
A16F: E7 05           STB     5,X                 
A171: 20 03           BRA     $A176                   
A173: F7 10 C2        STB     $10C2                   
A176: B6 10 C3        LDA     $10C3                   
A179: 48 ; ????
A17A: A7 0A           STA     10,X                
A17C: CE A1 90        LDU     #$A190                  
A17F: 84 08           ANDA    #$08                  
A181: 44              LSRA                        
A182: 44              LSRA                        
A183: 44              LSRA                        
A184: AB 05           ADDA    5,X                 
A186: E6 C6           LDB     A,U                 
A188: E7 05           STB     5,X                 
A18A: 86 03           LDA     #$03                  
A18C: A7 1A           STA     -6,X                
A18E: 20 42           BRA     $A1D2                   
A190: 01 ; ????
A191: 07 01           ASR     $01                   
A193: 03 03           COM     $03                   
A195: 05 ; ????
A196: 07 05           ASR     $05                   
A198: E6 1B           LDB     -5,X                
A19A: 27 22           BEQ     $A1BE                   
A19C: 53              COMB                        
A19D: C4 0F           ANDB    #$0F                  
A19F: 5C              INCB                        
A1A0: E7 1B           STB     -5,X                
A1A2: 20 1A           BRA     $A1BE                   
A1A4: E6 1B           LDB     -5,X                
A1A6: 26 0D           BNE     $A1B5                   
A1A8: BD C9 4C        JSR     $C94C                   
A1AB: B6 10 D8        LDA     $10D8                   
A1AE: 27 01           BEQ     $A1B1                   
A1B0: 39              RTS                         
A1B1: 86 10           LDA     #$10                  
A1B3: A7 1B           STA     -5,X                
A1B5: BD C0 00        JSR     $C000                   
A1B8: BD C0 9F        JSR     $C09F                   
A1BB: 7E C4 80        JMP     $C480                   
A1BE: A7 05           STA     5,X                 
A1C0: 48 ; ????
A1C1: A7 0A           STA     10,X                
A1C3: CC 02 08        LDD     #$0208                  
A1C6: A7 1A           STA     -6,X                
A1C8: E7 04           STB     4,X                 
A1CA: 39              RTS                         
A1CB: 6A 04           DEC     4,X                 
A1CD: 26 02           BNE     $A1D1                   
A1CF: 6A 1A           DEC     -6,X                
A1D1: 39              RTS                         
A1D2: A6 1B           LDA     -5,X                
A1D4: 27 09           BEQ     $A1DF                   
A1D6: BD C0 00        JSR     $C000                   
A1D9: BD C0 9F        JSR     $C09F                   
A1DC: 7E C4 80        JMP     $C480                   
A1DF: CC 01 10        LDD     #$0110                  
A1E2: A7 1A           STA     -6,X                
A1E4: F0 10 C2        SUBB    $10C2                   
A1E7: E7 1B           STB     -5,X                
A1E9: B6 10 C3        LDA     $10C3                   
A1EC: A7 05           STA     5,X                 
A1EE: 48 ; ????
A1EF: A7 0A           STA     10,X                
A1F1: 39              RTS                         
A1F2: A6 04           LDA     4,X                 
A1F4: 26 03           BNE     $A1F9                   
A1F6: A7 0B           STA     11,X                
A1F8: 39              RTS                         
A1F9: 4A              DECA                        
A1FA: A7 04           STA     4,X                 
A1FC: 84 30           ANDA    #$30                  
A1FE: 44              LSRA                        
A1FF: 44              LSRA                        
A200: 44              LSRA                        
A201: 44              LSRA                        
A202: 43              COMA                        
A203: 84 03           ANDA    #$03                  
A205: 8B 38           ADDA    #$38                  
A207: A7 0A           STA     10,X                
A209: 39              RTS                         
A20A: B6 10 10        LDA     $1010                   
A20D: 26 0E           BNE     $A21D                   
A20F: B6 10 4F        LDA     $104F                   
A212: 27 09           BEQ     $A21D                   
A214: 7A 10 4F        DEC     $104F                   
A217: 27 01           BEQ     $A21A                   
A219: 39              RTS                         
A21A: 7C 40 51        INC     $4051                   
A21D: A6 04           LDA     4,X                 
A21F: 26 03           BNE     $A224                   
A221: A7 0B           STA     11,X                
A223: 39              RTS                         
A224: 4A              DECA                        
A225: A7 04           STA     4,X                 
A227: 84 30           ANDA    #$30                  
A229: 44              LSRA                        
A22A: 44              LSRA                        
A22B: 44              LSRA                        
A22C: 44              LSRA                        
A22D: 8A 54           ORA     #$54                  
A22F: A7 0A           STA     10,X                
A231: 39              RTS                         
A232: BD 81 50        JSR     $8150                   
A235: B6 40 40        LDA     $4040                   
A238: 26 F8           BNE     $A232                   
A23A: FC 10 D0        LDD     $10D0                   
A23D: 26 F3           BNE     $A232                   
A23F: B6 25 00        LDA     $2500                   
A242: 27 EE           BEQ     $A232                   
A244: B6 10 DA        LDA     $10DA                   
A247: 26 E9           BNE     $A232                   
A249: B6 25 0A        LDA     $250A                   
A24C: 81 03           CMPA    #$03                  
A24E: 27 E2           BEQ     $A232                   
A250: B6 10 15        LDA     $1015                   
A253: 81 01           CMPA    #$01                  
A255: 26 DB           BNE     $A232                   
A257: 8E 25 10        LDX     #$2510                  
A25A: A7 12           STA     -14,X               
A25C: F6 25 01        LDB     $2501                   
A25F: 27 0B           BEQ     $A26C                   
A261: 6F 11           CLR     -15,X               
A263: F6 17 07        LDB     $1707                   
A266: E7 03           STB     3,X                 
A268: 6F 1D           CLR     -3,X                
A26A: 6F 08           CLR     8,X                 
A26C: B7 40 45        STA     $4045                   
A26F: A6 05           LDA     5,X                 
A271: 8B 48           ADDA    #$48                  
A273: A7 0A           STA     10,X                
A275: 6F 88 BA        CLR     $BA,X                 
A278: 8E 24 D0        LDX     #$24D0                  
A27B: CE A2 E9        LDU     #$A2E9                  
A27E: A6 1A           LDA     -6,X                
A280: 48 ; ????
A281: AD D6           JSR     [A,U]               
A283: A6 1A           LDA     -6,X                
A285: 2B 0F           BMI     $A296                   
A287: BD 81 50        JSR     $8150                   
A28A: B6 25 02        LDA     $2502                   
A28D: 27 A3           BEQ     $A232                   
A28F: FC 10 D0        LDD     $10D0                   
A292: 26 9E           BNE     $A232                   
A294: 20 E2           BRA     $A278                   
A296: BD A5 4F        JSR     $A54F                   
A299: B6 25 15        LDA     $2515                   
A29C: 48 ; ????
A29D: B7 25 1A        STA     $251A                   
A2A0: BD 81 50        JSR     $8150                   
A2A3: FC 10 D0        LDD     $10D0                   
A2A6: 26 8A           BNE     $A232                   
A2A8: B6 25 02        LDA     $2502                   
A2AB: 27 85           BEQ     $A232                   
A2AD: 8E 25 10        LDX     #$2510                  
A2B0: B6 10 15        LDA     $1015                   
A2B3: 81 01           CMPA    #$01                  
A2B5: 27 B5           BEQ     $A26C                   
A2B7: B6 10 14        LDA     $1014                   
A2BA: 26 1A           BNE     $A2D6                   
A2BC: B6 10 13        LDA     $1013                   
A2BF: 2B DF           BMI     $A2A0                   
A2C1: CE A2 E1        LDU     #$A2E1                  
A2C4: E6 C6           LDB     A,U                 
A2C6: E1 05           CMPB    5,X                 
A2C8: 26 0C           BNE     $A2D6                   
A2CA: A7 05           STA     5,X                 
A2CC: A6 1B           LDA     -5,X                
A2CE: 27 06           BEQ     $A2D6                   
A2D0: 43              COMA                        
A2D1: 4C              INCA                        
A2D2: 84 0F           ANDA    #$0F                  
A2D4: A7 1B           STA     -5,X                
A2D6: 7F 25 02        CLR     $2502                   
A2D9: A6 05           LDA     5,X                 
A2DB: 48 ; ????
A2DC: A7 0A           STA     10,X                
A2DE: 7E A2 32        JMP     $A232                   
A2E1: 04 70           LSR     $70                   
A2E3: 06 74           ROR     $74                   
A2E5: 00 72           NEG     $72                   
A2E7: 02 ; ????
A2E8: 75 ; ????
A2E9: A2 ; ????
A2EA: F7 A3 8A        STB     $A38A                   
A2ED: A3 3B           SUBD    -5,Y                
A2EF: A3 ; ????
A2F0: 8A A3           ORA     #$A3                  
A2F2: 57              ASRB                        
A2F3: A3 ; ????
A2F4: 8A A4           ORA     #$A4                  
A2F6: C1 A6           CMPB    #$A6                  
A2F8: 88 45           EORA    #$45                  
A2FA: 84 04           ANDA    #$04                  
A2FC: 48 ; ????
A2FD: 8B FC           ADDA    #$FC                  
A2FF: E6 88 45        LDB     $45,X                 
A302: C5 02           BITB    #$02                  
A304: 26 04           BNE     $A30A                   
A306: A7 11           STA     -15,X               
A308: 20 02           BRA     $A30C                   
A30A: A7 12           STA     -14,X               
A30C: A6 88 4F        LDA     $4F,X                 
A30F: 8B F5           ADDA    #$F5                  
A311: A7 0F           STA     15,X                
A313: EE 88 3E        LDU     $3E,X                 
A316: EF 1E           STU     -2,X                
A318: A6 88 4D        LDA     $4D,X                 
A31B: A7 0D           STA     13,X                
A31D: A6 88 45        LDA     $45,X                 
A320: 44              LSRA                        
A321: 8B 78           ADDA    #$78                  
A323: A7 0A           STA     10,X                
A325: 86 05           LDA     #$05                  
A327: A7 0B           STA     11,X                
A329: A6 88 45        LDA     $45,X                 
A32C: 84 02           ANDA    #$02                  
A32E: 8B 02           ADDA    #$02                  
A330: A7 14           STA     -12,X               
A332: CC 00 C0        LDD     #$00C0                  
A335: A7 1D           STA     -3,X                
A337: E7 03           STB     3,X                 
A339: 20 49           BRA     $A384                   
A33B: A6 0F           LDA     15,X                
A33D: A7 88 2F        STA     $2F,X                 
A340: A6 0D           LDA     13,X                
A342: A7 88 2D        STA     $2D,X                 
A345: CE A2 E2        LDU     #$A2E2                  
A348: A6 88 45        LDA     $45,X                 
A34B: E6 C6           LDB     A,U                 
A34D: E7 88 2A        STB     $2A,X                 
A350: 86 05           LDA     #$05                  
A352: A7 88 2B        STA     $2B,X                 
A355: 20 2A           BRA     $A381                   
A357: A6 88 45        LDA     $45,X                 
A35A: 85 02           BITA    #$02                  
A35C: 26 13           BNE     $A371                   
A35E: C6 04           LDB     #$04                  
A360: E7 88 28        STB     $28,X                 
A363: 58 ; ????
A364: 85 04           BITA    #$04                  
A366: 26 01           BNE     $A369                   
A368: 50              NEGB                        
A369: EB 88 2F        ADDB    $2F,X                 
A36C: E7 88 2F        STB     $2F,X                 
A36F: 20 10           BRA     $A381                   
A371: C6 08           LDB     #$08                  
A373: E7 88 28        STB     $28,X                 
A376: 85 04           BITA    #$04                  
A378: 26 01           BNE     $A37B                   
A37A: 50              NEGB                        
A37B: EB 88 2D        ADDB    $2D,X                 
A37E: E7 88 2D        STB     $2D,X                 
A381: 6F 88 2C        CLR     $2C,X                 
A384: 86 04           LDA     #$04                  
A386: A7 1B           STA     -5,X                
A388: 6C 1A           INC     -6,X                
A38A: B6 10 13        LDA     $1013                   
A38D: 2B 0A           BMI     $A399                   
A38F: A1 88 45        CMPA    $45,X                 
A392: 27 05           BEQ     $A399                   
A394: 86 FF           LDA     #$FF                  
A396: A7 1A           STA     -6,X                
A398: 39              RTS                         
A399: A6 1D           LDA     -3,X                
A39B: AB 03           ADDA    3,X                 
A39D: 25 ; ????
A39E: 04 A7           LSR     $A7                   
A3A0: 1D              SEX                         
A3A1: 20 1C           BRA     $A3BF                   
A3A3: A7 1D           STA     -3,X                
A3A5: 6A 1B           DEC     -5,X                
A3A7: A6 11           LDA     -15,X               
A3A9: AB 0F           ADDA    15,X                
A3AB: 81 01           CMPA    #$01                  
A3AD: 27 E5           BEQ     $A394                   
A3AF: A7 0F           STA     15,X                
A3B1: A6 12           LDA     -14,X               
A3B3: EE 1E           LDU     -2,X                
A3B5: 33 C6           LEAU    A,U                 
A3B7: EF 1E           STU     -2,X                
A3B9: AB 0D           ADDA    13,X                
A3BB: A7 0D           STA     13,X                
A3BD: 6F 0C           CLR     12,X                
A3BF: EE 1E           LDU     -2,X                
A3C1: FF 10 3A        STU     $103A                   
A3C4: CE 25 30        LDU     #$2530                  
A3C7: 86 0B           LDA     #$0B                  
A3C9: AB 0F           ADDA    15,X                
A3CB: A7 0F           STA     15,X                
A3CD: A6 50           LDA     -16,U               
A3CF: 27 36           BEQ     $A407                   
A3D1: A6 4D           LDA     13,U                
A3D3: 27 32           BEQ     $A407                   
A3D5: A6 5A           LDA     -6,U                
A3D7: 81 12           CMPA    #$12                  
A3D9: 27 1D           BEQ     $A3F8                   
A3DB: 81 0D           CMPA    #$0D                  
A3DD: 24 ; ????
A3DE: 28 81           BVC     $A361                   
A3E0: 06 23           ROR     $23                   
A3E2: 15 ; ????
A3E3: 81 0B           CMPA    #$0B                  
A3E5: 24 ; ????
A3E6: 11 ; ????
A3E7: A6 45           LDA     5,U                 
A3E9: 84 04           ANDA    #$04                  
A3EB: 48 ; ????
A3EC: 48 ; ????
A3ED: 8B F8           ADDA    #$F8                  
A3EF: 10 BE 10 3A     LDY     $103A                   
A3F3: 31 A6           LEAY    A,Y                 
A3F5: 10 AF 1E        STY     -2,X                
A3F8: BD C4 F4        JSR     $C4F4                   
A3FB: B6 10 D3        LDA     $10D3                   
A3FE: 26 26           BNE     $A426                   
A400: 10 BE 10 3A     LDY     $103A                   
A404: 10 AF 1E        STY     -2,X                
A407: 33 C8 20        LEAU    $20,U                 
A40A: 11 83 26 70     CMPU    #$2670                  
A40E: 26 BD           BNE     $A3CD                   
A410: 86 F5           LDA     #$F5                  
A412: AB 0F           ADDA    15,X                
A414: A7 0F           STA     15,X                
A416: A6 1B           LDA     -5,X                
A418: 27 01           BEQ     $A41B                   
A41A: 39              RTS                         
A41B: A6 1A           LDA     -6,X                
A41D: 4C              INCA                        
A41E: 81 06           CMPA    #$06                  
A420: 25 ; ????
A421: 01 ; ????
A422: 40              NEGA                        
A423: A7 1A           STA     -6,X                
A425: 39              RTS                         
A426: 10 BE 10 3A     LDY     $103A                   
A42A: 10 AF 1E        STY     -2,X                
A42D: EF 15           STU     -11,X               
A42F: A6 5A           LDA     -6,U                
A431: 81 02           CMPA    #$02                  
A433: 26 1F           BNE     $A454                   
A435: 68 ; ????
A436: 43              COMA                        
A437: 68 ; ????
A438: 43              COMA                        
A439: 6F 54           CLR     -12,U               
A43B: A6 5B           LDA     -5,U                
A43D: 27 15           BEQ     $A454                   
A43F: 84 0F           ANDA    #$0F                  
A441: A7 5B           STA     -5,U                
A443: 81 09           CMPA    #$09                  
A445: 25 ; ????
A446: 0D 40           TST     $40                   
A448: 84 0F           ANDA    #$0F                  
A44A: A7 5B           STA     -5,U                
A44C: A6 45           LDA     5,U                 
A44E: 8B 04           ADDA    #$04                  
A450: 84 07           ANDA    #$07                  
A452: A7 45           STA     5,U                 
A454: CC 06 F5        LDD     #$06F5                  
A457: A7 1A           STA     -6,X                
A459: 7F 40 45        CLR     $4045                   
A45C: EB 0F           ADDB    15,X                
A45E: E7 0F           STB     15,X                
A460: 86 6A           LDA     #$6A                  
A462: E6 59           LDB     -7,U                
A464: 2A 01           BPL     $A467                   
A466: 4C              INCA                        
A467: A7 4A           STA     10,U                
A469: 6C 52           INC     -14,U               
A46B: A6 52           LDA     -14,U               
A46D: 81 04           CMPA    #$04                  
A46F: 10 27 00 B5     LBEQ    $A528                   
A473: 86 5A           LDA     #$5A                  
A475: A7 44           STA     4,U                 
A477: A6 5A           LDA     -6,U                
A479: 81 0C           CMPA    #$0C                  
A47B: 27 3C           BEQ     $A4B9                   
A47D: E6 59           LDB     -7,U                
A47F: 2A 32           BPL     $A4B3                   
A481: 81 06           CMPA    #$06                  
A483: 25 ; ????
A484: 2E 27           BGT     $A4AD                   
A486: 2A 81           BPL     $A409                   
A488: 0B ; ????
A489: 24 ; ????
A48A: 28 A6           BVC     $A432                   
A48C: 45 ; ????
A48D: 84 04           ANDA    #$04                  
A48F: 48 ; ????
A490: 48 ; ????
A491: 8B F8           ADDA    #$F8                  
A493: 40              NEGA                        
A494: 10 AE 5E        LDY     -2,U                
A497: 31 A6           LEAY    A,Y                 
A499: 10 AF 5E        STY     -2,U                
A49C: AB 4D           ADDA    13,U                
A49E: A7 4D           STA     13,U                
A4A0: A6 53           LDA     -13,U               
A4A2: 27 0D           BEQ     $A4B1                   
A4A4: BF 10 36        STX     $1036                   
A4A7: AE 55           LDX     -11,U               
A4A9: BD 87 32        JSR     $8732                   
A4AC: BE 10 36        LDX     $1036                   
A4AF: 6F 53           CLR     -13,U               
A4B1: 6F 5B           CLR     -5,U                
A4B3: 86 0C           LDA     #$0C                  
A4B5: A7 5A           STA     -6,U                
A4B7: 6F 54           CLR     -12,U               
A4B9: 86 24           LDA     #$24                  
A4BB: A7 04           STA     4,X                 
A4BD: A6 1C           LDA     -4,X                
A4BF: 26 3F           BNE     $A500                   
A4C1: 6F 1C           CLR     -4,X                
A4C3: B6 10 13        LDA     $1013                   
A4C6: 2B 05           BMI     $A4CD                   
A4C8: 86 FF           LDA     #$FF                  
A4CA: A7 1A           STA     -6,X                
A4CC: 39              RTS                         
A4CD: EE 15           LDU     -11,X               
A4CF: A6 5A           LDA     -6,U                
A4D1: 81 0C           CMPA    #$0C                  
A4D3: 26 F3           BNE     $A4C8                   
A4D5: A6 52           LDA     -14,U               
A4D7: 27 EF           BEQ     $A4C8                   
A4D9: 6A 04           DEC     4,X                 
A4DB: 27 15           BEQ     $A4F2                   
A4DD: B6 10 15        LDA     $1015                   
A4E0: 26 01           BNE     $A4E3                   
A4E2: 39              RTS                         
A4E3: 81 01           CMPA    #$01                  
A4E5: 26 19           BNE     $A500                   
A4E7: 64 04           LSR     4,X                 
A4E9: 26 15           BNE     $A500                   
A4EB: A7 1C           STA     -4,X                
A4ED: 6F 04           CLR     4,X                 
A4EF: 7E A4 69        JMP     $A469                   
A4F2: B6 10 15        LDA     $1015                   
A4F5: 10 26 FF 70     LBNE    $A469                   
A4F9: 86 0E           LDA     #$0E                  
A4FB: A7 04           STA     4,X                 
A4FD: 39              RTS                         
A4FE: A7 04           STA     4,X                 
A500: B6 10 01        LDA     $1001                   
A503: 84 04           ANDA    #$04                  
A505: 44              LSRA                        
A506: 44              LSRA                        
A507: B7 10 34        STA     $1034                   
A50A: 86 01           LDA     #$01                  
A50C: B7 40 46        STA     $4046                   
A50F: A6 88 4A        LDA     $4A,X                 
A512: 84 4E           ANDA    #$4E                  
A514: BA 10 34        ORA     $1034                   
A517: A7 88 4A        STA     $4A,X                 
A51A: B6 10 01        LDA     $1001                   
A51D: 84 02           ANDA    #$02                  
A51F: 44              LSRA                        
A520: 8B 06           ADDA    #$06                  
A522: A7 88 2B        STA     $2B,X                 
A525: A7 0B           STA     11,X                
A527: 39              RTS                         
A528: 7C 40 50        INC     $4050                   
A52B: CC 1E 0D        LDD     #$1E0D                  
A52E: A7 44           STA     4,U                 
A530: E7 5A           STB     -6,U                
A532: A6 88 45        LDA     $45,X                 
A535: 84 02           ANDA    #$02                  
A537: A7 54           STA     -12,U               
A539: 86 D0           LDA     #$D0                  
A53B: E6 59           LDB     -7,U                
A53D: 2A 02           BPL     $A541                   
A53F: 8B 0C           ADDA    #$0C                  
A541: A7 4A           STA     10,U                
A543: CC 00 FF        LDD     #$00FF                  
A546: B7 40 45        STA     $4045                   
A549: B7 40 46        STA     $4046                   
A54C: E7 1A           STB     -6,X                
A54E: 39              RTS                         
A54F: 8E 24 D0        LDX     #$24D0                  
A552: BD 87 32        JSR     $8732                   
A555: 8E 24 F0        LDX     #$24F0                  
A558: 7E 87 32        JMP     $8732                   
A55B: BD 81 50        JSR     $8150                   
A55E: B6 25 01        LDA     $2501                   
A561: 27 F8           BEQ     $A55B                   
A563: B7 40 47        STA     $4047                   
A566: 8E 25 10        LDX     #$2510                  
A569: BD A6 78        JSR     $A678                   
A56C: 64 03           LSR     3,X                 
A56E: A6 1B           LDA     -5,X                
A570: 27 4A           BEQ     $A5BC                   
A572: E6 05           LDB     5,X                 
A574: CE A6 8C        LDU     #$A68C                  
A577: A1 C5           CMPA    B,U                 
A579: 23 05           BLS     $A580                   
A57B: 5C              INCB                        
A57C: A1 C5           CMPA    B,U                 
A57E: 25 ; ????
A57F: 2A 86           BPL     $A507                   
A581: 04 AB           LSR     $AB                   
A583: 0F 84           CLR     $84                   
A585: F0 A7 0F        SUBB    $A70F                   
A588: CC 00 04        LDD     #$0004                  
A58B: E3 1E           ADDD    -2,X                
A58D: C4 F0           ANDB    #$F0                  
A58F: ED 1E           STD     -2,X                
A591: 6F 1B           CLR     -5,X                
A593: BD C4 80        JSR     $C480                   
A596: 20 24           BRA     $A5BC                   
A598: BD 81 50        JSR     $8150                   
A59B: B6 25 01        LDA     $2501                   
A59E: 27 BB           BEQ     $A55B                   
A5A0: B7 40 47        STA     $4047                   
A5A3: B6 10 14        LDA     $1014                   
A5A6: 10 27 00 B7     LBEQ    $A661                   
A5AA: 8E 25 10        LDX     #$2510                  
A5AD: A6 1B           LDA     -5,X                
A5AF: 27 0B           BEQ     $A5BC                   
A5B1: BD C0 00        JSR     $C000                   
A5B4: BD C4 80        JSR     $C480                   
A5B7: BD C0 78        JSR     $C078                   
A5BA: 20 DC           BRA     $A598                   
A5BC: 86 01           LDA     #$01                  
A5BE: B7 10 C0        STA     $10C0                   
A5C1: BD C5 34        JSR     $C534                   
A5C4: C1 30           CMPB    #$30                  
A5C6: 26 7B           BNE     $A643                   
A5C8: FF 10 3E        STU     $103E                   
A5CB: E6 05           LDB     5,X                 
A5CD: 20 13           BRA     $A5E2                   
A5CF: F6 10 13        LDB     $1013                   
A5D2: 2B 2D           BMI     $A601                   
A5D4: E1 05           CMPB    5,X                 
A5D6: 27 0A           BEQ     $A5E2                   
A5D8: E7 05           STB     5,X                 
A5DA: BD A6 78        JSR     $A678                   
A5DD: E6 05           LDB     5,X                 
A5DF: FE 10 3E        LDU     $103E                   
A5E2: C5 04           BITB    #$04                  
A5E4: 26 04           BNE     $A5EA                   
A5E6: A6 C4           LDA     ,U                  
A5E8: 20 03           BRA     $A5ED                   
A5EA: A6 C8 21        LDA     $21,U                 
A5ED: C5 02           BITB    #$02                  
A5EF: 26 06           BNE     $A5F7                   
A5F1: 85 01           BITA    #$01                  
A5F3: 26 0C           BNE     $A601                   
A5F5: 20 04           BRA     $A5FB                   
A5F7: 85 02           BITA    #$02                  
A5F9: 26 06           BNE     $A601                   
A5FB: F7 10 40        STB     $1040                   
A5FE: 7C 10 D5        INC     $10D5                   
A601: BD C0 78        JSR     $C078                   
A604: BD 81 50        JSR     $8150                   
A607: B6 25 01        LDA     $2501                   
A60A: 10 27 FF 4D     LBEQ    $A55B                   
A60E: B6 10 14        LDA     $1014                   
A611: 27 4E           BEQ     $A661                   
A613: B7 40 47        STA     $4047                   
A616: 8E 25 10        LDX     #$2510                  
A619: B6 10 D5        LDA     $10D5                   
A61C: 26 E3           BNE     $A601                   
A61E: FE 10 3E        LDU     $103E                   
A621: E6 C9 08 00     LDB     $0800,U                 
A625: C1 30           CMPB    #$30                  
A627: 27 A6           BEQ     $A5CF                   
A629: 20 D6           BRA     $A601                   
A62B: BD C0 78        JSR     $C078                   
A62E: BD 81 50        JSR     $8150                   
A631: B6 25 01        LDA     $2501                   
A634: 10 27 FF 23     LBEQ    $A55B                   
A638: B6 10 14        LDA     $1014                   
A63B: 27 24           BEQ     $A661                   
A63D: B7 40 47        STA     $4047                   
A640: 8E 25 10        LDX     #$2510                  
A643: B6 10 13        LDA     $1013                   
A646: 2B E3           BMI     $A62B                   
A648: A1 05           CMPA    5,X                 
A64A: 27 06           BEQ     $A652                   
A64C: A7 05           STA     5,X                 
A64E: 8D 28           BSR     $A678                   
A650: A6 05           LDA     5,X                 
A652: BD C9 4C        JSR     $C94C                   
A655: B6 10 D8        LDA     $10D8                   
A658: 26 D1           BNE     $A62B                   
A65A: 86 10           LDA     #$10                  
A65C: A7 1B           STA     -5,X                
A65E: 7E A5 B1        JMP     $A5B1                   
A661: 8E 25 10        LDX     #$2510                  
A664: A6 05           LDA     5,X                 
A666: 48 ; ????
A667: A7 0A           STA     10,X                
A669: B6 17 07        LDA     $1707                   
A66C: A7 03           STA     3,X                 
A66E: 6F 08           CLR     8,X                 
A670: 6F 1D           CLR     -3,X                
A672: 7F 25 01        CLR     $2501                   
A675: 7E A5 5B        JMP     $A55B                   
A678: CE A6 84        LDU     #$A684                  
A67B: E6 05           LDB     5,X                 
A67D: EC C5           LDD     B,U                 
A67F: A7 0A           STA     10,X                
A681: E7 08           STB     8,X                 
A683: 39              RTS                         
A684: 30 04           LEAX    4,X                 
A686: 20 04           BRA     $A68C                   
A688: 28 04           BVC     $A68E                   
A68A: 20 06           BRA     $A692                   
A68C: 04 0C           LSR     $0C                   
A68E: 04 0C           LSR     $0C                   
A690: 04 09           LSR     $09                   
A692: 04 0C           LSR     $0C                   
A694: 7F 10 D5        CLR     $10D5                   
A697: BD 81 50        JSR     $8150                   
A69A: B6 10 D5        LDA     $10D5                   
A69D: 27 F8           BEQ     $A697                   
A69F: B6 10 3F        LDA     $103F                   
A6A2: 84 1C           ANDA    #$1C                  
A6A4: 44              LSRA                        
A6A5: 44              LSRA                        
A6A6: B7 10 CE        STA     $10CE                   
A6A9: FC 10 3E        LDD     $103E                   
A6AC: 58 ; ????
A6AD: 49              ROLA                        
A6AE: 48 ; ????
A6AF: 48 ; ????
A6B0: 48 ; ????
A6B1: BB 10 CE        ADDA    $10CE                   
A6B4: B7 10 C1        STA     $10C1                   
A6B7: CE 15 00        LDU     #$1500                  
A6BA: 8E A8 3C        LDX     #$A83C                  
A6BD: F6 10 40        LDB     $1040                   
A6C0: 3A              ABX                         
A6C1: 33 C6           LEAU    A,U                 
A6C3: E6 80           LDB     ,X+                 
A6C5: A6 C5           LDA     B,U                 
A6C7: 2B CB           BMI     $A694                   
A6C9: E6 84           LDB     ,X                  
A6CB: A6 C5           LDA     B,U                 
A6CD: 2B C5           BMI     $A694                   
A6CF: CE A8 2C        LDU     #$A82C                  
A6D2: B6 10 40        LDA     $1040                   
A6D5: 48 ; ????
A6D6: 33 C6           LEAU    A,U                 
A6D8: EC C1           LDD     ,U++                
A6DA: BE 10 3E        LDX     $103E                   
A6DD: 3A              ABX                         
A6DE: BF 10 41        STX     $1041                   
A6E1: 1F 89           TFR     A,B                   
A6E3: 84 0C           ANDA    #$0C                  
A6E5: B7 10 46        STA     $1046                   
A6E8: C4 03           ANDB    #$03                  
A6EA: F7 10 3C        STB     $103C                   
A6ED: EC C4           LDD     ,U                  
A6EF: FD 10 43        STD     $1043                   
A6F2: 86 04           LDA     #$04                  
A6F4: B7 10 45        STA     $1045                   
A6F7: 20 06           BRA     $A6FF                   
A6F9: BD 81 50        JSR     $8150                   
A6FC: BE 10 41        LDX     $1041                   
A6FF: 86 02           LDA     #$02                  
A701: B7 10 09        STA     $1009                   
A704: B6 10 46        LDA     $1046                   
A707: B7 10 CE        STA     $10CE                   
A70A: A6 84           LDA     ,X                  
A70C: 2B 35           BMI     $A743                   
A70E: E6 89 08 00     LDB     $0800,X                 
A712: C1 30           CMPB    #$30                  
A714: 27 41           BEQ     $A757                   
A716: C1 1F           CMPB    #$1F                  
A718: 23 1B           BLS     $A735                   
A71A: C5 04           BITB    #$04                  
A71C: 27 04           BEQ     $A722                   
A71E: C4 0F           ANDB    #$0F                  
A720: 20 13           BRA     $A735                   
A722: 81 66           CMPA    #$66                  
A724: 26 04           BNE     $A72A                   
A726: 8B 1F           ADDA    #$1F                  
A728: 20 07           BRA     $A731                   
A72A: 81 65           CMPA    #$65                  
A72C: 26 01           BNE     $A72F                   
A72E: 4C              INCA                        
A72F: 8B 20           ADDA    #$20                  
A731: C4 0F           ANDB    #$0F                  
A733: 20 03           BRA     $A738                   
A735: BB 10 3C        ADDA    $103C                   
A738: A7 84           STA     ,X                  
A73A: FA 10 CE        ORB     $10CE                   
A73D: E7 89 08 00     STB     $0800,X                 
A741: 20 19           BRA     $A75C                   
A743: CE C4 21        LDU     #$C421                  
A746: A1 C0           CMPA    ,U+                 
A748: 27 08           BEQ     $A752                   
A74A: 11 83 C4 40     CMPU    #$C440                  
A74E: 26 F6           BNE     $A746                   
A750: 33 41           LEAU    1,U                 
A752: E6 C8 3E        LDB     $3E,U                 
A755: 20 E6           BRA     $A73D                   
A757: BB 10 3C        ADDA    $103C                   
A75A: A7 84           STA     ,X                  
A75C: 7A 10 09        DEC     $1009                   
A75F: 27 0C           BEQ     $A76D                   
A761: 74 10 CE        LSR     $10CE                   
A764: 74 10 CE        LSR     $10CE                   
A767: F6 10 44        LDB     $1044                   
A76A: 3A              ABX                         
A76B: 20 9D           BRA     $A70A                   
A76D: 7A 10 45        DEC     $1045                   
A770: 27 0E           BEQ     $A780                   
A772: BE 10 41        LDX     $1041                   
A775: B6 10 43        LDA     $1043                   
A778: 30 86           LEAX    A,X                 
A77A: BF 10 41        STX     $1041                   
A77D: 7E A6 F9        JMP     $A6F9                   
A780: B6 10 C1        LDA     $10C1                   
A783: 8E 15 00        LDX     #$1500                  
A786: 30 86           LEAX    A,X                 
A788: F6 10 40        LDB     $1040                   
A78B: CE A8 3C        LDU     #$A83C                  
A78E: 33 C5           LEAU    B,U                 
A790: E6 C0           LDB     ,U+                 
A792: 3A              ABX                         
A793: E6 84           LDB     ,X                  
A795: FA 10 46        ORB     $1046                   
A798: C1 0F           CMPB    #$0F                  
A79A: 26 02           BNE     $A79E                   
A79C: CA 80           ORB     #$80                  
A79E: E7 84           STB     ,X                  
A7A0: E6 C4           LDB     ,U                  
A7A2: 3A              ABX                         
A7A3: E6 84           LDB     ,X                  
A7A5: FA 10 CE        ORB     $10CE                   
A7A8: C1 0F           CMPB    #$0F                  
A7AA: 26 02           BNE     $A7AE                   
A7AC: CA 80           ORB     #$80                  
A7AE: E7 84           STB     ,X                  
A7B0: 8E 15 00        LDX     #$1500                  
A7B3: F6 10 C1        LDB     $10C1                   
A7B6: 3A              ABX                         
A7B7: A6 84           LDA     ,X                  
A7B9: 84 0C           ANDA    #$0C                  
A7BB: B7 10 34        STA     $1034                   
A7BE: A6 09           LDA     9,X                 
A7C0: 84 03           ANDA    #$03                  
A7C2: BA 10 34        ORA     $1034                   
A7C5: 8E A8 44        LDX     #$A844                  
A7C8: E6 86           LDB     A,X                 
A7CA: 27 06           BEQ     $A7D2                   
A7CC: BD C5 74        JSR     $C574                   
A7CF: 7E A6 94        JMP     $A694                   
A7D2: B6 10 40        LDA     $1040                   
A7D5: 81 04           CMPA    #$04                  
A7D7: 10 26 FE B9     LBNE    $A694                   
A7DB: 8E 15 80        LDX     #$1580                  
A7DE: F6 10 C1        LDB     $10C1                   
A7E1: 3A              ABX                         
A7E2: E6 02           LDB     2,X                 
A7E4: C1 0B           CMPB    #$0B                  
A7E6: 10 ; ????
A7E7: 25 ; ????
A7E8: FE AA E6        LDU     $AAE6                   
A7EB: 0A C1           DEC     $C1                   
A7ED: 0B ; ????
A7EE: 10 ; ????
A7EF: 25 ; ????
A7F0: FE A2 CE        LDU     $A2CE                   
A7F3: C3 A1 58        ADDD    #$A158                  
A7F6: 58 ; ????
A7F7: A6 C5           LDA     B,U                 
A7F9: 48 ; ????
A7FA: 48 ; ????
A7FB: E6 02           LDB     2,X                 
A7FD: 58 ; ????
A7FE: 58 ; ????
A7FF: CB 02           ADDB    #$02                  
A801: AA C5           ORA     B,U                 
A803: 10 8E A8 54     LDY     #$A854                  
A807: BE 10 41        LDX     $1041                   
A80A: E6 A0           LDB     ,Y+                 
A80C: 10 27 FE 84     LBEQ    $A694                   
A810: 3A              ABX                         
A811: 44              LSRA                        
A812: 24 ; ????
A813: F6 E6 84        LDB     $E684                   
A816: CE C4 21        LDU     #$C421                  
A819: E1 C0           CMPB    ,U+                 
A81B: 27 06           BEQ     $A823                   
A81D: 11 83 C4 40     CMPU    #$C440                  
A821: 26 F6           BNE     $A819                   
A823: E6 C8 3E        LDB     $3E,U                 
A826: E7 89 08 00     STB     $0800,X                 
A82A: 20 DE           BRA     $A80A                   
A82C: 09 00           ROL     $00                   
A82E: FF 20 06        STU     $2006                   
A831: 00 E0           NEG     $E0                   
A833: 01 ; ????
A834: 09 01           ROL     $01                   
A836: 01 ; ????
A837: 20 06           BRA     $A83F                   
A839: 20 20           BRA     $A85B                   
A83B: 01 ; ????
A83C: 00 08           NEG     $08                   
A83E: 00 01           NEG     $01                   
A840: 01 ; ????
A841: 08 ; ????
A842: 08 ; ????
A843: 01 ; ????
A844: 00 00           NEG     $00                   
A846: 00 0C           NEG     $0C                   
A848: 00 0A           NEG     $0A                   
A84A: 06 0E           ROR     $0E                   
A84C: 00 09           NEG     $09                   
A84E: 05 ; ????
A84F: 0D 03           TST     $03                   
A851: 0B ; ????
A852: 07 0F           ASR     $0F                   
A854: 01 ; ????
A855: 01 ; ????
A856: 1F 01           TFR     D,X                   
A858: 00 BD           NEG     $BD                   
A85A: 81 50           CMPA    #$50                  
A85C: B6 40 40        LDA     $4040                   
A85F: 26 F8           BNE     $A859                   
A861: B6 10 D6        LDA     $10D6                   
A864: 27 F3           BEQ     $A859                   
A866: 86 3C           LDA     #$3C                  
A868: B7 10 50        STA     $1050                   
A86B: BD 81 50        JSR     $8150                   
A86E: B6 10 D6        LDA     $10D6                   
A871: 27 E6           BEQ     $A859                   
A873: B6 10 50        LDA     $1050                   
A876: 10 26 00 AA     LBNE    $A924                   
A87A: FC 10 D0        LDD     $10D0                   
A87D: 10 26 00 A3     LBNE    $A924                   
A881: B6 17 17        LDA     $1717                   
A884: 10 27 00 9C     LBEQ    $A924                   
A888: B6 10 E4        LDA     $10E4                   
A88B: 10 27 00 95     LBEQ    $A924                   
A88F: B6 10 5C        LDA     $105C                   
A892: 27 05           BEQ     $A899                   
A894: 7A 10 5C        DEC     $105C                   
A897: 26 1F           BNE     $A8B8                   
A899: 8E 25 30        LDX     #$2530                  
A89C: A6 10           LDA     -16,X               
A89E: 27 10           BEQ     $A8B0                   
A8A0: A6 1A           LDA     -6,X                
A8A2: 81 01           CMPA    #$01                  
A8A4: 26 0A           BNE     $A8B0                   
A8A6: CC 00 03        LDD     #$0003                  
A8A9: E7 1A           STB     -6,X                
A8AB: B7 10 E4        STA     $10E4                   
A8AE: 20 08           BRA     $A8B8                   
A8B0: 30 88 20        LEAX    $20,X                 
A8B3: 8C 26 70        CMPX    #$2670                  
A8B6: 26 E4           BNE     $A89C                   
A8B8: B6 10 DB        LDA     $10DB                   
A8BB: 26 1A           BNE     $A8D7                   
A8BD: F6 17 17        LDB     $1717                   
A8C0: 8E 25 30        LDX     #$2530                  
A8C3: A6 10           LDA     -16,X               
A8C5: 27 0A           BEQ     $A8D1                   
A8C7: A6 19           LDA     -7,X                
A8C9: 2A 06           BPL     $A8D1                   
A8CB: A6 11           LDA     -15,X               
A8CD: 27 02           BEQ     $A8D1                   
A8CF: 6A 11           DEC     -15,X               
A8D1: 30 88 20        LEAX    $20,X                 
A8D4: 5A              DECB                        
A8D5: 26 EC           BNE     $A8C3                   
A8D7: B6 10 49        LDA     $1049                   
A8DA: 27 48           BEQ     $A924                   
A8DC: 7A 10 49        DEC     $1049                   
A8DF: 26 05           BNE     $A8E6                   
A8E1: FC 17 1D        LDD     $171D                   
A8E4: 20 0B           BRA     $A8F1                   
A8E6: B6 17 17        LDA     $1717                   
A8E9: B1 17 1C        CMPA    $171C                   
A8EC: 22 36           BHI     $A924                   
A8EE: FC 17 0A        LDD     $170A                   
A8F1: 7D 10 DB        TST     $10DB                   
A8F4: 27 03           BEQ     $A8F9                   
A8F6: 7F 10 DB        CLR     $10DB                   
A8F9: B7 10 34        STA     $1034                   
A8FC: 8E 25 30        LDX     #$2530                  
A8FF: A6 10           LDA     -16,X               
A901: 27 13           BEQ     $A916                   
A903: A6 1A           LDA     -6,X                
A905: 81 02           CMPA    #$02                  
A907: 27 0D           BEQ     $A916                   
A909: A6 19           LDA     -7,X                
A90B: 2A 07           BPL     $A914                   
A90D: B6 10 34        LDA     $1034                   
A910: A7 03           STA     3,X                 
A912: 20 02           BRA     $A916                   
A914: E7 03           STB     3,X                 
A916: 30 88 20        LEAX    $20,X                 
A919: 8C 26 70        CMPX    #$2670                  
A91C: 26 E1           BNE     $A8FF                   
A91E: CC 00 01        LDD     #$0001                  
A921: FD 10 DC        STD     $10DC                   
A924: B6 10 D7        LDA     $10D7                   
A927: 10 27 FF 40     LBEQ    $A86B                   
A92B: CC 00 09        LDD     #$0009                  
A92E: B7 10 CD        STA     $10CD                   
A931: B7 10 34        STA     $1034                   
A934: 8E 14 00        LDX     #$1400                  
A937: A6 85           LDA     B,X                 
A939: 2F 4E           BLE     $A989                   
A93B: 6A 85           DEC     B,X                 
A93D: 26 47           BNE     $A986                   
A93F: 6A 85           DEC     B,X                 
A941: F7 10 35        STB     $1035                   
A944: 7C 10 34        INC     $1034                   
A947: 3A              ABX                         
A948: A6 89 01 80     LDA     $0180,X                 
A94C: 8D 7A           BSR     $A9C8                   
A94E: 86 0A           LDA     #$0A                  
A950: A1 89 01 7F     CMPA    $017F,X                 
A954: 23 05           BLS     $A95B                   
A956: 4C              INCA                        
A957: AB 89 01 7F     ADDA    $017F,X                 
A95B: CE 12 F7        LDU     #$12F7                  
A95E: E6 89 FE 80     LDB     $FE80,X                 
A962: 6A C5           DEC     B,U                 
A964: 26 05           BNE     $A96B                   
A966: 7C 10 E6        INC     $10E6                   
A969: 6A C5           DEC     B,U                 
A96B: 8D 35           BSR     $A9A2                   
A96D: 30 01           LEAX    1,X                 
A96F: 7C 10 35        INC     $1035                   
A972: A6 89 01 80     LDA     $0180,X                 
A976: 81 0A           CMPA    #$0A                  
A978: 23 06           BLS     $A980                   
A97A: 8D 4C           BSR     $A9C8                   
A97C: 86 0A           LDA     #$0A                  
A97E: 8D 22           BSR     $A9A2                   
A980: F6 10 35        LDB     $1035                   
A983: 8E 14 00        LDX     #$1400                  
A986: 7C 10 CD        INC     $10CD                   
A989: 5C              INCB                        
A98A: C1 6F           CMPB    #$6F                  
A98C: 25 ; ????
A98D: A9 B6           ADCA    [A,Y]               
A98F: 10 ; ????
A990: 34 27           PSHS    Y,B,A,CC                   
A992: 03 BD           COM     $BD                   
A994: C9 DA           ADCB    #$DA                  
A996: BD CC 6A        JSR     $CC6A                   
A999: B6 10 CD        LDA     $10CD                   
A99C: B7 10 D7        STA     $10D7                   
A99F: 7E A8 6B        JMP     $A86B                   
A9A2: BF 10 36        STX     $1036                   
A9A5: 10 8E D0 E8     LDY     #$D0E8                  
A9A9: A7 89 01 80     STA     $0180,X                 
A9AD: 8E D3 88        LDX     #$D388                  
A9B0: F6 10 35        LDB     $1035                   
A9B3: 58 ; ????
A9B4: 3A              ABX                         
A9B5: BF 10 3A        STX     $103A                   
A9B8: AE 9F 10 3A     LDX     [$103A]                 
A9BC: C6 20           LDB     #$20                  
A9BE: 3D              MUL                         
A9BF: 31 AB           LEAY    D,Y                 
A9C1: BD C1 67        JSR     $C167                   
A9C4: BE 10 36        LDX     $1036                   
A9C7: 39              RTS                         
A9C8: 81 0D           CMPA    #$0D                  
A9CA: 26 01           BNE     $A9CD                   
A9CC: 39              RTS                         
A9CD: 81 10           CMPA    #$10                  
A9CF: 26 01           BNE     $A9D2                   
A9D1: 39              RTS                         
A9D2: CE 24 B0        LDU     #$24B0                  
A9D5: E6 50           LDB     -16,U               
A9D7: 27 13           BEQ     $A9EC                   
A9D9: 33 C8 E0        LEAU    $E0,U                 
A9DC: 11 83 1F F0     CMPU    #$1FF0                  
A9E0: 26 F3           BNE     $A9D5                   
A9E2: 86 42           LDA     #$42                  
A9E4: B7 07 AF        STA     $07AF                   
A9E7: B6 80 00        LDA     $8000                   
A9EA: 20 FB           BRA     $A9E7                   
A9EC: BF 10 36        STX     $1036                   
A9EF: 8E AA 45        LDX     #$AA45                  
A9F2: C6 04           LDB     #$04                  
A9F4: E7 4B           STB     11,U                
A9F6: 58 ; ????
A9F7: 81 0B           CMPA    #$0B                  
A9F9: 24 ; ????
A9FA: 01 ; ????
A9FB: 58 ; ????
A9FC: F7 10 CF        STB     $10CF                   
A9FF: 48 ; ????
AA00: 30 86           LEAX    A,X                 
AA02: EC 84           LDD     ,X                  
AA04: A7 4A           STA     10,U                
AA06: E7 48           STB     8,U                 
AA08: 6C 50           INC     -16,U               
AA0A: F6 10 35        LDB     $1035                   
AA0D: C4 07           ANDB    #$07                  
AA0F: 86 20           LDA     #$20                  
AA11: 3D              MUL                         
AA12: FB 10 CF        ADDB    $10CF                   
AA15: E7 4F           STB     15,U                
AA17: F6 10 35        LDB     $1035                   
AA1A: C4 78           ANDB    #$78                  
AA1C: 86 04           LDA     #$04                  
AA1E: 3D              MUL                         
AA1F: C3 00 20        ADDD    #$0020                  
AA22: ED 5E           STD     -2,U                
AA24: 7C 10 D9        INC     $10D9                   
AA27: CC 03 10        LDD     #$0310                  
AA2A: F4 10 CF        ANDB    $10CF                   
AA2D: 26 01           BNE     $AA30                   
AA2F: 4A              DECA                        
AA30: A7 5B           STA     -5,U                
AA32: CC 08 01        LDD     #$0801                  
AA35: A7 44           STA     4,U                 
AA37: F7 40 43        STB     $4043                   
AA3A: 1E 31           EXG     U,X                   
AA3C: BD C0 BB        JSR     $C0BB                   
AA3F: 6F 0C           CLR     12,X                
AA41: BE 10 36        LDX     $1036                   
AA44: 39              RTS                         
AA45: 8C 0E 8C        CMPX    #$0E8C                  
AA48: 0C A4           INC     $A4                   
AA4A: 0E 98           JMP     $98                   
AA4C: 0E 98           JMP     $98                   
AA4E: 0C A4           INC     $A4                   
AA50: 0C B0           INC     $B0                   
AA52: 0E B0           JMP     $B0                   
AA54: 0C 80           INC     $80                   
AA56: 0E 80           JMP     $80                   
AA58: 0C 01           INC     $01                   
AA5A: 01 ; ????
AA5B: C0 0A           SUBB    #$0A                  
AA5D: C0 08           SUBB    #$08                  
AA5F: 01 ; ????
AA60: 01 ; ????
AA61: C4 0A           ANDB    #$0A                  
AA63: C4 08           ANDB    #$08                  
AA65: 01 ; ????
AA66: 01 ; ????
AA67: BC 0A BC        CMPX    $0ABC                   
AA6A: 08 ; ????
AA6B: BC 0A BC        CMPX    $0ABC                   
AA6E: 08 ; ????
AA6F: BD 81 50        JSR     $8150                   
AA72: B6 10 D9        LDA     $10D9                   
AA75: 27 F8           BEQ     $AA6F                   
AA77: 8E 20 10        LDX     #$2010                  
AA7A: 7F 10 09        CLR     $1009                   
AA7D: A6 10           LDA     -16,X               
AA7F: 27 2C           BEQ     $AAAD                   
AA81: 6A 04           DEC     4,X                 
AA83: 26 15           BNE     $AA9A                   
AA85: 6A 1B           DEC     -5,X                
AA87: 27 21           BEQ     $AAAA                   
AA89: CC 04 08        LDD     #$0408                  
AA8C: E7 04           STB     4,X                 
AA8E: E6 0A           LDB     10,X                
AA90: C1 BE           CMPB    #$BE                  
AA92: 25 ; ????
AA93: 02 ; ????
AA94: 44              LSRA                        
AA95: 44              LSRA                        
AA96: AB 0A           ADDA    10,X                
AA98: A7 0A           STA     10,X                
AA9A: BD C0 BB        JSR     $C0BB                   
AA9D: CC 00 01        LDD     #$0001                  
AAA0: A7 0C           STA     12,X                
AAA2: F7 40 43        STB     $4043                   
AAA5: 7C 10 09        INC     $1009                   
AAA8: 20 03           BRA     $AAAD                   
AAAA: BD 87 32        JSR     $8732                   
AAAD: 30 88 20        LEAX    $20,X                 
AAB0: 8C 24 D0        CMPX    #$24D0                  
AAB3: 26 C8           BNE     $AA7D                   
AAB5: B6 10 09        LDA     $1009                   
AAB8: B7 10 D9        STA     $10D9                   
AABB: 20 B2           BRA     $AA6F                   
AABD: BD 81 50        JSR     $8150                   
AAC0: B6 10 D2        LDA     $10D2                   
AAC3: 27 F8           BEQ     $AABD                   
AAC5: BD 81 50        JSR     $8150                   
AAC8: B6 10 D2        LDA     $10D2                   
AACB: 27 F0           BEQ     $AABD                   
AACD: FC 10 D0        LDD     $10D0                   
AAD0: 10 26 00 A6     LBNE    $AB7A                   
AAD4: B6 10 50        LDA     $1050                   
AAD7: 26 EC           BNE     $AAC5                   
AAD9: 7A 10 4A        DEC     $104A                   
AADC: 26 E7           BNE     $AAC5                   
AADE: 7C 10 DB        INC     $10DB                   
AAE1: 8E 15 80        LDX     #$1580                  
AAE4: B6 10 11        LDA     $1011                   
AAE7: 48 ; ????
AAE8: 48 ; ????
AAE9: 48 ; ????
AAEA: B8 10 11        EORA    $1011                   
AAED: 43              COMA                        
AAEE: 48 ; ????
AAEF: 79 10 11        ROL     $1011                   
AAF2: B6 10 11        LDA     $1011                   
AAF5: 84 7F           ANDA    #$7F                  
AAF7: 81 78           CMPA    #$78                  
AAF9: 24 ; ????
AAFA: E9 E6           ADCB    A,S                 
AAFC: 86 C1           LDA     #$C1                  
AAFE: 0A 24           DEC     $24                   
AB00: E3 1F           ADDD    -1,X                
AB02: 89 84           ADCA    #$84                  
AB04: 07 48           ASR     $48                   
AB06: 48 ; ????
AB07: 48 ; ????
AB08: 48 ; ????
AB09: 48 ; ????
AB0A: 8B 10           ADDA    #$10                  
AB0C: B7 10 4C        STA     $104C                   
AB0F: C4 78           ANDB    #$78                  
AB11: 86 04           LDA     #$04                  
AB13: 3D              MUL                         
AB14: C3 00 20        ADDD    #$0020                  
AB17: FD 10 4D        STD     $104D                   
AB1A: 20 12           BRA     $AB2E                   
AB1C: BD 81 50        JSR     $8150                   
AB1F: B6 10 D2        LDA     $10D2                   
AB22: 27 99           BEQ     $AABD                   
AB24: FC 10 D0        LDD     $10D0                   
AB27: 26 51           BNE     $AB7A                   
AB29: B6 10 DB        LDA     $10DB                   
AB2C: 27 2C           BEQ     $AB5A                   
AB2E: 8E 25 30        LDX     #$2530                  
AB31: C6 0B           LDB     #$0B                  
AB33: A6 10           LDA     -16,X               
AB35: 27 08           BEQ     $AB3F                   
AB37: A6 1A           LDA     -6,X                
AB39: 81 01           CMPA    #$01                  
AB3B: 26 02           BNE     $AB3F                   
AB3D: E7 1A           STB     -6,X                
AB3F: 30 88 20        LEAX    $20,X                 
AB42: 8C 26 70        CMPX    #$2670                  
AB45: 26 EC           BNE     $AB33                   
AB47: B6 10 50        LDA     $1050                   
AB4A: 26 D0           BNE     $AB1C                   
AB4C: 7A 10 4B        DEC     $104B                   
AB4F: 26 CB           BNE     $AB1C                   
AB51: 7F 10 DB        CLR     $10DB                   
AB54: FC 17 18        LDD     $1718                   
AB57: FD 10 4A        STD     $104A                   
AB5A: 8E 25 30        LDX     #$2530                  
AB5D: C6 01           LDB     #$01                  
AB5F: A6 10           LDA     -16,X               
AB61: 27 08           BEQ     $AB6B                   
AB63: A6 1A           LDA     -6,X                
AB65: 81 0B           CMPA    #$0B                  
AB67: 26 02           BNE     $AB6B                   
AB69: E7 1A           STB     -6,X                
AB6B: 30 88 20        LEAX    $20,X                 
AB6E: 8C 26 70        CMPX    #$2670                  
AB71: 26 EC           BNE     $AB5F                   
AB73: B6 10 49        LDA     $1049                   
AB76: 10 26 FF 4B     LBNE    $AAC5                   
AB7A: BD 81 50        JSR     $8150                   
AB7D: B6 10 D2        LDA     $10D2                   
AB80: 26 F8           BNE     $AB7A                   
AB82: 7E AA BD        JMP     $AABD                   
AB85: BD 81 50        JSR     $8150                   
AB88: B6 10 D2        LDA     $10D2                   
AB8B: 27 F8           BEQ     $AB85                   
AB8D: BD AC 90        JSR     $AC90                   
AB90: BD 81 50        JSR     $8150                   
AB93: B6 40 40        LDA     $4040                   
AB96: 26 F8           BNE     $AB90                   
AB98: BD 81 50        JSR     $8150                   
AB9B: B6 10 D2        LDA     $10D2                   
AB9E: 10 27 00 AD     LBEQ    $AC4F                   
ABA2: B6 10 D0        LDA     $10D0                   
ABA5: 26 09           BNE     $ABB0                   
ABA7: B6 10 D1        LDA     $10D1                   
ABAA: 10 26 00 96     LBNE    $AC44                   
ABAE: 20 23           BRA     $ABD3                   
ABB0: 7F 10 DF        CLR     $10DF                   
ABB3: C6 05           LDB     #$05                  
ABB5: 8E 25 30        LDX     #$2530                  
ABB8: A6 10           LDA     -16,X               
ABBA: 27 0F           BEQ     $ABCB                   
ABBC: A6 1A           LDA     -6,X                
ABBE: 27 0B           BEQ     $ABCB                   
ABC0: 81 0C           CMPA    #$0C                  
ABC2: 24 ; ????
ABC3: 04 E7           LSR     $E7                   
ABC5: 1A 20           ORCC    #$20                  
ABC7: 03 7C           COM     $7C                   
ABC9: 10 DF 30        STS     $30                   
ABCC: 88 20           EORA    #$20                  
ABCE: 8C 26 70        CMPX    #$2670                  
ABD1: 26 E5           BNE     $ABB8                   
ABD3: 8E 25 30        LDX     #$2530                  
ABD6: CE AC 66        LDU     #$AC66                  
ABD9: A6 10           LDA     -16,X               
ABDB: 27 5C           BEQ     $AC39                   
ABDD: A6 1A           LDA     -6,X                
ABDF: 27 58           BEQ     $AC39                   
ABE1: 48 ; ????
ABE2: AD D6           JSR     [A,U]               
ABE4: B6 10 D0        LDA     $10D0                   
ABE7: 26 50           BNE     $AC39                   
ABE9: A6 1A           LDA     -6,X                
ABEB: 81 14           CMPA    #$14                  
ABED: 27 04           BEQ     $ABF3                   
ABEF: 81 0C           CMPA    #$0C                  
ABF1: 24 ; ????
ABF2: 46              RORA                        
ABF3: A6 0D           LDA     13,X                
ABF5: 27 42           BEQ     $AC39                   
ABF7: CE 25 10        LDU     #$2510                  
ABFA: BD C4 F4        JSR     $C4F4                   
ABFD: B6 10 D3        LDA     $10D3                   
AC00: 27 37           BEQ     $AC39                   
AC02: CC 01 06        LDD     #$0106                  
AC05: B7 10 D0        STA     $10D0                   
AC08: 6C 4F           INC     15,U                
AC0A: E7 5A           STB     -6,U                
AC0C: CC 3C 57        LDD     #$3C57                  
AC0F: A7 44           STA     4,U                 
AC11: E7 4A           STB     10,U                
AC13: 6F 48           CLR     8,U                 
AC15: B6 10 10        LDA     $1010                   
AC18: 26 08           BNE     $AC22                   
AC1A: 86 3C           LDA     #$3C                  
AC1C: B7 10 4F        STA     $104F                   
AC1F: 7C 40 4D        INC     $404D                   
AC22: B6 25 02        LDA     $2502                   
AC25: 27 0C           BEQ     $AC33                   
AC27: 7F 25 02        CLR     $2502                   
AC2A: BF 10 36        STX     $1036                   
AC2D: BD A5 4F        JSR     $A54F                   
AC30: BE 10 36        LDX     $1036                   
AC33: 7F 25 01        CLR     $2501                   
AC36: 7F 10 DA        CLR     $10DA                   
AC39: 30 88 20        LEAX    $20,X                 
AC3C: 8C 26 70        CMPX    #$2670                  
AC3F: 26 95           BNE     $ABD6                   
AC41: 7E AB 98        JMP     $AB98                   
AC44: 7F 10 DF        CLR     $10DF                   
AC47: BD 81 50        JSR     $8150                   
AC4A: B6 10 D2        LDA     $10D2                   
AC4D: 26 F8           BNE     $AC47                   
AC4F: 8E 25 30        LDX     #$2530                  
AC52: A6 10           LDA     -16,X               
AC54: 26 04           BNE     $AC5A                   
AC56: A6 16           LDA     -10,X               
AC58: 27 03           BEQ     $AC5D                   
AC5A: BD 87 32        JSR     $8732                   
AC5D: 30 88 20        LEAX    $20,X                 
AC60: 8C 27 90        CMPX    #$2790                  
AC63: 26 ED           BNE     $AC52                   
AC65: 7E AB 85        JMP     $AB85                   
AC68: AD 49           JSR     9,U                 
AC6A: B5 ED AD        BITA    $EDAD                   
AC6D: EC ; ????
AC6E: AE D3           LDX     [,--U]              
AC70: C0 BB           SUBB    #$BB                  
AC72: B2 3F B2        SBCA    $3FB2                   
AC75: 7A B3 33        DEC     $B333                   
AC78: B3 58 B3        SUBD    $58B3                   
AC7B: 81 B0           CMPA    #$B0                  
AC7D: AC ; ????
AC7E: AF 45           STX     5,U                 
AC80: AF 9B           STX     [D,X]               
AC82: C0 BB           SUBB    #$BB                  
AC84: AF A4           STX     ,Y                  
AC86: B0 15 B0        SUBA    $15B0                   
AC89: 69 AD 3C B0     ROL     $E93D,PC                
AC8D: 62 ; ????
AC8E: AF 0B           STX     11,X                
AC90: 8E 15 88        LDX     #$1588                  
AC93: CC 00 0A        LDD     #$000A                  
AC96: B7 10 69        STA     $1069                   
AC99: E1 80           CMPB    ,X+                 
AC9B: 23 01           BLS     $AC9E                   
AC9D: 4C              INCA                        
AC9E: 8C 15 F0        CMPX    #$15F0                  
ACA1: 26 F6           BNE     $AC99                   
ACA3: 81 01           CMPA    #$01                  
ACA5: 22 05           BHI     $ACAC                   
ACA7: 86 10           LDA     #$10                  
ACA9: B7 10 69        STA     $1069                   
ACAC: 8E 25 30        LDX     #$2530                  
ACAF: 7F 10 3C        CLR     $103C                   
ACB2: CE 17 0D        LDU     #$170D                  
ACB5: A6 4A           LDA     10,U                
ACB7: B7 10 09        STA     $1009                   
ACBA: 7C 10 3C        INC     $103C                   
ACBD: A6 C0           LDA     ,U+                 
ACBF: 27 F9           BEQ     $ACBA                   
ACC1: 2B 0A           BMI     $ACCD                   
ACC3: B6 17 09        LDA     $1709                   
ACC6: A7 03           STA     3,X                 
ACC8: CC 14 01        LDD     #$1401                  
ACCB: 20 0F           BRA     $ACDC                   
ACCD: B6 17 08        LDA     $1708                   
ACD0: A7 03           STA     3,X                 
ACD2: CC 80 05        LDD     #$8005                  
ACD5: A7 19           STA     -7,X                
ACD7: E7 11           STB     -15,X               
ACD9: CC 1C 01        LDD     #$1C01                  
ACDC: ED 0A           STD     10,X                
ACDE: E7 10           STB     -16,X               
ACE0: CC 04 12        LDD     #$0412                  
ACE3: A7 05           STA     5,X                 
ACE5: E7 1A           STB     -6,X                
ACE7: BD 8A A0        JSR     $8AA0                   
ACEA: 84 0F           ANDA    #$0F                  
ACEC: 4C              INCA                        
ACED: A7 04           STA     4,X                 
ACEF: A6 19           LDA     -7,X                
ACF1: BA 10 3C        ORA     $103C                   
ACF4: A7 19           STA     -7,X                
ACF6: FF 10 38        STU     $1038                   
ACF9: BD C8 EF        JSR     $C8EF                   
ACFC: BD C0 BB        JSR     $C0BB                   
ACFF: FE 10 38        LDU     $1038                   
AD02: 30 88 20        LEAX    $20,X                 
AD05: 7A 10 09        DEC     $1009                   
AD08: 26 B0           BNE     $ACBA                   
AD0A: CE 94 D9        LDU     #$94D9                  
AD0D: B6 17 17        LDA     $1717                   
AD10: E6 C6           LDB     A,U                 
AD12: F7 10 6C        STB     $106C                   
AD15: 81 01           CMPA    #$01                  
AD17: 26 04           BNE     $AD1D                   
AD19: 86 05           LDA     #$05                  
AD1B: 20 03           BRA     $AD20                   
AD1D: B6 17 1F        LDA     $171F                   
AD20: B7 10 5C        STA     $105C                   
AD23: B6 17 1B        LDA     $171B                   
AD26: B7 10 49        STA     $1049                   
AD29: FC 17 18        LDD     $1718                   
AD2C: FD 10 4A        STD     $104A                   
AD2F: CC 00 01        LDD     #$0001                  
AD32: B7 10 69        STA     $1069                   
AD35: F7 10 E4        STB     $10E4                   
AD38: B7 10 6D        STA     $106D                   
AD3B: 39              RTS                         
AD3C: 6A 04           DEC     4,X                 
AD3E: 10 26 13 79     LBNE    $C0BB                   
AD42: 86 01           LDA     #$01                  
AD44: A7 1A           STA     -6,X                
AD46: 7E C0 BB        JMP     $C0BB                   
AD49: A6 1B           LDA     -5,X                
AD4B: 27 09           BEQ     $AD56                   
AD4D: BD C0 00        JSR     $C000                   
AD50: BD C0 9A        JSR     $C09A                   
AD53: 7E C0 BB        JMP     $C0BB                   
AD56: A6 19           LDA     -7,X                
AD58: 2A 67           BPL     $ADC1                   
AD5A: A6 0D           LDA     13,X                
AD5C: 27 63           BEQ     $ADC1                   
AD5E: E6 05           LDB     5,X                 
AD60: C5 02           BITB    #$02                  
AD62: 27 5D           BEQ     $ADC1                   
AD64: C5 04           BITB    #$04                  
AD66: 26 06           BNE     $AD6E                   
AD68: 81 18           CMPA    #$18                  
AD6A: 23 55           BLS     $ADC1                   
AD6C: 20 04           BRA     $AD72                   
AD6E: 81 E8           CMPA    #$E8                  
AD70: 24 ; ????
AD71: 4F              CLRA                        
AD72: BD 8A A0        JSR     $8AA0                   
AD75: B1 17 1A        CMPA    $171A                   
AD78: 23 1A           BLS     $AD94                   
AD7A: A6 11           LDA     -15,X               
AD7C: 26 43           BNE     $ADC1                   
AD7E: C5 04           BITB    #$04                  
AD80: 26 07           BNE     $AD89                   
AD82: EC 1E           LDD     -2,X                
AD84: B3 25 0E        SUBD    $250E                   
AD87: 20 05           BRA     $AD8E                   
AD89: FC 25 0E        LDD     $250E                   
AD8C: A3 1E           SUBD    -2,X                
AD8E: 10 83 00 40     CMPD    #$0040                  
AD92: 22 2D           BHI     $ADC1                   
AD94: CE 25 30        LDU     #$2530                  
AD97: A6 50           LDA     -16,U               
AD99: 26 1D           BNE     $ADB8                   
AD9B: A6 56           LDA     -10,U               
AD9D: 26 19           BNE     $ADB8                   
AD9F: 6C 56           INC     -10,U               
ADA1: EF 15           STU     -11,X               
ADA3: CC 06 3F        LDD     #$063F                  
ADA6: A7 1A           STA     -6,X                
ADA8: E7 1B           STB     -5,X                
ADAA: 86 6C           LDA     #$6C                  
ADAC: A7 0A           STA     10,X                
ADAE: A6 05           LDA     5,X                 
ADB0: 84 04           ANDA    #$04                  
ADB2: 44              LSRA                        
ADB3: A7 08           STA     8,X                 
ADB5: 7E C0 BB        JMP     $C0BB                   
ADB8: 33 C8 20        LEAU    $20,U                 
ADBB: 11 83 27 70     CMPU    #$2770                  
ADBF: 26 D6           BNE     $AD97                   
ADC1: BD B3 BD        JSR     $B3BD                   
ADC4: A6 1A           LDA     -6,X                
ADC6: 81 01           CMPA    #$01                  
ADC8: 27 03           BEQ     $ADCD                   
ADCA: 7E C0 BB        JMP     $C0BB                   
ADCD: B6 10 34        LDA     $1034                   
ADD0: A1 05           CMPA    5,X                 
ADD2: 27 0B           BEQ     $ADDF                   
ADD4: E6 0A           LDB     10,X                
ADD6: C4 18           ANDB    #$18                  
ADD8: FB 10 34        ADDB    $1034                   
ADDB: E7 0A           STB     10,X                
ADDD: A7 05           STA     5,X                 
ADDF: 86 10           LDA     #$10                  
ADE1: A7 1B           STA     -5,X                
ADE3: BD C0 00        JSR     $C000                   
ADE6: BD C0 9A        JSR     $C09A                   
ADE9: 7E C0 BB        JMP     $C0BB                   
ADEC: A6 1B           LDA     -5,X                
ADEE: 27 09           BEQ     $ADF9                   
ADF0: BD C0 00        JSR     $C000                   
ADF3: BD C0 9A        JSR     $C09A                   
ADF6: 7E C0 BB        JMP     $C0BB                   
ADF9: A6 1F           LDA     -1,X                
ADFB: 84 10           ANDA    #$10                  
ADFD: 27 0A           BEQ     $AE09                   
ADFF: 86 01           LDA     #$01                  
AE01: A7 1A           STA     -6,X                
AE03: B7 10 E4        STA     $10E4                   
AE06: 7E AD 56        JMP     $AD56                   
AE09: BD CD 83        JSR     $CD83                   
AE0C: A6 0F           LDA     15,X                
AE0E: 85 10           BITA    #$10                  
AE10: 26 01           BNE     $AE13                   
AE12: 5A              DECB                        
AE13: CE 15 80        LDU     #$1580                  
AE16: 33 C5           LEAU    B,U                 
AE18: 86 50           LDA     #$50                  
AE1A: E6 58           LDB     -8,U                
AE1C: C1 09           CMPB    #$09                  
AE1E: 23 02           BLS     $AE22                   
AE20: 8A 20           ORA     #$20                  
AE22: E6 48           LDB     8,U                 
AE24: C1 09           CMPB    #$09                  
AE26: 23 02           BLS     $AE2A                   
AE28: 8A 80           ORA     #$80                  
AE2A: B7 10 6A        STA     $106A                   
AE2D: BD B3 BD        JSR     $B3BD                   
AE30: A6 17           LDA     -9,X                
AE32: 84 F0           ANDA    #$F0                  
AE34: B4 10 6A        ANDA    $106A                   
AE37: 26 09           BNE     $AE42                   
AE39: A6 1A           LDA     -6,X                
AE3B: 81 02           CMPA    #$02                  
AE3D: 26 C0           BNE     $ADFF                   
AE3F: 7E C0 BB        JMP     $C0BB                   
AE42: C6 04           LDB     #$04                  
AE44: 49              ROLA                        
AE45: 25 ; ????
AE46: 03 5A           COM     $5A                   
AE48: 20 FA           BRA     $AE44                   
AE4A: CE AE 81        LDU     #$AE81                  
AE4D: 58 ; ????
AE4E: A6 0F           LDA     15,X                
AE50: 84 10           ANDA    #$10                  
AE52: 44              LSRA                        
AE53: 33 C6           LEAU    A,U                 
AE55: 10 AE C5        LDY     B,U                 
AE58: CE 11 8A        LDU     #$118A                  
AE5B: A6 19           LDA     -7,X                
AE5D: 84 0F           ANDA    #$0F                  
AE5F: 48 ; ????
AE60: 10 AF C6        STY     A,U                 
AE63: CB 0E           ADDB    #$0E                  
AE65: A6 19           LDA     -7,X                
AE67: 2A 02           BPL     $AE6B                   
AE69: CB 08           ADDB    #$08                  
AE6B: E7 0A           STB     10,X                
AE6D: A6 1A           LDA     -6,X                
AE6F: 81 02           CMPA    #$02                  
AE71: 26 06           BNE     $AE79                   
AE73: 6F 1B           CLR     -5,X                
AE75: 68 ; ????
AE76: 03 68           COM     $68                   
AE78: 03 CC           COM     $CC                   
AE7A: 04 3F           LSR     $3F                   
AE7C: A7 1A           STA     -6,X                
AE7E: E7 04           STB     4,X                 
AE80: 7E C0 BB        JMP     $C0BB                   
AE83: AE 93           LDX     [,--X]              
AE85: AE 99 AE A3     LDX     [$AEA3,X]               
AE89: AE A9 AE B3     LDX     $AEB3,Y                 
AE8D: AE B9 AE C3     LDX     [$AEC3,Y]               
AE91: AE C9 00 28     LDX     $0028,U                 
AE95: 04 08           LSR     $08                   
AE97: FF FF 01        STU     $FF01                   
AE9A: 08 ; ????
AE9B: 02 ; ????
AE9C: 08 ; ????
AE9D: 03 08           COM     $08                   
AE9F: 04 08           LSR     $08                   
AEA1: FF FF 00        STU     $FF00                   
AEA4: 08 ; ????
AEA5: 04 28           LSR     $28                   
AEA7: FF FF 07        STU     $FF07                   
AEAA: 08 ; ????
AEAB: 06 08           ROR     $08                   
AEAD: 05 ; ????
AEAE: 08 ; ????
AEAF: 04 08           LSR     $08                   
AEB1: FF FF 00        STU     $FF00                   
AEB4: 18 ; ????
AEB5: 04 08           LSR     $08                   
AEB7: FF FF 01        STU     $FF01                   
AEBA: 08 ; ????
AEBB: 02 ; ????
AEBC: 08 ; ????
AEBD: 03 08           COM     $08                   
AEBF: 04 18           LSR     $18                   
AEC1: FF FF 00        STU     $FF00                   
AEC4: 08 ; ????
AEC5: 04 38           LSR     $38                   
AEC7: FF FF 07        STU     $FF07                   
AECA: 08 ; ????
AECB: 06 08           ROR     $08                   
AECD: 05 ; ????
AECE: 08 ; ????
AECF: 04 18           LSR     $18                   
AED1: FF FF 6A        STU     $FF6A                   
AED4: 04 27           LSR     $27                   
AED6: 15 ; ????
AED7: A6 04           LDA     4,X                 
AED9: 84 04           ANDA    #$04                  
AEDB: 44              LSRA                        
AEDC: 44              LSRA                        
AEDD: B7 10 34        STA     $1034                   
AEE0: A6 0A           LDA     10,X                
AEE2: 84 1E           ANDA    #$1E                  
AEE4: BB 10 34        ADDA    $1034                   
AEE7: A7 0A           STA     10,X                
AEE9: 7E C0 BB        JMP     $C0BB                   
AEEC: 10 8E 11 8A     LDY     #$118A                  
AEF0: A6 19           LDA     -7,X                
AEF2: 84 0F           ANDA    #$0F                  
AEF4: 48 ; ????
AEF5: 31 A6           LEAY    A,Y                 
AEF7: EE A4           LDU     ,Y                  
AEF9: EC C1           LDD     ,U++                
AEFB: EF A4           STU     ,Y                  
AEFD: A7 05           STA     5,X                 
AEFF: E7 1B           STB     -5,X                
AF01: CC 14 C0        LDD     #$14C0                  
AF04: A7 1A           STA     -6,X                
AF06: E7 03           STB     3,X                 
AF08: 7E C0 BB        JMP     $C0BB                   
AF0B: A6 1B           LDA     -5,X                
AF0D: 27 06           BEQ     $AF15                   
AF0F: BD C0 00        JSR     $C000                   
AF12: 7E C0 BB        JMP     $C0BB                   
AF15: 10 8E 11 8A     LDY     #$118A                  
AF19: A6 19           LDA     -7,X                
AF1B: 84 0F           ANDA    #$0F                  
AF1D: 48 ; ????
AF1E: 31 A6           LEAY    A,Y                 
AF20: EE A4           LDU     ,Y                  
AF22: EC C1           LDD     ,U++                
AF24: 2B 09           BMI     $AF2F                   
AF26: EF A4           STU     ,Y                  
AF28: A7 05           STA     5,X                 
AF2A: E7 1B           STB     -5,X                
AF2C: 7E C0 BB        JMP     $C0BB                   
AF2F: CC 10 3F        LDD     #$103F                  
AF32: A7 1A           STA     -6,X                
AF34: E7 04           STB     4,X                 
AF36: A6 0F           LDA     15,X                
AF38: 81 F0           CMPA    #$F0                  
AF3A: 10 ; ????
AF3B: 25 ; ????
AF3C: 11 ; ????
AF3D: 7D 86 06        TST     $8606                   
AF40: A7 0F           STA     15,X                
AF42: 7E C0 BB        JMP     $C0BB                   
AF45: A6 12           LDA     -14,X               
AF47: 81 01           CMPA    #$01                  
AF49: 26 0B           BNE     $AF56                   
AF4B: 6F 08           CLR     8,X                 
AF4D: 86 6A           LDA     #$6A                  
AF4F: E6 19           LDB     -7,X                
AF51: 2A 11           BPL     $AF64                   
AF53: 4C              INCA                        
AF54: 20 0E           BRA     $AF64                   
AF56: C6 0C           LDB     #$0C                  
AF58: E7 08           STB     8,X                 
AF5A: 48 ; ????
AF5B: 48 ; ????
AF5C: 8B C0           ADDA    #$C0                  
AF5E: E6 19           LDB     -7,X                
AF60: 2A 02           BPL     $AF64                   
AF62: 8B 0C           ADDA    #$0C                  
AF64: A7 0A           STA     10,X                
AF66: 6A 04           DEC     4,X                 
AF68: 26 08           BNE     $AF72                   
AF6A: 6A 12           DEC     -14,X               
AF6C: 27 07           BEQ     $AF75                   
AF6E: 86 5A           LDA     #$5A                  
AF70: A7 04           STA     4,X                 
AF72: 7E C0 BB        JMP     $C0BB                   
AF75: CC 00 01        LDD     #$0001                  
AF78: A7 08           STA     8,X                 
AF7A: E7 1A           STB     -6,X                
AF7C: F1 17 17        CMPB    $1717                   
AF7F: 26 09           BNE     $AF8A                   
AF81: CC 01 02        LDD     #$0102                  
AF84: F7 10 5C        STB     $105C                   
AF87: B7 10 E4        STA     $10E4                   
AF8A: A6 05           LDA     5,X                 
AF8C: 84 06           ANDA    #$06                  
AF8E: E6 19           LDB     -7,X                
AF90: 2A 02           BPL     $AF94                   
AF92: 8B 08           ADDA    #$08                  
AF94: 8A 10           ORA     #$10                  
AF96: A7 0A           STA     10,X                
AF98: 7E C0 BB        JMP     $C0BB                   
AF9B: 6A 04           DEC     4,X                 
AF9D: 10 27 00 8F     LBEQ    $B030                   
AFA1: 7E C0 BB        JMP     $C0BB                   
AFA4: A6 04           LDA     4,X                 
AFA6: 4A              DECA                        
AFA7: 27 14           BEQ     $AFBD                   
AFA9: A7 04           STA     4,X                 
AFAB: 84 02           ANDA    #$02                  
AFAD: 44              LSRA                        
AFAE: B7 10 34        STA     $1034                   
AFB1: A6 0A           LDA     10,X                
AFB3: 84 1E           ANDA    #$1E                  
AFB5: BB 10 34        ADDA    $1034                   
AFB8: A7 0A           STA     10,X                
AFBA: 7E C0 BB        JMP     $C0BB                   
AFBD: CE 15 80        LDU     #$1580                  
AFC0: BD CD 83        JSR     $CD83                   
AFC3: A6 C5           LDA     B,U                 
AFC5: 81 0A           CMPA    #$0A                  
AFC7: 25 ; ????
AFC8: 0E A6           JMP     $A6                   
AFCA: 0F 84           CLR     $84                   
AFCC: F0 8A 1E        SUBB    $8A1E                   
AFCF: 81 F0           CMPA    #$F0                  
AFD1: 25 ; ????
AFD2: 02 ; ????
AFD3: 86 06           LDA     #$06                  
AFD5: A7 0F           STA     15,X                
AFD7: CC 01 3F        LDD     #$013F                  
AFDA: B7 40 4F        STA     $404F                   
AFDD: E7 04           STB     4,X                 
AFDF: CC 10 89        LDD     #$1089                  
AFE2: A7 1A           STA     -6,X                
AFE4: E7 0A           STB     10,X                
AFE6: 86 06           LDA     #$06                  
AFE8: B7 10 C0        STA     $10C0                   
AFEB: BD C5 34        JSR     $C534                   
AFEE: 5F              CLRB                        
AFEF: 81 FC           CMPA    #$FC                  
AFF1: 25 ; ????
AFF2: 02 ; ????
AFF3: CA 01           ORB     #$01                  
AFF5: A6 C8 A0        LDA     $A0,U                 
AFF8: 81 FC           CMPA    #$FC                  
AFFA: 25 ; ????
AFFB: 02 ; ????
AFFC: CA 02           ORB     #$02                  
AFFE: C1 03           CMPB    #$03                  
B000: 10 27 10 B7     LBEQ    $C0BB                   
B004: 86 04           LDA     #$04                  
B006: C5 02           BITB    #$02                  
B008: 27 02           BEQ     $B00C                   
B00A: 86 FC           LDA     #$FC                  
B00C: EE 1E           LDU     -2,X                
B00E: 33 C6           LEAU    A,U                 
B010: EF 1E           STU     -2,X                
B012: 7E C0 BB        JMP     $C0BB                   
B015: 6A 04           DEC     4,X                 
B017: 27 12           BEQ     $B02B                   
B019: A6 04           LDA     4,X                 
B01B: 84 30           ANDA    #$30                  
B01D: 44              LSRA                        
B01E: 44              LSRA                        
B01F: 44              LSRA                        
B020: 44              LSRA                        
B021: 43              COMA                        
B022: 84 03           ANDA    #$03                  
B024: 8B 38           ADDA    #$38                  
B026: A7 0A           STA     10,X                
B028: 7E C0 BB        JMP     $C0BB                   
B02B: 6C 1A           INC     -6,X                
B02D: 7E C0 BB        JMP     $C0BB                   
B030: CC F5 20        LDD     #$F520                  
B033: B7 10 34        STA     $1034                   
B036: A6 19           LDA     -7,X                
B038: 2A 08           BPL     $B042                   
B03A: A6 14           LDA     -12,X               
B03C: 27 04           BEQ     $B042                   
B03E: 7C 10 34        INC     $1034                   
B041: 58 ; ????
B042: 4F              CLRA                        
B043: BF 10 36        STX     $1036                   
B046: BD 8A DB        JSR     $8ADB                   
B049: BE 10 36        LDX     $1036                   
B04C: CC 13 1F        LDD     #$131F                  
B04F: A7 1A           STA     -6,X                
B051: E7 04           STB     4,X                 
B053: CC 00 0C        LDD     #$000C                  
B056: A7 08           STA     8,X                 
B058: E7 0B           STB     11,X                
B05A: B6 10 34        LDA     $1034                   
B05D: A7 0A           STA     10,X                
B05F: 7E C0 BB        JMP     $C0BB                   
B062: 6A 04           DEC     4,X                 
B064: 27 03           BEQ     $B069                   
B066: 7E C0 BB        JMP     $C0BB                   
B069: CE 17 0C        LDU     #$170C                  
B06C: A6 19           LDA     -7,X                
B06E: 84 0F           ANDA    #$0F                  
B070: 6F C6           CLR     A,U                 
B072: 6A 4B           DEC     11,U                
B074: 27 30           BEQ     $B0A6                   
B076: A6 4B           LDA     11,U                
B078: 81 01           CMPA    #$01                  
B07A: 27 13           BEQ     $B08F                   
B07C: B6 10 E4        LDA     $10E4                   
B07F: 10 26 D6 AF     LBNE    $8732                   
B083: CC 01 02        LDD     #$0102                  
B086: B7 10 E4        STA     $10E4                   
B089: F7 10 5C        STB     $105C                   
B08C: 7E 87 32        JMP     $8732                   
B08F: F6 10 E4        LDB     $10E4                   
B092: 26 03           BNE     $B097                   
B094: B7 10 E4        STA     $10E4                   
B097: 86 05           LDA     #$05                  
B099: B1 10 5C        CMPA    $105C                   
B09C: 10 22 D6 92     LBHI    $8732                   
B0A0: B7 10 5C        STA     $105C                   
B0A3: 7E 87 32        JMP     $8732                   
B0A6: 7C 10 D1        INC     $10D1                   
B0A9: 7E 87 32        JMP     $8732                   
B0AC: A6 1B           LDA     -5,X                
B0AE: 27 09           BEQ     $B0B9                   
B0B0: BD C0 00        JSR     $C000                   
B0B3: BD C0 9A        JSR     $C09A                   
B0B6: 7E C0 BB        JMP     $C0BB                   
B0B9: 86 05           LDA     #$05                  
B0BB: B7 10 C0        STA     $10C0                   
B0BE: BD C5 34        JSR     $C534                   
B0C1: BF 10 36        STX     $1036                   
B0C4: 8E B1 5E        LDX     #$B15E                  
B0C7: 4F              CLRA                        
B0C8: E6 81           LDB     ,X++                
B0CA: 27 24           BEQ     $B0F0                   
B0CC: 33 C5           LEAU    B,U                 
B0CE: E6 C4           LDB     ,U                  
B0D0: C1 70           CMPB    #$70                  
B0D2: 24 ; ????
B0D3: 18 ; ????
B0D4: E6 C9 08 00     LDB     $0800,U                 
B0D8: C1 30           CMPB    #$30                  
B0DA: 26 08           BNE     $B0E4                   
B0DC: E6 C4           LDB     ,U                  
B0DE: C4 03           ANDB    #$03                  
B0E0: 26 0A           BNE     $B0EC                   
B0E2: 20 E4           BRA     $B0C8                   
B0E4: C1 20           CMPB    #$20                  
B0E6: 24 ; ????
B0E7: 04 C4           LSR     $C4                   
B0E9: 0F 27           CLR     $27                   
B0EB: DC AA           LDD     $AA                   
B0ED: 1F 20           TFR     Y,D                   
B0EF: D8 BE           EORB    $BE                   
B0F1: 10 ; ????
B0F2: 36 A7           PSHU    PC,Y,B,A,CC                   
B0F4: 17 A6 0F        LBSR    $5706                   
B0F7: B1 10 4C        CMPA    $104C                   
B0FA: 27 0E           BEQ     $B10A                   
B0FC: 25 ; ????
B0FD: 05 ; ????
B0FE: CC 01 00        LDD     #$0100                  
B101: 20 03           BRA     $B106                   
B103: CC 04 04        LDD     #$0404                  
B106: A4 17           ANDA    -9,X                
B108: 27 3B           BEQ     $B145                   
B10A: EC 1E           LDD     -2,X                
B10C: 10 B3 10 4D     CMPD    $104D                   
B110: 27 0E           BEQ     $B120                   
B112: 25 ; ????
B113: 05 ; ????
B114: CC 02 02        LDD     #$0202                  
B117: 20 03           BRA     $B11C                   
B119: CC 08 06        LDD     #$0806                  
B11C: A4 17           ANDA    -9,X                
B11E: 27 25           BEQ     $B145                   
B120: CE B1 61        LDU     #$B161                  
B123: E6 05           LDB     5,X                 
B125: 58 ; ????
B126: A6 C5           LDA     B,U                 
B128: A4 17           ANDA    -9,X                
B12A: 27 18           BEQ     $B144                   
B12C: CB 0C           ADDB    #$0C                  
B12E: C4 0C           ANDB    #$0C                  
B130: A6 C5           LDA     B,U                 
B132: A4 17           ANDA    -9,X                
B134: 27 0E           BEQ     $B144                   
B136: CB 08           ADDB    #$08                  
B138: C4 0C           ANDB    #$0C                  
B13A: A6 C5           LDA     B,U                 
B13C: A4 17           ANDA    -9,X                
B13E: 27 04           BEQ     $B144                   
B140: CB 04           ADDB    #$04                  
B142: C4 0C           ANDB    #$0C                  
B144: 54              LSRB                        
B145: E7 05           STB     5,X                 
B147: A6 19           LDA     -7,X                
B149: 2A 02           BPL     $B14D                   
B14B: CB 08           ADDB    #$08                  
B14D: CB 10           ADDB    #$10                  
B14F: E7 0A           STB     10,X                
B151: 86 10           LDA     #$10                  
B153: A7 1B           STA     -5,X                
B155: BD C0 00        JSR     $C000                   
B158: BD C0 9A        JSR     $C09A                   
B15B: 7E C0 BB        JMP     $C0BB                   
B15E: FF 01 E0        STU     $01E0                   
B161: 01 ; ????
B162: C2 02           SBCB    #$02                  
B164: 01 ; ????
B165: 02 ; ????
B166: 42 ; ????
B167: 04 20           LSR     $20                   
B169: 04 3D           LSR     $3D                   
B16B: 08 ; ????
B16C: 01 ; ????
B16D: 08 ; ????
B16E: 00 12           NEG     $12                   
B170: E6 05           LDB     5,X                 
B172: A6 0F           LDA     15,X                
B174: B1 25 1F        CMPA    $251F                   
B177: 27 1A           BEQ     $B193                   
B179: 25 ; ????
B17A: 09 C1           ROL     $C1                   
B17C: 04 27           LSR     $27                   
B17E: 14 ; ????
B17F: CC 11 00        LDD     #$1100                  
B182: 20 06           BRA     $B18A                   
B184: 5D              TSTB                        
B185: 27 0C           BEQ     $B193                   
B187: CC 44 04        LDD     #$4404                  
B18A: A4 17           ANDA    -9,X                
B18C: 10 27 00 AB     LBEQ    $B23B                   
B190: F7 10 CF        STB     $10CF                   
B193: A6 05           LDA     5,X                 
B195: EE 1E           LDU     -2,X                
B197: 11 B3 25 0E     CMPU    $250E                   
B19B: 27 1B           BEQ     $B1B8                   
B19D: 25 ; ????
B19E: 09 81           ROL     $81                   
B1A0: 06 27           ROR     $27                   
B1A2: 15 ; ????
B1A3: CC 22 02        LDD     #$2202                  
B1A6: 20 07           BRA     $B1AF                   
B1A8: 81 02           CMPA    #$02                  
B1AA: 27 0C           BEQ     $B1B8                   
B1AC: CC 88 06        LDD     #$8806                  
B1AF: A4 17           ANDA    -9,X                
B1B1: 10 27 00 86     LBEQ    $B23B                   
B1B5: F7 10 CF        STB     $10CF                   
B1B8: CE B6 CF        LDU     #$B6CF                  
B1BB: B6 25 1F        LDA     $251F                   
B1BE: A0 0F           SUBA    15,X                
B1C0: 2A 03           BPL     $B1C5                   
B1C2: 40              NEGA                        
B1C3: 33 44           LEAU    4,U                 
B1C5: 81 18           CMPA    #$18                  
B1C7: 22 27           BHI     $B1F0                   
B1C9: FC 25 0E        LDD     $250E                   
B1CC: A3 1E           SUBD    -2,X                
B1CE: 2A 07           BPL     $B1D7                   
B1D0: 43              COMA                        
B1D1: 53              COMB                        
B1D2: C3 00 01        ADDD    #$0001                  
B1D5: 33 42           LEAU    2,U                 
B1D7: 10 83 00 18     CMPD    #$0018                  
B1DB: 22 13           BHI     $B1F0                   
B1DD: E6 17           LDB     -9,X                
B1DF: E4 C4           ANDB    ,U                  
B1E1: 27 0D           BEQ     $B1F0                   
B1E3: E1 C4           CMPB    ,U                  
B1E5: 26 05           BNE     $B1EC                   
B1E7: A6 41           LDA     1,U                 
B1E9: 7E B5 C7        JMP     $B5C7                   
B1EC: 86 0C           LDA     #$0C                  
B1EE: A7 18           STA     -8,X                
B1F0: CE B6 AF        LDU     #$B6AF                  
B1F3: A6 18           LDA     -8,X                
B1F5: 81 0C           CMPA    #$0C                  
B1F7: 25 ; ????
B1F8: 20 A6           BRA     $B1A0                   
B1FA: 0D 27           TST     $27                   
B1FC: 1E B6           EXG     DP,?                   
B1FE: 10 ; ????
B1FF: CF ; ????
B200: E6 C6           LDB     A,U                 
B202: C4 0F           ANDB    #$0F                  
B204: E4 17           ANDB    -9,X                
B206: 10 26 03 BD     LBNE    $B5C7                   
B20A: B6 10 CE        LDA     $10CE                   
B20D: E6 C6           LDB     A,U                 
B20F: C4 0F           ANDB    #$0F                  
B211: E4 17           ANDB    -9,X                
B213: 10 26 03 B0     LBNE    $B5C7                   
B217: 20 02           BRA     $B21B                   
B219: 6C 18           INC     -8,X                
B21B: E6 05           LDB     5,X                 
B21D: A6 C5           LDA     B,U                 
B21F: A4 17           ANDA    -9,X                
B221: 27 18           BEQ     $B23B                   
B223: CB 06           ADDB    #$06                  
B225: C4 06           ANDB    #$06                  
B227: A6 C5           LDA     B,U                 
B229: A4 17           ANDA    -9,X                
B22B: 27 0E           BEQ     $B23B                   
B22D: CB 04           ADDB    #$04                  
B22F: C4 06           ANDB    #$06                  
B231: A6 C5           LDA     B,U                 
B233: A4 17           ANDA    -9,X                
B235: 27 04           BEQ     $B23B                   
B237: CB 02           ADDB    #$02                  
B239: C4 06           ANDB    #$06                  
B23B: F7 10 34        STB     $1034                   
B23E: 39              RTS                         
B23F: 6A 1B           DEC     -5,X                
B241: 27 11           BEQ     $B254                   
B243: A6 1B           LDA     -5,X                
B245: 85 04           BITA    #$04                  
B247: 26 04           BNE     $B24D                   
B249: 86 1A           LDA     #$1A                  
B24B: 20 02           BRA     $B24F                   
B24D: 86 69           LDA     #$69                  
B24F: A7 0A           STA     10,X                
B251: 7E C0 BB        JMP     $C0BB                   
B254: CC 58 03        LDD     #$5803                  
B257: A7 0A           STA     10,X                
B259: E7 1B           STB     -5,X                
B25B: 86 08           LDA     #$08                  
B25D: AA 08           ORA     8,X                 
B25F: A7 08           STA     8,X                 
B261: 6C 1A           INC     -6,X                
B263: A6 05           LDA     5,X                 
B265: 85 04           BITA    #$04                  
B267: 26 05           BNE     $B26E                   
B269: CC FF F8        LDD     #$FFF8                  
B26C: 20 03           BRA     $B271                   
B26E: CC 00 08        LDD     #$0008                  
B271: E3 1E           ADDD    -2,X                
B273: ED 1E           STD     -2,X                
B275: 6C 14           INC     -12,X               
B277: 7E C0 BB        JMP     $C0BB                   
B27A: 6A 1B           DEC     -5,X                
B27C: 27 0F           BEQ     $B28D                   
B27E: 86 01           LDA     #$01                  
B280: B7 40 4E        STA     $404E                   
B283: BD C0 BB        JSR     $C0BB                   
B286: A6 0D           LDA     13,X                
B288: 10 27 00 FD     LBEQ    $B389                   
B28C: 39              RTS                         
B28D: 6C 1A           INC     -6,X                
B28F: CC 03 59        LDD     #$0359                  
B292: A7 1B           STA     -5,X                
B294: E7 0A           STB     10,X                
B296: 6C 13           INC     -13,X               
B298: EE 15           LDU     -11,X               
B29A: A6 08           LDA     8,X                 
B29C: 84 02           ANDA    #$02                  
B29E: A7 48           STA     8,U                 
B2A0: A6 0F           LDA     15,X                
B2A2: 80 08           SUBA    #$08                  
B2A4: A7 4F           STA     15,U                
B2A6: CC 68 01        LDD     #$6801                  
B2A9: ED 4A           STD     10,U                
B2AB: A6 05           LDA     5,X                 
B2AD: 85 04           BITA    #$04                  
B2AF: 26 04           BNE     $B2B5                   
B2B1: 86 E8           LDA     #$E8                  
B2B3: 20 02           BRA     $B2B7                   
B2B5: 86 18           LDA     #$18                  
B2B7: A7 57           STA     -9,U                
B2B9: 10 AE 1E        LDY     -2,X                
B2BC: 31 A6           LEAY    A,Y                 
B2BE: 10 AF 5E        STY     -2,U                
B2C1: BD C0 BB        JSR     $C0BB                   
B2C4: A6 0D           LDA     13,X                
B2C6: 10 27 00 BF     LBEQ    $B389                   
B2CA: E6 05           LDB     5,X                 
B2CC: C5 04           BITB    #$04                  
B2CE: 26 08           BNE     $B2D8                   
B2D0: 81 20           CMPA    #$20                  
B2D2: 10 23 00 B3     LBLS    $B389                   
B2D6: 20 06           BRA     $B2DE                   
B2D8: 81 E0           CMPA    #$E0                  
B2DA: 10 ; ????
B2DB: 24 ; ????
B2DC: 00 AB           NEG     $AB                   
B2DE: AB 57           ADDA    -9,U                
B2E0: A7 4D           STA     13,U                
B2E2: 6F 4C           CLR     12,U                
B2E4: BF 10 36        STX     $1036                   
B2E7: 1F 31           TFR     U,X                   
B2E9: CE 25 10        LDU     #$2510                  
B2EC: A6 0F           LDA     15,X                
B2EE: 8B 0C           ADDA    #$0C                  
B2F0: A7 0F           STA     15,X                
B2F2: BD C4 F4        JSR     $C4F4                   
B2F5: A6 0F           LDA     15,X                
B2F7: 80 0C           SUBA    #$0C                  
B2F9: A7 0F           STA     15,X                
B2FB: B6 10 D3        LDA     $10D3                   
B2FE: 27 2A           BEQ     $B32A                   
B300: CC 01 06        LDD     #$0106                  
B303: B7 10 D0        STA     $10D0                   
B306: E7 5A           STB     -6,U                
B308: 6A 4F           DEC     15,U                
B30A: CC 00 3C        LDD     #$003C                  
B30D: A7 48           STA     8,U                 
B30F: E7 44           STB     4,U                 
B311: F7 10 4F        STB     $104F                   
B314: 7C 40 4D        INC     $404D                   
B317: 6C 4F           INC     15,U                
B319: B6 25 02        LDA     $2502                   
B31C: 27 06           BEQ     $B324                   
B31E: BD A5 4F        JSR     $A54F                   
B321: 7F 25 02        CLR     $2502                   
B324: 7F 25 01        CLR     $2501                   
B327: 7F 10 DA        CLR     $10DA                   
B32A: BE 10 36        LDX     $1036                   
B32D: 86 01           LDA     #$01                  
B32F: B7 40 4E        STA     $404E                   
B332: 39              RTS                         
B333: EE 15           LDU     -11,X               
B335: 6A 1B           DEC     -5,X                
B337: 26 88           BNE     $B2C1                   
B339: 6C 1A           INC     -6,X                
B33B: CC 28 5C        LDD     #$285C                  
B33E: A7 1B           STA     -5,X                
B340: E7 0A           STB     10,X                
B342: CC 01 61        LDD     #$0161                  
B345: A7 54           STA     -12,U               
B347: E7 4A           STB     10,U                
B349: A6 48           LDA     8,U                 
B34B: 8A 08           ORA     #$08                  
B34D: A7 48           STA     8,U                 
B34F: A6 57           LDA     -9,U                
B351: 8B 10           ADDA    #$10                  
B353: 84 E0           ANDA    #$E0                  
B355: 7E B2 B7        JMP     $B2B7                   
B358: EE 15           LDU     -11,X               
B35A: 6A 1B           DEC     -5,X                
B35C: 27 13           BEQ     $B371                   
B35E: A6 1B           LDA     -5,X                
B360: 84 04           ANDA    #$04                  
B362: 44              LSRA                        
B363: 44              LSRA                        
B364: 8A 5C           ORA     #$5C                  
B366: A7 0A           STA     10,X                
B368: 8B 07           ADDA    #$07                  
B36A: 84 65           ANDA    #$65                  
B36C: A7 4A           STA     10,U                
B36E: 7E B2 C1        JMP     $B2C1                   
B371: 6C 1A           INC     -6,X                
B373: CC 07 60        LDD     #$0760                  
B376: A7 1B           STA     -5,X                
B378: E7 0A           STB     10,X                
B37A: C6 65           LDB     #$65                  
B37C: E7 4A           STB     10,U                
B37E: 7E B2 C1        JMP     $B2C1                   
B381: EE 15           LDU     -11,X               
B383: 6A 1B           DEC     -5,X                
B385: 10 26 FF 38     LBNE    $B2C1                   
B389: CC 01 05        LDD     #$0105                  
B38C: A7 1A           STA     -6,X                
B38E: E7 11           STB     -15,X               
B390: 6F 08           CLR     8,X                 
B392: 10 AE 1E        LDY     -2,X                
B395: A6 05           LDA     5,X                 
B397: 85 04           BITA    #$04                  
B399: 26 04           BNE     $B39F                   
B39B: C6 08           LDB     #$08                  
B39D: 20 02           BRA     $B3A1                   
B39F: C6 F8           LDB     #$F8                  
B3A1: 31 A5           LEAY    B,Y                 
B3A3: 10 AF 1E        STY     -2,X                
B3A6: 8A 18           ORA     #$18                  
B3A8: A7 0A           STA     10,X                
B3AA: 6F 14           CLR     -12,X               
B3AC: 6F 1B           CLR     -5,X                
B3AE: 6F 13           CLR     -13,X               
B3B0: 7F 40 4E        CLR     $404E                   
B3B3: 1E 31           EXG     U,X                   
B3B5: BD 87 32        JSR     $8732                   
B3B8: 1E 31           EXG     U,X                   
B3BA: 7E C0 BB        JMP     $C0BB                   
B3BD: A6 05           LDA     5,X                 
B3BF: 84 06           ANDA    #$06                  
B3C1: A7 05           STA     5,X                 
B3C3: 86 01           LDA     #$01                  
B3C5: B7 10 C0        STA     $10C0                   
B3C8: BD C5 34        JSR     $C534                   
B3CB: BF 10 36        STX     $1036                   
B3CE: FF 10 38        STU     $1038                   
B3D1: 8E B6 93        LDX     #$B693                  
B3D4: CC 04 70        LDD     #$0470                  
B3D7: B7 10 09        STA     $1009                   
B3DA: 7F 10 CE        CLR     $10CE                   
B3DD: A6 81           LDA     ,X++                
B3DF: E1 C6           CMPB    A,U                 
B3E1: 23 1F           BLS     $B402                   
B3E3: 8B E0           ADDA    #$E0                  
B3E5: E1 C6           CMPB    A,U                 
B3E7: 23 19           BLS     $B402                   
B3E9: B7 10 34        STA     $1034                   
B3EC: B6 10 09        LDA     $1009                   
B3EF: 85 01           BITA    #$01                  
B3F1: 26 17           BNE     $B40A                   
B3F3: B6 10 34        LDA     $1034                   
B3F6: 8B 21           ADDA    #$21                  
B3F8: E1 C6           CMPB    A,U                 
B3FA: 23 06           BLS     $B402                   
B3FC: 8B E0           ADDA    #$E0                  
B3FE: E1 C6           CMPB    A,U                 
B400: 22 08           BHI     $B40A                   
B402: A6 1F           LDA     -1,X                
B404: BA 10 CE        ORA     $10CE                   
B407: B7 10 CE        STA     $10CE                   
B40A: 7A 10 09        DEC     $1009                   
B40D: 26 CE           BNE     $B3DD                   
B40F: F6 10 CE        LDB     $10CE                   
B412: 58 ; ????
B413: 25 ; ????
B414: 52 ; ????
B415: A6 84           LDA     ,X                  
B417: B7 10 09        STA     $1009                   
B41A: A6 01           LDA     1,X                 
B41C: 33 C6           LEAU    A,U                 
B41E: A6 C9 08 00     LDA     $0800,U                 
B422: 81 10           CMPA    #$10                  
B424: 27 37           BEQ     $B45D                   
B426: 25 ; ????
B427: 10 ; ????
B428: 81 20           CMPA    #$20                  
B42A: 25 ; ????
B42B: 19              DAA                         
B42C: 81 30           CMPA    #$30                  
B42E: 26 2D           BNE     $B45D                   
B430: A6 C4           LDA     ,U                  
B432: A5 04           BITA    4,X                 
B434: 26 1F           BNE     $B455                   
B436: 20 25           BRA     $B45D                   
B438: A6 C4           LDA     ,U                  
B43A: 81 70           CMPA    #$70                  
B43C: 25 ; ????
B43D: 17 B6 10        LBSR    $6A50                   
B440: CE AA 03        LDU     #$AA03                  
B443: 20 15           BRA     $B45A                   
B445: A6 84           LDA     ,X                  
B447: 85 01           BITA    #$01                  
B449: 27 0A           BEQ     $B455                   
B44B: A6 C4           LDA     ,U                  
B44D: 81 60           CMPA    #$60                  
B44F: 25 ; ????
B450: 04 A5           LSR     $A5                   
B452: 84 27           ANDA    #$27                  
B454: 08 ; ????
B455: B6 10 CE        LDA     $10CE                   
B458: AA 02           ORA     2,X                 
B45A: B7 10 CE        STA     $10CE                   
B45D: 7A 10 09        DEC     $1009                   
B460: 27 05           BEQ     $B467                   
B462: 33 C8 E0        LEAU    $E0,U                 
B465: 20 B7           BRA     $B41E                   
B467: FE 10 38        LDU     $1038                   
B46A: 30 05           LEAX    5,X                 
B46C: 8C B6 AF        CMPX    #$B6AF                  
B46F: 26 A1           BNE     $B412                   
B471: B6 10 CE        LDA     $10CE                   
B474: 85 40           BITA    #$40                  
B476: 26 41           BNE     $B4B9                   
B478: BE 10 36        LDX     $1036                   
B47B: E6 0F           LDB     15,X                
B47D: C5 10           BITB    #$10                  
B47F: 27 07           BEQ     $B488                   
B481: 84 FB           ANDA    #$FB                  
B483: B7 10 CE        STA     $10CE                   
B486: 20 37           BRA     $B4BF                   
B488: C6 02           LDB     #$02                  
B48A: F7 10 09        STB     $1009                   
B48D: FE 10 38        LDU     $1038                   
B490: E6 C9 08 00     LDB     $0800,U                 
B494: C1 30           CMPB    #$30                  
B496: 26 08           BNE     $B4A0                   
B498: E6 C4           LDB     ,U                  
B49A: C4 03           ANDB    #$03                  
B49C: 26 0A           BNE     $B4A8                   
B49E: 20 0F           BRA     $B4AF                   
B4A0: C1 10           CMPB    #$10                  
B4A2: 23 0B           BLS     $B4AF                   
B4A4: C1 20           CMPB    #$20                  
B4A6: 24 ; ????
B4A7: 07 8A           ASR     $8A                   
B4A9: 04 B7           LSR     $B7                   
B4AB: 10 CE 20 10     LDS     #$2010                  
B4AF: 7A 10 09        DEC     $1009                   
B4B2: 27 0B           BEQ     $B4BF                   
B4B4: 33 C8 20        LEAU    $20,U                 
B4B7: 20 D7           BRA     $B490                   
B4B9: BE 10 36        LDX     $1036                   
B4BC: B6 10 CE        LDA     $10CE                   
B4BF: A7 17           STA     -9,X                
B4C1: A6 05           LDA     5,X                 
B4C3: B7 10 CE        STA     $10CE                   
B4C6: B7 10 CF        STA     $10CF                   
B4C9: BD 8A A0        JSR     $8AA0                   
B4CC: E6 19           LDB     -7,X                
B4CE: 2A 08           BPL     $B4D8                   
B4D0: 81 D0           CMPA    #$D0                  
B4D2: 10 ; ????
B4D3: 25 ; ????
B4D4: FC 99 20        LDD     $9920                   
B4D7: 06 81           ROR     $81                   
B4D9: D0 10           SUBB    $10                   
B4DB: 24 ; ????
B4DC: FC 91 A6        LDD     $91A6                   
B4DF: 05 ; ????
B4E0: EE 1E           LDU     -2,X                
B4E2: 11 B3 25 0E     CMPU    $250E                   
B4E6: 27 1B           BEQ     $B503                   
B4E8: 25 ; ????
B4E9: 09 81           ROL     $81                   
B4EB: 06 27           ROR     $27                   
B4ED: 15 ; ????
B4EE: CC 22 02        LDD     #$2202                  
B4F1: 20 07           BRA     $B4FA                   
B4F3: 81 02           CMPA    #$02                  
B4F5: 27 0C           BEQ     $B503                   
B4F7: CC 88 06        LDD     #$8806                  
B4FA: A4 17           ANDA    -9,X                
B4FC: 10 27 00 C3     LBEQ    $B5C3                   
B500: F7 10 CE        STB     $10CE                   
B503: E6 05           LDB     5,X                 
B505: A6 0F           LDA     15,X                
B507: B1 25 1F        CMPA    $251F                   
B50A: 27 1A           BEQ     $B526                   
B50C: 25 ; ????
B50D: 09 C1           ROL     $C1                   
B50F: 04 27           LSR     $27                   
B511: 14 ; ????
B512: CC 11 00        LDD     #$1100                  
B515: 20 06           BRA     $B51D                   
B517: 5D              TSTB                        
B518: 27 0C           BEQ     $B526                   
B51A: CC 44 04        LDD     #$4404                  
B51D: A4 17           ANDA    -9,X                
B51F: 10 27 00 A0     LBEQ    $B5C3                   
B523: F7 10 CF        STB     $10CF                   
B526: CE B6 CF        LDU     #$B6CF                  
B529: B6 25 1F        LDA     $251F                   
B52C: A0 0F           SUBA    15,X                
B52E: 2A 03           BPL     $B533                   
B530: 40              NEGA                        
B531: 33 44           LEAU    4,U                 
B533: 81 18           CMPA    #$18                  
B535: 22 43           BHI     $B57A                   
B537: FC 25 0E        LDD     $250E                   
B53A: A3 1E           SUBD    -2,X                
B53C: 2A 07           BPL     $B545                   
B53E: 43              COMA                        
B53F: 53              COMB                        
B540: C3 00 01        ADDD    #$0001                  
B543: 33 42           LEAU    2,U                 
B545: 10 83 00 18     CMPD    #$0018                  
B549: 22 2F           BHI     $B57A                   
B54B: E6 17           LDB     -9,X                
B54D: E4 C4           ANDB    ,U                  
B54F: 27 29           BEQ     $B57A                   
B551: E1 C4           CMPB    ,U                  
B553: 26 04           BNE     $B559                   
B555: A6 41           LDA     1,U                 
B557: 20 6E           BRA     $B5C7                   
B559: 86 0C           LDA     #$0C                  
B55B: A7 18           STA     -8,X                
B55D: B6 10 DD        LDA     $10DD                   
B560: 27 18           BEQ     $B57A                   
B562: 6C 1C           INC     -4,X                
B564: A6 1C           LDA     -4,X                
B566: 81 0A           CMPA    #$0A                  
B568: 25 ; ????
B569: 10 ; ????
B56A: A6 0F           LDA     15,X                
B56C: 81 50           CMPA    #$50                  
B56E: 25 ; ????
B56F: 0A 81           DEC     $81                   
B571: D0 22           SUBB    $22                   
B573: 06 6F           ROR     $6F                   
B575: 1C A6           ANDCC   #$A6                  
B577: 41 ; ????
B578: 20 4D           BRA     $B5C7                   
B57A: CE B6 AF        LDU     #$B6AF                  
B57D: A6 18           LDA     -8,X                
B57F: 81 0C           CMPA    #$0C                  
B581: 25 ; ????
B582: 1E A6           EXG     CC,?                   
B584: 0D B6           TST     $B6                   
B586: 10 CE E6 C6     LDS     #$E6C6                  
B58A: C4 0F           ANDB    #$0F                  
B58C: E4 17           ANDB    -9,X                
B58E: 10 26 00 35     LBNE    $B5C7                   
B592: B6 10 CF        LDA     $10CF                   
B595: E6 C6           LDB     A,U                 
B597: C4 0F           ANDB    #$0F                  
B599: E4 17           ANDB    -9,X                
B59B: 10 26 00 28     LBNE    $B5C7                   
B59F: 20 02           BRA     $B5A3                   
B5A1: 6C 18           INC     -8,X                
B5A3: E6 05           LDB     5,X                 
B5A5: A6 C5           LDA     B,U                 
B5A7: A4 17           ANDA    -9,X                
B5A9: 27 18           BEQ     $B5C3                   
B5AB: CB 02           ADDB    #$02                  
B5AD: C4 06           ANDB    #$06                  
B5AF: A6 C5           LDA     B,U                 
B5B1: A4 17           ANDA    -9,X                
B5B3: 27 0E           BEQ     $B5C3                   
B5B5: CB 04           ADDB    #$04                  
B5B7: C4 06           ANDB    #$06                  
B5B9: A6 C5           LDA     B,U                 
B5BB: A4 17           ANDA    -9,X                
B5BD: 27 04           BEQ     $B5C3                   
B5BF: CB 06           ADDB    #$06                  
B5C1: C4 06           ANDB    #$06                  
B5C3: F7 10 34        STB     $1034                   
B5C6: 39              RTS                         
B5C7: A7 05           STA     5,X                 
B5C9: CC 00 6C        LDD     #$006C                  
B5CC: A7 18           STA     -8,X                
B5CE: A6 19           LDA     -7,X                
B5D0: 2A 02           BPL     $B5D4                   
B5D2: CB 02           ADDB    #$02                  
B5D4: E7 0A           STB     10,X                
B5D6: CC 02 20        LDD     #$0220                  
B5D9: A7 1A           STA     -6,X                
B5DB: A6 05           LDA     5,X                 
B5DD: 84 03           ANDA    #$03                  
B5DF: 26 02           BNE     $B5E3                   
B5E1: C6 10           LDB     #$10                  
B5E3: E7 1B           STB     -5,X                
B5E5: 64 03           LSR     3,X                 
B5E7: 64 03           LSR     3,X                 
B5E9: 86 03           LDA     #$03                  
B5EB: A7 14           STA     -12,X               
B5ED: A6 1B           LDA     -5,X                
B5EF: 27 42           BEQ     $B633                   
B5F1: 81 10           CMPA    #$10                  
B5F3: 10 26 00 86     LBNE    $B67D                   
B5F7: EC 1E           LDD     -2,X                
B5F9: 83 00 18        SUBD    #$0018                  
B5FC: C4 F8           ANDB    #$F8                  
B5FE: 58 ; ????
B5FF: 49              ROLA                        
B600: 58 ; ????
B601: 49              ROLA                        
B602: FD 10 CE        STD     $10CE                   
B605: E6 0F           LDB     15,X                
B607: 54              LSRB                        
B608: 54              LSRB                        
B609: 54              LSRB                        
B60A: 4F              CLRA                        
B60B: F3 10 CE        ADDD    $10CE                   
B60E: FD 10 34        STD     $1034                   
B611: CE B6 D7        LDU     #$B6D7                  
B614: A6 05           LDA     5,X                 
B616: E6 C6           LDB     A,U                 
B618: FE 10 34        LDU     $1034                   
B61B: 33 C5           LEAU    B,U                 
B61D: CC 10 70        LDD     #$1070                  
B620: E1 C4           CMPB    ,U                  
B622: 23 05           BLS     $B629                   
B624: E1 C8 E0        CMPB    $E0,U                 
B627: 22 52           BHI     $B67B                   
B629: E6 05           LDB     5,X                 
B62B: CB 04           ADDB    #$04                  
B62D: C4 07           ANDB    #$07                  
B62F: E7 05           STB     5,X                 
B631: 20 48           BRA     $B67B                   
B633: 6A 1A           DEC     -6,X                
B635: B6 10 E4        LDA     $10E4                   
B638: 26 08           BNE     $B642                   
B63A: 86 01           LDA     #$01                  
B63C: B7 10 5C        STA     $105C                   
B63F: B7 10 E4        STA     $10E4                   
B642: B6 10 49        LDA     $1049                   
B645: 26 05           BNE     $B64C                   
B647: FC 17 1D        LDD     $171D                   
B64A: 20 10           BRA     $B65C                   
B64C: B6 17 17        LDA     $1717                   
B64F: B1 17 1C        CMPA    $171C                   
B652: 22 05           BHI     $B659                   
B654: FC 17 0A        LDD     $170A                   
B657: 20 03           BRA     $B65C                   
B659: FC 17 08        LDD     $1708                   
B65C: 6D 19           TST     -7,X                
B65E: 2A 04           BPL     $B664                   
B660: A7 03           STA     3,X                 
B662: 20 02           BRA     $B666                   
B664: E7 03           STB     3,X                 
B666: A6 05           LDA     5,X                 
B668: 84 06           ANDA    #$06                  
B66A: A7 05           STA     5,X                 
B66C: 8B 10           ADDA    #$10                  
B66E: E6 19           LDB     -7,X                
B670: 2A 02           BPL     $B674                   
B672: 8B 08           ADDA    #$08                  
B674: A7 0A           STA     10,X                
B676: 6F 14           CLR     -12,X               
B678: 7E C0 BB        JMP     $C0BB                   
B67B: A6 1B           LDA     -5,X                
B67D: 84 04           ANDA    #$04                  
B67F: 44              LSRA                        
B680: 44              LSRA                        
B681: B7 10 34        STA     $1034                   
B684: A6 0A           LDA     10,X                
B686: 84 6E           ANDA    #$6E                  
B688: BA 10 34        ORA     $1034                   
B68B: A7 0A           STA     10,X                
B68D: BD C0 00        JSR     $C000                   
B690: 7E C0 BB        JMP     $C0BB                   
B693: 1E 10           EXG     X,D                   
B695: E0 20           SUBB    0,Y                 
B697: 21 40           BRN     $B6D9                   
B699: 60 80           NEG     ,X+                 
B69B: 01 ; ????
B69C: 60 08           NEG     8,X                 
B69E: 80 01           SUBA    #$01                  
B6A0: 02 ; ????
B6A1: 23 04           BLS     $B6A7                   
B6A3: 40              NEGA                        
B6A4: 03 01           COM     $01                   
B6A6: C0 02           SUBB    #$02                  
B6A8: 20 01           BRA     $B6AB                   
B6AA: 02 ; ????
B6AB: 1E 01           EXG     D,X                   
B6AD: 10 ; ????
B6AE: 03 11           COM     $11                   
B6B0: FF 22 F8        STU     $22F8                   
B6B3: 44              LSRA                        
B6B4: 01 ; ????
B6B5: 88 08           EORA    #$08                  
B6B7: 0E 0B           JMP     $0B                   
B6B9: 0D 07           TST     $07                   
B6BB: 0B ; ????
B6BC: 0E 07           JMP     $07                   
B6BE: 0D 20           TST     $20                   
B6C0: 20 FF           BRA     $B6C1                   
B6C2: E0 E0           SUBB    ,S+                 
B6C4: E0 01           SUBB    1,X                 
B6C6: 00 01           NEG     $01                   
B6C8: 20 FF           BRA     $B6C9                   
B6CA: FF FF E0        STU     $FFE0                   
B6CD: 01 ; ????
B6CE: 00 0C           NEG     $0C                   
B6D0: 05 ; ????
B6D1: 06 03           ROR     $03                   
B6D3: 09 07           ROL     $07                   
B6D5: 03 01           COM     $01                   
B6D7: 1D              SEX                         
B6D8: DD DF           STD     $DF                   
B6DA: 00 20           NEG     $20                   
B6DC: 60 5F           NEG     -1,U                
B6DE: 5D              TSTB                        
B6DF: 7F 1F 60        CLR     $1F60                   
B6E2: BD 81 50        JSR     $8150                   
B6E5: B6 1F 60        LDA     $1F60                   
B6E8: 27 F8           BEQ     $B6E2                   
B6EA: BD 81 50        JSR     $8150                   
B6ED: FC 10 D0        LDD     $10D0                   
B6F0: 26 ED           BNE     $B6DF                   
B6F2: B6 1F 60        LDA     $1F60                   
B6F5: 27 EB           BEQ     $B6E2                   
B6F7: 7A 1F 74        DEC     $1F74                   
B6FA: 26 EE           BNE     $B6EA                   
B6FC: 8E 1F 70        LDX     #$1F70                  
B6FF: CC 08 03        LDD     #$0803                  
B702: A7 04           STA     4,X                 
B704: E7 14           STB     -12,X               
B706: CE 15 80        LDU     #$1580                  
B709: 10 8E 15 00     LDY     #$1500                  
B70D: B6 10 08        LDA     $1008                   
B710: 84 E0           ANDA    #$E0                  
B712: 44              LSRA                        
B713: 44              LSRA                        
B714: 8B 08           ADDA    #$08                  
B716: B7 10 34        STA     $1034                   
B719: 8B 2F           ADDA    #$2F                  
B71B: B7 10 35        STA     $1035                   
B71E: BD 8A A0        JSR     $8AA0                   
B721: 84 7F           ANDA    #$7F                  
B723: B1 10 34        CMPA    $1034                   
B726: 23 F6           BLS     $B71E                   
B728: B1 10 35        CMPA    $1035                   
B72B: 24 ; ????
B72C: F1 E6 C6        CMPB    $E6C6                   
B72F: C1 0A           CMPB    #$0A                  
B731: 24 ; ????
B732: EB C1           ADDB    ,U++                
B734: 05 ; ????
B735: 23 E7           BLS     $B71E                   
B737: 6D A6           TST     A,Y                 
B739: 2B E3           BMI     $B71E                   
B73B: 1F 89           TFR     A,B                   
B73D: 84 07           ANDA    #$07                  
B73F: 48 ; ????
B740: 48 ; ????
B741: 48 ; ????
B742: 48 ; ????
B743: 48 ; ????
B744: 8B 14           ADDA    #$14                  
B746: A7 0F           STA     15,X                
B748: C4 78           ANDB    #$78                  
B74A: 86 04           LDA     #$04                  
B74C: 3D              MUL                         
B74D: C3 00 20        ADDD    #$0020                  
B750: ED 1E           STD     -2,X                
B752: F6 17 04        LDB     $1704                   
B755: C1 10           CMPB    #$10                  
B757: 23 0C           BLS     $B765                   
B759: BD 8A A0        JSR     $8AA0                   
B75C: 84 0F           ANDA    #$0F                  
B75E: CE B8 15        LDU     #$B815                  
B761: E6 C6           LDB     A,U                 
B763: 20 03           BRA     $B768                   
B765: 5A              DECB                        
B766: C4 0F           ANDB    #$0F                  
B768: E7 13           STB     -13,X               
B76A: CE B8 05        LDU     #$B805                  
B76D: A6 C5           LDA     B,U                 
B76F: A7 0A           STA     10,X                
B771: 6C 0B           INC     11,X                
B773: 6F 0C           CLR     12,X                
B775: BD C0 BB        JSR     $C0BB                   
B778: BD 81 50        JSR     $8150                   
B77B: B6 1F 60        LDA     $1F60                   
B77E: 27 7C           BEQ     $B7FC                   
B780: FC 10 D0        LDD     $10D0                   
B783: 26 65           BNE     $B7EA                   
B785: 8E 1F 70        LDX     #$1F70                  
B788: CE 25 10        LDU     #$2510                  
B78B: 86 0B           LDA     #$0B                  
B78D: AB 0F           ADDA    15,X                
B78F: A7 0F           STA     15,X                
B791: BD C4 F4        JSR     $C4F4                   
B794: 86 F5           LDA     #$F5                  
B796: AB 0F           ADDA    15,X                
B798: A7 0F           STA     15,X                
B79A: B6 10 D3        LDA     $10D3                   
B79D: 26 0B           BNE     $B7AA                   
B79F: B6 10 50        LDA     $1050                   
B7A2: 26 CF           BNE     $B773                   
B7A4: 6A 04           DEC     4,X                 
B7A6: 26 CB           BNE     $B773                   
B7A8: 20 52           BRA     $B7FC                   
B7AA: CE B8 35        LDU     #$B835                  
B7AD: A6 13           LDA     -13,X               
B7AF: 48 ; ????
B7B0: EC C6           LDD     A,U                 
B7B2: BD 8A DB        JSR     $8ADB                   
B7B5: 8E 1F 70        LDX     #$1F70                  
B7B8: CE B8 25        LDU     #$B825                  
B7BB: A6 13           LDA     -13,X               
B7BD: E6 C6           LDB     A,U                 
B7BF: E7 0A           STB     10,X                
B7C1: CC 0C 3F        LDD     #$0C3F                  
B7C4: A7 0B           STA     11,X                
B7C6: E7 04           STB     4,X                 
B7C8: F7 40 4C        STB     $404C                   
B7CB: BD C0 BB        JSR     $C0BB                   
B7CE: 6F 0C           CLR     12,X                
B7D0: BD 81 50        JSR     $8150                   
B7D3: B6 1F 60        LDA     $1F60                   
B7D6: 27 24           BEQ     $B7FC                   
B7D8: FC 10 D0        LDD     $10D0                   
B7DB: 26 0D           BNE     $B7EA                   
B7DD: 8E 1F 70        LDX     #$1F70                  
B7E0: 6A 04           DEC     4,X                 
B7E2: 26 E7           BNE     $B7CB                   
B7E4: BD 87 32        JSR     $8732                   
B7E7: 7E B6 E2        JMP     $B6E2                   
B7EA: BD 81 50        JSR     $8150                   
B7ED: 8E 1F 70        LDX     #$1F70                  
B7F0: B6 1F 60        LDA     $1F60                   
B7F3: 27 0A           BEQ     $B7FF                   
B7F5: BD C0 BB        JSR     $C0BB                   
B7F8: 6F 0C           CLR     12,X                
B7FA: 20 EE           BRA     $B7EA                   
B7FC: 8E 1F 70        LDX     #$1F70                  
B7FF: BD 87 32        JSR     $8732                   
B802: 7E B6 E2        JMP     $B6E2                   
B805: 46              RORA                        
B806: 47              ASRA                        
B807: 50              NEGB                        
B808: 51 ; ????
B809: 51 ; ????
B80A: 52 ; ????
B80B: 52 ; ????
B80C: 53              COMB                        
B80D: 53              COMB                        
B80E: 7C 7C 7D        INC     $7C7D                   
B811: 7D 7E 7E        TST     $7E7E                   
B814: 7F 01 03        CLR     $0103                   
B817: 03 09           COM     $09                   
B819: 09 0B           ROL     $0B                   
B81B: 0B ; ????
B81C: 0B ; ????
B81D: 0B ; ????
B81E: 0D 0D           TST     $0D                   
B820: 0D 0D           TST     $0D                   
B822: 0F 0F           CLR     $0F                   
B824: 0F F6           CLR     $F6                   
B826: F7 F8 F9        STB     $F8F9                   
B829: F9 FA FA        ADCB    $FAFA                   
B82C: FB FB FC        ADDB    $FBFC                   
B82F: FC FD FD        LDD     $FDFD                   
B832: FE FE FF        LDU     $FEFF                   
B835: 00 40           NEG     $40                   
B837: 00 60           NEG     $60                   
B839: 00 80           NEG     $80                   
B83B: 01 ; ????
B83C: 00 01           NEG     $01                   
B83E: 00 02           NEG     $02                   
B840: 00 02           NEG     $02                   
B842: 00 03           NEG     $03                   
B844: 00 03           NEG     $03                   
B846: 00 04           NEG     $04                   
B848: 00 04           NEG     $04                   
B84A: 00 05           NEG     $05                   
B84C: 00 05           NEG     $05                   
B84E: 00 06           NEG     $06                   
B850: 00 06           NEG     $06                   
B852: 00 07           NEG     $07                   
B854: 00 FF           NEG     $FF                   
B856: FF FF FF        STU     $FFFF                   
B859: FF FF FF        STU     $FFFF                   
B85C: FF FF FF        STU     $FFFF                   
B85F: FF FF FF        STU     $FFFF                   
B862: FF FF FF        STU     $FFFF                   
B865: FF FF FF        STU     $FFFF                   
B868: FF FF FF        STU     $FFFF                   
B86B: FF FF FF        STU     $FFFF                   
B86E: FF FF FF        STU     $FFFF                   
B871: FF FF FF        STU     $FFFF                   
B874: FF FF FF        STU     $FFFF                   
B877: FF FF FF        STU     $FFFF                   
B87A: FF FF FF        STU     $FFFF                   
B87D: FF FF FF        STU     $FFFF                   
B880: FF FF FF        STU     $FFFF                   
B883: FF FF FF        STU     $FFFF                   
B886: FF FF FF        STU     $FFFF                   
B889: FF FF FF        STU     $FFFF                   
B88C: FF FF FF        STU     $FFFF                   
B88F: FF FF FF        STU     $FFFF                   
B892: FF FF FF        STU     $FFFF                   
B895: FF FF FF        STU     $FFFF                   
B898: FF FF FF        STU     $FFFF                   
B89B: FF FF FF        STU     $FFFF                   
B89E: FF FF FF        STU     $FFFF                   
B8A1: FF FF FF        STU     $FFFF                   
B8A4: FF FF FF        STU     $FFFF                   
B8A7: FF FF FF        STU     $FFFF                   
B8AA: FF FF FF        STU     $FFFF                   
B8AD: FF FF FF        STU     $FFFF                   
B8B0: FF FF FF        STU     $FFFF                   
B8B3: FF FF FF        STU     $FFFF                   
B8B6: FF FF FF        STU     $FFFF                   
B8B9: FF FF FF        STU     $FFFF                   
B8BC: FF FF FF        STU     $FFFF                   
B8BF: FF FF FF        STU     $FFFF                   
B8C2: FF FF FF        STU     $FFFF                   
B8C5: FF FF FF        STU     $FFFF                   
B8C8: FF FF FF        STU     $FFFF                   
B8CB: FF FF FF        STU     $FFFF                   
B8CE: FF FF FF        STU     $FFFF                   
B8D1: FF FF FF        STU     $FFFF                   
B8D4: FF FF FF        STU     $FFFF                   
B8D7: FF FF FF        STU     $FFFF                   
B8DA: FF FF FF        STU     $FFFF                   
B8DD: FF FF FF        STU     $FFFF                   
B8E0: FF FF FF        STU     $FFFF                   
B8E3: FF FF FF        STU     $FFFF                   
B8E6: FF FF FF        STU     $FFFF                   
B8E9: FF FF FF        STU     $FFFF                   
B8EC: FF FF FF        STU     $FFFF                   
B8EF: FF FF FF        STU     $FFFF                   
B8F2: FF FF FF        STU     $FFFF                   
B8F5: FF FF FF        STU     $FFFF                   
B8F8: FF FF FF        STU     $FFFF                   
B8FB: FF FF FF        STU     $FFFF                   
B8FE: FF FF FF        STU     $FFFF                   
B901: FF FF FF        STU     $FFFF                   
B904: FF FF FF        STU     $FFFF                   
B907: FF FF FF        STU     $FFFF                   
B90A: FF FF FF        STU     $FFFF                   
B90D: FF FF FF        STU     $FFFF                   
B910: FF FF FF        STU     $FFFF                   
B913: FF FF FF        STU     $FFFF                   
B916: FF FF FF        STU     $FFFF                   
B919: FF FF FF        STU     $FFFF                   
B91C: FF FF FF        STU     $FFFF                   
B91F: FF FF FF        STU     $FFFF                   
B922: FF FF FF        STU     $FFFF                   
B925: FF FF FF        STU     $FFFF                   
B928: FF FF FF        STU     $FFFF                   
B92B: FF FF FF        STU     $FFFF                   
B92E: FF FF FF        STU     $FFFF                   
B931: FF FF FF        STU     $FFFF                   
B934: FF FF FF        STU     $FFFF                   
B937: FF FF FF        STU     $FFFF                   
B93A: FF FF FF        STU     $FFFF                   
B93D: FF FF FF        STU     $FFFF                   
B940: FF FF FF        STU     $FFFF                   
B943: FF FF FF        STU     $FFFF                   
B946: FF FF FF        STU     $FFFF                   
B949: FF FF FF        STU     $FFFF                   
B94C: FF FF FF        STU     $FFFF                   
B94F: FF FF FF        STU     $FFFF                   
B952: FF FF FF        STU     $FFFF                   
B955: FF FF FF        STU     $FFFF                   
B958: FF FF FF        STU     $FFFF                   
B95B: FF FF FF        STU     $FFFF                   
B95E: FF FF FF        STU     $FFFF                   
B961: FF FF FF        STU     $FFFF                   
B964: FF FF FF        STU     $FFFF                   
B967: FF FF FF        STU     $FFFF                   
B96A: FF FF FF        STU     $FFFF                   
B96D: FF FF FF        STU     $FFFF                   
B970: FF FF FF        STU     $FFFF                   
B973: FF FF FF        STU     $FFFF                   
B976: FF FF FF        STU     $FFFF                   
B979: FF FF FF        STU     $FFFF                   
B97C: FF FF FF        STU     $FFFF                   
B97F: FF FF FF        STU     $FFFF                   
B982: FF FF FF        STU     $FFFF                   
B985: FF FF FF        STU     $FFFF                   
B988: FF FF FF        STU     $FFFF                   
B98B: FF FF FF        STU     $FFFF                   
B98E: FF FF FF        STU     $FFFF                   
B991: FF FF FF        STU     $FFFF                   
B994: FF FF FF        STU     $FFFF                   
B997: FF FF FF        STU     $FFFF                   
B99A: FF FF FF        STU     $FFFF                   
B99D: FF FF FF        STU     $FFFF                   
B9A0: FF FF FF        STU     $FFFF                   
B9A3: FF FF FF        STU     $FFFF                   
B9A6: FF FF FF        STU     $FFFF                   
B9A9: FF FF FF        STU     $FFFF                   
B9AC: FF FF FF        STU     $FFFF                   
B9AF: FF FF FF        STU     $FFFF                   
B9B2: FF FF FF        STU     $FFFF                   
B9B5: FF FF FF        STU     $FFFF                   
B9B8: FF FF FF        STU     $FFFF                   
B9BB: FF FF FF        STU     $FFFF                   
B9BE: FF FF FF        STU     $FFFF                   
B9C1: FF FF FF        STU     $FFFF                   
B9C4: FF FF FF        STU     $FFFF                   
B9C7: FF FF FF        STU     $FFFF                   
B9CA: FF FF FF        STU     $FFFF                   
B9CD: FF FF FF        STU     $FFFF                   
B9D0: FF FF FF        STU     $FFFF                   
B9D3: FF FF FF        STU     $FFFF                   
B9D6: FF FF FF        STU     $FFFF                   
B9D9: FF FF FF        STU     $FFFF                   
B9DC: FF FF FF        STU     $FFFF                   
B9DF: FF FF FF        STU     $FFFF                   
B9E2: FF FF FF        STU     $FFFF                   
B9E5: FF FF FF        STU     $FFFF                   
B9E8: FF FF FF        STU     $FFFF                   
B9EB: FF FF FF        STU     $FFFF                   
B9EE: FF FF FF        STU     $FFFF                   
B9F1: FF FF FF        STU     $FFFF                   
B9F4: FF FF FF        STU     $FFFF                   
B9F7: FF FF FF        STU     $FFFF                   
B9FA: FF FF FF        STU     $FFFF                   
B9FD: FF FF FF        STU     $FFFF                   
BA00: FF FF FF        STU     $FFFF                   
BA03: FF FF FF        STU     $FFFF                   
BA06: FF FF FF        STU     $FFFF                   
BA09: FF FF FF        STU     $FFFF                   
BA0C: FF FF FF        STU     $FFFF                   
BA0F: FF FF FF        STU     $FFFF                   
BA12: FF FF FF        STU     $FFFF                   
BA15: FF FF FF        STU     $FFFF                   
BA18: FF FF FF        STU     $FFFF                   
BA1B: FF FF FF        STU     $FFFF                   
BA1E: FF FF FF        STU     $FFFF                   
BA21: FF FF FF        STU     $FFFF                   
BA24: FF FF FF        STU     $FFFF                   
BA27: FF FF FF        STU     $FFFF                   
BA2A: FF FF FF        STU     $FFFF                   
BA2D: FF FF FF        STU     $FFFF                   
BA30: FF FF FF        STU     $FFFF                   
BA33: FF FF FF        STU     $FFFF                   
BA36: FF FF FF        STU     $FFFF                   
BA39: FF FF FF        STU     $FFFF                   
BA3C: FF FF FF        STU     $FFFF                   
BA3F: FF FF FF        STU     $FFFF                   
BA42: FF FF FF        STU     $FFFF                   
BA45: FF FF FF        STU     $FFFF                   
BA48: FF FF FF        STU     $FFFF                   
BA4B: FF FF FF        STU     $FFFF                   
BA4E: FF FF FF        STU     $FFFF                   
BA51: FF FF FF        STU     $FFFF                   
BA54: FF FF FF        STU     $FFFF                   
BA57: FF FF FF        STU     $FFFF                   
BA5A: FF FF FF        STU     $FFFF                   
BA5D: FF FF FF        STU     $FFFF                   
BA60: FF FF FF        STU     $FFFF                   
BA63: FF FF FF        STU     $FFFF                   
BA66: FF FF FF        STU     $FFFF                   
BA69: FF FF FF        STU     $FFFF                   
BA6C: FF FF FF        STU     $FFFF                   
BA6F: FF FF FF        STU     $FFFF                   
BA72: FF FF FF        STU     $FFFF                   
BA75: FF FF FF        STU     $FFFF                   
BA78: FF FF FF        STU     $FFFF                   
BA7B: FF FF FF        STU     $FFFF                   
BA7E: FF FF FF        STU     $FFFF                   
BA81: FF FF FF        STU     $FFFF                   
BA84: FF FF FF        STU     $FFFF                   
BA87: FF FF FF        STU     $FFFF                   
BA8A: FF FF FF        STU     $FFFF                   
BA8D: FF FF FF        STU     $FFFF                   
BA90: FF FF FF        STU     $FFFF                   
BA93: FF FF FF        STU     $FFFF                   
BA96: FF FF FF        STU     $FFFF                   
BA99: FF FF FF        STU     $FFFF                   
BA9C: FF FF FF        STU     $FFFF                   
BA9F: FF FF FF        STU     $FFFF                   
BAA2: FF FF FF        STU     $FFFF                   
BAA5: FF FF FF        STU     $FFFF                   
BAA8: FF FF FF        STU     $FFFF                   
BAAB: FF FF FF        STU     $FFFF                   
BAAE: FF FF FF        STU     $FFFF                   
BAB1: FF FF FF        STU     $FFFF                   
BAB4: FF FF FF        STU     $FFFF                   
BAB7: FF FF FF        STU     $FFFF                   
BABA: FF FF FF        STU     $FFFF                   
BABD: FF FF FF        STU     $FFFF                   
BAC0: FF FF FF        STU     $FFFF                   
BAC3: FF FF FF        STU     $FFFF                   
BAC6: FF FF FF        STU     $FFFF                   
BAC9: FF FF FF        STU     $FFFF                   
BACC: FF FF FF        STU     $FFFF                   
BACF: FF FF FF        STU     $FFFF                   
BAD2: FF FF FF        STU     $FFFF                   
BAD5: FF FF FF        STU     $FFFF                   
BAD8: FF FF FF        STU     $FFFF                   
BADB: FF FF FF        STU     $FFFF                   
BADE: FF FF FF        STU     $FFFF                   
BAE1: FF FF FF        STU     $FFFF                   
BAE4: FF FF FF        STU     $FFFF                   
BAE7: FF FF FF        STU     $FFFF                   
BAEA: FF FF FF        STU     $FFFF                   
BAED: FF FF FF        STU     $FFFF                   
BAF0: FF FF FF        STU     $FFFF                   
BAF3: FF FF FF        STU     $FFFF                   
BAF6: FF FF FF        STU     $FFFF                   
BAF9: FF FF FF        STU     $FFFF                   
BAFC: FF FF FF        STU     $FFFF                   
BAFF: FF FF FF        STU     $FFFF                   
BB02: FF FF FF        STU     $FFFF                   
BB05: FF FF FF        STU     $FFFF                   
BB08: FF FF FF        STU     $FFFF                   
BB0B: FF FF FF        STU     $FFFF                   
BB0E: FF FF FF        STU     $FFFF                   
BB11: FF FF FF        STU     $FFFF                   
BB14: FF FF FF        STU     $FFFF                   
BB17: FF FF FF        STU     $FFFF                   
BB1A: FF FF FF        STU     $FFFF                   
BB1D: FF FF FF        STU     $FFFF                   
BB20: FF FF FF        STU     $FFFF                   
BB23: FF FF FF        STU     $FFFF                   
BB26: FF FF FF        STU     $FFFF                   
BB29: FF FF FF        STU     $FFFF                   
BB2C: FF FF FF        STU     $FFFF                   
BB2F: FF FF FF        STU     $FFFF                   
BB32: FF FF FF        STU     $FFFF                   
BB35: FF FF FF        STU     $FFFF                   
BB38: FF FF FF        STU     $FFFF                   
BB3B: FF FF FF        STU     $FFFF                   
BB3E: FF FF FF        STU     $FFFF                   
BB41: FF FF FF        STU     $FFFF                   
BB44: FF FF FF        STU     $FFFF                   
BB47: FF FF FF        STU     $FFFF                   
BB4A: FF FF FF        STU     $FFFF                   
BB4D: FF FF FF        STU     $FFFF                   
BB50: FF FF FF        STU     $FFFF                   
BB53: FF FF FF        STU     $FFFF                   
BB56: FF FF FF        STU     $FFFF                   
BB59: FF FF FF        STU     $FFFF                   
BB5C: FF FF FF        STU     $FFFF                   
BB5F: FF FF FF        STU     $FFFF                   
BB62: FF FF FF        STU     $FFFF                   
BB65: FF FF FF        STU     $FFFF                   
BB68: FF FF FF        STU     $FFFF                   
BB6B: FF FF FF        STU     $FFFF                   
BB6E: FF FF FF        STU     $FFFF                   
BB71: FF FF FF        STU     $FFFF                   
BB74: FF FF FF        STU     $FFFF                   
BB77: FF FF FF        STU     $FFFF                   
BB7A: FF FF FF        STU     $FFFF                   
BB7D: FF FF FF        STU     $FFFF                   
BB80: FF FF FF        STU     $FFFF                   
BB83: FF FF FF        STU     $FFFF                   
BB86: FF FF FF        STU     $FFFF                   
BB89: FF FF FF        STU     $FFFF                   
BB8C: FF FF FF        STU     $FFFF                   
BB8F: FF FF FF        STU     $FFFF                   
BB92: FF FF FF        STU     $FFFF                   
BB95: FF FF FF        STU     $FFFF                   
BB98: FF FF FF        STU     $FFFF                   
BB9B: FF FF FF        STU     $FFFF                   
BB9E: FF FF FF        STU     $FFFF                   
BBA1: FF FF FF        STU     $FFFF                   
BBA4: FF FF FF        STU     $FFFF                   
BBA7: FF FF FF        STU     $FFFF                   
BBAA: FF FF FF        STU     $FFFF                   
BBAD: FF FF FF        STU     $FFFF                   
BBB0: FF FF FF        STU     $FFFF                   
BBB3: FF FF FF        STU     $FFFF                   
BBB6: FF FF FF        STU     $FFFF                   
BBB9: FF FF FF        STU     $FFFF                   
BBBC: FF FF FF        STU     $FFFF                   
BBBF: FF FF FF        STU     $FFFF                   
BBC2: FF FF FF        STU     $FFFF                   
BBC5: FF FF FF        STU     $FFFF                   
BBC8: FF FF FF        STU     $FFFF                   
BBCB: FF FF FF        STU     $FFFF                   
BBCE: FF FF FF        STU     $FFFF                   
BBD1: FF FF FF        STU     $FFFF                   
BBD4: FF FF FF        STU     $FFFF                   
BBD7: FF FF FF        STU     $FFFF                   
BBDA: FF FF FF        STU     $FFFF                   
BBDD: FF FF FF        STU     $FFFF                   
BBE0: FF FF FF        STU     $FFFF                   
BBE3: FF FF FF        STU     $FFFF                   
BBE6: FF FF FF        STU     $FFFF                   
BBE9: FF FF FF        STU     $FFFF                   
BBEC: FF FF FF        STU     $FFFF                   
BBEF: FF FF FF        STU     $FFFF                   
BBF2: FF FF FF        STU     $FFFF                   
BBF5: FF FF FF        STU     $FFFF                   
BBF8: FF FF FF        STU     $FFFF                   
BBFB: FF FF FF        STU     $FFFF                   
BBFE: FF FF FF        STU     $FFFF                   
BC01: FF FF FF        STU     $FFFF                   
BC04: FF FF FF        STU     $FFFF                   
BC07: FF FF FF        STU     $FFFF                   
BC0A: FF FF FF        STU     $FFFF                   
BC0D: FF FF FF        STU     $FFFF                   
BC10: FF FF FF        STU     $FFFF                   
BC13: FF FF FF        STU     $FFFF                   
BC16: FF FF FF        STU     $FFFF                   
BC19: FF FF FF        STU     $FFFF                   
BC1C: FF FF FF        STU     $FFFF                   
BC1F: FF FF FF        STU     $FFFF                   
BC22: FF FF FF        STU     $FFFF                   
BC25: FF FF FF        STU     $FFFF                   
BC28: FF FF FF        STU     $FFFF                   
BC2B: FF FF FF        STU     $FFFF                   
BC2E: FF FF FF        STU     $FFFF                   
BC31: FF FF FF        STU     $FFFF                   
BC34: FF FF FF        STU     $FFFF                   
BC37: FF FF FF        STU     $FFFF                   
BC3A: FF FF FF        STU     $FFFF                   
BC3D: FF FF FF        STU     $FFFF                   
BC40: FF FF FF        STU     $FFFF                   
BC43: FF FF FF        STU     $FFFF                   
BC46: FF FF FF        STU     $FFFF                   
BC49: FF FF FF        STU     $FFFF                   
BC4C: FF FF FF        STU     $FFFF                   
BC4F: FF FF FF        STU     $FFFF                   
BC52: FF FF FF        STU     $FFFF                   
BC55: FF FF FF        STU     $FFFF                   
BC58: FF FF FF        STU     $FFFF                   
BC5B: FF FF FF        STU     $FFFF                   
BC5E: FF FF FF        STU     $FFFF                   
BC61: FF FF FF        STU     $FFFF                   
BC64: FF FF FF        STU     $FFFF                   
BC67: FF FF FF        STU     $FFFF                   
BC6A: FF FF FF        STU     $FFFF                   
BC6D: FF FF FF        STU     $FFFF                   
BC70: FF FF FF        STU     $FFFF                   
BC73: FF FF FF        STU     $FFFF                   
BC76: FF FF FF        STU     $FFFF                   
BC79: FF FF FF        STU     $FFFF                   
BC7C: FF FF FF        STU     $FFFF                   
BC7F: FF FF FF        STU     $FFFF                   
BC82: FF FF FF        STU     $FFFF                   
BC85: FF FF FF        STU     $FFFF                   
BC88: FF FF FF        STU     $FFFF                   
BC8B: FF FF FF        STU     $FFFF                   
BC8E: FF FF FF        STU     $FFFF                   
BC91: FF FF FF        STU     $FFFF                   
BC94: FF FF FF        STU     $FFFF                   
BC97: FF FF FF        STU     $FFFF                   
BC9A: FF FF FF        STU     $FFFF                   
BC9D: FF FF FF        STU     $FFFF                   
BCA0: FF FF FF        STU     $FFFF                   
BCA3: FF FF FF        STU     $FFFF                   
BCA6: FF FF FF        STU     $FFFF                   
BCA9: FF FF FF        STU     $FFFF                   
BCAC: FF FF FF        STU     $FFFF                   
BCAF: FF FF FF        STU     $FFFF                   
BCB2: FF FF FF        STU     $FFFF                   
BCB5: FF FF FF        STU     $FFFF                   
BCB8: FF FF FF        STU     $FFFF                   
BCBB: FF FF FF        STU     $FFFF                   
BCBE: FF FF FF        STU     $FFFF                   
BCC1: FF FF FF        STU     $FFFF                   
BCC4: FF FF FF        STU     $FFFF                   
BCC7: FF FF FF        STU     $FFFF                   
BCCA: FF FF FF        STU     $FFFF                   
BCCD: FF FF FF        STU     $FFFF                   
BCD0: FF FF FF        STU     $FFFF                   
BCD3: FF FF FF        STU     $FFFF                   
BCD6: FF FF FF        STU     $FFFF                   
BCD9: FF FF FF        STU     $FFFF                   
BCDC: FF FF FF        STU     $FFFF                   
BCDF: FF FF FF        STU     $FFFF                   
BCE2: FF FF FF        STU     $FFFF                   
BCE5: FF FF FF        STU     $FFFF                   
BCE8: FF FF FF        STU     $FFFF                   
BCEB: FF FF FF        STU     $FFFF                   
BCEE: FF FF FF        STU     $FFFF                   
BCF1: FF FF FF        STU     $FFFF                   
BCF4: FF FF FF        STU     $FFFF                   
BCF7: FF FF FF        STU     $FFFF                   
BCFA: FF FF FF        STU     $FFFF                   
BCFD: FF FF FF        STU     $FFFF                   
BD00: FF FF FF        STU     $FFFF                   
BD03: FF FF FF        STU     $FFFF                   
BD06: FF FF FF        STU     $FFFF                   
BD09: FF FF FF        STU     $FFFF                   
BD0C: FF FF FF        STU     $FFFF                   
BD0F: FF FF FF        STU     $FFFF                   
BD12: FF FF FF        STU     $FFFF                   
BD15: FF FF FF        STU     $FFFF                   
BD18: FF FF FF        STU     $FFFF                   
BD1B: FF FF FF        STU     $FFFF                   
BD1E: FF FF FF        STU     $FFFF                   
BD21: FF FF FF        STU     $FFFF                   
BD24: FF FF FF        STU     $FFFF                   
BD27: FF FF FF        STU     $FFFF                   
BD2A: FF FF FF        STU     $FFFF                   
BD2D: FF FF FF        STU     $FFFF                   
BD30: FF FF FF        STU     $FFFF                   
BD33: FF FF FF        STU     $FFFF                   
BD36: FF FF FF        STU     $FFFF                   
BD39: FF FF FF        STU     $FFFF                   
BD3C: FF FF FF        STU     $FFFF                   
BD3F: FF FF FF        STU     $FFFF                   
BD42: FF FF FF        STU     $FFFF                   
BD45: FF FF FF        STU     $FFFF                   
BD48: FF FF FF        STU     $FFFF                   
BD4B: FF FF FF        STU     $FFFF                   
BD4E: FF FF FF        STU     $FFFF                   
BD51: FF FF FF        STU     $FFFF                   
BD54: FF FF FF        STU     $FFFF                   
BD57: FF FF FF        STU     $FFFF                   
BD5A: FF FF FF        STU     $FFFF                   
BD5D: FF FF FF        STU     $FFFF                   
BD60: FF FF FF        STU     $FFFF                   
BD63: FF FF FF        STU     $FFFF                   
BD66: FF FF FF        STU     $FFFF                   
BD69: FF FF FF        STU     $FFFF                   
BD6C: FF FF FF        STU     $FFFF                   
BD6F: FF FF FF        STU     $FFFF                   
BD72: FF FF FF        STU     $FFFF                   
BD75: FF FF FF        STU     $FFFF                   
BD78: FF FF FF        STU     $FFFF                   
BD7B: FF FF FF        STU     $FFFF                   
BD7E: FF FF FF        STU     $FFFF                   
BD81: FF FF FF        STU     $FFFF                   
BD84: FF FF FF        STU     $FFFF                   
BD87: FF FF FF        STU     $FFFF                   
BD8A: FF FF FF        STU     $FFFF                   
BD8D: FF FF FF        STU     $FFFF                   
BD90: FF FF FF        STU     $FFFF                   
BD93: FF FF FF        STU     $FFFF                   
BD96: FF FF FF        STU     $FFFF                   
BD99: FF FF FF        STU     $FFFF                   
BD9C: FF FF FF        STU     $FFFF                   
BD9F: FF FF FF        STU     $FFFF                   
BDA2: FF FF FF        STU     $FFFF                   
BDA5: FF FF FF        STU     $FFFF                   
BDA8: FF FF FF        STU     $FFFF                   
BDAB: FF FF FF        STU     $FFFF                   
BDAE: FF FF FF        STU     $FFFF                   
BDB1: FF FF FF        STU     $FFFF                   
BDB4: FF FF FF        STU     $FFFF                   
BDB7: FF FF FF        STU     $FFFF                   
BDBA: FF FF FF        STU     $FFFF                   
BDBD: FF FF FF        STU     $FFFF                   
BDC0: FF FF FF        STU     $FFFF                   
BDC3: FF FF FF        STU     $FFFF                   
BDC6: FF FF FF        STU     $FFFF                   
BDC9: FF FF FF        STU     $FFFF                   
BDCC: FF FF FF        STU     $FFFF                   
BDCF: FF FF FF        STU     $FFFF                   
BDD2: FF FF FF        STU     $FFFF                   
BDD5: FF FF FF        STU     $FFFF                   
BDD8: FF FF FF        STU     $FFFF                   
BDDB: FF FF FF        STU     $FFFF                   
BDDE: FF FF FF        STU     $FFFF                   
BDE1: FF FF FF        STU     $FFFF                   
BDE4: FF FF FF        STU     $FFFF                   
BDE7: FF FF FF        STU     $FFFF                   
BDEA: FF FF FF        STU     $FFFF                   
BDED: FF FF FF        STU     $FFFF                   
BDF0: FF FF FF        STU     $FFFF                   
BDF3: FF FF FF        STU     $FFFF                   
BDF6: FF FF FF        STU     $FFFF                   
BDF9: FF FF FF        STU     $FFFF                   
BDFC: FF FF FF        STU     $FFFF                   
BDFF: FF FF FF        STU     $FFFF                   
BE02: FF FF FF        STU     $FFFF                   
BE05: FF FF FF        STU     $FFFF                   
BE08: FF FF FF        STU     $FFFF                   
BE0B: FF FF FF        STU     $FFFF                   
BE0E: FF FF FF        STU     $FFFF                   
BE11: FF FF FF        STU     $FFFF                   
BE14: FF FF FF        STU     $FFFF                   
BE17: FF FF FF        STU     $FFFF                   
BE1A: FF FF FF        STU     $FFFF                   
BE1D: FF FF FF        STU     $FFFF                   
BE20: FF FF FF        STU     $FFFF                   
BE23: FF FF FF        STU     $FFFF                   
BE26: FF FF FF        STU     $FFFF                   
BE29: FF FF FF        STU     $FFFF                   
BE2C: FF FF FF        STU     $FFFF                   
BE2F: FF FF FF        STU     $FFFF                   
BE32: FF FF FF        STU     $FFFF                   
BE35: FF FF FF        STU     $FFFF                   
BE38: FF FF FF        STU     $FFFF                   
BE3B: FF FF FF        STU     $FFFF                   
BE3E: FF FF FF        STU     $FFFF                   
BE41: FF FF FF        STU     $FFFF                   
BE44: FF FF FF        STU     $FFFF                   
BE47: FF FF FF        STU     $FFFF                   
BE4A: FF FF FF        STU     $FFFF                   
BE4D: FF FF FF        STU     $FFFF                   
BE50: FF FF FF        STU     $FFFF                   
BE53: FF FF FF        STU     $FFFF                   
BE56: FF FF FF        STU     $FFFF                   
BE59: FF FF FF        STU     $FFFF                   
BE5C: FF FF FF        STU     $FFFF                   
BE5F: FF FF FF        STU     $FFFF                   
BE62: FF FF FF        STU     $FFFF                   
BE65: FF FF FF        STU     $FFFF                   
BE68: FF FF FF        STU     $FFFF                   
BE6B: FF FF FF        STU     $FFFF                   
BE6E: FF FF FF        STU     $FFFF                   
BE71: FF FF FF        STU     $FFFF                   
BE74: FF FF FF        STU     $FFFF                   
BE77: FF FF FF        STU     $FFFF                   
BE7A: FF FF FF        STU     $FFFF                   
BE7D: FF FF FF        STU     $FFFF                   
BE80: FF FF FF        STU     $FFFF                   
BE83: FF FF FF        STU     $FFFF                   
BE86: FF FF FF        STU     $FFFF                   
BE89: FF FF FF        STU     $FFFF                   
BE8C: FF FF FF        STU     $FFFF                   
BE8F: FF FF FF        STU     $FFFF                   
BE92: FF FF FF        STU     $FFFF                   
BE95: FF FF FF        STU     $FFFF                   
BE98: FF FF FF        STU     $FFFF                   
BE9B: FF FF FF        STU     $FFFF                   
BE9E: FF FF FF        STU     $FFFF                   
BEA1: FF FF FF        STU     $FFFF                   
BEA4: FF FF FF        STU     $FFFF                   
BEA7: FF FF FF        STU     $FFFF                   
BEAA: FF FF FF        STU     $FFFF                   
BEAD: FF FF FF        STU     $FFFF                   
BEB0: FF FF FF        STU     $FFFF                   
BEB3: FF FF FF        STU     $FFFF                   
BEB6: FF FF FF        STU     $FFFF                   
BEB9: FF FF FF        STU     $FFFF                   
BEBC: FF FF FF        STU     $FFFF                   
BEBF: FF FF FF        STU     $FFFF                   
BEC2: FF FF FF        STU     $FFFF                   
BEC5: FF FF FF        STU     $FFFF                   
BEC8: FF FF FF        STU     $FFFF                   
BECB: FF FF FF        STU     $FFFF                   
BECE: FF FF FF        STU     $FFFF                   
BED1: FF FF FF        STU     $FFFF                   
BED4: FF FF FF        STU     $FFFF                   
BED7: FF FF FF        STU     $FFFF                   
BEDA: FF FF FF        STU     $FFFF                   
BEDD: FF FF FF        STU     $FFFF                   
BEE0: FF FF FF        STU     $FFFF                   
BEE3: FF FF FF        STU     $FFFF                   
BEE6: FF FF FF        STU     $FFFF                   
BEE9: FF FF FF        STU     $FFFF                   
BEEC: FF FF FF        STU     $FFFF                   
BEEF: FF FF FF        STU     $FFFF                   
BEF2: FF FF FF        STU     $FFFF                   
BEF5: FF FF FF        STU     $FFFF                   
BEF8: FF FF FF        STU     $FFFF                   
BEFB: FF FF FF        STU     $FFFF                   
BEFE: FF FF FF        STU     $FFFF                   
BF01: FF FF FF        STU     $FFFF                   
BF04: FF FF FF        STU     $FFFF                   
BF07: FF FF FF        STU     $FFFF                   
BF0A: FF FF FF        STU     $FFFF                   
BF0D: FF FF FF        STU     $FFFF                   
BF10: FF FF FF        STU     $FFFF                   
BF13: FF FF FF        STU     $FFFF                   
BF16: FF FF FF        STU     $FFFF                   
BF19: FF FF FF        STU     $FFFF                   
BF1C: FF FF FF        STU     $FFFF                   
BF1F: FF FF FF        STU     $FFFF                   
BF22: FF FF FF        STU     $FFFF                   
BF25: FF FF FF        STU     $FFFF                   
BF28: FF FF FF        STU     $FFFF                   
BF2B: FF FF FF        STU     $FFFF                   
BF2E: FF FF FF        STU     $FFFF                   
BF31: FF FF FF        STU     $FFFF                   
BF34: FF FF FF        STU     $FFFF                   
BF37: FF FF FF        STU     $FFFF                   
BF3A: FF FF FF        STU     $FFFF                   
BF3D: FF FF FF        STU     $FFFF                   
BF40: FF FF FF        STU     $FFFF                   
BF43: FF FF FF        STU     $FFFF                   
BF46: FF FF FF        STU     $FFFF                   
BF49: FF FF FF        STU     $FFFF                   
BF4C: FF FF FF        STU     $FFFF                   
BF4F: FF FF FF        STU     $FFFF                   
BF52: FF FF FF        STU     $FFFF                   
BF55: FF FF FF        STU     $FFFF                   
BF58: FF FF FF        STU     $FFFF                   
BF5B: FF FF FF        STU     $FFFF                   
BF5E: FF FF FF        STU     $FFFF                   
BF61: FF FF FF        STU     $FFFF                   
BF64: FF FF FF        STU     $FFFF                   
BF67: FF FF FF        STU     $FFFF                   
BF6A: FF FF FF        STU     $FFFF                   
BF6D: FF FF FF        STU     $FFFF                   
BF70: FF FF FF        STU     $FFFF                   
BF73: FF FF FF        STU     $FFFF                   
BF76: FF FF FF        STU     $FFFF                   
BF79: FF FF FF        STU     $FFFF                   
BF7C: FF FF FF        STU     $FFFF                   
BF7F: FF FF FF        STU     $FFFF                   
BF82: FF FF FF        STU     $FFFF                   
BF85: FF FF FF        STU     $FFFF                   
BF88: FF FF FF        STU     $FFFF                   
BF8B: FF FF FF        STU     $FFFF                   
BF8E: FF FF FF        STU     $FFFF                   
BF91: FF FF FF        STU     $FFFF                   
BF94: FF FF FF        STU     $FFFF                   
BF97: FF FF FF        STU     $FFFF                   
BF9A: FF FF FF        STU     $FFFF                   
BF9D: FF FF FF        STU     $FFFF                   
BFA0: FF FF FF        STU     $FFFF                   
BFA3: FF FF FF        STU     $FFFF                   
BFA6: FF FF FF        STU     $FFFF                   
BFA9: FF FF FF        STU     $FFFF                   
BFAC: FF FF FF        STU     $FFFF                   
BFAF: FF FF FF        STU     $FFFF                   
BFB2: FF FF FF        STU     $FFFF                   
BFB5: FF FF FF        STU     $FFFF                   
BFB8: FF FF FF        STU     $FFFF                   
BFBB: FF FF FF        STU     $FFFF                   
BFBE: FF FF FF        STU     $FFFF                   
BFC1: FF FF FF        STU     $FFFF                   
BFC4: FF FF FF        STU     $FFFF                   
BFC7: FF FF FF        STU     $FFFF                   
BFCA: FF FF FF        STU     $FFFF                   
BFCD: FF FF FF        STU     $FFFF                   
BFD0: FF FF FF        STU     $FFFF                   
BFD3: FF FF FF        STU     $FFFF                   
BFD6: FF FF FF        STU     $FFFF                   
BFD9: FF FF FF        STU     $FFFF                   
BFDC: FF FF FF        STU     $FFFF                   
BFDF: FF 31 39        STU     $3139                   
BFE2: 38 ; ????
BFE3: 35 20           PULS    Y                   
BFE5: 4E ; ????
BFE6: 41 ; ????
BFE7: 4D              TSTA                        
BFE8: 43              COMA                        
BFE9: 4F              CLRA                        
BFEA: 20 41           BRA     $C02D                   
BFEC: 4C              INCA                        
BFED: 4C              INCA                        
BFEE: 20 52           BRA     $C042                   
BFF0: 49              ROLA                        
BFF1: 47              ASRA                        
BFF2: 48 ; ????
BFF3: 54              LSRB                        
BFF4: 53              COMB                        
BFF5: 20 52           BRA     $C049                   
BFF7: 45 ; ????
BFF8: 53              COMB                        
BFF9: 45 ; ????
BFFA: 52 ; ????
BFFB: 56              RORB                        
BFFC: 45 ; ????
BFFD: 44              LSRA                        
BFFE: FF FF E6        STU     $FFE6                   
C001: 03 2A           COM     $2A                   
C003: 06 8D           ROR     $8D                   
C005: 1C E6           ANDCC   #$E6                  
C007: 03 C4           COM     $C4                   
C009: 7F 4F FD        CLR     $4FFD                   
C00C: 10 ; ????
C00D: 6E E6           JMP     A,S                 
C00F: 1D              SEX                         
C010: F3 10 6E        ADDD    $106E                   
C013: 85 01           BITA    #$01                  
C015: 26 09           BNE     $C020                   
C017: C5 80           BITB    #$80                  
C019: 26 03           BNE     $C01E                   
C01B: E7 1D           STB     -3,X                
C01D: 39              RTS                         
C01E: C4 7F           ANDB    #$7F                  
C020: E7 1D           STB     -3,X                
C022: E6 1B           LDB     -5,X                
C024: 26 01           BNE     $C027                   
C026: 39              RTS                         
C027: 6A 1B           DEC     -5,X                
C029: CE C0 70        LDU     #$C070                  
C02C: E6 05           LDB     5,X                 
C02E: A6 C5           LDA     B,U                 
C030: EE 1E           LDU     -2,X                
C032: 85 01           BITA    #$01                  
C034: 27 0A           BEQ     $C040                   
C036: 11 83 00 20     CMPU    #$0020                  
C03A: 23 12           BLS     $C04E                   
C03C: 33 5F           LEAU    -1,U                
C03E: 20 0C           BRA     $C04C                   
C040: 85 02           BITA    #$02                  
C042: 27 0A           BEQ     $C04E                   
C044: 11 83 01 E0     CMPU    #$01E0                  
C048: 24 ; ????
C049: 04 33           LSR     $33                   
C04B: 41 ; ????
C04C: EF 1E           STU     -2,X                
C04E: EE 0E           LDU     14,X                
C050: 85 04           BITA    #$04                  
C052: 27 0B           BEQ     $C05F                   
C054: E6 0F           LDB     15,X                
C056: C1 10           CMPB    #$10                  
C058: 26 01           BNE     $C05B                   
C05A: 39              RTS                         
C05B: 33 5F           LEAU    -1,U                
C05D: 20 0E           BRA     $C06D                   
C05F: 85 08           BITA    #$08                  
C061: 26 01           BNE     $C064                   
C063: 39              RTS                         
C064: 11 83 00 FE     CMPU    #$00FE                  
C068: 25 ; ????
C069: 01 ; ????
C06A: 39              RTS                         
C06B: 33 41           LEAU    1,U                 
C06D: EF 0E           STU     14,X                
C06F: 39              RTS                         
C070: 04 05           LSR     $05                   
C072: 01 ; ????
C073: 09 08           ROL     $08                   
C075: 0A 02           DEC     $02                   
C077: 06 B6           ROR     $B6                   
C079: 10 ; ????
C07A: 01 ; ????
C07B: 84 03           ANDA    #$03                  
C07D: 26 1A           BNE     $C099                   
C07F: CE A6 84        LDU     #$A684                  
C082: E6 05           LDB     5,X                 
C084: A6 0A           LDA     10,X                
C086: 8B 02           ADDA    #$02                  
C088: 84 02           ANDA    #$02                  
C08A: AA C5           ORA     B,U                 
C08C: A7 0A           STA     10,X                
C08E: B6 10 01        LDA     $1001                   
C091: 84 10           ANDA    #$10                  
C093: 44              LSRA                        
C094: 44              LSRA                        
C095: AA 0A           ORA     10,X                
C097: A7 0A           STA     10,X                
C099: 39              RTS                         
C09A: CC 04 1E        LDD     #$041E                  
C09D: 20 03           BRA     $C0A2                   
C09F: CC 0C 0C        LDD     #$0C0C                  
C0A2: FD 10 34        STD     $1034                   
C0A5: A6 1B           LDA     -5,X                
C0A7: 43              COMA                        
C0A8: B4 10 34        ANDA    $1034                   
C0AB: 44              LSRA                        
C0AC: 44              LSRA                        
C0AD: B7 10 34        STA     $1034                   
C0B0: A6 0A           LDA     10,X                
C0B2: B4 10 35        ANDA    $1035                   
C0B5: BA 10 34        ORA     $1034                   
C0B8: A7 0A           STA     10,X                
C0BA: 39              RTS                         
C0BB: 7F 10 CE        CLR     $10CE                   
C0BE: F6 10 08        LDB     $1008                   
C0C1: F7 10 CF        STB     $10CF                   
C0C4: EC 1E           LDD     -2,X                
C0C6: B3 10 CE        SUBD    $10CE                   
C0C9: 2B 0C           BMI     $C0D7                   
C0CB: 10 83 00 07     CMPD    #$0007                  
C0CF: 25 ; ????
C0D0: 06 10           ROR     $10                   
C0D2: 83 00 FF        SUBD    #$00FF                  
C0D5: 25 ; ????
C0D6: 01 ; ????
C0D7: 5F              CLRB                        
C0D8: E7 0D           STB     13,X                
C0DA: 39              RTS                         
C0DB: BD C7 DD        JSR     $C7DD                   
C0DE: BD C1 9A        JSR     $C19A                   
C0E1: 8E 16 40        LDX     #$1640                  
C0E4: B6 17 44        LDA     $1744                   
C0E7: 20 0C           BRA     $C0F5                   
C0E9: BD C7 D8        JSR     $C7D8                   
C0EC: BD C1 A2        JSR     $C1A2                   
C0EF: 8E 15 80        LDX     #$1580                  
C0F2: B6 17 04        LDA     $1704                   
C0F5: 4A              DECA                        
C0F6: 84 0F           ANDA    #$0F                  
C0F8: BB 17 21        ADDA    $1721                   
C0FB: CE D4 F0        LDU     #$D4F0                  
C0FE: C6 3C           LDB     #$3C                  
C100: F7 10 09        STB     $1009                   
C103: C0 04           SUBB    #$04                  
C105: 3D              MUL                         
C106: 33 CB           LEAU    D,U                 
C108: A6 C0           LDA     ,U+                 
C10A: 1F 89           TFR     A,B                   
C10C: 84 F0           ANDA    #$F0                  
C10E: 44              LSRA                        
C10F: 44              LSRA                        
C110: 44              LSRA                        
C111: 44              LSRA                        
C112: 81 0B           CMPA    #$0B                  
C114: 26 02           BNE     $C118                   
C116: AB 1F           ADDA    -1,X                
C118: A7 80           STA     ,X+                 
C11A: C4 0F           ANDB    #$0F                  
C11C: C1 0B           CMPB    #$0B                  
C11E: 26 02           BNE     $C122                   
C120: EB 1F           ADDB    -1,X                
C122: E7 80           STB     ,X+                 
C124: 7A 10 09        DEC     $1009                   
C127: 26 DF           BNE     $C108                   
C129: 39              RTS                         
C12A: BD 87 06        JSR     $8706                   
C12D: 8E 15 80        LDX     #$1580                  
C130: CE D3 88        LDU     #$D388                  
C133: 10 8E CE 48     LDY     #$CE48                  
C137: B6 80 00        LDA     $8000                   
C13A: A6 80           LDA     ,X+                 
C13C: C6 20           LDB     #$20                  
C13E: 3D              MUL                         
C13F: 31 AB           LEAY    D,Y                 
C141: BF 10 36        STX     $1036                   
C144: AE C4           LDX     ,U                  
C146: FF 10 3A        STU     $103A                   
C149: 8D 1C           BSR     $C167                   
C14B: BE 10 36        LDX     $1036                   
C14E: 8C 15 F8        CMPX    #$15F8                  
C151: 27 07           BEQ     $C15A                   
C153: FE 10 3A        LDU     $103A                   
C156: 33 42           LEAU    2,U                 
C158: 20 D9           BRA     $C133                   
C15A: BD C1 D2        JSR     $C1D2                   
C15D: BD C2 04        JSR     $C204                   
C160: BD C2 66        JSR     $C266                   
C163: BD C8 11        JSR     $C811                   
C166: 39              RTS                         
C167: CE C1 92        LDU     #$C192                  
C16A: FF 10 38        STU     $1038                   
C16D: 8D 0F           BSR     $C17E                   
C16F: FE 10 38        LDU     $1038                   
C172: A6 C0           LDA     ,U+                 
C174: 27 1B           BEQ     $C191                   
C176: AE 9F 10 3A     LDX     [$103A]                 
C17A: 30 86           LEAX    A,X                 
C17C: 20 EC           BRA     $C16A                   
C17E: CE C1 96        LDU     #$C196                  
C181: EC A1           LDD     ,Y++                
C183: A7 84           STA     ,X                  
C185: E7 89 08 00     STB     $0800,X                 
C189: A6 C0           LDA     ,U+                 
C18B: 27 04           BEQ     $C191                   
C18D: 30 86           LEAX    A,X                 
C18F: 20 F0           BRA     $C181                   
C191: 39              RTS                         
C192: 02 ; ????
C193: 40              NEGA                        
C194: 42 ; ????
C195: 00 01           NEG     $01                   
C197: 1F 01           TFR     D,X                   
C199: 00 8E           NEG     $8E                   
C19B: 16 FC B6        LBRA    $BE54                   
C19E: 17 44 20        LBSR    $105C1                   
C1A1: 06 8E           ROR     $8E                   
C1A3: 16 3C B6        LBRA    $FE5C                   
C1A6: 17 04 C6        LBSR    $C66F                   
C1A9: 3C 6F           CWAI    $6F                   
C1AB: 82 5A           SBCA    #$5A                  
C1AD: 26 FB           BNE     $C1AA                   
C1AF: 4A              DECA                        
C1B0: 84 0F           ANDA    #$0F                  
C1B2: BB 17 21        ADDA    $1721                   
C1B5: CE DB F4        LDU     #$DBF4                  
C1B8: C6 0C           LDB     #$0C                  
C1BA: 3D              MUL                         
C1BB: 33 CB           LEAU    D,U                 
C1BD: C6 0C           LDB     #$0C                  
C1BF: F7 10 09        STB     $1009                   
C1C2: 86 05           LDA     #$05                  
C1C4: E6 C0           LDB     ,U+                 
C1C6: 59              ROLB                        
C1C7: 69 80           ROL     ,X+                 
C1C9: 4A              DECA                        
C1CA: 26 FA           BNE     $C1C6                   
C1CC: 7A 10 09        DEC     $1009                   
C1CF: 26 F1           BNE     $C1C2                   
C1D1: 39              RTS                         
C1D2: 8E 16 00        LDX     #$1600                  
C1D5: CE D4 78        LDU     #$D478                  
C1D8: B6 80 00        LDA     $8000                   
C1DB: A6 80           LDA     ,X+                 
C1DD: 27 15           BEQ     $C1F4                   
C1DF: BF 10 36        STX     $1036                   
C1E2: AE C4           LDX     ,U                  
C1E4: FF 10 38        STU     $1038                   
C1E7: 10 8E C1 FC     LDY     #$C1FC                  
C1EB: BD C1 7E        JSR     $C17E                   
C1EE: BE 10 36        LDX     $1036                   
C1F1: FE 10 38        LDU     $1038                   
C1F4: 33 42           LEAU    2,U                 
C1F6: 8C 16 3C        CMPX    #$163C                  
C1F9: 26 DD           BNE     $C1D8                   
C1FB: 39              RTS                         
C1FC: 10 ; ????
C1FD: 30 14           LEAX    -12,X               
C1FF: 30 1C           LEAX    -4,X                
C201: 30 18           LEAX    -8,X                
C203: 30 ; ????
C204: 8E 15 80        LDX     #$1580                  
C207: CE C2 50        LDU     #$C250                  
C20A: B6 80 00        LDA     $8000                   
C20D: A6 80           LDA     ,X+                 
C20F: 81 09           CMPA    #$09                  
C211: 23 04           BLS     $C217                   
C213: C6 FF           LDB     #$FF                  
C215: 20 02           BRA     $C219                   
C217: E6 C6           LDB     A,U                 
C219: E7 89 FF 7F     STB     $FF7F,X                 
C21D: 8C 15 F8        CMPX    #$15F8                  
C220: 26 E8           BNE     $C20A                   
C222: 8E 15 08        LDX     #$1508                  
C225: A6 80           LDA     ,X+                 
C227: 2B 21           BMI     $C24A                   
C229: CE C2 5A        LDU     #$C25A                  
C22C: A5 42           BITA    2,U                 
C22E: 26 10           BNE     $C240                   
C230: B7 10 34        STA     $1034                   
C233: A6 C4           LDA     ,U                  
C235: E6 86           LDB     A,X                 
C237: B6 10 34        LDA     $1034                   
C23A: E5 41           BITB    1,U                 
C23C: 27 02           BEQ     $C240                   
C23E: AA 42           ORA     2,U                 
C240: 33 43           LEAU    3,U                 
C242: 11 83 C2 66     CMPU    #$C266                  
C246: 26 E4           BNE     $C22C                   
C248: A7 1F           STA     -1,X                
C24A: 8C 15 70        CMPX    #$1570                  
C24D: 26 D6           BNE     $C225                   
C24F: 39              RTS                         
C250: 0C 06           INC     $06                   
C252: 0C 04           INC     $04                   
C254: 04 06           LSR     $06                   
C256: 09 03           ROL     $03                   
C258: 00 00           NEG     $00                   
C25A: FE 04 01        LDU     $0401                   
C25D: F7 08 02        STB     $0802                   
C260: 00 01           NEG     $01                   
C262: 04 07           LSR     $07                   
C264: 02 ; ????
C265: 08 ; ????
C266: 8E 15 89        LDX     #$1589                  
C269: CE D3 9A        LDU     #$D39A                  
C26C: A6 80           LDA     ,X+                 
C26E: 81 0A           CMPA    #$0A                  
C270: 10 27 01 0D     LBEQ    $C381                   
C274: 25 ; ????
C275: 06 E6           ROR     $E6                   
C277: 89 FF           ADCA    #$FF                  
C279: 7E 20 04        JMP     $2004                   
C27C: E6 89 FF 7F     LDB     $FF7F,X                 
C280: 10 8E C3 8B     LDY     #$C38B                  
C284: E4 A6           ANDB    A,Y                 
C286: 10 27 00 F7     LBEQ    $C381                   
C28A: F7 10 CF        STB     $10CF                   
C28D: C4 01           ANDB    #$01                  
C28F: F7 10 EA        STB     $10EA                   
C292: C6 04           LDB     #$04                  
C294: F7 10 09        STB     $1009                   
C297: BF 10 36        STX     $1036                   
C29A: FF 10 38        STU     $1038                   
C29D: CE C3 F4        LDU     #$C3F4                  
C2A0: 10 8E C3 A0     LDY     #$C3A0                  
C2A4: B7 10 35        STA     $1035                   
C2A7: 48 ; ????
C2A8: 48 ; ????
C2A9: 31 A6           LEAY    A,Y                 
C2AB: 76 10 CF        ROR     $10CF                   
C2AE: 10 ; ????
C2AF: 24 ; ????
C2B0: 00 BE           NEG     $BE                   
C2B2: 86 04           LDA     #$04                  
C2B4: B7 10 CE        STA     $10CE                   
C2B7: AE 9F 10 38     LDX     [$1038]                 
C2BB: EC C1           LDD     ,U++                
C2BD: FD 10 3C        STD     $103C                   
C2C0: A6 A0           LDA     ,Y+                 
C2C2: E6 C0           LDB     ,U+                 
C2C4: 30 85           LEAX    B,X                 
C2C6: 46              RORA                        
C2C7: 10 ; ????
C2C8: 24 ; ????
C2C9: 00 9C           NEG     $9C                   
C2CB: B7 10 34        STA     $1034                   
C2CE: A6 84           LDA     ,X                  
C2D0: 2B 20           BMI     $C2F2                   
C2D2: E6 89 08 00     LDB     $0800,X                 
C2D6: C4 0F           ANDB    #$0F                  
C2D8: FA 10 3D        ORB     $103D                   
C2DB: C5 04           BITB    #$04                  
C2DD: 27 0C           BEQ     $C2EB                   
C2DF: C5 0A           BITB    #$0A                  
C2E1: 27 08           BEQ     $C2EB                   
C2E3: 8B 1F           ADDA    #$1F                  
C2E5: A7 84           STA     ,X                  
C2E7: C4 0F           ANDB    #$0F                  
C2E9: 20 75           BRA     $C360                   
C2EB: BB 10 3C        ADDA    $103C                   
C2EE: A7 84           STA     ,X                  
C2F0: 20 4E           BRA     $C340                   
C2F2: FF 10 3A        STU     $103A                   
C2F5: CE C4 0C        LDU     #$C40C                  
C2F8: F6 10 35        LDB     $1035                   
C2FB: 33 C5           LEAU    B,U                 
C2FD: E6 C4           LDB     ,U                  
C2FF: CE C4 21        LDU     #$C421                  
C302: 33 C5           LEAU    B,U                 
C304: A1 C0           CMPA    ,U+                 
C306: 27 08           BEQ     $C310                   
C308: 11 83 C4 40     CMPU    #$C440                  
C30C: 26 F6           BNE     $C304                   
C30E: 33 41           LEAU    1,U                 
C310: F6 10 09        LDB     $1009                   
C313: C5 01           BITB    #$01                  
C315: 27 21           BEQ     $C338                   
C317: C5 02           BITB    #$02                  
C319: 27 0B           BEQ     $C326                   
C31B: E6 88 E0        LDB     $E0,X                 
C31E: 81 A7           CMPA    #$A7                  
C320: 26 0F           BNE     $C331                   
C322: C6 25           LDB     #$25                  
C324: 20 15           BRA     $C33B                   
C326: E6 88 20        LDB     $20,X                 
C329: 81 A4           CMPA    #$A4                  
C32B: 26 04           BNE     $C331                   
C32D: C6 25           LDB     #$25                  
C32F: 20 0A           BRA     $C33B                   
C331: C1 FC           CMPB    #$FC                  
C333: 24 ; ????
C334: 03 33           COM     $33                   
C336: C8 20           EORB    #$20                  
C338: E6 C8 1E        LDB     $1E,U                 
C33B: FE 10 3A        LDU     $103A                   
C33E: 20 20           BRA     $C360                   
C340: B6 10 EA        LDA     $10EA                   
C343: 26 1B           BNE     $C360                   
C345: B6 10 09        LDA     $1009                   
C348: 85 01           BITA    #$01                  
C34A: 27 14           BEQ     $C360                   
C34C: 85 02           BITA    #$02                  
C34E: 27 05           BEQ     $C355                   
C350: A6 88 E0        LDA     $E0,X                 
C353: 20 03           BRA     $C358                   
C355: A6 88 20        LDA     $20,X                 
C358: 81 FC           CMPA    #$FC                  
C35A: 24 ; ????
C35B: 04 C4           LSR     $C4                   
C35D: 0F CA           CLR     $CA                   
C35F: 10 ; ????
C360: E7 89 08 00     STB     $0800,X                 
C364: B6 10 34        LDA     $1034                   
C367: 7A 10 CE        DEC     $10CE                   
C36A: 10 26 FF 54     LBNE    $C2C2                   
C36E: 20 04           BRA     $C374                   
C370: 33 46           LEAU    6,U                 
C372: 31 21           LEAY    1,Y                 
C374: 7A 10 09        DEC     $1009                   
C377: 10 26 FF 30     LBNE    $C2AB                   
C37B: BE 10 36        LDX     $1036                   
C37E: FE 10 38        LDU     $1038                   
C381: 33 42           LEAU    2,U                 
C383: 8C 15 F0        CMPX    #$15F0                  
C386: 10 26 FE E2     LBNE    $C26C                   
C38A: 39              RTS                         
C38B: 03 09           COM     $09                   
C38D: 0B ; ????
C38E: 0B ; ????
C38F: 0B ; ????
C390: 0B ; ????
C391: 06 0C           ROR     $0C                   
C393: 0F 0F           CLR     $0F                   
C395: 00 02           NEG     $02                   
C397: 08 ; ????
C398: 02 ; ????
C399: 0A 0A           DEC     $0A                   
C39B: 08 ; ????
C39C: 0A 0A           DEC     $0A                   
C39E: 0A 0A           DEC     $0A                   
C3A0: 0F 0F           CLR     $0F                   
C3A2: 00 00           NEG     $00                   
C3A4: 0F 00           CLR     $00                   
C3A6: 00 0F           NEG     $0F                   
C3A8: 0F 0F           CLR     $0F                   
C3AA: 00 03           NEG     $03                   
C3AC: 0F 0F           CLR     $0F                   
C3AE: 00 0F           NEG     $0F                   
C3B0: 0F 0F           CLR     $0F                   
C3B2: 00 0F           NEG     $0F                   
C3B4: 0F 01           CLR     $01                   
C3B6: 00 07           NEG     $07                   
C3B8: 00 0F           NEG     $0F                   
C3BA: 0F 00           CLR     $00                   
C3BC: 00 00           NEG     $00                   
C3BE: 0F 0F           CLR     $0F                   
C3C0: 0F 0F           CLR     $0F                   
C3C2: 0F 0F           CLR     $0F                   
C3C4: 0F 0F           CLR     $0F                   
C3C6: 0F 0F           CLR     $0F                   
C3C8: 00 00           NEG     $00                   
C3CA: 00 00           NEG     $00                   
C3CC: 00 02           NEG     $02                   
C3CE: 00 00           NEG     $00                   
C3D0: 00 00           NEG     $00                   
C3D2: 00 03           NEG     $03                   
C3D4: 00 01           NEG     $01                   
C3D6: 00 00           NEG     $00                   
C3D8: 00 03           NEG     $03                   
C3DA: 00 01           NEG     $01                   
C3DC: 00 01           NEG     $01                   
C3DE: 00 03           NEG     $03                   
C3E0: 00 00           NEG     $00                   
C3E2: 00 01           NEG     $01                   
C3E4: 00 03           NEG     $03                   
C3E6: 00 03           NEG     $03                   
C3E8: 00 03           NEG     $03                   
C3EA: 00 03           NEG     $03                   
C3EC: 00 03           NEG     $03                   
C3EE: 00 03           NEG     $03                   
C3F0: 00 03           NEG     $03                   
C3F2: 00 03           NEG     $03                   
C3F4: 02 ; ????
C3F5: 21 60           BRN     $C457                   
C3F7: E0 E0           SUBB    ,S+                 
C3F9: E0 01           SUBB    1,X                 
C3FB: 22 00           BHI     $C3FD                   
C3FD: 01 ; ????
C3FE: 01 ; ????
C3FF: 01 ; ????
C400: 02 ; ????
C401: 24 ; ????
C402: 63 E0           COM     ,S+                 
C404: E0 E0           SUBB    ,S+                 
C406: 01 ; ????
C407: 28 60           BVC     $C469                   
C409: 01 ; ????
C40A: 01 ; ????
C40B: 01 ; ????
C40C: 00 02           NEG     $02                   
C40E: 05 ; ????
C40F: 09 0D           ROL     $0D                   
C411: 11 ; ????
C412: 1B ; ????
C413: 1D              SEX                         
C414: 00 00           NEG     $00                   
C416: 00 01           NEG     $01                   
C418: 03 08           COM     $08                   
C41A: 0A 0E           DEC     $0E                   
C41C: 12              NOP                         
C41D: 13              SYNC                        
C41E: 17 13 17        LBSR    $D738                   
C421: AD ; ????
C422: C7 ; ????
C423: D3 C9           ADDD    $C9                   
C425: CA 8C           ORB     #$8C                  
C427: 87 ; ????
C428: 8B E7           ADDA    #$E7                  
C42A: EA ; ????
C42B: EE A8 E9        LDU     $E9,Y                 
C42E: 84 D9           ANDA    #$D9                  
C430: D4 D5           ANDB    $D5                   
C432: 83 E2 A1        SUBD    #$E2A1                  
C435: A5 A0           BITA    ,Y+                 
C437: A2 A8 AC        SBCA    $AC,Y                 
C43A: A6 A9 B0 B5     LDA     $B0B5,Y                 
C43E: B8 BC 1A        EORA    $BC1A                   
C441: 36 1A           PSHU    X,DP,A                   
C443: 3D              MUL                         
C444: 3D              MUL                         
C445: 3C 3C           CWAI    $3C                   
C447: 36 36           PSHU    Y,X,B,A                   
C449: 36 3D           PSHU    Y,X,DP,B,CC                   
C44B: 31 36           LEAY    -10,Y               
C44D: 36 36           PSHU    Y,X,B,A                   
C44F: 1A 3D           ORCC    #$3D                  
C451: 3D              MUL                         
C452: 31 31           LEAY    -15,Y               
C454: 36 31           PSHU    Y,X,CC                   
C456: 36 31           PSHU    Y,X,CC                   
C458: 36 36           PSHU    Y,X,B,A                   
C45A: 36 29           PSHU    Y,DP,CC                   
C45C: 28 29           BVC     $C487                   
C45E: 28 09           BVC     $C469                   
C460: 1B ; ????
C461: 35 1B           PULS    CC,A,DP,X                   
C463: 2A 2A           BPL     $C48F                   
C465: 3A              ABX                         
C466: 3A              ABX                         
C467: 35 35           PULS    CC,B,X,Y                   
C469: 35 2A           PULS    A,DP,Y                   
C46B: 34 35           PSHS    Y,X,B,CC                   
C46D: 35 35           PULS    CC,B,X,Y                   
C46F: 1B ; ????
C470: 35 2A           PULS    A,DP,Y                   
C472: 34 34           PSHS    Y,X,B                   
C474: 35 34           PULS    B,X,Y                   
C476: 35 34           PULS    B,X,Y                   
C478: 35 34           PULS    B,X,Y                   
C47A: 35 28           PULS    DP,Y                   
C47C: 28 2C           BVC     $C4AA                   
C47E: 28 17           BVC     $C497                   
C480: EC 1E           LDD     -2,X                
C482: 10 83 00 80     CMPD    #$0080                  
C486: 2F 11           BLE     $C499                   
C488: 10 83 01 7F     CMPD    #$017F                  
C48C: 2C 11           BGE     $C49F                   
C48E: 83 00 80        SUBD    #$0080                  
C491: F7 10 08        STB     $1008                   
C494: 86 80           LDA     #$80                  
C496: A7 0D           STA     13,X                
C498: 39              RTS                         
C499: E7 0D           STB     13,X                
C49B: 7F 10 08        CLR     $1008                   
C49E: 39              RTS                         
C49F: 5C              INCB                        
C4A0: E7 0D           STB     13,X                
C4A2: 86 FF           LDA     #$FF                  
C4A4: B7 10 08        STA     $1008                   
C4A7: 39              RTS                         
C4A8: 8E 17 00        LDX     #$1700                  
C4AB: 6F 88 21        CLR     $21,X                 
C4AE: A6 05           LDA     5,X                 
C4B0: 81 15           CMPA    #$15                  
C4B2: 23 0E           BLS     $C4C2                   
C4B4: 81 99           CMPA    #$99                  
C4B6: 27 07           BEQ     $C4BF                   
C4B8: C6 10           LDB     #$10                  
C4BA: E7 88 21        STB     $21,X                 
C4BD: 20 03           BRA     $C4C2                   
C4BF: 4F              CLRA                        
C4C0: A7 04           STA     4,X                 
C4C2: 8B 01           ADDA    #$01                  
C4C4: 19              DAA                         
C4C5: A7 05           STA     5,X                 
C4C7: A6 04           LDA     4,X                 
C4C9: 84 0F           ANDA    #$0F                  
C4CB: 4C              INCA                        
C4CC: 6C 04           INC     4,X                 
C4CE: AB 88 21        ADDA    $21,X                 
C4D1: CE DD 5B        LDU     #$DD5B                  
C4D4: C6 19           LDB     #$19                  
C4D6: 3D              MUL                         
C4D7: 33 CB           LEAU    D,U                 
C4D9: 30 07           LEAX    7,X                 
C4DB: 86 18           LDA     #$18                  
C4DD: E6 C0           LDB     ,U+                 
C4DF: E7 80           STB     ,X+                 
C4E1: 4A              DECA                        
C4E2: 26 F9           BNE     $C4DD                   
C4E4: A6 C4           LDA     ,U                  
C4E6: A7 80           STA     ,X+                 
C4E8: 86 03           LDA     #$03                  
C4EA: A7 84           STA     ,X                  
C4EC: B6 10 10        LDA     $1010                   
C4EF: 10 27 FB F6     LBEQ    $C0E9                   
C4F3: 39              RTS                         
C4F4: 7F 10 D3        CLR     $10D3                   
C4F7: A6 14           LDA     -12,X               
C4F9: 48 ; ????
C4FA: 10 8E C5 2A     LDY     #$C52A                  
C4FE: 31 A6           LEAY    A,Y                 
C500: A6 4F           LDA     15,U                
C502: A0 0F           SUBA    15,X                
C504: 2A 02           BPL     $C508                   
C506: 43              COMA                        
C507: 4C              INCA                        
C508: A1 A4           CMPA    ,Y                  
C50A: 22 1D           BHI     $C529                   
C50C: EC 5E           LDD     -2,U                
C50E: A3 1E           SUBD    -2,X                
C510: 2A 05           BPL     $C517                   
C512: 43              COMA                        
C513: 53              COMB                        
C514: C3 00 01        ADDD    #$0001                  
C517: E1 21           CMPB    1,Y                 
C519: 22 0E           BHI     $C529                   
C51B: 8C 24 D0        CMPX    #$24D0                  
C51E: 26 04           BNE     $C524                   
C520: 7C 10 D3        INC     $10D3                   
C523: 39              RTS                         
C524: 86 01           LDA     #$01                  
C526: B7 10 D3        STA     $10D3                   
C529: 39              RTS                         
C52A: 04 04           LSR     $04                   
C52C: 0A 12           DEC     $12                   
C52E: 08 ; ????
C52F: 04 06           LSR     $06                   
C531: 06 04           ROR     $04                   
C533: 08 ; ????
C534: EC 1E           LDD     -2,X                
C536: 83 00 18        SUBD    #$0018                  
C539: C4 F8           ANDB    #$F8                  
C53B: 58 ; ????
C53C: 49              ROLA                        
C53D: 58 ; ????
C53E: 49              ROLA                        
C53F: FD 10 CE        STD     $10CE                   
C542: E6 0F           LDB     15,X                
C544: 54              LSRB                        
C545: 54              LSRB                        
C546: 54              LSRB                        
C547: 4F              CLRA                        
C548: F3 10 CE        ADDD    $10CE                   
C54B: 27 1A           BEQ     $C567                   
C54D: 10 83 07 80     CMPD    #$0780                  
C551: 24 ; ????
C552: 14 ; ????
C553: 10 8E C5 6B     LDY     #$C56B                  
C557: 1F 03           TFR     D,U                   
C559: F6 10 C0        LDB     $10C0                   
C55C: A6 A5           LDA     B,Y                 
C55E: 33 C6           LEAU    A,U                 
C560: A6 C4           LDA     ,U                  
C562: E6 C9 08 00     LDB     $0800,U                 
C566: 39              RTS                         
C567: CC FF FF        LDD     #$FFFF                  
C56A: 39              RTS                         
C56B: 1D              SEX                         
C56C: FF DF 00        STU     $DF00                   
C56F: 20 1E           BRA     $C58F                   
C571: 5F              CLRB                        
C572: FE 21 8E        LDU     $218E                   
C575: 14 ; ????
C576: 80 4F           SUBA    #$4F                  
C578: E6 89 00 80     LDB     $0080,X                 
C57C: 2A 07           BPL     $C585                   
C57E: C5 10           BITB    #$10                  
C580: 26 04           BNE     $C586                   
C582: 4C              INCA                        
C583: 20 01           BRA     $C586                   
C585: 5F              CLRB                        
C586: E7 80           STB     ,X+                 
C588: 8C 14 F8        CMPX    #$14F8                  
C58B: 26 EB           BNE     $C578                   
C58D: 4D              TSTA                        
C58E: 10 26 01 36     LBNE    $C6C8                   
C592: 8E C7 50        LDX     #$C750                  
C595: CE 14 80        LDU     #$1480                  
C598: F6 10 40        LDB     $1040                   
C59B: 3A              ABX                         
C59C: 86 FE           LDA     #$FE                  
C59E: E6 80           LDB     ,X+                 
C5A0: FB 10 C1        ADDB    $10C1                   
C5A3: F7 10 47        STB     $1047                   
C5A6: 6C C5           INC     B,U                 
C5A8: EB 84           ADDB    ,X                  
C5AA: A7 C5           STA     B,U                 
C5AC: 8E 15 00        LDX     #$1500                  
C5AF: F6 10 47        LDB     $1047                   
C5B2: A6 85           LDA     B,X                 
C5B4: 8E C7 58        LDX     #$C758                  
C5B7: F6 10 40        LDB     $1040                   
C5BA: 58 ; ????
C5BB: 58 ; ????
C5BC: 58 ; ????
C5BD: 3A              ABX                         
C5BE: E6 86           LDB     A,X                 
C5C0: F7 10 48        STB     $1048                   
C5C3: AB 0F           ADDA    15,X                
C5C5: E6 86           LDB     A,X                 
C5C7: F7 10 40        STB     $1040                   
C5CA: 10 8E 15 00     LDY     #$1500                  
C5CE: B6 10 47        LDA     $1047                   
C5D1: 8E C7 98        LDX     #$C798                  
C5D4: F6 10 40        LDB     $1040                   
C5D7: 58 ; ????
C5D8: 58 ; ????
C5D9: 58 ; ????
C5DA: 3A              ABX                         
C5DB: C6 04           LDB     #$04                  
C5DD: F7 10 09        STB     $1009                   
C5E0: AB 84           ADDA    ,X                  
C5E2: E6 A6           LDB     A,Y                 
C5E4: E4 01           ANDB    1,X                 
C5E6: 26 09           BNE     $C5F1                   
C5E8: 30 03           LEAX    3,X                 
C5EA: 7A 10 09        DEC     $1009                   
C5ED: 26 F1           BNE     $C5E0                   
C5EF: 20 22           BRA     $C613                   
C5F1: E6 02           LDB     2,X                 
C5F3: F7 10 40        STB     $1040                   
C5F6: E6 C6           LDB     A,U                 
C5F8: 2B 15           BMI     $C60F                   
C5FA: 27 0F           BEQ     $C60B                   
C5FC: B1 10 47        CMPA    $1047                   
C5FF: 26 D0           BNE     $C5D1                   
C601: F6 10 40        LDB     $1040                   
C604: F1 10 48        CMPB    $1048                   
C607: 26 C8           BNE     $C5D1                   
C609: 20 09           BRA     $C614                   
C60B: 6C C6           INC     A,U                 
C60D: 20 C2           BRA     $C5D1                   
C60F: C5 01           BITB    #$01                  
C611: 27 00           BEQ     $C613                   
C613: 39              RTS                         
C614: 7F 10 09        CLR     $1009                   
C617: 8E 14 88        LDX     #$1488                  
C61A: A6 84           LDA     ,X                  
C61C: 26 14           BNE     $C632                   
C61E: CE C7 A4        LDU     #$C7A4                  
C621: E6 C0           LDB     ,U+                 
C623: 27 0D           BEQ     $C632                   
C625: A6 85           LDA     B,X                 
C627: 2C F8           BGE     $C621                   
C629: 85 01           BITA    #$01                  
C62B: 26 F4           BNE     $C621                   
C62D: A7 84           STA     ,X                  
C62F: 7C 10 09        INC     $1009                   
C632: 30 01           LEAX    1,X                 
C634: 8C 14 F0        CMPX    #$14F0                  
C637: 26 E1           BNE     $C61A                   
C639: A6 82           LDA     ,-X                 
C63B: 26 14           BNE     $C651                   
C63D: CE C7 A4        LDU     #$C7A4                  
C640: E6 C0           LDB     ,U+                 
C642: 27 0D           BEQ     $C651                   
C644: A6 85           LDA     B,X                 
C646: 2C F8           BGE     $C640                   
C648: 85 01           BITA    #$01                  
C64A: 26 F4           BNE     $C640                   
C64C: A7 84           STA     ,X                  
C64E: 7C 10 09        INC     $1009                   
C651: 8C 14 88        CMPX    #$1488                  
C654: 26 E3           BNE     $C639                   
C656: B6 10 09        LDA     $1009                   
C659: 26 B9           BNE     $C614                   
C65B: 7F 10 09        CLR     $1009                   
C65E: A6 84           LDA     ,X                  
C660: 26 10           BNE     $C672                   
C662: CE C7 A4        LDU     #$C7A4                  
C665: E6 C0           LDB     ,U+                 
C667: 27 09           BEQ     $C672                   
C669: A6 85           LDA     B,X                 
C66B: 2F F8           BLE     $C665                   
C66D: A7 84           STA     ,X                  
C66F: 7C 10 09        INC     $1009                   
C672: 30 01           LEAX    1,X                 
C674: 8C 14 F0        CMPX    #$14F0                  
C677: 26 E5           BNE     $C65E                   
C679: A6 82           LDA     ,-X                 
C67B: 26 10           BNE     $C68D                   
C67D: CE C7 A4        LDU     #$C7A4                  
C680: E6 C0           LDB     ,U+                 
C682: 27 09           BEQ     $C68D                   
C684: A6 85           LDA     B,X                 
C686: 2F F8           BLE     $C680                   
C688: A7 84           STA     ,X                  
C68A: 7C 10 09        INC     $1009                   
C68D: 8C 14 88        CMPX    #$1488                  
C690: 26 E7           BNE     $C679                   
C692: B6 10 09        LDA     $1009                   
C695: 26 C4           BNE     $C65B                   
C697: 4F              CLRA                        
C698: E6 80           LDB     ,X+                 
C69A: 2B 01           BMI     $C69D                   
C69C: 4C              INCA                        
C69D: 8C 14 F0        CMPX    #$14F0                  
C6A0: 26 F6           BNE     $C698                   
C6A2: B7 10 34        STA     $1034                   
C6A5: 4F              CLRA                        
C6A6: E6 82           LDB     ,-X                 
C6A8: C5 01           BITB    #$01                  
C6AA: 26 01           BNE     $C6AD                   
C6AC: 4C              INCA                        
C6AD: 8C 14 88        CMPX    #$1488                  
C6B0: 26 F4           BNE     $C6A6                   
C6B2: 8E 14 F8        LDX     #$14F8                  
C6B5: B1 10 34        CMPA    $1034                   
C6B8: 25 ; ????
C6B9: 0E A6           JMP     $A6                   
C6BB: 82 43           SBCA    #$43                  
C6BD: 84 80           ANDA    #$80                  
C6BF: A7 84           STA     ,X                  
C6C1: 8C 14 80        CMPX    #$1480                  
C6C4: 26 F4           BNE     $C6BA                   
C6C6: 20 0C           BRA     $C6D4                   
C6C8: A6 82           LDA     ,-X                 
C6CA: 4C              INCA                        
C6CB: 84 80           ANDA    #$80                  
C6CD: A7 84           STA     ,X                  
C6CF: 8C 14 80        CMPX    #$1480                  
C6D2: 26 F4           BNE     $C6C8                   
C6D4: 7F 10 09        CLR     $1009                   
C6D7: B6 10 5D        LDA     $105D                   
C6DA: 26 05           BNE     $C6E1                   
C6DC: 86 04           LDA     #$04                  
C6DE: B7 10 5D        STA     $105D                   
C6E1: 8E 14 89        LDX     #$1489                  
C6E4: 86 06           LDA     #$06                  
C6E6: E6 80           LDB     ,X+                 
C6E8: 27 35           BEQ     $C71F                   
C6EA: B7 10 34        STA     $1034                   
C6ED: CC 00 FF        LDD     #$00FF                  
C6F0: E7 88 7F        STB     $7F,X                 
C6F3: E6 86           LDB     A,X                 
C6F5: 27 06           BEQ     $C6FD                   
C6F7: 4C              INCA                        
C6F8: B1 10 34        CMPA    $1034                   
C6FB: 26 F6           BNE     $C6F3                   
C6FD: 48 ; ????
C6FE: 4C              INCA                        
C6FF: 48 ; ????
C700: 48 ; ????
C701: 48 ; ????
C702: A7 89 FF 7F     STA     $FF7F,X                 
C706: B6 10 5D        LDA     $105D                   
C709: A7 89 FD FF     STA     $FDFF,X                 
C70D: 7C 10 09        INC     $1009                   
C710: E6 89 01 00     LDB     $0100,X                 
C714: C1 0A           CMPB    #$0A                  
C716: 23 04           BLS     $C71C                   
C718: A7 89 FE 00     STA     $FE00,X                 
C71C: B6 10 34        LDA     $1034                   
C71F: 4A              DECA                        
C720: 26 C4           BNE     $C6E6                   
C722: 30 02           LEAX    2,X                 
C724: 8C 14 F1        CMPX    #$14F1                  
C727: 26 BB           BNE     $C6E4                   
C729: CE 12 F7        LDU     #$12F7                  
C72C: B6 10 09        LDA     $1009                   
C72F: F6 10 5D        LDB     $105D                   
C732: A7 C5           STA     B,U                 
C734: 7A 10 5D        DEC     $105D                   
C737: CC 00 10        LDD     #$0010                  
C73A: BD 8A DB        JSR     $8ADB                   
C73D: CC 01 08        LDD     #$0108                  
C740: B7 10 D7        STA     $10D7                   
C743: 7A 17 20        DEC     $1720                   
C746: 27 01           BEQ     $C749                   
C748: 39              RTS                         
C749: B7 1F 60        STA     $1F60                   
C74C: F7 1F 74        STB     $1F74                   
C74F: 39              RTS                         
C750: 00 08           NEG     $08                   
C752: 01 ; ????
C753: FF 09 F8        STU     $09F8                   
C756: 08 ; ????
C757: 01 ; ????
C758: FF 00 02        STU     $0002                   
C75B: 00 04           NEG     $04                   
C75D: 00 02           NEG     $02                   
C75F: 00 00           NEG     $00                   
C761: 00 00           NEG     $00                   
C763: 00 06           NEG     $06                   
C765: 06 04           ROR     $04                   
C767: F9 FF 02        ADCB    $FF02                   
C76A: 02 ; ????
C76B: 02 ; ????
C76C: 04 02           LSR     $02                   
C76E: 02 ; ????
C76F: 02 ; ????
C770: 06 00           ROR     $00                   
C772: 02 ; ????
C773: 00 04           NEG     $04                   
C775: 06 02           ROR     $02                   
C777: 01 ; ????
C778: 04 04           LSR     $04                   
C77A: 04 02           LSR     $02                   
C77C: 06 06           ROR     $06                   
C77E: 04 02           LSR     $02                   
C780: 04 04           LSR     $04                   
C782: 04 00           LSR     $00                   
C784: 00 FF           NEG     $FF                   
C786: 04 FE           LSR     $FE                   
C788: 06 06           ROR     $06                   
C78A: 06 06           ROR     $06                   
C78C: 06 06           ROR     $06                   
C78E: 04 02           LSR     $02                   
C790: 00 02           NEG     $02                   
C792: 00 FF           NEG     $FF                   
C794: 06 06           ROR     $06                   
C796: 04 FC           LSR     $FC                   
C798: 00 01           NEG     $01                   
C79A: 02 ; ????
C79B: FF 08 00        STU     $0800                   
C79E: 08 ; ????
C79F: 04 06           LSR     $06                   
C7A1: 01 ; ????
C7A2: 02 ; ????
C7A3: 04 FF           LSR     $FF                   
C7A5: F8 01 08        EORB    $0108                   
C7A8: 00 02           NEG     $02                   
C7AA: 04 F8           LSR     $F8                   
C7AC: 01 ; ????
C7AD: 02 ; ????
C7AE: FF 08 00        STU     $0800                   
C7B1: 08 ; ????
C7B2: 04 06           LSR     $06                   
C7B4: 04 08           LSR     $08                   
C7B6: 02 ; ????
C7B7: 01 ; ????
C7B8: 00 04           NEG     $04                   
C7BA: 06 01           ROR     $01                   
C7BC: 02 ; ????
C7BD: 04 F8           LSR     $F8                   
C7BF: 01 ; ????
C7C0: 02 ; ????
C7C1: FF 08 00        STU     $0800                   
C7C4: FF FF FF        STU     $FFFF                   
C7C7: FF 00 08        STU     $0008                   
C7CA: 00 08           NEG     $08                   
C7CC: 04 06           LSR     $06                   
C7CE: 01 ; ????
C7CF: 02 ; ????
C7D0: 04 F8           LSR     $F8                   
C7D2: 01 ; ????
C7D3: 02 ; ????
C7D4: FF FF FF        STU     $FFFF                   
C7D7: FF 8E 13        STU     $8E13                   
C7DA: 00 20           NEG     $20                   
C7DC: 03 8E           COM     $8E                   
C7DE: 13              SYNC                        
C7DF: 80 BF           SUBA    #$BF                  
C7E1: 10 ; ????
C7E2: 36 CC           PSHU    PC,S,DP,B                   
C7E4: 00 78           NEG     $78                   
C7E6: A7 80           STA     ,X+                 
C7E8: 5A              DECB                        
C7E9: 26 FB           BNE     $C7E6                   
C7EB: 8E E0 94        LDX     #$E094                  
C7EE: F6 17 04        LDB     $1704                   
C7F1: 5A              DECB                        
C7F2: C4 0F           ANDB    #$0F                  
C7F4: FB 17 21        ADDB    $1721                   
C7F7: 58 ; ????
C7F8: 3A              ABX                         
C7F9: EE 84           LDU     ,X                  
C7FB: A6 C0           LDA     ,U+                 
C7FD: 26 01           BNE     $C800                   
C7FF: 39              RTS                         
C800: B7 10 09        STA     $1009                   
C803: BE 10 36        LDX     $1036                   
C806: EC C1           LDD     ,U++                
C808: 3A              ABX                         
C809: A7 84           STA     ,X                  
C80B: 7A 10 09        DEC     $1009                   
C80E: 26 F3           BNE     $C803                   
C810: 39              RTS                         
C811: 8E 15 00        LDX     #$1500                  
C814: 10 8E D3 88     LDY     #$D388                  
C818: A6 80           LDA     ,X+                 
C81A: AA 89 FD FF     ORA     $FDFF,X                 
C81E: A0 1F           SUBA    -1,X                
C820: A7 89 FD FF     STA     $FDFF,X                 
C824: 26 09           BNE     $C82F                   
C826: 31 22           LEAY    2,Y                 
C828: 10 8C D4 78     CMPY    #$D478                  
C82C: 26 EA           BNE     $C818                   
C82E: 39              RTS                         
C82F: B7 10 CE        STA     $10CE                   
C832: AA 1F           ORA     -1,X                
C834: A7 1F           STA     -1,X                
C836: C6 04           LDB     #$04                  
C838: F7 10 CF        STB     $10CF                   
C83B: BF 10 36        STX     $1036                   
C83E: CE C8 D2        LDU     #$C8D2                  
C841: 76 10 CE        ROR     $10CE                   
C844: 24 ; ????
C845: 75 ; ????
C846: EC 44           LDD     4,U                 
C848: B7 10 3C        STA     $103C                   
C84B: F7 10 40        STB     $1040                   
C84E: 86 04           LDA     #$04                  
C850: B7 10 09        STA     $1009                   
C853: AE A4           LDX     ,Y                  
C855: E6 C0           LDB     ,U+                 
C857: 3A              ABX                         
C858: A6 84           LDA     ,X                  
C85A: 2B 3C           BMI     $C898                   
C85C: E6 89 08 00     LDB     $0800,X                 
C860: C1 30           CMPB    #$30                  
C862: 26 07           BNE     $C86B                   
C864: BB 10 3C        ADDA    $103C                   
C867: A7 84           STA     ,X                  
C869: 20 49           BRA     $C8B4                   
C86B: C1 1F           CMPB    #$1F                  
C86D: 23 1B           BLS     $C88A                   
C86F: C5 04           BITB    #$04                  
C871: 27 04           BEQ     $C877                   
C873: C4 0F           ANDB    #$0F                  
C875: 20 13           BRA     $C88A                   
C877: 81 65           CMPA    #$65                  
C879: 26 04           BNE     $C87F                   
C87B: 8B 21           ADDA    #$21                  
C87D: 20 07           BRA     $C886                   
C87F: 81 66           CMPA    #$66                  
C881: 26 01           BNE     $C884                   
C883: 4A              DECA                        
C884: 8B 20           ADDA    #$20                  
C886: C4 0F           ANDB    #$0F                  
C888: 20 03           BRA     $C88D                   
C88A: BB 10 3C        ADDA    $103C                   
C88D: A7 84           STA     ,X                  
C88F: FA 10 40        ORB     $1040                   
C892: E7 89 08 00     STB     $0800,X                 
C896: 20 1C           BRA     $C8B4                   
C898: FF 10 38        STU     $1038                   
C89B: CE C4 21        LDU     #$C421                  
C89E: A1 C0           CMPA    ,U+                 
C8A0: 27 08           BEQ     $C8AA                   
C8A2: 11 83 C4 40     CMPU    #$C440                  
C8A6: 26 F6           BNE     $C89E                   
C8A8: 33 41           LEAU    1,U                 
C8AA: E6 C8 3E        LDB     $3E,U                 
C8AD: E7 89 08 00     STB     $0800,X                 
C8B1: FE 10 38        LDU     $1038                   
C8B4: 7A 10 09        DEC     $1009                   
C8B7: 26 9C           BNE     $C855                   
C8B9: 33 5C           LEAU    -4,U                
C8BB: 33 46           LEAU    6,U                 
C8BD: 7A 10 CF        DEC     $10CF                   
C8C0: 10 26 FF 7D     LBNE    $C841                   
C8C4: BE 10 36        LDX     $1036                   
C8C7: 31 22           LEAY    2,Y                 
C8C9: 10 8C D4 78     CMPY    #$D478                  
C8CD: 10 26 FF 47     LBNE    $C818                   
C8D1: 39              RTS                         
C8D2: 00 20           NEG     $20                   
C8D4: 20 20           BRA     $C8F6                   
C8D6: 02 ; ????
C8D7: 01 ; ????
C8D8: 00 01           NEG     $01                   
C8DA: 01 ; ????
C8DB: 01 ; ????
C8DC: 01 ; ????
C8DD: 02 ; ????
C8DE: 03 20           COM     $20                   
C8E0: 20 20           BRA     $C902                   
C8E2: 02 ; ????
C8E3: 04 60           LSR     $60                   
C8E5: 01 ; ????
C8E6: 01 ; ????
C8E7: 01 ; ????
C8E8: 01 ; ????
C8E9: 08 ; ????
C8EA: B6 17 0C        LDA     $170C                   
C8ED: 20 04           BRA     $C8F3                   
C8EF: A6 5F           LDA     -1,U                
C8F1: 84 7F           ANDA    #$7F                  
C8F3: CE 15 80        LDU     #$1580                  
C8F6: E6 C6           LDB     A,U                 
C8F8: C1 09           CMPB    #$09                  
C8FA: 23 0B           BLS     $C907                   
C8FC: BD 8A A0        JSR     $8AA0                   
C8FF: 84 7F           ANDA    #$7F                  
C901: 81 78           CMPA    #$78                  
C903: 25 ; ????
C904: F1 20 F5        CMPB    $20F5                   
C907: E6 19           LDB     -7,X                
C909: 26 05           BNE     $C910                   
C90B: B7 17 0C        STA     $170C                   
C90E: 20 1E           BRA     $C92E                   
C910: B1 17 0C        CMPA    $170C                   
C913: 26 05           BNE     $C91A                   
C915: 7D 10 69        TST     $1069                   
C918: 27 E2           BEQ     $C8FC                   
C91A: CE 17 0C        LDU     #$170C                  
C91D: B7 10 34        STA     $1034                   
C920: A6 19           LDA     -7,X                
C922: 84 80           ANDA    #$80                  
C924: BA 10 34        ORA     $1034                   
C927: C4 0F           ANDB    #$0F                  
C929: A7 C5           STA     B,U                 
C92B: B6 10 34        LDA     $1034                   
C92E: 1F 89           TFR     A,B                   
C930: 84 07           ANDA    #$07                  
C932: 48 ; ????
C933: 48 ; ????
C934: 48 ; ????
C935: 48 ; ????
C936: 48 ; ????
C937: 8B 10           ADDA    #$10                  
C939: BB 10 69        ADDA    $1069                   
C93C: A7 0F           STA     15,X                
C93E: C4 78           ANDB    #$78                  
C940: 86 04           LDA     #$04                  
C942: 3D              MUL                         
C943: C3 00 20        ADDD    #$0020                  
C946: ED 1E           STD     -2,X                
C948: B6 80 00        LDA     $8000                   
C94B: 39              RTS                         
C94C: B7 10 C0        STA     $10C0                   
C94F: 84 02           ANDA    #$02                  
C951: B7 10 09        STA     $1009                   
C954: BD C5 34        JSR     $C534                   
C957: 81 70           CMPA    #$70                  
C959: 24 ; ????
C95A: 19              DAA                         
C95B: 86 70           LDA     #$70                  
C95D: A1 C8 E0        CMPA    $E0,U                 
C960: 23 12           BLS     $C974                   
C962: F6 10 09        LDB     $1009                   
C965: 26 09           BNE     $C970                   
C967: A1 41           CMPA    1,U                 
C969: 23 09           BLS     $C974                   
C96B: A1 C8 E1        CMPA    $E1,U                 
C96E: 23 04           BLS     $C974                   
C970: 7F 10 D8        CLR     $10D8                   
C973: 39              RTS                         
C974: B7 10 D8        STA     $10D8                   
C977: 39              RTS                         
C978: E6 05           LDB     5,X                 
C97A: B6 10 C4        LDA     $10C4                   
C97D: 27 01           BEQ     $C980                   
C97F: 53              COMB                        
C980: C4 04           ANDB    #$04                  
C982: 58 ; ????
C983: 58 ; ????
C984: CE 1F 50        LDU     #$1F50                  
C987: 1E 31           EXG     U,X                   
C989: A6 45           LDA     5,U                 
C98B: 10 AE 5E        LDY     -2,U                
C98E: 85 02           BITA    #$02                  
C990: 26 0B           BNE     $C99D                   
C992: EB 4F           ADDB    15,U                
C994: C4 F0           ANDB    #$F0                  
C996: E7 0F           STB     15,X                
C998: 10 AF 1E        STY     -2,X                
C99B: 20 0F           BRA     $C9AC                   
C99D: 31 A5           LEAY    B,Y                 
C99F: 10 AF 1E        STY     -2,X                
C9A2: E6 1F           LDB     -1,X                
C9A4: C4 F0           ANDB    #$F0                  
C9A6: E7 1F           STB     -1,X                
C9A8: E6 4F           LDB     15,U                
C9AA: E7 0F           STB     15,X                
C9AC: B6 10 13        LDA     $1013                   
C9AF: FF 10 36        STU     $1036                   
C9B2: 8D 98           BSR     $C94C                   
C9B4: BE 10 36        LDX     $1036                   
C9B7: 39              RTS                         
C9B8: 81 04           CMPA    #$04                  
C9BA: 26 01           BNE     $C9BD                   
C9BC: 48 ; ????
C9BD: B7 10 C0        STA     $10C0                   
C9C0: BD C5 34        JSR     $C534                   
C9C3: C1 28           CMPB    #$28                  
C9C5: 27 0F           BEQ     $C9D6                   
C9C7: 81 70           CMPA    #$70                  
C9C9: 24 ; ????
C9CA: 0B ; ????
C9CB: 86 70           LDA     #$70                  
C9CD: A1 C8 E0        CMPA    $E0,U                 
C9D0: 23 04           BLS     $C9D6                   
C9D2: 7F 10 D8        CLR     $10D8                   
C9D5: 39              RTS                         
C9D6: B7 10 D8        STA     $10D8                   
C9D9: 39              RTS                         
C9DA: 8E 15 FF        LDX     #$15FF                  
C9DD: 10 8E D4 76     LDY     #$D476                  
C9E1: C6 3C           LDB     #$3C                  
C9E3: A6 85           LDA     B,X                 
C9E5: 27 5D           BEQ     $CA44                   
C9E7: F7 10 35        STB     $1035                   
C9EA: BF 10 36        STX     $1036                   
C9ED: 58 ; ????
C9EE: AE A5           LDX     B,Y                 
C9F0: 30 89 08 00     LEAX    $0800,X                 
C9F4: CE CC 20        LDU     #$CC20                  
C9F7: 5F              CLRB                        
C9F8: F7 10 CE        STB     $10CE                   
C9FB: A6 85           LDA     B,X                 
C9FD: 81 30           CMPA    #$30                  
C9FF: 27 08           BEQ     $CA09                   
CA01: B6 10 CE        LDA     $10CE                   
CA04: AA 44           ORA     4,U                 
CA06: B7 10 CE        STA     $10CE                   
CA09: E6 C0           LDB     ,U+                 
CA0B: 26 EE           BNE     $C9FB                   
CA0D: B6 10 CE        LDA     $10CE                   
CA10: 27 23           BEQ     $CA35                   
CA12: CE C1 96        LDU     #$C196                  
CA15: 10 BF 10 3A     STY     $103A                   
CA19: 10 8E CB FA     LDY     #$CBFA                  
CA1D: 44              LSRA                        
CA1E: 25 ; ????
CA1F: 0E E6           JMP     $E6                   
CA21: 89 F8           ADCA    #$F8                  
CA23: 00 CB           NEG     $CB                   
CA25: 50              NEGB                        
CA26: E7 89 F8 00     STB     $F800,X                 
CA2A: E6 A5           LDB     B,Y                 
CA2C: E7 84           STB     ,X                  
CA2E: E6 C0           LDB     ,U+                 
CA30: 27 06           BEQ     $CA38                   
CA32: 3A              ABX                         
CA33: 20 E8           BRA     $CA1D                   
CA35: 4C              INCA                        
CA36: 20 04           BRA     $CA3C                   
CA38: 10 BE 10 3A     LDY     $103A                   
CA3C: F6 10 35        LDB     $1035                   
CA3F: BE 10 36        LDX     $1036                   
CA42: A7 85           STA     B,X                 
CA44: 5A              DECB                        
CA45: 26 9C           BNE     $C9E3                   
CA47: 8E 15 88        LDX     #$1588                  
CA4A: 86 08           LDA     #$08                  
CA4C: B7 10 09        STA     $1009                   
CA4F: 10 8E CC 31     LDY     #$CC31                  
CA53: A6 89 FE 80     LDA     $FE80,X                 
CA57: 10 2C 01 B8     LBGE    $CC13                   
CA5B: 7F 10 CF        CLR     $10CF                   
CA5E: 6F 89 FE 80     CLR     $FE80,X                 
CA62: A6 84           LDA     ,X                  
CA64: E6 A6           LDB     A,Y                 
CA66: 53              COMB                        
CA67: C4 0F           ANDB    #$0F                  
CA69: F7 10 35        STB     $1035                   
CA6C: CE CC 28        LDU     #$CC28                  
CA6F: E6 C1           LDB     ,U++                
CA71: 27 12           BEQ     $CA85                   
CA73: A6 85           LDA     B,X                 
CA75: 81 0A           CMPA    #$0A                  
CA77: 27 F6           BEQ     $CA6F                   
CA79: E6 A6           LDB     A,Y                 
CA7B: E4 5F           ANDB    -1,U                
CA7D: FA 10 CF        ORB     $10CF                   
CA80: F7 10 CF        STB     $10CF                   
CA83: 20 EA           BRA     $CA6F                   
CA85: F6 10 CF        LDB     $10CF                   
CA88: F4 10 35        ANDB    $1035                   
CA8B: F7 10 CF        STB     $10CF                   
CA8E: BF 10 36        STX     $1036                   
CA91: 8E D3 88        LDX     #$D388                  
CA94: F6 10 09        LDB     $1009                   
CA97: 58 ; ????
CA98: 3A              ABX                         
CA99: CC 00 04        LDD     #$0004                  
CA9C: B7 10 3A        STA     $103A                   
CA9F: F7 10 CE        STB     $10CE                   
CAA2: EE 84           LDU     ,X                  
CAA4: 33 C8 20        LEAU    $20,U                 
CAA7: FF 10 38        STU     $1038                   
CAAA: 8E CC 46        LDX     #$CC46                  
CAAD: 76 10 CF        ROR     $10CF                   
CAB0: 10 ; ????
CAB1: 24 ; ????
CAB2: 01 ; ????
CAB3: 50              NEGB                        
CAB4: A6 80           LDA     ,X+                 
CAB6: 10 27 01 4C     LBEQ    $CC06                   
CABA: 7A 10 3A        DEC     $103A                   
CABD: 33 C6           LEAU    A,U                 
CABF: E6 C9 08 00     LDB     $0800,U                 
CAC3: C4 3F           ANDB    #$3F                  
CAC5: A6 C4           LDA     ,U                  
CAC7: 2A 32           BPL     $CAFB                   
CAC9: C1 0F           CMPB    #$0F                  
CACB: 27 E7           BEQ     $CAB4                   
CACD: C1 10           CMPB    #$10                  
CACF: 10 ; ????
CAD0: 25 ; ????
CAD1: 00 A0           NEG     $A0                   
CAD3: 81 D0           CMPA    #$D0                  
CAD5: 27 DD           BEQ     $CAB4                   
CAD7: 81 EA           CMPA    #$EA                  
CAD9: 27 10           BEQ     $CAEB                   
CADB: 81 A3           CMPA    #$A3                  
CADD: 27 04           BEQ     $CAE3                   
CADF: 81 84           CMPA    #$84                  
CAE1: 26 10           BNE     $CAF3                   
CAE3: C6 25           LDB     #$25                  
CAE5: E7 C9 08 00     STB     $0800,U                 
CAE9: 20 C9           BRA     $CAB4                   
CAEB: C6 36           LDB     #$36                  
CAED: E7 C9 08 00     STB     $0800,U                 
CAF1: 20 C1           BRA     $CAB4                   
CAF3: C6 09           LDB     #$09                  
CAF5: E7 C9 08 00     STB     $0800,U                 
CAF9: 20 B9           BRA     $CAB4                   
CAFB: C4 0F           ANDB    #$0F                  
CAFD: 84 03           ANDA    #$03                  
CAFF: 81 03           CMPA    #$03                  
CB01: 10 26 00 84     LBNE    $CB89                   
CB05: B6 10 CE        LDA     $10CE                   
CB08: 81 04           CMPA    #$04                  
CB0A: 27 A8           BEQ     $CAB4                   
CB0C: 81 02           CMPA    #$02                  
CB0E: 27 09           BEQ     $CB19                   
CB10: B6 10 3A        LDA     $103A                   
CB13: 85 02           BITA    #$02                  
CB15: 27 43           BEQ     $CB5A                   
CB17: 20 70           BRA     $CB89                   
CB19: B7 10 34        STA     $1034                   
CB1C: A6 C4           LDA     ,U                  
CB1E: 81 67           CMPA    #$67                  
CB20: 27 13           BEQ     $CB35                   
CB22: 81 6B           CMPA    #$6B                  
CB24: 26 31           BNE     $CB57                   
CB26: A6 C8 E0        LDA     $E0,U                 
CB29: 2A 2C           BPL     $CB57                   
CB2B: 81 B8           CMPA    #$B8                  
CB2D: 27 28           BEQ     $CB57                   
CB2F: 81 85           CMPA    #$85                  
CB31: 27 24           BEQ     $CB57                   
CB33: 20 0D           BRA     $CB42                   
CB35: A6 C8 20        LDA     $20,U                 
CB38: 2A 1D           BPL     $CB57                   
CB3A: 81 B0           CMPA    #$B0                  
CB3C: 27 19           BEQ     $CB57                   
CB3E: 81 8A           CMPA    #$8A                  
CB40: 27 15           BEQ     $CB57                   
CB42: CA 20           ORB     #$20                  
CB44: E7 C9 08 00     STB     $0800,U                 
CB48: E6 C9 08 01     LDB     $0801,U                 
CB4C: C4 0F           ANDB    #$0F                  
CB4E: CA 20           ORB     #$20                  
CB50: E7 C9 08 01     STB     $0801,U                 
CB54: 7E CA B4        JMP     $CAB4                   
CB57: B6 10 34        LDA     $1034                   
CB5A: 84 01           ANDA    #$01                  
CB5C: 43              COMA                        
CB5D: 84 1F           ANDA    #$1F                  
CB5F: AB C4           ADDA    ,U                  
CB61: 81 86           CMPA    #$86                  
CB63: 27 04           BEQ     $CB69                   
CB65: 81 82           CMPA    #$82                  
CB67: 26 01           BNE     $CB6A                   
CB69: 4A              DECA                        
CB6A: A7 C4           STA     ,U                  
CB6C: E7 C9 08 00     STB     $0800,U                 
CB70: 7E CA B4        JMP     $CAB4                   
CB73: B6 10 CE        LDA     $10CE                   
CB76: 81 04           CMPA    #$04                  
CB78: 10 27 FF 38     LBEQ    $CAB4                   
CB7C: A6 C4           LDA     ,U                  
CB7E: 81 85           CMPA    #$85                  
CB80: 26 01           BNE     $CB83                   
CB82: 4C              INCA                        
CB83: 80 1F           SUBA    #$1F                  
CB85: A7 C4           STA     ,U                  
CB87: C4 0F           ANDB    #$0F                  
CB89: B6 10 CE        LDA     $10CE                   
CB8C: 85 01           BITA    #$01                  
CB8E: 27 6B           BEQ     $CBFB                   
CB90: 85 02           BITA    #$02                  
CB92: 27 05           BEQ     $CB99                   
CB94: A6 C8 20        LDA     $20,U                 
CB97: 20 03           BRA     $CB9C                   
CB99: A6 C8 E0        LDA     $E0,U                 
CB9C: 81 FC           CMPA    #$FC                  
CB9E: 25 ; ????
CB9F: 36 A6           PSHU    PC,Y,B,A                   
CBA1: 5F              CLRB                        
CBA2: 81 FC           CMPA    #$FC                  
CBA4: 24 ; ????
CBA5: 55 ; ????
CBA6: 81 81           CMPA    #$81                  
CBA8: 27 20           BEQ     $CBCA                   
CBAA: 81 8E           CMPA    #$8E                  
CBAC: 27 2C           BEQ     $CBDA                   
CBAE: 81 BC           CMPA    #$BC                  
CBB0: 26 0C           BNE     $CBBE                   
CBB2: A6 C9 07 FF     LDA     $07FF,U                 
CBB6: 81 28           CMPA    #$28                  
CBB8: 26 1C           BNE     $CBD6                   
CBBA: 86 01           LDA     #$01                  
CBBC: 20 9C           BRA     $CB5A                   
CBBE: 81 B5           CMPA    #$B5                  
CBC0: 26 14           BNE     $CBD6                   
CBC2: A6 C9 07 FF     LDA     $07FF,U                 
CBC6: 81 28           CMPA    #$28                  
CBC8: 26 0C           BNE     $CBD6                   
CBCA: CC 86 09        LDD     #$8609                  
CBCD: A7 C4           STA     ,U                  
CBCF: E7 C9 08 00     STB     $0800,U                 
CBD3: 7E CA B4        JMP     $CAB4                   
CBD6: 81 8D           CMPA    #$8D                  
CBD8: 26 05           BNE     $CBDF                   
CBDA: CC 89 03        LDD     #$8903                  
CBDD: 20 8B           BRA     $CB6A                   
CBDF: B6 10 3A        LDA     $103A                   
CBE2: 85 02           BITA    #$02                  
CBE4: 27 15           BEQ     $CBFB                   
CBE6: A6 C9 07 FF     LDA     $07FF,U                 
CBEA: 81 10           CMPA    #$10                  
CBEC: 25 ; ????
CBED: 0D 81           TST     $81                   
CBEF: 20 24           BRA     $CC15                   
CBF1: 09 CA           ROL     $CA                   
CBF3: 10 ; ????
CBF4: E7 C9 08 00     STB     $0800,U                 
CBF8: 7E CA B4        JMP     $CAB4                   
CBFB: CA 20           ORB     #$20                  
CBFD: E7 C9 08 00     STB     $0800,U                 
CC01: 7E CA B4        JMP     $CAB4                   
CC04: 30 05           LEAX    5,X                 
CC06: FE 10 38        LDU     $1038                   
CC09: 7A 10 CE        DEC     $10CE                   
CC0C: 10 26 FE 9D     LBNE    $CAAD                   
CC10: BE 10 36        LDX     $1036                   
CC13: 7C 10 09        INC     $1009                   
CC16: 30 01           LEAX    1,X                 
CC18: 8C 15 F0        CMPX    #$15F0                  
CC1B: 10 26 FE 34     LBNE    $CA53                   
CC1F: 39              RTS                         
CC20: 01 ; ????
CC21: 21 20           BRN     $CC43                   
CC23: 00 01           NEG     $01                   
CC25: 02 ; ????
CC26: 08 ; ????
CC27: 04 FF           LSR     $FF                   
CC29: 01 ; ????
CC2A: F8 02 01        EORB    $0201                   
CC2D: 04 08           LSR     $08                   
CC2F: 08 ; ????
CC30: 00 0C           NEG     $0C                   
CC32: 0E 09           JMP     $09                   
CC34: 0C 0E           INC     $0E                   
CC36: 04 0C           LSR     $0C                   
CC38: 06 0F           ROR     $0F                   
CC3A: 0F 00           CLR     $00                   
CC3C: 02 ; ????
CC3D: 08 ; ????
CC3E: 02 ; ????
CC3F: 01 ; ????
CC40: 09 08           ROL     $08                   
CC42: 01 ; ????
CC43: 01 ; ????
CC44: 01 ; ????
CC45: 01 ; ????
CC46: 3F              SWI                         
CC47: E0 E0           SUBB    ,S+                 
CC49: E0 00           SUBB    0,X                 
CC4B: C0 01           SUBB    #$01                  
CC4D: 01 ; ????
CC4E: 01 ; ????
CC4F: 00 E4           NEG     $E4                   
CC51: 20 20           BRA     $CC73                   
CC53: 20 00           BRA     $CC55                   
CC55: 60 01           NEG     1,X                 
CC57: 01 ; ????
CC58: 01 ; ????
CC59: 00 10           NEG     $10                   
CC5B: 18 ; ????
CC5C: 14 ; ????
CC5D: 1C 10           ANDCC   #$10                  
CC5F: 18 ; ????
CC60: 11 ; ????
CC61: 19              DAA                         
CC62: 10 ; ????
CC63: 12              NOP                         
CC64: 11 ; ????
CC65: 13              SYNC                        
CC66: 10 ; ????
CC67: 12              NOP                         
CC68: 14 ; ????
CC69: 16 8E 1F        LBRA    $5A8B                   
CC6C: 70 A6 10        NEG     $A610                   
CC6F: 27 0E           BEQ     $CC7F                   
CC71: CE 15 80        LDU     #$1580                  
CC74: BD CD 83        JSR     $CD83                   
CC77: A6 C5           LDA     B,U                 
CC79: 81 0A           CMPA    #$0A                  
CC7B: 25 ; ????
CC7C: 02 ; ????
CC7D: 6F 10           CLR     -16,X               
CC7F: 8E 25 30        LDX     #$2530                  
CC82: A6 10           LDA     -16,X               
CC84: 27 39           BEQ     $CCBF                   
CC86: A6 1A           LDA     -6,X                
CC88: 81 0D           CMPA    #$0D                  
CC8A: 24 ; ????
CC8B: 33 BD CD 9B     LEAU    [$9A2A,PC]              
CC8F: 4D              TSTA                        
CC90: 27 2D           BEQ     $CCBF                   
CC92: E6 05           LDB     5,X                 
CC94: C4 06           ANDB    #$06                  
CC96: CB 10           ADDB    #$10                  
CC98: E7 0A           STB     10,X                
CC9A: A6 19           LDA     -7,X                
CC9C: 2A 13           BPL     $CCB1                   
CC9E: CB 08           ADDB    #$08                  
CCA0: E7 0A           STB     10,X                
CCA2: A6 13           LDA     -13,X               
CCA4: 27 0B           BEQ     $CCB1                   
CCA6: BF 10 36        STX     $1036                   
CCA9: AE 15           LDX     -11,X               
CCAB: BD 87 32        JSR     $8732                   
CCAE: BE 10 36        LDX     $1036                   
CCB1: CC 3F 0F        LDD     #$3F0F                  
CCB4: A7 04           STA     4,X                 
CCB6: E7 1A           STB     -6,X                
CCB8: CC 00 01        LDD     #$0001                  
CCBB: A7 08           STA     8,X                 
CCBD: E7 0B           STB     11,X                
CCBF: 30 88 20        LEAX    $20,X                 
CCC2: 8C 26 70        CMPX    #$2670                  
CCC5: 26 BB           BNE     $CC82                   
CCC7: B6 10 DA        LDA     $10DA                   
CCCA: BA 10 D0        ORA     $10D0                   
CCCD: 27 01           BEQ     $CCD0                   
CCCF: 39              RTS                         
CCD0: 8E 25 10        LDX     #$2510                  
CCD3: 86 01           LDA     #$01                  
CCD5: B7 10 C0        STA     $10C0                   
CCD8: BD C5 34        JSR     $C534                   
CCDB: 7D 10 EC        TST     $10EC                   
CCDE: 27 23           BEQ     $CD03                   
CCE0: 81 70           CMPA    #$70                  
CCE2: 10 ; ????
CCE3: 25 ; ????
CCE4: 00 84           NEG     $84                   
CCE6: A6 C8 20        LDA     $20,U                 
CCE9: 81 70           CMPA    #$70                  
CCEB: 10 ; ????
CCEC: 25 ; ????
CCED: 00 7B           NEG     $7B                   
CCEF: A6 41           LDA     1,U                 
CCF1: 81 70           CMPA    #$70                  
CCF3: 10 ; ????
CCF4: 25 ; ????
CCF5: 00 73           NEG     $73                   
CCF7: A6 C8 21        LDA     $21,U                 
CCFA: 81 70           CMPA    #$70                  
CCFC: 25 ; ????
CCFD: 6C CC 44        INC     $CD44,PC                
CD00: 06 20           ROR     $20                   
CD02: 33 EA C9        LEAU    $C9,X                 
CD05: 08 ; ????
CD06: 01 ; ????
CD07: EA C9 08 21     ORB     $0821,U                 
CD0B: EA C9 08 20     ORB     $0820,U                 
CD0F: C4 80           ANDB    #$80                  
CD11: F7 10 EB        STB     $10EB                   
CD14: 5F              CLRB                        
CD15: 8E CD 6B        LDX     #$CD6B                  
CD18: A6 81           LDA     ,X++                
CD1A: A6 C6           LDA     A,U                 
CD1C: 81 90           CMPA    #$90                  
CD1E: 25 ; ????
CD1F: 02 ; ????
CD20: EA 1F           ORB     -1,X                
CD22: 8C CD 73        CMPX    #$CD73                  
CD25: 26 F1           BNE     $CD18                   
CD27: A6 85           LDA     B,X                 
CD29: 27 3F           BEQ     $CD6A                   
CD2B: 2A 03           BPL     $CD30                   
CD2D: CC 44 06        LDD     #$4406                  
CD30: 7D 10 EB        TST     $10EB                   
CD33: 26 01           BNE     $CD36                   
CD35: 39              RTS                         
CD36: 8E 25 10        LDX     #$2510                  
CD39: 6F 08           CLR     8,X                 
CD3B: A7 0A           STA     10,X                
CD3D: 81 40           CMPA    #$40                  
CD3F: 26 06           BNE     $CD47                   
CD41: 86 06           LDA     #$06                  
CD43: AB 0F           ADDA    15,X                
CD45: A7 0F           STA     15,X                
CD47: C1 08           CMPB    #$08                  
CD49: 25 ; ????
CD4A: 08 ; ????
CD4B: C1 09           CMPB    #$09                  
CD4D: 27 04           BEQ     $CD53                   
CD4F: 86 02           LDA     #$02                  
CD51: A7 08           STA     8,X                 
CD53: CC 01 5F        LDD     #$015F                  
CD56: B7 10 DA        STA     $10DA                   
CD59: E7 04           STB     4,X                 
CD5B: 7F 25 01        CLR     $2501                   
CD5E: B6 25 02        LDA     $2502                   
CD61: 26 01           BNE     $CD64                   
CD63: 39              RTS                         
CD64: BD A5 4F        JSR     $A54F                   
CD67: 7F 25 02        CLR     $2502                   
CD6A: 39              RTS                         
CD6B: 00 01           NEG     $01                   
CD6D: 01 ; ????
CD6E: 02 ; ????
CD6F: 21 04           BRN     $CD75                   
CD71: 20 08           BRA     $CD7B                   
CD73: 00 42           NEG     $42                   
CD75: 44              LSRA                        
CD76: 42 ; ????
CD77: 44              LSRA                        
CD78: 40              NEGA                        
CD79: 44              LSRA                        
CD7A: FF 42 40        STU     $4240                   
CD7D: 40              NEGA                        
CD7E: 40              NEGA                        
CD7F: 42 ; ????
CD80: 40              NEGA                        
CD81: 42 ; ????
CD82: FF E6 0F        STU     $E60F                   
CD85: 54              LSRB                        
CD86: 54              LSRB                        
CD87: 54              LSRB                        
CD88: 54              LSRB                        
CD89: 54              LSRB                        
CD8A: F7 10 35        STB     $1035                   
CD8D: EC 1E           LDD     -2,X                
CD8F: 83 00 10        SUBD    #$0010                  
CD92: C4 E0           ANDB    #$E0                  
CD94: 46              RORA                        
CD95: 56              RORB                        
CD96: 54              LSRB                        
CD97: FB 10 35        ADDB    $1035                   
CD9A: 39              RTS                         
CD9B: 86 01           LDA     #$01                  
CD9D: B7 10 C0        STA     $10C0                   
CDA0: BD C5 34        JSR     $C534                   
CDA3: 86 70           LDA     #$70                  
CDA5: F6 10 EC        LDB     $10EC                   
CDA8: 27 0F           BEQ     $CDB9                   
CDAA: A1 41           CMPA    1,U                 
CDAC: 10 22 00 96     LBHI    $CE46                   
CDB0: A1 C8 21        CMPA    $21,U                 
CDB3: 10 22 00 8F     LBHI    $CE46                   
CDB7: 20 06           BRA     $CDBF                   
CDB9: E6 1A           LDB     -6,X                
CDBB: C1 0C           CMPB    #$0C                  
CDBD: 27 27           BEQ     $CDE6                   
CDBF: A1 C4           CMPA    ,U                  
CDC1: 10 22 00 81     LBHI    $CE46                   
CDC5: A1 C8 20        CMPA    $20,U                 
CDC8: 22 7C           BHI     $CE46                   
CDCA: 5F              CLRB                        
CDCB: A1 C8 E0        CMPA    $E0,U                 
CDCE: 22 02           BHI     $CDD2                   
CDD0: CA 01           ORB     #$01                  
CDD2: A1 C8 40        CMPA    $40,U                 
CDD5: 22 02           BHI     $CDD9                   
CDD7: CA 02           ORB     #$02                  
CDD9: C1 03           CMPB    #$03                  
CDDB: 27 42           BEQ     $CE1F                   
CDDD: 86 04           LDA     #$04                  
CDDF: C5 02           BITB    #$02                  
CDE1: 26 36           BNE     $CE19                   
CDE3: 40              NEGA                        
CDE4: 20 33           BRA     $CE19                   
CDE6: 5F              CLRB                        
CDE7: A6 C4           LDA     ,U                  
CDE9: 81 70           CMPA    #$70                  
CDEB: 25 ; ????
CDEC: 07 84           ASR     $84                   
CDEE: F0 81 80        SUBB    $8180                   
CDF1: 27 01           BEQ     $CDF4                   
CDF3: 5C              INCB                        
CDF4: A6 C8 20        LDA     $20,U                 
CDF7: 81 70           CMPA    #$70                  
CDF9: 25 ; ????
CDFA: 08 ; ????
CDFB: 84 F0           ANDA    #$F0                  
CDFD: 81 80           CMPA    #$80                  
CDFF: 27 02           BEQ     $CE03                   
CE01: 5C              INCB                        
CE02: 5C              INCB                        
CE03: F7 10 CF        STB     $10CF                   
CE06: 27 3E           BEQ     $CE46                   
CE08: C1 03           CMPB    #$03                  
CE0A: 27 13           BEQ     $CE1F                   
CE0C: 86 08           LDA     #$08                  
CE0E: C5 02           BITB    #$02                  
CE10: 26 01           BNE     $CE13                   
CE12: 40              NEGA                        
CE13: E6 1F           LDB     -1,X                
CE15: C4 F0           ANDB    #$F0                  
CE17: E7 1F           STB     -1,X                
CE19: EE 1E           LDU     -2,X                
CE1B: 33 C6           LEAU    A,U                 
CE1D: EF 1E           STU     -2,X                
CE1F: B6 10 EC        LDA     $10EC                   
CE22: 26 19           BNE     $CE3D                   
CE24: CE 12 80        LDU     #$1280                  
CE27: 10 8E 12 FB     LDY     #$12FB                  
CE2B: BD CD 83        JSR     $CD83                   
CE2E: A6 C5           LDA     B,U                 
CE30: 26 11           BNE     $CE43                   
CE32: 5A              DECB                        
CE33: A6 C5           LDA     B,U                 
CE35: 26 0C           BNE     $CE43                   
CE37: CB 02           ADDB    #$02                  
CE39: A6 C5           LDA     B,U                 
CE3B: 26 06           BNE     $CE43                   
CE3D: 7C 10 CB        INC     $10CB                   
CE40: 86 01           LDA     #$01                  
CE42: 39              RTS                         
CE43: 6C A6           INC     A,Y                 
CE45: 39              RTS                         
CE46: 4F              CLRA                        
CE47: 39              RTS                         
CE48: 68 ; ????
CE49: 10 ; ????
CE4A: 6C 10           INC     -16,X               
CE4C: 64 10           LSR     -16,X               
CE4E: 0F 10           CLR     $10                   
CE50: 68 ; ????
CE51: 10 ; ????
CE52: 6C 10           INC     -16,X               
CE54: CC 25 C3        LDD     #$25C3                  
CE57: 27 68           BEQ     $CEC1                   
CE59: 10 ; ????
CE5A: 0E 10           JMP     $10                   
CE5C: F0 25 AD        SUBB    $25AD                   
CE5F: 17 C1 25        LBSR    $8F87                   
CE62: 87 ; ????
CE63: 33 ; ????
CE64: AE 3D           LDX     -3,Y                
CE66: C0 3E           SUBB    #$3E                  
CE68: A3 25           SUBD    5,Y                 
CE6A: D3 17           ADDD    $17                   
CE6C: 64 10           LSR     -16,X               
CE6E: 0E 10           JMP     $10                   
CE70: D1 3D           CMPB    $3D                   
CE72: D0 15           SUBB    $15                   
CE74: AF 25           STX     5,Y                 
CE76: CB 37           ADDB    #$37                  
CE78: 68 ; ????
CE79: 10 ; ????
CE7A: 0F 10           CLR     $10                   
CE7C: 64 10           LSR     -16,X               
CE7E: 60 10           NEG     -16,X               
CE80: 0E 10           JMP     $10                   
CE82: CC 2D 64        LDD     #$2D64                  
CE85: 10 ; ????
CE86: 60 10           NEG     -16,X               
CE88: 68 ; ????
CE89: 10 ; ????
CE8A: 6C 10           INC     -16,X               
CE8C: 64 10           LSR     -16,X               
CE8E: 0B ; ????
CE8F: 27 8C           BEQ     $CE1D                   
CE91: 05 ; ????
CE92: 87 ; ????
CE93: 39              RTS                         
CE94: E5 27           BITB    7,Y                 
CE96: E6 37           LDB     -9,Y                
CE98: 68 ; ????
CE99: 10 ; ????
CE9A: 0A 27           DEC     $27                   
CE9C: A4 25           ANDA    5,Y                 
CE9E: 8B 31           ADDA    #$31                  
CEA0: E3 32           ADDD    -14,Y               
CEA2: CD ; ????
CEA3: 04 ED           LSR     $ED                   
CEA5: 31 E3           LEAY    ,--S                
CEA7: 1E 68           EXG     ?,A                   
CEA9: 10 ; ????
CEAA: 6C 10           INC     -16,X               
CEAC: 64 10           LSR     -16,X               
CEAE: 0E 10           JMP     $10                   
CEB0: 68 ; ????
CEB1: 10 ; ????
CEB2: 6C 10           INC     -16,X               
CEB4: 0F 10           CLR     $10                   
CEB6: EB 27           ADDB    7,Y                 
CEB8: 68 ; ????
CEB9: 10 ; ????
CEBA: 0F 10           CLR     $10                   
CEBC: 64 10           LSR     -16,X               
CEBE: 60 10           NEG     -16,X               
CEC0: 77 27 E8        ASR     $27E8                   
CEC3: 2B 8F           BMI     $CE54                   
CEC5: 2D EA           BLT     $CEB1                   
CEC7: 39              RTS                         
CEC8: 68 ; ????
CEC9: 10 ; ????
CECA: 6C 10           INC     -16,X               
CECC: 64 10           LSR     -16,X               
CECE: 0E 10           JMP     $10                   
CED0: 8E 25 84        LDX     #$2584                  
CED3: 31 73           LEAY    -13,S               
CED5: 27 DA           BEQ     $CEB1                   
CED7: 37 68           PULU    DP,Y,S                   
CED9: 10 ; ????
CEDA: 0F 10           CLR     $10                   
CEDC: 64 10           LSR     -16,X               
CEDE: 60 10           NEG     -16,X               
CEE0: 72 ; ????
CEE1: 27 DB           BEQ     $CEBE                   
CEE3: 2D 64           BLT     $CF49                   
CEE5: 10 ; ????
CEE6: 60 10           NEG     -16,X               
CEE8: A7 25           STA     5,Y                 
CEEA: 83 2B 64        SUBD    #$2B64                  
CEED: 10 ; ????
CEEE: 0D 27           TST     $27                   
CEF0: E0 31           SUBB    -15,Y               
CEF2: CA 01           ORB     #$01                  
CEF4: DF 27           STU     $27                   
CEF6: DE 37           LDU     $37                   
CEF8: 68 ; ????
CEF9: 10 ; ????
CEFA: 0C 27           INC     $27                   
CEFC: 64 10           LSR     -16,X               
CEFE: 60 10           NEG     -16,X               
CF00: DD 27           STD     $27                   
CF02: DE 33           LDU     $33                   
CF04: 64 10           LSR     -16,X               
CF06: DC 3B           LDD     $3B                   
CF08: B0 2C 6C        SUBA    $2C6C                   
CF0B: 10 ; ????
CF0C: B1 07 B2        CMPA    $07B2                   
CF0F: 07 68           ASR     $68                   
CF11: 10 ; ????
CF12: 6C 10           INC     -16,X               
CF14: 0E 10           JMP     $10                   
CF16: 60 10           NEG     -16,X               
CF18: FE 0F B3        LDU     $0FB3                   
CF1B: 07 FD           ASR     $FD                   
CF1D: 0F FF           CLR     $FF                   
CF1F: 0F 0F           CLR     $0F                   
CF21: 10 ; ????
CF22: 6C 10           INC     -16,X               
CF24: B4 07 B5        ANDA    $07B5                   
CF27: 2C FC           BGE     $CF25                   
CF29: 0F FE           CLR     $FE                   
CF2B: 0F FD           CLR     $FD                   
CF2D: 0F BA           CLR     $BA                   
CF2F: 07 BB           ASR     $BB                   
CF31: 07 BC           ASR     $BC                   
CF33: 2C 0E           BGE     $CF43                   
CF35: 10 ; ????
CF36: 60 10           NEG     -16,X               
CF38: B9 07 0E        ADCA    $070E                   
CF3B: 10 ; ????
CF3C: B8 2C 60        EORA    $2C60                   
CF3F: 10 ; ????
CF40: 0F 10           CLR     $10                   
CF42: 6C 10           INC     -16,X               
CF44: 64 10           LSR     -16,X               
CF46: 60 10           NEG     -16,X               
CF48: 68 ; ????
CF49: 10 ; ????
CF4A: 6C 10           INC     -16,X               
CF4C: 64 10           LSR     -16,X               
CF4E: 0F 10           CLR     $10                   
CF50: 68 ; ????
CF51: 10 ; ????
CF52: 6C 10           INC     -16,X               
CF54: 0E 10           JMP     $10                   
CF56: 60 10           NEG     -16,X               
CF58: 68 ; ????
CF59: 10 ; ????
CF5A: 0E 10           JMP     $10                   
CF5C: 64 10           LSR     -16,X               
CF5E: 60 10           NEG     -16,X               
CF60: 0F 10           CLR     $10                   
CF62: 6C 10           INC     -16,X               
CF64: 64 10           LSR     -16,X               
CF66: 60 10           NEG     -16,X               
CF68: 68 ; ????
CF69: 10 ; ????
CF6A: 6C 10           INC     -16,X               
CF6C: 64 10           LSR     -16,X               
CF6E: 0F 10           CLR     $10                   
CF70: 68 ; ????
CF71: 10 ; ????
CF72: 6C 10           INC     -16,X               
CF74: 0E 10           JMP     $10                   
CF76: 60 10           NEG     -16,X               
CF78: 68 ; ????
CF79: 10 ; ????
CF7A: 0E 10           JMP     $10                   
CF7C: 64 10           LSR     -16,X               
CF7E: 60 10           NEG     -16,X               
CF80: 0F 10           CLR     $10                   
CF82: 6C 10           INC     -16,X               
CF84: 64 10           LSR     -16,X               
CF86: 60 10           NEG     -16,X               
CF88: FC 0F FD        LDD     $0FFD                   
CF8B: 0F FE           CLR     $FE                   
CF8D: 0F FF           CLR     $FF                   
CF8F: 0F FD           CLR     $FD                   
CF91: 0F FD           CLR     $FD                   
CF93: 0F FC           CLR     $FC                   
CF95: 0F FE           CLR     $FE                   
CF97: 0F FF           CLR     $FF                   
CF99: 0F FE           CLR     $FE                   
CF9B: 0F FC           CLR     $FC                   
CF9D: 0F FD           CLR     $FD                   
CF9F: 0F FE           CLR     $FE                   
CFA1: 0F FF           CLR     $FF                   
CFA3: 0F FF           CLR     $FF                   
CFA5: 0F FC           CLR     $FC                   
CFA7: 0F C6           CLR     $C6                   
CFA9: 2B C7           BMI     $CF72                   
CFAB: 34 C4           PSHS    PC,U,B                   
CFAD: 27 C5           BEQ     $CF74                   
CFAF: 31 C8 31        LEAY    $31,U                 
CFB2: FC 0F C4        LDD     $0FC4                   
CFB5: 3E              RESET                       
CFB6: FD 0F C2        STD     $0FC2                   
CFB9: 31 C1           LEAY    ,U++                
CFBB: 3F              SWI                         
CFBC: FC 0F FE        LDD     $0FFE                   
CFBF: 0F FC           CLR     $FC                   
CFC1: 0F FE           CLR     $FE                   
CFC3: 0F FF           CLR     $FF                   
CFC5: 0F FD           CLR     $FD                   
CFC7: 0F D0           CLR     $D0                   
CFC9: 2F FC           BLE     $CFC7                   
CFCB: 0F CE           CLR     $CE                   
CFCD: 31 ; ????
CFCE: CF ; ????
CFCF: 31 ; ????
CFD0: FE 0F FD        LDU     $0FFD                   
CFD3: 0F CD           CLR     $CD                   
CFD5: 2E FC           BGT     $CFD3                   
CFD7: 0F CB           CLR     $CB                   
CFD9: 33 C0           LEAU    ,U+                 
CFDB: 32 C9 2B CA     LEAS    $2BCA,U                 
CFDF: 2B CD           BMI     $CFAE                   
CFE1: 36 FE           PSHU    PC,S,Y,X,DP,B,A                   
CFE3: 0F C2           CLR     $C2                   
CFE5: 3F              SWI                         
CFE6: FF 0F E7        STU     $0FE7                   
CFE9: 39              RTS                         
CFEA: FC 0F E6        LDD     $0FE6                   
CFED: 2F FF           BLE     $CFEE                   
CFEF: 0F FD           CLR     $FD                   
CFF1: 0F FE           CLR     $FE                   
CFF3: 0F FF           CLR     $FF                   
CFF5: 0F FC           CLR     $FC                   
CFF7: 0F FE           CLR     $FE                   
CFF9: 0F FC           CLR     $FC                   
CFFB: 0F FC           CLR     $FC                   
CFFD: 0F FF           CLR     $FF                   
CFFF: 0F FC           CLR     $FC                   
D001: 0F FD           CLR     $FD                   
D003: 0F FD           CLR     $FD                   
D005: 0F FF           CLR     $FF                   
D007: 0F EE           CLR     $EE                   
D009: 1F A8           TFR     CC,A                   
D00B: 37 EC           PULU    B,DP,Y,S,PC                   
D00D: 27 C4           BEQ     $CFD3                   
D00F: 32 ; ????
D010: EF 31           STU     -15,Y               
D012: FF 0F E6        STU     $0FE6                   
D015: 02 ; ????
D016: FE 0F D1        LDU     $0FD1                   
D019: 37 E1           PULU    CC,Y,S,PC                   
D01B: 01 ; ????
D01C: E9 39           ADCB    -7,Y                
D01E: E8 3E           EORB    -2,Y                
D020: FC 0F FD        LDD     $0FFD                   
D023: 0F FE           CLR     $FE                   
D025: 0F FF           CLR     $FF                   
D027: 0F D9           CLR     $D9                   
D029: 39              RTS                         
D02A: E0 01           SUBB    1,X                 
D02C: D7 33           STB     $33                   
D02E: D8 31           EORB    $31                   
D030: FC 0F FD        LDD     $0FFD                   
D033: 0F FD           CLR     $FD                   
D035: 0F FF           CLR     $FF                   
D037: 0F D6           CLR     $D6                   
D039: 1F D7           TFR     ?,?                   
D03B: 37 D4           PULU    B,X,S,PC                   
D03D: 17 D5 31        LBSR    $A571                   
D040: D6 1E           LDB     $1E                   
D042: FF 0F D6        STU     $0FD6                   
D045: 3F              SWI                         
D046: FC 0F FF        LDD     $0FFF                   
D049: 0F FC           CLR     $FC                   
D04B: 0F E0           CLR     $E0                   
D04D: 01 ; ????
D04E: FD 0F FE        STD     $0FFE                   
D051: 0F FD           CLR     $FD                   
D053: 0F FE           CLR     $FE                   
D055: 0F FC           CLR     $FC                   
D057: 0F E1           CLR     $E1                   
D059: 31 E1           LEAY    ,S++                
D05B: 01 ; ????
D05C: E2 37           SBCB    -9,Y                
D05E: E2 01           SBCB    1,X                 
D060: FF 0F FE        STU     $0FFE                   
D063: 0F FC           CLR     $FC                   
D065: 0F FD           CLR     $FD                   
D067: 0F A1           CLR     $A1                   
D069: 32 A5           LEAS    B,Y                 
D06B: 31 A1           LEAY    ,Y++                
D06D: 33 7B           LEAU    -5,S                
D06F: 31 ; ????
D070: FE 0F FD        LDU     $0FFD                   
D073: 0F FF           CLR     $FF                   
D075: 0F FC           CLR     $FC                   
D077: 0F A0           CLR     $A0                   
D079: 33 7A           LEAU    -6,S                
D07B: 31 A0           LEAY    ,Y+                 
D07D: 32 A2           LEAS    ,-Y                 
D07F: 31 FF 0F FF     LEAY    [$0FFF]                 
D083: 0F FF           CLR     $FF                   
D085: 0F FF           CLR     $FF                   
D087: 0F A8           CLR     $A8                   
D089: 38 ; ????
D08A: AC 39           CMPX    -7,Y                
D08C: 7C 38 88        INC     $3888                   
D08F: 31 FC 0F        LEAY    [$D0A1,PC]              
D092: FD 0F FD        STD     $0FFD                   
D095: 0F FD           CLR     $FD                   
D097: 0F 7C           CLR     $7C                   
D099: 32 80           LEAS    ,X+                 
D09B: 31 A6           LEAY    A,Y                 
D09D: 37 A9           PULU    CC,DP,Y,PC                   
D09F: 39              RTS                         
D0A0: FF 0F FF        STU     $0FFF                   
D0A3: 0F FF           CLR     $FF                   
D0A5: 0F FF           CLR     $FF                   
D0A7: 0F A1           CLR     $A1                   
D0A9: 32 A5           LEAS    B,Y                 
D0AB: 31 A1           LEAY    ,Y++                
D0AD: 33 7B           LEAU    -5,S                
D0AF: 31 ; ????
D0B0: FE 0F FD        LDU     $0FFD                   
D0B3: 0F FF           CLR     $FF                   
D0B5: 0F FC           CLR     $FC                   
D0B7: 0F A0           CLR     $A0                   
D0B9: 33 7A           LEAU    -6,S                
D0BB: 31 A0           LEAY    ,Y+                 
D0BD: 32 A2           LEAS    ,-Y                 
D0BF: 31 FF 0F FF     LEAY    [$0FFF]                 
D0C3: 0F FF           CLR     $FF                   
D0C5: 0F FF           CLR     $FF                   
D0C7: 0F A8           CLR     $A8                   
D0C9: 38 ; ????
D0CA: AC 39           CMPX    -7,Y                
D0CC: 7C 38 88        INC     $3888                   
D0CF: 31 FC 0F        LEAY    [$D0E1,PC]              
D0D2: FD 0F FD        STD     $0FFD                   
D0D5: 0F FD           CLR     $FD                   
D0D7: 0F 7C           CLR     $7C                   
D0D9: 32 80           LEAS    ,X+                 
D0DB: 31 A6           LEAY    A,Y                 
D0DD: 37 A9           PULU    CC,DP,Y,PC                   
D0DF: 39              RTS                         
D0E0: FF 0F FF        STU     $0FFF                   
D0E3: 0F FF           CLR     $FF                   
D0E5: 0F FF           CLR     $FF                   
D0E7: 0F 68           CLR     $68                   
D0E9: 90 6C           SUBA    $6C                   
D0EB: 90 64           SUBA    $64                   
D0ED: 90 0F           SUBA    $0F                   
D0EF: 90 68           SUBA    $68                   
D0F1: 90 6C           SUBA    $6C                   
D0F3: 90 CC           SUBA    $CC                   
D0F5: A5 C3           BITA    ,--U                
D0F7: A7 68           STA     8,S                 
D0F9: 90 0E           SUBA    $0E                   
D0FB: 90 F0           SUBA    $F0                   
D0FD: A5 AD 97 C1     BITA    $68C2,PC                
D101: A5 ; ????
D102: 87 ; ????
D103: B3 AE BD        SUBD    $AEBD                   
D106: C0 BE           SUBB    #$BE                  
D108: A3 A5           SUBD    B,Y                 
D10A: D3 97           ADDD    $97                   
D10C: 64 ; ????
D10D: 90 0E           SUBA    $0E                   
D10F: 90 D1           SUBA    $D1                   
D111: BD D0 95        JSR     $D095                   
D114: AF A5           STX     B,Y                 
D116: CB B7           ADDB    #$B7                  
D118: 68 ; ????
D119: 90 0F           SUBA    $0F                   
D11B: 90 64           SUBA    $64                   
D11D: 90 60           SUBA    $60                   
D11F: 90 0E           SUBA    $0E                   
D121: 90 CC           SUBA    $CC                   
D123: AD 64           JSR     4,S                 
D125: 90 60           SUBA    $60                   
D127: 90 68           SUBA    $68                   
D129: 90 6C           SUBA    $6C                   
D12B: 90 64           SUBA    $64                   
D12D: 90 0B           SUBA    $0B                   
D12F: A7 8C 85        STA     $D0B7,PC                
D132: 87 ; ????
D133: B9 E5 A7        ADCA    $E5A7                   
D136: E6 ; ????
D137: B7 68 90        STA     $6890                   
D13A: 0A A7           DEC     $A7                   
D13C: A4 A5           ANDA    B,Y                 
D13E: 8B B1           ADDA    #$B1                  
D140: E3 ; ????
D141: B2 CD 84        SBCA    $CD84                   
D144: ED B1           STD     [,Y++]              
D146: E3 ; ????
D147: 9E 68           LDX     $68                   
D149: 90 6C           SUBA    $6C                   
D14B: 90 64           SUBA    $64                   
D14D: 90 0E           SUBA    $0E                   
D14F: 90 68           SUBA    $68                   
D151: 90 6C           SUBA    $6C                   
D153: 90 0F           SUBA    $0F                   
D155: 90 EB           SUBA    $EB                   
D157: A7 68           STA     8,S                 
D159: 90 0F           SUBA    $0F                   
D15B: 90 64           SUBA    $64                   
D15D: 90 60           SUBA    $60                   
D15F: 90 77           SUBA    $77                   
D161: A7 E8 AB        STA     $AB,S                 
D164: 8F ; ????
D165: AD EA B9        JSR     $B9,X                 
D168: 68 ; ????
D169: 90 6C           SUBA    $6C                   
D16B: 90 64           SUBA    $64                   
D16D: 90 0E           SUBA    $0E                   
D16F: 90 8E           SUBA    $8E                   
D171: A5 84           BITA    ,X                  
D173: B1 73 A7        CMPA    $73A7                   
D176: DA B7           ORB     $B7                   
D178: 68 ; ????
D179: 90 0F           SUBA    $0F                   
D17B: 90 64           SUBA    $64                   
D17D: 90 60           SUBA    $60                   
D17F: 90 72           SUBA    $72                   
D181: A7 DB           STA     [D,U]               
D183: AD 64           JSR     4,S                 
D185: 90 60           SUBA    $60                   
D187: 90 A7           SUBA    $A7                   
D189: A5 83           BITA    ,--X                
D18B: AB 64           ADDA    4,S                 
D18D: 90 0D           SUBA    $0D                   
D18F: A7 E0           STA     ,S+                 
D191: B1 CA 81        CMPA    $CA81                   
D194: DF A7           STU     $A7                   
D196: DE B7           LDU     $B7                   
D198: 68 ; ????
D199: 90 0C           SUBA    $0C                   
D19B: A7 64           STA     4,S                 
D19D: 90 60           SUBA    $60                   
D19F: 90 DD           SUBA    $DD                   
D1A1: A7 ; ????
D1A2: DE B3           LDU     $B3                   
D1A4: 64 ; ????
D1A5: 90 DC           SUBA    $DC                   
D1A7: BB B0 AC        ADDA    $B0AC                   
D1AA: 6C ; ????
D1AB: 90 B1           SUBA    $B1                   
D1AD: 87 ; ????
D1AE: B2 87 68        SBCA    $8768                   
D1B1: 90 6C           SUBA    $6C                   
D1B3: 90 0E           SUBA    $0E                   
D1B5: 90 60           SUBA    $60                   
D1B7: 90 FE           SUBA    $FE                   
D1B9: 8F ; ????
D1BA: B3 87 FD        SUBD    $87FD                   
D1BD: 8F ; ????
D1BE: FF 8F 0F        STU     $8F0F                   
D1C1: 90 6C           SUBA    $6C                   
D1C3: 90 B4           SUBA    $B4                   
D1C5: 87 ; ????
D1C6: B5 AC FC        BITA    $ACFC                   
D1C9: 8F ; ????
D1CA: FE 8F FD        LDU     $8FFD                   
D1CD: 8F ; ????
D1CE: BA 87 BB        ORA     $87BB                   
D1D1: 87 ; ????
D1D2: BC AC 0E        CMPX    $AC0E                   
D1D5: 90 60           SUBA    $60                   
D1D7: 90 B9           SUBA    $B9                   
D1D9: 87 ; ????
D1DA: 0E 90           JMP     $90                   
D1DC: B8 AC 60        EORA    $AC60                   
D1DF: 90 0F           SUBA    $0F                   
D1E1: 90 6C           SUBA    $6C                   
D1E3: 90 64           SUBA    $64                   
D1E5: 90 60           SUBA    $60                   
D1E7: 90 68           SUBA    $68                   
D1E9: 90 6C           SUBA    $6C                   
D1EB: 90 64           SUBA    $64                   
D1ED: 90 0F           SUBA    $0F                   
D1EF: 90 68           SUBA    $68                   
D1F1: 90 6C           SUBA    $6C                   
D1F3: 90 0E           SUBA    $0E                   
D1F5: 90 60           SUBA    $60                   
D1F7: 90 68           SUBA    $68                   
D1F9: 90 0E           SUBA    $0E                   
D1FB: 90 64           SUBA    $64                   
D1FD: 90 60           SUBA    $60                   
D1FF: 90 0F           SUBA    $0F                   
D201: 90 6C           SUBA    $6C                   
D203: 90 64           SUBA    $64                   
D205: 90 60           SUBA    $60                   
D207: 90 68           SUBA    $68                   
D209: 90 6C           SUBA    $6C                   
D20B: 90 64           SUBA    $64                   
D20D: 90 0F           SUBA    $0F                   
D20F: 90 68           SUBA    $68                   
D211: 90 6C           SUBA    $6C                   
D213: 90 0E           SUBA    $0E                   
D215: 90 60           SUBA    $60                   
D217: 90 68           SUBA    $68                   
D219: 90 0E           SUBA    $0E                   
D21B: 90 64           SUBA    $64                   
D21D: 90 60           SUBA    $60                   
D21F: 90 0F           SUBA    $0F                   
D221: 90 6C           SUBA    $6C                   
D223: 90 64           SUBA    $64                   
D225: 90 60           SUBA    $60                   
D227: 90 FC           SUBA    $FC                   
D229: 8F ; ????
D22A: FD 8F FE        STD     $8FFE                   
D22D: 8F ; ????
D22E: FF 8F FD        STU     $8FFD                   
D231: 8F ; ????
D232: FD 8F FC        STD     $8FFC                   
D235: 8F ; ????
D236: FE 8F FF        LDU     $8FFF                   
D239: 8F ; ????
D23A: FE 8F FC        LDU     $8FFC                   
D23D: 8F ; ????
D23E: FD 8F FE        STD     $8FFE                   
D241: 8F ; ????
D242: FF 8F FF        STU     $8FFF                   
D245: 8F ; ????
D246: FC 8F C6        LDD     $8FC6                   
D249: AB ; ????
D24A: C7 ; ????
D24B: B4 C4 A7        ANDA    $C4A7                   
D24E: C5 B1           BITB    #$B1                  
D250: C8 B1           EORB    #$B1                  
D252: FC 8F C4        LDD     $8FC4                   
D255: BE FD 8F        LDX     $FD8F                   
D258: C2 B1           SBCB    #$B1                  
D25A: C1 BF           CMPB    #$BF                  
D25C: FC 8F FE        LDD     $8FFE                   
D25F: 8F ; ????
D260: FC 8F FE        LDD     $8FFE                   
D263: 8F ; ????
D264: FF 8F FD        STU     $8FFD                   
D267: 8F ; ????
D268: D0 AF           SUBB    $AF                   
D26A: FC 8F CE        LDD     $8FCE                   
D26D: B1 CF B1        CMPA    $CFB1                   
D270: FE 8F FD        LDU     $8FFD                   
D273: 8F ; ????
D274: CD ; ????
D275: AE FC 8F        LDX     [$D207,PC]              
D278: CB B3           ADDB    #$B3                  
D27A: C0 B2           SUBB    #$B2                  
D27C: C9 AB           ADCB    #$AB                  
D27E: CA AB           ORB     #$AB                  
D280: CD ; ????
D281: B6 FE 8F        LDA     $FE8F                   
D284: C2 BF           SBCB    #$BF                  
D286: FF 8F E7        STU     $8FE7                   
D289: B9 FC 8F        ADCA    $FC8F                   
D28C: E6 ; ????
D28D: AF FF 8F FD     STX     [$8FFD]                 
D291: 8F ; ????
D292: FE 8F FF        LDU     $8FFF                   
D295: 8F ; ????
D296: FC 8F FE        LDD     $8FFE                   
D299: 8F ; ????
D29A: FC 8F FC        LDD     $8FFC                   
D29D: 8F ; ????
D29E: FF 8F FC        STU     $8FFC                   
D2A1: 8F ; ????
D2A2: FD 8F FD        STD     $8FFD                   
D2A5: 8F ; ????
D2A6: FF 8F EE        STU     $8FEE                   
D2A9: 9F A8           STX     $A8                   
D2AB: B7 EC A7        STA     $ECA7                   
D2AE: C4 B2           ANDB    #$B2                  
D2B0: EF B1           STU     [,Y++]              
D2B2: FF 8F E6        STU     $8FE6                   
D2B5: 82 FE           SBCA    #$FE                  
D2B7: 8F ; ????
D2B8: D1 B7           CMPB    $B7                   
D2BA: E1 81           CMPB    ,X++                
D2BC: E9 B9 E8 BE     ADCB    [$E8BE,Y]               
D2C0: FC 8F FD        LDD     $8FFD                   
D2C3: 8F ; ????
D2C4: FE 8F FF        LDU     $8FFF                   
D2C7: 8F ; ????
D2C8: D9 B9           ADCB    $B9                   
D2CA: E0 81           SUBB    ,X++                
D2CC: D7 B3           STB     $B3                   
D2CE: D8 B1           EORB    $B1                   
D2D0: FC 8F FD        LDD     $8FFD                   
D2D3: 8F ; ????
D2D4: FD 8F FF        STD     $8FFF                   
D2D7: 8F ; ????
D2D8: D6 9F           LDB     $9F                   
D2DA: D7 B7           STB     $B7                   
D2DC: D4 97           ANDB    $97                   
D2DE: D5 B1           BITB    $B1                   
D2E0: D6 9E           LDB     $9E                   
D2E2: FF 8F D6        STU     $8FD6                   
D2E5: BF FC 8F        STX     $FC8F                   
D2E8: FF 8F FC        STU     $8FFC                   
D2EB: 8F ; ????
D2EC: E0 81           SUBB    ,X++                
D2EE: FD 8F FE        STD     $8FFE                   
D2F1: 8F ; ????
D2F2: FD 8F FE        STD     $8FFE                   
D2F5: 8F ; ????
D2F6: FC 8F E1        LDD     $8FE1                   
D2F9: B1 E1 81        CMPA    $E181                   
D2FC: E2 ; ????
D2FD: B7 E2 81        STA     $E281                   
D300: FF 8F FE        STU     $8FFE                   
D303: 8F ; ????
D304: FC 8F FD        LDD     $8FFD                   
D307: 8F ; ????
D308: A1 ; ????
D309: B2 A5 B1        SBCA    $A5B1                   
D30C: A1 B3           CMPA    [,--Y]              
D30E: 7B ; ????
D30F: B1 FE 8F        CMPA    $FE8F                   
D312: FD 8F FF        STD     $8FFF                   
D315: 8F ; ????
D316: FC 8F A0        LDD     $8FA0                   
D319: B3 7A B1        SUBD    $7AB1                   
D31C: A0 ; ????
D31D: B2 A2 B1        SBCA    $A2B1                   
D320: FF 8F FF        STU     $8FFF                   
D323: 8F ; ????
D324: FF 8F FF        STU     $8FFF                   
D327: 8F ; ????
D328: A8 B8 AC        EORA    [$AC,Y]               
D32B: B9 7C B8        ADCA    $7CB8                   
D32E: 88 B1           EORA    #$B1                  
D330: FC 8F FD        LDD     $8FFD                   
D333: 8F ; ????
D334: FD 8F FD        STD     $8FFD                   
D337: 8F ; ????
D338: 7C B2 80        INC     $B280                   
D33B: B1 A6 B7        CMPA    $A6B7                   
D33E: A9 B9 FF 8F     ADCA    [$FF8F,Y]               
D342: FF 8F FF        STU     $8FFF                   
D345: 8F ; ????
D346: FF 8F A1        STU     $8FA1                   
D349: B2 A5 B1        SBCA    $A5B1                   
D34C: A1 B3           CMPA    [,--Y]              
D34E: 7B ; ????
D34F: B1 FE 8F        CMPA    $FE8F                   
D352: FD 8F FF        STD     $8FFF                   
D355: 8F ; ????
D356: FC 8F A0        LDD     $8FA0                   
D359: B3 7A B1        SUBD    $7AB1                   
D35C: A0 ; ????
D35D: B2 A2 B1        SBCA    $A2B1                   
D360: FF 8F FF        STU     $8FFF                   
D363: 8F ; ????
D364: FF 8F FF        STU     $8FFF                   
D367: 8F ; ????
D368: A8 B8 AC        EORA    [$AC,Y]               
D36B: B9 7C B8        ADCA    $7CB8                   
D36E: 88 B1           EORA    #$B1                  
D370: FC 8F FD        LDD     $8FFD                   
D373: 8F ; ????
D374: FD 8F FD        STD     $8FFD                   
D377: 8F ; ????
D378: 7C B2 80        INC     $B280                   
D37B: B1 A6 B7        CMPA    $A6B7                   
D37E: A9 B9 FF 8F     ADCA    [$FF8F,Y]               
D382: FF 8F FF        STU     $8FFF                   
D385: 8F ; ????
D386: FF 8F 00        STU     $8F00                   
D389: 00 00           NEG     $00                   
D38B: 04 00           LSR     $00                   
D38D: 08 ; ????
D38E: 00 0C           NEG     $0C                   
D390: 00 10           NEG     $10                   
D392: 00 14           NEG     $14                   
D394: 00 18           NEG     $18                   
D396: 00 1C           NEG     $1C                   
D398: 00 80           NEG     $80                   
D39A: 00 84           NEG     $84                   
D39C: 00 88           NEG     $88                   
D39E: 00 8C           NEG     $8C                   
D3A0: 00 90           NEG     $90                   
D3A2: 00 94           NEG     $94                   
D3A4: 00 98           NEG     $98                   
D3A6: 00 9C           NEG     $9C                   
D3A8: 01 ; ????
D3A9: 00 01           NEG     $01                   
D3AB: 04 01           LSR     $01                   
D3AD: 08 ; ????
D3AE: 01 ; ????
D3AF: 0C 01           INC     $01                   
D3B1: 10 ; ????
D3B2: 01 ; ????
D3B3: 14 ; ????
D3B4: 01 ; ????
D3B5: 18 ; ????
D3B6: 01 ; ????
D3B7: 1C 01           ANDCC   #$01                  
D3B9: 80 01           SUBA    #$01                  
D3BB: 84 01           ANDA    #$01                  
D3BD: 88 01           EORA    #$01                  
D3BF: 8C 01 90        CMPX    #$0190                  
D3C2: 01 ; ????
D3C3: 94 01           ANDA    $01                   
D3C5: 98 01           EORA    $01                   
D3C7: 9C 02           CMPX    $02                   
D3C9: 00 02           NEG     $02                   
D3CB: 04 02           LSR     $02                   
D3CD: 08 ; ????
D3CE: 02 ; ????
D3CF: 0C 02           INC     $02                   
D3D1: 10 ; ????
D3D2: 02 ; ????
D3D3: 14 ; ????
D3D4: 02 ; ????
D3D5: 18 ; ????
D3D6: 02 ; ????
D3D7: 1C 02           ANDCC   #$02                  
D3D9: 80 02           SUBA    #$02                  
D3DB: 84 02           ANDA    #$02                  
D3DD: 88 02           EORA    #$02                  
D3DF: 8C 02 90        CMPX    #$0290                  
D3E2: 02 ; ????
D3E3: 94 02           ANDA    $02                   
D3E5: 98 02           EORA    $02                   
D3E7: 9C 03           CMPX    $03                   
D3E9: 00 03           NEG     $03                   
D3EB: 04 03           LSR     $03                   
D3ED: 08 ; ????
D3EE: 03 0C           COM     $0C                   
D3F0: 03 10           COM     $10                   
D3F2: 03 14           COM     $14                   
D3F4: 03 18           COM     $18                   
D3F6: 03 1C           COM     $1C                   
D3F8: 03 80           COM     $80                   
D3FA: 03 84           COM     $84                   
D3FC: 03 88           COM     $88                   
D3FE: 03 8C           COM     $8C                   
D400: 03 90           COM     $90                   
D402: 03 94           COM     $94                   
D404: 03 98           COM     $98                   
D406: 03 9C           COM     $9C                   
D408: 04 00           LSR     $00                   
D40A: 04 04           LSR     $04                   
D40C: 04 08           LSR     $08                   
D40E: 04 0C           LSR     $0C                   
D410: 04 10           LSR     $10                   
D412: 04 14           LSR     $14                   
D414: 04 18           LSR     $18                   
D416: 04 1C           LSR     $1C                   
D418: 04 80           LSR     $80                   
D41A: 04 84           LSR     $84                   
D41C: 04 88           LSR     $88                   
D41E: 04 8C           LSR     $8C                   
D420: 04 90           LSR     $90                   
D422: 04 94           LSR     $94                   
D424: 04 98           LSR     $98                   
D426: 04 9C           LSR     $9C                   
D428: 05 ; ????
D429: 00 05           NEG     $05                   
D42B: 04 05           LSR     $05                   
D42D: 08 ; ????
D42E: 05 ; ????
D42F: 0C 05           INC     $05                   
D431: 10 ; ????
D432: 05 ; ????
D433: 14 ; ????
D434: 05 ; ????
D435: 18 ; ????
D436: 05 ; ????
D437: 1C 05           ANDCC   #$05                  
D439: 80 05           SUBA    #$05                  
D43B: 84 05           ANDA    #$05                  
D43D: 88 05           EORA    #$05                  
D43F: 8C 05 90        CMPX    #$0590                  
D442: 05 ; ????
D443: 94 05           ANDA    $05                   
D445: 98 05           EORA    $05                   
D447: 9C 06           CMPX    $06                   
D449: 00 06           NEG     $06                   
D44B: 04 06           LSR     $06                   
D44D: 08 ; ????
D44E: 06 0C           ROR     $0C                   
D450: 06 10           ROR     $10                   
D452: 06 14           ROR     $14                   
D454: 06 18           ROR     $18                   
D456: 06 1C           ROR     $1C                   
D458: 06 80           ROR     $80                   
D45A: 06 84           ROR     $84                   
D45C: 06 88           ROR     $88                   
D45E: 06 8C           ROR     $8C                   
D460: 06 90           ROR     $90                   
D462: 06 94           ROR     $94                   
D464: 06 98           ROR     $98                   
D466: 06 9C           ROR     $9C                   
D468: 07 00           ASR     $00                   
D46A: 07 04           ASR     $04                   
D46C: 07 08           ASR     $08                   
D46E: 07 0C           ASR     $0C                   
D470: 07 10           ASR     $10                   
D472: 07 14           ASR     $14                   
D474: 07 18           ASR     $18                   
D476: 07 1C           ASR     $1C                   
D478: 00 E7           NEG     $E7                   
D47A: 00 EB           NEG     $EB                   
D47C: 00 EF           NEG     $EF                   
D47E: 00 F3           NEG     $F3                   
D480: 00 F7           NEG     $F7                   
D482: 01 ; ????
D483: 67 01           ASR     1,X                 
D485: 6B ; ????
D486: 01 ; ????
D487: 6F 01           CLR     1,X                 
D489: 73 01 77        COM     $0177                   
D48C: 01 ; ????
D48D: E7 01           STB     1,X                 
D48F: EB 01           ADDB    1,X                 
D491: EF 01           STU     1,X                 
D493: F3 01 F7        ADDD    $01F7                   
D496: 02 ; ????
D497: 67 02           ASR     2,X                 
D499: 6B ; ????
D49A: 02 ; ????
D49B: 6F 02           CLR     2,X                 
D49D: 73 02 77        COM     $0277                   
D4A0: 02 ; ????
D4A1: E7 02           STB     2,X                 
D4A3: EB 02           ADDB    2,X                 
D4A5: EF 02           STU     2,X                 
D4A7: F3 02 F7        ADDD    $02F7                   
D4AA: 03 67           COM     $67                   
D4AC: 03 6B           COM     $6B                   
D4AE: 03 6F           COM     $6F                   
D4B0: 03 73           COM     $73                   
D4B2: 03 77           COM     $77                   
D4B4: 03 E7           COM     $E7                   
D4B6: 03 EB           COM     $EB                   
D4B8: 03 EF           COM     $EF                   
D4BA: 03 F3           COM     $F3                   
D4BC: 03 F7           COM     $F7                   
D4BE: 04 67           LSR     $67                   
D4C0: 04 6B           LSR     $6B                   
D4C2: 04 6F           LSR     $6F                   
D4C4: 04 73           LSR     $73                   
D4C6: 04 77           LSR     $77                   
D4C8: 04 E7           LSR     $E7                   
D4CA: 04 EB           LSR     $EB                   
D4CC: 04 EF           LSR     $EF                   
D4CE: 04 F3           LSR     $F3                   
D4D0: 04 F7           LSR     $F7                   
D4D2: 05 ; ????
D4D3: 67 05           ASR     5,X                 
D4D5: 6B ; ????
D4D6: 05 ; ????
D4D7: 6F 05           CLR     5,X                 
D4D9: 73 05 77        COM     $0577                   
D4DC: 05 ; ????
D4DD: E7 05           STB     5,X                 
D4DF: EB 05           ADDB    5,X                 
D4E1: EF 05           STU     5,X                 
D4E3: F3 05 F7        ADDD    $05F7                   
D4E6: 06 67           ROR     $67                   
D4E8: 06 6B           ROR     $6B                   
D4EA: 06 6F           ROR     $6F                   
D4EC: 06 73           ROR     $73                   
D4EE: 06 77           ROR     $77                   
D4F0: AA ; ????
D4F1: AA ; ????
D4F2: AA ; ????
D4F3: AA ; ????
D4F4: A7 88 88        STA     $88,X                 
D4F7: 1B ; ????
D4F8: A8 88 88        EORA    $88,X                 
D4FB: 8B A8           ADDA    #$A8                  
D4FD: 88 88           EORA    #$88                  
D4FF: 8B A8           ADDA    #$A8                  
D501: 88 88           EORA    #$88                  
D503: 8B A8           ADDA    #$A8                  
D505: 88 88           EORA    #$88                  
D507: 8B A8           ADDA    #$A8                  
D509: 88 88           EORA    #$88                  
D50B: 8B A8           ADDA    #$A8                  
D50D: 88 88           EORA    #$88                  
D50F: 8B AA           ADDA    #$AA                  
D511: AA ; ????
D512: AA ; ????
D513: AA ; ????
D514: AA ; ????
D515: AA ; ????
D516: AA ; ????
D517: AA ; ????
D518: AA ; ????
D519: AA ; ????
D51A: AA ; ????
D51B: AA ; ????
D51C: AA ; ????
D51D: AA ; ????
D51E: AA ; ????
D51F: AA ; ????
D520: AA ; ????
D521: AA ; ????
D522: AA ; ????
D523: AA ; ????
D524: AA ; ????
D525: AA ; ????
D526: AA ; ????
D527: AA ; ????
D528: AA ; ????
D529: AA ; ????
D52A: AA ; ????
D52B: AA A8 8B        ORA     $8B,Y                 
D52E: 88 BA           EORA    #$BA                  
D530: A8 8B           EORA    D,X                 
D532: 88 BA           EORA    #$BA                  
D534: A8 88 88        EORA    $88,X                 
D537: BA AA 88        ORA     $AA88                   
D53A: 8B AA           ADDA    #$AA                  
D53C: A8 88 88        EORA    $88,X                 
D53F: BA A8 8B        ORA     $A88B                   
D542: 88 BA           EORA    #$BA                  
D544: A8 8B           EORA    D,X                 
D546: 88 BA           EORA    #$BA                  
D548: AA ; ????
D549: AA ; ????
D54A: AA ; ????
D54B: AA ; ????
D54C: AA ; ????
D54D: AA ; ????
D54E: AA ; ????
D54F: AA ; ????
D550: AA ; ????
D551: AA ; ????
D552: AA ; ????
D553: AA ; ????
D554: AA ; ????
D555: AA ; ????
D556: AA ; ????
D557: AA ; ????
D558: AA ; ????
D559: AA ; ????
D55A: AA ; ????
D55B: AA ; ????
D55C: AA ; ????
D55D: AA ; ????
D55E: AA ; ????
D55F: AA ; ????
D560: AA ; ????
D561: AA ; ????
D562: AA ; ????
D563: AA ; ????
D564: AA 88 88        ORA     $88,X                 
D567: 1B ; ????
D568: A8 88 88        EORA    $88,X                 
D56B: 8B A8           ADDA    #$A8                  
D56D: 88 88           EORA    #$88                  
D56F: 8B A8           ADDA    #$A8                  
D571: 88 88           EORA    #$88                  
D573: 8B A8           ADDA    #$A8                  
D575: 88 88           EORA    #$88                  
D577: 8B A8           ADDA    #$A8                  
D579: 88 88           EORA    #$88                  
D57B: 8B AA           ADDA    #$AA                  
D57D: AA ; ????
D57E: AA ; ????
D57F: AA ; ????
D580: AA ; ????
D581: AA ; ????
D582: AA ; ????
D583: AA ; ????
D584: AA ; ????
D585: AA ; ????
D586: AA ; ????
D587: AA ; ????
D588: AA ; ????
D589: AA ; ????
D58A: AA ; ????
D58B: AA ; ????
D58C: AA ; ????
D58D: AA ; ????
D58E: AA ; ????
D58F: AA ; ????
D590: AA ; ????
D591: AA ; ????
D592: AA ; ????
D593: AA ; ????
D594: AA ; ????
D595: AA ; ????
D596: AA ; ????
D597: AA ; ????
D598: AA ; ????
D599: AA ; ????
D59A: AA ; ????
D59B: AA A8 88        ORA     $88,Y                 
D59E: 88 8B           EORA    #$8B                  
D5A0: A8 88 88        EORA    $88,X                 
D5A3: 8B A8           ADDA    #$A8                  
D5A5: 88 88           EORA    #$88                  
D5A7: 8B AA           ADDA    #$AA                  
D5A9: 88 88           EORA    #$88                  
D5AB: BA A8 88        ORA     $A888                   
D5AE: 88 8B           EORA    #$8B                  
D5B0: A8 88 88        EORA    $88,X                 
D5B3: 8B A8           ADDA    #$A8                  
D5B5: 88 88           EORA    #$88                  
D5B7: 8B AA           ADDA    #$AA                  
D5B9: AA ; ????
D5BA: AA ; ????
D5BB: AA ; ????
D5BC: AA ; ????
D5BD: AA ; ????
D5BE: AA ; ????
D5BF: AA ; ????
D5C0: AA ; ????
D5C1: AA ; ????
D5C2: AA ; ????
D5C3: AA ; ????
D5C4: AA ; ????
D5C5: AA ; ????
D5C6: AA ; ????
D5C7: AA ; ????
D5C8: AA ; ????
D5C9: AA ; ????
D5CA: AA ; ????
D5CB: AA ; ????
D5CC: AA ; ????
D5CD: AA ; ????
D5CE: AA ; ????
D5CF: AA ; ????
D5D0: AA ; ????
D5D1: AA ; ????
D5D2: AA ; ????
D5D3: AA ; ????
D5D4: AA 78           ORA     -8,S                
D5D6: 88 8B           EORA    #$8B                  
D5D8: AA 88 88        ORA     $88,X                 
D5DB: 8B AA           ADDA    #$AA                  
D5DD: 88 88           EORA    #$88                  
D5DF: 8B AA           ADDA    #$AA                  
D5E1: A8 88 8B        EORA    $8B,X                 
D5E4: A8 88 BA        EORA    $BA,X                 
D5E7: 8B A8           ADDA    #$A8                  
D5E9: B8 8B 8B        EORA    $8B8B                   
D5EC: A8 B8 8B        EORA    [$8B,Y]               
D5EF: 8B A8           ADDA    #$A8                  
D5F1: 1B ; ????
D5F2: A7 8B           STA     D,X                 
D5F4: A6 88 88        LDA     $88,X                 
D5F7: 0B ; ????
D5F8: AA ; ????
D5F9: AA ; ????
D5FA: AA ; ????
D5FB: AA ; ????
D5FC: AA ; ????
D5FD: AA ; ????
D5FE: AA ; ????
D5FF: AA ; ????
D600: AA ; ????
D601: AA ; ????
D602: AA ; ????
D603: AA ; ????
D604: AA ; ????
D605: AA ; ????
D606: AA ; ????
D607: AA ; ????
D608: AA ; ????
D609: AA ; ????
D60A: AA ; ????
D60B: AA ; ????
D60C: AA ; ????
D60D: AA ; ????
D60E: AA 7B           ORA     -5,S                
D610: AA ; ????
D611: AA ; ????
D612: A7 8B           STA     D,X                 
D614: AA ; ????
D615: AA 78           ORA     -8,S                
D617: 8B AA           ADDA    #$AA                  
D619: A7 88 8B        STA     $8B,X                 
D61C: AA 78           ORA     -8,S                
D61E: 88 0B           EORA    #$0B                  
D620: A7 80           STA     ,X+                 
D622: B8 BA A8        EORA    $BAA8                   
D625: 8B A8           ADDA    #$A8                  
D627: BA A6 81        ORA     $A681                   
D62A: B8 BA AA        EORA    $BAAA                   
D62D: 68 ; ????
D62E: 88 1B           EORA    #$1B                  
D630: AA A6           ORA     A,Y                 
D632: 88 8B           EORA    #$8B                  
D634: AA ; ????
D635: AA 68           ORA     8,S                 
D637: 8B AA           ADDA    #$AA                  
D639: AA A6           ORA     A,Y                 
D63B: 8B AA           ADDA    #$AA                  
D63D: AA ; ????
D63E: AA 6B           ORA     11,S                
D640: AA ; ????
D641: AA ; ????
D642: AA ; ????
D643: AA A8 88        ORA     $88,Y                 
D646: 88 8B           EORA    #$8B                  
D648: A8 88 88        EORA    $88,X                 
D64B: 8B A8           ADDA    #$A8                  
D64D: 88 88           EORA    #$88                  
D64F: 8B A8           ADDA    #$A8                  
D651: 88 88           EORA    #$88                  
D653: 8B AA           ADDA    #$AA                  
D655: A7 88 8B        STA     $8B,X                 
D658: AA 78           ORA     -8,S                
D65A: B8 8B A7        EORA    $8BA7                   
D65D: 88 88           EORA    #$88                  
D65F: 0B ; ????
D660: A8 8B           EORA    D,X                 
D662: 80 BA           SUBA    #$BA                  
D664: A8 88 0B        EORA    $0B,X                 
D667: AA A8 88        ORA     $88,Y                 
D66A: 88 8B           EORA    #$8B                  
D66C: A8 88 88        EORA    $88,X                 
D66F: 8B A8           ADDA    #$A8                  
D671: 88 88           EORA    #$88                  
D673: 8B A8           ADDA    #$A8                  
D675: 88 88           EORA    #$88                  
D677: 8B AA           ADDA    #$AA                  
D679: AA ; ????
D67A: AA ; ????
D67B: AA ; ????
D67C: A7 88 88        STA     $88,X                 
D67F: 8B A8           ADDA    #$A8                  
D681: 88 88           EORA    #$88                  
D683: 8B A8           ADDA    #$A8                  
D685: 88 0B           EORA    #$0B                  
D687: AA A8 80        ORA     $80,Y                 
D68A: B7 1B A8        STA     $1BA8                   
D68D: 8B 78           ADDA    #$78                  
D68F: 8B A8           ADDA    #$A8                  
D691: 88 88           EORA    #$88                  
D693: 8B A6           ADDA    #$A6                  
D695: 88 88           EORA    #$88                  
D697: 3B              RTI                         
D698: AA 88 88        ORA     $88,X                 
D69B: 2B A7           BMI     $D644                   
D69D: 88 8B           EORA    #$8B                  
D69F: AA A8 88        ORA     $88,Y                 
D6A2: 88 1B           EORA    #$1B                  
D6A4: A8 8B           EORA    D,X                 
D6A6: 88 8B           EORA    #$8B                  
D6A8: A8 8B           EORA    D,X                 
D6AA: 88 8B           EORA    #$8B                  
D6AC: A8 8B           EORA    D,X                 
D6AE: 88 0B           EORA    #$0B                  
D6B0: AA ; ????
D6B1: AA ; ????
D6B2: AA ; ????
D6B3: AA ; ????
D6B4: AA 88 88        ORA     $88,X                 
D6B7: BA A8 8B        ORA     $A88B                   
D6BA: A8 8B           EORA    D,X                 
D6BC: A8 88 88        EORA    $88,X                 
D6BF: 8B A8           ADDA    #$A8                  
D6C1: 88 88           EORA    #$88                  
D6C3: 8B A8           ADDA    #$A8                  
D6C5: 88 88           EORA    #$88                  
D6C7: 8B A8           ADDA    #$A8                  
D6C9: 8B A8           ADDA    #$A8                  
D6CB: 8B AA           ADDA    #$AA                  
D6CD: 88 88           EORA    #$88                  
D6CF: BA AA AA        ORA     $AAAA                   
D6D2: AA ; ????
D6D3: AA ; ????
D6D4: AA ; ????
D6D5: AA ; ????
D6D6: AA ; ????
D6D7: AA ; ????
D6D8: AA ; ????
D6D9: AA ; ????
D6DA: AA ; ????
D6DB: AA ; ????
D6DC: AA ; ????
D6DD: AA ; ????
D6DE: AA ; ????
D6DF: AA ; ????
D6E0: AA ; ????
D6E1: AA ; ????
D6E2: AA ; ????
D6E3: AA ; ????
D6E4: AA ; ????
D6E5: AA ; ????
D6E6: AA ; ????
D6E7: AA ; ????
D6E8: AA ; ????
D6E9: AA ; ????
D6EA: AA ; ????
D6EB: AA ; ????
D6EC: AA 78           ORA     -8,S                
D6EE: 1B ; ????
D6EF: AA ; ????
D6F0: AA 88 8B        ORA     $8B,X                 
D6F3: AA ; ????
D6F4: AA 68           ORA     8,S                 
D6F6: 0B ; ????
D6F7: AA ; ????
D6F8: AA A8 BA        ORA     $BA,Y                 
D6FB: AA ; ????
D6FC: AA A8 BA        ORA     $BA,Y                 
D6FF: AA ; ????
D700: A7 88 81        STA     $81,X                 
D703: BA A8 88        ORA     $A888                   
D706: 88 BA           EORA    #$BA                  
D708: A8 88 88        EORA    $88,X                 
D70B: BA A6 88        ORA     $A688                   
D70E: 80 BA           SUBA    #$BA                  
D710: AA ; ????
D711: AA ; ????
D712: AA ; ????
D713: AA ; ????
D714: AA ; ????
D715: AA ; ????
D716: AA ; ????
D717: AA ; ????
D718: AA ; ????
D719: AA ; ????
D71A: AA ; ????
D71B: AA ; ????
D71C: AA ; ????
D71D: AA ; ????
D71E: AA ; ????
D71F: AA ; ????
D720: AA ; ????
D721: AA ; ????
D722: AA ; ????
D723: AA ; ????
D724: AA ; ????
D725: AA ; ????
D726: AA ; ????
D727: AA ; ????
D728: AA ; ????
D729: AA ; ????
D72A: AA ; ????
D72B: AA A8 88        ORA     $88,Y                 
D72E: 88 8B           EORA    #$8B                  
D730: A8 88 88        EORA    $88,X                 
D733: 8B A8           ADDA    #$A8                  
D735: 88 88           EORA    #$88                  
D737: 8B A8           ADDA    #$A8                  
D739: 88 88           EORA    #$88                  
D73B: 8B A8           ADDA    #$A8                  
D73D: 88 88           EORA    #$88                  
D73F: 8B A8           ADDA    #$A8                  
D741: 88 88           EORA    #$88                  
D743: 8B A8           ADDA    #$A8                  
D745: 88 88           EORA    #$88                  
D747: 8B A8           ADDA    #$A8                  
D749: 88 88           EORA    #$88                  
D74B: 8B A8           ADDA    #$A8                  
D74D: 88 88           EORA    #$88                  
D74F: 8B AA           ADDA    #$AA                  
D751: AA ; ????
D752: AA ; ????
D753: AA ; ????
D754: AA ; ????
D755: AA ; ????
D756: AA ; ????
D757: AA ; ????
D758: AA ; ????
D759: AA ; ????
D75A: AA ; ????
D75B: AA ; ????
D75C: AA ; ????
D75D: AA ; ????
D75E: AA ; ????
D75F: AA ; ????
D760: AA ; ????
D761: AA ; ????
D762: AA ; ????
D763: AA ; ????
D764: AA ; ????
D765: AA ; ????
D766: AA ; ????
D767: AA A8 1B        ORA     $1B,Y                 
D76A: A7 8B           STA     D,X                 
D76C: A8 8B           EORA    D,X                 
D76E: A8 8B           EORA    D,X                 
D770: A8 88 88        EORA    $88,X                 
D773: 8B A8           ADDA    #$A8                  
D775: 8B A8           ADDA    #$A8                  
D777: 8B A8           ADDA    #$A8                  
D779: 88 88           EORA    #$88                  
D77B: 8B A8           ADDA    #$A8                  
D77D: 8B A8           ADDA    #$A8                  
D77F: 8B A8           ADDA    #$A8                  
D781: 0B ; ????
D782: A6 8B           LDA     D,X                 
D784: AA ; ????
D785: AA ; ????
D786: AA ; ????
D787: AA ; ????
D788: AA ; ????
D789: AA ; ????
D78A: AA ; ????
D78B: AA ; ????
D78C: AA ; ????
D78D: AA ; ????
D78E: AA ; ????
D78F: AA ; ????
D790: AA ; ????
D791: AA ; ????
D792: AA ; ????
D793: AA ; ????
D794: A7 88 88        STA     $88,X                 
D797: 1B ; ????
D798: A8 3B           EORA    -5,Y                
D79A: 68 ; ????
D79B: 8B A8           ADDA    #$A8                  
D79D: 2B A8           BMI     $D747                   
D79F: 8B A8           ADDA    #$A8                  
D7A1: 5B ; ????
D7A2: A8 3B           EORA    -5,Y                
D7A4: A8 4B           EORA    11,U                
D7A6: 78 ; ????
D7A7: 2B A6           BMI     $D74F                   
D7A9: 88 88           EORA    #$88                  
D7AB: BA AA 88        ORA     $AA88                   
D7AE: 88 BA           EORA    #$BA                  
D7B0: A7 88 88        STA     $88,X                 
D7B3: BA A8 3B        ORA     $A83B                   
D7B6: 68 ; ????
D7B7: 5B ; ????
D7B8: A8 2B           EORA    11,Y                
D7BA: A8 4B           EORA    11,U                
D7BC: A8 5B           EORA    -5,U                
D7BE: A8 8B           EORA    D,X                 
D7C0: A8 4B           EORA    11,U                
D7C2: 78 ; ????
D7C3: 8B A6           ADDA    #$A6                  
D7C5: 88 88           EORA    #$88                  
D7C7: 0B ; ????
D7C8: AA ; ????
D7C9: AA ; ????
D7CA: AA ; ????
D7CB: AA ; ????
D7CC: AA 78           ORA     -8,S                
D7CE: 81 BA           CMPA    #$BA                  
D7D0: A7 88 88        STA     $88,X                 
D7D3: 1B ; ????
D7D4: A8 88 88        EORA    $88,X                 
D7D7: 8B A8           ADDA    #$A8                  
D7D9: 88 88           EORA    #$88                  
D7DB: 8B A8           ADDA    #$A8                  
D7DD: 88 88           EORA    #$88                  
D7DF: 8B A8           ADDA    #$A8                  
D7E1: 8B A8           ADDA    #$A8                  
D7E3: 8B A8           ADDA    #$A8                  
D7E5: 8B A8           ADDA    #$A8                  
D7E7: 8B A8           ADDA    #$A8                  
D7E9: 8B A8           ADDA    #$A8                  
D7EB: 8B A8           ADDA    #$A8                  
D7ED: 88 88           EORA    #$88                  
D7EF: 8B A8           ADDA    #$A8                  
D7F1: 88 88           EORA    #$88                  
D7F3: 8B A8           ADDA    #$A8                  
D7F5: 88 88           EORA    #$88                  
D7F7: 8B A6           ADDA    #$A6                  
D7F9: 88 88           EORA    #$88                  
D7FB: 0B ; ????
D7FC: AA 68           ORA     8,S                 
D7FE: 80 BA           SUBA    #$BA                  
D800: AA ; ????
D801: AA ; ????
D802: AA ; ????
D803: AA A8 88        ORA     $88,Y                 
D806: 88 8B           EORA    #$8B                  
D808: A8 88 88        EORA    $88,X                 
D80B: 8B A8           ADDA    #$A8                  
D80D: 88 88           EORA    #$88                  
D80F: 8B A8           ADDA    #$A8                  
D811: 88 88           EORA    #$88                  
D813: 8B AA           ADDA    #$AA                  
D815: 88 88           EORA    #$88                  
D817: BA AA 88        ORA     $AA88                   
D81A: 88 BA           EORA    #$BA                  
D81C: AA 88 88        ORA     $88,X                 
D81F: BA AA 88        ORA     $AA88                   
D822: 88 BA           EORA    #$BA                  
D824: AA 88 88        ORA     $88,X                 
D827: BA A8 88        ORA     $A888                   
D82A: 88 8B           EORA    #$8B                  
D82C: A8 88 88        EORA    $88,X                 
D82F: 8B A8           ADDA    #$A8                  
D831: 88 88           EORA    #$88                  
D833: 8B A8           ADDA    #$A8                  
D835: 88 88           EORA    #$88                  
D837: 8B AA           ADDA    #$AA                  
D839: AA ; ????
D83A: AA ; ????
D83B: AA A8 88        ORA     $88,Y                 
D83E: 88 8B           EORA    #$8B                  
D840: A8 88 88        EORA    $88,X                 
D843: 8B A8           ADDA    #$A8                  
D845: 88 88           EORA    #$88                  
D847: 8B A8           ADDA    #$A8                  
D849: 88 81           EORA    #$81                  
D84B: BA A6 88        ORA     $A688                   
D84E: 88 1B           EORA    #$1B                  
D850: AA 68           ORA     8,S                 
D852: 88 8B           EORA    #$8B                  
D854: AA A8 88        ORA     $88,Y                 
D857: 8B AA           ADDA    #$AA                  
D859: 78 ; ????
D85A: 88 8B           EORA    #$8B                  
D85C: A7 88 88        STA     $88,X                 
D85F: 0B ; ????
D860: A8 88 80        EORA    $80,X                 
D863: BA A8 88        ORA     $A888                   
D866: 88 8B           EORA    #$8B                  
D868: A8 88 88        EORA    $88,X                 
D86B: 8B A8           ADDA    #$A8                  
D86D: 88 88           EORA    #$88                  
D86F: 8B AA           ADDA    #$AA                  
D871: AA ; ????
D872: AA ; ????
D873: AA A8 88        ORA     $88,Y                 
D876: 81 BA           CMPA    #$BA                  
D878: A8 88 88        EORA    $88,X                 
D87B: 3B              RTI                         
D87C: A8 8B           EORA    D,X                 
D87E: 88 2B           EORA    #$2B                  
D880: A8 88 88        EORA    $88,X                 
D883: BA A8 88        ORA     $A888                   
D886: 88 1B           EORA    #$1B                  
D888: A8 88 88        EORA    $88,X                 
D88B: 8B A8           ADDA    #$A8                  
D88D: 88 8B           EORA    #$8B                  
D88F: 8B A8           ADDA    #$A8                  
D891: 88 88           EORA    #$88                  
D893: 8B A8           ADDA    #$A8                  
D895: 88 88           EORA    #$88                  
D897: 8B A8           ADDA    #$A8                  
D899: 88 88           EORA    #$88                  
D89B: 8B A8           ADDA    #$A8                  
D89D: 8B 88           ADDA    #$88                  
D89F: 8B A8           ADDA    #$A8                  
D8A1: 88 88           EORA    #$88                  
D8A3: 3B              RTI                         
D8A4: A8 88 88        EORA    $88,X                 
D8A7: 2B AA           BMI     $D853                   
D8A9: AA ; ????
D8AA: AA ; ????
D8AB: AA ; ????
D8AC: A7 88 88        STA     $88,X                 
D8AF: 1B ; ????
D8B0: A8 88 88        EORA    $88,X                 
D8B3: 8B A8           ADDA    #$A8                  
D8B5: 88 88           EORA    #$88                  
D8B7: 8B A8           ADDA    #$A8                  
D8B9: 88 88           EORA    #$88                  
D8BB: 8B A8           ADDA    #$A8                  
D8BD: 88 88           EORA    #$88                  
D8BF: 0B ; ????
D8C0: A8 88 83        EORA    $83,X                 
D8C3: BA A8 88        ORA     $A888                   
D8C6: 82 BA           SBCA    #$BA                  
D8C8: A8 88 88        EORA    $88,X                 
D8CB: 1B ; ????
D8CC: A8 88 88        EORA    $88,X                 
D8CF: 8B A8           ADDA    #$A8                  
D8D1: 88 88           EORA    #$88                  
D8D3: 8B A8           ADDA    #$A8                  
D8D5: 88 88           EORA    #$88                  
D8D7: 8B A8           ADDA    #$A8                  
D8D9: 88 88           EORA    #$88                  
D8DB: 3B              RTI                         
D8DC: A8 88 B8        EORA    $B8,X                 
D8DF: 2B AA           BMI     $D88B                   
D8E1: AA ; ????
D8E2: AA ; ????
D8E3: AA ; ????
D8E4: A7 1B           STA     -5,X                
D8E6: A7 1B           STA     -5,X                
D8E8: A8 8B           EORA    D,X                 
D8EA: A8 8B           EORA    D,X                 
D8EC: A8 8B           EORA    D,X                 
D8EE: A8 8B           EORA    D,X                 
D8F0: A8 8B           EORA    D,X                 
D8F2: A8 8B           EORA    D,X                 
D8F4: A8 8B           EORA    D,X                 
D8F6: A8 8B           EORA    D,X                 
D8F8: A8 8B           EORA    D,X                 
D8FA: A8 8B           EORA    D,X                 
D8FC: A8 8B           EORA    D,X                 
D8FE: A8 8B           EORA    D,X                 
D900: A8 88 88        EORA    $88,X                 
D903: 8B A8           ADDA    #$A8                  
D905: 88 88           EORA    #$88                  
D907: 8B A8           ADDA    #$A8                  
D909: 88 88           EORA    #$88                  
D90B: 8B A8           ADDA    #$A8                  
D90D: 88 88           EORA    #$88                  
D90F: 8B A6           ADDA    #$A6                  
D911: 88 88           EORA    #$88                  
D913: 0B ; ????
D914: AA 68           ORA     8,S                 
D916: 80 BA           SUBA    #$BA                  
D918: AA ; ????
D919: AA ; ????
D91A: AA ; ????
D91B: AA A8 88        ORA     $88,Y                 
D91E: 88 8B           EORA    #$8B                  
D920: A8 88 88        EORA    $88,X                 
D923: 8B A8           ADDA    #$A8                  
D925: 88 88           EORA    #$88                  
D927: 8B A8           ADDA    #$A8                  
D929: 88 88           EORA    #$88                  
D92B: 8B A8           ADDA    #$A8                  
D92D: 88 88           EORA    #$88                  
D92F: 8B A8           ADDA    #$A8                  
D931: 88 88           EORA    #$88                  
D933: 8B A8           ADDA    #$A8                  
D935: 88 88           EORA    #$88                  
D937: 8B A8           ADDA    #$A8                  
D939: 88 88           EORA    #$88                  
D93B: 8B A8           ADDA    #$A8                  
D93D: 88 88           EORA    #$88                  
D93F: 8B A8           ADDA    #$A8                  
D941: 88 88           EORA    #$88                  
D943: 8B A8           ADDA    #$A8                  
D945: 88 88           EORA    #$88                  
D947: 8B A8           ADDA    #$A8                  
D949: 88 88           EORA    #$88                  
D94B: 8B A8           ADDA    #$A8                  
D94D: 88 88           EORA    #$88                  
D94F: 8B AA           ADDA    #$AA                  
D951: AA ; ????
D952: AA ; ????
D953: AA ; ????
D954: AA ; ????
D955: A7 88 1B        STA     $1B,X                 
D958: A7 88 88        STA     $88,X                 
D95B: 8B A8           ADDA    #$A8                  
D95D: 88 88           EORA    #$88                  
D95F: 8B A8           ADDA    #$A8                  
D961: 88 88           EORA    #$88                  
D963: 8B A8           ADDA    #$A8                  
D965: 88 88           EORA    #$88                  
D967: 8B A6           ADDA    #$A6                  
D969: 88 88           EORA    #$88                  
D96B: 8B AA           ADDA    #$AA                  
D96D: A6 88 0B        LDA     $0B,X                 
D970: AA ; ????
D971: AA ; ????
D972: AA ; ????
D973: AA ; ????
D974: AA ; ????
D975: AA ; ????
D976: AA ; ????
D977: AA ; ????
D978: AA ; ????
D979: AA ; ????
D97A: AA ; ????
D97B: AA ; ????
D97C: AA ; ????
D97D: AA ; ????
D97E: AA ; ????
D97F: AA ; ????
D980: AA ; ????
D981: AA ; ????
D982: AA ; ????
D983: AA ; ????
D984: AA ; ????
D985: AA ; ????
D986: AA ; ????
D987: AA ; ????
D988: AA ; ????
D989: AA ; ????
D98A: AA ; ????
D98B: AA A8 8B        ORA     $8B,Y                 
D98E: 88 1B           EORA    #$1B                  
D990: A8 88 88        EORA    $88,X                 
D993: 8B A8           ADDA    #$A8                  
D995: 88 88           EORA    #$88                  
D997: 8B AA           ADDA    #$AA                  
D999: A8 8B           EORA    D,X                 
D99B: AA A8 88        ORA     $88,Y                 
D99E: 88 8B           EORA    #$8B                  
D9A0: A8 88 88        EORA    $88,X                 
D9A3: 8B A8           ADDA    #$A8                  
D9A5: 88 88           EORA    #$88                  
D9A7: 8B A6           ADDA    #$A6                  
D9A9: 88 88           EORA    #$88                  
D9AB: 0B ; ????
D9AC: AA 88 81        ORA     $81,X                 
D9AF: BA AA 88        ORA     $AA88                   
D9B2: 88 1B           EORA    #$1B                  
D9B4: A8 88 88        EORA    $88,X                 
D9B7: 8B A8           ADDA    #$A8                  
D9B9: 8B 88           ADDA    #$88                  
D9BB: 8B A6           ADDA    #$A6                  
D9BD: BA 88 8B        ORA     $888B                   
D9C0: AA ; ????
D9C1: AA ; ????
D9C2: AA ; ????
D9C3: AA A8 1B        ORA     $1B,Y                 
D9C6: A7 1B           STA     -5,X                
D9C8: A8 81           EORA    ,X++                
D9CA: B8 8B A6        EORA    $8BA6                   
D9CD: 88 88           EORA    #$88                  
D9CF: 8B AA           ADDA    #$AA                  
D9D1: 68 ; ????
D9D2: 88 3B           EORA    #$3B                  
D9D4: AA 78           ORA     -8,S                
D9D6: 88 2B           EORA    #$2B                  
D9D8: A7 80           STA     ,X+                 
D9DA: B8 8B A8        EORA    $8BA8                   
D9DD: 8B AA           ADDA    #$AA                  
D9DF: 8B A6           ADDA    #$A6                  
D9E1: 81 B8           CMPA    #$B8                  
D9E3: 8B AA           ADDA    #$AA                  
D9E5: 68 ; ????
D9E6: 88 5B           EORA    #$5B                  
D9E8: AA 78           ORA     -8,S                
D9EA: 88 4B           EORA    #$4B                  
D9EC: A7 88 88        STA     $88,X                 
D9EF: 8B A8           ADDA    #$A8                  
D9F1: 80 B8           SUBA    #$B8                  
D9F3: 8B A8           ADDA    #$A8                  
D9F5: 0B ; ????
D9F6: A6 0B           LDA     11,X                
D9F8: AA ; ????
D9F9: AA ; ????
D9FA: AA ; ????
D9FB: AA ; ????
D9FC: AA ; ????
D9FD: AA ; ????
D9FE: AA ; ????
D9FF: AA ; ????
DA00: AA ; ????
DA01: AA ; ????
DA02: AA ; ????
DA03: AA ; ????
DA04: AA ; ????
DA05: AA ; ????
DA06: A7 8B           STA     D,X                 
DA08: AA 78           ORA     -8,S                
DA0A: 88 8B           EORA    #$8B                  
DA0C: A7 88 88        STA     $88,X                 
DA0F: 8B A8           ADDA    #$A8                  
DA11: 8B 88           ADDA    #$88                  
DA13: 0B ; ????
DA14: A8 88 88        EORA    $88,X                 
DA17: BA A8 8B        ORA     $A88B                   
DA1A: 88 1B           EORA    #$1B                  
DA1C: A6 88 88        LDA     $88,X                 
DA1F: 8B AA           ADDA    #$AA                  
DA21: 68 ; ????
DA22: 88 8B           EORA    #$8B                  
DA24: AA ; ????
DA25: AA A6           ORA     A,Y                 
DA27: 8B AA           ADDA    #$AA                  
DA29: AA ; ????
DA2A: AA ; ????
DA2B: AA ; ????
DA2C: AA ; ????
DA2D: AA ; ????
DA2E: AA ; ????
DA2F: AA ; ????
DA30: AA ; ????
DA31: AA ; ????
DA32: AA ; ????
DA33: AA A8 B8        ORA     $B8,Y                 
DA36: 8B 8B           ADDA    #$8B                  
DA38: A8 88 88        EORA    $88,X                 
DA3B: 8B A6           ADDA    #$A6                  
DA3D: 88 88           EORA    #$88                  
DA3F: 8B AA           ADDA    #$AA                  
DA41: 68 ; ????
DA42: 88 0B           EORA    #$0B                  
DA44: AA A6           ORA     A,Y                 
DA46: 80 BA           SUBA    #$BA                  
DA48: AA A8 88        ORA     $88,Y                 
DA4B: BA AA 88        ORA     $AA88                   
DA4E: 88 BA           EORA    #$BA                  
DA50: A7 88 88        STA     $88,X                 
DA53: 8B A8           ADDA    #$A8                  
DA55: 88 BA           EORA    #$BA                  
DA57: 8B A8           ADDA    #$A8                  
DA59: 88 88           EORA    #$88                  
DA5B: 0B ; ????
DA5C: A8 8B           EORA    D,X                 
DA5E: 88 BA           EORA    #$BA                  
DA60: AA 88 88        ORA     $88,X                 
DA63: BA AA A8        ORA     $AAA8                   
DA66: B0 BA AA        SUBA    $BAAA                   
DA69: AA ; ????
DA6A: AA ; ????
DA6B: AA ; ????
DA6C: AA ; ????
DA6D: AA 88 1B        ORA     $1B,X                 
DA70: AA 88 88        ORA     $88,X                 
DA73: 8B A7           ADDA    #$A7                  
DA75: 88 88           EORA    #$88                  
DA77: 8B A8           ADDA    #$A8                  
DA79: 88 88           EORA    #$88                  
DA7B: 8B A8           ADDA    #$A8                  
DA7D: 88 8B           EORA    #$8B                  
DA7F: 8B A8           ADDA    #$A8                  
DA81: 88 88           EORA    #$88                  
DA83: 8B A8           ADDA    #$A8                  
DA85: 88 88           EORA    #$88                  
DA87: 3B              RTI                         
DA88: A6 8B           LDA     D,X                 
DA8A: 88 2B           EORA    #$2B                  
DA8C: AA ; ????
DA8D: AA ; ????
DA8E: AA ; ????
DA8F: AA ; ????
DA90: AA ; ????
DA91: AA ; ????
DA92: AA ; ????
DA93: AA ; ????
DA94: AA ; ????
DA95: AA ; ????
DA96: AA ; ????
DA97: AA ; ????
DA98: AA ; ????
DA99: AA ; ????
DA9A: AA ; ????
DA9B: AA ; ????
DA9C: AA ; ????
DA9D: AA ; ????
DA9E: AA ; ????
DA9F: AA ; ????
DAA0: AA ; ????
DAA1: AA ; ????
DAA2: AA ; ????
DAA3: AA ; ????
DAA4: AA A8 8B        ORA     $8B,Y                 
DAA7: AA ; ????
DAA8: AA A8 8B        ORA     $8B,Y                 
DAAB: AA ; ????
DAAC: AA A8 8B        ORA     $8B,Y                 
DAAF: AA A8 88        ORA     $88,Y                 
DAB2: 88 8B           EORA    #$8B                  
DAB4: A8 88 88        EORA    $88,X                 
DAB7: 8B A8           ADDA    #$A8                  
DAB9: 88 88           EORA    #$88                  
DABB: 8B A8           ADDA    #$A8                  
DABD: 88 88           EORA    #$88                  
DABF: 8B A8           ADDA    #$A8                  
DAC1: 88 88           EORA    #$88                  
DAC3: 8B A8           ADDA    #$A8                  
DAC5: 88 88           EORA    #$88                  
DAC7: 8B A8           ADDA    #$A8                  
DAC9: 88 88           EORA    #$88                  
DACB: 8B AA           ADDA    #$AA                  
DACD: A8 8B           EORA    D,X                 
DACF: AA ; ????
DAD0: AA A8 8B        ORA     $8B,Y                 
DAD3: AA ; ????
DAD4: AA A8 8B        ORA     $8B,Y                 
DAD7: AA ; ????
DAD8: AA ; ????
DAD9: AA ; ????
DADA: AA ; ????
DADB: AA ; ????
DADC: AA A8 88        ORA     $88,Y                 
DADF: 8B AA           ADDA    #$AA                  
DAE1: A8 88 8B        EORA    $8B,X                 
DAE4: A7 88 88        STA     $88,X                 
DAE7: 8B A8           ADDA    #$A8                  
DAE9: 88 88           EORA    #$88                  
DAEB: 8B A8           ADDA    #$A8                  
DAED: 88 88           EORA    #$88                  
DAEF: 3B              RTI                         
DAF0: AA A8 88        ORA     $88,Y                 
DAF3: 2B AA           BMI     $DA9F                   
DAF5: 78 ; ????
DAF6: 88 5B           EORA    #$5B                  
DAF8: AA 88 88        ORA     $88,X                 
DAFB: 4B ; ????
DAFC: A7 88 88        STA     $88,X                 
DAFF: 8B A8           ADDA    #$A8                  
DB01: 88 88           EORA    #$88                  
DB03: 8B A8           ADDA    #$A8                  
DB05: 88 88           EORA    #$88                  
DB07: 0B ; ????
DB08: AA 68           ORA     8,S                 
DB0A: 88 BA           EORA    #$BA                  
DB0C: AA ; ????
DB0D: AA ; ????
DB0E: AA ; ????
DB0F: AA ; ????
DB10: AA ; ????
DB11: AA ; ????
DB12: AA ; ????
DB13: AA A8 8B        ORA     $8B,Y                 
DB16: 88 8B           EORA    #$8B                  
DB18: A8 8B           EORA    D,X                 
DB1A: 88 8B           EORA    #$8B                  
DB1C: A8 88 88        EORA    $88,X                 
DB1F: 8B AA           ADDA    #$AA                  
DB21: 88 8B           EORA    #$8B                  
DB23: AA A8 88        ORA     $88,Y                 
DB26: 8B AA           ADDA    #$AA                  
DB28: A8 88 BA        EORA    $BA,X                 
DB2B: AA A8 88        ORA     $88,Y                 
DB2E: 88 BA           EORA    #$BA                  
DB30: AA A8 88        ORA     $88,Y                 
DB33: BA AA 88        ORA     $AA88                   
DB36: 88 BA           EORA    #$BA                  
DB38: AA 88 8B        ORA     $8B,X                 
DB3B: AA ; ????
DB3C: AA 88 88        ORA     $88,X                 
DB3F: 8B A8           ADDA    #$A8                  
DB41: 88 88           EORA    #$88                  
DB43: 8B A8           ADDA    #$A8                  
DB45: 88 88           EORA    #$88                  
DB47: 8B AA           ADDA    #$AA                  
DB49: AA ; ????
DB4A: AA ; ????
DB4B: AA ; ????
DB4C: AA ; ????
DB4D: AA 78           ORA     -8,S                
DB4F: 1B ; ????
DB50: AA 78           ORA     -8,S                
DB52: 88 8B           EORA    #$8B                  
DB54: AA 88 88        ORA     $88,X                 
DB57: 0B ; ????
DB58: A7 88 88        STA     $88,X                 
DB5B: 5B ; ????
DB5C: A8 88 88        EORA    $88,X                 
DB5F: 4B ; ????
DB60: A8 88 88        EORA    $88,X                 
DB63: 8B A6           ADDA    #$A6                  
DB65: 88 88           EORA    #$88                  
DB67: 8B AA           ADDA    #$AA                  
DB69: AA 68           ORA     8,S                 
DB6B: 0B ; ????
DB6C: AA ; ????
DB6D: AA ; ????
DB6E: AA ; ????
DB6F: AA ; ????
DB70: AA ; ????
DB71: AA ; ????
DB72: AA ; ????
DB73: AA ; ????
DB74: AA ; ????
DB75: AA ; ????
DB76: AA ; ????
DB77: AA ; ????
DB78: AA ; ????
DB79: AA ; ????
DB7A: AA ; ????
DB7B: AA ; ????
DB7C: AA ; ????
DB7D: AA ; ????
DB7E: AA ; ????
DB7F: AA ; ????
DB80: AA ; ????
DB81: AA ; ????
DB82: AA ; ????
DB83: AA ; ????
DB84: AA 88 8B        ORA     $8B,X                 
DB87: AA ; ????
DB88: AA 88 8B        ORA     $8B,X                 
DB8B: AA ; ????
DB8C: AA 88 8B        ORA     $8B,X                 
DB8F: AA ; ????
DB90: AA 88 8B        ORA     $8B,X                 
DB93: AA ; ????
DB94: AA 88 8B        ORA     $8B,X                 
DB97: AA ; ????
DB98: AA 88 8B        ORA     $8B,X                 
DB9B: AA ; ????
DB9C: AA 88 8B        ORA     $8B,X                 
DB9F: AA ; ????
DBA0: AA ; ????
DBA1: AA ; ????
DBA2: AA ; ????
DBA3: AA ; ????
DBA4: AA ; ????
DBA5: AA ; ????
DBA6: AA ; ????
DBA7: AA ; ????
DBA8: AA ; ????
DBA9: AA ; ????
DBAA: AA ; ????
DBAB: AA ; ????
DBAC: AA ; ????
DBAD: AA ; ????
DBAE: AA ; ????
DBAF: AA ; ????
DBB0: AA ; ????
DBB1: AA ; ????
DBB2: AA ; ????
DBB3: AA ; ????
DBB4: AA ; ????
DBB5: AA ; ????
DBB6: AA ; ????
DBB7: AA ; ????
DBB8: AA ; ????
DBB9: AA ; ????
DBBA: AA ; ????
DBBB: AA A8 B7        ORA     $B7,Y                 
DBBE: 8B 8B           ADDA    #$8B                  
DBC0: A8 B8 88        EORA    [$88,Y]               
DBC3: 8B A8           ADDA    #$A8                  
DBC5: 88 88           EORA    #$88                  
DBC7: 8B A8           ADDA    #$A8                  
DBC9: 88 88           EORA    #$88                  
DBCB: 8B AA           ADDA    #$AA                  
DBCD: 88 88           EORA    #$88                  
DBCF: 0B ; ????
DBD0: AA 88 88        ORA     $88,X                 
DBD3: BA A8 88        ORA     $A888                   
DBD6: 88 8B           EORA    #$8B                  
DBD8: A6 88 88        LDA     $88,X                 
DBDB: 8B AA           ADDA    #$AA                  
DBDD: A8 88 BA        EORA    $BA,X                 
DBE0: A8 88 88        EORA    $88,X                 
DBE3: 8B A6           ADDA    #$A6                  
DBE5: 88 88           EORA    #$88                  
DBE7: BA A7 88        ORA     $A788                   
DBEA: 88 8B           EORA    #$8B                  
DBEC: A8 88 88        EORA    $88,X                 
DBEF: 8B AA           ADDA    #$AA                  
DBF1: AA ; ????
DBF2: AA ; ????
DBF3: AA 50           ORA     -16,U               
DBF5: A8 00           EORA    0,X                 
DBF7: F8 00 00        EORB    $0000                   
DBFA: 00 00           NEG     $00                   
DBFC: 00 00           NEG     $00                   
DBFE: 00 00           NEG     $00                   
DC00: 80 10           SUBA    #$10                  
DC02: 60 60           NEG     0,S                 
DC04: 90 90           SUBA    $90                   
DC06: 00 00           NEG     $00                   
DC08: 00 00           NEG     $00                   
DC0A: 00 00           NEG     $00                   
DC0C: 70 C0 F0        NEG     $C0F0                   
DC0F: 78 ; ????
DC10: F8 00 00        EORB    $0000                   
DC13: 00 00           NEG     $00                   
DC15: 00 00           NEG     $00                   
DC17: 00 00           NEG     $00                   
DC19: 88 70           EORA    #$70                  
DC1B: 70 00 90        NEG     $0090                   
DC1E: 00 00           NEG     $00                   
DC20: 00 00           NEG     $00                   
DC22: 00 00           NEG     $00                   
DC24: 40              NEGA                        
DC25: 08 ; ????
DC26: 20 00           BRA     $DC28                   
DC28: 00 20           NEG     $20                   
DC2A: 00 00           NEG     $00                   
DC2C: 00 00           NEG     $00                   
DC2E: 00 00           NEG     $00                   
DC30: 00 08           NEG     $08                   
DC32: 18 ; ????
DC33: 38 ; ????
DC34: 40              NEGA                        
DC35: 80 80           SUBA    #$80                  
DC37: 40              NEGA                        
DC38: 38 ; ????
DC39: 18 ; ????
DC3A: 08 ; ????
DC3B: 00 F8           NEG     $F8                   
DC3D: F8 F8 00        EORB    $F800                   
DC40: 00 00           NEG     $00                   
DC42: 00 00           NEG     $00                   
DC44: 00 F8           NEG     $F8                   
DC46: F8 F8 F8        EORB    $F8F8                   
DC49: E0 C0           SUBB    ,U+                 
DC4B: 08 ; ????
DC4C: 18 ; ????
DC4D: 98 40           EORA    $40                   
DC4F: 40              NEGA                        
DC50: C0 98           SUBB    #$98                  
DC52: 98 98           EORA    $98                   
DC54: 00 00           NEG     $00                   
DC56: 20 20           BRA     $DC78                   
DC58: 00 00           NEG     $00                   
DC5A: 00 00           NEG     $00                   
DC5C: 00 00           NEG     $00                   
DC5E: 00 00           NEG     $00                   
DC60: 00 00           NEG     $00                   
DC62: 00 00           NEG     $00                   
DC64: 00 F0           NEG     $F0                   
DC66: F0 F0 00        SUBB    $F000                   
DC69: 00 00           NEG     $00                   
DC6B: 00 00           NEG     $00                   
DC6D: 00 50           NEG     $50                   
DC6F: 48 ; ????
DC70: 00 20           NEG     $20                   
DC72: 00 48           NEG     $48                   
DC74: 00 58           NEG     $58                   
DC76: 00 00           NEG     $00                   
DC78: 00 00           NEG     $00                   
DC7A: 00 00           NEG     $00                   
DC7C: 88 88           EORA    #$88                  
DC7E: 88 88           EORA    #$88                  
DC80: 00 00           NEG     $00                   
DC82: 00 00           NEG     $00                   
DC84: 98 88           EORA    $88                   
DC86: 08 ; ????
DC87: 00 80           NEG     $80                   
DC89: 00 00           NEG     $00                   
DC8B: 80 00           SUBA    #$00                  
DC8D: 08 ; ????
DC8E: 88 98           EORA    #$98                  
DC90: 00 50           NEG     $50                   
DC92: 20 88           BRA     $DC1C                   
DC94: 08 ; ????
DC95: 08 ; ????
DC96: 08 ; ????
DC97: 08 ; ????
DC98: 88 20           EORA    #$20                  
DC9A: 50              NEGB                        
DC9B: 00 A8           NEG     $A8                   
DC9D: 00 A8           NEG     $A8                   
DC9F: 00 00           NEG     $00                   
DCA1: 00 00           NEG     $00                   
DCA3: 00 00           NEG     $00                   
DCA5: A8 00           EORA    0,X                 
DCA7: A8 F8 F8        EORA    [$F8,S]               
DCAA: 20 00           BRA     $DCAC                   
DCAC: 00 08           NEG     $08                   
DCAE: 00 10           NEG     $10                   
DCB0: 20 00           BRA     $DCB2                   
DCB2: D0 D8           SUBB    $D8                   
DCB4: A0 ; ????
DCB5: 90 80           SUBA    $80                   
DCB7: 00 38           NEG     $38                   
DCB9: 60 60           NEG     0,S                 
DCBB: 78 ; ????
DCBC: 00 00           NEG     $00                   
DCBE: 90 E0           SUBA    $E0                   
DCC0: F8 E0 D0        EORB    $E0D0                   
DCC3: 88 80           EORA    #$80                  
DCC5: 00 00           NEG     $00                   
DCC7: 08 ; ????
DCC8: 90 58           SUBA    $58                   
DCCA: F8 40 80        EORB    $4080                   
DCCD: 80 08           SUBA    #$08                  
DCCF: 80 08           SUBA    #$08                  
DCD1: 88 00           EORA    #$00                  
DCD3: 08 ; ????
DCD4: 90 90           SUBA    $90                   
DCD6: 58 ; ????
DCD7: 30 98 20        LEAX    [$20,X]               
DCDA: 00 48           NEG     $48                   
DCDC: 00 10           NEG     $10                   
DCDE: 00 48           NEG     $48                   
DCE0: 00 80           NEG     $80                   
DCE2: 10 ; ????
DCE3: 00 10           NEG     $10                   
DCE5: 58 ; ????
DCE6: 40              NEGA                        
DCE7: A8 20           EORA    0,Y                 
DCE9: 18 ; ????
DCEA: 00 00           NEG     $00                   
DCEC: 00 00           NEG     $00                   
DCEE: 00 00           NEG     $00                   
DCF0: 90 A8           SUBA    $A8                   
DCF2: 00 00           NEG     $00                   
DCF4: 20 50           BRA     $DD46                   
DCF6: 10 ; ????
DCF7: 40              NEGA                        
DCF8: 20 58           BRA     $DD52                   
DCFA: 98 18           EORA    $18                   
DCFC: 88 C8           EORA    #$C8                  
DCFE: 48 ; ????
DCFF: 10 ; ????
DD00: 00 00           NEG     $00                   
DD02: 00 00           NEG     $00                   
DD04: 00 08           NEG     $08                   
DD06: C8 88           EORB    #$88                  
DD08: 00 00           NEG     $00                   
DD0A: 08 ; ????
DD0B: 18 ; ????
DD0C: 18 ; ????
DD0D: 80 80           SUBA    #$80                  
DD0F: 18 ; ????
DD10: 18 ; ????
DD11: 08 ; ????
DD12: 00 00           NEG     $00                   
DD14: 00 F8           NEG     $F8                   
DD16: 78 ; ????
DD17: 20 00           BRA     $DD19                   
DD19: 10 ; ????
DD1A: 00 80           NEG     $80                   
DD1C: 40              NEGA                        
DD1D: 90 10           SUBA    $10                   
DD1F: 00 10           NEG     $10                   
DD21: 20 88           BRA     $DCAB                   
DD23: 20 80           BRA     $DCA5                   
DD25: B8 10 00        EORA    $1000                   
DD28: 00 00           NEG     $00                   
DD2A: 00 00           NEG     $00                   
DD2C: 20 00           BRA     $DD2E                   
DD2E: 00 A0           NEG     $A0                   
DD30: 70 70 70        NEG     $7070                   
DD33: 70 A0 00        NEG     $A000                   
DD36: 00 20           NEG     $20                   
DD38: 08 ; ????
DD39: 00 10           NEG     $10                   
DD3B: 48 ; ????
DD3C: 00 00           NEG     $00                   
DD3E: 00 18           NEG     $18                   
DD40: 88 50           EORA    #$50                  
DD42: 00 00           NEG     $00                   
DD44: 98 98           EORA    $98                   
DD46: 20 00           BRA     $DD48                   
DD48: 00 00           NEG     $00                   
DD4A: 00 20           NEG     $20                   
DD4C: 00 40           NEG     $40                   
DD4E: 38 ; ????
DD4F: D8 00           EORB    $00                   
DD51: 18 ; ????
DD52: 40              NEGA                        
DD53: 00 10           NEG     $10                   
DD55: 40              NEGA                        
DD56: 08 ; ????
DD57: 00 00           NEG     $00                   
DD59: 00 00           NEG     $00                   
DD5B: 00 60           NEG     $60                   
DD5D: 60 00           NEG     0,X                 
DD5F: 00 60           NEG     $60                   
DD61: 60 00           NEG     0,X                 
DD63: 00 00           NEG     $00                   
DD65: 00 00           NEG     $00                   
DD67: 00 20           NEG     $20                   
DD69: 28 50           BVC     $DDBB                   
DD6B: 08 ; ????
DD6C: 20 10           BRA     $DD7E                   
DD6E: C8 10           EORB    #$10                  
DD70: 00 B0           NEG     $B0                   
DD72: 40              NEGA                        
DD73: 50              NEGB                        
DD74: 80 40           SUBA    #$40                  
DD76: 37 50           PULU    X,S                   
DD78: 47              ASRA                        
DD79: 23 29           BLS     $DDA4                   
DD7B: 2B B2           BMI     $DD2F                   
DD7D: B9 3D 00        ADCA    $3D00                   
DD80: 00 00           NEG     $00                   
DD82: 00 00           NEG     $00                   
DD84: 05 ; ????
DD85: 0F 01           CLR     $01                   
DD87: 10 ; ????
DD88: 1E 01           EXG     D,X                   
DD8A: 50              NEGB                        
DD8B: 47              ASRA                        
DD8C: 28 87           BVC     $DD15                   
DD8E: 40              NEGA                        
DD8F: 37 50           PULU    X,S                   
DD91: 47              ASRA                        
DD92: 23 8D           BLS     $DD21                   
DD94: 19              DAA                         
DD95: 34 B9           PSHS    PC,Y,X,DP,CC                   
DD97: 00 00           NEG     $00                   
DD99: 00 00           NEG     $00                   
DD9B: 00 00           NEG     $00                   
DD9D: 04 08           LSR     $08                   
DD9F: 03 03           COM     $03                   
DDA1: 14 ; ????
DDA2: 01 ; ????
DDA3: 50              NEGB                        
DDA4: 47              ASRA                        
DDA5: 28 87           BVC     $DD2E                   
DDA7: 40              NEGA                        
DDA8: 37 50           PULU    X,S                   
DDAA: 47              ASRA                        
DDAB: 1B ; ????
DDAC: B1 21 23        CMPA    $2123                   
DDAF: 35 00           PULS                       
DDB1: 00 00           NEG     $00                   
DDB3: 00 00           NEG     $00                   
DDB5: 00 04           NEG     $04                   
DDB7: 0F 02           CLR     $02                   
DDB9: 10 ; ????
DDBA: 0A 02           DEC     $02                   
DDBC: 50              NEGB                        
DDBD: 47              ASRA                        
DDBE: 28 87           BVC     $DD47                   
DDC0: 47              ASRA                        
DDC1: 40              NEGA                        
DDC2: 57              ASRB                        
DDC3: 50              NEGB                        
DDC4: 24 ; ????
DDC5: 09 8E           ROL     $8E                   
DDC7: B2 12 95        SBCA    $1295                   
DDCA: 35 00           PULS                       
DDCC: 00 00           NEG     $00                   
DDCE: 00 06           NEG     $06                   
DDD0: 0F 01           CLR     $01                   
DDD2: 03 1E           COM     $1E                   
DDD4: 02 ; ????
DDD5: 57              ASRB                        
DDD6: 50              NEGB                        
DDD7: 28 87           BVC     $DD60                   
DDD9: 50              NEGB                        
DDDA: 47              ASRA                        
DDDB: 57              ASRB                        
DDDC: 50              NEGB                        
DDDD: 3C 3E           CWAI    $3E                   
DDDF: 41 ; ????
DDE0: CA 4B           ORB     #$4B                  
DDE2: CD ; ????
DDE3: 00 00           NEG     $00                   
DDE5: 00 00           NEG     $00                   
DDE7: 00 05           NEG     $05                   
DDE9: 0F 01           CLR     $01                   
DDEB: 05 ; ????
DDEC: 14 ; ????
DDED: 02 ; ????
DDEE: 57              ASRB                        
DDEF: 50              NEGB                        
DDF0: 28 90           BVC     $DD82                   
DDF2: 57              ASRB                        
DDF3: 50              NEGB                        
DDF4: 67 53           ASR     -13,U               
DDF6: 3D              MUL                         
DDF7: 16 39 66        LBRA    $11760                   
DDFA: 00 00           NEG     $00                   
DDFC: 00 00           NEG     $00                   
DDFE: 00 00           NEG     $00                   
DE00: 00 03           NEG     $03                   
DE02: 0F 01           CLR     $01                   
DE04: 03 1E           COM     $1E                   
DE06: 01 ; ????
DE07: 67 57           ASR     -9,U                
DE09: 3C 90           CWAI    $90                   
DE0B: 57              ASRB                        
DE0C: 50              NEGB                        
DE0D: 67 57           ASR     -9,U                
DE0F: 3C 09           CWAI    $09                   
DE11: 86 21           LDA     #$21                  
DE13: 56              RORB                        
DE14: E1 6E           CMPB    14,S                
DE16: 4A              DECA                        
DE17: 00 00           NEG     $00                   
DE19: 00 07           NEG     $07                   
DE1B: 0F 01           CLR     $01                   
DE1D: 03 14           COM     $14                   
DE1F: 02 ; ????
DE20: 67 57           ASR     -9,U                
DE22: 3C 87           CWAI    $87                   
DE24: 50              NEGB                        
DE25: 47              ASRA                        
DE26: 67 53           ASR     -13,U               
DE28: 43              COMA                        
DE29: 0E 11           JMP     $11                   
DE2B: AE 52           LDX     -14,U               
DE2D: 66 EA 00        ROR     $00,X                 
DE30: 00 00           NEG     $00                   
DE32: 00 06           NEG     $06                   
DE34: 0F 01           CLR     $01                   
DE36: 03 1E           COM     $1E                   
DE38: 02 ; ????
DE39: 67 57           ASR     -9,U                
DE3B: 3C 90           CWAI    $90                   
DE3D: 67 60           ASR     0,S                 
DE3F: 77 67 24        ASR     $6724                   
DE42: 0A 8B           DEC     $8B                   
DE44: 0C 8D           INC     $8D                   
DE46: 3A              ABX                         
DE47: BB 3C BD        ADDA    $3CBD                   
DE4A: 00 00           NEG     $00                   
DE4C: 08 ; ????
DE4D: 0F 01           CLR     $01                   
DE4F: 03 14           COM     $14                   
DE51: 02 ; ????
DE52: 77 67 28        ASR     $6728                   
DE55: 90 00           SUBA    $00                   
DE57: 00 67           NEG     $67                   
DE59: 60 23           NEG     3,Y                 
DE5B: 8A 0B           ORA     #$0B                  
DE5D: 8C 12 93        CMPX    #$1293                  
DE60: 14 ; ????
DE61: 9A 1B           ORA     $1B                   
DE63: 9C 00           CMPX    $00                   
DE65: 09 0F           ROL     $0F                   
DE67: 01 ; ????
DE68: 03 02           COM     $02                   
DE6A: 03 67           COM     $67                   
DE6C: 60 20           NEG     0,Y                 
DE6E: 90 70           SUBA    $70                   
DE70: 67 77           ASR     -9,S                
DE72: 70 3C 99        NEG     $3C99                   
DE75: 1E 21           EXG     Y,X                   
DE77: B5 4E D4        BITA    $4ED4                   
DE7A: D9 5E           ADCB    $5E                   
DE7C: 00 00           NEG     $00                   
DE7E: 08 ; ????
DE7F: 0F 02           CLR     $02                   
DE81: 03 14           COM     $14                   
DE83: 06 77           ROR     $77                   
DE85: 70 14 97        NEG     $1497                   
DE88: 70 67 80        NEG     $6780                   
DE8B: 77 3D A1        ASR     $3DA1                   
DE8E: 26 D1           BNE     $DE61                   
DE90: 56              RORB                        
DE91: B9 3A 00        ADCA    $3A00                   
DE94: 00 00           NEG     $00                   
DE96: 00 06           NEG     $06                   
DE98: 0F 01           CLR     $01                   
DE9A: 03 14           COM     $14                   
DE9C: 02 ; ????
DE9D: 80 77           SUBA    #$77                  
DE9F: 3C 87           CWAI    $87                   
DEA1: 80 77           SUBA    #$77                  
DEA3: 87 ; ????
DEA4: 83 3C 8B        SUBD    #$3C8B                  
DEA7: 91 96           CMPA    $96                   
DEA9: 29 49           BVS     $DEF4                   
DEAB: 61 ; ????
DEAC: 66 EB           ROR     D,S                 
DEAE: 00 00           NEG     $00                   
DEB0: 08 ; ????
DEB1: 0F 01           CLR     $01                   
DEB3: 03 14           COM     $14                   
DEB5: 02 ; ????
DEB6: 87 ; ????
DEB7: 83 3C 87        SUBD    #$3C87                  
DEBA: 70 67 87        NEG     $6787                   
DEBD: 83 3D 8A        SUBD    #$3D8A                  
DEC0: 1A 9D           ORCC    #$9D                  
DEC2: A9 C9 DA 5D     ADCA    $DA5D,U                 
DEC6: 6B ; ????
DEC7: 3A              ABX                         
DEC8: 00 09           NEG     $09                   
DECA: 0F 01           CLR     $01                   
DECC: 03 1E           COM     $1E                   
DECE: 02 ; ????
DECF: 87 ; ????
DED0: 83 3C 90        SUBD    #$3C90                  
DED3: 77 77 90        ASR     $7790                   
DED6: 87 ; ????
DED7: 3D              MUL                         
DED8: 89 16           ADCA    #$16                  
DEDA: 9E 21           LDX     $21                   
DEDC: 29 49           BVS     $DF27                   
DEDE: 51 ; ????
DEDF: DE 66           LDU     $66                   
DEE1: E9 0A           ADCB    10,X                
DEE3: 0F 01           CLR     $01                   
DEE5: 03 0A           COM     $0A                   
DEE7: 08 ; ????
DEE8: 90 87           SUBA    $87                   
DEEA: 3C 97           CWAI    $97                   
DEEC: 80 70           SUBA    #$70                  
DEEE: 97 93           STA     $93                   
DEF0: 3D              MUL                         
DEF1: 0A 9E           DEC     $9E                   
DEF3: 2C CA           BGE     $DEBF                   
DEF5: DE 62           LDU     $62                   
DEF7: 99 EE           ADCA    $EE                   
DEF9: 00 00           NEG     $00                   
DEFB: 08 ; ????
DEFC: 0F 01           CLR     $01                   
DEFE: 03 10           COM     $10                   
DF00: 02 ; ????
DF01: 87 ; ????
DF02: 80 3C           SUBA    #$3C                  
DF04: 97 80           STA     $80                   
DF06: 77 A0 9A        ASR     $A09A                   
DF09: 3C 13           CWAI    $13                   
DF0B: A5 ; ????
DF0C: BE 5E E3        LDX     $5EE3                   
DF0F: 89 39           ADCA    #$39                  
DF11: 5A              DECB                        
DF12: 0C 61           INC     $61                   
DF14: 0A 0F           DEC     $0F                   
DF16: 01 ; ????
DF17: 03 10           COM     $10                   
DF19: 02 ; ????
DF1A: 80 87           SUBA    #$87                  
DF1C: 3C 90           CWAI    $90                   
DF1E: A0 80           SUBA    ,X+                 
DF20: A0 93           SUBA    [,--X]              
DF22: 2B 16           BMI     $DF3A                   
DF24: AA 2C           ORA     12,Y                
DF26: 4A              DECA                        
DF27: CC 69 6D        LDD     #$696D                  
DF2A: 1B ; ????
DF2B: EB 00           ADDB    0,X                 
DF2D: 09 0F           ROL     $0F                   
DF2F: 01 ; ????
DF30: 03 10           COM     $10                   
DF32: 02 ; ????
DF33: 97 93           STA     $93                   
DF35: 3C 87           CWAI    $87                   
DF37: 80 77           SUBA    #$77                  
DF39: 87 ; ????
DF3A: 83 53 11        SUBD    #$5311                  
DF3D: 15 ; ????
DF3E: 9E AA           LDX     $AA                   
DF40: AD CB           JSR     D,U                 
DF42: 56              RORB                        
DF43: 44              LSRA                        
DF44: 00 00           NEG     $00                   
DF46: 08 ; ????
DF47: 0F 01           CLR     $01                   
DF49: 03 10           COM     $10                   
DF4B: 02 ; ????
DF4C: 87 ; ????
DF4D: 83 3C 97        SUBD    #$3C97                  
DF50: 97 97           STA     $97                   
DF52: A7 ; ????
DF53: A7 44           STA     4,U                 
DF55: 8E 91 A1        LDX     #$91A1                  
DF58: 26 33           BNE     $DF8D                   
DF5A: C9 55           ADCB    #$55                  
DF5C: E4 69           ANDB    9,S                 
DF5E: 6E 0A           JMP     10,X                
DF60: 08 ; ????
DF61: 01 ; ????
DF62: 03 10           COM     $10                   
DF64: 02 ; ????
DF65: A7 ; ????
DF66: A7 3C           STA     -4,Y                
DF68: 90 87           SUBA    $87                   
DF6A: 80 A0           SUBA    #$A0                  
DF6C: 97 24           STA     $24                   
DF6E: 86 22           LDA     #$22                  
DF70: B3 36 01        SUBD    $3601                   
DF73: 40              NEGA                        
DF74: 00 00           NEG     $00                   
DF76: 00 00           NEG     $00                   
DF78: 06 08           ROR     $08                   
DF7A: 02 ; ????
DF7B: 10 ; ????
DF7C: 10 ; ????
DF7D: 03 A0           COM     $A0                   
DF7F: A0 20           SUBA    0,Y                 
DF81: 90 77           SUBA    $77                   
DF83: 70 87 80        NEG     $8780                   
DF86: 34 16           PSHS    X,B,A                   
DF88: 99 24           ADCA    $24                   
DF8A: 32 BD D3 DE     LEAS    [$B36C,PC]              
DF8E: 61 ; ????
DF8F: 6C 00           INC     0,X                 
DF91: 09 0F           ROL     $0F                   
DF93: 01 ; ????
DF94: 03 0A           COM     $0A                   
DF96: 05 ; ????
DF97: 87 ; ????
DF98: 80 3C           SUBA    #$3C                  
DF9A: 87 ; ????
DF9B: 70 67 87        NEG     $6787                   
DF9E: 83 3A 09        SUBD    #$3A09                  
DFA1: 15 ; ????
DFA2: B6 46 E6        LDA     $46E6                   
DFA5: E9 2C           ADCB    12,Y                
DFA7: CC 00 00        LDD     #$0000                  
DFAA: 08 ; ????
DFAB: 0F 01           CLR     $01                   
DFAD: 03 1E           COM     $1E                   
DFAF: 05 ; ????
DFB0: 87 ; ????
DFB1: 83 3C 90        SUBD    #$3C90                  
DFB4: 78 ; ????
DFB5: 70 80 78        NEG     $8078                   
DFB8: 3C 9E           CWAI    $9E                   
DFBA: 2E B2           BGT     $DF6E                   
DFBC: 35 C2           PULS    A,U,PC                   
DFBE: 45 ; ????
DFBF: 4E ; ????
DFC0: DE 00           LDU     $00                   
DFC2: 00 08           NEG     $08                   
DFC4: 0F 01           CLR     $01                   
DFC6: 03 08           COM     $08                   
DFC8: 05 ; ????
DFC9: 80 78           SUBA    #$78                  
DFCB: 3C A0           CWAI    $A0                   
DFCD: 90 87           SUBA    $87                   
DFCF: A0 A0           SUBA    ,Y+                 
DFD1: 3C 89           CWAI    $89                   
DFD3: 0C 8E           INC     $8E                   
DFD5: 1B ; ????
DFD6: 1D              SEX                         
DFD7: 3A              ABX                         
DFD8: CE CB E2        LDU     #$CBE2                  
DFDB: 65 ; ????
DFDC: 0A 08           DEC     $08                   
DFDE: 01 ; ????
DFDF: 03 08           COM     $08                   
DFE1: 06 A0           ROR     $A0                   
DFE3: A0 3C           SUBA    -4,Y                
DFE5: A0 ; ????
DFE6: 90 87           SUBA    $87                   
DFE8: A7 A0           STA     ,Y+                 
DFEA: 2C 10           BGE     $DFFC                   
DFEC: 12              NOP                         
DFED: 16 9C 25        LBRA    $7C15                   
DFF0: A6 2E           LDA     14,Y                
DFF2: B2 C0 C4        SBCA    $C0C4                   
DFF5: 0A 08           DEC     $08                   
DFF7: 02 ; ????
DFF8: 03 10           COM     $10                   
DFFA: 04 A7           LSR     $A7                   
DFFC: A0 20           SUBA    0,Y                 
DFFE: A0 80           SUBA    ,X+                 
E000: 80 A7           SUBA    #$A7                  
E002: A7 3C           STA     -4,Y                
E004: 8B 0C           ADDA    #$0C                  
E006: 13              SYNC                        
E007: 94 A6           ANDA    $A6                   
E009: 56              RORB                        
E00A: E3 64           ADDD    4,S                 
E00C: 6B ; ????
E00D: EC 0A           LDD     10,X                
E00F: 0F 01           CLR     $01                   
E011: 03 06           COM     $06                   
E013: 07 A7           ASR     $A7                   
E015: A7 3C           STA     -4,Y                
E017: A0 A0           SUBA    ,Y+                 
E019: 97 B0           STA     $B0                   
E01B: A7 34           STA     -12,Y               
E01D: 11 ; ????
E01E: 08 ; ????
E01F: 87 ; ????
E020: 61 ; ????
E021: 0C 24           INC     $24                   
E023: B3 D1 56        SUBD    $D156                   
E026: E4 0A           ANDB    10,X                
E028: 0F 01           CLR     $01                   
E02A: 05 ; ????
E02B: 0F 05           CLR     $05                   
E02D: A7 ; ????
E02E: A7 3C           STA     -4,Y                
E030: A0 ; ????
E031: 90 87           SUBA    $87                   
E033: A0 ; ????
E034: 97 44           STA     $44                   
E036: 09 8C           ROL     $8C                   
E038: 8E 1E AA        LDX     #$1EAA                  
E03B: 2C DE           BGE     $E01B                   
E03D: 65 ; ????
E03E: EC 6E           LDD     14,S                
E040: 0A 07           DEC     $07                   
E042: 01 ; ????
E043: 03 08           COM     $08                   
E045: 07 A0           ASR     $A0                   
E047: 97 3C           STA     $3C                   
E049: A0 ; ????
E04A: 90 87           SUBA    $87                   
E04C: A7 A0           STA     ,Y+                 
E04E: 24 ; ????
E04F: 19              DAA                         
E050: D5 03           BITB    $03                   
E052: 41 ; ????
E053: 83 C4 1B        SUBD    #$C41B                  
E056: AD B1           JSR     [,Y++]              
E058: C5 0A           BITB    #$0A                  
E05A: 08 ; ????
E05B: 02 ; ????
E05C: 08 ; ????
E05D: 08 ; ????
E05E: 06 A7           ROR     $A7                   
E060: A0 3C           SUBA    -4,Y                
E062: A0 80           SUBA    ,X+                 
E064: 77 B0 B0        ASR     $B0B0                   
E067: 23 8A           BLS     $DFF3                   
E069: 0C 3A           INC     $3A                   
E06B: BC 39 70        CMPX    $3970                   
E06E: 27 80           BEQ     $DFF0                   
E070: A1 D8 0A        CMPA    [$0A,U]               
E073: 08 ; ????
E074: 02 ; ????
E075: 10 ; ????
E076: 08 ; ????
E077: 08 ; ????
E078: B0 A7 14        SUBA    $A714                   
E07B: A0 ; ????
E07C: 97 90           STA     $90                   
E07E: A7 ; ????
E07F: A7 3D           STA     -3,Y                
E081: 09 9E           ROL     $9E                   
E083: A1 24           CMPA    4,Y                 
E085: 3A              ABX                         
E086: 51 ; ????
E087: D4 E5           ANDB    $E5                   
E089: EA 6E           ORB     14,S                
E08B: 0A 04           DEC     $04                   
E08D: 02 ; ????
E08E: 20 08           BRA     $E098                   
E090: 08 ; ????
E091: B7 B7 3C        STA     $B73C                   
E094: E0 D4           SUBB    [,U]                
E096: E1 07           CMPB    7,X                 
E098: E1 2E           CMPB    14,Y                
E09A: E1 61           CMPB    1,S                 
E09C: E1 98 E1        CMPB    [$E1,X]               
E09F: BB E1 D2        ADDA    $E1D2                   
E0A2: E1 ; ????
E0A3: D7 E1           STB     $E1                   
E0A5: FA E2 1F        ORB     $E21F                   
E0A8: E2 20           SBCB    0,Y                 
E0AA: E2 83           SBCB    ,--X                
E0AC: E2 ; ????
E0AD: 9E E2           LDX     $E2                   
E0AF: BB E3 0C        ADDA    $E30C                   
E0B2: E3 2D           ADDD    13,Y                
E0B4: E3 72           ADDD    -14,S               
E0B6: E3 A3           ADDD    ,--Y                
E0B8: E3 D6           ADDD    [A,U]               
E0BA: E4 01           ANDB    1,X                 
E0BC: E4 84           ANDB    ,X                  
E0BE: E4 AD E4 BE     ANDB    $C580,PC                
E0C2: E4 DF E4 E6     ANDB    [$E4E6]                 
E0C6: E4 F3           ANDB    [,--S]              
E0C8: E5 26           BITB    6,Y                 
E0CA: E5 27           BITB    7,Y                 
E0CC: E5 52           BITB    -14,U               
E0CE: E5 6F           BITB    15,S                
E0D0: E5 94           BITB    [,X]                
E0D2: E5 9B           BITB    [D,X]               
E0D4: 19              DAA                         
E0D5: 08 ; ????
E0D6: 1C 08           ANDCC   #$08                  
E0D8: 1D              SEX                         
E0D9: 08 ; ????
E0DA: 1E 08           EXG     D,A                   
E0DC: 21 08           BRN     $E0E6                   
E0DE: 22 08           BHI     $E0E8                   
E0E0: 23 0A           BLS     $E0EC                   
E0E2: 24 ; ????
E0E3: 0A 25           DEC     $25                   
E0E5: 02 ; ????
E0E6: 26 06           BNE     $E0EE                   
E0E8: 29 03           BVS     $E0ED                   
E0EA: 2A 06           BPL     $E0F2                   
E0EC: 2B 03           BMI     $E0F1                   
E0EE: 2C 0A           BGE     $E0FA                   
E0F0: 2D 08           BLT     $E0FA                   
E0F2: 2E 04           BGT     $E0F8                   
E0F4: 31 05           LEAY    5,X                 
E0F6: 32 05           LEAS    5,X                 
E0F8: 33 09           LEAU    9,X                 
E0FA: 34 0A           PSHS    DP,A                   
E0FC: 35 02           PULS    A                   
E0FE: 36 04           PSHU    B                   
E100: 3A              ABX                         
E101: 01 ; ????
E102: 3B              RTI                         
E103: 02 ; ????
E104: 3C 02           CWAI    $02                   
E106: 3D              MUL                         
E107: 13              SYNC                        
E108: 08 ; ????
E109: 0D 04           TST     $04                   
E10B: 11 ; ????
E10C: 01 ; ????
E10D: 12              NOP                         
E10E: 08 ; ????
E10F: 14 ; ????
E110: 02 ; ????
E111: 15 ; ????
E112: 04 19           LSR     $19                   
E114: 09 1A           ROL     $1A                   
E116: 04 1B           LSR     $1B                   
E118: 03 1C           COM     $1C                   
E11A: 02 ; ????
E11B: 22 08           BHI     $E125                   
E11D: 24 ; ????
E11E: 0C 2A           INC     $2A                   
E120: 01 ; ????
E121: 2B 0A           BMI     $E12D                   
E123: 2C 08           BGE     $E12D                   
E125: 31 02           LEAY    2,X                 
E127: 32 06           LEAS    6,X                 
E129: 34 01           PSHS    CC                   
E12B: 35 02           PULS    A                   
E12D: 39              RTS                         
E12E: 19              DAA                         
E12F: 08 ; ????
E130: 14 ; ????
E131: 08 ; ????
E132: 15 ; ????
E133: 08 ; ????
E134: 16 08 19        LBRA    $E950                   
E137: 08 ; ????
E138: 1A 08           ORCC    #$08                  
E13A: 1B ; ????
E13B: 0A 1C           DEC     $1C                   
E13D: 0A 1D           DEC     $1D                   
E13F: 02 ; ????
E140: 1E 06           EXG     D,?                   
E142: 21 03           BRN     $E147                   
E144: 22 06           BHI     $E14C                   
E146: 23 03           BLS     $E14B                   
E148: 24 ; ????
E149: 0A 25           DEC     $25                   
E14B: 08 ; ????
E14C: 26 04           BNE     $E152                   
E14E: 29 05           BVS     $E155                   
E150: 2A 05           BPL     $E157                   
E152: 2B 09           BMI     $E15D                   
E154: 2C 0A           BGE     $E160                   
E156: 2D 02           BLT     $E15A                   
E158: 2E 04           BGT     $E15E                   
E15A: 32 01           LEAS    1,X                 
E15C: 33 02           LEAU    2,X                 
E15E: 34 02           PSHS    A                   
E160: 35 1B           PULS    CC,A,DP,X                   
E162: 04 0B           LSR     $0B                   
E164: 05 ; ????
E165: 0C 05           INC     $05                   
E167: 0D 01           TST     $01                   
E169: 0E 08           JMP     $08                   
E16B: 12              NOP                         
E16C: 0C 13           INC     $13                   
E16E: 05 ; ????
E16F: 14 ; ????
E170: 09 15           ROL     $15                   
E172: 0A 1A           DEC     $1A                   
E174: 02 ; ????
E175: 1B ; ????
E176: 0A 1D           DEC     $1D                   
E178: 0A 22           DEC     $22                   
E17A: 0A 25           DEC     $25                   
E17C: 0A 2A           DEC     $2A                   
E17E: 08 ; ????
E17F: 2B 04           BMI     $E185                   
E181: 2C 03           BGE     $E186                   
E183: 2D 04           BLT     $E189                   
E185: 31 0B           LEAY    11,X                
E187: 32 06           LEAS    6,X                 
E189: 33 05           LEAU    5,X                 
E18B: 34 0D           PSHS    DP,B,CC                   
E18D: 35 01           PULS    CC                   
E18F: 36 02           PSHU    A                   
E191: 3A              ABX                         
E192: 04 3B           LSR     $3B                   
E194: 01 ; ????
E195: 3C 02           CWAI    $02                   
E197: 3D              MUL                         
E198: 11 ; ????
E199: 08 ; ????
E19A: 0B ; ????
E19B: 08 ; ????
E19C: 0C 08           INC     $08                   
E19E: 0D 08           TST     $08                   
E1A0: 0E 08           JMP     $08                   
E1A2: 12              NOP                         
E1A3: 0A 13           DEC     $13                   
E1A5: 0A 14           DEC     $14                   
E1A7: 0A 15           DEC     $15                   
E1A9: 02 ; ????
E1AA: 16 02 1A        LBRA    $E3C7                   
E1AD: 02 ; ????
E1AE: 1B ; ????
E1AF: 0A 1C           DEC     $1C                   
E1B1: 0A 1D           DEC     $1D                   
E1B3: 08 ; ????
E1B4: 1E 02           EXG     D,Y                   
E1B6: 24 ; ????
E1B7: 02 ; ????
E1B8: 25 ; ????
E1B9: 02 ; ????
E1BA: 26 0B           BNE     $E1C7                   
E1BC: 04 1C           LSR     $1C                   
E1BE: 01 ; ????
E1BF: 1D              SEX                         
E1C0: 08 ; ????
E1C1: 1E 04           EXG     D,X                   
E1C3: 24 ; ????
E1C4: 09 25           ROL     $25                   
E1C6: 02 ; ????
E1C7: 26 02           BNE     $E1CB                   
E1C9: 2D 08           BLT     $E1D3                   
E1CB: 4D              TSTA                        
E1CC: 06 55           ROR     $55                   
E1CE: 09 56           ROL     $56                   
E1D0: 02 ; ????
E1D1: 5E ; ????
E1D2: 02 ; ????
E1D3: 04 3B           LSR     $3B                   
E1D5: 01 ; ????
E1D6: 3C 11           CWAI    $11                   
E1D8: 08 ; ????
E1D9: 11 ; ????
E1DA: 08 ; ????
E1DB: 12              NOP                         
E1DC: 04 14           LSR     $14                   
E1DE: 01 ; ????
E1DF: 15 ; ????
E1E0: 02 ; ????
E1E1: 19              DAA                         
E1E2: 02 ; ????
E1E3: 1A 08           ORCC    #$08                  
E1E5: 35 02           PULS    A                   
E1E7: 3D              MUL                         
E1E8: 08 ; ????
E1E9: 43              COMA                        
E1EA: 02 ; ????
E1EB: 4B ; ????
E1EC: 08 ; ????
E1ED: 4A              DECA                        
E1EE: 02 ; ????
E1EF: 52 ; ????
E1F0: 08 ; ????
E1F1: 5D              TSTB                        
E1F2: 08 ; ????
E1F3: 5E ; ????
E1F4: 04 64           LSR     $64                   
E1F6: 03 65           COM     $65                   
E1F8: 02 ; ????
E1F9: 66 12           ROR     -14,X               
E1FB: 04 11           LSR     $11                   
E1FD: 01 ; ????
E1FE: 12              NOP                         
E1FF: 04 15           LSR     $15                   
E201: 01 ; ????
E202: 16 04 19        LBRA    $E61E                   
E205: 09 1A           ROL     $1A                   
E207: 0C 1D           INC     $1D                   
E209: 01 ; ????
E20A: 1E 0A           EXG     D,CC                   
E20C: 22 0A           BHI     $E218                   
E20E: 25 ; ????
E20F: 04 29           LSR     $29                   
E211: 03 2A           COM     $2A                   
E213: 06 2D           ROR     $2D                   
E215: 01 ; ????
E216: 2E 04           BGT     $E21C                   
E218: 31 01           LEAY    1,X                 
E21A: 32 04           LEAS    4,X                 
E21C: 35 01           PULS    CC                   
E21E: 36 00           PSHU                       
E220: 31 08           LEAY    8,X                 
E222: 19              DAA                         
E223: 08 ; ????
E224: 1A 08           ORCC    #$08                  
E226: 1B ; ????
E227: 04 1C           LSR     $1C                   
E229: 01 ; ????
E22A: 1D              SEX                         
E22B: 08 ; ????
E22C: 1E 02           EXG     D,Y                   
E22E: 21 02           BRN     $E232                   
E230: 22 02           BHI     $E234                   
E232: 23 08           BLS     $E23C                   
E234: 24 ; ????
E235: 08 ; ????
E236: 25 ; ????
E237: 02 ; ????
E238: 26 04           BNE     $E23E                   
E23A: 29 05           BVS     $E241                   
E23C: 2A 01           BPL     $E23F                   
E23E: 2B 0A           BMI     $E24A                   
E240: 2C 0A           BGE     $E24C                   
E242: 2D 04           BLT     $E248                   
E244: 31 09           LEAY    9,X                 
E246: 32 08           LEAS    8,X                 
E248: 33 06           LEAU    6,X                 
E24A: 34 0B           PSHS    DP,A,CC                   
E24C: 35 08           PULS    DP                   
E24E: 36 04           PSHU    B                   
E250: 39              RTS                         
E251: 03 3A           COM     $3A                   
E253: 02 ; ????
E254: 3B              RTI                         
E255: 08 ; ????
E256: 3C 0A           CWAI    $0A                   
E258: 3D              MUL                         
E259: 02 ; ????
E25A: 3E              RESET                       
E25B: 08 ; ????
E25C: 41 ; ????
E25D: 04 42           LSR     $42                   
E25F: 01 ; ????
E260: 43              COMA                        
E261: 06 44           ROR     $44                   
E263: 03 45           COM     $45                   
E265: 08 ; ????
E266: 46              RORA                        
E267: 02 ; ????
E268: 49              ROLA                        
E269: 08 ; ????
E26A: 4A              DECA                        
E26B: 0C 4B           INC     $4B                   
E26D: 05 ; ????
E26E: 4C              INCA                        
E26F: 05 ; ????
E270: 4D              TSTA                        
E271: 03 4E           COM     $4E                   
E273: 08 ; ????
E274: 51 ; ????
E275: 06 52           ROR     $52                   
E277: 03 53           COM     $53                   
E279: 0C 54           INC     $54                   
E27B: 09 55           ROL     $55                   
E27D: 02 ; ????
E27E: 5C              INCB                        
E27F: 02 ; ????
E280: 59              ROLB                        
E281: 02 ; ????
E282: 5D              TSTB                        
E283: 0D 08           TST     $08                   
E285: 2D 02           BLT     $E289                   
E287: 35 08           PULS    DP                   
E289: 36 08           PSHU    DP                   
E28B: 39              RTS                         
E28C: 0A 3E           DEC     $3E                   
E28E: 02 ; ????
E28F: 41 ; ????
E290: 08 ; ????
E291: 42 ; ????
E292: 02 ; ????
E293: 46              RORA                        
E294: 02 ; ????
E295: 4A              DECA                        
E296: 04 4D           LSR     $4D                   
E298: 01 ; ????
E299: 4E ; ????
E29A: 04 55           LSR     $55                   
E29C: 01 ; ????
E29D: 56              RORB                        
E29E: 0E 04           JMP     $04                   
E2A0: 32 01           LEAS    1,X                 
E2A2: 33 08           LEAU    8,X                 
E2A4: 34 08           PSHS    DP                   
E2A6: 35 04           PULS    B                   
E2A8: 3A              ABX                         
E2A9: 01 ; ????
E2AA: 3B              RTI                         
E2AB: 02 ; ????
E2AC: 3C 02           CWAI    $02                   
E2AE: 3D              MUL                         
E2AF: 04 43           LSR     $43                   
E2B1: 01 ; ????
E2B2: 44              LSRA                        
E2B3: 08 ; ????
E2B4: 56              RORB                        
E2B5: 08 ; ????
E2B6: 5D              TSTB                        
E2B7: 02 ; ????
E2B8: 5E ; ????
E2B9: 02 ; ????
E2BA: 65 ; ????
E2BB: 28 08           BVC     $E2C5                   
E2BD: 12              NOP                         
E2BE: 0C 13           INC     $13                   
E2C0: 09 14           ROL     $14                   
E2C2: 08 ; ????
E2C3: 15 ; ????
E2C4: 04 19           LSR     $19                   
E2C6: 0B ; ????
E2C7: 1A 06           ORCC    #$06                  
E2C9: 1B ; ????
E2CA: 03 1C           COM     $1C                   
E2CC: 0E 1D           JMP     $1D                   
E2CE: 01 ; ????
E2CF: 1E 02           EXG     D,Y                   
E2D1: 22 04           BHI     $E2D7                   
E2D3: 23 01           BLS     $E2D6                   
E2D5: 24 ; ????
E2D6: 02 ; ????
E2D7: 25 ; ????
E2D8: 04 29           LSR     $29                   
E2DA: 01 ; ????
E2DB: 2A 04           BPL     $E2E1                   
E2DD: 31 01           LEAY    1,X                 
E2DF: 32 04           LEAS    4,X                 
E2E1: 41 ; ????
E2E2: 01 ; ????
E2E3: 42 ; ????
E2E4: 04 49           LSR     $49                   
E2E6: 01 ; ????
E2E7: 4A              DECA                        
E2E8: 08 ; ????
E2E9: 52 ; ????
E2EA: 04 53           LSR     $53                   
E2EC: 01 ; ????
E2ED: 54              LSRB                        
E2EE: 08 ; ????
E2EF: 55 ; ????
E2F0: 04 59           LSR     $59                   
E2F2: 0B ; ????
E2F3: 5A              DECB                        
E2F4: 0C 5B           INC     $5B                   
E2F6: 09 5C           ROL     $5C                   
E2F8: 0E 5D           JMP     $5D                   
E2FA: 01 ; ????
E2FB: 5E ; ????
E2FC: 02 ; ????
E2FD: 62 ; ????
E2FE: 06 63           ROR     $63                   
E300: 03 64           COM     $64                   
E302: 02 ; ????
E303: 65 ; ????
E304: 04 0B           LSR     $0B                   
E306: 01 ; ????
E307: 0C 04           INC     $04                   
E309: 6B ; ????
E30A: 01 ; ????
E30B: 6C 10           INC     -16,X               
E30D: 08 ; ????
E30E: 22 08           BHI     $E318                   
E310: 25 ; ????
E311: 02 ; ????
E312: 2A 08           BPL     $E31C                   
E314: 2B 08           BMI     $E31E                   
E316: 2C 02           BGE     $E31A                   
E318: 2D 02           BLT     $E31C                   
E31A: 33 02           LEAU    2,X                 
E31C: 34 08           PSHS    DP                   
E31E: 43              COMA                        
E31F: 08 ; ????
E320: 44              LSRA                        
E321: 08 ; ????
E322: 4A              DECA                        
E323: 02 ; ????
E324: 4B ; ????
E325: 02 ; ????
E326: 4C              INCA                        
E327: 08 ; ????
E328: 4D              TSTA                        
E329: 02 ; ????
E32A: 52 ; ????
E32B: 02 ; ????
E32C: 55 ; ????
E32D: 22 04           BHI     $E333                   
E32F: 15 ; ????
E330: 01 ; ????
E331: 16 04 1D        LBRA    $E751                   
E334: 01 ; ????
E335: 1E 0C           EXG     D,?                   
E337: 22 09           BHI     $E342                   
E339: 23 02           BLS     $E33D                   
E33B: 2A 02           BPL     $E33F                   
E33D: 2B 0C           BMI     $E34B                   
E33F: 2C 01           BGE     $E342                   
E341: 2D 0A           BLT     $E34D                   
E343: 34 08           PSHS    DP                   
E345: 35 08           PULS    DP                   
E347: 3B              RTI                         
E348: 02 ; ????
E349: 3C 02           CWAI    $02                   
E34B: 3D              MUL                         
E34C: 08 ; ????
E34D: 3E              RESET                       
E34E: 02 ; ????
E34F: 43              COMA                        
E350: 0C 44           INC     $44                   
E352: 01 ; ????
E353: 45 ; ????
E354: 02 ; ????
E355: 46              RORA                        
E356: 04 4B           LSR     $4B                   
E358: 03 4C           COM     $4C                   
E35A: 08 ; ????
E35B: 52 ; ????
E35C: 08 ; ????
E35D: 53              COMB                        
E35E: 02 ; ????
E35F: 5A              DECB                        
E360: 02 ; ????
E361: 5B ; ????
E362: 04 5D           LSR     $5D                   
E364: 01 ; ????
E365: 5E ; ????
E366: 0C 63           INC     $63                   
E368: 09 64           ROL     $64                   
E36A: 04 65           LSR     $65                   
E36C: 01 ; ????
E36D: 66 02           ROR     2,X                 
E36F: 6B ; ????
E370: 02 ; ????
E371: 6C 18           INC     -8,X                
E373: 08 ; ????
E374: 22 04           BHI     $E37A                   
E376: 24 ; ????
E377: 09 25           ROL     $25                   
E379: 02 ; ????
E37A: 2A 08           BPL     $E384                   
E37C: 2B 02           BMI     $E380                   
E37E: 2D 04           BLT     $E384                   
E380: 31 01           LEAY    1,X                 
E382: 32 02           LEAS    2,X                 
E384: 33 04           LEAU    4,X                 
E386: 39              RTS                         
E387: 01 ; ????
E388: 3A              ABX                         
E389: 08 ; ????
E38A: 4B ; ????
E38B: 08 ; ????
E38C: 4C              INCA                        
E38D: 08 ; ????
E38E: 52 ; ????
E38F: 02 ; ????
E390: 53              COMB                        
E391: 02 ; ????
E392: 54              LSRB                        
E393: 08 ; ????
E394: 56              RORB                        
E395: 02 ; ????
E396: 5A              DECB                        
E397: 04 5C           LSR     $5C                   
E399: 09 5D           ROL     $5D                   
E39B: 02 ; ????
E39C: 5E ; ????
E39D: 02 ; ????
E39E: 65 ; ????
E39F: 04 39           LSR     $39                   
E3A1: 01 ; ????
E3A2: 3A              ABX                         
E3A3: 19              DAA                         
E3A4: 04 14           LSR     $14                   
E3A6: 09 15           ROL     $15                   
E3A8: 08 ; ????
E3A9: 16 02 1D        LBRA    $E5C9                   
E3AC: 02 ; ????
E3AD: 1E 0C           EXG     D,?                   
E3AF: 22 05           BHI     $E3B6                   
E3B1: 23 09           BLS     $E3BC                   
E3B3: 24 ; ????
E3B4: 0E 2A           JMP     $2A                   
E3B6: 05 ; ????
E3B7: 2B 0B           BMI     $E3C4                   
E3B9: 2C 06           BGE     $E3C1                   
E3BB: 32 05           LEAS    5,X                 
E3BD: 33 03           LEAU    3,X                 
E3BF: 34 08           PSHS    DP                   
E3C1: 3A              ABX                         
E3C2: 06 42           ROR     $42                   
E3C4: 09 43           ROL     $43                   
E3C6: 08 ; ????
E3C7: 44              LSRA                        
E3C8: 06 4B           ROR     $4B                   
E3CA: 03 4C           COM     $4C                   
E3CC: 04 53           LSR     $53                   
E3CE: 01 ; ????
E3CF: 54              LSRB                        
E3D0: 08 ; ????
E3D1: 5D              TSTB                        
E3D2: 04 64           LSR     $64                   
E3D4: 03 65           COM     $65                   
E3D6: 13              SYNC                        
E3D7: 08 ; ????
E3D8: 1E 08           EXG     D,A                   
E3DA: 25 ; ????
E3DB: 06 2D           ROR     $2D                   
E3DD: 01 ; ????
E3DE: 2E 08           BGT     $E3E8                   
E3E0: 36 02           PSHU    A                   
E3E2: 3E              RESET                       
E3E3: 08 ; ????
E3E4: 45 ; ????
E3E5: 08 ; ????
E3E6: 4B ; ????
E3E7: 06 4D           ROR     $4D                   
E3E9: 01 ; ????
E3EA: 4E ; ????
E3EB: 04 52           LSR     $52                   
E3ED: 07 53           ASR     $53                   
E3EF: 01 ; ????
E3F0: 54              LSRB                        
E3F1: 04 55           LSR     $55                   
E3F3: 09 56           ROL     $56                   
E3F5: 04 5A           LSR     $5A                   
E3F7: 01 ; ????
E3F8: 5B ; ????
E3F9: 02 ; ????
E3FA: 5E ; ????
E3FB: 02 ; ????
E3FC: 26 04           BNE     $E402                   
E3FE: 39              RTS                         
E3FF: 01 ; ????
E400: 3A              ABX                         
E401: 41 ; ????
E402: 04 0A           LSR     $0A                   
E404: 01 ; ????
E405: 0B ; ????
E406: 08 ; ????
E407: 0D 08           TST     $08                   
E409: 0E 0C           JMP     $0C                   
E40B: 11 ; ????
E40C: 01 ; ????
E40D: 12              NOP                         
E40E: 04 13           LSR     $13                   
E410: 09 14           ROL     $14                   
E412: 02 ; ????
E413: 15 ; ????
E414: 02 ; ????
E415: 16 02 19        LBRA    $E631                   
E418: 08 ; ????
E419: 1B ; ????
E41A: 02 ; ????
E41B: 1C 04           ANDCC   #$04                  
E41D: 1D              SEX                         
E41E: 09 1E           ROL     $1E                   
E420: 08 ; ????
E421: 22 06           BHI     $E429                   
E423: 23 01           BLS     $E426                   
E425: 24 ; ????
E426: 08 ; ????
E427: 25 ; ????
E428: 02 ; ????
E429: 26 04           BNE     $E42F                   
E42B: 29 03           BVS     $E430                   
E42D: 2A 08           BPL     $E437                   
E42F: 2B 04           BMI     $E435                   
E431: 2C 03           BGE     $E436                   
E433: 2D 08           BLT     $E43D                   
E435: 31 06           LEAY    6,X                 
E437: 33 01           LEAU    1,X                 
E439: 34 0C           PSHS    DP,B                   
E43B: 35 01           PULS    CC                   
E43D: 36 02           PSHU    A                   
E43F: 39              RTS                         
E440: 0C 3A           INC     $3A                   
E442: 01 ; ????
E443: 3B              RTI                         
E444: 08 ; ????
E445: 3C 02           CWAI    $02                   
E447: 3D              MUL                         
E448: 08 ; ????
E449: 41 ; ????
E44A: 06 42           ROR     $42                   
E44C: 01 ; ????
E44D: 43              COMA                        
E44E: 06 44           ROR     $44                   
E450: 01 ; ????
E451: 45 ; ????
E452: 08 ; ????
E453: 46              RORA                        
E454: 06 49           ROR     $49                   
E456: 09 4A           ROL     $4A                   
E458: 08 ; ????
E459: 4C              INCA                        
E45A: 08 ; ????
E45B: 4D              TSTA                        
E45C: 02 ; ????
E45D: 4E ; ????
E45E: 02 ; ????
E45F: 52 ; ????
E460: 08 ; ????
E461: 53              COMB                        
E462: 06 54           ROR     $54                   
E464: 03 55           COM     $55                   
E466: 08 ; ????
E467: 56              RORB                        
E468: 08 ; ????
E469: 59              ROLB                        
E46A: 06 5B           ROR     $5B                   
E46C: 01 ; ????
E46D: 5C              INCB                        
E46E: 08 ; ????
E46F: 5D              TSTB                        
E470: 02 ; ????
E471: 5E ; ????
E472: 0C 62           INC     $62                   
E474: 01 ; ????
E475: 63 08           COM     8,X                 
E477: 64 06           LSR     6,X                 
E479: 65 ; ????
E47A: 01 ; ????
E47B: 66 04           ROR     4,X                 
E47D: 69 03           ROL     3,X                 
E47F: 6A 02           DEC     2,X                 
E481: 6C 02           INC     2,X                 
E483: 61 ; ????
E484: 14 ; ????
E485: 0C 14           INC     $14                   
E487: 09 15           ROL     $15                   
E489: 0C 1A           INC     $1A                   
E48B: 09 1B           ROL     $1B                   
E48D: 06 1C           ROR     $1C                   
E48F: 03 1D           COM     $1D                   
E491: 08 ; ????
E492: 21 06           BRN     $E49A                   
E494: 22 03           BHI     $E499                   
E496: 23 0C           BLS     $E4A4                   
E498: 25 ; ????
E499: 09 26           ROL     $26                   
E49B: 02 ; ????
E49C: 29 0C           BVS     $E4AA                   
E49E: 2B 09           BMI     $E4A9                   
E4A0: 2C 06           BGE     $E4A8                   
E4A2: 2D 03           BLT     $E4A7                   
E4A4: 2E 06           BGT     $E4AC                   
E4A6: 33 03           LEAU    3,X                 
E4A8: 34 04           PSHS    B                   
E4AA: 3C 01           CWAI    $01                   
E4AC: 3D              MUL                         
E4AD: 08 ; ????
E4AE: 08 ; ????
E4AF: 2B 04           BMI     $E4B5                   
E4B1: 32 03           LEAS    3,X                 
E4B3: 33 0C           LEAU    12,X                
E4B5: 35 01           PULS    CC                   
E4B7: 36 04           PSHU    B                   
E4B9: 3B              RTI                         
E4BA: 01 ; ????
E4BB: 3C 02           CWAI    $02                   
E4BD: 3D              MUL                         
E4BE: 10 ; ????
E4BF: 04 1B           LSR     $1B                   
E4C1: 01 ; ????
E4C2: 1C 08           ANDCC   #$08                  
E4C4: 1E 02           EXG     D,Y                   
E4C6: 26 04           BNE     $E4CC                   
E4C8: 2C 01           BGE     $E4CB                   
E4CA: 2D 04           BLT     $E4D0                   
E4CC: 4B ; ????
E4CD: 05 ; ????
E4CE: 4C              INCA                        
E4CF: 01 ; ????
E4D0: 4D              TSTA                        
E4D1: 04 53           LSR     $53                   
E4D3: 09 54           ROL     $54                   
E4D5: 08 ; ????
E4D6: 55 ; ????
E4D7: 08 ; ????
E4D8: 5A              DECB                        
E4D9: 02 ; ????
E4DA: 5C              INCB                        
E4DB: 02 ; ????
E4DC: 5D              TSTB                        
E4DD: 02 ; ????
E4DE: 62 ; ????
E4DF: 03 08           COM     $08                   
E4E1: 35 0A           PULS    A,DP                   
E4E3: 3D              MUL                         
E4E4: 02 ; ????
E4E5: 45 ; ????
E4E6: 06 04           ROR     $04                   
E4E8: 0B ; ????
E4E9: 01 ; ????
E4EA: 0C 04           INC     $04                   
E4EC: 43              COMA                        
E4ED: 01 ; ????
E4EE: 44              LSRA                        
E4EF: 08 ; ????
E4F0: 46              RORA                        
E4F1: 02 ; ????
E4F2: 4E ; ????
E4F3: 19              DAA                         
E4F4: 04 14           LSR     $14                   
E4F6: 09 15           ROL     $15                   
E4F8: 08 ; ????
E4F9: 16 04 1B        LBRA    $E917                   
E4FC: 09 1C           ROL     $1C                   
E4FE: 0A 1D           DEC     $1D                   
E500: 02 ; ????
E501: 1E 08           EXG     D,A                   
E503: 21 06           BRN     $E50B                   
E505: 24 ; ????
E506: 03 25           COM     $25                   
E508: 08 ; ????
E509: 26 02           BNE     $E50D                   
E50B: 29 08           BVS     $E515                   
E50D: 2A 08           BPL     $E517                   
E50F: 2B 02           BMI     $E513                   
E511: 2E 08           BGT     $E51B                   
E513: 31 06           LEAY    6,X                 
E515: 32 03           LEAS    3,X                 
E517: 33 08           LEAU    8,X                 
E519: 34 04           PSHS    B                   
E51B: 35 01           PULS    CC                   
E51D: 36 02           PSHU    A                   
E51F: 39              RTS                         
E520: 04 3A           LSR     $3A                   
E522: 01 ; ????
E523: 3B              RTI                         
E524: 02 ; ????
E525: 3C 00           CWAI    $00                   
E527: 15 ; ????
E528: 08 ; ????
E529: 0B ; ????
E52A: 02 ; ????
E52B: 13              SYNC                        
E52C: 0C 1B           INC     $1B                   
E52E: 09 1C           ROL     $1C                   
E530: 06 23           ROR     $23                   
E532: 03 24           COM     $24                   
E534: 04 25           LSR     $25                   
E536: 01 ; ????
E537: 26 08           BNE     $E541                   
E539: 4A              DECA                        
E53A: 04 4B           LSR     $4B                   
E53C: 01 ; ????
E53D: 4C              INCA                        
E53E: 02 ; ????
E53F: 52 ; ????
E540: 04 53           LSR     $53                   
E542: 05 ; ????
E543: 54              LSRB                        
E544: 01 ; ????
E545: 55 ; ????
E546: 04 5A           LSR     $5A                   
E548: 01 ; ????
E549: 5B ; ????
E54A: 04 62           LSR     $62                   
E54C: 01 ; ????
E54D: 63 04           COM     4,X                 
E54F: 64 01           LSR     1,X                 
E551: 65 ; ????
E552: 0E 04           JMP     $04                   
E554: 1A 01           ORCC    #$01                  
E556: 1B ; ????
E557: 08 ; ????
E558: 22 08           BHI     $E562                   
E55A: 24 ; ????
E55B: 02 ; ????
E55C: 2A 08           BPL     $E566                   
E55E: 2B 02           BMI     $E562                   
E560: 2C 08           BGE     $E56A                   
E562: 32 02           LEAS    2,X                 
E564: 33 02           LEAU    2,X                 
E566: 3A              ABX                         
E567: 04 3C           LSR     $3C                   
E569: 01 ; ????
E56A: 3D              MUL                         
E56B: 08 ; ????
E56C: 4B ; ????
E56D: 02 ; ????
E56E: 53              COMB                        
E56F: 12              NOP                         
E570: 08 ; ????
E571: 13              SYNC                        
E572: 08 ; ????
E573: 15 ; ????
E574: 0E 1B           JMP     $1B                   
E576: 05 ; ????
E577: 1C 03           ANDCC   #$03                  
E579: 1D              SEX                         
E57A: 02 ; ????
E57B: 23 0C           BLS     $E589                   
E57D: 24 ; ????
E57E: 01 ; ????
E57F: 25 ; ????
E580: 0C 2A           INC     $2A                   
E582: 09 2B           ROL     $2B                   
E584: 02 ; ????
E585: 2C 06           BGE     $E58D                   
E587: 32 03           LEAS    3,X                 
E589: 33 0C           LEAU    12,X                
E58B: 35 01           PULS    CC                   
E58D: 36 02           PSHU    A                   
E58F: 3D              MUL                         
E590: 08 ; ????
E591: 3E              RESET                       
E592: 02 ; ????
E593: 46              RORA                        
E594: 03 08           COM     $08                   
E596: 1B ; ????
E597: 0A 23           DEC     $23                   
E599: 02 ; ????
E59A: 2B 0F           BMI     $E5AB                   
E59C: 04 1C           LSR     $1C                   
E59E: 09 1D           ROL     $1D                   
E5A0: 08 ; ????
E5A1: 5D              TSTB                        
E5A2: 02 ; ????
E5A3: 25 ; ????
E5A4: 02 ; ????
E5A5: 65 ; ????
E5A6: 08 ; ????
E5A7: 22 02           BHI     $E5AB                   
E5A9: 2A 04           BPL     $E5AF                   
E5AB: 3A              ABX                         
E5AC: 01 ; ????
E5AD: 3B              RTI                         
E5AE: 08 ; ????
E5AF: 4C              INCA                        
E5B0: 02 ; ????
E5B1: 54              LSRB                        
E5B2: 04 5B           LSR     $5B                   
E5B4: 01 ; ????
E5B5: 5C              INCB                        
E5B6: 04 63           LSR     $63                   
E5B8: 01 ; ????
E5B9: 64 


Reset:
E5BA: 7F 38 00        CLR     $3800
E5BD: B6 80 00        CLR     $8000
E5C0: 1C FF           ANDCC   #$FF                  
E5C2: B6 80 00        LDA     $8000                   
E5C5: 7F 50 02        CLR     $5002                   
E5C8: 7F 50 0A        CLR     $500A                   
E5CB: 7F 50 08        CLR     $5008                   
E5CE: 86 08           LDA     #$08                  
E5D0: 8E 00 00        LDX     #$0000                  
E5D3: A7 84           STA     ,X                  
E5D5: 7F 80 00        CLR     $8000                   
E5D8: A1 80           CMPA    ,X+                 
E5DA: 26 3D           BNE     $E619                   
E5DC: 8C 28 00        CMPX    #$2800                  
E5DF: 26 F2           BNE     $E5D3                   
E5E1: 8E 40 40        LDX     #$4040                  
E5E4: A7 84           STA     ,X                  
E5E6: 7F 80 00        CLR     $8000                   
E5E9: A1 80           CMPA    ,X+                 
E5EB: 26 38           BNE     $E625                   
E5ED: 8C 44 00        CMPX    #$4400                  
E5F0: 26 F2           BNE     $E5E4                   
E5F2: 8E 00 00        LDX     #$0000                  
E5F5: E6 84           LDB     ,X                  
E5F7: 7F 80 00        CLR     $8000                   
E5FA: E1 80           CMPB    ,X+                 
E5FC: 26 1B           BNE     $E619                   
E5FE: 8C 28 00        CMPX    #$2800                  
E601: 26 F2           BNE     $E5F5                   
E603: 8E 40 40        LDX     #$4040                  
E606: E6 84           LDB     ,X                  
E608: 7F 80 00        CLR     $8000                   
E60B: E1 80           CMPB    ,X+                 
E60D: 26 16           BNE     $E625                   
E60F: 8C 44 00        CMPX    #$4400                  
E612: 26 F2           BNE     $E606                   
E614: 4A              DECA                        
E615: 26 B9           BNE     $E5D0                   
E617: 20 30           BRA     $E649                  
; 
E619: 30 1F           LEAX    -1,X                
E61B: 1F 10           TFR     X,D                   
E61D: 84 3F           ANDA    #$3F                  
E61F: 44              LSRA                        
E620: 44              LSRA                        
E621: 44              LSRA                        
E622: 4C              INCA                        
E623: 20 0A           BRA     $E62F                   
E625: 84 F0           ANDA    #$F0                  
E627: 27 04           BEQ     $E62D                   
E629: 86 06           LDA     #$06                  
E62B: 20 02           BRA     $E62F                   
E62D: 86 07           LDA     #$07                  
E62F: 7F 10 08        CLR     $1008                   
E632: CE 00 00        LDU     #$0000                  
E635: C6 20           LDB     #$20                  
E637: E7 C0           STB     ,U+                 
E639: 6F C9 07 FF     CLR     $07FF,U                 
E63D: 7F 80 00        CLR     $8000                   
E640: 11 83 07 FF     CMPU    #$07FF                  
E644: 26 F1           BNE     $E637                   
E646: B7 02 C6        STA     $02C6                   
E649: 8E 10 00        LDX     #$1000                  
E64C: CE 00 00        LDU     #$0000                  
E64F: EF 81           STU     ,X++                
E651: 7F 80 00        CLR     $8000                   
E654: 8C 28 00        CMPX    #$2800                  
E657: 26 F6           BNE     $E64F                   
E659: 8E 40 40        LDX     #$4040                  
E65C: EF 81           STU     ,X++                
E65E: 7F 80 00        CLR     $8000                   
E661: 8C 44 00        CMPX    #$4400                  
E664: 26 F6           BNE     $E65C                   
E666: 10 CE 19 00     LDS     #$1900                  
E66A: C6 00           LDB     #$00                  
E66C: 1F 9B           TFR     B,DP                   
E66E: 7F 10 08        CLR     $1008                   
E671: 4D              TSTA                        
E672: 26 06           BNE     $E67A                   
E674: BD 87 01        JSR     $8701                   
E677: 7F 02 C6        CLR     $02C6                   
E67A: 8E 80 00        LDX     #$8000                  
E67D: 4F              CLRA                        
E67E: AB 80           ADDA    ,X+                 
E680: 7F 80 00        CLR     $8000                   
E683: 8C C0 00        CMPX    #$C000                  
E686: 26 F6           BNE     $E67E                   
E688: 81 73           CMPA    #$73                  
E68A: 26 16           BNE     $E6A2                   
E68C: 8E C0 00        LDX     #$C000                  
E68F: 4F              CLRA                        
E690: AB 80           ADDA    ,X+                 
E692: 7F 80 00        CLR     $8000                   
E695: 8C FF FF        CMPX    #$FFFF                  
E698: 26 F6           BNE     $E690                   
E69A: AB 84           ADDA    ,X                  
E69C: 81 77           CMPA    #$77                  
E69E: 26 06           BNE     $E6A6                   
E6A0: 20 09           BRA     $E6AB                   
E6A2: C6 01           LDB     #$01                  
E6A4: 20 02           BRA     $E6A8                   
E6A6: C6 02           LDB     #$02                  
E6A8: F7 03 06        STB     $0306                   
E6AB: 86 08           LDA     #$08                  
E6AD: B7 10 34        STA     $1034                   
E6B0: 8E 48 00        LDX     #$4800                  
E6B3: A7 84           STA     ,X                  
E6B5: 7F 80 00        CLR     $8000                   
E6B8: E6 80           LDB     ,X+                 
E6BA: C4 0F           ANDB    #$0F                  
E6BC: F1 10 34        CMPB    $1034                   
E6BF: 26 0D           BNE     $E6CE                   
E6C1: 8C 4C 00        CMPX    #$4C00                  
E6C4: 26 ED           BNE     $E6B3                   
E6C6: 4A              DECA                        
E6C7: 26 E4           BNE     $E6AD                   
E6C9: B7 02 86        STA     $0286                   
E6CC: 20 05           BRA     $E6D3                   
E6CE: 86 01           LDA     #$01                  
E6D0: B7 02 86        STA     $0286                   
E6D3: 1C EF           ANDCC   #$EF                  
E6D5: 7F 50 03        CLR     $5003                   
E6D8: 7F 10 00        CLR     $1000                   
E6DB: B6 10 00        LDA     $1000                   
E6DE: 27 FB           BEQ     $E6DB                   
E6E0: B6 80 00        LDA     $8000                   
E6E3: 7F 50 03        CLR     $5003                   
E6E6: 7F 10 00        CLR     $1000                   
E6E9: BD EA 17        JSR     $EA17                   
E6EC: BD EB B9        JSR     $EBB9                   
E6EF: B6 10 00        LDA     $1000                   
E6F2: 27 FB           BEQ     $E6EF                   
E6F4: B6 80 00        LDA     $8000                   
E6F7: 7F 50 03        CLR     $5003                   
E6FA: 7F 10 00        CLR     $1000                   
E6FD: BD EA 17        JSR     $EA17                   
E700: BD EB B9        JSR     $EBB9                   
E703: 8E 48 00        LDX     #$4800                  
E706: CC 00 00        LDD     #$0000                  
E709: ED 81           STD     ,X++                
E70B: 8C 48 20        CMPX    #$4820                  
E70E: 26 F9           BNE     $E709                   
E710: B7 50 09        STA     $5009                   
E713: B7 50 0B        STA     $500B                   
E716: B6 10 00        LDA     $1000                   
E719: 27 FB           BEQ     $E716                   
E71B: B6 80 00        LDA     $8000                   
E71E: 7F 50 03        CLR     $5003                   
E721: 7F 10 00        CLR     $1000                   
E724: BD EA 17        JSR     $EA17                   
E727: BD EB B9        JSR     $EBB9                   
E72A: B6 10 00        LDA     $1000                   
E72D: 27 FB           BEQ     $E72A                   
E72F: B6 80 00        LDA     $8000                   
E732: 7F 50 03        CLR     $5003                   
E735: 7F 10 00        CLR     $1000                   
E738: BD EA 17        JSR     $EA17                   
E73B: BD EB B9        JSR     $EBB9                   
E73E: 86 04           LDA     #$04                  
E740: B7 48 18        STA     $4818                   
E743: B6 10 00        LDA     $1000                   
E746: 27 FB           BEQ     $E743                   
E748: B6 80 00        LDA     $8000                   
E74B: 7F 50 03        CLR     $5003                   
E74E: 7F 10 00        CLR     $1000                   
E751: BD EA 17        JSR     $EA17                   
E754: BD EB B9        JSR     $EBB9                   
E757: B6 10 00        LDA     $1000                   
E75A: 27 FB           BEQ     $E757                   
E75C: B6 80 00        LDA     $8000                   
E75F: 7F 50 03        CLR     $5003                   
E762: 7F 10 00        CLR     $1000                   
E765: BD EA 17        JSR     $EA17                   
E768: BD EB B9        JSR     $EBB9                   
E76B: 8E 48 10        LDX     #$4810                  
E76E: CE EB 3A        LDU     #$EB3A                  
E771: 86 08           LDA     #$08                  
E773: E6 C0           LDB     ,U+                 
E775: E7 82           STB     ,-X                 
E777: 4A              DECA                        
E778: 26 F9           BNE     $E773                   
E77A: B6 10 00        LDA     $1000                   
E77D: 27 FB           BEQ     $E77A                   
E77F: B6 80 00        LDA     $8000                   
E782: 7F 50 03        CLR     $5003                   
E785: 7F 10 00        CLR     $1000                   
E788: BD EA 17        JSR     $EA17                   
E78B: BD EB B9        JSR     $EBB9                   
E78E: B6 10 00        LDA     $1000                   
E791: 27 FB           BEQ     $E78E                   
E793: B6 80 00        LDA     $8000                   
E796: 7F 50 03        CLR     $5003                   
E799: 7F 10 00        CLR     $1000                   
E79C: BD EA 17        JSR     $EA17                   
E79F: BD EB B9        JSR     $EBB9                   
E7A2: B6 03 06        LDA     $0306                   
E7A5: 85 03           BITA    #$03                  
E7A7: 26 37           BNE     $E7E0                   
E7A9: C6 01           LDB     #$01                  
E7AB: F7 40 B0        STB     $40B0                   
E7AE: B6 80 00        LDA     $8000                   
E7B1: F1 40 B0        CMPB    $40B0                   
E7B4: 27 F8           BEQ     $E7AE                   
E7B6: B6 40 B0        LDA     $40B0                   
E7B9: 81 E4           CMPA    #$E4                  
E7BB: 27 0B           BEQ     $E7C8                   
E7BD: CC 00 03        LDD     #$0003                  
E7C0: B7 40 B0        STA     $40B0                   
E7C3: F7 03 06        STB     $0306                   
E7C6: 20 18           BRA     $E7E0                   
E7C8: 7F 03 06        CLR     $0306                   
E7CB: 7F 40 B0        CLR     $40B0                   
E7CE: 86 FF           LDA     #$FF                  
E7D0: B7 10 CE        STA     $10CE                   
E7D3: B6 80 00        LDA     $8000                   
E7D6: 7A 10 CF        DEC     $10CF                   
E7D9: 26 F8           BNE     $E7D3                   
E7DB: 7A 10 CE        DEC     $10CE                   
E7DE: 26 F3           BNE     $E7D3                   
E7E0: B6 03 06        LDA     $0306                   
E7E3: BB 02 C6        ADDA    $02C6                   
E7E6: BB 02 86        ADDA    $0286                   
E7E9: 26 21           BNE     $E80C                   
E7EB: 8E 03 06        LDX     #$0306                  
E7EE: CE EB 4E        LDU     #$EB4E                  
E7F1: 86 06           LDA     #$06                  
E7F3: BD 85 90        JSR     $8590                   
E7F6: 8E 03 04        LDX     #$0304                  
E7F9: CE EB 54        LDU     #$EB54                  
E7FC: 86 06           LDA     #$06                  
E7FE: BD 85 90        JSR     $8590                   
E801: 8E 03 08        LDX     #$0308                  
E804: CE EB 5A        LDU     #$EB5A                  
E807: 86 06           LDA     #$06                  
E809: BD 85 90        JSR     $8590                   
E80C: 7F 10 16        CLR     $1016                   
E80F: 7F 02 14        CLR     $0214                   
E812: 7F 01 F4        CLR     $01F4                   
E815: 86 4F           LDA     #$4F                  
E817: B7 02 10        STA     $0210                   
E81A: B7 02 16        STA     $0216                   
E81D: 8E 02 CD        LDX     #$02CD                  
E820: CE EB 60        LDU     #$EB60                  
E823: 86 0E           LDA     #$0E                  
E825: BD 85 90        JSR     $8590                   
E828: 8E 03 10        LDX     #$0310                  
E82B: CE EB 87        LDU     #$EB87                  
E82E: 86 06           LDA     #$06                  
E830: BD 85 90        JSR     $8590                   
E833: 8E 03 12        LDX     #$0312                  
E836: CE EB 73        LDU     #$EB73                  
E839: 86 06           LDA     #$06                  
E83B: BD 85 90        JSR     $8590                   
E83E: 8E 03 14        LDX     #$0314                  
E841: CE EB 6E        LDU     #$EB6E                  
E844: 86 05           LDA     #$05                  
E846: BD 85 90        JSR     $8590                   
E849: 8E 03 16        LDX     #$0316                  
E84C: CE EB 8D        LDU     #$EB8D                  
E84F: 86 06           LDA     #$06                  
E851: BD 85 90        JSR     $8590                   
E854: 8E 03 18        LDX     #$0318                  
E857: CE EB 93        LDU     #$EB93                  
E85A: 86 0C           LDA     #$0C                  
E85C: BD 85 90        JSR     $8590                   
E85F: B6 10 00        LDA     $1000                   
E862: 27 FB           BEQ     $E85F                   
E864: B6 80 00        LDA     $8000                   
E867: 7F 50 03        CLR     $5003                   
E86A: 7F 10 00        CLR     $1000                   
E86D: BD EA 17        JSR     $EA17                   
E870: BD EB B9        JSR     $EBB9                   
E873: B6 10 1E        LDA     $101E                   
E876: 10 27 00 D7     LBEQ    $E951                   
E87A: B6 10 1A        LDA     $101A                   
E87D: 81 01           CMPA    #$01                  
E87F: 27 4B           BEQ     $E8CC                   
E881: BD EA 80        JSR     $EA80                   
E884: 8E 40 40        LDX     #$4040                  
E887: B6 10 17        LDA     $1017                   
E88A: 81 01           CMPA    #$01                  
E88C: 27 15           BEQ     $E8A3                   
E88E: B6 10 18        LDA     $1018                   
E891: 81 01           CMPA    #$01                  
E893: 27 07           BEQ     $E89C                   
E895: B6 10 19        LDA     $1019                   
E898: 81 01           CMPA    #$01                  
E89A: 26 14           BNE     $E8B0                   
E89C: F6 10 16        LDB     $1016                   
E89F: A7 85           STA     B,X                 
E8A1: 20 0D           BRA     $E8B0                   
E8A3: F6 10 16        LDB     $1016                   
E8A6: 6F 85           CLR     B,X                 
E8A8: 5C              INCB                        
E8A9: C4 1F           ANDB    #$1F                  
E8AB: A7 85           STA     B,X                 
E8AD: F7 10 16        STB     $1016                   
E8B0: B6 10 16        LDA     $1016                   
E8B3: 1F 89           TFR     A,B                   
E8B5: 84 F0           ANDA    #$F0                  
E8B7: 44              LSRA                        
E8B8: 44              LSRA                        
E8B9: 44              LSRA                        
E8BA: 44              LSRA                        
E8BB: B7 02 14        STA     $0214                   
E8BE: C4 0F           ANDB    #$0F                  
E8C0: C1 0A           CMPB    #$0A                  
E8C2: 25 ; ????
E8C3: 02 ; ????
E8C4: CB 37           ADDB    #$37                  
E8C6: F7 01 F4        STB     $01F4                   
E8C9: 7E E8 5F        JMP     $E85F                   
E8CC: BD EB 02        JSR     $EB02                   
E8CF: B6 10 00        LDA     $1000                   
E8D2: 27 FB           BEQ     $E8CF                   
E8D4: B6 80 00        LDA     $8000                   
E8D7: 7F 50 03        CLR     $5003                   
E8DA: 7F 10 00        CLR     $1000                   
E8DD: BD EA 17        JSR     $EA17                   
E8E0: BD EB B9        JSR     $EBB9                   
E8E3: B6 10 1E        LDA     $101E                   
E8E6: 27 69           BEQ     $E951                   
E8E8: B6 10 1A        LDA     $101A                   
E8EB: 81 01           CMPA    #$01                  
E8ED: 27 44           BEQ     $E933                   
E8EF: BD EA 80        JSR     $EA80                   
E8F2: B6 10 08        LDA     $1008                   
E8F5: 81 F8           CMPA    #$F8                  
E8F7: 24 ; ????
E8F8: 12              NOP                         
E8F9: 7C 10 08        INC     $1008                   
E8FC: 7C 10 08        INC     $1008                   
E8FF: 8E 07 FF        LDX     #$07FF                  
E902: 86 20           LDA     #$20                  
E904: C6 80           LDB     #$80                  
E906: BD 85 BD        JSR     $85BD                   
E909: 20 C4           BRA     $E8CF                   
E90B: BD EB 20        JSR     $EB20                   
E90E: 20 BF           BRA     $E8CF                   
E910: B6 10 00        LDA     $1000                   
E913: 27 FB           BEQ     $E910                   
E915: B6 80 00        LDA     $8000                   
E918: 7F 50 03        CLR     $5003                   
E91B: 7F 10 00        CLR     $1000                   
E91E: BD EA 17        JSR     $EA17                   
E921: BD EB B9        JSR     $EBB9                   
E924: B6 10 1E        LDA     $101E                   
E927: 27 28           BEQ     $E951                   
E929: B6 10 1A        LDA     $101A                   
E92C: 81 01           CMPA    #$01                  
E92E: 27 C2           BEQ     $E8F2                   
E930: BD EA 80        JSR     $EA80                   
E933: B6 10 6B        LDA     $106B                   
E936: 2B 27           BMI     $E95F                   
E938: B6 10 08        LDA     $1008                   
E93B: 10 27 FF 20     LBEQ    $E85F                   
E93F: 7A 10 08        DEC     $1008                   
E942: 7A 10 08        DEC     $1008                   
E945: 8E 07 FF        LDX     #$07FF                  
E948: 86 20           LDA     #$20                  
E94A: C6 80           LDB     #$80                  
E94C: BD 85 BD        JSR     $85BD                   
E94F: 20 BF           BRA     $E910                   
E951: 1C FF           ANDCC   #$FF                  
E953: 7F 50 02        CLR     $5002                   
E956: 7F 50 0A        CLR     $500A                   
E959: 7F 50 08        CLR     $5008                   
E95C: 7E 80 72        JMP     $8072                   
E95F: 7C 40 55        INC     $4055                   
E962: 8E 07 FF        LDX     #$07FF                  
E965: 86 20           LDA     #$20                  
E967: C6 80           LDB     #$80                  
E969: BD 85 BD        JSR     $85BD                   
E96C: 8E 00 00        LDX     #$0000                  
E96F: CC 4F 4F        LDD     #$4F4F                  
E972: ED 81           STD     ,X++                
E974: 8C 03 80        CMPX    #$0380                  
E977: 26 F6           BNE     $E96F                   
E979: B6 10 00        LDA     $1000                   
E97C: 27 FB           BEQ     $E979                   
E97E: B6 80 00        LDA     $8000                   
E981: 7F 50 03        CLR     $5003                   
E984: 7F 10 00        CLR     $1000                   
E987: BD EA 17        JSR     $EA17                   
E98A: BD EB B9        JSR     $EBB9                   
E98D: B6 10 08        LDA     $1008                   
E990: 27 05           BEQ     $E997                   
E992: 7A 10 08        DEC     $1008                   
E995: 20 E2           BRA     $E979                   
E997: CC 01 08        LDD     #$0108                  
E99A: B7 40 4A        STA     $404A                   
E99D: F7 10 72        STB     $1072                   
E9A0: 8E EC 23        LDX     #$EC23                  
E9A3: A6 80           LDA     ,X+                 
E9A5: B7 10 73        STA     $1073                   
E9A8: BF 10 76        STX     $1076                   
E9AB: 8E 03 80        LDX     #$0380                  
E9AE: BF 10 74        STX     $1074                   
E9B1: B6 10 00        LDA     $1000                   
E9B4: 27 FB           BEQ     $E9B1                   
E9B6: B6 80 00        LDA     $8000                   
E9B9: 7F 50 03        CLR     $5003                   
E9BC: 7F 10 00        CLR     $1000                   
E9BF: BD EA 17        JSR     $EA17                   
E9C2: BD EB B9        JSR     $EBB9                   
E9C5: CC 01 20        LDD     #$0120                  
E9C8: B7 40 4A        STA     $404A                   
E9CB: FE 10 74        LDU     $1074                   
E9CE: B6 10 73        LDA     $1073                   
E9D1: 48 ; ????
E9D2: 25 ; ????
E9D3: 02 ; ????
E9D4: E7 5F           STB     -1,U                
E9D6: B7 10 73        STA     $1073                   
E9D9: 7A 10 72        DEC     $1072                   
E9DC: 26 10           BNE     $E9EE                   
E9DE: 86 08           LDA     #$08                  
E9E0: B7 10 72        STA     $1072                   
E9E3: BE 10 76        LDX     $1076                   
E9E6: A6 80           LDA     ,X+                 
E9E8: B7 10 73        STA     $1073                   
E9EB: BF 10 76        STX     $1076                   
E9EE: 33 5F           LEAU    -1,U                
E9F0: FF 10 74        STU     $1074                   
E9F3: 11 83 00 00     CMPU    #$0000                  
E9F7: 26 B8           BNE     $E9B1                   
E9F9: B6 10 00        LDA     $1000                   
E9FC: 27 FB           BEQ     $E9F9                   
E9FE: B6 80 00        LDA     $8000                   
EA01: 7F 50 03        CLR     $5003                   
EA04: 7F 10 00        CLR     $1000                   
EA07: BD EA 17        JSR     $EA17                   
EA0A: BD EB B9        JSR     $EBB9                   
EA0D: B6 40 4A        LDA     $404A                   
EA10: 26 E7           BNE     $E9F9                   
EA12: B6 80 00        LDA     $8000                   
EA15: 20 FB           BRA     $EA12                   
EA17: 8E 48 00        LDX     #$4800                  
EA1A: F6 10 17        LDB     $1017                   
EA1D: 58 ; ????
EA1E: A6 05           LDA     5,X                 
EA20: 84 0F           ANDA    #$0F                  
EA22: 26 06           BNE     $EA2A                   
EA24: A6 06           LDA     6,X                 
EA26: 84 0F           ANDA    #$0F                  
EA28: 27 01           BEQ     $EA2B                   
EA2A: 5C              INCB                        
EA2B: C4 03           ANDB    #$03                  
EA2D: F7 10 17        STB     $1017                   
EA30: F6 10 18        LDB     $1018                   
EA33: 58 ; ????
EA34: A6 07           LDA     7,X                 
EA36: 84 03           ANDA    #$03                  
EA38: 26 0E           BNE     $EA48                   
EA3A: A6 88 15        LDA     $15,X                 
EA3D: 84 02           ANDA    #$02                  
EA3F: 26 07           BNE     $EA48                   
EA41: A6 88 17        LDA     $17,X                 
EA44: 84 02           ANDA    #$02                  
EA46: 27 01           BEQ     $EA49                   
EA48: 5C              INCB                        
EA49: C4 03           ANDB    #$03                  
EA4B: F7 10 18        STB     $1018                   
EA4E: F6 10 19        LDB     $1019                   
EA51: 58 ; ????
EA52: A6 07           LDA     7,X                 
EA54: 84 0C           ANDA    #$0C                  
EA56: 26 06           BNE     $EA5E                   
EA58: A6 04           LDA     4,X                 
EA5A: 84 03           ANDA    #$03                  
EA5C: 27 01           BEQ     $EA5F                   
EA5E: 5C              INCB                        
EA5F: C4 03           ANDB    #$03                  
EA61: F7 10 19        STB     $1019                   
EA64: F6 10 1A        LDB     $101A                   
EA67: 58 ; ????
EA68: A6 04           LDA     4,X                 
EA6A: 84 08           ANDA    #$08                  
EA6C: 27 01           BEQ     $EA6F                   
EA6E: 5C              INCB                        
EA6F: F7 10 1A        STB     $101A                   
EA72: A6 88 14        LDA     $14,X                 
EA75: 84 01           ANDA    #$01                  
EA77: AA 88 17        ORA     $17,X                 
EA7A: 84 09           ANDA    #$09                  
EA7C: B7 10 1E        STA     $101E                   
EA7F: 39              RTS                         
EA80: 8E 85 88        LDX     #$8588                  
EA83: CE EB 42        LDU     #$EB42                  
EA86: B6 48 14        LDA     $4814                   
EA89: 84 0C           ANDA    #$0C                  
EA8B: 44              LSRA                        
EA8C: B7 10 34        STA     $1034                   
EA8F: EC 86           LDD     A,X                 
EA91: B7 03 0D        STA     $030D                   
EA94: F7 02 0D        STB     $020D                   
EA97: B6 10 34        LDA     $1034                   
EA9A: EC C6           LDD     A,U                 
EA9C: B7 02 4D        STA     $024D                   
EA9F: F7 01 0D        STB     $010D                   
EAA2: B6 48 14        LDA     $4814                   
EAA5: 84 02           ANDA    #$02                  
EAA7: 8B 03           ADDA    #$03                  
EAA9: B7 02 12        STA     $0212                   
EAAC: B6 48 16        LDA     $4816                   
EAAF: 85 04           BITA    #$04                  
EAB1: 26 05           BNE     $EAB8                   
EAB3: CC 46 46        LDD     #$4646                  
EAB6: 20 03           BRA     $EABB                   
EAB8: CC 4E 20        LDD     #$4E20                  
EABB: B7 01 F0        STA     $01F0                   
EABE: F7 01 D0        STB     $01D0                   
EAC1: 8E EB 4A        LDX     #$EB4A                  
EAC4: B6 48 16        LDA     $4816                   
EAC7: 84 03           ANDA    #$03                  
EAC9: E6 86           LDB     A,X                 
EACB: F7 01 78        STB     $0178                   
EACE: B6 48 16        LDA     $4816                   
EAD1: 85 08           BITA    #$08                  
EAD3: 26 05           BNE     $EADA                   
EAD5: CC 46 46        LDD     #$4646                  
EAD8: 20 03           BRA     $EADD                   
EADA: CC 4E 20        LDD     #$4E20                  
EADD: B7 01 F6        STA     $01F6                   
EAE0: F7 01 D6        STB     $01D6                   
EAE3: B6 48 15        LDA     $4815                   
EAE6: 84 08           ANDA    #$08                  
EAE8: 26 0C           BNE     $EAF6                   
EAEA: 8E 03 0A        LDX     #$030A                  
EAED: CE EB 80        LDU     #$EB80                  
EAF0: 86 07           LDA     #$07                  
EAF2: BD 85 90        JSR     $8590                   
EAF5: 39              RTS                         
EAF6: 8E 03 0A        LDX     #$030A                  
EAF9: CE EB 79        LDU     #$EB79                  
EAFC: 86 07           LDA     #$07                  
EAFE: BD 85 90        JSR     $8590                   
EB01: 39              RTS                         
EB02: 8E 03 E0        LDX     #$03E0                  
EB05: CE F8 F9        LDU     #$F8F9                  
EB08: 10 8E FA FB     LDY     #$FAFB                  
EB0C: 86 10           LDA     #$10                  
EB0E: EF 81           STU     ,X++                
EB10: 10 AF 88 1E     STY     $1E,X                 
EB14: 4A              DECA                        
EB15: 26 F7           BNE     $EB0E                   
EB17: 30 88 20        LEAX    $20,X                 
EB1A: 8C 07 60        CMPX    #$0760                  
EB1D: 25 ; ????
EB1E: ED 39           STD     -7,Y                
EB20: 8E 07 80        LDX     #$0780                  
EB23: CC F8 FA        LDD     #$F8FA                  
EB26: CE F9 FB        LDU     #$F9FB                  
EB29: ED 81           STD     ,X++                
EB2B: ED 88 3E        STD     $3E,X                 
EB2E: EF 88 1E        STU     $1E,X                 
EB31: EF 88 5E        STU     $5E,X                 
EB34: 8C 07 A0        CMPX    #$07A0                  
EB37: 26 F0           BNE     $EB29                   
EB39: 39              RTS                         
EB3A: 0F 0F           CLR     $0F                   
EB3C: 0F 0F           CLR     $0F                   
EB3E: 0F 0F           CLR     $0F                   
EB40: 0F 01           CLR     $01                   
EB42: 20 20           BRA     $EB64                   
EB44: 53              COMB                        
EB45: 20 20           BRA     $EB67                   
EB47: 53              COMB                        
EB48: 53              COMB                        
EB49: 20 41           BRA     $EB8C                   
EB4B: 43              COMA                        
EB4C: 42 ; ????
EB4D: 44              LSRA                        
EB4E: 52 ; ????
EB4F: 41 ; ????
EB50: 4D              TSTA                        
EB51: 20 4F           BRA     $EBA2                   
EB53: 4B ; ????
EB54: 52 ; ????
EB55: 4F              CLRA                        
EB56: 4D              TSTA                        
EB57: 20 4F           BRA     $EBA8                   
EB59: 4B ; ????
EB5A: 49              ROLA                        
EB5B: 5F              CLRB                        
EB5C: 4F              CLRA                        
EB5D: 20 4F           BRA     $EBAE                   
EB5F: 4B ; ????
EB60: 43              COMA                        
EB61: 4F              CLRA                        
EB62: 49              ROLA                        
EB63: 4E ; ????
EB64: 20 20           BRA     $EB86                   
EB66: 20 20           BRA     $EB88                   
EB68: 43              COMA                        
EB69: 52 ; ????
EB6A: 45 ; ????
EB6B: 44              LSRA                        
EB6C: 49              ROLA                        
EB6D: 54              LSRB                        
EB6E: 53              COMB                        
EB6F: 4F              CLRA                        
EB70: 55 ; ????
EB71: 4E ; ????
EB72: 44              LSRA                        
EB73: 44              LSRA                        
EB74: 49              ROLA                        
EB75: 47              ASRA                        
EB76: 44              LSRA                        
EB77: 55 ; ????
EB78: 47              ASRA                        
EB79: 54              LSRB                        
EB7A: 41 ; ????
EB7B: 42 ; ????
EB7C: 4C              INCA                        
EB7D: 45 ; ????
EB7E: 20 20           BRA     $EBA0                   
EB80: 55 ; ????
EB81: 50              NEGB                        
EB82: 52 ; ????
EB83: 49              ROLA                        
EB84: 47              ASRA                        
EB85: 48 ; ????
EB86: 54              LSRB                        
EB87: 53              COMB                        
EB88: 45 ; ????
EB89: 4C              INCA                        
EB8A: 45 ; ????
EB8B: 43              COMA                        
EB8C: 54              LSRB                        
EB8D: 46              RORA                        
EB8E: 52 ; ????
EB8F: 45 ; ????
EB90: 45 ; ????
EB91: 5A              DECB                        
EB92: 45 ; ????
EB93: 45 ; ????
EB94: 58 ; ????
EB95: 54              LSRB                        
EB96: 45 ; ????
EB97: 4E ; ????
EB98: 44              LSRA                        
EB99: 20 20           BRA     $EBBB                   
EB9B: 54              LSRB                        
EB9C: 59              ROLB                        
EB9D: 50              NEGB                        
EB9E: 45 ; ????
EB9F: 45 ; ????
EBA0: 52 ; ????
EBA1: 52 ; ????
EBA2: 4F              CLRA                        
EBA3: 52 ; ????
EBA4: 20 52           BRA     $EBF8                   
EBA6: 41 ; ????
EBA7: 4D              TSTA                        
EBA8: 45 ; ????
EBA9: 52 ; ????
EBAA: 52 ; ????
EBAB: 4F              CLRA                        
EBAC: 52 ; ????
EBAD: 20 52           BRA     $EC01                   
EBAF: 4F              CLRA                        
EBB0: 4D              TSTA                        
EBB1: 45 ; ????
EBB2: 52 ; ????
EBB3: 52 ; ????
EBB4: 4F              CLRA                        
EBB5: 52 ; ????
EBB6: 20 49           BRA     $EC01                   
EBB8: 4F              CLRA                        
EBB9: B6 10 08        LDA     $1008                   
EBBC: 81 F8           CMPA    #$F8                  
EBBE: 26 1C           BNE     $EBDC                   
EBC0: B6 10 16        LDA     $1016                   
EBC3: 81 1B           CMPA    #$1B                  
EBC5: 26 15           BNE     $EBDC                   
EBC7: B6 10 6B        LDA     $106B                   
EBCA: 2A 14           BPL     $EBE0                   
EBCC: B6 10 17        LDA     $1017                   
EBCF: 81 01           CMPA    #$01                  
EBD1: 27 09           BEQ     $EBDC                   
EBD3: B6 10 18        LDA     $1018                   
EBD6: BA 10 19        ORA     $1019                   
EBD9: 26 01           BNE     $EBDC                   
EBDB: 39              RTS                         
EBDC: 7F 10 6B        CLR     $106B                   
EBDF: 39              RTS                         
EBE0: B6 10 18        LDA     $1018                   
EBE3: BA 10 19        ORA     $1019                   
EBE6: BA 10 1A        ORA     $101A                   
EBE9: 26 F1           BNE     $EBDC                   
EBEB: B6 10 17        LDA     $1017                   
EBEE: 81 01           CMPA    #$01                  
EBF0: 27 01           BEQ     $EBF3                   
EBF2: 39              RTS                         
EBF3: B6 48 06        LDA     $4806                   
EBF6: 84 0F           ANDA    #$0F                  
EBF8: 26 E2           BNE     $EBDC                   
EBFA: B6 48 05        LDA     $4805                   
EBFD: 84 0F           ANDA    #$0F                  
EBFF: F6 10 6B        LDB     $106B                   
EC02: 8E EC 16        LDX     #$EC16                  
EC05: A1 85           CMPA    B,X                 
EC07: 26 D3           BNE     $EBDC                   
EC09: 7C 10 6B        INC     $106B                   
EC0C: 5C              INCB                        
EC0D: A6 85           LDA     B,X                 
EC0F: 2B 01           BMI     $EC12                   
EC11: 39              RTS                         
EC12: B7 10 6B        STA     $106B                   
EC15: 39              RTS                         
EC16: 04 04           LSR     $04                   
EC18: 02 ; ????
EC19: 08 ; ????
EC1A: 08 ; ????
EC1B: 04 04           LSR     $04                   
EC1D: 08 ; ????
EC1E: 08 ; ????
EC1F: 08 ; ????
EC20: 01 ; ????
EC21: 01 ; ????
EC22: FF E5 EE        STU     $E5EE                   
EC25: 4B ; ????
EC26: DF 95           STU     $95                   
EC28: 09 4A           ROL     $4A                   
EC2A: 0A 95           DEC     $95                   
EC2C: 69 4A           ROL     10,U                
EC2E: CA 95           ORB     #$95                  
EC30: 29 4A           BVS     $EC7C                   
EC32: 4A              DECA                        
EC33: E5 ; ????
EC34: EE 7B           LDU     -5,S                
EC36: DF 00           STU     $00                   
EC38: 00 00           NEG     $00                   
EC3A: 00 00           NEG     $00                   
EC3C: 00 00           NEG     $00                   
EC3E: 00 1F           NEG     $1F                   
EC40: 00 00           NEG     $00                   
EC42: 00 20           NEG     $20                   
EC44: 80 00           SUBA    #$00                  
EC46: 00 2E           NEG     $2E                   
EC48: 84 F7           ANDA    #$F7                  
EC4A: BC 28 8C        CMPX    $288C                   
EC4D: 94 A0           ANDA    $A0                   
EC4F: 2E 84           BGT     $EBD5                   
EC51: F7 BC 20        STB     $BC20                   
EC54: 84 14           ANDA    #$14                  
EC56: 84 1F           ANDA    #$1F                  
EC58: 0E F7           JMP     $F7                   
EC5A: BC 00 00        CMPX    $0000                   
EC5D: 00 00           NEG     $00                   
EC5F: 00 00           NEG     $00                   
EC61: 00 00           NEG     $00                   
EC63: 44              LSRA                        
EC64: E4 4E           ANDB    14,U                
EC66: 38 ; ????
EC67: 65 ; ????
EC68: 16 D1 44        LBRA    $BDAF                   
EC6B: 55 ; ????
EC6C: F5 50 44        BITB    $5044                   
EC6F: 4D              TSTA                        
EC70: 14 ; ????
EC71: 51 ; ????
EC72: 44              LSRA                        
EC73: 45 ; ????
EC74: 14 ; ????
EC75: 4E ; ????
EC76: 38 ; ????
EC77: 00 00           NEG     $00                   
EC79: 00 00           NEG     $00                   
EC7B: 00 00           NEG     $00                   
EC7D: 00 00           NEG     $00                   
EC7F: 00 10           NEG     $10                   
EC81: 7D E0 00        TST     $E000                   
EC84: 10 ; ????
EC85: 11 ; ????
EC86: 10 ; ????
EC87: 00 10           NEG     $10                   
EC89: 11 ; ????
EC8A: 10 ; ????
EC8B: 00 10           NEG     $10                   
EC8D: 11 ; ????
EC8E: 10 ; ????
EC8F: 00 1F           NEG     $1F                   
EC91: 11 ; ????
EC92: E4 FF FF FF     ANDB    [$FFFF]                 
EC96: FF FF FF        STU     $FFFF                   
EC99: FF FF FF        STU     $FFFF                   
EC9C: FF FF FF        STU     $FFFF                   
EC9F: FF FF FF        STU     $FFFF                   
ECA2: FF FF FF        STU     $FFFF                   
ECA5: FF FF FF        STU     $FFFF                   
ECA8: FF FF FF        STU     $FFFF                   
ECAB: FF FF FF        STU     $FFFF                   
ECAE: FF FF FF        STU     $FFFF                   
ECB1: FF FF FF        STU     $FFFF                   
ECB4: FF FF FF        STU     $FFFF                   
ECB7: FF FF FF        STU     $FFFF                   
ECBA: FF FF FF        STU     $FFFF                   
ECBD: FF FF FF        STU     $FFFF                   
ECC0: FF FF FF        STU     $FFFF                   
ECC3: FF FF FF        STU     $FFFF                   
ECC6: FF FF FF        STU     $FFFF                   
ECC9: FF FF FF        STU     $FFFF                   
ECCC: FF FF FF        STU     $FFFF                   
ECCF: FF FF FF        STU     $FFFF                   
ECD2: FF FF FF        STU     $FFFF                   
ECD5: FF FF FF        STU     $FFFF                   
ECD8: FF FF FF        STU     $FFFF                   
ECDB: FF FF FF        STU     $FFFF                   
ECDE: FF FF FF        STU     $FFFF                   
ECE1: FF FF FF        STU     $FFFF                   
ECE4: FF FF FF        STU     $FFFF                   
ECE7: FF FF FF        STU     $FFFF                   
ECEA: FF FF FF        STU     $FFFF                   
ECED: FF FF FF        STU     $FFFF                   
ECF0: FF FF FF        STU     $FFFF                   
ECF3: FF FF FF        STU     $FFFF                   
ECF6: FF FF FF        STU     $FFFF                   
ECF9: FF FF FF        STU     $FFFF                   
ECFC: FF FF FF        STU     $FFFF                   
ECFF: FF FF FF        STU     $FFFF                   
ED02: FF FF FF        STU     $FFFF                   
ED05: FF FF FF        STU     $FFFF                   
ED08: FF FF FF        STU     $FFFF                   
ED0B: FF FF FF        STU     $FFFF                   
ED0E: FF FF FF        STU     $FFFF                   
ED11: FF FF FF        STU     $FFFF                   
ED14: FF FF FF        STU     $FFFF                   
ED17: FF FF FF        STU     $FFFF                   
ED1A: FF FF FF        STU     $FFFF                   
ED1D: FF FF FF        STU     $FFFF                   
ED20: FF FF FF        STU     $FFFF                   
ED23: FF FF FF        STU     $FFFF                   
ED26: FF FF FF        STU     $FFFF                   
ED29: FF FF FF        STU     $FFFF                   
ED2C: FF FF FF        STU     $FFFF                   
ED2F: FF FF FF        STU     $FFFF                   
ED32: FF FF FF        STU     $FFFF                   
ED35: FF FF FF        STU     $FFFF                   
ED38: FF FF FF        STU     $FFFF                   
ED3B: FF FF FF        STU     $FFFF                   
ED3E: FF FF FF        STU     $FFFF                   
ED41: FF FF FF        STU     $FFFF                   
ED44: FF FF FF        STU     $FFFF                   
ED47: FF FF FF        STU     $FFFF                   
ED4A: FF FF FF        STU     $FFFF                   
ED4D: FF FF FF        STU     $FFFF                   
ED50: FF FF FF        STU     $FFFF                   
ED53: FF FF FF        STU     $FFFF                   
ED56: FF FF FF        STU     $FFFF                   
ED59: FF FF FF        STU     $FFFF                   
ED5C: FF FF FF        STU     $FFFF                   
ED5F: FF FF FF        STU     $FFFF                   
ED62: FF FF FF        STU     $FFFF                   
ED65: FF FF FF        STU     $FFFF                   
ED68: FF FF FF        STU     $FFFF                   
ED6B: FF FF FF        STU     $FFFF                   
ED6E: FF FF FF        STU     $FFFF                   
ED71: FF FF FF        STU     $FFFF                   
ED74: FF FF FF        STU     $FFFF                   
ED77: FF FF FF        STU     $FFFF                   
ED7A: FF FF FF        STU     $FFFF                   
ED7D: FF FF FF        STU     $FFFF                   
ED80: FF FF FF        STU     $FFFF                   
ED83: FF FF FF        STU     $FFFF                   
ED86: FF FF FF        STU     $FFFF                   
ED89: FF FF FF        STU     $FFFF                   
ED8C: FF FF FF        STU     $FFFF                   
ED8F: FF FF FF        STU     $FFFF                   
ED92: FF FF FF        STU     $FFFF                   
ED95: FF FF FF        STU     $FFFF                   
ED98: FF FF FF        STU     $FFFF                   
ED9B: FF FF FF        STU     $FFFF                   
ED9E: FF FF FF        STU     $FFFF                   
EDA1: FF FF FF        STU     $FFFF                   
EDA4: FF FF FF        STU     $FFFF                   
EDA7: FF FF FF        STU     $FFFF                   
EDAA: FF FF FF        STU     $FFFF                   
EDAD: FF FF FF        STU     $FFFF                   
EDB0: FF FF FF        STU     $FFFF                   
EDB3: FF FF FF        STU     $FFFF                   
EDB6: FF FF FF        STU     $FFFF                   
EDB9: FF FF FF        STU     $FFFF                   
EDBC: FF FF FF        STU     $FFFF                   
EDBF: FF FF FF        STU     $FFFF                   
EDC2: FF FF FF        STU     $FFFF                   
EDC5: FF FF FF        STU     $FFFF                   
EDC8: FF FF FF        STU     $FFFF                   
EDCB: FF FF FF        STU     $FFFF                   
EDCE: FF FF FF        STU     $FFFF                   
EDD1: FF FF FF        STU     $FFFF                   
EDD4: FF FF FF        STU     $FFFF                   
EDD7: FF FF FF        STU     $FFFF                   
EDDA: FF FF FF        STU     $FFFF                   
EDDD: FF FF FF        STU     $FFFF                   
EDE0: FF FF FF        STU     $FFFF                   
EDE3: FF FF FF        STU     $FFFF                   
EDE6: FF FF FF        STU     $FFFF                   
EDE9: FF FF FF        STU     $FFFF                   
EDEC: FF FF FF        STU     $FFFF                   
EDEF: FF FF FF        STU     $FFFF                   
EDF2: FF FF FF        STU     $FFFF                   
EDF5: FF FF FF        STU     $FFFF                   
EDF8: FF FF FF        STU     $FFFF                   
EDFB: FF FF FF        STU     $FFFF                   
EDFE: FF FF FF        STU     $FFFF                   
EE01: FF FF FF        STU     $FFFF                   
EE04: FF FF FF        STU     $FFFF                   
EE07: FF FF FF        STU     $FFFF                   
EE0A: FF FF FF        STU     $FFFF                   
EE0D: FF FF FF        STU     $FFFF                   
EE10: FF FF FF        STU     $FFFF                   
EE13: FF FF FF        STU     $FFFF                   
EE16: FF FF FF        STU     $FFFF                   
EE19: FF FF FF        STU     $FFFF                   
EE1C: FF FF FF        STU     $FFFF                   
EE1F: FF FF FF        STU     $FFFF                   
EE22: FF FF FF        STU     $FFFF                   
EE25: FF FF FF        STU     $FFFF                   
EE28: FF FF FF        STU     $FFFF                   
EE2B: FF FF FF        STU     $FFFF                   
EE2E: FF FF FF        STU     $FFFF                   
EE31: FF FF FF        STU     $FFFF                   
EE34: FF FF FF        STU     $FFFF                   
EE37: FF FF FF        STU     $FFFF                   
EE3A: FF FF FF        STU     $FFFF                   
EE3D: FF FF FF        STU     $FFFF                   
EE40: FF FF FF        STU     $FFFF                   
EE43: FF FF FF        STU     $FFFF                   
EE46: FF FF FF        STU     $FFFF                   
EE49: FF FF FF        STU     $FFFF                   
EE4C: FF FF FF        STU     $FFFF                   
EE4F: FF FF FF        STU     $FFFF                   
EE52: FF FF FF        STU     $FFFF                   
EE55: FF FF FF        STU     $FFFF                   
EE58: FF FF FF        STU     $FFFF                   
EE5B: FF FF FF        STU     $FFFF                   
EE5E: FF FF FF        STU     $FFFF                   
EE61: FF FF FF        STU     $FFFF                   
EE64: FF FF FF        STU     $FFFF                   
EE67: FF FF FF        STU     $FFFF                   
EE6A: FF FF FF        STU     $FFFF                   
EE6D: FF FF FF        STU     $FFFF                   
EE70: FF FF FF        STU     $FFFF                   
EE73: FF FF FF        STU     $FFFF                   
EE76: FF FF FF        STU     $FFFF                   
EE79: FF FF FF        STU     $FFFF                   
EE7C: FF FF FF        STU     $FFFF                   
EE7F: FF FF FF        STU     $FFFF                   
EE82: FF FF FF        STU     $FFFF                   
EE85: FF FF FF        STU     $FFFF                   
EE88: FF FF FF        STU     $FFFF                   
EE8B: FF FF FF        STU     $FFFF                   
EE8E: FF FF FF        STU     $FFFF                   
EE91: FF FF FF        STU     $FFFF                   
EE94: FF FF FF        STU     $FFFF                   
EE97: FF FF FF        STU     $FFFF                   
EE9A: FF FF FF        STU     $FFFF                   
EE9D: FF FF FF        STU     $FFFF                   
EEA0: FF FF FF        STU     $FFFF                   
EEA3: FF FF FF        STU     $FFFF                   
EEA6: FF FF FF        STU     $FFFF                   
EEA9: FF FF FF        STU     $FFFF                   
EEAC: FF FF FF        STU     $FFFF                   
EEAF: FF FF FF        STU     $FFFF                   
EEB2: FF FF FF        STU     $FFFF                   
EEB5: FF FF FF        STU     $FFFF                   
EEB8: FF FF FF        STU     $FFFF                   
EEBB: FF FF FF        STU     $FFFF                   
EEBE: FF FF FF        STU     $FFFF                   
EEC1: FF FF FF        STU     $FFFF                   
EEC4: FF FF FF        STU     $FFFF                   
EEC7: FF FF FF        STU     $FFFF                   
EECA: FF FF FF        STU     $FFFF                   
EECD: FF FF FF        STU     $FFFF                   
EED0: FF FF FF        STU     $FFFF                   
EED3: FF FF FF        STU     $FFFF                   
EED6: FF FF FF        STU     $FFFF                   
EED9: FF FF FF        STU     $FFFF                   
EEDC: FF FF FF        STU     $FFFF                   
EEDF: FF FF FF        STU     $FFFF                   
EEE2: FF FF FF        STU     $FFFF                   
EEE5: FF FF FF        STU     $FFFF                   
EEE8: FF FF FF        STU     $FFFF                   
EEEB: FF FF FF        STU     $FFFF                   
EEEE: FF FF FF        STU     $FFFF                   
EEF1: FF FF FF        STU     $FFFF                   
EEF4: FF FF FF        STU     $FFFF                   
EEF7: FF FF FF        STU     $FFFF                   
EEFA: FF FF FF        STU     $FFFF                   
EEFD: FF FF FF        STU     $FFFF                   
EF00: FF FF FF        STU     $FFFF                   
EF03: FF FF FF        STU     $FFFF                   
EF06: FF FF FF        STU     $FFFF                   
EF09: FF FF FF        STU     $FFFF                   
EF0C: FF FF FF        STU     $FFFF                   
EF0F: FF FF FF        STU     $FFFF                   
EF12: FF FF FF        STU     $FFFF                   
EF15: FF FF FF        STU     $FFFF                   
EF18: FF FF FF        STU     $FFFF                   
EF1B: FF FF FF        STU     $FFFF                   
EF1E: FF FF FF        STU     $FFFF                   
EF21: FF FF FF        STU     $FFFF                   
EF24: FF FF FF        STU     $FFFF                   
EF27: FF FF FF        STU     $FFFF                   
EF2A: FF FF FF        STU     $FFFF                   
EF2D: FF FF FF        STU     $FFFF                   
EF30: FF FF FF        STU     $FFFF                   
EF33: FF FF FF        STU     $FFFF                   
EF36: FF FF FF        STU     $FFFF                   
EF39: FF FF FF        STU     $FFFF                   
EF3C: FF FF FF        STU     $FFFF                   
EF3F: FF FF FF        STU     $FFFF                   
EF42: FF FF FF        STU     $FFFF                   
EF45: FF FF FF        STU     $FFFF                   
EF48: FF FF FF        STU     $FFFF                   
EF4B: FF FF FF        STU     $FFFF                   
EF4E: FF FF FF        STU     $FFFF                   
EF51: FF FF FF        STU     $FFFF                   
EF54: FF FF FF        STU     $FFFF                   
EF57: FF FF FF        STU     $FFFF                   
EF5A: FF FF FF        STU     $FFFF                   
EF5D: FF FF FF        STU     $FFFF                   
EF60: FF FF FF        STU     $FFFF                   
EF63: FF FF FF        STU     $FFFF                   
EF66: FF FF FF        STU     $FFFF                   
EF69: FF FF FF        STU     $FFFF                   
EF6C: FF FF FF        STU     $FFFF                   
EF6F: FF FF FF        STU     $FFFF                   
EF72: FF FF FF        STU     $FFFF                   
EF75: FF FF FF        STU     $FFFF                   
EF78: FF FF FF        STU     $FFFF                   
EF7B: FF FF FF        STU     $FFFF                   
EF7E: FF FF FF        STU     $FFFF                   
EF81: FF FF FF        STU     $FFFF                   
EF84: FF FF FF        STU     $FFFF                   
EF87: FF FF FF        STU     $FFFF                   
EF8A: FF FF FF        STU     $FFFF                   
EF8D: FF FF FF        STU     $FFFF                   
EF90: FF FF FF        STU     $FFFF                   
EF93: FF FF FF        STU     $FFFF                   
EF96: FF FF FF        STU     $FFFF                   
EF99: FF FF FF        STU     $FFFF                   
EF9C: FF FF FF        STU     $FFFF                   
EF9F: FF FF FF        STU     $FFFF                   
EFA2: FF FF FF        STU     $FFFF                   
EFA5: FF FF FF        STU     $FFFF                   
EFA8: FF FF FF        STU     $FFFF                   
EFAB: FF FF FF        STU     $FFFF                   
EFAE: FF FF FF        STU     $FFFF                   
EFB1: FF FF FF        STU     $FFFF                   
EFB4: FF FF FF        STU     $FFFF                   
EFB7: FF FF FF        STU     $FFFF                   
EFBA: FF FF FF        STU     $FFFF                   
EFBD: FF FF FF        STU     $FFFF                   
EFC0: FF FF FF        STU     $FFFF                   
EFC3: FF FF FF        STU     $FFFF                   
EFC6: FF FF FF        STU     $FFFF                   
EFC9: FF FF FF        STU     $FFFF                   
EFCC: FF FF FF        STU     $FFFF                   
EFCF: FF FF FF        STU     $FFFF                   
EFD2: FF FF FF        STU     $FFFF                   
EFD5: FF FF FF        STU     $FFFF                   
EFD8: FF FF FF        STU     $FFFF                   
EFDB: FF FF FF        STU     $FFFF                   
EFDE: FF FF FF        STU     $FFFF                   
EFE1: FF FF FF        STU     $FFFF                   
EFE4: FF FF FF        STU     $FFFF                   
EFE7: FF FF FF        STU     $FFFF                   
EFEA: FF FF FF        STU     $FFFF                   
EFED: FF FF FF        STU     $FFFF                   
EFF0: FF FF FF        STU     $FFFF                   
EFF3: FF FF FF        STU     $FFFF                   
EFF6: FF FF FF        STU     $FFFF                   
EFF9: FF FF FF        STU     $FFFF                   
EFFC: FF FF FF        STU     $FFFF                   
EFFF: FF FF FF        STU     $FFFF                   
F002: FF FF FF        STU     $FFFF                   
F005: FF FF FF        STU     $FFFF                   
F008: FF FF FF        STU     $FFFF                   
F00B: FF FF FF        STU     $FFFF                   
F00E: FF FF FF        STU     $FFFF                   
F011: FF FF FF        STU     $FFFF                   
F014: FF FF FF        STU     $FFFF                   
F017: FF FF FF        STU     $FFFF                   
F01A: FF FF FF        STU     $FFFF                   
F01D: FF FF FF        STU     $FFFF                   
F020: FF FF FF        STU     $FFFF                   
F023: FF FF FF        STU     $FFFF                   
F026: FF FF FF        STU     $FFFF                   
F029: FF FF FF        STU     $FFFF                   
F02C: FF FF FF        STU     $FFFF                   
F02F: FF FF FF        STU     $FFFF                   
F032: FF FF FF        STU     $FFFF                   
F035: FF FF FF        STU     $FFFF                   
F038: FF FF FF        STU     $FFFF                   
F03B: FF FF FF        STU     $FFFF                   
F03E: FF FF FF        STU     $FFFF                   
F041: FF FF FF        STU     $FFFF                   
F044: FF FF FF        STU     $FFFF                   
F047: FF FF FF        STU     $FFFF                   
F04A: FF FF FF        STU     $FFFF                   
F04D: FF FF FF        STU     $FFFF                   
F050: FF FF FF        STU     $FFFF                   
F053: FF FF FF        STU     $FFFF                   
F056: FF FF FF        STU     $FFFF                   
F059: FF FF FF        STU     $FFFF                   
F05C: FF FF FF        STU     $FFFF                   
F05F: FF FF FF        STU     $FFFF                   
F062: FF FF FF        STU     $FFFF                   
F065: FF FF FF        STU     $FFFF                   
F068: FF FF FF        STU     $FFFF                   
F06B: FF FF FF        STU     $FFFF                   
F06E: FF FF FF        STU     $FFFF                   
F071: FF FF FF        STU     $FFFF                   
F074: FF FF FF        STU     $FFFF                   
F077: FF FF FF        STU     $FFFF                   
F07A: FF FF FF        STU     $FFFF                   
F07D: FF FF FF        STU     $FFFF                   
F080: FF FF FF        STU     $FFFF                   
F083: FF FF FF        STU     $FFFF                   
F086: FF FF FF        STU     $FFFF                   
F089: FF FF FF        STU     $FFFF                   
F08C: FF FF FF        STU     $FFFF                   
F08F: FF FF FF        STU     $FFFF                   
F092: FF FF FF        STU     $FFFF                   
F095: FF FF FF        STU     $FFFF                   
F098: FF FF FF        STU     $FFFF                   
F09B: FF FF FF        STU     $FFFF                   
F09E: FF FF FF        STU     $FFFF                   
F0A1: FF FF FF        STU     $FFFF                   
F0A4: FF FF FF        STU     $FFFF                   
F0A7: FF FF FF        STU     $FFFF                   
F0AA: FF FF FF        STU     $FFFF                   
F0AD: FF FF FF        STU     $FFFF                   
F0B0: FF FF FF        STU     $FFFF                   
F0B3: FF FF FF        STU     $FFFF                   
F0B6: FF FF FF        STU     $FFFF                   
F0B9: FF FF FF        STU     $FFFF                   
F0BC: FF FF FF        STU     $FFFF                   
F0BF: FF FF FF        STU     $FFFF                   
F0C2: FF FF FF        STU     $FFFF                   
F0C5: FF FF FF        STU     $FFFF                   
F0C8: FF FF FF        STU     $FFFF                   
F0CB: FF FF FF        STU     $FFFF                   
F0CE: FF FF FF        STU     $FFFF                   
F0D1: FF FF FF        STU     $FFFF                   
F0D4: FF FF FF        STU     $FFFF                   
F0D7: FF FF FF        STU     $FFFF                   
F0DA: FF FF FF        STU     $FFFF                   
F0DD: FF FF FF        STU     $FFFF                   
F0E0: FF FF FF        STU     $FFFF                   
F0E3: FF FF FF        STU     $FFFF                   
F0E6: FF FF FF        STU     $FFFF                   
F0E9: FF FF FF        STU     $FFFF                   
F0EC: FF FF FF        STU     $FFFF                   
F0EF: FF FF FF        STU     $FFFF                   
F0F2: FF FF FF        STU     $FFFF                   
F0F5: FF FF FF        STU     $FFFF                   
F0F8: FF FF FF        STU     $FFFF                   
F0FB: FF FF FF        STU     $FFFF                   
F0FE: FF FF FF        STU     $FFFF                   
F101: FF FF FF        STU     $FFFF                   
F104: FF FF FF        STU     $FFFF                   
F107: FF FF FF        STU     $FFFF                   
F10A: FF FF FF        STU     $FFFF                   
F10D: FF FF FF        STU     $FFFF                   
F110: FF FF FF        STU     $FFFF                   
F113: FF FF FF        STU     $FFFF                   
F116: FF FF FF        STU     $FFFF                   
F119: FF FF FF        STU     $FFFF                   
F11C: FF FF FF        STU     $FFFF                   
F11F: FF FF FF        STU     $FFFF                   
F122: FF FF FF        STU     $FFFF                   
F125: FF FF FF        STU     $FFFF                   
F128: FF FF FF        STU     $FFFF                   
F12B: FF FF FF        STU     $FFFF                   
F12E: FF FF FF        STU     $FFFF                   
F131: FF FF FF        STU     $FFFF                   
F134: FF FF FF        STU     $FFFF                   
F137: FF FF FF        STU     $FFFF                   
F13A: FF FF FF        STU     $FFFF                   
F13D: FF FF FF        STU     $FFFF                   
F140: FF FF FF        STU     $FFFF                   
F143: FF FF FF        STU     $FFFF                   
F146: FF FF FF        STU     $FFFF                   
F149: FF FF FF        STU     $FFFF                   
F14C: FF FF FF        STU     $FFFF                   
F14F: FF FF FF        STU     $FFFF                   
F152: FF FF FF        STU     $FFFF                   
F155: FF FF FF        STU     $FFFF                   
F158: FF FF FF        STU     $FFFF                   
F15B: FF FF FF        STU     $FFFF                   
F15E: FF FF FF        STU     $FFFF                   
F161: FF FF FF        STU     $FFFF                   
F164: FF FF FF        STU     $FFFF                   
F167: FF FF FF        STU     $FFFF                   
F16A: FF FF FF        STU     $FFFF                   
F16D: FF FF FF        STU     $FFFF                   
F170: FF FF FF        STU     $FFFF                   
F173: FF FF FF        STU     $FFFF                   
F176: FF FF FF        STU     $FFFF                   
F179: FF FF FF        STU     $FFFF                   
F17C: FF FF FF        STU     $FFFF                   
F17F: FF FF FF        STU     $FFFF                   
F182: FF FF FF        STU     $FFFF                   
F185: FF FF FF        STU     $FFFF                   
F188: FF FF FF        STU     $FFFF                   
F18B: FF FF FF        STU     $FFFF                   
F18E: FF FF FF        STU     $FFFF                   
F191: FF FF FF        STU     $FFFF                   
F194: FF FF FF        STU     $FFFF                   
F197: FF FF FF        STU     $FFFF                   
F19A: FF FF FF        STU     $FFFF                   
F19D: FF FF FF        STU     $FFFF                   
F1A0: FF FF FF        STU     $FFFF                   
F1A3: FF FF FF        STU     $FFFF                   
F1A6: FF FF FF        STU     $FFFF                   
F1A9: FF FF FF        STU     $FFFF                   
F1AC: FF FF FF        STU     $FFFF                   
F1AF: FF FF FF        STU     $FFFF                   
F1B2: FF FF FF        STU     $FFFF                   
F1B5: FF FF FF        STU     $FFFF                   
F1B8: FF FF FF        STU     $FFFF                   
F1BB: FF FF FF        STU     $FFFF                   
F1BE: FF FF FF        STU     $FFFF                   
F1C1: FF FF FF        STU     $FFFF                   
F1C4: FF FF FF        STU     $FFFF                   
F1C7: FF FF FF        STU     $FFFF                   
F1CA: FF FF FF        STU     $FFFF                   
F1CD: FF FF FF        STU     $FFFF                   
F1D0: FF FF FF        STU     $FFFF                   
F1D3: FF FF FF        STU     $FFFF                   
F1D6: FF FF FF        STU     $FFFF                   
F1D9: FF FF FF        STU     $FFFF                   
F1DC: FF FF FF        STU     $FFFF                   
F1DF: FF FF FF        STU     $FFFF                   
F1E2: FF FF FF        STU     $FFFF                   
F1E5: FF FF FF        STU     $FFFF                   
F1E8: FF FF FF        STU     $FFFF                   
F1EB: FF FF FF        STU     $FFFF                   
F1EE: FF FF FF        STU     $FFFF                   
F1F1: FF FF FF        STU     $FFFF                   
F1F4: FF FF FF        STU     $FFFF                   
F1F7: FF FF FF        STU     $FFFF                   
F1FA: FF FF FF        STU     $FFFF                   
F1FD: FF FF FF        STU     $FFFF                   
F200: FF FF FF        STU     $FFFF                   
F203: FF FF FF        STU     $FFFF                   
F206: FF FF FF        STU     $FFFF                   
F209: FF FF FF        STU     $FFFF                   
F20C: FF FF FF        STU     $FFFF                   
F20F: FF FF FF        STU     $FFFF                   
F212: FF FF FF        STU     $FFFF                   
F215: FF FF FF        STU     $FFFF                   
F218: FF FF FF        STU     $FFFF                   
F21B: FF FF FF        STU     $FFFF                   
F21E: FF FF FF        STU     $FFFF                   
F221: FF FF FF        STU     $FFFF                   
F224: FF FF FF        STU     $FFFF                   
F227: FF FF FF        STU     $FFFF                   
F22A: FF FF FF        STU     $FFFF                   
F22D: FF FF FF        STU     $FFFF                   
F230: FF FF FF        STU     $FFFF                   
F233: FF FF FF        STU     $FFFF                   
F236: FF FF FF        STU     $FFFF                   
F239: FF FF FF        STU     $FFFF                   
F23C: FF FF FF        STU     $FFFF                   
F23F: FF FF FF        STU     $FFFF                   
F242: FF FF FF        STU     $FFFF                   
F245: FF FF FF        STU     $FFFF                   
F248: FF FF FF        STU     $FFFF                   
F24B: FF FF FF        STU     $FFFF                   
F24E: FF FF FF        STU     $FFFF                   
F251: FF FF FF        STU     $FFFF                   
F254: FF FF FF        STU     $FFFF                   
F257: FF FF FF        STU     $FFFF                   
F25A: FF FF FF        STU     $FFFF                   
F25D: FF FF FF        STU     $FFFF                   
F260: FF FF FF        STU     $FFFF                   
F263: FF FF FF        STU     $FFFF                   
F266: FF FF FF        STU     $FFFF                   
F269: FF FF FF        STU     $FFFF                   
F26C: FF FF FF        STU     $FFFF                   
F26F: FF FF FF        STU     $FFFF                   
F272: FF FF FF        STU     $FFFF                   
F275: FF FF FF        STU     $FFFF                   
F278: FF FF FF        STU     $FFFF                   
F27B: FF FF FF        STU     $FFFF                   
F27E: FF FF FF        STU     $FFFF                   
F281: FF FF FF        STU     $FFFF                   
F284: FF FF FF        STU     $FFFF                   
F287: FF FF FF        STU     $FFFF                   
F28A: FF FF FF        STU     $FFFF                   
F28D: FF FF FF        STU     $FFFF                   
F290: FF FF FF        STU     $FFFF                   
F293: FF FF FF        STU     $FFFF                   
F296: FF FF FF        STU     $FFFF                   
F299: FF FF FF        STU     $FFFF                   
F29C: FF FF FF        STU     $FFFF                   
F29F: FF FF FF        STU     $FFFF                   
F2A2: FF FF FF        STU     $FFFF                   
F2A5: FF FF FF        STU     $FFFF                   
F2A8: FF FF FF        STU     $FFFF                   
F2AB: FF FF FF        STU     $FFFF                   
F2AE: FF FF FF        STU     $FFFF                   
F2B1: FF FF FF        STU     $FFFF                   
F2B4: FF FF FF        STU     $FFFF                   
F2B7: FF FF FF        STU     $FFFF                   
F2BA: FF FF FF        STU     $FFFF                   
F2BD: FF FF FF        STU     $FFFF                   
F2C0: FF FF FF        STU     $FFFF                   
F2C3: FF FF FF        STU     $FFFF                   
F2C6: FF FF FF        STU     $FFFF                   
F2C9: FF FF FF        STU     $FFFF                   
F2CC: FF FF FF        STU     $FFFF                   
F2CF: FF FF FF        STU     $FFFF                   
F2D2: FF FF FF        STU     $FFFF                   
F2D5: FF FF FF        STU     $FFFF                   
F2D8: FF FF FF        STU     $FFFF                   
F2DB: FF FF FF        STU     $FFFF                   
F2DE: FF FF FF        STU     $FFFF                   
F2E1: FF FF FF        STU     $FFFF                   
F2E4: FF FF FF        STU     $FFFF                   
F2E7: FF FF FF        STU     $FFFF                   
F2EA: FF FF FF        STU     $FFFF                   
F2ED: FF FF FF        STU     $FFFF                   
F2F0: FF FF FF        STU     $FFFF                   
F2F3: FF FF FF        STU     $FFFF                   
F2F6: FF FF FF        STU     $FFFF                   
F2F9: FF FF FF        STU     $FFFF                   
F2FC: FF FF FF        STU     $FFFF                   
F2FF: FF FF FF        STU     $FFFF                   
F302: FF FF FF        STU     $FFFF                   
F305: FF FF FF        STU     $FFFF                   
F308: FF FF FF        STU     $FFFF                   
F30B: FF FF FF        STU     $FFFF                   
F30E: FF FF FF        STU     $FFFF                   
F311: FF FF FF        STU     $FFFF                   
F314: FF FF FF        STU     $FFFF                   
F317: FF FF FF        STU     $FFFF                   
F31A: FF FF FF        STU     $FFFF                   
F31D: FF FF FF        STU     $FFFF                   
F320: FF FF FF        STU     $FFFF                   
F323: FF FF FF        STU     $FFFF                   
F326: FF FF FF        STU     $FFFF                   
F329: FF FF FF        STU     $FFFF                   
F32C: FF FF FF        STU     $FFFF                   
F32F: FF FF FF        STU     $FFFF                   
F332: FF FF FF        STU     $FFFF                   
F335: FF FF FF        STU     $FFFF                   
F338: FF FF FF        STU     $FFFF                   
F33B: FF FF FF        STU     $FFFF                   
F33E: FF FF FF        STU     $FFFF                   
F341: FF FF FF        STU     $FFFF                   
F344: FF FF FF        STU     $FFFF                   
F347: FF FF FF        STU     $FFFF                   
F34A: FF FF FF        STU     $FFFF                   
F34D: FF FF FF        STU     $FFFF                   
F350: FF FF FF        STU     $FFFF                   
F353: FF FF FF        STU     $FFFF                   
F356: FF FF FF        STU     $FFFF                   
F359: FF FF FF        STU     $FFFF                   
F35C: FF FF FF        STU     $FFFF                   
F35F: FF FF FF        STU     $FFFF                   
F362: FF FF FF        STU     $FFFF                   
F365: FF FF FF        STU     $FFFF                   
F368: FF FF FF        STU     $FFFF                   
F36B: FF FF FF        STU     $FFFF                   
F36E: FF FF FF        STU     $FFFF                   
F371: FF FF FF        STU     $FFFF                   
F374: FF FF FF        STU     $FFFF                   
F377: FF FF FF        STU     $FFFF                   
F37A: FF FF FF        STU     $FFFF                   
F37D: FF FF FF        STU     $FFFF                   
F380: FF FF FF        STU     $FFFF                   
F383: FF FF FF        STU     $FFFF                   
F386: FF FF FF        STU     $FFFF                   
F389: FF FF FF        STU     $FFFF                   
F38C: FF FF FF        STU     $FFFF                   
F38F: FF FF FF        STU     $FFFF                   
F392: FF FF FF        STU     $FFFF                   
F395: FF FF FF        STU     $FFFF                   
F398: FF FF FF        STU     $FFFF                   
F39B: FF FF FF        STU     $FFFF                   
F39E: FF FF FF        STU     $FFFF                   
F3A1: FF FF FF        STU     $FFFF                   
F3A4: FF FF FF        STU     $FFFF                   
F3A7: FF FF FF        STU     $FFFF                   
F3AA: FF FF FF        STU     $FFFF                   
F3AD: FF FF FF        STU     $FFFF                   
F3B0: FF FF FF        STU     $FFFF                   
F3B3: FF FF FF        STU     $FFFF                   
F3B6: FF FF FF        STU     $FFFF                   
F3B9: FF FF FF        STU     $FFFF                   
F3BC: FF FF FF        STU     $FFFF                   
F3BF: FF FF FF        STU     $FFFF                   
F3C2: FF FF FF        STU     $FFFF                   
F3C5: FF FF FF        STU     $FFFF                   
F3C8: FF FF FF        STU     $FFFF                   
F3CB: FF FF FF        STU     $FFFF                   
F3CE: FF FF FF        STU     $FFFF                   
F3D1: FF FF FF        STU     $FFFF                   
F3D4: FF FF FF        STU     $FFFF                   
F3D7: FF FF FF        STU     $FFFF                   
F3DA: FF FF FF        STU     $FFFF                   
F3DD: FF FF FF        STU     $FFFF                   
F3E0: FF FF FF        STU     $FFFF                   
F3E3: FF FF FF        STU     $FFFF                   
F3E6: FF FF FF        STU     $FFFF                   
F3E9: FF FF FF        STU     $FFFF                   
F3EC: FF FF FF        STU     $FFFF                   
F3EF: FF FF FF        STU     $FFFF                   
F3F2: FF FF FF        STU     $FFFF                   
F3F5: FF FF FF        STU     $FFFF                   
F3F8: FF FF FF        STU     $FFFF                   
F3FB: FF FF FF        STU     $FFFF                   
F3FE: FF FF FF        STU     $FFFF                   
F401: FF FF FF        STU     $FFFF                   
F404: FF FF FF        STU     $FFFF                   
F407: FF FF FF        STU     $FFFF                   
F40A: FF FF FF        STU     $FFFF                   
F40D: FF FF FF        STU     $FFFF                   
F410: FF FF FF        STU     $FFFF                   
F413: FF FF FF        STU     $FFFF                   
F416: FF FF FF        STU     $FFFF                   
F419: FF FF FF        STU     $FFFF                   
F41C: FF FF FF        STU     $FFFF                   
F41F: FF FF FF        STU     $FFFF                   
F422: FF FF FF        STU     $FFFF                   
F425: FF FF FF        STU     $FFFF                   
F428: FF FF FF        STU     $FFFF                   
F42B: FF FF FF        STU     $FFFF                   
F42E: FF FF FF        STU     $FFFF                   
F431: FF FF FF        STU     $FFFF                   
F434: FF FF FF        STU     $FFFF                   
F437: FF FF FF        STU     $FFFF                   
F43A: FF FF FF        STU     $FFFF                   
F43D: FF FF FF        STU     $FFFF                   
F440: FF FF FF        STU     $FFFF                   
F443: FF FF FF        STU     $FFFF                   
F446: FF FF FF        STU     $FFFF                   
F449: FF FF FF        STU     $FFFF                   
F44C: FF FF FF        STU     $FFFF                   
F44F: FF FF FF        STU     $FFFF                   
F452: FF FF FF        STU     $FFFF                   
F455: FF FF FF        STU     $FFFF                   
F458: FF FF FF        STU     $FFFF                   
F45B: FF FF FF        STU     $FFFF                   
F45E: FF FF FF        STU     $FFFF                   
F461: FF FF FF        STU     $FFFF                   
F464: FF FF FF        STU     $FFFF                   
F467: FF FF FF        STU     $FFFF                   
F46A: FF FF FF        STU     $FFFF                   
F46D: FF FF FF        STU     $FFFF                   
F470: FF FF FF        STU     $FFFF                   
F473: FF FF FF        STU     $FFFF                   
F476: FF FF FF        STU     $FFFF                   
F479: FF FF FF        STU     $FFFF                   
F47C: FF FF FF        STU     $FFFF                   
F47F: FF FF FF        STU     $FFFF                   
F482: FF FF FF        STU     $FFFF                   
F485: FF FF FF        STU     $FFFF                   
F488: FF FF FF        STU     $FFFF                   
F48B: FF FF FF        STU     $FFFF                   
F48E: FF FF FF        STU     $FFFF                   
F491: FF FF FF        STU     $FFFF                   
F494: FF FF FF        STU     $FFFF                   
F497: FF FF FF        STU     $FFFF                   
F49A: FF FF FF        STU     $FFFF                   
F49D: FF FF FF        STU     $FFFF                   
F4A0: FF FF FF        STU     $FFFF                   
F4A3: FF FF FF        STU     $FFFF                   
F4A6: FF FF FF        STU     $FFFF                   
F4A9: FF FF FF        STU     $FFFF                   
F4AC: FF FF FF        STU     $FFFF                   
F4AF: FF FF FF        STU     $FFFF                   
F4B2: FF FF FF        STU     $FFFF                   
F4B5: FF FF FF        STU     $FFFF                   
F4B8: FF FF FF        STU     $FFFF                   
F4BB: FF FF FF        STU     $FFFF                   
F4BE: FF FF FF        STU     $FFFF                   
F4C1: FF FF FF        STU     $FFFF                   
F4C4: FF FF FF        STU     $FFFF                   
F4C7: FF FF FF        STU     $FFFF                   
F4CA: FF FF FF        STU     $FFFF                   
F4CD: FF FF FF        STU     $FFFF                   
F4D0: FF FF FF        STU     $FFFF                   
F4D3: FF FF FF        STU     $FFFF                   
F4D6: FF FF FF        STU     $FFFF                   
F4D9: FF FF FF        STU     $FFFF                   
F4DC: FF FF FF        STU     $FFFF                   
F4DF: FF FF FF        STU     $FFFF                   
F4E2: FF FF FF        STU     $FFFF                   
F4E5: FF FF FF        STU     $FFFF                   
F4E8: FF FF FF        STU     $FFFF                   
F4EB: FF FF FF        STU     $FFFF                   
F4EE: FF FF FF        STU     $FFFF                   
F4F1: FF FF FF        STU     $FFFF                   
F4F4: FF FF FF        STU     $FFFF                   
F4F7: FF FF FF        STU     $FFFF                   
F4FA: FF FF FF        STU     $FFFF                   
F4FD: FF FF FF        STU     $FFFF                   
F500: FF FF FF        STU     $FFFF                   
F503: FF FF FF        STU     $FFFF                   
F506: FF FF FF        STU     $FFFF                   
F509: FF FF FF        STU     $FFFF                   
F50C: FF FF FF        STU     $FFFF                   
F50F: FF FF FF        STU     $FFFF                   
F512: FF FF FF        STU     $FFFF                   
F515: FF FF FF        STU     $FFFF                   
F518: FF FF FF        STU     $FFFF                   
F51B: FF FF FF        STU     $FFFF                   
F51E: FF FF FF        STU     $FFFF                   
F521: FF FF FF        STU     $FFFF                   
F524: FF FF FF        STU     $FFFF                   
F527: FF FF FF        STU     $FFFF                   
F52A: FF FF FF        STU     $FFFF                   
F52D: FF FF FF        STU     $FFFF                   
F530: FF FF FF        STU     $FFFF                   
F533: FF FF FF        STU     $FFFF                   
F536: FF FF FF        STU     $FFFF                   
F539: FF FF FF        STU     $FFFF                   
F53C: FF FF FF        STU     $FFFF                   
F53F: FF FF FF        STU     $FFFF                   
F542: FF FF FF        STU     $FFFF                   
F545: FF FF FF        STU     $FFFF                   
F548: FF FF FF        STU     $FFFF                   
F54B: FF FF FF        STU     $FFFF                   
F54E: FF FF FF        STU     $FFFF                   
F551: FF FF FF        STU     $FFFF                   
F554: FF FF FF        STU     $FFFF                   
F557: FF FF FF        STU     $FFFF                   
F55A: FF FF FF        STU     $FFFF                   
F55D: FF FF FF        STU     $FFFF                   
F560: FF FF FF        STU     $FFFF                   
F563: FF FF FF        STU     $FFFF                   
F566: FF FF FF        STU     $FFFF                   
F569: FF FF FF        STU     $FFFF                   
F56C: FF FF FF        STU     $FFFF                   
F56F: FF FF FF        STU     $FFFF                   
F572: FF FF FF        STU     $FFFF                   
F575: FF FF FF        STU     $FFFF                   
F578: FF FF FF        STU     $FFFF                   
F57B: FF FF FF        STU     $FFFF                   
F57E: FF FF FF        STU     $FFFF                   
F581: FF FF FF        STU     $FFFF                   
F584: FF FF FF        STU     $FFFF                   
F587: FF FF FF        STU     $FFFF                   
F58A: FF FF FF        STU     $FFFF                   
F58D: FF FF FF        STU     $FFFF                   
F590: FF FF FF        STU     $FFFF                   
F593: FF FF FF        STU     $FFFF                   
F596: FF FF FF        STU     $FFFF                   
F599: FF FF FF        STU     $FFFF                   
F59C: FF FF FF        STU     $FFFF                   
F59F: FF FF FF        STU     $FFFF                   
F5A2: FF FF FF        STU     $FFFF                   
F5A5: FF FF FF        STU     $FFFF                   
F5A8: FF FF FF        STU     $FFFF                   
F5AB: FF FF FF        STU     $FFFF                   
F5AE: FF FF FF        STU     $FFFF                   
F5B1: FF FF FF        STU     $FFFF                   
F5B4: FF FF FF        STU     $FFFF                   
F5B7: FF FF FF        STU     $FFFF                   
F5BA: FF FF FF        STU     $FFFF                   
F5BD: FF FF FF        STU     $FFFF                   
F5C0: FF FF FF        STU     $FFFF                   
F5C3: FF FF FF        STU     $FFFF                   
F5C6: FF FF FF        STU     $FFFF                   
F5C9: FF FF FF        STU     $FFFF                   
F5CC: FF FF FF        STU     $FFFF                   
F5CF: FF FF FF        STU     $FFFF                   
F5D2: FF FF FF        STU     $FFFF                   
F5D5: FF FF FF        STU     $FFFF                   
F5D8: FF FF FF        STU     $FFFF                   
F5DB: FF FF FF        STU     $FFFF                   
F5DE: FF FF FF        STU     $FFFF                   
F5E1: FF FF FF        STU     $FFFF                   
F5E4: FF FF FF        STU     $FFFF                   
F5E7: FF FF FF        STU     $FFFF                   
F5EA: FF FF FF        STU     $FFFF                   
F5ED: FF FF FF        STU     $FFFF                   
F5F0: FF FF FF        STU     $FFFF                   
F5F3: FF FF FF        STU     $FFFF                   
F5F6: FF FF FF        STU     $FFFF                   
F5F9: FF FF FF        STU     $FFFF                   
F5FC: FF FF FF        STU     $FFFF                   
F5FF: FF FF FF        STU     $FFFF                   
F602: FF FF FF        STU     $FFFF                   
F605: FF FF FF        STU     $FFFF                   
F608: FF FF FF        STU     $FFFF                   
F60B: FF FF FF        STU     $FFFF                   
F60E: FF FF FF        STU     $FFFF                   
F611: FF FF FF        STU     $FFFF                   
F614: FF FF FF        STU     $FFFF                   
F617: FF FF FF        STU     $FFFF                   
F61A: FF FF FF        STU     $FFFF                   
F61D: FF FF FF        STU     $FFFF                   
F620: FF FF FF        STU     $FFFF                   
F623: FF FF FF        STU     $FFFF                   
F626: FF FF FF        STU     $FFFF                   
F629: FF FF FF        STU     $FFFF                   
F62C: FF FF FF        STU     $FFFF                   
F62F: FF FF FF        STU     $FFFF                   
F632: FF FF FF        STU     $FFFF                   
F635: FF FF FF        STU     $FFFF                   
F638: FF FF FF        STU     $FFFF                   
F63B: FF FF FF        STU     $FFFF                   
F63E: FF FF FF        STU     $FFFF                   
F641: FF FF FF        STU     $FFFF                   
F644: FF FF FF        STU     $FFFF                   
F647: FF FF FF        STU     $FFFF                   
F64A: FF FF FF        STU     $FFFF                   
F64D: FF FF FF        STU     $FFFF                   
F650: FF FF FF        STU     $FFFF                   
F653: FF FF FF        STU     $FFFF                   
F656: FF FF FF        STU     $FFFF                   
F659: FF FF FF        STU     $FFFF                   
F65C: FF FF FF        STU     $FFFF                   
F65F: FF FF FF        STU     $FFFF                   
F662: FF FF FF        STU     $FFFF                   
F665: FF FF FF        STU     $FFFF                   
F668: FF FF FF        STU     $FFFF                   
F66B: FF FF FF        STU     $FFFF                   
F66E: FF FF FF        STU     $FFFF                   
F671: FF FF FF        STU     $FFFF                   
F674: FF FF FF        STU     $FFFF                   
F677: FF FF FF        STU     $FFFF                   
F67A: FF FF FF        STU     $FFFF                   
F67D: FF FF FF        STU     $FFFF                   
F680: FF FF FF        STU     $FFFF                   
F683: FF FF FF        STU     $FFFF                   
F686: FF FF FF        STU     $FFFF                   
F689: FF FF FF        STU     $FFFF                   
F68C: FF FF FF        STU     $FFFF                   
F68F: FF FF FF        STU     $FFFF                   
F692: FF FF FF        STU     $FFFF                   
F695: FF FF FF        STU     $FFFF                   
F698: FF FF FF        STU     $FFFF                   
F69B: FF FF FF        STU     $FFFF                   
F69E: FF FF FF        STU     $FFFF                   
F6A1: FF FF FF        STU     $FFFF                   
F6A4: FF FF FF        STU     $FFFF                   
F6A7: FF FF FF        STU     $FFFF                   
F6AA: FF FF FF        STU     $FFFF                   
F6AD: FF FF FF        STU     $FFFF                   
F6B0: FF FF FF        STU     $FFFF                   
F6B3: FF FF FF        STU     $FFFF                   
F6B6: FF FF FF        STU     $FFFF                   
F6B9: FF FF FF        STU     $FFFF                   
F6BC: FF FF FF        STU     $FFFF                   
F6BF: FF FF FF        STU     $FFFF                   
F6C2: FF FF FF        STU     $FFFF                   
F6C5: FF FF FF        STU     $FFFF                   
F6C8: FF FF FF        STU     $FFFF                   
F6CB: FF FF FF        STU     $FFFF                   
F6CE: FF FF FF        STU     $FFFF                   
F6D1: FF FF FF        STU     $FFFF                   
F6D4: FF FF FF        STU     $FFFF                   
F6D7: FF FF FF        STU     $FFFF                   
F6DA: FF FF FF        STU     $FFFF                   
F6DD: FF FF FF        STU     $FFFF                   
F6E0: FF FF FF        STU     $FFFF                   
F6E3: FF FF FF        STU     $FFFF                   
F6E6: FF FF FF        STU     $FFFF                   
F6E9: FF FF FF        STU     $FFFF                   
F6EC: FF FF FF        STU     $FFFF                   
F6EF: FF FF FF        STU     $FFFF                   
F6F2: FF FF FF        STU     $FFFF                   
F6F5: FF FF FF        STU     $FFFF                   
F6F8: FF FF FF        STU     $FFFF                   
F6FB: FF FF FF        STU     $FFFF                   
F6FE: FF FF FF        STU     $FFFF                   
F701: FF FF FF        STU     $FFFF                   
F704: FF FF FF        STU     $FFFF                   
F707: FF FF FF        STU     $FFFF                   
F70A: FF FF FF        STU     $FFFF                   
F70D: FF FF FF        STU     $FFFF                   
F710: FF FF FF        STU     $FFFF                   
F713: FF FF FF        STU     $FFFF                   
F716: FF FF FF        STU     $FFFF                   
F719: FF FF FF        STU     $FFFF                   
F71C: FF FF FF        STU     $FFFF                   
F71F: FF FF FF        STU     $FFFF                   
F722: FF FF FF        STU     $FFFF                   
F725: FF FF FF        STU     $FFFF                   
F728: FF FF FF        STU     $FFFF                   
F72B: FF FF FF        STU     $FFFF                   
F72E: FF FF FF        STU     $FFFF                   
F731: FF FF FF        STU     $FFFF                   
F734: FF FF FF        STU     $FFFF                   
F737: FF FF FF        STU     $FFFF                   
F73A: FF FF FF        STU     $FFFF                   
F73D: FF FF FF        STU     $FFFF                   
F740: FF FF FF        STU     $FFFF                   
F743: FF FF FF        STU     $FFFF                   
F746: FF FF FF        STU     $FFFF                   
F749: FF FF FF        STU     $FFFF                   
F74C: FF FF FF        STU     $FFFF                   
F74F: FF FF FF        STU     $FFFF                   
F752: FF FF FF        STU     $FFFF                   
F755: FF FF FF        STU     $FFFF                   
F758: FF FF FF        STU     $FFFF                   
F75B: FF FF FF        STU     $FFFF                   
F75E: FF FF FF        STU     $FFFF                   
F761: FF FF FF        STU     $FFFF                   
F764: FF FF FF        STU     $FFFF                   
F767: FF FF FF        STU     $FFFF                   
F76A: FF FF FF        STU     $FFFF                   
F76D: FF FF FF        STU     $FFFF                   
F770: FF FF FF        STU     $FFFF                   
F773: FF FF FF        STU     $FFFF                   
F776: FF FF FF        STU     $FFFF                   
F779: FF FF FF        STU     $FFFF                   
F77C: FF FF FF        STU     $FFFF                   
F77F: FF FF FF        STU     $FFFF                   
F782: FF FF FF        STU     $FFFF                   
F785: FF FF FF        STU     $FFFF                   
F788: FF FF FF        STU     $FFFF                   
F78B: FF FF FF        STU     $FFFF                   
F78E: FF FF FF        STU     $FFFF                   
F791: FF FF FF        STU     $FFFF                   
F794: FF FF FF        STU     $FFFF                   
F797: FF FF FF        STU     $FFFF                   
F79A: FF FF FF        STU     $FFFF                   
F79D: FF FF FF        STU     $FFFF                   
F7A0: FF FF FF        STU     $FFFF                   
F7A3: FF FF FF        STU     $FFFF                   
F7A6: FF FF FF        STU     $FFFF                   
F7A9: FF FF FF        STU     $FFFF                   
F7AC: FF FF FF        STU     $FFFF                   
F7AF: FF FF FF        STU     $FFFF                   
F7B2: FF FF FF        STU     $FFFF                   
F7B5: FF FF FF        STU     $FFFF                   
F7B8: FF FF FF        STU     $FFFF                   
F7BB: FF FF FF        STU     $FFFF                   
F7BE: FF FF FF        STU     $FFFF                   
F7C1: FF FF FF        STU     $FFFF                   
F7C4: FF FF FF        STU     $FFFF                   
F7C7: FF FF FF        STU     $FFFF                   
F7CA: FF FF FF        STU     $FFFF                   
F7CD: FF FF FF        STU     $FFFF                   
F7D0: FF FF FF        STU     $FFFF                   
F7D3: FF FF FF        STU     $FFFF                   
F7D6: FF FF FF        STU     $FFFF                   
F7D9: FF FF FF        STU     $FFFF                   
F7DC: FF FF FF        STU     $FFFF                   
F7DF: FF FF FF        STU     $FFFF                   
F7E2: FF FF FF        STU     $FFFF                   
F7E5: FF FF FF        STU     $FFFF                   
F7E8: FF FF FF        STU     $FFFF                   
F7EB: FF FF FF        STU     $FFFF                   
F7EE: FF FF FF        STU     $FFFF                   
F7F1: FF FF FF        STU     $FFFF                   
F7F4: FF FF FF        STU     $FFFF                   
F7F7: FF FF FF        STU     $FFFF                   
F7FA: FF FF FF        STU     $FFFF                   
F7FD: FF FF FF        STU     $FFFF                   
F800: FF FF FF        STU     $FFFF                   
F803: FF FF FF        STU     $FFFF                   
F806: FF FF FF        STU     $FFFF                   
F809: FF FF FF        STU     $FFFF                   
F80C: FF FF FF        STU     $FFFF                   
F80F: FF FF FF        STU     $FFFF                   
F812: FF FF FF        STU     $FFFF                   
F815: FF FF FF        STU     $FFFF                   
F818: FF FF FF        STU     $FFFF                   
F81B: FF FF FF        STU     $FFFF                   
F81E: FF FF FF        STU     $FFFF                   
F821: FF FF FF        STU     $FFFF                   
F824: FF FF FF        STU     $FFFF                   
F827: FF FF FF        STU     $FFFF                   
F82A: FF FF FF        STU     $FFFF                   
F82D: FF FF FF        STU     $FFFF                   
F830: FF FF FF        STU     $FFFF                   
F833: FF FF FF        STU     $FFFF                   
F836: FF FF FF        STU     $FFFF                   
F839: FF FF FF        STU     $FFFF                   
F83C: FF FF FF        STU     $FFFF                   
F83F: FF FF FF        STU     $FFFF                   
F842: FF FF FF        STU     $FFFF                   
F845: FF FF FF        STU     $FFFF                   
F848: FF FF FF        STU     $FFFF                   
F84B: FF FF FF        STU     $FFFF                   
F84E: FF FF FF        STU     $FFFF                   
F851: FF FF FF        STU     $FFFF                   
F854: FF FF FF        STU     $FFFF                   
F857: FF FF FF        STU     $FFFF                   
F85A: FF FF FF        STU     $FFFF                   
F85D: FF FF FF        STU     $FFFF                   
F860: FF FF FF        STU     $FFFF                   
F863: FF FF FF        STU     $FFFF                   
F866: FF FF FF        STU     $FFFF                   
F869: FF FF FF        STU     $FFFF                   
F86C: FF FF FF        STU     $FFFF                   
F86F: FF FF FF        STU     $FFFF                   
F872: FF FF FF        STU     $FFFF                   
F875: FF FF FF        STU     $FFFF                   
F878: FF FF FF        STU     $FFFF                   
F87B: FF FF FF        STU     $FFFF                   
F87E: FF FF FF        STU     $FFFF                   
F881: FF FF FF        STU     $FFFF                   
F884: FF FF FF        STU     $FFFF                   
F887: FF FF FF        STU     $FFFF                   
F88A: FF FF FF        STU     $FFFF                   
F88D: FF FF FF        STU     $FFFF                   
F890: FF FF FF        STU     $FFFF                   
F893: FF FF FF        STU     $FFFF                   
F896: FF FF FF        STU     $FFFF                   
F899: FF FF FF        STU     $FFFF                   
F89C: FF FF FF        STU     $FFFF                   
F89F: FF FF FF        STU     $FFFF                   
F8A2: FF FF FF        STU     $FFFF                   
F8A5: FF FF FF        STU     $FFFF                   
F8A8: FF FF FF        STU     $FFFF                   
F8AB: FF FF FF        STU     $FFFF                   
F8AE: FF FF FF        STU     $FFFF                   
F8B1: FF FF FF        STU     $FFFF                   
F8B4: FF FF FF        STU     $FFFF                   
F8B7: FF FF FF        STU     $FFFF                   
F8BA: FF FF FF        STU     $FFFF                   
F8BD: FF FF FF        STU     $FFFF                   
F8C0: FF FF FF        STU     $FFFF                   
F8C3: FF FF FF        STU     $FFFF                   
F8C6: FF FF FF        STU     $FFFF                   
F8C9: FF FF FF        STU     $FFFF                   
F8CC: FF FF FF        STU     $FFFF                   
F8CF: FF FF FF        STU     $FFFF                   
F8D2: FF FF FF        STU     $FFFF                   
F8D5: FF FF FF        STU     $FFFF                   
F8D8: FF FF FF        STU     $FFFF                   
F8DB: FF FF FF        STU     $FFFF                   
F8DE: FF FF FF        STU     $FFFF                   
F8E1: FF FF FF        STU     $FFFF                   
F8E4: FF FF FF        STU     $FFFF                   
F8E7: FF FF FF        STU     $FFFF                   
F8EA: FF FF FF        STU     $FFFF                   
F8ED: FF FF FF        STU     $FFFF                   
F8F0: FF FF FF        STU     $FFFF                   
F8F3: FF FF FF        STU     $FFFF                   
F8F6: FF FF FF        STU     $FFFF                   
F8F9: FF FF FF        STU     $FFFF                   
F8FC: FF FF FF        STU     $FFFF                   
F8FF: FF FF FF        STU     $FFFF                   
F902: FF FF FF        STU     $FFFF                   
F905: FF FF FF        STU     $FFFF                   
F908: FF FF FF        STU     $FFFF                   
F90B: FF FF FF        STU     $FFFF                   
F90E: FF FF FF        STU     $FFFF                   
F911: FF FF FF        STU     $FFFF                   
F914: FF FF FF        STU     $FFFF                   
F917: FF FF FF        STU     $FFFF                   
F91A: FF FF FF        STU     $FFFF                   
F91D: FF FF FF        STU     $FFFF                   
F920: FF FF FF        STU     $FFFF                   
F923: FF FF FF        STU     $FFFF                   
F926: FF FF FF        STU     $FFFF                   
F929: FF FF FF        STU     $FFFF                   
F92C: FF FF FF        STU     $FFFF                   
F92F: FF FF FF        STU     $FFFF                   
F932: FF FF FF        STU     $FFFF                   
F935: FF FF FF        STU     $FFFF                   
F938: FF FF FF        STU     $FFFF                   
F93B: FF FF FF        STU     $FFFF                   
F93E: FF FF FF        STU     $FFFF                   
F941: FF FF FF        STU     $FFFF                   
F944: FF FF FF        STU     $FFFF                   
F947: FF FF FF        STU     $FFFF                   
F94A: FF FF FF        STU     $FFFF                   
F94D: FF FF FF        STU     $FFFF                   
F950: FF FF FF        STU     $FFFF                   
F953: FF FF FF        STU     $FFFF                   
F956: FF FF FF        STU     $FFFF                   
F959: FF FF FF        STU     $FFFF                   
F95C: FF FF FF        STU     $FFFF                   
F95F: FF FF FF        STU     $FFFF                   
F962: FF FF FF        STU     $FFFF                   
F965: FF FF FF        STU     $FFFF                   
F968: FF FF FF        STU     $FFFF                   
F96B: FF FF FF        STU     $FFFF                   
F96E: FF FF FF        STU     $FFFF                   
F971: FF FF FF        STU     $FFFF                   
F974: FF FF FF        STU     $FFFF                   
F977: FF FF FF        STU     $FFFF                   
F97A: FF FF FF        STU     $FFFF                   
F97D: FF FF FF        STU     $FFFF                   
F980: FF FF FF        STU     $FFFF                   
F983: FF FF FF        STU     $FFFF                   
F986: FF FF FF        STU     $FFFF                   
F989: FF FF FF        STU     $FFFF                   
F98C: FF FF FF        STU     $FFFF                   
F98F: FF FF FF        STU     $FFFF                   
F992: FF FF FF        STU     $FFFF                   
F995: FF FF FF        STU     $FFFF                   
F998: FF FF FF        STU     $FFFF                   
F99B: FF FF FF        STU     $FFFF                   
F99E: FF FF FF        STU     $FFFF                   
F9A1: FF FF FF        STU     $FFFF                   
F9A4: FF FF FF        STU     $FFFF                   
F9A7: FF FF FF        STU     $FFFF                   
F9AA: FF FF FF        STU     $FFFF                   
F9AD: FF FF FF        STU     $FFFF                   
F9B0: FF FF FF        STU     $FFFF                   
F9B3: FF FF FF        STU     $FFFF                   
F9B6: FF FF FF        STU     $FFFF                   
F9B9: FF FF FF        STU     $FFFF                   
F9BC: FF FF FF        STU     $FFFF                   
F9BF: FF FF FF        STU     $FFFF                   
F9C2: FF FF FF        STU     $FFFF                   
F9C5: FF FF FF        STU     $FFFF                   
F9C8: FF FF FF        STU     $FFFF                   
F9CB: FF FF FF        STU     $FFFF                   
F9CE: FF FF FF        STU     $FFFF                   
F9D1: FF FF FF        STU     $FFFF                   
F9D4: FF FF FF        STU     $FFFF                   
F9D7: FF FF FF        STU     $FFFF                   
F9DA: FF FF FF        STU     $FFFF                   
F9DD: FF FF FF        STU     $FFFF                   
F9E0: FF FF FF        STU     $FFFF                   
F9E3: FF FF FF        STU     $FFFF                   
F9E6: FF FF FF        STU     $FFFF                   
F9E9: FF FF FF        STU     $FFFF                   
F9EC: FF FF FF        STU     $FFFF                   
F9EF: FF FF FF        STU     $FFFF                   
F9F2: FF FF FF        STU     $FFFF                   
F9F5: FF FF FF        STU     $FFFF                   
F9F8: FF FF FF        STU     $FFFF                   
F9FB: FF FF FF        STU     $FFFF                   
F9FE: FF FF FF        STU     $FFFF                   
FA01: FF FF FF        STU     $FFFF                   
FA04: FF FF FF        STU     $FFFF                   
FA07: FF FF FF        STU     $FFFF                   
FA0A: FF FF FF        STU     $FFFF                   
FA0D: FF FF FF        STU     $FFFF                   
FA10: FF FF FF        STU     $FFFF                   
FA13: FF FF FF        STU     $FFFF                   
FA16: FF FF FF        STU     $FFFF                   
FA19: FF FF FF        STU     $FFFF                   
FA1C: FF FF FF        STU     $FFFF                   
FA1F: FF FF FF        STU     $FFFF                   
FA22: FF FF FF        STU     $FFFF                   
FA25: FF FF FF        STU     $FFFF                   
FA28: FF FF FF        STU     $FFFF                   
FA2B: FF FF FF        STU     $FFFF                   
FA2E: FF FF FF        STU     $FFFF                   
FA31: FF FF FF        STU     $FFFF                   
FA34: FF FF FF        STU     $FFFF                   
FA37: FF FF FF        STU     $FFFF                   
FA3A: FF FF FF        STU     $FFFF                   
FA3D: FF FF FF        STU     $FFFF                   
FA40: FF FF FF        STU     $FFFF                   
FA43: FF FF FF        STU     $FFFF                   
FA46: FF FF FF        STU     $FFFF                   
FA49: FF FF FF        STU     $FFFF                   
FA4C: FF FF FF        STU     $FFFF                   
FA4F: FF FF FF        STU     $FFFF                   
FA52: FF FF FF        STU     $FFFF                   
FA55: FF FF FF        STU     $FFFF                   
FA58: FF FF FF        STU     $FFFF                   
FA5B: FF FF FF        STU     $FFFF                   
FA5E: FF FF FF        STU     $FFFF                   
FA61: FF FF FF        STU     $FFFF                   
FA64: FF FF FF        STU     $FFFF                   
FA67: FF FF FF        STU     $FFFF                   
FA6A: FF FF FF        STU     $FFFF                   
FA6D: FF FF FF        STU     $FFFF                   
FA70: FF FF FF        STU     $FFFF                   
FA73: FF FF FF        STU     $FFFF                   
FA76: FF FF FF        STU     $FFFF                   
FA79: FF FF FF        STU     $FFFF                   
FA7C: FF FF FF        STU     $FFFF                   
FA7F: FF FF FF        STU     $FFFF                   
FA82: FF FF FF        STU     $FFFF                   
FA85: FF FF FF        STU     $FFFF                   
FA88: FF FF FF        STU     $FFFF                   
FA8B: FF FF FF        STU     $FFFF                   
FA8E: FF FF FF        STU     $FFFF                   
FA91: FF FF FF        STU     $FFFF                   
FA94: FF FF FF        STU     $FFFF                   
FA97: FF FF FF        STU     $FFFF                   
FA9A: FF FF FF        STU     $FFFF                   
FA9D: FF FF FF        STU     $FFFF                   
FAA0: FF FF FF        STU     $FFFF                   
FAA3: FF FF FF        STU     $FFFF                   
FAA6: FF FF FF        STU     $FFFF                   
FAA9: FF FF FF        STU     $FFFF                   
FAAC: FF FF FF        STU     $FFFF                   
FAAF: FF FF FF        STU     $FFFF                   
FAB2: FF FF FF        STU     $FFFF                   
FAB5: FF FF FF        STU     $FFFF                   
FAB8: FF FF FF        STU     $FFFF                   
FABB: FF FF FF        STU     $FFFF                   
FABE: FF FF FF        STU     $FFFF                   
FAC1: FF FF FF        STU     $FFFF                   
FAC4: FF FF FF        STU     $FFFF                   
FAC7: FF FF FF        STU     $FFFF                   
FACA: FF FF FF        STU     $FFFF                   
FACD: FF FF FF        STU     $FFFF                   
FAD0: FF FF FF        STU     $FFFF                   
FAD3: FF FF FF        STU     $FFFF                   
FAD6: FF FF FF        STU     $FFFF                   
FAD9: FF FF FF        STU     $FFFF                   
FADC: FF FF FF        STU     $FFFF                   
FADF: FF FF FF        STU     $FFFF                   
FAE2: FF FF FF        STU     $FFFF                   
FAE5: FF FF FF        STU     $FFFF                   
FAE8: FF FF FF        STU     $FFFF                   
FAEB: FF FF FF        STU     $FFFF                   
FAEE: FF FF FF        STU     $FFFF                   
FAF1: FF FF FF        STU     $FFFF                   
FAF4: FF FF FF        STU     $FFFF                   
FAF7: FF FF FF        STU     $FFFF                   
FAFA: FF FF FF        STU     $FFFF                   
FAFD: FF FF FF        STU     $FFFF                   
FB00: FF FF FF        STU     $FFFF                   
FB03: FF FF FF        STU     $FFFF                   
FB06: FF FF FF        STU     $FFFF                   
FB09: FF FF FF        STU     $FFFF                   
FB0C: FF FF FF        STU     $FFFF                   
FB0F: FF FF FF        STU     $FFFF                   
FB12: FF FF FF        STU     $FFFF                   
FB15: FF FF FF        STU     $FFFF                   
FB18: FF FF FF        STU     $FFFF                   
FB1B: FF FF FF        STU     $FFFF                   
FB1E: FF FF FF        STU     $FFFF                   
FB21: FF FF FF        STU     $FFFF                   
FB24: FF FF FF        STU     $FFFF                   
FB27: FF FF FF        STU     $FFFF                   
FB2A: FF FF FF        STU     $FFFF                   
FB2D: FF FF FF        STU     $FFFF                   
FB30: FF FF FF        STU     $FFFF                   
FB33: FF FF FF        STU     $FFFF                   
FB36: FF FF FF        STU     $FFFF                   
FB39: FF FF FF        STU     $FFFF                   
FB3C: FF FF FF        STU     $FFFF                   
FB3F: FF FF FF        STU     $FFFF                   
FB42: FF FF FF        STU     $FFFF                   
FB45: FF FF FF        STU     $FFFF                   
FB48: FF FF FF        STU     $FFFF                   
FB4B: FF FF FF        STU     $FFFF                   
FB4E: FF FF FF        STU     $FFFF                   
FB51: FF FF FF        STU     $FFFF                   
FB54: FF FF FF        STU     $FFFF                   
FB57: FF FF FF        STU     $FFFF                   
FB5A: FF FF FF        STU     $FFFF                   
FB5D: FF FF FF        STU     $FFFF                   
FB60: FF FF FF        STU     $FFFF                   
FB63: FF FF FF        STU     $FFFF                   
FB66: FF FF FF        STU     $FFFF                   
FB69: FF FF FF        STU     $FFFF                   
FB6C: FF FF FF        STU     $FFFF                   
FB6F: FF FF FF        STU     $FFFF                   
FB72: FF FF FF        STU     $FFFF                   
FB75: FF FF FF        STU     $FFFF                   
FB78: FF FF FF        STU     $FFFF                   
FB7B: FF FF FF        STU     $FFFF                   
FB7E: FF FF FF        STU     $FFFF                   
FB81: FF FF FF        STU     $FFFF                   
FB84: FF FF FF        STU     $FFFF                   
FB87: FF FF FF        STU     $FFFF                   
FB8A: FF FF FF        STU     $FFFF                   
FB8D: FF FF FF        STU     $FFFF                   
FB90: FF FF FF        STU     $FFFF                   
FB93: FF FF FF        STU     $FFFF                   
FB96: FF FF FF        STU     $FFFF                   
FB99: FF FF FF        STU     $FFFF                   
FB9C: FF FF FF        STU     $FFFF                   
FB9F: FF FF FF        STU     $FFFF                   
FBA2: FF FF FF        STU     $FFFF                   
FBA5: FF FF FF        STU     $FFFF                   
FBA8: FF FF FF        STU     $FFFF                   
FBAB: FF FF FF        STU     $FFFF                   
FBAE: FF FF FF        STU     $FFFF                   
FBB1: FF FF FF        STU     $FFFF                   
FBB4: FF FF FF        STU     $FFFF                   
FBB7: FF FF FF        STU     $FFFF                   
FBBA: FF FF FF        STU     $FFFF                   
FBBD: FF FF FF        STU     $FFFF                   
FBC0: FF FF FF        STU     $FFFF                   
FBC3: FF FF FF        STU     $FFFF                   
FBC6: FF FF FF        STU     $FFFF                   
FBC9: FF FF FF        STU     $FFFF                   
FBCC: FF FF FF        STU     $FFFF                   
FBCF: FF FF FF        STU     $FFFF                   
FBD2: FF FF FF        STU     $FFFF                   
FBD5: FF FF FF        STU     $FFFF                   
FBD8: FF FF FF        STU     $FFFF                   
FBDB: FF FF FF        STU     $FFFF                   
FBDE: FF FF FF        STU     $FFFF                   
FBE1: FF FF FF        STU     $FFFF                   
FBE4: FF FF FF        STU     $FFFF                   
FBE7: FF FF FF        STU     $FFFF                   
FBEA: FF FF FF        STU     $FFFF                   
FBED: FF FF FF        STU     $FFFF                   
FBF0: FF FF FF        STU     $FFFF                   
FBF3: FF FF FF        STU     $FFFF                   
FBF6: FF FF FF        STU     $FFFF                   
FBF9: FF FF FF        STU     $FFFF                   
FBFC: FF FF FF        STU     $FFFF                   
FBFF: FF FF FF        STU     $FFFF                   
FC02: FF FF FF        STU     $FFFF                   
FC05: FF FF FF        STU     $FFFF                   
FC08: FF FF FF        STU     $FFFF                   
FC0B: FF FF FF        STU     $FFFF                   
FC0E: FF FF FF        STU     $FFFF                   
FC11: FF FF FF        STU     $FFFF                   
FC14: FF FF FF        STU     $FFFF                   
FC17: FF FF FF        STU     $FFFF                   
FC1A: FF FF FF        STU     $FFFF                   
FC1D: FF FF FF        STU     $FFFF                   
FC20: FF FF FF        STU     $FFFF                   
FC23: FF FF FF        STU     $FFFF                   
FC26: FF FF FF        STU     $FFFF                   
FC29: FF FF FF        STU     $FFFF                   
FC2C: FF FF FF        STU     $FFFF                   
FC2F: FF FF FF        STU     $FFFF                   
FC32: FF FF FF        STU     $FFFF                   
FC35: FF FF FF        STU     $FFFF                   
FC38: FF FF FF        STU     $FFFF                   
FC3B: FF FF FF        STU     $FFFF                   
FC3E: FF FF FF        STU     $FFFF                   
FC41: FF FF FF        STU     $FFFF                   
FC44: FF FF FF        STU     $FFFF                   
FC47: FF FF FF        STU     $FFFF                   
FC4A: FF FF FF        STU     $FFFF                   
FC4D: FF FF FF        STU     $FFFF                   
FC50: FF FF FF        STU     $FFFF                   
FC53: FF FF FF        STU     $FFFF                   
FC56: FF FF FF        STU     $FFFF                   
FC59: FF FF FF        STU     $FFFF                   
FC5C: FF FF FF        STU     $FFFF                   
FC5F: FF FF FF        STU     $FFFF                   
FC62: FF FF FF        STU     $FFFF                   
FC65: FF FF FF        STU     $FFFF                   
FC68: FF FF FF        STU     $FFFF                   
FC6B: FF FF FF        STU     $FFFF                   
FC6E: FF FF FF        STU     $FFFF                   
FC71: FF FF FF        STU     $FFFF                   
FC74: FF FF FF        STU     $FFFF                   
FC77: FF FF FF        STU     $FFFF                   
FC7A: FF FF FF        STU     $FFFF                   
FC7D: FF FF FF        STU     $FFFF                   
FC80: FF FF FF        STU     $FFFF                   
FC83: FF FF FF        STU     $FFFF                   
FC86: FF FF FF        STU     $FFFF                   
FC89: FF FF FF        STU     $FFFF                   
FC8C: FF FF FF        STU     $FFFF                   
FC8F: FF FF FF        STU     $FFFF                   
FC92: FF FF FF        STU     $FFFF                   
FC95: FF FF FF        STU     $FFFF                   
FC98: FF FF FF        STU     $FFFF                   
FC9B: FF FF FF        STU     $FFFF                   
FC9E: FF FF FF        STU     $FFFF                   
FCA1: FF FF FF        STU     $FFFF                   
FCA4: FF FF FF        STU     $FFFF                   
FCA7: FF FF FF        STU     $FFFF                   
FCAA: FF FF FF        STU     $FFFF                   
FCAD: FF FF FF        STU     $FFFF                   
FCB0: FF FF FF        STU     $FFFF                   
FCB3: FF FF FF        STU     $FFFF                   
FCB6: FF FF FF        STU     $FFFF                   
FCB9: FF FF FF        STU     $FFFF                   
FCBC: FF FF FF        STU     $FFFF                   
FCBF: FF FF FF        STU     $FFFF                   
FCC2: FF FF FF        STU     $FFFF                   
FCC5: FF FF FF        STU     $FFFF                   
FCC8: FF FF FF        STU     $FFFF                   
FCCB: FF FF FF        STU     $FFFF                   
FCCE: FF FF FF        STU     $FFFF                   
FCD1: FF FF FF        STU     $FFFF                   
FCD4: FF FF FF        STU     $FFFF                   
FCD7: FF FF FF        STU     $FFFF                   
FCDA: FF FF FF        STU     $FFFF                   
FCDD: FF FF FF        STU     $FFFF                   
FCE0: FF FF FF        STU     $FFFF                   
FCE3: FF FF FF        STU     $FFFF                   
FCE6: FF FF FF        STU     $FFFF                   
FCE9: FF FF FF        STU     $FFFF                   
FCEC: FF FF FF        STU     $FFFF                   
FCEF: FF FF FF        STU     $FFFF                   
FCF2: FF FF FF        STU     $FFFF                   
FCF5: FF FF FF        STU     $FFFF                   
FCF8: FF FF FF        STU     $FFFF                   
FCFB: FF FF FF        STU     $FFFF                   
FCFE: FF FF FF        STU     $FFFF                   
FD01: FF FF FF        STU     $FFFF                   
FD04: FF FF FF        STU     $FFFF                   
FD07: FF FF FF        STU     $FFFF                   
FD0A: FF FF FF        STU     $FFFF                   
FD0D: FF FF FF        STU     $FFFF                   
FD10: FF FF FF        STU     $FFFF                   
FD13: FF FF FF        STU     $FFFF                   
FD16: FF FF FF        STU     $FFFF                   
FD19: FF FF FF        STU     $FFFF                   
FD1C: FF FF FF        STU     $FFFF                   
FD1F: FF FF FF        STU     $FFFF                   
FD22: FF FF FF        STU     $FFFF                   
FD25: FF FF FF        STU     $FFFF                   
FD28: FF FF FF        STU     $FFFF                   
FD2B: FF FF FF        STU     $FFFF                   
FD2E: FF FF FF        STU     $FFFF                   
FD31: FF FF FF        STU     $FFFF                   
FD34: FF FF FF        STU     $FFFF                   
FD37: FF FF FF        STU     $FFFF                   
FD3A: FF FF FF        STU     $FFFF                   
FD3D: FF FF FF        STU     $FFFF                   
FD40: FF FF FF        STU     $FFFF                   
FD43: FF FF FF        STU     $FFFF                   
FD46: FF FF FF        STU     $FFFF                   
FD49: FF FF FF        STU     $FFFF                   
FD4C: FF FF FF        STU     $FFFF                   
FD4F: FF FF FF        STU     $FFFF                   
FD52: FF FF FF        STU     $FFFF                   
FD55: FF FF FF        STU     $FFFF                   
FD58: FF FF FF        STU     $FFFF                   
FD5B: FF FF FF        STU     $FFFF                   
FD5E: FF FF FF        STU     $FFFF                   
FD61: FF FF FF        STU     $FFFF                   
FD64: FF FF FF        STU     $FFFF                   
FD67: FF FF FF        STU     $FFFF                   
FD6A: FF FF FF        STU     $FFFF                   
FD6D: FF FF FF        STU     $FFFF                   
FD70: FF FF FF        STU     $FFFF                   
FD73: FF FF FF        STU     $FFFF                   
FD76: FF FF FF        STU     $FFFF                   
FD79: FF FF FF        STU     $FFFF                   
FD7C: FF FF FF        STU     $FFFF                   
FD7F: FF FF FF        STU     $FFFF                   
FD82: FF FF FF        STU     $FFFF                   
FD85: FF FF FF        STU     $FFFF                   
FD88: FF FF FF        STU     $FFFF                   
FD8B: FF FF FF        STU     $FFFF                   
FD8E: FF FF FF        STU     $FFFF                   
FD91: FF FF FF        STU     $FFFF                   
FD94: FF FF FF        STU     $FFFF                   
FD97: FF FF FF        STU     $FFFF                   
FD9A: FF FF FF        STU     $FFFF                   
FD9D: FF FF FF        STU     $FFFF                   
FDA0: FF FF FF        STU     $FFFF                   
FDA3: FF FF FF        STU     $FFFF                   
FDA6: FF FF FF        STU     $FFFF                   
FDA9: FF FF FF        STU     $FFFF                   
FDAC: FF FF FF        STU     $FFFF                   
FDAF: FF FF FF        STU     $FFFF                   
FDB2: FF FF FF        STU     $FFFF                   
FDB5: FF FF FF        STU     $FFFF                   
FDB8: FF FF FF        STU     $FFFF                   
FDBB: FF FF FF        STU     $FFFF                   
FDBE: FF FF FF        STU     $FFFF                   
FDC1: FF FF FF        STU     $FFFF                   
FDC4: FF FF FF        STU     $FFFF                   
FDC7: FF FF FF        STU     $FFFF                   
FDCA: FF FF FF        STU     $FFFF                   
FDCD: FF FF FF        STU     $FFFF                   
FDD0: FF FF FF        STU     $FFFF                   
FDD3: FF FF FF        STU     $FFFF                   
FDD6: FF FF FF        STU     $FFFF                   
FDD9: FF FF FF        STU     $FFFF                   
FDDC: FF FF FF        STU     $FFFF                   
FDDF: FF FF FF        STU     $FFFF                   
FDE2: FF FF FF        STU     $FFFF                   
FDE5: FF FF FF        STU     $FFFF                   
FDE8: FF FF FF        STU     $FFFF                   
FDEB: FF FF FF        STU     $FFFF                   
FDEE: FF FF FF        STU     $FFFF                   
FDF1: FF FF FF        STU     $FFFF                   
FDF4: FF FF FF        STU     $FFFF                   
FDF7: FF FF FF        STU     $FFFF                   
FDFA: FF FF FF        STU     $FFFF                   
FDFD: FF FF FF        STU     $FFFF                   
FE00: FF FF FF        STU     $FFFF                   
FE03: FF FF FF        STU     $FFFF                   
FE06: FF FF FF        STU     $FFFF                   
FE09: FF FF FF        STU     $FFFF                   
FE0C: FF FF FF        STU     $FFFF                   
FE0F: FF FF FF        STU     $FFFF                   
FE12: FF FF FF        STU     $FFFF                   
FE15: FF FF FF        STU     $FFFF                   
FE18: FF FF FF        STU     $FFFF                   
FE1B: FF FF FF        STU     $FFFF                   
FE1E: FF FF FF        STU     $FFFF                   
FE21: FF FF FF        STU     $FFFF                   
FE24: FF FF FF        STU     $FFFF                   
FE27: FF FF FF        STU     $FFFF                   
FE2A: FF FF FF        STU     $FFFF                   
FE2D: FF FF FF        STU     $FFFF                   
FE30: FF FF FF        STU     $FFFF                   
FE33: FF FF FF        STU     $FFFF                   
FE36: FF FF FF        STU     $FFFF                   
FE39: FF FF FF        STU     $FFFF                   
FE3C: FF FF FF        STU     $FFFF                   
FE3F: FF FF FF        STU     $FFFF                   
FE42: FF FF FF        STU     $FFFF                   
FE45: FF FF FF        STU     $FFFF                   
FE48: FF FF FF        STU     $FFFF                   
FE4B: FF FF FF        STU     $FFFF                   
FE4E: FF FF FF        STU     $FFFF                   
FE51: FF FF FF        STU     $FFFF                   
FE54: FF FF FF        STU     $FFFF                   
FE57: FF FF FF        STU     $FFFF                   
FE5A: FF FF FF        STU     $FFFF                   
FE5D: FF FF FF        STU     $FFFF                   
FE60: FF FF FF        STU     $FFFF                   
FE63: FF FF FF        STU     $FFFF                   
FE66: FF FF FF        STU     $FFFF                   
FE69: FF FF FF        STU     $FFFF                   
FE6C: FF FF FF        STU     $FFFF                   
FE6F: FF FF FF        STU     $FFFF                   
FE72: FF FF FF        STU     $FFFF                   
FE75: FF FF FF        STU     $FFFF                   
FE78: FF FF FF        STU     $FFFF                   
FE7B: FF FF FF        STU     $FFFF                   
FE7E: FF FF FF        STU     $FFFF                   
FE81: FF FF FF        STU     $FFFF                   
FE84: FF FF FF        STU     $FFFF                   
FE87: FF FF FF        STU     $FFFF                   
FE8A: FF FF FF        STU     $FFFF                   
FE8D: FF FF FF        STU     $FFFF                   
FE90: FF FF FF        STU     $FFFF                   
FE93: FF FF FF        STU     $FFFF                   
FE96: FF FF FF        STU     $FFFF                   
FE99: FF FF FF        STU     $FFFF                   
FE9C: FF FF FF        STU     $FFFF                   
FE9F: FF FF FF        STU     $FFFF                   
FEA2: FF FF FF        STU     $FFFF                   
FEA5: FF FF FF        STU     $FFFF                   
FEA8: FF FF FF        STU     $FFFF                   
FEAB: FF FF FF        STU     $FFFF                   
FEAE: FF FF FF        STU     $FFFF                   
FEB1: FF FF FF        STU     $FFFF                   
FEB4: FF FF FF        STU     $FFFF                   
FEB7: FF FF FF        STU     $FFFF                   
FEBA: FF FF FF        STU     $FFFF                   
FEBD: FF FF FF        STU     $FFFF                   
FEC0: FF FF FF        STU     $FFFF                   
FEC3: FF FF FF        STU     $FFFF                   
FEC6: FF FF FF        STU     $FFFF                   
FEC9: FF FF FF        STU     $FFFF                   
FECC: FF FF FF        STU     $FFFF                   
FECF: FF FF FF        STU     $FFFF                   
FED2: FF FF FF        STU     $FFFF                   
FED5: FF FF FF        STU     $FFFF                   
FED8: FF FF FF        STU     $FFFF                   
FEDB: FF FF FF        STU     $FFFF                   
FEDE: FF FF FF        STU     $FFFF                   
FEE1: FF FF FF        STU     $FFFF                   
FEE4: FF FF FF        STU     $FFFF                   
FEE7: FF FF FF        STU     $FFFF                   
FEEA: FF FF FF        STU     $FFFF                   
FEED: FF FF FF        STU     $FFFF                   
FEF0: FF FF FF        STU     $FFFF                   
FEF3: FF FF FF        STU     $FFFF                   
FEF6: FF FF FF        STU     $FFFF                   
FEF9: FF FF FF        STU     $FFFF                   
FEFC: FF FF FF        STU     $FFFF                   
FEFF: FF FF FF        STU     $FFFF                   
FF02: FF FF FF        STU     $FFFF                   
FF05: FF FF FF        STU     $FFFF                   
FF08: FF FF FF        STU     $FFFF                   
FF0B: FF FF FF        STU     $FFFF                   
FF0E: FF FF FF        STU     $FFFF                   
FF11: FF FF FF        STU     $FFFF                   
FF14: FF FF FF        STU     $FFFF                   
FF17: FF FF FF        STU     $FFFF                   
FF1A: FF FF FF        STU     $FFFF                   
FF1D: FF FF FF        STU     $FFFF                   
FF20: FF FF FF        STU     $FFFF                   
FF23: FF FF FF        STU     $FFFF                   
FF26: FF FF FF        STU     $FFFF                   
FF29: FF FF FF        STU     $FFFF                   
FF2C: FF FF FF        STU     $FFFF                   
FF2F: FF FF FF        STU     $FFFF                   
FF32: FF FF FF        STU     $FFFF                   
FF35: FF FF FF        STU     $FFFF                   
FF38: FF FF FF        STU     $FFFF                   
FF3B: FF FF FF        STU     $FFFF                   
FF3E: FF FF FF        STU     $FFFF                   
FF41: FF FF FF        STU     $FFFF                   
FF44: FF FF FF        STU     $FFFF                   
FF47: FF FF FF        STU     $FFFF                   
FF4A: FF FF FF        STU     $FFFF                   
FF4D: FF FF FF        STU     $FFFF                   
FF50: FF FF FF        STU     $FFFF                   
FF53: FF FF FF        STU     $FFFF                   
FF56: FF FF FF        STU     $FFFF                   
FF59: FF FF FF        STU     $FFFF                   
FF5C: FF FF FF        STU     $FFFF                   
FF5F: FF FF FF        STU     $FFFF                   
FF62: FF FF FF        STU     $FFFF                   
FF65: FF FF FF        STU     $FFFF                   
FF68: FF FF FF        STU     $FFFF                   
FF6B: FF FF FF        STU     $FFFF                   
FF6E: FF FF FF        STU     $FFFF                   
FF71: FF FF FF        STU     $FFFF                   
FF74: FF FF FF        STU     $FFFF                   
FF77: FF FF FF        STU     $FFFF                   
FF7A: FF FF FF        STU     $FFFF                   
FF7D: FF FF FF        STU     $FFFF                   
FF80: FF FF FF        STU     $FFFF                   
FF83: FF FF FF        STU     $FFFF                   
FF86: FF FF FF        STU     $FFFF                   
FF89: FF FF FF        STU     $FFFF                   
FF8C: FF FF FF        STU     $FFFF                   
FF8F: FF FF FF        STU     $FFFF                   
FF92: FF FF FF        STU     $FFFF                   
FF95: FF FF FF        STU     $FFFF                   
FF98: FF FF FF        STU     $FFFF                   
FF9B: FF FF FF        STU     $FFFF                   
FF9E: FF FF FF        STU     $FFFF                   
FFA1: FF FF FF        STU     $FFFF                   
FFA4: FF FF FF        STU     $FFFF                   
FFA7: FF FF FF        STU     $FFFF                   
FFAA: FF FF FF        STU     $FFFF                   
FFAD: FF FF FF        STU     $FFFF                   
FFB0: FF FF FF        STU     $FFFF                   
FFB3: FF FF FF        STU     $FFFF                   
FFB6: FF FF FF        STU     $FFFF                   
FFB9: FF FF FF        STU     $FFFF                   
FFBC: FF FF FF        STU     $FFFF                   
FFBF: FF 31 39        STU     $3139                   
FFC2: 38 ; ????
FFC3: 35 20           PULS    Y                   
FFC5: 4E ; ????
FFC6: 41 ; ????
FFC7: 4D              TSTA                        
FFC8: 43              COMA                        
FFC9: 4F              CLRA                        
FFCA: 20 41           BRA     $1000D                   
FFCC: 4C              INCA                        
FFCD: 4C              INCA                        
FFCE: 20 52           BRA     $10022                   
FFD0: 49              ROLA                        
FFD1: 47              ASRA                        
FFD2: 48 ; ????
FFD3: 54              LSRB                        
FFD4: 53              COMB                        
FFD5: 20 52           BRA     $10029                   
FFD7: 45 ; ????
FFD8: 53              COMB                        
FFD9: 45 ; ????
FFDA: 52 ; ????
FFDB: 56              RORB                        
FFDC: 45 ; ????
FFDD: 44              LSRA                        
FFDE: FF FF FF        STU     $FFFF                   
FFE1: FF FF FF        STU     $FFFF                   
FFE4: FF FF FF        STU     $FFFF                   
FFE7: FF FF FF        STU     $FFFF                   
FFEA: FF FF FF        STU     $FFFF                   
FFED: FF FF FF        STU     $FFFF                   

; Vectors

FFF0: FF 57 ; Reserved
FFF2: E5 BA ; SWI3 (to reset)
FFF4: E5 BA ; SWI2 (to reset)
FFF6: E5 BA ; FIRQ (to reset)
FFF8: 80 00 ; IRQ (to reset)
FFFA: E5 BA ; SWI (to reset)
FFFC: E5 BA ; NMI (to reset)
FFFE: E5 BA ; RESET (to reset)
