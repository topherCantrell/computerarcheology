
from trac.wiki.macros import WikiMacroBase


class AssemblyCodeMacro(WikiMacroBase):
    
    def expand_macro(self, formatter, name, text):
        return "<pre class='ca_assembly'>"+processText(text)+"</pre>"
        
def isHex(c):
    if c>='0' and c<='9':
        return True
    if c>='A' and c<='F':
        return True
    if c>='a' and c<='f':
        return True
    
def processText(text):
    # Line-at-a-time
    textLines = text.splitlines()
    ln = 0
    si = len(textLines)
    while ln<si:
        textLine = textLines[ln]
        
        # If we encounter an assembler directive then don't process the labels.
        # The pure assembly uses "{ }" for code
        if len(textLine)>0 and textLine[0] == ".":
            break
        
        # We can do one anchor and one link on each line. Peel out the anchor first.
        # {*label} or {*}
        span = ""        
        i = textLine.find("{*")
        if i>=0:
            j = textLine.find("}",i)
            dest = textLine[i+2:j]
            if len(dest)==0:
                dest = textLine[0:4]
            span = "<span id='"+dest+"'></span>"
            textLine = textLine[0:i]+textLine[j+2:]           
        
        # Now for any link.
        # {---%/dest:label}
        i = textLine.find("{")
        if i>=0:
            j = textLine.find("}",i)
            dest = textLine[i+1:j]          
            
            # We are going to do some other substitutions. We'll need the line
            # without the instruction in it
            textLine = textLine[0:i] + textLine[j+1:]   
            
            # Count the '-' and peel them off the instruction. The count of these
            # determines the class name for CSS.
            classCount = 0
            while dest.startswith('-'):
                dest = dest[1:]
                classCount+=1
                          
            # The label can be explicitly different or the same as the dest. Get an explicit
            # label off the end of the instruction.     
            label = dest            
            i = dest.find(":")
            if i>=0:
                label = dest[i+1:]
                dest = dest[0:i]
                
            # Find the end of the opcode. We'll need this to adjust the spacing after substitution
            p = textLine.find(";")
            if p<0:
                p = len(textLine) # no comment ... start at the end of the line
            while p>0 and textLine[p-1]==' ':
                p -= 1 
                                    
            # Find the hex number beginning (if any)
            k = textLine.find("$")                
                
            # Find the end of the opcode if we need it
            if k<0 or dest.find('%')==0:                
                k=p
                kk = k # kk is one-past-end of number substitution
            else:
                # We are substituting over a number. Find one-past-end
                kk = k+1
                while isHex(textLine[kk]):
                    kk+=1
                    
            # k is now the start of the substitution and kk is one-past-end     
                
            # if the dest wasn't given use the replaced address                   
            if len(dest)==0:                    
                dest = textLine[k+1:kk]
                label = textLine[k:kk]
                
            # drop any leading '%' flag
            if dest[0]=='%':
                dest = dest[1:]
                 
            # Could be an absolute destination or a shorter '#' within the page
            preDest = ""
            if dest[0]=='/':
                dest = dest[1:]
            else:
                preDest = "#"
                                
            # Hover text will be whatever we replace
            hover = textLine[k:kk]           
             
            if len(label)==0:
                # Just a coloring span
                # The label will likely be longer than the address we replace. We need
                # to move any ";" to the left so they line up.
                remSpace = len(dest) - (kk-k)
                if remSpace<0:
                    remSpace = 0
                # Make the sub
                textLine = textLine[0:k]+"<span class='ca_codeLink"+str(classCount)+"' title='"+hover+"'>"+dest+"</span>"+textLine[kk:p]+textLine[p+remSpace:]
            else:       
                # The label will likely be longer than the address we replace. We need
                # to move any ";" to the left so they line up.
                remSpace = len(label) - (kk-k)
                if remSpace<0:
                    remSpace = 0
                # Here is the link
                textLine = textLine[0:k]+"<a class='ca_codeLink"+str(classCount)+"' href='"+preDest+dest+"' title='"+hover+"'>"+label+"</a>"+textLine[kk:p]+textLine[p+remSpace:]
                       
        # Combine any anchor with any link
        textLines[ln] = span+textLine
        
        # Next line
        ln += 1
    return "\n".join(textLines);  
        
        
        
        
#                                  s    ep
# 002D: 3A EB 20        LD      A,($20EB)           ; Number of credits in BCD        
        
if __name__=="__main__":
    text = """002A: CA 42 00        JP      Z,$0042             ; No ... skip registering the credit
;
; Handle bumping credit count
002D: 3A EB 20        LD      A,($20EB)           ; Number of credits in BCD
0030: FE 99           CP      $99                 ; 99 credits already?
0032: CA 3E 00        JP      Z,$003E             ; {} Yes ... ignore this (better than rolling over to 00)
0035: C6 01           ADD     A,$01               ; Bump number of credits
0037: 27              DAA                         ; Make it binary coded decimal
0038: 32 EB 20        LD      ($20EB),A           ; New number of credits 
003B: CD 47 19        CALL    $1947               ; Draw credits on screen
003E: AF              XOR     A                   ; {*} Credit switch ...
003F: 32 EA 20        LD      ($20EA),A           ; ... has opened
;
0042: 3A E9 20        LD      A,($20E9)           ; Are we moving ...
0045: A7              AND     A                   ; ... game objects?
0046: CA 82 00        JP      Z,$0082             ; {skipit} No ... restore registers and out
0049: 3A EF 20        LD      A,($20EF)           ; Are we in ...
004C: A7              AND     A                   ; ... game mode?
004D: C2 6F 00        JP      NZ,$006F            ; {*here} Yes ... go process game-play things and out
0050: 3A EB 20        LD      A,($20EB)           ; {-NumCredits:} Number of credits
0053: A7              AND     A                   ; Are there any credits (player standing there)?
0054: C2 5D 00        JP      NZ,$005D            ; Yes ... skip any ISR animations for the splash screens
0057: CD BF 0A        CALL    $0ABF               ; Process ISR tasks for splash screens
005A: C3 82 00        JP      $0082               ; Restore registers and out"""

    text = processText(text)  
    print text