import sys

fname = "../../content/Arcade/SpaceInvaders/SpaceInvaders.mark"

with open(fname) as f:
    raw = f.readlines()

REPS = [{'utf8': "\xE2\x80\x9C", 'rep': '"'},
        {'utf8': "\xE2\x80\x9D", 'rep': '"'},
        {'utf8': "\xE2\x80\x93", 'rep': '--'},
        {'utf8': "\xE2\x80\xA6", 'rep': '...'},
        {'utf8': "\xE2\x80\x98", 'rep': "'"},

        {'utf8': "\xE2\x80\x99", 'rep': "'"}

        ]


def checkString(s):
    for x in iter(range(len(s))):
        if ord(s[x]) > 127:
            for y in iter(range(5)):
                print (ord(s[x + y]))
            return False
    return True

for x in iter(range(len(raw))):
    # if '\xE2\x80\x73' in raw[x]:
    #    print raw[x]
    r = raw[x]
    for o in REPS:
        r = r.replace(o["utf8"], o["rep"])
    raw[x] = r
    if not checkString(r):
        print ("OOPS")
        print ("::" + r + "::")
        break

with open("New.mark", "w") as f:
    f.writelines(raw)
