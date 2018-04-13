# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 11:23:53 2018

@author: ASUS
"""

def avoids(str_1,str_2):
    for char in str_2:
        if char in str_1:
            return False
    
    return True

    
print(avoids('python','vb'))
print(avoids('python','th'))

def print_avoids():
    string = input('enter a string:\n')
    file = open('words.txt')
    count = 0
    for line in file:
        word = line.strip()
        if avoids(word,string):
            count += 1
    print('The total words that avoid {} is {}'.format(string,count))
    
print_avoids()
            
        

