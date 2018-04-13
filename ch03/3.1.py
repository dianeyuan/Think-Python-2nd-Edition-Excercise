# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 16:40:15 2018

@author: ASUS
"""

def right_justify(s):
    str_len = len(s)
    space_len = 70 - str_len
    print(' '*space_len+s)
    
string = 'monty'
right_justify(string)