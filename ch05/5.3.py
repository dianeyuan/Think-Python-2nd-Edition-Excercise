# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 11:20:03 2018

@author: ASUS
"""

def is_triangle(a,b,c):
    if a>(b+c) or b>(a+c) or c>(a+b):
        print('No')
    else:
        print('Yes')
        
is_triangle(2,3,5)

def check_triangle():
    a = int(input('Enter an interger:'))
    b = int(input('Enter an interger:'))
    c = int(input('Enter an interger:'))
    
    is_triangle(a,b,c)
    
check_triangle()