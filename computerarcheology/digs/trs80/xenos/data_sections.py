with open('content/trs80/xenos/roms/xenos.bin', 'rb') as f:
    data = f.read()

ORIGIN = 0x5D00



def print_word_data(pos):
    g = f"{pos:04X}: {data[pos-ORIGIN]:02X} "
    for i in range(data[pos-ORIGIN]):
        g += f"{data[pos-ORIGIN+1+i]:02X} "
    num = data[pos-ORIGIN+2+i]
    g = g.ljust(35)+f"{num:02X} ; "
    sz = data[pos-ORIGIN]
    for i in range(sz):
        c = data[pos-ORIGIN+1+i]
        g += chr(c)    
    print(g)

pos = 0x762D
while data[pos-ORIGIN] != 0x00:
    print_word_data(pos)
    pos += data[pos-ORIGIN] + 2    

print("7909: 00")

pos = 0x790A
while data[pos-ORIGIN] != 0x00:
    print_word_data(pos)
    pos += data[pos-ORIGIN] + 2    

print("7BBB: 00")

pos = 0x7BBC
while data[pos-ORIGIN] != 0x00:
    print_word_data(pos)
    pos += data[pos-ORIGIN] + 2    

print("7CDA: 00")

pos = 0x7CDB
while data[pos-ORIGIN] != 0x00:
    print_word_data(pos)
    pos += data[pos-ORIGIN] + 2    