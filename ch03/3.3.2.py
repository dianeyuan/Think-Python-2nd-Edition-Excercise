# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 17:32:38 2018

@author: ASUS
"""

def horizonal_line():
    print('+'+'-'*4+'+'+'-'*4+'+'+'-'*4+'+'+'-'*4+'+')
    
def vertical_line():
    print('|'+' '*4+'|'+' '*4+'|'+' '*4+'|'+' '*4+'|')
    
def grid_4():
    for i in range(4):
        horizonal_line()
        for j in range(4):
            vertical_line()
    horizonal_line()
    
grid_4()
