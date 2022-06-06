# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 19:07:50 2022

@author: nghia_sv
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

image_dir = 'D:/REC/cards/'
image_card_dir = image_dir + 'card_images/'
image_list = [f for f in os.listdir(image_dir) if (f.endswith('.jpg') or f.endswith('.png'))]

if not os.path.isdir(image_card_dir):
    os.makedirs(image_card_dir)

CW = 447
CH = 646
IX = 132
IY = 168

ALPHA_MASK = np.zeros((CH,CW,1), dtype=np.uint8) + 1
ALPHA_MASK[0,0:6,:] = 0
ALPHA_MASK[1,0:5,:] = 0
ALPHA_MASK[2,0:4,:] = 0
ALPHA_MASK[3,0:3,:] = 0
ALPHA_MASK[4,0:2,:] = 0
ALPHA_MASK[5,0:1,:] = 0

ALPHA_MASK[0,-6:,:] = 0
ALPHA_MASK[1,-5:,:] = 0
ALPHA_MASK[2,-4:,:] = 0
ALPHA_MASK[3,-3:,:] = 0
ALPHA_MASK[4,-2:,:] = 0
ALPHA_MASK[5,-1:,:] = 0

ALPHA_MASK[-1,0:6,:] = 0
ALPHA_MASK[-2,0:5,:] = 0
ALPHA_MASK[-3,0:4,:] = 0
ALPHA_MASK[-4,0:3,:] = 0
ALPHA_MASK[-5,0:2,:] = 0
ALPHA_MASK[-6,0:1,:] = 0

ALPHA_MASK[-1,-6:,:] = 0
ALPHA_MASK[-2,-5:,:] = 0
ALPHA_MASK[-3,-4:,:] = 0
ALPHA_MASK[-4,-3:,:] = 0
ALPHA_MASK[-5,-2:,:] = 0
ALPHA_MASK[-6,-1:,:] = 0

for image_file in image_list:
    image = np.asarray(Image.open(image_dir + image_file))
    image_card = np.zeros((CH,CW,3), dtype=np.uint8)
    image_card = image[IY:IY+CH, IX:IX+CW, :]
    image_card = image_card * ALPHA_MASK
    plt.imsave(image_card_dir + image_file[:-4] + '.png', image_card)
