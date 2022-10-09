from random import random
from pynput.mouse import Listener, Controller
import pyautogui 
#import mouse
#import pythoncom, pyHook 

mouse = Controller()

tmp_x, tmp_y =  mouse.position
pressed = False

    
def on_click(x,y,button, press):
    global pressed
    pressed = press


def on_move(x,y):
    global tmp_x, tmp_y
    global pressed
    print("pos: ",x, y)
    print(pressed)
    #if button == mouse.Button.middle : 
    if pressed:
        print("pressed")
        tmp_x = x
        tmp_y = y
    print(tmp_x, tmp_y)
    mouse.position = (tmp_x + random()*0.01, tmp_y+random()*0.01)
    #pyautogui.moveTo(tmp_x,tmp_y)

with Listener(
        on_move=on_move,
        on_click=on_click,) as listener:
    listener.join()


