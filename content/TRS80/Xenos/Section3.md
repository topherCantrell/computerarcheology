![Xenos](Xenos.png)

# Xenos SECTION3.DAT

>>> cpu Z80

>>> binary 5200:roms/section3.bin

```code
5200: 00 89 FB                      ; List ID: 0x00, Length: 0x09FB

5203: 90 80 8C 00                   ; Room Number: 0x90, Length: 0x008C, Data: 0x00
;
5207:    03 6C                      ;   Section DESCRIPTION, Length: 0x006C
5209:       04 6A                   ;     PRINT, Length: 0x006A
;
; WEST ALLEY INTERSECTION. YOU ARE STANDING AT THE INTERSECTION OF MAIN STREET AND AN ALLEY AT THE WEST END OF TOWN. TO THE SOUTH THE ALLEY LEADS TO THE DESERT. 
;
520B:          B5 D0 03 BC FF 8C 4B DB BF 9A 97 B3 03 56 27 A0 ; 
521B:          51 18 43 C2 5B B1 FB B9 43 98 AB 98 73 49 5F BE ; 
522B:          D0 15 F4 BD A5 B7 91 BE 91 96 8F 64 D0 47 66 17 ; 
523B:          67 B1 03 BC 33 98 83 48 46 48 3B 63 73 49 5F BE ; 
524B:          F7 17 F3 B9 8E 61 B8 16 89 17 27 D2 89 17 82 17 ; 
525B:          55 5E 36 A1 16 71 DB 72 46 48 3B 63 E3 8B 0B 5C ; 
526B:          6B BF 5F BE FF 14 B4 B7 9B C1 ; 
;
5275:    04 1B                      ;   Section COMMANDS, Length: 0x001B
5277:       0B 19 0A                ;     SWITCH, Length: 0x0019, Function to call: 0x0A
527A:          02                   ;       Phrase number: 0x02
527B:          02                   ;       ELSE go to: 0x527E
527C:             00 91             ;         MOVE AND LOOK, Destination room: 0x91
527E:          01                   ;       Phrase number: 0x01
527F:          06                   ;       ELSE go to: 0x5286
5280:             0D 04             ;         WHILE PASS, Length: 0x0004
5282:                30 A4          ;           UNKNOWN1, Data: 0xA4
5284:                2F 02          ;           UNKNOWN2 Data: 0x02
5286:          03                   ;       Phrase number: 0x03
5287:          02                   ;       ELSE go to: 0x528A
5288:             00 93             ;         MOVE AND LOOK, Destination room: 0x93
528A:          04                   ;       Phrase number: 0x04
528B:          06                   ;       ELSE go to: 0x5292
528C:             0D 04             ;         WHILE PASS, Length: 0x0004
528E:                30 8D          ;           UNKNOWN1, Data: 0x8D
5290:                2F 02          ;           UNKNOWN2 Data: 0x02

5292: 91 4E 00                      ; Room Number: 0x91, Length: 0x004E, Data: 0x00
;
5295:    03 3A                      ;   Section DESCRIPTION, Length: 0x003A
5297:       04 38                   ;     PRINT, Length: 0x0038
;
; WEST ALLEY SOUTH. YOU ARE IN THE ALLEY BETWEEN THE SHERIFF'S OFFICE AND THE GROCERY.
;
5299:          B5 D0 03 BC FF 8C 55 DB 36 A1 9B 76 C7 DE 94 14 ; 
52A9:          4B 5E 96 96 DB 72 46 48 3B 63 76 4D A7 D0 96 96 ; 
52B9:          DB 72 1F B8 08 B2 E5 64 B8 16 05 67 43 5E 33 98 ; 
52C9:          5F BE 84 15 57 9E 9F B4 ; 
;
52D1:    04 0F                      ;   Section COMMANDS, Length: 0x000F
52D3:       0B 0D 0A                ;     SWITCH, Length: 0x000D, Function to call: 0x0A
52D6:          01                   ;       Phrase number: 0x01
52D7:          02                   ;       ELSE go to: 0x52DA
52D8:             00 90             ;         MOVE AND LOOK, Destination room: 0x90
52DA:          02                   ;       Phrase number: 0x02
52DB:          06                   ;       ELSE go to: 0x52E2
52DC:             0D 04             ;         WHILE PASS, Length: 0x0004
52DE:                30 92          ;           UNKNOWN1, Data: 0x92
52E0:                2F 02          ;           UNKNOWN2 Data: 0x02

52E2: 93 81 1B 00                   ; Room Number: 0x93, Length: 0x011B, Data: 0x00
;
52E6:    03 80 F6                   ;   Section DESCRIPTION, Length: 0x00F6
52E9:       04 80 F3                ;     PRINT, Length: 0x00F3
;
; TOWN CENTER. YOU ARE NOW STANDING IN THE CENTER OF TOWN. TO THE NORTH IS "BOB'S HARDWARE." TO THE SOUTH IS "SLIM'S GROCERIES." TO THE EAST IS THE HOTEL. OPPOSING IT ON THE SOUTH SIDE OF THE STREET IS "THE FIRST BANK OF PURGATORY." TO THE WEST BESIDE "BOB'S HARDWARE" IS "HARVEY'S BAR AND GRILL," OPPOSING IT ON THE SOUTH SIDE OF THE STREET IS THE SHERIFF'S OFFICE.
;
52EC:          89 BF 85 96 9E 61 47 62 51 18 43 C2 5B B1 09 9A ; 
52FC:          66 17 8E 48 91 7A D0 15 82 17 45 5E 9E 61 23 62 ; 
530C:          C3 9E 89 BF 1B 9C 6B BF 5F BE 99 16 C2 B3 D5 15 ; 
531C:          6C 13 25 9E CA B5 2E 49 14 D0 DC 63 89 17 82 17 ; 
532C:          55 5E 36 A1 0B 71 BC B5 C3 B8 A5 90 84 15 57 9E ; 
533C:          07 B2 5C BB 89 17 82 17 47 5E 66 49 D5 15 82 17 ; 
534C:          4A 5E FF A0 9B 8F 6A A0 DB A0 AB 98 73 7B 03 A0 ; 
535C:          5F BE 61 17 82 C6 5B 17 DB 59 C3 9E 5F BE 66 17 ; 
536C:          67 B1 0B BC BC B5 5F BE 53 15 A6 B3 AB 14 4B 99 ; 
537C:          C3 9E 74 A7 16 6C C3 A0 63 F4 6B BF 5F BE F7 17 ; 
538C:          F3 B9 75 4D FF 78 6C 13 25 9E CA B5 2E 49 14 D0 ; 
539C:          63 5E 4B 7B DB 1B 0F B4 A5 DB AB 14 83 AF 33 98 ; 
53AC:          B3 6E 16 8D 91 19 A9 A6 50 B8 CB 6A 11 BC 96 96 ; 
53BC:          DB 72 47 B9 53 BE 46 B8 51 5E 96 64 DB 72 0C BA ; 
53CC:          36 60 D5 15 82 17 55 5E F4 72 50 79 CB 23 D0 9E ; 
53DC:          D7 78 2E             ; 
;
53DF:    04 1F                      ;   Section COMMANDS, Length: 0x001F
53E1:       0B 1D 0A                ;     SWITCH, Length: 0x001D, Function to call: 0x0A
53E4:          01                   ;       Phrase number: 0x01
53E5:          08                   ;       ELSE go to: 0x53EE
53E6:             0E 06             ;         WHILE FAIL, Length: 0x0006
53E8:                14             ;           EXECUTE AND REVERSE STATUS
53E9:                1C 0C          ;           SET VAR OBJECT, Object number: 0x0C
53EB:                8D             ;           COMMAND 0x8D
53EC:                00 A6          ;           MOVE AND LOOK, Destination room: 0xA6
53EE:          02                   ;       Phrase number: 0x02
53EF:          08                   ;       ELSE go to: 0x53F8
53F0:             0E 06             ;         WHILE FAIL, Length: 0x0006
53F2:                14             ;           EXECUTE AND REVERSE STATUS
53F3:                1C 0B          ;           SET VAR OBJECT, Object number: 0x0B
53F5:                8D             ;           COMMAND 0x8D
53F6:                00 94          ;           MOVE AND LOOK, Destination room: 0x94
53F8:          03                   ;       Phrase number: 0x03
53F9:          02                   ;       ELSE go to: 0x53FC
53FA:             00 96             ;         MOVE AND LOOK, Destination room: 0x96
53FC:          04                   ;       Phrase number: 0x04
53FD:          02                   ;       ELSE go to: 0x5400
53FE:             00 90             ;         MOVE AND LOOK, Destination room: 0x90

5400: 94 4E 00                      ; Room Number: 0x94, Length: 0x004E, Data: 0x00
;
5403:    03 3C                      ;   Section DESCRIPTION, Length: 0x003C
5405:       04 3A                   ;     PRINT, Length: 0x003A
;
; SLIM'S GROCERY. YOU ARE IN THE GROCERY STORE. THE STORE APPEARS TO HAVE BEEN RANSACKED.
;
5407:          C3 B8 A5 90 84 15 57 9E 9F B4 51 18 43 C2 5B B1 ; 
5417:          83 7A 5F BE 84 15 57 9E 7B B4 09 BA 7F B1 82 17 ; 
5427:          55 5E 84 BF 43 5E 9F A6 3D 49 89 17 9B 15 5B CA ; 
5437:          67 4D 94 96 9D 48 DD 46 17 60 ; 
;
5441:    04 0D                      ;   Section COMMANDS, Length: 0x000D
5443:       0B 0B 0A                ;     SWITCH, Length: 0x000B, Function to call: 0x0A
5446:          01                   ;       Phrase number: 0x01
5447:          08                   ;       ELSE go to: 0x5450
5448:             0E 06             ;         WHILE FAIL, Length: 0x0006
544A:                14             ;           EXECUTE AND REVERSE STATUS
544B:                1C 0D          ;           SET VAR OBJECT, Object number: 0x0D
544D:                8D             ;           COMMAND 0x8D
544E:                00 93          ;           MOVE AND LOOK, Destination room: 0x93

5450: 95 80 E8 00                   ; Room Number: 0x95, Length: 0x00E8, Data: 0x00
;
5454:    03 80 CF                   ;   Section DESCRIPTION, Length: 0x00CF
5457:       04 80 CC                ;     PRINT, Length: 0x00CC
;
; SOUTH OF SLIM'S. YOU ARE NOW SOUTH OF THE GROCERY STORE. TO THE WEST YOU CAN SEE THE BACK OF AN ADOBE BUILDING WITH BARS IN THE WINDOWS. TO THE EAST YOU CAN SEE THE SOUTH WALL OF A BRICK BUILDING. THERE ARE ALLEYS IMMEDIATELY EAST AND WEST OF THE GROCERY STORE. THE DESERT STRETCHES ENDLESSLY TO THE SOUTH.
;
545A:          47 B9 53 BE C3 9E C3 B8 A5 90 5B F4 1B A1 2F 49 ; 
546A:          99 16 D5 CE 36 A1 11 71 96 64 DB 72 B9 6E B4 53 ; 
547A:          55 DB 84 BF DB 63 6B BF 5F BE F7 17 F3 B9 C7 DE ; 
548A:          D3 14 95 96 1B 60 5F BE AB 14 8B 54 C3 9E 83 48 ; 
549A:          09 47 5B 4D EB 4F C3 8B AB 98 56 D1 04 71 3D 49 ; 
54AA:          D0 15 82 17 59 5E 8E 7A 85 A1 56 F4 D6 9C DB 72 ; 
54BA:          95 5F 1B BC 1B A1 10 53 57 17 56 5E DB 72 47 B9 ; 
54CA:          53 BE 0E D0 11 8A 83 64 BC 14 DD 78 BF 14 3E 7A ; 
54DA:          91 7A 56 F4 F4 72 43 5E 5B B1 46 48 55 63 CF 15 ; 
54EA:          26 92 96 78 53 61 23 15 F3 B9 8E 48 F7 17 F3 B9 ; 
54FA:          C3 9E 5F BE 84 15 57 9E 7B B4 09 BA 7F B1 82 17 ; 
550A:          46 5E 57 62 B3 B3 0C BA 7D 62 F5 72 30 15 FF 5A ; 
551A:          DE B9 56 DB D6 9C DB 72 47 B9 77 BE ; 
;
5526:    04 13                      ;   Section COMMANDS, Length: 0x0013
5528:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
552B:          03                   ;       Phrase number: 0x03
552C:          02                   ;       ELSE go to: 0x552F
552D:             00 98             ;         MOVE AND LOOK, Destination room: 0x98
552F:          04                   ;       Phrase number: 0x04
5530:          06                   ;       ELSE go to: 0x5537
5531:             0D 04             ;         WHILE PASS, Length: 0x0004
5533:                30 92          ;           UNKNOWN1, Data: 0x92
5535:                2F 02          ;           UNKNOWN2 Data: 0x02
5537:          02                   ;       Phrase number: 0x02
5538:          02                   ;       ELSE go to: 0x553B
5539:             00 B1             ;         MOVE AND LOOK, Destination room: 0xB1

553B: 96 81 98 00                   ; Room Number: 0x96, Length: 0x0198, Data: 0x00
;
553F:    03 81 7B                   ;   Section DESCRIPTION, Length: 0x017B
5542:       04 81 78                ;     PRINT, Length: 0x0178
;
; EAST ALLEY INTERSECTION. YOU NOW STAND AT THE INTERSECTION OF MAIN STREET AND THE ALLEY AT THE EAST SIDE OF TOWN. A HOTEL SITS TO YOUR EAST, ON THE NORTH SIDE OF THE STREET. OPPOSITE IT, ON THE SOUTH SIDE OF THE STREET IS A BRICK BUILDING THAT SERVES AS THE TOWN'S BANK. TO THE WEST YOU CAN SEE THE SOUTH SIDE OF A HARDWARE STORE. BESIDE THE HARDWARE STORE, FURTHER DOWN THE STREET, IS A LARGE WOODEN BUILDING WITH A NEON SIGN ON THE FRONT. TO THE WEST, ON THE SOUTH SIDE OF THE STREET, THERE IS SLIM'S GROCERY. FURTHER DOWN THE STREET THERE IS AN ADOBE BUILDING. 
;
5545:          95 5F 03 BC FF 8C 4B DB BF 9A 97 B3 03 56 27 A0 ; 
5555:          51 18 50 C2 6B A1 FB B9 33 98 73 49 5F BE D0 15 ; 
5565:          F4 BD A5 B7 91 BE 91 96 8F 64 D0 47 66 17 67 B1 ; 
5575:          03 BC 33 98 5F BE 8E 14 FB 8B 96 14 82 17 47 5E ; 
5585:          66 49 5B 17 DB 59 C3 9E 89 BF 1B 9C 4A 45 FF A0 ; 
5595:          15 8A 8D 7B 89 17 51 18 23 C6 95 5F 73 C1 03 A0 ; 
55A5:          5F BE 99 16 C2 B3 5B 17 DB 59 C3 9E 5F BE 66 17 ; 
55B5:          67 B1 9B C1 6A A0 DB A0 DB BD 96 7B C0 16 82 17 ; 
55C5:          55 5E 36 A1 15 71 FF 78 B8 16 82 17 55 5E EF BF ; 
55D5:          73 62 4B 7B 44 45 05 B2 C4 83 CE C4 90 5A D6 6A ; 
55E5:          56 72 57 17 0F B4 C3 B5 D6 B5 DB 72 89 BF E5 96 ; 
55F5:          AB 14 6F 99 89 17 82 17 59 5E 66 62 51 18 45 C2 ; 
5605:          83 48 A7 B7 82 17 55 5E 36 A1 15 71 FF 78 B8 16 ; 
5615:          7B 14 54 72 B3 5C 5B B1 09 BA 7F B1 AF 14 46 B8 ; 
5625:          56 5E DB 72 54 72 B3 5C 5B B1 09 BA 7E B1 5F 15 ; 
5635:          C2 B3 23 62 89 5B 96 96 DB 72 0C BA 36 60 0B EE ; 
5645:          C3 B5 3B 16 B7 B1 01 18 7F 9E 84 96 CE C4 90 5A ; 
5655:          D9 6A 82 7B 7B 14 71 98 95 96 80 79 C0 16 82 17 ; 
5665:          48 5E 00 B3 9B C1 6B BF 5F BE F7 17 16 BA C0 16 ; 
5675:          82 17 55 5E 36 A1 15 71 FF 78 B8 16 82 17 55 5E ; 
5685:          EF BF 96 62 82 17 2F 62 D5 15 5E 17 5D 7A C9 B5 ; 
5695:          F5 B2 43 62 48 F4 3E C6 F4 72 09 15 03 D2 5F BE ; 
56A5:          66 17 67 B1 16 BC F4 72 4B 5E C3 B5 83 96 74 5B ; 
56B5:          44 5E CE C4 90 5A 5B 70 ; 
;
56BD:    04 17                      ;   Section COMMANDS, Length: 0x0017
56BF:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: 0x0A
56C2:          02                   ;       Phrase number: 0x02
56C3:          02                   ;       ELSE go to: 0x56C6
56C4:             00 97             ;         MOVE AND LOOK, Destination room: 0x97
56C6:          01                   ;       Phrase number: 0x01
56C7:          02                   ;       ELSE go to: 0x56CA
56C8:             00 A8             ;         MOVE AND LOOK, Destination room: 0xA8
56CA:          04                   ;       Phrase number: 0x04
56CB:          02                   ;       ELSE go to: 0x56CE
56CC:             00 93             ;         MOVE AND LOOK, Destination room: 0x93
56CE:          03                   ;       Phrase number: 0x03
56CF:          06                   ;       ELSE go to: 0x56D6
56D0:             0D 04             ;         WHILE PASS, Length: 0x0004
56D2:                30 99          ;           UNKNOWN1, Data: 0x99
56D4:                2F 04          ;           UNKNOWN2 Data: 0x04

56D6: 97 7F 00                      ; Room Number: 0x97, Length: 0x007F, Data: 0x00
;
56D9:    03 6F                      ;   Section DESCRIPTION, Length: 0x006F
56DB:       04 6D                   ;     PRINT, Length: 0x006D
;
; EAST ALLEY SOUTH. YOU ARE STANDING IN THE ALLEY BETWEEN THE GROCERY AND THE BANK. TO THE NORTH YOU CAN SEE MAIN STREET. TO THE SOUTH THE ALLEY OPENS TO THE DESERT.
;
56DD:          95 5F 03 BC FF 8C 55 DB 36 A1 9B 76 C7 DE 94 14 ; 
56ED:          55 5E 50 BD 90 5A CB 6A 96 96 DB 72 46 48 3B 63 ; 
56FD:          76 4D A7 D0 96 96 DB 72 B9 6E B4 53 43 DB 33 98 ; 
570D:          5F BE AB 14 6F 99 89 17 82 17 50 5E BE A0 1B 71 ; 
571D:          1B A1 10 53 57 17 4F 5E D0 47 66 17 67 B1 9B C1 ; 
572D:          6B BF 5F BE 61 17 82 C6 82 17 43 5E FF 8C 51 DB ; 
573D:          F0 A4 D6 B5 D6 9C DB 72 F5 59 3E 62 2E ; 
;
574A:    04 0B                      ;   Section COMMANDS, Length: 0x000B
574C:       0B 09 0A                ;     SWITCH, Length: 0x0009, Function to call: 0x0A
574F:          01                   ;       Phrase number: 0x01
5750:          02                   ;       ELSE go to: 0x5753
5751:             00 96             ;         MOVE AND LOOK, Destination room: 0x96
5753:          02                   ;       Phrase number: 0x02
5754:          02                   ;       ELSE go to: 0x5757
5755:             00 98             ;         MOVE AND LOOK, Destination room: 0x98

5757: 98 80 E8 00                   ; Room Number: 0x98, Length: 0x00E8, Data: 0x00
;
575B:    03 80 C7                   ;   Section DESCRIPTION, Length: 0x00C7
575E:       04 80 C4                ;     PRINT, Length: 0x00C4
;
; SOUTH OF EAST ALLEY. YOU ARE NOW IN THE DESERT SOUTH OF THE ALLEY AT THE EAST END OF TOWN. TO THE EAST YOU CAN SEE THE FEATURELESS SOUTH WALL OF A BRICK BUILDING. TO THE WEST YOU CAN SEE THE BACK OF THE GROCERY STORE, WHICH IS MARKED AS SUCH. IN THE DISTANCE A SMALL ADOBE BUILDING CAN BE SEEN.
;
5761:          47 B9 53 BE C3 9E 95 5F 03 BC FF 8C DB E0 C7 DE ; 
5771:          94 14 50 5E 6B A1 83 7A 5F BE FF 14 B4 B7 15 BC ; 
5781:          36 A1 11 71 96 64 DB 72 46 48 3B 63 73 49 5F BE ; 
5791:          23 15 F3 B9 8E 61 B8 16 89 17 27 D2 89 17 82 17 ; 
57A1:          47 5E 66 49 51 18 45 C2 83 48 A7 B7 82 17 48 5E ; 
57B1:          96 5F 2F C6 F5 8B D5 B5 36 A1 19 71 46 48 B8 16 ; 
57C1:          7B 14 73 4F 8B 54 EB 4F C3 8B CF 98 89 17 82 17 ; 
57D1:          59 5E 66 62 51 18 45 C2 83 48 A7 B7 82 17 44 5E ; 
57E1:          DD 46 B8 16 82 17 49 5E F5 B2 43 62 66 17 AF A0 ; 
57F1:          19 EE 85 73 0B 71 CF B5 35 49 F3 5F 4B 49 25 BA ; 
5801:          9B 76 83 7A 5F BE 03 15 FB B9 17 98 7B 14 E3 B8 ; 
5811:          F3 8C 09 47 5B 4D EB 4F C3 8B AB 98 10 53 AF 14 ; 
5821:          57 17 A7 61          ; 
;
5825:    04 1B                      ;   Section COMMANDS, Length: 0x001B
5827:       0B 19 0A                ;     SWITCH, Length: 0x0019, Function to call: 0x0A
582A:          04                   ;       Phrase number: 0x04
582B:          02                   ;       ELSE go to: 0x582E
582C:             00 95             ;         MOVE AND LOOK, Destination room: 0x95
582E:          01                   ;       Phrase number: 0x01
582F:          02                   ;       ELSE go to: 0x5832
5830:             00 97             ;         MOVE AND LOOK, Destination room: 0x97
5832:          02                   ;       Phrase number: 0x02
5833:          06                   ;       ELSE go to: 0x583A
5834:             0D 04             ;         WHILE PASS, Length: 0x0004
5836:                30 B2          ;           UNKNOWN1, Data: 0xB2
5838:                2F 04          ;           UNKNOWN2 Data: 0x04
583A:          03                   ;       Phrase number: 0x03
583B:          06                   ;       ELSE go to: 0x5842
583C:             0D 04             ;         WHILE PASS, Length: 0x0004
583E:                30 9B          ;           UNKNOWN1, Data: 0x9B
5840:                2F 04          ;           UNKNOWN2 Data: 0x04

5842: A5 80 92 00                   ; Room Number: 0xA5, Length: 0x0092, Data: 0x00
;
5846:    03 7A                      ;   Section DESCRIPTION, Length: 0x007A
5848:       04 78                   ;     PRINT, Length: 0x0078
;
; NORTH OF BOB'S. YOU ARE STANDING NORTH OF THE HARDWARE STORE. TO THE EAST YOU CAN SEE THE NORTH SIDE OF A TWO STORY BUILDING. TO THE WEST YOU CAN SEE THE NORTH SIDE OF THE SALOON. 
;
584A:          04 9A 53 BE C3 9E F4 4E EF 23 51 18 43 C2 5B B1 ; 
585A:          FB B9 43 98 AB 98 04 9A 53 BE C3 9E 5F BE 9B 15 ; 
586A:          51 B1 2F 49 66 17 AF A0 56 F4 D6 9C DB 72 95 5F ; 
587A:          1B BC 1B A1 10 53 57 17 56 5E DB 72 04 9A 53 BE ; 
588A:          46 B8 51 5E 83 64 91 17 D5 9C 84 BF 44 DB CE C4 ; 
589A:          90 5A 5B 70 6B BF 5F BE F7 17 F3 B9 C7 DE D3 14 ; 
58AA:          95 96 1B 60 5F BE 99 16 C2 B3 5B 17 DB 59 C3 9E ; 
58BA:          5F BE 53 17 81 8D 1B 9C ; 
;
58C2:    04 13                      ;   Section COMMANDS, Length: 0x0013
58C4:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
58C7:          01                   ;       Phrase number: 0x01
58C8:          02                   ;       ELSE go to: 0x58CB
58C9:             00 B8             ;         MOVE AND LOOK, Destination room: 0xB8
58CB:          03                   ;       Phrase number: 0x03
58CC:          02                   ;       ELSE go to: 0x58CF
58CD:             00 A7             ;         MOVE AND LOOK, Destination room: 0xA7
58CF:          04                   ;       Phrase number: 0x04
58D0:          06                   ;       ELSE go to: 0x58D7
58D1:             0D 04             ;         WHILE PASS, Length: 0x0004
58D3:                30 A3          ;           UNKNOWN1, Data: 0xA3
58D5:                2F 02          ;           UNKNOWN2 Data: 0x02

58D7: A6 6C 00                      ; Room Number: 0xA6, Length: 0x006C, Data: 0x00
;
58DA:    03 56                      ;   Section DESCRIPTION, Length: 0x0056
58DC:       04 54                   ;     PRINT, Length: 0x0054
;
; HARDWARE SOUTH. YOU ARE NOW IN THE FRONT HALF OF THE HARDWARE STORE. THERE IS A LARGE AQUARIUM SITTING ON THE FLOOR NEAR YOU. 
;
58DE:          54 72 B3 5C 5B B1 47 B9 77 BE 51 18 43 C2 5B B1 ; 
58EE:          09 9A D0 15 82 17 48 5E 00 B3 0A BC 40 48 B8 16 ; 
58FE:          82 17 4A 5E 2E 49 14 D0 55 5E 84 BF DB 63 5F BE ; 
590E:          5B B1 4B 7B 4E 45 31 49 43 5E A3 AD 17 B2 55 90 ; 
591E:          8E 7B 91 7A C0 16 82 17 48 5E 81 8D 90 AF 94 5F ; 
592E:          51 18 DB C7          ; 
;
5932:    04 11                      ;   Section COMMANDS, Length: 0x0011
5934:       0B 0F 0A                ;     SWITCH, Length: 0x000F, Function to call: 0x0A
5937:          01                   ;       Phrase number: 0x01
5938:          02                   ;       ELSE go to: 0x593B
5939:             00 DC             ;         MOVE AND LOOK, Destination room: 0xDC
593B:          02                   ;       Phrase number: 0x02
593C:          08                   ;       ELSE go to: 0x5945
593D:             0E 06             ;         WHILE FAIL, Length: 0x0006
593F:                14             ;           EXECUTE AND REVERSE STATUS
5940:                1C 0A          ;           SET VAR OBJECT, Object number: 0x0A
5942:                8D             ;           COMMAND 0x8D
5943:                00 93          ;           MOVE AND LOOK, Destination room: 0x93

5945: A7 80 DE 00                   ; Room Number: 0xA7, Length: 0x00DE, Data: 0x00
;
5949:    03 80 C1                   ;   Section DESCRIPTION, Length: 0x00C1
594C:       04 80 BE                ;     PRINT, Length: 0x00BE
;
; NORTH OF EAST ALLEY. YOU ARE IN THE DESERT NORTH OF THE ALLEY AT THE EAST END OF TOWN. TO THE NORTH YOU CAN SEE A TRAIL THAT LEADS INTO THE DESERT. TO THE SOUTH YOU CAN SEE AN ALLEY. TO YOUR IMMEDIATE EAST THERE IS A TWO STORY BUILDING. TO YOUR WEST THERE IS THE BACK OF A SMALL STORE.
;
594F:          04 9A 53 BE C3 9E 95 5F 03 BC FF 8C DB E0 C7 DE ; 
595F:          94 14 4B 5E 96 96 DB 72 F5 59 3E 62 99 16 C2 B3 ; 
596F:          B8 16 82 17 43 5E FF 8C 43 DB 16 BC DB 72 95 5F ; 
597F:          07 BC 33 98 C3 9E 89 BF 1B 9C 6B BF 5F BE 99 16 ; 
598F:          C2 B3 51 18 45 C2 83 48 A7 B7 7B 14 EB BF 33 7A ; 
599F:          5B BE 0E BC 86 5F CB B5 C9 9A 82 17 46 5E 57 62 ; 
59AF:          D7 B3 89 17 82 17 55 5E 36 A1 1B 71 1B A1 10 53 ; 
59BF:          57 17 43 5E 83 96 FF 8C DB E0 6B BF C7 DE 8B AF ; 
59CF:          67 93 83 5A DB BD 95 5F 16 BC F4 72 4B 5E C3 B5 ; 
59DF:          91 17 D5 9C 84 BF 44 DB CE C4 90 5A 5B 70 6B BF ; 
59EF:          C7 DE 99 AF 66 62 82 17 2F 62 D5 15 82 17 44 5E ; 
59FF:          DD 46 B8 16 7B 14 E3 B8 F3 8C 09 BA 7F B1 ; 
;
5A0D:    04 17                      ;   Section COMMANDS, Length: 0x0017
5A0F:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: 0x0A
5A12:          01                   ;       Phrase number: 0x01
5A13:          02                   ;       ELSE go to: 0x5A16
5A14:             00 B8             ;         MOVE AND LOOK, Destination room: 0xB8
5A16:          02                   ;       Phrase number: 0x02
5A17:          02                   ;       ELSE go to: 0x5A1A
5A18:             00 A8             ;         MOVE AND LOOK, Destination room: 0xA8
5A1A:          03                   ;       Phrase number: 0x03
5A1B:          06                   ;       ELSE go to: 0x5A22
5A1C:             0D 04             ;         WHILE PASS, Length: 0x0004
5A1E:                30 A9          ;           UNKNOWN1, Data: 0xA9
5A20:                2F 04          ;           UNKNOWN2 Data: 0x04
5A22:          04                   ;       Phrase number: 0x04
5A23:          02                   ;       ELSE go to: 0x5A26
5A24:             00 A5             ;         MOVE AND LOOK, Destination room: 0xA5

5A26: A8 80 80 00                   ; Room Number: 0xA8, Length: 0x0080, Data: 0x00
;
5A2A:    03 70                      ;   Section DESCRIPTION, Length: 0x0070
5A2C:       04 6E                   ;     PRINT, Length: 0x006E
;
; EAST ALLEY NORTH. YOU ARE IN THE ALLEY NORTH OF MAIN STREET AT THE EAST END OF TOWN. THERE IS A SMALL ALCOVE HERE THAT IS NOT VISIBLE FROM THE STREET OR THE DESERT. 
;
5A2E:          95 5F 03 BC FF 8C 50 DB BE A0 9B 76 C7 DE 94 14 ; 
5A3E:          4B 5E 96 96 DB 72 46 48 3B 63 04 9A 53 BE C3 9E ; 
5A4E:          8B 91 95 96 EF BF 73 62 73 49 5F BE 23 15 F3 B9 ; 
5A5E:          8E 61 B8 16 89 17 27 D2 82 17 2F 62 D5 15 7B 14 ; 
5A6E:          E3 B8 F3 8C 3D 48 4F A1 9F 15 5B B1 5B BE 0B BC ; 
5A7E:          D0 B5 F3 A0 15 CB B6 78 48 5E FF B2 82 17 55 5E ; 
5A8E:          EF BF 73 62 A3 A0 5F BE FF 14 B4 B7 9B C1 ; 
;
5A9C:    04 0B                      ;   Section COMMANDS, Length: 0x000B
5A9E:       0B 09 0A                ;     SWITCH, Length: 0x0009, Function to call: 0x0A
5AA1:          01                   ;       Phrase number: 0x01
5AA2:          02                   ;       ELSE go to: 0x5AA5
5AA3:             00 A7             ;         MOVE AND LOOK, Destination room: 0xA7
5AA5:          02                   ;       Phrase number: 0x02
5AA6:          02                   ;       ELSE go to: 0x5AA9
5AA7:             00 96             ;         MOVE AND LOOK, Destination room: 0x96

5AA9: B1 4A 00                      ; Room Number: 0xB1, Length: 0x004A, Data: 0x00
;
5AAC:    03 26                      ;   Section DESCRIPTION, Length: 0x0026
5AAE:       04 24                   ;     PRINT, Length: 0x0024
;
; DESERT SOUTH. YOU ARE IN THE DESERT SOUTH OF THE TOWN.
;
5AB0:          F5 59 3E 62 61 17 82 C6 5B F4 1B A1 2F 49 D0 15 ; 
5AC0:          82 17 46 5E 57 62 B3 B3 47 B9 53 BE C3 9E 5F BE ; 
5AD0:          89 17 27 D2          ; 
;
5AD4:    04 1F                      ;   Section COMMANDS, Length: 0x001F
5AD6:       0B 1D 0A                ;     SWITCH, Length: 0x001D, Function to call: 0x0A
5AD9:          01                   ;       Phrase number: 0x01
5ADA:          06                   ;       ELSE go to: 0x5AE1
5ADB:             0D 04             ;         WHILE PASS, Length: 0x0004
5ADD:                30 92          ;           UNKNOWN1, Data: 0x92
5ADF:                2F 02          ;           UNKNOWN2 Data: 0x02
5AE1:          02                   ;       Phrase number: 0x02
5AE2:          02                   ;       ELSE go to: 0x5AE5
5AE3:             00 B3             ;         MOVE AND LOOK, Destination room: 0xB3
5AE5:          03                   ;       Phrase number: 0x03
5AE6:          06                   ;       ELSE go to: 0x5AED
5AE7:             0D 04             ;         WHILE PASS, Length: 0x0004
5AE9:                30 B2          ;           UNKNOWN1, Data: 0xB2
5AEB:                2F 04          ;           UNKNOWN2 Data: 0x04
5AED:          04                   ;       Phrase number: 0x04
5AEE:          06                   ;       ELSE go to: 0x5AF5
5AEF:             0D 04             ;         WHILE PASS, Length: 0x0004
5AF1:                30 B0          ;           UNKNOWN1, Data: 0xB0
5AF3:                2F 01          ;           UNKNOWN2 Data: 0x01

5AF5: B3 5C 00                      ; Room Number: 0xB3, Length: 0x005C, Data: 0x00
;
5AF8:    03 2F                      ;   Section DESCRIPTION, Length: 0x002F
5AFA:       04 2D                   ;     PRINT, Length: 0x002D
;
; DESERT. YOU ARE IN THE DESERT. FAR TO THE NORTH YOU CAN SEE A TOWN.
;
5AFC:          F5 59 3E 62 5B F4 1B A1 2F 49 D0 15 82 17 46 5E ; 
5B0C:          57 62 D7 B3 4B 15 96 AF D6 9C DB 72 04 9A 53 BE ; 
5B1C:          C7 DE D3 14 95 96 1B 60 56 45 80 A1 2E ; 
;
5B29:    04 28                      ;   Section COMMANDS, Length: 0x0028
5B2B:       0B 26 0A                ;     SWITCH, Length: 0x0026, Function to call: 0x0A
5B2E:          02                   ;       Phrase number: 0x02
5B2F:          09                   ;       ELSE go to: 0x5B39
5B30:             0D 07             ;         WHILE PASS, Length: 0x0007
5B32:                30 E1          ;           UNKNOWN1, Data: 0xE1
5B34:                17 9D 01       ;           MOVE TO, Object number: 0x9D, Destination room: 0x01
5B37:                2F 05          ;           UNKNOWN2 Data: 0x05
5B39:          03                   ;       Phrase number: 0x03
5B3A:          09                   ;       ELSE go to: 0x5B44
5B3B:             0D 07             ;         WHILE PASS, Length: 0x0007
5B3D:                30 E2          ;           UNKNOWN1, Data: 0xE2
5B3F:                17 9D 01       ;           MOVE TO, Object number: 0x9D, Destination room: 0x01
5B42:                2F 05          ;           UNKNOWN2 Data: 0x05
5B44:          04                   ;       Phrase number: 0x04
5B45:          09                   ;       ELSE go to: 0x5B4F
5B46:             0D 07             ;         WHILE PASS, Length: 0x0007
5B48:                30 E0          ;           UNKNOWN1, Data: 0xE0
5B4A:                17 9D 01       ;           MOVE TO, Object number: 0x9D, Destination room: 0x01
5B4D:                2F 05          ;           UNKNOWN2 Data: 0x05
5B4F:          01                   ;       Phrase number: 0x01
5B50:          02                   ;       ELSE go to: 0x5B53
5B51:             00 B1             ;         MOVE AND LOOK, Destination room: 0xB1

5B53: B8 72 00                      ; Room Number: 0xB8, Length: 0x0072, Data: 0x00
;
5B56:    03 4B                      ;   Section DESCRIPTION, Length: 0x004B
5B58:       04 49                   ;     PRINT, Length: 0x0049
;
; DESERT NORTH. YOU ARE NOW STANDING ON A PATH TO THE NORTH OF TOWN. THE PATH RUNS FROM THE SOUTH TO THE NORTH.
;
5B5A:          F5 59 3E 62 99 16 C2 B3 5B F4 1B A1 2F 49 99 16 ; 
5B6A:          D5 CE 50 BD 90 5A D1 6A 83 96 DB 16 53 BE 6B BF ; 
5B7A:          5F BE 99 16 C2 B3 B8 16 89 17 27 D2 82 17 52 5E ; 
5B8A:          82 49 3F 17 8B 9A 79 68 56 90 DB 72 47 B9 53 BE ; 
5B9A:          6B BF 5F BE 99 16 C2 B3 2E ; 
;
5BA3:    04 22                      ;   Section COMMANDS, Length: 0x0022
5BA5:       0B 20 0A                ;     SWITCH, Length: 0x0020, Function to call: 0x0A
5BA8:          01                   ;       Phrase number: 0x01
5BA9:          06                   ;       ELSE go to: 0x5BB0
5BAA:             0D 04             ;         WHILE PASS, Length: 0x0004
5BAC:                30 B7          ;           UNKNOWN1, Data: 0xB7
5BAE:                2F 02          ;           UNKNOWN2 Data: 0x02
5BB0:          02                   ;       Phrase number: 0x02
5BB1:          02                   ;       ELSE go to: 0x5BB4
5BB2:             00 A7             ;         MOVE AND LOOK, Destination room: 0xA7
5BB4:          03                   ;       Phrase number: 0x03
5BB5:          09                   ;       ELSE go to: 0x5BBF
5BB6:             0D 07             ;         WHILE PASS, Length: 0x0007
5BB8:                30 F1          ;           UNKNOWN1, Data: 0xF1
5BBA:                17 9D 01       ;           MOVE TO, Object number: 0x9D, Destination room: 0x01
5BBD:                2F 05          ;           UNKNOWN2 Data: 0x05
5BBF:          04                   ;       Phrase number: 0x04
5BC0:          06                   ;       ELSE go to: 0x5BC7
5BC1:             0D 04             ;         WHILE PASS, Length: 0x0004
5BC3:                30 B6          ;           UNKNOWN1, Data: 0xB6
5BC5:                2F 02          ;           UNKNOWN2 Data: 0x02

5BC7: DC 35 00                      ; Room Number: 0xDC, Length: 0x0035, Data: 0x00
;
5BCA:    03 29                      ;   Section DESCRIPTION, Length: 0x0029
5BCC:       04 27                   ;     PRINT, Length: 0x0027
;
; HARDWARE NORTH. YOU ARE IN THE BACK OF THE HARDWARE STORE.
;
5BCE:          54 72 B3 5C 5B B1 04 9A 77 BE 51 18 43 C2 5B B1 ; 
5BDE:          83 7A 5F BE AB 14 8B 54 C3 9E 5F BE 9B 15 51 B1 ; 
5BEE:          2F 49 66 17 AF A0 2E ; 
;
5BF5:    04 07                      ;   Section COMMANDS, Length: 0x0007
5BF7:       0B 05 0A                ;     SWITCH, Length: 0x0005, Function to call: 0x0A
5BFA:          02                   ;       Phrase number: 0x02
5BFB:          02                   ;       ELSE go to: 0x5BFE
5BFC:             00 A6             ;         MOVE AND LOOK, Destination room: 0xA6


5BFE: 1D 0A 37 10 0D 0E 0E 04 09 00 09 60 0E 06 14 1C ; ..7.............
5C0E: 15 8D 00 A0 54 08 0E 06 14 1C 15 8D 00 A0 52 45 ; ....T.........RE
5C1E: 54 3D 06 53 4B 45 4C 45 54 17 05 53 54 45 45 4C ; T=.SKELET..STEEL
5C2E: 18 03 43 41 42 4B 03 42 49 47 0E 05 4C 41 52 47 ; ..CABK.BIG..LARG
5C3E: 45 0E 05 53 4D 41 4C 4C 0F 06 4C 49 54 54 4C 45 ; E..SMALL..LITTLE
5C4E: 0F 03 54 4F 50 28 06 4D 49 44 44 4C 45 3C 06 42 ; ..TOP(.MIDDLE<.B
5C5E: 4F 54 54 4F 4D 3E 04 46 4C 41 54 22 05 53 50 41 ; OTTOM>.FLAT".SPA
5C6E: 52 45 23 04 42 4C 55 45 0D 06 4D 41 53 53 49 56 ; RE#.BLUE..MASSIV
5C7E: 3F 04 42 41 4E 4B 40 06 53 41 4C 4F 4F 4E 41 06 ; ?.BANK@.SALOONA.
5C8E: 53 48 45 52 49 46 42 06 4F 46 46 49 43 45 42 06 ; SHERIFB.OFFICEB.
5C9E: 53 4C 49 4D 27 53 43 05 53 4C 49 4D 53 43 05 42 ; SLIM'SC.SLIMSC.B
5CAE: 4F 42 27 53 44 04 42 4F 42 53 44 06 44 4F 55 42 ; OB'SD.BOBSD.DOUB
5CBE: 4C 45 45 05 48 4F 54 45 4C 47 06 53 57 49 4E 47 ; LEE.HOTELG.SWING
5CCE: 49 46 04 54 53 4F 4D 6B 04 43 4F 4F 4C 72 05 43 ; IF.TSOMk.COOLr.C
5CDE: 4C 45 41 52 74 05 42 52 4F 57 4E 73 00 02 54 4F ; LEARt.BROWNs..TO
5CEE: 01 04 57 49 54 48 02 05 55 53 49 4E 47 02 02 41 ; ..WITH..USING..A
5CFE: 54 03 05 02 02 00 72 60 0E 06 14 1C 15 8D 00 A0 ; T.....r.........
5D0E: 54 08 0E 06 14 1C 15 8D 00 A0 52 45 54 3D 06 53 ; T.........RET=.S
5D1E: 4B 45 4C 45 54 17 05 53 54 45 45 4C 18 03 43 41 ; KELET..STEEL..CA
5D2E: 42 4B 03 42 49 47 0E 05 4C 41 52 47 45 0E 05 53 ; BK.BIG..LARGE..S
5D3E: 4D 41 4C 4C 0F 06 4C 49 54 54 4C 45 0F 03 54 4F ; MALL..LITTLE..TO
5D4E: 50 28 06 4D 49 44 44 4C 45 3C 06 42 4F 54 54 4F ; P(.MIDDLE<.BOTTO
5D5E: 4D 3E 04 46 4C 41 54 22 05 53 50 41 52 45 23 04 ; M>.FLAT".SPARE#.
5D6E: 42 4C 55 45 0D 06 4D 41 53 53 49 56 3F 04 42 41 ; BLUE..MASSIV?.BA
5D7E: 4E 4B 40 06 53 41 4C 4F 4F 4E 41 06 53 48 45 52 ; NK@.SALOONA.SHER
5D8E: 49 46 42 06 4F 46 46 49 43 45 42 06 53 4C 49 4D ; IFB.OFFICEB.SLIM
5D9E: 27 53 43 05 53 4C 49 4D 53 43 05 42 4F 42 27 53 ; 'SC.SLIMSC.BOB'S
5DAE: 44 04 42 4F 42 53 44 06 44 4F 55 42 4C 45 45 05 ; D.BOBSD.DOUBLEE.
5DBE: 48 4F 54 45 4C 47 06 53 57 49 4E 47 49 46 04 54 ; HOTELG.SWINGIF.T
5DCE: 53 4F                                           ; SO
```

