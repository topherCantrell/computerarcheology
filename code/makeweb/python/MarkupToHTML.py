import Deploy
import string
import pprint
    
headers = []
rawMode = None

def makeHeaderLink(text):
    ret = ""
    for t in text:
        if t in string.ascii_letters or t in string.digits:
            ret = ret + t
    if len(ret)==0:
        ret = "header"
    if ret in headers:
        ret = ret +str(len(headers))
    headers.append(ret)
    return ret
        
def markDownHeaders(proc,pageNav):    
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
    
    
    lidLink = makeHeaderLink(lid)
    
    t = '<h'+str(i)+' id="'+lidLink+'">'+s+'</h'+str(i)+'>'
    pageNav.append({'level':i, 'text':lid, 'link':lidLink})
    return t            

def markDownBraces(proc):
    while "[" in proc:
        #print proc
        i = proc.index("[")
        j = proc.index("]",i)
        if " " in proc:
            k = proc.index(" ",i)  
            proc = proc[0:i]+'<a href="'+proc[i+1:k].strip()+'">'+proc[k+1:j].strip()+'</a>'+proc[j+1:]
        else:
            proc = proc[0:i]+'<a href="'+proc[i+1:j].strip()+'">'+proc[i+1:j].strip()+'</a>'+proc[j+1:]  
    return proc   

def markDownStartRaw(proc,bodyLines):
    global rawMode
    if(proc.startswith("{{{html")):
        rawMode = "html"
        return
    bodyLines.append("<pre>")
    rawMode = "pre"
    
def markDownContinueRaw(proc,bodyLines):
    global rawMode
    if proc.startswith("}}}"):
        if rawMode=="pre":
            bodyLines.append("</pre>")
        return True
    
    bodyLines.append(proc+"\n")
    return False

def markDownStartBullets(proc):
    return '<ul><li>'+proc[1:].strip()+'</li>'
def markDownContinueBullets(proc):
    return '<li>'+proc[1:].strip()+'</li>'
def markDownEndBullets(bodyLines):
    bodyLines.append('</ul>')

def markDownStartTable(proc):
    hdrs = proc.split("||")[1:-1]  
    s = '<table class="table table-bordered"><thead><tr>'
    for h in hdrs:
        s = s + '<th>'+h.strip()+'</th>'
    s = s + '</tr></thead><tbody>'
    return s
def markDownContinueTable(proc):
    cells = proc.split("||")[1:-1]
    s = '<tr>'
    for c in cells:
        s = s + '<td>'+c.strip()+'</td>'
    s = s + '</tr>'
    return s
def markDownEndTable(bodyLines):
    bodyLines.append("</tbody></table>")
    

def markDown(raw,fills,pageNav):
    rawMode = "none"
    headers = []
    
    mode = "none"
    bodyLines = []  # List of lines for the body
    for line in raw:        
        proc = line.strip()
        
        # In raw mode, we don't process any markup at all
        if mode == "raw":
            nm = markDownContinueRaw(proc,bodyLines)
            if nm:
                mode = "none"
            continue

        # This is how you get into raw mode
        if proc.startswith("{{{"):
            markDownStartRaw(proc,bodyLines)
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
            proc = markDownHeaders(proc,pageNav)
            
        # Handle quick links
        if "[" in proc:
            proc = markDownBraces(proc)
            
        # If we are making a list of bullets
        if mode == "bullets":
            if proc.startswith("*"):
                proc = markDownContinueBullets(proc)
            else:
                markDownEndBullets(bodyLines)
                mode = "none"
        else:
            if proc.startswith("*"):
                proc = markDownStartBullets(proc)
                mode = "bullets"        
                bodyLines.append(proc)
                continue
        
        # If we are making a table
        if mode == "table":
            if proc.startswith("||"):
                proc = markDownContinueTable(proc)
            else:
                markDownEndTable(bodyLines)
                mode = "none"
        else:
            if proc.startswith("||"):
                proc = markDownStartTable(proc)
                mode = "table"
                bodyLines.append(proc)
                continue
                
        # If we get here we have a line to add
        bodyLines.append(proc)
        
    # All done
    return bodyLines

def makePageNav(pageNav):
    if len(pageNav)<1:
        return ""
    
    # Normalize for pages that start at "2"
    tlev = pageNav[0]["level"]
    if tlev!=1:
        tlev = tlev - 1
        for p in pageNav:
            p["level"]=p["level"] - tlev
    
    pret = [{'level':0}]    
    _makePageNavRecurse(pret,1,0,pageNav)      
    
    #pprint.pprint(pret)
    
    lines = []
    _makePageNavHTMLRecurse(pret[0]['sub'],lines)  
    return "".join(lines)
   
def _makePageNavHTMLRecurse(cur,lines):  
    for c in cur:    
        cl = "n"
        if c["level"]==1:
            cl = "1"
        lines.append('<li class="sn'+cl+'"><a class="sna" onclick="pageScrollTo(\''+c["link"]+'\');return false;">'+c["text"]+'</a>')                   
        if 'sub' in c:            
            lines.append('<ul>')
            _makePageNavHTMLRecurse(c['sub'],lines)
            lines.append('</ul>')
        lines.append('</li>')

def _makePageNavRecurse(parent,lev,pos,pageNav):
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
        pos = _makePageNavRecurse(ret,lev+1,pos,pageNav)    
    
def translate(inName, outName, breadCrumbs,siteTree):
    
    template = "<!-- %%BODY%% -->"    # Default (body-only) template 
    fills = {}                        # Fill-ins dictionary (with defaults)
    pageNav = []
        
    # Read the markup
    with open(inName) as f:
        raw = f.readlines()   
    
    # Process the mark down on the content
    bodyLines = markDown(raw,fills,pageNav) 
                    
    # Page template
    if "template" in fills:
        with open(Deploy.rootDir+fills["template"]) as f:
            template = f.read()    
        
    im = ""    
    if "image" in fills:
        im = '<img src="/img/'+fills["image"] +'" height="90" style="PADDING-LEFT: 40px"/>'
            
    # To a single string
    body = "".join(bodyLines)
    #body = "TESTING"
        
    pageTree = makePageNav(pageNav)    
            
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
    
    translate("../../../content/CoCo/MadnessMinotaur/Madness.mark","../../../deploy/CoCo/MadnessMinotaur/index.html", breadCrumbs, siteTree)