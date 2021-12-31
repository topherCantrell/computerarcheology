from digs.raaka_bed import decoder_functions as FUN
from digs.raaka_bed import unpacker
import digs.raaka_bed.commands as RTC
import util.util as U


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
    
    def print_assembly(self,pos,ident,out):
        s = U.hex4(pos)+': '+U.hex2(self.command_value)+' 02 ; HIT POINTS'
        out.append(U.indent_code(s,ident)) 
        pos+=2
        s = U.hex4(pos)+': '+U.hex2(self._max)+' '+U.hex2(self._current)+' ; maxHitPoints='+U.hex2(self._max)+' currentHitPoints='+U.hex2(self._current)
        out.append(U.indent_code(s,ident)) 
        return pos+2
    
    def tojson(self,parent,include_scripts=True):
        parent['max_points'] = self._max
        parent['current_points'] = self._current      
        
class Adjectives:
    
    command_value = 1
    command_name = '01 ADJECTIVES'
    
    def parse_binary(self,data):
        #print(ShortName.command_name)
        self._raw_data = data
        if len(data)!=1:
            raise Exception('OOPS ... expected only one adjective')       
        self._adjective = data[0] 
        
    def get_assembly(self): 
        return bytes([self.command_value])+RTC.BaseCommand.make_length_bytes(len(self._raw_data))+self._raw_data    
    
    def print_assembly(self,pos,ident,out):
        pre = bytes([self.command_value]) + RTC.BaseCommand.make_length_bytes(len(self._raw_data))
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; '+self.command_name
        out.append(U.indent_code(s,ident))
        pos += len(pre)
        s = U.hex4(pos)+': '+U.hex2(self._adjective)+' ; TODO WORD'
        out.append(U.indent_code(s,ident))          
        return pos+1   
    
    def tojson(self,parent,include_scripts=True):
        parent['adjectives'] = self._adjective 
    
class ShortName:
    
    command_value = 2
    command_name = '02 SHORT_NAME'
    
    def parse_binary(self,data):
        #print(ShortName.command_name)
        self._raw_data = data
        self._text = unpacker.decode_message(data)        
        
    def get_assembly(self): 
        return bytes([self.command_value])+RTC.BaseCommand.make_length_bytes(len(self._raw_data))+self._raw_data    
    
    def print_assembly(self,pos,ident,out):
        pre = bytes([self.command_value]) + RTC.BaseCommand.make_length_bytes(len(self._raw_data))
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; '+self.command_name
        out.append(U.indent_code(s,ident))
        pos += len(pre)
        pos = RTC.PrintMessage.print_assembly_text(pos,ident+1,self._raw_data,self._text,out)             
        return pos   
    
    def tojson(self,parent,include_scripts=True):
        parent['short_name'] = self._text 
    
class Description:
    
    # Two different versions of this. In RaakaTu, it is just a packed string (like short-name)
    # In Bedlam, it is a command script
    
    command_value = 3
    command_name = '03 DESCRIPTION'
     
    def parse_binary(self,data):        
        if FUN.decode_is_bedlam():
            self._raw_data = data
            self._command = RTC.decode_script(data)
        else:
            self._raw_data = data
            self._text = unpacker.decode_message(data)
            #print(Description.command_name,self._text)
        
    def get_assembly(self): 
        if FUN.decode_is_bedlam():
            data = b''
            for com in self._command:
                data = data + com.get_assembly()
            return bytes([self.command_value])+RTC.BaseCommand.make_length_bytes(len(data))+data
        else:
            return bytes([self.command_value])+RTC.BaseCommand.make_length_bytes(len(self._raw_data))+self._raw_data
    
    def print_assembly(self,pos,ident,out):
        if FUN.decode_is_bedlam():
            data = b''
            for com in self._command:
                data = data + com.get_assembly()            
            pre = bytes([self.command_value]) + RTC.BaseCommand.make_length_bytes(len(data))
            s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; '+self.command_name
            out.append(U.indent_code(s,ident))  
            pos += len(pre)
            
            for com in self._command:
                pos = com.print_assembly(pos,ident+1,out)
            
            return pos
        else:
            pre = bytes([self.command_value]) + RTC.BaseCommand.make_length_bytes(len(self._raw_data))
            s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; '+self.command_name
            out.append(U.indent_code(s,ident))
            pos += len(pre)
            pos = RTC.PrintMessage.print_assembly_text(pos,ident+1,self._raw_data,self._text,out)             
            return pos
    
    def tojson(self,parent,include_scripts=True):
        if FUN.decode_is_bedlam():
            script = []
            parent['description'] = script
            for com in self._command:
                script.append(com.tojson())
        else:
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
    
    def print_assembly(self,pos,ident,out):
        
        data = b''
        for com in self._command:
            data = data + com.get_assembly()            
        pre = bytes([self.command_value]) + RTC.BaseCommand.make_length_bytes(len(data))
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; '+self.command_name
        out.append(U.indent_code(s,ident))  
        pos += len(pre)
        
        for com in self._command:
            pos = com.print_assembly(pos,ident+1,out)
        
        return pos
    
    def tojson(self,parent,include_scripts=True):
        script = []
        parent['user_input_handler'] = script
        if include_scripts:
            for com in self._command:
                script.append(com.tojson())

class HandlerGivenCommand:
    command_value = 0x0B
    command_name = '0B COMMAND HANDLING IF GIVEN COMMAND'
    
    def parse_binary(self,data):
        #print(HandlerAsSecondNoun.command_name)
        self._raw_data = data
        self._script = RTC.decode_script(data)
        
    def get_assembly(self): 
        data = b''
        for com in self._script:
            data = data + com.get_assembly()
        return bytes([self.command_value])+RTC.BaseCommand.make_length_bytes(len(data))+data
    
    def print_assembly(self,pos,ident,out):
        
        data = b''
        for com in self._script:
            data = data + com.get_assembly()            
        pre = bytes([self.command_value]) + RTC.BaseCommand.make_length_bytes(len(data))
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; '+self.command_name
        out.append(U.indent_code(s,ident)) 
        pos += len(pre)
        
        for com in self._script:
            pos = com.print_assembly(pos,ident+1,out)
        
        return pos
    
    def tojson(self,parent,include_scripts=True):
        
        script = []
        parent['handler_if_given_command'] = script
        if include_scripts:
            for com in self._script:
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
    
    def print_assembly(self,pos,ident,out):
        
        data = b''
        for com in self._script:
            data = data + com.get_assembly()            
        pre = bytes([self.command_value]) + RTC.BaseCommand.make_length_bytes(len(data))
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; '+self.command_name
        out.append(U.indent_code(s,ident)) 
        pos += len(pre)
        
        for com in self._script:
            pos = com.print_assembly(pos,ident+1,out)
        
        return pos
    
    def tojson(self,parent,include_scripts=True):
        
        script = []
        parent['handler_if_second_noun'] = script
        if include_scripts:
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
    
    def print_assembly(self,pos,ident,out):
        
        data = b''
        for com in self._script:
            data = data + com.get_assembly()            
        pre = bytes([self.command_value]) + RTC.BaseCommand.make_length_bytes(len(data))
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; '+self.command_name
        out.append(U.indent_code(s,ident)) 
        pos += len(pre)
        
        for com in self._script:
            pos = com.print_assembly(pos,ident+1,out)
        
        return pos
    
    def tojson(self,parent,include_scripts=True):
        script = []
        parent['handler_if_first_noun'] = script
        if include_scripts:
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
    
    def print_assembly(self,pos,ident,out):
        
        data = b''
        for com in self._script:
            data = data + com.get_assembly()            
        pre = bytes([self.command_value]) + RTC.BaseCommand.make_length_bytes(len(data))
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; '+self.command_name
        out.append(U.indent_code(s,ident)) 
        pos += len(pre)
        
        for com in self._script:
            pos = com.print_assembly(pos,ident+1,out)
        
        return pos
    
    def tojson(self,parent,include_scripts=True):
        script = []
        parent['handler_every_turn'] = script
        if include_scripts:
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
    
    def print_assembly(self,pos,ident,out):
        
        data = b''
        for com in self._script:
            data = data + com.get_assembly()            
        pre = bytes([self.command_value]) + RTC.BaseCommand.make_length_bytes(len(data))
        s = U.hex4(pos)+': '+U.dump_bytes(pre)+' ; '+self.command_name
        out.append(U.indent_code(s,ident)) 
        pos += len(pre)
        
        for com in self._script:
            pos = com.print_assembly(pos,ident+1,out)
        
        return pos
    
    def tojson(self,parent,include_scripts=True):
        script = []
        parent['on_death_handler'] = script
        if include_scripts:
            for com in self._script:
                script.append(com.tojson())       

OBJ_ATTRIBUTES = {
    Adjectives.command_value : Adjectives, # 01
    ShortName.command_value : ShortName, # 02
    Description.command_value : Description, # 03
    CommandScript.command_value : CommandScript, # 04
    # 05 ?
    HandlerAsSecondNoun.command_value : HandlerAsSecondNoun, #06
    HandlerAsFirstNoun.command_value : HandlerAsFirstNoun, #07
    HandlerTurn.command_value : HandlerTurn, #08
    HitPoints.command_value : HitPoints, # 09
    HandlerDeath.command_value : HandlerDeath, # 0A    
    HandlerGivenCommand.command_value : HandlerGivenCommand, # 0B
}
