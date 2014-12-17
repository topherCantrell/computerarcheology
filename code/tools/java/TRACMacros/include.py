
from trac.wiki.macros import WikiMacroBase
from trac.wiki.model import WikiPage

from trac.wiki.api import WikiSystem, parse_args

class IncludeMacro(WikiMacroBase):
    
    def get_page_text(self, formatter, page_resource):
        """Return a tuple of `(text, exists)` for the given page (resource)."""
        if page_resource.id == formatter.context.resource.id:
            return (formatter.source, True)
        else:
            page = WikiPage(self.env, page_resource)
            return (page.text, page.exists)
    
    def expand_macro(self, formatter, name, args):
        context = formatter.context
        resource = formatter.context.resource
        
        # Parse the arguments
        args, kw = parse_args(args)
               
        # Make sure we got all three arguments
        if "page" not in kw:
            return "Must specify 'page'"
        if "start" not in kw:
            return "Must specify 'start'"
        if "stop" not in kw:
            return "Must specify 'stop'"
        
        page  = kw["page"]
        start = kw["start"]
        stop  = kw["stop"]
                           
        # Make sure the viewer has access to the included page     
        page_resource = resource(id=page)
        if not 'WIKI_VIEW' in context.perm(page_resource):            
            return 'No WIKI_VIEW access to '+page
        
        # Get the page text (make sure the page exists)
        page_text, page_exist = self.get_page_text(formatter, page_resource)        
        if not page_exist:
            return "Referenced 'page='"+page+" does not exist"
        
        txt = page_text.splitlines()
        
        startPos = findLine(txt,start)
        stopPos = findLine(txt,stop,startPos)
        
        ret = "<pre class='wiki'>"
        retSet = txt[startPos:stopPos]
        for line in retSet:
            ret = ret+line+"\n"
        ret = ret+"</pre>"
                
        return ret
    
    
#startsWith('value')
#endsWith('value')
#contains('value')
#notStartsWith('value') * n +- m
def findLine(text,target,startPos=0):
    i = target.find('(')
    if i<0:
        return -1
    com = target[0:i].strip()
    
    j = target.rfind(')')
    if j<0:
        return -1
    txt = target[i+1:j].strip()
        
    target = target[j+1:].strip()
    
    multiplier = 1
    offset = 0    
    
    if len(target)>0 and target[0] == '*':
        i = target.find('+')
        if i<0:
            i = target.find('-')
        if i<0:
            i = len(target)
        if i>0:
            mult = target[1:i].strip()
            target = target[i:].strip()
            if mult.isdigit():
                multiplier = int(mult)
               
    sign = 0
    if len(target)>0 and target[0] == '+':
        sign = 1
        target = target[1:].strip()
    elif len(target)>0 and target[0] == '-':
        sign = -1
        target = target[1:].strip()
                
    if target.isdigit():
        offset = int(target) * sign
        
    ttext = text[startPos:]
    ret = -1
    if com == "startsWith":
        for line in ttext:
            ret += 1
            if line.startswith(txt):
                multiplier-=1
                if multiplier<=0:
                    return ret+offset+startPos
    elif com == "endsWith":
        for line in ttext:
            ret += 1
            if line.endswith(txt):
                multiplier-=1
                if multiplier<=0:
                    return ret+offset+startPos
    elif com == "contains":
        for line in ttext:
            ret += 1
            if line.find(txt)>=0:
                multiplier-=1
                if multiplier<=0:
                    return ret+offset+startPos
    elif com == "notStartsWith":
        for line in ttext:
            ret += 1
            if not line.startswith(txt):
                multiplier-=1
                if multiplier<=0:
                    return ret+offset+startPos       
    
    return -1
    
#f = open("c:\\projects\\computerarcheology\\spaceinvaders\\spaceinvaders.txt")
#page_text = f.readlines()
    
#i = findLine(page_text,"startsWith(;##! <canvas)*2+1",10)
#j = findLine(page_text,"startsWith(;##! </canvas>)",i)

#print str(j)+":"+page_text[j]

