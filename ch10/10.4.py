# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 15:16:46 2018

@author: ASUS
"""

def chop(a_list):
    del a_list[0]
    del a_list[-1]
    return None

t = [1,2,3,4]
chop(t)
print(t)
