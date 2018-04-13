# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 11:52:54 2018

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

def snowflake(x):
    for i in range(3):
        koch(x)
        right(120)

        
snowflake(40)

done()