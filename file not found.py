# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

try:
    file = open("data.txt ", "r")
    print(file.read())
    file.close()
except FileNotFoundError :
    print ("Error: File not found!")
