ROOM_TABLE = """4888: DB 5B CC 49
488C: 10 5C E1 49
4890: 57 5C F2 49
4894: 57 5C 03 4A
4898: 57 5C 14 4A
489C: 57 5C 25 4A
48A0: 68 5C 36 4A
48A4: E2 5C 47 4A
48A8: 28 5D 58 4A
48AC: 7D 5D 69 4A
48B0: A0 5D 7E 4A
48B4: 1E 5E 87 4A
48B8: 8E 5E 9D 4A
48BC: 69 5F C8 4A
48C0: AB 5F D1 4A
48C4: 08 60 0D 4B
48C8: 3C 60 48 4B
48CC: 55 60 51 4B
48D0: 85 60 90 4B
48D4: F1 60 A9 4B
48D8: 5F 61 BE 4B
48DC: AC 61 C7 4B
48E0: D8 61 D8 4B
48E4: E0 61 E1 4B
48E8: 18 62 F2 4B
48EC: 58 62 07 4C
48F0: B0 62 14 4C
48F4: C8 62 21 4C
48F8: C8 62 36 4C
48FC: C8 62 47 4C
4900: C8 62 60 4C
4904: C8 62 69 4C
4908: C8 62 76 4C
490C: C8 62 87 4C
4910: C8 62 98 4C
4914: C8 62 B1 4C
4918: C8 62 C2 4C
491C: C8 62 CB 4C
4920: C8 62 DC 4C
4924: C8 62 E9 4C
4928: C8 62 F6 4C
492C: D8 61 03 4D
4930: D8 61 08 4D
4934: D8 61 0D 4D
4938: D8 61 12 4D
493C: D8 61 17 4D
4940: D8 61 1C 4D
4944: D8 61 21 4D
4948: D8 61 26 4D
494C: D8 61 2B 4D
4950: D8 61 30 4D
4954: EA 62 41 4D
4958: D8 61 56 4D
495C: 49 63 5B 4D
4960: A6 63 68 4D
4964: DA 63 75 4D
4968: 1F 64 93 4D
496C: 7A 64 9C 4D
4970: 0A 65 B1 4D
4974: A1 65 BE 4D
4978: D5 65 06 4E
497C: 82 66 21 4E
4980: E0 66 2A 4E
4984: 07 67 33 4E
4988: 29 67 3C 4E
498C: 89 67 65 4E
4990: 00 00 00 00
4994: D2 6B 3B 4F
4998: 00 00 00 00
499C: B1 6B 32 4F
49A0: 5C 6B 25 4F
49A4: 25 68 6E 4E
49A8: 82 68 77 4E
49AC: 00 00 00 00
49B0: 00 00 00 00
49B4: F6 68 86 4E
49B8: F3 6A 0E 4F
49BC: 3F 69 9B 4E
49C0: 21 6A A8 4E
49C4: 4B 6A B1 4E
49C8: 9D 6A BE 4E"""

rooms = ROOM_TABLE.splitlines()
info = []
for r in rooms:
    inf = r.split(' ')
    info.append([inf[2]+inf[1], inf[4]+inf[3]])

with open("content/TRS80/Pyramid/Code.md", "r") as f:
    lines = f.readlines()

def find_address(addr):
    for i, line in enumerate(lines):
        if line.startswith(addr+":"):
            return i
    return None

for i, line in enumerate(lines):
    j = line.find('Print("')
    if j != -1:
        s = line[12:14]+line[9:11]
        k = find_address(s)
        ps = lines[k-1][:5]
        lines[i] = lines[i][0:j+6] + ps + ':'+lines[i][j+6:]
        
with open("content/TRS80/Pyramid/new.md", "w") as f:
    f.writelines(lines)

