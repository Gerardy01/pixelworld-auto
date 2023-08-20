import os
import threading
import pyautogui as pt

from services.autofarm import auto_left_right, auto_middle
from services.action import always_punch_mouse, always_punch
from utils import must_yes, count_down, ready_start
from services.autofish import Fishing

path = os.path.dirname(os.path.dirname(__file__))
img_path = os.path.join(path, 'img')



class PixelWorldAuto:
    
    def main(self):
        self.routing()
    
    def routing(self):
        print('\n\nWARNING! YOU ARE REQUIRED NOT TO MOVE ANYTHING AFTER THE PROGRAM STARTED\n\n')
        print('- auto break left right mode = (1)')
        print('- auto break middle mode = (2)')
        print('- always punch with (p) key = (3)')
        print('- always punch with hold mouse left = (4)')
        print('- auto fish = (5)')
        action = input('\nPlease select action: ')

        if str(action) == "1":
            auto_left_right()
            return

        if str(action) == "2":
            auto_middle()
            return

        if str(action) == "3":
            always_punch()
            return
        
        if str(action) == "4":
            always_punch_mouse()
            return
        
        if str(action) == "5":
            print('\nset your cursor right on your fishing spot')
            must_yes()
            
            count_down(1, 'Locating...')
            x, y = pt.position()
            print('RECORDED!')

            ready_start()

            obj = Fishing()

            strike_detect = threading.Thread(target=obj.fish_strike_detection)
            strike_detect.daemon = True
            strike_detect.start()

            strike_detect = threading.Thread(target=obj.auto_click, args=(x, y))
            strike_detect.daemon = True
            strike_detect.start()

            strike_detect = threading.Thread(target=obj.find_net)
            strike_detect.daemon = True
            strike_detect.start()

            strike_detect = threading.Thread(target=obj.detect_fish_on)
            strike_detect.daemon = True
            strike_detect.start()

            obj.auto_fish2()
            return
        
        if str(action) == "0":
            self.test()
            return
        
        print('there is no any action with inputed number')
    


    def test(self):
        ...



if __name__ == "__main__":
    object = PixelWorldAuto()
    object.main()