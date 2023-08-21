import pyautogui as pt
import random
import cv2
import mss
import numpy as np
import dxcam

from time import sleep

from utils import screen_shot, match_image, find_image, hold_key, hold_mouse
from config import IMG_PATH

from PIL import ImageGrab

import time
import matplotlib.pyplot as plt
pt.PAUSE = 0.001
class Fishing:

    def __init__(self):
        self.is_catching = False
        self.is_strike = False

    def auto_fish(self):
        screen_width, screen_height = pt.size()
        fish_on_pos_x = 0
        fish_on_pos_y = 0
        while True:
            if fish_on_pos_x == 0:
                max_loc, max_val, _ = match_image("fishon.png", screen_shot())
                if max_val > 0.8:
                    fish_on_pos_x = max_loc[0]
                    fish_on_pos_y = max_loc[1]
            stc = mss.mss()
            scr = stc.grab(
                {
                    "left": fish_on_pos_x - 300,
                    "top": fish_on_pos_y + 55,
                    "width": 800,
                    "height": 50,
                }
            )
            ss = np.array(scr)
            ss = cv2.cvtColor(ss, cv2.IMREAD_COLOR)

            frame = np.array(scr)

            unfish_x, unfish_y, unactive_img = self.unactive_fish_detection(ss)
            acfish_x, acfish_y, active_img = self.active_fish_detection(ss)

            if unfish_x != 0 and unfish_y != 0:
                w = unactive_img.shape[1]
                h = unactive_img.shape[0]
                cv2.rectangle(frame, (unfish_x, unfish_y), (unfish_x + w, unfish_y + h), (0, 255, 255), 2)
                arrow_right_x, arrow_right_y = find_image("arrowright.png", ss)
                arrow_left_x, arrow_left_y = find_image("arrowleft.png", ss)
                print(arrow_right_x, arrow_left_x)
                if arrow_right_x != 0 and arrow_left_x != 0:
                    arrow_mid = ((arrow_right_x + arrow_left_x) / 2) + 10
                    midpoint_y = (arrow_right_y + arrow_left_y) / 2
                    cv2.circle(frame, (int(arrow_mid), int(midpoint_y)), 5, (0, 255, 0), -1)
                    if unfish_x < arrow_mid:
                        pt.keyUp('d')
                        pt.keyDown('a')
                    elif unfish_x > arrow_mid:
                        pt.keyUp('a')
                        pt.keyDown('d')
            elif acfish_x != 0 and acfish_y != 0:
                w = active_img.shape[1]
                h = active_img.shape[0]
                cv2.circle(frame, (int(acfish_x), int(acfish_y)), 5, (255, 0, 0), -1)
                arrow_right_x, arrow_right_y = find_image("arrowright.png", ss)
                arrow_left_x, arrow_left_y = find_image("arrowleft.png", ss)
                if arrow_right_x != 0:
                    arrow_mid = ((arrow_right_x + arrow_left_x) / 2) + 10
                    midpoint_y = (arrow_right_y + arrow_left_y) / 2
                    cv2.circle(frame, (int(arrow_mid), int(midpoint_y)), 5, (0, 0, 255), -1)

                    if abs(acfish_x + (w/2) - arrow_mid)> 5: 
                        if acfish_x + (w/2) < arrow_mid:
                            pt.keyUp('d')
                            pt.keyDown('a')
                        if acfish_x + (w/2) > arrow_mid:
                            pt.keyUp('a')
                            pt.keyDown('d')
            else:
                pt.keyUp('a')
                pt.keyUp('d')
        
            cv2.imshow("fish bar", frame)
            cv2.setWindowProperty("fish bar", cv2.WND_PROP_TOPMOST, 1)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                cv2.waitKey(1)



    def unactive_fish_detection(self, ss=screen_shot()):
        max_loc, max_val, img = match_image("fishfin.png", ss)
        if max_val > 0.6:
            return max_loc[0], max_loc[1], img
        
        max_loc, max_val, img = match_image("fishfinreverse.png", ss)
        if max_val > 0.6:
            return max_loc[0], max_loc[1], img

        return 0, 0, img
    
    def active_fish_detection(self, ss=screen_shot()):

        max_loc, max_val, img = match_image("fishtailactiveleft.png", ss)
        if max_val > 0.6:
            return max_loc[0]-20, max_loc[1], img
        
        max_loc, max_val, img = match_image("fishtailactiveright.png", ss)
        if max_val > 0.6:
            return max_loc[0]+12, max_loc[1], img

        return 0, 0, img

    def fish_strike_detection(self):
        while True:
            sleep(0.1)
            try:
                max_loc, max_val, _ = match_image("strike.png", screen_shot())
                if max_val > 0.8:
                    hold_key('space', 0)
                    self.is_catching = True
                    self.is_strike = True
            except:
                continue
    
    def auto_click(self, pos_x, pos_y):
        while True:
            try:
                max_loc, max_val, _ = match_image("take.png", screen_shot())
                if max_val > 0.8:
                    pt.moveTo(x=max_loc[0], y=max_loc[1])
                    hold_mouse('left', 0.1)
                    continue
                else:
                    pt.moveTo(x=pos_x, y=pos_y, duration=random.uniform(0.1, 0.3))
                    hold_mouse('left', 0.1)
            except:
                continue
            sleep(random.uniform(5, 6))
    
    def find_net(self):

        fish_on_pos_x = 0
        fish_on_pos_y = 0

        while fish_on_pos_x == 0:
            sleep(0.1)
            try:
                max_loc, max_val, _ = match_image("fishon.png", screen_shot())
                if max_val > 0.8:
                    fish_on_pos_x = max_loc[0]
                    fish_on_pos_y = max_loc[1]
            except:
                continue

        while True:
            sleep(0.1)
            try:
                stc = mss.mss()
                scr = stc.grab(
                    {
                        "left": fish_on_pos_x - 200,
                        "top": fish_on_pos_y + 90,
                        "width": 600,
                        "height": 60,
                    }
                )
                ss = np.array(scr)
                ss = cv2.cvtColor(ss, cv2.IMREAD_COLOR)

                max_loc, max_val, _ = match_image("fishnet.png", ss=ss)
                if max_val > 0.8:
                    hold_key('space', 0)
            except:
                continue
    
    def detect_fish_on(self):
        while True:
            sleep(0.1)
            try:
                if not self.is_strike: continue
                max_loc, max_val, _ = match_image("fishon.png", screen_shot())
                if max_val > 0.8:
                    self.is_catching = True
                    continue
                if max_val < 0.8:
                    self.is_catching = False
                    pt.keyUp('a')
                    pt.keyUp('d')
                    continue
                self.is_strike = False
            except:
                continue

    


    def auto_fish2(self):
        
        fish_on_pos_x = 0
        fish_on_pos_y = 0

        while fish_on_pos_x == 0:
            max_loc, max_val, _ = match_image("fishon.png", screen_shot())
            if max_val > 0.8:
                fish_on_pos_x = max_loc[0]
                fish_on_pos_y = max_loc[1]

        camera = dxcam.create()
        camera.start(region=(fish_on_pos_x - 201, fish_on_pos_y + 66, fish_on_pos_x + 369, fish_on_pos_y + 67), target_fps= 60, video_mode= True)

        while True:
            if not self.is_catching: continue
            fish_pic = camera.get_latest_frame()
            sqr_loc = self.locate_color(fish_pic , color = [8, 255, 29])
            fish_loc = self.locate_2color(pic=fish_pic, color = ([16, 53, 94], [4, 232, 21]))
            if sqr_loc != None and fish_loc != None:
                dis = abs(fish_loc - sqr_loc)
                eps = 0
                if dis > eps:
                    # ke kiri`
                    if fish_loc< sqr_loc:
                        pt.keyUp('d')
                        pt.keyDown('a')
                    #ke kanan
                    else:
                        pt.keyUp('a')
                        pt.keyDown('d')
    
    def locate_color(self, pic, color = [11, 52, 94], round_val = 2):
        shape_rgb = np.array(color)

        pic_arr = np.array(pic)    

        loc_mask = np.absolute(pic_arr -shape_rgb) <= round_val 
        try:
            shape_loc =round(np.mean(np.where(loc_mask)[1]))
            return shape_loc
        except:
            return None

    def locate_2color(self, pic, color = ([11, 52, 94], [0,198, 15]), round_val = 2):
        
        color1 = np.array(color[0])
        color2 = np.array(color[1])
        pic_arr = np.array(pic)
        # loc_mask1 = np.absolute(pic_arr -color1) <= round_val
        pic_brightness = self.color_brightness(pic)
        loc_mask1 = pic_brightness <= 55
        loc_mask2 = np.absolute(pic_arr -color2) <= round_val
        mask1_sum = np.sum(loc_mask1)
        mask2_sum = np.sum(loc_mask2)
        area_threshold = 150
        try:
            if mask1_sum > mask2_sum:
                shape1_locs =np.where(loc_mask1)[1]
                shape_loc = round(np.mean(shape1_locs))
            else:
                shape2_locs =np.where(loc_mask2)[1]
                shape_loc = round(np.mean(shape2_locs))
            return shape_loc
        except:
            return None

    def color_brightness(self, rgb):
        return rgb[:, :, 0]*0.21 + rgb[:, :, 1]*0.72 + rgb[:, :, 2]*0.07
    
