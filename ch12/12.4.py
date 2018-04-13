# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 18:08:07 2018

@author: ASUS
"""

def make_dict():
    d = dict()
    file = open('words.txt')
    for line in file:
        word = line.strip().lower()
        d[word] = 1
    file.close()
    
    for k in ['a','i','']:
        d[k] = 1
        
    return d

d = make_dict()

def children(word):
    # get a list of all the child words of a word
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        if child in d:
            res.append(child)
            
    return res

# initialize the memo
memo = {'':['']}

def is_reducible(word):
    ''' check if the word is reducible , return its children if yes, return 
    an empty list if no'''
    
    if word in memo:
        return memo[word]
    
    res = []
    for child in children(word):
        if is_reducible(child):
            res.append(child)
            
    memo[word] = res
    return res

def get_reducible(a_dict):
    ''' iterate through the dict and make a list of words that is reducible'''
    result = []
    for word in a_dict:
        t = is_reducible(word)
        if t != []:            
            result.append(word)
            
    return result

def print_trail(word):
    if len(word) == 0:
        return
    print(word, end = ' ')
    
    t = is_reducible(word)
    print_trail(t[0])
    
def print_longest_words():
    redu_words = get_reducible(d)
    reverse = []
    for word in redu_words:
        reverse.append((len(word),word))
        
    reverse.sort(reverse = True)
    
    for i in range(5):
        print_trail(reverse[i][1])
        
        
print_longest_words()
        
    
        


        
        
        
    
        
            
    