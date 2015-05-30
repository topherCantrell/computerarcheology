
with open("c:/users/topher/desktop/asteroids.asm") as f:
    newLines = f.readlines()

ncs = {}
for n in newLines:
    n = n.strip()
    if ".BYTE" in n:
        continue
    if len(n) < 6:
        continue
    if n[5] == ' ':
        continue
    if n[0] != '6' and n[0] != '7':
        continue

    if ";" not in n:
        continue
    i = n.index(";")
    com = n[i + 1:]
    if len(com) == 0:
        continue

    ncs[n[0:4]] = com

with open("c:/users/topher/git/computerarcheology/content/arcade/asteroids/code.mark") as f:
    oldLines = f.readlines()


newLines = []
for o in oldLines:
    if len(o) < 5:
        newLines.append(o)
        continue
    if o[4] != ':':
        newLines.append(o)
        continue

    ad = o[0:4]
    if ad not in ncs:
        newLines.append(o)
        continue

    if ";" in o:
        newLines.append(o)
        continue

    o = o.strip()
    while len(o) < 38:
        o = o + " "
    o = o + "; " + ncs[ad]

    print o

    newLines.append(o + "\n")

with open("Code.mark", "w") as f:
    f.writelines(newLines)
