import sections

org_data = sections.SECTIONS[4]

WORDS = {}

word_count = 0
for record in org_data:
    info = record.split('\t')
    num = int(info[0])
    txt = info[1]
    if num not in WORDS:
        WORDS[num] = []
    WORDS[num].append(txt)
    word_count += 1

if __name__ == '__main__':
    for num in sorted(WORDS.keys()):
        print(f"{num}: {', '.join(WORDS[num])}")
    print(f"Total words: {word_count}")
    print(f"Total unique numbers: {len(WORDS)}")
