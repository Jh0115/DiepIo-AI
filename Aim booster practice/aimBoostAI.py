from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(3)
xs = 580
ys = 470

# screen region: [576,444],[1325,968]
# target B value: 195

def clickScreen(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(xs,ys,749,524))
    width,height = pic.size

    for x in range(0,width,5):
        for y in range(0,height,5):

            r,g,b = pic.getpixel((x,y))
            
            if r>250 and b>170 and g>150:
                clickScreen((x+xs),(y+ys))
                time.sleep(0.1)

            if keyboard.is_pressed('q') == True: #we have to check q every time or else itll take an entire screen analysis to return to while loop
                break
        if keyboard.is_pressed('q') == True:
                break




