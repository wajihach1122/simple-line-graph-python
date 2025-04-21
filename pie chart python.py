# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 18:17:02 2025

@author: test
"""

import matplotlib.pyplot as plt
sizes = [1,2,3,4,5]
labels = [11,15,10,9,6]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
