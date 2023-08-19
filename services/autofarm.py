import pyautogui as pt
import random

from time import sleep

from utils import hold_key, hold_mouse, count_down, must_yes, yes_or_no, ready_start



def auto_left_right():
    print('\n!READ THIS!')
    print(f'- Make sure there is no any block on the left and right side of your character for two blocks length')
    print('- Make sure to select desired items to break in inventory')
    print('!READ THIS!')

    right_placement_1_x = 0
    right_placement_1_y = 0
    right_placement_2_x = 0
    right_placement_2_y = 0

    left_placement_1_x = 0
    left_placement_1_y = 0
    left_placement_2_x = 0
    left_placement_2_y = 0

    break_duration = 1

    print('\nset your cursor right on your character')
    must_yes()
    
    count_down(1, 'Locating...')

    x, y = pt.position()

    right_placement_1_x = x - 60
    right_placement_1_y = y
    right_placement_2_x = x - 130
    right_placement_2_y = y

    left_placement_1_x = x + 60
    left_placement_1_y = y
    left_placement_2_x = x + 130
    left_placement_2_y = y
    print('RECORDED!')

    ready = False
    while not ready:
        try:
            break_duration = float(input('input how long is the desired break duration for one side: '))
            ready = True
        except:
            print('must be valid number')
    
    auto_collect = yes_or_no("do you want to use auto collect?")

    if auto_collect:
        harmless_block_x = 0
        harmless_block_y = 0

        break_block_x = 0
        break_block_y = 0

        ready = False
        while not ready:
            try:
                collect_round = int(input('collect every how many cycle: '))
                ready = True
            except:
                print('must be valid number')
        
        print('\nset your cursor right on any harmless block')
        must_yes()
        count_down(1, 'Locating...')
        x, y = pt.position()
        harmless_block_x = x
        harmless_block_y = y
        print('RECORDED!')

        
        print('\nset your cursor right on desired block to break')
        must_yes()
        count_down(1, 'Locating...')
        x, y = pt.position()
        break_block_x = x
        break_block_y = y
        print('RECORDED!')

    ready_start()

    count = 0

    while True:
        sleep(random.uniform(0.1, 0.3))

        pt.moveTo(x=right_placement_1_x, y=right_placement_1_y, duration=random.uniform(0.1, 0.3))
        hold_mouse('left', 0.1)
        pt.moveTo(x=right_placement_2_x, y=right_placement_2_y, duration=random.uniform(0.1, 0.3))
        hold_mouse('left', 0.1)
        hold_key('p', break_duration)

        pt.moveTo(x=left_placement_1_x, y=left_placement_1_y, duration=random.uniform(0.1, 0.3))
        hold_mouse('left', 0.1)
        pt.moveTo(x=left_placement_2_x, y=left_placement_2_y, duration=random.uniform(0.1, 0.3))
        hold_mouse('left', 0.1)
        hold_key('p', break_duration)

        sleep(random.uniform(0.1, 0.3))

        count += 1
        if auto_collect and count >= collect_round:
            pt.moveTo(x=harmless_block_x, y=harmless_block_y, duration=random.uniform(0.1, 0.3))
            hold_mouse('left', 0.1)
            pt.moveTo(x=left_placement_1_x, y=left_placement_1_y, duration=random.uniform(0.1, 0.3))
            hold_mouse('left', 0.1)
            
            hold_key('a', 0.3)
            sleep(random.uniform(0.1, 0.3))
            hold_key('d', 0.4)
            sleep(random.uniform(0.1, 0.3))

            pt.moveTo(x=right_placement_1_x, y=right_placement_1_y, duration=random.uniform(0.1, 0.3))
            hold_mouse('left', 0.1)

            hold_key('d', 0.01)
            hold_key('p', break_duration/2)

            hold_key('d', 0.3)
            sleep(random.uniform(0.1, 0.3))
            hold_key('a', 0.4)
            sleep(0.3)

            hold_key('p', break_duration/2)

            pt.moveTo(x=break_block_x, y=break_block_y, duration=random.uniform(0.1, 0.3))
            hold_mouse('left', 0.1)

            count = 0



def auto_middle():
    print('\n!READ THIS!')
    print('- Make sure there is no any block on the right side of your character for 3 blocks length')
    print('- Make sure to select desired items to break in inventory')
    print('!READ THIS!')

    right_placement_1_x = 0
    right_placement_1_y = 0
    right_placement_2_x = 0
    right_placement_2_y = 0

    left_placement_1_x = 0
    left_placement_1_y = 0
    left_placement_2_x = 0
    left_placement_2_y = 0

    break_duration = 1

    print('\nset your cursor right on your character')
    must_yes()
    
    count_down(1, 'Locating...')

    x, y = pt.position()

    right_placement_1_x = x - 70
    right_placement_1_y = y
    right_placement_2_x = x - 140
    right_placement_2_y = y

    left_placement_1_x = x + 70
    left_placement_1_y = y
    left_placement_2_x = x + 140
    left_placement_2_y = y
    print('RECORDED!')

    ready = False
    while not ready:
        try:
            break_duration = float(input('input how long is the desired break duration for one side: '))
            ready = True
        except:
            print('must be valid number')
    
    ready = False
    while not ready:
        try:
            collect_round = int(input('collect every how many cycle: '))
            ready = True
        except:
            print('must be valid number')
    
    ready_start()

    pos = 1
    count = 0
    while True:
        sleep(random.uniform(0.1, 0.3))

        if pos == 1:
            pt.moveTo(x=left_placement_1_x, y=left_placement_1_y, duration=random.uniform(0.1, 0.3))
            hold_mouse('left', 0.1)
            pt.moveTo(x=left_placement_2_x, y=left_placement_2_y, duration=random.uniform(0.1, 0.3))
            hold_mouse('left', 0.1)
            hold_key('p', break_duration)

        if pos == 2:
            pt.moveTo(x=right_placement_1_x, y=right_placement_1_y, duration=random.uniform(0.1, 0.3))
            hold_mouse('left', 0.1)
            pt.moveTo(x=right_placement_2_x, y=right_placement_2_y, duration=random.uniform(0.1, 0.3))
            hold_mouse('left', 0.1)
            hold_key('p', break_duration)

        count += 1
        if count >= collect_round:
            hold_key('p', break_duration)
            sleep(0.3)
            if pos == 1:
                hold_key('d', 0.6)
                pos = 2
            elif pos == 2:
                hold_key('a', 0.6)
                pos = 1
            count = 0