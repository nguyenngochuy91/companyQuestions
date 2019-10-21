# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:34:56 2019

@author: huyn
"""

#Next Closest Time
#Given a time represented in the format "HH:MM", form the next closest time by 
#reusing the current digits. There is no limit on how many times a digit can be reused.
#
#You may assume the given input string is always valid. For example, "01:34", "12:09" 
#are all valid. "1:34", "12:9" are all invalid.
import itertools
def nextClosestTime(time: str) -> str:
    value = int(time[0]+time[1])*60+int(time[3]+time[4])
    mySet = set()
    mySet.add(time[0])
    mySet.add(time[1])
    mySet.add(time[3])
    mySet.add(time[4])
    perm = itertools.product(mySet,repeat = 4)
    myMin = float("inf")
    res = None
    for potential in perm:
        val = isValid(potential)
        if val != None:
            if value <val:
                if val - value < myMin:
                    myMin = val - value
                    res   = "{}:{}".format(potential[0]+potential[1],potential[2]+potential[3])
            else:
                extra = 24*60 - value + val
                if extra < myMin:
                    myMin = extra
                    res   = "{}:{}".format(potential[0]+potential[1],potential[2]+potential[3])
                    
    return res
def isValid(potential):
    hour = int(potential[0]+potential[1])
    minute = int(potential[2]+potential[3])
    if hour<24:
        if minute<60:
            return hour*60+minute
    return None
time = "19:34"
time = "23:59"