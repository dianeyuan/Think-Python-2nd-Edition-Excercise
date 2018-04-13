# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 07:52:17 2018

@author: ASUS
"""

from turtle import *

def polygon(length,n):
    for i in range(n):
        forward(length)
        left(360/n)
        
polygon(50,6)
done()