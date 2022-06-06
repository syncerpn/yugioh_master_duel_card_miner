# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 20:32:06 2022

@author: nghia_sv
"""
IDLE_SECS = 0.5
WAIT_SECS = 0.3 #ok
COLS = 6

OFFSET_X = 1316
OFFSET_Y =  340

W_SMALLCARD =  79
H_SMALLCARD = 114

W_GAP =  7
H_GAP = 26

X_INIT = OFFSET_X + W_SMALLCARD // 2
Y_INIT = OFFSET_Y + H_SMALLCARD // 2

H_SCROLL = 98

# X_BIGCARD = 343
# Y_BIGCARD = 484

X_BIGCARD = 151
Y_BIGCARD = 315


from pynput import mouse, keyboard
import time

card_x = X_INIT
card_y = Y_INIT

mc = mouse.Controller()
kc = keyboard.Controller()

time.sleep(2) ######################################

for t in range(2):
    for i in range(COLS):
        #card position
        card_x = X_INIT + i * (W_GAP + W_SMALLCARD)
        
        # #action
        mc.position = (card_x, card_y) #move to small card
        time.sleep(WAIT_SECS)
        mc.click(mouse.Button.left, 1) #choose it
        time.sleep(WAIT_SECS)
        mc.position = (X_BIGCARD, Y_BIGCARD) #move to big card
        time.sleep(WAIT_SECS)
        mc.click(mouse.Button.left, 1)
        time.sleep(IDLE_SECS) #wait for it to show up; takes time (IDLE)
        kc.press(keyboard.Key.f12)
        kc.release(keyboard.Key.f12)
        time.sleep(IDLE_SECS) #wait for it to close; takes time (IDLE)
        mc.click(mouse.Button.right, 1)
        time.sleep(IDLE_SECS) #wait for it to close; takes time (IDLE)
    
    mc.position = (X_INIT, Y_INIT) #move to small card area
    time.sleep(WAIT_SECS)
    mc.scroll(0, -1) #scroll down
    time.sleep(IDLE_SECS) #wait for it to close; takes time (IDLE)
    card_y = card_y + H_SMALLCARD + H_GAP - H_SCROLL
    while card_y - H_SCROLL > OFFSET_Y:
        card_y = card_y - H_SCROLL
        mc.scroll(0, -1) #scroll down
        time.sleep(IDLE_SECS) #wait for it to close; takes time (IDLE)
        
        