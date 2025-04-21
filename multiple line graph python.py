# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 17:17:57 2025

@author: test
"""

import matplotlib.pyplot as plt
years = [2018, 2019, 2020, 2021, 2022]
product_a = [120,240,37,4,5]
product_b = [500,4,10,9,7]
product_c = [100,88,99,9,7]
product_d = [3,420,6,300,76]
product_e = [160,4,230,6,79]

plt.plot(years, product_a, label="product a", marker='o', linestyle='-', color='green')
plt.plot(years, product_b, label="product b", marker='s', linestyle='--', color='blue')
plt.plot(years, product_c, label="product c", marker='x', linestyle='-', color='red')
plt.plot(years, product_d, label="product d", marker='d', linestyle=':', color='purple')
plt.plot(years, product_e, label="product e", marker='^', linestyle='-', color='orange')


plt.xlabel("year")
plt.ylabel("sales")
plt.title("sales trends of 5 products (2018-2022)")
plt.grid(True)
plt.legend()

plt.show()
