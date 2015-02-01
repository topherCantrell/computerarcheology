
from MarkupToHTML import MarkupToHTML

p1 = '<td><span class="siteTarget" id="%s">%s</span></td>'

class AddressToHTML(MarkupToHTML):   
    
    def markDownStartTable(self,proc):
        hdrs = proc.split("||")[1:-1]  
        if hdrs[0].startswith("="):
            hdrs[0] = hdrs[0][1:].strip()        
            s = '<table class="table table-condensed"><thead><tr>'
            for h in hdrs:
                s = s + '<th>'+h.strip()+'</th>'
            s = s + '</tr></thead>'
        else:
            first = True
            s = '<table class="table table-condensed"><tr>'
            for h in hdrs:
                if first:
                    first = False
                    s = s + p1 % (self.getFirstAddress(hdrs[0]),h.strip())                    
                else:
                    s = s + '<td>'+h.strip()+'</td>'
            s = s + '</tr>' 
        return s
    
    def markDownContinueTable(self,proc):
        cells = proc.split("||")[1:-1]
        s = '<tr>'
        first = True
        for c in cells:
            if first:
                first = False
                s = s + p1 % (self.getFirstAddress(cells[0]),c.strip())
            else:
                s = s + '<td>'+c.strip()+'</td>'
        s = s + '</tr>'
        return s
    
    def getFirstAddress(self,str):
        if ":" in str:
            str = str[0:str.index(":")]
        return str.strip()
    
    def hexInt(self,s):
        s = s.replace("_","")
        return int(s,16)
    
    def loadMap(self,inName):
        
        i = inName.index(" ")
        self.mapFile = inName[0:i]
        self.mapURL = inName[i+1:].strip()
                
        with open(self.mapFile) as f:
            raw = f.readlines()
            
        self.entries = {}
            
        for r in raw:
            line = r.strip()
            if line.startswith("||") and not line[2]=='=':
                entry = {}
                ens = line.split("||")[1:-1]
                e1 = ens[0].strip()
                if ":" in e1:
                    i = e1.index(':')
                    entry["endAddress"] = self.hexInt(e1[i+1:])                    
                    entry["address"] = self.hexInt(e1[0:i])
                    entry["target"] = e1[0:i]
                else:
                    entry["endAddress"] = self.hexInt(e1)                    
                    entry["address"] = self.hexInt(e1,)
                    entry["target"] = e1
                    
                if len(ens)==2:
                    entry["name"]=None
                    entry["description"]=ens[1].strip()
                else:
                    entry["name"]=ens[1].strip()
                    entry["description"]=ens[2].strip()
                self.entries[entry["address"]] = entry
    
    def getEntry(self,address):
        if address in self.entries:
            return self.entries[address] # Most of the time this works
        
        # Might be in a defined area
        for entry in self.entries.values():
            if address>=entry["address"] and address<=entry["endAddress"]:
                return entry
            
        # Nope ... not in this map
        return None     
    
    def getEntryForName(self,name):
        for entry in self.entries.values():
            if entry["name"] == name:
                return entry
                       
                
if __name__ == "__main__":
    ad = AddressToHTML()    
    ad.loadMap("../../../content/CoCo/MadnessMinotaur/RAMUse.mark WOW")
    
    ent = ad.getEntry(0x8A)
    print ent
    
    
        
   