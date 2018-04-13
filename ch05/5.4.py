# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 11:26:11 2018

@author: ASUS
"""

def recurse(n,s):
    if n == 0:
        print (s)
    else :
        recurse(n-1,n+s)

recurse(3, 0)


