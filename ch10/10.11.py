# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 17:33:47 2018

@author: ASUS
"""
import bisect

def in_bisect(a_list,x):
    i = bisect.bisect_left(a_list, x)
    if i != len(a_list) and a_list[i] == x:
        return i
    return None

    
def make_list():
    l = []
    file = open('words.txt')
    for line in file:
        word = line.strip()
        l.append(word)
    file.close()
    return l


def print_pairs(a_list):
    for item in a_list:
        # check if the reverse of the word is in the list
        if in_bisect(a_list,item[::-1]) != None:
            print(item, item[::-1])

                
word_list = make_list()
print_pairs(word_list)
    
    

            