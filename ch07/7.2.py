# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 09:50:28 2018

@author: ASUS
"""
def eval_loop():
    while True:
        n = input('>')
        if n == 'done':
            break
        else:
            result = eval(n)
            print(result)
    print(result)

eval_loop()
    
        
        