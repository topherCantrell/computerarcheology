import os
import pprint
import shutil

rootDir = "../../content/"
deployDir = "../../deploy/"

def loadDeployFileLines(filename):    
    with open(filename) as f:
        lines = f.readlines()
    ret = []
    for line in lines:
        if ";" in line:
            line = line[0:line.index(";")]
        line = line.strip()
        if len(line)>0:
            ret.append(line)
    return ret

def loadDeployTree(root):
    
    ret = {"dirs":[], "files":[]}
    
    conts = os.listdir(root)
    for c in conts:
        cc = root+c
        if os.path.isfile(cc):
            if c=="deploy.txt":
                ret["deploy"] = loadDeployFileLines(cc)
            else:
                ret["files"].append(c)
        if os.path.isdir(cc):            
            sub = loadDeployTree(cc+"/")
            if sub!=None: 
                ret["dirs"].append(sub)
                
    if not "deploy" in ret:
        return None
            
    pcomps = root[len(rootDir):].split("/")
    if len(pcomps)>1:
        ret = {pcomps[-2]: ret}
    else:
        ret = {pcomps[-1]: ret}         
    
    return ret

def processDeploy(curdir,deploy):    
    lines = deploy['deploy']
    if lines==['*']:
        for f in deploy['files']:
            shutil.copy(rootDir+curdir+"/"+f, deployDir+curdir+"/"+f) 
    else:
        for line in lines:
            i = line.index(' ')
            dst = line[0:i]
            src = line[i+1:].strip()
            #print ":"+dst+":"+src       
            

def makeDeployDirectory(parent,deploy):
    for (key,val) in deploy.iteritems():
        curDeployDir = deployDir + parent + key + "/"
        curContentDir = rootDir + parent + key + "/"        
        os.makedirs(curDeployDir)
        processDeploy(parent+key+"/", val)
        for deps in val['dirs']:
            makeDeployDirectory(parent+key+"/",deps)

def getSiteTreeFiles(deploy):
    if deploy['deploy']==None:
        return []
    ret = []
    for d in deploy['deploy']:
        i = d.index(":")
        fn = d[0:i]
        if "(" in fn:
            i = fn.index("(")
            j = fn.index(")")
            ret.append((fn[0:i].strip(),fn[i+1:j].strip()))
    return ret
            
def getSiteTree(deploy,lines,curDir,curPage):    
    for (key,val) in deploy.iteritems():        
        if key=="css" or key=="js" or key=="img":
            continue
        
        href = curDir+"/"+key
        href = href.replace("//","/")
        
        k = key
        if k=="":
            k="Home"
                
        if curDir==curPage:
            print "::"+curDir+"::"+curPage+"::"
            lnk = k
        else:
            lnk = '<a href="'+href+'" class="sna">'+k+'</a>'
                
        if key=="":
            lines.append('<li class="sn1">'+lnk)
        else:
            lines.append('<li class="snn">'+lnk)
            
        sf = getSiteTreeFiles(val)     
                  
        if len(sf)>0:
            lines.append('<ul>')
            for (targ,name) in sf:
                lines.append('<li class="snn"><a href="'+href+"/"+targ+'" class="sna">'+name+'</a></li>')
            lines.append('</ul>')    
            
        if len(val['dirs'])>0:
            lines.append('<ul>')            
            for d in val['dirs']:
                getSiteTree(d,lines,href,curPage)
            lines.append('</ul>')
        
        lines.append("</li>")

def makeDeployDirectories(deploy):
    if os.path.exists(deployDir):
        shutil.rmtree(deployDir)    
    makeDeployDirectory('',deploy)    

if __name__=="__main__":
    
    d = loadDeployTree(rootDir)
    
    #pprint.pprint(d)
    
    siteLines = []
    siteTree = getSiteTree(d,siteLines,'','')
    siteTreeHTML = "".join(siteLines)
    
    pprint.pprint(siteTreeHTML)
    
    #makeDeployDirectories(d)
