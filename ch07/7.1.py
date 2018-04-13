# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:13:56 2018

@author: ASUS
"""

import math

def mysqrt(a):
    x = 3
    while True:
        y = (x + a/x)/2
        if abs(y-x) < 0.0000001:
            break
        x = y
        
    return y

def test_square_root():
    print('{:<4}{:<10}{:<15}{:<4}'.format('a','mysqrt(a)','math.sqrt(a)','diff'))
    print('{:<4}{:<10}{:<15}{:<4}'.format('-','-'*8,'-'*12,'-'*4))
    for i in range(1,10):
        print('{:<4}{:<10f}{:<15f}{:<4}'.format(i*1.0,mysqrt(i),math.sqrt(i),\
              mysqrt(i)-math.sqrt(i)))
        
     
test_square_root()    

    