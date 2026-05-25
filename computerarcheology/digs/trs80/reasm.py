
def line_to_data(line):
    if len(line) < 5 or line[4] != ":":
        return line
    line = line[5:].strip()
    comment = ''
    i = line.find(';')
    if i != -1:
        comment = line[i:].strip()
        line = line[:i].strip()
    line = line.split(' ')
    for i in range(len(line)):
        line[i] = '0x' + line[i]
    line = '.byte ' + ', '.join(line)
    if comment:
        line = line.ljust(25) + ' ' + comment        
    return line

with open("new.asm","w") as fo:
    with open("content/TRS80/Pyramid/reassmeble/rooms.asm", "r") as f:
        for line in f:
            line = line.strip()
            n = line_to_data(line)
            i = line.find('Print(PS_')
            if i != -1:
                ps = line[i+6:i+11]
                n = n[:10]+'            '+n[22:]
                print(n)
                print(f'.word {ps}')
            else:
                print(n)