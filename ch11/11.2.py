# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 10:24:51 2018

@author: ASUS
"""

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val,[]).append(key)
        
    return inverse

def histogram(s):
    d = dict()
    for char in s:
        d[char] = d.get(char,0)+1
    return d

print(histogram('parrot'))
d = histogram('parrot')
print(invert_dict(d))
        
        
        
        
            