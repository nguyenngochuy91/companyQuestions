# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 04:19:44 2019

@author: huyn
"""
from typing import List
def nextPermutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(len(nums)-1,0,-1):
        if nums[i]>nums[i-1]:
            # we find on the right hand of i, for the minimal number that is greater than nums[i-1]
            minimum = float("inf")
            chosen  = None
            for index in range(len(nums)-1,i-1,-1):
                if nums[index]<minimum and nums[index]>nums[i-1]:
                    minimum,chosen = nums[index],index
            nums[i-1],nums[chosen] = nums[chosen],nums[i-1]
            nums[i:].sort()
            return 
    nums.sort()
    return