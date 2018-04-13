# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 11:44:39 2018

@author: ASUS
"""

from turtle import *

def koch(x):
    if x<3:
        forward(x)
    else:
        y = x/3
        koch(y)
        left(60)
        koch(y)
        right(120)
        koch(y)
        left(60)
        koch(y)
    
koch(30)
done()