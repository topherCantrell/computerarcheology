
# Kinds of code lines:
# - Label : Single word before a comment ending in ':'
# - Data (no mnemonics) : Line begins with XXXX: and is all XX XX XX ...
# - Code (mnemonics) : Line begins with XXXX: and has XX XX XX and non XX parts
# - Other (comments, blanks) : Everything else


class CodeLine:
    # Info about the line: original text, line number, file
    # Comment
    # Label
    # Data
    # Mnemonic
    # Address
    
    def __init__(self,line,filename=None,line_number=None):
        self._original = line
        self._filename = filename
        self._line_number = line_number
        
        line = line.strip()
        
        if ';' in line:
            i = line.index(';')
            self._comment = line[i+1:].strip()
            line = line[0:i].strip()
        else:
            self._comment = None
            
        if not ' ' in line and line.endswith(':'):
            self.type = 'Label'
            self._label = line[0:-1]
            return
        
        if len(line)>4:
            try:
                if line[4]==':':
                    self._address = int(line[0:4],16)
                    # TODO this is either Data or Code                
            except:
                pass
        
        
            
        
        
if __name__ == '__main__':
    
    c = CodeLine('Here: ; Top of the function')
    print(c.type)
    print(c._label)