# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 15:19:13 2018

@author: ASUS
"""

import math
r = 5
volume = 4/3*math.pi*(r**3)
print('The volume is {:.2f}'.format(volume))

price = 24.95
discount = 0.4
num = 60
total = price*(1-discount)*num + 3+0.75*(num-1)
print('Total price is {:.2f}'.format(total))

easy_pace=8+15/60.0
tempo=7+12/60.0
running_time=easy_pace*1+tempo*3+easy_pace*1  # in minutes
start_time = 6*60+52  # in minutes
end_time = start_time + running_time  
print('End time is {:.0f}:{:.0f}'.format(end_time//60,end_time% 60)) 


