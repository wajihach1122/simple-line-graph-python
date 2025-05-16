# -*- coding: utf-8 -*-
"""
Created on Fri May 16 16:41:39 2025

@author: test
"""
import cv2
image = cv2.imread ('image.jpg')
cv2.rectangle(image,(50,50), ( 200,150), (0,255,0), 2)
cv2.imshow('Rectangle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()