![TRS-80 RaakaTu](trs80raakatu.jpg)

# Raaka-Tu

>>> cpu Z80

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

# Start

```code
4300: 31 FF 7F       LD      SP,$7FFF        
4303: 21 80 3F       LD      HL,$3F80        
4306: 22 20 40       LD      ($4020),HL      
4309: 3E 1D          LD      A,$1D           
430B: 32 20 50       LD      ($5020),A       
430E: 3E 96          LD      A,$96           
4310: 47             LD      B,A             
4311: 32 23 50       LD      ($5023),A       
4314: 21 1F 68       LD      HL,$681F        
4317: CD ED 46       CALL    $46ED           
431A: 22 24 50       LD      ($5024),HL      
431D: CD D0 49       CALL    $49D0           
4320: 31 FF 7F       LD      SP,$7FFF        
4323: CD 8F 47       CALL    $478F           
4326: 97             SUB     A               
4327: 32 05 50       LD      ($5005),A       
432A: 32 08 50       LD      ($5008),A       
432D: 32 0A 50       LD      ($500A),A       
4330: 32 00 50       LD      ($5000),A       
4333: 32 01 50       LD      ($5001),A       
4336: 32 07 50       LD      ($5007),A       
4339: 32 06 50       LD      ($5006),A       
433C: 32 02 50       LD      ($5002),A       
433F: 32 03 50       LD      ($5003),A       
4342: 32 0D 50       LD      ($500D),A       
4345: 32 11 50       LD      ($5011),A       
4348: 32 17 50       LD      ($5017),A       
434B: 3E 1D          LD      A,$1D           
434D: 32 20 50       LD      ($5020),A       
4350: 47             LD      B,A             
4351: CD 83 4E       CALL    $4E83           
4354: 22 21 50       LD      ($5021),HL      
4357: CD 05 47       CALL    $4705           
435A: 7E             LD      A,(HL)          
435B: 32 23 50       LD      ($5023),A       
435E: 47             LD      B,A             
435F: 21 1F 68       LD      HL,$681F        
4362: CD ED 46       CALL    $46ED           
4365: 22 24 50       LD      ($5024),HL      
4368: 21 47 50       LD      HL,$5047        
436B: 22 26 50       LD      ($5026),HL      
436E: 36 00          LD      (HL),$00        
4370: 21 C0 3F       LD      HL,$3FC0        
4373: CD E2 47       CALL    $47E2           
4376: CA 89 43       JP      Z,$4389         
4379: 7E             LD      A,(HL)          
437A: FE 20          CP      $20             
437C: CA 73 43       JP      Z,$4373         
437F: 7D             LD      A,L             
4380: FE FF          CP      $FF             
4382: CA 89 43       JP      Z,$4389         
4385: 23             INC     HL              
4386: C3 79 43       JP      $4379           
4389: 7D             LD      A,L             
438A: FE FF          CP      $FF             
438C: C2 73 43       JP      NZ,$4373        
438F: 2A 26 50       LD      HL,($5026)      
4392: 36 00          LD      (HL),$00        
4394: 21 47 50       LD      HL,$5047        
4397: 7E             LD      A,(HL)          
4398: A7             AND     A               
4399: CA 39 44       JP      Z,$4439         
439C: FE 02          CP      $02             
439E: C2 AF 43       JP      NZ,$43AF        
43A1: 23             INC     HL              
43A2: 7E             LD      A,(HL)          
43A3: 2B             DEC     HL              
43A4: FE 06          CP      $06             
43A6: D2 AF 43       JP      NC,$43AF        
43A9: 32 06 50       LD      ($5006),A       
43AC: 23             INC     HL              
43AD: 23             INC     HL              
43AE: 23             INC     HL              
43AF: 7E             LD      A,(HL)          
43B0: 23             INC     HL              
43B1: A7             AND     A               
43B2: CA 39 44       JP      Z,$4439         
43B5: 46             LD      B,(HL)          
43B6: 23             INC     HL              
43B7: 4E             LD      C,(HL)          
43B8: 23             INC     HL              
43B9: E5             PUSH    HL              
43BA: 3D             DEC     A               
43BB: C2 E2 43       JP      NZ,$43E2        
43BE: 21 B7 50       LD      HL,$50B7        
43C1: CD ED 46       CALL    $46ED           
43C4: D2 DB 43       JP      NC,$43DB        
43C7: CD 05 47       CALL    $4705           
43CA: CD 19 47       CALL    $4719           
43CD: D2 DB 43       JP      NC,$43DB        
43D0: 3A 01 50       LD      A,($5001)       
43D3: BE             CP      (HL)            
43D4: 23             INC     HL              
43D5: 7E             LD      A,(HL)          
43D6: 23             INC     HL              
43D7: C2 CA 43       JP      NZ,$43CA        
43DA: 47             LD      B,A             
43DB: 78             LD      A,B             
43DC: 32 01 50       LD      ($5001),A       
43DF: C3 35 44       JP      $4435           
43E2: 3D             DEC     A               
43E3: C2 1F 44       JP      NZ,$441F        
43E6: 3A 03 50       LD      A,($5003)       
43E9: A7             AND     A               
43EA: CA 0D 44       JP      Z,$440D         
43ED: 21 17 50       LD      HL,$5017        
43F0: 70             LD      (HL),B          
43F1: 23             INC     HL              
43F2: 3A 05 50       LD      A,($5005)       
43F5: 77             LD      (HL),A          
43F6: 23             INC     HL              
43F7: 3A 08 50       LD      A,($5008)       
43FA: 77             LD      (HL),A          
43FB: A7             AND     A               
43FC: C2 00 44       JP      NZ,$4400        
43FF: 71             LD      (HL),C          
4400: 97             SUB     A               
4401: 32 05 50       LD      ($5005),A       
4404: 32 03 50       LD      ($5003),A       
4407: 32 08 50       LD      ($5008),A       
440A: C3 35 44       JP      $4435           
440D: 2A 11 50       LD      HL,($5011)      
4410: 22 17 50       LD      ($5017),HL      
4413: 3A 13 50       LD      A,($5013)       
4416: 32 19 50       LD      ($5019),A       
4419: 21 11 50       LD      HL,$5011        
441C: C3 F0 43       JP      $43F0           
441F: 3D             DEC     A               
4420: C2 2E 44       JP      NZ,$442E        
4423: 78             LD      A,B             
4424: 32 05 50       LD      ($5005),A       
4427: 79             LD      A,C             
4428: 32 08 50       LD      ($5008),A       
442B: C3 35 44       JP      $4435           
442E: 78             LD      A,B             
442F: 32 02 50       LD      ($5002),A       
4432: 32 03 50       LD      ($5003),A       
4435: E1             POP     HL              
4436: C3 AF 43       JP      $43AF           
4439: 3A 01 50       LD      A,($5001)       
443C: A7             AND     A               
443D: CA 85 46       JP      Z,$4685         
4440: 21 17 50       LD      HL,$5017        
4443: CD 2A 45       CALL    $452A           
4446: 22 1A 50       LD      ($501A),HL      
4449: 21 11 50       LD      HL,$5011        
444C: CD 2A 45       CALL    $452A           
444F: 22 14 50       LD      ($5014),HL      
4452: 97             SUB     A               
4453: 32 03 50       LD      ($5003),A       
4456: 2A 14 50       LD      HL,($5014)      
4459: 3A 11 50       LD      A,($5011)       
445C: A7             AND     A               
445D: CA 66 44       JP      Z,$4466         
4460: CD 05 47       CALL    $4705           
4463: 23             INC     HL              
4464: 23             INC     HL              
4465: 7E             LD      A,(HL)          
4466: 32 16 50       LD      ($5016),A       
4469: 2A 1A 50       LD      HL,($501A)      
446C: 3A 17 50       LD      A,($5017)       
446F: A7             AND     A               
4470: CA 79 44       JP      Z,$4479         
4473: CD 05 47       CALL    $4705           
4476: 23             INC     HL              
4477: 23             INC     HL              
4478: 7E             LD      A,(HL)          
4479: 32 1C 50       LD      ($501C),A       
447C: 21 B9 50       LD      HL,$50B9        
447F: 7E             LD      A,(HL)          
4480: A7             AND     A               
4481: CA 3B 46       JP      Z,$463B         
4484: 3A 01 50       LD      A,($5001)       
4487: BE             CP      (HL)            
4488: 23             INC     HL              
4489: C2 EB 44       JP      NZ,$44EB        
448C: 7E             LD      A,(HL)          
448D: 32 04 50       LD      ($5004),A       
4490: 3A 02 50       LD      A,($5002)       
4493: A7             AND     A               
4494: CA 9B 44       JP      Z,$449B         
4497: BE             CP      (HL)            
4498: C2 EB 44       JP      NZ,$44EB        
449B: 23             INC     HL              
449C: 7E             LD      A,(HL)          
449D: A7             AND     A               
449E: CA B7 44       JP      Z,$44B7         
44A1: 3A 11 50       LD      A,($5011)       
44A4: A7             AND     A               
44A5: C2 BE 44       JP      NZ,$44BE        
44A8: 3A 0A 50       LD      A,($500A)       
44AB: 32 0B 50       LD      ($500B),A       
44AE: 11 11 50       LD      DE,$5011        
44B1: CD CB 45       CALL    $45CB           
44B4: C3 BE 44       JP      $44BE           
44B7: 3A 11 50       LD      A,($5011)       
44BA: A7             AND     A               
44BB: C2 3B 46       JP      NZ,$463B        
44BE: 23             INC     HL              
44BF: 7E             LD      A,(HL)          
44C0: A7             AND     A               
44C1: CA DF 44       JP      Z,$44DF         
44C4: 3A 17 50       LD      A,($5017)       
44C7: A7             AND     A               
44C8: C2 E6 44       JP      NZ,$44E6        
44CB: 3A 09 50       LD      A,($5009)       
44CE: 32 0B 50       LD      ($500B),A       
44D1: 3E 01          LD      A,$01           
44D3: 32 03 50       LD      ($5003),A       
44D6: 11 17 50       LD      DE,$5017        
44D9: CD CB 45       CALL    $45CB           
44DC: C3 E6 44       JP      $44E6           
44DF: 3A 17 50       LD      A,($5017)       
44E2: A7             AND     A               
44E3: C2 3B 46       JP      NZ,$463B        
44E6: 23             INC     HL              
44E7: 7E             LD      A,(HL)          
44E8: C3 F2 44       JP      $44F2           
44EB: 23             INC     HL              
44EC: 23             INC     HL              
44ED: 23             INC     HL              
44EE: 23             INC     HL              
44EF: C3 7F 44       JP      $447F           
44F2: 32 1F 50       LD      ($501F),A       
44F5: 21 FF 3F       LD      HL,$3FFF        
44F8: 22 20 40       LD      ($4020),HL      
44FB: 3E 0D          LD      A,$0D           
44FD: CD 0D 4F       CALL    $4F0D           
4500: 3A 11 50       LD      A,($5011)       
4503: A7             AND     A               
4504: C2 13 45       JP      NZ,$4513        
4507: 2A 1A 50       LD      HL,($501A)      
450A: 22 14 50       LD      ($5014),HL      
450D: 3A 17 50       LD      A,($5017)       
4510: 32 11 50       LD      ($5011),A       
4513: 21 FB 73       LD      HL,$73FB        
4516: CD 05 47       CALL    $4705           
4519: CD 94 48       CALL    $4894           
451C: CD D5 4B       CALL    $4BD5           
451F: 3E 0D          LD      A,$0D           
4521: CD 0D 4F       CALL    $4F0D           
4524: 3A 1F 50       LD      A,($501F)       
4527: C3 20 43       JP      $4320           
452A: 97             SUB     A               
452B: 32 0D 50       LD      ($500D),A       
452E: 7E             LD      A,(HL)          
452F: 32 00 50       LD      ($5000),A       
4532: 47             LD      B,A             
4533: A7             AND     A               
4534: C8             RET     Z               
4535: 23             INC     HL              
4536: 7E             LD      A,(HL)          
4537: 32 05 50       LD      ($5005),A       
453A: 23             INC     HL              
453B: 7E             LD      A,(HL)          
453C: 32 1D 50       LD      ($501D),A       
453F: 21 51 56       LD      HL,$5651        
4542: CD ED 46       CALL    $46ED           
4545: D2 97 45       JP      NC,$4597        
4548: D5             PUSH    DE              
4549: E5             PUSH    HL              
454A: CD A6 45       CALL    $45A6           
454D: C2 A2 45       JP      NZ,$45A2        
4550: 3A 05 50       LD      A,($5005)       
4553: A7             AND     A               
4554: CA 79 45       JP      Z,$4579         
4557: E1             POP     HL              
4558: E5             PUSH    HL              
4559: CD 05 47       CALL    $4705           
455C: 01 03 00       LD      BC,$0003        
455F: 09             ADD     HL,BC           
4560: 06 01          LD      B,$01           
4562: CD F1 46       CALL    $46F1           
4565: D2 79 45       JP      NC,$4579        
4568: CD 05 47       CALL    $4705           
456B: CD 19 47       CALL    $4719           
456E: D2 A2 45       JP      NC,$45A2        
4571: 3A 05 50       LD      A,($5005)       
4574: BE             CP      (HL)            
4575: 23             INC     HL              
4576: C2 6B 45       JP      NZ,$456B        
4579: E1             POP     HL              
457A: 3A 0D 50       LD      A,($500D)       
457D: A7             AND     A               
457E: C2 7C 46       JP      NZ,$467C        
4581: 7E             LD      A,(HL)          
4582: 32 0D 50       LD      ($500D),A       
4585: 22 0E 50       LD      ($500E),HL      
4588: CD 05 47       CALL    $4705           
458B: EB             EX      DE,HL           
458C: D1             POP     DE              
458D: 3A 00 50       LD      A,($5000)       
4590: 47             LD      B,A             
4591: CD F1 46       CALL    $46F1           
4594: DA 48 45       JP      C,$4548         
4597: 3A 0D 50       LD      A,($500D)       
459A: 2A 0E 50       LD      HL,($500E)      
459D: A7             AND     A               
459E: C0             RET     NZ              
459F: C3 32 46       JP      $4632           
45A2: E1             POP     HL              
45A3: C3 88 45       JP      $4588           
45A6: CD 05 47       CALL    $4705           
45A9: 3A 23 50       LD      A,($5023)       
45AC: BE             CP      (HL)            
45AD: C8             RET     Z               
45AE: 7E             LD      A,(HL)          
45AF: A7             AND     A               
45B0: CA C8 45       JP      Z,$45C8         
45B3: 3C             INC     A               
45B4: C8             RET     Z               
45B5: 3D             DEC     A               
45B6: FA C8 45       JP      M,$45C8         
45B9: 46             LD      B,(HL)          
45BA: 3A 20 50       LD      A,($5020)       
45BD: B8             CP      B               
45BE: C8             RET     Z               
45BF: 21 51 56       LD      HL,$5651        
45C2: CD ED 46       CALL    $46ED           
45C5: DA A6 45       JP      C,$45A6         
45C8: F6 01          OR      $01             
45CA: C9             RET                     
45CB: E5             PUSH    HL              
45CC: 97             SUB     A               
45CD: 32 00 50       LD      ($5000),A       
45D0: D5             PUSH    DE              
45D1: 4E             LD      C,(HL)          
45D2: 21 51 56       LD      HL,$5651        
45D5: CD 05 47       CALL    $4705           
45D8: CD 19 47       CALL    $4719           
45DB: D2 16 46       JP      NC,$4616        
45DE: D5             PUSH    DE              
45DF: E5             PUSH    HL              
45E0: CD A6 45       CALL    $45A6           
45E3: E1             POP     HL              
45E4: C2 10 46       JP      NZ,$4610        
45E7: 46             LD      B,(HL)          
45E8: 22 26 50       LD      ($5026),HL      
45EB: CD 05 47       CALL    $4705           
45EE: 23             INC     HL              
45EF: 23             INC     HL              
45F0: 7E             LD      A,(HL)          
45F1: A1             AND     C               
45F2: B9             CP      C               
45F3: C2 0B 46       JP      NZ,$460B        
45F6: 3A 00 50       LD      A,($5000)       
45F9: A7             AND     A               
45FA: C2 44 46       JP      NZ,$4644        
45FD: 78             LD      A,B             
45FE: 32 00 50       LD      ($5000),A       
4601: 7E             LD      A,(HL)          
4602: 32 05 50       LD      ($5005),A       
4605: 2A 26 50       LD      HL,($5026)      
4608: 22 47 50       LD      ($5047),HL      
460B: EB             EX      DE,HL           
460C: D1             POP     DE              
460D: C3 D8 45       JP      $45D8           
4610: CD 05 47       CALL    $4705           
4613: C3 0B 46       JP      $460B           
4616: 3A 00 50       LD      A,($5000)       
4619: A7             AND     A               
461A: CA 44 46       JP      Z,$4644         
461D: D1             POP     DE              
461E: 2A 47 50       LD      HL,($5047)      
4621: 12             LD      (DE),A          
4622: 13             INC     DE              
4623: 13             INC     DE              
4624: 13             INC     DE              
4625: 7D             LD      A,L             
4626: 12             LD      (DE),A          
4627: 13             INC     DE              
4628: 7C             LD      A,H             
4629: 12             LD      (DE),A          
462A: 13             INC     DE              
462B: 3A 05 50       LD      A,($5005)       
462E: 12             LD      (DE),A          
462F: E1             POP     HL              
4630: 97             SUB     A               
4631: C9             RET                     
4632: 11 2F 50       LD      DE,$502F        
4635: 3A 1D 50       LD      A,($501D)       
4638: C3 8A 46       JP      $468A           
463B: 11 3E 50       LD      DE,$503E        
463E: 3A 09 50       LD      A,($5009)       
4641: C3 8A 46       JP      $468A           
4644: 3A 03 50       LD      A,($5003)       
4647: A7             AND     A               
4648: CA 73 46       JP      Z,$4673         
464B: 3A 02 50       LD      A,($5002)       
464E: A7             AND     A               
464F: C2 73 46       JP      NZ,$4673        
4652: 16 00          LD      D,$00           
4654: 21 F8 55       LD      HL,$55F8        
4657: 7E             LD      A,(HL)          
4658: A7             AND     A               
4659: CA 73 46       JP      Z,$4673         
465C: E5             PUSH    HL              
465D: 5E             LD      E,(HL)          
465E: 23             INC     HL              
465F: 19             ADD     HL,DE           
4660: 3A 04 50       LD      A,($5004)       
4663: BE             CP      (HL)            
4664: CA 6C 46       JP      Z,$466C         
4667: 23             INC     HL              
4668: C1             POP     BC              
4669: C3 57 46       JP      $4657           
466C: D1             POP     DE              
466D: 3A 0B 50       LD      A,($500B)       
4670: CD C6 46       CALL    $46C6           
4673: 11 2F 50       LD      DE,$502F        
4676: 3A 0B 50       LD      A,($500B)       
4679: C3 8A 46       JP      $468A           
467C: 11 36 50       LD      DE,$5036        
467F: 3A 1D 50       LD      A,($501D)       
4682: C3 8A 46       JP      $468A           
4685: 11 28 50       LD      DE,$5028        
4688: 3E C0          LD      A,$C0           
468A: 31 FF 7F       LD      SP,$7FFF        
468D: 21 C0 3F       LD      HL,$3FC0        
4690: CD C6 46       CALL    $46C6           
4693: 1A             LD      A,(DE)          
4694: 4F             LD      C,A             
4695: E5             PUSH    HL              
4696: 36 20          LD      (HL),$20        
4698: 23             INC     HL              
4699: 0D             DEC     C               
469A: C2 96 46       JP      NZ,$4696        
469D: CD BB 46       CALL    $46BB           
46A0: E1             POP     HL              
46A1: 05             DEC     B               
46A2: C2 B5 46       JP      NZ,$46B5        
46A5: 1A             LD      A,(DE)          
46A6: 3C             INC     A               
46A7: 4F             LD      C,A             
46A8: CD 9E 47       CALL    $479E           
46AB: 0D             DEC     C               
46AC: C2 A8 46       JP      NZ,$46A8        
46AF: CD 22 47       CALL    $4722           
46B2: C3 26 43       JP      $4326           
46B5: CD D5 46       CALL    $46D5           
46B8: C3 93 46       JP      $4693           
46BB: 3E 32          LD      A,$32           
46BD: 0D             DEC     C               
46BE: C2 BD 46       JP      NZ,$46BD        
46C1: 3D             DEC     A               
46C2: C2 BD 46       JP      NZ,$46BD        
46C5: C9             RET                     
46C6: 6F             LD      L,A             
46C7: 1A             LD      A,(DE)          
46C8: 3C             INC     A               
46C9: 4F             LD      C,A             
46CA: D5             PUSH    DE              
46CB: CD B5 47       CALL    $47B5           
46CE: 0D             DEC     C               
46CF: C2 CB 46       JP      NZ,$46CB        
46D2: D1             POP     DE              
46D3: 06 08          LD      B,$08           
46D5: 1A             LD      A,(DE)          
46D6: 4F             LD      C,A             
46D7: D5             PUSH    DE              
46D8: E5             PUSH    HL              
46D9: 13             INC     DE              
46DA: 1A             LD      A,(DE)          
46DB: 77             LD      (HL),A          
46DC: 23             INC     HL              
46DD: 13             INC     DE              
46DE: 0D             DEC     C               
46DF: C2 DA 46       JP      NZ,$46DA        
46E2: 2C             INC     L               
46E3: 7D             LD      A,L             
46E4: 32 0B 50       LD      ($500B),A       
46E7: CD BB 46       CALL    $46BB           
46EA: E1             POP     HL              
46EB: D1             POP     DE              
46EC: C9             RET                     
46ED: 23             INC     HL              
46EE: CD 06 47       CALL    $4706           
46F1: CD 19 47       CALL    $4719           
46F4: D0             RET     NC              
46F5: 78             LD      A,B             
46F6: BE             CP      (HL)            
46F7: CA 03 47       JP      Z,$4703         
46FA: D5             PUSH    DE              
46FB: CD 05 47       CALL    $4705           
46FE: EB             EX      DE,HL           
46FF: D1             POP     DE              
4700: C3 F1 46       JP      $46F1           
4703: 37             SCF                     
4704: C9             RET                     
4705: 23             INC     HL              
4706: 16 00          LD      D,$00           
4708: 7E             LD      A,(HL)          
4709: E6 80          AND     $80             
470B: CA 13 47       JP      Z,$4713         
470E: 7E             LD      A,(HL)          
470F: E6 7F          AND     $7F             
4711: 57             LD      D,A             
4712: 23             INC     HL              
4713: 5E             LD      E,(HL)          
4714: 23             INC     HL              
4715: EB             EX      DE,HL           
4716: 19             ADD     HL,DE           
4717: EB             EX      DE,HL           
4718: C9             RET                     
4719: 7C             LD      A,H             
471A: BA             CP      D               
471B: C0             RET     NZ              
471C: 7D             LD      A,L             
471D: BB             CP      E               
471E: C9             RET                     
471F: 21 C0 3F       LD      HL,$3FC0        
4722: CD D0 47       CALL    $47D0           
4725: CD D6 47       CALL    $47D6           
4728: FE 18          CP      $18             
472A: CA 56 47       JP      Z,$4756         
472D: FE 19          CP      $19             
472F: CA 66 47       JP      Z,$4766         
4732: FE 09          CP      $09             
4734: CA 76 47       JP      Z,$4776         
4737: FE 0D          CP      $0D             
4739: CA 8B 47       JP      Z,$478B         
473C: FE 1F          CP      $1F             
473E: CA 8F 47       JP      Z,$478F         
4741: FE 08          CP      $08             
4743: CA 7E 47       JP      Z,$477E         
4746: 47             LD      B,A             
4747: 7D             LD      A,L             
4748: FE FF          CP      $FF             
474A: CA 25 47       JP      Z,$4725         
474D: 78             LD      A,B             
474E: CD B5 47       CALL    $47B5           
4751: 77             LD      (HL),A          
4752: 23             INC     HL              
4753: C3 25 47       JP      $4725           
4756: 7D             LD      A,L             
4757: FE C0          CP      $C0             
4759: CA 25 47       JP      Z,$4725         
475C: 2B             DEC     HL              
475D: 7E             LD      A,(HL)          
475E: 23             INC     HL              
475F: 77             LD      (HL),A          
4760: 2B             DEC     HL              
4761: 36 8F          LD      (HL),$8F        
4763: C3 25 47       JP      $4725           
4766: 7D             LD      A,L             
4767: FE FF          CP      $FF             
4769: CA 25 47       JP      Z,$4725         
476C: 23             INC     HL              
476D: 7E             LD      A,(HL)          
476E: 2B             DEC     HL              
476F: 77             LD      (HL),A          
4770: 23             INC     HL              
4771: 36 8F          LD      (HL),$8F        
4773: C3 25 47       JP      $4725           
4776: CD 9E 47       CALL    $479E           
4779: 36 8F          LD      (HL),$8F        
477B: C3 25 47       JP      $4725           
477E: 7D             LD      A,L             
477F: FE C0          CP      $C0             
4781: CA 25 47       JP      Z,$4725         
4784: 2B             DEC     HL              
4785: CD 9E 47       CALL    $479E           
4788: C3 25 47       JP      $4725           
478B: CD 9E 47       CALL    $479E           
478E: C9             RET                     
478F: 21 C0 3F       LD      HL,$3FC0        
4792: 06 40          LD      B,$40           
4794: 36 20          LD      (HL),$20        
4796: 23             INC     HL              
4797: 05             DEC     B               
4798: C2 94 47       JP      NZ,$4794        
479B: C3 1F 47       JP      $471F           
479E: 54             LD      D,H             
479F: 5D             LD      E,L             
47A0: 45             LD      B,L             
47A1: 36 20          LD      (HL),$20        
47A3: 13             INC     DE              
47A4: 7B             LD      A,E             
47A5: A7             AND     A               
47A6: C8             RET     Z               
47A7: FE 01          CP      $01             
47A9: C8             RET     Z               
47AA: 1A             LD      A,(DE)          
47AB: 77             LD      (HL),A          
47AC: 2C             INC     L               
47AD: 1C             INC     E               
47AE: C2 AA 47       JP      NZ,$47AA        
47B1: 36 20          LD      (HL),$20        
47B3: 68             LD      L,B             
47B4: C9             RET                     
47B5: F5             PUSH    AF              
47B6: 7D             LD      A,L             
47B7: FE FF          CP      $FF             
47B9: CA CE 47       JP      Z,$47CE         
47BC: 45             LD      B,L             
47BD: 21 FF 3F       LD      HL,$3FFF        
47C0: 11 FE 3F       LD      DE,$3FFE        
47C3: 1A             LD      A,(DE)          
47C4: 77             LD      (HL),A          
47C5: 2B             DEC     HL              
47C6: 1B             DEC     DE              
47C7: 7D             LD      A,L             
47C8: B8             CP      B               
47C9: C2 C3 47       JP      NZ,$47C3        
47CC: 36 20          LD      (HL),$20        
47CE: F1             POP     AF              
47CF: C9             RET                     
47D0: CD B5 47       CALL    $47B5           
47D3: 36 8F          LD      (HL),$8F        
47D5: C9             RET                     
47D6: CD D3 4F       CALL    $4FD3           
47D9: CD 2B 00       CALL    $002B           
47DC: A7             AND     A               
47DD: CA D6 47       JP      Z,$47D6         
47E0: C9             RET                     
47E1: 23             INC     HL              
47E2: 7D             LD      A,L             
47E3: 32 1D 50       LD      ($501D),A       
47E6: FE FF          CP      $FF             
47E8: C8             RET     Z               
47E9: 7E             LD      A,(HL)          
47EA: FE 20          CP      $20             
47EC: CA E1 47       JP      Z,$47E1         
47EF: FE 41          CP      $41             
47F1: DA E1 47       JP      C,$47E1         
47F4: 11 C2 52       LD      DE,$52C2        
47F7: CD 2E 48       CALL    $482E           
47FA: CA E2 47       JP      Z,$47E2         
47FD: 06 01          LD      B,$01           
47FF: 13             INC     DE              
4800: CD 2E 48       CALL    $482E           
4803: CA 0F 48       JP      Z,$480F         
4806: 04             INC     B               
4807: 78             LD      A,B             
4808: FE 05          CP      $05             
480A: C2 FF 47       JP      NZ,$47FF        
480D: A7             AND     A               
480E: C9             RET                     
480F: EB             EX      DE,HL           
4810: 2A 26 50       LD      HL,($5026)      
4813: 70             LD      (HL),B          
4814: 23             INC     HL              
4815: 77             LD      (HL),A          
4816: 23             INC     HL              
4817: 3A 1D 50       LD      A,($501D)       
481A: 77             LD      (HL),A          
481B: 23             INC     HL              
481C: 22 26 50       LD      ($5026),HL      
481F: EB             EX      DE,HL           
4820: 78             LD      A,B             
4821: FE 01          CP      $01             
4823: C2 2C 48       JP      NZ,$482C        
4826: 3A 09 50       LD      A,($5009)       
4829: 32 0A 50       LD      ($500A),A       
482C: 97             SUB     A               
482D: C9             RET                     
482E: 1A             LD      A,(DE)          
482F: A7             AND     A               
4830: C2 36 48       JP      NZ,$4836        
4833: F6 01          OR      $01             
4835: C9             RET                     
4836: 4F             LD      C,A             
4837: 32 1E 50       LD      ($501E),A       
483A: E5             PUSH    HL              
483B: 13             INC     DE              
483C: 7E             LD      A,(HL)          
483D: FE 20          CP      $20             
483F: CA 8A 48       JP      Z,$488A         
4842: 7D             LD      A,L             
4843: A7             AND     A               
4844: CA 8A 48       JP      Z,$488A         
4847: 7E             LD      A,(HL)          
4848: FE 41          CP      $41             
484A: D2 51 48       JP      NC,$4851        
484D: 23             INC     HL              
484E: C3 3C 48       JP      $483C           
4851: 1A             LD      A,(DE)          
4852: BE             CP      (HL)            
4853: C2 8A 48       JP      NZ,$488A        
4856: 13             INC     DE              
4857: 23             INC     HL              
4858: 0D             DEC     C               
4859: C2 3C 48       JP      NZ,$483C        
485C: 3A 1E 50       LD      A,($501E)       
485F: FE 06          CP      $06             
4861: CA 6F 48       JP      Z,$486F         
4864: 7E             LD      A,(HL)          
4865: FE 41          CP      $41             
4867: DA 6F 48       JP      C,$486F         
486A: FE 20          CP      $20             
486C: C2 8F 48       JP      NZ,$488F        
486F: 1A             LD      A,(DE)          
4870: D1             POP     DE              
4871: 4F             LD      C,A             
4872: 7E             LD      A,(HL)          
4873: FE 20          CP      $20             
4875: CA 82 48       JP      Z,$4882         
4878: 7D             LD      A,L             
4879: FE FF          CP      $FF             
487B: CA 84 48       JP      Z,$4884         
487E: 23             INC     HL              
487F: C3 72 48       JP      $4872           
4882: 7D             LD      A,L             
4883: 3C             INC     A               
4884: 32 09 50       LD      ($5009),A       
4887: 97             SUB     A               
4888: 79             LD      A,C             
4889: C9             RET                     
488A: 13             INC     DE              
488B: 0D             DEC     C               
488C: C2 8A 48       JP      NZ,$488A        
488F: E1             POP     HL              
4890: 13             INC     DE              
4891: C3 2E 48       JP      $482E           
4894: 7E             LD      A,(HL)          
4895: 47             LD      B,A             
4896: 23             INC     HL              
4897: E6 80          AND     $80             
4899: CA B0 48       JP      Z,$48B0         
489C: E5             PUSH    HL              
489D: D5             PUSH    DE              
489E: 21 CD 7B       LD      HL,$7BCD        
48A1: CD ED 46       CALL    $46ED           
48A4: D2 AD 48       JP      NC,$48AD        
48A7: CD 05 47       CALL    $4705           
48AA: CD 94 48       CALL    $4894           
48AD: D1             POP     DE              
48AE: E1             POP     HL              
48AF: C9             RET                     
48B0: 78             LD      A,B             
48B1: 11 66 50       LD      DE,$5066        
48B4: 07             RLCA                    
48B5: 83             ADD     A,E             
48B6: 5F             LD      E,A             
48B7: 7A             LD      A,D             
48B8: CE 00          ADC     $00             
48BA: 57             LD      D,A             
48BB: 1A             LD      A,(DE)          
48BC: 32 C5 48       LD      ($48C5),A       
48BF: 13             INC     DE              
48C0: 1A             LD      A,(DE)          
48C1: 32 C6 48       LD      ($48C6),A       
48C4: C3 C4 48       JP      $48C4           
48C7: CD 06 47       CALL    $4706           
48CA: CD 19 47       CALL    $4719           
48CD: D2 DA 48       JP      NC,$48DA        
48D0: D5             PUSH    DE              
48D1: CD 94 48       CALL    $4894           
48D4: D1             POP     DE              
48D5: CA CA 48       JP      Z,$48CA         
48D8: EB             EX      DE,HL           
48D9: C9             RET                     
48DA: EB             EX      DE,HL           
48DB: 97             SUB     A               
48DC: C9             RET                     
48DD: CD 06 47       CALL    $4706           
48E0: CD 19 47       CALL    $4719           
48E3: D2 F0 48       JP      NC,$48F0        
48E6: D5             PUSH    DE              
48E7: CD 94 48       CALL    $4894           
48EA: D1             POP     DE              
48EB: C2 E0 48       JP      NZ,$48E0        
48EE: EB             EX      DE,HL           
48EF: C9             RET                     
48F0: EB             EX      DE,HL           
48F1: F6 01          OR      $01             
48F3: C9             RET                     
48F4: CD 06 47       CALL    $4706           
48F7: 46             LD      B,(HL)          
48F8: 23             INC     HL              
48F9: CD 19 47       CALL    $4719           
48FC: D2 F0 48       JP      NC,$48F0        
48FF: D5             PUSH    DE              
4900: C5             PUSH    BC              
4901: 78             LD      A,B             
4902: CD B1 48       CALL    $48B1           
4905: C1             POP     BC              
4906: CA 11 49       JP      Z,$4911         
4909: CD 06 47       CALL    $4706           
490C: EB             EX      DE,HL           
490D: D1             POP     DE              
490E: C3 F9 48       JP      $48F9           
4911: CD 06 47       CALL    $4706           
4914: CD 94 48       CALL    $4894           
4917: E1             POP     HL              
4918: C9             RET                     
4919: CD 23 49       CALL    $4923           
491C: E5             PUSH    HL              
491D: CD D0 49       CALL    $49D0           
4920: E1             POP     HL              
4921: 97             SUB     A               
4922: C9             RET                     
4923: 7E             LD      A,(HL)          
4924: 23             INC     HL              
4925: E5             PUSH    HL              
4926: 32 23 50       LD      ($5023),A       
4929: 47             LD      B,A             
492A: 21 1F 68       LD      HL,$681F        
492D: CD ED 46       CALL    $46ED           
4930: 22 24 50       LD      ($5024),HL      
4933: 2A 21 50       LD      HL,($5021)      
4936: CD 05 47       CALL    $4705           
4939: 3A 23 50       LD      A,($5023)       
493C: 77             LD      (HL),A          
493D: E1             POP     HL              
493E: 97             SUB     A               
493F: C9             RET                     
4940: E5             PUSH    HL              
4941: 2A 14 50       LD      HL,($5014)      
4944: 22 0E 50       LD      ($500E),HL      
4947: 3A 11 50       LD      A,($5011)       
494A: 32 0D 50       LD      ($500D),A       
494D: E1             POP     HL              
494E: 97             SUB     A               
494F: C9             RET                     
4950: E5             PUSH    HL              
4951: 2A 1A 50       LD      HL,($501A)      
4954: 22 0E 50       LD      ($500E),HL      
4957: 3A 17 50       LD      A,($5017)       
495A: 32 0D 50       LD      ($500D),A       
495D: E1             POP     HL              
495E: 97             SUB     A               
495F: C9             RET                     
4960: 46             LD      B,(HL)          
4961: 23             INC     HL              
4962: E5             PUSH    HL              
4963: 78             LD      A,B             
4964: 32 0D 50       LD      ($500D),A       
4967: CD 83 4E       CALL    $4E83           
496A: 22 0E 50       LD      ($500E),HL      
496D: E1             POP     HL              
496E: 97             SUB     A               
496F: C9             RET                     
4970: EB             EX      DE,HL           
4971: 2A 14 50       LD      HL,($5014)      
4974: E5             PUSH    HL              
4975: 2A 1A 50       LD      HL,($501A)      
4978: E5             PUSH    HL              
4979: 3A 11 50       LD      A,($5011)       
497C: 47             LD      B,A             
497D: 3A 17 50       LD      A,($5017)       
4980: 4F             LD      C,A             
4981: C5             PUSH    BC              
4982: 3A 0A 00       LD      A,($000A)       
4985: 47             LD      B,A             
4986: C5             PUSH    BC              
4987: EB             EX      DE,HL           
4988: 7E             LD      A,(HL)          
4989: 32 0A 00       LD      ($000A),A       
498C: 23             INC     HL              
498D: 46             LD      B,(HL)          
498E: 23             INC     HL              
498F: 4E             LD      C,(HL)          
4990: 23             INC     HL              
4991: E5             PUSH    HL              
4992: 78             LD      A,B             
4993: 32 11 50       LD      ($5011),A       
4996: A7             AND     A               
4997: CA A0 49       JP      Z,$49A0         
499A: CD 83 4E       CALL    $4E83           
499D: 22 14 50       LD      ($5014),HL      
49A0: 79             LD      A,C             
49A1: 32 17 50       LD      ($5017),A       
49A4: A7             AND     A               
49A5: CA AE 49       JP      Z,$49AE         
49A8: CD 83 4E       CALL    $4E83           
49AB: 22 1A 50       LD      ($501A),HL      
49AE: 21 FB 73       LD      HL,$73FB        
49B1: CD 05 47       CALL    $4705           
49B4: CD 94 48       CALL    $4894           
49B7: D1             POP     DE              
49B8: C1             POP     BC              
49B9: 78             LD      A,B             
49BA: 32 0A 00       LD      ($000A),A       
49BD: C1             POP     BC              
49BE: 78             LD      A,B             
49BF: 32 11 50       LD      ($5011),A       
49C2: 79             LD      A,C             
49C3: 32 17 50       LD      ($5017),A       
49C6: E1             POP     HL              
49C7: 22 1A 50       LD      ($501A),HL      
49CA: E1             POP     HL              
49CB: 22 14 50       LD      ($5014),HL      
49CE: EB             EX      DE,HL           
49CF: C9             RET                     
49D0: 3A 20 50       LD      A,($5020)       
49D3: FE 1D          CP      $1D             
49D5: C0             RET     NZ              
49D6: 2A 24 50       LD      HL,($5024)      
49D9: CD 05 47       CALL    $4705           
49DC: 23             INC     HL              
49DD: 06 03          LD      B,$03           
49DF: CD F1 46       CALL    $46F1           
49E2: D2 E9 49       JP      NC,$49E9        
49E5: 23             INC     HL              
49E6: CD 9B 4E       CALL    $4E9B           
49E9: 21 51 56       LD      HL,$5651        
49EC: CD 05 47       CALL    $4705           
49EF: D5             PUSH    DE              
49F0: CD 05 47       CALL    $4705           
49F3: 3A 23 50       LD      A,($5023)       
49F6: BE             CP      (HL)            
49F7: C2 0B 4A       JP      NZ,$4A0B        
49FA: 23             INC     HL              
49FB: 23             INC     HL              
49FC: 23             INC     HL              
49FD: 06 03          LD      B,$03           
49FF: CD F1 46       CALL    $46F1           
4A02: D2 0B 4A       JP      NC,$4A0B        
4A05: 23             INC     HL              
4A06: D5             PUSH    DE              
4A07: CD 9B 4E       CALL    $4E9B           
4A0A: D1             POP     DE              
4A0B: EB             EX      DE,HL           
4A0C: D1             POP     DE              
4A0D: CD 19 47       CALL    $4719           
4A10: DA EF 49       JP      C,$49EF         
4A13: C9             RET                     
4A14: 46             LD      B,(HL)          
4A15: 23             INC     HL              
4A16: E5             PUSH    HL              
4A17: CD 83 4E       CALL    $4E83           
4A1A: CD A6 45       CALL    $45A6           
4A1D: E1             POP     HL              
4A1E: C9             RET                     
4A1F: 3A 20 50       LD      A,($5020)       
4A22: BE             CP      (HL)            
4A23: 23             INC     HL              
4A24: C9             RET                     
4A25: 46             LD      B,(HL)          
4A26: 23             INC     HL              
4A27: C3 CE 4B       JP      $4BCE           
4A2A: 4E             LD      C,(HL)          
4A2B: 23             INC     HL              
4A2C: 46             LD      B,(HL)          
4A2D: 23             INC     HL              
4A2E: E5             PUSH    HL              
4A2F: CD 83 4E       CALL    $4E83           
4A32: CD 05 47       CALL    $4705           
4A35: 5E             LD      E,(HL)          
4A36: 23             INC     HL              
4A37: 7E             LD      A,(HL)          
4A38: E1             POP     HL              
4A39: 7B             LD      A,E             
4A3A: B9             CP      C               
4A3B: C9             RET                     
4A3C: F6 01          OR      $01             
4A3E: C9             RET                     
4A3F: 3A 20 50       LD      A,($5020)       
4A42: FE 1D          CP      $1D             
4A44: C2 54 4A       JP      NZ,$4A54        
4A47: 06 1D          LD      B,$1D           
4A49: E5             PUSH    HL              
4A4A: CD 83 4E       CALL    $4E83           
4A4D: CD A6 45       CALL    $45A6           
4A50: E1             POP     HL              
4A51: CA 5B 4A       JP      Z,$4A5B         
4A54: CD 06 47       CALL    $4706           
4A57: EB             EX      DE,HL           
4A58: C3 5E 4A       JP      $4A5E           
4A5B: CD 9B 4E       CALL    $4E9B           
4A5E: 97             SUB     A               
4A5F: C9             RET                     
4A60: CD D0 49       CALL    $49D0           
4A63: 97             SUB     A               
4A64: C9             RET                     
4A65: E5             PUSH    HL              
4A66: 3E 0D          LD      A,$0D           
4A68: CD 0D 4F       CALL    $4F0D           
4A6B: 21 51 56       LD      HL,$5651        
4A6E: CD 05 47       CALL    $4705           
4A71: CD 19 47       CALL    $4719           
4A74: D2 99 4A       JP      NC,$4A99        
4A77: D5             PUSH    DE              
4A78: CD 05 47       CALL    $4705           
4A7B: 46             LD      B,(HL)          
4A7C: 3A 20 50       LD      A,($5020)       
4A7F: B8             CP      B               
4A80: C2 94 4A       JP      NZ,$4A94        
4A83: 23             INC     HL              
4A84: 23             INC     HL              
4A85: 23             INC     HL              
4A86: 06 02          LD      B,$02           
4A88: CD F1 46       CALL    $46F1           
4A8B: D2 94 4A       JP      NC,$4A94        
4A8E: 23             INC     HL              
4A8F: D5             PUSH    DE              
4A90: CD 92 4E       CALL    $4E92           
4A93: D1             POP     DE              
4A94: EB             EX      DE,HL           
4A95: D1             POP     DE              
4A96: C3 71 4A       JP      $4A71           
4A99: 97             SUB     A               
4A9A: E1             POP     HL              
4A9B: C9             RET                     
4A9C: E5             PUSH    HL              
4A9D: 2A 14 50       LD      HL,($5014)      
4AA0: 3A 11 50       LD      A,($5011)       
4AA3: 22 26 50       LD      ($5026),HL      
4AA6: E1             POP     HL              
4AA7: A7             AND     A               
4AA8: CA BD 4A       JP      Z,$4ABD         
4AAB: 46             LD      B,(HL)          
4AAC: 23             INC     HL              
4AAD: E5             PUSH    HL              
4AAE: CD 83 4E       CALL    $4E83           
4AB1: EB             EX      DE,HL           
4AB2: E1             POP     HL              
4AB3: 3A 26 50       LD      A,($5026)       
4AB6: BB             CP      E               
4AB7: C0             RET     NZ              
4AB8: 3A 27 50       LD      A,($5027)       
4ABB: BA             CP      D               
4ABC: C9             RET                     
4ABD: B8             CP      B               
4ABE: C9             RET                     
4ABF: E5             PUSH    HL              
4AC0: 2A 1A 50       LD      HL,($501A)      
4AC3: 3A 17 50       LD      A,($5017)       
4AC6: C3 A3 4A       JP      $4AA3           
4AC9: 46             LD      B,(HL)          
4ACA: 23             INC     HL              
4ACB: 3A 1F 50       LD      A,($501F)       
4ACE: B8             CP      B               
4ACF: C9             RET                     
4AD0: E5             PUSH    HL              
4AD1: 2A 0E 50       LD      HL,($500E)      
4AD4: CD 05 47       CALL    $4705           
4AD7: 3A 20 50       LD      A,($5020)       
4ADA: 77             LD      (HL),A          
4ADB: 97             SUB     A               
4ADC: E1             POP     HL              
4ADD: C9             RET                     
4ADE: E5             PUSH    HL              
4ADF: 2A 0E 50       LD      HL,($500E)      
4AE2: CD 05 47       CALL    $4705           
4AE5: 3A 23 50       LD      A,($5023)       
4AE8: 77             LD      (HL),A          
4AE9: 97             SUB     A               
4AEA: E1             POP     HL              
4AEB: C9             RET                     
4AEC: E5             PUSH    HL              
4AED: 2A 24 50       LD      HL,($5024)      
4AF0: CD 05 47       CALL    $4705           
4AF3: 23             INC     HL              
4AF4: 06 04          LD      B,$04           
4AF6: CD F1 46       CALL    $46F1           
4AF9: D2 05 4B       JP      NC,$4B05        
4AFC: CD 05 47       CALL    $4705           
4AFF: CD 94 48       CALL    $4894           
4B02: CA 48 4B       JP      Z,$4B48         
4B05: 3A 17 50       LD      A,($5017)       
4B08: A7             AND     A               
4B09: CA 26 4B       JP      Z,$4B26         
4B0C: 2A 1A 50       LD      HL,($501A)      
4B0F: CD 05 47       CALL    $4705           
4B12: 23             INC     HL              
4B13: 23             INC     HL              
4B14: 23             INC     HL              
4B15: 06 06          LD      B,$06           
4B17: CD F1 46       CALL    $46F1           
4B1A: D2 26 4B       JP      NC,$4B26        
4B1D: CD 05 47       CALL    $4705           
4B20: CD 94 48       CALL    $4894           
4B23: CA 48 4B       JP      Z,$4B48         
4B26: 3A 11 50       LD      A,($5011)       
4B29: A7             AND     A               
4B2A: C2 31 4B       JP      NZ,$4B31        
4B2D: E1             POP     HL              
4B2E: F6 01          OR      $01             
4B30: C9             RET                     
4B31: 2A 14 50       LD      HL,($5014)      
4B34: CD 05 47       CALL    $4705           
4B37: 23             INC     HL              
4B38: 23             INC     HL              
4B39: 23             INC     HL              
4B3A: 06 07          LD      B,$07           
4B3C: CD F1 46       CALL    $46F1           
4B3F: D2 2D 4B       JP      NC,$4B2D        
4B42: CD 05 47       CALL    $4705           
4B45: CD 94 48       CALL    $4894           
4B48: E1             POP     HL              
4B49: C9             RET                     
4B4A: E5             PUSH    HL              
4B4B: 2A 0E 50       LD      HL,($500E)      
4B4E: 3A 0D 50       LD      A,($500D)       
4B51: C3 5B 4B       JP      $4B5B           
4B54: E5             PUSH    HL              
4B55: 2A 14 50       LD      HL,($5014)      
4B58: 3A 11 50       LD      A,($5011)       
4B5B: A7             AND     A               
4B5C: CA 48 4B       JP      Z,$4B48         
4B5F: 3A 20 50       LD      A,($5020)       
4B62: FE 1D          CP      $1D             
4B64: C2 79 4B       JP      NZ,$4B79        
4B67: CD 05 47       CALL    $4705           
4B6A: 23             INC     HL              
4B6B: 23             INC     HL              
4B6C: 23             INC     HL              
4B6D: 06 02          LD      B,$02           
4B6F: CD F1 46       CALL    $46F1           
4B72: D2 79 4B       JP      NC,$4B79        
4B75: 23             INC     HL              
4B76: CD 9B 4E       CALL    $4E9B           
4B79: E1             POP     HL              
4B7A: 97             SUB     A               
4B7B: C9             RET                     
4B7C: E5             PUSH    HL              
4B7D: 3A 17 50       LD      A,($5017)       
4B80: 2A 1A 50       LD      HL,($501A)      
4B83: C3 5B 4B       JP      $4B5B           
4B86: E5             PUSH    HL              
4B87: 2A 0E 50       LD      HL,($500E)      
4B8A: 3A 0D 50       LD      A,($500D)       
4B8D: A7             AND     A               
4B8E: CA 2D 4B       JP      Z,$4B2D         
4B91: CD 05 47       CALL    $4705           
4B94: 23             INC     HL              
4B95: 23             INC     HL              
4B96: 7E             LD      A,(HL)          
4B97: E1             POP     HL              
4B98: A6             AND     (HL)            
4B99: AE             XOR     (HL)            
4B9A: 23             INC     HL              
4B9B: C9             RET                     
4B9C: CD 94 48       CALL    $4894           
4B9F: C2 A5 4B       JP      NZ,$4BA5        
4BA2: F6 01          OR      $01             
4BA4: C9             RET                     
4BA5: 97             SUB     A               
4BA6: C9             RET                     
4BA7: 46             LD      B,(HL)          
4BA8: 23             INC     HL              
4BA9: E5             PUSH    HL              
4BAA: CD 83 4E       CALL    $4E83           
4BAD: CD 05 47       CALL    $4705           
4BB0: D1             POP     DE              
4BB1: 1A             LD      A,(DE)          
4BB2: 77             LD      (HL),A          
4BB3: EB             EX      DE,HL           
4BB4: 23             INC     HL              
4BB5: 97             SUB     A               
4BB6: C9             RET                     
4BB7: E5             PUSH    HL              
4BB8: 2A 0E 50       LD      HL,($500E)      
4BBB: CD 05 47       CALL    $4705           
4BBE: 46             LD      B,(HL)          
4BBF: 78             LD      A,B             
4BC0: A7             AND     A               
4BC1: E1             POP     HL              
4BC2: CA C8 45       JP      Z,$45C8         
4BC5: 3A 20 50       LD      A,($5020)       
4BC8: B8             CP      B               
4BC9: C8             RET     Z               
4BCA: 78             LD      A,B             
4BCB: E6 80          AND     $80             
4BCD: C0             RET     NZ              
4BCE: E5             PUSH    HL              
4BCF: CD 83 4E       CALL    $4E83           
4BD2: C3 BB 4B       JP      $4BBB           
4BD5: 21 51 56       LD      HL,$5651        
4BD8: 97             SUB     A               
4BD9: 32 1E 50       LD      ($501E),A       
4BDC: CD 05 47       CALL    $4705           
4BDF: CD 19 47       CALL    $4719           
4BE2: D0             RET     NC              
4BE3: 3A 1E 50       LD      A,($501E)       
4BE6: 3C             INC     A               
4BE7: 32 1E 50       LD      ($501E),A       
4BEA: D5             PUSH    DE              
4BEB: CD 05 47       CALL    $4705           
4BEE: 4E             LD      C,(HL)          
4BEF: D5             PUSH    DE              
4BF0: 7E             LD      A,(HL)          
4BF1: A7             AND     A               
4BF2: CA 3A 4C       JP      Z,$4C3A         
4BF5: 23             INC     HL              
4BF6: 23             INC     HL              
4BF7: 23             INC     HL              
4BF8: 06 08          LD      B,$08           
4BFA: CD F1 46       CALL    $46F1           
4BFD: D2 3A 4C       JP      NC,$4C3A        
4C00: CD 05 47       CALL    $4705           
4C03: E5             PUSH    HL              
4C04: CD D3 4F       CALL    $4FD3           
4C07: 3A 1E 50       LD      A,($501E)       
4C0A: 32 20 50       LD      ($5020),A       
4C0D: 47             LD      B,A             
4C0E: CD 83 4E       CALL    $4E83           
4C11: 22 21 50       LD      ($5021),HL      
4C14: 79             LD      A,C             
4C15: A7             AND     A               
4C16: FA 29 4C       JP      M,$4C29         
4C19: 47             LD      B,A             
4C1A: CD 83 4E       CALL    $4E83           
4C1D: CD 05 47       CALL    $4705           
4C20: 7E             LD      A,(HL)          
4C21: A7             AND     A               
4C22: C2 15 4C       JP      NZ,$4C15        
4C25: E1             POP     HL              
4C26: C3 3A 4C       JP      $4C3A           
4C29: 32 23 50       LD      ($5023),A       
4C2C: 21 1F 68       LD      HL,$681F        
4C2F: 47             LD      B,A             
4C30: CD ED 46       CALL    $46ED           
4C33: 22 24 50       LD      ($5024),HL      
4C36: E1             POP     HL              
4C37: CD 94 48       CALL    $4894           
4C3A: E1             POP     HL              
4C3B: D1             POP     DE              
4C3C: C3 DF 4B       JP      $4BDF           
4C3F: 3A F9 4F       LD      A,($4FF9)       
4C42: BE             CP      (HL)            
4C43: 23             INC     HL              
4C44: DA 4D 4C       JP      C,$4C4D         
4C47: CA 4D 4C       JP      Z,$4C4D         
4C4A: F6 01          OR      $01             
4C4C: C9             RET                     
4C4D: 97             SUB     A               
4C4E: C9             RET                     
4C4F: 4E             LD      C,(HL)          
4C50: 23             INC     HL              
4C51: E5             PUSH    HL              
4C52: 2A 0E 50       LD      HL,($500E)      
4C55: CD 05 47       CALL    $4705           
4C58: 23             INC     HL              
4C59: 23             INC     HL              
4C5A: 23             INC     HL              
4C5B: E5             PUSH    HL              
4C5C: D5             PUSH    DE              
4C5D: 06 09          LD      B,$09           
4C5F: CD F1 46       CALL    $46F1           
4C62: D2 8A 4C       JP      NC,$4C8A        
4C65: CD 05 47       CALL    $4705           
4C68: 23             INC     HL              
4C69: 7E             LD      A,(HL)          
4C6A: 91             SUB     C               
4C6B: D2 6F 4C       JP      NC,$4C6F        
4C6E: 97             SUB     A               
4C6F: 77             LD      (HL),A          
4C70: D1             POP     DE              
4C71: E1             POP     HL              
4C72: A7             AND     A               
4C73: CA 79 4C       JP      Z,$4C79         
4C76: 97             SUB     A               
4C77: E1             POP     HL              
4C78: C9             RET                     
4C79: 06 0A          LD      B,$0A           
4C7B: CD F1 46       CALL    $46F1           
4C7E: D2 76 4C       JP      NC,$4C76        
4C81: CD 05 47       CALL    $4705           
4C84: CD 94 48       CALL    $4894           
4C87: C3 76 4C       JP      $4C76           
4C8A: D1             POP     DE              
4C8B: E1             POP     HL              
4C8C: C3 76 4C       JP      $4C76           
4C8F: 46             LD      B,(HL)          
4C90: 23             INC     HL              
4C91: 4E             LD      C,(HL)          
4C92: 23             INC     HL              
4C93: E5             PUSH    HL              
4C94: CD 83 4E       CALL    $4E83           
4C97: CD 05 47       CALL    $4705           
4C9A: 5E             LD      E,(HL)          
4C9B: 41             LD      B,C             
4C9C: E5             PUSH    HL              
4C9D: D5             PUSH    DE              
4C9E: CD 83 4E       CALL    $4E83           
4CA1: CD 05 47       CALL    $4705           
4CA4: D1             POP     DE              
4CA5: 7E             LD      A,(HL)          
4CA6: 73             LD      (HL),E          
4CA7: E1             POP     HL              
4CA8: 77             LD      (HL),A          
4CA9: E1             POP     HL              
4CAA: 97             SUB     A               
4CAB: C9             RET                     
4CAC: 4E             LD      C,(HL)          
4CAD: 23             INC     HL              
4CAE: E5             PUSH    HL              
4CAF: 2A 0E 50       LD      HL,($500E)      
4CB2: CD 05 47       CALL    $4705           
4CB5: 23             INC     HL              
4CB6: 23             INC     HL              
4CB7: 23             INC     HL              
4CB8: 06 09          LD      B,$09           
4CBA: CD F1 46       CALL    $46F1           
4CBD: D2 CC 4C       JP      NC,$4CCC        
4CC0: CD 05 47       CALL    $4705           
4CC3: 23             INC     HL              
4CC4: 7E             LD      A,(HL)          
4CC5: B9             CP      C               
4CC6: DA D0 4C       JP      C,$4CD0         
4CC9: CA D0 4C       JP      Z,$4CD0         
4CCC: E1             POP     HL              
4CCD: F6 01          OR      $01             
4CCF: C9             RET                     
4CD0: 97             SUB     A               
4CD1: E1             POP     HL              
4CD2: C9             RET                     
4CD3: 4E             LD      C,(HL)          
4CD4: 23             INC     HL              
4CD5: E5             PUSH    HL              
4CD6: 2A 0E 50       LD      HL,($500E)      
4CD9: CD 05 47       CALL    $4705           
4CDC: 23             INC     HL              
4CDD: 23             INC     HL              
4CDE: 23             INC     HL              
4CDF: 06 09          LD      B,$09           
4CE1: CD F1 46       CALL    $46F1           
4CE4: D2 D0 4C       JP      NC,$4CD0        
4CE7: CD 05 47       CALL    $4705           
4CEA: 56             LD      D,(HL)          
4CEB: 23             INC     HL              
4CEC: 7E             LD      A,(HL)          
4CED: 81             ADD     A,C             
4CEE: BA             CP      D               
4CEF: DA F3 4C       JP      C,$4CF3         
4CF2: 7A             LD      A,D             
4CF3: 77             LD      (HL),A          
4CF4: C3 D0 4C       JP      $4CD0           
4CF7: 3E 0D          LD      A,$0D           
4CF9: CD 0D 4F       CALL    $4F0D           
4CFC: 3E 0D          LD      A,$0D           
4CFE: CD 0D 4F       CALL    $4F0D           
4D01: C3 00 43       JP      $4300           
4D04: C3 04 4D       JP      $4D04           
4D07: E5             PUSH    HL              
4D08: 11 9E 4D       LD      DE,$4D9E        
4D0B: CD AF 4D       CALL    $4DAF           
4D0E: CD D6 47       CALL    $47D6           
4D11: FE 08          CP      $08             
4D13: CA D0 4C       JP      Z,$4CD0         
4D16: FE 0D          CP      $0D             
4D18: C2 0E 4D       JP      NZ,$4D0E        
4D1B: 97             SUB     A               
4D1C: CD 12 02       CALL    $0212           
4D1F: CD 96 02       CALL    $0296           
4D22: 21 51 56       LD      HL,$5651        
4D25: 01 CE 11       LD      BC,$11CE        
4D28: 04             INC     B               
4D29: 0E 00          LD      C,$00           
4D2B: 59             LD      E,C             
4D2C: 3A 3F 3C       LD      A,($3C3F)       
4D2F: EE 0A          XOR     $0A             
4D31: 32 3F 3C       LD      ($3C3F),A       
4D34: E5             PUSH    HL              
4D35: C5             PUSH    BC              
4D36: D5             PUSH    DE              
4D37: CD 35 02       CALL    $0235           
4D3A: D1             POP     DE              
4D3B: C1             POP     BC              
4D3C: E1             POP     HL              
4D3D: 77             LD      (HL),A          
4D3E: 83             ADD     A,E             
4D3F: 5F             LD      E,A             
4D40: 23             INC     HL              
4D41: 0D             DEC     C               
4D42: C2 34 4D       JP      NZ,$4D34        
4D45: E5             PUSH    HL              
4D46: D5             PUSH    DE              
4D47: C5             PUSH    BC              
4D48: CD 35 02       CALL    $0235           
4D4B: C1             POP     BC              
4D4C: D1             POP     DE              
4D4D: E1             POP     HL              
4D4E: BB             CP      E               
4D4F: C2 89 4D       JP      NZ,$4D89        
4D52: 05             DEC     B               
4D53: C2 29 4D       JP      NZ,$4D29        
4D56: CD F8 01       CALL    $01F8           
4D59: 31 FF 7F       LD      SP,$7FFF        
4D5C: 3E 1D          LD      A,$1D           
4D5E: 32 20 50       LD      ($5020),A       
4D61: 47             LD      B,A             
4D62: CD 83 4E       CALL    $4E83           
4D65: 22 21 50       LD      ($5021),HL      
4D68: CD 05 47       CALL    $4705           
4D6B: 7E             LD      A,(HL)          
4D6C: 32 23 50       LD      ($5023),A       
4D6F: 47             LD      B,A             
4D70: 21 1F 68       LD      HL,$681F        
4D73: CD ED 46       CALL    $46ED           
4D76: 22 24 50       LD      ($5024),HL      
4D79: 3E 0D          LD      A,$0D           
4D7B: CD 0D 4F       CALL    $4F0D           
4D7E: CD D0 49       CALL    $49D0           
4D81: 3E 0D          LD      A,$0D           
4D83: CD 0D 4F       CALL    $4F0D           
4D86: C3 23 43       JP      $4323           
4D89: CD F8 01       CALL    $01F8           
4D8C: 11 95 4D       LD      DE,$4D95        
4D8F: CD AF 4D       CALL    $4DAF           
4D92: C3 0E 4D       JP      $4D0E           
4D95: 0D             DEC     C               
4D96: 43             LD      B,E             
4D97: 48             LD      C,B             
4D98: 45             LD      B,L             
4D99: 43             LD      B,E             
4D9A: 4B             LD      C,E             
4D9B: 53             LD      D,E             
4D9C: 55             LD      D,L             
4D9D: 4D             LD      C,L             
4D9E: 0D             DEC     C               
4D9F: 52             LD      D,D             
4DA0: 45             LD      B,L             
4DA1: 41             LD      B,C             
4DA2: 44             LD      B,H             
4DA3: 59             LD      E,C             
4DA4: 20 43          JR      NZ,$4DE9        
4DA6: 41             LD      B,C             
4DA7: 53             LD      D,E             
4DA8: 53             LD      D,E             
4DA9: 45             LD      B,L             
4DAA: 54             LD      D,H             
4DAB: 54             LD      D,H             
4DAC: 45             LD      B,L             
4DAD: 0D             DEC     C               
4DAE: 00             NOP                     
4DAF: 1A             LD      A,(DE)          
4DB0: A7             AND     A               
4DB1: C8             RET     Z               
4DB2: D5             PUSH    DE              
4DB3: CD 0D 4F       CALL    $4F0D           
4DB6: D1             POP     DE              
4DB7: 13             INC     DE              
4DB8: C3 AF 4D       JP      $4DAF           
4DBB: E5             PUSH    HL              
4DBC: 11 9E 4D       LD      DE,$4D9E        
4DBF: CD AF 4D       CALL    $4DAF           
4DC2: CD D6 47       CALL    $47D6           
4DC5: FE 08          CP      $08             
4DC7: CA D0 4C       JP      Z,$4CD0         
4DCA: FE 0D          CP      $0D             
4DCC: C2 C2 4D       JP      NZ,$4DC2        
4DCF: 97             SUB     A               
4DD0: CD 12 02       CALL    $0212           
4DD3: CD 87 02       CALL    $0287           
4DD6: 21 51 56       LD      HL,$5651        
4DD9: 01 CE 11       LD      BC,$11CE        
4DDC: 04             INC     B               
4DDD: 0E 00          LD      C,$00           
4DDF: 59             LD      E,C             
4DE0: E5             PUSH    HL              
4DE1: C5             PUSH    BC              
4DE2: 7E             LD      A,(HL)          
4DE3: 83             ADD     A,E             
4DE4: 5F             LD      E,A             
4DE5: D5             PUSH    DE              
4DE6: 7E             LD      A,(HL)          
4DE7: CD 64 02       CALL    $0264           
4DEA: D1             POP     DE              
4DEB: C1             POP     BC              
4DEC: E1             POP     HL              
4DED: 23             INC     HL              
4DEE: 0D             DEC     C               
4DEF: C2 E0 4D       JP      NZ,$4DE0        
4DF2: 7B             LD      A,E             
4DF3: E5             PUSH    HL              
4DF4: D5             PUSH    DE              
4DF5: C5             PUSH    BC              
4DF6: CD 64 02       CALL    $0264           
4DF9: C1             POP     BC              
4DFA: D1             POP     DE              
4DFB: E1             POP     HL              
4DFC: 05             DEC     B               
4DFD: C2 DD 4D       JP      NZ,$4DDD        
4E00: CD F8 01       CALL    $01F8           
4E03: C3 D0 4C       JP      $4CD0           
4E06: E5             PUSH    HL              
4E07: 97             SUB     A               
4E08: 32 FD 4F       LD      ($4FFD),A       
4E0B: 32 FE 4F       LD      ($4FFE),A       
4E0E: 3A 23 50       LD      A,($5023)       
4E11: FE 96          CP      $96             
4E13: C2 1B 4E       JP      NZ,$4E1B        
4E16: 3E 01          LD      A,$01           
4E18: 32 FE 4F       LD      ($4FFE),A       
4E1B: 21 51 56       LD      HL,$5651        
4E1E: CD 05 47       CALL    $4705           
4E21: CD 19 47       CALL    $4719           
4E24: D2 5A 4E       JP      NC,$4E5A        
4E27: D5             PUSH    DE              
4E28: CD 05 47       CALL    $4705           
4E2B: 7E             LD      A,(HL)          
4E2C: 47             LD      B,A             
4E2D: FE 96          CP      $96             
4E2F: CA 37 4E       JP      Z,$4E37         
4E32: FE 1D          CP      $1D             
4E34: C2 55 4E       JP      NZ,$4E55        
4E37: 23             INC     HL              
4E38: 3A FD 4F       LD      A,($4FFD)       
4E3B: 86             ADD     A,(HL)          
4E3C: 27             DAA                     
4E3D: 32 FD 4F       LD      ($4FFD),A       
4E40: 78             LD      A,B             
4E41: FE 96          CP      $96             
4E43: CA 4D 4E       JP      Z,$4E4D         
4E46: 3A FE 4F       LD      A,($4FFE)       
4E49: A7             AND     A               
4E4A: CA 55 4E       JP      Z,$4E55         
4E4D: 3A FD 4F       LD      A,($4FFD)       
4E50: 86             ADD     A,(HL)          
4E51: 27             DAA                     
4E52: 32 FD 4F       LD      ($4FFD),A       
4E55: EB             EX      DE,HL           
4E56: D1             POP     DE              
4E57: C3 21 4E       JP      $4E21           
4E5A: 3A FD 4F       LD      A,($4FFD)       
4E5D: 0F             RRCA                    
4E5E: 0F             RRCA                    
4E5F: 0F             RRCA                    
4E60: 0F             RRCA                    
4E61: E6 0F          AND     $0F             
4E63: C6 30          ADD     $30             
4E65: 47             LD      B,A             
4E66: CD 0D 4F       CALL    $4F0D           
4E69: 3A FD 4F       LD      A,($4FFD)       
4E6C: E6 0F          AND     $0F             
4E6E: C6 30          ADD     $30             
4E70: 47             LD      B,A             
4E71: CD 0D 4F       CALL    $4F0D           
4E74: 3E 2E          LD      A,$2E           
4E76: 47             LD      B,A             
4E77: CD 0D 4F       CALL    $4F0D           
4E7A: 3E 20          LD      A,$20           
4E7C: 47             LD      B,A             
4E7D: CD 0D 4F       CALL    $4F0D           
4E80: E1             POP     HL              
4E81: 97             SUB     A               
4E82: C9             RET                     
4E83: 21 51 56       LD      HL,$5651        
4E86: CD 05 47       CALL    $4705           
4E89: 05             DEC     B               
4E8A: C8             RET     Z               
4E8B: CD 05 47       CALL    $4705           
4E8E: EB             EX      DE,HL           
4E8F: C3 89 4E       JP      $4E89           
4E92: CD 9B 4E       CALL    $4E9B           
4E95: 3E 0D          LD      A,$0D           
4E97: CD 0D 4F       CALL    $4F0D           
4E9A: C9             RET                     
4E9B: 01 00 00       LD      BC,$0000        
4E9E: 7E             LD      A,(HL)          
4E9F: E6 80          AND     $80             
4EA1: CA A9 4E       JP      Z,$4EA9         
4EA4: 7E             LD      A,(HL)          
4EA5: E6 7F          AND     $7F             
4EA7: 47             LD      B,A             
4EA8: 23             INC     HL              
4EA9: 4E             LD      C,(HL)          
4EAA: 23             INC     HL              
4EAB: 78             LD      A,B             
4EAC: A7             AND     A               
4EAD: C2 B6 4E       JP      NZ,$4EB6        
4EB0: 79             LD      A,C             
4EB1: FE 02          CP      $02             
4EB3: DA F9 4E       JP      C,$4EF9         
4EB6: CD 3D 4F       CALL    $4F3D           
4EB9: 0B             DEC     BC              
4EBA: 0B             DEC     BC              
4EBB: 3A 20 40       LD      A,($4020)       
4EBE: FE FB          CP      $FB             
4EC0: DA AB 4E       JP      C,$4EAB         
4EC3: E5             PUSH    HL              
4EC4: 2A 20 40       LD      HL,($4020)      
4EC7: 11 BF FF       LD      DE,$FFBF        
4ECA: 19             ADD     HL,DE           
4ECB: 3E 0D          LD      A,$0D           
4ECD: CD 0D 4F       CALL    $4F0D           
4ED0: 3E 20          LD      A,$20           
4ED2: 32 0C 50       LD      ($500C),A       
4ED5: 7E             LD      A,(HL)          
4ED6: FE 20          CP      $20             
4ED8: CA DF 4E       JP      Z,$4EDF         
4EDB: 2B             DEC     HL              
4EDC: C3 D5 4E       JP      $4ED5           
4EDF: 23             INC     HL              
4EE0: 7E             LD      A,(HL)          
4EE1: FE 20          CP      $20             
4EE3: CA F5 4E       JP      Z,$4EF5         
4EE6: 36 20          LD      (HL),$20        
4EE8: FE 1B          CP      $1B             
4EEA: D2 EF 4E       JP      NC,$4EEF        
4EED: C6 40          ADD     $40             
4EEF: CD 0D 4F       CALL    $4F0D           
4EF2: C3 DF 4E       JP      $4EDF           
4EF5: E1             POP     HL              
4EF6: C3 AB 4E       JP      $4EAB           
4EF9: 79             LD      A,C             
4EFA: A7             AND     A               
4EFB: CA 07 4F       JP      Z,$4F07         
4EFE: 7E             LD      A,(HL)          
4EFF: CD 0D 4F       CALL    $4F0D           
4F02: 23             INC     HL              
4F03: 0D             DEC     C               
4F04: C3 F9 4E       JP      $4EF9           
4F07: 3E 20          LD      A,$20           
4F09: CD 0D 4F       CALL    $4F0D           
4F0C: C9             RET                     
4F0D: F5             PUSH    AF              
4F0E: 3A 0C 50       LD      A,($500C)       
4F11: FE 20          CP      $20             
4F13: C2 35 4F       JP      NZ,$4F35        
4F16: F1             POP     AF              
4F17: FE 20          CP      $20             
4F19: C8             RET     Z               
4F1A: FE 2E          CP      $2E             
4F1C: CA 29 4F       JP      Z,$4F29         
4F1F: FE 3F          CP      $3F             
4F21: CA 29 4F       JP      Z,$4F29         
4F24: FE 21          CP      $21             
4F26: C2 36 4F       JP      NZ,$4F36        
4F29: E5             PUSH    HL              
4F2A: 2A 20 40       LD      HL,($4020)      
4F2D: 2B             DEC     HL              
4F2E: 22 20 40       LD      ($4020),HL      
4F31: E1             POP     HL              
4F32: C3 36 4F       JP      $4F36           
4F35: F1             POP     AF              
4F36: 32 0C 50       LD      ($500C),A       
4F39: CD 33 00       CALL    $0033           
4F3C: C9             RET                     
4F3D: 11 CF 4F       LD      DE,$4FCF        
4F40: C5             PUSH    BC              
4F41: 06 03          LD      B,$03           
4F43: 7E             LD      A,(HL)          
4F44: 23             INC     HL              
4F45: 4E             LD      C,(HL)          
4F46: 23             INC     HL              
4F47: E5             PUSH    HL              
4F48: 61             LD      H,C             
4F49: 6F             LD      L,A             
4F4A: 13             INC     DE              
4F4B: 13             INC     DE              
4F4C: EB             EX      DE,HL           
4F4D: E5             PUSH    HL              
4F4E: C5             PUSH    BC              
4F4F: 21 28 00       LD      HL,$0028        
4F52: 22 CD 4F       LD      ($4FCD),HL      
4F55: 21 85 4F       LD      HL,$4F85        
4F58: 36 11          LD      (HL),$11        
4F5A: 01 00 00       LD      BC,$0000        
4F5D: C5             PUSH    BC              
4F5E: 7B             LD      A,E             
4F5F: 17             RLA                     
4F60: 5F             LD      E,A             
4F61: 7A             LD      A,D             
4F62: 17             RLA                     
4F63: 57             LD      D,A             
4F64: 35             DEC     (HL)            
4F65: E1             POP     HL              
4F66: CA 86 4F       JP      Z,$4F86         
4F69: 3E 00          LD      A,$00           
4F6B: CE 00          ADC     $00             
4F6D: 29             ADD     HL,HL           
4F6E: 44             LD      B,H             
4F6F: 85             ADD     A,L             
4F70: 2A CD 4F       LD      HL,($4FCD)      
4F73: 95             SUB     L               
4F74: 4F             LD      C,A             
4F75: 78             LD      A,B             
4F76: 9C             SBC     H               
4F77: 47             LD      B,A             
4F78: C5             PUSH    BC              
4F79: D2 7E 4F       JP      NC,$4F7E        
4F7C: 09             ADD     HL,BC           
4F7D: E3             EX      (SP),HL         
4F7E: 21 85 4F       LD      HL,$4F85        
4F81: 3F             CCF                     
4F82: C3 5E 4F       JP      $4F5E           
4F85: 00             NOP                     
4F86: 01 A4 4F       LD      BC,$4FA4        
4F89: 09             ADD     HL,BC           
4F8A: 7E             LD      A,(HL)          
4F8B: C1             POP     BC              
4F8C: E1             POP     HL              
4F8D: 77             LD      (HL),A          
4F8E: 2B             DEC     HL              
4F8F: 05             DEC     B               
4F90: C2 4D 4F       JP      NZ,$4F4D        
4F93: 21 CF 4F       LD      HL,$4FCF        
4F96: 06 03          LD      B,$03           
4F98: 7E             LD      A,(HL)          
4F99: CD 0D 4F       CALL    $4F0D           
4F9C: 23             INC     HL              
4F9D: 05             DEC     B               
4F9E: C2 98 4F       JP      NZ,$4F98        
4FA1: E1             POP     HL              
4FA2: C1             POP     BC              
4FA3: C9             RET                     
4FA4: 3F             CCF                     
4FA5: 21 32 20       LD      HL,$2032        
4FA8: 22 27 3C       LD      ($3C27),HL      
4FAB: 3E 2F          LD      A,$2F           
4FAD: 30 33          JR      NC,$4FE2        
4FAF: 41             LD      B,C             
4FB0: 42             LD      B,D             
4FB1: 43             LD      B,E             
4FB2: 44             LD      B,H             
4FB3: 45             LD      B,L             
4FB4: 46             LD      B,(HL)          
4FB5: 47             LD      B,A             
4FB6: 48             LD      C,B             
4FB7: 49             LD      C,C             
4FB8: 4A             LD      C,D             
4FB9: 4B             LD      C,E             
4FBA: 4C             LD      C,H             
4FBB: 4D             LD      C,L             
4FBC: 4E             LD      C,(HL)          
4FBD: 4F             LD      C,A             
4FBE: 50             LD      D,B             
4FBF: 51             LD      D,C             
4FC0: 52             LD      D,D             
4FC1: 53             LD      D,E             
4FC2: 54             LD      D,H             
4FC3: 55             LD      D,L             
4FC4: 56             LD      D,(HL)          
4FC5: 57             LD      D,A             
4FC6: 58             LD      E,B             
4FC7: 59             LD      E,C             
4FC8: 5A             LD      E,D             
4FC9: 2D             DEC     L               
4FCA: 2C             INC     L               
4FCB: 2E 00          LD      L,$00           
4FCD: 00             NOP                     
4FCE: 00             NOP                     
4FCF: 00             NOP                     
4FD0: 00             NOP                     
4FD1: 00             NOP                     
4FD2: 00             NOP                     
4FD3: C5             PUSH    BC              
4FD4: E5             PUSH    HL              
4FD5: 2A F9 4F       LD      HL,($4FF9)      
4FD8: 06 17          LD      B,$17           
4FDA: 7D             LD      A,L             
4FDB: E6 06          AND     $06             
4FDD: 37             SCF                     
4FDE: EA E2 4F       JP      PE,$4FE2        
4FE1: 3F             CCF                     
4FE2: 7C             LD      A,H             
4FE3: 1F             RRA                     
4FE4: 67             LD      H,A             
4FE5: 7D             LD      A,L             
4FE6: 1F             RRA                     
4FE7: E6 FE          AND     $FE             
4FE9: 6F             LD      L,A             
4FEA: 05             DEC     B               
4FEB: C2 DB 4F       JP      NZ,$4FDB        
4FEE: 22 F9 4F       LD      ($4FF9),HL      
4FF1: 7C             LD      A,H             
4FF2: E1             POP     HL              
4FF3: C1             POP     BC              
4FF4: C9             RET                     
4FF5: 12             LD      (DE),A          
4FF6: 23             INC     HL              
4FF7: 44             LD      B,H             
4FF8: 1D             DEC     E               
4FF9: 27             DAA                     
4FFA: 4D             LD      C,L             
4FFB: 2D             DEC     L               
4FFC: 13             INC     DE              
4FFD: 00             NOP                     
4FFE: 00             NOP                     
4FFF: 00             NOP                     
5000: 00             NOP                     
5001: 00             NOP                     
5002: 00             NOP                     
5003: 00             NOP                     
5004: 00             NOP                     
5005: 00             NOP                     
5006: 00             NOP                     
5007: 00             NOP                     
5008: 00             NOP                     
5009: 00             NOP                     
500A: 00             NOP                     
500B: 00             NOP                     
500C: 00             NOP                     
500D: 00             NOP                     
500E: 00             NOP                     
500F: 00             NOP                     
5010: 00             NOP                     
5011: 00             NOP                     
5012: 00             NOP                     
5013: 00             NOP                     
5014: 00             NOP                     
5015: 00             NOP                     
5016: 00             NOP                     
5017: 00             NOP                     
5018: 00             NOP                     
5019: 00             NOP                     
501A: 00             NOP                     
501B: 00             NOP                     
501C: 00             NOP                     
501D: 00             NOP                     
501E: 00             NOP                     
501F: 00             NOP                     
5020: 1D             DEC     E               
5021: 00             NOP                     
5022: 00             NOP                     
5023: 81             ADD     A,C             
5024: 22 68 48       LD      ($4868),HL      
5027: 50             LD      D,B      
```
       
## Feedback Prompts

```code
FeedbackPrompts:        
5028: 06 3F          LD      B,$3F           
502A: 56             LD      D,(HL)          
502B: 45             LD      B,L             
502C: 52             LD      D,D             
502D: 42             LD      B,D             
502E: 3F             CCF                     
502F: 06 3F          LD      B,$3F           
5031: 57             LD      D,A             
5032: 48             LD      C,B             
5033: 41             LD      B,C             
5034: 54             LD      D,H             
5035: 3F             CCF                     
5036: 07             RLCA                    
5037: 3F             CCF                     
5038: 57             LD      D,A             
5039: 48             LD      C,B             
503A: 49             LD      C,C             
503B: 43             LD      B,E             
503C: 48             LD      C,B             
503D: 3F             CCF                     
503E: 08             EX      AF,AF'          
503F: 3F             CCF                     
5040: 50             LD      D,B             
5041: 48             LD      C,B             
5042: 52             LD      D,D             
5043: 41             LD      B,C             
5044: 53             LD      D,E             
5045: 45             LD      B,L             
5046: 3F             CCF                     
5047: D4 00 00       CALL    NC,$0000        
504A: 00             NOP                     
504B: 00             NOP                     
504C: 00             NOP                     
504D: 00             NOP                     
504E: 00             NOP                     
504F: 00             NOP                     
5050: 00             NOP                     
5051: 00             NOP                     
5052: 00             NOP                     
5053: 00             NOP                     
5054: 00             NOP                     
5055: 00             NOP                     
5056: 00             NOP                     
5057: 00             NOP                     
5058: 00             NOP                     
5059: 00             NOP                     
505A: 00             NOP                     
505B: 00             NOP                     
505C: 00             NOP                     
505D: 00             NOP                     
505E: 00             NOP                     
505F: 00             NOP                     
5060: 00             NOP                     
5061: 00             NOP                     
5062: 00             NOP                     
5063: 00             NOP                     
5064: 00             NOP                     
5065: 00             NOP                     
5066: 19             ADD     HL,DE           
5067: 49             LD      C,C             
5068: 14             INC     D               
5069: 4A             LD      C,D             
506A: 25             DEC     H               
506B: 4A             LD      C,D             
506C: 2A 4A 3F       LD      HL,($3F4A)      
506F: 4A             LD      C,D             
5070: 3F             CCF                     
5071: 4C             LD      C,H             
5072: 65             LD      H,L             
5073: 4A             LD      C,D             
5074: 60             LD      H,B             
5075: 4A             LD      C,D             
5076: 9C             SBC     H               
5077: 4A             LD      C,D             
5078: BF             CP      A               
5079: 4A             LD      C,D             
507A: C9             RET                     
507B: 4A             LD      C,D             
507C: F4 48 3C       CALL    P,$3C48         
507F: 4A             LD      C,D             
5080: C7             RST     0X00            
5081: 48             LD      C,B             
5082: DD             ???                     
5083: 48             LD      C,B             
5084: D0             RET     NC              
5085: 4A             LD      C,D             
5086: DE 4A          SBC     $4A             
5088: 54             LD      D,H             
5089: 4B             LD      C,E             
508A: 7C             LD      A,H             
508B: 4B             LD      C,E             
508C: EC 4A 9C       CALL    PE,$9C4A        
508F: 4B             LD      C,E             
5090: 86             ADD     A,(HL)          
5091: 4B             LD      C,E             
5092: 4A             LD      C,D             
5093: 4B             LD      C,E             
5094: A7             AND     A               
5095: 4B             LD      C,E             
5096: B7             OR      A               
5097: 4B             LD      C,E             
5098: 23             INC     HL              
5099: 49             LD      C,C             
509A: 40             LD      B,B             
509B: 49             LD      C,C             
509C: 50             LD      D,B             
509D: 49             LD      C,C             
509E: 60             LD      H,B             
509F: 49             LD      C,C             
50A0: 4F             LD      C,A             
50A1: 4C             LD      C,H             
50A2: 8F             ADC     A,A             
50A3: 4C             LD      C,H             
50A4: 47             LD      B,A             
50A5: 4A             LD      C,D             
50A6: 1F             RRA                     
50A7: 4A             LD      C,D             
50A8: 70             LD      (HL),B          
50A9: 49             LD      C,C             
50AA: AC             XOR     H               
50AB: 4C             LD      C,H             
50AC: D3 4C          OUT     ($4C),A         
50AE: 04             INC     B               
50AF: 4D             LD      C,L             
50B0: F7             RST     0X30            
50B1: 4C             LD      C,H             
50B2: 06 4E          LD      B,$4E           
50B4: 07             RLCA                    
50B5: 4D             LD      C,L             
50B6: BB             CP      E               
50B7: 4D             LD      C,L             
50B8: 00             NOP 
```

## Phrase List

```code
PhraseList: 
; The noun values are bits that must be set in the target noun. The value for a noun in this table must be 
; non-zero since a zero in the phrase means no-word. If no other bit is flagged then the upper bit is set
; (all objects have the upper bit set). The upper bit is set with "A", but it doesn't have to be.
;
;    Bits: uvCPAXOL
;    v=1 if object is a true weapon (only sword has this set)
;    C=1 if object can be carried
;    P=1 if object is a person;
;    A=1 if open/close-able
;    X=1 if lock/unlock-able 
;    O=1 if closed
;    L=1 if locked
;                                                               ; #   Verb    Prep   Noun1      Noun2                    
50B9: 05             DEC     B               
50BA: 00             NOP                     
50BB: 00             NOP                     
50BC: 00             NOP                     
50BD: 01 06 00       LD      BC,$0006        
50C0: 00             NOP                     
50C1: 00             NOP                     
50C2: 02             LD      (BC),A          
50C3: 07             RLCA                    
50C4: 00             NOP                     
50C5: 00             NOP                     
50C6: 00             NOP                     
50C7: 03             INC     BC              
50C8: 08             EX      AF,AF'          
50C9: 00             NOP                     
50CA: 00             NOP                     
50CB: 00             NOP                     
50CC: 04             INC     B               
50CD: 09             ADD     HL,BC           
50CE: 00             NOP                     
50CF: 20 00          JR      NZ,$50D1        
50D1: 05             DEC     B               
50D2: 34             INC     (HL)            
50D3: 07             RLCA                    
50D4: 00             NOP                     
50D5: 80             ADD     A,B             
50D6: 05             DEC     B               
50D7: 34             INC     (HL)            
50D8: 07             RLCA                    
50D9: 80             ADD     A,B             
50DA: 00             NOP                     
50DB: 05             DEC     B               
50DC: 0A             LD      A,(BC)          
50DD: 00             NOP                     
50DE: 20 00          JR      NZ,$50E0        
50E0: 06 0A          LD      B,$0A           
50E2: 05             DEC     B               
50E3: 80             ADD     A,B             
50E4: 80             ADD     A,B             
50E5: 0F             RRCA                    
50E6: 0A             LD      A,(BC)          
50E7: 06 00          LD      B,$00           
50E9: 88             ADC     A,B             
50EA: 16 0B          LD      D,$0B           
50EC: 00             NOP                     
50ED: 00             NOP                     
50EE: 00             NOP                     
50EF: 07             RLCA                    
50F0: 01 00 04       LD      BC,$0400        
50F3: 00             NOP                     
50F4: 08             EX      AF,AF'          
50F5: 04             INC     B               
50F6: 02             LD      (BC),A          
50F7: 10 40          DJNZ    $5139           
50F9: 09             ADD     HL,BC           
50FA: 0C             INC     C               
50FB: 00             NOP                     
50FC: 00             NOP                     
50FD: 00             NOP                     
50FE: 0A             LD      A,(BC)          
50FF: 0C             INC     C               
5100: 03             INC     BC              
5101: 00             NOP                     
5102: 80             ADD     A,B             
5103: 0B             DEC     BC              
5104: 0C             INC     C               
5105: 04             INC     B               
5106: 00             NOP                     
5107: 80             ADD     A,B             
5108: 0C             INC     C               
5109: 0C             INC     C               
510A: 05             DEC     B               
510B: 00             NOP                     
510C: 80             ADD     A,B             
510D: 10 03          DJNZ    $5112           
510F: 03             INC     BC              
5110: 40             LD      B,B             
5111: 10 0D          DJNZ    $5120           
5113: 03             INC     BC              
5114: 05             DEC     B               
5115: 80             ADD     A,B             
5116: 80             ADD     A,B             
5117: 39             ADD     HL,SP           
5118: 03             INC     BC              
5119: 08             EX      AF,AF'          
511A: 00             NOP                     
511B: 20 06          JR      NZ,$5123        
511D: 03             INC     BC              
511E: 01 80 10       LD      BC,$1080        
5121: 0E 0D          LD      C,$0D           
5123: 01 80 10       LD      BC,$1080        
5126: 0E 0E          LD      C,$0E           
5128: 00             NOP                     
5129: 80             ADD     A,B             
512A: 00             NOP                     
512B: 0B             DEC     BC              
512C: 0E 05          LD      C,$05           
512E: 00             NOP                     
512F: 80             ADD     A,B             
5130: 0B             DEC     BC              
5131: 0F             RRCA                    
5132: 00             NOP                     
5133: 80             ADD     A,B             
5134: 00             NOP                     
5135: 11 0F 02       LD      DE,$020F        
5138: 80             ADD     A,B             
5139: 80             ADD     A,B             
513A: 3A 10 00       LD      A,($0010)       
513D: 80             ADD     A,B             
513E: 00             NOP                     
513F: 12             LD      (DE),A          
5140: 10 08          DJNZ    $514A           
5142: 00             NOP                     
5143: 80             ADD     A,B             
5144: 12             LD      (DE),A          
5145: 10 06          DJNZ    $514D           
5147: 00             NOP                     
5148: 80             ADD     A,B             
5149: 05             DEC     B               
514A: 10 06          DJNZ    $5152           
514C: 80             ADD     A,B             
514D: 00             NOP                     
514E: 05             DEC     B               
514F: 10 07          DJNZ    $5158           
5151: 00             NOP                     
5152: 80             ADD     A,B             
5153: 2D             DEC     L               
5154: 10 07          DJNZ    $515D           
5156: 80             ADD     A,B             
5157: 00             NOP                     
5158: 2D             DEC     L               
5159: 11 02 88       LD      DE,$8802        
515C: 88             ADC     A,B             
515D: 14             INC     D               
515E: 12             LD      (DE),A          
515F: 00             NOP                     
5160: 80             ADD     A,B             
5161: 00             NOP                     
5162: 15             DEC     D               
5163: 13             INC     DE              
5164: 06 00          LD      B,$00           
5166: 88             ADC     A,B             
5167: 16 14          LD      D,$14           
5169: 00             NOP                     
516A: 88             ADC     A,B             
516B: 00             NOP                     
516C: 16 15          LD      D,$15           
516E: 00             NOP                     
516F: 80             ADD     A,B             
5170: 00             NOP                     
5171: 17             RLA                     
5172: 15             DEC     D               
5173: 07             RLCA                    
5174: 00             NOP                     
5175: 80             ADD     A,B             
5176: 17             RLA                     
5177: 15             DEC     D               
5178: 08             EX      AF,AF'          
5179: 00             NOP                     
517A: 80             ADD     A,B             
517B: 17             RLA                     
517C: 15             DEC     D               
517D: 09             ADD     HL,BC           
517E: 00             NOP                     
517F: 80             ADD     A,B             
5180: 17             RLA                     
5181: 15             DEC     D               
5182: 0C             INC     C               
5183: 00             NOP                     
5184: 80             ADD     A,B             
5185: 17             RLA                     
5186: 15             DEC     D               
5187: 05             DEC     B               
5188: 00             NOP                     
5189: 00             NOP                     
518A: 36 15          LD      (HL),$15        
518C: 05             DEC     B               
518D: 00             NOP                     
518E: 80             ADD     A,B             
518F: 36 15          LD      (HL),$15        
5191: 06 00          LD      B,$00           
5193: 00             NOP                     
5194: 37             SCF                     
5195: 15             DEC     D               
5196: 06 00          LD      B,$00           
5198: 80             ADD     A,B             
5199: 37             SCF                     
519A: 15             DEC     D               
519B: 04             INC     B               
519C: 00             NOP                     
519D: 80             ADD     A,B             
519E: 38 16          JR      C,$51B6         
51A0: 00             NOP                     
51A1: 80             ADD     A,B             
51A2: 00             NOP                     
51A3: 18 17          JR      $51BC           
51A5: 00             NOP                     
51A6: 00             NOP                     
51A7: 00             NOP                     
51A8: 19             ADD     HL,DE           
51A9: 18 00          JR      $51AB           
51AB: 00             NOP                     
51AC: 00             NOP                     
51AD: 1A             LD      A,(DE)          
51AE: 05             DEC     B               
51AF: 01 00 00       LD      BC,$0000        
51B2: 01 06 01       LD      BC,$0106        
51B5: 00             NOP                     
51B6: 00             NOP                     
51B7: 02             LD      (BC),A          
51B8: 07             RLCA                    
51B9: 01 00 00       LD      BC,$0000        
51BC: 03             INC     BC              
51BD: 08             EX      AF,AF'          
51BE: 01 00 00       LD      BC,$0000        
51C1: 04             INC     B               
51C2: 0A             LD      A,(BC)          
51C3: 08             EX      AF,AF'          
51C4: 00             NOP                     
51C5: 20 06          JR      NZ,$51CD        
51C7: 0A             LD      A,(BC)          
51C8: 08             EX      AF,AF'          
51C9: 20 00          JR      NZ,$51CB        
51CB: 06 0A          LD      B,$0A           
51CD: 0A             LD      A,(BC)          
51CE: 20 80          JR      NZ,$5150        
51D0: 06 0A          LD      B,$0A           
51D2: 04             INC     B               
51D3: 20 80          JR      NZ,$5155        
51D5: 06 0A          LD      B,$0A           
51D7: 0C             INC     C               
51D8: 20 80          JR      NZ,$515A        
51DA: 06 0C          LD      B,$0C           
51DC: 07             RLCA                    
51DD: 00             NOP                     
51DE: 00             NOP                     
51DF: 0A             LD      A,(BC)          
51E0: 0C             INC     C               
51E1: 08             EX      AF,AF'          
51E2: 00             NOP                     
51E3: 00             NOP                     
51E4: 0A             LD      A,(BC)          
51E5: 0C             INC     C               
51E6: 09             ADD     HL,BC           
51E7: 80             ADD     A,B             
51E8: 00             NOP                     
51E9: 0B             DEC     BC              
51EA: 0C             INC     C               
51EB: 09             ADD     HL,BC           
51EC: 00             NOP                     
51ED: 80             ADD     A,B             
51EE: 0A             LD      A,(BC)          
51EF: 0C             INC     C               
51F0: 0B             DEC     BC              
51F1: 00             NOP                     
51F2: 00             NOP                     
51F3: 0A             LD      A,(BC)          
51F4: 0C             INC     C               
51F5: 0A             LD      A,(BC)          
51F6: 00             NOP                     
51F7: 00             NOP                     
51F8: 0A             LD      A,(BC)          
51F9: 0C             INC     C               
51FA: 0B             DEC     BC              
51FB: 00             NOP                     
51FC: 80             ADD     A,B             
51FD: 1B             DEC     DE              
51FE: 0C             INC     C               
51FF: 0A             LD      A,(BC)          
5200: 00             NOP                     
5201: 80             ADD     A,B             
5202: 1C             INC     E               
5203: 0C             INC     C               
5204: 06 00          LD      B,$00           
5206: 00             NOP                     
5207: 1D             DEC     E               
5208: 2F             CPL                     
5209: 00             NOP                     
520A: 00             NOP                     
520B: 00             NOP                     
520C: 1E 30          LD      E,$30           
520E: 00             NOP                     
520F: 00             NOP                     
5210: 00             NOP                     
5211: 1F             RRA                     
5212: 32 00 00       LD      ($0000),A       
5215: 00             NOP                     
5216: 21 2B 00       LD      HL,$002B        
5219: 00             NOP                     
521A: 00             NOP                     
521B: 22 2D 00       LD      ($002D),HL      
521E: 00             NOP                     
521F: 00             NOP                     
5220: 23             INC     HL              
5221: 2C             INC     L               
5222: 00             NOP                     
5223: 00             NOP                     
5224: 00             NOP                     
5225: 25             DEC     H               
5226: 2C             INC     L               
5227: 00             NOP                     
5228: 20 00          JR      NZ,$522A        
522A: 06 21          LD      B,$21           
522C: 00             NOP                     
522D: 00             NOP                     
522E: 00             NOP                     
522F: 25             DEC     H               
5230: 21 01 00       LD      HL,$0001        
5233: 80             ADD     A,B             
5234: 3D             DEC     A               
5235: 21 05 00       LD      HL,$0005        
5238: 80             ADD     A,B             
5239: 36 21          LD      (HL),$21        
523B: 06 00          LD      B,$00           
523D: 80             ADD     A,B             
523E: 37             SCF                     
523F: 21 04 00       LD      HL,$0004        
5242: 80             ADD     A,B             
5243: 38 21          JR      C,$5266         
5245: 07             RLCA                    
5246: 00             NOP                     
5247: 80             ADD     A,B             
5248: 17             RLA                     
5249: 21 08 00       LD      HL,$0008        
524C: 80             ADD     A,B             
524D: 17             RLA                     
524E: 21 0B 00       LD      HL,$000B        
5251: 80             ADD     A,B             
5252: 26 23          LD      H,$23           
5254: 00             NOP                     
5255: 80             ADD     A,B             
5256: 00             NOP                     
5257: 27             DAA                     
5258: 23             INC     HL              
5259: 08             EX      AF,AF'          
525A: 00             NOP                     
525B: 80             ADD     A,B             
525C: 27             DAA                     
525D: 23             INC     HL              
525E: 05             DEC     B               
525F: 00             NOP                     
5260: 80             ADD     A,B             
5261: 27             DAA                     
5262: 24             INC     H               
5263: 02             LD      (BC),A          
5264: 10 80          DJNZ    $51E6           
5266: 28 24          JR      Z,$528C         
5268: 01 80 10       LD      BC,$1080        
526B: 29             ADD     HL,HL           
526C: 26 00          LD      H,$00           
526E: 80             ADD     A,B             
526F: 00             NOP                     
5270: 2A 28 00       LD      HL,($0028)      
5273: 00             NOP                     
5274: 00             NOP                     
5275: 2C             INC     L               
5276: 1C             INC     E               
5277: 00             NOP                     
5278: 80             ADD     A,B             
5279: 00             NOP                     
527A: 2D             DEC     L               
527B: 1F             RRA                     
527C: 00             NOP                     
527D: 00             NOP                     
527E: 00             NOP                     
527F: 2F             CPL                     
5280: 1F             RRA                     
5281: 0B             DEC     BC              
5282: 00             NOP                     
5283: 00             NOP                     
5284: 2F             CPL                     
5285: 09             ADD     HL,BC           
5286: 07             RLCA                    
5287: 00             NOP                     
5288: 00             NOP                     
5289: 2F             CPL                     
528A: 1A             LD      A,(DE)          
528B: 00             NOP                     
528C: 80             ADD     A,B             
528D: 00             NOP                     
528E: 31 20 09       LD      SP,$0920        
5291: 00             NOP                     
5292: 80             ADD     A,B             
5293: 34             INC     (HL)            
5294: 20 05          JR      NZ,$529B        
5296: 00             NOP                     
5297: 80             ADD     A,B             
5298: 36 20          LD      (HL),$20        
529A: 06 00          LD      B,$00           
529C: 80             ADD     A,B             
529D: 37             SCF                     
529E: 20 0C          JR      NZ,$52AC        
52A0: 00             NOP                     
52A1: 80             ADD     A,B             
52A2: 35             DEC     (HL)            
52A3: 1D             DEC     E               
52A4: 09             ADD     HL,BC           
52A5: 00             NOP                     
52A6: 80             ADD     A,B             
52A7: 34             INC     (HL)            
52A8: 1D             DEC     E               
52A9: 05             DEC     B               
52AA: 00             NOP                     
52AB: 80             ADD     A,B             
52AC: 36 1D          LD      (HL),$1D        
52AE: 06 00          LD      B,$00           
52B0: 80             ADD     A,B             
52B1: 37             SCF                     
52B2: 1D             DEC     E               
52B3: 0C             INC     C               
52B4: 00             NOP                     
52B5: 80             ADD     A,B             
52B6: 35             DEC     (HL)            
52B7: 36 00          LD      (HL),$00        
52B9: 00             NOP                     
52BA: 00             NOP                     
52BB: 3E 37          LD      A,$37           
52BD: 00             NOP                     
52BE: 00             NOP                     
52BF: 00             NOP                     
52C0: 3F             CCF                     
52C1: 00             NOP                     
52C2: 00             NOP                     
52C3: 04             INC     B               
52C4: 52             LD      D,D             
52C5: 45             LD      B,L             
52C6: 41             LD      B,C             
52C7: 44             LD      B,H             
52C8: 01 03 47       LD      BC,$4703        
52CB: 45             LD      B,L             
52CC: 54             LD      D,H             
52CD: 09             ADD     HL,BC           
52CE: 05             DEC     B               
52CF: 54             LD      D,H             
52D0: 48             LD      C,B             
52D1: 52             LD      D,D             
52D2: 4F             LD      C,A             
52D3: 57             LD      D,A             
52D4: 03             INC     BC              
52D5: 06 41          LD      B,$41           
52D7: 54             LD      D,H             
52D8: 54             LD      D,H             
52D9: 41             LD      B,C             
52DA: 43             LD      B,E             
52DB: 4B             LD      C,E             
52DC: 04             INC     B               
52DD: 04             INC     B               
52DE: 4B             LD      C,E             
52DF: 49             LD      C,C             
52E0: 4C             LD      C,H             
52E1: 4C             LD      C,H             
52E2: 04             INC     B               
52E3: 03             INC     BC              
52E4: 48             LD      C,B             
52E5: 49             LD      C,C             
52E6: 54             LD      D,H             
52E7: 04             INC     B               
52E8: 06 44          LD      B,$44           
52EA: 45             LD      B,L             
52EB: 53             LD      D,E             
52EC: 54             LD      D,H             
52ED: 52             LD      D,D             
52EE: 4F             LD      C,A             
52EF: 04             INC     B               
52F0: 05             DEC     B               
52F1: 4E             LD      C,(HL)          
52F2: 4F             LD      C,A             
52F3: 52             LD      D,D             
52F4: 54             LD      D,H             
52F5: 48             LD      C,B             
52F6: 05             DEC     B               
52F7: 01 4E 05       LD      BC,$054E        
52FA: 05             DEC     B               
52FB: 53             LD      D,E             
52FC: 4F             LD      C,A             
52FD: 55             LD      D,L             
52FE: 54             LD      D,H             
52FF: 48             LD      C,B             
5300: 06 01          LD      B,$01           
5302: 53             LD      D,E             
5303: 06 04          LD      B,$04           
5305: 45             LD      B,L             
5306: 41             LD      B,C             
5307: 53             LD      D,E             
5308: 54             LD      D,H             
5309: 07             RLCA                    
530A: 01 45 07       LD      BC,$0745        
530D: 04             INC     B               
530E: 57             LD      D,A             
530F: 45             LD      B,L             
5310: 53             LD      D,E             
5311: 54             LD      D,H             
5312: 08             EX      AF,AF'          
5313: 01 57 08       LD      BC,$0857        
5316: 04             INC     B               
5317: 54             LD      D,H             
5318: 41             LD      B,C             
5319: 4B             LD      C,E             
531A: 45             LD      B,L             
531B: 09             ADD     HL,BC           
531C: 05             DEC     B               
531D: 43             LD      B,E             
531E: 41             LD      B,C             
531F: 52             LD      D,D             
5320: 52             LD      D,D             
5321: 59             LD      E,C             
5322: 09             ADD     HL,BC           
5323: 04             INC     B               
5324: 44             LD      B,H             
5325: 52             LD      D,D             
5326: 4F             LD      C,A             
5327: 50             LD      D,B             
5328: 0A             LD      A,(BC)          
5329: 03             INC     BC              
532A: 50             LD      D,B             
532B: 55             LD      D,L             
532C: 54             LD      D,H             
532D: 0A             LD      A,(BC)          
532E: 06 49          LD      B,$49           
5330: 4E             LD      C,(HL)          
5331: 56             LD      D,(HL)          
5332: 45             LD      B,L             
5333: 4E             LD      C,(HL)          
5334: 54             LD      D,H             
5335: 0B             DEC     BC              
5336: 04             INC     B               
5337: 4C             LD      C,H             
5338: 4F             LD      C,A             
5339: 4F             LD      C,A             
533A: 4B             LD      C,E             
533B: 0C             INC     C               
533C: 04             INC     B               
533D: 47             LD      B,A             
533E: 49             LD      C,C             
533F: 56             LD      D,(HL)          
5340: 45             LD      B,L             
5341: 0D             DEC     C               
5342: 05             DEC     B               
5343: 4F             LD      C,A             
5344: 46             LD      B,(HL)          
5345: 46             LD      B,(HL)          
5346: 45             LD      B,L             
5347: 52             LD      D,D             
5348: 0D             DEC     C               
5349: 06 45          LD      B,$45           
534B: 58             LD      E,B             
534C: 41             LD      B,C             
534D: 4D             LD      C,L             
534E: 49             LD      C,C             
534F: 4E             LD      C,(HL)          
5350: 0E 06          LD      C,$06           
5352: 44             LD      B,H             
5353: 45             LD      B,L             
5354: 53             LD      D,E             
5355: 43             LD      B,E             
5356: 52             LD      D,D             
5357: 49             LD      C,C             
5358: 0E 06          LD      C,$06           
535A: 53             LD      D,E             
535B: 45             LD      B,L             
535C: 41             LD      B,C             
535D: 52             LD      D,D             
535E: 43             LD      B,E             
535F: 48             LD      C,B             
5360: 0E 04          LD      C,$04           
5362: 4F             LD      C,A             
5363: 50             LD      D,B             
5364: 45             LD      B,L             
5365: 4E             LD      C,(HL)          
5366: 0F             RRCA                    
5367: 04             INC     B               
5368: 50             LD      D,B             
5369: 55             LD      D,L             
536A: 4C             LD      C,H             
536B: 4C             LD      C,H             
536C: 10 05          DJNZ    $5373           
536E: 4C             LD      C,H             
536F: 49             LD      C,C             
5370: 47             LD      B,A             
5371: 48             LD      C,B             
5372: 54             LD      D,H             
5373: 11 04 42       LD      DE,$4204        
5376: 55             LD      D,L             
5377: 52             LD      D,D             
5378: 4E             LD      C,(HL)          
5379: 11 06 49       LD      DE,$4906        
537C: 47             LD      B,A             
537D: 4E             LD      C,(HL)          
537E: 49             LD      C,C             
537F: 54             LD      D,H             
5380: 45             LD      B,L             
5381: 11 03 45       LD      DE,$4503        
5384: 41             LD      B,C             
5385: 54             LD      D,H             
5386: 12             LD      (DE),A          
5387: 05             DEC     B               
5388: 54             LD      D,H             
5389: 41             LD      B,C             
538A: 53             LD      D,E             
538B: 54             LD      D,H             
538C: 45             LD      B,L             
538D: 12             LD      (DE),A          
538E: 04             INC     B               
538F: 42             LD      B,D             
5390: 4C             LD      C,H             
5391: 4F             LD      C,A             
5392: 57             LD      D,A             
5393: 13             INC     DE              
5394: 06 45          LD      B,$45           
5396: 58             LD      E,B             
5397: 54             LD      D,H             
5398: 49             LD      C,C             
5399: 4E             LD      C,(HL)          
539A: 47             LD      B,A             
539B: 14             INC     D               
539C: 05             DEC     B               
539D: 43             LD      B,E             
539E: 4C             LD      C,H             
539F: 49             LD      C,C             
53A0: 4D             LD      C,L             
53A1: 42             LD      B,D             
53A2: 15             DEC     D               
53A3: 06 41          LD      B,$41           
53A5: 53             LD      D,E             
53A6: 43             LD      B,E             
53A7: 45             LD      B,L             
53A8: 4E             LD      C,(HL)          
53A9: 44             LD      B,H             
53AA: 15             DEC     D               
53AB: 06 44          LD      B,$44           
53AD: 45             LD      B,L             
53AE: 53             LD      D,E             
53AF: 43             LD      B,E             
53B0: 45             LD      B,L             
53B1: 4E             LD      C,(HL)          
53B2: 15             DEC     D               
53B3: 03             INC     BC              
53B4: 52             LD      D,D             
53B5: 55             LD      D,L             
53B6: 42             LD      B,D             
53B7: 16 04          LD      D,$04           
53B9: 57             LD      D,A             
53BA: 49             LD      C,C             
53BB: 50             LD      D,B             
53BC: 45             LD      B,L             
53BD: 16 06          LD      D,$06           
53BF: 50             LD      D,B             
53C0: 4F             LD      C,A             
53C1: 4C             LD      C,H             
53C2: 49             LD      C,C             
53C3: 53             LD      D,E             
53C4: 48             LD      C,B             
53C5: 16 06          LD      D,$06           
53C7: 44             LD      B,H             
53C8: 49             LD      C,C             
53C9: 41             LD      B,C             
53CA: 47             LD      B,A             
53CB: 4E             LD      C,(HL)          
53CC: 4F             LD      C,A             
53CD: 17             RLA                     
53CE: 04             INC     B               
53CF: 46             LD      B,(HL)          
53D0: 49             LD      C,C             
53D1: 4E             LD      C,(HL)          
53D2: 44             LD      B,H             
53D3: 1A             LD      A,(DE)          
53D4: 04             INC     B               
53D5: 4C             LD      C,H             
53D6: 49             LD      C,C             
53D7: 46             LD      B,(HL)          
53D8: 54             LD      D,H             
53D9: 1C             INC     E               
53DA: 04             INC     B               
53DB: 53             LD      D,E             
53DC: 54             LD      D,H             
53DD: 45             LD      B,L             
53DE: 50             LD      D,B             
53DF: 1D             DEC     E               
53E0: 04             INC     B               
53E1: 57             LD      D,A             
53E2: 41             LD      B,C             
53E3: 49             LD      C,C             
53E4: 54             LD      D,H             
53E5: 1F             RRA                     
53E6: 04             INC     B               
53E7: 53             LD      D,E             
53E8: 54             LD      D,H             
53E9: 41             LD      B,C             
53EA: 59             LD      E,C             
53EB: 1F             RRA                     
53EC: 04             INC     B               
53ED: 4A             LD      C,D             
53EE: 55             LD      D,L             
53EF: 4D             LD      C,L             
53F0: 50             LD      D,B             
53F1: 20 02          JR      NZ,$53F5        
53F3: 47             LD      B,A             
53F4: 4F             LD      C,A             
53F5: 21 03 52       LD      HL,$5203        
53F8: 55             LD      D,L             
53F9: 4E             LD      C,(HL)          
53FA: 21 04 4C       LD      HL,$4C04        
53FD: 45             LD      B,L             
53FE: 46             LD      B,(HL)          
53FF: 54             LD      D,H             
5400: 21 05 52       LD      HL,$5205        
5403: 49             LD      C,C             
5404: 47             LD      B,A             
5405: 48             LD      C,B             
5406: 54             LD      D,H             
5407: 21 05 45       LD      HL,$4505        
540A: 4E             LD      C,(HL)          
540B: 54             LD      D,H             
540C: 45             LD      B,L             
540D: 52             LD      D,D             
540E: 21 04 50       LD      HL,$5004        
5411: 55             LD      D,L             
5412: 53             LD      D,E             
5413: 48             LD      C,B             
5414: 10 04          DJNZ    $541A           
5416: 4D             LD      C,L             
5417: 4F             LD      C,A             
5418: 56             LD      D,(HL)          
5419: 45             LD      B,L             
541A: 10 04          DJNZ    $5420           
541C: 4B             LD      C,E             
541D: 49             LD      C,C             
541E: 43             LD      B,E             
541F: 4B             LD      C,E             
5420: 23             INC     HL              
5421: 04             INC     B               
5422: 46             LD      B,(HL)          
5423: 45             LD      B,L             
5424: 45             LD      B,L             
5425: 44             LD      B,H             
5426: 24             INC     H               
5427: 05             DEC     B               
5428: 44             LD      B,H             
5429: 52             LD      D,D             
542A: 49             LD      C,C             
542B: 4E             LD      C,(HL)          
542C: 4B             LD      C,E             
542D: 25             DEC     H               
542E: 03             INC     BC              
542F: 55             LD      D,L             
5430: 53             LD      D,E             
5431: 45             LD      B,L             
5432: 26 03          LD      H,$03           
5434: 53             LD      D,E             
5435: 41             LD      B,C             
5436: 59             LD      E,C             
5437: 27             DAA                     
5438: 05             DEC     B               
5439: 53             LD      D,E             
543A: 43             LD      B,E             
543B: 4F             LD      C,A             
543C: 52             LD      D,D             
543D: 45             LD      B,L             
543E: 28 04          JR      Z,$5444         
5440: 50             LD      D,B             
5441: 4F             LD      C,A             
5442: 55             LD      D,L             
5443: 52             LD      D,D             
5444: 29             ADD     HL,HL           
5445: 04             INC     B               
5446: 46             LD      B,(HL)          
5447: 49             LD      C,C             
5448: 4C             LD      C,H             
5449: 4C             LD      C,H             
544A: 2A 06 53       LD      HL,($5306)      
544D: 43             LD      B,E             
544E: 52             LD      D,D             
544F: 45             LD      B,L             
5450: 41             LD      B,C             
5451: 4D             LD      C,L             
5452: 2B             DEC     HL              
5453: 04             INC     B               
5454: 59             LD      E,C             
5455: 45             LD      B,L             
5456: 4C             LD      C,H             
5457: 4C             LD      C,H             
5458: 2B             DEC     HL              
5459: 04             INC     B               
545A: 51             LD      D,C             
545B: 55             LD      D,L             
545C: 49             LD      C,C             
545D: 54             LD      D,H             
545E: 2D             DEC     L               
545F: 04             INC     B               
5460: 53             LD      D,E             
5461: 54             LD      D,H             
5462: 4F             LD      C,A             
5463: 50             LD      D,B             
5464: 2D             DEC     L               
5465: 03             INC     BC              
5466: 59             LD      E,C             
5467: 45             LD      B,L             
5468: 53             LD      D,E             
5469: 2F             CPL                     
546A: 02             LD      (BC),A          
546B: 4E             LD      C,(HL)          
546C: 4F             LD      C,A             
546D: 30 05          JR      NC,$5474        
546F: 50             LD      D,B             
5470: 4C             LD      C,H             
5471: 55             LD      D,L             
5472: 47             LD      B,A             
5473: 48             LD      C,B             
5474: 32 05 4C       LD      ($4C05),A       
5477: 45             LD      B,L             
5478: 41             LD      B,C             
5479: 56             LD      D,(HL)          
547A: 45             LD      B,L             
547B: 2C             INC     L               
547C: 04             INC     B               
547D: 50             LD      D,B             
547E: 49             LD      C,C             
547F: 43             LD      B,E             
5480: 4B             LD      C,E             
5481: 34             INC     (HL)            
5482: 04             INC     B               
5483: 4C             LD      C,H             
5484: 4F             LD      C,A             
5485: 41             LD      B,C             
5486: 44             LD      B,H             
5487: 36 04          LD      (HL),$04        
5489: 53             LD      D,E             
548A: 41             LD      B,C             
548B: 56             LD      D,(HL)          
548C: 45             LD      B,L             
548D: 37             SCF                     
548E: 00             NOP                     
548F: 06 42          LD      B,$42           
5491: 4F             LD      C,A             
5492: 54             LD      D,H             
5493: 54             LD      D,H             
5494: 4C             LD      C,H             
5495: 45             LD      B,L             
5496: 01 06 50       LD      BC,$5006        
5499: 4F             LD      C,A             
549A: 54             LD      D,H             
549B: 49             LD      C,C             
549C: 4F             LD      C,A             
549D: 4E             LD      C,(HL)          
549E: 03             INC     BC              
549F: 03             INC     BC              
54A0: 52             LD      D,D             
54A1: 55             LD      D,L             
54A2: 47             LD      B,A             
54A3: 06 04          LD      B,$04           
54A5: 44             LD      B,H             
54A6: 4F             LD      C,A             
54A7: 4F             LD      C,A             
54A8: 52             LD      D,D             
54A9: 09             ADD     HL,BC           
54AA: 04             INC     B               
54AB: 46             LD      B,(HL)          
54AC: 4F             LD      C,A             
54AD: 4F             LD      C,A             
54AE: 44             LD      B,H             
54AF: 0C             INC     C               
54B0: 06 53          LD      B,$53           
54B2: 54             LD      D,H             
54B3: 41             LD      B,C             
54B4: 54             LD      D,H             
54B5: 55             LD      D,L             
54B6: 45             LD      B,L             
54B7: 0D             DEC     C               
54B8: 05             DEC     B               
54B9: 53             LD      D,E             
54BA: 57             LD      D,A             
54BB: 4F             LD      C,A             
54BC: 52             LD      D,D             
54BD: 44             LD      B,H             
54BE: 0E 06          LD      C,$06           
54C0: 47             LD      B,A             
54C1: 41             LD      B,C             
54C2: 52             LD      D,D             
54C3: 47             LD      B,A             
54C4: 4F             LD      C,A             
54C5: 59             LD      E,C             
54C6: 0F             RRCA                    
54C7: 04             INC     B               
54C8: 52             LD      D,D             
54C9: 49             LD      C,C             
54CA: 4E             LD      C,(HL)          
54CB: 47             LD      B,A             
54CC: 12             LD      (DE),A          
54CD: 03             INC     BC              
54CE: 47             LD      B,A             
54CF: 45             LD      B,L             
54D0: 4D             LD      C,L             
54D1: 13             INC     DE              
54D2: 05             DEC     B               
54D3: 4C             LD      C,H             
54D4: 45             LD      B,L             
54D5: 56             LD      D,(HL)          
54D6: 45             LD      B,L             
54D7: 52             LD      D,D             
54D8: 16 06          LD      D,$06           
54DA: 50             LD      D,B             
54DB: 4C             LD      C,H             
54DC: 41             LD      B,C             
54DD: 51             LD      D,C             
54DE: 55             LD      D,L             
54DF: 45             LD      B,L             
54E0: 18 05          JR      $54E7           
54E2: 52             LD      D,D             
54E3: 55             LD      D,L             
54E4: 4E             LD      C,(HL)          
54E5: 45             LD      B,L             
54E6: 53             LD      D,E             
54E7: 18 04          JR      $54ED           
54E9: 53             LD      D,E             
54EA: 49             LD      C,C             
54EB: 47             LD      B,A             
54EC: 4E             LD      C,(HL)          
54ED: 18 06          JR      $54F5           
54EF: 4D             LD      C,L             
54F0: 45             LD      B,L             
54F1: 53             LD      D,E             
54F2: 53             LD      D,E             
54F3: 41             LD      B,C             
54F4: 47             LD      B,A             
54F5: 18 06          JR      $54FD           
54F7: 43             LD      B,E             
54F8: 41             LD      B,C             
54F9: 4E             LD      C,(HL)          
54FA: 44             LD      B,H             
54FB: 4C             LD      C,H             
54FC: 45             LD      B,L             
54FD: 19             ADD     HL,DE           
54FE: 04             INC     B               
54FF: 4C             LD      C,H             
5500: 41             LD      B,C             
5501: 4D             LD      C,L             
5502: 50             LD      D,B             
5503: 1B             DEC     DE              
5504: 06 43          LD      B,$43           
5506: 48             LD      C,B             
5507: 4F             LD      C,A             
5508: 50             LD      D,B             
5509: 53             LD      D,E             
550A: 54             LD      D,H             
550B: 1E 04          LD      E,$04           
550D: 48             LD      C,B             
550E: 41             LD      B,C             
550F: 4E             LD      C,(HL)          
5510: 44             LD      B,H             
5511: 1F             RRA                     
5512: 05             DEC     B               
5513: 48             LD      C,B             
5514: 41             LD      B,C             
5515: 4E             LD      C,(HL)          
5516: 44             LD      B,H             
5517: 53             LD      D,E             
5518: 1F             RRA                     
5519: 04             INC     B               
551A: 43             LD      B,E             
551B: 4F             LD      C,A             
551C: 49             LD      C,C             
551D: 4E             LD      C,(HL)          
551E: 20 04          JR      NZ,$5524        
5520: 53             LD      D,E             
5521: 4C             LD      C,H             
5522: 4F             LD      C,A             
5523: 54             LD      D,H             
5524: 21 05 41       LD      HL,$4105        
5527: 4C             LD      C,H             
5528: 54             LD      D,H             
5529: 41             LD      B,C             
552A: 52             LD      D,D             
552B: 22 04 49       LD      ($4904),HL      
552E: 44             LD      B,H             
552F: 4F             LD      C,A             
5530: 4C             LD      C,H             
5531: 23             INC     HL              
5532: 06 53          LD      B,$53           
5534: 45             LD      B,L             
5535: 52             LD      D,D             
5536: 50             LD      D,B             
5537: 45             LD      B,L             
5538: 4E             LD      C,(HL)          
5539: 24             INC     H               
553A: 05             DEC     B               
553B: 53             LD      D,E             
553C: 4E             LD      C,(HL)          
553D: 41             LD      B,C             
553E: 4B             LD      C,E             
553F: 45             LD      B,L             
5540: 24             INC     H               
5541: 04             INC     B               
5542: 57             LD      D,A             
5543: 41             LD      B,C             
5544: 4C             LD      C,H             
5545: 4C             LD      C,H             
5546: 25             DEC     H               
5547: 05             DEC     B               
5548: 57             LD      D,A             
5549: 41             LD      B,C             
554A: 4C             LD      C,H             
554B: 4C             LD      C,H             
554C: 53             LD      D,E             
554D: 25             DEC     H               
554E: 04             INC     B               
554F: 56             LD      D,(HL)          
5550: 49             LD      C,C             
5551: 4E             LD      C,(HL)          
5552: 45             LD      B,L             
5553: 26 05          LD      H,$05           
5555: 56             LD      D,(HL)          
5556: 49             LD      C,C             
5557: 4E             LD      C,(HL)          
5558: 45             LD      B,L             
5559: 53             LD      D,E             
555A: 26 04          LD      H,$04           
555C: 47             LD      B,A             
555D: 41             LD      B,C             
555E: 54             LD      D,H             
555F: 45             LD      B,L             
5560: 27             DAA                     
5561: 05             DEC     B               
5562: 47             LD      B,A             
5563: 41             LD      B,C             
5564: 54             LD      D,H             
5565: 45             LD      B,L             
5566: 53             LD      D,E             
5567: 27             DAA                     
5568: 05             DEC     B               
5569: 47             LD      B,A             
556A: 55             LD      D,L             
556B: 41             LD      B,C             
556C: 52             LD      D,D             
556D: 44             LD      B,H             
556E: 28 06          JR      Z,$5576         
5570: 47             LD      B,A             
5571: 55             LD      D,L             
5572: 41             LD      B,C             
5573: 52             LD      D,D             
5574: 44             LD      B,H             
5575: 53             LD      D,E             
5576: 28 04          JR      Z,$557C         
5578: 52             LD      D,D             
5579: 4F             LD      C,A             
557A: 4F             LD      C,A             
557B: 4D             LD      C,L             
557C: 2A 05 46       LD      HL,($4605)      
557F: 4C             LD      C,H             
5580: 4F             LD      C,A             
5581: 4F             LD      C,A             
5582: 52             LD      D,D             
5583: 2B             DEC     HL              
5584: 04             INC     B               
5585: 45             LD      B,L             
5586: 58             LD      E,B             
5587: 49             LD      C,C             
5588: 54             LD      D,H             
5589: 2C             INC     L               
558A: 06 50          LD      B,$50           
558C: 41             LD      B,C             
558D: 53             LD      D,E             
558E: 53             LD      D,E             
558F: 41             LD      B,C             
5590: 47             LD      B,A             
5591: 2D             DEC     L               
5592: 04             INC     B               
5593: 48             LD      C,B             
5594: 4F             LD      C,A             
5595: 4C             LD      C,H             
5596: 45             LD      B,L             
5597: 2E 06          LD      L,$06           
5599: 43             LD      B,E             
559A: 4F             LD      C,A             
559B: 52             LD      D,D             
559C: 52             LD      D,D             
559D: 49             LD      C,C             
559E: 44             LD      B,H             
559F: 2F             CPL                     
55A0: 03             INC     BC              
55A1: 42             LD      B,D             
55A2: 4F             LD      C,A             
55A3: 57             LD      D,A             
55A4: 31 05 41       LD      SP,$4105        
55A7: 52             LD      D,D             
55A8: 52             LD      D,D             
55A9: 4F             LD      C,A             
55AA: 57             LD      D,A             
55AB: 32 06 48       LD      ($4806),A       
55AE: 41             LD      B,C             
55AF: 4C             LD      C,H             
55B0: 4C             LD      C,H             
55B1: 57             LD      D,A             
55B2: 41             LD      B,C             
55B3: 33             INC     SP              
55B4: 06 43          LD      B,$43           
55B6: 48             LD      C,B             
55B7: 41             LD      B,C             
55B8: 4D             LD      C,L             
55B9: 42             LD      B,D             
55BA: 45             LD      B,L             
55BB: 34             INC     (HL)            
55BC: 05             DEC     B               
55BD: 56             LD      D,(HL)          
55BE: 41             LD      B,C             
55BF: 55             LD      D,L             
55C0: 4C             LD      C,H             
55C1: 54             LD      D,H             
55C2: 35             DEC     (HL)            
55C3: 06 45          LD      B,$45           
55C5: 4E             LD      C,(HL)          
55C6: 54             LD      D,H             
55C7: 52             LD      D,D             
55C8: 41             LD      B,C             
55C9: 4E             LD      C,(HL)          
55CA: 36 06          LD      (HL),$06        
55CC: 54             LD      D,H             
55CD: 55             LD      D,L             
55CE: 4E             LD      C,(HL)          
55CF: 4E             LD      C,(HL)          
55D0: 45             LD      B,L             
55D1: 4C             LD      C,H             
55D2: 37             SCF                     
55D3: 06 4A          LD      B,$4A           
55D5: 55             LD      D,L             
55D6: 4E             LD      C,(HL)          
55D7: 47             LD      B,A             
55D8: 4C             LD      C,H             
55D9: 45             LD      B,L             
55DA: 38 06          JR      C,$55E2         
55DC: 54             LD      D,H             
55DD: 45             LD      B,L             
55DE: 4D             LD      C,L             
55DF: 50             LD      D,B             
55E0: 4C             LD      C,H             
55E1: 45             LD      B,L             
55E2: 39             ADD     HL,SP           
55E3: 03             INC     BC              
55E4: 50             LD      D,B             
55E5: 49             LD      C,C             
55E6: 54             LD      D,H             
55E7: 3A 06 43       LD      A,($4306)       
55EA: 45             LD      B,L             
55EB: 49             LD      C,C             
55EC: 4C             LD      C,H             
55ED: 49             LD      C,C             
55EE: 4E             LD      C,(HL)          
55EF: 3B             DEC     SP              
55F0: 04             INC     B               
55F1: 52             LD      D,D             
55F2: 4F             LD      C,A             
55F3: 4F             LD      C,A             
55F4: 46             LD      B,(HL)          
55F5: 3B             DEC     SP              
55F6: 00             NOP                     
55F7: 00             NOP                     
55F8: 02             LD      (BC),A          
55F9: 54             LD      D,H             
55FA: 4F             LD      C,A             
55FB: 01 04 57       LD      BC,$5704        
55FE: 49             LD      C,C             
55FF: 54             LD      D,H             
5600: 48             LD      C,B             
5601: 02             LD      (BC),A          
5602: 02             LD      (BC),A          
5603: 41             LD      B,C             
5604: 54             LD      D,H             
5605: 03             INC     BC              
5606: 05             DEC     B               
5607: 55             LD      D,L             
5608: 4E             LD      C,(HL)          
5609: 44             LD      B,H             
560A: 45             LD      B,L             
560B: 52             LD      D,D             
560C: 04             INC     B               
560D: 02             LD      (BC),A          
560E: 49             LD      C,C             
560F: 4E             LD      C,(HL)          
5610: 05             DEC     B               
5611: 04             INC     B               
5612: 49             LD      C,C             
5613: 4E             LD      C,(HL)          
5614: 54             LD      D,H             
5615: 4F             LD      C,A             
5616: 05             DEC     B               
5617: 06 49          LD      B,$49           
5619: 4E             LD      C,(HL)          
561A: 53             LD      D,E             
561B: 49             LD      C,C             
561C: 44             LD      B,H             
561D: 45             LD      B,L             
561E: 05             DEC     B               
561F: 03             INC     BC              
5620: 4F             LD      C,A             
5621: 55             LD      D,L             
5622: 54             LD      D,H             
5623: 06 06          LD      B,$06           
5625: 4F             LD      C,A             
5626: 55             LD      D,L             
5627: 54             LD      D,H             
5628: 53             LD      D,E             
5629: 49             LD      C,C             
562A: 44             LD      B,H             
562B: 06 02          LD      B,$02           
562D: 55             LD      D,L             
562E: 50             LD      D,B             
562F: 07             RLCA                    
5630: 04             INC     B               
5631: 44             LD      B,H             
5632: 4F             LD      C,A             
5633: 57             LD      D,A             
5634: 4E             LD      C,(HL)          
5635: 08             EX      AF,AF'          
5636: 04             INC     B               
5637: 4F             LD      C,A             
5638: 56             LD      D,(HL)          
5639: 45             LD      B,L             
563A: 52             LD      D,D             
563B: 09             ADD     HL,BC           
563C: 06 42          LD      B,$42           
563E: 45             LD      B,L             
563F: 48             LD      C,B             
5640: 49             LD      C,C             
5641: 4E             LD      C,(HL)          
5642: 44             LD      B,H             
5643: 0A             LD      A,(BC)          
5644: 06 41          LD      B,$41           
5646: 52             LD      D,D             
5647: 4F             LD      C,A             
5648: 55             LD      D,L             
5649: 4E             LD      C,(HL)          
564A: 44             LD      B,H             
564B: 0B             DEC     BC              
564C: 02             LD      (BC),A          
564D: 4F             LD      C,A             
564E: 4E             LD      C,(HL)          
564F: 0C             INC     C               
5650: 00             NOP                     
5651: 00             NOP                     
5652: 91             SUB     C               
5653: CB 01          RLC     C               
5655: 47             LD      B,A             
5656: 81             ADD     A,C             
5657: 00             NOP                     
5658: A0             AND     B               
5659: 03             INC     BC              
565A: 1E 5F          LD      E,$5F           
565C: BE             CP      (HL)            
565D: 5B             LD      E,E             
565E: B1             OR      C               
565F: 4B             LD      C,E             
5660: 7B             LD      A,E             
5661: 55             LD      D,L             
5662: 45             LD      B,L             
5663: 8E             ADC     A,(HL)          
5664: 91             SUB     C               
5665: 04             INC     B               
5666: 8A             ADC     A,D             
5667: 0E A1          LD      C,$A1           
5669: DB 8B          IN      A,($8B)         
566B: 56             LD      D,(HL)          
566C: B8             CP      B               
566D: 90             SUB     B               
566E: BE             CP      (HL)            
566F: D1             POP     DE              
5670: 6A             LD      L,D             
5671: 96             SUB     (HL)            
5672: 96             SUB     (HL)            
5673: DB 72          IN      A,($72)         
5675: 89             ADC     A,C             
5676: 67             LD      H,A             
5677: C7             RST     0X00            
5678: A0             AND     B               
5679: 02             LD      (BC),A          
567A: 08             EX      AF,AF'          
567B: E3             EX      (SP),HL         
567C: B8             CP      B               
567D: F3             DI                      
567E: 8C             ADC     A,H             
567F: 06 4F          LD      B,$4F           
5681: FF             RST     0X38            
5682: BE             CP      (HL)            
5683: 07             RLCA                    
5684: 18 0D          JR      $5693           
5686: 16 0A          LD      D,$0A           
5688: 11 04 12       LD      DE,$1204        
568B: 5F             LD      E,A             
568C: BE             CP      (HL)            
568D: B9             CP      C               
568E: 14             INC     D               
568F: 46             LD      B,(HL)          
5690: C0             RET     NZ              
5691: 4B             LD      C,E             
5692: 5E             LD      E,(HL)          
5693: C3 B5 EF       JP      $EFB5           
5696: 8D             ADC     A,L             
5697: 13             INC     DE              
5698: 47             LD      B,A             
5699: C2 16 A7       JP      NZ,$A716        
569C: 61             LD      H,C   

; Object_02. Different before ??
          
569D: 03             INC     BC    
569E: 03             INC     BC              
569F: 00             NOP                     
56A0: 00             NOP                     
56A1: 00             NOP                     
56A2: 06 48          LD      B,$48           
56A4: 82             ADD     A,D             
56A5: 00             NOP                     
56A6: 80             ADD     A,B             
56A7: 02             LD      (BC),A          
56A8: 02             LD      (BC),A          
56A9: E9             JP      (HL)            
56AA: B3             OR      E               
56AB: 07             RLCA                    
56AC: 3F             CCF                     
56AD: 0B             DEC     BC              
56AE: 3D             DEC     A               
56AF: 0A             LD      A,(BC)          
56B0: 0C             INC     C               
56B1: 01 8C 36       LD      BC,$368C        
56B4: 01 8A 33       LD      BC,$338A        
56B7: 01 8A 34       LD      BC,$348A        
56BA: 01 8A 35       LD      BC,$358A        
56BD: 01 8B 2D       LD      BC,$2D8B        
56C0: 01 8C 26       LD      BC,$268C        
56C3: 28 04          JR      Z,$56C9         
56C5: 26 C7          LD      H,$C7           
56C7: DE D3          SBC     $D3             
56C9: 14             INC     D               
56CA: E6 96          AND     $96             
56CC: 16 EE          LD      D,$EE           
56CE: DB 72          IN      A,($72)         
56D0: E9             JP      (HL)            
56D1: B3             OR      E               
56D2: 66             LD      H,(HL)          
56D3: 17             RLA                     
56D4: 76             HALT                    
56D5: B1             OR      C               
56D6: 1F             RRA                     
56D7: 54             LD      D,H             
56D8: C3 B5 F3       JP      $F3B5           
56DB: 8C             ADC     A,H             
56DC: 5F             LD      E,A             
56DD: BE             CP      (HL)            
56DE: F3             DI                      
56DF: 17             RLA                     
56E0: 43             LD      B,E             
56E1: DB B9          IN      A,($B9)         
56E3: 55             LD      D,L             
56E4: CB B9          RES     7,C             
56E6: 5F             LD      E,A             
56E7: BE             CP      (HL)            
56E8: 39             ADD     HL,SP           
56E9: 17             RLA                     
56EA: FF             RST     0X38            
56EB: 9F             SBC     A               
56EC: 09             ADD     HL,BC           
56ED: 5E             LD      E,(HL)          
56EE: 82             ADD     A,D             
56EF: 00             NOP                     
56F0: 84             ADD     A,H             
56F1: 02             LD      (BC),A          
56F2: 03             INC     BC              
56F3: 81             ADD     A,C             
56F4: 5B             LD      E,E             
56F5: 52             LD      D,D             
56F6: 07             RLCA                    
56F7: 54             LD      D,H             
56F8: 0E 52          LD      C,$52           
56FA: 0D             DEC     C               
56FB: 22 0A 08       LD      ($080A),HL      
56FE: 04             INC     B               
56FF: 1E 5F          LD      E,$5F           
5701: BE             CP      (HL)            
5702: D3 14          OUT     ($14),A         
5704: 13             INC     DE              
5705: B4             OR      H               
5706: C5             PUSH    BC              
5707: 98             SBC     B               
5708: C0             RET     NZ              
5709: 16 82          LD      D,$82           
570B: 17             RLA                     
570C: 46             LD      B,(HL)          
570D: 5E             LD      E,(HL)          
570E: 44             LD      B,H             
570F: A0             AND     B               
5710: 53             LD      D,E             
5711: 17             RLA                     
5712: B3             OR      E               
5713: E0             RET     PO              
5714: 49             LD      C,C             
5715: 1B             DEC     DE              
5716: 99             SBC     C               
5717: 16 07          LD      D,$07           
5719: BC             CP      H               
571A: BF             CP      A               
571B: 9A             SBC     D               
571C: 1C             INC     E               
571D: B5             OR      L               
571E: 0D             DEC     C               
571F: 2C             INC     L               
5720: 14             INC     D               
5721: 0A             LD      A,(BC)          
5722: 0B             DEC     BC              
5723: 04             INC     B               
5724: 27             DAA                     
5725: C7             RST     0X00            
5726: DE C6          SBC     $C6             
5728: 22 9B 15       LD      ($159B),HL      
572B: 5B             LD      E,E             
572C: CA 6B BF       JP      Z,$BF6B         
572F: 2B             DEC     HL              
5730: 6E             LD      L,(HL)          
5731: 6B             LD      L,E             
5732: BF             CP      A               
5733: 5F             LD      E,A             
5734: BE             CP      (HL)            
5735: 23             INC     HL              
5736: 15             DEC     D               
5737: F3             DI                      
5738: B9             CP      C               
5739: 46             LD      B,(HL)          
573A: B8             CP      B               
573B: 51             LD      D,C             
573C: 5E             LD      E,(HL)          
573D: 96             SUB     (HL)            
573E: 64             LD      H,H             
573F: DB 72          IN      A,($72)         
5741: 01 B3 56       LD      BC,$56B3        
5744: 90             SUB     B               
5745: C6 9C          ADD     $9C             
5747: D6 9C          SUB     $9C             
5749: 56             LD      D,(HL)          
574A: 72             LD      (HL),D          
574B: 2E 0C          LD      L,$0C           
574D: 2A 84 00       LD      HL,($0084)      
5750: A0             AND     B               
5751: 03             INC     BC              
5752: 0D             DEC     C               
5753: 5F             LD      E,A             
5754: BE             CP      (HL)            
5755: 5B             LD      E,E             
5756: B1             OR      C               
5757: 4B             LD      C,E             
5758: 7B             LD      A,E             
5759: 01 68 0A       LD      BC,$0A68        
575C: 58             LD      E,B             
575D: 2F             CPL                     
575E: 62             LD      H,D             
575F: 2E 07          LD      L,$07           
5761: 11 0D 0F       LD      DE,$0F0D        
5764: 0A             LD      A,(BC)          
5765: 15             DEC     D               
5766: 04             INC     B               
5767: 04             INC     B               
5768: F4 4F AB       CALL    P,$AB4F         
576B: A2             AND     D               
576C: 17             RLA                     
576D: 05             DEC     B               
576E: 00             NOP                     
576F: 1C             INC     E               
5770: 1D             DEC     E               
5771: 23             INC     HL              
5772: 0F             RRCA                    
5773: 02             LD      (BC),A          
5774: 03             INC     BC              
5775: 01 68 44       LD      BC,$4468        
5778: 0D             DEC     C               
5779: 2A 88 00       LD      HL,($0088)      
577C: 80             ADD     A,B             
577D: 02             LD      (BC),A          
577E: 04             INC     B               
577F: FB             EI                      
5780: B9             CP      C               
5781: 67             LD      H,A             
5782: C0             RET     NZ              
5783: 07             RLCA                    
5784: 05             DEC     B               
5785: 0D             DEC     C               
5786: 03             INC     BC              
5787: 0A             LD      A,(BC)          
5788: 12             LD      (DE),A          
5789: 8D             ADC     A,L             
578A: 03             INC     BC              
578B: 18 5F          JR      $57EC           
578D: BE             CP      (HL)            
578E: 66             LD      H,(HL)          
578F: 17             RLA                     
5790: 8F             ADC     A,A             
5791: 49             LD      C,C             
5792: 4B             LD      C,E             
5793: 5E             LD      E,(HL)          
5794: C8             RET     Z               
5795: B5             OR      L               
5796: DB 46          IN      A,($46)         
5798: AB             XOR     E               
5799: 98             SBC     B               
579A: 5F             LD      E,A             
579B: BE             CP      (HL)            
579C: 23             INC     HL              
579D: 15             DEC     D               
579E: F3             DI                      
579F: B9             CP      C               
57A0: 81             ADD     A,C             
57A1: 5B             LD      E,E             
57A2: 1B             DEC     DE              
57A3: B5             OR      L               
57A4: 0D             DEC     C               
57A5: 2A 00 00       LD      HL,($0000)      
57A8: 80             ADD     A,B             
57A9: 02             LD      (BC),A          
57AA: 04             INC     B               
57AB: FB             EI                      
57AC: B9             CP      C               
57AD: 67             LD      H,A             
57AE: C0             RET     NZ              
57AF: 07             RLCA                    
57B0: 05             DEC     B               
57B1: 0D             DEC     C               
57B2: 03             INC     BC              
57B3: 0A             LD      A,(BC)          
57B4: 12             LD      (DE),A          
57B5: 8D             ADC     A,L             
57B6: 03             INC     BC              
57B7: 18 5F          JR      $5818           
57B9: BE             CP      (HL)            
57BA: 66             LD      H,(HL)          
57BB: 17             RLA                     
57BC: 8F             ADC     A,A             
57BD: 49             LD      C,C             
57BE: 4B             LD      C,E             
57BF: 5E             LD      E,(HL)          
57C0: C8             RET     Z               
57C1: B5             OR      L               
57C2: DB 46          IN      A,($46)         
57C4: AB             XOR     E               
57C5: 98             SBC     B               
57C6: 5F             LD      E,A             
57C7: BE             CP      (HL)            
57C8: F7             RST     0X30            
57C9: 17             RLA                     
57CA: F3             DI                      
57CB: B9             CP      C               
57CC: 81             ADD     A,C             
57CD: 5B             LD      E,E             
57CE: 1B             DEC     DE              
57CF: B5             OR      L               
57D0: 12             LD      (DE),A          
57D1: 44             LD      B,H             
57D2: 8C             ADC     A,H             
57D3: 05             DEC     B               
57D4: A4             AND     H               
57D5: 03             INC     BC              
57D6: 14             INC     D               
57D7: 54             LD      D,H             
57D8: 45             LD      B,L             
57D9: 91             SUB     C               
57DA: 7A             LD      A,D             
57DB: B8             CP      B               
57DC: 16 53          LD      D,$53           
57DE: 15             DEC     D               
57DF: 75             LD      (HL),L          
57E0: 98             SBC     B               
57E1: 09             ADD     HL,BC           
57E2: BC             CP      H               
57E3: BE             CP      (HL)            
57E4: 9F             SBC     A               
57E5: D5             PUSH    DE              
57E6: 15             DEC     D               
57E7: 9F             SBC     A               
57E8: 15             DEC     D               
57E9: 7F             LD      A,A             
57EA: B1             OR      C               
57EB: 02             LD      (BC),A          
57EC: 06 3E          LD      B,$3E           
57EE: 6E             LD      L,(HL)          
57EF: 14             INC     D               
57F0: 58             LD      E,B             
57F1: 91             SUB     C               
57F2: 7A             LD      A,D             
57F3: 07             RLCA                    
57F4: 21 0D 1F       LD      HL,$1F0D        
57F7: 0A             LD      A,(BC)          
57F8: 08             EX      AF,AF'          
57F9: 04             INC     B               
57FA: 1B             DEC     DE              
57FB: 5F             LD      E,A             
57FC: BE             CP      (HL)            
57FD: D0             RET     NC              
57FE: 15             DEC     D               
57FF: 64             LD      H,H             
5800: B7             OR      A               
5801: EE 7A          XOR     $7A             
5803: C0             RET     NZ              
5804: 7A             LD      A,D             
5805: 2F             CPL                     
5806: 17             RLA                     
5807: 0D             DEC     C               
5808: 47             LD      B,A             
5809: FC ED 10       CALL    M,$10ED         
580C: B2             OR      D               
580D: D1             POP     DE              
580E: 6A             LD      L,D             
580F: 8F             ADC     A,A             
5810: 64             LD      H,H             
5811: 03             INC     BC              
5812: A1             AND     C               
5813: 27             DAA                     
5814: A0             AND     B               
5815: 22 0E 42       LD      ($420E),HL      
5818: A1             AND     C               
5819: 00             NOP                     
581A: E4 03 19       CALL    PO,$1903        
581D: 5F             LD      E,A             
581E: BE             CP      (HL)            
581F: 5B             LD      E,E             
5820: B1             OR      C               
5821: 4B             LD      C,E             
5822: 7B             LD      A,E             
5823: 4E             LD      C,(HL)          
5824: 45             LD      B,L             
5825: 31 49 55       LD      SP,$5549        
5828: 5E             LD      E,(HL)          
5829: 44             LD      B,H             
582A: D2 0E 58       JP      NC,$580E        
582D: 4B             LD      C,E             
582E: 4A             LD      C,D             
582F: AB             XOR     E               
5830: 98             SBC     B               
5831: 63             LD      H,E             
5832: 98             SBC     B               
5833: 03             INC     BC              
5834: B1             OR      C               
5835: 2E 07          LD      L,$07           
5837: 18 0D          JR      $5846           
5839: 16 0A          LD      D,$0A           
583B: 08             EX      AF,AF'          
583C: 04             INC     B               
583D: 12             LD      (DE),A          
583E: 2C             INC     L               
583F: 1D             DEC     E               
5840: 5F             LD      E,A             
5841: A0             AND     B               
5842: D3 B3          OUT     ($B3),A         
5844: B8             CP      B               
5845: 16 43          LD      D,$43           
5847: 16 57          LD      D,$57           
5849: 63             LD      H,E             
584A: 28 54          JR      Z,$58A0         
584C: BD             CP      L               
584D: 5F             LD      E,A             
584E: 23             INC     HL              
584F: BC             CP      H               
5850: 02             LD      (BC),A          
5851: 08             EX      AF,AF'          
5852: 54             LD      D,H             
5853: 8B             ADC     A,E             
5854: 9B             SBC     E               
5855: 6C             LD      L,H             
5856: 81             ADD     A,C             
5857: BA             CP      D               
5858: 33             INC     SP              
5859: B1             OR      C               
585A: 0F             RRCA                    
585B: 6B             LD      L,E             
585C: 8E             ADC     A,(HL)          
585D: 00             NOP                     
585E: 80             ADD     A,B             
585F: 03             INC     BC              
5860: 34             INC     (HL)            
5861: 5F             LD      E,A             
5862: BE             CP      (HL)            
5863: 5B             LD      E,E             
5864: B1             OR      C               
5865: 4B             LD      C,E             
5866: 7B             LD      A,E             
5867: 4A             LD      C,D             
5868: 45             LD      B,L             
5869: FF             RST     0X38            
586A: 78             LD      A,B             
586B: 35             DEC     (HL)            
586C: A1             AND     C               
586D: 66             LD      H,(HL)          
586E: 17             RLA                     
586F: 0F             RRCA                    
5870: A0             AND     B               
5871: 73             LD      (HL),E          
5872: 15             DEC     D               
5873: C1             POP     BC              
5874: B1             OR      C               
5875: 3F             CCF                     
5876: DE DF          SBC     $DF             
5878: 16 1A          LD      D,$1A           
587A: B1             OR      C               
587B: F3             DI                      
587C: 5F             LD      E,A             
587D: 03             INC     BC              
587E: A0             AND     B               
587F: 4E             LD      C,(HL)          
5880: 45             LD      B,L             
5881: 01 60 43       LD      BC,$4360        
5884: 5E             LD      E,(HL)          
5885: 08             EX      AF,AF'          
5886: 4F             LD      C,A             
5887: 56             LD      D,(HL)          
5888: 5E             LD      E,(HL)          
5889: DB 72          IN      A,($72)         
588B: 04             INC     B               
588C: 9A             SBC     D               
588D: 53             LD      D,E             
588E: BE             CP      (HL)            
588F: 55             LD      D,L             
5890: A4             AND     H               
5891: 09             ADD     HL,BC           
5892: B7             OR      A               
5893: DB 63          IN      A,($63)         
5895: 07             RLCA                    
5896: 24             INC     H               
5897: 0D             DEC     C               
5898: 22 0A 0B       LD      ($0B0A),HL      
589B: 04             INC     B               
589C: 1E 5F          LD      E,$5F           
589E: BE             CP      (HL)            
589F: 5B             LD      E,E             
58A0: B1             OR      C               
58A1: EA 48 94       JP      PE,$9448        
58A4: 5F             LD      E,A             
58A5: D6 B5          SUB     $B5             
58A7: C4 9C 46       CALL    NZ,$469C        
58AA: 5E             LD      E,(HL)          
58AB: 07             RLCA                    
58AC: B2             OR      D               
58AD: 04             INC     B               
58AE: 58             LD      E,B             
58AF: 81             ADD     A,C             
58B0: 8D             ADC     A,L             
58B1: 11 58 8A       LD      DE,$8A58        
58B4: 96             SUB     (HL)            
58B5: 4B             LD      C,E             
58B6: 7B             LD      A,E             
58B7: BB             CP      E               
58B8: 54             LD      D,H             
58B9: C9             RET                     
58BA: D2 02 0A       JP      NC,$0A02        
58BD: 09             ADD     HL,BC           
58BE: BA             CP      D               
58BF: 5B             LD      E,E             
58C0: 98             SBC     B               
58C1: 14             INC     D               
58C2: 6C             LD      L,H             
58C3: 4B             LD      C,E             
58C4: 6E             LD      L,(HL)          
58C5: DB 8B          IN      A,($8B)         
58C7: 22 58 95       LD      ($9558),HL      
58CA: 00             NOP                     
58CB: 80             ADD     A,B             
58CC: 03             INC     BC              
58CD: 32 68 4D       LD      ($4D68),A       
58D0: AF             XOR     A               
58D1: A0             AND     B               
58D2: 51             LD      D,C             
58D3: 18 55          JR      $592A           
58D5: C2 50 BD       JP      NZ,$BD50        
58D8: 0B             DEC     BC              
58D9: 5C             LD      E,H             
58DA: 83             ADD     A,E             
58DB: 48             LD      C,B             
58DC: 4E             LD      C,(HL)          
58DD: 48             LD      C,B             
58DE: 46             LD      B,(HL)          
58DF: 49             LD      C,C             
58E0: 66             LD      H,(HL)          
58E1: 17             RLA                     
58E2: D0             RET     NC              
58E3: 47             LD      B,A             
58E4: F3             DI                      
58E5: 5F             LD      E,A             
58E6: 56             LD      D,(HL)          
58E7: D1             POP     DE              
58E8: 16 71          LD      D,$71           
58EA: DB 72          IN      A,($72)         
58EC: 89             ADC     A,C             
58ED: 4E             LD      C,(HL)          
58EE: 73             LD      (HL),E          
58EF: 9E             SBC     (HL)            
58F0: C3 9E 47       JP      $479E           
58F3: 55             LD      D,L             
58F4: C6 9A          ADD     $9A             
58F6: 65             LD      H,L             
58F7: 62             LD      H,D             
58F8: 53             LD      D,E             
58F9: 17             RLA                     
58FA: B3             OR      E               
58FB: 55             LD      D,L             
58FC: 05             DEC     B               
58FD: 67             LD      H,A             
58FE: 6F             LD      L,A             
58FF: 62             LD      H,D             
5900: 07             RLCA                    
5901: 10 0B          DJNZ    $590E           
5903: 0E 0A          LD      C,$0A           
5905: 12             LD      (DE),A          
5906: 01 8E 0C       LD      BC,$0C8E        
5909: 01 8E 38       LD      BC,$388E        
590C: 05             DEC     B               
590D: 0D             DEC     C               
590E: 03             INC     BC              
590F: 00             NOP                     
5910: A5             AND     L               
5911: 90             SUB     B               
5912: 02             LD      (BC),A          
5913: 0D             DEC     C               
5914: 89             ADC     A,C             
5915: 4E             LD      C,(HL)          
5916: 73             LD      (HL),E          
5917: 9E             SBC     (HL)            
5918: FB             EI                      
5919: B9             CP      C               
591A: 8F             ADC     A,A             
591B: 7A             LD      A,D             
591C: 03             INC     BC              
591D: 58             LD      E,B             
591E: 3B             DEC     SP              
591F: 8E             ADC     A,(HL)          
5920: 52             LD      D,D             
5921: 23             INC     HL              
5922: 2F             CPL                     
5923: 95             SUB     L               
5924: 05             DEC     B               
5925: A0             AND     B               
5926: 03             INC     BC              
5927: 20 49          JR      NZ,$5972        
5929: 45             LD      B,L             
592A: BE             CP      (HL)            
592B: 9F             SBC     A               
592C: 83             ADD     A,E             
592D: 61             LD      H,C             
592E: 09             ADD     HL,BC           
592F: 79             LD      A,C             
5930: 15             DEC     D               
5931: 8A             ADC     A,D             
5932: 50             LD      D,B             
5933: BD             CP      L               
5934: 0B             DEC     BC              
5935: 5C             LD      E,H             
5936: 83             ADD     A,E             
5937: 7A             LD      A,D             
5938: 5F             LD      E,A             
5939: BE             CP      (HL)            
593A: D7             RST     0X10            
593B: 14             INC     D               
593C: BF             CP      A               
593D: 9A             SBC     D               
593E: 91             SUB     C               
593F: AF             XOR     A               
5940: 96             SUB     (HL)            
5941: 64             LD      H,H             
5942: DB 72          IN      A,($72)         
5944: 01 B3 DB       LD      BC,$DBB3        
5947: 95             SUB     L               
5948: 02             LD      (BC),A          
5949: 08             EX      AF,AF'          
594A: 3E 6E          LD      A,$6E           
594C: F0             RET     P               
594D: 59             LD      E,C             
594E: C6 15          ADD     $15             
5950: B3             OR      E               
5951: 9F             SBC     A               
5952: 27             DAA                     
5953: 80             ADD     A,B             
5954: 9A             SBC     D               
5955: 9C             SBC     H               
5956: 00             NOP                     
5957: 80             ADD     A,B             
5958: 03             INC     BC              
5959: 34             INC     (HL)            
595A: AF             XOR     A               
595B: 6E             LD      L,(HL)          
595C: 73             LD      (HL),E          
595D: 49             LD      C,C             
595E: 79             LD      A,C             
595F: 4F             LD      C,A             
5960: AF             XOR     A               
5961: 9B             SBC     E               
5962: 73             LD      (HL),E          
5963: 15             DEC     D               
5964: F5             PUSH    AF              
5965: BD             CP      L               
5966: 30 15          JR      NC,$597D        
5968: AB             XOR     E               
5969: 6E             LD      L,(HL)          
596A: 66             LD      H,(HL)          
596B: CA FB 17       JP      Z,$17FB         
596E: 53             LD      D,E             
596F: BE             CP      (HL)            
5970: 63             LD      H,E             
5971: 7A             LD      A,D             
5972: B5             OR      L               
5973: 6C             LD      L,H             
5974: B8             CP      B               
5975: 16 57          LD      D,$57           
5977: 17             RLA                     
5978: 1F             RRA                     
5979: B3             OR      E               
597A: CD 9A 66       CALL    $669A           
597D: 17             RLA                     
597E: 8E             ADC     A,(HL)          
597F: 48             LD      C,B             
5980: 5B             LD      E,E             
5981: 17             RLA                     
5982: F0             RET     P               
5983: 8B             ADC     A,E             
5984: 13             INC     DE              
5985: BF             CP      A               
5986: AF             XOR     A               
5987: 14             INC     D               
5988: 04             INC     B               
5989: 68             LD      L,B             
598A: 5B             LD      E,E             
598B: 5E             LD      E,(HL)          
598C: 3F             CCF                     
598D: A1             AND     C               
598E: 07             RLCA                    
598F: 55             LD      D,L             
5990: 0B             DEC     BC              
5991: 53             LD      D,E             
5992: 0A             LD      A,(BC)          
5993: 11 20 04       LD      DE,$0420        
5996: 1E 5F          LD      E,$5F           
5998: BE             CP      (HL)            
5999: 73             LD      (HL),E          
599A: 15             DEC     D               
599B: F5             PUSH    AF              
599C: BD             CP      L               
599D: 94             SUB     H               
599E: 14             INC     D               
599F: 4E             LD      C,(HL)          
59A0: 5E             LD      E,(HL)          
59A1: 5D             LD      E,L             
59A2: 9E             SBC     (HL)            
59A3: 16 60          LD      D,$60           
59A5: 51             LD      D,C             
59A6: 18 45          JR      $59ED           
59A8: C2 83 48       JP      NZ,$4883        
59AB: 06 9A          LD      B,$9A           
59AD: C2 16 83       JP      NZ,$8316        
59B0: 61             LD      H,C             
59B1: 5F             LD      E,A             
59B2: BE             CP      (HL)            
59B3: DB 95          IN      A,($95)         
59B5: 36 10          LD      (HL),$10        
59B7: 04             INC     B               
59B8: 0E 5F          LD      C,$5F           
59BA: BE             CP      (HL)            
59BB: 73             LD      (HL),E          
59BC: 15             DEC     D               
59BD: F5             PUSH    AF              
59BE: BD             CP      L               
59BF: 94             SUB     H               
59C0: 14             INC     D               
59C1: 45             LD      B,L             
59C2: 5E             LD      E,(HL)          
59C3: 85             ADD     A,L             
59C4: 8D             ADC     A,L             
59C5: 17             RLA                     
59C6: 60             LD      H,B             
59C7: 17             RLA                     
59C8: 19             ADD     HL,DE           
59C9: 04             INC     B               
59CA: 17             RLA                     
59CB: 5F             LD      E,A             
59CC: BE             CP      (HL)            
59CD: 73             LD      (HL),E          
59CE: 15             DEC     D               
59CF: F5             PUSH    AF              
59D0: BD             CP      L               
59D1: 94             SUB     H               
59D2: 14             INC     D               
59D3: 56             LD      D,(HL)          
59D4: 5E             LD      E,(HL)          
59D5: 2B             DEC     HL              
59D6: A0             AND     B               
59D7: F1             POP     AF              
59D8: B8             CP      B               
59D9: 02             LD      (BC),A          
59DA: A1             AND     C               
59DB: 89             ADC     A,C             
59DC: 17             RLA                     
59DD: DE 14          SBC     $14             
59DF: 64             LD      H,H             
59E0: 7A             LD      A,D             
59E1: 2E 34          LD      L,$34           
59E3: 01 89 02       LD      BC,$0289        
59E6: 08             EX      AF,AF'          
59E7: 79             LD      A,C             
59E8: 4F             LD      C,A             
59E9: AF             XOR     A               
59EA: 9B             SBC     E               
59EB: 73             LD      (HL),E          
59EC: 15             DEC     D               
59ED: F5             PUSH    AF              
59EE: BD             CP      L               
59EF: 16 59          LD      D,$59           
59F1: 91             SUB     C               
59F2: 00             NOP                     
59F3: A0             AND     B               
59F4: 02             LD      (BC),A          
59F5: 04             INC     B               
59F6: F8             RET     M               
59F7: 8B             ADC     A,E             
59F8: 23             INC     HL              
59F9: 62             LD      H,D             
59FA: 03             INC     BC              
59FB: 16 44          LD      D,$44           
59FD: 45             LD      B,L             
59FE: EF             RST     0X28            
59FF: 60             LD      H,B             
5A00: AE             XOR     (HL)            
5A01: D0             RET     NC              
5A02: F3             DI                      
5A03: 5F             LD      E,A             
5A04: F8             RET     M               
5A05: 8B             ADC     A,E             
5A06: 23             INC     HL              
5A07: 62             LD      H,D             
5A08: 4B             LD      C,E             
5A09: 7B             LD      A,E             
5A0A: 03             INC     BC              
5A0B: A0             AND     B               
5A0C: 0F             RRCA                    
5A0D: A0             AND     B               
5A0E: F3             DI                      
5A0F: 17             RLA                     
5A10: 17             RLA                     
5A11: 8D             ADC     A,L             
5A12: 07             RLCA                    
5A13: 36 0D          LD      (HL),$0D        
5A15: 34             INC     (HL)            
5A16: 0A             LD      A,(BC)          
5A17: 12             LD      (DE),A          
5A18: 04             INC     B               
5A19: 2F             CPL                     
5A1A: 56             LD      D,(HL)          
5A1B: 45             LD      B,L             
5A1C: D2 B0 09       JP      NC,$09B0        
5A1F: 15             DEC     D               
5A20: A3             AND     E               
5A21: A0             AND     B               
5A22: 5F             LD      E,A             
5A23: A0             AND     B               
5A24: 8B             ADC     A,E             
5A25: 9A             SBC     D               
5A26: B9             CP      C               
5A27: 46             LD      B,(HL)          
5A28: 5B             LD      E,E             
5A29: CA C7 DE       JP      Z,$DEC7         
5A2C: 3B             DEC     SP              
5A2D: F4 3E 6E       CALL    P,$6E3E         
5A30: 06 58          LD      B,$58           
5A32: 66             LD      H,(HL)          
5A33: C6 53          ADD     $53             
5A35: 15             DEC     D               
5A36: 0D             DEC     C               
5A37: 8D             ADC     A,L             
5A38: 82             ADD     A,D             
5A39: 17             RLA                     
5A3A: 54             LD      D,H             
5A3B: 5E             LD      E,(HL)          
5A3C: 3F             CCF                     
5A3D: A0             AND     B               
5A3E: 90             SUB     B               
5A3F: 14             INC     D               
5A40: 06 58          LD      B,$58           
5A42: 09             ADD     HL,BC           
5A43: B3             OR      E               
5A44: 8B             ADC     A,E             
5A45: 9A             SBC     D               
5A46: C7             RST     0X00            
5A47: DE 2E          SBC     $2E             
5A49: 81             ADD     A,C             
5A4A: 16 42          LD      D,$42           
5A4C: 00             NOP                     
5A4D: 05             DEC     B               
5A4E: A0             AND     B               
5A4F: 03             INC     BC              
5A50: 12             LD      (DE),A          
5A51: 44             LD      B,H             
5A52: 45             LD      B,L             
5A53: EF             RST     0X28            
5A54: 60             LD      H,B             
5A55: AE             XOR     (HL)            
5A56: D0             RET     NC              
5A57: F3             DI                      
5A58: 5F             LD      E,A             
5A59: F8             RET     M               
5A5A: 8B             ADC     A,E             
5A5B: 23             INC     HL              
5A5C: 62             LD      H,D             
5A5D: 4B             LD      C,E             
5A5E: 7B             LD      A,E             
5A5F: F4 72 DB       CALL    P,$DB72         
5A62: 63             LD      H,E             
5A63: 02             LD      (BC),A          
5A64: 0A             LD      A,(BC)          
5A65: 6C             LD      L,H             
5A66: 4D             LD      C,L             
5A67: F7             RST     0X30            
5A68: 62             LD      H,D             
5A69: E6 8B          AND     $8B             
5A6B: 3F             CCF                     
5A6C: 16 74          LD      D,$74           
5A6E: CA 07 1D       JP      Z,$1D07         
5A71: 0D             DEC     C               
5A72: 1B             DEC     DE              
5A73: 0A             LD      A,(BC)          
5A74: 12             LD      (DE),A          
5A75: 04             INC     B               
5A76: 17             RLA                     
5A77: 5F             LD      E,A             
5A78: BE             CP      (HL)            
5A79: 3F             CCF                     
5A7A: 16 74          LD      D,$74           
5A7C: CA D3 14       JP      Z,$14D3         
5A7F: 90             SUB     B               
5A80: 96             SUB     (HL)            
5A81: CE 9C          ADC     $9C             
5A83: 11 A0 23       LD      DE,$23A0        
5A86: 62             LD      H,D             
5A87: 5B             LD      E,E             
5A88: 4D             LD      C,L             
5A89: 6E             LD      L,(HL)          
5A8A: A7             AND     A               
5A8B: E6 8B          AND     $8B             
5A8D: 2E 18          LD      L,$18           
5A8F: 80             ADD     A,B             
5A90: C5             PUSH    BC              
5A91: 91             SUB     C               
5A92: 00             NOP                     
5A93: 84             ADD     A,H             
5A94: 07             RLCA                    
5A95: 80             ADD     A,B             
5A96: 98             SBC     B               
5A97: 0D             DEC     C               
5A98: 80             ADD     A,B             
5A99: 95             SUB     L               
5A9A: 0A             LD      A,(BC)          
5A9B: 08             EX      AF,AF'          
5A9C: 04             INC     B               
5A9D: 80             ADD     A,B             
5A9E: 90             SUB     B               
5A9F: 9E             SBC     (HL)            
5AA0: C5             PUSH    BC              
5AA1: BE             CP      (HL)            
5AA2: 9F             SBC     A               
5AA3: 33             INC     SP              
5AA4: 17             RLA                     
5AA5: 1F             RRA                     
5AA6: 54             LD      D,H             
5AA7: CE B5          ADC     $B5             
5AA9: 1B             DEC     DE              
5AAA: 79             LD      A,C             
5AAB: 56             LD      D,(HL)          
5AAC: D1             POP     DE              
5AAD: 90             SUB     B               
5AAE: 73             LD      (HL),E          
5AAF: 2F             CPL                     
5AB0: 17             RLA                     
5AB1: DA 46 0A       JP      C,$0A46         
5AB4: EE 2F          XOR     $2F             
5AB6: 62             LD      H,D             
5AB7: D6 E7          SUB     $E7             
5AB9: C3 9C 7B       JP      $7B9C           
5ABC: 9B             SBC     E               
5ABD: 19             ADD     HL,DE           
5ABE: 87             ADD     A,A             
5ABF: 50             LD      D,B             
5AC0: D1             POP     DE              
5AC1: 33             INC     SP              
5AC2: 70             LD      (HL),B          
5AC3: 98             SBC     B               
5AC4: 8C             ADC     A,H             
5AC5: 91             SUB     C               
5AC6: 7A             LD      A,D             
5AC7: E4 14 96       CALL    PO,$9614        
5ACA: 5F             LD      E,A             
5ACB: 2F             CPL                     
5ACC: C6 44          ADD     $44             
5ACE: F4 59 5E       CALL    P,$5E59         
5AD1: 43             LD      B,E             
5AD2: 49             LD      C,C             
5AD3: 82             ADD     A,D             
5AD4: 17             RLA                     
5AD5: 29             ADD     HL,HL           
5AD6: A1             AND     C               
5AD7: 73             LD      (HL),E          
5AD8: 76             HALT                    
5AD9: EB             EX      DE,HL           
5ADA: 99             SBC     C               
5ADB: 96             SUB     (HL)            
5ADC: 91             SUB     C               
5ADD: F4 BD FA       CALL    P,$FABD         
5AE0: 17             RLA                     
5AE1: 73             LD      (HL),E          
5AE2: 49             LD      C,C             
5AE3: 73             LD      (HL),E          
5AE4: BE             CP      (HL)            
5AE5: E4 14 26       CALL    PO,$2614        
5AE8: 60             LD      H,B             
5AE9: 16 EE          LD      D,$EE           
5AEB: 56             LD      D,(HL)          
5AEC: 72             LD      (HL),D          
5AED: 82             ADD     A,D             
5AEE: 17             RLA                     
5AEF: 1B             DEC     DE              
5AF0: A1             AND     C               
5AF1: 54             LD      D,H             
5AF2: 72             LD      (HL),D          
5AF3: 75             LD      (HL),L          
5AF4: 98             SBC     B               
5AF5: C3 B5 33       JP      $33B5           
5AF8: 98             SBC     B               
5AF9: 8F             ADC     A,A             
5AFA: 8C             ADC     A,H             
5AFB: 73             LD      (HL),E          
5AFC: 7B             LD      A,E             
5AFD: 73             LD      (HL),E          
5AFE: BE             CP      (HL)            
5AFF: E9             JP      (HL)            
5B00: 16 B4          LD      D,$B4           
5B02: D0             RET     NC              
5B03: EE 68          XOR     $68             
5B05: 84             ADD     A,H             
5B06: 15             DEC     D               
5B07: 26 60          LD      H,$60           
5B09: 3B             DEC     SP              
5B0A: F4 6E A7       CALL    P,$A76E         
5B0D: 16 8A          LD      D,$8A           
5B0F: DB 72          IN      A,($72)         
5B11: F8             RET     M               
5B12: 8B             ADC     A,E             
5B13: 23             INC     HL              
5B14: 62             LD      H,D             
5B15: 6B             LD      L,E             
5B16: BF             CP      A               
5B17: 0B             DEC     BC              
5B18: 6C             LD      L,H             
5B19: 96             SUB     (HL)            
5B1A: 96             SUB     (HL)            
5B1B: FB             EI                      
5B1C: 75             LD      (HL),L          
5B1D: A3             AND     E               
5B1E: D0             RET     NC              
5B1F: 42             LD      B,D             
5B20: 8E             ADC     A,(HL)          
5B21: 04             INC     B               
5B22: EE 52          XOR     $52             
5B24: 5E             LD      E,(HL)          
5B25: 72             LD      (HL),D          
5B26: B1             OR      C               
5B27: 2F             CPL                     
5B28: 49             LD      C,C             
5B29: 16 58          LD      D,$58           
5B2B: DF             RST     0X18            
5B2C: 9C             SBC     H               
5B2D: DB F9          IN      A,($F9)         
5B2F: 03             INC     BC              
5B30: 1F             RRA                     
5B31: 5F             LD      E,A             
5B32: BE             CP      (HL)            
5B33: 5B             LD      E,E             
5B34: B1             OR      C               
5B35: 4B             LD      C,E             
5B36: 7B             LD      A,E             
5B37: 52             LD      D,D             
5B38: 45             LD      B,L             
5B39: 53             LD      D,E             
5B3A: 8B             ADC     A,E             
5B3B: 1B             DEC     DE              
5B3C: C4 03 A0       CALL    NZ,$A003        
5B3F: 5F             LD      E,A             
5B40: BE             CP      (HL)            
5B41: F3             DI                      
5B42: 17             RLA                     
5B43: F3             DI                      
5B44: 8C             ADC     A,H             
5B45: B9             CP      C               
5B46: 46             LD      B,(HL)          
5B47: 5B             LD      E,E             
5B48: CA 5F BE       JP      Z,$BE5F         
5B4B: 3F             CCF                     
5B4C: 16 74          LD      D,$74           
5B4E: CA 2E 02       JP      Z,$022E         
5B51: 04             INC     B               
5B52: FB             EI                      
5B53: A5             AND     L               
5B54: A7             AND     A               
5B55: AD             XOR     L               
5B56: 19             ADD     HL,DE           
5B57: 6F             LD      L,A             
5B58: 92             SUB     D               
5B59: 00             NOP                     
5B5A: A8             XOR     B               
5B5B: 03             INC     BC              
5B5C: 10 45          DJNZ    $5BA3           
5B5E: 45             LD      B,L             
5B5F: 8E             ADC     A,(HL)          
5B60: 48             LD      C,B             
5B61: DB 8B          IN      A,($8B)         
5B63: 4B             LD      C,E             
5B64: 7B             LD      A,E             
5B65: 83             ADD     A,E             
5B66: 7A             LD      A,D             
5B67: 5F             LD      E,A             
5B68: BE             CP      (HL)            
5B69: 39             ADD     HL,SP           
5B6A: 17             RLA                     
5B6B: FF             RST     0X38            
5B6C: 9F             SBC     A               
5B6D: 02             LD      (BC),A          
5B6E: 04             INC     B               
5B6F: 10 53          DJNZ    $5BC4           
5B71: FF             RST     0X38            
5B72: 5A             LD      E,D             
5B73: 07             RLCA                    
5B74: 52             LD      D,D             
5B75: 0B             DEC     BC              
5B76: 50             LD      D,B             
5B77: 0A             LD      A,(BC)          
5B78: 14             INC     D               
5B79: 34             INC     (HL)            
5B7A: 0E 32          LD      C,$32           
5B7C: 0D             DEC     C               
5B7D: 2F             CPL                     
5B7E: 09             ADD     HL,BC           
5B7F: 14             INC     D               
5B80: 1E 11          LD      E,$11           
5B82: 12             LD      (DE),A          
5B83: 04             INC     B               
5B84: 28 5F          JR      Z,$5BE5         
5B86: BE             CP      (HL)            
5B87: D3 14          OUT     ($14),A         
5B89: 46             LD      B,(HL)          
5B8A: 98             SBC     B               
5B8B: 4B             LD      C,E             
5B8C: 5E             LD      E,(HL)          
5B8D: D0             RET     NC              
5B8E: B5             OR      L               
5B8F: 6B             LD      L,E             
5B90: A1             AND     C               
5B91: F4 4F 10       CALL    P,$104F         
5B94: 99             SBC     C               
5B95: 33             INC     SP              
5B96: 70             LD      (HL),B          
5B97: 55             LD      D,L             
5B98: 45             LD      B,L             
5B99: A7             AND     A               
5B9A: D0             RET     NC              
5B9B: 15             DEC     D               
5B9C: BC             CP      H               
5B9D: B0             OR      B               
5B9E: 53             LD      D,E             
5B9F: 12             LD      (DE),A          
5BA0: BC             CP      H               
5BA1: 37             SCF                     
5BA2: 62             LD      H,D             
5BA3: 96             SUB     (HL)            
5BA4: 5F             LD      E,A             
5BA5: 4B             LD      C,E             
5BA6: 62             LD      H,D             
5BA7: 5F             LD      E,A             
5BA8: BE             CP      (HL)            
5BA9: 39             ADD     HL,SP           
5BAA: 17             RLA                     
5BAB: FF             RST     0X38            
5BAC: 9F             SBC     A               
5BAD: 88             ADC     A,B             
5BAE: 15             DEC     D               
5BAF: 17             RLA                     
5BB0: 0D             DEC     C               
5BB1: 15             DEC     D               
5BB2: 04             INC     B               
5BB3: 12             LD      (DE),A          
5BB4: 55             LD      D,L             
5BB5: BD             CP      L               
5BB6: F5             PUSH    AF              
5BB7: BD             CP      L               
5BB8: F3             DI                      
5BB9: 17             RLA                     
5BBA: 1E DA          LD      E,$DA           
5BBC: D6 15          SUB     $15             
5BBE: D2 B5 55       JP      NC,$55B5        
5BC1: 9F             SBC     A               
5BC2: 19             ADD     HL,DE           
5BC3: A0             AND     B               
5BC4: 49             LD      C,C             
5BC5: C6 81          ADD     $81             
5BC7: 19             ADD     HL,DE           
5BC8: 80             ADD     A,B             
5BC9: C6 00          ADD     $00             
5BCB: 00             NOP                     
5BCC: A8             XOR     B               
5BCD: 03             INC     BC              
5BCE: 12             LD      (DE),A          
5BCF: 45             LD      B,L             
5BD0: 45             LD      B,L             
5BD1: 8E             ADC     A,(HL)          
5BD2: 48             LD      C,B             
5BD3: DB 8B          IN      A,($8B)         
5BD5: 4B             LD      C,E             
5BD6: 7B             LD      A,E             
5BD7: F4 4F 10       CALL    P,$104F         
5BDA: 99             SBC     C               
5BDB: C6 6A          ADD     $6A             
5BDD: 6E             LD      L,(HL)          
5BDE: 7A             LD      A,D             
5BDF: DB E0          IN      A,($E0)         
5BE1: 02             LD      (BC),A          
5BE2: 0A             LD      A,(BC)          
5BE3: F4 4F 10       CALL    P,$104F         
5BE6: 99             SBC     C               
5BE7: C5             PUSH    BC              
5BE8: 6A             LD      L,D             
5BE9: 8E             ADC     A,(HL)          
5BEA: 48             LD      C,B             
5BEB: DB 8B          IN      A,($8B)         
5BED: 07             RLCA                    
5BEE: 59             LD      E,C             
5BEF: 0E 57          LD      C,$57           
5BF1: 0D             DEC     C               
5BF2: 1C             INC     E               
5BF3: 0E 04          LD      C,$04           
5BF5: 0A             LD      A,(BC)          
5BF6: 13             INC     DE              
5BF7: 0A             LD      A,(BC)          
5BF8: 14             INC     D               
5BF9: 04             INC     B               
5BFA: 14             INC     D               
5BFB: 5F             LD      E,A             
5BFC: BE             CP      (HL)            
5BFD: D3 14          OUT     ($14),A         
5BFF: 46             LD      B,(HL)          
5C00: 98             SBC     B               
5C01: 4B             LD      C,E             
5C02: 5E             LD      E,(HL)          
5C03: C3 B5 EF       JP      $EFB5           
5C06: 8D             ADC     A,L             
5C07: 13             INC     DE              
5C08: 47             LD      B,A             
5C09: BF             CP      A               
5C0A: 14             INC     D               
5C0B: D3 B2          OUT     ($B2),A         
5C0D: CF             RST     0X08            
5C0E: 98             SBC     B               
5C0F: 0D             DEC     C               
5C10: 19             ADD     HL,DE           
5C11: 0A             LD      A,(BC)          
5C12: 16 1E          LD      D,$1E           
5C14: 11 12 04       LD      DE,$0412        
5C17: 12             LD      (DE),A          
5C18: 5F             LD      E,A             
5C19: BE             CP      (HL)            
5C1A: D3 14          OUT     ($14),A         
5C1C: 46             LD      B,(HL)          
5C1D: 98             SBC     B               
5C1E: 4B             LD      C,E             
5C1F: 5E             LD      E,(HL)          
5C20: C7             RST     0X00            
5C21: B5             OR      L               
5C22: 43             LD      B,E             
5C23: D9             EXX                     
5C24: C7             RST     0X00            
5C25: 98             SBC     B               
5C26: 5A             LD      E,D             
5C27: 7B             LD      A,E             
5C28: 17             RLA                     
5C29: 60             LD      H,B             
5C2A: 0D             DEC     C               
5C2B: 1C             INC     E               
5C2C: 0A             LD      A,(BC)          
5C2D: 15             DEC     D               
5C2E: 04             INC     B               
5C2F: 18 C7          JR      $5BF8           
5C31: DE 2F          SBC     $2F             
5C33: 17             RLA                     
5C34: 46             LD      B,(HL)          
5C35: 48             LD      C,B             
5C36: 55             LD      D,L             
5C37: DB 87          IN      A,($87)         
5C39: 74             LD      (HL),H          
5C3A: B3             OR      E               
5C3B: 8B             ADC     A,E             
5C3C: 76             HALT                    
5C3D: A7             AND     A               
5C3E: D6 15          SUB     $15             
5C40: C7             RST     0X00            
5C41: 16 08          LD      D,$08           
5C43: BC             CP      H               
5C44: 3D             DEC     A               
5C45: 7B             LD      A,E             
5C46: 9B             SBC     E               
5C47: C1             POP     BC              
5C48: 08             EX      AF,AF'          
5C49: 46             LD      B,(HL)          
5C4A: 0D             DEC     C               
5C4B: 44             LD      B,H             
5C4C: 1F             RRA                     
5C4D: 24             INC     H               
5C4E: 5F             LD      E,A             
5C4F: BE             CP      (HL)            
5C50: 43             LD      B,E             
5C51: 16 2E          LD      D,$2E           
5C53: 6D             LD      L,L             
5C54: 5C             LD      E,H             
5C55: 15             DEC     D               
5C56: DB 9F          IN      A,($9F)         
5C58: 5F             LD      E,A             
5C59: BE             CP      (HL)            
5C5A: D3 14          OUT     ($14),A         
5C5C: 46             LD      B,(HL)          
5C5D: 98             SBC     B               
5C5E: 55             LD      D,L             
5C5F: 5E             LD      E,(HL)          
5C60: 2F             CPL                     
5C61: 60             LD      H,B             
5C62: D6 B5          SUB     $B5             
5C64: C4 9C 49       CALL    NZ,$499C        
5C67: 5E             LD      E,(HL)          
5C68: 09             ADD     HL,BC           
5C69: B3             OR      E               
5C6A: 91             SUB     C               
5C6B: 7A             LD      A,D             
5C6C: 03             INC     BC              
5C6D: 15             DEC     D               
5C6E: 67             LD      H,A             
5C6F: 93             SUB     E               
5C70: 1B             DEC     DE              
5C71: B5             OR      L               
5C72: 0B             DEC     BC              
5C73: 1C             INC     E               
5C74: 01 1D 07       LD      BC,$071D        
5C77: 0D             DEC     C               
5C78: 05             DEC     B               
5C79: 1C             INC     E               
5C7A: 1D             DEC     E               
5C7B: 1D             DEC     E               
5C7C: 14             INC     D               
5C7D: 0C             INC     C               
5C7E: 1E 07          LD      E,$07           
5C80: 0D             DEC     C               
5C81: 05             DEC     B               
5C82: 1C             INC     E               
5C83: 1E 1D          LD      E,$1D           
5C85: 32 0C 15       LD      ($150C),A       
5C88: 07             RLCA                    
5C89: 0D             DEC     C               
5C8A: 05             DEC     B               
5C8B: 1C             INC     E               
5C8C: 15             DEC     D               
5C8D: 1D             DEC     E               
5C8E: 0F             RRCA                    
5C8F: 0C             INC     C               
5C90: 18 80          JR      $5C12           
5C92: 84             ADD     A,H             
5C93: 92             SUB     D               
5C94: 00             NOP                     
5C95: 84             ADD     A,H             
5C96: 07             RLCA                    
5C97: 5B             LD      E,E             
5C98: 0D             DEC     C               
5C99: 59             LD      E,C             
5C9A: 0A             LD      A,(BC)          
5C9B: 08             EX      AF,AF'          
5C9C: 04             INC     B               
5C9D: 55             LD      D,L             
5C9E: 9E             SBC     (HL)            
5C9F: 7A             LD      A,D             
5CA0: D6 9C          SUB     $9C             
5CA2: DB 72          IN      A,($72)         
5CA4: 70             LD      (HL),B          
5CA5: C0             RET     NZ              
5CA6: 6E             LD      L,(HL)          
5CA7: 98             SBC     B               
5CA8: 30 15          JR      NC,$5CBF        
5CAA: F4 BD D6       CALL    P,$D6BD         
5CAD: B5             OR      L               
5CAE: DB 72          IN      A,($72)         
5CB0: A7             AND     A               
5CB1: B7             OR      A               
5CB2: B4             OR      H               
5CB3: 85             ADD     A,L             
5CB4: 04             INC     B               
5CB5: EE D8          XOR     $D8             
5CB7: B0             OR      B               
5CB8: 53             LD      D,E             
5CB9: 61             LD      H,C             
5CBA: 90             SUB     B               
5CBB: 14             INC     D               
5CBC: 19             ADD     HL,DE           
5CBD: 58             LD      E,B             
5CBE: 57             LD      D,A             
5CBF: 7B             LD      A,E             
5CC0: FB             EI                      
5CC1: 8E             ADC     A,(HL)          
5CC2: DB 72          IN      A,($72)         
5CC4: 37             SCF                     
5CC5: 6E             LD      L,(HL)          
5CC6: 5B             LD      E,E             
5CC7: BB             CP      E               
5CC8: 04             INC     B               
5CC9: 68             LD      L,B             
5CCA: 9F             SBC     A               
5CCB: 15             DEC     D               
5CCC: FB             EI                      
5CCD: 17             RLA                     
5CCE: F3             DI                      
5CCF: 8C             ADC     A,H             
5CD0: 65             LD      H,L             
5CD1: B1             OR      C               
5CD2: 00             NOP                     
5CD3: 9F             SBC     A               
5CD4: 6F             LD      L,A             
5CD5: 7C             LD      A,H             
5CD6: 82             ADD     A,D             
5CD7: 17             RLA                     
5CD8: 54             LD      D,H             
5CD9: 5E             LD      E,(HL)          
5CDA: 92             SUB     D               
5CDB: 5F             LD      E,A             
5CDC: 46             LD      B,(HL)          
5CDD: 62             LD      H,D             
5CDE: 95             SUB     L               
5CDF: 14             INC     D               
5CE0: 82             ADD     A,D             
5CE1: 17             RLA                     
5CE2: 4E             LD      C,(HL)          
5CE3: 5E             LD      E,(HL)          
5CE4: 7A             LD      A,D             
5CE5: 79             LD      A,C             
5CE6: 04             INC     B               
5CE7: BC             CP      H               
5CE8: 59             LD      E,C             
5CE9: 60             LD      H,B             
5CEA: 5B             LD      E,E             
5CEB: B1             OR      C               
5CEC: 8F             ADC     A,A             
5CED: 73             LD      (HL),E          
5CEE: 7E             LD      A,(HL)          
5CEF: 15             DEC     D               
5CF0: 85             ADD     A,L             
5CF1: A1             AND     C               
5CF2: 2E 03          LD      L,$03           
5CF4: 1C             INC     E               
5CF5: 5F             LD      E,A             
5CF6: BE             CP      (HL)            
5CF7: 5B             LD      E,E             
5CF8: B1             OR      C               
5CF9: 2F             CPL                     
5CFA: 49             LD      C,C             
5CFB: E4 14 EE       CALL    PO,$EE14        
5CFE: DE CB          SBC     $CB             
5D00: 78             LD      A,B             
5D01: F0             RET     P               
5D02: B3             OR      E               
5D03: 4B             LD      C,E             
5D04: 62             LD      H,D             
5D05: B9             CP      C               
5D06: 46             LD      B,(HL)          
5D07: 5B             LD      E,E             
5D08: CA 5F BE       JP      Z,$BE5F         
5D0B: 8F             ADC     A,A             
5D0C: 17             RLA                     
5D0D: CF             RST     0X08            
5D0E: 99             SBC     C               
5D0F: 9B             SBC     E               
5D10: 8F             ADC     A,A             
5D11: 02             LD      (BC),A          
5D12: 04             INC     B               
5D13: F0             RET     P               
5D14: B3             OR      E               
5D15: 4B             LD      C,E             
5D16: 62             LD      H,D             
5D17: 1B             DEC     DE              
5D18: 80             ADD     A,B             
5D19: B5             OR      L               
5D1A: A0             AND     B               
5D1B: 00             NOP                     
5D1C: AC             XOR     H               
5D1D: 03             INC     BC              
5D1E: 14             INC     D               
5D1F: 5F             LD      E,A             
5D20: BE             CP      (HL)            
5D21: 5B             LD      E,E             
5D22: B1             OR      C               
5D23: 4B             LD      C,E             
5D24: 7B             LD      A,E             
5D25: 44             LD      B,H             
5D26: 45             LD      B,L             
5D27: 38 C6          JR      C,$5CEF         
5D29: 91             SUB     C               
5D2A: 7A             LD      A,D             
5D2B: 3B             DEC     SP              
5D2C: 16 D3          LD      D,$D3           
5D2E: 93             SUB     E               
5D2F: F4 72 DB       CALL    P,$DB72         
5D32: 63             LD      H,E             
5D33: 07             RLCA                    
5D34: 80             ADD     A,B             
5D35: 8F             ADC     A,A             
5D36: 0E 80          LD      C,$80           
5D38: 8C             ADC     A,H             
5D39: 0D             DEC     C               
5D3A: 1B             DEC     DE              
5D3B: 0E 04          LD      C,$04           
5D3D: 0A             LD      A,(BC)          
5D3E: 13             INC     DE              
5D3F: 0A             LD      A,(BC)          
5D40: 14             INC     D               
5D41: 04             INC     B               
5D42: 13             INC     DE              
5D43: 5F             LD      E,A             
5D44: BE             CP      (HL)            
5D45: 3B             DEC     SP              
5D46: 16 D3          LD      D,$D3           
5D48: 93             SUB     E               
5D49: 4B             LD      C,E             
5D4A: 7B             LD      A,E             
5D4B: 4C             LD      C,H             
5D4C: 48             LD      C,B             
5D4D: 86             ADD     A,(HL)          
5D4E: 5F             LD      E,A             
5D4F: 44             LD      B,H             
5D50: DB 38          IN      A,($38)         
5D52: C6 91          ADD     $91             
5D54: 7A             LD      A,D             
5D55: 2E 0B          LD      L,$0B           
5D57: 6D             LD      L,L             
5D58: 0A             LD      A,(BC)          
5D59: 16 12          LD      D,$12           
5D5B: 0D             DEC     C               
5D5C: 10 1E          DJNZ    $5D7C           
5D5E: 28 14          JR      Z,$5D74         
5D60: 04             INC     B               
5D61: 0B             DEC     BC              
5D62: 5F             LD      E,A             
5D63: BE             CP      (HL)            
5D64: 3B             DEC     SP              
5D65: 16 D3          LD      D,$D3           
5D67: 93             SUB     E               
5D68: 4B             LD      C,E             
5D69: 7B             LD      A,E             
5D6A: 36 A1          LD      (HL),$A1        
5D6C: 2E 18          LD      L,$18           
5D6E: 2D             DEC     L               
5D6F: 0D             DEC     C               
5D70: 2B             DEC     HL              
5D71: 04             INC     B               
5D72: 26 5F          LD      H,$5F           
5D74: BE             CP      (HL)            
5D75: 3B             DEC     SP              
5D76: 16 D3          LD      D,$D3           
5D78: 93             SUB     E               
5D79: 37             SCF                     
5D7A: 6E             LD      L,(HL)          
5D7B: D1             POP     DE              
5D7C: B5             OR      L               
5D7D: 97             SUB     A               
5D7E: C6 51          ADD     $51             
5D80: 18 4F          JR      $5DD1           
5D82: C2 66 C6       JP      NZ,$C666        
5D85: 9B             SBC     E               
5D86: 15             DEC     D               
5D87: 5B             LD      E,E             
5D88: CA E4 B3       JP      Z,$B3E4         
5D8B: 66             LD      H,(HL)          
5D8C: 4D             LD      C,L             
5D8D: D6 15          SUB     $15             
5D8F: 82             ADD     A,D             
5D90: 17             RLA                     
5D91: 59             LD      E,C             
5D92: 5E             LD      E,(HL)          
5D93: 00             NOP                     
5D94: B3             OR      E               
5D95: D9             EXX                     
5D96: 6A             LD      L,D             
5D97: 39             ADD     HL,SP           
5D98: 4A             LD      C,D             
5D99: 1E 28          LD      E,$28           
5D9B: 14             INC     D               
5D9C: 08             EX      AF,AF'          
5D9D: 27             DAA                     
5D9E: 04             INC     B               
5D9F: 25             DEC     H               
5DA0: 5F             LD      E,A             
5DA1: BE             CP      (HL)            
5DA2: 3B             DEC     SP              
5DA3: 16 D3          LD      D,$D3           
5DA5: 93             SUB     E               
5DA6: 4B             LD      C,E             
5DA7: 7B             LD      A,E             
5DA8: 48             LD      C,B             
5DA9: 55             LD      D,L             
5DAA: 2F             CPL                     
5DAB: 62             LD      H,D             
5DAC: 19             ADD     HL,DE           
5DAD: 58             LD      E,B             
5DAE: 82             ADD     A,D             
5DAF: 7B             LD      A,E             
5DB0: 7B             LD      A,E             
5DB1: 17             RLA                     
5DB2: D3 B2          OUT     ($B2),A         
5DB4: 13             INC     DE              
5DB5: B8             CP      B               
5DB6: 8E             ADC     A,(HL)          
5DB7: 48             LD      C,B             
5DB8: 51             LD      D,C             
5DB9: 18 45          JR      $5E00           
5DBB: C2 85 48       JP      NZ,$4885        
5DBE: 14             INC     D               
5DBF: BC             CP      H               
5DC0: 86             ADD     A,(HL)          
5DC1: 5F             LD      E,A             
5DC2: D6 15          SUB     $15             
5DC4: 2E 02          LD      L,$02           
5DC6: 08             EX      AF,AF'          
5DC7: F4 4F 10       CALL    P,$104F         
5DCA: 99             SBC     C               
5DCB: CE 6A          ADC     $6A             
5DCD: 72             LD      (HL),D          
5DCE: 48             LD      C,B             
5DCF: 24             INC     H               
5DD0: 81             ADD     A,C             
5DD1: C0             RET     NZ              
5DD2: 00             NOP                     
5DD3: 00             NOP                     
5DD4: 90             SUB     B               
5DD5: 03             INC     BC              
5DD6: 1C             INC     E               
5DD7: 4E             LD      C,(HL)          
5DD8: 45             LD      B,L             
5DD9: 31 49 55       LD      SP,$5549        
5DDC: 5E             LD      E,(HL)          
5DDD: 3A 62 9E       LD      A,($9E62)       
5DE0: 61             LD      H,C             
5DE1: 43             LD      B,E             
5DE2: 16 4B          LD      D,$4B           
5DE4: 62             LD      H,D             
5DE5: 3B             DEC     SP              
5DE6: 55             LD      D,L             
5DE7: E6 8B          AND     $8B             
5DE9: C0             RET     NZ              
5DEA: 16 82          LD      D,$82           
5DEC: 17             RLA                     
5DED: 48             LD      C,B             
5DEE: 5E             LD      E,(HL)          
5DEF: 81             ADD     A,C             
5DF0: 8D             ADC     A,L             
5DF1: 1B             DEC     DE              
5DF2: B5             OR      L               
5DF3: 09             ADD     HL,BC           
5DF4: 02             LD      (BC),A          
5DF5: 3C             INC     A               
5DF6: 3C             INC     A               
5DF7: 07             RLCA                    
5DF8: 80             ADD     A,B             
5DF9: B3             OR      E               
5DFA: 0B             DEC     BC              
5DFB: 80             ADD     A,B             
5DFC: B0             OR      B               
5DFD: 0A             LD      A,(BC)          
5DFE: 09             ADD     HL,BC           
5DFF: 80             ADD     A,B             
5E00: 9A             SBC     D               
5E01: 0D             DEC     C               
5E02: 80             ADD     A,B             
5E03: 97             SUB     A               
5E04: 1A             LD      A,(DE)          
5E05: 09             ADD     HL,BC           
5E06: 09             ADD     HL,BC           
5E07: 0B             DEC     BC              
5E08: 80             ADD     A,B             
5E09: 91             SUB     C               
5E0A: 05             DEC     B               
5E0B: 99             SBC     C               
5E0C: 2B             DEC     HL              
5E0D: 0D             DEC     C               
5E0E: 29             ADD     HL,HL           
5E0F: 04             INC     B               
5E10: 03             INC     BC              
5E11: C7             RST     0X00            
5E12: DE 52          SBC     $52             
5E14: 12             LD      (DE),A          
5E15: 04             INC     B               
5E16: 1F             RRA                     
5E17: 50             LD      D,B             
5E18: B8             CP      B               
5E19: CB 87          RES     0,A             
5E1B: 6B             LD      L,E             
5E1C: BF             CP      A               
5E1D: 5F             LD      E,A             
5E1E: BE             CP      (HL)            
5E1F: A3             AND     E               
5E20: 15             DEC     D               
5E21: 33             INC     SP              
5E22: 8E             ADC     A,(HL)          
5E23: 83             ADD     A,E             
5E24: 7A             LD      A,D             
5E25: 5F             LD      E,A             
5E26: BE             CP      (HL)            
5E27: 57             LD      D,A             
5E28: 17             RLA                     
5E29: 1F             RRA                     
5E2A: B3             OR      E               
5E2B: B5             OR      L               
5E2C: 9A             SBC     D               
5E2D: D5             PUSH    DE              
5E2E: B5             OR      L               
5E2F: 0E 53          LD      C,$53           
5E31: 44             LD      B,H             
5E32: DB 93          IN      A,($93)         
5E34: 9E             SBC     (HL)            
5E35: 21 1D 11       LD      HL,$111D        
5E38: CC 2E 0D       CALL    Z,$0D2E         
5E3B: 2C             INC     L               
5E3C: 04             INC     B               
5E3D: 03             INC     BC              
5E3E: C7             RST     0X00            
5E3F: DE 52          SBC     $52             
5E41: 12             LD      (DE),A          
5E42: 04             INC     B               
5E43: 24             INC     H               
5E44: 6C             LD      L,H             
5E45: BE             CP      (HL)            
5E46: 85             ADD     A,L             
5E47: A1             AND     C               
5E48: 7B             LD      A,E             
5E49: 14             INC     D               
5E4A: 29             ADD     HL,HL           
5E4B: B8             CP      B               
5E4C: B4             OR      H               
5E4D: D0             RET     NC              
5E4E: B8             CP      B               
5E4F: 16 62          LD      D,$62           
5E51: 17             RLA                     
5E52: 35             DEC     (HL)            
5E53: 49             LD      C,C             
5E54: C3 B5 CB       JP      $CBB5           
5E57: B5             OR      L               
5E58: 09             ADD     HL,BC           
5E59: BC             CP      H               
5E5A: 50             LD      D,B             
5E5B: 8B             ADC     A,E             
5E5C: B5             OR      L               
5E5D: 53             LD      D,E             
5E5E: B8             CP      B               
5E5F: 16 96          LD      D,$96           
5E61: 64             LD      H,H             
5E62: DB 72          IN      A,($72)         
5E64: 0E D0          LD      C,$D0           
5E66: AB             XOR     E               
5E67: 89             ADC     A,C             
5E68: FF             RST     0X38            
5E69: 31 0D 2F       LD      SP,$2F0D        
5E6C: 04             INC     B               
5E6D: 2B             DEC     HL              
5E6E: 5F             LD      E,A             
5E6F: BE             CP      (HL)            
5E70: 57             LD      D,A             
5E71: 17             RLA                     
5E72: 1F             RRA                     
5E73: B3             OR      E               
5E74: B5             OR      L               
5E75: 9A             SBC     D               
5E76: CA B5 86       JP      Z,$86B5         
5E79: 5F             LD      E,A             
5E7A: D5             PUSH    DE              
5E7B: 15             DEC     D               
5E7C: 57             LD      D,A             
5E7D: 17             RLA                     
5E7E: 74             LD      (HL),H          
5E7F: CA F3 5F       JP      Z,$5FF3         
5E82: 79             LD      A,C             
5E83: 68             LD      L,B             
5E84: 4A             LD      C,D             
5E85: 90             SUB     B               
5E86: 4B             LD      C,E             
5E87: 7B             LD      A,E             
5E88: F6 4E          OR      $4E             
5E8A: EB             EX      DE,HL           
5E8B: DA 4F 45       JP      C,$454F         
5E8E: 80             ADD     A,B             
5E8F: 47             LD      B,A             
5E90: 53             LD      D,E             
5E91: 79             LD      A,C             
5E92: B0             OR      B               
5E93: 53             LD      D,E             
5E94: 04             INC     B               
5E95: BC             CP      H               
5E96: 89             ADC     A,C             
5E97: 8D             ADC     A,L             
5E98: 21 1D FF       LD      HL,$FF1D        
5E9B: 15             DEC     D               
5E9C: 10 04          DJNZ    $5EA2           
5E9E: 0E 76          LD      C,$76           
5EA0: 4D             LD      C,L             
5EA1: F4 BD 1B       CALL    P,$1BBD         
5EA4: 16 F3          LD      D,$F3           
5EA6: 8C             ADC     A,H             
5EA7: 73             LD      (HL),E          
5EA8: 7B             LD      A,E             
5EA9: 14             INC     D               
5EAA: 67             LD      H,A             
5EAB: F1             POP     AF              
5EAC: B9             CP      C               
5EAD: 08             EX      AF,AF'          
5EAE: 80             ADD     A,B             
5EAF: C4 0D 80       CALL    NZ,$800D        
5EB2: C1             POP     BC              
5EB3: 0E 3E          LD      C,$3E           
5EB5: 0D             DEC     C               
5EB6: 32 14 01       LD      ($0114),A       
5EB9: 1D             DEC     E               
5EBA: 0B             DEC     BC              
5EBB: 19             ADD     HL,DE           
5EBC: 0A             LD      A,(BC)          
5EBD: 04             INC     B               
5EBE: 04             INC     B               
5EBF: 21 04 00       LD      HL,$0004        
5EC2: 00             NOP                     
5EC3: 03             INC     BC              
5EC4: 04             INC     B               
5EC5: 21 03 00       LD      HL,$0003        
5EC8: 00             NOP                     
5EC9: 01 04 21       LD      BC,$2104        
5ECC: 01 00 00       LD      BC,$0000        
5ECF: 02             LD      (BC),A          
5ED0: 04             INC     B               
5ED1: 21 02 00       LD      HL,$0002        
5ED4: 00             NOP                     
5ED5: 1F             RRA                     
5ED6: 12             LD      (DE),A          
5ED7: 5F             LD      E,A             
5ED8: BE             CP      (HL)            
5ED9: 57             LD      D,A             
5EDA: 17             RLA                     
5EDB: 1F             RRA                     
5EDC: B3             OR      E               
5EDD: B3             OR      E               
5EDE: 9A             SBC     D               
5EDF: 74             LD      (HL),H          
5EE0: A7             AND     A               
5EE1: 27             DAA                     
5EE2: BA             CP      D               
5EE3: DB B5          IN      A,($B5)         
5EE5: 1B             DEC     DE              
5EE6: A1             AND     C               
5EE7: 8E             ADC     A,(HL)          
5EE8: 48             LD      C,B             
5EE9: 1F             RRA                     
5EEA: 08             EX      AF,AF'          
5EEB: 5F             LD      E,A             
5EEC: BE             CP      (HL)            
5EED: 57             LD      D,A             
5EEE: 17             RLA                     
5EEF: 1F             RRA                     
5EF0: B3             OR      E               
5EF1: B3             OR      E               
5EF2: 9A             SBC     D               
5EF3: 0D             DEC     C               
5EF4: 7F             LD      A,A             
5EF5: 01 1D 1C       LD      BC,$1C1D        
5EF8: 1D             DEC     E               
5EF9: 0B             DEC     BC              
5EFA: 79             LD      A,C             
5EFB: 05             DEC     B               
5EFC: 33             INC     SP              
5EFD: 23             INC     HL              
5EFE: 0D             DEC     C               
5EFF: 21 1F 1D       LD      HL,$1D1F        
5F02: 0C             INC     C               
5F03: BA             CP      D               
5F04: 17             RLA                     
5F05: 7A             LD      A,D             
5F06: 33             INC     SP              
5F07: BB             CP      E               
5F08: 7B             LD      A,E             
5F09: A6             AND     (HL)            
5F0A: 40             LD      B,B             
5F0B: B9             CP      C               
5F0C: E1             POP     HL              
5F0D: 14             INC     D               
5F0E: 3D             DEC     A               
5F0F: C6 4B          ADD     $4B             
5F11: 62             LD      H,D             
5F12: 6C             LD      L,H             
5F13: BE             CP      (HL)            
5F14: 29             ADD     HL,HL           
5F15: A1             AND     C               
5F16: 1B             DEC     DE              
5F17: 71             LD      (HL),C          
5F18: 34             INC     (HL)            
5F19: A1             AND     C               
5F1A: CF             RST     0X08            
5F1B: 17             RLA                     
5F1C: 9D             SBC     L               
5F1D: 7A             LD      A,D             
5F1E: 21 1D 14       LD      HL,$141D        
5F21: 99             SBC     C               
5F22: 16 1F          LD      D,$1F           
5F24: 14             INC     D               
5F25: 0C             INC     C               
5F26: BA             CP      D               
5F27: 17             RLA                     
5F28: 7A             LD      A,D             
5F29: 33             INC     SP              
5F2A: BB             CP      E               
5F2B: C7             RST     0X00            
5F2C: DE 09          SBC     $09             
5F2E: 15             DEC     D               
5F2F: 37             SCF                     
5F30: 5A             LD      E,D             
5F31: A3             AND     E               
5F32: 15             DEC     D               
5F33: CE B5          ADC     $B5             
5F35: 91             SUB     C               
5F36: C5             PUSH    BC              
5F37: EB             EX      DE,HL           
5F38: 5D             LD      E,L             
5F39: CC 21 0D       CALL    Z,$0D21         
5F3C: 1F             RRA                     
5F3D: 1F             RRA                     
5F3E: 1B             DEC     DE              
5F3F: 3B             DEC     SP              
5F40: 55             LD      D,L             
5F41: 0B             DEC     BC              
5F42: 8E             ADC     A,(HL)          
5F43: D2 B0 06       JP      NC,$06B0        
5F46: 79             LD      A,C             
5F47: 43             LD      B,E             
5F48: DB 07          IN      A,($07)         
5F4A: B3             OR      E               
5F4B: 33             INC     SP              
5F4C: 98             SBC     B               
5F4D: C7             RST     0X00            
5F4E: DE 90          SBC     $90             
5F50: 14             INC     D               
5F51: 05             DEC     B               
5F52: 58             LD      E,B             
5F53: 1D             DEC     E               
5F54: A0             AND     B               
5F55: F3             DI                      
5F56: BF             CP      A               
5F57: 0D             DEC     C               
5F58: 56             LD      D,(HL)          
5F59: 21 1D 14       LD      HL,$141D        
5F5C: FF             RST     0X38            
5F5D: 16 1F          LD      D,$1F           
5F5F: 14             INC     D               
5F60: 16 6C          LD      D,$6C           
5F62: F4 72 CB       CALL    P,$CB72         
5F65: B5             OR      L               
5F66: 17             RLA                     
5F67: C0             RET     NZ              
5F68: 03             INC     BC              
5F69: 8C             ADC     A,H             
5F6A: 04             INC     B               
5F6B: 68             LD      L,B             
5F6C: 90             SUB     B               
5F6D: 14             INC     D               
5F6E: 96             SUB     (HL)            
5F6F: 14             INC     D               
5F70: 45             LD      B,L             
5F71: BD             CP      L               
5F72: 5B             LD      E,E             
5F73: 89             ADC     A,C             
5F74: 0A             LD      A,(BC)          
5F75: 15             DEC     D               
5F76: 0D             DEC     C               
5F77: 13             INC     DE              
5F78: 1F             RRA                     
5F79: 0E 5F          LD      C,$5F           
5F7B: BE             CP      (HL)            
5F7C: 57             LD      D,A             
5F7D: 17             RLA                     
5F7E: 1F             RRA                     
5F7F: B3             OR      E               
5F80: B3             OR      E               
5F81: 9A             SBC     D               
5F82: 4B             LD      C,E             
5F83: 7B             LD      A,E             
5F84: E3             EX      (SP),HL         
5F85: 59             LD      E,C             
5F86: 9B             SBC     E               
5F87: 5D             LD      E,L             
5F88: 1E 15          LD      E,$15           
5F8A: 16 02          LD      D,$02           
5F8C: 05             DEC     B               
5F8D: B4             OR      H               
5F8E: B7             OR      A               
5F8F: F0             RET     P               
5F90: A4             AND     H               
5F91: 54             LD      D,H             
5F92: 24             INC     H               
5F93: 40             LD      B,B             
5F94: 00             NOP                     
5F95: 00             NOP                     
5F96: 80             ADD     A,B             
5F97: 03             INC     BC              
5F98: 1A             LD      A,(DE)          
5F99: 4E             LD      C,(HL)          
5F9A: 45             LD      B,L             
5F9B: 31 49 46       LD      SP,$4649        
5F9E: 5E             LD      E,(HL)          
5F9F: 86             ADD     A,(HL)          
5FA0: 5F             LD      E,A             
5FA1: 57             LD      D,A             
5FA2: 17             RLA                     
5FA3: 1F             RRA                     
5FA4: B3             OR      E               
5FA5: B3             OR      E               
5FA6: 9A             SBC     D               
5FA7: 87             ADD     A,A             
5FA8: 8C             ADC     A,H             
5FA9: D1             POP     DE              
5FAA: B5             OR      L               
5FAB: 96             SUB     (HL)            
5FAC: 96             SUB     (HL)            
5FAD: DB 72          IN      A,($72)         
5FAF: 89             ADC     A,C             
5FB0: 67             LD      H,A             
5FB1: C7             RST     0X00            
5FB2: A0             AND     B               
5FB3: 07             RLCA                    
5FB4: 15             DEC     D               
5FB5: 0D             DEC     C               
5FB6: 13             INC     DE              
5FB7: 0A             LD      A,(BC)          
5FB8: 15             DEC     D               
5FB9: 04             INC     B               
5FBA: 0F             RRCA                    
5FBB: A8             XOR     B               
5FBC: 77             LD      (HL),A          
5FBD: 4E             LD      C,(HL)          
5FBE: 5E             LD      E,(HL)          
5FBF: E6 A0          AND     $A0             
5FC1: 7B             LD      A,E             
5FC2: 16 92          LD      D,$92           
5FC4: 14             INC     D               
5FC5: F6 A4          OR      $A4             
5FC7: 7F             LD      A,A             
5FC8: 7B             LD      A,E             
5FC9: 21 02 08       LD      HL,$0802        
5FCC: E3             EX      (SP),HL         
5FCD: 59             LD      E,C             
5FCE: 15             DEC     D               
5FCF: 58             LD      E,B             
5FD0: 3A 62 9E       LD      A,($9E62)       
5FD3: 61             LD      H,C             
5FD4: 1F             RRA                     
5FD5: 09             ADD     HL,BC           
5FD6: FF             RST     0X38            
5FD7: 00             NOP                     
5FD8: 80             ADD     A,B             
5FD9: 02             LD      (BC),A          
5FDA: 04             INC     B               
5FDB: 50             LD      D,B             
5FDC: 72             LD      (HL),D          
5FDD: 0B             DEC     BC              
5FDE: 5C             LD      E,H             
5FDF: 20 34          JR      NZ,$6015        
5FE1: 9C             SBC     H               
5FE2: 05             DEC     B               
5FE3: A4             AND     H               
5FE4: 03             INC     BC              
5FE5: 14             INC     D               
5FE6: 5F             LD      E,A             
5FE7: BE             CP      (HL)            
5FE8: 5B             LD      E,E             
5FE9: B1             OR      C               
5FEA: 4B             LD      C,E             
5FEB: 7B             LD      A,E             
5FEC: 45             LD      B,L             
5FED: 45             LD      B,L             
5FEE: 50             LD      D,B             
5FEF: 9F             SBC     A               
5FF0: C0             RET     NZ              
5FF1: 16 82          LD      D,$82           
5FF3: 17             RLA                     
5FF4: 49             LD      C,C             
5FF5: 5E             LD      E,(HL)          
5FF6: 07             RLCA                    
5FF7: B3             OR      E               
5FF8: 57             LD      D,A             
5FF9: 98             SBC     B               
5FFA: 07             RLCA                    
5FFB: 14             INC     D               
5FFC: 0D             DEC     C               
5FFD: 12             LD      (DE),A          
5FFE: 0A             LD      A,(BC)          
5FFF: 08             EX      AF,AF'          
6000: 04             INC     B               
6001: 0E 2C          LD      C,$2C           
6003: 1D             DEC     E               
6004: D5             PUSH    DE              
6005: 47             LD      B,A             
6006: F3             DI                      
6007: 5F             LD      E,A             
6008: 5B             LD      E,E             
6009: 4D             LD      C,L             
600A: C3 B0 1D       JP      $1DB0           
600D: 85             ADD     A,L             
600E: 5C             LD      E,H             
600F: C0             RET     NZ              
6010: 02             LD      (BC),A          
6011: 03             INC     BC              
6012: 3B             DEC     SP              
6013: 55             LD      D,L             
6014: 4E             LD      C,(HL)          
6015: 21 7F 88       LD      HL,$887F        
6018: 00             NOP                     
6019: 80             ADD     A,B             
601A: 03             INC     BC              
601B: 1D             DEC     E               
601C: 5F             LD      E,A             
601D: BE             CP      (HL)            
601E: 5B             LD      E,E             
601F: B1             OR      C               
6020: 4B             LD      C,E             
6021: 7B             LD      A,E             
6022: 56             LD      D,(HL)          
6023: 45             LD      B,L             
6024: A3             AND     E               
6025: 7A             LD      A,D             
6026: 5E             LD      E,(HL)          
6027: 17             RLA                     
6028: F3             DI                      
6029: A0             AND     B               
602A: 36 56          LD      (HL),$56        
602C: D0             RET     NC              
602D: 15             DEC     D               
602E: 82             ADD     A,D             
602F: 17             RLA                     
6030: 50             LD      D,B             
6031: 5E             LD      E,(HL)          
6032: BE             CP      (HL)            
6033: A0             AND     B               
6034: 19             ADD     HL,DE           
6035: 71             LD      (HL),C          
6036: 46             LD      B,(HL)          
6037: 48             LD      C,B             
6038: 2E 02          LD      L,$02           
603A: 06 90          LD      B,$90           
603C: BE             CP      (HL)            
603D: 55             LD      D,L             
603E: DB 86          IN      A,($86)         
6040: 8D             ADC     A,L             
6041: 06 53          LD      B,$53           
6043: 0D             DEC     C               
6044: 51             LD      D,C             
6045: 0A             LD      A,(BC)          
6046: 0F             RRCA                    
6047: 0E 4D          LD      C,$4D           
6049: 0D             DEC     C               
604A: 24             INC     H               
604B: 14             INC     D               
604C: 08             EX      AF,AF'          
604D: 18 04          JR      $6053           
604F: 02             LD      (BC),A          
6050: 5F             LD      E,A             
6051: BE             CP      (HL)            
6052: 11 04 1A       LD      DE,$1A04        
6055: 4B             LD      C,E             
6056: 7B             LD      A,E             
6057: 81             ADD     A,C             
6058: BF             CP      A               
6059: B3             OR      E               
605A: 14             INC     D               
605B: D6 6A          SUB     $6A             
605D: C8             RET     Z               
605E: 9C             SBC     H               
605F: 73             LD      (HL),E          
6060: 7B             LD      A,E             
6061: 83             ADD     A,E             
6062: 7A             LD      A,D             
6063: 25             DEC     H               
6064: BA             CP      D               
6065: 03             INC     BC              
6066: 71             LD      (HL),C          
6067: 83             ADD     A,E             
6068: 17             RLA                     
6069: 7B             LD      A,E             
606A: 9B             SBC     E               
606B: C9             RET                     
606C: B8             CP      B               
606D: 9B             SBC     E               
606E: C1             POP     BC              
606F: 0D             DEC     C               
6070: 25             DEC     H               
6071: 17             RLA                     
6072: 06 00          LD      B,$00           
6074: 17             RLA                     
6075: 07             RLCA                    
6076: 88             ADC     A,B             
6077: 17             RLA                     
6078: 18 00          JR      $607A           
607A: 04             INC     B               
607B: 1A             LD      A,(DE)          
607C: 5F             LD      E,A             
607D: BE             CP      (HL)            
607E: 66             LD      H,(HL)          
607F: 17             RLA                     
6080: 8F             ADC     A,A             
6081: 49             LD      C,C             
6082: 56             LD      D,(HL)          
6083: 5E             LD      E,(HL)          
6084: 38 C6          JR      C,$604C         
6086: D6 B5          SUB     $B5             
6088: C8             RET     Z               
6089: 9C             SBC     H               
608A: D7             RST     0X10            
608B: 46             LD      B,(HL)          
608C: 82             ADD     A,D             
608D: 17             RLA                     
608E: 59             LD      E,C             
608F: 5E             LD      E,(HL)          
6090: 66             LD      H,(HL)          
6091: 62             LD      H,D             
6092: 09             ADD     HL,BC           
6093: 15             DEC     D               
6094: C7             RST     0X00            
6095: A0             AND     B               
6096: 18 53          JR      $60EB           
6098: 88             ADC     A,B             
6099: 00             NOP                     
609A: 84             ADD     A,H             
609B: 03             INC     BC              
609C: 1C             INC     E               
609D: 5F             LD      E,A             
609E: BE             CP      (HL)            
609F: 5B             LD      E,E             
60A0: B1             OR      C               
60A1: 4B             LD      C,E             
60A2: 7B             LD      A,E             
60A3: 4F             LD      C,A             
60A4: 45             LD      B,L             
60A5: 65             LD      H,L             
60A6: 62             LD      H,D             
60A7: 77             LD      (HL),A          
60A8: 47             LD      B,A             
60A9: D3 14          OUT     ($14),A         
60AB: 0F             RRCA                    
60AC: B4             OR      H               
60AD: 17             RLA                     
60AE: 58             LD      E,B             
60AF: 3F             CCF                     
60B0: 98             SBC     B               
60B1: 96             SUB     (HL)            
60B2: AF             XOR     A               
60B3: DB 72          IN      A,($72)         
60B5: C9             RET                     
60B6: B8             CP      B               
60B7: 9B             SBC     E               
60B8: C1             POP     BC              
60B9: 02             LD      (BC),A          
60BA: 0A             LD      A,(BC)          
60BB: 14             INC     D               
60BC: 53             LD      D,E             
60BD: 66             LD      H,(HL)          
60BE: CA 67 16       JP      Z,$1667         
60C1: D3 B9          OUT     ($B9),A         
60C3: 9B             SBC     E               
60C4: 6C             LD      L,H             
60C5: 07             RLCA                    
60C6: 24             INC     H               
60C7: 0D             DEC     C               
60C8: 22 0A 08       LD      ($080A),HL      
60CB: 04             INC     B               
60CC: 1E 5F          LD      E,$5F           
60CE: BE             CP      (HL)            
60CF: 67             LD      H,A             
60D0: 16 D3          LD      D,$D3           
60D2: B9             CP      C               
60D3: 9B             SBC     E               
60D4: 6C             LD      L,H             
60D5: 1B             DEC     DE              
60D6: B7             OR      A               
60D7: 33             INC     SP              
60D8: BB             CP      E               
60D9: 93             SUB     E               
60DA: 1D             DEC     E               
60DB: 5B             LD      E,E             
60DC: 66             LD      H,(HL)          
60DD: 55             LD      D,L             
60DE: A4             AND     H               
60DF: 09             ADD     HL,BC           
60E0: B7             OR      A               
60E1: 48             LD      C,B             
60E2: 5E             LD      E,(HL)          
60E3: A3             AND     E               
60E4: A0             AND     B               
60E5: 52             LD      D,D             
60E6: 45             LD      B,L             
60E7: 05             DEC     B               
60E8: B2             OR      D               
60E9: DC 63 09       CALL    C,$0963         
60EC: 3B             DEC     SP              
60ED: 90             SUB     B               
60EE: 00             NOP                     
60EF: 80             ADD     A,B             
60F0: 03             INC     BC              
60F1: 0D             DEC     C               
60F2: 5F             LD      E,A             
60F3: BE             CP      (HL)            
60F4: 09             ADD     HL,BC           
60F5: 15             DEC     D               
60F6: A3             AND     E               
60F7: A0             AND     B               
60F8: 4B             LD      C,E             
60F9: 7B             LD      A,E             
60FA: C9             RET                     
60FB: 54             LD      D,H             
60FC: A6             AND     (HL)            
60FD: B7             OR      A               
60FE: 2E 02          LD      L,$02           
6100: 03             INC     BC              
6101: 81             ADD     A,C             
6102: 5B             LD      E,E             
6103: 52             LD      D,D             
6104: 07             RLCA                    
6105: 22 0D 20       LD      ($200D),HL      
6108: 0A             LD      A,(BC)          
6109: 11 17 1B       LD      DE,$1B17        
610C: 00             NOP                     
610D: 17             RLA                     
610E: 1C             INC     E               
610F: 90             SUB     B               
6110: 04             INC     B               
6111: 16 7C          LD      D,$7C           
6113: B3             OR      E               
6114: 6F             LD      L,A             
6115: B3             OR      E               
6116: 27             DAA                     
6117: 60             LD      H,B             
6118: 2D             DEC     L               
6119: 60             LD      H,B             
611A: 8B             ADC     A,E             
611B: 18 5F          JR      $617C           
611D: BE             CP      (HL)            
611E: 09             ADD     HL,BC           
611F: 15             DEC     D               
6120: A3             AND     E               
6121: A0             AND     B               
6122: 4B             LD      C,E             
6123: 7B             LD      A,E             
6124: 5F             LD      E,A             
6125: A0             AND     B               
6126: 1B             DEC     DE              
6127: 9C             SBC     H               
6128: 09             ADD     HL,BC           
6129: 30 00          JR      NC,$612B        
612B: 00             NOP                     
612C: 80             ADD     A,B             
612D: 03             INC     BC              
612E: 12             LD      (DE),A          
612F: 5F             LD      E,A             
6130: BE             CP      (HL)            
6131: 09             ADD     HL,BC           
6132: 15             DEC     D               
6133: A3             AND     E               
6134: A0             AND     B               
6135: 4B             LD      C,E             
6136: 7B             LD      A,E             
6137: FB             EI                      
6138: B9             CP      C               
6139: 43             LD      B,E             
613A: 98             SBC     B               
613B: AB             XOR     E               
613C: 98             SBC     B               
613D: 5F             LD      E,A             
613E: A0             AND     B               
613F: 1B             DEC     DE              
6140: 9C             SBC     H               
6141: 02             LD      (BC),A          
6142: 03             INC     BC              
6143: 81             ADD     A,C             
6144: 5B             LD      E,E             
6145: 52             LD      D,D             
6146: 07             RLCA                    
6147: 12             LD      (DE),A          
6148: 0D             DEC     C               
6149: 10 0A          DJNZ    $6155           
614B: 11 04 0C       LD      DE,$0C04        
614E: 8D             ADC     A,L             
614F: 7B             LD      A,E             
6150: 8E             ADC     A,(HL)          
6151: 14             INC     D               
6152: 63             LD      H,E             
6153: B1             OR      C               
6154: FB             EI                      
6155: 5C             LD      E,H             
6156: 5F             LD      E,A             
6157: A0             AND     B               
6158: 1B             DEC     DE              
6159: 9C             SBC     H               
615A: FF             RST     0X38            
615B: 80             ADD     A,B             
615C: 87             ADD     A,A             
615D: 96             SUB     (HL)            
615E: 00             NOP                     
615F: 80             ADD     A,B             
6160: 0A             LD      A,(BC)          
6161: 76             HALT                    
6162: 0E 74          LD      C,$74           
6164: 0B             DEC     BC              
6165: 07             RLCA                    
6166: 20 1D          JR      NZ,$6185        
6168: 01 81 23       LD      BC,$2381        
616B: 01 81 0D       LD      BC,$0D81        
616E: 69             LD      L,C             
616F: 1F             RRA                     
6170: 66             LD      H,(HL)          
6171: C7             RST     0X00            
6172: DE DB          SBC     $DB             
6174: 16 CB          LD      D,$CB           
6176: B9             CP      C               
6177: 36 A1          LD      (HL),$A1        
6179: 59             LD      E,C             
617A: F4 F0 72       CALL    P,$72F0         
617D: 51             LD      D,C             
617E: 18 43          JR      $61C3           
6180: C2 0D D0       JP      NZ,$D00D        
6183: A6             AND     (HL)            
6184: 61             LD      H,C             
6185: 51             LD      D,C             
6186: 18 48          JR      $61D0           
6188: C2 8E 7A       JP      NZ,$7A8E        
618B: 51             LD      D,C             
618C: 18 3D          JR      $61CB           
618E: C6 40          ADD     $40             
6190: 61             LD      H,C             
6191: DA 14 D0       JP      C,$D014         
6194: 47             LD      B,A             
6195: F3             DI                      
6196: 5F             LD      E,A             
6197: 6B             LD      L,E             
6198: BF             CP      A               
6199: 44             LD      B,H             
619A: 45             LD      B,L             
619B: 81             ADD     A,C             
619C: 8D             ADC     A,L             
619D: 15             DEC     D               
619E: 58             LD      E,B             
619F: 4B             LD      C,E             
61A0: BD             CP      L               
61A1: 66             LD      H,(HL)          
61A2: 98             SBC     B               
61A3: 8E             ADC     A,(HL)          
61A4: 14             INC     D               
61A5: 54             LD      D,H             
61A6: BD             CP      L               
61A7: 43             LD      B,E             
61A8: F4 EC 16       CALL    P,$16EC         
61AB: 35             DEC     (HL)            
61AC: 79             LD      A,C             
61AD: 0B             DEC     BC              
61AE: BC             CP      H               
61AF: CD B5 67       CALL    $67B5           
61B2: 98             SBC     B               
61B3: 90             SUB     B               
61B4: 8C             ADC     A,H             
61B5: D1             POP     DE              
61B6: 6A             LD      L,D             
61B7: 74             LD      (HL),H          
61B8: CA 51 18       JP      Z,$1851         
61BB: 59             LD      E,C             
61BC: C2 82 7B       JP      NZ,$7B82        
61BF: 7B             LD      A,E             
61C0: 14             INC     D               
61C1: 13             INC     DE              
61C2: 87             ADD     A,A             
61C3: 7F             LD      A,A             
61C4: 66             LD      H,(HL)          
61C5: D6 15          SUB     $15             
61C7: 49             LD      C,C             
61C8: 16 A5          LD      D,$A5           
61CA: 9F             SBC     A               
61CB: 43             LD      B,E             
61CC: 16 9B          LD      D,$9B           
61CE: 85             ADD     A,L             
61CF: 63             LD      H,E             
61D0: BE             CP      (HL)            
61D1: CB B5          RES     6,L             
61D3: CB B5          RES     6,L             
61D5: 9B             SBC     E               
61D6: C1             POP     BC              
61D7: 81             ADD     A,C             
61D8: 08             EX      AF,AF'          
61D9: 06 0D          LD      B,$0D           
61DB: 04             INC     B               
61DC: 1C             INC     E               
61DD: 1D             DEC     E               
61DE: 23             INC     HL              
61DF: 05             DEC     B               
61E0: 09             ADD     HL,BC           
61E1: 02             LD      (BC),A          
61E2: 46             LD      B,(HL)          
61E3: 46             LD      B,(HL)          
61E4: 0F             RRCA                    
61E5: 81             ADD     A,C             
61E6: B4             OR      H               
61E7: 00             NOP                     
61E8: 00             NOP                     
61E9: 90             SUB     B               
61EA: 03             INC     BC              
61EB: 25             DEC     H               
61EC: 5F             LD      E,A             
61ED: BE             CP      (HL)            
61EE: 5B             LD      E,E             
61EF: B1             OR      C               
61F0: 4B             LD      C,E             
61F1: 7B             LD      A,E             
61F2: 4A             LD      C,D             
61F3: 45             LD      B,L             
61F4: FF             RST     0X38            
61F5: 78             LD      A,B             
61F6: 35             DEC     (HL)            
61F7: A1             AND     C               
61F8: 73             LD      (HL),E          
61F9: 15             DEC     D               
61FA: C1             POP     BC              
61FB: B1             OR      C               
61FC: 3F             CCF                     
61FD: DE B6          SBC     $B6             
61FF: 14             INC     D               
6200: 5D             LD      E,L             
6201: 9E             SBC     (HL)            
6202: 91             SUB     C               
6203: 7A             LD      A,D             
6204: 82             ADD     A,D             
6205: 17             RLA                     
6206: 50             LD      D,B             
6207: 5E             LD      E,(HL)          
6208: BE             CP      (HL)            
6209: A0             AND     B               
620A: 12             LD      (DE),A          
620B: 71             LD      (HL),C          
620C: 65             LD      H,L             
620D: 49             LD      C,C             
620E: 77             LD      (HL),A          
620F: 47             LD      B,A             
6210: 2E 02          LD      L,$02           
6212: 06 14          LD      B,$14           
6214: 6C             LD      L,H             
6215: 4B             LD      C,E             
6216: 6E             LD      L,(HL)          
6217: DB 8B          IN      A,($8B)         
6219: 09             ADD     HL,BC           
621A: 02             LD      (BC),A          
621B: FF             RST     0X38            
621C: FF             RST     0X38            
621D: 07             RLCA                    
621E: 22 0D 20       LD      ($200D),HL      
6221: 0A             LD      A,(BC)          
6222: 15             DEC     D               
6223: 04             INC     B               
6224: 1C             INC     E               
6225: DD 72 F3       LD      (IX+$F3),D      
6228: 8C             ADC     A,H             
6229: 96             SUB     (HL)            
622A: 5F             LD      E,A             
622B: 51             LD      D,C             
622C: 18 4E          JR      $627C           
622E: C2 11 A0       JP      NZ,$A011        
6231: AF             XOR     A               
6232: 14             INC     D               
6233: 04             INC     B               
6234: 68             LD      L,B             
6235: 5B             LD      E,E             
6236: 5E             LD      E,(HL)          
6237: 1D             DEC     E               
6238: A1             AND     C               
6239: F3             DI                      
623A: 8C             ADC     A,H             
623B: 96             SUB     (HL)            
623C: 5F             LD      E,A             
623D: A3             AND     E               
623E: 15             DEC     D               
623F: EB             EX      DE,HL           
6240: 8F             ADC     A,A             
6241: 08             EX      AF,AF'          
6242: 81             ADD     A,C             
6243: 29             ADD     HL,HL           
6244: 0D             DEC     C               
6245: 81             ADD     A,C             
6246: 26 01          LD      H,$01           
6248: 1D             DEC     E               
6249: 1C             INC     E               
624A: 1D             DEC     E               
624B: 14             INC     D               
624C: 01 12 0B       LD      BC,$0B12        
624F: 81             ADD     A,C             
6250: 1C             INC     E               
6251: 05             DEC     B               
6252: 19             ADD     HL,DE           
6253: 2E 0D          LD      L,$0D           
6255: 2C             INC     L               
6256: 1F             RRA                     
6257: 28 5F          JR      Z,$62B8         
6259: BE             CP      (HL)            
625A: 73             LD      (HL),E          
625B: 15             DEC     D               
625C: C1             POP     BC              
625D: B1             OR      C               
625E: 3F             CCF                     
625F: DE 81          SBC     $81             
6261: 15             DEC     D               
6262: 75             LD      (HL),L          
6263: B1             OR      C               
6264: 51             LD      D,C             
6265: 18 59          JR      $62C0           
6267: C2 82 7B       JP      NZ,$7B82        
626A: A3             AND     E               
626B: 15             DEC     D               
626C: CA B5 B8       JP      Z,$B8B5         
626F: A0             AND     B               
6270: 90             SUB     B               
6271: 14             INC     D               
6272: 14             INC     D               
6273: 58             LD      E,B             
6274: ED 7A          ADC     HL,SP           
6276: 51             LD      D,C             
6277: 18 23          JR      $629C           
6279: C6 36          ADD     $36             
627B: 6F             LD      L,A             
627C: D1             POP     DE              
627D: B5             OR      L               
627E: 71             LD      (HL),C          
627F: C6 1D          ADD     $1D             
6281: FF             RST     0X38            
6282: 3F             CCF                     
6283: 21 0D 1F       LD      HL,$1F0D        
6286: 1F             RRA                     
6287: 1B             DEC     DE              
6288: 5F             LD      E,A             
6289: BE             CP      (HL)            
628A: 73             LD      (HL),E          
628B: 15             DEC     D               
628C: C1             POP     BC              
628D: B1             OR      C               
628E: 3F             CCF                     
628F: DE DE          SBC     $DE             
6291: 14             INC     D               
6292: 05             DEC     B               
6293: 4A             LD      C,D             
6294: 51             LD      D,C             
6295: 18 43          JR      $62DA           
6297: C2 B9 55       JP      NZ,$55B9        
629A: CB B9          RES     7,C             
629C: 5F             LD      E,A             
629D: BE             CP      (HL)            
629E: DA 14 66       JP      C,$6614         
62A1: 62             LD      H,D             
62A2: 21 1D 32       LD      HL,$321D        
62A5: 64             LD      H,H             
62A6: 2E 0D          LD      L,$0D           
62A8: 2C             INC     L               
62A9: 1F             RRA                     
62AA: 28 C7          JR      Z,$6273         
62AC: DE 4F          SBC     $4F             
62AE: 15             DEC     D               
62AF: 33             INC     SP              
62B0: 61             LD      H,C             
62B1: 5F             LD      E,A             
62B2: BE             CP      (HL)            
62B3: 80             ADD     A,B             
62B4: 15             DEC     D               
62B5: 5A             LD      E,D             
62B6: 49             LD      C,C             
62B7: 91             SUB     C               
62B8: 7A             LD      A,D             
62B9: B8             CP      B               
62BA: 16 82          LD      D,$82           
62BC: 17             RLA                     
62BD: 49             LD      C,C             
62BE: 5E             LD      E,(HL)          
62BF: 31 49 CE       LD      SP,$CE49        
62C2: A1             AND     C               
62C3: A5             AND     L               
62C4: 5E             LD      E,(HL)          
62C5: 7F             LD      A,A             
62C6: 17             RLA                     
62C7: 82             ADD     A,D             
62C8: 62             LD      H,D             
62C9: D0             RET     NC              
62CA: 15             DEC     D               
62CB: 51             LD      D,C             
62CC: 18 23          JR      $62F1           
62CE: C6 46          ADD     $46             
62D0: B8             CP      B               
62D1: EB             EX      DE,HL           
62D2: 5D             LD      E,L             
62D3: 1D             DEC     E               
62D4: 32 A3 3C       LD      ($3CA3),A       
62D7: 0D             DEC     C               
62D8: 3A 1F 36       LD      A,($361F)       
62DB: 5F             LD      E,A             
62DC: BE             CP      (HL)            
62DD: DE 14          SBC     $14             
62DF: 05             DEC     B               
62E0: 4A             LD      C,D             
62E1: B8             CP      B               
62E2: 16 82          LD      D,$82           
62E4: 17             RLA                     
62E5: 49             LD      C,C             
62E6: 5E             LD      E,(HL)          
62E7: 31 49 CE       LD      SP,$CE49        
62EA: A1             AND     C               
62EB: 54             LD      D,H             
62EC: 5E             LD      E,(HL)          
62ED: D3 7A          OUT     ($7A),A         
62EF: 6C             LD      L,H             
62F0: BE             CP      (HL)            
62F1: 29             ADD     HL,HL           
62F2: A1             AND     C               
62F3: 1B             DEC     DE              
62F4: 71             LD      (HL),C          
62F5: 34             INC     (HL)            
62F6: A1             AND     C               
62F7: 94             SUB     H               
62F8: 14             INC     D               
62F9: 4B             LD      C,E             
62FA: 90             SUB     B               
62FB: 83             ADD     A,E             
62FC: 96             SUB     (HL)            
62FD: 83             ADD     A,E             
62FE: 96             SUB     (HL)            
62FF: 3F             CCF                     
6300: C0             RET     NZ              
6301: EE 93          XOR     $93             
6303: 89             ADC     A,C             
6304: 17             RLA                     
6305: 2F             CPL                     
6306: 17             RLA                     
6307: DA 46 51       JP      C,$5146         
630A: 18 23          JR      $632F           
630C: C6 F6          ADD     $F6             
630E: 4E             LD      C,(HL)          
630F: EB             EX      DE,HL           
6310: DA 1D 19       JP      C,$191D         
6313: E1             POP     HL              
6314: 3E 0D          LD      A,$0D           
6316: 3C             INC     A               
6317: 1F             RRA                     
6318: 38 5F          JR      C,$6379         
631A: BE             CP      (HL)            
631B: 73             LD      (HL),E          
631C: 15             DEC     D               
631D: C1             POP     BC              
631E: B1             OR      C               
631F: 3F             CCF                     
6320: DE 4F          SBC     $4F             
6322: 16 B7          LD      D,$B7           
6324: 98             SBC     B               
6325: C3 B5 1B       JP      $1BB5           
6328: BC             CP      H               
6329: 34             INC     (HL)            
632A: A1             AND     C               
632B: 4B             LD      C,E             
632C: 15             DEC     D               
632D: 9B             SBC     E               
632E: 53             LD      D,E             
632F: F6 4F          OR      $4F             
6331: 51             LD      D,C             
6332: 18 52          JR      $6386           
6334: C2 46 C5       JP      NZ,$C546        
6337: AB             XOR     E               
6338: 14             INC     D               
6339: AF             XOR     A               
633A: 54             LD      D,H             
633B: 4A             LD      C,D             
633C: 13             INC     DE              
633D: 44             LD      B,H             
633E: 5E             LD      E,(HL)          
633F: 7F             LD      A,A             
6340: 7B             LD      A,E             
6341: DB B5          IN      A,($B5)         
6343: 34             INC     (HL)            
6344: A1             AND     C               
6345: 5A             LD      E,D             
6346: 17             RLA                     
6347: 2E A1          LD      L,$A1           
6349: F4 59 D0       CALL    P,$D059         
634C: 15             DEC     D               
634D: FF             RST     0X38            
634E: B9             CP      C               
634F: F1             POP     AF              
6350: 46             LD      B,(HL)          
6351: 1D             DEC     E               
6352: 19             ADD     HL,DE           
6353: FF             RST     0X38            
6354: 18 0D          JR      $6363           
6356: 16 1F          LD      D,$1F           
6358: 14             INC     D               
6359: C7             RST     0X00            
635A: DE 09          SBC     $09             
635C: 15             DEC     D               
635D: 37             SCF                     
635E: 5A             LD      E,D             
635F: 82             ADD     A,D             
6360: 17             RLA                     
6361: 49             LD      C,C             
6362: 5E             LD      E,(HL)          
6363: 31 49 CE       LD      SP,$CE49        
6366: A1             AND     C               
6367: A5             AND     L               
6368: 5E             LD      E,(HL)          
6369: A9             XOR     C               
636A: 15             DEC     D               
636B: E7             RST     0X20            
636C: B2             OR      D               
636D: 0A             LD      A,(BC)          
636E: 2C             INC     L               
636F: 0D             DEC     C               
6370: 2A 1F 22       LD      HL,($221F)      
6373: 5F             LD      E,A             
6374: BE             CP      (HL)            
6375: 73             LD      (HL),E          
6376: 15             DEC     D               
6377: C1             POP     BC              
6378: B1             OR      C               
6379: 3F             CCF                     
637A: DE 7B          SBC     $7B             
637C: 17             RLA                     
637D: B5             OR      L               
637E: 85             ADD     A,L             
637F: 7B             LD      A,E             
6380: 14             INC     D               
6381: 10 67          DJNZ    $63EA           
6383: 33             INC     SP              
6384: 48             LD      C,B             
6385: 6F             LD      L,A             
6386: 4F             LD      C,A             
6387: 82             ADD     A,D             
6388: 49             LD      C,C             
6389: 90             SUB     B               
638A: 14             INC     D               
638B: 16 58          LD      D,$58           
638D: F0             RET     P               
638E: 72             LD      (HL),D          
638F: 3A 15 94       LD      A,($9415)       
6392: A5             AND     L               
6393: 6F             LD      L,A             
6394: 62             LD      H,D             
6395: 17             RLA                     
6396: 1E 00          LD      E,$00           
6398: 17             RLA                     
6399: 1F             RRA                     
639A: 8E             ADC     A,(HL)          
639B: 0F             RRCA                    
639C: 53             LD      D,E             
639D: 00             NOP                     
639E: 00             NOP                     
639F: 80             ADD     A,B             
63A0: 03             INC     BC              
63A1: 24             INC     H               
63A2: 5F             LD      E,A             
63A3: BE             CP      (HL)            
63A4: 5B             LD      E,E             
63A5: B1             OR      C               
63A6: 4B             LD      C,E             
63A7: 7B             LD      A,E             
63A8: 5F             LD      E,A             
63A9: BE             CP      (HL)            
63AA: FF             RST     0X38            
63AB: 14             INC     D               
63AC: F3             DI                      
63AD: 46             LD      B,(HL)          
63AE: 14             INC     D               
63AF: 53             LD      D,E             
63B0: 15             DEC     D               
63B1: 53             LD      D,E             
63B2: D1             POP     DE              
63B3: B5             OR      L               
63B4: 83             ADD     A,E             
63B5: 64             LD      H,H             
63B6: 97             SUB     A               
63B7: 96             SUB     (HL)            
63B8: D3 6D          OUT     ($6D),A         
63BA: 73             LD      (HL),E          
63BB: 15             DEC     D               
63BC: C1             POP     BC              
63BD: B1             OR      C               
63BE: 3F             CCF                     
63BF: DE 8F          SBC     $8F             
63C1: 16 2C          LD      D,$2C           
63C3: 49             LD      C,C             
63C4: DB E0          IN      A,($E0)         
63C6: 07             RLCA                    
63C7: 1D             DEC     E               
63C8: 0D             DEC     C               
63C9: 1B             DEC     DE              
63CA: 0A             LD      A,(BC)          
63CB: 15             DEC     D               
63CC: 04             INC     B               
63CD: 17             RLA                     
63CE: 7A             LD      A,D             
63CF: C4 CB 06       CALL    NZ,$06CB        
63D2: 82             ADD     A,D             
63D3: 17             RLA                     
63D4: 95             SUB     L               
63D5: 7A             LD      A,D             
63D6: BD             CP      L               
63D7: 15             DEC     D               
63D8: 49             LD      C,C             
63D9: 90             SUB     B               
63DA: 50             LD      D,B             
63DB: 9F             SBC     A               
63DC: D6 6A          SUB     $6A             
63DE: C4 9C 55       CALL    NZ,$559C        
63E1: 5E             LD      E,(HL)          
63E2: DD             ???                     
63E3: 78             LD      A,B             
63E4: 21 02 09       LD      HL,$0902        
63E7: E3             EX      (SP),HL         
63E8: 59             LD      E,C             
63E9: 09             ADD     HL,BC           
63EA: 58             LD      E,B             
63EB: 31 49 CE       LD      SP,$CE49        
63EE: A1             AND     C               
63EF: 45             LD      B,L             
63F0: 25             DEC     H               
63F1: 32 FF 00       LD      ($00FF),A       
63F4: 80             ADD     A,B             
63F5: 07             RLCA                    
63F6: 28 0B          JR      Z,$6403         
63F8: 26 0A          LD      H,$0A           
63FA: 17             RLA                     
63FB: 20 04          JR      NZ,$6401        
63FD: 1E C7          LD      E,$C7           
63FF: DE D3          SBC     $D3             
6401: 14             INC     D               
6402: 90             SUB     B               
6403: 96             SUB     (HL)            
6404: F3             DI                      
6405: A0             AND     B               
6406: C3 54 A3       JP      $A354           
6409: 91             SUB     C               
640A: 5F             LD      E,A             
640B: BE             CP      (HL)            
640C: F3             DI                      
640D: 17             RLA                     
640E: 16 8D          LD      D,$8D           
6410: D6 15          SUB     $15             
6412: D5             PUSH    DE              
6413: 15             DEC     D               
6414: 89             ADC     A,C             
6415: 17             RLA                     
6416: D5             PUSH    DE              
6417: 9C             SBC     H               
6418: C1             POP     BC              
6419: 93             SUB     E               
641A: 77             LD      (HL),A          
641B: BE             CP      (HL)            
641C: 34             INC     (HL)            
641D: 01 89 02       LD      BC,$0289        
6420: 03             INC     BC              
6421: 0E D0          LD      C,$D0           
6423: 4C             LD      C,H             
6424: 26 29          LD      H,$29           
6426: 9D             SBC     L               
6427: 00             NOP                     
6428: 80             ADD     A,B             
6429: 03             INC     BC              
642A: 1E 4E          LD      E,$4E           
642C: 45             LD      B,L             
642D: 31 49 50       LD      SP,$5049        
6430: 5E             LD      E,(HL)          
6431: 91             SUB     C               
6432: 62             LD      H,D             
6433: B5             OR      L               
6434: A0             AND     B               
6435: B8             CP      B               
6436: 16 D3          LD      D,$D3           
6438: 17             RLA                     
6439: 75             LD      (HL),L          
643A: 98             SBC     B               
643B: DE 14          SBC     $14             
643D: 91             SUB     C               
643E: 7A             LD      A,D             
643F: D6 B5          SUB     $B5             
6441: D6 9C          SUB     $9C             
6443: DB 72          IN      A,($72)         
6445: 0E D0          LD      C,$D0           
6447: 9B             SBC     E               
6448: 8F             ADC     A,A             
6449: 02             LD      (BC),A          
644A: 04             INC     B               
644B: 10 CB          DJNZ    $6418           
644D: 4B             LD      C,E             
644E: 62             LD      H,D             
644F: 1E 28          LD      E,$28           
6451: 8F             ADC     A,A             
6452: 05             DEC     B               
6453: A0             AND     B               
6454: 03             INC     BC              
6455: 16 5F          LD      D,$5F           
6457: BE             CP      (HL)            
6458: 5B             LD      E,E             
6459: B1             OR      C               
645A: 4B             LD      C,E             
645B: 7B             LD      A,E             
645C: 49             LD      C,C             
645D: 45             LD      B,L             
645E: BE             CP      (HL)            
645F: 9F             SBC     A               
6460: 83             ADD     A,E             
6461: 61             LD      H,C             
6462: 29             ADD     HL,HL           
6463: 54             LD      D,H             
6464: 26 A7          LD      H,$A7           
6466: DD             ???                     
6467: 78             LD      A,B             
6468: 9F             SBC     A               
6469: 15             DEC     D               
646A: 7F             LD      A,A             
646B: B1             OR      C               
646C: 02             LD      (BC),A          
646D: 0B             DEC     BC              
646E: 3E 6E          LD      A,$6E           
6470: F0             RET     P               
6471: 59             LD      E,C             
6472: DA 14 6D       JP      C,$6D14         
6475: A0             AND     B               
6476: 85             ADD     A,L             
6477: BE             CP      (HL)            
6478: 4B             LD      C,E             
6479: 28 80          JR      Z,$63FB         
647B: CA 9C 00       JP      Z,$009C         
647E: 90             SUB     B               
647F: 03             INC     BC              
6480: 27             DAA                     
6481: B8             CP      B               
6482: B7             OR      A               
6483: 2B             DEC     HL              
6484: 62             LD      H,D             
6485: 09             ADD     HL,BC           
6486: 8A             ADC     A,D             
6487: 94             SUB     H               
6488: C3 0B 5C       JP      $5C0B           
648B: 14             INC     D               
648C: 53             LD      D,E             
648D: 8B             ADC     A,E             
648E: B4             OR      H               
648F: AB             XOR     E               
6490: 98             SBC     B               
6491: F6 8B          OR      $8B             
6493: 4E             LD      C,(HL)          
6494: 72             LD      (HL),D          
6495: E4 14 E5       CALL    PO,$E514        
6498: A0             AND     B               
6499: 09             ADD     HL,BC           
649A: 4F             LD      C,A             
649B: D6 B5          SUB     $B5             
649D: 38 C6          JR      C,$6465         
649F: 89             ADC     A,C             
64A0: 17             RLA                     
64A1: 4B             LD      C,E             
64A2: 15             DEC     D               
64A3: 9B             SBC     E               
64A4: 53             LD      D,E             
64A5: C7             RST     0X00            
64A6: DE 2E          SBC     $2E             
64A8: 08             EX      AF,AF'          
64A9: 80             ADD     A,B             
64AA: 95             SUB     L               
64AB: 0E 80          LD      C,$80           
64AD: 92             SUB     D               
64AE: 0D             DEC     C               
64AF: 2F             CPL                     
64B0: 14             INC     D               
64B1: 01 1D 0B       LD      BC,$0B1D        
64B4: 29             ADD     HL,HL           
64B5: 03             INC     BC              
64B6: 9C             SBC     H               
64B7: 23             INC     HL              
64B8: 07             RLCA                    
64B9: 0D             DEC     C               
64BA: 05             DEC     B               
64BB: 00             NOP                     
64BC: 9D             SBC     L               
64BD: 01 1D 86       LD      BC,$861D        
64C0: 9F             SBC     A               
64C1: 23             INC     HL              
64C2: 07             RLCA                    
64C3: 0D             DEC     C               
64C4: 05             DEC     B               
64C5: 00             NOP                     
64C6: 9C             SBC     H               
64C7: 01 1D 86       LD      BC,$861D        
64CA: 9E             SBC     (HL)            
64CB: 23             INC     HL              
64CC: 07             RLCA                    
64CD: 0D             DEC     C               
64CE: 05             DEC     B               
64CF: 00             NOP                     
64D0: 9F             SBC     A               
64D1: 01 1D 86       LD      BC,$861D        
64D4: 9D             SBC     L               
64D5: 23             INC     HL              
64D6: 07             RLCA                    
64D7: 0D             DEC     C               
64D8: 05             DEC     B               
64D9: 00             NOP                     
64DA: 9E             SBC     (HL)            
64DB: 01 1D 86       LD      BC,$861D        
64DE: 0C             INC     C               
64DF: 0D             DEC     C               
64E0: 5F             LD      E,A             
64E1: 01 1D 1C       LD      BC,$1C1D        
64E4: 1D             DEC     E               
64E5: 1F             RRA                     
64E6: 58             LD      E,B             
64E7: A6             AND     (HL)            
64E8: 1D             DEC     E               
64E9: 51             LD      D,C             
64EA: A0             AND     B               
64EB: D0             RET     NC              
64EC: 15             DEC     D               
64ED: 06 67          LD      B,$67           
64EF: 33             INC     SP              
64F0: 61             LD      H,C             
64F1: 79             LD      A,C             
64F2: 5B             LD      E,E             
64F3: 06 07          LD      B,$07           
64F5: 82             ADD     A,D             
64F6: 17             RLA                     
64F7: 49             LD      C,C             
64F8: 5E             LD      E,(HL)          
64F9: 94             SUB     H               
64FA: C3 0B 5C       JP      $5C0B           
64FD: F8             RET     M               
64FE: 8B             ADC     A,E             
64FF: 33             INC     SP              
6500: 61             LD      H,C             
6501: 5F             LD      E,A             
6502: BE             CP      (HL)            
6503: 23             INC     HL              
6504: 7B             LD      A,E             
6505: B9             CP      C               
6506: 55             LD      D,L             
6507: D4 B9 85       CALL    NC,$85B9        
650A: A1             AND     C               
650B: 90             SUB     B               
650C: 14             INC     D               
650D: 0E 58          LD      C,$58           
650F: 45             LD      B,L             
6510: A0             AND     B               
6511: 56             LD      D,(HL)          
6512: 5E             LD      E,(HL)          
6513: EB             EX      DE,HL           
6514: 72             LD      (HL),D          
6515: 84             ADD     A,H             
6516: AF             XOR     A               
6517: CE 9F          ADC     $9F             
6519: 6B             LD      L,E             
651A: B5             OR      L               
651B: C7             RST     0X00            
651C: DE 84          SBC     $84             
651E: AF             XOR     A               
651F: 93             SUB     E               
6520: 9E             SBC     (HL)            
6521: 4B             LD      C,E             
6522: 15             DEC     D               
6523: 0D             DEC     C               
6524: 8D             ADC     A,L             
6525: 89             ADC     A,C             
6526: 17             RLA                     
6527: 82             ADD     A,D             
6528: 17             RLA                     
6529: 49             LD      C,C             
652A: 5E             LD      E,(HL)          
652B: 07             RLCA                    
652C: B3             OR      E               
652D: 33             INC     SP              
652E: 98             SBC     B               
652F: 06 B2          LD      B,$B2           
6531: FF             RST     0X38            
6532: 5A             LD      E,D             
6533: 19             ADD     HL,DE           
6534: 58             LD      E,B             
6535: 82             ADD     A,D             
6536: 7B             LD      A,E             
6537: 82             ADD     A,D             
6538: 17             RLA                     
6539: 55             LD      D,L             
653A: 5E             LD      E,(HL)          
653B: 48             LD      C,B             
653C: 72             LD      (HL),D          
653D: 09             ADD     HL,BC           
653E: C0             RET     NZ              
653F: 81             ADD     A,C             
6540: 02             LD      (BC),A          
6541: 04             INC     B               
6542: 23             INC     HL              
6543: 6F             LD      L,A             
6544: 4D             LD      C,L             
6545: B1             OR      C               
6546: 29             ADD     HL,HL           
6547: 4C             LD      C,H             
6548: 1D             DEC     E               
6549: 00             NOP                     
654A: 00             NOP                     
654B: 08             EX      AF,AF'          
654C: 47             LD      B,A             
654D: 0B             DEC     BC              
654E: 45             LD      B,L             
654F: 03             INC     BC              
6550: 9C             SBC     H               
6551: 23             INC     HL              
6552: 0E 0E          LD      C,$0E           
6554: 0C             INC     C               
6555: 0D             DEC     C               
6556: 04             INC     B               
6557: 03             INC     BC              
6558: 9A             SBC     D               
6559: 1D             DEC     E               
655A: 85             ADD     A,L             
655B: 0D             DEC     C               
655C: 04             INC     B               
655D: 03             INC     BC              
655E: 99             SBC     C               
655F: 1D             DEC     E               
6560: 87             ADD     A,A             
6561: 9F             SBC     A               
6562: 23             INC     HL              
6563: 0E 0E          LD      C,$0E           
6565: 0C             INC     C               
6566: 0D             DEC     C               
6567: 04             INC     B               
6568: 03             INC     BC              
6569: 99             SBC     C               
656A: 1D             DEC     E               
656B: 85             ADD     A,L             
656C: 0D             DEC     C               
656D: 04             INC     B               
656E: 03             INC     BC              
656F: 98             SBC     B               
6570: 1D             DEC     E               
6571: 87             ADD     A,A             
6572: 9E             SBC     (HL)            
6573: 23             INC     HL              
6574: 0E 0E          LD      C,$0E           
6576: 0C             INC     C               
6577: 0D             DEC     C               
6578: 04             INC     B               
6579: 03             INC     BC              
657A: 98             SBC     B               
657B: 1D             DEC     E               
657C: 85             ADD     A,L             
657D: 0D             DEC     C               
657E: 04             INC     B               
657F: 03             INC     BC              
6580: 9B             SBC     E               
6581: 1D             DEC     E               
6582: 87             ADD     A,A             
6583: 9D             SBC     L               
6584: 23             INC     HL              
6585: 0E 0E          LD      C,$0E           
6587: 0C             INC     C               
6588: 0D             DEC     C               
6589: 04             INC     B               
658A: 03             INC     BC              
658B: 9B             SBC     E               
658C: 1D             DEC     E               
658D: 85             ADD     A,L             
658E: 0D             DEC     C               
658F: 04             INC     B               
6590: 03             INC     BC              
6591: 9A             SBC     D               
6592: 1D             DEC     E               
6593: 87             ADD     A,A             
6594: 13             INC     DE              
6595: 30 9C          JR      NC,$6533        
6597: 00             NOP                     
6598: A0             AND     B               
6599: 02             LD      (BC),A          
659A: 08             EX      AF,AF'          
659B: EF             RST     0X28            
659C: A6             AND     (HL)            
659D: 51             LD      D,C             
659E: 54             LD      D,H             
659F: 4B             LD      C,E             
65A0: C6 AF          ADD     $AF             
65A2: 6C             LD      L,H             
65A3: 08             EX      AF,AF'          
65A4: 21 0D 1F       LD      HL,$1F0D        
65A7: 03             INC     BC              
65A8: 9C             SBC     H               
65A9: 25             DEC     H               
65AA: 0B             DEC     BC              
65AB: 1A             LD      A,(DE)          
65AC: 05             DEC     B               
65AD: 33             INC     SP              
65AE: 03             INC     BC              
65AF: 17             RLA                     
65B0: 25             DEC     H               
65B1: 89             ADC     A,C             
65B2: 66             LD      H,(HL)          
65B3: 03             INC     BC              
65B4: 17             RLA                     
65B5: 25             DEC     H               
65B6: 94             SUB     H               
65B7: 99             SBC     C               
65B8: 03             INC     BC              
65B9: 17             RLA                     
65BA: 25             DEC     H               
65BB: 86             ADD     A,(HL)          
65BC: CC 03 17       CALL    Z,$1703         
65BF: 25             DEC     H               
65C0: 8E             ADC     A,(HL)          
65C1: FF             RST     0X38            
65C2: 03             INC     BC              
65C3: 17             RLA                     
65C4: 25             DEC     H               
65C5: 83             ADD     A,E             
65C6: 13             INC     DE              
65C7: 23             INC     HL              
65C8: 00             NOP                     
65C9: 05             DEC     B               
65CA: A0             AND     B               
65CB: 02             LD      (BC),A          
65CC: 08             EX      AF,AF'          
65CD: EF             RST     0X28            
65CE: A6             AND     (HL)            
65CF: 51             LD      D,C             
65D0: 54             LD      D,H             
65D1: 4B             LD      C,E             
65D2: C6 AF          ADD     $AF             
65D4: 6C             LD      L,H             
65D5: 03             INC     BC              
65D6: 14             INC     D               
65D7: 5F             LD      E,A             
65D8: BE             CP      (HL)            
65D9: 5B             LD      E,E             
65DA: B1             OR      C               
65DB: 4B             LD      C,E             
65DC: 7B             LD      A,E             
65DD: 52             LD      D,D             
65DE: 45             LD      B,L             
65DF: 65             LD      H,L             
65E0: B1             OR      C               
65E1: C7             RST     0X00            
65E2: 7A             LD      A,D             
65E3: C9             RET                     
65E4: B5             OR      L               
65E5: 5B             LD      E,E             
65E6: 61             LD      H,C             
65E7: F4 72 DB       CALL    P,$DB72         
65EA: 63             LD      H,E             
65EB: 2A 32 FF       LD      HL,($FF32)      
65EE: 00             NOP                     
65EF: 00             NOP                     
65F0: 02             LD      (BC),A          
65F1: 03             INC     BC              
65F2: 01 B3 4D       LD      BC,$4DB3        
65F5: 07             RLCA                    
65F6: 28 0D          JR      Z,$6605         
65F8: 26 0A          LD      H,$0A           
65FA: 0B             DEC     BC              
65FB: 01 25 04       LD      BC,$0425        
65FE: 20 C7          JR      NZ,$65C7        
6600: DE 03          SBC     $03             
6602: 15             DEC     D               
6603: 61             LD      H,C             
6604: B7             OR      A               
6605: 74             LD      (HL),H          
6606: CA 7B 14       JP      Z,$147B         
6609: EF             RST     0X28            
660A: A6             AND     (HL)            
660B: 51             LD      D,C             
660C: 54             LD      D,H             
660D: 4B             LD      C,E             
660E: C6 AF          ADD     $AF             
6610: 6C             LD      L,H             
6611: A3             AND     E               
6612: 15             DEC     D               
6613: BF             CP      A               
6614: 59             LD      E,C             
6615: 8B             ADC     A,E             
6616: 96             SUB     (HL)            
6617: 83             ADD     A,E             
6618: 96             SUB     (HL)            
6619: E4 14 D3       CALL    PO,$D314        
661C: 62             LD      H,D             
661D: BF             CP      A               
661E: 53             LD      D,E             
661F: 1B             DEC     DE              
6620: 62             LD      H,D             
6621: 00             NOP                     
6622: 00             NOP                     
6623: AC             XOR     H               
6624: 02             LD      (BC),A          
6625: 03             INC     BC              
6626: 4F             LD      C,A             
6627: 8B             ADC     A,E             
6628: 50             LD      D,B             
6629: 03             INC     BC              
662A: 0E 5F          LD      C,$5F           
662C: BE             CP      (HL)            
662D: 5B             LD      E,E             
662E: B1             OR      C               
662F: 4B             LD      C,E             
6630: 7B             LD      A,E             
6631: 4E             LD      C,(HL)          
6632: 45             LD      B,L             
6633: 72             LD      (HL),D          
6634: 48             LD      C,B             
6635: 9F             SBC     A               
6636: 15             DEC     D               
6637: 7F             LD      A,A             
6638: B1             OR      C               
6639: 07             RLCA                    
663A: 48             LD      C,B             
663B: 0B             DEC     BC              
663C: 46             LD      B,(HL)          
663D: 0A             LD      A,(BC)          
663E: 14             INC     D               
663F: 1C             INC     E               
6640: 0E 1A          LD      C,$1A           
6642: 0D             DEC     C               
6643: 17             RLA                     
6644: 09             ADD     HL,BC           
6645: 12             LD      (DE),A          
6646: 1E 28          LD      E,$28           
6648: 14             INC     D               
6649: 04             INC     B               
664A: 10 5F          DJNZ    $66AB           
664C: BE             CP      (HL)            
664D: 3B             DEC     SP              
664E: 16 D3          LD      D,$D3           
6650: 93             SUB     E               
6651: 4B             LD      C,E             
6652: 7B             LD      A,E             
6653: 09             ADD     HL,BC           
6654: 9A             SBC     D               
6655: BF             CP      A               
6656: 14             INC     D               
6657: D3 B2          OUT     ($B2),A         
6659: CF             RST     0X08            
665A: 98             SBC     B               
665B: 88             ADC     A,B             
665C: 18 19          JR      $6677           
665E: 04             INC     B               
665F: 17             RLA                     
6660: 29             ADD     HL,HL           
6661: D1             POP     DE              
6662: 09             ADD     HL,BC           
6663: 15             DEC     D               
6664: 51             LD      D,C             
6665: 18 56          JR      $66BD           
6667: C2 90 73       JP      NZ,$7390        
666A: DB 83          IN      A,($83)         
666C: 1B             DEC     DE              
666D: A1             AND     C               
666E: 2F             CPL                     
666F: 49             LD      C,C             
6670: 03             INC     BC              
6671: EE 46          XOR     $46             
6673: 8B             ADC     A,E             
6674: 90             SUB     B               
6675: 5A             LD      E,D             
6676: 3F             CCF                     
6677: 08             EX      AF,AF'          
6678: 0A             LD      A,(BC)          
6679: 04             INC     B               
667A: 08             EX      AF,AF'          
667B: 49             LD      C,C             
667C: 1B             DEC     DE              
667D: 99             SBC     C               
667E: 16 14          LD      D,$14           
6680: BC             CP      H               
6681: A4             AND     H               
6682: C3 2B 09       JP      $092B           
6685: 00             NOP                     
6686: 00             NOP                     
6687: 80             ADD     A,B             
6688: 02             LD      (BC),A          
6689: 04             INC     B               
668A: 89             ADC     A,C             
668B: 67             LD      H,A             
668C: A3             AND     E               
668D: A0             AND     B               
668E: 2C             INC     L               
668F: 0B             DEC     BC              
6690: 00             NOP                     
6691: 00             NOP                     
6692: 80             ADD     A,B             
6693: 07             RLCA                    
6694: 01 93 02       LD      BC,$0293        
6697: 03             INC     BC              
6698: 23             INC     HL              
6699: 63             LD      H,E             
669A: 54             LD      D,H             
669B: 2D             DEC     L               
669C: 0D             DEC     C               
669D: 00             NOP                     
669E: 00             NOP                     
669F: 80             ADD     A,B             
66A0: 07             RLCA                    
66A1: 01 93 02       LD      BC,$0293        
66A4: 05             DEC     B               
66A5: 55             LD      D,L             
66A6: A4             AND     H               
66A7: 09             ADD     HL,BC           
66A8: B7             OR      A               
66A9: 45             LD      B,L             
66AA: 2E 0B          LD      L,$0B           
66AC: 00             NOP                     
66AD: 00             NOP                     
66AE: 80             ADD     A,B             
66AF: 07             RLCA                    
66B0: 01 93 02       LD      BC,$0293        
66B3: 03             INC     BC              
66B4: 7E             LD      A,(HL)          
66B5: 74             LD      (HL),H          
66B6: 45             LD      B,L             
66B7: 2F             CPL                     
66B8: 0E 00          LD      C,$00           
66BA: 00             NOP                     
66BB: 80             ADD     A,B             
66BC: 07             RLCA                    
66BD: 01 93 02       LD      BC,$0293        
66C0: 06 44          LD      B,$44           
66C2: 55             LD      D,L             
66C3: 06 B2          LD      B,$B2           
66C5: A3             AND     E               
66C6: A0             AND     B               
66C7: 30 09          JR      NC,$66D2        
66C9: 00             NOP                     
66CA: 00             NOP                     
66CB: 80             ADD     A,B             
66CC: 02             LD      (BC),A          
66CD: 04             INC     B               
66CE: 44             LD      B,H             
66CF: 55             LD      D,L             
66D0: 74             LD      (HL),H          
66D1: 98             SBC     B               
66D2: 31 07 88       LD      SP,$8807        
66D5: 00             NOP                     
66D6: 80             ADD     A,B             
66D7: 02             LD      (BC),A          
66D8: 02             LD      (BC),A          
66D9: 09             ADD     HL,BC           
66DA: 4F             LD      C,A             
66DB: 32 09 88       LD      ($8809),A       
66DE: 00             NOP                     
66DF: 80             ADD     A,B             
66E0: 02             LD      (BC),A          
66E1: 04             INC     B               
66E2: 3C             INC     A               
66E3: 49             LD      C,C             
66E4: 6B             LD      L,E             
66E5: A1             AND     C               
66E6: 33             INC     SP              
66E7: 0D             DEC     C               
66E8: 00             NOP                     
66E9: 00             NOP                     
66EA: 80             ADD     A,B             
66EB: 07             RLCA                    
66EC: 01 93 02       LD      BC,$0293        
66EF: 05             DEC     B               
66F0: 4E             LD      C,(HL)          
66F1: 72             LD      (HL),D          
66F2: B3             OR      E               
66F3: 8E             ADC     A,(HL)          
66F4: 59             LD      E,C             
66F5: 34             INC     (HL)            
66F6: 0A             LD      A,(BC)          
66F7: 8D             ADC     A,L             
66F8: 00             NOP                     
66F9: 80             ADD     A,B             
66FA: 02             LD      (BC),A          
66FB: 05             DEC     B               
66FC: 1B             DEC     DE              
66FD: 54             LD      D,H             
66FE: AF             XOR     A               
66FF: 91             SUB     C               
6700: 52             LD      D,D             
6701: 35             DEC     (HL)            
6702: 09             ADD     HL,BC           
6703: 91             SUB     C               
6704: 00             NOP                     
6705: 80             ADD     A,B             
6706: 02             LD      (BC),A          
6707: 04             INC     B               
6708: D7             RST     0X10            
6709: C9             RET                     
670A: 33             INC     SP              
670B: 8E             ADC     A,(HL)          
670C: 36 0E          LD      (HL),$0E        
670E: 00             NOP                     
670F: 00             NOP                     
6710: 80             ADD     A,B             
6711: 07             RLCA                    
6712: 01 93 02       LD      BC,$0293        
6715: 06 9E          LD      B,$9E           
6717: 61             LD      H,C             
6718: D0             RET     NC              
6719: B0             OR      B               
671A: 9B             SBC     E               
671B: 53             LD      D,E             
671C: 37             SCF                     
671D: 0C             INC     C               
671E: 00             NOP                     
671F: 00             NOP                     
6720: 80             ADD     A,B             
6721: 07             RLCA                    
6722: 01 93 02       LD      BC,$0293        
6725: 04             INC     B               
6726: 70             LD      (HL),B          
6727: C0             RET     NZ              
6728: 6E             LD      L,(HL)          
6729: 98             SBC     B               
672A: 38 0C          JR      C,$6738         
672C: FF             RST     0X38            
672D: 00             NOP                     
672E: 80             ADD     A,B             
672F: 07             RLCA                    
6730: 01 93 02       LD      BC,$0293        
6733: 04             INC     B               
6734: F0             RET     P               
6735: 81             ADD     A,C             
6736: BF             CP      A               
6737: 6D             LD      L,L             
6738: 39             ADD     HL,SP           
6739: 0C             INC     C               
673A: FF             RST     0X38            
673B: 00             NOP                     
673C: 80             ADD     A,B             
673D: 07             RLCA                    
673E: 01 93 02       LD      BC,$0293        
6741: 04             INC     B               
6742: EF             RST     0X28            
6743: BD             CP      L               
6744: FF             RST     0X38            
6745: A5             AND     L               
6746: 24             INC     H               
6747: 0B             DEC     BC              
6748: 9C             SBC     H               
6749: 00             NOP                     
674A: 80             ADD     A,B             
674B: 02             LD      (BC),A          
674C: 06 B4          LD      B,$B4           
674E: B7             OR      A               
674F: F0             RET     P               
6750: A4             AND     H               
6751: 0B             DEC     BC              
6752: C0             RET     NZ              
6753: 3A 31 82       LD      A,($8231)       
6756: 00             NOP                     
6757: 80             ADD     A,B             
6758: 07             RLCA                    
6759: 28 0B          JR      Z,$6766         
675B: 26 0A          LD      H,$0A           
675D: 36 01          LD      (HL),$01        
675F: 8A             ADC     A,D             
6760: 33             INC     SP              
6761: 01 8A 34       LD      BC,$348A        
6764: 01 8A 26       LD      BC,$268A        
6767: 17             RLA                     
6768: 04             INC     B               
6769: 15             DEC     D               
676A: 5F             LD      E,A             
676B: BE             CP      (HL)            
676C: 5B             LD      E,E             
676D: B1             OR      C               
676E: 4B             LD      C,E             
676F: 7B             LD      A,E             
6770: EB             EX      DE,HL           
6771: 99             SBC     C               
6772: 1B             DEC     DE              
6773: D0             RET     NC              
6774: 94             SUB     H               
6775: 14             INC     D               
6776: 30 A1          JR      NC,$6719        
6778: 16 58          LD      D,$58           
677A: DB 72          IN      A,($72)         
677C: 96             SUB     (HL)            
677D: A5             AND     L               
677E: 2E 17          LD      L,$17           
6780: 01 8A 02       LD      BC,$028A        
6783: 02             LD      (BC),A          
6784: 96             SUB     (HL)            
6785: A5             AND     L               
6786: 3B             DEC     SP              
6787: 0A             LD      A,(BC)          
6788: 00             NOP                     
6789: 00             NOP                     
678A: 80             ADD     A,B             
678B: 02             LD      (BC),A          
678C: 05             DEC     B               
678D: AB             XOR     E               
678E: 53             LD      D,E             
678F: 90             SUB     B               
6790: 8C             ADC     A,H             
6791: 47             LD      B,A             
6792: 22 39 A5       LD      ($A539),HL      
6795: 00             NOP                     
6796: 80             ADD     A,B             
6797: 02             LD      (BC),A          
6798: 04             INC     B               
6799: 4E             LD      C,(HL)          
679A: 48             LD      C,B             
679B: 23             INC     HL              
679C: 62             LD      H,D             
679D: 07             RLCA                    
679E: 2E 0D          LD      L,$0D           
67A0: 2C             INC     L               
67A1: 0A             LD      A,(BC)          
67A2: 12             LD      (DE),A          
67A3: 04             INC     B               
67A4: 28 C7          JR      Z,$676D         
67A6: DE D3          SBC     $D3             
67A8: 14             INC     D               
67A9: 90             SUB     B               
67AA: 96             SUB     (HL)            
67AB: F3             DI                      
67AC: A0             AND     B               
67AD: C8             RET     Z               
67AE: 93             SUB     E               
67AF: 56             LD      D,(HL)          
67B0: 5E             LD      E,(HL)          
67B1: DB 72          IN      A,($72)         
67B3: 4E             LD      C,(HL)          
67B4: 48             LD      C,B             
67B5: 23             INC     HL              
67B6: 62             LD      H,D             
67B7: 79             LD      A,C             
67B8: 68             LD      L,B             
67B9: 44             LD      B,H             
67BA: 90             SUB     B               
67BB: 8F             ADC     A,A             
67BC: 61             LD      H,C             
67BD: 82             ADD     A,D             
67BE: 49             LD      C,C             
67BF: D6 15          SUB     $15             
67C1: 0B             DEC     BC              
67C2: EE 0B          XOR     $0B             
67C4: BC             CP      H               
67C5: D6 B5          SUB     $B5             
67C7: 2B             DEC     HL              
67C8: A0             AND     B               
67C9: E3             EX      (SP),HL         
67CA: 72             LD      (HL),D          
67CB: 9F             SBC     A               
67CC: CD 3C 50       CALL    $503C           
67CF: 1D             DEC     E               
67D0: 00             NOP                     
67D1: 80             ADD     A,B             
67D2: 08             EX      AF,AF'          
67D3: 4B             LD      C,E             
67D4: 0B             DEC     BC              
67D5: 49             LD      C,C             
67D6: 05             DEC     B               
67D7: 7F             LD      A,A             
67D8: 1F             RRA                     
67D9: 1F             RRA                     
67DA: 1D             DEC     E               
67DB: C7             RST     0X00            
67DC: DE 9F          SBC     $9F             
67DE: 15             DEC     D               
67DF: 23             INC     HL              
67E0: 49             LD      C,C             
67E1: 5F             LD      E,A             
67E2: BE             CP      (HL)            
67E3: 03             INC     BC              
67E4: 15             DEC     D               
67E5: FB             EI                      
67E6: B9             CP      C               
67E7: B3             OR      E               
67E8: 9A             SBC     D               
67E9: B3             OR      E               
67EA: 55             LD      D,L             
67EB: 4B             LD      C,E             
67EC: 62             LD      H,D             
67ED: C3 9E 4E       JP      $4E9E           
67F0: D1             POP     DE              
67F1: 03             INC     BC              
67F2: 58             LD      E,B             
67F3: 0F             RRCA                    
67F4: 99             SBC     C               
67F5: 4D             LD      C,L             
67F6: 48             LD      C,B             
67F7: 2E F5          LD      L,$F5           
67F9: 01 0C FF       LD      BC,$FF0C        
67FC: 22 1F 20       LD      ($201F),HL      
67FF: C7             RST     0X00            
6800: DE 94          SBC     $94             
6802: 14             INC     D               
6803: 46             LD      B,(HL)          
6804: 5E             LD      E,(HL)          
6805: 35             DEC     (HL)            
6806: A1             AND     C               
6807: F3             DI                      
6808: 5F             LD      E,A             
6809: 7B             LD      A,E             
680A: 50             LD      D,B             
680B: 44             LD      B,H             
680C: 45             LD      B,L             
680D: 07             RLCA                    
680E: B2             OR      D               
680F: 96             SUB     (HL)            
6810: 64             LD      H,H             
6811: 02             LD      (BC),A          
6812: B3             OR      E               
6813: D3 78          OUT     ($78),A         
6815: 14             INC     D               
6816: 8A             ADC     A,D             
6817: D0             RET     NC              
6818: 47             LD      B,A             
6819: 5A             LD      E,D             
681A: 17             RLA                     
681B: 77             LD      (HL),A          
681C: A1             AND     C               
681D: 1B             DEC     DE              
681E: B5             OR      L     
```

## Room Descriptions

```code
RoomDescriptions:          
681F: 00             NOP                     
6820: 8B             ADC     A,E             
6821: D9             EXX                     
6822: 81             ADD     A,C             
6823: 5E             LD      E,(HL)          
6824: 00             NOP                     
6825: 03             INC     BC              
6826: 52             LD      D,D             
6827: C7             RST     0X00            
6828: DE 94          SBC     $94             
682A: 14             INC     D               
682B: 4B             LD      C,E             
682C: 5E             LD      E,(HL)          
682D: 83             ADD     A,E             
682E: 96             SUB     (HL)            
682F: 5F             LD      E,A             
6830: 17             RLA                     
6831: 46             LD      B,(HL)          
6832: 48             LD      C,B             
6833: 39             ADD     HL,SP           
6834: 17             RLA                     
6835: DB 9F          IN      A,($9F)         
6837: 56             LD      D,(HL)          
6838: D1             POP     DE              
6839: 09             ADD     HL,BC           
683A: 71             LD      (HL),C          
683B: D0             RET     NC              
683C: B0             OR      B               
683D: 7F             LD      A,A             
683E: 7B             LD      A,E             
683F: F3             DI                      
6840: 17             RLA                     
6841: 0D             DEC     C               
6842: 8D             ADC     A,L             
6843: 90             SUB     B               
6844: 14             INC     D               
6845: 08             EX      AF,AF'          
6846: 58             LD      E,B             
6847: 81             ADD     A,C             
6848: 8D             ADC     A,L             
6849: 1B             DEC     DE              
684A: B5             OR      L               
684B: 5F             LD      E,A             
684C: BE             CP      (HL)            
684D: 5B             LD      E,E             
684E: B1             OR      C               
684F: 4B             LD      C,E             
6850: 7B             LD      A,E             
6851: 55             LD      D,L             
6852: 45             LD      B,L             
6853: 8E             ADC     A,(HL)          
6854: 91             SUB     C               
6855: 11 8A F0       LD      DE,$F08A        
6858: A4             AND     H               
6859: 91             SUB     C               
685A: 7A             LD      A,D             
685B: 89             ADC     A,C             
685C: 17             RLA                     
685D: 82             ADD     A,D             
685E: 17             RLA                     
685F: 47             LD      B,A             
6860: 5E             LD      E,(HL)          
6861: 66             LD      H,(HL)          
6862: 49             LD      C,C             
6863: 90             SUB     B               
6864: 14             INC     D               
6865: 03             INC     BC              
6866: 58             LD      E,B             
6867: 3B             DEC     SP              
6868: 16 B7          LD      D,$B7           
686A: B1             OR      C               
686B: A9             XOR     C               
686C: 15             DEC     D               
686D: DB 8B          IN      A,($8B)         
686F: 83             ADD     A,E             
6870: 7A             LD      A,D             
6871: 5F             LD      E,A             
6872: BE             CP      (HL)            
6873: D7             RST     0X10            
6874: 14             INC     D               
6875: 43             LD      B,E             
6876: 7A             LD      A,D             
6877: CF             RST     0X08            
6878: 98             SBC     B               
6879: 04             INC     B               
687A: 07             RLCA                    
687B: 0B             DEC     BC              
687C: 05             DEC     B               
687D: 0A             LD      A,(BC)          
687E: 03             INC     BC              
687F: 02             LD      (BC),A          
6880: 00             NOP                     
6881: 82             ADD     A,D             
6882: 82             ADD     A,D             
6883: 80             ADD     A,B             
6884: C4 00 03       CALL    NZ,$0300        
6887: 80             ADD     A,B             
6888: AB             XOR     E               
6889: C7             RST     0X00            
688A: DE 94          SBC     $94             
688C: 14             INC     D               
688D: 4B             LD      C,E             
688E: 5E             LD      E,(HL)          
688F: 83             ADD     A,E             
6890: 96             SUB     (HL)            
6891: 3B             DEC     SP              
6892: 16 B7          LD      D,$B7           
6894: B1             OR      C               
6895: 2F             CPL                     
6896: 17             RLA                     
6897: FB             EI                      
6898: 55             LD      D,L             
6899: C7             RST     0X00            
689A: 98             SBC     B               
689B: 54             LD      D,H             
689C: 8B             ADC     A,E             
689D: 39             ADD     HL,SP           
689E: 17             RLA                     
689F: FF             RST     0X38            
68A0: 9F             SBC     A               
68A1: C0             RET     NZ              
68A2: 16 82          LD      D,$82           
68A4: 17             RLA                     
68A5: 48             LD      C,B             
68A6: 5E             LD      E,(HL)          
68A7: 81             ADD     A,C             
68A8: 8D             ADC     A,L             
68A9: 91             SUB     C               
68AA: AF             XOR     A               
68AB: 96             SUB     (HL)            
68AC: 64             LD      H,H             
68AD: DB 72          IN      A,($72)         
68AF: 95             SUB     L               
68B0: 5F             LD      E,A             
68B1: 15             DEC     D               
68B2: BC             CP      H               
68B3: FF             RST     0X38            
68B4: 78             LD      A,B             
68B5: B8             CP      B               
68B6: 16 82          LD      D,$82           
68B8: 17             RLA                     
68B9: 54             LD      D,H             
68BA: 5E             LD      E,(HL)          
68BB: 3F             CCF                     
68BC: A0             AND     B               
68BD: D5             PUSH    DE              
68BE: 15             DEC     D               
68BF: 90             SUB     B               
68C0: 14             INC     D               
68C1: D0             RET     NC              
68C2: 15             DEC     D               
68C3: F3             DI                      
68C4: BF             CP      A               
68C5: 16 53          LD      D,$53           
68C7: 51             LD      D,C             
68C8: 5E             LD      E,(HL)          
68C9: 07             RLCA                    
68CA: B2             OR      D               
68CB: BB             CP      E               
68CC: 9A             SBC     D               
68CD: 14             INC     D               
68CE: 8A             ADC     A,D             
68CF: 6B             LD      L,E             
68D0: C4 0C BA       CALL    NZ,$BA0C        
68D3: 7D             LD      A,L             
68D4: 62             LD      H,D             
68D5: 90             SUB     B               
68D6: 73             LD      (HL),E          
68D7: C4 6A 91       CALL    NZ,$916A        
68DA: 62             LD      H,D             
68DB: 30 60          JR      NC,$693D        
68DD: 82             ADD     A,D             
68DE: 17             RLA                     
68DF: 50             LD      D,B             
68E0: 5E             LD      E,(HL)          
68E1: BE             CP      (HL)            
68E2: A0             AND     B               
68E3: 03             INC     BC              
68E4: 71             LD      (HL),C          
68E5: 33             INC     SP              
68E6: 98             SBC     B               
68E7: 47             LD      B,A             
68E8: B9             CP      C               
68E9: 53             LD      D,E             
68EA: BE             CP      (HL)            
68EB: 0E D0          LD      C,$D0           
68ED: 2F             CPL                     
68EE: 8E             ADC     A,(HL)          
68EF: D0             RET     NC              
68F0: 15             DEC     D               
68F1: 82             ADD     A,D             
68F2: 17             RLA                     
68F3: 47             LD      B,A             
68F4: 5E             LD      E,(HL)          
68F5: 66             LD      H,(HL)          
68F6: 49             LD      C,C             
68F7: F3             DI                      
68F8: 17             RLA                     
68F9: F3             DI                      
68FA: 8C             ADC     A,H             
68FB: 4B             LD      C,E             
68FC: 7B             LD      A,E             
68FD: 4A             LD      C,D             
68FE: 45             LD      B,L             
68FF: 77             LD      (HL),A          
6900: C4 D3 14       CALL    NZ,$14D3        
6903: 0F             RRCA                    
6904: B4             OR      H               
6905: 19             ADD     HL,DE           
6906: 58             LD      E,B             
6907: 36 A0          LD      (HL),$A0        
6909: 83             ADD     A,E             
690A: 61             LD      H,C             
690B: 81             ADD     A,C             
690C: 5B             LD      E,E             
690D: 1B             DEC     DE              
690E: B5             OR      L               
690F: 6B             LD      L,E             
6910: BF             CP      A               
6911: 5F             LD      E,A             
6912: BE             CP      (HL)            
6913: 61             LD      H,C             
6914: 17             RLA                     
6915: 82             ADD     A,D             
6916: C6 03          ADD     $03             
6918: EE 5F          XOR     $5F             
691A: 17             RLA                     
691B: 46             LD      B,(HL)          
691C: 48             LD      C,B             
691D: A9             XOR     C               
691E: 15             DEC     D               
691F: DB 8B          IN      A,($8B)         
6921: E3             EX      (SP),HL         
6922: 8B             ADC     A,E             
6923: 0B             DEC     BC              
6924: 5C             LD      E,H             
6925: 6B             LD      L,E             
6926: BF             CP      A               
6927: 46             LD      B,(HL)          
6928: 45             LD      B,L             
6929: 35             DEC     (HL)            
692A: 49             LD      C,C             
692B: DB 16          IN      A,($16)         
692D: D3 B9          OUT     ($B9),A         
692F: 9B             SBC     E               
6930: 6C             LD      L,H             
6931: 1B             DEC     DE              
6932: D0             RET     NC              
6933: 2E 04          LD      L,$04           
6935: 13             INC     DE              
6936: 0B             DEC     BC              
6937: 11 0A 04       LD      DE,$040A        
693A: 02             LD      (BC),A          
693B: 00             NOP                     
693C: 81             ADD     A,C             
693D: 02             LD      (BC),A          
693E: 02             LD      (BC),A          
693F: 00             NOP                     
6940: 83             ADD     A,E             
6941: 03             INC     BC              
6942: 06 0D          LD      B,$0D           
6944: 04             INC     B               
6945: 20 1D          JR      NZ,$6964        
6947: 8B             ADC     A,E             
6948: 81             ADD     A,C             
6949: 83             ADD     A,E             
694A: 3A 00 03       LD      A,($0300)       
694D: 2A C7 DE       LD      HL,($DEC7)      
6950: 94             SUB     H               
6951: 14             INC     D               
6952: 4B             LD      C,E             
6953: 5E             LD      E,(HL)          
6954: 83             ADD     A,E             
6955: 96             SUB     (HL)            
6956: FB             EI                      
6957: 14             INC     D               
6958: 4B             LD      C,E             
6959: B2             OR      D               
695A: 55             LD      D,L             
695B: A4             AND     H               
695C: 09             ADD     HL,BC           
695D: B7             OR      A               
695E: 59             LD      E,C             
695F: 5E             LD      E,(HL)          
6960: 3B             DEC     SP              
6961: 4A             LD      C,D             
6962: 23             INC     HL              
6963: D1             POP     DE              
6964: 13             INC     DE              
6965: 54             LD      D,H             
6966: C9             RET                     
6967: B8             CP      B               
6968: F5             PUSH    AF              
6969: A4             AND     H               
696A: B2             OR      D               
696B: 17             RLA                     
696C: 90             SUB     B               
696D: 14             INC     D               
696E: 16 58          LD      D,$58           
6970: D6 9C          SUB     $9C             
6972: DB 72          IN      A,($72)         
6974: 47             LD      B,A             
6975: B9             CP      C               
6976: 77             LD      (HL),A          
6977: BE             CP      (HL)            
6978: 04             INC     B               
6979: 0B             DEC     BC              
697A: 0B             DEC     BC              
697B: 09             ADD     HL,BC           
697C: 0A             LD      A,(BC)          
697D: 01 02 00       LD      BC,$0002        
6980: 82             ADD     A,D             
6981: 02             LD      (BC),A          
6982: 02             LD      (BC),A          
6983: 00             NOP                     
6984: 84             ADD     A,H             
6985: 84             ADD     A,H             
6986: 67             LD      H,A             
6987: 00             NOP                     
6988: 03             INC     BC              
6989: 53             LD      D,E             
698A: C7             RST     0X00            
698B: DE 94          SBC     $94             
698D: 14             INC     D               
698E: 43             LD      B,E             
698F: 5E             LD      E,(HL)          
6990: 16 BC          LD      D,$BC           
6992: DB 72          IN      A,($72)         
6994: 82             ADD     A,D             
6995: BF             CP      A               
6996: B8             CP      B               
6997: 16 7B          LD      D,$7B           
6999: 14             INC     D               
699A: 55             LD      D,L             
699B: A4             AND     H               
699C: 09             ADD     HL,BC           
699D: B7             OR      A               
699E: 59             LD      E,C             
699F: 5E             LD      E,(HL)          
69A0: 85             ADD     A,L             
69A1: 73             LD      (HL),E          
69A2: 15             DEC     D               
69A3: 71             LD      (HL),C          
69A4: 82             ADD     A,D             
69A5: 8D             ADC     A,L             
69A6: 4B             LD      C,E             
69A7: 62             LD      H,D             
69A8: 89             ADC     A,C             
69A9: 5B             LD      E,E             
69AA: 83             ADD     A,E             
69AB: 96             SUB     (HL)            
69AC: 33             INC     SP              
69AD: 98             SBC     B               
69AE: 6B             LD      L,E             
69AF: BF             CP      A               
69B0: 5F             LD      E,A             
69B1: BE             CP      (HL)            
69B2: 99             SBC     C               
69B3: 16 C2          LD      D,$C2           
69B5: B3             OR      E               
69B6: 56             LD      D,(HL)          
69B7: F4 F4 72       CALL    P,$72F4         
69BA: 4B             LD      C,E             
69BB: 5E             LD      E,(HL)          
69BC: C3 B5 E1       JP      $E1B5           
69BF: 14             INC     D               
69C0: 73             LD      (HL),E          
69C1: B3             OR      E               
69C2: 84             ADD     A,H             
69C3: 5B             LD      E,E             
69C4: 89             ADC     A,C             
69C5: 17             RLA                     
69C6: 82             ADD     A,D             
69C7: 17             RLA                     
69C8: 47             LD      B,A             
69C9: 5E             LD      E,(HL)          
69CA: 66             LD      H,(HL)          
69CB: 49             LD      C,C             
69CC: 90             SUB     B               
69CD: 14             INC     D               
69CE: 03             INC     BC              
69CF: 58             LD      E,B             
69D0: 06 9A          LD      B,$9A           
69D2: F4 72 89       CALL    P,$8972         
69D5: 17             RLA                     
69D6: 82             ADD     A,D             
69D7: 17             RLA                     
69D8: 59             LD      E,C             
69D9: 5E             LD      E,(HL)          
69DA: 66             LD      H,(HL)          
69DB: 62             LD      H,D             
69DC: 2E 04          LD      L,$04           
69DE: 0F             RRCA                    
69DF: 0B             DEC     BC              
69E0: 0D             DEC     C               
69E1: 0A             LD      A,(BC)          
69E2: 01 02 00       LD      BC,$0002        
69E5: 83             ADD     A,E             
69E6: 04             INC     B               
69E7: 02             LD      (BC),A          
69E8: 00             NOP                     
69E9: A1             AND     C               
69EA: 03             INC     BC              
69EB: 02             LD      (BC),A          
69EC: 00             NOP                     
69ED: 85             ADD     A,L             
69EE: 85             ADD     A,L             
69EF: 44             LD      B,H             
69F0: 00             NOP                     
69F1: 03             INC     BC              
69F2: 26 63          LD      H,$63           
69F4: BE             CP      (HL)            
69F5: CB B5          RES     6,L             
69F7: C3 B5 73       JP      $73B5           
69FA: 17             RLA                     
69FB: 1B             DEC     DE              
69FC: B8             CP      B               
69FD: E6 A4          AND     $A4             
69FF: 39             ADD     HL,SP           
6A00: 17             RLA                     
6A01: DB 9F          IN      A,($9F)         
6A03: 56             LD      D,(HL)          
6A04: D1             POP     DE              
6A05: 07             RLCA                    
6A06: 71             LD      (HL),C          
6A07: 96             SUB     (HL)            
6A08: D7             RST     0X10            
6A09: C7             RST     0X00            
6A0A: B5             OR      L               
6A0B: 66             LD      H,(HL)          
6A0C: 49             LD      C,C             
6A0D: 15             DEC     D               
6A0E: EE 36          XOR     $36             
6A10: A1             AND     C               
6A11: 73             LD      (HL),E          
6A12: 76             HALT                    
6A13: 8E             ADC     A,(HL)          
6A14: 48             LD      C,B             
6A15: F7             RST     0X30            
6A16: 17             RLA                     
6A17: 17             RLA                     
6A18: BA             CP      D               
6A19: 04             INC     B               
6A1A: 19             ADD     HL,DE           
6A1B: 0B             DEC     BC              
6A1C: 17             RLA                     
6A1D: 0A             LD      A,(BC)          
6A1E: 04             INC     B               
6A1F: 02             LD      (BC),A          
6A20: 00             NOP                     
6A21: 84             ADD     A,H             
6A22: 02             LD      (BC),A          
6A23: 02             LD      (BC),A          
6A24: 00             NOP                     
6A25: 86             ADD     A,(HL)          
6A26: 03             INC     BC              
6A27: 0C             INC     C               
6A28: 0D             DEC     C               
6A29: 0A             LD      A,(BC)          
6A2A: 00             NOP                     
6A2B: 88             ADC     A,B             
6A2C: 14             INC     D               
6A2D: 0D             DEC     C               
6A2E: 05             DEC     B               
6A2F: 20 1D          JR      NZ,$6A4E        
6A31: 01 07 82       LD      BC,$8207        
6A34: 86             ADD     A,(HL)          
6A35: 3F             CCF                     
6A36: 00             NOP                     
6A37: 03             INC     BC              
6A38: 2F             CPL                     
6A39: C7             RST     0X00            
6A3A: DE 94          SBC     $94             
6A3C: 14             INC     D               
6A3D: 4B             LD      C,E             
6A3E: 5E             LD      E,(HL)          
6A3F: 83             ADD     A,E             
6A40: 96             SUB     (HL)            
6A41: 39             ADD     HL,SP           
6A42: 17             RLA                     
6A43: DB 9F          IN      A,($9F)         
6A45: 56             LD      D,(HL)          
6A46: D1             POP     DE              
6A47: 09             ADD     HL,BC           
6A48: 71             LD      (HL),C          
6A49: DB B0          IN      A,($B0)         
6A4B: 66             LD      H,(HL)          
6A4C: 17             RLA                     
6A4D: 0F             RRCA                    
6A4E: A0             AND     B               
6A4F: F3             DI                      
6A50: 17             RLA                     
6A51: 0D             DEC     C               
6A52: 8D             ADC     A,L             
6A53: 52             LD      D,D             
6A54: F4 65 49       CALL    P,$4965         
6A57: 77             LD      (HL),A          
6A58: 47             LD      B,A             
6A59: CE B5          ADC     $B5             
6A5B: 86             ADD     A,(HL)          
6A5C: 5F             LD      E,A             
6A5D: 99             SBC     C               
6A5E: 16 C2          LD      D,$C2           
6A60: B3             OR      E               
6A61: 90             SUB     B               
6A62: 14             INC     D               
6A63: 07             RLCA                    
6A64: 58             LD      E,B             
6A65: 66             LD      H,(HL)          
6A66: 49             LD      C,C             
6A67: 2E 04          LD      L,$04           
6A69: 0B             DEC     BC              
6A6A: 0B             DEC     BC              
6A6B: 09             ADD     HL,BC           
6A6C: 0A             LD      A,(BC)          
6A6D: 01 02 00       LD      BC,$0002        
6A70: 85             ADD     A,L             
6A71: 03             INC     BC              
6A72: 02             LD      (BC),A          
6A73: 00             NOP                     
6A74: 87             ADD     A,A             
6A75: 87             ADD     A,A             
6A76: 44             LD      B,H             
6A77: 00             NOP                     
6A78: 03             INC     BC              
6A79: 2F             CPL                     
6A7A: 63             LD      H,E             
6A7B: BE             CP      (HL)            
6A7C: CB B5          RES     6,L             
6A7E: C3 B5 39       JP      $39B5           
6A81: 17             RLA                     
6A82: 8E             ADC     A,(HL)          
6A83: C5             PUSH    BC              
6A84: 39             ADD     HL,SP           
6A85: 17             RLA                     
6A86: DB 9F          IN      A,($9F)         
6A88: 56             LD      D,(HL)          
6A89: D1             POP     DE              
6A8A: 0A             LD      A,(BC)          
6A8B: 71             LD      (HL),C          
6A8C: 7A             LD      A,D             
6A8D: 79             LD      A,C             
6A8E: F3             DI                      
6A8F: 17             RLA                     
6A90: 0D             DEC     C               
6A91: 8D             ADC     A,L             
6A92: 56             LD      D,(HL)          
6A93: F4 DB 72       CALL    P,$72DB         
6A96: 16 A0          LD      D,$A0           
6A98: 51             LD      D,C             
6A99: DB F0          IN      A,($F0)         
6A9B: A4             AND     H               
6A9C: 91             SUB     C               
6A9D: 7A             LD      A,D             
6A9E: D5             PUSH    DE              
6A9F: 15             DEC     D               
6AA0: 89             ADC     A,C             
6AA1: 17             RLA                     
6AA2: 82             ADD     A,D             
6AA3: 17             RLA                     
6AA4: 59             LD      E,C             
6AA5: 5E             LD      E,(HL)          
6AA6: 66             LD      H,(HL)          
6AA7: 62             LD      H,D             
6AA8: 2E 04          LD      L,$04           
6AAA: 10 0B          DJNZ    $6AB7           
6AAC: 0E 0A          LD      C,$0A           
6AAE: 05             DEC     B               
6AAF: 07             RLCA                    
6AB0: 0D             DEC     C               
6AB1: 05             DEC     B               
6AB2: 08             EX      AF,AF'          
6AB3: 08             EX      AF,AF'          
6AB4: 19             ADD     HL,DE           
6AB5: 8C             ADC     A,H             
6AB6: 0C             INC     C               
6AB7: 04             INC     B               
6AB8: 02             LD      (BC),A          
6AB9: 00             NOP                     
6ABA: 86             ADD     A,(HL)          
6ABB: 88             ADC     A,B             
6ABC: 79             LD      A,C             
6ABD: 00             NOP                     
6ABE: 03             INC     BC              
6ABF: 57             LD      D,A             
6AC0: C7             RST     0X00            
6AC1: DE 94          SBC     $94             
6AC3: 14             INC     D               
6AC4: 4B             LD      C,E             
6AC5: 5E             LD      E,(HL)          
6AC6: 83             ADD     A,E             
6AC7: 96             SUB     (HL)            
6AC8: 8C             ADC     A,H             
6AC9: 17             RLA                     
6ACA: 90             SUB     B               
6ACB: 78             LD      A,B             
6ACC: 2E 6F          LD      L,$6F           
6ACE: 23             INC     HL              
6ACF: 49             LD      C,C             
6AD0: 01 B3 59       LD      BC,$59B3        
6AD3: 90             SUB     B               
6AD4: 82             ADD     A,D             
6AD5: 7B             LD      A,E             
6AD6: C2 16 93       JP      NZ,$9316        
6AD9: 61             LD      H,C             
6ADA: C5             PUSH    BC              
6ADB: 98             SBC     B               
6ADC: D0             RET     NC              
6ADD: 15             DEC     D               
6ADE: 82             ADD     A,D             
6ADF: 17             RLA                     
6AE0: 47             LD      B,A             
6AE1: 5E             LD      E,(HL)          
6AE2: 66             LD      H,(HL)          
6AE3: 49             LD      C,C             
6AE4: 90             SUB     B               
6AE5: 14             INC     D               
6AE6: 19             ADD     HL,DE           
6AE7: 58             LD      E,B             
6AE8: 66             LD      H,(HL)          
6AE9: 62             LD      H,D             
6AEA: E1             POP     HL              
6AEB: 14             INC     D               
6AEC: CF             RST     0X08            
6AED: B2             OR      D               
6AEE: AF             XOR     A               
6AEF: B3             OR      E               
6AF0: 82             ADD     A,D             
6AF1: 17             RLA                     
6AF2: 2F             CPL                     
6AF3: 62             LD      H,D             
6AF4: D5             PUSH    DE              
6AF5: 15             DEC     D               
6AF6: 7B             LD      A,E             
6AF7: 14             INC     D               
6AF8: FB             EI                      
6AF9: B9             CP      C               
6AFA: 67             LD      H,A             
6AFB: C0             RET     NZ              
6AFC: D0             RET     NC              
6AFD: 15             DEC     D               
6AFE: 82             ADD     A,D             
6AFF: 17             RLA                     
6B00: 55             LD      D,L             
6B01: 5E             LD      E,(HL)          
6B02: 36 A1          LD      (HL),$A1        
6B04: 05             DEC     B               
6B05: 71             LD      (HL),C          
6B06: B8             CP      B               
6B07: A0             AND     B               
6B08: 23             INC     HL              
6B09: 62             LD      H,D             
6B0A: 56             LD      D,(HL)          
6B0B: D1             POP     DE              
6B0C: 04             INC     B               
6B0D: 71             LD      (HL),C          
6B0E: 6B             LD      L,E             
6B0F: A1             AND     C               
6B10: 8E             ADC     A,(HL)          
6B11: 48             LD      C,B             
6B12: 94             SUB     H               
6B13: 14             INC     D               
6B14: 09             ADD     HL,BC           
6B15: B3             OR      E               
6B16: 2E 04          LD      L,$04           
6B18: 1D             DEC     E               
6B19: 0B             DEC     BC              
6B1A: 1B             DEC     DE              
6B1B: 0A             LD      A,(BC)          
6B1C: 04             INC     B               
6B1D: 0B             DEC     BC              
6B1E: 0E 09          LD      C,$09           
6B20: 0D             DEC     C               
6B21: 05             DEC     B               
6B22: 20 1D          JR      NZ,$6B41        
6B24: 01 07 82       LD      BC,$8207        
6B27: 00             NOP                     
6B28: 85             ADD     A,L             
6B29: 03             INC     BC              
6B2A: 0B             DEC     BC              
6B2B: 0E 09          LD      C,$09           
6B2D: 0D             DEC     C               
6B2E: 05             DEC     B               
6B2F: 20 1D          JR      NZ,$6B4E        
6B31: 01 06 82       LD      BC,$8206        
6B34: 00             NOP                     
6B35: 89             ADC     A,C             
6B36: 89             ADC     A,C             
6B37: 5D             LD      E,L             
6B38: 00             NOP                     
6B39: 03             INC     BC              
6B3A: 3F             CCF                     
6B3B: C7             RST     0X00            
6B3C: DE 94          SBC     $94             
6B3E: 14             INC     D               
6B3F: 43             LD      B,E             
6B40: 5E             LD      E,(HL)          
6B41: 16 BC          LD      D,$BC           
6B43: DB 72          IN      A,($72)         
6B45: 47             LD      B,A             
6B46: B9             CP      C               
6B47: 53             LD      D,E             
6B48: BE             CP      (HL)            
6B49: 8E             ADC     A,(HL)          
6B4A: 61             LD      H,C             
6B4B: B8             CP      B               
6B4C: 16 82          LD      D,$82           
6B4E: 17             RLA                     
6B4F: 49             LD      C,C             
6B50: 5E             LD      E,(HL)          
6B51: 63             LD      H,E             
6B52: B1             OR      C               
6B53: 05             DEC     B               
6B54: BC             CP      H               
6B55: 9E             SBC     (HL)            
6B56: 61             LD      H,C             
6B57: CE B0          ADC     $B0             
6B59: 9B             SBC     E               
6B5A: 15             DEC     D               
6B5B: 11 8D 5F       LD      DE,$5F8D        
6B5E: 4A             LD      C,D             
6B5F: 3A 15 8D       LD      A,($8D15)       
6B62: 7B             LD      A,E             
6B63: 3A 15 66       LD      A,($6615)       
6B66: 7B             LD      A,E             
6B67: D0             RET     NC              
6B68: 15             DEC     D               
6B69: 82             ADD     A,D             
6B6A: 17             RLA                     
6B6B: 47             LD      B,A             
6B6C: 5E             LD      E,(HL)          
6B6D: 66             LD      H,(HL)          
6B6E: 49             LD      C,C             
6B6F: 90             SUB     B               
6B70: 14             INC     D               
6B71: 19             ADD     HL,DE           
6B72: 58             LD      E,B             
6B73: 66             LD      H,(HL)          
6B74: 62             LD      H,D             
6B75: F3             DI                      
6B76: 17             RLA                     
6B77: 0D             DEC     C               
6B78: 8D             ADC     A,L             
6B79: 2E 04          LD      L,$04           
6B7B: 19             ADD     HL,DE           
6B7C: 0B             DEC     BC              
6B7D: 17             RLA                     
6B7E: 0A             LD      A,(BC)          
6B7F: 04             INC     B               
6B80: 0C             INC     C               
6B81: 0D             DEC     C               
6B82: 0A             LD      A,(BC)          
6B83: 00             NOP                     
6B84: 88             ADC     A,B             
6B85: 14             INC     D               
6B86: 0D             DEC     C               
6B87: 05             DEC     B               
6B88: 20 1D          JR      NZ,$6BA7        
6B8A: 01 06 82       LD      BC,$8206        
6B8D: 01 02 00       LD      BC,$0002        
6B90: 90             SUB     B               
6B91: 03             INC     BC              
6B92: 02             LD      (BC),A          
6B93: 00             NOP                     
6B94: 8A             ADC     A,D             
6B95: 8A             ADC     A,D             
6B96: 3A 00 03       LD      A,($0300)       
6B99: 26 63          LD      H,$63           
6B9B: BE             CP      (HL)            
6B9C: CB B5          RES     6,L             
6B9E: C3 B5 73       JP      $73B5           
6BA1: 17             RLA                     
6BA2: 1B             DEC     DE              
6BA3: B8             CP      B               
6BA4: E6 A4          AND     $A4             
6BA6: 39             ADD     HL,SP           
6BA7: 17             RLA                     
6BA8: DB 9F          IN      A,($9F)         
6BAA: 56             LD      D,(HL)          
6BAB: D1             POP     DE              
6BAC: 07             RLCA                    
6BAD: 71             LD      (HL),C          
6BAE: 96             SUB     (HL)            
6BAF: D7             RST     0X10            
6BB0: C7             RST     0X00            
6BB1: B5             OR      L               
6BB2: 66             LD      H,(HL)          
6BB3: 49             LD      C,C             
6BB4: 15             DEC     D               
6BB5: EE 36          XOR     $36             
6BB7: A1             AND     C               
6BB8: 73             LD      (HL),E          
6BB9: 76             HALT                    
6BBA: 8E             ADC     A,(HL)          
6BBB: 48             LD      C,B             
6BBC: F7             RST     0X30            
6BBD: 17             RLA                     
6BBE: 17             RLA                     
6BBF: BA             CP      D               
6BC0: 04             INC     B               
6BC1: 0F             RRCA                    
6BC2: 0B             DEC     BC              
6BC3: 0D             DEC     C               
6BC4: 0A             LD      A,(BC)          
6BC5: 04             INC     B               
6BC6: 02             LD      (BC),A          
6BC7: 00             NOP                     
6BC8: 89             ADC     A,C             
6BC9: 02             LD      (BC),A          
6BCA: 02             LD      (BC),A          
6BCB: 00             NOP                     
6BCC: 8B             ADC     A,E             
6BCD: 03             INC     BC              
6BCE: 02             LD      (BC),A          
6BCF: 00             NOP                     
6BD0: 8D             ADC     A,L             
6BD1: 8B             ADC     A,E             
6BD2: 3F             CCF                     
6BD3: 00             NOP                     
6BD4: 03             INC     BC              
6BD5: 2F             CPL                     
6BD6: C7             RST     0X00            
6BD7: DE 94          SBC     $94             
6BD9: 14             INC     D               
6BDA: 4B             LD      C,E             
6BDB: 5E             LD      E,(HL)          
6BDC: 83             ADD     A,E             
6BDD: 96             SUB     (HL)            
6BDE: 39             ADD     HL,SP           
6BDF: 17             RLA                     
6BE0: DB 9F          IN      A,($9F)         
6BE2: 56             LD      D,(HL)          
6BE3: D1             POP     DE              
6BE4: 09             ADD     HL,BC           
6BE5: 71             LD      (HL),C          
6BE6: 7B             LD      A,E             
6BE7: B1             OR      C               
6BE8: 66             LD      H,(HL)          
6BE9: 17             RLA                     
6BEA: 0F             RRCA                    
6BEB: A0             AND     B               
6BEC: F3             DI                      
6BED: 17             RLA                     
6BEE: 0D             DEC     C               
6BEF: 8D             ADC     A,L             
6BF0: 52             LD      D,D             
6BF1: F4 65 49       CALL    P,$4965         
6BF4: 77             LD      (HL),A          
6BF5: 47             LD      B,A             
6BF6: CE B5          ADC     $B5             
6BF8: 86             ADD     A,(HL)          
6BF9: 5F             LD      E,A             
6BFA: 99             SBC     C               
6BFB: 16 C2          LD      D,$C2           
6BFD: B3             OR      E               
6BFE: 90             SUB     B               
6BFF: 14             INC     D               
6C00: 07             RLCA                    
6C01: 58             LD      E,B             
6C02: 66             LD      H,(HL)          
6C03: 49             LD      C,C             
6C04: 2E 04          LD      L,$04           
6C06: 0B             DEC     BC              
6C07: 0B             DEC     BC              
6C08: 09             ADD     HL,BC           
6C09: 0A             LD      A,(BC)          
6C0A: 01 02 00       LD      BC,$0002        
6C0D: 8A             ADC     A,D             
6C0E: 03             INC     BC              
6C0F: 02             LD      (BC),A          
6C10: 00             NOP                     
6C11: 8C             ADC     A,H             
6C12: 8C             ADC     A,H             
6C13: 44             LD      B,H             
6C14: 00             NOP                     
6C15: 03             INC     BC              
6C16: 2F             CPL                     
6C17: 63             LD      H,E             
6C18: BE             CP      (HL)            
6C19: CB B5          RES     6,L             
6C1B: C3 B5 39       JP      $39B5           
6C1E: 17             RLA                     
6C1F: 8E             ADC     A,(HL)          
6C20: C5             PUSH    BC              
6C21: 39             ADD     HL,SP           
6C22: 17             RLA                     
6C23: DB 9F          IN      A,($9F)         
6C25: 56             LD      D,(HL)          
6C26: D1             POP     DE              
6C27: 0A             LD      A,(BC)          
6C28: 71             LD      (HL),C          
6C29: 7A             LD      A,D             
6C2A: 79             LD      A,C             
6C2B: F3             DI                      
6C2C: 17             RLA                     
6C2D: 0D             DEC     C               
6C2E: 8D             ADC     A,L             
6C2F: 56             LD      D,(HL)          
6C30: F4 DB 72       CALL    P,$72DB         
6C33: 16 A0          LD      D,$A0           
6C35: 51             LD      D,C             
6C36: DB F0          IN      A,($F0)         
6C38: A4             AND     H               
6C39: 91             SUB     C               
6C3A: 7A             LD      A,D             
6C3B: D5             PUSH    DE              
6C3C: 15             DEC     D               
6C3D: 89             ADC     A,C             
6C3E: 17             RLA                     
6C3F: 82             ADD     A,D             
6C40: 17             RLA                     
6C41: 59             LD      E,C             
6C42: 5E             LD      E,(HL)          
6C43: 66             LD      H,(HL)          
6C44: 62             LD      H,D             
6C45: 2E 04          LD      L,$04           
6C47: 10 0B          DJNZ    $6C54           
6C49: 0E 0A          LD      C,$0A           
6C4B: 05             DEC     B               
6C4C: 07             RLCA                    
6C4D: 0D             DEC     C               
6C4E: 05             DEC     B               
6C4F: 08             EX      AF,AF'          
6C50: 08             EX      AF,AF'          
6C51: 19             ADD     HL,DE           
6C52: 87             ADD     A,A             
6C53: 0C             INC     C               
6C54: 04             INC     B               
6C55: 02             LD      (BC),A          
6C56: 00             NOP                     
6C57: 8B             ADC     A,E             
6C58: 8D             ADC     A,L             
6C59: 4D             LD      C,L             
6C5A: 00             NOP                     
6C5B: 03             INC     BC              
6C5C: 3D             DEC     A               
6C5D: C7             RST     0X00            
6C5E: DE 94          SBC     $94             
6C60: 14             INC     D               
6C61: 4B             LD      C,E             
6C62: 5E             LD      E,(HL)          
6C63: 83             ADD     A,E             
6C64: 96             SUB     (HL)            
6C65: DF             RST     0X18            
6C66: 16 96          LD      D,$96           
6C68: BE             CP      (HL)            
6C69: 45             LD      B,L             
6C6A: 5E             LD      E,(HL)          
6C6B: 4F             LD      C,A             
6C6C: 72             LD      (HL),D          
6C6D: 74             LD      (HL),H          
6C6E: 4D             LD      C,L             
6C6F: 56             LD      D,(HL)          
6C70: F4 F4 72       CALL    P,$72F4         
6C73: 4B             LD      C,E             
6C74: 5E             LD      E,(HL)          
6C75: C3 B5 3B       JP      $3BB5           
6C78: 16 B7          LD      D,$B7           
6C7A: B1             OR      C               
6C7B: 94             SUB     H               
6C7C: AF             XOR     A               
6C7D: 3F             CCF                     
6C7E: A0             AND     B               
6C7F: 89             ADC     A,C             
6C80: 17             RLA                     
6C81: 82             ADD     A,D             
6C82: 17             RLA                     
6C83: 50             LD      D,B             
6C84: 5E             LD      E,(HL)          
6C85: BE             CP      (HL)            
6C86: A0             AND     B               
6C87: 03             INC     BC              
6C88: 71             LD      (HL),C          
6C89: 33             INC     SP              
6C8A: 98             SBC     B               
6C8B: 52             LD      D,D             
6C8C: 45             LD      B,L             
6C8D: 65             LD      H,L             
6C8E: 49             LD      C,C             
6C8F: 77             LD      (HL),A          
6C90: 47             LD      B,A             
6C91: 89             ADC     A,C             
6C92: 17             RLA                     
6C93: 82             ADD     A,D             
6C94: 17             RLA                     
6C95: 59             LD      E,C             
6C96: 5E             LD      E,(HL)          
6C97: 66             LD      H,(HL)          
6C98: 62             LD      H,D             
6C99: 2E 04          LD      L,$04           
6C9B: 0B             DEC     BC              
6C9C: 0B             DEC     BC              
6C9D: 09             ADD     HL,BC           
6C9E: 0A             LD      A,(BC)          
6C9F: 04             INC     B               
6CA0: 02             LD      (BC),A          
6CA1: 00             NOP                     
6CA2: 8A             ADC     A,D             
6CA3: 01 02 00       LD      BC,$0002        
6CA6: 8E             ADC     A,(HL)          
6CA7: 8E             ADC     A,(HL)          
6CA8: 80             ADD     A,B             
6CA9: A2             AND     D               
6CAA: 00             NOP                     
6CAB: 03             INC     BC              
6CAC: 3B             DEC     SP              
6CAD: C7             RST     0X00            
6CAE: DE 94          SBC     $94             
6CB0: 14             INC     D               
6CB1: 4B             LD      C,E             
6CB2: 5E             LD      E,(HL)          
6CB3: 83             ADD     A,E             
6CB4: 96             SUB     (HL)            
6CB5: 3B             DEC     SP              
6CB6: 16 B7          LD      D,$B7           
6CB8: B1             OR      C               
6CB9: 39             ADD     HL,SP           
6CBA: 17             RLA                     
6CBB: DB 9F          IN      A,($9F)         
6CBD: 23             INC     HL              
6CBE: D1             POP     DE              
6CBF: 13             INC     DE              
6CC0: 54             LD      D,H             
6CC1: E7             RST     0X20            
6CC2: B8             CP      B               
6CC3: 0D             DEC     C               
6CC4: 8D             ADC     A,L             
6CC5: B8             CP      B               
6CC6: 16 FF          LD      D,$FF           
6CC8: 14             INC     D               
6CC9: 1B             DEC     DE              
6CCA: 53             LD      D,E             
6CCB: 91             SUB     C               
6CCC: 7A             LD      A,D             
6CCD: 56             LD      D,(HL)          
6CCE: 15             DEC     D               
6CCF: 5A             LD      E,D             
6CD0: 62             LD      H,D             
6CD1: 56             LD      D,(HL)          
6CD2: F4 F4 72       CALL    P,$72F4         
6CD5: 43             LD      B,E             
6CD6: 5E             LD      E,(HL)          
6CD7: 5B             LD      E,E             
6CD8: B1             OR      C               
6CD9: 23             INC     HL              
6CDA: 63             LD      H,E             
6CDB: 0B             DEC     BC              
6CDC: C0             RET     NZ              
6CDD: 04             INC     B               
6CDE: 9A             SBC     D               
6CDF: 53             LD      D,E             
6CE0: BE             CP      (HL)            
6CE1: 8E             ADC     A,(HL)          
6CE2: 48             LD      C,B             
6CE3: 61             LD      H,C             
6CE4: 17             RLA                     
6CE5: 82             ADD     A,D             
6CE6: C6 2E          ADD     $2E             
6CE8: 04             INC     B               
6CE9: 62             LD      H,D             
6CEA: 0B             DEC     BC              
6CEB: 60             LD      H,B             
6CEC: 0A             LD      A,(BC)          
6CED: 02             LD      (BC),A          
6CEE: 02             LD      (BC),A          
6CEF: 00             NOP                     
6CF0: 8D             ADC     A,L             
6CF1: 01 59 0E       LD      BC,$0E59        
6CF4: 57             LD      D,A             
6CF5: 0D             DEC     C               
6CF6: 1D             DEC     E               
6CF7: 01 1E 20       LD      BC,$201E        
6CFA: 1D             DEC     E               
6CFB: 04             INC     B               
6CFC: 17             RLA                     
6CFD: 5F             LD      E,A             
6CFE: BE             CP      (HL)            
6CFF: 73             LD      (HL),E          
6D00: 15             DEC     D               
6D01: C1             POP     BC              
6D02: B1             OR      C               
6D03: 3F             CCF                     
6D04: DE B6          SBC     $B6             
6D06: 14             INC     D               
6D07: 5D             LD      E,L             
6D08: 9E             SBC     (HL)            
6D09: D6 B5          SUB     $B5             
6D0B: DB 72          IN      A,($72)         
6D0D: 1B             DEC     DE              
6D0E: D0             RET     NC              
6D0F: 99             SBC     C               
6D10: 16 C2          LD      D,$C2           
6D12: B3             OR      E               
6D13: 2E 0D          LD      L,$0D           
6D15: 34             INC     (HL)            
6D16: 20 1D          JR      NZ,$6D35        
6D18: 01 0A 17       LD      BC,$170A        
6D1B: 0A             LD      A,(BC)          
6D1C: 00             NOP                     
6D1D: 17             RLA                     
6D1E: 1E 8E          LD      E,$8E           
6D20: 04             INC     B               
6D21: 28 5F          JR      Z,$6D82         
6D23: BE             CP      (HL)            
6D24: 73             LD      (HL),E          
6D25: 15             DEC     D               
6D26: C1             POP     BC              
6D27: B1             OR      C               
6D28: 3F             CCF                     
6D29: DE E1          SBC     $E1             
6D2B: 14             INC     D               
6D2C: 35             DEC     (HL)            
6D2D: 92             SUB     D               
6D2E: 89             ADC     A,C             
6D2F: 17             RLA                     
6D30: 43             LD      B,E             
6D31: 16 5B          LD      D,$5B           
6D33: 66             LD      H,(HL)          
6D34: 8E             ADC     A,(HL)          
6D35: 48             LD      C,B             
6D36: FF             RST     0X38            
6D37: 15             DEC     D               
6D38: ED             ???                     
6D39: 93             SUB     E               
6D3A: 09             ADD     HL,BC           
6D3B: 15             DEC     D               
6D3C: 03             INC     BC              
6D3D: D2 6B BF       JP      NC,$BF6B        
6D40: 89             ADC     A,C             
6D41: 4E             LD      C,(HL)          
6D42: 8B             ADC     A,E             
6D43: 54             LD      D,H             
6D44: C7             RST     0X00            
6D45: DE 99          SBC     $99             
6D47: AF             XOR     A               
6D48: 39             ADD     HL,SP           
6D49: 4A             LD      C,D             
6D4A: 00             NOP                     
6D4B: 8F             ADC     A,A             
6D4C: 8F             ADC     A,A             
6D4D: 3A 00 03       LD      A,($0300)       
6D50: 2E 63          LD      L,$63           
6D52: BE             CP      (HL)            
6D53: CB B5          RES     6,L             
6D55: C3 B5 7B       JP      $7BB5           
6D58: 17             RLA                     
6D59: F3             DI                      
6D5A: 8C             ADC     A,H             
6D5B: 01 B3 45       LD      BC,$45B3        
6D5E: 90             SUB     B               
6D5F: 40             LD      B,B             
6D60: 49             LD      C,C             
6D61: F3             DI                      
6D62: 5F             LD      E,A             
6D63: C3 9E 09       JP      $099E           
6D66: BA             CP      D               
6D67: 5B             LD      E,E             
6D68: 98             SBC     B               
6D69: 56             LD      D,(HL)          
6D6A: D1             POP     DE              
6D6B: 03             INC     BC              
6D6C: 71             LD      (HL),C          
6D6D: 5B             LD      E,E             
6D6E: 17             RLA                     
6D6F: BE             CP      (HL)            
6D70: 98             SBC     B               
6D71: 47             LD      B,A             
6D72: 5E             LD      E,(HL)          
6D73: 96             SUB     (HL)            
6D74: D7             RST     0X10            
6D75: 89             ADC     A,C             
6D76: 17             RLA                     
6D77: 82             ADD     A,D             
6D78: 17             RLA                     
6D79: 55             LD      D,L             
6D7A: 5E             LD      E,(HL)          
6D7B: 36 A1          LD      (HL),$A1        
6D7D: 9B             SBC     E               
6D7E: 76             HALT                    
6D7F: 04             INC     B               
6D80: 07             RLCA                    
6D81: 0B             DEC     BC              
6D82: 05             DEC     B               
6D83: 0A             LD      A,(BC)          
6D84: 02             LD      (BC),A          
6D85: 02             LD      (BC),A          
6D86: 00             NOP                     
6D87: 8E             ADC     A,(HL)          
6D88: 90             SUB     B               
6D89: 80             ADD     A,B             
6D8A: A2             AND     D               
6D8B: 00             NOP                     
6D8C: 03             INC     BC              
6D8D: 56             LD      D,(HL)          
6D8E: C7             RST     0X00            
6D8F: DE 94          SBC     $94             
6D91: 14             INC     D               
6D92: 43             LD      B,E             
6D93: 5E             LD      E,(HL)          
6D94: 16 BC          LD      D,$BC           
6D96: DB 72          IN      A,($72)         
6D98: 04             INC     B               
6D99: 9A             SBC     D               
6D9A: 53             LD      D,E             
6D9B: BE             CP      (HL)            
6D9C: 8E             ADC     A,(HL)          
6D9D: 61             LD      H,C             
6D9E: B8             CP      B               
6D9F: 16 82          LD      D,$82           
6DA1: 17             RLA                     
6DA2: 49             LD      C,C             
6DA3: 5E             LD      E,(HL)          
6DA4: 63             LD      H,E             
6DA5: B1             OR      C               
6DA6: 05             DEC     B               
6DA7: BC             CP      H               
6DA8: 9E             SBC     (HL)            
6DA9: 61             LD      H,C             
6DAA: CE B0          ADC     $B0             
6DAC: 9B             SBC     E               
6DAD: 15             DEC     D               
6DAE: 11 8D 5F       LD      DE,$5F8D        
6DB1: 4A             LD      C,D             
6DB2: 3A 15 8D       LD      A,($8D15)       
6DB5: 7B             LD      A,E             
6DB6: 3A 15 66       LD      A,($6615)       
6DB9: 7B             LD      A,E             
6DBA: D0             RET     NC              
6DBB: 15             DEC     D               
6DBC: 82             ADD     A,D             
6DBD: 17             RLA                     
6DBE: 47             LD      B,A             
6DBF: 5E             LD      E,(HL)          
6DC0: 66             LD      H,(HL)          
6DC1: 49             LD      C,C             
6DC2: 90             SUB     B               
6DC3: 14             INC     D               
6DC4: 19             ADD     HL,DE           
6DC5: 58             LD      E,B             
6DC6: 66             LD      H,(HL)          
6DC7: 62             LD      H,D             
6DC8: F3             DI                      
6DC9: 17             RLA                     
6DCA: 0D             DEC     C               
6DCB: 8D             ADC     A,L             
6DCC: 56             LD      D,(HL)          
6DCD: F4 F4 72       CALL    P,$72F4         
6DD0: 4B             LD      C,E             
6DD1: 5E             LD      E,(HL)          
6DD2: C3 B5 09       JP      $09B5           
6DD5: 15             DEC     D               
6DD6: A3             AND     E               
6DD7: A0             AND     B               
6DD8: 03             INC     BC              
6DD9: A0             AND     B               
6DDA: 5F             LD      E,A             
6DDB: BE             CP      (HL)            
6DDC: 99             SBC     C               
6DDD: 16 C2          LD      D,$C2           
6DDF: B3             OR      E               
6DE0: F3             DI                      
6DE1: 17             RLA                     
6DE2: 17             RLA                     
6DE3: 8D             ADC     A,L             
6DE4: 04             INC     B               
6DE5: 47             LD      B,A             
6DE6: 0B             DEC     BC              
6DE7: 45             LD      B,L             
6DE8: 0A             LD      A,(BC)          
6DE9: 02             LD      (BC),A          
6DEA: 02             LD      (BC),A          
6DEB: 00             NOP                     
6DEC: 89             ADC     A,C             
6DED: 03             INC     BC              
6DEE: 02             LD      (BC),A          
6DEF: 00             NOP                     
6DF0: A0             AND     B               
6DF1: 01 36 0E       LD      BC,$0E36        
6DF4: 34             INC     (HL)            
6DF5: 0D             DEC     C               
6DF6: 14             INC     D               
6DF7: 01 1B 04       LD      BC,$041B        
6DFA: 10 5F          DJNZ    $6E5B           
6DFC: BE             CP      (HL)            
6DFD: 09             ADD     HL,BC           
6DFE: 15             DEC     D               
6DFF: A3             AND     E               
6E00: A0             AND     B               
6E01: 89             ADC     A,C             
6E02: 4E             LD      C,(HL)          
6E03: A5             AND     L               
6E04: 54             LD      D,H             
6E05: DB 16          IN      A,($16)         
6E07: D3 B9          OUT     ($B9),A         
6E09: BF             CP      A               
6E0A: 6C             LD      L,H             
6E0B: 0D             DEC     C               
6E0C: 1C             INC     E               
6E0D: 00             NOP                     
6E0E: 91             SUB     C               
6E0F: 17             RLA                     
6E10: 1B             DEC     DE              
6E11: 91             SUB     C               
6E12: 04             INC     B               
6E13: 12             LD      (DE),A          
6E14: 5F             LD      E,A             
6E15: BE             CP      (HL)            
6E16: 09             ADD     HL,BC           
6E17: 15             DEC     D               
6E18: A3             AND     E               
6E19: A0             AND     B               
6E1A: C9             RET                     
6E1B: 54             LD      D,H             
6E1C: B5             OR      L               
6E1D: B7             OR      A               
6E1E: AF             XOR     A               
6E1F: 14             INC     D               
6E20: 90             SUB     B               
6E21: 73             LD      (HL),E          
6E22: 1B             DEC     DE              
6E23: 58             LD      E,B             
6E24: 3F             CCF                     
6E25: A1             AND     C               
6E26: 17             RLA                     
6E27: 1C             INC     E               
6E28: 00             NOP                     
6E29: 04             INC     B               
6E2A: 02             LD      (BC),A          
6E2B: 00             NOP                     
6E2C: 92             SUB     D               
6E2D: 91             SUB     C               
6E2E: 80             ADD     A,B             
6E2F: 8F             ADC     A,A             
6E30: 00             NOP                     
6E31: 03             INC     BC              
6E32: 22 C7 DE       LD      ($DEC7),HL      
6E35: 94             SUB     H               
6E36: 14             INC     D               
6E37: 4B             LD      C,E             
6E38: 5E             LD      E,(HL)          
6E39: 83             ADD     A,E             
6E3A: 96             SUB     (HL)            
6E3B: CB 17          RL      A               
6E3D: 4E             LD      C,(HL)          
6E3E: C5             PUSH    BC              
6E3F: FB             EI                      
6E40: 17             RLA                     
6E41: 53             LD      D,E             
6E42: BE             CP      (HL)            
6E43: 4E             LD      C,(HL)          
6E44: 45             LD      B,L             
6E45: 31 49 46       LD      SP,$4649        
6E48: 5E             LD      E,(HL)          
6E49: 44             LD      B,H             
6E4A: A0             AND     B               
6E4B: 89             ADC     A,C             
6E4C: 17             RLA                     
6E4D: 82             ADD     A,D             
6E4E: 17             RLA                     
6E4F: 55             LD      D,L             
6E50: 5E             LD      E,(HL)          
6E51: 36 A1          LD      (HL),$A1        
6E53: 9B             SBC     E               
6E54: 76             HALT                    
6E55: 04             INC     B               
6E56: 68             LD      L,B             
6E57: 0B             DEC     BC              
6E58: 66             LD      H,(HL)          
6E59: 0A             LD      A,(BC)          
6E5A: 02             LD      (BC),A          
6E5B: 2F             CPL                     
6E5C: 0E 2D          LD      C,$2D           
6E5E: 0D             DEC     C               
6E5F: 10 01          DJNZ    $6E62           
6E61: 1B             DEC     DE              
6E62: 04             INC     B               
6E63: 0C             INC     C               
6E64: 5F             LD      E,A             
6E65: BE             CP      (HL)            
6E66: 09             ADD     HL,BC           
6E67: 15             DEC     D               
6E68: A3             AND     E               
6E69: A0             AND     B               
6E6A: 4B             LD      C,E             
6E6B: 7B             LD      A,E             
6E6C: 2F             CPL                     
6E6D: B8             CP      B               
6E6E: 9B             SBC     E               
6E6F: C1             POP     BC              
6E70: 0D             DEC     C               
6E71: 19             ADD     HL,DE           
6E72: 00             NOP                     
6E73: 90             SUB     B               
6E74: 17             RLA                     
6E75: 1B             DEC     DE              
6E76: 90             SUB     B               
6E77: 04             INC     B               
6E78: 0F             RRCA                    
6E79: 5F             LD      E,A             
6E7A: BE             CP      (HL)            
6E7B: 09             ADD     HL,BC           
6E7C: 15             DEC     D               
6E7D: A3             AND     E               
6E7E: A0             AND     B               
6E7F: C9             RET                     
6E80: 54             LD      D,H             
6E81: B5             OR      L               
6E82: B7             OR      A               
6E83: 89             ADC     A,C             
6E84: 14             INC     D               
6E85: D0             RET     NC              
6E86: 47             LD      B,A             
6E87: 2E 17          LD      L,$17           
6E89: 1C             INC     E               
6E8A: 00             NOP                     
6E8B: 11 32 0E       LD      DE,$0E32        
6E8E: 30 0D          JR      NC,$6E9D        
6E90: 10 08          DJNZ    $6E9A           
6E92: 1C             INC     E               
6E93: 04             INC     B               
6E94: 0C             INC     C               
6E95: 8D             ADC     A,L             
6E96: 7B             LD      A,E             
6E97: 8E             ADC     A,(HL)          
6E98: 14             INC     D               
6E99: 63             LD      H,E             
6E9A: B1             OR      C               
6E9B: FB             EI                      
6E9C: 5C             LD      E,H             
6E9D: 5F             LD      E,A             
6E9E: A0             AND     B               
6E9F: 1B             DEC     DE              
6EA0: 9C             SBC     H               
6EA1: 0D             DEC     C               
6EA2: 1C             INC     E               
6EA3: 08             EX      AF,AF'          
6EA4: 1B             DEC     DE              
6EA5: 17             RLA                     
6EA6: 1C             INC     E               
6EA7: 91             SUB     C               
6EA8: 17             RLA                     
6EA9: 1B             DEC     DE              
6EAA: 00             NOP                     
6EAB: 04             INC     B               
6EAC: 12             LD      (DE),A          
6EAD: 64             LD      H,H             
6EAE: B7             OR      A               
6EAF: B7             OR      A               
6EB0: C6 B0          ADD     $B0             
6EB2: C6 D6          ADD     $D6             
6EB4: 6A             LD      L,D             
6EB5: DB 72          IN      A,($72)         
6EB7: 81             ADD     A,C             
6EB8: 5B             LD      E,E             
6EB9: 91             SUB     C               
6EBA: AF             XOR     A               
6EBB: F0             RET     P               
6EBC: A4             AND     H               
6EBD: 5B             LD      E,E             
6EBE: BB             CP      E               
6EBF: 92             SUB     D               
6EC0: 4B             LD      C,E             
6EC1: 00             NOP                     
6EC2: 03             INC     BC              
6EC3: 3B             DEC     SP              
6EC4: C7             RST     0X00            
6EC5: DE 94          SBC     $94             
6EC7: 14             INC     D               
6EC8: 43             LD      B,E             
6EC9: 5E             LD      E,(HL)          
6ECA: 16 BC          LD      D,$BC           
6ECC: DB 72          IN      A,($72)         
6ECE: 9E             SBC     (HL)            
6ECF: 61             LD      H,C             
6ED0: D0             RET     NC              
6ED1: B0             OR      B               
6ED2: 9B             SBC     E               
6ED3: 53             LD      D,E             
6ED4: 6B             LD      L,E             
6ED5: BF             CP      A               
6ED6: 4E             LD      C,(HL)          
6ED7: 45             LD      B,L             
6ED8: 11 A0 FB       LD      DE,$FBA0        
6EDB: 14             INC     D               
6EDC: 4B             LD      C,E             
6EDD: B2             OR      D               
6EDE: 70             LD      (HL),B          
6EDF: C0             RET     NZ              
6EE0: 6E             LD      L,(HL)          
6EE1: 98             SBC     B               
6EE2: FA 17 DA       JP      M,$DA17         
6EE5: 78             LD      A,B             
6EE6: 3F             CCF                     
6EE7: 16 0D          LD      D,$0D           
6EE9: 47             LD      B,A             
6EEA: F7             RST     0X30            
6EEB: 17             RLA                     
6EEC: 17             RLA                     
6EED: BA             CP      D               
6EEE: 82             ADD     A,D             
6EEF: 17             RLA                     
6EF0: 2F             CPL                     
6EF1: 62             LD      H,D             
6EF2: D5             PUSH    DE              
6EF3: 15             DEC     D               
6EF4: 7B             LD      A,E             
6EF5: 14             INC     D               
6EF6: 55             LD      D,L             
6EF7: A4             AND     H               
6EF8: 09             ADD     HL,BC           
6EF9: B7             OR      A               
6EFA: 47             LD      B,A             
6EFB: 5E             LD      E,(HL)          
6EFC: 66             LD      H,(HL)          
6EFD: 49             LD      C,C             
6EFE: 2E 04          LD      L,$04           
6F00: 0B             DEC     BC              
6F01: 0B             DEC     BC              
6F02: 09             ADD     HL,BC           
6F03: 0A             LD      A,(BC)          
6F04: 03             INC     BC              
6F05: 02             LD      (BC),A          
6F06: 00             NOP                     
6F07: 90             SUB     B               
6F08: 04             INC     B               
6F09: 02             LD      (BC),A          
6F0A: 00             NOP                     
6F0B: 93             SUB     E               
6F0C: 93             SUB     E               
6F0D: 22 00 03       LD      ($0300),HL      
6F10: 12             LD      (DE),A          
6F11: C7             RST     0X00            
6F12: DE 94          SBC     $94             
6F14: 14             INC     D               
6F15: 4B             LD      C,E             
6F16: 5E             LD      E,(HL)          
6F17: 96             SUB     (HL)            
6F18: 96             SUB     (HL)            
6F19: DB 72          IN      A,($72)         
6F1B: 54             LD      D,H             
6F1C: 59             LD      E,C             
6F1D: D6 83          SUB     $83             
6F1F: 98             SBC     B               
6F20: C5             PUSH    BC              
6F21: 57             LD      D,A             
6F22: 61             LD      H,C             
6F23: 04             INC     B               
6F24: 0B             DEC     BC              
6F25: 0B             DEC     BC              
6F26: 09             ADD     HL,BC           
6F27: 0A             LD      A,(BC)          
6F28: 03             INC     BC              
6F29: 02             LD      (BC),A          
6F2A: 00             NOP                     
6F2B: 92             SUB     D               
6F2C: 04             INC     B               
6F2D: 02             LD      (BC),A          
6F2E: 00             NOP                     
6F2F: 94             SUB     H               
6F30: 94             SUB     H               
6F31: 58             LD      E,B             
6F32: 00             NOP                     
6F33: 03             INC     BC              
6F34: 3B             DEC     SP              
6F35: C7             RST     0X00            
6F36: DE 94          SBC     $94             
6F38: 14             INC     D               
6F39: 43             LD      B,E             
6F3A: 5E             LD      E,(HL)          
6F3B: 16 BC          LD      D,$BC           
6F3D: DB 72          IN      A,($72)         
6F3F: 9E             SBC     (HL)            
6F40: 61             LD      H,C             
6F41: D0             RET     NC              
6F42: B0             OR      B               
6F43: 9B             SBC     E               
6F44: 53             LD      D,E             
6F45: 6B             LD      L,E             
6F46: BF             CP      A               
6F47: 4E             LD      C,(HL)          
6F48: 45             LD      B,L             
6F49: 11 A0 FB       LD      DE,$FBA0        
6F4C: 14             INC     D               
6F4D: 4B             LD      C,E             
6F4E: B2             OR      D               
6F4F: 70             LD      (HL),B          
6F50: C0             RET     NZ              
6F51: 6E             LD      L,(HL)          
6F52: 98             SBC     B               
6F53: FA 17 DA       JP      M,$DA17         
6F56: 78             LD      A,B             
6F57: 3F             CCF                     
6F58: 16 0D          LD      D,$0D           
6F5A: 47             LD      B,A             
6F5B: 23             INC     HL              
6F5C: 15             DEC     D               
6F5D: 17             RLA                     
6F5E: BA             CP      D               
6F5F: 82             ADD     A,D             
6F60: 17             RLA                     
6F61: 2F             CPL                     
6F62: 62             LD      H,D             
6F63: D5             PUSH    DE              
6F64: 15             DEC     D               
6F65: 7B             LD      A,E             
6F66: 14             INC     D               
6F67: 55             LD      D,L             
6F68: A4             AND     H               
6F69: 09             ADD     HL,BC           
6F6A: B7             OR      A               
6F6B: 59             LD      E,C             
6F6C: 5E             LD      E,(HL)          
6F6D: 66             LD      H,(HL)          
6F6E: 62             LD      H,D             
6F6F: 2E 04          LD      L,$04           
6F71: 18 0B          JR      $6F7E           
6F73: 16 0A          LD      D,$0A           
6F75: 03             INC     BC              
6F76: 02             LD      (BC),A          
6F77: 00             NOP                     
6F78: 93             SUB     E               
6F79: 04             INC     B               
6F7A: 0F             RRCA                    
6F7B: 0E 0D          LD      C,$0D           
6F7D: 0D             DEC     C               
6F7E: 09             ADD     HL,BC           
6F7F: 20 1D          JR      NZ,$6F9E        
6F81: 03             INC     BC              
6F82: 00             NOP                     
6F83: 16 17          LD      D,$17           
6F85: 15             DEC     D               
6F86: 95             SUB     L               
6F87: 0C             INC     C               
6F88: 00             NOP                     
6F89: 95             SUB     L               
6F8A: 95             SUB     L               
6F8B: 32 00 03       LD      ($0300),A       
6F8E: 20 C7          JR      NZ,$6F57        
6F90: DE 94          SBC     $94             
6F92: 14             INC     D               
6F93: 4B             LD      C,E             
6F94: 5E             LD      E,(HL)          
6F95: 83             ADD     A,E             
6F96: 96             SUB     (HL)            
6F97: 3B             DEC     SP              
6F98: 16 B7          LD      D,$B7           
6F9A: B1             OR      C               
6F9B: 39             ADD     HL,SP           
6F9C: 17             RLA                     
6F9D: DB 9F          IN      A,($9F)         
6F9F: 56             LD      D,(HL)          
6FA0: D1             POP     DE              
6FA1: 03             INC     BC              
6FA2: 71             LD      (HL),C          
6FA3: 5B             LD      E,E             
6FA4: 17             RLA                     
6FA5: BE             CP      (HL)            
6FA6: 98             SBC     B               
6FA7: 47             LD      B,A             
6FA8: 5E             LD      E,(HL)          
6FA9: 96             SUB     (HL)            
6FAA: D7             RST     0X10            
6FAB: 23             INC     HL              
6FAC: 15             DEC     D               
6FAD: 17             RLA                     
6FAE: BA             CP      D               
6FAF: 04             INC     B               
6FB0: 0D             DEC     C               
6FB1: 0B             DEC     BC              
6FB2: 0B             DEC     BC              
6FB3: 0A             LD      A,(BC)          
6FB4: 36 01          LD      (HL),$01        
6FB6: 8F             ADC     A,A             
6FB7: 17             RLA                     
6FB8: 01 8F 03       LD      BC,$038F        
6FBB: 02             LD      (BC),A          
6FBC: 00             NOP                     
6FBD: 94             SUB     H               
6FBE: 96             SUB     (HL)            
6FBF: 30 00          JR      NC,$6FC1        
6FC1: 03             INC     BC              
6FC2: 18 C7          JR      $6F8B           
6FC4: DE 94          SBC     $94             
6FC6: 14             INC     D               
6FC7: 4B             LD      C,E             
6FC8: 5E             LD      E,(HL)          
6FC9: 83             ADD     A,E             
6FCA: 96             SUB     (HL)            
6FCB: FF             RST     0X38            
6FCC: 14             INC     D               
6FCD: 97             SUB     A               
6FCE: 9A             SBC     D               
6FCF: FB             EI                      
6FD0: 14             INC     D               
6FD1: 4B             LD      C,E             
6FD2: B2             OR      D               
6FD3: 4F             LD      C,A             
6FD4: 59             LD      E,C             
6FD5: 0C             INC     C               
6FD6: A3             AND     E               
6FD7: 91             SUB     C               
6FD8: C5             PUSH    BC              
6FD9: FF             RST     0X38            
6FDA: 8B             ADC     A,E             
6FDB: 04             INC     B               
6FDC: 13             INC     DE              
6FDD: 0B             DEC     BC              
6FDE: 11 0A 01       LD      DE,$010A        
6FE1: 02             LD      (BC),A          
6FE2: 00             NOP                     
6FE3: A3             AND     E               
6FE4: 02             LD      (BC),A          
6FE5: 02             LD      (BC),A          
6FE6: 00             NOP                     
6FE7: A4             AND     H               
6FE8: 04             INC     B               
6FE9: 02             LD      (BC),A          
6FEA: 00             NOP                     
6FEB: 97             SUB     A               
6FEC: 03             INC     BC              
6FED: 02             LD      (BC),A          
6FEE: 00             NOP                     
6FEF: A4             AND     H               
6FF0: 97             SUB     A               
6FF1: 30 00          JR      NC,$6FF3        
6FF3: 03             INC     BC              
6FF4: 18 C7          JR      $6FBD           
6FF6: DE 94          SBC     $94             
6FF8: 14             INC     D               
6FF9: 4B             LD      C,E             
6FFA: 5E             LD      E,(HL)          
6FFB: 83             ADD     A,E             
6FFC: 96             SUB     (HL)            
6FFD: FB             EI                      
6FFE: 14             INC     D               
6FFF: 4B             LD      C,E             
7000: B2             OR      D               
7001: F0             RET     P               
7002: 59             LD      E,C             
7003: 9B             SBC     E               
7004: B7             OR      A               
7005: 4F             LD      C,A             
7006: 59             LD      E,C             
7007: 0C             INC     C               
7008: A3             AND     E               
7009: 91             SUB     C               
700A: C5             PUSH    BC              
700B: FF             RST     0X38            
700C: 8B             ADC     A,E             
700D: 04             INC     B               
700E: 13             INC     DE              
700F: 0B             DEC     BC              
7010: 11 0A 01       LD      DE,$010A        
7013: 02             LD      (BC),A          
7014: 00             NOP                     
7015: A2             AND     D               
7016: 02             LD      (BC),A          
7017: 02             LD      (BC),A          
7018: 00             NOP                     
7019: 96             SUB     (HL)            
701A: 03             INC     BC              
701B: 02             LD      (BC),A          
701C: 00             NOP                     
701D: A3             AND     E               
701E: 04             INC     B               
701F: 02             LD      (BC),A          
7020: 00             NOP                     
7021: 98             SBC     B               
7022: 98             SBC     B               
7023: 40             LD      B,B             
7024: 00             NOP                     
7025: 03             INC     BC              
7026: 28 6C          JR      Z,$7094         
7028: BE             CP      (HL)            
7029: 29             ADD     HL,HL           
702A: A1             AND     C               
702B: 16 71          LD      D,$71           
702D: DB 72          IN      A,($72)         
702F: F0             RET     P               
7030: 81             ADD     A,C             
7031: BF             CP      A               
7032: 6D             LD      L,L             
7033: 51             LD      D,C             
7034: 18 55          JR      $708B           
7036: C2 1B 60       JP      NZ,$601B        
7039: 5F             LD      E,A             
703A: BE             CP      (HL)            
703B: 23             INC     HL              
703C: 15             DEC     D               
703D: F3             DI                      
703E: B9             CP      C               
703F: 0E D0          LD      C,$D0           
7041: 11 8A 83       LD      DE,$838A        
7044: 64             LD      H,H             
7045: 84             ADD     A,H             
7046: 15             DEC     D               
7047: 96             SUB     (HL)            
7048: 5F             LD      E,A             
7049: 7F             LD      A,A             
704A: 17             RLA                     
704B: E6 93          AND     $93             
704D: DB 63          IN      A,($63)         
704F: 04             INC     B               
7050: 13             INC     DE              
7051: 0B             DEC     BC              
7052: 11 0A 01       LD      DE,$010A        
7055: 02             LD      (BC),A          
7056: 00             NOP                     
7057: 9B             SBC     E               
7058: 02             LD      (BC),A          
7059: 02             LD      (BC),A          
705A: 00             NOP                     
705B: 99             SBC     C               
705C: 03             INC     BC              
705D: 02             LD      (BC),A          
705E: 00             NOP                     
705F: 97             SUB     A               
7060: 04             INC     B               
7061: 02             LD      (BC),A          
7062: 00             NOP                     
7063: 9E             SBC     (HL)            
7064: 99             SBC     C               
7065: 44             LD      B,H             
7066: 00             NOP                     
7067: 03             INC     BC              
7068: 2C             INC     L               
7069: 83             ADD     A,E             
706A: 7A             LD      A,D             
706B: 45             LD      B,L             
706C: 45             LD      B,L             
706D: E3             EX      (SP),HL         
706E: 8B             ADC     A,E             
706F: 10 B2          DJNZ    $7023           
7071: C4 6A 59       CALL    NZ,$596A        
7074: 60             LD      H,B             
7075: 5B             LD      E,E             
7076: B1             OR      C               
7077: C7             RST     0X00            
7078: DE 66          SBC     $66             
707A: 17             RLA                     
707B: 8E             ADC     A,(HL)          
707C: 48             LD      C,B             
707D: D6 B5          SUB     $B5             
707F: DB 72          IN      A,($72)         
7081: 47             LD      B,A             
7082: B9             CP      C               
7083: 53             LD      D,E             
7084: BE             CP      (HL)            
7085: 0E D0          LD      C,$D0           
7087: 11 8A 83       LD      DE,$838A        
708A: 64             LD      H,H             
708B: 84             ADD     A,H             
708C: 15             DEC     D               
708D: 96             SUB     (HL)            
708E: 5F             LD      E,A             
708F: 7F             LD      A,A             
7090: 17             RLA                     
7091: E6 93          AND     $93             
7093: DB 63          IN      A,($63)         
7095: 04             INC     B               
7096: 13             INC     DE              
7097: 0B             DEC     BC              
7098: 11 0A 01       LD      DE,$010A        
709B: 02             LD      (BC),A          
709C: 00             NOP                     
709D: 9F             SBC     A               
709E: 02             LD      (BC),A          
709F: 02             LD      (BC),A          
70A0: 00             NOP                     
70A1: 96             SUB     (HL)            
70A2: 03             INC     BC              
70A3: 02             LD      (BC),A          
70A4: 00             NOP                     
70A5: 98             SBC     B               
70A6: 04             INC     B               
70A7: 02             LD      (BC),A          
70A8: 00             NOP                     
70A9: 9A             SBC     D               
70AA: 9A             SBC     D               
70AB: 59             LD      E,C             
70AC: 00             NOP                     
70AD: 03             INC     BC              
70AE: 41             LD      B,C             
70AF: 6C             LD      L,H             
70B0: BE             CP      (HL)            
70B1: 29             ADD     HL,HL           
70B2: A1             AND     C               
70B3: 16 71          LD      D,$71           
70B5: DB 72          IN      A,($72)         
70B7: F0             RET     P               
70B8: 59             LD      E,C             
70B9: 9B             SBC     E               
70BA: B7             OR      A               
70BB: 8E             ADC     A,(HL)          
70BC: C5             PUSH    BC              
70BD: 31 62 09       LD      SP,$0962        
70C0: B3             OR      E               
70C1: 76             HALT                    
70C2: BE             CP      (HL)            
70C3: 51             LD      D,C             
70C4: 18 45          JR      $710B           
70C6: C2 83 48       JP      NZ,$4883        
70C9: A7             AND     A               
70CA: B7             OR      A               
70CB: 82             ADD     A,D             
70CC: 17             RLA                     
70CD: 49             LD      C,C             
70CE: 5E             LD      E,(HL)          
70CF: 63             LD      H,E             
70D0: B1             OR      C               
70D1: 04             INC     B               
70D2: BC             CP      H               
70D3: 00             NOP                     
70D4: B3             OR      E               
70D5: 5B             LD      E,E             
70D6: E3             EX      (SP),HL         
70D7: 16 6C          LD      D,$6C           
70D9: 4B             LD      C,E             
70DA: 62             LD      H,D             
70DB: 03             INC     BC              
70DC: A0             AND     B               
70DD: 5F             LD      E,A             
70DE: BE             CP      (HL)            
70DF: F7             RST     0X30            
70E0: 17             RLA                     
70E1: F3             DI                      
70E2: B9             CP      C               
70E3: 0E D0          LD      C,$D0           
70E5: 11 8A 96       LD      DE,$968A        
70E8: 64             LD      H,H             
70E9: DB 72          IN      A,($72)         
70EB: EF             RST     0X28            
70EC: BD             CP      L               
70ED: FF             RST     0X38            
70EE: A5             AND     L               
70EF: 2E 04          LD      L,$04           
70F1: 13             INC     DE              
70F2: 0B             DEC     BC              
70F3: 11 0A 01       LD      DE,$010A        
70F6: 02             LD      (BC),A          
70F7: 00             NOP                     
70F8: 9B             SBC     E               
70F9: 02             LD      (BC),A          
70FA: 02             LD      (BC),A          
70FB: 00             NOP                     
70FC: 99             SBC     C               
70FD: 03             INC     BC              
70FE: 02             LD      (BC),A          
70FF: 00             NOP                     
7100: 9C             SBC     H               
7101: 04             INC     B               
7102: 02             LD      (BC),A          
7103: 00             NOP                     
7104: A4             AND     H               
7105: 9B             SBC     E               
7106: 4D             LD      C,L             
7107: 00             NOP                     
7108: 03             INC     BC              
7109: 35             DEC     (HL)            
710A: 6C             LD      L,H             
710B: BE             CP      (HL)            
710C: 29             ADD     HL,HL           
710D: A1             AND     C               
710E: 03             INC     BC              
710F: 71             LD      (HL),C          
7110: 73             LD      (HL),E          
7111: 15             DEC     D               
7112: 0B             DEC     BC              
7113: A3             AND     E               
7114: 96             SUB     (HL)            
7115: 96             SUB     (HL)            
7116: DB 72          IN      A,($72)         
7118: F0             RET     P               
7119: 81             ADD     A,C             
711A: BF             CP      A               
711B: 6D             LD      L,L             
711C: 51             LD      D,C             
711D: 18 45          JR      $7164           
711F: C2 83 48       JP      NZ,$4883        
7122: A7             AND     A               
7123: B7             OR      A               
7124: 82             ADD     A,D             
7125: 17             RLA                     
7126: 50             LD      D,B             
7127: 5E             LD      E,(HL)          
7128: BE             CP      (HL)            
7129: A0             AND     B               
712A: 19             ADD     HL,DE           
712B: 71             LD      (HL),C          
712C: 46             LD      B,(HL)          
712D: 48             LD      C,B             
712E: B8             CP      B               
712F: 16 7B          LD      D,$7B           
7131: 14             INC     D               
7132: 89             ADC     A,C             
7133: 91             SUB     C               
7134: 08             EX      AF,AF'          
7135: 99             SBC     C               
7136: D7             RST     0X10            
7137: 78             LD      A,B             
7138: B3             OR      E               
7139: 9A             SBC     D               
713A: EF             RST     0X28            
713B: BD             CP      L               
713C: FF             RST     0X38            
713D: A5             AND     L               
713E: 2E 04          LD      L,$04           
7140: 13             INC     DE              
7141: 0B             DEC     BC              
7142: 11 0A 01       LD      DE,$010A        
7145: 02             LD      (BC),A          
7146: 00             NOP                     
7147: A2             AND     D               
7148: 02             LD      (BC),A          
7149: 02             LD      (BC),A          
714A: 00             NOP                     
714B: 9D             SBC     L               
714C: 04             INC     B               
714D: 02             LD      (BC),A          
714E: 00             NOP                     
714F: 9A             SBC     D               
7150: 03             INC     BC              
7151: 02             LD      (BC),A          
7152: 00             NOP                     
7153: 98             SBC     B               
7154: 9C             SBC     H               
7155: 3A 00 03       LD      A,($0300)       
7158: 26 C7          LD      H,$C7           
715A: DE 94          SBC     $94             
715C: 14             INC     D               
715D: 55             LD      D,L             
715E: 5E             LD      E,(HL)          
715F: 50             LD      D,B             
7160: BD             CP      L               
7161: 90             SUB     B               
7162: 5A             LD      E,D             
7163: C4 6A 59       CALL    NZ,$596A        
7166: 60             LD      H,B             
7167: 5B             LD      E,E             
7168: B1             OR      C               
7169: 5F             LD      E,A             
716A: BE             CP      (HL)            
716B: F7             RST     0X30            
716C: 17             RLA                     
716D: F3             DI                      
716E: B9             CP      C               
716F: 9E             SBC     (HL)            
7170: 61             LD      H,C             
7171: D0             RET     NC              
7172: B0             OR      B               
7173: 9B             SBC     E               
7174: 53             LD      D,E             
7175: C3 9E 5F       JP      $5F9E           
7178: BE             CP      (HL)            
7179: 7F             LD      A,A             
717A: 17             RLA                     
717B: E6 93          AND     $93             
717D: DB 63          IN      A,($63)         
717F: 04             INC     B               
7180: 0F             RRCA                    
7181: 0B             DEC     BC              
7182: 0D             DEC     C               
7183: 0A             LD      A,(BC)          
7184: 01 02 00       LD      BC,$0002        
7187: 9D             SBC     L               
7188: 02             LD      (BC),A          
7189: 02             LD      (BC),A          
718A: 00             NOP                     
718B: 9F             SBC     A               
718C: 04             INC     B               
718D: 02             LD      (BC),A          
718E: 00             NOP                     
718F: 9A             SBC     D               
7190: 9D             SBC     L               
7191: 80             ADD     A,B             
7192: B3             OR      E               
7193: 00             NOP                     
7194: 03             INC     BC              
7195: 12             LD      (DE),A          
7196: C7             RST     0X00            
7197: DE 94          SBC     $94             
7199: 14             INC     D               
719A: 43             LD      B,E             
719B: 5E             LD      E,(HL)          
719C: 16 BC          LD      D,$BC           
719E: DB 72          IN      A,($72)         
71A0: 04             INC     B               
71A1: 9A             SBC     D               
71A2: 53             LD      D,E             
71A3: BE             CP      (HL)            
71A4: 0E D0          LD      C,$D0           
71A6: 9B             SBC     E               
71A7: 8F             ADC     A,A             
71A8: 04             INC     B               
71A9: 80             ADD     A,B             
71AA: 9B             SBC     E               
71AB: 0B             DEC     BC              
71AC: 80             ADD     A,B             
71AD: 98             SBC     B               
71AE: 0A             LD      A,(BC)          
71AF: 01 02 00       LD      BC,$0002        
71B2: 9B             SBC     E               
71B3: 03             INC     BC              
71B4: 02             LD      (BC),A          
71B5: 00             NOP                     
71B6: 9E             SBC     (HL)            
71B7: 17             RLA                     
71B8: 80             ADD     A,B             
71B9: 88             ADC     A,B             
71BA: 0D             DEC     C               
71BB: 80             ADD     A,B             
71BC: 85             ADD     A,L             
71BD: 08             EX      AF,AF'          
71BE: 21 0E 80       LD      HL,$800E        
71C1: 80             ADD     A,B             
71C2: 0D             DEC     C               
71C3: 54             LD      D,H             
71C4: 05             DEC     B               
71C5: 7F             LD      A,A             
71C6: 04             INC     B               
71C7: 2A C7 DE       LD      HL,($DEC7)      
71CA: DE 14          SBC     $14             
71CC: 64             LD      H,H             
71CD: 7A             LD      A,D             
71CE: 89             ADC     A,C             
71CF: 17             RLA                     
71D0: 82             ADD     A,D             
71D1: 17             RLA                     
71D2: 54             LD      D,H             
71D3: 5E             LD      E,(HL)          
71D4: 38 A0          JR      C,$7176         
71D6: 3B             DEC     SP              
71D7: F4 4B 49       CALL    P,$494B         
71DA: C7             RST     0X00            
71DB: DE 66          SBC     $66             
71DD: 17             RLA                     
71DE: D3 61          OUT     ($61),A         
71E0: 03             INC     BC              
71E1: A0             AND     B               
71E2: 5F             LD      E,A             
71E3: BE             CP      (HL)            
71E4: 39             ADD     HL,SP           
71E5: 17             RLA                     
71E6: E6 9E          AND     $9E             
71E8: D6 15          SUB     $15             
71EA: E1             POP     HL              
71EB: 14             INC     D               
71EC: FB             EI                      
71ED: 8C             ADC     A,H             
71EE: 17             RLA                     
71EF: A7             AND     A               
71F0: 5B             LD      E,E             
71F1: BB             CP      E               
71F2: 17             RLA                     
71F3: 36 00          LD      (HL),$00        
71F5: 17             RLA                     
71F6: 29             ADD     HL,HL           
71F7: FF             RST     0X38            
71F8: 17             RLA                     
71F9: 2A FF 17       LD      HL,($17FF)      
71FC: 2B             DEC     HL              
71FD: FF             RST     0X38            
71FE: 17             RLA                     
71FF: 2C             INC     L               
7200: FF             RST     0X38            
7201: 17             RLA                     
7202: 2D             DEC     L               
7203: FF             RST     0X38            
7204: 17             RLA                     
7205: 2E FF          LD      L,$FF           
7207: 17             RLA                     
7208: 31 FF 17       LD      SP,$17FF        
720B: 34             INC     (HL)            
720C: FF             RST     0X38            
720D: 17             RLA                     
720E: 35             DEC     (HL)            
720F: FF             RST     0X38            
7210: 17             RLA                     
7211: 3A FF 17       LD      A,($17FF)       
7214: 3C             INC     A               
7215: 00             NOP                     
7216: 00             NOP                     
7217: 81             ADD     A,C             
7218: 04             INC     B               
7219: 28 4B          JR      Z,$7266         
721B: 49             LD      C,C             
721C: C7             RST     0X00            
721D: DE DE          SBC     $DE             
721F: 14             INC     D               
7220: 64             LD      H,H             
7221: 7A             LD      A,D             
7222: 16 EE          LD      D,$EE           
7224: DB 72          IN      A,($72)         
7226: 10 CB          DJNZ    $71F3           
7228: 49             LD      C,C             
7229: 5E             LD      E,(HL)          
722A: CF             RST     0X08            
722B: 7B             LD      A,E             
722C: D9             EXX                     
722D: B5             OR      L               
722E: 3B             DEC     SP              
722F: 4A             LD      C,D             
7230: 8E             ADC     A,(HL)          
7231: 48             LD      C,B             
7232: 51             LD      D,C             
7233: 18 48          JR      $727D           
7235: C2 46 48       JP      NZ,$4846        
7238: 89             ADC     A,C             
7239: 17             RLA                     
723A: 82             ADD     A,D             
723B: 17             RLA                     
723C: 49             LD      C,C             
723D: 5E             LD      E,(HL)          
723E: 07             RLCA                    
723F: B3             OR      E               
7240: 57             LD      D,A             
7241: 98             SBC     B               
7242: 04             INC     B               
7243: 02             LD      (BC),A          
7244: 00             NOP                     
7245: 9C             SBC     H               
7246: 9E             SBC     (HL)            
7247: 25             DEC     H               
7248: 00             NOP                     
7249: 03             INC     BC              
724A: 11 C7 DE       LD      DE,$DEC7        
724D: 94             SUB     H               
724E: 14             INC     D               
724F: 43             LD      B,E             
7250: 5E             LD      E,(HL)          
7251: 16 BC          LD      D,$BC           
7253: DB 72          IN      A,($72)         
7255: 95             SUB     L               
7256: 5F             LD      E,A             
7257: 19             ADD     HL,DE           
7258: BC             CP      H               
7259: 46             LD      B,(HL)          
725A: 48             LD      C,B             
725B: 2E 04          LD      L,$04           
725D: 0F             RRCA                    
725E: 0B             DEC     BC              
725F: 0D             DEC     C               
7260: 0A             LD      A,(BC)          
7261: 01 02 00       LD      BC,$0002        
7264: 9D             SBC     L               
7265: 02             LD      (BC),A          
7266: 02             LD      (BC),A          
7267: 00             NOP                     
7268: 9F             SBC     A               
7269: 03             INC     BC              
726A: 02             LD      (BC),A          
726B: 00             NOP                     
726C: 98             SBC     B               
726D: 9F             SBC     A               
726E: 26 00          LD      H,$00           
7270: 03             INC     BC              
7271: 12             LD      (DE),A          
7272: C7             RST     0X00            
7273: DE 94          SBC     $94             
7275: 14             INC     D               
7276: 43             LD      B,E             
7277: 5E             LD      E,(HL)          
7278: 16 BC          LD      D,$BC           
727A: DB 72          IN      A,($72)         
727C: 47             LD      B,A             
727D: B9             CP      C               
727E: 53             LD      D,E             
727F: BE             CP      (HL)            
7280: 0E D0          LD      C,$D0           
7282: 9B             SBC     E               
7283: 8F             ADC     A,A             
7284: 04             INC     B               
7285: 0F             RRCA                    
7286: 0B             DEC     BC              
7287: 0D             DEC     C               
7288: 0A             LD      A,(BC)          
7289: 04             INC     B               
728A: 02             LD      (BC),A          
728B: 00             NOP                     
728C: 9C             SBC     H               
728D: 03             INC     BC              
728E: 02             LD      (BC),A          
728F: 00             NOP                     
7290: 9E             SBC     (HL)            
7291: 02             LD      (BC),A          
7292: 02             LD      (BC),A          
7293: 00             NOP                     
7294: 99             SBC     C               
7295: A0             AND     B               
7296: 20 00          JR      NZ,$7298        
7298: 03             INC     BC              
7299: 14             INC     D               
729A: C7             RST     0X00            
729B: DE 94          SBC     $94             
729D: 14             INC     D               
729E: 4B             LD      C,E             
729F: 5E             LD      E,(HL)          
72A0: 83             ADD     A,E             
72A1: 96             SUB     (HL)            
72A2: CF             RST     0X08            
72A3: 17             RLA                     
72A4: 7B             LD      A,E             
72A5: B4             OR      H               
72A6: E3             EX      (SP),HL         
72A7: B8             CP      B               
72A8: F3             DI                      
72A9: 8C             ADC     A,H             
72AA: 01 B3 DB       LD      BC,$DBB3        
72AD: 95             SUB     L               
72AE: 04             INC     B               
72AF: 07             RLCA                    
72B0: 0B             DEC     BC              
72B1: 05             DEC     B               
72B2: 0A             LD      A,(BC)          
72B3: 04             INC     B               
72B4: 02             LD      (BC),A          
72B5: 00             NOP                     
72B6: 90             SUB     B               
72B7: A1             AND     C               
72B8: 2C             INC     L               
72B9: 00             NOP                     
72BA: 03             INC     BC              
72BB: 20 C7          JR      NZ,$7284        
72BD: DE 94          SBC     $94             
72BF: 14             INC     D               
72C0: 4B             LD      C,E             
72C1: 5E             LD      E,(HL)          
72C2: 83             ADD     A,E             
72C3: 96             SUB     (HL)            
72C4: 5F             LD      E,A             
72C5: 17             RLA                     
72C6: 46             LD      B,(HL)          
72C7: 48             LD      C,B             
72C8: 39             ADD     HL,SP           
72C9: 17             RLA                     
72CA: DB 9F          IN      A,($9F)         
72CC: 56             LD      D,(HL)          
72CD: D1             POP     DE              
72CE: 03             INC     BC              
72CF: 71             LD      (HL),C          
72D0: 5B             LD      E,E             
72D1: 17             RLA                     
72D2: BE             CP      (HL)            
72D3: 98             SBC     B               
72D4: 47             LD      B,A             
72D5: 5E             LD      E,(HL)          
72D6: 96             SUB     (HL)            
72D7: D7             RST     0X10            
72D8: 23             INC     HL              
72D9: 15             DEC     D               
72DA: 17             RLA                     
72DB: BA             CP      D               
72DC: 04             INC     B               
72DD: 07             RLCA                    
72DE: 0B             DEC     BC              
72DF: 05             DEC     B               
72E0: 0A             LD      A,(BC)          
72E1: 03             INC     BC              
72E2: 02             LD      (BC),A          
72E3: 00             NOP                     
72E4: 84             ADD     A,H             
72E5: A2             AND     D               
72E6: 30 00          JR      NC,$72E8        
72E8: 03             INC     BC              
72E9: 18 C7          JR      $72B2           
72EB: DE 94          SBC     $94             
72ED: 14             INC     D               
72EE: 4B             LD      C,E             
72EF: 5E             LD      E,(HL)          
72F0: 83             ADD     A,E             
72F1: 96             SUB     (HL)            
72F2: FB             EI                      
72F3: 14             INC     D               
72F4: 4B             LD      C,E             
72F5: B2             OR      D               
72F6: 4F             LD      C,A             
72F7: 59             LD      E,C             
72F8: 06 A3          LD      B,$A3           
72FA: 9D             SBC     L               
72FB: 61             LD      H,C             
72FC: 4C             LD      C,H             
72FD: 5E             LD      E,(HL)          
72FE: 91             SUB     C               
72FF: C5             PUSH    BC              
7300: FF             RST     0X38            
7301: 8B             ADC     A,E             
7302: 04             INC     B               
7303: 13             INC     DE              
7304: 0B             DEC     BC              
7305: 11 0A 03       LD      DE,$030A        
7308: 02             LD      (BC),A          
7309: 00             NOP                     
730A: A4             AND     H               
730B: 01 02 00       LD      BC,$0002        
730E: 96             SUB     (HL)            
730F: 02             LD      (BC),A          
7310: 02             LD      (BC),A          
7311: 00             NOP                     
7312: A3             AND     E               
7313: 04             INC     B               
7314: 02             LD      (BC),A          
7315: 00             NOP                     
7316: 97             SUB     A               
7317: A3             AND     E               
7318: 30 00          JR      NC,$731A        
731A: 03             INC     BC              
731B: 18 C7          JR      $72E4           
731D: DE 94          SBC     $94             
731F: 14             INC     D               
7320: 4B             LD      C,E             
7321: 5E             LD      E,(HL)          
7322: 83             ADD     A,E             
7323: 96             SUB     (HL)            
7324: FF             RST     0X38            
7325: 14             INC     D               
7326: 97             SUB     A               
7327: 9A             SBC     D               
7328: FB             EI                      
7329: 14             INC     D               
732A: D3 93          OUT     ($93),A         
732C: 54             LD      D,H             
732D: 59             LD      E,C             
732E: CC 83 91       CALL    Z,$9183         
7331: C5             PUSH    BC              
7332: FF             RST     0X38            
7333: 8B             ADC     A,E             
7334: 04             INC     B               
7335: 13             INC     DE              
7336: 0B             DEC     BC              
7337: 11 0A 03       LD      DE,$030A        
733A: 02             LD      (BC),A          
733B: 00             NOP                     
733C: A4             AND     H               
733D: 01 02 00       LD      BC,$0002        
7340: A2             AND     D               
7341: 02             LD      (BC),A          
7342: 02             LD      (BC),A          
7343: 00             NOP                     
7344: 96             SUB     (HL)            
7345: 04             INC     B               
7346: 02             LD      (BC),A          
7347: 00             NOP                     
7348: 97             SUB     A               
7349: A4             AND     H               
734A: 30 00          JR      NC,$734C        
734C: 03             INC     BC              
734D: 18 C7          JR      $7316           
734F: DE 94          SBC     $94             
7351: 14             INC     D               
7352: 4B             LD      C,E             
7353: 5E             LD      E,(HL)          
7354: 83             ADD     A,E             
7355: 96             SUB     (HL)            
7356: FB             EI                      
7357: 14             INC     D               
7358: D3 93          OUT     ($93),A         
735A: 54             LD      D,H             
735B: 59             LD      E,C             
735C: C6 83          ADD     $83             
735E: 9D             SBC     L               
735F: 61             LD      H,C             
7360: 4C             LD      C,H             
7361: 5E             LD      E,(HL)          
7362: 91             SUB     C               
7363: C5             PUSH    BC              
7364: FF             RST     0X38            
7365: 8B             ADC     A,E             
7366: 04             INC     B               
7367: 13             INC     DE              
7368: 0B             DEC     BC              
7369: 11 0A 03       LD      DE,$030A        
736C: 02             LD      (BC),A          
736D: 00             NOP                     
736E: A3             AND     E               
736F: 01 02 00       LD      BC,$0002        
7372: A2             AND     D               
7373: 02             LD      (BC),A          
7374: 02             LD      (BC),A          
7375: 00             NOP                     
7376: 96             SUB     (HL)            
7377: 04             INC     B               
7378: 02             LD      (BC),A          
7379: 00             NOP                     
737A: A3             AND     E               
737B: A5             AND     L               
737C: 2C             INC     L               
737D: 00             NOP                     
737E: 03             INC     BC              
737F: 20 C7          JR      NZ,$7348        
7381: DE 94          SBC     $94             
7383: 14             INC     D               
7384: 4B             LD      C,E             
7385: 5E             LD      E,(HL)          
7386: 96             SUB     (HL)            
7387: 96             SUB     (HL)            
7388: DB 72          IN      A,($72)         
738A: A5             AND     L               
738B: B7             OR      A               
738C: 76             HALT                    
738D: B1             OR      C               
738E: DB 16          IN      A,($16)         
7390: D3 B9          OUT     ($B9),A         
7392: 9B             SBC     E               
7393: 6C             LD      L,H             
7394: 23             INC     HL              
7395: D1             POP     DE              
7396: 13             INC     DE              
7397: 54             LD      D,H             
7398: E3             EX      (SP),HL         
7399: 8B             ADC     A,E             
739A: 0B             DEC     BC              
739B: 5C             LD      E,H             
739C: 95             SUB     L               
739D: 5F             LD      E,A             
739E: 9B             SBC     E               
739F: C1             POP     BC              
73A0: 04             INC     B               
73A1: 07             RLCA                    
73A2: 0B             DEC     BC              
73A3: 05             DEC     B               
73A4: 0A             LD      A,(BC)          
73A5: 03             INC     BC              
73A6: 02             LD      (BC),A          
73A7: 00             NOP                     
73A8: A6             AND     (HL)            
73A9: A6             AND     (HL)            
73AA: 50             LD      D,B             
73AB: 00             NOP                     
73AC: 03             INC     BC              
73AD: 2C             INC     L               
73AE: C7             RST     0X00            
73AF: DE 94          SBC     $94             
73B1: 14             INC     D               
73B2: 43             LD      B,E             
73B3: 5E             LD      E,(HL)          
73B4: 16 BC          LD      D,$BC           
73B6: DB 72          IN      A,($72)         
73B8: 8E             ADC     A,(HL)          
73B9: 61             LD      H,C             
73BA: B8             CP      B               
73BB: 16 82          LD      D,$82           
73BD: 17             RLA                     
73BE: 52             LD      D,D             
73BF: 5E             LD      E,(HL)          
73C0: 65             LD      H,L             
73C1: 49             LD      C,C             
73C2: 77             LD      (HL),A          
73C3: 47             LD      B,A             
73C4: 56             LD      D,(HL)          
73C5: F4 F4 72       CALL    P,$72F4         
73C8: 4B             LD      C,E             
73C9: 5E             LD      E,(HL)          
73CA: C3 B5 A9       JP      $A9B5           
73CD: 15             DEC     D               
73CE: DB 8B          IN      A,($8B)         
73D0: 83             ADD     A,E             
73D1: 7A             LD      A,D             
73D2: 5F             LD      E,A             
73D3: BE             CP      (HL)            
73D4: D7             RST     0X10            
73D5: 14             INC     D               
73D6: 43             LD      B,E             
73D7: 7A             LD      A,D             
73D8: CF             RST     0X08            
73D9: 98             SBC     B               
73DA: 04             INC     B               
73DB: 1F             RRA                     
73DC: 0B             DEC     BC              
73DD: 1D             DEC     E               
73DE: 0A             LD      A,(BC)          
73DF: 04             INC     B               
73E0: 02             LD      (BC),A          
73E1: 00             NOP                     
73E2: A5             AND     L               
73E3: 17             RLA                     
73E4: 05             DEC     B               
73E5: 0D             DEC     C               
73E6: 03             INC     BC              
73E7: 08             EX      AF,AF'          
73E8: 2C             INC     L               
73E9: 91             SUB     C               
73EA: 36 05          LD      (HL),$05        
73EC: 0D             DEC     C               
73ED: 03             INC     BC              
73EE: 08             EX      AF,AF'          
73EF: 2C             INC     L               
73F0: 91             SUB     C               
73F1: 37             SCF                     
73F2: 05             DEC     B               
73F3: 0D             DEC     C               
73F4: 03             INC     BC              
73F5: 08             EX      AF,AF'          
73F6: 2C             INC     L               
73F7: 91             SUB     C               
73F8: 33             INC     SP              
73F9: 01 91 00       LD      BC,$0091        
73FC: 87             ADD     A,A             
73FD: CF             RST     0X08            
73FE: 0E 87          LD      C,$87           
7400: CC 0D 2C       CALL    Z,$2C0D         
7403: 0E 08          LD      C,$08           
7405: 0A             LD      A,(BC)          
7406: 01 0A 02       LD      BC,$020A        
7409: 0A             LD      A,(BC)          
740A: 03             INC     BC              
740B: 0A             LD      A,(BC)          
740C: 04             INC     B               
740D: 0E 20          LD      C,$20           
740F: 13             INC     DE              
7410: 0D             DEC     C               
7411: 1D             DEC     E               
7412: 04             INC     B               
7413: 19             ADD     HL,DE           
7414: 5F             LD      E,A             
7415: BE             CP      (HL)            
7416: 5B             LD      E,E             
7417: B1             OR      C               
7418: 4B             LD      C,E             
7419: 7B             LD      A,E             
741A: EB             EX      DE,HL           
741B: 99             SBC     C               
741C: 1B             DEC     DE              
741D: D0             RET     NC              
741E: 89             ADC     A,C             
741F: 17             RLA                     
7420: 81             ADD     A,C             
7421: 15             DEC     D               
7422: 82             ADD     A,D             
7423: 17             RLA                     
7424: 73             LD      (HL),E          
7425: 49             LD      C,C             
7426: 94             SUB     H               
7427: 5A             LD      E,D             
7428: E6 5F          AND     $5F             
742A: C0             RET     NZ              
742B: 7A             LD      A,D             
742C: 2E 20          LD      L,$20           
742E: 1D             DEC     E               
742F: 0B             DEC     BC              
7430: 87             ADD     A,A             
7431: 97             SUB     A               
7432: 0A             LD      A,(BC)          
7433: 05             DEC     B               
7434: 21 0E 1F       LD      HL,$1F0E        
7437: 0D             DEC     C               
7438: 19             ADD     HL,DE           
7439: 1A             LD      A,(DE)          
743A: 18 04          JR      $7440           
743C: 13             INC     DE              
743D: C7             RST     0X00            
743E: DE 94          SBC     $94             
7440: 14             INC     D               
7441: 43             LD      B,E             
7442: 5E             LD      E,(HL)          
7443: EF             RST     0X28            
7444: 8D             ADC     A,L             
7445: 13             INC     DE              
7446: 47             LD      B,A             
7447: D3 14          OUT     ($14),A         
7449: 83             ADD     A,E             
744A: B3             OR      E               
744B: 91             SUB     C               
744C: 7A             LD      A,D             
744D: 82             ADD     A,D             
744E: 17             RLA                     
744F: 45             LD      B,L             
7450: 16 84          LD      D,$84           
7452: 13             INC     DE              
7453: 83             ADD     A,E             
7454: 14             INC     D               
7455: 0C             INC     C               
7456: 06 0C          LD      B,$0C           
7458: 0D             DEC     C               
7459: 0A             LD      A,(BC)          
745A: 1A             LD      A,(DE)          
745B: 10 04          DJNZ    $7461           
745D: 06 F9          LD      B,$F9           
745F: 5B             LD      E,E             
7460: 9F             SBC     A               
7461: A6             AND     (HL)            
7462: 9B             SBC     E               
7463: 5D             LD      E,L             
7464: 08             EX      AF,AF'          
7465: 17             RLA                     
7466: 0E 15          LD      C,$15           
7468: 13             INC     DE              
7469: 0D             DEC     C               
746A: 12             LD      (DE),A          
746B: 04             INC     B               
746C: 0E 89          LD      C,$89           
746E: 74             LD      (HL),H          
746F: D3 14          OUT     ($14),A         
7471: 9B             SBC     E               
7472: 96             SUB     (HL)            
7473: 1B             DEC     DE              
7474: A1             AND     C               
7475: 63             LD      H,E             
7476: B1             OR      C               
7477: 16 58          LD      D,$58           
7479: DB 72          IN      A,($72)         
747B: 11 84 11       LD      DE,$1184        
747E: 16 0E          LD      D,$0E           
7480: 14             INC     D               
7481: 13             INC     DE              
7482: 0D             DEC     C               
7483: 11 04 0D       LD      DE,$0D04        
7486: EB             EX      DE,HL           
7487: 99             SBC     C               
7488: 0F             RRCA                    
7489: A0             AND     B               
748A: D3 14          OUT     ($14),A         
748C: 91             SUB     C               
748D: 96             SUB     (HL)            
748E: F0             RET     P               
748F: A4             AND     H               
7490: 82             ADD     A,D             
7491: 17             RLA                     
7492: 45             LD      B,L             
7493: 11 84 12       LD      DE,$1284        
7496: 21 0E 1F       LD      HL,$1F0E        
7499: 13             INC     DE              
749A: 0D             DEC     C               
749B: 1C             INC     E               
749C: 04             INC     B               
749D: 13             INC     DE              
749E: 33             INC     SP              
749F: D1             POP     DE              
74A0: 09             ADD     HL,BC           
74A1: 15             DEC     D               
74A2: E6 96          AND     $96             
74A4: 51             LD      D,C             
74A5: 18 4E          JR      $74F5           
74A7: C2 98 5F       JP      NZ,$5F98        
74AA: 56             LD      D,(HL)          
74AB: 5E             LD      E,(HL)          
74AC: DB 72          IN      A,($72)         
74AE: 81             ADD     A,C             
74AF: A6             AND     (HL)            
74B0: 52             LD      D,D             
74B1: 11 04 04       LD      DE,$0404        
74B4: 49             LD      C,C             
74B5: 48             LD      C,B             
74B6: 7F             LD      A,A             
74B7: 98             SBC     B               
74B8: 09             ADD     HL,BC           
74B9: 81             ADD     A,C             
74BA: 37             SCF                     
74BB: 0E 81          LD      C,$81           
74BD: 34             INC     (HL)            
74BE: 14             INC     D               
74BF: 1B             DEC     DE              
74C0: 14             INC     D               
74C1: 0E 03          LD      C,$03           
74C3: 09             ADD     HL,BC           
74C4: 17             RLA                     
74C5: 83             ADD     A,E             
74C6: 0E 81          LD      C,$81           
74C8: 29             ADD     HL,HL           
74C9: 0D             DEC     C               
74CA: 1F             RRA                     
74CB: 14             INC     D               
74CC: 15             DEC     D               
74CD: 40             LD      B,B             
74CE: 14             INC     D               
74CF: 09             ADD     HL,BC           
74D0: 17             RLA                     
74D1: 04             INC     B               
74D2: 0C             INC     C               
74D3: C7             RST     0X00            
74D4: DE D3          SBC     $D3             
74D6: 14             INC     D               
74D7: E6 96          AND     $96             
74D9: AF             XOR     A               
74DA: 15             DEC     D               
74DB: B3             OR      E               
74DC: B3             OR      E               
74DD: 5F             LD      E,A             
74DE: BE             CP      (HL)            
74DF: 11 04 06       LD      DE,$0604        
74E2: 56             LD      D,(HL)          
74E3: D1             POP     DE              
74E4: 16 71          LD      D,$71           
74E6: DB 72          IN      A,($72)         
74E8: 12             LD      (DE),A          
74E9: 84             ADD     A,H             
74EA: 13             INC     DE              
74EB: 0D             DEC     C               
74EC: 1A             LD      A,(DE)          
74ED: 1A             LD      A,(DE)          
74EE: 14             INC     D               
74EF: 15             DEC     D               
74F0: 10 04          DJNZ    $74F6           
74F2: 12             LD      (DE),A          
74F3: 73             LD      (HL),E          
74F4: 7B             LD      A,E             
74F5: 77             LD      (HL),A          
74F6: 5B             LD      E,E             
74F7: D0             RET     NC              
74F8: B5             OR      L               
74F9: C9             RET                     
74FA: 9C             SBC     H               
74FB: 36 A0          LD      (HL),$A0        
74FD: 89             ADC     A,C             
74FE: 17             RLA                     
74FF: 96             SUB     (HL)            
7500: 14             INC     D               
7501: 45             LD      B,L             
7502: BD             CP      L               
7503: C3 83 11       JP      $1183           
7506: 84             ADD     A,H             
7507: 0D             DEC     C               
7508: 80             ADD     A,B             
7509: D7             RST     0X10            
750A: 1A             LD      A,(DE)          
750B: 0B             DEC     BC              
750C: 80             ADD     A,B             
750D: D3 09          OUT     ($09),A         
750F: 09             ADD     HL,BC           
7510: 80             ADD     A,B             
7511: 99             SBC     C               
7512: 0B             DEC     BC              
7513: 80             ADD     A,B             
7514: 96             SUB     (HL)            
7515: 05             DEC     B               
7516: 52             LD      D,D             
7517: 28 0D          JR      Z,$7526         
7519: 26 04          LD      H,$04           
751B: 17             RLA                     
751C: 4F             LD      C,A             
751D: 45             LD      B,L             
751E: 7A             LD      A,D             
751F: 79             LD      A,C             
7520: FB             EI                      
7521: C0             RET     NZ              
7522: 6C             LD      L,H             
7523: BE             CP      (HL)            
7524: 66             LD      H,(HL)          
7525: C6 04          ADD     $04             
7527: EE 73          XOR     $73             
7529: C6 73          ADD     $73             
752B: 7B             LD      A,E             
752C: D5             PUSH    DE              
752D: 92             SUB     D               
752E: B5             OR      L               
752F: B7             OR      A               
7530: 82             ADD     A,D             
7531: 17             RLA                     
7532: 45             LD      B,L             
7533: 16 04          LD      D,$04           
7535: 0A             LD      A,(BC)          
7536: 7B             LD      A,E             
7537: 50             LD      D,B             
7538: 4D             LD      C,L             
7539: 45             LD      B,L             
753A: 49             LD      C,C             
753B: 7A             LD      A,D             
753C: 36 92          LD      (HL),$92        
753E: 21 62 A4       LD      HL,$A462        
7541: 2D             DEC     L               
7542: 0D             DEC     C               
7543: 2B             DEC     HL              
7544: 04             INC     B               
7545: 1C             INC     E               
7546: 89             ADC     A,C             
7547: 4E             LD      C,(HL)          
7548: 73             LD      (HL),E          
7549: 9E             SBC     (HL)            
754A: F5             PUSH    AF              
754B: B3             OR      E               
754C: F5             PUSH    AF              
754D: 72             LD      (HL),D          
754E: 59             LD      E,C             
754F: 15             DEC     D               
7550: C2 B3 95       JP      NZ,$95B3        
7553: 14             INC     D               
7554: 51             LD      D,C             
7555: 18 4A          JR      $75A1           
7557: C2 CF 49       JP      NZ,$49CF        
755A: 5E             LD      E,(HL)          
755B: 17             RLA                     
755C: 5A             LD      E,D             
755D: 49             LD      C,C             
755E: F3             DI                      
755F: 5F             LD      E,A             
7560: 5F             LD      E,A             
7561: BE             CP      (HL)            
7562: 16 04          LD      D,$04           
7564: 08             EX      AF,AF'          
7565: 83             ADD     A,E             
7566: 7A             LD      A,D             
7567: 5F             LD      E,A             
7568: BE             CP      (HL)            
7569: 94             SUB     H               
756A: 14             INC     D               
756B: EB             EX      DE,HL           
756C: 8F             ADC     A,A             
756D: 1D             DEC     E               
756E: 0A             LD      A,(BC)          
756F: FD 20 0D       JR      NZ,$757E        
7572: 1E 04          LD      E,$04           
7574: 1A             LD      A,(DE)          
7575: C7             RST     0X00            
7576: DE 63          SBC     $63             
7578: 16 C9          LD      D,$C9           
757A: 97             SUB     A               
757B: 43             LD      B,E             
757C: 5E             LD      E,(HL)          
757D: 84             ADD     A,H             
757E: 15             DEC     D               
757F: 73             LD      (HL),E          
7580: 4A             LD      C,D             
7581: AB             XOR     E               
7582: 98             SBC     B               
7583: 89             ADC     A,C             
7584: 4E             LD      C,(HL)          
7585: D6 CE          SUB     $CE             
7587: D6 9C          SUB     $9C             
7589: DB 72          IN      A,($72)         
758B: 1F             RRA                     
758C: 54             LD      D,H             
758D: F1             POP     AF              
758E: B9             CP      C               
758F: 1D             DEC     E               
7590: 14             INC     D               
7591: FF             RST     0X38            
7592: 18 0D          JR      $75A1           
7594: 16 04          LD      D,$04           
7596: 12             LD      (DE),A          
7597: 4E             LD      C,(HL)          
7598: 45             LD      B,L             
7599: DD             ???                     
759A: C3 44 DB       JP      $DB44           
759D: 89             ADC     A,C             
759E: 8D             ADC     A,L             
759F: 89             ADC     A,C             
75A0: 17             RLA                     
75A1: 82             ADD     A,D             
75A2: 17             RLA                     
75A3: 4A             LD      C,D             
75A4: 5E             LD      E,(HL)          
75A5: 94             SUB     H               
75A6: 5F             LD      E,A             
75A7: AB             XOR     E               
75A8: BB             CP      E               
75A9: 1D             DEC     E               
75AA: FF             RST     0X38            
75AB: 17             RLA                     
75AC: 34             INC     (HL)            
75AD: 0B             DEC     BC              
75AE: 32 05 AF       LD      ($AF05),A       
75B1: 14             INC     D               
75B2: 04             INC     B               
75B3: 12             LD      (DE),A          
75B4: 59             LD      E,C             
75B5: 45             LD      B,L             
75B6: 3E 7A          LD      A,$7A           
75B8: EF             RST     0X28            
75B9: 16 1A          LD      D,$1A           
75BB: 98             SBC     B               
75BC: 90             SUB     B               
75BD: 14             INC     D               
75BE: 1B             DEC     DE              
75BF: 58             LD      E,B             
75C0: 1B             DEC     DE              
75C1: A1             AND     C               
75C2: D5             PUSH    DE              
75C3: 92             SUB     D               
75C4: 5B             LD      E,E             
75C5: BB             CP      E               
75C6: FF             RST     0X38            
75C7: 19             ADD     HL,DE           
75C8: 0D             DEC     C               
75C9: 17             RLA                     
75CA: 04             INC     B               
75CB: 13             INC     DE              
75CC: C7             RST     0X00            
75CD: DE EF          SBC     $EF             
75CF: 16 1A          LD      D,$1A           
75D1: 98             SBC     B               
75D2: F3             DI                      
75D3: 5F             LD      E,A             
75D4: 8F             ADC     A,A             
75D5: 73             LD      (HL),E          
75D6: D0             RET     NC              
75D7: 15             DEC     D               
75D8: 82             ADD     A,D             
75D9: 17             RLA                     
75DA: 4A             LD      C,D             
75DB: 5E             LD      E,(HL)          
75DC: 86             ADD     A,(HL)          
75DD: 5F             LD      E,A             
75DE: 21 1D 03       LD      HL,$031D        
75E1: 0D             DEC     C               
75E2: 0F             RRCA                    
75E3: 04             INC     B               
75E4: 02             LD      (BC),A          
75E5: 5F             LD      E,A             
75E6: BE             CP      (HL)            
75E7: 11 04 08       LD      DE,$0804        
75EA: 4B             LD      C,E             
75EB: 7B             LD      A,E             
75EC: 92             SUB     D               
75ED: C5             PUSH    BC              
75EE: 37             SCF                     
75EF: 49             LD      C,C             
75F0: 17             RLA                     
75F1: 60             LD      H,B             
75F2: 0A             LD      A,(BC)          
75F3: 01 07 15       LD      BC,$1507        
75F6: 29             ADD     HL,HL           
75F7: 0E 27          LD      C,$27           
75F9: 13             INC     DE              
75FA: 0D             DEC     C               
75FB: 24             INC     H               
75FC: 04             INC     B               
75FD: 0D             DEC     C               
75FE: 80             ADD     A,B             
75FF: 5B             LD      E,E             
7600: F3             DI                      
7601: 23             INC     HL              
7602: 5B             LD      E,E             
7603: 4D             LD      C,L             
7604: 4E             LD      C,(HL)          
7605: B8             CP      B               
7606: F9             LD      SP,HL           
7607: 8E             ADC     A,(HL)          
7608: 82             ADD     A,D             
7609: 17             RLA                     
760A: 45             LD      B,L             
760B: 11 04 12       LD      DE,$1204        
760E: 47             LD      B,A             
760F: D2 C8 8B       JP      NC,$8BC8        
7612: F3             DI                      
7613: 23             INC     HL              
7614: 55             LD      D,L             
7615: BD             CP      L               
7616: DB BD          IN      A,($BD)         
7618: 41             LD      B,C             
7619: 6E             LD      L,(HL)          
761A: 03             INC     BC              
761B: 58             LD      E,B             
761C: 99             SBC     C               
761D: 9B             SBC     E               
761E: 5F             LD      E,A             
761F: 4A             LD      C,D             
7620: 17             RLA                     
7621: 51             LD      D,C             
7622: 0E 4F          LD      C,$4F           
7624: 13             INC     DE              
7625: 0D             DEC     C               
7626: 25             DEC     H               
7627: 1A             LD      A,(DE)          
7628: 15             DEC     D               
7629: 10 04          DJNZ    $762F           
762B: 0C             INC     C               
762C: 46             LD      B,(HL)          
762D: 77             LD      (HL),A          
762E: 05             DEC     B               
762F: A0             AND     B               
7630: 16 BC          LD      D,$BC           
7632: 90             SUB     B               
7633: 73             LD      (HL),E          
7634: D6 83          SUB     $83             
7636: DB 72          IN      A,($72)         
7638: 11 04 11       LD      DE,$1104        
763B: 4E             LD      C,(HL)          
763C: D1             POP     DE              
763D: 15             DEC     D               
763E: 8A             ADC     A,D             
763F: 50             LD      D,B             
7640: BD             CP      L               
7641: 15             DEC     D               
7642: 58             LD      E,B             
7643: 8E             ADC     A,(HL)          
7644: BE             CP      (HL)            
7645: 08             EX      AF,AF'          
7646: 8A             ADC     A,D             
7647: BE             CP      (HL)            
7648: A0             AND     B               
7649: 56             LD      D,(HL)          
764A: 72             LD      (HL),D          
764B: 2E 0D          LD      L,$0D           
764D: 25             DEC     H               
764E: 04             INC     B               
764F: 12             LD      (DE),A          
7650: CF             RST     0X08            
7651: 62             LD      H,D             
7652: 8B             ADC     A,E             
7653: 96             SUB     (HL)            
7654: 9B             SBC     E               
7655: 64             LD      H,H             
7656: 1B             DEC     DE              
7657: A1             AND     C               
7658: 47             LD      B,A             
7659: 55             LD      D,L             
765A: B3             OR      E               
765B: 8B             ADC     A,E             
765C: C3 54 A3       JP      $A354           
765F: 91             SUB     C               
7660: 5F             LD      E,A             
7661: BE             CP      (HL)            
7662: 11 04 0E       LD      DE,$0E04        
7665: 73             LD      (HL),E          
7666: 7B             LD      A,E             
7667: 47             LD      B,A             
7668: D2 C8 8B       JP      NC,$8BC8        
766B: F3             DI                      
766C: 23             INC     HL              
766D: EE 72          XOR     $72             
766F: 1B             DEC     DE              
7670: A3             AND     E               
7671: 3F             CCF                     
7672: A1             AND     C               
7673: 16 16          LD      D,$16           
7675: 0E 14          LD      C,$14           
7677: 13             INC     DE              
7678: 0D             DEC     C               
7679: 11 04 02       LD      DE,$0204        
767C: 5F             LD      E,A             
767D: BE             CP      (HL)            
767E: 11 04 0A       LD      DE,$0A04        
7681: 4B             LD      C,E             
7682: 7B             LD      A,E             
7683: 06 9A          LD      B,$9A           
7685: BF             CP      A               
7686: 14             INC     D               
7687: D3 B2          OUT     ($B2),A         
7689: CF             RST     0X08            
768A: 98             SBC     B               
768B: 18 35          JR      $76C2           
768D: 0E 33          LD      C,$33           
768F: 13             INC     DE              
7690: 0D             DEC     C               
7691: 18 1A          JR      $76AD           
7693: 15             DEC     D               
7694: 10 04          DJNZ    $769A           
7696: 11 5B BE       LD      DE,$BE5B        
7699: 65             LD      H,L             
769A: BC             CP      H               
769B: 99             SBC     C               
769C: 16 F3          LD      D,$F3           
769E: 17             RLA                     
769F: 56             LD      D,(HL)          
76A0: DB CA          IN      A,($CA)         
76A2: 9C             SBC     H               
76A3: 3E C6          LD      A,$C6           
76A5: 82             ADD     A,D             
76A6: 17             RLA                     
76A7: 45             LD      B,L             
76A8: 16 84          LD      D,$84           
76AA: 0D             DEC     C               
76AB: 16 04          LD      D,$04           
76AD: 02             LD      (BC),A          
76AE: 5F             LD      E,A             
76AF: BE             CP      (HL)            
76B0: 11 04 0F       LD      DE,$0F04        
76B3: 81             ADD     A,C             
76B4: 8D             ADC     A,L             
76B5: CB 87          RES     0,A             
76B7: A5             AND     L               
76B8: 94             SUB     H               
76B9: 04             INC     B               
76BA: 71             LD      (HL),C          
76BB: 8E             ADC     A,(HL)          
76BC: 62             LD      H,D             
76BD: 23             INC     HL              
76BE: 62             LD      H,D             
76BF: 09             ADD     HL,BC           
76C0: 9A             SBC     D               
76C1: 2E 0B          LD      L,$0B           
76C3: 3A 0E 38       LD      A,($380E)       
76C6: 13             INC     DE              
76C7: 0D             DEC     C               
76C8: 19             ADD     HL,DE           
76C9: 1A             LD      A,(DE)          
76CA: 15             DEC     D               
76CB: 04             INC     B               
76CC: 04             INC     B               
76CD: 12             LD      (DE),A          
76CE: 3F             CCF                     
76CF: B9             CP      C               
76D0: 82             ADD     A,D             
76D1: 62             LD      H,D             
76D2: 91             SUB     C               
76D3: 7A             LD      A,D             
76D4: D5             PUSH    DE              
76D5: 15             DEC     D               
76D6: 04             INC     B               
76D7: 18 8E          JR      $7667           
76D9: 7B             LD      A,E             
76DA: 83             ADD     A,E             
76DB: 61             LD      H,C             
76DC: 03             INC     BC              
76DD: A0             AND     B               
76DE: 5F             LD      E,A             
76DF: BE             CP      (HL)            
76E0: 16 84          LD      D,$84           
76E2: 0D             DEC     C               
76E3: 1A             LD      A,(DE)          
76E4: 04             INC     B               
76E5: 16 5F          LD      D,$5F           
76E7: BE             CP      (HL)            
76E8: 5D             LD      E,L             
76E9: B1             OR      C               
76EA: D0             RET     NC              
76EB: B5             OR      L               
76EC: 02             LD      (BC),A          
76ED: A1             AND     C               
76EE: 91             SUB     C               
76EF: 7A             LD      A,D             
76F0: 62             LD      H,D             
76F1: 17             RLA                     
76F2: DB 5F          IN      A,($5F)         
76F4: 33             INC     SP              
76F5: 48             LD      C,B             
76F6: B9             CP      C               
76F7: 46             LD      B,(HL)          
76F8: 73             LD      (HL),E          
76F9: C6 5F          ADD     $5F             
76FB: BE             CP      (HL)            
76FC: 11 84 0C       LD      DE,$0C84        
76FF: 1A             LD      A,(DE)          
7700: 0E 18          LD      C,$18           
7702: 13             INC     DE              
7703: 0D             DEC     C               
7704: 15             DEC     D               
7705: 04             INC     B               
7706: 11 5F BE       LD      DE,$BE5F        
7709: 5D             LD      E,L             
770A: B1             OR      C               
770B: D0             RET     NC              
770C: B5             OR      L               
770D: 02             LD      (BC),A          
770E: A1             AND     C               
770F: 91             SUB     C               
7710: 7A             LD      A,D             
7711: B0             OR      B               
7712: 17             RLA                     
7713: F4 59 82       CALL    P,$8259         
7716: 17             RLA                     
7717: 45             LD      B,L             
7718: 11 84 10       LD      DE,$1084        
771B: 18 0E          JR      $772B           
771D: 16 13          LD      D,$13           
771F: 0D             DEC     C               
7720: 13             INC     DE              
7721: 04             INC     B               
7722: 0F             RRCA                    
7723: 5F             LD      E,A             
7724: BE             CP      (HL)            
7725: 5D             LD      E,L             
7726: B1             OR      C               
7727: D0             RET     NC              
7728: B5             OR      L               
7729: 02             LD      (BC),A          
772A: A1             AND     C               
772B: 91             SUB     C               
772C: 7A             LD      A,D             
772D: D0             RET     NC              
772E: 15             DEC     D               
772F: 82             ADD     A,D             
7730: 17             RLA                     
7731: 45             LD      B,L             
7732: 11 84 1B       LD      DE,$1B84        
7735: 20 0E          JR      NZ,$7745        
7737: 1E 13          LD      E,$13           
7739: 0D             DEC     C               
773A: 03             INC     BC              
773B: 08             EX      AF,AF'          
773C: 00             NOP                     
773D: 07             RLCA                    
773E: 0D             DEC     C               
773F: 16 04          LD      D,$04           
7741: 12             LD      (DE),A          
7742: 5F             LD      E,A             
7743: BE             CP      (HL)            
7744: 5B             LD      E,E             
7745: B1             OR      C               
7746: 4B             LD      C,E             
7747: 7B             LD      A,E             
7748: 06 9A          LD      B,$9A           
774A: 90             SUB     B               
774B: 73             LD      (HL),E          
774C: C3 6A 07       JP      $076A           
774F: B3             OR      E               
7750: 33             INC     SP              
7751: 98             SBC     B               
7752: 5F             LD      E,A             
7753: BE             CP      (HL)            
7754: 11 84 1C       LD      DE,$1C84        
7757: 34             INC     (HL)            
7758: 0E 32          LD      C,$32           
775A: 13             INC     DE              
775B: 0D             DEC     C               
775C: 17             RLA                     
775D: 08             EX      AF,AF'          
775E: 00             NOP                     
775F: 04             INC     B               
7760: 13             INC     DE              
7761: 5F             LD      E,A             
7762: BE             CP      (HL)            
7763: 5B             LD      E,E             
7764: B1             OR      C               
7765: 4B             LD      C,E             
7766: 7B             LD      A,E             
7767: 06 9A          LD      B,$9A           
7769: 90             SUB     B               
776A: 73             LD      (HL),E          
776B: C4 6A A3       CALL    NZ,$A36A        
776E: 60             LD      H,B             
776F: 33             INC     SP              
7770: 98             SBC     B               
7771: C7             RST     0X00            
7772: DE 2E          SBC     $2E             
7774: 0D             DEC     C               
7775: 16 04          LD      D,$04           
7777: 12             LD      (DE),A          
7778: 5F             LD      E,A             
7779: BE             CP      (HL)            
777A: 5B             LD      E,E             
777B: B1             OR      C               
777C: 4B             LD      C,E             
777D: 7B             LD      A,E             
777E: 06 9A          LD      B,$9A           
7780: 90             SUB     B               
7781: 73             LD      (HL),E          
7782: C4 6A A3       CALL    NZ,$A36A        
7785: 60             LD      H,B             
7786: 33             INC     SP              
7787: 98             SBC     B               
7788: 5F             LD      E,A             
7789: BE             CP      (HL)            
778A: 11 84 1D       LD      DE,$1D84        
778D: 16 04          LD      D,$04           
778F: 14             INC     D               
7790: 9F             SBC     A               
7791: 77             LD      (HL),A          
7792: AF             XOR     A               
7793: 14             INC     D               
7794: 91             SUB     C               
7795: 7A             LD      A,D             
7796: 95             SUB     L               
7797: 14             INC     D               
7798: D3 14          OUT     ($14),A         
779A: 68             LD      L,B             
779B: B1             OR      C               
779C: 33             INC     SP              
779D: C5             PUSH    BC              
779E: 4B             LD      C,E             
779F: 49             LD      C,C             
77A0: 45             LD      B,L             
77A1: 77             LD      (HL),A          
77A2: 81             ADD     A,C             
77A3: 48             LD      C,B             
77A4: 1E 04          LD      E,$04           
77A6: 04             INC     B               
77A7: 02             LD      (BC),A          
77A8: E9             JP      (HL)            
77A9: 99             SBC     C               
77AA: 1F             RRA                     
77AB: 05             DEC     B               
77AC: 04             INC     B               
77AD: 03             INC     BC              
77AE: 35             DEC     (HL)            
77AF: DD 21 21 0A    LD      IX,$0A21        
77B3: 04             INC     B               
77B4: 08             EX      AF,AF'          
77B5: B5             OR      L               
77B6: 6C             LD      L,H             
77B7: 8E             ADC     A,(HL)          
77B8: C5             PUSH    BC              
77B9: EB             EX      DE,HL           
77BA: 72             LD      (HL),D          
77BB: AB             XOR     E               
77BC: BB             CP      E               
77BD: 22 12 04       LD      ($0412),HL      
77C0: 10 5B          DJNZ    $781D           
77C2: E0             RET     PO              
77C3: 27             DAA                     
77C4: 60             LD      H,B             
77C5: 31 60 41       LD      SP,$4160        
77C8: A0             AND     B               
77C9: 49             LD      C,C             
77CA: A0             AND     B               
77CB: 89             ADC     A,C             
77CC: D3 89          OUT     ($89),A         
77CE: D3 69          OUT     ($69),A         
77D0: CE 23          ADC     $23             
77D2: 05             DEC     B               
77D3: 0D             DEC     C               
77D4: 03             INC     BC              
77D5: 92             SUB     D               
77D6: 26 24          LD      H,$24           
77D8: 2C             INC     L               
77D9: 04             INC     B               
77DA: 0D             DEC     C               
77DB: 02             LD      (BC),A          
77DC: 92             SUB     D               
77DD: 26 3E          LD      H,$3E           
77DF: 01 27 3F       LD      BC,$3F27        
77E2: 01 28 25       LD      BC,$2528        
77E5: 20 04          JR      NZ,$77EB        
77E7: 1E C7          LD      E,$C7           
77E9: DE AF          SBC     $AF             
77EB: 23             INC     HL              
77EC: 99             SBC     C               
77ED: 16 09          LD      D,$09           
77EF: BC             CP      H               
77F0: 8E             ADC     A,(HL)          
77F1: 62             LD      H,D             
77F2: 91             SUB     C               
77F3: 7A             LD      A,D             
77F4: 90             SUB     B               
77F5: 14             INC     D               
77F6: FA DF 2F       JP      M,$2FDF         
77F9: 62             LD      H,D             
77FA: 16 EE          LD      D,$EE           
77FC: 7B             LD      A,E             
77FD: B4             OR      H               
77FE: 46             LD      B,(HL)          
77FF: 45             LD      B,L             
7800: 2F             CPL                     
7801: 7B             LD      A,E             
7802: 03             INC     BC              
7803: 56             LD      D,(HL)          
7804: 27             DAA                     
7805: A0             AND     B               
7806: 26 24          LD      H,$24           
7808: 0E 22          LD      C,$22           
780A: 13             INC     DE              
780B: 0D             DEC     C               
780C: 17             RLA                     
780D: 1A             LD      A,(DE)          
780E: 15             DEC     D               
780F: 10 04          DJNZ    $7815           
7811: 02             LD      (BC),A          
7812: 5F             LD      E,A             
7813: BE             CP      (HL)            
7814: 11 04 0D       LD      DE,$0D04        
7817: 40             LD      B,B             
7818: D2 F3 23       JP      NC,$23F3        
781B: F6 8B          OR      $8B             
781D: 51             LD      D,C             
781E: 18 52          JR      $7872           
7820: C2 65 49       JP      NZ,$4965        
7823: 21 04 06       LD      HL,$0604        
7826: 09             ADD     HL,BC           
7827: 9A             SBC     D               
7828: FA 17 70       JP      M,$7017         
782B: 49             LD      C,C             
782C: 3D             DEC     A               
782D: 01 94 27       LD      BC,$2794        
7830: 0E 0E          LD      C,$0E           
7832: 0C             INC     C               
7833: 13             INC     DE              
7834: 04             INC     B               
7835: 09             ADD     HL,BC           
7836: 25             DEC     H               
7837: A1             AND     C               
7838: AB             XOR     E               
7839: 70             LD      (HL),B          
783A: 3B             DEC     SP              
783B: 95             SUB     L               
783C: 77             LD      (HL),A          
783D: BF             CP      A               
783E: 21 28 40       LD      HL,$4028        
7841: 0E 3E          LD      C,$3E           
7843: 13             INC     DE              
7844: 0D             DEC     C               
7845: 1D             DEC     E               
7846: 1A             LD      A,(DE)          
7847: 15             DEC     D               
7848: 10 04          DJNZ    $784E           
784A: 18 5B          JR      $78A7           
784C: BE             CP      (HL)            
784D: 65             LD      H,L             
784E: BC             CP      H               
784F: 7B             LD      A,E             
7850: 14             INC     D               
7851: 41             LD      B,C             
7852: 6E             LD      L,(HL)          
7853: 19             ADD     HL,DE           
7854: 58             LD      E,B             
7855: 3B             DEC     SP              
7856: 4A             LD      C,D             
7857: 6B             LD      L,E             
7858: BF             CP      A               
7859: 85             ADD     A,L             
785A: 8D             ADC     A,L             
785B: 5B             LD      E,E             
785C: 5E             LD      E,(HL)          
785D: 34             INC     (HL)            
785E: A1             AND     C               
785F: 9B             SBC     E               
7860: 15             DEC     D               
7861: 31 98 0D       LD      SP,$0D98        
7864: 1C             INC     E               
7865: 04             INC     B               
7866: 10 80          DJNZ    $77E8           
7868: 5B             LD      E,E             
7869: F3             DI                      
786A: 23             INC     HL              
786B: C7             RST     0X00            
786C: DE 20          SBC     $20             
786E: 16 6B          LD      D,$6B           
7870: A1             AND     C               
7871: 5B             LD      E,E             
7872: BE             CP      (HL)            
7873: 16 BC          LD      D,$BC           
7875: DB 72          IN      A,($72)         
7877: 11 04 07       LD      DE,$0704        
787A: 10 53          DJNZ    $78CF           
787C: F3             DI                      
787D: 23             INC     HL              
787E: 96             SUB     (HL)            
787F: 5F             LD      E,A             
7880: 21 29 38       LD      HL,$3829        
7883: 0E 36          LD      C,$36           
7885: 13             INC     DE              
7886: 0D             DEC     C               
7887: 18 1B          JR      $78A4           
7889: 15             DEC     D               
788A: 10 04          DJNZ    $7890           
788C: 02             LD      (BC),A          
788D: 5F             LD      E,A             
788E: BE             CP      (HL)            
788F: 12             LD      (DE),A          
7890: 04             INC     B               
7891: 0E 47          LD      C,$47           
7893: D2 B3 8B       JP      NC,$8BB3        
7896: D6 B0          SUB     $B0             
7898: F4 72 23       CALL    P,$2372         
789B: 15             DEC     D               
789C: 1B             DEC     DE              
789D: BC             CP      H               
789E: 19             ADD     HL,DE           
789F: A1             AND     C               
78A0: 0D             DEC     C               
78A1: 19             ADD     HL,DE           
78A2: 04             INC     B               
78A3: 17             RLA                     
78A4: 43             LD      B,E             
78A5: 79             LD      A,C             
78A6: C7             RST     0X00            
78A7: DE D3          SBC     $D3             
78A9: 14             INC     D               
78AA: 88             ADC     A,B             
78AB: 96             SUB     (HL)            
78AC: 8E             ADC     A,(HL)          
78AD: 7A             LD      A,D             
78AE: 7B             LD      A,E             
78AF: 14             INC     D               
78B0: C7             RST     0X00            
78B1: 93             SUB     E               
78B2: 76             HALT                    
78B3: BE             CP      (HL)            
78B4: BD             CP      L               
78B5: 15             DEC     D               
78B6: 49             LD      C,C             
78B7: 90             SUB     B               
78B8: 67             LD      H,A             
78B9: 48             LD      C,B             
78BA: 21 2A 0F       LD      HL,$0F2A        
78BD: 04             INC     B               
78BE: 0D             DEC     C               
78BF: FF             RST     0X38            
78C0: A5             AND     L               
78C1: 57             LD      D,A             
78C2: 49             LD      C,C             
78C3: AF             XOR     A               
78C4: 14             INC     D               
78C5: 62             LD      H,D             
78C6: 17             RLA                     
78C7: DB 5F          IN      A,($5F)         
78C9: 05             DEC     B               
78CA: 67             LD      H,A             
78CB: 2E 2F          LD      L,$2F           
78CD: 07             RLCA                    
78CE: 04             INC     B               
78CF: 05             DEC     B               
78D0: 9B             SBC     E               
78D1: 29             ADD     HL,HL           
78D2: 57             LD      D,A             
78D3: C6 3E          ADD     $3E             
78D5: 31 17 04       LD      SP,$0417        
78D8: 15             DEC     D               
78D9: 36 9F          LD      (HL),$9F        
78DB: D6 15          SUB     $15             
78DD: CB 23          SLA     E               
78DF: 39             ADD     HL,SP           
78E0: 49             LD      C,C             
78E1: 8E             ADC     A,(HL)          
78E2: C5             PUSH    BC              
78E3: 9F             SBC     A               
78E4: 15             DEC     D               
78E5: 5B             LD      E,E             
78E6: B1             OR      C               
78E7: 3F             CCF                     
78E8: B9             CP      C               
78E9: FA 62 2F       JP      M,$2F62         
78EC: 62             LD      H,D             
78ED: 2E 2D          LD      L,$2D           
78EF: 09             ADD     HL,BC           
78F0: 0E 07          LD      C,$07           
78F2: 13             INC     DE              
78F3: 0D             DEC     C               
78F4: 02             LD      (BC),A          
78F5: 1A             LD      A,(DE)          
78F6: 83             ADD     A,E             
78F7: 14             INC     D               
78F8: 0C             INC     C               
78F9: 33             INC     SP              
78FA: 27             DAA                     
78FB: 0E 25          LD      C,$25           
78FD: 13             INC     DE              
78FE: 04             INC     B               
78FF: 22 0F A0       LD      ($A00F),HL      
7902: 5F             LD      E,A             
7903: 17             RLA                     
7904: 46             LD      B,(HL)          
7905: 48             LD      C,B             
7906: 66             LD      H,(HL)          
7907: 17             RLA                     
7908: D3 61          OUT     ($61),A         
790A: 04             INC     B               
790B: 68             LD      L,B             
790C: 63             LD      H,E             
790D: 16 5B          LD      D,$5B           
790F: 99             SBC     C               
7910: 56             LD      D,(HL)          
7911: 98             SBC     B               
7912: C0             RET     NZ              
7913: 16 49          LD      D,$49           
7915: 5E             LD      E,(HL)          
7916: 90             SUB     B               
7917: 78             LD      A,B             
7918: 0E BC          LD      C,$BC           
791A: 92             SUB     D               
791B: 5F             LD      E,A             
791C: 59             LD      E,C             
791D: 15             DEC     D               
791E: 9B             SBC     E               
791F: AF             XOR     A               
7920: 19             ADD     HL,DE           
7921: A1             AND     C               
7922: 34             INC     (HL)            
7923: 23             INC     HL              
7924: 0E 21          LD      C,$21           
7926: 13             INC     DE              
7927: 04             INC     B               
7928: 1E C7          LD      E,$C7           
792A: DE 95          SBC     $95             
792C: AF             XOR     A               
792D: D5             PUSH    DE              
792E: C3 65 62       JP      $6265           
7931: D5             PUSH    DE              
7932: 15             DEC     D               
7933: 67             LD      H,A             
7934: 16 67          LD      D,$67           
7936: 49             LD      C,C             
7937: 66             LD      H,(HL)          
7938: B1             OR      C               
7939: D0             RET     NC              
793A: 15             DEC     D               
793B: 3F             CCF                     
793C: 16 ED          LD      D,$ED           
793E: 48             LD      C,B             
793F: 90             SUB     B               
7940: 14             INC     D               
7941: 04             INC     B               
7942: 58             LD      E,B             
7943: 30 A1          JR      NC,$78E6        
7945: 09             ADD     HL,BC           
7946: 5C             LD      E,H             
7947: 35             DEC     (HL)            
7948: 1C             INC     E               
7949: 0E 1A          LD      C,$1A           
794B: 13             INC     DE              
794C: 04             INC     B               
794D: 17             RLA                     
794E: C7             RST     0X00            
794F: DE 73          SBC     $73             
7951: 21 76 4D       LD      HL,$4D76        
7954: F4 BD F3       CALL    P,$F3BD         
7957: 17             RLA                     
7958: 9A             SBC     D               
7959: BD             CP      L               
795A: FA 17 2F       JP      M,$2F17         
795D: 62             LD      H,D             
795E: 51             LD      D,C             
795F: 18 55          JR      $79B6           
7961: C2 F2 BD       JP      NZ,$BDF2        
7964: 21 36 17       LD      HL,$1736        
7967: 0E 15          LD      C,$15           
7969: 13             INC     DE              
796A: 0D             DEC     C               
796B: 12             LD      (DE),A          
796C: 04             INC     B               
796D: 0E C7          LD      C,$C7           
796F: DE D3          SBC     $D3             
7971: 14             INC     D               
7972: E6 96          AND     $96             
7974: 77             LD      (HL),A          
7975: 15             DEC     D               
7976: 0B             DEC     BC              
7977: BC             CP      H               
7978: 96             SUB     (HL)            
7979: 96             SUB     (HL)            
797A: DB 72          IN      A,($72)         
797C: 11 84 37       LD      DE,$3784        
797F: 15             DEC     D               
7980: 0E 13          LD      C,$13           
7982: 13             INC     DE              
7983: 0D             DEC     C               
7984: 10 04          DJNZ    $798A           
7986: 0C             INC     C               
7987: C7             RST     0X00            
7988: DE 94          SBC     $94             
798A: 14             INC     D               
798B: 85             ADD     A,L             
798C: 61             LD      H,C             
798D: 0B             DEC     BC              
798E: BC             CP      H               
798F: 96             SUB     (HL)            
7990: 96             SUB     (HL)            
7991: DB 72          IN      A,($72)         
7993: 11 84 38       LD      DE,$3884        
7996: 20 0E          JR      NZ,$79A6        
7998: 1E 13          LD      E,$13           
799A: 0D             DEC     C               
799B: 1B             DEC     DE              
799C: 04             INC     B               
799D: 17             RLA                     
799E: 5F             LD      E,A             
799F: BE             CP      (HL)            
79A0: 5B             LD      E,E             
79A1: B1             OR      C               
79A2: 4B             LD      C,E             
79A3: 7B             LD      A,E             
79A4: 06 9A          LD      B,$9A           
79A6: 30 15          JR      NC,$79BD        
79A8: 29             ADD     HL,HL           
79A9: A1             AND     C               
79AA: 14             INC     D               
79AB: 71             LD      (HL),C          
79AC: 3F             CCF                     
79AD: A0             AND     B               
79AE: B0             OR      B               
79AF: 17             RLA                     
79B0: F4 59 82       CALL    P,$8259         
79B3: 17             RLA                     
79B4: 45             LD      B,L             
79B5: 11 84 39       LD      DE,$3984        
79B8: 1D             DEC     E               
79B9: 0E 1B          LD      C,$1B           
79BB: 13             INC     DE              
79BC: 0D             DEC     C               
79BD: 18 04          JR      $79C3           
79BF: 16 C7          LD      D,$C7           
79C1: DE FB          SBC     $FB             
79C3: 17             RLA                     
79C4: F3             DI                      
79C5: 8C             ADC     A,H             
79C6: 58             LD      E,B             
79C7: 72             LD      (HL),D          
79C8: 56             LD      D,(HL)          
79C9: 5E             LD      E,(HL)          
79CA: D2 9C 73       JP      NC,$739C        
79CD: C6 73          ADD     $73             
79CF: 7B             LD      A,E             
79D0: 83             ADD     A,E             
79D1: 7A             LD      A,D             
79D2: 5F             LD      E,A             
79D3: BE             CP      (HL)            
79D4: 7F             LD      A,A             
79D5: B1             OR      C               
79D6: 3A 1E 0E       LD      A,($0E1E)       
79D9: 1C             INC     E               
79DA: 13             INC     DE              
79DB: 0D             DEC     C               
79DC: 19             ADD     HL,DE           
79DD: 04             INC     B               
79DE: 0C             INC     C               
79DF: C7             RST     0X00            
79E0: DE D3          SBC     $D3             
79E2: 14             INC     D               
79E3: E6 96          AND     $96             
79E5: C2 16 83       JP      NZ,$8316        
79E8: 61             LD      H,C             
79E9: 5F             LD      E,A             
79EA: BE             CP      (HL)            
79EB: 11 04 06       LD      DE,$0604        
79EE: 56             LD      D,(HL)          
79EF: D1             POP     DE              
79F0: 16 71          LD      D,$71           
79F2: DB 72          IN      A,($72)         
79F4: 12             LD      (DE),A          
79F5: 84             ADD     A,H             
79F6: 0D             DEC     C               
79F7: 34             INC     (HL)            
79F8: 0E 32          LD      C,$32           
79FA: 0D             DEC     C               
79FB: 2E 1A          LD      L,$1A           
79FD: 83             ADD     A,E             
79FE: 0E 2A          LD      C,$2A           
7A00: 0D             DEC     C               
7A01: 27             DAA                     
7A02: 0E 07          LD      C,$07           
7A04: 14             INC     D               
7A05: 15             DEC     D               
7A06: 10 1B          DJNZ    $7A23           
7A08: 14             INC     D               
7A09: 15             DEC     D               
7A0A: 40             LD      B,B             
7A0B: 04             INC     B               
7A0C: 02             LD      (BC),A          
7A0D: 5F             LD      E,A             
7A0E: BE             CP      (HL)            
7A0F: 11 04 14       LD      DE,$1404        
7A12: 07             RLCA                    
7A13: 4F             LD      C,A             
7A14: 17             RLA                     
7A15: 98             SBC     B               
7A16: CA B5 37       JP      Z,$37B5         
7A19: 49             LD      C,C             
7A1A: F5             PUSH    AF              
7A1B: 8B             ADC     A,E             
7A1C: D3 B8          OUT     ($B8),A         
7A1E: B8             CP      B               
7A1F: 16 91          LD      D,$91           
7A21: 64             LD      H,H             
7A22: 96             SUB     (HL)            
7A23: 64             LD      H,H             
7A24: DB 72          IN      A,($72)         
7A26: 12             LD      (DE),A          
7A27: 84             ADD     A,H             
7A28: 10 13          DJNZ    $7A3D           
7A2A: 14             INC     D               
7A2B: 0C             INC     C               
7A2C: 0E 39          LD      C,$39           
7A2E: 0E 37          LD      C,$37           
7A30: 0D             DEC     C               
7A31: 1B             DEC     DE              
7A32: 1B             DEC     DE              
7A33: 14             INC     D               
7A34: 15             DEC     D               
7A35: 10 04          DJNZ    $7A3B           
7A37: 02             LD      (BC),A          
7A38: 5F             LD      E,A             
7A39: BE             CP      (HL)            
7A3A: 12             LD      (DE),A          
7A3B: 04             INC     B               
7A3C: 10 4B          DJNZ    $7A89           
7A3E: 7B             LD      A,E             
7A3F: 06 9A          LD      B,$9A           
7A41: 85             ADD     A,L             
7A42: 14             INC     D               
7A43: B2             OR      D               
7A44: 53             LD      D,E             
7A45: 90             SUB     B               
7A46: BE             CP      (HL)            
7A47: C9             RET                     
7A48: 6A             LD      L,D             
7A49: 5E             LD      E,(HL)          
7A4A: 79             LD      A,C             
7A4B: 5B             LD      E,E             
7A4C: BB             CP      E               
7A4D: 13             INC     DE              
7A4E: 0D             DEC     C               
7A4F: 17             RLA                     
7A50: 04             INC     B               
7A51: 02             LD      (BC),A          
7A52: 5F             LD      E,A             
7A53: BE             CP      (HL)            
7A54: 12             LD      (DE),A          
7A55: 04             INC     B               
7A56: 10 60          DJNZ    $7AB8           
7A58: 7B             LD      A,E             
7A59: F3             DI                      
7A5A: 23             INC     HL              
7A5B: D5             PUSH    DE              
7A5C: 46             LD      B,(HL)          
7A5D: EE 61          XOR     $61             
7A5F: 91             SUB     C               
7A60: 7A             LD      A,D             
7A61: BC             CP      H               
7A62: 14             INC     D               
7A63: AF             XOR     A               
7A64: 78             LD      A,B             
7A65: 5B             LD      E,E             
7A66: BB             CP      E               
7A67: 0F             RRCA                    
7A68: 19             ADD     HL,DE           
7A69: 0E 17          LD      C,$17           
7A6B: 13             INC     DE              
7A6C: 0D             DEC     C               
7A6D: 14             INC     D               
7A6E: 04             INC     B               
7A6F: 02             LD      (BC),A          
7A70: 5F             LD      E,A             
7A71: BE             CP      (HL)            
7A72: 11 04 0B       LD      DE,$0B04        
7A75: 40             LD      B,B             
7A76: D2 F3 23       JP      NC,$23F3        
7A79: 16 67          LD      D,$67           
7A7B: D0             RET     NC              
7A7C: 15             DEC     D               
7A7D: 82             ADD     A,D             
7A7E: 17             RLA                     
7A7F: 45             LD      B,L             
7A80: 12             LD      (DE),A          
7A81: 84             ADD     A,H             
7A82: 19             ADD     HL,DE           
7A83: 80             ADD     A,B             
7A84: EB             EX      DE,HL           
7A85: 0D             DEC     C               
7A86: 80             ADD     A,B             
7A87: E8             RET     PE              
7A88: 1C             INC     E               
7A89: 1D             DEC     E               
7A8A: 0B             DEC     BC              
7A8B: 80             ADD     A,B             
7A8C: E3             EX      (SP),HL         
7A8D: 22 05 24       LD      ($2405),HL      
7A90: 04             INC     B               
7A91: 22 C7 DE       LD      ($DEC7),HL      
7A94: 94             SUB     H               
7A95: 14             INC     D               
7A96: 51             LD      D,C             
7A97: 5E             LD      E,(HL)          
7A98: 9B             SBC     E               
7A99: 96             SUB     (HL)            
7A9A: 34             INC     (HL)            
7A9B: A1             AND     C               
7A9C: 3B             DEC     SP              
7A9D: 16 F3          LD      D,$F3           
7A9F: B9             CP      C               
7AA0: E9             JP      (HL)            
7AA1: 8B             ADC     A,E             
7AA2: 5B             LD      E,E             
7AA3: BB             CP      E               
7AA4: A3             AND     E               
7AA5: 48             LD      C,B             
7AA6: 63             LD      H,E             
7AA7: BE             CP      (HL)            
7AA8: AB             XOR     E               
7AA9: 98             SBC     B               
7AAA: 47             LD      B,A             
7AAB: 55             LD      D,L             
7AAC: B3             OR      E               
7AAD: 8B             ADC     A,E             
7AAE: 4E             LD      C,(HL)          
7AAF: 86             ADD     A,(HL)          
7AB0: 1B             DEC     DE              
7AB1: 8A             ADC     A,D             
7AB2: 19             ADD     HL,DE           
7AB3: A1             AND     C               
7AB4: 14             INC     D               
7AB5: 1C             INC     E               
7AB6: 04             INC     B               
7AB7: 1A             LD      A,(DE)          
7AB8: 0F             RRCA                    
7AB9: A0             AND     B               
7ABA: 71             LD      (HL),C          
7ABB: 16 5B          LD      D,$5B           
7ABD: B1             OR      C               
7ABE: 41             LD      B,C             
7ABF: 6E             LD      L,(HL)          
7AC0: 0B             DEC     BC              
7AC1: 58             LD      E,B             
7AC2: 3F             CCF                     
7AC3: 99             SBC     C               
7AC4: 7B             LD      A,E             
7AC5: B4             OR      H               
7AC6: 8E             ADC     A,(HL)          
7AC7: 48             LD      C,B             
7AC8: 51             LD      D,C             
7AC9: 18 A8          JR      $7A73           
7ACB: C2 4A 5E       JP      NZ,$5E4A        
7ACE: F3             DI                      
7ACF: 46             LD      B,(HL)          
7AD0: 71             LD      (HL),C          
7AD1: 7B             LD      A,E             
7AD2: 23             INC     HL              
7AD3: 22 04 20       LD      ($2004),HL      
7AD6: C7             RST     0X00            
7AD7: DE 94          SBC     $94             
7AD9: 14             INC     D               
7ADA: 48             LD      C,B             
7ADB: 5E             LD      E,(HL)          
7ADC: 2E 60          LD      L,$60           
7ADE: 91             SUB     C               
7ADF: 7A             LD      A,D             
7AE0: 17             RLA                     
7AE1: 17             RLA                     
7AE2: 7F             LD      A,A             
7AE3: 7B             LD      A,E             
7AE4: CE 15          ADC     $15             
7AE6: 9B             SBC     E               
7AE7: 8F             ADC     A,A             
7AE8: 52             LD      D,D             
7AE9: 77             LD      (HL),A          
7AEA: 75             LD      (HL),L          
7AEB: B1             OR      C               
7AEC: B3             OR      E               
7AED: 55             LD      D,L             
7AEE: 5B             LD      E,E             
7AEF: 4D             LD      C,L             
7AF0: 17             RLA                     
7AF1: 53             LD      D,E             
7AF2: 91             SUB     C               
7AF3: BE             CP      (HL)            
7AF4: 2B             DEC     HL              
7AF5: 96             SUB     (HL)            
7AF6: 33             INC     SP              
7AF7: 32 04 30       LD      ($3004),A       
7AFA: C7             RST     0X00            
7AFB: DE 94          SBC     $94             
7AFD: 14             INC     D               
7AFE: 50             LD      D,B             
7AFF: 5E             LD      E,(HL)          
7B00: F3             DI                      
7B01: A0             AND     B               
7B02: 67             LD      H,A             
7B03: 66             LD      H,(HL)          
7B04: 90             SUB     B               
7B05: 8C             ADC     A,H             
7B06: D7             RST     0X10            
7B07: 6A             LD      L,D             
7B08: 16 A3          LD      D,$A3           
7B0A: D2 9C 47       JP      NC,$479C        
7B0D: 49             LD      C,C             
7B0E: 51             LD      D,C             
7B0F: 18 55          JR      $7B66           
7B11: C2 87 74       JP      NZ,$7487        
7B14: B3             OR      E               
7B15: 8B             ADC     A,E             
7B16: 4D             LD      C,L             
7B17: BD             CP      L               
7B18: 44             LD      B,H             
7B19: 5E             LD      E,(HL)          
7B1A: 8E             ADC     A,(HL)          
7B1B: 62             LD      H,D             
7B1C: 23             INC     HL              
7B1D: 62             LD      H,D             
7B1E: 14             INC     D               
7B1F: 53             LD      D,E             
7B20: 51             LD      D,C             
7B21: 5E             LD      E,(HL)          
7B22: 9B             SBC     E               
7B23: 64             LD      H,H             
7B24: 34             INC     (HL)            
7B25: A1             AND     C               
7B26: AE             XOR     (HL)            
7B27: B7             OR      A               
7B28: 1B             DEC     DE              
7B29: 6A             LD      L,D             
7B2A: 44             LD      B,H             
7B2B: 24             INC     H               
7B2C: 04             INC     B               
7B2D: 22 C7 DE       LD      ($DEC7),HL      
7B30: AF             XOR     A               
7B31: 23             INC     HL              
7B32: 4F             LD      C,A             
7B33: 15             DEC     D               
7B34: 43             LD      B,E             
7B35: 61             LD      H,C             
7B36: AB             XOR     E               
7B37: 98             SBC     B               
7B38: EF             RST     0X28            
7B39: A6             AND     (HL)            
7B3A: 53             LD      D,E             
7B3B: C0             RET     NZ              
7B3C: 81             ADD     A,C             
7B3D: 15             DEC     D               
7B3E: 73             LD      (HL),E          
7B3F: 9E             SBC     (HL)            
7B40: 8E             ADC     A,(HL)          
7B41: C5             PUSH    BC              
7B42: 23             INC     HL              
7B43: 62             LD      H,D             
7B44: 5F             LD      E,A             
7B45: BE             CP      (HL)            
7B46: DB 14          IN      A,($14)         
7B48: 27             DAA                     
7B49: B1             OR      C               
7B4A: 66             LD      H,(HL)          
7B4B: 94             SUB     H               
7B4C: 8D             ADC     A,L             
7B4D: 48             LD      C,B             
7B4E: 6F             LD      L,A             
7B4F: 62             LD      H,D             
7B50: FF             RST     0X38            
7B51: 1E 04          LD      E,$04           
7B53: 1C             INC     E               
7B54: C7             RST     0X00            
7B55: DE 4F          SBC     $4F             
7B57: 15             DEC     D               
7B58: 33             INC     SP              
7B59: 61             LD      H,C             
7B5A: 4B             LD      C,E             
7B5B: 49             LD      C,C             
7B5C: 41             LD      B,C             
7B5D: 6E             LD      L,(HL)          
7B5E: 03             INC     BC              
7B5F: 58             LD      E,B             
7B60: D6 B5          SUB     $B5             
7B62: DB 72          IN      A,($72)         
7B64: 5B             LD      E,E             
7B65: 59             LD      E,C             
7B66: 51             LD      D,C             
7B67: 18 59          JR      $7BC2           
7B69: C2 2F 62       JP      NZ,$622F        
7B6C: B9             CP      C               
7B6D: 14             INC     D               
7B6E: E7             RST     0X20            
7B6F: B2             OR      D               
7B70: 14             INC     D               
7B71: 3B             DEC     SP              
7B72: 0D             DEC     C               
7B73: 39             ADD     HL,SP           
7B74: 1B             DEC     DE              
7B75: 83             ADD     A,E             
7B76: 0E 35          LD      C,$35           
7B78: 0D             DEC     C               
7B79: 18 1A          JR      $7B95           
7B7B: 15             DEC     D               
7B7C: 08             EX      AF,AF'          
7B7D: 0E 04          LD      C,$04           
7B7F: 09             ADD     HL,BC           
7B80: 12             LD      (DE),A          
7B81: 09             ADD     HL,BC           
7B82: 14             INC     D               
7B83: 0E 0D          LD      C,$0D           
7B85: 13             INC     DE              
7B86: 04             INC     B               
7B87: 0A             LD      A,(BC)          
7B88: 73             LD      (HL),E          
7B89: 7B             LD      A,E             
7B8A: 40             LD      B,B             
7B8B: D2 F3 23       JP      NC,$23F3        
7B8E: F4 4F 1B       CALL    P,$1B4F         
7B91: 9C             SBC     H               
7B92: 0D             DEC     C               
7B93: 19             ADD     HL,DE           
7B94: 04             INC     B               
7B95: 0C             INC     C               
7B96: C7             RST     0X00            
7B97: DE D3          SBC     $D3             
7B99: 14             INC     D               
7B9A: E6 96          AND     $96             
7B9C: BF             CP      A               
7B9D: 14             INC     D               
7B9E: C3 B2 5F       JP      $5FB2           
7BA1: BE             CP      (HL)            
7BA2: 11 04 06       LD      DE,$0604        
7BA5: 56             LD      D,(HL)          
7BA6: D1             POP     DE              
7BA7: 16 71          LD      D,$71           
7BA9: DB 72          IN      A,($72)         
7BAB: 12             LD      (DE),A          
7BAC: 84             ADD     A,H             
7BAD: 07             RLCA                    
7BAE: 1A             LD      A,(DE)          
7BAF: 0D             DEC     C               
7BB0: 18 04          JR      $7BB6           
7BB2: 15             DEC     D               
7BB3: C7             RST     0X00            
7BB4: DE 94          SBC     $94             
7BB6: 14             INC     D               
7BB7: 45             LD      B,L             
7BB8: 5E             LD      E,(HL)          
7BB9: 3C             INC     A               
7BBA: 49             LD      C,C             
7BBB: D0             RET     NC              
7BBC: DD             ???                     
7BBD: D6 6A          SUB     $6A             
7BBF: DB 72          IN      A,($72)         
7BC1: FE 67          CP      $67             
7BC3: 89             ADC     A,C             
7BC4: 8D             ADC     A,L             
7BC5: 91             SUB     C               
7BC6: 7A             LD      A,D             
7BC7: 3A 06 04       LD      A,($0406)       
7BCA: 02             LD      (BC),A          
7BCB: 00             NOP                     
7BCC: 00             NOP                     
7BCD: 00             NOP                     
7BCE: 83             ADD     A,E             
7BCF: CF             RST     0X08            
7BD0: 81             ADD     A,C             
7BD1: 63             LD      H,E             
7BD2: 0D             DEC     C               
7BD3: 61             LD      H,C             
7BD4: 1F             RRA                     
7BD5: 10 C7          DJNZ    $7B9E           
7BD7: DE AF          SBC     $AF             
7BD9: 23             INC     HL              
7BDA: FF             RST     0X38            
7BDB: 14             INC     D               
7BDC: 17             RLA                     
7BDD: 47             LD      B,A             
7BDE: 8C             ADC     A,H             
7BDF: 17             RLA                     
7BE0: 43             LD      B,E             
7BE1: DB 0B          IN      A,($0B)         
7BE3: 6C             LD      L,H             
7BE4: 1B             DEC     DE              
7BE5: 9C             SBC     H               
7BE6: 95             SUB     L               
7BE7: 17             RLA                     
7BE8: 01 81 17       LD      BC,$1781        
7BEB: 05             DEC     B               
7BEC: 84             ADD     A,H             
7BED: 17             RLA                     
7BEE: 06 88          LD      B,$88           
7BF0: 17             RLA                     
7BF1: 07             RLCA                    
7BF2: 00             NOP                     
7BF3: 17             RLA                     
7BF4: 08             EX      AF,AF'          
7BF5: 8C             ADC     A,H             
7BF6: 17             RLA                     
7BF7: 09             ADD     HL,BC           
7BF8: A1             AND     C               
7BF9: 17             RLA                     
7BFA: 0A             LD      A,(BC)          
7BFB: 8E             ADC     A,(HL)          
7BFC: 17             RLA                     
7BFD: 0C             INC     C               
7BFE: 95             SUB     L               
7BFF: 17             RLA                     
7C00: 0E 91          LD      C,$91           
7C02: 17             RLA                     
7C03: 0F             RRCA                    
7C04: 00             NOP                     
7C05: 17             RLA                     
7C06: 11 92 17       LD      DE,$1792        
7C09: 12             LD      (DE),A          
7C0A: 00             NOP                     
7C0B: 17             RLA                     
7C0C: 14             INC     D               
7C0D: A0             AND     B               
7C0E: 17             RLA                     
7C0F: 15             DEC     D               
7C10: 00             NOP                     
7C11: 17             RLA                     
7C12: 16 00          LD      D,$00           
7C14: 17             RLA                     
7C15: 18 9C          JR      $7BB3           
7C17: 17             RLA                     
7C18: 1E 00          LD      E,$00           
7C1A: 17             RLA                     
7C1B: 1F             RRA                     
7C1C: 00             NOP                     
7C1D: 17             RLA                     
7C1E: 22 8F 17       LD      ($178F),HL      
7C21: 25             DEC     H               
7C22: 9C             SBC     H               
7C23: 17             RLA                     
7C24: 26 00          LD      H,$00           
7C26: 17             RLA                     
7C27: 28 00          JR      Z,$7C29         
7C29: 1C             INC     E               
7C2A: 15             DEC     D               
7C2B: 23             INC     HL              
7C2C: 3C             INC     A               
7C2D: 1C             INC     E               
7C2E: 1D             DEC     E               
7C2F: 23             INC     HL              
7C30: 46             LD      B,(HL)          
7C31: 17             RLA                     
7C32: 1D             DEC     E               
7C33: 96             SUB     (HL)            
7C34: 25             DEC     H               
7C35: 82             ADD     A,D             
7C36: 2C             INC     L               
7C37: 0D             DEC     C               
7C38: 2A 1F 27       LD      HL,($271F)      
7C3B: 5F             LD      E,A             
7C3C: BE             CP      (HL)            
7C3D: 66             LD      H,(HL)          
7C3E: 17             RLA                     
7C3F: 8F             ADC     A,A             
7C40: 49             LD      C,C             
7C41: 54             LD      D,H             
7C42: 5E             LD      E,(HL)          
7C43: 3F             CCF                     
7C44: 61             LD      H,C             
7C45: 57             LD      D,A             
7C46: 49             LD      C,C             
7C47: D6 B5          SUB     $B5             
7C49: DB 72          IN      A,($72)         
7C4B: 3C             INC     A               
7C4C: 49             LD      C,C             
7C4D: 6B             LD      L,E             
7C4E: A1             AND     C               
7C4F: 23             INC     HL              
7C50: D1             POP     DE              
7C51: 13             INC     DE              
7C52: 54             LD      D,H             
7C53: F0             RET     P               
7C54: A4             AND     H               
7C55: 8C             ADC     A,H             
7C56: 62             LD      H,D             
7C57: 7F             LD      A,A             
7C58: 49             LD      C,C             
7C59: DB B5          IN      A,($B5)         
7C5B: 34             INC     (HL)            
7C5C: A1             AND     C               
7C5D: 9F             SBC     A               
7C5E: 15             DEC     D               
7C5F: 3E 49          LD      A,$49           
7C61: 2E 81          LD      L,$81           
7C63: 83             ADD     A,E             
7C64: 66             LD      H,(HL)          
7C65: 0D             DEC     C               
7C66: 64             LD      H,H             
7C67: 0E 61          LD      C,$61           
7C69: 0D             DEC     C               
7C6A: 08             EX      AF,AF'          
7C6B: 08             EX      AF,AF'          
7C6C: 0E 17          LD      C,$17           
7C6E: 0E 00          LD      C,$00           
7C70: 1C             INC     E               
7C71: 0F             RRCA                    
7C72: 0C             INC     C               
7C73: 0D             DEC     C               
7C74: 08             EX      AF,AF'          
7C75: 08             EX      AF,AF'          
7C76: 25             DEC     H               
7C77: 17             RLA                     
7C78: 25             DEC     H               
7C79: 00             NOP                     
7C7A: 1C             INC     E               
7C7B: 26 0C          LD      H,$0C           
7C7D: 0D             DEC     C               
7C7E: 1D             DEC     E               
7C7F: 15             DEC     D               
7C80: 10 04          DJNZ    $7C86           
7C82: 0C             INC     C               
7C83: 46             LD      B,(HL)          
7C84: 77             LD      (HL),A          
7C85: 05             DEC     B               
7C86: A0             AND     B               
7C87: 16 BC          LD      D,$BC           
7C89: 90             SUB     B               
7C8A: 73             LD      (HL),E          
7C8B: D6 83          SUB     $83             
7C8D: DB 72          IN      A,($72)         
7C8F: 16 04          LD      D,$04           
7C91: 0A             LD      A,(BC)          
7C92: 4E             LD      C,(HL)          
7C93: D1             POP     DE              
7C94: 05             DEC     B               
7C95: 8A             ADC     A,D             
7C96: 42             LD      B,D             
7C97: A0             AND     B               
7C98: 2B             DEC     HL              
7C99: 62             LD      H,D             
7C9A: FF             RST     0X38            
7C9B: BD             CP      L               
7C9C: 0D             DEC     C               
7C9D: 21 14 15       LD      HL,$1514        
7CA0: 20 04          JR      NZ,$7CA6        
7CA2: 1A             LD      A,(DE)          
7CA3: C7             RST     0X00            
7CA4: DE 94          SBC     $94             
7CA6: 14             INC     D               
7CA7: 53             LD      D,E             
7CA8: 5E             LD      E,(HL)          
7CA9: D6 C4          SUB     $C4             
7CAB: 4B             LD      C,E             
7CAC: 5E             LD      E,(HL)          
7CAD: 13             INC     DE              
7CAE: 98             SBC     B               
7CAF: 44             LD      B,H             
7CB0: A4             AND     H               
7CB1: DB 8B          IN      A,($8B)         
7CB3: C3 9E 6F       JP      $6F9E           
7CB6: B1             OR      C               
7CB7: 53             LD      D,E             
7CB8: A1             AND     C               
7CB9: AB             XOR     E               
7CBA: 98             SBC     B               
7CBB: 5F             LD      E,A             
7CBC: BE             CP      (HL)            
7CBD: 16 84          LD      D,$84           
7CBF: 18 0D          JR      $7CCE           
7CC1: 08             EX      AF,AF'          
7CC2: 0F             RRCA                    
7CC3: 16 04          LD      D,$04           
7CC5: 04             INC     B               
7CC6: 4D             LD      C,L             
7CC7: BD             CP      L               
7CC8: A7             AND     A               
7CC9: 61             LD      H,C             
7CCA: 18 84          JR      $7C50           
7CCC: 04             INC     B               
7CCD: 04             INC     B               
7CCE: 02             LD      (BC),A          
7CCF: 3B             DEC     SP              
7CD0: F4 85 29       CALL    P,$2985         
7CD3: 1F             RRA                     
7CD4: 27             DAA                     
7CD5: 49             LD      C,C             
7CD6: 45             LD      B,L             
7CD7: 07             RLCA                    
7CD8: B3             OR      E               
7CD9: 11 A3 89       LD      DE,$89A3        
7CDC: 64             LD      H,H             
7CDD: 94             SUB     H               
7CDE: C3 0B 5C       JP      $5C0B           
7CE1: 94             SUB     H               
7CE2: 91             SUB     C               
7CE3: 1F             RRA                     
7CE4: 54             LD      D,H             
7CE5: C3 B5 07       JP      $07B5           
7CE8: B3             OR      E               
7CE9: 33             INC     SP              
7CEA: 98             SBC     B               
7CEB: 5F             LD      E,A             
7CEC: BE             CP      (HL)            
7CED: E1             POP     HL              
7CEE: 14             INC     D               
7CEF: CF             RST     0X08            
7CF0: B2             OR      D               
7CF1: 96             SUB     (HL)            
7CF2: AF             XOR     A               
7CF3: DB 9C          IN      A,($9C)         
7CF5: 34             INC     (HL)            
7CF6: A1             AND     C               
7CF7: 33             INC     SP              
7CF8: 17             RLA                     
7CF9: 2E 6D          LD      L,$6D           
7CFB: 2E 87          LD      L,$87           
7CFD: 2A 1F 28       LD      HL,($281F)      
7D00: 49             LD      C,C             
7D01: 45             LD      B,L             
7D02: 07             RLCA                    
7D03: B3             OR      E               
7D04: 11 A3 89       LD      DE,$89A3        
7D07: 64             LD      H,H             
7D08: 94             SUB     H               
7D09: C3 0B 5C       JP      $5C0B           
7D0C: 95             SUB     L               
7D0D: 5A             LD      E,D             
7D0E: EA 48 94       JP      PE,$9448        
7D11: 5F             LD      E,A             
7D12: C3 B5 07       JP      $07B5           
7D15: B3             OR      E               
7D16: 33             INC     SP              
7D17: 98             SBC     B               
7D18: 5F             LD      E,A             
7D19: BE             CP      (HL)            
7D1A: E1             POP     HL              
7D1B: 14             INC     D               
7D1C: CF             RST     0X08            
7D1D: B2             OR      D               
7D1E: 96             SUB     (HL)            
7D1F: AF             XOR     A               
7D20: DB 9C          IN      A,($9C)         
7D22: 34             INC     (HL)            
7D23: A1             AND     C               
7D24: 3F             CCF                     
7D25: 16 D7          LD      D,$D7           
7D27: 68             LD      L,B             
7D28: 86             ADD     A,(HL)          
7D29: 1E 1F          LD      E,$1F           
7D2B: 1C             INC     E               
7D2C: 49             LD      C,C             
7D2D: 45             LD      B,L             
7D2E: 07             RLCA                    
7D2F: B3             OR      E               
7D30: 11 A3 89       LD      DE,$89A3        
7D33: 64             LD      H,H             
7D34: 94             SUB     H               
7D35: C3 0B 5C       JP      $5C0B           
7D38: 3F             CCF                     
7D39: 55             LD      D,L             
7D3A: 4B             LD      C,E             
7D3B: 62             LD      H,D             
7D3C: 39             ADD     HL,SP           
7D3D: 49             LD      C,C             
7D3E: 8E             ADC     A,(HL)          
7D3F: C5             PUSH    BC              
7D40: 82             ADD     A,D             
7D41: 17             RLA                     
7D42: 45             LD      B,L             
7D43: 5E             LD      E,(HL)          
7D44: B8             CP      B               
7D45: A0             AND     B               
7D46: 47             LD      B,A             
7D47: 62             LD      H,D             
7D48: 88             ADC     A,B             
7D49: 13             INC     DE              
7D4A: 0D             DEC     C               
7D4B: 11 04 02       LD      DE,$0204        
7D4E: 5F             LD      E,A             
7D4F: BE             CP      (HL)            
7D50: 12             LD      (DE),A          
7D51: 04             INC     B               
7D52: 0A             LD      A,(BC)          
7D53: 4B             LD      C,E             
7D54: 7B             LD      A,E             
7D55: 06 9A          LD      B,$9A           
7D57: BF             CP      A               
7D58: 14             INC     D               
7D59: 10 B2          DJNZ    $7D0D           
7D5B: 5B             LD      E,E             
7D5C: 70             LD      (HL),B          
7D5D: 92             SUB     D               
7D5E: 1C             INC     E               
7D5F: 1F             RRA                     
7D60: 1A             LD      A,(DE)          
7D61: 36 A1          LD      (HL),$A1        
7D63: B8             CP      B               
7D64: 16 7B          LD      D,$7B           
7D66: 14             INC     D               
7D67: 85             ADD     A,L             
7D68: A6             AND     (HL)            
7D69: 44             LD      B,H             
7D6A: B8             CP      B               
7D6B: DB 8B          IN      A,($8B)         
7D6D: 08             EX      AF,AF'          
7D6E: 67             LD      H,A             
7D6F: 1E C1          LD      E,$C1           
7D71: 51             LD      D,C             
7D72: 18 23          JR      $7D97           
7D74: C6 61          ADD     $61             
7D76: B7             OR      A               
7D77: 5B             LD      E,E             
7D78: B1             OR      C               
7D79: 4B             LD      C,E             
7D7A: 7B             LD      A,E             
7D7B: 89             ADC     A,C             
7D7C: 12             LD      (DE),A          
7D7D: 1F             RRA                     
7D7E: 10 C7          DJNZ    $7D47           
7D80: DE D3          SBC     $D3             
7D82: 14             INC     D               
7D83: E6 96          AND     $96             
7D85: FF             RST     0X38            
7D86: 15             DEC     D               
7D87: D3 93          OUT     ($93),A         
7D89: 5B             LD      E,E             
7D8A: BE             CP      (HL)            
7D8B: 08             EX      AF,AF'          
7D8C: BC             CP      H               
7D8D: 21 49 8A       LD      HL,$8A49        
7D90: 32 0D 30       LD      ($300D),A       
7D93: 1F             RRA                     
7D94: 2D             DEC     L               
7D95: C7             RST     0X00            
7D96: DE 3B          SBC     $3B             
7D98: 16 33          LD      D,$33           
7D9A: 98             SBC     B               
7D9B: 03             INC     BC              
7D9C: A0             AND     B               
7D9D: 55             LD      D,L             
7D9E: 45             LD      B,L             
7D9F: 8D             ADC     A,L             
7DA0: A5             AND     L               
7DA1: 43             LD      B,E             
7DA2: 5E             LD      E,(HL)          
7DA3: 16 BC          LD      D,$BC           
7DA5: DB 72          IN      A,($72)         
7DA7: 06 4F          LD      B,$4F           
7DA9: 7F             LD      A,A             
7DAA: BF             CP      A               
7DAB: B8             CP      B               
7DAC: 16 82          LD      D,$82           
7DAE: 17             RLA                     
7DAF: 52             LD      D,D             
7DB0: 5E             LD      E,(HL)          
7DB1: 73             LD      (HL),E          
7DB2: 7B             LD      A,E             
7DB3: 23             INC     HL              
7DB4: D1             POP     DE              
7DB5: 13             INC     DE              
7DB6: 54             LD      D,H             
7DB7: 5F             LD      E,A             
7DB8: BE             CP      (HL)            
7DB9: 3F             CCF                     
7DBA: 17             RLA                     
7DBB: C5             PUSH    BC              
7DBC: 6A             LD      L,D             
7DBD: 4F             LD      C,A             
7DBE: A1             AND     C               
7DBF: 66             LD      H,(HL)          
7DC0: B1             OR      C               
7DC1: 2E 81          LD      L,$81           
7DC3: 8B             ADC     A,E             
7DC4: 79             LD      A,C             
7DC5: 0D             DEC     C               
7DC6: 77             LD      (HL),A          
7DC7: 1F             RRA                     
7DC8: 74             LD      (HL),H          
7DC9: C7             RST     0X00            
7DCA: DE 2F          SBC     $2F             
7DCC: 17             RLA                     
7DCD: 43             LD      B,E             
7DCE: 48             LD      C,B             
7DCF: 5B             LD      E,E             
7DD0: E3             EX      (SP),HL         
7DD1: 23             INC     HL              
7DD2: D1             POP     DE              
7DD3: DB 8B          IN      A,($8B)         
7DD5: C7             RST     0X00            
7DD6: DE AF          SBC     $AF             
7DD8: 23             INC     HL              
7DD9: 4B             LD      C,E             
7DDA: 15             DEC     D               
7DDB: 03             INC     BC              
7DDC: 8D             ADC     A,L             
7DDD: AB             XOR     E               
7DDE: 98             SBC     B               
7DDF: 5B             LD      E,E             
7DE0: BE             CP      (HL)            
7DE1: 16 BC          LD      D,$BC           
7DE3: DB 72          IN      A,($72)         
7DE5: E9             JP      (HL)            
7DE6: B3             OR      E               
7DE7: E1             POP     HL              
7DE8: 14             INC     D               
7DE9: 74             LD      (HL),H          
7DEA: CA F3 5F       JP      Z,$5FF3         
7DED: 52             LD      D,D             
7DEE: 45             LD      B,L             
7DEF: 97             SUB     A               
7DF0: 7B             LD      A,E             
7DF1: 82             ADD     A,D             
7DF2: 17             RLA                     
7DF3: 44             LD      B,H             
7DF4: 5E             LD      E,(HL)          
7DF5: 0E A1          LD      C,$A1           
7DF7: DB 9F          IN      A,($9F)         
7DF9: C3 9E 5F       JP      $5F9E           
7DFC: BE             CP      (HL)            
7DFD: E3             EX      (SP),HL         
7DFE: 16 0B          LD      D,$0B           
7E00: BC             CP      H               
7E01: C5             PUSH    BC              
7E02: B5             OR      L               
7E03: 4F             LD      C,A             
7E04: A1             AND     C               
7E05: 66             LD      H,(HL)          
7E06: B1             OR      C               
7E07: FB             EI                      
7E08: 17             RLA                     
7E09: 53             LD      D,E             
7E0A: BE             CP      (HL)            
7E0B: 63             LD      H,E             
7E0C: B9             CP      C               
7E0D: B5             OR      L               
7E0E: 85             ADD     A,L             
7E0F: 84             ADD     A,H             
7E10: 14             INC     D               
7E11: 36 A1          LD      (HL),$A1        
7E13: 59             LD      E,C             
7E14: 15             DEC     D               
7E15: 23             INC     HL              
7E16: C6 67          ADD     $67             
7E18: 66             LD      H,(HL)          
7E19: 16 BC          LD      D,$BC           
7E1B: 46             LD      B,(HL)          
7E1C: 48             LD      C,B             
7E1D: 8B             ADC     A,E             
7E1E: 18 C7          JR      $7DE7           
7E20: DE 09          SBC     $09             
7E22: 15             DEC     D               
7E23: E6 96          AND     $96             
7E25: 9B             SBC     E               
7E26: 15             DEC     D               
7E27: 5B             LD      E,E             
7E28: CA 8F BE       JP      Z,$BE8F         
7E2B: 56             LD      D,(HL)          
7E2C: 5E             LD      E,(HL)          
7E2D: CF             RST     0X08            
7E2E: 9C             SBC     H               
7E2F: 95             SUB     L               
7E30: 5F             LD      E,A             
7E31: 2F             CPL                     
7E32: C6 82          ADD     $82             
7E34: 17             RLA                     
7E35: 5B             LD      E,E             
7E36: 61             LD      H,C             
7E37: 1B             DEC     DE              
7E38: 63             LD      H,E             
7E39: 06 56          LD      B,$56           
7E3B: DB E0          IN      A,($E0)         
7E3D: 81             ADD     A,C             
7E3E: 8C             ADC     A,H             
7E3F: 49             LD      C,C             
7E40: 1F             RRA                     
7E41: 47             LD      B,A             
7E42: C7             RST     0X00            
7E43: DE 03          SBC     $03             
7E45: 15             DEC     D               
7E46: 61             LD      H,C             
7E47: B7             OR      A               
7E48: 74             LD      (HL),H          
7E49: CA 7B 14       JP      Z,$147B         
7E4C: E7             RST     0X20            
7E4D: 59             LD      E,C             
7E4E: 06 A3          LD      B,$A3           
7E50: 35             DEC     (HL)            
7E51: 49             LD      C,C             
7E52: E3             EX      (SP),HL         
7E53: 16 19          LD      D,$19           
7E55: BC             CP      H               
7E56: 85             ADD     A,L             
7E57: 73             LD      (HL),E          
7E58: 07             RLCA                    
7E59: 71             LD      (HL),C          
7E5A: 3F             CCF                     
7E5B: D9             EXX                     
7E5C: 4D             LD      C,L             
7E5D: 98             SBC     B               
7E5E: 5C             LD      E,H             
7E5F: 15             DEC     D               
7E60: DB 9F          IN      A,($9F)         
7E62: 5F             LD      E,A             
7E63: BE             CP      (HL)            
7E64: 99             SBC     C               
7E65: 16 C2          LD      D,$C2           
7E67: B3             OR      E               
7E68: 89             ADC     A,C             
7E69: 17             RLA                     
7E6A: 82             ADD     A,D             
7E6B: 17             RLA                     
7E6C: 55             LD      D,L             
7E6D: 5E             LD      E,(HL)          
7E6E: 36 A1          LD      (HL),$A1        
7E70: 19             ADD     HL,DE           
7E71: 71             LD      (HL),C          
7E72: 46             LD      B,(HL)          
7E73: 48             LD      C,B             
7E74: 56             LD      D,(HL)          
7E75: F4 DB 72       CALL    P,$72DB         
7E78: 96             SUB     (HL)            
7E79: A5             AND     L               
7E7A: D5             PUSH    DE              
7E7B: 15             DEC     D               
7E7C: 89             ADC     A,C             
7E7D: 17             RLA                     
7E7E: C4 9C F3       CALL    NZ,$F39C        
7E81: B2             OR      D               
7E82: 16 58          LD      D,$58           
7E84: CC 9C 72       CALL    Z,$729C         
7E87: C5             PUSH    BC              
7E88: 2E 8D          LD      L,$8D           
7E8A: 20 04          JR      NZ,$7E90        
7E8C: 1E 5F          LD      E,$5F           
7E8E: BE             CP      (HL)            
7E8F: 66             LD      H,(HL)          
7E90: 17             RLA                     
7E91: 8F             ADC     A,A             
7E92: 49             LD      C,C             
7E93: 4B             LD      C,E             
7E94: 5E             LD      E,(HL)          
7E95: CF             RST     0X08            
7E96: B5             OR      L               
7E97: DA C3 89       JP      C,$89C3         
7E9A: 17             RLA                     
7E9B: CA 9C 98       JP      Z,$989C         
7E9E: 5F             LD      E,A             
7E9F: 48             LD      C,B             
7EA0: DB A3          IN      A,($A3)         
7EA2: A0             AND     B               
7EA3: C7             RST     0X00            
7EA4: DE 89          SBC     $89             
7EA6: 17             RLA                     
7EA7: 71             LD      (HL),C          
7EA8: 16 7F          LD      D,$7F           
7EAA: CA 8E 3E       JP      Z,$3E8E         
7EAD: 04             INC     B               
7EAE: 3C             INC     A               
7EAF: 7A             LD      A,D             
7EB0: C4 D9 06       CALL    NZ,$06D9        
7EB3: 82             ADD     A,D             
7EB4: 7B             LD      A,E             
7EB5: 84             ADD     A,H             
7EB6: 15             DEC     D               
7EB7: 96             SUB     (HL)            
7EB8: 5F             LD      E,A             
7EB9: 03             INC     BC              
7EBA: 15             DEC     D               
7EBB: 93             SUB     E               
7EBC: 66             LD      H,(HL)          
7EBD: 2E 56          LD      L,$56           
7EBF: FB             EI                      
7EC0: C0             RET     NZ              
7EC1: C7             RST     0X00            
7EC2: DE 63          SBC     $63             
7EC4: 16 C9          LD      D,$C9           
7EC6: 97             SUB     A               
7EC7: 56             LD      D,(HL)          
7EC8: 5E             LD      E,(HL)          
7EC9: CF             RST     0X08            
7ECA: 9C             SBC     H               
7ECB: 4F             LD      C,A             
7ECC: A1             AND     C               
7ECD: 82             ADD     A,D             
7ECE: 17             RLA                     
7ECF: 43             LD      B,E             
7ED0: 5E             LD      E,(HL)          
7ED1: 3B             DEC     SP              
7ED2: 8E             ADC     A,(HL)          
7ED3: 83             ADD     A,E             
7ED4: AF             XOR     A               
7ED5: 33             INC     SP              
7ED6: 98             SBC     B               
7ED7: C7             RST     0X00            
7ED8: DE 03          SBC     $03             
7EDA: 15             DEC     D               
7EDB: 61             LD      H,C             
7EDC: B7             OR      A               
7EDD: 74             LD      (HL),H          
7EDE: CA 7B 14       JP      Z,$147B         
7EE1: A5             AND     L               
7EE2: B7             OR      A               
7EE3: 76             HALT                    
7EE4: B1             OR      C               
7EE5: DB 16          IN      A,($16)         
7EE7: D3 B9          OUT     ($B9),A         
7EE9: BF             CP      A               
7EEA: 6C             LD      L,H             
7EEB: 8F             ADC     A,A             
7EEC: 07             RLCA                    
7EED: 0D             DEC     C               
7EEE: 05             DEC     B               
7EEF: 08             EX      AF,AF'          
7EF0: 2B             DEC     HL              
7EF1: 00             NOP                     
7EF2: A5             AND     L               
7EF3: 90             SUB     B               
7EF4: 90             SUB     B               
7EF5: 22 1F 20       LD      ($201F),HL      
7EF8: 5F             LD      E,A             
7EF9: BE             CP      (HL)            
7EFA: 8E             ADC     A,(HL)          
7EFB: 14             INC     D               
7EFC: 54             LD      D,H             
7EFD: BD             CP      L               
7EFE: 71             LD      (HL),C          
7EFF: 16 75          LD      D,$75           
7F01: CA AB 14       JP      Z,$14AB         
7F04: 8B             ADC     A,E             
7F05: 54             LD      D,H             
7F06: 6B             LD      L,E             
7F07: BF             CP      A               
7F08: A3             AND     E               
7F09: B7             OR      A               
7F0A: 16 8A          LD      D,$8A           
7F0C: DB 72          IN      A,($72)         
7F0E: 7E             LD      A,(HL)          
7F0F: 74             LD      (HL),H          
7F10: 43             LD      B,E             
7F11: 5E             LD      E,(HL)          
7F12: 08             EX      AF,AF'          
7F13: 4F             LD      C,A             
7F14: 5B             LD      E,E             
7F15: 5E             LD      E,(HL)          
7F16: 3F             CCF                     
7F17: A1             AND     C               
7F18: 91             SUB     C               
7F19: 37             SCF                     
7F1A: 0D             DEC     C               
7F1B: 35             DEC     (HL)            
7F1C: 1F             RRA                     
7F1D: 30 4B          JR      NC,$7F6A        
7F1F: 49             LD      C,C             
7F20: C7             RST     0X00            
7F21: DE DE          SBC     $DE             
7F23: 14             INC     D               
7F24: 64             LD      H,H             
7F25: 7A             LD      A,D             
7F26: C7             RST     0X00            
7F27: 16 11          LD      D,$11           
7F29: BC             CP      H               
7F2A: 96             SUB     (HL)            
7F2B: 64             LD      H,H             
7F2C: DB 72          IN      A,($72)         
7F2E: 7E             LD      A,(HL)          
7F2F: 74             LD      (HL),H          
7F30: B3             OR      E               
7F31: 63             LD      H,E             
7F32: 73             LD      (HL),E          
7F33: 7B             LD      A,E             
7F34: A7             AND     A               
7F35: B7             OR      A               
7F36: 4B             LD      C,E             
7F37: 94             SUB     H               
7F38: 6B             LD      L,E             
7F39: BF             CP      A               
7F3A: 89             ADC     A,C             
7F3B: 91             SUB     C               
7F3C: D3 78          OUT     ($78),A         
7F3E: 13             INC     DE              
7F3F: 8D             ADC     A,L             
7F40: 57             LD      D,A             
7F41: 17             RLA                     
7F42: 33             INC     SP              
7F43: 48             LD      C,B             
7F44: D3 C5          OUT     ($C5),A         
7F46: 6A             LD      L,D             
7F47: 4D             LD      C,L             
7F48: 8E             ADC     A,(HL)          
7F49: 7A             LD      A,D             
7F4A: 51             LD      D,C             
7F4B: 18 DB          JR      $7F28           
7F4D: C7             RST     0X00            
7F4E: 00             NOP                     
7F4F: 9F             SBC     A               
7F50: 95             SUB     L               
7F51: 93             SUB     E               
7F52: 09             ADD     HL,BC           
7F53: 0B             DEC     BC              
7F54: 07             RLCA                    
7F55: 0A             LD      A,(BC)          
7F56: 36 01          LD      (HL),$01        
7F58: 94             SUB     H               
7F59: 37             SCF                     
7F5A: 01 94 94       LD      BC,$9494        
7F5D: 19             ADD     HL,DE           
7F5E: 1F             RRA                     
7F5F: 17             RLA                     
7F60: FF             RST     0X38            
7F61: A5             AND     L               
7F62: 57             LD      D,A             
7F63: 49             LD      C,C             
7F64: B5             OR      L               
7F65: 17             RLA                     
7F66: 46             LD      B,(HL)          
7F67: 5E             LD      E,(HL)          
7F68: 2F             CPL                     
7F69: 7B             LD      A,E             
7F6A: 03             INC     BC              
7F6B: 56             LD      D,(HL)          
7F6C: 1D             DEC     E               
7F6D: A0             AND     B               
7F6E: A6             AND     (HL)            
7F6F: 16 3F          LD      D,$3F           
7F71: BB             CP      E               
7F72: 11 EE 99       LD      DE,$99EE        
7F75: AF             XOR     A               
7F76: 2E 95          LD      L,$95           
7F78: 26 0D          LD      H,$0D           
7F7A: 24             INC     H               
7F7B: 17             RLA                     
7F7C: 36 FF          LD      (HL),$FF        
7F7E: 17             RLA                     
7F7F: 29             ADD     HL,HL           
7F80: 00             NOP                     
7F81: 17             RLA                     
7F82: 2A 00 17       LD      HL,($1700)      
7F85: 2B             DEC     HL              
7F86: 00             NOP                     
7F87: 17             RLA                     
7F88: 2C             INC     L               
7F89: 00             NOP                     
7F8A: 17             RLA                     
7F8B: 2D             DEC     L               
7F8C: 00             NOP                     
7F8D: 17             RLA                     
7F8E: 2E 00          LD      L,$00           
7F90: 17             RLA                     
7F91: 31 00 17       LD      SP,$1700        
7F94: 34             INC     (HL)            
7F95: 00             NOP                     
7F96: 17             RLA                     
7F97: 35             DEC     (HL)            
7F98: 00             NOP                     
7F99: 17             RLA                     
7F9A: 3A 00 17       LD      A,($1700)       
7F9D: 3C             INC     A               
7F9E: 1D             DEC     E               
7F9F: 00             NOP                     
7FA0: FF             RST     0X38            
7FA1: 00             NOP                     
7FA2: FF             RST     0X38            
7FA3: 00             NOP                     
7FA4: FF             RST     0X38            
7FA5: 00             NOP                     
7FA6: FF             RST     0X38            
7FA7: 00             NOP                     
7FA8: FF             RST     0X38            
7FA9: 00             NOP                     
7FAA: FF             RST     0X38            
7FAB: 00             NOP                     
7FAC: FF             RST     0X38            
7FAD: 00             NOP                     
7FAE: FF             RST     0X38            
7FAF: 00             NOP                     
7FB0: FF             RST     0X38            
7FB1: 00             NOP                     
7FB2: FF             RST     0X38            
7FB3: 00             NOP                     
7FB4: FF             RST     0X38            
7FB5: 00             NOP                     
7FB6: FF             RST     0X38            
7FB7: 00             NOP                     
7FB8: FF             RST     0X38            
7FB9: 00             NOP                     
7FBA: FF             RST     0X38            
7FBB: 00             NOP                     
7FBC: FF             RST     0X38            
7FBD: 00             NOP                     
7FBE: FF             RST     0X38            
7FBF: 00             NOP                     
7FC0: FF             RST     0X38            
7FC1: 00             NOP                     
7FC2: FF             RST     0X38            
7FC3: 00             NOP                     
7FC4: FF             RST     0X38            
7FC5: 00             NOP                     
7FC6: FF             RST     0X38            
7FC7: 00             NOP                     
7FC8: FF             RST     0X38            
7FC9: 00             NOP                     
7FCA: FF             RST     0X38            
7FCB: 00             NOP                     
7FCC: FF             RST     0X38            
7FCD: 00             NOP                     
7FCE: FF             RST     0X38            
7FCF: 00             NOP                     
7FD0: FF             RST     0X38            
7FD1: 00             NOP                     
7FD2: FF             RST     0X38            
7FD3: 00             NOP                     
7FD4: FF             RST     0X38            
7FD5: 00             NOP                     
7FD6: FF             RST     0X38            
7FD7: 00             NOP                     
7FD8: FF             RST     0X38            
7FD9: 00             NOP                     
7FDA: FF             RST     0X38            
7FDB: 00             NOP                     
7FDC: FF             RST     0X38            
7FDD: 00             NOP                     
7FDE: FF             RST     0X38            
7FDF: 00             NOP                     
7FE0: FF             RST     0X38            
7FE1: 00             NOP                     
7FE2: FF             RST     0X38            
7FE3: 00             NOP                     
7FE4: FF             RST     0X38            
7FE5: 00             NOP                     
7FE6: FF             RST     0X38            
7FE7: 00             NOP                     
7FE8: FF             RST     0X38            
7FE9: 00             NOP                     
7FEA: FF             RST     0X38            
7FEB: 00             NOP                     
7FEC: FF             RST     0X38            
7FED: 00             NOP                     
7FEE: FF             RST     0X38            
7FEF: 00             NOP                     
7FF0: FF             RST     0X38            
7FF1: 00             NOP                     
7FF2: FF             RST     0X38            
7FF3: 00             NOP                     
7FF4: FF             RST     0X38            
7FF5: 00             NOP                     
7FF6: FF             RST     0X38            
7FF7: 00             NOP                     
7FF8: FF             RST     0X38            
7FF9: 00             NOP                     
7FFA: FF             RST     0X38            
7FFB: 00             NOP                     
7FFC: FF             RST     0X38            
7FFD: 00             NOP                     
7FFE: FF             RST     0X38            
7FFF: 00             NOP                     
```