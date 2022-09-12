from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(5)

# screen region: [576,444],[1325,968]
# target B value: 195


def clickScreen(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(576,444,749,524))
    width,height = pic.size

    for x in range(0,width,5):
        for y in range(0,height,5):
            if pic.getpixel((x,y))[2]==195:
                clickScreen((x+576),(y+444))
                time.sleep(0.05)




