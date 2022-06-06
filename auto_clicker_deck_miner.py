# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 20:32:06 2022

@author: nghia_sv
"""
IDLE_SECS = 0.8
WAIT_SECS = 0.1 #ok
CAPT_SECS = 0.2 #ok

MAX_CARDS = 40

if MAX_CARDS <= 50:
    COLS = 10
    ROWS = MAX_CARDS // COLS
    if MAX_CARDS % COLS != 0:
        ROWS += 1
    W_GAP = 12
    
elif MAX_CARDS <= 55:
    COLS = 11
    ROWS = 5
    W_GAP = 5
    
elif MAX_CARDS <= 60:
    COLS = 12
    ROWS = 5
    W_GAP = 0
    
else:
    COLS = 13
    ROWS = 5
    W_GAP = -6

H_GAP = 12

OFFSET_X = 512
OFFSET_Y = 222

W_SMALLCARD = 64
H_SMALLCARD = 93

X_INIT = OFFSET_X + W_SMALLCARD // 2
Y_INIT = OFFSET_Y + H_SMALLCARD // 2

X_BIGCARD = 135
Y_BIGCARD = 286

from pynput import mouse, keyboard
import time

card_x = X_INIT
card_y = Y_INIT

mc = mouse.Controller()
kc = keyboard.Controller()

time.sleep(2) ######################################

n_cards = 0
        
for j in range(ROWS):
    for i in range(COLS):
        if n_cards >= MAX_CARDS:
            break
        n_cards += 1
        card_x = X_INIT + i * (W_GAP + W_SMALLCARD)
        
        #action
        mc.position = (card_x, card_y) #move to small card
        time.sleep(WAIT_SECS)
        mc.click(mouse.Button.left, 1)
        time.sleep(IDLE_SECS) #wait for it to show up; takes time (IDLE)
        mc.position = (X_BIGCARD, Y_BIGCARD) #move to big card
        time.sleep(WAIT_SECS)
        mc.click(mouse.Button.left, 1)
        time.sleep(IDLE_SECS) #wait for it to show up; takes time (IDLE)
        kc.press(keyboard.Key.f12)
        kc.release(keyboard.Key.f12)
        time.sleep(CAPT_SECS) #wait for it to close; takes time (IDLE)
        mc.click(mouse.Button.right, 1)
        time.sleep(IDLE_SECS) #wait for it to close; takes time (IDLE)

    card_y = card_y + H_SMALLCARD + H_GAP

#EXTRA DECK ==================================================================

MAX_EXTRA = 5
COLS = 10
ROWS = MAX_EXTRA // COLS
if MAX_EXTRA % COLS != 0:
    ROWS += 1
W_GAP = 12
H_GAP = 12
OFFSET_X = 512
OFFSET_Y = 792

W_SMALLCARD = 64
H_SMALLCARD = 93
X_INIT = OFFSET_X + W_SMALLCARD // 2
Y_INIT = OFFSET_Y + H_SMALLCARD // 2
card_x = X_INIT
card_y = Y_INIT
n_cards = 0
        
for j in range(ROWS):
    for i in range(COLS):
        if n_cards >= MAX_EXTRA:
            break
        n_cards += 1
        card_x = X_INIT + i * (W_GAP + W_SMALLCARD)
        
        #action
        mc.position = (card_x, card_y) #move to small card
        time.sleep(WAIT_SECS)
        mc.click(mouse.Button.left, 1)
        time.sleep(IDLE_SECS) #wait for it to show up; takes time (IDLE)
        mc.position = (X_BIGCARD, Y_BIGCARD) #move to big card
        time.sleep(WAIT_SECS)
        mc.click(mouse.Button.left, 1)
        time.sleep(IDLE_SECS) #wait for it to show up; takes time (IDLE)
        kc.press(keyboard.Key.f12)
        kc.release(keyboard.Key.f12)
        time.sleep(CAPT_SECS) #wait for it to close; takes time (IDLE)
        mc.click(mouse.Button.right, 1)
        time.sleep(IDLE_SECS) #wait for it to close; takes time (IDLE)

    card_y = card_y + H_SMALLCARD + H_GAP