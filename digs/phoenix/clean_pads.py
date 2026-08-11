with open('./content/arcade/phoenix/tt.txt','w') as o:
    with open('./content/arcade/phoenix/code.md') as f:
        for line in f:

            line = line.strip()
            if len(line)>4 and line[4]==':' and line.endswith('`'):
                g = line.replace('`','').strip()
                while True:
                    line = f.readline().strip()
                    if(not line):                       
                        break
                    g = g + ' FF'    
                o.write(g+'\n\n')
            else:
                o.write(line+'\n')              
            
