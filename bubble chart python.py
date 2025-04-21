# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 18:17:02 2025

@author: test
"""

import matplotlib.pyplot as plt
import numpy as np
x = [5,7,8,9,5]
y = [99, 86, 87, 100,86]
sizes = [10, 100, 99, 150,220]


plt.scatter(x, y, s=sizes, alpha=0.5, color='black')

plt.title('bubble chart')
plt.xlabel('x')
plt.ylabel('y')

plt.show()