# -*- coding: utf-8 -*-
"""
Created on Fri May 16 16:41:39 2025

@author: test
"""
import cv2
image = cv2.imread ('image.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()