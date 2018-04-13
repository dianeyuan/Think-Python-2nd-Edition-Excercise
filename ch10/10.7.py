# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 16:09:44 2018

@author: ASUS
"""

def has_duplicates(a_list):
    for i in a_list:
        if a_list.count(i) > 1:
            return True
    return False

# true
print(has_duplicates(['a','b','c','a']))

# false
print(has_duplicates(['a','b','c','d']))