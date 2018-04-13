# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 11:12:43 2018

@author: ASUS
"""

def check_fermat(a,b,c,n):
    if n > 2 and a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that does not work.')
        
def start_check():
    a = int(input('Enter an interger:'))
    b = int(input('Enter an interger:'))
    c = int(input('Enter an interger:'))
    n = int(input('Enter an interger bigger than 2:'))
    check_fermat(a,b,c,n)
    
start_check()
    