SCALE_FACTOR = [
    2,
    4,
    8,
    16,
]

with open("content/arcade/asteroids/vectorrom.md") as f:
    with open("content/arcade/asteroids/t.txt", "w") as out:        
        for line in f:
            if len(line)>4 and line[4] == ':' and 'SVEC' in line:
                i = line.index('scale=')+6
                j = line.index('(',i)
                scale = int(line[i:j])
                i = line.index('bri=')+4
                j = line.index(' ',i)
                bri = int(line[i:j].strip())                
                i = line.index('x=')+2
                j = line.index(' ',i)
                x = int(line[i:j].strip())
                i = line.index('y=')+2
                j = line.index(' ',i)
                y = int(line[i:j].strip())
                # print(scale,bri,x,y)

                field_scale = f'scale=0{scale}(*{SCALE_FACTOR[scale]})'.ljust(15)
                field_bri = f'bri={bri}'.ljust(10)
                field_x = f'x={x}'.ljust(10)
                field_y = f'y={y}'.ljust(10)
                fx = x * SCALE_FACTOR[scale]
                fy = y * SCALE_FACTOR[scale]                         


                line = line[:30] + field_scale+field_bri+field_x+field_y+f'({fx:.4f}, {fy:.4f})\n'

            out.write(line)

