# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:51:27 2019

@author: huyn
"""

#3Sum
from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    for index,num in enumerate(nums):
        start,stop = 0,len(nums)-1
        while start<stop:
            