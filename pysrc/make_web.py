CONTENT_DIR = '..\\content'
DEPLOY_DIR = '..\\deploy'

def read_deploy(directory):
    ret = ['README']
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

print(read_deploy(CONTENT_DIR))
