# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 20:20:42 2018

@author: ASUS
"""
import string
def print_words(file):
   
    for line in file:
        for char in string.punctuation:
            line = line.replace(char,'').lower().strip()
        print(line)
        
file = open('emma2.txt')
print_words(file)
file.close()
        
        