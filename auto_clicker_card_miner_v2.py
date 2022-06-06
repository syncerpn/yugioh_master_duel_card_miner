# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 20:32:06 2022

@author: nghia_sv
"""
SCRL_SECS = 0.1
IDLE_SECS = 0.8
WAIT_SECS = 0.1 #ok
CAPT_SECS = 0.2 #ok
COLS = 8
ROWS = 3

MAX_CARDS = 86

OFFSET_X = 159
OFFSET_Y = 324

W_SMALLCARD = 157
H_SMALLCARD = 230

W_GAP = 49
H_GAP = 64

X_INIT = OFFSET_X + W_SMALLCARD // 2
Y_INIT = OFFSET_Y + H_SMALLCARD // 2

H_SCROLL = 60

from pynput import mouse, keyboard
import time

card_x = X_INIT
card_y = Y_INIT

mc = mouse.Controller()
kc = keyboard.Controller()

time.sleep(2) ######################################

last_cards = MAX_CARDS % COLS
if last_cards == 0:
    last_cards = COLS

last_cards += (ROWS-1) * COLS

n_cards = 0

while n_cards < MAX_CARDS-last_cards:
    for i in range(COLS):
        n_cards += 1
        #card position
        card_x = X_INIT + i * (W_GAP + W_SMALLCARD)
        
        #action
        mc.position = (card_x, card_y) #move to small card
        time.sleep(WAIT_SECS)
        mc.click(mouse.Button.left, 1)
        time.sleep(IDLE_SECS) #wait for it to show up; takes time (IDLE)
        kc.press(keyboard.Key.f12)
        kc.release(keyboard.Key.f12)
        time.sleep(CAPT_SECS) #wait for it to close; takes time (IDLE)
        mc.click(mouse.Button.right, 1)
        time.sleep(IDLE_SECS) #wait for it to close; takes time (IDLE)
    
    mc.position = (X_INIT, card_y) #move to small card area
    time.sleep(WAIT_SECS)
    mc.scroll(0, -1) #scroll down
    time.sleep(SCRL_SECS) #wait for it to close; takes time (IDLE)
    card_y = card_y + H_SMALLCARD + H_GAP - H_SCROLL
    while card_y - H_SCROLL > OFFSET_Y:
        card_y = card_y - H_SCROLL
        mc.scroll(0, -1) #scroll down
        time.sleep(SCRL_SECS) #wait for it to close; takes time (IDLE)
        
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
        kc.press(keyboard.Key.f12)
        kc.release(keyboard.Key.f12)
        time.sleep(CAPT_SECS) #wait for it to close; takes time (IDLE)
        mc.click(mouse.Button.right, 1)
        time.sleep(IDLE_SECS) #wait for it to close; takes time (IDLE)
    card_y = card_y + H_SMALLCARD + H_GAP