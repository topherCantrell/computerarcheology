
LENGTHS = [12, 16]

IN_NAME = "../../content/arcade/MoonPatrol/RAMUse.mark"
OUT_NAME = "new.cmark"


def pad_to(s, length):
    s = s.strip()
    while(len(s) < length):
        s = s + " "

    return s

# Load the raw lines
with open(IN_NAME) as f:
    raw = f.readlines()

new_lines = []

for r in raw:
    if not r.strip().startswith("||"):
        new_lines.append(r)
        continue

    cols = r.strip().split("||")

    # print cols

    if len(cols) != 5 or len(cols[0]) != 0 or len(cols[4]) != 0:
        raise Exception("Invalid format '" + r.strip() + "'")

    f1 = "|| " + pad_to(cols[1], LENGTHS[0]) + " || " + pad_to(cols[2], LENGTHS[0]) + " || " + cols[3].strip() + " ||"
    new_lines.append(f1 + "\n")

# Write the lines
with open(OUT_NAME, "w") as f:
    f.writelines(new_lines)
