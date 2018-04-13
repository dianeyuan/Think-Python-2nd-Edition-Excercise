# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 08:51:38 2018

@author: ASUS
"""

from turtle import *
import math

def triangle(l,angle):
    bottom_l = 2*l*math.sin(math.radians(angle/2))
    forward(l)
    left(90+angle/2)
    forward(bottom_l)
    left(90+angle/2)
    forward(l)

def pie(length,n):
    angle = 360/n
    # draw n triangles
    for i in range(n):
        triangle(length,angle)
        right(180)
        
# draw 5 pies
penup()
backward(200)
pendown()        
pie(50,5)

# draw 6 pies
penup()
forward(200)
pendown()        
pie(50,6)

# draw 7 pies
penup()
forward(200)
pendown()        
pie(50,7)

done()