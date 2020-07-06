from tools import binary
from tools import format as FORM

import util.util as U
from digs.raaka_bed import commands as RTC
from digs.raaka_bed import object_attributes as OBJ
from digs.raaka_bed import decoder_functions as FUN

class Decoder:    
       
    def decode_room_name(self,rn):
        if rn in self._room_short_names:
            return self._room_short_names[rn]
        else:
            return 'Room_'+U.hex2(rn)
    
    def decode_helper_name(self,hn):
        if hn in self._helper_names:
            return self._helper_names[hn]
        else:
            return 'HelperFunction_'+U.hex2(hn)    
        
    def __init__(self,config,object_short_names,room_short_names,helper_names):
        
        self._object_short_names = object_short_names
        self._room_short_names = room_short_names
        self._helper_names = helper_names
        
        self._file = config['binfile']
        self._codefile = config['codefile']
        self._origin = config['origin']
        self._word_data = config['word_data']
        self._phrase_data = config['phrase_data']
        self._object_data = config['object_data']
        self._general_commands_data = config['general_commands_data']
        self._helper_commands_data = config['helper_commands_data']
        self._room_descriptions_data = config['room_descriptions_data']
        self._command_table = config['command_table']
        
        FUN.decode_room_name = self.decode_room_name
        FUN.decode_helper_name = self.decode_helper_name
        FUN.decode_phrase = self.decode_phrase
        FUN.decode_noun = self.decode_noun
        FUN.decode_is_bedlam = self.decode_is_bedlam
                
        with open(self._file,'rb') as f:
            self._binary = bytes([0]*self._origin)+f.read()
            
        self._words = self.load_words()
        self._phrases = self.load_phrases()
        
        self._general_commands = self.load_general_script()
        self._helper_commands = self.load_helper_commands()
        self._room_descriptions = self.load_room_descriptions()
        self._objects = self.load_object_data()            
    
    def decode_is_bedlam(self):
        if 'edlam' in self._codefile:
            return True
        return False
            
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
                    
    def decode_noun(self,index): 
        # Number is the INDEX, not the word number        
        if index in self._object_short_names:
            return self._object_short_names[index]
                
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
        return words

    def _print_word_list(self,wtype,pos,out):
        out.append('; --- '+wtype.upper()+' ---')        
        for w in self._words[wtype]:               
            s = U.hex4(pos)+': ';
            s += U.hex2(len(w['text']))+' '        
            for c in w['text']:
                s += U.hex2(ord(c)) + ' '       
            s += U.hex2(w['num'])
            s = s.ljust(32)+'; '+w['text'].ljust(9)+U.hex2(w['num'])    
            out.append(s)
            pos += len(w['text'])+2
        out.append(U.hex4(pos)+': 00')
        out.append(';')
        return pos+1
        
    def print_words(self,out):
        pos = self._word_data
        pos = self._print_word_list('ignores',pos,out)
        pos = self._print_word_list('verbs',pos,out)
        pos = self._print_word_list('nouns',pos,out)
        pos = self._print_word_list('adjectives',pos,out)
        pos = self._print_word_list('prepositions',pos,out)
        del out[-1]
        
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
            
        #RTC.set_decode_phrase(self.get_text_phrase)
                    
        return phrases

    def find_word(self,wtype,word_num):
        for w in self._words[wtype]:
            if w['num'] == word_num:
                return w
        return None
    
    def decode_phrase(self,number, full=True):
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
                    
                na = FUN.decode_object_bits(phr[2])
                nb = FUN.decode_object_bits(phr[3])
                                                       
                if full:                               
                    # return '"'+U.hex2(phr[-1])+': '+wrt.ljust(8)+na.ljust(10)+w2.ljust(8)+nb.ljust(10)+'"'
                    return '"'+U.hex2(phr[-1])+': '+ wrt+' '+na+' '+w2+' '+nb+'"'
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
                
            na = FUN.decode_object_bits(phr[2])
            nb = FUN.decode_object_bits(phr[3])
            
            r = {'verb':wrt}
            if na!='*':
                r['first_noun'] = na
            if w2!='*':
                r['preposition'] = w2
            if nb!='*':
                r['second_noun'] = nb            
            
            ret.append(r)
        return ret
        
    def print_phrases(self,out):
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
                
            na = FUN.decode_object_bits(phr[2])
            nb = FUN.decode_object_bits(phr[3])
                                                                                  
            com = '; '+U.hex2(phr[-1])+': '+wrt.ljust(8) + na.ljust(10) +  w2.ljust(8)  + nb.ljust(10)
                            
            out.append(s+' '+com)  
            pos += 5
            
        out.append(U.hex4(pos)+': 00')
    
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
                'bits_decode' : FUN.decode_object_bits(params,False)
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
            
    def print_general_commands(self,out):          
        
        data = self._general_commands.get_assembly()        
        pre = bytes([0])+RTC.BaseCommand.make_length_bytes(len(data))
        self.compare_binary(self._general_commands_data,pre+data)
                
        pos = self._general_commands_data
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; size='+U.hex4(len(data))
        out.append(U.indent_code(s,0))
        
        pos += len(pre)
        self._general_commands.print_assembly(pos,0,out)
        
    def tojson_general(self):
        return self._general_commands.tojson()
    
    def tojson_helpers(self):
        ret = []
        for common in self._helper_commands:
            h = {'number':common['number'],'name':self.decode_helper_name(common['number'])}
            ret.append(h)
            scr = []
            for com in common['script']:
                scr.append(com.tojson())
            h['script'] = scr
        return ret
        
                
    def print_helper_commands(self,out):        
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
        out.append(U.indent_code(s,0))
        pos += len(pre)
                       
        for helper in self._helper_commands:
            cdata = b''
            for com in helper['script']:
                cdata = cdata + com.get_assembly()              
            pre = bytes([helper['number']]) + RTC.BaseCommand.make_length_bytes(len(cdata))
            s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; Function='+U.hex2(helper['number'])+'('+self.decode_helper_name(helper['number'])+') size='+U.hex4(len(cdata))
            out.append(';')
            out.append('; '+self.decode_helper_name(helper['number']))
            out.append(U.indent_code(s,0))
            pos += len(pre)            
            for com in helper['script']:
                pos = com.print_assembly(pos,0,out)
        
    def tojson_room_descriptions(self):
        ret = []
        
        for room in self._room_descriptions:
            r = {'name' : self.decode_room_name(room['room'])}
            ret.append(r)
            for att in room['attributes']:
                att.tojson(r)
            
        return ret    
        
    def print_room_descriptions(self,out):
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
        out.append(U.indent_code(s,0))
        pos += len(pre)
        
        for room in self._room_descriptions:
            adata = b''
            for att in room['attributes']:
                d = att.get_assembly()
                adata = adata  + d                        
            out.append(';')
            out.append('; '+self.decode_room_name(room['room']))
            pre = bytes([room['room']]) + RTC.BaseCommand.make_length_bytes(len(adata)+1)
            s = U.hex4(pos)+': '+U.dump_bytes(pre)+' '+U.hex2(room['data'])+' ; roomNumber='+U.hex2(room['room'])+'('+self.decode_room_name(room['room'])+')'+' size='+U.hex4(len(adata)+1)+' data='+U.hex2(room['data'])
            out.append(U.indent_code(s,0))
            pos += len(pre)+1
            for att in room['attributes']:
                pos = att.print_assembly(pos,1,out)                      
    
    def tojson_objects(self):
        ret = []
        
        num = 1
        for obj in self._objects:
            r = {'name' : self.decode_noun(num),'location' : self.decode_room_name(obj['location']), 'score':obj['score'], 'bits':FUN.decode_object_bits(obj['bits'],False)}
            num += 1
            
            ret.append(r)
            
            for att in obj['attributes']:
                att.tojson(r)
            
        return ret
                
    def print_object_data(self,out):
        
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
        out.append(U.indent_code(s,0))
        pos += len(pre)
        
        num = 1
        data = b''
        for obj in self._objects:
            out.append(';')
            out.append('; Object_'+U.hex2(num)+' "'+self.decode_noun(num)+'"')
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
            out.append(U.indent_code(s,0))                  
            pos += len(pre)
            s = U.hex4(pos)+': '+U.hex2(aa)+' '+U.hex2(bb)+' '+U.hex2(cc)+' ; room='+U.hex2(aa)+' scorePoints='+U.hex2(bb)+' bits='+U.hex2(cc)
            out.append(U.indent_code(s,0))
            pos += 3
            
            for att in obj['attributes']:
                pos = att.print_assembly(pos,1,out)
                
        return pos 
    
    def fix_command_names(self):
        fn = self._codefile
        with open(fn) as f:
            code = f.readlines()
        org_data = binary.get_binary_lines(code,self._origin)
        coco = False
        if 'CoCo' in fn:
            coco = True
        bedlam = False
        if 'Bedlam' in fn:
            bedlam = True
        
        table = RTC.COMMAND_INFO    
        mx = len(table)
        
        if bedlam:
            mx = 0x2D+1 # Bedlam for TRS80 and CoCo
        else:        
            if coco:
                mx = 0x26+1 # RaakaTu for Coco
            else:
                mx = 0x28+1 # RaakaTu for TRS80
        
        for ent in table:
            #print(ent)
            ofs = ent[1]*2+self._command_table-self._origin
            a = org_data[ofs]
            b = org_data[ofs+1]
            if coco:
                p = a*256+b
            else:
                p = b*256+a
            if len(ent)==4:
                ent.append(p)
            else:
                ent[4] = p
            #print(FORM.shex4(p))
            
        # First, fix the names in the table itself
                
        org = FORM.shex4(self._command_table)+':'
        for pos in range(len(code)):
            if code[pos].startswith(org):                
                break
        for x in range(mx):
            g = code[pos][0:13]+'; '+FORM.shex2(table[x][1])+' '+table[x][3]
            code[pos] = g+'\n'
            pos+=1            
            
        # Track down the command code and make sure it is labeled correctly
        for x in range(mx):
            ent = table[x]
            org = FORM.shex4(ent[-1])+':'
            for pos in range(len(code)):
                if code[pos].startswith(org):
                    break
            while not code[pos].startswith('Com_'):
                pos-=1
            
            g = ent[-2]
            i = g.find('(')
            if i<0:
                i = g.find(':')
            g = g[0:i]
            
            g = 'Com_'+FORM.shex2(ent[1])+'_'+g+':'
            code[pos] = g+'\n'
            code[pos+1] = '; '+ent[-2]+'\n'    
            
        with open(fn,'w') as f:
            f.writelines(code)
       
    def merge_into(self,newlines):
        nc = -1
        for g in newlines:
            nc+=1
            if not g.startswith(';'):    
                origin = int(g[0:4],16)
                break
            
        endpos = 0
        while True:
            endpos -= 1
            g = newlines[endpos]
            if not g.startswith(';'):
                endpos = int(g[0:4],16)
                break
            
        orgstr = FORM.shex4(origin)+':'
        endstr = FORM.shex4(endpos)+':'
            
        new_data = binary.get_binary_lines(newlines,origin)
        with open(self._codefile) as f:
            code = f.readlines()
            
        pos = -1
        while True:
            pos += 1
            if code[pos].startswith(orgstr):
                break
            
        epos = pos    
        while True:
            epos += 1
            if code[epos].startswith(endstr):
                break
            
        while nc:
            pos-=1
            nc-=1
            if not code[pos].startswith(';'):
                raise Exception('Expected leading comments')        
            
        org_data = binary.get_binary_lines(code[pos:epos+1],origin)
        if org_data!=new_data:
            raise Exception('The binary of the new lines does not match the binary of the old')
        
        with open(self._codefile,'w') as f:
            for i in range(pos):
                f.write(code[i])
            for g in newlines:
                f.write(g+'\n')
            for i in range(epos+1,len(code)):
                f.write(code[i])