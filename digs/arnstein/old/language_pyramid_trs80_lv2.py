
class Language:
    def __init__(self):

        self.nouns = {}  # dataNumber -> [word]
        self.verbs = {}  # dataNumber -> [word]        

        with open("d:/git/computerarcheology/content/trs80/pyramid/Code.md", "r") as f:            

            g = ''
            while not g.startswith('56CE:'):
                g = f.readline()
            word_type = self.nouns
            g = g.strip()
            while not g.startswith('59AF:'):              
                if g.startswith('; Verbs'):
                    word_type = self.verbs
                i = g.find(';')                
                if i<=0: # -1 or ZERO -- skipping comment lines
                    g = f.readline()
                    g = g.strip()
                    continue
                a = g[:i].strip()
                b = g[i+1:].strip()

                word_text = b.split(' ')[-1]
                pos = a.find('  ')
                a = a[pos:].strip().split(' ')

                for wn in a:
                    n = int(wn, 16)
                    if n in word_type:
                        word_type[n].append(word_text)
                    else:
                        word_type[n] = [word_text]              

                g = f.readline()
                g = g.strip()
                
        def get_verb(self, num):
            return self.verbs[num][0]

        def get_noun(self, num):
            return self.nouns[num][0]       

def print_format_words(words):
    for num, word_list in words.items():
        print(f"{num}: {word_list}") 

if __name__ == '__main__':
    lamg = Language()
    # print(f"Verbs: {lamg.verbs}")
    # print(f"Nouns: {lamg.nouns}")    
    print_format_words(lamg.verbs)
    print()
    print_format_words(lamg.nouns)
