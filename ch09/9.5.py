# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 12:24:48 2018

@author: ASUS
"""

def uses_all(word,string):
    for char in string:
        if char not in word:
            return False
    return True

# true
print(uses_all('banana','abn'))
# false
print(uses_all('banana','abmn'))

def count(string):
    count = 0
    file = open('words.txt')
    for line in file:
        word = line.strip()
        if uses_all(word,string):
            count += 1
            
    return count

print(count('aeiou'))
print(count('aeiouy'))

            