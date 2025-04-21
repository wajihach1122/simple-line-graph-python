# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 18:17:02 2025

@author: test
"""

import matplotlib.pyplot as plt
categories = [1,2,3,4,5]
values = [11,15,10,9,6]

plt.bar(categories, values)
plt.title('bar chart')
plt.xlabel('categories')
plt.ylabel('values')

plt.show()