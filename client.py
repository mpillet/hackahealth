import socket
import time 
import struct
from pynput.mouse import Button, Controller

mouse = Controller()
UDP_IP = "0.0.0.0" #fix

UDP_PORT = 9027

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(2048) # buffer size is 1024 bytes
    x,y = data.decode().split('\n')

    if x !="!!":
        mouse.position =(int(x),int(y)) 

    else:
        if y =="Salut Ian":
            mouse.press(Button.left)
        elif y=="Adieu Ian": 
            mouse.release(Button.left)



    
    
    #struct.unpack('>6s1I2B1I1B7x3f', data) #to unpack when it is center of mass sent
    
    #struct.unpack('>6sI2BIB7x440x', ja) # with all joint angles, need to replace 440x  by 2I3f 22 times