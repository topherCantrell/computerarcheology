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
         
    
    def parse(self,str):
        self.original = str
        str = str.strip()
        if ';' in str:
            i = str.index(';')
            self.comment = str[i+1:]
            str = str[0:i].strip()
        
        first = str        
        if ' ' in first:
            first = str[0:str.index(' ')]
         
        if first.endswith(":"):
            first = first[0:-1]
            if self.isFourDigitHex(first):
                address = int(first,16)
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