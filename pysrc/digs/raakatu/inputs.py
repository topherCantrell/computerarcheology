import json

class Inputs:
    
    def __init__(self,words_fname,phrases_fname):
        with open(words_fname) as f:
            raw_words = json.load(f)
        self._words = {}
        for typ in raw_words:
            col = self._collect_words(typ['words'])
            self._words[typ['type']] = col
        with open(phrases_fname) as f:
            raw_phrases = json.load(f)
        self._phrases = []
        for phr in raw_phrases:
            vrb = phr['verb']
            if vrb != '??' and self._words['verbs'][vrb]!=None:
                raise Exception('Phrase verb '+vrb+' is not a root verb in the words table.')
            prep = '*'
            first = '*'
            second = '*'
            if 'preposition' in phr:
                prep = phr['preposition']
            if 'first_noun' in phr:
                first = phr['first_noun']
            if 'second_noun' in phr:
                second = phr['second_noun']
            p = vrb+' '+first+' '+prep+' '+second
            self._phrases.append(p)
        
    def _collect_words(self,word_list):
        ret = {}
        for word in word_list:
            if word['id'] in ret:
                ret[word['id']].append(word['word'])
            else:
                ret[word['id']] = [word['word']]
        ret2 = {}
        for ent in ret:
            words = ret[ent]
            ret2[words[0]] = None
            if len(words)>1:
                for w in words[1:]:
                    ret2[w] = words[0]                   
        return ret2
    
    def _is_match(self,cand,word):
        if len(word)==6:
            return cand.startswith(word)
        return cand==word
    
    def find_word(self,word):
        for typ in self._words:            
            for w in self._words[typ]:
                if self._is_match(word,w):
                    trns = self._words[typ][w]
                    if trns:
                        w = trns                    
                    return (w,typ) 
        return None
    
    def decode(self,inp):
        # Build a list of known words. Ignore words we don't know. The list includes the word and the list (verb, noun, prep, etc).
        # The "ignores" are ignored.
        ret = []
        inp = inp.split(' ')
        for i in inp:
            i = i.upper().strip()
            if not i:
                continue
            tok = self.find_word(i)
            if tok and tok[1]!='ignores':
                ret.append(tok)
        
        verb = None        
        command_target = None
        first_adjective = None
        first_noun = None
        first_noun_pos = -1
        second_adjective = None
        second_noun = None
        second_noun_pos = -1
        preposition = None
        
        prepGiven = False
        adj = None        
                                
        #           1st             2nd
        # GET GREEN KEY WITH YELLOW HOOK
        for i in range(len(ret)):
            w = ret[i]
            if w[1]=='verbs':
                verb = w[0]
                
            elif w[1]=='adjectives':
                adj = w[0]
                
            elif w[1]=='prepositions':
                preposition = w[0]
                prepGiven = True         
                
            elif w[1]=='nouns':
                if prepGiven:                    
                    second_noun = w[0]
                    second_adjective = adj
                    second_noun_pos = i                    
                else:
                    second_noun = first_noun
                    second_adjective = first_adjective
                    second_noun_pos = i
                    first_noun = w[0]
                    first_adjective = adj
                    first_noun_pos = i
                adj = None
                prepGiven = False            
            else:
                raise Exception('Unknown word type: '+w[1])
        
        # 0736
        
        print('target',command_target)
        print('verb',verb)              
        print('1stAdjective', first_adjective)
        print('1stNoun', first_noun)
        print('1stNounPos',first_noun_pos)
        print('Preposition', preposition)
        print('2ndAdjective',second_adjective)
        print('2ndNoun', second_noun)
        print('2ndNounPos', second_noun_pos)
        
        # In original, "GET AAA" will tell you that you already have the first object in your pack.
        
        # If no verb, error "?VERB?"
        
        # Decode the two nouns. Look in the room and pack for things like multiple "DOOR" but no adjectives given and error "?WHICH?" for it. If the noun doesn't decode error "?WHAT?" for it.
        
        return ret        
        
            
if __name__ == '__main__':
    inp = Inputs('words.json','phrases.json')
    d = inp.decode('  Hit the   serpent  with sword   ')
    print(d)