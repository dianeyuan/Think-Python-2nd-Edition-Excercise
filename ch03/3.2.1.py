# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 17:01:51 2018

@author: ASUS
"""

def do_twice(f):
    f()
    f()
    
def print_spam():
    print('spam')
    
do_twice(print_spam)