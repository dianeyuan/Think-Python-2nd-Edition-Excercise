# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 15:20:20 2018

@author: ASUS
"""

def is_sorted(a_list):
    if a_list == sorted(a_list):
        return True
    else:
        return False
    
print(is_sorted([1,2,2]))
print(is_sorted(['b','a']))