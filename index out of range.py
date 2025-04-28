# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
numbers = [10,20,30]
try:
    index = int(input(" Enter a index (0-2): "))
    print("value:", numbers[index])
except IndexError :
    print ("Error: index out of range")
