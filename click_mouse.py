from pynput.mouse import Listener, Controller
from threading import Thread
import pyautogui 
#import mouse
#import pythoncom, pyHook 

tmp_x, tmp_y =  pyautogui.position()
press = False

mouse = Controller()

def on_click(x,y,button, pressed):
    global tmp_x 
    global tmp_y
    global press
    press = pressed
    print("ON_CLICK")
    #if button == mouse.Button.middle : 
    
        #print("Mouse clicked with {0}".format(button))
    #    print (f'{tmp_x} , {tmp_y}')

def on_move(x,y):
    global tmp_x 
    global tmp_y
    global press
    print("pos: ",x, y)
    print(press)
    if press:
        tmp_x = x
        tmp_y = y
    print(tmp_x, tmp_y)
    mouse.position = (tmp_x, tmp_y)
    #pyautogui.moveTo(tmp_x,tmp_y)
    #mouse.move(1,1)

with Listener(
        on_move=on_move,
        on_click=on_click,) as listener:
    listener.join()


# import pyHook 

# def uMad(event):
#     return False

# hm = pyHook.HookManager()
# hm.MouseAll = uMad
# hm.HookMouse()

