# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 17:13:12 2018

@author: ASUS
"""
import bisect
def in_bisect(x,a_list):
    i = bisect.bisect_left(a_list, x)
    if i != len(a_list) and a_list[i] == x:
        return i
    else:
        return None
    
def make_list():
    l = []
    file = open('words.txt')
    for line in file:
        word = line.strip()
        l.append(word)
    file.close()
    return l


word_list = make_list()
# true
print(in_bisect('highway',word_list))

# none
print(in_bisect('magicworld',word_list))
