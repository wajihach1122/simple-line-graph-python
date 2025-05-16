
# -*- coding: utf-8 -*-
"""
Created on Fri May 16 16:11:14 2025

@author: test
"""

from PIL import Image

image = Image.open('image.jpg')

image.show()

print(image.size)