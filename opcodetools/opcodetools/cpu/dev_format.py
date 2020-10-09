
fname = 'cpu_Z80GB.py'

with open(fname) as f:
    lines = f.readlines()

for o in lines:
    o = o[0:-1]
    if o.endswith('},'):
        x = len(o) - 3
        while o[x] == ' ':
            x -= 1
        if o[x] == ',':
            o = o[:x] + o[x + 1:]
    print(o)
