import sections

org_data = sections.SECTIONS[4]

WORDS = {}

for record in org_data:
    info = record.split('\t')
    num = int(info[0])
    txt = info[1]
    if num not in WORDS:
        WORDS[num] = []
    WORDS[num].append(txt)
