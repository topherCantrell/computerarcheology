with open("content/trs80/xenos/roms2/xenos.bin", "rb") as f:
    fgood = f.read()

with open("content/trs80/xenos/roms/xenos.bin", "rb") as f:
    forg = f.read()

print(f"Lengths: {len(fgood)} vs {len(forg)}")

dc = 0
for i in range(len(fgood)):
    if fgood[i] != forg[i]:
        print(f"Difference at position {0x5D00+i:04X}: {fgood[i]:02X} vs {forg[i]:02X}")
        dc += 1
        if dc > 100:
            raise Exception("STOP")
