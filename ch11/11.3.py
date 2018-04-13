# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 11:05:34 2018

@author: ASUS
"""
known = {(0,0):1,(1,0):2}

def ackermann(m,n):
    if (m,n) in known:
        return known[(m,n)]
    else:
        if m == 0:
            res = n+1

        elif m > 0  and n==0:
            res = ackermann(m-1,1)

        elif m > 0 and n > 0:
            res = ackermann(m-1,ackermann(m,n-1))
          
        known[(m,n)] = res
        return res
   
    
print(ackermann(0,0))
print(ackermann(3,2))
print(known)
    
        
    