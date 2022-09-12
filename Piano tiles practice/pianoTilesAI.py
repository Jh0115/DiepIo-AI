from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#tile color [0,0,0]
#tile positions [775,659],[892,659],[1007,659],[1120,659]

dy = 100

def clickScreen(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.005)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(775,659)[0] == 0:
        #do thing
        clickScreen(775,659+dy)
    elif pyautogui.pixel(892,659)[0] == 0:
        #do thing
        clickScreen(892,659+dy)
    elif pyautogui.pixel(1007,659)[0] == 0:
        #do thing
        clickScreen(1007,659+dy)
    elif pyautogui.pixel(1120,659)[0] == 0:
        #do thing
        clickScreen(1120,659+dy)



















