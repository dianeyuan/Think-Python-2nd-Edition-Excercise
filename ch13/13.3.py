# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 11:52:04 2018

@author: ASUS
"""
import string

def process_line(line, a_dict): 
    # for each line, add the word to dict and count it.
    line = line.replace('-',' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace).lower()
        a_dict[word] = a_dict.get(word,0)+1
    

def read_file(file):
    d = dict()
    
    # for each line, add the word to dict and count it.
    for line in file:
        process_line(line, d)
        
    return d

def most_frequent(a_dict):
    h = []
    for key in a_dict:
        h.append((a_dict[key],key))
        
    h.sort(reverse = True)
    return h

file = open('pride2.txt')
word_dict = read_file(file)
h = most_frequent(word_dict)
file.close

print('The 20 most frequent words are:\n {}'.format(h[:20]))

        
    
    
  
    