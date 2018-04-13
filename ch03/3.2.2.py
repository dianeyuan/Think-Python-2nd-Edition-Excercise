# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 17:11:16 2018

@author: ASUS
"""

def do_twice(f,v):
    f(v)
    f(v)
    
def print_twice(bruce):
    print(bruce)
    print(bruce)
    
do_twice(print_twice,'spam')   


def do_four(f,v):
    do_twice(f,v)
    do_twice(f,v)
    