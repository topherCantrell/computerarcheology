from digs.coco.app_make_madness_bin import pos


with open('../../../content/coco/madnessminotaur/s_one.cas', 'rb') as f:
    data = f.read()

pos = 0

while data[pos] != 0x55:
    pos += 1
while data[pos] != 0x3C:
    pos += 1

bt = data[pos:pos + 1]
pos += 1

print(bt, pos)
