# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 15:01:53 2018

@author: ASUS
"""

seconds = 42*60+42
miles = 10/1.61
print(seconds)
print(miles)

pace = seconds/miles
print('The pace is {:.0f} minutes and {:.0f} seconds.'.format(pace//60,pace % 60))

hours = seconds/3600
speed = miles/hours
print('The speed is {:.2f} miles per hour.'.format(speed))

