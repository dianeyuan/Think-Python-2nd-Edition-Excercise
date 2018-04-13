# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 11:35:54 2018

@author: ASUS
"""

def has_duplicates(a_list):
    d = dict()
    for item in a_list:
        d[item] = d.get(item,0)+1
        if d[item] > 1:
            return True
    return False

# false
list_1 = ['a','b','c','d']
print(has_duplicates(list_1))

# true
list_2 = ['a','b','c','a']
print(has_duplicates(list_2))

    