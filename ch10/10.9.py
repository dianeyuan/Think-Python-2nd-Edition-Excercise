# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 16:55:49 2018

@author: ASUS
"""

import time

def fun_1():
    l = []
    file = open('words.txt')
    for line in file:
        word = line.strip()
        l.append(word)
    file.close()
    return l

def fun_2():
    t = []
    file = open('words.txt')
    for line in file:
        word = line.strip()
        t = t + [word]
    file.close()
    return t


start_1 = time.time()
fun_1()
end_1 = time.time()
print('Function 1 takes {:.5f} seconds'.format(end_1-start_1))

# fun_2 takes a longer time
start_2 = time.time()
fun_2()
end_2 = time.time()
print('Function 2 takes {:.5f} seconds'.format(end_2-start_2))
