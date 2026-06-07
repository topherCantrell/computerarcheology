#with open("content/trs80/xenos/roms/XENOS.CMD.tst", "rb") as f:
#with open("content/trs80/xenos/roms/SECTION9.DAT", "rb") as f:
with open("content/trs80/xenos/roms2/section9.dat", "rb") as f:
    data = f.read()

with open("content/trs80/xenos/roms2/section9.bin","wb") as f:
    x = 93
    pos = 0
    while pos < len(data):
        print(f"{list(data[pos:pos+4])}")
        if data[pos+3] != x+1:
            print(f"Unexpected value {data[pos+3]} at position {pos}")
            x = data[pos+3] - 1
        pos += 4
        f.write(data[pos:pos+256])
        pos += 256
        x+=1
