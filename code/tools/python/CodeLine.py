import string

class CodeLine:
    
    # ([])      labels
    # (int)     address
    # ([])      bytes
    # (string)  opcode
    # (int)     printedOpcodeLen
    # (string)  comment
    # (string)  original
   
    def __init__(self):
        self.labels = []
        self.bytes = []
        self.comment = None
        self.opcode = None
        self.address = None      
        self.target = None
        self.numbers = None 
        self.originalCommentPos = -1
    
    def isFourDigitHex(self,str):
        if len(str)!=4:
            return False       
        try:
            int(str,16)
            return True
        except:
            return False
        
    def isTwoDigitHex(self,str):
        if len(str)!=2:
            return False       
        try:
            int(str,16)
            return True
        except:
            return False
         
    def decodeTargetLink(self,str):
        ret = {}
        str = str.strip()
        if str.startswith(">>"):
            ret["placement"] = 'comment'
            str = str[2:].strip()
        elif str.startswith(">"):
            ret["placement"] = 'side'
            str = str[2:].strip()
        else:
            ret["placement"] = 'inline'
            
        if str.startswith("--"):
            ret["map"] = "hardware"
            str = str[2:].strip()
        elif str.startswith("-"):
            ret["map"] = "ram"
            str = str[1:].strip()
        else:
            ret["map"] = ""
        
        if ":" in str:
            i = str.index(":")
            ret["target"] = str[0:i].strip()
            ret["text"] = str[i+1:].strip()
        else:
            ret["target"] = str
            ret["text"] = str
            
        
        return ret
    
    def getNumbersFromOpcode(self):
        ret = []
        pos = 0
        while True:
            if not "$" in self.opcode[pos:]:
                break
            numEntry = {}
            pos = self.opcode.index("$",pos)
            numEntry["startPos"] = pos
            i = pos+1
            while i<len(self.opcode) and self.opcode[i] in '0123456789ABCDEF':
                i = i + 1
            numEntry["textLen"]=i-pos
            numEntry["value"]=int(self.opcode[pos+1:i],16)
            numEntry["text"]= self.opcode[pos:i]
            pos = i+1
            ret.append(numEntry)
        return ret
    
    def parse(self,str):
        self.original = str
        str = str.strip()
        if ';' in str:
            self.originalCommentPos = self.original.index(";")
            i = str.index(';')
            self.comment = str[i+1:]
            str = str[0:i].strip()  
        
        first = str        
        if ' ' in first:
            first = str[0:str.index(' ')]
         
        if first.endswith(":"):
            first = first[0:-1]
            if self.isFourDigitHex(first):
                self.address = int(first,16)
            else:
                self.labels.append(first)
                
        i = len(first)+1
        str = str[i:].strip()
        
        while(True):
            if len(str)<2:
                break
            if len(str)>2 and str[2]!=' ':
                break
            if (str[0] in '0123456789ABCDEF') and (str[1] in '0123456789ABCDEF'):
                self.bytes.append(int(str[0:2],16))
                str = str[2:].strip()
            else:
                break 
            
        if len(str)>0:
            self.opcode = str
            self.printedOpcodeLen = len(self.opcode)
            self.originalOpcodePos = self.original.index(str)
            
        if self.comment and "{" in self.comment:
            i = self.comment.index("{")
            j = self.comment.index("}")              
            self.target = self.decodeTargetLink(self.comment[i+1:j])
            self.numbers = self.getNumbersFromOpcode()
            h = self.comment[0:i]+self.comment[j+1:]
            self.comment = h
            
                        
            