# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 17:18:52 2018

@author: ASUS
"""

def make_key(word):
    t = str(sorted(list(word)))
    return t

def make_dict():
    # make a dict with sorted strings as keys, anagrams as values
    d = dict()
    file = open('words.txt')
    for line in file:
        word = line.strip().lower()
        key = make_key(word)
        if key not in d:
            d[key] = [word]
        else:
            d[key].append(word)
            
    file.close()
    return d

def is_meta(word_1,word_2):
    count = 0
    if word_1 != word_2 and len(word_1) == len(word_2):
        for i in range(len(word_1)):
            if word_1[i] != word_2[i]:
                count += 1
        if count == 2:
            return True
    else:
        return False


def print_meta_pairs(d):    
    # print anagram pairs       
    for key in d:
        if len(d[key])>1:
            for i in range(len(d[key])):
                for j in range(i+1,len(d[key])):
                    if is_meta(d[key][i],d[key][j]):
                        print(d[key][i],d[key][j])
                        
word_dict = make_dict()
print_meta_pairs(word_dict)
            