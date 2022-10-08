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

    '''
    sampling_period = 1 / 144
    fs = 1 / sampling_period
    nyq = fs/2
    fc = 5
    Wn = fc/nyq
    b, a = signal.butter(4, Wn, 'low')
    '''
    sample_size = 1000
    nb_iter = 0
    new_x , new_y = record()
    true_x = np.ones((sample_size,))* new_x
    true_y =np.ones((sample_size,))* new_y


    nb_iter = 0 
    start = False
    new_vx = 0
    new_vy = 0
    filtered_vx = np.zeros((sample_size))
    filtered_vy =  np.zeros((sample_size))


    while True:


        time.sleep(sampling_period)
        x = new_x
        y = new_y
        new_x , new_y = record()

        filtered_vx[:-1] = filtered_vx[1:]
        filtered_vx[-1]=new_x - x 
        filtered_vy[:-1] = filtered_vy[1:]
        filtered_vy[-1]=new_y - y


   

        #filtered_vx.append(signal.lfilter(b,a, x_speed)[-1])
        #filtered_vy.append(signal.lfilter(b,a, y_speed)[-1])
        #filtered_vx.append(np.mean(x_speed))
        #filtered_vy.append(np.mean(y_speed))
        #print(x_speed)
        #print(filtered_vx)
    


        mouse.position =(x + np.mean(filtered_vx), y + np.mean(filtered_vy)) 
 

