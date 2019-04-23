
with open('../../../content/coco/madnessminotaur/first.cas', 'rb') as f:
    data = f.read()

def read_block(data,pos):
    while data[pos] != 0x55:
        pos += 1
    while data[pos] != 0x3C:
        pos += 1
    pos+=1
    ret = {}
    ret['type'] = data[pos];
    pos+=1
    ret['len'] = data[pos];
    pos+=1    
    
    if ret['type'] == 0:
        # filename block
        ret['name'] = data[pos:pos+8].decode()
        ret['id'] = data[pos+9]
        ret['continuous'] = data[pos+10]==0
        ret['exec_addr'] = data[pos+11]*256+data[pos+12]
        ret['load_addr'] = data[pos+13]*256+data[pos+14]
        ret['checksum'] = data[pos+15]
        if data[pos+16]!=0x55:
            raise Exception('Missing 0x55 on end of filename block')
        pos+=(15+2)                
    elif ret['type'] ==1:
        # data block
        ret['data'] = data[pos:pos+ret['len']]        
        pos+=ret['len']
        ret['checksum'] = data[pos]
        pos+=1
        if data[pos]!=0x55:
            raise Exception('Missing 0x55 on end of filename block')        
    elif ret['type'] == 0xFF:
        ret['checksum'] = data[pos]
        pos+=1
        if data[pos]!=0x55:
            raise Exception('Missing 0x55 on end of filename block')   
    else:
        raise Exception('Unknown block type '+str(ret['type'])+' at '+str(pos-1))
    
    return pos,ret

pos = 0

# Filename
pos,block = read_block(data,pos)
print(block)

# Data
bin = b''
while True:
    pos,block = read_block(data,pos)
    if block['type']==0xFF:
        break
    bin = bin + block['data']

# Filename (second file)
pos,block = read_block(data,pos)
print(block)

# Data (second part)
while True:
    pos,block = read_block(data,pos)
    if block['type']==0xFF:
        break
    bin = bin + block['data']
    
import base64
print(base64.b64encode(bin))
