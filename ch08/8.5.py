# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 10:51:06 2018

@author: ASUS
"""

def rotate_word(string,num):
    
    res = ''
    if string.islower():
 
        for char in string:
            new_char = chr(ord('a')+(ord(char)-ord('a')+num)%26)
            res += new_char
        return res
            
    if string.isupper():
        for char in string:
            new_char = chr(ord('A')+(ord(char)-ord('A')+num)%26)
            res += new_char
        return res
    else:
        return 'error!enter lower or upper string.'
  
        
print(rotate_word('cheer',7))
print(rotate_word('melon',-10))
print(rotate_word('IBM',-1))

        