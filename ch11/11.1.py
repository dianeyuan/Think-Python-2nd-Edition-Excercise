# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 09:19:59 2018

@author: ASUS
"""

import time
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

def dictionary():
    d = dict()
    file = open('words.txt')
    for line in file:
        word = line.strip()
        d[word] = 1
    file.close()
    return d
        
 

# get the running time for dict search
start_1 = time.time()
print('highway' in dictionary())
end_1 = time.time()
print('Dictionary search takes {:.5f} seconds'.format(end_1-start_1))


# get the running time for binary search, it takes less time.
word_list = make_list()

start_2 = time.time()
print(in_bisect('highway',word_list))
end_2 = time.time()
print('Binary search takes {:.5f} seconds'.format(end_2-start_2)) 