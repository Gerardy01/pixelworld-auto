import pyautogui as pt
import cv2
import os
import mss
import numpy as np
from time import sleep
pt.PAUSE = 0.001

from config import IMG_PATH

def hold_key(key, duration):
    pt.keyDown(key)
    sleep(duration)
    pt.keyUp(key)

def hold_mouse(key, duration):
    pt.mouseDown(button=key)
    sleep(duration)
    pt.mouseUp(button=key)

def count_down(duration, end_text="START"):
    for i in range(duration):
        sleep(1)
        print(duration - i)
    sleep(1)
    print(end_text)

def must_yes(question = "Ready?"):
    ready = False
    while not ready:
        input_value = str(input(f'{question} (Y/N): '))
        ready = True if input_value.lower() == "y" else False

def yes_or_no(question = "Ready?"):
    ready = False
    while not ready:
        input_value =  str(input(f'{question} (Y/N): '))
        if input_value.lower() == "y":
            ready = True
            return True
        if input_value.lower() == "n":
            ready = True
            return False
        
def ready_start():
    print('\n You are ready!')
    ready = False
    while not ready:
        input_value = str(input('start the program now? (Y/N): '))
        ready = True if input_value.lower() == "y" else False
    count_down(3)



def match_image(image, ss):
    img = cv2.imread(f"{IMG_PATH}{image}", cv2.IMREAD_UNCHANGED)
    result_try = cv2.matchTemplate(ss, img, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result_try)
    return max_loc, max_val, img

def screen_shot(left=0, top=0, width=1920, height=1080):
    stc = mss.mss()
    scr = stc.grab({
        'left': left,
        'top': top,
        'width': width,
        'height': height
    })

    img = np.array(scr)
    img = cv2.cvtColor(img, cv2.IMREAD_COLOR)

    return img

def find_image(name, ss):
    max_loc, max_val, _ = match_image(name, ss)
    if max_val > 0.6:
        return max_loc[0], max_loc[1]
    return 0, 0


 