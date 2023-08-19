import os

from services.autofarm import auto_left_right, auto_middle
from services.action import always_punch_mouse, always_punch
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
            obj = Fishing()
            obj.auto_fish()
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