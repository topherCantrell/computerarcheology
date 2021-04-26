
with open('gfx4.md') as f:
    for line in f:
        if len(line) < 5 or line[4] != ':':
            continue
        print(line[:22].strip())
