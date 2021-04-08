from tools import format as FORM


source = ('../../content/CoCo/RaakaTu/RaakaTu.bin',0x0600)
target = ('../../content/TRS80/RaakaTu/RAAKA.bin',0x4300)
source_start = 0x1523

#source = ('../../content/CoCo/Bedlam/BEDLAM.bin',0x0600)
#target = ('../../content/TRS80/Bedlam/Bedlam.bin',0x4300)
#source_start = 0x2F24

source_len = 20

with open(source[0],'rb') as f:
    source_data = f.read()
    
with open(target[0],'rb') as f:
    target_data = f.read()
    
sp = source_start-source[1]

dat = source_data[sp:sp+source_len]

i = target_data.index(dat)

print(FORM.shex4(i+0x4300))

while source_data[sp] == target_data[i]:
    sp -= 1
    i -= 1

sp+=1
i+=1
    
source_find_start = sp
target_find_start = i

while source_data[sp] == target_data[i]:
    sp += 1
    i += 1
    
print('Source',hex(source_find_start+source[1]),'to',hex(sp+source[1]),"("+hex(sp-source_find_start)+" bytes)")
print('Target',hex(target_find_start+target[1]),'to',hex(i+target[1]))

#print(hex(i+target[1]))