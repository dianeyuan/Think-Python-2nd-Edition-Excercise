# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 12:31:16 2018

@author: ASUS
"""

def is_abecedarian(word):
    for i in range(len(word)-1):
        if ord(word[i]) > ord(word[i+1]):
            return False
    return True

# true
print(is_abecedarian('deep'))

# false
print(is_abecedarian('depth'))

file = open('words.txt')
count = 0
for line in file:
    word = line.strip()
    if is_abecedarian(word):
        count +=1
print('The total number of abecedarian words is {}.'.format(count))
        
            
    
    