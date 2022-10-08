from pynput.mouse import Listener, Controller
import pyautogui 

tmp_x, tmp_y =  pyautogui.position()
press = False

mouse = Controller()

def on_click(x,y,button, pressed):
    global tmp_x 
    global tmp_y
    global press
    press = pressed
    #if button == mouse.Button.middle : 
    
        #print("Mouse clicked with {0}".format(button))
    #    print (f'{tmp_x} , {tmp_y}')

listener = Listener(on_click=on_click)
listener.start()

while True: 
    if press:
        print(press)
        x,y = pyautogui.position()
        tmp_x = x
        tmp_y = y
    print(tmp_x, tmp_y)
    mouse.position = (tmp_x, tmp_y)







