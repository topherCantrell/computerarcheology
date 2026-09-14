with open('../../../content/TRS80/Pyramid/Code.md') as f:
    lines = []
    for line in f:
        lines.append(line.strip())

string_count = 0
word_count = 0
pos = 0
while pos < len(lines):
    line = lines[pos]
    if line.startswith('PS_') and line[5]==':':
        string_count += 1
        print(line)
        dt = lines[pos+1]
        print(dt)
        v = int(dt[6:8],16)
        word_count = word_count + v
        # print(v)
    pos = pos + 1

print(f'Strings:{string_count} doubles:{word_count}')
