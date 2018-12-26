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
    
    # TODO look for jumps, addresses, etc
    for c in code:
        if c.opcode != None:
            if cpu.is_bus_x(c.opcode):
                print(c.original.line+':'+str(c.opcode))
        
    code_info['processed_code'] = code
    