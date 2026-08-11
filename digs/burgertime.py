
import os

with open('../../content/atari2600/burgertime/burgertime.bin','rb') as f:
    data = f.read()
    
for i in range(8):
    with open('../../content/atari2600/burgertime/btBank'+str(i)+'.bin','wb') as f:
        f.write(data[i*2048:(i+1)*2048])
    
print(len(data))