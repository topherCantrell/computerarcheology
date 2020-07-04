![RAM Use](TRS80Pyramid.jpg)

# RAM Use

>>> memory

| | | |
| --- | --- | --- |
| 4FF5:4FF6 | tmp1A7                | used in decoding the input |                   
| 4FF7      | tmp1A9                | used in comparing X to Y |                     
| 4FF8      | not1AA                | never used |
| 4FF9      | tmp1AB                | used in lots of places |                       
| 4FFA      | not1AC                | never used |
| 4FFB      | tmp1AD                | used in the phrase decoding |                  
| 4FFC      | not1AE                | never used |
| 4FFD      | not1AF                | never used |
| 4FFE      | not1B0                | never used |
| 4FFF      | not1B1                | never used |
| 5000      | tmp1B2                | used in word decoding |                        
| 5001      | verbWord              | input verb word number |                     
| 5002      | perpWord              | preposition word number |                     
| 5003      | prepGiven             | preposition given flag |                       
| 5004      | phrasePrep            | used in phrase decoding |                      
| 5005      | adjWord               | adjective word number |                        
| 5006      | commandTarg           | target object of input command |               
| 5007      | not1B9                | cleared before decode but never used |        
| 5008      | lsbAdj1               | screen LSB of 1st adjective |                  
| 5009      | lsbVerb               | screen LSB of verb |                           
| 500A      | lsbCursor             | screen lsb used in decoding the input line |   
| 500B      | lsbError              | screen lsb used for flashing error messages |  
| 500C      | lastChar              | last character printed to screen |             
| 500D      | VAR_OBJ_NUMBER        | variable object number |                       
| 500E:500F |  VAR_OBJ_DATA         | variable object data |                         
| 5010      | not1C2                | never used |
| 5011      | FIRST_NOUN_NUM        | first input noun number |                      
| 5012      | firstNounAdj          | first input noun adjective word number |
| 5013      | firstNounLSB          | first input noun screen LSB |                  
| 5014:5015 | FIRST_NOUN_DATA       | first input noun object data |                
| 5016      | firstNounParams       | first input noun parameter bits |             
| 5017      | SECOND_NOUN_NUM       | second input noun number |                     
| 5018      | secondNounAdj         | second input noun adjective word number |
| 5019      | secondNounLSB         | second input noun noun screen LSB |           
| 501A:501B | SECOND_NOUN_DATA      | second input noun object data |                
| 501C      | secondNounParams      | second input noun parameter bits |             
| 501D      | tmp1CF                | another screen pointer used in decode |       
| 501E      | tmp1DO                | used in making index of data fields |         
| 501F      | PHRASE_FORM           | decoded phrase form |                          
| 5020      | ACTIVE_OBJ_NUM        | active object |                                
| 5021:5022 | ACTIVE_OBJ_DATA       | active object data |                          
| 5023      | CUR_ROOM              | current room number |                         
| 5024:5025 | CUR_ROOM_DATA         | current room data |                          
| 5026:5027 | nextToken             | used in decoding input |                      
| 5028      | tmp1DA                | used in unpacking bytes |                      
| 5029      | tmp1DB                | used in unpacking bytes |                    
| 502A      | tmp1DC                | used in unpacking bytes |                     
| 502B      | tmp1DD                | used in unpacking bytes |                     
| 502C      | tmp1DE                | used in unpacking bytes |                      
| 502D      | tmp1DF                | used in unpacking bytes |                     
| 502E      | tmp1EO                | used in unpacking bytes |                      
| 502F      | tmp1E1                | used in making index of data fields |         
| 5030      | tmp1E2                | used in input processing |                    
| 5031      | tillMORE              | rows left until MORE prompt (not used here) |


Stack initialized to 7FFF
