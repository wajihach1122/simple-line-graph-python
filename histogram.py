# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 18:17:02 2025

@author: test
"""

import matplotlib.pyplot as plt
data = [10,32,36,40,20,12,20,10,6]
plt.hist(data, bins=5, color='pink', edgecolor='black')

plt.title('histogram example (list data)')
plt.xlabel('value')
plt.ylabel('frequency')

plt.show()