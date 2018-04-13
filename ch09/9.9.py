# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 14:01:19 2018

@author: ASUS
"""

def is_reverse(num_1,num_2):
    if str(num_1).zfill(2)[::-1] == str(num_2):
        return True
    else:
        return False
    
# true
print(is_reverse(37,73))
# false
print(is_reverse(37,72))

for gap in range(12,60):
    count = 0
    for i in range(1,90):
        if is_reverse(i,i+gap):
            count +=1
            
            if count == 6:
                res = i
                
            if count == 8:
                print('current age:{}'.format(res))
                break
    