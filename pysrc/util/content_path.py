import os


def get_content_path(name):
    # We assume that "content" is somewhere back up the directory structure
    
    cur_path = os.getcwd()
    
    while True:
        cur = os.listdir(cur_path)
        #print(cur,cur_path)
        if 'content' in cur and os.path.isdir(os.path.join(cur_path,'content')):
            #print('FOUND',cur_path)
            break
        i = cur_path.rfind(os.path.sep)
        #print(i,os.path.sep)
        cur_path = cur_path[0:i]
           
    name = ['content']+name.split('/')
    
    for p in name:
        cur_path = os.path.join(cur_path,p)
        
    return cur_path


if __name__ == '__main__':
    
    s = get_content_path('CoCo/MegaBug/Code.md')
    print(s)