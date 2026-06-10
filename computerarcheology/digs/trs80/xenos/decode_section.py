import script_cursor
import sys

SECTION_NUMBER = int(sys.argv[1])
with open(f'd:/git/computerarcheology/content/trs80/xenos/roms/section{SECTION_NUMBER}.bin', 'rb') as f:
    RAW = f.read()
cursor = script_cursor.ScriptCursor(RAW, 0x5200)
cursor.set_pos(0x5200)

# TODO look to see what section number
cursor.decode_script(SECTION_NUMBER)
