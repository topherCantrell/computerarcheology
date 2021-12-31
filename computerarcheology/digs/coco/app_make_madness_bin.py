
with open('../../../content/coco/madnessminotaur/madness.bin', 'rb') as f:
    data = f.read()

pos = 0
for d in data:
    print('0x{:02X},'.format(d), end='')
    pos += 1
    if pos == 32:
        pos = 0
        print()
