import string
import pprint

from Config import rootDir
from Config import deployDir

class MarkupToHTML:
    
    def __init__(self):
        self.headers = []
        self.rawMode = None

    def makeHeaderLink(self,text):
        ret = ""
        for t in text:
            if t in string.ascii_letters or t in string.digits:
                ret = ret + t
        if len(ret)==0:
            ret = "header"
        if ret in self.headers:
            ret = ret +str(len(headers))
        self.headers.append(ret)
        return ret
            
    def markDownHeaders(self,proc,pageNav):    
        i = 1
        while(proc[i]=='='):
            i=i+1                
        s = proc[i:].strip()
        
        lid = None
        j = s.rindex('=')
        if j!=(len(s)-1) and (j!=i):
            lid = s[j+1:].strip()
            s = s[0:j+1]
        
        while(s[-1]=='='):
            s = s[0:-1]
            
        if lid == None:
            lid = s     
        
        lidLink = self.makeHeaderLink(lid)
        
        t = '<h'+str(i)+' id="'+lidLink+'">'+s+'</h'+str(i)+'>'
        pageNav.append({'level':i, 'text':lid, 'link':lidLink})
        return t            
    
    def markDownBraces(self,proc):
        while "[" in proc:
            #print proc
            i = proc.index("[")
            ii=i
            j = proc.index("]",i)
            tag = "a"
            attr = "href"
            if proc[i+1]=='!':
                tag = "img"
                attr = "src"
                ii = i + 1
            if " " in proc:
                k = proc.index(" ",i)  
                proc = proc[0:i]+'<'+tag+" "+attr+'="'+proc[ii+1:k].strip()+'">'+proc[k+1:j].strip()+'</'+tag+'>'+proc[j+1:]
            else:
                proc = proc[0:i]+'<'+tag+" "+attr+'="'+proc[ii+1:j].strip()+'">'+proc[ii+1:j].strip()+'</'+tag+'>'+proc[j+1:]  
        return proc   
    
    def markDownStartRaw(self,proc,bodyLines):
        if proc.startswith("{{{code"):
            self.rawMode = "pre"
            bodyLines.append('<pre class="codePreStyle">')
            self.rawMode = "pre"
            return
        
        if proc.startswith("{{{html"):
            self.rawMode = "html"
            return
        
        bodyLines.append("<pre>")
        self.rawMode = "pre"
        
    def markDownContinueRaw(self,proc,bodyLines):
        if proc.startswith("}}}") or proc.startswith(";}}}"):
            if self.rawMode=="pre":
                bodyLines.append("</pre>")
            return True
        
        bodyLines.append(proc+"\n")
        return False
    
    def markDownStartBullets(self,proc):
        return '<ul><li>'+proc[1:].strip()+'</li>'
    def markDownContinueBullets(self,proc):
        return '<li>'+proc[1:].strip()+'</li>'
    def markDownEndBullets(self,bodyLines):
        bodyLines.append('</ul>')
    
    def markDownStartTable(self,proc):
        hdrs = proc.split("||")[1:-1]  
        if hdrs[0].startswith("="):
            hdrs[0] = hdrs[0][1:].strip()        
            s = '<table class="table table-condensed"><thead><tr>'
            for h in hdrs:
                s = s + '<th>'+h.strip()+'</th>'
            s = s + '</tr></thead>'
        else:
            s = '<table class="table table-condensed"><tr>'
            for h in hdrs:
                s = s + '<td>'+h.strip()+'</td>'
            s = s + '</tr>' 
        return s
    def markDownContinueTable(self,proc):
        cells = proc.split("||")[1:-1]
        s = '<tr>'
        for c in cells:
            s = s + '<td>'+c.strip()+'</td>'
        s = s + '</tr>'
        return s
    def markDownEndTable(self,bodyLines):
        bodyLines.append("</table>")
        
    
    def markDown(self,raw,fills,pageNav):
        self.rawMode = None
        self.headers = []
        
        mode = "none"
        
        bodyLines = []  # List of lines for the body
        for line in raw:        
            proc = line.strip()
            
            # In raw mode, we don't process any markup at all
            if mode == "raw":
                nm = self.markDownContinueRaw(proc,bodyLines)
                if nm:
                    mode = "none"
                continue
            
            # In case we are in a code file
            if proc.startswith(";"):
                proc = proc[1:]
    
            # This is how you get into raw mode
            if proc.startswith("{{{"):
                self.markDownStartRaw(proc,bodyLines)
                mode = "raw"
                continue    
            
            # -- Markup Processing --          
            
            # Handle defines
            if proc.startswith("%%"):
                i = proc.index(" ")
                fills[proc[2:i]] = proc[i+1:].strip()
                continue
                        
            # Handle line breaks
            proc = proc.replace("[[br]]","<br>")
            
            # Handle paragraph breaks
            if proc=="":
                proc = '<p />'
                
            # Handle quick headers
            if proc.startswith("="):
                proc = self.markDownHeaders(proc,pageNav)
                
            # Handle quick links
            if "[" in proc:
                proc = self.markDownBraces(proc)
                
            # If we are making a list of bullets
            if mode == "bullets":
                if proc.startswith("*"):
                    proc = self.markDownContinueBullets(proc)
                else:
                    self.markDownEndBullets(bodyLines)
                    mode = "none"
            else:
                if proc.startswith("*"):
                    proc = self.markDownStartBullets(proc)
                    mode = "bullets"        
                    bodyLines.append(proc)
                    continue
            
            # If we are making a table
            if mode == "table":
                if proc.startswith("||"):
                    proc = self.markDownContinueTable(proc)
                else:
                    self.markDownEndTable(bodyLines)
                    mode = "none"
            else:
                if proc.startswith("||"):
                    proc = self.markDownStartTable(proc)
                    mode = "table"
                    bodyLines.append(proc)
                    continue
                    
            # If we get here we have a line to add
            bodyLines.append(proc+" ")
            
        # All done
        return bodyLines
    
    def makePageNav(self,pageNav):
        if len(pageNav)<1:
            return ""
        
        # Normalize for pages that start at "2"
        tlev = pageNav[0]["level"]
        if tlev!=1:
            tlev = tlev - 1
            for p in pageNav:
                p["level"]=p["level"] - tlev
        
        pret = [{'level':0}]    
        self._makePageNavRecurse(pret,1,0,pageNav)      
        
        #pprint.pprint(pret)
        
        lines = []
        self._makePageNavHTMLRecurse(pret[0]['sub'],lines)  
        return "".join(lines)
       
    def _makePageNavHTMLRecurse(self,cur,lines):  
        for c in cur:    
            cl = "n"
            if c["level"]==1:
                cl = "1"
            lines.append('<li class="sn'+cl+'"><a class="sna" onclick="pageScrollTo(\''+c["link"]+'\');return false;">'+c["text"]+'</a>')                   
            if 'sub' in c:            
                lines.append('<ul>')
                self._makePageNavHTMLRecurse(c['sub'],lines)
                lines.append('</ul>')
            lines.append('</li>')
    
    def _makePageNavRecurse(self,parent,lev,pos,pageNav):
        ret = []
        while True:
            if pos==len(pageNav) or pageNav[pos]["level"]<lev:
                parent[len(parent)-1]["sub"] = ret
                return pos        
            if pageNav[pos]["level"]==lev:
                ret.append(pageNav[pos])
                pos = pos + 1
                continue
            if pageNav[pos]["level"]!=(lev+1):
                raise Exception("Missing header level")
            pos = self._makePageNavRecurse(ret,lev+1,pos,pageNav)    
        
    def translate(self, inName, outName, breadCrumbs, siteTree, title, raw=None):
        
        template = "<!-- %%BODY%% -->"           # Default (body-only) template 
        fills = {"template":"master.template", "title":title}   # Fill-ins dictionary (with defaults)
        pageNav = []
            
        # Read the markup (if it wasn't passed in)
        if raw==None:
            with open(inName) as f:
                raw = f.readlines()   
        
        # Process the mark down on the content
        bodyLines = self.markDown(raw,fills,pageNav) 
                        
        # Page template
        if "template" in fills:
            with open(rootDir+fills["template"]) as f:
                template = f.read()    
            
        im = ""    
        if "image" in fills:
            im = '<img src="'+fills["image"] +'" height="90" style="PADDING-LEFT: 40px"/>'
                
        # To a single string
        body = "".join(bodyLines)
        #body = "TESTING"
            
        pageTree = self.makePageNav(pageNav)    
                
        # Substitute pieces into the template
        oput = template.replace("<!-- %%TITLE%% -->",fills["title"])
        oput = oput.replace("<!-- %%CONTENT_TITLE%% -->", fills["title"])
        oput = oput.replace("<!-- %%BREAD_CRUMBS%% -->", breadCrumbs)
        oput = oput.replace("<!-- %%PAGE_TREE%% -->", pageTree)
        oput = oput.replace("<!-- %%SITE_TREE%% -->", siteTree)          
        oput = oput.replace("<!-- %%CONTENT%% -->",body)
        oput = oput.replace("<!-- %%IMAGE%% -->",im)
            
        # Remove any un-filled parts of the template
        while("<!-- %%") in oput:
            i = oput.index("<!-- %%")
            j = oput.index("-->",i)
            oput = oput[0:i]+oput[j+3:]          
       
        # Write the HTML
        with open(outName,'w') as f:
            f.write(oput)    
    
if __name__ == "__main__":
    
    mu = MarkupToHTML()
    
    breadCrumbs = '<li class="active"><strong>Home</strong></li>'
    
    siteTree = '<li class="sn1"><strong>Home</strong></li>'

    pageTree = \
        '<li class="sn1"><a class="sna">Page Header 1</a>'\
        '  <ul>'\
        '    <li class="snn"><a class="sna">Inner 1</a>'\
        '      <ul>'\
        '        <li class="snn"><a class="sna">Way In 1</a></li>'\
        '        <li class="snn"><a class="sna">Way In 2</a></li>'\
        '      </ul>'\
        '    </li>'\
        '    <li class="snn"><a class="sna">Inner 2</a></li>'\
        '  </ul>'\
        '</li>'    
    
    mu.translate("../../../content/CoCo/MadnessMinotaur/Madness.mark","../../../deploy/CoCo/MadnessMinotaur/index.html", breadCrumbs, siteTree)