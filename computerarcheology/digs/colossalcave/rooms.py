import sections

ROOMS = {}

org_data = sections.SECTIONS[1]
for record in org_data:
    i = record.find('\t')
    rn = int(record[:i])
    txt = record[i+1:]
    if rn not in ROOMS:
        ROOMS[rn] = {
            "long": [],
            "short": None
        }
    ROOMS[rn]['long'].append(txt)

org_data = sections.SECTIONS[2]
for record in org_data:
    i = record.find('\t')
    rn = int(record[:i])
    txt = record[i+1:]
    ROOMS[rn]['short'] = txt

