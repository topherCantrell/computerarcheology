
def hex4(value):
    value = hex(value).upper()[2:]
    value = value.rjust(4,'0')
    return value

def hex2(value):
    value = hex(value).upper()[2:]
    value = value.rjust(2,'0')
    return value

def dump_bytes(b):
    ret = ''
    b = list(b)    
    for i in b:
        ret+=hex2(i)+' '    
    return ret.strip()

def hexlist(b):
    ret = '['
    for i in b:
        ret+=hex2(i)+', '
    ret = ret[0:-2] + ']'
    return ret

def indent_code(s,level):
    # code goes out to column 65
    if s[4]!= ':':
        return s
    
    i = s.find(';')
    
    if i>=0:        
        comment = s[i+1:].strip()
        code = s[6:i].strip()
        return s[0:6]+code.rjust(len(code)+level*2).ljust(65)+'; '+comment.rjust(len(comment)+level*2)
    else:
        code = s[6:].strip()
        return s[0:6]+code.rjust(len(code)+level*2)
