# -*- coding: utf-8 -*-
"""
Created on Fri May 16 16:11:14 2025

@author: test
"""

import cv2
image = cv2.imread('image.jpg')

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyALLWindows()

print(image.shape)