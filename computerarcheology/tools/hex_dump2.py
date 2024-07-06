from computerarcheology.util import util

with open('content/arcade/galaga/roms/prom-3.1c','rb') as f:
    data = f.read()

origin = 0

num_printed = 0
for d in data:
    if num_printed == 0:
        print(f'{util.hex4(origin)}:', end='')
    print(f' {util.hex2(d)}', end='')
    num_printed += 1
    if num_printed == 16:
        num_printed = 0
        print()
    origin += 1
    