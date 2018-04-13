# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 07:49:41 2018

@author: ASUS
"""

from turtle import *

def square(length):
    for i in range(4):
        forward(length)
        left(90)
        
square(50)
done()