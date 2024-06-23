with open('./content/arcade/phoenix/code.md') as f:
    for line in f:

        line = line.strip()

        if line.startswith(';topherchars'):
            break



#     for i in range(48):
#         line = f.readline().strip()
#         i = line.index(';')
#         addr = line[0:4]
#         data = line[6:i].strip()+' '
#         ndata = (len(data)+1)//3
#         dd = []
#         for i in range(ndata):
#             dd.append(f'{data[i*3:i*3+2]}')
        
#         g = f':{ndata//2}x2:'
#         for n in range(0,len(dd),2):
#             g = g + f'{dd[n]},'            
#         for n in range(0,len(dd),2):
#             g = g + f'{dd[n+1]},' 
#         g = g[:-1]
#         print(f"""##Object {addr}

# ```html
# <canvas width="460" height"140" data-colors="CM6"
#         data-command="{g}">
# </canvas>
# ```
# """)

    for i in range(13):
        line = f.readline().strip()
        i = line.index(';')
        addr = line[0:4]
        data = line[6:i].strip()+' '
        ndata = (len(data)+1)//3
        dd = []
        for i in range(ndata):
            dd.append(f'{data[i*3:i*3+2]}')
        
        g = f':4x4:'
        for n in range(0,len(dd),4):
            g = g + f'{dd[n]},'            
        for n in range(0,len(dd),4):
            g = g + f'{dd[n+1]},' 
        for n in range(0,len(dd),4):
            g = g + f'{dd[n+2]},' 
        for n in range(0,len(dd),4):
            g = g + f'{dd[n+3]},' 
        g = g[:-1]
        print(f"""##Object {addr}

```html
<canvas width="270" height="270" data-colors="CM6"
        data-command="{g}">
</canvas>
```
""")
        
        