# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:02:38 2019

@author: huyn
"""

#283. Move Zeroes
#
#Given an array nums, write a function to move all 0's to the end of it while 
#maintaining the relative order of the non-zero elements.
from typing import List
def moveZeroes(nums: List[int]) -> None:
    start,stop = 0,0
    while stop<len(nums):
        if nums[stop]!=0:
            while start<stop and nums[start]!=0:
                start+=1
            if nums[start]==0:
                # we swap start, stop
                nums[start],nums[stop]=nums[stop],nums[start]
                start+=1
        stop+=1
    return
nums =[0,1,0,3,12]
moveZeroes(nums)
print (nums)
