
# Kinds of code lines:
# - Label : Single word before a comment ending in ':'
# - Data (no mnemonics) : Line begins with XXXX: and is all XX XX XX ...
# - Code (mnemonics) : Line begins with XXXX: and has XX XX XX and non XX parts
# - Other (comments, blanks) : Everything else


class CodeLine:
    # Info about the line: original, line_number, filename
    # line
    # comment
    # label
    # data
    # mnemonicText
    # mnemonic
    # address
    
    def __init__(self,md,filename=None,line_number=None):
        self.original = md
        self.filename = filename
        self.line_number = line_number
        
        line = md.line.strip()
                
        self.address = None
        self.comment = None
        
        if ';' in line:
            i = line.index(';')
            self.comment = line[i+1:].strip()
            line = line[0:i].strip()                    
        
        self.label = None    
        if not ' ' in line and line.endswith(':'):
            self.type = 'Label'
            self.label = line[0:-1]
            return        
        
        if len(line)>4:
            try:
                if line[4]==':':
                    self.address = int(line[0:4],16)
                    # TODO this is either Data or Code        
                    line = line[5:].strip()
                    
                    self.data = []
                    while True:
                        if len(line)==2 or (len(line)>2 and line[2]==' '):
                            try:
                                self.data.append(int(line[0:2],16))
                                line = line[2:].strip()
                                if len(line)==0:
                                    break
                            except:
                                # This is not a number ... done with data
                                break
                        else:
                            break
                    
                    if len(line)==0:
                        self.type = 'Data'
                    else:
                        self.type = 'Code'
                        self.mnemonicText = line        
                        if ' ' in line:
                            i = line.index(' ')
                            self.mnemonic = [line[0:i],line[i+1:].strip()]
                        else:
                            self.mnemonic = [line]
                    return    
            except:
                # Nothing to do here. This is how we check to see
                # if the 4 character value is a hex number.
                # Fall through.
                pass
            
        self.type = 'Other'            
