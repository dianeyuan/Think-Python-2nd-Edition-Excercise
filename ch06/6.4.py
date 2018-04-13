# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 12:23:35 2018

@author: ASUS
"""

def is_power(a,b):
    if a % b !=0:
        return False
    elif a==b:
        return True
    elif is_power(a/b,b):
        return True


print(is_power(2,2))    
print(is_power(4,2))
print(is_power(5,2))
