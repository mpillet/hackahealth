from pynput.mouse import Controller, Listener
import random
import Quartz

mouse = Controller()

pressed = False
tmp_x, tmp_y = (1, 1)


def on_move(x, y):
    global pressed
    global tmp_x, tmp_y
    print(tmp_x, tmp_y)
    if (pressed):
        mouse.position = (tmp_x + random.random(),
                          tmp_y + random.random())
        return
    else:
        tmp_x, tmp_y = mouse.position
        return


def on_click(x, y, button, press):
    global pressed
    pressed = press


# def intercept(event_type, event):
#     Quartz.CGEventPost(
#         Quartz.kCGHIDEventTap,
#         Quartz.CGEventCreateMouseEvent(
#             None,
#             Quartz.kCGEventMouseMoved,
#             (tmp_x + random.random()*0.01, tmp_y + random.random()*0.01),
#             0))
#     Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
#     return


with Listener(on_move=on_move, on_click=on_click) as listener:
    listener.join()
