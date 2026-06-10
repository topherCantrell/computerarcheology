![Xenos](Xenos.png)

# Xenos SECTION8.DAT

>>> cpu Z80

>>> binary 5200:roms/section8.bin

```code
5200: 00 87 8A                      ; List ID: 0x00, Length: 0x078A

5203: 84 2B 00                      ; room=84_8_??84??, Length: 0x002B, Data: 0x00
;
5206:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5208:       9C                      ;     ROUTINE 0x9C
;
5209:    04 25                      ;   Section COMMANDS, Length: 0x0025
520B:       0B 23 0A                ;     SWITCH, Length: 0x0023, Function to call: 0x0A
520E:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
520F:          04                   ;       ELSE go to: 0x5214
5210:             0E 02             ;         WHILE FAIL, Length: 0x0002
5212:                A0             ;           ROUTINE 0xA0
5213:                A1             ;           ROUTINE 0xA1
5214:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
5215:          1A                   ;       ELSE go to: 0x5230
5216:             0D 18             ;         WHILE PASS, Length: 0x0018
5218:                C0             ;           ROUTINE 0xC0
5219:                0E 15          ;           WHILE FAIL, Length: 0x0015
521B:                   AE          ;             ROUTINE 0xAE
521C:                   14          ;             EXECUTE AND REVERSE STATUS
521D:                   0B 10 03    ;             SWITCH, Length: 0x0010, Function to call: 0x03
5220:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
5221:                      3E       ;               ELSE go to: 0x5260
5222:                         07    ;                 PRINT ROOM DESCRIPTION
5223:                      0D       ;               Phrase 0x0D: "THROW    .vC.....   AT       ...P...."
5224:                      05       ;               ELSE go to: 0x522A
5225:                         9E    ;                 ROUTINE 0x9E
5226:                      30       ;               Phrase 0x30: "??30??"
5227:                      82 2F    ;               ELSE go to: 0x5458
5229:                         07    ;                 PRINT ROOM DESCRIPTION
522A:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
522B:                      3E       ;               ELSE go to: 0x526A
522C:                         02 00 86 ;                 IS OWNED BY, A=0x86, obj=??00??
522F:                   9E          ;             ROUTINE 0x9E

5230: 86 80 BF 00                   ; room=86_8_FOOGLURN_GALLEY, Length: 0x00BF, Data: 0x00
;
5234:    03 80 99                   ;   Section DESCRIPTION, Length: 0x0099
5237:       0D 80 96                ;     WHILE PASS, Length: 0x0096
523A:          04 06                ;       PRINT, Length: 0x0006
523C:             01 68 CF 6D C3 B2 ; 
;
;                 FOOGLURN 
;
5242:          0E 07                ;       WHILE FAIL, Length: 0x0007
5244:             C3                ;         ROUTINE 0xC3
5245:             04 04             ;         PRINT, Length: 0x0004
5247:                0E 6C FB 8B    ; 
;
;                    GALLEY
;
524B:          8B                   ;       ROUTINE 0x8B
524C:          04 80 81             ;       PRINT, Length: 0x0081
524F:             C7 DE 94 14 4B 5E 83 96 5F 17 46 48 84 15 3B 63 ; 
525F:             01 B3 DB 95 5F BE 5B B1 4B 7B 4E 45 31 49 55 5E ; 
526F:             A3 AD 5B B1 65 B1 65 62 D0 15 C0 16 59 5E 46 48 ; 
527F:             51 F4 17 98 71 16 7E B1 49 16 9B 9F AB 98 6A 4D ; 
528F:             8E 7A 51 18 B3 C7 C7 DE 57 17 56 5E DB 72 4B A4 ; 
529F:             91 AF 94 64 F3 5F 8E 48 B6 14 1B C4 F6 4F 80 BF ; 
52AF:             D1 B5 96 96 DB 72 0E D0 9B 8F 5F BE 5B B1 4B 7B ; 
52BF:             55 45 8E 91 19 8A 96 73 56 5E B6 46 4A 5E 2F 62 ; 
52CF:             2E                ; 
;
;                 YOU ARE IN A SMALL GREY ROOM. THERE IS A LARGE SQUARE
;                 RECESS IN ONE WALL. ONCE MORE, LOOKING BEHIND YOU, YOU SEE
;                 THE PAIR OF RED AND BLUE BUTTONS ON THE WALL. THERE IS A
;                 SMALL WHITE TABLE HERE.
;
;
52D0:    04 20                      ;   Section COMMANDS, Length: 0x0020
52D2:       0B 1E 0A                ;     SWITCH, Length: 0x001E, Function to call: 0x0A
52D5:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
52D6:          04                   ;       ELSE go to: 0x52DB
52D7:             0E 02             ;         WHILE FAIL, Length: 0x0002
52D9:                A0             ;           ROUTINE 0xA0
52DA:                A1             ;           ROUTINE 0xA1
52DB:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
52DC:          15                   ;       ELSE go to: 0x52F2
52DD:             0D 13             ;         WHILE PASS, Length: 0x0013
52DF:                C0             ;           ROUTINE 0xC0
52E0:                0E 10          ;           WHILE FAIL, Length: 0x0010
52E2:                   AE          ;             ROUTINE 0xAE
52E3:                   14          ;             EXECUTE AND REVERSE STATUS
52E4:                   0B 0B 03    ;             SWITCH, Length: 0x000B, Function to call: 0x03
52E7:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
52E8:                      3E       ;               ELSE go to: 0x5327
52E9:                         02 00 84 ;                 IS OWNED BY, A=0x84, obj=??00??
52EC:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
52ED:                      3E       ;               ELSE go to: 0x532C
52EE:                         02 00 88 ;                 IS OWNED BY, A=0x88, obj=??00??
52F1:                   9E          ;             ROUTINE 0x9E

52F2: 88 26 00                      ; room=88_8_??88??, Length: 0x0026, Data: 0x00
;
52F5:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
52F7:       9C                      ;     ROUTINE 0x9C
;
52F8:    04 20                      ;   Section COMMANDS, Length: 0x0020
52FA:       0B 1E 0A                ;     SWITCH, Length: 0x001E, Function to call: 0x0A
52FD:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
52FE:          04                   ;       ELSE go to: 0x5303
52FF:             0E 02             ;         WHILE FAIL, Length: 0x0002
5301:                A0             ;           ROUTINE 0xA0
5302:                A1             ;           ROUTINE 0xA1
5303:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
5304:          15                   ;       ELSE go to: 0x531A
5305:             0D 13             ;         WHILE PASS, Length: 0x0013
5307:                C0             ;           ROUTINE 0xC0
5308:                0E 10          ;           WHILE FAIL, Length: 0x0010
530A:                   AE          ;             ROUTINE 0xAE
530B:                   14          ;             EXECUTE AND REVERSE STATUS
530C:                   0B 0B 03    ;             SWITCH, Length: 0x000B, Function to call: 0x03
530F:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
5310:                      3E       ;               ELSE go to: 0x534F
5311:                         02 00 86 ;                 IS OWNED BY, A=0x86, obj=??00??
5314:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
5315:                      3E       ;               ELSE go to: 0x5354
5316:                         02 00 8A ;                 IS OWNED BY, A=0x8A, obj=??00??
5319:                   9E          ;             ROUTINE 0x9E

531A: 8A 80 D4 00                   ; room=8A_8_SPLURB_RECREATION, Length: 0x00D4, Data: 0x00
;
531E:    03 80 AE                   ;   Section DESCRIPTION, Length: 0x00AE
5321:       0D 80 AB                ;     WHILE PASS, Length: 0x00AB
5324:          04 04                ;       PRINT, Length: 0x0004
5326:             66 B9 2C C6       ; 
;
;                 SPLURB
;
532A:          0E 0A                ;       WHILE FAIL, Length: 0x000A
532C:             C3                ;         ROUTINE 0xC3
532D:             04 07             ;         PRINT, Length: 0x0007
532F:                65 B1 63 B1 91 BE 4E ; 
;
;                    RECREATION
;
5336:          8B                   ;       ROUTINE 0x8B
5337:          04 80 95             ;       PRINT, Length: 0x0095
533A:             C7 DE 94 14 4B 5E 83 96 FA 17 7F 7B 39 17 DB 9F ; 
534A:             56 D1 03 71 DA 14 D4 47 FA 17 DA 78 4B 15 B5 53 ; 
535A:             82 17 59 5E 66 62 F3 17 17 8D 82 17 2F 62 D5 15 ; 
536A:             7B 14 AB D0 33 B1 81 8D 50 86 CA 6A 8E 48 B3 6E ; 
537A:             16 A3 56 72 3A 15 F0 BD 0B 5C 36 A1 B8 16 82 17 ; 
538A:             59 5E 46 48 89 17 14 D0 0B 5C 5F BE DA 14 D4 47 ; 
539A:             56 F4 DB 72 0E D0 04 8A A3 60 33 98 5F BE E6 16 ; 
53AA:             D7 46 51 18 43 C2 5B B1 FB B9 43 98 AB 98 55 72 ; 
53BA:             7B 14 66 B1 90 14 03 58 B6 14 1B C4 F6 4F 80 BF ; 
53CA:             C0 16 D6 15 2E    ; 
;
;                 YOU ARE IN A WHITE ROOM WITH A CHAIR WHICH FACES THE WEST
;                 WALL. THERE IS A WEIRD LOOKING HANDGRIP THAT EXTENDS OUT OF
;                 THE WALL TOWARDS THE CHAIR. THE WALL BEHIND THE PLACE YOU
;                 ARE STANDING HAS A RED AND A BLUE BUTTON ON IT.
;
;
53CF:    04 20                      ;   Section COMMANDS, Length: 0x0020
53D1:       0B 1E 0A                ;     SWITCH, Length: 0x001E, Function to call: 0x0A
53D4:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
53D5:          04                   ;       ELSE go to: 0x53DA
53D6:             0E 02             ;         WHILE FAIL, Length: 0x0002
53D8:                A0             ;           ROUTINE 0xA0
53D9:                A1             ;           ROUTINE 0xA1
53DA:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
53DB:          15                   ;       ELSE go to: 0x53F1
53DC:             0D 13             ;         WHILE PASS, Length: 0x0013
53DE:                C0             ;           ROUTINE 0xC0
53DF:                0E 10          ;           WHILE FAIL, Length: 0x0010
53E1:                   AE          ;             ROUTINE 0xAE
53E2:                   14          ;             EXECUTE AND REVERSE STATUS
53E3:                   0B 0B 03    ;             SWITCH, Length: 0x000B, Function to call: 0x03
53E6:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
53E7:                      3E       ;               ELSE go to: 0x5426
53E8:                         02 00 88 ;                 IS OWNED BY, A=0x88, obj=??00??
53EB:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
53EC:                      3E       ;               ELSE go to: 0x542B
53ED:                         02 00 8C ;                 IS OWNED BY, A=0x8C, obj=??00??
53F0:                   9E          ;             ROUTINE 0x9E

53F1: 8C 2C 00                      ; room=8C_8_??8C??, Length: 0x002C, Data: 0x00
;
53F4:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
53F6:       B0                      ;     ROUTINE 0xB0
;
53F7:    04 26                      ;   Section COMMANDS, Length: 0x0026
53F9:       0B 24 0A                ;     SWITCH, Length: 0x0024, Function to call: 0x0A
53FC:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
53FD:          05                   ;       ELSE go to: 0x5403
53FE:             0E 03             ;         WHILE FAIL, Length: 0x0003
5400:                9F             ;           ROUTINE 0x9F
5401:                A0             ;           ROUTINE 0xA0
5402:                A1             ;           ROUTINE 0xA1
5403:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
5404:          1A                   ;       ELSE go to: 0x541F
5405:             0D 18             ;         WHILE PASS, Length: 0x0018
5407:                C0             ;           ROUTINE 0xC0
5408:                0E 15          ;           WHILE FAIL, Length: 0x0015
540A:                   AE          ;             ROUTINE 0xAE
540B:                   14          ;             EXECUTE AND REVERSE STATUS
540C:                   0B 10 03    ;             SWITCH, Length: 0x0010, Function to call: 0x03
540F:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
5410:                      3E       ;               ELSE go to: 0x544F
5411:                         02 00 8A ;                 IS OWNED BY, A=0x8A, obj=??00??
5414:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
5415:                      3E       ;               ELSE go to: 0x5454
5416:                         02 00 8E ;                 IS OWNED BY, A=0x8E, obj=??00??
5419:                      3F       ;               Phrase 0x3F: "SAVE     *          *           *"
541A:                      3E       ;               ELSE go to: 0x5459
541B:                         02 00 9A ;                 IS OWNED BY, A=0x9A, obj=??00??
541E:                   9E          ;             ROUTINE 0x9E

541F: 8E 80 9C 00                   ; room=8E_8_KURABEL_SICK_BAY, Length: 0x009C, Data: 0x00
;
5423:    03 77                      ;   Section DESCRIPTION, Length: 0x0077
5425:       0D 75                   ;     WHILE PASS, Length: 0x0075
5427:          04 05                ;       PRINT, Length: 0x0005
5429:             34 88 AF 46 4C    ; 
;
;                 KURABEL
;
542E:          0E 09                ;       WHILE FAIL, Length: 0x0009
5430:             C3                ;         ROUTINE 0xC3
5431:             04 06             ;         PRINT, Length: 0x0006
5433:                45 B8 C4 83 3B 4A ; 
;
;                    SICK BAY 
;
5439:          8B                   ;       ROUTINE 0x8B
543A:          04 60                ;       PRINT, Length: 0x0060
543C:             C7 DE 94 14 4B 5E 83 96 5F 17 46 48 39 17 FF 9F ; 
544C:             82 17 2F 62 D5 15 7B 14 66 B1 7B 17 7F 4E 89 14 ; 
545C:             D0 47 F3 B9 0F A0 F3 17 17 8D C0 16 82 17 51 5E ; 
546C:             A9 A6 50 B8 D9 6A 46 48 82 17 2F 62 D5 15 82 17 ; 
547C:             50 5E 6B A1 CF 65 43 7A 23 49 66 B1 90 14 04 58 ; 
548C:             67 8E BF 14 49 C0 83 96 6B B3 B7 98 30 92 9B C1 ; 
;
;                 YOU ARE IN A SMALL ROOM. THERE IS A RED TABLE AGAINST ONE
;                 WALL. ON THE OPPOSING WALL THERE IS THE NOW FAMILIAR RED
;                 AND BLUE BUTTON ARRANGEMENT.
;
;
549C:    04 20                      ;   Section COMMANDS, Length: 0x0020
549E:       0B 1E 0A                ;     SWITCH, Length: 0x001E, Function to call: 0x0A
54A1:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
54A2:          04                   ;       ELSE go to: 0x54A7
54A3:             0E 02             ;         WHILE FAIL, Length: 0x0002
54A5:                A0             ;           ROUTINE 0xA0
54A6:                A1             ;           ROUTINE 0xA1
54A7:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
54A8:          15                   ;       ELSE go to: 0x54BE
54A9:             0D 13             ;         WHILE PASS, Length: 0x0013
54AB:                C0             ;           ROUTINE 0xC0
54AC:                0E 10          ;           WHILE FAIL, Length: 0x0010
54AE:                   AE          ;             ROUTINE 0xAE
54AF:                   14          ;             EXECUTE AND REVERSE STATUS
54B0:                   0B 0B 03    ;             SWITCH, Length: 0x000B, Function to call: 0x03
54B3:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
54B4:                      3E       ;               ELSE go to: 0x54F3
54B5:                         02 00 8C ;                 IS OWNED BY, A=0x8C, obj=??00??
54B8:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
54B9:                      3E       ;               ELSE go to: 0x54F8
54BA:                         02 00 8F ;                 IS OWNED BY, A=0x8F, obj=??00??
54BD:                   9E          ;             ROUTINE 0x9E

54BE: 8F 26 00                      ; room=8F_8_??8F??, Length: 0x0026, Data: 0x00
;
54C1:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
54C3:       9C                      ;     ROUTINE 0x9C
;
54C4:    04 20                      ;   Section COMMANDS, Length: 0x0020
54C6:       0B 1E 0A                ;     SWITCH, Length: 0x001E, Function to call: 0x0A
54C9:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
54CA:          04                   ;       ELSE go to: 0x54CF
54CB:             0E 02             ;         WHILE FAIL, Length: 0x0002
54CD:                A0             ;           ROUTINE 0xA0
54CE:                A1             ;           ROUTINE 0xA1
54CF:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
54D0:          15                   ;       ELSE go to: 0x54E6
54D1:             0D 13             ;         WHILE PASS, Length: 0x0013
54D3:                C0             ;           ROUTINE 0xC0
54D4:                0E 10          ;           WHILE FAIL, Length: 0x0010
54D6:                   AE          ;             ROUTINE 0xAE
54D7:                   14          ;             EXECUTE AND REVERSE STATUS
54D8:                   0B 0B 03    ;             SWITCH, Length: 0x000B, Function to call: 0x03
54DB:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
54DC:                      3E       ;               ELSE go to: 0x551B
54DD:                         02 00 8E ;                 IS OWNED BY, A=0x8E, obj=??00??
54E0:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
54E1:                      3E       ;               ELSE go to: 0x5520
54E2:                         02 00 90 ;                 IS OWNED BY, A=0x90, obj=??00??
54E5:                   9E          ;             ROUTINE 0x9E

54E6: 90 81 10 00                   ; room=90_8_ENURGLE_POWER, Length: 0x0110, Data: 0x00
;
54EA:    03 80 EA                   ;   Section DESCRIPTION, Length: 0x00EA
54ED:       0D 80 E7                ;     WHILE PASS, Length: 0x00E7
54F0:          04 05                ;       PRINT, Length: 0x0005
54F2:             9F 61 BE B1 45    ; 
;
;                 ENURGLE
;
54F7:          0E 07                ;       WHILE FAIL, Length: 0x0007
54F9:             C3                ;         ROUTINE 0xC3
54FA:             04 04             ;         PRINT, Length: 0x0004
54FC:                89 A6 23 62    ; 
;
;                    POWER 
;
5500:          8B                   ;       ROUTINE 0x8B
5501:          04 80 D3             ;       PRINT, Length: 0x00D3
5504:             C7 DE 94 14 4B 5E 83 96 39 17 DB 9F 56 D1 03 71 ; 
5514:             77 15 C6 9A 58 5E BE 7A 73 62 89 8C 33 75 63 61 ; 
5524:             D6 97 91 7A 5C 15 DB 9F 5F BE D7 14 43 7A CF 98 ; 
5534:             82 17 2F 62 D5 15 7B 14 54 8B 9B 6C 36 92 33 48 ; 
5544:             E6 A4 66 62 33 48 FB B9 43 98 AB 98 83 7A 5F BE ; 
5554:             D7 14 BF 9A 91 AF 96 64 DB 72 01 B3 DB 95 5F BE ; 
5564:             5B B1 4B 7B 56 45 2B D2 8D 7A 15 71 A3 AD 5B B1 ; 
5574:             7E 74 4B 5E 96 96 DB 72 82 BF B8 16 82 17 52 5E ; 
5584:             FF 5F FB B9 9B 8F 03 A0 5F BE F3 17 F3 8C C7 DE ; 
5594:             84 AF DD 46 D0 15 83 7B 46 48 48 DB D7 46 73 5D ; 
55A4:             2F 49 7B 14 66 B1 BF 14 49 C0 83 96 33 98 44 45 ; 
55B4:             67 8E BF 14 49 C0 83 96 6B B3 B7 98 0A 58 B3 A0 ; 
55C4:             00 E5 4E BD FB 8E 79 68 4E 90 5E 60 89 17 33 17 ; 
55D4:             2E 6D 2E          ; 
;
;                 YOU ARE IN A ROOM WITH A GENTLE VIOLET LIGHT EMANATING FROM
;                 THE CEILING. THERE IS A LARGE METAL PEDESTAL STANDING IN
;                 THE CENTER OF THE ROOM. THERE IS A TWO INCH SQUARE HOLE IN
;                 THE TOP OF THE PEDESTAL. ON THE WALL YOUR BACK INITIALLY
;                 FACED, ARE A RED BUTTON AND A BLUE BUTTON ARRANGED
;                 HORIZONTALLY FROM LEFT TO RIGHT.
;
;
55D7:    04 20                      ;   Section COMMANDS, Length: 0x0020
55D9:       0B 1E 0A                ;     SWITCH, Length: 0x001E, Function to call: 0x0A
55DC:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
55DD:          04                   ;       ELSE go to: 0x55E2
55DE:             0E 02             ;         WHILE FAIL, Length: 0x0002
55E0:                A0             ;           ROUTINE 0xA0
55E1:                A1             ;           ROUTINE 0xA1
55E2:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
55E3:          15                   ;       ELSE go to: 0x55F9
55E4:             0D 13             ;         WHILE PASS, Length: 0x0013
55E6:                C0             ;           ROUTINE 0xC0
55E7:                0E 10          ;           WHILE FAIL, Length: 0x0010
55E9:                   AE          ;             ROUTINE 0xAE
55EA:                   14          ;             EXECUTE AND REVERSE STATUS
55EB:                   0B 0B 03    ;             SWITCH, Length: 0x000B, Function to call: 0x03
55EE:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
55EF:                      3E       ;               ELSE go to: 0x562E
55F0:                         02 00 8F ;                 IS OWNED BY, A=0x8F, obj=??00??
55F3:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
55F4:                      3E       ;               ELSE go to: 0x5633
55F5:                         02 00 91 ;                 IS OWNED BY, A=0x91, obj=??00??
55F8:                   9E          ;             ROUTINE 0x9E

55F9: 91 26 00                      ; room=91_8_??91??, Length: 0x0026, Data: 0x00
;
55FC:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
55FE:       9C                      ;     ROUTINE 0x9C
;
55FF:    04 20                      ;   Section COMMANDS, Length: 0x0020
5601:       0B 1E 0A                ;     SWITCH, Length: 0x001E, Function to call: 0x0A
5604:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
5605:          04                   ;       ELSE go to: 0x560A
5606:             0E 02             ;         WHILE FAIL, Length: 0x0002
5608:                A0             ;           ROUTINE 0xA0
5609:                A1             ;           ROUTINE 0xA1
560A:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
560B:          15                   ;       ELSE go to: 0x5621
560C:             0D 13             ;         WHILE PASS, Length: 0x0013
560E:                C0             ;           ROUTINE 0xC0
560F:                0E 10          ;           WHILE FAIL, Length: 0x0010
5611:                   AE          ;             ROUTINE 0xAE
5612:                   14          ;             EXECUTE AND REVERSE STATUS
5613:                   0B 0B 03    ;             SWITCH, Length: 0x000B, Function to call: 0x03
5616:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
5617:                      3E       ;               ELSE go to: 0x5656
5618:                         02 00 90 ;                 IS OWNED BY, A=0x90, obj=??00??
561B:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
561C:                      3E       ;               ELSE go to: 0x565B
561D:                         02 00 92 ;                 IS OWNED BY, A=0x92, obj=??00??
5620:                   9E          ;             ROUTINE 0x9E

5621: 92 81 2E 00                   ; room=92_8_MOTOVATOM_ENGINES, Length: 0x012E, Data: 0x00
;
5625:    03 80 AB                   ;   Section DESCRIPTION, Length: 0x00AB
5628:       0D 80 A8                ;     WHILE PASS, Length: 0x00A8
562B:          04 06                ;       PRINT, Length: 0x0006
562D:             C6 93 4B A1 7F BF ; 
;
;                 MOTOVATOM
;
5633:          0E 08                ;       WHILE FAIL, Length: 0x0008
5635:             C3                ;         ROUTINE 0xC3
5636:             04 05             ;         PRINT, Length: 0x0005
5638:                91 61 8F 7A 53 ; 
;
;                    ENGINES
;
563D:          8B                   ;       ROUTINE 0x8B
563E:          04 80 92             ;       PRINT, Length: 0x0092
5641:             C7 DE 94 14 4B 5E 83 96 3B 16 B7 B1 39 17 DB 9F ; 
5651:             56 D1 15 71 CF 62 CE B0 63 16 DB B9 5B CA 87 A5 ; 
5661:             B5 53 B8 16 63 16 23 54 74 98 DB E0 54 8B 9B 6C ; 
5671:             4E B8 74 CA AB 14 8B B3 40 55 65 98 16 BC EF 72 ; 
5681:             89 17 B6 6C F4 72 56 F4 F4 72 4B 5E C3 B5 4B 15 ; 
5691:             9E 7A B6 14 1B C4 C9 6D C7 CE 90 91 83 49 AB 98 ; 
56A1:             79 68 56 90 DB 72 85 91 90 73 6F 62 C0 16 82 17 ; 
56B1:             59 5E 46 48 AF 14 90 73 1B 58 3E A1 82 17 2F 62 ; 
56C1:             D5 15 7B 14 3E B9 7B 7B 7B B4 66 B1 BF 14 49 C0 ; 
56D1:             1B 9C             ; 
;
;                 YOU ARE IN A LARGE ROOM WITH SEVERAL MASSIVE PIECES OF
;                 MACHINERY. LARGE SILVER BARS CONNECT THEM TOGETHER. THERE
;                 IS A FAINT BLUE GLOW EMANATING FROM THE MACHINES. ON THE
;                 WALL BEHIND YOU, THERE IS A SOLITARY RED BUTTON.
;
;
56D3:    04 7D                      ;   Section COMMANDS, Length: 0x007D
56D5:       0E 7B                   ;     WHILE FAIL, Length: 0x007B
56D7:          0D 61                ;       WHILE PASS, Length: 0x0061
56D9:             0E 5E             ;         WHILE FAIL, Length: 0x005E
56DB:                0D 1A          ;           WHILE PASS, Length: 0x001A
56DD:                   03 01 84    ;             IS LOCATED, room=01_PLAYER, obj=??84??
56E0:                   04 11       ;             PRINT, Length: 0x0011
56E2:                      C6 B0 96 78 C0 7A 9B 15 CD B5 46 7A F3 5F C7 DE ; 
56F2:                      21       ; 
;
;                          RADIATION HAS KILLED YOU!
;
56F3:                   1C 01       ;             SET VAR OBJECT, obj=01_YOU
56F5:                   1D 4B       ;             ATTACK VAR, Points: 75
56F7:                0D 1E          ;           WHILE PASS, Length: 0x001E
56F9:                   03 01 83    ;             IS LOCATED, room=01_PLAYER, obj=??83??
56FC:                   04 12       ;             PRINT, Length: 0x0012
56FE:                      09 9A 51 18 54 C2 8E 5F FB 8E 67 66 03 8A DF D0 ; 
570E:                      AB 89    ; 
;
;                          NOW YOU REALLY FEEL AWFUL! 
;
5710:                   1C 01       ;             SET VAR OBJECT, obj=01_YOU
5712:                   1D 0A       ;             ATTACK VAR, Points: 10
5714:                   17 84 01    ;             MOVE TO, obj=??84??, room=01_PLAYER
5717:                0D 20          ;           WHILE PASS, Length: 0x0020
5719:                   04 17       ;             PRINT, Length: 0x0017
571B:                      C7 DE 94 14 48 5E 2E 60 91 7A 61 17 39 92 56 72 ; 
572B:                      8B 16 57 C6 35 A1 2E ; 
;
;                          YOU ARE FEELING SOMEWHAT NAUSEOUS.
;
5732:                   17 83 01    ;             MOVE TO, obj=??83??, room=01_PLAYER
5735:                   1C 01       ;             SET VAR OBJECT, obj=01_YOU
5737:                   1D 0A       ;             ATTACK VAR, Points: 10
5739:             0C                ;         FAIL
573A:          0B 16 0A             ;       SWITCH, Length: 0x0016, Function to call: 0x0A
573D:             12                ;         Phrase 0x12: "PULL     u.......   *           *"
573E:             01                ;         ELSE go to: 0x5740
573F:                A0             ;           ROUTINE 0xA0
5740:             36                ;         Phrase 0x36: "ENTER    *          *           *"
5741:             10                ;         ELSE go to: 0x5752
5742:                0D 0E          ;           WHILE PASS, Length: 0x000E
5744:                   C0          ;             ROUTINE 0xC0
5745:                   0E 0B       ;             WHILE FAIL, Length: 0x000B
5747:                      AE       ;               ROUTINE 0xAE
5748:                      14       ;               EXECUTE AND REVERSE STATUS
5749:                      0B 06 03 ;               SWITCH, Length: 0x0006, Function to call: 0x03
574C:                         40    ;                 Phrase 0x40: "CLOSE    ....A...   *           *"
574D:                         3E    ;                 ELSE go to: 0x578C
574E:                            02 00 91 ;                   IS OWNED BY, A=0x91, obj=??00??
5751:                      9E       ;               ROUTINE 0x9E

5752: 9A 2C 00                      ; room=9A_8_??9A??, Length: 0x002C, Data: 0x00
;
5755:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5757:       B0                      ;     ROUTINE 0xB0
;
5758:    04 26                      ;   Section COMMANDS, Length: 0x0026
575A:       0B 24 0A                ;     SWITCH, Length: 0x0024, Function to call: 0x0A
575D:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
575E:          05                   ;       ELSE go to: 0x5764
575F:             0E 03             ;         WHILE FAIL, Length: 0x0003
5761:                A0             ;           ROUTINE 0xA0
5762:                A1             ;           ROUTINE 0xA1
5763:                9F             ;           ROUTINE 0x9F
5764:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
5765:          1A                   ;       ELSE go to: 0x5780
5766:             0D 18             ;         WHILE PASS, Length: 0x0018
5768:                C0             ;           ROUTINE 0xC0
5769:                0E 15          ;           WHILE FAIL, Length: 0x0015
576B:                   AE          ;             ROUTINE 0xAE
576C:                   14          ;             EXECUTE AND REVERSE STATUS
576D:                   0B 10 03    ;             SWITCH, Length: 0x0010, Function to call: 0x03
5770:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
5771:                      3E       ;               ELSE go to: 0x57B0
5772:                         02 00 9B ;                 IS OWNED BY, A=0x9B, obj=??00??
5775:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
5776:                      3E       ;               ELSE go to: 0x57B5
5777:                         02 00 9C ;                 IS OWNED BY, A=0x9C, obj=??00??
577A:                      3F       ;               Phrase 0x3F: "SAVE     *          *           *"
577B:                      3E       ;               ELSE go to: 0x57BA
577C:                         02 00 8C ;                 IS OWNED BY, A=0x8C, obj=??00??
577F:                   9E          ;             ROUTINE 0x9E

5780: 9B 80 DA 00                   ; room=9B_8_PLASTOTRO_GUN, Length: 0x00DA, Data: 0x00
;
5784:    03 80 BC                   ;   Section DESCRIPTION, Length: 0x00BC
5787:       0D 80 B9                ;     WHILE PASS, Length: 0x00B9
578A:          04 06                ;       PRINT, Length: 0x0006
578C:             FB A5 09 BA F9 BF ; 
;
;                 PLASTOTRO
;
5792:          0E 05                ;       WHILE FAIL, Length: 0x0005
5794:             C3                ;         ROUTINE 0xC3
5795:             04 02             ;         PRINT, Length: 0x0002
5797:                30 6F          ; 
;
;                    GUN
;
5799:          8B                   ;       ROUTINE 0x8B
579A:          04 80 A6             ;       PRINT, Length: 0x00A6
579D:             C7 DE 94 14 4B 5E 83 96 5F 17 46 48 09 15 1B 92 ; 
57AD:             1B B8 E6 A4 39 17 FF 9F D0 15 82 17 45 5E 9E 61 ; 
57BD:             23 62 C3 9E 5F BE 39 17 DB 9F 4B 7B 4E 45 31 49 ; 
57CD:             B3 63 0C BA 91 48 53 61 4B 15 CE 92 94 78 63 16 ; 
57DD:             23 54 5B 98 56 D1 15 71 CF 62 CE B0 5B 17 8F 8E ; 
57ED:             84 AF 3D 49 EC 16 6F 9F 03 56 AB 98 79 68 4B 90 ; 
57FD:             73 C1 9E 7A D6 9C DB 72 0E D0 2F 8E 7B 14 34 56 ; 
580D:             44 B9 47 DB 4F D6 8B 7A 91 BE 91 96 96 64 DB 72 ; 
581D:             01 B3 54 90 CF 62 4D 48 7B 14 3E B9 7B 7B 7B B4 ; 
582D:             8F 4E 44 5E 8E C6 03 A0 03 A0 0F A0 B8 16 82 17 ; 
583D:             59 5E 46 48 5B BB ; 
;
;                 YOU ARE IN A SMALL DOME SHAPED ROOM. IN THE CENTER OF THE
;                 ROOM IS A LARGE, STRANGELY FAMILIAR MACHINE WITH SEVERAL
;                 SILVER BARS PROJECTING FROM IT, INTO THE WALLS. A CURSORY
;                 EXAMINATION OF THE ROOM REVEALS A SOLITARY BLUE BUTTON ON
;                 ONE OF THE WALLS.
;
;
5843:    04 18                      ;   Section COMMANDS, Length: 0x0018
5845:       0B 16 0A                ;     SWITCH, Length: 0x0016, Function to call: 0x0A
5848:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
5849:          01                   ;       ELSE go to: 0x584B
584A:             A1                ;         ROUTINE 0xA1
584B:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
584C:          10                   ;       ELSE go to: 0x585D
584D:             0D 0E             ;         WHILE PASS, Length: 0x000E
584F:                C0             ;           ROUTINE 0xC0
5850:                0E 0B          ;           WHILE FAIL, Length: 0x000B
5852:                   AE          ;             ROUTINE 0xAE
5853:                   14          ;             EXECUTE AND REVERSE STATUS
5854:                   0B 06 03    ;             SWITCH, Length: 0x0006, Function to call: 0x03
5857:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
5858:                      3E       ;               ELSE go to: 0x5897
5859:                         02 00 9A ;                 IS OWNED BY, A=0x9A, obj=??00??
585C:                   9E          ;             ROUTINE 0x9E

585D: 9C 80 E5 00                   ; room=9C_8_ARMSMITAN_WEAPONRY, Length: 0x00E5, Data: 0x00
;
5861:    03 80 BF                   ;   Section DESCRIPTION, Length: 0x00BF
5864:       0D 80 BC                ;     WHILE PASS, Length: 0x00BC
5867:          04 06                ;       PRINT, Length: 0x0006
5869:             37 49 EB B8 50 BD ; 
;
;                 ARMSMITAN
;
586F:          0E 09                ;       WHILE FAIL, Length: 0x0009
5871:             C3                ;         ROUTINE 0xC3
5872:             04 06             ;         PRINT, Length: 0x0006
5874:                A3 D0 80 A6 7B B4 ; 
;
;                    WEAPONRY 
;
587A:          8B                   ;       ROUTINE 0x8B
587B:          04 80 A5             ;       PRINT, Length: 0x00A5
587E:             C7 DE 94 14 55 5E 50 BD 90 5A CB 6A 83 96 3B 16 ; 
588E:             B7 B1 39 17 FE 9F D0 15 82 17 45 5E 9E 61 23 62 ; 
589E:             C3 9E 23 D1 13 54 4B 7B 45 45 1D A0 BF 9F 90 14 ; 
58AE:             05 58 4B 72 1B B5 0D A0 43 5E 0B 6C 9B 96 1B A1 ; 
58BE:             95 5A 48 55 23 62 5F BE 99 16 C8 CE 6B 48 83 8C ; 
58CE:             96 AF 3F 61 84 A6 4E BD BF 14 49 C0 8B 9A 03 A0 ; 
58DE:             5F BE F3 17 17 8D C0 16 4B 5E D4 B5 F3 5F 8E 48 ; 
58EE:             82 17 51 5E 5F BE 8B AF C4 B5 67 8E 48 F4 DB 46 ; 
58FE:             AB 98 5F BE DA 14 D4 47 90 14 16 58 DB 72 40 55 ; 
590E:             3E B9 4B 5E C3 B5 3B 16 B7 B1 D3 17 FB 62 AB 98 ; 
591E:             64 B7 30 60 2E    ; 
;
;                 YOU ARE STANDING IN A LARGE ROOM, IN THE CENTER OF WHICH IS
;                 A CONSOLE AND CHAIR. ONCE AGAIN YOU DISCOVER THE NOW
;                 FAMILIAR TELEPORTAL BUTTONS ON THE WALL. ONE IS RED AND THE
;                 OTHER IS BLUE. FACING THE CHAIR AND THE CONSOLE IS A LARGE
;                 VIEWING SCREEN.
;
;
5923:    04 20                      ;   Section COMMANDS, Length: 0x0020
5925:       0B 1E 0A                ;     SWITCH, Length: 0x001E, Function to call: 0x0A
5928:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
5929:          04                   ;       ELSE go to: 0x592E
592A:             0E 02             ;         WHILE FAIL, Length: 0x0002
592C:                A0             ;           ROUTINE 0xA0
592D:                A1             ;           ROUTINE 0xA1
592E:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
592F:          15                   ;       ELSE go to: 0x5945
5930:             0D 13             ;         WHILE PASS, Length: 0x0013
5932:                C0             ;           ROUTINE 0xC0
5933:                0E 10          ;           WHILE FAIL, Length: 0x0010
5935:                   AE          ;             ROUTINE 0xAE
5936:                   14          ;             EXECUTE AND REVERSE STATUS
5937:                   0B 0B 03    ;             SWITCH, Length: 0x000B, Function to call: 0x03
593A:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
593B:                      3E       ;               ELSE go to: 0x597A
593C:                         02 00 9A ;                 IS OWNED BY, A=0x9A, obj=??00??
593F:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
5940:                      3E       ;               ELSE go to: 0x597F
5941:                         02 00 9D ;                 IS OWNED BY, A=0x9D, obj=??00??
5944:                   9E          ;             ROUTINE 0x9E

5945: 9D 26 00                      ; room=9D_8_??9D??, Length: 0x0026, Data: 0x00
;
5948:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
594A:       9C                      ;     ROUTINE 0x9C
;
594B:    04 20                      ;   Section COMMANDS, Length: 0x0020
594D:       0B 1E 0A                ;     SWITCH, Length: 0x001E, Function to call: 0x0A
5950:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
5951:          04                   ;       ELSE go to: 0x5956
5952:             0E 02             ;         WHILE FAIL, Length: 0x0002
5954:                A0             ;           ROUTINE 0xA0
5955:                A1             ;           ROUTINE 0xA1
5956:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
5957:          15                   ;       ELSE go to: 0x596D
5958:             0D 13             ;         WHILE PASS, Length: 0x0013
595A:                C0             ;           ROUTINE 0xC0
595B:                0E 10          ;           WHILE FAIL, Length: 0x0010
595D:                   AE          ;             ROUTINE 0xAE
595E:                   14          ;             EXECUTE AND REVERSE STATUS
595F:                   0B 0B 03    ;             SWITCH, Length: 0x000B, Function to call: 0x03
5962:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
5963:                      3E       ;               ELSE go to: 0x59A2
5964:                         02 00 9C ;                 IS OWNED BY, A=0x9C, obj=??00??
5967:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
5968:                      3E       ;               ELSE go to: 0x59A7
5969:                         02 00 9E ;                 IS OWNED BY, A=0x9E, obj=??00??
596C:                   9E          ;             ROUTINE 0x9E

596D: 9E 1E 00                      ; room=9E_8_??9E??, Length: 0x001E, Data: 0x00
;
5970:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5972:       9D                      ;     ROUTINE 0x9D
;
5973:    04 18                      ;   Section COMMANDS, Length: 0x0018
5975:       0B 16 0A                ;     SWITCH, Length: 0x0016, Function to call: 0x0A
5978:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
5979:          01                   ;       ELSE go to: 0x597B
597A:             9F                ;         ROUTINE 0x9F
597B:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
597C:          10                   ;       ELSE go to: 0x598D
597D:             0D 0E             ;         WHILE PASS, Length: 0x000E
597F:                C0             ;           ROUTINE 0xC0
5980:                0E 0B          ;           WHILE FAIL, Length: 0x000B
5982:                   AE          ;             ROUTINE 0xAE
5983:                   14          ;             EXECUTE AND REVERSE STATUS
5984:                   0B 06 03    ;             SWITCH, Length: 0x0006, Function to call: 0x03
5987:                      3F       ;               Phrase 0x3F: "SAVE     *          *           *"
5988:                      3E       ;               ELSE go to: 0x59C7
5989:                         02 00 9D ;                 IS OWNED BY, A=0x9D, obj=??00??
598C:                   9E          ;             ROUTINE 0x9E
```

```code
598D: D0 15 82 17 46 5E 57 62 B3 B3 47 B9 53 BE C3 9E ; ....F^Wb..G.S...
599D: 5F BE 89 17 27 D2 04 22 0B 20 0A 01 02 00 9B 02 ; _...'..". ......
59AD: 06 0D 04 30 B3 2F 03 03 09 0D 07 30 E2 17 9D 01 ; ...0./.....0....
59BD: 2F 05 04 06 0D 04 30 B1 2F 03 B4 80 BB 00 03 80 ; /.....0./.......
59CD: 9B 04 80 98 89 73 B3 75 47 DB 66 49 5B F4 1B A1 ; .....s.uG.fI[...
59DD: 2F 49 C0 16 82 17 4A 5E 7A 79 1B D0 56 F4 D6 9C ; /I....J^zy..V...
59ED: DB 72 B5 D0 0B BC 96 96 DB 72 95 5A 50 BD 9B 53 ; .r.......r.ZP..S
59FD: C7 DE 57 17 59 5E 56 72 92 14 E3 A4 8B B3 6B BF ; ..W.Y^Vr......k.
5A0D: 5B 4D 55 45 8E 91 16 8A 80 A1 56 F4 D6 9C DB 72 ; [MUE......V....r
5A1D: 04 9A 53 BE 8E 48 61 17 82 C6 82 17 4F 5E 19 A0 ; ..S..Ha.....O^..
5A2D: 80 BF 35 A1 FF 14 B4 B7 15 BC 3C C6 30 A1 0B 5C ; ..5.......<.0..\
5A3D: C7 DE 56 F4 DB 72 89 73 B3 75 4E DB 3D A0 CE B5 ; ..V..r.s.uN.=...
5A4D: 17 7A 7B 14 7B 4E 8B 54 04 B2 00 4F 66 17 76 B1 ; .z{.{N.T...Of.v.
5A5D: 23 54 AB 98 6B BF 5F BE 23 15 17 BA 04 1A 0B 18 ; #T..k._.#.......
5A6D: 0A 03 09 0D 07 30 F0 17 9D 01 2F 05 01 02 00 B9 ; .....0..../.....
5A7D: 02 02 00 B5 04 02 00 9C B5 6F 00 03 49 04 47 47 ; .........o..I.GG
5A8D: B9 53 BE C3 9E 89 73 B3 75 DB E0 C7 DE 94 14 55 ; .S....s.u......U
5A9D: 5E 36 A1 11 71 96 64 DB 72 89 73 B3 75 DB E0 83 ; ^6..q.d.r.s.u...
5AAD: 7A 5F BE 03 15 FB B9 17 98 89 17 82 17 59 5E 66 ; z_...........Y^f
5ABD: 62 51 18 45 C2 83 48 A7 B7 57 17 74 CA 33 48 EB ; bQ.E..H..W.t.3H.
5ACD: 4F C3 8B C5 98 2E 04 21 0B 1F 0A 01 02 00 B4 02 ; O......!........
5ADD: 09 0D 07 30 E2 17 9D 01 2F 05 03 09 0D 07 30 F0 ; ...0..../.....0.
5AED: 17 9D 01 2F 05 04 02 00 9D B9 75 00 03 4F 04 4D ; .../......u..O.M
5AFD: 04 9A 53 BE C3 9E 89 73 B3 75 DB E0 C7 DE 94 14 ; ..S....s.u......
5B0D: 4B 5E 96 96 DB 72 F5 59 3E 62 99 16 C2 B3 B8 16 ; K^...r.Y>b......
5B1D: 82 17 4A 5E 7A 79 1B D0 4B F4 96 96 DB 72 95 5A ; ..J^zy..K....r.Z
5B2D: 50 BD 9B 53 6B BF 5F BE F7 17 F3 B9 C7 DE D3 14 ; P..Sk._.........
5B3D: 95 96 1B 60 55 45 8E 91 16 8A 80 A1 2E 04 21 0B ; ....UE........!.
5B4D: 1F 0A 01 09 0D 07 30 F1 17 9D 01 2F 05 02 02 00 ; ......0..../....
5B5D: B4 03 09 0D 07 30 F0 17 9D 01 2F 05 04 02 00 AC ; .....0..../.....
5B6D: DD 44 00 03 20 04 1E 4E 72 B3 8E DB E0 C7 DE 94 ; .D.. ..Nr.......
5B7D: 14 4B 5E 83 96 5A 17 BE A0 10 EE 3C 49 6B A1 4E ; .K^..Z.....<Ik.N
5B8D: 72 B3 8E DB E0 04 1F 0B 1D 0A 01 08 0E 06 14 1C ; r...............
5B9D: 16 8D 00 DE 02 08 0E 06 14 1C 18 8D 00 DF 04 02 ; ................
5BAD: 00 AA 55 02 00 AA DE 4E 00 03 3C 04 3A 04 9A 53 ; ..U....N..<.:..S
5BBD: BE 01 B3 DB 95 C7 DE 94 14 4B 5E 83 96 5F 17 46 ; .........K^.._.F
5BCD: 48 39 17 FF 9F 82 17 2F 62 D5 15 7B 14 66 4D 03 ; H9...../b..{.fM.
5BDD: EE DA 14 D4 47 03 EE 33 98 55 45 8E 91 06 8A 75 ; ....G..3.UE....u
5BED: B1 B4 B7 9F 15 7F B1 04 0D 0B 0B 0A 02 08 0E 06 ; ................
5BFD: 14 1C 17 8D 00 DD DF 4E 00 03 3C 04 3A 47 B9 53 ; .......N..<.:G.S
5C0D: BE 01 B3 DB 95 C7 DE 94 14 4B 5E 83 96 5F 17 46 ; .........K^.._.F
5C1D: 48 39 17 FF 9F 82 17 2F 62 D5 15 7B 14 66 4D 03 ; H9...../b..{.fM.
5C2D: EE DA 14 D4 47 03 EE 33 98 55 45 8E 91 06 8A 75 ; ....G..3.UE....u
5C3D: B1 B4 B7 9F 15 7F B1 04 0D 0B 0B 0A 01 08 0E 06 ; ................
5C4D: 14 1C 19 8D 00 DD 4C 41 52 47 45 0E 05 53 4D 41 ; ......LARGE..SMA
5C5D: 4C 4C 0F 06 4C 49 54 54 4C 45 0F 03 54 4F 50 28 ; LL..LITTLE..TOP(
5C6D: 06 4D 49 44 44 4C 45 3C 06 42 4F 54 54 4F 4D 3E ; .MIDDLE<.BOTTOM>
5C7D: 04 46 4C 41 54 22 05 53 50 41 52 45 23 04 42 4C ; .FLAT".SPARE#.BL
5C8D: 55 45 0D 06 4D 41 53 53 49 56 3F 04 42 41 4E 4B ; UE..MASSIV?.BANK
5C9D: 40 06 53 41 4C 4F 4F 4E 41 06 53 48 45 52 49 46 ; @.SALOONA.SHERIF
5CAD: 42 06 4F 46 46 49 43 45 42 06 53 4C 49 4D 27 53 ; B.OFFICEB.SLIM'S
5CBD: 43 05 53 4C 49 4D 53 43 05 42 4F 42 27 53 44 04 ; C.SLIMSC.BOB'SD.
5CCD: 42 4F 42 53 44 06 44 4F 55 42 4C 45 45 05 48 4F ; BOBSD.DOUBLEE.HO
5CDD: 54 45 4C 47 06 53 57 49 4E 47 49 46 04 54 53 4F ; TELG.SWINGIF.TSO
5CED: 4D 6B 04 43 4F 4F 4C 72 05 43 4C 45 41 52 74 05 ; Mk.COOLr.CLEARt.
5CFD: 42 52 4F 57 
```

