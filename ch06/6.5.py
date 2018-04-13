# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 12:31:41 2018

@author: ASUS
"""

def gcd(a,b):
    if b==0:
        return a
    else:
        r = a%b
        return gcd(b,r)
    
print(gcd(6,4))
print(gcd(10,15))