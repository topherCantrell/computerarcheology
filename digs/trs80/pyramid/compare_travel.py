from difflib import SequenceMatcher

"""
The pyramid strings and map are nearly identical to colossal cave. This script compares the 
travel maps
"""




with open("../../../content/TRS80/Pyramid/Code.md") as f:
    lines = []
    for line in f:
        lines.append(line.strip())

pos = 0
while not lines[pos].startswith('; PS_'):
    pos += 1
room_name = lines[pos-1][7:-1]

while lines[pos].startswith(';'):
    pos += 1

print(lines[pos],pos)
