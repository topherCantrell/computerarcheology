import os
import pprint
import shutil

rootDir = "../../../content/"
deployDir = "../../../deploy/"

def loadDeployFileLines(filename):   
    """Load the 'deploy.tx' lines
    
    This method loads the lines from a file and trims out any
    comments and blank lines.
    
    Args:
        filename (string): the name of the file to load
      
    Returns:
        list of lines
    """
    
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

def loadContentTree(root):
    """Load all content information
    
    This function loads the content information from the given directory
    and all subdirectories. Only directories with a 'deploy.txt' are 
    included.
    
    Args:
        root (string): directory path
        
    Returns:
        dictionary/tree data structure for all subdirectories
    """
    
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
            sub = loadContentTree(cc+"/")
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

def makeDeployDirectories(content):
    """Remove and recreate the entire deployment directory
    
    Args:
        content (dictionary): the root content
        
    """
    if os.path.exists(deployDir):
        shutil.rmtree(deployDir)    
    makeDeployDirectory('',content) 
    
def makeDeployDirectory(parent,content):
    """Create deploy directory structure
    
    This recursive method creates the directories and subdirectories for all 
    entries in the deploy information
    
    Args:
        parent (string): the parent directory
        deploy (dictionary): the deployment info for the given directory
        
    """
    for (key,val) in content.iteritems():
        curDeployDir = deployDir + parent + key + "/"
        curContentDir = rootDir + parent + key + "/"        
        os.makedirs(curDeployDir)
        processDeploy(parent+key+"/", val)
        for deps in val['dirs']:
            makeDeployDirectory(parent+key+"/",deps)

def processDeploy(curdir,deploy):   
    """Process a single deploy.txt file
    
    This processes all the lines from the given deploy.txt info. This
    creates files in the target deploy directory.
    
    Args:
        curdir (string): the current directory path off of the root
        deploy (list): list of lines from deploy.txt
        
    """
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

def getBreadCrumbs(curPage):
    """Get HTML bread-crumbs for page
    
    This method returns the HTML lines for the bread-crumbs to the given page.
    
    Args:
        curPage : the path to the desired page
        
        
    Returns:
        (string) the HTML for the bread-crumbs
        
    """ 
    lnks = curPage.split("/")
    ret = ''
    curdir = ''
    for lnk in lnks[0:-1]:
        curdir=curdir+lnk+"/"
        l = lnk
        if l=="":
            l = "Home"
        ret = ret + '<li><a href="'+curdir+'">'+l+'</a></li>'
    ret = ret + '<li><a class="active">'+lnks[-1]+'</li>'
    return ret
            
def getSiteNav(content,lines,curDir,curPage):
    """Returns the site-tree for a given page
    
    This method returns the HTML for the site-tree for a given
    page in the content hierarchy.
    
    Args:
        content (string): the content info for the current directory
        lines (list): the growing list of lines to write to
        curDir (string): the current directory (this is recursive)
        curPage (string): the page this navigation is for (affects 'active' in the tree)
        
    Returns:
        list of HTML lines
        
    """
    
    # TODO: This doesn't handle the 'curPage' correctly
    
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



if __name__=="__main__":
    
    d = loadContentTree(rootDir)
    
    #pprint.pprint(d)
    
    siteLines = []
    siteTree = getSiteNav(d,siteLines,'','')
    siteTreeHTML = "".join(siteLines)
    
    crumbs = getBreadCrumbs('/CoCo/Bedlam/Code')
    print crumbs
    
    #pprint.pprint(siteTreeHTML)
    
    #makeDeployDirectories(d)
