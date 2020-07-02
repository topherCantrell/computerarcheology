from util.content_path import get_content_path
import util.util as U
from digs.raakatu import raakatu_commands as RTC
from digs.raakatu import object_attributes as OBJ
from digs.raakatu import extract_code as EC
import json

# Nothing in the code ... best we can do is make lists here

OBJECT_SHORT_NAMES = {
    0x00 : 'nowhere',
    0x01 : 'BOTTLE', # Word is not in CoCo version
    0x1D : 'PLAYER',
    0x24 : 'GUARD REPORTER',
    0x2E : 'CORNER',
    0x3C : 'AMBIENT SOUNDS',
    0xFF : 'everywhere',
}

ROOM_SHORT_NAMES = {
    0x81 : 'Small room granite walls',
    0x82 : 'Oriental rug',
    0x83 : 'Dark passage',
    0x84 : 'Top of a passage',
    0x85 : 'T-shaped room 1',
    0x86 : 'Gray stone walls 1',
    0x87 : 'Round room high walls 1',
    0x88 : 'Triangular room',
    0x89 : 'South end central hall',
    0x8A : 'T-shaped room 2',
    0x8B : 'Grey stone walls 2', # Not the 'GRAY stone walls'
    0x8C : 'Round room high walls 2',
    0x8D : 'Petite chamber',
    0x8E : 'Smells of decaying flesh',
    0x8F : 'Tall room',
    0x90 : 'North end central hall',
    0x91 : 'Vault',
    0x92 : 'Entrance long dark tunnel west',
    0x93 : 'Dark tunnel',
    0x94 : 'Entrance long dark tunnel east',
    0x95 : 'Large room',
    0x96 : 'Dense dark damp jungle',
    0x97 : 'Dark dense damp jungle',
    0x98 : 'See east wall',
    0x99 : 'Stands south wall',
    0x9A : 'See bronze gates',
    0x9B : 'See north wall',
    0x9C : 'Standing west entrance',
    0x9D : 'At north wall',
    0x9E : 'At east wall',
    0x9F : 'At south wall',
    0xA0 : 'Very small room',
    0xA1 : 'Small room',
    0xA2 : 'Dark damp dense jungle',
    0xA3 : 'Dense damp dark jungle',
    0xA4 : 'Damp dark dense jungle',
    0xA5 : 'Secret passage',
    0xA6 : 'End of the passage',
}

HELPER_SHORT_NAMES = {
    0x81: 'ResetGame',
    0x82: 'DeathByStatue',
    0x83: 'Manipulate',
    0x84: 'PrintPeriod',
    0x85: 'PrintGuardsMarchRight',
    0x86: 'PrintGuardsAroundCorner',
    0x87: 'PrintGuardsDisappearLeft',    
    0x88: 'PrintTheNOUNIsNotBurning',    
    0x89: 'PrintCantJumpThatFar',
    0x8A: 'DeathByRugSpike',
    0x8B: 'DeathByHiddenRugSpike',
    0x8C: 'PrintDiscoverPit',
    0x8D: 'PrintStatueTooHeavy',
    0x8E: 'PrintMoveAlter',
    0x8F: 'EnterSecretPassage',
    0x90: 'PrinteAlterMovesBack',
    0x91: 'SealUpHole',
    0x92: 'PrintScore',
    0x93: 'InvalidClimbInOrOut',
    0x94: 'PrintUseDirections',
    0x95: 'ResetDungeon',
    0x96: 'PrintGoodWayToLoseHand',
    0x97: 'PrintMouthImGame',
    0x98: 'PrintGiantLeapForYou'    
}

def DECODE_ROOM_NAME(rn,full=True):
    if rn in ROOM_SHORT_NAMES:
        return ROOM_SHORT_NAMES[rn]
    else:
        return 'Room_'+U.hex2(rn)
    
def DECODE_HELPER_NAME(hn):
    if hn in HELPER_SHORT_NAMES:
        return HELPER_SHORT_NAMES[hn]
    else:
        return 'HelperFunction_'+U.hex2(hn)
    
RTC.set_decode_helper(DECODE_HELPER_NAME)
RTC.set_decode_room(DECODE_ROOM_NAME)

class Raaka:
        
    def __init__(self,config):
        self._file = config['file']
        self._origin = config['origin']
        self._word_data = config['word_data']
        self._phrase_data = config['phrase_data']
        self._object_data = config['object_data']
        self._general_commands_data = config['general_commands_data']
        self._helper_commands_data = config['helper_commands_data']
        self._room_descriptions_data = config['room_descriptions_data']
        
        with open(get_content_path(self._file),'rb') as f:
            self._binary = bytes([0]*self._origin)+f.read()
            
        self._words = self.load_words()
        self._phrases = self.load_phrases()
        
        self._general_commands = self.load_general_script()
        self._helper_commands = self.load_helper_commands()
        self._room_descriptions = self.load_room_descriptions()
        self._objects = self.load_object_data()
            
    def _parse_words_bin(self,pos):
        ret = []
        data = self._binary       
        while True:
            if data[pos] == 0:
                return pos+1,ret
            n = data[pos]
            pos+=1
            
            word = data[pos:pos+n]
            word_num = data[pos+n]
            ret.append({
                'text' : word.decode(),
                'num' : word_num
                })
                            
            pos = pos + n + 1
                    
    def find_noun_word(self,index): 
        # Number is the INDEX, not the word number        
        if index in OBJECT_SHORT_NAMES:
            return OBJECT_SHORT_NAMES[index]
                
        obj = self._objects[index-1]        
        for n in self._words['nouns']:            
            if n['num']==obj['word']:
                return n['text']
                
        return '??'+U.hex2(index)
            
    def load_words(self):
        words = {}
        pos = self._word_data
        pos,words['ignores'] = self._parse_words_bin(pos)
        pos,words['verbs'] = self._parse_words_bin(pos)
        pos,words['nouns'] = self._parse_words_bin(pos)
        pos,words['adjectives'] = self._parse_words_bin(pos)
        pos,words['prepositions'] = self._parse_words_bin(pos)
        RTC.set_decode_noun(self.find_noun_word)
        RTC.set_decode_bits(OBJ.decode_noun)
        return words

    def _print_word_list(self,wtype,pos):
        print('; --- '+wtype.upper()+' ---')        
        for w in self._words[wtype]:               
            s = U.hex4(pos)+': ';
            s += U.hex2(len(w['text']))+' '        
            for c in w['text']:
                s += U.hex2(ord(c)) + ' '       
            s += U.hex2(w['num'])
            s = s.ljust(32)+'; '+w['text'].ljust(9)+U.hex2(w['num'])    
            print(s)
            pos += len(w['text'])+2
        print(U.hex4(pos)+': 00')
        print(';')
        return pos+1
        
    def print_words(self):
        pos = self._word_data
        pos = self._print_word_list('ignores',pos)
        pos = self._print_word_list('verbs',pos)
        pos = self._print_word_list('nouns',pos)
        pos = self._print_word_list('adjectives',pos)
        pos = self._print_word_list('prepositions',pos)
        
    def tojson_words(self):
        ret = []
        for types in ['ignores','verbs','nouns','adjectives','prepositions']:
            sub = []
            for w in self._words[types]:
                wj = {'word':w['text'],'id':w['num']}
                sub.append(wj)
            ret.append({'type':types,'words':sub})        
        return ret
    
    def load_phrases(self):
        pos = self._phrase_data
        data = self._binary
        phrases = []
        
        while data[pos]!=0:
            phr = data[pos:pos+5]
            pos += 5
            phrases.append(phr)
            
        RTC.set_decode_phrase(self.get_text_phrase)
                    
        return phrases

    def find_word(self,wtype,word_num):
        for w in self._words[wtype]:
            if w['num'] == word_num:
                return w
        return None
    
    def get_text_phrase(self,number, full=True):
        for phr in self._phrases:
            if phr[-1] == number:
                wr = self.find_word('verbs',phr[0])
                if wr:
                    wrt = wr['text']
                else:
                    wrt = '??'
                    
                if phr[1]:
                    w2 = self.find_word('prepositions',phr[1])['text']
                else:
                    w2 = '*'
                    
                na = OBJ.decode_noun(phr[2])
                nb = OBJ.decode_noun(phr[3])
                                                       
                if full:                               
                    return '"'+U.hex2(phr[-1])+': '+wrt.ljust(8)+na.ljust(10)+w2.ljust(8)+nb.ljust(10)+'"'
                else:
                    return wrt+' '+na+' '+w2+' '+nb
        return "??? Phrase "+U.hex2(number)+" not found"
                
    def tojson_phrases(self):
        ret = []
        for phr in self._phrases:            
            wr = self.find_word('verbs',phr[0])
            if wr:
                wrt = wr['text']
            else:
                wrt = '??'
                
            if phr[1]:
                w2 = self.find_word('prepositions',phr[1])['text']
            else:
                w2 = '*'
                
            na = OBJ.decode_noun(phr[2])
            nb = OBJ.decode_noun(phr[3])
            
            r = {'verb':wrt}
            if na!='*':
                r['first_noun'] = na
            if w2!='*':
                r['preposition'] = w2
            if nb!='*':
                r['second_noun'] = nb            
            
            ret.append(r)
        return ret
        
    def print_phrases(self):
        pos = self._phrase_data
        
        for phr in self._phrases:
            s = U.hex4(pos)+': '
            for i in phr:
                s = s + U.hex2(i)+' '
                
            wr = self.find_word('verbs',phr[0])
            if wr:
                wrt = wr['text']
            else:
                wrt = '??'
                
            if phr[1]:
                w2 = self.find_word('prepositions',phr[1])['text']
            else:
                w2 = '*'
                
            na = OBJ.decode_noun(phr[2])
            nb = OBJ.decode_noun(phr[3])
                                                                                  
            com = '; '+U.hex2(phr[-1])+': '+wrt.ljust(8) + na.ljust(10) +  w2.ljust(8)  + nb.ljust(10)
                            
            print(s,com)  
            pos += 5
            
        print(U.hex4(pos)+': 00')
    
    def read_length(self,pos,data=None):
        if not data:        
            data = self._binary
        if data[pos]>=0x80:
            sz = (data[pos]&0x7F)*256 + data[pos+1]
            return sz,pos+2
        else:
            return data[pos],pos+1    
        
    def load_general_script(self):
        pos = self._general_commands_data
                
        pos+=1
        sz,pos = self.read_length(pos)
        end_pos = pos + sz
        
        ret = []
        
        while pos < end_pos:
            ret.append(RTC.decode_script(self._binary[pos:pos+sz]))            
            pos += sz
            
        if len(ret)!=1 or len(ret[0])!=1:
            raise Exception('Expected only one')
        return ret[0][0]
     
    def load_room_descriptions(self):
        pos = self._room_descriptions_data
        data = self._binary
                
        pos+=1
        sz,pos = self.read_length(pos)
        end_pos = pos + sz
        
        ret = []
        
        while pos < end_pos:        
            
            rn = data[pos]
            pos+=1
            sz,pos = self.read_length(pos)
            
            oend = pos+sz
            
            dat = data[pos]
            pos += 1
            
            atts = []
            
            while pos!=oend:
                com = data[pos]
                pos += 1
                csz,pos = self.read_length(pos)
                sdata = self._binary[pos:pos+csz]
                
                att = OBJ.OBJ_ATTRIBUTES[com]()
                #print(U.hex4(pos))
                att.parse_binary(sdata)
                atts.append(att)
                                                    
                pos += csz     
                
            ret.append({'room':rn, 'data' : dat, 'attributes':atts})            
        
        return ret    
        
    def load_helper_commands(self):
        pos = self._helper_commands_data
        data = self._binary
                
        pos+=1
        sz,pos = self.read_length(pos)
        end_pos = pos + sz
        
        ret = []
        
        while pos < end_pos:                        
            
            hn = data[pos]
            pos+=1
            hz,pos = self.read_length(pos)
            #print(U.hex4(pos),U.hex4(pos+hz))
            scr =  RTC.decode_script(self._binary[pos:pos+hz])
            h = {'number' : hn, 'script' : scr}
            #print(h)
            
            ret.append(h)
            pos += hz
            
        #print(len(ret))
        return ret
        
        
    def load_object_data(self):
        pos = self._object_data        
        data = self._binary
        
        pos+=1
        sz,pos = self.read_length(pos)
        end_pos = pos + sz
                    
        ret = []
        
        while pos < end_pos:        
            #porg = pos 
            word = data[pos]
            pos+=1
            sz,pos = self.read_length(pos)  
            oend = pos+sz          
            loc = data[pos]
            score = data[pos+1]
            params = data[pos+2]
            pos+=3
            
            obj = {       
                'word' : word,     
                'location' : loc,
                'score' : score,
                'bits' : params,
                'bits_decode' : OBJ.decode_noun(params,False)
                }
            ret.append(obj)
            #print(U.hex4(porg),obj)
            
            atts = []
            
            while pos!=oend:
                com = data[pos]
                pos += 1
                csz,pos = self.read_length(pos)
                sdata = self._binary[pos:pos+csz]
                
                att = OBJ.OBJ_ATTRIBUTES[com]()
                #print(U.hex4(pos))
                att.parse_binary(sdata)
                atts.append(att)
                                                    
                pos += csz          
                
            obj['attributes'] = atts 
            
        return ret

    def compare_binary(self,start,data):
        for i in range(len(data)):
            if self._binary[start+i] != data[i]:
                raise Exception('DIFFERENT '+U.hex4(start+i)+': '+U.hex2(data[i])+' '+U.hex2(self._binary[start+i]))
            
    def print_general_commands(self):          
        
        data = self._general_commands.get_assembly()        
        pre = bytes([0])+RTC.BaseCommand.make_length_bytes(len(data))
        self.compare_binary(self._general_commands_data,pre+data)
                
        pos = self._general_commands_data
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; size='+U.hex4(len(data))
        print(U.indent_code(s,0))
        
        pos += len(pre)
        self._general_commands.print_assembly(pos,0)
        
    def tojson_general(self):
        return self._general_commands.tojson()
    
    def tojson_helpers(self):
        ret = []
        for common in self._helper_commands:
            h = {'number':common['number'],'name':DECODE_HELPER_NAME(common['number'])}
            ret.append(h)
            scr = []
            for com in common['script']:
                scr.append(com.tojson())
            h['script'] = scr
        return ret
        
                
    def print_helper_commands(self):        
        data = b''
        for common in self._helper_commands:
            cdata = b''
            for com in common['script']:
                cdata = cdata + com.get_assembly()
            data = data + bytes([common['number']]) + RTC.BaseCommand.make_length_bytes(len(cdata)) + cdata            
        pre = bytes([0])+RTC.BaseCommand.make_length_bytes(len(data))                
        self.compare_binary(self._helper_commands_data,pre+data)
        
        pos = self._helper_commands_data
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; size='+U.hex4(len(data))
        print(U.indent_code(s,0))
        pos += len(pre)
                       
        for helper in self._helper_commands:
            cdata = b''
            for com in helper['script']:
                cdata = cdata + com.get_assembly()              
            pre = bytes([helper['number']]) + RTC.BaseCommand.make_length_bytes(len(cdata))
            s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; Function='+U.hex2(helper['number'])+'('+DECODE_HELPER_NAME(helper['number'])+') size='+U.hex4(len(cdata))
            print(';')
            print('; '+DECODE_HELPER_NAME(helper['number']))
            print(U.indent_code(s,0))
            pos += len(pre)            
            for com in helper['script']:
                pos = com.print_assembly(pos,0)
        
    def tojson_room_descriptions(self):
        ret = []
        
        for room in self._room_descriptions:
            r = {'name' : DECODE_ROOM_NAME(room['room'],full=False)}
            ret.append(r)
            for att in room['attributes']:
                att.tojson(r)
            
        return ret    
        
    def print_room_descriptions(self):
        data = b''
        for room in self._room_descriptions:            
            adata = b''
            for att in room['attributes']:
                d = att.get_assembly()
                adata = adata  + d
            adata = bytes([room['room']]) + RTC.BaseCommand.make_length_bytes(len(adata)+1) + bytes([room['data']]) + adata            
            data = data + adata
        
        pre = bytes([0])+RTC.BaseCommand.make_length_bytes(len(data))        
        self.compare_binary(self._room_descriptions_data,pre+data)
        pos = self._room_descriptions_data
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; '
        print(U.indent_code(s,0))
        pos += len(pre)
        
        for room in self._room_descriptions:
            adata = b''
            for att in room['attributes']:
                d = att.get_assembly()
                adata = adata  + d                        
            print(';')
            print('; '+DECODE_ROOM_NAME(room['room']))
            pre = bytes([room['room']]) + RTC.BaseCommand.make_length_bytes(len(adata)+1)
            s = U.hex4(pos)+': '+U.dump_bytes(pre)+' '+U.hex2(room['data'])+' ; roomNumber='+U.hex2(room['room'])+'('+DECODE_ROOM_NAME(room['room'])+')'+' size='+U.hex4(len(adata)+1)+' data='+U.hex2(room['data'])
            print(U.indent_code(s,0))
            pos += len(pre)+1
            for att in room['attributes']:
                pos = att.print_assembly(pos,1)                      
    
    def tojson_objects(self):
        ret = []
        
        num = 1
        for obj in self._objects:
            r = {'name' : self.find_noun_word(num),'location' : DECODE_ROOM_NAME(obj['location']), 'score':obj['score'], 'bits':OBJ.decode_noun(obj['bits'],False)}
            num += 1
            
            ret.append(r)
            
            for att in obj['attributes']:
                att.tojson(r)
            
        return ret
                
    def print_object_data(self):
        
        data = b''
        for obj in self._objects:
            aa = obj['location']
            bb = obj['score']
            cc = obj['bits']
            adata = bytes([aa,bb,cc])
            for att in obj['attributes']:
                d = att.get_assembly()
                adata = adata  + d                 
            data = data + bytes([obj['word']])+RTC.BaseCommand.make_length_bytes(len(adata)) + adata                    
            
        pos = self._object_data
        pre = bytes([0])+RTC.BaseCommand.make_length_bytes(len(data))
        self.compare_binary(self._object_data,pre+data)
        
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; size='+U.hex4(len(data))
        print(U.indent_code(s,0))
        pos += len(pre)
        
        num = 1
        data = b''
        for obj in self._objects:
            print(';')
            print('; Object_'+U.hex2(num)+' "'+self.find_noun_word(num)+'"')
            num+=1
            aa = obj['location']
            bb = obj['score']
            cc = obj['bits']
            adata = bytes([aa,bb,cc])
            for att in obj['attributes']:
                d = att.get_assembly()
                adata = adata  + d           
            pre = bytes([obj['word']])+RTC.BaseCommand.make_length_bytes(len(adata))
            s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; word='+U.hex2(obj['word'])+' size='+U.hex4(len(adata))
            print(U.indent_code(s,0))                  
            pos += len(pre)
            s = U.hex4(pos)+': '+U.hex2(aa)+' '+U.hex2(bb)+' '+U.hex2(cc)+' ; room='+U.hex2(aa)+' scorePoints='+U.hex2(bb)+' bits='+U.hex2(cc)
            print(U.indent_code(s,0))
            pos += 3
            
            for att in obj['attributes']:
                pos = att.print_assembly(pos,1)
                
        return pos 
             
        
INFO_TRS80 = {
    'file' : 'TRS80/RaakaTu/RAAKA.bin',
    'origin' : 0x4300,
    'word_data' : 0x52C2,
    'phrase_data' : 0x50B9,
    'object_data' : 0x5651,
    'general_commands_data' : 0x73FB,
    'helper_commands_data' : 0x7BCD,
    'room_descriptions_data' : 0x681F,
}

INFO_COCO = {
    'file' : 'CoCo/RaakaTu/RaakaTu.bin',
    'origin' : 0x0600,
    'word_data' : 0x3C29,
    'phrase_data' : 0x135B,
    'object_data' : 0x20FF,
    'general_commands_data' : 0x323C,
    'helper_commands_data' : 0x37FA,
    'room_descriptions_data' : 0x1523,
}

trs80 = Raaka(INFO_TRS80)
#coco = Raaka(INFO_COCO)

plat = trs80
#plat.print_general_commands()
#plat.print_helper_commands()
#plat.print_room_descriptions()
#plat.print_object_data()
#plat.print_words()
#plat.print_phrases()

with open('rooms.json','w') as f:
    js = plat.tojson_room_descriptions()
    js = json.dumps(js,indent=2)
    f.write(js)
with open('objects.json','w') as f:
    js = plat.tojson_objects()
    js = json.dumps(js,indent=2)
    f.write(js)    
with open('general.json','w') as f:
    js = plat.tojson_general()
    js = json.dumps(js,indent=2)
    f.write(js)    
with open('helpers.json','w') as f:
    js = plat.tojson_helpers()
    js = json.dumps(js,indent=2)
    f.write(js)    
with open('words.json','w') as f:
    js = plat.tojson_words()
    js = json.dumps(js,indent=2)
    f.write(js)
with open('phrases.json','w') as f:
    js = plat.tojson_phrases()
    js = json.dumps(js,indent=2)
    f.write(js)

#plat.print_words()
#plat.print_phrases()

"""
with open('generated.txt') as f:
        lines = f.readlines()
        
start,dat = EC.extract_code(lines)

coco.compare_binary(start,dat)
#trs80.compare_binary(start,dat)
"""

