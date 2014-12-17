
rootDir = "../../content/"

breadCrumbs = \
    '<li><a href="#">Home</a></li>'\
    '        <li><a href="#">Arcade</a></li>'\
    '        <li class="active">Space Invaders</li>'
    
siteTree = '<li class="sn1"><a class="sna"><strong>Home</strong></a><ul><li class="snn"><a href="/CoCo" class="sna">CoCo</a><ul><li class="snn"><a href="/CoCo/Bedlam" class="sna">Bedlam</a><ul><li class="snn"><a href="/CoCo/Bedlam/Code.html" class="sna">Code</a></li><li class="snn"><a href="/CoCo/Bedlam/RAMTable.html" class="sna">RAM Table</a></li></ul></li><li class="snn"><a href="/CoCo/MadnessMinotaur" class="sna">MadnessMinotaur</a></li></ul></li></ul></li>'

pageTree = \
    '<li class="sn1"><a class="sna">Page Header 1</a>'\
    '            <ul>'\
    '              <li class="snn"><a class="sna">Inner 1</a>'\
    '                <ul>'\
    '                  <li class="snn"><a class="sna">Way In 1</a></li>'\
    '                  <li class="snn"><a class="sna">Way In 2</a></li>'\
    '                </ul>'\
    '              </li>'\
    '              <li class="snn"><a class="sna">Inner 2</a></li>'\
    '            </ul>'\
    '          </li>'\
    '          <li class="sn1"><a class="sna">Header 2</a></li>'
    
def markDownHeaders(bodyLines):    
    for x in xrange(len(bodyLines)):
        line = bodyLines[x]
        
        # = for headers
        if line.startswith("="):
            i = 1
            while(line[i]=='='):
                i=i+1                
            s = line[i:].strip()
            while(s[-1]=='='):
                s = s[0:-1]
            s = "<h"+str(i)+">"+s+"</h"+str(i)+">"
            bodyLines[x] = s
            
def markDownBullets(bodyLines):
    x = 0
    while(x<len(bodyLines)):
        line = bodyLines[x]
        
        if line.startswith(" *"):
            i = x + 1
            while bodyLines[i].startswith(" *"):
                i = i + 1
            s = '<ul><li>' + bodyLines[x][2:] + '</li>'
            bodyLines[x] = s
            x=x+1
            while x<i:
                s = '<li>'+bodyLines[x][2:]+'</li>'
                bodyLines[x]=s
                x=x+1
            bodyLines[x-1] = bodyLines[x-1]+'</ul>'
        
        x=x+1

def markDownTables(bodyLines):
    x = 0
    while(x<len(bodyLines)):    
        line = bodyLines[x]
                
        if line.startswith("||"):     
            i = x+1
            while bodyLines[i].startswith("||"):
                i = i + 1          
            hdrs = bodyLines[x].strip().split("||")[1:-1]  
            s = '<table class="table table-bordered"><thead>'
            for h in hdrs:
                s = s + '<th>'+h.strip()+'</th>'
            s = s + '</tr></thead><tbody>'
            bodyLines[x] = s
            x=x+1
            
            while x<i:                
                tds = bodyLines[x].strip().split("||")[1:-1]
                s = '<tr>'
                for td in tds:
                    s = s + '<td>'+td.strip()+'</td>'
                s = s + '</tr>'
                bodyLines[x] = s                
                x = x + 1
            bodyLines[x-1] = bodyLines[x-1]+'</tbody></table>'                
            
        x = x + 1
        
def markDownBlankLines(bodyLines):
    for x in xrange(len(bodyLines)):
        line = bodyLines[x]
        if line.strip()=='':
            bodyLines[x] = '<p />'
        
def markDownBraces(bodyLines):
    for x in xrange(len(bodyLines)):
        line = bodyLines[x]
        while "[" in line:
            i = line.index("[")
            j = line.index("]",i)
            k = line.index(" ",i)  
            line = line[0:i]+'<a href="'+line[i+1:k].strip()+'">'+line[k+1:j].strip()+'</a>'+line[j+1:]  
        bodyLines[x] = line      
        
    

def markDown(bodyLines):
    markDownBlankLines(bodyLines)
    markDownHeaders(bodyLines)
    markDownTables(bodyLines)
    markDownBraces(bodyLines)
    markDownBullets(bodyLines)
    

def translate(inName, outName, breadCrumbs,siteTree,pageTree):
    
    global rootDir
    
    template = "<!-- %%BODY%% -->" # Default (body-only) template 
    fills = {}                     # Fill-ins dictionary
    bodyLines = []                 # List of lines for the body
    
    # Read the markup
    with open(inName) as f:
        content = f.readlines()   
    
    # Peel the %% fills out of the markup
    for line in content:
        if line.startswith("%%"):
            i = line.index(" ")
            fills[line[2:i]] = line[i+1:].strip()            
        else:
            bodyLines.append(line)
            
    # Process the markdown
    markDown(bodyLines)         
            
    # Page template
    if "template" in fills:
        with open(rootDir+fills["template"]) as f:
            template = f.read()    
            
    # To a single string
    body = "".join(bodyLines)    
            
    # Substitute pieces into the template
    oput = template.replace("<!-- %%TITLE%% -->",fills["title"])
    oput = oput.replace("<!-- %%CONTENT_TITLE%% -->", fills["title"])
    oput = oput.replace("<!-- %%BREAD_CRUMBS%% -->", breadCrumbs)
    oput = oput.replace("<!-- %%PAGE_TREE%% -->", pageTree)
    oput = oput.replace("<!-- %%SITE_TREE%% -->", siteTree)          
    oput = oput.replace("<!-- %%CONTENT%% -->",body)
    
    # Remove any un-filled parts of the template
    while("<!-- %%") in oput:
        i = oput.index("<!-- %%")
        j = oput.index("-->",i)
        oput = oput[0:i]+oput[j+3:]          
   
    # Write the HTML
    with open(outName,'w') as f:
        f.write(oput)    
    
if __name__ == "__main__":
    translate("../../content/index.mark","../../deploy/index.html", breadCrumbs, siteTree, pageTree)