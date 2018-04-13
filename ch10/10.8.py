# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 16:12:42 2018

@author: ASUS
"""

import random

# make a list with random birthdays
def random_bday(num):
    l = []
    for i in range(num):
        bday = random.randint(1,365)
        l.append(bday)
    return l

# check if the list has duplicates       
def has_duplicates(a_list):
    for i in a_list:
        if a_list.count(i) > 1:
            return True
    return False

# get the probability
def prob(num, times):
    
    count = 0
    for i in range(times):
        sample = random_bday(num)
        if has_duplicates(sample):
            count += 1
    prob = count / times
    return prob

num = 23
times = 1000
print('The probability that 2 of {} students have the same birthday is {}'.\
      format(num,prob(num,times)))


            
    
    
        