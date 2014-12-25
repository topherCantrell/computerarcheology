import os
import pprint
import shutil
import json

import MarkupToHTML

rootDir = "../../../content/"
deployDir = "../../../deploy/"

def _loadContentTreeRecurse(parent,path,displayName):
    # This recursive helper function loads and "deploy.json" file
    # from the "path" and appends the information to the the
    # "parent" dirs. This "path" is given the "displayName".
            
    ret = {} # Base object to append for this directory "path"
               
    if not os.path.isfile(path+"deploy.json"):
        return # Noting in this directory
    
    parent["dirs"].append(ret) # Add us to the parent
        
    # Load the JSON object
    with open(path+"deploy.json") as f:
        obj = json.load(f)
        ret["deploy"] = obj
        
    # Some basics
    ret["dirs"] = []    
    ret["dirPath"] = path[len(rootDir):]
    ret["displayPath"] = parent["displayPath"]+"/"+displayName
     
    # Run any "dirList" and append those recursively
    if "dirList" in obj:       
        for dpath in obj["dirList"]:
            _loadContentTreeRecurse(ret,path+dpath["dirName"]+"/",dpath["displayName"])    

def loadContentTree():
    """Load all content information
    
    This function loads the content information from the given directory
    and all subdirectories. Only directories with a 'deploy.json' are 
    included.    
    
    Returns:
        The tree object
    
    """
    
    root = rootDir
    parent = {'displayPath':'', 'dirPath':'', 'dirs':[]}
    
    _loadContentTreeRecurse(parent,root,"Home")
    
    return parent["dirs"][0]       

def makeDeployDirectories(content):
    """Remove and recreate the entire deployment directory
    
    Args:
        content (dictionary): the root content
        
    """
    if os.path.exists(deployDir):
        shutil.rmtree(deployDir)    
    _makeDeployDirectory(content["dirs"]) 
    
def _makeDeployDirectory(contentDirs):
    # Recursive function to create directories and subdirectories   
    
    for dinfo in contentDirs:
        os.makedirs(deployDir+dinfo["dirPath"])
        _makeDeployDirectory(dinfo["dirs"])
        
def processDeploys(rootContent,content):   
    """Process a tree of deploy.json commands
    
    This processes all the lines from the given deploy.json info. This
    creates files in the target deploy directory and subdirectories
    
    Args:
        content (content object): the content directory object
        
    """
    lines = content['deploy']['files']
    if lines==['*']:
        for f in os.listdir(rootDir+content["dirPath"]):
            if (os.path.isfile(rootDir+content["dirPath"]+f)) and (f != "deploy.json"):    
                shutil.copy(rootDir+content["dirPath"]+f, deployDir+content["dirPath"]+f)        
             
    else:
        for line in lines:
           coms = line["command"].strip().split(" ")
           if coms[0] == "markup":                
               n = line["displayName"]
               if n == "":
                   n = None
               breadCrumbs = getBreadCrumbs(content,n)
               siteNav = getSiteNav(rootContent,content,n)
                              
               MarkupToHTML.translate(rootDir+content["dirPath"]+coms[1], 
                                      deployDir+content["dirPath"]+line["outputName"], 
                                      breadCrumbs,siteNav)               
                           
           else:
               raise Exception("Unknown command:"+line["command"])
            #print "#"+str(line)+"#"
            #i = line.index(' ')
            #dst = line[0:i]
            #src = line[i+1:].strip()
            #print ":"+dst+":"+src  
            #def translate(inName, outName, breadCrumbs,siteTree,pageTree):
    
    for d in content["dirs"]:
        processDeploys(rootContent,d)        
         

def getSiteTreeFiles(content):
    """Get list of files to be deployed
    
    This method reads the list of files to be deployed from the 'deploy.txt'
    file. The file lists both the display-name and deployed-file-name for
    each file.
    
    Args:
        deploy (dictionary): the content information
        
    Returns:
        list of (file,name) tuples
        
    """
    
    if content['deploy']==None:
        return []
    ret = []
    for d in content['deploy']:
        i = d.index(":")
        fn = d[0:i]
        if "(" in fn:
            i = fn.index("(")
            j = fn.index(")")
            ret.append((fn[0:i].strip(),fn[i+1:j].strip()))
    return ret

def getBreadCrumbs(content,fname=None):
    """Get HTML bread-crumbs for page
    
    This method returns the HTML lines for the bread-crumbs to the given page.
    
    Args:
        content : the desired directory content object        
        
    Returns:
        (string) the HTML for the bread-crumbs
        
    """
    
    pathLinks = ["/"] + content["dirPath"].split("/")[0:-1]
    dispLinks = content["displayPath"].split("/")[1:]
    
    fo = None
    if fname!=None:
        for fi in content["deploy"]["files"]:
            if fi["displayName"]==fname:
                fo = fi
                break
        pathLinks = pathLinks + [fi["outputName"]]
        dispLinks = dispLinks + [fi["displayName"]]
    
    ret = ''
    for x in xrange(len(pathLinks)-1):
        href = "/"+"/".join(pathLinks[1:x+1])
        ret = ret + '<li><a href="'+href+'">'+dispLinks[x]+'</a></li>'
    ret = ret + '<li class="active"><strong>'+dispLinks[-1]+'</strong></li>'
    
    return ret
   
def getSiteNav(content,curContent,fname=None):
    lines = []
    _getSiteNav(content,lines,curContent,fname)
    return "".join(lines)
    
            
def _getSiteNav(content,lines,curContent,fname):
        
    # TODO: This doesn't handle the 'curPage' correctly
    
    sn = "snn"
    href = "/"+content["dirPath"]
    if href=="/":
        sn = "sn1"       
    
    dispLinks = content["displayPath"].split("/")[1:]   
        
    if curContent == content and fname==None:
        lines.append('<li class="'+sn+'"><span class="sna"><strong>'+dispLinks[-1]+"</strong></span>")
    else:        
        lines.append('<li class="'+sn+'"><a class="sna" href="'+href+'">'+dispLinks[-1]+'</a>')        
        
    if len(content["deploy"]["files"])>0:
        ifs = content["deploy"]["files"][1:]
        if len(ifs)>0:
            lines.append("<ul>")
            for fi in ifs:
                if curContent == content and fname==fi['displayName']:
                    lines.append('<li class="'+sn+'"><span class="sna"><strong>'+fi["displayName"]+"</strong></span>")
                else:
                    lines.append('<li class="'+sn+'"><a class="sna" href="'+href+fi["outputName"]+'">'+fi["displayName"]+'</a>')                    
            lines.append("</ul>")
    
    if len(content["dirs"])>0:
        lines.append("<ul>")
        for sub in content["dirs"]:
            if sub["displayPath"][-1]!='*':
                _getSiteNav(sub,lines,curContent,fname)
        lines.append("</ul>")
    lines.append('</li>')
    
    """
    for (key,val) in content.iteritems():        
        if key=="css" or key=="js" or key=="img":
            continue
        
        href = curDir+"/"+key
        href = href.replace("//","/")
        
        k = key
        if k=="":
            k="Home"
                
        if curDir==curPage:
            #print "::"+curDir+"::"+curPage+"::"
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
                getSiteNav(d,lines,href,curPage)
            lines.append('</ul>')
        
        lines.append("</li>")
"""


if __name__=="__main__":
    
    d = loadContentTree()
    #pprint.pprint(d)
    makeDeployDirectories(d)
    processDeploys(d,d)
    
    crumbs = getBreadCrumbs(d)
    #print "'"+crumbs+"'"
    
    nav = getSiteNav(d,d)
    #print "'"+nav+"'"
    
    
    #siteLines = []
    #siteTree = getSiteNav(d,siteLines,'','')
    #siteTreeHTML = "".join(siteLines)
    
    
    
    #pprint.pprint(siteTreeHTML)
    
    
