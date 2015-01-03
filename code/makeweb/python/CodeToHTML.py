from CodeLine import CodeLine

from AddressToHTML import AddressToHTML
from MarkupToHTML import MarkupToHTML

from Config import rootDir
from Config import deployDir

# {% means append the link to the opcode. Without means replace the number.
# : means alternate text for destination
# Now we can look up labels, but allow for manual labels
#0001: C2 4D 00        JP      NZ,$004D            ; {goHere} Replace the jump address with the known routine name
#0002: C2 4D 00        JP      NZ,$004D            ; {goHere:GOHERE} Jump to the named routine, but use different text in the link
#0003: C2 50 00        JP      NZ,$0050            ; {} The address $0050 is named with its address
#0004: E9              JP      (HL)                ; {goHere} I know we are going to routine "goHere"
#0005: C2 4D 00        JP      NZ,$004D            ; {%goHere:HERE} Just add the link next to the opcode
#0006: C2 4D 00        JP      NZ,$004D            ; {%//wiki/wiki/NES/Zelda:SEE ZELDA} Quick link to another page

# RAM reference
# 0042: 3A E9 20        LD      A,($20E9)          ; {-suspendPlay:} Are we moving ...

# Link to hardware definition. Can be shortened to {--}
# E57A: 8D 00 20      STA   $2000                  ; {--_P_CNTRL_1:} ... VBLANK NMIs

# {-} and {--} link names are given in the defines

# {%--goHere:altText}

class CodeToHTML(MarkupToHTML):
    
    def getAddressMap(self,filename):
        ad = AddressToHTML()
        ad.loadMap(rootDir+filename)
        return ad
    
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
            if not line.target["target"]=="": # and only if we need to lookup the address
                continue            
            
            for x in xrange(len(lines)):
                g = lines[x]
                if isinstance(g,CodeLine) and g.address==line.numbers[0]["value"]:                    
                    g.linkID = line.numbers[0]["text"][1:]
                    # This line of code might also have a preceding label. Let's look for that.
                    y = x-1
                    while y>=0:
                        if not isinstance(lines[y],CodeLine):
                            y = y - 1
                            continue
                        if lines[y].labels:
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
                tar = ad.mapURL+"#"+line.numbers[0]["text"][1:]
                aClass = "ramAddressLink"
        elif line.target["map"]=="hardware":
            if tar=="":
                ad = maps["hardwareMap"]
                entry = ad.getEntry(line.numbers[0]["value"])
                if txt=="":
                    txt = entry["name"]
                tar = ad.mapURL+"#"+line.numbers[0]["text"][1:]
                aClass = "hardwareAddressLink"                     
        else:
            if tar=="":
                tar = line.numbers[0]["text"][1:]
            if not "/" in tar:
                tar = "#" + tar
            if txt=="":
                txt = line.numbers[0]["text"]
                
        rep = '<a class="'+aClass+'" href="'+tar+'" title="'+line.numbers[0]["text"]+'">'+txt+"</a>"
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
                line.original = '<span class="siteTarget" id="'+line.linkID+'">'+line.original[0]+'</span>'+line.original[1:] 
                
                
    def translate(self, inName, outName, breadCrumbs, siteTree, title):
        # Read the code
        with open(inName) as f:
            raw = f.readlines()
            
        maps = {}
        ret = []
        for r in raw:                        
                        
            t = r.strip() 
                           
            if t.startswith(";%%ramMap"):
                maps["ramMap"] = self.getAddressMap(t[9:].strip()) #;%%ramMap RAMUse.mark 
                continue
            elif t.startswith(";%%hardwareMap"):
                maps["hardwareMap"] = self.getAddressMap(t[14:].strip()) #;%%hardwareMap /Coco/Hardware.mark
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
            #if "[" in line:
            #    line = self.markDownBraces(line)
                
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