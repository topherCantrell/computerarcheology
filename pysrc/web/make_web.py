import shutil
import os
from web.nav_tree import NavTree
from web.id_mgr import IDMgr
import web.ENVIRONMENT as ENV
import web.site_tree

def read_deploy(directory):    
    ret = [['README.md','']]
    with open(directory+'\\README.md', 'r') as f:
        g = ''
        while not g.startswith('>>> deploy:'):        
            g = f.readline()
            if g=='':
                break
        
        while True:
            g = f.readline().strip()
            if g=='':
                break
            if not g.startswith('>>>'):
                break
            g = g[3:].strip()
            if g.endswith('<br>'):
                g = g[0:-4].strip()
            
            if g=='README.md':
                continue
                       
            if ':' in g:
                i = g.index(':')
                t = g[i+1:].strip()
                g = g[0:i].strip()
                if g.endswith('/'):
                    g = g[0:-1]
            else:
                if g.endswith('/'):
                    g = g[0:-1]
                t = g
                if t.endswith('.md'):
                    t = t[0:-3]
            
            ret.append([g,t])
            
    
    return ret

def substitute(lines,tag,value):
    tag = '<!-- %%'+tag+'%% -->'
    for i in range(len(lines)):
        if tag in lines[i]:
            lines[i] = lines[i].replace(tag,value)

def process_markdown(lines,path):
    
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
            page_nav.add_page_nav(level,text,anchor)
            content += '<h{level} id="{anchor}">{text}</h{level}>\n'.format(level=level,anchor=anchor,text=text)
    
        
    
    ret['PAGE_TREE'] = page_nav.to_html()      
    ret['CONTENT'] = content   
    
    # TODO     
    ret['BREAD_CRUMBS'] = 'Crumbs'
    ret['SITE_TREE'] = web.site_tree.make_site_nav(path) # TODO path    
    
    # Some basic error checking
    if ret['IMAGE']=='' or ret['TITLE']=='':
        raise Exception('IMAGE and TITLE are required')
        
    return ret

def deploy_directory(content_current,deploy_current,path):
    deps = read_deploy(content_current)
    for dep in deps:
        print(content_current+' : '+str(dep))
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
                deploy_directory(src,dst,path+'/'+dep)
            else:
                f = open(src,'r')
                cont = f.readlines()
                cont = process_markdown(cont,path)
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

if __name__ == '__main__':
    
    global site_nav
    
    if os.path.isdir(ENV.DEPLOY_DIR):
        shutil.rmtree(ENV.DEPLOY_DIR)
    
    os.makedirs(ENV.DEPLOY_DIR)
    
    deploy_directory(ENV.CONTENT_DIR,ENV.DEPLOY_DIR,'/')