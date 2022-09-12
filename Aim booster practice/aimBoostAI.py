from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(3)
xs = 580
ys = 470
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

    n = 0
    tarX = [0] * 200 #we assume the number of targetted pixels never exceeds 100
    tarY = [0] * 200
    
    for x in range(0,width,stag): #first we scan the picture and save all of the target coordinates
        for y in range(0,height,stag):

            r,g,b = pic.getpixel((x,y))
            
            if b==195:
                tarX[n] = x+xs
                tarY[n] = y+ys
                n = n+1

            if keyboard.is_pressed('q') == True: #we have to check q every time or else itll take an entire screen analysis to return to while loop
                break
        if keyboard.is_pressed('q') == True:
                break

    n = 0;
    for x in tarX: #then we authorize a click on all targets in a row
        for y in tarY:
            
            if tarX[n]==0:
                break
            if tarY[n]==0:
                break

            if pyautogui.pixel(x,y)[0]>250: #before clicking double check the pixel color
                clickScreen(x,y)
            n = n+1

            if keyboard.is_pressed('q') == True: #we have to check q every time or else itll take an entire screen analysis to return to while loop
                break
        if keyboard.is_pressed('q') == True:
                break




