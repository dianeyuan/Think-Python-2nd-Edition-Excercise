# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 12:15:54 2018

@author: ASUS
"""

def uses_only(word,string):
    for char in word:
        if char not in string:
            return False
    return True

# should be true
print(uses_only('banana','abmn')) 

# should be false
print(uses_only('apple','ael'))

# should be true
print(uses_only('helloface','acefhlo'))

