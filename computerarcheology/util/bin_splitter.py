
with open("content/nes/kidicarus/roms/kidicarus.nes", "rb") as file:          
    content = file.read()
    print('>>>',len(content))

    n = -1
    for i in range(16,16+8*1024*16, 1024*16):
        n+=1
        bin = content[i:i+1024*16]
        with open(f"content/nes/kidicarus/roms/bank{n}.bin", "wb") as file:
            file.write(bin)

