# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 11:56:47 2018

@author: ASUS
"""

def ack(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1,ack(m,n-1))
    
print(ack(3,4))
