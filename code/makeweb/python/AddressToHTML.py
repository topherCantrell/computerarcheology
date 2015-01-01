
from MarkupToHTML import MarkupToHTML

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
            s = '<table class="table table-condensed"><tr id="'+self.getFirstAddress(hdrs[0])+'">'
            for h in hdrs:
                s = s + '<td>'+h.strip()+'</td>'
            s = s + '</tr>' 
        return s
    
    def markDownContinueTable(self,proc):
        cells = proc.split("||")[1:-1]
        s = '<tr id="'+self.getFirstAddress(cells[0])+'">'
        for c in cells:
            s = s + '<td>'+c.strip()+'</td>'
        s = s + '</tr>'
        return s
    
    def getFirstAddress(self,str):
        if ":" in str:
            str = str[0:str.index(":")]
        return str.strip()
    
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
                    entry["endAddress"] = int(e1[i+1:],16)                    
                    entry["address"] = int(e1[0:i],16)
                else:
                    entry["endAddress"] = int(e1,16)                    
                    entry["address"] = int(e1,16)
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
                       
                
if __name__ == "__main__":
    ad = AddressToHTML()    
    ad.loadMap("../../../content/CoCo/MadnessMinotaur/RAMUse.mark")
        
   