import script_cursor

# with open('content/trs80/xenos/roms/section9.bin', 'rb') as f:
#     RAW = f.read()
# cursor = script_cursor.ScriptCursor(RAW, 0x5200)
# cursor.decode_script()

with open('content/trs80/xenos/roms/xenos.bin', 'rb') as f:
    RAW = f.read()
cursor = script_cursor.ScriptCursor(RAW, 0x5D00)
cursor.pos = 0x7DBF-0x5D00
for _ in range(4):
    cursor.decode_command(0)
#cursor.decode_script()

# print()
# print()
# line = []
# origin = cursor.origin+cursor.pos
# while cursor.pos < len(cursor.data):
#     cursor.get_byte(line)
# cursor.print_data_run_ascii(origin, line,0)
