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
            print ":"+dst+":"+src       
            

def makeDeployDirectory(parent,deploy):
    for (key,val) in deploy.iteritems():
        curDeployDir = deployDir + parent + key + "/"
        curContentDir = rootDir + parent + key + "/"        
        os.makedirs(curDeployDir)
        processDeploy(parent+key+"/", val)
        for deps in val['dirs']:
            makeDeployDirectory(parent+key+"/",deps)
        

def makeDeployDirectories(deploy):
    if os.path.exists(deployDir):
        shutil.rmtree(deployDir)    
    makeDeployDirectory('',deploy)    

if __name__=="__main__":
    
    d = loadDeployTree(rootDir)
    makeDeployDirectories(d)
