import serial
import time

ser = serial.Serial('COM3',115200)

# aaLL....

def write_byte(d):
    d = bytearray([d])
    #print(d)
    ser.write(d)
    time.sleep(0.01)

with open('../../RC2014/code/echo.bin','rb') as f:
    data = f.read()
    
size = len(data)

write_byte(0x80)
write_byte(0x00)

write_byte(size>>8)
write_byte(size&0xFF)

for d in data:
    write_byte(d)
    
    