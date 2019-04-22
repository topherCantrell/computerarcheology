
with open('../../../content/coco/madnessminotaur/s_one.cas', 'rb') as f:
    data = f.read()


def skip_leader(data, pos):
    while data[pos] != 0x55:
        pos += 1
    while data[pos] != 0x3C:
        pos += 1
    return pos


pos = 0

pos = skip_leader(data, pos)

bt = data[pos]
pos += 1

print(bt, pos)
