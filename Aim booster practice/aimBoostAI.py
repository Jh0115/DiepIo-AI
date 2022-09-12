from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)
xs = 580
xf = 1325
ys = 470
yf = 968

stag = 15

# screen region: [576,444],[1325,968]
# target B value: 195

def clickScreen(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(xs,ys,749,524))
    width,height = pic.size

    for x in range(0,width,stag): #we scan the entire screenshot
        for y in range(0,height,stag):
            
            r,g,b = pic.getpixel((x,y)) #we save the rgb values
            
            if r==255: #first check the picture
                if pyautogui.pixel((x+xs),(y+ys))[0]==255: #double check the actual screen to save time
                    clickScreen((x+xs+2),(y+ys+2)) #authorize clicking the screen, bias the target by a few pixels to better center on target
                    
            if keyboard.is_pressed('q') == True: #we have to check q every time or else itll take an entire screen analysis to return to while loop
                break
        if keyboard.is_pressed('q') == True:
                break

