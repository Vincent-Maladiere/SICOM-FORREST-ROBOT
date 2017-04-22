import sys
sys.path[0] = sys.path[0].replace('/test/comm','')
import serial 
import time
 
ser = serial.Serial('/dev/ttyACM0', 9600)
ser.timeout=3
print(ser.is_open)
francis = [ b'\xAA',b'\x00',b'\x08',b'\x0A',b'\x0B',b'\x0C',b'\x0D',b'\xFF']
    
time.sleep(10)
for i in francis :
       ser.write(i)
       print(ser.readline())

while True :
       print(ser.readline())
