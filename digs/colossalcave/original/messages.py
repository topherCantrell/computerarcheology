import sections

MESSAGES = {}

org_data = sections.SECTIONS[6]
for record in org_data:
    i = record.find('\t')
    mn = int(record[:i])
    txt = record[i+1:]
    if mn not in MESSAGES:
        MESSAGES[mn] = []
    MESSAGES[mn].append(txt)
