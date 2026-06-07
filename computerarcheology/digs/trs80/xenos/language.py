
with open("content/trs80/xenos/Code.md", "r") as f:

    PHRASES = {
    }

    WORDS = [
        {}, # Verbs
        {}, # Nouns
        {}, # Adjectives
        {}, # Adverbs
    ]

    g = ''
    while not g.startswith('72E1:'):
        g = f.readline()
    g = g.strip()
    while not g.startswith('7629:'):              
        i = g.find(';')
        if i<0:
            g = f.readline()
            g = g.strip()
            continue
        g = g[i+1:].strip()

        wn = int(g[:2], 16)        
        phrase = g[5:].strip()
        if wn in PHRASES:
            PHRASES[wn].append(phrase)
        else:
            PHRASES[wn] = [phrase] 

        g = f.readline()
        g = g.strip()
    
    word_list = 0
    while not g.startswith('762D:'):
        g = f.readline()
    g = g.strip()
    while not g.startswith('7D4E:'):
        if len(g) < 5 or g[4] != ':':
            g = f.readline()
            g = g.strip()
            continue
        if g[4:]== ': 00':
            word_list += 1
            g = f.readline()
            g = g.strip()
            continue

        # 762D: 04 52 45 41 44               01 ; READ
        i = g.find(';')
        wn = int(g[i-3:i-1], 16)
        text = g[i+1:].strip()
        if wn in WORDS[word_list]:
            WORDS[word_list][wn].append(text)
        else:
            WORDS[word_list][wn] = [text]        

        g = f.readline()
        g = g.strip()
