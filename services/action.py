import pyautogui as pt
import random

from time import sleep

from utils import hold_key, hold_mouse, count_down, must_yes, yes_or_no, ready_start



def always_punch():
    ready_start()

    while True:
        sleep(0.1)
        hold_key('p', duration=5)

def always_punch_mouse():
    ready_start()

    while True:
        sleep(0.1)
        hold_mouse('left', duration=5)