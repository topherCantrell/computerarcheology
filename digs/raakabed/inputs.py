import json

from objects import Objects


class DecodedInput:
    
    def __init__(self,original):
        
        self.original = original
        
        self.frags = []        
        self.command_target = None
        self.verb = None              
        self.first_adjective = None
        self.first_noun = None
        self.first_noun_pos = None
        self.preposition = None
        self.second_adjective = None
        self.second_noun = None
        self.second_noun_pos = None
        
        self.error_message = None  
    
class Inputs:
    
    def __init__(self,words_fname,phrases_fname,objs):
        self._objs = objs
        with open(words_fname) as f:
            raw_words = json.load(f)
        self._words = {}
        for typ in raw_words:
            col = self._collect_words(typ['words'])
            self._words[typ['type']] = col
        with open(phrases_fname) as f:
            self.raw_phrases = json.load(f)
        self._phrases = []
        for phr in self.raw_phrases:
            vrb = phr['verb']
            if vrb[0:2] != '??' and self._words['verbs'][vrb]!=None:
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
        ret = DecodedInput(inp)
                
        inp = inp.split(' ')
        for i in inp:
            i = i.upper().strip()
            if not i:
                continue
            tok = self.find_word(i)
            if tok and tok[1]!='ignores':
                ret.frags.append(tok)
        
        #verb = None        
        #command_target = None
        #first_adjective = None
        #first_noun = None
        #first_noun_pos = -1
        #second_adjective = None
        #second_noun = None
        #second_noun_pos = -1
        #preposition = None
        
        prepGiven = False
        adj = None        
                                
        # Verb   1stNoun      Prep    2ndNoun
        # GET    GREEN KEY    WITH    YELLOW HOOK
        for i in range(len(ret.frags)):
            w = ret.frags[i]
            if w[1]=='verbs':
                ret.verb = w[0]
                
            elif w[1]=='adjectives':
                adj = w[0]
                
            elif w[1]=='prepositions':
                ret.preposition = w[0]
                prepGiven = True         
                
            elif w[1]=='nouns':
                if prepGiven:                    
                    ret.second_noun = w[0]
                    ret.second_adjective = adj
                    ret.second_noun_pos = i                    
                else:
                    ret.second_noun = ret.first_noun
                    ret.second_adjective = ret.first_adjective
                    ret.second_noun_pos = i
                    ret.first_noun = w[0]
                    ret.first_adjective = adj
                    ret.first_noun_pos = i
                adj = None
                prepGiven = False            
            else:
                raise Exception('Unknown word type: '+w[1])
        
        # Original coco raka code at 0736
        
        if not ret.verb:
            ret.error_message = 'You must use a VERB.'
            return ret
        
        if ret.first_noun:
            nd = self._objs.get_object_nearby(ret.first_adjective,ret.first_noun)
            if not nd:
                ret.error_message = 'I do not see '+ret.first_noun+'.'
                return ret
            if len(nd)>1:
                ret.error_message = 'Which '+ret.first_noun+' ?'
                return ret
            ret.first_noun = nd[0]
            
        if ret.second_noun:
            nd = self._objs.get_object_nearby(ret.second_adjective,ret.second_noun)
            if not nd:
                ret.error_message = 'I do not see '+ret.second_noun+'.'
                return ret
            if len(nd)>1:
                ret.error_message = 'Which '+ret.second_noun+' ?'
                return ret
            ret.second_noun = nd[0]
            
            # TODO ATTACK SERPEN WITH SWORD
            # Does the sword have to be in your pack?
        
        phs = []
        for ph in self.raw_phrases:
            if ph['verb'] == ret.verb:
                if 'preposition' in ph and ret.preposition!=ph['preposition']:
                    # TODO Preposition mismatch error message?
                    # TODO No preposition error message?
                    continue
                
                if 'first_noun' in ph:
                    if not ret.first_noun:
                        continue
                    if not self._objs.has_bit(ret.first_noun,ph['first_noun']):
                        continue
                
                if 'second_noun' in ph:
                    if not ret.second_noun:
                        continue
                    if not self._objs.has_bit(ret.second_noun,ph['second_noun']):
                        continue
                
                phs.append(ph)
                #print('#1',ret.first_noun)
                #print('#2',ret.second_noun)
        
        if len(phs)==1:
            ret.phrase = phs[0]
            return ret
        
        if phs:
            ret.error_message = 'Multiple phrases'
            return ret
        
        ret.error_message = 'No phrase'
        return ret
                
            
if __name__ == '__main__':
    
    objs = Objects('objects_raaka_trs80.json')
    
    objs.o['SERPENT_LIVE']['location'] = objs.player['location'] # Serpent
    objs.o['SWORD']['location'] = objs.player_number # Sword
        
    inp = Inputs('words_raaka_trs80.json','phrases_raaka_trs80.json',objs)
    d = inp.decode('  Hit the   serpent  with sword   ')
    print(d.frags)
    print(d.error_message)
    print(d.phrase)