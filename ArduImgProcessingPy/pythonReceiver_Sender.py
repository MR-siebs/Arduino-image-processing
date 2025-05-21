import serial as S
import time as T
from imageProcessing import scan4laser


scan4laser('testDot.jpg')

ardu = S.Serial('COM7', 1000000, timeout=1.1) 

t0 = T.time()

for i in range(0,5):
    number = int(input('number please: '))
    print(f'number: {number.to_bytes(1)}')
    print(f'Sent Bytes:\t{ardu.write(bytes(number.to_bytes(1)))}')
    
    while True:
        if ardu.in_waiting > 0:
            incomingByte = ardu.readline()
            print(int(incomingByte))
            break

ardu.close()

# with S.Serial() as ardu:
#     ardu.baudrate = 9600
#     ardu.port = 'COM7'

#     ardu.open()
#     print(ardu.read()) 
    




