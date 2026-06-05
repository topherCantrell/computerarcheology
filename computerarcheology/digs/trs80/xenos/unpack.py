
CHARS = '?!2 "\'<>/03ABCDEFGHIJKLMNOPQRSTUVWXYZ-,.#'

def unpack_2_bytes(b,a):
    val = a * 256 + b
    
    # 2. Extract character indices
    idx3 = val % 40
    val //= 40
    idx2 = val % 40
    idx1 = val // 40
    
    return CHARS[idx1] + CHARS[idx2] + CHARS[idx3]

def unpack(ptr,data,length):
    ret = ''    
    while True:
        if length > 1:
            ret += unpack_2_bytes(data[ptr], data[ptr+1])
            ptr += 2
            length -= 2
        else:
            if length == 1:
                ret +=chr(data[ptr])
            # 0 or 1, we are done
            break
    return ret
