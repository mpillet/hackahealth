import time
import matplotlib.pyplot as plt
import sys
from pynput.mouse import Button, Controller

import threading
import numpy as np
from scipy import signal
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

if __name__ == "__main__":
    cuttofreq = 0.5
    dt = 1/10
    previousFilterValueX = 0
    previousFilterValueY = 0


    starttime = time.time()
    nb_iter = 0
    new_x , new_y = record()

    filtered_x = 0
    filtered_y = 0 


    while True:

        time.sleep(1/500)
        new_x , new_y = record()

        filtered_x = low_pass(previousFilterValueX, new_x, dt, cuttofreq)
        filtered_y = low_pass(previousFilterValueY, new_y, dt, cuttofreq)

        previousFilterValueX = filtered_x
        previousFilterValueY = filtered_y

        mouse.position =(filtered_x, filtered_y) 
 

