import sys

fchanges = sys.argv[1]
fdest = sys.argv[2]

changes = []
with open(fchanges, 'r') as f:
    for line in f:
        changes.append(line)    

dest = []
with open(fdest, 'r') as f:
    for line in f:
        dest.append(line)

for pos in range(len(changes)):
    line = changes[pos]
    if len(line) > 4 and line[4] == ':':
        changes_start = line[:6]
        break
for pos in range(len(changes)-1,-1,-1):
    line = changes[pos]
    if len(line) > 4 and line[4] == ':':
        changes_end = line[:6]
        break

start_dest = None
for pos in range(len(dest)):
    line = dest[pos]
    if line.startswith(changes_start):
        start_dest = pos
    if line.startswith(changes_end):
        end_dest = pos

current_address = None
line_comments = {}
added_comments = {}
for pos in range(len(dest)-1,-1,-1):
    line = dest[pos]
    if line.startswith(changes_start):
        break
    if len(line) > 4 and line[4] == ':':
        current_address = line[:4]
    if line.startswith(';;'):
        if current_address not in line_comments:
            line_comments[current_address] = [line]
        else:
            line_comments[current_address].append(line)
    elif ';;' in line:
        com_pos = line.index(';;')
        added_comments[current_address] = [com_pos, line[com_pos:]]

print(f'Changes: {len(changes)} lines, Dest: {len(dest)} lines, Start at {start_dest}, End at {end_dest}')

with open(fdest,'w') as f:
    for pos in range(start_dest):
        f.write(dest[pos])

    for pos in range(len(changes)):
        address = None
        if len(changes[pos]) > 4 and changes[pos][4] == ':':
            address = changes[pos][:4]

        if address in line_comments:
            for comment in reversed(line_comments[address]):
                f.write(comment)
        elif address in added_comments:
            new_line = changes[pos].rstrip('\n').ljust(added_comments[address][0]) + added_comments[address][1]             
            changes[pos] = new_line
            # print(">>>>", changes[pos], '>>>', added_comments[address][1])            

        f.write(changes[pos])
    
    for pos in range(end_dest+1, len(dest)):
        f.write(dest[pos])

#print(len(changes))#
#print(len(dest))