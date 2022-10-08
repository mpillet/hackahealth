import time
import matplotlib.pyplot as plt
import sys
from pynput.mouse import Button, Controller

import threading
import numpy as np
from scipy import signal
print('Press Ctrl-C to quit.')

mouse = Controller()


def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

def record():
    x, y = mouse.position
    return x,y

if __name__ == "__main__":
    sampling_period = 1 / 144
    fs = 1 / sampling_period
    nyq = fs/2
    fc = 5
    Wn = fc/nyq
    b, a = signal.butter(4, Wn, 'low')

    starttime = time.time()
    nb_iter = 0
    new_x , new_y = record()
    true_x =[new_x]
    true_y = [new_y]
    filtered_x = []
    filtered_y = []     


    nb_iter = 0 
    start = False
    new_vx = 0
    new_vy = 0
    x_speed = []
    y_speed = [] 
    filtered_vx = []
    filtered_vy = []


    while True:

        time.sleep(sampling_period)
        if nb_iter >= 300:
            start = True
            x_speed.pop(0)
            y_speed.pop(0)
            filtered_vx.pop(0)
            filtered_vy.pop(0)
        x = true_x[-1]
        y = true_y[-1]
        new_x , new_y = record()
        new_vx = new_x - x
        new_vy = new_y - y

        x_speed.append(new_vx)
        y_speed.append(new_vy)

   

        if nb_iter >= 150 :
            #filtered_vx.append(signal.lfilter(b,a, x_speed)[-1])
            #filtered_vy.append(signal.lfilter(b,a, y_speed)[-1])
            filtered_vx.append(np.mean(x_speed))
            filtered_vy.append(np.mean(y_speed))
        #print(x_speed)
        #print(filtered_vx)
        if start:
    
  
            true_x.append(x + filtered_vx[-1])
            true_y.append(y + filtered_vy[-1])

            mouse.position =(true_x[-1], true_y[-1]) 
 
        nb_iter += 1

