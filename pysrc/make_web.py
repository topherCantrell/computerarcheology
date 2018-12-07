import shutil
import os
from page_tree import PageTree

CONTENT_DIR = '../content'
DEPLOY_DIR = '../deploy'

def read_deploy(directory):
    ret = ['README.md']
    with open(directory+'\\README.md', 'r') as f:
        g = ''
        while not g.startswith('<!-- deploy'):        
            g = f.readline()
        
        while True:
            g = f.readline().strip()
            if g=='README':
                continue
            if g.startswith('-->'):
                break    
            ret.append(g)
    
    return ret

def substitute(lines,tag,value):
    tag = '<!-- %%'+tag+'%% -->'
    for i in range(len(lines)):
        if tag in lines[i]:
            lines[i] = lines[i].replace(tag,value)

def process_markdown(lines):
        
    page_nav = PageTree()
    
    ret = {}
        
    # Image and Title ... both before the first header
    for g in lines:
        if g.startswith('#'):
            break
        if g.startswith('!['):
            i = g.index('](')
            ret['TITLE'] = g[2:i].strip()            
            j = g.rindex(')')
            ret['IMAGE'] = g[i+2:j].strip()
            if ret['TITLE']=='':
                ret['TITLE'] = ret['IMAGE'][0:ret['IMAGE'].rindex('.')]
            break
        
        
        
        
    # Line by line from the top ... here we go    
    for i in range(len(lines)):
        # Keeping the index in case we have to look backwards
        line = lines[i]
        line_strip = line.strip()
        
        # Build the page tree while we are processing the file
        if(line_strip.startswith('#')):
            page_nav.add_page_nav(line_strip)
    
    
    
          
    
    
    # TODO convert page_tree to HTML
    
    ret['PAGE_TREE'] = page_nav.to_html()          
    
    if ret['IMAGE']=='' or ret['TITLE']=='':
        raise Exception('IMAGE and TITLE are required')
    
    # TODO lots of conversions    
    ret['BREAD_CRUMBS'] = 'Crumbs'
    ret['SITE_TREE'] = 'SiteTree'
    ret['CONTENT'] = 'Content'
        
    return ret

def deploy_directory(content_current,deploy_current):
    deps = read_deploy(content_current)
    for dep in deps:
        print(content_current+' : '+dep)
        if dep.startswith('+'):
            dep = dep[1:].strip()
            src = os.path.join(content_current,dep)
            dst = os.path.join(deploy_current,dep)                        
            if os.path.isdir(src):
                shutil.copytree(src,dst)
            else:
                shutil.copy(src,dst)
        else:
            src = os.path.join(content_current,dep)
            dst = os.path.join(deploy_current,dep)
            if os.path.isdir(src):
                os.makedirs(dst)
                deploy_directory(src,dst)
            else:
                f = open(src,'r')
                cont = f.readlines()
                cont = process_markdown(cont)
                f = open('../content/master.template','r')
                lines = f.readlines()
                f.close()
                substitute(lines,'TITLE',cont['TITLE'])
                substitute(lines,'IMAGE',cont['IMAGE'])
                substitute(lines,'BREAD_CRUMBS',cont['BREAD_CRUMBS'])
                substitute(lines,'SITE_TREE',cont['SITE_TREE'])
                substitute(lines,'PAGE_TREE',cont['PAGE_TREE'])
                substitute(lines,'CONTENT',cont['CONTENT'])                
                if dep=='README.md':
                    dep = 'index.html'
                else:
                    dep = dep[0:-2]+'html'
                f = open(os.path.join(deploy_current,dep),'w+')
                f.writelines(lines)
                f.close()

if __name__ == '__main__':
    
    if os.path.isdir(DEPLOY_DIR):
        shutil.rmtree(DEPLOY_DIR)
    
    os.makedirs(DEPLOY_DIR)
    
    deploy_directory(CONTENT_DIR,DEPLOY_DIR)