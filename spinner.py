# -*- coding: utf-8 -*-
from __future__ import print_function
import time
import sys
from datetime import timedelta
import datetime


CALLED = 0
def test_callback_true():
    '''
    test_callback which returns true and then false
    '''
    global CALLED
    CALLED = CALLED + 1
    if CALLED < 50: # equals ~ 10s = 0,2 * 50
        return True
    else:
        CALLED = 0
        return False

def test_callback_false():
    '''
    test_callback which returns true and then false
    '''
    global CALLED
    CALLED = CALLED + 1
    if CALLED < 50: # equals ~ 10s = 0,2 * 50
        return False
    else:
        CALLED = 0
        return True

'''
LOADING ANIMATION AND COUNTDOWN
'''
def sleep(interval_time=0, countdown=False, callback=None, negative=False, loading_anim=None):
    '''
    makes cool print effect with countdown, to show it is working and not crashed
    '''
    if loading_anim and (len(loading_anim) > 2):
        loading_anim = loading_anim
    else:
        loading_anim = ['🌑','🌒','🌓','🌔','🌕','🌖','🌗','🌘'] # rotating moon
        # loading_anim = ['🕐','🕑','🕒','🕓','🕔','🕕','🕖','🕗','🕘','🕙','🕚','🕛'] # rotation clock
        # loading_anim = ['|','/','–','\\'] # rotating slash

    length_index = len(loading_anim)
    anim_index = 0

    '''
    if got callback and check while false
    '''
    if callback and negative:
        while not callback():
            print(str(loading_anim[anim_index]) + '\r' ,end='')
            time.sleep(0.2)
            anim_index = anim_index + 1
            if anim_index == length_index:
                anim_index = 0
            sys.stdout.flush()
        return
    '''
    if got callback and check while true
    '''
    if callback:
        while callback():
            print(str(loading_anim[anim_index]) + '\r' ,end='')
            time.sleep(0.2)
            anim_index = anim_index + 1
            if anim_index == length_index:
                anim_index = 0
            sys.stdout.flush()
        return
    '''
    doing for given interval
    '''
    if interval_time <= 0:
        return
    end_time = datetime.datetime.now() + timedelta(seconds=interval_time)
    while datetime.datetime.now() <= end_time:
        if countdown:
            print(str(loading_anim[anim_index]) + ' Remaining: ' + str(end_time - datetime.datetime.now()) + '\r' ,end='')
        else:
            print(str(loading_anim[anim_index]) + '\r' ,end='')
        time.sleep(0.2)
        anim_index = anim_index + 1
        if anim_index == length_index:
            anim_index = 0
        sys.stdout.flush()
    return

if __name__ == '__main__':
    interval_time = 10.0
    # look cool while waiting and idling
    print('Starting showtime:')
    print('Loading anim for time interval with countdown \nExample: sleep(interval_time, countdown=True|False|None)')
    sleep(interval_time, countdown=True)
    print('Loading anim while callback returns TRUE \nExample: sleep(callback=callable_function)')
    sleep(callback=test_callback_true)
    print('Loading anim while callback returns FALSE \nExample: sleep(callback=callable_function, negative=True)')
    sleep(callback=test_callback_false, negative=True)
    print('Loading anim with another animation via arguments \nExample: sleep(interval_time=interval_time, loading_anim=[".  ",".. ","..."])')
    sleep(interval_time=interval_time, loading_anim=[".  ",".. ","..."])
