import script_cursor

if __name__ == "__main__":    
    with open('d:/git/computerarcheology/content/trs80/xenos/roms/xenos.bin', 'rb') as f:
        RAW = f.read()
    cursor = script_cursor.ScriptCursor(RAW, 0x5D00)
    cursor.set_pos(0x7D4F)
    mlength = cursor.decode_length([])
    end_of_coms = mlength + cursor.pos


    # None of the general commands should reference room descriptions (other than objects)
    # There is no need to pass in a valid disk section number for room name lookup
    cursor.decode_command_list(end_of_coms, None, 0)
