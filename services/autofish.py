import pyautogui as pt
import random
import cv2
import mss
import numpy as np

from time import sleep

from utils import screen_shot, match_image, find_image, hold_key
from config import IMG_PATH

from PIL import ImageGrab

import time
import matplotlib.pyplot as plt

class Fishing:

    def auto_fish2(self):
        screen_width, screen_height = pt.size()
        while True:
            stc = mss.mss()
            scr = stc.grab(
                {
                    "left": screen_width // 2 - 400,
                    "top": screen_height // 2 - 285,
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
                # cv2.rectangle(frame, (acfish_x, acfish_y), (acfish_x + w, acfish_y + h), (0, 0, 255), 2)
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
        
        # max_loc, max_val, img = match_image("fishtail.png", ss)
        # if max_val > 0.8:
        #     return max_loc[0], max_loc[1], img
        
        # max_loc, max_val, img = match_image("fishtailreverse.png", ss)
        # if max_val > 0.8:
        #     return max_loc[0], max_loc[1], img

        return 0, 0, img
    
    def active_fish_detection(self, ss=screen_shot()):

        # max_loc, max_val, img = match_image("fishgreen.png", ss)
        # if max_val > 0.6:
        #     return max_loc[0], max_loc[1], img
        
        # max_loc, max_val, img = match_image("fishgreenleft.png", ss)
        # if max_val > 0.6:
        #     return max_loc[0], max_loc[1], img

        max_loc, max_val, img = match_image("fishtailactiveleft.png", ss)
        if max_val > 0.6:
            return max_loc[0]-20, max_loc[1], img
        
        max_loc, max_val, img = match_image("fishtailactiveright.png", ss)
        if max_val > 0.6:
            return max_loc[0]+22, max_loc[1], img

        return 0, 0, img
    


    def locate_color(self, pic, color = [11, 52, 94], round_val = 15):
        shape_rgb = np.array(color)

        pic_arr = np.array(pic)    

        loc_mask = np.absolute(pic_arr -shape_rgb) <= round_val 
        try:
            shape_loc =round(np.median(np.where(loc_mask)[1]))
            return shape_loc
        except:
            return None

    def locate_2color(self, pic, color = ([11, 52, 94], [0,198, 15]),block = (0,0), round_val = 10):
        color1 = np.array(color[0])
        color2 = np.array(color[1])
        pic_arr = np.array(pic)
        loc_mask1 = np.absolute(pic_arr -color1) <= round_val
        loc_mask2 = np.absolute(pic_arr -color2) <= round_val
        mask1_sum = np.sum(loc_mask1)
        mask2_sum = np.sum(loc_mask2)
        area_threshold = 150
        try:
            if mask1_sum > mask2_sum:
                loc_mask1[block[0]:block[1]] = False
                # if np.sum(loc_mask1) < 475:
                #     return None
                shape1_locs =np.where(loc_mask1)[1]
                shape_loc = round(np.median(shape1_locs))
            else:
                loc_mask2[block[0]:block[1]] = False
                if np.sum(loc_mask2) < 1200:
                    return None
                shape2_locs =np.where(loc_mask2)[1]
                shape_loc = round(np.median(shape2_locs))
            return shape_loc
        except:
            return None
        
    def auto_fish(self):
        locs_fish = []
        locs_sqr = []
        times = []
        # time_end = time.perf_counter() + 60
        # while time.perf_counter() < time_end:
        while True:
            #get image for fish
            fish_pic =  ImageGrab.grab(bbox=(290,140,980, 150))
            #get image for square
            sqr_pic = ImageGrab.grab(bbox=(290,114,980, 116))
            
            #locate square
            sqr_loc = self.locate_color(sqr_pic, color = [61, 136, 0])

            
            #move
            if sqr_loc != None:
                #locate fish
                fish_loc = self.locate_2color(pic=fish_pic, color = ([74, 232, 0], [16, 53, 94]), block = (sqr_loc-35, sqr_loc+35))
                if fish_loc != None:
                        
                    # locs_fish.append(fish_loc)
                    # locs_sqr.append(sqr_loc)
                    # times.append(time.perf_counter())
                    dis = abs(fish_loc - sqr_loc)
                    eps = 5
                    if dis > eps:
                        #ke kiri
                        if fish_loc< sqr_loc:
                            pt.keyUp('d')
                            pt.keyDown('a')
                        #ke kanan
                        else:
                            pt.keyUp('a')
                            pt.keyDown('d')

                else:
                    pt.keyUp('a')
                    pt.keyUp('d')

        # plt.scatter(times, aaalocs_fish)
        # plt.scatter(times, locs_sqr)
        # plt.show()
    
