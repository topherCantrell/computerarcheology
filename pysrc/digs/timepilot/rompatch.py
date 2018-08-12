from tools import binary

src_file = "../../../content/arcade/timepilot/soundcode.mark"
bin_file = "../../../content/arcade/timepilot/roms/TM7"
mame_rom = "d:/mame/roms/timeplt/TM7"

len_same,data_same = binary.compare_source_to_binary(src_file, bin_file, 0)

if not len_same:
    raise Exception("Lengths are different")

if not data_same:
    print("Data is different")

data = binary.get_binary(src_file, 0)    
       
with open(mame_rom, mode="wb") as out:
    out.write(data)