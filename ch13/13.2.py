# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 11:24:10 2018

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

def sum_of_words(a_dict):
    return sum(a_dict.values())

file = open('pride2.txt')
word_dict = read_file(file)
file.close

print('The sum of the words is: {}'.format(sum_of_words(word_dict)))
print(word_dict)



        
    
