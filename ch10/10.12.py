# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 19:04:57 2018

@author: ASUS
"""

import bisect

def in_bisect(x,a_list):
    i = bisect.bisect_left(a_list, x)
    if i != len(a_list) and a_list[i] == x:
        return i
    return None

def is_interlock(word,a_list):
    word_1 = word[::2]
    word_2 = word[1::2]
    if in_bisect(word_1,a_list) != None and in_bisect(word_2,a_list) != None:
        return True
    else:
        return False

def make_list():
    l = []
    file = open('words.txt')
    for line in file:
        word = line.strip()
        l.append(word)
    file.close()
    return l
    
def print_pairs(a_list):
    for word in a_list:
        if is_interlock(word,a_list):
            print(word[::2],word[1::2],word)
            
word_list = make_list()
print('Interlock pairs are:')
print_pairs(word_list)

def three_interlock(word,a_list):
    word_1 = word[::2]
    word_2 = word[1::2]
    word_3 = word[2::2]
    if in_bisect(word_1,a_list) != None and \
    in_bisect(word_2,a_list) != None and in_bisect(word_3,a_list) != None:
        return True
    else:
        return False
    
def print_three_way_pairs(a_list):
    for word in a_list:
        if is_interlock(word,a_list):
            print(word[::2],word[1::2],word[2::2],word) 
            
print('Three-way-interlock pairs are:')
print_three_way_pairs(word_list)
