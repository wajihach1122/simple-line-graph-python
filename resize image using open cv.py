# -*- coding: utf-8 -*-
"""
Created on Fri May 16 16:41:39 2025

@author: test
"""
import cv2
image = cv2.imread ('image.jpg')
resized_image = cv2.resize(image, (300,200))
cv2.imshow('Resized image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()