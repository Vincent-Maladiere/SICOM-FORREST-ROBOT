import serial 
import time
 
ser = serial.Serial('/dev/ttyACM0', 9600)
compteur = 0


francis = [ b'\xAA',b'\x00',b'\x08',b'\x0A',b'\x0B',b'\x0C',b'\x0D',b'\xFF']
for i in francis :
       ser.write(i)
       print(ser.readline())
while True :
       print(ser.readline())
