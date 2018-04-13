# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 11:08:18 2018

@author: ASUS
"""

file = open('words.txt')
for line in file:
    word = line.strip()
    if len(word) > 20:
        print(word)