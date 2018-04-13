# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 11:41:58 2018

@author: ASUS
"""

def make_dict():
    d = dict()
    file = open('words.txt')
    for line in file:
        word = line.strip().lower()
        d[word] = 1
    file.close()
    return d

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
    
def print_rotate_pairs(a_dict):
    for word in a_dict:
        for i in range(1,14):
            rotated = rotate_word(word,i)
            if rotated in a_dict:
                print('{} rotated by {} is {}'.format(word,i,rotated))
                
                
word_dict = make_dict()
print_rotate_pairs(word_dict)
        
    
    
  