# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 11:48:40 2019

@author: Huy Nguyen
"""

#Product of Array Except Self
from typing import List
def productExceptSelf(nums: List[int]) -> List[int]:
    # consider array [1,2,3,4,5]
    # accumulate from left [1,1,1*2,1*2*3,1*2*3*4]
    # accumulate from right [2*3*4*5,3*4*5,4*5,5,1]
    left = [1]
    for i in range(len(nums)-1):
        left.append(left[-1]*nums[i])
    right = [1]
    for i in range(len(nums)-1,0,-1):
        right.append(right[-1]*nums[i])
    
    res = []
    for i in range(len(nums)):
        j = len(nums)-i-1
        res.append(left[i]*right[j])
    return res