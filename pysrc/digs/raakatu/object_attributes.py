from digs.raakatu import unpacker
import digs.raakatu.raakatu_commands as RTC
import util.util as U

class ShortName:
    
    command_value = 2
    command_name = '02 SHORT_NAME'
    
    def parse_binary(self,data):
        #print(ShortName.command_name)
        self._raw_data = data
        self._text = unpacker.decode_message(data)        
        
    def get_assembly(self): 
        return bytes([self.command_value])+RTC.BaseCommand.make_length_bytes(len(self._raw_data))+self._raw_data    
    
    def print_assembly(self,pos,ident):
        pre = bytes([self.command_value]) + RTC.BaseCommand.make_length_bytes(len(self._raw_data))
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; '+self.command_name
        print(U.indent_code(s,ident))
        pos += len(pre)
        pos = RTC.PrintMessage.print_assembly_text(pos,ident+1,self._raw_data,self._text)             
        return pos   
    
    def tojson(self,parent):
        parent['short_name'] = self._text 
 
class Description:
    
    command_value = 3
    command_name = '03 DESCRIPTION'
     
    def parse_binary(self,data):        
        self._raw_data = data
        self._text = unpacker.decode_message(data)
        #print(Description.command_name,self._text)
        
    def get_assembly(self): 
        return bytes([self.command_value])+RTC.BaseCommand.make_length_bytes(len(self._raw_data))+self._raw_data
    
    def print_assembly(self,pos,ident):
        pre = bytes([self.command_value]) + RTC.BaseCommand.make_length_bytes(len(self._raw_data))
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; '+self.command_name
        print(U.indent_code(s,ident))
        pos += len(pre)
        pos = RTC.PrintMessage.print_assembly_text(pos,ident+1,self._raw_data,self._text)             
        return pos
    
    def tojson(self,parent):
        parent['description'] = self._text
    
class CommandScript:
    
    command_value = 4
    command_name = '04 COMMAND'
       
    def parse_binary(self,data):
        #print(self.command_name)
        self._raw_data = data
        self._command = RTC.decode_script(data)
    
    def get_assembly(self): 
        data = b''
        for com in self._command:
            data = data + com.get_assembly()
        return bytes([self.command_value])+RTC.BaseCommand.make_length_bytes(len(data))+data
    
    def print_assembly(self,pos,ident):
        
        data = b''
        for com in self._command:
            data = data + com.get_assembly()            
        pre = bytes([self.command_value]) + RTC.BaseCommand.make_length_bytes(len(data))
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; '+self.command_name
        print(U.indent_code(s,ident))  
        pos += len(pre)
        
        for com in self._command:
            pos = com.print_assembly(pos,ident+1)
        
        return pos
    
    def tojson(self,parent):
        script = []
        parent['user_input_handler'] = script
        for com in self._command:
            script.append(com.tojson())
   
class HandlerAsSecondNoun:
    
    command_value = 6
    command_name = '06 COMMAND HANDLING IF SECOND NOUN'
       
    def parse_binary(self,data):
        #print(HandlerAsSecondNoun.command_name)
        self._raw_data = data
        self._script = RTC.decode_script(data)
        
    def get_assembly(self): 
        data = b''
        for com in self._script:
            data = data + com.get_assembly()
        return bytes([self.command_value])+RTC.BaseCommand.make_length_bytes(len(data))+data
    
    def print_assembly(self,pos,ident):
        
        data = b''
        for com in self._script:
            data = data + com.get_assembly()            
        pre = bytes([self.command_value]) + RTC.BaseCommand.make_length_bytes(len(data))
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; '+self.command_name
        print(U.indent_code(s,ident)) 
        pos += len(pre)
        
        for com in self._script:
            pos = com.print_assembly(pos,ident+1)
        
        return pos
    
    def tojson(self,parent):
        
        script = []
        parent['handler_if_second_noun'] = script
        for com in self._script:
            script.append(com.tojson())
        
   
class HandlerAsFirstNoun:
    
    command_value = 7
    command_name = '07 COMMAND HANDLING IF FIRST NOUN'
      
    def parse_binary(self,data):
        #print(HandlerAsFirstNoun.command_name)
        self._raw_data = data
        self._script = RTC.decode_script(data)
        
    def get_assembly(self): 
        data = b''
        for com in self._script:
            data = data + com.get_assembly()
        return bytes([self.command_value])+RTC.BaseCommand.make_length_bytes(len(data))+data
    
    def print_assembly(self,pos,ident):
        
        data = b''
        for com in self._script:
            data = data + com.get_assembly()            
        pre = bytes([self.command_value]) + RTC.BaseCommand.make_length_bytes(len(data))
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; '+self.command_name
        print(U.indent_code(s,ident)) 
        pos += len(pre)
        
        for com in self._script:
            pos = com.print_assembly(pos,ident+1)
        
        return pos
    
    def tojson(self,parent):
        script = []
        parent['handler_if_first_noun'] = script
        for com in self._script:
            script.append(com.tojson())
        
  
class HandlerTurn:
    
    command_value = 8
    command_name = '08 TURN SCRIPT'

    def parse_binary(self,data):
        #print(HandlerTurn.command_name)
        self._raw_data = data
        self._script = RTC.decode_script(data)
        
    def get_assembly(self): 
        data = b''
        for com in self._script:
            data = data + com.get_assembly()
        return bytes([self.command_value])+RTC.BaseCommand.make_length_bytes(len(data))+data
    
    def print_assembly(self,pos,ident):
        
        data = b''
        for com in self._script:
            data = data + com.get_assembly()            
        pre = bytes([self.command_value]) + RTC.BaseCommand.make_length_bytes(len(data))
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; '+self.command_name
        print(U.indent_code(s,ident)) 
        pos += len(pre)
        
        for com in self._script:
            pos = com.print_assembly(pos,ident+1)
        
        return pos
    
    def tojson(self,parent):
        script = []
        parent['handler_every_turn'] = script
        for com in self._script:
            script.append(com.tojson())        
    
class HandlerDeath:
    
    command_value = 10
    command_name = '0A UPON DEATH SCRIPT'
        
    def parse_binary(self,data):
        #print(HandlerTurn.command_name)
        self._raw_data = data
        self._script = RTC.decode_script(data)
        
    def get_assembly(self): 
        data = b''
        for com in self._script:
            data = data + com.get_assembly()
        return bytes([self.command_value])+RTC.BaseCommand.make_length_bytes(len(data))+data
    
    def print_assembly(self,pos,ident):
        
        data = b''
        for com in self._script:
            data = data + com.get_assembly()            
        pre = bytes([self.command_value]) + RTC.BaseCommand.make_length_bytes(len(data))
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; '+self.command_name
        print(U.indent_code(s,ident)) 
        pos += len(pre)
        
        for com in self._script:
            pos = com.print_assembly(pos,ident+1)
        
        return pos
    
    def tojson(self,parent):
        script = []
        parent['on_death_handler'] = script
        for com in self._script:
            script.append(com.tojson())        
            
class HitPoints:
    
    command_value = 9
    command_name = '09 HIT POINTS'
    
    def parse_binary(self,data):
        #print(HitPoints.command_name)
        self._raw_data = data
        self._max = data[0]
        self._current = data[1]
    
    def get_assembly(self): 
        return bytes([self.command_value])+RTC.BaseCommand.make_length_bytes(len(self._raw_data))+bytes([self._max,self._current])   
    
    def print_assembly(self,pos,ident):
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' 02 ; HIT POINTS'
        print(U.indent_code(s,ident)) 
        pos+=2
        s = U.hex4(pos)+': '+U.hex2(self._max)+' '+U.hex2(self._current)+' ; maxHitPoints='+U.hex2(self._max)+' currentHitPoints='+U.hex2(self._current)
        print(U.indent_code(s,ident)) 
        return pos+2
    
    def tojson(self,parent):
        parent['max_points'] = self._max
        parent['current_points'] = self._current      

def decode_noun(n,collapse_zero=True):
    if collapse_zero and n==0:
        return '*'
    ret = ''
    if n&0x80:
        ret=ret+'u'
    else:
        ret=ret+'.'
    if n&0x40:
        ret = ret + 'v'
    else:
        ret = ret + '.'
    if n&0x20:
        ret = ret + 'C'
    else:
        ret = ret + '.'
    if n&0x10:
        ret = ret + 'P'
    else:
        ret = ret + '.'
    if n&0x08:
        ret = ret + 'A'
    else:
        ret = ret + '.'
    if n&0x04:
        ret = ret + 'X'
    else:
        ret = ret + '.'
    if n&0x02:
        ret = ret + 'O'
    else:
        ret = ret + '.'
    if n&0x01:
        ret = ret + 'L'
    else:
        ret = ret + '.'
        
    return ret

OBJ_ATTRIBUTES = {
    ShortName.command_value : ShortName,
    Description.command_value : Description,
    HandlerAsSecondNoun.command_value : HandlerAsSecondNoun,
    HandlerAsFirstNoun.command_value : HandlerAsFirstNoun,
    HandlerTurn.command_value : HandlerTurn,
    HitPoints.command_value : HitPoints,
    HandlerDeath.command_value : HandlerDeath,
    CommandScript.command_value : CommandScript,      
}