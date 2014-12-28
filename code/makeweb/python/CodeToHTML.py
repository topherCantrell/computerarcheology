from CodeLine import CodeLine

def translate(inName,outName):
    # Read the code
    with open(inName) as f:
        raw = f.readlines()   
        
    ret = []
    for r in raw:
        
        t = r.strip()
        
        # Keep comment lines as-is
        if t.startswith(";"):
            ret.append(r)
            continue
        
        # Keep blank lines as-is
        if t=="":
            ret.append(r)
            continue
        
        # Must be code. Parse that.
        c = CodeLine()
        c.parse(r)
        ret.append(c)
        
    for o in ret:
        if isinstance(o,CodeLine):
            if o.comment and '{' in o.comment:
                print o.comment
        

if __name__ == "__main__":    
   translate("../../../content/CoCo/MadnessMinotaur/Code.mark",
             "../../../deploy/CoCo/MadnessMinotaur/Code.html")