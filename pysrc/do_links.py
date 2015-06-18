import cpu.find_links_Z80

IN_NAME = "../content/arcade/MoonPatrol/Code.cmark"
OUT_NAME = "new.cmark"

DO_RAM = True


# Load the raw lines
with open(IN_NAME) as f:
    raw = f.readlines()

# Get the right processor
proc = None
for r in raw:
    if ";;%%CPU" in r:
        i = r.index(";;%%CPU")
        proc = r[i + 7:].strip()
        break

if proc == "Z80":
    proc = cpu.find_links_Z80.FindLinksZ80()
# elif cpu == "6809":
#    cpu = find_links_6809.FindLinks6809

# Do the magic
new_lines = proc.process(raw, DO_RAM)

# Some sanity checking
for x in iter(range(len(new_lines))):
    if not new_lines[x].endswith("\n"):
        print ":" + new_lines[x] + ":"

# Write the lines
with open(OUT_NAME, "w") as f:
    f.writelines(new_lines)

# This is the RAM table
proc.print_ram_hits()
