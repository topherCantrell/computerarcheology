C ADVENTURES
	IMPLICIT INTEGER(A-Z)
	REAL RAN
	COMMON RTEXT,LLINE
	DIMENSION IOBJ(300),ICHAIN(100),IPLACE(100)
	1 ,IFIXED(100),COND(300),PROP(100),ABB(300),LLINE(1000,22)
	2 ,LTEXT(300),STEXT(300),KEY(300),DEFAULT(300),TRAVEL(1000)
	3 ,TK(25),KTAB(1000),ATAB(1000),BTEXT(200),DSEEN(10)
	4 ,DLOC(10),ODLOC(10),DTRAV(20),RTEXT(100),JSPKT(100)
	5 ,IPLT(100),IFIXT(100)

C READ THE PARAMETERS

	IF(SETUP.NE.0) GOTO 1
	SETUP=1
	KEYS=1
	LAMP=2
	GRATE=3
	ROD=5
	BIRD=7
	NUGGET=10
	SNAKE=11
	FOOD=19
	WATER=20
	AXE=21
	
	;; A default message for every transitive verb function:
	;;  1 GET   = 24  YOU ARE ALREADY CARRYING IT!
	;;  2 DROP  = 29  YOU AREN'T CARRYING IT!
	;;  3 DUMMY =  0
	;;  4 OPEN  = 31  YOU HAVE NO KEYS!
	;;  5 HOLD  =  0
	;;  6 LOCK  = 31  YOU HAVE NO KEYS!
	;;  7 ON    = 38  YOU HAVE NO SOURCE OF LIGHT.
	;;  8 OFF   = 38  YOU HAVE NO SOURCE OF LIGHT.
	;;  9 STRIK = 42  NOTHING HAPPENS.
	;; 10 WAVE  = 42  NOTHING HAPPENS.
	;; 11 RUN   = 43  WHERE?
	;; 12 KILL  = 46  ATTACKING THE SNAKE BOTH DOESN'T WORK AND IS VERY DANGEROUS.
	;; 13 POUR  = 77  YOUR BOTTLE IS EMPTY AND THE GROUND IS WET.
	;; 14 EAT   = 71  THERE IS NOTHING HERE TO EAT.
	;; 15 DRINK = 73  THERE IS NO DRINKABLE WATER HERE.
	;; 16 RUB   = 75  RUBBING THE ELECTRIC LAMP IS NOT PARTICULARLY REWARDING.
	DATA(JSPKT(I),I=1,16)/24,29,0,31,0,31,38,38,42,42,43,46,77,71
	1 ,73,75/

	DATA(IPLT(I),I=1,20)/3,3,8,10,11,14,13,9,15,18,19,17,27,28,29
	1 ,30,0,0,3,3/
	DATA(IFIXT(I),I=1,20)/0,0,1,0,0,1,0,1,1,0,1,1,0,0,0,0,0,0,0,0/
	DATA(DTRAV(I),I=1,15)/36,28,19,30,62,60,41,27,17,15,19,28,36
	1 ,300,300/
	DO 1001 I=1,300
	STEXT(I)=0
	IF(I.LE.200) BTEXT(I)=0
	IF(I.LE.100)RTEXT(I)=0
1001	LTEXT(I)=0
	I=1
	CALL IFILE(1,'TEXT')
1002	READ(1,1003) IKIND
1003	FORMAT(G)
	GOTO(1100,1004,1004,1013,1020,1004,1004)(IKIND+1)
1004	READ(1,1005)JKIND,(LLINE(I,J),J=3,22)
1005	FORMAT(1G,20A5)
	IF(JKIND.EQ.-1) GOTO 1002
	DO 1006 K=1,20
	KK=K
	IF(LLINE(I,21-K).NE.' ') GOTO 1007
1006	CONTINUE
	STOP
1007	LLINE(I,2)=20-KK+1
	LLINE(I,1)=0
	IF(IKIND.EQ.6)GOTO 1023
	IF(IKIND.EQ.5)GOTO 1011
	IF(IKIND.EQ.1) GOTO 1008
	IF(STEXT(JKIND).NE.0) GOTO 1009
	STEXT(JKIND)=I
	GOTO 1010

1008	IF(LTEXT(JKIND).NE.0) GOTO 1009
	LTEXT(JKIND)=I
	GOTO 1010
1009	LLINE(I-1,1)=I
1010	I=I+1
	IF(I.NE.1000)GOTO 1004
	PAUSE 'TOO MANY LINES'

1011	IF(JKIND.LT.200)GOTO 1012
	IF(BTEXT(JKIND-100).NE.0)GOTO 1009
	BTEXT(JKIND-100)=I
	BTEXT(JKIND-200)=I
	GOTO 1010
1012	IF(BTEXT(JKIND).NE.0)GOTO 1009
	BTEXT(JKIND)=I
	GOTO 1010

1023	IF(RTEXT(JKIND).NE.0) GOTO 1009
	RTEXT(JKIND)=I
	GOTO 1010

1013	I=1
1014	READ(1,1015)JKIND,LKIND,(TK(L),L=1,10)
1015	FORMAT(12G)
	IF(JKIND.EQ.-1) GOTO 1002
	IF(KEY(JKIND).NE.0) GOTO 1016
	KEY(JKIND)=I
	GOTO 1017
1016	TRAVEL(I-1)=-TRAVEL(I-1)
1017	DO 1018 L=1,10
	IF(TK(L).EQ.0) GOTO 1019
	TRAVEL(I)=LKIND*1024+TK(L)
	I=I+1
	IF(I.EQ.1000) STOP
1018	CONTINUE
1019	TRAVEL(I-1)=-TRAVEL(I-1)
	GOTO 1014

1020	DO 1022 IU=1,1000
	READ(1,1021) KTAB(IU),ATAB(IU)
1021	FORMAT(G,A5)
	IF(KTAB(IU).EQ.-1)GOTO 1002
1022	CONTINUE
	PAUSE 'TOO MANY WORDS'


C TRAVEL = NEG IF LAST THIS SOURCE + DEST*1024 + KEYWORD

C COND  = 1 IF LIGHT,  2 IF DON T ASK QUESTION





1100	DO 1101 I=1,100
	IPLACE(I)=IPLT(I)
	IFIXED(I)=IFIXT(I)
1101	ICHAIN(I)=0

	DO 1102 I=1,300
	COND(I)=0
	ABB(I)=0
1102	IOBJ(I)=0
	DO 1103 I=1,10
1103	COND(I)=1
	COND(16)=2
	COND(20)=2
	COND(21)=2
	COND(22)=2
	COND(23)=2
	COND(24)=2
	COND(25)=2
	COND(26)=2
	COND(31)=2
	COND(32)=2
	COND(79)=2

	DO 1107 I=1,100
	KTEM=IPLACE(I)
	IF(KTEM.EQ.0)GOTO 1107
	IF(IOBJ(KTEM).NE.0) GOTO 1104
	IOBJ(KTEM)=I
	GO TO 1107
1104	KTEM=IOBJ(KTEM)
1105	IF(ICHAIN(KTEM).NE.0) GOTO 1106
	ICHAIN(KTEM)=I
	GOTO 1107
1106	KTEM=ICHAIN(KTEM)
	GOTO 1105
1107	CONTINUE
	IDWARF=0
	IFIRST=1
	IWEST=0
	ILONG=1
	IDETAL=0
	PAUSE 'INIT DONE'



1	CALL YES(65,1,0,YEA)
	L=1
	LOC=1
2	DO 73 I=1,3
	IF(ODLOC(I).NE.L.OR.DSEEN(I).EQ.0)GOTO 73
	L=LOC
	CALL SPEAK(2)  ;; "A LITTLE DWARF WITH A BIG KNIFE BLOCKS YOUR WAY."
	GOTO 74
73	CONTINUE
74	LOC=L

C DWARF STUFF

	IF(IDWARF.NE.0) GOTO 60
	IF(LOC.EQ.15) IDWARF=1
	GOTO 71
60	IF(IDWARF.NE.1)GOTO 63
	IF(RAN(QZ).GT.0.05) GOTO 71
	IDWARF=2
	DO 61 I=1,3
	DLOC(I)=0
	ODLOC(I)=0
61	DSEEN(I)=0
	CALL SPEAK(3)  ; "A LITTLE DWARF JUST WALKED AROUND A CORNER"
	ICHAIN(AXE)=IOBJ(LOC)
	IOBJ(LOC)=AXE
	IPLACE(AXE)=LOC
	GOTO 71

63	IDWARF=IDWARF+1
	ATTACK=0
	DTOT=0
	STICK=0
	DO 66 I=1,3
	IF(2*I+IDWARF.LT.8)GOTO 66
	IF(2*I+IDWARF.GT.23.AND.DSEEN(I).EQ.0)GOTO 66
	ODLOC(I)=DLOC(I)
	IF(DSEEN(I).NE.0.AND.LOC.GT.14)GOTO 65
	DLOC(I)=DTRAV(I*2+IDWARF-8)
	DSEEN(I)=0
	IF(DLOC(I).NE.LOC.AND.ODLOC(I).NE.LOC) GOTO 66
65	DSEEN(I)=1
	DLOC(I)=LOC
	DTOT=DTOT+1
	IF(ODLOC(I).NE.DLOC(I)) GOTO 66
	ATTACK=ATTACK+1
	IF(RAN(QZ).LT.0.1) STICK=STICK+1
66	CONTINUE
	IF(DTOT.EQ.0) GOTO 71
	IF(DTOT.EQ.1)GOTO 75
	TYPE 67,DTOT
67	FORMAT(' THERE ARE ',I2,' THREATENING LITTLE DWARVES IN THE
	1  ROOM WITH YOU.',/)
	GOTO 77
75	CALL SPEAK(4)  ;; "THERE IS A THREATENING LITTLE DWARF"
77	IF(ATTACK.EQ.0)GOTO 71
	IF(ATTACK.EQ.1)GOTO 79
	TYPE 78,ATTACK
78	FORMAT(' ',I2,' OF THEM THROW KNIVES AT YOU!',/)
	GOTO 81
79	CALL SPEAK(5)  ;; "ONE SHARP NASTY KNIFE IS THROWN AT YOU!"
	CALL SPEAK(52+STICK)
	GOTO(71,83)(STICK+1)

81	IF(STICK.EQ.0) GOTO 69
	IF(STICK.EQ.1)GOTO 82
	TYPE 68,STICK
68	FORMAT(' ',I2,' OF THEM GET YOU.',/)
	GOTO 83
82	CALL SPEAK(6)  ;; "HE GETS YOU!"
83	PAUSE 'GAMES OVER'
	GOTO 71
69	CALL SPEAK(7) ;; "NONE OF THEM HIT YOU!"

C PLACE DESCRIPTOR



71	KK=STEXT(L)
	IF(ABB(L).EQ.0.OR.KK.EQ.0)KK=LTEXT(L)
	IF(KK.EQ.0) GOTO 7
4	TYPE 5,(LLINE(KK,JJ),JJ=3,LLINE(KK,2))
5	FORMAT(20A5)
	KK=KK+1
	IF(LLINE(KK-1,1).NE.0) GOTO 4
	TYPE 6                                ;; Print ...
6	FORMAT(/)                             ;; ... blank line
7	IF(COND(L).EQ.2)GOTO 8
	IF(LOC.EQ.33.AND.RAN(QZ).LT.0.25)CALL SPEAK(8)  ;; In room 33, 25% chance to see "A HOLLOW VOICE SAYS 'PLUGH'"
	J=L
	GOTO 2000

C GO GET A NEW LOCATION

8	KK=KEY(LOC)
	IF(KK.EQ.0)GOTO 19
	IF(K.EQ.57)GOTO 32
	IF(K.EQ.67)GOTO 40
	IF(K.EQ.8)GOTO 12
	LOLD=L
9	LL=TRAVEL(KK)
	IF(LL.LT.0) LL=-LL
	IF(1.EQ.MOD(LL,1024))GOTO 10
	IF(K.EQ.MOD(LL,1024))GOTO 10
	IF(TRAVEL(KK).LT.0)GOTO 11
	KK=KK+1
	GOTO 9
12	TEMP=LOLD
	LOLD=L
	L=TEMP
	GOTO 21
10	L=LL/1024
	GOTO 21
11	JSPK=12
	IF(K.GE.43.AND.K.LE.46)JSPK=9
	IF(K.EQ.29.OR.K.EQ.30)JSPK=9
	IF(K.EQ.7.OR.K.EQ.8.OR.K.EQ.36.OR.K.EQ.37.OR.K.EQ.68)
	1 JSPK=10
	IF(K.EQ.11.OR.K.EQ.19)JSPK=11
	IF(JVERB.EQ.1)JSPK=59
	IF(K.EQ.48)JSPK=42
	IF(K.EQ.17)JSPK=80
	CALL SPEAK(JSPK)
	GOTO 2
19	CALL SPEAK(13)  ;; "I DON'T UNDERSTAND THAT!"
	L=LOC
	IF(IFIRST.EQ.0) CALL SPEAK(14)  ;; "I ALWAYS UNDERSTAND COMPASS DIRECTIONS"
21	IF(L.LT.300)GOTO 2
	IL=L-300+1
	GOTO(22,23,24,25,26,31,27,28,29,30,33,34,36,37)IL
	GOTO 2

;; TODO this might be the complex room near bedquilt. Woods might have moved all this to the travel table.

22	L=6
	IF(RAN(QZ).GT.0.5) L=5
	GOTO 2
23	L=23
	IF(PROP(GRATE).NE.0) L=9
	GOTO 2
24	L=9
	IF(PROP(GRATE).NE.0)L=8
	GOTO 2
25	L=20
	IF(IPLACE(NUGGET).NE.-1)L=15
	GOTO 2
26	L=22
	IF(IPLACE(NUGGET).NE.-1) L=14
	GOTO 2
27	L=27
	IF(PROP(12).EQ.0)L=31
	GOTO 2
28	L=28
	IF(PROP(SNAKE).EQ.0)L=32
	GOTO 2
29	L=29
	IF(PROP(SNAKE).EQ.0) L=32
	GOTO 2
30	L=30
	IF(PROP(SNAKE).EQ.0) L=32
	GOTO 2
31	PAUSE 'GAME IS OVER'
	GOTO 1100
32	IF(IDETAL.LT.3)CALL SPEAK(15)  ;; "I AM NOT ALLOWED TO GIVE MORE DETAIL"
	IDETAL=IDETAL+1
	L=LOC
	ABB(L)=0
	GOTO 2
33	L=8
	IF(PROP(GRATE).EQ.0) L=9
	GOTO 2
34	IF(RAN(QZ).GT.0.2)GOTO 35
	L=68
	GOTO 2
35	L=65
38	CALL SPEAK(56)  ;; "YOU HAVE CRAWLED AROUND IN SOME LITTLE HOLES"
	GOTO 2
36	IF(RAN(QZ).GT.0.2)GOTO 35
	L=39
	IF(RAN(QZ).GT.0.5)L=70
	GOTO 2
37	L=66
	IF(RAN(QZ).GT.0.4)GOTO 38
	L=71
	IF(RAN(QZ).GT.0.25)L=72
	GOTO 2
39	L=66
	IF(RAN(QZ).GT.0.2)GOTO 38
	L=77
	GOTO 2
40	IF(LOC.LT.8)CALL SPEAK(57)  ;; "I WOULD TRY THE STREAM." At the surface entrance to cave
	IF(LOC.GE.8)CALL SPEAK(58)  ;; "I NEED MORE DETAILED INSTRUCTIONS" underground
	L=LOC
	GOTO 2



C DO NEXT INPUT

;; There is a counter on the room description that is bumped and rolled with every visit. Every
;; five visits, you get the room description.

2000	LTRUBL=0
	LOC=J
	ABB(J)=MOD((ABB(J)+1),5)                              ;; Bump the "visited" count (resets to 0 at 5)
	IDARK=0                                               ;; Assume it is NOT dark for the moment
	IF(MOD(COND(J),2).EQ.1) GOTO 2003                     ;; This room has light in it, don't check the lamp
	IF((IPLACE(2).NE.J).AND.(IPLACE(2).NE.-1)) GOTO 2001  ;; If the LAMP is not in pack or room, it doesn't give us light
	IF(PROP(2).EQ.1)GOTO 2003                             ;; If the LAMP is on, 
2001	CALL SPEAK(16)                                    ;; "IT IS NOW PITCH BLACK."
	IDARK=1


2003	I=IOBJ(J)
2004	IF(I.EQ.0) GOTO 2011
	IF(((I.EQ.6).OR.(I.EQ.9)).AND.(IPLACE(10).EQ.-1))GOTO 2008
	ILK=I
	IF(PROP(I).NE.0) ILK=I+100
	KK=BTEXT(ILK)
	IF(KK.EQ.0) GOTO 2008
2005	TYPE 2006,(LLINE(KK,JJ),JJ=3,LLINE(KK,2))
2006	FORMAT(20A5)
	KK=KK+1
	IF(LLINE(KK-1,1).NE.0) GOTO 2005
	TYPE 2007
2007	FORMAT(/)
2008	I=ICHAIN(I)
	GOTO 2004



C K=1 MEANS ANY INPUT


2012	A=WD2                          ;; Move 2nd word to 1st word
	B=' '                              ;; Clear out ...
	TWOWDS=0                           ;; ... second word
	GOTO 2021                          ;; Process the new 1st word ("ENTER BUILDing" becomes "BUILDing")

2009	K=54                           ;; "OK" -- acknowledgement before next command
2010	JSPK=K                         ;; Print response ...
5200	CALL SPEAK(JSPK)               ;; ... before next input

;; Clear the verb/object and start input
;;
2011	JVERB=0                        ;; Initialize to no-verb
	JOBJ=0                             ;; Initialize to no-noun
	TWOWDS=0                           ;; Initialize to not-two-words

;; Continue input with existing verb/object
;;
2020	CALL GETIN(TWOWDS,A,WD2,B)                                    ;; Get one or two words

	K=70                                                              ;; "YOUR FEET ARE NOW WET."
	IF(A.EQ.'ENTER'.AND.(WD2.EQ.'STREA'.OR.WD2.EQ.'WATER'))GOTO 2010  ;; Handle "ENTER STREA" or "ENTER WATER"

	IF(A.EQ.'ENTER'.AND.TWOWDS.NE.0)GOTO 2012              ;; "ENTER" with a 2nd word (try "ENTER NORTH"), treat 2nd word as 1st

2021	IF(A.NE.'WEST')GOTO 2023       ;; If the player types "WEST" 10 times, we
	IWEST=IWEST+1                      ;; ... give ...
	IF(IWEST.NE.10)GOTO 2023           ;; ... the hint ...
	CALL SPEAK(17)                     ;; ... "IF YOU PREFER, SIMPLY TYPE W RATHER THAN WEST."

2023	DO 2024 I=1,1000               ;; Decode the first word
	IF(KTAB(I).EQ.-1)GOTO 3000         ;; We reached the end of the word list (no match)
	IF(ATAB(I).EQ.A)GOTO 2025          ;; We found the word, go process it
2024	CONTINUE                       ;; Loop over all words
	PAUSE 'ERROR 6'                    ;; Should never get here. Only if there is no "-1" on the end.

;; Lower 3 digits are the word function. NORTH and N are the same: 045
;; Upper digit is the word type:
;;   - 0: single word verb like "NORTH" and "LOOK"
;;   - 1: nouns like "LAMP" and "BIRD"
;;   - 2: verbs that require a noun like "GET" and "EAT"
;;   - 3: small collection of words that have simple responses
2025	K=MOD(KTAB(I),1000)           ;; Word function
	KQ=KTAB(I)/1000+1                 ;; Word type (noun, single word verb, etc)
	GOTO (5014,5000,2026,2010)KQ      ;; Process the first word based on type
	PAUSE 'NO NO'                     ;; Should never get here. Only if unexpected word type.

;; PROCESS TRANSITIVE VERBS (require a 2nd word object)
;;
2026	JVERB=K                       ;; Hold on to the verb (will loop back to decode noun)
	JSPK=JSPKT(JVERB)                 ;; Default response for this transitive verb
	IF(TWOWDS.NE.0)GOTO 2028          ;; We have a 2nd word, go parse it
	IF(JOBJ.EQ.0)GOTO 2036            ;; No 2nd word and no earlier noun, general error for transitive verbs
;;
;; 3rd entry is for "DUMMY object". If the object is in pack or room, you get this general error. Try "GET KEYS" to see
;; "I DON'T KNOW THAT WORD." even though the code parsed both words. Or "DUMMY GET".
;;
;; 5th entry is for HOLD or NOTHING. A valid entry just prints OK so that things like "GET NOTHING" and
;; "RUB NOTHING" make sense. You can do NOTHING to any old object. The HOLD makes less sense. Try "HOLD SNAKE"
;; when you see it. Or find the lamp in a room and do "HOLD LAMP". It says "OK", but you don't "GET" it.
;;
2027	GOTO(9000,5066,3000,5031,2009,5031,9404,9406,5081,5200,  ;; Hanlders for each verb type (GET, DROP, etc)
	1 5200,5300,5506,5502,5504,5505)JVERB
	PAUSE 'ERROR 5'                    ;; Should never get here (only if error in word table)

;; We have the verb in JVERB. Now go back and parse the second word
2028	A=WD2                          ;; Move 2nd word to 1st
	B=' '                              ;; Clear ...
	TWOWDS=0                           ;; ... second word
	GOTO 2023                          ;; Reprocess using 2nd word as 1st

3000	JSPK=60                        ;; "I DON'T KNOW THAT WORD."
	IF(RAN(QZ).GT.0.8)JSPK=61          ;; "WHAT?"
	IF(RAN(QZ).GT.0.8)JSPK=13          ;; "I DON'T UNDERSTAND THAT!"
	CALL SPEAK(JSPK)                   ;; Print the message
	LTRUBL=LTRUBL+1                    ;; Bump the "bad input" count
	IF(LTRUBL.NE.3)GOTO 2020           ;; Not 3 times, Go back to continue input

	IF(J.NE.13.OR.IPLACE(7).NE.13.OR.IPLACE(5).NE.-1)GOTO 2032  ;; Is this where the bird is? No ... move on
	CALL YES(18,19,54,YEA)             ;; "TRYING TO CATCH THE BIRD?", yes:"THE BIRD IS FRIGHTENED", no:"OK"
	GOTO 2033

2032	IF(J.NE.19.OR.PROP(11).NE.0.OR.IPLACE(7).EQ.-1)GOTO 2034
	CALL YES(20,21,54,YEA)             ;; "TRYING TO ATTACK OR AVOID THE SNAKE", yes:"YOU CAN'T", no:"OK"
	GOTO 2033

2034	IF(J.NE.8.OR.PROP(GRATE).NE.0)GOTO 2035 ;; Is this where the locked grate is? No ... move on
	CALL YES(62,63,54,YEA)             ;; "ARE YOU TRYING TO GET INTO THE CAVE", yes:"THE GRATE IS VERY SOLID", no:"OK"

2033	IF(YEA.EQ.0)GOTO 2011          ;; Not tyring those special things? Go back for new input
	GOTO 2020                          ;; Go back to continue input

2035	IF(IPLACE(5).NE.J.AND.IPLACE(5).NE.-1)GOTO 2020 ;; ROD is not here, back to input
	IF(JOBJ.NE.5)GOTO 2020             ;; Noun is not the ROD, back to input
	CALL SPEAK(22)                     ;; "MY WORD FOR HITTING SOMETHING WITH THE ROD IS 'STRIKE'."
	GOTO 2020                          ;; Go back to continue input

;; Errors for transitive verb without a noun
2036	GOTO(2037,5062,5062,9403,2009,9403,9404,9406,5062,5062,
	1 5200,5300,5062,5062,5062,5062)JVERB
	PAUSE 'OOPS'

;; ERROR 1=GET but no object
;;
2037	IF((IOBJ(J).EQ.0).OR.(ICHAIN(IOBJ(J)).NE.0)) GOTO 5062 ;; TODO ?? list of objects in room
	DO 5312 I=1,3
	IF(DSEEN(I).NE.0)GOTO 5062         ;; TODO Try "E" from 1st room then "GET" or "CAPTURE" with no object.
5312	CONTINUE
	JOBJ=IOBJ(J)                       ;; TODO Automatically use this object ??
	GOTO 2027                          ;; Handler for verb

;; ERROR 2=DROP but no object (also 3=DUMMY)
;; 
5062	IF(B.NE.' ')GOTO 5333          ;; Verb word has 10 characters (like "CAPTUre")
	TYPE 5063,A                        ;; Print error for 5 char ...
5063	FORMAT('  ',A5,' WHAT?',/)     ;; ... verb with no noun. Try "DROP" with no object.
	GOTO 2020                          ;; Go back to continue input
5333	TYPE 5334,A,B                  ;; Print error for 10 char ... 
5334	FORMAT(' ',2A5,' WHAT?',/)     ;;; ... verb with no noun. Try "RELEASE" with no object
	GOTO 2020                          ;; Go back to continue input


;; PROCESS SINGLE WORD VERBS (movement commands) K has the verb number
;;
5014	IF(IDARK.EQ.0) GOTO 8          ;; We have light, go handle the move

	IF(RAN(QZ).GT.0.25) GOTO 8         ;; 3/4ths of the time, the move is ok
5017	CALL SPEAK(23)                 ;; "YOU FELL INTO A PIT" the other 1/4th, you die in the dark
	PAUSE 'GAME IS OVER'               ;; The pause allows the user to end the program (no other way to exit? TODO)
	GOTO 2011                          ;; Go back for new input


;; PROCESS NOUN
;;
5000	JOBJ=K                                             ;; Note the decoded noun (if any)
	IF(TWOWDS.NE.0)GOTO 2028                               ;; There is a word after the noun, go parse it

;; Code bug!
;; If the verb is 2nd, like "LAMP GET", we never make the following check if the object is in
;; the room or the pack. The GET routine expects this to have been made. If it sees the object
;; is not in the room, it assumes you are carying it and says "YOU ARE ALREADY CARYING IT." even
;; when you aren't. Try "LAMP GET" or "ROD GET" or "FISSURE GET".
;;
;; If you try "STEPS GET" you'll be surprised! The "STEPS" listed in the noun list is shadowed by
;; the "STEPS" in the verb list. The code sees "STEPS" as a movement, not a noun.
;;
	IF((J.EQ.IPLACE(K)).OR.(IPLACE(K).EQ.-1)) GOTO 5004    ;; The requested object is here (room or pack), keep it
	IF(K.NE.GRATE)GOTO 502                                 ;; Not the GRATE, move on

	IF((J.EQ.1).OR.(J.EQ.4).OR.(J.EQ.7))GOTO 5098          ;; "GRATE" translates to "DEPREssion" in rooms 1, 4, and 7 
	IF((J.GT.9).AND.(J.LT.15))GOTO 5097                    ;; "GRATE" translates to "ENTRAnce" in rooms 10, 11, 12, 13, and 14

502	IF(B.NE.' ')GOTO 5316                                  ;; Noun word has 10 characters ("BOTTLe" for instance)
	TYPE 5005,A                                            ;; Error for 5 character ...
5005	FORMAT(' I SEE NO ',A5,' HERE.',/)                 ;; ... noun not in room or pack
	GOTO 2011                                              ;; Go back for new input
5316	TYPE 5317,A,B                                      ;; Error for 10 character ...
5317	FORMAT(' I SEE NO ',2A5,' HERE.'/)                 ;; ... noun not in room or pack
	GOTO 2011                                              ;; Go back for new input
5098	K=49                                               ;; Change word to "DEPREssion"
	GOTO 5014                                              ;; Process the "DEPRE" as a verb (move to TODO)
5097	K=50                                               ;; Change word to "ENTRAnce"
	GOTO 5014                                              ;; Process the "ENTRAnce" as a verb (move to TODO)
5004	JOBJ=K                                             ;; Remember the validated noun word

	IF(JVERB.NE.0)GOTO 2027                                    ;; If we have a transitive verb, go handle it
5064	IF(B.NE.' ')GOTO 5314                                  ;; Noun word has 10 characters ("BOTTLe" for instance)
	TYPE 5001,A                                                ;; Error for 5 character ... 
5001	FORMAT(' WHAT DO YOU WANT TO DO WITH THE ',A5,'?',/)   ;; ... noun without a verb
	GOTO 2020                                                  ;; Go back to continue input
5314	TYPE 5315,A,B                                          ;; Error for 10 character ...
5315	FORMAT(' WHAT DO YOU WANT TO DO WITH THE ',2A5,'?',/)  ;; ... noun without a verb
	GOTO 2020                                                  ;; Go back to continue input


C CARRY

;; Interesting. You don't have to be carying the cage to put the bird in it. It can be in the room.
;; "@;EAST;GET LAMP;LAMP ON;GET KEYS;WEST;GRATE" You are transported to the entrance
;; "UNLOCK GRATE;DOWN;WEST;GET CAGE;WEST;WEST;WEST" The bird is in this room
;; "DROP CAGE;LOOK" You see the bird and the cage
;; "GET BIRD;LOOK" The bird is no longer in the room (it is in the cage)
;;
9000	IF(JOBJ.EQ.18)GOTO 2009                                ;; Is this the KNIFE? Print OK and next input. Try "GET KNIFE"

;; Bad assumption here. When you type "GET object", the noun parser makes sure that the object is in the pack or the room.
;; The object is either in the room (and we continue on processing it), or it is not in the room and must
;; be in the pack. The default message printed by the GOTO is "YOU ARE ALREADY CARYING IT."
;;
;; But when you type "object GET", the noun parser skips checking if the object is in the room or pack. This same IF
;; check fails and you see "ALREADY CARYING IT" even when you aren't. Try "LAMP GET".
;;
	IF(IPLACE(JOBJ).NE.J) GOTO 5200                            ;; The object isn't here. Print the !! incorrect error "ALREADY CARYING IT"
9001	IF(IFIXED(JOBJ).EQ.0)GOTO 9002                         ;; Is the object gettable? Yes, continue on
	CALL SPEAK(25)                                             ;; "YOU CAN'T BE SERIOUS!" Try "GRATE" then "GET GRATE".
	GOTO 2011                                                  ;; Go back for new input
9002	IF(JOBJ.NE.BIRD)GOTO 9004                              ;; Not the bird, skip the checks
	IF(IPLACE(ROD).NE.-1)GOTO 9003                             ;; Rod is not in pack, continue on
	CALL SPEAK(26)                                             ;; "YOU CANNOT CATCH IT." Not with the ROD in your pack.
	GOTO 2011                                                  ;; Go back for new input
9003	IF((IPLACE(4).EQ.-1).OR.(IPLACE(4).EQ.J)) GOTO 9004    ;; Is the CAGE in this room or the pack? Yes, go capture the bird
	CALL SPEAK(27)                                             ;; "YOU CANNOT CARRY IT." without the cage
	GOTO 2011                                                  ;; Go back for new input

;; Add the object to the chain of things we have
;;
9004	IPLACE(JOBJ)=-1                                        ;; The object is no longer in this room
9005	IF(IOBJ(J).NE.JOBJ) GOTO 9006
	IOBJ(J)=ICHAIN(JOBJ)
	GOTO 2009                                                  ;; Print "OK" and next input
9006	ITEMP=IOBJ(J)
9007	IF(ICHAIN(ITEMP).EQ.(JOBJ)) GOTO 9008
	ITEMP=ICHAIN(ITEMP)
	GOTO 9007
9008	ICHAIN(ITEMP)=ICHAIN(JOBJ)
	GOTO 2009                                                  ;; Print "OK" and next input


C LOCK, UNLOCK, NO OBJECT YET

9403	IF((J.EQ.8).OR.(J.EQ.9))GOTO 5105           ;; In room 8 or 9, the target is always the grate. Try "E;GET KEYS;W;GRATE;UNLOCK BIRD"
5032	CALL SPEAK(28)                              ;; "THERE IS NOTHING HERE WITH A LOCK!"
	GOTO 2011                                       ;; Go back for new input
5105	JOBJ=GRATE                                  ;; Change the object to the GRATE in this room
	GOTO 2027                                       ;; Do the UNLOCK again with the GRATE

C DISCARD OBJECT

5066	IF(JOBJ.EQ.18)GOTO 2009                                           ;; For KNIFE print "OK" and next input
	IF(IPLACE(JOBJ).NE.-1) GOTO 5200                                      ;; If the object is not in the pack, error and next input

5012	IF((JOBJ.NE.BIRD).OR.(J.NE.19).OR.(PROP(11).EQ.1))GOTO 9401       ;; DROP BIRD in room 19 with snake, anything else continue at 9401
	CALL SPEAK(30)                                                        ;; Print "DRIVES THE SNAKE AWAY."
	PROP(11)=1                                                            ;; Snake is now gone
5160	ICHAIN(JOBJ)=IOBJ(J)                                              ;; Move ...
	IOBJ(J)=JOBJ                                                          ;; ... object ...
	IPLACE(JOBJ)=J                                                        ;; ... to this room
	GOTO 2011                                                             ;; Go back for new input

9401	CALL SPEAK(54)                                                    ;; "OK"
	GOTO 5160                                                             ;; Do the drop

C LOCK,UNLOCK OBJECT

5031	IF(IPLACE(KEYS).NE.-1.AND.IPLACE(KEYS).NE.J)GOTO 5200                ;; Error if we don't have the keys
	IF(JOBJ.NE.4)GOTO 5102                                                   ;; If target is the CAGE ...
	CALL SPEAK(32)                                                           ;; ... print "IT HAS NO LOCK."
	GOTO 2011                                                                ;; Go back for new input
5102	IF(JOBJ.NE.KEYS)GOTO 5104                                            ;; If target is the KEYS ...
	CALL SPEAK(55)                                                           ;; ... print "YOU CAN'T UNLOCK THE KEYS."
	GOTO 2011                                                                ;; Go back for new input
5104	IF(JOBJ.EQ.GRATE)GOTO 5107                                           ;; If object is NOT the GRATE ...
	CALL SPEAK(33)                                                           ;; ... print "I DON'T KNOW HOW TO LOCK OR UNLOCK SUCH A THING."
	GOTO 2011                                                                ;; Go back for new input
;;
5107	IF(JVERB.EQ.4) GOTO 5033                                             ;; Go handle UNLOCK GRATE at 5033
	IF(PROP(GRATE).NE.0)GOTO 5034                                            ;; If the GRATE is already locked ...
	CALL SPEAK(34)                                                           ;; ... print "THE GRATE WAS ALREADY LOCKED."
	GOTO 2011                                                                ;; Go back for new input
5034	CALL SPEAK(35)                                                       ;; "THE GRATE IS NOW LOCKED."
	PROP(GRATE)=0                                                            ;; 0 means LOCKED
	PROP(8)=0                                                                ;; ?? Other side of grate? No noun with 8
	GOTO 2011                                                                ;; Go back for new input

5033	IF(PROP(GRATE).EQ.0)GOTO 5109                                        ;; If the GRATE is already unlocked ...
	CALL SPEAK(36)                                                           ;; ... print "THE GRATE WAS ALREADY UNLOCKED."
	GOTO 2011                                                                ;; Go back for new input
5109	CALL SPEAK(37)                                                       ;; Print "THE GRATE IS NOW UNLOCKED."
	PROP(GRATE)=1                                                            ;; 1 means UNLOCKED
	PROP(8)=1                                                                ;; ?? Other side of grate? No noun with 8
	GOTO 2011                                                                ;; Go back for new input



C LIGHT LAMP

9404	IF((IPLACE(2).NE.J).AND.(IPLACE(2).NE.-1))GOTO 5200  ;; Error if the LAMP is not in pack or room
	PROP(2)=1                                                ;; 1 means ON
	IDARK=0                                                  ;; No longer dark (the lamp is on)
	CALL SPEAK(39)                                           ;; Print "YOUR LAMP IS NOW ON."
	GOTO 2011                                                ;; Go back for new input

C LAMP OFF

9406	IF((IPLACE(2).NE.J).AND.(IPLACE(2).NE.-1)) GOTO 5200
	PROP(2)=0
	CALL SPEAK(40) ;; "YOUR LAMP IS NOW OFF."
	GOTO 2011 ;; Go back for new input

C STRIKE

5081	IF(JOBJ.NE.12)GOTO 5200
	PROP(12)=1
	GOTO 2003

C ATTACK

5300	DO 5313 ID=1,3
	IID=ID
	IF(DSEEN(ID).NE.0)GOTO 5307
5313	CONTINUE
	IF(JOBJ.EQ.0)GOTO 5062
	IF(JOBJ.EQ.SNAKE) GOTO 5200
	IF(JOBJ.EQ.BIRD) GOTO 5302
	CALL SPEAK(44) ;; "THERE IS NOTHING HERE TO ATTACK."
	GOTO 2011 ;; Go back for new input
5302	CALL SPEAK(45) ;; "THE LITTLE BIRD IS NOW DEAD."
	IPLACE(JOBJ)=300
	GOTO 9005

5307	IF(RAN(QZ).GT.0.4) GOTO 5309
	DSEEN(IID)=0
	ODLOC(IID)=0
	DLOC(IID)=0
	CALL SPEAK(47)  ;; "YOU KILLED A LITTLE DWARF."
	GOTO 5311       
5309	CALL SPEAK(48)  ;; "HE DODGES OUT OF THE WAY."
5311	K=21
	GOTO 5014

C EAT

5502	IF((IPLACE(FOOD).NE.J.AND.IPLACE(FOOD).NE.-1).OR.PROP(FOOD).NE.0
	1 .OR.JOBJ.NE.FOOD)GOTO 5200
	PROP(FOOD)=1
5501	JSPK=72
	GOTO 5200

C DRINK

5504	IF((IPLACE(WATER).NE.J.AND.IPLACE(WATER).NE.-1)
	1 .OR.PROP(WATER).NE.0.OR.JOBJ.NE.WATER) GOTO 5200
	PROP(WATER)=1
	JSPK=74
	GOTO 5200

C RUB

5505	IF(JOBJ.NE.LAMP)JSPK=76
	GOTO 5200

C POUR

5506	IF(JOBJ.NE.WATER)JSPK=78
	PROP(WATER)=1
	GOTO 5200



	END


	SUBROUTINE SPEAK(IT)
	IMPLICIT INTEGER(A-Z)
	COMMON RTEXT,LLINE
	DIMENSION RTEXT(100),LLINE(1000,22)

	KKT=RTEXT(IT)
	IF(KKT.EQ.0)RETURN
999	TYPE 998, (LLINE(KKT,JJT),JJT=3,LLINE(KKT,2))
998	FORMAT(20A5)
	KKT=KKT+1
	IF(LLINE(KKT-1,1).NE.0)GOTO 999
997	TYPE 996
996	FORMAT(/)
	RETURN
	END

    ;; TWOW= 0 for one word, 1 for two words
    ;; B=    1st word (up to 5 characters)
	;; C=    2nd word (up to 5 characters) 
	;; D=    2nd 5 characters entered (available for error messages)
	;; - No leading spaces are allowed
	;; - Spaces between 1st and 2nd word are ignored
	;; - There must be 1 space to end the 2nd word
	;; - All characters after 2nd are ignored

	SUBROUTINE GETIN(TWOW,B,C,D)
	IMPLICIT INTEGER(A-Z)
	DIMENSION A(5),M2(6)
	DATA M2/"4000000000,"20000000,"100000,"400,"2,0/       ;; 7-bit mask positions
6	ACCEPT 1,(A(I), I=1,4)                                 ;; Get 20 characters of input into ...
1	FORMAT(4A5)                                            ;; ... four memory locations
	TWOW=0                                                 ;; Not two-words
	S=0                                                    ;; 0 if in first word, 1 if in second word
	B=A(1)                                                 ;; First word is first 5 characters (strip space later)
;;
	DO 2 J=1,4                                             ;; Loop J over 4 input variables
	DO 2 K=1,5                                             ;; Loop K over 5 digits per variable
	MASK1="774000000000                                    ;; 1111111_0000000_0000000_0000000_0000000_0 single character mask for 1st
	IF(K.NE.1) MASK1="177*M2(K)                            ;; 1111111 make mask of the right character (2nd, 3rd, 4th, or 5th)
	IF(((A(J).XOR."201004020100).AND.MASK1).EQ.0)GOTO 3    ;; (ASCII space in all 5 slots) Is the character a space? yes ... start/end 2nd word
;;
;; non-space character
;;
	IF(S.EQ.0) GOTO 2                                      ;; Still in first word ... continue (looking for a space)
	TWOW=1                                                 ;; Note that we found a second word
	CALL SHIFT(A(J),7*(K-1),XX)                            ;; Shift ...
	CALL SHIFT(A(J+1),7*(K-6),YY)                          ;; ... second word ...
	MASK=-M2(6-K)                                          ;; ... into ...
	C=(XX.AND.MASK)+(YY.AND.(-2-MASK))                     ;; ... C (might get typed garbage on the end! -- "GET ROD NOW" vs "GET ROD  NOW")
	GOTO 4                                                 ;; Done 
;;
;; Found a space
;;
3	IF(S.EQ.1) GOTO 2                                      ;; Already in 2nd word? Yes ... continue
	S=1                                                    ;; Starting 2nd word
	IF(J.EQ.1) B=(B.AND.-M2(K)).OR.("201004020100.AND.     ;; Trim off trailing space ...
	1 (-M2(K).XOR.-1))                                     ;; ... from 1st word
2	CONTINUE                                               ;; loop over K then J
;;
4	D=A(2)                                                 ;; return the 2nd 5 characters as is (for error messages)
	RETURN                                                 ;; Done
	END

;; Print the prompt and ask for input. If "NO", print Z.
;; If "YES" print Y.
;;
	SUBROUTINE YES(X,Y,Z,YEA)
	IMPLICIT INTEGER(A-Z)
	CALL SPEAK(X)                                          ;; Print the prompt
	CALL GETIN(JUNK,IA1,JUNK,IB1)                          ;; Only interested in the 1st word
	IF(IA1.EQ.'NO'.OR.IA1.EQ.'N') GOTO 1                   ;; "N" or "NO" means no
	YEA=1                                                  ;; Everything else means yes
	IF(Y.NE.0) CALL SPEAK(Y)                               ;; If there is a message for "yes", print it
	RETURN                                                 ;; Done
1	YEA=0                                                  ;; Return no
	IF(Z.NE.0)CALL SPEAK(Z)                                ;; If there is a message for "no", print it
	RETURN                                                 ;; Done
	END

	SUBROUTINE SHIFT (VAL,DIST,RES)
	IMPLICIT INTEGER (A-Z)
	RES=VAL
	IF(DIST)10,20,30
;;
;; Shift right
10	IDIST=-DIST                            ;; Positive number of shifts
	DO 11 I=1,IDIST                        ;; Loop over all bit positions
	J = 0                                  ;; 0000_00..00 when upper bit is 0
	IF (RES.LT.0) J="200000000000          ;; 0100_00..00 when upper bit is 1
11	RES = ((RES.AND."377777777777)/2) + J  ;; 0111_11..11 drop upper bit, shift others by 2, and add in upper bit shifted
20	RETURN                                 ;; Done
;;
;; Shift left
30	DO 31 I=1,DIST                                    ;; Loop over all bit positions
	j = 0                                             ;; 0000_00..00 when next to MSB is 0
	IF ((RES.AND."200000000000).NE.0) J="400000000000 ;; 0100_00..00, 1000_00..00
31	RES = (RES.AND."177777777777)*2 + J               ;; 0011_11..11
	RETURN                                            ;; Done
	END
