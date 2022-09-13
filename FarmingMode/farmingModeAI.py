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

smallShotWidth = 70

screenXstart = 5
screenYstart = 140
screenXend = 1900
screenYend = 1000
screen_dx = screenXend-screenXstart
screen_dy = screenYend-screenYstart

def findCentroid(x,y,c): #find the centroid of a shape which contains the pixels x and y
    ss = pyautogui.screenshot(region=((x-smallShotWidth),(y-smallShotWidth),smallShotWidth,smallShotWidth))
    width,height = ss.size

    shapeXpix = []
    shapeYpix = []

    for xx in range(0,width): #search all pixels in the screen and save their values for later
        for yy in range(0,height):
            r,g,b = ss.getpixel((xx,yy))
            if b==c:
                shapeXpix = shapeXpix+[xx]
                print(xx)
                shapeYpix = shapeYpix+[yy]
    
    #centroid the x and y coordinates
    x_cent = sum(shapeXpix)/len(shapeXpix)
    y_cent = sum(shapeYpix)/len(shapeYpix)

    return x_cent,y_cent

while keyboard.is_pressed('q') == False:
    pic = pyautogui.screenshot(region=(screenXstart,screenYstart,screen_dx,screen_dy))
    width,height = pic.size
    target_flag = False
    
    for xx in range(0,width,5): #first scan for pentagons
        for yy in range(0,height,5):
            r,g,b = pic.getpixel((xx,yy))
            if b==252:
                c_best = 252
                x_tar = xx
                y_tar = yy
                target_flag = True
                break
                
    if not target_flag:
        for xx in range(0,width,5): #then scan for triangles
            for yy in range(0,height,5):
                r,g,b = pic.getpixel((xx,yy))
                if b==119:
                    c_best = 119
                    x_tar = xx
                    y_tar = yy
                    target_flag = True
                    break

    if not target_flag:
        for xx in range(0,width,5): #finally scan for squares
            for yy in range(0,height,5):
                r,g,b = pic.getpixel((xx,yy))
                if b==105:
                    c_best = 105
                    x_tar = xx
                    y_tar = yy
                    target_flag = True
                    break
    if target_flag: #if we found a target, centroid its pixels
        Xc,Yc = findCentroid(x_tar,y_tar,c_best)
        win32api.SetCursorPos((Xc,Yc))
                
    







