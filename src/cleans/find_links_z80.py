from code_line import CodeLine

# Dig specifics
IN_FILE = "../../content/Arcade/Frogger/SoundCode.mark"
OUT_FILE = "New.mark"
CODE_SPACE = (0x0000, 0x17FF)
RAM_SPACE = (0x4000, 0x43FF)

# Z80 specifics
CODE_OPS = ["JP", "JR", "CALL", "DJNZ", "DJZ"]

# All memory fetches are ($....)
# Things like "LD  HL,$4040" where $4040 is the address of a known memory location


def add_spec(r, s, last_comment_pos):

    if ";" not in r:
        r = add_comment(r, last_comment_pos)

    # In case we are replacing an existing ... strip out the existing
    i = r.index(";")
    if r[i + 1:].strip().startswith("{"):
        j = r.index("}", i)
        r = r[0:i] + " " + r[j + 1:]

    r = r[0:i + 1] + s + " " + r[i + 1:].strip()

    return r + "\n"


def add_comment(original, commentPos):
    """
    Add a blank comment to the code line
    """
    original = original[:-1]  # Strip line feed
    while len(original) < commentPos:
        original = original + " "
    original = original + ";\n"
    return original


def print_ram_hits():
    ram_hits.sort()
    for r in ram_hits:
        print "|| " + r + "     ||                  || ||"


# Load the raw lines
with open(IN_FILE) as f:
    raw = f.readlines()

# Process the file line by line
last_comment_pos = 0
newLines = []
candidates = []
ram_hits = []
for r in raw:

    t = r.strip()

    # Keep comment lines as-is
    if t.startswith(";"):
        newLines.append(r)
        continue

    # Keep blank lines as-is
    if t == "":
        newLines.append(r)
        continue

    # Must be code. Parse that.
    c = CodeLine()
    c.parse(r)

    # Keep up with the comment spacing from line to line in case we
    # need to add a blank comment
    if c.comment:
        last_comment_pos = c.originalCommentPos

    # Ignore any existing specs (comment this out if you want to overwrite)
    if c.comment and c.comment[1:].strip().startswith("{"):
        newLines.append(r)
        continue

    # Only process lines that are opcodes
    if not c.opcode:
        newLines.append(r)
        continue

    #
    # CPU specifics here
    #

    # Good old Z80 -- memory references are in parens
    if "($" in c.opcode:

        # INs and OUTs come from port space
        if c.opcode.startswith("OUT ") or c.opcode.startswith("IN "):
            newLines.append(r)
            continue

        i = c.opcode.index("($") + 2
        j = c.opcode.index(")", i)
        v = c.opcode[i:j]
        if v not in ram_hits:
            ram_hits.append(v)

        # This must be a RAM reference
        r = add_spec(r, "{-}", last_comment_pos)
        newLines.append(r)
        continue

    if "$" in c.opcode:
        i = c.opcode.index("$")

        wrds = c.opcode.split(" ")
        if wrds[0] in CODE_OPS:
            # This must be a code reference
            r = add_spec(r, "{}", last_comment_pos)
            newLines.append(r)
            continue

        # Numeric but not code
        cand = c.opcode[0:i]
        if cand not in candidates:
            candidates.append(cand)

    # This doesn't need any fixing
    newLines.append(r)

# These are numeric constants we did not process
# for c in candidates:
#    print c

for x in xrange(len(newLines)):
    if not newLines[x].endswith("\n"):
        print ":" + newLines[x] + ":"

with open(OUT_FILE, "w") as f:
    f.writelines(newLines)

# print_ram_hits()
