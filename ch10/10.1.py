# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 14:52:01 2018

@author: ASUS
"""

def nested_sum(a_list):
    res = 0
    for item in a_list:
        res += sum(item)
    return res

t = [[1,2],[3],[4,5,6]]
print(nested_sum(t))