
class TextLine(object):
    
    def __init__(self,text,fileName="INTERNAL",lineNumber=0):
        self.original = text
        self.text = text
        self.fileName = fileName
        self.lineNumber = lineNumber