from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Targets are pentagons, triangles, and squares
#pentagons: [118,141,252]
#triangles: [252,118,119]
#squares: [255,232,105]

time.sleep(5)

while keyboard.is_pressed('q') == False:
    loop_flag = True
    
    point = pyautogui.locateCenterOnScreen('pentagon.png',confidence=0.5)
    if point!=(None):
        win32api.SetCursorPos((point[0],point[1]))
        loop_flag = False
        
    point = pyautogui.locateCenterOnScreen('triangle.png',confidence=0.5)
    if point!=(None) and loop_flag:
        win32api.SetCursorPos((point[0],point[1]))
        loop_flag = False
        
    point = pyautogui.locateCenterOnScreen('square.png',confidence=0.5)
    if point!=(None):
        win32api.SetCursorPos((point[0],point[1]))
        loop_flag = False
                
    







