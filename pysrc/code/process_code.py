#from code.block_line import Block

from code.code_line import CodeLine

def is_hex_digit(d):
    if d>='0' and d<='9':
        return True
    if d>='A' and d<='F':
        return True
    
def find_end_of_hex(s,p=0):
    while True:
        if p>=len(s):
            return p
        if not is_hex_digit(s[p]):
            return p
        p+=1

def process_code(lines,code_info):
    
    code = []
    cpu = code_info['cpu']
    
    for md in lines: 
        if str(type(md)) == "<class 'code.block_line.Block'>":     
            for m in md.lines:
                if type(m) is CodeLine:
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
            
    # TODO collect the label addresses
    
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
            
    for c in code:
        if c.opcode != None:
            if cpu.is_memory_reference(c.opcode):                             
                i = c.original.line.index('$')
                j = find_end_of_hex(c.original.line,i+1)
                link_info = {'opcode_i':i,'opcode_j':j}
                c.link_info = link_info   
                addr = int(c.original.line[i+1:j],16)
                
                for d in code:
                    if d.is_address_in(addr):
                        print(":::"+d.original.line)
                        break
                
                # TODO where is this address? Is it in the code? Is it in a table?
                
                
                if cpu.is_bus_x(c.opcode):
                    print('*'+c.original.line+':'+str(c.opcode))
                else:
                    print('%'+c.original.line+':'+str(c.opcode))   
                print(c.original.line[i:j])         
        
    code_info['processed_code'] = code
    