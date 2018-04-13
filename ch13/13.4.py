# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 12:09:02 2018

@author: ASUS
"""
import string

def process_line(line, a_dict): 
    # for each line, add the word to dict and count it.
    line = line.replace('-',' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        
        word = word.lower()
        a_dict[word] = a_dict.get(word,0)+1
    

def read_file(file):
    d = dict()
    
    # for each line, add the word to dict and count it.
    for line in file:
        process_line(line, d)
        
    return d


def make_dict():
    d = dict()
    file = open('words.txt')
    for line in file:
        word = line.strip().lower()
        d[word] = 1
    file.close()
    return d

word_dict = make_dict()

file = open('emma2.txt')
d = read_file(file)
print(d)
for word in d:
    if word not in word_dict:
        print(word, end = ' ')
        
