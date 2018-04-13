# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 11:03:28 2018

@author: ASUS
"""

import time
current = time.time()
print(current)

seconds = current % 60
minutes = current // 60
hours = current // 3600
days = current // (3600*24)

print('It has been {:.0f} days {:.0f} hours {:.0f} minutes and {:.0f} seconds since \
      the epoch.'.format(days,hours,minutes,seconds))