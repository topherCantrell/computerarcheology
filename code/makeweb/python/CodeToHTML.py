from CodeLine import CodeLine

from AddressToHTML import AddressToHTML
from MarkupToHTML import MarkupToHTML

from Config import rootDir
from Config import deployDir

class CodeToHTML(MarkupToHTML):
    
    def getAddressMap(self,filename):
        ad = AddressToHTML()
        ad.loadMap(rootDir+filename)
        return ad
    
    def collectLabels(self,lines):
        cur = []
        for x in xrange(len(lines)):
            r = lines[x]
            if isinstance(r,CodeLine):
                if len(r.bytes)==0 and not r.opcode:
                    # This is a label. Save it for the next real line of code.
                    for i in r.labels:
                        cur.append(i)
                    lines[x].collected = True
                else:
                    # This is a line of code. Add all the free labels before it.
                    lines[x].collected = False
                    if len(cur)>0:
                        for i in cur:
                            lines[x].labels.append(i)
                        cur = []
    
    def addCodeLinkTargetIDs(self,lines):        
        for line in lines:
            
            if not isinstance(line,CodeLine): # only looking at CodeLines
                continue 
            
             # Always id the labels
            if not line.opcode and not line.bytes:
                line.linkID = line.labels[0]
            
            # A "{}" means we have to lookup the code address
            if not line.target:               # and only if they have a target in the comment
                continue
            if not line.target["map"]=="":    # and only if that target is in code
                continue
            
            if not line.target["target"]=="": # Could be an explicit target
                if not line.target["target"] in self.labels:
                    print "COULD NOT FIND '"+line.target["target"]+"'"                            
            
            # This an empty {} ... look up the label
            
            for x in xrange(len(lines)):
                g = lines[x]
                if isinstance(g,CodeLine) and g.address==line.numbers[0]["value"]:                    
                    g.linkID = line.numbers[0]["text"][1:]
                    # This line of code might also have a preceding label. Let's look for that.
                    y = x
                    while y>=0:
                        if not isinstance(lines[y],CodeLine):
                            y = y - 1
                            continue
                        if lines[y].labels:
                            if (line.target["target"]!="") and (line.collected==False) and (not line.target["target"] in lines[y].labels):
                                print "TARGET SAYS '"+line.target["target"]+"' BUT I THINK IT SHOULD BE '"+lines[y].labels[0]+"'"
                                print lines[y-5].labels
                                print lines[y].labels
                            line.target["target"] = lines[y].labels[0]
                            if line.target["text"] == "":
                                line.target["text"] = lines[y].labels[0]
                            del g.linkID
                        break
                        
                    
    def makeAddressAnchor(self,line,maps):
        # TODO: handle RAM and Hardware
        
        tar = line.target["target"]
        txt = line.target["text"]
        aClass = "codeAddressLink"
        
        if line.target["map"]=="ram":
            if tar=="":
                ad = maps["ramMap"]                
                entry = ad.getEntry(line.numbers[0]["value"])
                if txt=="":
                    txt = entry["name"]
                    if txt=="":
                        txt = line.numbers[0]["text"]                        
                tar = ad.mapURL+"#"+entry["target"]
                aClass = "ramAddressLink"
                trg = "TAB_RAM"
        elif line.target["map"]=="hardware":
            if tar=="":
                ad = maps["hardwareMap"]
                entry = ad.getEntry(line.numbers[0]["value"])
                if txt=="":
                    txt = entry["name"]
                    if txt=="":
                        txt = line.numbers[0]["text"]
                tar = ad.mapURL+"#"+entry["target"]
                aClass = "hardwareAddressLink"
                trg="TAB_HARDWARE"                     
        else:
            trg = "_self"
            if tar=="":
                tar = line.numbers[0]["text"][1:]
                while len(tar)<4:
                    tar = "0"+tar
            if not "/" in tar:
                tar = "#" + tar
            if txt=="":
                txt = line.numbers[0]["text"]               
             
        a = '<a class="%s" href="%s" title="%s" target="%s">%s</a>'  
        rep = a % (aClass,tar,line.numbers[0]["text"],trg,txt )
        return (len(txt),rep)
                    
    def modifyCodeLines(self,lines,maps):        
        for line in lines:
            if not isinstance(line,CodeLine): # only looking at CodeLines
                continue 
            
            # First change the numbers to links
            
            if line.target:
                # There are three possible placements:
                # "inline"   - Replace the number in the opcode
                # "side"     - To the immediate right of the opcode
                # "comment"  - In the comments (where the markup was)
                
                (lenRep,rep) = self.makeAddressAnchor(line,maps)                
                
                # A little tricky here. The comments are usually lined up nicely down
                # the page, but we are going to change the spacing.
                
                newText = line.original
                if line.comment:
                    i = line.originalCommentPos - 1
                    while newText[i] == ' ':
                        i = i - 1
                    newText = newText[0:i+1]
                
                if line.target["placement"] == "comment":
                    raise Exception("TODO")
                
                elif line.target["placement"] == "side":
                    raise Exception("TODO")
                
                else: # Must be "inline"
                    first = newText[0:line.numbers[0]["startPos"]+line.originalOpcodePos]
                    last =  newText[line.numbers[0]["startPos"]+line.originalOpcodePos+line.numbers[0]["textLen"]:]                  
                    newText =  first + rep + last                      
                    opVisLen = len(first)+lenRep+len(last)                    
                    while opVisLen<line.originalCommentPos:
                        newText = newText + " "         
                        opVisLen = opVisLen + 1           
                    newText = newText + ";"+line.comment                    
                    line.original = newText
                    
            # Now for any ID
            if hasattr(line,"linkID"):
                n = line.linkID
                while len(n)<4:
                    n = "0"+n
                line.original = '<span class="siteTarget" id="'+n+'">'+line.original[0]+'</span>'+line.original[1:] 
                
                
    def translate(self, inName, outName, breadCrumbs, siteTree, title):
        # Read the code
        with open(inName) as f:
            raw = f.readlines()
            
        self.labels = []
            
        maps = {}
        ret = []
        for r in raw:                        
                        
            t = r.strip() 
                           
            if t.startswith(";;%%ramMap"):
                maps["ramMap"] = self.getAddressMap(t[10:].strip()) #;%%ramMap RAMUse.mark 
                continue
            elif t.startswith(";;%%hardwareMap"):
                maps["hardwareMap"] = self.getAddressMap(t[15:].strip()) #;%%hardwareMap /Coco/Hardware.mark
                continue
            
            # Keep comment lines as-is
            if t.startswith(";"):
                ret.append(self.entizeString(r))
                continue
            
            # Keep blank lines as-is
            if t=="":
                ret.append(r)
                continue
            
            # Must be code. Parse that.
            c = CodeLine()
            c.parse(r)
            ret.append(c)
            
            for a in c.labels:
                if a in self.labels:
                    raise Exception("Duplicate label '"+a+"'")
                self.labels.append(a)
                
        # Get all the labels together
        self.collectLabels(ret)
                
        # These are all the code lines that need to have "id" added to them
        self.addCodeLinkTargetIDs(ret) 
        
        # Change the code line to include the HTML spans and anchors
        self.modifyCodeLines(ret,maps)
        
        raw = []
        for r in ret:
            if isinstance(r,CodeLine):
                raw.append(r.original)
            else:
                raw.append(r)
                
        for x in xrange(len(raw)):
            if not raw[x].endswith("\n"):
                raw[x] = raw[x] + "\n"
                        
        MarkupToHTML.translate(self,inName,outName,breadCrumbs,siteTree,title,raw)
        
    def markDown(self,raw,fills,pageNav):
        self.headers = []
        
        mode="none" 
        
        bodyLines = ['<pre class="codePreStyle">']  # List of lines for the body
        for line in raw:    
            
            if not line.startswith(";"):
                bodyLines.append(line)
                continue  
            
            # -- Markup processing on full-line comments --          
            
            # Handle defines
            if line.startswith(";%%"):
                i = line.index(" ")
                fills[line[3:i]] = line[i+1:].strip()
                continue
                                        
            # Handle quick headers
            if line.startswith(";="):
                line = self.markDownHeaders(line[1:],pageNav)
                
            # Handle quick links
            if line.startswith(";") and "[" in line:
                line = self.markDownBraces(line)
                
            # If we are making a list of bullets
            if mode == "bullets":
                if line.startswith(";*"):
                    line = self.markDownContinueBullets(line[1:])
                else:
                    self.markDownEndBullets(bodyLines)
                    mode = "none"
            else:
                if line.startswith(";*"):
                    proc = self.markDownStartBullets(line[1:])
                    mode = "bullets"        
                    bodyLines.append(line)
                    continue
            
            # If we are making a table
            if mode == "table":
                if line.startswith(";||"):
                    line = self.markDownContinueTable(line[1:])
                else:
                    self.markDownEndTable(bodyLines)
                    mode = "none"
            else:
                if line.startswith(";||"):
                    line = self.markDownStartTable(line[1:])
                    mode = "table"
                    bodyLines.append(line)
                    continue
                    
            # If we get here we have a line to add
            bodyLines.append(line)
            
        # All done
        bodyLines.append("</pre>")       
        return bodyLines

if __name__ == "__main__":    
    ch = CodeToHTML()
    ch.translate("../../../content/CoCo/MadnessMinotaur/Code.mark",
                 "../../../deploy/CoCo/MadnessMinotaur/Code.html",
                 "TODO","TODO","TODO")