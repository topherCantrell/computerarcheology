COCO_MATCHES = [
    ['59B0', '5A40','1945','19D5'],
    ['5A4B', '5BDA','19D6','1B65'],
    ['56CE', '59AF','3C40','3F15'],
    ['5047', '509D','18ED','1943'],
    ['4FE7', '503D', '188D', '18E3'],
    ['49CC', '4F44','1272','17EA'],
    ['4888', '49C8', '112E','126E']
]
MATCHES = [
    ['4308', '45FE', '4203', '44F9'],
    ['45FE+2', '4650', '458B+2', '45E3'],
    ['467A-1', '46D0+3', '4617-1', '466D+3'],
    ['4725-2', '4782', '46C2-2', '471F'],
    ['47BF-3', '55F2', '475C-3', '558F'],
    ['5694-#', '7FE8', '55E8-#', '7F3C'],
]
# Code:4308 and Code1:4203
#   through
# Code:45FE and Code1:44F9
#
# Code:45FE+2 and Code1:458B+2
#   through
# Code:4650 and Code1:45F6
#
# Code:467A-1 and Code1:4617-1
#   through
# Code:46D0+3 and Code1:466D+3
#
# Code:4725-2 and Code1:46C2-2
#   through
# Code:4782 and Code1:471F
#
# Code:47BF-3 and Code1:475C-3
#   through
# Code:55F2 and Code1:558F
#
# Code:5694-# and Code1:55E8-#
#   through
# Code:7FE8 Code1:7F3C

with open("content/TRS80/Pyramid/Code.md", "r") as f1:
    lines1 = []
    for line in f1:
        lines1.append(line.strip('\n'))

# with open("content/TRS80/Pyramid/Code1.md", "r") as f2:
#     lines2 = []
#     for line in f2:
#         lines2.append(line.strip('\n'))

with open("content/CoCo/Pyramid/Code.md", "r") as f1:
    lines2 = []
    for line in f1:
        lines2.append(line.strip('\n'))

def fun1():
    pos1 = 0
    while True:
        if lines1[pos1].startswith('RoomDescriptions:'):
            break
        pos1 += 1

    pos2 = 0
    while True:
        if lines2[pos2].startswith('RoomDescriptions:'):
            break
        pos2 += 1

    print(pos1, pos2)

    codeorg = 0x5BDB
    code1org = 0x5B2F

    orgdelta = codeorg - code1org

    while pos1 < len(lines1):
        nline = lines1[pos1]
        if len(nline)>4 and nline[4] == ':':
            # print(nline)
            org = int(nline[:4], 16)
            neworg = org - orgdelta
            nline = f"{neworg:04X}" + nline[4:]
            print(nline)
            
        else:
            print(nline)        
        pos1 += 1

def fun2():
    pos2 = 0
    data = []
    while True:
        if lines2[pos2].startswith('5904:'):
            break
        pos2 += 1
    while not lines2[pos2].startswith("```"):
        s = lines2[pos2][6:].strip(' ').split(' ')
        for b in s:
            data.append(b)
        pos2 += 1

    sizes = {}
    pos1 = 0
    while True:
        if lines1[pos1].startswith('GeneralCommandHandler:'):
            break
        pos1 += 1

    sizes = []
    while not lines1[pos1].startswith('5BDA:'):
        s = lines1[pos1]
        i = s.find(';')
        s = s[:i].strip(' ')
        s = s.split(' ')
        if len(s) > 1:
            sizes.append(len(s)-1)
        pos1 += 1

    p = 0x5904
    for s in sizes:
        print(f"{p:04X}: ", end="")
        for i in range(s):
            print(data[p-0x5904], end=" ")
            p += 1
        print()

def find_line(lines, info):
    if not '+' in info and not '-' in info:
        for i in range(len(lines)):
            if lines[i].startswith(info + ':'):
                return i
        raise Exception('Not found')
    pat = info[5:]
    if pat=='#':
        i = find_line(lines, info[:4])
        delta = 1
        if info[4] == '-':
            delta = -1
        while lines[i].startswith('#'):
            i += delta
        return i
    else:
        i = find_line(lines, info[:4])
        n = int(info[5:])
        if info[4] == '-':
            n = -n
        return i + n

def check_code_match(a,b):
    a = a.strip(' ')
    b = b.strip(' ')
    # 55E8: 3A 11 47        LD      A,($4711)           ; {code.keyWaitCounter} Random value
    # 5694: 3A 74 47        LD      A,($4774)           ; {code.keyWaitCounter} Random value
    if a[4] != ':' or b[4] != ':':
        return False
    # if a[4:7] != b[4:7]:
    #     return False
    i = a.find(';')
    if i != -1:
        a = a[:i]
    j = b.find(';')
    if j != -1:
        b = b[:j]
    i = a.find('$')
    if i != -1:
        a = a[:i]
    j = b.find('$')
    if j != -1:
        b = b[:j]
    return a[22:] == b[22:]

def do_match(a,b,c,d):
    pos1 = find_line(lines1, a)
    end1 = find_line(lines1, b)
    pos2 = find_line(lines2, c)
    end2 = find_line(lines2, d)
    while pos1 <= end1:
        a = lines1[pos1]
        b = lines2[pos2]

        if len(a)>4 and a[4] == ':':
            if not check_code_match(a,b):
                print('>>>',a)
                print('>>>',b)
                print(pos1)
                raise Exception('Mismatch')        
            i = a.find(';')
            if i>=0:            
                j = b.find(';')
                if j>=0:
                    b = b[:j].strip(' ')
                b = b.strip(' ').ljust(i) + a[i:]
            print(b)
                
        else:
            if a != b:
                print('>>>',a)
                print('>>>',b)
                print(pos1)
                raise Exception('Mismatch')
            print(b)

        pos1 += 1
        pos2 += 1

do_match(*COCO_MATCHES[6])
