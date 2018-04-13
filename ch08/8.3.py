# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 10:49:38 2018

@author: ASUS
"""

def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome('noon'))
print(is_palindrome('redivider'))
print(is_palindrome('apple'))