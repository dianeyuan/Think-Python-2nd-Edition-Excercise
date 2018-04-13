# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 12:49:26 2018

@author: ASUS
"""

def consecutive(word):
    if len(word) < 6:
        return False
    else:
        for i in range(len(word)-5):
            if word[i]==word[i+1] and word[i+2]==word[i+3] and \
            word[i+4]==word[i+5]:
                return True
        return False
# true  
print(consecutive('abccddee'))
# false
print(consecutive('committee'))

file = open('words.txt')

for line in file:
    word = line.strip()
    if consecutive(word):
        print(word)
    