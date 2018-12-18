import shutil
import os
from web.nav_tree import NavTree
from web.id_mgr import IDMgr
import web.ENVIRONMENT as ENV
import code.markdown_line
import copy

def substitute(lines,tag,value):
    tag = '<!-- %%'+tag+'%% -->'
    for i in range(len(lines)):
        if tag in lines[i]:
            lines[i] = lines[i].replace(tag,value)

def process_markdown(lines,path,crumb_path):
    
    # TODO the path must be a list like: [ [text,anchor],[text,anchor] ]
    
    #crumbs = path
    
    if crumb_path[-1]=='/':
        crumb_path=crumb_path[0:-1]
    else:
        crumb_path=crumb_path+'.html'
    crumbs = '<li><a>Home</a></li> <li><a>Amiga</a></li> <li><a>What</a></li> <li><a>Now</a></li>'
    print(crumb_path)
           
    # Used to make unique anchor ids on this page    
    ids = IDMgr()
    
    # Used to build the page's navigation tab
    page_nav = NavTree()
    
    # All the different pieces of the page
    ret = {}
    
    # The HTML content of the page
    content = '' 
        
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
            level = 0
            while line[level]=='#':
                level = level + 1                
            text = line[level:].strip()
            anchor = ids.add_id(text)
            page_nav.add_page_nav(level,text,'#'+anchor)
            content += '<h{level} id="{anchor}">{text}</h{level}>\n'.format(level=level,anchor=anchor,text=text)
    
        
    
    ret['PAGE_TREE'] = page_nav.to_html()      
    ret['CONTENT'] = content   
    
    spec_site_nav = copy.deepcopy(site_nav)
    # TODO open path
        
    ret['BREAD_CRUMBS'] = crumbs
    ret['SITE_TREE'] = spec_site_nav.to_html()    
    
    # Some basic error checking
    if ret['IMAGE']=='' or ret['TITLE']=='':
        raise Exception('IMAGE and TITLE are required')
        
    return ret

def deploy_directory(content_current,deploy_current,path):
    
    lines = code.markdown_line.load_file(content_current+'/README.md')
    deps = code.markdown_line.get_deploy(lines)
                
    for dep in deps:
        print(content_current+' : '+str(dep))
        text = dep[1]
        dep = dep[0]
        if dep.startswith('+'):
            # This is just a blind copy -- no processing
            dep = dep[1:].strip()
            src = os.path.join(content_current,dep)
            dst = os.path.join(deploy_current,dep)                        
            if os.path.isdir(src):
                shutil.copytree(src,dst)
            else:
                shutil.copy(src,dst)
        else:
            # This is a markdown file that needs processing
            src = os.path.join(content_current,dep)
            dst = os.path.join(deploy_current,dep)
            if os.path.isdir(src):
                os.makedirs(dst)
                np = path
                if path=='/':
                    np = ''
                deploy_directory(src,dst,np+'/'+dep)
            else:
                f = open(src,'r')
                cont = f.readlines()
                cont = process_markdown(cont,path,path+'/'+text)
                f = open(os.path.join(ENV.CONTENT_DIR,'master.template'),'r')
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

def load_site_directory(d,level,physical_path,tree=None):
    
    if tree==None:
        tree = NavTree()       
        tree.add_page_nav(1,'Home','/')
        
    lines = code.markdown_line.load_file(d+'/README.md')
    info = code.markdown_line.get_deploy(lines)  
    
    for (physical,title) in info:
        if physical=='README.md' or physical.startswith('+'):
            # These do not contribute to navigation
            continue
        if os.path.isdir(os.path.join(d,physical)):
            # This is a directory.
            tree.add_page_nav(level,title,physical_path+'/'+physical)
            load_site_directory(os.path.join(d,physical),level+1,physical_path+'/'+physical,tree)
        else:        
            g = physical.replace('.md','.html')
            tree.add_page_nav(level,title,physical_path+'/'+g)    
            
    return tree

if __name__ == '__main__':
    
    site_nav = load_site_directory(ENV.CONTENT_DIR,1,'')    
    
    if os.path.isdir(ENV.DEPLOY_DIR):
        shutil.rmtree(ENV.DEPLOY_DIR)
    
    os.makedirs(ENV.DEPLOY_DIR)
    
    deploy_directory(ENV.CONTENT_DIR,ENV.DEPLOY_DIR,'/')