
decode_room_name = None # Set me
decode_helper_name = None # Set me
decode_noun = None # Set me
decode_phrase = None # Set me

def decode_object_bits(n,collapse_zero=True):
    if collapse_zero and n==0:
        return '*'
    ret = ''
    if n&0x80:
        ret=ret+'u'
    else:
        ret=ret+'.'
    if n&0x40:
        ret = ret + 'v'
    else:
        ret = ret + '.'
    if n&0x20:
        ret = ret + 'C'
    else:
        ret = ret + '.'
    if n&0x10:
        ret = ret + 'P'
    else:
        ret = ret + '.'
    if n&0x08:
        ret = ret + 'A'
    else:
        ret = ret + '.'
    if n&0x04:
        ret = ret + 'X'
    else:
        ret = ret + '.'
    if n&0x02:
        ret = ret + 'O'
    else:
        ret = ret + '.'
    if n&0x01:
        ret = ret + 'L'
    else:
        ret = ret + '.'
        
    return ret