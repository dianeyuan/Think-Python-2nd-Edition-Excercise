# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 13:47:39 2018

@author: ASUS
"""

def most_frequent(string):
    # build a dict
    d = dict()
    for char in string:
        if char not in ' .,':
            d[char.lower()] = d.get(char.lower(),0)+1
    
    # make a invert dict
    
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val,[]).append(key)
        
    res = sorted(inverse.items(),reverse = True)
    return res

string = 'Letter frequency analysis gained additional importance \
in Europe with the development of movable type in AD, where one must estimate the amount of type required for each letterform, as evidenced by the variations in letter compartment size in typographer'

print(most_frequent(string))