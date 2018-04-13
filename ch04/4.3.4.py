# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 07:55:47 2018

@author: ASUS
"""

from turtle import *
import math

def polygon(length,n):
    for i in range(n):
        forward(length)
        left(360/n)
        
def circle(r):
    n = 50
    length = 2*math.pi*r/n
    polygon(length,n)
    
circle(60)
done()