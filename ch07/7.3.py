# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 10:29:11 2018

@author: ASUS
"""
import math

def estimate_pi():
    total = 0
    k = 0
    coefficient = 2 * math.sqrt(2) / 9801
    
    while True:
        den = math.factorial(k)**4.0 * (394.0**(4.0*k))
        num = math.factorial(4.0*k) * (1103.0 + (26390.0*k))
        interim_sum =  coefficient * (num/den) 
        total = total + interim_sum
        if abs(interim_sum) < 1e-15:
            break
        k = k + 1
    return 1 / total


print(estimate_pi())
print(math.pi)
        