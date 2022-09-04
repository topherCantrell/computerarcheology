![Bank 06](GBZelda.jpg)

# Bank 06

>>> cpu Z80GB

>>> binary 4000:roms/zelda.gb[18000:1C000]

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](../Hardware.md)

```code
4000: 50              LD      D,B                 
4001: 00              NOP                         
4002: 52              LD      D,D                 
4003: 00              NOP                         
4004: 54              LD      D,H                 
4005: 00              NOP                         
4006: 56              LD      D,(HL)              
4007: 00              NOP                         
4008: 50              LD      D,B                 
4009: 00              NOP                         
400A: 52              LD      D,D                 
400B: 00              NOP                         
400C: 54              LD      D,H                 
400D: 00              NOP                         
400E: 56              LD      D,(HL)              
400F: 00              NOP                         
4010: 58              LD      E,B                 
4011: 00              NOP                         
4012: 5A              LD      E,D                 
4013: 00              NOP                         
4014: 5C              LD      E,H                 
4015: 00              NOP                         
4016: 5E              LD      E,(HL)              
4017: 00              NOP                         
4018: 5A              LD      E,D                 
4019: 20 58           JR      NZ,$4073            ; {}
401B: 20 5E           JR      NZ,$407B            ; {}
401D: 20 5C           JR      NZ,$407B            ; {}
401F: 20 3E           JR      NZ,$405F            ; {}
4021: 21 E0 EC        LD      HL,$ECE0            
4024: 11 00 40        LD      DE,$4000            
4027: CD 3B 3C        CALL    $3C3B               
402A: CD DF 64        CALL    $64DF               ; {}
402D: F0 E7           LD      A,($E7)             
402F: E6 1F           AND     $1F                 
4031: 20 08           JR      NZ,$403B            ; {}
4033: CD BE 65        CALL    $65BE               ; {}
4036: 21 80 C3        LD      HL,$C380            
4039: 09              ADD     HL,BC               
403A: 73              LD      (HL),E              
403B: CD 70 64        CALL    $6470               ; {}
403E: 21 B0 C2        LD      HL,$C2B0            
4041: 09              ADD     HL,BC               
4042: 7E              LD      A,(HL)              
4043: A7              AND     A                   
4044: 20 03           JR      NZ,$4049            ; {}
4046: CD 49 64        CALL    $6449               ; {}
4049: F0 F0           LD      A,($F0)             
404B: C7              RST     0X00                
404C: 56              LD      D,(HL)              
404D: 40              LD      B,B                 
404E: 68              LD      L,B                 
404F: 40              LD      B,B                 
4050: C7              RST     0X00                
4051: 40              LD      B,B                 
4052: DA 40 EC        JP      C,$EC40             
4055: 40              LD      B,B                 
4056: CD 8D 3B        CALL    $3B8D               
4059: FA 15 DB        LD      A,($DB15)           
405C: FE 06           CP      $06                 
405E: D8              RET     C                   
405F: 36 04           LD      (HL),$04            
4061: 21 00 C2        LD      HL,$C200            
4064: 09              ADD     HL,BC               
4065: 36 58           LD      (HL),$58            
4067: C9              RET                         
4068: CD 8C 64        CALL    $648C               ; {}
406B: 30 59           JR      NC,$40C6            ; {}
406D: FA 56 DB        LD      A,($DB56)           
4070: A7              AND     A                   
4071: 28 05           JR      Z,$4078             ; {}
4073: 1E 2D           LD      E,$2D               
4075: C3 C2 40        JP      $40C2               ; {}
4078: F0 F8           LD      A,($F8)             
407A: E6 10           AND     $10                 
407C: 28 06           JR      Z,$4084             ; {}
407E: FA 15 DB        LD      A,($DB15)           
4081: A7              AND     A                   
4082: 20 1D           JR      NZ,$40A1            ; {}
4084: F0 F8           LD      A,($F8)             
4086: F6 10           OR      $10                 
4088: E0 F8           LD      ($FF00+$F8),A       
408A: EA C7 DA        LD      ($DAC7),A           
408D: 3E 3A           LD      A,$3A               
408F: CD 85 21        CALL    $2185               
4092: FA 55 DB        LD      A,($DB55)           
4095: FE 02           CP      $02                 
4097: 30 05           JR      NC,$409E            ; {}
4099: 3E 02           LD      A,$02               
409B: EA 55 DB        LD      ($DB55),A           
409E: C3 8D 3B        JP      $3B8D               
40A1: 1E 3F           LD      E,$3F               
40A3: FE 05           CP      $05                 
40A5: 38 1B           JR      C,$40C2             ; {}
40A7: CD 8D 3B        CALL    $3B8D               
40AA: 36 03           LD      (HL),$03            
40AC: CD 91 08        CALL    $0891               
40AF: 36 20           LD      (HL),$20            
40B1: 21 B0 C2        LD      HL,$C2B0            
40B4: 09              ADD     HL,BC               
40B5: 36 01           LD      (HL),$01            
40B7: 3E FF           LD      A,$FF               
40B9: EA 15 DB        LD      ($DB15),A           
40BC: 3E 09           LD      A,$09               
40BE: E0 A5           LD      ($FF00+$A5),A       
40C0: 1E 3D           LD      E,$3D               
40C2: 7B              LD      A,E                 
40C3: CD 85 21        CALL    $2185               
40C6: C9              RET                         
40C7: FA 77 C1        LD      A,($C177)           
40CA: A7              AND     A                   
40CB: 3E 3B           LD      A,$3B               
40CD: 28 02           JR      Z,$40D1             ; {}
40CF: 3E 3C           LD      A,$3C               
40D1: CD 85 21        CALL    $2185               
40D4: CD 8D 3B        CALL    $3B8D               
40D7: 36 01           LD      (HL),$01            
40D9: C9              RET                         
40DA: CD 91 08        CALL    $0891               
40DD: 20 03           JR      NZ,$40E2            ; {}
40DF: CD 8D 3B        CALL    $3B8D               
40E2: 21 40 C2        LD      HL,$C240            
40E5: 09              ADD     HL,BC               
40E6: 36 F8           LD      (HL),$F8            
40E8: CD 58 65        CALL    $6558               ; {}
40EB: C9              RET                         
40EC: CD 8C 64        CALL    $648C               ; {}
40EF: 30 0E           JR      NC,$40FF            ; {}
40F1: FA 15 DB        LD      A,($DB15)           
40F4: FE 06           CP      $06                 
40F6: 3E 3E           LD      A,$3E               
40F8: 28 02           JR      Z,$40FC             ; {}
40FA: 3E 3D           LD      A,$3D               
40FC: CD 85 21        CALL    $2185               
40FF: F0 98           LD      A,($98)             
4101: D6 78           SUB     $78                 
4103: C6 02           ADD     $02                 
4105: FE 04           CP      $04                 
4107: 30 22           JR      NC,$412B            ; {}
4109: F0 99           LD      A,($99)             
410B: D6 20           SUB     $20                 
410D: C6 05           ADD     $05                 
410F: FE 0A           CP      $0A                 
4111: 30 18           JR      NC,$412B            ; {}
4113: 21 01 D4        LD      HL,$D401            
4116: 3E 01           LD      A,$01               
4118: 22              LD      (HLI),A             
4119: 3E 11           LD      A,$11               
411B: 22              LD      (HLI),A             
411C: 3E D8           LD      A,$D8               
411E: 22              LD      (HLI),A             
411F: 3E 88           LD      A,$88               
4121: 22              LD      (HLI),A             
4122: 3E 70           LD      A,$70               
4124: 22              LD      (HLI),A             
4125: CD E5 65        CALL    $65E5               ; {}
4128: C3 09 09        JP      $0909               
412B: C9              RET                         
412C: FF              RST     0X38                
412D: 00              NOP                         
412E: FF              RST     0X38                
412F: 20 70           JR      NZ,$41A1            ; {}
4131: 00              NOP                         
4132: 70              LD      (HL),B              
4133: 20 72           JR      NZ,$41A7            ; {}
4135: 00              NOP                         
4136: 72              LD      (HL),D              
4137: 20 74           JR      NZ,$41AD            ; {}
4139: 00              NOP                         
413A: 76              HALT                        
413B: 00              NOP                         
413C: 76              HALT                        
413D: 20 74           JR      NZ,$41B3            ; {}
413F: 20 28           JR      NZ,$4169            ; {}
4141: 38 58           JR      C,$419B             ; {}
4143: 58              LD      E,B                 
4144: 78              LD      A,B                 
4145: 88              ADC     A,B                 
4146: 28 88           JR      Z,$40D0             ; {}
4148: 40              LD      B,B                 
4149: 70              LD      (HL),B              
414A: 20 50           JR      NZ,$419C            ; {}
414C: 70              LD      (HL),B              
414D: 40              LD      B,B                 
414E: 40              LD      B,B                 
414F: 40              LD      B,B                 
4150: F0 F8           LD      A,($F8)             
4152: E6 10           AND     $10                 
4154: C2 E5 65        JP      NZ,$65E5            ; {}
4157: 21 E0 C4        LD      HL,$C4E0            
415A: 09              ADD     HL,BC               
415B: 36 3C           LD      (HL),$3C            
415D: 21 60 C4        LD      HL,$C460            
4160: 09              ADD     HL,BC               
4161: 36 FF           LD      (HL),$FF            
4163: 11 2C 41        LD      DE,$412C            
4166: CD 3B 3C        CALL    $3C3B               
4169: CD DF 64        CALL    $64DF               ; {}
416C: CD E2 08        CALL    $08E2               
416F: F0 F0           LD      A,($F0)             
4171: C7              RST     0X00                
4172: 7C              LD      A,H                 
4173: 41              LD      B,C                 
4174: 84              ADD     A,H                 
4175: 41              LD      B,C                 
4176: BF              CP      A                   
4177: 41              LD      B,C                 
4178: D4 41 2D        CALL    NC,$2D41            
417B: 42              LD      B,D                 
417C: CD 91 08        CALL    $0891               
417F: 36 40           LD      (HL),$40            
4181: C3 8D 3B        JP      $3B8D               
4184: CD 91 08        CALL    $0891               
4187: 20 35           JR      NZ,$41BE            ; {}
4189: CD ED 27        CALL    $27ED               
418C: E6 07           AND     $07                 
418E: 5F              LD      E,A                 
418F: 50              LD      D,B                 
4190: 21 40 41        LD      HL,$4140            
4193: 19              ADD     HL,DE               
4194: 7E              LD      A,(HL)              
4195: 21 00 C2        LD      HL,$C200            
4198: 09              ADD     HL,BC               
4199: 77              LD      (HL),A              
419A: 21 48 41        LD      HL,$4148            
419D: 19              ADD     HL,DE               
419E: 7E              LD      A,(HL)              
419F: 21 10 C2        LD      HL,$C210            
41A2: 09              ADD     HL,BC               
41A3: 77              LD      (HL),A              
41A4: CD 9E 65        CALL    $659E               ; {}
41A7: C6 20           ADD     $20                 
41A9: FE 40           CP      $40                 
41AB: 30 09           JR      NC,$41B6            ; {}
41AD: CD AE 65        CALL    $65AE               ; {}
41B0: C6 20           ADD     $20                 
41B2: FE 40           CP      $40                 
41B4: 38 08           JR      C,$41BE             ; {}
41B6: CD 91 08        CALL    $0891               
41B9: 36 18           LD      (HL),$18            
41BB: CD 8D 3B        CALL    $3B8D               
41BE: C9              RET                         
41BF: CD 91 08        CALL    $0891               
41C2: 20 05           JR      NZ,$41C9            ; {}
41C4: 36 30           LD      (HL),$30            
41C6: C3 8D 3B        JP      $3B8D               
41C9: FE 0C           CP      $0C                 
41CB: 3E 01           LD      A,$01               
41CD: 30 01           JR      NC,$41D0            ; {}
41CF: 3C              INC     A                   
41D0: CD 87 3B        CALL    $3B87               
41D3: C9              RET                         
41D4: CD B4 3B        CALL    $3BB4               
41D7: CD 91 08        CALL    $0891               
41DA: 20 46           JR      NZ,$4222            ; {}
41DC: 36 10           LD      (HL),$10            
41DE: CD 8D 3B        CALL    $3B8D               
41E1: 21 20 C4        LD      HL,$C420            
41E4: 09              ADD     HL,BC               
41E5: 7E              LD      A,(HL)              
41E6: A7              AND     A                   
41E7: 20 38           JR      NZ,$4221            ; {}
41E9: 3E 02           LD      A,$02               
41EB: CD 01 3C        CALL    $3C01               
41EE: F0 D7           LD      A,($D7)             
41F0: 21 00 C2        LD      HL,$C200            
41F3: 19              ADD     HL,DE               
41F4: 77              LD      (HL),A              
41F5: F0 D8           LD      A,($D8)             
41F7: 21 10 C2        LD      HL,$C210            
41FA: 19              ADD     HL,DE               
41FB: 77              LD      (HL),A              
41FC: 21 10 C3        LD      HL,$C310            
41FF: 19              ADD     HL,DE               
4200: 36 04           LD      (HL),$04            
4202: 21 20 C3        LD      HL,$C320            
4205: 19              ADD     HL,DE               
4206: 36 18           LD      (HL),$18            
4208: 21 E0 C2        LD      HL,$C2E0            
420B: 19              ADD     HL,DE               
420C: 36 40           LD      (HL),$40            
420E: 21 40 C4        LD      HL,$C440            
4211: 19              ADD     HL,DE               
4212: 36 01           LD      (HL),$01            
4214: C5              PUSH    BC                  
4215: D5              PUSH    DE                  
4216: C1              POP     BC                  
4217: 3E 10           LD      A,$10               
4219: CD 25 3C        CALL    $3C25               
421C: C1              POP     BC                  
421D: 3E 08           LD      A,$08               
421F: E0 F2           LD      ($FF00+$F2),A       
4221: C9              RET                         
4222: E6 20           AND     $20                 
4224: 3E 03           LD      A,$03               
4226: 20 01           JR      NZ,$4229            ; {}
4228: 3C              INC     A                   
4229: CD 87 3B        CALL    $3B87               
422C: C9              RET                         
422D: CD 91 08        CALL    $0891               
4230: 20 0A           JR      NZ,$423C            ; {}
4232: CD 8D 3B        CALL    $3B8D               
4235: 70              LD      (HL),B              
4236: 3E FF           LD      A,$FF               
4238: CD 87 3B        CALL    $3B87               
423B: C9              RET                         
423C: FE 08           CP      $08                 
423E: 3E 01           LD      A,$01               
4240: 38 01           JR      C,$4243             ; {}
4242: 3C              INC     A                   
4243: CD 87 3B        CALL    $3B87               
4246: C9              RET                         
4247: CD C6 44        CALL    $44C6               ; {}
424A: CD DF 64        CALL    $64DF               ; {}
424D: CD 01 65        CALL    $6501               ; {}
4250: CD 84 65        CALL    $6584               ; {}
4253: 21 20 C3        LD      HL,$C320            
4256: 09              ADD     HL,BC               
4257: 35              DEC     (HL)                
4258: 35              DEC     (HL)                
4259: 35              DEC     (HL)                
425A: 21 10 C3        LD      HL,$C310            
425D: 09              ADD     HL,BC               
425E: 7E              LD      A,(HL)              
425F: E6 80           AND     $80                 
4261: E0 E8           LD      ($FF00+$E8),A       
4263: 28 06           JR      Z,$426B             ; {}
4265: 70              LD      (HL),B              
4266: 21 20 C3        LD      HL,$C320            
4269: 09              ADD     HL,BC               
426A: 70              LD      (HL),B              
426B: F0 F0           LD      A,($F0)             
426D: C7              RST     0X00                
426E: 78              LD      A,B                 
426F: 42              LD      B,D                 
4270: D7              RST     0X10                
4271: 42              LD      B,D                 
4272: 21 43 D4        LD      HL,$D443            
4275: 43              LD      B,E                 
4276: 38 44           JR      C,$42BC             ; {}
4278: CD 91 08        CALL    $0891               
427B: 20 32           JR      NZ,$42AF            ; {}
427D: CD AF 3D        CALL    $3DAF               
4280: CD 87 08        CALL    $0887               
4283: 20 1C           JR      NZ,$42A1            ; {}
4285: CD 9E 65        CALL    $659E               ; {}
4288: 21 80 C3        LD      HL,$C380            
428B: 09              ADD     HL,BC               
428C: 7E              LD      A,(HL)              
428D: E6 01           AND     $01                 
428F: BB              CP      E                   
4290: 20 0F           JR      NZ,$42A1            ; {}
4292: CD 8D 3B        CALL    $3B8D               
4295: 36 02           LD      (HL),$02            
4297: CD 91 08        CALL    $0891               
429A: 36 FF           LD      (HL),$FF            
429C: 3E 3B           LD      A,$3B               
429E: E0 F4           LD      ($FF00+$F4),A       
42A0: C9              RET                         
42A1: CD 91 08        CALL    $0891               
42A4: CD ED 27        CALL    $27ED               
42A7: E6 1F           AND     $1F                 
42A9: C6 10           ADD     $10                 
42AB: 77              LD      (HL),A              
42AC: CD 8D 3B        CALL    $3B8D               
42AF: F0 E8           LD      A,($E8)             
42B1: A7              AND     A                   
42B2: 28 06           JR      Z,$42BA             ; {}
42B4: 21 20 C3        LD      HL,$C320            
42B7: 09              ADD     HL,BC               
42B8: 36 10           LD      (HL),$10            
42BA: CD 4B 65        CALL    $654B               ; {}
42BD: CD 9E 3B        CALL    $3B9E               
42C0: 21 80 C3        LD      HL,$C380            
42C3: 09              ADD     HL,BC               
42C4: 7E              LD      A,(HL)              
42C5: 17              RLA                         
42C6: E6 06           AND     $06                 
42C8: CD 87 3B        CALL    $3B87               
42CB: CD B4 3B        CALL    $3BB4               
42CE: C9              RET                         
42CF: 08 F8 08        LD      ($08F8),SP          
42D2: F8 F8           LD      HL,SP+$F8           
42D4: F8 08           LD      HL,SP+$08           
42D6: 08 CD 91        LD      ($91CD),SP          
42D9: 08 20 42        LD      ($4220),SP          ; {}
42DC: CD ED 27        CALL    $27ED               
42DF: E6 1F           AND     $1F                 
42E1: C6 20           ADD     $20                 
42E3: 77              LD      (HL),A              
42E4: CD 8D 3B        CALL    $3B8D               
42E7: 70              LD      (HL),B              
42E8: CD ED 27        CALL    $27ED               
42EB: CB 57           BIT     1,E                 
42ED: 28 04           JR      Z,$42F3             ; {}
42EF: E6 03           AND     $03                 
42F1: 18 10           JR      $4303               ; {}
42F3: CD 9E 65        CALL    $659E               ; {}
42F6: D5              PUSH    DE                  
42F7: CD AE 65        CALL    $65AE               ; {}
42FA: 7B              LD      A,E                 
42FB: E6 03           AND     $03                 
42FD: 3D              DEC     A                   
42FE: 3D              DEC     A                   
42FF: CB 27           SLA     1,E                 
4301: D1              POP     DE                  
4302: B3              OR      E                   
4303: 5F              LD      E,A                 
4304: 21 80 C3        LD      HL,$C380            
4307: 09              ADD     HL,BC               
4308: 73              LD      (HL),E              
4309: 50              LD      D,B                 
430A: 21 CF 42        LD      HL,$42CF            
430D: 19              ADD     HL,DE               
430E: 7E              LD      A,(HL)              
430F: 21 40 C2        LD      HL,$C240            
4312: 09              ADD     HL,BC               
4313: 77              LD      (HL),A              
4314: 21 D3 42        LD      HL,$42D3            
4317: 19              ADD     HL,DE               
4318: 7E              LD      A,(HL)              
4319: 21 50 C2        LD      HL,$C250            
431C: 09              ADD     HL,BC               
431D: 77              LD      (HL),A              
431E: C3 AF 42        JP      $42AF               ; {}
4321: CD EB 3B        CALL    $3BEB               
4324: CD 91 08        CALL    $0891               
4327: 20 10           JR      NZ,$4339            ; {}
4329: CD 8D 3B        CALL    $3B8D               
432C: 70              LD      (HL),B              
432D: CD 87 08        CALL    $0887               
4330: CD ED 27        CALL    $27ED               
4333: E6 1F           AND     $1F                 
4335: C6 08           ADD     $08                 
4337: 77              LD      (HL),A              
4338: C9              RET                         
4339: 3E 01           LD      A,$01               
433B: EA E6 D3        LD      ($D3E6),A           
433E: 21 20 C3        LD      HL,$C320            
4341: 09              ADD     HL,BC               
4342: 70              LD      (HL),B              
4343: F0 E7           LD      A,($E7)             
4345: E6 03           AND     $03                 
4347: 20 10           JR      NZ,$4359            ; {}
4349: 21 10 C3        LD      HL,$C310            
434C: 09              ADD     HL,BC               
434D: 7E              LD      A,(HL)              
434E: D6 0C           SUB     $0C                 
4350: 28 07           JR      Z,$4359             ; {}
4352: E6 80           AND     $80                 
4354: 28 02           JR      Z,$4358             ; {}
4356: 34              INC     (HL)                
4357: 34              INC     (HL)                
4358: 35              DEC     (HL)                
4359: F0 9D           LD      A,($9D)             
435B: FE FF           CP      $FF                 
435D: 28 67           JR      Z,$43C6             ; {}
435F: CD 9E 65        CALL    $659E               ; {}
4362: 21 80 C3        LD      HL,$C380            
4365: 09              ADD     HL,BC               
4366: 7E              LD      A,(HL)              
4367: E6 01           AND     $01                 
4369: BB              CP      E                   
436A: 20 5A           JR      NZ,$43C6            ; {}
436C: CD 9E 65        CALL    $659E               ; {}
436F: C6 40           ADD     $40                 
4371: FE 80           CP      $80                 
4373: 30 51           JR      NC,$43C6            ; {}
4375: 21 10 C2        LD      HL,$C210            
4378: 09              ADD     HL,BC               
4379: 7E              LD      A,(HL)              
437A: E5              PUSH    HL                  
437B: F5              PUSH    AF                  
437C: F0 EC           LD      A,($EC)             
437E: 77              LD      (HL),A              
437F: CD AE 65        CALL    $65AE               ; {}
4382: 5F              LD      E,A                 
4383: F1              POP     AF                  
4384: E1              POP     HL                  
4385: 77              LD      (HL),A              
4386: 7B              LD      A,E                 
4387: C6 30           ADD     $30                 
4389: FE 60           CP      $60                 
438B: 30 39           JR      NC,$43C6            ; {}
438D: 3E 08           LD      A,$08               
438F: CD 30 3C        CALL    $3C30               
4392: F0 D7           LD      A,($D7)             
4394: 2F              CPL                         
4395: 3C              INC     A                   
4396: E0 9B           LD      ($FF00+$9B),A       
4398: F0 D8           LD      A,($D8)             
439A: 2F              CPL                         
439B: 3C              INC     A                   
439C: E0 9A           LD      ($FF00+$9A),A       
439E: C5              PUSH    BC                  
439F: CD D6 20        CALL    $20D6               
43A2: CD 49 3E        CALL    $3E49               
43A5: C1              POP     BC                  
43A6: 21 EE FF        LD      HL,$FFEE            
43A9: F0 98           LD      A,($98)             
43AB: 96              SUB     (HL)                
43AC: C6 04           ADD     $04                 
43AE: FE 08           CP      $08                 
43B0: 30 14           JR      NC,$43C6            ; {}
43B2: 21 EC FF        LD      HL,$FFEC            
43B5: F0 99           LD      A,($99)             
43B7: 96              SUB     (HL)                
43B8: C6 04           ADD     $04                 
43BA: FE 08           CP      $08                 
43BC: 30 08           JR      NC,$43C6            ; {}
43BE: CD 91 08        CALL    $0891               
43C1: 36 80           LD      (HL),$80            
43C3: CD 8D 3B        CALL    $3B8D               
43C6: 21 80 C3        LD      HL,$C380            
43C9: 09              ADD     HL,BC               
43CA: 7E              LD      A,(HL)              
43CB: 17              RLA                         
43CC: E6 06           AND     $06                 
43CE: F6 01           OR      $01                 
43D0: CD 87 3B        CALL    $3B87               
43D3: C9              RET                         
43D4: CD 91 08        CALL    $0891               
43D7: 28 2B           JR      Z,$4404             ; {}
43D9: F0 E8           LD      A,($E8)             
43DB: A7              AND     A                   
43DC: 28 13           JR      Z,$43F1             ; {}
43DE: 21 B0 C2        LD      HL,$C2B0            
43E1: 09              ADD     HL,BC               
43E2: 7E              LD      A,(HL)              
43E3: A7              AND     A                   
43E4: 20 0B           JR      NZ,$43F1            ; {}
43E6: 34              INC     (HL)                
43E7: 21 20 C3        LD      HL,$C320            
43EA: 09              ADD     HL,BC               
43EB: 36 0C           LD      (HL),$0C            
43ED: 3E 09           LD      A,$09               
43EF: E0 F2           LD      ($FF00+$F2),A       
43F1: 21 80 C3        LD      HL,$C380            
43F4: 09              ADD     HL,BC               
43F5: 7E              LD      A,(HL)              
43F6: C6 08           ADD     $08                 
43F8: CD 87 3B        CALL    $3B87               
43FB: 3E FF           LD      A,$FF               
43FD: E0 9D           LD      ($FF00+$9D),A       
43FF: 3E 02           LD      A,$02               
4401: E0 A1           LD      ($FF00+$A1),A       
4403: C9              RET                         
4404: 36 0C           LD      (HL),$0C            
4406: 21 B0 C2        LD      HL,$C2B0            
4409: 09              ADD     HL,BC               
440A: 70              LD      (HL),B              
440B: AF              XOR     A                   
440C: E0 9B           LD      ($FF00+$9B),A       
440E: 21 80 C3        LD      HL,$C380            
4411: 09              ADD     HL,BC               
4412: 7E              LD      A,(HL)              
4413: E6 01           AND     $01                 
4415: 3E 18           LD      A,$18               
4417: 28 02           JR      Z,$441B             ; {}
4419: 3E E8           LD      A,$E8               
441B: E0 9A           LD      ($FF00+$9A),A       
441D: 3E 10           LD      A,$10               
441F: E0 A3           LD      ($FF00+$A3),A       
4421: 3E 20           LD      A,$20               
4423: EA C7 DB        LD      ($DBC7),A           
4426: 3E 02           LD      A,$02               
4428: EA 46 C1        LD      ($C146),A           
442B: 3E 02           LD      A,$02               
442D: EA 94 DB        LD      ($DB94),A           
4430: 3E 08           LD      A,$08               
4432: E0 F2           LD      ($FF00+$F2),A       
4434: CD 8D 3B        CALL    $3B8D               
4437: C9              RET                         
4438: CD 91 08        CALL    $0891               
443B: CA 29 43        JP      Z,$4329             ; {}
443E: 21 20 C3        LD      HL,$C320            
4441: 09              ADD     HL,BC               
4442: 70              LD      (HL),B              
4443: C3 C6 43        JP      $43C6               ; {}
4446: 62              LD      H,D                 
4447: 20 60           JR      NZ,$44A9            ; {}
4449: 20 68           JR      NZ,$44B3            ; {}
444B: 20 66           JR      NZ,$44B3            ; {}
444D: 20 60           JR      NZ,$44AF            ; {}
444F: 00              NOP                         
4450: 62              LD      H,D                 
4451: 00              NOP                         
4452: 66              LD      H,(HL)              
4453: 00              NOP                         
4454: 68              LD      L,B                 
4455: 00              NOP                         
4456: 62              LD      H,D                 
4457: 20 60           JR      NZ,$44B9            ; {}
4459: 20 68           JR      NZ,$44C3            ; {}
445B: 20 66           JR      NZ,$44C3            ; {}
445D: 20 60           JR      NZ,$44BF            ; {}
445F: 00              NOP                         
4460: 62              LD      H,D                 
4461: 00              NOP                         
4462: 66              LD      H,(HL)              
4463: 00              NOP                         
4464: 68              LD      L,B                 
4465: 00              NOP                         
4466: 00              NOP                         
4467: FC                              
4468: 62              LD      H,D                 
4469: 20 00           JR      NZ,$446B            ; {}
446B: 04              INC     B                   
446C: 6A              LD      L,D                 
446D: 20 00           JR      NZ,$446F            ; {}
446F: 0C              INC     C                   
4470: 64              LD      H,H                 
4471: 20 00           JR      NZ,$4473            ; {}
4473: FC                              
4474: 64              LD      H,H                 
4475: 00              NOP                         
4476: 00              NOP                         
4477: 04              INC     B                   
4478: 6A              LD      L,D                 
4479: 00              NOP                         
447A: 00              NOP                         
447B: 0C              INC     C                   
447C: 62              LD      H,D                 
447D: 00              NOP                         
447E: 00              NOP                         
447F: FC                              
4480: 62              LD      H,D                 
4481: 20 00           JR      NZ,$4483            ; {}
4483: 04              INC     B                   
4484: 6A              LD      L,D                 
4485: 20 00           JR      NZ,$4487            ; {}
4487: 0C              INC     C                   
4488: 64              LD      H,H                 
4489: 20 00           JR      NZ,$448B            ; {}
448B: FC                              
448C: 64              LD      H,H                 
448D: 00              NOP                         
448E: 00              NOP                         
448F: 04              INC     B                   
4490: 6A              LD      L,D                 
4491: 00              NOP                         
4492: 00              NOP                         
4493: 0C              INC     C                   
4494: 62              LD      H,D                 
4495: 00              NOP                         
4496: 00              NOP                         
4497: 0E 24           LD      C,$24               
4499: 00              NOP                         
449A: F8 18           LD      HL,SP+$18           
449C: 24              INC     H                   
449D: 00              NOP                         
449E: 08 18 24        LD      ($2418),SP          
44A1: 00              NOP                         
44A2: FE 13           CP      $13                 
44A4: 24              INC     H                   
44A5: 00              NOP                         
44A6: 03              INC     BC                  
44A7: 13              INC     DE                  
44A8: 24              INC     H                   
44A9: 00              NOP                         
44AA: 03              INC     BC                  
44AB: 13              INC     DE                  
44AC: FF              RST     0X38                
44AD: 00              NOP                         
44AE: 00              NOP                         
44AF: FA 24 00        LD      A,($0024)           
44B2: F8 F0           LD      HL,SP+$F0           
44B4: 24              INC     H                   
44B5: 00              NOP                         
44B6: 08 F0 24        LD      ($24F0),SP          
44B9: 00              NOP                         
44BA: FE F5           CP      $F5                 
44BC: 24              INC     H                   
44BD: 00              NOP                         
44BE: 03              INC     BC                  
44BF: F5              PUSH    AF                  
44C0: 24              INC     H                   
44C1: 00              NOP                         
44C2: 03              INC     BC                  
44C3: F5              PUSH    AF                  
44C4: FF              RST     0X38                
44C5: 00              NOP                         
44C6: F0 F1           LD      A,($F1)             
44C8: FE 08           CP      $08                 
44CA: 30 37           JR      NC,$4503            ; {}
44CC: 11 46 44        LD      DE,$4446            
44CF: CD 3B 3C        CALL    $3C3B               
44D2: F0 F0           LD      A,($F0)             
44D4: FE 02           CP      $02                 
44D6: 20 2A           JR      NZ,$4502            ; {}
44D8: 21 80 C3        LD      HL,$C380            
44DB: 09              ADD     HL,BC               
44DC: 7E              LD      A,(HL)              
44DD: 17              RLA                         
44DE: E6 02           AND     $02                 
44E0: 5F              LD      E,A                 
44E1: F0 E7           LD      A,($E7)             
44E3: 1F              RRA                         
44E4: 1F              RRA                         
44E5: 1F              RRA                         
44E6: E6 01           AND     $01                 
44E8: B3              OR      E                   
44E9: 17              RLA                         
44EA: 17              RLA                         
44EB: E6 FC           AND     $FC                 
44ED: 5F              LD      E,A                 
44EE: 17              RLA                         
44EF: E6 F8           AND     $F8                 
44F1: 83              ADD     A,E                 
44F2: 5F              LD      E,A                 
44F3: 50              LD      D,B                 
44F4: 21 96 44        LD      HL,$4496            
44F7: 19              ADD     HL,DE               
44F8: 0E 03           LD      C,$03               
44FA: CD 26 3D        CALL    $3D26               
44FD: 3E 03           LD      A,$03               
44FF: CD D0 3D        CALL    $3DD0               
4502: C9              RET                         
4503: D6 08           SUB     $08                 
4505: 17              RLA                         
4506: 17              RLA                         
4507: E6 FC           AND     $FC                 
4509: 5F              LD      E,A                 
450A: CB 27           SLA     1,E                 
450C: 83              ADD     A,E                 
450D: 5F              LD      E,A                 
450E: 50              LD      D,B                 
450F: 21 66 44        LD      HL,$4466            
4512: 19              ADD     HL,DE               
4513: 0E 03           LD      C,$03               
4515: CD 26 3D        CALL    $3D26               
4518: C3 19 3D        JP      $3D19               
451B: 21 40 C4        LD      HL,$C440            
451E: 09              ADD     HL,BC               
451F: 7E              LD      A,(HL)              
4520: A7              AND     A                   
4521: C2 99 47        JP      NZ,$4799            ; {}
4524: 79              LD      A,C                 
4525: EA 02 D2        LD      ($D202),A           
4528: 21 D0 C2        LD      HL,$C2D0            
452B: 09              ADD     HL,BC               
452C: 7E              LD      A,(HL)              
452D: A7              AND     A                   
452E: 20 21           JR      NZ,$4551            ; {}
4530: 34              INC     (HL)                
4531: 3E 92           LD      A,$92               
4533: CD 01 3C        CALL    $3C01               
4536: 7B              LD      A,E                 
4537: EA 01 D2        LD      ($D201),A           
453A: F0 D8           LD      A,($D8)             
453C: C6 10           ADD     $10                 
453E: 21 10 C2        LD      HL,$C210            
4541: 19              ADD     HL,DE               
4542: 77              LD      (HL),A              
4543: F0 D7           LD      A,($D7)             
4545: C6 30           ADD     $30                 
4547: 21 00 C2        LD      HL,$C200            
454A: 19              ADD     HL,DE               
454B: 77              LD      (HL),A              
454C: 21 40 C4        LD      HL,$C440            
454F: 19              ADD     HL,DE               
4550: 34              INC     (HL)                
4551: CD 7F 47        CALL    $477F               ; {}
4554: CD 12 3F        CALL    $3F12               
4557: F0 EA           LD      A,($EA)             
4559: FE 05           CP      $05                 
455B: C2 CB 53        JP      NZ,$53CB            ; {}
455E: CD DF 64        CALL    $64DF               ; {}
4561: CD 01 65        CALL    $6501               ; {}
4564: CD B4 3B        CALL    $3BB4               
4567: CD 84 65        CALL    $6584               ; {}
456A: 21 20 C3        LD      HL,$C320            
456D: 09              ADD     HL,BC               
456E: 35              DEC     (HL)                
456F: 35              DEC     (HL)                
4570: 35              DEC     (HL)                
4571: 21 10 C3        LD      HL,$C310            
4574: 09              ADD     HL,BC               
4575: 7E              LD      A,(HL)              
4576: E6 80           AND     $80                 
4578: E0 E8           LD      ($FF00+$E8),A       
457A: 28 06           JR      Z,$4582             ; {}
457C: 70              LD      (HL),B              
457D: 21 20 C3        LD      HL,$C320            
4580: 09              ADD     HL,BC               
4581: 70              LD      (HL),B              
4582: F0 F0           LD      A,($F0)             
4584: C7              RST     0X00                
4585: 8F              ADC     A,A                 
4586: 45              LD      B,L                 
4587: 15              DEC     D                   
4588: 46              LD      B,(HL)              
4589: 83              ADD     A,E                 
458A: 46              LD      B,(HL)              
458B: DE 46           SBC     $46                 
458D: 2B              DEC     HL                  
458E: 47              LD      B,A                 
458F: FA 01 D2        LD      A,($D201)           
4592: 5F              LD      E,A                 
4593: 50              LD      D,B                 
4594: 21 90 C2        LD      HL,$C290            
4597: 19              ADD     HL,DE               
4598: 7E              LD      A,(HL)              
4599: FE 00           CP      $00                 
459B: 20 57           JR      NZ,$45F4            ; {}
459D: F0 98           LD      A,($98)             
459F: F5              PUSH    AF                  
45A0: F0 99           LD      A,($99)             
45A2: F5              PUSH    AF                  
45A3: 21 00 C2        LD      HL,$C200            
45A6: 19              ADD     HL,DE               
45A7: 7E              LD      A,(HL)              
45A8: E0 98           LD      ($FF00+$98),A       
45AA: 21 10 C2        LD      HL,$C210            
45AD: 19              ADD     HL,DE               
45AE: 7E              LD      A,(HL)              
45AF: E0 99           LD      ($FF00+$99),A       
45B1: 3E 10           LD      A,$10               
45B3: CD 25 3C        CALL    $3C25               
45B6: CD 4B 65        CALL    $654B               ; {}
45B9: CD 9E 3B        CALL    $3B9E               
45BC: CD 9E 65        CALL    $659E               ; {}
45BF: 21 80 C3        LD      HL,$C380            
45C2: 09              ADD     HL,BC               
45C3: 73              LD      (HL),E              
45C4: C6 0C           ADD     $0C                 
45C6: FE 18           CP      $18                 
45C8: 30 22           JR      NC,$45EC            ; {}
45CA: CD AE 65        CALL    $65AE               ; {}
45CD: C6 0C           ADD     $0C                 
45CF: FE 18           CP      $18                 
45D1: 30 19           JR      NC,$45EC            ; {}
45D3: CD 8D 3B        CALL    $3B8D               
45D6: 36 02           LD      (HL),$02            
45D8: FA 01 D2        LD      A,($D201)           
45DB: 5F              LD      E,A                 
45DC: 50              LD      D,B                 
45DD: 21 90 C2        LD      HL,$C290            
45E0: 19              ADD     HL,DE               
45E1: 36 01           LD      (HL),$01            
45E3: CD 91 08        CALL    $0891               
45E6: 36 1F           LD      (HL),$1F            
45E8: 3E 1C           LD      A,$1C               
45EA: E0 F3           LD      ($FF00+$F3),A       
45EC: F1              POP     AF                  
45ED: E0 99           LD      ($FF00+$99),A       
45EF: F1              POP     AF                  
45F0: E0 98           LD      ($FF00+$98),A       
45F2: 18 03           JR      $45F7               ; {}
45F4: CD 8D 3B        CALL    $3B8D               
45F7: F0 E8           LD      A,($E8)             
45F9: A7              AND     A                   
45FA: 28 06           JR      Z,$4602             ; {}
45FC: 21 20 C3        LD      HL,$C320            
45FF: 09              ADD     HL,BC               
4600: 36 10           LD      (HL),$10            
4602: 21 80 C3        LD      HL,$C380            
4605: 09              ADD     HL,BC               
4606: 7E              LD      A,(HL)              
4607: E6 01           AND     $01                 
4609: CD 87 3B        CALL    $3B87               
460C: C9              RET                         
460D: 0C              INC     C                   
460E: F4                              
460F: 0C              INC     C                   
4610: F4                              
4611: FC                              
4612: FC                              
4613: 04              INC     B                   
4614: 04              INC     B                   
4615: FA 01 D2        LD      A,($D201)           
4618: 5F              LD      E,A                 
4619: 50              LD      D,B                 
461A: 21 90 C2        LD      HL,$C290            
461D: 19              ADD     HL,DE               
461E: 7E              LD      A,(HL)              
461F: FE 00           CP      $00                 
4621: 20 04           JR      NZ,$4627            ; {}
4623: CD 8D 3B        CALL    $3B8D               
4626: 70              LD      (HL),B              
4627: CD 91 08        CALL    $0891               
462A: 20 25           JR      NZ,$4651            ; {}
462C: CD ED 27        CALL    $27ED               
462F: E6 1F           AND     $1F                 
4631: C6 10           ADD     $10                 
4633: 77              LD      (HL),A              
4634: E6 03           AND     $03                 
4636: 21 80 C3        LD      HL,$C380            
4639: 09              ADD     HL,BC               
463A: 77              LD      (HL),A              
463B: 5F              LD      E,A                 
463C: 50              LD      D,B                 
463D: 21 0D 46        LD      HL,$460D            
4640: 19              ADD     HL,DE               
4641: 7E              LD      A,(HL)              
4642: 21 40 C2        LD      HL,$C240            
4645: 09              ADD     HL,BC               
4646: 77              LD      (HL),A              
4647: 21 11 46        LD      HL,$4611            
464A: 19              ADD     HL,DE               
464B: 7E              LD      A,(HL)              
464C: 21 50 C2        LD      HL,$C250            
464F: 09              ADD     HL,BC               
4650: 77              LD      (HL),A              
4651: CD 4B 65        CALL    $654B               ; {}
4654: CD 9E 3B        CALL    $3B9E               
4657: CD F7 45        CALL    $45F7               ; {}
465A: F0 E7           LD      A,($E7)             
465C: E6 08           AND     $08                 
465E: 28 02           JR      Z,$4662             ; {}
4660: 34              INC     (HL)                
4661: 34              INC     (HL)                
4662: C9              RET                         
4663: 00              NOP                         
4664: 02              LD      (BC),A              
4665: 04              INC     B                   
4666: 06 08           LD      B,$08               
4668: 0A              LD      A,(BC)              
4669: 0C              INC     C                   
466A: 0E 00           LD      C,$00               
466C: FE FC           CP      $FC                 
466E: FA F8 F6        LD      A,($F6F8)           
4671: F4                              
4672: F2                              
4673: F0 F1           LD      A,($F1)             
4675: F2                              
4676: F4                              
4677: F6 F8           OR      $F8                 
4679: FA FE F0        LD      A,($F0FE)           
467C: F1              POP     AF                  
467D: F2                              
467E: F4                              
467F: F6 F8           OR      $F8                 
4681: FA FE 21        LD      A,($21FE)           
4684: 80              ADD     A,B                 
4685: C3 09 7E        JP      $7E09               ; {}
4688: E6 01           AND     $01                 
468A: 17              RLA                         
468B: 17              RLA                         
468C: 17              RLA                         
468D: E6 08           AND     $08                 
468F: 5F              LD      E,A                 
4690: CD 91 08        CALL    $0891               
4693: 20 06           JR      NZ,$469B            ; {}
4695: 36 20           LD      (HL),$20            
4697: CD 8D 3B        CALL    $3B8D               
469A: C9              RET                         
469B: 1F              RRA                         
469C: 1F              RRA                         
469D: E6 07           AND     $07                 
469F: B3              OR      E                   
46A0: C5              PUSH    BC                  
46A1: 4F              LD      C,A                 
46A2: FA 01 D2        LD      A,($D201)           
46A5: 5F              LD      E,A                 
46A6: 50              LD      D,B                 
46A7: F0 EE           LD      A,($EE)             
46A9: 21 63 46        LD      HL,$4663            
46AC: 09              ADD     HL,BC               
46AD: 86              ADD     A,(HL)              
46AE: 21 00 C2        LD      HL,$C200            
46B1: 19              ADD     HL,DE               
46B2: 77              LD      (HL),A              
46B3: 21 73 46        LD      HL,$4673            
46B6: 09              ADD     HL,BC               
46B7: 7E              LD      A,(HL)              
46B8: 2F              CPL                         
46B9: 3C              INC     A                   
46BA: C1              POP     BC                  
46BB: 21 10 C3        LD      HL,$C310            
46BE: 09              ADD     HL,BC               
46BF: 86              ADD     A,(HL)              
46C0: 21 10 C3        LD      HL,$C310            
46C3: 19              ADD     HL,DE               
46C4: 77              LD      (HL),A              
46C5: 21 10 C2        LD      HL,$C210            
46C8: 09              ADD     HL,BC               
46C9: 7E              LD      A,(HL)              
46CA: C6 02           ADD     $02                 
46CC: 21 10 C2        LD      HL,$C210            
46CF: 19              ADD     HL,DE               
46D0: 77              LD      (HL),A              
46D1: 21 80 C3        LD      HL,$C380            
46D4: 09              ADD     HL,BC               
46D5: 7E              LD      A,(HL)              
46D6: E6 01           AND     $01                 
46D8: F6 02           OR      $02                 
46DA: CD 87 3B        CALL    $3B87               
46DD: C9              RET                         
46DE: AF              XOR     A                   
46DF: CD A0 46        CALL    $46A0               ; {}
46E2: CD 91 08        CALL    $0891               
46E5: 20 2A           JR      NZ,$4711            ; {}
46E7: 36 20           LD      (HL),$20            
46E9: FA 01 D2        LD      A,($D201)           
46EC: 5F              LD      E,A                 
46ED: 50              LD      D,B                 
46EE: 21 90 C2        LD      HL,$C290            
46F1: 19              ADD     HL,DE               
46F2: 36 04           LD      (HL),$04            
46F4: C5              PUSH    BC                  
46F5: D5              PUSH    DE                  
46F6: C1              POP     BC                  
46F7: 3E 20           LD      A,$20               
46F9: CD 25 3C        CALL    $3C25               
46FC: 21 20 C3        LD      HL,$C320            
46FF: 09              ADD     HL,BC               
4700: 36 18           LD      (HL),$18            
4702: C1              POP     BC                  
4703: 21 20 C3        LD      HL,$C320            
4706: 09              ADD     HL,BC               
4707: 36 20           LD      (HL),$20            
4709: 3E 08           LD      A,$08               
470B: E0 F2           LD      ($FF00+$F2),A       
470D: CD 8D 3B        CALL    $3B8D               
4710: C9              RET                         
4711: CD F7 45        CALL    $45F7               ; {}
4714: 3E 04           LD      A,$04               
4716: CD 25 3C        CALL    $3C25               
4719: CD 9E 65        CALL    $659E               ; {}
471C: 21 80 C3        LD      HL,$C380            
471F: 09              ADD     HL,BC               
4720: 73              LD      (HL),E              
4721: CD D1 46        CALL    $46D1               ; {}
4724: CD 4B 65        CALL    $654B               ; {}
4727: CD 9E 3B        CALL    $3B9E               
472A: C9              RET                         
472B: CD 91 08        CALL    $0891               
472E: 20 04           JR      NZ,$4734            ; {}
4730: CD 8D 3B        CALL    $3B8D               
4733: 70              LD      (HL),B              
4734: 21 80 C3        LD      HL,$C380            
4737: 09              ADD     HL,BC               
4738: 7E              LD      A,(HL)              
4739: E6 01           AND     $01                 
473B: CD 87 3B        CALL    $3B87               
473E: C9              RET                         
473F: 00              NOP                         
4740: FC                              
4741: 64              LD      H,H                 
4742: 20 00           JR      NZ,$4744            ; {}
4744: 04              INC     B                   
4745: 62              LD      H,D                 
4746: 20 00           JR      NZ,$4748            ; {}
4748: 0C              INC     C                   
4749: 60              LD      H,B                 
474A: 20 F0           JR      NZ,$473C            ; {}
474C: FC                              
474D: 6C              LD      L,H                 
474E: 20 00           JR      NZ,$4750            ; {}
4750: FC                              
4751: 60              LD      H,B                 
4752: 00              NOP                         
4753: 00              NOP                         
4754: 04              INC     B                   
4755: 62              LD      H,D                 
4756: 00              NOP                         
4757: 00              NOP                         
4758: 0C              INC     C                   
4759: 64              LD      H,H                 
475A: 00              NOP                         
475B: F0 0C           LD      A,($0C)             
475D: 6C              LD      L,H                 
475E: 00              NOP                         
475F: 00              NOP                         
4760: FC                              
4761: 6A              LD      L,D                 
4762: 20 00           JR      NZ,$4764            ; {}
4764: 04              INC     B                   
4765: 68              LD      L,B                 
4766: 20 00           JR      NZ,$4768            ; {}
4768: 0C              INC     C                   
4769: 66              LD      H,(HL)              
476A: 20 F0           JR      NZ,$475C            ; {}
476C: FC                              
476D: 6C              LD      L,H                 
476E: 00              NOP                         
476F: 00              NOP                         
4770: FC                              
4771: 66              LD      H,(HL)              
4772: 00              NOP                         
4773: 00              NOP                         
4774: 04              INC     B                   
4775: 68              LD      L,B                 
4776: 00              NOP                         
4777: 00              NOP                         
4778: 0C              INC     C                   
4779: 6A              LD      L,D                 
477A: 00              NOP                         
477B: F0 0C           LD      A,($0C)             
477D: 6C              LD      L,H                 
477E: 20 F0           JR      NZ,$4770            ; {}
4780: F1              POP     AF                  
4781: 17              RLA                         
4782: 17              RLA                         
4783: 17              RLA                         
4784: 17              RLA                         
4785: E6 F0           AND     $F0                 
4787: 5F              LD      E,A                 
4788: 50              LD      D,B                 
4789: 21 3F 47        LD      HL,$473F            
478C: 19              ADD     HL,DE               
478D: 0E 04           LD      C,$04               
478F: CD 26 3D        CALL    $3D26               
4792: C3 19 3D        JP      $3D19               
4795: 6E              LD      L,(HL)              
4796: 00              NOP                         
4797: 6E              LD      L,(HL)              
4798: 20 21           JR      NZ,$47BB            ; {}
479A: 40              LD      B,B                 
479B: C3 09 36        JP      $3609               
479E: 92              SUB     D                   
479F: 21 D0 C5        LD      HL,$C5D0            
47A2: 09              ADD     HL,BC               
47A3: 36 FF           LD      (HL),$FF            
47A5: 11 95 47        LD      DE,$4795            
47A8: CD 3B 3C        CALL    $3C3B               
47AB: CD DF 64        CALL    $64DF               ; {}
47AE: CD E2 08        CALL    $08E2               
47B1: CD EB 3B        CALL    $3BEB               
47B4: CD 4B 65        CALL    $654B               ; {}
47B7: CD 84 65        CALL    $6584               ; {}
47BA: 21 20 C3        LD      HL,$C320            
47BD: 09              ADD     HL,BC               
47BE: 35              DEC     (HL)                
47BF: 35              DEC     (HL)                
47C0: 21 10 C3        LD      HL,$C310            
47C3: 09              ADD     HL,BC               
47C4: 7E              LD      A,(HL)              
47C5: E0 E9           LD      ($FF00+$E9),A       
47C7: E6 80           AND     $80                 
47C9: E0 E8           LD      ($FF00+$E8),A       
47CB: 28 25           JR      Z,$47F2             ; {}
47CD: 70              LD      (HL),B              
47CE: 21 20 C3        LD      HL,$C320            
47D1: 09              ADD     HL,BC               
47D2: 7E              LD      A,(HL)              
47D3: CB 2F           SRA     1,E                 
47D5: 2F              CPL                         
47D6: FE 07           CP      $07                 
47D8: 30 03           JR      NC,$47DD            ; {}
47DA: AF              XOR     A                   
47DB: 18 04           JR      $47E1               ; {}
47DD: 3E 09           LD      A,$09               
47DF: E0 F2           LD      ($FF00+$F2),A       
47E1: 77              LD      (HL),A              
47E2: 21 40 C2        LD      HL,$C240            
47E5: 09              ADD     HL,BC               
47E6: CB 2E           SRA     1,E                 
47E8: CB 2E           SRA     1,E                 
47EA: 21 50 C2        LD      HL,$C250            
47ED: 09              ADD     HL,BC               
47EE: CB 2E           SRA     1,E                 
47F0: CB 2E           SRA     1,E                 
47F2: CD 9E 3B        CALL    $3B9E               
47F5: F0 F0           LD      A,($F0)             
47F7: C7              RST     0X00                
47F8: 02              LD      (BC),A              
47F9: 48              LD      C,B                 
47FA: 6B              LD      L,E                 
47FB: 48              LD      C,B                 
47FC: 6C              LD      L,H                 
47FD: 48              LD      C,B                 
47FE: 6D              LD      L,L                 
47FF: 48              LD      C,B                 
4800: F5              PUSH    AF                  
4801: 48              LD      C,B                 
4802: F0 E9           LD      A,($E9)             
4804: 3D              DEC     A                   
4805: E6 80           AND     $80                 
4807: 28 15           JR      Z,$481E             ; {}
4809: 21 50 C2        LD      HL,$C250            
480C: CD 12 48        CALL    $4812               ; {}
480F: 21 40 C2        LD      HL,$C240            
4812: 09              ADD     HL,BC               
4813: 7E              LD      A,(HL)              
4814: A7              AND     A                   
4815: 28 07           JR      Z,$481E             ; {}
4817: E6 80           AND     $80                 
4819: 28 02           JR      Z,$481D             ; {}
481B: 34              INC     (HL)                
481C: 34              INC     (HL)                
481D: 35              DEC     (HL)                
481E: CD D5 3B        CALL    $3BD5               
4821: 30 47           JR      NC,$486A            ; {}
4823: FA 9B C1        LD      A,($C19B)           
4826: A7              AND     A                   
4827: 20 41           JR      NZ,$486A            ; {}
4829: FA 00 DB        LD      A,($DB00)           
482C: FE 03           CP      $03                 
482E: 20 08           JR      NZ,$4838            ; {}
4830: F0 CC           LD      A,($CC)             
4832: E6 20           AND     $20                 
4834: 20 0F           JR      NZ,$4845            ; {}
4836: 18 32           JR      $486A               ; {}
4838: FA 01 DB        LD      A,($DB01)           
483B: FE 03           CP      $03                 
483D: 20 2B           JR      NZ,$486A            ; {}
483F: F0 CC           LD      A,($CC)             
4841: E6 10           AND     $10                 
4843: 28 25           JR      Z,$486A             ; {}
4845: FA CF C3        LD      A,($C3CF)           
4848: A7              AND     A                   
4849: 20 1F           JR      NZ,$486A            ; {}
484B: CD 8D 3B        CALL    $3B8D               
484E: 36 02           LD      (HL),$02            
4850: 21 80 C2        LD      HL,$C280            
4853: 09              ADD     HL,BC               
4854: 36 07           LD      (HL),$07            
4856: 21 90 C4        LD      HL,$C490            
4859: 09              ADD     HL,BC               
485A: 70              LD      (HL),B              
485B: F0 9E           LD      A,($9E)             
485D: EA 5D C1        LD      ($C15D),A           
4860: CD 91 08        CALL    $0891               
4863: 36 02           LD      (HL),$02            
4865: 21 F3 FF        LD      HL,$FFF3            
4868: 36 02           LD      (HL),$02            
486A: C9              RET                         
486B: C9              RET                         
486C: C9              RET                         
486D: FA 02 D2        LD      A,($D202)           
4870: 5F              LD      E,A                 
4871: 50              LD      D,B                 
4872: 21 00 C2        LD      HL,$C200            
4875: 19              ADD     HL,DE               
4876: F0 EE           LD      A,($EE)             
4878: 96              SUB     (HL)                
4879: C6 0C           ADD     $0C                 
487B: FE 18           CP      $18                 
487D: D2 F3 48        JP      NC,$48F3            ; {}
4880: 21 10 C2        LD      HL,$C210            
4883: 19              ADD     HL,DE               
4884: F0 EC           LD      A,($EC)             
4886: 96              SUB     (HL)                
4887: C6 0C           ADD     $0C                 
4889: FE 18           CP      $18                 
488B: 30 66           JR      NC,$48F3            ; {}
488D: 21 10 C4        LD      HL,$C410            
4890: 19              ADD     HL,DE               
4891: 36 10           LD      (HL),$10            
4893: 21 20 C4        LD      HL,$C420            
4896: 19              ADD     HL,DE               
4897: 36 20           LD      (HL),$20            
4899: 21 40 C2        LD      HL,$C240            
489C: 09              ADD     HL,BC               
489D: 7E              LD      A,(HL)              
489E: E5              PUSH    HL                  
489F: 21 F0 C3        LD      HL,$C3F0            
48A2: 19              ADD     HL,DE               
48A3: 77              LD      (HL),A              
48A4: E1              POP     HL                  
48A5: 2F              CPL                         
48A6: 3C              INC     A                   
48A7: CB 2F           SRA     1,E                 
48A9: 77              LD      (HL),A              
48AA: 21 50 C2        LD      HL,$C250            
48AD: 09              ADD     HL,BC               
48AE: 7E              LD      A,(HL)              
48AF: E5              PUSH    HL                  
48B0: 21 00 C4        LD      HL,$C400            
48B3: 19              ADD     HL,DE               
48B4: 77              LD      (HL),A              
48B5: E1              POP     HL                  
48B6: 2F              CPL                         
48B7: 3C              INC     A                   
48B8: CB 2F           SRA     1,E                 
48BA: 77              LD      (HL),A              
48BB: 3E 07           LD      A,$07               
48BD: E0 F3           LD      ($FF00+$F3),A       
48BF: 21 60 C3        LD      HL,$C360            
48C2: 19              ADD     HL,DE               
48C3: 7E              LD      A,(HL)              
48C4: D6 02           SUB     $02                 
48C6: 77              LD      (HL),A              
48C7: 3D              DEC     A                   
48C8: E6 80           AND     $80                 
48CA: 28 23           JR      Z,$48EF             ; {}
48CC: 21 80 C2        LD      HL,$C280            
48CF: 19              ADD     HL,DE               
48D0: 36 01           LD      (HL),$01            
48D2: 21 80 C2        LD      HL,$C280            
48D5: 09              ADD     HL,BC               
48D6: 36 01           LD      (HL),$01            
48D8: 21 80 C4        LD      HL,$C480            
48DB: 09              ADD     HL,BC               
48DC: 36 1F           LD      (HL),$1F            
48DE: 21 40 C3        LD      HL,$C340            
48E1: 09              ADD     HL,BC               
48E2: 7E              LD      A,(HL)              
48E3: 36 04           LD      (HL),$04            
48E5: 21 30 C4        LD      HL,$C430            
48E8: 09              ADD     HL,BC               
48E9: CB BE           RES     1,E                 
48EB: 3E 10           LD      A,$10               
48ED: E0 F3           LD      ($FF00+$F3),A       
48EF: CD 8D 3B        CALL    $3B8D               
48F2: 70              LD      (HL),B              
48F3: 18 0F           JR      $4904               ; {}
48F5: 21 40 C3        LD      HL,$C340            
48F8: 09              ADD     HL,BC               
48F9: 36 12           LD      (HL),$12            
48FB: CD BF 3B        CALL    $3BBF               
48FE: 21 40 C3        LD      HL,$C340            
4901: 09              ADD     HL,BC               
4902: 36 92           LD      (HL),$92            
4904: F0 E8           LD      A,($E8)             
4906: A7              AND     A                   
4907: 20 1B           JR      NZ,$4924            ; {}
4909: 21 A0 C2        LD      HL,$C2A0            
490C: 09              ADD     HL,BC               
490D: 7E              LD      A,(HL)              
490E: A7              AND     A                   
490F: 28 17           JR      Z,$4928             ; {}
4911: E6 03           AND     $03                 
4913: 28 05           JR      Z,$491A             ; {}
4915: 21 40 C2        LD      HL,$C240            
4918: 18 03           JR      $491D               ; {}
491A: 21 50 C2        LD      HL,$C250            
491D: 09              ADD     HL,BC               
491E: 7E              LD      A,(HL)              
491F: 2F              CPL                         
4920: 3C              INC     A                   
4921: CB 2F           SRA     1,E                 
4923: 77              LD      (HL),A              
4924: CD 8D 3B        CALL    $3B8D               
4927: 70              LD      (HL),B              
4928: C9              RET                         
4929: 74              LD      (HL),H              
492A: 00              NOP                         
492B: 76              HALT                        
492C: 00              NOP                         
492D: 76              HALT                        
492E: 20 74           JR      NZ,$49A4            ; {}
4930: 20 70           JR      NZ,$49A2            ; {}
4932: 00              NOP                         
4933: 72              LD      (HL),D              
4934: 00              NOP                         
4935: 72              LD      (HL),D              
4936: 20 70           JR      NZ,$49A8            ; {}
4938: 20 78           JR      NZ,$49B2            ; {}
493A: 00              NOP                         
493B: 7A              LD      A,D                 
493C: 00              NOP                         
493D: 7A              LD      A,D                 
493E: 20 78           JR      NZ,$49B8            ; {}
4940: 20 7C           JR      NZ,$49BE            ; {}
4942: 00              NOP                         
4943: 7E              LD      A,(HL)              
4944: 00              NOP                         
4945: 7E              LD      A,(HL)              
4946: 20 7C           JR      NZ,$49C4            ; {}
4948: 20 21           JR      NZ,$496B            ; {}
494A: 60              LD      H,B                 
494B: C3 09 36        JP      $3609               
494E: 20 11           JR      NZ,$4961            ; {}
4950: 29              ADD     HL,HL               
4951: 49              LD      C,C                 
4952: CD 3B 3C        CALL    $3C3B               
4955: CD DF 64        CALL    $64DF               ; {}
4958: CD E2 08        CALL    $08E2               
495B: CD 4B 65        CALL    $654B               ; {}
495E: CD 9E 3B        CALL    $3B9E               
4961: F0 F0           LD      A,($F0)             
4963: C7              RST     0X00                
4964: 6A              LD      L,D                 
4965: 49              LD      C,C                 
4966: BD              CP      L                   
4967: 49              LD      C,C                 
4968: EE 49           XOR     $49                 
496A: CD B4 3B        CALL    $3BB4               
496D: CD 91 08        CALL    $0891               
4970: 20 08           JR      NZ,$497A            ; {}
4972: 36 20           LD      (HL),$20            
4974: CD AF 3D        CALL    $3DAF               
4977: CD 8D 3B        CALL    $3B8D               
497A: 21 D0 C3        LD      HL,$C3D0            
497D: 09              ADD     HL,BC               
497E: 34              INC     (HL)                
497F: 21 80 C3        LD      HL,$C380            
4982: 09              ADD     HL,BC               
4983: F0 E7           LD      A,($E7)             
4985: E6 0F           AND     $0F                 
4987: 20 05           JR      NZ,$498E            ; {}
4989: 7E              LD      A,(HL)              
498A: 3C              INC     A                   
498B: E6 03           AND     $03                 
498D: 77              LD      (HL),A              
498E: 5E              LD      E,(HL)              
498F: CB 23           SLA     1,E                 
4991: 21 D0 C3        LD      HL,$C3D0            
4994: 09              ADD     HL,BC               
4995: 7E              LD      A,(HL)              
4996: 1F              RRA                         
4997: 1F              RRA                         
4998: 1F              RRA                         
4999: E6 01           AND     $01                 
499B: B3              OR      E                   
499C: CD 87 3B        CALL    $3B87               
499F: 21 10 C4        LD      HL,$C410            
49A2: 09              ADD     HL,BC               
49A3: 7E              LD      A,(HL)              
49A4: A7              AND     A                   
49A5: 28 0D           JR      Z,$49B4             ; {}
49A7: CD 8D 3B        CALL    $3B8D               
49AA: 36 02           LD      (HL),$02            
49AC: CD 91 08        CALL    $0891               
49AF: 36 40           LD      (HL),$40            
49B1: CD AF 3D        CALL    $3DAF               
49B4: C9              RET                         
49B5: 0C              INC     C                   
49B6: F4                              
49B7: 00              NOP                         
49B8: 00              NOP                         
49B9: 00              NOP                         
49BA: 00              NOP                         
49BB: F4                              
49BC: 0C              INC     C                   
49BD: CD B4 3B        CALL    $3BB4               
49C0: CD 91 08        CALL    $0891               
49C3: 20 27           JR      NZ,$49EC            ; {}
49C5: CD ED 27        CALL    $27ED               
49C8: E6 1F           AND     $1F                 
49CA: C6 20           ADD     $20                 
49CC: 77              LD      (HL),A              
49CD: CD 8D 3B        CALL    $3B8D               
49D0: 70              LD      (HL),B              
49D1: CD ED 27        CALL    $27ED               
49D4: E6 03           AND     $03                 
49D6: 5F              LD      E,A                 
49D7: 50              LD      D,B                 
49D8: 21 B5 49        LD      HL,$49B5            
49DB: 19              ADD     HL,DE               
49DC: 7E              LD      A,(HL)              
49DD: 21 40 C2        LD      HL,$C240            
49E0: 09              ADD     HL,BC               
49E1: 77              LD      (HL),A              
49E2: 21 B9 49        LD      HL,$49B9            
49E5: 19              ADD     HL,DE               
49E6: 7E              LD      A,(HL)              
49E7: 21 50 C2        LD      HL,$C250            
49EA: 09              ADD     HL,BC               
49EB: 77              LD      (HL),A              
49EC: 18 91           JR      $497F               ; {}
49EE: 21 60 C4        LD      HL,$C460            
49F1: 09              ADD     HL,BC               
49F2: 7E              LD      A,(HL)              
49F3: A7              AND     A                   
49F4: C2 C1 4A        JP      NZ,$4AC1            ; {}
49F7: E0 D7           LD      ($FF00+$D7),A       
49F9: 1E 0F           LD      E,$0F               
49FB: 50              LD      D,B                 
49FC: 21 80 C2        LD      HL,$C280            
49FF: 19              ADD     HL,DE               
4A00: 7E              LD      A,(HL)              
4A01: A7              AND     A                   
4A02: 28 1F           JR      Z,$4A23             ; {}
4A04: 21 A0 C3        LD      HL,$C3A0            
4A07: 19              ADD     HL,DE               
4A08: 7E              LD      A,(HL)              
4A09: FE 90           CP      $90                 
4A0B: 20 16           JR      NZ,$4A23            ; {}
4A0D: 21 90 C2        LD      HL,$C290            
4A10: 19              ADD     HL,DE               
4A11: 7E              LD      A,(HL)              
4A12: FE 02           CP      $02                 
4A14: 20 0D           JR      NZ,$4A23            ; {}
4A16: 21 E0 C2        LD      HL,$C2E0            
4A19: 19              ADD     HL,DE               
4A1A: 7E              LD      A,(HL)              
4A1B: A7              AND     A                   
4A1C: 20 05           JR      NZ,$4A23            ; {}
4A1E: F0 D7           LD      A,($D7)             
4A20: 3C              INC     A                   
4A21: E0 D7           LD      ($FF00+$D7),A       
4A23: 1D              DEC     E                   
4A24: 7B              LD      A,E                 
4A25: FE FF           CP      $FF                 
4A27: 20 D3           JR      NZ,$49FC            ; {}
4A29: F0 D7           LD      A,($D7)             
4A2B: FE 03           CP      $03                 
4A2D: C2 C1 4A        JP      NZ,$4AC1            ; {}
4A30: C5              PUSH    BC                  
4A31: 48              LD      C,B                 
4A32: 1E 0F           LD      E,$0F               
4A34: 50              LD      D,B                 
4A35: 21 80 C2        LD      HL,$C280            
4A38: 19              ADD     HL,DE               
4A39: 7E              LD      A,(HL)              
4A3A: A7              AND     A                   
4A3B: 28 14           JR      Z,$4A51             ; {}
4A3D: 21 A0 C3        LD      HL,$C3A0            
4A40: 19              ADD     HL,DE               
4A41: 7E              LD      A,(HL)              
4A42: FE 90           CP      $90                 
4A44: 20 0B           JR      NZ,$4A51            ; {}
4A46: 21 80 C3        LD      HL,$C380            
4A49: 19              ADD     HL,DE               
4A4A: 7E              LD      A,(HL)              
4A4B: 21 D9 FF        LD      HL,$FFD9            
4A4E: 09              ADD     HL,BC               
4A4F: 77              LD      (HL),A              
4A50: 03              INC     BC                  
4A51: 1D              DEC     E                   
4A52: 7B              LD      A,E                 
4A53: FE FF           CP      $FF                 
4A55: 20 DE           JR      NZ,$4A35            ; {}
4A57: C1              POP     BC                  
4A58: CD AC 08        CALL    $08AC               
4A5B: 1E 00           LD      E,$00               
4A5D: F0 D9           LD      A,($D9)             
4A5F: 21 DA FF        LD      HL,$FFDA            
4A62: BE              CP      (HL)                
4A63: 20 17           JR      NZ,$4A7C            ; {}
4A65: 23              INC     HL                  
4A66: BE              CP      (HL)                
4A67: 20 13           JR      NZ,$4A7C            ; {}
4A69: 1E FF           LD      E,$FF               
4A6B: FE 02           CP      $02                 
4A6D: 30 0D           JR      NC,$4A7C            ; {}
4A6F: 21 F2 FF        LD      HL,$FFF2            
4A72: 36 02           LD      (HL),$02            
4A74: 1E 2D           LD      E,$2D               
4A76: FE 01           CP      $01                 
4A78: 20 02           JR      NZ,$4A7C            ; {}
4A7A: 1E 2E           LD      E,$2E               
4A7C: 7B              LD      A,E                 
4A7D: E0 E8           LD      ($FF00+$E8),A       
4A7F: 1E 0F           LD      E,$0F               
4A81: 50              LD      D,B                 
4A82: 21 80 C2        LD      HL,$C280            
4A85: 19              ADD     HL,DE               
4A86: 7E              LD      A,(HL)              
4A87: A7              AND     A                   
4A88: 28 31           JR      Z,$4ABB             ; {}
4A8A: 21 A0 C3        LD      HL,$C3A0            
4A8D: 19              ADD     HL,DE               
4A8E: 7E              LD      A,(HL)              
4A8F: FE 90           CP      $90                 
4A91: 20 28           JR      NZ,$4ABB            ; {}
4A93: F0 E8           LD      A,($E8)             
4A95: A7              AND     A                   
4A96: 20 07           JR      NZ,$4A9F            ; {}
4A98: 21 90 C2        LD      HL,$C290            
4A9B: 19              ADD     HL,DE               
4A9C: 72              LD      (HL),D              
4A9D: 18 1C           JR      $4ABB               ; {}
4A9F: 21 E0 C4        LD      HL,$C4E0            
4AA2: 19              ADD     HL,DE               
4AA3: 77              LD      (HL),A              
4AA4: 21 80 C4        LD      HL,$C480            
4AA7: 19              ADD     HL,DE               
4AA8: 36 1F           LD      (HL),$1F            
4AAA: 21 80 C2        LD      HL,$C280            
4AAD: 19              ADD     HL,DE               
4AAE: 36 01           LD      (HL),$01            
4AB0: 21 40 C3        LD      HL,$C340            
4AB3: 19              ADD     HL,DE               
4AB4: 36 04           LD      (HL),$04            
4AB6: 21 F4 FF        LD      HL,$FFF4            
4AB9: 36 13           LD      (HL),$13            
4ABB: 1D              DEC     E                   
4ABC: 7B              LD      A,E                 
4ABD: FE FF           CP      $FF                 
4ABF: 20 C1           JR      NZ,$4A82            ; {}
4AC1: C9              RET                         
4AC2: 4A              LD      C,D                 
4AC3: 00              NOP                         
4AC4: 4C              LD      C,H                 
4AC5: 00              NOP                         
4AC6: 4C              LD      C,H                 
4AC7: 20 4A           JR      NZ,$4B13            ; {}
4AC9: 20 4E           JR      NZ,$4B19            ; {}
4ACB: 00              NOP                         
4ACC: 4E              LD      C,(HL)              
4ACD: 20 11           JR      NZ,$4AE0            ; {}
4ACF: C2 4A CD        JP      NZ,$CD4A            
4AD2: 3B              DEC     SP                  
4AD3: 3C              INC     A                   
4AD4: CD DF 64        CALL    $64DF               ; {}
4AD7: CD 01 65        CALL    $6501               ; {}
4ADA: CD B4 3B        CALL    $3BB4               
4ADD: F0 F0           LD      A,($F0)             
4ADF: C7              RST     0X00                
4AE0: E8 4A           ADD     SP,$4A              
4AE2: F1              POP     AF                  
4AE3: 4A              LD      C,D                 
4AE4: 2D              DEC     L                   
4AE5: 4B              LD      C,E                 
4AE6: 54              LD      D,H                 
4AE7: 4B              LD      C,E                 
4AE8: CD 91 08        CALL    $0891               
4AEB: 20 03           JR      NZ,$4AF0            ; {}
4AED: CD 8D 3B        CALL    $3B8D               
4AF0: C9              RET                         
4AF1: F0 E7           LD      A,($E7)             
4AF3: A9              XOR     C                   
4AF4: E6 03           AND     $03                 
4AF6: 20 05           JR      NZ,$4AFD            ; {}
4AF8: 3E 08           LD      A,$08               
4AFA: CD 25 3C        CALL    $3C25               
4AFD: CD 9E 65        CALL    $659E               ; {}
4B00: C6 1C           ADD     $1C                 
4B02: FE 38           CP      $38                 
4B04: 30 17           JR      NC,$4B1D            ; {}
4B06: CD AE 65        CALL    $65AE               ; {}
4B09: C6 1C           ADD     $1C                 
4B0B: FE 38           CP      $38                 
4B0D: 30 0E           JR      NC,$4B1D            ; {}
4B0F: 21 20 C3        LD      HL,$C320            
4B12: 09              ADD     HL,BC               
4B13: 36 28           LD      (HL),$28            
4B15: 3E 10           LD      A,$10               
4B17: CD 25 3C        CALL    $3C25               
4B1A: CD 8D 3B        CALL    $3B8D               
4B1D: CD 4B 65        CALL    $654B               ; {}
4B20: CD 9E 3B        CALL    $3B9E               
4B23: F0 E7           LD      A,($E7)             
4B25: 1F              RRA                         
4B26: 1F              RRA                         
4B27: E6 01           AND     $01                 
4B29: CD 87 3B        CALL    $3B87               
4B2C: C9              RET                         
4B2D: CD 4B 65        CALL    $654B               ; {}
4B30: CD 9E 3B        CALL    $3B9E               
4B33: CD 84 65        CALL    $6584               ; {}
4B36: 21 20 C3        LD      HL,$C320            
4B39: 09              ADD     HL,BC               
4B3A: 35              DEC     (HL)                
4B3B: 35              DEC     (HL)                
4B3C: 7E              LD      A,(HL)              
4B3D: FE 02           CP      $02                 
4B3F: 30 0D           JR      NC,$4B4E            ; {}
4B41: 36 C0           LD      (HL),$C0            
4B43: CD 91 08        CALL    $0891               
4B46: 36 10           LD      (HL),$10            
4B48: CD AF 3D        CALL    $3DAF               
4B4B: CD 8D 3B        CALL    $3B8D               
4B4E: 3E 02           LD      A,$02               
4B50: CD 87 3B        CALL    $3B87               
4B53: C9              RET                         
4B54: CD 91 08        CALL    $0891               
4B57: 20 34           JR      NZ,$4B8D            ; {}
4B59: CD 84 65        CALL    $6584               ; {}
4B5C: 21 10 C3        LD      HL,$C310            
4B5F: 09              ADD     HL,BC               
4B60: 7E              LD      A,(HL)              
4B61: A7              AND     A                   
4B62: 28 04           JR      Z,$4B68             ; {}
4B64: E6 80           AND     $80                 
4B66: 28 25           JR      Z,$4B8D             ; {}
4B68: 70              LD      (HL),B              
4B69: CD 91 08        CALL    $0891               
4B6C: 36 20           LD      (HL),$20            
4B6E: CD 8D 3B        CALL    $3B8D               
4B71: 70              LD      (HL),B              
4B72: 21 20 C3        LD      HL,$C320            
4B75: 09              ADD     HL,BC               
4B76: 7E              LD      A,(HL)              
4B77: 70              LD      (HL),B              
4B78: CB 7F           BIT     1,E                 
4B7A: 28 11           JR      Z,$4B8D             ; {}
4B7C: FE D0           CP      $D0                 
4B7E: 30 0D           JR      NC,$4B8D            ; {}
4B80: F0 EE           LD      A,($EE)             
4B82: E0 D7           LD      ($FF00+$D7),A       
4B84: F0 EC           LD      A,($EC)             
4B86: C6 0C           ADD     $0C                 
4B88: E0 D8           LD      ($FF00+$D8),A       
4B8A: CD A1 09        CALL    $09A1               
4B8D: C9              RET                         
4B8E: 00              NOP                         
4B8F: 03              INC     BC                  
4B90: 01 02 21        LD      BC,$2102            
4B93: B0              OR      B                   
4B94: C2 09 7E        JP      NZ,$7E09            ; {}
4B97: A7              AND     A                   
4B98: C2 A4 4E        JP      NZ,$4EA4            ; {}
4B9B: 21 D0 C2        LD      HL,$C2D0            
4B9E: 09              ADD     HL,BC               
4B9F: 7E              LD      A,(HL)              
4BA0: A7              AND     A                   
4BA1: 20 0D           JR      NZ,$4BB0            ; {}
4BA3: 34              INC     (HL)                
4BA4: 21 60 C3        LD      HL,$C360            
4BA7: 09              ADD     HL,BC               
4BA8: 36 08           LD      (HL),$08            
4BAA: 21 40 C4        LD      HL,$C440            
4BAD: 09              ADD     HL,BC               
4BAE: 36 01           LD      (HL),$01            
4BB0: CD 0E 38        CALL    $380E               
4BB3: CD 7F 4E        CALL    $4E7F               ; {}
4BB6: F0 EA           LD      A,($EA)             
4BB8: FE 05           CP      $05                 
4BBA: C2 CB 53        JP      NZ,$53CB            ; {}
4BBD: CD DF 64        CALL    $64DF               ; {}
4BC0: CD 12 3F        CALL    $3F12               
4BC3: CD E2 08        CALL    $08E2               
4BC6: CD BF 3B        CALL    $3BBF               
4BC9: CD 4B 65        CALL    $654B               ; {}
4BCC: FA 46 C1        LD      A,($C146)           
4BCF: A7              AND     A                   
4BD0: 20 27           JR      NZ,$4BF9            ; {}
4BD2: 21 30 C4        LD      HL,$C430            
4BD5: 09              ADD     HL,BC               
4BD6: 36 C4           LD      (HL),$C4            
4BD8: F0 F0           LD      A,($F0)             
4BDA: A7              AND     A                   
4BDB: 20 19           JR      NZ,$4BF6            ; {}
4BDD: 21 80 C3        LD      HL,$C380            
4BE0: 09              ADD     HL,BC               
4BE1: 5E              LD      E,(HL)              
4BE2: 50              LD      D,B                 
4BE3: 21 8E 4B        LD      HL,$4B8E            
4BE6: 19              ADD     HL,DE               
4BE7: 7E              LD      A,(HL)              
4BE8: F5              PUSH    AF                  
4BE9: CD BE 65        CALL    $65BE               ; {}
4BEC: F1              POP     AF                  
4BED: BB              CP      E                   
4BEE: 28 06           JR      Z,$4BF6             ; {}
4BF0: 21 30 C4        LD      HL,$C430            
4BF3: 09              ADD     HL,BC               
4BF4: 36 84           LD      (HL),$84            
4BF6: CD EB 3B        CALL    $3BEB               
4BF9: F0 F0           LD      A,($F0)             
4BFB: C7              RST     0X00                
4BFC: 38 4C           JR      C,$4C4A             ; {}
4BFE: 55              LD      D,L                 
4BFF: 4D              LD      C,L                 
4C00: 14              INC     D                   
4C01: 00              NOP                         
4C02: EC                              
4C03: 00              NOP                         
4C04: 00              NOP                         
4C05: 14              INC     D                   
4C06: 00              NOP                         
4C07: EC                              
4C08: 06 07           LD      B,$07               
4C0A: 00              NOP                         
4C0B: 01 04 05        LD      BC,$0504            
4C0E: 02              LD      (BC),A              
4C0F: 03              INC     BC                  
4C10: 10 10           ;;STOP    $10                 
4C12: F4                              
4C13: 0C              INC     C                   
4C14: F0 F0           LD      A,($F0)             
4C16: F4                              
4C17: 0C              INC     C                   
4C18: F4                              
4C19: 0C              INC     C                   
4C1A: 10 10           ;;STOP    $10                 
4C1C: F4                              
4C1D: 0C              INC     C                   
4C1E: F0 F0           LD      A,($F0)             
4C20: 80              ADD     A,B                 
4C21: 80              ADD     A,B                 
4C22: 80              ADD     A,B                 
4C23: 7F              LD      A,A                 
4C24: 7F              LD      A,A                 
4C25: 7F              LD      A,A                 
4C26: 80              ADD     A,B                 
4C27: 7F              LD      A,A                 
4C28: 80              ADD     A,B                 
4C29: 7F              LD      A,A                 
4C2A: 80              ADD     A,B                 
4C2B: 80              ADD     A,B                 
4C2C: 80              ADD     A,B                 
4C2D: 7F              LD      A,A                 
4C2E: 7F              LD      A,A                 
4C2F: 7F              LD      A,A                 
4C30: 00              NOP                         
4C31: 02              LD      (BC),A              
4C32: 00              NOP                         
4C33: 01 01 03        LD      BC,$0301            
4C36: 02              LD      (BC),A              
4C37: 03              INC     BC                  
4C38: 21 20 C4        LD      HL,$C420            
4C3B: 09              ADD     HL,BC               
4C3C: 7E              LD      A,(HL)              
4C3D: A7              AND     A                   
4C3E: 28 28           JR      Z,$4C68             ; {}
4C40: CD 72 4C        CALL    $4C72               ; {}
4C43: CD 8D 3B        CALL    $3B8D               
4C46: 21 80 C3        LD      HL,$C380            
4C49: 09              ADD     HL,BC               
4C4A: 7E              LD      A,(HL)              
4C4B: 21 90 C3        LD      HL,$C390            
4C4E: 09              ADD     HL,BC               
4C4F: 77              LD      (HL),A              
4C50: CD 91 08        CALL    $0891               
4C53: 36 58           LD      (HL),$58            
4C55: CD ED 27        CALL    $27ED               
4C58: E6 01           AND     $01                 
4C5A: 20 08           JR      NZ,$4C64            ; {}
4C5C: 21 40 C4        LD      HL,$C440            
4C5F: 09              ADD     HL,BC               
4C60: 7E              LD      A,(HL)              
4C61: 2F              CPL                         
4C62: 3C              INC     A                   
4C63: 77              LD      (HL),A              
4C64: CD AF 3D        CALL    $3DAF               
4C67: C9              RET                         
4C68: CD 91 08        CALL    $0891               
4C6B: 28 05           JR      Z,$4C72             ; {}
4C6D: FE 01           CP      $01                 
4C6F: 28 2C           JR      Z,$4C9D             ; {}
4C71: C9              RET                         
4C72: 21 00 C2        LD      HL,$C200            
4C75: 09              ADD     HL,BC               
4C76: 7E              LD      A,(HL)              
4C77: FE 20           CP      $20                 
4C79: 38 16           JR      C,$4C91             ; {}
4C7B: FE 80           CP      $80                 
4C7D: 30 12           JR      NC,$4C91            ; {}
4C7F: 21 10 C2        LD      HL,$C210            
4C82: 09              ADD     HL,BC               
4C83: 7E              LD      A,(HL)              
4C84: FE 28           CP      $28                 
4C86: 38 04           JR      C,$4C8C             ; {}
4C88: FE 68           CP      $68                 
4C8A: 38 1F           JR      C,$4CAB             ; {}
4C8C: F0 EF           LD      A,($EF)             
4C8E: 77              LD      (HL),A              
4C8F: 18 03           JR      $4C94               ; {}
4C91: F0 EE           LD      A,($EE)             
4C93: 77              LD      (HL),A              
4C94: CD 91 08        CALL    $0891               
4C97: 36 15           LD      (HL),$15            
4C99: CD AF 3D        CALL    $3DAF               
4C9C: C9              RET                         
4C9D: 21 40 C4        LD      HL,$C440            
4CA0: 09              ADD     HL,BC               
4CA1: 5E              LD      E,(HL)              
4CA2: 21 80 C3        LD      HL,$C380            
4CA5: 09              ADD     HL,BC               
4CA6: 7E              LD      A,(HL)              
4CA7: 83              ADD     A,E                 
4CA8: E6 03           AND     $03                 
4CAA: 77              LD      (HL),A              
4CAB: 21 80 C3        LD      HL,$C380            
4CAE: 09              ADD     HL,BC               
4CAF: 7E              LD      A,(HL)              
4CB0: 5F              LD      E,A                 
4CB1: 50              LD      D,B                 
4CB2: 21 00 4C        LD      HL,$4C00            
4CB5: 19              ADD     HL,DE               
4CB6: 7E              LD      A,(HL)              
4CB7: 21 40 C2        LD      HL,$C240            
4CBA: 09              ADD     HL,BC               
4CBB: 77              LD      (HL),A              
4CBC: 21 04 4C        LD      HL,$4C04            
4CBF: 19              ADD     HL,DE               
4CC0: 7E              LD      A,(HL)              
4CC1: 21 50 C2        LD      HL,$C250            
4CC4: 09              ADD     HL,BC               
4CC5: 77              LD      (HL),A              
4CC6: CB 23           SLA     1,E                 
4CC8: F0 E7           LD      A,($E7)             
4CCA: 1F              RRA                         
4CCB: 1F              RRA                         
4CCC: 1F              RRA                         
4CCD: E6 01           AND     $01                 
4CCF: B3              OR      E                   
4CD0: E6 07           AND     $07                 
4CD2: 5F              LD      E,A                 
4CD3: 50              LD      D,B                 
4CD4: 21 08 4C        LD      HL,$4C08            
4CD7: 19              ADD     HL,DE               
4CD8: 7E              LD      A,(HL)              
4CD9: CD 87 3B        CALL    $3B87               
4CDC: F0 E7           LD      A,($E7)             
4CDE: E6 0F           AND     $0F                 
4CE0: 20 72           JR      NZ,$4D54            ; {}
4CE2: 3E 2F           LD      A,$2F               
4CE4: E0 F4           LD      ($FF00+$F4),A       
4CE6: 3E 01           LD      A,$01               
4CE8: E0 E8           LD      ($FF00+$E8),A       
4CEA: 3E 8E           LD      A,$8E               
4CEC: CD 01 3C        CALL    $3C01               
4CEF: 38 63           JR      C,$4D54             ; {}
4CF1: C5              PUSH    BC                  
4CF2: 21 80 C3        LD      HL,$C380            
4CF5: 09              ADD     HL,BC               
4CF6: 7E              LD      A,(HL)              
4CF7: CB 27           SLA     1,E                 
4CF9: 21 E8 FF        LD      HL,$FFE8            
4CFC: B6              OR      (HL)                
4CFD: 4F              LD      C,A                 
4CFE: 21 10 4C        LD      HL,$4C10            
4D01: 09              ADD     HL,BC               
4D02: F0 D7           LD      A,($D7)             
4D04: 86              ADD     A,(HL)              
4D05: 21 00 C2        LD      HL,$C200            
4D08: 19              ADD     HL,DE               
4D09: 77              LD      (HL),A              
4D0A: 21 18 4C        LD      HL,$4C18            
4D0D: 09              ADD     HL,BC               
4D0E: F0 D8           LD      A,($D8)             
4D10: 86              ADD     A,(HL)              
4D11: 21 10 C2        LD      HL,$C210            
4D14: 19              ADD     HL,DE               
4D15: 77              LD      (HL),A              
4D16: 21 20 4C        LD      HL,$4C20            
4D19: 09              ADD     HL,BC               
4D1A: 7E              LD      A,(HL)              
4D1B: 21 40 C2        LD      HL,$C240            
4D1E: 19              ADD     HL,DE               
4D1F: 77              LD      (HL),A              
4D20: 21 28 4C        LD      HL,$4C28            
4D23: 09              ADD     HL,BC               
4D24: 7E              LD      A,(HL)              
4D25: 21 50 C2        LD      HL,$C250            
4D28: 19              ADD     HL,DE               
4D29: 77              LD      (HL),A              
4D2A: 21 30 4C        LD      HL,$4C30            
4D2D: 09              ADD     HL,BC               
4D2E: 7E              LD      A,(HL)              
4D2F: 21 B0 C3        LD      HL,$C3B0            
4D32: 19              ADD     HL,DE               
4D33: 77              LD      (HL),A              
4D34: 21 B0 C2        LD      HL,$C2B0            
4D37: 19              ADD     HL,DE               
4D38: 36 01           LD      (HL),$01            
4D3A: 21 40 C3        LD      HL,$C340            
4D3D: 19              ADD     HL,DE               
4D3E: 36 C2           LD      (HL),$C2            
4D40: 21 30 C4        LD      HL,$C430            
4D43: 19              ADD     HL,DE               
4D44: 36 00           LD      (HL),$00            
4D46: 21 E0 C2        LD      HL,$C2E0            
4D49: 19              ADD     HL,DE               
4D4A: 36 0C           LD      (HL),$0C            
4D4C: C1              POP     BC                  
4D4D: F0 E8           LD      A,($E8)             
4D4F: 3D              DEC     A                   
4D50: FE FF           CP      $FF                 
4D52: 20 94           JR      NZ,$4CE8            ; {}
4D54: C9              RET                         
4D55: CD 91 08        CALL    $0891               
4D58: 20 11           JR      NZ,$4D6B            ; {}
4D5A: 21 90 C3        LD      HL,$C390            
4D5D: 09              ADD     HL,BC               
4D5E: 7E              LD      A,(HL)              
4D5F: EE 02           XOR     $02                 
4D61: 21 80 C3        LD      HL,$C380            
4D64: 09              ADD     HL,BC               
4D65: 77              LD      (HL),A              
4D66: CD 8D 3B        CALL    $3B8D               
4D69: 70              LD      (HL),B              
4D6A: C9              RET                         
4D6B: E6 03           AND     $03                 
4D6D: 20 09           JR      NZ,$4D78            ; {}
4D6F: 21 80 C3        LD      HL,$C380            
4D72: 09              ADD     HL,BC               
4D73: 7E              LD      A,(HL)              
4D74: 3C              INC     A                   
4D75: E6 03           AND     $03                 
4D77: 77              LD      (HL),A              
4D78: CD AB 4C        CALL    $4CAB               ; {}
4D7B: CD AF 3D        CALL    $3DAF               
4D7E: C9              RET                         
4D7F: F8 F8           LD      HL,SP+$F8           
4D81: 60              LD      H,B                 
4D82: 00              NOP                         
4D83: F8 00           LD      HL,SP+$00           
4D85: 62              LD      H,D                 
4D86: 00              NOP                         
4D87: F8 08           LD      HL,SP+$08           
4D89: 62              LD      H,D                 
4D8A: 20 F8           JR      NZ,$4D84            ; {}
4D8C: 10 60           ;;STOP    $60                 
4D8E: 20 08           JR      NZ,$4D98            ; {}
4D90: F8 64           LD      HL,SP+$64           
4D92: 00              NOP                         
4D93: 08 00 66        LD      ($6600),SP          ; {}
4D96: 00              NOP                         
4D97: 08 08 66        LD      ($6608),SP          ; {}
4D9A: 20 08           JR      NZ,$4DA4            ; {}
4D9C: 10 64           ;;STOP    $64                 
4D9E: 20 FA           JR      NZ,$4D9A            ; {}
4DA0: F8 60           LD      HL,SP+$60           
4DA2: 00              NOP                         
4DA3: FA 00 62        LD      A,($6200)           ; {}
4DA6: 00              NOP                         
4DA7: FA 08 62        LD      A,($6208)           ; {}
4DAA: 20 FA           JR      NZ,$4DA6            ; {}
4DAC: 10 60           ;;STOP    $60                 
4DAE: 20 08           JR      NZ,$4DB8            ; {}
4DB0: F8 64           LD      HL,SP+$64           
4DB2: 00              NOP                         
4DB3: 08 00 66        LD      ($6600),SP          ; {}
4DB6: 00              NOP                         
4DB7: 08 08 66        LD      ($6608),SP          ; {}
4DBA: 20 08           JR      NZ,$4DC4            ; {}
4DBC: 10 64           ;;STOP    $64                 
4DBE: 20 F8           JR      NZ,$4DB8            ; {}
4DC0: F8 64           LD      HL,SP+$64           
4DC2: 40              LD      B,B                 
4DC3: F8 00           LD      HL,SP+$00           
4DC5: 66              LD      H,(HL)              
4DC6: 40              LD      B,B                 
4DC7: F8 08           LD      HL,SP+$08           
4DC9: 66              LD      H,(HL)              
4DCA: 60              LD      H,B                 
4DCB: F8 10           LD      HL,SP+$10           
4DCD: 64              LD      H,H                 
4DCE: 60              LD      H,B                 
4DCF: 08 F8 60        LD      ($60F8),SP          ; {}
4DD2: 40              LD      B,B                 
4DD3: 08 00 62        LD      ($6200),SP          ; {}
4DD6: 40              LD      B,B                 
4DD7: 08 08 62        LD      ($6208),SP          ; {}
4DDA: 60              LD      H,B                 
4DDB: 08 10 60        LD      ($6010),SP          ; {}
4DDE: 60              LD      H,B                 
4DDF: F8 F8           LD      HL,SP+$F8           
4DE1: 64              LD      H,H                 
4DE2: 40              LD      B,B                 
4DE3: F8 00           LD      HL,SP+$00           
4DE5: 66              LD      H,(HL)              
4DE6: 40              LD      B,B                 
4DE7: F8 08           LD      HL,SP+$08           
4DE9: 66              LD      H,(HL)              
4DEA: 60              LD      H,B                 
4DEB: F8 10           LD      HL,SP+$10           
4DED: 64              LD      H,H                 
4DEE: 60              LD      H,B                 
4DEF: 06 F8           LD      B,$F8               
4DF1: 60              LD      H,B                 
4DF2: 40              LD      B,B                 
4DF3: 06 00           LD      B,$00               
4DF5: 62              LD      H,D                 
4DF6: 40              LD      B,B                 
4DF7: 06 08           LD      B,$08               
4DF9: 62              LD      H,D                 
4DFA: 60              LD      H,B                 
4DFB: 06 10           LD      B,$10               
4DFD: 60              LD      H,B                 
4DFE: 60              LD      H,B                 
4DFF: F8 F8           LD      HL,SP+$F8           
4E01: 68              LD      L,B                 
4E02: 00              NOP                         
4E03: F8 00           LD      HL,SP+$00           
4E05: 6A              LD      L,D                 
4E06: 00              NOP                         
4E07: F8 08           LD      HL,SP+$08           
4E09: 62              LD      H,D                 
4E0A: 20 F8           JR      NZ,$4E04            ; {}
4E0C: 10 60           ;;STOP    $60                 
4E0E: 20 08           JR      NZ,$4E18            ; {}
4E10: F8 68           LD      HL,SP+$68           
4E12: 40              LD      B,B                 
4E13: 08 00 6A        LD      ($6A00),SP          ; {}
4E16: 40              LD      B,B                 
4E17: 08 08 62        LD      ($6208),SP          ; {}
4E1A: 60              LD      H,B                 
4E1B: 08 10 60        LD      ($6010),SP          ; {}
4E1E: 60              LD      H,B                 
4E1F: F8 F8           LD      HL,SP+$F8           
4E21: 68              LD      L,B                 
4E22: 00              NOP                         
4E23: F8 00           LD      HL,SP+$00           
4E25: 6A              LD      L,D                 
4E26: 00              NOP                         
4E27: F8 06           LD      HL,SP+$06           
4E29: 62              LD      H,D                 
4E2A: 20 F8           JR      NZ,$4E24            ; {}
4E2C: 0E 60           LD      C,$60               
4E2E: 20 08           JR      NZ,$4E38            ; {}
4E30: F8 68           LD      HL,SP+$68           
4E32: 40              LD      B,B                 
4E33: 08 00 6A        LD      ($6A00),SP          ; {}
4E36: 40              LD      B,B                 
4E37: 08 06 62        LD      ($6206),SP          ; {}
4E3A: 60              LD      H,B                 
4E3B: 08 0E 60        LD      ($600E),SP          ; {}
4E3E: 60              LD      H,B                 
4E3F: F8 F8           LD      HL,SP+$F8           
4E41: 60              LD      H,B                 
4E42: 00              NOP                         
4E43: F8 00           LD      HL,SP+$00           
4E45: 62              LD      H,D                 
4E46: 00              NOP                         
4E47: F8 08           LD      HL,SP+$08           
4E49: 6A              LD      L,D                 
4E4A: 20 F8           JR      NZ,$4E44            ; {}
4E4C: 10 68           ;;STOP    $68                 
4E4E: 20 08           JR      NZ,$4E58            ; {}
4E50: F8 60           LD      HL,SP+$60           
4E52: 40              LD      B,B                 
4E53: 08 00 62        LD      ($6200),SP          ; {}
4E56: 40              LD      B,B                 
4E57: 08 08 6A        LD      ($6A08),SP          ; {}
4E5A: 60              LD      H,B                 
4E5B: 08 10 68        LD      ($6810),SP          ; {}
4E5E: 60              LD      H,B                 
4E5F: F8 FA           LD      HL,SP+$FA           
4E61: 60              LD      H,B                 
4E62: 00              NOP                         
4E63: F8 02           LD      HL,SP+$02           
4E65: 62              LD      H,D                 
4E66: 00              NOP                         
4E67: F8 08           LD      HL,SP+$08           
4E69: 6A              LD      L,D                 
4E6A: 20 F8           JR      NZ,$4E64            ; {}
4E6C: 10 68           ;;STOP    $68                 
4E6E: 20 08           JR      NZ,$4E78            ; {}
4E70: FA 60 40        LD      A,($4060)           ; {}
4E73: 08 02 62        LD      ($6202),SP          ; {}
4E76: 40              LD      B,B                 
4E77: 08 08 6A        LD      ($6A08),SP          ; {}
4E7A: 60              LD      H,B                 
4E7B: 08 10 68        LD      ($6810),SP          ; {}
4E7E: 60              LD      H,B                 
4E7F: F0 F1           LD      A,($F1)             
4E81: 17              RLA                         
4E82: 17              RLA                         
4E83: 17              RLA                         
4E84: 17              RLA                         
4E85: 17              RLA                         
4E86: E6 E0           AND     $E0                 
4E88: 5F              LD      E,A                 
4E89: 50              LD      D,B                 
4E8A: 21 7F 4D        LD      HL,$4D7F            
4E8D: 19              ADD     HL,DE               
4E8E: 0E 08           LD      C,$08               
4E90: CD 26 3D        CALL    $3D26               
4E93: C9              RET                         
4E94: 6C              LD      L,H                 
4E95: 00              NOP                         
4E96: 6E              LD      L,(HL)              
4E97: 00              NOP                         
4E98: 6E              LD      L,(HL)              
4E99: 20 6C           JR      NZ,$4F07            ; {}
4E9B: 20 6C           JR      NZ,$4F09            ; {}
4E9D: 40              LD      B,B                 
4E9E: 6E              LD      L,(HL)              
4E9F: 40              LD      B,B                 
4EA0: 6E              LD      L,(HL)              
4EA1: 60              LD      H,B                 
4EA2: 6C              LD      L,H                 
4EA3: 60              LD      H,B                 
4EA4: 11 94 4E        LD      DE,$4E94            
4EA7: CD 3B 3C        CALL    $3C3B               
4EAA: CD DF 64        CALL    $64DF               ; {}
4EAD: CD 91 08        CALL    $0891               
4EB0: CA E5 65        JP      Z,$65E5             ; {}
4EB3: FE 06           CP      $06                 
4EB5: 20 03           JR      NZ,$4EBA            ; {}
4EB7: CD 4B 65        CALL    $654B               ; {}
4EBA: C9              RET                         
4EBB: F8 10           LD      HL,SP+$10           
4EBD: FA 10 F0        LD      A,($F010)           
4EC0: F0 A7           LD      A,($A7)             
4EC2: 20 11           JR      NZ,$4ED5            ; {}
4EC4: 21 00 C2        LD      HL,$C200            
4EC7: 09              ADD     HL,BC               
4EC8: 7E              LD      A,(HL)              
4EC9: C6 08           ADD     $08                 
4ECB: 77              LD      (HL),A              
4ECC: 21 10 C3        LD      HL,$C310            
4ECF: 09              ADD     HL,BC               
4ED0: 36 10           LD      (HL),$10            
4ED2: C3 8D 3B        JP      $3B8D               
4ED5: 11 BB 4E        LD      DE,$4EBB            
4ED8: CD 3B 3C        CALL    $3C3B               
4EDB: CD DF 64        CALL    $64DF               ; {}
4EDE: F0 BA           LD      A,($BA)             
4EE0: FE 02           CP      $02                 
4EE2: 28 2C           JR      Z,$4F10             ; {}
4EE4: A7              AND     A                   
4EE5: 28 1A           JR      Z,$4F01             ; {}
4EE7: 21 D0 C3        LD      HL,$C3D0            
4EEA: 09              ADD     HL,BC               
4EEB: 34              INC     (HL)                
4EEC: 7E              LD      A,(HL)              
4EED: FE 0A           CP      $0A                 
4EEF: 20 0F           JR      NZ,$4F00            ; {}
4EF1: 70              LD      (HL),B              
4EF2: 3E 11           LD      A,$11               
4EF4: E0 F4           LD      ($FF00+$F4),A       
4EF6: 21 10 C3        LD      HL,$C310            
4EF9: 09              ADD     HL,BC               
4EFA: 7E              LD      A,(HL)              
4EFB: FE 20           CP      $20                 
4EFD: 30 01           JR      NC,$4F00            ; {}
4EFF: 34              INC     (HL)                
4F00: C9              RET                         
4F01: 21 10 C3        LD      HL,$C310            
4F04: 09              ADD     HL,BC               
4F05: 7E              LD      A,(HL)              
4F06: A7              AND     A                   
4F07: 28 24           JR      Z,$4F2D             ; {}
4F09: F0 E7           LD      A,($E7)             
4F0B: E6 0F           AND     $0F                 
4F0D: 20 01           JR      NZ,$4F10            ; {}
4F0F: 35              DEC     (HL)                
4F10: 7E              LD      A,(HL)              
4F11: FE 04           CP      $04                 
4F13: 30 17           JR      NC,$4F2C            ; {}
4F15: CD D5 3B        CALL    $3BD5               
4F18: 30 1B           JR      NC,$4F35            ; {}
4F1A: 3E 08           LD      A,$08               
4F1C: EA 3E C1        LD      ($C13E),A           
4F1F: 3E 10           LD      A,$10               
4F21: CD 30 3C        CALL    $3C30               
4F24: F0 D7           LD      A,($D7)             
4F26: E0 9B           LD      ($FF00+$9B),A       
4F28: F0 D8           LD      A,($D8)             
4F2A: E0 9A           LD      ($FF00+$9A),A       
4F2C: C9              RET                         
4F2D: CD D5 3B        CALL    $3BD5               
4F30: 30 03           JR      NC,$4F35            ; {}
4F32: CD 4E 64        CALL    $644E               ; {}
4F35: C9              RET                         
4F36: F0 F0           LD      A,($F0)             
4F38: A7              AND     A                   
4F39: C2 D5 4E        JP      NZ,$4ED5            ; {}
4F3C: 21 10 C2        LD      HL,$C210            
4F3F: 09              ADD     HL,BC               
4F40: 7E              LD      A,(HL)              
4F41: C6 08           ADD     $08                 
4F43: 77              LD      (HL),A              
4F44: 21 10 C3        LD      HL,$C310            
4F47: 09              ADD     HL,BC               
4F48: 36 10           LD      (HL),$10            
4F4A: C3 8D 3B        JP      $3B8D               
4F4D: 44              LD      B,H                 
4F4E: 00              NOP                         
4F4F: 44              LD      B,H                 
4F50: 20 46           JR      NZ,$4F98            ; {}
4F52: 00              NOP                         
4F53: 46              LD      B,(HL)              
4F54: 20 64           JR      NZ,$4FBA            ; {}
4F56: 00              NOP                         
4F57: 64              LD      H,H                 
4F58: 20 66           JR      NZ,$4FC0            ; {}
4F5A: 00              NOP                         
4F5B: 66              LD      H,(HL)              
4F5C: 20 11           JR      NZ,$4F6F            ; {}
4F5E: 4D              LD      C,L                 
4F5F: 4F              LD      C,A                 
4F60: F0 F7           LD      A,($F7)             
4F62: FE 0A           CP      $0A                 
4F64: 20 03           JR      NZ,$4F69            ; {}
4F66: 11 55 4F        LD      DE,$4F55            
4F69: CD 3B 3C        CALL    $3C3B               
4F6C: CD DF 64        CALL    $64DF               ; {}
4F6F: CD 01 65        CALL    $6501               ; {}
4F72: CD B4 3B        CALL    $3BB4               
4F75: CD 4B 65        CALL    $654B               ; {}
4F78: CD 9E 3B        CALL    $3B9E               
4F7B: F0 E7           LD      A,($E7)             
4F7D: 1F              RRA                         
4F7E: 1F              RRA                         
4F7F: 1F              RRA                         
4F80: E6 01           AND     $01                 
4F82: CD 87 3B        CALL    $3B87               
4F85: F0 E7           LD      A,($E7)             
4F87: A9              XOR     C                   
4F88: E6 03           AND     $03                 
4F8A: 20 44           JR      NZ,$4FD0            ; {}
4F8C: CD ED 27        CALL    $27ED               
4F8F: A9              XOR     C                   
4F90: E6 07           AND     $07                 
4F92: C6 04           ADD     $04                 
4F94: CD 30 3C        CALL    $3C30               
4F97: F0 D7           LD      A,($D7)             
4F99: 21 50 C2        LD      HL,$C250            
4F9C: CD C4 4F        CALL    $4FC4               ; {}
4F9F: 21 A0 C2        LD      HL,$C2A0            
4FA2: 09              ADD     HL,BC               
4FA3: 7E              LD      A,(HL)              
4FA4: E6 0C           AND     $0C                 
4FA6: 28 05           JR      Z,$4FAD             ; {}
4FA8: 21 50 C2        LD      HL,$C250            
4FAB: 09              ADD     HL,BC               
4FAC: 70              LD      (HL),B              
4FAD: F0 D8           LD      A,($D8)             
4FAF: 21 40 C2        LD      HL,$C240            
4FB2: CD C4 4F        CALL    $4FC4               ; {}
4FB5: 21 A0 C2        LD      HL,$C2A0            
4FB8: 09              ADD     HL,BC               
4FB9: 7E              LD      A,(HL)              
4FBA: E6 03           AND     $03                 
4FBC: 28 05           JR      Z,$4FC3             ; {}
4FBE: 21 40 C2        LD      HL,$C240            
4FC1: 09              ADD     HL,BC               
4FC2: 70              LD      (HL),B              
4FC3: C9              RET                         
4FC4: 09              ADD     HL,BC               
4FC5: 96              SUB     (HL)                
4FC6: 28 08           JR      Z,$4FD0             ; {}
4FC8: CB 7F           BIT     1,E                 
4FCA: 28 03           JR      Z,$4FCF             ; {}
4FCC: 35              DEC     (HL)                
4FCD: 18 01           JR      $4FD0               ; {}
4FCF: 34              INC     (HL)                
4FD0: C9              RET                         
4FD1: FF              RST     0X38                
4FD2: 00              NOP                         
4FD3: FF              RST     0X38                
4FD4: 20 3A           JR      NZ,$5010            ; {}
4FD6: 00              NOP                         
4FD7: 3A              LD      A,(HLD)             
4FD8: 20 3C           JR      NZ,$5016            ; {}
4FDA: 00              NOP                         
4FDB: 3C              INC     A                   
4FDC: 20 3C           JR      NZ,$501A            ; {}
4FDE: 00              NOP                         
4FDF: 3C              INC     A                   
4FE0: 20 58           JR      NZ,$503A            ; {}
4FE2: 78              LD      A,B                 
4FE3: 78              LD      A,B                 
4FE4: 28 28           JR      Z,$500E             ; {}
4FE6: 28 78           JR      Z,$5060             ; {}
4FE8: 58              LD      E,B                 
4FE9: 28 78           JR      Z,$5063             ; {}
4FEB: 28 78           JR      Z,$5065             ; {}
4FED: 28 78           JR      Z,$5067             ; {}
4FEF: 58              LD      E,B                 
4FF0: 58              LD      E,B                 
4FF1: 28 78           JR      Z,$506B             ; {}
4FF3: 28 78           JR      Z,$506D             ; {}
4FF5: 40              LD      B,B                 
4FF6: 30 50           JR      NC,$5048            ; {}
4FF8: 50              LD      D,B                 
4FF9: 30 30           JR      NC,$502B            ; {}
4FFB: 50              LD      D,B                 
4FFC: 40              LD      B,B                 
4FFD: 50              LD      D,B                 
4FFE: 30 50           JR      NC,$5050            ; {}
5000: 50              LD      D,B                 
5001: 30 30           JR      NC,$5033            ; {}
5003: 40              LD      B,B                 
5004: 40              LD      B,B                 
5005: 50              LD      D,B                 
5006: 30 30           JR      NC,$5038            ; {}
5008: 50              LD      D,B                 
5009: F2                              
500A: 00              NOP                         
500B: 3A              LD      A,(HLD)             
500C: 00              NOP                         
500D: F2                              
500E: 08 3A 20        LD      ($203A),SP          
5011: 0E 00           LD      C,$00               
5013: 3A              LD      A,(HLD)             
5014: 00              NOP                         
5015: 0E 08           LD      C,$08               
5017: 3A              LD      A,(HLD)             
5018: 20 F6           JR      NZ,$5010            ; {}
501A: 0A              LD      A,(BC)              
501B: 3A              LD      A,(HLD)             
501C: 00              NOP                         
501D: F6 12           OR      $12                 
501F: 3A              LD      A,(HLD)             
5020: 20 0A           JR      NZ,$502C            ; {}
5022: F6 3A           OR      $3A                 
5024: 00              NOP                         
5025: 0A              LD      A,(BC)              
5026: FE 3A           CP      $3A                 
5028: 20 00           JR      NZ,$502A            ; {}
502A: 0E 3A           LD      C,$3A               
502C: 00              NOP                         
502D: 00              NOP                         
502E: 16 3A           LD      D,$3A               
5030: 20 00           JR      NZ,$5032            ; {}
5032: F2                              
5033: 3A              LD      A,(HLD)             
5034: 00              NOP                         
5035: 00              NOP                         
5036: FA 3A 20        LD      A,($203A)           
5039: 0A              LD      A,(BC)              
503A: 0A              LD      A,(BC)              
503B: 3A              LD      A,(HLD)             
503C: 00              NOP                         
503D: 0A              LD      A,(BC)              
503E: 12              LD      (DE),A              
503F: 3A              LD      A,(HLD)             
5040: 20 F6           JR      NZ,$5038            ; {}
5042: F6 3A           OR      $3A                 
5044: 00              NOP                         
5045: F6 FE           OR      $FE                 
5047: 3A              LD      A,(HLD)             
5048: 20 F0           JR      NZ,$503A            ; {}
504A: F0 A7           LD      A,($A7)             
504C: 28 1B           JR      Z,$5069             ; {}
504E: CD 91 08        CALL    $0891               
5051: CA E5 65        JP      Z,$65E5             ; {}
5054: 17              RLA                         
5055: 17              RLA                         
5056: E6 30           AND     $30                 
5058: 5F              LD      E,A                 
5059: 50              LD      D,B                 
505A: 21 09 50        LD      HL,$5009            
505D: 19              ADD     HL,DE               
505E: 0E 04           LD      C,$04               
5060: CD 26 3D        CALL    $3D26               
5063: 3E 02           LD      A,$02               
5065: CD D0 3D        CALL    $3DD0               
5068: C9              RET                         
5069: CD DF 64        CALL    $64DF               ; {}
506C: F0 EB           LD      A,($EB)             
506E: FE 8A           CP      $8A                 
5070: 20 0F           JR      NZ,$5081            ; {}
5072: F0 E7           LD      A,($E7)             
5074: 1F              RRA                         
5075: 1F              RRA                         
5076: E6 03           AND     $03                 
5078: CD 87 3B        CALL    $3B87               
507B: 11 D1 4F        LD      DE,$4FD1            
507E: CD 3B 3C        CALL    $3C3B               
5081: 21 D0 C3        LD      HL,$C3D0            
5084: 09              ADD     HL,BC               
5085: F0 B9           LD      A,($B9)             
5087: 5F              LD      E,A                 
5088: CB 27           SLA     1,E                 
508A: CB 27           SLA     1,E                 
508C: 83              ADD     A,E                 
508D: 86              ADD     A,(HL)              
508E: 5F              LD      E,A                 
508F: 50              LD      D,B                 
5090: 21 E1 4F        LD      HL,$4FE1            
5093: 19              ADD     HL,DE               
5094: 7E              LD      A,(HL)              
5095: 21 00 C2        LD      HL,$C200            
5098: 09              ADD     HL,BC               
5099: 77              LD      (HL),A              
509A: 21 F5 4F        LD      HL,$4FF5            
509D: 19              ADD     HL,DE               
509E: 7E              LD      A,(HL)              
509F: 21 10 C2        LD      HL,$C210            
50A2: 09              ADD     HL,BC               
50A3: 77              LD      (HL),A              
50A4: CD BA 3D        CALL    $3DBA               
50A7: 21 B0 C2        LD      HL,$C2B0            
50AA: 09              ADD     HL,BC               
50AB: F0 B8           LD      A,($B8)             
50AD: BE              CP      (HL)                
50AE: 28 47           JR      Z,$50F7             ; {}
50B0: FE 8D           CP      $8D                 
50B2: 20 43           JR      NZ,$50F7            ; {}
50B4: CD D5 3B        CALL    $3BD5               
50B7: 30 39           JR      NC,$50F2            ; {}
50B9: 21 D0 C3        LD      HL,$C3D0            
50BC: 09              ADD     HL,BC               
50BD: 7E              LD      A,(HL)              
50BE: FE 04           CP      $04                 
50C0: 20 08           JR      NZ,$50CA            ; {}
50C2: CD E5 65        CALL    $65E5               ; {}
50C5: CD EC 08        CALL    $08EC               
50C8: 18 2D           JR      $50F7               ; {}
50CA: 34              INC     (HL)                
50CB: 3E 13           LD      A,$13               
50CD: E0 F2           LD      ($FF00+$F2),A       
50CF: 3E 8A           LD      A,$8A               
50D1: CD 01 3C        CALL    $3C01               
50D4: 38 1A           JR      C,$50F0             ; {}
50D6: F0 D7           LD      A,($D7)             
50D8: 21 00 C2        LD      HL,$C200            
50DB: 19              ADD     HL,DE               
50DC: 77              LD      (HL),A              
50DD: F0 D8           LD      A,($D8)             
50DF: 21 10 C2        LD      HL,$C210            
50E2: 19              ADD     HL,DE               
50E3: 77              LD      (HL),A              
50E4: C5              PUSH    BC                  
50E5: D5              PUSH    DE                  
50E6: C1              POP     BC                  
50E7: CD 8D 3B        CALL    $3B8D               
50EA: CD 91 08        CALL    $0891               
50ED: 36 18           LD      (HL),$18            
50EF: C1              POP     BC                  
50F0: 18 05           JR      $50F7               ; {}
50F2: 21 D0 C3        LD      HL,$C3D0            
50F5: 09              ADD     HL,BC               
50F6: 70              LD      (HL),B              
50F7: F0 B8           LD      A,($B8)             
50F9: 21 B0 C2        LD      HL,$C2B0            
50FC: 09              ADD     HL,BC               
50FD: 77              LD      (HL),A              
50FE: C9              RET                         
50FF: 08 F8 00        LD      ($00F8),SP          
5102: 00              NOP                         
5103: 00              NOP                         
5104: 00              NOP                         
5105: F8 08           LD      HL,SP+$08           
5107: CD 8C 53        CALL    $538C               ; {}
510A: AF              XOR     A                   
510B: EA 67 C1        LD      ($C167),A           
510E: F0 EA           LD      A,($EA)             
5110: FE 05           CP      $05                 
5112: C2 CB 53        JP      NZ,$53CB            ; {}
5115: CD DF 64        CALL    $64DF               ; {}
5118: CD 12 3F        CALL    $3F12               
511B: CD 01 65        CALL    $6501               ; {}
511E: CD 8C 08        CALL    $088C               
5121: 28 03           JR      Z,$5126             ; {}
5123: CD 01 53        CALL    $5301               ; {}
5126: F0 F0           LD      A,($F0)             
5128: FE 04           CP      $04                 
512A: 30 14           JR      NC,$5140            ; {}
512C: 21 20 C4        LD      HL,$C420            
512F: 09              ADD     HL,BC               
5130: 7E              LD      A,(HL)              
5131: FE 03           CP      $03                 
5133: 20 0B           JR      NZ,$5140            ; {}
5135: CD 8D 3B        CALL    $3B8D               
5138: 36 05           LD      (HL),$05            
513A: CD 91 08        CALL    $0891               
513D: 36 20           LD      (HL),$20            
513F: C9              RET                         
5140: F0 F0           LD      A,($F0)             
5142: C7              RST     0X00                
5143: C4 51 4F        CALL    NZ,$4F51            ; {}
5146: 51              LD      D,C                 
5147: F9              LD      SP,HL               
5148: 51              LD      D,C                 
5149: 1C              INC     E                   
514A: 52              LD      D,D                 
514B: 8C              ADC     A,H                 
514C: 52              LD      D,D                 
514D: 0D              DEC     C                   
514E: 53              LD      D,E                 
514F: CD B4 3B        CALL    $3BB4               
5152: CD 91 08        CALL    $0891               
5155: 28 13           JR      Z,$516A             ; {}
5157: FE 0A           CP      $0A                 
5159: 20 0B           JR      NZ,$5166            ; {}
515B: CD BE 65        CALL    $65BE               ; {}
515E: 21 80 C3        LD      HL,$C380            
5161: 09              ADD     HL,BC               
5162: 7B              LD      A,E                 
5163: BE              CP      (HL)                
5164: 20 00           JR      NZ,$5166            ; {}
5166: CD 9E 3B        CALL    $3B9E               
5169: C9              RET                         
516A: 21 D0 C2        LD      HL,$C2D0            
516D: 09              ADD     HL,BC               
516E: 34              INC     (HL)                
516F: 7E              LD      A,(HL)              
5170: FE 02           CP      $02                 
5172: 20 13           JR      NZ,$5187            ; {}
5174: 70              LD      (HL),B              
5175: CD ED 27        CALL    $27ED               
5178: E6 01           AND     $01                 
517A: 20 0B           JR      NZ,$5187            ; {}
517C: CD 8D 3B        CALL    $3B8D               
517F: 36 02           LD      (HL),$02            
5181: CD 91 08        CALL    $0891               
5184: 36 30           LD      (HL),$30            
5186: C9              RET                         
5187: CD 91 08        CALL    $0891               
518A: CD ED 27        CALL    $27ED               
518D: E6 1F           AND     $1F                 
518F: F6 20           OR      $20                 
5191: 77              LD      (HL),A              
5192: CD 8D 3B        CALL    $3B8D               
5195: 70              LD      (HL),B              
5196: 21 B0 C2        LD      HL,$C2B0            
5199: 09              ADD     HL,BC               
519A: 7E              LD      A,(HL)              
519B: 3C              INC     A                   
519C: E6 03           AND     $03                 
519E: 77              LD      (HL),A              
519F: FE 00           CP      $00                 
51A1: 20 05           JR      NZ,$51A8            ; {}
51A3: CD BE 65        CALL    $65BE               ; {}
51A6: 18 03           JR      $51AB               ; {}
51A8: CD ED 27        CALL    $27ED               
51AB: E6 03           AND     $03                 
51AD: 5F              LD      E,A                 
51AE: 50              LD      D,B                 
51AF: 21 FF 50        LD      HL,$50FF            
51B2: 19              ADD     HL,DE               
51B3: 7E              LD      A,(HL)              
51B4: 21 40 C2        LD      HL,$C240            
51B7: 09              ADD     HL,BC               
51B8: 77              LD      (HL),A              
51B9: 21 03 51        LD      HL,$5103            
51BC: 19              ADD     HL,DE               
51BD: 7E              LD      A,(HL)              
51BE: 21 50 C2        LD      HL,$C250            
51C1: 09              ADD     HL,BC               
51C2: 77              LD      (HL),A              
51C3: C9              RET                         
51C4: CD B4 3B        CALL    $3BB4               
51C7: 21 A0 C2        LD      HL,$C2A0            
51CA: 09              ADD     HL,BC               
51CB: 7E              LD      A,(HL)              
51CC: E6 0F           AND     $0F                 
51CE: 20 05           JR      NZ,$51D5            ; {}
51D0: CD 91 08        CALL    $0891               
51D3: 20 0E           JR      NZ,$51E3            ; {}
51D5: CD ED 27        CALL    $27ED               
51D8: E6 0F           AND     $0F                 
51DA: F6 10           OR      $10                 
51DC: 77              LD      (HL),A              
51DD: CD 8D 3B        CALL    $3B8D               
51E0: CD AF 3D        CALL    $3DAF               
51E3: CD 4B 65        CALL    $654B               ; {}
51E6: CD 9E 3B        CALL    $3B9E               
51E9: 21 D0 C3        LD      HL,$C3D0            
51EC: 09              ADD     HL,BC               
51ED: 34              INC     (HL)                
51EE: 7E              LD      A,(HL)              
51EF: 1F              RRA                         
51F0: 1F              RRA                         
51F1: 1F              RRA                         
51F2: 1F              RRA                         
51F3: E6 01           AND     $01                 
51F5: CD 87 3B        CALL    $3B87               
51F8: C9              RET                         
51F9: CD B4 3B        CALL    $3BB4               
51FC: CD 91 08        CALL    $0891               
51FF: 20 0A           JR      NZ,$520B            ; {}
5201: 36 20           LD      (HL),$20            
5203: CD 8D 3B        CALL    $3B8D               
5206: 3E 18           LD      A,$18               
5208: CD 25 3C        CALL    $3C25               
520B: CD E9 51        CALL    $51E9               ; {}
520E: CD E9 51        CALL    $51E9               ; {}
5211: F0 E7           LD      A,($E7)             
5213: E6 0F           AND     $0F                 
5215: 20 04           JR      NZ,$521B            ; {}
5217: 3E 20           LD      A,$20               
5219: E0 F2           LD      ($FF00+$F2),A       
521B: C9              RET                         
521C: CD B4 3B        CALL    $3BB4               
521F: CD 91 08        CALL    $0891               
5222: 20 04           JR      NZ,$5228            ; {}
5224: CD 8D 3B        CALL    $3B8D               
5227: 70              LD      (HL),B              
5228: CD 4B 65        CALL    $654B               ; {}
522B: CD 9E 3B        CALL    $3B9E               
522E: CD 9E 65        CALL    $659E               ; {}
5231: C6 18           ADD     $18                 
5233: FE 30           CP      $30                 
5235: 30 1C           JR      NC,$5253            ; {}
5237: CD AE 65        CALL    $65AE               ; {}
523A: C6 18           ADD     $18                 
523C: FE 30           CP      $30                 
523E: 30 13           JR      NC,$5253            ; {}
5240: FA 1C C1        LD      A,($C11C)           
5243: FE 00           CP      $00                 
5245: 20 0C           JR      NZ,$5253            ; {}
5247: CD 8D 3B        CALL    $3B8D               
524A: CD 91 08        CALL    $0891               
524D: 36 4F           LD      (HL),$4F            
524F: 3E 16           LD      A,$16               
5251: E0 F3           LD      ($FF00+$F3),A       
5253: F0 E7           LD      A,($E7)             
5255: E6 07           AND     $07                 
5257: 20 0F           JR      NZ,$5268            ; {}
5259: F0 EE           LD      A,($EE)             
525B: E0 D7           LD      ($FF00+$D7),A       
525D: F0 EC           LD      A,($EC)             
525F: C6 0A           ADD     $0A                 
5261: E0 D8           LD      ($FF00+$D8),A       
5263: 3E 0B           LD      A,$0B               
5265: CD 53 09        CALL    $0953               
5268: 18 A1           JR      $520B               ; {}
526A: 00              NOP                         
526B: 00              NOP                         
526C: 00              NOP                         
526D: 00              NOP                         
526E: 01 01 01        LD      BC,$0101            
5271: 01 00 00        LD      BC,$0000            
5274: EF              RST     0X28                
5275: EF              RST     0X28                
5276: EF              RST     0X28                
5277: EF              RST     0X28                
5278: EF              RST     0X28                
5279: EF              RST     0X28                
527A: EF              RST     0X28                
527B: EF              RST     0X28                
527C: F3              DI                          
527D: F7              RST     0X30                
527E: FB              EI                          
527F: 00              NOP                         
5280: 15              DEC     D                   
5281: 15              DEC     D                   
5282: 15              DEC     D                   
5283: 15              DEC     D                   
5284: 15              DEC     D                   
5285: 14              INC     D                   
5286: 14              INC     D                   
5287: 14              INC     D                   
5288: 10 08           ;;STOP    $08                 
528A: 04              INC     B                   
528B: 00              NOP                         
528C: CD 91 08        CALL    $0891               
528F: 20 05           JR      NZ,$5296            ; {}
5291: CD 8D 3B        CALL    $3B8D               
5294: 70              LD      (HL),B              
5295: C9              RET                         
5296: FE 20           CP      $20                 
5298: 20 30           JR      NZ,$52CA            ; {}
529A: 3E 20           LD      A,$20               
529C: E0 9B           LD      ($FF00+$9B),A       
529E: F0 98           LD      A,($98)             
52A0: FE 50           CP      $50                 
52A2: 3E E0           LD      A,$E0               
52A4: 30 02           JR      NC,$52A8            ; {}
52A6: 3E 20           LD      A,$20               
52A8: E0 9A           LD      ($FF00+$9A),A       
52AA: 3E 10           LD      A,$10               
52AC: E0 A3           LD      ($FF00+$A3),A       
52AE: 3E 02           LD      A,$02               
52B0: EA 46 C1        LD      ($C146),A           
52B3: 3E 08           LD      A,$08               
52B5: E0 F2           LD      ($FF00+$F2),A       
52B7: 3E 08           LD      A,$08               
52B9: EA 94 DB        LD      ($DB94),A           
52BC: F0 EE           LD      A,($EE)             
52BE: E0 98           LD      ($FF00+$98),A       
52C0: F0 EF           LD      A,($EF)             
52C2: E0 99           LD      ($FF00+$99),A       
52C4: CD 8C 08        CALL    $088C               
52C7: 36 50           LD      (HL),$50            
52C9: C9              RET                         
52CA: 1F              RRA                         
52CB: 1F              RRA                         
52CC: 1F              RRA                         
52CD: E6 0F           AND     $0F                 
52CF: 5F              LD      E,A                 
52D0: 50              LD      D,B                 
52D1: 21 6A 52        LD      HL,$526A            
52D4: 19              ADD     HL,DE               
52D5: 7E              LD      A,(HL)              
52D6: CD 87 3B        CALL    $3B87               
52D9: CD 91 08        CALL    $0891               
52DC: FE 20           CP      $20                 
52DE: 38 2C           JR      C,$530C             ; {}
52E0: D6 20           SUB     $20                 
52E2: 1F              RRA                         
52E3: 1F              RRA                         
52E4: E6 0F           AND     $0F                 
52E6: 5F              LD      E,A                 
52E7: 50              LD      D,B                 
52E8: 21 74 52        LD      HL,$5274            
52EB: 19              ADD     HL,DE               
52EC: F0 EE           LD      A,($EE)             
52EE: 86              ADD     A,(HL)              
52EF: E0 98           LD      ($FF00+$98),A       
52F1: 21 80 52        LD      HL,$5280            
52F4: 19              ADD     HL,DE               
52F5: 7E              LD      A,(HL)              
52F6: E0 A2           LD      ($FF00+$A2),A       
52F8: 3E 02           LD      A,$02               
52FA: EA 46 C1        LD      ($C146),A           
52FD: F0 EF           LD      A,($EF)             
52FF: E0 99           LD      ($FF00+$99),A       
5301: 3E 01           LD      A,$01               
5303: E0 A1           LD      ($FF00+$A1),A       
5305: 3E 6A           LD      A,$6A               
5307: E0 9D           LD      ($FF00+$9D),A       
5309: EA 67 C1        LD      ($C167),A           
530C: C9              RET                         
530D: CD B4 3B        CALL    $3BB4               
5310: CD 91 08        CALL    $0891               
5313: 20 05           JR      NZ,$531A            ; {}
5315: CD 8D 3B        CALL    $3B8D               
5318: 70              LD      (HL),B              
5319: C9              RET                         
531A: 1E 00           LD      E,$00               
531C: FE 10           CP      $10                 
531E: 38 01           JR      C,$5321             ; {}
5320: 1C              INC     E                   
5321: FE 10           CP      $10                 
5323: 20 22           JR      NZ,$5347            ; {}
5325: 3E 02           LD      A,$02               
5327: CD 01 3C        CALL    $3C01               
532A: 38 1B           JR      C,$5347             ; {}
532C: F0 D7           LD      A,($D7)             
532E: D6 0C           SUB     $0C                 
5330: 21 00 C2        LD      HL,$C200            
5333: 19              ADD     HL,DE               
5334: 77              LD      (HL),A              
5335: F0 D8           LD      A,($D8)             
5337: D6 00           SUB     $00                 
5339: 21 10 C2        LD      HL,$C210            
533C: 19              ADD     HL,DE               
533D: 77              LD      (HL),A              
533E: 21 10 C3        LD      HL,$C310            
5341: 19              ADD     HL,DE               
5342: 36 10           LD      (HL),$10            
5344: C3 02 42        JP      $4202               ; {}
5347: 7B              LD      A,E                 
5348: CD 87 3B        CALL    $3B87               
534B: C9              RET                         
534C: F4                              
534D: F8 60           LD      HL,SP+$60           
534F: 00              NOP                         
5350: F4                              
5351: 00              NOP                         
5352: 62              LD      H,D                 
5353: 00              NOP                         
5354: F4                              
5355: 08 64 00        LD      ($0064),SP          
5358: F4                              
5359: 10 66           ;;STOP    $66                 
535B: 00              NOP                         
535C: 04              INC     B                   
535D: F8 68           LD      HL,SP+$68           
535F: 00              NOP                         
5360: 04              INC     B                   
5361: 00              NOP                         
5362: 6A              LD      L,D                 
5363: 00              NOP                         
5364: 04              INC     B                   
5365: 08 6C 00        LD      ($006C),SP          
5368: 04              INC     B                   
5369: 10 6E           ;;STOP    $6E                 
536B: 00              NOP                         
536C: F4                              
536D: F8 66           LD      HL,SP+$66           
536F: 20 F4           JR      NZ,$5365            ; {}
5371: 00              NOP                         
5372: 64              LD      H,H                 
5373: 20 F4           JR      NZ,$5369            ; {}
5375: 08 62 20        LD      ($2062),SP          
5378: F4                              
5379: 10 60           ;;STOP    $60                 
537B: 20 04           JR      NZ,$5381            ; {}
537D: F8 6E           LD      HL,SP+$6E           
537F: 20 04           JR      NZ,$5385            ; {}
5381: 00              NOP                         
5382: 6C              LD      L,H                 
5383: 20 04           JR      NZ,$5389            ; {}
5385: 08 6A 20        LD      ($206A),SP          
5388: 04              INC     B                   
5389: 10 68           ;;STOP    $68                 
538B: 20 F0           JR      NZ,$537D            ; {}
538D: F1              POP     AF                  
538E: 17              RLA                         
538F: 17              RLA                         
5390: 17              RLA                         
5391: 17              RLA                         
5392: 17              RLA                         
5393: E6 E0           AND     $E0                 
5395: 5F              LD      E,A                 
5396: 50              LD      D,B                 
5397: 21 4C 53        LD      HL,$534C            
539A: 19              ADD     HL,DE               
539B: 0E 08           LD      C,$08               
539D: CD 26 3D        CALL    $3D26               
53A0: C9              RET                         
53A1: 21 60 C4        LD      HL,$C460            
53A4: 09              ADD     HL,BC               
53A5: 36 FF           LD      (HL),$FF            
53A7: 21 E0 C4        LD      HL,$C4E0            
53AA: 09              ADD     HL,BC               
53AB: 36 30           LD      (HL),$30            
53AD: 21 60 C3        LD      HL,$C360            
53B0: 09              ADD     HL,BC               
53B1: 7E              LD      A,(HL)              
53B2: FE 08           CP      $08                 
53B4: 30 0C           JR      NC,$53C2            ; {}
53B6: 1E 02           LD      E,$02               
53B8: FE 04           CP      $04                 
53BA: 30 02           JR      NC,$53BE            ; {}
53BC: 1E 03           LD      E,$03               
53BE: 7B              LD      A,E                 
53BF: CD 87 3B        CALL    $3B87               
53C2: CD 80 56        CALL    $5680               ; {}
53C5: F0 EA           LD      A,($EA)             
53C7: FE 05           CP      $05                 
53C9: 28 5D           JR      Z,$5428             ; {}
53CB: 21 C0 C2        LD      HL,$C2C0            
53CE: 09              ADD     HL,BC               
53CF: 7E              LD      A,(HL)              
53D0: C7              RST     0X00                
53D1: D9              RETI                        
53D2: 53              LD      D,E                 
53D3: E8 53           ADD     SP,$53              
53D5: F9              LD      SP,HL               
53D6: 53              LD      D,E                 
53D7: 27              DAA                         
53D8: 54              LD      D,H                 
53D9: CD 91 08        CALL    $0891               
53DC: 36 A0           LD      (HL),$A0            
53DE: 21 20 C4        LD      HL,$C420            
53E1: 09              ADD     HL,BC               
53E2: 36 FF           LD      (HL),$FF            
53E4: CD 01 57        CALL    $5701               ; {}
53E7: C9              RET                         
53E8: CD 91 08        CALL    $0891               
53EB: 20 0B           JR      NZ,$53F8            ; {}
53ED: 36 C0           LD      (HL),$C0            
53EF: 21 20 C4        LD      HL,$C420            
53F2: 09              ADD     HL,BC               
53F3: 36 FF           LD      (HL),$FF            
53F5: CD 01 57        CALL    $5701               ; {}
53F8: C9              RET                         
53F9: CD 91 08        CALL    $0891               
53FC: 20 25           JR      NZ,$5423            ; {}
53FE: 3E 1A           LD      A,$1A               
5400: E0 F4           LD      ($FF00+$F4),A       
5402: CD BD 27        CALL    $27BD               
5405: CD 7A 3F        CALL    $3F7A               
5408: F0 EB           LD      A,($EB)             
540A: FE 88           CP      $88                 
540C: C8              RET     Z                   
540D: F0 EB           LD      A,($EB)             
540F: FE 89           CP      $89                 
5411: 28 08           JR      Z,$541B             ; {}
5413: FE 8E           CP      $8E                 
5415: 28 04           JR      Z,$541B             ; {}
5417: FE 92           CP      $92                 
5419: 20 05           JR      NZ,$5420            ; {}
541B: F0 F7           LD      A,($F7)             
541D: FE 06           CP      $06                 
541F: D0              RET     NC                  
5420: C3 B4 6C        JP      $6CB4               ; {}
5423: CD FC 6F        CALL    $6FFC               ; {}
5426: C9              RET                         
5427: C9              RET                         
5428: CD DF 64        CALL    $64DF               ; {}
542B: CD 12 3F        CALL    $3F12               
542E: CD EB 3B        CALL    $3BEB               
5431: CD 49 64        CALL    $6449               ; {}
5434: CD 84 65        CALL    $6584               ; {}
5437: 21 20 C3        LD      HL,$C320            
543A: 09              ADD     HL,BC               
543B: 35              DEC     (HL)                
543C: 35              DEC     (HL)                
543D: 21 10 C3        LD      HL,$C310            
5440: 09              ADD     HL,BC               
5441: 7E              LD      A,(HL)              
5442: E6 80           AND     $80                 
5444: E0 E8           LD      ($FF00+$E8),A       
5446: 28 06           JR      Z,$544E             ; {}
5448: 70              LD      (HL),B              
5449: 21 20 C3        LD      HL,$C320            
544C: 09              ADD     HL,BC               
544D: 70              LD      (HL),B              
544E: CD 8C 08        CALL    $088C               
5451: 28 08           JR      Z,$545B             ; {}
5453: 3E 02           LD      A,$02               
5455: E0 A1           LD      ($FF00+$A1),A       
5457: 3E 6A           LD      A,$6A               
5459: E0 9D           LD      ($FF00+$9D),A       
545B: 21 60 C3        LD      HL,$C360            
545E: 09              ADD     HL,BC               
545F: 7E              LD      A,(HL)              
5460: 21 B0 C2        LD      HL,$C2B0            
5463: 09              ADD     HL,BC               
5464: BE              CP      (HL)                
5465: 77              LD      (HL),A              
5466: CA D8 54        JP      Z,$54D8             ; {}
5469: FE 08           CP      $08                 
546B: 30 6B           JR      NC,$54D8            ; {}
546D: FE 04           CP      $04                 
546F: 30 29           JR      NC,$549A            ; {}
5471: 21 D0 C3        LD      HL,$C3D0            
5474: 09              ADD     HL,BC               
5475: 7E              LD      A,(HL)              
5476: FE 02           CP      $02                 
5478: 30 5E           JR      NC,$54D8            ; {}
547A: 34              INC     (HL)                
547B: 3E 05           LD      A,$05               
547D: CD 01 3C        CALL    $3C01               
5480: 38 56           JR      C,$54D8             ; {}
5482: F0 D7           LD      A,($D7)             
5484: 21 00 C2        LD      HL,$C200            
5487: 19              ADD     HL,DE               
5488: 3D              DEC     A                   
5489: 77              LD      (HL),A              
548A: E0 D7           LD      ($FF00+$D7),A       
548C: F0 D8           LD      A,($D8)             
548E: 21 DA FF        LD      HL,$FFDA            
5491: 96              SUB     (HL)                
5492: 21 10 C2        LD      HL,$C210            
5495: 19              ADD     HL,DE               
5496: D6 10           SUB     $10                 
5498: 18 26           JR      $54C0               ; {}
549A: 21 D0 C3        LD      HL,$C3D0            
549D: 09              ADD     HL,BC               
549E: 7E              LD      A,(HL)              
549F: FE 01           CP      $01                 
54A1: 30 35           JR      NC,$54D8            ; {}
54A3: 34              INC     (HL)                
54A4: 3E 05           LD      A,$05               
54A6: CD 01 3C        CALL    $3C01               
54A9: 38 2D           JR      C,$54D8             ; {}
54AB: F0 D7           LD      A,($D7)             
54AD: 21 00 C2        LD      HL,$C200            
54B0: 19              ADD     HL,DE               
54B1: C6 07           ADD     $07                 
54B3: 77              LD      (HL),A              
54B4: E0 D7           LD      ($FF00+$D7),A       
54B6: F0 D8           LD      A,($D8)             
54B8: 21 DA FF        LD      HL,$FFDA            
54BB: 96              SUB     (HL)                
54BC: 21 10 C2        LD      HL,$C210            
54BF: 19              ADD     HL,DE               
54C0: 77              LD      (HL),A              
54C1: E0 D8           LD      ($FF00+$D8),A       
54C3: 21 F0 C2        LD      HL,$C2F0            
54C6: 19              ADD     HL,DE               
54C7: 36 0F           LD      (HL),$0F            
54C9: 21 40 C3        LD      HL,$C340            
54CC: 19              ADD     HL,DE               
54CD: 36 C4           LD      (HL),$C4            
54CF: 3E 02           LD      A,$02               
54D1: CD 53 09        CALL    $0953               
54D4: 3E 29           LD      A,$29               
54D6: E0 F4           LD      ($FF00+$F4),A       
54D8: F0 F0           LD      A,($F0)             
54DA: C7              RST     0X00                
54DB: EB                              
54DC: 54              LD      D,H                 
54DD: 09              ADD     HL,BC               
54DE: 55              LD      D,L                 
54DF: 1E 55           LD      E,$55               
54E1: 4F              LD      C,A                 
54E2: 55              LD      D,L                 
54E3: 88              ADC     A,B                 
54E4: 55              LD      D,L                 
54E5: A3              AND     E                   
54E6: 55              LD      D,L                 
54E7: B8              CP      B                   
54E8: 55              LD      D,L                 
54E9: E2              LD      (C),A               
54EA: 55              LD      D,L                 
54EB: CD E2 08        CALL    $08E2               
54EE: CD 9E 65        CALL    $659E               ; {}
54F1: C6 20           ADD     $20                 
54F3: FE 40           CP      $40                 
54F5: 30 11           JR      NC,$5508            ; {}
54F7: CD AE 65        CALL    $65AE               ; {}
54FA: C6 20           ADD     $20                 
54FC: FE 40           CP      $40                 
54FE: 30 08           JR      NC,$5508            ; {}
5500: CD 8D 3B        CALL    $3B8D               
5503: CD 91 08        CALL    $0891               
5506: 36 30           LD      (HL),$30            
5508: C9              RET                         
5509: CD E2 08        CALL    $08E2               
550C: CD 91 08        CALL    $0891               
550F: 20 05           JR      NZ,$5516            ; {}
5511: 36 80           LD      (HL),$80            
5513: CD 8D 3B        CALL    $3B8D               
5516: 1F              RRA                         
5517: 1F              RRA                         
5518: E6 01           AND     $01                 
551A: CD 87 3B        CALL    $3B87               
551D: C9              RET                         
551E: CD E2 08        CALL    $08E2               
5521: CD 91 08        CALL    $0891               
5524: 20 18           JR      NZ,$553E            ; {}
5526: 36 50           LD      (HL),$50            
5528: CD 8D 3B        CALL    $3B8D               
552B: 21 40 C3        LD      HL,$C340            
552E: 09              ADD     HL,BC               
552F: CB BE           RES     1,E                 
5531: 21 50 C3        LD      HL,$C350            
5534: 09              ADD     HL,BC               
5535: CB BE           RES     1,E                 
5537: 21 30 C4        LD      HL,$C430            
553A: 09              ADD     HL,BC               
553B: CB B6           RES     1,E                 
553D: C9              RET                         
553E: 1E 08           LD      E,$08               
5540: E6 04           AND     $04                 
5542: 28 02           JR      Z,$5546             ; {}
5544: 1E F8           LD      E,$F8               
5546: 21 40 C2        LD      HL,$C240            
5549: 09              ADD     HL,BC               
554A: 73              LD      (HL),E              
554B: CD 58 65        CALL    $6558               ; {}
554E: C9              RET                         
554F: CD 01 65        CALL    $6501               ; {}
5552: CD 91 08        CALL    $0891               
5555: 20 0E           JR      NZ,$5565            ; {}
5557: 21 20 C3        LD      HL,$C320            
555A: 09              ADD     HL,BC               
555B: 36 30           LD      (HL),$30            
555D: CD 8D 3B        CALL    $3B8D               
5560: 3E 24           LD      A,$24               
5562: E0 F2           LD      ($FF00+$F2),A       
5564: C9              RET                         
5565: F0 E8           LD      A,($E8)             
5567: A7              AND     A                   
5568: 28 1A           JR      Z,$5584             ; {}
556A: 21 20 C3        LD      HL,$C320            
556D: 09              ADD     HL,BC               
556E: 36 0C           LD      (HL),$0C            
5570: 21 60 C3        LD      HL,$C360            
5573: 09              ADD     HL,BC               
5574: 7E              LD      A,(HL)              
5575: FE 05           CP      $05                 
5577: 3E 08           LD      A,$08               
5579: 30 02           JR      NC,$557D            ; {}
557B: 3E 0C           LD      A,$0C               
557D: CD 25 3C        CALL    $3C25               
5580: 3E 20           LD      A,$20               
5582: E0 F2           LD      ($FF00+$F2),A       
5584: CD 4B 65        CALL    $654B               ; {}
5587: C9              RET                         
5588: CD 01 65        CALL    $6501               ; {}
558B: 21 20 C3        LD      HL,$C320            
558E: 09              ADD     HL,BC               
558F: 7E              LD      A,(HL)              
5590: E6 FE           AND     $FE                 
5592: 20 0B           JR      NZ,$559F            ; {}
5594: CD 91 08        CALL    $0891               
5597: 36 10           LD      (HL),$10            
5599: CD AF 3D        CALL    $3DAF               
559C: CD 8D 3B        CALL    $3B8D               
559F: CD 4B 65        CALL    $654B               ; {}
55A2: C9              RET                         
55A3: CD 01 65        CALL    $6501               ; {}
55A6: CD 91 08        CALL    $0891               
55A9: 3E 00           LD      A,$00               
55AB: 20 05           JR      NZ,$55B2            ; {}
55AD: CD 8D 3B        CALL    $3B8D               
55B0: 3E B0           LD      A,$B0               
55B2: 21 20 C3        LD      HL,$C320            
55B5: 09              ADD     HL,BC               
55B6: 77              LD      (HL),A              
55B7: C9              RET                         
55B8: CD 01 65        CALL    $6501               ; {}
55BB: F0 E8           LD      A,($E8)             
55BD: A7              AND     A                   
55BE: 28 21           JR      Z,$55E1             ; {}
55C0: 3E 30           LD      A,$30               
55C2: EA 57 C1        LD      ($C157),A           
55C5: 3E 04           LD      A,$04               
55C7: EA 58 C1        LD      ($C158),A           
55CA: 3E 0B           LD      A,$0B               
55CC: E0 F2           LD      ($FF00+$F2),A       
55CE: CD 91 08        CALL    $0891               
55D1: 36 30           LD      (HL),$30            
55D3: FA 46 C1        LD      A,($C146)           
55D6: A7              AND     A                   
55D7: 20 05           JR      NZ,$55DE            ; {}
55D9: CD 8C 08        CALL    $088C               
55DC: 36 40           LD      (HL),$40            
55DE: CD 8D 3B        CALL    $3B8D               
55E1: C9              RET                         
55E2: CD 01 65        CALL    $6501               ; {}
55E5: CD 91 08        CALL    $0891               
55E8: 20 05           JR      NZ,$55EF            ; {}
55EA: CD 8D 3B        CALL    $3B8D               
55ED: 36 02           LD      (HL),$02            
55EF: C9              RET                         
55F0: F4                              
55F1: F8 70           LD      HL,SP+$70           
55F3: 00              NOP                         
55F4: F4                              
55F5: 00              NOP                         
55F6: 72              LD      (HL),D              
55F7: 00              NOP                         
55F8: F4                              
55F9: 08 72 20        LD      ($2072),SP          
55FC: F4                              
55FD: 10 70           ;;STOP    $70                 
55FF: 20 04           JR      NZ,$5605            ; {}
5601: F8 74           LD      HL,SP+$74           
5603: 00              NOP                         
5604: 04              INC     B                   
5605: 00              NOP                         
5606: 76              HALT                        
5607: 00              NOP                         
5608: 04              INC     B                   
5609: 08 7A 00        LD      ($007A),SP          
560C: 04              INC     B                   
560D: 10 7A           ;;STOP    $7A                 
560F: 20 F4           JR      NZ,$5605            ; {}
5611: F8 70           LD      HL,SP+$70           
5613: 00              NOP                         
5614: F4                              
5615: 00              NOP                         
5616: 78              LD      A,B                 
5617: 00              NOP                         
5618: F4                              
5619: 08 78 20        LD      ($2078),SP          
561C: F4                              
561D: 10 70           ;;STOP    $70                 
561F: 20 04           JR      NZ,$5625            ; {}
5621: F8 74           LD      HL,SP+$74           
5623: 00              NOP                         
5624: 04              INC     B                   
5625: 00              NOP                         
5626: 76              HALT                        
5627: 00              NOP                         
5628: 04              INC     B                   
5629: 08 7A 00        LD      ($007A),SP          
562C: 04              INC     B                   
562D: 10 7A           ;;STOP    $7A                 
562F: 20 F4           JR      NZ,$5625            ; {}
5631: F8 70           LD      HL,SP+$70           
5633: 00              NOP                         
5634: F4                              
5635: 00              NOP                         
5636: 72              LD      (HL),D              
5637: 00              NOP                         
5638: F4                              
5639: 08 72 20        LD      ($2072),SP          
563C: F4                              
563D: 10 70           ;;STOP    $70                 
563F: 20 04           JR      NZ,$5645            ; {}
5641: F8 74           LD      HL,SP+$74           
5643: 00              NOP                         
5644: 04              INC     B                   
5645: 00              NOP                         
5646: 76              HALT                        
5647: 00              NOP                         
5648: 04              INC     B                   
5649: 08 76 20        LD      ($2076),SP          
564C: 04              INC     B                   
564D: 10 74           ;;STOP    $74                 
564F: 20 F4           JR      NZ,$5645            ; {}
5651: F8 7C           LD      HL,SP+$7C           
5653: 00              NOP                         
5654: F4                              
5655: 00              NOP                         
5656: 7E              LD      A,(HL)              
5657: 00              NOP                         
5658: F4                              
5659: 08 7E 20        LD      ($207E),SP          
565C: F4                              
565D: 10 7C           ;;STOP    $7C                 
565F: 20 04           JR      NZ,$5665            ; {}
5661: F8 74           LD      HL,SP+$74           
5663: 00              NOP                         
5664: 04              INC     B                   
5665: 00              NOP                         
5666: 76              HALT                        
5667: 00              NOP                         
5668: 04              INC     B                   
5669: 08 76 20        LD      ($2076),SP          
566C: 04              INC     B                   
566D: 10 74           ;;STOP    $74                 
566F: 20 0C           JR      NZ,$567D            ; {}
5671: FB              EI                          
5672: 26 00           LD      H,$00               
5674: 0C              INC     C                   
5675: 01 26 00        LD      BC,$0026            
5678: 0C              INC     C                   
5679: 07              RLCA                        
567A: 26 00           LD      H,$00               
567C: 0C              INC     C                   
567D: 0D              DEC     C                   
567E: 26 00           LD      H,$00               
5680: F0 F1           LD      A,($F1)             
5682: 17              RLA                         
5683: 17              RLA                         
5684: 17              RLA                         
5685: 17              RLA                         
5686: 17              RLA                         
5687: E6 E0           AND     $E0                 
5689: 5F              LD      E,A                 
568A: 50              LD      D,B                 
568B: 21 F0 55        LD      HL,$55F0            
568E: 19              ADD     HL,DE               
568F: 0E 08           LD      C,$08               
5691: CD 26 3D        CALL    $3D26               
5694: 3E 04           LD      A,$04               
5696: CD D0 3D        CALL    $3DD0               
5699: 21 10 C3        LD      HL,$C310            
569C: 09              ADD     HL,BC               
569D: 7E              LD      A,(HL)              
569E: A7              AND     A                   
569F: 28 0C           JR      Z,$56AD             ; {}
56A1: F0 EF           LD      A,($EF)             
56A3: E0 EC           LD      ($FF00+$EC),A       
56A5: 21 70 56        LD      HL,$5670            
56A8: 0E 04           LD      C,$04               
56AA: CD 26 3D        CALL    $3D26               
56AD: C3 BA 3D        JP      $3DBA               
56B0: 00              NOP                         
56B1: 04              INC     B                   
56B2: FC                              
56B3: 08 F8 21        LD      ($21F8),SP          
56B6: D0              RET     NC                  
56B7: C2 09 7E        JP      NZ,$7E09            ; {}
56BA: FE 02           CP      $02                 
56BC: CA 5C 5A        JP      Z,$5A5C             ; {}
56BF: FE 00           CP      $00                 
56C1: 20 1B           JR      NZ,$56DE            ; {}
56C3: 34              INC     (HL)                
56C4: 3E 50           LD      A,$50               
56C6: E0 B0           LD      ($FF00+$B0),A       
56C8: 21 10 C3        LD      HL,$C310            
56CB: 09              ADD     HL,BC               
56CC: 36 FF           LD      (HL),$FF            
56CE: CD 91 08        CALL    $0891               
56D1: 36 50           LD      (HL),$50            
56D3: 1E 00           LD      E,$00               
56D5: 3E FF           LD      A,$FF               
56D7: 21 00 D2        LD      HL,$D200            
56DA: 22              LD      (HLI),A             
56DB: 1D              DEC     E                   
56DC: 20 FC           JR      NZ,$56DA            ; {}
56DE: CD 9C 59        CALL    $599C               ; {}
56E1: F0 EA           LD      A,($EA)             
56E3: FE 01           CP      $01                 
56E5: C2 95 57        JP      NZ,$5795            ; {}
56E8: 21 C0 C2        LD      HL,$C2C0            
56EB: 09              ADD     HL,BC               
56EC: 7E              LD      A,(HL)              
56ED: C7              RST     0X00                
56EE: F6 56           OR      $56                 
56F0: 07              RLCA                        
56F1: 57              LD      D,A                 
56F2: 18 57           JR      $574B               ; {}
56F4: 94              SUB     H                   
56F5: 57              LD      D,A                 
56F6: 21 20 C4        LD      HL,$C420            
56F9: 09              ADD     HL,BC               
56FA: 36 FF           LD      (HL),$FF            
56FC: CD 91 08        CALL    $0891               
56FF: 36 60           LD      (HL),$60            
5701: 21 C0 C2        LD      HL,$C2C0            
5704: 09              ADD     HL,BC               
5705: 34              INC     (HL)                
5706: C9              RET                         
5707: CD 91 08        CALL    $0891               
570A: 20 0B           JR      NZ,$5717            ; {}
570C: 36 CF           LD      (HL),$CF            
570E: CD 01 57        CALL    $5701               ; {}
5711: 21 40 C4        LD      HL,$C440            
5714: 09              ADD     HL,BC               
5715: 36 05           LD      (HL),$05            
5717: C9              RET                         
5718: CD 91 08        CALL    $0891               
571B: 20 3A           JR      NZ,$5757            ; {}
571D: CD BD 27        CALL    $27BD               
5720: 3E 30           LD      A,$30               
5722: CD 01 3C        CALL    $3C01               
5725: F0 D7           LD      A,($D7)             
5727: 21 00 C2        LD      HL,$C200            
572A: 19              ADD     HL,DE               
572B: 77              LD      (HL),A              
572C: F0 D8           LD      A,($D8)             
572E: 21 10 C2        LD      HL,$C210            
5731: 19              ADD     HL,DE               
5732: 77              LD      (HL),A              
5733: F0 DA           LD      A,($DA)             
5735: 21 10 C3        LD      HL,$C310            
5738: 19              ADD     HL,DE               
5739: 77              LD      (HL),A              
573A: 21 B0 C3        LD      HL,$C3B0            
573D: 19              ADD     HL,DE               
573E: 36 02           LD      (HL),$02            
5740: 21 20 C3        LD      HL,$C320            
5743: 19              ADD     HL,DE               
5744: 36 10           LD      (HL),$10            
5746: 21 F0 C2        LD      HL,$C2F0            
5749: 19              ADD     HL,DE               
574A: 36 10           LD      (HL),$10            
574C: CD E5 65        CALL    $65E5               ; {}
574F: F0 EE           LD      A,($EE)             
5751: E0 D7           LD      ($FF00+$D7),A       
5753: F0 EC           LD      A,($EC)             
5755: 18 31           JR      $5788               ; {}
5757: E6 1F           AND     $1F                 
5759: 20 38           JR      NZ,$5793            ; {}
575B: 21 D0 C3        LD      HL,$C3D0            
575E: 09              ADD     HL,BC               
575F: 7E              LD      A,(HL)              
5760: 21 40 C4        LD      HL,$C440            
5763: 09              ADD     HL,BC               
5764: 5E              LD      E,(HL)              
5765: 35              DEC     (HL)                
5766: 50              LD      D,B                 
5767: 21 96 59        LD      HL,$5996            
576A: 19              ADD     HL,DE               
576B: 96              SUB     (HL)                
576C: 5F              LD      E,A                 
576D: 50              LD      D,B                 
576E: 21 00 D0        LD      HL,$D000            
5771: 19              ADD     HL,DE               
5772: 7E              LD      A,(HL)              
5773: E0 D7           LD      ($FF00+$D7),A       
5775: 21 00 D2        LD      HL,$D200            
5778: 19              ADD     HL,DE               
5779: 7E              LD      A,(HL)              
577A: E6 80           AND     $80                 
577C: 20 15           JR      NZ,$5793            ; {}
577E: E5              PUSH    HL                  
577F: 21 00 D1        LD      HL,$D100            
5782: 19              ADD     HL,DE               
5783: 7E              LD      A,(HL)              
5784: E1              POP     HL                  
5785: 96              SUB     (HL)                
5786: 36 FF           LD      (HL),$FF            
5788: E0 D8           LD      ($FF00+$D8),A       
578A: 3E 02           LD      A,$02               
578C: CD 53 09        CALL    $0953               
578F: 3E 13           LD      A,$13               
5791: E0 F4           LD      ($FF00+$F4),A       
5793: C9              RET                         
5794: C9              RET                         
5795: CD DF 64        CALL    $64DF               ; {}
5798: CD 12 3F        CALL    $3F12               
579B: CD 8C 08        CALL    $088C               
579E: 28 53           JR      Z,$57F3             ; {}
57A0: E6 0F           AND     $0F                 
57A2: 20 4F           JR      NZ,$57F3            ; {}
57A4: 3E 02           LD      A,$02               
57A6: E0 E8           LD      ($FF00+$E8),A       
57A8: 3E 87           LD      A,$87               
57AA: CD 01 3C        CALL    $3C01               
57AD: 38 44           JR      C,$57F3             ; {}
57AF: C5              PUSH    BC                  
57B0: F0 E8           LD      A,($E8)             
57B2: 4F              LD      C,A                 
57B3: 21 B0 C3        LD      HL,$C3B0            
57B6: 19              ADD     HL,DE               
57B7: E6 02           AND     $02                 
57B9: 77              LD      (HL),A              
57BA: FA CD C1        LD      A,($C1CD)           
57BD: 21 B0 56        LD      HL,$56B0            
57C0: 09              ADD     HL,BC               
57C1: 86              ADD     A,(HL)              
57C2: 21 00 C2        LD      HL,$C200            
57C5: 19              ADD     HL,DE               
57C6: 77              LD      (HL),A              
57C7: 21 B2 56        LD      HL,$56B2            
57CA: 09              ADD     HL,BC               
57CB: 7E              LD      A,(HL)              
57CC: 21 40 C2        LD      HL,$C240            
57CF: 19              ADD     HL,DE               
57D0: 77              LD      (HL),A              
57D1: FA CE C1        LD      A,($C1CE)           
57D4: C6 00           ADD     $00                 
57D6: 21 10 C2        LD      HL,$C210            
57D9: 19              ADD     HL,DE               
57DA: 77              LD      (HL),A              
57DB: 21 50 C2        LD      HL,$C250            
57DE: 19              ADD     HL,DE               
57DF: 36 F0           LD      (HL),$F0            
57E1: 21 D0 C2        LD      HL,$C2D0            
57E4: 19              ADD     HL,DE               
57E5: 36 02           LD      (HL),$02            
57E7: 21 40 C3        LD      HL,$C340            
57EA: 19              ADD     HL,DE               
57EB: 36 C1           LD      (HL),$C1            
57ED: C1              POP     BC                  
57EE: F0 E8           LD      A,($E8)             
57F0: 3D              DEC     A                   
57F1: 20 B3           JR      NZ,$57A6            ; {}
57F3: CD 1F 5A        CALL    $5A1F               ; {}
57F6: CD E2 08        CALL    $08E2               
57F9: F0 F0           LD      A,($F0)             
57FB: FE 02           CP      $02                 
57FD: 38 22           JR      C,$5821             ; {}
57FF: 21 D0 C3        LD      HL,$C3D0            
5802: 09              ADD     HL,BC               
5803: 7E              LD      A,(HL)              
5804: 34              INC     (HL)                
5805: E6 FF           AND     $FF                 
5807: 5F              LD      E,A                 
5808: 50              LD      D,B                 
5809: 21 00 D0        LD      HL,$D000            
580C: 19              ADD     HL,DE               
580D: F0 EE           LD      A,($EE)             
580F: 77              LD      (HL),A              
5810: 21 00 D1        LD      HL,$D100            
5813: 19              ADD     HL,DE               
5814: F0 EF           LD      A,($EF)             
5816: 77              LD      (HL),A              
5817: 21 10 C3        LD      HL,$C310            
581A: 09              ADD     HL,BC               
581B: 7E              LD      A,(HL)              
581C: 21 00 D2        LD      HL,$D200            
581F: 19              ADD     HL,DE               
5820: 77              LD      (HL),A              
5821: F0 F0           LD      A,($F0)             
5823: C7              RST     0X00                
5824: 40              LD      B,B                 
5825: 58              LD      E,B                 
5826: 77              LD      (HL),A              
5827: 58              LD      E,B                 
5828: BD              CP      L                   
5829: 58              LD      E,B                 
582A: DD                              
582B: 58              LD      E,B                 
582C: 07              RLCA                        
582D: 59              LD      E,C                 
582E: 72              LD      (HL),D              
582F: 59              LD      E,C                 
5830: 28 38           JR      Z,$586A             ; {}
5832: 48              LD      C,B                 
5833: 58              LD      E,B                 
5834: 68              LD      L,B                 
5835: 78              LD      A,B                 
5836: 88              ADC     A,B                 
5837: 28 30           JR      Z,$5869             ; {}
5839: 40              LD      B,B                 
583A: 50              LD      D,B                 
583B: 60              LD      H,B                 
583C: 70              LD      (HL),B              
583D: 30 40           JR      NC,$587F            ; {}
583F: 50              LD      D,B                 
5840: CD 91 08        CALL    $0891               
5843: 20 31           JR      NZ,$5876            ; {}
5845: CD 91 08        CALL    $0891               
5848: 36 18           LD      (HL),$18            
584A: CD ED 27        CALL    $27ED               
584D: E6 07           AND     $07                 
584F: 5F              LD      E,A                 
5850: 50              LD      D,B                 
5851: 21 30 58        LD      HL,$5830            
5854: 19              ADD     HL,DE               
5855: 7E              LD      A,(HL)              
5856: 21 00 C2        LD      HL,$C200            
5859: 09              ADD     HL,BC               
585A: 77              LD      (HL),A              
585B: CD ED 27        CALL    $27ED               
585E: E6 07           AND     $07                 
5860: 5F              LD      E,A                 
5861: 21 38 58        LD      HL,$5838            
5864: 19              ADD     HL,DE               
5865: 7E              LD      A,(HL)              
5866: 21 10 C2        LD      HL,$C210            
5869: 09              ADD     HL,BC               
586A: 77              LD      (HL),A              
586B: 21 10 C3        LD      HL,$C310            
586E: 09              ADD     HL,BC               
586F: 70              LD      (HL),B              
5870: CD BA 3D        CALL    $3DBA               
5873: CD 8D 3B        CALL    $3B8D               
5876: C9              RET                         
5877: CD 91 08        CALL    $0891               
587A: 20 33           JR      NZ,$58AF            ; {}
587C: 36 20           LD      (HL),$20            
587E: F0 98           LD      A,($98)             
5880: F5              PUSH    AF                  
5881: F0 99           LD      A,($99)             
5883: F5              PUSH    AF                  
5884: 3E 58           LD      A,$58               
5886: E0 98           LD      ($FF00+$98),A       
5888: 3E 50           LD      A,$50               
588A: E0 99           LD      ($FF00+$99),A       
588C: 3E 08           LD      A,$08               
588E: CD 25 3C        CALL    $3C25               
5891: F1              POP     AF                  
5892: E0 99           LD      ($FF00+$99),A       
5894: F1              POP     AF                  
5895: E0 98           LD      ($FF00+$98),A       
5897: 21 20 C3        LD      HL,$C320            
589A: 09              ADD     HL,BC               
589B: 36 08           LD      (HL),$08            
589D: F0 EE           LD      A,($EE)             
589F: EA CD C1        LD      ($C1CD),A           
58A2: F0 EF           LD      A,($EF)             
58A4: EA CE C1        LD      ($C1CE),A           
58A7: CD 8C 08        CALL    $088C               
58AA: 36 61           LD      (HL),$61            
58AC: CD 8D 3B        CALL    $3B8D               
58AF: F0 E7           LD      A,($E7)             
58B1: 1F              RRA                         
58B2: 1F              RRA                         
58B3: 1F              RRA                         
58B4: 1F              RRA                         
58B5: E6 01           AND     $01                 
58B7: C6 05           ADD     $05                 
58B9: CD 87 3B        CALL    $3B87               
58BC: C9              RET                         
58BD: CD 91 08        CALL    $0891               
58C0: 20 11           JR      NZ,$58D3            ; {}
58C2: CD ED 27        CALL    $27ED               
58C5: E6 1F           AND     $1F                 
58C7: C6 20           ADD     $20                 
58C9: 77              LD      (HL),A              
58CA: 21 B0 C2        LD      HL,$C2B0            
58CD: 09              ADD     HL,BC               
58CE: 36 20           LD      (HL),$20            
58D0: CD 8D 3B        CALL    $3B8D               
58D3: CD 4B 65        CALL    $654B               ; {}
58D6: CD 84 65        CALL    $6584               ; {}
58D9: CD B4 3B        CALL    $3BB4               
58DC: C9              RET                         
58DD: CD 91 08        CALL    $0891               
58E0: 20 05           JR      NZ,$58E7            ; {}
58E2: 36 80           LD      (HL),$80            
58E4: CD 8D 3B        CALL    $3B8D               
58E7: 21 B0 C2        LD      HL,$C2B0            
58EA: 09              ADD     HL,BC               
58EB: 7E              LD      A,(HL)              
58EC: 34              INC     (HL)                
58ED: 7E              LD      A,(HL)              
58EE: CB 47           BIT     1,E                 
58F0: 20 0B           JR      NZ,$58FD            ; {}
58F2: 21 20 C3        LD      HL,$C320            
58F5: 09              ADD     HL,BC               
58F6: E6 20           AND     $20                 
58F8: 20 02           JR      NZ,$58FC            ; {}
58FA: 34              INC     (HL)                
58FB: 34              INC     (HL)                
58FC: 35              DEC     (HL)                
58FD: CD 4B 65        CALL    $654B               ; {}
5900: CD 84 65        CALL    $6584               ; {}
5903: CD B4 3B        CALL    $3BB4               
5906: C9              RET                         
5907: CD 91 08        CALL    $0891               
590A: 20 07           JR      NZ,$5913            ; {}
590C: 36 60           LD      (HL),$60            
590E: CD 8D 3B        CALL    $3B8D               
5911: 70              LD      (HL),B              
5912: C9              RET                         
5913: FE 78           CP      $78                 
5915: 20 13           JR      NZ,$592A            ; {}
5917: F0 EE           LD      A,($EE)             
5919: EA CD C1        LD      ($C1CD),A           
591C: F0 EF           LD      A,($EF)             
591E: EA CE C1        LD      ($C1CE),A           
5921: CD 8C 08        CALL    $088C               
5924: 36 60           LD      (HL),$60            
5926: 3E 23           LD      A,$23               
5928: E0 F4           LD      ($FF00+$F4),A       
592A: 21 20 C3        LD      HL,$C320            
592D: 09              ADD     HL,BC               
592E: 7E              LD      A,(HL)              
592F: D6 F4           SUB     $F4                 
5931: E6 80           AND     $80                 
5933: 20 01           JR      NZ,$5936            ; {}
5935: 35              DEC     (HL)                
5936: F0 E7           LD      A,($E7)             
5938: E6 07           AND     $07                 
593A: 20 1E           JR      NZ,$595A            ; {}
593C: 21 40 C2        LD      HL,$C240            
593F: 09              ADD     HL,BC               
5940: 7E              LD      A,(HL)              
5941: A7              AND     A                   
5942: 28 07           JR      Z,$594B             ; {}
5944: E6 80           AND     $80                 
5946: 28 02           JR      Z,$594A             ; {}
5948: 34              INC     (HL)                
5949: 34              INC     (HL)                
594A: 35              DEC     (HL)                
594B: 21 50 C2        LD      HL,$C250            
594E: 09              ADD     HL,BC               
594F: 7E              LD      A,(HL)              
5950: A7              AND     A                   
5951: 28 07           JR      Z,$595A             ; {}
5953: E6 80           AND     $80                 
5955: 28 02           JR      Z,$5959             ; {}
5957: 34              INC     (HL)                
5958: 34              INC     (HL)                
5959: 35              DEC     (HL)                
595A: CD 4B 65        CALL    $654B               ; {}
595D: CD 84 65        CALL    $6584               ; {}
5960: 21 10 C3        LD      HL,$C310            
5963: 09              ADD     HL,BC               
5964: 7E              LD      A,(HL)              
5965: E6 80           AND     $80                 
5967: 20 03           JR      NZ,$596C            ; {}
5969: CD B4 3B        CALL    $3BB4               
596C: 3E 02           LD      A,$02               
596E: CD 87 3B        CALL    $3B87               
5971: C9              RET                         
5972: 72              LD      (HL),D              
5973: 00              NOP                         
5974: 74              LD      (HL),H              
5975: 00              NOP                         
5976: 74              LD      (HL),H              
5977: 20 72           JR      NZ,$59EB            ; {}
5979: 20 70           JR      NZ,$59EB            ; {}
597B: 00              NOP                         
597C: 70              LD      (HL),B              
597D: 20 70           JR      NZ,$59EF            ; {}
597F: 40              LD      B,B                 
5980: 70              LD      (HL),B              
5981: 60              LD      H,B                 
5982: 76              HALT                        
5983: 00              NOP                         
5984: 76              HALT                        
5985: 20 7A           JR      NZ,$5A01            ; {}
5987: 00              NOP                         
5988: 7A              LD      A,D                 
5989: 60              LD      H,B                 
598A: 7A              LD      A,D                 
598B: 40              LD      B,B                 
598C: 7A              LD      A,D                 
598D: 20 78           JR      NZ,$5A07            ; {}
598F: 00              NOP                         
5990: 78              LD      A,B                 
5991: 60              LD      H,B                 
5992: 78              LD      A,B                 
5993: 40              LD      B,B                 
5994: 78              LD      A,B                 
5995: 20 0C           JR      NZ,$59A3            ; {}
5997: 18 24           JR      $59BD               ; {}
5999: 30 3C           JR      NC,$59D7            ; {}
599B: 48              LD      C,B                 
599C: 21 10 C3        LD      HL,$C310            
599F: 09              ADD     HL,BC               
59A0: 7E              LD      A,(HL)              
59A1: E6 80           AND     $80                 
59A3: 20 06           JR      NZ,$59AB            ; {}
59A5: 11 72 59        LD      DE,$5972            
59A8: CD 3B 3C        CALL    $3C3B               
59AB: 21 D0 C3        LD      HL,$C3D0            
59AE: 09              ADD     HL,BC               
59AF: 7E              LD      A,(HL)              
59B0: E0 D7           LD      ($FF00+$D7),A       
59B2: F0 E7           LD      A,($E7)             
59B4: E6 01           AND     $01                 
59B6: 28 08           JR      Z,$59C0             ; {}
59B8: 3E 06           LD      A,$06               
59BA: E0 E9           LD      ($FF00+$E9),A       
59BC: 3E 00           LD      A,$00               
59BE: 18 06           JR      $59C6               ; {}
59C0: 3E FF           LD      A,$FF               
59C2: E0 E9           LD      ($FF00+$E9),A       
59C4: 3E 05           LD      A,$05               
59C6: E0 E8           LD      ($FF00+$E8),A       
59C8: 5F              LD      E,A                 
59C9: 50              LD      D,B                 
59CA: 21 96 59        LD      HL,$5996            
59CD: 19              ADD     HL,DE               
59CE: F0 D7           LD      A,($D7)             
59D0: 96              SUB     (HL)                
59D1: E6 FF           AND     $FF                 
59D3: 5F              LD      E,A                 
59D4: 16 00           LD      D,$00               
59D6: 21 00 D0        LD      HL,$D000            
59D9: 19              ADD     HL,DE               
59DA: 7E              LD      A,(HL)              
59DB: E0 EE           LD      ($FF00+$EE),A       
59DD: 21 00 D1        LD      HL,$D100            
59E0: 19              ADD     HL,DE               
59E1: 7E              LD      A,(HL)              
59E2: E0 EF           LD      ($FF00+$EF),A       
59E4: 21 00 D2        LD      HL,$D200            
59E7: 19              ADD     HL,DE               
59E8: 96              SUB     (HL)                
59E9: E0 EC           LD      ($FF00+$EC),A       
59EB: 7E              LD      A,(HL)              
59EC: E6 80           AND     $80                 
59EE: 20 19           JR      NZ,$5A09            ; {}
59F0: F0 E8           LD      A,($E8)             
59F2: FE 05           CP      $05                 
59F4: 3E 04           LD      A,$04               
59F6: 20 09           JR      NZ,$5A01            ; {}
59F8: F0 E7           LD      A,($E7)             
59FA: 1F              RRA                         
59FB: 1F              RRA                         
59FC: 1F              RRA                         
59FD: E6 01           AND     $01                 
59FF: C6 07           ADD     $07                 
5A01: E0 F1           LD      ($FF00+$F1),A       
5A03: 11 72 59        LD      DE,$5972            
5A06: CD 3B 3C        CALL    $3C3B               
5A09: 1E FF           LD      E,$FF               
5A0B: F0 E7           LD      A,($E7)             
5A0D: E6 01           AND     $01                 
5A0F: 28 02           JR      Z,$5A13             ; {}
5A11: 1E 01           LD      E,$01               
5A13: 21 E9 FF        LD      HL,$FFE9            
5A16: F0 E8           LD      A,($E8)             
5A18: 83              ADD     A,E                 
5A19: BE              CP      (HL)                
5A1A: 20 AA           JR      NZ,$59C6            ; {}
5A1C: C3 BA 3D        JP      $3DBA               
5A1F: 21 40 C2        LD      HL,$C240            
5A22: 09              ADD     HL,BC               
5A23: 7E              LD      A,(HL)              
5A24: 57              LD      D,A                 
5A25: CB 7F           BIT     1,E                 
5A27: 28 02           JR      Z,$5A2B             ; {}
5A29: 2F              CPL                         
5A2A: 3C              INC     A                   
5A2B: 5F              LD      E,A                 
5A2C: 21 50 C2        LD      HL,$C250            
5A2F: 09              ADD     HL,BC               
5A30: 7E              LD      A,(HL)              
5A31: CB 7F           BIT     1,E                 
5A33: 28 02           JR      Z,$5A37             ; {}
5A35: 2F              CPL                         
5A36: 3C              INC     A                   
5A37: BB              CP      E                   
5A38: 30 0C           JR      NC,$5A46            ; {}
5A3A: CB 7A           BIT     1,E                 
5A3C: 20 04           JR      NZ,$5A42            ; {}
5A3E: 3E 01           LD      A,$01               
5A40: 18 0E           JR      $5A50               ; {}
5A42: 3E 00           LD      A,$00               
5A44: 18 0A           JR      $5A50               ; {}
5A46: CB 7E           BIT     1,E                 
5A48: 20 04           JR      NZ,$5A4E            ; {}
5A4A: 3E 02           LD      A,$02               
5A4C: 18 02           JR      $5A50               ; {}
5A4E: 3E 03           LD      A,$03               
5A50: CD 87 3B        CALL    $3B87               
5A53: C9              RET                         
5A54: 7C              LD      A,H                 
5A55: 20 7E           JR      NZ,$5AD5            ; {}
5A57: 20 7C           JR      NZ,$5AD5            ; {}
5A59: 00              NOP                         
5A5A: 7E              LD      A,(HL)              
5A5B: 00              NOP                         
5A5C: 11 54 5A        LD      DE,$5A54            
5A5F: CD D0 3C        CALL    $3CD0               
5A62: CD DF 64        CALL    $64DF               ; {}
5A65: CD 4B 65        CALL    $654B               ; {}
5A68: 21 50 C2        LD      HL,$C250            
5A6B: 09              ADD     HL,BC               
5A6C: 34              INC     (HL)                
5A6D: 7E              LD      A,(HL)              
5A6E: A7              AND     A                   
5A6F: 20 05           JR      NZ,$5A76            ; {}
5A71: 21 B0 C3        LD      HL,$C3B0            
5A74: 09              ADD     HL,BC               
5A75: 34              INC     (HL)                
5A76: FE 10           CP      $10                 
5A78: 20 03           JR      NZ,$5A7D            ; {}
5A7A: CD E5 65        CALL    $65E5               ; {}
5A7D: C9              RET                         
5A7E: 70              LD      (HL),B              
5A7F: 00              NOP                         
5A80: 72              LD      (HL),D              
5A81: 00              NOP                         
5A82: 74              LD      (HL),H              
5A83: 00              NOP                         
5A84: 76              HALT                        
5A85: 00              NOP                         
5A86: 72              LD      (HL),D              
5A87: 20 70           JR      NZ,$5AF9            ; {}
5A89: 20 76           JR      NZ,$5B01            ; {}
5A8B: 20 74           JR      NZ,$5B01            ; {}
5A8D: 20 00           JR      NZ,$5A8F            ; {}
5A8F: 00              NOP                         
5A90: 02              LD      (BC),A              
5A91: 00              NOP                         
5A92: 04              INC     B                   
5A93: 00              NOP                         
5A94: 06 00           LD      B,$00               
5A96: 02              LD      (BC),A              
5A97: 20 00           JR      NZ,$5A99            ; {}
5A99: 20 06           JR      NZ,$5AA1            ; {}
5A9B: 20 04           JR      NZ,$5AA1            ; {}
5A9D: 20 78           JR      NZ,$5B17            ; {}
5A9F: 00              NOP                         
5AA0: 7A              LD      A,D                 
5AA1: 00              NOP                         
5AA2: 7C              LD      A,H                 
5AA3: 00              NOP                         
5AA4: 7E              LD      A,(HL)              
5AA5: 00              NOP                         
5AA6: 7A              LD      A,D                 
5AA7: 20 78           JR      NZ,$5B21            ; {}
5AA9: 20 7E           JR      NZ,$5B29            ; {}
5AAB: 20 7C           JR      NZ,$5B29            ; {}
5AAD: 20 10           JR      NZ,$5ABF            ; {}
5AAF: 00              NOP                         
5AB0: 12              LD      (DE),A              
5AB1: 00              NOP                         
5AB2: 14              INC     D                   
5AB3: 00              NOP                         
5AB4: 16 00           LD      D,$00               
5AB6: 12              LD      (DE),A              
5AB7: 20 10           JR      NZ,$5AC9            ; {}
5AB9: 20 16           JR      NZ,$5AD1            ; {}
5ABB: 20 14           JR      NZ,$5AD1            ; {}
5ABD: 20 FA           JR      NZ,$5AB9            ; {}
5ABF: 9F              SBC     A                   
5AC0: C1              POP     BC                  
5AC1: A7              AND     A                   
5AC2: 28 1F           JR      Z,$5AE3             ; {}
5AC4: FA 73 C1        LD      A,($C173)           
5AC7: FE 82           CP      $82                 
5AC9: 28 18           JR      Z,$5AE3             ; {}
5ACB: CD 9E 65        CALL    $659E               ; {}
5ACE: 21 80 C3        LD      HL,$C380            
5AD1: 09              ADD     HL,BC               
5AD2: 73              LD      (HL),E              
5AD3: CD AF 3D        CALL    $3DAF               
5AD6: FA 70 C1        LD      A,($C170)           
5AD9: 1E 00           LD      E,$00               
5ADB: E6 06           AND     $06                 
5ADD: 28 01           JR      Z,$5AE0             ; {}
5ADF: 1C              INC     E                   
5AE0: 7B              LD      A,E                 
5AE1: E0 F1           LD      ($FF00+$F1),A       
5AE3: 21 80 C3        LD      HL,$C380            
5AE6: 09              ADD     HL,BC               
5AE7: 7E              LD      A,(HL)              
5AE8: A7              AND     A                   
5AE9: 20 06           JR      NZ,$5AF1            ; {}
5AEB: F0 F1           LD      A,($F1)             
5AED: C6 02           ADD     $02                 
5AEF: E0 F1           LD      ($FF00+$F1),A       
5AF1: 11 7E 5A        LD      DE,$5A7E            
5AF4: 21 B0 C2        LD      HL,$C2B0            
5AF7: 09              ADD     HL,BC               
5AF8: 7E              LD      A,(HL)              
5AF9: A7              AND     A                   
5AFA: 20 0D           JR      NZ,$5B09            ; {}
5AFC: F0 F6           LD      A,($F6)             
5AFE: FE B2           CP      $B2                 
5B00: 20 0A           JR      NZ,$5B0C            ; {}
5B02: FA 0E DB        LD      A,($DB0E)           
5B05: FE 03           CP      $03                 
5B07: 38 03           JR      C,$5B0C             ; {}
5B09: 11 9E 5A        LD      DE,$5A9E            
5B0C: FA 95 DB        LD      A,($DB95)           
5B0F: FE 01           CP      $01                 
5B11: 20 06           JR      NZ,$5B19            ; {}
5B13: F0 F1           LD      A,($F1)             
5B15: C6 04           ADD     $04                 
5B17: E0 F1           LD      ($FF00+$F1),A       
5B19: CD 3B 3C        CALL    $3C3B               
5B1C: CD DF 64        CALL    $64DF               ; {}
5B1F: CD E2 08        CALL    $08E2               
5B22: CD 84 65        CALL    $6584               ; {}
5B25: 21 20 C3        LD      HL,$C320            
5B28: 09              ADD     HL,BC               
5B29: 35              DEC     (HL)                
5B2A: 35              DEC     (HL)                
5B2B: 21 10 C3        LD      HL,$C310            
5B2E: 09              ADD     HL,BC               
5B2F: 7E              LD      A,(HL)              
5B30: E6 80           AND     $80                 
5B32: E0 E8           LD      ($FF00+$E8),A       
5B34: 28 07           JR      Z,$5B3D             ; {}
5B36: AF              XOR     A                   
5B37: 77              LD      (HL),A              
5B38: 21 20 C3        LD      HL,$C320            
5B3B: 09              ADD     HL,BC               
5B3C: 77              LD      (HL),A              
5B3D: F0 F0           LD      A,($F0)             
5B3F: FE 02           CP      $02                 
5B41: 30 2B           JR      NC,$5B6E            ; {}
5B43: CD 8C 64        CALL    $648C               ; {}
5B46: 30 26           JR      NC,$5B6E            ; {}
5B48: 1E 23           LD      E,$23               
5B4A: F0 F6           LD      A,($F6)             
5B4C: FE B2           CP      $B2                 
5B4E: 20 17           JR      NZ,$5B67            ; {}
5B50: 1E 80           LD      E,$80               
5B52: FA 0E DB        LD      A,($DB0E)           
5B55: FE 02           CP      $02                 
5B57: 20 07           JR      NZ,$5B60            ; {}
5B59: CD 8D 3B        CALL    $3B8D               
5B5C: 36 02           LD      (HL),$02            
5B5E: 1E 81           LD      E,$81               
5B60: 7B              LD      A,E                 
5B61: CD 85 21        CALL    $2185               
5B64: C3 A3 5B        JP      $5BA3               ; {}
5B67: 7B              LD      A,E                 
5B68: CD 97 21        CALL    $2197               
5B6B: CD A3 5B        CALL    $5BA3               ; {}
5B6E: F0 F0           LD      A,($F0)             
5B70: C7              RST     0X00                
5B71: BE              CP      (HL)                
5B72: 5B              LD      E,E                 
5B73: 01 5C 79        LD      BC,$795C            
5B76: 5B              LD      E,E                 
5B77: A8              XOR     B                   
5B78: 5B              LD      E,E                 
5B79: FA 9F C1        LD      A,($C19F)           
5B7C: A7              AND     A                   
5B7D: 20 28           JR      NZ,$5BA7            ; {}
5B7F: FA 77 C1        LD      A,($C177)           
5B82: A7              AND     A                   
5B83: 20 15           JR      NZ,$5B9A            ; {}
5B85: 3E 03           LD      A,$03               
5B87: EA 0E DB        LD      ($DB0E),A           
5B8A: 3E 0D           LD      A,$0D               
5B8C: E0 A5           LD      ($FF00+$A5),A       
5B8E: 3E 83           LD      A,$83               
5B90: CD 85 21        CALL    $2185               
5B93: CD A3 5B        CALL    $5BA3               ; {}
5B96: CD 8D 3B        CALL    $3B8D               
5B99: C9              RET                         
5B9A: CD 8D 3B        CALL    $3B8D               
5B9D: 70              LD      (HL),B              
5B9E: 3E 84           LD      A,$84               
5BA0: CD 85 21        CALL    $2185               
5BA3: 3E 18           LD      A,$18               
5BA5: E0 F3           LD      ($FF00+$F3),A       
5BA7: C9              RET                         
5BA8: FA 9F C1        LD      A,($C19F)           
5BAB: A7              AND     A                   
5BAC: 20 07           JR      NZ,$5BB5            ; {}
5BAE: CD 98 08        CALL    $0898               
5BB1: CD 8D 3B        CALL    $3B8D               
5BB4: 70              LD      (HL),B              
5BB5: C9              RET                         
5BB6: 02              LD      (BC),A              
5BB7: 08 0C 08        LD      ($080C),SP          
5BBA: FE F8           CP      $F8                 
5BBC: F4                              
5BBD: F8 AF           LD      HL,SP+$AF           
5BBF: CD 87 3B        CALL    $3B87               
5BC2: CD 91 08        CALL    $0891               
5BC5: 20 37           JR      NZ,$5BFE            ; {}
5BC7: CD ED 27        CALL    $27ED               
5BCA: E6 07           AND     $07                 
5BCC: 5F              LD      E,A                 
5BCD: 50              LD      D,B                 
5BCE: 21 B6 5B        LD      HL,$5BB6            
5BD1: 19              ADD     HL,DE               
5BD2: 7E              LD      A,(HL)              
5BD3: 21 40 C2        LD      HL,$C240            
5BD6: 09              ADD     HL,BC               
5BD7: 77              LD      (HL),A              
5BD8: 7B              LD      A,E                 
5BD9: E6 04           AND     $04                 
5BDB: 21 80 C3        LD      HL,$C380            
5BDE: 09              ADD     HL,BC               
5BDF: 77              LD      (HL),A              
5BE0: CD ED 27        CALL    $27ED               
5BE3: E6 07           AND     $07                 
5BE5: 5F              LD      E,A                 
5BE6: 21 B6 5B        LD      HL,$5BB6            
5BE9: 19              ADD     HL,DE               
5BEA: 7E              LD      A,(HL)              
5BEB: 21 50 C2        LD      HL,$C250            
5BEE: 09              ADD     HL,BC               
5BEF: 77              LD      (HL),A              
5BF0: CD 91 08        CALL    $0891               
5BF3: CD ED 27        CALL    $27ED               
5BF6: E6 1F           AND     $1F                 
5BF8: C6 30           ADD     $30                 
5BFA: 77              LD      (HL),A              
5BFB: CD 8D 3B        CALL    $3B8D               
5BFE: C3 23 5C        JP      $5C23               ; {}
5C01: CD 4B 65        CALL    $654B               ; {}
5C04: CD 9E 3B        CALL    $3B9E               
5C07: F0 E8           LD      A,($E8)             
5C09: A7              AND     A                   
5C0A: 28 17           JR      Z,$5C23             ; {}
5C0C: CD 91 08        CALL    $0891               
5C0F: 20 07           JR      NZ,$5C18            ; {}
5C11: 36 30           LD      (HL),$30            
5C13: CD 8D 3B        CALL    $3B8D               
5C16: 70              LD      (HL),B              
5C17: C9              RET                         
5C18: 21 20 C3        LD      HL,$C320            
5C1B: 09              ADD     HL,BC               
5C1C: 36 08           LD      (HL),$08            
5C1E: 21 10 C3        LD      HL,$C310            
5C21: 09              ADD     HL,BC               
5C22: 34              INC     (HL)                
5C23: F0 E7           LD      A,($E7)             
5C25: 1F              RRA                         
5C26: 1F              RRA                         
5C27: 1F              RRA                         
5C28: E6 01           AND     $01                 
5C2A: CD 87 3B        CALL    $3B87               
5C2D: C9              RET                         
5C2E: 60              LD      H,B                 
5C2F: 00              NOP                         
5C30: 62              LD      H,D                 
5C31: 00              NOP                         
5C32: 62              LD      H,D                 
5C33: 20 60           JR      NZ,$5C95            ; {}
5C35: 20 64           JR      NZ,$5C9B            ; {}
5C37: 00              NOP                         
5C38: 66              LD      H,(HL)              
5C39: 00              NOP                         
5C3A: 66              LD      H,(HL)              
5C3B: 20 64           JR      NZ,$5CA1            ; {}
5C3D: 20 68           JR      NZ,$5CA7            ; {}
5C3F: 00              NOP                         
5C40: 6A              LD      L,D                 
5C41: 00              NOP                         
5C42: 6C              LD      L,H                 
5C43: 00              NOP                         
5C44: 6E              LD      L,(HL)              
5C45: 00              NOP                         
5C46: 6A              LD      L,D                 
5C47: 20 68           JR      NZ,$5CB1            ; {}
5C49: 20 6E           JR      NZ,$5CB9            ; {}
5C4B: 20 6C           JR      NZ,$5CB9            ; {}
5C4D: 20 CD           JR      NZ,$5C1C            ; {}
5C4F: 91              SUB     C                   
5C50: 08 FE 01        LD      ($01FE),SP          
5C53: 20 06           JR      NZ,$5C5B            ; {}
5C55: 70              LD      (HL),B              
5C56: 3E FF           LD      A,$FF               
5C58: EA 93 DB        LD      ($DB93),A           
5C5B: F0 E7           LD      A,($E7)             
5C5D: E6 1F           AND     $1F                 
5C5F: 20 08           JR      NZ,$5C69            ; {}
5C61: CD BE 65        CALL    $65BE               ; {}
5C64: 21 80 C3        LD      HL,$C380            
5C67: 09              ADD     HL,BC               
5C68: 73              LD      (HL),E              
5C69: CD 70 64        CALL    $6470               ; {}
5C6C: 11 2E 5C        LD      DE,$5C2E            
5C6F: CD 3B 3C        CALL    $3C3B               
5C72: FA 56 DB        LD      A,($DB56)           
5C75: FE 80           CP      $80                 
5C77: 20 23           JR      NZ,$5C9C            ; {}
5C79: CD 84 65        CALL    $6584               ; {}
5C7C: 21 20 C3        LD      HL,$C320            
5C7F: 09              ADD     HL,BC               
5C80: 35              DEC     (HL)                
5C81: 35              DEC     (HL)                
5C82: 21 10 C3        LD      HL,$C310            
5C85: 09              ADD     HL,BC               
5C86: 7E              LD      A,(HL)              
5C87: A7              AND     A                   
5C88: 28 04           JR      Z,$5C8E             ; {}
5C8A: E6 80           AND     $80                 
5C8C: 28 0E           JR      Z,$5C9C             ; {}
5C8E: 70              LD      (HL),B              
5C8F: 21 20 C3        LD      HL,$C320            
5C92: 09              ADD     HL,BC               
5C93: 70              LD      (HL),B              
5C94: F0 E7           LD      A,($E7)             
5C96: E6 3F           AND     $3F                 
5C98: 20 02           JR      NZ,$5C9C            ; {}
5C9A: 36 10           LD      (HL),$10            
5C9C: CD DF 64        CALL    $64DF               ; {}
5C9F: F0 EF           LD      A,($EF)             
5CA1: E0 EC           LD      ($FF00+$EC),A       
5CA3: CD 49 64        CALL    $6449               ; {}
5CA6: CD BA 3D        CALL    $3DBA               
5CA9: CD 8C 64        CALL    $648C               ; {}
5CAC: 30 2F           JR      NC,$5CDD            ; {}
5CAE: 1E 30           LD      E,$30               
5CB0: FA 66 DB        LD      A,($DB66)           
5CB3: E6 02           AND     $02                 
5CB5: 28 14           JR      Z,$5CCB             ; {}
5CB7: FA 56 DB        LD      A,($DB56)           
5CBA: FE 01           CP      $01                 
5CBC: 20 0D           JR      NZ,$5CCB            ; {}
5CBE: AF              XOR     A                   
5CBF: EA 56 DB        LD      ($DB56),A           
5CC2: CD 91 08        CALL    $0891               
5CC5: 36 10           LD      (HL),$10            
5CC7: 1E 2F           LD      E,$2F               
5CC9: 18 0E           JR      $5CD9               ; {}
5CCB: FA 56 DB        LD      A,($DB56)           
5CCE: A7              AND     A                   
5CCF: 28 08           JR      Z,$5CD9             ; {}
5CD1: 1E 31           LD      E,$31               
5CD3: FE 01           CP      $01                 
5CD5: 20 02           JR      NZ,$5CD9            ; {}
5CD7: 1E 32           LD      E,$32               
5CD9: 7B              LD      A,E                 
5CDA: CD DE 5C        CALL    $5CDE               ; {}
5CDD: C9              RET                         
5CDE: 7B              LD      A,E                 
5CDF: CD 85 21        CALL    $2185               
5CE2: 21 9F C1        LD      HL,$C19F            
5CE5: CB FE           SET     1,E                 
5CE7: C9              RET                         
5CE8: CD 33 5D        CALL    $5D33               ; {}
5CEB: CD DF 64        CALL    $64DF               ; {}
5CEE: F0 E7           LD      A,($E7)             
5CF0: 1F              RRA                         
5CF1: 1F              RRA                         
5CF2: 1F              RRA                         
5CF3: 1F              RRA                         
5CF4: 1F              RRA                         
5CF5: E6 01           AND     $01                 
5CF7: CD 87 3B        CALL    $3B87               
5CFA: CD 49 64        CALL    $6449               ; {}
5CFD: CD 8C 64        CALL    $648C               ; {}
5D00: 30 10           JR      NC,$5D12            ; {}
5D02: FA 55 DB        LD      A,($DB55)           
5D05: A7              AND     A                   
5D06: 20 05           JR      NZ,$5D0D            ; {}
5D08: 3E 01           LD      A,$01               
5D0A: EA 55 DB        LD      ($DB55),A           
5D0D: 3E 40           LD      A,$40               
5D0F: CD 85 21        CALL    $2185               
5D12: C9              RET                         
5D13: F0 00           LD      A,($00)             
5D15: 70              LD      (HL),B              
5D16: 00              NOP                         
5D17: F0 08           LD      A,($08)             
5D19: 72              LD      (HL),D              
5D1A: 00              NOP                         
5D1B: 00              NOP                         
5D1C: 00              NOP                         
5D1D: 74              LD      (HL),H              
5D1E: 00              NOP                         
5D1F: 00              NOP                         
5D20: 08 76 00        LD      ($0076),SP          
5D23: F0 00           LD      A,($00)             
5D25: 78              LD      A,B                 
5D26: 00              NOP                         
5D27: F0 08           LD      A,($08)             
5D29: 7A              LD      A,D                 
5D2A: 00              NOP                         
5D2B: 00              NOP                         
5D2C: 00              NOP                         
5D2D: 7C              LD      A,H                 
5D2E: 00              NOP                         
5D2F: 00              NOP                         
5D30: 08 7E 00        LD      ($007E),SP          
5D33: F0 F1           LD      A,($F1)             
5D35: 17              RLA                         
5D36: 17              RLA                         
5D37: 17              RLA                         
5D38: 17              RLA                         
5D39: E6 F0           AND     $F0                 
5D3B: 5F              LD      E,A                 
5D3C: 50              LD      D,B                 
5D3D: 21 13 5D        LD      HL,$5D13            
5D40: 19              ADD     HL,DE               
5D41: 0E 04           LD      C,$04               
5D43: CD 26 3D        CALL    $3D26               
5D46: 3E 04           LD      A,$04               
5D48: CD D0 3D        CALL    $3DD0               
5D4B: C9              RET                         
5D4C: 50              LD      D,B                 
5D4D: 00              NOP                         
5D4E: 52              LD      D,D                 
5D4F: 00              NOP                         
5D50: 54              LD      D,H                 
5D51: 00              NOP                         
5D52: 56              LD      D,(HL)              
5D53: 00              NOP                         
5D54: 52              LD      D,D                 
5D55: 20 50           JR      NZ,$5DA7            ; {}
5D57: 20 56           JR      NZ,$5DAF            ; {}
5D59: 20 54           JR      NZ,$5DAF            ; {}
5D5B: 20 F0           JR      NZ,$5D4D            ; {}
5D5D: F6 FE           OR      $FE                 
5D5F: 58              LD      E,B                 
5D60: 20 13           JR      NZ,$5D75            ; {}
5D62: F0 F8           LD      A,($F8)             
5D64: E6 10           AND     $10                 
5D66: C2 E5 65        JP      NZ,$65E5            ; {}
5D69: 21 60 C4        LD      HL,$C460            
5D6C: 09              ADD     HL,BC               
5D6D: 36 FF           LD      (HL),$FF            
5D6F: 21 E0 C4        LD      HL,$C4E0            
5D72: 09              ADD     HL,BC               
5D73: 36 3C           LD      (HL),$3C            
5D75: 21 80 C3        LD      HL,$C380            
5D78: 09              ADD     HL,BC               
5D79: 7E              LD      A,(HL)              
5D7A: A7              AND     A                   
5D7B: 20 06           JR      NZ,$5D83            ; {}
5D7D: F0 F1           LD      A,($F1)             
5D7F: C6 02           ADD     $02                 
5D81: E0 F1           LD      ($FF00+$F1),A       
5D83: 11 4C 5D        LD      DE,$5D4C            
5D86: CD 3B 3C        CALL    $3C3B               
5D89: F0 F0           LD      A,($F0)             
5D8B: A7              AND     A                   
5D8C: 20 0E           JR      NZ,$5D9C            ; {}
5D8E: 21 10 C2        LD      HL,$C210            
5D91: 09              ADD     HL,BC               
5D92: 7E              LD      A,(HL)              
5D93: D6 04           SUB     $04                 
5D95: 77              LD      (HL),A              
5D96: CD 8D 3B        CALL    $3B8D               
5D99: 7E              LD      A,(HL)              
5D9A: E0 F0           LD      ($FF00+$F0),A       
5D9C: CD DF 64        CALL    $64DF               ; {}
5D9F: CD 01 65        CALL    $6501               ; {}
5DA2: F0 F0           LD      A,($F0)             
5DA4: 3D              DEC     A                   
5DA5: C7              RST     0X00                
5DA6: AE              XOR     (HL)                
5DA7: 5D              LD      E,L                 
5DA8: 14              INC     D                   
5DA9: 5E              LD      E,(HL)              
5DAA: 2F              CPL                         
5DAB: 5E              LD      E,(HL)              
5DAC: 7F              LD      A,A                 
5DAD: 5E              LD      E,(HL)              
5DAE: F0 F6           LD      A,($F6)             
5DB0: FE 58           CP      $58                 
5DB2: 20 3A           JR      NZ,$5DEE            ; {}
5DB4: FA 0C C5        LD      A,($C50C)           
5DB7: 5F              LD      E,A                 
5DB8: 50              LD      D,B                 
5DB9: 21 80 C2        LD      HL,$C280            
5DBC: 19              ADD     HL,DE               
5DBD: 7E              LD      A,(HL)              
5DBE: A7              AND     A                   
5DBF: 28 52           JR      Z,$5E13             ; {}
5DC1: 21 A0 C3        LD      HL,$C3A0            
5DC4: 19              ADD     HL,DE               
5DC5: 7E              LD      A,(HL)              
5DC6: FE 05           CP      $05                 
5DC8: 20 49           JR      NZ,$5E13            ; {}
5DCA: 21 F0 C2        LD      HL,$C2F0            
5DCD: 19              ADD     HL,DE               
5DCE: 7E              LD      A,(HL)              
5DCF: A7              AND     A                   
5DD0: 28 41           JR      Z,$5E13             ; {}
5DD2: 21 00 C2        LD      HL,$C200            
5DD5: 19              ADD     HL,DE               
5DD6: F0 EE           LD      A,($EE)             
5DD8: 96              SUB     (HL)                
5DD9: C6 10           ADD     $10                 
5DDB: FE 20           CP      $20                 
5DDD: 30 34           JR      NC,$5E13            ; {}
5DDF: 21 10 C2        LD      HL,$C210            
5DE2: 19              ADD     HL,DE               
5DE3: F0 EC           LD      A,($EC)             
5DE5: 96              SUB     (HL)                
5DE6: C6 28           ADD     $28                 
5DE8: FE 50           CP      $50                 
5DEA: 30 27           JR      NC,$5E13            ; {}
5DEC: 18 17           JR      $5E05               ; {}
5DEE: CD 9E 65        CALL    $659E               ; {}
5DF1: 21 80 C3        LD      HL,$C380            
5DF4: 09              ADD     HL,BC               
5DF5: 73              LD      (HL),E              
5DF6: C6 18           ADD     $18                 
5DF8: FE 30           CP      $30                 
5DFA: 30 17           JR      NC,$5E13            ; {}
5DFC: CD AE 65        CALL    $65AE               ; {}
5DFF: C6 30           ADD     $30                 
5E01: FE 60           CP      $60                 
5E03: 30 0E           JR      NC,$5E13            ; {}
5E05: 21 40 C3        LD      HL,$C340            
5E08: 09              ADD     HL,BC               
5E09: 36 12           LD      (HL),$12            
5E0B: CD 91 08        CALL    $0891               
5E0E: 36 22           LD      (HL),$22            
5E10: CD 8D 3B        CALL    $3B8D               
5E13: C9              RET                         
5E14: CD B4 3B        CALL    $3BB4               
5E17: CD 91 08        CALL    $0891               
5E1A: 20 05           JR      NZ,$5E21            ; {}
5E1C: 36 30           LD      (HL),$30            
5E1E: C3 8D 3B        JP      $3B8D               
5E21: CD AF 3D        CALL    $3DAF               
5E24: 21 20 C3        LD      HL,$C320            
5E27: 09              ADD     HL,BC               
5E28: 36 08           LD      (HL),$08            
5E2A: CD 84 65        CALL    $6584               ; {}
5E2D: 18 40           JR      $5E6F               ; {}
5E2F: CD B4 3B        CALL    $3BB4               
5E32: CD 91 08        CALL    $0891               
5E35: CA 8D 3B        JP      Z,$3B8D             
5E38: E6 01           AND     $01                 
5E3A: 20 2D           JR      NZ,$5E69            ; {}
5E3C: 3E 20           LD      A,$20               
5E3E: CD 30 3C        CALL    $3C30               
5E41: F0 D7           LD      A,($D7)             
5E43: 21 50 C2        LD      HL,$C250            
5E46: 09              ADD     HL,BC               
5E47: 96              SUB     (HL)                
5E48: E6 80           AND     $80                 
5E4A: 20 02           JR      NZ,$5E4E            ; {}
5E4C: 34              INC     (HL)                
5E4D: 34              INC     (HL)                
5E4E: 35              DEC     (HL)                
5E4F: F0 D8           LD      A,($D8)             
5E51: 21 40 C2        LD      HL,$C240            
5E54: 09              ADD     HL,BC               
5E55: 96              SUB     (HL)                
5E56: E6 80           AND     $80                 
5E58: 20 02           JR      NZ,$5E5C            ; {}
5E5A: 34              INC     (HL)                
5E5B: 34              INC     (HL)                
5E5C: 35              DEC     (HL)                
5E5D: 21 40 C2        LD      HL,$C240            
5E60: 09              ADD     HL,BC               
5E61: 7E              LD      A,(HL)              
5E62: E6 80           AND     $80                 
5E64: 21 80 C3        LD      HL,$C380            
5E67: 09              ADD     HL,BC               
5E68: 77              LD      (HL),A              
5E69: CD 4B 65        CALL    $654B               ; {}
5E6C: CD 7B 5E        CALL    $5E7B               ; {}
5E6F: CD 7B 5E        CALL    $5E7B               ; {}
5E72: 7E              LD      A,(HL)              
5E73: 1F              RRA                         
5E74: 1F              RRA                         
5E75: 1F              RRA                         
5E76: E6 01           AND     $01                 
5E78: C3 87 3B        JP      $3B87               
5E7B: CD C5 29        CALL    $29C5               
5E7E: C9              RET                         
5E7F: CD B4 3B        CALL    $3BB4               
5E82: F0 E7           LD      A,($E7)             
5E84: E6 03           AND     $03                 
5E86: 20 31           JR      NZ,$5EB9            ; {}
5E88: 3E 20           LD      A,$20               
5E8A: CD 30 3C        CALL    $3C30               
5E8D: F0 D7           LD      A,($D7)             
5E8F: 2F              CPL                         
5E90: 3C              INC     A                   
5E91: 21 50 C2        LD      HL,$C250            
5E94: 09              ADD     HL,BC               
5E95: 96              SUB     (HL)                
5E96: E6 80           AND     $80                 
5E98: 20 02           JR      NZ,$5E9C            ; {}
5E9A: 34              INC     (HL)                
5E9B: 34              INC     (HL)                
5E9C: 35              DEC     (HL)                
5E9D: F0 D8           LD      A,($D8)             
5E9F: 2F              CPL                         
5EA0: 3C              INC     A                   
5EA1: 21 40 C2        LD      HL,$C240            
5EA4: 09              ADD     HL,BC               
5EA5: 96              SUB     (HL)                
5EA6: E6 80           AND     $80                 
5EA8: 20 02           JR      NZ,$5EAC            ; {}
5EAA: 34              INC     (HL)                
5EAB: 34              INC     (HL)                
5EAC: 35              DEC     (HL)                
5EAD: 21 40 C2        LD      HL,$C240            
5EB0: 09              ADD     HL,BC               
5EB1: 7E              LD      A,(HL)              
5EB2: E6 80           AND     $80                 
5EB4: 21 80 C3        LD      HL,$C380            
5EB7: 09              ADD     HL,BC               
5EB8: 77              LD      (HL),A              
5EB9: CD 69 5E        CALL    $5E69               ; {}
5EBC: F0 EC           LD      A,($EC)             
5EBE: FE 88           CP      $88                 
5EC0: D2 E5 65        JP      NC,$65E5            ; {}
5EC3: F0 EE           LD      A,($EE)             
5EC5: FE A8           CP      $A8                 
5EC7: D2 E5 65        JP      NC,$65E5            ; {}
5ECA: C9              RET                         
5ECB: F8 00           LD      HL,SP+$00           
5ECD: 64              LD      H,H                 
5ECE: 00              NOP                         
5ECF: F8 08           LD      HL,SP+$08           
5ED1: 66              LD      H,(HL)              
5ED2: 00              NOP                         
5ED3: 08 00 68        LD      ($6800),SP          ; {}
5ED6: 00              NOP                         
5ED7: 08 08 6A        LD      ($6A08),SP          ; {}
5EDA: 00              NOP                         
5EDB: F8 00           LD      HL,SP+$00           
5EDD: 60              LD      H,B                 
5EDE: 00              NOP                         
5EDF: F8 08           LD      HL,SP+$08           
5EE1: 62              LD      H,D                 
5EE2: 00              NOP                         
5EE3: 08 00 68        LD      ($6800),SP          ; {}
5EE6: 00              NOP                         
5EE7: 08 08 6A        LD      ($6A08),SP          ; {}
5EEA: 00              NOP                         
5EEB: F8 00           LD      HL,SP+$00           
5EED: 66              LD      H,(HL)              
5EEE: 20 F8           JR      NZ,$5EE8            ; {}
5EF0: 08 64 20        LD      ($2064),SP          
5EF3: 08 00 6A        LD      ($6A00),SP          ; {}
5EF6: 20 08           JR      NZ,$5F00            ; {}
5EF8: 08 68 20        LD      ($2068),SP          
5EFB: A0              AND     B                   
5EFC: 10 CD           ;;STOP    $CD                 
5EFE: 91              SUB     C                   
5EFF: 08 28 2D        LD      ($2D28),SP          
5F02: F0 98           LD      A,($98)             
5F04: E0 EE           LD      ($FF00+$EE),A       
5F06: FA 45 C1        LD      A,($C145)           
5F09: D6 10           SUB     $10                 
5F0B: E0 EC           LD      ($FF00+$EC),A       
5F0D: 3E 6C           LD      A,$6C               
5F0F: E0 9D           LD      ($FF00+$9D),A       
5F11: 3E 02           LD      A,$02               
5F13: E0 A1           LD      ($FF00+$A1),A       
5F15: 3E 03           LD      A,$03               
5F17: E0 9E           LD      ($FF00+$9E),A       
5F19: AF              XOR     A                   
5F1A: EA 37 C1        LD      ($C137),A           
5F1D: EA 6A C1        LD      ($C16A),A           
5F20: EA 22 C1        LD      ($C122),A           
5F23: EA 21 C1        LD      ($C121),A           
5F26: 11 FB 5E        LD      DE,$5EFB            
5F29: CD D0 3C        CALL    $3CD0               
5F2C: CD BA 3D        CALL    $3DBA               
5F2F: 1E 00           LD      E,$00               
5F31: F0 98           LD      A,($98)             
5F33: FE 30           CP      $30                 
5F35: 38 08           JR      C,$5F3F             ; {}
5F37: 1E 01           LD      E,$01               
5F39: FE 60           CP      $60                 
5F3B: 38 02           JR      C,$5F3F             ; {}
5F3D: 1E 02           LD      E,$02               
5F3F: 7B              LD      A,E                 
5F40: E0 F1           LD      ($FF00+$F1),A       
5F42: 17              RLA                         
5F43: 17              RLA                         
5F44: 17              RLA                         
5F45: 17              RLA                         
5F46: E6 F0           AND     $F0                 
5F48: 5F              LD      E,A                 
5F49: 50              LD      D,B                 
5F4A: 21 CB 5E        LD      HL,$5ECB            
5F4D: 19              ADD     HL,DE               
5F4E: F0 EC           LD      A,($EC)             
5F50: D6 04           SUB     $04                 
5F52: E0 EC           LD      ($FF00+$EC),A       
5F54: 0E 04           LD      C,$04               
5F56: CD 26 3D        CALL    $3D26               
5F59: 3E 04           LD      A,$04               
5F5B: CD D0 3D        CALL    $3DD0               
5F5E: CD BA 3D        CALL    $3DBA               
5F61: CD DF 64        CALL    $64DF               ; {}
5F64: CD 49 64        CALL    $6449               ; {}
5F67: F0 F0           LD      A,($F0)             
5F69: C7              RST     0X00                
5F6A: 82              ADD     A,D                 
5F6B: 5F              LD      E,A                 
5F6C: A8              XOR     B                   
5F6D: 5F              LD      E,A                 
5F6E: E5              PUSH    HL                  
5F6F: 5F              LD      E,A                 
5F70: 70              LD      (HL),B              
5F71: 60              LD      H,B                 
5F72: 79              LD      A,C                 
5F73: 60              LD      H,B                 
5F74: F0 99           LD      A,($99)             
5F76: 21 EF FF        LD      HL,$FFEF            
5F79: 96              SUB     (HL)                
5F7A: C6 28           ADD     $28                 
5F7C: FE 50           CP      $50                 
5F7E: CD 97 64        CALL    $6497               ; {}
5F81: C9              RET                         
5F82: CD 74 5F        CALL    $5F74               ; {}
5F85: 30 20           JR      NC,$5FA7            ; {}
5F87: 3E 17           LD      A,$17               
5F89: CD 97 21        CALL    $2197               
5F8C: 21 9F C1        LD      HL,$C19F            
5F8F: CB FE           SET     1,E                 
5F91: FA 15 D4        LD      A,($D415)           
5F94: E6 01           AND     $01                 
5F96: 21 B0 C2        LD      HL,$C2B0            
5F99: 09              ADD     HL,BC               
5F9A: 77              LD      (HL),A              
5F9B: FA 75 DB        LD      A,($DB75)           
5F9E: FE 07           CP      $07                 
5FA0: 20 02           JR      NZ,$5FA4            ; {}
5FA2: 34              INC     (HL)                
5FA3: 34              INC     (HL)                
5FA4: CD 8D 3B        CALL    $3B8D               
5FA7: C9              RET                         
5FA8: CD 74 5F        CALL    $5F74               ; {}
5FAB: D0              RET     NC                  
5FAC: FA 0D DB        LD      A,($DB0D)           
5FAF: A7              AND     A                   
5FB0: 20 18           JR      NZ,$5FCA            ; {}
5FB2: 21 B0 C2        LD      HL,$C2B0            
5FB5: 09              ADD     HL,BC               
5FB6: 7E              LD      A,(HL)              
5FB7: E6 01           AND     $01                 
5FB9: 3E 18           LD      A,$18               
5FBB: 28 02           JR      Z,$5FBF             ; {}
5FBD: 3E 19           LD      A,$19               
5FBF: CD 97 21        CALL    $2197               
5FC2: 21 9F C1        LD      HL,$C19F            
5FC5: CB FE           SET     1,E                 
5FC7: C3 8D 3B        JP      $3B8D               
5FCA: 3E 1C           LD      A,$1C               
5FCC: CD 97 21        CALL    $2197               
5FCF: 21 9F C1        LD      HL,$C19F            
5FD2: CB FE           SET     1,E                 
5FD4: C9              RET                         
5FD5: 28 42           JR      Z,$6019             ; {}
5FD7: 07              RLCA                        
5FD8: 07              RLCA                        
5FD9: 00              NOP                         
5FDA: 00              NOP                         
5FDB: 00              NOP                         
5FDC: 00              NOP                         
5FDD: 1C              INC     E                   
5FDE: 2A              LD      A,(HLI)             
5FDF: 07              RLCA                        
5FE0: 07              RLCA                        
5FE1: 00              NOP                         
5FE2: 00              NOP                         
5FE3: 00              NOP                         
5FE4: 00              NOP                         
5FE5: FA 9F C1        LD      A,($C19F)           
5FE8: A7              AND     A                   
5FE9: C2 6F 60        JP      NZ,$606F            ; {}
5FEC: FA 77 C1        LD      A,($C177)           
5FEF: A7              AND     A                   
5FF0: 20 6F           JR      NZ,$6061            ; {}
5FF2: 21 B0 C2        LD      HL,$C2B0            
5FF5: 09              ADD     HL,BC               
5FF6: 5E              LD      E,(HL)              
5FF7: 50              LD      D,B                 
5FF8: 21 D9 5F        LD      HL,$5FD9            
5FFB: 19              ADD     HL,DE               
5FFC: 7E              LD      A,(HL)              
5FFD: 21 D5 5F        LD      HL,$5FD5            
6000: 19              ADD     HL,DE               
6001: 5E              LD      E,(HL)              
6002: 57              LD      D,A                 
6003: FA 5E DB        LD      A,($DB5E)           
6006: 93              SUB     E                   
6007: FA 5D DB        LD      A,($DB5D)           
600A: 9A              SBC     D                   
600B: 30 04           JR      NC,$6011            ; {}
600D: 3E 1B           LD      A,$1B               
600F: 18 52           JR      $6063               ; {}
6011: FA 75 DB        LD      A,($DB75)           
6014: 3C              INC     A                   
6015: E6 07           AND     $07                 
6017: EA 75 DB        LD      ($DB75),A           
601A: 20 0D           JR      NZ,$6029            ; {}
601C: 3E 1E           LD      A,$1E               
601E: CD 97 21        CALL    $2197               
6021: 21 9F C1        LD      HL,$C19F            
6024: CB FE           SET     1,E                 
6026: C3 8D 3B        JP      $3B8D               
6029: 21 B0 C2        LD      HL,$C2B0            
602C: 09              ADD     HL,BC               
602D: 5E              LD      E,(HL)              
602E: 50              LD      D,B                 
602F: 21 DD 5F        LD      HL,$5FDD            
6032: 19              ADD     HL,DE               
6033: FA 92 DB        LD      A,($DB92)           
6036: 86              ADD     A,(HL)              
6037: EA 92 DB        LD      ($DB92),A           
603A: CB 17           RL      1,E                 
603C: 21 E1 5F        LD      HL,$5FE1            
603F: 19              ADD     HL,DE               
6040: CB 1F           RR      1,E                 
6042: FA 91 DB        LD      A,($DB91)           
6045: 8E              ADC     A,(HL)              
6046: EA 91 DB        LD      ($DB91),A           
6049: 21 0D DB        LD      HL,$DB0D            
604C: 34              INC     (HL)                
604D: 3E 1A           LD      A,$1A               
604F: CD 63 60        CALL    $6063               ; {}
6052: CD 8D 3B        CALL    $3B8D               
6055: 36 04           LD      (HL),$04            
6057: CD 91 08        CALL    $0891               
605A: 36 20           LD      (HL),$20            
605C: 3E 01           LD      A,$01               
605E: E0 F2           LD      ($FF00+$F2),A       
6060: C9              RET                         
6061: 3E 1D           LD      A,$1D               
6063: CD 97 21        CALL    $2197               
6066: 21 9F C1        LD      HL,$C19F            
6069: CB FE           SET     1,E                 
606B: CD 8D 3B        CALL    $3B8D               
606E: 70              LD      (HL),B              
606F: C9              RET                         
6070: FA 9F C1        LD      A,($C19F)           
6073: A7              AND     A                   
6074: 20 02           JR      NZ,$6078            ; {}
6076: 18 B1           JR      $6029               ; {}
6078: C9              RET                         
6079: CD 91 08        CALL    $0891               
607C: C0              RET     NZ                  
607D: FA 9F C1        LD      A,($C19F)           
6080: A7              AND     A                   
6081: 20 19           JR      NZ,$609C            ; {}
6083: FA A9 C5        LD      A,($C5A9)           
6086: A7              AND     A                   
6087: 20 0F           JR      NZ,$6098            ; {}
6089: 3E FF           LD      A,$FF               
608B: EA 93 DB        LD      ($DB93),A           
608E: 3E 9A           LD      A,$9A               
6090: CD 85 21        CALL    $2185               
6093: 21 9F C1        LD      HL,$C19F            
6096: CB FE           SET     1,E                 
6098: CD 8D 3B        CALL    $3B8D               
609B: 70              LD      (HL),B              
609C: 3E 02           LD      A,$02               
609E: E0 A1           LD      ($FF00+$A1),A       
60A0: C9              RET                         
60A1: 70              LD      (HL),B              
60A2: 00              NOP                         
60A3: 72              LD      (HL),D              
60A4: 00              NOP                         
60A5: 72              LD      (HL),D              
60A6: 20 70           JR      NZ,$6118            ; {}
60A8: 20 74           JR      NZ,$611E            ; {}
60AA: 00              NOP                         
60AB: 76              HALT                        
60AC: 00              NOP                         
60AD: 76              HALT                        
60AE: 20 74           JR      NZ,$6124            ; {}
60B0: 20 78           JR      NZ,$612A            ; {}
60B2: 00              NOP                         
60B3: 7A              LD      A,D                 
60B4: 00              NOP                         
60B5: 7C              LD      A,H                 
60B6: 00              NOP                         
60B7: 7E              LD      A,(HL)              
60B8: 00              NOP                         
60B9: 7A              LD      A,D                 
60BA: 20 78           JR      NZ,$6134            ; {}
60BC: 20 7E           JR      NZ,$613C            ; {}
60BE: 20 7C           JR      NZ,$613C            ; {}
60C0: 20 3E           JR      NZ,$6100            ; {}
60C2: 00              NOP                         
60C3: 21 B0 C2        LD      HL,$C2B0            
60C6: 09              ADD     HL,BC               
60C7: 7E              LD      A,(HL)              
60C8: A7              AND     A                   
60C9: 28 1B           JR      Z,$60E6             ; {}
60CB: 11 C1 60        LD      DE,$60C1            
60CE: CD D0 3C        CALL    $3CD0               
60D1: CD DF 64        CALL    $64DF               ; {}
60D4: CD 4B 65        CALL    $654B               ; {}
60D7: CD 84 65        CALL    $6584               ; {}
60DA: 21 20 C3        LD      HL,$C320            
60DD: 09              ADD     HL,BC               
60DE: 35              DEC     (HL)                
60DF: CD 91 08        CALL    $0891               
60E2: CA E5 65        JP      Z,$65E5             ; {}
60E5: C9              RET                         
60E6: FA 56 DB        LD      A,($DB56)           
60E9: FE 80           CP      $80                 
60EB: C2 A8 61        JP      NZ,$61A8            ; {}
60EE: FA 95 DB        LD      A,($DB95)           
60F1: FE 01           CP      $01                 
60F3: CA A8 61        JP      Z,$61A8             ; {}
60F6: 11 A1 60        LD      DE,$60A1            
60F9: CD 3B 3C        CALL    $3C3B               
60FC: CD AE 65        CALL    $65AE               ; {}
60FF: 7B              LD      A,E                 
6100: 3D              DEC     A                   
6101: E6 02           AND     $02                 
6103: EE 02           XOR     $02                 
6105: 5F              LD      E,A                 
6106: F0 E7           LD      A,($E7)             
6108: 1F              RRA                         
6109: 1F              RRA                         
610A: 1F              RRA                         
610B: E6 01           AND     $01                 
610D: 83              ADD     A,E                 
610E: CD 87 3B        CALL    $3B87               
6111: 21 D0 C2        LD      HL,$C2D0            
6114: 09              ADD     HL,BC               
6115: 7E              LD      A,(HL)              
6116: C7              RST     0X00                
6117: 1D              DEC     E                   
6118: 61              LD      H,C                 
6119: 35              DEC     (HL)                
611A: 61              LD      H,C                 
611B: 6C              LD      L,H                 
611C: 61              LD      H,C                 
611D: CD DF 64        CALL    $64DF               ; {}
6120: 21 C0 C2        LD      HL,$C2C0            
6123: 09              ADD     HL,BC               
6124: 36 30           LD      (HL),$30            
6126: 3E 0E           LD      A,$0E               
6128: EA 68 D3        LD      ($D368),A           
612B: E0 B0           LD      ($FF00+$B0),A       
612D: E0 BD           LD      ($FF00+$BD),A       
612F: 21 D0 C2        LD      HL,$C2D0            
6132: 09              ADD     HL,BC               
6133: 34              INC     (HL)                
6134: C9              RET                         
6135: CD DF 64        CALL    $64DF               ; {}
6138: CD AE 65        CALL    $65AE               ; {}
613B: C6 20           ADD     $20                 
613D: FE 40           CP      $40                 
613F: 38 07           JR      C,$6148             ; {}
6141: 21 C0 C2        LD      HL,$C2C0            
6144: 09              ADD     HL,BC               
6145: 35              DEC     (HL)                
6146: 20 14           JR      NZ,$615C            ; {}
6148: FA 6B C1        LD      A,($C16B)           
614B: FE 04           CP      $04                 
614D: C0              RET     NZ                  
614E: F0 EB           LD      A,($EB)             
6150: FE 71           CP      $71                 
6152: 20 05           JR      NZ,$6159            ; {}
6154: 3E 20           LD      A,$20               
6156: CD 8E 21        CALL    $218E               
6159: C3 2F 61        JP      $612F               ; {}
615C: 3E 08           LD      A,$08               
615E: CD 25 3C        CALL    $3C25               
6161: CD 4B 65        CALL    $654B               ; {}
6164: 3E 02           LD      A,$02               
6166: E0 A1           LD      ($FF00+$A1),A       
6168: EA 67 C1        LD      ($C167),A           
616B: C9              RET                         
616C: AF              XOR     A                   
616D: EA 67 C1        LD      ($C167),A           
6170: F0 EF           LD      A,($EF)             
6172: E0 EC           LD      ($FF00+$EC),A       
6174: CD 49 64        CALL    $6449               ; {}
6177: CD BA 3D        CALL    $3DBA               
617A: CD 8C 64        CALL    $648C               ; {}
617D: 30 05           JR      NC,$6184            ; {}
617F: 3E 20           LD      A,$20               
6181: CD 8E 21        CALL    $218E               
6184: CD 84 65        CALL    $6584               ; {}
6187: 21 20 C3        LD      HL,$C320            
618A: 09              ADD     HL,BC               
618B: 35              DEC     (HL)                
618C: 35              DEC     (HL)                
618D: 21 10 C3        LD      HL,$C310            
6190: 09              ADD     HL,BC               
6191: 7E              LD      A,(HL)              
6192: A7              AND     A                   
6193: 28 04           JR      Z,$6199             ; {}
6195: E6 80           AND     $80                 
6197: 28 0E           JR      Z,$61A7             ; {}
6199: 70              LD      (HL),B              
619A: 21 20 C3        LD      HL,$C320            
619D: 09              ADD     HL,BC               
619E: 70              LD      (HL),B              
619F: F0 E7           LD      A,($E7)             
61A1: E6 1F           AND     $1F                 
61A3: 20 02           JR      NZ,$61A7            ; {}
61A5: 36 10           LD      (HL),$10            
61A7: C9              RET                         
61A8: 21 80 C3        LD      HL,$C380            
61AB: 09              ADD     HL,BC               
61AC: F0 F1           LD      A,($F1)             
61AE: B6              OR      (HL)                
61AF: E0 F1           LD      ($FF00+$F1),A       
61B1: 11 B1 60        LD      DE,$60B1            
61B4: CD 3B 3C        CALL    $3C3B               
61B7: CD DF 64        CALL    $64DF               ; {}
61BA: CD 6A 62        CALL    $626A               ; {}
61BD: CD 84 65        CALL    $6584               ; {}
61C0: 21 20 C3        LD      HL,$C320            
61C3: 09              ADD     HL,BC               
61C4: 35              DEC     (HL)                
61C5: 21 10 C3        LD      HL,$C310            
61C8: 09              ADD     HL,BC               
61C9: 7E              LD      A,(HL)              
61CA: E6 80           AND     $80                 
61CC: E0 E8           LD      ($FF00+$E8),A       
61CE: 28 07           JR      Z,$61D7             ; {}
61D0: AF              XOR     A                   
61D1: 77              LD      (HL),A              
61D2: 21 20 C3        LD      HL,$C320            
61D5: 09              ADD     HL,BC               
61D6: 77              LD      (HL),A              
61D7: F0 F0           LD      A,($F0)             
61D9: C7              RST     0X00                
61DA: DE 61           SBC     $61                 
61DC: 24              INC     H                   
61DD: 62              LD      H,D                 
61DE: CD 91 08        CALL    $0891               
61E1: 20 40           JR      NZ,$6223            ; {}
61E3: 36 80           LD      (HL),$80            
61E5: CD 8D 3B        CALL    $3B8D               
61E8: 3E 01           LD      A,$01               
61EA: CD 87 3B        CALL    $3B87               
61ED: 3E 71           LD      A,$71               
61EF: CD 01 3C        CALL    $3C01               
61F2: 38 2F           JR      C,$6223             ; {}
61F4: F0 D7           LD      A,($D7)             
61F6: 21 00 C2        LD      HL,$C200            
61F9: 19              ADD     HL,DE               
61FA: 77              LD      (HL),A              
61FB: F0 D8           LD      A,($D8)             
61FD: 21 10 C2        LD      HL,$C210            
6200: 19              ADD     HL,DE               
6201: 77              LD      (HL),A              
6202: 21 B0 C2        LD      HL,$C2B0            
6205: 19              ADD     HL,DE               
6206: 36 01           LD      (HL),$01            
6208: 21 20 C3        LD      HL,$C320            
620B: 19              ADD     HL,DE               
620C: 36 10           LD      (HL),$10            
620E: F0 EB           LD      A,($EB)             
6210: FE 71           CP      $71                 
6212: 3E 14           LD      A,$14               
6214: 28 02           JR      Z,$6218             ; {}
6216: 3E EC           LD      A,$EC               
6218: 21 40 C2        LD      HL,$C240            
621B: 19              ADD     HL,DE               
621C: 77              LD      (HL),A              
621D: 21 E0 C2        LD      HL,$C2E0            
6220: 19              ADD     HL,DE               
6221: 36 24           LD      (HL),$24            
6223: C9              RET                         
6224: CD 91 08        CALL    $0891               
6227: 20 07           JR      NZ,$6230            ; {}
6229: 36 60           LD      (HL),$60            
622B: CD 8D 3B        CALL    $3B8D               
622E: 70              LD      (HL),B              
622F: C9              RET                         
6230: FE 60           CP      $60                 
6232: 30 13           JR      NC,$6247            ; {}
6234: FE 40           CP      $40                 
6236: 30 0B           JR      NC,$6243            ; {}
6238: F0 E8           LD      A,($E8)             
623A: A7              AND     A                   
623B: 28 06           JR      Z,$6243             ; {}
623D: 21 20 C3        LD      HL,$C320            
6240: 09              ADD     HL,BC               
6241: 36 08           LD      (HL),$08            
6243: AF              XOR     A                   
6244: CD 87 3B        CALL    $3B87               
6247: C9              RET                         
6248: F0 F6           LD      A,($F6)             
624A: FE 92           CP      $92                 
624C: 20 08           JR      NZ,$6256            ; {}
624E: FA 0E DB        LD      A,($DB0E)           
6251: FE 07           CP      $07                 
6253: DA E5 65        JP      C,$65E5             ; {}
6256: 11 A1 60        LD      DE,$60A1            
6259: CD 3B 3C        CALL    $3C3B               
625C: CD DF 64        CALL    $64DF               ; {}
625F: F0 E7           LD      A,($E7)             
6261: 1F              RRA                         
6262: 1F              RRA                         
6263: 1F              RRA                         
6264: 1F              RRA                         
6265: E6 01           AND     $01                 
6267: CD 87 3B        CALL    $3B87               
626A: F0 EF           LD      A,($EF)             
626C: E0 EC           LD      ($FF00+$EC),A       
626E: CD 49 64        CALL    $6449               ; {}
6271: CD BA 3D        CALL    $3DBA               
6274: CD 8C 64        CALL    $648C               ; {}
6277: 30 64           JR      NC,$62DD            ; {}
6279: FA 74 DB        LD      A,($DB74)           
627C: A7              AND     A                   
627D: 28 05           JR      Z,$6284             ; {}
627F: 3E 23           LD      A,$23               
6281: C3 85 21        JP      $2185               
6284: FA 73 DB        LD      A,($DB73)           
6287: A7              AND     A                   
6288: 28 05           JR      Z,$628F             ; {}
628A: 3E 21           LD      A,$21               
628C: C3 85 21        JP      $2185               
628F: F0 F6           LD      A,($F6)             
6291: FE 92           CP      $92                 
6293: 20 0C           JR      NZ,$62A1            ; {}
6295: FA FD D8        LD      A,($D8FD)           
6298: E6 30           AND     $30                 
629A: 20 05           JR      NZ,$62A1            ; {}
629C: 3E 20           LD      A,$20               
629E: C3 85 21        JP      $2185               
62A1: FA 66 DB        LD      A,($DB66)           
62A4: E6 02           AND     $02                 
62A6: 28 12           JR      Z,$62BA             ; {}
62A8: FA BE DA        LD      A,($DABE)           
62AB: E6 10           AND     $10                 
62AD: 20 0B           JR      NZ,$62BA            ; {}
62AF: F0 F6           LD      A,($F6)             
62B1: FE 83           CP      $83                 
62B3: 20 05           JR      NZ,$62BA            ; {}
62B5: 3E 22           LD      A,$22               
62B7: C3 85 21        JP      $2185               
62BA: 21 7E DB        LD      HL,$DB7E            
62BD: 7E              LD      A,(HL)              
62BE: F5              PUSH    AF                  
62BF: 3C              INC     A                   
62C0: FE 04           CP      $04                 
62C2: 20 01           JR      NZ,$62C5            ; {}
62C4: AF              XOR     A                   
62C5: 77              LD      (HL),A              
62C6: FA 65 DB        LD      A,($DB65)           
62C9: E6 02           AND     $02                 
62CB: 20 06           JR      NZ,$62D3            ; {}
62CD: F1              POP     AF                  
62CE: C6 18           ADD     $18                 
62D0: C3 85 21        JP      $2185               
62D3: F1              POP     AF                  
62D4: F0 EB           LD      A,($EB)             
62D6: D6 70           SUB     $70                 
62D8: C6 1C           ADD     $1C                 
62DA: CD 85 21        CALL    $2185               
62DD: C9              RET                         
62DE: CD A3 63        CALL    $63A3               ; {}
62E1: CD DF 64        CALL    $64DF               ; {}
62E4: CD E2 08        CALL    $08E2               
62E7: CD EB 3B        CALL    $3BEB               
62EA: CD 49 64        CALL    $6449               ; {}
62ED: F0 F0           LD      A,($F0)             
62EF: C7              RST     0X00                
62F0: F6 62           OR      $62                 
62F2: FE 62           CP      $62                 
62F4: 12              LD      (DE),A              
62F5: 63              LD      H,E                 
62F6: CD 91 08        CALL    $0891               
62F9: 36 C0           LD      (HL),$C0            
62FB: C3 8D 3B        JP      $3B8D               
62FE: CD 91 08        CALL    $0891               
6301: 20 05           JR      NZ,$6308            ; {}
6303: 36 50           LD      (HL),$50            
6305: CD 8D 3B        CALL    $3B8D               
6308: 1F              RRA                         
6309: 1F              RRA                         
630A: 1F              RRA                         
630B: 1F              RRA                         
630C: E6 01           AND     $01                 
630E: CD 87 3B        CALL    $3B87               
6311: C9              RET                         
6312: CD 91 08        CALL    $0891               
6315: 20 04           JR      NZ,$631B            ; {}
6317: CD 8D 3B        CALL    $3B8D               
631A: 70              LD      (HL),B              
631B: FE 4A           CP      $4A                 
631D: 20 1E           JR      NZ,$633D            ; {}
631F: 3E 7D           LD      A,$7D               
6321: CD 01 3C        CALL    $3C01               
6324: 38 17           JR      C,$633D             ; {}
6326: F0 D7           LD      A,($D7)             
6328: 21 00 C2        LD      HL,$C200            
632B: 19              ADD     HL,DE               
632C: 77              LD      (HL),A              
632D: F0 D8           LD      A,($D8)             
632F: 21 10 C2        LD      HL,$C210            
6332: 19              ADD     HL,DE               
6333: 77              LD      (HL),A              
6334: C5              PUSH    BC                  
6335: D5              PUSH    DE                  
6336: C1              POP     BC                  
6337: 3E 0C           LD      A,$0C               
6339: CD 25 3C        CALL    $3C25               
633C: C1              POP     BC                  
633D: 3E 02           LD      A,$02               
633F: CD 87 3B        CALL    $3B87               
6342: C9              RET                         
6343: F8 F8           LD      HL,SP+$F8           
6345: 70              LD      (HL),B              
6346: 00              NOP                         
6347: F8 00           LD      HL,SP+$00           
6349: 72              LD      (HL),D              
634A: 00              NOP                         
634B: F8 08           LD      HL,SP+$08           
634D: 72              LD      (HL),D              
634E: 20 F8           JR      NZ,$6348            ; {}
6350: 10 70           ;;STOP    $70                 
6352: 20 08           JR      NZ,$635C            ; {}
6354: F8 74           LD      HL,SP+$74           
6356: 00              NOP                         
6357: 08 00 76        LD      ($7600),SP          ; {}
635A: 00              NOP                         
635B: 08 08 76        LD      ($7608),SP          ; {}
635E: 20 08           JR      NZ,$6368            ; {}
6360: 10 74           ;;STOP    $74                 
6362: 20 F9           JR      NZ,$635D            ; {}
6364: F9              LD      SP,HL               
6365: 70              LD      (HL),B              
6366: 00              NOP                         
6367: F9              LD      SP,HL               
6368: 01 72 00        LD      BC,$0072            
636B: F9              LD      SP,HL               
636C: 07              RLCA                        
636D: 72              LD      (HL),D              
636E: 20 F9           JR      NZ,$6369            ; {}
6370: 0F              RRCA                        
6371: 70              LD      (HL),B              
6372: 20 07           JR      NZ,$637B            ; {}
6374: F9              LD      SP,HL               
6375: 74              LD      (HL),H              
6376: 00              NOP                         
6377: 07              RLCA                        
6378: 01 76 00        LD      BC,$0076            
637B: 07              RLCA                        
637C: 07              RLCA                        
637D: 76              HALT                        
637E: 20 07           JR      NZ,$6387            ; {}
6380: 0F              RRCA                        
6381: 74              LD      (HL),H              
6382: 20 F8           JR      NZ,$637C            ; {}
6384: F8 78           LD      HL,SP+$78           
6386: 00              NOP                         
6387: F8 00           LD      HL,SP+$00           
6389: 7A              LD      A,D                 
638A: 00              NOP                         
638B: F8 08           LD      HL,SP+$08           
638D: 7A              LD      A,D                 
638E: 20 F8           JR      NZ,$6388            ; {}
6390: 10 78           ;;STOP    $78                 
6392: 20 08           JR      NZ,$639C            ; {}
6394: F8 7C           LD      HL,SP+$7C           
6396: 00              NOP                         
6397: 08 00 7E        LD      ($7E00),SP          ; {}
639A: 00              NOP                         
639B: 08 08 7E        LD      ($7E08),SP          ; {}
639E: 20 08           JR      NZ,$63A8            ; {}
63A0: 10 7C           ;;STOP    $7C                 
63A2: 20 F0           JR      NZ,$6394            ; {}
63A4: F1              POP     AF                  
63A5: 17              RLA                         
63A6: 17              RLA                         
63A7: 17              RLA                         
63A8: 17              RLA                         
63A9: 17              RLA                         
63AA: E6 E0           AND     $E0                 
63AC: 5F              LD      E,A                 
63AD: 50              LD      D,B                 
63AE: 21 43 63        LD      HL,$6343            
63B1: 19              ADD     HL,DE               
63B2: 0E 08           LD      C,$08               
63B4: CD 26 3D        CALL    $3D26               
63B7: 3E 08           LD      A,$08               
63B9: CD D0 3D        CALL    $3DD0               
63BC: C9              RET                         
63BD: 1E 00           LD      E,$00               
63BF: 1E 60           LD      E,$60               
63C1: 1E 40           LD      E,$40               
63C3: 1E 20           LD      E,$20               
63C5: 32              LD      (HLD),A             
63C6: 00              NOP                         
63C7: 32              LD      (HLD),A             
63C8: 20 30           JR      NZ,$63FA            ; {}
63CA: 00              NOP                         
63CB: 30 20           JR      NC,$63ED            ; {}
63CD: 21 60 C3        LD      HL,$C360            
63D0: 09              ADD     HL,BC               
63D1: 36 30           LD      (HL),$30            
63D3: 21 B0 C2        LD      HL,$C2B0            
63D6: 09              ADD     HL,BC               
63D7: 7E              LD      A,(HL)              
63D8: A7              AND     A                   
63D9: 28 08           JR      Z,$63E3             ; {}
63DB: F0 E7           LD      A,($E7)             
63DD: 17              RLA                         
63DE: 17              RLA                         
63DF: E6 10           AND     $10                 
63E1: E0 ED           LD      ($FF00+$ED),A       
63E3: 11 BD 63        LD      DE,$63BD            
63E6: CD 3B 3C        CALL    $3C3B               
63E9: CD 91 08        CALL    $0891               
63EC: 28 0E           JR      Z,$63FC             ; {}
63EE: 3D              DEC     A                   
63EF: CA E5 65        JP      Z,$65E5             ; {}
63F2: 1F              RRA                         
63F3: 1F              RRA                         
63F4: 1F              RRA                         
63F5: E6 01           AND     $01                 
63F7: C6 02           ADD     $02                 
63F9: C3 87 3B        JP      $3B87               
63FC: 21 10 C4        LD      HL,$C410            
63FF: 09              ADD     HL,BC               
6400: 7E              LD      A,(HL)              
6401: FE 02           CP      $02                 
6403: 38 06           JR      C,$640B             ; {}
6405: CD 91 08        CALL    $0891               
6408: 36 10           LD      (HL),$10            
640A: C9              RET                         
640B: 70              LD      (HL),B              
640C: CD DF 64        CALL    $64DF               ; {}
640F: F0 E7           LD      A,($E7)             
6411: 1F              RRA                         
6412: 1F              RRA                         
6413: 1F              RRA                         
6414: E6 01           AND     $01                 
6416: CD 87 3B        CALL    $3B87               
6419: CD B4 3B        CALL    $3BB4               
641C: CD 4B 65        CALL    $654B               ; {}
641F: C3 BC 5E        JP      $5EBC               ; {}
6422: 50              LD      D,B                 
6423: 00              NOP                         
6424: 50              LD      D,B                 
6425: 20 52           JR      NZ,$6479            ; {}
6427: 00              NOP                         
6428: 52              LD      D,D                 
6429: 20 11           JR      NZ,$643C            ; {}
642B: 22              LD      (HLI),A             
642C: 64              LD      H,H                 
642D: CD 3B 3C        CALL    $3C3B               
6430: CD DF 64        CALL    $64DF               ; {}
6433: CD E2 08        CALL    $08E2               
6436: CD EB 3B        CALL    $3BEB               
6439: CD 49 64        CALL    $6449               ; {}
643C: F0 E7           LD      A,($E7)             
643E: 58              LD      E,B                 
643F: E6 30           AND     $30                 
6441: 28 01           JR      Z,$6444             ; {}
6443: 1C              INC     E                   
6444: 7B              LD      A,E                 
6445: CD 87 3B        CALL    $3B87               
6448: C9              RET                         
6449: CD D5 3B        CALL    $3BD5               
644C: 30 1D           JR      NC,$646B            ; {}
644E: CD 4A 09        CALL    $094A               
6451: CD 42 09        CALL    $0942               
6454: FA A6 C1        LD      A,($C1A6)           
6457: A7              AND     A                   
6458: 28 11           JR      Z,$646B             ; {}
645A: 5F              LD      E,A                 
645B: 50              LD      D,B                 
645C: 21 9F C3        LD      HL,$C39F            
645F: 19              ADD     HL,DE               
6460: 7E              LD      A,(HL)              
6461: FE 03           CP      $03                 
6463: 20 06           JR      NZ,$646B            ; {}
6465: 21 8F C2        LD      HL,$C28F            
6468: 19              ADD     HL,DE               
6469: 36 00           LD      (HL),$00            
646B: C9              RET                         
646C: 06 04           LD      B,$04               
646E: 02              LD      (BC),A              
646F: 00              NOP                         
6470: 21 80 C3        LD      HL,$C380            
6473: 09              ADD     HL,BC               
6474: 5E              LD      E,(HL)              
6475: 50              LD      D,B                 
6476: 21 6C 64        LD      HL,$646C            
6479: 19              ADD     HL,DE               
647A: E5              PUSH    HL                  
647B: 21 D0 C3        LD      HL,$C3D0            
647E: 09              ADD     HL,BC               
647F: 34              INC     (HL)                
6480: 7E              LD      A,(HL)              
6481: 1F              RRA                         
6482: 1F              RRA                         
6483: 1F              RRA                         
6484: 1F              RRA                         
6485: E1              POP     HL                  
6486: E6 01           AND     $01                 
6488: B6              OR      (HL)                
6489: C3 87 3B        JP      $3B87               
648C: 58              LD      E,B                 
648D: F0 99           LD      A,($99)             
648F: 21 EF FF        LD      HL,$FFEF            
6492: 96              SUB     (HL)                
6493: C6 14           ADD     $14                 
6495: FE 28           CP      $28                 
6497: 30 44           JR      NC,$64DD            ; {}
6499: F0 98           LD      A,($98)             
649B: 21 EE FF        LD      HL,$FFEE            
649E: 96              SUB     (HL)                
649F: C6 10           ADD     $10                 
64A1: FE 20           CP      $20                 
64A3: 30 38           JR      NC,$64DD            ; {}
64A5: 1C              INC     E                   
64A6: F0 EB           LD      A,($EB)             
64A8: FE 78           CP      $78                 
64AA: 28 0C           JR      Z,$64B8             ; {}
64AC: D5              PUSH    DE                  
64AD: CD BE 65        CALL    $65BE               ; {}
64B0: F0 9E           LD      A,($9E)             
64B2: EE 01           XOR     $01                 
64B4: BB              CP      E                   
64B5: D1              POP     DE                  
64B6: 20 25           JR      NZ,$64DD            ; {}
64B8: 21 AD C1        LD      HL,$C1AD            
64BB: 36 01           LD      (HL),$01            
64BD: FA 9F C1        LD      A,($C19F)           
64C0: 21 4F C1        LD      HL,$C14F            
64C3: B6              OR      (HL)                
64C4: 21 46 C1        LD      HL,$C146            
64C7: B6              OR      (HL)                
64C8: 21 34 C1        LD      HL,$C134            
64CB: B6              OR      (HL)                
64CC: 20 0F           JR      NZ,$64DD            ; {}
64CE: FA 9A DB        LD      A,($DB9A)           
64D1: FE 80           CP      $80                 
64D3: 20 08           JR      NZ,$64DD            ; {}
64D5: F0 CC           LD      A,($CC)             
64D7: E6 10           AND     $10                 
64D9: 28 02           JR      Z,$64DD             ; {}
64DB: 37              SCF                         
64DC: C9              RET                         
64DD: A7              AND     A                   
64DE: C9              RET                         
64DF: F0 EA           LD      A,($EA)             
64E1: FE 05           CP      $05                 
64E3: 20 1A           JR      NZ,$64FF            ; {}
64E5: FA 95 DB        LD      A,($DB95)           
64E8: FE 07           CP      $07                 
64EA: 28 13           JR      Z,$64FF             ; {}
64EC: 21 A8 C1        LD      HL,$C1A8            
64EF: FA 9F C1        LD      A,($C19F)           
64F2: B6              OR      (HL)                
64F3: 21 4F C1        LD      HL,$C14F            
64F6: B6              OR      (HL)                
64F7: 20 06           JR      NZ,$64FF            ; {}
64F9: FA 24 C1        LD      A,($C124)           
64FC: A7              AND     A                   
64FD: 28 01           JR      Z,$6500             ; {}
64FF: F1              POP     AF                  
6500: C9              RET                         
6501: 21 10 C4        LD      HL,$C410            
6504: 09              ADD     HL,BC               
6505: 7E              LD      A,(HL)              
6506: A7              AND     A                   
6507: 28 41           JR      Z,$654A             ; {}
6509: 3D              DEC     A                   
650A: 77              LD      (HL),A              
650B: CD B8 3E        CALL    $3EB8               
650E: 21 40 C2        LD      HL,$C240            
6511: 09              ADD     HL,BC               
6512: 7E              LD      A,(HL)              
6513: F5              PUSH    AF                  
6514: 21 50 C2        LD      HL,$C250            
6517: 09              ADD     HL,BC               
6518: 7E              LD      A,(HL)              
6519: F5              PUSH    AF                  
651A: 21 F0 C3        LD      HL,$C3F0            
651D: 09              ADD     HL,BC               
651E: 7E              LD      A,(HL)              
651F: 21 40 C2        LD      HL,$C240            
6522: 09              ADD     HL,BC               
6523: 77              LD      (HL),A              
6524: 21 00 C4        LD      HL,$C400            
6527: 09              ADD     HL,BC               
6528: 7E              LD      A,(HL)              
6529: 21 50 C2        LD      HL,$C250            
652C: 09              ADD     HL,BC               
652D: 77              LD      (HL),A              
652E: CD 4B 65        CALL    $654B               ; {}
6531: 21 30 C4        LD      HL,$C430            
6534: 09              ADD     HL,BC               
6535: 7E              LD      A,(HL)              
6536: E6 20           AND     $20                 
6538: 20 03           JR      NZ,$653D            ; {}
653A: CD 9E 3B        CALL    $3B9E               
653D: 21 50 C2        LD      HL,$C250            
6540: 09              ADD     HL,BC               
6541: F1              POP     AF                  
6542: 77              LD      (HL),A              
6543: 21 40 C2        LD      HL,$C240            
6546: 09              ADD     HL,BC               
6547: F1              POP     AF                  
6548: 77              LD      (HL),A              
6549: F1              POP     AF                  
654A: C9              RET                         
654B: CD 58 65        CALL    $6558               ; {}
654E: C5              PUSH    BC                  
654F: 79              LD      A,C                 
6550: C6 10           ADD     $10                 
6552: 4F              LD      C,A                 
6553: CD 58 65        CALL    $6558               ; {}
6556: C1              POP     BC                  
6557: C9              RET                         
6558: 21 40 C2        LD      HL,$C240            
655B: 09              ADD     HL,BC               
655C: 7E              LD      A,(HL)              
655D: A7              AND     A                   
655E: 28 23           JR      Z,$6583             ; {}
6560: F5              PUSH    AF                  
6561: CB 37           SWAP    1,E                 
6563: E6 F0           AND     $F0                 
6565: 21 60 C2        LD      HL,$C260            
6568: 09              ADD     HL,BC               
6569: 86              ADD     A,(HL)              
656A: 77              LD      (HL),A              
656B: CB 12           RL      1,E                 
656D: 21 00 C2        LD      HL,$C200            
6570: 09              ADD     HL,BC               
6571: F1              POP     AF                  
6572: 1E 00           LD      E,$00               
6574: CB 7F           BIT     1,E                 
6576: 28 02           JR      Z,$657A             ; {}
6578: 1E F0           LD      E,$F0               
657A: CB 37           SWAP    1,E                 
657C: E6 0F           AND     $0F                 
657E: B3              OR      E                   
657F: CB 1A           RR      1,E                 
6581: 8E              ADC     A,(HL)              
6582: 77              LD      (HL),A              
6583: C9              RET                         
6584: 21 20 C3        LD      HL,$C320            
6587: 09              ADD     HL,BC               
6588: 7E              LD      A,(HL)              
6589: A7              AND     A                   
658A: 28 F7           JR      Z,$6583             ; {}
658C: F5              PUSH    AF                  
658D: CB 37           SWAP    1,E                 
658F: E6 F0           AND     $F0                 
6591: 21 30 C3        LD      HL,$C330            
6594: 09              ADD     HL,BC               
6595: 86              ADD     A,(HL)              
6596: 77              LD      (HL),A              
6597: CB 12           RL      1,E                 
6599: 21 10 C3        LD      HL,$C310            
659C: 18 D2           JR      $6570               ; {}
659E: 1E 00           LD      E,$00               
65A0: F0 98           LD      A,($98)             
65A2: 21 00 C2        LD      HL,$C200            
65A5: 09              ADD     HL,BC               
65A6: 96              SUB     (HL)                
65A7: CB 7F           BIT     1,E                 
65A9: 28 01           JR      Z,$65AC             ; {}
65AB: 1C              INC     E                   
65AC: 57              LD      D,A                 
65AD: C9              RET                         
65AE: 1E 02           LD      E,$02               
65B0: F0 99           LD      A,($99)             
65B2: 21 10 C2        LD      HL,$C210            
65B5: 09              ADD     HL,BC               
65B6: 96              SUB     (HL)                
65B7: CB 7F           BIT     1,E                 
65B9: 20 01           JR      NZ,$65BC            ; {}
65BB: 1C              INC     E                   
65BC: 57              LD      D,A                 
65BD: C9              RET                         
65BE: CD 9E 65        CALL    $659E               ; {}
65C1: 7B              LD      A,E                 
65C2: E0 D7           LD      ($FF00+$D7),A       
65C4: 7A              LD      A,D                 
65C5: CB 7F           BIT     1,E                 
65C7: 28 02           JR      Z,$65CB             ; {}
65C9: 2F              CPL                         
65CA: 3C              INC     A                   
65CB: F5              PUSH    AF                  
65CC: CD AE 65        CALL    $65AE               ; {}
65CF: 7B              LD      A,E                 
65D0: E0 D8           LD      ($FF00+$D8),A       
65D2: 7A              LD      A,D                 
65D3: CB 7F           BIT     1,E                 
65D5: 28 02           JR      Z,$65D9             ; {}
65D7: 2F              CPL                         
65D8: 3C              INC     A                   
65D9: D1              POP     DE                  
65DA: BA              CP      D                   
65DB: 30 04           JR      NC,$65E1            ; {}
65DD: F0 D7           LD      A,($D7)             
65DF: 18 02           JR      $65E3               ; {}
65E1: F0 D8           LD      A,($D8)             
65E3: 5F              LD      E,A                 
65E4: C9              RET                         
65E5: 21 80 C2        LD      HL,$C280            
65E8: 09              ADD     HL,BC               
65E9: 70              LD      (HL),B              
65EA: C9              RET                         
65EB: 6A              LD      L,D                 
65EC: 20 68           JR      NZ,$6656            ; {}
65EE: 20 68           JR      NZ,$6658            ; {}
65F0: 00              NOP                         
65F1: 6A              LD      L,D                 
65F2: 00              NOP                         
65F3: 6C              LD      L,H                 
65F4: 40              LD      B,B                 
65F5: 6C              LD      L,H                 
65F6: 60              LD      H,B                 
65F7: 6C              LD      L,H                 
65F8: 00              NOP                         
65F9: 6C              LD      L,H                 
65FA: 20 F0           JR      NZ,$65EC            ; {}
65FC: E7              RST     0X20                
65FD: 17              RLA                         
65FE: 17              RLA                         
65FF: E6 10           AND     $10                 
6601: E0 ED           LD      ($FF00+$ED),A       
6603: 11 EB 65        LD      DE,$65EB            
6606: CD 3B 3C        CALL    $3C3B               
6609: CD DF 64        CALL    $64DF               ; {}
660C: CD CA 3B        CALL    $3BCA               
660F: CD 4B 65        CALL    $654B               ; {}
6612: CD A9 3B        CALL    $3BA9               
6615: 21 A0 C2        LD      HL,$C2A0            
6618: 09              ADD     HL,BC               
6619: 7E              LD      A,(HL)              
661A: A7              AND     A                   
661B: 28 03           JR      Z,$6620             ; {}
661D: CD E5 65        CALL    $65E5               ; {}
6620: C9              RET                         
6621: 5C              LD      E,H                 
6622: 00              NOP                         
6623: 5C              LD      E,H                 
6624: 20 5C           JR      NZ,$6682            ; {}
6626: 10 5C           ;;STOP    $5C                 
6628: 30 00           JR      NC,$662A            ; {}
662A: 10 00           ;;STOP    $00                 
662C: F0 00           LD      A,($00)             
662E: F0 00           LD      A,($00)             
6630: 10 10           ;;STOP    $10                 
6632: 00              NOP                         
6633: F0 00           LD      A,($00)             
6635: 10 00           ;;STOP    $00                 
6637: F0 00           LD      A,($00)             
6639: 01 08 02        LD      BC,$0208            
663C: 04              INC     B                   
663D: 01 04 02        LD      BC,$0204            
6640: 08 3E 01        LD      ($013E),SP          
6643: E0 BE           LD      ($FF00+$BE),A       
6645: F0 E7           LD      A,($E7)             
6647: 1F              RRA                         
6648: E6 01           AND     $01                 
664A: E0 F1           LD      ($FF00+$F1),A       
664C: 11 21 66        LD      DE,$6621            
664F: CD 3B 3C        CALL    $3C3B               
6652: CD DF 64        CALL    $64DF               ; {}
6655: CD 01 65        CALL    $6501               ; {}
6658: CD BF 3B        CALL    $3BBF               
665B: CD 4B 65        CALL    $654B               ; {}
665E: CD D8 66        CALL    $66D8               ; {}
6661: 21 B0 C2        LD      HL,$C2B0            
6664: 09              ADD     HL,BC               
6665: 7E              LD      A,(HL)              
6666: 5F              LD      E,A                 
6667: 50              LD      D,B                 
6668: 21 C0 C2        LD      HL,$C2C0            
666B: 09              ADD     HL,BC               
666C: 86              ADD     A,(HL)              
666D: 5F              LD      E,A                 
666E: 21 39 66        LD      HL,$6639            
6671: 19              ADD     HL,DE               
6672: E5              PUSH    HL                  
6673: 21 A0 C2        LD      HL,$C2A0            
6676: 09              ADD     HL,BC               
6677: 7E              LD      A,(HL)              
6678: E1              POP     HL                  
6679: A6              AND     (HL)                
667A: 20 15           JR      NZ,$6691            ; {}
667C: CD 91 08        CALL    $0891               
667F: 20 1B           JR      NZ,$669C            ; {}
6681: 21 A0 C2        LD      HL,$C2A0            
6684: 09              ADD     HL,BC               
6685: 7E              LD      A,(HL)              
6686: E6 0F           AND     $0F                 
6688: 20 1F           JR      NZ,$66A9            ; {}
668A: CD 91 08        CALL    $0891               
668D: 36 09           LD      (HL),$09            
668F: 18 18           JR      $66A9               ; {}
6691: 21 B0 C2        LD      HL,$C2B0            
6694: 09              ADD     HL,BC               
6695: 34              INC     (HL)                
6696: 7E              LD      A,(HL)              
6697: E6 03           AND     $03                 
6699: 77              LD      (HL),A              
669A: 18 0D           JR      $66A9               ; {}
669C: FE 06           CP      $06                 
669E: 20 09           JR      NZ,$66A9            ; {}
66A0: 21 B0 C2        LD      HL,$C2B0            
66A3: 09              ADD     HL,BC               
66A4: 35              DEC     (HL)                
66A5: 7E              LD      A,(HL)              
66A6: E6 03           AND     $03                 
66A8: 77              LD      (HL),A              
66A9: 21 B0 C2        LD      HL,$C2B0            
66AC: 09              ADD     HL,BC               
66AD: 7E              LD      A,(HL)              
66AE: 5F              LD      E,A                 
66AF: 50              LD      D,B                 
66B0: 21 C0 C2        LD      HL,$C2C0            
66B3: 09              ADD     HL,BC               
66B4: 86              ADD     A,(HL)              
66B5: 5F              LD      E,A                 
66B6: 21 29 66        LD      HL,$6629            
66B9: 19              ADD     HL,DE               
66BA: 7E              LD      A,(HL)              
66BB: 21 50 C2        LD      HL,$C250            
66BE: 09              ADD     HL,BC               
66BF: 77              LD      (HL),A              
66C0: 21 B0 C2        LD      HL,$C2B0            
66C3: 09              ADD     HL,BC               
66C4: 7E              LD      A,(HL)              
66C5: 5F              LD      E,A                 
66C6: 50              LD      D,B                 
66C7: 21 C0 C2        LD      HL,$C2C0            
66CA: 09              ADD     HL,BC               
66CB: 86              ADD     A,(HL)              
66CC: 5F              LD      E,A                 
66CD: 21 31 66        LD      HL,$6631            
66D0: 19              ADD     HL,DE               
66D1: 7E              LD      A,(HL)              
66D2: 21 40 C2        LD      HL,$C240            
66D5: 09              ADD     HL,BC               
66D6: 77              LD      (HL),A              
66D7: C9              RET                         
66D8: 21 40 C2        LD      HL,$C240            
66DB: 09              ADD     HL,BC               
66DC: 7E              LD      A,(HL)              
66DD: F5              PUSH    AF                  
66DE: 36 01           LD      (HL),$01            
66E0: 21 50 C2        LD      HL,$C250            
66E3: 09              ADD     HL,BC               
66E4: 7E              LD      A,(HL)              
66E5: F5              PUSH    AF                  
66E6: 36 01           LD      (HL),$01            
66E8: CD 9E 3B        CALL    $3B9E               
66EB: 21 A0 C2        LD      HL,$C2A0            
66EE: 09              ADD     HL,BC               
66EF: 7E              LD      A,(HL)              
66F0: F5              PUSH    AF                  
66F1: 21 40 C2        LD      HL,$C240            
66F4: 09              ADD     HL,BC               
66F5: 36 FF           LD      (HL),$FF            
66F7: 21 50 C2        LD      HL,$C250            
66FA: 09              ADD     HL,BC               
66FB: 36 FF           LD      (HL),$FF            
66FD: CD 9E 3B        CALL    $3B9E               
6700: 21 A0 C2        LD      HL,$C2A0            
6703: 09              ADD     HL,BC               
6704: F1              POP     AF                  
6705: B6              OR      (HL)                
6706: 77              LD      (HL),A              
6707: F1              POP     AF                  
6708: 21 50 C2        LD      HL,$C250            
670B: 09              ADD     HL,BC               
670C: 77              LD      (HL),A              
670D: F1              POP     AF                  
670E: 21 40 C2        LD      HL,$C240            
6711: 09              ADD     HL,BC               
6712: 77              LD      (HL),A              
6713: C9              RET                         
6714: 42              LD      B,D                 
6715: 00              NOP                         
6716: 42              LD      B,D                 
6717: 20 40           JR      NZ,$6759            ; {}
6719: 00              NOP                         
671A: 40              LD      B,B                 
671B: 20 62           JR      NZ,$677F            ; {}
671D: 00              NOP                         
671E: 62              LD      H,D                 
671F: 20 60           JR      NZ,$6781            ; {}
6721: 00              NOP                         
6722: 60              LD      H,B                 
6723: 20 00           JR      NZ,$6725            ; {}
6725: 05              DEC     B                   
6726: 0A              LD      A,(BC)              
6727: 0D              DEC     C                   
6728: 0E 0D           LD      C,$0D               
672A: 0A              LD      A,(BC)              
672B: 05              DEC     B                   
672C: 00              NOP                         
672D: FB              EI                          
672E: F6 F3           OR      $F3                 
6730: F2                              
6731: F3              DI                          
6732: F6 FB           OR      $FB                 
6734: 00              NOP                         
6735: 05              DEC     B                   
6736: 0A              LD      A,(BC)              
6737: 0D              DEC     C                   
6738: 0C              INC     C                   
6739: 04              INC     B                   
673A: 08 00 11        LD      ($1100),SP          
673D: 14              INC     D                   
673E: 67              LD      H,A                 
673F: F0 F7           LD      A,($F7)             
6741: FE 0A           CP      $0A                 
6743: 20 03           JR      NZ,$6748            ; {}
6745: 11 1C 67        LD      DE,$671C            
6748: CD 3B 3C        CALL    $3C3B               
674B: CD DF 64        CALL    $64DF               ; {}
674E: CD 01 65        CALL    $6501               ; {}
6751: CD B4 3B        CALL    $3BB4               
6754: F0 F0           LD      A,($F0)             
6756: C7              RST     0X00                
6757: 5B              LD      E,E                 
6758: 67              LD      H,A                 
6759: 9B              SBC     E                   
675A: 67              LD      H,A                 
675B: CD 91 08        CALL    $0891               
675E: C2 F2 67        JP      NZ,$67F2            ; {}
6761: CD 9E 65        CALL    $659E               ; {}
6764: C6 20           ADD     $20                 
6766: FE 40           CP      $40                 
6768: D2 F2 67        JP      NC,$67F2            ; {}
676B: CD AE 65        CALL    $65AE               ; {}
676E: C6 20           ADD     $20                 
6770: FE 40           CP      $40                 
6772: D2 F2 67        JP      NC,$67F2            ; {}
6775: CD BE 65        CALL    $65BE               ; {}
6778: 16 00           LD      D,$00               
677A: 21 38 67        LD      HL,$6738            
677D: 19              ADD     HL,DE               
677E: 7E              LD      A,(HL)              
677F: 21 B0 C2        LD      HL,$C2B0            
6782: 09              ADD     HL,BC               
6783: 77              LD      (HL),A              
6784: CD 91 08        CALL    $0891               
6787: CD ED 27        CALL    $27ED               
678A: E6 3F           AND     $3F                 
678C: C6 50           ADD     $50                 
678E: 77              LD      (HL),A              
678F: 21 C0 C2        LD      HL,$C2C0            
6792: 09              ADD     HL,BC               
6793: 36 01           LD      (HL),$01            
6795: CD 8D 3B        CALL    $3B8D               
6798: C3 F2 67        JP      $67F2               ; {}
679B: CD 4B 65        CALL    $654B               ; {}
679E: CD 9E 3B        CALL    $3B9E               
67A1: CD 91 08        CALL    $0891               
67A4: 20 08           JR      NZ,$67AE            ; {}
67A6: 36 20           LD      (HL),$20            
67A8: CD 8D 3B        CALL    $3B8D               
67AB: 70              LD      (HL),B              
67AC: 18 44           JR      $67F2               ; {}
67AE: 21 D0 C2        LD      HL,$C2D0            
67B1: 09              ADD     HL,BC               
67B2: 34              INC     (HL)                
67B3: 7E              LD      A,(HL)              
67B4: FE 0A           CP      $0A                 
67B6: 38 3A           JR      C,$67F2             ; {}
67B8: 70              LD      (HL),B              
67B9: 21 C0 C2        LD      HL,$C2C0            
67BC: 09              ADD     HL,BC               
67BD: 7E              LD      A,(HL)              
67BE: 21 B0 C2        LD      HL,$C2B0            
67C1: 09              ADD     HL,BC               
67C2: 86              ADD     A,(HL)              
67C3: E6 0F           AND     $0F                 
67C5: 77              LD      (HL),A              
67C6: 21 B0 C2        LD      HL,$C2B0            
67C9: 09              ADD     HL,BC               
67CA: 5E              LD      E,(HL)              
67CB: 50              LD      D,B                 
67CC: 21 24 67        LD      HL,$6724            
67CF: 19              ADD     HL,DE               
67D0: 7E              LD      A,(HL)              
67D1: 21 50 C2        LD      HL,$C250            
67D4: 09              ADD     HL,BC               
67D5: 77              LD      (HL),A              
67D6: 21 28 67        LD      HL,$6728            
67D9: 19              ADD     HL,DE               
67DA: 7E              LD      A,(HL)              
67DB: 21 40 C2        LD      HL,$C240            
67DE: 09              ADD     HL,BC               
67DF: 77              LD      (HL),A              
67E0: CD ED 27        CALL    $27ED               
67E3: E6 1F           AND     $1F                 
67E5: 20 0B           JR      NZ,$67F2            ; {}
67E7: CD ED 27        CALL    $27ED               
67EA: E6 02           AND     $02                 
67EC: 3D              DEC     A                   
67ED: 21 C0 C2        LD      HL,$C2C0            
67F0: 09              ADD     HL,BC               
67F1: 77              LD      (HL),A              
67F2: F0 F0           LD      A,($F0)             
67F4: A7              AND     A                   
67F5: 28 07           JR      Z,$67FE             ; {}
67F7: F0 E7           LD      A,($E7)             
67F9: 1F              RRA                         
67FA: 1F              RRA                         
67FB: 1F              RRA                         
67FC: E6 01           AND     $01                 
67FE: C3 87 3B        JP      $3B87               
6801: 79              LD      A,C                 
6802: EA 01 C5        LD      ($C501),A           
6805: F0 F6           LD      A,($F6)             
6807: FE 64           CP      $64                 
6809: 20 0E           JR      NZ,$6819            ; {}
680B: FA E3 D9        LD      A,($D9E3)           
680E: E6 40           AND     $40                 
6810: C8              RET     Z                   
6811: FA 69 DB        LD      A,($DB69)           
6814: E6 02           AND     $02                 
6816: C2 E5 65        JP      NZ,$65E5            ; {}
6819: F0 F6           LD      A,($F6)             
681B: FE AC           CP      $AC                 
681D: 20 07           JR      NZ,$6826            ; {}
681F: F0 F8           LD      A,($F8)             
6821: E6 10           AND     $10                 
6823: CA E5 65        JP      Z,$65E5             ; {}
6826: F0 F6           LD      A,($F6)             
6828: FE 41           CP      $41                 
682A: 20 09           JR      NZ,$6835            ; {}
682C: FA 11 DB        LD      A,($DB11)           
682F: A7              AND     A                   
6830: C8              RET     Z                   
6831: CD 8C 08        CALL    $088C               
6834: C0              RET     NZ                  
6835: F0 F6           LD      A,($F6)             
6837: FE EE           CP      $EE                 
6839: 20 06           JR      NZ,$6841            ; {}
683B: FA 12 DB        LD      A,($DB12)           
683E: A7              AND     A                   
683F: 18 68           JR      $68A9               ; {}
6841: F0 F6           LD      A,($F6)             
6843: FE D2           CP      $D2                 
6845: 28 13           JR      Z,$685A             ; {}
6847: FE 36           CP      $36                 
6849: 20 14           JR      NZ,$685F            ; {}
684B: FA 66 DB        LD      A,($DB66)           
684E: A7              AND     A                   
684F: C2 E5 65        JP      NZ,$65E5            ; {}
6852: FA 56 DB        LD      A,($DB56)           
6855: FE 01           CP      $01                 
6857: C2 E5 65        JP      NZ,$65E5            ; {}
685A: FA 65 DB        LD      A,($DB65)           
685D: 18 48           JR      $68A7               ; {}
685F: F0 F6           LD      A,($F6)             
6861: FE 08           CP      $08                 
6863: 20 10           JR      NZ,$6875            ; {}
6865: FA 6C DB        LD      A,($DB6C)           
6868: E6 02           AND     $02                 
686A: C2 E5 65        JP      NZ,$65E5            ; {}
686D: FA 08 D8        LD      A,($D808)           
6870: E6 10           AND     $10                 
6872: C8              RET     Z                   
6873: 18 37           JR      $68AC               ; {}
6875: FE 9D           CP      $9D                 
6877: 20 05           JR      NZ,$687E            ; {}
6879: FA 69 DB        LD      A,($DB69)           
687C: 18 29           JR      $68A7               ; {}
687E: FE 06           CP      $06                 
6880: 20 08           JR      NZ,$688A            ; {}
6882: FA 06 D8        LD      A,($D806)           
6885: E6 10           AND     $10                 
6887: C8              RET     Z                   
6888: 18 22           JR      $68AC               ; {}
688A: FE B6           CP      $B6                 
688C: 20 05           JR      NZ,$6893            ; {}
688E: FA 67 DB        LD      A,($DB67)           
6891: 18 14           JR      $68A7               ; {}
6893: FE 17           CP      $17                 
6895: 28 04           JR      Z,$689B             ; {}
6897: FE 9C           CP      $9C                 
6899: 20 05           JR      NZ,$68A0            ; {}
689B: FA 6A DB        LD      A,($DB6A)           
689E: 18 07           JR      $68A7               ; {}
68A0: FE 16           CP      $16                 
68A2: 20 08           JR      NZ,$68AC            ; {}
68A4: FA 66 DB        LD      A,($DB66)           
68A7: E6 02           AND     $02                 
68A9: CA E5 65        JP      Z,$65E5             ; {}
68AC: F0 F6           LD      A,($F6)             
68AE: FE D2           CP      $D2                 
68B0: 28 0E           JR      Z,$68C0             ; {}
68B2: FE 16           CP      $16                 
68B4: 28 0A           JR      Z,$68C0             ; {}
68B6: FE 36           CP      $36                 
68B8: 28 06           JR      Z,$68C0             ; {}
68BA: F0 F0           LD      A,($F0)             
68BC: FE 00           CP      $00                 
68BE: 28 03           JR      Z,$68C3             ; {}
68C0: CD 5A 6A        CALL    $6A5A               ; {}
68C3: F0 E7           LD      A,($E7)             
68C5: E6 B0           AND     $B0                 
68C7: 3E 00           LD      A,$00               
68C9: 20 01           JR      NZ,$68CC            ; {}
68CB: 3C              INC     A                   
68CC: CD 87 3B        CALL    $3B87               
68CF: FA 24 C1        LD      A,($C124)           
68D2: A7              AND     A                   
68D3: C0              RET     NZ                  
68D4: F0 F0           LD      A,($F0)             
68D6: C7              RST     0X00                
68D7: E1              POP     HL                  
68D8: 68              LD      L,B                 
68D9: 3C              INC     A                   
68DA: 69              LD      L,C                 
68DB: 82              ADD     A,D                 
68DC: 69              LD      L,C                 
68DD: B1              OR      C                   
68DE: 69              LD      L,C                 
68DF: DB                              
68E0: 69              LD      L,C                 
68E1: F0 F6           LD      A,($F6)             
68E3: FE F2           CP      $F2                 
68E5: 20 14           JR      NZ,$68FB            ; {}
68E7: 3E 1D           LD      A,$1D               
68E9: E0 B0           LD      ($FF00+$B0),A       
68EB: F0 99           LD      A,($99)             
68ED: FE 44           CP      $44                 
68EF: D8              RET     C                   
68F0: F0 98           LD      A,($98)             
68F2: D6 58           SUB     $58                 
68F4: C6 18           ADD     $18                 
68F6: FE 30           CP      $30                 
68F8: D0              RET     NC                  
68F9: 18 07           JR      $6902               ; {}
68FB: FA 4E DB        LD      A,($DB4E)           
68FE: A7              AND     A                   
68FF: CA E5 65        JP      Z,$65E5             ; {}
6902: F0 B0           LD      A,($B0)             
6904: 21 B0 C2        LD      HL,$C2B0            
6907: 09              ADD     HL,BC               
6908: 77              LD      (HL),A              
6909: 3E 22           LD      A,$22               
690B: EA 68 D3        LD      ($D368),A           
690E: E0 B0           LD      ($FF00+$B0),A       
6910: E0 BD           LD      ($FF00+$BD),A       
6912: F0 F6           LD      A,($F6)             
6914: FE 16           CP      $16                 
6916: 28 08           JR      Z,$6920             ; {}
6918: FE 36           CP      $36                 
691A: 28 04           JR      Z,$6920             ; {}
691C: FE D2           CP      $D2                 
691E: 20 06           JR      NZ,$6926            ; {}
6920: CD 8D 3B        CALL    $3B8D               
6923: 36 02           LD      (HL),$02            
6925: C9              RET                         
6926: 21 10 C3        LD      HL,$C310            
6929: 09              ADD     HL,BC               
692A: 36 20           LD      (HL),$20            
692C: 21 40 C2        LD      HL,$C240            
692F: 09              ADD     HL,BC               
6930: 36 18           LD      (HL),$18            
6932: 21 50 C2        LD      HL,$C250            
6935: 09              ADD     HL,BC               
6936: 36 10           LD      (HL),$10            
6938: CD 8D 3B        CALL    $3B8D               
693B: C9              RET                         
693C: CD BE 65        CALL    $65BE               ; {}
693F: 7B              LD      A,E                 
6940: EE 01           XOR     $01                 
6942: E0 9E           LD      ($FF00+$9E),A       
6944: 3E 02           LD      A,$02               
6946: E0 A1           LD      ($FF00+$A1),A       
6948: 3E 05           LD      A,$05               
694A: EA 11 C1        LD      ($C111),A           
694D: CD CD 69        CALL    $69CD               ; {}
6950: CD 4B 65        CALL    $654B               ; {}
6953: 21 10 C3        LD      HL,$C310            
6956: 09              ADD     HL,BC               
6957: 7E              LD      A,(HL)              
6958: A7              AND     A                   
6959: 20 04           JR      NZ,$695F            ; {}
695B: CD 8D 3B        CALL    $3B8D               
695E: C9              RET                         
695F: 21 20 C3        LD      HL,$C320            
6962: 09              ADD     HL,BC               
6963: 36 FC           LD      (HL),$FC            
6965: CD 84 65        CALL    $6584               ; {}
6968: CD C5 29        CALL    $29C5               
696B: F0 E7           LD      A,($E7)             
696D: E6 03           AND     $03                 
696F: 20 10           JR      NZ,$6981            ; {}
6971: 3E 00           LD      A,$00               
6973: 21 50 C2        LD      HL,$C250            
6976: CD 36 6A        CALL    $6A36               ; {}
6979: 3E 00           LD      A,$00               
697B: 21 40 C2        LD      HL,$C240            
697E: CD 36 6A        CALL    $6A36               ; {}
6981: C9              RET                         
6982: CD DF 64        CALL    $64DF               ; {}
6985: CD 49 64        CALL    $6449               ; {}
6988: FA 6B C1        LD      A,($C16B)           
698B: FE 04           CP      $04                 
698D: C0              RET     NZ                  
698E: FA 7B C1        LD      A,($C17B)           
6991: A7              AND     A                   
6992: C0              RET     NZ                  
6993: F0 F6           LD      A,($F6)             
6995: FE 06           CP      $06                 
6997: 20 07           JR      NZ,$69A0            ; {}
6999: 3E CD           LD      A,$CD               
699B: CD 97 21        CALL    $2197               
699E: 18 03           JR      $69A3               ; {}
69A0: CD D0 29        CALL    $29D0               
69A3: 3E 19           LD      A,$19               
69A5: EA AB C5        LD      ($C5AB),A           
69A8: CD 8D 3B        CALL    $3B8D               
69AB: CD 91 08        CALL    $0891               
69AE: 36 10           LD      (HL),$10            
69B0: C9              RET                         
69B1: CD DF 64        CALL    $64DF               ; {}
69B4: F0 F6           LD      A,($F6)             
69B6: FE 06           CP      $06                 
69B8: 28 08           JR      Z,$69C2             ; {}
69BA: CD 91 08        CALL    $0891               
69BD: 20 0E           JR      NZ,$69CD            ; {}
69BF: CD 8D 3B        CALL    $3B8D               
69C2: F0 F6           LD      A,($F6)             
69C4: 5F              LD      E,A                 
69C5: 50              LD      D,B                 
69C6: 21 00 D8        LD      HL,$D800            
69C9: 19              ADD     HL,DE               
69CA: CB EE           SET     1,E                 
69CC: C9              RET                         
69CD: 3E 02           LD      A,$02               
69CF: E0 A1           LD      ($FF00+$A1),A       
69D1: F0 E7           LD      A,($E7)             
69D3: 1F              RRA                         
69D4: 1F              RRA                         
69D5: E6 02           AND     $02                 
69D7: CD 87 3B        CALL    $3B87               
69DA: C9              RET                         
69DB: CD DF 64        CALL    $64DF               ; {}
69DE: CD CD 69        CALL    $69CD               ; {}
69E1: CD 4B 65        CALL    $654B               ; {}
69E4: CD BC 5E        CALL    $5EBC               ; {}
69E7: 21 20 C3        LD      HL,$C320            
69EA: 09              ADD     HL,BC               
69EB: 36 04           LD      (HL),$04            
69ED: CD 84 65        CALL    $6584               ; {}
69F0: 21 80 C2        LD      HL,$C280            
69F3: 09              ADD     HL,BC               
69F4: 7E              LD      A,(HL)              
69F5: A7              AND     A                   
69F6: 20 18           JR      NZ,$6A10            ; {}
69F8: 21 B0 C2        LD      HL,$C2B0            
69FB: 09              ADD     HL,BC               
69FC: 7E              LD      A,(HL)              
69FD: EA 68 D3        LD      ($D368),A           
6A00: E0 B0           LD      ($FF00+$B0),A       
6A02: FA 7C D4        LD      A,($D47C)           
6A05: A7              AND     A                   
6A06: 28 07           JR      Z,$6A0F             ; {}
6A08: 3E 49           LD      A,$49               
6A0A: EA 68 D3        LD      ($D368),A           
6A0D: E0 BD           LD      ($FF00+$BD),A       
6A0F: C9              RET                         
6A10: F0 E7           LD      A,($E7)             
6A12: E6 07           AND     $07                 
6A14: 20 04           JR      NZ,$6A1A            ; {}
6A16: 3E 05           LD      A,$05               
6A18: E0 F4           LD      ($FF00+$F4),A       
6A1A: F0 E7           LD      A,($E7)             
6A1C: E6 01           AND     $01                 
6A1E: 20 21           JR      NZ,$6A41            ; {}
6A20: 3E 20           LD      A,$20               
6A22: CD 30 3C        CALL    $3C30               
6A25: F0 D7           LD      A,($D7)             
6A27: 2F              CPL                         
6A28: 3C              INC     A                   
6A29: 21 50 C2        LD      HL,$C250            
6A2C: CD 36 6A        CALL    $6A36               ; {}
6A2F: F0 D8           LD      A,($D8)             
6A31: 2F              CPL                         
6A32: 3C              INC     A                   
6A33: 21 40 C2        LD      HL,$C240            
6A36: 09              ADD     HL,BC               
6A37: 96              SUB     (HL)                
6A38: 28 07           JR      Z,$6A41             ; {}
6A3A: CB 7F           BIT     1,E                 
6A3C: 28 02           JR      Z,$6A40             ; {}
6A3E: 35              DEC     (HL)                
6A3F: 35              DEC     (HL)                
6A40: 34              INC     (HL)                
6A41: C9              RET                         
6A42: 78              LD      A,B                 
6A43: 00              NOP                         
6A44: 78              LD      A,B                 
6A45: 20 7A           JR      NZ,$6AC1            ; {}
6A47: 00              NOP                         
6A48: 7A              LD      A,D                 
6A49: 20 00           JR      NZ,$6A4B            ; {}
6A4B: F8 7C           LD      HL,SP+$7C           
6A4D: 00              NOP                         
6A4E: 00              NOP                         
6A4F: 00              NOP                         
6A50: 7E              LD      A,(HL)              
6A51: 00              NOP                         
6A52: 00              NOP                         
6A53: 08 7E 20        LD      ($207E),SP          
6A56: 00              NOP                         
6A57: 10 7C           ;;STOP    $7C                 
6A59: 20 F0           JR      NZ,$6A4B            ; {}
6A5B: F1              POP     AF                  
6A5C: FE 02           CP      $02                 
6A5E: 30 06           JR      NC,$6A66            ; {}
6A60: 11 42 6A        LD      DE,$6A42            
6A63: C3 3B 3C        JP      $3C3B               
6A66: 21 4A 6A        LD      HL,$6A4A            
6A69: 0E 04           LD      C,$04               
6A6B: CD 26 3D        CALL    $3D26               
6A6E: 3E 04           LD      A,$04               
6A70: CD D0 3D        CALL    $3DD0               
6A73: F0 F6           LD      A,($F6)             
6A75: FE 08           CP      $08                 
6A77: 28 04           JR      Z,$6A7D             ; {}
6A79: CD 19 3D        CALL    $3D19               
6A7C: C9              RET                         
6A7D: 21 40 C3        LD      HL,$C340            
6A80: 09              ADD     HL,BC               
6A81: CB A6           RES     1,E                 
6A83: C9              RET                         
6A84: 50              LD      D,B                 
6A85: 00              NOP                         
6A86: 52              LD      D,D                 
6A87: 00              NOP                         
6A88: F0 EC           LD      A,($EC)             
6A8A: D6 05           SUB     $05                 
6A8C: E0 EC           LD      ($FF00+$EC),A       
6A8E: 11 84 6A        LD      DE,$6A84            
6A91: CD 3B 3C        CALL    $3C3B               
6A94: CD DF 64        CALL    $64DF               ; {}
6A97: CD 8C 64        CALL    $648C               ; {}
6A9A: D0              RET     NC                  
6A9B: 1E FD           LD      E,$FD               
6A9D: F0 F6           LD      A,($F6)             
6A9F: FE A9           CP      $A9                 
6AA1: CA 98 6B        JP      Z,$6B98             ; {}
6AA4: 1E 41           LD      E,$41               
6AA6: FA A9 DA        LD      A,($DAA9)           
6AA9: E6 20           AND     $20                 
6AAB: CA 98 6B        JP      Z,$6B98             ; {}
6AAE: 1E 46           LD      E,$46               
6AB0: FA 65 DB        LD      A,($DB65)           
6AB3: E6 02           AND     $02                 
6AB5: CA 98 6B        JP      Z,$6B98             ; {}
6AB8: 1E 42           LD      E,$42               
6ABA: FA 56 DB        LD      A,($DB56)           
6ABD: FE 80           CP      $80                 
6ABF: CA 98 6B        JP      Z,$6B98             ; {}
6AC2: 1E 43           LD      E,$43               
6AC4: FA 66 DB        LD      A,($DB66)           
6AC7: E6 02           AND     $02                 
6AC9: CA 98 6B        JP      Z,$6B98             ; {}
6ACC: 1E 44           LD      E,$44               
6ACE: FA 56 DB        LD      A,($DB56)           
6AD1: FE 01           CP      $01                 
6AD3: CA 9E 6B        JP      Z,$6B9E             ; {}
6AD6: 1E 44           LD      E,$44               
6AD8: FA 55 DB        LD      A,($DB55)           
6ADB: FE 02           CP      $02                 
6ADD: C2 98 6B        JP      NZ,$6B98            ; {}
6AE0: 1E 45           LD      E,$45               
6AE2: FA 0E DB        LD      A,($DB0E)           
6AE5: FE 05           CP      $05                 
6AE7: DA 98 6B        JP      C,$6B98             ; {}
6AEA: 1E 47           LD      E,$47               
6AEC: FA 15 DB        LD      A,($DB15)           
6AEF: FE 05           CP      $05                 
6AF1: DA 98 6B        JP      C,$6B98             ; {}
6AF4: 1E 48           LD      E,$48               
6AF6: CA 98 6B        JP      Z,$6B98             ; {}
6AF9: FE 06           CP      $06                 
6AFB: C2 98 6B        JP      NZ,$6B98            ; {}
6AFE: 1E 49           LD      E,$49               
6B00: FA 67 DB        LD      A,($DB67)           
6B03: E6 02           AND     $02                 
6B05: CA 98 6B        JP      Z,$6B98             ; {}
6B08: 1E 4A           LD      E,$4A               
6B0A: FA 12 DB        LD      A,($DB12)           
6B0D: A7              AND     A                   
6B0E: CA 98 6B        JP      Z,$6B98             ; {}
6B11: 1E 40           LD      E,$40               
6B13: FA 68 DB        LD      A,($DB68)           
6B16: E6 02           AND     $02                 
6B18: CA 9E 6B        JP      Z,$6B9E             ; {}
6B1B: FA 79 DB        LD      A,($DB79)           
6B1E: A7              AND     A                   
6B1F: 28 09           JR      Z,$6B2A             ; {}
6B21: 1E 4B           LD      E,$4B               
6B23: FA E3 D9        LD      A,($D9E3)           
6B26: E6 40           AND     $40                 
6B28: 28 6E           JR      Z,$6B98             ; {}
6B2A: 1E 4C           LD      E,$4C               
6B2C: FA 69 DB        LD      A,($DB69)           
6B2F: E6 02           AND     $02                 
6B31: 28 65           JR      Z,$6B98             ; {}
6B33: 1E 45           LD      E,$45               
6B35: FA 49 DB        LD      A,($DB49)           
6B38: E6 01           AND     $01                 
6B3A: CA 9E 6B        JP      Z,$6B9E             ; {}
6B3D: 1E 4D           LD      E,$4D               
6B3F: FA 6A DB        LD      A,($DB6A)           
6B42: E6 02           AND     $02                 
6B44: 28 52           JR      Z,$6B98             ; {}
6B46: 1E 4E           LD      E,$4E               
6B48: FA 7B DB        LD      A,($DB7B)           
6B4B: A7              AND     A                   
6B4C: 28 0B           JR      Z,$6B59             ; {}
6B4E: 1E 46           LD      E,$46               
6B50: FA 14 DB        LD      A,($DB14)           
6B53: A7              AND     A                   
6B54: CA 9E 6B        JP      Z,$6B9E             ; {}
6B57: 1E 41           LD      E,$41               
6B59: FA 6B DB        LD      A,($DB6B)           
6B5C: E6 02           AND     $02                 
6B5E: 20 07           JR      NZ,$6B67            ; {}
6B60: 7B              LD      A,E                 
6B61: FE 4E           CP      $4E                 
6B63: 28 33           JR      Z,$6B98             ; {}
6B65: 18 37           JR      $6B9E               ; {}
6B67: 1E 4F           LD      E,$4F               
6B69: FA 10 D8        LD      A,($D810)           
6B6C: E6 30           AND     $30                 
6B6E: 28 28           JR      Z,$6B98             ; {}
6B70: 1E 48           LD      E,$48               
6B72: FA 6C DB        LD      A,($DB6C)           
6B75: E6 02           AND     $02                 
6B77: 28 25           JR      Z,$6B9E             ; {}
6B79: 1E 42           LD      E,$42               
6B7B: FA 06 D8        LD      A,($D806)           
6B7E: E6 30           AND     $30                 
6B80: 28 1C           JR      Z,$6B9E             ; {}
6B82: 1E 43           LD      E,$43               
6B84: FA 74 DA        LD      A,($DA74)           
6B87: E6 40           AND     $40                 
6B89: 28 13           JR      Z,$6B9E             ; {}
6B8B: 1E 47           LD      E,$47               
6B8D: FA 4E DB        LD      A,($DB4E)           
6B90: FE 02           CP      $02                 
6B92: 38 0A           JR      C,$6B9E             ; {}
6B94: 1E 48           LD      E,$48               
6B96: 18 06           JR      $6B9E               ; {}
6B98: 7B              LD      A,E                 
6B99: CD 85 21        CALL    $2185               
6B9C: 18 04           JR      $6BA2               ; {}
6B9E: 7B              LD      A,E                 
6B9F: CD 8E 21        CALL    $218E               
6BA2: 21 A9 DA        LD      HL,$DAA9            
6BA5: CB EE           SET     1,E                 
6BA7: C9              RET                         
6BA8: 5E              LD      E,(HL)              
6BA9: 00              NOP                         
6BAA: 5E              LD      E,(HL)              
6BAB: 40              LD      B,B                 
6BAC: 04              INC     B                   
6BAD: FC                              
6BAE: 03              INC     BC                  
6BAF: FD                              
6BB0: 02              LD      (BC),A              
6BB1: FE 05           CP      $05                 
6BB3: FA F0 F1        LD      A,($F1F0)           
6BB6: FE 01           CP      $01                 
6BB8: 20 06           JR      NZ,$6BC0            ; {}
6BBA: F0 EC           LD      A,($EC)             
6BBC: D6 00           SUB     $00                 
6BBE: E0 EC           LD      ($FF00+$EC),A       
6BC0: 11 A8 6B        LD      DE,$6BA8            
6BC3: CD D0 3C        CALL    $3CD0               
6BC6: CD DF 64        CALL    $64DF               ; {}
6BC9: 79              LD      A,C                 
6BCA: CB 27           SLA     1,E                 
6BCC: CB 27           SLA     1,E                 
6BCE: CB 27           SLA     1,E                 
6BD0: 21 E7 FF        LD      HL,$FFE7            
6BD3: 86              ADD     A,(HL)              
6BD4: E0 F0           LD      ($FF00+$F0),A       
6BD6: 1F              RRA                         
6BD7: 1F              RRA                         
6BD8: 1F              RRA                         
6BD9: E6 01           AND     $01                 
6BDB: CD 87 3B        CALL    $3B87               
6BDE: CD 4B 65        CALL    $654B               ; {}
6BE1: F0 F0           LD      A,($F0)             
6BE3: E6 1F           AND     $1F                 
6BE5: 20 16           JR      NZ,$6BFD            ; {}
6BE7: CD ED 27        CALL    $27ED               
6BEA: E6 07           AND     $07                 
6BEC: 5F              LD      E,A                 
6BED: 50              LD      D,B                 
6BEE: 21 AC 6B        LD      HL,$6BAC            
6BF1: 19              ADD     HL,DE               
6BF2: 7E              LD      A,(HL)              
6BF3: 21 B0 C2        LD      HL,$C2B0            
6BF6: 09              ADD     HL,BC               
6BF7: 86              ADD     A,(HL)              
6BF8: 21 40 C2        LD      HL,$C240            
6BFB: 09              ADD     HL,BC               
6BFC: 77              LD      (HL),A              
6BFD: F0 F0           LD      A,($F0)             
6BFF: C6 10           ADD     $10                 
6C01: E6 1F           AND     $1F                 
6C03: 20 16           JR      NZ,$6C1B            ; {}
6C05: CD ED 27        CALL    $27ED               
6C08: E6 07           AND     $07                 
6C0A: 5F              LD      E,A                 
6C0B: 50              LD      D,B                 
6C0C: 21 AC 6B        LD      HL,$6BAC            
6C0F: 19              ADD     HL,DE               
6C10: 7E              LD      A,(HL)              
6C11: 21 C0 C2        LD      HL,$C2C0            
6C14: 09              ADD     HL,BC               
6C15: 86              ADD     A,(HL)              
6C16: 21 50 C2        LD      HL,$C250            
6C19: 09              ADD     HL,BC               
6C1A: 77              LD      (HL),A              
6C1B: F0 F0           LD      A,($F0)             
6C1D: E6 3F           AND     $3F                 
6C1F: 20 36           JR      NZ,$6C57            ; {}
6C21: F0 98           LD      A,($98)             
6C23: F5              PUSH    AF                  
6C24: F0 99           LD      A,($99)             
6C26: F5              PUSH    AF                  
6C27: FA 0F C5        LD      A,($C50F)           
6C2A: FE FF           CP      $FF                 
6C2C: 28 10           JR      Z,$6C3E             ; {}
6C2E: 5F              LD      E,A                 
6C2F: 50              LD      D,B                 
6C30: 21 00 C2        LD      HL,$C200            
6C33: 19              ADD     HL,DE               
6C34: 7E              LD      A,(HL)              
6C35: E0 98           LD      ($FF00+$98),A       
6C37: 21 10 C2        LD      HL,$C210            
6C3A: 19              ADD     HL,DE               
6C3B: 7E              LD      A,(HL)              
6C3C: E0 99           LD      ($FF00+$99),A       
6C3E: 3E 02           LD      A,$02               
6C40: CD 30 3C        CALL    $3C30               
6C43: F1              POP     AF                  
6C44: E0 99           LD      ($FF00+$99),A       
6C46: F1              POP     AF                  
6C47: E0 98           LD      ($FF00+$98),A       
6C49: F0 D7           LD      A,($D7)             
6C4B: 21 C0 C2        LD      HL,$C2C0            
6C4E: 09              ADD     HL,BC               
6C4F: 77              LD      (HL),A              
6C50: F0 D8           LD      A,($D8)             
6C52: 21 B0 C2        LD      HL,$C2B0            
6C55: 09              ADD     HL,BC               
6C56: 77              LD      (HL),A              
6C57: C9              RET                         
6C58: 79              LD      A,C                 
6C59: EA 02 D2        LD      ($D202),A           
6C5C: F0 F7           LD      A,($F7)             
6C5E: FE 07           CP      $07                 
6C60: 20 04           JR      NZ,$6C66            ; {}
6C62: 3E 10           LD      A,$10               
6C64: E0 F5           LD      ($FF00+$F5),A       
6C66: CD 6C 6E        CALL    $6E6C               ; {}
6C69: CD 12 3F        CALL    $3F12               
6C6C: CD 0E 38        CALL    $380E               
6C6F: F0 EA           LD      A,($EA)             
6C71: FE 05           CP      $05                 
6C73: 28 55           JR      Z,$6CCA             ; {}
6C75: 21 30 C4        LD      HL,$C430            
6C78: 09              ADD     HL,BC               
6C79: 36 80           LD      (HL),$80            
6C7B: 21 B0 C2        LD      HL,$C2B0            
6C7E: 09              ADD     HL,BC               
6C7F: 7E              LD      A,(HL)              
6C80: C7              RST     0X00                
6C81: 85              ADD     A,L                 
6C82: 6C              LD      L,H                 
6C83: 96              SUB     (HL)                
6C84: 6C              LD      L,H                 
6C85: CD 91 08        CALL    $0891               
6C88: 36 FF           LD      (HL),$FF            
6C8A: 21 20 C4        LD      HL,$C420            
6C8D: 09              ADD     HL,BC               
6C8E: 36 FF           LD      (HL),$FF            
6C90: 21 B0 C2        LD      HL,$C2B0            
6C93: 09              ADD     HL,BC               
6C94: 34              INC     (HL)                
6C95: C9              RET                         
6C96: CD 91 08        CALL    $0891               
6C99: CA A9 6C        JP      Z,$6CA9             ; {}
6C9C: 21 20 C4        LD      HL,$C420            
6C9F: 09              ADD     HL,BC               
6CA0: 77              LD      (HL),A              
6CA1: FE 80           CP      $80                 
6CA3: 30 03           JR      NC,$6CA8            ; {}
6CA5: CD FC 6F        CALL    $6FFC               ; {}
6CA8: C9              RET                         
6CA9: CD BD 27        CALL    $27BD               
6CAC: CD 7A 3F        CALL    $3F7A               
6CAF: F0 F7           LD      A,($F7)             
6CB1: FE 07           CP      $07                 
6CB3: C8              RET     Z                   
6CB4: F0 F6           LD      A,($F6)             
6CB6: 5F              LD      E,A                 
6CB7: 50              LD      D,B                 
6CB8: F0 F7           LD      A,($F7)             
6CBA: FE 1A           CP      $1A                 
6CBC: 30 05           JR      NC,$6CC3            ; {}
6CBE: FE 06           CP      $06                 
6CC0: 38 01           JR      C,$6CC3             ; {}
6CC2: 14              INC     D                   
6CC3: 21 00 D9        LD      HL,$D900            
6CC6: 19              ADD     HL,DE               
6CC7: CB EE           SET     1,E                 
6CC9: C9              RET                         
6CCA: CD DF 64        CALL    $64DF               ; {}
6CCD: CD 01 65        CALL    $6501               ; {}
6CD0: CD B4 3B        CALL    $3BB4               
6CD3: 21 60 C3        LD      HL,$C360            
6CD6: 09              ADD     HL,BC               
6CD7: 7E              LD      A,(HL)              
6CD8: E0 E9           LD      ($FF00+$E9),A       
6CDA: 21 40 C2        LD      HL,$C240            
6CDD: 09              ADD     HL,BC               
6CDE: 7E              LD      A,(HL)              
6CDF: A7              AND     A                   
6CE0: 28 0D           JR      Z,$6CEF             ; {}
6CE2: 1E 00           LD      E,$00               
6CE4: E6 80           AND     $80                 
6CE6: 20 02           JR      NZ,$6CEA            ; {}
6CE8: 1E 03           LD      E,$03               
6CEA: 21 80 C3        LD      HL,$C380            
6CED: 09              ADD     HL,BC               
6CEE: 73              LD      (HL),E              
6CEF: CD 84 65        CALL    $6584               ; {}
6CF2: 21 20 C3        LD      HL,$C320            
6CF5: 09              ADD     HL,BC               
6CF6: 35              DEC     (HL)                
6CF7: 35              DEC     (HL)                
6CF8: 00              NOP                         
6CF9: 00              NOP                         
6CFA: 21 10 C3        LD      HL,$C310            
6CFD: 09              ADD     HL,BC               
6CFE: 7E              LD      A,(HL)              
6CFF: E6 80           AND     $80                 
6D01: E0 E8           LD      ($FF00+$E8),A       
6D03: 28 0F           JR      Z,$6D14             ; {}
6D05: 70              LD      (HL),B              
6D06: 21 20 C3        LD      HL,$C320            
6D09: 09              ADD     HL,BC               
6D0A: 7E              LD      A,(HL)              
6D0B: 70              LD      (HL),B              
6D0C: FE F2           CP      $F2                 
6D0E: 30 04           JR      NC,$6D14            ; {}
6D10: 3E 20           LD      A,$20               
6D12: E0 F2           LD      ($FF00+$F2),A       
6D14: F0 F0           LD      A,($F0)             
6D16: C7              RST     0X00                
6D17: 1F              RRA                         
6D18: 6D              LD      L,L                 
6D19: 60              LD      H,B                 
6D1A: 6D              LD      L,L                 
6D1B: 91              SUB     C                   
6D1C: 6D              LD      L,L                 
6D1D: 9A              SBC     D                   
6D1E: 6D              LD      L,L                 
6D1F: CD 91 08        CALL    $0891               
6D22: 20 3B           JR      NZ,$6D5F            ; {}
6D24: FA 01 D2        LD      A,($D201)           
6D27: 5F              LD      E,A                 
6D28: 50              LD      D,B                 
6D29: 21 00 C2        LD      HL,$C200            
6D2C: 19              ADD     HL,DE               
6D2D: F0 EE           LD      A,($EE)             
6D2F: 96              SUB     (HL)                
6D30: 1E 08           LD      E,$08               
6D32: CB 7F           BIT     1,E                 
6D34: 20 02           JR      NZ,$6D38            ; {}
6D36: 1E F8           LD      E,$F8               
6D38: 21 40 C2        LD      HL,$C240            
6D3B: 09              ADD     HL,BC               
6D3C: 73              LD      (HL),E              
6D3D: C6 10           ADD     $10                 
6D3F: FE 20           CP      $20                 
6D41: 30 09           JR      NC,$6D4C            ; {}
6D43: CD 91 08        CALL    $0891               
6D46: 36 18           LD      (HL),$18            
6D48: CD 8D 3B        CALL    $3B8D               
6D4B: C9              RET                         
6D4C: CD 58 65        CALL    $6558               ; {}
6D4F: F0 E8           LD      A,($E8)             
6D51: A7              AND     A                   
6D52: 28 06           JR      Z,$6D5A             ; {}
6D54: 21 20 C3        LD      HL,$C320            
6D57: 09              ADD     HL,BC               
6D58: 36 0C           LD      (HL),$0C            
6D5A: 3E 01           LD      A,$01               
6D5C: CD 87 3B        CALL    $3B87               
6D5F: C9              RET                         
6D60: CD 91 08        CALL    $0891               
6D63: 20 2B           JR      NZ,$6D90            ; {}
6D65: 21 80 C3        LD      HL,$C380            
6D68: 09              ADD     HL,BC               
6D69: 7E              LD      A,(HL)              
6D6A: A7              AND     A                   
6D6B: 3E 10           LD      A,$10               
6D6D: 20 02           JR      NZ,$6D71            ; {}
6D6F: 3E F0           LD      A,$F0               
6D71: F5              PUSH    AF                  
6D72: FA 01 D2        LD      A,($D201)           
6D75: 5F              LD      E,A                 
6D76: 50              LD      D,B                 
6D77: 21 40 C2        LD      HL,$C240            
6D7A: 19              ADD     HL,DE               
6D7B: F1              POP     AF                  
6D7C: 77              LD      (HL),A              
6D7D: 21 90 C2        LD      HL,$C290            
6D80: 19              ADD     HL,DE               
6D81: 36 01           LD      (HL),$01            
6D83: CD 91 08        CALL    $0891               
6D86: 36 20           LD      (HL),$20            
6D88: CD 8D 3B        CALL    $3B8D               
6D8B: 3E 00           LD      A,$00               
6D8D: CD 87 3B        CALL    $3B87               
6D90: C9              RET                         
6D91: CD 91 08        CALL    $0891               
6D94: 20 03           JR      NZ,$6D99            ; {}
6D96: CD 8D 3B        CALL    $3B8D               
6D99: C9              RET                         
6D9A: 21 10 C3        LD      HL,$C310            
6D9D: 09              ADD     HL,BC               
6D9E: 7E              LD      A,(HL)              
6D9F: FE 08           CP      $08                 
6DA1: 3E 01           LD      A,$01               
6DA3: 38 01           JR      C,$6DA6             ; {}
6DA5: 3C              INC     A                   
6DA6: CD 87 3B        CALL    $3B87               
6DA9: CD 91 08        CALL    $0891               
6DAC: FE 01           CP      $01                 
6DAE: 28 10           JR      Z,$6DC0             ; {}
6DB0: FE 00           CP      $00                 
6DB2: C2 0B 6E        JP      NZ,$6E0B            ; {}
6DB5: F0 E8           LD      A,($E8)             
6DB7: A7              AND     A                   
6DB8: 28 36           JR      Z,$6DF0             ; {}
6DBA: CD 91 08        CALL    $0891               
6DBD: 36 10           LD      (HL),$10            
6DBF: C9              RET                         
6DC0: 1E 10           LD      E,$10               
6DC2: 21 20 C3        LD      HL,$C320            
6DC5: 09              ADD     HL,BC               
6DC6: 36 19           LD      (HL),$19            
6DC8: F0 E9           LD      A,($E9)             
6DCA: FE 05           CP      $05                 
6DCC: 30 04           JR      NC,$6DD2            ; {}
6DCE: 1E 14           LD      E,$14               
6DD0: 36 16           LD      (HL),$16            
6DD2: 21 80 C3        LD      HL,$C380            
6DD5: 09              ADD     HL,BC               
6DD6: 7E              LD      A,(HL)              
6DD7: A7              AND     A                   
6DD8: 7B              LD      A,E                 
6DD9: 20 02           JR      NZ,$6DDD            ; {}
6DDB: 2F              CPL                         
6DDC: 3C              INC     A                   
6DDD: 21 40 C2        LD      HL,$C240            
6DE0: 09              ADD     HL,BC               
6DE1: 77              LD      (HL),A              
6DE2: F0 EC           LD      A,($EC)             
6DE4: FE 50           CP      $50                 
6DE6: 7B              LD      A,E                 
6DE7: 38 02           JR      C,$6DEB             ; {}
6DE9: 2F              CPL                         
6DEA: 3C              INC     A                   
6DEB: 21 50 C2        LD      HL,$C250            
6DEE: 09              ADD     HL,BC               
6DEF: 77              LD      (HL),A              
6DF0: CD 4B 65        CALL    $654B               ; {}
6DF3: CD 9E 3B        CALL    $3B9E               
6DF6: 21 A0 C2        LD      HL,$C2A0            
6DF9: 09              ADD     HL,BC               
6DFA: 7E              LD      A,(HL)              
6DFB: E6 03           AND     $03                 
6DFD: 28 0C           JR      Z,$6E0B             ; {}
6DFF: CD 8D 3B        CALL    $3B8D               
6E02: 70              LD      (HL),B              
6E03: CD 91 08        CALL    $0891               
6E06: 36 08           LD      (HL),$08            
6E08: CD AF 3D        CALL    $3DAF               
6E0B: C9              RET                         
6E0C: 00              NOP                         
6E0D: F8 60           LD      HL,SP+$60           
6E0F: 00              NOP                         
6E10: 00              NOP                         
6E11: 00              NOP                         
6E12: 62              LD      H,D                 
6E13: 00              NOP                         
6E14: 00              NOP                         
6E15: 08 64 00        LD      ($0064),SP          
6E18: F0 00           LD      A,($00)             
6E1A: 6E              LD      L,(HL)              
6E1B: 20 00           JR      NZ,$6E1D            ; {}
6E1D: F8 66           LD      HL,SP+$66           
6E1F: 00              NOP                         
6E20: 00              NOP                         
6E21: 00              NOP                         
6E22: 68              LD      L,B                 
6E23: 00              NOP                         
6E24: 00              NOP                         
6E25: 08 6A 00        LD      ($006A),SP          
6E28: F0 00           LD      A,($00)             
6E2A: 6E              LD      L,(HL)              
6E2B: 00              NOP                         
6E2C: 00              NOP                         
6E2D: F8 66           LD      HL,SP+$66           
6E2F: 00              NOP                         
6E30: 00              NOP                         
6E31: 00              NOP                         
6E32: 68              LD      L,B                 
6E33: 00              NOP                         
6E34: 00              NOP                         
6E35: 08 6A 00        LD      ($006A),SP          
6E38: F0 06           LD      A,($06)             
6E3A: 6E              LD      L,(HL)              
6E3B: 20 00           JR      NZ,$6E3D            ; {}
6E3D: 00              NOP                         
6E3E: 64              LD      H,H                 
6E3F: 20 00           JR      NZ,$6E41            ; {}
6E41: 08 62 20        LD      ($2062),SP          
6E44: 00              NOP                         
6E45: 10 60           ;;STOP    $60                 
6E47: 20 F0           JR      NZ,$6E39            ; {}
6E49: 08 6E 00        LD      ($006E),SP          
6E4C: 00              NOP                         
6E4D: 00              NOP                         
6E4E: 6A              LD      L,D                 
6E4F: 20 00           JR      NZ,$6E51            ; {}
6E51: 08 68 20        LD      ($2068),SP          
6E54: 00              NOP                         
6E55: 10 66           ;;STOP    $66                 
6E57: 20 F0           JR      NZ,$6E49            ; {}
6E59: 08 6E 20        LD      ($206E),SP          
6E5C: 00              NOP                         
6E5D: 00              NOP                         
6E5E: 6A              LD      L,D                 
6E5F: 20 00           JR      NZ,$6E61            ; {}
6E61: 08 68 20        LD      ($2068),SP          
6E64: 00              NOP                         
6E65: 10 66           ;;STOP    $66                 
6E67: 20 F0           JR      NZ,$6E59            ; {}
6E69: 02              LD      (BC),A              
6E6A: 6E              LD      L,(HL)              
6E6B: 00              NOP                         
6E6C: 21 80 C3        LD      HL,$C380            
6E6F: 09              ADD     HL,BC               
6E70: F0 F1           LD      A,($F1)             
6E72: 86              ADD     A,(HL)              
6E73: 17              RLA                         
6E74: 17              RLA                         
6E75: 17              RLA                         
6E76: 17              RLA                         
6E77: E6 F0           AND     $F0                 
6E79: 5F              LD      E,A                 
6E7A: 50              LD      D,B                 
6E7B: 21 0C 6E        LD      HL,$6E0C            
6E7E: 19              ADD     HL,DE               
6E7F: 0E 04           LD      C,$04               
6E81: CD 26 3D        CALL    $3D26               
6E84: 3E 04           LD      A,$04               
6E86: CD D0 3D        CALL    $3DD0               
6E89: 21 10 C3        LD      HL,$C310            
6E8C: 09              ADD     HL,BC               
6E8D: 7E              LD      A,(HL)              
6E8E: A7              AND     A                   
6E8F: 28 34           JR      Z,$6EC5             ; {}
6E91: F0 E7           LD      A,($E7)             
6E93: E6 01           AND     $01                 
6E95: 20 2E           JR      NZ,$6EC5            ; {}
6E97: FA C0 C3        LD      A,($C3C0)           
6E9A: 5F              LD      E,A                 
6E9B: 50              LD      D,B                 
6E9C: 21 30 C0        LD      HL,$C030            
6E9F: 19              ADD     HL,DE               
6EA0: F0 EF           LD      A,($EF)             
6EA2: C6 0C           ADD     $0C                 
6EA4: 22              LD      (HLI),A             
6EA5: F0 EE           LD      A,($EE)             
6EA7: C6 02           ADD     $02                 
6EA9: 22              LD      (HLI),A             
6EAA: 3E 26           LD      A,$26               
6EAC: 22              LD      (HLI),A             
6EAD: 3E 00           LD      A,$00               
6EAF: 22              LD      (HLI),A             
6EB0: F0 EF           LD      A,($EF)             
6EB2: C6 0C           ADD     $0C                 
6EB4: 22              LD      (HLI),A             
6EB5: F0 EE           LD      A,($EE)             
6EB7: C6 04           ADD     $04                 
6EB9: 22              LD      (HLI),A             
6EBA: 3E 26           LD      A,$26               
6EBC: 22              LD      (HLI),A             
6EBD: 3E 00           LD      A,$00               
6EBF: 22              LD      (HLI),A             
6EC0: 3E 02           LD      A,$02               
6EC2: CD D0 3D        CALL    $3DD0               
6EC5: C9              RET                         
6EC6: 6C              LD      L,H                 
6EC7: 00              NOP                         
6EC8: 6C              LD      L,H                 
6EC9: 20 6C           JR      NZ,$6F37            ; {}
6ECB: 40              LD      B,B                 
6ECC: 6C              LD      L,H                 
6ECD: 60              LD      H,B                 
6ECE: 70              LD      (HL),B              
6ECF: 60              LD      H,B                 
6ED0: 50              LD      D,B                 
6ED1: 40              LD      B,B                 
6ED2: 30 20           JR      NC,$6EF4            ; {}
6ED4: F0 F7           LD      A,($F7)             
6ED6: FE 07           CP      $07                 
6ED8: 20 04           JR      NZ,$6EDE            ; {}
6EDA: 3E 10           LD      A,$10               
6EDC: E0 F5           LD      ($FF00+$F5),A       
6EDE: F0 F8           LD      A,($F8)             
6EE0: E6 20           AND     $20                 
6EE2: C2 E5 65        JP      NZ,$65E5            ; {}
6EE5: 79              LD      A,C                 
6EE6: EA 01 D2        LD      ($D201),A           
6EE9: CD DB 6F        CALL    $6FDB               ; {}
6EEC: CD DF 64        CALL    $64DF               ; {}
6EEF: FA 02 D2        LD      A,($D202)           
6EF2: 5F              LD      E,A                 
6EF3: 50              LD      D,B                 
6EF4: 21 80 C2        LD      HL,$C280            
6EF7: 19              ADD     HL,DE               
6EF8: 7E              LD      A,(HL)              
6EF9: FE 01           CP      $01                 
6EFB: C8              RET     Z                   
6EFC: A7              AND     A                   
6EFD: 20 3A           JR      NZ,$6F39            ; {}
6EFF: CD 91 08        CALL    $0891               
6F02: 20 34           JR      NZ,$6F38            ; {}
6F04: 36 03           LD      (HL),$03            
6F06: 21 B0 C2        LD      HL,$C2B0            
6F09: 09              ADD     HL,BC               
6F0A: F0 EE           LD      A,($EE)             
6F0C: E0 D7           LD      ($FF00+$D7),A       
6F0E: 5E              LD      E,(HL)              
6F0F: 34              INC     (HL)                
6F10: 7E              LD      A,(HL)              
6F11: FE 06           CP      $06                 
6F13: 20 18           JR      NZ,$6F2D            ; {}
6F15: CD E5 65        CALL    $65E5               ; {}
6F18: 21 60 C4        LD      HL,$C460            
6F1B: 09              ADD     HL,BC               
6F1C: 5E              LD      E,(HL)              
6F1D: 50              LD      D,B                 
6F1E: 21 72 3F        LD      HL,$3F72            
6F21: 19              ADD     HL,DE               
6F22: F0 F6           LD      A,($F6)             
6F24: 5F              LD      E,A                 
6F25: 50              LD      D,B                 
6F26: 7E              LD      A,(HL)              
6F27: 21 00 CF        LD      HL,$CF00            
6F2A: 19              ADD     HL,DE               
6F2B: B6              OR      (HL)                
6F2C: 77              LD      (HL),A              
6F2D: 50              LD      D,B                 
6F2E: 21 CE 6E        LD      HL,$6ECE            
6F31: 19              ADD     HL,DE               
6F32: 7E              LD      A,(HL)              
6F33: E0 D8           LD      ($FF00+$D8),A       
6F35: C3 29 70        JP      $7029               ; {}
6F38: C9              RET                         
6F39: CD E2 08        CALL    $08E2               
6F3C: F0 A2           LD      A,($A2)             
6F3E: A7              AND     A                   
6F3F: 20 03           JR      NZ,$6F44            ; {}
6F41: CD B4 3B        CALL    $3BB4               
6F44: CD 58 65        CALL    $6558               ; {}
6F47: CD 9E 3B        CALL    $3B9E               
6F4A: 21 40 C2        LD      HL,$C240            
6F4D: 09              ADD     HL,BC               
6F4E: 7E              LD      A,(HL)              
6F4F: A7              AND     A                   
6F50: 28 25           JR      Z,$6F77             ; {}
6F52: CB 7F           BIT     1,E                 
6F54: 28 02           JR      Z,$6F58             ; {}
6F56: 2F              CPL                         
6F57: 3C              INC     A                   
6F58: 1E 04           LD      E,$04               
6F5A: FE 08           CP      $08                 
6F5C: 30 02           JR      NC,$6F60            ; {}
6F5E: 1E 08           LD      E,$08               
6F60: FE 04           CP      $04                 
6F62: 30 02           JR      NC,$6F66            ; {}
6F64: 1E 10           LD      E,$10               
6F66: FE 02           CP      $02                 
6F68: 30 02           JR      NC,$6F6C            ; {}
6F6A: 1E 20           LD      E,$20               
6F6C: 50              LD      D,B                 
6F6D: F0 E7           LD      A,($E7)             
6F6F: A3              AND     E                   
6F70: 28 01           JR      Z,$6F73             ; {}
6F72: 14              INC     D                   
6F73: 7A              LD      A,D                 
6F74: CD 87 3B        CALL    $3B87               
6F77: F0 F0           LD      A,($F0)             
6F79: C7              RST     0X00                
6F7A: 80              ADD     A,B                 
6F7B: 6F              LD      L,A                 
6F7C: 81              ADD     A,C                 
6F7D: 6F              LD      L,A                 
6F7E: B5              OR      L                   
6F7F: 6F              LD      L,A                 
6F80: C9              RET                         
6F81: 21 A0 C2        LD      HL,$C2A0            
6F84: 09              ADD     HL,BC               
6F85: 7E              LD      A,(HL)              
6F86: E6 03           AND     $03                 
6F88: 28 1A           JR      Z,$6FA4             ; {}
6F8A: 21 40 C2        LD      HL,$C240            
6F8D: 09              ADD     HL,BC               
6F8E: 7E              LD      A,(HL)              
6F8F: CB 2F           SRA     1,E                 
6F91: 2F              CPL                         
6F92: 3C              INC     A                   
6F93: 77              LD      (HL),A              
6F94: 3E 20           LD      A,$20               
6F96: EA 57 C1        LD      ($C157),A           
6F99: AF              XOR     A                   
6F9A: EA 58 C1        LD      ($C158),A           
6F9D: 3E 0B           LD      A,$0B               
6F9F: E0 F2           LD      ($FF00+$F2),A       
6FA1: CD 8D 3B        CALL    $3B8D               
6FA4: FA 10 D2        LD      A,($D210)           
6FA7: 3C              INC     A                   
6FA8: FE 09           CP      $09                 
6FAA: 38 05           JR      C,$6FB1             ; {}
6FAC: 3E 1A           LD      A,$1A               
6FAE: E0 F3           LD      ($FF00+$F3),A       
6FB0: AF              XOR     A                   
6FB1: EA 10 D2        LD      ($D210),A           
6FB4: C9              RET                         
6FB5: F0 E7           LD      A,($E7)             
6FB7: E6 07           AND     $07                 
6FB9: 20 0F           JR      NZ,$6FCA            ; {}
6FBB: 21 40 C2        LD      HL,$C240            
6FBE: 09              ADD     HL,BC               
6FBF: 7E              LD      A,(HL)              
6FC0: A7              AND     A                   
6FC1: 28 08           JR      Z,$6FCB             ; {}
6FC3: E6 80           AND     $80                 
6FC5: 28 02           JR      Z,$6FC9             ; {}
6FC7: 34              INC     (HL)                
6FC8: 34              INC     (HL)                
6FC9: 35              DEC     (HL)                
6FCA: C9              RET                         
6FCB: CD 8D 3B        CALL    $3B8D               
6FCE: 70              LD      (HL),B              
6FCF: CD 91 08        CALL    $0891               
6FD2: 36 50           LD      (HL),$50            
6FD4: C9              RET                         
6FD5: 80              ADD     A,B                 
6FD6: 70              LD      (HL),B              
6FD7: 60              LD      H,B                 
6FD8: 50              LD      D,B                 
6FD9: 40              LD      B,B                 
6FDA: 30 3E           JR      NC,$701A            ; {}
6FDC: 20 E0           JR      NZ,$6FBE            ; {}
6FDE: EC                              
6FDF: 11 C6 6E        LD      DE,$6EC6            
6FE2: CD 3B 3C        CALL    $3C3B               
6FE5: F0 EC           LD      A,($EC)             
6FE7: C6 10           ADD     $10                 
6FE9: E0 EC           LD      ($FF00+$EC),A       
6FEB: 21 B0 C2        LD      HL,$C2B0            
6FEE: 09              ADD     HL,BC               
6FEF: 5E              LD      E,(HL)              
6FF0: 50              LD      D,B                 
6FF1: 21 D5 6F        LD      HL,$6FD5            
6FF4: 19              ADD     HL,DE               
6FF5: BE              CP      (HL)                
6FF6: 20 E7           JR      NZ,$6FDF            ; {}
6FF8: CD BA 3D        CALL    $3DBA               
6FFB: C9              RET                         
6FFC: E6 07           AND     $07                 
6FFE: 20 1D           JR      NZ,$701D            ; {}
7000: CD ED 27        CALL    $27ED               
7003: E6 1F           AND     $1F                 
7005: D6 10           SUB     $10                 
7007: 5F              LD      E,A                 
7008: 21 EE FF        LD      HL,$FFEE            
700B: 86              ADD     A,(HL)              
700C: 77              LD      (HL),A              
700D: CD ED 27        CALL    $27ED               
7010: E6 1F           AND     $1F                 
7012: D6 14           SUB     $14                 
7014: 5F              LD      E,A                 
7015: 21 EC FF        LD      HL,$FFEC            
7018: 86              ADD     A,(HL)              
7019: 77              LD      (HL),A              
701A: CD 1E 70        CALL    $701E               ; {}
701D: C9              RET                         
701E: CD E5 64        CALL    $64E5               ; {}
7021: F0 EE           LD      A,($EE)             
7023: E0 D7           LD      ($FF00+$D7),A       
7025: F0 EC           LD      A,($EC)             
7027: E0 D8           LD      ($FF00+$D8),A       
7029: 3E 02           LD      A,$02               
702B: CD 53 09        CALL    $0953               
702E: 3E 13           LD      A,$13               
7030: E0 F4           LD      ($FF00+$F4),A       
7032: C9              RET                         
7033: 3E 36           LD      A,$36               
7035: CD 01 3C        CALL    $3C01               
7038: F0 D7           LD      A,($D7)             
703A: 21 00 C2        LD      HL,$C200            
703D: 19              ADD     HL,DE               
703E: 77              LD      (HL),A              
703F: F0 D8           LD      A,($D8)             
7041: 21 10 C2        LD      HL,$C210            
7044: 19              ADD     HL,DE               
7045: 77              LD      (HL),A              
7046: F0 F9           LD      A,($F9)             
7048: A7              AND     A                   
7049: 28 08           JR      Z,$7053             ; {}
704B: 21 50 C2        LD      HL,$C250            
704E: 09              ADD     HL,BC               
704F: 36 F0           LD      (HL),$F0            
7051: 18 0C           JR      $705F               ; {}
7053: 21 20 C3        LD      HL,$C320            
7056: 19              ADD     HL,DE               
7057: 36 10           LD      (HL),$10            
7059: 21 10 C3        LD      HL,$C310            
705C: 19              ADD     HL,DE               
705D: 36 08           LD      (HL),$08            
705F: CD E5 65        CALL    $65E5               ; {}
7062: CD D7 08        CALL    $08D7               
7065: C9              RET                         
7066: F0 F0           LD      A,($F0)             
7068: C7              RST     0X00                
7069: 6F              LD      L,A                 
706A: 70              LD      (HL),B              
706B: CE 70           ADC     $70                 
706D: 6D              LD      L,L                 
706E: 71              LD      (HL),C              
706F: CD 9E 65        CALL    $659E               ; {}
7072: C6 0E           ADD     $0E                 
7074: FE 1C           CP      $1C                 
7076: 30 45           JR      NC,$70BD            ; {}
7078: CD AE 65        CALL    $65AE               ; {}
707B: C6 0C           ADD     $0C                 
707D: FE 18           CP      $18                 
707F: 30 3C           JR      NC,$70BD            ; {}
7081: F0 9E           LD      A,($9E)             
7083: A7              AND     A                   
7084: 20 37           JR      NZ,$70BD            ; {}
7086: FA 33 C1        LD      A,($C133)           
7089: A7              AND     A                   
708A: 28 31           JR      Z,$70BD             ; {}
708C: CD 8D 3B        CALL    $3B8D               
708F: CD 91 08        CALL    $0891               
7092: 36 A0           LD      (HL),$A0            
7094: 3E 01           LD      A,$01               
7096: E0 A2           LD      ($FF00+$A2),A       
7098: 3E 02           LD      A,$02               
709A: EA 46 C1        LD      ($C146),A           
709D: 3E 12           LD      A,$12               
709F: E0 A3           LD      ($FF00+$A3),A       
70A1: 3E 0C           LD      A,$0C               
70A3: E0 9A           LD      ($FF00+$9A),A       
70A5: AF              XOR     A                   
70A6: E0 9B           LD      ($FF00+$9B),A       
70A8: 3E 00           LD      A,$00               
70AA: E0 9E           LD      ($FF00+$9E),A       
70AC: 3E 01           LD      A,$01               
70AE: EA 0A C1        LD      ($C10A),A           
70B1: 3E 1E           LD      A,$1E               
70B3: EA 68 D3        LD      ($D368),A           
70B6: AF              XOR     A                   
70B7: EA 6B C1        LD      ($C16B),A           
70BA: EA 6C C1        LD      ($C16C),A           
70BD: C9              RET                         
70BE: 50              LD      D,B                 
70BF: 00              NOP                         
70C0: 52              LD      D,D                 
70C1: 00              NOP                         
70C2: 54              LD      D,H                 
70C3: 00              NOP                         
70C4: 56              LD      D,(HL)              
70C5: 00              NOP                         
70C6: 98              SBC     B                   
70C7: 42              LD      B,D                 
70C8: 98              SBC     B                   
70C9: 50              LD      D,B                 
70CA: 99              SBC     C                   
70CB: 90              SUB     B                   
70CC: 99              SBC     C                   
70CD: 82              ADD     A,D                 
70CE: FA 46 C1        LD      A,($C146)           
70D1: A7              AND     A                   
70D2: C2 6C 71        JP      NZ,$716C            ; {}
70D5: CD 91 08        CALL    $0891               
70D8: 20 12           JR      NZ,$70EC            ; {}
70DA: 3E 01           LD      A,$01               
70DC: EA 7F C1        LD      ($C17F),A           
70DF: AF              XOR     A                   
70E0: EA 80 C1        LD      ($C180),A           
70E3: 3E 08           LD      A,$08               
70E5: EA CA C3        LD      ($C3CA),A           
70E8: CD 8D 3B        CALL    $3B8D               
70EB: AF              XOR     A                   
70EC: F5              PUSH    AF                  
70ED: FE 80           CP      $80                 
70EF: 30 53           JR      NC,$7144            ; {}
70F1: F5              PUSH    AF                  
70F2: E6 1F           AND     $1F                 
70F4: 20 11           JR      NZ,$7107            ; {}
70F6: FA 6B C1        LD      A,($C16B)           
70F9: FE 02           CP      $02                 
70FB: 28 0A           JR      Z,$7107             ; {}
70FD: 3E 03           LD      A,$03               
70FF: EA 6C C1        LD      ($C16C),A           
7102: C5              PUSH    BC                  
7103: CD 76 17        CALL    $1776               
7106: C1              POP     BC                  
7107: F1              POP     AF                  
7108: E6 0F           AND     $0F                 
710A: 20 38           JR      NZ,$7144            ; {}
710C: 21 C0 C2        LD      HL,$C2C0            
710F: 09              ADD     HL,BC               
7110: 7E              LD      A,(HL)              
7111: FE 04           CP      $04                 
7113: 28 2F           JR      Z,$7144             ; {}
7115: FA 00 D6        LD      A,($D600)           
7118: 5F              LD      E,A                 
7119: 50              LD      D,B                 
711A: C6 05           ADD     $05                 
711C: EA 00 D6        LD      ($D600),A           
711F: 21 01 D6        LD      HL,$D601            
7122: 19              ADD     HL,DE               
7123: E5              PUSH    HL                  
7124: 21 C0 C2        LD      HL,$C2C0            
7127: 09              ADD     HL,BC               
7128: 7E              LD      A,(HL)              
7129: 34              INC     (HL)                
712A: CB 27           SLA     1,E                 
712C: 5F              LD      E,A                 
712D: 50              LD      D,B                 
712E: 21 C6 70        LD      HL,$70C6            
7131: 19              ADD     HL,DE               
7132: E5              PUSH    HL                  
7133: D1              POP     DE                  
7134: E1              POP     HL                  
7135: 1A              LD      A,(DE)              
7136: 13              INC     DE                  
7137: 22              LD      (HLI),A             
7138: 1A              LD      A,(DE)              
7139: 22              LD      (HLI),A             
713A: 3E 01           LD      A,$01               
713C: 22              LD      (HLI),A             
713D: 3E 64           LD      A,$64               
713F: 22              LD      (HLI),A             
7140: 3E 65           LD      A,$65               
7142: 22              LD      (HLI),A             
7143: 70              LD      (HL),B              
7144: F1              POP     AF                  
7145: 1E 00           LD      E,$00               
7147: FE 80           CP      $80                 
7149: 38 01           JR      C,$714C             ; {}
714B: 1C              INC     E                   
714C: 7B              LD      A,E                 
714D: E0 F1           LD      ($FF00+$F1),A       
714F: 3E 58           LD      A,$58               
7151: E0 EE           LD      ($FF00+$EE),A       
7153: E0 98           LD      ($FF00+$98),A       
7155: 3E 44           LD      A,$44               
7157: E0 EC           LD      ($FF00+$EC),A       
7159: E0 99           LD      ($FF00+$99),A       
715B: 3E 02           LD      A,$02               
715D: E0 A1           LD      ($FF00+$A1),A       
715F: 3E FF           LD      A,$FF               
7161: E0 9D           LD      ($FF00+$9D),A       
7163: 11 BE 70        LD      DE,$70BE            
7166: CD 3B 3C        CALL    $3C3B               
7169: CD BA 3D        CALL    $3DBA               
716C: C9              RET                         
716D: AF              XOR     A                   
716E: CD 4D 71        CALL    $714D               ; {}
7171: FA 7F C1        LD      A,($C17F)           
7174: A7              AND     A                   
7175: 20 1B           JR      NZ,$7192            ; {}
7177: AF              XOR     A                   
7178: E0 9D           LD      ($FF00+$9D),A       
717A: 21 01 D4        LD      HL,$D401            
717D: 3E 01           LD      A,$01               
717F: 22              LD      (HLI),A             
7180: F0 F7           LD      A,($F7)             
7182: 22              LD      (HLI),A             
7183: 3E CE           LD      A,$CE               
7185: 22              LD      (HLI),A             
7186: 3E 50           LD      A,$50               
7188: 22              LD      (HLI),A             
7189: 3E 7C           LD      A,$7C               
718B: 77              LD      (HL),A              
718C: CD E5 65        CALL    $65E5               ; {}
718F: C3 2A 09        JP      $092A               
7192: C9              RET                         
7193: F0 FC           LD      A,($FC)             
7195: 50              LD      D,B                 
7196: 00              NOP                         
7197: F0 04           LD      A,($04)             
7199: 52              LD      D,D                 
719A: 00              NOP                         
719B: F0 0C           LD      A,($0C)             
719D: 54              LD      D,H                 
719E: 00              NOP                         
719F: 00              NOP                         
71A0: FC                              
71A1: 56              LD      D,(HL)              
71A2: 00              NOP                         
71A3: 00              NOP                         
71A4: 04              INC     B                   
71A5: 58              LD      E,B                 
71A6: 00              NOP                         
71A7: 00              NOP                         
71A8: 0C              INC     C                   
71A9: 5A              LD      E,D                 
71AA: 00              NOP                         
71AB: F0 FC           LD      A,($FC)             
71AD: 50              LD      D,B                 
71AE: 00              NOP                         
71AF: F0 04           LD      A,($04)             
71B1: 52              LD      D,D                 
71B2: 00              NOP                         
71B3: F0 0C           LD      A,($0C)             
71B5: 54              LD      D,H                 
71B6: 00              NOP                         
71B7: 00              NOP                         
71B8: FC                              
71B9: 5C              LD      E,H                 
71BA: 00              NOP                         
71BB: 00              NOP                         
71BC: 04              INC     B                   
71BD: 58              LD      E,B                 
71BE: 00              NOP                         
71BF: 00              NOP                         
71C0: 0C              INC     C                   
71C1: 5E              LD      E,(HL)              
71C2: 00              NOP                         
71C3: A8              XOR     B                   
71C4: 10 01           ;;STOP    $01                 
71C6: FF              RST     0X38                
71C7: 18 E8           JR      $71B1               ; {}
71C9: 21 D0 C2        LD      HL,$C2D0            
71CC: 09              ADD     HL,BC               
71CD: 7E              LD      A,(HL)              
71CE: A7              AND     A                   
71CF: CA 35 72        JP      Z,$7235             ; {}
71D2: 21 80 C2        LD      HL,$C280            
71D5: FA 01 D2        LD      A,($D201)           
71D8: 5F              LD      E,A                 
71D9: 50              LD      D,B                 
71DA: 19              ADD     HL,DE               
71DB: 7E              LD      A,(HL)              
71DC: A7              AND     A                   
71DD: CA E5 65        JP      Z,$65E5             ; {}
71E0: FA 02 D2        LD      A,($D202)           
71E3: E0 F1           LD      ($FF00+$F1),A       
71E5: 11 C3 71        LD      DE,$71C3            
71E8: CD D0 3C        CALL    $3CD0               
71EB: F0 E7           LD      A,($E7)             
71ED: E6 01           AND     $01                 
71EF: 20 40           JR      NZ,$7231            ; {}
71F1: 21 B0 C2        LD      HL,$C2B0            
71F4: 09              ADD     HL,BC               
71F5: 5E              LD      E,(HL)              
71F6: 50              LD      D,B                 
71F7: 21 C5 71        LD      HL,$71C5            
71FA: 19              ADD     HL,DE               
71FB: 7E              LD      A,(HL)              
71FC: 21 40 C2        LD      HL,$C240            
71FF: 09              ADD     HL,BC               
7200: 86              ADD     A,(HL)              
7201: 77              LD      (HL),A              
7202: 21 C7 71        LD      HL,$71C7            
7205: 19              ADD     HL,DE               
7206: BE              CP      (HL)                
7207: 20 08           JR      NZ,$7211            ; {}
7209: 21 B0 C2        LD      HL,$C2B0            
720C: 09              ADD     HL,BC               
720D: 7E              LD      A,(HL)              
720E: EE 01           XOR     $01                 
7210: 77              LD      (HL),A              
7211: 21 C0 C2        LD      HL,$C2C0            
7214: 09              ADD     HL,BC               
7215: 5E              LD      E,(HL)              
7216: 50              LD      D,B                 
7217: 21 C5 71        LD      HL,$71C5            
721A: 19              ADD     HL,DE               
721B: 7E              LD      A,(HL)              
721C: 21 50 C2        LD      HL,$C250            
721F: 09              ADD     HL,BC               
7220: 86              ADD     A,(HL)              
7221: 77              LD      (HL),A              
7222: 21 C7 71        LD      HL,$71C7            
7225: 19              ADD     HL,DE               
7226: BE              CP      (HL)                
7227: 20 08           JR      NZ,$7231            ; {}
7229: 21 C0 C2        LD      HL,$C2C0            
722C: 09              ADD     HL,BC               
722D: 7E              LD      A,(HL)              
722E: EE 01           XOR     $01                 
7230: 77              LD      (HL),A              
7231: CD 4B 65        CALL    $654B               ; {}
7234: C9              RET                         
7235: 21 93 71        LD      HL,$7193            
7238: F0 E7           LD      A,($E7)             
723A: E6 08           AND     $08                 
723C: 28 03           JR      Z,$7241             ; {}
723E: 21 AB 71        LD      HL,$71AB            
7241: 0E 06           LD      C,$06               
7243: CD 26 3D        CALL    $3D26               
7246: 3E 06           LD      A,$06               
7248: CD D0 3D        CALL    $3DD0               
724B: CD 19 3D        CALL    $3D19               
724E: 1E FE           LD      E,$FE               
7250: 21 D0 C3        LD      HL,$C3D0            
7253: 09              ADD     HL,BC               
7254: 34              INC     (HL)                
7255: 7E              LD      A,(HL)              
7256: E6 40           AND     $40                 
7258: 28 02           JR      Z,$725C             ; {}
725A: 1E 02           LD      E,$02               
725C: 21 20 C3        LD      HL,$C320            
725F: 09              ADD     HL,BC               
7260: 73              LD      (HL),E              
7261: CD 84 65        CALL    $6584               ; {}
7264: CD DF 64        CALL    $64DF               ; {}
7267: F0 F0           LD      A,($F0)             
7269: C7              RST     0X00                
726A: 70              LD      (HL),B              
726B: 72              LD      (HL),D              
726C: 9A              SBC     D                   
726D: 72              LD      (HL),D              
726E: 06 73           LD      B,$73               
7270: AF              XOR     A                   
7271: EA 02 D2        LD      ($D202),A           
7274: 79              LD      A,C                 
7275: EA 01 D2        LD      ($D201),A           
7278: F0 98           LD      A,($98)             
727A: D6 50           SUB     $50                 
727C: C6 08           ADD     $08                 
727E: FE 10           CP      $10                 
7280: 30 17           JR      NC,$7299            ; {}
7282: F0 99           LD      A,($99)             
7284: D6 58           SUB     $58                 
7286: C6 08           ADD     $08                 
7288: FE 10           CP      $10                 
728A: 30 0D           JR      NC,$7299            ; {}
728C: CD 8D 3B        CALL    $3B8D               
728F: CD 87 08        CALL    $0887               
7292: 36 48           LD      (HL),$48            
7294: 3E 24           LD      A,$24               
7296: CD 97 21        CALL    $2197               
7299: C9              RET                         
729A: CD 87 08        CALL    $0887               
729D: 20 0D           JR      NZ,$72AC            ; {}
729F: CD 91 08        CALL    $0891               
72A2: 36 48           LD      (HL),$48            
72A4: CD 8D 3B        CALL    $3B8D               
72A7: 3E 26           LD      A,$26               
72A9: E0 F2           LD      ($FF00+$F2),A       
72AB: C9              RET                         
72AC: 3E 02           LD      A,$02               
72AE: E0 A1           LD      ($FF00+$A1),A       
72B0: 3E 1A           LD      A,$1A               
72B2: E0 F2           LD      ($FF00+$F2),A       
72B4: CD DF 64        CALL    $64DF               ; {}
72B7: 21 00 C3        LD      HL,$C300            
72BA: 09              ADD     HL,BC               
72BB: 7E              LD      A,(HL)              
72BC: A7              AND     A                   
72BD: 20 10           JR      NZ,$72CF            ; {}
72BF: 36 01           LD      (HL),$01            
72C1: 21 B0 C2        LD      HL,$C2B0            
72C4: 09              ADD     HL,BC               
72C5: 7E              LD      A,(HL)              
72C6: FE 04           CP      $04                 
72C8: 38 05           JR      C,$72CF             ; {}
72CA: 3E 04           LD      A,$04               
72CC: EA 93 DB        LD      ($DB93),A           
72CF: CD 8C 08        CALL    $088C               
72D2: 20 31           JR      NZ,$7305            ; {}
72D4: 36 13           LD      (HL),$13            
72D6: 21 B0 C2        LD      HL,$C2B0            
72D9: 09              ADD     HL,BC               
72DA: 7E              LD      A,(HL)              
72DB: FE 0A           CP      $0A                 
72DD: 28 26           JR      Z,$7305             ; {}
72DF: 34              INC     (HL)                
72E0: 3E 84           LD      A,$84               
72E2: CD 01 3C        CALL    $3C01               
72E5: 38 1E           JR      C,$7305             ; {}
72E7: 21 D0 C2        LD      HL,$C2D0            
72EA: 19              ADD     HL,DE               
72EB: 36 01           LD      (HL),$01            
72ED: F0 D7           LD      A,($D7)             
72EF: 21 00 C2        LD      HL,$C200            
72F2: 19              ADD     HL,DE               
72F3: C6 00           ADD     $00                 
72F5: 77              LD      (HL),A              
72F6: F0 D8           LD      A,($D8)             
72F8: 21 10 C2        LD      HL,$C210            
72FB: 19              ADD     HL,DE               
72FC: D6 0E           SUB     $0E                 
72FE: 77              LD      (HL),A              
72FF: 21 40 C2        LD      HL,$C240            
7302: 19              ADD     HL,DE               
7303: 36 E8           LD      (HL),$E8            
7305: C9              RET                         
7306: CD 91 08        CALL    $0891               
7309: CA E5 65        JP      Z,$65E5             ; {}
730C: F0 E7           LD      A,($E7)             
730E: E6 02           AND     $02                 
7310: 3E 00           LD      A,$00               
7312: 28 02           JR      Z,$7316             ; {}
7314: 3E FF           LD      A,$FF               
7316: EA 02 D2        LD      ($D202),A           
7319: CD 87 3B        CALL    $3B87               
731C: 3E 02           LD      A,$02               
731E: E0 A1           LD      ($FF00+$A1),A       
7320: C9              RET                         
7321: 68              LD      L,B                 
7322: 00              NOP                         
7323: 6A              LD      L,D                 
7324: 00              NOP                         
7325: 64              LD      H,H                 
7326: 00              NOP                         
7327: 66              LD      H,(HL)              
7328: 00              NOP                         
7329: 6C              LD      L,H                 
732A: 00              NOP                         
732B: 6E              LD      L,(HL)              
732C: 00              NOP                         
732D: 6A              LD      L,D                 
732E: 20 68           JR      NZ,$7398            ; {}
7330: 20 66           JR      NZ,$7398            ; {}
7332: 20 64           JR      NZ,$7398            ; {}
7334: 20 6E           JR      NZ,$73A4            ; {}
7336: 20 6C           JR      NZ,$73A4            ; {}
7338: 20 21           JR      NZ,$735B            ; {}
733A: 80              ADD     A,B                 
733B: C3 09 F0        JP      $F009               
733E: F1              POP     AF                  
733F: 86              ADD     A,(HL)              
7340: E0 F1           LD      ($FF00+$F1),A       
7342: 21 40 C2        LD      HL,$C240            
7345: 09              ADD     HL,BC               
7346: 7E              LD      A,(HL)              
7347: A7              AND     A                   
7348: 28 0D           JR      Z,$7357             ; {}
734A: E6 80           AND     $80                 
734C: 3E 00           LD      A,$00               
734E: 20 02           JR      NZ,$7352            ; {}
7350: 3E 03           LD      A,$03               
7352: 21 80 C3        LD      HL,$C380            
7355: 09              ADD     HL,BC               
7356: 77              LD      (HL),A              
7357: 11 21 73        LD      DE,$7321            
735A: CD 3B 3C        CALL    $3C3B               
735D: CD DF 64        CALL    $64DF               ; {}
7360: FA A5 DB        LD      A,($DBA5)           
7363: A7              AND     A                   
7364: CA 67 74        JP      Z,$7467             ; {}
7367: CD 84 65        CALL    $6584               ; {}
736A: 21 20 C3        LD      HL,$C320            
736D: 09              ADD     HL,BC               
736E: 35              DEC     (HL)                
736F: 21 10 C3        LD      HL,$C310            
7372: 09              ADD     HL,BC               
7373: 7E              LD      A,(HL)              
7374: E6 80           AND     $80                 
7376: E0 E8           LD      ($FF00+$E8),A       
7378: 28 06           JR      Z,$7380             ; {}
737A: 70              LD      (HL),B              
737B: 21 10 C3        LD      HL,$C310            
737E: 09              ADD     HL,BC               
737F: 70              LD      (HL),B              
7380: F0 F0           LD      A,($F0)             
7382: C7              RST     0X00                
7383: 91              SUB     C                   
7384: 73              LD      (HL),E              
7385: D7              RST     0X10                
7386: 73              LD      (HL),E              
7387: 07              RLCA                        
7388: 74              LD      (HL),H              
7389: 02              LD      (BC),A              
738A: 06 08           LD      B,$08               
738C: 06 FE           LD      B,$FE               
738E: FA F8 FA        LD      A,($FAF8)           
7391: CD 2A 74        CALL    $742A               ; {}
7394: AF              XOR     A                   
7395: CD 87 3B        CALL    $3B87               
7398: CD 91 08        CALL    $0891               
739B: 20 37           JR      NZ,$73D4            ; {}
739D: CD ED 27        CALL    $27ED               
73A0: E6 07           AND     $07                 
73A2: 5F              LD      E,A                 
73A3: 50              LD      D,B                 
73A4: 21 89 73        LD      HL,$7389            
73A7: 19              ADD     HL,DE               
73A8: 7E              LD      A,(HL)              
73A9: 21 40 C2        LD      HL,$C240            
73AC: 09              ADD     HL,BC               
73AD: 77              LD      (HL),A              
73AE: 7B              LD      A,E                 
73AF: E6 04           AND     $04                 
73B1: 21 80 C3        LD      HL,$C380            
73B4: 09              ADD     HL,BC               
73B5: 77              LD      (HL),A              
73B6: CD ED 27        CALL    $27ED               
73B9: E6 07           AND     $07                 
73BB: 5F              LD      E,A                 
73BC: 21 89 73        LD      HL,$7389            
73BF: 19              ADD     HL,DE               
73C0: 7E              LD      A,(HL)              
73C1: 21 50 C2        LD      HL,$C250            
73C4: 09              ADD     HL,BC               
73C5: 77              LD      (HL),A              
73C6: CD 91 08        CALL    $0891               
73C9: CD ED 27        CALL    $27ED               
73CC: E6 1F           AND     $1F                 
73CE: C6 20           ADD     $20                 
73D0: 77              LD      (HL),A              
73D1: CD 8D 3B        CALL    $3B8D               
73D4: C3 FC 73        JP      $73FC               ; {}
73D7: CD 2A 74        CALL    $742A               ; {}
73DA: CD 4B 65        CALL    $654B               ; {}
73DD: CD 9E 3B        CALL    $3B9E               
73E0: F0 E8           LD      A,($E8)             
73E2: A7              AND     A                   
73E3: 28 17           JR      Z,$73FC             ; {}
73E5: CD 91 08        CALL    $0891               
73E8: 20 07           JR      NZ,$73F1            ; {}
73EA: 36 30           LD      (HL),$30            
73EC: CD 8D 3B        CALL    $3B8D               
73EF: 70              LD      (HL),B              
73F0: C9              RET                         
73F1: 21 20 C3        LD      HL,$C320            
73F4: 09              ADD     HL,BC               
73F5: 36 08           LD      (HL),$08            
73F7: 21 10 C3        LD      HL,$C310            
73FA: 09              ADD     HL,BC               
73FB: 34              INC     (HL)                
73FC: F0 E7           LD      A,($E7)             
73FE: 1F              RRA                         
73FF: 1F              RRA                         
7400: 1F              RRA                         
7401: E6 01           AND     $01                 
7403: CD 87 3B        CALL    $3B87               
7406: C9              RET                         
7407: CD 4B 65        CALL    $654B               ; {}
740A: CD 9E 3B        CALL    $3B9E               
740D: F0 E7           LD      A,($E7)             
740F: E6 01           AND     $01                 
7411: 20 05           JR      NZ,$7418            ; {}
7413: 21 20 C3        LD      HL,$C320            
7416: 09              ADD     HL,BC               
7417: 34              INC     (HL)                
7418: F0 E8           LD      A,($E8)             
741A: A7              AND     A                   
741B: 28 04           JR      Z,$7421             ; {}
741D: CD 8D 3B        CALL    $3B8D               
7420: 70              LD      (HL),B              
7421: F0 E7           LD      A,($E7)             
7423: 1F              RRA                         
7424: E6 02           AND     $02                 
7426: CD 87 3B        CALL    $3B87               
7429: C9              RET                         
742A: FA 37 C1        LD      A,($C137)           
742D: FE 02           CP      $02                 
742F: 20 35           JR      NZ,$7466            ; {}
7431: CD 9E 65        CALL    $659E               ; {}
7434: C6 18           ADD     $18                 
7436: FE 30           CP      $30                 
7438: 30 2C           JR      NC,$7466            ; {}
743A: CD AE 65        CALL    $65AE               ; {}
743D: C6 18           ADD     $18                 
743F: FE 30           CP      $30                 
7441: 30 23           JR      NC,$7466            ; {}
7443: CD 8D 3B        CALL    $3B8D               
7446: 36 02           LD      (HL),$02            
7448: 3E 10           LD      A,$10               
744A: CD 30 3C        CALL    $3C30               
744D: F0 D7           LD      A,($D7)             
744F: 2F              CPL                         
7450: 3C              INC     A                   
7451: 21 50 C2        LD      HL,$C250            
7454: 09              ADD     HL,BC               
7455: 77              LD      (HL),A              
7456: F0 D8           LD      A,($D8)             
7458: 2F              CPL                         
7459: 3C              INC     A                   
745A: 21 40 C2        LD      HL,$C240            
745D: 09              ADD     HL,BC               
745E: 77              LD      (HL),A              
745F: 21 20 C3        LD      HL,$C320            
7462: 09              ADD     HL,BC               
7463: 36 0C           LD      (HL),$0C            
7465: F1              POP     AF                  
7466: C9              RET                         
7467: C9              RET                         
7468: 70              LD      (HL),B              
7469: 00              NOP                         
746A: 70              LD      (HL),B              
746B: 20 72           JR      NZ,$74DF            ; {}
746D: 00              NOP                         
746E: 72              LD      (HL),D              
746F: 20 FA           JR      NZ,$746B            ; {}
7471: 66              LD      H,(HL)              
7472: C1              POP     BC                  
7473: FE 01           CP      $01                 
7475: 20 2B           JR      NZ,$74A2            ; {}
7477: FA 49 DB        LD      A,($DB49)           
747A: E6 04           AND     $04                 
747C: 28 24           JR      Z,$74A2             ; {}
747E: FA 4A DB        LD      A,($DB4A)           
7481: A7              AND     A                   
7482: 20 1E           JR      NZ,$74A2            ; {}
7484: F0 EA           LD      A,($EA)             
7486: FE 01           CP      $01                 
7488: 28 18           JR      Z,$74A2             ; {}
748A: 21 80 C4        LD      HL,$C480            
748D: 09              ADD     HL,BC               
748E: 36 1F           LD      (HL),$1F            
7490: 21 80 C2        LD      HL,$C280            
7493: 09              ADD     HL,BC               
7494: 36 01           LD      (HL),$01            
7496: 21 40 C3        LD      HL,$C340            
7499: 09              ADD     HL,BC               
749A: 36 04           LD      (HL),$04            
749C: 21 F4 FF        LD      HL,$FFF4            
749F: 36 13           LD      (HL),$13            
74A1: C9              RET                         
74A2: 11 68 74        LD      DE,$7468            
74A5: CD 3B 3C        CALL    $3C3B               
74A8: CD DF 64        CALL    $64DF               ; {}
74AB: CD 01 65        CALL    $6501               ; {}
74AE: CD 4B 65        CALL    $654B               ; {}
74B1: 21 10 C4        LD      HL,$C410            
74B4: 09              ADD     HL,BC               
74B5: 36 01           LD      (HL),$01            
74B7: E5              PUSH    HL                  
74B8: CD 9E 3B        CALL    $3B9E               
74BB: E1              POP     HL                  
74BC: 70              LD      (HL),B              
74BD: CD B4 3B        CALL    $3BB4               
74C0: F0 F0           LD      A,($F0)             
74C2: E6 01           AND     $01                 
74C4: C7              RST     0X00                
74C5: D5              PUSH    DE                  
74C6: 74              LD      (HL),H              
74C7: 1A              LD      A,(DE)              
74C8: 75              LD      (HL),L              
74C9: 08 08 F8        LD      ($F808),SP          
74CC: F8 04           LD      HL,SP+$04           
74CE: FC                              
74CF: FC                              
74D0: 04              INC     B                   
74D1: FC                              
74D2: 04              INC     B                   
74D3: 08 F8 21        LD      ($21F8),SP          
74D6: B0              OR      B                   
74D7: C3 09 36        JP      $3609               
74DA: 01 CD 91        LD      BC,$91CD            
74DD: 08 20 39        LD      ($3920),SP          
74E0: CD 8D 3B        CALL    $3B8D               
74E3: CD ED 27        CALL    $27ED               
74E6: E6 07           AND     $07                 
74E8: C6 10           ADD     $10                 
74EA: 21 20 C3        LD      HL,$C320            
74ED: 09              ADD     HL,BC               
74EE: 77              LD      (HL),A              
74EF: CD ED 27        CALL    $27ED               
74F2: E6 07           AND     $07                 
74F4: FE 06           CP      $06                 
74F6: 38 07           JR      C,$74FF             ; {}
74F8: 3E 0A           LD      A,$0A               
74FA: CD 25 3C        CALL    $3C25               
74FD: 18 16           JR      $7515               ; {}
74FF: 5F              LD      E,A                 
7500: 50              LD      D,B                 
7501: 21 C9 74        LD      HL,$74C9            
7504: 19              ADD     HL,DE               
7505: 7E              LD      A,(HL)              
7506: 21 40 C2        LD      HL,$C240            
7509: 09              ADD     HL,BC               
750A: 77              LD      (HL),A              
750B: 21 CF 74        LD      HL,$74CF            
750E: 19              ADD     HL,DE               
750F: 7E              LD      A,(HL)              
7510: 21 50 C2        LD      HL,$C250            
7513: 09              ADD     HL,BC               
7514: 77              LD      (HL),A              
7515: AF              XOR     A                   
7516: CD 87 3B        CALL    $3B87               
7519: C9              RET                         
751A: CD 84 65        CALL    $6584               ; {}
751D: 21 20 C3        LD      HL,$C320            
7520: 09              ADD     HL,BC               
7521: 35              DEC     (HL)                
7522: 21 10 C3        LD      HL,$C310            
7525: 09              ADD     HL,BC               
7526: 7E              LD      A,(HL)              
7527: E6 80           AND     $80                 
7529: 28 13           JR      Z,$753E             ; {}
752B: AF              XOR     A                   
752C: 77              LD      (HL),A              
752D: CD 8D 3B        CALL    $3B8D               
7530: CD 91 08        CALL    $0891               
7533: CD ED 27        CALL    $27ED               
7536: E6 0F           AND     $0F                 
7538: C6 18           ADD     $18                 
753A: 77              LD      (HL),A              
753B: CD AF 3D        CALL    $3DAF               
753E: C9              RET                         
753F: 60              LD      H,B                 
7540: 00              NOP                         
7541: 62              LD      H,D                 
7542: 00              NOP                         
7543: 64              LD      H,H                 
7544: 00              NOP                         
7545: 66              LD      H,(HL)              
7546: 00              NOP                         
7547: 11 3F 75        LD      DE,$753F            
754A: CD 3B 3C        CALL    $3C3B               
754D: CD DF 64        CALL    $64DF               ; {}
7550: CD 01 65        CALL    $6501               ; {}
7553: AF              XOR     A                   
7554: E0 E8           LD      ($FF00+$E8),A       
7556: CD EB 3B        CALL    $3BEB               
7559: CD D5 3B        CALL    $3BD5               
755C: 30 0D           JR      NC,$756B            ; {}
755E: 3E 01           LD      A,$01               
7560: E0 E8           LD      ($FF00+$E8),A       
7562: F0 F0           LD      A,($F0)             
7564: FE 02           CP      $02                 
7566: 30 03           JR      NC,$756B            ; {}
7568: CD 4A 09        CALL    $094A               
756B: CD 4B 65        CALL    $654B               ; {}
756E: CD 9E 3B        CALL    $3B9E               
7571: F0 F0           LD      A,($F0)             
7573: C7              RST     0X00                
7574: 7A              LD      A,D                 
7575: 75              LD      (HL),L              
7576: 8E              ADC     A,(HL)              
7577: 75              LD      (HL),L              
7578: C4 75 F0        CALL    NZ,$F075            
757B: E8 A7           ADD     SP,$A7              
757D: 28 0E           JR      Z,$758D             ; {}
757F: CD 8D 3B        CALL    $3B8D               
7582: CD 91 08        CALL    $0891               
7585: 36 30           LD      (HL),$30            
7587: 21 20 C4        LD      HL,$C420            
758A: 09              ADD     HL,BC               
758B: 36 18           LD      (HL),$18            
758D: C9              RET                         
758E: CD 91 08        CALL    $0891               
7591: 20 19           JR      NZ,$75AC            ; {}
7593: CD 8D 3B        CALL    $3B8D               
7596: 21 40 C3        LD      HL,$C340            
7599: 09              ADD     HL,BC               
759A: CB BE           RES     1,E                 
759C: 21 50 C3        LD      HL,$C350            
759F: 09              ADD     HL,BC               
75A0: CB BE           RES     1,E                 
75A2: 21 30 C4        LD      HL,$C430            
75A5: 09              ADD     HL,BC               
75A6: CB B6           RES     1,E                 
75A8: CD AF 3D        CALL    $3DAF               
75AB: C9              RET                         
75AC: 1E 08           LD      E,$08               
75AE: E6 04           AND     $04                 
75B0: 28 02           JR      Z,$75B4             ; {}
75B2: 1E F8           LD      E,$F8               
75B4: 21 40 C2        LD      HL,$C240            
75B7: 09              ADD     HL,BC               
75B8: 73              LD      (HL),E              
75B9: C9              RET                         
75BA: F8 FA           LD      HL,SP+$FA           
75BC: 00              NOP                         
75BD: 06 08           LD      B,$08               
75BF: 06 00           LD      B,$00               
75C1: FA F8 FA        LD      A,($FAF8)           
75C4: CD 91 08        CALL    $0891               
75C7: 20 20           JR      NZ,$75E9            ; {}
75C9: CD ED 27        CALL    $27ED               
75CC: E6 3F           AND     $3F                 
75CE: C6 20           ADD     $20                 
75D0: 77              LD      (HL),A              
75D1: E6 07           AND     $07                 
75D3: 5F              LD      E,A                 
75D4: 50              LD      D,B                 
75D5: 21 BC 75        LD      HL,$75BC            
75D8: 19              ADD     HL,DE               
75D9: 7E              LD      A,(HL)              
75DA: 21 40 C2        LD      HL,$C240            
75DD: 09              ADD     HL,BC               
75DE: 77              LD      (HL),A              
75DF: 21 BA 75        LD      HL,$75BA            
75E2: 19              ADD     HL,DE               
75E3: 7E              LD      A,(HL)              
75E4: 21 50 C2        LD      HL,$C250            
75E7: 09              ADD     HL,BC               
75E8: 77              LD      (HL),A              
75E9: F0 E7           LD      A,($E7)             
75EB: 1F              RRA                         
75EC: 1F              RRA                         
75ED: 1F              RRA                         
75EE: 1F              RRA                         
75EF: E6 01           AND     $01                 
75F1: CD 87 3B        CALL    $3B87               
75F4: C9              RET                         
75F5: 50              LD      D,B                 
75F6: 00              NOP                         
75F7: 50              LD      D,B                 
75F8: 20 20           JR      NZ,$761A            ; {}
75FA: E0 00           LD      ($FF00+$00),A       
75FC: 00              NOP                         
75FD: F8 08           LD      HL,SP+$08           
75FF: 00              NOP                         
7600: 00              NOP                         
7601: 00              NOP                         
7602: 00              NOP                         
7603: E0 20           LD      ($FF00+$20),A       
7605: 00              NOP                         
7606: 00              NOP                         
7607: 08 F8 30        LD      ($30F8),SP          
760A: 20 3E           JR      NZ,$764A            ; {}
760C: 01 E0 BE        LD      BC,$BEE0            
760F: 11 F5 75        LD      DE,$75F5            
7612: CD 3B 3C        CALL    $3C3B               
7615: CD DF 64        CALL    $64DF               ; {}
7618: CD E2 08        CALL    $08E2               
761B: CD B4 3B        CALL    $3BB4               
761E: F0 F0           LD      A,($F0)             
7620: C7              RST     0X00                
7621: 29              ADD     HL,HL               
7622: 76              HALT                        
7623: 3A              LD      A,(HLD)             
7624: 76              HALT                        
7625: 9D              SBC     L                   
7626: 76              HALT                        
7627: BE              CP      (HL)                
7628: 76              HALT                        
7629: F0 EE           LD      A,($EE)             
762B: 21 B0 C2        LD      HL,$C2B0            
762E: 09              ADD     HL,BC               
762F: 77              LD      (HL),A              
7630: F0 EC           LD      A,($EC)             
7632: 21 C0 C2        LD      HL,$C2C0            
7635: 09              ADD     HL,BC               
7636: 77              LD      (HL),A              
7637: C3 8D 3B        JP      $3B8D               
763A: CD 91 08        CALL    $0891               
763D: 20 55           JR      NZ,$7694            ; {}
763F: CD AF 3D        CALL    $3DAF               
7642: CD AE 65        CALL    $65AE               ; {}
7645: C6 12           ADD     $12                 
7647: FE 24           CP      $24                 
7649: 30 17           JR      NC,$7662            ; {}
764B: CD 9E 65        CALL    $659E               ; {}
764E: 50              LD      D,B                 
764F: 21 F9 75        LD      HL,$75F9            
7652: 19              ADD     HL,DE               
7653: 7E              LD      A,(HL)              
7654: 21 80 C3        LD      HL,$C380            
7657: 09              ADD     HL,BC               
7658: 73              LD      (HL),E              
7659: 21 40 C2        LD      HL,$C240            
765C: 09              ADD     HL,BC               
765D: 77              LD      (HL),A              
765E: 1E 18           LD      E,$18               
7660: 18 1E           JR      $7680               ; {}
7662: CD 9E 65        CALL    $659E               ; {}
7665: C6 12           ADD     $12                 
7667: FE 24           CP      $24                 
7669: 30 29           JR      NC,$7694            ; {}
766B: CD AE 65        CALL    $65AE               ; {}
766E: 50              LD      D,B                 
766F: 21 01 76        LD      HL,$7601            
7672: 19              ADD     HL,DE               
7673: 7E              LD      A,(HL)              
7674: 21 80 C3        LD      HL,$C380            
7677: 09              ADD     HL,BC               
7678: 73              LD      (HL),E              
7679: 21 50 C2        LD      HL,$C250            
767C: 09              ADD     HL,BC               
767D: 77              LD      (HL),A              
767E: 1E 10           LD      E,$10               
7680: CD 91 08        CALL    $0891               
7683: 73              LD      (HL),E              
7684: CD 9E 3B        CALL    $3B9E               
7687: 21 A0 C2        LD      HL,$C2A0            
768A: 09              ADD     HL,BC               
768B: 7E              LD      A,(HL)              
768C: E6 0F           AND     $0F                 
768E: 28 05           JR      Z,$7695             ; {}
7690: CD 91 08        CALL    $0891               
7693: 70              LD      (HL),B              
7694: C9              RET                         
7695: 3E 0A           LD      A,$0A               
7697: E0 F4           LD      ($FF00+$F4),A       
7699: CD 8D 3B        CALL    $3B8D               
769C: C9              RET                         
769D: CD 4B 65        CALL    $654B               ; {}
76A0: CD 91 08        CALL    $0891               
76A3: 20 0C           JR      NZ,$76B1            ; {}
76A5: 3E 07           LD      A,$07               
76A7: E0 F2           LD      ($FF00+$F2),A       
76A9: CD 91 08        CALL    $0891               
76AC: 36 20           LD      (HL),$20            
76AE: C3 8D 3B        JP      $3B8D               
76B1: CD 9E 3B        CALL    $3B9E               
76B4: 21 A0 C2        LD      HL,$C2A0            
76B7: 09              ADD     HL,BC               
76B8: 7E              LD      A,(HL)              
76B9: E6 0F           AND     $0F                 
76BB: 20 E8           JR      NZ,$76A5            ; {}
76BD: C9              RET                         
76BE: CD 91 08        CALL    $0891               
76C1: 20 3F           JR      NZ,$7702            ; {}
76C3: 21 80 C3        LD      HL,$C380            
76C6: 09              ADD     HL,BC               
76C7: 5E              LD      E,(HL)              
76C8: 50              LD      D,B                 
76C9: 21 FD 75        LD      HL,$75FD            
76CC: 19              ADD     HL,DE               
76CD: 7E              LD      A,(HL)              
76CE: 21 40 C2        LD      HL,$C240            
76D1: 09              ADD     HL,BC               
76D2: 77              LD      (HL),A              
76D3: 21 05 76        LD      HL,$7605            
76D6: 19              ADD     HL,DE               
76D7: 7E              LD      A,(HL)              
76D8: 21 50 C2        LD      HL,$C250            
76DB: 09              ADD     HL,BC               
76DC: 77              LD      (HL),A              
76DD: CD 4B 65        CALL    $654B               ; {}
76E0: 21 B0 C2        LD      HL,$C2B0            
76E3: 09              ADD     HL,BC               
76E4: 7E              LD      A,(HL)              
76E5: 21 00 C2        LD      HL,$C200            
76E8: 09              ADD     HL,BC               
76E9: BE              CP      (HL)                
76EA: 20 16           JR      NZ,$7702            ; {}
76EC: 21 C0 C2        LD      HL,$C2C0            
76EF: 09              ADD     HL,BC               
76F0: 7E              LD      A,(HL)              
76F1: 21 10 C2        LD      HL,$C210            
76F4: 09              ADD     HL,BC               
76F5: BE              CP      (HL)                
76F6: 20 0A           JR      NZ,$7702            ; {}
76F8: CD 91 08        CALL    $0891               
76FB: 36 20           LD      (HL),$20            
76FD: CD 8D 3B        CALL    $3B8D               
7700: 36 01           LD      (HL),$01            
7702: C9              RET                         
7703: 6E              LD      L,(HL)              
7704: 00              NOP                         
7705: 6E              LD      L,(HL)              
7706: 20 66           JR      NZ,$776E            ; {}
7708: 20 64           JR      NZ,$776E            ; {}
770A: 20 64           JR      NZ,$7770            ; {}
770C: 00              NOP                         
770D: 66              LD      H,(HL)              
770E: 00              NOP                         
770F: 62              LD      H,D                 
7710: 00              NOP                         
7711: 62              LD      H,D                 
7712: 20 60           JR      NZ,$7774            ; {}
7714: 00              NOP                         
7715: 60              LD      H,B                 
7716: 20 08           JR      NZ,$7720            ; {}
7718: F8 00           LD      HL,SP+$00           
771A: 00              NOP                         
771B: 00              NOP                         
771C: 00              NOP                         
771D: F8 08           LD      HL,SP+$08           
771F: 20 E0           JR      NZ,$7701            ; {}
7721: 00              NOP                         
7722: 00              NOP                         
7723: 00              NOP                         
7724: 00              NOP                         
7725: E0 20           LD      ($FF00+$20),A       
7727: 11 03 77        LD      DE,$7703            
772A: CD 3B 3C        CALL    $3C3B               
772D: CD DF 64        CALL    $64DF               ; {}
7730: CD 01 65        CALL    $6501               ; {}
7733: CD 4B 65        CALL    $654B               ; {}
7736: CD 9E 3B        CALL    $3B9E               
7739: 21 90 C2        LD      HL,$C290            
773C: 09              ADD     HL,BC               
773D: 7E              LD      A,(HL)              
773E: C7              RST     0X00                
773F: 47              LD      B,A                 
7740: 77              LD      (HL),A              
7741: 5F              LD      E,A                 
7742: 77              LD      (HL),A              
7743: 8F              ADC     A,A                 
7744: 77              LD      (HL),A              
7745: BD              CP      L                   
7746: 77              LD      (HL),A              
7747: 21 E0 C2        LD      HL,$C2E0            
774A: 09              ADD     HL,BC               
774B: 7E              LD      A,(HL)              
774C: A7              AND     A                   
774D: 20 0E           JR      NZ,$775D            ; {}
774F: CD 8D 3B        CALL    $3B8D               
7752: 21 B0 C2        LD      HL,$C2B0            
7755: 09              ADD     HL,BC               
7756: 36 01           LD      (HL),$01            
7758: CD 8C 08        CALL    $088C               
775B: 36 20           LD      (HL),$20            
775D: 18 1F           JR      $777E               ; {}
775F: CD 8C 08        CALL    $088C               
7762: 20 15           JR      NZ,$7779            ; {}
7764: 21 B0 C2        LD      HL,$C2B0            
7767: 09              ADD     HL,BC               
7768: 7E              LD      A,(HL)              
7769: 21 90 C2        LD      HL,$C290            
776C: 09              ADD     HL,BC               
776D: 86              ADD     A,(HL)              
776E: 77              LD      (HL),A              
776F: 21 E0 C2        LD      HL,$C2E0            
7772: 09              ADD     HL,BC               
7773: 36 30           LD      (HL),$30            
7775: CD 39 78        CALL    $7839               ; {}
7778: C9              RET                         
7779: 7E              LD      A,(HL)              
777A: E6 02           AND     $02                 
777C: 20 09           JR      NZ,$7787            ; {}
777E: 3E FF           LD      A,$FF               
7780: CD 87 3B        CALL    $3B87               
7783: CD 39 78        CALL    $7839               ; {}
7786: C9              RET                         
7787: AF              XOR     A                   
7788: CD 87 3B        CALL    $3B87               
778B: CD 39 78        CALL    $7839               ; {}
778E: C9              RET                         
778F: AF              XOR     A                   
7790: CD 87 3B        CALL    $3B87               
7793: CD 8C 08        CALL    $088C               
7796: FE 02           CP      $02                 
7798: 30 1F           JR      NC,$77B9            ; {}
779A: 7E              LD      A,(HL)              
779B: FE 01           CP      $01                 
779D: 28 06           JR      Z,$77A5             ; {}
779F: 36 18           LD      (HL),$18            
77A1: CD 39 78        CALL    $7839               ; {}
77A4: C9              RET                         
77A5: 21 B0 C2        LD      HL,$C2B0            
77A8: 09              ADD     HL,BC               
77A9: 7E              LD      A,(HL)              
77AA: 21 90 C2        LD      HL,$C290            
77AD: 09              ADD     HL,BC               
77AE: 86              ADD     A,(HL)              
77AF: 77              LD      (HL),A              
77B0: FE 01           CP      $01                 
77B2: 20 05           JR      NZ,$77B9            ; {}
77B4: CD 8C 08        CALL    $088C               
77B7: 36 20           LD      (HL),$20            
77B9: CD 39 78        CALL    $7839               ; {}
77BC: C9              RET                         
77BD: CD B4 3B        CALL    $3BB4               
77C0: CD 8C 08        CALL    $088C               
77C3: FE 28           CP      $28                 
77C5: 28 26           JR      Z,$77ED             ; {}
77C7: FE 02           CP      $02                 
77C9: 30 66           JR      NC,$7831            ; {}
77CB: 7E              LD      A,(HL)              
77CC: FE 01           CP      $01                 
77CE: 28 11           JR      Z,$77E1             ; {}
77D0: 36 40           LD      (HL),$40            
77D2: CD BE 65        CALL    $65BE               ; {}
77D5: 21 80 C3        LD      HL,$C380            
77D8: 09              ADD     HL,BC               
77D9: 77              LD      (HL),A              
77DA: 3C              INC     A                   
77DB: 21 B0 C3        LD      HL,$C3B0            
77DE: 09              ADD     HL,BC               
77DF: 77              LD      (HL),A              
77E0: C9              RET                         
77E1: 21 B0 C2        LD      HL,$C2B0            
77E4: 09              ADD     HL,BC               
77E5: 36 FF           LD      (HL),$FF            
77E7: 21 90 C2        LD      HL,$C290            
77EA: 09              ADD     HL,BC               
77EB: 35              DEC     (HL)                
77EC: C9              RET                         
77ED: 3E 22           LD      A,$22               
77EF: CD 01 3C        CALL    $3C01               
77F2: 38 3D           JR      C,$7831             ; {}
77F4: C5              PUSH    BC                  
77F5: F0 D9           LD      A,($D9)             
77F7: 21 80 C3        LD      HL,$C380            
77FA: 19              ADD     HL,DE               
77FB: 77              LD      (HL),A              
77FC: 4F              LD      C,A                 
77FD: 21 17 77        LD      HL,$7717            
7800: 09              ADD     HL,BC               
7801: F0 D7           LD      A,($D7)             
7803: 86              ADD     A,(HL)              
7804: 21 00 C2        LD      HL,$C200            
7807: 19              ADD     HL,DE               
7808: 77              LD      (HL),A              
7809: 21 1B 77        LD      HL,$771B            
780C: 09              ADD     HL,BC               
780D: F0 D8           LD      A,($D8)             
780F: 86              ADD     A,(HL)              
7810: 21 10 C2        LD      HL,$C210            
7813: 19              ADD     HL,DE               
7814: 77              LD      (HL),A              
7815: 21 1F 77        LD      HL,$771F            
7818: 09              ADD     HL,BC               
7819: 7E              LD      A,(HL)              
781A: 21 40 C2        LD      HL,$C240            
781D: 19              ADD     HL,DE               
781E: 77              LD      (HL),A              
781F: 21 23 77        LD      HL,$7723            
7822: 09              ADD     HL,BC               
7823: 7E              LD      A,(HL)              
7824: 21 50 C2        LD      HL,$C250            
7827: 19              ADD     HL,DE               
7828: 77              LD      (HL),A              
7829: C1              POP     BC                  
782A: F0 D9           LD      A,($D9)             
782C: 21 B0 C3        LD      HL,$C3B0            
782F: 19              ADD     HL,DE               
7830: 77              LD      (HL),A              
7831: 21 40 C3        LD      HL,$C340            
7834: 09              ADD     HL,BC               
7835: 3E 02           LD      A,$02               
7837: 77              LD      (HL),A              
7838: C9              RET                         
7839: 21 40 C3        LD      HL,$C340            
783C: 09              ADD     HL,BC               
783D: 36 42           LD      (HL),$42            
783F: C9              RET                         
7840: 00              NOP                         
7841: D8              RET     C                   
7842: 60              LD      H,B                 
7843: 00              NOP                         
7844: 00              NOP                         
7845: E0 60           LD      ($FF00+$60),A       
7847: 20 00           JR      NZ,$7849            ; {}
7849: 28 60           JR      Z,$78AB             ; {}
784B: 00              NOP                         
784C: 00              NOP                         
784D: 30 60           JR      NC,$78AF            ; {}
784F: 20 D8           JR      NZ,$7829            ; {}
7851: 00              NOP                         
7852: 62              LD      H,D                 
7853: 00              NOP                         
7854: D8              RET     C                   
7855: 08 62 20        LD      ($2062),SP          
7858: 28 00           JR      Z,$785A             ; {}
785A: 62              LD      H,D                 
785B: 00              NOP                         
785C: 28 08           JR      Z,$7866             ; {}
785E: 62              LD      H,D                 
785F: 20 F0           JR      NZ,$7851            ; {}
7861: F0 6A           LD      A,($6A)             
7863: 00              NOP                         
7864: F0 F8           LD      A,($F8)             
7866: 6A              LD      L,D                 
7867: 60              LD      H,B                 
7868: F0 10           LD      A,($10)             
786A: 6A              LD      L,D                 
786B: 40              LD      B,B                 
786C: F0 18           LD      A,($18)             
786E: 6A              LD      L,D                 
786F: 20 10           JR      NZ,$7881            ; {}
7871: F0 6A           LD      A,($6A)             
7873: 40              LD      B,B                 
7874: 10 F8           ;;STOP    $F8                 
7876: 6A              LD      L,D                 
7877: 20 10           JR      NZ,$7889            ; {}
7879: 10 6A           ;;STOP    $6A                 
787B: 00              NOP                         
787C: 10 18           ;;STOP    $18                 
787E: 6A              LD      L,D                 
787F: 60              LD      H,B                 
7880: 00              NOP                         
7881: E8 60           ADD     SP,$60              
7883: 00              NOP                         
7884: 00              NOP                         
7885: F0 60           LD      A,($60)             
7887: 20 00           JR      NZ,$7889            ; {}
7889: 18 60           JR      $78EB               ; {}
788B: 00              NOP                         
788C: 00              NOP                         
788D: 20 60           JR      NZ,$78EF            ; {}
788F: 20 E8           JR      NZ,$7879            ; {}
7891: 00              NOP                         
7892: 62              LD      H,D                 
7893: 00              NOP                         
7894: E8 08           ADD     SP,$08              
7896: 62              LD      H,D                 
7897: 20 18           JR      NZ,$78B1            ; {}
7899: 00              NOP                         
789A: 62              LD      H,D                 
789B: 00              NOP                         
789C: 18 08           JR      $78A6               ; {}
789E: 62              LD      H,D                 
789F: 20 F0           JR      NZ,$7891            ; {}
78A1: F0 FF           LD      A,($FF)             
78A3: 00              NOP                         
78A4: F0 F8           LD      A,($F8)             
78A6: FF              RST     0X38                
78A7: 00              NOP                         
78A8: F0 10           LD      A,($10)             
78AA: FF              RST     0X38                
78AB: 00              NOP                         
78AC: F0 18           LD      A,($18)             
78AE: FF              RST     0X38                
78AF: 00              NOP                         
78B0: 10 F0           ;;STOP    $F0                 
78B2: FF              RST     0X38                
78B3: 00              NOP                         
78B4: 10 F8           ;;STOP    $F8                 
78B6: FF              RST     0X38                
78B7: 00              NOP                         
78B8: 10 10           ;;STOP    $10                 
78BA: FF              RST     0X38                
78BB: 00              NOP                         
78BC: 10 18           ;;STOP    $18                 
78BE: FF              RST     0X38                
78BF: 00              NOP                         
78C0: E0 E0           LD      ($FF00+$E0),A       
78C2: 68              LD      L,B                 
78C3: 00              NOP                         
78C4: E0 E8           LD      ($FF00+$E8),A       
78C6: 68              LD      L,B                 
78C7: 60              LD      H,B                 
78C8: 20 E0           JR      NZ,$78AA            ; {}
78CA: 68              LD      L,B                 
78CB: 40              LD      B,B                 
78CC: 20 E8           JR      NZ,$78B6            ; {}
78CE: 68              LD      L,B                 
78CF: 20 E0           JR      NZ,$78B1            ; {}
78D1: 20 68           JR      NZ,$793B            ; {}
78D3: 40              LD      B,B                 
78D4: E0 28           LD      ($FF00+$28),A       
78D6: 68              LD      L,B                 
78D7: 20 20           JR      NZ,$78F9            ; {}
78D9: 20 68           JR      NZ,$7943            ; {}
78DB: 00              NOP                         
78DC: 20 28           JR      NZ,$7906            ; {}
78DE: 68              LD      L,B                 
78DF: 60              LD      H,B                 
78E0: 00              NOP                         
78E1: F0 64           LD      A,($64)             
78E3: 00              NOP                         
78E4: 00              NOP                         
78E5: F8 64           LD      HL,SP+$64           
78E7: 20 F0           JR      NZ,$78D9            ; {}
78E9: 00              NOP                         
78EA: 66              LD      H,(HL)              
78EB: 00              NOP                         
78EC: F0 08           LD      A,($08)             
78EE: 66              LD      H,(HL)              
78EF: 20 00           JR      NZ,$78F1            ; {}
78F1: 10 64           ;;STOP    $64                 
78F3: 00              NOP                         
78F4: 00              NOP                         
78F5: 18 64           JR      $795B               ; {}
78F7: 20 10           JR      NZ,$7909            ; {}
78F9: 00              NOP                         
78FA: 66              LD      H,(HL)              
78FB: 00              NOP                         
78FC: 10 08           ;;STOP    $08                 
78FE: 66              LD      H,(HL)              
78FF: 20 E8           JR      NZ,$78E9            ; {}
7901: E8 68           ADD     SP,$68              
7903: 00              NOP                         
7904: E8 F0           ADD     SP,$F0              
7906: 68              LD      L,B                 
7907: 60              LD      H,B                 
7908: 18 E8           JR      $78F2               ; {}
790A: 68              LD      L,B                 
790B: 40              LD      B,B                 
790C: 18 F0           JR      $78FE               ; {}
790E: 68              LD      L,B                 
790F: 20 E8           JR      NZ,$78F9            ; {}
7911: 18 68           JR      $797B               ; {}
7913: 40              LD      B,B                 
7914: E8 20           ADD     SP,$20              
7916: 68              LD      L,B                 
7917: 20 18           JR      NZ,$7931            ; {}
7919: 18 68           JR      $7983               ; {}
791B: 00              NOP                         
791C: 18 20           JR      $793E               ; {}
791E: 68              LD      L,B                 
791F: 60              LD      H,B                 
7920: 00              NOP                         
7921: F0 FF           LD      A,($FF)             
7923: 00              NOP                         
7924: 00              NOP                         
7925: F8 FF           LD      HL,SP+$FF           
7927: 20 F0           JR      NZ,$7919            ; {}
7929: 00              NOP                         
792A: FF              RST     0X38                
792B: 00              NOP                         
792C: F0 08           LD      A,($08)             
792E: FF              RST     0X38                
792F: 20 00           JR      NZ,$7931            ; {}
7931: 10 FF           ;;STOP    $FF                 
7933: 00              NOP                         
7934: 00              NOP                         
7935: 18 FF           JR      $7936               ; {}
7937: 20 10           JR      NZ,$7949            ; {}
7939: 00              NOP                         
793A: FF              RST     0X38                
793B: 00              NOP                         
793C: 10 08           ;;STOP    $08                 
793E: FF              RST     0X38                
793F: 20 CD           JR      NZ,$790E            ; {}
7941: DF              RST     0X18                
7942: 64              LD      H,H                 
7943: F0 E7           LD      A,($E7)             
7945: 1F              RRA                         
7946: 1F              RRA                         
7947: 1F              RRA                         
7948: E6 03           AND     $03                 
794A: 5F              LD      E,A                 
794B: 50              LD      D,B                 
794C: CB 23           SLA     1,E                 
794E: CB 12           RL      1,E                 
7950: CB 23           SLA     1,E                 
7952: CB 12           RL      1,E                 
7954: CB 23           SLA     1,E                 
7956: CB 12           RL      1,E                 
7958: CB 23           SLA     1,E                 
795A: CB 12           RL      1,E                 
795C: CB 23           SLA     1,E                 
795E: CB 12           RL      1,E                 
7960: CB 23           SLA     1,E                 
7962: CB 12           RL      1,E                 
7964: 21 40 78        LD      HL,$7840            
7967: 19              ADD     HL,DE               
7968: 0E 10           LD      C,$10               
796A: CD 26 3D        CALL    $3D26               
796D: 3E 10           LD      A,$10               
796F: CD D0 3D        CALL    $3DD0               
7972: C9              RET                         
7973: 5A              LD      E,D                 
7974: 00              NOP                         
7975: 5A              LD      E,D                 
7976: 20 5A           JR      NZ,$79D2            ; {}
7978: 10 5A           ;;STOP    $5A                 
797A: 30 11           JR      NC,$798D            ; {}
797C: 73              LD      (HL),E              
797D: 79              LD      A,C                 
797E: CD 3B 3C        CALL    $3C3B               
7981: CD DF 64        CALL    $64DF               ; {}
7984: CD 01 65        CALL    $6501               ; {}
7987: CD B4 3B        CALL    $3BB4               
798A: CD 4B 65        CALL    $654B               ; {}
798D: CD 9E 3B        CALL    $3B9E               
7990: 21 A0 C2        LD      HL,$C2A0            
7993: 09              ADD     HL,BC               
7994: 7E              LD      A,(HL)              
7995: E6 03           AND     $03                 
7997: 20 07           JR      NZ,$79A0            ; {}
7999: 7E              LD      A,(HL)              
799A: E6 0C           AND     $0C                 
799C: 20 0C           JR      NZ,$79AA            ; {}
799E: 18 12           JR      $79B2               ; {}
79A0: 21 40 C2        LD      HL,$C240            
79A3: 09              ADD     HL,BC               
79A4: 7E              LD      A,(HL)              
79A5: 2F              CPL                         
79A6: 3C              INC     A                   
79A7: 77              LD      (HL),A              
79A8: 18 08           JR      $79B2               ; {}
79AA: 21 50 C2        LD      HL,$C250            
79AD: 09              ADD     HL,BC               
79AE: 7E              LD      A,(HL)              
79AF: 2F              CPL                         
79B0: 3C              INC     A                   
79B1: 77              LD      (HL),A              
79B2: F0 E7           LD      A,($E7)             
79B4: 1F              RRA                         
79B5: 1F              RRA                         
79B6: 1F              RRA                         
79B7: E6 01           AND     $01                 
79B9: CD 87 3B        CALL    $3B87               
79BC: C9              RET                         
79BD: 58              LD      E,B                 
79BE: 00              NOP                         
79BF: 58              LD      E,B                 
79C0: 20 5A           JR      NZ,$7A1C            ; {}
79C2: 00              NOP                         
79C3: 5A              LD      E,D                 
79C4: 20 10           JR      NZ,$79D6            ; {}
79C6: F0 10           LD      A,($10)             
79C8: F0 10           LD      A,($10)             
79CA: 10 F0           ;;STOP    $F0                 
79CC: F0 11           LD      A,($11)             
79CE: BD              CP      L                   
79CF: 79              LD      A,C                 
79D0: CD 3B 3C        CALL    $3C3B               
79D3: CD DF 64        CALL    $64DF               ; {}
79D6: CD 01 65        CALL    $6501               ; {}
79D9: CD B4 3B        CALL    $3BB4               
79DC: CD 4B 65        CALL    $654B               ; {}
79DF: CD 9E 3B        CALL    $3B9E               
79E2: 21 A0 C2        LD      HL,$C2A0            
79E5: 09              ADD     HL,BC               
79E6: 7E              LD      A,(HL)              
79E7: E6 03           AND     $03                 
79E9: 28 03           JR      Z,$79EE             ; {}
79EB: CD 83 7A        CALL    $7A83               ; {}
79EE: 7E              LD      A,(HL)              
79EF: E6 0C           AND     $0C                 
79F1: 28 03           JR      Z,$79F6             ; {}
79F3: CD 88 7A        CALL    $7A88               ; {}
79F6: F0 F0           LD      A,($F0)             
79F8: A7              AND     A                   
79F9: 20 2D           JR      NZ,$7A28            ; {}
79FB: 21 10 C3        LD      HL,$C310            
79FE: 09              ADD     HL,BC               
79FF: 7E              LD      A,(HL)              
7A00: E6 80           AND     $80                 
7A02: 28 1B           JR      Z,$7A1F             ; {}
7A04: AF              XOR     A                   
7A05: 77              LD      (HL),A              
7A06: CD AF 3D        CALL    $3DAF               
7A09: 21 90 C2        LD      HL,$C290            
7A0C: 09              ADD     HL,BC               
7A0D: 34              INC     (HL)                
7A0E: CD 91 08        CALL    $0891               
7A11: CD ED 27        CALL    $27ED               
7A14: E6 3F           AND     $3F                 
7A16: C6 10           ADD     $10                 
7A18: 77              LD      (HL),A              
7A19: 3E 01           LD      A,$01               
7A1B: CD 87 3B        CALL    $3B87               
7A1E: C9              RET                         
7A1F: CD 84 65        CALL    $6584               ; {}
7A22: 21 20 C3        LD      HL,$C320            
7A25: 09              ADD     HL,BC               
7A26: 35              DEC     (HL)                
7A27: C9              RET                         
7A28: 21 D0 C3        LD      HL,$C3D0            
7A2B: 09              ADD     HL,BC               
7A2C: 34              INC     (HL)                
7A2D: 7E              LD      A,(HL)              
7A2E: E6 10           AND     $10                 
7A30: CB 3F           SRL     1,E                 
7A32: CB 3F           SRL     1,E                 
7A34: CB 3F           SRL     1,E                 
7A36: CB 3F           SRL     1,E                 
7A38: CD 87 3B        CALL    $3B87               
7A3B: A7              AND     A                   
7A3C: 20 44           JR      NZ,$7A82            ; {}
7A3E: CD 91 08        CALL    $0891               
7A41: 20 3F           JR      NZ,$7A82            ; {}
7A43: CD ED 27        CALL    $27ED               
7A46: E6 07           AND     $07                 
7A48: C6 10           ADD     $10                 
7A4A: 21 20 C3        LD      HL,$C320            
7A4D: 09              ADD     HL,BC               
7A4E: 77              LD      (HL),A              
7A4F: CD 84 65        CALL    $6584               ; {}
7A52: CD ED 27        CALL    $27ED               
7A55: E6 03           AND     $03                 
7A57: 5F              LD      E,A                 
7A58: 50              LD      D,B                 
7A59: 21 C5 79        LD      HL,$79C5            
7A5C: 19              ADD     HL,DE               
7A5D: 7E              LD      A,(HL)              
7A5E: 21 40 C2        LD      HL,$C240            
7A61: 09              ADD     HL,BC               
7A62: 77              LD      (HL),A              
7A63: 21 C9 79        LD      HL,$79C9            
7A66: 19              ADD     HL,DE               
7A67: 7E              LD      A,(HL)              
7A68: 21 50 C2        LD      HL,$C250            
7A6B: 09              ADD     HL,BC               
7A6C: 77              LD      (HL),A              
7A6D: CD ED 27        CALL    $27ED               
7A70: E6 01           AND     $01                 
7A72: 28 05           JR      Z,$7A79             ; {}
7A74: 3E 14           LD      A,$14               
7A76: CD 25 3C        CALL    $3C25               
7A79: 21 90 C2        LD      HL,$C290            
7A7C: 09              ADD     HL,BC               
7A7D: AF              XOR     A                   
7A7E: 77              LD      (HL),A              
7A7F: CD 87 3B        CALL    $3B87               
7A82: C9              RET                         
7A83: 21 40 C2        LD      HL,$C240            
7A86: 18 04           JR      $7A8C               ; {}
7A88: 21 40 C2        LD      HL,$C240            
7A8B: 09              ADD     HL,BC               
7A8C: 7E              LD      A,(HL)              
7A8D: 2F              CPL                         
7A8E: 3C              INC     A                   
7A8F: CB 2F           SRA     1,E                 
7A91: 77              LD      (HL),A              
7A92: C9              RET                         
7A93: 62              LD      H,D                 
7A94: 20 60           JR      NZ,$7AF6            ; {}
7A96: 20 66           JR      NZ,$7AFE            ; {}
7A98: 20 64           JR      NZ,$7AFE            ; {}
7A9A: 20 60           JR      NZ,$7AFC            ; {}
7A9C: 00              NOP                         
7A9D: 62              LD      H,D                 
7A9E: 00              NOP                         
7A9F: 64              LD      H,H                 
7AA0: 00              NOP                         
7AA1: 66              LD      H,(HL)              
7AA2: 00              NOP                         
7AA3: 68              LD      L,B                 
7AA4: 00              NOP                         
7AA5: 68              LD      L,B                 
7AA6: 20 6A           JR      NZ,$7B12            ; {}
7AA8: 00              NOP                         
7AA9: 6A              LD      L,D                 
7AAA: 20 6E           JR      NZ,$7B1A            ; {}
7AAC: 20 6C           JR      NZ,$7B1A            ; {}
7AAE: 20 6C           JR      NZ,$7B1C            ; {}
7AB0: 00              NOP                         
7AB1: 6E              LD      L,(HL)              
7AB2: 00              NOP                         
7AB3: 11 93 7A        LD      DE,$7A93            
7AB6: CD 3B 3C        CALL    $3C3B               
7AB9: CD DF 64        CALL    $64DF               ; {}
7ABC: CD 01 65        CALL    $6501               ; {}
7ABF: CD 4B 65        CALL    $654B               ; {}
7AC2: CD BC 5E        CALL    $5EBC               ; {}
7AC5: F0 F0           LD      A,($F0)             
7AC7: C7              RST     0X00                
7AC8: CC 7A 4B        CALL    Z,$4B7A             ; {}
7ACB: 7B              LD      A,E                 
7ACC: FA A2 C1        LD      A,($C1A2)           
7ACF: A7              AND     A                   
7AD0: C2 45 7B        JP      NZ,$7B45            ; {}
7AD3: CD 91 08        CALL    $0891               
7AD6: 20 43           JR      NZ,$7B1B            ; {}
7AD8: CD 8C 08        CALL    $088C               
7ADB: 20 4F           JR      NZ,$7B2C            ; {}
7ADD: FA 37 C1        LD      A,($C137)           
7AE0: FE 03           CP      $03                 
7AE2: 28 20           JR      Z,$7B04             ; {}
7AE4: CD ED 27        CALL    $27ED               
7AE7: A9              XOR     C                   
7AE8: E6 07           AND     $07                 
7AEA: C6 06           ADD     $06                 
7AEC: CD 30 3C        CALL    $3C30               
7AEF: F0 D7           LD      A,($D7)             
7AF1: 21 50 C2        LD      HL,$C250            
7AF4: CD 86 7B        CALL    $7B86               ; {}
7AF7: F0 D8           LD      A,($D8)             
7AF9: 21 40 C2        LD      HL,$C240            
7AFC: CD 86 7B        CALL    $7B86               ; {}
7AFF: CD BF 3B        CALL    $3BBF               
7B02: 18 2F           JR      $7B33               ; {}
7B04: CD 9E 65        CALL    $659E               ; {}
7B07: C6 24           ADD     $24                 
7B09: FE 48           CP      $48                 
7B0B: 30 26           JR      NC,$7B33            ; {}
7B0D: CD AE 65        CALL    $65AE               ; {}
7B10: C6 24           ADD     $24                 
7B12: FE 48           CP      $48                 
7B14: 30 1D           JR      NC,$7B33            ; {}
7B16: CD 91 08        CALL    $0891               
7B19: 36 20           LD      (HL),$20            
7B1B: CD AF 3D        CALL    $3DAF               
7B1E: CD BD 7B        CALL    $7BBD               ; {}
7B21: 21 B0 C2        LD      HL,$C2B0            
7B24: 09              ADD     HL,BC               
7B25: 7E              LD      A,(HL)              
7B26: A7              AND     A                   
7B27: 28 1B           JR      Z,$7B44             ; {}
7B29: CD 99 7B        CALL    $7B99               ; {}
7B2C: CD AF 3D        CALL    $3DAF               
7B2F: CD BD 7B        CALL    $7BBD               ; {}
7B32: C9              RET                         
7B33: CD 9E 65        CALL    $659E               ; {}
7B36: CB 23           SLA     1,E                 
7B38: F0 E7           LD      A,($E7)             
7B3A: 1F              RRA                         
7B3B: 1F              RRA                         
7B3C: 1F              RRA                         
7B3D: 1F              RRA                         
7B3E: E6 01           AND     $01                 
7B40: 83              ADD     A,E                 
7B41: CD 87 3B        CALL    $3B87               
7B44: C9              RET                         
7B45: CD 8D 3B        CALL    $3B8D               
7B48: 36 01           LD      (HL),$01            
7B4A: C9              RET                         
7B4B: FA A2 C1        LD      A,($C1A2)           
7B4E: A7              AND     A                   
7B4F: 28 30           JR      Z,$7B81             ; {}
7B51: 21 60 C3        LD      HL,$C360            
7B54: 09              ADD     HL,BC               
7B55: 36 01           LD      (HL),$01            
7B57: CD B4 3B        CALL    $3BB4               
7B5A: 3E 04           LD      A,$04               
7B5C: CD 30 3C        CALL    $3C30               
7B5F: F0 D7           LD      A,($D7)             
7B61: 2F              CPL                         
7B62: 3C              INC     A                   
7B63: 21 50 C2        LD      HL,$C250            
7B66: 09              ADD     HL,BC               
7B67: 77              LD      (HL),A              
7B68: F0 D8           LD      A,($D8)             
7B6A: 2F              CPL                         
7B6B: 3C              INC     A                   
7B6C: 21 40 C2        LD      HL,$C240            
7B6F: 09              ADD     HL,BC               
7B70: 77              LD      (HL),A              
7B71: F0 E7           LD      A,($E7)             
7B73: 1F              RRA                         
7B74: 1F              RRA                         
7B75: 1F              RRA                         
7B76: 1F              RRA                         
7B77: E6 01           AND     $01                 
7B79: C6 04           ADD     $04                 
7B7B: 21 B0 C3        LD      HL,$C3B0            
7B7E: 09              ADD     HL,BC               
7B7F: 77              LD      (HL),A              
7B80: C9              RET                         
7B81: CD 8D 3B        CALL    $3B8D               
7B84: 70              LD      (HL),B              
7B85: C9              RET                         
7B86: 09              ADD     HL,BC               
7B87: 96              SUB     (HL)                
7B88: 28 0E           JR      Z,$7B98             ; {}
7B8A: CB 7F           BIT     1,E                 
7B8C: 28 06           JR      Z,$7B94             ; {}
7B8E: 35              DEC     (HL)                
7B8F: 35              DEC     (HL)                
7B90: 35              DEC     (HL)                
7B91: 35              DEC     (HL)                
7B92: 18 04           JR      $7B98               ; {}
7B94: 34              INC     (HL)                
7B95: 34              INC     (HL)                
7B96: 34              INC     (HL)                
7B97: 34              INC     (HL)                
7B98: C9              RET                         
7B99: CD 8C 08        CALL    $088C               
7B9C: 36 20           LD      (HL),$20            
7B9E: 21 B0 C2        LD      HL,$C2B0            
7BA1: 09              ADD     HL,BC               
7BA2: 36 00           LD      (HL),$00            
7BA4: 21 10 C2        LD      HL,$C210            
7BA7: 09              ADD     HL,BC               
7BA8: 7E              LD      A,(HL)              
7BA9: D6 48           SUB     $48                 
7BAB: 5F              LD      E,A                 
7BAC: 3E 48           LD      A,$48               
7BAE: 93              SUB     E                   
7BAF: 77              LD      (HL),A              
7BB0: 21 00 C2        LD      HL,$C200            
7BB3: 09              ADD     HL,BC               
7BB4: 7E              LD      A,(HL)              
7BB5: D6 50           SUB     $50                 
7BB7: 5F              LD      E,A                 
7BB8: 3E 50           LD      A,$50               
7BBA: 93              SUB     E                   
7BBB: 77              LD      (HL),A              
7BBC: C9              RET                         
7BBD: F0 E7           LD      A,($E7)             
7BBF: 1F              RRA                         
7BC0: 1F              RRA                         
7BC1: E6 01           AND     $01                 
7BC3: 28 0F           JR      Z,$7BD4             ; {}
7BC5: CD 9E 65        CALL    $659E               ; {}
7BC8: CB 3B           SRL     1,E                 
7BCA: 38 04           JR      C,$7BD0             ; {}
7BCC: 3E 06           LD      A,$06               
7BCE: 18 06           JR      $7BD6               ; {}
7BD0: 3E 07           LD      A,$07               
7BD2: 18 02           JR      $7BD6               ; {}
7BD4: 3E FF           LD      A,$FF               
7BD6: CD 87 3B        CALL    $3B87               
7BD9: 21 B0 C2        LD      HL,$C2B0            
7BDC: 09              ADD     HL,BC               
7BDD: 70              LD      (HL),B              
7BDE: CD 91 08        CALL    $0891               
7BE1: FE 01           CP      $01                 
7BE3: 20 05           JR      NZ,$7BEA            ; {}
7BE5: 21 B0 C2        LD      HL,$C2B0            
7BE8: 09              ADD     HL,BC               
7BE9: 34              INC     (HL)                
7BEA: C9              RET                         
7BEB: A6              AND     (HL)                
7BEC: 10 8E           ;;STOP    $8E                 
7BEE: 10 80           ;;STOP    $80                 
7BF0: 10 A6           ;;STOP    $A6                 
7BF2: 10 A9           ;;STOP    $A9                 
7BF4: 10 2A           ;;STOP    $2A                 
7BF6: 40              LD      B,B                 
7BF7: 2A              LD      A,(HLI)             
7BF8: 60              LD      H,B                 
7BF9: 00              NOP                         
7BFA: FC                              
7BFB: 22              LD      (HLI),A             
7BFC: 00              NOP                         
7BFD: 00              NOP                         
7BFE: 0C              INC     C                   
7BFF: 22              LD      (HLI),A             
7C00: 20 00           JR      NZ,$7C02            ; {}
7C02: FC                              
7C03: 22              LD      (HLI),A             
7C04: 40              LD      B,B                 
7C05: 00              NOP                         
7C06: 0C              INC     C                   
7C07: 22              LD      (HLI),A             
7C08: 60              LD      H,B                 
7C09: 0F              RRCA                        
7C0A: 0F              RRCA                        
7C0B: 10 11           ;;STOP    $11                 
7C0D: 11 11 10        LD      DE,$1011            
7C10: 0F              RRCA                        
7C11: 00              NOP                         
7C12: 00              NOP                         
7C13: 01 02 02        LD      BC,$0202            
7C16: 02              LD      (BC),A              
7C17: 01 00 21        LD      BC,$2100            
7C1A: 09              ADD     HL,BC               
7C1B: 7C              LD      A,H                 
7C1C: F0 F9           LD      A,($F9)             
7C1E: A7              AND     A                   
7C1F: 28 03           JR      Z,$7C24             ; {}
7C21: 21 11 7C        LD      HL,$7C11            
7C24: F0 E7           LD      A,($E7)             
7C26: 1F              RRA                         
7C27: 1F              RRA                         
7C28: 1F              RRA                         
7C29: E6 07           AND     $07                 
7C2B: 5F              LD      E,A                 
7C2C: 50              LD      D,B                 
7C2D: 19              ADD     HL,DE               
7C2E: 7E              LD      A,(HL)              
7C2F: 21 10 C3        LD      HL,$C310            
7C32: 09              ADD     HL,BC               
7C33: 77              LD      (HL),A              
7C34: F0 F1           LD      A,($F1)             
7C36: FE 05           CP      $05                 
7C38: 20 08           JR      NZ,$7C42            ; {}
7C3A: 11 E1 7B        LD      DE,$7BE1            
7C3D: CD 3B 3C        CALL    $3C3B               
7C40: 18 06           JR      $7C48               ; {}
7C42: 11 EB 7B        LD      DE,$7BEB            
7C45: CD D0 3C        CALL    $3CD0               
7C48: F0 E7           LD      A,($E7)             
7C4A: E6 08           AND     $08                 
7C4C: 5F              LD      E,A                 
7C4D: 50              LD      D,B                 
7C4E: 21 F9 7B        LD      HL,$7BF9            
7C51: 19              ADD     HL,DE               
7C52: 0E 02           LD      C,$02               
7C54: CD 26 3D        CALL    $3D26               
7C57: 3E 01           LD      A,$01               
7C59: CD D0 3D        CALL    $3DD0               
7C5C: CD BA 3D        CALL    $3DBA               
7C5F: CD DF 64        CALL    $64DF               ; {}
7C62: F0 F9           LD      A,($F9)             
7C64: A7              AND     A                   
7C65: 20 06           JR      NZ,$7C6D            ; {}
7C67: F0 A2           LD      A,($A2)             
7C69: FE 0C           CP      $0C                 
7C6B: 38 3A           JR      C,$7CA7             ; {}
7C6D: CD D5 3B        CALL    $3BD5               
7C70: 30 35           JR      NC,$7CA7            ; {}
7C72: CD 88 3F        CALL    $3F88               
7C75: CD E5 65        CALL    $65E5               ; {}
7C78: 3E 01           LD      A,$01               
7C7A: E0 F3           LD      ($FF00+$F3),A       
7C7C: F0 F1           LD      A,($F1)             
7C7E: C7              RST     0X00                
7C7F: A2              AND     D                   
7C80: 7C              LD      A,H                 
7C81: A8              XOR     B                   
7C82: 7C              LD      A,H                 
7C83: B9              CP      C                   
7C84: 7C              LD      A,H                 
7C85: A2              AND     D                   
7C86: 7C              LD      A,H                 
7C87: 8B              ADC     A,E                 
7C88: 7C              LD      A,H                 
7C89: 98              SBC     B                   
7C8A: 7C              LD      A,H                 
7C8B: FA 93 DB        LD      A,($DB93)           
7C8E: C6 18           ADD     $18                 
7C90: 30 02           JR      NC,$7C94            ; {}
7C92: 3E FF           LD      A,$FF               
7C94: EA 93 DB        LD      ($DB93),A           
7C97: C9              RET                         
7C98: FA 45 DB        LD      A,($DB45)           
7C9B: C6 10           ADD     $10                 
7C9D: 27              DAA                         
7C9E: EA 45 DB        LD      ($DB45),A           
7CA1: C9              RET                         
7CA2: 3E 0A           LD      A,$0A               
7CA4: EA 90 DB        LD      ($DB90),A           
7CA7: C9              RET                         
7CA8: 16 0C           LD      D,$0C               
7CAA: CD 95 3E        CALL    $3E95               
7CAD: 3E 0B           LD      A,$0B               
7CAF: E0 A5           LD      ($FF00+$A5),A       
7CB1: 21 76 DB        LD      HL,$DB76            
7CB4: 11 4C DB        LD      DE,$DB4C            
7CB7: 18 06           JR      $7CBF               ; {}
7CB9: 21 77 DB        LD      HL,$DB77            
7CBC: 11 4D DB        LD      DE,$DB4D            
7CBF: 1A              LD      A,(DE)              
7CC0: BE              CP      (HL)                
7CC1: 30 08           JR      NC,$7CCB            ; {}
7CC3: C6 10           ADD     $10                 
7CC5: 27              DAA                         
7CC6: BE              CP      (HL)                
7CC7: 38 01           JR      C,$7CCA             ; {}
7CC9: 7E              LD      A,(HL)              
7CCA: 12              LD      (DE),A              
7CCB: C9              RET                         
7CCC: 56              LD      D,(HL)              
7CCD: 00              NOP                         
7CCE: 56              LD      D,(HL)              
7CCF: 20 CD           JR      NZ,$7C9E            ; {}
7CD1: DC 7C 11        CALL    C,$117C             
7CD4: CC 7C CD        CALL    Z,$CD7C             
7CD7: D0              RET     NC                  
7CD8: 3C              INC     A                   
7CD9: C3 05 7D        JP      $7D05               ; {}
7CDC: F0 F7           LD      A,($F7)             
7CDE: FE 0A           CP      $0A                 
7CE0: C0              RET     NZ                  
7CE1: F0 F6           LD      A,($F6)             
7CE3: FE 97           CP      $97                 
7CE5: 28 03           JR      Z,$7CEA             ; {}
7CE7: FE 98           CP      $98                 
7CE9: C0              RET     NZ                  
7CEA: FA 7F DB        LD      A,($DB7F)           
7CED: A7              AND     A                   
7CEE: C8              RET     Z                   
7CEF: 3E FF           LD      A,$FF               
7CF1: E0 F1           LD      ($FF00+$F1),A       
7CF3: C9              RET                         
7CF4: 52              LD      D,D                 
7CF5: 00              NOP                         
7CF6: 52              LD      D,D                 
7CF7: 20 54           JR      NZ,$7D4D            ; {}
7CF9: 00              NOP                         
7CFA: 54              LD      D,H                 
7CFB: 20 CD           JR      NZ,$7CCA            ; {}
7CFD: DC 7C 11        CALL    C,$117C             
7D00: F4                              
7D01: 7C              LD      A,H                 
7D02: CD 3B 3C        CALL    $3C3B               
7D05: 21 AE C1        LD      HL,$C1AE            
7D08: 34              INC     (HL)                
7D09: CD DF 64        CALL    $64DF               ; {}
7D0C: CD 84 65        CALL    $6584               ; {}
7D0F: 21 20 C3        LD      HL,$C320            
7D12: 09              ADD     HL,BC               
7D13: 35              DEC     (HL)                
7D14: 35              DEC     (HL)                
7D15: 35              DEC     (HL)                
7D16: 21 10 C3        LD      HL,$C310            
7D19: 09              ADD     HL,BC               
7D1A: 7E              LD      A,(HL)              
7D1B: E6 80           AND     $80                 
7D1D: E0 E8           LD      ($FF00+$E8),A       
7D1F: 28 06           JR      Z,$7D27             ; {}
7D21: 70              LD      (HL),B              
7D22: 21 20 C3        LD      HL,$C320            
7D25: 09              ADD     HL,BC               
7D26: 70              LD      (HL),B              
7D27: F0 EB           LD      A,($EB)             
7D29: FE 1B           CP      $1B                 
7D2B: 20 61           JR      NZ,$7D8E            ; {}
7D2D: 21 20 C4        LD      HL,$C420            
7D30: 09              ADD     HL,BC               
7D31: 7E              LD      A,(HL)              
7D32: FE 08           CP      $08                 
7D34: 20 58           JR      NZ,$7D8E            ; {}
7D36: 70              LD      (HL),B              
7D37: 21 60 C4        LD      HL,$C460            
7D3A: 09              ADD     HL,BC               
7D3B: 7E              LD      A,(HL)              
7D3C: E5              PUSH    HL                  
7D3D: F5              PUSH    AF                  
7D3E: 21 A0 C3        LD      HL,$C3A0            
7D41: 09              ADD     HL,BC               
7D42: 36 1C           LD      (HL),$1C            
7D44: CD 26 38        CALL    $3826               
7D47: F1              POP     AF                  
7D48: E1              POP     HL                  
7D49: 77              LD      (HL),A              
7D4A: 21 00 C2        LD      HL,$C200            
7D4D: 09              ADD     HL,BC               
7D4E: 7E              LD      A,(HL)              
7D4F: D6 04           SUB     $04                 
7D51: 77              LD      (HL),A              
7D52: CD AF 3D        CALL    $3DAF               
7D55: 21 10 C4        LD      HL,$C410            
7D58: 09              ADD     HL,BC               
7D59: 70              LD      (HL),B              
7D5A: 21 20 C3        LD      HL,$C320            
7D5D: 09              ADD     HL,BC               
7D5E: 36 20           LD      (HL),$20            
7D60: 3E 1C           LD      A,$1C               
7D62: CD 01 3C        CALL    $3C01               
7D65: 38 27           JR      C,$7D8E             ; {}
7D67: 21 60 C4        LD      HL,$C460            
7D6A: 09              ADD     HL,BC               
7D6B: 7E              LD      A,(HL)              
7D6C: 21 60 C4        LD      HL,$C460            
7D6F: 19              ADD     HL,DE               
7D70: 77              LD      (HL),A              
7D71: F0 D7           LD      A,($D7)             
7D73: C6 08           ADD     $08                 
7D75: 21 00 C2        LD      HL,$C200            
7D78: 19              ADD     HL,DE               
7D79: 77              LD      (HL),A              
7D7A: F0 D8           LD      A,($D8)             
7D7C: 21 10 C2        LD      HL,$C210            
7D7F: 19              ADD     HL,DE               
7D80: 77              LD      (HL),A              
7D81: F0 DA           LD      A,($DA)             
7D83: 21 10 C3        LD      HL,$C310            
7D86: 19              ADD     HL,DE               
7D87: 77              LD      (HL),A              
7D88: 21 20 C3        LD      HL,$C320            
7D8B: 19              ADD     HL,DE               
7D8C: 36 20           LD      (HL),$20            
7D8E: CD 01 65        CALL    $6501               ; {}
7D91: 21 00 C3        LD      HL,$C300            
7D94: 09              ADD     HL,BC               
7D95: 7E              LD      A,(HL)              
7D96: A7              AND     A                   
7D97: 20 12           JR      NZ,$7DAB            ; {}
7D99: F0 F0           LD      A,($F0)             
7D9B: E6 01           AND     $01                 
7D9D: 21 B0 C3        LD      HL,$C3B0            
7DA0: 09              ADD     HL,BC               
7DA1: 77              LD      (HL),A              
7DA2: 3D              DEC     A                   
7DA3: 20 06           JR      NZ,$7DAB            ; {}
7DA5: 21 00 C3        LD      HL,$C300            
7DA8: 09              ADD     HL,BC               
7DA9: 36 08           LD      (HL),$08            
7DAB: F0 F0           LD      A,($F0)             
7DAD: FE 04           CP      $04                 
7DAF: 28 0B           JR      Z,$7DBC             ; {}
7DB1: 21 80 C4        LD      HL,$C480            
7DB4: 09              ADD     HL,BC               
7DB5: 7E              LD      A,(HL)              
7DB6: A7              AND     A                   
7DB7: 20 03           JR      NZ,$7DBC            ; {}
7DB9: CD B4 3B        CALL    $3BB4               
7DBC: F0 F0           LD      A,($F0)             
7DBE: C7              RST     0X00                
7DBF: FC                              
7DC0: 7D              LD      A,L                 
7DC1: C9              RET                         
7DC2: 7D              LD      A,L                 
7DC3: 0F              RRCA                        
7DC4: 7E              LD      A,(HL)              
7DC5: 3C              INC     A                   
7DC6: 7E              LD      A,(HL)              
7DC7: 49              LD      C,C                 
7DC8: 7E              LD      A,(HL)              
7DC9: CD 91 08        CALL    $0891               
7DCC: 20 18           JR      NZ,$7DE6            ; {}
7DCE: 36 10           LD      (HL),$10            
7DD0: CD AF 3D        CALL    $3DAF               
7DD3: CD ED 27        CALL    $27ED               
7DD6: E6 0F           AND     $0F                 
7DD8: 20 08           JR      NZ,$7DE2            ; {}
7DDA: CD 91 08        CALL    $0891               
7DDD: 36 50           LD      (HL),$50            
7DDF: C3 8D 3B        JP      $3B8D               
7DE2: CD 8D 3B        CALL    $3B8D               
7DE5: 70              LD      (HL),B              
7DE6: CD 4B 65        CALL    $654B               ; {}
7DE9: CD 8C 08        CALL    $088C               
7DEC: C0              RET     NZ                  
7DED: 21 10 C4        LD      HL,$C410            
7DF0: 09              ADD     HL,BC               
7DF1: 36 02           LD      (HL),$02            
7DF3: CD 9E 3B        CALL    $3B9E               
7DF6: 21 10 C4        LD      HL,$C410            
7DF9: 09              ADD     HL,BC               
7DFA: 70              LD      (HL),B              
7DFB: C9              RET                         
7DFC: CD E6 7D        CALL    $7DE6               ; {}
7DFF: CD 91 08        CALL    $0891               
7E02: 20 0A           JR      NZ,$7E0E            ; {}
7E04: 36 07           LD      (HL),$07            
7E06: CD 8D 3B        CALL    $3B8D               
7E09: 3E 04           LD      A,$04               
7E0B: CD 25 3C        CALL    $3C25               
7E0E: C9              RET                         
7E0F: CD 91 08        CALL    $0891               
7E12: 20 0F           JR      NZ,$7E23            ; {}
7E14: CD 8D 3B        CALL    $3B8D               
7E17: 3E 10           LD      A,$10               
7E19: CD 25 3C        CALL    $3C25               
7E1C: 21 20 C3        LD      HL,$C320            
7E1F: 09              ADD     HL,BC               
7E20: 36 20           LD      (HL),$20            
7E22: C9              RET                         
7E23: CD 91 08        CALL    $0891               
7E26: 21 40 C2        LD      HL,$C240            
7E29: 09              ADD     HL,BC               
7E2A: E6 04           AND     $04                 
7E2C: 20 04           JR      NZ,$7E32            ; {}
7E2E: 36 08           LD      (HL),$08            
7E30: 18 02           JR      $7E34               ; {}
7E32: 36 F8           LD      (HL),$F8            
7E34: 21 50 C2        LD      HL,$C250            
7E37: 09              ADD     HL,BC               
7E38: 70              LD      (HL),B              
7E39: C3 E6 7D        JP      $7DE6               ; {}
7E3C: CD E6 7D        CALL    $7DE6               ; {}
7E3F: F0 E8           LD      A,($E8)             
7E41: A7              AND     A                   
7E42: 28 04           JR      Z,$7E48             ; {}
7E44: CD 8D 3B        CALL    $3B8D               
7E47: 70              LD      (HL),B              
7E48: C9              RET                         
7E49: CD 91 08        CALL    $0891               
7E4C: 20 1C           JR      NZ,$7E6A            ; {}
7E4E: 21 80 C4        LD      HL,$C480            
7E51: 09              ADD     HL,BC               
7E52: 36 30           LD      (HL),$30            
7E54: 3E 10           LD      A,$10               
7E56: CD 25 3C        CALL    $3C25               
7E59: 21 20 C3        LD      HL,$C320            
7E5C: 09              ADD     HL,BC               
7E5D: 36 20           LD      (HL),$20            
7E5F: 21 10 C3        LD      HL,$C310            
7E62: 09              ADD     HL,BC               
7E63: 34              INC     (HL)                
7E64: CD 8D 3B        CALL    $3B8D               
7E67: 36 03           LD      (HL),$03            
7E69: C9              RET                         
7E6A: F5              PUSH    AF                  
7E6B: 1F              RRA                         
7E6C: E6 07           AND     $07                 
7E6E: D6 04           SUB     $04                 
7E70: 5F              LD      E,A                 
7E71: F0 98           LD      A,($98)             
7E73: 93              SUB     E                   
7E74: 21 00 C2        LD      HL,$C200            
7E77: 09              ADD     HL,BC               
7E78: 77              LD      (HL),A              
7E79: F1              POP     AF                  
7E7A: 1F              RRA                         
7E7B: 1F              RRA                         
7E7C: E6 07           AND     $07                 
7E7E: D6 04           SUB     $04                 
7E80: 5F              LD      E,A                 
7E81: F0 99           LD      A,($99)             
7E83: 93              SUB     E                   
7E84: 21 10 C2        LD      HL,$C210            
7E87: 09              ADD     HL,BC               
7E88: 77              LD      (HL),A              
7E89: F0 A2           LD      A,($A2)             
7E8B: 21 10 C3        LD      HL,$C310            
7E8E: 09              ADD     HL,BC               
7E8F: 77              LD      (HL),A              
7E90: 3E 01           LD      A,$01               
7E92: EA 17 C1        LD      ($C117),A           
7E95: CD 9E 3B        CALL    $3B9E               
7E98: F0 CC           LD      A,($CC)             
7E9A: A7              AND     A                   
7E9B: 28 0F           JR      Z,$7EAC             ; {}
7E9D: CD A6 7E        CALL    $7EA6               ; {}
7EA0: CD A6 7E        CALL    $7EA6               ; {}
7EA3: CD A6 7E        CALL    $7EA6               ; {}
7EA6: CD 91 08        CALL    $0891               
7EA9: 28 01           JR      Z,$7EAC             ; {}
7EAB: 35              DEC     (HL)                
7EAC: C9              RET                         
7EAD: 7C              LD      A,H                 
7EAE: 00              NOP                         
7EAF: 7C              LD      A,H                 
7EB0: 20 7E           JR      NZ,$7F30            ; {}
7EB2: 00              NOP                         
7EB3: 7E              LD      A,(HL)              
7EB4: 20 11           JR      NZ,$7EC7            ; {}
7EB6: AD              XOR     L                   
7EB7: 7E              LD      A,(HL)              
7EB8: CD 3B 3C        CALL    $3C3B               
7EBB: CD DF 64        CALL    $64DF               ; {}
7EBE: CD 01 65        CALL    $6501               ; {}
7EC1: 21 D0 C2        LD      HL,$C2D0            
7EC4: 09              ADD     HL,BC               
7EC5: 7E              LD      A,(HL)              
7EC6: C7              RST     0X00                
7EC7: CB 7E           BIT     1,E                 
7EC9: E5              PUSH    HL                  
7ECA: 7E              LD      A,(HL)              
7ECB: CD 87 08        CALL    $0887               
7ECE: 20 0F           JR      NZ,$7EDF            ; {}
7ED0: CD BF 3B        CALL    $3BBF               
7ED3: 30 0A           JR      NC,$7EDF            ; {}
7ED5: 21 D0 C2        LD      HL,$C2D0            
7ED8: 09              ADD     HL,BC               
7ED9: 34              INC     (HL)                
7EDA: 21 D0 C3        LD      HL,$C3D0            
7EDD: 09              ADD     HL,BC               
7EDE: 70              LD      (HL),B              
7EDF: CD EB 3B        CALL    $3BEB               
7EE2: C3 77 7F        JP      $7F77               ; {}
7EE5: F0 CC           LD      A,($CC)             
7EE7: E6 30           AND     $30                 
7EE9: 28 15           JR      Z,$7F00             ; {}
7EEB: 21 D0 C3        LD      HL,$C3D0            
7EEE: 09              ADD     HL,BC               
7EEF: 34              INC     (HL)                
7EF0: 7E              LD      A,(HL)              
7EF1: FE 08           CP      $08                 
7EF3: 38 0B           JR      C,$7F00             ; {}
7EF5: CD 87 08        CALL    $0887               
7EF8: 36 15           LD      (HL),$15            
7EFA: 21 D0 C2        LD      HL,$C2D0            
7EFD: 09              ADD     HL,BC               
7EFE: 70              LD      (HL),B              
7EFF: C9              RET                         
7F00: 3E FF           LD      A,$FF               
7F02: E0 9D           LD      ($FF00+$9D),A       
7F04: 21 B0 C2        LD      HL,$C2B0            
7F07: 09              ADD     HL,BC               
7F08: 7E              LD      A,(HL)              
7F09: A7              AND     A                   
7F0A: 20 22           JR      NZ,$7F2E            ; {}
7F0C: 21 00 DB        LD      HL,$DB00            
7F0F: 58              LD      E,B                 
7F10: 7E              LD      A,(HL)              
7F11: FE 04           CP      $04                 
7F13: 20 12           JR      NZ,$7F27            ; {}
7F15: FA 44 DB        LD      A,($DB44)           
7F18: FE 02           CP      $02                 
7F1A: 30 12           JR      NC,$7F2E            ; {}
7F1C: 70              LD      (HL),B              
7F1D: 21 B0 C2        LD      HL,$C2B0            
7F20: 09              ADD     HL,BC               
7F21: FA 44 DB        LD      A,($DB44)           
7F24: 77              LD      (HL),A              
7F25: 18 07           JR      $7F2E               ; {}
7F27: 23              INC     HL                  
7F28: 1C              INC     E                   
7F29: 7B              LD      A,E                 
7F2A: FE 02           CP      $02                 
7F2C: 20 E2           JR      NZ,$7F10            ; {}
7F2E: FA 1C C1        LD      A,($C11C)           
7F31: FE 00           CP      $00                 
7F33: C0              RET     NZ                  
7F34: F0 EE           LD      A,($EE)             
7F36: E0 98           LD      ($FF00+$98),A       
7F38: F0 EF           LD      A,($EF)             
7F3A: E0 99           LD      ($FF00+$99),A       
7F3C: AF              XOR     A                   
7F3D: EA 46 C1        LD      ($C146),A           
7F40: E0 A2           LD      ($FF00+$A2),A       
7F42: CD DF 7F        CALL    $7FDF               ; {}
7F45: CD DF 7F        CALL    $7FDF               ; {}
7F48: C9              RET                         
7F49: 74              LD      (HL),H              
7F4A: 00              NOP                         
7F4B: 76              HALT                        
7F4C: 00              NOP                         
7F4D: 76              HALT                        
7F4E: 20 74           JR      NZ,$7FC4            ; {}
7F50: 20 44           JR      NZ,$7F96            ; {}
7F52: 00              NOP                         
7F53: 46              LD      B,(HL)              
7F54: 00              NOP                         
7F55: 46              LD      B,(HL)              
7F56: 20 44           JR      NZ,$7F9C            ; {}
7F58: 20 00           JR      NZ,$7F5A            ; {}
7F5A: 08 F8 00        LD      ($00F8),SP          
7F5D: F8 08           LD      HL,SP+$08           
7F5F: 11 49 7F        LD      DE,$7F49            
7F62: F0 F7           LD      A,($F7)             
7F64: FE 07           CP      $07                 
7F66: 20 03           JR      NZ,$7F6B            ; {}
7F68: 11 51 7F        LD      DE,$7F51            
7F6B: CD 3B 3C        CALL    $3C3B               
7F6E: CD DF 64        CALL    $64DF               ; {}
7F71: CD E2 08        CALL    $08E2               
7F74: CD B4 3B        CALL    $3BB4               
7F77: CD 4B 65        CALL    $654B               ; {}
7F7A: CD 9E 3B        CALL    $3B9E               
7F7D: 21 A0 C2        LD      HL,$C2A0            
7F80: 09              ADD     HL,BC               
7F81: 7E              LD      A,(HL)              
7F82: E6 03           AND     $03                 
7F84: 20 0F           JR      NZ,$7F95            ; {}
7F86: 7E              LD      A,(HL)              
7F87: E6 0C           AND     $0C                 
7F89: 28 12           JR      Z,$7F9D             ; {}
7F8B: 21 50 C2        LD      HL,$C250            
7F8E: 09              ADD     HL,BC               
7F8F: 7E              LD      A,(HL)              
7F90: EE F0           XOR     $F0                 
7F92: 77              LD      (HL),A              
7F93: 18 08           JR      $7F9D               ; {}
7F95: 21 40 C2        LD      HL,$C240            
7F98: 09              ADD     HL,BC               
7F99: 7E              LD      A,(HL)              
7F9A: EE F0           XOR     $F0                 
7F9C: 77              LD      (HL),A              
7F9D: 21 90 C2        LD      HL,$C290            
7FA0: 09              ADD     HL,BC               
7FA1: 7E              LD      A,(HL)              
7FA2: A7              AND     A                   
7FA3: 20 07           JR      NZ,$7FAC            ; {}
7FA5: CD ED 27        CALL    $27ED               
7FA8: E6 3F           AND     $3F                 
7FAA: 20 2D           JR      NZ,$7FD9            ; {}
7FAC: AF              XOR     A                   
7FAD: 21 50 C2        LD      HL,$C250            
7FB0: 09              ADD     HL,BC               
7FB1: 77              LD      (HL),A              
7FB2: CD ED 27        CALL    $27ED               
7FB5: E6 03           AND     $03                 
7FB7: 5F              LD      E,A                 
7FB8: 50              LD      D,B                 
7FB9: 21 59 7F        LD      HL,$7F59            
7FBC: 19              ADD     HL,DE               
7FBD: 7E              LD      A,(HL)              
7FBE: 21 40 C2        LD      HL,$C240            
7FC1: 09              ADD     HL,BC               
7FC2: 77              LD      (HL),A              
7FC3: A7              AND     A                   
7FC4: 20 13           JR      NZ,$7FD9            ; {}
7FC6: CD ED 27        CALL    $27ED               
7FC9: E6 01           AND     $01                 
7FCB: C6 04           ADD     $04                 
7FCD: 5F              LD      E,A                 
7FCE: 50              LD      D,B                 
7FCF: 21 59 7F        LD      HL,$7F59            
7FD2: 19              ADD     HL,DE               
7FD3: 7E              LD      A,(HL)              
7FD4: 21 50 C2        LD      HL,$C250            
7FD7: 09              ADD     HL,BC               
7FD8: 77              LD      (HL),A              
7FD9: 21 90 C2        LD      HL,$C290            
7FDC: 09              ADD     HL,BC               
7FDD: AF              XOR     A                   
7FDE: 77              LD      (HL),A              
7FDF: 21 40 C4        LD      HL,$C440            
7FE2: 09              ADD     HL,BC               
7FE3: 7E              LD      A,(HL)              
7FE4: 34              INC     (HL)                
7FE5: 1F              RRA                         
7FE6: 1F              RRA                         
7FE7: 1F              RRA                         
7FE8: 1F              RRA                         
7FE9: E6 01           AND     $01                 
7FEB: C3 87 3B        JP      $3B87               
7FEE: FF              RST     0X38                
7FEF: FF              RST     0X38                
7FF0: FF              RST     0X38                
7FF1: FF              RST     0X38                
7FF2: FF              RST     0X38                
7FF3: FF              RST     0X38                
7FF4: FF              RST     0X38                
7FF5: FF              RST     0X38                
7FF6: FF              RST     0X38                
7FF7: FF              RST     0X38                
7FF8: FF              RST     0X38                
7FF9: FF              RST     0X38                
7FFA: FF              RST     0X38                
7FFB: FF              RST     0X38                
7FFC: FF              RST     0X38                
7FFD: FF              RST     0X38                
7FFE: FF              RST     0X38                
7FFF: FF              RST     0X38                
```

