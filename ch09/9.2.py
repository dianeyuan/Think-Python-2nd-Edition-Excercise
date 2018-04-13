# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 11:16:16 2018

@author: ASUS
"""

def has_no_e(word):
    if 'e' not in word:
        return True
    else:
        return False
    
print(has_no_e('banana'))
print(has_no_e('apple'))

def print_no_e(word):
    count = 0
    for char in word:
        if char != 'e':
            print(char)
            count += 1
            
    print('The percentage of letters other than e is {:.2f}'.format(count/len(word)))
    
print_no_e('banana')
print_no_e('apple')