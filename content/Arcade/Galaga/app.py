
import os

print(os.listdir('roms'))

for fn in os.listdir('roms'):
    with open(os.path.join('roms', fn), 'rb') as f:
        data = f.read()
        if data[0x96] == 0x3A:
            print(fn)
