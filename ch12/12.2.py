# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 16:26:35 2018

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
    
def print_pairs(d):    
    # print anagram pairs       
    for key in d:
        if len(d[key])>1:
            print(d[key])
 

def reverse_print(d):
    pair_list = []
    print('print the anagram pairs in reverse order:')
    for key in d:
        if len(d[key]) > 1:
            pair_list.append((len(d[key]),d[key]))
            
    pair_list.sort(reverse = True)
    for item in pair_list:
        print(item[1])
        
def bingo(d):
    for key in d:
        if len(d[key]) == 8:
            print(d[key])
        
d = make_dict()

print_pairs(d)
reverse_print(d) 
bingo(d)   

    
            
            
        
    
    

    
            
    
            
    