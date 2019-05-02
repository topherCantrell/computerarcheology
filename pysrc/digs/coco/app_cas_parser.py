import base64

#with open('../../../content/coco/madnessminotaur/first.cas', 'rb') as f:
#with open('../../../content/coco/madnessminotaur/s_one.cas', 'rb') as f:
#with open('../../../content/coco/madnessminotaur/s_two.cas', 'rb') as f:
#with open('../../../content/coco/madnessminotaur/s_three.cas', 'rb') as f:
#with open('../../../content/coco/madnessminotaur/s_four.cas', 'rb') as f:
#with open('../../../content/coco/madnessminotaur/s_five.cas', 'rb') as f:
#with open('../../../content/coco/madnessminotaur/s_six.cas', 'rb') as f:
with open('../../../content/coco/madnessminotaur/s_seven.cas', 'rb') as f:
    data = f.read()


def add_leader(data):
    for i in range(149):
        data = data + b'\x00'
    for i in range(128):
        data = data + b'\x55'
    return data


def add_filename_block(data, name, id, is_binary, continuous, exec_addr, load_addr):
    data = data + b'\x55\x3C'
    p = len(data)
    data = data + b'\x00\x0F'
    if len(name) != 8:
        raise Exception('Filename must be 8 characters')
    data = data + name.encode()
    data = data + bytes([id])
    if is_binary:        
        data = data + b'\x00'
    else:
        data = data + b'\xFF'
    if continuous:
        data = data + b'\x00'
    else:
        data = data + b'\xFF'
    data = data + bytes([exec_addr // 256, exec_addr & 0xFF])
    data = data + bytes([load_addr // 256, load_addr & 0xFF])

    chk = 0
    while(p != len(data)):
        chk = chk + data[p]
        p += 1
    data = data + bytes([chk & 0xFF])
    data = data + b'\x55'

    return data


def add_data(data, bin):
    pos = 0
    while pos != len(bin):
        rem = len(bin) - pos
        if(rem > 255):
            rem = 255
        data = add_data_block(data, bin[pos:pos + rem])
        pos = pos + rem
    return data


def add_data_block(data, bin):
    data = data + b'\x55\x3c'
    p = len(data)
    data = data + b'\x01'
    data = data + bytes([len(bin)])
    data = data + bin
    chk = 0
    while(p != len(data)):
        chk = chk + data[p]
        p += 1
    data = data + bytes([chk & 0xFF])
    data = data + b'\x55'
    return data


def add_eof_block(data):
    data = data + b'\x55\x3C\xFF\x00\xFF\x55'
    return data


def read_block(data, pos):
    while data[pos] != 0x55:
        pos += 1
    while data[pos] != 0x3C:
        pos += 1
    pos += 1
    ret = {}
    ret['type'] = data[pos]
    pos += 1
    ret['len'] = data[pos]
    pos += 1

    if ret['type'] == 0:
        # filename block
        ret['name'] = data[pos:pos + 8].decode()
        ret['id'] = data[pos + 8]
        ret['continuous'] = data[pos + 8] == 0
        ret['exec_addr'] = data[pos + 11] * 256 + data[pos + 12]
        ret['load_addr'] = data[pos + 13] * 256 + data[pos + 14]
        ret['checksum'] = data[pos + 15]
        if data[pos + 16] != 0x55:
            raise Exception('Missing 0x55 on end of filename block')
        pos += (15 + 2)
    elif ret['type'] == 1:
        # data block
        ret['data'] = data[pos:pos + ret['len']]
        pos += ret['len']
        ret['checksum'] = data[pos]
        pos += 1
        if data[pos] != 0x55:
            raise Exception('Missing 0x55 on end of filename block')
    elif ret['type'] == 0xFF:
        ret['checksum'] = data[pos]
        pos += 1
        if data[pos] != 0x55:
            raise Exception('Missing 0x55 on end of filename block')
    else:
        raise Exception('Unknown block type ' +
                        str(ret['type']) + ' at ' + str(pos - 1))

    return pos, ret


pos = 0

# Filename
pos, block = read_block(data, pos)
print(block)

# Data
bin = b''
while True:
    pos, block = read_block(data, pos)
    if block['type'] == 0xFF:
        break
    bin = bin + block['data']

print(len(bin))

# Filename (second file)
pos, block = read_block(data, pos)
print(block)

# Data (second part)
while True:
    pos, block = read_block(data, pos)
    if block['type'] == 0xFF:
        break
    bin = bin + block['data']

print(base64.b64encode(bin).decode())

# Written as 2 files
# TODO what is the byte after the id?
b = add_leader(b'')
b = add_filename_block(b, '        ', 2, True, True, 0x673B, 0x0240)
b = add_leader(b)
b = add_data(b, bin[0:960])
b = add_eof_block(b)

b = add_leader(b)
b = add_filename_block(b, '        ', 2, True, True, 0x673B, 0x3BC1)
b = add_leader(b)
b = add_data(b, bin[960:])
b = add_eof_block(b)


with open('test.cas', 'wb') as f:
    f.write(b)
