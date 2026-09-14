from difflib import SequenceMatcher

"""
The pyramid strings and map are nearly identical to colossal cave. This script compares the strings
between the two games and reports the differences.
"""

def extract_string(lines, i, j):
    ret = ''
    for k in range(i,j):
        n = lines[k][1:].strip()
        if n[0].islower():
            x = n.find(' ')
            n = n[x+1:].strip()
        ret += n + ' '

    ret = ret.replace('_',' ')
    ret = ret.strip()
    return " ".join(ret.split())

def jaccard_word_similarity(str1, str2):
    # Split strings into lowercase words and convert to sets
    set1 = set(str1.lower().split())
    set2 = set(str2.lower().split())
    
    # Calculate intersection and union
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    
    # Avoid DivisionByZero if both strings are empty
    if not union:
        return 0.0
        
    return len(intersection) / len(union)


with open("../../../content/trs80/pyramid/Code.md") as f:
    lines = []
    for line in f:
        lines.append(line.strip())

pos  = 0

new_strings = []
metrics = []

try:
    while True:
        while len(lines[pos]) < 6 or not lines[pos].startswith('PS_') or lines[pos][5] != ':':
            pos += 1

        name = lines[pos][:5].strip()

        while lines[pos].strip():
            pos -= 1
        pos += 1
        epos = pos
        mpos = None
        while not lines[epos].startswith('PS_'):
            if lines[epos].strip() == ';':
                mpos = epos
            epos += 1

        if mpos is None:
            a = None
            b = extract_string(lines, pos, epos)
        else:
            a = extract_string(lines, pos, mpos)
            b = extract_string(lines, mpos+1, epos)

        if a is None:
            new_strings.append((name, b))
        else:
            # print(a)
            # print(b)
            ratio = SequenceMatcher(None, a, b).ratio()
            # ratio = jaccard_word_similarity(a, b)
            # print(ratio)
            metrics.append((name, ratio, a, b))            

        pos = epos+1
except IndexError:
    pass

print("New strings in PYRAMID:", len(new_strings))
for rec in new_strings:
    print(f'{rec[0]}: {rec[1]}')
print()

cnt_100 = 0
cnt_75 = 0
cnt_50 = 0
for rec in metrics:
    if rec[1] == 1.0:
        cnt_100 += 1
    elif rec[1] >= 0.75:
        cnt_75 += 1
    elif rec[1] >= 0.5:
        cnt_50 += 1

print(f'Total strings compared: {len(metrics)}')
print(f'100%: {cnt_100}  75%: {cnt_75}  50%: {cnt_50}')

sorted_data = sorted(metrics, key=lambda x: x[1])

for rec in sorted_data:
    print(rec[0])
    print(rec[1])
    print(rec[2])
    print(rec[3])
