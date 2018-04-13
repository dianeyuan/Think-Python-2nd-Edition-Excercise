# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 12:20:56 2018

@author: ASUS
"""

def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome('noon'))
print(is_palindrome('redivider'))
print(is_palindrome('apple'))