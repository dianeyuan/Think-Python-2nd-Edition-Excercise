# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 13:19:19 2018

@author: ASUS
"""

def read_dictionary(filename='c06d'):
    """Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.

    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".

    filename: string
    returns: map from string to pronunciation
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': 
            continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron
    
    fin.close()
    return d

def solve_puzzle(a_dict):
    for word in a_dict:
        if len(word) == 5:
            pron = a_dict[word]
            remove_1 = word[1:]
            remove_2 = word[0]+word[2:]
            if remove_1 in a_dict and remove_2 in a_dict and \
            a_dict[remove_1] ==pron and a_dict[remove_2] == pron:
                print(word)
                
pron_dict = read_dictionary()
solve_puzzle(pron_dict)
            
            
            
        
        
    
