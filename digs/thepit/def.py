
with open('../../../content/arcade/thepit/Code.md') as f:
    for line in f:
        line = line.strip()
        if len(line)>4 and line[4]==':':
            i = line.find('DEFB')
            if i>0:                
                line = line[:i].strip() + line[i+7:].strip()
                line = line.replace(',$', ' ')
                line = line.replace('$', ' ')
        print(line)
