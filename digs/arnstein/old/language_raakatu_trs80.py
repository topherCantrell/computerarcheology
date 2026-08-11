
class Language:
    def __init__(self):

        self.verbs = {}
        self.nouns = {}
        self.words = [
            {}, # verbs
            {}, # nouns
            {}, # adjectives
            {}  # prepositions
        ]
        self.phrases = {}

        with open("d:/git/computerarcheology/content/trs80/raakatu/Code.md", "r") as f:            

            g = ''
            while not g.startswith('50B9:'): # Start of phrases
                g = f.readline()
            g = g.strip()
            while not g.startswith('52C1:'): # End of phrases 
                i = g.find(';')
                if i<0:
                    g = f.readline()
                    g = g.strip()
                    continue
                g = g[i+1:].strip()

                wn = int(g[:2], 16)        
                phrase = g[5:].strip()
                if wn in self.phrases:
                    self.phrases[wn].append(phrase)
                else:
                    self.phrases[wn] = [phrase] 

                g = f.readline()
                g = g.strip()
            
            word_list = 0
            while not g.startswith('52C3:'):  # Start of words
                g = f.readline()
            g = g.strip()
            while not g.startswith('5650:'): # End of words
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
                if wn in self.words[word_list]:
                    self.words[word_list][wn].append(text)
                else:
                    self.words[word_list][wn] = [text]        

                g = f.readline()
                g = g.strip()

        def get_verb(self, num):
            return self.words[0][num][0]

        def get_noun(self, num):
            if num not in self.words[1]:
                return f'??{num:02X}??'
            return self.words[1][num][0]

        def get_adjective(self, num):
            return self.words[2][num][0]

        def get_preposition(self, num):
            return self.words[3][num][0]

        def get_phrase(self, num):
            if num not in self.phrases:
                return f'??{num:02X}??'
            ret = self.phrases[num][0]
            return ' '.join(ret.split())    

def print_format_words(words):
    for num, word_list in words.items():
        print(f"{num}: {word_list},") 


if __name__ == '__main__':
    lamg = Language()
    # print_format_words(lamg.phrases)
    # print(f"Phrases: {lamg.phrases}")
    print_format_words(lamg.words[0])
    print()
    print_format_words(lamg.words[1])
    print()
    print_format_words(lamg.words[2])
    print()
    print_format_words(lamg.words[3])
    print()
    # print(f"Verbs: {lamg.words[0]}")
    # print(f"Nouns: {lamg.words[1]}")
    # print(f"Adjectives: {lamg.words[2]}")
    # print(f"Prepositions: {lamg.words[3]}")
