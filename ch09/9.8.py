# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 13:51:28 2018

@author: ASUS
"""
def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


for i in range(100000,1000000):
    last_four = str(i)[2:]
    last_five = str(i+1)[1:]
    middle_four = str(i+2)[1:5]
    all_six = str(i+3)
    if is_palindrome(last_four) and is_palindrome(last_five) and \
    is_palindrome(middle_four) and is_palindrome(all_six):
        print(i)
    
    