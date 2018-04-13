# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 16:06:04 2018

@author: ASUS
"""

def is_anagram(str_1,str_2):
    if sorted(list(str_1)) == sorted(list(str_2)):
        return True
    else:
        return False
    
# true
print(is_anagram('bat','tab'))

# false
print(is_anagram('bat','cat'))
    
