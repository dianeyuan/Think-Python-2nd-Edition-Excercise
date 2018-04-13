# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 08:14:51 2018

@author: ASUS
"""

from turtle import *

def petal(r,angle):
    for i in range(2):
        circle(r,angle)
        left(180-angle)

   
def flower(n,r,angle):
    # draw petal in n times
    for i in range(n):
        # draw a petal
        petal(r,angle)
        left(360/n)

# draw flower with 7 petals
penup()
backward(200)
pendown()
flower(7,60,50)

# draw flower with 10 petals
penup()
forward(150)
pendown()
flower(10,80,40)
  
# draw flower with 20 petals       
penup()
forward(150)
pendown()
flower(20,100,30)

done()      