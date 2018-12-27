#from code.block_line import Block

from code.code_line import CodeLine

def process_code(lines,code_info):
    
    code = []
    cpu = code_info['cpu']
    
    for md in lines: 
        if str(type(md)) == "<class 'code.block_line.Block'>":     
            for m in md.lines:
                if type(m) is CodeLine and m.data!=None:
                    code.append(m)   
                            
    for c in code: 
        if c.mnemonic != None:      
            ops = cpu.get_opcode_from_data(c.data)
            if len(ops)==0:
                raise Exception("Opcode not found "+c.original.line)
            if len(ops)>1:
                alias = cpu.pick_opcode_from_aliases(c.mnemonic,ops)
                if alias == None:
                    raise Exception("Opcode not found "+c.original.line) 
                ops = [alias]    
            c.opcode = ops[0]        
    
    '''
    
    Attach a link_info_structure to each line:
    
    here:
    F000: 15 25     LDA   #$25   ; {is_target: True}
    F002: 20 F3     STA   $F3    ; {opcode_i:5, opcode_j:7, memory_table: *, memory_table_entry: *}
    F004: 88 F0 00  JMP   $F000  ; {opcode_i:5, opcode_j:9, target_label: 'here', target_line: *}
    
    {
        is_target: boolean         True if this line is to be an ID for an anchor
        target_line: CodeLine      Pointer to the line this constant targets
        target_label: str          String if there is a label at the target point (rename the constant)
        opcode_i: int              Starting point of the constant in the opcode
        opcode_j: int              Ending point of the constant in the opcode
        memory_table: MemoryTable  If this is a memory table reference
        memory_table_entry: dict   If this is a memory table reference
    }
    
    '''
    
    # Destination code line: {
    #    is_target:bool  True if this line should have an ID for an anchor
    # }
    
    # Source code line: {target_line:CodeLine,label:str,i:int,j:int}
    
    # TODO look for jumps, addresses, etc
    for c in code:
        if c.opcode != None:
            if cpu.is_bus_x(c.opcode):
                print(c.original.line+':'+str(c.opcode))
        
    code_info['processed_code'] = code
    