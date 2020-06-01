# http://www.trs-80.com/wordpress/zaps-patches-pokes-tips/tape-and-file-formats-structures/

name = '../../content/TRS80/RaakaTu/raaka.cas'
#name = '../../content/TRS80/HauntedHouse/haunt.cas'

with open(name,'rb') as f:
    data = f.read()
    
pos = 0

while data[pos]==0:
    pos += 1
    
if data[pos]!=0xA5 or data[pos+1]!=0x55:
    raise Exception('Incorrect CAS header (expected A5 55)')

pos+=2

name = data[pos:pos+6].decode()
pos+=6
print(':'+name+':')

bindata = b''

while True:
    cmd = data[pos]
    pos+=1
    if cmd==0x3C:
        sz = data[pos]
        if sz==0:
            sz=256
        pos += 1
        load_address = data[pos+1]*256 + data[pos]
        pos += 2
        checksum = data[pos+sz]
        print('DATA BLOCK',hex(sz),hex(load_address),hex(checksum))
        bindata += data[pos:pos+sz]
        # get data
        pos+= sz + 1
    elif cmd==0x78:
        exec_address = data[pos+1]*256 + data[pos]
        pos = pos + 2
        print('END BLOCK',hex(exec_address))
        break
    else:
        raise Exception('Unknown block type',hex(cmd),hex(pos))

with open(name.strip()+'.bin','wb') as f:
    f.write(bindata)
print(bindata)