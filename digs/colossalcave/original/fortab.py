# with open('adventure.f') as f:
#     for line in f:        
#         if line.startswith('C') or not line.strip():
#             print(line.strip())
#             continue
#         line = line.replace('\t', '    ')
#         label = ''
#         cont_char = ' '
#         if line[0].isnumeric():            
#             i = line.find(' ')
#             label = line[:i]      
#             line = line[i+1:]                
#         line = line.strip()
#         if line[0].isnumeric():
#             cont_char = line[0]
#             line = line[1:].strip()
#         line = line.strip()

#         a = label.ljust(5,' ')
#         print(a+cont_char+line)

with open('adventure.dat') as f:
    for line in f:
        tabs = line.split('\t')
        tabs[-1] = tabs[-1][:-1]
        g = ''
        for i, t in enumerate(tabs):
            if i==0:
                g += t.ljust(5,' ')
            else:
                g += '  ' + t
        print(g)