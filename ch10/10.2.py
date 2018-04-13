# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 15:12:39 2018

@author: ASUS
"""

def cumsum(a_list):
    res = []
    total = 0
    for i in a_list:
        total += i
        res.append(total)
        
    return res

print(cumsum([1,2,3]))
        
        