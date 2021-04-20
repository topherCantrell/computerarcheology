
class MemoryMapEntry:
    def __init__(self, first, last, name, description, special):
        self.first = first
        self.last = last
        self.name = name
        self.description = description
        self.special = special
        
class MemoryMap:
    
    def __init__(self, paras):
        self.entries = []
        
        for i in range(len(paras)):
            para = paras[i]
            if para[0]=='TABLE' and paras[i-1][0]=='META' and paras[i-1][1]=='>>> memory':        
                for p in para[3:]:                    
                    data = p.split('|')[1:-1]
                    i = data[0].find(':')
                    if i>=0:
                        first_txt = data[0][:i].strip()
                        last_txt = data[0][i+1:].strip()
                    else:
                        first_txt = data[0].strip()
                        last_txt = first_txt
                    special = None
                    for i in range(len(first_txt)):
                        if first_txt[i] in 'pwr':
                            special = first_txt[i:]
                            first_txt = first_txt[:i]
                            break
                    for i in range(len(last_txt)):
                        if last_txt[i] in 'pwr':
                            last_txt = last_txt[:i]
                            break
                        
                    try:
                        first = int(first_txt,16)
                        last = int(last_txt,16)
                        self.entries.append(MemoryMapEntry(first,last,data[1].strip(),data[2].strip(),special))
                    except Exception:
                        raise Exception('Invalid map entry:'+data[0])
