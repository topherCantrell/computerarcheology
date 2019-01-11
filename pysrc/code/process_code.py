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

def process_code(lines,code_info,skip_no_label_jumps=False):
    
    # We'll use this a lot
    cpu = code_info['cpu']
    
    # Collect all the code together. Everything else is text.
    code = []
    for md in lines: 
        if str(type(md)) == "<class 'code.block_line.Block'>":     
            for m in md.lines:
                if type(m) is CodeLine:
                    code.append(m)   
    
    # For all lines with mnemonics: find the opcode for each                        
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
            
    # Collect the labels
    labels = {}
    for i in range(len(code)):
        c = code[i]
        if c.label:            
            if c.label in labels:
                raise Exception('Label already defined:'+c.label)
            for j in range(i+1,len(code)):
                if code[j].data and len(code[j].data)>0:
                    labels[code[j].address] = {'label':c.label,'target' : code[j]}                    
                    break
            if j==len(code):
                raise Exception('No data to attach label to:'+c.label)
        
    '''
    
    Attach a link_info_structure to each line:
    
    here:
    F000: 15 25     LDA   #$25   ; {is_target: True}
    F002: 20 F3     STA   $F3    ; {opcode_i:5, opcode_j:7, memory_table: *, memory_table_entry: *}
    F004: 88 F0 00  JMP   $F000  ; {opcode_i:5, opcode_j:9, target_label: 'here', target_line: *}
    
    {
    # If this line has somebody targeting it
        is_target: boolean         True if this line is to be an ID for an anchor
        
    # If this line is reference to code
        target_line: CodeLine      Pointer to the line this constant targets
        target_label: str          String if there is a label at the target point (rename the constant)
        opcode_i: int              Starting point of the constant in the opcode
        opcode_j: int              Ending point of the constant in the opcode
    # OR If this line is a reference to an entry in a memory table   
        memory_table: MemoryTable  If this is a memory table reference
        memory_table_name: str     If this is a memory table reference
        memory_table_entry: dict   If this is a memory table reference
        opcode_i: int              Starting point of the constant in the opcode
        opcode_j: int              Ending point of the constant in the opcode
    }
        
    ; {!+ram:buffer} The numeric constant is to be processed as an address even if the opcode doesn't think so
    ; {!-} The numeric constant is not to be processed as an address even if the opcode thinks it should
    ; {doProcessing} Regular, replaced information
    
    '''       
                  
    code_info['unknown_memory'] = []
    
    
    
    # For each opcode that is a memory reference, make a reference to a line the code or an entry in a memory table          
    for c in code:
        if c.opcode != None:
            
            memref = cpu.is_memory_reference(c.opcode)
            if c.comment and '{!+' in c.comment:
                memref = True
            elif c.comment and '{!-}' in c.comment:
                memref = False                
            
            if memref:       
                # Record the opcode start and stop                      
                i = c.original.line.index('$')
                j = find_end_of_hex(c.original.line,i+1)
                if c.link_info == None:
                    c.link_info = {}
                c.link_info = {'opcode_i':i,'opcode_j':j}
                
                # This is the referenced memory                   
                addr = int(c.original.line[i+1:j],16)
                
                
                # First, see if this is in the code
                for d in code:
                    if d.is_address_in(addr):
                        c.link_info['target_line'] = d
                        if d.link_info == None:
                            d.link_info = {}
                        d.link_info['is_target']=True
                        if addr in labels:                            
                            entry = labels[addr]
                            c.link_info['target_label'] = entry['label'] 
                        break
                
                # No? Then check all the memory tables we know of
                if not 'target_line' in c.link_info:                    
                    for table in code_info['memory']:                        
                        tab = code_info['memory'][table]                        
                        entry = tab.find_entry(addr)
                        if entry:                            
                            c.link_info['memory_table'] = tab 
                            c.link_info['memory_table_name'] = table
                            c.link_info['memory_table_entry'] = entry
                
                # We have no info on these memory addresses. Remove the link info
                if not 'target_line' in c.link_info and not 'memory_table' in c.link_info:
                    #print(c.original.line) 
                    code_info['unknown_memory'] = {'address':addr,'line':c}       
                    c.link_info = None    
                                                 
                if c.link_info:
                    # Replace the information in the comment
                    nc = c.comment
                    if not nc:
                        nc = ''
                    
                    if not '{!-}' in nc:                    
                        if '{' in nc:
                            i = nc.index('{')
                            j = nc.index('}')+1
                            override = (nc[i+1]=='!')
                        else:
                            i = 0
                            j = 0
                            override = False
                        if 'memory_table' in c.link_info:
                            ns = c.link_info['memory_table_name']+':'+c.link_info['memory_table_entry']['name']                                
                        else:
                            if 'target_label' in c.link_info:
                                ns = c.link_info['target_label']
                            else:
                                if skip_no_label_jumps:
                                    ns = ''
                                else:
                                    ns = format(c.link_info['target_line'].address,'04X')
                                    
                        nc = (nc[0:i]+nc[j:]).strip()
                        
                        if override:
                            nc = '{!+'+ns+'} '+nc
                        elif skip_no_label_jumps and 'target_line' in c.link_info and not 'target_label' in c.link_info:
                            nc = nc
                        else:
                            nc = '{'+ns+'} '+nc
                            
                        # Replace the existing comment (or prepend a new one)
                        c.replace_comment(nc) 
                                                                   
    code_info['processed_code'] = code
    