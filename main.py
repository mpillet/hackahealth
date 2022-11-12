import time
import sys
from pynput.mouse import Button, Controller, Listener 

import threading
import numpy as np
import socket
import struct

print('Press Ctrl-C to quit.')

mouse = Controller()

def low_pass(previousFilterValue, input, dt, cuttofreq) :
    tau = 1./(2*np.pi*cuttofreq)
    alpha = dt/(tau+dt)
    return alpha*input+(1.-alpha)*previousFilterValue


def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

def record():
    x, y = mouse.position
    return x,y
    
def on_move(new_x, new_y):
    #time.sleep(1/50)
    #new_x , new_y = record()
    global previousFilterValueX
    global previousFilterValueY
    
    cuttofreq = 5
    dt = 1/500
    
    filtered_x = low_pass(previousFilterValueX, new_x, dt, cuttofreq)
    filtered_y = low_pass(previousFilterValueY, new_y, dt, cuttofreq)

    
    previousFilterValueX = filtered_x
    previousFilterValueY = filtered_y
    
    print("Prev: b'" ,int(new_x) , int(new_y) )
#        mouse.position =(filtered_x, filtered_y) 
    buf = str.encode("\n".join([str(int(filtered_x)),str(int(filtered_y))]))
                
    sock.sendto(buf, (UDP_IP,UDP_PORT))
    print('sent:', buf) 
    
def on_click(x,y,osef,pressed):
    if pressed:
        buf = str.encode("!!\nSalut Ian")
        sock.sendto(buf, (UDP_IP,UDP_PORT))
    else:
        buf = str.encode("!!\nAdieu Ian")
        sock.sendto(buf, (UDP_IP,UDP_PORT))
    print(buf)
    return
        
def intercept(event_type, event):
    print(event)
    
    return

if __name__ == "__main__":
    UDP_IP = "192.168.2.1" #Have to edit this according to the new ip of the ian's computer
    UDP_PORT = 9027
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    previousFilterValueX = 0
    previousFilterValueY = 0


    starttime = time.time()
    nb_iter = 0
    new_x , new_y = record()

    filtered_x = 0
    filtered_y = 0 


    #
    #with Listener(suppress=True, on_click=on_click) as listener:
        #listener.join()
    if True:
        listener = Listener(suppress=True, on_click=on_click)
        listener.start()
        
        print('IN')
        while True:
            dt = 1/25
            time.sleep(dt)
            new_x , new_y = record()

            
            cuttofreq = 0.5
            
            
            
            #filtered_x = previousFilterValueX - 0.5*(previousFilterValueX-low_pass(previousFilterValueX, new_x, dt, cuttofreq))
            #filtered_y = previousFilterValueY - 0.5*(previousFilterValueY-low_pass(previousFilterValueY, new_y, dt, cuttofreq))
            
            filtered_x = low_pass(previousFilterValueX, new_x, dt, cuttofreq)
            filtered_y = low_pass(previousFilterValueY, new_y, dt, cuttofreq)
            
            
            previousFilterValueX = filtered_x
            previousFilterValueY = filtered_y
            
            print("Prev: b'" ,int(new_x) , int(new_y) )
        #        mouse.position =(filtered_x, filtered_y) 
            buf = str.encode("\n".join([str(int(filtered_x)),str(int(filtered_y))]))
            #buf = str.encode("\n".join([str(int(new_x)),str(int(new_y))]))            
            sock.sendto(buf, (UDP_IP,UDP_PORT))
            print('sent:', buf) 
 

