# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 11:34:31 2018

@author: ASUS
"""
import turtle
def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd( length *n)
    t.lt( angle )
    draw(t,length,n-1)
    t.rt(2* angle )
    draw(t,length,n-1)
    t.lt( angle )
    t.bk( length *n)

bob = turtle.Turtle()
draw(bob, 5 ,6)
turtle.done()