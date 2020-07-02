from digs.raakatu import unpacker
import util.util as U

DECODE_PHRASE = None
DECODE_NOUN = None
DECODE_HELPER = None
DECODE_ROOM = None
DECODE_BITS = None

def set_decode_phrase(fn):
    global DECODE_PHRASE
    DECODE_PHRASE = fn
    
def set_decode_noun(fn):
    global DECODE_NOUN
    DECODE_NOUN = fn
    
def set_decode_helper(fn):
    global DECODE_HELPER
    DECODE_HELPER = fn
    
def set_decode_room(fn):
    global DECODE_ROOM
    DECODE_ROOM = fn
    
def set_decode_bits(fn):
    global DECODE_BITS
    DECODE_BITS = fn

class CommonCommand:
    
    command_length = 0
    
    def __init__(self,number):
        self._number = number        
    
    def parse_binary(self,data):        
        self._raw_data = data
        
    def get_assembly(self):
        return bytes([self._number])
    
    def print_assembly(self,pos,ident):        
        s = U.hex4(pos)+': '+U.hex2(self._number)+' ; '+U.hex2(self._number)+'('+DECODE_HELPER(self._number)+')'
        print(U.indent_code(s,ident))         
        return pos+1
    
    def tojson(self):
        return ['function('+DECODE_HELPER(self._number)+')']
    
class BaseCommand:
    
    def get_assembly(self):        
        ret = bytes([self.command_value])
        x = self.command_length
        if x is None:
            ret = ret + BaseCommand.make_length_bytes(len(self._raw_data))    
        ret = ret + self._raw_data
        print('get_assembly',self.command_name, U.hexlist(ret))
        raise Exception('Should not be here')
        return ret
    
    @staticmethod
    def make_length_bytes(val):
        if val<0x80:
            return bytes([val])
        else:
            return bytes([int(val/256)|0x80,val&0xFF])
        
    def fill_json_params(self,*params):
        ret = self.command_name
        i = ret.find('(')
        pms = ret[i+1:-1].split(',')
        ret = ret[0:i+1]
        for i in range(len(params)):
            ret=ret+pms[i]+'='+params[i]+', '
        return ret[0:-2]+')'

class MoveActiveObjectToRoom(BaseCommand):
    command_value = 0x19
    command_name = 'move_ACTIVE(room)'
    command_length = 1
    
    def parse_binary(self,data):              
        self._raw_data = data      
        self._room = data[0]
        
    def get_assembly(self):
        return bytes([self.command_value,self._room])   
    
    def print_assembly(self,pos,ident):        
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' '+U.hex2(self._room)+' ; '+self.command_name+' room='+U.hex2(self._room)+'('+DECODE_ROOM(self._room) +')'
        print(U.indent_code(s,ident))       
        return pos+2
    
    def tojson(self):
        return [self.command_name,DECODE_ROOM(self._room)]
    
class PrintInventory(BaseCommand):
    
    command_value = 0x06
    command_name = 'print_inventory()'
    command_length = 0
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data 
        
    def get_assembly(self):
        return bytes([self.command_value])   
    
    def print_assembly(self,pos,ident):  
        s =  U.hex4(pos)+': '+U.hex2(self.command_value)+' ; '+self.command_name     
        print(U.indent_code(s,ident))        
        return pos+1
    
    def tojson(self):
        return [self.command_name]

class UnknownCommand2(BaseCommand):
    
    command_value = 0x02
    command_name = 'unknown_02(x)'
    command_length = 1
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data           
        self._unknown = data[0]
        
    def print_assembly(self,pos,ident):  
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' '+U.hex2(self._unknown)+' ; '+self.command_name+' unknown='+U.hex2(self._unknown)      
        print(U.indent_code(s,ident))        
        return pos+2
    
    def tojson(self):
        return [self.command_name,self._unknown]
       
class UnknownCommand22(BaseCommand):
    
    command_value = 0x22
    command_name = 'unknown_22(x)'
    command_length = 1
    
    @classmethod
    def get_switch_comment(cs,cdata):
        return cs.command_name+' unknown='+U.hex2(cdata[0])
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data     
        self._unknown = data[0]
        
    def print_assembly(self,pos,ident):        
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' '+U.hex2(self._unknown)+' ; '+self.command_name+' unknown='+U.hex2(self._unknown)
        print(U.indent_code(s,ident))        
        return pos+2
    
    @classmethod
    def tojson_switch(cls,cdata):
        return [cls.command_name,cdata[0]]
    
    def tojson(self):
        return [self.command_name,self._unknown]
    
class UnknownCommand28(BaseCommand):
    
    command_value = 0x28
    command_name = 'unknown_28(x)'
    command_length = 0
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data       
        
    def get_assembly(self):
        return bytes([self.command_value])    
    
    def print_assembly(self,pos,ident):   
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' ; '+self.command_name      
        print(U.indent_code(s,ident))        
        return pos+1
    
    def tojson(self):
        return [self.command_name]
        
class UnknownCommand27(BaseCommand):
    
    command_value = 0x27
    command_name = 'unknown_27(x)'
    command_length = 0
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data  
        
    def get_assembly(self):
        return bytes([self.command_value])   
    
    def print_assembly(self,pos,ident):        
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' ; '+self.command_name
        print(U.indent_code(s,ident))        
        return pos+1
    
    def tojson(self):
        return [self.command_name]
 
class EndlessLoop(BaseCommand):
    
    command_value = 0x24
    command_name = 'endless_loop()'
    command_length = 0
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data  
    
    def get_assembly(self):
        return bytes([self.command_value])   
    
    def print_assembly(self,pos,ident):       
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' ; '+self.command_name 
        print(U.indent_code(s,ident))        
        return pos+1
    
    def tojson(self):
        return [self.command_name]
       
class PrintScore(BaseCommand):
    
    command_value = 0x26
    command_name = 'print_score()'
    command_length = 0
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data        
        
    def get_assembly(self):
        return bytes([self.command_value])   
    
    def print_assembly(self,pos,ident):        
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' ; '+self.command_name
        print(U.indent_code(s,ident))        
        return pos+1
    
    def tojson(self):
        return [self.command_name]
    
class PrintRoomDescription(BaseCommand):
    
    command_value = 0x07
    command_name = 'print_room_description()'
    command_length = 0
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data     
        
    def get_assembly(self):
        return bytes([self.command_value])   
    
    def print_assembly(self,pos,ident):    
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' ; '+self.command_name    
        print(U.indent_code(s,ident))        
        return pos+1
    
    def tojson(self):
        return [self.command_name]
    
class SetVarObjectToSecondNoun(BaseCommand):
    
    command_value = 0x1B
    command_name = 'set_VAR_to_second_noun()'
    command_length = 0
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data      
        
    def get_assembly(self):
        return bytes([self.command_value])   
    
    def print_assembly(self,pos,ident):        
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' ; '+self.command_name
        print(U.indent_code(s,ident))        
        return pos+1
    
    def tojson(self):
        return [self.command_name]

class DropObject(BaseCommand):
    
    command_value = 0x10
    command_name = 'drop_VAR()'
    command_length = 0
    
    def print_assembly(self,pos,ident):   
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' ; '+self.command_name    
        print(U.indent_code(s,ident))        
        return pos+1
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data      
        
    def get_assembly(self):
        return bytes([self.command_value])   
    
    def tojson(self):
        return [self.command_name]
    
class SetVarObjectToFirstNoun(BaseCommand):
    
    command_value = 0x1A
    command_name = 'set_VAR_to_first_noun()'
    command_length = 0
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data   
    
    def get_assembly(self):
        return bytes([self.command_value])     
    
    def print_assembly(self,pos,ident):        
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' ; '+self.command_name
        print(U.indent_code(s,ident))        
        return pos+1
    
    def tojson(self):
        return [self.command_name]
        
class AttackObject(BaseCommand):
    
    command_value = 0x1D
    command_name = 'attack_VAR(points)'
    command_length = 1
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data
        self._points = data[0]      
        
    def get_assembly(self):
        return bytes([self.command_value,self._points])   
    
    def print_assembly(self,pos,ident):       
        s =  U.hex4(pos)+': '+U.hex2(self.command_value)+' '+U.hex2(self._points)+' ; '+self.command_name+' points='+U.hex2(self._points)
        print(U.indent_code(s,ident))        
        return pos+2
    
    def tojson(self):
        return [self.command_name,self._points]
        
class CompareObjectToSecondNoun(BaseCommand):
    
    command_value = 0x09
    command_name = 'compare_to_second_noun(object)'
    command_length = 1
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data
        self._object = data[0]    
        
    def get_assembly(self):
        return bytes([self.command_value,self._object])   
    
    @classmethod
    def get_switch_comment(cs,cdata):
        return cs.command_name+' object='+U.hex2(cdata[0])+'('+DECODE_NOUN(cdata[0])+')'
    
    def print_assembly(self,pos,ident):        
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' '+U.hex2(self._object)+' ; '+self.command_name+' object='+U.hex2(self._object)+'('+DECODE_NOUN(self._object)+')'
        print(U.indent_code(s,ident))        
        return pos+2
    
    @classmethod
    def tojson_switch(cls,cdata):
        return [cls.command_name,DECODE_NOUN(cdata[0])]
    
    def tojson(self):
        return [self.command_name,DECODE_NOUN(self._object)]
        
class MoveActiveObjectToRoomAndLook(BaseCommand):
    
    command_value = 0x00
    command_name = 'move_ACTIVE_and_look(room)'
    command_length = 1
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data
        self._room = data[0]      
        
    def get_assembly(self):
        return bytes([self.command_value,self._room])
    
    def print_assembly(self,pos,ident):      
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' '+U.hex2(self._room)+' ; '+self.command_name+' room='+U.hex2(self._room)+'('+DECODE_ROOM(self._room)+')'
        print(U.indent_code(s,ident))        
        return pos+2
    
    def tojson(self):
        return [self.command_name,DECODE_ROOM(self._room)]        
        #return [self.command_name,DECODE_ROOM(self._room)]
    
class PrintSecondNounShortName(BaseCommand):
    
    command_value = 0x12
    command_name = 'print_second_noun'
    command_length = 0
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data      
        
    def get_assembly(self):
        return bytes([self.command_value])   
    
    def print_assembly(self,pos,ident):        
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' ; '+self.command_name
        print(U.indent_code(s,ident))        
        return pos+1
    
    def tojson(self):
        return [self.command_name]
    
class PrintVarShortName(BaseCommand):
    
    command_value = 0x16
    command_name = 'print_VAR'
    command_length = 0
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data     
        
    def get_assembly(self):
        return bytes([self.command_value])   
    
    def print_assembly(self,pos,ident):        
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' ; '+self.command_name
        print(U.indent_code(s,ident))        
        return pos+1
    
    def tojson(self):
        return [self.command_name]
    
class CheckObjectBits(BaseCommand):
    
    command_value = 0x15
    command_name = 'check_VAR(bits)'
    command_length = 1
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data       
        self._bits = data[0]        
        
    def get_assembly(self):
        return bytes([self.command_value,self._bits])   
    
    def print_assembly(self,pos,ident):     
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' '+U.hex2(self._bits)+' ; '+self.command_name+' bits='+U.hex2(self._bits)+'('+DECODE_BITS(self._bits)+')'
        print(U.indent_code(s,ident))        
        return pos+2
    
    def tojson(self):
        return [self.command_name,DECODE_BITS(self._bits)]
    
class ExecutePhrase(BaseCommand):
    
    command_value = 0x21
    command_name = 'execute_phrase(phrase,first_noun,second_noun)'
    command_length = 3
        
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data       
        self._phrase = data[0]
        self._first_noun = data[1]
        self._second_noun = data[2] 
        
    def get_assembly(self):
        return bytes([self.command_value,self._phrase,self._first_noun,self._second_noun])
    
    def print_assembly(self,pos,ident):     
        
        fn = '00'
        if self._first_noun:
            fn = U.hex2(self._first_noun)+'('+DECODE_NOUN(self._first_noun)+')'
        sn = '00'
        if self._second_noun:
            sn = U.hex2(self._second_noun)+'('+DECODE_NOUN(self._second_noun)+')'
        
        s = (U.hex4(pos)+': '+U.hex2(self.command_value)+' '+U.hex2(self._phrase)+' '+U.hex2(self._first_noun)+' '+U.hex2(self._second_noun)+
             ' ; '+self.command_name+' phrase='+DECODE_PHRASE(self._phrase)+' firstNoun='+fn+' secondNoun='+sn)
        print(U.indent_code(s,ident))        
        return pos+4
    
    def tojson(self):
        return [self.command_name,DECODE_PHRASE(self._phrase),DECODE_NOUN(self._first_noun),DECODE_NOUN(self._second_noun)]

class RestartGame(BaseCommand):
    
    command_value = 0x25
    command_name = 'restart_game()'
    command_length = 0
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data       
        
    def get_assembly(self):
        return bytes([self.command_value])   
    
    def print_assembly(self,pos,ident):        
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' ; '+self.command_name
        print(U.indent_code(s,ident))        
        return pos+1
    
    def tojson(self):
        return [self.command_name]

class CheckActiveObject(BaseCommand):
    
    command_value = 0x20
    command_name = 'is_ACTIVE_this(object)'
    command_length = 1
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data
        self._object = data[0]  
        
    @classmethod
    def get_switch_comment(cs,cdata):
        return cs.command_name+' object='+U.hex2(cdata[0])+'('+DECODE_NOUN(cdata[0])+')'
        
    def get_assembly(self):
        return bytes([self.command_value,self._object])    
    
    def print_assembly(self,pos,ident):    
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' '+U.hex2(self._object)+' ; '+self.command_name+' object='+U.hex2(self._object)+'('+DECODE_NOUN(self._object)+')'    
        print(U.indent_code(s,ident))        
        return pos+2
    
    @classmethod
    def tojson_switch(cls,cdata):
        return [cls.command_name,DECODE_NOUN(cdata[0])]
    
    def tojson(self):
        return [self.command_name,DECODE_NOUN(self._object)]
    
class ProcessPhraseByRoomFirstSecond(BaseCommand):
    
    command_value = 0x13
    command_name = 'process_phrase_by_room_first_second()'
    command_length = 0
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data      
        
    def get_assembly(self):
        return bytes([self.command_value])
    
    def print_assembly(self,pos,ident):    
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' ; '+self.command_name    
        print(U.indent_code(s,ident))        
        return pos+1
    
    def tojson(self):
        return [self.command_name]
        
class IsObjectAtLocation(BaseCommand):
    
    command_value = 0x03
    command_name = 'is_located(room,object)'
    command_length = 2
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data           
        self._room = data[0]
        self._object = data[1]
        
    def get_assembly(self):
        return bytes([self.command_value,self._room,self._object])  
    
    @classmethod
    def get_switch_comment(cs,cdata):
        return cs.command_name+' room='+U.hex2(cdata[0])+'('+DECODE_ROOM(cdata[0])+')'+' object='+U.hex2(cdata[1])+'('+DECODE_NOUN(cdata[1])+')'
    
    def print_assembly(self,pos,ident):  
        s = (U.hex4(pos)+': '+U.hex2(self.command_value)+' '+U.hex2(self._room)+' '+U.hex2(self._object)+
              ' ; '+self.command_name+' room='+U.hex2(self._room)+'('+DECODE_ROOM(self._room)+')'+' object='+U.hex2(self._object)+'('+DECODE_NOUN(self._object)+')')      
        print(U.indent_code(s,ident))        
        return pos+3
    
    def tojson(self):
        return [self.command_name,DECODE_ROOM(self._room),DECODE_NOUN(self._object)]
    
    @classmethod
    def tojson_switch(cls,cdata):
        return [cls.command_name,DECODE_ROOM(cdata[0]),DECODE_NOUN(cdata[1])]
    
class Fail(BaseCommand):
    
    command_value = 0x0C
    command_name = 'fail()'
    command_length = 0
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data  
        
    def get_assembly(self):
        return bytes([self.command_value])   
    
    def print_assembly(self,pos,ident):      
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' ; '+self.command_name  
        print(U.indent_code(s,ident))        
        return pos+1
    
    def tojson(self):
        return [self.command_name]
    
class IsVarOwnedBy(BaseCommand):
    
    command_value = 0x18
    command_name = 'is_VAR_owned_by_ACTIVE()'
    command_length = 0
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data
    
    def get_assembly(self):
        return bytes([self.command_value])   
    
    def print_assembly(self,pos,ident):      
        s =  U.hex4(pos)+': '+U.hex2(self.command_value)+' ; '+self.command_name 
        print(U.indent_code(s,ident))        
        return pos+1
    
    def tojson(self):
        return [self.command_name]
        
class PrintFirstNounShortName(BaseCommand):
    
    command_value = 0x11
    command_name = 'print_first_noun()'
    command_length = 0
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data           
        
    def get_assembly(self):
        return bytes([self.command_value])   
    
    def print_assembly(self,pos,ident):        
        s =U.hex4(pos)+': '+U.hex2(self.command_value)+' ; '+self.command_name 
        print(U.indent_code(s,ident))        
        return pos+1
    
    def tojson(self):
        return [self.command_name]

class CompareObjectToFirstNoun(BaseCommand):
    
    command_value = 0x08
    command_name = 'is_first_noun(object)'
    command_length = 1
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data
        self._object = data[0]    
        
    def get_assembly(self):
        return bytes([self.command_value,self._object])    
    
    def print_assembly(self,pos,ident):      
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' '+U.hex2(self._object)+' ; '+self.command_name+' object='+U.hex2(self._object)+'('+DECODE_NOUN(self._object)+')'
        print(U.indent_code(s,ident))        
        return pos+2
    
    def tojson(self):
        return [self.command_name,DECODE_NOUN(self._object)]
    
class IsObjectInRoomOrPack(BaseCommand):
    
    command_value = 0x01
    command_name = 'is_in_pack_or_current_room(object)'
    command_length = 1
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data
        self._object = data[0]
        
    @classmethod
    def get_switch_comment(cs,cdata):
        return cs.command_name+' object='+U.hex2(cdata[0]) +'('+DECODE_NOUN(cdata[0])+')'
        
    def get_assembly(self):
        return bytes([self.command_value,self._object])  
    
    def print_assembly(self,pos,ident):     
        s =U.hex4(pos)+': '+U.hex2(self.command_value)+' '+U.hex2(self._object)+' ; '+self.command_name+' object='+U.hex2(self._object)+'('+DECODE_NOUN(self._object)+')'    
        print(U.indent_code(s,ident))        
        return pos+2
    
    def tojson(self):
        return [self.command_name,DECODE_NOUN(self._object)]
    
    @classmethod
    def tojson_switch(cls,cdata):
        return [cls.command_name,DECODE_NOUN(cdata[0])]
    
class PrintMessage2(BaseCommand):
    
    command_value = 0x1F
    command_name = 'print2(msg)'
    command_length = None
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data
        self._text = unpacker.decode_message(data)   
        
    def get_assembly(self):
        return bytes([self.command_value])+BaseCommand.make_length_bytes(len(self._raw_data))+self._raw_data
    
    def print_assembly(self,pos,ident):        
        pre = bytes([self.command_value])+BaseCommand.make_length_bytes(len(self._raw_data))
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; '+self.command_name+' size='+U.hex4(len(self._raw_data))
        print(U.indent_code(s,ident))
        pos+=len(pre)
        pos = PrintMessage.print_assembly_text(pos,ident+1,self._raw_data,self._text)             
        return pos
    
    def tojson(self):
        return [self.command_name,self._text]
    
class SwapObjects(BaseCommand):
    
    command_value = 0x1E
    command_name = 'swap(object_a,object_b)'
    command_length = 2
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data
        self._object_a = data[0]
        self._object_b = data[1]
        
    def get_assembly(self):
        return bytes([self.command_value,self._object_a,self._object_b])
    
    def print_assembly(self,pos,ident):        
        s = (U.hex4(pos)+': '+U.hex2(self.command_value)+' '+U.hex2(self._object_a)+' '+U.hex2(self._object_b)+
              ' ; '+self.command_name+' object_a='+'('+DECODE_NOUN(self._object_a)+')'+ U.hex2(self._object_a)+' object_b='+U.hex2(self._object_b)+'('+DECODE_NOUN(self._object_b)+')')
        print(U.indent_code(s,ident))        
        return pos+3
    
    def tojson(self):
        return [self.command_name,self._object_a,self._object_b]
    
class PickUpObject(BaseCommand):
    
    command_value = 0x0F
    command_name = 'pick_up_VAR()'
    command_length = 0
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data
        
    def get_assembly(self):
        return bytes([self.command_value])   
    
    def print_assembly(self,pos,ident):        
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' ; '+self.command_name
        print(U.indent_code(s,ident))        
        return pos+1
    
    def tojson(self):
        return [self.command_name]
    
class SetVarObject(BaseCommand):
    
    command_value = 0x1C
    command_name = 'set_VAR(object)'
    command_length = 1
        
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data
        self._object = data[0]    
        
    def get_assembly(self):
        return bytes([self.command_value,self._object])
    
    def print_assembly(self,pos,ident):       
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' '+U.hex2(self._object)+' ; '+self.command_name+' object='+U.hex2(self._object)+'('+DECODE_NOUN(self._object)+')'
        print(U.indent_code(s,ident))        
        return pos+2
    
    def tojson(self):
        return [self.command_name,DECODE_NOUN(self._object)]
    
class IsLessEqualRandom(BaseCommand):
    
    command_value = 0x05
    command_name = 'is_less_equal_last_random(value)'
    command_length = 1
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data
        self._value = data[0]   
        
    @classmethod
    def get_switch_comment(cs,cdata):
        return cs.command_name+' value='+U.hex2(cdata[0])
    
    def get_assembly(self):
        return bytes([self.command_value,self._value])  
    
    def print_assembly(self,pos,ident):   
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' '+U.hex2(self._value)+' ; '+self.command_name+' number='+U.hex2(self._value)     
        print(U.indent_code(s,ident))        
        return pos+2
    
    def tojson(self):
        return [self.command_name,int(self._value)]
    
    @classmethod
    def tojson_switch(cls,cdata):
        return [cls.command_name,int(cdata[0])]

class WhileFail(BaseCommand):
    
    command_value = 0x0E
    command_name = 'while_fail:'
    command_length = None # Variable length        
    
    def get_assembly(self):        
        data = b''
        for com in self._script:
            data = data + com.get_assembly()
            
        data = bytes([self.command_value])+BaseCommand.make_length_bytes(len(data))+data
        
        #print('get_assembly', self.command_name,U.hex4(len(data)),U.hexlist(data))
            
        return data       
    
    def print_assembly(self,pos,ident):
        data = b''
        for com in self._script:
            data = data + com.get_assembly() 
        pre = bytes([self.command_value])+BaseCommand.make_length_bytes(len(data))
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; '+self.command_name+' size='+U.hex4(len(data)) 
        print(U.indent_code(s,ident))
        pos+=len(pre)
        for com in self._script:
            pos = com.print_assembly(pos,ident+1)
        return pos
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data
        self._script = decode_script(data)  
        
    def tojson(self):
        scr = []
        for com in self._script:
            scr.append(com.tojson())
        return [self.command_name,scr]

class ExecuteReverseStatus(BaseCommand):
    
    command_value = 0x14
    command_name = 'execute_and_reverse_status:'
    command_length = 0
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data
        #self._script = decode_script(data)   
    
    def get_assembly(self):
        return bytes([self.command_value])    
    
    def print_assembly(self,pos,ident):      
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' ; '+self.command_name  
        print(U.indent_code(s,ident))        
        return pos+1
    
    def tojson(self):
        return [self.command_name]
    
class MoveObject(BaseCommand):
    
    command_value = 0x17
    command_name = 'move_to(object,room)'
    command_length = 2
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data
        self._object = data[0]
        self._room = data[1]     
        
    def get_assembly(self):
        return bytes([self.command_value,self._object,self._room])
    
    def print_assembly(self,pos,ident):    
        s =  (U.hex4(pos)+': '+U.hex2(self.command_value)+' '+U.hex2(self._object)+' '+U.hex2(self._room)+
              ' ; '+self.command_name+' object='+U.hex2(self._object)+'('+DECODE_NOUN(self._object)+') room='+U.hex2(self._room)+'('+DECODE_ROOM(self._room)+')')   
        print(U.indent_code(s,ident))        
        return pos+3
    
    def tojson(self):
        return [self.command_name,DECODE_ROOM(self._room)]
    
class Heal(BaseCommand):
    
    command_value = 0x23
    command_name = 'heal_VAR(points)'
    command_length = 1
    
    def parse_binary(self,data):    
        #print(self.command_name)    
        self._raw_data = data
        self._points = data[0]     
        
    def get_assembly(self):
        return bytes([self.command_value,self._points])
    
    def print_assembly(self,pos,ident):    
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' '+U.hex2(self._points)+' ; '+self.command_name+' value='+U.hex2(self._points)    
        print(U.indent_code(s,ident))        
        return pos+2
    
    def tojson(self):
        return [self.command_name,self._points]
    
class WhilePass(BaseCommand):
    
    command_value = 0x0D
    command_name = 'while_pass:'    
    command_length = None # Variable length
    
    def parse_binary(self,data):      
        #print(self.command_name)  
        self._raw_data = data
        self._script = decode_script(data)  
        
    def get_assembly(self):
        data = b''
        for com in self._script:
            data = data + com.get_assembly()            
        data = bytes([self.command_value])+BaseCommand.make_length_bytes(len(data))+data
        #print('get_assembly', self.command_name,U.hexlist(data))    
        return data
    
    def print_assembly(self,pos,ident):
        data = b''
        for com in self._script:
            data = data + com.get_assembly() 
        pre = bytes([self.command_value])+BaseCommand.make_length_bytes(len(data))
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; '+self.command_name+' size='+U.hex4(len(data))
        print(U.indent_code(s,ident))
        pos+=len(pre)
        for com in self._script:
            pos = com.print_assembly(pos,ident+1)
        return pos
    
    def tojson(self):
        scr = []
        for com in self._script:
            scr.append(com.tojson())
        return [self.command_name,scr]
            
class PrintMessage(BaseCommand):
    
    command_value = 0x04
    command_name = 'print(msg)'
    command_length = None # Variable length
    
    @staticmethod
    def print_assembly_text(pos,ident,raw,text):
        # Only 16 bytes of data.
        # Only 40 characters of text.
        data = []
        while raw:
            g = len(raw)
            if g>16:
                g = 16
            data.append(raw[0:g])
            raw = raw[g:]   
            
        chars = []
        while text:
            g = len(text)
            if g>40:
                g = 40
            chars.append(text[0:40])
            text = text[g:]                    
            
        if len(chars)>len(data):
            raise Exception('Trouble')
        while len(chars)<len(data):
            chars.append('~')
            
        for i in range(len(data)):
            s = U.hex4(pos)+': '+U.dump_bytes(data[i])+' ; '+chars[i]
            print(U.indent_code(s,ident))
            pos += len(data[i])
            
        return pos            
    
    def parse_binary(self,data):
        self._text = unpacker.decode_message(data)
        self._raw_data = data
        #print(self.command_name,self._text)    
        
    def get_assembly(self):
        return bytes([self.command_value])+BaseCommand.make_length_bytes(len(self._raw_data))+self._raw_data
    
    def print_assembly(self,pos,ident):        
        pre = bytes([self.command_value])+BaseCommand.make_length_bytes(len(self._raw_data))
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; '+self.command_name+' size='+U.hex4(len(self._raw_data))
        print(U.indent_code(s,ident))
        pos+=len(pre)
        pos = PrintMessage.print_assembly_text(pos,ident+1,self._raw_data,self._text)             
        return pos
    
    def tojson(self):
        return [self.command_name,self._text]
    
class CompareToPhrase(BaseCommand):
    
    command_value = 0x0A
    command_name = 'compare_input_to(phrase)'
    command_length = 1
    
    def parse_binary(self,data):        
        #print(self.command_name)
        self._raw_data = data
        self._phrase = data[0]        
        
    def get_assembly(self):
        return bytes([self.command_value,self._phrase])

    @classmethod
    def get_switch_comment(cs,cdata):
        return cs.command_name+' phrase='+DECODE_PHRASE(int(cdata[0]))
    
    def print_assembly(self,pos,ident):
        
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' '+U.hex2(self._phrase)+' ; '+self.command_name+' phrase='+DECODE_PHRASE(self._phrase)
        print(U.indent_code(s,ident)) 
        # TODO decode the phrase
                
        return pos+2
    
    def tojson(self):
        return [self.command_name,DECODE_PHRASE(self._phrase,full=False)]
    
    @classmethod
    def tojson_switch(cs,cdata):
        return [cs.command_name,DECODE_PHRASE(cdata[0],full=False)]
    
class Switch(BaseCommand):
    
    command_value = 0x0B
    command_name = 'switch'    
    command_length = None # Variable length
    
    def parse_binary(self,data):        
        self._raw_data = data
        pos = 0
        #print(self.command_name)
        self._command = data[pos]
        pos += 1
        self._command_data_length = SCRIPT_COMMANDS[self._command].command_length
        if self._command_data_length is None:
            raise Exception('Not prepared for a variable-length switch command')
        
        #if self._command_data_length != 1:
        #    is_located(room,object)
        #    raise Exception('Really?'+SCRIPT_COMMANDS[self._command].command_name)
        
        self._cases = []
        while pos<len(data):
            ds = []
            for _ in range(self._command_data_length):
                ds.append(data[pos])
                pos+=1
            slen,pos = read_length(pos,data)
            cdat = data[pos:pos+slen]
            scr = decode_script(cdat)
            self._cases.append((ds,scr))
            pos += slen
            
    def tojson(self):
        cases = []
        ret = ['switch',cases]
        scm = SCRIPT_COMMANDS[self._command]
        
        for case in self._cases:            
            cd = bytes(case[0])
            test = scm.tojson_switch(cd)
            test.append(case[1][0].tojson())
            cases.append(test)
        
        return ret
    
    def print_assembly(self,pos,ident):
        
        data = bytes([self._command])
        
        for c in self._cases:
            if len(c[1])!=1:
                raise Exception('OOPS ... work on me')
            asm = c[1][0].get_assembly()            
            data = data + bytes(c[0]) + BaseCommand.make_length_bytes(len(asm))+asm
            
        scm = SCRIPT_COMMANDS[self._command]
        pre = bytes([self.command_value])+BaseCommand.make_length_bytes(len(data))+bytes([self._command])
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; '+self.command_name+'('+scm.command_name+'): size='+U.hex4(len(data))
        print(U.indent_code(s,ident))
        pos+=len(pre)
        
        #s = U.hex4(pos)+': '+U.hex2(self._command)+' ; '+scm.command_name
        #print(U.indent_code(s,ident))
        #pos+=1
        
        for case in self._cases:            
            cd = bytes(case[0])
            #cn = SCRIPT_COMMANDS[self.command_value].command_name
            s = U.hex4(pos)+': '+U.dump_bytes(cd)+' ; '+scm.get_switch_comment(cd)
            print(U.indent_code(s,ident+1))
            pos += len(cd)
            asm = case[1][0].get_assembly()         
            sz = BaseCommand.make_length_bytes(len(asm))
            s = U.hex4(pos)+': '+U.dump_bytes(sz)+' ; IF_NOT_GOTO address='+U.hex4(len(asm)+pos+1)
            print(U.indent_code(s,ident+1))
            pos += len(sz)
            pos = case[1][0].print_assembly(pos,ident+2)
                
        return pos
            
    def get_assembly(self):
        
        cdata = bytes([self._command])
        
        for c in self._cases:
            if len(c[1])!=1:
                raise Exception('OOPS ... work on me')
            asm = c[1][0].get_assembly()            
            cdata = cdata + bytes(c[0]) + BaseCommand.make_length_bytes(len(asm))+asm
        cdata = bytes([self.command_value])+BaseCommand.make_length_bytes(len(cdata))+cdata
                        
        return cdata

COMMAND_INFO = [
    IsObjectInRoomOrPack,            0x01, '1', 'is_in_pack_or_current_room(object)',
    UnknownCommand2,                 0x02, '1', 'unknown_02(x)',
    IsObjectAtLocation,              0x03, '2', 'is_located(room,object)',
    PrintMessage,                    0x04, 'v', 'print(msg)',
    IsLessEqualRandom,               0x05, '1', 'is_less_equal_last_random(value)',
    PrintInventory,                  0x06, '0', 'print_inventory()',
    PrintRoomDescription,            0x07, '0', 'print_room_description()',
    CompareObjectToFirstNoun,        0x08, '1', 'is_first_noun(object)',
    CompareObjectToSecondNoun,       0x09, '1', 'compare_to_second_noun(object)',
    CompareToPhrase,                 0x0A, '1', 'compare_input_to(phrase)',
    Switch,                          0x0B, 'v', 'switch:',
    Fail,                            0x0C, '0', 'fail()',
    WhilePass,                       0x0D, 'v', 'while_pass:',
    WhileFail,                       0x0E, 'v', 'while_fail:',
    PickUpObject,                    0x0F, '0', 'pick_up_VAR()',
    DropObject,                      0x10, '0', 'drop_VAR()',
    PrintFirstNounShortName,         0x11, '0', 'print_first_noun()',
    PrintSecondNounShortName,        0x12, '0', 'print_second_noun()',
    ProcessPhraseByRoomFirstSecond,  0x13, '0', 'process_phrase_by_room_first_second()',
    ExecuteReverseStatus,            0x14, '0', 'execute_and_reverse_status:',
    CheckObjectBits,                 0x15, '1', 'check_VAR(bits)',
    PrintVarShortName,               0x16, '0', 'print_VAR()',
    MoveObject,                      0x17, '2', 'move_to(object,room)',
    IsVarOwnedBy,                    0x18, '0', 'is_VAR_owned_by_ACTIVE()',
    MoveActiveObjectToRoom,          0x19, '1', 'move_ACTIVE(room)',
    SetVarObjectToFirstNoun,         0x1A, '0', 'set_VAR_to_first_noun()',
    SetVarObjectToSecondNoun,        0x1B, '0', 'set_VAR_to_second_noun()',
    SetVarObject,                    0x1C, '1', 'set_VAR(object)',
    AttackObject,                    0x1D, '1', 'attack_VAR(points)',
    SwapObjects,                     0x1E, '2', 'swap(object_a,object_b)',
    PrintMessage2,                   0x1F, 'v', 'print2(msg)',
    CheckActiveObject,               0x20, '1', 'is_ACTIVE_this(object)',
    ExecutePhrase,                   0x21, '3', 'execute_phrase(phrase,first_noun,second_noun)',
    UnknownCommand22,                0x22, '1', 'unknown_22(x)',
    Heal,                            0x23, '1', 'heal_VAR(points)',
    EndlessLoop,                     0x24, '0', 'endless_loop()',
    RestartGame,                     0x25, '0', 'restart_game()',
    PrintScore,                      0x26, '0', 'print_score()',
    UnknownCommand27,                0x27, '1', 'unknown_27(x)',
    UnknownCommand28,                0x28, '1', 'unknown_28(x)',    
]

        
SCRIPT_COMMANDS = {
MoveActiveObjectToRoomAndLook.command_value : MoveActiveObjectToRoomAndLook, # (00) : 1 move_ACTIVE_and_look(room)
    IsObjectInRoomOrPack.command_value : IsObjectInRoomOrPack, # (01) : 1 is_in_pack_or_current_room(object)
    UnknownCommand2.command_value : UnknownCommand2, # (02) : 1 unknown_02(x)
    IsObjectAtLocation.command_value : IsObjectAtLocation, # (03) : 2 is_located(room,object)
    PrintMessage.command_value : PrintMessage, # (04) : var print(msg)
    IsLessEqualRandom.command_value : IsLessEqualRandom, # (05) : 1 is_less_equal_last_random(value)
    PrintInventory.command_value : PrintInventory, # (06) print_inventory()
    PrintRoomDescription.command_value : PrintRoomDescription, # (07) print_room_description()
    CompareObjectToFirstNoun.command_value : CompareObjectToFirstNoun, # (08) : 1 is_first_noun(object)
    CompareObjectToSecondNoun.command_value : CompareObjectToSecondNoun, # (09) : 1 compare_to_second_noun(object)
    CompareToPhrase.command_value : CompareToPhrase, # (0A) : 1 compare_input_to(phrase)
    Switch.command_value : Switch, # (0B) : var switch:
    Fail.command_value : Fail, # (0C) fail()
    WhilePass.command_value : WhilePass, # (0D) : var while_pass:
    WhileFail.command_value : WhileFail, # (0E) : var while_fail:
    PickUpObject.command_value : PickUpObject, # (0F)  pick_up_VAR()
    DropObject.command_value : DropObject, # (10) drop_VAR()
    PrintFirstNounShortName.command_value : PrintFirstNounShortName, # (11) print_first_noun()
    PrintSecondNounShortName.command_value : PrintSecondNounShortName, # (12) print_second_noun()
    ProcessPhraseByRoomFirstSecond.command_value : ProcessPhraseByRoomFirstSecond, # (13) process_phrase_by_room_first_second()
    ExecuteReverseStatus.command_value : ExecuteReverseStatus, # (14) execute_and_reverse_status:
    CheckObjectBits.command_value : CheckObjectBits, # (15) : 1 check_VAR(bits)
    PrintVarShortName.command_value : PrintVarShortName, # (16) print_VAR()
    MoveObject.command_value : MoveObject, # (17) : 2 move_to(object,room)
    IsVarOwnedBy.command_value : IsVarOwnedBy, # (18) is_VAR_owned_by_ACTIVE()
    MoveActiveObjectToRoom.command_value : MoveActiveObjectToRoom, # (19) move_ACTIVE(room)
    SetVarObjectToFirstNoun.command_value : SetVarObjectToFirstNoun, # (1A) set_VAR_to_first_noun()
    SetVarObjectToSecondNoun.command_value : SetVarObjectToSecondNoun, # (1B) set_VAR_to_second_noun()
    SetVarObject.command_value : SetVarObject, # (1C) : 1 set_VAR(object)
    AttackObject.command_value : AttackObject, # (1D) : 1 attack_VAR(points)
    SwapObjects.command_value : SwapObjects, # (1E) : 2 swap(object_a,object_b)
    PrintMessage2.command_value : PrintMessage2, # (1F) : var print2(msg)
    CheckActiveObject.command_value : CheckActiveObject, # (20) : 1 is_ACTIVE_this(object)
    ExecutePhrase.command_value : ExecutePhrase, # (21) : 3 execute_phrase(phrase,first_noun,second_noun)
    UnknownCommand22.command_value : UnknownCommand22, # (22) : 1 unknown_22(x)
    Heal.command_value : Heal, # (23) : 1 heal_VAR(points)
    EndlessLoop.command_value : EndlessLoop, # (24) endless_loop()
    RestartGame.command_value : RestartGame, # (25) restart_game()
    PrintScore.command_value : PrintScore, # (26) print_score()
    UnknownCommand27.command_value : UnknownCommand27, # (27) unknown_27(x)
    UnknownCommand28.command_value : UnknownCommand28, # (28) unknown_28(x)
}

def read_length(pos,data):    
    if data[pos]>=0x80:
        sz = (data[pos]&0x7F)*256 + data[pos+1]
        return sz,pos+2
    else:
        return data[pos],pos+1    
    
def decode_script(sdata):        
    pos = 0
    ret = []
    while pos<len(sdata):
        cmd = sdata[pos]
        #print('##',cmd,hex(pos))
        pos+=1
        if cmd>=0x80:
            cob = CommonCommand(cmd)
        else:
            cob = SCRIPT_COMMANDS[cmd]()
            
        csz = cob.command_length  
        if csz is None:
            csz,pos = read_length(pos,sdata)        
        cdata = sdata[pos:pos+csz]
        #print(pos,dump_bytes(cdata))
        cob.parse_binary(cdata)
        ret.append(cob)
        pos += csz           
                
    return ret    
    
if __name__ == '__main__':
    for i in range(41):    
        cmd = SCRIPT_COMMANDS[i]
        if cmd.command_length is None:
            cb = ': var'
        elif cmd.command_length==0:
            cb = ''
        else:
            cb = ': '+str(cmd.command_length)
        cn = cmd.__name__
        print(f'    {cn}.command_value : {cn}, # ({U.hex2(cmd.command_value)}) {cb}')
        


