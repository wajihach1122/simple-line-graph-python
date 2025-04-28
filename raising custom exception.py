# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def check_age(age):
    if age < 18:
        raise ValueError("age must be 18 or above.")
    return "access granted."
try:
    print(check_age(20))
except ValueError as e:
    print (f" Exception: {e}")
