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

print(f'Changes: {len(changes)} lines, Dest: {len(dest)} lines, Start at {start_dest}, End at {end_dest}')

with open(fdest,'w') as f:
    for pos in range(start_dest):
        f.write(dest[pos])
    for pos in range(len(changes)):
        f.write(changes[pos])
    for pos in range(end_dest+1, len(dest)):
        f.write(dest[pos])

#print(len(changes))#
#print(len(dest))